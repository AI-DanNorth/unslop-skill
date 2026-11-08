# Contributing

## A rule card gets in when

1. **It is specific.** It names an element, a property or a string, and a number or a test. "Use good spacing" is rejected.
2. **It has a source.** Cite at least one collection and section, or mark it `authored` with the reason no source covers it (the email starter rules, for example).
3. **It does not duplicate a card.** Search `rules/` for the property and the tell first. If two sources say the same thing, merge them into one card and list both.
4. **Conflicts are settled first.** If sources disagree, add a row to `core/conflict-register.md` before writing the card, and keep the losing value as a profile or library setting.
5. **Mechanical rules ship with a seed.** A new detector needs an entry in `data/thresholds.yaml` and a `data-seed` in a page under `evals/seeded-defects/`. `scripts/selftest.py` must pass: the seed is caught, and the control stays clean.

## Promotion ladder

Draft cards (mined, `status: draft`) are advice for lenses. A lesson moves up as evidence accumulates:

observed → reproduced on a second artifact → guidance (draft card) → automated check (detector + seed) → default (active card)

`learn` (later phase) proposes promotions from repeated lens findings and waivers. A human approves each step.

## Tiers

- Floor: accessibility, truth, broken render, data loss. Never waivable. Be conservative: a false Floor blocks ships.
- Reflex: slop defaults and craft errors. Waivable with a written reason.
- Finish: polish. Never blocks.

## Before a pull request

```bash
python3 scripts/build/make_lexicons.py && python3 scripts/build/build_rules.py && python3 scripts/selftest.py
```
