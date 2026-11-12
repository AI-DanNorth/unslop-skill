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

## Writing style (findings and reports)

An audit that flags generated prose must not read like generated prose. Lenses and `synthesize` write `evidence`, `why`, the four-line read and every report line to these rules:

- **Name the mechanism or the number, not the feeling.** Write "body text is #9ca3af on #ffffff, 2.5:1, needs 4.5:1", not "the text feels faint". If a line could appear unchanged in another audit, it says nothing about this artifact. Cut it.
- **Active voice, with the actor named.** Write "the hero CTA hides the focus ring", not "focus is hidden".
- **Whole sentences.** Keep the articles and verbs, and spell out arrows and abbreviations. Write "the h1 wraps to four lines at 375", not "h1 → 4 lines @375".
- **Plain words.** Use "use", not "leverage"; "help", not "facilitate"; "many", not "numerous". Avoid metaphor nouns such as landscape, north star, surface or bedrock.
- **One idea per sentence.** Split any sentence the reader has to parse twice.
- **No chatbot or filler phrases.** No "Great question", "I hope this helps", "It is important to note that", "in order to", or generic closers. No hedging stacks: "may" is enough.
- **No inline-header lists.** "**Contrast:** the contrast is low" restates itself. A bold lead-in is fine when it names the item and the text after it adds new detail.
- **Sentence-case headings, no decorative emoji.**

Source: an external "unslop" writing skill reviewed 9 Nov 2026 (`research/notes/unslop-writing-skill-review.md`). These rules govern Unslop's own output. They are not detectors for audited pages.

## Score caps

- An open Floor finding caps the overall score at 4.
- Concept at 5 or below caps the overall score at 6.
- Straight 9s and 10s must name what was cut to earn them.

## Disputing a sweep Floor

A lens may dispute a sweep Floor in its own domain by listing it under `disputes` in its output: `detector`, `where` (a substring of the hit's `where` or `evidence`), `evidence` you can point to (a linked case study, an "Ad" label, a fixture or example label, a tile path and region) and `reason`. `synthesize.py` demotes each matching Floor to Reflex and records `disputed_by` on the finding. It never drops the finding, and it ignores a dispute with no evidence or one from a lens that does not own the rule's domain (integrity D18, a11y D10, copy D11, color D06, typography D05, structure D07, concept D02, motion D09, slop D03, components D08, imagery D13, dataviz D12, robustness D15). Dispute only what the page itself shows to be true; suspicion is not evidence. (Owner decision, 11 Nov 2026, from lens-integrity round 1.)
