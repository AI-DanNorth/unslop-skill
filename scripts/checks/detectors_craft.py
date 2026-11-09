"""Craft detectors from the still-frame rules of source 21 (Stageshow references/craft.md, Spacing and alignment;
benjitaylor/skills, MIT). All Finish tier: they are finishing errors, not slop calls.

near_tangent   a painted box whose edge sits 2-3 px from its painted container's edge or from a painted sibling
               ("edges 1 to 3 px apart read as an accident"; 1 px is left out, because 1 px gaps are the usual hairline
               grid trick)
nested_radius  a rounded painted box evenly inset in a rounded painted container whose radius is not the inner radius
               plus the inset ("the outer radius equals the inner radius plus that padding")
unit_wrapped   a short figure whose unit lands on its own line ("a stat's unit on its own line")
"""
import re, collections
from core import detector, hit, px, where
import colorlib as cl


def _painted(e):
    s = e["style"]
    bg = cl.parse(s.get("backgroundColor"))
    return bool((bg and bg[3] > 0.05) or s.get("backgroundImage", "none") != "none" or px(s.get("borderTopWidth")) > 0 or s.get("boxShadow", "none") != "none")


def _box(e):
    r = e["rect"]
    return r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"]


def _parent(ev, e, w=None):
    a = ev.ancestors(e, w)
    return a[0] if a else None


def _painted_container(ev, e, depth):
    for a in ev.ancestors(e)[:depth]:
        if _painted(a) and a["rect"]["w"] > e["rect"]["w"] and a["rect"]["h"] >= e["rect"]["h"]: return a
    return None


SKIP_TAGS = {"td", "th", "tr", "tbody", "thead", "table", "html", "body", "input", "select", "textarea", "option", "svg", "path", "img", "video", "canvas", "iframe", "hr"}


@detector("near_tangent")
def near_tangent(ev, cfg):
    lo, hi = cfg["min_px"], cfg["max_px"]
    out, seen = [], set()
    vis = [e for e in ev.visible() if e["tag"] not in SKIP_TAGS and not e.get("inDialog") and e["rect"]["w"] >= cfg["min_size"] and e["rect"]["h"] >= cfg["min_size"]]
    painted = [e for e in vis if _painted(e)]
    # inside a painted container
    for e in painted:
        c = _painted_container(ev, e, 4)
        if not c or c["rect"]["w"] > cfg["max_container"]: continue
        ex0, ey0, ex1, ey1 = _box(e); cx0, cy0, cx1, cy1 = _box(c)
        for side, d in (("left", ex0 - cx0), ("top", ey0 - cy0), ("right", cx1 - ex1), ("bottom", cy1 - ey1)):
            if lo <= d <= hi and e["id"] not in seen:
                seen.add(e["id"])
                out.append(hit(cfg, where(e), f"its {side} edge sits {d:.0f}px inside its container's edge ({c['sel'].split(' > ')[-1]}): close enough to look like a miss",
                               value=d, after="Line the edges up exactly, or part them by the container's padding (at least 8px)"))
    # painted siblings stacked with a hair of space between
    kids = collections.defaultdict(list)
    for e in painted:
        if e.get("parent") is not None: kids[e["parent"]].append(e)
    for sibs in kids.values():
        sibs.sort(key=lambda e: e["rect"]["y"])
        for a, b in zip(sibs, sibs[1:]):
            ax0, ay0, ax1, ay1 = _box(a); bx0, by0, bx1, by1 = _box(b)
            if min(ax1, bx1) - max(ax0, bx0) < 0.5 * min(a["rect"]["w"], b["rect"]["w"]): continue
            d = by0 - ay1
            if lo <= d <= hi and b["id"] not in seen:
                seen.add(b["id"])
                out.append(hit(cfg, where(b), f"sits {d:.0f}px below the box above it: neither touching nor apart", value=d,
                               after="Join them (0px, shared border) or separate them by the layout's gap"))
    return out[:cfg["max_hits"]]


@detector("nested_radius")
def nested_radius(ev, cfg):
    out = []
    for e in ev.visible():
        rc = px(e["style"].get("borderTopLeftRadius"))
        if rc <= 0 or not _painted(e) or e["tag"] in SKIP_TAGS or e.get("inDialog"): continue
        if e["rect"]["w"] < cfg["min_size"] or e["rect"]["h"] < cfg["min_size"]: continue
        c = _painted_container(ev, e, 3)
        if not c: continue
        rp = px(c["style"].get("borderTopLeftRadius"))
        if rp <= 0 or rp >= 999 or rc >= 999: continue          # pills: radius is "fully round", not a corner size
        dx, dy = e["rect"]["x"] - c["rect"]["x"], e["rect"]["y"] - c["rect"]["y"]
        if not (cfg["min_inset"] <= dx <= cfg["max_inset"] and abs(dx - dy) <= 2): continue   # evenly nested at the corner
        want = rc + dx
        if rc > rp or abs(rp - want) > max(cfg["tolerance_px"], cfg["tolerance_ratio"] * dx):
            how = "rounder than its container" if rc > rp else f"container {rp:.0f}px, expected about {want:.0f}px"
            out.append(hit(cfg, where(e), f"radius {rc:.0f}px inset {dx:.0f}px in a {rp:.0f}px-radius container: {how}",
                           value={"inner": rc, "outer": rp, "inset": dx}, after=f"Outer radius = inner radius + inset: {want:.0f}px outer, or {max(rp - dx, 0):.0f}px inner"))
    return out[:cfg["max_hits"]]


FIGURE = re.compile(r"^[$€£¥]?\s?\d[\d.,]*\s?(%|[a-zA-Zµ]{1,5}|/\s?(mo|yr|month|year|day|wk))$")


@detector("unit_wrapped")
def unit_wrapped(ev, cfg):
    d = ev.dom()
    children = collections.defaultdict(list)
    for e in d["elements"]:
        if e.get("parent") is not None: children[int(e["parent"])].append(e)

    def rects(e, depth=0):
        out = list(e.get("textRects") or [])
        if depth < 3:
            for c in children.get(e["id"], []): out += rects(c, depth + 1)
        return out
    found = {}                 # one hit per figure: document order puts ancestors first, so the innermost match wins
    for e in ev.visible():
        t = (e.get("blockText") or e.get("text") or "").strip()
        if not t or len(t) > cfg["max_chars"] or not FIGURE.match(t) or e.get("inDialog"): continue
        if not re.search(r"\d\s?\D", t): continue
        rs = rects(e)
        if len(rs) < 2: continue
        fs = px(e["style"].get("fontSize")) or 16
        if max(r[1] for r in rs) - min(r[1] for r in rs) > 0.6 * fs:
            found[t] = hit(cfg, where(e), f"\"{t}\" breaks across lines: the unit sits on its own line",
                           after="Keep the figure and unit together (white-space: nowrap), size the figure to its box, or move the unit to the label")
    return list(found.values())[:cfg["max_hits"]]
