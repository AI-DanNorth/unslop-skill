#!/usr/bin/env bash
# Copy each item's lens output and report into evals/testset/results/<round>/ so a round's judgments survive re-captures.
# usage: archive_round.sh <round-name> <runs-dir>
set -euo pipefail
dest="$(dirname "$0")/results/$1"; mkdir -p "$dest"
for d in "$2"/*/; do id=$(basename "$d"); mkdir -p "$dest/$id"
  [ -d "$d/03-lenses" ] && cp -r "$d/03-lenses" "$dest/$id/"
  for f in 04-report.md 04-findings.json; do [ -f "$d/$f" ] && cp "$d/$f" "$dest/$id/"; done
done; echo "archived to $dest"
