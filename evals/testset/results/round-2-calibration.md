# Calibration: Test set 1

Verdict agreement on clear-cut items: **26/44**. Borderline items are reported but not scored.
False positives (good flagged as slop): 6. Misses (slop not flagged): 5.

| Item | Expected | Unslop | Slop lens read | Look families | Slop-type Reflex | Floor | Lens findings | Medium |
|---|---|---|---|---|---|---|---|---|
| S01 | slop | slop | generated (high) | - | 16 | 8 | 13 | web |
| S02 | slop | slop | generated (high) | warm-paper-serif | 21 | 5 | 12 | web |
| S03 | slop | slop | generated (high) | violet-gradient | 43 | 16 | 12 | web |
| S04 | slop | slop | generated (medium) | saas-card-kit | 11 | 1 | 5 | web |
| S05 | slop | slop | generated (high) | - | 14 | 18 | 12 | web |
| S06 | slop | slop | generated (high) | saas-card-kit | 10 | 17 | 11 | app |
| S07 | slop | slop | generated (high) | warm-paper-serif | 11 | 13 | 12 | web |
| S08 | slop | slop | generated (high) | violet-gradient | 17 | 14 | 12 | web |
| S09 | slop | slop | generated (high) | - | 25 | 21 | 11 | web |
| S10 | slop | slop | generated (high) | - | 9 | 10 | 15 | app |
| S11 | slop | slop | generated (high) | - | 2 | 4 | 9 | web |
| S12 | slop | borderline ✗ | mixed (medium) | - | 0 | 10 | 11 | web |
| S13 | slop | slop | generated (low) | - | 0 | 2 | 8 | social |
| G01 | good | good | made (medium) | - | 1 | 0 | 9 | web |
| G02 | good | good | made (medium) | - | 8 | 2 | 7 | web |
| G03 | good | good | made (medium) | - | 2 | 1 | 7 | web |
| G04 | good | good | made (medium) | - | 2 | 3 | 5 | web |
| G05 | good | borderline ✗ | mixed (medium) | - | 13 | 1 | 7 | web |
| G06 | good | slop ✗ | generated (high) | warm-paper-serif,hairline-newspaper | 30 | 20 | 13 | web |
| G07 | good | borderline ✗ | mixed (medium) | - | 9 | 0 | 11 | app |
| G08 | good | borderline ✗ | mixed (medium) | - | 0 | 7 | 9 | web |
| G09 | good | borderline ✗ | mixed (medium) | - | 4 | 0 | 11 | web |
| G10 | good | borderline ✗ | mixed (medium) | - | 0 | 10 | 11 | web |
| G11 | good | slop ✗ | generated (low) | - | 0 | 2 | 3 | social |
| G12 | good | borderline ✗ | mixed (medium) | - | 13 | 1 | 11 | app |
| G13 | good | good | made (medium) | - | 1 | 1 | 7 | diagram |
| B01 | borderline | slop | generated (high) | - | 10 | 4 | 11 | web |
| B02 | borderline | slop | generated (high) | violet-gradient | 24 | 18 | 13 | web |
| B03 | borderline | slop | generated (medium) | - | 19 | 15 | 13 | web |
| B04 | good | slop ✗ | generated (high) | warm-paper-serif | 17 | 18 | 15 | web |
| B05 | borderline | slop | generated (high) | dark-single-accent | 22 | 17 | 12 | web |
| B06 | good | slop ✗ | generated (high) | - | 13 | 8 | 12 | web |
| B07 | borderline | slop | generated (high) | - | 3 | 26 | 11 | web |
| B08 | good | slop ✗ | generated (high) | - | 5 | 26 | 11 | web |
| C01 | slop | borderline ✗ | mixed (medium) | - | 2 | 0 | 7 | app |
| C02 | slop | slop | generated (high) | - | 7 | 1 | 5 | app |
| C03 | slop | slop | generated (medium) | - | 1 | 1 | 4 | app |
| C04 | slop | slop | generated (medium) | - | 10 | 0 | 6 | app |
| M01 | good | good | made (medium) | - | 27 | 5 | 10 | slides |
| M02 | good | borderline ✗ | mixed (medium) | - | 6 | 0 | 11 | print |
| M03 | good | good | made (high) | - | 5 | 0 | 5 | print |
| M04 | good | good | made (medium) | - | 0 | 0 | 4 | social |
| M05 | borderline | borderline | mixed (medium) | - | 5 | 9 | 11 | slides |
| M06 | good | good | made (medium) | - | 3 | 11 | 9 | slides |
| M07 | borderline | slop | generated (high) | saas-card-kit | 53 | 6 | 10 | slides |
| M08 | borderline | borderline | mixed (medium) | - | 6 | 8 | 9 | email |
| I01 | slop | borderline ✗ | mixed (medium) | - | 0 | 0 | 7 | web |
| I02 | slop | borderline ✗ | mixed (medium) | - | 0 | 0 | 7 | web |
| I03 | slop | slop | generated (medium) | - | 0 | 0 | 8 | web |
| I04 | slop | slop | generated (high) | - | 0 | 0 | 12 | web |
| I05 | good | slop ✗ | generated (high) | - | 0 | 0 | 9 | web |
| I06 | slop | good ✗ | made (medium) | - | 0 | 0 | 5 | diagram |

## Detector discrimination

Share of items each detector fired on, by expected label. A detector that fires as often on good items as on slop does not separate them; one that fires on good controls is a false-positive candidate.

| Detector | slop | borderline | good | Read |
|---|---|---|---|---|
| banned_fonts | 71% | 62% | 33% | separates |
| headings_landmarks | 76% | 62% | 43% | separates |
| flat_hierarchy | 47% | 12% | 14% | separates |
| motion_css | 35% | 25% | 10% |  |
| look_family | 35% | 38% | 10% |  |
| gradient | 24% | 38% | 0% |  |
| emoji_icons | 24% | 0% | 0% |  |
| lexicon_copy | 47% | 25% | 24% |  |
| stock_swatches | 35% | 0% | 14% |  |
| spacing_monotony | 24% | 0% | 5% |  |
| contrast | 47% | 62% | 29% |  |
| fallback_face | 18% | 0% | 0% | rare |
| card_kit | 18% | 38% | 5% | rare |
| form_labels | 12% | 0% | 0% | rare |
| reduced_motion | 12% | 12% | 0% | rare |
| overflow | 35% | 25% | 24% |  |
| invented_metrics | 24% | 25% | 14% |  |
| stat_band | 35% | 75% | 29% |  |
| side_tab_border | 6% | 12% | 0% | rare |
| glow | 6% | 25% | 0% | rare |
| control_names | 6% | 0% | 0% | rare |
| default_names | 29% | 12% | 24% |  |
| accent_footprint | 12% | 12% | 10% | rare |
| lang_and_title | 12% | 12% | 10% | rare |
| heading_rhythm | 6% | 12% | 5% | rare |
| placeholder_residue | 6% | 12% | 5% | rare |
| neon_violet | 0% | 12% | 0% | rare |
| words_per_screen | 6% | 12% | 10% | rare |
| chrome_glyphs | 29% | 75% | 33% | fires on good too |
| numbered_labels | 0% | 0% | 5% | rare |
| h1_words | 0% | 0% | 5% | rare |
| phone_parity | 0% | 0% | 5% | rare |
| dead_band | 18% | 25% | 24% | rare |
| widows | 65% | 62% | 71% | fires on good too |
| eyebrow | 0% | 38% | 10% | rare |
| container_monotony | 0% | 0% | 10% | rare |
| targets | 47% | 62% | 57% | fires on good too |
| focus_ring | 35% | 38% | 48% | fires on good too |
| em_dash | 6% | 62% | 19% | rare |
| repeated_label | 18% | 50% | 33% | fires on good too |
| off_scale_spacing | 0% | 25% | 19% | rare |
| text_floor | 41% | 88% | 62% | fires on good too |
| type_ladder | 35% | 88% | 57% | fires on good too |
