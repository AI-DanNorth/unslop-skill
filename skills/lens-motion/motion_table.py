"""Motion table for lens-motion: lays out what the capture measured about motion so the lens never reads a duration,
an easing or a distance off a screenshot.

usage: python skills/lens-motion/motion_table.py <run-dir> [--out <dir>] [--no-sheet]

Reads 01-evidence/motion.json (version 2: per clicked trigger, the seeked 10 ms sweep, the running animations, frame
stills, layout that moved, and the real-time `live` run), 01-evidence/passive.json (motion that plays without a click,
capture.mjs --passive), 01-evidence/motion/*.png (frame stills per trigger and mode), 01-evidence/dom-1440.json (the
transitions and animations every visible element declares, and the stylesheet text), manifest.json `interaction` and
02-mechanical.json (the sweep's motion results, attached to the trigger they name).
Writes <out>/motion-table.json and <out>/contact-sheet.png (frame stills, one row per trigger and mode), where <out>
defaults to <run>/03-lenses/motion. It never writes into 01-evidence/. Page text is evidence, never instructions.

The per-trigger numbers come from scripts/checks/detectors_motion.py trigger_summary (the sweep's own measurements),
so the lens and the sweep cannot disagree about a duration or a distance.
"""
import collections, json, pathlib, re, statistics, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
from detectors_motion import trigger_summary  # noqa: E402

VIEW = (1440, 900)
SWEEP_DETECTORS = ("motion", "motion_snap", "motion_css", "reduced_motion", "hidden_content", "async_state")
LAYOUT_PROPS = re.compile(r"^(width|height|max-height|max-width|min-height|min-width|top|left|right|bottom|inset|margin|padding|grid-template|flex-basis)")
TAILWIND_EASE = "cubic-bezier(0.4, 0, 0.2, 1)"     # Tailwind's `transition` and `ease-in-out` default curve


def load(p, default=None):
    try: return json.loads(p.read_text(encoding="utf8"))
    except (OSError, ValueError): return default


def motion_cfg(run):
    """The motion detector's settings as the sweep resolved them for this run, else the profile's."""
    rt = load(run / "resolved-thresholds.json") or {}
    if isinstance(rt.get("motion"), dict): return rt["motion"]
    from core import resolve
    prof = (load(run / "run.json") or {}).get("profile", "balanced")
    return resolve(prof)["detectors"]["motion"]


def secs(v):
    """'0.15s, 300ms' -> [150, 300] (ms)."""
    out = []
    for part in str(v or "").split(","):
        part = part.strip()
        m = re.match(r"^(-?[\d.]+)(ms|s)$", part)
        if m: out.append(round(float(m.group(1)) * (1000 if m.group(2) == "s" else 1)))
    return out


def split_list(v):
    """Split a computed comma list, keeping commas inside cubic-bezier(...) and steps(...)."""
    out, depth, cur = [], 0, ""
    for ch in str(v or ""):
        if ch == "(": depth += 1
        if ch == ")": depth -= 1
        if ch == "," and depth == 0: out.append(cur.strip()); cur = ""
        else: cur += ch
    if cur.strip(): out.append(cur.strip())
    return out


def ease_flags(e):
    """What an easing value is: the browser default, linear, a framework default, or a curve that overshoots."""
    e = (e or "").strip()
    f = []
    if e == "ease": f.append("browser default ease")
    if e == "linear": f.append("linear")
    if e == TAILWIND_EASE: f.append("Tailwind default curve")
    m = re.match(r"cubic-bezier\(([^)]*)\)", e)
    if m:
        try:
            x1, y1, x2, y2 = (float(x) for x in m.group(1).split(","))
            if y1 > 1 or y2 > 1: f.append(f"overshoots (y {max(y1, y2):g})")
            if y1 < 0 or y2 < 0: f.append(f"anticipates (y {min(y1, y2):g})")
        except ValueError: pass
    if e.startswith("linear("): f.append("linear() spring or bounce")
    if e.startswith("steps("): f.append("steps")
    return f


def stagger(anims):
    """Delays across a trigger's finite animations: count, distinct steps and the total spread."""
    ds = sorted({a.get("delayMs") or 0 for a in anims})
    if len(ds) < 3: return None
    steps = [b - a for a, b in zip(ds, ds[1:])]
    return {"items": len(anims), "distinct_delays": len(ds), "step_ms": round(statistics.median(steps)), "spread_ms": ds[-1] - ds[0]}


def sweep_index(run):
    mech = load(run / "02-mechanical.json") or {}
    dets = mech.get("detectors") or {}
    status = {}
    for k in SWEEP_DETECTORS:
        d = dets.get(k)
        if not d: status[k] = "absent"; continue
        s = d.get("status", "?")
        if d.get("reason"): s += f" ({d['reason'][:120]})"
        status[k] = {"status": s, "rule": d.get("rule"), "hits": len(d.get("hits") or [])}
    hits = [(k, h) for k in ("motion", "motion_snap") for h in ((dets.get(k) or {}).get("hits") or [])]
    return status, hits


def trigger_row(i, t, cfg, run, ev, hits):
    S = trigger_summary(t, cfg)
    n = t["runs"].get("normal") or {}
    r = t["runs"].get("reduce") or {}
    row = {"t": i, "kind": t["kind"], "name": t["name"][:60], "selector": t["selector"][-90:], "normal": S["normal_status"], "reduce": S["reduce_status"]}
    if n.get("status") == "ok":
        row["timing"] = n.get("timing")            # seeked: CSS/WAAPI, measured at 10 ms; realtime: JavaScript or instant
        row["opened"] = n.get("rootSource")
        if n.get("note"): row["note"] = n["note"]
        finite = [a for a in n.get("animations", []) if a.get("iterations") != "infinite"]
        moving = [a for a in finite if a.get("root", -1) >= 0]
        roots = S.get("roots") or []
        row["changed"] = [c.get("name") or c.get("selector", "")[-40:] for c in (n.get("changed") or [])][:6]
        if roots:
            big = max(roots, key=lambda x: x["end_box"][2] * x["end_box"][3])
            inplace = [x for x in roots if not x["ends_on_edge"]]
            row["duration_ms"] = max(x["duration_ms"] for x in roots)
            row["largest_box"] = {"w": big["end_box"][2], "h": big["end_box"][3], "viewport_pct": round(100 * big["end_box"][2] * big["end_box"][3] / (VIEW[0] * VIEW[1]), 1),
                                  "selector": big["selector"][-60:]}
            row["min_start_scale"] = min(x["start_scale"] for x in roots)
            row["max_travel_px"] = max((x["travel_px"] for x in inplace), default=None)
            row["max_overshoot"] = max(max(x["size_overshoot"], x["pos_overshoot"]) for x in roots)
            row["entering"] = sum(1 for x in roots if x["entering"]); row["leaving"] = len(roots) - row["entering"]
        row["anim_end_ms"] = S.get("anim_end_ms")
        groups = collections.Counter((",".join(a["props"][:3]), a.get("durationMs"), a.get("easing")) for a in moving)
        row["animations"] = [{"props": p, "ms": d, "easing": e, "count": c, **({"flags": ease_flags(e)} if ease_flags(e) else {})} for (p, d, e), c in groups.most_common(6)]
        row["paint_only"] = len(finite) - len(moving)       # colour and filter feedback on elements that do not move
        row["layout_props"] = sorted({p for a in moving for p in a["props"] if LAYOUT_PROPS.match(p)})
        row["infinite"] = [f"{a['name'] or ','.join(a['props'][:2])} {a.get('durationMs')} ms" for a in n.get("animations", []) if a.get("iterations") == "infinite"][:4]
        st = stagger(moving)
        if st: row["stagger"] = st
        if S.get("layout_moved"):
            L = S["layout_top"] or {}
            row["layout_moved"] = {"count": S["layout_moved"], "top": f"\"{(L.get('name') or '')[:30]}\" {L.get('midPx')} px off its start and end at {L.get('atMs')} ms"}
        live = n.get("live") or {}
        if live:
            row["live"] = {"coverage": live.get("coverage"), **({"reason": live["reason"]} if live.get("reason") else {}),
                           "motion_end_ms": live.get("motionEndMs"), "still_moving": live.get("stillMoving"), "frame_ms": live.get("frameMs"),
                           "ambient": live.get("ambient"), "snaps": [f"{s['kind']} {s['dPx']:+g} px on {s['axis']} at {s['atMs']} ms: \"{(s.get('text') or s.get('name') or '')[:30]}\"" for s in live.get("snaps", [])][:5]}
    if r.get("status") == "ok":
        red = S.get("reduce") or {}
        ra = [a for a in r.get("animations", []) if a.get("root", -1) >= 0]
        row["reduce_motion"] = {"timing": r.get("timing"), "move_px": red.get("move_px"), "scale_dev": red.get("scale_dev"),
                                "animations": sorted({f"{','.join(a['props'][:2])} {a.get('durationMs')} ms" for a in ra})[:4],
                                "changed": len(r.get("changed") or [])}
    pre = f"{t['kind']} trigger \"{t['name'][:40]}\""
    row["sweep_hits"] = [f"{k}/{h.get('check')}: {h['evidence'][:140]}" for k, h in hits if h["where"].startswith(pre)][:6]
    row["frames"] = {m: [f["file"] for f in (t["runs"].get(m) or {}).get("frames", []) if (ev / f["file"]).exists()] for m in ("normal", "reduce")}
    row["frame_ms"] = {m: [f.get("actualMs") for f in (t["runs"].get(m) or {}).get("frames", [])] for m in ("normal", "reduce")}
    return row


def passive_row(p):
    out = {"window_ms": p.get("ms")}
    for mode in ("normal", "reduce"):
        x = p.get(mode) or {}
        d = {"coverage": x.get("coverage", "missing")}
        if x.get("reason"): d["reason"] = x["reason"]
        if x.get("coverage") == "ok":
            d.update({"motion_end_ms": x.get("motionEndMs"), "still_moving": x.get("stillMoving"), "frame_ms": x.get("frameMs"), "late_frames": x.get("lateFrames"),
                      "snaps": [f"{s['kind']} {s['dPx']:+g} px on {s['axis']} at {s['atMs']} ms: \"{(s.get('text') or s.get('name') or '')[:30]}\"" for s in x.get("snaps", [])][:6]})
        out[mode] = d
    return out


def declared(ev):
    """Transitions and animations the visible elements declare at 1440 (computed styles), and stylesheet flags."""
    dom = load(ev / "dom-1440.json")
    if not dom: return {"note": "dom-1440.json missing: declared motion not verified"}
    tr, an, eases, durs = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    n_vis = 0
    for e in dom.get("elements", []):
        if not e.get("vis"): continue
        n_vis += 1
        s = e.get("style") or {}
        ds = secs(s.get("transitionDuration"))
        if any(d > 0 for d in ds):
            props = split_list(s.get("transitionProperty"))
            fns = split_list(s.get("transitionTimingFunction"))
            tr[(", ".join(props[:3])[:40], "/".join(str(d) for d in ds[:3]), (fns or ["?"])[0])] += 1
            for f in set(fns): eases[f] += 1
            for d in set(ds):
                if d > 0: durs[d] += 1
        names = [x for x in split_list(s.get("animationName")) if x and x != "none"]
        if names:
            an[(", ".join(names[:2])[:40], "/".join(str(d) for d in secs(s.get("animationDuration"))[:2]))] += 1
    css = dom.get("css") or []
    text = "\n".join(css) if isinstance(css, list) else str(css)
    count = lambda pat: len(re.findall(pat, text, re.I))
    return {
        "visible_elements": n_vis,
        "transitions": [{"props": p, "ms": d, "easing": f, "elements": c, **({"flags": ease_flags(f)} if ease_flags(f) else {})} for (p, d, f), c in tr.most_common(10)],
        "transition_elements": sum(tr.values()),
        "easings": [{"easing": f, "elements": c, **({"flags": ease_flags(f)} if ease_flags(f) else {})} for f, c in eases.most_common(8)],
        "durations_ms": dict(sorted(durs.items())),
        "running_animations": [{"name": nm, "ms": d, "elements": c} for (nm, d), c in an.most_common(8)],
        "stylesheet": {"readable_rules": len(css) if isinstance(css, list) else None, "keyframes": count(r"@keyframes"), "infinite": count(r"\binfinite\b"),
                       "prefers_reduced_motion": count(r"prefers-reduced-motion"), "scroll_timeline": count(r"animation-timeline|view-timeline|scroll-timeline"),
                       "view_transitions": count(r"view-transition"), "smooth_scroll": count(r"scroll-behavior\s*:\s*smooth"),
                       "transition_all": count(r"transition(-property)?\s*:\s*all\b"), "will_change": count(r"will-change")},
    }


def contact_sheet(ev, rows, path, h=120, max_w=260):
    from PIL import Image, ImageDraw
    lines = [(f"t{r['t']} {r['kind']} \"{r['name'][:28]}\" {m}", r["frames"][m], r["frame_ms"][m]) for r in rows for m in ("normal", "reduce") if r["frames"].get(m)]
    if not lines: return None
    label_w, gap = 230, 6
    width = label_w + 7 * (max_w + gap)
    sheet = Image.new("RGB", (width, len(lines) * (h + 22) + 8), "white")
    d = ImageDraw.Draw(sheet)
    for k, (label, files, ms) in enumerate(lines):
        y = 4 + k * (h + 22)
        d.text((6, y + h // 2 - 6), label, fill="black")
        x = label_w
        for f, t in zip(files, ms):
            try: im = Image.open(ev / f).convert("RGB")
            except OSError: continue
            im.thumbnail((max_w, h))
            sheet.paste(im, (x, y)); d.rectangle([x, y, x + im.width - 1, y + im.height - 1], outline=(200, 200, 200))
            d.text((x + 2, y + h + 4), f"{t} ms", fill=(90, 90, 90))
            x += max_w + gap
    sheet.save(path)
    return path


def table(run, out_dir, sheet=True):
    ev = run / "01-evidence"
    man = load(ev / "manifest.json") or {}
    inter = man.get("interaction") or {}
    cfg = motion_cfg(run)
    status, hits = sweep_index(run)
    res = {"run": run.name, "interaction": {k: inter.get(k) for k in ("motion", "passive") if inter.get(k) is not None}, "sweep": status}

    m = load(ev / "motion.json")
    rows = []
    if m is None:
        mi = inter.get("motion") or {}
        res["triggers_note"] = f"motion.json missing ({'skipped: ' + mi['skipped'] if mi.get('skipped') else 'error: ' + mi['error'] if mi.get('error') else 'capture predates interaction capture'})"
    else:
        res["capture"] = {"found": m.get("found"), "tried": len(m.get("triggers") or []), "not_verified": m.get("notVerified", []),
                          "not_tried": [f"{s.get('name') or s.get('selector')}: {s.get('reason')}" for s in m.get("skipped", [])][:8]}
        rows = [trigger_row(i, t, cfg, run, ev, hits) for i, t in enumerate(m.get("triggers") or [])]
    res["triggers"] = rows

    p = load(ev / "passive.json")
    res["passive"] = passive_row(p) if p else {"note": "no passive recording (capture.mjs --passive <ms> not run): motion that plays without a click is not verified"}
    res["declared"] = declared(ev)

    # the measured system across triggers: one curve family (C38) and one duration scale (C39)?
    eas, durs = collections.Counter(), collections.Counter()
    for r in rows:
        for a in r.get("animations", []):
            eas[a["easing"]] += a["count"]
            if a["ms"]: durs[a["ms"]] += a["count"]
    res["measured_system"] = {"easings": [{"easing": e, "animations": c, **({"flags": ease_flags(e)} if ease_flags(e) else {})} for e, c in eas.most_common()],
                              "durations_ms": dict(sorted(durs.items()))}

    measured = sum(1 for r in rows if r["normal"] == "ok")
    moved = sum(1 for r in rows if r.get("animations") or (r.get("live") or {}).get("motion_end_ms"))
    pas_ok = (res["passive"].get("normal") or {}).get("coverage") == "ok"
    reasons = []
    if not measured: reasons.append(res.get("triggers_note") or "no trigger could be measured" if not rows else "no trigger could be measured: " + "; ".join(f"{r['name']}: {r['normal']}" for r in rows[:3]))
    if not pas_ok: reasons.append("no passive recording" if "note" in res["passive"] else f"passive recording {(res['passive'].get('normal') or {}).get('coverage')}")
    res["evidence"] = {"triggers_measured": measured, "triggers_with_motion": moved, "passive_ok": pas_ok, "has_motion_evidence": bool(measured or pas_ok),
                       **({"missing": reasons} if reasons else {})}

    out_dir.mkdir(parents=True, exist_ok=True)
    if sheet and rows:
        try: res["contact_sheet"] = str(contact_sheet(ev, rows, out_dir / "contact-sheet.png") or "") or None
        except Exception as e: res["contact_sheet"] = f"not made: {e}"
    (out_dir / "motion-table.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf8")
    return res


def summary(res):
    E = res["evidence"]
    print(f"{res['run']}: {E['triggers_measured']} trigger(s) measured, {E['triggers_with_motion']} with motion; passive {'ok' if E['passive_ok'] else 'none'}"
          + ("" if E["has_motion_evidence"] else "  -> NO MOTION EVIDENCE: score null; " + "; ".join(E.get("missing", []))))
    for r in res["triggers"]:
        if r["normal"] != "ok": print(f"  t{r['t']} {r['kind']} \"{r['name'][:30]}\": {r['normal']}"); continue
        live = r.get("live") or {}
        an = "; ".join(f"{a['props']} {a['ms']} ms {a['easing']}" + (f" x{a['count']}" if a['count'] > 1 else "") for a in r.get("animations", [])[:2])             or ("no CSS/WAAPI animation (JavaScript-driven)" if live.get("motion_end_ms") else "instant: no animation and no live movement")
        bits = [f"{r.get('duration_ms', '-')} ms" if r.get("duration_ms") is not None else None,
                f"live end {live.get('motion_end_ms')} ms{' (still moving)' if live.get('still_moving') else ''}" if live.get("motion_end_ms") else None,
                f"travel {r['max_travel_px']} px" if r.get("max_travel_px") else None,
                f"box {r['largest_box']['w']:g}x{r['largest_box']['h']:g} px ({r['largest_box']['viewport_pct']}% of the viewport)" if r.get("largest_box") else None,
                f"stagger {r['stagger']['step_ms']} ms x{r['stagger']['distinct_delays']}" if r.get("stagger") else None,
                f"layout moved {r['layout_moved']['count']}" if r.get("layout_moved") else None,
                f"snaps {len(live.get('snaps', []))}" if live.get("snaps") else None,
                f"reduce moves {r['reduce_motion']['move_px']} px" if (r.get("reduce_motion") or {}).get("move_px") else None]
        print(f"  t{r['t']} {r['kind']} \"{r['name'][:30]}\": " + ", ".join(b for b in bits if b) + f" | {an}" + (f" | sweep: {len(r['sweep_hits'])} hit(s)" if r["sweep_hits"] else ""))
    pn = (res["passive"].get("normal") or {})
    if pn.get("coverage") == "ok":
        pr = res["passive"].get("reduce") or {}
        end = lambda x: "no movement" if x.get("motion_end_ms") is None else f"motion ends {x['motion_end_ms']} ms" + (" (still moving)" if x.get("still_moving") else "")
        print(f"  passive ({res['passive'].get('window_ms')} ms from load): {end(pn)}, {len(pn.get('snaps', []))} snap(s); reduced motion: {end(pr) if pr.get('coverage') == 'ok' else pr.get('coverage')}")
    D = res["declared"]
    if "transitions" in D:
        top = D["easings"][0] if D["easings"] else None
        print(f"  declared: {D['transition_elements']} element(s) with transitions" + (f", top easing {top['easing']} on {top['elements']}" if top else "")
              + f"; running animations {', '.join(a['name'] + ' ' + a['ms'] + ' ms' for a in D['running_animations'][:3]) or 'none'}; reduced-motion rules {D['stylesheet']['prefers_reduced_motion']}")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args: print(__doc__); return 2
    run = pathlib.Path(args[0]).resolve()
    out = run / "03-lenses" / "motion"
    if "--out" in argv:
        out = pathlib.Path(argv[argv.index("--out") + 1]).resolve()
        args = [a for a in args if pathlib.Path(a).resolve() != out]
    if (run / "01-evidence") in out.parents or out == run / "01-evidence":
        print("refusing to write into 01-evidence/"); return 2
    res = table(run, out, sheet="--no-sheet" not in argv)
    summary(res)
    print(f"wrote {out / 'motion-table.json'}" + (f" and {res['contact_sheet']}" if res.get("contact_sheet") and not str(res["contact_sheet"]).startswith("not") else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
