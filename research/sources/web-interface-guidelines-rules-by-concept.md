# Design Rules by Concept

Distilled from the Web Interface Guidelines (accessible, fast, delightful UIs), plus deep dives into the pages they reference: ARIA component patterns, WCAG criteria, APCA contrast, scroll/pointer CSS, and media delivery.

# Part 1 — Guiding Principles

## 1. Interfaces Are Hundreds of Small Decisions
- Interfaces succeed because of hundreds of small, deliberate choices; treat every detail (an ellipsis, a focus ring, a hit target) as a design decision, not an afterthought.
- Rules carry strength levels: MUST = non-negotiable, SHOULD = default unless there's a reason, NEVER = a flagged anti-pattern.
- Audit every generated interface against the full list; AI-generated UI routinely misses these details.
- When reviewing, be terse and high signal: state the issue and its location; only explain when the fix isn't obvious.

## 2. The Three Goals
- Accessible: everything works with keyboard, assistive tech, zoom, and without relying on colour.
- Fast: the UI responds immediately, never shifts, never blocks input.
- Delightful: motion and polish are used deliberately, only where they clarify or genuinely delight.

# Part 2 — Keyboard & Focus

## 3. Keyboard Works Everywhere
- MUST: every flow is fully keyboard-operable and follows the standard ARIA authoring patterns for its component type.
- Interactive custom elements need keyboard handlers, not just click handlers; prefer native elements so you get them for free.
- Use `<button>` for actions and `<a>` for navigation; a `<div>` or `<span>` with a click handler is an anti-pattern.

## 4. Clear, Visible Focus
- MUST: every focusable element shows a visible, unobscured focus ring.
- Prefer `:focus-visible` over `:focus` so pointer users don't see rings on click.
- Use `:focus-within` to highlight grouped/compound controls.
- NEVER: `outline: none` (or a utility like `outline-none`) without a visible replacement focus style.
- Sticky headers, footers, banners and overlays must never cover the focused element.

## 5. Manage Focus
- MUST: trap focus inside modal surfaces, move focus into new content, and return focus to the trigger on close, per standard patterns.
- On form submit with errors, move focus to the first error.

## 6. Autofocus for Speed
- SHOULD: autofocus on desktop when a screen has a single primary input.
- Rarely autofocus on mobile: the opening keyboard causes layout shift.
- Treat any autofocus without a clear justification as a smell.

## 7. Locale-Aware Keyboard Shortcuts
- Internationalise shortcuts for non-QWERTY layouts.
- Display platform-specific symbols (`⌘` on macOS, `Ctrl` on Windows/Linux).

# Part 3 — Targets, Touch & Pointer

## 8. Match Visual and Hit Targets
- MUST: hit targets are at least `24px`; on mobile at least `44px`.
- If the visual target is smaller than `24px`, expand the hit area (padding or pseudo-element) rather than the visual.
- Keep visual target and hit target matched otherwise, so what looks tappable is exactly what is tappable.

## 9. No Dead Zones
- MUST: if part of a control looks interactive, it is interactive; users should never guess where to click.
- Checkboxes and radios: the label and control share one generous hit target with no gaps.
- Clicking a `<label>` focuses or toggles its associated control.

## 10. Design Forgiving Interactions
- Minimise finickiness: generous hit targets, clear affordances, predictable behaviour.
- Use prediction cones (safe triangles) on submenus so diagonal pointer movement toward a submenu doesn't close it.

## 11. Mobile Input Size
- MUST: `<input>` font size is at least `16px` on mobile, preventing iOS Safari auto-zoom/pan on focus.

## 12. Respect Zoom
- NEVER disable browser zoom (`user-scalable=no`, `maximum-scale=1`); fix the input size instead.

## 13. Touch Behaviour
- MUST: set `touch-action: manipulation` on controls to prevent double-tap zoom delay.
- SHOULD: set `-webkit-tap-highlight-color` intentionally so the tap highlight follows the design.

## 14. Overscroll
- MUST: `overscroll-behavior: contain` in modals, drawers and sheets so scrolling doesn't chain to the page behind.
- To suppress desktop rubber-band bounce, set `overscroll-behavior: none` on `<html>` only inside `@media (pointer: fine)`.
- Keep page overscroll defaults on coarse-pointer devices to preserve pull-to-refresh.
- `pointer` describes the primary input only; test hybrid touch devices separately.
- `none` also disables scroll chaining and native swipe-back navigation; use it knowingly.

## 15. Clean Drag Interactions
- MUST: during a drag, disable text selection and set `inert` on the dragged element so selection and hover don't fire simultaneously.

## 16. Gestures Have Alternatives
- MUST: every drag, swipe, pinch or path-based action also works with a tap/click control and with the keyboard, unless the gesture is essential.

## 17. Tooltip Timing
- MUST: delay the first tooltip in a group; once one is open, subsequent peer tooltips appear with no delay.
- Prefer inline help first; tooltips are a last resort.

# Part 4 — Navigation & State

## 18. URL as State
- MUST: persist UI state in the URL so share, refresh and Back/Forward all work.
- Deep-link everything: filters, tabs, pagination, expanded panels — any piece of local component state is a candidate.

## 19. Links Are Links
- MUST: use real anchors for navigation so Cmd/Ctrl+Click, middle-click and right-click "open in new tab" work.
- NEVER substitute a `<button>` or `<div onClick>` for a navigational link.

## 20. Scroll Positions Persist
- MUST: Back/Forward restores the prior scroll position.

## 21. Anchored Headings
- Set `scroll-margin-top` on headings so section links don't land under a sticky header.

## 22. Accurate Page Titles
- MUST: `<title>` reflects the current context (page, item, state).

## 23. No Dead Ends
- MUST: every screen offers a next step or a recovery path.

## 24. Unsaved Changes
- MUST: warn before navigation when data could be lost.

# Part 5 — Feedback, Loading & Async

## 25. Loading Buttons
- MUST: show a loading indicator and keep the original label visible.

## 26. Minimum Loading-State Duration
- Add a show-delay of `~150–300ms` before showing a spinner or skeleton.
- Once shown, keep it visible for a minimum of `~300–500ms` to avoid flicker on fast responses.

## 27. Stable Skeletons
- MUST: skeletons mirror final content exactly so nothing shifts when it loads.

## 28. Optimistic Updates
- SHOULD: update the UI immediately when success is likely; reconcile with the server response.
- On failure, show an error and roll back, or offer Undo.

## 29. Confirm Destructive Actions
- MUST: destructive actions require confirmation or provide Undo with a safe window; never act immediately and irreversibly.

## 30. Ellipsis for Follow-Up and Loading
- Menu options that open further input end with an ellipsis: "Rename…".
- Loading/processing states end with an ellipsis: "Loading…", "Saving…", "Generating…".

## 31. Announce Async Updates
- MUST: use polite `aria-live` for toasts and inline validation so assistive tech hears them.

## 32. Network Latency Budget
- MUST: mutations (`POST`/`PATCH`/`DELETE`) complete in under `500ms`.

# Part 6 — Forms

## 33. Enter Submits
- MUST: when a text input is focused, Enter submits if it's the only control; with many controls, Enter applies on the last one.
- In a `<textarea>`, `⌘/Ctrl+Enter` submits and Enter inserts a newline.

## 34. Labels Everywhere
- MUST: every control has a `<label>` or an associated accessible label.
- Labels are clickable and focus their control.

## 35. Submission Rule
- MUST: keep submit enabled until submission starts; then disable it during the in-flight request, show a spinner, and include an idempotency key.
- NEVER pre-disable submit; allow submitting incomplete forms so validation feedback surfaces.

## 36. Don't Block Typing
- MUST: accept free text even in number-only fields, then validate and explain; silently blocking keystrokes gives the user no explanation.

## 37. Don't Block Paste
- NEVER disable paste in `<input>` or `<textarea>`.

## 38. Error Placement
- MUST: show errors inline next to their fields; on submit, focus the first error.

## 39. Autofill and Names
- MUST: set `autocomplete` and a meaningful `name` on inputs to enable autofill.
- Use the correct `type` (`email`, `tel`, `url`, `number`) and `inputmode` for better keyboards and validation.

## 40. Spellcheck Selectively
- SHOULD: disable spellcheck on emails, codes, usernames and similar.

## 41. Placeholders
- Placeholders signal emptiness and end with an ellipsis.
- Set placeholders to an example value or pattern, e.g. `+1 (123) 456-7890`, `sk-012345679…`.
- Placeholders never replace labels.

## 42. Password Managers and 2FA
- MUST: stay compatible with password managers; allow pasting one-time codes.
- Don't trigger password managers on non-auth fields (e.g. Search): avoid reserved names like `password`; use `autocomplete="off"` or a specific token like `autocomplete="one-time-code"` for OTP.

## 43. Trim Input
- MUST: trim values; text replacements and expansions can add trailing whitespace that would otherwise cause a confusing error.

## 44. Hydration-Safe Inputs
- MUST: inputs never lose focus or value after the page hydrates.
- A controlled input with a value needs a change handler (or use an uncontrolled default value).

## 45. Windows Select Contrast
- MUST: explicitly set `background-color` and `color` on native `<select>` to avoid dark-mode contrast bugs on Windows.

# Part 7 — Animation

## 46. Honor Reduced Motion
- MUST: honour `prefers-reduced-motion` with a reduced variant or by disabling motion.
- Muted decorative loops must stop under reduced motion.

## 47. Implementation Preference
- SHOULD: CSS > Web Animations API > JavaScript animation libraries; avoid main-thread JS-driven animation where possible.

## 48. Compositor-Friendly Properties
- MUST: animate `transform` and `opacity`.
- NEVER animate layout properties (`top`, `left`, `width`, `height`) that trigger reflow/repaint.

## 49. Never Transition All
- NEVER `transition: all`; explicitly list the properties you intend to animate (typically `opacity`, `transform`), since `all` can animate layout properties and cause jank.

## 50. Necessity Check
- SHOULD: animate only when it clarifies cause and effect, or adds deliberate delight.

## 51. Easing Fits the Subject
- SHOULD: choose easing based on what's changing — size, distance, trigger.

## 52. Interruptible and Input-Driven
- MUST: animations are cancelable by user input and respond mid-animation.
- Avoid autoplay except for muted, non-essential loops.
- MUST: autoplaying motion lasting more than `5s` alongside other content has pause, stop or hide controls.

## 53. Correct Transform Origin
- MUST: anchor motion to where it physically starts (a popover grows from its trigger).

## 54. SVG Transforms
- MUST: apply transforms/animations to a `<g>` wrapper with `transform-box: fill-box; transform-origin: center;` to avoid cross-browser origin bugs.

## 55. Text and Transforms
- Scaling text can change anti-aliasing; animate a wrapper instead of the text node.
- If artifacts persist, promote to its own layer with `translateZ(0)` or `will-change: transform`.

# Part 8 — Layout

## 56. Optical Alignment
- SHOULD: adjust by `±1px` when perception beats geometry (icons in buttons, play triangles, punctuation).

## 57. Deliberate Alignment
- MUST: every element aligns intentionally to a grid, baseline, edge, or optical centre; no accidental positioning.

## 58. Balance Lockups
- SHOULD: when text and icons sit side by side, tune weight, size, spacing or colour so they don't clash (e.g. a thin-stroke icon needs a bolder stroke next to medium-weight text).

## 59. Responsive Coverage
- MUST: verify on mobile, laptop and ultra-wide; simulate ultra-wide by zooming out to `50%`.

## 60. Safe Areas
- MUST: full-bleed layouts respect notches and insets with `env(safe-area-inset-*)`.

## 61. No Excessive Scrollbars
- MUST: render only useful scrollbars; fix overflow instead of hiding the symptom.
- Test with scrollbars always shown (as Windows users see them).

## 62. Let the Browser Size Things
- SHOULD: prefer flex, grid and intrinsic sizing over measuring in JS; let CSS handle flow, wrapping and alignment.

## 63. Resilient to Content
- MUST: layouts handle short, average and very long user-generated content.
- Text containers handle overflow with truncation, line-clamping, or word-breaking.
- Flex children need `min-width: 0` to allow truncation.
- Handle empty strings and arrays without rendering broken UI.

# Part 9 — Content & Typography

## 64. All States Designed
- MUST: design empty, sparse, dense and error states, not just the happy path.

## 65. Typographic Quotes and Ellipsis
- Prefer curly quotes (`“ ”`) over straight quotes (`" "`).
- MUST: use the ellipsis character `…`, never three periods `...`.

## 66. Widows and Orphans
- Tidy rag and line breaks; use `text-wrap: balance` (headings) or `text-wrap: pretty` (body).

## 67. Tabular Numbers
- MUST: use `font-variant-numeric: tabular-nums` (or a monospace) wherever numbers are compared, e.g. columns, counters, prices.

## 68. Non-Breaking Spaces
- Keep glued terms together with `&nbsp;`: `10&nbsp;MB`, `⌘&nbsp;+&nbsp;K`, multi-word brand names.
- Use a word joiner `&#x2060;` when terms must stay together with no space.

## 69. Redundant Status Cues
- MUST: never rely on colour alone; pair status colours with text labels or icons.

## 70. Locale-Aware Formats
- MUST: format dates, times, numbers, delimiters and currency for the user's locale using locale APIs rather than hardcoded formats.
- Detect language from browser language preferences, never from IP or GPS.
- Shield brand names, product names, code tokens and identifiers from auto-translation with `translate="no"`.

## 71. Brand Resources from the Logo
- Right-clicking the nav logo can surface brand assets for quick access.

# Part 10 — Accessible Content

## 72. Semantics Before ARIA
- MUST: prefer native elements (`button`, `a`, `label`, `table`) before reaching for `aria-*`.

## 73. Accessible Names
- MUST: icon-only buttons have a descriptive `aria-label`.
- Icons convey the same meaning in text for non-sighted users.
- Visual layouts may omit visible labels, but accessible names must still exist ("don't ship the schema" — the design omits, the semantics don't).
- Hide decoration with `aria-hidden`; images need `alt` (empty `alt=""` when decorative).
- Verify in the full accessibility tree.

## 74. Headings and Skip Link
- MUST: hierarchical `<h1>`–`<h6>` and a "Skip to content" link.

## 75. Accessible Media
- Caption speech and meaningful sounds; provide transcripts for audio-only content; describe essential visual information.
- Decorative media is hidden from assistive tech; media controls are keyboard-operable.

# Part 11 — Visual Design Details

## 76. Layered Shadows
- SHOULD: mimic ambient plus direct light with at least two shadow layers.

## 77. Crisp Borders
- SHOULD: combine borders with shadows; semi-transparent borders improve edge clarity on any background.

## 78. Nested Radii
- SHOULD: child radius ≤ parent radius, and concentric so curves align (inner radius = outer radius − padding).

## 79. Hue Consistency
- SHOULD: on non-neutral backgrounds, tint borders, shadows and text toward the background hue instead of using neutral grey/black.

## 80. Accessible Charts
- MUST: use colour-blind-friendly palettes.

## 81. Minimum Contrast
- MUST: meet contrast; prefer APCA over WCAG 2 for more accurate perceptual contrast.

## 82. Interactions Increase Contrast
- MUST: `:hover`, `:active` and `:focus` states have more contrast than the rest state.
- Buttons and links always have a visible hover state.

## 83. Browser UI Matches Background
- SHOULD: set `<meta name="theme-color">` to match the page background.
- MUST: in dark themes, set `color-scheme: dark` on `<html>` so scrollbars and native controls get proper contrast.

## 84. Avoid Gradient Banding
- Fading content to dark colours with CSS masks can band; use a background image instead when needed.

# Part 12 — Performance as UX

## 85. Test the Real Matrix
- SHOULD: test iOS Low Power Mode and macOS Safari.
- MUST: disable browser extensions that add overhead or change runtime behaviour while measuring.
- MUST: profile with CPU and network throttling.

## 86. Re-renders and Keystroke Cost
- MUST: track and minimise re-renders, and make them fast.
- SHOULD: prefer uncontrolled inputs; controlled-input loops must be cheap per keystroke.

## 87. Minimize Layout Work
- MUST: batch DOM reads and writes; never interleave them or read layout during render.

## 88. Large Lists
- MUST: virtualise large lists (more than `50` items), or use `content-visibility: auto`.

## 89. Images and Layout Shift
- MUST: set explicit image `width`/`height` and reserve space so images cause no CLS.
- Preload only above-the-fold images (high fetch priority); lazy-load the rest.

## 90. Network and Fonts
- SHOULD: `<link rel="preconnect">` to asset/CDN origins (with `crossorigin` when needed).
- SHOULD: preload critical fonts with `font-display: swap` to avoid flash and shift.
- Subset fonts to the code points/scripts you use via `unicode-range`, and limit variable axes to what you need.

## 91. Keep the Main Thread Free
- Move expensive, long-running work to Web Workers so interaction is never blocked.

## 92. Video Over GIF
- SHOULD: use `<video autoplay muted loop playsinline>` instead of animated GIF; modern video is much smaller.
- Provide a still alternative and honour `prefers-reduced-motion`.
- For short, non-essential loops, add an H.264 MP4 source to `<picture>` (Safari renders it as an image), gated by a reduced-motion media condition, with a still fallback; use `<video>` when users need controls or the motion is essential.

## 93. Hydration Safety
- Guard date/time rendering against server/client mismatch; suppress hydration warnings only where truly needed.

# Part 13 — Copywriting (Product Voice)

## 94. Active, Action-Oriented Voice
- Use active voice: "Install the CLI", not "The CLI will be installed".
- Lead with the action: "Install the CLI…" instead of "You will need the CLI…".

## 95. Case Conventions
- Headings and buttons use Title Case (Chicago style) in product UI; marketing pages use sentence case.

## 96. Clear and Concise
- Use as few words as possible.
- Prefer `&` over "and" where space is constrained.
- Keep nouns consistent; introduce as few unique terms as possible.
- Write in second person; avoid first person.

## 97. Numbers and Units
- Use numerals for counts: "8 deployments", not "eight deployments".
- Display currency with either 0 or 2 decimal places in a given context; never mix.
- Separate numbers and units with a (non-breaking) space: `10 MB`, not `10MB`.

## 98. Placeholders in Copy
- Use consistent placeholder values: strings `YOUR_API_TOKEN_HERE`, numbers `0123456789`.

## 99. Positive, Guiding Errors
- Default to positive, problem-solving language even for errors: "Something went wrong—try again or contact support" rather than "Your deployment failed".
- Error messages guide the exit: say how to fix it, not just what broke ("Your API key is incorrect or expired. Generate a new key in your account settings.").
- Pair the message with a button or link that performs the fix.

## 100. Specific Labels
- Avoid ambiguity: "Save API Key" instead of "Continue".

# Part 14 — Anti-Patterns to Flag

## 101. The Review Blacklist
- `user-scalable=no` or `maximum-scale=1` disabling zoom.
- Paste prevented on inputs.
- `transition: all`.
- `outline: none` without a focus-visible replacement.
- Navigation via click handlers instead of an anchor.
- `<div>` or `<span>` with click handlers instead of `<button>`.
- Images without dimensions.
- Large lists rendered without virtualisation.
- Form inputs without labels.
- Icon buttons without `aria-label`.
- Hardcoded date/number formats.
- Autofocus without clear justification.
- Animated GIF where compressed video would work.
- Gesture-only actions with no tap/click and keyboard alternative.
- `...` instead of `…`; straight quotes instead of curly.
- Destructive actions that execute immediately with no confirm or Undo.

# Part 15 — Keyboard & Focus Fundamentals

## 102. Keyboard Operability Baseline
- Every interactive element must be operable from the keyboard alone; pointer-only interactions are a defect.
- `Tab` / `Shift`+`Tab` move between components; arrow keys (plus `Home`, `End`, `Page Up`, `Page Down`) move within a composite widget.
- A composite widget (radio group, tablist, menu, listbox, grid, tree, toolbar) exposes exactly one tab stop; its children are reached with arrow keys.
- Borrow key bindings from equivalent desktop GUI controls so users can transfer existing knowledge; keep the same pattern behaving identically everywhere in the product.

## 103. Focus Visibility
- The focus indicator must be visible at all times; prefer the browser default ring, and if restyling, verify it survives high-contrast / forced-colours modes (colour fills and gradients alone can vanish).
- Focus must always sit on a meaningful element, never fall back to `body`.
- Selected state and focused state must be visually distinct from each other, especially in multi-select widgets where they diverge.
- Do not hide the focus ring on mouse click by removing outlines globally; use `:focus-visible` to scope it [general].

## 104. Tab Sequence and `tabindex`
- Tab order follows reading order: finish one section before the next, avoid large backward jumps.
- Fix order by rearranging the DOM, not with `tabindex`; DOM order drives both tab order and screen reader reading order.
- `tabindex="0"` adds an element to the sequence in DOM order; `tabindex="-1"` removes it from the sequence but keeps it script-focusable.
- Positive `tabindex` values are strongly discouraged; they jump ahead of everything else and break predictability.
- On macOS, browsers by default tab only to form controls unless the user changes a setting; do not assume links are tab stops there.
- Avoid setting initial focus on page load unless the page has one primary task nearly every visitor starts immediately (e.g. a search page).

## 105. Where Focus Lands When Tabbing Into a Composite
- Grid and treegrid: the last-focused cell or row.
- Radio group, tabs, listbox, tree: the selected or checked item, or the first item if none.
- Menubar and toolbar: the first item on first entry; may return to the last-focused item afterwards.

## 106. Roving `tabindex`
- On load: `tabindex="0"` on the initial item, `tabindex="-1"` on all other items.
- On arrow-key move: set the current item to `-1`, set the target to `0`, call `focus()` on the target.
- When focus leaves, leave `tabindex="0"` on whichever item should receive focus on next entry.
- Advantage: real DOM focus means the browser scrolls the item into view automatically.
- Pointer clicks must update `tabindex` exactly as keyboard moves do, or the tab stop and visual state desync.

## 107. `aria-activedescendant`
- DOM focus stays on the container (the only tab stop); `aria-activedescendant` holds the `id` of the active child.
- Script must draw the visual focus indicator on the referenced child and scroll it into view, since the browser will not.
- The referenced element must be a DOM descendant of the container, listed in its `aria-owns`, or (for `combobox`, `textbox`, `searchbox`) inside the element named by `aria-controls`.
- Use it only on roles that support it; preferred where DOM focus must remain in a text input (combobox popups).
- Pointer interactions must update the attribute the same way keyboard navigation does.

## 108. Focus vs Selection
- Focus is a single point (`document.activeElement`); selection is a state (`aria-selected="true"`) that persists when focus leaves.
- Selection may follow focus only in single-select composites whose result displays instantly (tablists, single-select listboxes).
- Never use selection-follows-focus when moving focus triggers slow work (network fetch, page reload); require `Enter` or `Space` instead.
- In multi-select widgets, arrows move focus only; separate keys (`Space`, `Shift`+arrows, `Ctrl`+`A`) change selection.

## 109. Disabled Elements
- Native `disabled` removes a control from the tab sequence; `aria-disabled="true"` keeps it focusable and discoverable.
- Use native `disabled` when presence is obvious from neighbours (a disabled "Up" next to an enabled "Down").
- Use `aria-disabled="true"` when discoverability matters: menu items, tabs, listbox options, tree items, toolbar commands such as Cut/Copy/Paste.
- Skipping disabled items saves keystrokes, but screen reader users often learn what exists by moving focus; offset with shortcuts if skipping.

## 110. Trapping and Returning Focus
- Trap focus only in modal contexts (modal dialog, alert dialog): `Tab` wraps from last to first, `Shift`+`Tab` from first to last, `Escape` closes.
- Opening a popup or dialog moves focus into it; closing returns focus to the invoking control.
- If the invoker no longer exists (item deleted, page removed), move focus to the next logical element in the workflow, never to `body`.
- When the completed task leads directly to a next step, focus may move there instead (e.g. first cell of newly added rows).
- Non-modal popups (menus, tooltips, combobox listboxes) do not trap; `Tab` leaves and closes them.
- Live announcements (alerts, status) must never move focus.

## 111. Standard Key Assignments
- Context menu: `Shift`+`F10` (Windows/Linux).
- Copy `Ctrl`+`C` / `Cmd`+`C`; Paste `Ctrl`+`V` / `Cmd`+`V`; Cut `Ctrl`+`X` / `Cmd`+`X`.
- Undo `Ctrl`+`Z` / `Cmd`+`Z`; Redo `Ctrl`+`Y` on Windows/Linux, `Cmd`+`Shift`+`Z` on macOS.
- Use the macOS assignments on macOS rather than mapping `Ctrl` literally.
- Never intercept platform text-editing keys inside editable fields; rely on native browser editing.

## 112. Keyboard Shortcuts
- Shortcuts supplement standard navigation, never replace it; every shortcut target must also be reachable by `Tab`/arrows.
- Show the shortcut on or next to the element it triggers so it is discoverable.
- Choose behaviour deliberately: navigation (moves focus), activation (acts without moving focus, so screen reader users hear the result), or both (for single-purpose targets like a button that opens a dialog).
- Fix layout and command structure before adding shortcuts; many shortcuts raise cognitive load.
- Prefer mnemonics (`Ctrl`+`S` = Save) and familiar desktop conventions; consider localisation.
- Avoid OS conflicts: any modifier with `Tab`, `Enter`, `Space`, `Escape`; `Meta`+any key; `Alt`+function keys.
- Avoid assistive technology conflicts: `Caps Lock`+key, `Insert`+key, `Scroll Lock`+key, macOS `Control`+`Option`+key.
- Avoid browser conflicts (address bar, refresh, bookmarks, history, find); override only when the app function is frequent, the browser function is rare, and an alternate path to it exists.

# Part 16 — Component Interaction Patterns

## 113. Accordion
- What: a vertically stacked set of headings, each revealing or hiding a section; use to cut scrolling on pages with many sections. For a single show/hide, use a Disclosure instead [general].
- Keys: `Enter` / `Space` on a collapsed header expands it (and collapses the open one if only one may be open); on an expanded header collapses it if collapsing is supported.
- Keys: `Tab` / `Shift`+`Tab` move through all focusable elements in the accordion as part of normal page order; arrow keys between headers are not required.
- Focus: stays on the header button when toggling.
- ARIA: header text inside a `button`, wrapped in a `heading` with an appropriate `aria-level` (or native `h2`–`h6`); `aria-expanded` `true`/`false`; `aria-controls` points to the panel.
- ARIA: if the open panel cannot be collapsed, set `aria-disabled="true"` on its button.
- Labelling: optional panel container with `role="region"` and `aria-labelledby` pointing to its button.
- Pitfall: the button must be the only element inside the heading; put action menus or snippets outside it.
- Pitfall: avoid `region` panels when more than about six can be open at once; it causes landmark proliferation.

## 114. Alert
- What: a brief, important message that gets attention without interrupting the task; use Alert Dialog when the user must respond.
- Keys: none.
- Focus: must never move or change keyboard focus.
- ARIA: `role="alert"` on the container, rendered dynamically.
- Pitfall: alerts present at page load are not announced; inject them after load.
- Pitfall: do not auto-dismiss alerts; users who are slow to read or using AT may miss them.
- Pitfall: limit frequency; repeated interruptions harm users with visual and cognitive disabilities.

## 115. Alert Dialog
- What: a modal dialog that interrupts to deliver an urgent message and get a response; use for confirmations of destructive actions and error acknowledgements.
- Keys: same as modal dialog (`Tab`/`Shift`+`Tab` wrap inside, `Escape` closes).
- Focus: moves into the dialog on open; for irreversible actions focus the least destructive button (e.g. Cancel); return focus to the invoker on close.
- ARIA: `role="alertdialog"` on the container holding message and buttons; `aria-modal="true"`.
- Labelling: `aria-labelledby` to a visible title, else `aria-label`; `aria-describedby` points to the alert message text.
- Pitfall: set `aria-modal="true"` only when outside content is truly blocked and visually obscured.

## 116. Breadcrumb
- What: a horizontal list of links to the current page's ancestors in hierarchical order, usually placed before main content.
- Keys: none beyond normal link behaviour.
- ARIA: wrap in a `navigation` landmark (`nav`); current page link has `aria-current="page"` (optional if the current item is not a link).
- Labelling: label the `nav` with `aria-label` or `aria-labelledby` (e.g. "Breadcrumb").
- Pitfall: visual separators between items should be decorative (CSS or `aria-hidden`), not announced text [general].

## 117. Button
- What: triggers an action (submit, open dialog, cancel, delete); variants are toggle buttons and menu buttons. Use a link instead when it navigates.
- Keys: `Space` and `Enter` activate.
- Focus after opening a dialog: moves into the dialog.
- Focus after closing a dialog: returns to the invoker unless the action logically leads elsewhere.
- Focus after an in-place action (Apply, Recalculate): stays on the button.
- Focus after a context change (next wizard step): moves to the start of the new context.
- Focus after a shortcut-key activation: stays in the current context.
- ARIA: `role="button"` (prefer native `button`); `aria-disabled="true"` when unavailable; toggle uses `aria-pressed` `true`/`false`; menu button uses `aria-haspopup="menu"`.
- Labelling: name from text content, or `aria-labelledby` / `aria-label`; extra help via `aria-describedby`.
- Labelling: append an ellipsis ("Save as…") when the button opens a dialog.
- Pitfall: a toggle's label must not change with state ("Mute" stays "Mute" with `aria-pressed`); if the label does change ("Mute"/"Unmute"), drop `aria-pressed`.
- Pitfall: match visual style to function; an element styled as a link but performing an action should be restyled as a button, not just given `role="button"`.

## 118. Carousel
- What: a set of slides shown one at a time with previous/next controls and optional auto-rotation. Styles: basic, tabbed (slide pickers as one tab stop), grouped (one button per slide).
- Keys: `Tab` / `Shift`+`Tab` through controls; buttons follow the Button pattern; tabbed pickers follow the Tabs pattern.
- Focus: if auto-rotating, the rotation control must be first in the carousel's tab sequence.
- Focus: rotation stops when any element in the carousel gets keyboard focus or the pointer hovers, and does not resume until the user activates the rotation control.
- Focus: activating rotate / previous / next does not move focus, so users can press repeatedly.
- ARIA: container `region` or `group` with `aria-roledescription="carousel"`; each slide `group` with `aria-roledescription="slide"` (or `tabpanel` in the tabbed style).
- ARIA: optional slide wrapper live region with `aria-atomic="false"`, `aria-live="off"` while rotating and `"polite"` when stopped.
- ARIA: rotation control changes its label ("Stop slide rotation" / "Start slide rotation") and has no `aria-pressed`.
- ARIA: in the grouped style, the current slide's picker button uses `aria-disabled="true"` (not `disabled`) so it stays tabbable.
- Labelling: label the container; label each slide without the word "slide"; fall back to "3 of 10" only when no unique names exist.
- Pitfall: uncontrollable auto-rotation disorients screen reader users; grouped pickers add one tab stop per slide and are the least keyboard-friendly style.
- Pitfall: hidden slides must be properly hidden, not just positioned off-screen.

## 119. Checkbox
- What: dual-state (checked / not checked) or tri-state (adds partially checked); tri-state parents summarise a group of child options.
- Keys: `Space` toggles; `Enter` is not the standard toggle key for checkboxes.
- ARIA: `role="checkbox"`; `aria-checked` `true` / `false` / `mixed` (mixed only for tri-state).
- ARIA: a labelled set of checkboxes goes in a `group` with `aria-labelledby` (or a `fieldset`/`legend`).
- Labelling: visible text content, `aria-labelledby`, or `aria-label`; static help via `aria-describedby`.
- Behaviour: activating a tri-state parent checks or unchecks all children; optionally a third activation restores the prior partial selection.

## 120. Combobox
- What: an input with a popup (`listbox`, `grid`, `tree`, or `dialog`) for choosing a value; select-only (no typing) or editable (free or restricted text with filtered suggestions).
- When: value comes from a set, or free text benefits from suggestions; unlike a menu button it shows the value in a field and supports `aria-required`.
- Autocomplete types: none (static suggestions); list with manual selection; list with automatic selection (first match highlighted and accepted on blur); list with inline completion (completion text after the caret).
- Keys in input: `Down Arrow` opens and moves into the popup; `Up Arrow` (optional) moves to the last item; `Escape` closes, and optionally clears if already closed; `Enter` accepts a selected suggestion.
- Keys in input: `Alt`+`Down Arrow` (optional) opens without moving focus; `Alt`+`Up Arrow` (optional) returns to the input and closes.
- Keys in input: printable characters type (editable) or jump to a matching value (select-only); never intercept standard text-editing keys.
- Keys in listbox popup: `Down` / `Up Arrow` move and select; `Enter` accepts and closes; `Escape` closes and returns to the input; `Left` / `Right Arrow`, `Home`, `End`, `Backspace`, `Delete`, and typing return to the input in editable comboboxes.
- Keys in grid popup: arrows move by cell; `Page Up` / `Page Down`, `Home` / `End`, `Ctrl`+`Home` / `Ctrl`+`End` optional.
- Keys in tree popup: `Right Arrow` opens or moves to child; `Left Arrow` closes or moves to parent; `Up` / `Down` move without expanding.
- Keys in dialog popup: follow modal dialog rules; an action sets the value, or `Escape` / Cancel returns focus without changing it.
- Focus: only the input is in the tab sequence; the popup, its indicator button and descendants are excluded.
- Focus: for listbox / grid / tree popups DOM focus stays in the input and `aria-activedescendant` tracks the active option; dialog popups receive real DOM focus.
- ARIA: `role="combobox"` on the input; `aria-expanded` `true`/`false`; `aria-controls` points to the popup; `aria-haspopup` required for `grid`, `tree`, `dialog` (implicit `listbox`).
- ARIA: `aria-autocomplete` `none` / `list` / `both`; `aria-selected="true"` on the option representing the value; use `aria-controls`, not legacy `aria-owns`.
- Labelling: native `label` for `input`; else `aria-labelledby` to visible text; else `aria-label`.
- Pitfall: in popups selection follows focus and only one value can be selected; use a different pattern for multi-select.

## 121. Dialog (Modal)
- What: a window overlaid on the page whose underlying content is inert; use Alert Dialog for brief urgent messages and non-modal dialogs when the page must stay usable.
- Keys: `Tab` moves to next tabbable element inside, wrapping from last to first; `Shift`+`Tab` wraps from first to last; `Escape` closes.
- Initial focus default: the first focusable element.
- Initial focus for structured or long content: a static element at the top (title or first paragraph) made focusable with `tabindex="-1"`, so the start does not scroll out of view.
- Initial focus for an irreversible final step: the least destructive action.
- Initial focus for informational / continue-only dialogs: the most likely action ("OK", "Continue").
- Focus on close: return to the invoker; if gone, to the next logical element; or to the next step when reopening is unlikely.
- ARIA: `role="dialog"` with all operable elements as descendants; `aria-modal="true"`.
- Labelling: `aria-labelledby` to a visible title, else `aria-label`; `aria-describedby` only for simple, unstructured descriptive text.
- Pitfall: set `aria-modal="true"` only when script blocks all outside interaction and styling obscures outside content.
- Pitfall: always include a visible close or cancel button; never rely on `Escape` alone.
- Pitfall: avoid positive `tabindex` inside the dialog.

## 122. Disclosure
- What: a button that shows or hides a single section of content (FAQ answer, image description, simple nav dropdown, card details).
- Keys: `Enter` and `Space` toggle.
- Focus: stays on the button.
- ARIA: `role="button"`; `aria-expanded` `true`/`false`; optional `aria-controls` to the content.
- Visual: collapsed shows a right-pointing triangle; expanded points down.
- Pitfall: for site navigation dropdowns a disclosure is usually more appropriate than an ARIA menu [general].

## 123. Feed
- What: a scrolling section of `article`s that loads more content as the user reads (infinite scroll); a document structure, not a widget, so screen readers stay in reading mode.
- Keys (recommended, document them): `Page Down` next article; `Page Up` previous article; `Ctrl`+`End` first focusable element after the feed; `Ctrl`+`Home` first focusable element before the feed.
- Focus: page code scrolls and loads or removes articles based on which article has focus.
- Focus: nested feeds can be entered with `Tab` or a dedicated key such as `Alt`+`Page Down`.
- ARIA: `role="feed"` container; each item `role="article"`; all content must be inside an article.
- ARIA: `aria-posinset` on each article; `aria-setsize` with loaded count, total, or `-1` if unknown.
- ARIA: set `aria-busy="true"` on the feed while adding or removing articles, and always reset it to `false` afterwards.
- Labelling: feed via `aria-labelledby` or `aria-label`; each article via `aria-labelledby` to its title, with `aria-describedby` to its main content strongly recommended.
- Pitfall: widgets inside an article that use the same keys take priority; users must move off them to resume feed navigation.

## 124. Grid
- What: a composite that navigates with directional keys and has one tab stop. Data grids present interactive or editable tabular data; layout grids group widgets (links, buttons) to reduce tab stops.
- When not: use a static Table for read-only data with no interactive cells.
- Data grid keys: arrows move one cell, stopping at edges; `Page Up` / `Page Down` move by an author-defined number of rows; `Home` / `End` first or last cell in row; `Ctrl`+`Home` / `Ctrl`+`End` first cell of grid / last cell of grid.
- Selection keys: `Ctrl`+`Space` select column; `Shift`+`Space` select row; `Ctrl`+`A` select all; `Shift`+arrows extend selection.
- Layout grid keys: arrows with optional wrapping between rows or columns; `Page Up`/`Page Down`, `Ctrl`+`Home`/`End` optional; selection rarely supported.
- Cell content: prefer one widget that does not need arrow keys (focus the widget) or plain text/graphic (focus the cell).
- Edit mode: `Enter` or `F2` enters edit / widget mode and disables grid navigation; typing a character in an editable cell starts editing.
- Edit mode: `Escape` restores grid navigation (may undo edits); `F2` again also restores; `Tab` / `Shift`+`Tab` move between widgets in the grid.
- Focus: re-entering the grid returns to the last-focused cell.
- ARIA: `role="grid"`; `row`; `columnheader` / `rowheader` / `gridcell`; `aria-sort` on sorted header; `aria-selected` on selected cells or rows; `aria-readonly` on non-editable cells or the whole grid.
- ARIA: when not all data is in the DOM, use `aria-rowcount` / `aria-colcount` and `aria-rowindex` / `aria-colindex`.
- Labelling: `aria-labelledby` to visible label, else `aria-label`; `aria-describedby` to caption.
- Pitfall: make every cell focusable; non-focusable content is missed in screen reader application mode.
- Pitfall: wrapping helps layout grids but disorients users in data grids.
- Pitfall: arrow-key widgets (listbox, slider, radio group) inside cells conflict with navigation; gate them behind `Enter`/`F2`.
- Pitfall: on an HTML `table` with `role="grid"`, do not add row or cell roles and use native `rowspan`/`colspan`.
- Pitfall: with lazy-loaded rows, `Ctrl`+`End` may reach only the last DOM row, not the last data row.

## 125. Link
- What: an interactive reference to a resource; navigates rather than performs an action.
- Keys: `Enter` activates and moves to the target; `Shift`+`F10` (optional) opens a context menu.
- ARIA: `role="link"` only when native `a href` is impossible.
- Pitfall: the `link` role adds no browser behaviour; you must script `Enter` activation and context-menu support. Use native `a` with `href`.
- Pitfall: `Space` does not activate links (it scrolls); do not make links that require it [general].

## 126. Listbox
- What: a list of options for single or multiple selection; option names are flat strings, so use a Grid if options need interactive content.
- Design: keep option names short and distinct at the start; avoid repeated prefixes (split into two listboxes instead).
- Focus on entry (single-select): the selected option, else the first option (auto-select optional).
- Focus on entry (multi-select): the first selected option, else the first option without selecting it.
- Keys: `Down` / `Up Arrow` move focus (selection may follow in single-select); `Home` / `End` optional but strongly recommended over five options.
- Keys: type-ahead recommended, especially over seven options; typing jumps to the next option starting with the typed string.
- Multi-select recommended model: `Space` toggles; `Shift`+`Down`/`Up` move and toggle; `Shift`+`Space` select range; `Ctrl`+`Shift`+`Home`/`End` select to start/end; `Ctrl`+`A` select all.
- Multi-select alternative model: moving without modifier clears other selections; `Shift`+arrows move and toggle; `Ctrl`+arrows move without changing selection; `Ctrl`+`Space` toggles.
- Horizontal: `Right` / `Left Arrow` replace `Down` / `Up` and set `aria-orientation="horizontal"`.
- ARIA: `role="listbox"`, `role="option"`, optional labelled `group`s; `aria-multiselectable="true"` for multi-select.
- ARIA: use either `aria-selected` or `aria-checked` on options, never both; at most one selected in single-select; set `aria-setsize` / `aria-posinset` when lazy-loading.
- Labelling: standalone listbox needs `aria-labelledby` to a visible label, or `aria-label`.
- Pitfall: selection-follows-focus can seriously harm usability when selection triggers effects; provide explicit "Select all" / "Unselect all" buttons where bulk selection matters.

## 127. Menu and Menubar
- What: a menu is a list of actions or functions behaving like an OS menu, opened from a menu button, a parent item, or a context command (`Shift`+`F10`); a menubar is a persistent, usually horizontal menu.
- When not: for ordinary site navigation links, a disclosure-style nav is usually simpler and expected [general].
- Focus: opening a menu or entering a menubar focuses the first item; `Tab` / `Shift`+`Tab` do not move between items, they leave and close all menus.
- Keys: `Enter` opens a submenu (focus first item) or activates the item and closes the menu.
- Keys: `Space` (optional) toggles `menuitemcheckbox` or checks `menuitemradio` without closing; otherwise activates.
- Keys in menu: `Down` / `Up Arrow` next / previous item (wrap optional); `Right Arrow` opens a submenu, or in a menubar submenu moves to the next menubar item; `Left Arrow` closes a submenu returning to parent, or moves to the previous menubar item.
- Keys in menubar: `Right` / `Left Arrow` move between items; `Down Arrow` opens a submenu at its first item; `Up Arrow` (optional) opens at its last item.
- Keys: `Home` / `End` first / last item; printable character (optional) jumps to next item starting with it.
- Keys: `Escape` closes the current menu and returns focus to its invoker (menu button or parent item).
- Behaviour: disabled items are focusable but not activatable; separators are not focusable.
- ARIA: `menu` / `menubar`; `menuitem`, `menuitemcheckbox`, `menuitemradio`; parent items `aria-haspopup="menu"` and `aria-expanded`; checked items `aria-checked="true"`; disabled `aria-disabled="true"`.
- ARIA: focus via `aria-activedescendant` on the container, or roving `tabindex` (`-1` on items, `0` on the first menubar item).
- ARIA: group radio items with `separator`; set `aria-orientation` when it differs from defaults (menubar horizontal, menu vertical).
- Labelling: menubar via `aria-labelledby` or `aria-label`; menu via `aria-labelledby` to its controlling button or item, or `aria-label`.
- Labelling: append an ellipsis to items that open dialogs.
- Pitfall: avoid items that both perform an action and open a submenu; if unavoidable, `Enter`/`Space` act and `Down Arrow` opens.

## 128. Menu Button
- What: a button that opens a menu, usually shown with a down-pointing arrow.
- Keys: `Enter` and `Space` open the menu and focus the first item; `Down Arrow` (optional) opens at the first item; `Up Arrow` (optional) opens at the last item.
- Focus on close: `Escape` or activating an item returns focus to the button (per the Menu pattern).
- ARIA: `role="button"` with `aria-haspopup="menu"` (or `true`) and `aria-expanded` `true`/`false`; popup has `role="menu"`; optional `aria-controls`.
- Pitfall: use a combobox, not a menu button, when the user is picking a form value that must be shown or marked required.

## 129. Meter
- What: a graphical display of a numeric value within a known range (battery, fuel, disk usage).
- When not: values without a meaningful maximum; progress of a task or loading (use `progressbar`).
- Keys: none; not interactive.
- ARIA: `role="meter"`; `aria-valuenow` within `aria-valuemin` and `aria-valuemax`; `aria-valuetext` when a percentage alone is unclear (e.g. "50% (6 hours) remaining").
- Labelling: `aria-labelledby` to a visible label, else `aria-label`.
- Pitfall: AT often announces the value as a percentage; supply `aria-valuetext` for meaningful units.

## 130. Radio Group
- What: a set of checkable buttons where at most one is checked; may start with none checked to force a deliberate choice.
- Keys (standalone): `Tab` / `Shift`+`Tab` enter and leave the group; `Space` checks the focused radio; `Right`/`Down Arrow` move to and check the next radio, wrapping; `Left`/`Up Arrow` move to and check the previous, wrapping.
- Keys (in a toolbar): arrows move focus without changing the checked radio; `Space` (and optional `Enter`) checks; arrows at the group edge move on to adjacent toolbar items.
- Focus: entering the group lands on the checked radio, else the first.
- ARIA: `role="radiogroup"` containing `role="radio"` items; `aria-checked` `true`/`false`.
- Labelling: group via `aria-labelledby` or `aria-label`; each radio via content, `aria-labelledby`, or `aria-label`; extra help via `aria-describedby`.
- Pitfall: native browser behaviour with no selection can differ (some focus the last radio on `Shift`+`Tab`).
- Pitfall: arrow keys check as they move; do not use radios where checking triggers expensive side effects [general].

## 131. Slider
- What: picks a value within a range by moving a thumb along a track.
- Keys (required): `Right`/`Up Arrow` increase one step; `Left`/`Down Arrow` decrease one step; `Home` minimum; `End` maximum.
- Keys (optional): `Page Up` / `Page Down` change by a larger step.
- Focus: on the thumb element itself.
- ARIA: `role="slider"`; `aria-valuenow`, `aria-valuemin`, `aria-valuemax`; `aria-valuetext` when numbers are not meaningful (units, day names, mm:ss); `aria-orientation="vertical"` for vertical sliders.
- Labelling: `aria-labelledby` to a visible label, else `aria-label`.
- Pitfall: touch-based AT may not support custom sliders; test on touch devices. Reversing arrow direction can be acceptable where it is more intuitive.

## 132. Slider (Multi-Thumb)
- What: two or more thumbs on one rail setting related values, e.g. a price range.
- Keys: each thumb supports all single-slider keys.
- Focus: each thumb is its own tab stop; tab order stays fixed regardless of thumb values or visual positions.
- ARIA: each thumb `role="slider"` with its own value attributes; when thumbs cannot cross, update the dependent thumb's `aria-valuemin` / `aria-valuemax` whenever the other changes.
- Labelling: each thumb needs a distinct accessible name (e.g. "Minimum price", "Maximum price").
- Pitfall: same touch-AT support caveat as the single slider.

## 133. Spinbutton
- What: an input restricted to a discrete set or range (minutes 0–59), typically a text field with increment and decrement buttons.
- Keys (required): `Up Arrow` increase; `Down Arrow` decrease; `Home` set to minimum (if one exists); `End` set to maximum (if one exists).
- Keys (optional): `Page Up` / `Page Down` larger steps.
- Keys: direct editing supports standard single-line text-editing keys and printable characters.
- Focus: stays in the text field; the increment / decrement buttons are usually not tab stops.
- ARIA: `role="spinbutton"`; `aria-valuenow` required; `aria-valuemin` / `aria-valuemax` when known; `aria-valuetext` for friendly text; `aria-invalid="true"` when out of range.
- Labelling: `aria-labelledby` to visible label, else `aria-label`.
- Pitfall: never capture text-editing keys in script.

## 134. Switch
- What: a binary on/off control with no mixed state; choose switch vs checkbox vs toggle button by visual design and semantics ("on/off" vs "checked").
- Keys: `Space` toggles (required); `Enter` toggles (optional).
- ARIA: `role="switch"` with `aria-checked` `true`/`false`; for native `input type="checkbox"` use `checked` instead.
- ARIA: group switches in `role="group"` with `aria-labelledby`, or `fieldset` with `legend`; help text via `aria-describedby`.
- Labelling: visible content, `aria-labelledby`, or `aria-label`.
- Pitfall: the label must not change when the state changes.

## 135. Table
- What: a static, non-interactive structure of rows and cells; cells are not focusable or selectable.
- When not: use a Grid when the content is interactive or contains many widgets (a grid collapses many tab stops into one).
- Keys: none; not a widget.
- ARIA: prefer native `table`; otherwise `role="table"`, `row`, `columnheader`, `rowheader`, `cell`; `aria-rowcount` / `aria-colcount` and indexes when content is virtualised; `aria-rowspan` / `aria-colspan` for spans.
- Sorting: `aria-sort` on the sorted column or row header.
- Labelling: `aria-labelledby` to a visible title, else `aria-label`; `aria-describedby` to a caption or description.
- Pitfall: elements added via `aria-owns` are read after DOM children.

## 136. Tabs
- What: layered panels showing one at a time, each activated by its tab; the tab list usually sits above the panel.
- Activation: automatic (panel shows on focus) only when panels render instantly; otherwise manual (`Enter`/`Space` to show).
- Keys: `Tab` enters the tablist on the active tab; `Tab` from the tablist goes to the panel (or its first focusable element).
- Keys: `Left` / `Right Arrow` move between tabs with wrapping (activation optional); `Space` / `Enter` activate if not automatic.
- Keys (optional): `Home` / `End` first / last tab; `Delete` closes a deletable tab, moving focus to the next tab, else the previous.
- Keys: `Shift`+`F10` opens a tab's popup menu if one exists.
- Vertical: `Up` / `Down Arrow` replace `Left` / `Right`; set `aria-orientation="vertical"`.
- Focus: horizontal tablists leave `Up`/`Down Arrow` to the browser for scrolling.
- Focus: panels with no focusable first content get `tabindex="0"` so they are reachable.
- ARIA: `tablist`, `tab`, `tabpanel`; `aria-selected="true"` on the active tab, `false` on others; each tab `aria-controls` its panel; each panel `aria-labelledby` its tab; `aria-haspopup` on tabs with menus.
- Labelling: `tablist` via `aria-labelledby` or `aria-label`.
- Pitfall: automatic activation with slow-loading panels makes keyboard navigation painfully slow.
- Pitfall: do not use tabs for site navigation between pages; use links in a `nav` [general].

## 137. Toolbar
- What: a container grouping related controls (buttons, menu buttons, checkboxes); use only with three or more controls.
- Keys: `Tab` / `Shift`+`Tab` enter and leave (single tab stop); first entry focuses the first enabled control, later entries may restore the last focused.
- Keys: horizontal `Left` / `Right Arrow` move (wrap optional); vertical uses `Up` / `Down Arrow`; `Home` / `End` optional.
- Focus: disabled controls are typically skipped; keep them focusable where discoverability matters.
- ARIA: `role="toolbar"`; `aria-orientation="vertical"` when vertical.
- Labelling: `aria-labelledby` to a visible label, else `aria-label`.
- Pitfall: avoid controls that need the same arrow keys as toolbar navigation; if unavoidable, include only one and place it last (e.g. a textbox at the end).
- Pitfall: when users must reach the toolbar quickly (e.g. from an editor), provide and document a shortcut.

## 138. Tooltip
- What: a popup describing an element, shown on keyboard focus or hover after a short delay.
- When not: never for content containing focusable or interactive elements; use a non-modal dialog.
- Keys: `Escape` dismisses.
- Focus: stays on the trigger; tooltips never take focus. A focus-triggered tooltip closes on blur.
- Hover: stays open while the pointer is over the trigger or the tooltip; closes on mouse out.
- ARIA: `role="tooltip"`; trigger references it with `aria-describedby`.
- Pitfall: tooltips that appear only on hover exclude keyboard and touch users; essential information should not live only in a tooltip [general].

## 139. Tree View
- What: a hierarchical list with expandable / collapsible parents (file navigators); single- or multi-select.
- Focus on entry (single-select): the selected node, else the first node.
- Focus on entry (multi-select): the first selected node, else the first node.
- Keys: `Right Arrow` opens a closed node / moves to first child of an open node / does nothing on an end node.
- Keys: `Left Arrow` closes an open node / moves to parent from a child / does nothing on a closed root.
- Keys: `Down` / `Up Arrow` next / previous visible node without expanding or collapsing; `Home` / `End` first / last node.
- Keys: `Enter` performs the default action (often toggle, or select in single-select without selection-follows-focus).
- Keys: type-ahead recommended (especially over seven root nodes); `*` (optional) expands all siblings.
- Multi-select keys: same recommended and alternative models as Listbox (`Space`, `Shift`+arrows, `Shift`+`Space`, `Ctrl`+`Shift`+`Home`/`End`, `Ctrl`+`A`, or `Ctrl`+arrows / `Ctrl`+`Space`).
- Horizontal: `Down`/`Up Arrow` act as `Right`/`Left`; set `aria-orientation="horizontal"`.
- ARIA: `role="tree"`, `treeitem`, child `group`s; `aria-expanded` only on parent nodes (never on end nodes); `aria-multiselectable` for multi-select; `aria-selected` or `aria-checked` (not both).
- ARIA: with lazy-loaded nodes, set `aria-level`, `aria-setsize`, `aria-posinset`.
- Labelling: `aria-labelledby` to a visible label, else `aria-label`.
- Pitfall: selected and focused nodes must look different; provide "Select all" / "Unselect all" controls when bulk selection matters.

## 140. Treegrid
- What: a hierarchical data grid where rows can expand to reveal child rows (threaded email); both rows and cells are focusable.
- Focus on entry: first row or first cell, depending on whether row focus is supported.
- Keys: `Right Arrow` on a collapsed row expands it; on an expanded or leaf row moves to the first cell; in a cell moves right.
- Keys: `Left Arrow` on an expanded row collapses it; from the first cell moves to the row (if row focus supported); in other cells moves left.
- Keys: `Up` / `Down Arrow` move one row or cell; `Page Up` / `Page Down` by author-defined amount; `Home` / `End` first/last row (on a row) or first/last cell (in a cell); `Ctrl`+`Home` / `Ctrl`+`End` first/last row.
- Keys: `Enter` toggles expansion on the first cell of an expandable row (cell-only focus) or performs the cell's default action; `Tab` moves to the next focusable element in the row, then out of the treegrid.
- Selection keys: `Ctrl`+`Space`, `Shift`+`Space`, `Ctrl`+`A`, `Shift`+arrows as in Grid.
- ARIA: `role="treegrid"`, `row`, `columnheader` / `rowheader` / `gridcell`; `aria-expanded` on parent rows only; `aria-multiselectable`; `aria-selected` (single-select only on the selected item; multi-select `true`/`false` on all).
- ARIA: `aria-sort`, `aria-readonly`, `aria-rowcount` / `aria-colcount`, indexes, and spans as in Grid.
- Labelling: `aria-labelledby` or `aria-label`; caption via `aria-describedby`.
- Pitfall: never put `aria-expanded` on rows that cannot expand; in-cell controls needing arrows require the Grid edit-mode convention.

## 141. Window Splitter
- What: a movable separator resizing two panes; variable (any position in range) or fixed (toggles between two positions). Its value is the primary pane's size.
- Keys: `Left` / `Right Arrow` move a vertical splitter; `Up` / `Down Arrow` move a horizontal splitter (omitted for fixed splitters).
- Keys: `Enter` collapses the primary pane, or restores the previous position if collapsed.
- Keys (optional): `Home` minimum primary size (may collapse it); `End` maximum primary size; `F6` cycles between panes.
- Focus: the separator itself is focusable.
- ARIA: focusable `role="separator"`; `aria-valuenow`, `aria-valuemin` (typically `0`), `aria-valuemax` (typically `100`); `aria-controls` to the primary pane.
- Labelling: name matches the primary pane, via `aria-labelledby` to its visible label or `aria-label`.
- Pitfall: "primary" pane is about the value model, not importance; provide a keyboard collapse/restore, not only drag.

# Part 17 — Landmarks & Page Structure

## 142. Landmark Principles
- Landmarks identify major page sections so AT users can perceive structure and jump between sections.
- Put all perceivable content inside a landmark so nothing is missed by landmark navigation.
- Derive landmarks from the visual design: areas separated by alignment and spacing become regions; subdivide only where the design subdivides (e.g. portlets).
- Keep the count low; a rule of thumb is seven or fewer landmarks per page, since value drops as they multiply.
- `banner`, `main`, `complementary`, and `contentinfo` should be top-level, not nested inside other landmarks.
- Do not wrap modal dialog content in a landmark; the dialog already supplies a name and boundaries.

## 143. Landmark Labelling
- When a role appears more than once, give each instance a unique label.
- Exception: identical content with identical purpose (pagination repeated above and below a table) shares one label.
- A role used once usually needs no label.
- If the area starts with a heading, label with `aria-labelledby` pointing to it; otherwise `aria-label`.
- Do not include the role name in the label: "Site", not "Site navigation", because AT already announces "navigation".

## 144. Banner
- HTML `header` in `body` context, or `role="banner"`.
- Site-level content at the top of each page: logo, identity, site search; typically full width.
- One per page; a `header` inside `article`, `aside`, `main`, `nav`, or `section` is not a banner.

## 145. Main
- HTML `main`, or `role="main"`.
- The page's primary content; one per page (per document or application frame); top-level.
- Pair with a "Skip to main content" link as the first focusable element [general].

## 146. Navigation
- HTML `nav`, or `role="navigation"`.
- Groups of links for site or page navigation; label each when there are several; navigations with the same links share the same label.

## 147. Complementary
- HTML `aside`, or `role="complementary"`.
- Supporting content that remains meaningful when separated from main; top-level; label each if several.
- Content unrelated to main belongs in a more general `region`.

## 148. Contentinfo
- HTML `footer` in `body` context, or `role="contentinfo"`.
- Page-bottom information: copyright, privacy and accessibility statement links; one per page.
- A `footer` inside `article`, `aside`, `main`, `nav`, or `section` is not contentinfo.

## 149. Search
- HTML `search`, or `role="search"`.
- Wraps the full set of controls forming search; use instead of `form` for search.

## 150. Form
- HTML `form` with an accessible name (`aria-labelledby`, `aria-label`, or `title`), or `role="form"`.
- Use only when no more specific landmark (`main`, `search`) fits; label visibly, e.g. with a heading.
- Mark the whole form region, not individual fields; prefer native `button`, `input`, `select`, `textarea`.

## 151. Region
- HTML `section` with an accessible name, or `role="region"`.
- Important sections users should be able to jump to that no named landmark describes.
- Must always have a label; an unlabelled `section` is not a landmark.

## 152. Headings and Structure
- Use a logical heading hierarchy (`h1`–`h6`) inside landmarks; headings and landmarks complement each other for navigation [general].
- Accordion and carousel containers should not create extra landmarks when doing so would push the page past a manageable count.

# Part 18 — Gestures & Pointer Alternatives

## 153. Single-Pointer Alternative to Dragging
- Every function operated by dragging must also be operable with a single pointer using clicks or taps alone, with no press-hold-move (WCAG 2.5.7, Level AA).
- Dragging may be the only method only when it is essential, meaning removing it would fundamentally change the information or function.
- The alternative need not be the same component; equivalent functionality anywhere on the page is enough.
- A keyboard alternative alone does not satisfy this; the alternative must be clickable or tappable.
- The alternative must not itself depend on a path-based gesture such as a swipe or flick (WCAG 2.5.1).
- Browser-owned gestures (scrollbar dragging, touch scrolling, pull-to-refresh, native `overflow` scrolling) are out of scope, but custom scroll mechanisms that override native scrolling are in scope.
- Remember who benefits: people with tremor or limited grip, and users of trackballs, head pointers, eye-gaze and speech-driven mouse emulation.

## 154. Drag Alternative Patterns
- Maps: provide pan buttons (up, down, left, right) next to drag-to-pan.
- Sliders: let a click or tap on the track jump the thumb to that point.
- Sortable lists: after selecting an item, offer move up / move down controls.
- Kanban boards: offer a menu or arrow buttons to move a card to another column.
- Color wheels: allow clicking a point on the wheel and provide numeric input fields.
- Assignment by drop target: offer a menu to choose the destination or recipient.
- Selection rectangles: support click first corner, then click second corner.
- Matching or connecting lines: support click-then-click pairing.
- Carousels: provide previous and next buttons (visible, or visually hidden but pointer-operable).
- Text entry is a valid alternative, since touch users receive an on-screen keyboard.

## 155. Gesture Keyboard Parity
- All gestures (drag, swipe, pinch, path) need both a tap/click alternative and a keyboard alternative unless the gesture is essential.
- Flag gesture-only actions as an anti-pattern.

## 156. Drag-Time Hygiene
- While dragging, disable text selection so the drag does not highlight page text.
- Set `inert` on the dragged element during the drag so it does not capture hover, focus or hit-testing beneath the pointer.

## 157. Pointer-Adaptive Sizing
- Use `@media (pointer: coarse)` to enlarge buttons, checkboxes and links and add spacing between them; for example a `15px` checkbox for fine pointers becomes `30px` for coarse.
- Use `@media (pointer: fine)` to permit denser layouts when a precise mouse is the primary input.
- `pointer` tests only the primary input; use `any-pointer` for hybrid devices such as touchscreen laptops with trackpads.
- `pointer: none` means the primary input has no pointing device; design for keyboard or other inputs.
- Do not rely on hover-only interactions on touch devices.

## 158. Menu Prediction Cones
- [context] Keep a submenu open while the pointer travels diagonally from the parent item toward it, instead of closing it as soon as the pointer crosses a sibling item.
- [context] Model the safe zone as a triangle or cone from the pointer position to the submenu edges; only switch submenus when the pointer leaves that zone or stops moving.

## 159. Tooltip Timing
- [context] Delay the first tooltip in a group so incidental hovers do not trigger it.
- [context] Once one tooltip is open, show subsequent tooltips on peer elements instantly, with no delay and no entrance animation, while the pointer moves across the group.

## 160. Touch Responsiveness
- Set `touch-action: manipulation` to remove the double-tap-to-zoom delay.
- Set `-webkit-tap-highlight-color` deliberately rather than leaving the default flash.
- Use autofocus sparingly: desktop only, one primary input, never on mobile where it pops the keyboard.

# Part 19 — Motion That Users Can Stop

## 161. Pause, Stop, Hide for Moving Content
- Moving, blinking or scrolling content that starts automatically, lasts more than `5 s`, and appears alongside other content needs a way to pause, stop or hide it (WCAG 2.2.2, Level A).
- Alternatively, make it stop by itself within `5 s` of starting.
- "Starts automatically" includes indirect triggers such as hover, focus or scrolling into view.
- Applies to all content on the page, not just content used to meet other criteria.
- Exempt only when the motion is essential, meaning removing it changes the information or function and no conforming alternative exists.

## 162. Auto-Updating Content
- Auto-updating content that starts automatically and sits alongside other content needs a way to pause, stop, hide or control update frequency.
- There is no `5 s` grace period for auto-updating content.
- On resume, non-real-time content (videos, articles, slideshows) continues from the paused point.
- On resume, real-time content (stock tickers, radar, traffic cams, auction timers) jumps to the current state; missed updates need not be preserved.
- A good ticker pattern: pause holds the current item, resume notes the delay, and a "jump to latest" control is offered.

## 163. Control Mechanism Quality
- Prefer one control that pauses all moving or updating content over a separate control per element.
- The mechanism must not trap focus or block use of the page.
- Pausing only while focused and restarting on blur fails; the pause must persist.
- Provide a visible on-page control, or a link or button that reloads the page without the blinking content.

## 164. Blinking and Animated Images
- Blink for less than `5 s`, or stop script-driven blinking within `5 s`.
- Configure animated GIFs to stop after a fixed number of cycles completing within `5 s`.
- Never let non-essential scrolling content run with no pause and restart.

## 165. Flash Thresholds
- Never flash more than `3` times in any one-second period (WCAG 2.3.1); blinking at `3` or more per second counts as flashing.
- A general flash is a pair of opposing luminance changes of `10%` or more where the darker state is below relative luminance `0.80`; red flashes are judged separately.
- Flashes are tolerable only if the flashing area stays under `0.006` steradians within any `10°` visual field (about `25%` of it).

## 166. Loading and Standalone Exceptions
- A preload animation can be essential only if users cannot interact during loading and omitting progress would confuse them.
- Content shown alone with nothing else on the page (a mandatory full-screen ad, a lone loading screen) is exempt.
- Turn-based games can let one party pause without affecting fairness.

## 167. Reduced Motion
- Respect `prefers-reduced-motion` with a reduced variant or no animation.
- Stop muted decorative video loops under reduced motion and show a still frame instead.
- Animations must be interruptible by user input.

# Part 20 — Accessible Media

## 168. Captions
- Captions provide speech and the non-speech sounds needed to understand the content; subtitles are the same concept.
- Identify speakers (for example with WebVTT `<v Name>` voice tags).
- Omit background music that carries no information.
- Do not ship automatic captions unless reviewed; recognition errors can reverse meaning.
- Keep captions synchronized with the audio.
- Prerecorded video with audio requires captions (WCAG 1.2.2, Level A); live video with audio requires captions (1.2.4, Level AA).
- Expect users to restyle captions; player defaults are usually white text on a black box, and author positioning support is inconsistent.

## 169. Transcripts
- A transcript is a text version of speech and meaningful non-speech audio; prerecorded audio-only (podcasts) requires one (1.2.1, Level A).
- A descriptive transcript adds descriptions of essential visual information and is the only way to serve people who are both Deaf and blind.
- Add what captions omit: on-screen text, titles, speaker identification.
- Group lines into paragraphs, lists or sections; mark added clarifications with brackets or headings.
- Include timestamps only when helpful, coarser than caption cues, with no end times.
- Label speakers with hanging indents or bold names; consider a two-column audio/visual table.
- Place the transcript directly under the media or link to it from there; for your own media, keep it on the same page.

## 170. Interactive Transcripts
- Highlight text as it is spoken and let users select text to jump to that point in the media.
- Drive it from the same captions file to avoid drift.

## 171. Audio Description
- Describe visual information needed to understand the content: key actions, scenes, charts, and on-screen text such as speaker names, titles, links and email addresses.
- Write objectively, in present tense, active voice and third person; do not describe what is already clear from audio.
- Prefer integrated description, where speakers naturally narrate visuals in the main audio; plan it in the script before filming.
- Otherwise use a timed text description track, a separate description audio track, or an alternate described video, in that order of preference.
- Prerecorded video needs audio description or a descriptive transcript at Level A (1.2.3) and audio description at Level AA (1.2.5).
- Use extended description, which pauses video, when gaps are too short (1.2.7, Level AAA).

## 172. Sign Language
- Provide sign language when the audience needs it, for Deaf people whose first language is sign.

## 173. Accessible Media Players
- All player controls must be operable by keyboard with a visible focus indicator.
- Controls need clear labels and programmatic structure, and must work with speech input, zoom and screen readers.
- Text, controls and backgrounds need sufficient contrast, including non-text contrast for controls.
- Useful extras: adjustable playback speed, caption styling settings, captions output to screen readers or braille, and description track support.
- Keep background audio low so speech stays intelligible.
- Hide purely decorative media from assistive technology.

# Part 21 — Scroll & Overscroll Control

## 174. Scroll Chaining
- When a nested scroll container hits its boundary, the gesture passes to the nearest scrollable ancestor; this lets a dialog's scroll move the page behind it.
- Set `overscroll-behavior: contain` on modals, drawers, sheets and inner panels to stop background scroll.
- `contain` blocks chaining but may still bounce; `none` blocks both chaining and bounce; `chain` allows chaining but suppresses bounce; `auto` is the default.
- Use per-axis control (`overscroll-behavior: auto contain` or `overscroll-behavior-y`) for chat windows and similar layouts.
- An element with no scrollable overflow is always at its boundary, so `contain` or `none` on it still blocks chaining.
- Setting it on an `<iframe>` element has no effect; set it on the framed document's `<html>` and `<body>`.

## 175. Rubber-Banding and Pull-to-Refresh
- Suppress page-level rubber-banding on desktop with `overscroll-behavior: none` on `<html>` inside `@media (pointer: fine)`, which makes app-like interfaces feel solid.
- Keep coarse-pointer defaults so pull-to-refresh and native bounce still work on phones.
- Test hybrid touch devices, because `none` also disables scroll chaining and swipe-to-navigate.
- Keep headers and footers `position: fixed` or `sticky` so they stay aligned during elastic overscroll.

## 176. Focus and Anchor Visibility
- Sticky headers, footers and overlays must never cover the focused element.
- Give heading anchors `scroll-margin-top` so jumped-to headings clear a sticky header.

# Part 22 — Inert & Interaction Blocking

## 177. Inert Regions
- An inert subtree cannot be clicked, focused, edited, selected, or found with find-in-page, and is removed from the accessibility tree.
- Use `inert` for whole sections of content (background behind custom overlays, off-screen panels, content during a blocking operation).
- A `<dialog>` opened with `showModal()` escapes ancestor inertness automatically; no other element does.

## 178. Make Inertness Visible
- Browsers give no visual cue for inert content; add one, such as reduced opacity, a scrim, or a label.
- Consider zoomed users who may only see the inert part of the page and be confused why it does not respond.

## 179. Inert vs Disabled
- Use `disabled` with `:disabled` styling for a single control; reserve `inert` for regions.
- Keep submit buttons enabled until the request starts, then show a spinner, rather than pre-disabling them.

# Part 23 — Safe Areas

## 180. Safe-Area Insets
- Use `env(safe-area-inset-top|right|bottom|left)` to keep content clear of notches, rounded corners, home indicators and dynamic toolbars in full-bleed layouts.
- Insets are `0` on rectangular viewports, so add them to a base value: `padding-bottom: calc(1em + env(safe-area-inset-bottom))`.
- Full-bleed layouts typically opt in with `viewport-fit=cover` in the viewport meta.
- Use `safe-area-max-inset-*` when you need the static maximum measured with all dynamic UI retracted.
- Sticky footers and bottom action bars are the most common place to apply the bottom inset.

## 181. Env Fallbacks
- Always supply a fallback as the second argument, e.g. `env(safe-area-inset-top, 20px)`; it can be another `env()`.
- Names are case-sensitive; a typo silently uses the fallback.
- An invalid substitution without a fallback makes the property take its initial or inherited value, not be ignored.

## 182. Other Device Regions
- In installed desktop apps using window-controls overlay, position headers with `env(titlebar-area-x|y|width|height)` to avoid window buttons.
- Use `keyboard-inset-*` to keep inputs and action bars above the on-screen keyboard.
- Use `viewport-segment-*` to avoid placing content across a fold or hinge.
- Prefer `<meta name="text-scale" content="scale">` over `env(preferred-text-scale)`; using both scales `em`/`rem` twice.

## 183. Layout Robustness
- Prefer flex and grid over JavaScript measurement.
- Fix the source of unwanted horizontal overflow rather than only hiding it with `overflow-x: hidden`.
- Never disable zoom with `user-scalable=no` or `maximum-scale=1`.

# Part 24 — Accessibility Tree

## 184. What Assistive Technology Sees
- Screen readers interact with the accessibility tree, a simplified model derived from the DOM where each node has a role and usually a name.
- Purely presentational nodes (styling `<div>`s) are dropped, so visual structure does not automatically become semantic structure.
- Shape the tree with semantic HTML first and ARIA second.

## 185. Verifying Roles and Names
- Inspect the accessibility tree to confirm important elements are not ignored and that their roles and names match intent.
- Give icon-only buttons an accessible name; give every form control a label.
- Mark decorative icons `aria-hidden="true"` and decorative images `alt=""`.
- Use `<button>` for actions and `<a>` for navigation so roles are correct and Cmd/Ctrl-click and middle-click work.
- Keep heading levels in order and provide a skip link to main content.
- Announce async updates such as toasts and validation with `aria-live="polite"`.

# Part 25 — Rendering Performance

## 186. Skipping Off-Screen Rendering
- Apply `content-visibility: auto` to chunked sections (feed items, long article sections, comments) so off-screen layout and paint are skipped.
- Focused or selected content is never skipped, and sections render as they approach the viewport.
- Typical gains: `50%` or more lower rendering cost on content-heavy pages (one demo dropped from `232ms` to `30ms`, about `7x`); also improves INP.
- Off-screen content stays in the DOM and accessibility tree, so find-in-page and navigation still work.

## 187. Placeholder Sizing
- Pair `content-visibility: auto` with `contain-intrinsic-size` so skipped sections do not collapse to `0` height.
- Use `contain-intrinsic-size: auto 300px` so the browser remembers the last rendered size and the scrollbar stops jumping.

## 188. Hidden but Cached Views
- Use `content-visibility: hidden` for inactive SPA views and tabs to keep rendering state cached while not painting; showing them again is fast (up to `250ms` faster back navigation reported).
- It sits between `display: none` (destroys rendering state) and `visibility: hidden` (keeps space and hit-testing).
- Avoid DOM APIs that force layout inside skipped subtrees, or the savings vanish.

## 189. Layout Thrash and Input Cost
- Do not read layout (`getBoundingClientRect`, `offsetHeight`, `offsetWidth`, `scrollTop`) during render.
- Batch DOM reads and writes rather than interleaving them.
- Prefer uncontrolled inputs; controlled inputs must be cheap per keystroke.
- Animate only `transform` and `opacity`, and never use `transition: all`.

## 190. Unnecessary Re-Renders
- Visualize which components re-render on each interaction and target the ones that re-render without changed output.
- Memoize expensive subtrees and stabilize props and callbacks so unrelated state changes do not cascade.

## 191. Loading Priorities
- Give every `<img>` explicit `width` and `height` to prevent layout shift.
- Lazy-load below-the-fold images; mark the above-the-fold hero with `fetchpriority="high"`.
- `preconnect` to CDN and asset origins; preload critical fonts with `font-display: swap`.

# Part 26 — Animated Media Delivery

## 192. Video Instead of GIF
- Replace animated GIFs with video; GIFs cost up to `12x` the bandwidth and `2x` the energy of modern codecs (example: `3.7 MB` GIF to `551 KB` MP4 and `341 KB` WebM).
- Use `<video autoplay loop muted playsinline>` to mimic GIF behavior; drop `loop` if it should not repeat.
- Offer WebM first and MP4 second; browsers take the first supported source, not the best.
- Omit `poster` when replacing a GIF; poster-less videos are not LCP candidates, which usually improves LCP.
- Encode H.264 MP4 at even pixel dimensions.

## 193. Short Loops via Picture
- For short non-essential loops, Safari can play an H.264 MP4 through `<picture><source type="video/mp4">` with an `<img>` still fallback, which loads faster and uses less battery.
- Add a `prefers-reduced-motion` media condition so reduced-motion users get the still image.
- Always provide a still alternative for animated content.

## 194. Autoplay Rules
- Autoplay only works when the video is `muted` or has no audio track, and on iOS only with `playsinline`.
- Playback pauses if the video gains audio, is unmuted without a gesture, or leaves the viewport.
- Autoplay only when users expect it (video is the page's purpose); never depend on autoplay succeeding.
- One-way live streams (webinars) need an explicit play button.

## 195. Inline vs Fullscreen
- Play short-form content inline (`playsinline`); without it iPhone forces fullscreen.
- Present long-form content fullscreen.
- Use `preload="metadata"` to fetch only size, duration and tracks up front.
- Use HLS for streaming and H.264 MP4 for static files.

## 196. Low-Power Fullscreen Playback
- Fullscreen video on a black background with nothing else on screen can enter a low-power mode that skips compositing.
- Custom controls should fully hide while the user is just watching; do not leave timelines or overlays visible.

# Part 27 — Perceptual Contrast (APCA)

## 197. APCA Lc Levels
- `Lc 90`: preferred for body text and columns, e.g. `18px/300` or `14px/400`; non-body text from `12px`; `24px/200` for very thin fonts.
- `Lc 75`: minimum for columns of body text, e.g. `24px/300`, `18px/400`, `16px/500`, `14px/700`; non-body text `15px/400`.
- `Lc 60`: minimum for content text that is not body text, e.g. `48px/200`, `36px/300`, `24px/400`, `21px/500`, `18px/600`, `16px/700`.
- `Lc 45`: larger, heavier text such as headlines (`36px/400` or `24px/700`) and fine-detail pictograms or outline icons at least `4px` in their smallest dimension.
- `Lc 30`: absolute minimum for spot text (placeholder, disabled, copyright) and mostly solid icons at least `10px`.
- `Lc 15`: absolute minimum for discernible non-text elements at least `15px` (dividers, large button fills, thick focus outlines); treat anything lower as invisible.

## 198. APCA Adjustments
- To use a non-body size as body text, add `Lc 15`.
- For an AAA-equivalent target, add `Lc 15` to every level.
- Treat `Lc 90` as a maximum for text over `36px` bold and for large color areas, to avoid harsh glare.
- Example weight-400 table: `14px` needs `Lc 100`, `16px` `Lc 90`, `18px` `Lc 75`, `24px` `Lc 60`, `36px` `Lc 45`.
- Avoid weight `100` fonts entirely; fonts with x-height below `0.5` (prefer `0.52` or more) need larger size or heavier weight.

## 199. Polarity
- APCA is polarity-aware: dark-on-light yields positive Lc (up to about `106`), light-on-dark negative (down to about `-108`); compare absolute values.
- Enter text and background in the correct slots; swapping them changes the result.
- Size and weight drive readability more than hue; thin small text needs far more contrast than headlines.

## 200. WCAG 2 Contrast Ratios
- Normal text: `4.5:1` (AA), `7:1` (AAA).
- Large text: `3:1` (AA), `4.5:1` (AAA); large means at least `18pt` (`24px`) or `14pt` (`18.66px`) bold.
- UI components and graphics such as input borders and focus indicators: `3:1` (WCAG 2.1 AA).
- Check translucent foregrounds against the actual composited background.
- Links identified only by color must also contrast with surrounding text.

# Part 28 — Title Case

## 201. Chicago Headline Style
- Use Title Case (Chicago style) for headings and buttons.
- Always capitalize the first and last word, and the first word after a colon or of a subtitle.
- Capitalize nouns, pronouns, verbs, adjectives, adverbs and subordinating conjunctions (because, although, when, unless).
- Lowercase articles (`a`, `an`, `the`), coordinating conjunctions (`and`, `but`, `or`, `nor`, `for`), and `to` as an infinitive marker.
- Lowercase prepositions regardless of length (Chicago), unless used adverbially or adjectivally, as in "Set Up" or "Log In".
- In hyphenated compounds, capitalize both parts except articles, prepositions and coordinating conjunctions ("Well-Known", "State-of-the-Art").

## 202. Copy Conventions
- Use active voice and second person; avoid first person.
- Use specific button labels ("Save API Key", not "Continue").
- Use numerals for counts ("8 deployments").
- Error messages state the fix or next step, not only the problem.
- Use `&` instead of "and" only where space is tight.

## 203. Typographic Characters
- Use the ellipsis character `…`, not three periods; loading states end with it ("Loading…", "Saving…").
- Use curly quotes `“` `”` rather than straight quotes.
- Use non-breaking spaces in units, shortcuts and brand names (`10 MB`, `⌘ K`).
- Placeholders end with `…` and show an example pattern.

# Part 29 — Interface Typefaces

## 204. UI Sans and Mono Pairing
- Use a restrained, Swiss-style neo-grotesque sans for interface text and running prose, prioritizing legibility at small sizes.
- Use a companion monospace for code, terminals, IDs and tabular data, where character alignment aids scanning.
- Prefer a family with many weights (for example `9`) to build hierarchy without switching typefaces.
- Use stylistic sets for alternate glyphs (e.g., disambiguated `0`/`O`, `1`/`l`) where confusion is costly.

## 205. Numeric Alignment
- Apply `font-variant-numeric: tabular-nums` to number columns, timers and comparisons so digits do not shift.
- Balance or prettify heading wraps with `text-wrap: balance` or `text-wrap: pretty`.
- Exclude brand names, code tokens and identifiers from translation with `translate="no"`.

## 206. Long Content Resilience
- Handle long content with truncation, line clamping or word breaking; flex children need `min-width: 0` to truncate.
- Test user-generated content at short, average and very long lengths; never render broken UI for empty values.

# Part 30 — URL State

## 207. State Belongs in the URL
- Store filters, tabs, pagination, search terms, sort order and expanded panels in query parameters so views can be shared, bookmarked and restored on reload.
- Deep-link any stateful UI; if state lives only in component memory, consider syncing it to the URL.
- Treat URL design as part of the interface: readable keys and typed, predictable values.

## 208. History Semantics
- Push a history entry for navigational changes users expect Back to undo (changing tab, page); replace the entry for high-frequency changes (typing in search, dragging a slider).
- Throttle or debounce URL writes during rapid input.
- Update the URL shallowly by default; re-fetch from the server only when needed.

## 209. Clean Defaults
- Remove a parameter when its value equals the default so URLs stay short and canonical.
- Parse and validate values on read and fall back to defaults on malformed input.

## 210. Navigation and Destructive Actions
- Navigation uses real links so open-in-new-tab, Cmd/Ctrl-click and middle-click work.
- Warn before leaving with unsaved changes.
- Destructive actions need a confirmation or an undo window; never act immediately.

# Part 31 — Large Lists

## 211. Virtualize Long Lists
- Virtualize lists over `50` items, rendering only visible rows plus a buffer; or use `content-visibility: auto` for simpler cases.
- Never map over large arrays without virtualization.
- Tune the overscan buffer: smaller when items are expensive, larger to avoid blank flashes during fast scrolling.

## 212. Dynamic Row Sizes
- Measure variable-height rows at runtime, keyed by stable unique IDs, never array indexes.
- Give rows with late-loading media a fixed or minimum height to prevent layout jumps.

## 213. Reverse and Bidirectional Lists
- In chat-style lists, anchor scroll position so prepending older messages does not move the viewport.
- Load older items when scrolling up and newer when scrolling down, preserving the reading position.
- Restore scroll position when the user returns to a list.

## 214. Rendering Cost per Row
- Memoize row components and avoid passing changing props to every row.
- Defer creation of row elements for very large data sets (around `1,000`+ items) to cut startup time.

# Part 32 — Interaction Craft Details

## 215. Optical Alignment
- [context] Align by perception, not bounding boxes: nudge icons, play triangles and glyphs with uneven visual weight so they look centered.
- [context] Reduce padding slightly on the side of a button that holds an icon so text and icon feel balanced.

## 216. Brand Asset Shortcut
- [context] Let right-clicking the site logo open a menu offering the logo as SVG, brand guidelines or a press kit, since that is what people right-clicking a logo usually want.

## 217. Theme Color
- Set `<meta name="theme-color">` to match the page background so browser chrome blends with the page.
- Set `color-scheme: dark` on `<html>` in dark themes so native scrollbars and controls match.
- Give native `<select>` explicit `background-color` and `color` for Windows dark mode.

## 218. Gradient Banding
- [context] Prevent visible banding in large, subtle gradients by adding a faint noise or dither texture, or by adding intermediate color stops.
- [context] Check gradients on low bit-depth displays and in dark mode, where banding is most visible.

## 219. Moments of Delight
- [context] Add small, optional delight (such as an ambient northern-lights effect) only where it does not distract from tasks, and keep it subtle.
- [context] Gate delight animations behind `prefers-reduced-motion` and keep them performant.

## 220. Interactive States
- Every button and link has a hover state; hover, active and focus states are more prominent than rest.
- Show a visible focus style using `:focus-visible`; never remove outlines without replacement; use `:focus-within` for compound controls.
- Checkbox and radio labels share one hit target with the control, with no dead zones.

## 221. Form Ergonomics
- Use correct `type`, `inputmode` and `autocomplete` with meaningful `name` attributes.
- Never block paste; disable spellcheck on emails, codes and usernames.
- Show errors inline beside fields and focus the first error on submit.
