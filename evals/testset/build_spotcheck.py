#!/usr/bin/env python3
"""Build evals/testset/results/spot-check.html: one self-contained page for a human reviewer to decide the
"label generous" and contested rows of the adjudications.

usage: build_spotcheck.py <refs-dir> <local-runs> <live-runs> [--out evals/testset/results/spot-check.html]
Rows come from the adjudication tables; the lens read from the archived round; screenshots from the run folders
(fold plus one more screen), embedded as JPEG data URIs. Decisions are kept in the reviewer's browser and exported
as JSON from the page.
"""
import argparse, base64, html, io, json, pathlib, re
import yaml
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RES = HERE / "results"
SOURCES = [  # (adjudication file, archived lens round, manifest, which runs dir)
    ("round-2-adjudication.md", "round-2", "set1.yaml", "local"),
    ("live-round-1-adjudication.md", "live-round-1", "set1-live.yaml", "live"),
]
KEEP = re.compile(r"label generous|contested", re.I)

ap = argparse.ArgumentParser(); ap.add_argument("refs"); ap.add_argument("local"); ap.add_argument("live")
ap.add_argument("--out", default=str(RES / "spot-check.html")); a = ap.parse_args()
RUNS = {"local": pathlib.Path(a.local), "live": pathlib.Path(a.live)}

def md_inline(s):
    s = html.escape(s.strip())
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", s)

def jpeg(im, w=900):
    im = im.convert("RGB")
    if im.width > w: im = im.resize((w, round(im.height * w / im.width)))
    b = io.BytesIO(); im.save(b, "JPEG", quality=70, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def screens(item, runs):
    """Two images: the first screen and one further screen, with captions."""
    ev = runs / item["id"] / "01-evidence"
    if item.get("kind") == "image":
        im = Image.open(pathlib.Path(a.refs) / item["repo"] / item["path"])
        h = round(im.width * 0.625)
        return [(jpeg(im.crop((0, 0, im.width, min(im.height, h)))), "Top of the image"),
                (jpeg(im.crop((0, min(h, max(0, im.height - h)), im.width, min(im.height, 2 * h)))), "Further down")]
    folds = sorted(ev.glob("fold-*.png"), key=lambda p: -int(p.stem.split("-")[1]))
    fold = next((p for p in folds if p.stem.endswith(("1440", "1920"))), folds[0] if folds else None)
    out = []
    if fold: out.append((jpeg(Image.open(fold)), f"First screen at {fold.stem.split('-')[1]}px"))
    w = fold.stem.split("-")[1] if fold else None
    tiles = sorted((ev / "tiles").glob(f"{w}-*.png")) if w else []
    if len(tiles) > 2: out.append((jpeg(Image.open(tiles[2])), "Third screen"))
    elif len(tiles) > 1: out.append((jpeg(Image.open(tiles[1])), "Second screen"))
    else:
        shot = next(iter(sorted(ev.glob("shot-*.png"), key=lambda p: -int(p.stem.split("-")[1]))), None)
        if shot:
            im = Image.open(shot); h = round(im.width * 1.2)
            if not out: out.append((jpeg(im.crop((0, 0, im.width, min(im.height, h)))), "First page"))
            if im.height > h: out.append((jpeg(im.crop((0, h, im.width, min(im.height, 2 * h)))), "Further down"))
    if len(out) < 2 and (ev / "fold-375.png").exists():      # short page: the phone view is the useful second look
        out.append((jpeg(Image.open(ev / "fold-375.png"), w=420), "First screen at 375px"))
    return out

rows = []
for adj, rnd, manifest, which in SOURCES:
    items = {i["id"]: i for i in yaml.safe_load((HERE / manifest).read_text(encoding="utf-8"))["items"]}
    for line in (RES / adj).read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 5 or not KEEP.search(cells[3]): continue
        iid = cells[0].split()[0]
        if iid not in items: continue
        it = items[iid]
        lens = RES / rnd / iid / "03-lenses" / "slop.json"
        sl = json.loads(lens.read_text(encoding="utf-8")) if lens.exists() else {}
        rows.append(dict(id=iid, round=rnd, name=cells[0][len(iid):].strip() or it.get("url", it.get("path", "")),
                         url=it.get("url"), source=f"{it.get('repo')}/{it.get('path')}" if it.get("repo") else None,
                         expect=cells[1], unslop=cells[2], cause="contested" if "contested" in cells[3].lower() else "label generous",
                         evidence=cells[4], read=sl.get("overall_read"), conf=sl.get("confidence"), reason=sl.get("overall_reason", ""),
                         why=it.get("why", ""), images=screens(it, RUNS[which])))

def card(r):
    imgs = "".join(f'<figure><img src="{src}" alt="{html.escape(r["id"])}: {html.escape(cap.lower())}" loading="lazy"><figcaption>{cap}</figcaption></figure>' for src, cap in r["images"])
    link = f'<a href="{html.escape(r["url"])}" target="_blank" rel="noopener">{html.escape(r["url"])}</a>' if r["url"] else f'<code>{html.escape(r["source"] or "")}</code>'
    read = f'{html.escape(r["read"] or "no lens read")}{" (" + html.escape(r["conf"]) + ")" if r["conf"] else ""}'
    rid = html.escape(r["id"])
    return f'''<article class="row" data-id="{rid}" data-cause="{r["cause"]}">
  <div class="shots">{imgs}</div>
  <div class="facts">
    <header><span class="iid">{rid}</span><span class="tag {r["cause"].replace(" ", "-")}">{r["cause"]}</span><span class="rnd">{html.escape(r["round"])}</span></header>
    <h2>{md_inline(r["name"])}</h2>
    <p class="src">{link}</p>
    <dl>
      <div><dt>Label says</dt><dd><span class="lab">{html.escape(r["expect"])}</span> <span class="muted">{html.escape(r["why"])}</span></dd></div>
      <div><dt>Unslop says</dt><dd><span class="lab">{md_inline(r["unslop"])}</span> <span class="muted">slop lens: {read}</span></dd></div>
      <div><dt>Evidence</dt><dd>{md_inline(r["evidence"])}</dd></div>
      <div><dt>Lens reason</dt><dd class="reason">{html.escape(r["reason"])}</dd></div>
    </dl>
    <fieldset class="decide" aria-label="Your call on {rid}">
      <legend>Your call</legend>
      <button type="button" data-v="unslop">Unslop is right</button>
      <button type="button" data-v="label">The label is right</button>
      <button type="button" data-v="unsure">Unsure</button>
    </fieldset>
    <label class="note-l" for="note-{rid}">Note (optional)</label>
    <textarea id="note-{rid}" class="note" rows="2" placeholder="What decided it for you"></textarea>
  </div>
</article>'''

page = (HERE / "spotcheck_template.html").read_text(encoding="utf-8")
page = page.replace("{{ROWS}}", "\n".join(card(r) for r in rows)).replace("{{COUNT}}", str(len(rows)))
page = page.replace("{{IDS}}", json.dumps([r["id"] for r in rows]))
pathlib.Path(a.out).write_text(page, encoding="utf-8")
print(f"{len(rows)} rows -> {a.out} ({pathlib.Path(a.out).stat().st_size // 1024} KB)")
