# lens-components, blind round 1 (12 Nov 2026)

Three blind reviewers ran `lens-components` (LENS-BRIEF-PHASE2) on 38 live sites of test set 1, using the captures from 9 Nov 2026. L04 was left out because it is not verified. The judgments and components tables (without PNGs) are in this folder.

## Result

| Expected | Sites | Read | Usability score | Mean |
|---|---|---|---|---|
| slop | 14 | 5 generated, 8 mixed, 1 made | 3, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 7, 7, 8 | 5.3 |
| borderline | 4 | 3 mixed, 1 made | 5, 5, 7, null | 5.7 |
| good | 20 | 12 made, 8 mixed | 5, 6, 6, 6, 7 (×9), 8 (×7), 9 | 7.2 |

- **"Generated" never lands on a human site.** The generated reads rest on things the capture shows:
  - every header item pointing to `#` (L12, L13; 18 dead links on L10)
  - sign-up buttons that only jump to an in-page anchor (L14)
  - a carousel drawn over its own buy buttons (L11)
  - an operator UI whose active filters look like their neighbours (L15)
- **Human-made sites get real, small findings,** and a few real bugs:
  - L37 and L38's navbar pushes the phone menu button off-screen (the page is 383 px wide at 375).
  - L34's anchor rail squeezes the article to 170 px at 375.
  - L23's and L27's menus stay open after Escape.
  - L26's field is labelled by placeholder only.

  The low human scores are evidence, not taste.
- **Separation is moderate.** The mean gap is 1.9 and the ranges overlap: slop L08 scores 8 and five slop sites score 7. Generated pages built from a component kit often carry the kit's states intact, so component craft separates less than structure or colour. GOV.UK (L32) scored 9, the top score: its kit is used as it ships, with the full state set.
- **What the capture limits:**
  - The current-page mark is inferred, because the DOM does not record `aria-current`, `aria-expanded`, `disabled`, `required` or `aria-invalid`.
  - Escape-close comes from the motion run's reset.
  - Nothing types invalid input, so inline validation is not investigated.
  - Phone menus are not opened.

  Recording those attributes in `extract.js` is the next capture change.
