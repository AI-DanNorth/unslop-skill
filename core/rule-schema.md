# Rule card schema

Every rule, from every source, is rewritten into this one shape. Cards live in `rules/<PREFIX>.yaml`, one list per domain prefix. The id is permanent: a retired rule keeps its id with `status: retired`.

```yaml
- id: SLP-012                 # PREFIX-NNN, never reused
  title: No eyebrow above section headings
  domain: D03                 # see glossary.md for D00-D20
  tier: Reflex                # Floor | Reflex | Finish (severity.md)
  priority: P1                # P0-P3
  kind: ban                   # ban | cap | context
  check: M                    # M mechanical | J judgment | H hybrid
  detector: eyebrow           # name of the script in scripts/checks/ (M and H only)
  applies_when: [web, app, slides]   # media; omit = all
  profiles: {strict: Reflex, balanced: cap, conventional: info}   # optional overrides
  rule: >                     # imperative, specific
    Do not place a small tracked label above a heading unless it carries a fact.
  why: >                      # user impact in one or two sentences
  values: {max_size_px: 14, ratio_to_heading: 0.45, min_tracking_em: 0.06}
  incorrect: "<p class=eyebrow>FEATURES</p><h2>Built for teams</h2>"
  correct: "<h2>Invoices that match your ledger</h2>"
  fix: Promote the fact into the heading, or delete the label.
  remedy: fix-typeset         # the remedy skill that owns the fix
  waivable_by: brief          # brief | brand-system | never
  tests: [eyebrow-test]       # named tests in core/tests/
  sources: ["hallmark §111", "impeccable §520"]
  status: active              # active | draft | retired
```

## Field rules

- `rule` is imperative and checkable. "Use good contrast" is not a rule; "Body text at least 4.5:1 against the worst sampled pixel" is.
- `values` holds every number the rule needs. A detector reads the number from `data/thresholds.yaml` under the detector's name; the card's `values` mirrors it for readers. If they disagree, `thresholds.yaml` wins and the linter (`scripts/lint-rules.py`) fails.
- `kind`:
  - `ban`: one occurrence is a finding.
  - `cap`: a finding only past a budget (`values.budget`).
  - `context`: a finding only when `applies_when` and the contract match (for example, "journey" outside travel).
- Floor cards set `waivable_by: never`.
- `sources` lists every collection the rule was merged from, so provenance survives the merge.
- `status: draft` cards are loaded by lenses as advice only and never produce a blocking finding.
