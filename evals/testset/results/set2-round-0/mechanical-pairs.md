# Pair calibration: Test set 2 (controlled pairs)

Pairs scored: 32 of 32. Mechanical sweep separates (bad half scores worse) on **18/32**, ties on 5, inverts on 9. Weighted score: Floor 5, Reflex 2, Finish 1.

- pair-composition: separates 7/13
- pair-detail: separates 0/2
- pair-scene: separates 4/9
- pair-style: separates 7/8

| Pair | Group | Expect | Fault (bad half) | Bad/good items | Score bad vs good | Detectors only on bad | Only on good |
|---|---|---|---|---|---|---|---|
| compact-reflow | pair-composition | borderline | The desktop table is scaled to half size | P25/P20 | 72 vs 86 ✗ | hidden_content, near_blank | - |
| content-density | pair-composition | borderline | Uniform gaps weaken the appointment groups | P29/P50 | 74 vs 74 = | - | - |
| control-alignment | pair-composition | borderline | Icons sit low and labels crowd the upper edge | P40/P06 | 26 vs 25 | off_scale_spacing | - |
| decorative-noise | pair-composition | borderline | Decorative effects compete with the report | P10/P47 | 65 vs 36 | glow, gradient | - |
| edge-separation | pair-composition | borderline | The confirmation almost touches the panel | P01/P04 | 35 vs 35 = | - | - |
| framing | pair-composition | borderline | Tight edges and a status over the content | P52/P23 | 58 vs 54 | - | - |
| icon-consistency | pair-composition | borderline | Mixed fill, stroke weight and visible size | P33/P51 | 36 vs 35 | mixed_icons | - |
| nested-spacing | pair-composition | borderline | The inner surface and action crowd the bottom | P54/P39 | 27 vs 26 | - | - |
| product-anatomy | pair-composition | borderline | Browser chrome disguises a sharing task | P16/P55 | 31 vs 27 | - | - |
| surface-contrast | pair-composition | borderline | Foreground, surface and ground blend together | P18/P35 | 52 vs 32 | - | - |
| ui-anatomy | pair-composition | borderline | Labels, metadata and actions compete | P41/P57 | 56 vs 57 ✗ | off_scale_spacing | nested_radius, text_floor |
| unread-gutter | pair-composition | borderline | Unread rows push their avatar in; the column zigzags | P19/P08 | 64 vs 64 = | - | - |
| visual-restraint | pair-composition | borderline | Borders, shadows and color on every part | P05/P45 | 33 vs 52 ✗ | nested_radius | contrast |
| detail-bar | pair-detail | borderline | Only the more button, the left side empty | P14/P26 | 25 vs 25 = | - | - |
| detail-copy | pair-detail | borderline | Truncated email, wrapped name, ragged labels | P44/P09 | 35 vs 36 ✗ | text_floor | near_blank |
| colored-layers | pair-scene | borderline | Ground, invoice and deposit compete in one saturated field | P38/P37 | 66 vs 44 | accent_footprint | - |
| crop-filler | pair-scene | borderline | The crop cuts the size the story ends on | P21/P42 | 34 vs 34 = | - | - |
| dashboard-phone | pair-scene | borderline | The phone hides the payment it is explaining | P15/P07 | 60 vs 48 | - | - |
| material-contrast | pair-scene | borderline | Inherited colors flatten the dark and light surfaces | P34/P30 | 74 vs 58 | - | - |
| result-weight | pair-scene | borderline | The new file is one thin row in a long list | P27/P12 | 38 vs 34 | - | - |
| story-crop | pair-scene | borderline | The whole application becomes a thumbnail | P43/P31 | 50 vs 51 ✗ | - | nested_radius |
| tile-lead | pair-scene | borderline | Four equal tiles, each a heading and bars | P36/P28 | 20 vs 43 ✗ | - | banned_fonts, contrast, default_names, hidden_content, text_floor |
| window-focus | pair-scene | borderline | Three active windows compete for attention | P03/P53 | 50 vs 58 ✗ | - | - |
| window-satellite | pair-scene | borderline | The receipt sits over the settings and action | P17/P22 | 45 vs 47 ✗ | - | - |
| style-caps | pair-style | slop | Capitals on the heading, labels and button | P24/P49 | 72 vs 47 | chrome_glyphs, hidden_content, nested_radius, text_floor | default_names |
| style-detail | pair-style | borderline | Every row carries six facts and a badge | P11/P49 | 106 vs 47 | chrome_glyphs, hidden_content, text_floor | - |
| style-glow | pair-style | slop | A colored glow on the card, button and dot | P56/P49 | 59 vs 47 | glow | - |
| style-icons | pair-style | slop | Invented glyphs in rainbow tiles | P32/P49 | 50 vs 47 | gradient, nested_radius | - |
| style-onion | pair-style | slop | Translucent ink: darker where strokes cross | P46/P49 | 32 vs 47 ✗ | - | - |
| style-purple | pair-style | slop | Purple gradient ground, gradient title, tinted everything | P48/P49 | 53 vs 47 | gradient | - |
| style-sparkle | pair-style | slop | Sparkles, a wand and a gradient AI chip | P02/P49 | 62 vs 47 | ai_sparkle, glow, gradient, look_family | - |
| style-tiny | pair-style | borderline | 9 to 10px text that only reads zoomed in | P13/P49 | 56 vs 47 | text_floor | off_scale_spacing |

Detectors that fire only on bad halves (how many pairs): gradient 4, text_floor 4, glow 3, nested_radius 3, hidden_content 3, off_scale_spacing 2, chrome_glyphs 2, ai_sparkle 1, look_family 1, near_blank 1, mixed_icons 1, accent_footprint 1

Detectors that fire only on good halves (noise the pairs expose): contrast 2, default_names 2, text_floor 2, nested_radius 2, near_blank 1, off_scale_spacing 1, banned_fonts 1, hidden_content 1

