# lens-dataviz, blind round 1 (12 Nov 2026)

Two blind reviewers ran `lens-dataviz` (LENS-BRIEF-PHASE2) on 20 items where the charts table found real charts, stat tiles or diagrams: 10 local (B07, G01, G12, G13, M01, M03, M07, S09, S10, and I06, which is image-only) and 10 live (L08, L10, L16, L17, L21, L25, L26, L27, L31, L33). The judgments and charts tables (without PNGs) are in this folder.

## Result

| Expected | Items | Read | Craft score |
|---|---|---|---|
| slop | 5 | 3 generated, 1 mixed, 1 made | S10 4, L10 4, S09 5, I06 6, L08 7 |
| borderline | 4 | 2 generated, 2 mixed | M07 3, B07 4, L17 6, L16 7 |
| good | 11 | 5 made, 4 mixed, 2 none | L33 5, G12 6, M01 6, L25 7, G13 8, M03 8, L21 8, L26 8, L27 8, G01 null, L31 null |

- **"Generated" never lands on a good item.** The generated reads name concrete chart lies:
  - a hero "Performance Overview" squiggle with no axis or values (B07)
  - traction bars whose heights do not follow their labels, under a "34% MoM" title the labels contradict (M07)
  - a KPI tile that shows an improvement as a red down arrow (S10)
  - stat bands with no period, scale or source (S09, L10)
- **The answer key's planted fault is caught.** On I06 the reviewer did the arithmetic: 240 + 64 − 36 + 22 − 52 = 238, but the plan bar says 236 (DVZ-005). The lens then scored it 6 rather than low, because a mis-totalled waterfall is otherwise well drawn. The fault is found and named, but the score barely reflects it, and the error is one of integrity as much as craft.
- **Real faults inside good artifacts:**
  - G12 and M01 draw bars from a hidden, cut baseline (the first bar is 54% of the last instead of 78%; 53% against 85% drawn from about 23%).
  - L33's template ranks seven stores that all read 323,234 (random mock data).

  These are true findings on artifacts that are good overall. The lens judges the charts, not the page.
- **No charts, no score:** G01 and L31 have no chart to judge and got `null` with `overall_read: "none"`, as designed.
- **Capture limits:**
  - Series colours are read from pixels.
  - Connectors are judged only from straight bounding-box segments.
  - Canvas classes are guesses, and the reviewers confirmed each one on its crop (L26's nine canvases are photos and textures).
  - Image charts with plain alt text are missed by the matcher. They are listed as unmatched large images so the reviewer looks once.
