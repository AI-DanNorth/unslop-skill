"""Accessibility, robustness, motion, performance and capture-integrity detectors."""
import re, collections, json, math
from core import detector, hit, px, where, Skip, NotVerified, ROOT
import colorlib as cl

def in_tag(ev, e, tags, w=None):
    return any(a["tag"] in tags for a in ev.ancestors(e, w)) or e["tag"] in tags

VIEW_H = {320: 568, 375: 812, 414: 896, 768: 1024, 1024: 768, 1280: 800, 1440: 900, 1920: 1080}   # capture.mjs HEIGHTS
def view_h(ev, w):
    vp = (ev.manifest.get("viewports") or {}).get(str(w))
    return vp.get("height") if isinstance(vp, dict) and vp.get("height") else VIEW_H.get(w, 900)

def scroll_driven(ev):
    """manifest.prep.config.scrollFrames: the page was flagged as scroll-driven, so the full-page render is not what a visitor sees."""
    return bool(((ev.manifest.get("prep") or {}).get("config") or {}).get("scrollFrames"))

def incidental(ev, e, cfg, w=None):
    """Why a text run is incidental (WCAG 1.4.3 exemption: part of a picture of a UI), or None.
    Live round 1: on the controls every text_floor Floor and about half the contrast Floors were text inside product
    illustrations: aria-hidden graphics (L26 calendar figure 7 of 8, L27 Stripe payments-graphic 15 of 15), class-named
    mocks (L25 Linear WS84WW_frame, L27 platform-graphic cards) and CSS-scaled mocks (L25 at 375: 8px glyph boxes for
    12px type). These are demoted to Reflex, never dropped: aria-hidden marquees are still seen (slop L14), and slop
    L06's fake workspace preview keeps its Reflex signal."""
    chain = [e] + ev.ancestors(e, w)
    if any(a.get("ariaHidden") for a in chain[1:]): return "inside an aria-hidden graphic"
    tr, fs = e.get("textRects"), px(e["style"]["fontSize"])
    if tr and fs > 0 and max(t[3] for t in tr) < cfg.get("scaled_ratio", 0.85) * fs:
        return f"scaled text ({max(t[3] for t in tr)}px glyph box for {fs:.0f}px type, a transformed mock)"
    if cfg.get("mock_hint"):
        rx = re.compile(cfg["mock_hint"])
        for a in chain:
            if a.get("interactive") or a["tag"] in ("a", "button"): continue      # a "Book a demo" button is not a mock
            for tok in re.findall(r"[.#]([\w-]+)", a["sel"].split(" > ")[-1]):
                if rx.search(tok): return f"in a product illustration (.{tok})"
    return None

# ------------------------------------------------------------------ contrast on real pixels
@detector("contrast")
def contrast(ev, cfg):
    import numpy as np
    out = []; nv = collections.Counter()
    pinned = scroll_driven(ev)
    widths = [w for w in ev.widths if ev.has(f"bg-{w}.png")]
    if not widths: raise NotVerified("no background-only render (bg-<w>.png)")
    for w in widths:
        bg = ev.img(f"bg-{w}.png")
        H, W = bg.shape[:2]
        vh = view_h(ev, w)
        shot = ev.img(f"shot-{w}.png") if ev.has(f"shot-{w}.png") else None
        if shot is not None and shot.shape != bg.shape: shot = None
        dead = [x["rect"] for x in ev.dom(w)["elements"] if x.get("img") and x["vis"] and not x["img"].get("nw")]
        if (ev.manifest.get("network") or {}).get("blockedImages"):
            dead += [a["rect"] for a in ev.dom(w)["elements"] if a["vis"] and "url(" in a["style"]["backgroundImage"]]
        def over_dead(r): return any(d["x"] <= r["x"] + r["w"] / 2 <= d["x"] + d["w"] and d["y"] <= r["y"] + r["h"] / 2 <= d["y"] + d["h"] for d in dead)
        for e in ev.texts(w, min_len=2):
            if e.get("ariaHidden") or over_dead(e["rect"]): continue      # background image failed to load: not verifiable
            r_ = e["rect"]
            if (e["style"]["position"] == "fixed" or any(a["style"]["position"] == "fixed" for a in ev.ancestors(e, w))) and \
               (r_["y"] + r_["h"] / 2 > vh or r_["x"] + r_["w"] / 2 > w):
                continue      # off-screen child of a fixed layer: never painted where the full-page render puts it (live round 1: L30 "Imagery" at y 1050 in an 800px viewport)
            c = cl.parse(e["style"]["color"])
            if not c or c[3] == 0: continue
            alpha = c[3] * e.get("opacity", 1)
            boxes = e.get("textRects") or [[e["rect"]["x"], e["rect"]["y"], e["rect"]["w"], e["rect"]["h"]]]
            samples = []; glyphs = []
            for bx, by, bw, bh in boxes:
                x0, y0, x1, y1 = max(0, bx + 1), max(0, by + 2), min(W, bx + bw - 1), min(H, by + bh - 2)
                if x1 - x0 < 2 or y1 - y0 < 2: continue
                xs = np.linspace(x0, x1 - 1, max(2, min(24, (x1 - x0) // 6))).astype(int); ys = np.linspace(y0, y1 - 1, max(2, min(6, (y1 - y0) // 3))).astype(int)
                samples.extend(bg[np.ix_(ys, xs)].reshape(-1, 3) / 255.0)
                if shot is not None: glyphs.append((x0, y0, x1, y1))
            if len(samples) < 4: continue
            ratios = sorted(((cl.contrast(cl.over((c[0], c[1], c[2], alpha), tuple(s_) + (1,)), s_), s_) for s_ in samples), key=lambda t: t[0])
            p10 = ratios[max(0, int(len(ratios) * 0.10) - 1)]
            worst, ws = p10
            absmin = ratios[0][0]
            size, weight = px(e["style"]["fontSize"]), int(e["style"]["fontWeight"] or 400)
            large = size >= cfg["large_px"] or (size >= cfg["large_bold_px"] and weight >= 700)
            need = cfg["large"] if large else cfg["body"]
            if worst < need - 0.005:
                # scroll-driven page (prep.scrollFrames): below the first viewport the full-page render never fired the
                # scroll-triggered colour swaps (live round 1: L28 dark-on-dark sections that are light in the scroll frames)
                if pinned and r_["y"] >= vh: nv["below the first viewport on a scroll-driven page (see the scroll frames)"] += 1; continue
                if glyphs:      # narrow shot-vs-bg guard (floor-B RC5); rendered glyph contrast never clears a hit in general
                    diff = [np.abs(shot[y0:y1, x0:x1].astype(int) - bg[y0:y1, x0:x1].astype(int)).max(axis=2) > 24 for x0, y0, x1, y1 in glyphs]
                    if max(d.mean() for d in diff) < 0.01:
                        if worst >= 1.5: nv["no glyphs painted at the DOM rect"] += 1; continue      # live round 1: L34 sticky-menu rows, slop L01/L06 popovers
                        # near-invisible by CSS and nothing painted: real only if the render at the rect is the element's own ground
                        own = next((cl.parse(a["style"]["backgroundColor"]) for a in [e] + ev.ancestors(e, w) if (cl.parse(a["style"]["backgroundColor"]) or (0, 0, 0, 0))[3] >= 0.99), None)
                        if own and max(abs(own[i] - float(np.median([s_[i] for s_ in samples]))) for i in range(3)) > 0.16:
                            nv["the render at the DOM rect is not the element's own background (layout differs from the full-page render)"] += 1; continue   # L27 "Start now" at 375: purple button, white render
                    if worst < 1.5:      # CSS colour says near-invisible: check what was painted (blend, background-clip, overlay)
                        rr = []
                        for x0, y0, x1, y1 in glyphs:      # glyph cores: the 2% of pixels that differ most from the bg render
                            a_, b_ = shot[y0:y1, x0:x1].reshape(-1, 3).astype(int), bg[y0:y1, x0:x1].reshape(-1, 3).astype(int)
                            d_ = np.abs(a_ - b_).max(axis=1)
                            for k in np.argsort(d_)[-max(3, len(d_) // 50):]:
                                if d_[k] > 24: rr.append(cl.contrast(tuple(a_[k] / 255.0) + (1,), b_[k] / 255.0))
                        if rr and float(np.percentile(rr, 25)) >= need:      # L27 hero: CSS 1.18:1, painted about 6:1
                            nv["rendered colour differs from the CSS colour (blend, background-clip or overlay)"] += 1; continue
                lc = cl.apca(cl.over((c[0], c[1], c[2], alpha), tuple(ws) + (1,)), ws)
                why = incidental(ev, e, cfg, w)
                out.append(hit(cfg, where(e), f"{worst:.2f}:1 against the background behind the text (10th-percentile pixel {cl.hexstr(ws)}, worst {absmin:.2f}:1; text {cl.hexstr(c)}{', opacity %.2f' % alpha if alpha < 1 else ''}, {size:.0f}px; needs {need}:1). APCA Lc {abs(lc):.0f} (advisory)"
                               + (f"; {why}: incidental (WCAG 1.4.3 exemption)" if why else ""),
                               value=round(worst, 2), width=w, tier="Reflex" if why else "Floor", **({"priority": "P2"} if why else {})))
    # one finding per selector+evidence; Floors first so demoted mock text cannot push real failures past the cap
    seen, res = set(), []
    for h in sorted(out, key=lambda h: h["tier"] != "Floor"):
        k = (h["where"], h["value"])
        if k not in seen: seen.add(k); res.append(h)
    note = "; ".join(f"{n} failing text run(s) not verified: {k}" for k, n in nv.items())
    if not res and note: raise NotVerified(note)
    res = res[:15]
    if note: res[0]["not_verified"] = note
    return res

@detector("text_floor")
def text_floor(ev, cfg):
    out = []; labels = []; shrunk = []
    floor = cfg["body_px"]
    hard = cfg.get("hard_px", cfg["dense_ui_px"])
    for e in ev.texts(min_len=1):
        k = e.get("scale") or 1.0          # rendered / layout width: a transform: scale() on the text or an ancestor
        s = px(e["style"]["fontSize"]) * k   # set 2: P25 scale(0.5) and P43 ~0.62 drew 10-14px type at 5-7px
        scaled = f" (declared {px(e['style']['fontSize']):.0f}px, drawn at {k:.2f} scale)" if abs(k - 1) > 0.03 else ""
        # text a transform draws below the hard floor, whatever its length or tag: the label and table exemptions are for
        # deliberately small dense UI, not for a whole design shrunk (set 2 P25: a task table at scale(0.5), labels at 5-7px)
        if scaled and k < 1 and s < hard - 0.1 and e["textLen"] < cfg["min_run_chars"]: shrunk.append((e, s, k))
        if in_tag(ev, e, ("footer", "figcaption", "small", "caption", "sup", "sub", "code", "pre", "label", "th", "td", "nav", "button")): continue
        if e["textLen"] >= cfg["min_run_chars"] and s < floor - 0.1:
            tier, pr = ("Floor", "P0") if s < hard - 0.1 else (("Reflex", "P1") if s < cfg["dense_ui_px"] - 0.1 else ("Finish", "P3"))
            why = incidental(ev, e, cfg) if tier == "Floor" else None      # live round 1: all 8 control Floors were mock text (L25 frame, L27 graphics)
            if why: tier, pr = "Reflex", "P2"
            out.append(hit(cfg, where(e), f"{e['textLen']}-character run at {s:.0f}px{scaled} (hard floor {hard}px, dense UI {cfg['dense_ui_px']}px, body {floor}px)"
                           + (f"; {why}: incidental (WCAG 1.4.3 exemption)" if why else ""), value=round(s, 1), tier=tier, priority=pr, **({"check": "scaled"} if scaled else {})))
        elif e["textLen"] < cfg["min_run_chars"] and s < cfg["label_px"] - 0.1:
            labels.append(e)
    if len(shrunk) >= cfg.get("min_shrunk", 3):
        e0 = min(shrunk, key=lambda x: x[1])
        why = incidental(ev, e0[0], cfg)
        lo, hi = min(x[1] for x in shrunk), max(x[1] for x in shrunk)
        out.append(hit(cfg, where(e0[0]), f"{len(shrunk)} short text runs drawn at {lo:.0f}-{hi:.0f}px by a transform (scale {e0[2]:.2f}; declared {px(e0[0]['style']['fontSize']):.0f}px and up): the whole block is shrunk below the {hard}px floor"
                       + (f"; {why}: incidental (WCAG 1.4.3 exemption)" if why else ""), value=round(lo, 1), tier="Reflex" if why else "Floor", priority="P2" if why else "P0", check="scaled",
                       after="Show the block at its real size, crop it, or redraw it at the size it is shown; never scale text below the floor"))
    if len(labels) > cfg["max_label_runs"]:
        out += [hit(cfg, where(e), f"label at {px(e['style']['fontSize']) * (e.get('scale') or 1):.0f}px (label floor {cfg['label_px']}px; {len(labels)} such)", tier="Reflex") for e in labels[:5]]
    return sorted(out, key=lambda h: h["tier"] != "Floor")[:12]

@detector("focus_ring", needs=("focus.json",))
def focus_ring(ev, cfg):
    import numpy as np
    from PIL import Image
    stops = ev.json("focus.json")
    if not stops:
        if not any(e.get("interactive") for e in ev.visible()): raise Skip("page has no interactive controls")
        return [hit(cfg, "page", "Tab reached no focusable element although the page has controls", tier="Floor")]
    out = []; nv = 0
    for s in stops:
        if s.get("tag") == "iframe": continue        # focus moved into a frame: its own document is not captured here
        r = s.get("rect") or {}
        if r.get("x", 0) < 0 or r.get("y", 0) < 0: nv += 1; continue      # off the page box (live round 1: L30 tile scroller, x -2958): the clamped crop shows other content
        # cover: "full" (every in-view sample point owned by a painted fixed or sticky layer) fails WCAG 2.4.11 (AA): Floor.
        # "partial" is 2.4.12 (AAA): Reflex. Legacy boolean `covered` was box overlap only, with no stacking order,
        # visibility or pointer-events (live round 1: 23 of 23 control "covered" Floors were false: L23/L25 skip links
        # over headers, L27 NotificationsShell, L33 bg-list, L36 back-to-top), so it is Reflex until recaptured.
        cov = s["cover"] if "cover" in s else (s["covered"] if isinstance(s.get("covered"), str) else ("legacy" if s.get("covered") else None))
        if cov == "full":
            out.append(hit(cfg, f"{s['tag']} \"{s['text']}\"", "focused element is entirely hidden by a fixed or sticky element (WCAG 2.4.11)", tier="Floor"))
        elif cov:
            out.append(hit(cfg, f"{s['tag']} \"{s['text']}\"", "focused element is partly hidden by a fixed or sticky element (WCAG 2.4.12)" if cov == "partial"
                           else "focused element overlaps a fixed or sticky element (box overlap only; stacking order not checked)", tier="Reflex", priority="P2"))
        if not (s.get("on") and s.get("off")): continue
        a = np.asarray(Image.open(ev.dir / s["on"]).convert("RGB")).astype("int16")
        b = np.asarray(Image.open(ev.dir / s["off"]).convert("RGB")).astype("int16")
        if a.shape != b.shape: continue
        if a.mean(axis=2).std() < 2 and b.mean(axis=2).std() < 2: nv += 1; continue      # both crops flat: element never painted (L36 opacity-0 reveal)
        diff = np.abs(a - b).max(axis=2) > 40
        if diff.mean() < 0.004:
            ol = s.get("outline") or ""
            drawn = bool(re.match(r"(solid|dashed|dotted|double)\s", ol)) and not re.search(r"(^|\s)0px", ol)      # L35: 2px solid ring in the ground's own colour
            out.append(hit(cfg, f"{s['tag']} \"{s['text']}\"", f"no visible focus indicator ({'outline is set but nothing visible changes, so it is clipped or the colour of the ground: ' if drawn else 'outline: '}{ol})", tier="Floor",
                           after="Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground.")); continue
        on, off = a[diff] / 255.0, b[diff] / 255.0
        ratios = sorted(cl.contrast(tuple(x) + (1,), tuple(y) + (1,)) for x, y in zip(on[::max(1, len(on) // 400)], off[::max(1, len(off) // 400)]))
        best = ratios[int(len(ratios) * 0.9)] if ratios else 0
        if best < cfg["fail_below"]:
            out.append(hit(cfg, f"{s['tag']} \"{s['text']}\"", f"focus indicator visible but faint: {best:.2f}:1 against the unfocused state (target {cfg['min_contrast']}:1, WCAG 2.4.13)", value=round(best, 2), tier="Reflex", priority="P2"))
    if not out and nv and nv == sum(1 for s in stops if s.get("tag") != "iframe"): raise NotVerified(f"all {nv} focus stops are off the page or never painted")
    out = sorted(out, key=lambda h: h["tier"] != "Floor")[:10]
    if out and nv: out[0]["not_verified"] = f"{nv} focus stop(s) not verified (off the page box or never painted)"
    return out

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
                # dense footer link lists: Reflex, not Floor (owner decision 9 Nov 2026; most live-round-1 hits on the 14
                # human controls were footer links). Still reported; fix or waive with a reason.
                foot = e.get("inFooter") or any(a["tag"] == "footer" or a.get("role") == "contentinfo" for a in ev.ancestors(e, w))
                tier, note = (cfg.get("footer_tier", "Reflex"), " in the footer") if foot else ("Floor", "")
                out.append(hit(cfg, where(e), f"target {ww}x{hh}px at {w}px{note}, closer than {cfg['floor_px']}px to another target (WCAG 2.5.8)", tier=tier, width=w))
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
        if not e["vis"] and e["rect"]["w"] <= 1 and e["rect"]["h"] <= 1:
            continue      # unrendered tracking pixel (live round 1: L31 t.co and analytics.twitter.com 1x1 images, rect 0x0)
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
        # text fields belong to form_labels, which reports a missing label once (live round 1: L33 range picker and L34
        # search were reported twice, though Chromium names them from the placeholder); button-like inputs stay here
        if e.get("field") and e["field"].get("type") not in ("submit", "button", "reset", "image"): continue
        # hidden from AT and out of the tab order (L34's six <a aria-hidden="true" tabindex="-1"> heading anchors).
        # Captures without a tabindex field are treated as tabindex=-1 when aria-hidden.
        if e.get("ariaHidden") and (e.get("tabindex") if "tabindex" in e else "-1") == "-1": continue
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
    why = []      # one finding per viewport meta (live round 1: L33's single meta was reported twice)
    m = re.search(r"user-scalable=(no|0)", v)
    if m: why.append(m.group(0))
    m = re.search(r"maximum-scale=([\d.]+)", v)
    if m and float(m.group(1)) < 2: why.append(f"{m.group(0)} blocks zoom")
    return [hit(cfg, "meta viewport", f"zoom disabled ({'; '.join(why)}): {v}", tier="Floor")] if why else []

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
    sheets = ev.dom()["css"]
    css = "\n".join(sheets)
    # Only keyframes that move count, not spinners or opacity/visibility-only flipbooks (live round 1: L31 tpd-spin and
    # nprogress-spinner, L29 svelte visibility sequence were Floors). An unreadable non-font sheet may hold the
    # prefers-reduced-motion rule, so it makes the check not verified (L30 cross-origin Webflow sheet).
    spin = re.compile(cfg["spinner_names"], re.I)
    moves = re.compile(r"transform|translate|scale|rotate|\b(left|top|right|bottom|margin[\w-]*|offset-distance)\s*:", re.I)
    def keyframes(s):
        for m in re.finditer(r"@(?:-webkit-)?keyframes\s+([\w-]+)\s*\{", s):
            i, depth = m.end(), 1
            while depth and i < len(s): depth += {"{": 1, "}": -1}.get(s[i], 0); i += 1
            yield m.group(1), s[m.end():i]
    moving_kf = {name for name, body in keyframes(css) if moves.search(body) and not spin.search(name)}
    moving = moving_kf or re.search(r"transition[^;{}]*(transform|translate|scale|rotate|all)", css)
    if re.search(r"prefers-reduced-motion", css): return []
    fonts = re.compile(cfg["font_hosts"], re.I)
    unread = [c for c in sheets if c.startswith("/* unreadable") and not fonts.search(c)]
    if unread: raise NotVerified(f"{len(unread)} stylesheet(s) could not be read; a prefers-reduced-motion rule may be in them")
    if not moving: raise Skip("no movement in stylesheets (spinners and opacity/visibility-only keyframes excluded)")
    anim = [e for e in ev.visible() if any(n.strip() in moving_kf for n in e["style"]["animationName"].split(","))]
    w = where(anim[0]) if anim else "stylesheet"
    what = ("keyframes " + ", ".join(sorted(moving_kf)[:3])) if moving_kf else "transform transitions"
    return [hit(cfg, w, f"page moves ({what}) but has no prefers-reduced-motion rule", tier="Floor")]

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
