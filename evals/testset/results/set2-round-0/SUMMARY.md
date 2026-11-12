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

## All five phase-2 lenses, blind (10 Nov 2026)

Seven blind reviewers ran `lens-typography`, `lens-color` and `lens-concept` (two reviewers each: P01 to P28 and P29 to P57) and `lens-copy` (one reviewer, all 57) under LENS-BRIEF-PHASE2. The target was withheld. The brief added one line of capture context: each item is one isolated composition, so missing page furniture is the framing. Table: `lens-pairs.md`. Judgments: `../set2-lenses-round-1/` (PNG working files left out).

| Lens | Bad half lower | Ties | Inverts | Where it separates |
|---|---|---|---|---|
| structure | **30 of 32** | 0 | 2 | everywhere |
| concept | 26 of 32 | 5 | 1 | scene 9 of 9, style 7 of 8, composition 10 of 13 |
| typography | 20 of 32 | 12 | 0 | compact-reflow, ui-anatomy, caps, tiny, detail, story-crop, result-weight |
| color | 15 of 32 | 17 | 0 | purple, glow, icons, decorative-noise, surface-contrast, visual-restraint, colored-layers, material-contrast |
| copy | 2 of 32 | 30 | 0 | tile-lead only: the halves of a pair share their words |

- **At least one lens separates every pair: 32 of 32.** Structure's two misses are each caught elsewhere. Concept catches crop-filler (5 against 6) and typography catches detail-copy (6 against 7).
- The mean of the four design lenses separates 30 of 32, with 1 tie (crop-filler) and 1 inversion (detail-copy).
- Only 3 of 160 judgments invert, all on the two pairs where the isolated crop misleads the reviewer. Typography and color never invert: off their own domain they tie and do not guess. That is the behaviour a per-dimension score needs.
- The lenses are specific. Color separates the color faults (purple, glow, onion layers) and ties on spacing. Typography separates the scaled-down and caps faults and ties on scene faults. Copy cannot separate pairs that share copy, which is expected rather than a gap.
- What the lenses add over the sweep: the half-scale transforms (`transform: scale(0.5)` in P25, about 0.62 in P43). The sweep's `text_floor` reads declared sizes, so it missed them, and both typography reviewers flagged them (TYP-135). Candidate detector: measure text size after transforms.

The motion pairs are not in this set yet. Capture now has a passive recording mode (`capture.mjs --passive <ms>`, `01-evidence/passive.json`, read by `motion_snap`) for motion that plays without a click.

## Motion pairs, sweep only (10 Nov 2026)

Stageshow's 22 motion pairs were added as P58 to P101 (44 halves). Each was captured on its own with `--no-interact --passive 6000`, which records every painted box from load with no click (`01-evidence/passive.json`). `motion_snap` reads the result. No lens ran on these halves: the passive recording keeps no stills, so a reviewer would see only the sweep's own numbers.

| Round | Separates | Ties | Good halves hit |
|---|---|---|---|
| First passive capture | 2 of 22 (adjacent-action, surface-resize) | 20 | 0 |
| After the animation-aware shove | **5 of 22** (adjacent-action, drag-offset, horizontal-insert, list-reflow, text-settle) | 17 | 1 (surface-resize) |

- **Animation-aware shove (`interact.mjs`):** the recorder now logs each frame's finite move, size and fade animations (`getAnimations()`, with target boxes). A jump counts as a shove when a nearby element runs one of them on both sides of the jump, or glides on any axis, width and height included. The evidence was list-reflow: its rows jump 34 px while the new row only fades in, and opacity moves no box.
- **New noise:** surface-resize's good half now has 5 hits (text jumps 19 px while the popup animates). Before the change it had none. Tier is Finish. Watch for this on the human controls at the next live recapture.
- **What a box recorder cannot see:** 17 pairs still tie. Their faults are instant swaps (label, identity, exit, press), timing order (interrupt, dependent-starts, spinner-start), edges that slice or fade (label-boundary, viewport-edge), and demos (detail-chart, detail-throw, detail-reaction, detail-pin, reset). These need stills from the passive recording and a motion lens.

### Transform-aware text size

`extract.js` records each text element's rendered-to-layout scale. `text_floor` judges text at its drawn size. When three or more short runs are shrunk below the floor, it reports one `scaled` hit, which counts labels and table cells too. Both bad halves (P25 at `scale(0.5)`, P43 at about 0.62) now carry a `scaled` hit; their good halves (P20, P31) carry none. The hits are Reflex, because CSS-scaled mocks count as incidental (live round 1).

## Motion pairs, lens-motion blind (12 Nov 2026)

The 44 motion halves were recaptured with passive stills: viewport shots over the first 5.5 s, from a separate load. Two blind reviewers then ran `lens-motion` on them. The judgments are in `../set2-motion-lens-round-1/`.

**The lens scores the bad half lower on 17 of 22 pairs**, against 5 of 22 for the passive sweep. It ties on 4 and inverts on 1. Every pair the sweep separates, the lens separates too.

- **What the stills let the lens see:**
  - Label and icon swaps in one frame (label, identity, detail-reaction)
  - A highlight that restarts from its origin (interrupt)
  - Hard clip edges that slice text (label-boundary, viewport-edge)
  - A value cycling with no cause shown (detail-pin)
  - A chart that fades in whole (detail-chart)
  - A press with no response (press)
- **Ties:** dependent-starts (both halves slide a panel sideways for 900 ms), exit (both stages end empty, and the exit falls between stills), space and spinner-start (the fault is in timing that falls between stills).
- **Inversion:** detail-throw (bad 6, good 5). The reviewer read the bad half's swipe as travelling visibly; the fault, a pause at release, is shorter than the gap between stills.
- **Limit:** seven stills over about 5.5 s cannot show faults that last under about 400 ms, or the order of overlapping starts. A denser still series or a short video would close it.
