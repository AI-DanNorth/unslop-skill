# Design Rules by Concept

Distilled from the design-taste collection: one core anti-slop method, 10 genre identities, 10 craft disciplines and 3 code disciplines, plus its before/after demos. Each concept is followed by its rules. Exact values are kept wherever the source gives them.

---

# Part 1 — Core Anti-Slop Method

## 1. Why AI Output Looks Generic
- Agents default to one look: indigo-purple gradients, a centered hero, three feature cards, Inter, `slate-900`, `rounded-2xl`.
- The model jumps to a default aesthetic instead of reading the brief. Taste isn't missing from the model's ability, it's missing from its defaults.
- Every rule is contextual. Read the brief first, then apply what fits, and never apply everything blindly.
- One undeniably intentional page beats a polished template.

## 2. Read the Room Before Anything
- **Page kind:** landing (SaaS, consumer, agency, event), portfolio (designer, developer, studio), product page or redesign.
- **Vibe words:** minimal, warm, premium, playful, trust-first, editorial, dark, agency. These pick the direction.
- **Audience:** the audience picks the aesthetic, not your taste. A government service doesn't get kinetic typography.
- **Existing brand:** logo, colors, type and photography are inputs for a redesign, not optional.

## 3. Declare a Design Read
- Before generating, write one line of reasoning the user can see, e.g. *"Reading this as: B2B SaaS landing for technical buyers, Linear-style minimal, restrained motion, monochrome + one accent."*
- If the read is genuinely ambiguous, ask exactly one question. Otherwise proceed without defaulting.

## 4. The Never List (LLM Fingerprints)
- No indigo-to-purple (or blue-to-purple) gradient hero backgrounds, and no gradient text.
- No centered hero made of a badge pill, an oversized bold heading, two buttons and a product screenshot.
- No "three equal feature cards" as the default section.
- No emoji as icons (📊🚀⚡). Icons are drawn or typographic.
- No glassmorphism (frosted `backdrop-filter` cards) everywhere.
- No `Inter` + `slate-900` as the automatic palette.
- No `rounded-2xl` on everything, and shadows are not the only source of depth.
- No identical symmetric sections stacked down the page, and no shared skeleton across every page.
- No "Get started free" purple button regardless of context.
- No six or more nested cards (cards in cards in cards).
- No screenshot-in-browser-chrome mockup as the default hero visual.
- If the design read gives no reason for one of these, don't use it.

## 5. The Default-Agent Baseline (What "Before" Looks Like)
- Inter as the only family.
- Repeated `linear-gradient(135deg, #6366f1, #8b5cf6)` indigo-to-violet fills on buttons, text and blobs.
- A violet radial glow behind a centered hero.
- Scattered radii (6, 8, 10, 12, 16, 24px and pills) with no system.
- Purple pill badge, two buttons, a mock dashboard, then three cards.

## 6. Pre-Flight Checklist (Fail the Page If…)
- [ ] It could have been made by typing "landing page" into the same agent without this guidance.
- [ ] The hero is a centered badge + heading + two buttons + screenshot.
- [ ] Any emoji is used as a UI element.
- [ ] Three identical cards appear in a row out of habit.
- [ ] The font is a single neutral sans with no display contrast.
- [ ] More than about two colors carry meaning.
- [ ] Body text wraps past about six lines, or the column is full-width.
- [ ] The accent appears more than about four times per viewport.
- [ ] Any section could be deleted without losing the design argument.
- If any box is ticked, redo that section.

## 7. How the Layers Compose
- A **genre identity** decides the look. Pick one per project.
- **Craft disciplines** police the details: type, color, motion, accessibility, copy, structure, brand.
- **Code disciplines** police the delivery: markup, tokens, performance, review.
- One brief can yield ten radically different identities. The brief and the chosen identity, not the template, should drive the result.

---

# Part 2 — Typography

## 8. Pairing
- Use two families at most, with structural contrast. Three families is soup, and one neutral sans is a template.
- Pairings that work:
  - A characterful serif (Fraunces, Newsreader) with a neutral sans or the serif itself: editorial, luxury, calm.
  - A heavy grotesk (Archivo, Bricolage) with the same family at 400: bold, playful, brutalist.
  - A neutral grotesk (Space Grotesk, system) on its own: dark tech, developer tools.
  - Mono for labels only, with a grotesk body: technical, terminal.
- Mono is a label voice. Use it for body text only in data tables and terminals.
- Never default to Inter unless the brand already uses it.
- When a brand mandates a family, choose the second from the same species (e.g. serif + sans by the same designer).

## 9. Scales
- **Display scale** (marketing): 64 / 48 / 32 / 24 / 18 / 16, made fluid with `clamp()`, e.g. `clamp(2rem, 5vw, 4rem)`.
- **Hero headline:** in the `clamp(3rem, 8vw, 7rem)` range, with tight leading of 0.95–1.05. Small-ish bold text reads as template.
- **UI scale** (product): 13 / 14 / 15 / 16 / 20 / 24. Never below 12px or above 24px inside UI surfaces.
- One display size per section. If two headings are equally large, neither is a heading.
- One type-size hierarchy per section. Don't show six sizes in one viewport.

## 10. Weights
- Use one weight for display (the family's natural voice: 400 for serifs, 700–900 for grotesks), 400 for body and 500–600 for emphasis.
- Use three weights per page at most.
- No fake bold (never `700` on a 400-only family) and no fake italics. Use real faces.

## 11. Measure, Leading, Rhythm
- Body line length is 45–75 characters. Hero subheads stay at 40 characters or fewer per line, and headlines at 24 or fewer.
- Leading: headlines 0.95–1.08 (serifs at the low end), body 1.55–1.7, labels 1.2–1.4.
- Letter-spacing: uppercase labels `0.08–0.2em`, lowercase display `−0.02em`, body 0.
- Never track lowercase body text above 16px, except as a deliberate editorial act.
- Small type (≤12px) needs at least `0.02em` letter-spacing. Never go below 10px without a data-table justification.
- Align text blocks to a 4px baseline grid, with line-heights in multiples of 4 (20/24/28/32px).
- Marketing paragraphs run about three lines at most. A six-line paragraph in a card is a layout failure.

## 12. Text Placement
- Never set body text full-width. Constrain it to 32–40em columns, especially on widescreen.
- Break headlines deliberately with manual line structure ("Know exactly / what your users do").
- Headline → sub → paragraph must each shrink visibly in **both** size and weight.
- Justified text is banned, except in print-style editorial columns of 60+ characters with hyphenation.
- No widows (a single word on the last line) in headings.
- Use `clamp()` with rem for all fluid text, and never `vw` without a rem floor.
- Mark labels and metadata in mono or small caps, uppercase and letterspaced. Section numbers ("01", "02") speak the same language.

## 13. Type Accessibility Floor
- Body text is at least 16px on marketing pages and at least 14px inside UI. Smaller text is only for metadata, at 4.5:1 contrast.
- Contrast is at least 4.5:1 for body and 3:1 for large display (≥24px, or ≥18.66px bold).
- Use `text-rendering: optimizeLegibility` on display, and avoid `-webkit-text-stroke` at small sizes.
- Load fonts with `font-display: swap`, preload the display face, and never render invisible text while fonts load.

## 14. Typography Fail Conditions
- [ ] One neutral family doing every job, or more than two families.
- [ ] A heading below 20px beside 16px body (no hierarchy).
- [ ] Body text wider than 75 characters.
- [ ] Any text under 10px.
- [ ] More than three weights.
- [ ] A six-line paragraph inside a card or sidebar.
- [ ] Justified text without hyphenation.

---

# Part 3 — Color

## 15. Palette Architecture (60-30-10)
- **60% neutrals:** surfaces and text from one family, warm or cool. That means 2–4 surfaces (background, panel, raised) plus three text steps (primary, secondary, muted).
- **30% structure:** borders, hairlines and dividers in a tinted neutral, not a color.
- **10% accent:** ONE saturated color with a job (primary CTA, links, active states, one data series).
- A second accent needs a distinct job (e.g. success green) and stays under 2% coverage.
- Two neutrals plus one accent is a complete palette. Three accents is a rainbow.
- More than three meaningful colors per viewport means the page has no message.

## 16. Color With Intent
- Start from one neutral and one accent: warm paper/ink, or off-black/off-white.
- No default dark-navy backgrounds unless the read is dark tech. Dark doesn't automatically mean premium.
- The accent exists to point at one action, stat or highlight, and everything else stays neutral.
- One accent used twice per viewport is a signal. The same accent everywhere is noise.
- Use tonal depth (tints of your neutral) instead of adding new colors.
- Replace gradients with flat color wherever a flat color would do.

## 17. Building Ramps
- Build ramps in OKLCH for perceptually even lightness. Never blindly interpolate hex.
- Neutral ramps have 9–11 steps (50–950) with chroma near 0.
- Accent ramps have 9–11 steps, with the hue locked and chroma rising from low at 50 to full at 500–600, then falling again by 900.
- The two most-used values on a page are the accent's 500–600 step (buttons) and the neutral's 50–100 step (backgrounds).

## 18. Contrast (WCAG 2.2)
- Body text: 4.5:1. Large text (≥24px, or ≥18.66px bold): 3:1.
- UI components (borders, icons, input edges): 3:1 against what's next to them.
- Focus indicator: 3:1 against what's next to it, at least 2px.
- Compute contrast with the luminance formula or a tool. Never eyeball it.
- A desaturated "premium" look is no excuse for low contrast: desaturate the background, not the text.
- Never put white text on yellow or pale accents. Use ink on yellow (`#FFD100` with ink text is correct).
- Never use white on low-opacity indigo.
- Placeholder text at ≤0.5 opacity is decorative and can never be the only label.

## 19. Semantic Color Tokens
- Name tokens for their jobs: `--color-surface`, `--color-surface-raised`, `--color-text`, `--color-text-muted`, `--color-border`, `--color-accent`, `--color-success`, `--color-danger`, `--color-warning`.
- Give statuses 3–4 steps, e.g. `--color-danger-bg`, `--color-danger-border`, `--color-danger-text`.
- The name carries the meaning: `--color-danger-text`, not `--color-red-700`.
- Danger, success and warning exist for status only, never decoration.
- Dark mode remaps the semantic tokens. Never sprinkle a second raw palette into components, and always recompute contrast.

## 20. Color-Blind Safety
- Never encode meaning in red vs. green alone. Add shape, position, pattern or labels (✓/✕, ↑/↓, solid/dashed).
- Blue-violet is the safest hue, and orange is the strongest safe accent against neutrals.
- Use color-blind-safe categorical sets (e.g. Okabe-Ito) for data viz, not rainbow defaults.

## 21. Color Fail Conditions
- [ ] Any adjacent text/background pair under 4.5:1 for normal text.
- [ ] More than one accent carrying meaning per viewport.
- [ ] A gradient where a flat color would do.
- [ ] Red and green as the only success/failure signal.
- [ ] Any raw hex in a component instead of a token.
- [ ] White text on a yellow or pale accent.
- [ ] A dark theme that just reuses the same colors on a dark background.

---

# Part 4 — Layout, Composition & Depth

## 22. Asymmetry Reads as Designed
- Offset the content column from center: a 7/5 split, 6/6 with a rule between, or an oversized left column with a narrow index column on the right.
- Use one deliberate grid per page, and align everything to it.
- Indexing (numbers, thin top/bottom hairlines, a visible grid) makes a page feel art-directed.
- Hairlines (1px `rgba(ink, 0.1–0.2)`) are the cheap way to look expensive.
- Vary section rhythm: full-bleed, split, indexed list, quote, table. Avoid equal-height card trios everywhere.

## 23. Whitespace
- Leave generous margins and breathing room around the hero.
- Space sections 96–160px apart.

## 24. Depth From Structure, Not Shadows
- Build depth with hairlines, inset panels, offset blocks and tonal backgrounds.
- Shadows are only for floating elements, and soft (blur ≥24px, low opacity).
- No gradient surfaces on buttons or CTAs. A solid, saturated accent looks and performs better.
- For the hero visual, a metric table, editorial column, oversized pull-quote or the type itself is often stronger than a mockup.
- With no imagery in the brief, design with structure (rules, type, color blocks), not stock gradients or placeholder photos.

## 25. Elevation Scale
- Use three levels at most:
  - flat (no shadow)
  - raised (blur ≥16px, opacity ≤0.15)
  - floating (blur ≥40px, opacity ≤0.2)
- Anything else is a bug.

---

# Part 5 — Motion

## 26. Motion Philosophy
- Motion explains the interface: what happened, where it is, what to do next.
- If you can't explain an animation in one sentence, delete it.
- The two AI-motion crimes are nothing moving at all, and everything moving forever.
- Default to minimal: one intentional transition (nav reveal, hero entrance or scroll-triggered fade).
- When the read is playful, spend the motion budget there, not on color.

## 27. Duration Tokens
- `--dur-fast` 100–150ms: hovers, pressed states, focus rings.
- `--dur-base` 200–300ms: small entrances and state changes (toggles, open/close).
- `--dur-slow` 400–600ms: section reveals, page transitions, dialog open.
- `--dur-hero` 600–900ms: the ONE hero entrance sequence.
- Under 100ms reads as a blink, unless it's a deliberate snap. Over 900ms reads as a slow website.

## 28. Easing Tokens
- Standard (UI states): `cubic-bezier(0.4, 0, 0.2, 1)`, fast in and calm out.
- Emphasized (entrances and reveals): `cubic-bezier(0.22, 1, 0.36, 1)`, with a long calm tail that feels premium.
- Exit: `cubic-bezier(0.4, 0, 1, 1)` or faster. Exits are snappier than entrances.
- Spring/overshoot (playful identities only): `cubic-bezier(0.34, 1.56, 0.64, 1)`, at most once per element and never on loops.
- Never use `ease-in-out` as a catch-all, and never `linear` except for marquees and progress.

## 29. What to Animate
- Animate `transform` and `opacity` only.
- Never animate `width`/`height` (use scale), `margin` or `top`/`left` (use transform), large `box-shadow` (use a pre-blurred pseudo-element), or `filter: blur` on large surfaces.

## 30. Choreography
- One scene per section: elements enter in 2–3 stages (heading → body → CTA), 60–120ms apart, with the same duration and easing. Stagger is hierarchy.
- Reveal distance is ≤20px (translateY 8–16px) plus opacity. Bigger reads as PowerPoint.
- Scale entrances ≤0.96→1, and only on dialogs and popovers, never full sections.
- The hero gets one sequence of 600–900ms total, with each element entering once and no looping floats.
- Allow one class of loops per page (ambient status: live dots, loaders, spinners). Any other loop is an error.

## 31. Micro-Interactions
- Hover is 100–150ms with standard easing and one property change (background tone, border, or translateY −1 to −3px). Never color AND position AND shadow at once.
- Pressed is the inverse of hover (translate down, shadow off), 80–120ms.
- Focus-visible is a 2px ring at 3:1 with `outline-offset: 2px`, faded in over 100ms. Never `outline: none` without a replacement.
- Disabled has no hover at all, opacity 0.4–0.5 and no pointer change.
- A transition nobody can perceive is dead code.

## 32. Scroll & Layout Motion
- Scroll reveals fire once per element via IntersectionObserver (or CSS `animation-timeline`). Never re-animate on every scroll pass.
- Sticky is allowed for nav and section labels. Keep animation out of sticky elements.
- View and page transitions run 300–500ms, with shared-element moves only where they earn it (list → detail).
- Layout transitions use FLIP (transform-based), never re-layout animation.

## 33. Reduced Motion
- Ship a global gate: under `prefers-reduced-motion: reduce`, set `animation-duration` and `transition-duration` to `0.01ms`, set iteration count to 1 and `scroll-behavior: auto`.
- Use zero motion by default under the query: no parallax, no auto-scrolling carousels, no marquees.
- Content simply appears (opacity 0→1 over one frame).

## 34. Motion Fail Conditions
- [ ] Any element animates longer than about 1.5s (outside loops and loaders).
- [ ] More than one looping element per viewport.
- [ ] Any width/height/margin/top animation.
- [ ] Reveal distances beyond 20px.
- [ ] `ease-in-out` as the global easing.
- [ ] Every element animates on load (a "bounce-entrance festival").
- [ ] No reduced-motion handling at all.

---

# Part 6 — Scroll-Driven Animation Craft

## 35. Animation Architecture
- Wrap each page's animations in one scoped context, which gives scoped selectors and instant teardown.
- Gate everything through media queries:
  - all animation inside `(prefers-reduced-motion: no-preference)`
  - heavy effects (pins, scrubs, per-character splits) inside `(min-width: 768px)` only
- Return cleanup functions, and revert on unmount in SPAs.
- Use one timeline per section, named by section, never one giant global timeline.
- Smooth scrolling (if used) runs about 1.1s, with anchors working. Stop it during a preloader, and never smooth-scroll under reduced motion.

## 36. Pin & Scrub Hygiene
- Use **two pinned sections per page at most**. One is the norm.
- Pins start at `top top`, end at `+=200%` to `+=300%`, and keep pin spacing.
- Horizontal galleries pin the section and translate the track on `x` only (never `left`). The distance is recalculated on resize as `scrollWidth − innerWidth`, with `scrub: 1`, desktop only.
- Native `overflow-x` + scroll-snap remains as the no-JS and reduced-motion fallback.
- Drag carousels use inertia, with bounds as a function (recalculated on resize) and edge resistance around 0.9. They need a native scroll-snap fallback and a visible "draggable" hint.
- Scrub smoothing is `0.6`–`1` on heavy sections. Use unsmoothed scrub only on trivial tweens.
- Never pin inside a pin, or start a second pin before the first one's spacer ends.
- Refresh scroll positions after fonts and images load, or everything misaligns.
- Test pins at 768px. A pin that traps mobile users is a bug.

## 37. Text & Reveal Patterns
- Reveal text by line by default (an `overflow: hidden` wrapper with `yPercent: 110 → 0`). Use character splits only for hero headlines, and only on desktop.
- Elements start visible in CSS. Hide from-states only when JS and motion are active, so a page whose JS never loads is still complete.
- Standard reveal: `opacity 0`, `y 40`, `0.9s`, `power3.out`, triggered at `top 82%`, once.
- Hero intro: one load timeline with 80–120ms stagger, `expo.out` or `power4.out`, under 1.4s total.
- Count-ups tween a proxy number and write the text on update, triggered once.

## 38. Animation Sins
- Scroll-jacking without a smooth-scroll layer, then not testing it. Native scroll is a feature.
- Animations triggering before content exists.
- Marquees not paused under reduced motion. Kill them in CSS too, not just JS.
- Autoplaying anything (hero video, accordions, carousels that move without input). Confidence is stillness between moments.
- `will-change` spam. Set it only while animating.
- 200-element staggers in one frame. Batch targets into one tween instead.
- A page whose "wow" depends on animation. If the still frame is boring, the animation is makeup, not design.

---

# Part 7 — Landing Pages & Conversion

## 39. The 8-Second Read
- Without scrolling, the top third must answer three questions:
  - **What is this?** The H1 names the outcome, not the category ("Analytics that don't need a data team" > "Enterprise analytics platform").
  - **Who is it for?** The subline names the audience.
  - **What do I do?** Exactly one primary CTA, visible and contrasting, above the fold.
- Design the top third first.

## 40. The Selling Sequence
1. **Hero:** the promise and the primary CTA (plus the product, if it's visual evidence).
2. **Proof strip:** logos, user count or press, so trust comes before claims.
3. **The problem:** one pain, in the reader's words, three lines max.
4. **The mechanism:** three features max, each one sentence plus one proof point. More is a spec sheet.
5. **The proof:** metric callouts with numbers, and quotes with a name and title.
6. **How it works:** three steps only, if needed.
7. **Pricing:** three tiers max, with the middle one highlighted.
8. **The close:** one line of residual doubt ("No credit card. Set up in 4 minutes."), the CTA again and a human touch ("Talk to a human →").
- Every section must answer the objection the reader has at that moment, or it's decoration.

## 41. Hero Patterns by Audience
- **Developer tool:** problem → mechanism ("Type less. Ship more." plus a terminal or product panel).
- **B2B buyer:** outcome + qualification ("Cut support tickets 40% with self-serve onboarding").
- **Consumer:** desire + friction removal ("Your photos, organized while you sleep").
- **Enterprise:** category + evidence ("Identity security for regulated industries" plus compliance chips).
- **Solo or passion:** identity + invitation ("Build the portfolio that gets you hired").
- Never combine two patterns in one H1.
- Never show the product screenshot before the promise is understood.

## 42. CTA Discipline
- One primary CTA per viewport. Secondaries are text links or quiet buttons, because two equal buttons means no button.
- The label states the outcome or action: "Start free trial" > "Get started" > "Submit". First person ("Start my free trial") lifts consumer clicks.
- The CTA color is the accent, and the accent appears nowhere else in that viewport.
- The final CTA uses the same label as the hero CTA. Never rename it mid-page.
- Minimize form fields: email + password for trials, and company name only for enterprise offers.

## 43. Proof & Trust Placement
- Show logos in grayscale, before features, with six or fewer (more reads as fake).
- Metrics give the number, what it measures and a source line: "18.4% trial→paid among 4,120 teams."
- Quotes carry a name, title and company, never "John D. from California".
- Place compliance chips (SOC 2, GDPR, ISO 27001) beside pricing and forms, where decisions happen.
- Put one guarantee where risk is highest, near the form ("14-day free trial. Cancel in two clicks.").

## 44. Pricing Psychology
- Three tiers: entry, featured (most popular, visually distinct with one accent) and top (premium or "contact us").
- The featured tier is the anchor: distinct but not aggressive.
- List the most valuable line item first.
- Show "≈ $1/day" framing for consumers, and annual billing with "2 months free" for B2B.
- Never three equal-weight columns. The eye must land on one.

## 45. Mobile Behavior
- Keep the same section order, but move proof before features on small screens.
- CTAs are full-width, at least 48px tall, and reachable by thumb at both ends of the scroll.
- Tables become stacked cards or horizontal scroll with a hint.
- Pricing stacks with the featured tier first.

## 46. Landing Page Fail Conditions
- [ ] The top third doesn't answer what/who/do within 8 seconds.
- [ ] More than one primary CTA per viewport.
- [ ] Features without nearby proof, or claims without a source line in the same viewport.
- [ ] Equal-weight pricing columns, or four or more tiers.
- [ ] A section that answers no objection.
- [ ] Different labels on the hero and final CTAs.

---

# Part 8 — UX Writing

## 47. Voice First
- **Plainspoken:** enterprise, fintech, health ("We tell you when something's wrong. Here's what to do.").
- **Direct:** developer tools ("Type less. Ship more.").
- **Warm:** consumer, education ("You're almost done — one step left.").
- **Dry humor:** consumer and indie brands.
- Pick one voice and lock it.

## 48. Rules in Every Voice
- Be concrete: "42 rows", not "some data".
- Be honest: no "just" ("Just enter your email" is a lie), and avoid "simply" and "easily".
- Address the reader as "you" on marketing pages.
- Use no exclamation marks, except one celebration per page.
- Errors use the active voice.
- No corporate filler: "leverage", "streamline", "robust", "seamless", "cutting-edge".

## 49. Headline Formulas
- **Outcome + audience:** "Analytics that don't need a data team."
- **Before → after:** "From 'where are my users going?' to 'oh, there.'"
- **Name the pain:** "Your signup form is leaking 63% of visitors."
- **Authority + promise:** "The 2026 pricing guide for indie SaaS."
- **Curiosity with a payoff,** never curiosity alone.
- Keep the H1 under 12 words with one idea. The product name can live in the subline.
- No "?!" or "!!!" theatrics, and no "The Future of X" openers.

## 50. Buttons & Actions
- Buttons say the action: "Save changes" > "Submit" > "OK".
- Destructive buttons say what dies ("Delete project"), paired with an equally visible cancel.
- Loading states say what's happening ("Saving…" > "Please wait"). Never "Almost done" unless it's provable.
- Labels survive without context. No icon-only buttons without accessible text.
- Use one label per action on a page.

## 51. Errors: What + Why + Fix
- **What happened,** plainly ("We couldn't save this section").
- **Why,** in one clause ("the file is larger than 10 MB").
- **The fix,** as a verb or link ("Remove some images and try again").
- "Error 500" becomes "This page hit a snag on our side. Reload — your work is saved."
- "Invalid input" becomes "Add at least 8 characters. A number helps."
- "Password incorrect" becomes "That password doesn't match. Forgot it? Reset here."
- Field errors sit next to the field, not in a toast across the screen.
- Never blame the user: "You entered…" becomes "This field needs…".

## 52. Empty States
- Name the emptiness ("No projects yet").
- Say why it's empty in one line.
- Give one next action ("Create your first project").
- Optionally add a tiny win ("Takes about 4 minutes").
- An empty state without a next step is a dead end, which is a product failure.

## 53. Status & Loading Copy
- Progress uses verbs, not promises: "Uploading 3 of 8 files…".
- Completion states what changed: "8 files uploaded to /reports", not "Done".
- Notifications give a subject, one clause and an optional action, in under 20 words.
- Never show a skeleton for more than about 2s without a message.

## 54. Inclusive & Localization-Ready Copy
- No "guys", "man-hours" or gendered generic pronouns. "They" is fine.
- Write "1,024", not "1k", where precision matters, and spell out ambiguous dates.
- Write for translation: no variables mid-sentence ("Friends: {{count}}"), no idioms, no emoji-only messages.

---

# Part 9 — Accessibility

## 55. Semantic Structure
- One `<h1>` per page, and heading levels never skip. Reading only the headings should give the outline.
- Use landmarks: header, nav, main and footer, plus named aside/section where meaningful.
- Use real lists for lists, and tables only for tabular data with `th scope`.
- Buttons are buttons and links are links, both with visible text.
- Icon-only controls get an `aria-label` that matches their visible tooltip.
- Decorative images get `alt=""`. Informative alt text describes meaning, not appearance ("Chart: conversion fell from 18% to 9% in May").
- Hide decorative SVG from assistive tech, and never hide focusable elements.

## 56. Keyboard
- Tab order follows visual order, and nothing is focusable unless it's interactive.
- Focus is visible everywhere: a 2px ring at 3:1 with offset ≥2px.
- Enter activates, Space toggles and Esc closes dialogs and menus.
- Dialogs move focus in, trap it and return it to the trigger, with a modal dialog role and a label.
- A "Skip to content" link is the first focusable element, visible on focus.
- Custom widgets implement their ARIA patterns correctly (tabs with selected state and arrow keys), or use the native element. A native select beats a broken custom one.

## 57. Contrast & Targets
- Text is 4.5:1, large text 3:1, and UI and focus 3:1 against what's next to them.
- Pointer targets are at least 24×24px (WCAG 2.2 AA), with 44×44px recommended and for touch.
- A 24px target with ≥24px gaps to its neighbors passes.
- Check the focus ring against its own background, on both dark and light surfaces.

## 58. Accessible Forms
- Every input has an associated label. Placeholder-only labels fail.
- Use the correct `type` and `autocomplete` tokens.
- Mark fields required (with `aria-required` too), and style validation with `:user-invalid` so users aren't punished before they submit.
- Use one column for four or more fields, labels above inputs, and hints tied to their fields.
- Errors are never color-only: give a text message plus an icon, announced assertively, naming the field and the fix.
- Multi-step wizards announce progress, summarize errors at the top, and keep back/next keyboard-safe.

## 59. Motion & Cognition
- Reduced motion means no parallax, autoplay carousels or marquees.
- Never autoplay media with sound. Carousels pause on hover and focus.
- Timeouts give at least a 20s warning, or user control.
- Use plain language, and expand abbreviations at first use.

## 60. Accessibility Testing Ritual
1. Tab through the whole page: focus visible at every stop, a sane order, no traps.
2. Use a screen reader to check the title, heading outline, labels and regions.
3. Sample the contrast of every text/background pair: headings, body, muted text, button text, placeholders and input borders.
4. At 200% zoom (up to 1280px wide), check for no horizontal scroll and no clipping.
5. Check for no empty buttons or links, and no redundant labels.
6. Check that both dark and light variants pass.

---

# Part 10 — Design Review

## 61. The Review Process
- Never fix while reviewing. The order is audit → rank → fix → verify.
- Capture full-page screenshots at desktop 1440, tablet 768 and mobile 390. Review what is there, not what you think is there.
- Do an 8-second first read: can you name the product, audience and primary action?
- Rank every finding:
  - P0 blocking or legal
  - P1 seriously undermines quality
  - P2 polish
  - P3 preference
- Fix in ranked order with atomic changes, then re-screenshot to confirm each fix didn't break the design argument.
- Never audit from code alone.

## 62. The Taste Pass
- The kill question: could a default agent have generated this? Every slop pattern found is a **P1**, never a "style preference".
- Hierarchy: one dominant element per viewport, where the business wants the eye to land.
- Type: text under 10px, more than three weights, no display contrast, full-width body, six-line paragraphs, widows.
- Color: more than about three meaningful colors, decorative gradients, the accent used more than four times per viewport, white on pale fills, contrast failures.
- Alignment: shared edges line up, hairline grid vs. scattered cards, and spacing-scale integrity (any 7px or 13px paddings?).
- Depth: shadows as the only depth, glass everywhere, nested cards.

## 63. Nielsen's 10 Heuristics, Applied
1. Visibility of status: every action gives feedback within 2–3s, with no dead buttons.
2. Match the real world: use the user's language ("deploy instance" on a consumer site fails).
3. User control: exit routes everywhere, and undo for destructive acts.
4. Consistency: one button style, and one way to reach the same destination.
5. Error prevention: confirm destructive actions, guard submits, use autocomplete.
6. Recognition over recall: no invented jargon.
7. Flexibility: shortcuts for repeat users that don't clutter the novice path.
8. Aesthetic and minimal: anything hiding the primary action is noise.
9. Errors explain what, why and what to do.
10. Help appears where users get stuck.

## 64. The Conversion Pass
- One primary CTA above the fold.
- The value lands in ≤8 seconds through the headline, not the sub-subline.
- Take a friction inventory: justify every field, step and click between "interested" and "started".
- Put trust signals where decisions happen.

## 65. Review Report Format
- Group findings under P0 / P1 / P2 / P3, each with a screenshot reference and a one-sentence fix.
- End with a one-paragraph verdict that names the ONE most important change.
- List P3 items but never fix them in the same session as P1s.
- If you can't name one key change, the audit didn't find the real issue.

---

# Part 11 — Design Systems

## 66. Three-Tier Tokens
- **Primitive:** raw values (`--color-ink-900`, `--space-4`, `--radius-md`).
- **Semantic:** meaning (`--color-surface`, `--color-text-muted`, `--space-inset-lg`). Products consume only these.
- **Component:** aliases (`--button-bg-primary`, `--input-border-width`).
- The chain runs component → semantic → primitive → value. Skipping a layer forks the system.
- Use kebab-case, noun first and scale last. Never encode intent ("fancy-purple") or put hex in components.

## 67. Fixed Scales
- Spacing: 4/8/12/16/24/32/48/64/96. Go below 4 only for hairlines.
- Never use 5, 7, 10 or 14px without a documented optical override.
- Type: 12/14/16/18/24/32/48/64, fluid via `clamp()`.
- Radius tokens, e.g. sm 2px, md 6px, lg 12px.
- Color ramps: 9–11 OKLCH steps.
- Elevation: three levels max.

## 68. Inventory Before Building
- Colors: list every hex. More than 15 out-of-scheme colors means the system is broken.
- Spacing: flag values off the 4px or 8px scale.
- Type: more than five sizes on one page means no hierarchy.
- Radius, elevation and borders: collect every value and cluster into 2–4 tokens.
- Components: flag components with more than three variants doing the same job, and anything styled from raw values.
- Output a token map, a violation list with counts and a fix order. Audit, report, then change. Never refactor in the same pass.

## 69. Component Anatomy
- One job, one name. An "and" in the description means split it.
- A full state matrix: default, hover, active, focus-visible, disabled, loading, error. Document impossible states.
- Size variants only where real (sm/md/lg), never color variants pretending to be states.
- Responsive behavior, with its breakpoint.
- Zero raw values in component styles.

## 70. Governance
- One documentation page per component: purpose, anatomy, states, usage, do/don't and accessibility notes.
- Token changes are additive: add the new token, deprecate the old, then remove it after one release cycle. Never silently change a token's value.
- One owner holds the token file.
- Track adoption quarterly: % of screens on semantic tokens, raw-color violations, off-scale spacing and % of components with documented states. The goal is a falling violation count.

---

# Part 12 — Brand Identity

## 71. Concept First
- Reduce the mark to one idea in two words ("north + needle", "record + flower").
- Literal category icons (sparks, rockets, chat bubbles, gears) are a last resort.
- Test at 16px before falling in love. The mark must read as a favicon.
- Two colors is the hard ceiling: ink + one accent, or monochrome. A mark that needs its gradient isn't a mark.

## 72. Wordmarks
- Modify a strong existing face rather than inventing one.
- Make one typographic move only: tight tracking (`−0.03em`), OR a case change, OR one altered glyph or punctuation detail. Two moves is a novelty logo.
- Test in caps, sentence case and at 12px.
- Never letterspace lowercase or stretch type. Use the real condensed family.

## 73. Lockups
- Build on a construction grid with shared optical centers.
- Clear space equals the height of the mark's smallest element (or ¼ of the mark's width) on all sides.
- Define three lockups: horizontal, stacked and compact.
- Minimum sizes: mark ≥16px favicon and ≥24px in-app, wordmark ≥12px in compact lockups only.
- Banned: shadowed, gradient or small outlined marks, and a mark shown without the name on first view.

## 74. Brand Color & Deliverables
- Ink plus one accent from the page palette, with a reversed (light-on-dark) variant and a 100%-ink monochrome fallback.
- The accent is a signal, never a background fill. A wordmark uses the same ink as the headings.
- Deliverables:
  - an SVG primary lockup
  - a favicon at 32px and 180px
  - an og-image at 1200×630 with ≥80px margins, never a site screenshot
  - a one-page brand sheet

---

# Part 13 — Code Craft as Design

## 75. Semantic Markup
- Use the element that means the thing: nav, main, labeled sections, figure, time, button and real links. Never a clickable div.
- A row of features is a list.
- Every image has alt text and explicit width/height.
- A page with no main, an unheaded section or a clickable div fails.

## 76. Tokens Over Literals
- Every color, spacing value, radius, shadow and font size comes from a variable, with zero hardcoded hex in components.
- A literal repeated three times is a missing token.
- The code palette matches the design read exactly. No invented extra grays.
- Use one breakpoint convention.

## 77. CSS Hygiene
- No `!important`, no ID styling, no side-effect element selectors, and no `*` rules beyond a box-sizing reset.
- Nest two levels at most.
- Utility classes are fine if the config is tokenized and readable. No 30-class soup.
- Delete unused CSS before shipping.
- No inline styles, except for dynamic CSS variables, a single documented one-off, or SVG attributes. More than about five inline styles on a page means architecture drift.
- No dead markup, console logs, lorem ipsum, placeholder image services or broken images.

## 78. Code Review Order
1. Behavior, including empty, error, repeated-click and offline cases.
2. Structure.
3. Taste: naming, duplication, consistency.
4. Security.
5. Performance.
6. Accessibility.
- Every finding gets a severity (blocker / should-fix / nit), a location, the problem and the fix.
- Breaking the design system is a blocker.
- Keep to about 10 findings on a diff that deserves fewer.
- Hold generated code to the same bar as written code.
- Final question: would I merge this if I'd written it?

---

# Part 14 — Performance as Design

## 79. Budgets
- At p75 on mobile: **LCP < 2.5s**, **CLS < 0.1**, **INP < 200ms**.
- A marketing page weighs ≤1.5MB, and a simple page < 500KB.
- Write the budget down. No budget means no plan.

## 80. Fonts
- Two families max and about four styles max.
- `font-display: swap`, with ≤3px shift when the font lands.
- Preload the hero face (woff2), and subset the rest.
- No `@import`, no blocking font scripts, and no unused fonts.
- Decorative display fonts can give way to system fonts below the hero.

## 81. Images
- Every image has dimensions or an aspect ratio.
- Use AVIF/WebP, and PNG only for real transparency. Never a 2MB JPEG.
- Use `srcset`/`sizes`, lazy-load below the fold, and give the LCP image high fetch priority.
- Make decorative backgrounds in CSS (gradients, noise, patterns), not 400KB images.

## 82. Delivery
- One CSS file or critical CSS.
- Defer non-critical JS, and no framework for a static page.
- No synchronous third-party scripts in the critical path.
- Run a throttled mobile audit and report the vitals and weight. Re-check after any font or image change.

---

# Part 15 — Genre Identities

## 83. Editorial Minimal: "A printed broadsheet that happens to be a website"
- **Palette:**
  - paper `#F5F1EA` (alternate `#EFEAE1`)
  - ink `#1A1A18`, secondary ink `#6B675E`
  - vermillion `#E34A2B` (or `#C73E1D`), once per page
  - hairlines `rgba(26,26,24,0.14)`
  - no other colors, no gradients, no dark sections
- **Display:** a characterful serif (Fraunces, Newsreader, Georgia/Charter) at `clamp(2.8rem, 7vw, 6.5rem)`, leading 0.98–1.08, normal weight.
- **Labels:** mono or small caps, uppercase, `0.10–0.15em`, 11–13px.
- **Body:** 16–18px, line-height 1.6–1.7, max 32–40em wide.
- **Flourishes:** italic serif pull-quotes and oversized drop figures ("01").
- **Composition:**
  - a 7/12 headline with a 5/12 index column
  - every section opens with "01 — Approach" and a hairline rule, so the page reads like a table of contents
  - rows over cards; any cards have square corners, tonal paper panels and a 1px hairline
  - hero padding ≥15vh, section gaps 96–160px
- **Content:** no emoji, metrics as a mono typeset table, no browser-chrome screenshots.
- **CTA:** one solid vermillion square button plus a caps text link.
- **Motion:** one 8–12px fade-up at 400ms, and an underline-on-hover trick.
- **Fail if:** any extra color, a radius ≥6px on a major surface, a headline under 2.8rem or wider than 22em, a full-width body, a centered hero.

## 84. Quiet Luxury: "A private bank's annual report"
- **Palette:**
  - ivory `#F7F2EA` (panels `#EFE8DC`)
  - espresso ink `#17130F`, secondary `#6E655A`
  - one accent: brass `#9A7B4F`, oxblood `#742D2C` or forest `#2E4436`
  - rules `rgba(23,19,15,0.18)`
  - no pure white, no gradients, no glow
  - shadows only on floating elements (blur ≥40px, ≤0.12 opacity)
- **Display:** a high-contrast serif (Cormorant, Playfair, Garamond) at `clamp(2.6rem, 6.5vw, 5.5rem)`, weight 400–500, leading 0.95–1.05, with one italic word per headline.
- **Body:** sans at 300–400, 16–17px, line-height 1.7, in soft ink, never pure black.
- **Labels:** small caps at `0.18–0.28em`, 10–11px.
- **Numerals:** serif oldstyle figures.
- **Composition:**
  - whitespace is the product: hero ≥18vh, sections ≥140px apart
  - a 7/12 headline, a vertical rule and a 3/12 label index
  - hairlines, not boxes; panels have no border and ≤2px radius
  - pricing as a hairline list with a thin accent rule over the featured tier
- **Content:** film-grade muted imagery, letterboxed with margins; short sentences, no exclamations.
- **CTA:** one ≤4px-radius button plus a small-caps text link.
- **Motion:** a 10–14px rise over 500–700ms with `cubic-bezier(0.22, 1, 0.36, 1)`; hover shifts to the accent or 0.85 opacity over 200ms.

## 85. Japanese Minimal: "A room with one vase"
- **Palette:**
  - rice paper `#F4F1EA` (alternate `#ECE8DF`)
  - sumi ink `#33302B`, ash `#8A8378`
  - hanko red `#B3392A` as the entire accent budget (seal, one underline, one stat, links)
  - accent is a mark, never a surface; no pure white, no gradients
- **Display:** a mincho serif (Shippori Mincho) at 400–600, `clamp(2.4rem, 6vw, 5rem)`, leading 1.15–1.3. No italics and no uppercase display.
- **Body:** a gothic (Zen Kaku Gothic New) at 300–400, 15–16px, line-height 1.8–2.0.
- **Labels:** gothic caps or roman numerals, `0.18em`, 10–11px.
- **Signature:** exactly one vertical text element per page (`writing-mode: vertical-rl`).
- **Composition:**
  - ma is the layout: hero ≥20vh, sections ≥160px apart
  - emptiness is correct, so don't fill it
  - content in a 5/12–7/12 offset column, one object per line of sight
  - 1px ash rules; borderless tonal panels
  - index rows: number / name / note
  - the hanko seal appears exactly twice (near the wordmark and in the footer)
- **Content:** typographic marks (・ — ◦); at most 1–2 muted images, smaller than the column, at `saturate(0.7) contrast(0.95)`; observational copy with no superlatives.
- **Motion:** an 8–10px fade/rise over 500–700ms; hover in seal red or 0.75 opacity.
- **Fail if:** radius >2px, any box-shadow, a sans display, more than one vertical element.

## 86. Brutalist Industrial: "A declassified blueprint"
- **Palette:**
  - aged paper `#F2F1EC` (dark `#1B1B18`)
  - ink `#141414`, secondary `#6E6C64`
  - one signal color: safety orange `#E8540B`, industrial yellow `#E3B23C` or technical blue `#2B5FA8`
  - 1px full-ink rules everywhere
  - no gradients, shadows or glow; depth comes from offset solid blocks
- **Display:** a heavy grotesk (Archivo Black) at 700–900, uppercase, `−0.01em`, `clamp(2.6rem, 7vw, 6rem)`.
- **Body:** the same family at 400, 15–17px.
- **Labels:** mono uppercase at `0.08–0.12em`, 10–12px, carrying coordinates ("01 / 04"), spec numbers ("GS-114") and status.
- **Never:** italic, serif or lowercase as the brand.
- **Composition:**
  - the visible grid is the design
  - masthead: wordmark left with mono coordinates right ("N-01 / REV 3"), closed by rules
  - a giant full-width headline with a signal-marked mono kicker (▪ ▸), body in 5/12, and a mono exit line plus CTA box
  - features and pricing as ledger rows; the featured row gets a signal fill
- **Buttons:** rectangles with a `4px 4px 0` hard shadow, removed on press.
- **Motion:** instant or 80–150ms snaps; hover inverts colors; one 8px clip-reveal at 150ms.

## 87. Neo-Brutalism: "Loud, honest, square"
- **Palette:**
  - paper `#FFF8E7` (fields `#FFEFC2`)
  - ink `#0A0A0A` for every border, all text and all shadows
  - two accents max: hot `#FF3878` (dominant) and cool `#7CC6FE` (supporting)
- **Rules:** everything has a 2.5px ink border; shadows are hard (`6px 6px 0 #0A0A0A`) on 60–70% of elevated elements; no soft shadows, gradients or glass.
- **Display:** Space Grotesk 700 / Archivo 800 at `clamp(2.6rem, 7vw, 5.5rem)`, leading 0.98, `−0.02em`.
- **Labels:** mono caps, 11px, `0.06em`.
- **Emphasis:** one trick, used ≤3 times (a highlight swatch, or a 6px ink underline).
- **Composition:**
  - rotations of 1–2°, on at most three elements per page
  - ≤2 hot fields and ≤2 cool fields per viewport, never two hot fields side by side
  - alternating paper and ink sections
  - pricing as paper / hot / paper, with the hot card's shadow biggest
- **Buttons:** ≥56px tall, pressing translates 6px and drops the shadow.
- **Copy:** direct and a little cocky, one "!" max, packaging-label price details stamped "MOST POPULAR".
- **Motion:** 150–250ms snaps with `cubic-bezier(0.34, 1.56, 0.64, 1)`; hover flips the border color or grows the shadow 2px; zero loops.

## 88. Retro Print: "A risograph poster just off the drum"
- **Palette:**
  - stock `#F4EDDE` (panels `#EBE2CF`)
  - ink `#21201C`
  - two riso inks max: red `#E4572E`, then blue `#355E8C`
  - no gradients, blurred shadows or pure white
- **Display:** a condensed poster face (Anton, Archivo Narrow 800), uppercase, `clamp(2.8rem, 8vw, 7rem)`, leading 0.95–1.0.
- **Body:** a quiet serif (Newsreader, Georgia) at 16–18px.
- **Labels:** mono caps at `0.1em`.
- **Signature:** misregistration (`text-shadow: 2px 2px 0` in red or blue) on 2–3 headings only, in one direction per page, never on body text.
- **Texture:**
  - halftone dot fields from a radial-gradient (≈1.2px dots on an 8–12px grid), ≤2 panels per page
  - full-bleed ink rules and print bleed
  - rotated dashed stamps (1–3°), max two
  - big red numerals with a blue offset
- **Composition:**
  - a 5/7 or 4/8 poster grid, one giant element per viewport
  - hero: stamp → headline → right-aligned serif 4/12 → two-line mono colophon
  - pricing as paper / ink / paper cards
  - duotone photos with a 1.5px frame
- **Motion:** a 200ms 6px snap-up ("paper landing"); hover turns red over 100ms.
- **Fail if:** no texture anywhere, because texture is the identity.

## 89. Playful Color: "A poster you can't walk past"
- **Palette:**
  - cream `#FDF6EC` / `#FFF9EF`, never white
  - ink `#101014`
  - two saturated inks max, from cobalt `#2E4BFF`, tomato `#FF4D2E`, banana `#FFD100`, mint `#2BD99B` and fuchsia `#FF3ED2` (one dominant, one supporting)
  - 2–3px ink "sticker cut-line" outlines
  - hard `6px 6px 0` shadows only, on 2–3 hero elements, one per viewport
- **Display:** ultra-heavy (Archivo Black, Bricolage 800) at `clamp(3rem, 8vw, 7rem)`, leading 0.95, `−0.02em`.
- **Body:** 16–18px. **Labels:** `0.06em`.
- **Emphasis:** one trick, ≤3 times.
- **Composition:**
  - on-grid bones with 2–4° rotations on 2–3 hero elements
  - color-blocked full-bleed sections
  - solid-field sticker badges
  - two colors max in the hero
  - pricing as paper / accent / paper, with a shadow on the featured card only
- **Content:** drawn marks (dot grids, asterisks, 3px arrows, squiggles), flat geometric illustration (no 3D or gradients), one "!" per page.
- **Buttons:** ≥56px chunky CTAs.
- **Motion:** spring `cubic-bezier(0.34, 1.56, 0.64, 1)` over 350–500ms, once per element; hover moves −3px and grows the shadow +2px; the logo wiggles at most once.

## 90. Dark Tech: "A machine you can trust"
- **Palette:**
  - ground `#08090A`
  - panels `#0E0F11` / `#131417`, hover `#181A1D`
  - text `#F7F7F8` / `#9CA3AD` / `#5C6370`
  - borders `rgba(255,255,255,0.08)`, interactive `0.16`
  - one accent: indigo `#5E6AD2`, violet `#7C7CF0` or emerald `#34D399`
- **Rules:** no gradients and no colored full-bleed sections; glow only on the primary button (`0 0 0 1px` accent at .35 plus `0 0 24px` at .25).
- **Display:** Space Grotesk or system 500–600 at `clamp(2.2rem, 5vw, 4rem)`, `−0.03em`, leading 1.05, capped at 4rem.
- **Body:** 14–15px in secondary gray. Pure white is reserved for headings, key values and interactive labels.
- **Labels:** mono 11–12px with no tracking theatrics. A 12–14px UI density is normal.
- **Composition:**
  - 1px borders on every panel and cell, with tonal fills
  - data, code, terminals and status tables as the hero
  - radius 6–10px on panels and 4–6px on buttons (the one identity where radius fits)
  - shadows only on hover (`0 4px 20px rgba(0,0,0,.5)`)
  - pricing as bordered panels, with an accent border on the featured one
- **Icons:** 1.5px stroke on a 16–20px grid.
- **Copy:** status language ("v2.4.1", "99.99% SLA").
- **Motion:** 120–240ms with `cubic-bezier(0.4,0,0.2,1)`; hover shifts surface tone and brightens the border; one slow live-dot pulse (2–4s, opacity only).

## 91. Corporate Trust: "Bought because nothing surprised anyone"
- **Palette:**
  - white `#FFFFFF`, panels `#F8FAFC`, hover `#F1F5F9`
  - ink `#0F1722` / `#3B4657` / `#5B6777`
  - borders `#E1E7EF`, stronger `#C7D0DC`
  - one accent: deep blue `#1F4FE0`
  - status only: success `#0E7F4B`, danger `#C0362C`
  - shadows at most `0 1px 2px rgba(15,23,34,0.06)`; no gradients and no dark hero
- **Display:** system sans 500–600 at `clamp(1.8rem, 3.6vw, 2.8rem)`, hard-capped at 2.8rem. No serif or uppercase display.
- **Body:** 15–16px, line-height 1.6. **Labels:** 12–13px at 500.
- **Composition:**
  - conventional layouts are correct for this audience: a left-aligned hero and a 12-column grid
  - hero: eyebrow → H1 (2.2–2.8rem) → sub → buttons → a bordered metric panel
  - evidence is the ornament: grayscale logos, sourced metrics ("Based on 2,400 customers, 2025"), text compliance chips, titled quotes
  - tables are the signature component (1px rules, 12px header caps, 14px rows, `#F8FAFC` row hover)
  - pricing as a table beats pricing cards
  - cards have 8px radius, and the border darkens on hover with no lift
  - complete footers with legal links
- **Copy:** every claim is qualified or sourced; tabular, precise numbers; concrete buttons ("Request a demo").
- **Motion:** 120–150ms background/border hovers only, plus at most one 200ms, 6px reveal.

## 92. Cinematic Motion: "Opening credits on studio print"
- **Palette:**
  - canvas `#F7F5E7`, cards `#FCFBF4`
  - ink `#121212`, muted `rgba(18,18,18,.55)`
  - one electric blue `#0F4BFD`
  - no gradients, pure black or white sections
- **Rhythm:** paper scenes alternate with at most two ink scenes and exactly one full-blue scene.
- **Type:** grotesk only (Inter Tight), no serif and no italic.
  - Headlines `clamp(3rem, 9vw, 8rem)`, weight 600, leading 0.94, `−0.04em`, with exactly one blue accent word.
  - Scene h2s `clamp(1.6rem, 3.4vw, 2.6rem)`.
  - Mono kickers at `0.14em`: "01 — THE LEAK".
  - Body ≥14.5px, line-height 1.65–1.7.
- **CTAs:** pills with a blue fill sweeping up on hover; one per viewport.
- **Structure:** a film sequence (hero with a live product screen, briefs, a pinned index, a marquee, a blue brief, a drag carousel, a native details accordion, a pinned roadmap, evidence, close, colophon footer). Two pins in total.
- **Hero presence without video:** a CSS-built live dashboard (ticking counter, bars, waveform), plus a ≤0.16-alpha particle field and an orbit ring. All of it is gated and stops under reduced motion.
- **Motion:**
  - a preloader of ≤2s, shown only when JS and motion are active
  - a hero intro of ≤1.4s with `expo.out`
  - a scrubbed numeral count with snapping, a drag carousel with inertia, and a blue rail fill climbing through roadmap steps
  - count-ups, a difference-blend cursor hidden on touch, and a magnetic CTA (≤5px pull)
  - 0.9–1.6s durations, `power3.out`/`expo.out`, scrub 0.6–1
- **Still-frame rule:** the page must be complete and beautiful with JS off and reduced motion on.

## 93. Choosing an Identity
- Editorial minimal suits publications, essays, portfolios and thoughtful products.
- Quiet luxury suits premium services, finance and high-ticket brands.
- Japanese minimal suits calm, craft and contemplative products.
- Brutalist industrial suits technical, hardware and systems tools with attitude.
- Neo-brutalism suits loud consumer and indie products.
- Retro print suits culture, events, indie and zine-spirited brands.
- Playful color suits consumer, education and joyful products.
- Dark tech suits developer and infrastructure tools.
- Corporate trust suits enterprise, regulated and procurement-driven buyers.
- Cinematic motion suits launch moments that should feel like a site-of-the-day film.
- Pick one identity per project and apply its fixed palette, type, composition and motion completely. Mixing identities dilutes all of them.

---

# Part 16 — Proving It Works

## 94. Before/After Ritual
- Run the same prompt twice, once with no guidance and once with it, so the guidance is the only variable.
- Screenshot both at the same viewport (1440×900), full page, with no scrollbars.
- Use real agent output only, never hand-tuned screenshots.
- State the prompt verbatim. Reproducibility is the trust layer.
- Ten radically different identities from one brief is the strongest proof that taste can be instructed.
