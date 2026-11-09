---
name: synthesize
description: Phase 4 of an Unslop audit. Merges sweep and lens findings into root causes, drops findings below the quality floor, ranks them, scores the seven dimensions with caps, and writes the final report with a verdict word. Use when the unslop orchestrator reaches synthesis, or to regenerate a report after lenses change.
---

# Synthesize

```bash
python3 $U/scripts/report/synthesize.py $RUN
```

The script writes `04-findings.json` (merged, ranked findings with a quality score each; anything under 0.55 is dropped) and a draft `04-report.md`. It fills only what evidence supports: the mechanical findings, the Accessibility and Integrity scores from the sweep, and a draft verdict. **You then edit `04-report.md`** to finish it. Follow `core/report-format.md`, including its "Writing style" section. When a lens file carries `score` (`03-lenses/<lens>.json`), use its value and reason for that report dimension instead of estimating it, and apply the concept veto in `core/report-format.md` (Concept at 5 or below caps the overall score at 6).

## What you write

1. **Verdict word**, the first word of the report: `ship` (no Floor open, no unanswered Reflex), `fix` (findings are fixable in place), `rebuild` (the concept fails: Concept at 5 or below, or the rival's-name test fails on the hero and most headings), or `recapture` (the evidence cannot be trusted). The script's draft is a starting point; `rebuild` is your call from the lens findings.
2. **Four-line read**: what the artifact is for; what works and must stay; what reads generated; what is broken. One line each, specific to this artifact.
3. **Scores**: fill Concept, Hierarchy, Craft, Usability and Distinctiveness from the lens findings and your own look at the screenshots, one line of reason each. Keep the sweep's Accessibility and Integrity unless a lens disputes a hit. Apply caps: open Floor caps overall at 4; Concept 5 or below caps overall at 6. A 9 or 10 must name what was cut to earn it.
4. **Root causes**: where several findings share one cause (one token, one component, one card recipe), merge them under the cause and list the instances. Fix the cause, not the instances.
5. **Order**: Floor first, then by priority, then by how much of the page the finding touches. A generic first screen outranks every detail. Show at most 15; the rest stay in `04-findings.json`.
6. **Quick wins**: the 3 fixes with the best effect per effort, each naming its finding.
7. **Keep**: what is specific and good, so remedies do not flatten it.
8. **Not investigated**: keep the script's list (skipped and not-verified detectors, unbuilt lenses) and add anything the lenses could not check. Disputed sweep hits go here with the lens's reason.

## Rules

- Every finding in the report has evidence. If you cannot point to it, drop it.
- Do not soften a Floor finding because the page is otherwise good.
- Do not add findings of your own here; that is the lenses' job. You may merge, rank and explain.
- If the user's brief overrides a rule, the finding becomes a one-line note under Keep or Not investigated, not a finding (unless Floor).

## Gate

`04-report.md` starts with a verdict word and has no `_(synthesize...)_` placeholders left.
