// Unslop interaction capture: transition frames (motion/) and scripted async actions (async/).
// Called by capture.mjs after every other step. Both steps are bounded in time and record what they skipped.
//
// Motion: for up to 6 transition triggers (dialogs, menus, tabs, disclosures, plain buttons), click and record the
// state 0, 50, 100, 150, 250, 400 and 600 ms after the action, with prefers-reduced-motion off and on. CSS
// transitions, CSS animations and WAAPI animations started by the click are paused and seeked, so every frame is
// exact; a 10 ms sweep of the same timeline gives bounding boxes for duration and overshoot. Changes the page drives
// from JavaScript timers cannot be seeked: those frames are taken in real time and marked `timing: "realtime"`.
// Then a live run (prefers-reduced-motion off only) clicks again in real time and records every painted element's box
// on every animation frame (`run.live`): the end of all click-driven movement, and one-frame snaps (see startLive).
//
// Async: clicks up to 4 primary actions (form submits, action buttons) with fetch and XHR held for 3 s, and records
// the UI at 0.5 s, 2 s and after completion; then repeats with a forced failure. Nothing leaves the site: cross-origin
// requests are refused, navigations away are aborted, native form submits are cancelled, and every request that would
// change data gets a synthetic response. Forms get obviously fake values (unslop-test@example.com).
import fs from "node:fs";
import path from "node:path";

export const FRAME_TIMES = [0, 50, 100, 150, 250, 400, 600];
const VIEW = 1440;

// ---------------------------------------------------------------- in-page helpers (init script, every document)
function pageHelpers(cfg) {
  if (window.__unslopU) return;
  const U = (window.__unslopU = {});
  U.vis = (e) => {
    if (!e || !e.isConnected) return false;
    const r = e.getBoundingClientRect();
    if (r.width < 4 || r.height < 4) return false;
    let op = 1;
    for (let x = e; x && x.nodeType === 1; x = x.parentElement) {
      const s = getComputedStyle(x);
      if (s.display === "none") return false;
      op *= parseFloat(s.opacity);
    }
    return getComputedStyle(e).visibility === "visible" && op > 0.05;
  };
  U.path = (e) => {
    const parts = [];
    for (let x = e; x && x.nodeType === 1 && x !== document.documentElement; x = x.parentElement) {
      if (x.id && document.querySelectorAll("#" + CSS.escape(x.id)).length === 1) { parts.unshift("#" + CSS.escape(x.id)); break; }
      const tag = x.tagName.toLowerCase();
      const sib = x.parentElement ? [...x.parentElement.children].filter((c) => c.tagName === x.tagName) : [x];
      parts.unshift(sib.length > 1 ? `${tag}:nth-of-type(${sib.indexOf(x) + 1})` : tag);
    }
    return parts.join(" > ");
  };
  U.name = (e) => (e.getAttribute("aria-label") || e.innerText || e.value || e.title || "").replace(/\s+/g, " ").trim().slice(0, 60);
  U.lines = () => (document.body ? document.body.innerText : "").split("\n").map((s) => s.replace(/\s+/g, " ").trim()).filter(Boolean);
  U.r1 = (v) => Math.round(v * 10) / 10;
  // visible text nodes, one entry each: finer than innerText lines, which merge inline siblings into one line
  U.texts = () => {
    const out = [];
    if (!document.body) return out;
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    for (let n; (n = w.nextNode());) {
      const t = n.textContent.replace(/\s+/g, " ").trim();
      const p = n.parentElement;
      if (!t || !p || /^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE)$/.test(p.tagName)) continue;
      if (p.checkVisibility ? !p.checkVisibility({ opacityProperty: true, visibilityProperty: true }) : !U.vis(p)) continue;
      out.push(t);
    }
    return out;
  };

  // ---- guards and the network hold, armed only during a scripted action ----
  const net = (window.__unslopNet = []);
  window.__unslopArmed = false;
  const sameOrigin = (u) => {
    try { const x = new URL(u, location.href); return location.protocol === "file:" ? x.protocol === "file:" : x.origin === location.origin; }
    catch { return false; }
  };
  const fileDoc = location.protocol === "file:";
  const of = window.fetch && window.fetch.bind(window);
  if (of) window.fetch = function (input, init) {
    if (!window.__unslopArmed) return of(input, init);
    const url = String(typeof input === "string" ? input : (input && input.url) || input);
    const method = String((init && init.method) || (input && input.method) || "GET").toUpperCase();
    const rec = { url: url.slice(0, 200), method, via: "fetch", start: performance.now(), end: null, status: null, outcome: null };
    net.push(rec);
    if (!sameOrigin(url)) { rec.outcome = "blocked-cross-origin"; rec.end = performance.now(); return Promise.reject(new TypeError("Failed to fetch")); }
    const mode = window.__unslopMode || "slow";
    return new Promise((res) => setTimeout(res, cfg.delay[mode])).then(() => {
      if (mode === "fail") { rec.outcome = "forced-500"; rec.status = 500; rec.end = performance.now();
        return new Response('{"error":"unslop forced failure"}', { status: 500, headers: { "content-type": "application/json" } }); }
      if (method === "GET" && !fileDoc) return of(input, init).then((r) => { rec.outcome = "passthrough"; rec.status = r.status; rec.end = performance.now(); return r; },
        (e) => { rec.outcome = "passthrough-failed"; rec.end = performance.now(); throw e; });
      rec.outcome = "synthetic-200"; rec.status = 200; rec.end = performance.now();
      return new Response('{"ok":true}', { status: 200, headers: { "content-type": "application/json" } });
    });
  };
  const XP = window.XMLHttpRequest && XMLHttpRequest.prototype;
  if (XP) {
    const XO = XP.open, XS = XP.send;
    XP.open = function (m, u, ...rest) { this.__unslop = { method: String(m).toUpperCase(), url: String(u) }; return XO.call(this, m, u, ...rest); };
    XP.send = function (body) {
      if (!window.__unslopArmed || !this.__unslop) return XS.call(this, body);
      const xhr = this, { method, url } = this.__unslop;
      const rec = { url: url.slice(0, 200), method, via: "xhr", start: performance.now(), end: null, status: null, outcome: null };
      net.push(rec);
      const fake = (status, text, ok) => {
        for (const [k, v] of Object.entries({ readyState: 4, status, statusText: status === 200 ? "OK" : status ? "Error" : "", responseText: text, response: text }))
          Object.defineProperty(xhr, k, { value: v, configurable: true });
        rec.status = status; rec.end = performance.now();
        xhr.dispatchEvent(new Event("readystatechange"));
        xhr.dispatchEvent(new ProgressEvent(ok ? "load" : "error"));
        xhr.dispatchEvent(new ProgressEvent("loadend"));
      };
      if (!sameOrigin(url)) { rec.outcome = "blocked-cross-origin"; setTimeout(() => fake(0, "", false), 0); return; }
      const mode = window.__unslopMode || "slow";
      setTimeout(() => {
        if (mode === "fail") { rec.outcome = "forced-500"; fake(500, '{"error":"unslop forced failure"}', true); return; }
        if (method === "GET" && !fileDoc) { rec.outcome = "passthrough"; xhr.addEventListener("loadend", () => { rec.status = xhr.status; rec.end = performance.now(); }); XS.call(xhr, body); return; }
        rec.outcome = "synthetic-200"; fake(200, '{"ok":true}', true);
      }, cfg.delay[mode]);
    };
  }
  if (navigator.sendBeacon) { const SB = navigator.sendBeacon.bind(navigator); navigator.sendBeacon = (u, d) => { if (!window.__unslopArmed) return SB(u, d); net.push({ url: String(u).slice(0, 200), method: "POST", via: "beacon", outcome: "blocked-beacon", start: performance.now(), end: performance.now() }); return true; }; }
  // A native form submit would leave the page: cancel it once the page's own handlers have run (window, bubble phase).
  window.addEventListener("submit", (e) => {
    if (!window.__unslopArmed || e.defaultPrevented) return;
    e.preventDefault();
    net.push({ url: (e.target && e.target.getAttribute("action")) || "(no action)", method: ((e.target && e.target.getAttribute("method")) || "GET").toUpperCase(), via: "native-submit", outcome: "blocked-native-submit", start: performance.now(), end: performance.now() });
  });
}

// Route guard for http(s) pages while an action is armed: no navigation away, nothing cross-origin, no writes.
async function routeGuard(ctx, page, url, log) {
  const guard = { armed: false };
  if (!/^https?:/.test(url)) return guard;            // file:// pages: the in-page shim and submit guard do the work
  const origin = new URL(url).origin;
  await ctx.route("**/*", async (route) => {
    if (!guard.armed) return route.fallback();
    const req = route.request(), u = req.url();
    let o = ""; try { o = new URL(u).origin; } catch {}
    if (req.isNavigationRequest() && req.frame() === page.mainFrame() && u.split("#")[0] !== page.url().split("#")[0]) { log.push(`navigation blocked: ${u.slice(0, 120)}`); return route.abort(); }
    if (o && o !== origin && !u.startsWith("data:")) { log.push(`cross-origin blocked: ${req.method()} ${u.slice(0, 120)}`); return route.abort(); }
    if (!["GET", "HEAD"].includes(req.method()) && !["fetch", "xhr"].includes(req.resourceType())) { log.push(`write blocked: ${req.method()} ${u.slice(0, 120)}`); return route.abort(); }
    return route.fallback();
  });
  return guard;
}

async function lightSettle(page, prepWait) {
  try { await page.waitForLoadState("networkidle", { timeout: 6000 }); } catch {}
  try { await page.evaluate(() => document.fonts && document.fonts.ready); } catch {}
  if (prepWait) await page.waitForTimeout(prepWait);
  await page.waitForTimeout(400);
}

// ---------------------------------------------------------------- motion
function discoverTriggers(maxN) {
  const U = window.__unslopU;
  const ACTION = /\b(save|create|add|submit|send|publish|export|import|subscribe|sign ?up|sign ?in|log ?in|join|register|book|reserve|order|buy|checkout|pay|apply|confirm|update|upload|invite|generate|sync|refresh|delete|remove|post|download|request)\b/i;
  const sel = "button, [role=button], [role=tab], summary, [aria-haspopup], [aria-expanded], [popovertarget], input[type=button]";
  const out = [], sigs = new Set();
  for (const e of document.querySelectorAll(sel)) {
    if (!U.vis(e) || e.disabled || e.getAttribute("aria-disabled") === "true") continue;
    if (e.closest("form") && (e.type === "submit" || e.matches("button:not([type])"))) continue;          // form submits: async step
    if (e.tagName === "A" && !/^(#.*)?$/.test(e.getAttribute("href") || "")) continue;                       // real links navigate
    if (e.getAttribute("aria-expanded") === "true") continue;                                                // already open
    const hp = (e.getAttribute("aria-haspopup") || "").toLowerCase();
    const ctlId = e.getAttribute("aria-controls") || e.getAttribute("popovertarget") || "";
    const ctl = ctlId ? document.getElementById(ctlId) : null;
    const toggle = e.getAttribute("data-bs-toggle") || e.getAttribute("data-toggle") || "";
    let kind = "button";
    if (hp === "dialog" || (ctl && ctl.matches("dialog,[role=dialog],[role=alertdialog],[aria-modal=true]")) || /modal|dialog|offcanvas/i.test(toggle)) kind = "dialog";
    else if (["menu", "listbox", "true", "tree", "grid"].includes(hp) || (ctl && ctl.matches("[role=menu],[role=listbox]")) || /dropdown/i.test(toggle)) kind = "menu";
    else if (e.getAttribute("role") === "tab") { if (e.getAttribute("aria-selected") === "true") continue; kind = "tab"; }
    else if (e.tagName === "SUMMARY" || e.hasAttribute("aria-expanded") || e.hasAttribute("popovertarget") || /collapse/i.test(toggle)) kind = "disclosure";
    const name = U.name(e);
    if (kind === "button" && ACTION.test(name)) continue;                                                    // primary actions: async step
    const r = e.getBoundingClientRect();
    const sig = kind + "|" + e.tagName + "|" + String(e.getAttribute("class") || "").split(/\s+/).filter((c) => !/active|selected|open|current/i.test(c)).sort().join(".");
    if (sigs.has(sig)) continue;                                                                             // one of each repeated control
    sigs.add(sig);
    out.push({ selector: U.path(e), name, kind, area: Math.round(r.width * r.height), top: Math.round(r.top + scrollY) });
  }
  const rank = { dialog: 0, menu: 1, tab: 2, disclosure: 3, button: 4 };
  out.sort((a, b) => rank[a.kind] - rank[b.kind] || (a.top > 2400) - (b.top > 2400) || b.area - a.area);
  return { found: out.length, triggers: out.slice(0, maxN), notTried: out.slice(maxN).map((t) => ({ ...t, reason: `over the cap of ${maxN} triggers` })) };
}

function preClick(selector) {
  const U = window.__unslopU;
  const el = document.querySelector(selector);
  if (!el) return { error: "trigger not found" };
  window.__unslopPre = new Set(document.getAnimations());
  const overlays = "dialog[open],[role=dialog],[role=alertdialog],[role=menu],[role=listbox],[role=tooltip],[popover],[aria-modal=true]";
  window.__unslopPreOverlays = new Set([...document.querySelectorAll(overlays)].filter(U.vis));
  window.__unslopOthers = [...document.querySelectorAll("p,h1,h2,h3,h4,h5,h6,li,img,button,a,input,label,td,figure,svg")]
    .filter((e) => U.vis(e) && !el.contains(e) && !e.contains(el)).slice(0, 160);
  window.__unslopSig = [U.lines().length, document.querySelectorAll("[aria-expanded=true]").length,
    [...document.querySelectorAll(overlays)].filter(U.vis).length, location.href].join("|");
  const r = el.getBoundingClientRect();
  return { rect: [r.left, r.top, r.width, r.height].map(U.r1), sig: window.__unslopSig,
    hit: (() => { const h = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2); return !!h && (el === h || el.contains(h)); })() };
}

async function postClick({ selector }) {
  const U = window.__unslopU, pre = window.__unslopPre || new Set();
  const MOVE = /^(transform|translate|scale|rotate|opacity|width|height|max-height|max-width|min-height|top|left|right|bottom|inset|margin|padding|clip-path|filter|grid-template|flex-basis|offset)/;
  let anims = [];
  for (let i = 0; i < 14; i++) {                    // up to ~14 frames: openers often add the class one or two frames later
    anims = document.getAnimations().filter((a) => !pre.has(a) && a.playState !== "finished" && a.playState !== "idle");
    if (anims.length && i >= 2) break;
    await new Promise((r) => requestAnimationFrame(r));
  }
  const info = anims.map((a) => {
    const eff = a.effect, tim = eff ? eff.getComputedTiming() : {}, kf = eff && eff.getKeyframes ? eff.getKeyframes() : [];
    const props = a.transitionProperty ? [a.transitionProperty] : [...new Set(kf.flatMap((k) => Object.keys(k).filter((x) => !["offset", "computedOffset", "easing", "composite"].includes(x))))]
      .map((p) => p.replace(/[A-Z]/g, (c) => "-" + c.toLowerCase()));
    const timingEase = eff ? eff.getTiming().easing : "linear";
    const kfEase = [...new Set(kf.slice(0, -1).map((k) => k.easing).filter(Boolean))];
    const target = eff && eff.target;
    return { a, target, type: a.constructor.name, name: a.animationName || a.transitionProperty || a.id || "", props, pseudo: (eff && eff.pseudoElement) || null,
      start: a.startTime, delay: eff ? eff.getTiming().delay : 0, duration: tim.duration, endTime: tim.endTime, iterations: tim.iterations,
      easing: timingEase !== "linear" ? timingEase : kfEase.length === 1 ? kfEase[0] : kfEase.length ? "per-keyframe" : "linear" };
  });
  const finite = info.filter((i) => i.iterations !== Infinity && isFinite(i.endTime));
  const starts = finite.map((i) => i.start).filter((s) => s !== null && s !== undefined);
  const s0 = starts.length ? Math.min(...starts) : 0;
  for (const i of finite) { i.offset = i.start !== null && i.start !== undefined ? Math.max(0, i.start - s0) : 0; try { i.a.pause(); } catch {} }
  // changed elements: targets of movement/opacity animations (paint-only colour transitions are trigger feedback)
  const moving = finite.filter((i) => i.target && i.props.some((p) => MOVE.test(p)));
  let roots = [...new Set(moving.map((i) => i.target))].filter((e) => e.nodeType === 1);
  roots.sort((a, b) => { const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect(); return rb.width * rb.height - ra.width * ra.height; });
  roots = roots.slice(0, 6);
  let rootSource = "animation-targets";
  if (!roots.length) {                                // nothing seekable moved: look for what opened (instant or JS-timed)
    const el = document.querySelector(selector);
    const ctlId = el && (el.getAttribute("aria-controls") || el.getAttribute("popovertarget"));
    const ctl = ctlId && document.getElementById(ctlId);
    const preO = window.__unslopPreOverlays || new Set();
    const opened = [...document.querySelectorAll("dialog[open],[role=dialog],[role=alertdialog],[role=menu],[role=listbox],[role=tooltip],[popover],[aria-modal=true]")].filter((e) => U.vis(e) && !preO.has(e));
    roots = [...new Set([...(ctl && U.vis(ctl) ? [ctl] : []), ...opened])].slice(0, 6);
    rootSource = roots.length ? "opened-element" : "none";
  }
  const maxEnd = finite.length ? Math.max(...finite.map((i) => i.offset + i.endTime)) : 0;
  window.__unslopRun = { finite, roots, others: (window.__unslopOthers || []).filter((o) => !roots.some((r) => r.contains(o))) };
  const seekable = moving.length > 0;
  const sweep = [], othersTrack = [];
  const seek = (t) => { for (const i of finite) { try { i.a.currentTime = Math.max(0, t - i.offset); } catch {} } };
  const meas = () => roots.map((e) => { const r = e.getBoundingClientRect(); return [U.r1(r.left), U.r1(r.top), U.r1(r.width), U.r1(r.height), +(+getComputedStyle(e).opacity).toFixed(3)]; });
  if (seekable) {
    const horizon = Math.min(Math.max(maxEnd, 600), 3000);
    for (let t = 0; t <= horizon + 0.1; t += 10) {
      seek(t);
      sweep.push({ t, roots: meas() });
      othersTrack.push(window.__unslopRun.others.map((o) => { const r = o.getBoundingClientRect(); return [r.left, r.top]; }));
    }
  }
  window.__unslopRun.othersTrack = othersTrack;
  return {
    seekable, rootSource, maxEndMs: Math.round(maxEnd),
    animations: info.map((i) => ({ target: i.target && i.target.nodeType === 1 ? U.path(i.target) : null, pseudo: i.pseudo, type: i.type, name: String(i.name).slice(0, 60), props: i.props.slice(0, 8),
      delayMs: Math.round(i.delay || 0), durationMs: i.duration === Infinity ? null : Math.round(i.duration || 0), endMs: isFinite(i.endTime) ? Math.round(i.endTime + (i.offset || 0)) : null,
      iterations: i.iterations === Infinity ? "infinite" : i.iterations, easing: i.easing, offsetMs: Math.round(i.offset || 0), root: roots.indexOf(i.target) })),
    roots: roots.map((e) => ({ selector: U.path(e), tag: e.tagName.toLowerCase(), role: e.getAttribute("role"), name: U.name(e).slice(0, 40) })),
    sweep,
  };
}

function frameAt(t) {
  const R = window.__unslopRun;
  if (t !== null) for (const i of R.finite) { try { i.a.currentTime = Math.max(0, t - i.offset); } catch {} }
  return R.roots.map((e) => {
    const r = e.getBoundingClientRect(), cs = getComputedStyle(e);
    return { box: [r.left, r.top, r.width, r.height].map((v) => Math.round(v * 10) / 10), opacity: +(+cs.opacity).toFixed(3), transform: cs.transform, visible: window.__unslopU.vis(e) };
  });
}

async function finishRun(layoutPx) {
  const R = window.__unslopRun, U = window.__unslopU;
  for (const i of R.finite) { try { i.a.finish(); } catch { try { i.a.play(); } catch {} } }
  await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
  const final = R.roots.map((e) => { const r = e.getBoundingClientRect(); return [U.r1(r.left), U.r1(r.top), U.r1(r.width), U.r1(r.height), +(+getComputedStyle(e).opacity).toFixed(3)]; });
  // layout movement: other content that sits between its start and end position during the transition (animated reflow)
  const moved = [];
  if (R.othersTrack.length > 2) {
    R.others.forEach((o, k) => {
      const r = o.getBoundingClientRect(), fin = [r.left, r.top], st = R.othersTrack[0][k];
      let mid = 0, at = null;
      for (let s = 1; s < R.othersTrack.length - 1; s++) {
        const p = R.othersTrack[s][k];
        const d = Math.min(Math.hypot(p[0] - st[0], p[1] - st[1]), Math.hypot(p[0] - fin[0], p[1] - fin[1]));
        if (d > mid) { mid = d; at = s * 10; }
      }
      if (mid > layoutPx) moved.push({ selector: U.path(o), name: U.name(o).slice(0, 40), midPx: U.r1(mid), atMs: at, netPx: U.r1(Math.hypot(fin[0] - st[0], fin[1] - st[1])) });
    });
  }
  moved.sort((a, b) => b.midPx - a.midPx);
  return { final, layoutMoved: moved.slice(0, 12), layoutMovedCount: moved.length };
}

// ---------------------------------------------------------------- live (real-time) recording
// The seeked sweep above only drives CSS transitions, CSS animations and WAAPI. Motion a page drives from JavaScript
// (requestAnimationFrame tweens, spring libraries) cannot be seeked, so its duration and its frames were unmeasured.
// The live run clicks the trigger again in real time and records the box of every painted element in the viewport on
// every animation frame. Method adapted from Stageshow's jump scanner (benjitaylor/skills, stageshow/scripts/
// jumps-core.mjs, MIT): a jump is a change over 2 px in one frame that is over 3x the change in the frames either side.
// What it adds for Unslop: the end of all click-driven movement (any engine), one-frame snaps at the end of a movement
// ("settle"), and content shoved in one frame while another element is mid-animation ("shove"). Elements that already
// move before the click (carousels, marquees, tickers) are ambient and left out. Instant changes are not judged.
export function startLive(ms) {
  const L = (window.__unslopLive = { frames: [], ids: new WeakMap(), meta: [], clickT: null, stop: false, t0: performance.now() });
  const idOf = (el) => {
    if (!L.ids.has(el)) {
      L.ids.set(el, L.meta.length);
      L.meta.push({ name: `${el.tagName.toLowerCase()}${el.id ? "#" + el.id : ""}${typeof el.className === "string" && el.className.trim() ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".") : ""}`.slice(0, 60),
        text: (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim().slice(0, 30), parent: -1, el });
    }
    return L.ids.get(el);
  };
  const scan = () => {
    const out = [];
    for (const el of document.body ? document.body.querySelectorAll("*") : []) {
      if (out.length >= 600) break;
      const r = el.getBoundingClientRect();
      if (r.width * r.height < 16 || r.bottom < -300 || r.right < -300 || r.top > innerHeight + 300 || r.left > innerWidth + 300) continue;   // margin: things entering from just off screen
      if (/^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE|BR|WBR)$/.test(el.tagName)) continue;
      const own = [...el.childNodes].some((c) => c.nodeType === 3 && c.textContent.trim());
      const cs = getComputedStyle(el);
      const paints = (cs.backgroundColor !== "rgba(0, 0, 0, 0)" && cs.backgroundColor !== "transparent") || cs.backgroundImage !== "none" || cs.boxShadow !== "none" ||
        parseFloat(cs.borderTopWidth) + parseFloat(cs.borderBottomWidth) + parseFloat(cs.borderLeftWidth) + parseFloat(cs.borderRightWidth) > 0;
      if (!own && !paints && !/^(IMG|svg|VIDEO|CANVAS|INPUT|BUTTON|SELECT|TEXTAREA)$/.test(el.tagName)) continue;
      const id = idOf(el);
      if (L.meta[id].parent < 0 && el.parentElement) L.meta[id].parent = idOf(el.parentElement);
      out.push(el);
    }
    return out;
  };
  let els = scan(), n = 0;
  const tick = () => {
    if (L.stop) return;
    if (++n % 8 === 0) els = scan();               // pick up what opened
    const t = performance.now() - L.t0, items = [];
    for (const el of els) {
      if (!el.isConnected) continue;
      const r = el.getBoundingClientRect();
      if (r.width * r.height < 16) continue;
      const shown = el.checkVisibility ? el.checkVisibility({ opacityProperty: true, visibilityProperty: true }) : true;
      if (!shown) continue;
      items.push([L.ids.get(el), Math.round(r.left * 10) / 10, Math.round(r.top * 10) / 10, Math.round(r.width * 10) / 10, Math.round(r.height * 10) / 10]);
    }
    L.frames.push({ t, items });
    if (t < ms) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
  return true;
}

export function analyseLive(cfg) {
  const L = window.__unslopLive, U = window.__unslopU;
  L.stop = true;
  const F = L.frames, out = { frames: F.length, coverage: "ok", snaps: [], ambient: 0, motionEndMs: null, stillMoving: false };
  if (F.length < 12 || L.clickT === null) { out.coverage = "inconclusive"; out.reason = `only ${F.length} frames recorded`; return out; }
  const dts = F.slice(1).map((f, i) => f.t - F[i].t).sort((a, b) => a - b);
  const frameMs = dts[Math.floor(dts.length / 2)] || 16.7;
  out.frameMs = Math.round(frameMs * 10) / 10;
  const late = (f) => f > 0 && F[f].t - F[f - 1].t > frameMs * 1.6;
  out.lateFrames = F.filter((_, f) => late(f)).length;
  if (out.lateFrames > F.length / 3) { out.coverage = "inconclusive"; out.reason = `${out.lateFrames} of ${F.length} frames came late (page busy)`; }
  const at = F.map((f) => new Map(f.items.map((i) => [i[0], i])));
  const c0 = F.findIndex((f) => f.t >= L.clickT);
  if (c0 < 4) { out.coverage = "inconclusive"; out.reason = "no baseline frames before the click"; return out; }
  const step = (f, id, k) => { const a = at[f - 1] && at[f - 1].get(id), b = at[f].get(id); return a && b ? b[k] - a[k] : null; };
  const AX = [[1, "x"], [2, "y"], [3, "width"], [4, "height"]];
  const moved = (f, id) => AX.some(([k]) => { const d = step(f, id, k); return d !== null && Math.abs(d) > 0.4; });
  // ambient: anything moving before the click
  const ambient = new Set();
  for (let f = 1; f < c0; f++) for (const id of at[f].keys()) if (moved(f, id)) ambient.add(id);
  // ancestors of ambient elements move them too: treat descendants of an ambient box as ambient
  const isAmbient = (id) => { for (let x = id, k = 0; x >= 0 && k < 40; x = L.meta[x].parent, k++) if (ambient.has(x)) return true; return false; };
  out.ambient = ambient.size;
  // the end of click-driven movement, any engine
  let last = null;
  for (let f = c0 + 1; f < F.length; f++) { if (late(f)) continue; for (const id of at[f].keys()) if (!isAmbient(id) && moved(f, id)) { last = f; break; } }
  if (last !== null) { out.motionEndMs = Math.round(F[last].t - L.clickT); out.stillMoving = last >= F.length - 3; }
  // snaps after the click
  const found = new Map();
  for (let f = c0 + 2; f < F.length - 1; f++) {
    if (late(f - 1) || late(f) || late(f + 1)) continue;
    for (const [id] of at[f]) {
      if (isAmbient(id)) continue;
      for (const [k, axis] of AX) {
        const d = step(f, id, k), before = step(f - 1, id, k), after = step(f + 1, id, k);
        if (d === null || before === null || after === null) continue;
        const calm = Math.max(Math.abs(before), Math.abs(after), 0.4);
        if (Math.abs(d) <= cfg.jumpPx || Math.abs(d) <= 3 * calm) continue;
        // settle: this element glided in at least 3 of the 8 frames before the jump
        let glided = 0;
        for (let g = Math.max(c0 + 1, f - 8); g < f; g++) { const s = step(g, id, k); if (s !== null && Math.abs(s) > 0.4 && Math.abs(s) <= cfg.jumpPx * 3) glided++; }
        // shove: another element is mid-glide across the jump (moving in the frames before and after it)
        let kind = glided >= 3 ? "settle" : null;
        if (!kind) {
          for (const [o] of at[f]) {
            if (o === id || isAmbient(o)) continue;
            const pb = step(f - 1, o, 2), pa = step(f + 1, o, 2), xb = step(f - 1, o, 1), xa = step(f + 1, o, 1);
            const glide = (u, v) => u !== null && v !== null && Math.abs(u) > 0.4 && Math.abs(v) > 0.4 && Math.abs(u) < cfg.jumpPx * 3 && Math.abs(v) < cfg.jumpPx * 3;
            if (glide(pb, pa) || glide(xb, xa)) { kind = "shove"; break; }
          }
        }
        if (!kind) continue;
        const key = `${id}:${axis}`;
        if (found.has(key)) { found.get(key).count++; continue; }
        found.set(key, { id, parent: L.meta[id].parent, kind, axis, d: Math.round(d * 10) / 10, atMs: Math.round(F[f].t - L.clickT), count: 1 });
      }
    }
  }
  // a parent's jump carries its children: keep the outermost
  const lines = [...found.values()].sort((a, b) => a.atMs - b.atMs), kept = [];
  for (const l of lines) {
    let anc = false;
    for (let x = l.parent, k = 0; x >= 0 && k < 40; x = L.meta[x].parent, k++) if (kept.some((s) => s.id === x && s.axis === l.axis && Math.abs(s.atMs - l.atMs) < 40)) { anc = true; break; }
    if (!anc) kept.push(l);
  }
  out.snapCount = kept.length;
  out.snaps = kept.slice(0, 10).map((l) => ({ kind: l.kind, axis: l.axis, dPx: l.d, atMs: l.atMs, count: l.count, name: L.meta[l.id].name, text: L.meta[l.id].text,
    selector: L.meta[l.id].el && L.meta[l.id].el.isConnected ? U.path(L.meta[l.id].el) : null }));
  return out;
}

async function clickTrigger(page, selector, pre) {
  const [x, y, w, h] = pre.rect;
  if (pre.hit && w > 0 && h > 0) { await page.mouse.click(x + w / 2, y + h / 2); return "mouse"; }
  await page.evaluate((s) => document.querySelector(s).click(), selector);          // covered: dispatch the click on the element
  return "element.click()";
}

const pageSig = () => { const U = window.__unslopU; const o = "dialog[open],[role=dialog],[role=alertdialog],[role=menu],[role=listbox],[role=tooltip],[popover],[aria-modal=true]";
  return [U.lines().length, document.querySelectorAll("[aria-expanded=true]").length, [...document.querySelectorAll(o)].filter(U.vis).length, location.href].join("|"); };

async function liveRun(page, selector, guard, load, dirty, liveMs) {
  const res = { coverage: "inconclusive", dirty };
  try {
    if (dirty) { await load(); res.dirty = false; }
    let navigated = false;
    const onNav = (f) => { if (f === page.mainFrame()) navigated = true; };
    page.on("framenavigated", onNav);
    await page.evaluate((s) => { const e = document.querySelector(s); if (e) e.scrollIntoView({ block: "center", inline: "nearest" }); }, selector);
    await page.waitForTimeout(250);
    let pre = await page.evaluate(preClick, selector);
    if (pre.error) { page.off("framenavigated", onNav); return { ...res, reason: pre.error }; }
    await page.mouse.move(pre.rect[0] + pre.rect[2] / 2, pre.rect[1] + pre.rect[3] / 2);
    await page.waitForTimeout(400);
    pre = await page.evaluate(preClick, selector);
    await page.evaluate(startLive, liveMs + 400);
    await page.waitForTimeout(400);                                       // baseline: what moves without the click is ambient
    guard.armed = true;
    await page.evaluate(() => { window.__unslopLive.clickT = performance.now() - window.__unslopLive.t0; });
    res.clickedWith = await clickTrigger(page, selector, pre);
    await page.waitForTimeout(liveMs);
    Object.assign(res, await page.evaluate(analyseLive, { jumpPx: 2 }));
    res.windowMs = liveMs;
    await page.keyboard.press("Escape").catch(() => {});
    await page.mouse.move(2, 2);
    await page.waitForTimeout(300);
    page.off("framenavigated", onNav);
    guard.armed = false;
    if (navigated) return { ...res, coverage: "inconclusive", reason: "the click navigated the page", dirty: true };
    const sig = await page.evaluate(pageSig).catch(() => "");
    res.dirty = sig !== pre.sig;
  } catch (e) { guard.armed = false; return { coverage: "inconclusive", reason: `error: ${e.message.split("\n")[0]}`, dirty: true }; }
  return res;
}

export async function captureMotion({ browser, open, url, ev, note, prepWait = 0, budgetMs = 60000, maxTriggers = 6, liveMs = 1500 }) {
  const dir = path.join(ev, "motion");
  fs.rmSync(dir, { recursive: true, force: true });       // capture output only: a re-capture replaces its own frames
  fs.mkdirSync(dir, { recursive: true });
  const t0 = Date.now();
  const out = { version: 2, viewport: [VIEW, 900], frameTimesMs: FRAME_TIMES, budgetMs, liveMs, modes: ["normal", "reduce"], triggers: [], skipped: [], notVerified: [], log: [] };
  const layoutPx = 2;
  let discovered = null;
  for (const mode of ["normal", "reduce"]) {
    const { ctx, page } = await open(browser, VIEW, mode === "reduce" ? { reducedMotion: "reduce" } : { reducedMotion: "no-preference" });
    await ctx.addInitScript(pageHelpers, { delay: { slow: 0, fail: 0 } });
    const guard = await routeGuard(ctx, page, url, out.log);
    const load = async () => { guard.armed = false; await page.goto(url, { waitUntil: "load", timeout: 45000 }); await lightSettle(page, prepWait); };
    try { await load(); } catch (e) { out.notVerified.push(`${mode}: page did not load: ${e.message}`); await ctx.close(); continue; }
    try {
      const iframes = await page.evaluate(() => document.querySelectorAll("iframe").length);
      if (iframes && mode === "normal") out.notVerified.push(`${iframes} iframe(s) on the page: transitions inside frames are not exercised`);
    } catch {}
    if (!discovered) {
      discovered = await page.evaluate(discoverTriggers, maxTriggers);
      out.found = discovered.found;
      out.skipped.push(...discovered.notTried);
      out.triggers = discovered.triggers.map((t) => ({ selector: t.selector, name: t.name, kind: t.kind, runs: {} }));
    }
    let dirty = false;
    for (const [ti, trig] of out.triggers.entries()) {
      if (Date.now() - t0 > budgetMs) { trig.runs[mode] = { status: "skipped", reason: `time budget ${budgetMs} ms used up` }; continue; }
      const run = { status: "ok" };
      trig.runs[mode] = run;
      try {
        if (dirty) { await load(); dirty = false; }
        let navigated = false;
        const onNav = (f) => { if (f === page.mainFrame()) navigated = true; };
        page.on("framenavigated", onNav);
        await page.evaluate((s) => { const e = document.querySelector(s); if (e) e.scrollIntoView({ block: "center", inline: "nearest" }); }, trig.selector);
        await page.waitForTimeout(250);
        let pre = await page.evaluate(preClick, trig.selector);
        if (pre.error) { run.status = "not-verified"; run.reason = pre.error; page.off("framenavigated", onNav); continue; }
        await page.mouse.move(pre.rect[0] + pre.rect[2] / 2, pre.rect[1] + pre.rect[3] / 2);
        await page.waitForTimeout(400);                                   // hover transitions finish before the snapshot
        pre = await page.evaluate(preClick, trig.selector);
        guard.armed = true;
        run.clickedWith = await clickTrigger(page, trig.selector, pre);
        const res = await page.evaluate(postClick, { selector: trig.selector });
        Object.assign(run, { seekable: res.seekable, timing: res.seekable ? "seeked" : "realtime", rootSource: res.rootSource, maxEndMs: res.maxEndMs, animations: res.animations, changed: res.roots });
        if (res.seekable) run.sweep = res.sweep;
        // frames
        const frames = [];
        const clickAt = Date.now();
        for (const t of FRAME_TIMES) {
          let at = t;
          if (!res.seekable) { const wait = t - (Date.now() - clickAt); if (wait > 0) await page.waitForTimeout(wait); at = Date.now() - clickAt; }
          const boxes = await page.evaluate(frameAt, res.seekable ? t : null);
          const file = `motion/t${ti}-${mode}-${String(t).padStart(3, "0")}.png`;
          const clip = clipFor([pre.rect, ...boxes.map((b) => b.box)]);
          try { await page.screenshot({ path: path.join(ev, file), clip, animations: "allow" }); } catch (e) { out.log.push(`frame ${file}: ${e.message}`); }
          frames.push({ tMs: t, actualMs: res.seekable ? t : at, file, changed: boxes });
        }
        run.frames = frames;
        const fin = await page.evaluate(finishRun, layoutPx);
        run.final = fin.final;
        run.layoutMoved = fin.layoutMoved; run.layoutMovedCount = fin.layoutMovedCount;
        if (!res.seekable && !res.roots.length) run.note = "no animation started and nothing opened: instant change or none";
        if (!res.seekable && res.roots.length) run.note = "change is not driven by CSS/WAAPI animations: frames are real-time screenshots, sweep not available";
        // reset: Escape, then reload if the page did not return to its pre-click state
        await page.keyboard.press("Escape").catch(() => {});
        await page.mouse.move(2, 2);
        await page.waitForTimeout(300);
        page.off("framenavigated", onNav);
        guard.armed = false;
        if (navigated) { run.status = "not-verified"; run.reason = "the click navigated the page"; dirty = true; continue; }
        const sig = await page.evaluate(() => { const U = window.__unslopU; const o = "dialog[open],[role=dialog],[role=alertdialog],[role=menu],[role=listbox],[role=tooltip],[popover],[aria-modal=true]";
          return [U.lines().length, document.querySelectorAll("[aria-expanded=true]").length, [...document.querySelectorAll(o)].filter(U.vis).length, location.href].join("|"); }).catch(() => "");
        if (sig !== pre.sig) { dirty = true; run.reset = "reload"; } else run.reset = "escape";
        // live run (normal mode): the same click in real time, every animation frame recorded
        if (mode === "normal" && liveMs > 0) {
          if (Date.now() - t0 > budgetMs) run.live = { coverage: "skipped", reason: `time budget ${budgetMs} ms used up` };
          else run.live = await liveRun(page, trig.selector, guard, load, dirty, liveMs);
          dirty = run.live.dirty; delete run.live.dirty;
        }
      } catch (e) { run.status = "not-verified"; run.reason = `error: ${e.message.split("\n")[0]}`; dirty = true; guard.armed = false; }
    }
    await ctx.close();
  }
  out.elapsedMs = Date.now() - t0;
  fs.writeFileSync(path.join(ev, "motion.json"), JSON.stringify(out));
  const ok = out.triggers.filter((t) => Object.values(t.runs).some((r) => r.status === "ok")).length;
  note(`motion: ${out.found ?? 0} trigger(s) found, ${out.triggers.length} tried, ${ok} measured in ${out.elapsedMs} ms`);
  return { found: out.found ?? 0, tried: out.triggers.length, measured: ok, skipped: out.skipped.length, notVerified: out.notVerified, elapsedMs: out.elapsedMs };
}

function clipFor(boxes) {
  const pad = 24;
  const bs = boxes.filter((b) => b && b[2] > 0 && b[3] > 0);
  if (!bs.length) return { x: 0, y: 0, width: VIEW, height: 900 };
  let x0 = Math.min(...bs.map((b) => b[0])) - pad, y0 = Math.min(...bs.map((b) => b[1])) - pad;
  let x1 = Math.max(...bs.map((b) => b[0] + b[2])) + pad, y1 = Math.max(...bs.map((b) => b[1] + b[3])) + pad;
  x0 = Math.max(0, x0); y0 = Math.max(0, y0); x1 = Math.min(VIEW, x1); y1 = Math.min(900, y1);
  if (x1 - x0 < 8 || y1 - y0 < 8) return { x: 0, y: 0, width: VIEW, height: 900 };
  return { x: Math.floor(x0), y: Math.floor(y0), width: Math.ceil(x1 - x0), height: Math.ceil(y1 - y0) };
}

// ---------------------------------------------------------------- async
function discoverActions(maxN) {
  const U = window.__unslopU;
  const ACTION = /\b(save|create|add|submit|send|publish|export|import|subscribe|sign ?up|join|register|book|reserve|order|buy|checkout|pay|apply|confirm|update|upload|invite|generate|sync|refresh|load more|delete|remove|post|download|request|notify|get started|continue)\b/i;
  const out = [];
  for (const e of document.querySelectorAll("button, input[type=submit], input[type=button], [role=button]")) {
    if (!U.vis(e) || e.disabled || e.getAttribute("aria-disabled") === "true") continue;
    if (e.tagName === "A" && !/^(#.*)?$/.test(e.getAttribute("href") || "")) continue;
    if (e.hasAttribute("aria-haspopup") || e.hasAttribute("aria-expanded") || e.getAttribute("role") === "tab") continue;
    const form = e.closest("form");
    const submit = !!form && (e.type === "submit" || e.matches("button:not([type])"));
    const name = U.name(e);
    if (!submit && !ACTION.test(name)) continue;
    const r = e.getBoundingClientRect();
    out.push({ selector: U.path(e), name, kind: submit ? "form-submit" : form ? "form-button" : "action-button", form: form ? U.path(form) : null, area: Math.round(r.width * r.height), top: Math.round(r.top + scrollY) });
  }
  const rank = { "form-submit": 0, "form-button": 1, "action-button": 2 };
  out.sort((a, b) => rank[a.kind] - rank[b.kind] || b.area - a.area);
  return { found: out.length, actions: out.slice(0, maxN), notTried: out.slice(maxN).map((a) => ({ ...a, reason: `over the cap of ${maxN} actions` })) };
}

// fill the action's form with obviously fake values; never real data
function fillForm(formSel) {
  const f = formSel && document.querySelector(formSel);
  if (!f) return 0;
  let n = 0;
  for (const el of f.querySelectorAll("input,textarea,select")) {
    if (el.disabled || el.readOnly) continue;
    const t = (el.type || "").toLowerCase();
    if (["submit", "button", "hidden", "reset", "file", "image"].includes(t)) continue;
    if (t === "checkbox" || t === "radio") { if (el.required) el.checked = true; }
    else if (el.tagName === "SELECT") { if (el.options.length > 1 && el.selectedIndex <= 0) el.selectedIndex = 1; }
    else el.value = t === "email" ? "unslop-test@example.com" : t === "tel" ? "5550100" : t === "number" ? "1" : t === "url" ? "https://example.com" : t === "date" ? "2030-01-01" : t === "password" ? "Unslop-test-0" : "Unslop test";
    el.dispatchEvent(new Event("input", { bubbles: true })); el.dispatchEvent(new Event("change", { bubbles: true })); n++;
  }
  return n;
}

function armAction({ selector, mode, spinnerSrc }) {
  const U = window.__unslopU;
  window.__unslopMode = mode;
  window.__unslopNet.length = 0;
  const before = new Set(U.texts());
  window.__unslopBefore = before;
  window.__unslopTL = [];
  window.__unslopClickT = null;
  const spin = new RegExp(spinnerSrc, "i");
  window.__unslopSpinners = () => [...document.querySelectorAll("body *")].filter((e) => {
    if (!U.vis(e)) return false;
    const id = `${e.getAttribute("class") || ""} ${e.id || ""} ${e.getAttribute("aria-label") || ""} ${e.getAttribute("data-state") || ""}`;
    if (e.getAttribute("role") === "progressbar" || e.tagName === "PROGRESS" || spin.test(id)) return true;
    return e.getAnimations().some((a) => a.playState === "running" && a.effect && a.effect.getComputedTiming().iterations === Infinity);
  }).slice(0, 12).map(U.path);
  window.__unslopPreSpin = new Set(window.__unslopSpinners());
  window.__unslopPreBusy = new Set([...document.querySelectorAll("[aria-busy=true]")].map(U.path));
  let pending = false, last = "", lastTrig = "";
  window.__unslopTrigTL = [];
  const trigSig = () => { const el = document.querySelector(selector); if (!el) return "gone"; const cs = getComputedStyle(el);
    return JSON.stringify({ cls: String(el.getAttribute("class") || "").slice(0, 120), opacity: cs.opacity, disabled: !!el.disabled, ariaBusy: el.getAttribute("aria-busy"), ariaDisabled: el.getAttribute("aria-disabled"), text: U.name(el) }); };
  const snap = () => {
    pending = false;
    if (window.__unslopClickT === null) return;
    const t = Math.round(performance.now() - window.__unslopClickT);
    const L = U.texts().filter((l) => !before.has(l));
    const key = L.join("\n");
    if (key !== last) { window.__unslopTL.push({ tMs: t, newLines: L.slice(0, 12).map((s) => s.slice(0, 160)) }); last = key; }
    const ts = trigSig();
    if (ts !== lastTrig) { window.__unslopTrigTL.push({ tMs: t, trigger: ts === "gone" ? null : JSON.parse(ts) }); lastTrig = ts; }
  };
  window.__unslopMO && window.__unslopMO.disconnect();
  window.__unslopMO = new MutationObserver(() => { if (!pending) { pending = true; setTimeout(snap, 25); } });
  window.__unslopMO.observe(document.body, { subtree: true, childList: true, characterData: true, attributes: true });
  document.addEventListener("click", () => { if (window.__unslopClickT === null) window.__unslopClickT = performance.now(); }, { capture: true, once: true });
  window.__unslopArmed = true;
  return true;
}

function actionState(selector) {
  const U = window.__unslopU, before = window.__unslopBefore || new Set();
  const el = document.querySelector(selector);
  const cs = el ? getComputedStyle(el) : null;
  const now = U.texts();
  const nowSet = new Set(now);
  return {
    trigger: el ? { present: true, disabled: !!el.disabled, ariaDisabled: el.getAttribute("aria-disabled"), ariaBusy: el.getAttribute("aria-busy"), text: U.name(el), opacity: cs.opacity, cls: String(el.getAttribute("class") || "").slice(0, 160), cursor: cs.cursor, bg: cs.backgroundColor } : { present: false },
    newLines: now.filter((l) => !before.has(l)).slice(0, 12).map((s) => s.slice(0, 160)),
    goneLines: [...before].filter((l) => !nowSet.has(l)).slice(0, 12).map((s) => s.slice(0, 160)),
    newBusy: [...document.querySelectorAll("[aria-busy=true]")].map(U.path).filter((p) => !(window.__unslopPreBusy || new Set()).has(p)),
    newSpinners: (window.__unslopSpinners ? window.__unslopSpinners() : []).filter((p) => !(window.__unslopPreSpin || new Set()).has(p)),
    activeLiveRegions: [...document.querySelectorAll("[role=status],[role=alert],[aria-live]")].filter((e) => U.vis(e) && e.innerText.trim()).map((e) => e.innerText.trim().slice(0, 120)).slice(0, 4),
    tMs: window.__unslopClickT === null ? null : Math.round(performance.now() - window.__unslopClickT),
  };
}

function netState() {
  const T = window.__unslopClickT;
  const rel = (v) => (v === null || v === undefined || T === null ? null : Math.round(v - T));
  return { requests: window.__unslopNet.map((r) => ({ ...r, start: undefined, end: undefined, startMs: rel(r.start), endMs: rel(r.end) })), timeline: window.__unslopTL || [], triggerTimeline: window.__unslopTrigTL || [] };
}

export async function captureAsync({ browser, open, url, ev, note, prepWait = 0, budgetMs = 60000, maxActions = 4, delayMs = 3000, failDelayMs = 1500, spinnerSrc = "spin|loader|loading|progress|skeleton|busy|pending" }) {
  const dir = path.join(ev, "async");
  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir, { recursive: true });
  const t0 = Date.now();
  const out = { version: 1, viewport: [VIEW, 900], delayMs, failDelayMs, budgetMs, sampleMs: [500, 2000, "completion+1000"], actions: [], skipped: [], notVerified: [], log: [],
    guards: "cross-origin requests refused; navigation away aborted; native form submits cancelled; non-GET and file:// requests get synthetic responses; GET passes through after the hold (http pages); forms filled with fake values" };
  const { ctx, page } = await open(browser, VIEW);
  await ctx.addInitScript(pageHelpers, { delay: { slow: delayMs, fail: failDelayMs } });
  const guard = await routeGuard(ctx, page, url, out.log);
  const load = async () => { guard.armed = false; await page.goto(url, { waitUntil: "load", timeout: 45000 }); await lightSettle(page, prepWait); };
  try { await load(); } catch (e) { out.notVerified.push(`page did not load: ${e.message}`); await ctx.close(); fs.writeFileSync(path.join(ev, "async.json"), JSON.stringify(out, null, 1)); return { found: 0 }; }
  const disc = await page.evaluate(discoverActions, maxActions);
  out.found = disc.found;
  out.skipped.push(...disc.notTried);
  for (const [ai, act] of disc.actions.entries()) {
    const entry = { selector: act.selector, name: act.name, kind: act.kind, form: act.form, runs: {} };
    out.actions.push(entry);
    for (const mode of ["slow", "fail"]) {
      if (mode === "fail" && !(entry.runs.slow && entry.runs.slow.requests && entry.runs.slow.requests.some((r) => r.outcome && !r.outcome.startsWith("blocked")))) {
        entry.runs.fail = { status: "skipped", reason: "the slow run made no same-origin request, so there is nothing to fail" }; continue; }
      if (Date.now() - t0 > budgetMs) { entry.runs[mode] = { status: "skipped", reason: `time budget ${budgetMs} ms used up` }; continue; }
      const run = { status: "ok", mode, holdMs: mode === "slow" ? delayMs : failDelayMs };
      entry.runs[mode] = run;
      let navigated = false;
      const onNav = (f) => { if (f === page.mainFrame()) navigated = true; };
      try {
        await load();
        page.on("framenavigated", onNav);
        run.filled = await page.evaluate(fillForm, act.form);
        await page.evaluate((s) => { const e = document.querySelector(s); if (e) e.scrollIntoView({ block: "center" }); }, act.selector);
        const box = await page.evaluate((s) => { const e = document.querySelector(s); if (!e) return null; const r = e.getBoundingClientRect();
          const h = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2); return [r.left, r.top, r.width, r.height, !!h && (h === e || e.contains(h))]; }, act.selector);
        if (!box) { run.status = "not-verified"; run.reason = "action not found after reload"; continue; }
        await page.mouse.move(box[0] + box[2] / 2, box[1] + box[3] / 2);
        await page.waitForTimeout(400);
        const shot = (label) => `async/a${ai}-${mode}-${label}.png`;
        await page.evaluate(armAction, { selector: act.selector, mode, spinnerSrc });
        const before = await page.evaluate(actionState, act.selector);
        await page.screenshot({ path: path.join(ev, shot("before")) });
        run.before = { shot: shot("before"), state: before };
        guard.armed = true;
        const clickAt = Date.now();
        if (box[4]) await page.mouse.click(box[0] + box[2] / 2, box[1] + box[3] / 2);
        else await page.evaluate((s) => document.querySelector(s).click(), act.selector);
        run.samples = [];
        const sample = async (label) => {
          if (navigated) return;
          const st = await page.evaluate(actionState, act.selector).catch(() => null);
          if (!st) return;
          try { await page.screenshot({ path: path.join(ev, shot(label)) }); } catch {}
          run.samples.push({ label, shot: shot(label), state: st });
        };
        for (const [label, at] of [["0.5s", 500], ["2s", 2000]]) {
          const wait = at - (Date.now() - clickAt);
          if (wait > 0) await page.waitForTimeout(wait);
          await sample(label);
        }
        // completion: every same-origin request ended, then 1 s for the UI to respond (cap 9 s after the click)
        let done = null;
        while (!navigated && Date.now() - clickAt < 9000) {
          const n = await page.evaluate(netState).catch(() => null);
          if (!n) break;
          const open_ = n.requests.filter((r) => r.endMs === null);
          if (!open_.length) { done = n.requests.length ? Math.max(...n.requests.map((r) => r.endMs || 0)) : 0; break; }
          await page.waitForTimeout(100);
        }
        run.completionMs = done;
        if (done === null && !navigated) run.completionNote = "requests still open 9 s after the click";
        const settleUntil = Math.max(2000, (done || 0)) + 1000;
        const wait = settleUntil - (Date.now() - clickAt);
        if (wait > 0) await page.waitForTimeout(wait);
        await sample("final");
        const n = await page.evaluate(netState).catch(() => ({ requests: [], timeline: [] }));
        run.requests = n.requests; run.timeline = n.timeline; run.triggerTimeline = n.triggerTimeline;
        if (navigated) { run.status = "not-verified"; run.reason = "the click navigated the page"; }
      } catch (e) { run.status = "not-verified"; run.reason = `error: ${e.message.split("\n")[0]}`; }
      finally { guard.armed = false; page.off("framenavigated", onNav); try { await page.evaluate(() => { window.__unslopArmed = false; }); } catch {} }
    }
  }
  await ctx.close();
  out.elapsedMs = Date.now() - t0;
  fs.writeFileSync(path.join(ev, "async.json"), JSON.stringify(out, null, 1));
  note(`async: ${out.found} action(s) found, ${out.actions.length} tried in ${out.elapsedMs} ms`);
  return { found: out.found, tried: out.actions.length, skipped: out.skipped.length, notVerified: out.notVerified, elapsedMs: out.elapsedMs };
}
