#!/usr/bin/env python3
"""Unslop sweep: run every mechanical detector over a capture and write 02-mechanical.json.

usage: sweep.py <run-dir> [--profile balanced] [--medium web] [--only det1,det2]
Every detector in data/thresholds.yaml gets a status: ran | skipped: reason | not-verified: reason.
"""
import argparse, json, sys, time, traceback, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from core import REGISTRY, Evidence, Skip, NotVerified, resolve
import detectors_visual, detectors_text, detectors_a11y, detectors_cross   # noqa: F401  (register)

ORDER_LAST = ["look_family"]          # needs other detectors' results

def run(run_dir, profile="balanced", medium="web", only=None, overrides=None):
    ev = Evidence(run_dir)
    rj = ev.run / "run.json"
    if overrides is None and rj.exists(): overrides = json.loads(rj.read_text()).get("overrides")
    cfg = resolve(profile, medium, overrides)
    (ev.run / "resolved-thresholds.json").write_text(json.dumps(cfg["detectors"], indent=1))
    control_ok = bool((ev.manifest.get("control") or {}).get("ok"))
    names = [n for n in cfg["detectors"] if not only or n in only]
    names.sort(key=lambda n: n in ORDER_LAST)
    results = {}
    for name in names:
        c = dict(cfg["detectors"][name]); c["_profile"] = cfg["profile"]
        if c.get("enabled") is False: results[name] = {"status": "skipped: disabled by profile", "rule": c["rule"]}; continue
        impl = REGISTRY.get(name)
        if not impl: results[name] = {"status": "not-verified: detector not implemented yet", "rule": c["rule"]}; continue
        t0 = time.time()
        try:
            hits = impl["fn"](ev, c, results) if name in ORDER_LAST else impl["fn"](ev, c)
            for h in hits:
                h.setdefault("source", "sweep"); h["detector"] = name
                if c.get("severity") == "info": h["tier"] = "info"
            status = "ran" if control_ok or name in ("near_blank",) else "not-verified: control render failed"
            results[name] = {"status": status, "rule": c["rule"], "hits": hits, "ms": round(1000 * (time.time() - t0))}
        except Skip as e: results[name] = {"status": f"skipped: {e}", "rule": c["rule"]}
        except NotVerified as e: results[name] = {"status": f"not-verified: {e}", "rule": c["rule"]}
        except Exception as e:
            results[name] = {"status": f"not-verified: detector error {type(e).__name__}: {e}", "rule": c["rule"], "trace": traceback.format_exc(limit=3)}
    summary = {"profile": profile, "medium": medium, "control_ok": control_ok, "widths": ev.widths,
               "counts": {t: sum(1 for r in results.values() if r["status"] == "ran" for h in r.get("hits", []) if h["tier"] == t) for t in ("Floor", "Reflex", "Finish")},
               "ran": sum(1 for r in results.values() if r["status"] == "ran"),
               "skipped": [f"{n}: {r['status']}" for n, r in results.items() if r["status"] != "ran"]}
    out = {"summary": summary, "detectors": results}
    (ev.run / "02-mechanical.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir"); ap.add_argument("--profile", default="balanced"); ap.add_argument("--medium", default="web")
    ap.add_argument("--only"); ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    out = run(a.run_dir, a.profile, a.medium, set(a.only.split(",")) if a.only else None)
    s = out["summary"]
    print(f"sweep {a.run_dir}: {s['ran']} detectors ran; Floor {s['counts']['Floor']}, Reflex {s['counts']['Reflex']}, Finish {s['counts']['Finish']}; control {'ok' if s['control_ok'] else 'FAILED'}")
    if not a.quiet:
        for n, r in out["detectors"].items():
            hits = r.get("hits", [])
            mark = f"{len(hits)} hit(s)" if r["status"] == "ran" else r["status"]
            print(f"  {n:22s} {r['rule']:8s} {mark}")
            for h in hits[:3]: print(f"      [{h['tier']}] {h['where'][:60]} :: {h['evidence'][:110]}")
