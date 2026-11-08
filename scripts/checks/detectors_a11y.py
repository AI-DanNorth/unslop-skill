"""Accessibility, robustness, motion, performance and capture-integrity detectors."""
import re, collections, json, math
from core import detector, hit, px, where, Skip, NotVerified, ROOT
import colorlib as cl

def in_tag(ev, e, tags, w=None):
    return any(a["tag"] in tags for a in ev.ancestors(e, w)) or e["tag"] in tags

# ------------------------------------------------------------------ contrast on real pixels
@detector("contrast")
def contrast(ev, cfg):
    import numpy as np
    out = []
    widths = [w for w in ev.widths if ev.has(f"bg-{w}.png")]
    if not widths: raise NotVerified("no background-only render (bg-<w>.png)")
    for w in widths:
        bg = ev.img(f"bg-{w}.png")
        H, W = bg.shape[:2]
        dead = [x["rect"] for x in ev.dom(w)["elements"] if x.get("img") and x["vis"] and not x["img"].get("nw")]
        if (ev.manifest.get("network") or {}).get("blockedImages"):
            dead += [a["rect"] for a in ev.dom(w)["elements"] if a["vis"] and "url(" in a["style"]["backgroundImage"]]
        def over_dead(r): return any(d["x"] <= r["x"] + r["w"] / 2 <= d["x"] + d["w"] and d["y"] <= r["y"] + r["h"] / 2 <= d["y"] + d["h"] for d in dead)
        for e in ev.texts(w, min_len=2):
            if e.get("ariaHidden") or over_dead(e["rect"]): continue      # background image failed to load: not verifiable
            c = cl.parse(e["style"]["color"])
            if not c or c[3] == 0: continue
            alpha = c[3] * e.get("opacity", 1)
            boxes = e.get("textRects") or [[e["rect"]["x"], e["rect"]["y"], e["rect"]["w"], e["rect"]["h"]]]
            samples = []
            for bx, by, bw, bh in boxes:
                x0, y0, x1, y1 = max(0, bx + 1), max(0, by + 2), min(W, bx + bw - 1), min(H, by + bh - 2)
                if x1 - x0 < 2 or y1 - y0 < 2: continue
                xs = np.linspace(x0, x1 - 1, max(2, min(24, (x1 - x0) // 6))).astype(int); ys = np.linspace(y0, y1 - 1, max(2, min(6, (y1 - y0) // 3))).astype(int)
                samples.extend(bg[np.ix_(ys, xs)].reshape(-1, 3) / 255.0)
            if len(samples) < 4: continue
            ratios = sorted(((cl.contrast(cl.over((c[0], c[1], c[2], alpha), tuple(s_) + (1,)), s_), s_) for s_ in samples), key=lambda t: t[0])
            p10 = ratios[max(0, int(len(ratios) * 0.10) - 1)]
            worst, ws = p10
            absmin = ratios[0][0]
            size, weight = px(e["style"]["fontSize"]), int(e["style"]["fontWeight"] or 400)
            large = size >= cfg["large_px"] or (size >= cfg["large_bold_px"] and weight >= 700)
            need = cfg["large"] if large else cfg["body"]
            if worst < need - 0.005:
                lc = cl.apca(cl.over((c[0], c[1], c[2], alpha), tuple(ws) + (1,)), ws)
                out.append(hit(cfg, where(e), f"{worst:.2f}:1 against the background behind the text (10th-percentile pixel {cl.hexstr(ws)}, worst {absmin:.2f}:1; text {cl.hexstr(c)}{', opacity %.2f' % alpha if alpha < 1 else ''}, {size:.0f}px; needs {need}:1). APCA Lc {abs(lc):.0f} (advisory)",
                               value=round(worst, 2), width=w, tier="Floor"))
    # one finding per selector+evidence
    seen, res = set(), []
    for h in out:
        k = (h["where"], h["value"])
        if k not in seen: seen.add(k); res.append(h)
    return res[:15]

@detector("text_floor")
def text_floor(ev, cfg):
    out = []; labels = []
    floor = cfg["body_px"]
    for e in ev.texts(min_len=1):
        s = px(e["style"]["fontSize"])
        if in_tag(ev, e, ("footer", "figcaption", "small", "caption", "sup", "sub", "code", "pre", "label", "th", "td", "nav", "button")): continue
        if e["textLen"] >= cfg["min_run_chars"] and s < floor - 0.1:
            hard = cfg.get("hard_px", cfg["dense_ui_px"])
            tier, pr = ("Floor", "P0") if s < hard - 0.1 else (("Reflex", "P1") if s < cfg["dense_ui_px"] - 0.1 else ("Finish", "P3"))
            out.append(hit(cfg, where(e), f"{e['textLen']}-character run at {s:.0f}px (hard floor {hard}px, dense UI {cfg['dense_ui_px']}px, body {floor}px)", value=s, tier=tier, priority=pr))
        elif e["textLen"] < cfg["min_run_chars"] and s < cfg["label_px"] - 0.1:
            labels.append(e)
    if len(labels) > cfg["max_label_runs"]:
        out += [hit(cfg, where(e), f"label at {px(e['style']['fontSize']):.0f}px (label floor {cfg['label_px']}px; {len(labels)} such)", tier="Reflex") for e in labels[:5]]
    return out[:12]

@detector("focus_ring", needs=("focus.json",))
def focus_ring(ev, cfg):
    import numpy as np
    from PIL import Image
    stops = ev.json("focus.json")
    if not stops:
        if not any(e.get("interactive") for e in ev.visible()): raise Skip("page has no interactive controls")
        return [hit(cfg, "page", "Tab reached no focusable element although the page has controls", tier="Floor")]
    out = []
    for s in stops:
        if s.get("tag") == "iframe": continue        # focus moved into a frame: its own document is not captured here
        if s.get("covered"):
            out.append(hit(cfg, f"{s['tag']} \"{s['text']}\"", "focused element is covered by a fixed or sticky element", tier="Floor"))
        if not (s.get("on") and s.get("off")): continue
        a = np.asarray(Image.open(ev.dir / s["on"]).convert("RGB")).astype("int16")
        b = np.asarray(Image.open(ev.dir / s["off"]).convert("RGB")).astype("int16")
        if a.shape != b.shape: continue
        diff = np.abs(a - b).max(axis=2) > 40
        if diff.mean() < 0.004:
            out.append(hit(cfg, f"{s['tag']} \"{s['text']}\"", f"no visible focus indicator (outline: {s['outline']})", tier="Floor",
                           after="Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground.")); continue
        on, off = a[diff] / 255.0, b[diff] / 255.0
        ratios = sorted(cl.contrast(tuple(x) + (1,), tuple(y) + (1,)) for x, y in zip(on[::max(1, len(on) // 400)], off[::max(1, len(off) // 400)]))
        best = ratios[int(len(ratios) * 0.9)] if ratios else 0
        if best < cfg["fail_below"]:
            out.append(hit(cfg, f"{s['tag']} \"{s['text']}\"", f"focus indicator visible but faint: {best:.2f}:1 against the unfocused state (target {cfg['min_contrast']}:1, WCAG 2.4.13)", value=round(best, 2), tier="Reflex", priority="P2"))
    return out[:10]

@detector("targets")
def targets(ev, cfg):
    out = []
    for w in ev.widths:
        touch = w <= 768
        for e in ev.visible(w):
            if not e.get("interactive"): continue
            if e["tag"] == "a" and e["style"]["display"] == "inline" and ev.dom(w)["byid"].get(int(e["parent"]) if e.get("parent") else -1, {}).get("tag") in ("p", "li", "td", "dd", "span", "label", "figcaption", "caption"):
                continue      # inline link in running text: WCAG 2.5.8 exception
            if e["rect"]["y"] < 0: continue
            ww, hh = e["rect"]["w"], e["rect"]["h"]
            small = ww < cfg["floor_px"] or hh < cfg["floor_px"]
            if small:      # spacing exception: a 24px circle on its centre must not meet another target's circle
                cx, cy = e["rect"]["x"] + ww / 2, e["rect"]["y"] + hh / 2
                crowded = any(o is not e and o.get("interactive") and math.hypot(o["rect"]["x"] + o["rect"]["w"] / 2 - cx, o["rect"]["y"] + o["rect"]["h"] / 2 - cy) < cfg["floor_px"] for o in ev.visible(w))
                small = crowded
            if small:
                out.append(hit(cfg, where(e), f"target {ww}x{hh}px at {w}px, closer than {cfg['floor_px']}px to another target (WCAG 2.5.8)", tier="Floor", width=w))
            elif touch and min(ww, hh) >= 1 and (ww < cfg["touch_px"] or hh < cfg["touch_px"]) and e["tag"] not in ("input", "textarea", "select"):
                out.append(hit(cfg, where(e), f"touch target {ww}x{hh}px at {w}px (min {cfg['touch_px']}px)", tier=cfg.get("touch_tier", "Reflex"), width=w))
    seen, res = set(), []
    for h in out:
        if (h["where"], h["tier"]) not in seen: seen.add((h["where"], h["tier"])); res.append(h)
    return res[:12]

@detector("img_alt")
def img_alt(ev, cfg):
    out = []
    for e in ev.dom()["elements"]:
        if e["tag"] != "img" or e.get("ariaHidden"): continue
        alt = e["img"].get("alt")
        if alt is None: out.append(hit(cfg, where(e), f"img without alt: {(e['img'].get('src') or '')[-60:]}", tier="Floor"))
        elif re.search(r"\.(png|jpe?g|webp|gif|svg)$|^(img|image|photo|picture)[\s_-]?\d*$", alt.strip(), re.I):
            out.append(hit(cfg, where(e), f"alt text is a file name or generic word: \"{alt}\"", tier="Reflex"))
    return out

@detector("control_names")
def control_names(ev, cfg):
    out = []
    for e in ev.visible():
        if not e.get("interactive") or e.get("type") in ("hidden",): continue
        if not (e.get("name") or "").strip():
            out.append(hit(cfg, where(e), f"{e['tag']}{'[type=%s]' % e['type'] if e.get('type') else ''} has no accessible name", tier="Floor"))
    return out[:10]

@detector("headings_landmarks")
def headings_landmarks(ev, cfg):
    d = ev.dom(); out = []
    hs = [e for e in d["elements"] if e.get("level") and e["vis"]]
    h1 = [e for e in hs if e["level"] == 1]
    if len(h1) != 1: out.append(hit(cfg, "page", f"{len(h1)} visible h1 elements (expected 1)", value=len(h1)))
    prev = 0
    for e in hs:
        if prev and e["level"] > prev + 1: out.append(hit(cfg, where(e), f"heading jumps from h{prev} to h{e['level']}"))
        prev = e["level"]
    for lm in ("main",):
        if not d["landmarks"].get(lm): out.append(hit(cfg, "page", f"no <{lm}> landmark"))
    ff = d.get("firstFocusable")
    if ff and not (ff["tag"] == "a" and (ff.get("href") or "").startswith("#")):
        out.append(hit(cfg, "page", f"first focusable element is {ff['tag']} \"{ff['text'][:30]}\", not a skip link", tier="Reflex", priority="P2"))
    return out

GENERIC_TITLES = re.compile(r"^(home|untitled|document|index|page|new page|landing page|website|my app|app)$", re.I)

@detector("lang_and_title")
def lang_and_title(ev, cfg):
    d = ev.dom(); out = []
    if not (d.get("lang") or "").strip(): out.append(hit(cfg, "<html>", "no lang attribute", tier="Floor"))
    t = (d.get("title") or "").strip()
    if not t: out.append(hit(cfg, "<title>", "page has no title", tier="Floor"))
    elif GENERIC_TITLES.match(t): out.append(hit(cfg, "<title>", f"title \"{t}\" does not describe the page", tier="Reflex"))
    return out

@detector("zoom_blocked")
def zoom_blocked(ev, cfg):
    v = (ev.dom()["meta"].get("viewport") or "").lower().replace(" ", "")
    out = []
    if re.search(r"user-scalable=(no|0)", v): out.append(hit(cfg, "meta viewport", f"zoom disabled: {v}", tier="Floor"))
    m = re.search(r"maximum-scale=([\d.]+)", v)
    if m and float(m.group(1)) < 2: out.append(hit(cfg, "meta viewport", f"maximum-scale={m.group(1)} blocks zoom", tier="Floor"))
    return out

@detector("form_labels")
def form_labels(ev, cfg):
    out = []
    for e in ev.visible():
        f = e.get("field")
        if not f or f["type"] in ("hidden", "submit", "button", "reset", "image"): continue
        if not f["labelled"]:
            out.append(hit(cfg, where(e), f"{e['tag']}[type={f['type']}] has no label{' (placeholder \"%s\" is not a label)' % f['placeholder'] if f.get('placeholder') else ''}", tier="Floor"))
        elif f["type"] in ("email", "tel") and not f.get("autocomplete"):
            out.append(hit(cfg, where(e), f"{f['type']} field without autocomplete", tier="Reflex", priority="P2"))
    return out

@detector("reduced_motion")
def reduced_motion(ev, cfg):
    css = "\n".join(ev.dom()["css"])
    moving = re.search(r"@keyframes|animation(-name)?\s*:\s*(?!none)[\w-]+", css) or re.search(r"transition[^;{}]*(transform|translate|scale|rotate|all)", css)
    if not moving: raise Skip("no animation or movement in stylesheets")
    if re.search(r"prefers-reduced-motion", css): return []
    anim = [e for e in ev.visible() if e["style"]["animationName"] not in ("none", "")]
    w = where(anim[0]) if anim else "stylesheet"
    return [hit(cfg, w, "page animates (keyframes or transform transitions) but has no prefers-reduced-motion rule", tier="Floor")]

# ------------------------------------------------------------------ robustness
@detector("hidden_content", needs=("hidden.json",))
def hidden_content(ev, cfg):
    h = ev.json("hidden.json"); base = h.get("baseline", {})
    if "visibleChars" not in base: raise NotVerified("baseline condition did not run")
    B, T = base["visibleChars"], base["totalChars"]
    out = []
    if T and 1 - B / T > cfg["max_hidden_share"]:
        out.append(hit(cfg, "page after load", f"{100*(1-B/T):.0f}% of text is hidden after load and scrolling (max {100*cfg['max_hidden_share']:.0f}%; menus and dialogs excluded)", tier="Reflex"))
    for cond in ("reduced_motion", "observer_never_fires", "scripts_off"):
        c = h.get(cond, {})
        if "visibleChars" not in c: out.append(hit(cfg, cond, f"condition did not run: {c.get('error', 'unknown')}", tier="Reflex")); continue
        lost = B - c["visibleChars"]
        if lost > max(100, 0.02 * B):
            label = {"reduced_motion": "with reduced motion", "observer_never_fires": "when IntersectionObserver never fires", "scripts_off": "with JavaScript off"}[cond]
            out.append(hit(cfg, cond, f"{lost} characters ({100*lost/max(1,B):.0f}% of text) stay invisible {label}", value=lost, tier="Floor",
                           after="Render content visible by default; animate from visible, never to visible."))
    return out

@detector("phone_parity")
def phone_parity(ev, cfg):
    if cfg["desktop"] not in ev.widths or cfg["phone"] not in ev.widths: raise Skip(f"needs captures at {cfg['desktop']} and {cfg['phone']}")
    big, small = ev.dom(cfg["desktop"]), ev.dom(cfg["phone"])
    same = len(big["elements"]) == len(small["elements"])
    smap = {e["id"]: e for e in small["elements"]} if same else {e["sel"]: e for e in small["elements"]}
    lost, ex = 0, []
    for e in big["elements"]:
        if not e["vis"] or not e["textLen"] or in_tag(ev, e, ("nav", "header"), cfg["desktop"]): continue
        o = smap.get(e["id"] if same else e["sel"])
        if o is not None and not o["vis"]:
            n = len(e["text"].split()); lost += n; ex.append(e)
    if lost >= cfg["max_hidden_words"]:
        return [hit(cfg, where(ex[0]), f"{lost} words shown at {cfg['desktop']}px are hidden at {cfg['phone']}px ({len(ex)} elements)", value=lost)]
    return []

@detector("overflow")
def overflow(ev, cfg):
    out = []
    for w in ev.widths:
        d = ev.dom(w)
        if d["docW"] > w + cfg["tolerance_px"]:
            culprits = [e for e in d["elements"] if e["vis"] and e["rect"]["x"] + e["rect"]["w"] > w + cfg["tolerance_px"]
                        and not any(a["style"]["overflowX"] in ("auto", "scroll", "hidden", "clip") for a in ev.ancestors(e, w))]
            culprits.sort(key=lambda e: -e["rect"]["w"])
            c = culprits[0] if culprits else None
            out.append(hit(cfg, where(c) if c else "page", f"page is {d['docW']}px wide at a {w}px viewport (sideways scroll){'; widest culprit %dpx' % c['rect']['w'] if c else ''}", tier="Floor", width=w, value=d["docW"]))
    return out

@detector("widows")
def widows(ev, cfg):
    out = []
    for w in cfg["widths"]:
        if w not in ev.widths: continue
        for e in ev.texts(w):
            ln = e.get("lines")
            if not ln or len(ln) > 4: continue
            share = ln[-1] / max(ln)
            if share < cfg["min_last_line_share"]:
                out.append(hit(cfg, where(e), f"last line is {100*share:.0f}% of the measure at {w}px ({len(ln)} lines)", width=w, tier="Finish", value=round(share, 2)))
    return out[:8]

@detector("motion_css")
def motion_css(ev, cfg):
    css = "\n".join(ev.dom()["css"])
    out = []
    for m in re.finditer(r"([^{}]+)\{[^}]*?(transition(-property)?\s*:\s*all\b[^;}]*)", css):
        out.append(hit(cfg, m.group(1).strip()[:60], f"\"{m.group(2).strip()[:60]}\": transition all animates layout and paint properties", after="List the properties: transition: transform 160ms, opacity 160ms"))
    allt = [e for e in ev.visible() if e["style"]["transitionProperty"].split(",")[0].strip() == "all" and any(float(x.strip().rstrip("ms").rstrip("s") or 0) > 0 for x in e["style"]["transitionDuration"].split(","))]
    if allt:
        out.append(hit(cfg, where(allt[0]), f"{len(allt)} elements transition \"all\" ({allt[0]['style']['transitionDuration']}): every property change animates, including layout", value=len(allt),
                       after="List the properties: transition: transform 160ms, opacity 160ms"))
    layout = "|".join(cfg["layout_props"])
    for m in re.finditer(r"([^{}]+)\{[^}]*?transition(-property)?\s*:\s*([^;}]*)", css):
        props = m.group(3)
        if re.search(r"(^|[\s,])(" + layout + r")(\s|,|$)", props) and "all" not in props:
            out.append(hit(cfg, m.group(1).strip()[:60], f"transition on a layout property: \"{props.strip()[:60]}\"", after="Animate transform or opacity instead"))
    for m in re.finditer(r"cubic-bezier\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)", css):
        y1, y2 = float(m.group(2)), float(m.group(4))
        if max(y1, y2) > cfg["max_overshoot"] or min(y1, y2) < -0.05:
            out.append(hit(cfg, "stylesheet", f"overshoot easing {m.group(0)} (y beyond 0..{cfg['max_overshoot']})", after="Use a non-overshoot curve such as cubic-bezier(0.16, 1, 0.3, 1)"))
    seen, res = set(), []
    for h in out:
        if h["evidence"] not in seen: seen.add(h["evidence"]); res.append(h)
    return res[:8]

@detector("performance", needs=("perf.json",))
def performance(ev, cfg):
    p = ev.json("perf.json"); out = []
    lcp = p.get("lcp") or 0
    if lcp > cfg["lcp_fail_ms"]: out.append(hit(cfg, "page", f"lab LCP {lcp:.0f}ms (fail > {cfg['lcp_fail_ms']}ms)", value=round(lcp), priority="P1"))
    elif lcp > cfg["lcp_warn_ms"]: out.append(hit(cfg, "page", f"lab LCP {lcp:.0f}ms (warn > {cfg['lcp_warn_ms']}ms)", value=round(lcp), priority="P2"))
    for im in p.get("images", []):
        kb = (im.get("bytes") or 0) / 1024
        if kb > cfg["image_max_kb"]: out.append(hit(cfg, (im.get("src") or "")[-60:], f"image is {kb:.0f}KB (max {cfg['image_max_kb']}KB)", value=round(kb)))
        if im.get("rw") and im.get("nw") and im["nw"] > cfg["image_max_ratio"] * im["rw"] * 2:     # allow 2x for retina
            out.append(hit(cfg, (im.get("src") or "")[-60:], f"image is {im['nw']}px wide but shown at {im['rw']}px", value=im["nw"]))
    if p.get("isFile") and lcp: out.append({"rule": cfg["rule"], "tier": "info", "where": "page", "evidence": "local file: LCP excludes network time"})
    return [h for h in out if h["tier"] != "info"]

# ------------------------------------------------------------------ capture integrity
@detector("near_blank")
def near_blank(ev, cfg):
    import numpy as np
    out = []
    for w in ev.widths:
        name = f"shot-{w}.png"
        if not ev.has(name): continue
        a = ev.img(name)[::4, ::4].astype("int16")
        flat = a.reshape(-1, 3)
        q = (flat // 16).astype("int32"); keys = q[:, 0] * 256 + q[:, 1] * 16 + q[:, 2]
        mode = np.bincount(keys).argmax()
        dom = np.array([(mode // 256) * 16 + 8, ((mode // 16) % 16) * 16 + 8, (mode % 16) * 16 + 8])
        share = (np.abs(flat - dom).max(axis=1) > cfg["level"]).mean()
        if share < cfg["max_diff_share"]:
            out.append(hit(cfg, name, f"screenshot is near-blank: {100*share:.2f}% of pixels differ from the dominant colour (min {100*cfg['max_diff_share']}%)", tier="Floor", width=w))
    return out

@detector("redesign_loss")
def redesign_loss(ev, cfg):
    run = ev.run / "run.json"
    base = json.loads(run.read_text()).get("baseline_run") if run.exists() else None
    if not base: raise Skip("redesign workflow only (no baseline_run in run.json)")
    from core import Evidence
    old = Evidence(base)
    o, n = old.dom(), ev.dom()
    out = []
    ow, nw = len(old.words()), len(ev.words())
    if ow and (ow - nw) / ow > cfg["max_word_drop"]: out.append(hit(cfg, "page", f"word count fell {ow} -> {nw} ({100*(ow-nw)/ow:.0f}%)", tier="Floor"))
    links = lambda d: {e.get("href") for e in d["elements"] if e.get("href")}
    lost = links(o) - links(n)
    if lost: out.append(hit(cfg, "page", f"{len(lost)} links removed: {', '.join(sorted(lost)[:5])}", tier="Floor"))
    fields = lambda d: {(e["field"]["name"] or e["sel"]) for e in d["elements"] if e.get("field")}
    lf = fields(o) - fields(n)
    if lf: out.append(hit(cfg, "page", f"{len(lf)} form fields removed: {', '.join(sorted(lf)[:5])}", tier="Floor"))
    return out
