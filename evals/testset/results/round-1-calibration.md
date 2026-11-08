# Calibration: Test set 1

Verdict agreement on clear-cut items: **23/44**. Borderline items are reported but not scored.
False positives (good flagged as slop): 4. Misses (slop not flagged): 6.

| Item | Expected | Unslop | Slop lens read | Look families | Slop-type Reflex | Floor | Lens findings | Medium |
|---|---|---|---|---|---|---|---|---|
| S01 | slop | slop | generated (high) | - | 7 | 5 | 13 | web |
| S02 | slop | slop | generated (high) | warm-paper-serif | 11 | 4 | 13 | web |
| S03 | slop | slop | generated (high) | violet-gradient | 32 | 16 | 12 | web |
| S04 | slop | slop | generated (medium) | saas-card-kit | 10 | 4 | 5 | web |
| S05 | slop | slop | generated (high) | - | 9 | 19 | 10 | web |
| S06 | slop | slop | generated (high) | saas-card-kit | 5 | 17 | 10 | app |
| S07 | slop | slop | generated (high) | warm-paper-serif | 7 | 11 | 14 | web |
| S08 | slop | slop | generated (high) | - | 8 | 5 | 12 | web |
| S09 | slop | slop | generated (high) | - | 12 | 4 | 11 | web |
| S10 | slop | slop | generated (medium) | - | 5 | 1 | 11 | app |
| S11 | slop | slop | generated (high) | - | 2 | 4 | 9 | web |
| S12 | slop | borderline ✗ | mixed (low) | - | 0 | 11 | 10 | web |
| S13 | slop | slop | generated (low) | - | 0 | 2 | 11 | social |
| G01 | good | good | made (medium) | - | 1 | 0 | 6 | web |
| G02 | good | good | made (high) | - | 8 | 7 | 6 | web |
| G03 | good | good | made (medium) | - | 2 | 1 | 6 | web |
| G04 | good | good | made (medium) | - | 2 | 3 | 5 | web |
| G05 | good | borderline ✗ | mixed (medium) | - | 3 | 1 | 8 | web |
| G06 | good | slop ✗ | generated (high) | warm-paper-serif,hairline-newspaper | 23 | 20 | 15 | web |
| G07 | good | borderline ✗ | mixed (medium) | - | 5 | 0 | 10 | app |
| G08 | good | borderline ✗ | mixed (medium) | - | 0 | 3 | 6 | web |
| G09 | good | borderline ✗ | mixed (medium) | - | 4 | 0 | 9 | web |
| G10 | good | borderline ✗ | mixed (low) | - | 0 | 11 | 10 | web |
| G11 | good | borderline ✗ | mixed (low) | - | 0 | 2 | 3 | social |
| G12 | good | borderline ✗ | mixed (medium) | - | 11 | 1 | 11 | app |
| G13 | good | borderline ✗ | mixed (medium) | - | 1 | 2 | 9 | diagram |
| B01 | borderline | slop | generated (high) | - | 6 | 2 | 10 | web |
| B02 | borderline | slop | generated (high) | violet-gradient | 19 | 26 | 11 | web |
| B03 | borderline | slop | generated (high) | - | 14 | 26 | 13 | web |
| B04 | good | slop ✗ | generated (high) | warm-paper-serif | 12 | 25 | 13 | web |
| B05 | borderline | slop | generated (high) | dark-single-accent | 14 | 23 | 14 | web |
| B06 | good | slop ✗ | generated (medium) | - | 9 | 14 | 13 | web |
| B07 | borderline | slop | generated (high) | - | 2 | 22 | 12 | web |
| B08 | good | slop ✗ | generated (high) | - | 3 | 19 | 12 | web |
| C01 | slop | borderline ✗ | mixed (medium) | - | 2 | 0 | 8 | app |
| C02 | slop | slop | generated (high) | - | 4 | 1 | 6 | app |
| C03 | slop | slop | generated (high) | - | 1 | 1 | 5 | app |
| C04 | slop | slop | generated (high) | - | 10 | 0 | 7 | app |
| M01 | good | good | made (medium) | - | 20 | 6 | 10 | slides |
| M02 | good | borderline ✗ | mixed (medium) | - | 5 | 0 | 8 | print |
| M03 | good | good | made (high) | - | 2 | 0 | 7 | print |
| M04 | good | good | made (medium) | - | 0 | 1 | 5 | social |
| M05 | borderline | borderline | mixed (medium) | - | 3 | 9 | 9 | slides |
| M06 | good | borderline ✗ | mixed (medium) | - | 2 | 11 | 9 | slides |
| M07 | borderline | slop | generated (medium) | saas-card-kit | 41 | 6 | 11 | slides |
| M08 | borderline | slop | generated (medium) | - | 3 | 8 | 9 | email |
| I01 | slop | borderline ✗ | mixed (medium) | - | 0 | 0 | 8 | web |
| I02 | slop | borderline ✗ | mixed (medium) | - | 0 | 0 | 8 | web |
| I03 | slop | good ✗ | made (medium) | - | 0 | 0 | 8 | web |
| I04 | slop | slop | generated (high) | - | 0 | 0 | 12 | web |
| I05 | good | borderline ✗ | mixed (medium) | - | 0 | 0 | 9 | web |
| I06 | slop | borderline ✗ | mixed (medium) | - | 0 | 0 | 7 | diagram |

## Detector discrimination

Share of items each detector fired on, by expected label. A detector that fires as often on good items as on slop does not separate them; one that fires on good controls is a false-positive candidate.

| Detector | slop | borderline | good | Read |
|---|---|---|---|---|
| flat_hierarchy | 59% | 12% | 14% | separates |
| headings_landmarks | 76% | 62% | 43% | separates |
| gradient | 24% | 38% | 0% |  |
| lexicon_copy | 41% | 25% | 19% |  |
| look_family | 29% | 38% | 10% |  |
| banned_fonts | 53% | 62% | 33% |  |
| spacing_monotony | 24% | 0% | 5% |  |
| fallback_face | 18% | 0% | 0% | rare |
| card_kit | 18% | 38% | 5% | rare |
| form_labels | 12% | 0% | 0% | rare |
| reduced_motion | 12% | 12% | 0% | rare |
| overflow | 35% | 25% | 24% |  |
| invented_metrics | 18% | 12% | 10% | rare |
| motion_css | 18% | 25% | 10% | rare |
| side_tab_border | 6% | 12% | 0% | rare |
| glow | 6% | 25% | 0% | rare |
| control_names | 6% | 0% | 0% | rare |
| default_names | 29% | 12% | 24% |  |
| accent_footprint | 12% | 12% | 10% | rare |
| lang_and_title | 12% | 12% | 10% | rare |
| contrast | 29% | 62% | 29% |  |
| neon_violet | 0% | 12% | 0% | rare |
| dead_band | 24% | 38% | 24% |  |
| chrome_glyphs | 18% | 50% | 19% | rare |
| stock_swatches | 6% | 0% | 10% | rare |
| hidden_content | 6% | 0% | 10% | rare |
| numbered_labels | 0% | 0% | 5% | rare |
| heading_rhythm | 0% | 12% | 5% | rare |
| h1_words | 0% | 0% | 5% | rare |
| phone_parity | 0% | 0% | 5% | rare |
| widows | 65% | 62% | 71% | fires on good too |
| eyebrow | 0% | 38% | 10% | rare |
| container_monotony | 0% | 0% | 10% | rare |
| words_per_screen | 0% | 12% | 10% | rare |
| targets | 47% | 62% | 57% | fires on good too |
| focus_ring | 35% | 38% | 48% | fires on good too |
| em_dash | 6% | 62% | 19% | rare |
| repeated_label | 18% | 50% | 33% | fires on good too |
| off_scale_spacing | 0% | 25% | 19% | rare |
| text_floor | 35% | 88% | 62% | fires on good too |
| type_ladder | 29% | 88% | 57% | fires on good too |
