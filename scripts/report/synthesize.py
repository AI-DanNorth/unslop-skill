#!/usr/bin/env python3
"""Merge sweep and lens findings into 04-findings.json and a draft 04-report.md.

usage: synthesize.py <run-dir>
The synthesize skill then edits the draft: it writes the four-line read, the Keep list, and the
judgment scores. This script never invents judgment; it fills only what the evidence supports.
"""
import json, pathlib, sys, collections, re
import yaml
ROOT = pathlib.Path(__file__).resolve().parents[2]
TIER_RANK = {"Floor": 0, "Reflex": 1, "Finish": 2}
DIM_OF_DOMAIN = {"D10": "Accessibility", "D18": "Integrity", "D03": "Distinctiveness", "D02": "Concept", "D05": "Craft", "D06": "Craft",
                 "D07": "Hierarchy", "D04": "Craft", "D08": "Usability", "D09": "Craft", "D11": "Craft", "D12": "Craft", "D13": "Craft",
                 "D15": "Usability", "D14": "Craft", "D17": "Craft", "D19": "Distinctiveness", "D20": "Concept"}

def cards():
    out = {}
    for f in (ROOT / "rules").glob("[A-Z]*.yaml"):
        for c in yaml.safe_load(f.read_text(encoding="utf-8")) or []: out[c["id"]] = c
    return out

def quality(f):
    """0..1 average of specificity, actionability, grounding, evidence (agent-skills quality floor)."""
    spec = 1.0 if re.search(r"[#.>\[]|px|screen|form|page|<", f.get("where", "")) else 0.5
    act = 1.0 if f.get("after") or f.get("fix") else 0.6
    ground = 1.0 if f.get("value") is not None or re.search(r"\d", f.get("evidence", "")) or '"' in f.get("evidence", "") else 0.5
    evid = 0.0 if str(f.get("evidence", "")).startswith("not verified") else 1.0
    return round((spec + act + ground + evid) / 4, 2)

def main(run):
    run = pathlib.Path(run); C = cards()
    mech = json.loads((run / "02-mechanical.json").read_text(encoding="utf-8"))
    findings, not_inv = [], []
    for det, r in mech["detectors"].items():
        if r["status"] != "ran": not_inv.append(f"{det} ({r['rule']}): {r['status']}"); continue
        for h in r.get("hits", []): findings.append(dict(h))
    net = json.loads((run / "01-evidence/manifest.json").read_text(encoding="utf-8")).get("network") or {}
    if net.get("blockedImages"): not_inv.append(f"capture: {net['blockedImages']} image(s) could not load (network blocked); imagery and layout around them not verified")
    if net.get("fontsMissing"): not_inv.append(f"capture: fonts unavailable offline: {', '.join(net['fontsMissing'])}; type findings for them not verified")
    other = [b for b in net.get("blocked", []) if not b.startswith("image ")]
    if other: not_inv.append(f"capture: {len(other)} other request(s) blocked, e.g. {other[0][:90]}")
    lens_dir = run / "03-lenses"
    lens_scores = collections.defaultdict(list)          # dimension -> [(value, lens, reason)]
    if lens_dir.exists():
        for f in sorted(lens_dir.glob("*.json")):
            data = json.loads(f.read_text(encoding="utf-8"))
            for h in data.get("findings", []): h.setdefault("source", f.stem); findings.append(h)
            for n in data.get("not_investigated", []): not_inv.append(f"{f.stem}: {n}")
            sc = data.get("score") or {}
            if sc.get("dimension") and isinstance(sc.get("value"), (int, float)):
                lens_scores[sc["dimension"]].append((sc["value"], f.stem, sc.get("reason", "")))
    for f in findings:
        c = C.get(f["rule"], {})
        f.setdefault("title", c.get("title", f["rule"])); f.setdefault("remedy", c.get("remedy")); f.setdefault("fix", c.get("fix"))
        f.setdefault("priority", {"Floor": "P0", "Reflex": "P1", "Finish": "P3"}.get(f["tier"], "P2"))
        f["dimension"] = DIM_OF_DOMAIN.get(c.get("domain", ""), "Craft")
        f["quality"] = quality(f)
    dropped = [f for f in findings if f["quality"] < 0.55]
    findings = [f for f in findings if f["quality"] >= 0.55]
    # merge to root causes: same rule -> one finding with instances
    groups = collections.OrderedDict()
    for f in findings: groups.setdefault((f["rule"], f["tier"]), []).append(f)
    merged = []
    for (rule, tier), lst in groups.items():
        head = dict(lst[0]); head["instances"] = len(lst)
        if len(lst) > 1: head["also"] = [x["where"] for x in lst[1:8]]
        merged.append(head)
    # within a tier: concept-level failures first (a generic first screen outranks every detail), then priority, then reach
    concept = lambda f: 0 if C.get(f["rule"], {}).get("domain") in ("D02", "D20") or f.get("test") in ("T-RIVAL-NAME", "T-MIRROR", "T-DEFAULT-AGENT", "T-SCREEN-BY-SCREEN") else 1
    merged.sort(key=lambda f: (TIER_RANK.get(f["tier"], 3), concept(f), f.get("priority", "P2"), -f["instances"]))
    open_floor = sum(1 for f in merged if f["tier"] == "Floor")
    verdict = "recapture" if not mech["summary"]["control_ok"] else ("fix" if open_floor or any(f["tier"] == "Reflex" for f in merged) else "ship")
    # mechanical part of the score: dimensions only where the sweep has evidence; judgment dims left for lenses
    dims = {d: None for d in ("Concept", "Hierarchy", "Craft", "Accessibility", "Usability", "Integrity", "Distinctiveness")}
    for d in ("Accessibility", "Integrity"):
        fl = sum(f["instances"] for f in merged if f["dimension"] == d and f["tier"] == "Floor")
        rf = sum(f["instances"] for f in merged if f["dimension"] == d and f["tier"] == "Reflex")
        dims[d] = max(1, 10 - 2 * fl - rf)
    # judgment dimensions from the lenses' own scores; several lenses on one dimension: the weakest one stands
    notes = {d: "from sweep" for d, v in dims.items() if v is not None}
    lens_dims = {}
    for d, vals in lens_scores.items():
        if d not in dims: continue
        v, lens, reason = min(vals)
        if dims[d] is not None:            # Accessibility, Integrity: computed from findings; a lower lens score still stands
            if v < dims[d]:
                notes[d] = f"lens-{lens} {v} below the findings-based {dims[d]}: {reason[:160]}"; dims[d] = v
            lens_dims[d] = [{"lens": l, "value": x} for x, l, _ in vals]
            continue
        dims[d] = v; lens_dims[d] = [{"lens": l, "value": x} for x, l, _ in vals]
        notes[d] = f"lens-{lens}" + (f" (lowest of {', '.join(f'{l} {x}' for x, l, _ in sorted(vals, key=lambda t: t[1]))})" if len(vals) > 1 else "") + f": {reason[:160]}"
    scored = [v for v in dims.values() if v is not None]
    overall, caps = None, []
    if dims["Concept"] is not None and len(scored) >= 5:
        overall = round(sum(scored) / len(scored), 1)
        if open_floor and overall > 4: overall, caps = 4, caps + ["open Floor caps at 4"]
        if dims["Concept"] <= 5 and overall > 6: overall, caps = 6, caps + ["Concept at 5 or below caps at 6"]
    if dims["Concept"] is not None and dims["Concept"] <= 5 and verdict == "fix": verdict = "rebuild"     # concept veto (core/report-format.md)
    out = {"verdict_draft": verdict, "open_floor": open_floor, "findings": merged, "dropped_below_quality_floor": len(dropped),
           "not_investigated": not_inv, "scores_mechanical": {d: v for d, v in dims.items() if notes.get(d) == "from sweep"},
           "scores": dims, "score_sources": notes, "lens_scores": lens_dims, "overall_draft": overall, "caps": caps, "profile": mech["summary"]["profile"]}
    (run / "04-findings.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    # draft report
    L = [f"# Unslop report: {json.loads((run / '01-evidence/manifest.json').read_text(encoding="utf-8"))['target']}", "",
         f"**Verdict (draft): {verdict}**. Profile: {out['profile']}. {open_floor} Floor finding(s) open." , "",
         "## Four-line read", "", "- **For:** _(synthesize writes this)_", "- **Works and stays:** _(synthesize)_", "- **Reads generated:** _(synthesize)_", "- **Broken:** _(synthesize)_", "",
         "## Score", "", "| Dimension | Score | Note |", "|---|---|---|"]
    for d, v in dims.items(): L.append(f"| {d} | {v if v is not None else '_lens_'} | {notes.get(d, 'judgment lens required')} |")
    L += ["", f"Overall (draft): **{overall}**" + (f" ({'; '.join(caps)})" if caps else "") if overall is not None else "Overall: _(needs Concept and at least five scored dimensions)_",
          "", "Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.", "", "## Findings", ""]
    for i, f in enumerate(merged[:15], 1):
        L.append(f"{i}. **[{f['tier']} {f['priority']}] {f['rule']} {f['title']}** ({f['instances']}x). {f['where']}  ")
        L.append(f"   Evidence: {f['evidence']}  ")
        if f.get("after") or f.get("fix"): L.append(f"   Fix: {f.get('after') or f.get('fix')} (remedy: {f.get('remedy')})")
    if len(merged) > 15: L.append(f"\n{len(merged) - 15} further findings are in 04-findings.json.")
    L += ["", "## Quick wins", "", "_(synthesize picks 3)_", "", "## Keep", "", "_(synthesize)_", "", "## Not investigated", ""]
    L += [f"- {n}" for n in not_inv] or ["- nothing"]
    (run / "04-report.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"synthesize: {len(merged)} findings ({open_floor} Floor), {len(dropped)} dropped below quality floor, verdict draft: {verdict}")

if __name__ == "__main__":
    main(sys.argv[1])
