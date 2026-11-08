---
name: sweep
description: Phase 2 of an Unslop audit. Runs every mechanical detector (slop tells, colour, type, spacing, copy lexicons, content integrity, accessibility, robustness, motion, performance) as scripts over the captured evidence and writes 02-mechanical.json. No judgment. Use when the unslop orchestrator reaches the sweep, or to re-check after fixes.
---

# Sweep

```bash
python3 $U/scripts/checks/sweep.py $RUN --profile <profile> --medium web        # prints a table
python3 $U/scripts/checks/sweep.py $RUN --only contrast,targets                  # a subset
```

The sweep resolves thresholds in precedence order (core default, profile, media adapter, brief overrides from `run.json`) and writes the resolved set to `$RUN/resolved-thresholds.json`, so the run records exactly which numbers it used.

Every detector listed in `data/thresholds.yaml` ends with one status:

- `ran`: with zero or more hits. Each hit cites a rule card (`rules/<domain>-<PREFIX>.yaml`, e.g. `D03-SLP.yaml`), a tier, where, and measured evidence.
- `skipped: <reason>`: the detector does not apply (no forms, no ledger yet, profile disabled it).
- `not-verified: <reason>`: it applies but the evidence is missing or untrustworthy (control failed, a capture file is absent, the detector errored).

## Your job in this phase

1. Run it. Read the printed table.
2. Read every `not-verified` line. If a capture file is missing, recapture; if a detector errored, report it as not verified. Never replace a failed detector with your own estimate.
3. Do not add, remove or re-tier hits here. Disagreement with a mechanical hit is recorded by `synthesize` as a note with your reason, never by editing `02-mechanical.json`.

## Trusting the detectors

`python3 $U/scripts/selftest.py` captures the seeded-defect pages and the control and fails if any detector misses its seed or fires on the control. Run it after changing any detector, threshold or lexicon. 49 detectors are seeded in this build; `distinctness` needs a ledger and `redesign_loss` needs a baseline run, so both report `skipped` in ordinary runs.

Detectors catch what can be measured. A clean sweep is not a clean design: the lenses judge concept, hierarchy and voice.
