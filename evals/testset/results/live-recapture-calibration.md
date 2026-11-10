# Calibration: Test set 1 (live)

Not verified, so not scored: L04 (see the capture notes).
Verdict agreement on clear-cut items: **29/34**. Borderline items are reported but not scored.
False positives (good flagged as slop): 1. Misses (slop not flagged): 2.

| Item | Expected | Unslop | Slop lens read | Look families | Slop-type Reflex | Floor | Lens findings | Medium |
|---|---|---|---|---|---|---|---|---|
| L01 | slop | slop | generated (high) | - | 7 | 10 | 12 | web |
| L02 | slop | slop | generated (high) | - | 10 | 11 | 11 | web |
| L03 | slop | slop | generated (high) | saas-card-kit | 31 | 12 | 37 | web |
| L04 | slop | not verified | - | - | 0 | 0 | 0 | web |
| L05 | slop | slop | generated (medium) | warm-paper-serif | 24 | 8 | 12 | web |
| L06 | slop | slop | generated (high) | saas-card-kit | 48 | 20 | 39 | web |
| L07 | slop | slop | generated (medium) | dark-single-accent | 41 | 13 | 13 | web |
| L08 | slop | slop | mixed (medium) | warm-paper-serif | 12 | 2 | 9 | web |
| L09 | slop | slop | mixed (medium) | dark-single-accent | 32 | 6 | 9 | web |
| L10 | slop | slop | generated (high) | - | 38 | 35 | 40 | web |
| L11 | slop | borderline ✗ | mixed (medium) | - | 11 | 31 | 11 | web |
| L12 | slop | slop | generated (high) | violet-gradient | 43 | 16 | 12 | web |
| L13 | slop | slop | generated (high) | warm-paper-serif | 35 | 3 | 35 | web |
| L14 | slop | slop | generated (high) | - | 11 | 2 | 10 | web |
| L15 | slop | good ✗ | made (medium) | - | 5 | 2 | 8 | app |
| L16 | borderline | borderline | mixed (medium) | - | 10 | 1 | 9 | app |
| L17 | borderline | slop | generated (medium) | saas-card-kit | 68 | 24 | 11 | web |
| L18 | good | good | made (medium) | - | 12 | 3 | 8 | web |
| L19 | good | borderline ✗ | made (medium) | violet-gradient | 49 | 12 | 6 | web |
| L20 | good | borderline ✗ | mixed (medium) | - | 38 | 2 | 10 | web |
| L21 | good | slop ✗ | mixed (medium) | warm-paper-serif,hairline-newspaper | 20 | 9 | 9 | diagram |
| L22 | borderline | borderline | mixed (medium) | - | 13 | 16 | 9 | slides |
| L23 | good | good | made (high) | - | 5 | 2 | 16 | web |
| L24 | good | good | made (medium) | - | 28 | 6 | 8 | web |
| L25 | good | good | made (high) | - | 56 | 25 | 16 | web |
| L26 | good | good | made (medium) | - | 65 | 20 | 10 | web |
| L27 | good | good | made (high) | - | 42 | 13 | 7 | web |
| L28 | good | good | made (high) | - | 2 | 8 | 7 | web |
| L29 | good | good | made (low) | - | 0 | 0 | 3 | web |
| L30 | good | good | made (high) | - | 0 | 2 | 4 | web |
| L31 | good | good | made (high) | - | 1 | 23 | 8 | web |
| L32 | good | good | made (high) | - | 7 | 0 | 7 | web |
| L33 | good | good | made (medium) | - | 5 | 23 | 6 | app |
| L34 | good | good | made (high) | - | 8 | 44 | 4 | web |
| L35 | good | good | made (high) | - | 4 | 11 | 9 | web |
| L36 | good | good | made (high) | - | 0 | 1 | 6 | web |
| L37 | good | good | made (high) | - | 44 | 15 | 5 | web |
| L38 | borderline | good | made (high) | - | 43 | 16 | 5 | web |
| L39 | good | good | made (high) | - | 26 | 13 | 3 | web |

## Detector discrimination

Share of items each detector fired on, by expected label. A detector that fires as often on good items as on slop does not separate them; one that fires on good controls is a false-positive candidate.

| Detector | slop | borderline | good | Read |
|---|---|---|---|---|
| stock_swatches | 57% | 75% | 10% | separates |
| look_family | 57% | 25% | 10% | separates |
| nested_radius | 43% | 25% | 5% | separates |
| contrast | 93% | 100% | 55% | separates |
| ai_sparkle | 36% | 25% | 5% | separates |
| glow | 43% | 25% | 15% |  |
| banned_fonts | 43% | 25% | 15% |  |
| default_names | 36% | 0% | 10% |  |
| overflow | 29% | 25% | 5% |  |
| chrome_glyphs | 57% | 50% | 35% |  |
| emoji_icons | 21% | 0% | 0% |  |
| type_ladder | 79% | 75% | 60% |  |
| heading_rhythm | 29% | 0% | 10% |  |
| text_floor | 93% | 100% | 75% |  |
| icon_tile | 21% | 25% | 5% |  |
| widows | 86% | 50% | 70% |  |
| lexicon_copy | 64% | 75% | 50% | fires on good too |
| numbered_labels | 14% | 25% | 0% | rare |
| reduced_motion | 29% | 25% | 15% |  |
| flat_hierarchy | 43% | 50% | 30% | fires on good too |
| em_dash | 21% | 25% | 10% |  |
| near_tangent | 21% | 25% | 10% |  |
| invented_metrics | 21% | 25% | 10% |  |
| targets | 100% | 75% | 90% | fires on good too |
| eyebrow | 14% | 0% | 5% | rare |
| fallback_face | 14% | 0% | 5% | rare |
| motion_css | 79% | 100% | 70% | fires on good too |
| gradient | 43% | 25% | 35% | fires on good too |
| neon_violet | 7% | 0% | 0% | rare |
| unit_wrapped | 7% | 0% | 0% | rare |
| motion_snap | 7% | 0% | 0% | rare |
| async_state | 7% | 0% | 0% | rare |
| words_per_screen | 71% | 75% | 65% | fires on good too |
| nested_cards | 21% | 0% | 15% |  |
| card_kit | 36% | 25% | 30% | fires on good too |
| control_names | 14% | 0% | 10% | rare |
| spacing_monotony | 7% | 0% | 5% | rare |
| headings_landmarks | 79% | 75% | 80% | fires on good too |
| stat_band | 7% | 50% | 10% | rare |
| hidden_content | 57% | 75% | 60% | fires on good too |
| phone_parity | 21% | 50% | 25% |  |
| container_monotony | 14% | 25% | 20% | rare |
| motion | 29% | 75% | 35% | fires on good too |
| accent_footprint | 7% | 25% | 15% | rare |
| zoom_blocked | 7% | 0% | 15% | rare |
| form_labels | 7% | 0% | 15% | rare |
| img_alt | 0% | 0% | 10% | rare |
| lang_and_title | 0% | 0% | 10% | rare |
| repeated_label | 43% | 25% | 55% | fires on good too |
| mixed_icons | 0% | 0% | 15% | rare |
| dead_band | 21% | 25% | 40% | fires on good too |
| page_words | 29% | 25% | 50% | fires on good too |
| performance | 43% | 25% | 65% | fires on good too |
| focus_ring | 57% | 75% | 80% | fires on good too |
| h1_words | 0% | 0% | 25% | rare |
| off_scale_spacing | 7% | 0% | 65% | fires on good too |
