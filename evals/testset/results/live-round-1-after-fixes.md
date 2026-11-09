# Calibration: Test set 1 (live)

Not verified, so not scored: L04 (see the capture notes).
Verdict agreement on clear-cut items: **29/34**. Borderline items are reported but not scored.
False positives (good flagged as slop): 2. Misses (slop not flagged): 2.

| Item | Expected | Unslop | Slop lens read | Look families | Slop-type Reflex | Floor | Lens findings | Medium |
|---|---|---|---|---|---|---|---|---|
| L01 | slop | slop | generated (high) | - | 7 | 9 | 12 | web |
| L02 | slop | slop | generated (high) | - | 7 | 1 | 11 | web |
| L03 | slop | slop | generated (high) | saas-card-kit | 30 | 12 | 10 | web |
| L04 | slop | not verified | - | - | 0 | 0 | 0 | web |
| L05 | slop | slop | generated (medium) | warm-paper-serif | 24 | 8 | 12 | web |
| L06 | slop | slop | generated (high) | saas-card-kit | 47 | 18 | 13 | web |
| L07 | slop | slop | generated (medium) | dark-single-accent | 45 | 10 | 13 | web |
| L08 | slop | slop | mixed (medium) | warm-paper-serif | 12 | 2 | 9 | web |
| L09 | slop | slop | mixed (medium) | dark-single-accent | 30 | 5 | 9 | web |
| L10 | slop | slop | generated (high) | - | 38 | 35 | 14 | web |
| L11 | slop | borderline ✗ | mixed (medium) | - | 11 | 30 | 11 | web |
| L12 | slop | slop | generated (high) | violet-gradient | 43 | 16 | 12 | web |
| L13 | slop | slop | generated (high) | warm-paper-serif | 35 | 3 | 10 | web |
| L14 | slop | slop | generated (high) | - | 11 | 2 | 10 | web |
| L15 | slop | good ✗ | made (medium) | - | 4 | 2 | 8 | app |
| L16 | borderline | borderline | mixed (medium) | - | 9 | 1 | 9 | app |
| L17 | borderline | slop | generated (medium) | saas-card-kit | 64 | 24 | 11 | web |
| L18 | good | good | made (medium) | - | 12 | 3 | 8 | web |
| L19 | good | borderline ✗ | made (medium) | dark-single-accent,violet-gradient | 60 | 12 | 6 | web |
| L20 | good | slop ✗ | mixed (medium) | violet-gradient | 50 | 3 | 10 | web |
| L21 | good | slop ✗ | mixed (medium) | warm-paper-serif,hairline-newspaper | 18 | 1 | 9 | diagram |
| L22 | borderline | borderline | mixed (medium) | - | 14 | 23 | 9 | slides |
| L23 | good | good | made (high) | - | 5 | 2 | 6 | web |
| L24 | good | good | made (medium) | - | 28 | 6 | 8 | web |
| L25 | good | good | made (high) | - | 56 | 24 | 6 | web |
| L26 | good | good | made (medium) | - | 67 | 23 | 10 | web |
| L27 | good | good | made (high) | - | 40 | 16 | 7 | web |
| L28 | good | good | made (high) | - | 2 | 8 | 7 | web |
| L29 | good | good | made (low) | - | 0 | 0 | 3 | web |
| L30 | good | good | made (high) | - | 0 | 2 | 4 | web |
| L31 | good | good | made (high) | - | 1 | 23 | 8 | web |
| L32 | good | good | made (high) | - | 7 | 1 | 4 | web |
| L33 | good | good | made (medium) | - | 5 | 22 | 6 | app |
| L34 | good | good | made (high) | - | 8 | 51 | 4 | web |
| L35 | good | good | made (high) | - | 4 | 11 | 3 | web |
| L36 | good | good | made (high) | - | 1 | 13 | 6 | web |
| L37 | good | good | made (high) | - | 43 | 16 | 5 | web |
| L38 | borderline | good | made (high) | - | 40 | 16 | 5 | web |
| L39 | good | good | made (high) | - | 26 | 13 | 3 | web |

## Detector discrimination

Share of items each detector fired on, by expected label. A detector that fires as often on good items as on slop does not separate them; one that fires on good controls is a false-positive candidate.

| Detector | slop | borderline | good | Read |
|---|---|---|---|---|
| look_family | 57% | 25% | 15% | separates |
| stock_swatches | 50% | 75% | 10% | separates |
| contrast | 86% | 100% | 55% | separates |
| glow | 43% | 25% | 15% |  |
| default_names | 36% | 0% | 10% |  |
| overflow | 29% | 25% | 5% |  |
| text_floor | 93% | 75% | 70% |  |
| banned_fonts | 43% | 50% | 20% |  |
| chrome_glyphs | 57% | 50% | 35% |  |
| emoji_icons | 21% | 0% | 0% |  |
| heading_rhythm | 29% | 0% | 10% |  |
| eyebrow | 21% | 0% | 5% |  |
| icon_tile | 21% | 25% | 5% |  |
| widows | 86% | 50% | 70% |  |
| lexicon_copy | 64% | 75% | 50% | fires on good too |
| numbered_labels | 14% | 25% | 0% | rare |
| reduced_motion | 29% | 25% | 15% |  |
| type_ladder | 79% | 75% | 65% | fires on good too |
| flat_hierarchy | 43% | 50% | 30% | fires on good too |
| em_dash | 21% | 25% | 10% |  |
| targets | 100% | 75% | 90% | fires on good too |
| fallback_face | 14% | 0% | 5% | rare |
| motion_css | 79% | 100% | 70% | fires on good too |
| gradient | 43% | 50% | 35% | fires on good too |
| nested_cards | 21% | 0% | 15% |  |
| invented_metrics | 21% | 25% | 15% |  |
| card_kit | 36% | 25% | 30% | fires on good too |
| words_per_screen | 64% | 25% | 60% | fires on good too |
| control_names | 14% | 0% | 10% | rare |
| neon_violet | 7% | 0% | 5% | rare |
| spacing_monotony | 7% | 0% | 5% | rare |
| headings_landmarks | 79% | 50% | 80% | fires on good too |
| stat_band | 7% | 50% | 10% | rare |
| hidden_content | 57% | 75% | 60% | fires on good too |
| side_tab_border | 0% | 0% | 5% | rare |
| container_monotony | 14% | 25% | 20% | rare |
| accent_footprint | 7% | 25% | 15% | rare |
| zoom_blocked | 7% | 0% | 15% | rare |
| form_labels | 7% | 0% | 15% | rare |
| phone_parity | 21% | 50% | 30% | fires on good too |
| img_alt | 0% | 0% | 10% | rare |
| lang_and_title | 0% | 0% | 10% | rare |
| repeated_label | 43% | 25% | 55% | fires on good too |
| page_words | 29% | 25% | 45% | fires on good too |
| h1_words | 7% | 0% | 25% | rare |
| dead_band | 21% | 25% | 40% | fires on good too |
| performance | 43% | 50% | 65% | fires on good too |
| focus_ring | 50% | 50% | 85% | fires on good too |
| off_scale_spacing | 7% | 0% | 65% | fires on good too |
