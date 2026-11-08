# Prompts for the next Claude Code sessions

Run these in order in Claude Code, from the repo root. Each one ends by reporting back, so you can review before the next. Paths assume the source repos are in `../unslop-refs` and runs go to `../unslop-runs-live`.

## 0. First message in a new session (setup check)

> Read CLAUDE.md, docs/HISTORY.md and the "Test corpus and calibration" and "Roadmap" sections of docs/PLAN.md. Check the setup:
> - `npm install && npx playwright install chromium`
> - `python3 -m pip install -r requirements.txt`
> - `evals/testset/fetch_refs.sh ../unslop-refs`
> - `python3 scripts/selftest.py`
>
> Also confirm git is set to commit as AI-DanNorth. Tell me anything that fails. Don't start other work yet.

## 1. Capture the live test set

> Run next step 1 from CLAUDE.md, capture only:
> - `python3 evals/testset/run_set.py evals/testset/set1-live.yaml ../unslop-refs ../unslop-runs-live`, then `scripts/capture/tiles.py` on every run.
> - Open each run's fold screenshot and manifest. List any item that shows a cookie wall, a bot or login block, an error page, a redirect to a different site, or a near-empty render.
> - For cookie walls, try once to dismiss the banner (add a click step or a consent cookie for that host in capture). Otherwise record the item as not verified in `evals/testset/results/live-capture-notes.md` with the reason and capture date.
>
> Commit and push. Report the capture table (item, status, notes) and stop.

## 2. Blind review of the live set

> Run blind lens reviews on every verified live item in ../unslop-runs-live:
> - Send general-purpose agents in batches of about 8, mixing groups, each with `evals/testset/LENS-BRIEF.md` and the paths filled in (repo, runs = ../unslop-runs-live, refs = ../unslop-refs).
> - Never tell a reviewer the expected labels.
> - When all are back, archive with `evals/testset/archive_round.sh live-round-1 ../unslop-runs-live`, synthesize every run, and score with `python3 evals/testset/calibrate.py evals/testset/set1-live.yaml ../unslop-runs-live --out evals/testset/results/live-round-1-calibration.md`.
>
> Commit and push. Report the agreement table and stop.

## 3. Adjudicate and fix

> Write `evals/testset/results/live-round-1-adjudication.md` in the same shape as round-2-adjudication.md. Sort every disagreement into:
> - label generous;
> - fixture semantics;
> - limitation;
> - partial;
> - contested;
> - system error.
>
> Each needs the evidence it rests on. Pay most attention to false positives on the human controls and exemplars (L23 to L36): any slop or Floor call there is a system error until proven otherwise. Then:
> - Fix only what the evidence supports, following the repo rules (threshold entry, curated card, seed, self-test).
> - Re-sweep, re-score and append the new numbers to the adjudication.
> - Update the "Status" section of CLAUDE.md and the build-status note in docs/PLAN.md.
>
> Commit and push, then report.

## 4. Prepare the human spot-check

> Build a single HTML page, `evals/testset/results/spot-check.html`, for a human reviewer. Show every "label generous" and "contested" row from both adjudications (local round 2 and live round 1). For each row include:
> - the fold screenshot and one more tile;
> - the expected label, Unslop's read and the cited evidence;
> - three buttons (Unslop right / label right / unsure) that save to localStorage, and an export-to-JSON button.
>
> Commit and push, and tell me how to open it.

## 5. Motion and interaction capture

> Add motion and interaction capture (next step 3 in CLAUDE.md):
> - **Frames:** in capture, for each transition trigger (buttons, menus, dialogs, tabs), record frames at 0, 50, 100, 150, 250, 400 and 600 ms after the action, with `prefers-reduced-motion` both off and on.
> - **Async:** a scripted-interaction step that clicks primary actions with the network slowed and records what the UI shows at 0.5 s, 2 s and after completion.
> - **Detectors:** add a motion detector (durations, overshoot measured from frames, layout movement) and an async-state detector (no feedback, false success, stuck spinner), each with seeds and self-test.
> - Re-run S12, G10 and C01 from set1.yaml and report whether they are now caught.
>
> Commit and push.

## 6. Phase 2: the remaining lenses

> Start phase 2 from the roadmap in docs/PLAN.md: the remaining judgment lenses. Do them one lens at a time, starting with concept, structure, typography, color and copy. For each lens:
> - Write its SKILL.md from the plan's lens table and the matching curated and draft cards in `rules/`.
> - Promote the 10 to 20 most important draft cards for that lens to curated, with values and sources.
> - Run it blind on 8 items from test set 1 (mixed labels).
> - Add its results to a new calibration round.
>
> Commit and push after each lens and report before starting the next.
