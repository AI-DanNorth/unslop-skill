"""Motion and async-state detectors, measured from interaction capture (scripts/capture/interact.mjs).

motion       reads 01-evidence/motion.json: per trigger, a 10 ms sweep of the changed elements' bounding boxes and opacity
             (CSS/WAAPI animations paused and seeked), seven screenshot frames, the end state, and other content that
             moved while the transition ran, with prefers-reduced-motion off and on.
async_state  reads 01-evidence/async.json: per primary action, the UI before the click, at 0.5 s, 2 s and after the
             request completed (fetch/XHR held 3 s), the request log, a text timeline, and a forced-failure rerun.
Anything the capture could not measure raises NotVerified or is listed in the result's `partial` notes; never a pass.
"""
import math, re
from core import detector, hit, Skip, NotVerified


class Hits(list):
    """A hit list that also carries notes on what could not be measured (copied to the sweep result as `partial`)."""
    def __init__(self):
        super().__init__()
        self.partial = []


def _interaction(ev, key, fname):
    inter = (ev.manifest.get("interaction") or {}).get(key) or {}
    if inter.get("skipped"): raise NotVerified(f"{key} capture skipped ({inter['skipped']})")
    if inter.get("error"): raise NotVerified(f"{key} capture failed: {inter['error']}")
    return ev.json(fname)          # NotVerified when the file is missing (capture predates interact.mjs)


# ------------------------------------------------------------------------------------------------ motion
def _center(b): return (b[0] + b[2] / 2, b[1] + b[3] / 2)


def _shift(b, F):
    """Translation of box b relative to box F, without the part a scale explains: per axis, the movement both edges
    share (a box scaling about its own origin moves its edges apart, or keeps one still, so it has no common part)."""
    out = []
    for lo, size in ((0, 2), (1, 3)):
        d1, d2 = b[lo] - F[lo], (b[lo] + b[size]) - (F[lo] + F[size])
        out.append(0.0 if d1 * d2 <= 0 else math.copysign(min(abs(d1), abs(d2)), d1))
    return out


def root_metrics(sweep, k, final, cfg):
    """Measured numbers for changed element k: duration, start scale, travel and overshoot, from the 10 ms sweep."""
    F = final[k]
    S = [(s["t"], s["roots"][k]) for s in sweep if k < len(s["roots"])]
    if not S or F[2] <= 0 or F[3] <= 0: return None
    sp, so = cfg["settle_px"], cfg["settle_opacity"]
    differs = lambda b: any(abs(b[j] - F[j]) > sp for j in range(4)) or abs(b[4] - F[4]) > so
    moving = [t for t, b in S if differs(b)]
    duration = (max(moving) + 10) if moving else 0
    b0 = S[0][1]
    scale0 = min(b0[2] / F[2], b0[3] / F[3]) if b0[2] > 0 and b0[3] > 0 else 0.0
    d0 = _shift(b0, F); travel = math.hypot(*d0)
    # size overshoot: growing past the end size (or shrinking below it) on the way
    if scale0 < 0.98: size_os = max(max(b[2] / F[2], b[3] / F[3]) for _, b in S)
    elif scale0 > 1.02: size_os = max(max(F[2] / b[2], F[3] / b[3]) for _, b in S if b[2] > 0 and b[3] > 0)
    else: size_os = 1.0
    size_px = max(max(b[2] - F[2], b[3] - F[3]) for _, b in S) if scale0 < 0.98 else 0.0
    # position overshoot: passing the end position against the direction of travel
    pos_os, pos_px = 1.0, 0.0
    if travel >= 4:
        ux, uy = d0[0] / travel, d0[1] / travel
        past = max(-(_shift(b, F)[0] * ux + _shift(b, F)[1] * uy) for _, b in S)
        if past > 0: pos_px, pos_os = past, 1 + past / travel
    edge = F[0] <= 1 or F[1] <= 1 or F[0] + F[2] >= 1439 or F[1] + F[3] >= 899
    return {"duration_ms": duration, "start_scale": round(scale0, 3), "travel_px": round(travel, 1), "size_overshoot": round(size_os, 3),
            "size_overshoot_px": round(size_px, 1), "pos_overshoot": round(pos_os, 3), "pos_overshoot_px": round(pos_px, 1),
            "entering": F[4] >= 0.5, "ends_on_edge": edge, "end_box": F[:4], "start_opacity": b0[4], "end_opacity": F[4]}


def end_state(run):
    """End state of the changed elements: the last seeked sample (every animation at its end) when the run was seeked.
    The post-finish measurement can include later JavaScript-timed changes (a label swapped back by a timer), which the
    seeked timeline does not drive, so it is used only for real-time runs."""
    if run.get("sweep"): return run["sweep"][-1]["roots"]
    return run.get("final") or []


def reduced_movement(run):
    """Largest movement (px) and scale deviation of any changed element under reduced motion, against its end state."""
    final = end_state(run)
    if not final: return None
    if run.get("sweep"): series = [s["roots"] for s in run["sweep"]]
    else: series = [[c["box"] + [c["opacity"]] for c in f["changed"]] for f in run.get("frames", [])]
    move, scale = 0.0, 0.0
    for roots in series:
        for k, b in enumerate(roots):
            if k >= len(final): continue
            F = final[k]
            if F[2] <= 0 or F[3] <= 0 or b[2] <= 0 or b[3] <= 0: continue
            move = max(move, math.hypot(*(a - c for a, c in zip(_center(b), _center(F)))))
            scale = max(scale, abs(b[2] / F[2] - 1), abs(b[3] / F[3] - 1))
    return {"move_px": round(move, 1), "scale_dev": round(scale, 3)}


def trigger_summary(trig, cfg):
    """Everything the motion detector measured for one trigger (also used by evals/testset reports)."""
    out = {"name": trig["name"], "kind": trig["kind"], "selector": trig["selector"]}
    n = trig["runs"].get("normal") or {}
    out["normal_status"] = n.get("status", "missing") + (f" ({n['reason']})" if n.get("reason") else "")
    if n.get("status") == "ok":
        out["timing"] = n.get("timing")
        roots = n.get("changed") or []
        if n.get("sweep"):
            ms = [(r, root_metrics(n["sweep"], k, end_state(n), cfg)) for k, r in enumerate(roots)]
            out["roots"] = [dict(selector=r["selector"], **m) for r, m in ms if m]
        anims = [a for a in n.get("animations", []) if a.get("root", -1) >= 0 and a.get("iterations") != "infinite"]
        out["easings"] = sorted({a["easing"] for a in anims})
        out["anim_end_ms"] = max([a["endMs"] or 0 for a in anims], default=0)
        out["layout_moved"] = n.get("layoutMovedCount", 0)
        out["layout_top"] = (n.get("layoutMoved") or [None])[0]
    r = trig["runs"].get("reduce") or {}
    out["reduce_status"] = r.get("status", "missing") + (f" ({r['reason']})" if r.get("reason") else "")
    if r.get("status") == "ok":
        out["reduce"] = reduced_movement(r) or {"move_px": 0.0, "scale_dev": 0.0}
        out["reduce_timing"] = r.get("timing")
    return out


@detector("motion", needs=("motion.json",))
def motion(ev, cfg):
    m = _interaction(ev, "motion", "motion.json")
    trigs = m.get("triggers") or []
    if not trigs:
        if m.get("notVerified"): raise NotVerified("; ".join(m["notVerified"]))
        raise Skip("no transition triggers (dialogs, menus, tabs, disclosures, buttons) on the page")
    out = Hits()
    out.partial += m.get("notVerified", [])
    out.partial += [f"{s.get('name') or s.get('selector')}: {s['reason']}" for s in m.get("skipped", [])]
    measured = 0
    for t in trigs:
        S = trigger_summary(t, cfg)
        w = f"{t['kind']} trigger \"{t['name'][:40]}\" ({t['selector'][-60:]})"
        for mode in ("normal", "reduce"):
            st = (t["runs"].get(mode) or {}).get("status")
            if st != "ok": out.partial.append(f"{w} [{mode}]: {S[mode + '_status']}")
        if S["normal_status"] == "ok": measured += 1
        roots = S.get("roots") or []
        lim = cfg["max_ms"].get(t["kind"], max(cfg["max_ms"].values()))
        if roots:
            dur = max(r["duration_ms"] for r in roots)
            if dur > lim:
                out.append(hit(cfg, w, f"transition runs {dur} ms (measured from frames; limit for a {t['kind']} {lim} ms)", value=dur, check="duration"))
            ent = [r for r in roots if r["entering"] and min(r["end_box"][2], r["end_box"][3]) >= cfg["min_root_px"]]
            low = min(ent, key=lambda r: r["start_scale"], default=None)
            if low and 0 < low["start_scale"] < cfg["min_enter_scale"]:
                out.append(hit(cfg, f"{w} -> {low['selector'][-50:]}", f"enters from {low['start_scale']:.2f} scale (minimum {cfg['min_enter_scale']}): the element pops in from far instead of settling",
                               value=low["start_scale"], check="enter_scale", after="Start at 0.96-0.97 scale"))
            far = max((r for r in roots if not r["ends_on_edge"]), key=lambda r: r["travel_px"], default=None)
            if far and far["travel_px"] > cfg["max_travel_px"]:
                out.append(hit(cfg, f"{w} -> {far['selector'][-50:]}", f"moves {far['travel_px']:.0f} px during the transition (limit {cfg['max_travel_px']} px for in-place UI)",
                               value=far["travel_px"], check="travel", after="Travel 6-8 px"))
            os_ = max(roots, key=lambda r: max(r["size_overshoot"], r["pos_overshoot"]))
            ratio = max(os_["size_overshoot"], os_["pos_overshoot"])
            px = os_["size_overshoot_px"] if os_["size_overshoot"] >= os_["pos_overshoot"] else os_["pos_overshoot_px"]
            if ratio > cfg["max_overshoot"] and px >= cfg["min_overshoot_px"]:
                out.append(hit(cfg, f"{w} -> {os_['selector'][-50:]}", f"overshoots its end state: {ratio:.3f} of final ({px:.0f} px past, limit {cfg['max_overshoot']})",
                               value=round(ratio, 3), check="overshoot", after="Use a non-overshoot curve such as cubic-bezier(0.22, 1, 0.36, 1)"))
        n = t["runs"].get("normal") or {}
        moving_anims = [a for a in n.get("animations", []) if a.get("root", -1) >= 0 and a.get("iterations") != "infinite"]
        bad = sorted({a["easing"] for a in moving_anims if a["easing"] in cfg["banned_easing"]})
        lin = cfg.get("linear_movement") and any(a["easing"] == "linear" and any(re.match(r"transform|translate|scale|rotate|top|left", p) for p in a["props"]) for a in moving_anims)
        if roots and (bad or lin):
            what = ", ".join(bad + (["linear on movement"] if lin else []))
            out.append(hit(cfg, w, f"transition easing is {what} (read from the running animations)", tier="Finish", check="easing",
                           after="cubic-bezier(0.22, 1, 0.36, 1) on enter, a shorter ease-in on exit"))
        if S.get("layout_moved", 0) and S["layout_top"] and S["layout_top"]["midPx"] > cfg["layout_px"]:
            L = S["layout_top"]
            out.append(hit(cfg, w, f"{S['layout_moved']} other element(s) move while the transition runs (e.g. \"{L['name'][:30]}\" {L['midPx']:.0f} px off its start and end at {L['atMs']} ms): the transition animates layout",
                           value=S["layout_moved"], check="layout", after="Animate transform/opacity, or reserve the space; let content reflow once"))
        red = S.get("reduce")
        if red and (red["move_px"] > cfg["reduced_move_px"] or red["scale_dev"] > cfg["reduced_scale"]):
            out.append(hit(cfg, w, f"with prefers-reduced-motion: reduce the transition still moves {red['move_px']:.0f} px / scales {red['scale_dev']*100:.0f}% (frames {S.get('reduce_timing')})",
                           tier="Floor", rule=cfg["reduced_rule"], value=red, check="reduced_motion",
                           after="Under prefers-reduced-motion: reduce, keep only opacity (or nothing)"))
    if not measured and not out: raise NotVerified("no trigger could be measured: " + "; ".join(out.partial[:4]))
    return out


# ------------------------------------------------------------------------------------------------ async
def changed_pixels(ev, a, b, level):
    import numpy as np
    try: x, y = ev.img(a).astype("int16"), ev.img(b).astype("int16")
    except NotVerified: return None
    if x.shape != y.shape: return None
    return int((np.abs(x - y).max(axis=2) > level).sum())


TRIG_KEYS = ("disabled", "ariaDisabled", "ariaBusy", "text", "opacity", "cls", "cursor", "bg")


def _success_lines(lines, cfg):
    ok, honest = re.compile(cfg["success_pattern"], re.I), re.compile(cfg["honest_pattern"], re.I)
    return [l for l in lines if len(l) <= cfg["max_success_chars"] and ok.search(l) and not honest.search(l)]


def action_summary(ev, act, cfg):
    """Measured states for one action: pending feedback, success timing, spinner after completion, per run."""
    res = {"name": act["name"], "selector": act["selector"], "kind": act["kind"]}
    for mode, run in act["runs"].items():
        r = {"status": run.get("status") + (f" ({run['reason']})" if run.get("reason") else "")}
        res[mode] = r
        if run.get("status") != "ok": continue
        reqs = run.get("requests") or []
        same = [q for q in reqs if q.get("outcome") and not q["outcome"].startswith("blocked")]
        r["requests"] = [f"{q['method']} {q['url'][-40:]} {q.get('outcome')} {q.get('startMs')}-{q.get('endMs')} ms" for q in reqs]
        r["blocked"] = [q for q in reqs if (q.get("outcome") or "").startswith("blocked")]
        ends = [q["endMs"] for q in same if q.get("endMs") is not None]
        r["completion_ms"] = run.get("completionMs")
        before = run["before"]["state"]
        samples = {s["label"]: s for s in run.get("samples", [])}
        fb = {}
        for label, at in (("0.5s", 500), ("2s", 2000)):
            s = samples.get(label)
            if not s: fb[label] = None; continue
            st = s["state"]
            trig_changed = [k for k in TRIG_KEYS if (before["trigger"] or {}).get(k) != (st["trigger"] or {}).get(k)]
            px = changed_pixels(ev, run["before"]["shot"], s["shot"], cfg["pixel_level"])
            pending = any(q.get("startMs") is not None and q["startMs"] <= at and (q.get("endMs") is None or q["endMs"] > at) for q in same)
            fb[label] = {"pending": pending, "new_text": st["newLines"][:3], "gone_text": st["goneLines"][:3], "trigger_changed": trig_changed,
                         "busy": st["newBusy"][:2], "spinners": st["newSpinners"][:2], "changed_px": px,
                         "responded": bool(st["newLines"] or st["goneLines"] or trig_changed or st["newBusy"] or st["newSpinners"] or (px is not None and px >= cfg["min_changed_px"]))}
        r["feedback"] = fb
        tl = run.get("timeline") or []
        first_success = next(((e["tMs"], _success_lines(e["newLines"], cfg)) for e in tl if _success_lines(e["newLines"], cfg)), None)
        r["first_success"] = first_success
        r["first_answer_ms"] = min(ends) if ends else None
        fin = samples.get("final")
        if fin:
            st = fin["state"]
            r["final_new_text"] = st["newLines"][:4]; r["final_gone_text"] = st["goneLines"][:4]
            r["final_success"] = _success_lines(st["newLines"], cfg)
            r["final_spinners"] = st["newSpinners"]; r["final_busy"] = st["newBusy"] + (["trigger aria-busy"] if (st["trigger"] or {}).get("ariaBusy") == "true" else [])
        r["trigger_timeline"] = [(e["tMs"], (e.get("trigger") or {}).get("cls"), (e.get("trigger") or {}).get("opacity")) for e in run.get("triggerTimeline") or []][:6]
        r["same_origin_requests"] = len(same)
    return res


@detector("async_state", needs=("async.json",))
def async_state(ev, cfg):
    a = _interaction(ev, "async", "async.json")
    acts = a.get("actions") or []
    if not acts:
        if a.get("notVerified"): raise NotVerified("; ".join(a["notVerified"]))
        raise Skip("no primary actions (form submits, action buttons) on the page")
    out = Hits()
    out.partial += a.get("notVerified", []) + [f"{s.get('name')}: {s['reason']}" for s in a.get("skipped", [])]
    fs_rule = cfg["false_success_rule"]
    measured = 0
    for act in acts:
        S = action_summary(ev, act, cfg)
        w = f"{act['kind']} \"{act['name'][:40]}\" ({act['selector'][-60:]})"
        for mode in ("slow", "fail"):
            r = S.get(mode) or {}
            st = r.get("status", "missing")
            if not st.startswith("ok"):
                if not st.startswith("skipped (the slow run made no"): out.partial.append(f"{w} [{mode}]: {st}")
                continue
            measured += 1
            if r["blocked"] and not r["same_origin_requests"]:
                out.partial.append(f"{w} [{mode}]: only cross-origin requests, refused by the capture; result not verified"); continue
            fb = r["feedback"]
            if mode == "slow" and r["same_origin_requests"] and all(fb.get(l) and fb[l]["pending"] and not fb[l]["responded"] for l in ("0.5s", "2s")):
                px = [fb[l]["changed_px"] for l in ("0.5s", "2s")]
                out.append(hit(cfg, w, f"no feedback while the request is pending: nothing changed at 0.5 s or 2 s (no text, busy state, spinner or trigger change; {px[0]} and {px[1]} px differ)",
                               check="no_feedback", value=px, after="Show a busy label or inline spinner with aria-busy within ~150 ms"))
            fsu = r["first_success"]
            if mode == "slow" and fsu and r["same_origin_requests"] and (r["first_answer_ms"] is None or fsu[0] < r["first_answer_ms"]):
                out.append(hit(cfg, w, f"shows \"{fsu[1][0][:60]}\" at {fsu[0]} ms, before the request answered ({r['first_answer_ms']} ms)", tier="Floor", rule=fs_rule,
                               check="false_success_early", value=fsu[0], after="Show success only from the server's answer"))
            if mode == "slow" and not r["requests"] and r.get("final_success"):
                others = [l for l in r.get("final_new_text", []) + r.get("final_gone_text", []) if l not in r["final_success"]]
                if not others:
                    t = f" at {fsu[0]} ms" if fsu else ""
                    out.append(hit(cfg, w, f"says \"{r['final_success'][0][:60]}\"{t} but made no request and nothing else on the page changed", tier="Floor", rule=fs_rule,
                                   check="false_success_no_request", after="Do the work, or say it is not connected yet"))
            if mode == "fail" and (r.get("final_success") or fsu):
                line = (r.get("final_success") or fsu[1])[0]
                out.append(hit(cfg, w, f"shows \"{line[:60]}\" although the request failed (forced HTTP 500)", tier="Floor", rule=fs_rule,
                               check="false_success_failed", after="On failure keep the input and say what went wrong, with a retry"))
            done = r["completion_ms"] is not None
            if done and (r.get("final_spinners") or r.get("final_busy")):
                what = (r.get("final_spinners") or r.get("final_busy"))[0]
                out.append(hit(cfg, w, f"progress state still showing 1 s after the request {'failed' if mode == 'fail' else 'completed'} ({r['completion_ms']} ms): {what[-60:]}",
                               check="stuck_spinner", after="Clear the spinner and aria-busy when the answer arrives, success or failure"))
    if not measured: raise NotVerified("no action could be measured: " + "; ".join(out.partial[:4]))
    seen, res = set(), Hits()
    res.partial = out.partial
    for h in out:
        k = (h["where"], h.get("check"))
        if k not in seen: seen.add(k); res.append(h)
    return res
