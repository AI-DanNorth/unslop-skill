# Test set 2, round 0: mechanical sweep on Stageshow's teaching pairs (9 Nov 2026)

Set: `evals/testset/set2.yaml`, 57 halves of 32 pairs (8 style, 13 composition, 9 scene, 2 detail), each pair the same scene with one fault on the bad half. Captured one half at a time with `--isolate` (the other half and the captions removed from the DOM) and `--withhold-target`, at 375 and 1440, without interaction capture. No lens has run yet: this round scores the sweep only. Full table: `mechanical-pairs.md` (from `evals/testset/calibrate_pairs.py`).

## Result

The sweep scores the bad half worse on **18 of 32** pairs. It ties on 5 and inverts on 9 (weighted score: Floor 5, Reflex 2, Finish 1).

| Group | Separates | What the sweep sees |
|---|---|---|
| Style (AI tells and type size) | **7 of 8** | The right detector fires on the bad half: `ai_sparkle` (sparkle), `glow` (glow), `gradient` (purple), `text_floor` (tiny type), `chrome_glyphs` (capitals, over-detailed). The miss is style-onion: translucent icon ink has no detector. |
| Composition | 7 of 13 | `mixed_icons` now catches icon-consistency (1 px and 2.2 px strokes in one list), and `glow`/`gradient` catch decorative-noise. Spacing, edges and anatomy faults are below what a page-level sweep measures. |
| Scene | 4 of 9 | Framing, crop, weight and lead faults are judgment calls: they belong to the lenses (structure, imagery once built). |
| Detail | 0 of 2 | Same. |

## What the round changed

- `mixed_icons` and `ai_sparkle` ignored every `aria-hidden` icon: `extract.js` folds aria-hidden into `inDialog`, and the detectors filtered on it. Fixed. Seeds are now aria-hidden, so the self-test guards the case.
- `mixed_icons` gained a stroke-width check (3+ glyphs in a group whose outline widths differ by 1.3x or more), from the icon-consistency pair.

## Noise the pairs expose

Detectors that fire only on good halves: `contrast` 2, `default_names` 2, `text_floor` 2, `nested_radius` 2 and singles. Most is harness noise: the playground's own labels and names. Not tuned on this round; compare with the human controls after the live recapture first.

## Next

Run the phase-2 lenses (structure, typography, color, concept) blind on the pairs and score them with `calibrate_pairs.py --lens ...`. The composition and scene pairs are where a lens has to beat the sweep.

## Lens-structure, blind (9 Nov 2026)

Three blind reviewers ran `lens-structure` on all 57 halves (LENS-BRIEF-PHASE2, target withheld). Table: `structure-pairs.md`; the lens files are in each run's `03-lenses/structure.json`.

**The lens scores the bad half lower on 30 of 32 pairs** (no ties), against 18 of 32 for the sweep. It gets 21 of 22 composition and scene pairs, where the sweep gets 11.

| Group | Sweep separates | Lens separates |
|---|---|---|
| Style | 7 of 8 | 8 of 8 |
| Composition | 7 of 13 | 13 of 13 |
| Scene | 4 of 9 | 8 of 9 |
| Detail | 0 of 2 | 1 of 2 |

The two misses:
- crop-filler (P21 bad 8, P42 good 7). The reviewer named the fault ("4.2 MB" cut to "4.2" at the frame edge) as a finding, but still scored the bad half 8. The good half lost a point for a 375 overflow. This is a calibration slip in the score, not a blind spot.
- detail-copy (P44 bad 7, P09 good 6). The reviewer found the truncated email chip on the bad half, but marked the good half down for having no title or action. That is the harness crop, not the design.

The lens and the sweep complement each other: the sweep is strongest where the lens is weakest (named AI tells), and the lens sees what geometry cannot (focus, crop, competing windows).
