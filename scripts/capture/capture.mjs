#!/usr/bin/env node
// Unslop capture: renders a web artifact and writes evidence for the sweep.
// usage: node capture.mjs <url-or-file> <run-dir> [--widths 375,1440] [--bless-control] [--skip-control]
//        [--no-motion] [--no-async] [--no-interact] [--motion-budget 60000] [--async-budget 60000] [--passive <ms>] [--stress] [--slow]
// Writes <run-dir>/01-evidence/: shot-<w>.png, bg-<w>.png, fold-<w>.png, dom-<w>.json, fonts.json,
// hidden.json, focus.json + focus/*.png, forms.json, perf.json, motion.json + motion/*.png, async.json + async/*.png, manifest.json
import { createRequire } from "node:module";
const { chromium } = createRequire(import.meta.url)("playwright");
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { installShim } from "./netshim.mjs";
import { captureMotion, captureAsync, capturePassive } from "./interact.mjs";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, "../..");
const EXTRACT = fs.readFileSync(path.join(HERE, "extract.js"), "utf8");
const HEIGHTS = { 320: 568, 375: 812, 414: 896, 768: 1024, 1024: 768, 1280: 800, 1440: 900, 1920: 1080 };
const BG_ALL = true;   // background-only render at every captured width (fixed-canvas media have one width)

const args = process.argv.slice(2);
const flag = (n) => args.includes(n);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : d; };
const VALUED = ["--widths", "--motion-budget", "--async-budget", "--isolate"];
const [target, runDir] = args.filter((a, i) => !a.startsWith("--") && !(i > 0 && VALUED.includes(args[i - 1])));
if (!target || !runDir) { console.error("usage: capture.mjs <url-or-file> <run-dir> [--widths 375,1440]"); process.exit(2); }
const widths = opt("--widths", "320,375,414,768,1024,1280,1440,1920").split(",").map(Number);
const toUrl = (t) => { if (/^https?:|^file:/.test(t)) return t; const [f, q] = t.split("?"); return pathToFileURL(path.resolve(f)).href + (q ? "?" + q : ""); };
const url = toUrl(target);
const ev = path.join(runDir, "01-evidence");
fs.mkdirSync(path.join(ev, "focus"), { recursive: true });
const log = [];
const note = (m) => { log.push(m); console.error(m); };
// later passes: wait for load, else fall back to DOMContentLoaded (slow third-party loads must not end the capture)
async function goLoad(page, url, pass) {
  try { await page.goto(url, { waitUntil: "load", timeout: 45000 }); }
  catch (e) { note(`${pass}: load event not reached (${e.message.split(String.fromCharCode(10))[0].slice(0, 80)}); continuing after DOMContentLoaded`);
    try { await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 }); } catch {} }
}

async function settle(page, { wheel = false } = {}) {
  try { await page.waitForLoadState("networkidle", { timeout: 15000 }); } catch { note("networkidle timeout; continuing after load"); }
  await page.evaluate(() => document.fonts && document.fonts.ready);
  await page.evaluate(async () => {           // trigger lazy content, then return to top
    const step = innerHeight * 0.8;
    for (let y = 0; y < document.documentElement.scrollHeight; y += step) { scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
    scrollTo(0, 0);
  });
  // Real wheel pass: reveal-on-scroll observers and smooth-scroll libraries ignore instant scrollTo, which left blank
  // bands in live captures (live round 1: L10, L16, L18, L20, L28, L36). Reveal-once content stays visible afterwards.
  if (wheel) try {
    const vp = page.viewportSize(), t0 = Date.now();      // budget: 30 s per pass, so long pages cannot stall the capture
    await page.mouse.move(vp.width / 2, vp.height / 2);
    for (let i = 0; i < 80; i++) {
      const [bottom, H] = await page.evaluate(() => [scrollY + innerHeight, document.documentElement.scrollHeight]);
      if (bottom >= H - 2 || Date.now() - t0 > 30000) break;
      await page.mouse.wheel(0, Math.round(vp.height * 0.66)); await page.waitForTimeout(250);
    }
    await page.waitForTimeout(800);
    for (let i = 0; i < 80 && (await page.evaluate(() => scrollY)) > 0; i++) { await page.mouse.wheel(0, -1500); await page.waitForTimeout(80); }
    await page.evaluate(() => scrollTo(0, 0));
  } catch (e) { note(`wheel pass failed: ${e.message}`); }
  await page.waitForTimeout(600);
}

// Settle animations so the DOM dump, the shot and the bg render are one frame: one-off animations jump to their end
// state (what a visitor sees after a reveal), infinite ones stop where they are. Live round 1: the bg render caught a
// later frame than the shot (L26 calendar chip 1.00:1, "Join" at opacity .35 mid-fade, L14 ticker, L28 icon swap).
async function settleAnimations(page) {
  try {
    return await page.evaluate(() => {
      let finished = 0, paused = 0;
      for (const a of document.getAnimations()) {
        try {
          if (a.effect && a.effect.getComputedTiming().iterations === Infinity) { a.pause(); paused++; }
          else { a.finish(); finished++; }
        } catch { /* finish() throws on an infinite or zero-rate animation: pause it instead */ try { a.pause(); paused++; } catch {} }
      }
      return { finished, paused };
    });
  } catch (e) { return { error: e.message }; }
}

// Per-host page preparation for live captures (page-prep.json): cookie banners, interstitials, tool overlays, extra settle.
// Every action is logged and lands in manifest.prep, so a capture never silently differs from what a visitor sees.
const PREP_HOSTS = JSON.parse(fs.readFileSync(path.join(HERE, "page-prep.json"), "utf8")).hosts;
const PREP_HOST = (() => { try { return new URL(url).hostname.replace(/^www\./, ""); } catch { return ""; } })();
const PREP = PREP_HOSTS[PREP_HOST] || null;
const prepLog = new Set();
// --isolate '<json>': a test set shows one half of a controlled pair (evals/testset/set2.yaml). Not for audits.
// {"remove": [selectors], "pair": {"parent": selector, "child": selector, "keep": n}}: matching nodes are removed from
// the DOM as soon as they appear (not hidden: hidden text would still reach the DOM dump and the hidden-content test).
const ISOLATE = opt("--isolate", null);
function isolatePage(spec) {
  const S = JSON.parse(spec), done = new WeakSet();
  const run = () => {
    for (const sel of S.remove || []) document.querySelectorAll(sel).forEach((e) => e.remove());
    if (S.pair) for (const p of document.querySelectorAll(S.pair.parent)) {
      if (done.has(p)) continue;
      const kids = [...p.children].filter((c) => c.matches(S.pair.child));
      if (kids.length < 2) continue;
      done.add(p);
      kids.forEach((c, i) => { if (i + 1 !== S.pair.keep) c.remove(); });
    }
  };
  const start = () => { run(); new MutationObserver(run).observe(document.documentElement, { childList: true, subtree: true }); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
}
function prepPage(p) {
  const want = (p.click || []).map((l) => l.toLowerCase());
  const text = (p.clickText || "").toLowerCase();
  const norm = (s) => (s || "").replace(/\s+/g, " ").trim().toLowerCase();
  const seen = (e) => e.getClientRects().length > 0;
  let left = p.presses || 1, textDone = !text, busy = false;
  const tick = () => {
    if (busy) return;
    if (left > 0 && want.length) {
      const els = [...document.querySelectorAll("button, a, [role=button], input[type=button], input[type=submit]")];
      for (const lab of want) {
        const el = els.find((e) => norm(e.innerText || e.value) === lab && seen(e));
        if (el) { el.click(); left--; console.log(`[unslop-prep] clicked "${lab}"`); busy = true; setTimeout(() => { busy = false; tick(); }, 500); return; }
      }
    }
    if (!textDone) {
      const hits = [...document.body.querySelectorAll("*")].filter((e) => seen(e) && norm(e.innerText).includes(text));
      const el = hits.find((e) => ![...e.children].some((c) => hits.includes(c)));      // innermost match
      if (el) { el.click(); textDone = true; console.log(`[unslop-prep] clicked text "${text}"`); }
    }
  };
  const obs = new MutationObserver(tick);
  const start = () => { tick(); obs.observe(document.documentElement, { childList: true, subtree: true }); setTimeout(() => obs.disconnect(), 20000); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
}

async function open(browser, w, ctxOpts = {}) {
  const ctx = await browser.newContext({ viewport: { width: w, height: HEIGHTS[w] || 900 }, deviceScaleFactor: 1, ...ctxOpts });
  NETS.push(await installShim(ctx));
  if (PREP) {
    if (PREP.click || PREP.clickText) await ctx.addInitScript(prepPage, PREP);
    for (const b of PREP.block || []) await ctx.route((u) => u.href.includes(b), (route) => { prepLog.add(`blocked ${b}`); return route.abort(); });
  }
  if (ISOLATE) await ctx.addInitScript(isolatePage, ISOLATE);      // test-set isolation: recorded in manifest.isolate
  const page = await ctx.newPage();
  const errors = [];
  page.on("pageerror", (e) => errors.push(String(e.message || e)));
  page.on("console", (m) => {
    const t = m.text();
    if (t.startsWith("[unslop-prep] ")) { prepLog.add(`w${w}: ${t.slice(14)}`); return; }
    if (m.type() === "error") errors.push(t);
  });
  return { ctx, page, errors };
}

const NETS = [];
const browser = await chromium.launch();
const WITHHELD = flag("--withhold-target") ? "(withheld for blind review)" : null;   // test sets: the URL names the lesson
const manifest = { target: WITHHELD || target, url: WITHHELD || url, started: new Date().toISOString(), widths: [], files: {}, control: null, log };

// ---- 1. check the checker: render the known-good control first ----------------------------------
const controlPath = path.join(ROOT, "evals/seeded-defects/control.html");
const expectedPath = path.join(ROOT, "evals/seeded-defects/control.expected.json");
if (!flag("--skip-control") && fs.existsSync(controlPath)) {
  const { ctx, page } = await open(browser, 1440);
  await page.goto(pathToFileURL(controlPath).href);
  await settle(page);
  const got = await page.evaluate(() => ({ textChars: document.body.innerText.replace(/\s+/g, "").length, elements: document.body.querySelectorAll("*").length,
    fonts: [...document.fonts].filter(f => f.status === "loaded").length }));
  if (flag("--bless-control")) { fs.writeFileSync(expectedPath, JSON.stringify(got, null, 2)); note(`control blessed: ${JSON.stringify(got)}`); }
  const exp = fs.existsSync(expectedPath) ? JSON.parse(fs.readFileSync(expectedPath, "utf8")) : null;
  manifest.control = { ok: !!exp && exp.textChars === got.textChars && exp.elements === got.elements, expected: exp, got };
  if (!manifest.control.ok) note("CONTROL FAILED: renderer did not reproduce the known-good page; capture-based findings are not verified");
  await ctx.close();
} else manifest.control = { ok: false, skipped: true };

// ---- 2. per-width render, screenshots, DOM dump ----------------------------------------------------
for (const w of widths) {
  const { ctx, page, errors } = await open(browser, w);
  try { await page.goto(url, { waitUntil: "load", timeout: 45000 }); } catch (e) { note(`width ${w}: load failed: ${e.message}`); await ctx.close(); continue; }
  await settle(page, { wheel: true });
  if (PREP && PREP.wait) { await page.waitForTimeout(PREP.wait); prepLog.add(`w${w}: waited ${PREP.wait}ms`); }
  await page.addStyleTag({ content: "*,*::before,*::after{background-attachment:scroll!important}" });   // fixed backgrounds render once in full-page shots
  const anim = await settleAnimations(page);
  note(`w${w}: animations settled before DOM/shot: ${JSON.stringify(anim)}`);
  const dom = await page.evaluate(EXTRACT);
  dom.consoleErrors = errors;
  fs.writeFileSync(path.join(ev, `dom-${w}.json`), JSON.stringify(dom));
  await page.screenshot({ path: path.join(ev, `shot-${w}.png`), fullPage: true });
  if (HEIGHTS[w] && [1280, 1440, 1920, 375].includes(w)) await page.screenshot({ path: path.join(ev, `fold-${w}.png`) });
  if (PREP && PREP.scrollFrames) {      // scroll-driven page: the full-page shot is not what a visitor sees, so record viewport frames while wheel-scrolling
    const vh = HEIGHTS[w] || 900, total = await page.evaluate(() => document.documentElement.scrollHeight);
    let n = 0;
    for (let y = 0; n < PREP.scrollFrames && (n === 0 || y < total); y += vh, n++) {
      if (n) await page.mouse.wheel(0, vh);
      await page.waitForTimeout(1500);
      await page.screenshot({ path: path.join(ev, `scroll-${w}-${String(n).padStart(2, "0")}.png`) });
    }
    prepLog.add(`w${w}: ${n} scroll frames`);
    for (let i = 0; i < n; i++) { await page.mouse.wheel(0, -vh); await page.waitForTimeout(150); }
  }
  if (BG_ALL) {      // background-only render for real-pixel contrast
    // transition:none so text-fill turns transparent at once: AntD's `transition: all .3s` left ghost glyphs in the bg
    // render (live round 1: L33 tab, L34 menu). Animations are settled again because the scroll frames may restart them.
    const animBg = await settleAnimations(page);
    note(`w${w}: animations settled before bg render: ${JSON.stringify(animBg)}`);
    await page.addStyleTag({ content: "*,*::before,*::after{transition:none!important;animation-play-state:paused!important;-webkit-text-fill-color:transparent!important;text-shadow:none!important;-webkit-text-stroke:0!important;caret-color:transparent!important;text-decoration-color:transparent!important} svg text{fill:transparent!important}" });
    await page.waitForTimeout(100);
    await page.screenshot({ path: path.join(ev, `bg-${w}.png`), fullPage: true });
  }
  manifest.widths.push(w);
  await ctx.close();
}

// ---- 3. fonts that actually rendered (CDP), at 1440 -----------------------------------------------
{
  const { ctx, page } = await open(browser, 1440);
  await goLoad(page, url, "fonts pass"); await settle(page);
  await page.evaluate(EXTRACT);
  const cdp = await ctx.newCDPSession(page);
  await cdp.send("DOM.enable"); await cdp.send("CSS.enable");
  const { root } = await cdp.send("DOM.getDocument", { depth: -1 });
  const ids = await page.evaluate(() => [...document.querySelectorAll("[data-unslop-id]")]
    .filter(e => [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())).slice(0, 400).map(e => e.getAttribute("data-unslop-id")));
  const fonts = {};
  for (const id of ids) {
    try {
      const { nodeId } = await cdp.send("DOM.querySelector", { nodeId: root.nodeId, selector: `[data-unslop-id="${id}"]` });
      if (!nodeId) continue;
      const r = await cdp.send("CSS.getPlatformFontsForNode", { nodeId });
      fonts[id] = r.fonts.map(f => ({ family: f.familyName, glyphs: f.glyphCount, postscript: f.postScriptName }));
    } catch { /* node vanished */ }
  }
  fs.writeFileSync(path.join(ev, "fonts.json"), JSON.stringify(fonts));
  await ctx.close();
}

// ---- 4. three-condition hidden-content test -------------------------------------------------------
const VISIBLE_CHARS = () => {
  let vis = 0, tot = 0;
  for (const el of document.body.querySelectorAll("*")) {
    if (["SCRIPT", "STYLE", "NOSCRIPT", "TEMPLATE", "TITLE", "DESC", "title", "desc", "OPTION"].includes(el.tagName)) continue;
    if (el.closest("dialog,[role=dialog],[role=menu],[role=listbox],[role=tooltip],details:not([open]),[aria-hidden=true],[hidden]")) continue;
    let t = ""; for (const n of el.childNodes) if (n.nodeType === 3) t += n.textContent;
    const len = t.replace(/\s+/g, "").length; if (!len) continue;
    tot += len;
    const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) continue;
    let e = el, op = 1, ok = true;
    while (e && e.nodeType === 1) { const c = getComputedStyle(e); op *= parseFloat(c.opacity); if (c.display === "none" || c.visibility === "hidden") { ok = false; break; } e = e.parentElement; }
    if (ok && op >= 0.05) vis += len;
  }
  return { visibleChars: vis, totalChars: tot };
};
{
  const hidden = {};
  const conds = {
    baseline: { opts: {}, init: null, scroll: true },
    // reduced_motion scrolls like the baseline, so it tests "reduced motion breaks the reveal" and not "never scrolled"
    // (live round 1: L23 161 and L27 948 chars "lost" were below-fold content that only loads on scroll; slop L07/L09/L10 too).
    reduced_motion: { opts: { reducedMotion: "reduce" }, init: null, scroll: true },
    observer_never_fires: { opts: {}, init: () => { window.IntersectionObserver = class { constructor() {} observe() {} unobserve() {} disconnect() {} takeRecords() { return []; } }; }, scroll: false, wait: 4000 },
    scripts_off: { opts: { javaScriptEnabled: false }, init: null, scroll: false },
  };
  for (const [name, c] of Object.entries(conds)) {
    const { ctx, page } = await open(browser, 1440, c.opts);
    if (c.init) await page.addInitScript(c.init);
    try {
      await page.goto(url, { waitUntil: "load", timeout: 45000 });
      if (c.scroll) await settle(page, { wheel: true }); else await page.waitForTimeout(c.wait || 1200);
      hidden[name] = await page.evaluate(VISIBLE_CHARS);
    } catch (e) { hidden[name] = { error: e.message }; }
    await ctx.close();
  }
  fs.writeFileSync(path.join(ev, "hidden.json"), JSON.stringify(hidden, null, 1));
}

// ---- 5. focus walk at 1440 --------------------------------------------------------------------------
{
  const { ctx, page } = await open(browser, 1440);
  await goLoad(page, url, "focus pass"); await settle(page);
  await page.evaluate(EXTRACT);
  const stops = [];
  for (let i = 0; i < 40; i++) {
    await page.keyboard.press("Tab");
    await page.waitForTimeout(80);
    const info = await page.evaluate(() => {
      const a = document.activeElement;
      if (!a || a === document.body) return null;
      const r = a.getBoundingClientRect();
      // cover: is the focused element actually hidden by a fixed/sticky layer? A box-overlap test flagged skip links that
      // sit above the header, pointer-events:none transparent shells, visibility:hidden or opacity 0 overlays and a 48px
      // back-to-top button over a large tile (live round 1: 23 false "covered" on controls L23, L25, L27, L28, L33, L36).
      // 9 sample points of the focused rect are hit-tested; "full" = every in-view point is owned by a painted cover
      // (WCAG 2.4.11), "partial" = some (2.4.12), null = none.
      const painted = (e) => { const c = getComputedStyle(e); if (c.visibility !== "visible") return false;
        let op = 1; for (let x = e; x && x.nodeType === 1; x = x.parentElement) op *= parseFloat(getComputedStyle(x).opacity); return op > 0.05; };
      const covers = [...document.querySelectorAll("body *")].filter(e => { const p = getComputedStyle(e).position; return (p === "fixed" || p === "sticky") && !e.contains(a); })
        .filter(e => { const h = e.getBoundingClientRect(); return h.width > 0 && h.height > 0 && h.left < r.right && h.right > r.left && h.top < r.bottom && h.bottom > r.top; })
        .filter(painted);
      // a layer hides the focused element only if it is painted at that point: a background, a backdrop filter, or
      // content of its own (text, image, canvas, svg, video, form control). Transparent wrappers do not hide anything.
      const opaque = (e) => {
        const s = getComputedStyle(e);
        if (s.visibility !== "visible") return false;
        if (s.backgroundColor !== "rgba(0, 0, 0, 0)" && s.backgroundColor !== "transparent") return true;
        if (s.backgroundImage !== "none" || (s.backdropFilter && s.backdropFilter !== "none")) return true;
        if (/^(IMG|CANVAS|VIDEO|IFRAME|INPUT|BUTTON|SELECT|TEXTAREA)$/.test(e.tagName) || e instanceof SVGElement) return true;
        return [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      };
      let cover = null;
      if (covers.length) {
        // make pointer-events:none layers (and the focused element) hit-testable for the probe, then restore them
        const probe = [...covers, a], saved = probe.map(c => [c, c.style.getPropertyValue("pointer-events"), c.style.getPropertyPriority("pointer-events")]);
        probe.forEach(c => c.style.setProperty("pointer-events", "auto", "important"));
        let inview = 0, hidden = 0;
        for (const fx of [0.1, 0.5, 0.9]) for (const fy of [0.1, 0.5, 0.9]) {
          const x = r.left + r.width * fx, y = r.top + r.height * fy;
          if (x < 0 || y < 0 || x >= innerWidth || y >= innerHeight) continue;
          inview++;
          // walk the paint stack from the top down to the focused element: a transparent shell on top must not mask
          // a real header underneath, and layers below the focused element do not count
          for (const e of document.elementsFromPoint(x, y)) {
            if (e === a || a.contains(e)) break;
            if (covers.some(c => c.contains(e)) && opaque(e)) { hidden++; break; }
          }
        }
        saved.forEach(([c, v, p]) => v ? c.style.setProperty("pointer-events", v, p) : c.style.removeProperty("pointer-events"));
        cover = inview && hidden === inview ? "full" : hidden ? "partial" : null;
      }
      const cs = getComputedStyle(a);
      return { sel: a.getAttribute("data-unslop-id") ? `[data-unslop-id="${a.getAttribute("data-unslop-id")}"]` : a.tagName, tag: a.tagName.toLowerCase(),
        text: (a.innerText || a.value || a.getAttribute("aria-label") || "").trim().slice(0, 60), href: a.getAttribute("href"),
        rect: { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height }, cover, covered: cover !== null,      // `covered` kept for older readers
        outline: `${cs.outlineStyle} ${cs.outlineWidth} ${cs.outlineColor}`, boxShadow: cs.boxShadow };
    });
    if (!info) continue;
    if (stops.length && stops[0].sel === info.sel) break;      // wrapped around
    const pad = 8, clip = { x: Math.max(0, info.rect.x - pad), y: Math.max(0, info.rect.y - pad), width: Math.max(1, info.rect.w + 2 * pad), height: Math.max(1, info.rect.h + 2 * pad) };
    const n = String(stops.length).padStart(2, "0");
    try { await page.screenshot({ path: path.join(ev, "focus", `${n}-on.png`), fullPage: true, clip }); info.clip = clip; info.on = `focus/${n}-on.png`; } catch {}
    stops.push(info);
  }
  // matching "off" clips: same clips with nothing focused
  await page.evaluate(() => { document.activeElement && document.activeElement.blur(); scrollTo(0, 0); });
  await page.mouse.move(0, 0);
  await page.waitForTimeout(200);
  for (const [i, s] of stops.entries()) {
    if (!s.clip) continue;
    const n = String(i).padStart(2, "0");
    try { await page.screenshot({ path: path.join(ev, "focus", `${n}-off.png`), fullPage: true, clip: s.clip }); s.off = `focus/${n}-off.png`; } catch {}
  }
  fs.writeFileSync(path.join(ev, "focus.json"), JSON.stringify(stops, null, 1));
  await ctx.close();
}

// ---- 6. fake-send test: submit every form with the network blocked --------------------------------
{
  const { ctx, page } = await open(browser, 1440);
  await goLoad(page, url, "fake-send pass"); await settle(page);
  const count = await page.evaluate(() => document.querySelectorAll("form").length);
  // the default state of every checkbox and radio, before anything is filled: a preselected consent or add-on box is a
  // deceptive default (INT-018), and the fake-send fill below ticks every box, so forms.json cannot show it
  const choices = await page.evaluate(() => [...document.querySelectorAll("input[type=checkbox],input[type=radio],[role=checkbox],[role=switch]")].slice(0, 200).map((el) => {
    const r = el.getBoundingClientRect(), lab = (el.id && document.querySelector(`label[for="${CSS.escape(el.id)}"]`)) || el.closest("label");
    const text = ((lab && lab.innerText) || el.getAttribute("aria-label") || (el.parentElement && el.parentElement.innerText) || "").replace(/\s+/g, " ").trim().slice(0, 160);
    const checked = el.matches("input") ? el.checked : el.getAttribute("aria-checked") === "true";
    return { type: el.getAttribute("type") || el.getAttribute("role"), name: el.getAttribute("name"), checked, required: !!el.required, inForm: !!el.closest("form"),
      visible: r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== "hidden", label: text, id: el.getAttribute("data-unslop-id") };
  })).catch(() => []);
  fs.writeFileSync(path.join(ev, "choices.json"), JSON.stringify(choices, null, 1));
  const results = [];
  for (let i = 0; i < count; i++) {
    const p2 = await ctx.newPage();
    await goLoad(p2, url, "fake-send pass (form page)"); await p2.waitForTimeout(300);
    let attempted = 0;
    await p2.route("**/*", (route) => { attempted++; route.abort(); });
    const before = await p2.evaluate(() => document.body.innerText);
    const r = await p2.evaluate(async (i) => {
      const f = document.querySelectorAll("form")[i];
      for (const el of f.querySelectorAll("input,textarea,select")) {
        if (el.type === "email") el.value = "test@example.com";
        else if (el.type === "checkbox" || el.type === "radio") el.checked = true;
        else if (el.tagName === "SELECT") { if (el.options.length > 1) el.selectedIndex = 1; }
        else if (!["submit", "button", "hidden", "reset", "file"].includes(el.type)) el.value = el.type === "tel" ? "5550100" : el.type === "number" ? "1" : el.type === "url" ? "https://example.com" : "Test entry";
        el.dispatchEvent(new Event("input", { bubbles: true })); el.dispatchEvent(new Event("change", { bubbles: true }));
      }
      const btn = f.querySelector("button[type=submit],input[type=submit],button:not([type])");
      try { if (btn) btn.click(); else f.requestSubmit(); } catch (e) { return { error: String(e) }; }
      return { action: f.getAttribute("action"), button: btn ? (btn.innerText || btn.value) : null };
    }, i).catch(e => ({ error: e.message }));
    await p2.waitForTimeout(1500);
    let after = ""; try { after = await p2.evaluate(() => document.body.innerText); } catch { after = "[navigated]"; }
    const beforeLines = new Set(before.split("\n").map(s => s.trim()));
    const newText = after.split("\n").map(s => s.trim()).filter(s => s && !beforeLines.has(s));
    results.push({ index: i, ...r, requestsAttempted: attempted, newText });
    await p2.close();
  }
  fs.writeFileSync(path.join(ev, "forms.json"), JSON.stringify(results, null, 1));
  await ctx.close();
}

// ---- 7. performance (lab) at 1440 ----------------------------------------------------------------
{
  const { ctx, page } = await open(browser, 1440);
  await page.addInitScript(() => { window.__lcp = 0; new PerformanceObserver(l => { for (const e of l.getEntries()) window.__lcp = e.startTime; }).observe({ type: "largest-contentful-paint", buffered: true }); window.__cls = 0; window.__shifts = 0; try { new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) { window.__cls += e.value; window.__shifts++; } }).observe({ type: "layout-shift", buffered: true }); } catch {} });
  await goLoad(page, url, "performance pass"); await settle(page);
  const perf = await page.evaluate(() => ({ lcp: window.__lcp, cls: Math.round((window.__cls || 0) * 1000) / 1000, layoutShifts: window.__shifts || 0, resources: performance.getEntriesByType("resource").map(r => ({ name: r.name, type: r.initiatorType, bytes: r.encodedBodySize || r.transferSize || 0 })),
    images: [...document.images].map(i => ({ src: i.currentSrc || i.src, nw: i.naturalWidth, rw: Math.round(i.getBoundingClientRect().width), id: i.getAttribute("data-unslop-id") })) }));
  for (const r of perf.resources) if (!r.bytes && r.name.startsWith("file:")) { try { r.bytes = fs.statSync(fileURLToPath(r.name)).size; } catch {} }
  for (const im of perf.images) if (im.src && im.src.startsWith("file:")) { try { im.bytes = fs.statSync(fileURLToPath(im.src)).size; } catch {} }
  for (const im of perf.images) { const r = perf.resources.find(x => x.name === im.src); if (r && r.bytes) im.bytes = r.bytes; }
  perf.isFile = url.startsWith("file:");
  fs.writeFileSync(path.join(ev, "perf.json"), JSON.stringify(perf, null, 1));
  await ctx.close();
}

// ---- 8. motion frames and 9. scripted async actions (interact.mjs), at 1440 ------------------------
// Added after every other step so they cannot change what steps 1 to 7 record. Each is bounded in time; what was
// skipped or could not be measured is listed in motion.json / async.json and becomes "not verified" in the sweep.
manifest.interaction = {};
const prepWait = PREP && PREP.wait ? PREP.wait : 0;
if (flag("--no-motion") || flag("--no-interact")) manifest.interaction.motion = { skipped: "--no-motion" };
else try { manifest.interaction.motion = await captureMotion({ browser, open, url, ev, note, prepWait, budgetMs: +opt("--motion-budget", 60000) }); }
catch (e) { manifest.interaction.motion = { error: e.message.split("\n")[0] }; note(`motion capture failed: ${e.message}`); }
if (opt("--passive", null) !== null) try { manifest.interaction.passive = await capturePassive({ browser, open, url, ev, note, prepWait, ms: +opt("--passive", 6000) }); }
catch (e) { manifest.interaction.passive = { error: e.message.split(String.fromCharCode(10))[0] }; note(`passive capture failed: ${e.message}`); }
if (flag("--no-async") || flag("--no-interact")) manifest.interaction.async = { skipped: "--no-async" };
else try { manifest.interaction.async = await captureAsync({ browser, open, url, ev, note, prepWait, budgetMs: +opt("--async-budget", 60000) }); }
catch (e) { manifest.interaction.async = { error: e.message.split("\n")[0] }; note(`async capture failed: ${e.message}`); }

// ---- 11. throttled page load (opt-in: --slow) ---------------------------------------------------------
// The lab pass above loads on the real line. A visitor on a slow phone line sees the page arrive over seconds: what
// shows first, whether text waits for fonts or script, and what jumps. This loads at 375 with a slow-4G-like line
// (CDP: 400 ms latency, ~1.6 Mbit/s down) and 4x CPU slowdown, and screenshots at 1, 3 and 6 s from navigation start.
if (flag("--slow")) {
  const res = { version: 1, profile: { latencyMs: 400, downKbps: 1600, upKbps: 750, cpuSlowdown: 4, width: 375 }, shots: [] };
  try {
    const { ctx, page } = await open(browser, 375);
    await page.addInitScript(() => { window.__lcp = 0; window.__cls = 0; window.__firstText = null;
      try { new PerformanceObserver(l => { for (const e of l.getEntries()) window.__lcp = e.startTime; }).observe({ type: "largest-contentful-paint", buffered: true }); } catch {}
      try { new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) window.__cls += e.value; }).observe({ type: "layout-shift", buffered: true }); } catch {}
      const tick = () => { if (window.__firstText === null && document.body && document.body.innerText.trim().length > 20) window.__firstText = performance.now(); if (window.__firstText === null) requestAnimationFrame(tick); };
      requestAnimationFrame(tick); });
    const cdp = await ctx.newCDPSession(page);
    await cdp.send("Network.enable");
    await cdp.send("Network.emulateNetworkConditions", { offline: false, latency: 400, downloadThroughput: 1600 * 1024 / 8, uploadThroughput: 750 * 1024 / 8 });
    await cdp.send("Emulation.setCPUThrottlingRate", { rate: 4 });
    const t0 = Date.now();
    const nav = page.goto(url, { waitUntil: "load", timeout: 60000 }).then(() => { res.loadMs = Date.now() - t0; }).catch((e) => { res.loadError = e.message.split(String.fromCharCode(10))[0]; });
    for (const at of [1000, 3000, 6000]) {
      const wait = at - (Date.now() - t0); if (wait > 0) await page.waitForTimeout(wait);
      const f = `slow-375-${String(at).padStart(5, "0")}.png`;
      try { await page.screenshot({ path: path.join(ev, f) }); res.shots.push({ file: f, atMs: Date.now() - t0 }); } catch (e) { res.shots.push({ atMs: at, error: e.message.split(String.fromCharCode(10))[0] }); }
    }
    await Promise.race([nav, page.waitForTimeout(30000)]);
    const m = await page.evaluate(() => ({ lcp: window.__lcp, cls: Math.round((window.__cls || 0) * 1000) / 1000, firstText: window.__firstText,
      text: document.body ? document.body.innerText.replace(/\s+/g, "").length : 0 })).catch(() => ({}));
    Object.assign(res, { lcpMs: Math.round(m.lcp || 0) || null, cls: m.cls, firstTextMs: m.firstText ? Math.round(m.firstText) : null, textChars: m.text });
    await ctx.close();
  } catch (e) { res.error = e.message.split(String.fromCharCode(10))[0]; }
  fs.writeFileSync(path.join(ev, "slow.json"), JSON.stringify(res, null, 1));
  manifest.slow = res.error ? { error: res.error } : { loadMs: res.loadMs || null, firstTextMs: res.firstTextMs, lcpMs: res.lcpMs, cls: res.cls };
  note(`slow line: ${res.error ? "error " + res.error : `first text ${res.firstTextMs} ms, LCP ${res.lcpMs} ms, load ${res.loadMs || "not reached"} ms, CLS ${res.cls}`}`);
}

// ---- 10. hostile-content stress pass (opt-in: --stress) ------------------------------------------
// Real content is longer than the sample. At each stress width the page is loaded, short labels, headings, names and
// buttons are made about 40% longer (a German-length translation), and up to five text runs get a 40-character unbroken
// token (a long email, URL or product code). Then it measures what breaks: horizontal overflow, text cut by its box,
// buttons that grew, and overlaps. The page is never navigated or submitted; nothing leaves it.
function stressPage(cfg) {
  const out = { changed: 0, unbroken: 0 };
  const pick = (el) => {
    if (!el.offsetParent && getComputedStyle(el).position !== "fixed") return false;
    if (el.closest("script,style,noscript,svg,code,pre,[contenteditable],input,textarea,select")) return false;
    return [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim().length >= 3);
  };
  const sel = "h1,h2,h3,h4,h5,h6,a,button,label,th,td,li,dt,dd,[role=button],[role=tab],[role=menuitem],span,strong,b,p";
  let unb = 0;
  for (const el of document.body.querySelectorAll(sel)) {
    if (!pick(el)) continue;
    for (const n of el.childNodes) {
      if (n.nodeType !== 3) continue;
      const s = n.textContent; const tr = s.trim(); if (tr.length < 3) continue;
      if (el.tagName === "P" && tr.length > 60) continue;              // long body copy reflows anyway; stress the short slots
      const extra = tr.split(/\s+/).slice(0, Math.max(1, Math.ceil(tr.split(/\s+/).length * cfg.grow))).join(" ");
      let add = " " + extra;
      if (unb < cfg.unbroken && tr.length <= 40 && /[A-Za-z]/.test(tr) && el.tagName !== "P") { add += " " + cfg.token; unb++; }
      n.textContent = s.replace(tr, tr + add); out.changed++;
    }
  }
  out.unbroken = unb;
  return out;
}
function stressMeasure() {
  const vw = document.documentElement.clientWidth, sw = document.documentElement.scrollWidth;
  const cut = [], grew = [], over = [];
  const U = (e) => { const p = []; for (let x = e; x && x.nodeType === 1 && p.length < 4; x = x.parentElement) p.unshift(x.tagName.toLowerCase() + (x.id ? "#" + x.id : "") + (typeof x.className === "string" && x.className.trim() ? "." + x.className.trim().split(/\s+/)[0] : "")); return p.join(" > "); };
  for (const el of document.body.querySelectorAll("*")) {
    const own = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim()); if (!own) continue;
    const r = el.getBoundingClientRect(); if (r.width < 2 || r.height < 2) continue;
    const cs = getComputedStyle(el);
    if (el.scrollWidth > el.clientWidth + 2 && /hidden|clip/.test(cs.overflowX + cs.overflow))
      cut.push({ sel: U(el), text: el.textContent.trim().slice(0, 60), cutPx: el.scrollWidth - el.clientWidth, ellipsis: cs.textOverflow === "ellipsis" });
    if (r.right > vw + 2 && cs.position !== "fixed") over.push({ sel: U(el), text: el.textContent.trim().slice(0, 60), pastPx: Math.round(r.right - vw) });
    if (el.matches("button,a,[role=button]") && r.height > 2.2 * parseFloat(cs.lineHeight || cs.fontSize || 16)) grew.push({ sel: U(el), text: el.textContent.trim().slice(0, 40), h: Math.round(r.height) });
  }
  return { viewport: vw, scrollWidth: sw, pageOverflowPx: Math.max(0, sw - vw), cut: cut.slice(0, 40), cutCount: cut.length,
           pastViewport: over.slice(0, 40), pastViewportCount: over.length, tallControls: grew.slice(0, 30), tallControlCount: grew.length };
}
if (flag("--stress")) {
  const res = { version: 1, widths: {}, note: "short slots made ~40% longer and up to 5 runs given a 40-character unbroken token" };
  for (const w of [375, 1440].filter((x) => widths.includes(x) || x === 1440)) {
    try {
      const { ctx, page } = await open(browser, w);
      await goLoad(page, url, `stress pass ${w}`); await settle(page);
      const before = await page.evaluate(stressMeasure);
      const changed = await page.evaluate(stressPage, { grow: 0.4, unbroken: 5, token: "Kundenkontaktverwaltungseinstellungen-2026" });
      await page.waitForTimeout(300);
      const after = await page.evaluate(stressMeasure);
      await page.screenshot({ path: path.join(ev, `stress-${w}.png`), fullPage: true });
      res.widths[w] = { changed, before: { pageOverflowPx: before.pageOverflowPx, cutCount: before.cutCount, pastViewportCount: before.pastViewportCount, tallControlCount: before.tallControlCount }, after };
      await ctx.close();
    } catch (e) { res.widths[w] = { error: e.message.split(String.fromCharCode(10))[0] }; }
  }
  fs.writeFileSync(path.join(ev, "stress.json"), JSON.stringify(res, null, 1));
  manifest.stress = Object.fromEntries(Object.entries(res.widths).map(([w, r]) => [w, r.error ? { error: r.error } : { changed: r.changed.changed, overflowPx: r.after.pageOverflowPx, newCut: r.after.cutCount - r.before.cutCount }]));
  note(`stress: ${Object.entries(manifest.stress).map(([w, r]) => `${w}px ${r.error ? "error" : `+${r.newCut} cut, page overflow ${r.overflowPx}px`}`).join("; ")}`);
}

await browser.close();
const uniq = (k) => [...new Set(NETS.flatMap((n) => n[k]))];
manifest.network = { mode: NETS[0] ? NETS[0].mode : null, shimmed: uniq("shimmed"), blocked: uniq("blocked"), fontsMissing: uniq("fontsMissing") };
if (ISOLATE) manifest.isolate = { applied: true, note: "test-set isolation removed part of the page; the spec is in the test-set manifest, kept from blind reviewers" };
if (PREP) manifest.prep = { host: PREP_HOST, config: PREP, applied: [...prepLog] };   // nothing applied = banner or overlay still up
manifest.network.blockedImages = manifest.network.blocked.filter((b) => b.startsWith("image ")).length;
manifest.network.blockedFonts = manifest.network.blocked.filter((b) => b.startsWith("font ") || /fonts\.|fontshare|typekit/.test(b)).length;
manifest.finished = new Date().toISOString();
for (const f of fs.readdirSync(ev)) manifest.files[f] = true;
fs.writeFileSync(path.join(ev, "manifest.json"), JSON.stringify(manifest, null, 1));
console.log(JSON.stringify({ ok: manifest.control.ok, widths: manifest.widths, evidence: ev }));
