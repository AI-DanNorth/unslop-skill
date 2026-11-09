# Phase 2, round 1: five new judgment lenses

Each lens was built (`skills/lens-<name>/SKILL.md`, 17 to 23 cards promoted from drafts with their sources kept, new named tests), then run blind by a fresh reviewer with `evals/testset/LENS-BRIEF-PHASE2.md` on the same 8 live items. The reviewers did not see each other's lens files or the labels. Scored with `evals/testset/calibrate_lens.py`. Per-lens tables are in `<lens>-calibration.md`, and lens files in `<ID>/`.

Items: L03 Bolt, L10 Optimus, L13 impeccable specimen, L06 Consile (slop); L23 Anthropic, L25 Linear, L32 GOV.UK, L35 Vercel guidelines (good).

| Lens | Dimension | Verdict agreement | Mean score, slop | Mean score, good | Overlap |
|---|---|---|---|---|---|
| concept | Concept | 7/8 | 2.8 (1-5) | 8.5 (8-9) | none |
| structure | Hierarchy | 8/8 | 4.2 (4-5) | 7.5 (7-8) | none |
| typography | Craft | 7/8 | 4.0 (3-5) | 8.0 (7-9) | none |
| color | Craft | 6/8 | 4.8 (3-7) | 8.8 (8-9) | none |
| copy | Distinctiveness | 7/8 | 3.0 (1-5) | 8.2 (7-9) | none |

Every lens's scores separate the 4 slop items from the 4 good ones with no overlap. The disagreements are reads of "mixed" or "made" on slop items, not false alarms on the human sites:
- **L06 (Consile)** reads mixed on concept, colour and copy. A real product dashboard sits in the hero, and the rest of the page is a stock template. That is a fair "mixed".
- **L10 (Optimus)** reads mixed on typography and made on colour (Craft 7). Its near-monochrome palette really is restrained. The colour lens judges the palette, not the whole page, and other lenses carry the slop call (concept 3, copy 2, structure 4).

No good item was read as generated or mixed by any lens.

## Fixes made during the round
- `palette_table.py` (colour): crashed on L25 and L32 (a leftover colour variable). Text greys now include slate/gray tints up to C 0.05, and `colorlib.parse` reads CSS `lab()`/`lch()` (L10).
- `copy_sheet.py` (copy): read only an element's own text, so headings built from spans gave no h1 on L10, L23, L25 and L06. It now uses `blockText`.
- `lens-structure`: the squint render goes to `03-lenses/squint/`, never `01-evidence/`.
- `build_rules.py`: fails on a card key with no value. Five curated titles with unquoted commas had been split.

## Limits
- 8 items, one reviewer per lens and one round. The numbers show the lenses work as designed, not their accuracy at scale.
- All 8 items are web pages. The lenses' notes for slides, print, email and diagrams are untested.
- Dark mode is not captured, so colour's T-DARK-MODE is "not verified" on every item.
- Wiring is still to do: `synthesize` takes each lens's `score` for its report dimension, but `intake` still runs only `slop` and `a11y` by default.
