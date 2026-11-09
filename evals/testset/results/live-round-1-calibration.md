# Calibration: Test set 1 (live)

Not verified, so not scored: L04 (see the capture notes).
Verdict agreement on clear-cut items: **27/34**. Borderline items are reported but not scored.
False positives (good flagged as slop): 2. Misses (slop not flagged): 1.

| Item | Expected | Unslop | Slop lens read | Look families | Slop-type Reflex | Floor | Lens findings | Medium |
|---|---|---|---|---|---|---|---|---|
| L01 | slop | slop | generated (high) | - | 7 | 11 | 12 | web |
| L02 | slop | slop | generated (high) | - | 7 | 3 | 11 | web |
| L03 | slop | slop | generated (high) | saas-card-kit | 30 | 14 | 10 | web |
| L04 | slop | not verified | - | - | 0 | 0 | 0 | web |
| L05 | slop | slop | generated (medium) | warm-paper-serif | 24 | 12 | 12 | web |
| L06 | slop | slop | generated (high) | saas-card-kit | 46 | 19 | 13 | web |
| L07 | slop | slop | generated (medium) | dark-single-accent | 36 | 34 | 13 | web |
| L08 | slop | slop | mixed (medium) | warm-paper-serif | 12 | 3 | 9 | web |
| L09 | slop | slop | mixed (medium) | dark-single-accent | 30 | 28 | 9 | web |
| L10 | slop | slop | generated (high) | hairline-newspaper | 17 | 35 | 14 | web |
| L11 | slop | slop | mixed (medium) | violet-gradient | 12 | 28 | 11 | web |
| L12 | slop | slop | generated (high) | violet-gradient | 43 | 16 | 12 | web |
| L13 | slop | slop | generated (high) | warm-paper-serif | 35 | 4 | 10 | web |
| L14 | slop | slop | generated (high) | - | 11 | 3 | 10 | web |
| L15 | slop | good ✗ | made (medium) | - | 4 | 2 | 8 | app |
| L16 | borderline | borderline | mixed (medium) | - | 9 | 2 | 9 | app |
| L17 | borderline | slop | generated (medium) | saas-card-kit,violet-gradient | 65 | 25 | 11 | web |
| L18 | good | good | made (medium) | - | 7 | 3 | 8 | web |
| L19 | good | borderline ✗ | made (medium) | dark-single-accent,violet-gradient | 60 | 18 | 6 | web |
| L20 | good | slop ✗ | mixed (medium) | violet-gradient | 48 | 24 | 10 | web |
| L21 | good | slop ✗ | mixed (medium) | warm-paper-serif,hairline-newspaper | 18 | 2 | 9 | diagram |
| L22 | borderline | borderline | mixed (medium) | - | 14 | 22 | 9 | slides |
| L23 | good | good | made (high) | - | 4 | 10 | 6 | web |
| L24 | good | borderline ✗ | made (medium) | violet-gradient | 29 | 8 | 8 | web |
| L25 | good | borderline ✗ | made (high) | violet-gradient | 56 | 29 | 6 | web |
| L26 | good | good | made (medium) | - | 64 | 18 | 10 | web |
| L27 | good | borderline ✗ | made (high) | violet-gradient | 39 | 39 | 7 | web |
| L28 | good | good | made (high) | - | 2 | 25 | 7 | web |
| L29 | good | good | made (low) | - | 0 | 1 | 3 | web |
| L30 | good | good | made (high) | - | 0 | 12 | 4 | web |
| L31 | good | good | made (high) | - | 0 | 29 | 8 | web |
| L32 | good | good | made (high) | - | 7 | 1 | 4 | web |
| L33 | good | good | made (medium) | - | 5 | 36 | 6 | app |
| L34 | good | good | made (high) | - | 8 | 48 | 4 | web |
| L35 | good | good | made (high) | - | 4 | 15 | 3 | web |
| L36 | good | good | made (high) | - | 1 | 13 | 6 | web |
| L37 | good | good | made (high) | - | 43 | 31 | 5 | web |
| L38 | borderline | good | made (high) | - | 43 | 30 | 5 | web |
| L39 | good | good | made (high) | - | 26 | 16 | 3 | web |

## Detector discrimination

Share of items each detector fired on, by expected label. A detector that fires as often on good items as on slop does not separate them; one that fires on good controls is a false-positive candidate.

| Detector | slop | borderline | good | Read |
|---|---|---|---|---|
| look_family | 71% | 25% | 30% | separates |
| stock_swatches | 50% | 75% | 10% | separates |
| contrast | 93% | 100% | 60% | separates |
| glow | 43% | 25% | 15% |  |
| default_names | 36% | 0% | 10% |  |
| overflow | 29% | 25% | 5% |  |
| text_floor | 93% | 75% | 70% |  |
| banned_fonts | 43% | 50% | 20% |  |
| chrome_glyphs | 57% | 50% | 35% |  |
| emoji_icons | 21% | 0% | 0% |  |
| icon_tile | 21% | 25% | 5% |  |
| widows | 86% | 50% | 70% |  |
| lexicon_copy | 64% | 75% | 50% | fires on good too |
| numbered_labels | 14% | 25% | 0% | rare |
| type_ladder | 79% | 75% | 65% | fires on good too |
| heading_rhythm | 21% | 0% | 10% |  |
| em_dash | 21% | 25% | 10% |  |
| flat_hierarchy | 36% | 50% | 25% |  |
| targets | 100% | 75% | 90% | fires on good too |
| words_per_screen | 64% | 25% | 55% | fires on good too |
| eyebrow | 14% | 0% | 5% | rare |
| motion_css | 79% | 100% | 70% | fires on good too |
| gradient | 43% | 50% | 35% | fires on good too |
| nested_cards | 21% | 0% | 15% |  |
| invented_metrics | 21% | 25% | 15% |  |
| card_kit | 36% | 25% | 30% | fires on good too |
| neon_violet | 7% | 0% | 5% | rare |
| spacing_monotony | 7% | 0% | 5% | rare |
| reduced_motion | 29% | 25% | 30% | fires on good too |
| headings_landmarks | 79% | 50% | 80% | fires on good too |
| stat_band | 7% | 50% | 10% | rare |
| hidden_content | 57% | 75% | 60% | fires on good too |
| side_tab_border | 0% | 0% | 5% | rare |
| container_monotony | 14% | 25% | 20% | rare |
| accent_footprint | 7% | 25% | 15% | rare |
| zoom_blocked | 7% | 0% | 15% | rare |
| phone_parity | 21% | 50% | 30% | fires on good too |
| lang_and_title | 0% | 0% | 10% | rare |
| repeated_label | 43% | 25% | 55% | fires on good too |
| img_alt | 0% | 0% | 15% | rare |
| control_names | 14% | 0% | 30% | fires on good too |
| performance | 43% | 25% | 60% | fires on good too |
| form_labels | 7% | 0% | 25% | rare |
| dead_band | 21% | 25% | 40% | fires on good too |
| placeholder_residue | 0% | 0% | 20% | rare |
| page_words | 21% | 25% | 45% | fires on good too |
| focus_ring | 64% | 75% | 95% | fires on good too |
| fallback_face | 7% | 25% | 45% | fires on good too |
| off_scale_spacing | 7% | 0% | 60% | fires on good too |
