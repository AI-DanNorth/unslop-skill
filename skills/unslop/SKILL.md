---
name: unslop
description: Audit a design artifact (web page now; slides, print, app, social, email, video later) for AI-default slop, accessibility floors and craft errors, and produce a ranked, evidence-backed report. Use when the user asks to audit, review, critique, "unslop", de-AI or QA a design, page, site, screen or deck, or asks whether something "looks AI-generated".
---

# Unslop orchestrator

You run the audit. You do not judge anything yourself in this skill; you call the phases in order, check each gate file, and stop when a gate is missing. Read `core/guardrails.md` before the first run in a session; it binds every phase.

`$U` below means the plugin root (`${CLAUDE_PLUGIN_ROOT}`).

## 1. Pick the workflow

| Workflow | When | Phases |
|---|---|---|
| `quick` | "quick look", "is this sloppy?", a single screen, time pressure | 0 (light) → 1 (375, 1280, 1440) → 2 → 4 |
| `full` | default for "audit / review this" | 0 → 1 → 2 → 3 (lenses the contract selects) → 4 |
| `diff` | reviewing a change: two targets or a branch | as `full`, on both; findings classed introduced / regression / pre-existing |
| `redesign` | the user is replacing an existing page | as `full` + `run.json.baseline_run` so `redesign_loss` runs |

Fix loops (phase 5 remedies, phase 6 verify) run only when the user asks for fixes after seeing the report. Phase-1 build: remedies are not shipped yet, so say so and offer to fix findings directly, finding by finding.

## 2. Run the phases

```bash
RUN=$(python3 $U/scripts/unslop.py new "<url-or-file>" --profile balanced --workflow full)
```

1. **Phase 0 Intake**: invoke the `intake` skill. Gate: `$RUN/00-contract.md`.
2. **Phase 1 Capture**: invoke `capture` (or `python3 $U/scripts/unslop.py capture $RUN`). Gate: `01-evidence/manifest.json` with `control.ok: true`. If the control failed, stop: the verdict is `recapture`.
3. **Phase 2 Sweep**: invoke `sweep` (or `python3 $U/scripts/unslop.py sweep $RUN`). Gate: `02-mechanical.json`.
4. **Phase 3 Lenses**: for each lens the contract selects, invoke it. This build ships `lens-slop`, `lens-a11y`, `lens-concept`, `lens-structure`, `lens-typography`, `lens-color`, `lens-copy`, `lens-motion`, `lens-integrity`, `lens-components`, `lens-imagery` and `lens-dataviz`; list the other lenses under "Not investigated: lens not built yet". Lenses run independently: never pass one lens's findings to another. Gate: `03-lenses/<lens>.json` per lens.
5. **Phase 4 Synthesize**: invoke `synthesize`. Gate: `04-report.md` with a verdict word.

After each phase run `python3 $U/scripts/unslop.py gates $RUN` and do not start a phase whose predecessor shows NOT DONE. A phase may be skipped only when the user says so; record it in `run.json` under `skips` with the reason.

## 3. Deliver

Give the user the verdict word, the score line, the top findings (Floor first) and the three quick wins, then attach `04-report.md`. Point out anything in "Not investigated" that matters for their decision. Do not paste the whole report into chat.

## Rules that never bend

- The control render, the Floor checks and the gate check are never skipped.
- A score never overrides the user's brief (`core/precedence.md`).
- The audit changes nothing in the artifact.
- If a script errors, report the phase as not verified with the error; never fill the gap with estimates.
