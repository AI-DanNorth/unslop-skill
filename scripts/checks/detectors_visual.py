"""Visual slop, colour, type and layout detectors."""
import re, math, collections
from core import detector, hit, px, where, Skip, NotVerified, lexicon, lexicon_patterns
import colorlib as cl

ALIASES = {"arial": "liberation sans", "helvetica": "liberation sans", "helvetica neue": "liberation sans", "times new roman": "liberation serif", "times": "liberation serif",
           "courier new": "liberation mono", "calibri": "carlito", "cambria": "caladea"}      # fontconfig metric-compatible substitutes on Linux renderers
GENERIC = {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui", "ui-sans-serif", "ui-serif", "ui-monospace", "-apple-system", "blinkmacsystemfont", "emoji", "math"}

def first_family(ff):
    return (ff or "").split(",")[0].strip().strip("'\"")

def rendered_family(ev, e):
    try: fonts = ev.json("fonts.json")
    except NotVerified: return first_family(e["style"]["fontFamily"])
    f = fonts.get(str(e["id"]))
    if not f: return first_family(e["style"]["fontFamily"])
    return max(f, key=lambda x: x["glyphs"])["family"]

def is_serif(ff): s = ff.lower(); return ("serif" in s and "sans-serif" not in s.split(",")[-1]) or any(k in s for k in ("charter", "garamond", "baskerville", "lora", "georgia", "times", "playfair", "fraunces", "newsreader", "caslon"))

def eff_bg(ev, e, w=None):
    """Composite ancestor backgrounds down to the element (flat colours only)."""
    d = ev.dom(w)
    chain = [e] + ev.ancestors(e, w)
    base = cl.parse(d.get("bodyBg")) or (1, 1, 1, 1)
    if base[3] < 0.5: base = cl.parse(d.get("htmlBg")) or (1, 1, 1, 1)
    if base[3] < 0.5: base = (1, 1, 1, 1)
    col = base[:3] + (1.0,)
    for a in reversed(chain):
        c = cl.parse(a["style"]["backgroundColor"])
        if c and c[3] > 0: col = cl.over(c, col)
    return col

def headings(ev, w=None):
    return [e for e in ev.visible(w) if e.get("level")]

# ------------------------------------------------------------------ slop tells
@detector("eyebrow")
def eyebrow(ev, cfg):
    texts = ev.texts()
    found = []
    for h in headings(ev):
        hs = px(h["style"]["fontSize"])
        if h["level"] > 4 or hs < cfg["min_heading_px"]: continue
        best = None
        for t in texts:
            if t is h or t.get("level") or t["textLen"] > 40: continue
            gap = h["rect"]["y"] - (t["rect"]["y"] + t["rect"]["h"])
            if gap < -2 or gap > cfg["max_gap_px"]: continue
            if t["rect"]["x"] + t["rect"]["w"] < h["rect"]["x"] or t["rect"]["x"] > h["rect"]["x"] + h["rect"]["w"]: continue
            if best is None or gap < best[0]: best = (gap, t)
        if not best: continue
        t = best[1]; ts = px(t["style"]["fontSize"]); ls = px(t["style"]["letterSpacing"]) if t["style"]["letterSpacing"] != "normal" else 0
        tracked = ts and ls / ts >= cfg["min_tracking_em"]
        caps = t["style"]["textTransform"] == "uppercase" or (t["text"].isupper() and len(t["text"]) > 2)
        if ts <= cfg["max_size_px"] and ts <= hs * cfg["max_ratio_to_heading"] and (tracked or caps):
            found.append((t, h, ts, ls))
    if len(found) <= cfg.get("budget", 0): return []
    return [hit(cfg, where(t), f"{ts:.0f}px label{' tracked %.2fem' % (ls/ts) if ls else ''}{' caps' if t['style']['textTransform']=='uppercase' else ''} above {px(h['style']['fontSize']):.0f}px heading \"{h['text'][:40]}\"; {len(found)} on page, budget {cfg.get('budget',0)}",
                value=len(found), after="Promote the fact into the heading or delete the label (T-EYEBROW).") for t, h, ts, ls in found]

@detector("numbered_labels")
def numbered_labels(ev, cfg):
    hs = headings(ev)
    found = []
    for t in ev.texts():
        if not re.fullmatch(r"(No\.?\s*)?0?\d{1,2}[.)/:]?|\d{2,3}\s*[/·]\s*\d{1,3}", t["text"]): continue
        if px(t["style"]["fontSize"]) > cfg["max_size_px"]: continue
        for h in hs:
            near = abs(h["rect"]["y"] - t["rect"]["y"]) < 80 and abs(h["rect"]["x"] - t["rect"]["x"]) < 400
            inside = t.get("parent") is not None and int(t["parent"]) == h["id"]
            if (near or inside) and px(h["style"]["fontSize"]) >= cfg["min_heading_ratio"] * px(t["style"]["fontSize"]):
                found.append((t, h)); break
    if len(found) < cfg["min_count"] or len(found) <= cfg.get("budget", 0): return []
    return [hit(cfg, where(t), f"section number \"{t['text']}\" ({px(t['style']['fontSize']):.0f}px) beside heading \"{h['text'][:40]}\"; {len(found)} on page", value=len(found)) for t, h in found]

@detector("icon_tile")
def icon_tile(ev, cfg):
    hs = headings(ev); tiles = []
    for e in ev.visible():
        r = e["rect"]
        if e["textLen"] or not (cfg["min_px"] <= r["w"] <= cfg["max_px"]) or abs(r["w"] - r["h"]) > 4: continue
        bg = cl.parse(e["style"]["backgroundColor"]); bw = px(e["style"]["borderTopWidth"])
        if not ((bg and bg[3] >= cfg["min_tint_alpha"]) or bw > 0): continue
        for h in hs:
            gap = h["rect"]["y"] - (r["y"] + r["h"])
            if 0 <= gap <= 48 and abs(h["rect"]["x"] - r["x"]) < 24: tiles.append((e, h)); break
    if len(tiles) < cfg["min_repeats"]: return []
    return [hit(cfg, where(e), f"{e['rect']['w']}px tinted tile above heading \"{h['text'][:40]}\" ({len(tiles)} repeats)", value=len(tiles)) for e, h in tiles]

@detector("side_tab_border")
def side_tab(ev, cfg):
    out = []
    for e in ev.visible():
        s = e["style"]; w = [px(s[k]) for k in ("borderTopWidth", "borderRightWidth", "borderBottomWidth", "borderLeftWidth")]
        thick = [i for i, v in enumerate(w) if v >= cfg["min_side_px"]]
        if len(thick) == 1 and all(v <= cfg["max_other_px"] for i, v in enumerate(w) if i != thick[0]) and px(s["borderTopLeftRadius"]) >= cfg["min_radius_px"]:
            side = ["top", "right", "bottom", "left"][thick[0]]
            out.append(hit(cfg, where(e), f"{w[thick[0]]:.0f}px {side} border, others ≤{cfg['max_other_px']}px, radius {s['borderTopLeftRadius']}"))
    return out[:6]

def recipe(e):
    s = e["style"]
    return (s["borderTopLeftRadius"], s["boxShadow"], s["borderTopWidth"], s["borderTopColor"] if px(s["borderTopWidth"]) else "", s["backgroundColor"])

@detector("card_kit")
def card_kit(ev, cfg):
    groups = collections.defaultdict(list)
    for e in ev.visible():
        s = e["style"]
        if s["boxShadow"] != "none" and px(s["borderTopLeftRadius"]) > 0 and e["rect"]["w"] > 80:
            groups[(s["borderTopLeftRadius"], s["boxShadow"])].append(e)
    out = []
    for (rad, sh), lst in groups.items():
        if len(lst) >= cfg["min_same_recipe"]:
            out.append(hit(cfg, where(lst[0]), f"{len(lst)} containers share radius {rad} and shadow \"{sh[:60]}\"", value=len(lst), root=f"radius {rad} + shadow"))
    return out

@detector("container_monotony")
def container_monotony(ev, cfg):
    groups = collections.defaultdict(list)
    for e in ev.visible():
        s = e["style"]
        boxed = s["boxShadow"] != "none" or px(s["borderTopWidth"]) > 0 or (cl.parse(s["backgroundColor"]) or (0, 0, 0, 0))[3] > 0
        if boxed and px(s["paddingTop"]) > 0 and e["rect"]["w"] > 60: groups[recipe(e) + (s["paddingTop"],)].append(e)
    out = []
    for k, lst in groups.items():
        classes = {re.sub(r":nth-of-type\(\d+\)", "", l["sel"].split(" > ")[-1]) for l in lst}
        if len(lst) >= cfg["min_selectors"] and len(classes) >= 3:
            out.append(hit(cfg, where(lst[0]), f"one box recipe on {len(lst)} elements across {len(classes)} selectors ({', '.join(sorted(classes)[:4])})", value=len(lst)))
    return out

def _in(h, rng):
    lo, hi = rng
    return lo <= h <= hi if lo <= hi else (h >= lo or h <= hi)

@detector("gradient")
def gradient(ev, cfg):
    out = []
    for e in ev.visible():
        bi = e["style"]["backgroundImage"]
        if "gradient(" not in bi: continue
        stops = cl.colors_in(bi)
        hues = [cl.oklch(c)[2] for c in stops if cl.oklch(c)[1] > 0.04 and c[3] > 0.2]
        reasons = []
        if len(stops) > cfg["max_stops"]: reasons.append(f"{len(stops)} stops")
        if len(hues) >= 2:
            span = max(min(abs(a - b), 360 - abs(a - b)) for a in hues for b in hues)
            if span > cfg["max_hue_span_deg"]: reasons.append(f"hue span {span:.0f}°")
            for p in cfg["banned_pairs"]:
                A, B = p[:2], p[2:]
                if any(_in(a, A) for a in hues) and any(_in(b, B) for b in hues): reasons.append(f"banned pair (hues {A[0]}-{A[1]} with {B[0]}-{B[1]})"); break
        if reasons:
            out.append(hit(cfg, where(e), f"gradient {' + '.join(reasons)}: {', '.join(cl.hexstr(c) for c in stops[:5])}", banned_pair=any("banned" in r for r in reasons)))
    return out

def shadows(v):
    if not v or v == "none": return []
    parts = re.split(r",(?![^(]*\))", v)
    out = []
    for p in parts:
        c = cl.colors_in(p); nums = [float(x) for x in re.findall(r"(-?\d*\.?\d+)px", p)]
        if c and len(nums) >= 3: out.append((c[0], nums))
    return out

@detector("glow")
def glow(ev, cfg):
    out = []
    for e in ev.visible():
        for prop in ("boxShadow", "textShadow"):
            for c, n in shadows(e["style"][prop]):
                ox, oy, blur = n[0], n[1], n[2]
                if abs(ox) < 1 and abs(oy) < 1 and blur * c[3] >= cfg["min_blur_x_alpha_px"] and cl.oklch(c)[1] > 0.05:
                    out.append(hit(cfg, where(e), f"zero-offset coloured {prop} {cl.hexstr(c)} blur {blur:.0f}px alpha {c[3]:.2f}"))
        bi = e["style"]["backgroundImage"]
        if "radial-gradient" in bi:
            for c in cl.colors_in(bi):
                if c[3] >= cfg["spotlight_min_alpha"] and cl.oklch(c)[1] > 0.05 and c[3] < 0.9:
                    out.append(hit(cfg, where(e), f"radial spotlight {cl.hexstr(c)} alpha {c[3]:.2f}")); break
    return out[:6]

@detector("neon_violet")
def neon_violet(ev, cfg):
    out = []
    for e in ev.texts():
        if px(e["style"]["fontSize"]) < cfg["min_px"] and not e.get("level"): continue
        c = cl.parse(e["style"]["color"])
        if not c: continue
        L, C, H = cl.oklch(c)
        if C >= cfg["violet_min_chroma"] and _in(H, cfg["violet_hue"]):
            out.append(hit(cfg, where(e), f"violet text {cl.hexstr(c)} (oklch hue {H:.0f}, chroma {C:.2f}) at {e['style']['fontSize']}"))
        elif C >= cfg["cyan_min_chroma"] and _in(H, cfg["cyan_hue"]) and cl.oklch(eff_bg(ev, e))[0] < cfg["dark_bg_max_l"]:
            out.append(hit(cfg, where(e), f"neon cyan {cl.hexstr(c)} on dark ground"))
    return out

def oklab_img(a):
    import numpy as np
    x = a.astype("float32") / 255
    x = np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)
    M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]], "float32")
    M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468], [1.9779984951, -2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, -0.8086757660]], "float32")
    lms = np.cbrt(x @ M1.T)
    return lms @ M2.T

@detector("accent_footprint")
def accent_footprint(ev, cfg):
    import numpy as np
    w = cfg["fold"][0]
    name = f"fold-{w}.png" if ev.has(f"fold-{w}.png") else f"fold-{ev.primary}.png"
    img = ev.img(name)
    lab = oklab_img(img)
    chroma = np.hypot(lab[..., 1], lab[..., 2])
    mask = chroma > 0.10
    dom = ev.dom(int(name.split("-")[1].split(".")[0]))
    for e in dom["elements"]:          # exclude photographs and video
        if e["tag"] in ("img", "video", "picture", "canvas", "iframe") and e["vis"]:
            r = e["rect"]; mask[max(0, r["y"]):r["y"] + r["h"], max(0, r["x"]):r["x"] + r["w"]] = False
    share = 100 * mask.mean()
    if share > cfg["fail_pct"]: return [hit(cfg, f"first screen at {name[5:-4]}px", f"saturated accent covers {share:.1f}% of the fold (fail > {cfg['fail_pct']}%)", value=round(share, 1), priority="P1")]
    if share > cfg["warn_pct"]: return [hit(cfg, f"first screen at {name[5:-4]}px", f"saturated accent covers {share:.1f}% of the fold (warn > {cfg['warn_pct']}%)", value=round(share, 1), priority="P2")]
    return []

@detector("stock_swatches")
def stock_swatches(ev, cfg):
    lx = lexicon("swatches")
    bad = {e["term"].lower(): g["name"] for g in lx["groups"] if g.get("policy") == "fail" for e in g["entries"]}
    out = []
    for name, val in ev.dom()["tokens"].items():
        c = cl.parse(val)
        if c and cl.hexstr(c) in bad:
            out.append(hit(cfg, f":root {name}", f"token {name}: {val} is a stock {bad[cl.hexstr(c)]} swatch", value=cl.hexstr(c)))
    return out

# ------------------------------------------------------------------ type
@detector("flat_hierarchy")
def flat_hierarchy(ev, cfg):
    sizes = collections.defaultdict(list)
    for e in ev.texts():
        role = f"h{e['level']}" if e.get("level") else ("body" if e["tag"] == "p" and e["textLen"] > 40 else None)
        if role: sizes[role].append(px(e["style"]["fontSize"]))
    med = {r: sorted(v)[len(v) // 2] for r, v in sizes.items()}
    order = [r for r in ("h1", "h2", "h3", "h4", "body") if r in med]
    if len(order) < cfg["min_roles"]: raise Skip(f"only {len(order)} type roles")
    out = []
    for a, b in zip(order, order[1:]):
        if med[b] > 0 and med[a] / med[b] < cfg["min_ratio"] and med[a] >= med[b]:
            out.append(hit(cfg, f"{a} vs {b}", f"{a} {med[a]:.0f}px is only {med[a]/med[b]:.2f}x {b} {med[b]:.0f}px (min {cfg['min_ratio']}x)", value=round(med[a] / med[b], 2)))
    return out

@detector("type_ladder")
def type_ladder(ev, cfg):
    sizes = sorted({round(px(e["style"]["fontSize"]) * 2) / 2 for e in ev.texts()})
    fams = collections.Counter(rendered_family(ev, e) for e in ev.texts(min_len=3))
    fams = [f for f, n in fams.items() if n >= 1]
    out = []
    if len(sizes) > cfg["max_distinct_sizes"]:
        out.append(hit(cfg, "whole page", f"{len(sizes)} distinct font sizes: {', '.join('%g' % s for s in sizes)} (max {cfg['max_distinct_sizes']})", value=len(sizes)))
    if len(fams) >= cfg["fail_families"]:
        out.append(hit(cfg, "whole page", f"{len(fams)} font families render: {', '.join(fams)}", value=len(fams), priority="P1"))
    elif len(fams) >= cfg["warn_families"]:
        out.append(hit(cfg, "whole page", f"{len(fams)} font families render: {', '.join(fams)}", value=len(fams), priority="P2"))
    return out

@detector("banned_fonts")
def banned_fonts(ev, cfg):
    lx = lexicon("fonts")
    banned = {e["term"].lower() for g in lx["groups"] if g["name"] == "banned-as-display" for e in g["entries"]}
    out, seen = [], set()
    for e in ev.texts():
        if not (px(e["style"]["fontSize"]) >= cfg["display_min_px"] or e.get("level") in (1, 2)): continue
        fam = rendered_family(ev, e)
        if fam.lower() in banned and fam not in seen:
            seen.add(fam)
            subs = lx.get("substitutes", {}).get(f"{fam} (display)") or lx.get("substitutes", {}).get(fam)
            out.append(hit(cfg, where(e), f"display text at {e['style']['fontSize']} set in {fam}, a UI text face", after=f"Try {', '.join(subs)}" if subs else None))
    return out

@detector("fallback_face", needs=("fonts.json",))
def fallback_face(ev, cfg):
    fonts = ev.json("fonts.json")
    bad = {b.lower() for b in cfg["bad_faces"]}
    out, seen = [], set()
    for e in ev.texts(min_len=2):
        f = fonts.get(str(e["id"]))
        if not f: continue
        drawn = max(f, key=lambda x: x["glyphs"])["family"]
        declared = first_family(e["style"]["fontFamily"])
        if declared.lower() in GENERIC or drawn.lower().startswith(declared.lower()) or declared.lower().startswith(drawn.lower()): continue
        if ALIASES.get(declared.lower()) == drawn.lower(): continue
        key = (declared, drawn)
        if key in seen: continue
        seen.add(key)
        note = " (a known fallback face)" if drawn.lower() in bad else ""
        out.append(hit(cfg, where(e), f"declared \"{declared}\" but {drawn} drew the text{note}", value=drawn,
                       after="Fix the font load (path, format, font-display) or declare the face you actually ship."))
    return out

# ------------------------------------------------------------------ layout
def spacing_values(ev):
    vals = []
    for e in ev.visible():
        s = e["style"]
        for k in ("marginTop", "marginBottom", "paddingTop", "paddingBottom", "paddingLeft", "paddingRight", "rowGap", "columnGap"):
            v = px(s.get(k, "0"))
            if v > 0.5: vals.append((v, e))
    return vals

@detector("spacing_monotony")
def spacing_monotony(ev, cfg):
    vals = spacing_values(ev)
    if len(vals) < cfg["min_values"]: raise Skip(f"only {len(vals)} spacing values")
    c = collections.Counter(round(v / 4) * 4 for v, _ in vals)
    top, n = c.most_common(1)[0]
    out = []
    if n / len(vals) > cfg["max_share_one_value"]:
        out.append(hit(cfg, "whole page", f"{top}px is {100*n/len(vals):.0f}% of {len(vals)} spacing values (max {100*cfg['max_share_one_value']:.0f}%)", value=round(n / len(vals), 2)))
    if len(c) < cfg["min_distinct"]:
        out.append(hit(cfg, "whole page", f"only {len(c)} distinct spacing values ({', '.join(str(k) for k in sorted(c))})", value=len(c)))
    return out

@detector("off_scale_spacing")
def off_scale(ev, cfg):
    off = collections.Counter()
    ex = {}
    for v, e in spacing_values(ev):
        if abs(v - round(v)) < 0.05 and round(v) % cfg["base_px"] != 0 and round(v) not in (1, 2, 6, 10, 14):   # hairline and half-steps tolerated
            off[round(v)] += 1; ex.setdefault(round(v), e)
    if len(off) <= cfg["max_off_scale"]: return []
    return [hit(cfg, "whole page", f"{len(off)} off-scale spacing values: {', '.join(f'{k}px' for k in sorted(off))} (e.g. {ex[sorted(off)[0]]['sel']})", value=len(off))]

@detector("heading_rhythm")
def heading_rhythm(ev, cfg):
    d = ev.dom(); vis = [e for e in d["elements"] if e["vis"]]
    sib = collections.defaultdict(list)
    for e in vis: sib[e.get("parent")].append(e)
    bad = []
    for par, kids in sib.items():
        kids.sort(key=lambda e: e["rect"]["y"])
        for i, h in enumerate(kids):
            if not h.get("level") or i == 0 or i == len(kids) - 1: continue
            prev, nxt = kids[i - 1], kids[i + 1]
            above = h["rect"]["y"] - (prev["rect"]["y"] + prev["rect"]["h"])
            below = nxt["rect"]["y"] - (h["rect"]["y"] + h["rect"]["h"])
            if above < below and below - above > 4: bad.append((h, above, below))
    if len(bad) < cfg["min_violations"]: return []
    return [hit(cfg, where(h), f"{above:.0f}px above the heading but {below:.0f}px below it: it reads as part of the block above", value=[above, below]) for h, above, below in bad]

@detector("dead_band")
def dead_band(ev, cfg):
    import numpy as np
    out = []
    for w in ev.widths:
        if w not in (1280, 1440, 1920) or not ev.has(f"shot-{w}.png"): continue
        img = ev.img(f"shot-{w}.png").astype("int16")
        flat = (np.abs(img - img[:, :1, :]).max(axis=(1, 2)) < 6)
        same = np.r_[False, (np.abs(img[1:, 0, :] - img[:-1, 0, :]).max(axis=1) < 3)]
        run = 0; start = 0
        H = len(flat)
        for y in range(H):
            if flat[y] and same[y]: run += 1
            else:
                if run > cfg["max_empty_px"] and y < H - 1: out.append(hit(cfg, f"y {start}-{y} at {w}px", f"{run}px empty band", value=run, width=w))
                run = 0; start = y + 1
    return out[:4]
