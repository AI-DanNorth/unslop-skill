# Design Rules by Concept

Distilled from Kami — a typesetting and layout system for documents, resumes, slides, one-pagers, letters, reports and landing pages: "good content deserves good paper."

# Part 1 — Philosophy and Invariants

## 1. Core Aesthetic in One Sentence
- Warm parchment canvas, ink-blue accent, serif carries hierarchy; avoid cool grays and hard shadows.
- This is not a UI framework; it is a constraint system for print, designed to keep pages stable, clear and readable.
- Good content deserves good paper: the page itself is the medium, not a screen mood.

## 2. The Ten Invariants
- Default page background is parchment `#f5f4ed`; a white-paper print variant is the only explicit exception.
- One accent, no second chromatic color: ink-blue `#1B365D` for documents; a product website takes the product's own color; a social card set takes one paper with its own single accent.
- All grays are warm-toned (yellow-brown undertone); no cool blue-grays.
- One serif family per page for headlines and body; add a distinct sans only for genuine UI chrome.
- Serif weight locked at `500` for emphasis, no bold; the sole exception is social-card list numerals in Charter Bold.
- Line-heights: tight headlines `1.1–1.3`, dense body `1.4–1.45`, reading body `1.5–1.55`; social cards read at arm's length on a phone and may go up to `1.75`.
- Letter-spacing: Chinese body `0.3pt`; English body `0`; tracking only for short labels and overlines.
- Tag backgrounds must be solid hex, never `rgba()` (translucent fills render as a visible double rectangle in print).
- Surfaces are flat by default; whisper shadows are reserved for real floating screenshots, popovers or overlays.
- No italic in print: no `font-style: italic` in any PDF document; landing pages do not italicize captions, feature subtitles or taglines either; italic marks only a font face's name, syntax tokens, or the author's own emphasis.
- Each invariant has a real cost; think before overriding.

## 3. A Deliberate Choice, Not the AI Default
- The warm-cream + high-contrast serif + terracotta look is a known AI-generated cliché, as are hairline broadsheet layouts and template chrome (all-caps eyebrow over every heading, `A · B · C` meta strings, numbered markers); every overlap with that list must earn its place.
- Paper tone is justified because output is printed or read as a PDF; parchment is the color of the page, not a screen mood. Use the white-paper variant when the sheet itself is white.
- Ink-blue, never clay: terracotta and warm clay are not in the palette; never add a second accent "for warmth".
- Serif is for reading length: documents are read top to bottom; display contrast stays modest; hierarchy comes from size and space, not a fashion display face.
- Rules separate data: a hairline appears only where it divides rows, regions or states; a broadsheet frame for its own sake is out.
- When a brief or brand profile asks for a different direction, follow it; when it asks for a look this system does not do (dark documents, futurist, saturated multi-color), say so instead of bending the system. Dark papers belong to social cards only.

## 4. No Chrome Without Information
- At most one eyebrow, on a cover or hero; never one over every heading.
- Numbering only for real sequences (chapters, slides, steps).
- Eyebrow test: cover it; if the title alone still says what the section is, cut the eyebrow. Keep one only if it adds what the title lacks (a version, a date, an error code, the slide's place in a sequence).

## 5. Middle Dot and Joiner Discipline
- A middle dot ` · ` only between parallel data fields on one line (author and date, phone and email), never as a decorative joiner.
- Swap test: if both sides keep their meaning in either order they are parallel facts and take ` · `; otherwise it is a sentence and takes the language's comma, or better, becomes one phrase with no punctuation (`Only 12 GB of disk space left`, not `Disk space low · 12 GB free`).
- A list row's own name is one phrase with its owner or qualifier (`MiaoYan Xcode Build Products`), never `name · qualifier`.
- Sibling strings in one slot share one joiner.
- Never use ` - ` as a joiner (it reads as a minus or a range); never turn every dot into a comma.
- A heading may join a name and its qualifier with a dot (`Tags · two levels`); drop the dot only when one side repeats the other (a name beside its own translation), and never trade it for parentheses.

## 6. Few Sizes, Few Rungs
- A screen page targets four type sizes: display, title, body, secondary; `12px` is the floor for secondary text.
- Text uses two color rungs to read (primary, secondary), one for meta, and one for disabled or decoration.
- Build hierarchy from weight, color rung and space before introducing a new size.

## 7. Concentric Corners
- A rounded shape inside another shares its centre: inner radius = outer radius − the inset between them.
- Radius follows role (page card, floating layer, row, tag); a new radius means a new role.

## 8. Buttons Need Fills
- A button needs a readable fill; do not replace it with a warning-like outline-only treatment.
- Borders otherwise mark region edges, not every row or control.

## 9. First Principles When Nothing Fits
- Serif carries authority, sans carries utility, warm gray carries rhythm, ink-blue carries focus.
- Add the smallest thing that works; prefer an existing component over inventing a new one.
- Assembling a new container from scratch is how a page ends up with three unrelated emphasis languages; reuse an established component and change its content.

# Part 2 — Color Palette and Tokens

## 10. Single Accent, Warm Neutrals, Zero Cool Tones
- This is the core of the color system: one chromatic color, all neutrals warm.

## 11. Brand Colors
- `--brand` Ink Blue `#1B365D`: the only chromatic color; CTAs, accents, key labels.
- `--brand-light` Ink Light `#2D5A8A`: brighter variant for links on dark surfaces and hover states.
- Ink-blue covers ≤ `5%` of document surface area; more is ornament, not restraint.
- Spend the accent on numbers and distinctive phrases.

## 12. Surface Colors
- Parchment `#f5f4ed`: page background, warm cream, the emotional foundation.
- Ivory `#faf9f5`: quiet filled container, brighter than parchment.
- Inline-code background `#f0eee6`: screen inline annotation, one warm-gray step darker than parchment.
- Warm sand `#e8e6dc`: button default / interactive surface / hovered UI background.
- Dark surface `#30302e`: dark-theme container, warm charcoal.
- Deep dark `#141413`: dark-theme page background, not pure black, slight olive undertone.
- Never use `#ffffff` pure white as page background.
- Never use `#f8f9fa`, `#f3f4f6` or any cool-gray surface.

## 13. Text Colors
- Near-black `#141413`: primary text, deepest but not pure black, warm olive undertone.
- Dark warm `#3d3d3a`: secondary text, table headers, links.
- Olive `#504e49`: subtext, descriptions, captions.
- Stone `#6b6a64`: tertiary, dates, metadata.
- Four levels only: near-black > dark-warm > olive > stone; no fifth level.
- Stone is the lightest gray allowed for text; anything lighter is a border or a surface, never copy.
- Japanese override for olive: `#4d4c48`, because YuMincho's thin strokes need darker text; the Chinese TsangerJinKai02 face needs no override.

## 14. Warm-Gray Mnemonic
- Every gray has a yellow-brown undertone.
- In `rgb()`, warm gray is R ≈ G > B (or R > G > B with small gaps).
- Cool gray is R < G < B, or R = G = B (neutral); both are banned.

## 15. Border Colors
- Border `#e8e6dc`: primary border, section dividers, table headers, controls.
- Border soft `#e5e3d8`: secondary border, row separators, subtle dividers.
- Line `#d8d5c8`: screen hairline for nav pill, cards, hovered borders; the strongest warm rule.

## 16. The One Sanctioned Semantic Exception
- Breaking-change badge background `#f0e0d8` (muted warm peach) with text `#8b4513` (warm brown).
- Reads as "caution" without importing a red; both values are warm (R > G > B).
- This is the only approved second chromatic value; any other off-palette color is a violation.
- Do not add another semantic accent without formally registering it in the palette first.

## 17. Solid Tints Instead of Translucency
- Translucent fills produce a visible double rectangle (padding vs glyph area compositing) on zoom in print; tags must be solid.
- Ink-blue over parchment resolves to two registered tints: tag background `#E4ECF5` (default tag swatch) and brand tint `#EEF2F7` (lightest fill, when a tag must recede).
- Never hand-mix an `rgba()`; a tint outside these two is a new token that must be registered first.
- Never: `background: rgba(201, 100, 66, 0.18)`.
- The inline-code warm-neutral `#f0eee6` is screen-only and is not a third accent tint; use it for small literals in explanatory web copy where blue would imply focus or clickability. Print keeps ivory inline code.

## 18. Twelve-Step UI Role Scale (Screen)
- Step 1 page background: parchment `#f5f4ed`.
- Step 2 raised surface (cards, nav pill, code blocks): ivory `#faf9f5`.
- Step 3 UI element background, inline code: `#f0eee6`.
- Step 4 hovered UI background: warm sand `#e8e6dc`.
- Step 5 selected UI background: brand tint (follows the accent).
- Step 6 subtle border and separator: `#e5e3d8` / `#e8e6dc`.
- Step 7 UI border, card edge: `#d8d5c8`.
- Step 8 focus ring: brand outline.
- Step 9 solid fill: brand.
- Step 10 hovered solid fill: brand-light.
- Step 11 low-contrast text (captions, meta): olive / stone at `7.5:1` / `4.9:1` on parchment.
- Step 12 high-contrast text (headings, body): near-black / dark-warm at `16.7:1` / `9.9:1` on parchment.

## 19. Syntax Highlighting on Light Surfaces
- Use existing tokens only, no new colors.
- Keyword `#1B365D` (brand); comment `#6b6a64` (stone); string `#504e49` (olive); number `#3d3d3a` (dark-warm); function/class `#141413` (near-black).
- Code without a declared language stays monochrome.

## 20. Syntax Highlighting on Dark Screen Surfaces
- Dark code surface `#141318`, the same as the screenshot gallery frame.
- Keep the token palette restrained: comment `#79756a` (faint, italic); keyword `#84aad6` (soft blue); string `#8cbb91` (muted green); number `#cbab86` (sand); function/class `#d6c78c` (sand-gold); builtin/constant `#b59ccd` (muted violet).
- Highlighting is baked statically, never runtime; merge adjacent same-class spans to keep markup small.

# Part 3 — Accent on Product Sites

## 21. Choosing the Accent
- A product site keeps the warm neutrals and takes its accent from the product; ink-blue is the last fallback, not a requirement.
- Order: (1) the product's own main color (dominant hue of its app icon, UI tint or brand assets); (2) if none, or sources disagree, show each candidate plus ink-blue as a filled button and a text link on parchment side by side and let the user choose; (3) only with no preference, keep ink-blue `#1B365D`.
- Lock the accent before filling any layout.

## 22. One Accent, Three Tokens
- `--brand` for buttons, links, the version link and active rails; `--brand-light` for hover; `--brand-tint` for selected tabs and selected fills.
- Brand must reach `4.5:1` against parchment and ivory, and ivory text on a brand fill must reach `4.5:1`; darken in lightness steps until both pass.
- Brand-light is lighter but must still pass `4.5:1` on parchment when used as text.
- Brand-tint is a solid hex near parchment, never `rgba()`.

## 23. Neutrals Never Follow the Accent
- Surfaces, grays and rules keep their warm values so several products from one maker read as one family.
- A cool or saturated product color is fine as the accent; it does not license cool-gray surfaces or a second chromatic color.

## 24. One Name Per Role
- Sites in one family use the same token names for shared roles; change the value, keep the name, and record why.
- Do not invent synonyms (a `--paper` here, an `--ink` meaning body text on one site and link color on another); that is how copied palettes drift apart unseen.

# Part 4 — Typeface Families and Stacks

## 25. One Serif Per Page
- The sans token equals the serif token: one page carries one typeface.
- Add a distinct sans only for genuine UI chrome (screen labels, buttons, chips).

## 26. English Stack
- `Charter, Georgia, Palatino, "Times New Roman", serif`.

## 27. Chinese Stack
- `"TsangerJinKai02", "Source Han Serif SC", "Source Han Serif CN", "Noto Serif CJK SC", "Noto Serif SC", "Songti SC", "STSong", Georgia, serif`.

## 28. Japanese Stack
- `"YuMincho", "Yu Mincho", "Hiragino Mincho ProN", "Noto Serif CJK JP", "Source Han Serif JP", "TsangerJinKai02", Georgia, serif`.

## 29. Korean Stack
- Serif: `"Source Han Serif K", "Source Han Serif KR", "Noto Serif KR", "Nanum Myeongjo", "AppleMyungjo", "Apple SD Gothic Neo", Charter, Georgia, serif`.
- Sans equals serif.
- Mono: `"JetBrains Mono", "D2Coding", "SF Mono", "Fira Code", Consolas, Monaco, "Source Han Serif K", "Source Han Serif KR", monospace`.
- Latin UI: `"Inter", system-ui, -apple-system, "Segoe UI", sans-serif`.
- Keep all name variants of the same face in the chain so whichever distribution is present resolves.

## 30. Monospace Stack With CJK Fallback
- `"JetBrains Mono", "SF Mono", "Fira Code", Consolas, Monaco, "TsangerJinKai02", "Source Han Serif SC", monospace`.
- Any font-family that may render Chinese or Japanese must include a CJK fallback, including running page footers, `pre`, `code` and SVG labels; a pure mono stack can render missing-glyph boxes.

## 31. Mono Size Offset
- Monospace may sit half a step off the serif (e.g. code at `13.5px` beside `15px` body) because its x-height differs; that offset is part of the declared ladder, not drift.

# Part 5 — Type Size Scale

## 32. Print Size Scale (A4)
- Display `36pt`, weight `500`, line-height `1.10`: cover title, one-pager hero.
- H1 Section `22pt`, `500`, `1.20`: chapter titles.
- H2 `16pt`, `500`, `1.25`: subsection.
- H3 `13pt`, `500`, `1.30`: item titles.
- Body Lead `11pt`, `400`, `1.55`: intro paragraphs.
- Body `10pt`, `400`, `1.55`: reading body.
- Body Dense `9.2pt`, `400`, `1.42`: resume, one-pager.
- Caption `9pt`, `400`, `1.45`: notes, figure captions.
- Label `9pt`, `500`, `1.35`: small labels, corner tags.
- Tiny `9pt`, `400`, `1.40`: footer, minor metadata.
- Reading body in practice: serif `400`, `9.5–10pt`, line-height `1.55`.

## 33. Screen Conversion
- Screen px ≈ pt × `1.33` (`9pt` ≈ `12px`, `18pt` ≈ `24px`).

## 34. Minimum Size Floors
- Web text ≥ `12px`; PDF body text and labels ≥ `9pt`.
- Named dense exceptions may go to `8–8.5pt`: compact tables, running footers, dense resume timelines.
- Slide captions at least `24px`, not `12px`: print `9pt` is unreadable at projection distance; slide captions use pt × `2.67`.
- On screen, the `12px` floor carries only uppercase micro-labels and badges, never prose; prose stops at `14px`.

## 35. Ladder Discipline
- Sizes must land on the scale, never between steps.
- Components that each pick their own size drift into `12.5` / `13.5` / `14.5` / `17.5` neighbours; a reader cannot tell 13.5 from 14, so the difference registers as noise, not hierarchy.
- After editing type, list every distinct font size in the stylesheet and confirm each is a declared step.
- A component that wants a new value takes the nearest existing step.

## 36. Screen Type Ladder Example
- Hero `96/64px`, section title `32/26px`, lede `16px`, body `15px`, secondary `14px`, meta `13px`, floor `12px`, plus named component sizes.
- Vertical margins and row gaps are multiples of `4`.

## 37. Serif Optical Size
- A tall x-height serif at `15px` already reads larger than a `15px` sans.
- Do not raise a serif body size to fix perceived readability; check the ladder step first.

# Part 6 — Weight, Line-Height and Letter-Spacing

## 38. Weight Discipline
- Serif body `400`; serif headings `500` (a real Medium file, not synthetic).
- Sans body `400`; sans labels and small titles `500` or `600`.
- Forbidden: `900` black, `100` thin.
- Serif uses only two weights (`400`/`500`); no synthetic bold `600`/`700`.
- Lock `strong` to `500` in long documents so the renderer never synthesizes `700` on top of Medium.
- Never ask for a weight above `500` in PDF (set `strong`, `b` and headings to `500`) so a real Medium face always resolves.
- Disable font synthesis in browsers (`font-synthesis: none`).
- Emphasize with size, space and ink-blue, never with an extra weight step.

## 39. Line-Height Tiers
- Tight headline `1.10–1.30`: display, H1, H2.
- Dense body `1.40–1.45`: resume, one-pager, dense information.
- Reading body `1.50–1.55`: long-doc chapters, letters.
- Label / caption `1.30–1.40`: small labels, multi-line metadata.
- CJK screen body at slide scale (`27–33px`) `1.55–1.65`: Chinese/Japanese serif needs looser leading than print × 1.33.
- Print is tighter than English web body; web typically runs `1.6–1.75`, which in print at pt sizes feels loose and floating.

## 40. Line-Height Bans
- `1.60+` on a print body is forbidden (loose, web rhythm); the only exception is CJK screen body at slide scale.
- `1.00–1.05` is forbidden; lines collide except at extreme display sizes.
- Short blocks read fine near `1.2×`; long passages want about `1.5×`, mapped onto the locked tiers, never invented values.

## 41. Letter-Spacing Rules
- English body text: `0`.
- Chinese and Japanese body with TsangerJinKai02: `0.3pt`; section titles and Mincho samples: `0`.
- Chinese lede text (`14–22pt`) with TsangerJinKai02: `0.03–0.06em` to open large-body paragraphs; English and Japanese ledes stay `0`.
- Chinese and Japanese display text (`24pt+`): `0.2–1pt` optical spacing, scaled with font size.
- English headings may take subtle localized optical tightening, never inherited by body copy.
- Small labels (< `10pt`): `+0.2` to `+0.5pt`.
- All-caps overlines: `+0.5` to `+1pt`, mandatory.
- Never track body copy for effect; kerning and tracking are for display sizes and all-caps or small-caps labels only.

## 42. Slide-Scale Tracking
- Halve print tracking at slide scale.
- Eyebrow max `3px` (not `8px`); display titles `-0.5pt`.
- Large type at `40pt+` looks scattered at print tracking values.
- For CJK slides, letter-spacing matters more than font size for density.

## 43. Set Blocks, Not Glyphs
- Type is a beautiful group of letters, not a group of beautiful letters; judge a paragraph as an even gray shape.
- Pin measure, line-height and tracking per context rather than tuning individual words.

## 44. Optical Alignment
- Text is aligned when it looks aligned, not when box edges match.
- Nudge the optical edge back when a quotation mark, bullet, large display cap or hanging figure pushes a line visually past the margin.

## 45. Measure
- Reading body: about `40–70` characters per line.
- On screen, cap prose at about `720px`; never let a full-frame column run edge to edge.

## 46. Alignment
- Left-align body text, ragged right, for a stable return edge.
- Centre only short display lines: a cover title, a short subtitle, or a single pinned callout line; never paragraphs or lists.

## 47. Hierarchy Through Contrast
- Separate levels with size, weight and space; when a step is unclear, open the size gap or skip a weight rather than adding a faint one.
- Never create an in-between size or a decorative rule to manufacture hierarchy.

## 48. Ideas Not to Import From Western Editorial Guides
- No multi-weight orchestration (Light, Regular, Medium, Bold); the serif range is `400` and `500`, full stop.
- No em-dash-heavy phrasing or ornamental punctuation.
- No faux en-dash bullets.

# Part 7 — CJK and Multilingual Typography

## 49. CJK Density Through Tracking
- `0.3pt` letter-spacing is the baseline for Chinese/Japanese body and is critical for breathing room.
- If CJK text looks tight, add `0.3pt` tracking before touching size.

## 50. No CJK Parentheses on Slides
- Replace full-width parentheses `（...）` with ` · ` or a comma.

## 51. Font Order Depends on Where Text Renders
- In PDF and inline SVG, CJK families lead and Latin faces trail; a leading Latin serif sends each ideograph to fallback separately and splits words across two faces.
- On a website that self-hosts a CJK subset with a CJK-only unicode range, the subset leads and Charter follows (e.g. `"Site Serif SC", Charter, Georgia, "Songti SC", serif`); the range keeps Latin letters and digits out of the subset.
- Leading with Charter on such a site hands it curly quotes and the ellipsis, which it draws as narrow Latin marks.
- A system CJK face without a range (Songti) stays after Charter, or it would take the Latin.
- A face whose Latin is designed to match its Han (TsangerJinKai02) may lead on purpose.

## 52. Ship the Chinese Serif on the Web
- iOS has no Chinese serif (PingFang, a sans, is its only Han face); a system-name stack sets Charter Latin beside sans Han in one sentence on every iPhone.
- Self-host a subset of the leading CJK face: regular plus one heavier weight, WOFF2, unicode range limited to CJK, full-width punctuation, `“”` and `…` (U+201C–201D, U+2026), with swap display.
- Chinese prose uses those quotes and ellipsis as its own; drawn by Charter they hug the Han and the ellipsis sits on the baseline.
- Keep the `halt` feature so adjacent punctuation such as `”。` can compress.
- Never put PingFang in a serif stack; it is the bug, not a fallback.
- Keep the subset in step with the copy, including attribute text (alt, aria-label, placeholder, data attributes); a missing character silently falls back to the system sans.

## 53. Font Licensing
- TsangerJinKai02's free license covers personal/non-commercial use only; for a paid product or its website replace it with Source Han Serif (OFL). A free, open-source product may keep it.

## 54. CJK Leading and Tracking on Screen
- Three leading tiers: long prose `1.8`, list items and answers `1.75`, lead lines and meta `1.6`, folding to `1.7` at phone width.
- CJK headings at `0` tracking; negative Latin display tracking pulls full-em glyphs into each other.
- A Chinese date spaces its numbers from the Han (`2026 年 7 月 20 日`) when the prose does; Japanese sets dates solid.

## 55. CJK Line Endings
- Every line fills the column.
- No `text-wrap: pretty`, no `text-wrap: balance`, no `line-break: strict`, no `word-break: keep-all` on Chinese or Japanese, and no glue binding final characters, chips with their punctuation or clauses; each causes early wraps on phones.
- Set `hanging-punctuation: allow-end` on Chinese and Japanese pages so a comma or full stop that does not fit hangs at the edge.
- Keep inline chips `display: inline` with `white-space: nowrap`, never inline-block, or a line can start with `，`.
- Default kinsoku keeps closing punctuation off a line start.
- A one-character last line is accepted; shorten the copy when it matters.
- Audit: count non-last lines ending more than `1.2em` short of the edge and any line-start punctuation across `320` to `1600px`, in both WebKit and Chromium engines.

## 56. Korean Specifics
- iOS ships Apple SD Gothic Neo and no Myeongjo; a Myeongjo stack falls to Gothic Hangul on every iPhone, mixing Charter and Gothic in one line.
- Unless a Hangul serif subset (`2,350+` syllables, several times a Chinese subset) is shipped, set Korean screen pages in system sans and keep only the wordmark in the Latin serif.
- Japanese has Hiragino Mincho on both macOS and iOS.

## 57. Korean Print Tuning
- Primary serif Source Han Serif K / Noto Serif KR; its Hangul metrics match the Chinese baseline closely, so Chinese per-component values carry over.
- Body `10pt`, line-height `1.45`, letter-spacing `0.3pt`.
- H1 `24pt`, weight `500`, line-height `1.15`, letter-spacing `0` to `−0.2pt` on display H1s.
- Bundle Regular `400` + Medium `500` only to mirror the two-weight discipline; Korean emphasis reads at the same Medium tier, not a heavier Bold.
- One-pager metric label drops from `9pt` to `7pt` because mixed Hangul + parenthesized metadata labels run wider.
- Every weight stays at `500` or below.

## 58. Numeric Alignment Across Scripts
- Use `font-variant-numeric: lining-nums tabular-nums` on every node showing numbers (prices, metrics, versions, tabular data): lining keeps digit height uniform, tabular keeps width uniform.
- Without lining figures, oldstyle fonts drop descenders on `3, 4, 5, 7, 9` and break vertical rhythm.
- Georgia (the Windows fallback for Charter) has only old-style figures and no lining feature; when digit height matters, put a digits-only face first in the stack (local Charter, Palatino Linotype or Cambria, unicode range `U+0030-0039`).

## 59. Spaces and Currency Glyphs
- No non-breaking spaces between words in Charter; it renders about twice the width of an ordinary space.
- Do not scale a currency glyph with `font-size: 0.5em; vertical-align: super`; it makes `$` and digits visually unequal. Prefer `font-size: 0.74em; line-height: 1; transform: translateY(0.015em)`.

## 60. Language Menu Descenders
- With `line-height: 1`, descenders of g/y/p clip; use `min-height: 32px; padding: 6px 10px; line-height: 1.35`.
- Add an invisible bridge between trigger and menu so the cursor can cross the gap without dismissing it.

## 61. One Locale Per Document
- No bilingual stacking in a single document (e.g. changelog); one locale per file.

# Part 8 — Spacing and Rhythm

## 62. Base Unit
- `4pt` in print, `4px` on screen.

## 63. Spacing Tiers
- xs `2–3pt`: inline adjacent elements.
- sm `4–5pt`: tag padding, dense layout.
- md `8–10pt`: component interior.
- lg `16–20pt`: between components, card padding.
- xl `24–32pt`: section-title margins.
- 2xl `40–60pt`: between major sections.
- 3xl `80–120pt`: between chapters in long documents.

## 64. Proximity Law
- A heading belongs to what follows: the gap under a section head must be clearly smaller than the gap above it, ideally by `2×` or more.
- Reversed (generous below, tight above), the head reads as the tail of the previous section regardless of its size.
- A screen page runs on three steps only: inside a block, head-to-content, section-to-section.

## 65. Cramped Heads Are Internal
- When a heading block feels dense, open its internals (eyebrow-to-title, title-to-lede) by a few points before touching macro rhythm.

## 66. Two-Column Rows
- Cap both tracks and push slack into the gutter, so both outer edges align to the container and copy sits at its natural measure.
- A free `1fr` copy column strands text against an empty far edge.

## 67. Repeated Rows Carry No Ornament
- A connector line, badge or index number charming once becomes noise on the fifth repetition; empty space between columns is the answer.

## 68. Section Rhythm as a System (Screen)
- Run section spacing as one responsive ladder, e.g. desktop `96/72`, tablet `72/54`, phone `56/42`.
- When a page reads too airy or tight, scale the whole set by one factor (about `0.75`) across all breakpoints at once; nudging one gap leaves structural asymmetry.
- At the phone breakpoint, step gutters down (`64px` to `16px`) and shrink display sizes (hero title, price) in the same pass.

# Part 9 — Page Formats and Margins

## 69. A4 Margins by Document Type
- Resume (dense): `11mm` top, `13mm` right, `11mm` bottom, `13mm` left.
- One-pager: `15mm` / `18mm` / `15mm` / `18mm`.
- Long document: `20mm` / `22mm` / `22mm` / `22mm`.
- Letter: `25mm` on all sides.
- Portfolio: `12mm` / `15mm` / `12mm` / `15mm`.
- Denser = smaller margins; more formal (letter) = larger margins.

## 70. Page Background Bleed
- Set the parchment background on the page box itself so it extends past the margin area and prints no white edges (e.g. A4, margin `20mm 22mm`, background `#f5f4ed`).

## 71. Slide Page Sizes
- Compact (default) `280mm × 158mm`: standard density.
- Standard `297mm × 167mm`: slightly more room.
- Wide `338mm × 190mm`: heavy content, many data points.
- Change the page size and slide box together.
- Reduce page size only when the entire deck is uniformly sparse.

## 72. Social Card Format
- Each card is `1242 × 1660px` (3:4).

# Part 10 — Lines, Depth and Decoration

## 73. Subtractive Rule for Lines
- A line earns its place only when it separates content regions, encodes state, or carries a data relationship.
- Banned: decorative eyebrow ticks, short cover rules, contact rules, heading side bars, quotation side bars, callout accent edges.
- Keep: table hairlines, chart axes, diagram connectors, input boundaries, full-width region separators, current-state indicators.
- Deletion test: if hiding a line preserves meaning, state, grouping and navigation, delete it and restore any pause with spacing.

## 74. Decoration Density
- Decoration does not create structure.
- Brand color appears in text, digits, labels and intentional fills; containers use ivory fill and restrained radius; lines stay neutral.
- Never layer a brand line, fill, radius and border onto the same component.

## 75. Flat Depth
- Default surface is flat; establish hierarchy with type, alignment, whitespace, one quiet fill, or one neutral hairline.
- Never stack fill, border, radius and shadow on one component.
- Card hover must not create artificial elevation.
- Use a visible outline for keyboard focus.
- Reserve a whisper shadow for a real product screenshot, popover, or anything physically floating; never to make an ordinary card look important.
- Forbidden: `box-shadow: 0 2px 8px rgba(0,0,0,0.3)` and relatives.

## 76. Radius Scale
- Print radii stay within `2–6pt`, scaled to physical size from compact chips to large media frames.
- Radii of `8pt` and up belong to screen surfaces only.
- Never use radius alone to create emphasis.

## 77. Decorative Layers on Screen
- Start with the plain surface: background, typography, content, required controls.
- Add a background, particle field, connecting line, texture or gradient motion only when it communicates a specific relationship, state or brand fact; if its job is "more polished" or "fills space", leave it out.

## 78. No White Cards on Parchment
- In decks, no white card panels on parchment; use spacing first, then one neutral hairline only when a boundary must be explicit.

# Part 11 — Core Document Components

## 79. Cards and Containers
- Ivory fill, `4pt` radius, padding `16pt 20pt`.
- The lift is carried by fill (ivory on parchment), not an outline; no closed hairline border.
- A sub-`1pt` closed border plus radius renders as a double ring in print.
- For more weight, strengthen the label or opening sentence; never add an accent edge or four-sided ring.

## 80. Callout
- Raises a passage above body text: ivory fill + `3pt` radius, no accent edge.
- On denser pages only the padding tightens.
- Same family as module notes; no decorative bar.

## 81. Tags
- Two tiers, both solid registered tints.
- Default: background `#E4ECF5`, brand text, `9pt`, weight `600`, padding `1pt 6pt`, radius `4pt`, letter-spacing `0.4pt`, uppercase.
- Recede (dense pages, several tags in a row): background `#EEF2F7`, padding `1pt 5pt`, radius `2pt`.
- If the eye lands on the tag's background shape before its text, the tag is too strong.
- No gradient tags; tint depth one step lighter than decoration wants; lightest solid wins most of the time.
- Inside an already filled highlight, do not stack a filled tag; use an ivory surface with a text-only ink-blue label.

## 82. Lists
- Native list markers in brand color: ordered lists carry numbers, unordered lists a disc.
- Padding-left `16pt`, line-height `1.55`.
- Ordered markers in brand at weight `500`.
- Never fake a bullet with an en-dash pseudo-element; a dash marker reads as AI default output.
- A custom short bar marker is decoration disguised as structure.

## 83. Quote
- Margin `12pt 16pt`, padding `4pt 0`, olive text, line-height `1.55`.
- Indented olive text with reading space; no fill and no side rule.

## 84. Code Block (Print)
- Ivory fill, `4pt` radius (inline code `2pt`), no border.
- Padding `10pt 14pt`, mono `9pt`, line-height `1.5`.

## 85. Section Title
- Serif `14pt`, weight `500`, near-black, margin `24pt 0 10pt 0`.
- Start a section with serif scale and margin only: no leading tick, side bar or short rule.

## 86. Marking Out One List Item
- Use ivory fill, a stronger label, or a short lead sentence; never an accent edge.

## 87. Document Header Signature
- Uppercase eyebrow text, then the serif title, meta right-aligned, optional `0.5pt` full-width hairline closing the block.
- The hairline is structural, separating header from body.
- No leading tick, centered version block, short decorative rule or full-height side bar.
- Resumes (name header) and letters (letterhead) keep purpose-built headers.

## 88. Cover Page
- Display heading, right-aligned author and date, heavy whitespace.

## 89. Buttons in Print
- Print documents have no buttons.

# Part 12 — Tables

## 90. Base Table
- Full width, collapsed borders, `9.5pt`, margin `12pt 0`, avoid breaking inside.
- Header: left-aligned, weight `500`, dark-warm, padding `6pt 8pt`, bottom rule `0.6pt` border color.
- Cells: padding `5pt 8pt`, bottom rule `0.25pt` border color, top-aligned.
- First and last columns carry no outer horizontal padding so the table's text edge aligns with heading and body text above.

## 91. Compact Variant
- `8pt` text; header padding `3pt 6pt`; cells `2.5pt 6pt`, line-height `1.4`.
- Use for `5+` columns, `8+` rows, or verified page-fit pressure.
- Never go below `3pt` header / `2.5pt` cell vertical padding.

## 92. Financial Variant
- Right-align all columns except the first; enable tabular figures.
- For revenue, pricing, metrics.

## 93. Striped Variant
- Optional neutral ivory on even rows, only for `8+` body rows when row tracking still fails at normal viewing size.
- Start without striping; a striped table keeps its inset because the fill needs room around text.

## 94. Total Row
- Weight `500`, near-black, `0.6pt` top rule, no bottom rule.
- Hierarchy from weight and placement, never a second color.

## 95. Table Acceptance Rules
- Every rule uses the border token; header and total rules `0.6pt`, body `0.25pt`.
- Normal tables keep at least `6pt` header and `5pt` cell vertical padding; fixed-length one-pagers and resumes may step down once to `5pt` / `4pt`.
- Banned: category-colored values, brand-colored rules, tinted headers, vertical grid lines, framed tables.
- Row separation comes from whitespace before line weight.

## 96. Position Table
- Three-column comparison (direction, reference project, approach) whose final row highlights the current subject.
- Highlight row: ivory fill + brand text; do not bold the whole row, let the subject name carry emphasis.

## 97. Editorial Screen Tables
- No framed box, tinted header bar, vertical rules or empty right gap.
- Content-sized columns, hairline row rules, muted uppercase UI-sans header.
- On phone, make the table a horizontally scrolling block rather than cramming columns.

## 98. Slide Data Tables
- Cells padding `8pt`, `0.25pt` bottom rule, `11pt`.
- First column weight `500` in dark-warm: hierarchy without a second table color.

# Part 13 — Numbers and Metrics

## 99. Emphasizing a Number
- Color it brand; never bold it.

## 100. Print Metric Row
- Flex row, gap `24pt`; each metric is value + label on a shared baseline, gap `6pt`.
- Value: serif `16pt`, weight `500`, brand, tabular figures.
- Label: `9pt`, olive, never wraps.
- Suffix: `0.58em`, weight `400`, left margin `0.06em`, raised `0.08em`.
- Transparent, no container; numbers carry themselves. A filled card around metrics is the most common drift.

## 101. Metric Labels Must Not Wrap
- Inline baseline metrics hold only because labels are short fixed strings; a wrapped label dangles below the baseline and reads broken.
- Keep labels to one line and forbid wrapping so overflow surfaces in review; fix by shortening the words.
- On screen and slides, where labels are translated and read at `375px`, metrics stack vertically instead.

## 102. Multiplication Sign as Suffix
- In values like `10×`, use the true multiplication sign at about `60%` of numeral size, optically aligned to the numeral body; a full-size `×` reads like a letter.

## 103. Glance Grid
- Four key-number cells after the table of contents or on a chapter-opening page of a long document or proposal.
- Two-column grid, gap `14pt`, margin `18pt 0`; cell padding `12pt 0 10pt 0`.
- Label: mono `8.5pt`, brand, letter-spacing `1pt`, uppercase, weight `500`.
- Value: `18pt`, weight `500`, near-black, tabular figures, letter-spacing `0.5pt`.
- Note: `9pt`, olive, line-height `1.4`.

## 104. Large Digits Need Tracking
- Headline price digits: serif `500`, `44pt`, tabular figures, letter-spacing `0.5pt`; without tracking, large digits crowd and read too dense.

## 105. Screen Metrics
- Flex row, `32px` gap; value serif `36px` weight `500`, label `13px` UI-sans in stone; tabular figures on values.

# Part 14 — Proposal and Report Components

## 106. Module Block
- Proposal A / B / C structure: brand-colored letter, a title, and an uppercase English subtitle.
- Letter `28pt` brand; title `17pt`; subtitle `10pt` mono brand, letter-spacing `2pt`.
- Head separated from body by a `0.3pt` warm-gray hairline, not brand color.

## 107. Module Note
- Short note explaining the relationship between two or more modules (e.g. "B is upstream capability building, C is downstream validation; together they form a minimal closed loop").
- Ivory background, `4pt` radius, label `8.5pt` brand uppercase mono; no decorative bar.

## 108. Pricing Card (Print)
- Eyebrow + price + short note (e.g. "Paid by milestone").
- Price digits serif `500`, `44pt`, tabular, letter-spacing `0.5pt`.
- Without-price variant: drop the price and follow the eyebrow with value anchors.

## 109. Value Anchors
- Replace pricing line-item breakdowns with `4–6` capability anchors, each a bold lead-in and one factual sentence about capability source or scarcity.
- Native disc marker in brand; padding-left `16pt`; margin `12pt 0 18pt 0`.
- Items padding `9pt 0`, `0.3pt` soft-border separator (none on last), line-height `1.55`, `10.5pt`.
- Lead-in in brand at weight `500`, right margin `6pt`.

## 110. Hero Product Shot on a One-Pager
- A product brief earns one real screenshot as visual anchor, not decorative texture.
- Frame with clipped overflow, restrained radius and a soft shadow; no closed sub-`1pt` border.
- Cover-fit to trim dead background evenly while the app window stays whole.
- One caption that adds a fact, not a restatement.
- If the page is sparse, merge or rebalance content; never inflate the screenshot to fill space.

## 111. Horizontal Funnel / Progress Bars
- Three-column grid: `80pt` label | `1fr` track | `40pt` external percentage; align center, gap `8pt`, row margin `4pt 0`.
- Use grid, not flex, so the percentage never drifts with bar length.
- Track `18pt` tall, soft-border fill, `2pt` radius; fill brand, `2pt` radius.
- Percentage tabular figures, right-aligned, stone, `9pt`.
- Single brand fill only; no gradients or per-row hues; vary opacity (e.g. `0.7`) for ranking.
- Inline labels inside the bar sit in an absolutely positioned child of the track.

# Part 15 — Document-Type Rules

## 112. Resume
- Densest margins (`11mm` / `13mm`), dense body `9.2pt` at `1.42`.
- A quiet full-width bottom rule under section titles, because it separates major regions.
- Project rows stay borderless to avoid double rules and page-top orphan lines.
- Purpose-built name header.

## 113. One-Pager
- Margins `15mm` / `18mm`; dense body.
- Metric strip in the header; one real product screenshot at most.

## 114. Long Document
- Margins `20mm` / `22mm`; reading body `1.50–1.55`; `80–120pt` between chapters.
- Table-of-contents rows link to stable chapter anchors and use generated page numbers; never hand-fill page numerals, which drift with any edit.
- Keep each TOC row a block with the page number floated right.

## 115. Letter
- `25mm` margins all round; reading body line-height; letterhead header.

## 116. Portfolio
- Margins `12mm` / `15mm`; main images `4:3` or `16:10`.

## 117. Changelog / Release Notes
- Same editorial language as the one-pager, never a centered version block.
- Left-aligned header: uppercase eyebrow, "Project Version" serif title, date on the right, structural hairline.
- Group entries under text-only section heads (Breaking / Features / Fixes, or Highlights / Fixes); drop sections that do not apply.
- Each entry is a numbered item with a bold lead-in, colon, then detail; numbers restart per section; no per-item bullet glyph.
- Acknowledgements are a quiet labelled note, never a filled card.
- Footer split: left description, right URL.
- A breaking entry may carry the warm breaking chip; it is the only inline tag worth keeping.

## 118. Quick Decision Table
- Big headline: serif `500`, size by level, line-height `1.10–1.30`.
- Reading body: serif `400`, `9.5–10pt`, `1.55`.
- Show key figures: baseline metric row, no container.
- Quote someone: indented olive text, no fill or side rule.
- Show code: ivory fill, `4pt` / `2pt` radius, no border.

# Part 16 — Print and Pagination

## 119. Break-Inside Protection
- Never split cards, metrics, project items, quotes, code blocks, figures, callouts, takeaways, modules, module notes, glance grids, pricing cards or compact tables across pages.
- Headings never sit alone at a page bottom (avoid break after `h1`–`h3`).
- Body widows/orphans minimum `3`; paragraphs minimum `2`.

## 120. Chapter-End Spillover
- CSS alone cannot stop the last two lines of a chapter landing on a fresh page; check rendered density.

## 121. Cascading Break Risk
- When two unbreakable blocks sit adjacent and the first would split, both get pushed together.
- More than two unbreakable blocks (quote + table + callout) near a page boundary risks `40–80mm` of trailing whitespace.
- Fix by splitting the chapter or letting one block break (e.g. a table with a repeating header).

## 122. Forced Breaks
- Use an explicit page-break-before element for deliberate breaks.

## 123. Print Renderer Pitfalls
- Translucent backgrounds composite as double rectangles: use solid hex.
- Sub-`1pt` closed border + radius renders a double ring.
- Renderers that cannot synthesize bold need a real Medium file for `500`.
- Gradient fills by reference and grid layout inside SVG are unsupported; draw arrowheads as explicit paths because auto-orienting markers do not rotate.
- Style-element class selectors inside SVG may be ignored; some chart types are screen-only.

# Part 17 — Slides and Decks

## 124. Slide Body Typography
- Body `13pt`, line-height `1.55`, letter-spacing `0.3pt`; slides are read across a room, not at `9–11pt`.
- `h2` page title `32pt` weight `500`, margin-bottom `16pt`.
- `h3` section heading `18pt` weight `500` in brand.
- Eyebrow `10pt` weight `400`, mono, letter-spacing `2pt`, stone.
- Lead `16pt` weight `400`, olive, below `h2`.

## 125. Slide Content Element Scale
- Module title `19pt` paired with a large brand letter prefix `28pt`.
- Module sub-label `9pt` mono with a bottom separator.
- Module body and line items `13pt`; line items padding `8pt 0`.
- Cadence/delivery note `11pt` with a top rule.
- Bottom callout `14pt` bold, pinned near the bottom, clear of the footer line.

## 126. Slide Spacing
- Slide padding baseline `80px`; padding-top `72–80px` (print is `96–120px`).
- Macro scale (font size, padding): print pt × ~`1.6`.
- Micro scale (display tracking, border, radius): halve the print value; body letter-spacing stays at print baseline.

## 127. Content Slide Section Header
- Margin-bottom `36px`.
- Eyebrow `12px`, weight `500`, letter-spacing `1.5px`, uppercase, stone, margin-bottom `14px`.
- H1 serif `38px`, weight `500`, line-height `1.1`, near-black.
- `14–20px` between eyebrow and H1; let outer margin create the larger pause; no short rule or dot.

## 128. Slide Layout Patterns
- Two-column: grid `1fr 1fr`, gap `22pt`, for modules with independent heights.
- 2×2 aligned: use a table, not a grid, so row heights align across cells.
- Pinned callout: absolute, `bottom: 12mm; left: 20mm; right: 20mm`; whitespace above it is intentional.
- If a footer spans full width at `10mm`, lift the pinned callout to about `18mm`.

## 129. Slide Content Rules
- No section divider slides; use the eyebrow for section numbering.
- Ghost deck test: read only the slide titles in order; they must tell the argument.
- One evidence shape per slide: chart, table, screenshot, code, quote or conclusion; split mixed evidence.
- One line per bullet; trim until each fits.
- Target `3–5` items per slide.
- Empty space ≥ `50%` is a draft defect: merge with a neighbor > remove and fold its point elsewhere > convert evidence only if clearer; never add a callout, chart or image to occupy space.
- Empty space `25–50%` is acceptable when one assertion and its proof genuinely need room; otherwise merge or tighten.
- Visual briefs (crop notes, prompt fragments, generation instructions) never appear in titles, body, or captions.

## 130. Slide Cover
- No horizontal rule; title centered at `44pt`; subtitle on one line; bottom meta centered.
- Optional logo centered above the cover title at `72px` height.
- No page number on the cover or closing slide.

## 131. Code Card on Slides
- Ivory, `1px` border, `8px` radius, padding `20px 24px`, clipped overflow.
- Mono `13px` (`14px` on larger slides), line-height `1.55`, near-black, no wrapping.
- Syntax colors from existing tokens only: keyword/string brand, comment stone.
- Optional line numbers: right-aligned stone, `1px` soft-border divider, `12px` right padding, `16px` column gap.
- Write pseudocode; comments should outnumber code lines; the reader sees logic, not syntax.

## 132. Preserving a Client Template
- When a real brand deck must be preserved, inventory its layout families first and map each section onto an existing layout.

# Part 18 — Images, Charts and Diagrams

## 133. Image Aspect Ratios
- Hero full-bleed (slides / cover): `16:9`, cover-fit.
- Main document image: `4:3` or `16:10`.
- Side-by-side two-up grid: `3:2`.
- Magazine inset with text wrap: `3:2` or `3:4` (portrait for people).
- Square thumbnail (icon, avatar, logo): `1:1`.
- Slide image grid: fixed row height (e.g. `26vh`), free width, clip width.
- Ratios are defaults; adjust by one step if the source differs greatly.

## 134. Slot-First Rule
- Decide the image's job first: proof screenshot, product surface, person/place photo, diagram, logo, or decorative texture.
- Proof screenshots and product UI keep fidelity; only diagrams and concept images may be redrawn for style.

## 135. Audience Copy vs Visual Brief
- Visible copy says what the reader should believe; the visual brief stays internal.
- Never paste prompt fragments ("16:9 cinematic UI mockup") or crop instructions into captions, bullets, alt text, FAQ or metadata.

## 136. Screenshot Handling
- Contain-fit inside a stable frame, or a quiet padded canvas when ratios differ.
- Never crop away UI text, numbers, window chrome, terminal prompts or controls to fill a frame.
- Too tall, narrow or dense: split into `2–3` panels before any redraw.
- A redraw must be labelled schematic or concept, never passed off as a real screenshot.

## 137. Cropping by Subject
- UI screenshots: contain or centered padding.
- People and product photos: cover-fit with subject in the safe centre (`center center` or `center 35%`).
- Document scans: often `top center` because titles live at the top.
- Under contain-fit, object position has little effect; use frame padding and alignment.

## 138. Brand Logo Slot
- Fixed height, auto width, contain-fit so any aspect scales without distortion.
- One-pager `44px`, top of header row; portfolio `72px` above cover eyebrow; slides `72px` centered above cover title.
- Sizes are per format, not a shared token.

## 139. Diagrams
- Same invariants: parchment canvas, ink-blue only for the focal element, warm neutrals elsewhere, serif labels with CJK fallback.
- Resolve any derived shades to static warm hex so no cool grays appear (e.g. `#dad9d3`).

## 140. SVG in Slides
- ViewBox width fixed at `920`, height to content; max height `105mm`.

## 141. Charts on Dashboards
- Every chart answers one question; a chart that only restates an on-screen stat gets deleted.

# Part 19 — Landing Pages: Layout and Hero

## 142. Page Layout
- Max width `1120px` centered, padding `88px 64px 120px`.
- Breakpoints: `880px` (tablet) and `480px` (phone).
- Each section opens with a title and optional lede; no numbered label above the title, since gallery, features, pricing and FAQ are not a sequence. One eyebrow on the hero is enough.

## 143. Product Site Locks
- Before filling a template, lock: product category (first-viewport label), real assets mapped to slots, site shape, exact locale list, and truth surfaces (install path, price, version, support route, FAQ, AI summaries).
- A missing asset stays marked, never replaced with stock imagery.
- Locale pages, FAQ, structured data, screenshots, install copy, pricing, version and support links are one public fact set; keep claims aligned.
- Check positioning against current product surfaces; stale category language is worse than a missing feature detail.

## 144. Product Screenshot Slots
- Hero signal: real product surface, terminal state or app window, `16:10` or `16:9`, recognition over full-bleed drama.
- Gallery panel: one shipped workflow or reachable UI state, stable frame, no filler.
- Feature panel: focused crop or two-step before/after; preserve labels and controls.
- Social image: product name + one recognizable surface, `1200×630`.
- Localized UI needs localized captures per locale; one shared English screenshot breaks the promise of localized copy.
- Encode the social image as a real baseline JPEG at `1200×630`; a renamed PNG fails validators.

## 145. Single-Line Surfaces
- Must render on one line at `1280px`: hero tagline, feature subtitles, benefit points, gallery captions, section ledes under ~`12` words, footer ethos.
- Must also hold one line at `375px`: price line, platform line, CTA labels, hero chips.
- A near-wrap (one word away) counts as failure.
- Fix container geometry and forced breaks first, then shorten redundant wording; never shrink the font, force a break, or shave padding.
- Text-height-dependent components (carousel captions, rotating taglines) are verified with the longest locale.
- One wrap found means sweeping every listed surface in every locale.

## 146. Hero Eyebrow
- Flex row, space-between: left = product category + version link; right = language switch and social icons.
- Version link brand, weight `600`, links to releases.
- Eyebrow text `12px` UI sans, weight `500`, letter-spacing `0.4px`, uppercase, stone.

## 147. Hero
- Title `96px` (EN) / `88px` (CN), weight `500`, letter-spacing `0`.
- No entrance effect on the title; no blur reveal or staged motion.
- Tagline `21px` (EN) / `20px` (CN), olive, letter-spacing `0.2px` (EN) / `0.4px` (CN), max width `820px`.
- Chips row: `13px` stone UI sans; about three product qualities, not an inventory of facts (license, package manager, OS version go to footer or docs).
- No chip may repeat the tagline.
- Chip separator middot placed after each non-last item, at `58%` mix toward transparent, so a wrapped chip never carries a leading dot.
- Use natural wrapping for title and tagline; no max-width cap just to move a widow; no balance/pretty wrap by default.

## 148. Mobile Density Inversion
- Below the phone breakpoint: images first, words second; feature copy compresses to `1–2` sentences.
- FAQ collapses by default.
- Wrap every hover style in a hover-capable media query; a hover flash on tap is a bug.

# Part 20 — Landing Pages: Components

## 149. Buttons
- Two variants only.
- Primary: brand fill and border, ivory text, hover brand-light and `translateY(-1px)`.
- Ghost: ivory fill, line-color border, near-black text, hover warm sand and `translateY(-1px)`.
- Both: pill `999px`, `15px` UI sans, weight `500`, line-height `1.55`, `1px` border, padding `13px 28px`, min width `158px`.
- A brand-outlined ghost beside a brand-filled primary reads as a second offer; avoid.
- Avoid weight `600` on Latin button labels beside CJK.
- Primary = the action most visitors take first (on a paid app with a trial, the download; buying is the ghost).

## 150. Button Labels
- Verb plus object: `Buy {{PRODUCT}}` (no price), `Download for Mac`; compact nav pill keeps the verb alone.
- Avoid urgency forms like "Buy now".

## 151. Mobile Button Pair
- Two hero buttons in one row from the hero text edge, each label-width, `42px` tall, `22px` sides, min `128px` wide, `12px` apart; sides drop to `14px` under `375px`.
- Second button wraps only when a long label does not fit.
- Ghost hairline mixes `60%` line color into ivory on phone, because `1px` reads heavy at high pixel density.
- Never stretch to share the row and never force equal halves (long German labels overflow); never center the pair.
- Verify at `320px` and `375px` in the longest language.

## 152. Links
- One behavior site-wide: brand color, no underline, hover lightens; no per-component exceptions.
- Brand color on non-links (FAQ questions, section titles) misleads; non-link headings stay near-black.

## 153. Gallery
- Grid `minmax(0, 1fr) auto`; frame full width, caption and tabs on row 2.
- Frame dark `#141318`, `8px` radius, `1px` border.
- Real captures over mockups; missing assets are omitted, not substituted.
- Transition: direction-aware slide + `scale(0.985)`, `620–880ms`, `cubic-bezier(0.22, 1, 0.36, 1)`.
- Auto-rotate every `4500ms`, pause on hover/focus, respect reduced motion; single image does not auto-rotate.
- Tabs: `12px` pill buttons, active state brand tint.
- Click left half = previous, right half = next.
- Caption upright serif `14px` olive; keep caption and tab state synced under rapid switching.

## 154. Pricing Section
- Benefits lead, the price states itself once, the CTA never carries the number.
- Benefits list `4–6` items, serif `16px` dark-warm, one line each, plain borderless list.
- Amount `30px` serif, one factual line (`$N · One-time purchase`), lining tabular figures; never display-size the price.
- No border box, shadow or gradient on the card; background and spacing frame it.
- Competitor comparison `18px` with struck-through prices in stone.
- Terms `13.5px` olive, centered, max width `640px`, line-height `1.5`.

## 155. Manifesto
- `20px`, weight `400`, line-height `1.55`, letter-spacing `0.05em`.
- Emphasis renders in brand color, upright, not italic.

## 156. Screen Code Block
- Ivory, `1px` border, `6px` radius, padding `18px 22px`.
- Mono `13.5px`, tabular, line-height `1.55`; `11.5px` at `480px`; long lines scroll rather than wrap.
- Inline code: inline-code background, dark-warm text, no border, `2px` radius, minimal padding, `0.9em`; an annotation, not a focal tag.

## 157. Cards Site-Wide
- One border treatment across all cards (same token, same width); reuse before inventing.
- Ordinary cards stay flat on hover; a linked card uses link color and focus outline.
- Re-check contrast in the hover state, not just resting.

## 158. Demo Card Grid
- Auto-fill `minmax(240px, 1fr)`, `18px` gap.
- Ivory, `1px` border, `8px` radius, no shadow or lift.
- Image on top, title `15px` weight `500`, description `12px` olive.

## 159. Article Card Lists
- Titles clamp at `2` lines with ellipsis but are written to fit one; no parenthetical asides; line-height `1.2–1.3`.
- Summaries clamp at `4` lines.
- Clamp plus ellipsis is the only truncation gesture: no fades, no inline "read more".

## 160. Features List
- Two-column grid: `200px` name + `1fr` description, `36px` gap, soft-border hairline separators.
- Name `22px` brand, weight `500`; optional subtitle `13px` olive upright.
- Description `15px` dark-warm, line-height `1.55`.

## 161. Feature Rows With a Visual
- Compute slack = content width − (visual + gutter + copy's natural width); it is almost always positive.
- Put slack on the outer trim, never in the gutter (a hole there separates copy from what it describes).
- Mirror only a text mass, never a short list; left edges are the strongest alignment cue.
- Rescues that fail: pinning a fixed measure to the gutter, right-aligning mirrored copy, centering seams on a shared axis.
- Run every row the same way: visual flush left, one copy left edge, slack outside.
- Buy variety with unequal weight (lead row larger, supporting rows shorter), not A-B-A-B alternation.
- Measure copy in every locale (CJK can run `30%` longer); let long locales wrap.

## 162. FAQ
- Each pair wrapped with `24px` bottom margin.
- Question `16px` weight `500`, no top margin; answer `14px` olive.
- Code spans mono `12px`, inline-code background, `2px` radius, no border.
- Close with a `13px` stone tail line linking to help.

## 163. Testimonial Wall
- Only real, attributed quotes.
- Clip collapsed masonry to the shortest column so the fold is one flat line under the fade.
- One "Show all" control; expansion reveals everything and keeps scroll anchored.
- Collapsed height roughly `9–12` quotes, never pushing pricing out of reach.
- An external "more quotes" link is a last card in the wall's own style, one line.

## 164. Footer
- Two-column flex: brand mark (icon + name + tagline) left, colophon (links + ethos) right; single column below `880px`.
- Mark icon `56px`, `8px` radius.
- Link separators placed after each non-last link; no non-breaking-space joining.
- Ethos: closing upright serif line, olive, max width `360px`.
- Credit any upstream project exactly once, quietly, in the footer; never in the hero.

# Part 21 — Screen: Docs Sites, Dashboards and Verification

## 165. Documentation Site Shell
- Sticky sidebar ~`178px` (top `84px`, max height viewport − `108px`, scrollable) plus prose column capped at ~`720px`.
- Active state is a rail: `2px` left border that fills brand on the current page, with brand text; no heavy fill or dark underline.
- One file per topic, grouped under sidebar sections; current page marked for both visuals and screen readers.

## 166. On-This-Page and Pager
- Thin in-flow list under a hairline top border, `11px` uppercase UI-sans heading, depth-3 entries indented ~`12px`; hidden below tablet.
- Prev/next: borderless text links in a two-column grid with one thin top divider; uppercase "Previous"/"Next" eyebrow over a brand serif title; next aligns right; pressed opacity `0.6`.
- Mobile: sidebar becomes a horizontal scroll strip with the rail moved to the bottom border.

## 167. Dashboards
- One currency and one unit system across the board.
- Zero rows disappear or aggregate into "other".
- One meaningful default time range; every selector option answers a real question.
- Implementation detail (sync, API state, field names) stays off the surface.
- Totals reconciled against one authoritative source with the basis noted.

## 168. Rendered Verification
- Screenshot the real render at `375px` (and `320px` for CTAs), `1280px`, both sides of each breakpoint and a tablet width, in every locale.
- Flag text blocks whose last line is under ~`13%` of the widest line as review candidates, not automatic defects.
- Scan for sparse blocks taller than ~a quarter viewport, empty grid slots or lone items in multi-column rows; fix by tightening, merging or removing, never by padding with content.
- Confirm zero horizontal overflow and that grids collapse to one column on phone.
- Verify with fresh, cache-busted renders scrolled to the section under review.

# Part 22 — Social Cards

## 169. Papers
- The one surface where page color changes, to sit beside the cover photo in a feed; one paper per set.
- Parchment `#f5f4ed` / accent `#1B365D` (default).
- Ink `#1B365D` / `#b9c6d8`.
- Olive `#2b3326` / `#bdb38c`.
- Espresso `#3a2a20` / `#d9b48a`.
- Pine `#1c3a29` / `#b5cfa4`.
- Teal `#134857` / `#a8d0cf`.
- Crimson `#5a1f17` / `#e6bca6`.
- Char `#1e1d1b` / `#d4c4a0`.
- Paper colors are allowed only on social cards, never in documents.

## 170. Choosing a Paper
- Match the cover photo: espresso for warm drinks or wood; ink or teal for sky and water; pine or olive for plants; char for dark-UI screenshots.
- A product's own set uses the paper derived from its color.

## 171. Social Card Contrast and Weight
- Text reaches `8.8:1`, accent `6:1`, muted `4.3:1` at `28px` and up.
- On dark papers all text is weight `500`; light-on-dark rasterizes thinner than previews show.

## 172. Card Geometry
- `96px` side margins, `30px` meta line at top; footer (except cover) `28px` with a one-pixel rule and title beneath, ending `84px` above the bottom.
- Cover: title `104px`, max width `7.3em`; real photo from `640px` down to `96px` above bottom, radius `20px`.
- Text card: heading `80px`, body `44px` at `1.75` (EN `1.5`, KO `1.7`), two or three paragraphs.
- List card: two to five items; numbers Charter Bold `64px` in accent (the one sanctioned bold); items `42px` at `1.68` (EN `1.48`, KO `1.65`).
- Shot card: heading, one or two sentences, full-width real screenshot, radius `20px`.

## 173. Social Card Copy
- Cover headline is the post title word for word; never force line breaks, narrow the max width instead.
- Author text used as written; a paragraph ending on `1–3` characters gets right padding until it breaks elsewhere.
- One point per text card; cards in a set carry similar weight.
- A card ending above about two-thirds of its height takes more of the author's text or merges; split rather than shrink type.
- Cover needs a real photo or screenshot, never stock or drawn UI; the photo box is near square (`1050×924`), so crop around one complete UI piece.
- Keep at least `40px` between the last text and the footer rule; no text over the photo.

## 174. Platform Limits
- Xiaohongshu: up to `18` images; title limit `20` characters, with Latin, digits and spaces counting less than one each.
- X: at most four images; keep headline and key evidence inside the centre `1242×1242` crop; post under `280` weighted characters (a URL counts `23`).

# Part 23 — Core Principles

## 175. Good Content Deserves Good Paper
- The aesthetic is editorial and print-first: serif type, warm paper backgrounds, a single ink-blue accent.
- Good typography with bad content is only "polished mediocrity"; content quality and layout quality are both required.
- The system is deliberately anti-future: do not apply it to dark, cyberpunk or futurist aesthetics.
- Do not apply it where a different design language is required (Material, Fluent, a default utility-CSS look), to saturated multi-color palettes, to cartoon/animation/illustration styles, or to dynamic web-app UI.

## 176. Ten Visual Invariants
- Default page background is parchment `#f5f4ed`; a white-paper print variant is an explicit, opt-in exception (it flips the page to white while cards and tables keep warm backgrounds).
- One accent only: ink-blue `#1B365D`; social cards instead pick one paper, each with exactly one accent.
- All grays are warm-toned (yellow-brown undertone); never cool blue-gray.
- One serif family per page for headings and body; the "sans" role is an alias of the same serif. Introduce a real sans only for genuinely UI-style chrome.
- Serif weights: `400` body, `500` headings; no bold (`700`) and no Light. The only exception is bold numerals in social-card lists.
- Line-height tiers: headlines `1.1-1.3`, dense `1.4-1.45`, reading `1.5-1.55`.
- Letter-spacing: Chinese body `0.1-0.2pt` (dense layouts may go to `0.3pt`); English body `0`; small labels and all-caps overlines `+0.2-1pt`.
- Tag backgrounds are solid hex, never `rgba()` (semi-transparent fills render as double rectangles in some PDF engines).
- No decorative ticks, short rules or side accents; every line must encode separation, state or relationship.
- No italic anywhere in documents or landing pages.

## 177. First Principles When No Rule Applies
- Use type size for hierarchy.
- Use spacing for grouping.
- Use ink-blue for emphasis.

## 178. Subtractive Rule
- Decoration earns its place only by encoding data, state, grouping or a relationship.
- Hierarchy comes from contrast in size, weight and space, never from ornament.
- Use the next registered size step, never an in-between size or a decorative rule.
- Do not use corner radius alone to create emphasis.
- To give a card more weight, strengthen its label or opening sentence rather than adding an accent edge.

## 179. Typography Cross-Check
- Set blocks, not glyphs: judge a paragraph as an even gray shape, not one nice letter at a time.
- Measure: reading body about `40-70` characters per line; screen prose held to a ~`720px` reading column, print to the A4 margins.
- Optical over mathematical alignment: nudge hanging quotes, bullets and large display caps by eye until they look aligned.
- Short lines map to ~`1.2x` line spacing (tight/dense tiers); long reading maps to ~`1.5x` (reading tier). Never invent `1.6+` on print body text.
- Left-align body text; centre only short display lines. No centred paragraphs or lists.
- Do not import a multi-weight system (Light/Regular/Medium/Bold); emphasis is size, space and ink-blue.
- Skip em-dash and ornamental punctuation habits.

# Part 24 — Color System

## 180. Surface Palette
- Parchment `#f5f4ed`: page background.
- Ivory `#faf9f5`: quiet filled container.
- Inline code `#f0eee6`: screen annotation, slightly darker than paper.
- Warm sand `#e8e6dc`: button or interactive surface.
- Dark surface `#30302e`: dark container.
- Deep dark `#141413`: dark page background.

## 181. Ink and Text Palette
- Brand ink-blue `#1B365D`: accent, call to action, key labels; keep it to `≤ 5%` of the surface.
- Ink light `#2D5A8A`: links on dark surfaces.
- Near black `#141413`: primary text.
- Dark warm `#3d3d3a`: secondary text, table headers, links.
- Olive `#504e49`: subtext and descriptions.
- Stone `#6b6a64`: tertiary text and metadata.

## 182. Borders
- Border `#e8e6dc`: primary border and section divider.
- Border soft `#e5e3d8`: secondary border and row separator.

## 183. Registered Solid Tints
- Quiet fill `#EEF2F7`.
- Default tag background `#E4ECF5`.
- Never substitute `rgba()` for a registered tint.

## 184. Emphasis Color
- Emphasize a number with the brand color alone; never also make it bold.
- Bold breaks the single-weight design language.
- No more than 3 brand-color accents per page; never several different highlight colors on one page.

## 185. Accent on a Product Site
- On a product landing page, the accent follows the product's own main color.
- If the product has no main color, have the owner pick one; keep ink-blue only as the fallback.
- If a document's brand color is unknown, keep ink-blue rather than inventing a new color.
- For documents, flag a brand color whose hue departs significantly from ink-blue; the warm parchment-and-neutrals constraint stays in force regardless.

# Part 25 — Typography

## 186. Print Type Scale
- Display `36pt`, weight `500`, line-height `1.10`.
- H1 `22pt`, `500`, `1.20`.
- H2 `16pt`, `500`, `1.25`.
- H3 `13pt`, `500`, `1.30`.
- Body lead `11pt`, `400`, `1.55`.
- Body `10pt`, `400`, `1.55`.
- Body dense `9.2pt`, `400`, `1.42`.
- Caption `9pt`, `400`, `1.45`.
- Label `9pt`, `500`, `1.35`.
- Tiny `9pt`, `400`, `1.40`.
- Screen px ≈ pt × `1.33`.

## 187. Minimum Type Floors
- Web text `>= 12px`.
- PDF body text and labels `>= 9pt`.
- Named dense exceptions may drop to `8-8.5pt`: compact tables, running footers, dense resume timelines.
- Never hide a content problem by shrinking type first.

## 188. Font Stacks by Language
- English serif: Charter, Georgia, Palatino, "Times New Roman", serif.
- Chinese serif: TsangerJinKai02 first, then Source Han Serif SC/CN, Noto Serif CJK SC, Noto Serif SC, Songti SC, STSong, SimSun, Georgia, serif.
- Japanese serif: YuMincho / Yu Mincho, Hiragino Mincho ProN, Noto Serif CJK JP, Source Han Serif JP, then the Chinese serif, Georgia, serif (Mincho first).
- Korean serif: Source Han Serif K.
- Monospace: JetBrains Mono, SF Mono, Fira Code, Consolas, Monaco, monospace; in CJK documents add a CJK serif fallback to the mono stack.
- The sans role always equals the serif.

## 189. CJK Fallback Coverage
- Any font-family that may render Chinese or Japanese must include a CJK fallback, including page footers, preformatted text, inline code and SVG labels.
- A pure monospace stack can render missing-glyph boxes for CJK text.
- Never let a CJK-bearing element fall back to a system sans (e.g. PingFang); it clashes with the serif.
- A missing CJK serif shows no fallback boxes, only a heavier, flatter page; never call a CJK document visually verified without confirming the font that actually drew the text.
- A font fallback from the primary CJK serif to Source Han Serif adds roughly `0.3pt` per line; re-check page fit after any font change.

## 190. Numerals
- Use tabular numerals on metric values.
- Use lining and tabular numerals on every element that displays numbers when CJK and Latin digits mix, to keep digits on one baseline.

## 191. Mathematics
- Author formulas only as standard LaTeX, inline or display; render them as proper typeset math.
- Never use Unicode pseudo-formulas, ASCII fractions, formula screenshots or raw TeX on the page.

## 192. Code Blocks
- Code blocks use an ivory fill with `4pt` (block) / `2pt` (inline) radius and no border.
- Syntax highlighting is optional; monochrome code is acceptable.

# Part 26 — Spacing, Margins and Components

## 193. Spacing Scale (4pt Base)
- xs `2-3pt`: inline.
- sm `4-5pt`: tag padding.
- md `8-10pt`: component interior.
- lg `16-20pt`: between components.
- xl `24-32pt`: section-title margin.
- 2xl `40-60pt`: between major sections.
- 3xl `80-120pt`: between chapters.

## 194. A4 Page Margins
- Resume `11 · 13 · 11 · 13 mm` (top, right, bottom, left).
- One-pager `15 · 18 · 15 · 18 mm`.
- Long document `20 · 22 · 22 · 22 mm`.
- Letter `25 mm` all sides.
- Portfolio `12 · 15 · 12 · 15 mm`.
- Equity report `16 · 18 · 18 · 18 mm`.
- Changelog `20 · 22 · 22 · 22 mm`.
- Landing page: screen-first, max-width `1120px`, padding `88px 64px`.

## 195. Radius Scale
- Print radii stay within `2-6pt` and follow physical scale, from compact chips to large media frames.
- Screen radius `8px` for blocks; `999px` only for pill-shaped actions.

## 196. Card
- Ivory background, `4pt` radius, padding `16pt 20pt`: one quiet grouping cue, no border, no shadow.
- A sub-`1pt` closed border plus a radius renders as a double ring; avoid it.

## 197. Tag
- Solid tag background `#E4ECF5`, brand-colored text, `9pt`, weight `500`, padding `1pt 5pt`, radius `3pt`, letter-spacing `0.3pt`.

## 198. Section Title
- Serif `16pt`, weight `500`, near-black, `6pt` bottom margin.
- Type carries the hierarchy; a section head needs no rule, bar or underline.
- Changelog release groups stay scannable through type, numbering and spacing alone.
- Section start: serif scale and margin only, no tick, side bar or short rule.

## 199. Tables
- Full width, collapsed borders, `9.5pt`, `12pt` vertical margin, keep the table unbroken across pages when possible.
- Header: left-aligned, weight `500`, dark-warm color, padding `6pt 8pt`, `0.6pt` bottom rule.
- Body cells: padding `5pt 8pt`, `0.25pt` bottom rule, top vertical alignment.
- Separate rows with whitespace first and neutral hairlines second.
- Compact variant: `8pt`, padding `3pt 6pt` header / `2.5pt 6pt` cells, line-height `1.4`; use only when density requires it.
- Financial variant: right-align all columns except the first, tabular numerals.
- Total row: weight `500`, `0.6pt` neutral top rule, no bottom border.
- Outer columns sit flush with the text edge unless the table is striped.
- Start without striping; add neutral stripes only for `8+` body rows that remain hard to track after rendering.
- All rules use the neutral border color; never a tinted header, category-colored values, brand-colored rules, vertical grid lines or a framed box.
- An empty table cell reads `n/a` (EN), "not applicable" in the local language; never an em dash.

## 200. Metric (Key Figure)
- Value: serif `16pt`, weight `500`, brand color, tabular numerals; label `9pt` olive.
- In print, key figures sit on a transparent baseline row, not in a card, with labels that do not wrap.
- On screen (landing pages, slides), stack value over label vertically, since a horizontal baseline row breaks when any label wraps.
- Metric labels in a 4-column row: soft cap `14-18` characters at `9pt`; trim context rather than wrap.

## 201. Quote and Callout
- Quote: indented (`12pt 16pt` margin, `4pt 0` padding), olive text, reading line-height `1.55`, no fill or side rule.
- Callout to raise a passage: ivory fill with `3pt` radius, no accent edge.

## 202. Cover
- Display heading, right-aligned author and date, heavy whitespace.

## 203. Figures
- Figure SVGs: full width, auto height, and a safe max-height; never a max-height alone (it starves width on wide aspect ratios).

## 204. Multi-Column Body
- Hold text lengths within `±10` characters across parallel columns.

## 205. Image References
- Keep every image inside the document's own images folder or a stable public URL; never depend on a sibling project's private files.

## 206. Slide Bullets
- On slides use numerals `1. 2. 3.` or `•`; an en-dash bullet reads informal at slide scale. Print documents keep the en-dash bullet.

# Part 27 — Choosing a Document Type

## 207. Request-to-Type Mapping
- One-pager: one-pager, proposal summary, executive summary.
- Long document: white paper, long-form article, annual summary, technical report.
- Letter: formal letter, resignation letter, recommendation letter, memo.
- Portfolio: portfolio, case studies.
- Resume: resume, CV.
- Slides: slides, PPT, deck, presentation.
- Equity report: single-stock research report, valuation analysis, investment memo, stock analysis.
- Changelog: update log, changelog, release notes, version history.
- Landing page: landing page, official website, product page.
- Social cards: social-feed image sets, X/Twitter images, carousel cards.

## 208. Deciding Between Two Fitting Types
- 1 page for investors, recruiters or an executive summary: one-pager.
- 1 page of formal correspondence (sales, hiring, resignation, memo): letter.
- Exactly 2 pages of career narrative with project bullets: resume.
- `3-6` visual-heavy pages showcasing projects: portfolio.
- `6-15` pages of sustained argument with low visual density: long document.
- Presentation flow with one assertion per slide: slides.
- Metrics dashboard plus thesis plus price or risk view: equity report.
- Version-by-version release facts: changelog.
- Product showcase, pricing, screenshots and FAQ for a browser: landing page.
- A set of `3:4` images for a social feed, one point per image: social cards.
- Ask only in truly ambiguous cases, e.g. "1.5 pages of career story, heavy visuals" (resume or portfolio?) or "2 pages of executive summary with metric tiles" (one-pager or equity report?).
- A styled changelog document and plain-text release notes are separate deliverables.

## 209. Language Paths
- Each language gets its own variant layout (Chinese, English, Korean); Japanese uses the CJK path with a Mincho face first; other languages follow the CJK or English path by script coverage.
- Japanese, Korean and other best-effort languages need a visual pass on rendered pages before shipping.

## 210. Output Formats
- Decide formats from context rather than asking.
- Any document: HTML source plus PDF deliverable.
- Slides: HTML plus PDF; add an editable PPTX only when an editable deck is requested.
- "Share / post / preview": add PNG.
- "Embed in another document": PNG only.
- Landing page: a ready-to-serve static HTML file, no PDF.
- Word requested for a long document, proposal or equity report: PDF plus DOCX.
- An explicit format request overrides all defaults.

# Part 28 — Planning and Process

## 211. Lock the Contract
- Before creating or changing an output, lock six things: language, document type, output formats, page or length target, visual acceptance criteria, and how it will be verified.
- State the contract in one short line in the requester's language (type, length, formats, planned figures, missing material) and proceed without waiting; adjust if they push back.
- Record audience, the job the document must do, narrative, required facts, required assets, acceptance checks, what must be preserved and any explicit deviations.

## 212. Question Budget
- Infer first. Ask at most once, in one compact question with at most two parts.
- Ask only when two or more of purpose, audience, hard constraints or success criteria are genuinely unresolvable, or two types genuinely both fit.
- Otherwise take the smallest reasonable assumption and report it at the end.

## 213. Route by Current State
- New document or substantial restructuring: lock the contract, distill content, then fill.
- Text replacement, translation or factual correction: preserve layout and styling unless the new copy proves a fit defect.
- A rejected render: treat the render as the brief and follow the feedback protocol.
- A standalone generated illustration or cover: lock the semantic brief before pixels and preserve accepted parts across iterations.
- Use the nearest existing layout; do not add a new layout, style layer or mode unless the request cannot be met without it.
- Never write a layout from scratch; start from the established template. Layout changes stay within spec; a real style change updates the spec and all sibling layouts together.

## 214. Distill Content
- Unless the content maps one-to-one onto the layout's sections or the author said to use it as-is, distill it.
- Every factual claim, number, date, name, source and material reference from the input must land in a section or in the gap report.
- Short atomic values (names, metrics, dates, bullets) survive verbatim; only values over `80` characters may be rephrased.
- Fix structural problems by fixing the content or asking for the fact, never by loosening the structure.

## 215. Gap Report
- List everything the layout needs that the input lacks (facts and materials) in one compact table, shown once.
- Ask one question only when a missing item would change the deliverable.
- Inside the document, mark a gap as `[DATA NEEDED: what]`.
- Never fill a gap with a guess, a stock image, an approximated logo or an invented value; do not describe stock images as placeholders.
- Do not pad slots: three real projects do not become five.

## 216. Document Metadata
- Author: the person's name for resumes, letters and portfolios.
- Description: one sentence, `≤150` characters, drawn from the first two paragraphs.
- Keywords: `3-5`, from the title and section headings.
- Title: from the main heading.

## 217. Visual Review Loop
- After the automated checks pass, open every page image and walk a checklist; one hit means a whole-document sweep for that class of issue.
- Fix the three most visible defects per round and stop after three rounds; list what is still wrong rather than looping.
- If page images cannot be inspected, say "checks passed, visuals unconfirmed", not "done".
- For browser surfaces, screenshot the responsive matrix in every shipped locale before calling it done, without waiting to be asked about mobile.

## 218. Fresh Review
- After the checks and the image pass, review once from the contract rather than from your own rationale: reread the brief, the content coverage and the page images.
- Check every acceptance item and preserve boundary; fix P0/P1 findings, each tied to the page or element that proves it.
- Use an independent reviewer when one is available.

## 219. Definition of Done
- Every deliverable in every promised format.
- The check verdict and page count against the contract.
- Every `[DATA NEEDED]` gap and every assumption, listed.
- An honest visual verdict.

## 220. Feedback Protocol
- When feedback is visual ("looks off", "too crowded", "not elegant"), inspect the current render before asking the requester to choose a value; the render is the evidence and the negative label is the acceptance signal.
- Name the concrete defect in one sentence: page or surface, viewport or state, and whether it is density, hierarchy, alignment, type, color, cropping or text fit.
- Lock the repair boundary: the target that may change and the adjacent pages, sections, content and shared tokens that must stay stable.
- Make the smallest content, geometry, spacing, typography, crop or token change that fixes the defect.
- Verify the affected matrix, not one screenshot: target page, neighbors, total page count, font result and every locale or variant reached by a shared token; for screens, breakpoints, tablet and baseline plus relevant states (focus, loading, empty/error).
- Never say "I'll adjust the spacing" without naming the exact property and its new value.

## 221. Escalate After Two Rounds
- If the same element is still not approved after two adjustment rounds, stop nudging and produce one comparison: current state plus `2-3` labeled variants (A/B/C) of the same content, in the real frame and background, changing only the compared property.
- For choices with no objective criterion (typeface, accent, logo), start with a specimen sheet of up to `5` labeled half-page blocks with identical title-plus-paragraph content.
- After the pick, apply it everywhere and rebuild everything it touches in the same round.

# Part 29 — Writing for the Page

## 222. Data Over Adjectives
- Write the specific numbers and deltas instead of "delivered significant growth".
- Use verified numbers for quantitative claims; do not add a number just to satisfy a quota.
- Explain mechanisms and judgments with concrete facts or examples.

## 223. Judgment Over Execution
- Junior writing says what was done; mid-level says how; senior writing says why the call was made and what it predicted correctly.

## 224. Distinctive Phrasing Over Clichés
- Say it in your own words and skip industry vocabulary ("embrace the AI era", "pioneer digital transformation").
- Use words that fit the author and subject; keep an established voice; do not invent a slogan to make a paragraph seem distinctive.

## 225. Honest Boundaries
- If you didn't do it, don't claim it.
- If the exact number is unknown, write a vague but honest magnitude.
- Attribute collaborators.
- A number you cannot verify ships as a magnitude or a marked gap, never as fake precision.

## 226. Sources Before Phrasing
- Verify companies, products, people, launch dates, versions, funding, financials, market data and technical specs before writing.
- Source priority: author-supplied material > official pages, docs, press releases > filings, app stores, repository releases > credible media.
- Do not write "latest", "new", version numbers or market figures before checking them.
- If sources conflict, list the conflict and ask rather than choosing one.
- Note source and date for the facts that drive the document; skip this for personal drafts where the author supplied everything.

## 227. Derived Figures
- A figure computed from supplied numbers stays beside its inputs ("23 to 9 minutes, about 61% less") or is marked as derived wherever it appears, including captions and tables.
- Never round a derived figure into a standalone headline metric the source did not state; check the arithmetic.

## 228. Materials Serve Recognition
- Branded documents first make the subject recognizable, then add decoration and atmosphere with restraint.
- Confirm logo, product image, UI screenshot and brand color before layout.
- If a key material is missing, mark the gap or ask; never fill the page with unrelated imagery.
- Physical products prefer official product images; digital products prefer real UI screenshots.
- An explicit logo in the current request always beats a stored default.

## 229. Third-Party Figures
- When redrawing a paper figure, patent illustration or official architecture diagram, caption it as "Schematic redrawn".
- Do not style a redraw to look like the original screenshot.
- If the figure carries primary evidentiary value (patent, official spec), embed the original with attribution rather than redrawing.

## 230. Term Annotation Half-Life
- Annotate a term on first appearance; the annotation expires after `8-10` pages or `10` slides.
- Past the half-life, re-annotate with a shorter gloss, e.g. first "LTV (Lifetime Value, total revenue a user contributes before churning)", later "LTV (user lifetime value)".
- Do not re-annotate within the half-life; it reads like explaining a known concept.
- Fast-reading positions (captions, card subtitles, chapter summaries) are especially strict.
- Applies to slides, long documents and equity reports over 8 pages; resumes and one-pagers are too short to trigger it.

## 231. English Term Density in CJK Text
- In Chinese or Japanese body text, at most `1` unannotated English term per sentence; beyond that, split the sentence or add inline glosses.
- Gloss with action words describing what happens (e.g. "warmup" as "ramping up", "rollout" as "running a generation pass", "credit assignment" as "attributing credit to the specific step") rather than abstract concept nouns that merely re-wrap the term.

## 232. Emphasis Rhythm
- At most `2` emphasized items per line.
- Emphasis must be a quantifiable number or a distinctive phrase; never emphasize adjectives.
- In prose-heavy sections, one emphasis per `80-150` words is a healthy default; short sections need no forced highlight.

## 233. Number Formatting
- Use thousands separators: `5,000+`, not `5000+`.
- No full-width comma in metrics.
- No space before percent: `90%`, not `90 %`.
- Prefer honest magnitude (`~$10M`) over false precision (`$9,876,543`).
- Compact dates (`2026.04`) when horizontal space is tight; natural dates (`April 2026`) in prose.
- Use `->` rather than a typographic arrow `→`.
- Never use an em dash as an empty-cell or connector mark.

## 234. Chinese Punctuation
- Use corner brackets 「」 for quoted prose, not straight double quotes.
- Keep numbers, commas, percent signs and dates half-width in metric-heavy areas.
- Add spaces between Chinese text and Latin product names when it improves readability.
- Short copy (UI hints, benefit items, changelog entries) joins clauses with commas; a full stop appears only at the end of the item or not at all.
- Never use the full-width semicolon in user-visible strings; split into two sentences or rejoin with a comma.
- Replace full-width parentheses on slides with a middle dot or a comma.

## 235. English Punctuation
- Use straight quotes unless the document already has a typographic quote convention.

## 236. Diagram and Infographic Wording
- Words inside a figure (title, eyebrow, node label, summary line) are read in seconds; rhetorical flourish reads as noise.
- Avoid slang verbs (e.g. "useless", "stands firm", "back to the furnace", "gate"); rewrite as literal claims.
- Avoid bait phrasing ("must-see", "understand it in one image", "fully master it"); state the figure's actual content.
- Avoid marketing tone ("viral hit", "killer tool") in engineering figures.
- Avoid "flywheel" / "closed loop" unless the audience is fluent; prefer "data loop", "continuous improvement", "four entry points".
- Avoid pinning categories to current product names (they date within a quarter); frame the paradigm ("previous-generation tool paradigm / new-generation execution paradigm") and let readers map products.
- Neutral rewrites: "not reconciled, not done" -> "three checks before delivery"; "if any fails, back to the furnace" -> "if any step fails, return to revision"; "the last gate before delivery" -> "final check before delivery".
- A diagram caption is engineering documentation, not marketing copy; restraint reads as competence.

## 237. Localization Pass
- Literal alignment is the failure mode; meaning alignment is the goal.
- Read each locale straight through as a native reader, not against the source; flag sentences that carry the source language's skeleton (word order, comparison patterns, punctuation rhythm).
- Rewrite, don't adjust: a source-shaped sentence needs its structure rebuilt.
- Localize the expression, preserve the facts; never add claims (e.g. "lifetime updates") not in the source offer.
- Approved phrasing in a locale is fixed; localize around it.
- Report locales and surfaces checked; keep already-natural sentences; a rewrite count is not evidence of quality.

## 238. Pre-Ship Writing Checklist
- Cut jargon like "leverage / unlock / embrace / pioneer".
- Rewrite Chinese filler words meaning "embrace / build out / empower / restructure" in plain language.
- Every paragraph's first sentence must stand alone; if not, the paragraph has no claim.
- Every number is verifiable ("where did this come from?").
- Current facts, versions, dates, funding, financials and specs are reliably sourced.
- Branded documents have logo, product image or UI screenshot coverage, with missing materials marked.
- Wording fits the author and subject, without stock phrases or forced slogans.
- Every brand-colored span is a number or distinctive phrase.
- Paragraph lengths are even; no paragraph over `5` lines.
- Number formats are consistent (commas, percent signs, arrows).
- Chinese punctuation and Chinese/Latin spacing are consistent.
- Page count within the document's constraint (resume 2, one-pager 1, letter 1).
- No AI writing clichés: in Chinese "the essence is", "this means", "it is worth noting", "not only... but also", piled-up dashes; in English em dashes, "It's worth noting", "This means that".
- Documents over 8 pages or 10 slides re-annotate terms past the half-life.
- Multilingual surfaces have a native-reader pass per locale.

## 239. Writing References
- Paul Graham's essays: short, direct, judgmental.
- Stripe Press books: print-grade typography with deep content; the craft of the single sentence.
- Minto's Pyramid Principle: conclusion first, evidence below; the shape of every one-pager and executive summary.
- Ben Horowitz's blog: technical and business judgment in plain prose; the model for long-document voice.

# Part 30 — Headlines and Structure by Document Type

## 240. Core Quality Rule per Type
- Resume: every bullet has action, honest scope and a concrete result.
- Portfolio: open with the problem and stakes, not the project name.
- Slides: titles are full-sentence assertions, not topic labels.
- Equity report: lead with variant perception, what you see that the market doesn't.
- Long document: each chapter's claim paragraph survives the "so what?" test.
- One-pager: metrics are the headline; if the 4 cards don't tell the story, the metrics are wrong.
- Letter: the first paragraph states purpose in one sentence.
- Changelog: one sentence per change, verb-led, user-facing language.
- Social cards: the author's words unchanged; layout fixes every short line, never a rewrite.
- Structure is necessary, not sufficient.

## 241. One-Pager
- The reader grasps the point in `30` seconds; anything not serving that is bloat.
- Structure: serif display headline plus one-line subtitle; `3-4` metric cards, numbers first; core argument in `1-2` paragraphs; `3-5` short evidence or roadmap bullets; next step or contact in the footer.
- Length: English `200-350` words; Chinese `400-600` characters.
- All section headlines must work as a standalone outline.
- Data fills `30%+` of the body.
- Company or product one-pagers confirm logo, core screenshot or product image, and the source of key metrics.
- No opening ceremony ("In recent years, as technology has rapidly evolved...").
- The lead paragraph contains the single sharpest claim, not context-setting.
- Each bullet is evidence: fact + number + "so what"; not a restated argument.
- The footer is for contact and classification, not one more argument.
- The ask belongs above the fold, never implied.

## 242. Long Document
- Slots: cover, contents, executive summary, body, optional appendix.
- The executive summary fits on one page with `3-5` takeaways.
- Each chapter stands alone as a mini-essay: claim -> evidence -> conclusion.
- Every chapter opens with a `2-3` sentence claim paragraph that answers "why should I care?".
- Break long paragraphs with real evidence, an attributed quote or a useful figure; otherwise edit the prose or add a descriptive subhead. Never invent a component or callout on a fixed cadence for rhythm.
- Highlight key data and conclusions with the brand-color highlight.
- Preserve inline source cues ("(Gartner, 2025)", "according to the company's 10-K") so readers can tell fact, judgment and inference apart.
- Support factual claims with sources, examples or verified measurements; do not add numbers to paragraphs explaining a mechanism or judgment.
- Address counter-arguments before they become reader objections.
- Give a major section its own opener only when it improves navigation; no ceremonial blank pages.
- When converting from Markdown, remove or convert thematic breaks, bold markers and inline-code backticks.

## 243. Proposal: Work-Volume vs Attention Frame
- A proposal is a long document arguing for a specific commercial engagement.
- Work-volume frame: sells execution of N items, priced by hours or deliverables, fixed commitment, reader acts as procurement, signals "I can do these tasks"; fits outsourced delivery.
- Attention frame: sells allocation of judgment, priced as a total engagement, flexes with the buyer's cadence, reader is hiring an advisor, signals "I bet on these directions"; fits senior advisory.
- Pick one frame and stay consistent; itemizing advisory work invites the reader to divide fee by hours and treat you as a vendor.
- In the attention frame, avoid rigid monthly volumes ("N reports per month"); use "by milestone" or "as the cadence requires".
- Avoid exhaustive coverage ("full involvement at every release"); use "deep involvement at major milestones".
- Avoid specific session counts ("20 sessions"); anchor on depth of content.
- Avoid "full-X" totalizers ("all-round", "full-chain", "end-to-end"); use "key X" or "core X".

## 244. Proposal: With-Price vs Without-Price
- Operating founder or direct buyer: print the price; decision-makers want the number.
- Intermediary or business contact: omit the price to leave room for their commercial layer.
- Investor or board reader: omit the price; strategy first.
- The without-price variant drops the large-figure hero, keeps the value anchors, and renames the chapter from "Plan & investment" to "Directions & value".

## 245. Proposal: Kickoff-Period Emphasis
- Twelve-month timelines fail when every month gets equal weight.
- Surface the first `60` days as a separate beat before the timeline table: one paragraph on time scarcity, then one paragraph per month (bold date, module, `2-3` concrete actions, outcome).
- Then show the month-by-month table as detail: story before grid.

## 246. Letter
- Slots: letterhead, date, salutation, body, sign-off, signature, optional enclosure.
- Body of `3-5` paragraphs; fits on one page; two pages means it is a memo or proposal.
- Minimal, no decorative elements; serif body for an editorial feel.
- Slightly larger body type `11-12pt`; paragraph spacing `≥ 10pt`; signature in serif `500`.
- First paragraph states purpose in one sentence; last paragraph states the specific ask or next step; everything between is evidence, one point per paragraph.
- Tone: resignation grateful and clear; recommendation specific and enthusiastic; proposal value-first and concrete; personal statement authentic and structured.
- Sign-off matches formality: "Sincerely" formal, "Best regards" professional-warm, "Warm regards" personal; Chinese letters use a formal traditional closing.

## 247. Portfolio
- Structure: cover (name, one-line positioning, two-to-three-line introduction, contact); `1-2` pages per project (title, type tag, date range, one-line description, `2-3` hero images, role + challenge + outcome); selected-works short list; contact.
- The introduction lives on the cover; an About page appears only when there is enough material to fill a whole page; one that would render under half full is deleted, not padded.
- Visuals first, text supports.
- Open every case study with the problem and its stakes, e.g. abandonment at 73% cut to 31%, not "I redesigned the dashboard".
- Show `2-3` decision points with the tradeoff, not just the winner.
- State exact role and scope ("designed" vs "led" vs "contributed to").
- `3-5` deep case studies beat 12 shallow ones.
- Close the loop with an observable result for each problem; state unresolved limits honestly.
- Include user quotes only when supplied or sourced.
- Image priority: final product screenshots or real photos > design mockups > code screenshots.
- Don't list every tech stack; a monospace tag row is enough.

## 248. Slides
- Every title is a full declarative sentence: "Q3 revenue grew 23% because enterprise deals closed 2x faster", not "Q3 Performance".
- The body provides one piece of evidence for the assertion; prefer one chart over seven bullet fragments.
- `20-40` words per slide maximum; over 40, split or convert to a visual.
- `5` items per list maximum.
- Three-act arc: setup (stakes), evidence (case), resolution (payoff); act lengths scale with deck size.
- A "so what" moment every `3-4` slides.
- End with one clear ask or recommendation, not a "Key Takeaways" slide of 8 points.

## 249. Slide Eyebrow vs Title
- The eyebrow is a stable cross-slide section label ("Growth / Q3 Results"); the title is a page-unique claim.
- They must never say the same thing in different words.
- If removing the eyebrow makes the title ambiguous, the title is too weak; if the title makes the eyebrow redundant, the eyebrow is a disguised topic label.

## 250. Slide Captions
- Every caption answers "why does this slide matter": a tradeoff, an applicability boundary, a next step, or an insight the diagram cannot say.
- Never restate the title or narrate the flow diagram in prose.
- If removing the caption changes nothing, rewrite it.

## 251. Term Consistency
- After drafting, list every domain term used 3+ times and confirm exactly one spelling and capitalization each ("LLM" vs "llm" vs "large language model" signals an unreviewed draft).

## 252. Equity Report
- Lead with variant perception and tie every thesis driver to a measurable financial impact.
- Investment thesis on page 1 above the fold: rating, price target if applicable, `3-5` thesis drivers.
- Every claim backed by a number or source; no unquantified superlatives ("strong management team" -> "23% revenue CAGR over 5 years with debt-to-equity below 0.4").
- At least two valuation methods with sensitivity ranges; single-method valuation is amateur.
- Catalysts carry dates and expected magnitude.
- Competitive positioning uses market share numbers, not narrative.
- Risks are quantified and connected to the model, not generic disclaimers.
- Professional tone ("we estimate", "our base case", "we see upside to"); never hype ("this stock will moon", "buy the dip").
- Acknowledge counter-arguments before dismissing them.
- Separate GAAP from non-GAAP; flag one-time items (warranty reserves, tax benefits, restructuring charges).

## 253. Changelog
- One sentence per change, verb-led, user-facing; if a user can't understand it alone, rewrite ("Fix crash when switching tabs rapidly on iPad", not "Refactored internal state management module").
- Name versions and reasons: "Upgrade OpenSSL to 3.2.1 (patches CVE-...)", not "Updated dependencies".
- Breaking changes always first, with a migration path.
- Group by user impact (Breaking / Features / Fixes), not by component or file; item counts do not set release boundaries.
- No internal jargon or internal class names.
- Breaking-change markers use a warm sienna pair: background `#f0e0d8`, text `#8b4513`.

## 254. Social Cards
- Carry the author's words unchanged; layout absorbs every fit problem, and copy edits are the author's call.
- One card per `1242x1660` (`3:4`) image; one paper color for the whole set.
- The cover headline equals the post title, and every card's footer repeats it.
- One point per card; list items `2-5` per card, grouped so neighboring cards read equally full and each card mostly full.
- The cover needs a real photo or screenshot; a text-only set ships only with the author's agreement.
- Keep firsthand experience, quoted advice and the author's conclusions apart; do not add a lesson to each card.
- For a product, show the product (what it is, a real screenshot) before the update.
- Fix a short last line with layout, not rewording.

## 255. SEO and Content-Marketing Articles
- A teaching document with the product as a worked example, not a brochure.
- The spine is a transferable mechanism explained at teaching depth with real commands, code or architecture diagrams.
- The product enters after the mechanism is established and stays out of the title's subject position.
- Deletion test: remove every product mention; the article must still be useful.
- Conclude with both paths: what the reader can do manually, then what the product automates.

# Part 31 — Page Density

## 256. Fill Targets
- Applies to slides, long documents, portfolios, equity reports and changelogs; resume, one-pager and letter have their own length contracts.
- Body pages target `60-80%` fill; cover, contents and closing colophon are exempt.
- The last body page may close at `40-60%`; forcing balance there usually means padding.
- The most common multi-page defect is content split too thin.

## 257. Per-Type Density Floors
- Slides: `1` assertion + `3-5` supporting items, or `1` chart + `2-3` callouts; under 3 items and no chart, merge into an adjacent slide.
- Long document: `1` chapter heading + `2-4` paragraphs + at most `1` figure; a chapter under `40%` of a page merges into a neighbor.
- Portfolio: `1` project header + `1` hero image + `3-5` outcome bullets; no image and under 3 outcomes, merge with an adjacent project.
- Equity report: `1` section + `1` table or chart + supporting prose; a page with only a 2-row table combines sections.
- Changelog: `1` version block + `4-8` entries; under 4 entries shares the page with the prior version.

## 258. Fixing a Sparse Page
- A body page under `50%` full gets, in order: merge upward; merge downward; remove the page and fold its one useful assertion into a neighbor; convert existing information to a small table or diagram only if that form is clearer on its own merits.
- Never fill a sparse page with filler prose, a heading restated as a sentence, invented statistics, the prior page reworded, or a callout, chart, icon or image whose only job is to occupy space.
- If no merge applies, the page should not exist.
- A pinned slide conclusion is valid only when it adds a real relationship, constraint or conclusion, never to fill trailing whitespace.

# Part 32 — Diagrams, Charts and Captions

## 259. Diagram Types
- Architecture (components and connections), architecture board (report-scale five-layer system), flowchart (decision branches), quadrant (`2×2` positioning), state machine, timeline, swimlane (cross-responsibility process), tree, layer stack, Venn, plus sequence, class and ER diagrams.
- Embed diagrams as inline vector figures inside a figure container.

## 260. Data Chart Limits
- Bar: category comparison, up to `8` groups × `3` series.
- Line: trends over time, up to `12` points × `3` lines.
- Donut: proportional breakdown, up to `6` segments.
- Horizontal bar: ranking, or a share with `7+` parts, up to `12` rows.
- Candlestick: OHLC price history, up to `30` days.
- Waterfall: revenue bridge or decomposition.

## 261. Generated, Not Hand-Drawn Charts
- Charts from data are generated from a numeric spec, never drawn by hand; bar heights or arc endpoints typed by hand drift from their labels.
- To change a number, change the data and regenerate; a chart whose marks disagree with its data is a defect.
- Chart colors, axes and geometry come from the shared chart system, not per-document choices.

## 262. Chart Titles and Value
- Title states the insight ("Revenue accelerated after Q2 price change"), not the topic ("Revenue by Quarter").
- A chart that restates numbers already in the text must add a dimension (comparison, trend, distribution) or go.
- The text must match what the chart shows.

## 263. Illustration Brief Style
- Redraws use a warm parchment `#f5f4ed` background, never pure white.
- One accent only, ink-blue `#1B365D`; everything else warm gray with a yellow-brown undertone.
- Thin single-line geometric strokes and simple flat icons; no gradients, drop shadows or 3D.
- Serif labels, generous whitespace, calm composition like a figure in a well-typeset report.

## 264. Maintained Diagram Assets
- A diagram that lives in a repository should keep source, an exported image re-exported after every change, and a brief (must preserve / suggested additions / visual direction / sister boundaries) in sync.
- Do an evidence pass before drawing; encode maturity visibly (shipped / in build / future).

## 265. Image Slots
- Decide the slot ratio first, then crop, pad or generate to that ratio.
- Preserve real screenshots; never AI-redesign them into fake UI; use padding or split panels instead.
- Normalize the frame and padding across a group of screenshots; keep content intact inside it.
- If a product image is missing, mark the gap or omit the panel; do not substitute abstract atmosphere.

# Part 33 — Landing Pages

## 266. Landing Page Purpose
- A landing page is a conversion surface, not a brochure; every element builds trust or wastes attention.
- No italic on landing pages: captions, subtitles and footer stay upright, separated by size, color and position; italic only marks a font face, syntax tokens or the author's own emphasis.

## 267. Hero
- Name the real product category in the first viewport; if the product outgrew its old anchor, rewrite the category instead of adding bullets under it.
- Tagline is one sentence in the reader's words.
- Key-fact tokens are scannable proof: price, platform, refund policy, compatibility; no adjectives (`$9 lifetime` beats "Affordable pricing for everyone").
- CTA pair: ghost button for the low-commitment try action, filled button for the revenue action; never three buttons.

## 268. Section Ledes
- A section lede is one plain sentence: no bold, no brand color, no second qualifying line; caveats belong in the FAQ or pricing terms.
- Competitor names stay out of the hero and ledes; they belong in the FAQ comparison answer and the meta description.

## 269. Gallery
- Show, don't describe: real screenshots replace feature paragraphs; each panel is one shipped tool, workflow or reachable state.
- Technical products may show the workflow itself (terminal transcript, command draft, error recovery) when it shows the real review/confirm boundary.
- Captions add information; omit a caption that repeats the heading.
- `3-6` panels maximum; users remember 4.

## 270. Features
- Name the feature directly; add a subtitle only for useful context; no required metaphor.
- Description answers "so what?" in one paragraph of `2-3` sentences.
- Mechanics (activation, boundaries, safety rules, edge cases) fold into the FAQ; a standalone "behaviors" section is documentation leaking into the pitch.
- Run every feature row the same direction so copy keeps one left edge; do not alternate rows to escape a list look. Mirror only paragraph-sized text masses; get rhythm from unequal weight (a lead row with a larger visual, fewer points on supporting rows).

## 271. Principles
- Title is the commitment ("Nothing leaves your Mac"); description is the proof of enforcement.
- `4-6` principles; more than 6 dilutes; with 8, two are redundant.

## 272. Social Proof
- Every quote visible before expansion praises the product form sold on this page; praise for a sibling product appears only after expansion and clearly attributed, or not at all.
- Order by credibility, not recency: recognizable names, then high-engagement posts, then well-written quotes from unknowns.
- Replace, trim or annotate quotes containing expired facts (old prices, stale versions).
- Roughly `9-12` quotes before the fold; the wall must not push pricing out of reach; the rest behind one expand control, no pagination.
- A "see more" external link is a card in the same visual language at the end of the wall, one line of copy.

## 273. Pricing
- Benefits are the headline: `4-6` one-line benefit points of similar length, no wrapping, a plain borderless list.
- State the price once at medium weight (`$N · One-time purchase` shape); a giant price turns the section into a price tag. Emphasis comes from placement and whitespace.
- The number appears at most twice on the page: once in pricing, at most once as a hero token.
- CTA buttons carry the action, never the price: "Buy Product", not "Buy for $19".
- Keep the block quiet: no border, shadow or gradient; at most one restrained fill.
- Compare honestly: name competitors, show their subscription price struck through, then your one-time price.
- Terms at the bottom: payment methods, refund policy, device limit; factual, not promotional.
- A currency symbol stays on the digit baseline (about `0.74em`, line-height `1`, tiny downward nudge); never shrink it to half size and superscript it.

## 274. FAQ
- First question is the positioning question ("How is this different from X?" or "Who is this not for?").
- Compare against tools users already know, named from the source material.
- Lead with the question the user is actually thinking ("Is it free?" before refund policy).
- Answers in `1-2` sentences; over 3 sentences belongs in docs.
- `6-8` questions maximum covering positioning, free tier, comparison, permissions/privacy, data collection, purchase flow, licensing.
- Keep the FAQ, structured data and any AI-facing product summary as one public fact set, updated together.

## 275. Footer
- Brand plus relevant links or license info; preserve an established tagline, never invent a poetic closing line.
- Link only to pages that exist; dead links destroy trust faster than missing links.

## 276. Multilingual Sites
- Language menu items need room for descenders: min-height `32px`, padding `6px 10px`, line-height `1.35`, plus an invisible hover bridge from trigger to menu.
- Every locale has alternate-language links (including an x-default) and social-locale alternates.
- When a fact (price, version, install path) changes, update every locale page and the structured data together.
- When the product UI is localized, capture screenshots per locale.
- Site chrome (social image, favicon, theme color) is one set for every page and subsite.
- Social preview image: a real baseline JPEG at `1200x630`.
- Dynamic counts (stars, users) are fetched at build time or carry a snapshot date.
- Templates carry placeholders, never real product data.

## 277. Responsive Verification
- Check breakpoints, tablet and baseline widths in every shipped locale, plus default, focus/selected, loading, empty/error and transition states where they exist.

# Part 34 — Resume Writing

## 278. Resume Hard Constraints
- Strictly `2` A4 pages, both visually used.
- Every project follows Role / Actions / Impact.
- `5` core skills, each with at least one brand-color emphasis.
- Team size, tech stack and narrative voice stay consistent throughout.

## 279. Resume Sections
- Header plus `4` metric cards.
- Summary of ~`50` English words or ~`80` Chinese characters.
- Timeline of `3` steps.
- `3-5` core projects.
- Optional public work / impact.
- `5` core skills.
- Education.

## 280. Metric Card Selection
- `1` card on time (years, consistency).
- `1` card on scale (team, users, projects or other quantifiable scope).
- `2` cards on results (quantifiable external proof).
- Top metrics stack value over label in each of four columns; labels stay single-line, and a wrapping label is shortened before the layout changes.
- In English, put the unit inside the value (`8 yrs`, `120ms`, `$280K`).

## 281. Impact Formula
- Action + honest scope + observable result; connect to business outcomes (revenue, cost, reliability, retention, time-to-market).
- Start every bullet with a strong past-tense verb (designed, led, reduced, migrated); never "Responsible for" or "Helped with".
- Use verified numbers when they explain result or scope; otherwise state the observable outcome without inventing one.
- Prefer before/after pairs ("from X to Y") over "improved by Z%".
- Match the source's precision; label estimates as estimates.
- Example: "Redesigned order pipeline serving 2M daily txns, cut p99 latency from 800ms to 120ms, saved $340K/yr", not "Worked on backend services".
- Senior resumes show judgment ("evaluated 3 approaches, chose Y because of tradeoff Z") and multiplier effect ("mentored 4 engineers, 2 promoted within 12 months").

## 282. Three-Part Row Limits
- Chinese: Role target `50` / hard limit `60` characters; Actions `70` / `80`; Impact `90` / `100`.
- English: Role target `35` / hard limit `40` words; Actions `45` / `55`; Impact `55` / `65`.
- These are maximums; shorter is better when complete.
- Role: what the project was, why it existed, your position; no verbs yet.
- Actions: decisions and techniques, one concrete approach per sentence.
- Impact: observable outcome; team size or traffic describes scope, not a result.
- Self-check: read Impact aloud; if it sounds like process ("improved the pipeline") rather than result ("reduced p95 latency from 800ms to 120ms"), rewrite.

## 283. Recruiter Pass
- Before rendering, reread every project as a recruiter would: Role carries your position, not background alone; Actions verb-led; Impact an outcome, not a restated process.
- No row repeats another row's information.
- Fix failing rows from the source; if no outcome fact exists, ask for it; never pad or fall back to generic claims ("ensured stable operation", "improved efficiency").
- The pass is silent unless a row cannot be fixed without new information.

## 284. Source and Truth Pass
- With multiple sources (old resume, self-review, annual review, promotion packet, notes), extract every claim, number, project name, role label and result from each.
- Use each source for its best material: annual reviews often have the strongest metrics; old resumes the clearest narrative.
- When sources conflict on scope, owner, unit or number, ask; never silently pick the bigger claim.
- Drop numbers with unclear unit or basis; a precise traceable number beats a bigger rounded estimate.
- Precise before/after values (`S1 68% / S2 93%`) beat "about 70%"; omit or question apparent typos.

## 285. Personal Information Hygiene
- Age and gender are optional metadata, included only when supplied and expected by the channel (e.g. some Chinese or Korean recruiting); place them in the contact line after location, never in metrics, summary or project copy.
- Never invent personal details; never include expected salary in the body (availability and negotiation go in a separate note).
- Use role positioning ("AI / Agent engineering") instead of an old-style "Job objective: front-end engineer" line.

## 286. Ownership and Title Calibration
- Pick the lowest truthful role word that reflects the contribution.
- Owner / lead / direction owner: defined direction, owned architecture or outcome, clearly accountable; use when you can defend strategy, tradeoffs and result.
- Drove / led: independently carried a line or module to production.
- Coordinated: pulled people or systems together around a bounded goal.
- Module owner: owned a specific module, slice or workflow inside a larger line.
- Contributed / core contributor: delivered a distinct piece of a shared project.
- Implemented / participated: solid execution without ownership.
- Not every project says "led"; mixing owner-level and narrower contributions reads more credible.

## 287. Team Resume Mode
- When polishing several resumes from one team, first list each person's projects, aliases, role labels and headline metrics.
- Mark shared projects, near-duplicate names and reused metrics.
- Confirm a unique owner for any owner-level claim; downgrade others' role words and switch them to their distinct contribution or metric dimension.

## 288. Project Metric Rows
- Horizontal by default for `2-3` short metrics.
- Vertical when any label exceeds `18` characters, three or more metrics have unequal lengths, or the card already has long rows.
- Never vertical for exactly two short metrics; never wrap metric rows (uneven splits look like errors).

## 289. Highlight Density
- One brand-color highlight per project row, maximum `2` across a project's three rows.
- Highlight numbers with units (`120ms`, `38%`) or a distinctive noun when no number exists.
- Never highlight adjectives or qualifiers ("significantly", "dramatically", "key"), two spans in one row, or a whole clause.

## 290. Timeline Arc
- The timeline shows career judgment, not job chronology: `3` steps, one sentence each.
- Foundation (constraint that shaped early thinking), inflection (decision that changed what you optimized for), present (operating mode and what it produces).
- List shifts in judgment and scope, e.g. "Shifted from feature delivery to owning the model quality loop end-to-end", not "Joined the AI team as senior engineer".

## 291. Open Source Entries
- Each entry: name, one-line description, star count; no README summaries or feature lists.
- Description formula: `[language or stack] · [what it does] · [platform or audience]`, e.g. "Swift · native Markdown notes · macOS AppKit".
- Enlarge star counts on the top two flagship entries only.
- The open-source highlight is one short anecdote of external validation (a notable share, a community, an unexpected audience), not a feature summary.
- Intro: one positioning sentence plus one sentence with aggregate numbers.

## 292. Page 2 Content
- Convictions: one judgment call plus one piece of downstream evidence each, not project summaries.
- Skills: one capability area per row, demonstrated with one concrete example.
- Education: one line, with any judgment-flavored note (declined grad school, switched majors), which signals self-direction better than GPA.
- Page 2 has more room; do not compress it to match page 1.

## 293. Density Tuning by Project Count
- 3 projects: body `9.4pt`, project line-height `1.42`, section-title top margin `6mm`.
- 4 projects (default): `9.2pt`, `1.40`, `5mm`.
- 5 projects (dense): `9pt`, `1.38` (CN) / `1.40` (EN), `3.5mm`; timeline body may drop to `8.5pt` in Chinese.
- 6 projects: `9pt`, `1.36` (CN) / `1.38` (EN), `3mm`; six projects on a page signals the list needs editing, not tightening.
- Tighten only page 1; never change page-2 line-heights or header typography.
- Page-2 references: open-source intro line-height `1.55`, convictions `1.40`, at least `4mm` buffer between header and first section.
- Never scale page-2 type below `9pt`; if it overflows, cut one conviction card or reduce skills to 2 rows.
- If page 2 is long, reduce individual blocks, never globally.

## 294. Two-Page Balance
- Exactly 2 pages; each page fill around `83-95%`; the two pages differ by less than `12` percentage points.
- If page 2 is too empty, fix content before typography: split a mixed project only if it truly holds two systems or result dimensions; add a skills row only if the source supports it; cut filler and repeated metrics before shrinking fonts.
- Never fill space by padding, duplicating a number or splitting one sentence across two lines.

## 295. Thin Source
- If total fill across both pages is below about `166%` (both pages at the 83% floor), the source cannot hold two pages; no break placement or density setting closes the gap.
- Three employers with eight bullets and one open-source line typically render to `120-135%`.
- Never start a continuation section ("Experience (cont.)") on a forced new page; it turns one shortfall into two half-empty pages.
- Keep two pages; collapsing to one breaks the contract.
- Stop at the 3-project density row; inflating type or spacing beyond it only reaches the floor with whitespace.
- Remove page-2 sections the source has nothing for, list missing material as gaps, and say which facts would close the shortfall.

## 296. Resume Visual Rhythm
- Header and section titles carry the only structural rules: a single quiet warm full-width bottom rule, never a brand-color left bar.
- Project rows have no top or bottom borders; separate by padding and project-name weight, avoiding double rules or lonely page-top lines.
- Highlight boxes (e.g. open-source validation) use tint and radius only, no vertical brand rail.

## 297. AI Engineering Resumes
- Show AI as an engineered system: evaluation gates, feedback loops, harnesses, regression checks, context boundaries, rollback paths.
- Make the human / AI division of labor clear: humans define scope, tradeoffs and risk; AI implements, repairs, classifies or generates under constraints.
- Tie metrics to the mechanism: pass rate, failure rate, iteration cycle, case coverage, retrieval precision, hallucination reduction, throughput, review load.
- Show operating-model evolution: prompt craft -> context engineering -> tool orchestration -> automated validation.
- Avoid listing model or tool names as skills, unbaselined claims ("AI improved efficiency by 50%"), passing an API demo off as an agent platform, claiming team results as individual, and filler ("empower", "lever", "combo punch", "at scale") without mechanism and metric.

# Part 35 — Anti-Patterns

## 298. Content Emptiness
- Adjective pile-up without numbers: state the number ("Revenue grew 34% YoY to $12M").
- Opening filler ("In today's rapidly evolving landscape..."): delete it and start with the first real claim.
- Restating the heading as a sentence: the body must add information the heading lacks.
- Vague time references ("recently", "in the near future"): pin to a date or quarter ("Launched Q1 2026").
- Synonyms masking repetition: one claim, one proof, move on.

## 299. Metric Fabrication
- Round numbers implying precision ("exactly 10,000" for "around 10K"): match the source's precision.
- Fake decimal precision ("23.7%" uncited): verify and cite, or mark unknown; rounding does not validate it.
- Metric-narrative disconnect: text must match the chart.
- Invented baselines ("3x faster than alternatives"): name the alternative and benchmark method, or remove.
- Mixed time periods (YoY next to QoQ): label every comparison window.
- Unlabelled derived figures: keep inputs beside them or mark them derived.

## 300. Structure Mimicry
- Resume bullet without result: action + scope + result ("Led 8-person team to ship v2.0, reducing churn 15%").
- Slots filled with filler ("Communication, Teamwork, Problem-solving"): name the specific skill and where it applied, or cut the section.
- Equity report without variant perception: state what the market gets wrong.
- One-pager without a clear ask: put the ask above the fold.
- Slide title as label ("Q3 Results"): make it an assertion ("Q3 revenue beat guidance by 12%").

## 301. Visual Excess
- More than 3 brand-color accents per page.
- Chart with no insight title.
- Decorative chart restating the text.
- Icons or emoji as section markers: use typographic hierarchy.
- Label chrome over every heading (`01 · FEATURES` on non-sequential sections, `Design · Build · Ship` joining non-data words): number only real sequences (chapters, slides, steps); at most one eyebrow on the cover or hero; a middle dot only separates data fields on one line.
- Hand-placed chart geometry.

## 302. Source Gaps
- Unverified version numbers: check the official source.
- "Latest" without a date: name it with an as-of date ("as of 2026-04").
- Leadership claims without market data: cite the ranking or say "one of the established solutions".
- Assumed availability ("all major platforms"): list verified platforms.
- Identity leaks in demo content: swap real resume or proposal details (job-search phrases, client names, quote amounts, engagement periods) for public or generic data before sharing, and list what was swapped.

## 303. Tone Contamination
- Chinese corporate speak ("empower enterprise digital transformation", "build a one-stop solution"): say what it does ("help the company move paper processes online").
- English corporate speak ("leverage our platform to unlock synergies"): "use the platform to share data between teams".
- Caption restating the flow diagram ("six sources -> six filters -> mix design -> training shards, four steps in series"): give judgment beyond the figure ("sources set the knowledge boundary, filtering sets cleanliness, mix sets capability emphasis").
- AI-tone clichés in Chinese ("essentially, the model is predicting — this means..."), heavy dashes: drop meta-commentary, state the conclusion, replace dashes with colons or full stops.
- Sans stack without CJK fallback on headers: use the serif for any element that may render CJK.
- Caption restating the slide title ("ORM vs PRM comparison" / "comparing ORM and PRM"): give decision criteria, applicable scenarios or the next step.

## 304. Slide Anti-Patterns
- Ghost deck fails: if titles alone read as topics, fix titles and order before layout.
- Multiple evidence shapes on one slide (chart + screenshot + code + quote): pick the primary proof and split the rest.
- Visual brief leaking into copy ("21:9 ultra-wide screenshot with quiet background"): keep prompts and crop notes out of captions.
- Fake layout-mapping phase: inventory a template only when a real brand deck is supplied.

# Part 36 — Brand Profiles

## 305. Profile Fields
- Identity: name, role title, email, website (no protocol), GitHub and X handles (expanded to full URLs), city, country.
- Brand: company, tagline, logo, brand color hex.
- Defaults: language, default document type, output format (PDF / PPTX / both), page size (`a4` or `letter`), always-include-contents toggle.
- Conventions: date format (default `YYYY-MM-DD`), currency locale (USD -> `$`, M/B; CNY -> yuan with 10k/100M units), footer note, signature block, tone (formal / balanced / casual).
- Freeform habit notes describe tendencies, scoped to document types where relevant.
- Leave fields blank without a strong preference; silence is fine.

## 306. Applying Profile Values
- Profile values fill matching placeholders only; if no slot exists, do not insert the field.
- Use profile defaults only when the request is ambiguous (language, type, format, page size, currency, tone, footer, contents); still ask about genuinely unclear intent.
- Tone mapping: formal -> deferential register; casual -> relaxed; balanced -> default.
- Apply a profile logo only to layouts with a logo slot, only when the request names none; if the file is missing, render without a logo and never insert a broken image or announce the omission.
- Habit notes merge with writing guidance and are advisory; when content doesn't fit a preference, follow the content.

## 307. Profile Guardrails
- The profile is a fallback, not a first resort; current-request signals win.
- Editorial judgment may silently override any profile layer (e.g. a playful changelog overrides a formal tone default).
- Vary surface details across documents: opening hook, chart selection, section order and density are chosen fresh; two documents of one type should not look like clones, even with the same logo.
- The profile never introduces new content.
- Apply silently; never write "applied your profile defaults".

## 308. Precedence
- Explicit prompt > editorial judgment for this document > habit notes > profile defaults > built-in defaults.

## 309. Drafting a Brand from a Website
- Extract one accent only, darkening it in lightness steps until it reaches `4.5:1` contrast on parchment `#f5f4ed`.
- Record site fonts and logo candidates as notes but keep the serif stacks.
- Show the draft and use it only after acceptance.

## 310. Matching Another Project's Style
- Only when explicitly asked, read that project's declared design tokens (prefer declared variables over inline literals): dominant colors, font stack, spacing scale, radius scale.
- Apply them as visual customization, never over a value the requester gave this turn; report "extracted N colors / M fonts" in one line.
- Skip when the source has no style definitions or conflicts with current instructions.

# Part 37 — Slide Deck Preflight

## 311. Deck Format Path
- Default to an HTML-rendered PDF deck; editable PPTX only when explicitly required; Markdown-authored decks only when explicitly requested.

## 312. Slide Page Size
- Default `280mm 158mm`; fits most decks.
- `297mm 167mm` when a bit more room is wanted.
- `338mm 190mm` for heavy content or many data points per page.
- Ask only if length or density constraints were mentioned.

## 313. Content Preflight Questions
- Audience and venue: live keynote, investor 1:1 or async share link?
- Length target: `15` min ≈ `10` slides; `30` min ≈ `20`; `45` min ≈ `25-30`.
- Source material: outline, document, notes, data?
- Images: screenshots, charts, logos, product images; which slides need real evidence slots; is a separate visual brief needed?
- Hard constraints: brand colors, required logo, editable format, mandatory slides?
- Format confirmation: a deck, or a one-pager styled like a deck?
- Treat these as an internal checklist, not a questionnaire; ask only what materially changes the deck.

## 314. Slide Content Rules
- Ghost deck test: titles read in order must tell the argument.
- One evidence shape per slide: chart, table, screenshot, code, quote or conclusion.
- Audience copy never contains image prompts, crop instructions or generation notes.
- No standalone section-divider slides in short decks; use the eyebrow for section numbering.
- No full-width CJK parentheses; use a middle dot or comma.
- Each bullet fits on one line; trim until it does.
- `2×2` layouts use a table structure.
- A pinned conclusion sits at the bottom, `12mm` from the edge.

## 315. Deck Rhythm
- For decks of `12+` slides: an ink-blue full-bleed chapter divider every `4-6` slides.
- No run of more than `5` consecutive content slides.
- Include at least one quote or metrics slide to vary density.
- Monotony is a structure failure, not a content one.

# Part 38 — Design Tokens

## 316. Background Tokens
- Parchment `#f5f4ed`.
- Ivory `#faf9f5`.
- Inline-code background `#f0eee6`.

## 317. Line Tokens
- Border `#e8e6dc`.
- Border soft `#e5e3d8`.
- Line `#d8d5c8`.

## 318. Brand Tokens
- Brand `#1B365D`.
- Brand tint `#EEF2F7`.
- Tag background `#E4ECF5`.

## 319. Text Tokens
- Near black `#141413`.
- Dark warm `#3d3d3a`.
- Charcoal `#4d4c48`.
- Olive `#504e49`.
- Stone `#6b6a64`.

## 320. State Tokens
- Breaking-change background `#f0e0d8`.
- Breaking-change foreground `#8b4513`.

# Part 39 — Quality Thresholds

## 321. Deck Rhythm Thresholds
- Maximum consecutive content slides: `5`.
- Chapter dividers required from deck size `12`.

## 322. Page Density Thresholds
- Warn when trailing whitespace exceeds `25%` of a page.
- A page is sparse at `50%` empty.
- Last page allowance: `60%`.

## 323. Resume Balance Thresholds
- Minimum page fill `83%`.
- Maximum page fill `95%`.
- Maximum fill gap between pages `12%`.

## 324. Orphan Thresholds
- A last line of at most `2` words or `15` characters is an orphan in documents.
- On social cards, a last line of `1` word or at most `3` characters is an orphan.

## 325. Social Card Fit Thresholds
- Keep at least `40px` between text and the footer.
- Keep at least `24px` between text and a photo.
- Card text must never outgrow the card or run onto the photo.

# Part 40 — Social Palettes

## 326. Paper Rules
- Social-card papers are allowed only in social cards; documents keep the single-accent print palette.
- Each paper has one background, one text color, one accent, one muted color and one footer rule (text mixed `16%` into the background).
- Contrast on background: text `>= 8.8:1`, accent `>= 6:1`, muted `>= 4.3:1`, with every muted use at `28px` or larger.
- One paper per card set.

## 327. Parchment Paper
- Background `#f5f4ed`, text `#141413`, accent `#1B365D`, muted `#6b6a64`, line `#d1d0ca`.

## 328. Ink Paper
- Background `#1B365D`, text `#f3f1e8`, accent `#b9c6d8`, muted `#8e9db3`, line `#3e5473`.

## 329. Olive Paper
- Background `#2b3326`, text `#ece8da`, accent `#bdb38c`, muted `#9a9883`, line `#4a5043`.

## 330. Espresso Paper
- Background `#3a2a20`, text `#f2e9dc`, accent `#d9b48a`, muted `#a8957f`, line `#57493e`.

## 331. Pine Paper
- Background `#1c3a29`, text `#eef0e6`, accent `#b5cfa4`, muted `#8fa593`, line `#3e5747`.

## 332. Teal Paper
- Background `#134857`, text `#eef2ef`, accent `#a8d0cf`, muted `#8fb0b4`, line `#36636f`.

## 333. Crimson Paper
- Background `#5a1f17`, text `#f4ebe2`, accent `#e6bca6`, muted `#bd968a`, line `#734037`.

## 334. Char Paper
- Background `#1e1d1b`, text `#f2f0ea`, accent `#d4c4a0`, muted `#a8a49a`, line `#403f3c`.

# Part 41 — Quick Reference

## 335. Quick Decisions
- Headline: serif `500`, line-height `1.10-1.30`.
- Reading body: serif `400`, `9.5-10pt`, `1.55`.
- Emphasize a number: brand color, no bold.
- Raise a passage: ivory fill and `3pt` radius, no accent edge.
- Quote: indented olive text with reading space, no fill or side rule.
- Code: ivory fill, `4pt` / `2pt` radius, no border.
- Key figures: transparent baseline row, not a card.
- Buttons (screen only): primary filled and ghost pair.
- Section start: serif scale and margin only.
- Cover: display heading, right-aligned author and date, heavy whitespace.

## 336. Length Contracts at a Glance
- Resume: exactly `2` pages.
- One-pager: `1` page, `200-350` English words / `400-600` Chinese characters.
- Letter: `1` page, `3-5` paragraphs.
- Portfolio: `3-6` visual pages, `1-2` per project.
- Long document: `6-15` pages.
- Slides: `20-40` words each; ~`10` slides per 15 minutes.
- Social cards: `1242x1660` each, one point per card.

## 337. Common Limits at a Glance
- Paragraph `≤ 5` lines.
- List `≤ 5` items on slides.
- Emphasis `≤ 2` per line; one per `80-150` words of prose.
- Brand accent `≤ 5%` of surface; `≤ 3` accents per page.
- FAQ `6-8` questions; gallery `3-6` panels; principles `4-6`; pricing benefits `4-6`.
- Description metadata `≤ 150` characters; keywords `3-5`.

# Part 42 — Diagram Philosophy

## 338. Diagrams Must Out-Teach Prose
- Before drawing, ask: would a well-written paragraph teach the reader less than this diagram? If the answer is no, do not draw.
- Diagrams add signal through hierarchy, direction, and magnitude; they never decorate prose.
- A diagram earns its space only when the structure itself is the point; if a table or a sentence conveys the same relationship, use that instead.
- When in doubt, write the sentence rather than drawing the box.

## 339. One System, One Skin
- Every diagram wears the same skin: warm parchment ground, a single ink-blue accent, and warm grays with a yellow-brown undertone.
- There is no second design system for diagrams; diagrams introduce `0` new colors and `0` new fonts beyond the document's own stacks.
- Consecutive diagrams in one document must look like one system: same tokens, same type tiers, same line language.

## 340. Editorial Schematic, Not UI
- The register is editorial schematic: thin strokes, open chevrons, restrained fills, generous whitespace.
- Avoid anything that reads as app chrome or a dashboard: glows, gradients, shadows, heavy radii, filled triangle arrowheads.
- Diagrams are self-contained figures with no interactive behavior; they must read fully when printed.

## 341. A Diagram Radiates Certainty
- Readers assume everything drawn exists and is decided; draw only what is true or clearly encode what is not.
- Never let a diagram promise what a roadmap has not decided; uncertain boundaries get an explicit `TO VERIFY` label instead of a drawn-through line.
- Structure carries the viewpoint; the diagram never needs a caption explaining whose perspective it represents.

## 342. The Caption States the Insight
- The figure caption states the takeaway, not a description of what is plotted or drawn.
- The focal element in the drawing must match the word the caption emphasizes; caption and focal color make the same claim.
- Keep captions to one line of takeaway where possible; standalone diagram captions run serif, olive `#504e49`, about `0.95rem`, max width `52ch` (boards `62ch`).

# Part 43 — Choosing a Diagram

## 343. Selection by What You Are Showing
- System components and their connections: Architecture.
- Full-system panorama with layers, control plane, roadmap, owners: Architecture Board.
- Decision branches ("if A then B else C"): Flowchart.
- Two-axis positioning or prioritization: Quadrant.
- Category comparison (revenue, market share, quarterly): Bar chart.
- Trend over time (price, growth rate, time series): Line chart.
- Proportional breakdown (spend, segments, share): Donut chart.
- Ranking, or a share split into `7+` parts: Horizontal bar.
- Finite states with directed transitions (lifecycle): State machine.
- Time axis with milestone events (roadmap, project progress): Timeline.
- Cross-responsibility process (multi-role, request path): Swimlane.
- Hierarchical relationships (org chart, module dependencies, directory tree): Tree.
- Vertically stacked system layers (network stack, application stack): Layer stack.
- Set intersections (feature overlap, audience comparison, capability map): Venn.
- Message order between participants over time: Sequence.
- Types with fields, methods, and associations: Class diagram.
- Data schema with entity cardinality: Entity-relationship diagram.
- Open-high-low-close price action: Candlestick.
- Revenue bridge, valuation decomposition, cash-flow breakdown: Waterfall.

## 344. What Is Not a Diagram
- Comparing two things is a table: a three-column table beats any diagram of a binary contrast.
- One box with a label is a sentence: delete the box, write the sentence.
- A relationship a sentence can state is a sentence.

## 345. Scale Before Type
- Decide the scale first: a single embeddable figure, a report-scale board, or a long-lived maintained asset.
- A single architecture figure follows the `9`-node budget; a full-system panorama is a board with its own budget. Never inflate one figure to carry a board's content.
- A maintained asset follows the figure or board rules plus a lifecycle contract (source, exported image, redraw brief).

## 346. Reading Path Before Canvas
- Decide how the reader's eye moves first; aspect ratio and canvas follow.
- Left to right fits mechanisms, request paths, and task flows: input, decision or merge, output.
- Top to bottom fits platform overviews and runtime architecture: access layer, runtime layer, governance layer.
- Current to target fits evolution and refactors: today, intervention point, target.
- Hub with edges fits plugin systems and context boundaries: center object, input boundary, output boundary.
- If the reader has no entry point, no amount of color or radius tuning helps; fix the path, then the pixels.

## 347. Common Pairings by Document Type
- Technical white paper: one architecture diagram per chapter maximum, plus a timeline; wanting two means the chapter covers two topics and should split.
- Portfolio project page: a quadrant (competitive positioning) or architecture (the layer you owned); not every project needs a diagram.
- One-pager: one diagram only, a quadrant (priority) or flowchart (decision path); if tempted to add a second, cut the weaker one.
- Resume: no diagrams; at most a link to a portfolio diagram when showing system-level capability.
- Slides: one diagram per slide maximum; the diagram is the body and text is caption, not a sidebar.

# Part 44 — Complexity and Focal Budget

## 348. Editorial Density Target
- Target density is `4/10` for editorial documents (reports, one-pagers, decks): technically complete, never so dense the reader needs a guide.
- More than `9` nodes means it is two diagrams, not one.
- Two nodes that always travel together are one node.
- A line whose meaning is obvious from layout should be removed.

## 349. Teaching Density Tier
- A figure inside a technical teaching article carries `6–7/10` density: layers, data-flow direction, and at least one labeled trade-off or decision point.
- A three-box overview shipped as an "architecture diagram" in a teaching context reads as marketing.
- If hand-built vector drawing cannot hold teaching detail at the target display width, switch to a raster illustration rather than enlarging the figure.

## 350. The Focal Rule
- Each diagram has `1–2` focal elements, marked with ink-blue stroke `#1B365D` and brand-tint fill `#EEF2F7`.
- Everything else stays in warm neutrals; focal signal comes from contrast, not count.
- Five ink-blue nodes means you have not decided what is focal.
- The total ink-blue area of a figure stays within a `5%` cap, icons included.
- Focal is not a signaling system: never paint every "important" node blue.

## 351. Focal Matches the Argument
- Put the accent on whatever element the caption's emphasized word names; two competing focals (caption says "core," a different node is blue) is a defect.
- When adapting an external diagram that used one color per node type, migrate the single focal to the element the caption emphasizes and neutralize everything else.

## 352. Maturity Encoding
- Encode maturity with stroke and opacity, never with new colors.
- Shipped: standard node (ivory `#faf9f5` fill, near-black `#141413` stroke) — exists today.
- In build: focal (brand `#1B365D` stroke, brand-tint `#EEF2F7` fill) — the current work and the diagram's point.
- Future: dashed stone `#6b6a64` stroke with node content at `55%` opacity — direction, not commitment.
- The focal budget and "under construction" share the same `1–2` slots.
- Future nodes never take focal color and never sit on the main path as if load-bearing.

## 353. No Plan Furniture in Architecture
- No dates, owners, phases, milestones, or 30/60/90 plans in an architecture diagram unless a board with a governance layer was explicitly requested.
- Architecture shows objects, relations, boundaries, and intervention points only; schedule belongs to a timeline or a board's governance layer.

# Part 45 — Diagram Visual Language

## 354. Canvas and Texture
- Canvas fill is parchment `#f5f4ed`, never pure white.
- Overlay a dotted texture: a `22×22` repeating tile with one dot of radius `0.9` at `(1,1)` in `#E3E2DC`, the whole overlay at opacity `0.55`.
- `#E3E2DC` is the parchment-blended solid equivalent of near-black at `8%`.
- Use the same texture on every textured diagram so the ground stays uniform; quadrant and flowchart figures may use plain parchment.

## 355. Solid Hex Only
- All fills and strokes are solid hex values pre-blended on parchment; never use alpha colors in diagram fills or strokes.
- Translucent colors disagree with the warm palette and print unpredictably.
- The only deliberate opacity uses are the dot texture overlay (`0.55`), the focal swimlane tint (`0.40`), and future-state content (`55%`).

## 356. Node Role Palette
- Standard node: fill ivory `#faf9f5`, stroke near-black `#141413`.
- Store node: fill `#EAE9E2` (near-black 5% solid), stroke olive `#504e49`.
- Cloud node: fill `#EEEDE6` (near-black 3% solid), stroke `#B2B1AC` (near-black 30% solid).
- External node: fill `#E9E8E1` (olive 8% solid), stroke stone `#6b6a64`.
- Focal node: fill brand-tint `#EEF2F7`, stroke brand `#1B365D`.
- Node stroke width is `1`.

## 357. Text Colors
- Primary text: near-black `#141413`.
- Secondary text: olive `#504e49`.
- Tertiary text and small mono labels: stone `#6b6a64`.
- Focal node tags and sublabels may switch to brand `#1B365D`.

## 358. One Accent, No Status Colors
- Never add a fourth state color such as warning amber or success green; there is exactly one accent.
- Up/down, increase/decrease, and positive/negative use ink-blue versus stone, not red versus green.

## 359. The Four-Unit Grid
- All coordinates, widths, heights, and gaps are divisible by `4`; breaking this once makes a diagram look "close enough."
- Board connector standoffs and export margins also stay divisible by `4`.

## 360. Node Width and Height Tiers
- Node widths come from three tiers only: `128`, `144`, `160`. Do not add more.
- Small diagrams (canvas width under `360`) may compress to `2` width tiers, but never tailor each node.
- Node heights: `32` (pill) and `64` (standard); compact nodes in trees, swimlanes, and board paths use `48`.
- Corner radius on nodes is `6`; bands `4–6`; maximum radius anywhere is `6–10` — above `10` reads as app-store chrome.
- Pills (start/end) use radius `16` on a `32`-high shape.

## 361. Node Anatomy
- A node holds three things: an optional icon, a title, then two or three short lines.
- Standard embedded-figure layout: uppercase mono tag at size `7`, letter-spacing `0.15em`, baseline `y+18`, left inset `22`; name at size `12`, weight `500`, centered, baseline `y+38`; sublabel at size `9`, centered, baseline `y+54`.
- No paragraphs and no noun trains inside a node; prose goes to a bottom note or a companion document.
- Mask each node with a parchment rectangle of identical geometry underneath, so lines and rings drawn behind never show through.

## 362. Diagram Type Tiers
- Standalone figure font sizes: `7` (small mono label), `9` (mono sublabel), `12` (name).
- Names use the serif (or the CJK-first serif stack); mono is only for technical content such as ports, URLs, fields, and tags.
- Arrow labels use mono size `8`; legend labels use serif size `8.5`; legend heading mono size `8`.
- Fixed pixel sizes only: no viewport-scaled type and no negative letter-spacing on body sizes.
- The caption tier is the smallest type on the page; never add a tier below it.

## 363. Lines and Connectors
- Standard connector: olive `#504e49`, stroke `1.2`.
- Focal / primary-path connector: brand `#1B365D`, stroke `1.4`.
- Draw connectors behind nodes.
- Prefer orthogonal routing (straight runs and right-angle elbows); no decorative curves except loop and back arcs.
- Never route a line through a module, across text, or through another label.
- Multiple branches from one node need separate attachment points; keep their order stable and leave room at corners.

## 364. Chevron Arrowheads
- Use open two-stroke chevrons, not filled triangles: a filled triangle reads as technical UI; an open chevron reads as editorial schematic.
- Chevron geometry: about `6` units deep and `10` units tall (e.g. points `(2,1) (8,5) (2,9)`), stroke `1.5`, round line caps, no fill.
- Draw each chevron with a hard-coded direction rather than relying on auto-oriented markers, which some print renderers draw always pointing right.
- Arrowhead color matches its shaft (olive or brand).

## 365. Endpoints Land on Edges
- In figures, arrow endpoints land exactly on node edges: start at `(x + w, y + h/2)`, end at `(x, y + h/2)`.
- A `5–10px` gap between arrow tip and node edge reads as an arrow floating in space; even `10px` is visible.
- Endpoints must attach outward from the node edge, within `8` units of it; segments must not cross any other node rectangle.

## 366. Dashed Line Vocabulary
- Dashed lines mean "exceptional," "auxiliary," or "not yet": reset/timeout arcs (`4,3`), timeline leaders (`3,3`), lifelines (`6 4`), return messages (`6 4`), future-state borders.
- Never use dashes decoratively on a primary path.

## 367. The Legend Strip
- The legend sits in a strip below the drawing, never floating inside the diagram area where it collides with nodes.
- Separate it with a hairline rule in `#DEDED7`, stroke `0.8`, spanning the content width.
- Heading reads `LEGEND` in mono, size `8`, letter-spacing `0.22em`, olive.
- Swatches are `14×10` rectangles with radius `2` (circles of radius `5–6` for point- or milestone-based diagrams), followed by a serif label at size `8.5` in olive.
- Show only the encodings actually used in the figure.

## 368. Standalone Figure Frame
- A standalone figure page has an eyebrow (mono, `0.7rem`, letter-spacing `0.22em`, uppercase, stone), a serif title (`1.9rem`, weight `500`, letter-spacing `-0.3pt`, line-height `1.15`), the drawing, then the caption.
- Standard figure canvases: `960×460` for most diagrams, `860×520` for flowcharts, `820×540` for quadrants, `1200×1016` for boards.
- Frame max width `1000px` (charts `920px`, boards `1240px`); drawings keep a minimum render width around `860px` (`820` flowchart, `780` quadrant, `640` charts, `1080` boards).
- The page is sized to the drawing's own frame so the whole figure exports on one uncropped sheet.

# Part 46 — Structural Diagrams

## 369. Architecture
- Shows system components and connections at single-figure scale: at most `9` nodes and one focal.
- Lay out left to right along the request path; branch to stores on a fan of short diagonals or elbows.
- Mix node roles (external, cloud, standard, store, focal) so role is legible from fill and stroke alone.
- Exactly one focal node: the component the reader should look at first.
- Label every relationship with a short mono verb or protocol (e.g. `HTTPS`, `SSR`, `READ`, `QUERY`) on a masking rectangle.
- The focal path carries the brand connector (`1.4`) and brand label; all other edges stay olive (`1.2`).
- Legend shows each node role used plus "standard flow" and "primary path."

## 370. Layer Stack
- Horizontal bands stacked vertically; each band is a system layer.
- Standalone layout: bands `56` high, `8` gap, width `724`, radius `4`.
- Layer tone darkens and recedes toward the foundation: top layer ivory with near-black stroke; middle neutral layers parchment or `#f0efe8`; foundation `#eae9e1` with `#b8b7b0` stroke and the faintest number.
- Each band carries a two-digit mono index (`01`–`05`) at size `7`, a name at `12` weight `500`, and a mono description at `9`.
- One focal layer in ink-blue, marking where domain-specific logic lives; its tag reads e.g. `02 · FOCAL`.
- Flow direction goes on the sides, not inside the bands: a request arrow down the left (olive) and a response arrow up the right (brand), each with a masked mono label.
- Embedded five-layer layout: canvas `1000×560`, layer height `88`, gap `8`; tag baseline `y+24` at mono `14` letter-spacing `2.5`; name baseline `y+54` at serif `24` weight `600`; description baseline `y+76` at mono `14`; right-side role tag at `x=900`, end-anchored, size `13`.

## 371. Tree
- Hierarchy with orthogonal elbow connectors only: a vertical drop from the parent to a junction bar, a horizontal bar spanning the children, then vertical drops to each child.
- Each child drop ends in a downward chevron at the child's top edge.
- Root uses the standard node; secondary branches use the external style; one focal sub-tree uses brand tint.
- Nodes are `48` high; parents `144` wide, leaves `128` wide.
- Within the focal sub-tree, the whole branch path turns brand (`1.4`), and leaves use brand-tint fill with a lighter `0.8` brand stroke and brand sublabels.
- The focal sub-tree marks where complexity lives or the path the reader must understand first.

## 372. Architecture Board Main Axis
- On a board, the single brand-colored line on the page is the main axis (e.g. input to pixels).
- Main-axis nodes are standard `144×48` nodes with name at `12` weight `600` and a `8.5` stone sublabel.
- Non-core relations along the axis are demoted to a single uppercase mono caption line (e.g. `AUX · ...`) rather than drawn as another line.

# Part 47 — Process Diagrams

## 373. Flowchart
- Decision logic with branches: one focal decision and two to four outcomes.
- Use only when the structure is the point; if a table communicates the same thing, use a table.
- Start and end are pills (`32` high, radius `16`) in the external style; steps are standard `160×64` nodes with a mono `STEP 01` tag.
- The decision is a stretched hexagonal diamond carrying the focal fill and brand stroke `1.2`, with the question at `11` weight `500` and a mono `BRANCH` tag in brand.
- Flow runs top to bottom; branches leave the decision horizontally and drop vertically into outcomes via right-angle elbows.
- Branch labels (`YES`, `NO`) sit on masking rectangles in mono size `8`, letter-spacing `0.12em`.
- Branches diverge into equal weights so the reader sees the question, not an implied answer; one branch may carry the brand path, the deferred branch uses the cloud style.

## 374. Swimlane
- Process flow across responsibility lanes, e.g. client, server, database.
- Lanes are full-width bands `120` high; neutral lanes fill `#F0F0E9`, the focal lane fills brand-tint `#EEF2F7` at `0.40` opacity.
- Lane dividers: outer edges solid `#e8e6dc` at `1`; inner dividers dashed `4,3` at `0.8`, with the divider bounding the focal lane drawn in brand.
- A `64`-wide label column on the left holds rotated uppercase mono lane names at size `8`, letter-spacing `0.15em`; the focal lane's label is brand, others stone.
- Nodes are `144×48`; connectors use orthogonal elbows only, drawn behind nodes, with a manual chevron at each landing.
- The focal lane is the one carrying the business logic that decides the outcome.

## 375. State Machine
- Finite states with directed transitions; one focal state, the one where the user spends most time.
- Follow UML convention: start is a solid near-black dot of radius `6`; end is a double circle (outer radius `8` stroke `1.4`, inner solid radius `4`).
- States are `144×64` nodes (terminal state `128` wide) with a mono `STATE` / `TERMINAL` / `FOCAL` tag.
- Forward transitions run left to right with masked mono labels (`TRIGGER`, `SUBMIT`, `COMPLETE`); the transition into the focal state is brand.
- Exceptional paths (reset, timeout) are dashed `4,3` arcs that loop above the main row, with their own masked label and a chevron at the landing.

## 376. Timeline
- A horizontal time axis with alternating above/below event labels, so labels never collide.
- Axis: light-stone `#b8b7b0`, stroke `1.4`, with an open chevron at the right end.
- Events evenly spaced (e.g. `152` apart); markers are circles of radius `5` with a `1.5` parchment ring; later events darken from stone to olive.
- Leaders from marker to label are dashed `3,3` stone at `1`; label cards are `40` high, radius `4`, parchment fill, `#e8e6dc` stroke `0.8`, with a mono date at `8` and a name at `11` weight `500`.
- The single focal milestone gets a radius `6` brand marker, a solid brand leader `1.2`, a taller card (`48` high) with brand-tint fill and brand stroke, and a `13` name.
- The focal milestone is the moment the reader should remember.

## 377. Cycle and Loop Diagrams
- For a four-cardinal-node ring, each arc is a quadratic curve whose control point sits at the outer intersection of the two adjacent tangent axes, not at a node corner.
- Example (top node to right node): start at the top node's right-edge midpoint, end at the right node's top-edge midpoint, control point at (right node center x, top node center y). This gives a pure horizontal departure and pure vertical arrival — a clean quarter circle.
- A control point at the node corner produces a squashed arc.
- Closed loops need a dashed framing ring centered on the visual center, radius slightly larger than the center-to-inner-edge distance, drawn beneath the nodes so solid node fills mask it.
- Never draw both a dashed ring and four directed arcs for the same loop; the reader sees two flows.
- Never leave every node as a single word with an empty center: either add a subtitle to each node or place one line of text at the center (exit condition, size metric). Pick one.

# Part 48 — Interaction and Model Diagrams

## 378. Sequence Diagram
- Participants sit in a top row as `80×40` boxes, radius `4`, ivory fill, border `#e8e6dc` at `1`, names at `13` weight `500` near-black.
- Lifelines drop from each participant: olive `#504e49`, stroke `0.75`, dashed `6 4`.
- Messages read top to bottom, evenly spaced (about `40` apart), as olive lines at stroke `1`.
- Calls are solid; returns are dashed `6 4` — dashing alone distinguishes responses from calls.
- Arrowheads are the accent color `#1B365D`; message labels sit centered `10` above the line at `11` in stone `#6b6a64`.
- Keep labels to short verb phrases (e.g. "Submit request," "Query records," "Return results," "Response data").

## 379. Class Diagram
- Boxes are types; compartments list fields and methods.
- Box: square corners (radius `0`), ivory fill, border `#e8e6dc` at `1`; header band `32` high filled `#eae9e2` with the type name centered at `13` weight `700`.
- Compartment dividers are hairlines `#e8e6dc` at `0.75`; member rows step `20` apart at size `11`.
- Member syntax is two-toned: punctuation and visibility marks (`+ `, `: `) in faint `#bdbcb6`, names and types in stone `#6b6a64`.
- Relationship lines are olive at `1`; markers in accent: inheritance a hollow triangle (parchment fill, brand stroke `1.5`), composition a filled brand diamond, aggregation a hollow diamond, association an open chevron.
- Relationship labels and cardinalities (`1`, `*`) sit beside the line at `11` in stone.

## 380. Entity-Relationship Diagram
- Use crow's-foot notation: each connector's ends mark cardinality between entities.
- Entity box: square corners, ivory fill, `#e8e6dc` border; header band `34` high in `#eae9e2` with the uppercase entity name at `13` weight `700`.
- An entity with no attributes shows an italic placeholder at `11` in faint `#bdbcb6`.
- Relationship lines are olive at `1`, routed orthogonally; cardinality glyphs (double bars for "one," three-prong foot for "many," a hollow circle of radius `4` for "zero") drawn in olive at `1.25`.
- Relationship verbs sit on a parchment label pill (radius `2`, `#dad9d3` stroke `0.5`, height about `20`) at `11` in stone.

## 381. Shared Model-Diagram Palette
- Model diagrams map seven roles: background parchment `#f5f4ed`, foreground near-black `#141413`, lines olive `#504e49`, accent brand `#1B365D` (arrowheads and focal emphasis, the only chromatic color), muted stone `#6b6a64` (secondary text, edge labels), surface ivory `#faf9f5` (node fill), border `#e8e6dc` (node and group stroke).
- Edge connectors are warm olive, never pure black.
- Labels render in one CJK-first serif face so mixed-script labels never split across fonts.
- Model diagrams size to their intrinsic dimensions and are never upscaled past natural size; cap display height near `780px` so tall ones stay on one page.

# Part 49 — Positioning and Set Diagrams

## 382. Quadrant
- Two-axis positioning with `4` quadrants, `6–10` plotted points, and `1–2` focal points.
- Classic axes: impact × effort, reach × confidence, urgency × importance.
- Plot area framed by a hairline `#DEDED7` at `0.8`; the midpoint cross axes in `#CCCCC6` at `0.8`.
- Tint only the preferred quadrant with a warm `#F3EEE6`; leave the other three untinted.
- Outer axis arrows run olive at `1.2` with axis titles at `11` weight `500`, letter-spacing `0.08em`; the vertical title is rotated `-90°`.
- Each quadrant gets a two-line label: an uppercase mono position code at `8.5`, letter-spacing `0.22em`, and a verdict word at `10` (e.g. "do first," "incubate," "delegate," "drop"); the preferred quadrant's label is brand.
- Point hierarchy by size and fill: focal solid brand radius `6.5` with an `11` brand label; near-focal brand-tint radius `5`; standard ivory radius `5`; secondary store-gray radius `4.5`; drop cloud-gray radius `4` with stone labels.
- Point labels sit `10` to the right of the point at `10`.

## 383. Venn
- Two or three overlapping circles showing set relationships.
- Circles of radius `152` with centers `208` apart give a readable lens.
- Focal circle: brand-tint fill, brand stroke `1.2`; secondary circle: `#EAE9E3` fill, olive stroke `1.2`.
- Zone labels centered in each region: set-only names at `12` weight `500`, with `9` olive sublabels.
- The intersection label is the focal callout: brand, size `13`, weight `500`, in a serif italic style, because the overlap is usually the point.
- Circle titles sit above each circle as uppercase labels at `10` weight `500`, letter-spacing `0.1em`, in the circle's stroke color.
- Example member rows sit low in each region at `9` stone, separated by middle dots.

# Part 50 — Architecture Boards

## 384. A Board Is a Reading Instrument
- A board is a standalone report-scale page, not an inflated figure.
- The reader must get three things, in order: what the parts are, how they flow or depend, and where the next piece of work should intervene.
- Any element that helps none of those judgments is deleted; the denser the system, the more restrained the board.

## 385. Canvas Follows Content
- One-screen product or system relationship: `16:9`, slide-sized.
- Whole-platform panorama: wide canvas with light vertical scroll.
- Roadmap plus owners plus governance loop: report page, the board as the spine of an A4 flow.
- The canvas may grow taller but never into an endless page; one scan must build the whole picture.

## 386. Five Fixed Information Layers
- Title: one sentence stating the subject and the judgment.
- Business: roles, capability domains, external consumers.
- System: platform modules and the control plane.
- Runtime: key paths — data flow, event flow, permission flow.
- Governance: monitoring, audit, lifecycle, roadmap, owners.
- Each layer answers exactly one question; no protocol detail in the business layer, no domain catalog in governance.

## 387. Bands Over Cards
- Parallel peers share one band with thin vertical dividers, not N separate cards.
- Bands: full-width ivory shells, radius `6`, `#e8e6dc` stroke `1`, `100` high, with dividers inset `16` from top and bottom.
- Tabular facts get a table shell: uppercase column heads at `10` weight `600` letter-spacing `0.18em`, a near-black `1` rule under the heads, light dividers, and a closing `#DEDED7` hairline.
- Never nest a card inside a card.
- Budget `10–25` major blocks per board; past that, merge blocks into domains instead of stacking nodes.
- The `1–2` focal rule still holds: one focal cell inside a band carries the only accent fill.

## 388. Board Section Anatomy
- Each section opens with a numbered uppercase mono header (e.g. `01 · PLATFORM SURFACE`) at `10`, letter-spacing `0.22em`, stone, left-aligned.
- A right-aligned uppercase scope note sits on the same baseline at `10`, letter-spacing `0.18em`.
- Sections step about `160` apart; band content inset `24` from the band edge.
- Cell content: title at `14` weight `600`, then two short lines at `10`, the first olive, the second stone, baselines `24` and `20` apart.

## 389. Board Title Layer
- Title sentence at `28` weight `600` states subject and judgment.
- A one-line olive subtitle at `13` sits below.
- A brand hairline rule at `0.8` closes the title layer across the full content width.
- Corner text holds only the date basis, version, or data scope (e.g. `WORKSPACE VIEW · 2026-07`), uppercase mono at `10`, right-aligned.

## 390. Board Type Scale
- Page title `36–40px`; section title `22–24px`; block title `17–19px`; body and node description `13–15px`; caption `11–12px` (standalone page sizes, larger than embedded figures).
- Fixed pixel sizes; no new fonts or colors on a board.

## 391. Board Line Discipline
- Orthogonal lines only: no curves, no passing through modules, no crossing text, no decorative junctions.
- Main path in brand; auxiliary lines in border tone; light open chevron heads.
- Connector standoff on boards is `4px`: start the shaft `4px` after the source edge and land the chevron tip `4px` before the target edge. Welded-on arrows read cramped at board scale.
- Never run a line along a module's top edge; route below or beside with `16–24px` of air and attach with a short stub to the outer edge, never into the text area.
- A relation that is not core information becomes a caption or small label, not a line; a line the reader cannot parse is deleted, not explained.

## 392. Board Copy Reads as Judgment
- Copy that is correct but decides nothing is the first failure; avoid saturated abstractions, long parallel noun phrases, and adjectives with no action.
- Prefer committing sentence shapes: "from X to Y," "inserted before X," "unifies X across Y," "owned by X," "measured by X."
- Board text is short, hard, and executable.
- A node line reads like "Foundation: event push / PublishEvent v2, EventBus, webhook subscription," never a title followed by eight comma-separated nouns.

## 393. Scan Anchors on Non-Latin Boards
- On a CJK board, uppercase mono English anchors (`MAIN AXIS`, `CONTROL PLANE`, `PUBLIC INFRA`, `OWNER MAP`, `ROADMAP`) help scanning.
- Never translate full sentences; the reader should never switch languages mid-thought.

## 394. No Viewpoint Captions
- Notes like "from the platform team's perspective" or "working draft for X" do not belong; structure carries the viewpoint.
- If deleting a caption changes nothing, delete it.

## 395. Whiteboard to Board
- Whiteboards explore; boards communicate. Never reuse whiteboard drawing style.
- Identify the core objects; merge repeated objects into domains; collapse free-form connections into one or two main paths; rewrite sticky-note phrasing into short labels; push detail into a bottom note or companion document.

## 396. Structure Before Pixels
- Outline the board first with a fixed vocabulary — Section, Band, Node, Flow, Table, Note — then render with the shared token map.
- Content fills the structure; the token map styles it.
- A closing note on the legend baseline may state what the board deliberately leaves out (e.g. "detail lives in the docs; this board carries the spine").

## 397. Module-Level Pass
- When macro structure is right but the board still reads crowded, the fault is inside modules; global fixes (bigger canvas, smaller type, recolor) do not touch it.
- Check per module: title too close to its description; CJK line breaks landing mid-phrase or orphaning one character; an icon eating the text column; padding thinner than siblings; baselines unaligned across a row; a table off-center in its section.
- Fix modules one at a time, re-render, then judge whether the canvas must change.

## 398. Board Pre-Ship Scan
- Content: the reader can state the main path within `30` seconds; each section answers exactly one question; current state, target, intervention points, governance, and roadmap are explicit; everything deletable is deleted.
- Visual: parchment ground, never pure white; one accent color; no gradient, shadow, bitmap, external fetch, or script; no overlapping text and no line over module content; uniform icon stroke and size; right-side captions right-aligned with at least `56px` outer margin.
- Every hex value must exist in the token map; no pure white `#fff` and no em dash characters in diagram copy.

# Part 51 — Maintained Diagram Assets

## 399. The Third Scale
- A maintained asset lives in a project (hero figure, documentation figure, architecture folder) and is redrawn for months by different hands.
- All figure and board rules still apply; what changes is lifecycle — the diagram becomes a source with a contract.
- Typical triggers: "draw an architecture diagram for the project," "a figure for the README," "update this architecture diagram."

## 400. The Source–Image–Brief Trio
- A self-contained vector source is the single source of truth, with no external image, script, or font fetch, carrying an accessible role, title, and description.
- An exported raster image of the same name is what readers see; it is re-exported after every content change and never edited directly.
- A redraw brief records intent that would otherwise die in a chat log; a missing or stale brief is rebuilt as part of the task.
- Deliver all three or say which is missing.

## 401. The Redraw Brief's Four Blocks
- Must preserve: what the current diagram already states correctly — never new ideas.
- Suggested additions: facts from sources not yet shown — never phrased as if already drawn.
- Visual direction: hierarchy, whitespace, line, and boundary fixes to try next — never a full palette dump.
- Sister boundaries: what belongs in companion diagrams — never content that should move back in.
- The separation prevents two failures: treating a suggestion as drawn, and a visual pass that silently grows scope.

## 402. Evidence Before Drawing
- Read, in order: the redraw brief, the current source, the current image at real size, then the facts (design docs, source definitions) that affect terminology and edges.
- Current facts override the brief; the brief overrides memory; never redraw from memory alone.
- Source existence alone does not prove a call or dependency; record evidence for relationships, not just component names.

## 403. Node Naming: Function First
- Node titles carry function first, protocol noun second; a bare protocol noun outsources reading cost to the reader.
- Weak "Registry" becomes "Plugin registry · Registry"; "Queue" becomes "Task queue · Queue"; "Policy Hook" becomes "Write-action admission · Policy Hook"; "Inbox" becomes "Task inbox · Inbox."
- In-diagram copy holds objects, boundaries, and actions only; argument stays in prose.
- CJK node copy uses short labels with commas, slashes, and semicolons — never the CJK full stop; a line needing a full stop is a sentence and belongs in the document.

## 404. Stable Semantic Geometry
- Give every node, edge, and edge-label mask a stable identity that survives text and position changes.
- Edges declare their source and target; labels belong to exactly one edge.
- Checks a well-formed diagram passes: no duplicate identities, no missing endpoints, no overlapping node rectangles or label masks, no edge through a node or another edge's label, endpoints attaching outward within `8` units of the named edge.
- Grazing a rectangle edge or crossing a real boundary frame is allowed; neither counts as passing through a node.
- Passing geometry does not prove text fit, arrowhead visibility, or factual accuracy; inspect real rendering.

## 405. Preserve Relationship Meaning
- Keep meaningful relationship labels: protocol, action, direction, synchronous versus asynchronous.
- When a label does not fit, move its mask and text together, widen the corridor, or reroute the edge; never shrink text or drop meaning to fit.
- During updates, distinguish changed relationships from moved boxes; unchanged objects keep their identities.

## 406. One Vocabulary
- The diagram and its host document share one vocabulary; a rename in prose updates the diagram text, title, description, redraw brief, and exported image in the same change.
- A diagram still showing an old name is a bug, not a style issue.

## 407. Image Export
- Documentation and README figures: `2400–3200px` wide.
- Social or chat previews: a separate lightweight copy; never overwrite the main image.
- Capture the content bounding box, not the full page, plus a fixed safe margin of `96–120px`, default `112`.
- When export clips, fix the export chain; never resize, crop, or hand-edit the image, and never change diagram content to appease the exporter.

## 408. Three-Surface Acceptance
- The source in a browser: structure, overlap, arrows, whitespace.
- The exported image at `100%`: clipping, blank bands, source-to-image drift.
- The published context: the image fills the prose column, sits at the right heading level, and is not half-width or double-margined.
- Crowding is solved by cutting content, banding peers, or splitting out a sister diagram — never by adding a smaller type tier or shrinking the export.

# Part 52 — Icons and Figures

## 409. Icon Line Style
- Icons are drawn with the same primitives as nodes (rectangles, circles, lines, paths); no icon fonts or sprites.
- Single line, stroke `1–1.5pt`, no fill.
- Stroke weight is consistent within one diagram; never mix `1pt` and `1.5pt` icons in one figure.
- No drop shadow, gradient, 3D, or glassmorphism; no emoji faces, mascots, or expressive characters.
- Focal icons may use brand stroke or fill, but the figure's total ink-blue area still respects the `5%` cap.

## 410. Canonical Icon Shapes
- Terminal / CLI: rounded rectangle with three dots top-left.
- Document / spec: rectangle with three short horizontal lines.
- Checklist / verification: rectangle with two check marks.
- Gear / system: 8-tooth gear outline.
- Magnifier / inspect: circle with a `45°` handle.
- Shield / safety: shield silhouette.
- Cloud / hosted service: three-arc cloud outline.
- Chip / hardware: square with leg lines on four sides.
- GPU / compute rack: rectangular stack with port indicators.

## 411. Icons Must Carry Information
- When in doubt, omit the icon; a clean text label beats a cute icon.
- Add an icon only when it carries information the label cannot (e.g. distinguishing hosted service from on-device compute at a glance).
- Decorative icons are a disaster.

## 412. Human and Robot Figures
- Avoid human figures and anthropomorphic AI in editorial diagrams.
- If a person must appear, use a minimal line drawing without facial detail.
- Industrial robots may appear as line-art mechanical structures, short of patent-illustration density.

# Part 53 — Embedding and Scale

## 413. Embedding a Figure
- Embed only the drawing itself into the document figure, leaving the standalone eyebrow, title, and frame behind.
- The figure caption reads "Figure N." followed by a short editorial caption in serif.

## 414. Embedded Font Calibration
- Standalone sizes `7 / 9 / 12` are too small embedded in an A4 column: a `1000`-unit drawing renders near `470pt`, a scale of about `0.47`.
- Raise sizes roughly `1.8–2.0×` when embedding so diagram text aligns with the `11pt` body.
- h2 / focal node name (`11pt` visual): size `24`.
- Body equivalent (`11pt`): `22–24`.
- h3 / sublabel (`9–10pt`): `18–20`.
- Caption equivalent (`8pt`): `15–16`.
- Uppercase mono tag (`7pt`, letter-spacing `2.5`): `14`.
- Size `24` at weight `600` in the body serif renders about `1.05×` body, reading as h2-equivalent without dominating.

## 415. In-Figure Header Line
- For embedded diagrams, put a "FIGURE N · TITLE" header inside the drawing instead of a separate caption; the brand header doubles as a section anchor.
- `FIGURE  1` in brand mono at `13` weight `600`, letter-spacing `3`; the title in olive mono at `13`, letter-spacing `3`; baseline at `y=38`.
- A brand rule at stroke `0.8`, `14` units below the baseline, spans the content width (e.g. `80` to `920`).
- Use two spaces between `FIGURE` and the number; with letter-spacing `3`, one space lets the digit collide with the letter.

## 416. Top Padding for Text
- A text element's y is its baseline; keep y at least `font-size × 1.2` from the top edge, or capitals clip (e.g. "TOOLS" renders as "TOULS").
- Pad the top of the canvas or move the baseline into the safe zone.

## 417. Diagrams on Slides
- At slide scale (`1920×1080`), the diagram fills at least `65%` of the slide area; a print-sized diagram on a slide leaves about `35%` dead space.
- When the diagram cannot grow (already at its semantic maximum, e.g. flows or quadrants), insert a `70–100` character olive paragraph at `28px`, line-height `1.55`, between figure and caption.
- The paragraph carries the editorial reading; the caption stays one line as the takeaway; vertical fill stays above `60%`.

# Part 54 — Chart Design

## 418. Geometry Comes From Data
- Never place bars, points, or arcs by hand; every mark is computed from the numbers, so no silent wrong values creep in.
- To change a number, change the data and regenerate; never edit a mark or label after generation.
- Refuse data that cannot be drawn honestly — a candle whose high/low do not contain open/close, a waterfall total that disagrees with its running sum, more items than the limit. Fix the data; never loosen the rules.

## 419. Choosing the Chart Yourself
- When content carries numbers, pick the chart and embed it without asking.
- A share summing to about `100%` is a donut only up to `6` items; `7+` becomes a horizontal bar.
- A single time series where absolute count changes dominate (not the rate) renders as bars, not a line.
- When several types fit, prefer the one that shows variance most clearly.

## 420. Chart Series Palette
- Series order: ink-blue `#1B365D`, olive `#504e49`, stone `#6b6a64`, light-stone `#b8b7b0`, mist `#d4d3cd`, brand-tint `#EEF2F7`.
- The first series is always the focal ink-blue and carries the primary argument.
- Any swatch, bar, or segment in brand-tint gets a `#e8e7e1` outline at `0.8` so it stays visible on parchment.
- Value labels are near-black `#141413`; tick labels and notes stone `#6b6a64`; legend labels olive.

## 421. Direction Colors
- Up candles and increases are ink-blue `#1B365D`; down candles and decreases are stone `#6b6a64`.
- Waterfall totals are charcoal `#4d4c48`.
- Never red/green.

## 422. Shared Chart Geometry
- Every chart shares one plot height and one type scale so charts in one document line up.
- Plot area runs from `y=24` to `y=224` (plot height `200`); category labels sit `22` below the baseline; the legend hairline sits `44` below the baseline.
- Chart height is baseline `+22+16` without a legend, or `+44+32` with one; a source line adds `22`.
- Base canvas width `680` (waterfall `720`, candlestick `760`), designed for a ~`170mm` column at about `0.7` scale so `12`-unit labels print near `8.5pt`, just under body text.
- Charts render near `75mm` tall at `170mm` wide.

## 423. Chart Type Scale
- Tick labels `11`; category labels `12`; value labels `12`; legend `12`; notes and source `11`.
- First-series value labels take weight `500`; others regular.
- Donut center figure `30` weight `500` in brand; donut legend percentages `14`.

## 424. Compact Size
- For a chart shown small (a half-column slide, two charts side by side), narrow the canvas to `65%` width instead of scaling the drawing down; drawn at the same physical width its labels come out about `1.5×` larger.
- Never cap a chart's height or shrink it to fit; a height cap shrinks every label with it.
- Place charts at the full width of their column.

## 425. Axes and Scales
- Axes round outward to a `4–8` tick scale with a `1 / 2 / 2.5 / 5` step (raw step = range ÷ `6`).
- Bars and areas always start at zero; only lines may opt out of zero so the axis starts near the data.
- Tick labels carry the precision of the step, not of the data (`0–20` by `5`, not `0.0–20.0`).
- Grid lines `#e8e7e1` at `0.8`; the zero/base line near-black `#141413` at `0.8`.
- Tick labels end-anchor `8` left of the plot, nudged `4` below the gridline.

## 426. Left-Edge Alignment
- Tick labels start at the chart's own left edge, so the chart aligns with the text column it sits in.
- The plot's left edge is the widest tick label plus `10` (plus `22` when a rotated unit caption is present).
- The right plot edge sits `4` in from the canvas edge (lines reserve room for end labels).

## 427. Unit Caption
- The unit caption is rotated `-90°` at the vertical middle of the plot, `8` from the left edge, at `11` in stone.
- On horizontal bars the unit sits above the first row at `11` stone, left-aligned to the bars.

## 428. Chart Legend
- A legend appears only with more than one series (or always for direction-coded charts: candlestick, waterfall).
- Legend sits below the plot under a `#e8e7e1` hairline at `0.8`.
- Swatches are `12×12` squares, radius `2`; label starts `18` after the swatch at `12` olive; entries step label width plus `32`.
- Line legends use a `24`-long line sample in the series stroke and dash, with the series marker at its center, label `32` after the start.

## 429. Source Line
- A source footnote sits on the last row, `6` above the bottom edge, at `11` in stone, left-aligned to the canvas edge.
- The chart never draws its own title; the document's figure caption carries the takeaway. A title exists only as an accessible name.

## 430. Number Formatting
- Decimals inferred from the data, capped at `2` (explicit range `0–4`).
- Thousands separators always; minus sign before the prefix (e.g. `-$1,200`).
- Waterfall deltas carry an explicit sign (`+30`, `-40`).
- Prefix and suffix (e.g. `$`, `%`) apply to value labels; the unit (e.g. "USD m") is the axis caption.

## 431. Chart Data Limits
- Bar: `8` categories, `3` series.
- Line: `12` points, `3` lines.
- Horizontal bar: `12` rows.
- Donut: `6` segments.
- Candlestick: `30` points.
- Waterfall: `8` bars.

## 432. Chart Language and Fonts
- Chart text uses the serif chain matching the label language (Latin serif, CJK serif, or Korean serif), detected from the labels.
- Width estimates count full-width glyphs at `1em` and Latin glyphs at about `0.56em`.
- Direction legends localize: "Up (close above open)" / "Down (close below open)," "Increase" / "Decrease" / "Total."

# Part 55 — Chart Types

## 433. Bar Chart
- For category comparison; up to `8` categories × `3` series.
- A single series gets bars about half the slot width, capped at `56`.
- Grouped bars stay narrow — `min(32, (slot × 0.7 − 8 × (series − 1)) ÷ series)` — with `8` between bars in a group, so the gap between groups still reads as the category break.
- Bar radius `2`; value labels `4` above positive bars or `12` below negative ones, centered.
- Negative values hang below the near-black zero line.

## 434. Line Chart
- For trends over ordered data; up to `12` points × `3` lines.
- Series styles: first line solid stroke `2`; second dashed `5 3` at `1.5`; third dotted `2 3` at `1.5`; round joins and caps.
- First series markers are filled circles of radius `4` with a `1.5` parchment ring, the last point enlarged to `5.5`; other series use hollow parchment circles of radius `3.5` with a `1.5` colored stroke.
- Interior vertical guides at each category: `#e8e7e1`, `0.5`, dashed `3 4`.
- End labels sit `8` right of the last point in the series color; stacked end labels keep at least `12` apart.
- Single-point series center on the plot.

## 435. Horizontal Bar
- For rankings and shares of `7+` parts; up to `12` rows; values must be zero or positive.
- Rows `30` tall, bars `18` thick, radius `2`.
- One focus row (default the first) in ink-blue with a weight-`500` value; all others light-stone `#b8b7b0`; focus may be none.
- Labels right-aligned `14` left of the bars, label column capped at `200`; values `8` after the bar end.
- A near-black `0.8` baseline runs down the bars' left edge.

## 436. Donut Chart
- For proportions; up to `6` segments; every value positive.
- Ring outer radius `112`, inner radius `68`, centered at `(114, 128)`; segments start at 12 o'clock and run clockwise in series order.
- Parchment separator rings at `1.5` on both outer and inner edges.
- Center shows the first (focal) share at `30` weight `500` in brand, with an optional center label at `11` stone `20` below.
- Legend sits beside the ring (`44` right of it) at reading size, `32`-tall rows vertically centered on the ring: swatch, percentage at `14`, then label at `12` olive.
- Shares are rounded to sum to exactly `100%` at the shown precision (largest remainder); default `0` decimals.

## 437. Waterfall
- For bridges and decompositions; up to `8` bars.
- Bars up to `64` wide (`75%` of the slot), radius `2`.
- Opening and closing totals charcoal from zero; increases ink-blue, decreases stone, floating between running levels.
- Dashed light-stone connectors (`0.8`, dash `3 2`) bridge each bar's level to the next bar's start.
- Value labels weight `500`, signed for deltas, `8` above or `14` below negative bars.
- A closing total must equal the running sum.

## 438. Candlestick
- For OHLC price action; up to `30` points; the axis does not need to start at zero.
- Bodies up to `16` wide (`50%` of the slot), radius `1`, minimum height `1`; wicks stroke `1.2` in the candle color.
- Up (close ≥ open) ink-blue; down stone.
- Thin out category labels to about `5` evenly spaced, at tick size `11` in stone.
- Legend always shows up and down.

# Part 56 — Labels and Annotation

## 439. Masked Edge Labels
- Every arrow label sits on a parchment masking rectangle so the line never bleeds through the text.
- Masks: radius `2`, height `12–14`, width snapped to the `4` grid (e.g. `48`, `56`, `84`).
- Label text: uppercase mono at `8`, letter-spacing `0.1–0.12em`, centered, in the color of its edge (olive or brand).
- A label mask never overlaps a node or another label, and no other edge may cross it.

## 440. Uppercase Mono Tags
- Category and role tags (`USER`, `EDGE`, `ORIGIN`, `STORE`, `STATE`, `FOCAL`, `STEP 01`) are uppercase mono at `7`, letter-spacing `0.15em`.
- Section and legend headings use wider tracking, `0.22em`; scope notes `0.18em`.
- Tags take the node's stroke color (brand on focal nodes, stone on external, olive on store).

## 441. No Vertical Text on Arrows
- Never use vertical writing mode on arrow labels; it is unreadable.
- Rotated text is reserved for lane names and axis titles only.

## 442. Labels Are Short
- Labels are single words or short phrases; sentences live in the document.
- Node copy has no full stops; use commas, slashes, semicolons, and middle dots to separate items.
- Separate list-like sublabels with a middle dot (`cache · SSL`, `render · route`).

## 443. Right-Side Captions
- Right-side captions and scope notes are right-aligned, end-anchored to the content edge, with at least `56px` outer margin.

# Part 57 — Illustration Briefs

## 444. When to Switch to Raster
- Use a generated raster illustration for a standalone illustration, a redraw of a photo or screenshot in house style, or a figure needing more detail than vector drawing holds at the display width (typically teaching-depth web figures).
- The brief is the deliverable you control; write it tightly so the image has nowhere to drift.

## 445. Brief Skeleton
- Claim: one sentence stating what the reader should conclude — the assertion, not the topic ("review protects the release boundary," not "software workflow").
- Placement: destination, aspect ratio, and smallest display size; each destination has a different type floor.
- Reference: the accepted sibling image or visual system it must sit beside, and what survives from it (composition, density, line language, crop).
- Exclusions: version strings, release copy, invented UI, unrelated atmosphere, extra hues, private identifiers.
- Canvas: warm parchment `#f5f4ed`, never pure white; generous whitespace; composed like a report figure.
- Accent: ink-blue `#1B365D` on the `1–2` focal elements only; everything else warm gray with a yellow-brown undertone; no second hue.
- Strokes and icons: thin single-line geometric strokes; flat rounded-line icons; no gradients, shadows, or 3D.
- Labels: serif, few, short — prefer single words, since generated images misspell long phrases; typeset any phrase over the image instead.
- Content: the complexity tier (`4/10` editorial or `6–7/10` teaching), what is focal, and the reading direction.

## 446. Batches Share One Style Anchor
- Drive multiple images from one list: slot, aspect ratio, shared style anchor, prompt, status.
- Generate at most `5` per batch, update status after each, and check existing output before regenerating.
- Per-image style drift is the failure mode; the anchor is shared by the whole batch.

## 447. Illustration Quality Check
- Palette holds: parchment ground, single blue accent, no stray hue, no cool grays.
- No gradient, shadow, or 3D.
- Text is correctly spelled and minimal; anything wrong is re-briefed with fewer words.
- Composition reads as a report figure with balanced margins and a clear focal point, not a poster or clip art.
- The claim is legible at the smallest stated display size.
- Every exclusion holds; style matches the other images in the deliverable.
- After two look-based rejections, stop blind regeneration: preserve the accepted part, show labeled alternatives side by side, and realign on claim, reference, and exclusions.

# Part 58 — Diagram Anti-Patterns

## 448. Cheap Technical Signifiers
- Dark mode with cyan or purple glow is a cheap "technical" signifier with no design decision.
- A monospace face as the universal "developer" font is wrong; names go in the serif/sans, mono only for ports, URLs, and fields.
- Shadows on anything are forbidden; only rings or whisper borders are permitted.
- Gradient backgrounds are forbidden.
- Border radius above `10` reads as app chrome.

## 449. Hierarchy Destroyers
- All nodes identical in size destroys hierarchy.
- Three equal-width summary cards as a default read as a template; vary widths.
- Per-node custom widths (e.g. `60 / 76 / 80 / 100`) feel hand-patched; small diagrams use `2` width tiers, large ones `3`.
- Ink-blue on every "important" node turns focal into noise.

## 450. Collision and Bleed
- A legend floating inside the diagram area collides with nodes.
- Arrow labels without a masking rectangle let the line bleed through.
- Text clipped at the canvas top because the baseline sits too high.
- A `5–10px` gap between arrow endpoint and node edge.
- A connector hugging a module's top edge reads as a broken border and a pressed module.

## 451. Redundant or Empty Structure
- A cycle drawn with both a dashed ring and four directed arcs reads as two flows.
- A ring of single-word nodes with an empty center has no anchor.
- Every fact drawn as its own small card instead of peers in one band.
- A paragraph inside a node.

## 452. Copy Failures
- A viewpoint caption ("from the X perspective," "working draft for Y").
- A full-sentence English translation duplicated on a CJK board.
- A bare protocol noun as a node title.
- A CJK full stop inside node copy.
- Prose renamed an object but the diagram still shows the old name.

## 453. Honesty Failures
- Future capability drawn at the same weight as shipped; the reader assumes it exists.
- Roadmap furniture (30/60/90, owner map, milestones) inside an architecture diagram.
- A focal color that contradicts the caption's claim.
- Porting an external diagram with one accent per node type.

## 454. Process Failures
- An exported image edited or resized instead of re-exported from the source.
- Only the source previewed, the exported image never opened at `100%`.
- A crowded board "fixed" by global scaling when the fault is module-level padding, line breaks, and baselines.
- Shrinking type or the export to relieve crowding instead of cutting, banding, or splitting.

# Part 59 — Resume

## 455. Page Setup
- Paper `A4`, margins `11mm 13mm 11mm 13mm` (top right bottom left); page background painted `#f5f4ed` parchment so no white edges print.
- Strict length target: exactly `2` pages; page 2 begins with a forced page break before the open-source / indie section.
- On screen the sheet is centred with `max-width: 210mm` and the same `11mm 13mm` padding, so screen and print match.
- Widows and orphans held at `3` lines.

## 456. Body Type
- Single serif for everything: `Charter, Georgia, Palatino, "Times New Roman", serif`; the "sans" role is aliased to the serif (one family per page).
- Body `9.4pt`, line-height `1.42`, letter-spacing `0`, colour near-black `#141413`.
- Links in ink blue `#1B365D`, no underline.
- Dense variant for 5+ projects: body drops to `9pt`, project text line-height `1.4`, project padding `1.6mm 0`, section-title margins `4.2mm` top / `1.5mm` bottom.

## 457. Header Band
- Flex row, name block left and contact block right, aligned on the bottom edge (`align-items: flex-end`).
- Separated from content by `0.6pt solid #e8e6dc` hairline; `2.3mm` padding above the rule, `4.2mm` gap below it.
- Name: `26pt`, weight `500`, letter-spacing `-0.2pt`, line-height `1`, never wraps; an alias/preferred name sits on the same baseline `3mm` to the right at `12.5pt` weight `400` in stone `#6b6a64`.
- Contact block right-aligned, `9pt`, line-height `1.5`, stone colour; role title on its own line in ink blue `10.5pt` weight `500`.
- Contact items separated by a middot coloured as the border `#e8e6dc` with `0.4em` side margins; links in dark-warm `#3d3d3a`; location in olive `#504e49` weight `500`.

## 458. Metric Strip
- Four equal columns (`repeat(4, minmax(0, 1fr))`), column gap `5mm`, `3mm` below; no boxes, no fills.
- Each metric stacks value over label with `0.7mm` gap and `1mm 0 1.2mm` padding.
- Value `13pt` weight `500` ink blue, line-height `1`, tabular figures, no wrap; unit suffix `10.5pt` with `0.5mm` left margin.
- Label `9pt` olive, line-height `1.2`, no wrap.
- Stacked variant adds a `0.3pt dotted #e8e6dc` underline per metric with `2mm` bottom padding.

## 459. Section Titles
- `13pt` weight `500` near-black, underlined by `0.5pt solid #e8e6dc`, `1mm` padding beneath text.
- Margins `5.8mm` above, `2mm` below; first section and first section on page 2 have no top margin.
- Optional right-aligned subtitle on the same baseline (flex `space-between`, gap `2.5mm`): `9pt`, weight `400`, stone, letter-spacing `0.2pt`.

## 460. Summary Paragraph
- About 50 words; `9.4pt` / `1.42`, near-black; key phrases coloured ink blue (colour, not bold, carries emphasis).

## 461. Career Timeline
- Three equal steps in a flex row, gap `7mm`, `2.5mm` below; each step `0.8mm` vertical padding, never split across pages.
- Top line: year in ink blue `11pt` weight `500` line-height `1`, then stage title `11pt` weight `500` near-black, `2mm` apart on a shared baseline, `0.6mm` below.
- Body `9pt` olive, line-height `1.45`, one sentence.

## 462. Project Blocks
- Repeat 3–5 times; each `2.6mm` vertical padding (`1.6mm` top for the first), never split.
- Head line: project name `11pt` weight `500`, then a middot and project type `11pt` olive with `1.5mm` left margin, `0.9mm` gap below.
- Role badge floated right: `9pt` weight `500` ink blue on solid tint `#EEF2F7`, padding `0.4mm 1.6mm`, radius `2pt`, letter-spacing `0.3pt`, uppercase.
- Body is a three-row label/text table (Role / Actions / Impact): label cell `16mm` wide, `9pt` weight `500` ink blue, letter-spacing `0.4pt`, uppercase, `0.4mm` vertical padding, top-aligned.
- Text cell `9.2pt` near-black line-height `1.45`, `1mm` left padding; impact row is numbers-first with 1–2 figures in ink blue.

## 463. Open-Source Grid
- Intro paragraph `9.4pt` / `1.45`, margins `1.6mm 0 2.4mm`; positioning line in ink blue; totals in weight `500`.
- Two-column grid, column gap `9mm`, row gap `1.2mm`.
- Each item a baseline-aligned flex row (gap `2.5mm`, `1.2mm` vertical padding) with `0.3pt dotted #e8e6dc` underline; last row in each column drops the rule.
- Name `10.5pt` weight `500` in ink blue, min width `18mm`; description `9pt` olive line-height `1.4`; star count right-aligned `9pt` dark-warm weight `500`, tabular, min width `10mm` (highlighted ones ink blue `9.2pt`).

## 464. Highlight Note
- Ivory `#faf9f5` fill, radius `2pt`, padding `1.8mm 3mm`, `2.5mm` above, `9pt` / `1.45`.
- Leading label inline: transparent background, ink blue `9pt` weight `500`, letter-spacing `0.6pt`, uppercase, `1.5mm` right margin.

## 465. Convictions Row
- Three equal columns, gap `3mm`, `1.4mm` above; each card only `2mm` right padding, no box.
- Head `10pt` weight `500` near-black with a date prefix in ink blue `9pt` tabular, `2mm` apart, `1mm` below.
- Body `9pt` olive line-height `1.45`.

## 466. Public Impact Block
- Handle strip: flex baseline row gap `3.5mm`, margins `1.4mm 0 2mm`; handle `10pt` weight `500` ink blue; follower count `9pt` stone tabular; description `9pt` olive `1.45`.
- Two-column grid `1.15fr 1fr`, gap `6mm` (writing left, talks right).
- Sub-block title `10pt` weight `500`, `0.3pt dotted` underline, `0.5mm` padding, `1.5mm` below, `2.5mm` above; a small `9pt` stone weight-`400` note shares the baseline.
- Rows `1.8mm` vertical padding with `0.3pt dotted #e5e3d8` separators, last row bare; titles `9.2pt` weight `500` line-height `1.4`; dates and venues `9pt` stone, tabular, no wrap.

## 467. Skills Rows
- Five fixed rows; each a baseline flex row (gap `3mm`, `1.8mm` padding) with `0.3pt dotted #e8e6dc` separators, last row bare.
- Label column `32mm` fixed: `9pt` weight `500` ink blue, letter-spacing `0.5pt`, uppercase, line-height `1.35`.
- Body `9.2pt` near-black line-height `1.45`, every row carrying at least one ink-blue emphasis.

## 468. Education Row
- One row, `space-between` baseline, `1.8mm` padding; school `11pt` weight `500`; college/major line `9.4pt` olive; dates `9pt` stone tabular; whole section unbreakable.

# Part 60 — Long Document

## 469. Page Setup
- Paper `A4`, margins `20mm 22mm 22mm 22mm`, parchment page background `#f5f4ed`.
- Body `10.5pt`, line-height `1.55`, near-black; widows/orphans `3` at body level, `2` for paragraphs.
- Spacing tokens: module rhythm `14pt`, section rhythm `18pt`.

## 470. Running Header and Folio
- Top-right running head pulls the current chapter title (set from each chapter heading): `8pt` serif in stone `#6b6a64`.
- Bottom-centre folio: page number, two spaces, a middot, two spaces, document title; `9pt` stone.
- Both are suppressed on the first (cover) page.

## 471. Cover Page
- Fills at least `240mm`, column flex with `space-between` so title block sits high and metadata sinks to the bottom; `40mm` top padding; page break after.
- Eyebrow: `10pt` ink blue weight `500`, letter-spacing `2pt`, uppercase, `18pt` below.
- Title: `40pt` weight `500`, line-height `1.12`, letter-spacing `-0.5pt`, `16pt` below, may span two lines.
- Subtitle: `14pt` olive line-height `1.45`, max width `85%`, `30pt` below.
- Meta block: `10pt` stone line-height `1.55` tabular; author line in dark-warm weight `500`.

## 472. Table of Contents
- Own page; heading `22pt` weight `500`, `14pt` below.
- Each entry a baseline row, `6pt` vertical padding, `0.3pt dotted #e8e6dc` separator (last bare), `11pt`.
- Two-digit chapter number in ink blue weight `500`, min width `30pt`, tabular; title `6pt` left padding.
- Page numbers generated from link targets, floated right, stone, tabular (title kept a block element so the numbers resolve).

## 473. Chapter Openers
- Every chapter starts on a new page.
- Chapter kicker above the heading: `10pt` ink blue weight `500`, letter-spacing `1pt`, uppercase, `6pt` below, format "01 · Name".
- Lead paragraph after the H1: `12pt` / `1.55` dark-warm, `14pt` below; brand-coloured emphasis on the sharpest claim.

## 474. Heading Scale
- H1 `24pt` weight `500`, line-height `1.15`, letter-spacing `-0.3pt`, `10pt` below, keeps with next.
- H2 `16pt` weight `500`, line-height `1.25`, margins `24pt` above / `8pt` below.
- H3 `13pt` weight `500`, line-height `1.3`, margins `18pt` / `6pt`, coloured dark-warm `#3d3d3a` to step down.
- No heading carries rules, bars or numbers-in-boxes; size alone sets hierarchy.

## 475. Lists
- Margins `6pt 0 10pt`, left indent `20pt`, line-height `1.55`.
- Bullet markers ink blue; ordered-list numerals ink blue weight `500`.

## 476. Quotations
- Indented `12pt 16pt`, `4pt` vertical padding, olive text, line-height `1.55`; no side rule, no italics.
- Citation on its own line `9pt` stone, `4pt` above, introduced with a dash.

## 477. Code
- Inline code: mono `9pt` on ivory `#faf9f5`, padding `1pt 4pt`, radius `2pt`, dark-warm text.
- Blocks: mono `9pt` line-height `1.5`, ivory fill, radius `4pt`, padding `10pt 14pt`, margins `10pt 0`, wrapped (`pre-wrap`), unbreakable, no border.

## 478. Callout and Takeaway
- Callout: ivory fill, padding `10pt 14pt`, radius `3pt`, margins `12pt 0`, line-height `1.55`; nested quotes drop to `6pt` margins and lose outer margins at the edges.
- Takeaway box: ivory fill, radius `4pt`, padding `10pt 14pt`, margins `14pt 0`; label `9pt` ink blue weight `500`, letter-spacing `1pt`, uppercase, `4pt` below.
- Neither carries a coloured edge or border; fill and type alone signal emphasis.

## 479. Tags
- Inline chip on solid `#E4ECF5`, ink blue `9pt` weight `500`, padding `1pt 6pt`, radius `3pt`, letter-spacing `0.4pt`, uppercase, `4pt` right margin.

## 480. Figures
- Margins `14pt 0`, unbreakable; images full width with `4pt` radius.
- Caption centred `9pt` stone, `6pt` above.
- Inline vector diagrams are centred and capped at `78%` of the column width so they never bleed past the text.

## 481. Executive Summary Panel
- Optional ivory panel, radius `6pt`, padding `16pt 20pt`, margins `14pt 0`, unbreakable; its H2 drops to `13pt` with no top margin.

# Part 61 — One-Pager

## 482. Page Setup
- Paper `A4`, margins `15mm 18mm` all round, parchment background; must fit one page.
- Body `10pt`, line-height `1.45`.

## 483. Editorial Header
- Flex row aligned to the bottom edge, gap `20pt`; `12pt` padding then `0.5pt solid #e8e6dc` rule, `16pt` below.
- Eyebrow `9pt` ink blue weight `500`, letter-spacing `1.5pt`, uppercase, `7pt` below.
- Headline `26pt` weight `500`, line-height `1.12`, letter-spacing `-0.3pt`, `5pt` below; verb-led, at most two lines.
- Subtitle `11.5pt` olive line-height `1.4`.
- Right-hand meta (author, date, version) `9pt` stone, right-aligned, line-height `1.5`, tabular, no wrap.
- Optional logo slot `44px` tall, max `160px` wide, contained, pinned to the top.

## 484. Metric Baseline Row
- Flex row of four, gap `16pt`, padding `4pt 0 6pt`, `18pt` below, single `0.3pt dotted` underline; no cards.
- Each metric puts value and label side by side on one baseline (gap `5pt`).
- Value `22pt` weight `500` ink blue, line-height `1`, letter-spacing `-0.3pt`, tabular; label `9pt` olive line-height `1.3`, no wrap.

## 485. Lead Paragraph
- `30–40` words, `12.5pt` / `1.5` dark-warm, `14pt` below; one ink-blue emphasis.

## 486. Product Shot
- Optional single screenshot as the visual anchor: frame `110mm` tall (tuned to fill the page), radius `5pt`, image cropped with `object-fit: cover` centred; `16pt` below.
- Caption centred `8.5pt` stone line-height `1.45`, `7pt` above, adds a fact rather than restating.

## 487. Sections and Columns
- Each section `18pt` below (last `0`), never split.
- Two equal columns with `18pt` gap for paired sections.
- H2 `16pt` weight `500`, `6pt` below; inline sub-label `9pt` stone weight `400` `6pt` to the right.
- Paragraphs `6pt` apart, line-height `1.45`.

## 488. Dash Lists
- Left indent `16pt`, items `5pt` apart, line-height `1.45`, ink-blue markers; one point per line.

## 489. Roadmap Timeline
- Three phases in a flex row, gap `12pt`, `6pt` above.
- Phase label `11pt` weight `500` ink blue, letter-spacing `0.3pt`, uppercase, `2pt` below; stage title `10pt` weight `500`; body `9pt` olive `1.45`.

## 490. Callout
- Ivory fill, radius `3pt`, padding `8pt 12pt`, margins `10pt 0`, `10.5pt` / `1.55` olive text, ink-blue emphasis.

## 491. Footer
- `18pt` above, `6pt` padding, `0.3pt dotted` top rule; `9pt` stone, tabular, letter-spacing `0.3pt`, `space-between`.

## 492. Print-White Variant
- For direct printing on white stock the page and body background switch to `#ffffff`; everything else (ivory cards, warm hairlines) is retained.
- That variant's numbers: headline `25pt` / `1.15`, metric value `24pt` letter-spacing `-0.2pt`, metric gap `14pt`, metric row `22pt` below, section spacing `20pt`.

# Part 62 — Letter

## 493. Page Setup
- Paper `A4`, generous equal margins `25mm` all round; parchment background.
- Body `11.5pt`, line-height `1.55` — the largest body size in the system, for reading at arm's length.

## 494. Letterhead
- Right-aligned block, `10pt` olive line-height `1.55`, `30pt` below.
- Sender name `13pt` weight `500` near-black, `4pt` below; links dark-warm, no underline.

## 495. Date Line
- Right-aligned `10.5pt` olive, tabular, no wrap, `24pt` below.

## 496. Recipient Block
- `24pt` below, line-height `1.5`.
- "To" label `9pt` stone weight `500`, letter-spacing `0.5pt`, uppercase, `3pt` below.
- Name `12pt` weight `500`; organisation `10.5pt` olive.

## 497. Subject Line
- `24pt` below; "Re" label `9pt` ink blue weight `500`, letter-spacing `1pt`, uppercase, `3pt` below.
- Subject `16pt` weight `500`, line-height `1.25`, letter-spacing `-0.2pt`, one sentence.

## 498. Salutation and Body
- Salutation `12pt`, `18pt` below.
- Paragraphs left-aligned (ragged right), `12pt` apart, line-height `1.55`; no first-line indent by default, optional `1.5em` indent class.
- At most four paragraphs: purpose, elaboration, specific ask, close; one ink-blue weight-`500` emphasis.

## 499. Closing and Signature
- `28pt` above; complimentary close `30pt` above the signature (room for a hand signature).
- Signature name `14pt` weight `500`, `3pt` below; title/department meta `10pt` olive line-height `1.5`.

## 500. Enclosures
- `36pt` above, `10pt` padding, `0.5pt dotted #e8e6dc` top rule; `9.5pt` stone line-height `1.55`.
- Label inline in ink blue weight `500`, letter-spacing `0.5pt`, uppercase, `6pt` right margin; items numbered with circled numerals.

## 501. Memo Variant
- Body drops to `10.5pt` / `1.55`, no paragraph indents, `10pt` paragraph spacing.

# Part 63 — Portfolio

## 502. Page Setup
- Paper `A4`, margins `12mm 15mm`; the first page has zero margin so the cover fills the sheet.
- Body `10pt` line-height `1.45`; module rhythm `14pt`, section rhythm `18pt`.

## 503. Full-Bleed Cover
- Exactly `297mm` tall, padding `25mm 20mm`, three-band column flex with `space-between` (top label, centre, bottom meta).
- Top label `10pt` ink blue weight `500`, letter-spacing `2.5pt`, uppercase (e.g. year range).
- Optional logo `72px` tall, max `200px` wide, `16pt` below.
- Centre stack gap `14pt`: name + "Portfolio" at `64pt` weight `500`, line-height `1.1`, letter-spacing `-1pt`; tagline `18pt` olive `1.4`, max `80%`; intro `11pt` dark-warm `1.55`, max `80%`.
- Bottom meta: two columns (discipline/location left, contact right-aligned), `10pt` stone, tabular; key line dark-warm weight `500`.

## 504. About Page (Optional)
- Only when there is enough to fill a whole page; otherwise omitted.
- Eyebrow `9pt` ink blue letter-spacing `1.5pt` uppercase; title `24pt` / `1.2`, `14pt` below; lead `11pt` dark-warm `1.55`, `22pt` below.
- Metrics in a four-column grid, gap `12pt`, `16pt` vertical padding between two `0.5pt solid` rules, `28pt` below; value `16pt` ink blue line-height `1.2`; label `9pt` stone `3pt` above.
- Sub-heads `13pt` weight `500`, margins `26pt 0 8pt`.
- Career timeline as a definition grid `62pt 1fr`, column gap `10pt`, row gap `7pt`; years in ink blue, no wrap.
- Project index table: first column ink blue, second stone, both no-wrap; `34pt` above.

## 505. Project Page Header
- One project per page (break before and after), `8mm` vertical padding.
- Large project number `48pt` weight `500` ink blue, line-height `1`, letter-spacing `-1pt`, `18pt` right margin.
- Title block `6pt` top padding: type label `9pt` ink blue letter-spacing `1.5pt` uppercase; title `24pt` / `1.2` letter-spacing `-0.3pt`; subtitle `11pt` olive `1.4`.
- Date right-aligned `9pt` stone tabular, min width `80pt`, `10pt` top padding.

## 506. Project Tags
- Wrapping flex row, gap `4pt`; chips on `#E4ECF5`, ink blue `9pt` weight `500`, padding `2pt 8pt`, radius `3pt`, letter-spacing `0.4pt`, uppercase.

## 507. Hero Image
- Full width, `110mm` tall, ivory placeholder, radius `6pt`, image cropped to cover.
- Two-image variant: two columns, gap `10pt`, each `80mm` tall.

## 508. Three-Column Body
- Equal columns, gap `16pt` (e.g. challenge / approach / outcome).
- Column head `12pt` weight `500` ink blue, letter-spacing `0.3pt`, `4pt` below; text `9.5pt` dark-warm line-height `1.5`.

## 509. Results Row
- Flex row gap `14pt`, `10pt` padding above a `0.5pt dotted` top rule.
- Value `20pt` weight `500` ink blue line-height `1.1` tabular; label `9pt` olive `1.3`, `2pt` above.

## 510. Selected Works List
- New page, `10mm` top padding; title `26pt` letter-spacing `-0.3pt`, `16pt` below.
- Rows on a grid `40pt 1fr 80pt`, gap `12pt`, `8pt` padding, `0.3pt dotted` separators, baseline aligned.
- Year `11pt` ink blue tabular; title `11pt` weight `500`; description `9pt` olive; link/date right-aligned `9pt` stone.

## 511. Contact Page
- New page, `20mm` padding, min height `230mm`, content vertically centred.
- Eyebrow `10pt` ink blue letter-spacing `2pt`; title `52pt` weight `500` line-height `1.05` letter-spacing `-1pt`, `20pt` below.
- Contact list `12pt` dark-warm `1.55`; labels `10pt` stone weight `500`, letter-spacing `1pt`, uppercase, min width `80pt`, `12pt` right margin; links ink blue.

# Part 64 — Equity / Research Report

## 512. Page Setup
- Paper `A4`, margins `16mm 18mm 18mm 18mm`; body `10pt` line-height `1.5`.
- Folio at bottom centre: page number, middot, company name + "Report", `9pt` stone.
- Semantic colours stay monochrome: positive is ink blue `#1B365D`, negative is stone `#6b6a64` — no red/green.

## 513. Ticker Header
- Flex `space-between`, top aligned; `10pt` padding then `0.5pt solid` rule, `14pt` below.
- Eyebrow `9pt` ink blue letter-spacing `1.5pt` uppercase, `4pt` below.
- Company name `26pt` / `1.12`, letter-spacing `-0.3pt`; ticker symbol inline at `14pt` stone.
- Sub-line `10pt` olive: sector · exchange · one-line thesis.
- Price block right-aligned, `4pt` top padding: current price `30pt` weight `500` near-black, line-height `1`, letter-spacing `-0.5pt`, tabular; change `10pt` weight `500` tabular; date `9pt` stone.

## 514. Key Metrics Band
- Flex row of four, gap `16pt`, padding `6pt 0`, between `0.3pt dotted` top and bottom rules, `16pt` below.
- Value `18pt` weight `500` ink blue line-height `1` letter-spacing `-0.3pt` tabular, label `9pt` olive beside it on one baseline (gap `5pt`).

## 515. Section Heads
- H2 `16pt` weight `500`, margins `18pt 0 6pt`, keeps with next.
- Rating H2 variant: heading and rating share a baseline; rating label `9pt` stone weight `400`, rating word `15pt` weight `500` ink blue `5pt` to the right.
- H3 `13pt` dark-warm, margins `12pt 0 4pt`.
- Paragraphs `8pt` apart; lists margins `4pt 0 8pt`, indent `18pt`, ink-blue markers.

## 516. Financial Tables
- Numeric columns right-aligned with tabular figures, first column left.
- Peer comparison uses the compact variant (`8pt` text), with the subject company in weight `500`.

## 517. Chart Slots
- Ivory placeholder, radius `4pt`, centred `9pt` stone label; price chart `60mm` tall, revenue breakdown `50mm`.
- Figures `12pt` vertical margin; caption centred `9pt` stone `4pt` above.

## 518. Risk Matrix
- Two-column grid, gap `10pt 24pt`, margins `8pt 0 14pt`; items unbreakable.
- Risk label `9pt` weight `500` ink blue, letter-spacing `0.3pt`, uppercase, `2pt` below; description `9pt` olive `1.45`.

## 519. Verdict Block
- No fill: a `0.6pt solid` top hairline, `8pt` padding, `14pt` above — the page already has its fills.
- Lead sentence `11pt` near-black `1.5`, `6pt` below.
- Bull / bear / catalyst definitions on a grid `62pt 1fr`, gaps `10pt` / `4pt`; terms `9pt` ink blue weight `500` letter-spacing `0.3pt` uppercase.

## 520. Report Footer
- `16pt` above, `6pt` padding, `0.3pt dotted` top rule; `9pt` stone, tabular, `space-between` (disclaimer / source).

# Part 65 — Changelog

## 521. Page Setup
- Paper `A4`, margins `20mm 22mm 22mm 22mm`; body `10.5pt` line-height `1.55`.

## 522. Release Header
- Same editorial opener as the one-pager: bottom-aligned flex row, gap `20pt`, `13pt` padding, `0.5pt solid` rule, `20pt` below.
- Eyebrow "Release Notes" `9pt` ink blue letter-spacing `1.5pt` uppercase, `8pt` below.
- Title (product + version) `29pt` weight `500`, line-height `1.1`, letter-spacing `-0.5pt`, `7pt` below.
- Subtitle `11.5pt` olive `1.45`, max width `150mm`; release date right `10pt` stone tabular.

## 523. Section Heads
- H2 `14pt` weight `500`, margins `20pt 0 10pt`, first one `0` top; type and spacing only.
- Order: Breaking Changes, Features, Fixes; drop any empty section.

## 524. Change Lists
- Numbered list, indent `18pt`, items `7pt` apart with `3pt` extra left padding, line-height `1.55`, never split.
- Markers ink blue weight `500`; numbering restarts per section.
- Each entry: bold lead-in (weight `500`), colon, then a one-line detail; inline code at `0.92em` mono.

## 525. Breaking Tag
- Standard tag shape (`9pt`, padding `1pt 6pt`, radius `3pt`, uppercase) recoloured to warm rust: background `#f0e0d8`, text `#8b4513` — the system's only warning hue.

## 526. Acknowledgements
- Quiet labelled note, no card: `18pt` above, `9.5pt` olive `1.55`.
- Label `9pt` ink blue weight `500`, letter-spacing `1pt`, uppercase, `4pt` below.

## 527. Footer
- `20pt` above, `8pt` padding, `0.3pt dotted` rule; `9pt` stone, line-height `1.5`, tabular, letter-spacing `0.3pt`; description left, project URL right.

# Part 66 — Landing Page

## 528. Canvas and Container
- Page background parchment `#f5f4ed`; content column `max-width: 1120px`, padding `88px 64px 120px`.
- Body `15px` serif, line-height `1.55`, letter-spacing `0`, antialiased font smoothing.
- A system UI sans (`system-ui, -apple-system, "Segoe UI", sans-serif`) is allowed only for tiny Latin UI chrome (eyebrow, tokens, tab pills, metric labels, footer links).
- Extra tokens: inline-code fill `#f0eee6`, warm sand `#e8e6dc`, control line `#d8d5c8`, lighter brand `#2D5A8A`, brand tint `#EEF2F7`, screenshot backdrop `#141318`.

## 529. Links and Motion
- Links ink blue, no underline, hover to `#2D5A8A` over `0.15s`.
- Reduced-motion preference disables gallery transforms and transitions.

## 530. Buttons
- Pill shape (`border-radius: 999px`), padding `13px 28px`, `15px` weight `500`, letter-spacing `0.2px`, min width `158px`, gap `8px`.
- Primary: ink blue fill and border, ivory text; hover to `#2D5A8A` and lift `translateY(-1px)`.
- Ghost: ivory fill, `1px solid #d8d5c8` border, near-black text; hover fill warm sand, same lift.
- Hero places ghost first and primary second, `24px` apart.
- On phones (≤`480px`): buttons `42px` tall, `0 22px` sides, min width `128px`, `12px` apart, no wrap of labels; below `375px` sides drop to `14px`; ghost hairline softened to `60%` line mixed into ivory.

## 531. Hero
- `48px` bottom padding, `1px solid #e5e3d8` rule, `80px` below.
- Eyebrow row: flex `space-between`, `12px` UI sans weight `500`, letter-spacing `0.4px`, uppercase, stone, `22px` below; version link ink blue weight `600`; social icon links stone, `12px` apart.
- Product name `96px` weight `500`, line-height `1.05`, letter-spacing `0`, `18px` below.
- Tagline `21px` weight `400` olive, line-height `1.4`, letter-spacing `0.2px`, max `820px`, `28px` below.
- Fact tokens: wrapping row, gap `18px`, `13px` stone, value bolded in dark-warm weight `500`, `32px` below.

## 532. Section Primitives
- Sections `72px` apart; head block `24px` below.
- Section title `32px` weight `500` line-height `1.2`.
- Lede `17px` olive `1.55`, `14px` above; optional "replaces X · Y" line `14px` stone with competitor names in ink blue.

## 533. Screenshot Gallery
- Frame on dark backdrop `#141318`, `1px solid #e8e6dc` border, radius `8px`, `ew-resize` cursor.
- Panels cross-fade and slide: incoming from `+44px` (or `-44px` going back), outgoing to `-34px`, scale `0.985`; opacity `620ms` and transform `880ms` on `cubic-bezier(0.22, 1, 0.36, 1)`.
- Auto-advance every `4.5s`; switch lock `~920ms`.
- Caption below: title `17px` weight `500` and one-line detail `14px` olive on a baseline, gap `14px`, min height `48px`, dims to `0.72` while switching.
- Tab pills right-aligned: `12px` UI sans, padding `8px 12px`, radius `999px`, `1px solid #e5e3d8`; active pill ink blue text on `#EEF2F7`.

## 534. Feature List
- Definition-style rows on a `200px 1fr` grid, column gap `36px`, `28px` vertical padding, `1px solid #e5e3d8` rules top and between.
- Feature name `22px` weight `500` ink blue `1.2`, optional context line `13px` olive; description `15px` dark-warm `1.55`.

## 535. Principles Grid
- Two columns separated by a `1px` vertical rule; rows `22px` padding, horizontal rules; odd items `32px` right padding, even items `32px` left padding; an odd last item spans both columns.
- Number column `32px`: `18px` weight `500` ink blue; title `15px` weight `500`, `4px` below; explanation `13px` olive `1.5`.

## 536. Manifesto
- `20px` / `1.55`, letter-spacing `0.05em`, weight `400`, near-black; emphasised words in ink blue without italics.

## 537. Install Code Block
- Ivory fill, `1px solid #e8e6dc`, radius `6px`, padding `18px 22px`, mono `13.5px` / `1.55`, lining tabular figures; comments stone, keywords ink blue.

## 538. Key Numbers
- Wrapping flex, gap `32px`; value `36px` weight `500` near-black line-height `1`; label `13px` UI sans stone.

## 539. Demo Cards
- Auto-fill grid, min `240px`, gap `18px`; card ivory with `1px` border and `8px` radius; image with bottom rule; title `15px` weight `500` (margins `12px 14px 4px`), description `12px` olive.

## 540. Pricing Card
- Centred column, max `960px`, padding `72px 32px 64px`, `1px solid #d8d5c8` rules above and below, no box.
- Benefits lead: 4–6 one-line items `16px` dark-warm, `4px` padding, `36px` below.
- Price stated once at medium size: `30px` weight `500`, tabular — never a display-size price tag.
- Comparison line `18px` dark-warm, max `580px`, `40px` below; struck-through old price in stone with `1px` line; saving in ink blue.
- Primary button min `280px`, padding `15px 28px`, `15.5px`; trial line `14px` stone with underlined link (offset `3px`); terms `13.5px` olive, max `640px`, separators in line colour.

## 541. FAQ
- Pairs `24px` apart; question `16px` weight `500`, letter-spacing `0.1px`, `6px` below; answer `14px` olive `1.55`; inline code `12px` mono on `#f0eee6`, radius `2px`.

## 542. Footer
- `56px` above, `40px` padding, `1px solid #e5e3d8` top rule, `space-between` bottom aligned, gap `48px`, `13px` stone.
- Wordmark: `56px` icon (radius `8px`) spanning two rows beside name `28px` weight `500` and tagline `13px` olive.
- Colophon right-aligned, max `480px`: middot-separated links in dark-warm (hover ink blue), `16px` below; ethos line olive, max `360px`.

## 543. Responsive Steps
- ≤`880px`: padding `64px 32px 80px`; hero name `64px`, tagline `18px`; sections `56px` apart, titles `26px`; features and principles collapse to one column; price `24px`; footer stacks left-aligned.
- ≤`480px`: hero name `56px`, tagline `17px`; gallery caption stacks.
- Print: page background forced to parchment with exact colour printing; sections `36px` apart; hero, cards, price card, quotes and code kept whole.

# Part 67 — Social Cards

## 544. Card Format
- Each card is one image: `1242 × 1660px` (3:4), zero page margin, one card per page.
- Padding `120px 96px 84px`; content that would collide with the footer is split into another card, never shrunk.
- For square-cropping feeds, headline and key evidence stay inside the centre `1242 × 1242` area.

## 545. Type Scale
- Meta line `30px`, line-height `1.4`, letter-spacing `1.2px`, stone.
- Cover headline `104px` weight `500`, line-height `1.28`, letter-spacing `1px`, `72px` above, max width `10em`; a short last line is fixed by narrowing max width, not by manual breaks.
- Verse / subtitle `46px` / `1.4`, letter-spacing `0.5px`, accent colour, `48px` above.
- Card heading `80px` weight `500` line-height `1.2`, `56px` above.
- Body paragraphs `44px` / `1.5`, `44px` above; bold phrases in accent colour weight `500`.

## 546. Cover Photo
- Absolutely placed from `640px` top to `96px` bottom, `96px` side insets, radius `20px`, image cropped to cover at `center 60%`; a real photo or screenshot is required.

## 547. List Items
- Flex rows `48px` apart; number column `120px` fixed, `64px` bold (`700`) serif, line-height `1.1`, accent colour, two-digit numbering; item text `42px` / `1.48`.
- Two to five items per card.

## 548. Screenshot Card
- One claim plus one real screenshot, `56px` above, radius `20px`, full width.

## 549. Footer Rule
- Pinned `84px` from the bottom with `96px` side insets; `30px` padding over a `1px` rule (`#d1d0ca` on parchment); `28px` / `1.4` stone.

## 550. Paper Palettes
- Default: parchment `#f5f4ed`, near-black text, ink-blue accent.
- Each alternative paper recolours four roles (background / foreground / accent / muted) plus a line colour; one paper per set.
- Ink: `#1B365D` / `#f3f1e8` / `#b9c6d8` / `#8e9db3`, line `#3e5473`.
- Olive: `#2b3326` / `#ece8da` / `#bdb38c` / `#9a9883`, line `#4a5043`.
- Espresso: `#3a2a20` / `#f2e9dc` / `#d9b48a` / `#a8957f`, line `#57493e`.
- Pine: `#1c3a29` / `#eef0e6` / `#b5cfa4` / `#8fa593`, line `#3e5747`.
- Teal: `#134857` / `#eef2ef` / `#a8d0cf` / `#8fb0b4`, line `#36636f`.
- Crimson: `#5a1f17` / `#f4ebe2` / `#e6bca6` / `#bd968a`, line `#734037`.
- Char: `#1e1d1b` / `#f2f0ea` / `#d4c4a0` / `#a8a49a`, line `#403f3c`.
- On every dark paper all text is set at weight `500`, because light text on dark rasterises thinner than it previews.

## 551. Content Rules
- Keep the author's words as written; one point per text card, two or three paragraphs.
- Meta and footer repeat the post title; cover headline equals the post title.

# Part 68 — Slides

## 552. Page-Rendered Deck Format
- Slide `280mm × 158mm` (16:9-ish), zero page margin, parchment background, padding `16mm 20mm`, column flex.
- Base text `13pt` line-height `1.55`; module rhythm `16pt`, section rhythm `22pt`.

## 553. Slide Chrome
- Eyebrow above the title in mono `10pt`, letter-spacing `2pt`, uppercase, stone, format "01 · Section".
- Page number bottom-right at `10mm` / `20mm`: mono `9.5pt` stone, letter-spacing `0.5pt`, tabular, two digits.
- Footer mark bottom-left at `10mm` / `20mm`: mono `9.5pt` stone, letter-spacing `1.5pt` (project name).

## 554. Slide Type Scale
- Title (H2) `32pt` weight `500`, line-height `1.2`, letter-spacing `-0.3pt`, `16pt` below; the title states a claim, not a topic.
- H3 `18pt` weight `500` ink blue `1.3`, `8pt` below.
- Lead `16pt` olive `1.5`, `8pt` below.
- Module title `19pt` weight `500` `1.3`, with a module letter (A/B/C/D) `28pt` ink blue `6pt` before it.
- Module separator label: mono `9pt`, letter-spacing `1.5pt`, uppercase, stone, `0.3pt solid` underline, `4pt` padding.
- Module body `13pt` dark-warm `1.55`, `22pt` below; list item `13pt` with `8pt` vertical padding.
- Module caption `11pt` olive `1.5`, `0.3pt solid` top rule, `8pt` padding, `22pt` above.

## 555. Pinned Conclusion
- Bottom-line takeaway absolutely pinned `22mm` from the bottom, `20mm` side insets: `14pt` weight `500` ink blue `1.55`.

## 556. Layout Grids
- Two columns: equal, gap `22pt`.
- 2×2 modules use a separated table (spacing `22pt 18pt`, negative margins `-18pt -22pt` to cancel the outer spacing) rather than a grid, so rows align their heights reliably.
- Data table: full width, cells `8pt` padding, `0.25pt solid #e8e6dc` bottom rules, `13pt` / `1.55`; first column weight `500` dark-warm flush left, last column flush right.
- Inline diagrams capped at `105mm` tall.

## 557. Cover Slide
- Centred both axes; title `44pt` weight `500`, line-height `1.05`, letter-spacing `-0.5pt`, `12pt` below.
- Subtitle `16pt` olive `1.45`, max `50ch`, `32pt` below; meta mono `10pt` stone letter-spacing `1.5pt` uppercase ("Author · Date").
- Optional logo `72px` tall, max `220px` wide, `24pt` below.

## 558. Markdown Deck Variant
- Same slide size and padding, base `13pt`, but the content scale steps down: title `24pt` with balanced wrapping, H3 `15pt`, lead `12pt`, module title `16pt`, module letter `24pt`, body and lists `11pt`, caption `9.5pt`, separator label `7.5pt`, eyebrow `9.5pt`.
- Lists: indent `1.4em`, items `4pt` apart, ink-blue markers.
- Pinned conclusion `11pt` at `18mm` from bottom; cover title `38pt`, subtitle `14pt`, meta `9.5pt`.
- Page number and footer mark mono `9pt` at `10mm` from bottom, `20mm` from sides; both hidden on cover slides.
- Rhythm tokens tighten to `14pt` module / `18pt` section.

## 559. Native Presentation-File Variant
- Slide `13.33in × 7.5in` (16:9); every slide starts with a full-bleed parchment rectangle; text boxes have zero internal margins and word wrap on.
- Palette mirrors the documents; pure white `#ffffff` appears only as text on ink-blue chapter slides.
- Cover: title `48pt` centred at `2.5in` from top across `11.33in`; subtitle `18pt` olive at `4.6in`; author · date `13pt` stone at `6.5in`.
- Contents slide: heading `34pt` at `1.2in` / `0.8in`; entries every `0.9in` from `2.4in`, number `28pt` ink blue, label `22pt` at `2.4in`.
- Chapter slide: full ink-blue background, two-digit number `28pt` white top-left (`0.8in`, `0.5in`), title `60pt` white centred at `3in`.
- Content slide: eyebrow `11pt` stone at `0.6in`, title `34pt` at `1.2in`, body `18pt` dark-warm at `3in` (max three lines), page number `11pt` stone bottom-right at `6.9in` formatted " - 05".
- Metrics slide: title `30pt` centred; cards `2.8in` wide with `0.3in` gaps, centred as a group; value `56pt` ink blue, label `14pt` olive.
- Quote slide: quotation in curly quotes `30pt` centred and vertically middle, source `14pt` olive below with a dash.
- Comparison slide: left column (old) muted — title `22pt` olive, items `17pt` stone; right column (new) full colour — title `22pt` near-black, items `17pt` dark-warm; columns at `1.2in` and `7.0in`, items every `0.9in`, max four.
- Pipeline slide: up to four steps across `11.5in`; numbers `42pt` ink blue at `2.5in`, step title `19pt` at `3.45in`, description `15pt` olive at `4.15in`.
- Ending slide: message `44pt` centred at `3in`, contact `16pt` olive at `4.8in`.
- Optional cards: ivory rounded rectangle with `0.5pt` border `#e8e6dc`, no shadow.

## 560. Landscape Keynote Demonstration
- A4 landscape `297mm × 210mm`, padding `18mm 22mm`; eyebrow mono `9pt` letter-spacing `2.5pt`.
- Split cover: two columns gap `32pt`; mark mono `10pt` ink blue letter-spacing `3pt`; title `42pt` line-height `1.05` letter-spacing `-1.5pt`; subtitle `15pt` max `34ch`.
- Content titles `38pt` / `1.1`, letter-spacing `-0.6pt`, max `24ch`, `28pt` below; claim paragraph `17pt` / `1.45`.
- Numbered points via counters: `12.5pt` / `1.5`, `18pt` hanging indent, ink-blue tabular numerals.
- Callout without ornament: transparent, `8pt` vertical padding, `14pt` olive.
- Stacked metrics (number above label so all numbers share one baseline even when labels wrap): value `32pt` ink blue, unit suffix at `0.58em` weight `400` raised `0.08em`, label `10pt` olive, `20pt` gap, dotted top rule.
- Code card: ivory, `1px` border, radius `6pt`, padding `14pt 18pt`, mono `10pt`.
- Ending title `52pt` letter-spacing `-0.8pt`, subtitle `17pt` max `44ch`.

# Part 69 — Shared Template Tokens

## 561. Colour Palette
- Parchment `#f5f4ed` (page), ivory `#faf9f5` (cards, code, callouts), warm sand `#e8e6dc` (secondary buttons).
- Text ladder: near-black `#141413` (body, headings), dark-warm `#3d3d3a` (H3, table heads, leads), olive `#504e49` (secondary text, captions), stone `#6b6a64` (meta, dates, folios).
- Accent: ink blue `#1B365D` only; lighter ink `#2D5A8A` for hover/links on dark.
- Borders: `#e8e6dc` standard, `#e5e3d8` soft; deeper edge `#dedbcf` for light surfaces on parchment.
- Tag fills (solid only): default `#E4ECF5`, receded `#EEF2F7`.
- Other reserved tones: dark surface `#30302e`, error `#B53333`, breaking-change rust `#f0e0d8` / `#8b4513`.
- All greys are warm (R ≈ G > B); no cool blue-greys; no second chromatic hue.

## 562. Accent Discipline
- Ink blue covers no more than about `5%` of any page.
- Used for: eyebrows, labels, numbering, list markers, metric values, links, single emphasised phrases.
- Emphasis is by colour (and at most weight `500`), never by heavy bold.

## 563. Font Stacks
- Latin serif: `Charter, Georgia, Palatino, "Times New Roman", serif`; the sans role points at the same stack.
- Mono: `"JetBrains Mono", "SF Mono", "Fira Code", Consolas, Monaco, monospace` at weights `400` and `500`, for code, version numbers, hex values and slide chrome only.
- Body weight `400`, headings and emphasis `500`; never `600+` synthetic bold.

## 564. Line-Height Bands
- Tight titles `1.05–1.3`; dense content `1.4–1.45`; reading text `1.5–1.55`.

## 565. Numeric Typesetting
- Every date, price, count, metric and page number uses tabular figures; values that must stay together use no-wrap.
- Metrics are always a transparent baseline row: serif ink-blue number + small olive label, no containers.

## 566. Hairline Grammar
- Structural rule (header/section boundary): `0.5–0.6pt solid #e8e6dc`.
- Row separators within lists: `0.3pt dotted #e8e6dc` with the last row bare.
- Table body rules: `0.25pt solid`; table head rule `0.6pt solid`.
- No vertical accent bars, no left-border callouts, no coloured edges on cards.

## 567. Standard Document Table
- Full width, collapsed borders, left-aligned headers weight `500` dark-warm on transparent background, cells top-aligned.
- Sizes scale with document: resume/one-pager `9pt`, cells `4pt 6pt`, heads `5pt 6pt`, margin `6–8pt`; long doc/report/portfolio `9.5pt`, cells `5pt 8pt`, heads `6pt 8pt`; letter `10pt`.
- Compact variant: `8pt`, heads `3pt` vertical padding, cells `2.5pt`, line-height `1.4`.
- Financial variant: every column after the first right-aligned with tabular figures.
- Striped variant: even rows ivory, keeps cell insets so the fill has room.
- Total row: weight `500`, `0.6pt solid` top rule, no bottom rule.
- Non-striped tables zero out outer left/right padding so the first and last columns sit on the text edge, aligning with the heading above.
- Tables never break across pages.

## 568. Tag Primitive
- `9pt` weight `500` ink blue on solid `#E4ECF5`, padding `1pt 6pt` (`2pt 8pt` on portfolio), radius `3pt`, letter-spacing `0.4pt`, uppercase.
- Solid hex only; translucent fills render as double rectangles in some PDF engines.

## 569. Eyebrow / Kicker Primitive
- `9–10pt` ink blue weight `500`, uppercase, letter-spacing `1–2.5pt` (bigger and wider on covers), `4–18pt` below.

## 570. Spacing Scale
- Base unit `4pt`: xs `2–3pt` inline; sm `4–5pt` tag padding; md `8–10pt` component internals; lg `16–20pt` between components / card padding; xl `24–32pt` section-title margins; 2xl `40–60pt` between major sections; 3xl `80–120pt` between long-document chapters.
- Denser documents get smaller margins (resume `11/13mm`), formal ones larger (letter `25mm`).

## 571. Radii and Depth
- Print chip `2pt`, print block `3–4pt`, large panels `6pt`, screen blocks `8px`, social images `20px`.
- Surfaces flat by default; shadows reserved for genuinely floating things (screenshots, popovers).

## 572. Print Behaviour
- `@page` background matches the parchment so printed pages have no white rims.
- Cards, tables, figures, callouts and metric groups never split across pages; headings keep with next.
- Screen preview centres a `210mm` sheet with the same padding as the print margins.

## 573. Brand Override
- Optional logo slots exist on one-pager (`44px`), portfolio (`72px`), and slide cover (`72px`); left empty rather than showing a broken image.
- A supplied brand profile replaces palette and fonts; structure stays.

# Part 70 — Korean/CJK Typesetting Differences

## 574. Chinese Font Stack
- Text face TsangerJinKai02 in two real weights: W04 for `400` body, W05 for `500` headings (no synthetic bold).
- Fallbacks: `"Source Han Serif SC", "Source Han Serif CN", "Noto Serif CJK SC", "Noto Serif SC", "Songti SC", "STSong", "SimSun", Georgia, serif`.
- Where Latin should stay Latin (social cards), the stack leads with `Charter, Georgia` so letters and digits set in Charter while Chinese falls through to the CJK face.

## 575. Korean Font Stack
- Text face Source Han Serif K, Regular `400` and Medium `500`.
- Fallbacks: `"Source Han Serif KR", "Noto Serif KR", "Nanum Myeongjo", "AppleMyungjo", "Apple SD Gothic Neo", Charter, Georgia, serif`.
- `font-synthesis: none` so the renderer never fakes bold or italic hangul.

## 576. Japanese Font Stack
- `"YuMincho", "Yu Mincho", "Hiragino Mincho ProN", "Noto Serif CJK JP", "Source Han Serif JP", "TsangerJinKai02", Georgia, serif`.
- Mincho strokes are thinner, so olive text darkens to `#4d4c48`; body line-height opens to `1.6`, letter-spacing `0.3pt`.

## 577. Letter-Spacing
- CJK body gets positive tracking `0.3pt` (Latin body is `0`).
- Display sizes switch from negative tracking (Latin `-0.2` to `-1pt`) to positive (`0.3–1pt`): e.g. resume name `+0.5pt`, portfolio cover `+1pt`, slide titles `+0.3pt`.
- Social cards in Chinese track much wider: headline `5.5px`, heading `3px`; Korean headline `1px`.

## 578. Size Adjustments
- CJK display sizes drop roughly 8–10% because ideographs fill the em box: long-doc cover `40pt → 36pt`, H1 `24pt → 22pt`; one-pager H1 `26pt → 24pt`, metric `22pt → 20pt`, lead `12.5pt → 12pt`; portfolio cover `64pt → 58pt`, project number `48pt → 42pt`, contact title `52pt → 48pt`; changelog title `29pt → 26pt`; equity price `30pt → 28pt`, metric `18pt → 16pt`; letter subject `16pt → 15pt`.
- Resume body `9.4pt → 9.2pt`, name `26pt → 26.5pt`, section title `13pt → 12.5pt`.
- Native deck in Chinese uses slightly smaller titles than Latin (cover `44pt` vs `48pt`, chapter `56pt` vs `60pt`, metric `52pt` vs `56pt`).

## 579. Line-Height Adjustments
- Display line-height loosens slightly (`1.12 → 1.15`, `1.05 → 1.1`).
- Social card body opens to `1.75` (Chinese) / `1.7` (Korean) versus `1.5`; list text `1.68` / `1.65` versus `1.48`; headings `1.3` versus `1.2`.
- Cover headline max width narrows to `7.3em` (Chinese) / `8.5em` (Korean) versus `10em`.

## 580. Uppercase and Tracking Labels
- Uppercase transforms and wide tracking are removed or reduced on CJK labels (e.g. tag tracking dropped; takeaway label `1pt → 0.5pt`; cover eyebrow `2pt → 1.5pt`).

## 581. Paragraph Conventions
- Chinese letters: justified text with a `2em` first-line indent on every paragraph (including the first), `14pt` apart; a no-indent class opts out.
- Korean letters: left-aligned, no indent, `14pt` apart — Korean follows Western paragraphing.
- Memo variants in all languages drop indents.

## 582. Korean Line Breaking
- Korean breaks only at spaces (`word-break: keep-all`) so a word never splits across lines; Chinese and Japanese keep normal per-character breaking.

## 583. Korean Optical Sizing
- Hangul in Source Han Serif K has a smaller optical body than the Chinese face, so Korean starts from the Chinese baseline sizes (H1 `24pt` / `1.15`) and is tuned per template.
- Korean metric labels can drop as low as `7pt` in the one-pager.

## 584. Mixed-Script Code
- Code stacks put mono first and append the CJK serif (`"JetBrains Mono", "SF Mono", Consolas, <CJK face>, monospace`) so CJK comments inside code render instead of missing-glyph boxes.
- Inline SVG diagram text declares the CJK stack explicitly inside the SVG.

# Part 71 — Showcase Site Techniques

## 585. Desktop Text Ladder
- Meta `14px`, body `15px`, lede `16px`, title `21px`, section `32px`; one variable per rung so every component pulls from the ladder.
- Hero wordmark `84px` weight `500`, line-height `1.05`, letter-spacing `-1.2px`; secondary-language glyph after it in ink blue, `16px` apart, tracking `0`.
- Hero tagline uses the title rung `21px` weight `500` olive `1.35`; CJK taglines on desktop use `20px`, the ladder's one exception.
- Eyebrow `14px` weight `500`, letter-spacing `1.2px`, uppercase, stone, `18px` below.

## 586. Phone Text Ladder
- At ≤`640px`: running text unified at `16px` (tagline, manifesto, ledes, prose, FAQ answers); secondary `15px`; meta `13px`; floor `12px`.
- Headings never smaller than the body they head (FAQ questions and subheads `16px`); section titles `24px`.
- Code sits one rung under surrounding text (`15px` in `16px` prose, `13px` in blocks).
- Text inside boxes keeps `16px` side padding.
- Tablet (≤`768px`): page padding `48px 20px 40px`, hero `64px`, grids collapse to one or two columns, fact tokens and date hidden.

## 587. Per-Language Tuning
- Language set on the root swaps the serif stack and tracking: Chinese body `0.35px`, Japanese `0.02em`, Korean and English `0`.
- English section titles track `-0.3px`; CJK section titles `0`.
- Display specimen: Latin `54px` letter-spacing `-0.5px`; Chinese `48px` `+0.5px`; Japanese `42px` line-height `1.12` `+0.3px`.
- Japanese ledes and descriptions may be held on one line at ≥`980px` widths.

## 588. Language Switcher
- Trigger `14px` weight `500` stone with a `4px` chevron drawn from two `1px` borders rotated `45°` (flips to `225°` when open), hover ink blue.
- Menu `140px` wide, ivory, `1px solid #e5e3d8`, radius `8px`, padding `5px`, soft shadow `0 8px 24px rgba(20,19,19,0.08)`, fades in over `0.16s`; an invisible `12px` bridge keeps hover alive between trigger and menu.
- Items `29px` tall, radius `6px`; hover tint is brand at `8%`, active brand at `12%` with weight `600`; focus ring `2px` brand at `38%`, offset `3px`.

## 589. Hero and Sections
- Hero `40px` padding over a `1px solid #e5e3d8` rule, `48px` below; fact tokens `14px` stone tabular with values in dark-warm.
- Sections `72px` apart; lede `16px` weight `500` olive `1.55`, `14px` above.
- Manifesto `21px` / `1.65`, letter-spacing `0.05em` (removed in English and Japanese).

## 590. Rules Ledger
- Two-column list with a centre `1px` rule and horizontal rules, `18px` padding, `32px` inner gutters; `15px` dark-warm text; inline code `14px` on `#f0eee6`.

## 591. Colour Swatches
- Four-column grid, gap `14px`; card ivory with `1px solid #dedbcf` edge, radius `8px`; chip `96px` tall above a matching rule.
- Info block padding `12px 14px 14px`: name `15px` weight `500` (brand swatch in ink blue), role `14px` olive, hex in mono stone letter-spacing `0.4px`.
- Tag tint samples shown in two columns, each tint swatched on ivory.

## 592. Type Specimen Table
- Three-column grid `220px | 1fr | 160px` with zero column gap so each row's rule runs unbroken; rows `18px` padding.
- Sample cell fills its column but is right-padded to keep running text near `540px` wide.
- Specs column right-aligned `14px` olive tabular (sizes in the text face, not mono).
- Scale shown: Display `36–48pt` / `1.10`; H1 `18–22pt` / `1.20`; H2 `14–16pt` / `1.25`; H3 `12–13pt` / `1.30`; Body `9.5–10pt` / `1.55`; Caption `8.5–9pt` / `1.45`; Label `7.5–8pt` / `1.35`; screen px = pt × `1.33`.

## 593. Font Family Cards
- Two columns gap `16px`; ivory, radius `8px`, padding `28px 24px 22px`; glyph sample `80px` weight `500` letter-spacing `-1px` (mono sample weight `400`, tracking `0`).

## 594. Spacing and Radius Specimens
- Spacing table rows `14px` padding with `1px` rules; name `15px` weight `500`, value mono `14px` olive, a `4px` stone bar at `50%` opacity showing the size.
- Radius boxes `72px` square on ivory with deep edge; radii and depth notes share one row (`72px` gap) so neither leaves half a column empty.

## 595. Component Cards
- Two-column grid gap `24px`; each card ivory, radius `8px`, padding `28px 28px 24px`, title `16px` weight `500`, hint `14px` stone `20px` below.
- Buttons specimen: `12px` weight `500`, padding `8px 14px`, radius `8px`, letter-spacing `0.4px`; primary ink fill + ivory text, secondary warm sand + dark-warm with border, ghost transparent with ink outline; no shadows.
- Tags specimen: `12px`, padding `2px 7px`, radius `2px` on `#EEF2F7` (quiet) or `2px 8px`, radius `4px` on `#E4ECF5` (default).
- Code specimen: ivory, `1px` border, radius `6px`, padding `12px 14px`, mono `14px`; document-style code on `#f0eee6` with `4pt` radius and no border.

## 596. Sample Document Thumbnails
- Four-column grid gap `20px`; thumbnails radius `8px` with deeper edge `#dedbcf` plus a whisper shadow `0 1px 3px rgba(20,19,19,0.06), 0 12px 28px -8px rgba(20,19,19,0.12)` so parchment sheets lift off the parchment page.
- Title `16px` weight `500`, `10px` above; description `14px` olive.
- Social and landing cards put name and description on one centred baseline line; images open in a zoom lightbox (`zoom-in` cursor).
- Landing showcase uses three columns.

## 597. Inline Charts
- Two-column showcase of ivory cards (radius `8px`, padding `16px 16px 12px`), label `14px` ink blue weight `500`, caption `14px` olive.
- Charts drawn on a parchment rect in a `280 × 160` viewBox with the document's own font.
- Architecture: nodes `64 × 44` radius `3`, parchment fill with `0.8` stone/olive stroke; one focal node in `#EEF2F7` with `1` ink-blue stroke; tiny `7px` uppercase category labels tracked `0.5`, node names `9px` weight `600`.
- Flowchart: start pill fully rounded (`rx 14`) in near-black with parchment text; decision diamond outlined `1px` near-black; success path and node in ink blue, rejection path muted.
- Bar chart: tonal ramp stone `#6b6a64` → olive `#504e49` → mid ink `#2d4e7a` → ink `#1B365D`, radius `3`, values above bars in matching colour weight `600`.
- Donut: 3–6 segments in ink / olive / stone separated by `1.5` white strokes; centre percentage `13px` weight `600` ink blue; legend chips `10 × 10` radius `2`.
- Sequence diagrams: participant boxes `80 × 40` radius `4` on ivory with `1` border; dashed lifelines `0.75` olive `6 4`; solid request / dashed reply arrows with small ink-blue arrowheads; labels `11px` stone.

## 598. Quick Reference Decisions
- Large headline: serif `500`, size by hierarchy, line-height `1.10–1.30`.
- Emphasise a number: ink-blue colour, not bold.
- Separate sections: whitespace first; one `0.5pt` neutral full-width hairline only when the boundary must be explicit.
- Quote: olive text, no side rule.
- Mark a special card: stronger label or subtle fill, never an accent edge.
- Primary vs secondary action: brand fill + ivory text vs warm sand + charcoal.
- Document cover: single page, display size, right-aligned author/date, generous whitespace.

## 599. Anti-Patterns
- Never pure white `#ffffff` or cool grey `#f3f4f6` as page background (except the deliberate print-white variant).
- Never translucent tag fills such as `rgba(27,54,93,0.18)`; use solid `#E4ECF5`.
- Never headings at `600+` or synthetic bold; use the real medium weight, size, spacing or ink colour for presence.
- Never hard drop shadows like `0 2px 8px rgba(0,0,0,0.3)`; they print as dark blobs.
- Layout ledger: grid `180px 1fr`, gap `40px`, `20px` rows; "Never" line in olive, "Instead" line in dark-warm with its cue in ink blue, cue column `72px`.

## 600. Footer and Prose Pages
- Footer `40px` padding over a `1px` rule; `56px` mark beside wordmark `21px` weight `500`; colophon `14px` stone, right-aligned, max `420px`, links joined by generated middots `6px` apart.
- Prose pages: hero `62px` letter-spacing `-0.6px` (`40px` on tablets); paragraphs and list items `16px` / `1.65` olive, `16px` apart; H3 `16px` weight `500`, margins `30px 0 10px`; list markers stone; links ink blue weight `500`.
- FAQ on the site: questions `16px` weight `600`, answers `15px` dark-warm `1.6`, pairs `20px` apart.

## 601. Motion and Print
- Reduced-motion preference collapses every transition and animation to `0.01ms`.
- Site print: A4 with `14mm 16mm` margins on parchment; hero shrinks to `76px`, section titles `26px`; swatches, cards, code and table rows kept whole.

# Part 72 — Print & Page Production

## 602. Page Size and Margins
- Default to `A4` portrait (`210mm 297mm`); use `A4 landscape` or `13in 10in` only when the document type calls for it. A fixed physical size keeps every page count reproducible.
- Set page margins around `20mm 22mm` (vertical, horizontal). This gives a calm, book-like frame and leaves room for running headers and folios.
- Remember that usable cover height is page height minus margins: on A4 with `20mm` top and bottom margins, a full cover is `257mm` tall.

## 603. Full-Bleed Page Background
- Paint the page background on the page box itself, not only on the body, using parchment `#f5f4ed`. A background set only on content stops at the margin and prints a white border around every page.
- Keep the html/body background equal to the page background so no seam shows between margin and content area.

## 604. White-Paper Print Variant
- Keep parchment as the default surface. Switch to white `#ffffff` only for a single document headed to a home or office printer, because a full-page warm tint bands unevenly and wastes toner.
- Treat white as an opt-in per document, never a default mode.
- When switching to white, move the warmth instead of deleting it: set page and body to `#ffffff` and let parchment `#f5f4ed` become the lifted surface for cards, code blocks and striped rows. On white, the usual ivory lift (`#faf9f5`, only about 1.5% lighter than white) disappears.
- Leave every other token unchanged: the ink-blue accent, warm text grays and the hairline border color all read correctly on white.
- Give any lifted surface that relied on fill alone a `0.5pt` border in the border color, so it keeps an edge on white.
- Re-inspect cards, code and tables on white before shipping; page-count and density expectations stay the same.

## 605. Running Headers and Footers
- Place the folio (page number) in the top-right margin box at `9pt`, serif, in stone `#6b6a64`.
- Put the document name and author in the bottom-center margin box at `9pt`, stone `#6b6a64`, joined by ` · `.
- Suppress both header and footer on the first page (cover). A folio on a cover reads as clutter.
- Drive the running header from chapter-level titles only (the H1 of each chapter), never from every H2, so a contents page cannot pin the header to "Contents".
- If chapter titles use some element other than H1, mark that element explicitly as the running-title source.

## 606. Document Metadata
- Fill title, author, description and keywords for every PDF so the file is identifiable outside its folder.
- Take the title from the H1 or the header title text.
- Set the author to the person's name for resumes, letters and portfolios; for other document types use the publishing system or organization name.
- Write the description as one sentence drawn from the first two paragraphs, at most `150` characters.
- Write `3-5` comma-separated keywords taken from the title and section headings.
- An author placeholder may remain unfilled only when the author is stamped in automatically at render time; every other placeholder must be replaced.

## 607. Features That Do Not Survive Print Rendering
- Never rely on JavaScript, `position: sticky`, CSS animations or transitions in a print document; print rendering engines ignore them.
- Use CSS filters, transforms and inline SVG attributes sparingly; support is partial.
- Use gradients sparingly; they render slowly in print and add nothing at small sizes.
- Rely freely on grid, flexbox, page rules, custom fonts, `break-before`, `break-inside: avoid`, CSS variables, `::before`/`::after`, and cross-reference page counters on block anchors.
## 608. Physical Units Instead of Viewport Units
- Never use viewport units (`100vh`, `100vw`) in print; they are undefined in the paged context and a `height: 100vh` cover renders empty. Use physical units instead (for an A4 cover, `min-height: 257mm` with a centered flex column).

## 609. Mathematics
- Render formulas as true vector math, authored strictly as inline `\( ... \)` or display `\[ ... \]` in body text.
- Never ship Unicode approximations, raw TeX, or screenshots of formulas.
- Let formulas inherit the document's text color; never set color, HTML or link commands inside the math.
- Treat unmatched delimiters or invalid TeX as a blocking error, not a cosmetic one.
- A finished document must contain no raw TeX delimiters in visible text.

## 610. Collaboration Copies (Editable Word Version)
- Treat PDF as the delivery format and an editable word-processor file as the collaboration format; ship the editable copy only for long documents, proposals and equity reports.
- Never produce an editable copy of resumes, one-pagers, slides or portfolios; they are visual artifacts and conversion only degrades them.
- Rasterize every inline vector figure to a wide PNG (about `1600px` wide) before conversion; word processors reject inline SVG.
- Expect headings, body, lists, tables, brand color on headings, bold and highlights, full-width figures and explicit page breaks to carry over. Expect grid layouts, custom positioning, subtle borders and shadows, figure editability and page margins to be lost. The goal is editability, not visual fidelity.

## 611. Standalone HTML Hand-off
- Prefer delivering the PDF; a shared HTML file is not guaranteed to render outside its original font environment.
- If HTML must be shared, keep the font file in the same folder as the HTML and reference it by bare filename, with no path prefix.

# Part 73 — Page Breaks & Pagination

## 612. Page Ceilings per Document Type
- Keep one-pagers and letters to exactly `1` page.
- Keep resumes to exactly `2` pages, never `1` and never `3`.
- Keep changelogs to at most `2` pages.
- Keep equity reports to at most `3` pages.
- Long documents target `6-15` pages; portfolios and slides have no hard page ceiling but must still pass density review.
- Re-check page count after any font change; a font fallback alone can turn `2` pages into `4`.

## 613. Hard-Limit Overflow Repair Order
- Treat content as the primary repair surface when a length-capped document overflows. First confirm the intended font actually loaded.
- Repair in this order: (1) cut redundant qualifiers ("deeply researched" becomes "researched"); (2) merge related data points within a section; (3) drop non-essential items whole, not piecemeal; (4) reduce section spacing, sparingly, since it changes global rhythm; (5) as a last resort shrink type by only `0.1-0.2pt`.
- Never cut structural blocks (cover, education, timeline) to save space.
- Never strip emphasis to save space; the page goes flat.
- Common overflow causes to rule out: font fallback, added content, an accidental font-size bump, line-height pushed from `1.4` to `1.6`.

## 614. Dense Resume Variant
- Use a dense resume variant only when content legitimately needs `5` projects and the `4`-project layout already overflows; never make it the default.
## 615. Dense Resume Values
- Dense values: body `9.2pt` becomes `9pt`; project text line-height `1.40` becomes `1.38` (Chinese) or stays `1.40` (English); timeline body `9pt` becomes `8.5pt` (Chinese only); section-title top margin `5mm` becomes `3.5mm`.
- When a resume spills to a third page, apply the dense variant or tighten project text line-height to `1.38`.

## 616. Resume Page Balance
- Fill each of the two resume pages between `83%` and `95%` of its height.
- Keep the fill difference between page 1 and page 2 at or below `12%`.
## 617. Thin Source Detection
- If both pages stay under the ceiling yet together hold less than `166%` (two times the `83%` floor), the source is too thin: list the missing material as data gaps rather than loosening layout, which only trades one sparse page for another.

## 618. Page Density
- Read body pages as `60-80%` full; the cover and the last page are exempt.
- Warn when a body page has more than `25%` trailing whitespace; treat more than `50%` as a sparse, failing page.
- Allow the last page of a multi-page document to close short, but never with more than `60%` trailing whitespace (it should typically run `40-60%` full).
- Judge single-page documents (one-pager, letter) on their only page too; they are not exempt.
- A chapter that would fill under `40%` of a page merges into its neighbor.
- Large trailing gaps usually come from a keep-together block pushed to the next page; restructure content rather than accept the hole.

## 619. Keep-Together Blocks
- Never let a heading strand at the bottom of a page, and never split a card or table mid-body.
- Keep-together does not work reliably on direct children of flex or grid containers in print; wrap each flex item in an extra plain block and apply keep-together to the wrapper.

## 620. Orphan Lines
- Never end a multi-line text block with a trailing line of `2` words or fewer that is also under `15` characters.
- On social cards, never end a paragraph on `1-3` CJK characters or a single Latin word.
- Fix a short last line with layout (for example right padding on the text box), never by rewording the author's text.

## 621. Table of Contents Page Numbers
- Generate TOC page numbers from the link target at render time, never by hand, so content edits never stale them.
- Keep every TOC entry a link to a stable chapter id.
- Keep the TOC anchor a block element and float the numeral right; never make the anchor itself a flex container, which in some print engines resolves every number to `0` while still printing a well-formed digit.
- Prefer `float: right` over `margin-left: auto` for right-aligned numerals and badges; it is stable across engine versions.
- Verify each rendered TOC numeral against the page its row actually links to; a `0` or a mismatch is a blocking error.

## 622. Rule Placement at Breaks
- Use section-title bottom rules and borderless project rows in resumes; never add a top border to each project as a density aid. It creates double rules under headings and orphan rules at page breaks.

# Part 74 — Fonts & Fallbacks

## 623. One Serif per Page
- Use a single serif family for the whole page, including headings and UI-like labels; sans is set to the same serif. Mixed families break the page texture.
- One page carries one serif: CJK text split across two families is a defect, not a style.

## 624. Primary Families
- Use Charter for English, TsangerJinKai02 for Chinese, and Source Han Serif K for Korean as primary faces.
- For Japanese, use a Mincho face (YuMincho, Hiragino Mincho, Noto Serif CJK JP, Source Han Serif JP).
- A healthy render shows Charter, Georgia, TsangerJinKai02 or a Japanese Mincho in the embedded fonts; DejaVu Serif or Bitstream Vera means the specified font did not load and the system's last-resort face took over.

## 625. Fallback Stacks
- English: `Charter, Georgia, Palatino, "Times New Roman", serif`.
- Chinese: `"TsangerJinKai02", "Source Han Serif SC", "Source Han Serif CN", "Noto Serif CJK SC", "Noto Serif SC", "Songti SC", "STSong", "SimSun", Georgia, serif`.
- Japanese: `"YuMincho", "Yu Mincho", "Hiragino Mincho ProN", "Noto Serif CJK JP", "Source Han Serif JP", "TsangerJinKai02", Georgia, serif`.
- Korean: `"Source Han Serif K", "Source Han Serif KR", "Noto Serif KR", "Nanum Myeongjo", AppleMyungjo, "Apple SD Gothic Neo", Charter, Georgia, serif`.
- Slide decks in presentation software: `Charter`, then `Georgia`, then `Palatino`, with sans identical to serif.

## 626. Serif Fallback vs Sans Substitution
- Accept a CJK serif fallback (Source Han Serif, Noto Serif CJK, Songti, STSong, SimSun, Kaiti, Ming, Hiragino Mincho, YuMincho, Myeongjo, Batang) as a degradation: the page keeps the serif texture the metrics were tuned for, but it is not the reference rendering.
- Never accept a sans substitution for CJK body text. Sizes, tracking and leading are tuned for serif stroke density; a sans reads heavier and flatter at the same size and produces no fallback boxes to warn you.
- Judge the font by which family actually drew the body text, not by the embedded font list; a document can embed a serif for two glyphs and a sans for three thousand.
- Only judge CJK font usage once there are at least `20` ideographs; a stray glyph proves nothing.
## 627. Mixed-Family Threshold
- Treat a second CJK family as a split when it draws at least `3` characters and at least `5%` of the CJK text.
- Count bold and weight variants (Regular, Medium, W04/W05, numeric weights) as the same family, not as a second typeface.

## 628. Font Loading Reliability
- Keep font files next to the HTML and reference them by relative path; this is the most stable setup.
- Keep a remote font URL as a fallback alongside the local source, so online renders still load the face.
- Every locally referenced font source must exist on disk before rendering; a missing file silently triggers fallback and page-count drift.
- If output overflows, first confirm the intended font loaded before editing content.

## 629. Presentation Software Fonts
- A generated deck is only done when the intended serif remains present after opening or exporting, with no silent substitution to the presentation software's default sans (for example Calibri or Aptos).
- Never use the presentation software's default template; its cool blue-gray clashes with parchment.

## 630. Fonts in Inline Vector Figures
- In SVG text, put CJK families first and let Latin faces trail (`"TsangerJinKai02", "Source Han Serif SC", "Songti SC", Charter, Georgia, serif`).
- Never lead an SVG text stack with a Latin serif when labels contain CJK: the stack walk stops at the Latin face and each ideograph falls back per glyph, splitting one label across two typefaces mid-word.
- Never pull in a runtime web font (for example a hosted web-font stylesheet) inside a print figure.

# Part 75 — CJK Rendering

## 631. Korean Word Breaking
- Break Korean lines between words (eojeol), never inside a word ("파이프라 / 인을", "pipeli / ne").
- Print engines may ignore `word-break: keep-all`, so word wholeness must be enforced in the rendered copy with invisible word joiners, never by editing the source.
- Never add joiners or a span around every word in the source HTML; it makes the source unreadable.
- Let Korean words longer than `16` characters remain breakable, so long compounds in narrow table cells wrap instead of overflowing.
- Keep words whole across inline formatting (highlights, bold, links) as well as plain text.
- Expect word-level breaking to fill lines less tightly; a Korean document near its page ceiling may need a line or two trimmed.

## 632. Korean Glyph Visibility
- Use TrueType-outline Korean fonts for PDF output; a CID-keyed CFF build of the Korean serif subsets into a PDF that some viewers draw blank (Latin and folios visible, Korean missing).
- Never prove Korean visibility with text extraction or the embedded font list alone; check the page in more than one PDF viewer, since one may draw the broken file correctly.
- Avoid embedding full, unsubsetted fonts as a fix; it costs about `7 MB` per weight.

## 633. CJK and Latin Spacing
- Separate a number and a Latin label in Chinese text into two spans and let a flex `gap` (about `6pt`) carry the space ("125.4k GitHub Stars").
- Never fix CJK/Latin crowding with hand-typed non-breaking spaces or ad hoc margins; they misalign neighbors.
- Between Chinese characters, use a full-width space (U+3000) around a `·` separator; between Latin words use half-width spaces around `·`. For mixed runs prefer flex gap over typed spaces.

## 634. CJK Line Height
- Never set title line-height below `1.3` at slide sizes; CJK characters collide below it.
- CJK screen copy may run to `1.65` line-height; print body copy stays at or below `1.55`.

## 635. CJK Punctuation at Slide Scale
- Use ` - ` for short joins and an ordered list for parallel items on slides; CJK commas break the visual rhythm at large sizes.

## 636. CJK Bold
- Use a real bold or medium weight for CJK emphasis, never synthetic bold.

# Part 76 — Image & Figure Handling

## 637. Image Resolution
- Supply raster images at `2x` or `3x` their printed size; print renders at source pixel density, and a full A4 page at `300 dpi` needs `2480 × 3508` pixels.

## 638. Asset Paths
- Every image must live inside the document's own asset folder and be referenced by a relative path within it.
- Never reference images through paths that climb out of the project, absolute user paths (`/Users/...`) or `file://` URLs; they work on one machine and break everywhere else.

## 639. Real Imagery Only
- Use real screenshots and photos of the actual product, person or work; never stock images, mocked interfaces or unrelated imagery.
- When a required image is missing, mark the gap clearly rather than substituting something else.
- Branded documents should include logo, product image or UI screenshot coverage.

## 640. Slide Images
- Size slide images with `width: 100%; object-fit: contain; max-height: 780px`; never a fixed height that clips images of different aspect ratios.

## 641. Figure Width Starvation
- Give every inline figure SVG `width: 100%; height: auto` and use `max-height` (around `70mm`) only as a safety ceiling, never as the primary sizing rule.
- Check that viewBox aspect ratio × max-height ≥ content width; if not, the figure shrinks and leaves a visible gap beside full-width titles and tables. Raise or remove the cap.

## 642. Arrowheads in Figures
- Never rely on SVG marker auto-orientation for arrowheads; print renderers draw every marker at `0°`, so all arrows point right.
- Draw each arrowhead as a manual chevron path at the endpoint with an `8px` arm and hard-coded direction (for a downward tip at x,y: from `(x-8, y-8)` to `(x, y)` to `(x+8, y-8)`), round caps and joins, stroke `1.5` in olive `#504e49`.
- Arrows never touch module edges, arrowheads must stay visible, and labels must never overlap.

## 643. Figures from Diagram Generators
- Never embed un-normalized generated diagram SVG in a print document: color-mixing functions do not resolve, foreign-object HTML does not render, and runtime web fonts do not load. Normalize it first.
- Keep inline figure colors to the warm-gray chart ramp and the brand accent.

## 644. Figures per Page and Captions
- Limit long documents to at most one figure per body page.
- Write captions that state the insight, not the data range.

## 645. Social Card Imagery
- Keep text at least `24px` clear of a photo's top edge and never set text on the photo.
- The cover card carries a real photo or screenshot.

## 646. Product Site Imagery
- Use stable aspect ratios for hero, gallery, feature and social-image slots.
- Never crop away UI text, numbers, prompts or controls for aesthetics.

# Part 77 — Enforced Typography Rules

## 647. Line-Height Ceilings
- Keep print line-height at or below `1.55`.
- Allow CJK screen pages up to `1.65`; English screen pages still stop at `1.55`.
- Allow social cards (phone images read at `42-44px` body) up to `1.8`; their body is set at `1.68-1.75`.
- Print titles sit at `1.1-1.3`; slide titles at least `1.3`.

## 648. Print vs Slide Type Scale
- Print display titles run `30-34pt`; slide titles run `48-64pt`.
- Slide type roles: title `48pt` serif 500; subtitle `24pt` 400; chapter H2 `32pt` 500; H3 `20pt` 500; body `18pt` 400; caption `14pt` 400; footer `12pt` 400.
- Resume body sits at `9.2pt` by default.

## 649. Letter-Spacing and Tracking
- Track print eyebrows at `0.5-1pt`; cap slide eyebrow tracking at `3px`.
- Halve print letter-spacing values on slides (for example `6px` becomes `3px`); large sizes multiply absolute tracking until text looks scattered. Monospace text is exempt.
- Tighten display titles: `0` to `-0.2pt` in print, about `-0.5pt` on slides, to prevent letter gaps.

## 650. Slide Scaling Rule
- Scale macro spacing by `×1.6` and micro details (letter-spacing, border weight, border radius) by `×0.5` when moving a design from print to slides.

## 651. Emphasis Rhythm
- Reserve brand-color emphasis for numbers and distinctive phrases only.
- Use at most `2` emphasized runs per line; four or five ink-blue runs in a line cause fatigue.
- Give long prose sections at least one scan handle; a section with zero emphasis is as wrong as one with too much.
- Give every resume skill line at least one emphasis-worthy number or distinctive phrase.

## 652. Banned Punctuation and Residue
- Never use the em dash in any deliverable.
## 653. Arrows and Number Formatting
- Never use the Unicode right arrow `→` in English body copy; write "to" or `->`.
- Use one arrow glyph, one thousands-separator style and one percent style consistently throughout a document.
## 654. No Markup Residue or Placeholders
- Never let raw Markdown leak into visible output: no literal three-hyphen thematic breaks, no `**` bold markers, no inline-code backticks.
- Never leave an unfilled `{{PLACEHOLDER}}` in delivered text.

## 655. List Markers
- On slides, use short numerals (`1.`, `2.`, `3.`) in brand color with tabular figures and weight `500`, or a brand-colored `•`; never en-dash markers, which read heavy and informal at slide size.
- Print documents keep the editorial en-dash list style.

## 656. Wrapping Quality
- Avoid lines one word from wrapping and lines that wrap early before filling their container.

# Part 78 — Enforced Layout Rules

## 657. Body Text Width
- Let section body copy fill the page container; never apply a generic article-style `max-width` that turns body copy into a narrow inset column.
- Constrain width only for type specimens and the closing colophon.

## 658. Metric Rows
- Stack metric value and label vertically (column direction) whenever any label can wrap, so all numbers share a top edge and all labels start on one line below.
- Use inline baseline alignment only when every label in the row is a fixed, short, single-line string.
- On slides and screen pages, always stack metrics; one wrapped label among three columns breaks the rhythm.

## 659. Metric Label Budgets
- Compute each column as `(content width − gap × (N−1)) / N` and plan labels against what remains after the value (a value at `14pt` takes about `12-18mm`).
- At `9pt` with `184mm` content: `4` columns at `7mm` gap give about `40.7mm` per column, `22-26mm` for the label, `14-18` characters.
- `3` columns at `7mm` gap give about `56.7mm`, `38-42mm` for the label, `24-28` characters.
- `4` columns at `5mm` gap give about `42.7mm`, `24-28mm` for the label, `16-20` characters.
- Trim long labels to the data essential; put supporting context in nearby body copy, not in the metric chip.

## 660. Parallel Column Balance
- Hold body length within `±10` characters across parallel columns of the same width, so all wrap to the same number of lines.
- Rewrite the longest column tighter rather than padding the shorter ones.

## 661. Grid Spanning in Print
- Span grid items by count (`span 2`) or positive lines (`1 / 3`); never negative line numbers (`1 / -1`), which print engines silently drop.
- Let a lone item in a two-column grid span both columns.

## 662. Rounded Borders
- Never combine a closed border thinner than `1pt` with a border radius; print engines stroke inner and outer paths separately and show two parallel arcs.
- Fix by using a background fill instead (preferred), a border of at least `1pt`, or no radius.

## 663. Emphasis Containers
- Raise passages one way per document: every filled, padded, rounded emphasis block uses the same fill color.
- Never invent a new container style per idea (a white card here, a tinted block there); two or more distinct emphasis fills is drift.
- Chips, tags, badges and code blocks are components, not emphasis containers, and are exempt.

## 664. Subtraction
- Never add decorative ticks, short rules or side accents; every visible rule must separate data, regions, relationships or state.

## 665. Tables
- Use one neutral rule color, hairline dividers, and enough vertical padding for each row to breathe.

## 666. Alignment
- Columns share baselines, margins stay even, and nothing crowds the page edge.

## 667. Slide Container and Safe Zone
- Use a fixed slide ratio: `1920×1080` or A4 landscape; never `100vw × 100vh`.
## 668. Slide Dimensions and Safe Zone
- Use `16:9` widescreen (`13.33 × 7.5in`) by preference, `4:3` (`10 × 7.5in`) otherwise.
- Keep content inside a `0.5in` safe zone on all sides, plus `0.3in` extra at the bottom for the page number.
## 669. Slide Padding and Header Gap
- Pad slides `72-80px` at the top and `80px` at the sides; under `72px` top feels cramped.
- Leave at least `36px` between a header rule and the H1 on slides; less makes the rule read as an underline. In print the header gap is `8-14pt`.

## 670. Slide Content Discipline
- Put one idea per slide; if a point runs past three lines, split the slide.
- Show slide code as pseudocode with highlighted keywords; full runnable code belongs in print.
## 671. Slide Footer, Motion and Pagination
- Use one footer component with injected text across the deck to prevent drift.
- Use no animations by default; when motion carries meaning, use fade only.
- Show all pipeline steps at once; never click-reveal.
- Show page numbers once per slide; never both a pinned page-number element and automatic pagination.

## 672. Deck Rhythm
- Never run more than `5` consecutive content slides.
- Give decks of `12` or more slides at least one chapter divider, ideally every `4-6` slides.
- Include at least one quote or metrics slide in every deck for density variation.
- Make the chapter divider the only fully chromatic slide: full ink-blue background with a centered white title.

## 673. Standard Slide Layouts
- Cover: parchment, centered display title, short brand-colored line, subtitle, author, date.
- Contents: left-aligned numbered chapters (`01  Chapter title`), numerals serif in brand color.
- Content: stone eyebrow, near-black core claim, brand line, dark-warm body.
- Data: top takeaway plus `2-4` metric cards (big brand-colored serif number, small olive label).
- Comparison: muted left column (before/old/problem) vs full-weight right column (after/new/solution), split by a `1pt` warm-gray divider.
- Pipeline: numbered `01/02/03` steps in equal-width columns.
- Quote: minimal parchment, centered serif quote with source.
- Closing: parchment, centered thanks, Q&A or contact.

## 674. Social Card Layout
- Keep at least `40px` between the lowest content and the footer rule; never let text run under the footer.
- Never let a card spill onto a second page; split a crowded card instead of shrinking its type.
- Give each card one point (text card) or `2-5` items (list card), similar weight across the set, each card mostly full of the author's text, not padding.

# Part 79 — Visibility & Overflow

## 675. Everything Required Must Be Visibly Rendered
- Content counts as present only if a reader can see it; hidden text never satisfies a content requirement.
- Treat as hidden: `display: none`, `visibility: hidden` or `collapse`, `opacity: 0`, `font-size: 0`, `color: transparent`, the `hidden` attribute, and `aria-hidden="true"`.
## 676. Hidden by Transform or Filter
- Treat as hidden: zero scale or zero matrix transforms, translations beyond about `-2000` units, `scale` or `zoom` of `0`, `content-visibility: hidden`, and `filter: opacity(0)`.
## 677. Hidden by Offset or Clipping
- Treat as hidden: offsets or text-indent of `100%`/`100em`/`100rem` or more, or `2000` absolute units or more.
- Treat as hidden: `clip: rect(0,0,0,0)`, `clip-path: inset(50%)`, `inset(100%)` or `circle(0)`.
## 678. Hidden by Zero Size
- Treat as hidden: zero width or height on images and other replaced elements, or on any box with overflow hidden or clipped.
## 679. Hidden SVG Content
- Treat as hidden: SVG shapes with `fill="none"` or `fill-opacity: 0`, and SVG elements positioned entirely outside their viewBox.

## 680. Ambiguous Visibility Fails Closed
- Avoid styling that makes visibility undecidable: conditional rules (media, supports or container queries), masks, clip paths, URL filters, unresolved custom properties, external or imported stylesheets, and complex selectors (sibling or attribute-substring combinators).
## 681. Unprovable Figure Text
- Never place required facts in SVG text, nested SVG viewports or offset SVG text; their visibility cannot be proven without rendering, so they do not count as evidence.
- Keep custom properties used for visibility defined once, unconditionally, on the root.
- Close tags properly; malformed nesting makes the whole document's visibility ambiguous.

## 682. Overflow and Cropping
- No text may overflow, crop, overlap or break across a page in a way the reader notices.
- In presentation output, nothing may overflow the safe zone and page numbers must stay intact.
- Long CJK compounds in narrow cells must wrap rather than overflow.

## 683. Raw Markup Leakage
- Any copy that could plausibly be visible is scanned for raw Markdown markers; text inside code, preformatted and monospace runs is exempt.

## 684. Screen Motion
- Gallery rotation, entrance animations and custom transitions must respect reduced-motion preferences, and the page must remain readable with motion disabled.

# Part 80 — Color & Contrast

## 685. Single-Accent Palette
- Use one chromatic accent, ink blue `#1B365D`, plus warm neutrals, and zero cool tones.
- Every color used must be a registered palette token; any other hex is an off-palette violation, including one defined as a root token and never used.
- Palette: parchment `#f5f4ed`, ivory `#faf9f5`, inline-code background `#f0eee6`, border `#e8e6dc`, soft border `#e5e3d8`, line `#d8d5c8`, brand `#1B365D`, brand tint `#EEF2F7`, tag background `#E4ECF5`, near-black `#141413`, dark-warm `#3d3d3a`, charcoal `#4d4c48`, olive `#504e49`, stone `#6b6a64`.
## 686. Sanctioned Exceptions to the Palette
- The single sanctioned semantic exception is the breaking-change badge: background `#f0e0d8`, text `#8b4513`.
- Pure white `#ffffff` is allowed only in the white-paper print variant.

## 687. Text Color Roles
- Use near-black for core claims, dark-warm for body, olive and stone for labels and muted text, stone for eyebrows, headers and footers.

## 688. Banned Cool Grays
- Never use neutral or cool grays: `#111`, `#222`, `#333`, `#444`, `#555`, `#666`, `#777`, `#888`, `#999`, `#aaa`, `#bbb`, `#ccc`, `#ddd`, `#eee` (and their six-digit forms).
- Never use Tailwind-style cool grays (`#6b7280`, `#9ca3af`, `#d1d5db`, `#e5e7eb`, `#f3f4f6`, `#4b5563`, `#374151`, `#1f2937`, `#111827`).
- Never use Bootstrap-style neutrals (`#f8f9fa`, `#e9ecef`, `#dee2e6`, `#ced4da`, `#adb5bd`, `#6c757d`, `#495057`, `#343a40`, `#212529`).

## 689. Solid Fills Only in Print
- Never use semi-transparent (rgba) backgrounds in print, directly or via a variable that resolves to rgba; print renderers composite the padding and glyph areas separately and draw a double rectangle on tags.
## 690. Solid Borders
- Never use rgba on borders; borders are solid colors.
## 691. Tag and Badge Tints
- Give tags and badges a solid hex fill from one of two registered tints: tag background `#E4ECF5` or brand tint `#EEF2F7`. Any new tint must be registered first.
- Avoid gradient textures on tags; solid is always the answer at tag size.
- Screen-only pages may use alpha gradients, since they never pass through a print renderer.

## 692. Cross-Locale Consistency
- Keep every color and spacing token identical across language variants of the same document; only font-stack tokens may differ per locale.

## 693. Social Card Papers
- Social cards may use only their own registered papers, each with exactly one background, one text color, one accent, one muted color and one footer rule.
- Papers: parchment (`#f5f4ed` bg, `#141413` text, `#1B365D` accent, `#6b6a64` muted, `#d1d0ca` line); ink (`#1B365D`, `#f3f1e8`, `#b9c6d8`, `#8e9db3`, `#3e5473`); olive (`#2b3326`, `#ece8da`, `#bdb38c`, `#9a9883`, `#4a5043`); espresso (`#3a2a20`, `#f2e9dc`, `#d9b48a`, `#a8957f`, `#57493e`); pine (`#1c3a29`, `#eef0e6`, `#b5cfa4`, `#8fa593`, `#3e5747`); teal (`#134857`, `#eef2ef`, `#a8d0cf`, `#8fb0b4`, `#36636f`); crimson (`#5a1f17`, `#f4ebe2`, `#e6bca6`, `#bd968a`, `#734037`); char (`#1e1d1b`, `#f2f0ea`, `#d4c4a0`, `#a8a49a`, `#403f3c`).
## 694. Social Paper Contrast
- Mix the footer rule as text color at `16%` into the background.
- Hold contrast on each paper: text at least `8.8:1`, accent at least `6:1`, muted at least `4.3:1`, and use muted only at `28px` or larger.
- Keep social papers out of every other document type.

## 695. Figure and Diagram Colors
- Theme generated diagrams from the same tokens: background parchment, text near-black, lines olive, accent brand, muted stone, surface ivory, border the border token.

# Part 81 — Document Anatomy by Type

## 696. Resume
- Exactly `2` A4 pages; every bullet states an action, honest scope and a concrete result, verb-led, with verified metrics and honest ownership.
- Required: name (`≤40` chars), contact (`4-160`), summary, metrics, projects, skills, education; optional title (`≤60`).
- Summary: about `50` English words or `80` Chinese characters (`30-400` chars).
- Metrics: exactly `4` cards (one on time, one on scale, two on quantified results); value `≤16` chars, label `≤40`.
- Timeline: exactly `3` steps showing long-range evolution; period `2-30` chars, milestone `4-80`.
- Projects: `3-5` core projects; name `2-60`, role `4-160`, `2-4` verb-led actions of `10-220` chars, impact `10-260` stated as an outcome, never a restated process; rows must not repeat each other.
- Public work: up to `6` items (`6-200` chars), each with a number where possible.
- Skills: exactly `5`, each `4-160` chars with an emphasis-worthy number or phrase.
- Education: `1-3` entries.

## 697. One-Pager
- Exactly `1` page; reader grasps the point in `30` seconds; length `200-350` English words or `400-600` Chinese characters; no opening ceremony.
- Required: title (`2-60`), subtitle (`2-120`), metrics, argument, evidence, next step (`4-160`); optional contact (`≤120`).
- Metrics: `3-4` cards, numbers first; value `≤16`, label `≤40`. Metrics are the headline; if the cards do not tell the story, the metrics are wrong.
- Argument: `1-2` paragraphs (`≥40` chars), lead sentence carries the sharpest claim, not context.
- Evidence: `3-5` bullets (`10-220`), each fact + number + so-what, never a restated argument.

## 698. Letter
- Exactly `1` page, never more. First paragraph states the purpose in one sentence; the last states the specific ask or next step; everything between is evidence, one point per paragraph.
- Required: sender (`2-160`), date, recipient (`2-160`), salutation (`2-60`), paragraphs, sign-off, signature (`≤60`); optional subject (`≤80`) and up to `5` enclosures.
- Paragraphs: `3-5`, each at least `40` characters; tone follows use (resignation grateful and clear, recommendation specific and enthusiastic, proposal value-first and concrete).
- Sign-off matches formality: "Sincerely" (formal), "Best regards" (professional-warm), or the Chinese equivalents of "With respectful regards" and "Wishing you business prosperity" (`2-40` chars).

## 699. Long Document
- `6-15` pages; every chapter opens with a claim paragraph that survives the so-what test; factual claims carry sources, examples or measurements.
- Required: title (`2-80`), author, date, summary, chapters; optional subtitle (`≤120`) and up to `30` references (`4-240`).
- Executive summary: at most one page, a claim of at least `60` chars plus `3-5` takeaways (`10-220`).
- Chapters: `3-10`, each a standalone mini-essay (claim, evidence, conclusion) with a `2-3` sentence claim (`≥40` chars) and at least `2` paragraphs (`≥60` chars each).
- At most one figure per chapter/body page, caption `6-200` chars stating the insight.

## 700. Portfolio
- Open every case study with the problem and its stakes, never with your role; `3-5` deep case studies beat many shallow ones.
- Required: name (`≤40`), positioning (`6-100`, one line on the cover), contact, about (`≥60`, two or three lines under the positioning), projects.
- Projects: `3-5`, each with title, kind, period, description (`10-160`), exact role and scope, a challenge (`≥20`), `2-3` decision points with tradeoffs, and `3-5` outcomes (`10-220`) backed by verified metrics or concrete evidence; state unresolved limits honestly.
- Up to `3` real images per project; up to `8` "more works" lines.
- Keep the About page out unless there is enough material to fill a page.

## 701. Equity Report
- At most `3` pages; lead with the variant perception and tie every thesis driver to a measurable financial impact; professional register ("we estimate"), never hype.
- Required: company, rating, thesis, valuation, catalysts, risks; optional ticker (`≤16`) and price target.
- Thesis: `3-5` drivers (`20-260`) above the fold on page 1, each backed by a number or source.
- Valuation: `2-4` methods, each with result and sensitivity range; single-method valuation is amateur.
- Catalysts: `1-6`, each with event, date and expected magnitude.
- Risks: `2-6`, quantified and tied to the model, acknowledging counter-arguments.
- Financials: up to `12` rows of up to `6` values; separate GAAP from non-GAAP and flag one-time items.
- Metric labels are fixed short strings, so inline baseline alignment is acceptable here.

## 702. Changelog
- At most `2` pages; one sentence per change, verb-led, user-facing language, no internal jargon.
- Product name `≤60`; `1-10` versions, each with version (`≤30`) and date.
- Breaking changes always first, `1-4` per version, each naming the change and its migration path (`6-200` chars each), using the breaking-change badge colors.
- Features and fixes: up to `8` each (`6-200` chars); aim for `4-8` entries per version; a version with fewer than `4` shares a page with the prior version.

## 703. Slide Deck
- Ghost-deck test: reading only the titles in order tells the full argument; every title is a full declarative assertion, unique to its slide, never a topic label (`2-110` chars).
- Required: title, audience (who and venue: keynote, investor one-on-one, async link), slides; `5-40` slides.
- Layouts: cover, chapter, content, quote, metrics, close.
- Eyebrow (`≤40`) is a stable cross-slide section label and never restates the title.
- Items: `3-5` per slide, each one line (`≤110`); a slide with fewer than `3` items and no chart merges into a neighbor.
- One evidence shape per slide; a chart carries an insight line (`6-160`).
- Cap (`≤200`) says why the slide matters (tradeoff, boundary, next step) and never restates the title or diagram.

## 704. Landing Page
- A conversion surface, not a brochure; name the real product category in the first viewport.
- Required: category, product name (`≤40`), tagline (one sentence, `6-80`), facts, CTA, gallery, features, FAQ.
- Facts: `3-6` scannable proof tokens (`≤40`), no adjectives ("$9 lifetime" beats "Affordable pricing").
- CTA: one secondary (try, ghost button) and one primary (buy, filled); never three buttons.
- Gallery: `3-6` real screenshots of shipped states; captions only when they add context.
- Features: `3-8`, named directly, `2-3` sentence result description (`20-400`).
- Principles: `4-6`, title is the commitment, description the proof.
- Pricing: `4-6` one-line benefits of similar length lead; the price states itself once at medium weight; the CTA carries the action, never the price; compare honestly with up to `4` named competitors.
- FAQ: `6-8` questions, the first positioning against known tools, answers in `1-2` sentences.
- The first viewport shows category, a real asset, the CTA and a hint of the next section, on desktop and at `375px` mobile.

## 705. Social Card Set
- Fixed `1242×1660` pages; up to `18` cards for long-form platforms; at most `4` cards for short-form platforms, with headline and key evidence inside the central `1242×1242` crop.
- The cover headline is the post title word for word (`2-60` chars), and every footer repeats it unchanged.
- Heading `≤40`; `1-3` paragraphs or `1-5` items per card; use the author's text as written.

# Part 82 — Final Verification Checklist

## 706. Verification Is Part of Done
- A successful render is not delivery evidence; not verified means not done.
- Rasterize every page and look at each image before shipping (about `110 dpi` for review, `160 dpi` standard, `300 dpi` for detail, `400 dpi` to catch tag double rectangles).

## 707. Five-Point Pre-Ship Review
- Facts: numbers, dates, versions, funding, specs and market facts are sourced; uncertainty is written as magnitude or marked missing.
- Structure: headlines read as a summary, each paragraph opens with a claim, no ceremonial filler.
- Materials: required logos, product images or screenshots are present, or clearly marked missing.
- Typography: fonts loaded, line-height in spec, emphasis only on numbers or distinctive phrases, tag fills solid.
- PDF readiness: page count fits, placeholders replaced, no overflow, overlap or broken page breaks.

## 708. Page-by-Page Visual Checklist
- Fonts: no fallback boxes or mixed families; CJK bold is a real weight.
- Tags and chips: solid backgrounds, no double rectangles or double rings.
- Figures: no overlapping labels, arrows clear of module edges, arrowheads visible.
- Page breaks: no stranded headings, no split cards or tables.
- Emphasis: brand color only on numbers or distinctive phrases, at most `2` per line.
- Density: body pages `60-80%` full, no orphan trailing line.
- Wraps, alignment, tables and subtraction as defined above.
- For social cards, replace the density and page-break items with the card-fill rule.

## 709. Product Site Pre-Ship Review
- Preview on desktop and `375px` mobile.
- Generated multi-locale pages fail on missing keys or drift; for three or more locales prefer generated pages over hand edits.
- Canonical, alternate-language links, locale, social image, structured data, robots, sitemap and machine-readable summaries reflect the shipped locale set.
- Positioning, price, version, install path, support link and FAQ carry identical facts in every locale.
- Every CTA, download, release, docs, help, social and locale link resolves.
