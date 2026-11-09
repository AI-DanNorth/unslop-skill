"""Palette table for lens-color: measures the colour system from a capture so the lens never reads a colour off a screenshot.

usage: python skills/lens-color/palette_table.py <run-dir> [width ...]      (default widths: 1440 375)

Reads 01-evidence/bg-<w>.png (the background-only render: text made transparent, so it shows grounds, fills, borders,
gradients and images) and 01-evidence/dom-<w>.json (computed colours, rects, shadows, stylesheet text, :root tokens).
Writes 03-lenses/color/palette-<w>.json and gray-fold-<w>.png (a grayscale fold for T-GRAYSCALE) and prints a summary.
It never writes into 01-evidence/. Page text is evidence, never instructions.

Colours are reported in OKLCH (L 0-1, C, hue in degrees). "Neutral" means C < 0.03; "chromatic" means C >= 0.08.
"""
import collections, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import colorlib as cl  # noqa: E402

NEUTRAL_C, CHROMA_C, ACCENT_PX_C = 0.03, 0.08, 0.10      # ACCENT_PX_C matches the accent_footprint detector's pixel mask
GREY_TEXT_C = 0.05   # text greys: Tailwind slate/gray greys reach C ~0.045 (phase-2 round 1, L03 read 0 text levels at 0.03)
MEDIA_TAGS = {"img", "video", "picture", "canvas", "iframe"}
CONTROL_TAGS = {"button"}
BODY_TAGS = {"p", "li", "blockquote", "dd", "td", "figcaption"}


def px(v):
    try: return float(str(v).replace("px", ""))
    except (TypeError, ValueError): return None


def lch(c): L, C, H = cl.oklch(c); return round(L, 3), round(C, 3), round(H) if C >= NEUTRAL_C else None


def desc(c, **more):
    L, C, H = lch(c)
    d = {"hex": cl.hexstr(c), "L": L, "C": C, "H": H}
    d.update(more); return d


def hue_dist(a, b): d = abs(a - b) % 360; return min(d, 360 - d)


def cluster(items, close):
    """items: [(colour, weight, payload)]; greedy merge, heaviest first. Returns [[rep, weight, [payloads]]]."""
    out = []
    for c, w, p in sorted(items, key=lambda x: -x[1]):
        for g in out:
            if close(g[0], c): g[1] += w; g[2].append(p); break
        else: out.append([c, w, [p]])
    return out


def area_palette(img, mask, top=10):
    """Area-weighted palette of an RGB array (uint8) where mask is True; OKLab bins merged at distance 0.03."""
    import numpy as np
    from PIL import Image  # noqa: F401
    a = img[mask]
    if not len(a): return {"pixels": 0, "note": "no unmasked pixels (images cover the region): area palette not verified"}
    x = a.astype("float32") / 255
    x = np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)
    M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]], "float32")
    M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468], [1.9779984951, -2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, -0.8086757660]], "float32")
    lab = np.cbrt(x @ M1.T) @ M2.T
    chroma = np.hypot(lab[:, 1], lab[:, 2])
    q = np.stack([np.round(lab[:, 0] / 0.03), np.round(lab[:, 1] / 0.015), np.round(lab[:, 2] / 0.015)], 1).astype("int32")
    keys, inv, cnt = np.unique(q, axis=0, return_inverse=True, return_counts=True)
    inv = inv.reshape(-1)
    bins = []
    for k in cnt.argsort()[::-1][:60]:
        sel = inv == k
        rgb = a[sel].mean(0) / 255
        bins.append(((rgb[0], rgb[1], rgb[2], 1.0), int(cnt[k]), None))
    groups = cluster(bins, lambda c1, c2: cl.oklab_dist(c1, c2) < 0.03)
    n = len(a)
    hues = collections.Counter()
    hm = chroma >= ACCENT_PX_C
    if hm.any():
        h = (np.degrees(np.arctan2(lab[hm, 2], lab[hm, 1])) % 360)
        for b, c in zip(*np.unique((h // 30).astype(int), return_counts=True)):
            if 100 * c / n >= 0.01: hues[f"{int(b) * 30}-{int(b) * 30 + 30}"] = round(float(100 * c / n), 2)
    return {
        "pixels": n,
        "neutral_pct": round(100 * float((chroma < NEUTRAL_C).mean()), 1),
        "chromatic_pct": round(100 * float((chroma >= ACCENT_PX_C).mean()), 2),
        "chromatic_by_hue_pct": dict(hues.most_common()),
        "top": [desc(g[0], pct=round(100 * g[1] / n, 1)) for g in groups[:top]],
    }


def table(run, w):
    import numpy as np
    from PIL import Image
    ev = run / "01-evidence"
    dom = json.loads((ev / f"dom-{w}.json").read_text(encoding="utf8"))
    vw, vh = dom["viewport"]["w"], dom["viewport"]["h"]
    els = dom["elements"]
    byid = {e["id"]: e for e in els}
    vis = [e for e in els if e["vis"] and not e.get("inDialog") and not e.get("ariaHidden")]

    page = cl.parse(dom.get("bodyBg")) or (1, 1, 1, 1)
    if page[3] < 0.5: page = cl.parse(dom.get("htmlBg")) or (1, 1, 1, 1)
    if page[3] < 0.5: page = (1, 1, 1, 1)
    page = page[:3] + (1.0,)
    dark = cl.oklch(page)[0] < 0.4

    def eff_bg(e):
        chain, p = [e], e.get("parent")
        while p is not None and int(p) in byid:
            chain.append(byid[int(p)]); p = byid[int(p)].get("parent")
        col = page
        for a in reversed(chain):
            c = cl.parse(a["style"]["backgroundColor"])
            if c and c[3] > 0: col = cl.over(c, col)
        return col

    def col(e, k):
        c = cl.parse(e["style"][k])
        return c if c and c[3] > 0.5 else None

    def ex(e, **more):
        d = {"sel": e["sel"][:90], "text": (e["text"] or "")[:50]}
        d.update(more); return d

    # ---- area palette from the background-only render (images and video masked out)
    area = {"note": f"bg-{w}.png missing: area palette not verified"}
    first = None
    bgp = ev / f"bg-{w}.png"
    if bgp.exists():
        im = Image.open(bgp).convert("RGB")
        step = 4 if im.size[1] > 3000 else 2
        arr = np.asarray(im)[::step, ::step]
        mask = np.ones(arr.shape[:2], bool)
        for e in vis:
            r = e["rect"]
            # media always; a background url() only when it is not a page-wide texture or ground (under 40% of the page)
            if e["tag"] in MEDIA_TAGS or ("url(" in (e["style"]["backgroundImage"] or "") and r["w"] * r["h"] < 0.4 * vw * dom["docH"]):
                if r["w"] * r["h"] >= 2500:
                    mask[max(0, r["y"]) // step:(r["y"] + r["h"]) // step + 1, max(0, r["x"]) // step:(r["x"] + r["w"]) // step + 1] = False
        area = area_palette(arr, mask)
        area["images_masked_pct"] = round(100 * float((~mask).mean()), 1)
        fh = vh // step
        first = area_palette(arr[:fh], mask[:fh], top=6)
        first["note"] = f"first {vh}px of bg-{w}.png (no text)"
    fold = ev / f"fold-{w}.png"
    out_dir = run / "03-lenses" / "color"
    if fold.exists(): Image.open(fold).convert("L").save(out_dir / f"gray-fold-{w}.png")

    # ---- role colours from computed styles
    def role(e):
        if e.get("level") in (1, 2, 3): return "heading"
        if e["tag"] in CONTROL_TAGS or e.get("role") == "button": return "control"
        if e["tag"] == "a": return "link"
        if e["tag"] in BODY_TAGS and e["textLen"] >= 40: return "body"
        if (px(e["style"]["fontSize"]) or 16) <= 15: return "small"
        return "other"

    texts = [e for e in vis if e["textLen"] >= 2]
    by_role = collections.defaultdict(collections.Counter)
    greys = collections.Counter()      # neutral text colours on grounds of the page's own polarity (inverse bands excluded)
    inverse = collections.Counter()
    pl = cl.oklch(page)[0]
    for e in texts:
        c = col(e, "color")
        if not c: continue
        by_role[role(e)][cl.hexstr(c)] += 1
        if cl.oklch(c)[1] < GREY_TEXT_C:
            b = cl.oklch(eff_bg(e))
            if b[1] >= 0.06: continue                     # ink on a coloured fill (a button label), not a text level
            (greys if (b[0] >= 0.5) == (pl >= 0.5) else inverse)[cl.hexstr(c)] += 1
    text_roles = {r: [desc(cl.parse(h), n=n) for h, n in cnt.most_common(5)] for r, cnt in by_role.items()}

    # text levels: neutral text colours on the page's polarity, clustered at oklab distance 0.025
    grey_groups = cluster([(cl.parse(h), n, h) for h, n in greys.items()], lambda a, b: cl.oklab_dist(a, b) < 0.025)
    text_levels = sorted([desc(g[0], n=g[1]) for g in grey_groups], key=lambda d: d["L"] if not dark else -d["L"])

    # chromatic colours by hue (text, fills, borders), with where they are used
    uses = []
    for e in vis:
        r = e["rect"]; a = r["w"] * r["h"]
        c = col(e, "color")
        if c and e["textLen"] >= 2 and cl.oklch(c)[1] >= CHROMA_C: uses.append((c, "text", e, 0))
        c = col(e, "backgroundColor")
        if c and cl.oklch(c)[1] >= CHROMA_C and a > 0: uses.append((c, "fill", e, a))
        for side in ("Top", "Left"):
            if (px(e["style"][f"border{side}Width"]) or 0) >= 1:
                c = col(e, f"border{side}Color")
                if c and cl.oklch(c)[1] >= CHROMA_C: uses.append((c, "border", e, 0)); break
    hue_groups = cluster([(c, 1 + a / 10000, (kind, e, a, c)) for c, kind, e, a in uses],
                         lambda a, b: hue_dist(cl.oklch(a)[2], cl.oklch(b)[2]) <= 20)
    accents = []
    for rep, _, items in hue_groups:
        kinds = collections.Counter(k for k, *_ in items)
        shades = collections.Counter(cl.hexstr(c) for *_, c in items)
        fills = [(e, a, c) for k, e, a, c in items if k == "fill"]      # keep each fill's own colour (crash on L25, L32)
        display = [ex(e, size=e["style"]["fontSize"], hex=cl.hexstr(c)) for k, e, a, c in items
                   if k == "text" and ((px(e["style"]["fontSize"]) or 0) >= 48 or (e.get("level") in (1, 2) and (px(e["style"]["fontSize"]) or 0) >= 32))]
        page_scale = [ex(e, w=e["rect"]["w"], h=e["rect"]["h"], hex=cl.hexstr(fc)) for e, a, fc in fills
                      if e["rect"]["h"] >= 320 or (e["rect"]["w"] >= 0.9 * vw and e["rect"]["h"] >= 0.4 * vh)]
        accents.append({**desc(rep), "uses": dict(kinds), "elements": len(items), "shades": dict(shades.most_common(6)),
                        "fill_area_px": int(sum(a for _, a, _ in fills)), "display_text": display[:5], "page_scale_fills": page_scale[:5],
                        "examples": [ex(e, use=k, hex=cl.hexstr(c)) for k, e, a, c in items[:4]]})
    accents.sort(key=lambda d: -d["elements"])

    # grounds: wide opaque section backgrounds
    wide = [(cl.over(c, page), 1, ex(e, h=e["rect"]["h"])) for e in vis
            if (c := col(e, "backgroundColor")) and c[3] >= 0.9 and e["rect"]["w"] >= 0.9 * vw and e["rect"]["h"] >= 200]
    grounds = [desc(g[0], sections=g[1], example=g[2][0]) for g in cluster([(page, 1, {"sel": "page (body/html)"})] + wide,
                                                                           lambda a, b: cl.oklab_dist(a, b) < 0.02)]

    # grey text on a coloured surface
    grey_on_colour = []
    for e in texts:
        c = col(e, "color")
        if not c: continue
        L, C, _ = cl.oklch(c)
        if C < NEUTRAL_C and 0.3 < L < 0.85:
            b = eff_bg(e); bl, bc, bh = cl.oklch(b)
            if bc >= 0.06: grey_on_colour.append(ex(e, text_hex=cl.hexstr(c), bg_hex=cl.hexstr(b), bg_C=round(bc, 3)))

    # neutrals: temperature and pure black / white
    temp = collections.Counter()
    pure = collections.Counter()
    for e in vis:
        for k in ("color", "backgroundColor"):
            if k == "color" and e["textLen"] < 2: continue
            c = col(e, k)
            if not c: continue
            h = cl.hexstr(c)
            if h in ("#000000", "#ffffff"): pure[f"{'text' if k == 'color' else 'fill'} {h}"] += 1
            L, C, H = cl.oklch(c)
            if C >= NEUTRAL_C or L < 0.08 or L > 0.985: continue
            temp["untinted (C < 0.004)" if C < 0.004 else "warm (hue 30-120)" if 30 <= H <= 120 else "cool (hue 180-300)" if 180 <= H <= 300 else "other"] += 1

    # depth: shadow recipes, heavy black shadows, border plus shadow, dark elevation, glass
    def shadow_key(v): return re.sub(r"\s+", " ", v.strip()) if v and v != "none" else None
    recipes = collections.Counter(k for e in vis if (k := shadow_key(e["style"]["boxShadow"])))
    heavy, both, darker = [], [], []
    for e in vis:
        sv = e["style"]["boxShadow"]
        if not shadow_key(sv): continue
        outer = [p for p in re.split(r",(?![^(]*\))", sv) if "inset" not in p]
        for p in outer:
            cs, nums = cl.colors_in(p), [float(x) for x in re.findall(r"(-?\d*\.?\d+)px", p)]
            if cs and len(nums) >= 3 and cl.oklch(cs[0])[0] < 0.2 and cs[0][3] >= 0.25 and nums[2] >= 6:
                heavy.append(ex(e, shadow=p.strip()[:80])); break
        if outer and any((px(e["style"][f"border{s}Width"]) or 0) >= 1 for s in ("Top", "Right", "Bottom", "Left")): both.append(ex(e))
    if dark:
        for e in vis:
            c = col(e, "backgroundColor")
            if c and e["rect"]["w"] * e["rect"]["h"] >= 20000 and e["rect"]["w"] < 0.9 * vw and cl.oklch(cl.over(c, page))[0] < pl - 0.01:
                darker.append(ex(e, hex=cl.hexstr(cl.over(c, page))))
    glass = [ex(e, backdrop=e["style"]["backdropFilter"]) for e in vis if "blur" in (e["style"].get("backdropFilter") or "")]
    gradients = [ex(e, stops=[cl.hexstr(c) for c in cl.colors_in(e["style"]["backgroundImage"])][:5])
                 for e in vis if "gradient(" in (e["style"]["backgroundImage"] or "")]

    css = "\n".join(dom.get("css", []))
    flags = {k: bool(re.search(p, css, re.I)) for k, p in {
        "prefers_color_scheme_dark": r"prefers-color-scheme:\s*dark", "color_scheme_declared": r"(?<![-\w])color-scheme:\s*\w",
        "dark_class_theme": r"\.dark\b|\[data-theme=.?dark|\[data-mode=.?dark", "filter_invert": r"filter:\s*[^;]*invert\(",
        "background_clip_text": r"background-clip:\s*text", "oklch_in_css": r"oklch\(", "selection_styled": r"::selection",
        "accent_color": r"(?<![-\w])accent-color:", "caret_color": r"caret-color:", "scrollbar_color": r"scrollbar-color:",
        "forced_colors": r"forced-colors", "unreadable_sheets": r"/\* unreadable:"}.items()}
    colour_tokens = {k: v for k, v in dom.get("tokens", {}).items() if cl.parse(v) and cl.parse(v)[3] > 0}

    return {
        "width": w, "page": {**desc(page), "mode": "dark" if dark else "light"},
        "area": area, "first_screen": first,
        "text_roles": text_roles, "text_levels": {"count": len(text_levels), "levels": text_levels[:8],
                        "inverse_band_text": [desc(cl.parse(h), n=n) for h, n in inverse.most_common(4)]},
        "chromatic": {"hues": len(accents), "groups": accents[:6]},
        "grounds": {"count": len(grounds), "list": grounds[:8]},
        "grey_text_on_colour": grey_on_colour[:8],
        "neutrals": {"temperature": dict(temp.most_common()), "pure_black_white": dict(pure)},
        "depth": {"shadow_recipes": len(recipes), "top_recipes": [{"shadow": k[:100], "n": n} for k, n in recipes.most_common(5)],
                  "heavy_black_shadows": {"count": len(heavy), "examples": heavy[:4]},
                  "border_plus_shadow": {"count": len(both), "examples": both[:4]},
                  "dark_surfaces_darker_than_page": darker[:6], "glass": {"count": len(glass), "examples": glass[:4]}},
        "gradients": {"count": len(gradients), "examples": gradients[:6]},
        "css": flags, "colour_tokens": {"count": len(colour_tokens), "sample": dict(list(colour_tokens.items())[:12])},
    }


def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    run = pathlib.Path(sys.argv[1])
    widths = [int(x) for x in sys.argv[2:]] or [1440, 375]
    out = run / "03-lenses" / "color"; out.mkdir(parents=True, exist_ok=True)
    for w in widths:
        if not (run / "01-evidence" / f"dom-{w}.json").exists():
            print(f"{w}: no dom-{w}.json, not verified"); continue
        t = table(run, w)
        (out / f"palette-{w}.json").write_text(json.dumps(t, indent=1, ensure_ascii=False), encoding="utf8")
        p, a = t["page"], t["area"]
        print(f"== {w}px: page {p['hex']} (L {p['L']}, C {p['C']}, {p['mode']})")
        if "top" in a:
            print(f"  area (bg render, {a['images_masked_pct']}% images masked): neutral {a['neutral_pct']}%, chromatic {a['chromatic_pct']}% {a['chromatic_by_hue_pct']}")
            print("  top colours: " + ", ".join(f"{c['hex']} {c['pct']}%" for c in a["top"][:8]))
            f = t["first_screen"]
            if "top" in f: print(f"  first screen: neutral {f['neutral_pct']}%, chromatic {f['chromatic_pct']}% {f['chromatic_by_hue_pct']}")
        else: print(f"  {a.get('note', 'area palette not verified')}")
        for g in t["chromatic"]["groups"]:
            print(f"  hue {g['H']} {g['hex']}: {g['elements']} uses {g['uses']}, fill {g['fill_area_px']}px2, display text {len(g['display_text'])}, page-scale fills {len(g['page_scale_fills'])}")
        print(f"  text levels (neutral greys) {t['text_levels']['count']}: " + ", ".join(f"{l['hex']} x{l['n']}" for l in t["text_levels"]["levels"]))
        print(f"  grounds {t['grounds']['count']}: " + ", ".join(f"{g['hex']} x{g['sections']}" for g in t["grounds"]["list"]))
        print(f"  grey text on colour {len(t['grey_text_on_colour'])}; neutrals {t['neutrals']}")
        d = t["depth"]
        print(f"  shadows: {d['shadow_recipes']} recipes, heavy black {d['heavy_black_shadows']['count']}, border+shadow {d['border_plus_shadow']['count']}, dark darker-than-page {len(d['dark_surfaces_darker_than_page'])}, glass {d['glass']['count']}; gradients {t['gradients']['count']}")
        print(f"  css {t['css']}; colour tokens {t['colour_tokens']['count']}")
        print(f"  -> {out / f'palette-{w}.json'}")


if __name__ == "__main__":
    main()
