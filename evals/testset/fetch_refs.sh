#!/usr/bin/env bash
# Rebuild the source repos the test sets point at (sources: in every set*.yaml), each at its pinned commit.
# usage: evals/testset/fetch_refs.sh [refs-dir]   (default: ../unslop-refs next to this repo)
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
refs="${1:-$here/../../../unslop-refs}"; mkdir -p "$refs"
# tr strips the \r that Windows Python adds to each line; without it the SHAs never match.
python3 - "$here" <<'PY' | tr -d '\r' | while read -r name repo sha; do
import sys, yaml, pathlib
seen = {}
for f in sorted(pathlib.Path(sys.argv[1]).glob("set*.yaml")):          # every test set's sources, once each
    for k, v in (yaml.safe_load(open(f, encoding="utf-8")).get("sources") or {}).items(): seen.setdefault(k, v)
for k, v in seen.items(): print(k, v["github"], v["commit"])
PY
  dir="$refs/$name"
  if [ -d "$dir/.git" ] && [ "$(git -C "$dir" rev-parse HEAD)" = "$sha" ]; then echo "ok    $name"; continue; fi
  rm -rf "$dir"; mkdir -p "$dir"
  git -C "$dir" init -q && git -C "$dir" remote add origin "https://github.com/$repo"
  git -C "$dir" fetch -q --depth 1 --filter=blob:none origin "$sha"
  # Leave out paths Windows cannot create (CON, PRN, AUX, NUL, COM1-9, LPT1-9, with any extension, any case),
  # so checkout succeeds on every OS. None of them are used by the test sets.
  git -C "$dir" sparse-checkout init --no-cone 2>/dev/null || git -C "$dir" config core.sparseCheckout true
  python3 - "$dir/.git/info/sparse-checkout" <<'PY'
import sys
names = ["con", "prn", "aux", "nul"] + [f"com{i}" for i in range(1, 10)] + [f"lpt{i}" for i in range(1, 10)]
ci = lambda n: "".join(f"[{c.lower()}{c.upper()}]" if c.isalpha() else c for c in n)
lines = ["/*"] + [f"!**/{ci(n)}{suffix}" for n in names for suffix in ("", ".*", "/")]
open(sys.argv[1], "w", newline="\n").write("\n".join(lines) + "\n")  # LF: git reads a \r as part of each pattern
PY
  # Git refuses reserved names in the tree on Windows even when sparse-checkout leaves them out.
  git -C "$dir" config core.protectNTFS false
  git -C "$dir" checkout -q FETCH_HEAD
  echo "fetched $name @ ${sha:0:7}"
done
echo "refs ready in $refs"
