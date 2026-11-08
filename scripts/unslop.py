#!/usr/bin/env python3
"""Unslop runner: the scripted half of the pipeline. The judgment half (lenses, report prose) is done by the skills.

usage:
  unslop.py new <target> [--profile balanced] [--workflow full|quick|diff|redesign] [--medium web] [--root .unslop]
  unslop.py capture <run-dir> [--widths ...]
  unslop.py sweep <run-dir>
  unslop.py synthesize <run-dir>
  unslop.py gates <run-dir>                  # which phases are done, per core/gates.md
  unslop.py quick <target> [--profile ...]    # new + capture + sweep + synthesize in one go
  unslop.py selftest
"""
import argparse, json, pathlib, subprocess, sys, datetime, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
GATES = [(0, "intake", "00-contract.md"), (1, "capture", "01-evidence/manifest.json"), (2, "sweep", "02-mechanical.json"),
         (3, "lenses", "03-lenses"), (4, "synthesize", "04-report.md"), (5, "remedies", "05-fixes"), (6, "verify", "06-verdict.md")]

def sh(*cmd):
    r = subprocess.run(cmd, text=True)
    if r.returncode: sys.exit(r.returncode)

def new(target, profile, workflow, medium, root):
    slug = re.sub(r"[^a-z0-9]+", "-", pathlib.Path(target).stem.lower() if not target.startswith("http") else re.sub(r"https?://", "", target).lower())[:40].strip("-")
    run = pathlib.Path(root) / f"{datetime.datetime.now():%Y%m%d-%H%M}-{slug}"
    run.mkdir(parents=True, exist_ok=True)
    (run / "run.json").write_text(json.dumps({"target": target, "profile": profile, "workflow": workflow, "medium": medium,
                                               "created": datetime.datetime.now().isoformat(timespec="seconds"), "skips": []}, indent=1))
    print(run)
    return run

def gates(run):
    run = pathlib.Path(run); cfg = json.loads((run / "run.json").read_text()) if (run / "run.json").exists() else {}
    skipped = {s["phase"] for s in cfg.get("skips", [])}
    for n, name, f in GATES:
        p = run / f
        ok = p.exists() and (p.is_dir() and any(p.iterdir()) or p.is_file() and p.stat().st_size > 0)
        if f.endswith("manifest.json") and ok: ok = json.loads(p.read_text()).get("control", {}).get("ok", False)
        print(f"  phase {n} {name:11s} {'done' if ok else ('skipped by user' if n in skipped else 'NOT DONE')}  ({f})")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd"); ap.add_argument("arg", nargs="?")
    ap.add_argument("--profile", default="balanced"); ap.add_argument("--workflow", default="full"); ap.add_argument("--medium", default="web")
    ap.add_argument("--root", default=".unslop"); ap.add_argument("--widths", default=None)
    a = ap.parse_args()
    py, node = sys.executable, "node"
    if a.cmd == "new": new(a.arg, a.profile, a.workflow, a.medium, a.root)
    elif a.cmd == "capture":
        cfg = json.loads((pathlib.Path(a.arg) / "run.json").read_text())
        widths = a.widths or ("375,1440" if cfg.get("workflow") == "quick" else "320,375,414,768,1024,1280,1440,1920")
        sh(node, str(ROOT / "scripts/capture/capture.mjs"), cfg["target"], a.arg, "--widths", widths)
    elif a.cmd == "sweep":
        cfg = json.loads((pathlib.Path(a.arg) / "run.json").read_text())
        sh(py, str(ROOT / "scripts/checks/sweep.py"), a.arg, "--profile", cfg.get("profile", "balanced"), "--medium", cfg.get("medium", "web"), "--quiet")
    elif a.cmd == "synthesize": sh(py, str(ROOT / "scripts/report/synthesize.py"), a.arg)
    elif a.cmd == "gates": gates(a.arg)
    elif a.cmd == "quick":
        run = new(a.arg, a.profile, "quick", a.medium, a.root)
        sh(node, str(ROOT / "scripts/capture/capture.mjs"), a.arg, str(run), "--widths", a.widths or "375,1280,1440")
        sh(py, str(ROOT / "scripts/checks/sweep.py"), str(run), "--profile", a.profile, "--medium", a.medium, "--quiet")
        sh(py, str(ROOT / "scripts/report/synthesize.py"), str(run))
    elif a.cmd == "selftest": sh(py, str(ROOT / "scripts/selftest.py"))
    else: ap.error(f"unknown command {a.cmd}")

if __name__ == "__main__":
    main()
