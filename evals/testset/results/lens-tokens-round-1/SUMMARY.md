# lens-tokens, blind round 1 (13 Nov 2026)

Two blind reviewers ran `lens-tokens` (LENS-BRIEF-PHASE2) on 38 live sites of test set 1 (L04 not verified). The judgments and tokens tables (without PNGs) are in this folder.

| Expected | Sites | Read | Craft score | Mean |
|---|---|---|---|---|
| slop | 14 | 5 made, 9 mixed | 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 9 | 6.4 |
| borderline | 4 | 1 made, 3 mixed | 5, 5, 5, 8 | 5.8 |
| good | 20 | 12 made, 8 mixed | 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8 (×7), 9, null | 6.7 |

- **Tokens does not separate slop from good,** and that is expected. Generated pages are assembled on a framework scale (Tailwind, shadcn) and inherit its tidiness: L01 scored 9 and L03 8. Long-lived human sites drift: L20's stylesheet is about 94% literal, L26 has 705 arbitrary values typed past the Tailwind scale, and L37 stitches a Webflow navbar onto a React app's neutrals. GOV.UK (L32) scored 9, the top, on its 5px spacing and 19/24/36/48 type scales.
- **No `generated` read on any item:** the lens judged system hygiene, as designed.
- **The findings are real and specific.** Examples: half-pixel size ladders (9 to 13px in 0.5 steps), near-black inks a few values apart, two Ant primaries from two major versions on one screen (L33), and dark themes that redefine only some of the semantic tokens.
- **Decision (13 Nov 2026):** like lens-motion, lens-tokens may pull Craft at most 1 point below the weakest visual Craft lens (`CAPPED_CRAFT` in `synthesize.py`). The reasons:
  - Its score carries no slop signal.
  - Taking the lowest score would let token drift on a strong human site outweigh what colour, typography and imagery see.
  - Its findings still appear in full in the report as fixes.
