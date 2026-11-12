# lens-robustness, blind round 1 (12 Nov 2026)

Two blind reviewers ran `lens-robustness` (LENS-BRIEF-PHASE2) on 38 live sites of test set 1, using the captures from 9 Nov 2026. L04 was left out because it is not verified. These captures predate the computed `text-overflow` and CLS records, so the table fell back to class rules. The judgments and robustness tables (without PNGs) are in this folder.

## Result

| Expected | Sites | Read | Usability score | Mean |
|---|---|---|---|---|
| slop | 14 | 4 generated, 7 mixed, 3 made | 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 6, 7, 8, 8 | 4.7 |
| borderline | 4 | 3 mixed, 1 made | 4, 4, 6, 7 | 5.2 |
| good | 20 | 10 made, 9 mixed, 1 generated | 3, 3, 4, 5, 5, 5, 6, 6, 6, 7 (×7), 8, 8, 9, 9 | 6.3 |

- **Robustness measures breakage, not authorship,** and it separates least of the lenses (mean gap 1.6, wide overlap). The slop pages fail in the generator's way:
  - no breakpoints, so the page is 694 to 698 px wide at 375 (L12, L13)
  - whole pages blank without script (L03, L05, L08, L09)
  - 22.5 MB of transfer with a 2.4 MB logo shown at 40 px (L07)
- **Human sites also break, and the breaks are real:**
  - a WebGL game with no text or poster fallback (L29)
  - a docs rail that squeezes the article to about 163 px at 375 (L34)
  - a header search that pushes the phone menu off-screen (L37, L38)
  - every store name cut at 375 (L33)
  - a 6.4 s LCP (L28)
  - React hydration errors and no text without script (L36)
- **One misused read.** L34 (a design-system docs page) was read `generated` for one phone layout bug. That is the first `generated` read on a human site in any lens. The SKILL now reserves `generated` for a build never tried beyond its sample as a whole (no breakpoints, the whole page blank without script, every slot fixed). One real bug on a considered build is `mixed`.
- **No cap on its Usability pull, unlike motion.** Motion's low scores on human sites were showpiece timing, a question of taste. Robustness's low scores are defects a visitor meets: an article 163 px wide, a menu off-screen, a page that needs WebGL. synthesize keeps the lowest of lens-components and lens-robustness on Usability, so these defects show in the score. That is intended, and a report should name them as fixes.
- **Capture follow-ups:**
  - Recorded from 12 Nov 2026: `text-overflow`, `overflow-wrap`, min and max width, `flex-wrap`, `object-fit` and CLS.
  - Still missing: a throttled page load and a hostile-content injection pass, so T-STRESS and T-SLOW-LINE can run.
