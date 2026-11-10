#!/usr/bin/env python3
"""Seeded-defect self-test (T-SEEDED-DEFECT): every detector must catch its seed and stay silent on the control.

usage: python3 scripts/selftest.py [--out DIR] [--no-capture] [--profile strict]
Seed pages live in evals/seeded-defects/. A page declares the detectors it seeds with data-seed="det1 det2"
attributes and/or <meta name="unslop-seeds" content="det1 det2">. control.html must produce zero findings.
"""
import argparse, json, pathlib, re, subprocess, sys, tempfile
ROOT = pathlib.Path(__file__).resolve().parents[1]
SEEDS = ROOT / "evals/seeded-defects"
sys.path.insert(0, str(ROOT / "scripts/checks"))

def ensure_assets():
    p = SEEDS / "assets/noise.png"
    if not p.exists():          # large on purpose (performance seed); generated, not committed
        import numpy as np
        from PIL import Image
        p.parent.mkdir(exist_ok=True)
        Image.fromarray(np.random.default_rng(7).integers(0, 255, (1400, 1400, 3), dtype=np.uint8)).save(p)

def seeds_of(html):
    s = set()
    for m in re.finditer(r'data-seed="([^"]+)"', html): s.update(m.group(1).split())
    for m in re.finditer(r'<meta name="unslop-seeds" content="([^"]+)"', html): s.update(m.group(1).split())
    return s

def capture(page, run, widths):
    r = subprocess.run(["node", str(ROOT / "scripts/capture/capture.mjs"), str(page), str(run), "--widths", widths, "--passive", "3000"], capture_output=True, text=True)
    if r.returncode: raise SystemExit(f"capture failed for {page.name}:\n{r.stderr[-2000:]}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None); ap.add_argument("--no-capture", action="store_true"); ap.add_argument("--profile", default="strict")
    a = ap.parse_args()
    out = pathlib.Path(a.out or tempfile.mkdtemp(prefix="unslop-selftest-"))
    ensure_assets()
    import sweep
    pages = {"control": SEEDS / "control.html", **{p.stem: p for p in sorted(SEEDS.glob("*.html")) if p.stem != "control"}}
    results, failures = {}, []
    for name, page in pages.items():
        run = out / name
        if not a.no_capture: capture(page, run, "375,1280,1440" if name != "blank" else "1440")
        results[name] = sweep.run(str(run), a.profile, "web")
        if not results[name]["summary"]["control_ok"]: failures.append(f"{name}: control render failed, nothing is verified")
    ctl = results["control"]["detectors"]
    for det, r in ctl.items():
        for h in r.get("hits", []): failures.append(f"control: {det} false positive: {h['where'][:50]} :: {h['evidence'][:90]}")
    expected = {}
    for name, page in pages.items():
        if name == "control": continue
        for det in seeds_of(page.read_text()): expected.setdefault(det, []).append(name)
    print(f"{'detector':22s} {'seed page(s)':28s} result")
    for det in sorted(set(ctl) | set(expected)):
        pages_for = expected.get(det, [])
        if not pages_for:
            st = ctl[det]["status"]
            print(f"{det:22s} {'(no seed)':28s} {'unseeded: ' + st if st != 'ran' else 'UNSEEDED'}")
            if st == "ran": failures.append(f"{det}: has no seed page")
            continue
        caught = [p for p in pages_for if results[p]["detectors"].get(det, {}).get("hits")]
        st = results[pages_for[0]]["detectors"].get(det, {}).get("status", "missing")
        ok = bool(caught)
        print(f"{det:22s} {', '.join(pages_for):28s} {'caught' if ok else 'MISSED (' + st + ')'}")
        if not ok: failures.append(f"{det}: missed its seed ({st})")
    # check-level seeds: <meta name="unslop-checks" content="detector:check ..."> needs a hit carrying that check, so a
    # second path in one detector (motion_snap passive, text_floor scaled) cannot pass on the strength of the first
    for name, page in pages.items():
        if name == "control": continue
        for m in re.finditer(r'<meta name="unslop-checks" content="([^"]+)"', page.read_text()):
            for pair in m.group(1).split():
                det, chk = pair.split(":")
                hits = results[name]["detectors"].get(det, {}).get("hits", [])
                ok = any(h.get("check") == chk for h in hits)
                print(f"{det + ':' + chk:22s} {name:28s} {'caught' if ok else 'MISSED'}")
                if not ok: failures.append(f"{det}: check '{chk}' missed its seed on {name}")
    print(f"\nevidence: {out}")
    if failures:
        print(f"\nSELF-TEST FAILED ({len(failures)}):"); [print(" -", f) for f in failures]; sys.exit(1)
    print("SELF-TEST PASSED: every seeded detector caught its seed; control is clean.")

if __name__ == "__main__":
    main()
