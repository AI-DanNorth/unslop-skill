#!/usr/bin/env node
// Unslop capture: renders a web artifact and writes evidence for the sweep.
// usage: node capture.mjs <url-or-file> <run-dir> [--widths 375,1440] [--bless-control] [--skip-control]
// Writes <run-dir>/01-evidence/: shot-<w>.png, bg-<w>.png, fold-<w>.png, dom-<w>.json, fonts.json,
// hidden.json, focus.json + focus/*.png, forms.json, perf.json, manifest.json
import { createRequire } from "node:module";
const { chromium } = createRequire(import.meta.url)("playwright");
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { installShim } from "./netshim.mjs";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, "../..");
const EXTRACT = fs.readFileSync(path.join(HERE, "extract.js"), "utf8");
const HEIGHTS = { 320: 568, 375: 812, 414: 896, 768: 1024, 1024: 768, 1280: 800, 1440: 900, 1920: 1080 };
const BG_ALL = true;   // background-only render at every captured width (fixed-canvas media have one width)

const args = process.argv.slice(2);
const flag = (n) => args.includes(n);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : d; };
const [target, runDir] = args.filter((a, i) => !a.startsWith("--") && !(i > 0 && args[i - 1].startsWith("--widths")));
if (!target || !runDir) { console.error("usage: capture.mjs <url-or-file> <run-dir> [--widths 375,1440]"); process.exit(2); }
const widths = opt("--widths", "320,375,414,768,1024,1280,1440,1920").split(",").map(Number);
const toUrl = (t) => { if (/^https?:|^file:/.test(t)) return t; const [f, q] = t.split("?"); return pathToFileURL(path.resolve(f)).href + (q ? "?" + q : ""); };
const url = toUrl(target);
const ev = path.join(runDir, "01-evidence");
fs.mkdirSync(path.join(ev, "focus"), { recursive: true });
const log = [];
const note = (m) => { log.push(m); console.error(m); };

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

// Per-host page preparation for live captures (page-prep.json): cookie banners, interstitials, tool overlays, extra settle.
// Every action is logged and lands in manifest.prep, so a capture never silently differs from what a visitor sees.
const PREP_HOSTS = JSON.parse(fs.readFileSync(path.join(HERE, "page-prep.json"), "utf8")).hosts;
const PREP_HOST = (() => { try { return new URL(url).hostname.replace(/^www\./, ""); } catch { return ""; } })();
const PREP = PREP_HOSTS[PREP_HOST] || null;
const prepLog = new Set();
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
const manifest = { target, url, started: new Date().toISOString(), widths: [], files: {}, control: null, log };

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
    await page.addStyleTag({ content: "*,*::before,*::after{-webkit-text-fill-color:transparent!important;text-shadow:none!important;-webkit-text-stroke:0!important;caret-color:transparent!important;text-decoration-color:transparent!important} svg text{fill:transparent!important}" });
    await page.waitForTimeout(100);
    await page.screenshot({ path: path.join(ev, `bg-${w}.png`), fullPage: true });
  }
  manifest.widths.push(w);
  await ctx.close();
}

// ---- 3. fonts that actually rendered (CDP), at 1440 -----------------------------------------------
{
  const { ctx, page } = await open(browser, 1440);
  await page.goto(url, { waitUntil: "load" }); await settle(page);
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
    reduced_motion: { opts: { reducedMotion: "reduce" }, init: null, scroll: false },
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
  await page.goto(url, { waitUntil: "load" }); await settle(page);
  await page.evaluate(EXTRACT);
  const stops = [];
  for (let i = 0; i < 40; i++) {
    await page.keyboard.press("Tab");
    await page.waitForTimeout(80);
    const info = await page.evaluate(() => {
      const a = document.activeElement;
      if (!a || a === document.body) return null;
      const r = a.getBoundingClientRect();
      const covers = [...document.querySelectorAll("body *")].filter(e => { const p = getComputedStyle(e).position; return (p === "fixed" || p === "sticky") && !e.contains(a); })
        .map(e => e.getBoundingClientRect()).filter(h => h.width > 0 && h.height > 0 && h.left < r.right && h.right > r.left && h.top < r.bottom && h.bottom > r.top);
      const cs = getComputedStyle(a);
      return { sel: a.getAttribute("data-unslop-id") ? `[data-unslop-id="${a.getAttribute("data-unslop-id")}"]` : a.tagName, tag: a.tagName.toLowerCase(),
        text: (a.innerText || a.value || a.getAttribute("aria-label") || "").trim().slice(0, 60), href: a.getAttribute("href"),
        rect: { x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height }, covered: covers.length > 0,
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
  await page.goto(url, { waitUntil: "load" }); await settle(page);
  const count = await page.evaluate(() => document.querySelectorAll("form").length);
  const results = [];
  for (let i = 0; i < count; i++) {
    const p2 = await ctx.newPage();
    await p2.goto(url, { waitUntil: "load" }); await p2.waitForTimeout(300);
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
  await page.addInitScript(() => { window.__lcp = 0; new PerformanceObserver(l => { for (const e of l.getEntries()) window.__lcp = e.startTime; }).observe({ type: "largest-contentful-paint", buffered: true }); });
  await page.goto(url, { waitUntil: "load" }); await settle(page);
  const perf = await page.evaluate(() => ({ lcp: window.__lcp, resources: performance.getEntriesByType("resource").map(r => ({ name: r.name, type: r.initiatorType, bytes: r.encodedBodySize || r.transferSize || 0 })),
    images: [...document.images].map(i => ({ src: i.currentSrc || i.src, nw: i.naturalWidth, rw: Math.round(i.getBoundingClientRect().width), id: i.getAttribute("data-unslop-id") })) }));
  for (const r of perf.resources) if (!r.bytes && r.name.startsWith("file:")) { try { r.bytes = fs.statSync(fileURLToPath(r.name)).size; } catch {} }
  for (const im of perf.images) if (im.src && im.src.startsWith("file:")) { try { im.bytes = fs.statSync(fileURLToPath(im.src)).size; } catch {} }
  for (const im of perf.images) { const r = perf.resources.find(x => x.name === im.src); if (r && r.bytes) im.bytes = r.bytes; }
  perf.isFile = url.startsWith("file:");
  fs.writeFileSync(path.join(ev, "perf.json"), JSON.stringify(perf, null, 1));
  await ctx.close();
}

await browser.close();
const uniq = (k) => [...new Set(NETS.flatMap((n) => n[k]))];
manifest.network = { mode: NETS[0] ? NETS[0].mode : null, shimmed: uniq("shimmed"), blocked: uniq("blocked"), fontsMissing: uniq("fontsMissing") };
if (PREP) manifest.prep = { host: PREP_HOST, config: PREP, applied: [...prepLog] };   // nothing applied = banner or overlay still up
manifest.network.blockedImages = manifest.network.blocked.filter((b) => b.startsWith("image ")).length;
manifest.network.blockedFonts = manifest.network.blocked.filter((b) => b.startsWith("font ") || /fonts\.|fontshare|typekit/.test(b)).length;
manifest.finished = new Date().toISOString();
for (const f of fs.readdirSync(ev)) manifest.files[f] = true;
fs.writeFileSync(path.join(ev, "manifest.json"), JSON.stringify(manifest, null, 1));
console.log(JSON.stringify({ ok: manifest.control.ok, widths: manifest.widths, evidence: ev }));
