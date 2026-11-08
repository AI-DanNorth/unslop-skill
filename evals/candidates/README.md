# Candidate examples

Everything the 23 repo agents and the web research found, kept whole for later deep dives.

- `ALL-candidates.csv`: 1,883 rows (1,786 unique). Columns: repo, kind (live URL / repo file), target, inferred_url, medium, side, label, why, source, file_check, also_cited_by, duplicate_of. Duplicates are marked, never dropped.
- `<repo>.md`: each agent's full table, best candidates and notes. `web-research.md`: 157 rows from the web research.
- `FIRST-TEST-SET.md`: draft first test set.
- Rebuild: `python3 scripts/build/merge_candidates.py evals/candidates <dir with the repo clones>`.

Status at 8 Nov 2026: every one of the 832 repo-file rows was checked against a local clone: 767 exist, 65 describe a pattern rather than point at a file. Live URLs (1,051, of which 10 are inferred from product names) are not liveness-checked: the cloud workspace cannot reach sites outside GitHub.
