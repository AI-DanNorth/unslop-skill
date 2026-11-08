# Design Rules by Concept

Distilled from the `jakubkrehel/skills` collection (interfaces.dev). Each concept is followed by its rules. Exact values are given wherever the source gives them.

---

# Part 1: Mindset & Judgment

## 1. Evidence, Not Taste
- A finding needs evidence you can show: a clip, an overlap, a failed contrast pair, a broken mirror, a misread group.
- A value that merely differs from your preference is not a finding.
- A deliberate, consistent project convention (no shadows, a dense layout, a brand voice) is a preference, not a defect.
- The same detail done two different ways within one project *is* a finding.
- Never report a value you didn't measure, and never estimate a value you could compute.
- Never present a plausible value as measured. "Roughly 50px blur, unmeasured" is honest. A made-up value is not.
- A predicted failure is not a finding. Render it, or leave it out.
- "Feels a bit tight" is not a finding. "The gap is 12px and the design says 16px" is.
- When you couldn't check something, say it's "Not verified". Never imply coverage you didn't inspect.
- "Nothing to report" and "everything survived" are complete, valid results. Never pad.

## 2. Exact Values vs. Heuristics
- Requirements can be unconditional: thresholds, criteria, minimum sizes.
- For design heuristics, name the context and the escape conditions before giving a recipe value.
- Exact means exact: `cubic-bezier(0.2, 0, 0, 1)` is not `cubic-bezier(0.4, 0, 0.2, 1)`, and `0.96` is not `0.95`.
- Optical nudges and some cutoffs are starting points, judged by eye.
- Where the project has its own scale or tokens, use them instead of the generic starting numbers.

## 3. Prefer the Cheaper Fix
1. **Delete.** Remove a separator that space already carries, an animation on a high-frequency interaction, redundant ARIA, or a color ramp nothing uses.
2. **Use the platform.** A native element, a native control, the browser's focus ring.
3. **Reuse what exists.** An existing token, spacing step or motion curve.
4. **Correct the value** to the exact right one.
5. **Add** something new only last: a token, a wrapper, a media query, an attribute.
- If a change adds what a deletion would fix, that's itself a problem.

## 4. Foundations Before Polish
- Polish never outranks a broken interaction.
- Review in this order so foundational failures aren't hidden by polish: accessibility, layout, writing, typography, color, then UI polish.
- Visual polish applies only once the underlying interaction is sound.

## 5. Match the Project
- Write every fix in the project's own styling system (Tailwind, plain CSS, CSS-in-JS). Never impose a new stack.
- Reuse existing components, tokens, density, motion language and notation.
- Never invent new colors, spacing values or components when an existing one is close.
- Read the project's own design docs and conventions first. They settle matters of taste, but never excuse a real failure.
- When a shared token or guideline causes a problem, report it once at the source rather than once per component.

## 6. Severity & Ranking
- **High** blocks a task, misleads, hides content or controls, risks data loss, or is a repeated systemic failure.
- **Medium** meaningfully harms comprehension, efficiency, adaptability or consistency.
- **Low** is isolated polish with limited impact.
- Within a severity level, rank by reach. A token or shared-component fix outranks the same symptom in one leaf component.
- One root cause is one finding, listing every location it appears.
- Cap reviews at around 15 findings, with blockers always listed first.
- Report findings as **Before → After → Why** (which principle, which user impact).

## 7. Automatic Blockers (always high severity)
- An interactive control with no accessible name.
- A keyboard-reachable control with no visible focus indicator.
- Anything reachable by pointer but not by keyboard.
- Motion or autoplay that ignores reduced-motion preferences.
- Content clipped, overlapped or unreachable at 320px width or 200% zoom.
- Body or control text failing its required contrast ratio.
- State or meaning carried by color alone.
- A destructive action with no confirmation, no undo and no distinct treatment.
- Truncated content with no way to reach the full value.
- Content hidden past a scroll edge or behind a disclosure with no visible cue.
- An error that names no way to recover.
- A semantic color used against its meaning, such as the danger hue on a non-destructive action.
- A state change carried by motion alone, with no static cue left behind.

---

# Part 2: UI Polish: Surfaces & Icons

## 8. Concentric Border Radius
- Outer radius = inner radius + padding + border width.
- For example, an inner `12px` radius with `8px` padding means a `20px` outer radius.
- Never give a padded parent and its child the same radius.
- Past `24px` of padding, or with deliberately asymmetric padding, treat the layers as separate surfaces with their own radius tokens.

## 9. Optical Alignment
- When geometric centering looks off, nudge it by eye.
- Give a button about `2px` less padding on its icon side than its text side (e.g. `16px` start, `14px` end).
- Shift a play triangle toward its point (about `2px`).
- Fix asymmetric glyphs (stars, arrows, carets) in the SVG's viewBox or path. Only nudge the wrapper when the asset can't change.

## 10. Shadows for Elevation, Borders for Structure
- When a border exists only to create depth, replace it with layered transparent shadows.
- Keep borders on dividers, separators, table cells, selected states and form inputs (inputs need a 3:1 boundary).
- A light-mode shadow has three layers: a 1px ring, lift and ambient depth.
  - Base: `0 0 0 1px oklch(0 0 0 / 0.06), 0 1px 2px -1px oklch(0 0 0 / 0.06), 0 2px 4px 0 oklch(0 0 0 / 0.04)`.
  - Hover: the same layers at `0.08`, `0.08` and `0.06`.
- Depth shadows vanish on dark backgrounds, so dark mode uses one white ring: `0 0 0 1px oklch(1 0 0 / 0.08)`, and `0.13` on hover.
- Keep `border: 1px solid transparent` under a shadow ring. Forced-colors mode removes shadows, so the border still draws an edge and the box size stays stable.
- Transition the shadow on hover over `150ms` with `ease-out`.

## 11. Image Outlines
- Give content images a `1px` outline inset by `1px`: `outline-offset: -1px`.
- Use pure black or white at 10%: `oklch(0 0 0 / 0.1)` in light mode, `oklch(1 0 0 / 0.1)` in dark.
- Never use a tinted neutral, a palette near-black or the accent color, which shows as a colored fringe.
- Use outline rather than border so the image size never changes and the outline follows the radius.
- Skip transparent artwork such as logos and illustrations.

## 12. Icon Stroke Matches Text Weight
- Regular (400) text at 14–16px takes a `1.5px` rendered stroke.
- Medium or semibold (500–600) takes `2px`.
- Bold (700), or an emphasized standalone icon, takes `2.5px`.
- Widths are rendered pixels. A 24px-grid icon drawn at 16px scales its stroke, so use an absolute-stroke option or `vector-effect: non-scaling-stroke`.
- Use one icon library per surface, and never mix libraries in one toolbar.
- Size inline icons at `1em`–`1.25em` of the adjacent font size.

## 13. Icon States & Variants
- One SVG, recolored per state with `currentColor`. Never separate assets per state.
- Strip hardcoded fills and strokes to `currentColor`.
- Hover, selected and disabled states come from CSS color and opacity (disabled around `0.4` opacity).
- Use outline as the default variant and fill for the active or selected state (active tab, toggled bookmark, liked heart).
- Never use filled icons everywhere, or the active state loses its signal.

## 14. Icons at Render Size
- Test every icon at the smallest size it renders, often `16px`.
- Prefer a simplified glyph over scaled-down detailed artwork.
- Use the per-size grid (16, 20, 24) that matches the render size, so the icon stays crisp.
- Always use SVG, never raster.

## 15. Icons in RTL
- Flip icons whose meaning follows reading direction: back and forward arrows, navigation chevrons, text-alignment and list glyphs, volume waves, "send".
- Don't flip logos, checkmarks, physical objects (clocks, cups, pencils) or media playback.
- Use one flip mechanism per element, since two can cancel out.
- Analyze composite icons part by part. A badge may stay put while the base glyph flips.

---

# Part 3: UI Polish: Motion

## 16. Transitions, Not Keyframes, for Interactive State
- Transitions retarget and reverse mid-flight. Keyframes run a fixed timeline and snap or restart.
- Use transitions or springs for hover, toggles, open and close.
- Reserve keyframes for sequences that run once (entrances, loading).

## 17. Press Feedback
- A pressed button scales to `0.96` over `150ms` with `ease-out`.
- Never go below `0.96` (no `0.95` or `0.90`).
- Disabled buttons never scale: use `:not(:disabled):active`.
- Offer an opt-out (a variant or `static` prop) wherever the motion would distract.

## 18. High-Frequency Interactions Respond Instantly
- Keystrokes, row hovers and tab switches get instant feedback, or ≤`150ms` on opacity or background color only.
- Reserve expressive motion for infrequent moments: first load, success, empty states.
- Never replay a full entrance animation on every hover.
- Hover-revealed row actions and tab icon swaps change instantly.

## 19. Motion Is Never the Only Signal
- Every animated state change leaves a static cue: a color, icon or label.
- If the animation doesn't run, the state must still be clear.

## 20. Reduced Motion
- Run movement, scale and blur only under `prefers-reduced-motion: no-preference`, so motion is opt-in.
- Under reduced motion, replace motion with an opacity cross-fade rather than removing elements instantly.
- Kill parallax and autoplay entirely under reduced motion.
- Turn smooth scrolling into an instant jump, and start auto-rotating carousels paused.
- Keep loading spinners, progress, instant color changes, focus rings and brief press feedback.
- In libraries, use a global reduced-motion config, and branch manually for blur, which may still run.

## 21. Staggered Entrances
- Only for infrequent, staged entrances where sequence communicates hierarchy.
- Split content into semantic chunks: title, description, actions.
- Stagger the chunks `100ms` apart.
- Split a short display headline into words staggered `80ms` apart, where it should read word by word.
- Each chunk enters with opacity `0→1`, blur `4px→0`, and `translateY 12px→0` over `300ms` with `ease-out`.
- Never stagger routine interactions.
- Keep the hidden state in the `from` keyframe with `animation-fill-mode: both`, so an item whose animation never runs stays visible.

## 22. Exits
- Exits are shorter and smaller than entrances.
- A standard exit is opacity to `0`, blur `4px` and a fixed `-12px` translateY over `150ms` with `ease-out`.
- Never exit across the full container height or with dramatic scale.
- Slide fully out only when the destination carries meaning (a drawer closing, a card returning to a list): `-100%` over `200ms`.
- Remove instantly when the motion adds no information.

## 23. Entering From `display: none`
- Use `@starting-style` to supply the pre-enter style.
- Use `transition-behavior: allow-discrete` to keep the element rendered through its exit.
- The open state's duration (around `300ms`) applies on enter, and the closed state's (around `150ms`) on exit.

## 24. Skip State Animations on First Load
- Don't animate a default state in on page mount (icon swaps, toggles, tabs, segmented controls).
- Never apply that skip around an intentional first-time entrance, like a staggered hero.
- Check the component on a full page refresh.

## 25. Contextual Icon Cross-Fade
- Only for infrequent swaps: play/pause, copy/copied, like/liked, loading/success.
- Scale `0.25→1`, opacity `0→1`, blur `4px→0`.
- With a spring, use duration `0.3` and **bounce always 0**.
- Without a library, keep both icons in the DOM in one grid cell and cross-fade over `300ms` with `cubic-bezier(0.2, 0, 0, 1)`.
- Never add a dependency just for icon transitions.

## 26. Theme Switching
- Suppress every transition during a theme swap, or every color transition fires at once and the switch smears.
- Recipe: inject a no-transition style, switch the theme, force a style flush, then remove the style after the next frame.

## 27. Transition Only What Changes
- Name exact properties (`transition-property: scale, opacity`). Never `all`.
- `all` animates things nobody intended, such as colors on a theme flip, and re-runs layout on width and padding.

## 28. `will-change` Sparingly
- Add it only after you see first-frame stutter.
- Name the animated property (`scale`, `transform`, `opacity`, `filter`). Never `all`.
- Never use it on properties that don't composite (background, padding, color, width).
- Know the side effects: it creates a stacking context and becomes the containing block for fixed-position children (modals, tooltips).

## 29. Hover & Touch
- Put hover-only styling behind `@media (hover: hover)`. On touch, hover latches after a tap and looks stuck.
- When a control draws its own pressed state, set `-webkit-tap-highlight-color: transparent`.

## 30. Scroll Containment
- Give scrollable dialogs, drawers, menus and side panels `overscroll-behavior: contain`, so scrolling past their end never scrolls the page behind.

---

# Part 4: Typography

## 31. Fewer Fonts, Sizes & Weights
- Rarely use more than three fonts. Marketing pages can carry more than apps.
- Each extra size or weight dilutes hierarchy.
- Pair fonts for contrast. A serif headline over a sans body reads as deliberate, while two near-identical sans-serifs read as a mistake.
- Never propose a new typeface unless a type change was asked for.

## 32. Weight Floors
- Below `18px`, use weight `400` or heavier.
- Weights `100`–`300` belong at `28px` and up, and even there check them against the background.
- Load every face the design uses. Browsers fake missing weights and italics, distorting the face.
- Disable font synthesis only narrowly, for the specific mode, after verifying fallbacks.

## 33. Type Scale With Semantic Names
- Define a small set of sizes and deviate rarely.
- Pair each size with its line-height and weight, so a role is one decision.
- Name sizes by role on teams (`body-sm`, `title`), not just `sm`/`lg`.
- A starting product scale:
  - Display: `36px`, line-height `1.1`, weight `600`.
  - Title: `24px`, line-height `1.2`, weight `600`.
  - Heading: `18px`, line-height `1.3`, weight `600`.
  - Body: `16px`, line-height `1.5`, weight `400`.
  - Caption: `13px`, line-height `1.4`, weight `400`.
- Emphasis within a role is one weight step up (`400→500`), not a size change.

## 34. Heading Hierarchy
- Heading levels map to descending steps of the scale.
- A subordinate heading never overpowers its parent.
- Deep levels may share a size if weight or letter-spacing keeps them distinct.
- A heading is never smaller than body text, unless it's a deliberate overline.

## 35. Line-Height by Role
- Display text `1.1`, headings `1.2`–`1.3`, body copy `1.5`–`1.6`.
- Always unitless, so line-height scales with the font size.
- Tight line-height is for short text only. Anything that wraps to three or more lines needs at least `1.4`.

## 36. Letter-Spacing by Size
- Headings at `24px` and up take `-0.01em` to `-0.02em`.
- Uppercase labels at `14px` or smaller take `+0.05em`.
- Body copy stays at `0`.
- Always use `em`, never `px`.
- Never disable kerning.

## 37. Measure (Line Length)
- Cap long-form text at 60–75 characters per line.
- At a 16px body size that's roughly `560–680px`, or `65ch`.
- Recheck the cap if the body size changes.

## 38. Size Floors
- Long-form body text starts at `16px`.
- UI text can go smaller: inputs and menus at `14px`, captions at `13px`, rarely below `12px`.
- Set font sizes in `rem` so the reader's browser setting still applies.

## 39. Wrapping
- `text-wrap: balance` for headings and short descriptions, never paragraphs (Chromium ignores it past six lines).
- `text-wrap: pretty` keeps a lone word off the last line. It's safe on any paragraph.
- `overflow-wrap: break-word` where a long word, link or ID could escape the container.
- `white-space: nowrap` on labels and badges where a break looks broken.
- Keep interface text at `text-align: start`. Use `justify` only in specific editorial layouts.

## 40. Tabular Numbers
- Use `font-variant-numeric: tabular-nums` on timers, counters, prices and numeric table columns.
- Leave numbers in prose proportional.
- Right-align numbers in tables (`text-align: end`) and left-align text.

## 41. Truncation
- Single line: `overflow: hidden`, `text-overflow: ellipsis`, `white-space: nowrap`.
- Multi-line: line-clamp (needs `display: -webkit-box` + `-webkit-box-orient: vertical`).
- Every truncated value needs a way back to the full text.

## 42. Typographic Punctuation
- Store text in natural case and set case with `text-transform`, so a redesign never means rewriting copy.
- Use curly quotes in rendered text (straight quotes only in code).
- Use an en dash for ranges (`2010–2020`), an em dash for asides, and the ellipsis character `…` instead of three periods.
- Put a non-breaking space between values and units (`10 km`).
- Use soft hyphens or `hyphens: auto` with a correct `lang` for controlled word breaks.

## 43. Underlines
- `text-underline-position: from-font` and `text-decoration-thickness: from-font`, or tune by hand (e.g. `1px` thick, `3px` offset).
- A dotted underline hints that a word carries extra information (an abbreviation, a defined term).
- Only an underline's color animates reliably. Anything fancier needs a separate element.
- Never disable skip-ink.

## 44. Inputs at 16px on Mobile
- iOS zooms the page when input text is under `16px`, and doesn't zoom back out.
- Fix A: size up on mobile (`16px` small screens, the design size from the `sm` breakpoint up).
- Fix B: keep `16px` and render the intended size with `transform: scale()`, compensating width and line-height, with a wrapper drawing the field surface.
- Never disable zoom to fix it.

## 45. Font Rendering & Features
- Apply font smoothing once on the root (`antialiased`), never per component.
- Use CSS properties over raw tags: `font-weight: 650`, not `font-variation-settings: "wght" 650`.
- `font-variant-numeric: tabular-nums` and `slashed-zero` instead of raw feature tags.
- Leave optical sizing on `auto`.
- Use raw tags only for custom axes (`"GRAD" 80`) and features with no property (`"ss01"`).
- Use real small caps (`font-variant-caps`) and real super/subscripts (`font-variant-position`) when the font has them.
- Use the font's `Display` cut for large sizes and the `Text` cut for small.

## 46. Choosing Typefaces
- Serif for long passages and editorial reading.
- Sans-serif as the default for most interfaces, because it stays crisp at small sizes.
- Monospace for code and fixed-width identifiers. Numeric columns use tabular-nums instead.
- Display faces for large headlines only. Script faces for rare decorative moments.
- `system-ui` gives each platform's native face. A commercial brand face still needs a fallback stack.
- Ship `.woff2`.
- Fonts at the same size look different because of x-height: a larger x-height looks bigger.
- Static fonts can be smaller at 1–2 weights. Variable fonts win at several weights or axes.

## 47. Text Trimming
- In buttons and badges, text sits low because of the font's reserved space. Use `text-box: trim-both cap alphabetic` as a progressive enhancement.

## 48. Decorative Text in CSS
- Build drop caps, gradient text, outlines and text shadows in CSS so text stays selectable and searchable.
- Use the static cut for stroked text if a variable font shows overlapping contours.

## 49. Selection
- Keep text selectable by default.
- Brand the selection color only if it stays legible.
- Use `user-select: none` only on drag or gesture surfaces, never across the interface.

## 50. Language & Direction
- Set `lang` so quotes, hyphenation and pronunciation are correct.
- Set `dir` on the document and wherever direction changes.
- Wrap mixed-direction values (names, numbers, URLs) in `<bdi>`. Never reorder digits by hand.
- Short snippets follow the UI's direction. Paragraphs of three or more lines align to their own script.
- Mark brand names and code tokens as non-translatable.

---

# Part 5: Color

## 51. A System Is Ramps, Not Colors
- One neutral ramp, which carries 80–90% of the interface.
- One accent ramp for the brand, interactive and selected states.
- Only the status ramps the product actually renders (danger, warning, success, info).
- A second accent hue earns its place only when two things must be told apart at a glance.
- Never generate fewer neutral steps than accent steps.

## 52. Every Step Has a Job
- Map each ramp step to a role. The step numbers below use Radix's 1–12 scale.
  - Page background: 1.
  - Subtle background: 2.
  - Component background: 3.
  - Hover: 4.
  - Active or selected: 5.
  - Subtle border or separator: 6.
  - Border or focus ring: 7.
  - Hovered border: 8.
  - Solid fill: 9.
  - Fill hover: 10.
  - Low-contrast text: 11.
  - High-contrast text: 12.
- Don't generate steps that no role consumes.
- Put solid fills one step darker than the mid-tone (e.g. Tailwind `600`, not `500`), since white text on most `500` hues fails 4.5:1.
- Role-defined steps survive theme changes better than lightness-defined ones.

## 53. Building a Good Ramp
- Hold one hue from end to end.
- Lightness changes steadily, measured perceptually (OKLCH L), not HSL.
- Vividness peaks mid-ramp and falls toward nearly neutral at both ends.
- Steps are finer at the light end: about `0.04–0.05` L apart for the lightest steps and `0.07–0.10` mid-ramp.
- Adjacent steps closer than `0.03` L are redundant, so drop one.
- Never reach pure black or white at the ends.
- Build ramps with a color library and perceptual interpolation, never by eye.

## 54. Brand Color Placement
- A brand color for buttons belongs on the solid-fill step.
- Pin a contractually fixed brand color. Otherwise snap it onto the ramp for even spacing.
- If the brand color fails contrast with white text, keep it as the brand but use a darker step for interactive fills.
- Never quietly darken the brand.

## 55. Multiple Hues Together
- The same step must read equally bright across hues.
- Match vividness proportionally to each hue's own maximum, not by copying one number. Yellows and cyans peak lower.

## 56. Neutrals
- A pure gray ramp is a fine default.
- Tinting neutrals toward the accent (OKLCH chroma `0.005–0.02`) is a stylistic option, not a correction.
- Warm neutrals read approachable and editorial. Cool neutrals read technical and precise.
- Hold the same neutral temperature across the whole interface. Mixed warm and cool grays are visible.

## 57. Status Colors
- Follow convention first: red for danger, amber for warning, green for success.
- Keep every status hue at least `15°` of hue away from the accent.
- If the brand is red, give destructive actions a distinct treatment, such as an outlined button with an icon.
- Status ramps need only about four roles: background, border, solid fill and text.

## 58. Token Naming
- Two tiers. **Primitives** name a value by hue and step (`blue-600`) and are never used directly in components.
- **Semantics** name a job (`text-secondary`, `border-subtle`), point at primitives, and are the only tier components use.
- Add a third, component-level tier only for documented, intentional exceptions.
- Grammar: `color-{bg|text|border}-{variant}-{state}` for neutrals, and `color-{accent|danger}-{subtle|border|solid|text}-{state}` for hues.
- Pick one word per concept and never mix: `text` (not fg/foreground/ink), `bg`, `border` (not stroke/line), `accent` (not primary/brand).
- Reserve "primary" for "the most prominent of its group". Don't use it for the brand.
- Anti-patterns:
  - A hue in a semantic name (`blue-button`).
  - A location name (`sidebar-gray`).
  - Lightness words (`light-gray` lies in dark mode).
  - Numbered semantics (`text-2`).
  - A primitive used directly in a component.

## 59. Role Inventory (a complete system)
- **Surfaces:** page, surface, raised (menus, popovers), sunken (inputs, wells), overlay scrim.
- **Text:** primary, secondary, disabled, inverse, on-accent.
- **Borders:** subtle, default, strong, focus ring, separator. Separator and border are separate roles.
- **Accent:** subtle background, border, solid, solid hover, text.
- **Status:** subtle background, border, solid and text, for each status.

## 60. Use a Token Only in Its Role
- Never borrow a token because its value happens to look right, such as a border token used as a text color.
- If a role has no token, add one.

## 61. One Color, One Meaning
- Use one color for one purpose across the whole interface.
- Treat anything within `15°` of hue as the same color.
- The rule runs both ways: if the accent means "interactive", an interactive element rendered neutral is also misleading.
- Never let color carry meaning alone. Pair it with an icon or label.

## 62. One Filled Action per View
- Only one primary action gets filled color. Peers stay neutral.
- Put the color on the background, not the label. Accent text on a neutral button reads as a link.
- Several colored backgrounds are fine when they encode distinct states or categories.
- Selected states (active tab, checked segment) may use accent on the glyph and label.

## 63. Contrast Requirements
- **WCAG 2 AA:** text `4.5:1`, large text (≥24px, or ≥18.67px bold) `3:1`, UI components and graphics `3:1`.
- **WCAG 2 AAA:** text `7:1`, large text `4.5:1`.
- **APCA:**
  - Body text Lc 75, with Lc 90 preferred.
  - Labels and headlines Lc 60.
  - Large text Lc 45.
  - Fine icons Lc 45.
  - Solid icons and UI Lc 30.
  - Dividers Lc 15.
  - Disabled or placeholder text around Lc 30.
- Disabled controls and logos are exempt.

## 64. Measuring Contrast
- Measure against the background the element actually renders on (the card, not the page).
- Measure every pair in every appearance (light, dark, increased contrast).
- Translucent surfaces need testing against the lightest and darkest content behind them, or more opacity.
- Measure the rendered result of `color-mix`, opacity modifiers and alpha colors. Prefer solid tokens under text.
- Text over images or gradients is measured at the worst region, or given a scrim.

## 65. Fixing Contrast
- Report a failing pair. Don't change design colors unless asked.
- Change lightness first and hold hue, so a contrast fix doesn't become a palette change.
- Mid-lightness backgrounds cap what's achievable. Body text needs a background near light or dark.
- Reduce saturation if pushing lightness goes out of gamut.
- Pick text polarity by measuring both black and white. The neutral crossover sits near 56% OKLCH lightness.
- Always remeasure after a fix.

## 66. Dark Mode
- A dark palette is not the light one reversed. Reversal is only the starting point.
- Swap semantic roles first, then tune.
- Lower the accent's vividness by a step or two, or it reads as neon on near-black.
- Widen separation at the dark end, where steps collapse together.
- Recheck every contrast pair in dark mode.
- Use one switching mechanism throughout: the OS preference only, a class (if users can override), or `light-dark()`.

## 67. Increased Contrast Mode
- Give each appearance its own increased-contrast value. One shared override hurts dark mode.
- Widen the gap to the background by at least `0.15` L, then remeasure (aim for Lc 90 on body text).

## 68. Gradients
- The interpolation space is a look, not a correctness setting.
- sRGB has a muddy, darker midpoint. `oklab` keeps even brightness and is the best default. `oklch` stays vivid but routes through the hues in between.
- Opposite hues go gray in the middle in rectangular spaces. Switch to `oklch` or add a middle stop.
- Choose `shorter hue` (usually) or `longer hue` (a rainbow sweep).
- Large, low-contrast gradients band, so add contrast, shrink the area or add subtle noise.
- Keep text off gradients where possible.

## 69. Color Notation & Gamut
- Match the project's notation. Hex isn't wrong.
- For new systems, `oklch()` is the best default.
- Convert notation only as a deliberate migration, never as a side effect.
- Declare the sRGB value first, then a vivid P3 value inside `@media (color-gamut: p3)`.
- Over-vivid colors get clipped and flatten neighboring ramp steps.

## 70. Color Across Cultures
- Check the meaning of colors per locale. In Chinese finance UIs, red means gains and green means losses.
- Make gain and loss per-locale tokens where needed.

## 71. Auditing a Palette
- Collect every color literal, including SVGs, charts and email templates.
- Sort by perceived lightness within each hue family.
- Collapse near-duplicates (within about `0.02` ΔE). Keep the most-used one and never average them.
- Assign every survivor a role. A color with no role is a missing token or a mistake.
- Report the inventory before consolidating, since consolidation changes screens nobody asked about.

---

# Part 6: Layout

## 72. Group With Space, Not Lines
- Use negative space first, background shapes second, separator lines last.
- The gap between groups is at least **2×** the gap within one (e.g. `8px` inside, `16px`+ between).
- Use background shapes when a group must read as one unit (a selectable row, a draggable card).
- Use lines only for dense data (tables, long settings lists), as low-contrast hairlines.
- Never pair a separator with a big gap that already did the job.

## 73. Controls Look Like Controls
- Every interactive element gets a background shape, border, underline or a consistent zone (like a toolbar).
- A control styled like the text beside it doesn't read as a control.
- The inverse: a non-clickable badge shaped like a button collects dead clicks.

## 74. Align to Shared Edges
- Pick a small set of alignment edges and put everything on them.
- Use one spacing step per nesting level (`16px` is a good default).
- Watch for stray edges: an icon 2px off the text, a card padded differently from its neighbor.

## 75. Order by Importance
- The most important content sits near the top and the leading edge.
- Within a row, identifying content leads, and metadata and actions trail.
- Never bury the key number under secondary detail. Demote detail to collapsed sections, tabs or detail views.
- Visual order must match DOM order. Never reorder with `order`, `row-reverse` or grid placement.

## 76. One Primary Action per View
- Each view has one primary action.
- Put secondary actions behind a menu once there are more than three.
- Prefer a short view that links deeper over one long view showing everything.

## 77. Hint at Hidden Content
- Every off-screen or collapsed piece of content needs a visible cue.
- Let the next item peek `16–32px` past a scroll edge. A row ending exactly at the edge looks complete, so nobody scrolls.
- Name the content in disclosure controls: "Show 12 more results", not "More".
- Truncated values get an expand control, a detail view or a keyboard-reachable tooltip. A hover-only `title` doesn't count.

## 78. Control Spacing
- `12px` between adjacent bordered or filled controls.
- `24px` between the visible glyphs of borderless text or icon controls, because space is their only boundary.
- `24px`+ between unrelated control groups.
- Compact layouts can go tighter, as long as hit areas never overlap.

## 79. Inset Buttons From Edges
- Keep full-width buttons inside the layout margins (around `16px` inline on mobile).
- A button glued to the viewport edges looks like system chrome and clips against curved corners.
- Edge-to-edge actions only work when they follow platform chrome and respect safe areas.

## 80. Content Bleeds, Controls Float
- Backgrounds and media can extend to the viewport edges.
- Controls and text stay inside margins and safe areas.
- Safe-area insets need `viewport-fit=cover`, or they resolve to 0.
- Content scrolls beneath sticky chrome. Set `scroll-padding-block-start` to the header height so anchors and focused elements aren't hidden.

## 81. Responsive Structure
- Breakpoints come from content, not device presets. Break where the layout stops fitting.
- Hold the expanded layout until it breaks, then collapse.
- Prefer container queries for components, since a viewport query breaks a component placed in a sidebar.
- Test the smallest and largest supported sizes first.
- Write media queries in `rem`/`em`, so larger browser text triggers the narrow layout.

## 82. Plan for Growth
- Translated strings grow, and short strings grow proportionally most. A one-word button is the riskiest thing on screen.
- Size text containers with `max-width` and `min-height`, never a fixed width or height.
- Let rows wrap (`flex-wrap`).
- Test with pseudo-localization and a long locale like German.
- Fixed heights clip text at 200% zoom. Use `min-height`, or `max-height` with scrolling.

## 83. Layout Pitfalls
- Grid tracks and flex children won't shrink below their content: use `minmax(0, 1fr)` and `min-width: 0`.
- `100vw` includes the scrollbar and causes horizontal scroll, so use `100%`.
- `100vh` ignores mobile toolbars, so use `100dvh` for full-height panes.
- Give modals `max-height: 100dvh`, a scrolling body and actions outside the scroll area.
- Keep primary actions in stable chrome (a sticky footer or the top of the view), never where zoom, resize or the keyboard clips them.

## 84. RTL & Logical Properties
- Write direction-dependent layout as start and end: `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`, `float: inline-start`, logical radius properties.
- Keep physical left and right only for physical geometry such as safe-area insets.
- Flex and grid mirror automatically. Physical values, `translateX` and `background-position` don't, so they need RTL overrides.
- Sequences that encode progression mirror in RTL (star ratings, step indicators, progress bars).
- Digit order inside numbers never reverses.

---

# Part 7: Accessibility

## 85. Native Elements First
- Use `<button>` for actions and `<a href>` for navigation. Never `<div onClick>`.
- A real link supports Cmd/Ctrl/middle-click and copying the link.
- A "button" that navigates is a styled link. A "link" that acts is a styled button.
- No ARIA is better than bad ARIA. A wrong role is worse than none.
- Every ARIA role promises the full keyboard model and states.
- When unsure, take the platform default and remove ARIA rather than add it.

## 86. Focus Rings
- Style `:focus-visible`, not bare `:focus`.
- Prefer the browser's default ring. Adding just `outline-offset: 2px` keeps it.
- A custom ring uses a verified focus token and reaches 3:1 against every color it crosses.
- The ideal is a `2px` solid perimeter.
- Never use `outline: none` without a verified replacement.
- Preserve system colors in forced-colors (high contrast) mode.
- Use `:focus-within` to light up a wrapper, like a search box with an inner icon.
- A focused element must never be fully hidden behind sticky headers, footers or banners.

## 87. Keyboard Support
- Every pointer interaction needs a keyboard path.
- Escape closes overlays. Arrows move within composite widgets. Tab moves between widgets. Enter and Space activate buttons.
- Use `tabindex="0"` to join the tab order and `-1` for programmatic focus. **Never use a positive tabindex.**
- Composite widgets (tabs, menus, toolbars, radio groups) take one Tab stop with roving tabindex.
- Comboboxes keep focus in the input, using `aria-activedescendant`.
- Escape dismisses whatever opened last: tooltip, then menu, then dialog.
- Tabs activate automatically when panels render instantly, and manually (Enter/Space) when switching is expensive.

## 88. Dialogs & Focus Management
- Prefer a native `<dialog>` with `showModal()`, which gives an inert background and Escape for free.
- A custom overlay needs a dialog role, `aria-modal`, a name and an `inert` background.
- On open, focus the first focusable element. For destructive confirmations, focus the least destructive option.
- On close, return focus to the trigger, or to the nearest logical container if it's gone.
- On client-side route changes, update `document.title` and move focus to the new `<h1>` or `<main>`.
- Restore scroll position on back and forward, and scroll to top on new navigation.

## 89. Hit Areas
- The WCAG AA baseline is 24×24px (or enough spacing that a 24px circle around each target doesn't touch others).
- Aim for 44×44px on touch and 40×40px on desktop where density allows. Apple uses 44pt and Material 48dp.
- The visible element can stay small. Extend the hit area with a pseudo-element on the wrapper or button, never on the input.
- Anything that looks clickable must be clickable across its whole visible extent.
- Extended hit areas must never overlap. Shrink them to avoid collisions.
- Decorative layers (glows, scrims, sheens) get `pointer-events: none` so they don't swallow clicks.
- Every drag needs a single-pointer alternative (move up/down buttons, a menu).
- Pinch and swipe gestures need single-pointer alternatives.
- Scope `touch-action: none` to custom gesture surfaces only.

## 90. Disabled States
- Use native `disabled` for genuinely unavailable controls.
- Use `aria-disabled="true"` when the control should stay focusable and discoverable, and block activation in code.
- A natively disabled control can't show a tooltip, so put the reason in visible text nearby.
- Never set both disabled and aria-disabled on one element.
- Never disable submit to gate validation.

## 91. Forms
- Every input gets a real label. A placeholder is never a label.
- Label and control share one hit target, with no dead zone between a checkbox and its text.
- Mark required fields with native `required` plus a visible indicator, explained once per form.
- Use valid `autocomplete` tokens (`email`, `name`, `tel`, `street-address`, `cc-number`, `current-password`, `new-password`, `one-time-code`).
- Set the correct `type` and `inputmode` for the right keyboard. Codes and cards use `text` + `numeric`, money uses `text` + `decimal`, and true quantities use `number`.
- Turn off spellcheck on emails, codes and usernames.
- Never block paste.
- Accept free text, trim it, then validate. Never block or filter typing.

## 92. Errors & Submission
- Validate on submit, not by disabling submit.
- Mark failing fields `aria-invalid`, link the inline error with `aria-describedby`, and focus the first invalid field.
- Show errors inline beside their field with text or an icon, never a red border alone.
- Keep submit enabled until the request starts. Show a spinner beside the label ("Save" + spinner), not instead of it.
- Mark a pending button `aria-disabled` and ignore repeat clicks, since native disabled drops focus.
- Announce success politely. On failure, focus the first invalid field.
- Warn about unsaved changes before navigation.
- A re-render must never reset typed values or steal focus.

## 93. Accessible Names
- Icon-only buttons need a descriptive name that says the action ("Delete project"), not the glyph ("Trash icon").
- The visible label must appear in the accessible name, so voice users can say what they see.
- Prefer visible text or `aria-labelledby` over `aria-label`.
- Hide decorative elements with `aria-hidden`, never on or above anything focusable.
- Don't put aria-label on generic divs or spans.

## 94. Announcing Changes
- If focus moves there anyway, the move is the announcement.
- Field-specific messages use `aria-describedby`.
- Non-urgent updates (toasts, "Saved", result counts, loading) use a polite status region.
- Urgent, untied errors use an alert, and nothing else.
- Render the empty live region first, then update its text.
- Default to polite. Never move focus to a toast.
- For loading, mark the region busy, announce "Loading…", then the outcome ("Loaded, 12 results").

## 95. Alt Text
- Decorative or redundant images get `alt=""`, empty but present.
- Informative images describe the meaning.
- Functional images describe the action ("Search", not "magnifying glass").
- Images of text use the exact text, or better, real text.
- Complex images (charts) get a short summary, with the full data nearby.
- A missing alt is worse than an empty one.
- Decorative SVGs are hidden from screen readers. Meaningful ones get an image role and a label.

## 96. Structure & Navigation
- Headings describe their sections and form a coherent outline.
- Have one primary `<main>`.
- Add a "Skip to content" link as the first focusable element when nav precedes content.
- Label repeated landmarks ("Primary" and "Breadcrumbs" navs).
- Page titles go most specific first: "Billing · Settings · Acme".
- Headings are structure. Style the level with CSS, and never pick a tag by its size.

## 97. Timers & Autoplay
- Anything moving or updating on its own for more than 5 seconds needs a visible pause control.
- Toasts with an action, an error or needed information stay until dismissed.
- Auto-dismiss only low-stakes confirmations: at least 5 seconds, paused on hover and focus.
- Never put critical information (like the only undo link) in a timed element.
- Never autoplay with sound. Prerecorded video needs captions and audio needs a transcript.

## 98. Zoom & Reflow
- Content must survive 200% text resize.
- The page must work at 320px width with vertical scrolling only. Tables, maps and code may scroll inside their own container.
- Text containers use `min-height`, not `height`.
- Never set `maximum-scale=1` or `user-scalable=no`.

---

# Part 8: Writing (UX Copy)

## 99. Know the Existing Vocabulary
- Before writing, inventory the nouns for each object and the verbs for each action already in use.
- New copy uses those terms. Never name the same thing two ways ("Archive" in the menu, "Move to storage" in the toast).
- A multi-step flow uses one vocabulary throughout: "Get started", then "Continue" or "Next", then "Done".

## 100. Tone Flexes With Stakes
- Success, onboarding and empty states can be warm and light.
- Routine actions and settings are neutral and minimal.
- Errors and destructive confirmations are calm and plain, with zero playfulness.
- Data loss and security are serious and explicit.

## 101. Address the Reader
- Write "you", not "the user".
- Avoid "we" in errors, which reads as deflection: "Unable to load content. Check your connection and try again."
- Use possessives sparingly ("Favorites" beats "Your favorites").
- Never mix perspectives ("My account" beside "Your settings").

## 102. Plain Words
- Choose words a tired reader understands on the first pass.
- Delete every word that does no work.
- No idioms, colloquialisms or humor that won't translate.
- Skip unnecessary gender.
- Match the input: "tap" on touch, "click" with a pointer, "select" when both apply.
- Cut "successfully" and routine "please".

## 103. Build Strings Whole
- Never assemble sentences from fragments around variables, because word order changes per language.
- Use one message with placeholders and proper plural rules (many languages have more than two forms).
- Format numbers, currency, dates, relative time and lists through locale-aware formatters. Never build them by hand.

## 104. Buttons & Links
- Button labels start with a verb: "Send", "Save draft", "Delete project". Never "OK!" or "Let's go!".
- Link text makes sense out of context: "Read the billing docs", never "Click here".
- Suffix repeated links: "Learn more about exports".

## 105. Capitalization
- Pick title case or sentence case per element type and apply it everywhere.
- Sentence case is the default.

## 106. Settings & Toggles
- Label a toggle for its ON state: "Send read receipts", never "Don't send read receipts".
- Link straight to a referenced setting rather than describing the path to it.

## 107. Errors
- An error is an instruction that says how to fix it, placed next to where it broke.
- "Choose a password with at least 8 characters", not "Password too short".
- "Enter a date as DD/MM/YYYY", not "Invalid date".
- "Unable to save. Check your connection and try again.", not "Oops! Something went wrong."
- No blame, no "oops", no exclamation marks.
- Phrase hints positively ("Use at least 8 characters").
- Show known requirements as helper text before input.
- If the same error keeps firing, redesign the interaction.

## 108. Undo vs. Confirmation
- Prefer undo for frequent, reversible actions: act at once, then "Project archived. Undo".
- Confirm when an action is irreversible, affects others, or destroys many items.
- The confirmation title names the action and object: "Delete 'Q3 report'?", never "Are you sure?".
- The body says what's lost, with counts: "This permanently deletes the report and its 4 comments."
- Buttons are verb + object ("Delete project" / "Cancel"), never Yes/No.
- For accounts, workspaces and repositories, make the person type the name to confirm.
- When an action affects others, name who: "The 8 members of Design lose access."

## 109. Empty States
- Say what this place is and how to fill it, with one clear next action.
- "No projects yet" plus "Projects keep your tasks and files together" plus a "Create a project" button.
- A filtered empty state names the query and offers an exit: "No results for 'quarterly'. Clear filters".
- Never park persistent information in an empty state, because it vanishes once content exists.

## 110. Status Copy
- In progress: an `-ing` verb plus the object ("Saving changes…").
- Done: the object plus a past-tense verb ("Changes saved"). Keep it parallel with the in-progress string.
- Failed: what didn't happen, then the next step ("Changes not saved. Check your connection and try again.").
- Unavailable: why, and what unlocks it, beside the control ("Add a payment method to publish").
- Partial: counts for both outcomes ("9 of 12 files uploaded. Retry 3 failed files").

## 111. Placeholders
- Show a realistic example in the accepted format (`name@example.com`, `DD/MM/YYYY`), never an instruction.

---

# Part 9: Working Methods

## 112. Reviewing a Change
- Ask "did I make this worse?" Report what the change caused, and stay mostly quiet about what it merely touched.
- Read the whole diff before forming an opinion.
- A changed file's blast radius is every surface it renders in, so review those surfaces.
- A changed shared token or primitive reaches the whole product.
- Read the removed lines. Regressions are invisible in the new state: deleted labels, focus styles, reduced-motion guards, logical properties, contrast tokens, strings.
- Classify each finding as Introduced, Regression or Pre-existing. Pre-existing is a courtesy, capped at about three.
- A finding caused by the change is Introduced even in an untouched consumer.
- Hold the change to its stated intent, and look for what's absent:
  - A new variant missing some states (hover, focus, active, disabled, loading, selected).
  - A new string missing from translations.
  - A new component with no empty, loading, error, disabled or narrow state.
  - A control added to one surface but not its siblings.

## 113. Stress-Testing a Component
- Test one component at a time, rendered under every scenario that can actually reach it.
- Stress only what varies. Keep an axis only if the component accepts that kind of input.
- **Content length:** empty, one word, typical, several sentences, one unbreakable string (long URL, `Donaudampfschiffahrtsgesellschaft`).
- **Content shape:** emoji, RTL, mixed direction, diacritics and tall scripts, aligned numbers.
- **Quantity:** zero items, one item, the realistic count, 10× the realistic count.
- **Container:** a 320px container, squeezed by a sibling, very wide.
- **State:** loading, error, disabled.
- **Environment:** dark mode, zoom, reduced motion (toggled by the viewer, never simulated).
- Use the real component with the app's real fonts and tokens. Never a lookalike, and never a re-theme.
- Report what visibly broke, not what feels off.

## 114. Working Through Every State
- Find states in the code's actual branches:
  - Data: loading, empty, error, one item, typical, long, partial, stale.
  - Account: plan tier, role, owner vs. member.
  - Feature: flags, trials, limits reached, locked.
- A state the code can't reach isn't a state. List missing states rather than inventing them.
- Name states in the product's own words.
- Feed mock data at the data boundary without editing the component.
- Use product-shaped data in real quantities, never "Test item" ×3.
- Hold loading states still until switched. Never resolve them on a timeout.
- After any visual change, recheck every state. A fix for one often breaks another.

## 115. Exploring Variants
- Each variant is a different answer to the brief, not a different tint.
- Vary on one primary axis:
  - Structure: grouping, order, columns.
  - Density: spacing, how much fits.
  - Emphasis: where filled color goes.
  - Type: scale, weight contrast, measure.
  - Voice: labels, tone, amount of copy.
- Let secondary choices follow from the primary axis for coherence.
- Make three variants by default, five only when asked. Name them by direction ("Quiet", "Editorial", "Dense"), never "Option A".
- Every variant clears the same accessibility floor. It's never traded against a design axis.
- Judge on the real page with real neighbors and realistic data, one variant at a time at full size. Never as thumbnails.
- Note the width you judged at, since the answer can change between 375px and 1440px.
- Present each variant with when it's right and what it costs. Never mark a favorite.
- If asked to choose, answer from how often the piece is seen and the product's personality, not enjoyment.
- Comparison chrome (pickers, switchers) stays visibly outside the design system: a dark neutral surface and the system font.

## 116. Building From a Design
- The design decides. Take values from the design file, never from taste.
- A screenshot only gives ratios, so state the assumed scale and treat measurements as estimates.
- Map design values to existing tokens. Round to the nearest token and list what was rounded.
- Ask before rounding visibly changes the design: more than 2px on spacing or size, or a color landing on a different step.
- Never add tokens, variants or arbitrary values just to hit a number.
- Trust bound variables over raw values, linked components over name matching, and auto-layout gaps over absolute positions.
- Build only the frames, breakpoints and states the design shows. List the missing states.
- No "while I was here" cleanups. A diff wider than the design is the most common failure.
- Compare side by side, element by element, at each frame's width.
- If the design breaks an accessibility or other rule, build it as designed and report the conflict.

## 117. Explaining Someone Else's Interface
- Scope to the question: "how was this site built" covers the system, and "how was this effect built" covers the layer stack.
- Visual effects are stacks, not single declarations: an oversized element, a low-alpha gradient, a large blur, a backdrop-filter layer.
- Report layers in paint order with the declaration doing the work.
- Pseudo-elements (`::before`/`::after`) carry effects more often than elements do.
- Ignore idle animation values (`blur(0px)`, `opacity: 1`, `transform: none`).
- Many fractional gradient stops mean one generated eased gradient, not many choices.
- Tag every claim as measured, derived or inferred.
- Explain the mechanism and its perceptual job, not just the readout. For example, 85% of a fade landing in the first 300ms makes a layer arrive at once and never read as finished.
- Describe sets by rule: first value, last value and step.
- Close on a transferable recipe in words, plus what wouldn't survive copying (licensed fonts, tuned blur, brand hues).
- From a screenshot, colors and contrast are exact, while sizes are only ratios. Never claim a typeface. Describe its category and tells.
- Say what a screenshot can't show: states, motion, other widths, keyboard access, the other theme.
- To read a design system: tokens grouped by prefix, the type scale by usage, the spacing base unit, the number of distinct radii and shadows, transition curves, breakpoints vs. framework defaults, fonts and theming.
- Check a second state: a 375px width, the other theme, keyboard focus.

## 118. Verification Habits
- Without a browser, read every state from the code: hover, pressed, selected, loading, empty, with durations and easings.
- With a browser, walk every state, and replay motion at 10% speed.
- Check computed values, resize with real content, tab through flows and read the accessibility tree.
- Check every supported width, 320px, 200% zoom and the RTL mirror.
- Check light and dark mode at phone width.
- Read copy in locale files as well as components.

## 119. Improving a Product Unattended
- Every idea answers: would someone using this genuinely find it better? Name the person and the moment.
- Rank ideas by evidence of need: real 404 traffic, production errors, copy that promises something the product doesn't do, a fix already shipped in a sibling project.
- Generate widely (15+ ideas) before choosing. Include features, not just polish, and at least one surprising idea.
- Fix real user pain first, then features, then polish.
- Every change should read as if the owner wrote it: same components, tokens, file layout, voice and architecture.
- Keep everything reversible, with one change per commit.
- See each change working where a person would meet it, in light and dark themes and at phone width.
- Report what a user now sees and why, not commit subjects.

---

# Part 10: Technical Illustration

## 120. Evidence for Drawings
- Separate the subject from the style reference.
- Classify every feature: supplied geometry, estimated from a photo, hidden (omit or mark illustrative), fictional (label as concept), or abstract (build as layered plates).
- A style reference can't establish another object's internals.
- Invented dimensions stay invented. An illustration is never a manufacturing drawing.

## 121. Choosing Views
- Use an exploded axonometric to show how parts fit, with the assembled view one switch away.
- Use one parallel pictorial view for external shape.
- Use aligned orthographic views for specified dimensions.
- Use a section for internal passages.
- Use an exploded stack of plates for layered concepts (pixels, interface layers), with color telling the layers apart.
- Use the smallest view set that answers the question.

## 122. Exploded Views
- Explode along real assembly paths, starting from assembled positions. Zero offset must rebuild the assembly.
- Use 8–15mm of clear paper space between silhouettes.
- Keep stacks coaxial (screw, washer, cover, boss).
- Use fine chain lines for necessary trails only, connecting two visible locating features.
- Fasteners hover just clear of their holes.
- Explosions should reveal mating surfaces, not just spread shapes apart.

## 123. Line & Sheet Craft
- Draw near-black ink (`#202020`) on plain white paper, with open interiors and generous separation.
- Leaders and dimension lines at `0.16mm`, hatching and centerlines at `0.13mm`.
- Text: title `5mm`, labels `3mm`, metadata `2.5mm`.
- Build hierarchy with line width before reducing opacity.
- Use round caps and joins, and butt ends on dashed lines.
- Hatch sections at 45°, 2–3mm apart, varied between adjacent parts, with openings left clear.
- Put balloons (7mm) in perimeter lanes, with one elbow per leader and at least 2mm clearance from text.
- Dimension only established features. Start 10mm from the silhouette, then 7mm steps. Use `NTS` unless the scale is verified.
- Centerlines through holes, never background grids.

## 124. Concept Diagrams as Layers
- Give each idea its own part. An interface card becomes page, shadow, surface, image, text and button.
- Build layers from thin plates, with about a tenth of the plate thickness between them, so faces don't fight.
- Layers rest on each other rather than wrapping around.
- Repeat elements from shared parameters, so one change updates the whole grid.

## 125. Inspect Drawings at Two Distances
- At delivery size, the object should read before the annotations, and every label should be readable without zoom.
- At 3–4×, check junctions, curves, doubled edges, lines through solid faces, and leaders ending in empty space.
- Every balloon resolves to one item, and every listed item appears.

## 126. Viewer Pages
- Center the drawing on a continuous blank page, with no gallery, sidebar or contrasting canvas.
- Keep controls compact at the edges, with panels on demand.
- Bound zoom at 25–400%.
- Follow the system theme, allow an override, and apply it before first paint.
- The page and the drawing paper are identical, so there's no contrasting rectangle.
- Keep appearance separate from drawing state. Exports keep the chosen ink on white or transparent.
