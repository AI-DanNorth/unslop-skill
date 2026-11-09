#!/usr/bin/env python3
"""Score a controlled-pair test set (set2.yaml): does each bad half come out worse than its good half?

usage: calibrate_pairs.py <set.yaml> <runs-dir> [--lens concept,color,...] [--out report.md]

Items carry `pair` (the lesson) and `half` (bad / good). Lessons with no good half of their own (Stageshow's style pairs
share one good card) are compared with the good half of the same group. For each pair it reports:
- mechanical: hits by tier on each half, a weighted score (Floor 5, Reflex 2, Finish 1), and the detectors that fire
  only on the bad half (the ones that see the fault) or only on the good half (noise the pair exposes);
- lenses (when 03-lenses/<lens>.json exists on both halves): the score value on each half.
A pair "separates" when the bad half's weighted mechanical score is higher, or its lens score lower.
"""
import argparse, json, pathlib, collections
import yaml

W = {"Floor": 5, "Reflex": 2, "Finish": 1}
ap = argparse.ArgumentParser(); ap.add_argument("manifest"); ap.add_argument("runs"); ap.add_argument("--lens", default=""); ap.add_argument("--out")
a = ap.parse_args()
doc = yaml.safe_load(open(a.manifest, encoding="utf-8")); runs = pathlib.Path(a.runs)
lenses = [x for x in a.lens.split(",") if x]


def mech(iid):
    p = runs / iid / "02-mechanical.json"
    if not p.exists(): return None
    d = json.loads(p.read_text(encoding="utf-8"))
    det = collections.Counter(); tiers = collections.Counter()
    for name, r in d["detectors"].items():
        for h in r.get("hits", []):
            det[name] += 1; tiers[h.get("tier", "?")] += 1
    return {"tiers": tiers, "det": det, "score": sum(W.get(t, 0) * n for t, n in tiers.items())}


def lens_score(iid, lens):
    p = runs / iid / "03-lenses" / f"{lens}.json"
    if not p.exists(): return None
    return ((json.loads(p.read_text(encoding="utf-8")).get("score") or {}).get("value"))


items = doc["items"]
by_pair = collections.defaultdict(dict)
for it in items: by_pair[it["pair"]][it["half"]] = it
group_good = {}
for it in items:
    if it["half"] == "good": group_good.setdefault(it["group"], it)

rows, det_bad, det_good = [], collections.Counter(), collections.Counter()
for pair, halves in by_pair.items():
    bad = halves.get("bad")
    if not bad: continue
    good = halves.get("good") or group_good.get(bad["group"])
    mb, mg = mech(bad["id"]), mech(good["id"]) if good else None
    if not mb or not mg: rows.append(dict(pair=pair, group=bad["group"], expect=bad["expect"], fault=bad["why"], missing=True)); continue
    only_bad = sorted(set(mb["det"]) - set(mg["det"])); only_good = sorted(set(mg["det"]) - set(mb["det"]))
    det_bad.update(only_bad); det_good.update(only_good)
    ls = {l: (lens_score(bad["id"], l), lens_score(good["id"], l)) for l in lenses}
    rows.append(dict(pair=pair, group=bad["group"], expect=bad["expect"], fault=bad["why"].replace("bad half: ", ""), bad=bad["id"], good=good["id"],
                     sb=mb["score"], sg=mg["score"], tb=mb["tiers"], tg=mg["tiers"], only_bad=only_bad, only_good=only_good, lens=ls))

done = [r for r in rows if not r.get("missing")]
sep = sum(r["sb"] > r["sg"] for r in done); tie = sum(r["sb"] == r["sg"] for r in done)
L = [f"# Pair calibration: {doc['name']}", "",
     f"Pairs scored: {len(done)} of {len(rows)}. Mechanical sweep separates (bad half scores worse) on **{sep}/{len(done)}**, ties on {tie}, "
     f"inverts on {len(done) - sep - tie}. Weighted score: Floor 5, Reflex 2, Finish 1.", ""]
for g in sorted({r["group"] for r in done}):
    gr = [r for r in done if r["group"] == g]
    L.append(f"- {g}: separates {sum(r['sb'] > r['sg'] for r in gr)}/{len(gr)}")
for l in lenses:
    lr = [r for r in done if None not in r["lens"][l]]
    if lr: L.append(f"- lens-{l}: bad half scores lower on {sum(r['lens'][l][0] < r['lens'][l][1] for r in lr)}/{len(lr)} (ties {sum(r['lens'][l][0] == r['lens'][l][1] for r in lr)})")
L += ["", "| Pair | Group | Expect | Fault (bad half) | Bad/good items | Score bad vs good | Detectors only on bad | Only on good |" + "".join(f" {l} bad/good |" for l in lenses),
      "|---|---|---|---|---|---|---|---|" + "---|" * len(lenses)]
for r in sorted(rows, key=lambda r: (r["group"], r["pair"])):
    if r.get("missing"): L.append(f"| {r['pair']} | {r['group']} | {r['expect']} | {r['fault']} | not captured | | | |" + " |" * len(lenses)); continue
    mark = "" if r["sb"] > r["sg"] else (" =" if r["sb"] == r["sg"] else " ✗")
    L.append(f"| {r['pair']} | {r['group']} | {r['expect']} | {r['fault']} | {r['bad']}/{r['good']} | {r['sb']} vs {r['sg']}{mark} | {', '.join(r['only_bad']) or '-'} | {', '.join(r['only_good']) or '-'} |"
             + "".join(f" {r['lens'][l][0]}/{r['lens'][l][1]} |" for l in lenses))
L += ["", "Detectors that fire only on bad halves (how many pairs): " + (", ".join(f"{d} {n}" for d, n in det_bad.most_common()) or "none"),
      "", "Detectors that fire only on good halves (noise the pairs expose): " + (", ".join(f"{d} {n}" for d, n in det_good.most_common()) or "none"), ""]
out = "\n".join(L) + "\n"
if a.out: pathlib.Path(a.out).write_text(out, encoding="utf-8")
print(out)
