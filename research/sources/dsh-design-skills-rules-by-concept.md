# Design Rules by Concept

Distilled from the DSH Design Skills — ten executable style specs (tokens, component rules, forbidden lists, acceptance checklists) for keeping generated websites free of the "AI look", plus techniques measured from a full landing page built in each style.

# Part 1 — Escaping the "AI Look" with Executable Style Specs

## 1. Why Generated Sites Look Generic
- Models know how to build a site; what they lack is how to make it look good. The cure is a committed aesthetic expressed as rules, not adjectives.
- Every style should be specified as four things: exact tokens, component rules, a forbidden list, and an acceptance checklist checked after implementation.
- Pick one style per product and follow it completely; mixing styles (glass + brutalist, neumorphic + hard borders) is a primary source of slop.
- Route the request to the style that fits the product: dark developer tools → Dark SaaS; premium product marketing → Minimal White; lifestyle/personal demos → Soft UI; experimental/indie → Brutalism; AI/SaaS marketing → Glassmorphism; culture/editorial → Japanese Minimal; feature walls → Bento Grid; tech/games → Cyberpunk; music/art → Vaporwave; luxury → Art Deco.
- If the user asks for dark within a light-only style, route to a dark style rather than inventing a dark variant.

## 2. Rules Shared Across the Ten Styles
- One accent colour per site (sometimes one plus a secondary); accent never decorative.
- Use a near-black or near-white rather than pure `#000`/`#fff` except where the style is defined by pure contrast (Brutalism).
- Lock a radius range per style and never drift outside it (`0` for Brutalism, `≤4px` Art Deco, `8–12px` Dark SaaS, `≥16px` Bento and Soft UI, `20px` Glass).
- Lock the shadow philosophy per style: none/faint (Dark SaaS, Japanese), soft large-radius (Glass, Minimal White), hard offset no blur (Brutalism), dual light/dark (Soft UI), glow (Cyberpunk, Vaporwave).
- Cap the proportion of the signature effect: glass `≤60%` of area, raised neumorphic elements `≤40%` of visible elements, gold `<15%` in Art Deco, vermilion in `≤2` places in Japanese Minimal.
- Validate against the checklist line by line once the build is finished.

## 3. The Big AI-Look Tells These Specs Ban
- Large purple/blue gradient backgrounds (except in styles where a gradient is the defining base).
- Rainbow or multi-accent palettes.
- Default framework cool greys in place of designed surface colours.
- Heavy drop shadows and glassmorphism applied without being asked.
- Oversized rounded cards (`>16px`) in technical products.
- Bold `700` headlines everywhere; system-default font stacks with no typographic intent.

# Part 2 — Dark SaaS (Linear-Inspired)

## 4. Dark SaaS — Principles
- Use for developer tools, data dashboards, AI products, SaaS admin.
- Near-black canvas, not pure black: `#010102` (slightly blue-black); pure `#000000` makes the interface feel dull and heavy.
- One saturated accent (e.g. lavender-blue `#5e6ad2`) appearing only on the brand mark, focus rings and primary CTAs; never decorative.
- Hierarchy comes from stepped surface colours (surface-1 → surface-4) and 1px hairlines, not from borders or shadows.
- Text is the hero: graded light greys; body at least weight `400`, `13–14px`; headings `500–600` with negative tracking.
- Density reads like technical documentation, compact and information-rich, not loose marketing whitespace.

## 5. Dark SaaS — Surface and Ink Tokens
- Canvas `#010102`; surface-1 `#0f1011` (cards, panels); surface-2 `#141516` (popovers, groups, hover); surface-3 `#18191a` (secondary hover); surface-4 `#191a1b` (selected).
- Hairline `#23252a` (default 1px divider); hairline-strong `#34343a`; hairline-tertiary `#3e3e44`.
- Ink `#f7f8f8`; ink-muted `#d0d6e0`; ink-subtle `#8a8f98` (captions); ink-tertiary `#62666d` (placeholders, disabled).

## 6. Dark SaaS — Accent and Semantic Tokens
- Primary `#5e6ad2`; primary-hover `#828fff`; primary-focus `#5e69d1`; on-primary `#ffffff`.
- Success `#27a644`; danger `#e5484d`; a muted secure/trust accent `#7a7fad`.
- Light mode must be implemented symmetrically with an inverse set: inverse-canvas `#ffffff`, inverse-surface-1 `#f5f6f6`, inverse-ink `#000000`.

## 7. Dark SaaS — Type Scale
- Display/headline (Inter-class display face): display-xl `80px/600/1.05/-3.0px`; display-lg `56px/600/1.10/-1.8px`; display-md `40px/600/1.15/-1.0px`; headline `28px/600/1.20/-0.6px`; card-title `22px/500/1.25/-0.4px`; subhead `20px/400/1.40/-0.2px`.
- Body: body-lg `18px/400/1.50/-0.1px`; body `16px/400/1.50/-0.05px`; body-sm `14px/400/1.50/0`; caption `12px/400/1.40/0`; button `14px/500/1.20/0`.
- Eyebrow `13px/500/1.30/+0.4px`: the only positive tracking, reserved for small labels.
- Mono `13px/400/1.50` for code, numbers and API endpoints.
- The bigger the heading, the more negative the tracking.
- Prefer `Inter` / `Manrope` with an `-apple-system` fallback to avoid the default-stack AI look.

## 8. Dark SaaS — Radius, Shadow, Focus
- Card radius `8–12px` (avoid `>16px`); button radius `8px`.
- Default: no shadow; only elevated/floating states get a faint one like `0 4px 12px rgba(0,0,0,.3)`.
- Focus ring `box-shadow: 0 0 0 2px rgba(94,106,210,.4)` (2px primary at 40%).

## 9. Dark SaaS — Components
- Card: surface-1 background, `1px` hairline border, radius `8–12px`, no or faint shadow.
- Primary button: primary background, primary-hover on hover, radius `8px`, weight `500`.
- Secondary button: transparent, 1px hairline border, ink text; surface-2 on hover.
- Input: surface-1 background, hairline border, `2px` primary/40% ring on focus.
- Nav: 1px hairline divider at top; logo + product name left; feature links `13px`.
- Tables/lists: hairline row dividers, surface-2 hover row, mono for number columns.
- Badges/status: semantic colour at `8%` opacity background with semantic-colour text, never solid blocks.
- Charts: surface tones for lines/fills with primary emphasis; hairline gridlines; ink-subtle axis text.

## 10. Dark SaaS — Forbidden and Acceptance
- Never: large gradient backgrounds (especially purple/blue), rainbow or multiple accents, heavy shadows, glassmorphism unless asked, default cool framework greys instead of designed surfaces, card radius `>16px`.
- Check: background is `#010102` not pure black; exactly one accent; hierarchy by surface not shadow; headings negative-tracked at `500–600`; all dividers `1px` hairlines; light mode implemented with the inverse tokens.

# Part 3 — Minimal White (Apple-Style)

## 11. Minimal White — Principles
- Use for product sites, landing pages, portfolios.
- Whitespace is the design: better empty than crowded. Section spacing `≥96px`, element spacing `≥24px`.
- Large, light headlines: not `600–700` bold, but weight `500–600` at huge sizes (`48–96px`) with tight leading. "Big and thin" creates premium feel.
- Black-and-white high contrast with almost no accent: near-black text `#1d1d1f`, pure white `#ffffff` or very light grey `#f5f5f7` backgrounds; link blue `#0066cc` only on clickable elements.
- Single-row navigation, always.
- Product imagery is the hero; UI recedes. Images sit on `#f5f5f7` panels.
- Restrained radius and shadow: cards `12–18px`; shadow only on elevated states and very faint (`0 4px 24px rgba(0,0,0,.08)`).

## 12. Minimal White — Tokens
- Canvas `#ffffff`; canvas-alt `#f5f5f7` (image panels, section separation).
- Ink `#1d1d1f`; ink-muted `#6e6e73`; ink-subtle `#86868b`; hairline `#d2d2d7`.
- Accent `#0066cc` (the only link/interaction colour); accent-hover `#0071e3`.
- Card shadow `0 4px 24px rgba(0,0,0,0.08)`; radius `12px`.

## 13. Minimal White — Typography
- Heading scale, all `500–600` with `letter-spacing` from `-0.02em`: `96px` hero → `64px` section → `40px` card title → `28px` subtitle.
- Body `17–21px / 400 / 1.5`, one step larger than usual (premium product sites start body at `17px`).
- Keep all text rendering "light": no `700` weight, no text shadows.
- Font: `-apple-system` / SF Pro first; `Inter` on other platforms.

## 14. Minimal White — Components
- Hero: `96px` light headline centred, `21px` muted subtitle, large product image beneath on an alt panel.
- Nav: one row; logo centred with link groups either side at `12–14px` light weight; pill CTA on the right (ink background, white text).
- Feature cards: white with faint shadow, `28px` line icons, `28px` light-weight titles.
- Large image section: canvas-alt background, image at `80%` width centred, `96px` breathing room above and below.
- Buttons: primary = near-black pill (ink background, white text, radius `980px`); secondary = transparent with accent text.
- Pricing: three columns, middle column highlighted on canvas-alt, prices at `48px` light weight.
- Footer: minimal 3–4 columns, `12px` muted text, hairline at top.

## 15. Minimal White — Forbidden and Acceptance
- Never: dark themes (route to Dark SaaS), gradients, glassmorphism, heavy shadows, flashy animation, complex multi-column nav or hamburger menus (except on very small viewports), full-bleed wall-to-wall card grids, `700` weight headlines.
- Check: headings light, `≥48px`, tight leading; section spacing `≥96px`; `≤1` accent colour site-wide; single-row nav; images on `#f5f5f7` or the image itself is the hero; no gradients, glass, or heavy shadows.

# Part 4 — Soft UI (Neumorphism)

## 16. Soft UI — Principles
- Use for personal pages, health/finance lifestyle apps, demos.
- Same-colour base plus dual shadow: every element sits on a base the same colour as the background and is "extruded" by a light top-left shadow and a dark bottom-right shadow: `-6px -6px 12px rgba(255,255,255,.8), 6px 6px 12px rgba(0,0,0,.12)`.
- Background and elements share one colour (`#e0e5ec`, or within `±2%` lightness); layers come from shadow, not colour difference.
- Low contrast: text and icons in mid grey `#5f6b7a`; no large areas of pure black or pure white.
- Rounded: radius `16–24px`; circles and pills dominate.
- Pressed state uses inner shadows: `inset 4px 4px 8px rgba(0,0,0,.12), inset -4px -4px 8px rgba(255,255,255,.8)`.
- Use sparingly: only buttons, cards, toggles and a few other elements are extruded; keep background and text simple.

## 17. Soft UI — Tokens
- Bg `#e0e5ec` (page = element base); bg-pressed `#dde2e9`.
- Ink `#5f6b7a`; ink-muted `#8a97a8`; optional soft accent `#6c9bd1`.
- Raised shadow `-6px -6px 12px rgba(255,255,255,.8), 6px 6px 12px rgba(0,0,0,.12)`.
- Pressed shadow `inset 4px 4px 8px rgba(0,0,0,.12), inset -4px -4px 8px rgba(255,255,255,.8)`.
- Radius `20px`.

## 18. Soft UI — Components and Type
- Button: same-colour background + raised shadow, pill radius (`20px+`); deeper shadow on hover; switch to pressed shadow on active.
- Card: raised shadow, radius `24px`, inner padding `24px`.
- Input: debossed (pressed/inner shadow), ink text.
- Toggle/slider: raised circular track; thumb in accent or white with a micro shadow.
- Icons: raised circles `40–56px` with line icons in ink.
- Progress: debossed track with a raised fill.
- Type: headings `600 / 28–36px`; body `14–16px / 400 / 1.6`, all in mid-grey ink; `-apple-system` / `Inter` / `Noto Sans SC`; no serifs, no heavy black bolds.

## 19. Soft UI — Forbidden and Acceptance
- Never: large areas of pure black/white text or high-contrast palettes; element/background difference beyond `3%` lightness; extruding more than `40%` of visible elements; mixing hard `1px solid` borders with extrusion; complex charts or tables (unsuited to dense interfaces).
- Check: every raised element is same-colour + dual shadow with no border; pressing gives inset feedback; all text is mid grey; extruded elements `≤40%`; radius `≥16px`.

# Part 5 — Brutalism (Neo-Brutalist)

## 20. Brutalism — Principles
- Use for experimental products, art/indie projects, developer tools.
- Thick black hard borders: `2–4px solid #000`; the border is the protagonist, not a divider.
- Square corners: `border-radius: 0`. Any rounding is an error.
- High contrast: pure black `#000` on pure white `#fff`.
- Hard offset shadows with no blur and no transparency: `4px 4px 0 #000`, growing on hover (`8px 8px 0`).
- At most two saturated primaries as accent blocks: yellow `#ffde00`, orange-red `#ff4d00`, blue `#00c2ff`.
- Chunky type: `700–900` weights, mono or ultra-heavy sans; headlines may overflow the grid.
- Inverted blocks: black-on-white, white-on-black and black-on-yellow alternate; deliberately "inelegant".

## 21. Brutalism — Tokens
- Ink `#000000`; paper `#ffffff`; yellow `#ffde00`; orange `#ff4d00` (optional); blue `#00c2ff` (optional, max 2 of 3 used).
- Border `3px solid #000`; shadow `4px 4px 0 #000`; shadow-lg `8px 8px 0 #000`.
- Heading font `'Arial Black', 'Helvetica Neue', Impact, sans-serif`; mono `ui-monospace, 'SF Mono', Menlo, monospace`.

## 22. Brutalism — Typography
- Headings `800–900`, ultra-heavy faces, `48–96px`, left-aligned by default.
- Body `16px / 400 / 1.5`, plain sans or mono.
- Small labels `12px` uppercase mono, bordered or on an inverted background.
- Overflowing and overlapping elements are allowed; brutalism isn't afraid of "messy".

## 23. Brutalism — Components
- Card: white, `3px` black border, `4px 4px 0` shadow, square.
- Button: black-on-white or white-on-black, `3px` border, `4px 4px 0` shadow, growing to `8px 8px 0` on hover.
- Nav: heavy black bottom border (`3px`); logo as a white-on-black block.
- Hero: huge headline (`72–96px` ultra-bold) with an inverted label block (black on yellow).
- Colour blocks: solid yellow/orange/blue emphasis areas with black text.
- Pricing: each card its own hard border + shadow; middle card inverted on yellow.
- Tables/lists: `2px` dividers or alternating colour-block rows.
- Footer: a solid black block with white text.

## 24. Brutalism — Forbidden and Acceptance
- Never: any radius `>0`; gradients, blur, glass, soft shadows (with blur or transparency); more than two primaries; thin (`<2px`) or grey borders; refined whitespace minimalism (brutalism is crowded and full).
- Check: radius `0` everywhere; borders `≥2px` pure black; shadows are hard offsets that grow on hover; `≤2` primaries; at least one inverted block; heavy-weight sans or mono headings.

# Part 6 — Glassmorphism

## 25. Glassmorphism — Principles
- Use for AI products, SaaS marketing sites, dashboards, demos.
- A vivid gradient background is the foundation: without it, glass reads as nothing. Gradients are large and soft (deep blue → purple → pink, or cyan → blue → purple), no hard colour blocks.
- Glass card = translucency + blur: `background: rgba(255,255,255,0.12); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.25)`.
- A `1px` bright edge at `rgba(255,255,255,0.2–0.3)` simulates refractive highlight.
- Soft large-radius shadow (`0 8px 32px rgba(0,0,0,0.35)`) makes cards float.
- White text and translucent white (`rgba(255,255,255,.7)`) on the typically dark gradient.
- Nest translucent white elements (buttons, tags) inside glass for layered depth.

## 26. Glassmorphism — Tokens
- Background `linear-gradient(135deg, #0f0c29, #302b63 50%, #24243e)`.
- Glass bg `rgba(255,255,255,0.12)`; border `1px solid rgba(255,255,255,0.25)`; blur `blur(20px)`; shadow `0 8px 32px rgba(0,0,0,0.35)`.
- Text `#ffffff`; muted `rgba(255,255,255,0.72)`; subtle `rgba(255,255,255,0.5)`.
- Radius `20px`; system sans stack; system mono stack.

## 27. Glassmorphism — Typography and Components
- Headings `600–700`, white, optional faint glow `text-shadow: 0 0 40px rgba(255,255,255,.15)`.
- Body `15–16px / 400 / 1.6` in translucent white; small labels `12px` uppercase in glass pills.
- Never black text on the dark gradient.
- Background: fixed gradient, optionally with floating low-opacity light blobs.
- Glass cards: the full recipe with `20px` radius.
- Buttons: glass pills; on hover background opacity rises to `0.2`.
- Nav: a glass bar with a bright bottom edge.
- Hero: big headline plus a glass card holding a product UI panel.
- Inputs: an inset glass feel with a translucent background and inner bright edge.
- Feature cards: glass grid; hover brightens edge and opacity slightly.

## 28. Glassmorphism — Forbidden and Acceptance
- Never: flat solid backgrounds; hard black borders or brutalist elements; opaque dark cards; blur below `10px` (glass disappears); glass covering the whole screen (cap at `40–60%` of area, the rest is gradient breathing room).
- Check: gradient background; cards use `backdrop-filter: blur(≥15px)` + translucent white; `1px` bright border at `rgba(255,255,255,.2)+`; white-family text, no pure black; soft shadows; glass `≤60%` of area.

# Part 7 — Japanese Minimal

## 29. Japanese Minimal — Principles
- Use for cultural/aesthetic products, blogs, art exhibitions, Japanese-inflected brands, zen landing pages.
- Whitespace as *ma* (the meaningful interval): emptiness dominates; section spacing `≥96px`, line-height `≥1.8`. Better empty than full.
- Serif is the soul: Mincho/Song-style serifs for headings and body; no gothic sans for headlines; weights `400–500`, no bold.
- Black and white plus one touch of vermilion: rice-paper background `#fafaf7` or white, near-black text `#1a1a18`, vermilion `#c3272b` only for a seal, key emphasis or links, in one place.
- Hairline dividers (`1px` warm grey `#d8d5cd`) or whitespace alone.
- Restraint and order: symmetric or grid-aligned, steady vertical rhythm, no decorative animation, no gradients, no (or nearly no) shadows.
- Vertical text is an optional refinement: titles or signatures in `writing-mode: vertical-rl`, right to left.

## 30. Japanese Minimal — Tokens
- Paper `#fafaf7`; ink `#1a1a18`; ink-muted `#6b675e` (warm grey); ink-subtle `#a09a8d`; line `#d8d5cd`; vermilion `#c3272b` (only accent).
- Serif stack: `'Hiragino Mincho ProN', 'Yu Mincho', 'Noto Serif SC', 'Songti SC', 'SimSun', Georgia, serif`.
- Sans stack for labels: `'Hiragino Kaku Gothic ProN', 'Yu Gothic', 'PingFang SC', 'Microsoft YaHei', sans-serif`.
- Section spacing base `96px`.

## 31. Japanese Minimal — Typography
- Headings: serif `400–500`, `40–64px`, line-height `1.4–1.6`, tracking `0.05em` (Japanese titles can take extra tracking).
- Body: serif `15–16px / 400 / 1.8–2.0`, tracking `0.02em`.
- Small labels: sans `11–12px`, tracking `0.2em`, uppercase or kana.
- Numbers/dates: serif or mono, restrained.
- Vertical title: `writing-mode: vertical-rl; height: 100%` for a hero side column or signature.

## 32. Japanese Minimal — Components
- Nav: `1px` hairline at top, small widely-tracked sans links; logo in serif or kanji.
- Hero: huge whitespace (`≥120px` above and below), serif headline centred or left, one line of small explanatory text beneath.
- Seal (hanko): a vermilion square (`background: vermilion; color: #fff`) with 2–4 characters, optionally rotated `-2°`, as the single focal accent.
- Feature/article cards: no border, no shadow; grouped by whitespace alone, or a `1px` line plus generous space.
- Images: large with whitespace around, greyscale or natural colour, a single serif caption line below.
- Dividers: `1px` line or pure whitespace.
- Footer: `1px` line at top, small type, optional vertical signature.

## 33. Japanese Minimal — Forbidden and Acceptance
- Never: sans-serif display headings; bold (`>500`) or italic; gradients, shadows, glass, heavy borders, rounded-card styling; more than one accent (vermilion only, in `1–2` places); filling the page; animation, motion or big hover changes (keep it still).
- Check: serif headings `≤500`; section spacing `≥96px`, body line-height `≥1.8`; rice-paper or white background, never black; vermilion only, `≤2` uses; dividers are `1px` lines or space; no gradients, shadows, or glass.

# Part 8 — Bento Grid

## 34. Bento Grid — Principles
- Use for product sites, feature showcases, SaaS homepages, personal pages.
- The grid is the skeleton: uniform gaps, tiles of different sizes (`1×1`, `2×1`, `2×2`, `1×2`) that must snap strictly to grid lines.
- Rounded and airy: tile radius `16–24px`, gaps `12–20px`, generous page whitespace (section spacing `≥80px`).
- Light by default (`#ffffff` / `#f5f5f7`); dark mode optional with the same grid logic.
- Restrained colour: each tile gets a soft low-saturation tint; one accent site-wide.
- Tile content = icon (rounded square or circle) + big title + one-line description; large tiles may hold screenshots, charts or lists.
- Hierarchy by size and tint: the most important content gets the largest tile (`2×2` or `3×2`).

## 35. Bento Grid — Tokens
- Canvas `#ffffff`; canvas-alt `#f5f5f7`; ink `#1d1d1f`; ink-muted `#6e6e73`; accent `#0071e3` (only accent).
- Card radius `20px`; gap `16px`; card padding `24px`.
- Low-saturation tile pool: blue `#eef2ff`, purple `#f5f0ff`, green `#e8f5ee`, yellow `#fff7e6`, orange `#fdf0ef`, teal `#f0f4f8`.

## 36. Bento Grid — Typography and Components
- Headings `600–700`: `36–48px` hero, `22–28px` tile titles; descriptions `14–15px / 400 / 1.5` muted; one font site-wide (`-apple-system` / `Inter`).
- Icons sit in rounded squares (`10–12px` radius), icon glyph `22–28px`.
- Hero: centred headline + subtitle + two CTAs, flowing straight into the grid.
- Grid mechanics: CSS grid with fixed `grid-auto-rows` (e.g. `120px`), `grid-auto-flow: dense`, tile size via `grid-column/row: span n`.
- Large `2×2` tile: main screenshot/chart + title + description, on `tile-1` or the deepest tint.
- Small `1×1` tile: icon + title + one line.
- Medium `2×1` tile: split layout, text plus image/chart.
- Metric tile: big number at `600` weight `32px+` plus a small label.
- Icon block: `28–40px` rounded square with a `24px` icon on `rgba(255,255,255,.6)` or accent at `10%`.
- Tile hover: slight lift (`translateY(-2px)`) with a deeper shadow.

## 37. Bento Grid — Forbidden and Acceptance
- Never: tiles of arbitrary misaligned sizes; gaps `<12px` or `>24px` (the boxed neatness is lost); high-saturation rainbow tile walls; radius `<12px`; complex gradient tiles (use very faint flat tints); mixing in glass or brutalist elements.
- Check: tiles strictly on the grid; 2–3 tile sizes present; radius `≥16px` and gaps `12–20px`; low-saturation tints with `≤1` accent; each tile is icon/image + title + description; section spacing `≥80px`.

# Part 9 — Cyberpunk (Neon)

## 38. Cyberpunk — Principles
- Use for tech products, AI tools, games, geek-facing landing pages.
- Dark base plus neon strokes: near-black blue backgrounds (`#0a0a12` / `#0d0d1a`) with neon cyan `#00f0ff`, magenta `#ff00e5` and yellow `#ffe600` as borders and text, like neon tubes.
- Glow is the core technique, built from layered shadows: `text-shadow: 0 0 8px rgba(0,240,255,0.8), 0 0 24px rgba(0,240,255,0.4)`; `box-shadow: 0 0 8px rgba(255,0,229,0.6), inset 0 0 8px rgba(255,0,229,0.3)`.
- Neon discipline: one main neon (cyan or magenta), one secondary, yellow only as a spark; body text white/light grey.
- Optional glitch/tech decoration: scanlines (`repeating-linear-gradient` horizontals), glitch text (offset `clip-path`), grid backgrounds, HUD corner brackets.
- Fonts: heavy or futuristic sans for headings, plain sans for body, mono for tech labels.
- Panels use `1px` neon borders with small HUD corner marks.

## 39. Cyberpunk — Tokens
- Bg `#0a0a12`; bg-2 `#12121f`; text `#e8e8f0`; text-dim `#8a8aa0`.
- Neon cyan `#00f0ff`; magenta `#ff00e5`; yellow `#ffe600`.
- Neon border `1px solid rgba(0,240,255,0.6)`.
- Cyan glow `0 0 8px rgba(0,240,255,0.8), 0 0 24px rgba(0,240,255,0.4)`; magenta glow `0 0 8px rgba(255,0,229,0.6), 0 0 24px rgba(255,0,229,0.3)`.
- Heading font `'Arial Black', 'Helvetica Neue', Impact, sans-serif`; mono system stack.

## 40. Cyberpunk — Typography and Components
- Headings: weight `900` or a futuristic face, white/cyan/magenta, with glow.
- Tech labels: mono `10–12px` uppercase, cyan or yellow, tracking `0.2em`.
- Body `14–15px` in text or text-dim; metrics in mono with cyan glow.
- Background: dark with optional faint `1px` gridlines or a scanline overlay.
- Nav: `1px` cyan bottom edge, glowing logo text.
- Primary button: neon fill (cyan or magenta) with black text and outer glow; glow intensifies on hover.
- Secondary button: transparent, `1px` neon border, neon text, inner glow.
- Cards: bg-2 with `1px` neon border and HUD corner brackets via pseudo-elements.
- Inputs: dark with neon border; glow intensifies on focus.
- Terminal panel: black with cyan border, mono green/cyan text, `>` prompt.
- Badges: neon-bordered pills with neon text.

## 41. Cyberpunk — Forbidden and Acceptance
- Never: soft or low-contrast palettes (cyberpunk is sharp); large radii (cards `≤8px`, buttons may be pills); more than two neons together (cyan + magenta, yellow as spark only); white or light pages; glass or minimal-white open whitespace; thin heading weights.
- Check: background dark (lightness `<30`); `≤3` neons with one main; headings/buttons glow; cards have `1px` neon borders; body text readable (white/light grey on dark); at least one tech decoration (scanlines, grid, HUD marks).

# Part 10 — Vaporwave (Synthwave)

## 42. Vaporwave — Principles
- Use for art projects, music/culture sites, experimental landing pages.
- Signature pink → purple gradient sky (`linear-gradient(#ff71ce, #b967ff)`) with a striped retro sun.
- A perspective grid floor below forms the horizon composition.
- Classical silhouettes (Greek busts, Roman columns, palm trees) set in front of the sun.
- Retro neon accents in magenta/cyan/yellow with glow, echoing the 80s.
- Japanese kana or kanji as decorative elements (a hallmark of the genre).
- Retro type: heavy sans, optionally skewed, or retro serif for headings; plain sans for body.

## 43. Vaporwave — Tokens
- Sky-1 `#ff71ce` (pink); sky-2 `#b967ff` (purple); sky-3 `#5c3d99` (deep purple below the horizon).
- Ink `#ffffff`; ink-dim `rgba(255,255,255,0.8)`.
- Neons: cyan `#00f0ff`, magenta `#ff00e5`, yellow `#ffe600`.
- Glow `0 0 8px rgba(255,0,229,0.7), 0 0 24px rgba(255,0,229,0.4)`.
- Heading font `'Arial Black', 'Helvetica Neue', Impact, sans-serif`; Japanese sans stack for decorative glyphs.

## 44. Vaporwave — Typography and Components
- Headings: heavy sans, white or neon, optional `skewX(-3deg)`, with glow.
- Decorative text: kana/kanji (e.g. 永遠 "eternity", 夢 "dream") placed in corners or beneath the sun.
- Body `15–16px` in white/translucent white; small labels `12px` uppercase mono or sans in neon.
- Sky: sky-1 → sky-2 gradient filling the top half of the first screen.
- Retro sun: a semicircle with horizontal stripes (`repeating-linear-gradient`) in pink-purple or orange.
- Silhouette layer: deep purple shapes (`rgba(30,20,60,.9)`) of columns, busts or palms in front of the sun.
- Grid floor: sky-3 base with white/purple horizontal and vertical lines, fading out with transparency.
- Cards: translucent deep purple (`rgba(30,20,60,.55)`) with `1px` neon border, optional blur.
- Buttons: magenta/cyan neon border with glow, intensifying on hover.
- Nav: transparent; glowing white logo. Metrics/code: mono in cyan/magenta.

## 45. Vaporwave — Forbidden and Acceptance
- Never: omitting the gradient sky; white or light pages; photorealism (aim for retro, degraded, VHS); modern minimal grey-white palettes; big rounded corners (stay 80s-hard + neon).
- Check: pink→purple sky at top; a retro sun or silhouettes; a grid floor/horizon; neon glow on headings or buttons; overall pink + purple + deep purple + neon; optional Japanese decorative text.

# Part 11 — Art Deco

## 46. Art Deco — Principles
- Use for luxury brands, grand hotels, art/fashion sites, boutiques.
- Symmetry and geometry: strictly symmetric layouts; ornament from geometric forms (sunbursts, stepped shapes, fans, diamonds, zigzags).
- Gold-on-dark luxury: emerald `#0e1f14`, navy `#101828` or black `#141414` with gold (`#c9a24b` / `#d4af37`) and ivory text.
- Line as ornament: thin gold lines (`1–2px`) for borders, dividers and frames; multi-layer stepped rectangular frames are the signature move.
- Type: serif with geometric flavour (Didot, Bodoni, Playfair Display) for headings, uppercase with wide tracking; plain serif or sans for body.
- Radiating elements: sunbursts and fans in the logo area, footer and corners.
- Restrained luxury: gold as line and accent only, never a flood; lots of dark space makes the gold shine.

## 47. Art Deco — Tokens
- Bg `#0e1f14` (emerald); bg-2 `#132619`; ink `#f2ead8` (ivory); ink-dim `#c8bda4`.
- Gold `#c9a24b`; gold-bright `#e8c86a`; line `1px solid rgba(201,162,75,0.6)`.
- Display font `'Playfair Display', Didot, 'Bodoni MT', Georgia, serif`; body `'Helvetica Neue', Helvetica, Arial, sans-serif`.

## 48. Art Deco — Typography
- Headings: serif, uppercase, wide tracking `0.15–0.3em`, gold or ivory.
- Subheads: `14–16px`, tracking `0.2em`, gold.
- Body: `14–15px / 1.7`, ivory or dim ivory.
- Numbers and dates: serif or geometric figures in gold.

## 49. Art Deco — Components
- Ornamental frame: double-line rectangles (heavy outer, thin inner, or two border layers) with stepped corners via `clip-path` or stacked frames.
- Sunburst: radiating lines via `repeating-conic-gradient` or SVG, behind the logo and above the footer.
- Nav: `1px` gold rule at top; gold serif logo centred or left.
- Buttons: gold border, transparent fill, gold uppercase widely-tracked text; on hover fill gold with black text.
- Cards/panels: bg-2 with a `1px` gold border and corner diamond/triangle ornaments.
- Dividers: thin gold line with a small central diamond or fan.
- Metrics: large gold serif numerals with small widely-tracked labels.
- Footer: gold rule at top, sunburst ornament, widely-tracked serif text.

## 50. Art Deco — Forbidden and Acceptance
- Never: bright modern palettes (neon, candy, pure white); big rounded cards (Deco is square/geometric, radius `≤4px`); sans-serif headings (must be serif/geometric); gold floods (gold `<15%` of area); asymmetric chaos (symmetry and order are the point); photorealistic imagery.
- Check: dark ground (emerald/navy/black); gold limited to lines, text and ornament; serif uppercase widely-tracked headings; at least one geometric ornament (sunburst, diamond, stepped or double frame); symmetric layout; radius `≤4px`.

# Part 12 — Art Deco in Practice

## 51. Tokens
- Emerald canvas stack: `--bg: #0e1f14`, `--bg-2: #132619` (cards, panels), `--bg-3: #0a1610` (code, featured price card).
- Warm ivory ink: `--ink: #f2ead8`, `--ink-dim: #c8bda4`; never pure white.
- Two golds: `--gold: #c9a24b` (lines, icons, eyebrows) and `--gold-bright: #e8c86a` (titles, metric numbers, hover text).
- Line tokens are full border shorthands: `--line: 1px solid rgba(201, 162, 75, 0.6)` and `--line-strong: 2px solid rgba(201, 162, 75, 0.85)`; weaker dividers use `rgba(201, 162, 75, 0.3)` and `0.2`.
- No radius token at all: every box is square-cornered.

## 52. Type Setup
- Display face `--font-display: 'Playfair Display', Didot, 'Bodoni MT', 'Times New Roman', Georgia, serif`; body `'Helvetica Neue', Helvetica, Arial, sans-serif`.
- Body `15px`, `line-height: 1.7`, antialiased.
- Display sizes are fixed px, no `clamp()`: `.display-xl` `58px` / `line-height: 1.15` / `letter-spacing: 0.12em`; `.display-lg` `40px` / `1.2` / `0.14em`.
- All display type is `font-weight: 400` + `text-transform: uppercase`: the wide tracking supplies the grandeur, not the weight.
- Eyebrow `12px`, weight `500`, `letter-spacing: 0.35em`, uppercase, gold; card titles `20px` / `0.12em` in `--gold-bright`.
- Small caps-style labels go very wide: nav links `0.25em`, price names `0.3em`, footer headings `0.3em`, metric labels `10px` at `0.25em`.
- Lead `16px` with `letter-spacing: 0.03em`; code `pre` uses the body sans at `line-height: 2`.

## 53. Layout & Section Order
- Narrow, centered column: `.container { max-width: 1000px; padding: 0 28px }`.
- Order: sticky nav → centered hero with framed terminal → 3 feature cards → 4-up metrics band → config code block → 3 pricing tiers → framed CTA → 4-column footer (`2fr 1fr 1fr 1fr`).
- Everything symmetrical: section heads `max-width: 560px; margin: 0 auto 56px; text-align: center`; cards and price cards also centre their text.
- Section rhythm `padding: 96px 0`; sections after features set `padding-top: 0` so content flows as one column.
- Section eyebrows are wrapped in diamonds: `◆ Why Relay ◆`.

## 54. Hero Treatment
- `padding: 130px 0 80px`, centered, `h1` capped at `720px`, lead at `500px`.
- Sunburst behind the headline: `.radial::before` is a `480px` circle at `top: -140px` filled with `repeating-conic-gradient(from 0deg, transparent 0deg 8deg, rgba(201,162,75,0.08) 8deg 16deg)`.
- Bottom gold rule fades out at both ends: `.hero::after { width: 180px; height: 1px; background: linear-gradient(to right, transparent, var(--gold), transparent) }`.
- Hero note `11px`, `letter-spacing: 0.3em`, uppercase.
- The terminal becomes a "deco panel": title `— Session № 4821 —` centred in display serif at `0.3em`, separated by `border-bottom: var(--line)`.

## 55. Components
- Buttons are square ghost frames: `padding: 15px 34px`, `13px`, weight `500`, `letter-spacing: 0.25em`, uppercase, `border: 1px solid rgba(201, 162, 75, 0.8)`, gold-bright text; `.btn-solid` fills with `--gold` and dark `#0e1f14` text; `.btn-lg` `17px 40px`.
- Nav: sticky, `background: rgba(14, 31, 20, 0.92)`, `border-bottom: var(--line)`, `height: 72px`, link gap `36px`; the CTA shrinks to `padding: 11px 24px; font-size: 11px`.
- Brand mark is a rotated diamond: `30px` box, `1px solid var(--gold)`, `transform: rotate(45deg)`, with the letter counter-rotated via `::before { transform: rotate(-45deg) }`.
- Feature card: `--bg-2`, `border: var(--line)`, `padding: 28px 24px`, centred; body `13px` / `line-height: 1.8`.
- Metrics band: `border-top`/`border-bottom: var(--line-strong)`, `padding: 40px 0`, columns divided by `border-right: 1px solid rgba(201,162,75,0.3)`; numbers in display serif `40px` gold-bright at `0.08em`.
- Price cards: `padding: 36px 28px`, centred, list rows divided by `rgba(201,162,75,0.2)`; amount `46px` display serif; featured tier gets `border-color: var(--gold)` and the darker `--bg-3`.
- Code tokens: keywords `--gold`, numbers `--gold-bright`, strings `--ink-dim`, comments `rgba(200,189,164,0.5)` italic.

## 56. Signature Effects
- Double frame: `border: var(--line-strong)` plus `outline: 1px solid rgba(201, 162, 75, 0.35); outline-offset: 6px`, used on the terminal and CTA.
- Glyph ornaments via pseudo-elements: `content: '◆'` at `9px` pinned to opposite corners (`top: -14px; left: -6px` / `bottom: -14px; right: -6px`) on the terminal.
- Corner brackets on cards: `14px` squares with `1px solid var(--gold)`, the top-left one with `border-right/bottom: none` at `top: 8px; left: 8px`, the bottom-right mirrored.
- Featured price card is crowned with `content: '★'` centred on the top border at `top: -13px`, given `background: var(--bg); padding: 0 12px` so it cuts the line.
- Ornament glyphs used as icons and markers: `⌁ ◉ ↻`, `◆`, `★`, `№`.

## 57. Motion
- No keyframes; only colour transitions.
- Buttons: `transition: background 200ms ease, color 200ms ease`; hover fills ghost buttons with `--gold` and flips text to `#0e1f14`; solid hover lightens to `--gold-bright`.
- Cards: `transition: border-color 150ms ease`, hover sharpens the border to full `--gold`.
- Links hover to `--gold-bright`; `html { scroll-behavior: smooth }`.

## 58. Responsive & Accessibility
- Single breakpoint `@media (max-width: 900px)`: `.display-xl` → `38px`, `.display-lg` → `30px`, feature and pricing grids → `1fr`, metrics → `repeat(2, 1fr)` with the column dividers removed, footer → `1fr 1fr`, nav links hidden, hero padding → `88px 0 56px`.
- Code block uses `overflow-x: auto`; decorative layers use `pointer-events: none`.
- Ivory-on-emerald keeps body contrast high; small gold labels are the weakest pair, so they sit at `11–12px` with wide tracking rather than thin weight.
- No focus styles or reduced-motion rule are defined; add them when adopting the style.

# Part 13 — Apple Minimal in Practice

## 59. Tokens
- Canvas pair: `--canvas: #ffffff`, `--canvas-alt: #f5f5f7` (alternate bands, product panel, featured tier, footer).
- Ink scale: `--ink: #1d1d1f`, `--ink-muted: #6e6e73`, `--ink-subtle: #86868b`, `--hairline: #d2d2d7`.
- One accent only: `--accent: #0066cc`, `--accent-hover: #0071e3`.
- Elevation and shape: `--card-shadow: 0 4px 24px rgba(0, 0, 0, 0.08)`, `--radius: 12px`, `--pill: 980px`; large surfaces use `24px` radius.
- System stacks: `-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif` and `ui-monospace, 'SF Mono', Menlo, Consolas, monospace`.

## 60. Type Setup
- Body `17px`, `line-height: 1.5`, global `letter-spacing: -0.01em`.
- Display scale in fixed px (no `clamp()`), all weight `600` with `letter-spacing: -0.02em`: `.display-xl` `80px` / `1.05`, `.display-lg` `56px` / `1.1`, `.display-md` `40px` / `1.15`.
- Card title `28px` / `1.2` / `-0.01em`; lead `21px` in `--ink-muted`; section-head paragraphs `19px`.
- Eyebrow `13px`, weight `600`, `letter-spacing: 0.02em`, uppercase, in `--accent`.
- Metric numbers `44px` weight `600` at `-0.02em`; labels `14px` in `--ink-subtle`.
- Footer headings `12px`, `600`, `0.04em`, uppercase.

## 61. Layout & Section Order
- `.container { max-width: 980px; padding: 0 22px }`.
- Order: sticky blurred nav → centred hero with product panel → 6-item feature grid → metrics on an alt-canvas band → config code → 3 pricing tiers → open CTA (no box) → alt-canvas footer.
- Generous spacing: `.section { padding: 120px 0 }`; section heads `max-width: 640px; margin: 0 auto 72px`, centred.
- Alternating bands: `.section-alt { background: var(--canvas-alt) }` for metrics at `padding: 96px 0`.
- Feature grid `repeat(3, 1fr)` with a wide `40px` gap; features are borderless and centred.

## 62. Hero Treatment
- `padding: 120px 0 96px`, centred; `h1` `max-width: 800px` with a manual `<br>` line break; lead `620px`.
- Product shot stand-in: `.product-panel { margin-top: 80px; background: var(--canvas-alt); border-radius: 24px; padding: 48px; box-shadow: var(--card-shadow) }`.
- Panel toolbar with three neutral `11px` dots in `--hairline`, separated from content by a `1px` hairline.
- Primary CTA is black, not blue: `--ink` fill with white text; secondary is accent text on hairline outline.

## 63. Components
- Pill buttons: `padding: 12px 22px`, `border-radius: 980px`, `14px`, weight `400`; `.btn-lg` `16px 30px` at `16px`.
- Primary: `background: var(--ink)`, hover `#333336`; secondary: transparent, `color: var(--accent)`, `border: 1px solid var(--hairline)`, hover `--canvas-alt`.
- Nav: `height: 52px`, `background: rgba(255,255,255,0.8)`, `backdrop-filter: blur(20px)`, hairline bottom border on the inner row; links `14px`, gap `32px`; CTA `8px 16px` at `13px`.
- Feature icon: `64px` circle, `--canvas-alt` fill, `1px solid var(--hairline)`, `24px` glyph; feature copy `15px` / `1.6` capped at `280px`.
- Code block: white, `1px` hairline, `--radius` (`12px`), `padding: 32px`, `--card-shadow`; tokens are keyword `--accent`, number `--ink-muted`, comment `--ink-subtle` italic.
- Price cards: white, hairline border, `border-radius: 24px`, `padding: 40px 32px`, left-aligned; featured tier swaps to `--canvas-alt`, `border-color: transparent` and the card shadow.

## 64. Signature Effects
- Restraint is the effect: a single soft shadow `0 4px 24px rgba(0,0,0,0.08)` and a frosted nav (`blur(20px)` over `0.8` white).
- Depth by tone shift between `#ffffff` and `#f5f5f7` rather than borders or colour.
- No gradients, glows, textures or decorative pseudo-elements.

## 65. Motion
- No keyframes.
- Buttons: `transition: opacity 150ms ease, background 150ms ease`; hover is a quiet background shift.
- Links: accent text that underlines on hover (`text-decoration: underline`) and moves to `--accent-hover`; nav links fade to `--ink-muted` instead.
- `html { scroll-behavior: smooth }`.

## 66. Responsive & Accessibility
- `@media (max-width: 900px)`: `.display-xl` → `48px`, `.display-lg` → `36px`, features and pricing → `1fr` with `48px` gap, metrics → `repeat(2, 1fr)` with `40px` gap, footer → `1fr 1fr`, nav links hidden, hero → `80px 0 64px`, sections → `80px 0`, product panel padding → `24px`.
- Dark ink `#1d1d1f` on white gives strong body contrast; `--ink-subtle #86868b` is reserved for notes and labels.
- Code uses `overflow-x: auto`; `button { cursor: pointer; font-family: inherit }`.
- No explicit focus ring or reduced-motion handling is defined.

# Part 14 — Bento Grid in Practice

## 67. Tokens
- Apple-like base: `--canvas: #ffffff`, `--canvas-alt: #f5f5f7`, `--ink: #1d1d1f`, `--ink-muted: #6e6e73`, `--accent: #0071e3`.
- Grid tokens: `--card-radius: 20px`, `--gap: 16px`, `--card-pad: 24px`.
- Six pastel tile fills: `--tile-1: #eef2ff`, `--tile-2: #f5f0ff`, `--tile-3: #e8f5ee`, `--tile-4: #fff7e6`, `--tile-5: #fdf0ef`, `--tile-6: #f0f4f8`.
- Dividers `#ececf0` (nav, footer) and `#e5e5ea` (price lists); button border `#e0e0e5`.

## 68. Type Setup
- System sans stack, body `15px` / `line-height: 1.5`.
- Bolder than Apple: `.display-xl` `56px` / weight `700` / `1.1` / `-0.03em`; `.display-lg` `40px` / `700` / `1.15` / `-0.02em`.
- Card title `20px` / `600` / `1.25` / `-0.01em`; tile body `13px` / `1.5` in `--ink-muted`.
- Eyebrow `12px`, `600`, `letter-spacing: 0.08em`, uppercase, accent.
- Metric tiles: number `40px` / `700` / `-0.02em`, label `12px`.
- No `clamp()`; fixed px with one breakpoint override.

## 69. Layout & Section Order
- `.container { max-width: 1060px; padding: 0 24px }`.
- Order: sticky nav → centred hero whose visual is the bento grid itself → pricing → boxed CTA → footer; the bento replaces separate features, metrics and code sections.
- Bento grid: `display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: 120px; grid-auto-flow: dense; gap: var(--gap); margin-top: 56px`.
- Span classes define the rhythm: `.tile-lg { grid-column: span 2; grid-row: span 2 }`, `.tile-w { grid-column: span 2 }`, `.tile-h { grid-row: span 2 }`, `.tile-1x1 { span 1 / span 1 }`.
- Sequence used: one 2×2 hero tile, one tall tile, two 1×1, two wide, one 1×1 metric; mixing content types (feature, chart, metric, terminal) per tile.
- Sections `padding: 96px 0`; heads `max-width: 560px; margin: 0 auto 56px`.

## 70. Hero Treatment
- `padding: 96px 0 64px`, centred, `h1` `680px`, lead `520px` at `18px`.
- The largest tile carries a dark mini terminal: `.term-mini { background: #0f1420; border-radius: 14px; padding: 14px; font-size: 12px; color: #7dd3fc; line-height: 1.8; flex: 1 }` with success text in `#34d399`.
- Tall tile embeds a CSS bar chart: `.bars` flex with `gap: 6px`, bars `border-radius: 4px 4px 0 0`, `background: rgba(0,113,227,0.35)`, heights set with `:nth-child` (`40% 65% 50% 85% 60% 95%`).

## 71. Components
- Tile: `border-radius: 20px`, `padding: 24px`, flex column, pastel background, no border.
- Tile icon: `36px` square, `border-radius: 11px`, `background: rgba(255,255,255,0.7)`, `18px` glyph.
- Buttons: pill `980px`, `padding: 13px 26px`, `14px`, weight `500`; default is `--canvas-alt` with `1px solid #e0e0e5`; primary `--ink` fill with white text; `.btn-lg` `15px 30px`.
- Nav: `height: 60px`, `rgba(255,255,255,0.85)` with `backdrop-filter: blur(14px)`; brand mark `30px` with `border-radius: 9px`, accent fill, white letter.
- Price cards: `--canvas-alt`, `--card-radius`, `padding: 32px 28px`, no border; featured uses `--tile-1`; price names `13px` uppercase `0.06em`.
- CTA is a large rounded slab: `background: var(--canvas-alt); border-radius: 28px; padding: 64px 32px`.

## 72. Signature Effects
- Colour coding by tile rather than by border or shadow: each tile gets its own pastel from the six tokens.
- Nested radii: `20px` tile, `14px` inner terminal, `11px` icon, `9px` brand mark, `4px` bar tops.
- Mini data-vis built purely with flex and percentage heights.
- Frosted nav (`blur(14px)`) is the only blur.

## 73. Motion
- No keyframes.
- Tiles: `transition: transform 150ms ease, box-shadow 150ms ease`; hover `translateY(-2px)` + `0 8px 24px rgba(0,0,0,0.08)`.
- Buttons: same properties at 150ms; hover `translateY(-1px)` + `0 4px 16px rgba(0,0,0,0.08)`.
- Nav links fade from `--ink-muted` to `--ink`.

## 74. Responsive & Accessibility
- `@media (max-width: 900px)`: bento → `repeat(2, 1fr)` with `grid-auto-rows: 100px`; `.tile-lg` and `.tile-w` keep `span 2` so they become full-width rows; `.display-xl` → `40px`; pricing → `1fr`; footer → `1fr 1fr`; nav links hidden; hero → `72px 0 48px`.
- `grid-auto-flow: dense` back-fills holes so the grid stays gap-free at both column counts.
- Fixed `grid-auto-rows` can clip long tile copy; keep tile text short.
- No focus styles or reduced-motion rule.

# Part 15 — Brutalism in Practice

## 75. Tokens
- Pure contrast: `--ink: #000000`, `--paper: #ffffff`.
- Three loud flats: `--yellow: #ffde00`, `--orange: #ff4d00`, `--blue: #00c2ff`.
- Border tokens: `--border: 3px solid #000`, `--border-thick: 4px solid #000`.
- Hard offset shadows with zero blur: `--shadow: 4px 4px 0 #000`, `--shadow-lg: 8px 8px 0 #000`; hero panel uses `10px 10px 0 #000`.
- Radius is explicitly `0` on every component.

## 76. Type Setup
- Head `--font-head: 'Arial Black', 'Helvetica Neue', Impact, 'Arial', sans-serif`; body `'Helvetica Neue', Helvetica, Arial`; mono `ui-monospace, 'SF Mono', Menlo, Consolas`.
- Body `16px` / `1.5`.
- Display is heavy, tight and uppercase: `.display-xl` `80px` / weight `900` / `line-height: 0.95` / `-0.03em`; `.display-lg` `52px` / `900` / `1` / `-0.02em`.
- Card titles `20px` / `900` / `1.1` uppercase; price amount `44px` / `900` / `line-height: 1`.
- Mono for labels: eyebrows, nav links, metric labels, price periods, footer headings, all `12–13px` bold uppercase at `0.05em`.
- Body copy uses weight `500` (lead `19px`, card text `14px` / `1.6`).

## 77. Layout & Section Order
- `.container { max-width: 1100px; padding: 0 24px }`.
- Order: sticky nav → left-aligned hero with hard-shadow terminal → 3 feature cards → inverted black metrics block → inverted code block → 3 pricing tiers → inverted CTA band → full-black footer.
- Left-aligned throughout: `.section-head { max-width: 640px; margin-bottom: 48px }` with no auto-centring.
- Sections `padding: 80px 0`; grids use a tight `gap: 20px`.
- Inversion as section rhythm: metrics, code, CTA and footer flip to black backgrounds.

## 78. Hero Treatment
- `padding: 80px 0 64px`, left aligned, `h1` up to `900px`.
- Eyebrow is a sticker: yellow fill, `3px` black border, `padding: 4px 10px`, `4px 4px 0` shadow.
- Hero note is another sticker in `--blue`.
- Terminal panel: `border: 4px solid #000`, `box-shadow: 10px 10px 0 #000`, `padding: 24px`; a `::before` tab label `content: 'LIVE SESSION #4821'` sits on the top border at `top: -14px; left: 16px` in yellow with `2px` border.
- Inline highlights: `.term-out b { background: var(--yellow); padding: 0 4px }`; prompts in `--orange` bold.

## 79. Components
- Buttons: `padding: 14px 26px`, radius `0`, Arial Black `14px` / `900` uppercase `0.02em`, `3px` border, `4px 4px 0` shadow; variants `.btn-primary` (black fill, white text), `.btn-accent` (yellow); `.btn-lg` `18px 34px` at `16px`.
- Nav: white with `border-bottom: 4px solid #000`, `height: 64px`; links mono `13px` bold with `padding: 6px 10px` and a `2px solid transparent` border reserved for hover.
- Brand mark: `30px` black square, white letter, `3px` border, `3px 3px 0 #000` shadow.
- Cards: white, `3px` border, `4px 4px 0` shadow, `padding: 24px`; icon box `44px` yellow with border, and `:nth-child(2)` / `:nth-child(3)` swap the icon fill to blue and orange.
- Metrics: black block with `4px` border, cells `padding: 28px 20px` divided by `2px solid #fff`; numbers `34px` / `900` in yellow.
- Pricing: list rows divided by `2px solid #000`, each prefixed `::before { content: '▮ ' }`; featured tier is solid yellow with the large shadow.
- Code: black, `4px` border, `8px 8px 0` shadow; keywords yellow bold, strings blue, comments `rgba(255,255,255,.5)`.

## 80. Signature Effects
- Hard shadows only: offset, zero blur, solid black.
- Sticker labels (eyebrow, note, panel tab) overlap borders and break the grid.
- Flat fills rotated per item through `:nth-child` selectors.
- No gradients, blur or transparency on surfaces.

## 81. Motion
- No keyframes; fast, mechanical transitions: `transition: box-shadow 80ms ease, transform 80ms ease`.
- Lift on hover for buttons and cards: `transform: translate(-2px, -2px)` while the shadow grows from `4px 4px 0` to `8px 8px 0`, so the element looks raised off the page.
- Nav link hover draws a box: `border: 2px solid #000; box-shadow: 3px 3px 0 #000`.
- Footer links hover to yellow.

## 82. Responsive & Accessibility
- `@media (max-width: 900px)`: `.display-xl` → `48px`, `.display-lg` → `36px`, features and pricing → `1fr`, metrics → `repeat(2, 1fr)` with `.metric:nth-child(2) { border-right: none }` to fix dividers, footer → `1fr 1fr`, nav links hidden, hero → `56px 0 48px`, sections → `56px 0`.
- `.hero-actions` uses `flex-wrap: wrap` so large buttons stack on narrow screens.
- Black on white and black on yellow give maximum contrast; the `2px` transparent border on nav links stops hover from shifting layout.
- No focus or reduced-motion rules defined.

# Part 16 — Cyberpunk in Practice

## 83. Tokens
- Near-black blue canvas: `--bg: #0a0a12`, `--bg-2: #12121f`, `--bg-3: #1a1a2c`; terminal and code wells `#05050c`.
- Text: `--text: #e8e8f0`, `--text-dim: #8a8aa0`.
- Neon triad: `--neon-cyan: #00f0ff`, `--neon-magenta: #ff00e5`, `--neon-yellow: #ffe600`.
- Borders: `--border-neon: 1px solid rgba(0, 240, 255, 0.55)`, `--border-neon-mg: 1px solid rgba(255, 0, 229, 0.55)`.
- Two-layer glows: `--glow-cyan: 0 0 8px rgba(0,240,255,0.8), 0 0 24px rgba(0,240,255,0.4)`; `--glow-magenta: 0 0 8px rgba(255,0,229,0.6), 0 0 24px rgba(255,0,229,0.3)`.
- Radius kept tight: `4px` buttons, `6px` cards and panels.

## 84. Type Setup
- `--font-tech: 'Arial Black', 'Helvetica Neue', Impact, 'Arial', sans-serif` for display; mono stack for UI labels; Helvetica body at `15px` / `1.6`.
- `.display-xl` `64px` / `900` / `line-height: 1` / `-0.02em` uppercase with `text-shadow: var(--glow-cyan)`.
- `.display-lg` `44px` / `900` / `1.05` uppercase with `text-shadow: var(--glow-magenta)`.
- Eyebrows mono `12px` / `700` / `letter-spacing: 0.3em` uppercase, cyan with glow, prefixed `// `.
- Buttons, nav links, price names and metric labels all mono uppercase at `0.1–0.2em`.
- No `clamp()`; px sizes overridden at one breakpoint.

## 85. Layout & Section Order
- `.container { max-width: 1040px; padding: 0 24px; position: relative; z-index: 1 }` so content sits above the hero grid.
- Order: sticky blurred nav → centred hero on a grid backdrop with terminal → 3 HUD cards → bordered metrics strip → magenta-framed code → 3 pricing tiers → glowing CTA → footer.
- Sections `padding: 88px 0`; centred heads `max-width: 560px; margin: 0 auto 48px`.

## 86. Hero Treatment
- `padding: 104px 0 64px`, centred.
- Grid backdrop: `.hero::before` with two `linear-gradient`s of `rgba(0,240,255,0.04) 1px, transparent 1px` (one rotated `90deg`), `background-size: 48px 48px`.
- Hero note in neon yellow mono wrapped in `>> … <<`.
- Terminal: `#05050c`, cyan border, `border-radius: 6px`, `box-shadow: var(--glow-cyan)`; the three window dots each glow in their own neon; title styled as a URI `relay://session/4821`.
- Corner brackets on the terminal: `::before`/`::after` `14px` boxes with `2px solid var(--neon-cyan)`, offset `-1px` to sit on the border.

## 87. Components
- Primary button: cyan fill, black text, `padding: 14px 28px`, `border-radius: 4px`, mono `13px` / `700` / `0.1em`, permanent cyan glow.
- Secondary button: transparent, magenta text, `1px solid rgba(255,0,229,0.7)`, magenta glow; hover fill `rgba(255,0,229,0.12)`.
- Nav: `rgba(10,10,18,0.85)`, `backdrop-filter: blur(10px)`, cyan bottom border, `height: 60px`; brand mark `28px` cyan tile with glow.
- Card: `--bg-2`, cyan border, `6px` radius, `padding: 24px`, magenta corner brackets (`10px`, inset `6px`).
- Card icon: `40px`, `6px` radius, `1px solid rgba(0,240,255,0.5)`, tinted fill `rgba(0,240,255,0.06)`, glowing glyph.
- Price cards: featured tier switches to magenta border + magenta glow; list items mono with `::before { content: '▸ ' }` in cyan; amounts `44px` glowing magenta.
- Code block carries a floating label `::before { content: '// RELAY.CONFIG' }` at `top: -11px; right: 16px` with `background: var(--bg)` to cut the border; tokens cyan / yellow / magenta.

## 88. Signature Effects
- Full-page scanlines: `body::after { position: fixed; inset: 0; z-index: 100; pointer-events: none; background: repeating-linear-gradient(to bottom, transparent 0 2px, rgba(0,0,0,0.12) 2px 4px); opacity: 0.35 }`.
- Text glow on headings, eyebrows, prompts, metric numbers and hovered links.
- Alternating neon roles: cyan for structure and primary, magenta for secondary and featured, yellow for status and notes.
- HUD corner brackets on terminal and cards.

## 89. Motion
- No keyframes (no flicker or glitch animation).
- Buttons `transition: box-shadow 150ms ease, transform 150ms ease`; primary hover intensifies glow to `0 0 12px rgba(0,240,255,1), 0 0 36px rgba(0,240,255,0.6)` and lifts `translateY(-1px)`.
- Cards: `transition: box-shadow 150ms ease`, hover adds `--glow-cyan`.
- Nav links hover to cyan with glow; footer links to magenta with glow.

## 90. Responsive & Accessibility
- `@media (max-width: 900px)`: `.display-xl` → `42px`, `.display-lg` → `32px`, features and pricing → `1fr`, metrics → `repeat(2, 1fr)` gap `24px`, footer → `1fr 1fr`, nav links hidden, hero → `72px 0 48px`.
- `body { overflow-x: hidden }` contains glow overflow; hero actions `flex-wrap: wrap`.
- Overlays are `pointer-events: none` so scanlines never block clicks.
- Black text on cyan buttons keeps the CTA legible; dim `#8a8aa0` body text is the contrast risk on `#12121f`.
- No focus or reduced-motion rules.

# Part 17 — Dark SaaS in Practice

## 91. Tokens
- Layered surfaces: `--canvas: #010102`, `--surface-1: #0f1011`, `--surface-2: #141516`, `--surface-3: #18191a`, `--surface-4: #191a1b`.
- Hairlines: `--hairline: #23252a`, `--hairline-strong: #34343a`.
- Four-step ink: `--ink: #f7f8f8`, `--ink-muted: #d0d6e0`, `--ink-subtle: #8a8f98`, `--ink-tertiary: #62666d`.
- Single accent: `--primary: #5e6ad2`, `--primary-hover: #828fff`, `--on-primary: #ffffff`.
- Semantic: `--success: #27a644`, `--danger: #e5484d`.
- Shape and focus: `--radius-card: 10px`, `--radius-btn: 8px`, `--focus-ring: 0 0 0 2px rgba(94, 106, 210, 0.4)`.

## 92. Type Setup
- System sans stack; body `14px` / `1.5` / `letter-spacing: -0.05px`.
- Tracking in px, tighter as size grows: `.display-xl` `72px` / `600` / `1.05` / `-3px`; `.display-lg` `48px` / `-1.8px`; `.display-md` `36px` / `-1px`; `.headline` `28px` / `-0.6px`; `.card-title` `20px` / `500` / `-0.4px`.
- Eyebrow `13px` / `500` / `0.4px` uppercase in `--primary`.
- Mono `13px` / `1.5` / `letter-spacing: 0`; code `12.5px` / `1.65`.
- Metric numbers `32px` / `500` / `-1px`; price amount `40px` / `-1.5px`.
- No `clamp()`.

## 93. Layout & Section Order
- `.container { max-width: 1080px; padding: 0 24px }`.
- Order: sticky nav with Sign in + Get started → centred hero with terminal → 6-card feature grid → hairline metrics strip → config code → 3 pricing tiers → boxed CTA → footer.
- Section heads are left-aligned: `max-width: 640px; margin-bottom: 56px`, while the hero stays centred.
- Sections `padding: 96px 0`; feature and pricing gaps `16px`.
- Metrics left-aligned inside `border-top`/`border-bottom: 1px solid var(--hairline)`, `padding: 40px 0`.

## 94. Hero Treatment
- `padding: 112px 0 72px`; `h1` `max-width: 760px` with a forced line break; lead `17px` in `--ink-muted`, `560px` wide.
- Small buttons even in the hero (`9px 16px`); secondary carries an arrow `Read the docs →`.
- Hero note `12px` in `--ink-tertiary`.
- Product terminal: `--surface-1`, hairline border, `10px` radius, `margin-top: 72px`; title bar with one accent dot (`--primary`) and two `--surface-3` dots; success words in `--success`.

## 95. Components
- Buttons: `padding: 9px 16px`, `border-radius: 8px`, `14px` / `500`; primary is accent fill with hover `#828fff`; secondary is transparent with hairline border, hover `--surface-2` + `--hairline-strong`.
- Nav: `height: 56px`, `rgba(1, 1, 2, 0.85)`, `backdrop-filter: blur(8px)`, hairline bottom; links `13px`, gap `28px`; nav buttons `7px 13px` at `13px`.
- Brand mark: `22px`, `border-radius: 6px`, accent fill, `12px` letter.
- Card: `--surface-1`, `1px solid var(--hairline)`, `10px` radius, `padding: 24px`; icon `36px` with `8px` radius, `--surface-2` fill, hairline border, accent mono glyph.
- Badge: featured price card `::before { content: 'MOST POPULAR' }`, `top: -1px; right: 16px; transform: translateY(-50%)`, accent fill, `10px` / `600` / `0.8px`, `padding: 3px 10px`, `border-radius: 4px`; featured border becomes `--primary`.
- Price list items use `::before { content: '✓' }` in `--success` mono `12px` with `gap: 10px`.

## 96. Signature Effects
- Elevation by surface step (`#0f1011` → `#141516`) plus hairline, never by shadow.
- Semantic colour used sparingly inside product UI (green checks, green success tokens in terminal and code).
- Code tokens: keyword `--primary`, string `--success`, number `--ink-muted`, comment `--ink-tertiary` italic.
- No gradients, glows or textures.

## 97. Motion
- No keyframes; fast `120ms ease` transitions on `background` and `border-color` for buttons and cards.
- Card hover: `background: var(--surface-2); border-color: var(--hairline-strong)`.
- Nav and footer links fade from muted to `--ink`.

## 98. Responsive & Accessibility
- Visible keyboard focus: `.btn:focus-visible { outline: none; box-shadow: var(--focus-ring) }`, the only example with a focus style.
- `@media (max-width: 900px)`: `.display-xl` → `48px` with `letter-spacing: -2px`, `.display-lg` → `36px`, features and pricing → `1fr`, metrics → `repeat(2, 1fr)` gap `24px`, footer → `1fr 1fr`, nav links hidden, hero → `72px 0 48px`, sections → `64px 0`.
- Code `overflow-x: auto`; tertiary ink `#62666d` limited to notes and copyright.
- No reduced-motion rule.

# Part 18 — Glassmorphism in Practice

## 99. Tokens
- Backdrop: `--gradient-bg: linear-gradient(135deg, #0f0c29 0%, #302b63 45%, #24243e 100%)`, applied with `background-attachment: fixed`.
- Glass: `--glass-bg: rgba(255, 255, 255, 0.12)`, `--glass-bg-hover: rgba(255, 255, 255, 0.18)`, `--glass-border: 1px solid rgba(255, 255, 255, 0.25)`, `--glass-blur: blur(20px)`, `--glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.35)`.
- Text in white alphas: `--text: #ffffff`, `--text-muted: rgba(255,255,255,0.72)`, `--text-subtle: rgba(255,255,255,0.5)`.
- `--radius: 20px`; pills `999px`.
- Orb colours `#7c3aed`, `#06b6d4`, `#ec4899`; accent text `#a78bfa`.

## 100. Type Setup
- System sans; body `15px` / `1.6`.
- `.display-xl` `64px` / `700` / `1.05` / `-0.03em` with a soft halo `text-shadow: 0 0 40px rgba(255,255,255,0.15)`.
- `.display-lg` `44px` / `700` / `1.12` / `-0.02em`; card titles `20px` / `600`.
- Lead `19px` in `--text-muted`.
- Eyebrow is a glass pill: `12px` / `600` / `0.08em` uppercase, `padding: 6px 14px`, `border-radius: 999px`, glass fill, border and blur.
- Metric numbers `30px` / `700` with `text-shadow: 0 0 20px rgba(255,255,255,0.2)`.

## 101. Layout & Section Order
- `.container { max-width: 1000px; padding: 0 24px; position: relative; z-index: 1 }` above the orbs.
- Order: three fixed orbs → floating pill nav → centred hero with glass terminal → 3 glass feature cards → 4 glass metric tiles → glass code → 3 glass price cards → glass CTA → footer.
- Sections `padding: 88px 0`; heads centred `max-width: 600px; margin: 0 auto 52px`; grids `gap: 20px` (metrics `16px`).
- Every surface reuses one `.glass` utility so the system stays consistent.

## 102. Hero Treatment
- `padding: 104px 0 72px`, centred, `h1` `720px`, lead `520px`.
- Primary CTA is near-opaque white glass `rgba(255,255,255,0.92)` with dark text `#1a1a2e`; secondary is standard glass.
- Glass terminal: `padding: 28px`, toolbar divided by `rgba(255,255,255,0.15)`, one glowing accent dot `#a78bfa` with `0 0 10px rgba(167,139,250,0.8)`.

## 103. Components
- `.glass` primitive: glass background, glass border, `border-radius: 20px`, `backdrop-filter` and `-webkit-backdrop-filter: blur(20px)`, glass shadow; `.glass-pill` is the same at `999px`.
- Buttons: pill, `padding: 13px 26px`, `14px` / `600`, glass fill, border, blur and shadow; `.btn-lg` `16px 32px`.
- Nav: `position: sticky; top: 12px`, inner bar `padding: 12px 24px`, `rgba(255,255,255,0.08)`, `1px solid rgba(255,255,255,0.18)`, `border-radius: 999px`, `blur(18px)`, `0 8px 32px rgba(0,0,0,0.3)`.
- Brand mark: `32px` circle, `linear-gradient(135deg, #7c3aed, #06b6d4)`, `1px solid rgba(255,255,255,0.4)`, `box-shadow: 0 0 20px rgba(124,58,237,0.5)`.
- Feature icon: `54px` circle, `rgba(255,255,255,0.14)`, `1px solid rgba(255,255,255,0.3)`, `blur(12px)`, `0 0 24px rgba(255,255,255,0.08)`.
- Price list ticks: `::before { content: '✓' }` in an `18px` glass circle with `#a78bfa` glyph; featured card raises fill to `rgba(255,255,255,0.2)` and border to `0.45`.
- Code tokens: keyword `#a78bfa`, string `#7dd3fc`, number `#f9a8d4`, comment `rgba(255,255,255,0.4)`.

## 104. Signature Effects
- Light orbs behind the glass: `.orb { position: fixed; border-radius: 50%; filter: blur(90px); opacity: 0.55; z-index: 0; pointer-events: none }`; sizes `480px` (top-left violet), `420px` (right cyan), `380px` (bottom pink).
- Frosting depends on something colourful behind it: fixed gradient plus orbs keep the blur visible on every scroll position.
- Always pair `backdrop-filter` with the `-webkit-` prefix.
- White-alpha borders (`0.18–0.45`) define glass edges instead of solid strokes.

## 105. Motion
- No keyframes; orbs are static.
- Buttons: `transition: background 150ms ease, transform 150ms ease`; hover to `--glass-bg-hover` and `translateY(-1px)`; primary hover goes solid `#ffffff`.
- Feature cards: hover to `--glass-bg-hover` and `translateY(-2px)`.

## 106. Responsive & Accessibility
- `@media (max-width: 900px)`: `.display-xl` → `44px`, `.display-lg` → `32px`, features and pricing → `1fr` gap `16px`, metrics → `repeat(2, 1fr)`, footer → `1fr 1fr`, nav links hidden, hero → `72px 0 48px`, sections → `56px 0`.
- `body { overflow-x: hidden; min-height: 100vh }` keeps off-canvas orbs from causing horizontal scroll.
- Text alphas stay at `0.5` or above on a dark backdrop; the primary CTA is near-opaque to guarantee contrast.
- No fallback for missing `backdrop-filter`, no focus styles, no reduced-motion rule.

# Part 19 — Japanese Minimal in Practice

## 107. Tokens
- Paper and ink: `--paper: #fafaf7`, `--ink: #1a1a18`, `--ink-muted: #6b675e`, `--ink-subtle: #a09a8d`, `--line: #d8d5cd`.
- One spot colour: `--vermilion: #c3272b` (hover `#a81f23`).
- Secondary surfaces: white `#ffffff` for code and CTA, featured tier `#f4f2ea`.
- Spacing token `--space: 96px` drives section padding.
- No radius anywhere except the small dots.

## 108. Type Setup
- Serif-first: `--font-serif: 'Hiragino Mincho ProN', 'Yu Mincho', 'Noto Serif SC', 'Songti SC', 'SimSun', 'Noto Serif JP', Georgia, 'Times New Roman', serif` for body and headings; `--font-sans: 'Hiragino Kaku Gothic ProN', 'Yu Gothic', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', sans-serif` only for small labels and buttons.
- Body `15px`, very open `line-height: 1.9`, `letter-spacing: 0.02em`.
- Light, airy display: `.display-xl` `56px` / weight `400` / `line-height: 1.4` / `0.05em`; `.display-lg` `40px` / `400` / `1.45` / `0.05em`; card title `22px` / `500` / `1.5` / `0.04em`.
- Lead `16px` at `line-height: 2`; feature copy `14px` at `2`.
- Labels in sans with wide tracking: eyebrow `11px` / `500` / `0.3em` uppercase; nav links `12px` / `0.2em`; buttons `13px` / `0.15em`.
- Even code is set in the serif at `line-height: 2`.

## 109. Layout & Section Order
- Narrow measure: `.container { max-width: 960px; padding: 0 32px }`.
- Order: sticky nav → centred hero with seal, vertical inscription and hairline panel → feature list (rows, not cards) → hairline metrics → code → hairline pricing table → bordered CTA → footer.
- "Ma" (negative space): sections `padding: var(--space) 0`, heads `margin: 0 auto 64px`.
- Feature list rows: `grid-template-columns: 96px 1fr; gap: 32px; padding: 32px 0; border-bottom: 1px solid var(--line)`, indexed with formal numerals `壹 贰 叁` ("one, two, three").
- Pricing is one continuous table: `gap: 0`, top and bottom hairlines, `border-right: 1px solid var(--line)` between tiers, centred text.

## 110. Hero Treatment
- Very tall: `padding: 140px 0 96px`; `h1` `640px`, lead `480px`.
- Vermilion seal (a hanko-style stamp): `.seal` `44px` square, vermilion fill, white serif `15px`, `transform: rotate(-2deg)`, `user-select: none`, absolutely placed at `top: 96px; left: 24px`, bearing the character `信` ("trust").
- Vertical inscription in the margin: `writing-mode: vertical-rl`, `13px`, `letter-spacing: 0.4em`, `--ink-subtle`, at `top: 140px; right: -8px`, reading `静寂に進む — Relay 二〇二六` ("Advance in stillness — Relay 2026").
- Primary CTA is the only vermilion block; secondary is an ink hairline outline.
- Product panel: `1px solid var(--line)` only, `padding: 40px`, `8px` dots with the first in vermilion, title tracked at `0.15em`.

## 111. Components
- Buttons: square, `padding: 14px 34px`, transparent with `1px solid var(--ink)`; hover inverts to ink fill with paper text; `.btn-vermilion` fills vermilion and darkens to `#a81f23`.
- Nav: `height: 68px`, `rgba(250, 250, 247, 0.92)` (no blur), hairline bottom border; links gap `40px`; brand `17px` serif at `0.12em` with a `32px` solid ink square mark.
- Hairline rule utility: `.rule { border: none; border-top: 1px solid var(--line) }`.
- Metrics: hairlines top and bottom, `padding: 48px 0`, numbers `36px` weight `400`, labels sans `11px` at `0.15em`.
- Code block: white, hairline border, `padding: 32px`; keywords in vermilion, everything else muted ink.
- CTA: white, hairline border, `padding: 72px 32px`.

## 112. Signature Effects
- Hairlines (`1px #d8d5cd`) do all structural work; no shadows, gradients or blur.
- Single spot of vermilion per view (seal, primary button, first dot, code keywords, link hover).
- Slight hand-set imperfection: the seal's `-2deg` rotation.
- Vertical CJK text as a marginal decoration.

## 113. Motion
- No keyframes; only `transition: background 200ms ease, color 200ms ease` on buttons.
- Nav and footer links hover to vermilion.
- `html { scroll-behavior: smooth }`.

## 114. Responsive & Accessibility
- `@media (max-width: 900px)`: `.display-xl` → `36px`, `.display-lg` → `30px`, feature rows collapse to `1fr` with `gap: 8px`, metrics → `repeat(2, 1fr)`, pricing → `1fr` with vertical dividers swapped for `border-bottom` hairlines, footer → `1fr 1fr`, nav links hidden, hero → `96px 0 64px`, sections → `64px 0`, vertical inscription hidden.
- Document declares `lang="ja"`, which steers CJK glyph selection in the serif stack.
- High-contrast ink on warm paper with very generous leading aids long-form reading.
- No focus or reduced-motion rules.

# Part 20 — Neo-Neumorphism in Practice

## 115. Tokens
- Same-colour canvas and surfaces: `--bg: #e0e5ec`, `--bg-pressed: #dde2e9`.
- Low-contrast ink: `--ink: #5f6b7a`, `--ink-muted: #8a97a8`; never pure black or white in bulk.
- Soft accent `--accent: #6c9bd1`.
- Raised shadow: `--shadow-raised: -6px -6px 12px rgba(255,255,255,0.8), 6px 6px 12px rgba(0,0,0,0.12)`.
- Large raised: `--shadow-raised-lg: -10px -10px 20px rgba(255,255,255,0.85), 10px 10px 20px rgba(0,0,0,0.14)`.
- Pressed: `--shadow-pressed: inset 4px 4px 8px rgba(0,0,0,0.12), inset -4px -4px 8px rgba(255,255,255,0.8)`.
- `--radius: 20px`, `--radius-lg: 28px`; buttons `var(--pill, 999px)`.

## 116. Type Setup
- System sans; body `15px` / `1.6`.
- `.display-xl` `56px` / `600` / `1.1` / `-0.02em`; `.display-lg` `40px` / `600` / `1.15`; card title `22px` / `600` / `1.25`.
- Headings stay in the soft gray `--ink`, not black.
- Lead `18px` in `--ink-muted`; eyebrow `13px` / `600` / `0.05em` uppercase in accent.
- Metric numbers `30px` / `600`; price amount `34px`.
- No `clamp()`.

## 117. Layout & Section Order
- `.container { max-width: 1000px; padding: 0 24px }`.
- Order: floating pill nav → centred hero with raised panel → 3 raised feature cards → 4 pressed metric wells → pressed code well → 3 raised price cards → raised CTA → footer.
- Sections `padding: 96px 0`; heads centred `max-width: 600px; margin: 0 auto 56px`.
- Grids use a roomy `gap: 24px` so neighbouring shadows don't collide.

## 118. Hero Treatment
- `padding: 96px 0 72px`, centred, `h1` `680px` with a forced break.
- Primary CTA is not a filled colour: same-colour raised pill with accent text (`.btn-accent { color: var(--accent) }`).
- Product panel uses `.raised-lg` (`28px` radius, large shadow), `padding: 32px`; toolbar dots are `12px` raised circles, the first filled with accent; no divider line under the toolbar.

## 119. Components
- Surface utilities: `.raised` (`--bg`, `20px`, raised shadow), `.raised-lg` (`28px`, large shadow), `.pressed` (`20px`, inset shadow). No borders anywhere.
- Buttons: pill, `padding: 14px 28px`, `14px` / `500`, `--bg` fill, raised shadow; `.btn-lg` `18px 36px` at `16px`.
- Nav: `position: sticky; top: 16px`; inner bar `padding: 14px 28px`, `border-radius: 999px`, `--shadow-raised-lg`.
- Brand mark: `34px` raised circle with accent letter.
- Feature icon: `56px` raised circle, accent glyph `22px`.
- Metrics and code are pressed wells (inset shadow), contrasting with raised cards above.
- Price list ticks: `::before { content: '✓' }` in a `20px` raised circle, accent glyph `11px`; featured tier just gets `--shadow-raised-lg`.

## 120. Signature Effects
- Dual-light extrusion: white highlight top-left, dark shadow bottom-right, on an element the exact colour of the canvas.
- Raised versus pressed communicates hierarchy and state (content you act on is raised; read-only data sits in wells).
- No borders, gradients or blur; the footer even drops the divider line.

## 121. Motion
- No keyframes.
- Buttons: `transition: box-shadow 150ms ease, transform 150ms ease`; hover deepens to `--shadow-raised-lg`; `:active` (and `.pressed-state`) swaps to `--shadow-pressed` with `translateY(1px)` for a physical press.
- Feature cards: hover to `--shadow-raised-lg`.

## 122. Responsive & Accessibility
- `@media (max-width: 900px)`: `.display-xl` → `40px`, `.display-lg` → `32px`, features and pricing → `1fr` gap `28px`, metrics → `repeat(2, 1fr)`, footer → `1fr 1fr`, nav links hidden, hero → `64px 0 48px`, sections → `64px 0`.
- Contrast is the known weakness: `#8a97a8` on `#e0e5ec` is low, so it is kept for secondary text, and the accent appears as text colour rather than fill.
- Interactive affordance rests on shadow alone; add a focus ring and a visible text/colour cue for buttons, since none is defined.
- No reduced-motion rule.

# Part 21 — Vaporwave in Practice

## 123. Tokens
- Sunset sky: `--sky-1: #ff71ce`, `--sky-2: #b967ff`, `--sky-3: #3d2b63` (also the page background).
- Ink: `--ink: #ffffff`, `--ink-dim: rgba(255,255,255,0.8)`.
- Neons shared with cyberpunk: `--neon-cyan: #00f0ff`, `--neon-magenta: #ff00e5`, `--neon-yellow: #ffe600`.
- Glows: `--glow: 0 0 8px rgba(255,0,229,0.7), 0 0 24px rgba(255,0,229,0.4)`; `--glow-cyan: 0 0 8px rgba(0,240,255,0.7), 0 0 24px rgba(0,240,255,0.4)`.
- Dark purple glass fills: `rgba(30, 18, 60, 0.5–0.7)`; code `rgba(20, 10, 40, 0.8)`.
- Sun stripes `#ffd166` / `#ff9e5e`; radius `4px` buttons, `6px` panels.

## 124. Type Setup
- Display `'Arial Black', 'Helvetica Neue', Impact, 'Arial', sans-serif`; mono for UI; `--font-jp: 'Hiragino Kaku Gothic ProN', 'Yu Gothic', 'PingFang SC', sans-serif` for decorative Japanese.
- Body Helvetica `15px` / `1.6`.
- `.display-xl` `60px` / `900` / `line-height: 1` / `-0.02em` uppercase, magenta glow, and a slanted `transform: skewX(-2deg)`.
- `.display-lg` `42px` / `900` / `1.05` uppercase with magenta glow.
- Eyebrow mono `12px` / `700` / `0.3em` uppercase in neon yellow with `0 0 12px rgba(255,230,0,0.6)`, framed by `✦ … ✦`.
- `.jp-deco` `14px` with `letter-spacing: 0.5em`, `rgba(255,255,255,0.7)` and a cyan glow, carrying phrases such as `永遠の夜明け` ("eternal dawn") and `夢と現実の境界` ("the boundary between dream and reality").

## 125. Layout & Section Order
- `.container { max-width: 1040px; padding: 0 24px; position: relative; z-index: 2 }`.
- Order: a `.sky` wrapper holding sun, silhouettes, nav and hero → 3 glass feature cards → magenta-ruled metrics → cyan code block → 3 pricing tiers → glowing CTA with Japanese tagline → footer.
- The sky gradient covers only the top; the rest of the page sits on solid `#3d2b63`.
- Sections `padding: 88px 0`; heads centred `max-width: 560px; margin: 0 auto 48px`.

## 126. Hero Treatment
- Sky: `linear-gradient(to bottom, var(--sky-1) 0%, var(--sky-2) 55%, var(--sky-3) 100%)`, `padding-top: 60px`.
- Striped retro sun: `300px` circle at `top: 96px`, `repeating-linear-gradient(to bottom, #ffd166 0 14px, #ff9e5e 14px 22px)`, `box-shadow: 0 0 60px rgba(255,170,100,0.7)`, `opacity: 0.9`, `z-index: 0`.
- Silhouette row of emoji (temple, moai, palm) at `120px`, `color: rgba(20,12,45,0.92)`, anchored bottom with `gap: 8%`, `z-index: 1`.
- Hero `padding: 120px 0 96px`; text over everything at `z-index: 2`.
- Terminal as tinted glass: `rgba(30,18,60,0.55)`, `1px solid rgba(255,0,229,0.5)`, `backdrop-filter: blur(10px)`, magenta glow.

## 127. Components
- Primary button: magenta fill, white text, magenta border, `padding: 14px 28px`, `4px` radius, mono `13px` / `700` / `0.12em` uppercase, with glow.
- Secondary: transparent, cyan text, `1px solid rgba(0,240,255,0.7)`, cyan glow; hover `rgba(0,240,255,0.1)`.
- Nav: `rgba(30, 18, 60, 0.7)`, `blur(8px)`, `1px solid rgba(255,0,229,0.4)` bottom, `height: 60px`; brand prefixed with a cyan `■`.
- Cards: `rgba(30,18,60,0.5)`, `1px solid rgba(0,240,255,0.35)`, `6px`, `padding: 24px`, `blur(8px)`; icon `40px` circle with magenta border and `rgba(255,0,229,0.08)` fill.
- Pricing: magenta borders, featured tier switches to cyan border + cyan glow; names in neon yellow mono; list markers `::before { content: '✦ ' }` in magenta.
- Metrics: magenta hairlines top and bottom, numbers `34px` cyan with glow.

## 128. Signature Effects
- Perspective grid floor: `.sky::before` covering the bottom `42%`, two `1px` `rgba(255,255,255,0.35)` gradients at `background-size: 56px 56px`, `transform: perspective(420px) rotateX(62deg)`, `transform-origin: bottom`.
- Grid fades to the horizon with `mask-image: linear-gradient(to top, rgba(0,0,0,0.9), transparent)` (plus `-webkit-` prefix) and `opacity: 0.55`.
- Pink-magenta and cyan glows alternate between headings, buttons and panels.
- Faux-skew on the hero headline and decorative wide-spaced Japanese text.

## 129. Motion
- No keyframes (sun and grid are static).
- Buttons: `transition: box-shadow 150ms ease, transform 150ms ease`; primary hover `0 0 12px rgba(255,0,229,1), 0 0 36px rgba(255,0,229,0.6)` with `translateY(-1px)`.
- Cards hover to `--glow-cyan`; nav links hover cyan with glow; footer links hover magenta with glow.

## 130. Responsive & Accessibility
- `@media (max-width: 900px)`: `.display-xl` → `40px`, `.display-lg` → `30px`, features and pricing → `1fr`, metrics → `repeat(2, 1fr)` gap `24px`, footer → `1fr 1fr`, nav links hidden, hero → `88px 0 64px`, silhouettes → `80px`, sun → `200px` at `top: 140px`.
- `body { overflow-x: hidden }` keeps the sun and glows from widening the page; decor layers use `pointer-events: none`.
- Emoji silhouettes are decorative but not marked `aria-hidden`; add it.
- White text on pink sky is the weakest contrast zone, which is why hero text sits on glow and the terminal uses dark glass.
- No focus or reduced-motion rules.
