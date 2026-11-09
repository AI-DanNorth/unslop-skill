// Runs inside the page (page.evaluate). Returns a JSON-safe dump of the rendered page.
// Keep it dependency-free: it is injected as a string.
(() => {
  const STYLE_KEYS = ["display","visibility","opacity","position","fontFamily","fontSize","fontWeight","fontStyle","letterSpacing",
    "textTransform","lineHeight","color","backgroundColor","backgroundImage","borderTopWidth","borderRightWidth","borderBottomWidth",
    "borderLeftWidth","borderTopColor","borderLeftColor","borderRightColor","borderBottomColor","borderTopLeftRadius","boxShadow",
    "marginTop","marginBottom","paddingTop","paddingBottom","paddingLeft","paddingRight","gap","rowGap","columnGap","textAlign",
    "outlineStyle","outlineWidth","outlineColor","outlineOffset","transitionProperty","transitionDuration","transitionTimingFunction",
    "animationName","animationDuration","overflowX","whiteSpace","textShadow","filter","backdropFilter","zIndex","gridTemplateColumns","width","height"];
  const SKIP = new Set(["SCRIPT","STYLE","NOSCRIPT","TEMPLATE","META","LINK","HEAD","TITLE","BR"]);
  const docH = Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0);
  const vw = window.innerWidth, vh = window.innerHeight;

  function sel(el) {
    if (el.id) return `#${CSS.escape(el.id)}`;
    const parts = [];
    let e = el;
    while (e && e.nodeType === 1 && parts.length < 5) {
      let p = e.tagName.toLowerCase();
      if (e.classList.length) p += "." + [...e.classList].slice(0, 2).map(c => CSS.escape(c)).join(".");
      const par = e.parentElement;
      if (par) { const sib = [...par.children].filter(c => c.tagName === e.tagName); if (sib.length > 1) p += `:nth-of-type(${sib.indexOf(e) + 1})`; }
      parts.unshift(p);
      if (e.id) break;
      e = par;
    }
    return parts.join(" > ");
  }
  function ownText(el) {
    let t = "";
    for (const n of el.childNodes) { if (n.nodeType === 3) t += n.textContent; else if (n.nodeName === "BR") t += " "; }   // <br> separates words
    return t.replace(/\s+/g, " ").trim();
  }
  function visible(el, cs, r) {
    if (cs.display === "none" || cs.visibility === "hidden" || cs.visibility === "collapse") return false;
    if (r.width < 1 || r.height < 1) return false;
    let e = el, op = 1;
    while (e && e.nodeType === 1) { const c = getComputedStyle(e); op *= parseFloat(c.opacity); if (c.display === "none") return false; e = e.parentElement; }
    if (op < 0.05) return false;
    if (cs.clipPath && cs.clipPath.startsWith("inset(50%")) return false;
    return true;
  }
  function effOpacity(el) { let e = el, op = 1; while (e && e.nodeType === 1) { op *= parseFloat(getComputedStyle(e).opacity); e = e.parentElement; } return op; }
  function accName(el) {
    const al = el.getAttribute("aria-label"); if (al && al.trim()) return al.trim();
    const lb = el.getAttribute("aria-labelledby");
    if (lb) { const t = lb.split(/\s+/).map(id => (document.getElementById(id) || {}).textContent || "").join(" ").trim(); if (t) return t; }
    if (el.labels && el.labels.length) { const t = [...el.labels].map(l => l.textContent).join(" ").trim(); if (t) return t; }
    if (el.tagName === "IMG") return (el.getAttribute("alt") || "").trim();
    if (el.tagName === "INPUT" && ["submit","button","reset"].includes(el.type)) return (el.value || "").trim();
    const t = (el.innerText || el.textContent || "").replace(/\s+/g, " ").trim(); if (t) return t;
    // Name from content also includes descendants' aria-label and alt, as Chromium computes it. Reading only the first
    // img[alt] gave empty names for icon buttons (live round 1: L25 x2, L27 x10, L33 x3, L34 x2; e.g. Ant's
    // <span role="img" aria-label="left">). Descendants inside an aria-hidden subtree or not rendered do not count.
    const parts = [...el.querySelectorAll("svg[aria-label], [role=img][aria-label], img[alt]")].filter(x => {
      const h = x.closest("[aria-hidden='true']"); if (h && h !== el && el.contains(h)) return false;
      return x.getClientRects().length > 0 && getComputedStyle(x).visibility !== "hidden";
    }).map(x => (x.getAttribute("aria-label") || x.getAttribute("alt") || "").trim()).filter(Boolean);
    if (parts.length) return parts.join(" ");
    const svgT = el.querySelector("svg title"); if (svgT) return svgT.textContent.trim();
    return (el.getAttribute("title") || "").trim();
  }

  const els = [];
  let idx = 0;
  for (const el of document.body ? document.body.querySelectorAll("*") : []) {
    if (SKIP.has(el.tagName)) continue;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const vis = visible(el, cs, r);
    const text = ownText(el);
    const id = idx++;
    el.setAttribute("data-unslop-id", String(id));
    const st = {};
    for (const k of STYLE_KEYS) st[k] = cs[k];
    const rec = { id, tag: el.tagName.toLowerCase(), sel: sel(el), vis, text, textLen: text.length,
      rect: { x: Math.round(r.left + scrollX), y: Math.round(r.top + scrollY), w: Math.round(r.width), h: Math.round(r.height) },
      style: st, opacity: vis ? effOpacity(el) : 0, parent: el.parentElement ? el.parentElement.getAttribute("data-unslop-id") : null,
      before: getComputedStyle(el, "::before").content, after: getComputedStyle(el, "::after").content };
    const interactive = el.matches("a[href],button,input,select,textarea,summary,[role=button],[role=link],[tabindex]:not([tabindex='-1'])");
    // tabindex: heading anchors like <a aria-hidden="true" tabindex="-1"> are out of the tab order (live round 1: L34 x6,
    // L33 disabled pager tabindex=-1). Recorded on every interactive element (null = no attribute) and wherever it is set.
    const tabindex = el.getAttribute("tabindex");
    if (interactive || tabindex !== null) rec.tabindex = tabindex;
    if (interactive) { rec.interactive = true; rec.name = accName(el); rec.type = el.type || null; rec.role = el.getAttribute("role"); rec.href = el.getAttribute("href"); rec.inFooter = !!el.closest("footer,[role=contentinfo]"); }
    if (el.tagName === "IMG") { rec.img = { alt: el.getAttribute("alt"), src: el.currentSrc || el.src, nw: el.naturalWidth, nh: el.naturalHeight, complete: el.complete, loading: el.loading }; }
    if (["INPUT","SELECT","TEXTAREA"].includes(el.tagName)) { rec.field = { type: el.type, name: el.name, placeholder: el.getAttribute("placeholder"), autocomplete: el.getAttribute("autocomplete"), labelled: !!accName(el) }; }   // accName never reads the placeholder, so a real aria-label equal to it is still a label (live round 1: L27 #newsletter-email)
    if (vis && text) {      // where the glyphs actually are: rects of this element's own text nodes
      const tr = [];
      for (const n of el.childNodes) {
        if (n.nodeType !== 3 || !n.textContent.trim()) continue;
        const rg = document.createRange(); rg.selectNodeContents(n);
        for (const b of rg.getClientRects()) if (b.width >= 2 && b.height >= 4 && tr.length < 12) tr.push([Math.round(b.left + scrollX), Math.round(b.top + scrollY), Math.round(b.width), Math.round(b.height)]);
      }
      if (tr.length) rec.textRects = tr;
    }
    if (vis && !["inline", "contents"].includes(cs.display)) {
      const bt = (el.innerText || "").replace(/\s+/g, " ").trim();
      if (bt.length >= 3 && bt.length <= 300 && bt !== text) rec.blockText = bt;
    }
    rec.inDialog = !!el.closest("dialog,[role=dialog],[role=menu],[role=listbox],details:not([open]),[aria-hidden=true],template,[hidden]");
    if (/^H[1-6]$/.test(el.tagName)) rec.level = +el.tagName[1];
    if (vis && (/^H[1-6]$/.test(el.tagName) || el.tagName === "P") && (el.textContent || "").length <= 300) {
      const rg = document.createRange(); rg.selectNodeContents(el);
      const rows = new Map();
      for (const b of rg.getClientRects()) { if (b.width < 1) continue; const k = Math.round(b.top / 4); const v = rows.get(k) || [Infinity, -Infinity]; rows.set(k, [Math.min(v[0], b.left), Math.max(v[1], b.right)]); }
      const lw = [...rows.entries()].sort((a, b) => a[0] - b[0]).map(([, v]) => Math.round(v[1] - v[0]));
      if (lw.length > 1) rec.lines = lw;
    }
    if (el.getAttribute("aria-hidden") === "true") rec.ariaHidden = true;
    // icons: class names (icon sets name their glyphs: lucide-sparkles, ph-magic-wand, fa-wand-magic-sparkles) and how an
    // SVG glyph is painted (filled vs outline), for ai_sparkle and mixed_icons
    const cls = typeof el.className === "string" ? el.className : (el.className && el.className.baseVal) || "";
    if (el.tagName.toLowerCase() === "svg") {
      const shapes = [...el.querySelectorAll("path,circle,rect,polygon,ellipse,line,polyline,use")];
      const sh = shapes[0], ss = sh ? getComputedStyle(sh) : null;
      rec.icon = { svg: true, cls: cls.slice(0, 120), lucide: el.getAttribute("data-lucide") || null, label: el.getAttribute("aria-label") || null,
        fill: ss ? ss.fill : cs.fill, stroke: ss ? ss.stroke : cs.stroke, strokeWidth: ss ? ss.strokeWidth : cs.strokeWidth, shapes: shapes.length };
    } else if (cls && /(^|[\s-])(icon|icons|fa|fas|far|fa-solid|fa-regular|bi|ph|ti|ri|lni|material-symbols[\w-]*|material-icons[\w-]*)($|[\s-])/i.test(cls) && r.width <= 64 && r.height <= 64) {
      rec.icon = { svg: false, cls: cls.slice(0, 120) };
    }
    els.push(rec);
  }

  // stylesheet text (same-origin only), custom properties on :root
  const css = [];
  for (const ss of document.styleSheets) { try { for (const r of ss.cssRules) css.push(r.cssText); } catch (e) { css.push(`/* unreadable: ${ss.href} */`); } }
  const rootCs = getComputedStyle(document.documentElement);
  const tokens = {};
  for (const t of css.join("\n").matchAll(/(--[\w-]+)\s*:/g)) tokens[t[1]] = rootCs.getPropertyValue(t[1]).trim();
  const meta = {};
  for (const m of document.querySelectorAll("meta[name]")) meta[m.name] = m.content;
  const forms = [...document.querySelectorAll("form")].map(f => ({ sel: sel(f), action: f.getAttribute("action"), method: f.method, fields: f.querySelectorAll("input,select,textarea").length }));
  return {
    url: location.href, title: document.title, lang: document.documentElement.getAttribute("lang"), meta,
    viewport: { w: vw, h: vh }, docH, docW: document.documentElement.scrollWidth,
    bodyBg: getComputedStyle(document.body).backgroundColor, htmlBg: rootCs.backgroundColor,
    bodyText: (document.body.innerText || "").replace(/[ \t]+/g, " "),
    elements: els, css, tokens, forms,
    landmarks: { main: document.querySelectorAll("main,[role=main]").length, nav: document.querySelectorAll("nav,[role=navigation]").length,
                 footer: document.querySelectorAll("footer,[role=contentinfo]").length, header: document.querySelectorAll("header,[role=banner]").length },
    firstFocusable: (() => { const f = document.querySelector("a[href],button,input,select,textarea,[tabindex]:not([tabindex='-1'])"); return f ? { tag: f.tagName.toLowerCase(), href: f.getAttribute("href"), text: (f.textContent || "").trim().slice(0, 60) } : null; })(),
  };
})()
