"""Detectors that combine other detectors' results (look families) or compare across deliveries (ledger)."""
import json, pathlib, collections, re, math
import yaml
from core import detector, hit, px, where, Skip, NotVerified, ROOT
import colorlib as cl
from detectors_visual import rendered_family, eff_bg, is_serif, first_family

MONO = re.compile(r"mono|courier|consolas|menlo", re.I)

def page_bg(ev):
    d = ev.dom()
    for k in ("bodyBg", "htmlBg"):
        c = cl.parse(d.get(k))
        if c and c[3] > 0.5: return c
    return (1, 1, 1, 1)

def tells(ev, results):
    """Evaluate every tell in data/look-families.yaml. Returns {family: {tell_id: evidence or None}}."""
    fired = lambda det: bool(results.get(det, {}).get("hits"))
    d = ev.dom(); vis = ev.visible(); texts = ev.texts()
    bg = page_bg(ev); L, C, H = cl.oklch(bg)
    r, g, b = (round(x * 255) for x in bg[:3])
    colours = []
    for e in vis:
        for k in ("color", "backgroundColor", "borderTopColor"):
            if k == "borderTopColor" and not px(e["style"]["borderTopWidth"]): continue
            c = cl.parse(e["style"][k])
            if c and c[3] > 0.3: colours.append(c)
        colours += [c for c in cl.colors_in(e["style"]["backgroundImage"]) if c[3] > 0.3]
    vivid = {cl.hexstr(c) for c in colours if cl.oklch(c)[1] > 0.15}
    hs = [e for e in texts if e.get("level") in (1, 2)]
    serif_display = [e for e in hs if is_serif(rendered_family(ev, e) + "," + e["style"]["fontFamily"])]
    # Italic serif display text: the heading itself, or (the common case) an italic accent word in a child span of an h1/h2.
    # Before 9 Nov 2026 only the heading element was checked, so this tell never fired on any of 84 test items.
    italic_serif = [e for e in texts if e["style"]["fontStyle"] == "italic" and px(e["style"]["fontSize"]) >= 40
                    and is_serif(rendered_family(ev, e) + "," + e["style"]["fontFamily"])
                    and (e.get("level") in (1, 2) or any(a.get("level") in (1, 2) for a in ev.ancestors(e)))]
    mono_labels = [e for e in texts if MONO.search(rendered_family(ev, e)) and e["textLen"] < 40 and e["tag"] not in ("code", "pre", "kbd", "samp")]
    bordered = [e for e in vis if px(e["style"]["borderTopWidth"]) > 0 or px(e["style"]["borderBottomWidth"]) > 0]
    hair = [e for e in bordered if e["tag"] not in ("td", "th", "tr", "table", "input", "textarea", "select") and e["rect"]["w"] > 200 and (px(e["style"]["borderTopWidth"]) == 1 or px(e["style"]["borderBottomWidth"]) == 1)]
    zero = [e for e in bordered if px(e["style"]["borderTopLeftRadius"]) == 0]
    radii = {e["style"]["borderTopLeftRadius"] for e in vis if px(e["style"]["borderTopLeftRadius"]) > 0}
    fams = {rendered_family(ev, e) for e in texts if e["textLen"] > 2}
    grid_eq = [e for e in vis if (lambda cols: 3 <= len(cols) <= 4 and len(set(cols)) == 1)(e["style"]["gridTemplateColumns"].split()) and e["style"]["gridTemplateColumns"] != "none"]
    greys = {"#6b7280", "#9ca3af", "#64748b"}
    stock_grey = [e for e in texts if cl.parse(e["style"]["color"]) and cl.hexstr(cl.parse(e["style"]["color"])) in greys]
    purple = [c for c in colours if cl.hexstr(c) in ("#6366f1", "#8b5cf6") or (cl.oklch(c)[1] > 0.12 and 265 <= cl.oklch(c)[2] <= 330)]
    terracotta = [c for c in colours if cl.oklab_dist(c, cl.parse("#d97757")) < 0.07 or (cl.oklch(c)[1] >= 0.08 and 15 <= cl.oklch(c)[2] <= 55)]
    gp = [h for h in results.get("gradient", {}).get("hits", []) if h.get("banned_pair")]
    caps_labels = [e for e in texts if e["textLen"] < 40 and px(e["style"]["fontSize"]) <= 14 and (e["style"]["textTransform"] == "uppercase" or (e["text"].isupper() and len(e["text"]) > 3))
                   and e["style"]["letterSpacing"] != "normal" and px(e["style"]["letterSpacing"]) / max(1, px(e["style"]["fontSize"])) >= 0.06]
    T = lambda cond, ev_: ev_ if cond else None
    return {
        "warm-paper-serif": {
            "cream_bg": T((L > 0.90 and 40 <= H <= 110 and C >= 0.003) or (min(r, g, b) >= 209 and r >= g >= b and 6 <= r - b <= 48), f"page {cl.hexstr(bg)}"),
            "terracotta_accent": T(bool(terracotta), terracotta and cl.hexstr(terracotta[0])),
            "serif_display": T(bool(serif_display), serif_display and rendered_family(ev, serif_display[0])),
            "italic_serif_hero": T(bool(italic_serif), "italic serif headline"),
            "eyebrows": T(fired("eyebrow") or len(caps_labels) >= 3, "eyebrow detector" if fired("eyebrow") else f"{len(caps_labels)} tracked caps labels"),
            "numbered_labels": T(fired("numbered_labels"), "numbered labels"),
        },
        "dark-single-accent": {
            "dark_bg": T(L < 0.20, f"page {cl.hexstr(bg)}"),
            "single_vivid": T(len(vivid) == 1, ", ".join(vivid)),
            "neon_cyan_violet": T(fired("neon_violet"), "neon detector"),
            "glow": T(fired("glow"), "glow detector"),
            "mono_labels": T(len(mono_labels) >= 3, f"{len(mono_labels)} mono labels"),
        },
        "hairline-newspaper": {
            "hairlines": T(len(hair) >= 8, f"{len(hair)} hairlines"),
            "zero_radius": T(len(bordered) >= 5 and len(zero) / len(bordered) > 0.9, "zero radius"),
            "mono_labels": T(len(mono_labels) >= 3, f"{len(mono_labels)} mono labels"),
            "italic_serif": T(bool(italic_serif), "italic serif"),
        },
        "saas-card-kit": {
            "card_kit": T(fired("card_kit"), "card kit detector"),
            "icon_tiles": T(fired("icon_tile"), "icon tile detector"),
            "equal_grid": T(bool(grid_eq), grid_eq and f"grid {grid_eq[0]['style']['gridTemplateColumns']}"),
            "inter_only": T(len(fams) == 1 and next(iter(fams)).lower() in ("inter", "roboto", "system-ui", "arial", "helvetica"), ", ".join(fams)),
            "stock_greys": T(bool(stock_grey), "stock grey text"),
        },
        "violet-gradient": {
            "ai_purple": T(bool(purple), purple and cl.hexstr(purple[0])),
            "gradient_pair": T(bool(gp), "banned gradient pair"),
            "glow": T(fired("glow"), "glow detector"),
        },
    }

@detector("look_family")
def look_family(ev, cfg, results=None):
    need = (cfg.get("_profile") or {}).get("look_family_cluster_min", 3)
    famcfg = yaml.safe_load((ROOT / "data" / "look-families.yaml").read_text(encoding="utf-8"))["families"]
    out = []
    for fam, ts in tells(ev, results or {}).items():
        on = {k: v for k, v in ts.items() if v}
        if len(on) >= need + (famcfg.get(fam) or {}).get("cluster_extra", 0):
            out.append(hit(cfg, "whole page", f"{fam}: {len(on)} of {len(ts)} tells ({'; '.join(f'{k} ({v})' for k, v in on.items())}); cluster minimum {need}", value=len(on), family=fam))
    return out

# ------------------------------------------------------------------ ledger and distinctness
def signature(ev):
    """Palette (top 6 colours, area weighted) and a 32x20 edge map of the first screen."""
    import numpy as np
    from PIL import Image
    name = f"fold-{ev.primary}.png" if ev.has(f"fold-{ev.primary}.png") else f"shot-{ev.primary}.png"
    im = Image.open(ev.dir / name).convert("RGB")
    a = np.asarray(im.resize((160, 100)))
    q = (a // 32).reshape(-1, 3); keys = q[:, 0] * 64 + q[:, 1] * 8 + q[:, 2]
    cnt = np.bincount(keys, minlength=512); top = cnt.argsort()[::-1][:6]
    pal = [{"hex": "#%02x%02x%02x" % ((k // 64) * 32 + 16, ((k // 8) % 8) * 32 + 16, (k % 8) * 32 + 16), "share": round(float(cnt[k] / cnt.sum()), 3)} for k in top if cnt[k]]
    g = np.asarray(im.convert("L").resize((32, 20)), dtype="float32")
    edges = np.hypot(np.diff(g, axis=1, prepend=g[:, :1]), np.diff(g, axis=0, prepend=g[:1, :]))
    d = ev.dom()
    hs = [e for e in ev.texts() if e.get("level") == 1] or [e for e in ev.texts() if e.get("level")]
    return {"palette": pal, "edges": [round(float(x), 1) for x in edges.flatten()], "bg": cl.hexstr(page_bg(ev)),
            "display_face": rendered_family(ev, hs[0]) if hs else None}

def palette_distance(p1, p2):
    def one_way(a, b):
        tot = sum(x["share"] for x in a) or 1
        return sum(x["share"] * min(cl.oklab_dist(cl.parse(x["hex"]), cl.parse(y["hex"])) for y in b) for x in a) / tot
    return (one_way(p1, p2) + one_way(p2, p1)) / 2

def edge_corr(e1, e2):
    import numpy as np
    a, b = np.array(e1), np.array(e2)
    if a.std() == 0 or b.std() == 0: return 0.0
    return float(np.corrcoef(a, b)[0, 1])

def ledger_path(ev):
    for p in (ev.run.parent / "ledger.jsonl", pathlib.Path.home() / ".unslop/ledger.jsonl"):
        if p.exists(): return p
    return None

@detector("distinctness")
def distinctness(ev, cfg):
    lp = ledger_path(ev)
    if not lp: raise Skip("no ledger yet (skills/ledger records deliveries)")
    entries = [json.loads(l) for l in lp.read_text().splitlines() if l.strip()][-cfg["ledger_size"]:]
    entries = [e for e in entries if e.get("run") != str(ev.run)]
    if not entries: raise Skip("ledger has no other deliveries")
    me = signature(ev); out = []
    for e in entries:
        pd, ec = palette_distance(me["palette"], e["palette"]), edge_corr(me["edges"], e["edges"])
        same_face = me["display_face"] and me["display_face"] == e.get("display_face")
        if pd < cfg["min_palette_oklab"] or ec > cfg["max_edge_corr"] or (same_face and me["bg"] == e.get("bg")):
            out.append(hit(cfg, f"vs {e.get('label', e.get('run'))}", f"palette distance {pd:.3f} (min {cfg['min_palette_oklab']}), skeleton correlation {ec:.2f} (max {cfg['max_edge_corr']}){', same display face and background' if same_face and me['bg'] == e.get('bg') else ''}",
                           value={"palette": round(pd, 3), "edges": round(ec, 2)}))
    return out
