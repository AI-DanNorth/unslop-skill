#!/usr/bin/env python3
"""Run capture + sweep + synthesize over every page item in a test-set manifest, one at a time.
usage: run_set.py set1.yaml <refs-dir> <runs-dir> [--profile balanced] [--only S01,S02]"""
import sys, yaml, json, subprocess, pathlib, time, argparse
ROOT = pathlib.Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser(); ap.add_argument("manifest"); ap.add_argument("refs"); ap.add_argument("runs")
ap.add_argument("--profile", default="balanced"); ap.add_argument("--only"); a = ap.parse_args()
HOSTS = {"transitions.dev": "transitions-dev"}       # live sites whose files are in the repo clone
doc = yaml.safe_load(open(a.manifest, encoding="utf-8")); runs = pathlib.Path(a.runs); runs.mkdir(parents=True, exist_ok=True)
only = set(a.only.split(",")) if a.only else None
for it in doc["items"]:
    it.setdefault("kind", "page"); it.setdefault("repo", "live"); it.setdefault("path", it.get("url", "")); it.setdefault("commit", None)
    if it["kind"] != "page" or (only and it["id"] not in only): continue
    run = runs / it["id"]
    if (run / "04-findings.json").exists() and not only: print(it["id"], "done already"); continue
    run.mkdir(exist_ok=True)
    shown = "(withheld for blind review)" if it.get("withhold_target") else it["path"]
    (run / "run.json").write_text(json.dumps({"target": shown, "profile": a.profile, "workflow": "testset", "medium": it["medium"],
        "item": {k: (shown if k == "path" else it[k]) for k in ("id", "repo", "path", "medium", "commit")}}, indent=1))   # no expected label: lenses review blind
    target = it["url"] if it.get("url") else str(pathlib.Path(a.refs) / it["repo"] / it["path"])
    medium = it["medium"]
    adapter = ROOT / f"skills/media-{medium}/thresholds.yaml"
    widths = ",".join(map(str, (yaml.safe_load(adapter.read_text()) or {}).get("capture_widths", [375, 1280, 1440]))) if adapter.exists() else "375,1280,1440"
    env = dict(__import__("os").environ, UNSLOP_HOST_MAP=",".join(f"{h}={pathlib.Path(a.refs) / r}" for h, r in HOSTS.items()))
    t0 = time.time()
    extra = list(it.get("capture_flags") or []) + (["--withhold-target"] if it.get("withhold_target") else []) + (["--isolate", json.dumps(it["isolate"])] if it.get("isolate") else [])
    c = subprocess.run(["node", str(ROOT / "scripts/capture/capture.mjs"), target, str(run), "--widths", it.get("widths") or widths, *extra], capture_output=True, text=True, timeout=900, env=env)
    if c.returncode: print(it["id"], "CAPTURE FAILED", c.stderr[-300:]); continue
    subprocess.run([sys.executable, str(ROOT / "scripts/checks/sweep.py"), str(run), "--profile", a.profile, "--medium", medium, "--quiet"], capture_output=True, text=True)
    s = subprocess.run([sys.executable, str(ROOT / "scripts/report/synthesize.py"), str(run)], capture_output=True, text=True)
    m = json.loads((run / "02-mechanical.json").read_text())["summary"]
    print(f"{it['id']} [{it['expect']:10s}] {time.time()-t0:4.0f}s  Floor {m['counts']['Floor']:3d} Reflex {m['counts']['Reflex']:3d} Finish {m['counts']['Finish']:2d}  {s.stdout.strip()[:90]}", flush=True)
