"""Merge every candidate row from evals/candidates/<repo>.md (+ research rows) into ALL-candidates.csv.
Keeps every row (duplicates are marked, never dropped) and checks repo files exist in the local clones."""
import re, csv, glob, pathlib, collections, os, sys
CAND = pathlib.Path(sys.argv[1]); REFS = pathlib.Path(sys.argv[2])
rows = []
def parse(f, repo):
    header = None
    for line in open(f, encoding="utf-8"):
        if not line.startswith("|"):
            if line.strip(): header = None
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if all(re.fullmatch(r":?-+:?", c) or c == "" for c in cells): continue
        if header is None: header = [c.lower() for c in cells]; continue
        if header[0].startswith("section"): continue
        get = lambda *ks: next((cells[i] for i, h in enumerate(header) if any(k in h for k in ks) and i < len(cells)), "")
        target, medium = get("url", "path"), get("medium")
        if not target or not medium: continue
        rows.append(dict(repo=repo, target=target.replace("`", ""), medium=medium, label=get("label", "side"), why=get("why", "notable", "useful"), source=get("source", "section", "cites")))
for f in sorted(CAND.glob("*.md")):
    if f.stem.isupper() or f.stem.startswith("FIRST"): continue
    parse(f, f.stem)
def side(l):
    l = l.lower()
    if "benchmark" in l or "pair" in l or ("slop" in l and "good" in l) or "do/don" in l or "→" in l or "and bad" in l: return "pair/comparison"
    if "false-positive" in l: return "control (false-positive)"
    if "slop" in l or "bad" in l: return "slop"
    if "baseline" in l: return "baseline"
    if "good" in l or "exemplar" in l: return "good"
    return "neutral"
basecache = {}
def expand(t):
    m = re.search(r"\{([^{}]+)\}", t)
    if not m: return [t]
    return [x for alt in m.group(1).split(",") for x in expand(t[:m.start()] + alt + t[m.end():])]

def find_file(repo, target):
    root = REFS / repo
    if not root.exists(): return "no clone"
    target = " ".join(expand(target.replace("(+", "( ")))
    toks = re.findall(r"[\w@.\-*{}/,]+\.(?:html?|png|jpe?g|webp|gif|svg|pdf|mp4|md|json|css|jsx?|tsx?|mmd|drawio|csv|mjs|py)\b|[\w.\-]+/[\w.\-/*{}]+/?", target)
    if not toks: return "descriptive (no path)"
    for t in toks:
        t = t.split(":")[0].rstrip("/")
        for c in [t]:
            if any((root / c).exists() for _ in [0]) or glob.glob(str(root / c)): return "verified"
            if glob.glob(str(root / "**" / c), recursive=True): return "verified (nested path)"
    for t in toks:
        b = os.path.basename(t.split(":")[0].rstrip("/"))
        if b and glob.glob(str(root / "**" / b), recursive=True): return "found by file name"
    return "NOT FOUND" if re.search(r"[\w-]+/[\w.-]+|\.\w{2,4}\b", target) else "described (no file)"
seen = collections.defaultdict(list)
for i, r in enumerate(rows):
    urls = re.findall(r"https?://[^\s)`|<>,]+", r["target"])
    bare = re.findall(r"\b(?:[a-z0-9-]+\.)+(?:com|app|dev|io|ai|co|org|net|design|ski|so|fun|fit|run|uk|me|studio|site)(?:/[\w./-]*)?\b", r["target"].lower())
    if not urls and bare and not re.search(r"\.(html?|png|jpe?g|webp|md|json|css|tsx?|jsx?|pdf|svg|mp4)\b", r["target"]):
        urls = ["https://" + bare[0]]; r["inferred_url"] = urls[0]
    r["kind"] = "live URL" if urls else "repo file"
    r["side"] = side(r["label"])
    r["file_check"] = "" if urls else find_file(r["repo"], r["target"])
    key = urls[0].rstrip("/.").lower() if urls else f"{r['repo']}:{r['target']}"
    seen[key].append(i)
for key, idx in seen.items():
    for j in idx[1:]: rows[j]["duplicate_of"] = rows[idx[0]]["repo"] + " row"
    if len(idx) > 1: rows[idx[0]]["also_cited_by"] = ", ".join(sorted({rows[j]["repo"] for j in idx[1:]} - {rows[idx[0]]["repo"]}))
cols = ["repo", "kind", "target", "inferred_url", "medium", "side", "label", "why", "source", "file_check", "also_cited_by", "duplicate_of"]
with open(CAND / "ALL-candidates.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader()
    for r in rows: w.writerow({c: r.get(c, "") for c in cols})
print("rows", len(rows), "unique", len(seen))
print(collections.Counter(r["kind"] for r in rows))
print(collections.Counter(r["side"] for r in rows))
print(collections.Counter(r["file_check"] for r in rows if r["kind"] == "repo file"))
nf = [r for r in rows if r["file_check"] == "NOT FOUND"]
for r in nf[:40]: print("  NF", r["repo"], "|", r["target"][:110])
print("not found total", len(nf))
