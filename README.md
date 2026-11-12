# Unslop

A Claude plugin that audits design artifacts for AI-default slop, accessibility floors and craft errors, then reports findings ranked by severity, each tied to a rule card and to measured evidence.

**Status: phase 1 (core and web MVP), calibrated on test set 1.** Draft adapters for slides, social, print, diagram, email and app. The other lenses and remedies follow the roadmap in `docs/PLAN.md`. Start with `CLAUDE.md`.

## How it works

```
intake ─▶ capture ─▶ sweep ─▶ lenses ─▶ synthesize ─▶ (remedies ─▶ verify)
 00-contract   01-evidence   02-mechanical   03-lenses/   04-report.md
```

- **Capture** renders the page with Playwright at each audit width, then clicks its transition triggers (frames with reduced motion off and on) and its primary actions (network held, then failed). It first renders a known-good control page, and if the control does not reproduce, every capture finding is marked "not verified".
- **Sweep** runs 58 mechanical detectors: slop tells, colour, type, spacing, copy lexicons, content integrity, accessibility, robustness, motion and performance. Each detector reads its numbers from `data/thresholds.yaml`.
- **Lenses** are Claude skills that judge what scripts cannot. Each one runs named tests from `core/tests/tests.yaml`.
- **Synthesize** merges findings to root causes, drops anything without evidence, scores 7 dimensions with caps, and writes a report that opens with a verdict word.

Phases hand off through gate files in `.unslop/<run-id>/`. A missing gate means the phase did not happen.

## Use

In Claude: "audit this page with unslop" (the `unslop` skill orchestrates the run).

From a shell:

```bash
python3 scripts/unslop.py quick https://example.com --profile balanced   # capture + sweep + draft report
python3 scripts/unslop.py gates .unslop/<run-id>                         # what is done
python3 scripts/selftest.py                                              # every detector vs. its seeded defect
```

Requirements: Node 18+, Playwright with Chromium, and Python 3.10+ with PyYAML, NumPy and Pillow.

## Layout

| Path | What |
|---|---|
| `core/` | Contracts every skill reads: rule schema, severity, report format, guardrails, precedence, gates, glossary, conflict register, named tests, profiles |
| `data/` | Thresholds, 12 lexicons, look-family definitions, stress fixtures |
| `rules/` | Rule cards: `curated.yaml` (227 active, hand-written) and generated `<PREFIX>.yaml` files (adds 2,194 mined drafts with provenance) |
| `skills/` | `unslop`, `intake`, `capture`, `sweep`, `lens-slop`, `lens-a11y`, `lens-concept`, `lens-structure`, `lens-typography`, `lens-color`, `lens-copy`, `lens-motion`, `lens-integrity`, `lens-components`, `lens-imagery`, `synthesize`, `media-web` |
| `scripts/` | Capture (Node), checks and sweep (Python), report synthesis, build tools, self-test |
| `evals/seeded-defects/` | Control page (must stay clean) and seed pages (every detector must catch its seed) |
| `research/` | The 21 source docs, the mining files the cards were built from, reader notes and the web research report |
| `docs/` | The plan (exported), project history and decisions, agent prompts, prompts for next sessions |
| `evals/candidates/`, `evals/testset/` | 1,883 candidate examples; test set 1 (52 local + 39 live), results and adjudications |
| `sources/` | Source index and `provenance.csv` (rule id → source sections) |

## Changing rules

Edit `rules/curated.yaml`, `data/thresholds.yaml` or the lexicon lists in `scripts/build/make_lexicons.py`. Then run:

```bash
python3 scripts/build/make_lexicons.py
python3 scripts/build/build_rules.py      # regenerates rules/<domain>-<PREFIX>.yaml and lints cards against thresholds
python3 scripts/selftest.py               # must pass
```

See `CONTRIBUTING.md` for the review bar.
