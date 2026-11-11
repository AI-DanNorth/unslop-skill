# lens-motion, blind round 1 (10 Nov 2026)

Two blind reviewers ran `lens-motion` (LENS-BRIEF-PHASE2) on the 22 live sites in test set 1 where the capture measured motion: L01, L02, L05 to L09, L16 to L18, L20 to L24, L30, L32 and L34 to L38. The captures are from the interaction recapture of 9 Nov 2026. The judgments are in this folder (`<ID>/motion.json`, plus the motion table without PNGs).

## Result

| Expected | Sites | Read | Score (Craft) | Mean |
|---|---|---|---|---|
| slop | 7 | 3 generated, 3 mixed, 1 made | 3, 4, 4, 5, 6, 6, 7 | 5.0 |
| borderline | 4 | 1 generated, 2 mixed, 1 made | 4, 6, 6, null | 5.3 |
| good | 11 | 0 generated, 3 mixed, 8 made | 5, 6, 6, 7, 7, 7, 8, 8, 8, null, null | 6.9 |

- **Precision is high.** "Generated" never lands on a human-made site. The generated reads name real tells: infinite decorative loops showing static content (L01 floating cards, L06 orbs, sheen and shimmer all at once, L17 blobs), and a carousel whose every click starts a 1000 ms full-screen cross-fade (L07).
- **The showpiece judgment works.** L18's sweep hits (790 ms, overshoot, 1095 px of travel on "Deal again") were called fitting, because the visitor starts the deal on purpose. The finding that remains is narrower: the same spring curve also drives hover and the copy check. L20's tab wipe was called a showpiece. That site's lower score (5) comes from 87 blocks rising on scroll.
- **Stillness is not scored.** L16, L32 and L35 change state instantly, and each got `score: null` with a "made" read. That is the designed behaviour: stillness does not raise or lower Craft.
- **The scores separate less than the other lenses'.** The mean gap is 1.9, and the ranges overlap: slop L08 scored 7 and L02 and L05 scored 6, while human-made L20 scored 5 and L24 and L37 scored 6. Motion is a weaker slop signal than structure or colour on these sites. Many generated pages barely animate beyond Tailwind's default transitions, and many human sites use the browser's `ease` (MOT-007 on L21, L34 and L36, Finish only).
- **Calibration to watch:** a MOT-007 "browser default ease" finding on design-system sites (Ant Design, Carbon) cost them nothing (both scored 8). That is right for a Finish card. A future rubric should keep it from capping Craft.

## What it means for synthesize

lens-motion reports on Craft, where synthesize keeps the weakest lens score. A 5 from motion would pull down a site whose colour and typography score 8. Because motion separates less, consider weighting it below the visual lenses in the scoring rubric (roadmap), or capping its pull at one point, before relying on it in the overall score.
