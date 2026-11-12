# lens-imagery, blind round 1 (12 Nov 2026)

Two blind reviewers ran `lens-imagery` (LENS-BRIEF-PHASE2) on 38 live sites of test set 1, using the captures from 9 Nov 2026. L04 was left out because it is not verified. The judgments and imagery tables (without PNGs) are in this folder.

## Result

| Expected | Sites | Read | Craft score | Mean |
|---|---|---|---|---|
| slop | 14 | 7 generated, 4 mixed, 3 made | 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, null | 4.8 |
| borderline | 4 | 2 mixed, 2 made | 5, 6, 7, null | 6.0 |
| good | 20 | 18 made, 2 mixed | 6, 6, 7 (×5), 8 (×10), 9, 9, null | 7.6 |

- **Imagery separates best of the four lenses built this week.** The mean gap is 2.8. "Generated" never lands on a human site. The overlap is small: two slop pages with real product material (L08's labelled example diagram, L09's real capture) score 7, and the lowest human scores are 6.
- **The generated reads rest on pictures that stand in for the product:**
  - glow fields as hero art, with no picture at all (L12, L13, L17)
  - HTML windows with drawn traffic lights posing as product shots (L06, L14)
  - invented letter tiles in place of real tools' logos (L02, L03, L05)
  - a generated team photo with the brand printed on the laptop (L06)
  - a generative particle sphere when the platform is never shown (L10)
- **Findings on human sites are about treatment, not material:**
  - Captures shown too small to read (L21, L22, L24, L31) or upscaled (L37, L38).
  - Mixed icon strokes (L25, L26). These support the sweep's `mixed_icons` hits on those controls as real but minor.
  - Untranslated labels baked into figures (L34).
- **No imagery:** L15, L16 and L35 have no imagery worth judging and got `score: null`, as designed.
- **Capture limits:** `object-fit` and `object-position` are inferred from class names; video and iframe sources are not captured; lazy images that never loaded are "not verified" (L28: 67).

## Image-only items (I01 to I06)

Each item's image was placed in `01-evidence/` (`image.webp` or `image.png`), with a manifest saying it is image-only: no DOM, no interaction, no other width, target withheld. A third blind reviewer ran the lens's image-only mode on them.

| Item | Expected | Read | Score | Note |
|---|---|---|---|---|
| I04 | slop | generated | 3 | Skeleton dashboard with unlabelled gradient bars; deleting it loses nothing |
| I05 | good (the fix of I04) | mixed | 6 | The logo row is typed placeholder names; the cohort chart is a strength |
| I01, I02, I03 | slop | made | 7 each | Their faults are layout and copy, not pictures; imagery is the wrong lens for them |
| I06 | slop (numbers wrong) | made | null | The only picture is a data chart. The reviewer still found the planted fault (240 + 64 - 36 + 22 - 52 = 238, the end bar says 236) and handed it to lens-dataviz |

