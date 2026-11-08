#!/usr/bin/env bash
# Rebuild the source repos that test set 1 points at, each at its pinned commit.
# usage: evals/testset/fetch_refs.sh [refs-dir]   (default: ../unslop-refs next to this repo)
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
refs="${1:-$here/../../../unslop-refs}"; mkdir -p "$refs"
python3 - "$here/set1.yaml" <<'PY' | while read -r name repo sha; do
import sys, yaml
for k, v in yaml.safe_load(open(sys.argv[1]))["sources"].items(): print(k, v["github"], v["commit"])
PY
  dir="$refs/$name"
  if [ -d "$dir/.git" ] && [ "$(git -C "$dir" rev-parse HEAD)" = "$sha" ]; then echo "ok    $name"; continue; fi
  rm -rf "$dir"; mkdir -p "$dir"
  git -C "$dir" init -q && git -C "$dir" remote add origin "https://github.com/$repo"
  git -C "$dir" fetch -q --depth 1 --filter=blob:none origin "$sha" && git -C "$dir" checkout -q FETCH_HEAD
  echo "fetched $name @ ${sha:0:7}"
done
echo "refs ready in $refs"
