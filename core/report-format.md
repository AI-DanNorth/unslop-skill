# Finding and report format

## Finding

Every lens and the sweep emit findings as JSON objects with these fields (`synthesize` validates them against `scripts/report/finding.schema.json`):

| Field | Content |
|---|---|
| `rule` | Rule id, e.g. `SLP-012` |
| `title` | Rule title |
| `tier`, `priority` | From the card, after profile resolution |
| `where` | CSS selector, `file:line`, slide or page number, plus viewport width |
| `evidence` | Measured value, screenshot crop path, or quoted text. Or `"not verified: <reason>"` |
| `before`, `after`, `why` | Current value, target value, user impact |
| `root` | The shared token or component when one cause shows in many places |
| `remedy` | The remedy skill that owns the fix |
| `source` | `sweep` or the lens name |
| `class` | Diff reviews only: `introduced`, `regression` or `pre-existing` |
| `quality` | 0 to 1, set by `synthesize` (specificity, actionability, grounding, evidence averaged) |

## Report (`04-report.md`)

1. **Verdict word**: `ship`, `fix`, `rebuild` or `recapture` (the capture was not trustworthy).
2. **Four-line read**: what this is for; what works and must stay; what reads generated; what is broken.
3. **Score**: seven dimensions 1 to 10 (Concept, Hierarchy, Craft, Accessibility, Usability, Integrity, Distinctiveness) with one line each, and the overall score with caps applied.
4. **Findings**: 5 to 15, Floor first, then by priority, then by how much of the page they touch. Root causes merged.
5. **Quick wins**: 3 fixes with the best effect per effort.
6. **Keep**: what holds up and must not be diluted by fixes.
7. **Not investigated**: every lens, check or width that did not run, with the reason.
8. **Data gaps**: content the artifact needs that does not exist yet.

## Score caps

- An open Floor finding caps the overall score at 4.
- Concept at 5 or below caps the overall score at 6.
- Straight 9s and 10s must name what was cut to earn them.
