# Unslop: working notes for Claude

Unslop is a Claude plugin that audits design artifacts for AI-default slop, accessibility floors and craft errors. Read `README.md` for the layout and `core/guardrails.md` before any audit. The plan and its history live in the claude.ai Project "Design Reviewing System" (the plan doc) and in `evals/testset/results/`.

## Where things are

| Need | Read |
|---|---|
| The plan (architecture, domains, pipeline, bundles, detectors, conflicts, roadmap) | `docs/PLAN.md` (export of the claude.ai Project plan doc; the live doc is the source of truth) |
| What happened, decisions, lessons, mistakes | `docs/HISTORY.md` |
| Prompts for the next sessions | `docs/NEXT-PROMPTS.md` |
| Prompts that produced the research | `docs/AGENT-PROMPTS.md` |
| The 21 source docs the rules came from | `research/sources/` |
| Mined rule rows, named tests, conflicts, lexicons | `research/mining/` (A to G) |
| Web research findings | `research/web-research-report.md` |
| Candidate examples (1,883 rows) | `evals/candidates/` |
| Test sets, results, adjudications | `evals/testset/` |

## Setup (once per machine)

```bash
npm install && npx playwright install chromium     # capture
python3 -m pip install -r requirements.txt          # checks and reports
evals/testset/fetch_refs.sh ../unslop-refs          # the 13 source repos test set 1 uses, at pinned commits
python3 scripts/selftest.py                         # must print SELF-TEST PASSED
```

## Commands

| Task | Command |
|---|---|
| Quick audit of a URL or file | `python3 scripts/unslop.py quick <url-or-file> --profile balanced` |
| Phase gates of a run | `python3 scripts/unslop.py gates <run-dir>` |
| Detector self-test | `python3 scripts/selftest.py` |
| Rebuild rule cards and lint | `python3 scripts/build/build_rules.py` |
| Rebuild lexicons | `python3 scripts/build/make_lexicons.py` |
| Capture + sweep a test set | `python3 evals/testset/run_set.py <set.yaml> <refs-dir> <runs-dir> [--only ID,ID]` |
| Screenshot tiles for reviewers | `python3 scripts/capture/tiles.py <run-dir>` |
| Score a test set | `python3 evals/testset/calibrate.py <set.yaml> <runs-dir> --out <report.md>` |
| Archive a review round | `evals/testset/archive_round.sh <round-name> <runs-dir>` |

## Rules for working in this repo

- **Commits** are authored as AI-DanNorth: `git config user.name "AI-DanNorth"` and `git config user.email "287803787+AI-DanNorth@users.noreply.github.com"`. Commit and push to `main` after each meaningful step.
- **Never delete review output.** `03-lenses/` folders hold blind judgments that cost real time. Archive a round with `archive_round.sh` before re-capturing, and never use globs like `rm -rf <runs>/*/0*`.
- **Detector changes need the self-test.** Any change to `scripts/checks/`, `data/thresholds.yaml`, a lexicon or `scripts/capture/` is followed by `python3 scripts/selftest.py`. A new detector needs a threshold entry, a curated card in `rules/curated.yaml` and a `data-seed` in `evals/seeded-defects/seeded.html`. The control page must stay clean. Re-bless it only after an intentional edit (`capture.mjs ... --bless-control`).
- **Reviews are blind.** Reviewers get `evals/testset/LENS-BRIEF.md` with the paths filled in, and never the manifests, candidates or source repos. Expected labels live only in the `set*.yaml` manifests.
- **Thresholds change only on evidence:** a detector firing on a control, or missing a tell in an answer key. Record the reason in the commit message.
- **Capture must be honest.** Blocked requests, missing fonts and failed images are recorded in `manifest.json` `network` and become "not verified", never a pass or a finding.
- **Network and page prep for live sites.** `netshim.mjs` turns itself off when the real network is reachable (`manifest.network.mode`; force it with `UNSLOP_NET=direct|shim`). Per-host cookie-banner clicks, interstitial clicks, overlay blocks, waits and scroll frames go in `scripts/capture/page-prep.json`, never in code. Each one is recorded in `manifest.prep`; see `evals/testset/results/live-capture-notes.md`.

## Status (9 Nov 2026)

- Phase 1 (core and web MVP) is built. Draft media adapters exist for slides, social, print, diagram, email and app.
- Test set 1 local items (52): two blind review rounds. 27 of 44 raw agreement; 37 of 41 after adjudication (`evals/testset/results/round-2-adjudication.md`). Re-scored on a fresh capture after the live-round fixes: unchanged.
- Motion and interaction capture (9 Nov 2026): transition frames and slowed-network actions, with `motion` and `async_state` detectors. S12 and C01 are now caught and G10 stays clean (`round-2-adjudication.md`, follow-up).
- Phase 2 started (9 Nov 2026): `lens-concept`, `lens-structure`, `lens-typography`, `lens-color` and `lens-copy` built (157 active cards). Run blind on 8 live items: verdict agreement 6 to 8 of 8 per lens, and every lens's score separates slop from good with no overlap (`evals/testset/results/phase2-round-1/SUMMARY.md`).
- Test set 1 live (39 sites, captured 9 Nov 2026): one blind round. 27 of 34 raw, **29 of 34 after evidence-based fixes**; 30 of 33 adjusted, with 2 contested (`evals/testset/results/live-round-1-adjudication.md`). L04 is not verified (unpublished app). Every Floor hit on the 14 human controls was verified: 148 false positives were traced and fixed, and what remains is real WCAG failures, not slop calls.

- Stageshow (benjitaylor/skills, MIT) added 9 Nov 2026 as source 21 (`research/notes/stageshow-review.md`): 95 draft cards from `research/mining/F-stageshow.md`, conflicts C45 to C51. Capture gained a live (real-time) motion recorder in `interact.mjs` (`run.live` in motion.json) and the `motion_snap` detector (MOT-003, Finish). Test set 2 (`evals/testset/set2.yaml`, 57 halves of Stageshow's teaching pairs, one fault per pair) needs the Stageshow playground served on port 5199 (command in the manifest).

## Owner decisions (9 Nov 2026)

- `targets`: a too-small target inside a footer (`footer`, `role=contentinfo`) is Reflex, not Floor (`footer_tier`). Floor everywhere else.
- Spot-check rows stay **provisional** until the designer's JSON comes back; keep working and fold the calls in then.
- The full live recapture with interaction waits until the live recorder is in (it now is): one recapture carries all the new evidence.

## Next steps, in order

1. **Human spot-check:** a designer works through `evals/testset/results/spot-check.html` (11 rows; rebuild with `evals/testset/build_spotcheck.py`) and returns the JSON. Record the calls in both adjudications. L15 (fixture semantics) is not on the page; decide it in the same pass. Until then the rows are provisional.
2. **Region-aware sweeping** for pages that exhibit slop on purpose (L19, L20): ignore sections labelled as examples.
3. **Interaction capture on live sites:** tried on L06, L13 and L26 (9 Nov 2026). The guards held (no request left the page), motion took about 33 s, L06 got a reduced-motion Floor and the Cal.com control got no hits. Recapture the full live set with interaction (now including the live recorder) before the next live round; use `--no-interact` for slow pages such as L28, which is already at about 740 s.
3a. **Test set 2 (Stageshow pairs):** round 0 (sweep only) separates 18 of 32 pairs, style 7 of 8 (`evals/testset/results/set2-round-0/SUMMARY.md`). Detectors built from it: `ai_sparkle`, `invented_mark`, `mixed_icons`, `near_tangent`, `nested_radius`, `unit_wrapped` (Reflex or Finish). Next: run the phase-2 lenses blind on the pairs (`calibrate_pairs.py --lens`), and check the icon detectors on the human controls once the live recapture has icon records. The motion pairs need a passive recording mode (they play without a click) and are not in set 2 yet. Region-aware sweeping (step 2) is built: exhibit regions are left out of slop-tell detectors (`thresholds.yaml` `exhibits`).
4. **Phase 2, continued:** add the five new lenses to intake's default set and test the full report on a few items. Then build the remaining lenses (integrity, components, imagery, dataviz, motion, robustness, tokens, brand, fidelity, usability), the scoring rubric and `verify-fix` (roadmap in the plan doc). Run each new lens blind on a larger, mixed set, including non-web media.
