"""Icon and logo detectors (source 21: Stageshow references/craft.md, Icons and logos; benjitaylor/skills, MIT).

ai_sparkle     a sparkle, wand or stars glyph as the generic sign for AI, matched on icon-set names (never on drawing)
invented_mark  a one-letter tile in a saturated colour beside a real company's name (ported from film-checks.mjs
               detectInventedMark)
mixed_icons    filled and outline SVG glyphs side by side in one nav, list or toolbar
All read `icon` records from the DOM dump (extract.js): class names, data-lucide, aria-label, and the first shape's
computed fill, stroke and stroke width.
"""
import re, collections
from core import detector, hit, px, where
import colorlib as cl


def _icons(ev):
    # no inDialog filter: icons are usually aria-hidden, which extract.js folds into inDialog; closed menus are invisible anyway
    return [e for e in ev.visible() if e.get("icon")]


@detector("ai_sparkle")
def ai_sparkle(ev, cfg):
    pat = re.compile(cfg["names"], re.I)
    out = []
    for e in _icons(ev):
        ic = e["icon"]
        name = " ".join(filter(None, [ic.get("cls"), ic.get("lucide"), ic.get("label")]))
        m = pat.search(name)
        if not m or e["rect"]["w"] > cfg["max_px"] or e["rect"]["h"] > cfg["max_px"]: continue
        out.append(hit(cfg, where(e), f"\"{m.group(0)}\" icon ({name[:60]}): a sparkle or wand as the generic sign for AI says nothing about what the feature does",
                       after="Name the action in a plain label, or use the product's own mark"))
    for e in ev.texts():                       # Material Symbols / Material Icons ligatures: the glyph name is the text
        t = e["text"].strip()
        if t in cfg["ligatures"] and re.search(r"material", e["style"].get("fontFamily", ""), re.I):
            out.append(hit(cfg, where(e), f"Material \"{t}\" glyph: the generic sign for AI", after="Name the action in a plain label"))
    return out[:cfg["max_hits"]]


@detector("invented_mark")
def invented_mark(ev, cfg):
    brands = re.compile(r"\b(" + cfg["brands"] + r")\b", re.I)
    d = ev.dom()
    out = []
    for e in ev.visible():
        t = (e.get("text") or "").strip()
        if not re.fullmatch(r"[A-Z0-9]", t): continue
        r = e["rect"]
        if not (cfg["min_px"] <= r["w"] <= cfg["max_px"] and cfg["min_px"] <= r["h"] <= cfg["max_px"]): continue
        tile = None
        for x in [e] + ev.ancestors(e)[:1]:
            bg = cl.parse(x["style"].get("backgroundColor"))
            if bg and bg[3] >= 0.5 and max(bg[:3]) - min(bg[:3]) > cfg["min_spread"]:
                tile = x; break
        if not tile: continue
        row = d["byid"].get(int(tile["parent"])) if tile.get("parent") is not None else None
        words = ((row or {}).get("blockText") or "").replace(t, " ", 1)
        m = brands.search(words)
        if m:
            out.append(hit(cfg, where(e), f"a \"{t}\" tile in a brand colour beside \"{m.group(0)}\", a real company: an invented mark, not its logo",
                           after="Use the company's real mark in its original proportions and colours, or a plain text name"))
    return out[:cfg["max_hits"]]


def _paint(ic):
    """'filled' or 'outline' for an SVG glyph, from its first shape's computed fill and stroke; None when unclear."""
    f = cl.parse(ic.get("fill")) if ic.get("fill") not in (None, "none") else None
    s = cl.parse(ic.get("stroke")) if ic.get("stroke") not in (None, "none") else None
    sw = px(ic.get("strokeWidth") or 0)
    filled = bool(f and f[3] > 0.05)
    stroked = bool(s and s[3] > 0.05 and sw > 0)
    if filled and not stroked: return "filled"
    if stroked and not filled: return "outline"
    return None


GROUP_TAGS = ("nav", "ul", "ol", "menu", "header", "aside", "footer")


@detector("mixed_icons")
def mixed_icons(ev, cfg):
    """A group needs at least min_each of both kinds, so one filled "selected" glyph among outline ones (a platform
    convention for state) is not reported."""
    groups = collections.defaultdict(list)
    d = ev.dom()
    for e in _icons(ev):
        ic = e["icon"]
        if not ic.get("svg") or not (cfg["min_px"] <= e["rect"]["w"] <= cfg["max_px"]): continue
        p = _paint(ic)
        if not p: continue
        anc = ev.ancestors(e)
        box = next((a for a in anc[:6] if a["tag"] in GROUP_TAGS or a.get("role") in ("toolbar", "tablist", "menubar")), None)
        if box is None: box = anc[2] if len(anc) > 2 else (anc[-1] if anc else None)
        if box is not None: groups[box["id"]].append((p, px(ic.get("strokeWidth") or 0)))
    out = []
    for gid, items in groups.items():
        k = collections.Counter(p for p, _ in items)
        g = d["byid"].get(gid, {})
        widths = sorted({round(w, 2) for p, w in items if p == "outline" and w > 0})
        if k["filled"] >= cfg["min_each"] and k["outline"] >= cfg["min_each"]:
            out.append(hit(cfg, g.get("sel", "?"), f"{k['filled']} filled and {k['outline']} outline icons in one group: glyphs of different constructions read as made up",
                           value=dict(k), check="fill", after="One icon set, one style and one stroke width per group; fill only to mark state"))
        elif len(items) >= cfg["min_group"] and len(widths) >= 2 and widths[-1] / widths[0] >= cfg["width_ratio"]:
            # one icon set draws every glyph at one stroke width (computed in the glyph's own units, so size does not change it)
            out.append(hit(cfg, g.get("sel", "?"), f"outline icons in one group use stroke widths {', '.join(f'{w:g}px' for w in widths)}: glyphs from different sets or drawn by hand",
                           value=widths, check="stroke", after="Take every glyph in the group from one set at one stroke width"))
    return out[:cfg["max_hits"]]
