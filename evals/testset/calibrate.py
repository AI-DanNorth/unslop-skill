#!/usr/bin/env python3
"""Score a test-set run: expected label vs what Unslop concluded, plus per-detector discrimination.

usage: calibrate.py set1.yaml <runs-dir> [--out report.md]
Reads 02-mechanical.json and 03-lenses/*.json per item. Expected labels live only in the manifest,
never in the run directories, so lenses review blind.
"""
import sys, json, yaml, pathlib, collections, argparse
ap = argparse.ArgumentParser(); ap.add_argument("manifest"); ap.add_argument("runs"); ap.add_argument("--out")
a = ap.parse_args()
doc = yaml.safe_load(open(a.manifest)); runs = pathlib.Path(a.runs)
SLOP_DOMAINS = ("SLP", "CPY", "INT", "CON", "CLR", "TYP")

def load(p):
    try: return json.loads(p.read_text())
    except Exception: return None

rows, det_fire = [], collections.defaultdict(lambda: collections.Counter())
for it in doc["items"]:
    run = runs / it["id"]
    mech = load(run / "02-mechanical.json")
    lenses = {f.stem: load(f) for f in sorted((run / "03-lenses").glob("*.json"))} if (run / "03-lenses").exists() else {}
    fams, slop_reflex, floor, fired = [], 0, 0, []
    if mech:
        for det, r in mech["detectors"].items():
            hits = r.get("hits", []) if r["status"] == "ran" else []
            if hits: fired.append(det)
            det_fire[det][it["expect"]] += bool(hits)
            for h in hits:
                if det == "look_family": fams.append(h.get("family"))
                if h["tier"] == "Reflex" and h["rule"].split("-")[0] in SLOP_DOMAINS: slop_reflex += 1
                if h["tier"] == "Floor": floor += 1
    det_fire["_items"][it["expect"]] += 1 if mech else 0
    sl = lenses.get("slop") or {}
    read = sl.get("overall_read")
    lens_findings = sum(len((l or {}).get("findings", [])) for l in lenses.values())
    if read == "generated" or (fams and read != "made"): pred = "slop"
    elif read == "made" and not fams: pred = "good"
    elif read is None and not mech: pred = "not run"
    elif read is None: pred = "slop" if fams else "good (mechanical only)"
    else: pred = "borderline"
    exp = it["expect"]
    agree = (exp == pred) or (exp == "borderline" and pred in ("borderline", "slop", "good")) or (exp == "good" and pred.startswith("good"))
    rows.append(dict(id=it["id"], expect=exp, pred=pred, agree=agree, read=read, conf=sl.get("confidence"), families=",".join(f for f in fams if f),
                     slop_reflex=slop_reflex, floor=floor, lens_findings=lens_findings, medium=it["medium"], group=it["group"], why=it["why"]))

L = ["# Calibration: " + doc["name"], ""]
scored = [r for r in rows if r["expect"] in ("slop", "good") and r["pred"] != "not run"]
ok = sum(r["agree"] for r in scored)
L.append(f"Verdict agreement on clear-cut items: **{ok}/{len(scored)}**. Borderline items are reported but not scored.")
fp = [r for r in scored if r["expect"] == "good" and r["pred"] == "slop"]
fn = [r for r in scored if r["expect"] == "slop" and not r["pred"].startswith("slop")]
L.append(f"False positives (good flagged as slop): {len(fp)}. Misses (slop not flagged): {len(fn)}.")
L += ["", "| Item | Expected | Unslop | Slop lens read | Look families | Slop-type Reflex | Floor | Lens findings | Medium |", "|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    mark = "" if r["agree"] or r["expect"] == "borderline" else " ✗"
    L.append(f"| {r['id']} | {r['expect']} | {r['pred']}{mark} | {r['read'] or '-'}{' (%s)' % r['conf'] if r['conf'] else ''} | {r['families'] or '-'} | {r['slop_reflex']} | {r['floor']} | {r['lens_findings']} | {r['medium']} |")
L += ["", "## Detector discrimination", "", "Share of items each detector fired on, by expected label. A detector that fires as often on good items as on slop does not separate them; one that fires on good controls is a false-positive candidate.", "",
      "| Detector | slop | borderline | good | Read |", "|---|---|---|---|---|"]
n = det_fire.pop("_items")
for det, c in sorted(det_fire.items(), key=lambda kv: -(kv[1]["slop"] / max(1, n["slop"]) - kv[1]["good"] / max(1, n["good"]))):
    s, b, g = (c[k] / max(1, n[k]) for k in ("slop", "borderline", "good"))
    if s == b == g == 0: continue
    note = "separates" if s - g >= 0.3 else ("fires on good too" if g >= 0.3 and s - g < 0.15 else ("rare" if s < 0.2 else ""))
    L.append(f"| {det} | {s:.0%} | {b:.0%} | {g:.0%} | {note} |")
out = "\n".join(L) + "\n"
if a.out: pathlib.Path(a.out).write_text(out)
print(out)
