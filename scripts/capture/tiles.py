#!/usr/bin/env python3
"""Cut tall full-page screenshots into screen-sized tiles for judgment lenses (T-SCREEN-BY-SCREEN).

usage: tiles.py <run-dir> [--max 6]
Writes 01-evidence/tiles/<w>-NN.png at one screen height each (900px at desktop widths, 812px at 375).
"""
import sys, pathlib
from PIL import Image
HEIGHT = {375: 812, 414: 896, 768: 1024, 1024: 768, 1280: 800, 1440: 900, 1920: 1080}
run = pathlib.Path(sys.argv[1]); mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 12
ev = run / "01-evidence"; out = ev / "tiles"; out.mkdir(exist_ok=True)
for shot in sorted(ev.glob("shot-*.png")):
    w = int(shot.stem.split("-")[1])
    im = Image.open(shot); W, H = im.size
    step = HEIGHT.get(w, int(W * 0.625))
    n = 0
    for i, y in enumerate(range(0, H, step)):
        if i >= mx: break
        im.crop((0, y, W, min(H, y + step))).save(out / f"{w}-{i:02d}.png"); n += 1
    print(f"{shot.name}: {H}px -> {n} tiles{' (truncated)' if H > step * mx else ''}")
