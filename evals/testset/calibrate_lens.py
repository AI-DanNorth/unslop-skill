#!/usr/bin/env python3
"""Score phase-2 judgment lenses against a test-set manifest.

usage: calibrate_lens.py <set.yaml> <runs-dir> --lens concept[,structure,...] [--only ID,ID] [--out report.md]
Reads <runs>/<ID>/03-lenses/<lens>.json. A lens's overall_read maps to a verdict (made -> good, generated -> slop,
mixed -> borderline); its score.value is the dimension score. Reports verdict agreement on clear-cut items, the
mean score by expected label (does the lens separate good from slop?) and the finding counts by tier.
"""
import argparse, json, pathlib, statistics as st
import yaml

ap = argparse.ArgumentParser(); ap.add_argument("manifest"); ap.add_argument("runs")
ap.add_argument("--lens", required=True); ap.add_argument("--only"); ap.add_argument("--out")
a = ap.parse_args()
doc = yaml.safe_load(open(a.manifest, encoding="utf-8")); runs = pathlib.Path(a.runs)
only = set(a.only.split(",")) if a.only else None
VERDICT = {"made": "good", "generated": "slop", "mixed": "borderline"}
L = [f"# Lens calibration: {doc['name']}", ""]
for lens in a.lens.split(","):
    rows = []
    for it in doc["items"]:
        if only and it["id"] not in only: continue
        p = runs / it["id"] / "03-lenses" / f"{lens}.json"
        if not p.exists(): continue
        d = json.loads(p.read_text(encoding="utf-8"))
        sc = (d.get("score") or {}).get("value")
        tiers = {}
        for f in d.get("findings", []): tiers[f.get("tier", "?")] = tiers.get(f.get("tier", "?"), 0) + 1
        pred = VERDICT.get(d.get("overall_read"), "none")
        rows.append(dict(id=it["id"], expect=it["expect"], read=d.get("overall_read"), conf=d.get("confidence"), pred=pred,
                         score=sc, tiers=tiers, n=len(d.get("findings", [])), reason=(d.get("overall_reason") or "")[:140]))
    clear = [r for r in rows if r["expect"] in ("slop", "good")]
    ok = sum(r["pred"] == r["expect"] for r in clear)
    L += [f"## lens-{lens}", "", f"Verdict agreement on clear-cut items: **{ok}/{len(clear)}** (made = good, generated = slop, mixed = neither)."]
    for lab in ("slop", "borderline", "good"):
        s = [r["score"] for r in rows if r["expect"] == lab and isinstance(r["score"], (int, float))]
        if s: L.append(f"- Mean {lens} score on {lab} items: {st.mean(s):.1f} (n={len(s)}, range {min(s)}-{max(s)})")
    L += ["", "| Item | Expected | Read | Verdict | Score | Findings (Floor/Reflex/Finish) | Reason |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        mark = "" if r["expect"] == "borderline" or r["pred"] == r["expect"] else " ✗"
        t = r["tiers"]
        L.append(f"| {r['id']} | {r['expect']} | {r['read']} ({r['conf']}) | {r['pred']}{mark} | {r['score']} | {r['n']} ({t.get('Floor', 0)}/{t.get('Reflex', 0)}/{t.get('Finish', 0)}) | {r['reason']} |")
    L.append("")
out = "\n".join(L) + "\n"
if a.out: pathlib.Path(a.out).write_text(out, encoding="utf-8")
print(out)
