# Design Rules by Concept

Distilled from the plugin87/ux-ui-agent-skills collection. Each concept is followed by its rules; exact values are kept wherever the source gives them.

# Part 1 — Philosophy & priorities

## 1. Decision priority order
- Rank every decision in this order: 1 User needs (is the task completable?), 2 Accessibility (POUR: perceivable, operable, understandable, robust), 3 Consistency (established patterns and tokens), 4 Aesthetics (balanced, intentional), 5 Developer experience (implementable, maintainable, composable).
- Never sacrifice a higher tier for a lower one: beautiful but inaccessible = broken; consistent but confusing = wrong pattern.
- Taste serves tier 4 (Aesthetics) only; a visual direction may sharpen anything below it but never overrides user needs, accessibility or consistency.
- A brand colour that fails contrast gets adjusted; taste never wins over POUR.
- When a taste rule and a system rule conflict, the system rule wins.
- Never sacrifice a working feature for aesthetics.

## 2. Systems thinking and shared vocabulary
- Think in systems, not screens: every output is grounded in design tokens, accessibility standards and production-ready patterns.
- Use a precise shared vocabulary (3-tier tokens, the 8 states, token by intent, POUR, focus ring, no colour-only, variance mandate) and name a problem with its term rather than a paragraph; a shared domain vocabulary means problems get named and solved correctly.
- Build small to large (Atomic Design): Atoms (indivisible: Button, Input, Icon) -> Molecules (atoms combined for one task: Form Field = Label + Input + Error) -> Organisms (complex sections: Header, Data Table, Modal) -> Templates (page-level layout: Dashboard, Auth, Settings, List/Detail) -> Pages.

## 3. The non-negotiables
- Token by intent: choose the token whose meaning matches the action.
- One theme, one source of truth: every page renders from the same token source through one CSS-variable layer imported once at the app root; no per-page palette; no hardcoded hex, px or timing.
- Every interactive element ships the eight states: default, hover, focus, active, disabled, loading (if async), error (if input), selected (mandatory when the thing can be selected).
- One thing leads: every screen has a first place for the eye; display type is at least 2.5x body size.
- Output completeness: a partial output is a broken output.
- Zero emoji, and never state a number you did not measure.

## 4. Design thinking process
- Follow the double diamond: Discover -> Define -> Develop -> Deliver.
- Diverge before converging: explore multiple solutions before committing.
- Validate at every fidelity level; user research is not optional.
- Study real reference screens first; matching an existing pattern beats inventing a new one; use real imagery, not grey boxes.

## 5. Inclusive design
- Design for the edges and the centre benefits.
- Treat WCAG 2.2 AA as the minimum, not the goal.
- Design keyboard navigation first, never as an afterthought.
- Never use colour as the only way to convey information.

## 6. Progressive disclosure
- Keep primary actions always visible.
- Put secondary actions one interaction away (menu, expand).
- Put advanced options behind an explicit "Advanced" disclosure.
- Make empty states guide users to the first action.
- Make error messages explain what happened AND how to fix it.

## 7. Correctness vs quality (honest scope)
- Correctness (tokens, contrast, states, no drift) is the floor, not the goal; a screen that is merely correct is not good.
- Objective checks (token consistency, contrast light and dark, keyboard, target size, reduced motion, responsive, no hardcodes, no emoji) prove correctness only; they never prove taste, and no automatic score or percentage covers beauty.
- Never state a quality number (contrast ratio, "WCAG pass", "100%", "all states OK") you did not actually measure on the render; say "not verified yet" otherwise.
- Re-measure after every edit; a measurement of a previous version does not count.
- Verify ALL states, not just resting: a button fine at rest can fail on hover, focus or active (specificity traps).
- A check that could not run (e.g. no renderer) measured nothing; never read "skipped" as a pass; report which checks were not run and why.
- Build with the rules from the start, then check, fix the cause and re-check until clean; never suppress a failing check; never announce success between failures.
- Render and look: checks pass while a UI is visibly broken; screenshot every state in both themes (transitions off, pointer parked off the UI), click every control and confirm the state actually changed, then seek critique.
- Typical defects that pass automated checks: a checkbox that will not toggle, a dash stuck at the bottom of its box, check mark and dash of mismatched stroke weight, an answer panel showing a grey band, unequal widths, no expand animation, a sort header that draws a chevron and sorts nothing, a tab that changes nothing, a dialog that traps nothing, a datepicker day drawn selected that never moves, an Export button styled live with no handler, a switch identical in both states.
- A control that declares a state (`aria-sort`, `aria-pressed`, `aria-expanded`, `aria-checked`, `aria-selected`, or a state-bearing role) must change something visible on a real click.
- A check that passes broken work is worse than a missing check: it turns a defect into a green tick.

## 8. Output completeness
- Treat a partial output as a broken output: deliver complete work, never placeholders ("... rest unchanged", "keep existing", "// ...").
- Asked for N components or screens, deliver all N; implement every in-scope token, state or breakpoint; do not stub.
- When length forces a split, split only at clean boundaries and continue to completion.

# Part 2 — Taste, brief inference & requirements interrogation

## 9. Decide before you generate (brief inference)
- Never open with default components; generated-looking work comes from generating before deciding.
- Before any markup or UI output, write the decision block (in the reply, not in your head), every line a decision:
- Domain: fintech, editorial, dev-tool, healthcare, consumer hardware... (sets density, restraint, trust cues).
- Audience and tone: expert vs first-time, calm vs energetic, premium vs utilitarian.
- Mood: the one adjective the result must earn ("expensive", "editorial", "precise", "warm", "brutal").
- Motion depth: none / subtle feedback / expressive choreography.
- Layout family: the named section sequence, varied per section.
- Reference anchor: an archetype or named design system to aim at.
- Vague values are non-decisions: "Mood: clean" is not a decision; "Mood: expensive" is.
- If you cannot name the mood and the layout family, you have decided nothing and the result will regress to the mean regardless of how many checks pass.
- Stop condition: if about to produce UI without the block written, stop and write it first; this holds even when the request never asks for it (e.g. a premium landing page).
- Decide taste up front; checks cannot see it, so it must be decided, not discovered.
- Do not apply an aesthetic direction the brief did not ask for.

## 10. Statistical slop (the core problem)
- Assume a model left to defaults regresses to the mean, and the mean is mediocre; treat each slop default as a defect to actively break, not a starting point.
- Ask before shipping: what would a critic reject first? Argue against your own work.

## 11. Read before you ask
- Look first for an existing brief, project context document or reference folder of real screens.
- Look for an existing theme or token source; if one exists, the theme question is answered; do not ask it.
- Read neighbouring screens and components; framework, conventions and component inventory are usually visible.
- Keep only the questions the existing material genuinely cannot answer.

## 12. Question bank
- Purpose and lead: who is this for, and what is the one task they came to finish?
- What is the first thing their eye should land on? (Four equal cards means "nothing", a composition bug.)
- What does success look like for them; what have they done when they leave?
- Content reality: what does it look like with zero items, one item, four hundred items?
- What is the longest real string: a 60-character project name, a nine-digit amount, an email with no spaces to break?
- Which numbers are real and which placeholder? Placeholder shipped as real is a lie users catch.
- Irreversible actions: which actions destroy or cannot be undone, and what confirms them?
- What happens when an action fails; what does the user read and what can they do next?
- Theme and platform: new theme or existing? If new, which direction, and does dark mode ship too?
- What is the narrowest width this must survive (floor 280px unless the brief says otherwise)?
- Which framework is the deliverable; does it need RTL; AA or AAA?
- Scope and done: how many screens or components exactly; what is explicitly out of scope?
- What must be true before done: which checks, and is adversarial critique part of the bar?

## 13. Rules on asking
- Ask at most seven questions, in one round; a drip of one at a time is worse than a wrong assumption.
- Ask only questions whose answer changes the build; if both answers produce the same build, take the default and say so.
- Never ask what you can choose well; taste is the job; ask about intent, content and constraint; decide the rest.
- Spend about five minutes up front; screens built correctly from the wrong brief cause the most expensive rework (work scoring 14/14 on objective checks still came back as rework from critique).
- Interrogation removes ambiguity; it does not produce quality or score anything.

## 14. Stated assumptions
- Write every unasked decision as an assumption: what was assumed, the default taken, and the cost if wrong.
- Example default: no dark mode requested, ship both anyway when the theme is already dual (cost of including is zero; cost of retrofitting is not).
- An assumption held silently is indistinguishable from a guess.

## 15. Checkable brief format
- Fields: Goal (one sentence from the user's side); User and task; Deliverables (exact list; N screens means N); Lead (the one thing the eye lands on first); Content reality (empty/one/many, longest string, real vs placeholder); Irreversible (which actions, what confirms them, what failure reads like); Theme (source of truth, dark mode, brand direction); Platform floor (narrowest width, framework, RTL, AA/AAA); Out of scope; Assumptions (each with default and cost if wrong); Done when (checks that must pass and whether critique is part of the bar).
- Keep the brief outside the conversation, next to the work, so a later reviewer can argue against it.
- Sequence: interrogate the brief, then build, then run objective checks, then adversarial critique.

# Part 3 — Anti-AI-slop rules

## 16. Banned visual defaults and their fixes
- 6-line wrapped headings in a narrow column -> wide measure for display type (max-width ~18-24ch), short and punchy.
- Same left-text / right-image row repeated -> vary composition per section.
- Everything centred -> asymmetry on a real grid; centre sparingly and deliberately.
- Three or four identical equal-weight feature cards -> one item leads (more size, more weight, or its own row) and the rest go quieter; break symmetry with density, not only size; a denser typographic or list composition beats three bigger boxes.
- Cheap meta-labels ("SECTION 01", "FEATURE") -> real, specific microcopy or none.
- Invisible or low-contrast button text -> solid contrast and a deliberate button hierarchy.
- Generic drop shadow on every box -> restrained, layered elevation; most things are flat.
- Pure black `#000` on pure white `#fff` -> off-black on warm-white (or cool-white) surfaces from the theme.
- Rainbow of accent colours -> one primary, one accent max; neutrals carry the weight.
- Cramped vertical spacing -> generous macro-whitespace between sections.
- Default system spacing (8px everywhere) -> an intentional spacing scale with large jumps at section level.
- Default hardcoded indigo-to-blue or indigo-purple gradient -> banned.
- One radius applied to everything -> a radius language with deliberate variation by role; use more than one radius on the page.
- One flat shadow everywhere -> an elevation scale.
- Two near-duplicate greys a step apart doing the same job -> consolidate neutrals.
- Heading that is only bold body text (24px over 16px = 1.5x, or 24px over 14px = 1.7x) -> display type at least 2.5x body.
- Default system font stack with no intent -> choose a face with intent.
- Accent sprayed on everything so nothing is emphasised -> reserve the accent.
- A theme toggle that communicates nothing about its own state -> make state visible.
- A main region that is 80% whitespace reads as machine-generated -> fill with real, plausible content.

## 17. Colour tells (mechanical thresholds)
- Never ship a hardcoded indigo/violet -> blue `linear-gradient` (hue 235-290 combined with 200-250); tokenise gradients or use a flat surface; this is the highest-priority tell.
- Never use pure `#000` text; use a tinted near-black token; avoid pure `#000`/`#fff` as text or background unless explicitly whitelisted with an allow marker.
- Cap distinct hex colours per source unit at 6 and distinct accent hues per page at 6 (target: one primary plus at most one accent; neutrals carry the rest).
- Collapse near-duplicate neutrals (RGB channel-sum distance 1-9) into one token.
- Never use opaque or heavy black shadows (rgb 0,0,0 with alpha >= 0.4); shadows are soft and slightly tinted.
- Destructive actions never wear the primary accent; this covers delete, remove, revoke, destroy, discard, erase, deactivate, terminate, wipe, unpublish, uninstall, drop, unsubscribe, cancel subscription/plan/account/membership/order/booking/reservation/shipment/invoice/payment/transfer/request/job/build/deployment/run, close account, leave team/workspace/organization.
- Affirmative actions (save, confirm, continue, submit, publish, apply, create, send) never wear the danger accent.
- The same destructive label uses the same accent everywhere (no red trigger with a blue confirm); a neutral or ghost destructive control is acceptable.
- A bare "Cancel" (dismiss) is not destructive.
- Only one primary fill per screen region; secondary actions are neutral, never a coloured fill.

## 18. Shape and elevation tells
- Do not give every rounded box the same radius (flags at >= 10 rounded boxes sharing one value); vary card > button > input/tag.
- Do not use the boilerplate shadow `0 1px 3px rgba(0,0,0,.1)` (0px 1px 2-3px at 10-19% black); use the elevation token scale.
- Do not use only one shadow across a page; resting, hover and overlay must differ.
- Never put a thick (>= 2px) coloured border on exactly one side of a card, alert, toast or callout, nor a four-sided border with one odd-coloured side; neutral dividers and tab underlines are not violations.

## 19. Spacing tells
- Do not use one padding value everywhere (flags at >= 10 padded boxes sharing one value); outer/container padding must exceed inner padding.
- Keep >= 8px between adjacent controls, badges or boxed cards, stacked or side by side, including after wrapping on a phone; a label may sit 4px from its own control.
- Boxed siblings starting on the same row end on the same row (no stray `align-items: start`); spanning bento tiles are exempt.

## 20. Typography tells
- Largest heading must be >= 2.0x body size (fails below 2.0x; premium target >= ~2.5x); 24px over 16px (1.5x) is bold body text, not display type.
- Make display type dramatically bigger and shorter; display type must say something (not "Welcome").
- Constrain body paragraphs to 60-75ch (`max-width: 65ch`); fail anything wider than ~80 real characters measured in the element's own font.
- Never `text-align: justify` body text (rivers).
- Keep h1/h2 headings to <= 12 words (longer wraps past 3 lines).
- No lorem ipsum or "placeholder text" shipped as content.

## 21. Composition tells
- Avoid 3+ equal-size, equal-class large sibling blocks (>= 160x110px) on marketing or feature sections; one item leads; acceptable in dashboard metric rows only when one metric still leads.
- Pricing: never three equal-weight plans with no recommended option.
- Never four equal stat cards; it is the loudest tell that nobody designed the screen.
- Ban symmetric everything: three identical cards, every section centred, one repeated row.

## 22. Emoji ban (absolute)
- Never emit an emoji or decorative pictograph (magnifier, check mark, warning sign, coloured circles, smileys, ballot boxes, dingbat ticks and crosses) in UI, code, data, copy, comments, commit messages or chat: not as icon, bullet, status dot, rating face, section marker, label, decoration or "polish".
- Replace every would-be emoji with a real icon (an icon set such as lucide as inline SVG, `currentColor`, consistent grid and weight) or plain words ("Warning:", "(pass)", "Search").
- When script swaps a button label, swap the SVG icon, never inject an emoji or text glyph string.
- When a reference brand uses a pictograph (a star rating, a heart), render it as an icon or words, never as the glyph.
- Illustrations in empty states are real icons or SVG, never emoji.
- Rationale: emoji are the number-one tell of machine-generated UI, read as a toy, and render differently on every platform.

## 23. Dash ban
- Never use an em dash or en dash in interface copy or instruction text; write a colon, a comma, parentheses, a period, or split into two short sentences.
- Hyphens in compound words ("two-factor") are fine.
- Only arrows and box-drawing characters are allowed as special Unicode in diagrams.

## 24. Copy and structure tells
- Ban marketing filler: "elevate", "unlock", "seamless", "effortless", "supercharge", "empower", "take it to the next level", "in today's fast-paced world", "updated in real-time"; say the concrete benefit.
- Ban hollow superlatives and triads ("powerful, intuitive, and beautiful"); name one specific, verifiable thing.
- Ban fake structure labels and placeholders: "SECTION 01", "FEATURE", "Lorem ipsum", "Your headline here", "Placeholder", "Item 1", fake data no real user would have.
- Ban over-hedged microcopy ("You may want to consider possibly..."); be direct and frontload the verb.
- Read copy aloud: if it sounds like a press release or a model warming up, rewrite it shorter and more specific.
- Say the concrete thing or say nothing.

## 25. One-sided coloured border ban
- Never put a coloured border on one side only of a card, alert, toast or callout, in any direction (left, right, top, bottom, or logical inline/block forms); the tinted 3-4px bar is decoration standing in for hierarchy the layout never established.
- Use a full hairline border on all sides, or surface and elevation separation instead.
- Carry status with a real icon plus text, never colour alone.

## 26. Native select ban
- Never ship a native `<select>`: its chevron sits hard against the control edge with no breathing room, and `appearance:none` fights the platform.
- Use a Listbox or Combobox pattern: a button trigger that announces the current value, a chevron placed with inner padding from tokens, full keyboard parity (typeahead, arrows, Home/End, Escape) and `aria-expanded` that really toggles something visible.
- The replacement loses free native accessibility, so it counts only after passing every state, keyboard and automated accessibility check.

## 27. Scaffolding never ships
- Never render non-product elements (preview checkbox, debug toggle, demo controls, "test" row) in the product screen; put them behind a query parameter or build flag.

## 28. Anatomy of a slop screen (what to recognise)
- Purple-to-violet 135deg gradient header (`#6366f1 -> #a855f7`) with white text and emoji in the title.
- Emoji as stat icons and as icon buttons (pencil, trash) at 16x16px (15.3x16 measured, under the 24px target floor).
- Four identical stat cards in `repeat(4, 1fr)`; nothing leads.
- Pure `#000` and `#ffffff` everywhere; system font only.
- Low-contrast grey labels (`#9ca3af` on white) for labels and deltas.
- A single 8px radius on every box; the same `0 4px 6px rgba(0,0,0,.1)` shadow on everything.
- Fixed `width: 1100px` container (+820px overflow at a 280px viewport).
- Heading 24px over 14-16px body (1.7x): bold text, not a display scale.
- Gradient primary button and a solid indigo "Delete Account" (destructive in the primary colour).
- Em dashes and "updated in real-time" filler in copy.

## 29. Anatomy of a golden screen (what to emulate)
- One shared theme (light + dark) with the full type scale 12/14/16/18/20/24/30/36/48/60/72px (`--text-xs..7xl`), 4px-based spacing (4 to 96px), radii 4/8/12/9999, control heights 32/40/48, disabled opacity 0.5.
- Zero raw hex, px or timing in components; every variable resolves.
- One hero metric card spans the full row at fluid display size (`clamp(36px, 9vw, 48px)`) with a stronger border and medium shadow; the other cards are quieter.
- Display type at a different size, not a bolder body (44/16 = 2.75x).
- Destructive wears the danger token everywhere it appears.
- Radius varies by component size.
- Modal primitive with focus trap, `role="dialog"`, `aria-modal`, `aria-labelledby`, Escape, return focus and backdrop.
- Button primitive with all 8 states, ARIA wired and dark-mode safe.
- Accent chosen by measured contrast against the canvas (warm orange `#ff8a3d` at 8.50:1 on `#08090a`) instead of the default indigo.
- Skeleton loading that still respects reduced motion.
- Responsive at multiple breakpoints; essential borders at 3:1; light and dark both AA.

# Part 4 — Composition & layout

## 30. One thing leads (focal point)
- Give every screen and every view a first place for the eye.
- Avoid four equal stat cards, three equal plan cards and grids of identical tiles: the eye lands nowhere and the screen reads as generated.
- Give the lead item more size, more weight or its own row and let the rest be quiet (e.g. a hero figure at 3x body size spanning the full row, then three deliberately different shapes such as donut, ranked bar list and sparklines rather than three identical cards).
- Display type is at least 2.5x the body size.
- Make primary actions keyboard reachable and the visual focal point.

## 31. Variance mandate (section archetypes)
- Never generate the same layout twice in a row; sameness is the loudest slop signal.
- Decide a varied layout sequence before building a multi-section page, choosing from: Bounded hero (oversized type, lots of air, single focal element, media capped); Asymmetric split (uneven columns such as 7/5 or 8/4, not 50/50); Bento grid (mixed tile sizes, gapless or tight, no empty dead cells, dense tiles only); Editorial stack (centred narrow measure for prose, wide for media); Offset / overlap (elements break the grid edge for depth); Marquee / full-width band (colour or media block that resets rhythm); Index / list (dense, typographic, table-like for specs or content).
- If two adjacent sections share the same column structure and alignment, change one of them.

## 32. Block coherence (iterative additions)
- Before adding a block, re-read what exists and match its contract.
- Reuse the established type scale, spacing rhythm, radius language, and the one primary + one accent; a new block never introduces a new colour, font or radius.
- Reuse existing primitives (Button, Card, Input); never hand-roll a parallel version with different padding or states.
- Vary composition, not vocabulary: layout differs from the previous block; materials (colour, type, depth, motion) stay constant.
- Keep density continuity: a sudden dense table after airy hero bands reads as bolted-on.
- Keep state and accessibility parity: same hover/focus/press/disabled treatment and dark-mode behaviour.
- Test: drop the new block next to an existing one; if a stranger could tell they were authored separately, it fails.

## 33. Screen economy (outranks any archetype or named system)
- Treat the viewport as scarce (most of all on phones) and bright area as costly (battery, especially OLED); keep large bright areas, heavy images and endless animation small and rare; large bright areas in dark mode are flagged.
- No full-bleed hero: media blocks (image, video, background-image) are capped at 60vh block-size (`media-max-block`); full-screen heroes show nothing the reader came for.
- Media never exceeds its container (`media-max-inline` 100%); wider than the viewport is a bug, not a bleed.
- No large hollow box: a card-like element covering more than 35% of the viewport must fill at least 30% of its own inner area (union bounding box) with text, controls or media; padding is not content.
- Bento only when tiles are dense; a bento of large mostly-empty blocks is the slop default with a trendy name.
- The first screen earns itself: at 390x844 the visible h1 and at least one primary action show without scrolling (component demo pages exempt).
- Every image has width and height; anything below the first screen is `loading="lazy"`; total image bytes per page stay under 500,000; prefer AVIF or WebP with `srcset` sized to rendered width.
- Nothing animates forever: no decorative infinite animation and no autoplaying background video unless a justified opt-out is documented with a written reason (> 15 characters).
- Every screen has a heading (h1), and an operational console offers a way to act on the first phone screen (e.g. counts in a top bar link to what they count).
- Keep these thresholds as tokens (`sizing.screen`) so a project can raise one deliberately.
- When a named brand system calls for full-bleed media, keep the identity (monochrome, type scale, stark contrast), cap the media, and state the adaptation explicitly; a silent adaptation is as bad as a silent override.

## 34. Composition truthfulness and endings
- An empty state owns the viewport it is in; a small centred block pinned under the header with ~1000px of nothing below reads as a page that failed to load; fill the space or centre within it and give the sparse case real content (what this will look like, what to do first).
- End a page on purpose: a footer, a summary line, a closing or secondary panel, something that says the content is finished rather than missing.
- Give a long list one differentiator per row (recency, status, a badge) so the eye has somewhere to land; forty identical cards read as one repeated.
- Feedback may not outrun the truth: a toast "Draft project created" over an unchanged list is a lie; change the data or change the copy.
- A region that scrolls sideways (e.g. a table) shows it visibly with an edge fade, shadow, scrollbar or arrow; an `aria-label` serves screen readers only.
- Never reuse disabled dimming for an in-flight action; keep the control at full strength and swap the label for a spinner.
- No silently clipped text and no overlapping controls.

## 35. Mobile-first
- Base styles ARE the phone layout; wider screens layer on with `min-width` queries.
- Use `max-width` queries only for a genuine narrow refinement or a range between two breakpoints, never as the way mobile gets supported; a desktop-first base with mobile patched afterwards is a bug.
- The `max-width` property is still right for reading measure, container caps and `max-width: 100%` on images.
- Test: strip every media and container query and render at 320px; a mobile-first page still fits.
- A fixed-px width that cannot shrink is a bug; every component survives 280px before earning a desktop layout.
- No horizontal document overflow at any width from 280px to 951px (check 280, 320, 382, 385, 414, 594, 669, 951), including at a 1.25x root font (proxy for other platforms' wider fallback fonts and users' larger text).
- Look at the 320px render before accepting the 1280px one.
- Interactive controls may not overlap by more than a quarter of the smaller one at 320/414/1280px; test with long content (60-character email, German compounds, pasted tokens, 10-digit figures).
- RTL must not introduce overflow absent in LTR.
- Use breakpoints at multiple widths, not a single 768px; KPI grids go 1 -> 2 -> 4 columns.
- On mobile, an opened sidebar pushes content down (switch the shell to block layout) rather than painting over it.
- On phones, drop the column a phone can lose (sparkline, derived value) instead of shrinking type below the scale, and note it.

## 36. Narrow-width defences
- An `<input>` keeps an intrinsic width of ~20 characters that sizes its grid column: set `inline-size:100%; min-inline-size:0`.
- A grid or flex item keeps `min-width:auto` and widens its own track: set `min-inline-size:0` on the item, or `grid-template-columns:minmax(0,1fr)`.
- One unbreakable token (email, URL, API key) sets min-content width: use `overflow-wrap:anywhere` (`break-word` alone does not shrink min-content).
- A `white-space:nowrap` tooltip or pill has no upper bound: set `max-inline-size:min(<n>rem, calc(100vw - <gutter>))`.
- A table without `table-layout:fixed` is sized by its cells' min-content.
- An absolutely positioned `.sr-only` span with no positioned ancestor resolves against the initial containing block and inflates scroll width inside a horizontal scroller; give it a positioned ancestor.
- Watch for a grid track collapsing (e.g. to 6px) while neighbours hold their floor, producing absurdly tall cards on phones without any overflow.
- A percentage block-size against an auto-height parent resolves to nothing (bars collapse to flat lines); give percentage-height children a definite-height ancestor.
- Replace fixed `inline-size:Npx` with `inline-size:100%; max-inline-size:Npx` (cap, don't pin).
- Replace `minmax(Npx,1fr)` with `minmax(min(Npx,100%),1fr)` when the minimum may exceed the viewport.
- Clear the default 40px inline-start list padding with `padding:0; margin:0` on every list (a margin reset does not clear padding; it also misaligns list edges against siblings).
- Make non-wrapping flex rows (breadcrumb, stepper, tabs) `flex-wrap:wrap`, or for tabs `overflow-x:auto` with tabs `flex:none`.

## 37. Foldables (dual-screen)
- Test the five iPhone Duo viewports (CSS px): outer upright 382; inner two windows side by side 385 each; outer on its side 594; inner upright 669; inner on its side 951.
- 382 and 385 are phone widths covered by a mobile-first base; 594-951 is where layouts grow from one to two columns and break when a breakpoint lands between them.
- One layout across the hinge is the default and fine for most visitors; never make the fold a requirement for the page to work.
- If you answer the fold (`@media (horizontal-viewport-segments: 2)` with `viewport-segment-width / left / right`), answer it fully: each pane gets exactly one segment, the gap equals the hinge, nothing readable or tappable sits on the hinge, and every `env()` keeps a fallback that is the unfolded layout.
- Detect the feature (media query, viewport segments API), never the device (user agent).
- Use list/detail as the natural split: list on one segment, selected item on the other; a three-column layout over two segments puts its middle column on the hinge.
- Reference hinge for emulation: a 40px band at 455-495px in a 951x620 half-closed pose.

## 38. Breakpoints, containers, grid and z-index
- Mobile-first `min-width` breakpoints: sm 640px (large phones, landscape), md 768px (tablets), lg 1024px (small laptops), xl 1280px (desktops), 2xl 1536px (large desktops).
- Container max-widths: sm 640, md 768, lg 1024, xl 1280, 2xl 1400px (narrower than its breakpoint for breathing room), prose 65ch.
- Columns: mobile 4 (< 640px), tablet 8 (640-1023px), desktop 12 (>= 1024px).
- Gutter: mobile 16px, tablet 24px, desktop 24px.
- Margin: mobile 16px, tablet 32px, desktop auto (centred with max-width).
- Sidebar widths: collapsed 64px, default 256px, wide 320px.
- Z-index scale: base 0, dropdown 10, sticky 20, fixed 30, overlay 40, modal 50, popover 60, toast 70, tooltip 80.

## 39. Responsive specification
- Document behaviour per breakpoint per major component: mobile (< 640px) single column, hide secondary nav, hamburger, touch gestures, bottom sheet for actions; tablet (640-1023px) 2 columns, icon-only sidebar, hover unreliable, larger touch targets; desktop (>= 1024px) 3 columns, full sidebar, hover, keyboard shortcuts.
- Patterns: Stack (horizontal to vertical: forms, card grids); Collapse (sidebar to hamburger or bottom nav); Priority+ (top items plus "More": tab bars, toolbars); Off-canvas (slide panel: details, filters); Truncate (truncate plus "Show more": long descriptions, tables); Transform (table to card list on mobile).
- Verify responsiveness at all breakpoints from 320px to 1536px.

## 40. Grid mechanics (fill space, avoid filler)
- Use `auto-fit`, never `auto-fill`, for card grids (auto-fill leaves phantom tracks so few cards cluster left): `repeat(auto-fit, minmax(min(Npx,100%),1fr))`.
- When item count is fixed and meaningful, use `repeat(3,minmax(0,1fr))` instead of auto-fit (auto-fit dropped the third gauge in a ~340px panel with a 7rem minimum) and give narrow widths their own rule.
- Never use auto-fit repeat for primary dashboard bands; it produces the equal-card wall; use a 12-column grid with explicit spans (e.g. 8/4) collapsing to 6 then 1.
- Equal-height panels in a row: `align-items:stretch` on the grid plus each panel as a flex column whose inner region is `flex:1`.
- Every panel in a row says how it handles slack: one child absorbs it (`grid-template-rows:auto minmax(0,1fr)` with inner tracks `minmax(<min>,1fr)`), rows share it (`align-content:space-between`), or the short column earns another panel; never end in a bordered void.
- Fix trailing gaps in toolbars by pushing the right cluster with `margin-inline-start:auto` rather than capped `flex:1` items.
- Fill dashboards with real, plausible content (stats row, activity list, chart), not one lonely widget; intentional density distinguishes designed from slop.
- Let flex rows wrap; reset list padding.
- Never reuse one class name across layout and colour.

## 41. Bands, whitespace and section rhythm
- One idea per band: a heading, at most one paragraph, one row or grid.
- Separate sections with large space (72-130px) and optionally a full-width hairline, not dividers between every element.
- Centre editorial section headers (title + one short paragraph); do not centre body content in grid systems.
- Constrain reading columns (e.g. a 568px single column, a 404px sign-up column).
- Full-bleed images may bleed on one side of 50/50 split blocks.
- Show product UI either as a faithful, lightly framed screenshot with an ambient shadow or dimmed and blended into a dark canvas; never a bright saturated screenshot in a dark hero.
- Hierarchy runs headline -> support text -> primary action; separate with whitespace before reaching for borders or shadows.

# Part 5 — Spacing & sizing

## 42. Spacing scale
- Use a 4px base unit; every gap and pad is a multiple of it (2px half-step allowed).
- Scale tokens: 0=0, 0.5=2, 1=4, 1.5=6, 2=8, 2.5=10, 3=12, 3.5=14, 4=16, 5=20, 6=24, 7=28, 8=32, 9=36, 10=40, 11=44, 12=48, 14=56, 16=64, 20=80, 24=96 (px); any 4px-grid value has a token.
- Use semantic spacing tokens for layout and scale tokens for component internals.
- Snap off-scale brand values to the nearest token and say which values changed.
- An alternative explicit scale is acceptable when it is a system (4/8/12/16/24/32/40, or a 5px scale 5/10/15/20/25/35/45/65/80/100/130); record recurring component-specific values exactly.

## 43. Semantic spacing tokens
- Page: inline-padding 16px (mobile), inline-padding-lg 32px (desktop), section-gap 64px, section-gap-sm 40px.
- Card: padding 24px, padding-sm 16px, gap 16px.
- Stack: xs 4px (icon + label), sm 8px, md 12px (field to label), lg 16px (between card sections), xl 24px (logical groups), 2xl 32px (major sections).
- Inline: xs 4px (icon gap), sm 8px (default), md 12px (button icon + text), lg 16px (between inline items).
- Component: button padding x16/y10, sm x12/y8, lg x24/y12; input padding x12/y8; badge padding x10/y2; modal padding 24px; table cell padding x16/y12.

## 44. Spacing hierarchy and rhythm
- Outer > inner: container/section padding > card padding > element gaps > element padding; never invert it (inner spacing equal to outer is a defect).
- Related items closer: proximity = relationship; tighten inside a group, expand between groups; distinguish internal gaps from between-item gaps (a card's 12px internal gap equal to the 12px gap between cards makes grouping read as one block).
- Establish a vertical rhythm on a chosen baseline and keep it throughout the page.
- Section seams get macro whitespace from the top of the stack scale; crowded sections read as cheap; sections never touch.
- Avoid one padding value everywhere; density is deliberate (row height, column padding and filter bar must not all share one value).

## 45. Rows, gaps and gutters
- Cards that share a row share a height and end on the same line; push a card's last line (note, action) to its bottom edge so endings align.
- The bug is usually an added `align-items:start` on a card row; remove it (the opposite of form-field rows, which need start).
- Exceptions: an item deliberately spanning two rows (bento lead tile); a plain text column beside cards (copy, not a card); a sticky column (must sit at top).
- The equal-height rule holds even when only one item draws a box (e.g. a tile at the end of a row of picture-led product cards).
- Nothing touches: buttons, fields, badges and cards keep at least 8px (`--space-2`) from neighbours, stacked or side by side, including after wrapping on phones (use `row-gap`, not luck).
- Exceptions: a label sits 4px (`--space-1`) from its own control; segments of one control (segmented button, stepper minus/value/plus) may join inside the box that draws them as one.
- One relationship gets one gap: if cards in a grid are 24px apart, every card in every grid like it is 24px apart; a label sits the same distance from its field on every form.
- The page has one gutter: section content starts on the same left edge from masthead to footer; a full-width band brings its content back to that edge.
- Avoid a short panel ending in a bordered void when grid rows stretch.

## 46. Form rows: equal controls, unequal content
- Give a row of fields `align-items:start` (or the field `align-content:start`) so a hint under one field does not stretch its neighbour.
- Give controls an explicit block-size from the size scale (not only `min-block-size`) so neighbours cannot stretch them.
- Watch the same trap in toolbar buttons, cards where one has a badge, and table cells where one column wraps.
- Verify by measuring: every control in a row reports the same rendered height.

## 47. Bento and edge tension
- Bento tiles vary in size but the grid stays mathematically exact: no empty or dead cells, no awkward leftover gaps; every tile earns its area.
- Let a small number of elements break the margin or grid edge for depth, only against an otherwise disciplined grid.

## 48. Density modes
- Support compact / default / spacious via `[data-density]`.
- Density is a multiplier on spacing and control sizing only (never colour or type): compact 0.875 (-12.5%) for data-dense enterprise UI; default 1; spacious 1.15 (+15%) for marketing and touch.

## 49. Sizing tokens: controls, icons, avatars, aspect ratios
- Control heights: xs 24px (minimum target, dense tables, chips), sm 32px (compact), md 40px (default), lg 48px (comfortable touch, recommended primary), xl 56px (hero CTAs).
- Target minimum 24px (WCAG 2.5.8 floor); 44px for primary touch actions.
- Icon boxes: xs 12, sm 16 (default inline), md 20, lg 24, xl 32px; stroke weight stays constant across sizes.
- Avatar sizes: xs 24, sm 32, md 40, lg 48, xl 64, 2xl 96px.
- Aspect ratios: square 1/1 (avatars, thumbnails), video 16/9 (embeds, hero video), portrait 3/4 (cards, posters), wide 21/9 (cinematic banners), golden 1.618/1 (editorial features).

# Part 6 — Typography

## 50. Font families and loading
- One family for UI, used with conviction: sans `Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif` for all interface text; weight and size create hierarchy, not extra fonts.
- Serif for editorial, long-form and marketing: `Lora, Georgia, Cambria, Times New Roman`; reserve serif and display faces for editorial moments.
- Mono for code, data and technical values: `JetBrains Mono, Fira Code, SF Mono, Consolas, Liberation Mono, Menlo`.
- Choose a face with intent; the default system stack with no intent is a tell.
- Substitute a licensed or open face for a proprietary brand font, keeping measured sizes, line heights and weights.
- Never `@import` web fonts in CSS (render-blocking); use preconnect + preload (or the framework's font loader) with `font-display: swap`; self-host when possible; preload one critical weight; subset glyphs; prefer variable fonts; take the family from a token.
- Never use a weight a font does not have (e.g. Lato has no 500/600).

## 51. Type scale and composite text styles
- Major Third (1.25) modular scale, base 16px (1rem = 16px): xs 12, sm 14, base 16, lg 18, xl 20, 2xl 24, 3xl 30, 4xl 36, 5xl 48, 6xl 60, 7xl 72 (px).
- Size type in rem; never lock `html { font-size }` to px.
- Use composite text styles rather than ad-hoc combinations.
- heading-1: 48px / 1 / bold / -0.05em (page titles).
- heading-2: 36px / 1.25 / bold / -0.025em (section titles).
- heading-3: 30px / 1.25 / semibold / -0.025em (sub-sections).
- heading-4: 24px / 1.375 / semibold (card titles).
- heading-5: 20px / 1.375 / semibold (widget titles).
- heading-6: 18px / 1.375 / semibold (smallest heading).
- body-lg: 18px / 1.625 / regular (lead paragraphs).
- body-base: 16px / 1.5 / regular (default body).
- body-sm: 14px / 1.5 / regular (secondary body).
- caption: 12px / 1.5 / regular / 0.025em (captions, timestamps).
- label: 14px / 1.5 / medium (form labels, table headers).
- overline: 12px / 1.5 / semibold / 0.1em, all-caps (category labels).
- code: mono 14px / 1.625 / regular.
- Line-height tokens: none 1, tight 1.25, snug 1.375, normal 1.5, relaxed 1.625, loose 2.
- Letter-spacing tokens: tighter -0.05em, tight -0.025em, normal 0, wide 0.025em, wider 0.05em, widest 0.1em.
- Marketing systems may use a fluid `clamp()` scale on a ~1.2-1.25 ratio.

## 52. Headings and display type
- Use exactly one h1 per page; never skip heading levels.
- Display type is a different size, not a bolder body: largest heading at least 2.5x body (e.g. 7xl/6xl over base); 2xl over lg or 24px over 16px is timid and reads as a template.
- Page titles at least 4xl (36px) over a 16px body to clear the bar; dashboards put the hero figure at 3x body.
- Display type is short and wide: measure ~18-24ch, line-height 1.0-1.15.
- Never let a headline wrap to 5+ lines; no heading past ~3 lines; shorten the copy or widen the container.
- Keep headlines sentence case; uppercase belongs to mono and label faces.
- Reserve extended or display widths for marketing headlines; never in nav, forms or footers.
- A document-like system may have no display type at all (max 19.2px on marketing); do not force a hero headline into it.
- An italic on the one emotional word of a headline is a valid emphasis device; never italicise the whole headline.

## 53. Measure and leading
- Body measure 45-75 characters, 65ch optimal (stricter taste range 60-75ch); enforce `max-width: 65ch`; flag lines past 75ch; long full-width lines are a readability and taste failure.
- Line heights: display 1.0-1.15; headings 1.1-1.25; reading text 1.35-1.5; body 1.5; caption 1.5.
- Never shrink type below the scale to fit dense content; drop columns instead.
- Fix scale contrast where display and body are too close.

## 54. Weight and hierarchy
- Weights: regular 400 for body, medium 500 for labels, semibold 600 for headings, bold 700 for page titles only.
- Build hierarchy with colour (ink vs muted) before size, and size before weight.
- Display type often stays at 400 (or light 100/300); bold headlines are a choice, not a default.
- Switch family (serif for editorial titles, a medium cut for actions) to create hierarchy instead of weight.
- Use non-standard variable weights where available (360 reading, 420 buttons, 480 headings) instead of 600/700.
- Pair a title in ink with a description in grey at the same size for tiles and captions.
- Never convey meaning by italics alone.

## 55. Tracking and typographic detail
- Track display sizes negatively by a fixed proportion: -0.02em (64px -> -1.28px, 52px -> -1.04px, 48px -> -0.96px) or -1% (62px -> -0.62px); sizes 24px and below at `normal`.
- Track uppercase labels positively (+0.09-0.1em; e.g. 1.7px at 17px, 1.98px at 22px); overline/eyebrow labels get generous tracking at a small size; mixed case stays at normal.
- Positive display tracking (+1-2%) is a deliberate brand inversion, not a default.
- Author capitals in the copy when uppercase is part of the brand voice rather than relying on `text-transform`.
- Apply `font-feature-settings: "case" on` globally in grotesk-led systems.
- Prefer optical alignment over metric: trim leading/trailing space, hang punctuation where it matters.
- Use tabular figures for data.
- Use dot-matrix or mono display faces only for short labels, never long paragraphs.

## 56. Small-is-default type systems
- In quiet commerce systems, 14px is the most-read size; 12px for utility, nav and badges; 16px for lead and price.

## 57. Thai and complex scripts
- Set Thai leading per font so one line's below-vowel room never reaches the next line's above-mark room (tone marks as in ที่, นี้, below vowel ุ): Sukhumvit Set ~1.35, Anuphan ~1.43, Noto Sans Thai ~1.49; Thai display leading >= ~1.45.
- Known failures: display at 1.25, a brand line at 1.2, a Thai line under an English name at 1.1, a heading at 1.3 in Sukhumvit Set (1.48 passed).
- Never apply negative letter-spacing to Thai; do not letter-space non-Latin text in general (font features and optical sizing differ per script).
- Never break Thai compounds or names across lines; never end a line on ความ, การ, ผู้ or ชาว; keep a noun prefix with its word, a number with its classifier or unit (23 คน), and a prefix with its number (พ.ศ. 2569) on one line with a `white-space: nowrap` span, including in script-built strings.
- Do not use `overflow-wrap: anywhere` or `word-break` on Thai; they do not help.
- Wrap only names, counts and compounds; wrapping every phrase makes the rag ragged on phones.
- Have a Thai reader check unknown compounds and place names.
- Choose fonts with the required script coverage (Arabic, Hebrew, Devanagari, Thai, CJK) and allow extra line-height for tall scripts (Thai and Arabic diacritics clip at tight leading).

# Part 7 — Color & tokens

## 58. Three-tier token architecture
- Primitive tokens: raw values (e.g. `blue.600 -> #2563EB`, `space.4`); never referenced directly in components.
- Semantic tokens: purpose aliases (`action.primary -> {primitive.blue.600}`, `text.secondary`, `surface.card`) used in designs and layouts.
- Component tokens: component-scoped (`button-bg-primary -> {semantic.action.primary}`, `input.border-focus`) used in component code.
- Build the token layer first, then components; a component never reads a primitive; if no semantic name exists, create one.
- Implement dark mode, brands and density by swapping semantic tokens; primitives stay stable.
- Token categories to cover: colour, typography, spacing, shadows (5-level elevation + inner + coloured + focus ring), borders (radius + width + semantic radii), breakpoints (+ containers, grid, z-index), motion, gradients, opacity (disabled, hover/pressed/selected overlays, scrim), blur (backdrop, frosted glass), sizing (control sizes, icon sizes, aspect ratios, screen-economy ceilings), states, theming (multi-brand + density), data-viz.
- A theme emits spacing, type, radius, shadow, font and transition variables, not only colours; include a scrim token.

## 59. Token naming and authoring
- Use DTCG format: every token has `$type` and `$value`; alias with `{dotted.path}`; preserve a description on every token.
- Name tokens `{category}.{property}.{variant}-{state}` by purpose, not appearance (`semantic.text.primary`, `component.button.primary-bg-hover`, `semantic.feedback.error-text`, never `red-dark`).
- Name props by meaning, not look: `variant="danger"` not `variant="red"`; `isLoading` not `spinner`.
- Before adding a token, reuse an existing semantic token with the same meaning; two names for one meaning kills a system.
- Add light and dark values together; a token in only one theme ships broken in the other.
- Change a value in one place; screens needing a different value get a new semantic token or theme override, never a local hex.
- Type the theme object so a token typo is a compile error.

## 60. Single-theme consistency
- Render every page, screen and component from one shared token theme via one CSS-variable layer (`:root` + `[data-theme="dark"]`) imported once at the app root; no per-page palette.
- Zero hardcoded hex, px, ms, font stacks or raw utility palette classes (e.g. `bg-gray-500`) in component and page code; only `0px` and `1px` are exempt raw lengths; the only other exception is adapter config that maps tokens into a third-party library's API.
- Every `var()` a component uses resolves to a defined theme token; a floating or dangling reference is a defect.
- Switching brand or theme is one edit at the source; a page that looks different bypassed the theme and is a bug.
- The token theme itself passes WCAG 2.2 in light and dark before any page ships (required text/action/border pairs fail the build; tertiary/decorative pairs are advisory).
- The component tier follows the dark map too (a secondary button at 1.13:1 dark-on-dark resulted when it did not).
- Even with a runtime CSS-in-JS theme, map tokens to CSS custom properties underneath so theme swaps are cheap and avoid re-render churn.

## 61. Token by intent
- Pick the token whose meaning matches the action, not any token that happens to resolve to the right colour.
- Destructive actions (Delete, Remove, Revoke, Cancel subscription) use `action.destructive` / `component.button.destructive-bg` everywhere they appear, trigger and confirm dialog alike; never `action.primary`; a blue Delete is a bug and an automatic fail.
- Primary = the one main affirmative action; secondary = neutral (transparent or outline, dark text, never a coloured fill, so no dark text on blue); danger = destructive.
- Use one canonical variant set (primary | secondary | danger | ghost); one action role -> one variant across all pages; a trigger and its confirm button match.
- Never style a non-destructive bulk action (e.g. "Mark all as read") as destructive.
- Keep destructive and primary colours distinct; they are never the same colour.
- A destructive label filled with a saturated colour outside the danger hue range is wrong-intent, themed or not.
- Automated checks do not catch intent mismatches reliably; check by hand.

## 62. Colour primitives
- Gray: 50 #f9fafb, 100 #f3f4f6, 200 #e5e7eb, 300 #d1d5db, 400 #9ca3af, 500 #6b7280, 600 #4b5563, 700 #374151, 800 #1f2937, 900 #111827, 950 #030712.
- Blue (brand default): 50 #eff6ff, 100 #dbeafe, 200 #bfdbfe, 300 #93c5fd, 400 #60a5fa, 500 #3b82f6, 600 #2563eb, 700 #1d4ed8, 800 #1e40af, 900 #1e3a8a, 950 #172554.
- Green: 50 #f0fdf4, 100 #dcfce7, 200 #bbf7d0, 300 #86efac, 400 #4ade80, 500 #22c55e, 600 #16a34a, 700 #15803d, 800 #166534, 900 #14532d, 950 #052e16.
- Red: 50 #fef2f2, 100 #fee2e2, 200 #fecaca, 300 #fca5a5, 400 #f87171, 500 #ef4444, 600 #dc2626, 700 #b91c1c, 800 #991b1b, 900 #7f1d1d, 950 #450a0a.
- Amber: 50 #fffbeb, 100 #fef3c7, 200 #fde68a, 300 #fcd34d, 400 #fbbf24, 500 #f59e0b, 600 #d97706, 700 #b45309, 800 #92400e, 900 #78350f, 950 #451a03.
- Purple: 50 #faf5ff, 100 #f3e8ff, 200 #e9d5ff, 300 #d8b4fe, 400 #c084fc, 500 #a855f7, 600 #9333ea, 700 #7e22ce, 800 #6b21a8, 900 #581c87, 950 #3b0764.
- White #ffffff, black #000000.
- Base palette shape: 6 hues x 11 shades + semantic + component + dark mode.
- When replacing the brand ramp, keep brand-600 at >= 4.5:1 against white so it can carry white text.

## 63. Semantic colour roles (light)
- Role set: actions (primary, primary-hover, primary-active, secondary, destructive, destructive-hover); text (primary, secondary, tertiary, disabled, on-action, on-dark, link); surfaces (page, card, raised, sunken, overlay, disabled); borders (default, strong, focus, error, disabled); feedback (success, warning, error, info, each split into bg/text/border/icon).
- Action: primary blue-600, primary-hover blue-700, primary-active blue-800; secondary gray-100, secondary-hover gray-200, secondary-active gray-300; destructive red-600, destructive-hover red-700.
- Feedback (bg/text/border/icon): success green-50/800/300/600; warning amber-50/800/300/600; error red-50/800/300/600; info blue-50/800/300/600.
- Feedback single-value variant: success green-600, warning amber-700, error red-600, info brand-600; colours read success green, warning amber, error red, info blue.
- Text: primary gray-900 (15.4:1 on white), secondary gray-600 (5.7:1 on white), tertiary gray-400 (placeholder and hint only, never essential info; alternative seed gray-500), disabled gray-300, on-action white (8.6:1 on blue-600), on-dark gray-50, link blue-600, link-hover blue-800.
- Surface: page white, card white, raised white (alternative seed gray-100), sunken gray-50, overlay rgba(0,0,0,0.5), disabled gray-100; scrim rgba(3,7,18,0.6) dims the page without hiding it.
- Border: default gray-200 (decorative dividers and card edges only, ~1.2:1, sub-3:1 by design, too low for essential control borders); strong gray-500 (4.8:1 on page; any border carrying meaning, meets 1.4.11); focus blue-500; error red-500; disabled gray-200.
- Interactive: hover-overlay rgba(0,0,0,0.04), active-overlay rgba(0,0,0,0.08), selected-bg blue-50, selected-border blue-200, focus-ring blue-500 (2px outline, offset 2px).
- All clickable elements use `action.primary` or `text.link`.

## 64. Component colour tokens
- Button: primary bg `action.primary` / hover / active with `text.on-action`; secondary bg `action.secondary` (or transparent neutral with a `border.strong` border, never a coloured fill) with `text.primary`; ghost bg transparent, hover `interactive.hover-overlay`, text `text.primary`; destructive bg `action.destructive` / hover with `text.on-action`; disabled bg `surface.disabled` with `text.disabled`.
- Input: bg `surface.card`, bg-disabled `surface.disabled`, border `border.default` (or `border.strong` for essential borders), border-hover `border.strong`, border-focus `border.focus`, border-error `border.error`, text `text.primary`, placeholder `text.tertiary`.
- Card: bg `surface.card`, border `border.default`.
- Badge (bg/text): neutral gray-100/gray-700, primary blue-100/blue-700, success green-100/green-700, warning amber-100/amber-700, error red-100/red-700.
- Avatar: bg gray-200, text gray-700, border white.

## 65. Dark mode strategy and values
- Design dark mode, don't invert it: dark surfaces, slightly desaturated accents, elevation through lighter surfaces rather than heavier shadows.
- Keep primitives fixed; swap only at the semantic tier.
- Light surfaces carry dark text and dark surfaces carry light text; both pass contrast; test every component state in both modes.
- Offer both light and dark and honour `prefers-color-scheme`.
- Text: primary gray-50 (`#f9fafb`), secondary gray-400 (`#9ca3af`; alternative gray-300), tertiary gray-500 (alternative gray-400), disabled gray-600, on-action white, link blue-400 (blue-600 is only ~3.9:1 on dark and fails), link-hover blue-300.
- Surface: page gray-950 (`#030712`), card gray-900 (`#111827`), raised gray-800, sunken black (alternative gray-950); scrim rgba(0,0,0,0.72).
- Border: default gray-800 (`#1f2937`, decorative), strong gray-500 (4.2:1 on the dark page, meets 3:1).
- Action: primary stays blue-600 (keeps white on-action >= 4.5:1; blue-500 = 3.68 fails), primary-hover blue-700 (darken on hover so white text stays >= 4.5:1), primary-active blue-800, secondary gray-800, secondary-hover gray-700, danger red-600 / red-700.
- Feedback in dark: success green-400, warning amber-400, error red-400, info brand-400.
- Tune link and primary-action colours per mode so both pass AA.
- On dark pages re-pick muted text (e.g. `#9b9d9d` / `#d8d9d9`) rather than reusing the light-mode grey, which fails on dark.
- Overlay shadows deepen in dark: light `0 20px 25px -5px rgba(0,0,0,.15), 0 8px 10px -6px rgba(0,0,0,.10)`; dark the same offsets at `rgba(0,0,0,.5)` and `rgba(0,0,0,.4)`.
- Do not sample or theme mid-transition; let theme switches settle; disable transitions before theme flips when measuring contrast.

## 66. Dark mode mechanics (web)
- Swap custom properties under `[data-theme="dark"]` and/or `@media (prefers-color-scheme: dark)`.
- Resolve the initial theme as stored preference, else system preference, and set the attribute or class on `<html>` in `<head>` before paint to avoid a flash.
- Persist a manual toggle in local storage.
- A theme toggle must change visibly (icon or text), not only `aria-checked`.
- Align library-native dark switches (e.g. Bootstrap `data-bs-theme`, MUI `palette.mode` / `colorSchemes`, Chakra colour mode, Mantine `defaultColorScheme="auto"`) with the app's `[data-theme]`.

## 67. Multi-brand theming
- Themes override SEMANTIC tokens only (re-point `action.*`, optionally the accent); primitives stay constant; apply via `[data-theme]` on web or theme objects on native.
- Default: primary blue-600 / hover blue-700.
- Violet: `#7c3aed` / hover `#6d28d9`.
- Emerald: `#059669` / hover `#047857`.
- Rose: `#e11d48` / hover `#be123c`.
- Add a theme by cloning the same override shape; light and dark are handled separately.
- Use multi-brand and density theming as override layers emitted as deltas only.

## 68. Palette generation (OKLCH)
- Generate new palettes in OKLCH for perceptually uniform shade scales.
- Define the brand hue (e.g. 264 for purple).
- Generate 11 shades from L=97% (50) to L=15% (950) with consistent chroma, plus a neutral ramp.
- Verify the 500 shade meets 4.5:1 on white for text use and the 600 shade meets 3:1 on white for UI use.
- Verify the strong border is at least 3:1 and that all required text/action/border pairs pass AA in light and dark.

## 69. Contrast requirements (WCAG 2.2)
- Normal text (< 24px): 4.5:1 minimum, AAA 7:1 (example: `text.primary` on `surface.page` = 15.4:1).
- Large text (>= 24px, or >= 18.66px bold): 3:1, AAA 4.5:1 (example: `text.secondary` on `surface.page` = 5.7:1).
- UI components and graphical objects, including icon-only controls: 3:1 (`border.strong` on `surface.page` = 4.8:1 for essential control borders; `border.default` at 1.2:1 is decorative-only).
- Focus indicators: 3:1 against every surface the ring can land on (page, card, raised) in both themes; a ring at 2.93:1 on a dark page, 2.34:1 on a card or 1.63:1 on a raised surface fails; use a lighter link-teal or blue-400 in dark.
- Required token pairs: text-primary on page and on card 4.5; text-secondary on page 4.5; link on page 4.5; text-on-action on action-primary 4.5; border-strong on page 3.0; check in light and dark.
- Advisory pairs: text-tertiary on page 4.5, secondary on raised 4.5, border-default on page 3.0.
- Disabled controls are exempt from contrast minimums; screen-reader-only clipped text has no contrast to meet.
- White text on a gradient has no measurable background (reads as 1.00:1); never.
- Chart palettes are tuned for large filled shapes, not text: 12px white initials on a chart colour measured 2.65:1 in dark; never use chart colours as text colours.
- Watch near-misses such as success-green chip text on a raised surface at 4.43:1; put colour on the icon and sign and keep text neutral.
- Pick accent-fill ink by measurement: near-black ink on bright orange (7.02:1) rather than white (2.9:1).
- Measure contrast on the real render (computed style against the alpha-composited background) in default, hover and focus, light and dark, for every text and interactive element; catch a secondary that picks up primary fill on hover; never eyeball.
- A brand hex that fails contrast is adjusted.

## 70. Colour usage and the one accent
- Never use colour as the only indicator; pair it with an icon, text or pattern.
- Limit the palette: 1 primary, 1 destructive, neutrals, and at most one accent used sparingly; neutrals carry the weight.
- Reserve the one chromatic accent for the single most important action per view or per viewport-height band; every other action is neutral, ghost, translucent or text.
- Do not introduce a second accent for buttons even when the token ramp contains other hues.
- Keep brand "object" colours (card art, wordmark, campaign colour, mascot) off the interface chrome.
- Colours that have only one step are used as flat fields, never as tints or ramps.
- Reserve status hues (red/green) for status meaning, never decoration; reserve legal/utility link colours for their scope (e.g. Terms/Privacy only).
- Let photography supply colour in greyscale or achromatic systems; never harmonise client or product imagery to the site palette.
- Calibrate, don't saturate: dial chroma down for large surfaces; reserve high saturation for small, intentional highlights.
- Use coloured shadows only on hover, and only on primary CTAs.
- Avoid theme-flipping tokens (chart colours, brand surfaces) behind white text or indicators; use dark-aware overrides or stable tokens (primary action, adaptive link colour) for avatars, active dots and selected states.
- No off-palette colours.

## 71. Near-black and off-white
- Use tinted near-black ink instead of `#000000` (e.g. `#333333`, `#151521`, `#1a1a1a`, `#21211f`, `#43423f`, `#040404`); reserve pure black for active/hover states, footers or full-bleed bands.
- Use off-white or tinted canvases instead of `#ffffff` where the brand is warm (`#fffef2` cream, `#f4f4f4`, `#f9f8f5` sand, `#f6f4ef`); slightly warm or cool neutrals read as designed.
- On dark canvases use a lavender or cool off-white ink (`#ededf3`) and a dimmer second ink (`#c3c3cc`); pure white only for labels on the accent fill.
- Translucent ink (navy at 60% `#09172399`; black at 60% `#00000099`) is a valid secondary text colour in place of a grey hex.
- Keep neutrals in one temperature family (all warm or all cool); never mix cool greys into a warm system.
- Avoid pure black on pure white for large text blocks (halation).

## 72. Opacity scale
- disabled 0.5 (paired with `pointer-events: none`); muted 0.6 (de-emphasised but legible); subtle 0.08 (hover state layer); pressed 0.12; selected 0.16; focus 0.24 (state layer in addition to the ring); scrim 0.6 (modal backdrop); ghost 0.04 (ghost buttons, zebra rows).
- Use the alpha scale instead of hardcoding rgba alpha.

## 73. Gradients
- One signature gradient per view, used sparingly, always from tokens.
- `brand.primary`: `#4f46e5 -> #7c3aed` (indigo to violet) for hero CTAs and brand surfaces.
- `brand.primary-soft`: `#6366f1 -> #8b5cf6` for large background washes.
- `surface.subtle`: `#0d0d15 -> #0a0a12` (near-flat dark depth, barely perceptible).
- `surface.scrim`: `rgba(0,0,0,0) -> rgba(0,0,0,0.6)` bottom-up image overlay for text legibility; photo overlays may step transparent -> 38% -> 56% black to keep white headlines legible.
- `feedback.success`: `#16a34a -> #22c55e`; `feedback.error`: `#dc2626 -> #ef4444`.
- `accent.aurora`: `#3b82f6` (0) -> `#8b5cf6` (0.5) -> `#ec4899` (1); decorative only, never behind body text.
- A hardcoded indigo-to-blue gradient remains banned; tokenised gradients are the only form allowed.

# Part 8 — Depth, radius, borders & effects

## 74. Elevation and shadow scale
- 5-level layered system plus inner, coloured and focus-ring shadows; higher = more prominence; depth corresponds to actual layering.
- none: level 0, flat.
- sm (level 1, cards at rest): `0 1px 2px 0 rgba(0,0,0,0.05)`.
- md (level 2, dropdowns, popovers): `0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px -1px rgba(0,0,0,0.1)`.
- lg (level 3, hover cards, sticky headers): `0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)`.
- xl (level 4, modals, dialogs): `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)`.
- 2xl (level 5, toasts, notifications): `0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)`.
- Inner sm (pressed buttons, inputs): `inset 0 1px 2px rgba(0,0,0,0.06)`; inner md (sunken containers): `inset 0 2px 4px rgba(0,0,0,0.08)`.
- Coloured (sparingly): primary `0 4px 14px rgba(37,99,235,0.25)` for primary CTA hover; success `rgba(22,163,74,0.25)`; error `rgba(220,38,38,0.25)`.
- Alternative seed: sm `0 1px 2px rgba(16,24,40,0.06)`; md `0 4px 12px rgba(16,24,40,0.08)`; lg `0 12px 32px rgba(16,24,40,0.12)`.
- Alternative constant-alpha elevation (16-24% alpha): `0 2px 8px`, `0 4px 16px`, `0 8px 32px`, `0 16px 48px`, `0 32px 64px`.
- Tint shadows with the theme foreground colour rather than pure black.

## 75. Depth strategy
- Default content to flat: no shadows on tiles, buttons or cards unless they genuinely float; most surfaces are flat.
- Build depth by layering (subtle surface elevation + hairline `border.subtle` + restrained shadow), not shadows alone; prefer 1px low-contrast hairlines to separate surfaces.
- Other depth sources: band colour stepping (white -> `#222222` -> `#000000`), surface fill steps on dark (`#171721` -> `#1e1e2a`), translucent glass over photography, full-bleed inverted bands.
- On dark, depth = lighter fills and translucency, never heavier shadows.
- When shadows exist, layer three very low-alpha shadows (2-9%), e.g. `rgba(28,28,35,.02) 0 10px 16px, rgba(28,28,35,.04) 0 6px 10px, rgba(28,28,35,.09) 0 0 3px`.
- Quiet systems use ambient glows (0 offset, large blur, 5-8% alpha, e.g. `0 0 34px rgba(0,0,0,.05)`) instead of Y-offset drop shadows.
- Reserve raised shadows for genuinely floating chrome: sticky header, carousel arrows, consent overlay.
- Put text directly on the darkest area of the art rather than in boxes over the art.

## 76. Radius scale and strategy
- Geometric scale: none 0, sm 4px, md 6px, lg 8px, xl 12px, 2xl 16px, 3xl 24px, full 9999px (`radius.full`, pill).
- Semantic radii: button 6px, input 6px (matches button), card 8px, modal 12px, badge full (pill), avatar full (circle), tooltip 6px, dropdown 8px, checkbox 4px, toggle full (pill track), image 8px.
- Alternative seed: sm 4px, md 8px (button), lg 12px (card), full 9999px.
- Pick a radius language (sharp / soft / pill) and apply it system-wide: 0px everywhere (luxury, editorial, gaming CTAs), 3-4px (utility, product), 8px tiles, full pills (500px/9999px) for consumer fintech and outdoor; random mixing looks accidental, but one radius on every card, button and input flattens importance.
- Vary radius by component size: chips 4px < buttons < tiles 8px < cards 12-32px < hero/footer 64px.
- Reserve 9999px/50% for pagination dots and circular media controls when buttons are square.
- Pill buttons in an account app and squares in a store are separate languages; never mix them on one surface.
- Radius may be platform-dependent: rectangular 4px on desktop, a 56px pill for the mobile marketing CTA.

## 77. Border widths and styles
- Widths: none 0, thin 1px (default: cards, inputs, dividers), medium 2px (focus rings, active tabs), thick 4px (sidebar indicator, branded borders).
- Styles: default 1px solid `border.default` (gray-200); strong 1px solid `border.strong`; focus 2px solid `border.focus` (blue-500); error 2px solid `border.error`.
- Essential input and control borders use `border.strong` at 3:1 against the surface.

## 78. Focus ring
- Double ring: `0 0 0 2px <surface>` then `0 0 0 4px <accent>` (light: `#ffffff` + `#3b82f6` or `#2563eb`; dark: `#030712` + `#60a5fa`); visible on light and dark; meets 2.4.7.
- Minimum: a 2px solid outline at 3:1 against adjacent colours with `outline-offset: 2px`.
- Retune the ring per theme rather than reuse action-primary, and measure it on every surface it can land on.
- Use `:focus-visible` (never bare `:focus`); suppress the default outline only when replacing it with the ring token; never `outline: none` alone.
- Never remove focus indicators, including under reduced motion.

## 79. Blur and glass
- Blur tokens: none 0; sm 4px (small popovers, tags over imagery); md 8px (default glass: cards, sticky headers); lg 16px (modal backdrops, nav overlays); xl 24px (full-screen scrims, immersive overlays).
- Glass is a once-per-view effect; use restraint.

## 80. Effects restraint and micro-detail
- Use glass/blur, gradients and glow each once, intentionally; never stack them.
- Do not mix unrelated visual metaphors.
- Treat focus rings, hover transitions, selection states, empty states and loading skeletons as the taste; their presence earns trust.

## 81. Hover, press and selected treatments
- Hover is a value shift (darken the fill, e.g. `#333333 -> #252525`, `#fc5200 -> #dd4800`), an opacity change (1 -> 0.5 on text buttons) or an underline toggle; in quiet systems never a lift or added shadow.
- Hover transitions run 0.25s ease-out on background-color and color in brand systems; style-family transitions sit at 150-250ms with stable easing.
- Underline inline links and remove the underline on hover (or the inverse); never change colour and decoration plus motion all at once.
- Selected states may use a thicker border (1px -> 2px) in the strongest ink rather than a colour fill.
- Active tab = strongest ink + 2px underline; inactive tabs in muted ink.
- State the hover mechanism explicitly (value shift, opacity, underline, fill change) with its duration and easing.

# Part 9 — Motion & choreography

## 82. Motion principles
- Purpose only: motion guides attention, shows a spatial or causal connection, or confirms an action; otherwise cut it.
- UI transitions run 100-300ms and never exceed 500ms (600ms entrances are a known trap).
- Every interactive element responds to hover, focus and press within 100ms.
- Animate only transform and opacity (GPU-composited, 60fps); never animate width, height, top, left, box-shadow or filter in hot paths or loops.
- Use `will-change` sparingly and only during the animation.
- Restraint reads as premium: one signature motion per view; stacking parallax + glow + spring + scrub looks cheap.
- Tokenise all durations and easings; never hardcode timing; derive stagger from a token (`duration-fast x 0.6 x n`), never typed ms.
- Never block content or delay interaction on animation.
- Prefer CSS state styling over script-driven animation.
- Animate value changes, not every re-render.
- Infinite animation is allowed only for real progress (inside `aria-busy` or a live region); decorative endless motion (floating blobs, looping backgrounds, idle shimmer, autoplaying video) is banned.

## 83. Duration tokens
- instant 0ms (reduced-motion fallback, instant swaps); fast 100ms (hover, focus, small colour/opacity changes); base 200ms (most state changes, toggles, dropdowns); moderate 300ms (modals, drawers, accordions, page sections); slow 500ms (maximum: full-screen transitions, large reveals).
- Feedback lands in fast to base; nothing routine exceeds moderate; only full-screen or hero transitions reach slow.
- Alternative seed: instant 100ms, fast 150ms, normal 250ms; default micro-transition 150ms ease-out; spinner turn 700ms.

## 84. Easing tokens
- linear `[0,0,1,1]`: only continuous loops (spinners, progress).
- ease-out `cubic-bezier(0, 0, 0.2, 1)`: entrances (arrive fast, settle); the default for most UI.
- ease-in `cubic-bezier(0.4, 0, 1, 1)`: exits.
- ease-in-out `cubic-bezier(0.4, 0, 0.2, 1)`: in-place state changes (toggles, reorders).
- spring `cubic-bezier(0.34, 1.56, 0.64, 1)`: rare celebratory or playful overshoot (success checkmarks, badges), sparingly.
- emphasized `cubic-bezier(0.2, 0, 0, 1)` (alternative seed).

## 85. Transition presets and keyframes
- micro: 100ms ease-out (hover/focus on buttons, links, inputs).
- default: 200ms ease-out (general state change).
- enter: 300ms ease-out (modal open, toast appear, menu reveal).
- exit: 200ms ease-in (exits are faster than entrances).
- emphasis: 300ms spring (success, confirmations).
- fade-in: opacity 0 -> 1 (the reduced-motion-safe substitute for any directional entrance); fade-out 1 -> 0.
- slide-up: translateY(8px) + opacity 0 -> translateY(0) + 1 (popovers, toasts; pair with fade).
- scale-in: scale(0.96) + 0 -> scale(1) + 1 (modal or dialog entrance).
- spin: rotate 0 -> 360deg over 600-1000ms, linear (spinner).
- pulse: opacity 1 -> 0.5, alternate, infinite (skeleton).

## 86. Standard animation values
- Fade in: 150ms ease-out (modals, tooltips, content load).
- Fade out: 100ms ease-in (dismiss, remove).
- Slide in: 250ms ease-out (drawers, mobile menus).
- Scale in: 150ms ease-out from scale(0.95) to 1 (dropdowns, popovers).
- Collapse: 200ms ease-in-out (accordion, disclosure).
- Hover background: 100ms ease.
- Skeleton pulse: 1.5s ease-in-out.
- Spinner: 600ms linear.

## 87. Motion patterns (choreography)
- Entrance reveals: translate <= 8-16px + fade, 300ms ease-out; never animate from far offscreen; reduced motion: opacity-only fade <= 100ms, no translate.
- Stagger: 40-80ms step, total stagger capped below ~400ms; reduced motion: reveal the group at once.
- Hover lift (pointer devices, where the system uses lift): translateY(-2px) + one elevation step, 100ms ease-out; optional coloured shadow on primary CTAs only; touch has no hover dependency and the resting state is complete.
- Press: scale(0.97) on press, snap back on release, 100ms; no layout shift.
- Scroll scrub and section transitions: sparingly, for storytelling; pin + scrub stays interruptible and never traps scroll; transform/opacity only; reduced motion disables pin/scrub and shows sections statically.
- Overlays (modal, drawer, popover, toast): enter scale 0.96 -> 1 + fade; exit with a faster fade; the backdrop fades with the surface; focus moves on enter and restores on exit; reduced motion: fade only, no scale.
- Loading: skeleton pulse (opacity 1 <-> 0.5) or shimmer, linear, infinite; spinner rotation 600-1000ms linear; prefer skeletons that match the final layout over spinners for perceived speed.
- Charts animate on entry (line-draw via `pathLength`, scaleY bars, staggered points) with reduced-motion parity.

## 88. Expand and collapse
- Animate the height of an open/close component, not just a chevron rotation; collapsing via `hidden` or `display:none` alone reads as rigid.
- Smooth-height pattern: a grid with `grid-template-rows:0fr` transitioning to `1fr`, an inner wrapper with `overflow:hidden; min-block-size:0`.
- Keep accessibility: on expand remove `hidden`, then add the open class on the next frame; on collapse remove the open class and set `hidden` on `transitionend`.
- Under `prefers-reduced-motion: reduce`, no transition.

## 89. Reduced motion
- Always honour `prefers-reduced-motion` (WCAG 2.3.3): replace travel with opacity or an instant change, keep the feedback; collapse durations to 0ms or cap opacity-only fades at 100ms.
- Disable transform and position animation; opacity and colour transitions are acceptable, but transform/size/position transitions longer than 0.1s are not; keep all non-motion feedback (colour, text, ARIA live).
- Global fallback: under `prefers-reduced-motion: reduce`, set animation and transition durations to 0.01ms; ship an explicit reduced-motion block whenever the page has real motion; gate motion with motion-safe / motion-reduce variants where the styling system offers them.
- Never let content be revealed only by an entrance animation (opacity:0 revealed only by animation); reduced-motion users must see everything.
- Never rely on zero-area elements that only have area while animating (give a radar sweep a wedge, not a 1px line).
- Make sure the reduced-motion rule is not lost to CSS specificity and that a policy exists even in external stylesheets.
- Native targets query the platform reduce-motion setting and default to fade.
- Never remove focus indicators under reduced motion.

## 90. Motion anti-patterns
- Everything animating on load (nothing feels important).
- Durations > 500ms on routine UI (sluggish).
- Bounce or spring on every element (toy-like).
- Animating box-shadow, filter or width (jank).
- Motion with no reduced-motion fallback.
- Scroll-jacking that fights the user's scroll.
- Nothing moving at all, or everything moving the same.
- Sampling or theming mid-transition.

## 91. Motion handoff spec
- Spec every animation with property, trigger, from, to, duration, easing, delay and reduced-motion fallback.

# Part 10 — Components: atoms

## 92. Eight interaction states
- Every interactive element defines all applicable states; consciously decide which apply and justify any N/A; a component that only looks right at rest is not finished.
- 1 Default (always): resting, base tokens.
- 2 Hover (always): `-hover` token, never a raw colour; background shift and cursor change; state-layer overlay alpha 0.08 (`opacity.subtle`).
- 3 Focus (always): focus-ring shadow token on `:focus-visible`, 3:1 against both neighbours; never `outline: none` alone.
- 4 Active/Pressed (always): `-active` token, deeper background shift; overlay alpha 0.12 (`opacity.pressed`).
- 5 Disabled (always): `disabled` or `aria-disabled`, opacity 0.5, no pointer events, `cursor: not-allowed`, still readable.
- 6 Loading (if async): spinner, skeleton or progress + `aria-busy`; width must not jump; content dim 0.7, `cursor: progress`; reads differently from disabled.
- 7 Error (if input): error border/ring (`feedback.error`, `border.error`) + a message below that says how to fix it + `aria-invalid`.
- 8 Selected (if selectable): `interactive.selected-bg` (accent background, checkmark), overlay alpha 0.16, `aria-pressed` / `aria-selected` / `aria-current` + a non-colour cue.
- Inputs also cover read-only (opacity 0.9, editable-looking but locked, legible, not disabled) and filled states; every input has an associated label.
- Document all states before coding; missing states cause the most rework.

## 93. Component spec quality bar
- Every spec includes: anatomy diagram; all visual variants (primary, secondary, ghost, etc.); sizes sm, md, lg with exact dimensions; states (at least 6: default, hover, focus, active, disabled, loading, plus the applicable rest of the 8); token mapping for every value; accessibility (ARIA pattern, role, keyboard model, screen-reader behaviour); rendering notes.
- Deliver as: anatomy diagram, variants table, sizes table, states table, token mapping, accessibility notes, code example.
- Check whether the component already exists before specifying and match the existing spec format.
- Pull the ARIA pattern for the component and the contrast and target rules from the WCAG checklist; map sizes and states to tokens.

## 94. Component API contract
- Expose variants through a typed prop: primary / secondary / ghost / destructive (+ link, icon).
- Expose sizes sm / md / lg with exact control heights 32 / 40 / 48px (icon button 40x40).
- Pair size with padding and type: sm = 12px inline padding + 14px text + 16px icon; md = 16px + 16px text + 20px icon; lg = 24px + 18px text + 24px icon.
- When a component needs a seventh boolean prop, split it into two components (composition over props).
- Use logical properties (`block-size`, `padding-inline`, `margin-inline-*`, `inset-inline-*`, `text-align: start`) for RTL readiness.
- Icons inside controls are `shrink-0` and `pointer-events: none`; icon-to-label gap 8px.

## 95. Cross-screen component consistency
- Use identical CSS and markup for the same component on every page; factor one pattern and reuse it verbatim; a checkbox thin in one place and heavy in another is a bug.
- Build one reusable primitive per atom (Button, Input, Modal, Badge); never repeat utility-class clusters inline or hand-roll a div-as-modal per screen.

## 96. Button
- Anatomy: [icon?] [label] [icon?] in a pressable container.
- Variants: Primary (main CTA, one per visible area), Secondary (supporting, neutral), Ghost (tertiary, toolbar, inline), Destructive (delete, remove, irreversible), Link (navigation styled as a button: link colour + underline).
- Sizes: sm 32px high, padding 12x8, 14px font, 16px icon; md 40px, 16x10, 16px font, 20px icon; lg 48px, 24x12, 18px font, 24px icon.
- Hover: background shifts one shade; Active: two shades; Focus: focus-ring shadow.
- Disabled: opacity 0.5, `cursor: not-allowed`, `pointer-events: none`.
- Loading: replace the icon with a spinner (`aria-hidden`), `aria-busy="true"`, a screen-reader-only "Loading" label, block interaction, announce through a live region; width does not jump.
- Error: N/A standalone; submit buttons reflect form error through the form.
- Selected: `interactive.selected-bg` + `aria-pressed` / `aria-selected`, toggle and segmented buttons only.
- Always a native `<button>`, never a `<div>`; icon-only needs `aria-label`.
- Disable with `disabled` (removes from tab order) or `aria-disabled="true"` (keeps it discoverable in tab order).
- Fix button height and centre the label vertically by height, not padding.
- Minimum target 24x24px (2.5.8).

## 97. Input
- Anatomy: [leading-icon?] [prefix?] [input] [suffix?] [trailing-icon?] [clear?].
- Variants: text, email, password (visibility toggle), number, search, URL, tel.
- Sizes: sm 32px, padding 12x8, body-sm; md 40px (default), 12x10 (12px inline padding), body-base; lg 48px, 16x12, body-lg.
- State matrix: default border neutral-200, bg white, text neutral-900; hover border neutral-300 (`border-hover`, `border.strong`); focus border blue-500 + focus ring; active border blue-500 with caret visible; disabled border neutral-200, bg neutral-100, text neutral-400, icon neutral-300, not-allowed cursor; loading text neutral-400 with a trailing spinner + `aria-busy` during async validation or lookup; error border red-500 + red error icon + message below + `aria-invalid`; filled shows the value with default styling; read-only is non-editable default with no hover.
- Placeholder uses `text.tertiary`; essential borders meet 3:1.
- Always associate `<label for>` / `id`; errors via `aria-describedby` + `aria-invalid="true"`; required via `aria-required="true"` + a visual asterisk.
- Password toggle labels: "Show password" / "Hide password".
- Never block paste; set `autocomplete` on personal-data fields (1.3.5).

## 98. Label
- Anatomy: [label-text] [required-indicator?] [optional-indicator?]; style 14px / medium, `text.primary`.
- Use `<label for>` so clicking focuses the input.
- Required: `<span aria-hidden="true">*</span>` + `aria-required` on the input.
- Group labels: `<legend>` inside `<fieldset>`.

## 99. Badge
- Anatomy: [dot?] [text] [remove-button?].
- Variants: neutral (default tags), primary (active/selected), success, warning, error, dot (8px circle, no text).
- Sizes: sm 20px high, md 24px high; pill radius; padding x10/y2.
- Notification badges carry a full label ("3 unread messages"), not the number alone.
- Status badges pair with descriptive text, not colour only.
- In quiet systems, badges may be bare coloured text (12px) rather than filled pills.

## 100. Avatar
- Anatomy: image | initials | fallback icon, circular.
- Sizes: xs 24, sm 32, md 40, lg 48, xl 64, 2xl 96px.
- Fallback order: uploaded image -> initials (first + last initial) -> generic person icon.
- Image `alt="[User name]"`, or `alt=""` if the name is adjacent; initials get `aria-label="[Full name]"`.
- An online/status dot is announced via `aria-label`, never colour only.
- Avoid chart colours behind white initials (measured 2.65:1 in dark).

## 101. Checkbox
- Anatomy: [box] [label] [help-text?]; sizes sm 16, md 20, lg 24px box; radius 4px.
- States: unchecked, checked, indeterminate, hover, focus, disabled.
- Prefer a native `<input type="checkbox">`; indeterminate via `el.indeterminate = true` + `aria-checked="mixed"`; use indeterminate for select-all in tables.
- Group in `<fieldset>` + `<legend>` (or `role="group"` + `aria-labelledby`).
- Space toggles; tri-state cycles true -> false -> mixed (or true -> false in simple implementations).
- Custom thin pattern: keep the real input underneath for native accessibility and keyboard; draw the box overlay with `pointer-events:none` (or a wrapping label forwards the click); draw check and dash as two paths in one SVG toggled by `:checked` / `:indeterminate` with matched stroke weight; 1.5px strong-border token, 0.25rem radius, 0.62rem glyph, stroke-width 2 with round caps.
- Do not use native `accent-color` when the house look is thin; it renders too heavy.

## 102. Radio
- Anatomy: [circle] [label] [help-text?]; sizes 16/20/24px.
- States: unselected, selected, hover, focus, disabled.
- Always inside `<fieldset>` + `<legend>` (or `role="radiogroup"` + `aria-labelledby`).
- Only one radio in the tab order (the selected one, else the first); arrows move selection AND focus and wrap last -> first and first -> last; Space selects the focused radio if not auto-selected.

## 103. Toggle / Switch
- Anatomy: [track] [thumb] + optional [label] [status-text]; pill track.
- Sizes: sm track 36x20 / thumb 16px; md 44x24 / 20px; lg 52x28 / 24px.
- States: off, on, hover, focus, disabled; the two states must look different.
- `role="switch"` + `aria-checked` (not `role="checkbox"`); Space and Enter toggle.
- The label describes what it controls; a switch implies immediate effect (no submit); in forms that require submit, use a checkbox.
- Provide visible on/off labels for users who cannot perceive colour.

## 104. Tooltip
- Anatomy: trigger -> container + arrow + text; non-interactive supplementary text.
- Placement: top by default, then right, bottom, left; auto-flip near viewport edges.
- Tokens: surface gray-900, text white, radius 6px, shadow md.
- Show on hover after a 300ms delay AND on focus; hide on mouse leave, blur, Escape and scroll.
- Max width 240px; no interactive content (use a popover or disclosure instead).
- `role="tooltip"` + `aria-describedby` on the trigger; never put essential information only in a tooltip.
- WCAG 1.4.13: dismissible (Esc), hoverable, persistent.

# Part 11 — Molecules & organisms

## 105. Form Field
- Composition: Label + Input + optional help text + optional error text.
- Layout: stacked (default, label on top) or inline (label left, for short labels); inline collapses to stacked below md; multi-column fields span full width below sm.
- Gaps: label-input 4px, input-help 4px, field-to-field 16px.
- State flow: default -> hover -> focus -> filled -> error -> disabled.
- Error replaces help text, using `feedback.error-text` colour + an error icon.
- Help text via `aria-describedby`; error via `aria-invalid="true"` + `aria-describedby`; error message in `role="alert"` or a live region.

## 106. Search Bar
- Composition: search icon + `type="search"` input + clear button + optional suggestion dropdown (recent, popular).
- Variants: instant (filter as you type, 300ms debounce), submit (Enter or button), combobox (autocomplete).
- States: empty, typing (show clear), has value, loading (spinner replaces the search icon), no results.
- Desktop: full width in a toolbar or container-constrained; mobile: collapses to an icon button that expands to a full-width overlay on tap.
- `role="search"` or `<search>`; clear button `aria-label="Clear search"`; suggestions use the combobox pattern; announce the count ("5 results found").

## 107. Card
- Composition: [image?] + [header: badge? + title + subtitle?] + [body] + [footer: buttons].
- Title heading-5 + optional overflow menu; supporting text body-sm `text.secondary`; body body-base.
- Variants: Outlined (`border.default`, no shadow: lists, dense); Elevated (no border, `shadow.sm`: standalone, dashboards); Interactive (border + `shadow.sm` on hover: clickable); Filled (no border or shadow: on sunken backgrounds).
- Padding 24px (compact 16px); internal gap 16px; radius 8px; header gap 6px + 16px bottom padding; footer right-aligned actions with 8px gap + 16px top padding.
- Image flush to the card edge with top-corner radius only, fixed aspect-ratio token, height capped at 60vh; never let card images grow with content ("column of posters").
- Grid: 3 columns desktop -> 2 tablet -> 1 mobile; card min-width 280px, no max.
- Interactive card: wrap in `<a>` / `<button>` with a full-card click area; with multiple links use the stretched-link pattern with one primary `<a>`.
- Title is a heading at the correct page level; image has meaningful `alt`, or `alt=""` if duplicated.
- Commerce tiles end in the same full-width button.

## 108. Navigation item
- Composition: icon + label + badge? + chevron? (nested).
- Variants: sidebar item, tab item, breadcrumb item, bottom-nav item (icon + label stacked).
- States: default, hover, active/current, focus, disabled.
- Active indicator: sidebar 3px `action.primary` indicator + selected-bg (prefer a full treatment over a lone coloured side strip on cards; a nav indicator is not a card border); tab bottom border 2px `action.primary`; breadcrumb current item bold text, no link.
- Text secondary by default, primary when active; background transparent / selected-bg; icon matches the text colour.
- Wrap in `<nav aria-label="Main navigation">`; current item `aria-current="page"` (sidebar, breadcrumb) or `aria-selected="true"` (tabs); collapsible groups `aria-expanded`; badge count in the label ("Messages, 3 unread").

## 109. Dropdown
- Composition: trigger button + floating list; separators; destructive item variant.
- Variants: menu (button + chevron, `role="menu"`), select (input-like, `role="listbox"`), multi-select (checkable), context menu (right-click).
- Min-width = trigger width; max-width 320px; item height 36px (md), 32px (sm); padding = input padding; shadow lg; radius 8px; placement bottom-start with auto-flip.
- Item states: default, hover, focus, active, selected (checkmark), disabled (grey, skipped in keyboard navigation).
- Opens on click, not hover; closes on selection, Escape and click-outside.
- Scrolls with a max-height when > 8 items; typeahead focuses the matching item.
- Trigger `aria-haspopup`, `aria-expanded`; items `menuitem` / `option`; Down/Up navigate, Enter selects, Esc closes.

## 110. Accordion and disclosure
- Accordion: heading > `<button aria-expanded aria-controls id>`; panel `role="region"` + `aria-labelledby`, `hidden` when collapsed.
- Enter/Space toggle; optional Down/Up between headers and Home/End first/last; focus stays on the button; panel content joins the tab order when expanded.
- Disclosure: a button with `aria-expanded` (on the button, not the content) + `aria-controls`; content hidden via `hidden` / `display:none`; Enter/Space toggle.
- Expand with a smooth grid-rows height animation (see Expand and collapse), not a chevron rotation alone.

## 111. Header / App bar
- Composition: logo (fixed width) + nav items (flex grow, centre) + search + avatar/actions (auto, right).
- Height 64px desktop, 56px mobile; padding = page inline-padding 16/32px; z-index sticky 20 or fixed 30.
- Slots: leading (logo, hamburger), centre (primary nav, breadcrumbs), trailing (search, notifications, avatar, CTA).
- Variants: static, sticky (`position: sticky`), transparent (over hero, opaque on scroll), compact (64 -> 48px on scroll).
- Desktop >= lg full nav; tablet md-lg collapsed nav (hamburger or priority+); mobile < md logo + hamburger + essential actions only.
- Scroll transition: opacity/height 200ms ease-out; mobile menu slides from the left at 250ms ease-in-out.
- `<header role="banner">` once per page; `<nav aria-label="Main navigation">`; the first focusable element is "Skip to main content"; mobile menu `aria-expanded`, `aria-controls`, focus trap when open.
- A sticky header must never cover the focused element (2.4.11).

## 112. Sidebar
- Structure: fixed header (logo, collapse), search, scrollable nav groups with labels and nested sub-items, fixed footer (user, settings).
- Width 256px default, 64px collapsed; z-index 30 for the mobile overlay.
- States: expanded 256px icons + labels (desktop default); collapsed 64px icons + tooltips (user preference); hidden 0px (mobile default); overlay 256px over content (mobile open).
- Collapse: width 200ms ease-in-out; text fades out at 150ms; icons remain.
- Desktop >= lg persistent and pushes content; tablet collapsed by default, expands on hover or click; mobile hidden, a hamburger opens the overlay with a backdrop.
- `<aside aria-label="Sidebar navigation">` containing `<nav>`; collapse button `aria-expanded` + `aria-label="Collapse sidebar"`; collapsed items show tooltips on hover and focus; mobile overlay traps focus, Esc closes, backdrop `aria-hidden`.

## 113. Data table
- Slots: toolbar (title, filters, search, bulk actions, add), header (labels, sort indicators, select-all), body (rows, inline edit, expandable rows), footer (pagination, row count, per-page).
- Sorting: clicking a header toggles asc / desc / none and really sorts; filtering column-specific or global; selection via a checkbox per row + select-all; bulk actions appear when rows are selected; row actions via an overflow menu.
- Empty state: illustration + message + CTA; an empty filter result is a real message, not a blank body; loading: 5 skeleton rows.
- Cell padding x16/y12; zebra rows use ghost alpha 0.04; density is deliberate (row height, padding and filter bar do not share one value).
- Desktop full table; tablet horizontal scroll with a sticky first column and a visible scroll cue; mobile card-per-row or collapsible rows; usable at 320px with no horizontal page scroll.
- Long values (80-character name, nine-digit total) truncate on purpose with ellipsis + `title`, or wrap; never clip silently.
- Semantic `<table>/<thead>/<tbody>/<th scope>`; a caption (visually hidden if the panel header says it); `aria-sort` on sortable headers only when clicking really sorts; sort controls are real buttons; select-all `aria-label="Select all rows"`; row checkbox `aria-label="Select [item]"`; `<nav aria-label="Table pagination">`; status badges include text; announce sort and filter changes with `aria-live="polite"`.
- Row selection carries a non-colour cue; never make the whole row the only click target without a keyboard equivalent.
- Known failures: 320px overflow, clipped text without ellipsis, one padding value everywhere, whole-row click with no keyboard equivalent.

## 114. Modal / Dialog
- Build ONE reusable modal primitive for all overlays; never hand-roll a div-as-modal per screen; a native `<dialog>` is acceptable.
- Must have: focus trap (Tab and Shift+Tab cycle only inside), `role="dialog"`, `aria-modal="true"`, `aria-labelledby` (title), `aria-describedby` (description), Escape to close, focus returned to the trigger on close, and a backdrop; a missing trap violates 2.4.3 and 2.1.2.
- Structure: header (icon, title, close), scrollable body (`overflow-y: auto`, the body scrolls, not the page), footer (secondary, primary); header and footer separated by hairline borders.
- Widths: sm 400px (confirmations, simple forms), md 560px (complex forms), lg 720px (multi-step, rich), xl 960px (data-heavy, split), full 100% - 48px (mobile).
- Tokens: bg `surface.card`, overlay `surface.overlay` / scrim (black at 50%), radius 12px, shadow xl, z-index 50, padding 24px.
- Animation: overlay fade-in 150ms + modal scale 0.95 -> 1 + fade 150ms, gated by motion-safe; close in reverse at 100ms; reduced motion: fade only.
- Focus: on open focus the first focusable element (or the dialog itself); set `inert` (or `aria-hidden`) on the background.

## 115. Drawer
- Structure: header with close, scrollable body, optional action footer; main content dimmed.
- Variants: right 320-480px (detail panels, edit forms); left 256-320px (mobile nav); bottom 40-90vh (mobile action sheets).
- Same surface and shadow as the modal; z-index overlay 40 or modal 50 with a backdrop.
- Slide translateX(100%) -> 0 over 250ms ease-out; backdrop fades over 150ms; honour reduced motion.
- With a backdrop it blocks content and traps focus; without one it is inline and persistent, pushes content, and does not trap.
- Swipe-to-close on touch (bottom, left, right).
- `role="dialog"`, `aria-modal="true"` if blocking, `aria-label`; Esc closes; focus returns to the trigger.

## 116. Destructive confirmation
- Give irreversible actions real friction (WCAG 3.3.4 / 3.3.6): a confirmation dialog.
- The title asks ("Delete account?"); the confirm button answers in matching words, restating action and object ("Delete account", never "Delete", "OK", "Yes" or "Confirm"); Cancel stays "Cancel".
- The confirm button uses the danger token and the same variant as the trigger.
- High-stakes actions require a type-to-confirm field (e.g. "DELETE") that enables the confirm button; focus that field on open.
- Order Cancel (secondary) then destructive; default focus goes to the safe path or the confirm field, never the destructive button.
- The dialog traps focus, closes on Escape and returns focus to the trigger.
- Confirmations state the consequence and count ("Delete 4 items? This can't be undone.").

# Part 12 — Navigation

## 117. Tabs
- Anatomy: tablist [tab...] -> tabpanel.
- Variants: underline (default, active border `action.primary`, 2px); pill/segmented (compact filters, <= 4 options, selected bg `state.selected.bg`); vertical (settings, side nav, leading-edge indicator).
- Sizes sm/md/lg from control heights.
- States: default, hover (`opacity.subtle` overlay), focus (focus ring), active, selected (indicator + `text.primary`), disabled (`opacity.disabled`), loading (skeleton panel), error n/a.
- `role="tablist"` (with `aria-label`) > `role="tab"` (`aria-selected`, `aria-controls`) > `role="tabpanel"` (`aria-labelledby`); inactive panels `hidden`.
- Roving tabindex: active tab `tabindex="0"`, others `-1`; Left/Right move, Home/End jump; Tab enters the tablist at the selected tab, then the panel; Delete optionally removes a closeable tab.
- Automatic activation (arrow moves + activates) for fast switching; manual activation (Enter/Space) for expensive loads.
- The selected tab is distinguished by more than colour (indicator + weight); a tab must actually change the panel.

## 118. Breadcrumb
- Anatomy: Home / Section / Subsection / [Current] with separators; optional leading icon.
- On small screens collapse the middle into an "..." menu.
- Links have default/hover/focus; the current item is non-interactive, not a link, `aria-current="page"`.
- `<nav aria-label="Breadcrumb">` > ordered list; separators `aria-hidden`, never the only indicator.
- Mirror breadcrumbs in RTL; let the row wrap.

## 119. Pagination
- Anatomy: [Prev] [1][2]...[n] [Next], or [<] Page X of Y [>].
- Variants: numbered with ellipsis, prev/next only, load-more, infinite (announce new items through a live region).
- Targets >= 24px (`control.xs`); recommend 40px (`control.md`) for touch.
- States: default, hover, focus, active, selected (current, `aria-current="page"`), disabled (prev on first, next on last), loading, error.
- `<nav aria-label="Pagination">`; disabled prev/next `aria-disabled` and non-actionable; announce result-range changes politely.

## 120. Stepper / progress steps
- Variants: horizontal, vertical, numbered vs icon, with or without descriptions.
- Step states: upcoming (muted), current (`action.primary` + `aria-current="step"`), completed (check + success), error (one step), disabled.
- An `<ol>` of steps; status by icon + text, never colour only; navigable steps are buttons or links with clear names ("Step 2: Shipping").
- Show progress and expected effort ("Step 2 of 4 · ~2 min"); let the row wrap on narrow screens.

## 121. Menu / Menubar
- Anatomy: trigger -> menu [menuitem][separator][submenu].
- Variants: dropdown, context, menubar, checkable (`menuitemcheckbox` / `menuitemradio`), submenus.
- Item height >= `control.sm` (32px).
- States: default, hover, focus, active, selected/checked, disabled, loading (async items), error.
- `role="menu"` > `menuitem`; separators `role="separator"`; trigger `aria-haspopup="menu"` + `aria-expanded` + `aria-controls`.
- Up/Down move; Right/Left open/close a submenu (menubar: next/previous top-level); Enter/Space activate; Home/End first/last; typeahead; Esc closes and returns focus to the trigger.
- Focus moves into the menu on open and returns to the trigger on close.

## 122. Toolbar
- `role="toolbar"` + `aria-label` (+ `aria-orientation` if vertical); a single tab stop.
- Left/Right (Up/Down when vertical) move between controls; Home/End first/last; Tab exits; nested controls keep their own activation keys.

## 123. Location and wayfinding
- Show where the user is: breadcrumb + current nav state (2.4.8 AAA).
- Provide at least two ways to locate pages: search, sitemap, nav (2.4.5).
- Keep navigation order and structure consistent across pages (3.2.3); the same function gets the same label (3.2.4).
- Place help and support links and chat widgets in the same relative position (3.2.6).
- Announce SPA route changes manually.

# Part 13 — Overlays & feedback

## 124. Popover
- Anatomy: trigger -> popover (arrow? + content + actions?); non-modal, can hold interactive content.
- Variants: click vs hover trigger, with or without arrow, rich content (forms, menus), confirmation popover.
- Auto-flip and shift to stay in the viewport; offset via spacing tokens; elevation shadow lg (dropdown/popover level).
- States: closed, opening (scale-in + fade), open, hover/focus within, interacting, closing (exit), disabled trigger, error (async content).
- Trigger `aria-expanded`, `aria-controls`; the popover is labelled by its heading.
- Focus moves in on open but the page stays interactive; Esc closes and returns focus to the trigger; click-outside closes.
- Tooltip = brief, non-interactive, describes; Menu = action list; Popover = interactive content.

## 125. Command palette
- Anatomy: a modal with a search input -> grouped results (icon, label, shortcut); triggered by Cmd/Ctrl+K.
- Variants: commands only, with navigation, with recent/suggested, nested pages, async results.
- States: closed, open (focus in input), typing (filtering), result hover/active, selected (execute), empty (helpful empty state), loading, error.
- A modal dialog containing a combobox (`role="combobox"` + `role="listbox"`); `aria-activedescendant` for the highlighted item.
- Up/Down navigate, Enter runs, Esc closes, typeahead; trap focus while open and restore it on close.
- Announce the result count; every item has an accessible name; shortcut hints are supplementary.

## 126. Backdrops and scrims
- Modal/drawer backdrop: rgba(0,0,0,0.5) or scrim alpha 0.6 (rgba(3,7,18,0.6) light; rgba(0,0,0,0.72) dark).
- Optional blur 16px for modal backdrops, 24px for full-screen scrims.
- The backdrop is `aria-hidden`; background content is `inert`.

## 127. Divider / Separator
- Horizontal or vertical (inline, needs an explicit height), with a label ("OR"), inset; solid or dashed.
- Decorative: `role="presentation"` / `aria-hidden`; semantic grouping: `role="separator"` (+ `aria-orientation` if vertical).
- Colour `border.default` / subtle; never rely on a divider alone to convey grouping to screen readers; use headings and landmarks.

## 128. Alert (contextual message)
- Composition: icon + title? + message + action? + close?.
- Variants: info (tips), success (completed), warning (potential issues), error (failures, blocking) using `feedback.*` colours.
- Full width within its container (not the page); padding 16px; icon-text gap 12px; radius 8px; a full hairline border + icon + text instead of a coloured one-side strip.
- Inline alerts persist until dismissed or resolved; toast alerts auto-dismiss after 5s (non-critical) or persist (errors); stack newest on top, max 3 visible.
- `role="alert"` for dynamic errors and warnings; `role="status"` for success; static inline info needs no role.
- Dismiss `aria-label="Dismiss alert"`; icon `aria-hidden`; never colour alone: icon + text + border convey the variant.
- Do not move focus to an alert unless it contains interactive elements the user must address.

## 129. Toast / Notification
- Anatomy: icon + title/message + action? + dismiss button.
- Variants: success (check, green), error (alert, red), warning (triangle, amber), info (i, blue).
- Auto-dismiss success/info after ~4-6s (5s); errors persist until dismissed; never auto-dismiss content the user must act on.
- Stack newest-first; cap visible count at 3; pause the timer on hover and focus.
- States: enter (slide-up + fade, 300ms ease-out), default, hover (pause), focus within, dismissing (exit 200ms ease-in), action-pressed, loading (in-toast progress), error.
- Container `role="region" aria-label="Notifications"`; info/success `aria-live="polite"`; errors `role="alert"` / assertive.
- Dismiss is a real labelled button; elevation shadow 2xl; z-index 70.
- Copy is one line, past tense for success ("Link copied"), and must match the visible state.
- Never inject toasts or banners that push content down; overlay or reserve space.
- Offer a quiet mode to postpone or suppress non-emergency interruptions (2.2.4 AAA).

## 130. Banner / inline alert
- Anatomy: icon + message + optional link + action? + dismiss?.
- Variants: info/success/warning/error; page-level (full width, square edges) vs inline (within a card, with radius); dismissible or sticky.
- States: default, hover/focus on interactive parts, dismissing, disabled action.
- Informational `role="status"`; critical `role="alert"`; colour + icon + text; dismiss is a labelled button.

## 131. Skeleton
- Shapes (lines, blocks, circles) matching the final layout geometry and dimensions to avoid layout shift.
- Variants: text lines, avatar/circle, card, table row, media block.
- Animation: pulse or shimmer, linear, infinite (opacity 1 -> 0.5 alternate).
- Loading -> resolved (swap) or error (replace with the error state).
- Wrap the region in `aria-busy="true"`; skeletons are `aria-hidden="true"`; reduced motion: a static placeholder.
- Prefer lightweight skeletons over spinners-then-jank; represent loading honestly with skeleton or progress plus `aria-busy`, never a frozen screen.

## 132. Progress and spinner
- Linear bar (track + fill) or circular ring, optional label/percentage; indeterminate; segmented/stepped; sizes sm/md/lg thickness.
- States: in-progress (0-100), indeterminate (animated), success, error (fill `feedback.error`).
- `role="progressbar"` + `aria-valuenow/min/max` (omit valuenow if indeterminate); label via `aria-label` / `aria-labelledby`.
- Announce milestones politely, not every tick.
- Spinner rotates 360deg over 600-1000ms with linear easing and pairs with `aria-busy`.

## 133. Empty state
- Anatomy: illustration/icon + headline + supporting text + primary action + secondary?.
- Variants: first-use (guide to the first action), no-results (offer to clear filters), cleared (reassure), error/permission (explain + recover).
- Centred, generous whitespace, illustration sized via aspect ratio; one clear primary action; it owns its viewport and gives explanation + first action + a way forward.
- The headline is a real heading; the illustration is `aria-hidden` unless meaningful; the primary action is the natural next focus.
- Never "No data. There is nothing to show." floating under the header.

## 134. Status messages and live regions
- Status messages use live regions announced without moving focus (4.1.3).
- Assertive for errors and critical; polite for success and status; `role="status"` for result counts and loading; `role="log"` for chat and activity feeds.
- `role="alert"` implies assertive + atomic; inject content to announce.

# Part 14 — Forms

## 135. Form (organism)
- Structure: title + description, sections with labels, 2-column rows, full-width rows, action bar.
- Field gap 16px; section gap 32px; column gap 16px; 2 columns desktop -> 1 mobile.
- Action bar right-aligned, primary action last (rightmost).
- States: empty; dirty (unsaved indicator, confirm on navigate away); validating (on blur, not keystroke); submitting (button loading, all fields disabled); success (alert, optional redirect); error (scroll to and focus the first invalid field, error summary).
- `<form>` with `aria-label` / `aria-labelledby`; `<fieldset>` / `<legend>` groups; an error summary `role="alert"` at the top linking to fields; submit `aria-disabled` while loading + announce "Submitting..."; a `beforeunload` confirm + visual indicator for unsaved changes.
- Don't ask for the same information twice; auto-populate earlier entries (3.3.7).
- Rows of fields keep equal control heights (see Form rows).

## 136. Validation and error prevention
- Validate on blur per field, all fields on submit, and revalidate a fixed field immediately; never on keystroke.
- The error appears below the field, replacing help text.
- Errors are identified and described in text, not just red borders (3.3.1), with correction suggestions (3.3.3).
- Legal, financial and data submissions are reversible, verifiable or confirmable (3.3.4); AAA covers all submissions (3.3.6) with review-before-submit and undo everywhere.
- Every input has a visible label; complex fields have instructions (3.3.2); visible label text is contained in the accessible name (2.5.3).
- Changing a setting never auto-triggers a context change without warning (3.2.2); focus alone never triggers a context change (3.2.1).
- Prevent double submission on double click; debounce rapid clicking where needed.

## 137. Combobox / Autocomplete
- Anatomy: input + clear? + toggle -> listbox of options.
- Variants: autocomplete (free text + suggestions), select-only, multi-select (chips), async (debounced fetch + loading).
- States: default, hover, focus, open, selected/active-descendant, disabled, loading, error.
- Input `role="combobox"`, `aria-expanded`, `aria-controls`, `aria-activedescendant`, `aria-autocomplete="list"`; popup `role="listbox"`; options `role="option"` + `aria-selected`.
- Down opens or moves next; Up previous; Enter selects and closes; Esc closes and clears; Home/End move the caret in the input; typing filters; Alt+Down opens without changing selection.
- Focus always stays in the input; announce the result count ("3 results available").

## 138. Select (enhanced)
- Anatomy: trigger (value or placeholder + chevron) -> listbox [group][option].
- Variants: single, multi (chips + count), grouped (optgroup), searchable (becomes a combobox), with icons or descriptions.
- States: default, hover, focus, open, selected, disabled, loading, error (`state.error.border`).
- Never a native `<select>` (see Native select ban); build it as a listbox/combobox with a button trigger and a chevron placed with token inner padding.
- The trigger announces the current value + `aria-expanded`; keyboard parity with native (typeahead, arrows, Esc); it passes every state, keyboard and automated accessibility check.

## 139. Listbox
- `role="listbox"` + `aria-labelledby`, `tabindex="0"`; options `role="option"` + `aria-selected`; multi adds `aria-multiselectable="true"`.
- Down/Up move; Home/End first/last; multi: Space toggles, Shift+Down/Up extends, Ctrl+A selects all.
- Focus via `aria-activedescendant` (the container keeps focus) or roving tabindex.

## 140. Slider / Range
- Anatomy: track + filled portion + thumb; dual thumb for a range.
- Variants: single, range, stepped/ticks, vertical.
- Thumb target >= 24x24 (larger for touch).
- States: default, hover (thumb grows), focus (ring on the thumb), active (dragging), filled track, disabled, error.
- Thumb `role="slider"`, `aria-valuenow/min/max`, a human-readable `aria-valuetext` ("$50", "50%", "Medium"), `aria-label` / `aria-labelledby`; a range = two separately focusable sliders.
- Right/Up +step, Left/Down -step, PageUp/PageDown large step (10x), Home min, End max.
- Show the current value visibly; never rely on position alone; dragging has a non-drag alternative (2.5.7).

## 141. Date / time picker
- Anatomy: input + calendar icon -> popover with a month grid or time list.
- Variants: single, range, date-time, inline vs popover, min/max + disabled dates, presets.
- States: default, hover (day cells), focus (focused day), selected (endpoints + in-range fill), today marker, disabled days, loading, error (invalid input).
- Accept typed dates (never force the calendar); support autofill and password managers.
- Calendar `role="grid"` / `gridcell`; arrows by day/week; PageUp/Down month; Home/End week; announce the focused date; `aria-selected` on the chosen day; the selected day must actually move.
- Localise the format and respect the locale's first day of week.

## 142. File upload
- Anatomy: dropzone (icon + "Drag files or browse") -> file list rows (name, size, progress, remove).
- Variants: single/multiple, drag-drop + click, image preview, type/size constraints.
- States: default, hover, focus, drag-over (active dropzone), uploading (per-file progress), success, disabled, error (rejected type/size: name which and state the limit).
- A real `<input type="file">` reachable by keyboard; drag-drop is enhancement only.
- Label each file row; remove is a labelled button; progress uses `role="progressbar"`; errors explain the constraint and the fix ("File is too large (max 10 MB). Try compressing it.").

## 143. Authentication
- Allow password managers and paste; no CAPTCHA as the sole method; no cognitive tests, puzzles, transcription or recall (3.3.8 AA).
- AAA 3.3.9: no object or image recognition ("select all traffic lights") either; use passkeys or email links.
- Offer "Show password"; support passkeys and email-link login.

# Part 15 — Data display, dashboards & data viz

## 144. Dashboard brief questions
- Who reads it, and what decision do they make from it?
- What is the one number that leads? A dashboard without a lead is a wall.
- What is the update cadence? Hourly figures get a "last run" line; live figures get a tape and a per-row timestamp.
- How dense is honest? A terminal earns 12 panels; a weekly report does not.

## 145. Dashboard layout bands
- Band 1: hero metric at 3x body size plus its own chart, spanning most of the width (the eye lands once).
- Band 2: two or three secondary figures, stacked or narrow (quiet by construction).
- Band 3: three different chart shapes side by side (donut, ranked bars, sparklines); variety reads as intent.
- Band 4: a table that really sorts, plus a feed or log (detail after summary).
- Band 5: a footer line that ends the page on purpose.
- Use a 12-column grid with explicit spans (e.g. 8/4) collapsing to 6, then 1; never auto-fit for primary bands; never four equal stat cards.
- Range tabs actually change the numbers and table headers actually sort.

## 146. Dashboard measurement traps
- Never use chart palette colours as text colours (white initials on a chart colour measured 2.65:1 in dark).
- Success green as text on a raised surface measured 4.43:1 (short of AA); put colour on the icon and sign and keep the text neutral.
- Disable transitions before theme flips when measuring contrast.
- When two fields share a grid row and only one has a hint, set `align-content:start` on the field and an explicit block-size on the control so inputs stay equal height.
- Give a visually-hidden element a positioned ancestor or it inflates scroll width inside scrollers.
- Screenshot at 1600 and 390 wide in both themes; checks pass charts that are drawn wrong.

## 147. Calendar / date grid
- Anatomy: header (prev | month year | next), weekday row, 6x7 day grid, footer (Today / Clear?).
- Variants: single, range (in-range fill = selected-bg at reduced opacity), multi-month (2-3 grids), with time, display-only (availability heatmap).
- Cell hit area >= 24px; the md grid uses 40px cells.
- States: default, hover (hover-bg), focus (roving focus ring), selected (selected-bg), today (`border.strong` ring + `aria-current="date"`), disabled (out of range, opacity 0.5), range endpoint, in-range (subtle fill).
- `role="grid"` (or `application` for rich range UX); `columnheader` with `abbr` weekday.
- Roving tabindex with one tabbable cell; arrows by day/week; PageUp/Down month; Shift+PageUp/Down year; Home/End week edges; Ctrl+Home/End grid corners; Enter/Space select.
- Selected `aria-selected="true"`; announce month/year changes through a polite live region.
- Never convey availability by colour alone; pair with an icon, label or `aria-disabled`.

## 148. Carousel / slideshow
- Anatomy: clipped viewport, slide track, prev/next, pagination dots, play/pause?.
- Variants: single-slide, multi-item, peek, fade vs slide, auto vs manual, looping vs bounded.
- Control hit area >= 44px recommended; slide width via aspect ratio or container fraction.
- Transition at the standard duration with ease-out; snap to slide boundaries; document whether multi-item advances by page or by item.
- States: default, hover (reveal or enlarge controls), focus, active slide (dot filled), transitioning, auto-playing, paused, disabled control at a non-looping bound.
- Container `role="region"` / `group` + `aria-roledescription="carousel"` + `aria-label`; slides `role="group"` + `aria-roledescription="slide"` + `aria-label="N of M"`.
- Auto-advance is pausable (2.2.2): a visible Pause control; pause on hover and focus within; disable autoplay under reduced motion (use fade or instant).
- Prev/next/dots are real labelled buttons held to 3:1; the live region is `off` while auto-playing, `polite` after user interaction; off-screen slides are `aria-hidden` / `inert`.

## 149. Tree view
- Anatomy: node (twisty, icon?, label, badge/count?), indent guides, nested group.
- Variants: single-select, multi-select (tri-state checkboxes), with icons, drag-reorder, lazy-loaded branches.
- Row height `control.sm` / `md` (32/40px); a consistent indent step per level from the spacing scale.
- States: default, hover, focus (roving), selected, expanded, collapsed, loading (branch spinner + `aria-busy`), disabled.
- `role="tree"` (+ `aria-label`) > `treeitem` > nested `role="group"`; `aria-expanded` (parents only), `aria-level`, `aria-setsize`, `aria-posinset`, `aria-selected`; partial multi-select `aria-checked="mixed"`.
- Down/Up visible items; Right expands or moves to the first child; Left collapses or moves to the parent; Home/End first/last visible; Enter activates; Space selects/toggles; `*` expands siblings; typeahead.
- A single `tabindex="0"` (roving); the twisty is decorative if the row is the control; expose state via `aria-expanded`, never the glyph alone.

## 150. Feed
- Container `role="feed"` (+ `aria-busy` while loading); items `role="article"` with `aria-labelledby`, `aria-posinset`, `aria-setsize` (large or estimated for infinite).
- PageDown/PageUp between articles; Home/End first/last loaded; Tab into article content.
- Load more before the user reaches the end to avoid focus loss.

## 151. Universal chart rules
- Shared anatomy: plot area, axes + tick labels, gridlines, series, legend, hover tooltip, optional title/caption.
- Charts are graphical objects: meaningful strokes >= 3:1; information never depends on colour alone.
- Draw charts from the same tokens as the UI (chart-1..n variables); map series to categorical tokens in order, sequences to sequential, +/- to diverging or semantic; never use the brand action or feedback colours directly.
- Cap categorical series at 8; beyond that group into "Other" or re-encode.
- Pair series with direct labels, distinct markers or dash patterns, or texture; provide a legend AND hover labels.
- Gridlines low-contrast (~1.4:1 acceptable, non-essential); axis text >= 4.5:1.
- Motion: ease-out, <= 300ms; animate value changes, not every re-render; reduced motion renders the final frame.
- Every chart ships a text or table equivalent (visually hidden `<table>` or `<figcaption>` summary) + a descriptive `aria-label` / `aria-labelledby`.
- Under forced colours, `forced-color-adjust: none` only for chart swatches that must keep colour, with a non-colour cue retained.
- Draw charts as inline SVG with a viewBox, sized by CSS and filled from chart colour tokens, without a chart-library dependency; generate geometry with a small deterministic (seeded) script, never hand-placed coordinates.
- Put category labels visibly under bars (labels only in `aria-label` leave anonymous bars); lay the plot on an even pitch so a label grid aligns.

## 152. Data-viz palettes
- Categorical (Okabe-Ito-inspired, colour-blind-safe, assign in order): 1 `#2563EB` blue, 2 `#E8710A` orange, 3 `#0E9F6E` green, 4 `#D81B7A` magenta, 5 `#7C3AED` purple, 6 `#0891B2` cyan, 7 `#B45309` brown/amber, 8 `#64748B` slate (neutral series).
- Sequential (single hue low -> high, 5 stops, interpolate for more): 100 `#EFF6FF`, 300 `#93C5FD`, 500 `#3B82F6`, 700 `#1D4ED8`, 900 `#172554`.
- Diverging (around a neutral midpoint): negative-strong `#B91C1C`, negative `#F87171`, neutral `#E5E7EB`, positive `#4ADE80`, positive-strong `#15803D`.
- Semantic outcome: positive `#15803D`, negative `#B91C1C`, neutral `#64748B` (distinct from feedback tokens so charts theme independently).
- Axis: line `border.strong` (baseline/zero), tick `border.default`, label `text.secondary` (essential text, 4.5:1).
- Grid: line `border.default`; line-subtle gray-100.
- Surface: tooltip bg gray-900 (inverse), tooltip text on-dark, plot bg `surface.page`.

## 153. Chart inventory and geometry
- Bar/column: a rect per bucket with a soft corner radius; for discrete periods.
- Candlestick: line wick plus rect body per period, styled by up/down; for OHLC.
- Volume: bars under the price chart on the same x-scale at opacity 0.45; conviction behind a move.
- Moving average: a 2px polyline over the candles with round joins; trend through noise.
- Line/sparkline: polyline with `pathLength` 1 for draw animation; trend in a cell.
- Area/stacked area: a path per band forward along the top and reversed along the previous baseline, closed; composition over time.
- Depth: two cumulative area paths mirrored around the mid; book liquidity.
- Waterfall: a floating rect per step plus dashed connectors; attribution.
- Donut: a circle with stroke-dasharray and rotation per segment; share of whole, 3-5 slices.
- Radial gauge: the same trick with a round linecap and a 270-degree sweep; one value against a limit.
- Scatter/bubble: circles, radius = third dimension.
- Correlation matrix: a table with cell tint by `color-mix`; pairwise relationships.
- Heatmap: a table or rect grid tinted by value; cohorts, calendars.
- Order book: a table with a depth bar per row; bids and asks.

## 154. Chart domain correctness and craft
- A correlation matrix is symmetric with a diagonal of exactly 1.
- A stacked area sums to the total; bands never cross or leave gaps or dark wedges (index the reversed baseline by coordinate, not by array index).
- A waterfall has connectors; the closing bar equals opening plus steps.
- Depth rises away from the mid on both sides; it never falls.
- Donut segments total the whole.
- Loss curves map high values to the top (SVG y grows downward).
- Wind barbs rotate about their origin and point into the wind; the viewBox clears shaft plus pennant.
- A forest-plot null line aligns with its own 1.0 tick (equal axis and plot widths).
- Kaplan-Meier censoring ticks are offset from event steps.

## 155. Chart accessibility contract
- Every SVG chart gets `role="img"` plus an `aria-label`, or title + desc via `aria-labelledby`, a legend, and an accessibility contract per chart type.
- Describe what the chart shows ("Range 182.06 to 200.10, closing at 187.84"), not that it is a chart.
- Never encode meaning in colour alone: green with "+" and an arrow, red with "-"; up/down carries a word in table cells.
- Sortable headers, range tabs and theme toggles that declare state actually change it on click.

## 156. Bar / column chart
- Compares discrete categories; variants vertical, horizontal, grouped, stacked, 100%-stacked.
- States: default, hover (emphasis + tooltip), focus (keyboardable bar with focus ring), selected/filtered, empty, loading (skeleton bars).
- Expose bars as `role="list"` / figure with per-bar `aria-label="Category: value"` or the backing table; order meaningfully (by value or category); label the axes.

## 157. Line / area chart
- Trends over a continuous dimension (usually time); variants single, multi-series, area, stacked area, stepped, threshold band.
- States: default, hover (crosshair + nearest-point tooltip), focus (point navigation), zoomed/brushed, empty, loading.
- Distinguish series by dash pattern + marker shape, not hue only; point-by-point keyboard traversal or a table fallback; label units on the axis.

## 158. Pie / donut chart
- Part-to-whole for few segments only (<= 5-6); variants pie, donut with a centre metric, leader-line labels.
- States: default, hover (segment lift + value), focus, selected, empty.
- Direct-label each segment with name + %; legends alone fail; order by magnitude; prefer bars when segments are many or similar.

## 159. Sparkline
- An inline micro-trend in a table cell or KPI card, without axes; variants line, bar, win/loss, end-dot, min/max markers.
- States: default, hover (reveal value), positive/negative tint (semantic positive/negative).
- Decorative (`aria-hidden`) if the numeric value is adjacent; otherwise an `aria-label` with a trend summary ("Up 12% over 7 days").

## 160. Scatter / bubble chart
- Correlation of two measures (three via bubble size); variants with a trend line, categorised by colour + shape.
- States: default, hover (point tooltip), focus, selected/lassoed, empty.
- Encode category by shape AND colour; label axes with units; provide a data table; include the size measure in the tooltip rather than relying on size alone.

# Part 16 — Icons & imagery

## 161. Icon foundations
- Use one icon set (e.g. lucide) with verbatim paths, never hand-drawn approximations (they render as broken glyphs).
- Design on one pixel grid (commonly 24x24) with a consistent live area and padding shared by every icon.
- One stroke width across the set (1.5-2px at 24px; default stroke-width 2); keep stroke constant across sizes (scale the canvas, not the stroke).
- Pick one primary style (outline OR solid OR duotone); use the alternate only as a deliberate signal (e.g. solid = selected/active).
- Align to optical centre and balance visual mass.
- In quiet editorial systems, use no icons beyond search and chevron.

## 162. Icon sizing and colour
- Sizes: xs 12px (dense inline, badge), sm 16px (default inline with body text), md 20px (buttons, inputs), lg 24px (standalone, nav), xl 32px (feature, empty-state accent).
- Pair icon size with text size; keep stroke legible at the smallest size used.
- Colour via `currentColor` only (stroke currentColor, fill none); never hard-code icon hex.

## 163. Icon delivery
- Default to inline `<svg>` (stylable, no extra request, supports ARIA, best for forced colours and theming).
- Use an SVG symbol sprite (`<use href="#id">`) referenced by name for large sets; define each icon once with no per-use path duplication.
- Avoid icon fonts (accessibility and rendering issues, no duotone or forced colours) and CSS background-image icons (they vanish in forced colours).
- Use an `<Icon name size>` wrapper to enforce size tokens and accessibility props.

## 164. Icon accessibility and states
- Decorative icon next to a label: `aria-hidden="true"`, no `title`.
- Informational icon: `role="img"` + `aria-label` / `<title>` on the SVG; interactive icon: wrap in a `<button>` with `aria-label`.
- Icon-only controls (carousel dots, kebab, icon buttons) need a >= 24x24px hit target (44px recommended) and 3:1 contrast (1.4.11), not 4.5:1.
- Set an empty button's `color` to the actual indicator colour and draw the visual from `currentColor` so measurement reflects reality (the default UA button colour is near-black regardless of theme).
- Never icon-alone for status; pair with text; icon meaning is not universal.
- States: default `text.secondary`; hover/active inherit the control state; selected `action.primary` or the solid variant; disabled opacity 0.5; loading an animated spinner + `aria-busy`.

## 165. Images and media
- Every image carries width and height (or an aspect-ratio token) to reserve space; below-the-fold images lazy-load.
- Serve AVIF/WebP with responsive sizes (`srcset` / `sizes` such as `(max-width: 768px) 100vw, 50vw`); mark the above-the-fold LCP image as priority; blur placeholders are acceptable for smooth loading.
- Media caps: <= 60vh tall, never wider than its container, <= 500,000 image bytes per page.
- Use real imagery, not grey boxes; never reproduce a reference's photos, logos or copyrighted copy.

## 166. Photography and art direction
- Let a full- or half-bleed photograph lead each section with type around it (within the screen-economy caps).
- Product shots on near-white or 5%-grey tiles, objects floating, no props.
- Prefer real people and real device screens over illustration for sports, fitness and banking.
- Keep imagery square-cornered and shadowless in gallery systems, or clip all photography into rounded containers in friendly systems; pick one.
- Never mask photography into circles or blobs unless the system does.
- Use tokenised overlay gradients on photos to keep white headlines legible, or put text on the darkest area of the art.

# Part 17 — Page templates & screen design pipeline

## 167. Choosing the method for a screen request
- A dashboard, terminal, console or any screen showing many numbers at once: use the dashboard method (layout bands, chart rules).
- An existing site or app to improve: use the redesign/audit method.
- A screenshot, mockup or reference image to match: use the reference-matching method.
- One component: use the component-spec method.
- A brand foundation from scratch before any screen: build the brand kit (tokens and design-system document) first.

## 168. Screen build sequence
- Step 1: write the brief inference block.
- Step 2: apply the non-negotiables (token by intent, one shared theme, eight states, one thing leads, zero emoji, no unmeasured numbers).
- Step 3: pick a reference anchor (archetype or named system) and resolve it into tokens rather than styling screens directly; one CSS-variable layer imported once; if a brand colour fails contrast, adjust it.
- Step 4: build mobile-first; every value a token; every interactive element ships all eight states; content first, then the layout that serves it.
- Step 5: run objective checks (states light/dark, responsive at 1.25 text scale, slop tells, taste heuristics).
- Step 6: render and look at every state; click each control.
- Step 7: run an adversarial critique.
- Deliver: the brief inference block, the complete output, the real check results and the critic's verdict.

## 169. Dashboard template
- Zones: header; title bar (title, date picker, + New); a stats row of KPI cards (metric, trend, sparkline); primary chart 8 columns; secondary panel 4 columns (breakdown, top items, notifications); a full-width (12 column) data table or activity feed.
- Make one KPI or zone lead rather than equal-weight cards (a hero metric spanning the row beats four equal cards).
- Desktop >= lg: sidebar + 12-column grid; tablet md-lg: collapsed sidebar + 8-column grid, secondary panel below primary; mobile < md: no sidebar, single column, KPIs 2x2, charts stack.
- States: loading (skeletons matching each zone), empty (illustration + value-first copy + CTA), error (alert at top + retry; partial data where possible), populated.

## 170. Auth template
- Centred card (max 400px, padding 24px, field gap 16px) with logo, title, form, social auth, secondary link, footer; or a split layout (brand/hero left, form right; brand panel hidden below md).
- Zones: brand (logo, tagline), title ("Sign in", "Create account", "Reset password"), form (email, password, remember, forgot link), social (OAuth), footer (terms, privacy, copyright).
- Login: email + password + remember -> "Sign in"; Register: name + email + password + confirm -> "Create account"; Forgot: email -> "Send reset link"; Reset: new + confirm -> "Reset password"; Verify email: 6-digit OTP -> "Verify".
- Mobile: a full-width card with page inline padding.
- States: loading (submit spinner), error (inline below the field + a top alert for general errors), rate limited (disable submit + countdown), success (redirect or message).
- `<main>` contains the form; allow password managers, no CAPTCHA-only (3.3.8); social buttons `aria-label="Sign in with Google"`.

## 171. Settings template
- Settings nav (3 columns or a sidebar of vertical section links) + content (9 columns).
- Section pattern: title + description, fields, divider, per-section Save (recommended) or a global save.
- Sections: Profile (avatar, display name, email, bio, timezone); Account (username, delete with confirmation); Security (password change, 2FA, active sessions); Notifications (channel toggles email/push/in-app per event); Billing (plan, payment method, invoices table); Team (members table, invite, roles); API (keys table, create key, usage).
- Desktop side nav + content; tablet top tabs + content; mobile nav list as a full page, content as a drill-down with a back button.
- States: loading (active section skeleton), saving (button loading, fields disabled), unsaved (dot/badge on the section nav + confirm on leave), success (inline toast), error (field errors + summary).

## 172. List / detail template
- List panel 4 columns (fixed or resizable: search, filters, scrollable list, load more) + detail panel 8 columns (title, edit, tabs/sections).
- List item: avatar + title + time, preview text, badges, with one differentiator per row.
- Variants: email client, CRM, file browser, documentation.
- Desktop >= lg side by side; tablet list narrows to 3 columns; mobile list on page 1, detail on page 2 with back; on foldables, list on one segment and detail on the other.
- States: loading (8 skeleton items + skeleton content), empty list (illustration + value-first copy + CTA; detail hidden), no selection ("Select an item" placeholder), selected (highlight + content), error (alert + retry in each panel).
- List `role="listbox"` or `<ul>` with `aria-current="true"` on the selected item; detail `<article>` with a heading matching the item; announce mobile panel changes; arrows navigate, Enter opens, Esc returns to the list (mobile).

## 173. Billing settings screen
- Shows current plan, payment method, a billing-history table, and controls to change plan, update card and cancel subscription.
- Cancel subscription wears the danger variant in both trigger and confirm dialog; a blue Cancel fails.
- The confirm dialog traps focus, closes on Escape and returns focus to the trigger.
- The plan area has a focal point; three equal-weight plan cards in a row fail.
- History survives a nine-digit amount, a 60-character description and an empty history.
- The card number is masked with a screen-reader-readable label.
- Copy frontloads the verb; works at 280px; every value comes from tokens.
- Known failures: a primary-blue Cancel, a missing confirm dialog, three identical plan cards, "Something went wrong" errors.

## 174. First-run and empty-state screens
- Design the empty, one-item and forty-item states.
- The empty state explains value, then names the first action.
- The one-item state must not look broken; the forty-item state must not overflow or become an undifferentiated grid.
- Loading is represented with skeleton or progress plus `aria-busy`.
- Nothing is conveyed by colour alone; illustration is a real icon or SVG, never emoji.
- The primary action is keyboard reachable and the visual focal point.
- Known failures: a "No data" empty state, emoji illustration, a wall of identical cards, a missing single-item case.

## 175. Notification centre
- Unread state, types (mention, comment, system, billing), relative timestamps, filters, mark-all-read, and an entrance animation for new items.
- Motion from tokens; respects reduced motion; no content visible only after an animation.
- Type is distinguishable without colour (icon, label or both); unread is never a coloured dot alone.
- Relative timestamps ("2 hours ago") with the absolute time on hover or in a `title`.
- Mark all as read uses non-destructive styling and is disabled with a stated reason when nothing is unread.
- Survives a 200-character body and an empty list.
- Known failures: a reduced-motion branch that never reveals items, unread as a coloured dot alone, emoji types, 600ms animations.

## 176. Page structure and landmarks
- Provide a skip link (first in the DOM) and landmarks (`<main>`, `<nav>`, `<aside>`, `<header role="banner">`).
- A unique, descriptive `<title>` per page; `<html lang>`; mark foreign-language parts with `lang`.
- Every landmark, label, role and accessible name is present.
- Every data-fetching route gets a skeleton loading state and an error boundary (message + retry, never a bare "Something went wrong"); ship a designed 404.
- Group routes by layout archetype: auth = centred card; dashboard = header + sidebar; settings = settings nav + content; resources = list + detail.

# Part 18 — Accessibility

## 177. Baseline and P0 checks (every component)
- Meet WCAG 2.2 AA as the minimum.
- Keyboard navigable: Tab reaches it, Enter/Space activates it, composite widgets answer arrows.
- Focus visible: the focus ring meets 3:1 and is never obscured by a sticky header.
- The screen reader announces name, role and state; proper ARIA roles and live regions.
- Contrast 4.5:1 text, 3:1 UI and graphics, in light AND dark, including hover and focus; 7:1 when targeting AAA.
- Target size >= 24x24px; 44x44px recommended for primary actions (48px recommended on touch; 44px for AAA).
- No colour-only information.
- Reduced motion stops motion without losing content.
- Modals trap Tab, Escape closes, focus returns to the trigger.
- No horizontal overflow 280-951px; no clipped text or overlapping controls; RTL mirrors via logical properties.
- One h1, no skipped heading levels; error text says what, why and how to fix.
- Re-run contrast, focus-visible, target-size and reduced-motion checks after applying any aesthetic direction; brand library specs describe aesthetics, not accessibility.

## 178. WCAG 2.2 additions and priorities
- 2.4.11 Focus Not Obscured: sticky headers and footers must not cover focused elements.
- 2.5.8 Target Size Minimum: all targets >= 24x24px, with exceptions for undersized targets with >= 24px centre-to-centre spacing, inline links in text, label + control measured as one hit area, and disabled controls.
- 3.3.8 Accessible Authentication: no cognitive function tests; allow password managers.
- Also prioritise 2.1.1 Keyboard, 2.1.2 No Keyboard Trap, 2.4.3 Focus Order (modal trap and return), 1.4.11 Non-text Contrast, 1.3.3 Sensory Characteristics, and reduced-motion handling.

## 179. WCAG 2.2 AA checklist: Perceivable
- 1.1.1 (A, P0): text alternatives for all images, icons and controls; decorative `alt=""` or `role="presentation"`; SVG icons `<title>` or `aria-label`.
- 1.2.1 / 1.2.2 (A, P0): captions or transcript; synchronised captions for prerecorded video.
- 1.2.3 (A, P1) / 1.2.5 (AA, P1): audio description for video.
- 1.3.1 (A, P0): structure in markup (h1-h6, ul/ol, th, label associations).
- 1.3.2 (A, P0): reading order matches visual order.
- 1.3.3 (A, P1): instructions do not rely only on shape, size, position or sound.
- 1.3.4 (AA, P1): no orientation lock.
- 1.3.5 (AA, P1): `autocomplete` on personal-data inputs.
- 1.4.1 (A, P0): colour never the sole means; error states need icons; check in greyscale.
- 1.4.2 (A, P0): controls to pause or stop audio playing > 3s.
- 1.4.3 (AA, P0): text 4.5:1; large text (18px bold / 24px) 3:1.
- 1.4.4 (AA, P0): resize to 200% without loss.
- 1.4.5 (AA, P1): real text, not images of text (logos the only exception).
- 1.4.10 (AA, P0): reflow at 320px width with no horizontal scroll (400% zoom single column).
- 1.4.11 (AA, P0): UI components and graphics 3:1 (borders, icons, focus, chart elements).
- 1.4.12 (AA, P1): survive line-height 1.5, paragraph spacing 2x, letter spacing 0.12em, word spacing 0.16em; no fixed heights that clip.
- 1.4.13 (AA, P1): hover/focus content dismissible, hoverable, persistent.

## 180. WCAG 2.2 AA checklist: Operable
- 2.1.1 (A, P0): all functionality by keyboard.
- 2.1.2 (A, P0): no keyboard trap; the user can Tab or Esc out.
- 2.1.4 (A, P1): single-character shortcuts remappable or disableable.
- 2.2.1 (A, P0): time limits extendable, off, or > 20 hours; warn and allow extension.
- 2.2.2 (A, P0): moving, blinking or auto-updating content pausable.
- 2.3.1 (A, P0): no flashing > 3 times per second.
- 2.4.1 (A, P0): skip link and landmarks.
- 2.4.2 (A, P0): unique, descriptive page titles.
- 2.4.3 (A, P0): logical focus order matching the visual layout.
- 2.4.4 (A, P0): link text describes the destination; no bare "click here" or "read more".
- 2.4.5 (AA, P1): multiple ways to find pages.
- 2.4.6 (AA, P1): descriptive headings and labels.
- 2.4.7 (AA, P0): visible focus on every focusable element.
- 2.4.11 (AA, P0): a focused item is not entirely hidden by sticky headers or footers.
- 2.5.1 (A, P1): single-pointer alternatives for multi-point gestures.
- 2.5.2 (A, P1): fire on the up-event; dragging away cancels.
- 2.5.3 (A, P0): visible label contained in the accessible name.
- 2.5.4 (A, P1): motion actuation (shake etc.) has a UI alternative.
- 2.5.7 (AA, P1): every drag has a non-drag alternative (arrows, select).
- 2.5.8 (AA, P0): targets >= 24x24px or adequate spacing.

## 181. WCAG 2.2 AA checklist: Understandable and Robust
- 3.1.1 (A, P0): `lang` on `<html>`; 3.1.2 (AA, P1): `lang` on foreign-language parts.
- 3.2.1 (A, P0): no context change on focus; 3.2.2 (A, P0): none on input without warning.
- 3.2.3 (AA, P1): consistent navigation; 3.2.4 (AA, P1): consistent identification; 3.2.6 (A, P1): consistent help placement.
- 3.3.1 (A, P0): errors identified in text and announced; 3.3.2 (A, P0): labels and instructions; 3.3.3 (AA, P1): error suggestions; 3.3.4 (AA, P1): error prevention for legal, financial and data submissions.
- 3.3.7 (A, P1): no redundant entry; 3.3.8 (AA, P0): accessible authentication.
- 4.1.2 (A, P0): name, role and value for all components; 4.1.3 (AA, P0): status messages via live regions without focus change.
- Priority tiers: P0 must fix (legal exposure, blocks users), P1 should fix (significant usability), P2 nice to have.

## 182. WCAG AAA upgrade
- Treat AAA as a prioritised enhancement list for high-support audiences (government, healthcare, education), not a pass/fail gate.
- 1.4.6: contrast 7:1 normal, 4.5:1 large.
- 1.4.8: line <= 80ch, line-height >= 1.5, no justification, user control of colour and width.
- 1.4.9: no images of text at all.
- 1.2.6-1.2.9: sign language, extended descriptions, live captions and audio-only alternatives (media-heavy products).
- 2.1.3: all functionality keyboard-operable, no exceptions.
- 2.2.3: no time limits; 2.2.4: users can postpone or suppress non-emergency interruptions.
- 2.3.2: no flashing at all.
- 2.4.8: show location; 2.4.9: link text alone is unambiguous.
- 2.4.12: focus never obscured (fully visible); 2.4.13: thick high-contrast focus (>= 2px perimeter, 3:1 change), offset.
- 2.5.5: targets 44x44px (use `control.lg` 48px).
- 3.1.3-3.1.6: define unusual words, expand abbreviations, lower-secondary reading level, pronunciation.
- 3.2.5: no automatic context changes (no auto-redirect or refresh).
- 3.3.5: context-sensitive help (inline help, tooltips).
- 3.3.6: error prevention for all submissions.
- 3.3.9: no cognitive test for authentication, no exceptions.

## 183. ARIA general patterns
- Prefer native elements; `role="button"` on a non-button needs `tabindex="0"` + Enter and Space handlers, and Space activation must prevent scroll; no `<div onclick>` buttons.
- Use `<button>` for actions and `<a>` for navigation.
- Toggle buttons use `aria-pressed`, not `aria-checked`.
- Icon-only buttons need `aria-label` or visually hidden text.
- Roving tabindex for composites: the container is a single tab stop; the active child has `tabindex="0"`, others `-1`; arrows move it; Tab exits the widget.
- Composite widgets (tablist, listbox, tree, grid, menu, radiogroup, toolbar) use roving tabindex with working arrow keys (or a moving `aria-activedescendant`) and at least one keyboard entry point.
- Dialog: `aria-modal`, labelled and described; focus the first focusable element (or the dialog); trap; restore; background `aria-hidden`, or native `<dialog>` + `inert`.
- Grid: `role="grid"` > `row` > `gridcell` / `columnheader` / `rowheader`; arrows between cells; Home/End row edges; Ctrl+Home/End corners; `aria-sort` on data-grid headers.
- State changes are visible, not only announced (a theme toggle changes its icon or text, not just `aria-checked`).

## 184. Interaction accessibility requirements
- Sort controls are real buttons, not click handlers on divs; headers announce sort state with `aria-sort`.
- Never make a whole row the only click target without a keyboard equivalent.
- Give row selection a non-colour cue in addition to colour.
- Distinguish notification types and unread state without colour (icon, label or both).
- Represent loading honestly with a skeleton or progress plus `aria-busy`, not a frozen screen.
- Mask sensitive numbers (card number) with a screen-reader-readable label.
- Show relative timestamps with the absolute time available on hover or in a `title`.
- Keyboard keys to cover: Tab, Enter, Space, Escape, Arrows.

## 185. Manual testing protocol
- Keyboard-only full flow: logical tab order, all actions reachable, focus visible, never trapped or obscured.
- Screen-reader walkthrough with at least two readers (VoiceOver, NVDA, Orca): name/role/state announced; dynamic changes announced; form errors announced on appearance; modal open/close announced with focus managed; SPA route changes announced; live regions fire; custom widgets (listbox, tree, date picker) checked.
- Zoom 200% and 400% reflow; a 320px viewport; the 200% text-spacing override (text-spacing bookmarklet).
- Colour-blindness simulation; `prefers-reduced-motion`; Windows High Contrast / forced-colours mode.
- Automated scanners catch only part of the problems (estimates range from ~30-40% to ~57% of WCAG issues); never treat an automated pass as complete.
- Audit output: a findings table with WCAG criterion (e.g. 1.4.3), severity (P0/P1/P2), what fails and a specific fix; confirm passes explicitly.

## 186. Cognitive accessibility
- Reduce load before explaining: every field, choice and step has a cost.
- Recognition over recall: show options, keep entered data visible, persist context across steps.
- One primary action per view; progressive disclosure for secondary and advanced paths.
- Be predictable: consistent navigation and identification; no context change on focus or input.
- Forgive errors: confirm destructive actions, allow undo, autosave, review before submit.
- Plain language: lower-secondary reading level, frontload the point, short sentences, common words, active voice; define jargon and acronyms on first use; one idea per paragraph; chunk with lists and headings.
- Keep instructions visible while the task is performed, not only in a dismissed dialog.
- Avoid timeouts; if needed, warn and allow extension; persist progress.
- Minimise concurrent decisions, default sensible values, remember preferences.
- Break long flows into stepped flows showing position, remaining steps and effort.
- Make the next action obvious; never hide the only way forward behind a gesture or hover.
- Verify: read labels and errors aloud for a tired first-time user; the task completes without remembering prior screens; remove any timeout, puzzle or transcription step.

## 187. Dyslexia and reading
- Body >= 16px, line-height 1.5, generous paragraph spacing, line length 45-75ch.
- Left-align body text; never justify; avoid all-caps running text.
- Use a clean sans (Inter, system-ui) or offer an OpenDyslexic option; never convey meaning by italics alone.
- Strong heading hierarchy and whitespace for scannability.

## 188. Reduced data and low bandwidth
- Respect `prefers-reduced-data` / Save-Data: skip autoplay media, heavy fonts and large hero images; serve text first.
- Do not block core tasks behind large downloads; prefer skeletons.

## 189. Colour-vision deficiency
- About 8% of men and 0.5% of women are affected; red-green (deutan/protan) is most common, tritan rarer, achromatopsia rarest.
- Never encode meaning in hue alone: pair with icon, text, shape or pattern (status, chart series, required marks, map regions).
- Do not rely on red vs green for success/error; add pass/fail icons and labels.
- Charts: marker shape + dash pattern + direct labels + a colour-blind-safe palette (Okabe-Ito based); cap series.
- Test deuteranopia, protanopia, tritanopia and greyscale; if information disappears in greyscale, it failed.

## 190. Low vision
- Support 200% zoom with no loss and 400% reflow to a single column at 320px; use logical properties and relative units.
- Respect the user's base font size (rem; iOS Dynamic Type / scaled metrics; Android `sp`).
- Survive 1.4.12 text-spacing overrides; no fixed heights that clip.
- Keep a >= 3:1 focus indicator that sticky headers never obscure.
- Keep clear hierarchy and generous spacing for magnifier users.
- At 4K, content does not stretch infinitely.

## 191. Light sensitivity and dark mode
- Provide light and dark themes that honour `prefers-color-scheme`.
- Avoid pure black on pure white for large text blocks (halation); use tuned surfaces and text.
- No flashing > 3 per second.

## 192. High contrast and forced colours
- Adapt in `@media (forced-colors: active)` using system keywords (CanvasText, Canvas, ButtonText, LinkText, Highlight), never hex.
- Do not convey state with background colour alone (it is flattened); add borders, outlines or icons.
- `forced-color-adjust: auto` for most UI; `none` only for must-keep-colour items (a chart swatch) with a non-colour cue.
- Use real `<svg>` with `currentColor` so icons take forced colours.
- Verify borders, focus and icons survive high-contrast emulation.

## 193. Internationalisation: logical properties
- Use flow-relative CSS: `margin-inline-start` / `padding-inline-end` (not left/right), `inset-inline-start/end`, `text-align: start`, `border-inline-start`, `inline-size` / `block-size`.
- Set direction once on the root (`<html dir="rtl" lang="ar">`); use the native leading/trailing equivalents on SwiftUI, Compose and Flutter.

## 194. RTL mirroring
- Mirror: layout flow, alignment, directional icons (arrows, back/forward, send, progress, chevrons), sliders, breadcrumbs, carousels.
- Do not mirror: time-independent media, logos, phone numbers, code, checkmarks, most pictographic icons (clock, search), media playback controls (verify per market).
- Isolate numbers and embedded LTR runs (URLs, emails, code) with `<bdi>` / `unicode-bidi: isolate`.
- Verify by flipping `dir="rtl"` and confirming full mirroring with no hard-coded left/right and no new overflow.

## 195. Text expansion and strings
- Plan for translations 30-40% longer than English (German and Finnish more); CJK is shorter but taller.
- Never fix widths to English; let buttons and labels grow and wrap; avoid truncating essential labels (otherwise show the full text on hover/focus + `title`).
- Test with a pseudo-locale (e.g. `[!!! Ŝȧṽḗ ƈħȧńɠḗŝ !!!]`) for clipping, overlap and concatenation.
- Never concatenate sentence fragments; use full strings with named placeholders (`{count} items`) and ICU plural/select.
- Externalise all user-facing strings.

## 196. Locale formatting
- Format dates, times, numbers, currency and units with locale-aware formatting (`Intl.*`); respect separators and first day of week.
- Do not assume first/last name order or US address and phone shapes.
- Respect script coverage and tall-script leading (see Thai and complex scripts).

# Part 19 — UX writing, voice & tone

## 197. Voice principles
- Voice is constant (who we are); tone adapts to context.
- Clear: plain language over jargon ("Sign in", not "Authenticate session").
- Concise: cut every word not pulling weight ("Email is required", not "The email field cannot be left empty").
- Useful: tell the user what to do next ("Add numbers or symbols", not "Invalid password").
- Human: talk like a calm person ("Something went wrong on our end", not "Error 500: Internal failure").
- Honest: never blame the user, never overpromise ("We couldn't save your changes", not "You did something wrong").

## 198. Tone spectrum
- Onboarding / empty state (curious, unsure): encouraging, warm.
- Success (accomplished): brief, affirming ("Changes saved.").
- Routine action (focused): neutral, transparent ("Uploading 3 files...").
- User-fixable error (frustrated): calm, directive ("Password must be at least 8 characters.").
- System-fault error (confused): reassuring, accountable ("We couldn't load this. Try refreshing in a moment.").
- Destructive confirm (cautious): direct, specific ("Delete 4 items? This can't be undone.").
- The higher the user's stress, the plainer the language; never use humour in errors, payments or destructive actions.

## 199. Buttons and actions copy
- Start actionable text with the verb ("Save changes", not "Click here to save your changes"; "Invite teammates", not "You can invite teammates here"; "Export report", not "Report exporting"; "Change plan", not "Click here to change your plan").
- Buttons are verbs, not nouns; label the outcome, not the mechanism ("Create account" beats "Submit").
- Verb + object, <= 3 words ("Save draft", "Delete account"); brand systems keep labels to two words or fewer ("Sign up", "Learn more", "Log in").
- Pair one filled CTA with one borderless text CTA with a trailing chevron or arrow.
- Disabled actions state a reason when unavailable (e.g. nothing unread).

## 200. Error messages
- Order: what happened -> why (drop if obvious) -> how to fix.
- Examples: "Enter a valid email, like name@example.com"; "That password doesn't match. Try again or reset it."; "File is too large (max 10 MB). Try compressing it."; "You're offline. We'll retry when you reconnect."; "Password must be at least 8 characters. Try adding numbers or symbols."
- Never expose stack traces, error codes alone, a bare "Something went wrong", or "Oops!" with no path forward; an error without a next step is a dead end.

## 201. Empty-state copy
- Formula: what goes here and why it's useful -> primary action ("No projects yet. Create your first project to organize your work." + [Create project]).
- Distinguish first-use empty (guide) from cleared empty (reassure: "Your inbox is clear. New messages will appear here.").
- Never "No data", "Nothing to show" or a bare "Error".

## 202. Microcopy patterns
- Confirmations: state the consequence + count ("Remove 12 contacts? This can't be undone."); the title asks and the button answers in matching words.
- Placeholders show format, not instruction, and never substitute for a label ("name@example.com").
- Helper text sets expectations before the error ("Use 8+ characters with a number").
- Toasts: one line, past tense for success ("Link copied").
- Loading says what's happening ("Generating report..." not "Please wait").
- Tooltips add information and never repeat the label ("Visible only to your team").
- Labels: sentence case, no colon ("Email address", not "Email Address:"); in quiet brand systems, plain nouns ("Work", "About", "Archive", "Show more").
- Badges read like labels ("Online exclusive", "New addition").
- Stay within character limits for tight UI.

## 203. Capitalisation and mechanics
- Sentence case for everything: buttons, labels, headings, menus.
- No terminal punctuation on labels, buttons or single-sentence tooltips; periods in multi-sentence body and error messages.
- Numerals for all numbers ("5 items").
- Oxford comma in lists.
- Contractions welcome ("you're", "can't").
- Avoid ALL CAPS for emphasis (shouting, and it hurts screen readers), exclamation marks (max one per screen), and "please" in routine actions.

## 204. Inclusive and translatable language
- Address the user as "you"; refer to the product as "we" sparingly; never "I".
- No idioms or cultural references that don't translate ("piece of cake", "home run").
- No directional-only or sense-only instructions ("the button on the right", "the green one"); pair with a label.
- No ableist metaphors ("crazy", "blind to", "sanity check" -> "quick check").
- Gender-neutral: "they" for unknown users; avoid "guys".
- Write for translation: short sentences, one idea each, no stacked nouns, no string concatenation.

## 205. Brand voice in quiet systems
- Sentence case, never shouted, never exclamatory.
- State values plainly as headings ("No ads, no personalized recommendations").
- Project and product descriptions are one factual sentence; truncate rather than paraphrase.
- Microcopy is short, active and consistent; avoid generic filler.
- Preserve style personality in headlines while keeping UI labels literal.

## 206. Pre-ship copy checklist
- Every button starts with a verb and names the outcome.
- Every error says what happened, why and how to fix it; no dead ends.
- Every empty state gives value, then guides to a first action.
- Sentence case throughout; no ALL CAPS.
- No jargon, error codes or stack traces shown to users.
- No blame on the user; system faults owned by "we".
- Labels present (placeholders are not labels).
- No directional or colour-only instructions.
- Numbers as numerals; counts shown in confirmations.
- Inclusive language; within character limits and translatable.
- Reads naturally aloud; if robotic, rewrite.

# Part 20 — Edge cases & content reality

## 207. Content is hostile
- Design and test for long unbroken strings (60-character names, emails with no spaces), empty lists, one item, many items (forty rows), nine- or ten-digit numbers, missing values and missing images.
- Spec edge cases at handoff: long text, empty, overflow, single item, many items.
- Use real or plausible content, never lorem ipsum, "Item 1" or "No data"; placeholder data shipped as real is a lie users catch.

## 208. Content edge cases
- Long text 50+ characters: decide truncate-with-ellipsis or wrap.
- Empty content: empty-state illustration plus CTA.
- Single item: the layout still makes sense and does not look broken.
- Many items (100+): paginate or virtual scroll; forty items must not overflow or become an undifferentiated grid.
- Special characters: Unicode, emoji in user content, RTL text, HTML entities.
- Missing optional fields: avatar without image, card without description.
- Number extremes: $0.00, $999,999.99, negatives, NaN, nine-digit amounts.
- Truncate long values on purpose with a `title` tooltip, or wrap; never let values silently disappear or clip without an ellipsis.
- Test bodies of 200 characters and descriptions of 60-80 characters.

## 209. Layout edge cases
- A 320px viewport with no horizontal scroll (and the 280px floor).
- A 4K display: content does not stretch infinitely.
- 200% zoom: all content visible, no overlap.
- Dynamic type and browser font scaling (test at 1.25x root font).
- Long unbroken words wrap (`overflow-wrap`).
- A no-JS fallback where applicable.

## 210. Interaction edge cases
- Prevent double submission on double click.
- Debounce rapid clicking where needed.
- Handle browser back in SPAs.
- Refresh: preserve form state or refetch data.
- Offline: an error message or cached content.
- Concurrent edits by two users.

# Part 21 — Aesthetic systems

## 211. Applying an aesthetic direction
- Do brief inference first (domain, audience and tone, mood adjective, motion depth, layout sequence) before any tokens.
- Choose two or three candidate systems matching the brief's positioning, not only its industry; a brand named in the brief ("feel like Stripe") goes straight to that system.
- Pick an archetype (high-end agency, editorial minimal, brutalist, soft-SaaS, dark-tech, morphism) or a named design system; never write a named system's spec from memory; if the real spec is unavailable, fall back to an archetype.
- Resolve the direction into tokens (override semantic tokens, keep primitives): colours to semantic tokens (verify every pair), typography to type tokens (keep the composite text-style structure), spacing to the spacing scale and grid, radius to border tokens, elevation and effects to shadow, blur and gradient tokens, motion to motion tokens and choreography, components through the component specs.
- Treat measured brand values as what a site shipped, not what is allowed: snap spacing to the nearest token, fix sub-AA contrast, substitute a licensed or open face, and state which values changed.
- Add purposeful motion, render, then run the pre-flight aesthetic check and re-run accessibility checks.

## 212. Archetype: High-End Agency (Linear / Apple tier)
- When: premium products, launches, anything that must feel expensive.
- Type: large display scale (6xl-7xl), tight leading, wide measure; one UI sans.
- Colour: off-black on warm or cool near-white; a single restrained accent; calibrated low chroma.
- Space: generous macro-whitespace; asymmetric grids; edge tension.
- Depth: hairline borders + subtle layered elevation; shadows rare.
- Motion: precise, fast, ease-out; scroll reveals with restraint.
- Kin: Linear, Apple, Vercel, Stripe, Superhuman.

## 213. Archetype: Editorial Minimalism
- When: content, docs, marketing with a literary tone.
- Type: serif or refined sans headings; strict 60-75ch measure; strong scale contrast.
- Colour: paper/ink neutrals; one ink accent.
- Space: column grids, lots of air, baseline rhythm.
- Depth: flat; rules and whitespace separate, not boxes.
- Kin: Notion, Wired, publication styles.

## 214. Archetype: Industrial Brutalism / Tactical
- When: data-heavy dashboards, dev tools, a declassified-blueprint vibe.
- Type: monospace or grotesque; extreme scale contrast; mono kickers and labels.
- Colour: utilitarian black/white + one signal colour; analog textures optional.
- Space: rigid modular grids, high density, visible structure.
- Depth: hard edges, thick borders, no soft shadows.
- Kin: brutalism, neobrutalism, mono, Warp, The Verge.

## 215. Archetype: Warm Soft-SaaS
- When: friendly consumer and productivity apps, onboarding-heavy products.
- Type: rounded humanist sans; medium scale contrast.
- Colour: warm neutrals + a friendly accent; soft pastels as support.
- Space: comfortable padding, soft radii (`radius.lg` and up), dense bento grids of tight content-rich tiles, never large mostly-empty blocks.
- Depth: soft shadows allowed; chunky tactile elements optional.
- Kin: Duolingo, Intercom, Zapier, Xiaohongshu.

## 216. Archetype: Dark-Tech / Cinematic
- When: AI, crypto, gaming, infra; high-drama dark surfaces.
- Type: tight sans or mono; bright type on dark.
- Colour: void-black surfaces, neon or gradient accents, desaturated supporting hues.
- Space: bounded media at dramatic scale (capped at 60vh); drama from contrast and type, not from filling the viewport.
- Depth: glow, gradient and glass, each used once, never stacked.
- Kin: ElevenLabs, Runway, Cursor, Revolut, SpaceX, Shopify.

## 217. Archetype: Morphism and effects
- When: a specific tactile gimmick is the point (glassmorphism, claymorphism, neumorphism, skeuomorphism, gradient, neon).
- Use the matching effect system's strict execution rules rather than improvising; contrast, focus and target rules still apply.

## 218. Matching a reference image
- Infer palette: one dominant surface family, text colours, one primary action plus at most one accent; sample hues, never guess hex.
- Infer type: family feel (geometric, grotesk, serif), scale jumps, display vs body contrast, weights.
- Infer spacing and density: base unit, section rhythm, card padding, airy vs compact.
- Infer radius and depth: sharp/soft/pill; shadow vs hairline separation.
- Infer layout archetype and sequence: bounded hero, asymmetric split, dense bento, editorial stack.
- Anchor to a known system if close, to stabilise decisions.
- Build one 3-tier token theme from the inferred values; no per-section palettes; verify every pair in light and dark and adjust sampled brand colours that fail AA.
- Rebuild with one shared primitive layer, all 8 states, accessibility wired, no emoji, a single theme; apply taste so it does not regress to generic.
- Render and compare side by side with the reference; it should visibly match the design language.
- Match the system, not a pixel-perfect copy; never reproduce the reference's photos, logos or copyrighted copy; substitute your own or generic placeholders.

# Part 22 — Brand design-system anatomy & category style patterns

## 219. Design-system document: token header
- Open with machine-readable tokens: `name`, `category`, a one-sentence `description`, then `colors`, `typography`, `rounded`, `spacing`, `components`.
- Write the description as a dense fingerprint: canvas hex, ink hex, the one accent, headline face + size/weight, body face + size, button radius/height/padding, footer colour.
- Name colour tokens by role: primary, primary-hover, canvas, ink, ink-muted, ink-strong, on-dark, on-primary, surface-alt, footer, badge, hairline, chip-border, disabled-bg, disabled-text.
- Name type tokens by role and breakpoint: display, display-mobile, display-sm, hero-title(-mobile), page-title, tab, footer-heading, lead, price, body, body-tile, product-name, button, footer-link, nav, utility, breadcrumb.
- Reference tokens by name in prose (`{colors.ink}`, `{typography.display}`, `{rounded.chip}`).

## 220. Design-system document: section order
- Overview: atmosphere metaphor, layout walkthrough, voice, density, and a Key Characteristics list of 5-8 bullets.
- Colours: Brand & Accent / Surface / Text / Semantic & State, each value with where it is used.
- Typography: Font Family / Hierarchy table (token, family, size, weight, line-height, where) / Principles / Note on Font Substitutes.
- Layout: Spacing System / Grid & Container / Whitespace Philosophy.
- Elevation & Depth: a level table (Level, Treatment, Use) plus Decorative Depth.
- Shapes: Border Radius Scale / Other Shapes / Photography Geometry.
- Components: Buttons / Cards & Containers / Inputs & Forms / Navigation (incl. Footer, Links, Tabs) / Pills, Tags, Chips / Signature Components.
- Design System Architecture: token architecture, theming, type and spacing system, component model, accessibility, delivery.
- Do's and Don'ts.
- Responsive Behaviour: Breakpoints / Measured changes at mobile / Touch Targets / Collapsing Strategy / Image Behaviour.
- Iteration Guide: a numbered build order ending in a verification checklist.
- Optional: Art Direction (hero, bands, density, motion cues) and Voice & Microcopy.
- A style-family (non-brand) variant uses 9 sections: Visual Theme & Atmosphere, Colour, Typography, Spacing & Grid, Layout & Composition, Components, Motion & Interaction, Voice & Brand, Anti-patterns.

## 221. Specification discipline
- Record measured values, not rounded guesses; keep fluid/clamp-computed sizes exact (e.g. 48.8288px at 1280px) rather than "nice" numbers.
- Measure at least desktop 1280px and mobile 390px and document what changes between them.
- Rank colours by real usage (weighted characters, painted area) to decide which is ink and which is on-dark.
- Mark one-off or leftover values (a stray font on one heading, unused shadows, reserved tokens) as do-not-adopt.
- When documentation and the live product disagree, follow the live product.
- Name proprietary fonts and give substitute guidance: keep measured sizes, line heights and weights; swap only the family (neo-grotesque for a grotesk, flared sans for an Optima-type, etc.).
- State the hover mechanism and the depth strategy explicitly (shadow scale, colour stepping, translucency, photography).
- End with a checklist of the few numbers that define the system (radius set, button height, type sizes).
- Style-family defaults: transitions 150-250ms with stable easing; hierarchy headline -> support text -> primary action; whitespace before borders or shadows; no off-palette colours; do not flatten hierarchy with one size or weight; do not mix unrelated visual metaphors.

## 222. Brand button and action patterns
- Common button specs: 48px tall `13px 24px 12px` with 0px radius; 40px tall `12px 16px` with 4px; 40px pill `0 20px` with 32px radius; 39px pill `9px 28px` with 30px radius.
- Secondary actions as translucent fills (`#afb2ce33`) or hairline ghosts (`1px solid` ink at 20% alpha), not solid strokes.
- Ghost on imagery: transparent with an on-dark label and a 1px on-dark border.
- One filled CTA paired with one borderless text CTA with a trailing chevron or arrow.

## 223. Accessibility in brand systems
- Put "skip to content" links first in the DOM.
- Include `@media (forced-colors: active)` rules.
- Keep a two-ring focus indicator (inner surface colour, outer accent).
- Inputs 40px, buttons 40-48px, large buttons 56px; filter chips may be 27-29px only with adequate spacing.

## 224. Luxury and beauty
- Warm cream or black canvas, graphite ink, no chromatic CTA (graphite, black, white, or one deep heritage green).
- 0px radii on buttons, inputs and tiles; 2px at most.
- Light weights (100-300) or 400 display; uppercase tracked labels (0.55-1.6px) common in fashion and automotive luxury.
- A serif or humanist face reserved for editorial titles; grotesk for UI.
- No shadows, gradients or glassmorphism; depth from warm low-key photography (amber glass, wood, paper) and dark footer bands.
- A literary, unhurried voice.

## 225. Fintech and banking
- Two modes: dark cinematic (indigo-black `#171721`, one electric accent `#5266eb`) or light friendly (white + mint or soft tint cards, navy pills).
- Pill CTAs (32px-500px radius), 40px tall; one filled accent per band, all others frosted or translucent.
- Big radii on cards (12-32px) and blocks; the coloured brand "object" stays off buttons.
- Heavy display weight (700-800) or custom variable weights; line-height 1.4 body / 1.2 headings.
- Painterly or warm photographic heroes; product UI shown dim or as exaggerated vignettes.
- Crypto exchanges: a near-black canvas with a single signal yellow or blue and 8-20px radii.
- Disclaimers collected at the page foot in 12px.

## 226. Consumer electronics
- Greyscale canvas (`#f4f4f4`), near-black ink and fills, one accent (`#ffc700`) for a single action.
- Small radii (4px buttons and fields, 6-8px tiles); no shadows; translucent glass over blurred photography.
- Multi-voice type: a display grotesk, dot-matrix labels, uppercase mono 11px nav and callouts, a separate long-form face.

## 227. Editorial, gallery and agency
- Achromatic UI, chromatic work; one typeface at one weight (400) for nearly everything.
- Display ~52px with -0.02em tracking and tight 1.05 leading; body 1.25 in dense grey blocks.
- Bands alternate white / `#222222` / black as "rooms".
- The only interactive fill is a translucent chip (`#00000012` light, `#ffffff1f` dark, 4px radius).
- Document-like products: a single narrow column, 19.2px body at 1.45, no display type, 3px radii, one navy accent, ambient glows, ~130px section gaps with hairlines.
- No icons beyond search and chevron; no underlined links where the system forbids it; no blue links.

## 228. News and publishing
- White canvas, near-black ink, one red or brand accent for breaking and brand moments.
- Dense multi-column grids; uppercase section titles; serif headlines with sans UI or vice versa.
- Square 0-3px corners or small 10px cards; flat surfaces.

## 229. Gaming
- Black or deep navy image-filled canvas; UI floats on full-bleed key art (still capped by screen economy).
- Square 0px CTAs and badges in the heaviest weight (900), uppercase, with a trailing chevron, or large pills, per publisher.
- CTA colour follows context: an evergreen lime, campaign takeover recolours (temporary), tier colours on plan cards.
- Big headline tracking -1% of size; only badges positively tracked.
- Never box text over art; put it on the darkest area.
- An icon quick-nav row with outline icons and uppercase labels under the hero.

## 230. Sports and fitness
- One signal colour (orange `#fc5200`) used flat for the primary action, active underline, wordmark and "NEW" tag.
- Warm near-black neutrals, white canvas, sand footer.
- Rectangular 4px desktop buttons; a 56px pill CTA on mobile.
- Hover by darkening; no shadows.
- Real athlete photography; illustration limited to a hand-drawn route line.
- A low-density sign-up column; an extended-width face only for marketing display.
- Dark gyms and boutiques: black canvas, uppercase display, tight negative tracking, square buttons.

## 231. Education
- White canvas, near-black ink (never pure black), one indigo or green CTA, 8px marketing / 4px product radius.
- Headings always 700, reading 400-500; italic on the emotional headline word.
- Pill subject chips (100px radius, 1px border, coloured geometric icon, 66px tall).
- Colourful testimonial cards (sunflower, leaf, tangerine) at 16px radius; nearly flat (max 2px blur shadow; deepest `0 8px 16px` at 16% alpha).
- Do not mix marketing and product accent colours on one screen.
- Universities: serif headlines, square corners, flat.

## 232. Outdoor and apparel
- Photography-first, near-monochrome chrome (black ink, white canvas, `#f5f5f5` tiles at 8px).
- Light body weight (300) for reading, 500 for scanning; 700 only for activism italics.
- Headings tracked -0.02em at line-height 1.1; no uppercase transforms.
- 30px-radius pill buttons, black on light, white on dark; no chromatic button colour.
- A serif face only for editorial stories; one flat navy field and one activism orange, never tinted.
- The header is raised with a soft three-layer shadow; the rest is flat.

## 233. Government, healthcare and nonprofit
- A clear single action colour (clinical blue or green, navy), 4-5px radii, underlined links that change hue on hover.
- 17-20px body text in government systems; light 300 large headlines acceptable.
- Multilingual fallbacks in the font stack (Thai, CJK, Arabic, Burmese, Khmer).
- Nonprofits: documentary photography, one warm signal yellow, cream bands.

## 234. Developer tools and SaaS
- Deep navy or violet bands, bold display with strong negative tracking (-1 to -4px), one blue CTA 48-56px tall with an 8px radius or pill.
- Mono uppercase labels with positive tracking; floating product screenshots.

# Part 23 — Platform conventions

## 235. Cross-platform token contract
- The token layer comes first; each platform maps the same semantic tokens into its native theme system; light/dark swap at the semantic tier.
- Support multi-brand and density switching through extra theme blocks (`[data-theme="..."]`, `[data-density="compact"]`) where the target allows runtime switching.
- Map duration and easing tokens to the platform's animation API and gate every animation on the platform reduce-motion setting with a fade or instant fallback.
- Support dynamic type and scaled metrics; adapt per platform rather than porting web visuals literally.

## 236. Apple / SwiftUI (HIG)
- Back semantic colours with system adaptive colours: text `.label` / `.secondaryLabel` / `.tertiaryLabel`; surfaces `.systemBackground` / `.secondarySystemBackground` / `.tertiarySystemBackground`; borders `.separator` / `.opaqueSeparator`.
- Brand colours live in Asset Catalog colour sets with Any/Dark appearances.
- Type scale (pt): h1 48 bold, h2 36 bold, h3 30 semibold, h4 24 semibold, h5 20 semibold, h6 18 semibold; body 18/16/14 regular; caption 12; label 14 medium; code 14 monospaced.
- Spacing scale (pt): 2, 4, 8, 12, 16, 20, 24, 32, 48.
- Implement buttons as a `ButtonStyle` (variants via `configuration.isPressed`, reading `@Environment(\.isEnabled)`), not ad-hoc modifiers; 6pt continuous corner, 1pt stroke on secondary, pressed animation `.easeOut(0.15)`, disabled opacity 0.5.
- Cards as a `ViewModifier`: 8pt radius, outlined (1pt separator) or elevated (black 5% shadow, radius 2, y 1), 24pt padding.
- Scale custom metrics with Dynamic Type (`@ScaledMetric(relativeTo: .body)`; icon default 20pt).
- Give icon-only buttons a state-aware `accessibilityLabel` ("Add to favorites" / "Remove from favorites") plus a hint.
- Expose slider values as spoken values ("42 percent").
- Combine related elements (`.accessibilityElement(children: .combine)`) with one summarised label ("Rating: 4.8 out of 5, 128 reviews").
- Post an accessibility announcement on async completion ("Changes saved").
- Read `accessibilityReduceMotion` and pass a `nil` animation when set; default spring 0.3s.
- iOS uses `NavigationStack` with typed destinations; macOS uses `NavigationSplitView` (sidebar + detail).
- Use `ViewThatFits` to fall back from a horizontal (16pt gap) to a vertical (8pt gap) label/control layout.

## 237. Android / Jetpack Compose (Material)
- Map colours to light + dark `ColorScheme` and type to `Typography`; carry spacing, radius, size, opacity and motion in a `CompositionLocal`.
- Pick the dark scheme from `isSystemInDarkTheme()`.
- Disable with `enabled = false` (the system dims and blocks).
- Declare `Role.Button` and `contentDescription` / `stateDescription` in semantics.
- Minimum touch target 48dp; respect `sp` for user font scaling.
- Animate with `animate*AsState` / `AnimatedVisibility` using token durations; snap to target when the system disables animation.
- Disable the Material ripple if it conflicts with reduced-motion expectations.

## 238. Flutter (Material)
- Encode tokens as a `ThemeExtension`; colours to `ColorScheme`, type to `TextTheme`; dark = a second `ThemeData`, switched via `themeMode`.
- Disabled = `onPressed: null`.
- Wrap custom controls in `Semantics(button: true, enabled, label)`.
- Minimum tap target 48x48.
- Honour `MediaQuery.disableAnimations` with an instant or opacity-only change.

## 239. React Native (touch)
- Resolve light/dark token maps via `useColorScheme()`; there are no CSS variables.
- Set `accessibilityRole`, `accessibilityState` (disabled, busy, selected) and `accessibilityLabel` on every control.
- A focus ring is N/A on touch; provide a clear pressed state instead.
- Minimum target 44x44.
- Never depend on hover (it exists only on web and TV targets).
- Honour `AccessibilityInfo.isReduceMotionEnabled()` with an opacity or instant fallback.

## 240. Web component libraries (Material UI, Bootstrap, Chakra, Mantine)
- Material UI variant map: primary = `contained`, secondary = `outlined`, ghost = `text`, destructive = `color="error"`; map surfaces to `palette.background.default/paper`, the 4px base to `spacing`, radius to `shape.borderRadius`, elevation to `shadows[]`.
- Override opinionated library defaults (Bootstrap heavy shadows, 0.375rem radius and its gray ramp; Material elevation and spacing; Mantine spacing and radius) to your tokens instead of accepting them.
- Libraries rarely cover error, loading and selected states; add them with semantic tokens.
- Keep library overlay primitives (Modal, Dropdown, Offcanvas, Dialog, Menu, Autocomplete) for focus trap and Escape rather than reinventing them, but still validate them against the ARIA patterns.
- Keep library focus rings but verify 3:1 against your surfaces (Mantine `focusRing: 'auto'`).
- Mantine: map 10-shade palette tuples, `primaryColor` + `primaryShade`; set `respectReducedMotion: true`.

## 241. Web: utility-class styling
- Never use raw palette utilities (`bg-gray-500`, `text-blue-600`, `border-red-400`, or any `{bg|text|border|ring|ring-offset|fill|stroke|from|via|to|divide|outline|decoration|accent|caret|placeholder|shadow}-{slate...rose}-{50...950}`).
- Map semantic tokens into the theme layer (`--color-action-primary`, `--radius-button`, `--shadow-focus-ring`) and use semantic utilities (`bg-action-primary`, `rounded-[var(--radius-button)]`).
- Control heights map to `h-8 / h-10 / h-12`; icon-label gap `gap-2`; default micro-transition `transition-colors duration-150`; gate motion with `motion-safe:` / `motion-reduce:`.

## 242. Web: frameworks, components and islands
- Load fonts through the framework's font optimiser (no external CSS font imports) and expose them as `--font-sans` / `--font-mono`; reference stack `"Inter", system-ui, -apple-system, sans-serif`; mono `"JetBrains Mono", "Fira Code", monospace`.
- Web Components: CSS custom properties on `:root` pierce shadow DOM; style focus inside the shadow root; use `delegatesFocus: true` for composite widgets; label carefully across shadow boundaries.
- Islands architectures own overlay focus management in the hydrated island; server-render `disabled` / `aria-*` so state is correct before script runs.
- Hydrate selectively: on load for above-the-fold interactive parts, on visible for below-fold, on idle for non-critical; never hydrate purely presentational components.
- Wrap page view transitions in a reduced-motion guard.

# Part 24 — Critique & review method

## 243. Pre-flight aesthetic check (12 points)
- No heading wraps past ~3 lines; display type is wide and short.
- Adjacent sections do not share the same layout archetype.
- Body text constrained to 60-75ch.
- One primary colour + at most one accent; neutrals carry the rest.
- Off-black text on a warm or cool white surface (no pure `#000` / `#fff`).
- Generous section-level whitespace; spacing hierarchy outer > inner.
- Depth from layered surfaces and hairlines, not a shadow on every box.
- Bento or grid has no empty dead cells; alignment is exact.
- All interactive elements have hover + focus + press states.
- No emoji anywhere; no "SECTION 01" filler; no invisible button text.
- Reduced-motion fallback present.
- Every value traces to a token; nothing hardcoded.

## 244. Adversarial critic stance
- Assume the work is mediocre until the render proves otherwise; the burden of proof is on the work; argue for rejection.
- Critique in a fresh context without the maker's reasoning; a critic holding the maker's argument reviews the argument, not the artifact, and agrees too easily.
- Run critique after objective checks are green, never instead of them.
- Do not critique a guessed target; if the target is unclear, say what was given and what would be accepted.
- Look before you speak: screenshot every screen at 1280 and 390 wide, light and dark, transitions off, pointer parked off the UI, then click every control and record what changed; a control that changes nothing is a finding; a critique from source alone is worthless and must be declared as such.
- Every finding names its evidence: the exact element and its location in source, a measured number, or a specific thing in a specific screenshot; "spacing feels off" or "feels generic" is not a finding; "the card's 12px internal gap equals the 12px gap between cards, so grouping reads as one block" is.
- Cite measured heuristic numbers as naming, not deciding; never cite a check pass in support of an aesthetic claim; a clean run is not a defence (seeded-defect samples pass every check).
- Never invent evidence; state what could not be judged (if not rendered, say so).
- Do not manufacture Critical findings to look rigorous; if everything is Minor, say so and let it ship.
- Do not soften; list at most two genuinely good things so the rest is credible, and do not pad that list to balance tone.
- State the scope every time: judgement, not measurement; no percentage covers taste.
- Output: verdict (reject / rework / ship); the three reasons a senior designer would send it back; a findings table (severity, finding, evidence, fix); at most two good things; what could not be judged.
- Act on it: fix every Critical and Major, re-run checks, re-critique what changed; the loop ends when only Minor or Enhancement remain.

## 245. Critic lenses (in order; most generated UI fails the first three)
- Focal point: everything the same weight and size; three equal cards, four equal stats, identical grey boxes.
- Type: one or two sizes doing all the work, timid scale contrast, headings as bold body, line length past 75ch, the default system stack with no intent.
- Spatial hierarchy: one padding everywhere, inner equal to outer, sections touching, a non-repeating rhythm.
- Colour: accent sprayed everywhere, the default indigo-blue gradient, pure black text, two near-identical greys.
- Elevation and radius: one shadow and one radius used uniformly; depth not matching layering.
- Content: lorem ipsum, "Placeholder", "Item 1", fake data, "No data" empty states.
- Motion: nothing moves or everything moves the same; entrances revealing content the reduced-motion path never shows.
- Craft under stress: long strings, empty lists, one item, forty items, nine-digit numbers, missing images; 320px before 1280px.
- Copy: labels not frontloading verbs, errors without fixes, machine-helpful sentences.
- Interaction truth: click every control; a checkbox that passes accessibility checks but does not toggle is broken.

## 246. Objective vs subjective split
- Measure objectively: token validity and alias resolution, contrast in all states and both themes, accessibility roles/names/landmarks, focus traps, RTL mirroring, responsive 280-951px, target size, keyboard operability, reduced motion (no content lost), silent text clipping and overlapping controls, token by intent, no emoji or dashes, no hardcoded values, card-row heights, nothing touching, Thai line breaks and leading, screen economy.
- Judge (never score): focal point, voice of type, meaning of spacing, one-relationship-one-gap and one-gutter consistency, overall quality.
- Taste heuristics (type-scale contrast, uniform repetition, measure, palette sprawl, single radius, flat shadow, hardcoded gradient, `#000` text, lorem, flat spacing, near-duplicate neutrals) are signals, not proof.

## 247. Six-dimension review rubric (score 1-10)
- Visual hierarchy 20%: clear focal points, scannable layout, meaningful contrast between elements, proper heading structure.
- Consistency 20%: token adherence, component reuse, pattern consistency across pages, naming conventions.
- Accessibility 20%: WCAG 2.2 AA, colour contrast, keyboard navigation, screen-reader support, target sizes.
- Usability 20%: task efficiency, learnability, error prevention, cognitive load, clear affordances.
- Responsiveness 10%: mobile-first, breakpoint behaviour, touch targets, content reflow, no horizontal scroll at 320px.
- Performance 10%: image optimisation, animation efficiency, perceived loading speed, skeleton states.
- Overall = Hierarchy x0.2 + Consistency x0.2 + Accessibility x0.2 + Usability x0.2 + Responsiveness x0.1 + Performance x0.1.
- Scoring guide: 9-10 exemplary, ship-ready reference quality; 7-8 good, minor polish; 5-6 adequate, several issues before ship; 3-4 below standard, significant rework; 1-2 critical, back to the drawing board.
- Distinguish design review (a new design before development) from design audit (an existing product, for consistency and quality).

## 248. Nielsen's 10 heuristics (flag violations by number)
- H1 Visibility of system status: loading indicators, progress, current/selected state.
- H2 Match between system and real world: natural language, familiar icons, logical order, cultural conventions.
- H3 User control and freedom: undo/redo, cancel, back, easy exit, dismissible modals.
- H4 Consistency and standards: platform conventions, internal consistency, component reuse.
- H5 Error prevention: confirmations for destructive actions, constraints, disabled invalid options.
- H6 Recognition over recall: visible options, contextual help, recent items, search suggestions.
- H7 Flexibility and efficiency: keyboard shortcuts, power features, customisable views.
- H8 Aesthetic and minimalist design: no unnecessary elements, clear visual weight, purposeful space.
- H9 Help users recognise and recover from errors: clear messages, suggestions, inline validation, recovery paths.
- H10 Help and documentation: onboarding, tooltips, help centre, contextual guidance.

## 249. Review process
- Step 1 context: target user and technical level, goal/task, place in the journey, constraints (technical, brand, timeline).
- Step 2 first impression (30 seconds, no interaction): what draws the eye first and is it right; can you tell what the page is for; cluttered or balanced; is the primary action obvious.
- Step 3 task walkthrough: completable without instructions; step count; dead ends or confusion; what happens on errors.
- Step 4 systematic check: token compliance; component-library use; accessibility P0 items; responsive mobile/tablet/desktop; states (empty, loading, error, populated, overflow, edge cases); real-ish content and edge cases (long names, empty fields); the banned-defaults list.
- Step 5 document findings in a prioritised table with concrete, token-referenced fixes.

## 250. Findings severity and table
- Critical: blocks users, P0 accessibility violation, data-loss risk; must fix before launch.
- Major: significant UX degradation, inconsistency across flows; fix in the current sprint.
- Minor: small polish, non-blocking inconsistencies; fix when convenient.
- Enhancement: improvement ideas, not bugs; backlog.
- Table columns: #, Severity, Category, Location, Finding, Evidence, Recommendation, Heuristic.
- Examples: error messages shown only in red (Critical: add icon + text); no empty state for new users (Major, H6); save button alignment differs (Minor, H4); no bulk keyboard shortcuts (Enhancement: add Shift+Click range select, H7).

## 251. Quick review checklist
- Visual hierarchy: a clear focal point and scanning path.
- Typography: correct heading levels, readable body.
- Colour: sufficient contrast, never the only means of information.
- Spacing: consistent rhythm, breathing room.
- Alignment: grid-aligned, no drift.
- Components: established patterns used correctly.
- States defined for every interactive element.
- Empty states: meaningful illustration plus CTA.
- Loading: skeleton or spinner for async content.
- Errors: clear, actionable, accessible.
- Responsive: mobile, tablet and desktop considered.
- Touch targets: 24px minimum, 48px recommended.
- Focus indicators visible on all interactive elements.
- Keyboard: the full flow completable without a mouse.
- Screen reader: meaningful landmarks, labels, live regions.
- Motion: purposeful and respects reduced motion.
- Content: real content and edge cases (long strings, empty, overflow).
- Dark mode tested thoroughly if supported.

# Part 25 — Redesign & audit

## 252. Audit inventory and gap analysis
- Screenshot every unique screen; catalogue all unique components; document every colour, font size and spacing value in use.
- Flag off-token colours, off-token typography, spacing off the 4px grid, and same-concept-different-implementation components.
- Severity map: Critical = accessibility violations (contrast, target size, keyboard); Major = confusing inconsistencies; Minor = visual polish (1px off, slightly wrong shade); Enhancement = opportunities.
- Remediation batches in order: quick wins (token swaps, contrast fixes, under 1 hour each); component standardisation; layout refactors (grid, responsive); new patterns (missing states, new components).
- Track token and component adoption to find drift (hardcoded values, forked components) and prioritise fixes.

## 253. Redesign sequence (Scan, Diagnose, Direct, Apply, Verify)
- Scan: identify the framework and styling method, the current token reality, the component and page inventory, what works and must be preserved (behaviour, routes, data, accessibility wins), and the current direction.
- Diagnose: run the banned-defaults list and the review rubric; flag generic tells and system failures (hardcoded values, missing states, contrast failures, no focus-visible, missing reduced motion, 6-line headings, default shadows, filler labels, emoji icons); produce prioritised findings.
- Direct: choose an archetype or named system that fits the brand; resolve it into tokens; re-verify every colour pair.
- Apply in order: tokens first (fixes most consistency slop), then typography and spacing (scale contrast, 60-75ch measure, section whitespace, vertical rhythm), then component states (all 8, focus rings, hover/press, loading/empty/error), then motion with reduced-motion fallbacks.
- Preserve behaviour at every step; do not change routes, data flow or markup semantics except to fix accessibility.
- Verify: re-run the rubric, an accessibility pass, a functional smoke test of every previously working flow, and a dark-mode and responsive spot-check.

## 254. Redesign guardrails
- Never introduce a brand colour that fails contrast; adjust it.
- Never remove existing accessibility affordances.
- Keep every change traceable to tokens.
- Consolidate to one shared theme consumed by every page; a redesign that leaves pages on different palettes has failed.
- Theme switches come from the single token source, not page edits.
- Deliver complete output, not fragments.

## 255. Interop and migration with external systems
- Map by role and intent across six axes: colour roles, type scale, spacing unit, radius, elevation, motion.
- From an external system to your tokens: re-point semantic tokens.
- To an external stack: theme their primitives with your tokens.
- Migrate screen by screen: Audit, Map, Bridge (an alias layer), Verify.
- Verify every mapped pair's contrast and that all 8 states and dark mode survive the mapping.
- Output a crosswalk table (own token, their token, value note) and a bridge plan.

# Part 26 — Design QA, gates & verification

## 256. Render-and-look inspection
- Functional: click each interactive element and confirm the state changed; a custom control whose overlay covers the real input will not toggle unless the overlay has `pointer-events:none` or a wrapping label forwards the click.
- Geometry: glyphs centred, not stacked or offset; in a grid box holding a hidden (opacity:0) sibling plus a pseudo-element, the pseudo lands in row 2; use `display:none` on the hidden sibling or keep one container child.
- Stroke consistency: a checkmark and its indeterminate dash use the same rendering method (one SVG, two paths toggled by state, same stroke-width), never an SVG check vs a CSS rect.
- Transition artifacts: disable transitions and park the pointer off the component before judging a state; a mid-animation half-faded control is not a bug.
- Capture at a high device scale (e.g. 4x) for inspection.
- Screenshot pages at 1280 (or 1600 for dashboards) and 390 wide, in both themes.

## 257. States verification sheet
- Render every variant x every applicable state on one page and verify each, light and dark.
- Verify contrast in default, hover and focus for every element, and that every text element meets AA.
- Verify ARIA role, name and label correctness.
- For overlays and modals also verify focus trapping.
- A component is correct only when every variant x state renders right, not just the resting default.

## 258. QA pyramid
- Layer 1, every commit (fast): token validity and alias resolution; no hardcoded hex/px/timing outside the token layer; a token-pair contrast gate; real-render contrast measurement.
- Layer 2, every change review: automated accessibility scanning over every component state; zero serious or critical violations to merge.
- Layer 3, every change review: visual regression snapshots.
- Layer 4, per release: manual accessibility (the ceiling).
- Run cheap gates first and fail fast; automated scanners gate the floor, not the ceiling.

## 259. Automated accessibility coverage
- Cover semantic-changing states: error, loading (`aria-busy`), disabled, expanded, selected, not just default.
- Never run accessibility checks mid-transition; disable transitions first.

## 260. Visual regression
- Snapshot variants x sizes x states x themes (light/dark).
- Snapshot at key breakpoints to catch reflow and overflow.
- Include RTL snapshots and a pseudo-locale frame to catch text-expansion clipping.
- Freeze animations and use deterministic data so diffs are real.
- Do not diff pixels across browser versions (noise); use screenshots for human inspection with a fixed viewport, reduced motion and the pointer parked off the UI.
- Review intentional diffs; block unintended ones.
- Track flake rate; quarantine flaky tests rather than disabling them; a flaky check is worse than a missing one (it teaches re-running until green).

## 261. Objective quality gate behaviour
- Treat the gate as all-or-nothing and report the real N/N result.
- List each failing check verbatim, fix the cause, and re-run until green.
- For any rendered page, also check states (light/dark), responsiveness and render-and-look.
- Before release: the full gate green, responsive 280-951px with the hinge clear, no emoji; confirm the version bump level with the owner; draft the changelog; take no irreversible release step without approval.
- Process compliance: every edited page has a passing check before work ends; no open finding is left on a page's latest version; work is not finished while pages remain unverified.
- Gate colour changes against WCAG before publishing.

## 262. Measuring the measurement
- Every check must be proven to reject a deliberate (seeded) defect, not just accept good work.
- A rule that silently does nothing is indistinguishable from one that works until its behaviour is measured.
- Write negative checks ("must never happen") so they can actually fail: bound both minimum and maximum at zero.
- Include at least one positive control proving the measured thing can occur, or a clean sweep may be measuring nothing.
- A check must not match its own template or instruction text; key on filled-in values (e.g. a "Mood:" line followed by something other than the template words).
- Measure an indicator before believing it; inspect where a pattern matched.
- Use at least 3 runs for contested indicators; two runs cannot distinguish "usually" from "once".
- Grade only what the conditions can produce, keep test prompts realistic, and validate that checks are well-formed before spending effort on runs.
- Separate output-quality evaluation (real artifacts, recorded results) from process evaluation.

## 263. QA definition of done
- An unreviewed change cannot introduce an unresolved token alias, a contrast failure, a raw hex/px or an accessibility violation; if it can, a gate is missing.
- Snapshots cover dark mode, RTL and semantic-changing states, not just the happy path.
- The manual accessibility checklist is signed off per release.

## 264. Component definition of done
- Functional: all variants; all 8 states handled or N/A'd; edge cases addressed; error and loading states implemented.
- Visual: within 1-2px of design (pixel-accurate); all tokens, zero hardcoded values; dark mode if applicable; responsive 320-1536px; animations with reduced-motion fallback.
- Accessible: keyboard (Tab, Enter, Space, Escape, Arrows); screen reader tested; AA contrast (4.5:1 text, 3:1 UI); focus visible; correct ARIA; targets at least 24x24px.
- Code quality: typed interfaces (no `any`), documented props, a composable variant API, compound patterns where appropriate, ref forwarding, no inline styles.
- Tested: unit tests for logic, visual regression, automated accessibility, manual screen reader, cross-browser (Chrome, Firefox, Safari).

# Part 27 — Prototyping & research

## 265. Fidelity ladder
- Pick the lowest fidelity that answers the question; never skip levels; never jump to high fidelity before validating the concept; validate at each level.
- Level 1 content-first (15-30 min): text outline and content hierarchy; validates information needs and architecture: does content answer user questions, is anything missing, is the order right.
- Level 2 wireframe (1-2 h): greyscale boxes, content zones in correct proportion, navigation, interactive elements as grey boxes, behaviour annotations; exclude colour, type, icons, pixel spacing and animation; validates layout, findability and navigation.
- Level 3 low-fi interactive (2-4 h): clickable flows, multi-step forms, key interactions, error and empty states, real-ish content; validates task completion, sticking points, step count.
- Level 4 high-fi (4-8 h per page): pixel-perfect, all tokens, all states, responsive, dark mode, all edge cases; validates feel, visual and brand consistency, accessibility.
- Level 5 code/production prototype (1-3 days): real components, seeded realistic data, real interactions, real devices, keyboard and screen reader; validates feasibility and performance.
- Hold high-fi and code prototypes to the same token and accessibility bar as production.
- User flows are step-by-step with decision points, error paths and edge cases (empty, loading, overflow), not just the happy path.
- Always deliver an explicit "what we validate next" plan with tasks and success criteria, never "test later".

## 266. User journey mapping
- Frame: journey (user goal), persona, context (where/when).
- Per phase record: action, touchpoint, thought, emotion, opportunity, metric.
- Awareness (curious): a clear value proposition above the fold; metric bounce rate.
- Exploration (evaluating): comparison table, social proof; metrics pages per session, time on site.
- Decision (anxious): free trial, money-back guarantee, simple pricing; metric trial sign-up rate.
- Onboarding (overwhelmed to relieved): progressive disclosure, guided setup, quick wins; metrics completion rate, time to first value.
- Retention (confident): feature discovery, personalisation, integrations; metrics DAU/MAU, feature adoption, NPS.

## 267. Information architecture research
- Card sorting informs navigation structure; tree testing validates findability.
- Open card sort: 30-60 cards, users define groups; analyse common groupings and labels.
- Closed card sort: predefined categories; measure % agreement per card; under 60% agreement means a confusing category.
- Tree testing: a text-only hierarchy with "Where would you find X?" tasks; measure success rate, directness and time; target over 80% success and over 60% directness.

## 268. Usability testing
- Test with 5 users per round (5 users catch ~85% of issues); measure task success rates.
- Intro (5 min): testing the product, not the participant; no wrong answers; think aloud; the facilitator does not answer during tasks; sessions run 30-45 minutes.
- Task format: scenario, task, success criteria; observe path, time, hesitation and backtracking, verbal confusion, expected interaction pattern.
- Set time limits per task (e.g. 2-3 minutes).
- Include find, complete-an-action and recover-from-error tasks.
- Post-task: ease rating on a 1-5 scale; anything confusing; what did you expect when clicking X.
- Post-session (5 min): overall impression; easiest and hardest part; anything expected but missing; would you use it and why; other feedback.
- Synthesise per task: success rate, average time, average difficulty, key observations; rank findings Critical/Major/Minor with targets (e.g. 60% success to a target of 90%); list recommended actions.

## 269. Research methods and sample sizes
- Stakeholder interviews: kickoff, 3-5 people, 30 min each.
- Competitive analysis: discovery, 3-5 competitors, 2-4 hours.
- Card sorting: IA design, 15-30 users (open sorts with 5-15 users for early grouping), 15 min each.
- Tree testing: IA validation, 30-50 users, 10 min each.
- Usability testing: any fidelity, 5 users, 30-45 min each.
- A/B testing: optimisation, 1000+ users, 1-2 weeks.
- Surveys: 100+ users, 5 min each.
- Diary studies: 10-15 users, 1-2 weeks.

# Part 28 — Performance

## 270. Core Web Vitals budgets
- LCP at most 2.5s: prioritise hero text and image, responsive images, preload the critical font, server-render above the fold.
- INP at most 200ms: keep the main thread free, debounce, defer non-critical script, avoid heavy synchronous handlers.
- CLS at most 0.1: reserve space (skeletons sized to content, media dimensions, aspect-ratio tokens); never insert content above existing content.
- Measure on a mid-tier mobile profile (slow 4G plus 4x CPU throttle); the first interaction must still feel responsive.

## 271. Loading strategy
- Render above the fold first (server rendering); push client interactivity to leaf components.
- Code-split by route and by heavy widget (chart, date picker, command palette); lazy-load below-fold and behind-interaction components.
- Fonts: never import via CSS; preconnect plus preload; `font-display: swap`; preload one critical weight; subset glyphs; prefer variable fonts; self-host; respect `prefers-reduced-data`.
- Images: AVIF/WebP, responsive sizes, lazy-load below the fold, explicit dimensions, <= 500,000 bytes per page.
- Every data-fetching view gets a skeleton loading state.

## 272. Layout shift prevention
- Size skeletons to final content dimensions.
- Reserve media space with aspect-ratio.
- Never inject banners, ads or toasts that push content down; overlay them or reserve space.

## 273. Design-system runtime cost
- Prefer CSS-variable tokens (nearly free, no script).
- Prefer CSS state styling (hover, focus-visible, data-state) over script.
- Tree-shake and import per component; prefer zero-runtime styling where INP matters.
- Keep animation on compositor properties (transform, opacity).
- Treat performance as accessibility: slow, janky UIs fail low-end devices first.

# Part 29 — Governance & handoff

## 274. Handoff checklist
- All values mapped to design tokens (zero hardcoded).
- All 8 states documented per interactive element.
- Edge cases addressed: long text, empty, overflow, single item, many items.
- Responsive behaviour specified at each breakpoint.
- Animation specified: property, trigger, duration, easing, reduced-motion fallback.
- Accessibility annotations: ARIA roles, keyboard model, focus management.

## 275. Design-to-token mapping
- Map every design value to a token before building.
- If a value matches no token: within 1-2 shades, use the nearest token; if intentionally different, discuss with design and possibly add a token; never hardcode.
- Map spacing to the semantic level first (card padding, stack, inline), then fall back to the scale.
- Map shadows to elevation tokens, borders to border styles, radii to radius tokens.

## 276. Token build and distribution
- Treat the token source as the single source of truth: author once, generate every platform output (CSS variables, utility-framework theme, iOS asset catalogs, Android/Compose), never hand-edit outputs.
- Resolve aliases to final values per platform; keep the reference graph for documentation.
- Expose semantic and component tokens publicly; keep primitives internal.
- Emit base plus dark/brand/density overrides as deltas only; never duplicate unchanged values.
- Format by type: colour to hex/rgb/platform colour; dimension to rem/px/pt/dp; duration to ms/s; cubic-bezier to an easing curve.
- Fail builds when generated outputs are stale; regenerating must produce no diff.
- Gate colour changes against WCAG before publishing.

## 277. Design-tool parity (e.g. Figma)
- Mirror the three tiers as three variable collections with aliasing (primitives, semantic, component); dark, brand and density as modes.
- Pick one authoritative sync direction (code to design tool, or design tool to code); the other side is generated with zero hand edits.
- Every design variable resolves to a token; no orphan hex in designs.
- Design-tool variants and properties cover code variants, sizes and all 8 states; flag missing states as parity gaps.
- Name layers and props to match code prop names so handoff is mechanical.
- Keep a per-component parity checklist: variants, sizes, states, tokens bound.
- Drift between design tool and code is the root cause of "the build doesn't match the mockup".

## 278. Build output rules (design-relevant)
- Trace every colour, size, radius, shadow, duration and font to a token; zero raw hex/px/ms and zero raw utility-palette classes; use semantic utilities.
- Give every interactive element accessibility: role/ARIA (or native accessibility modifiers), keyboard model, focus management, target at least 24px.
- Handle all states: default, hover, focus, active, disabled, loading, error, selected.
- Support dark mode via semantic tokens that switch automatically; provide reduced-motion fallbacks; build mobile-first and breakpoint-aware.
- Native Apple targets support Dynamic Type (scaled metrics) and the system reduce-motion setting; adapt per platform.
- Deliver copy-paste-ready, complete output; run the 12-point aesthetic pre-flight on the rendered result.

## 279. Versioning (SemVer for design)
- Major: breaking; a renamed or removed token or prop, changed anatomy or default behaviour, restructured token tiers.
- Minor: additive; a new token, component, variant, size or optional prop.
- Patch: fixes; a contrast fix, bug fix, doc or typo fix, a value tweak within tolerance.
- A token value change that materially alters appearance is at least minor (often major if it breaks a brand).
- Every change gets a SemVer level and a changelog entry.

## 280. Contribution workflow
- Propose: the problem, evidence of recurrence, the proposed pattern; check it is not an existing component or variant.
- Validate: a real, repeated need; one-offs stay in the product.
- Design to the full bar: anatomy, variants, sizes, 8 states, token mapping, accessibility.
- Review with the rubric and an accessibility audit; validate tokens and contrast.
- Document and ship: spec, discoverable from the system index, version bump, changelog.
- Promotion path: product one-off -> candidate (documented, used in at least 2 places) -> core (stable, versioned API); do not promote prematurely.

## 281. Deprecation and renames
- Never delete silently.
- Mark with reason, replacement and removal version.
- Warn in code and docs; keep it working for at least 1 minor cycle (emit old and new names during the window).
- Provide an old-to-new migration map (and a codemod where possible), e.g. `action-danger -> action-destructive`, `text-error -> feedback-error-text`, `radius-pill -> radius-full`, `duration-normal -> duration-base`, `ease-emphasized -> ease-spring`.
- Remove only in a major release, listed in the changelog.
- Prove renames on the render (before/after, light and dark): every value resolves identically.
- Treat tokens defined only in demos (no counterpart in the source) as gaps requiring a design decision, not mechanical aliases.

## 282. Change communication
- Each release states what changed, why, who is affected and the migration path; lead with breaking changes.
- Maintain a single source of truth that consumers know to consult.
- Define a contribution path, deprecation policy and change-communication channel up front.
