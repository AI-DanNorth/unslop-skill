# Design Rules by Concept

Distilled from a collection of UI engineering guidelines: view-transition motion, product writing, component composition, native mobile UI, user-perceived performance and fast rendering.

# Part 1 — When to Use Page/State Transitions

## 1. Purpose Test
- Every animated boundary must communicate a spatial relationship or continuity.
- If you cannot articulate what an animation communicates, do not add it.
- Use the browser's native view transition mechanism (`document.startViewTransition`) rather than third-party animation libraries; unsupported browsers simply skip the animation (graceful degradation).

## 2. Implementation Priority Order
- Implement every applicable pattern, in this order — it is an order of work, not a "pick one" list:
- 1. Shared element (named pair) — "same thing, going deeper".
- 2. Suspense/loading reveal — "data loaded".
- 3. List identity (per-item key) — "same items, new arrangement".
- 4. State change (enter/exit) — "something appeared/disappeared".
- 5. Route change (page-level) — "going to a new place".
- Skip a pattern only if the app has no use case for it.

## 3. Choosing Animation Style by Context
- Hierarchical navigation (list → detail): type-keyed directional slide (`nav-forward` / `nav-back`) — communicates spatial depth.
- Lateral navigation (tab-to-tab): plain cross-fade or no animation (`default="none"`) — there is no depth to communicate.
- Suspense reveal: simple enter/exit classes — content arriving.
- Revalidation / background refresh: no animation (`default="none"`) — silent.

## 4. Silence for Background Updates
- Background revalidation, deferred-value updates and unrelated transitions should not animate.
- A bare boundary fires the browser cross-fade on every trigger; opt out with `default="none"` and opt in only to the triggers that boundary should handle.

## 5. Audit Before Animating
- Inventory every navigation trigger (links, programmatic pushes).
- Inventory every loading boundary and what its fallback renders — each is a reveal candidate.
- List every page/route; each needs a placement decision.
- Identify persistent elements (headers, navbars, sidebars, sticky controls) that need isolation.
- Identify shared visual elements (images, cards, avatars) that appear on both a source and target view.
- Identify skeleton-to-content control pairs (search input, tab bar rendered in both fallback and content).

## 6. Navigation Map
- Classify every navigation into a table: route, destination, direction, pattern.
- `/` → `/detail/[id]`: forward, directional slide.
- `/detail/[id]` → `/`: back, directional slide.
- `/detail/[id]` → `/detail/[other]`: sequential — directional slide for ordered prev/next, otherwise key+share cross-fade.
- `/tab/[a]` → `/tab/[b]`: lateral — key+share cross-fade.
- Loading → content: slide-up reveal.
- For each shared element, note every navigation where a pair forms and where it does not — this decides whether an enter/exit fallback is needed alongside the morph.

# Part 2 — Motion Semantics

## 7. Shared Element Morph
- Communicates "this is the same thing" and "going deeper"; the element visibly travels and resizes from source to target.

## 8. Directional Slide
- Communicates spatial depth (hierarchy) or position in an ordered sequence.
- Falsely implies depth if used on lateral/unordered navigation — never use it there.

## 9. Cross-Fade
- Communicates a swap in place with no spatial relationship (tabs, panels, carousel content without order semantics).
- The browser default (`auto`) is a cross-fade.

## 10. Enter/Exit
- Communicates that something appeared or disappeared (panels, drawers, collapsible sections).

## 11. Vertical Reveal (Slide Up)
- Communicates content arriving / data loaded, replacing a skeleton.

## 12. List Reorder Motion
- Communicates "same items, new arrangement" — items keep identity while positions change.

## 13. Layout Displacement Glide
- Communicates that content below moved because something above changed; avoids teleporting.

## 14. Sliding Indicator
- Communicates selection moving between tabs or segments; the solid bar travels rather than blinking.

# Part 3 — Activation Mechanics

## 15. What Activates a Transition
- Only updates wrapped in a transition (`startTransition`), deferred values (`useDeferredValue`), or loading-boundary (Suspense) resolutions animate.
- A regular synchronous state update does not animate; `flushSync` skips animations — use `startTransition`.
- Never call `document.startViewTransition` yourself when the framework manages it.

## 16. Trigger Types
- enter: boundary first inserted during a transition.
- exit: boundary first removed during a transition.
- update: DOM mutations inside a boundary, or the boundary changing size/position due to an immediate sibling; with nested boundaries the innermost one owns the mutation.
- share: a named boundary unmounts and another with the same name mounts in the same transition.

## 17. Placement Rule
- An animated boundary only activates enter/exit if it appears before any DOM node — a wrapping `<div>` around it suppresses enter/exit.
- Avoid wrapper elements between a list and its per-item boundaries.
- Only update animates (no enter/exit) when swapping content without a loading boundary — conditionally render the boundary itself instead.

## 18. Class Values per Trigger
- `"auto"`: browser cross-fade.
- `"none"`: disabled.
- `"class-name"`: custom CSS class targeted via pseudo-elements.
- `{ [type]: value, default: value }`: type-specific classes; a `default` key is required.
- If `default` is `"none"`, every trigger is off unless explicitly listed.

## 19. Pseudo-Element Anatomy
- `::view-transition-old(.class)` — outgoing snapshot.
- `::view-transition-new(.class)` — incoming snapshot.
- `::view-transition-group(.class)` — container that animates position/size.
- `::view-transition-image-pair(.class)` — wraps old + new.
- `::view-transition` — the fixed overlay hosting everything.

## 20. Transition Types
- Tag a transition with semantic types (e.g. `nav-forward`, `select-item`) so different boundaries pick different animations from the same event.
- Types can be stacked; different boundaries in the tree respond to different types.
- Type maps work on enter, exit and share.
- Centralize the type-keyed boundary in a reusable wrapper so every page shares one definition and new types are added in one place.

## 21. Simultaneity
- Every boundary matching the trigger fires simultaneously within one view transition.
- Boundaries in different transitions (navigation vs. a later loading resolve) never compete.
- Rapid successive updates are batched: A→B→C→D renders as B→D.

## 22. Force Re-Enter with Key
- Changing a boundary's `key` (e.g. to the serialized search params) forces exit + enter, replaying an entrance like `slide-up` on new results.
- If the key wraps a loading boundary, changing it remounts and refetches.

## 23. Cross-Fade Without Remount
- Omit `key` to get an update cross-fade instead of exit + enter; avoids remount/refetch.
- Use `key` when content identity changes (state should reset); omit it for tabs, panels, carousels.

## 24. Imperative Animation Hooks
- Per-trigger callbacks (`onEnter`, `onExit`, `onUpdate`, `onShare`) let you drive the Web Animations API on `instance.old`, `instance.new`, `instance.group`, `instance.imagePair`.
- Example entrance: keyframes `[{ transform: 'scale(0.8)', opacity: 0 }, { transform: 'scale(1)', opacity: 1 }]`, `duration: 300`, `easing: 'ease-out'`.
- Always return a cleanup that cancels the animation; vary behavior by the types array.
- Share callback takes precedence over enter/exit callbacks.

# Part 4 — Transition Recipes

## 25. Timing Tokens
- Define shared duration tokens:
```css
:root {
  --duration-exit: 150ms;
  --duration-enter: 210ms;
  --duration-move: 400ms;
}
```

## 26. Shared Keyframes
- Keep a small reusable keyframe set; directions come from custom properties, not separate keyframes.
```css
@keyframes fade { from { opacity: 0; } to { opacity: 1; } }
@keyframes slide { from { translate: var(--slide-offset); } to { translate: 0; } }
@keyframes slide-y {
  from { transform: translateY(var(--slide-y-offset, 10px)); }
  to { transform: translateY(0); }
}
```
- Exits reuse the same keyframes with `reverse`.

## 27. Fade
- Exit: `var(--duration-exit) ease-in fade reverse`.
- Enter: `var(--duration-enter) ease-out var(--duration-exit) both fade` — delayed by the exit duration so old leaves before new arrives.
```css
::view-transition-old(.fade-out) { animation: var(--duration-exit) ease-in fade reverse; }
::view-transition-new(.fade-in) { animation: var(--duration-enter) ease-out var(--duration-exit) both fade; }
```
- Keep the shared fade keyframe opacity-only so ordinary reveals stay crisp.

## 28. Vertical Slide (Skeleton → Content)
- Outgoing skeleton (`slide-down`): fade reverse + `slide-y` reverse, both `var(--duration-exit) ease-out both`.
- Incoming content (`slide-up`): `var(--duration-enter) ease-in var(--duration-exit) both fade` plus `var(--duration-move) ease-in both slide-y`.
- Default vertical offset `10px` via `--slide-y-offset`.

## 29. Directional Horizontal Slide
- Offset `60px`; incoming from the right uses `--slide-offset: 60px`, outgoing to the left uses `--slide-offset: -60px`.
- Incoming: `var(--duration-enter) ease-out var(--duration-exit) both fade, var(--duration-move) ease-in-out both slide`.
- Outgoing: `var(--duration-exit) ease-in both fade reverse, var(--duration-move) ease-in-out both slide reverse`.
- Pair classes: `slide-from-right` / `slide-to-left` for forward, `slide-from-left` / `slide-to-right` for back.

## 30. Single-Class Directional Navigation
- One class per direction targeting both snapshots:
```css
::view-transition-old(.nav-forward) { --slide-offset: -60px; animation: var(--duration-exit) ease-in both fade reverse, var(--duration-move) ease-in-out both slide reverse; }
::view-transition-new(.nav-forward) { --slide-offset: 60px; animation: var(--duration-enter) ease-out var(--duration-exit) both fade, var(--duration-move) ease-in-out both slide; }
::view-transition-old(.nav-back) { --slide-offset: 60px; animation: var(--duration-exit) ease-in both fade reverse, var(--duration-move) ease-in-out both slide reverse; }
::view-transition-new(.nav-back) { --slide-offset: -60px; animation: var(--duration-enter) ease-out var(--duration-exit) both fade, var(--duration-move) ease-in-out both slide; }
```

## 31. Asymmetric Enter/Exit
- Enter and exit need not match: e.g. new page fades in while the old page slides out directionally.

## 32. Shared Element Morph
- Group duration `var(--duration-move)`; add a mid-flight motion blur on the image pair.
```css
::view-transition-group(.morph) { animation-duration: var(--duration-move); }
::view-transition-image-pair(.morph) { animation-name: via-blur; }
@keyframes via-blur { 30% { filter: blur(3px); } }
```
- For a simpler morph use the browser default (`auto`).
- Scope blur to the specific morph class; never put it in shared fade keyframes.

## 33. Text Morph
- Avoids raster-scaling ghosting on text by hiding the old snapshot and showing new text at full resolution.
```css
::view-transition-group(.text-morph) { animation-duration: var(--duration-move); }
::view-transition-old(.text-morph) { display: none; }
::view-transition-new(.text-morph) { animation: none; object-fit: none; object-position: left top; }
```

## 34. Scale
- Exit: `var(--duration-exit) ease-in scale-down`; enter: `var(--duration-enter) ease-out var(--duration-exit) both scale-up`.
- Keyframes scale between `scale(1)`/`opacity: 1` and `scale(0.85)`/`opacity: 0`.

## 35. Sliding Indicator (Tab Underline / Segmented Pill)
- Animate only the group; disable old/new so the solid bar slides instead of cross-fading.
```css
::view-transition-group(.tab-underline) {
  animation-duration: 220ms;
  animation-timing-function: cubic-bezier(0.5, 0, 0.2, 1);
}
::view-transition-old(.tab-underline),
::view-transition-new(.tab-underline) { animation: none; height: 100%; }
```
- Render the indicator only under the active tab so exactly one element holds the name; use a distinct name per tab strip.
- Trigger the selection change inside a transition so the move animates.

## 36. Expand/Collapse
- Wrap conditionally rendered content in a boundary with `enter="expand-in"` / `exit="collapse-out"`; toggle inside a transition.
- To preserve hidden-subtree state (scroll, form input) while it animates in and out, pair with a state-preserving visibility wrapper (Activity); only do so when there is state worth preserving.

## 37. Card Expand to Detail
- Grid item and its expanded detail share `item-${id}`; open/close inside a transition.
- Save scroll position before expanding; on close, restore with smooth scroll after ~`100`ms.

## 38. Same-Route Content Swap
- When content changes within the same route/segment (e.g. `/collection/[slug]`), use `key` = segment + a stable `name` + `share="auto"` + `default="none"` for a container cross-fade.
- Keep the boundary inside the loading boundary (without keying the loading boundary) so old content stays visible while loading.

# Part 5 — Shared Element Rules

## 39. Unique Names
- Only one element with a given name may be mounted at a time; use ID-prefixed names (`photo-${id}`, `product-${id}`).
- Reusable components rendered simultaneously in two surfaces (modal/popover and page) break the morph — make the name conditional or move it to the specific consumer.

## 40. Share Precedence and Fallbacks
- Share takes precedence over enter/exit.
- When no pair forms on a path (target lacks the name), enter/exit fires instead — decide whether the element needs a fallback animation there.

## 41. Silent Morph Failures
- `default="none"` without an explicit share value turns share off — always set share explicitly (e.g. `share="morph"`).
- A type-keyed share resolves to its `default` when the navigation never adds the type — every link that should morph must add the type.

## 42. Target Readiness
- Both old and new must be rendered in the same transition; a target behind an unresolved loading fallback cannot pair.
- Render the target above the data boundary, or prefetch/cache its data so it resolves in time.
- If the destination still suspends, the route transition animates the fallback and the content arrives in a later untyped transition — give it its own reveal.

## 43. List-Side Shared Elements
- Add `default="none"` on list-side named elements so filter/search updates do not cross-fade every item on each keystroke.

## 44. Composing with List Identity
- Shared element and list identity are independent: use an outer keyed boundary (reorder/enter) and an inner named boundary (cross-route morph).
- Missing either layer silently loses that animation.

## 45. No Fade-Out Exit with Morphs
- Never pair a shared morph with a fading page exit — the fade dissolves the source mid-morph; use a directional slide or no exit.

## 46. Raster Snapshot Limits
- Morphs scale raster snapshots; large size differences on text (`<h3>` → `<h1>`) produce ghosting — use the text-morph recipe.
- `border-radius` can be lost; apply it directly to the captured element.

## 47. Skeleton-to-Control Morph
- Give a skeleton control and its real counterpart the same `view-transition-name` so they morph in place instead of sliding away.
- Use fallback/content share pairs only when interpolation does not distort layout or geometry.

## 48. Manual Names Inside Managed Boundaries
- Do not put a manual `viewTransitionName` on the root DOM node inside a managed boundary — the auto-assigned name overrides it.

# Part 6 — Navigation Direction

## 49. Reserve Directional Motion
- Use directional slides only for hierarchical navigation and ordered sequences (prev/next photo, carousel, paginated results).
- In ordered sequences, "next" slides in from the right and "previous" from the left.

## 50. Tag Direction Explicitly
- Mark each navigation with a direction type (`nav-forward`, `nav-back`) at the trigger (link prop or programmatic push).
- Back/forward browser buttons and history-back calls carry no types — typed slides resolve to default and do not play (untyped morphs still apply); use explicit push to a URL for typed back motion.

## 51. Always Pair Enter with Exit
- Without an exit, the old page vanishes instantly while the new one animates in.
- Include `default: "none"` in type maps and `default="none"` on the boundary so it does not fire on every transition.

## 52. Page-Level Placement
- Put directional boundaries in each page, not in a persistent layout — layouts persist and never trigger enter/exit on route changes.
- Do not wrap layout children in a boundary when pages have their own; the nested page boundaries mount as one unit with the parent and silently skip enter/exit.
- A bare layout boundary works only when pages have none of their own.

## 53. Two Layers Coexist
- Directional slides (typed, fire on navigation) and loading reveals (untyped, fire on data arrival) coexist because they fire at different moments; `default="none"` on both prevents interference.

## 54. Nested Stagger Limitation
- When a parent boundary mounts as one unit, nested boundaries do not animate individually — per-item staggered entrances during page navigation are unavailable.

## 55. Verify in Production Conditions
- Test directional transitions in a production build with a cold cache; development mode may not prefetch, changing what is ready at commit.

# Part 7 — Loading Reveals

## 56. Separate Fallback and Content Boundaries
- Wrap the skeleton in an exit boundary (`slide-down`) and the content in an enter boundary (`slide-up`, `default="none"`).
- Simpler alternative: one bare boundary around the loading boundary for a zero-config cross-fade.

## 57. Untyped Reveal Props
- Loading resolutions fire as separate transitions without types — use simple string classes, never type maps.

## 58. Prevent Re-Animation
- Always set `default="none"` on the content boundary to avoid re-animating on revalidation.

## 59. Enter-Only Reveal with Live Root
- With the root animation disabled, skip the fallback exit entirely: the skeleton snaps out live while content fades in (`enter="auto"`, `default="none"`).

## 60. Shared Content Outside the Boundary
- An element rendered in both fallback and content (title, heading) fades against itself and dips in opacity — render it once above the loading boundary or pin it with its own name.

## 61. Unwanted Enter on Warm Navigation
- If content enters even though the fallback never showed, add a host DOM element immediately outside the loading boundary at that call site to suppress the nested enter while keeping later reveals working.

## 62. Keep Reveals Short
- The overlay is `position: fixed` and snapshots do not scroll; long reveals make scrolling feel hung.

# Part 8 — Lists and Layout

## 63. List Reorder
- Wrap each item in a boundary keyed by stable ID; trigger sorting/filtering inside a transition.
- Keyed list items want update — leave them bare or set `update="auto"`.

## 64. Optimistic Controls vs. Committed Content
- Drive control labels (sort button text, `aria-current`) from an optimistic value so feedback is instant and excluded from animation.
- Drive the animated list from committed state; optimistic list order resolves before the snapshot and will not animate.
- For tabs whose content suspends, an optimistic `aria-current` keeps the strip from feeling dead while the indicator follows committed state.

## 65. Layout Displacement Morph
- Only content inside an activated boundary animates position; everything else teleports.
- Wrap sibling content below a growing/shrinking list in a bare boundary so it glides as one group.
- Place that boundary as a direct sibling of the changing content; a boundary under an extra wrapper is not measured.
- `default="none"` disables this glide by turning off update.

## 66. Fixed Slot Alternative
- Sometimes the better fix is no morph: pad fixed-size lists to a constant slot count with invisible fillers so height never changes.

# Part 9 — Isolating Persistent and Floating Elements

## 67. Pull Out of the Root Snapshot
- Persistent chrome (header, nav, sidebar, player bar) gets its own real, unique `view-transition-name` so it does not slide or fade with page content.
- `view-transition-name: none` is a no-op (the CSS default) and leaves the element in root — a common flicker cause.
- A raw `view-transition-name` only isolates; it does not activate an animation.

## 68. Persistent Element CSS
```css
::view-transition-group(persistent-nav) { animation: none; z-index: 100; }
```
- Hand-name when you need `z-index` or `display` control; an auto-named neutral boundary cannot take those.

## 69. Z-Index Tiers
- Chrome pinned at `100`; toasts/overlays that must beat everything at `200`.

## 70. Backdrop-Filter Elements
- For elements using `backdrop-filter`, hide the old snapshot to avoid a flash:
```css
::view-transition-old(persistent-nav) { display: none; }
::view-transition-new(persistent-nav) { animation: none; }
```

## 71. Floating Elements
- Open popovers, menus, tooltips and control clusters are captured in root and flicker on settle; give each a unique name and:
```css
::view-transition-group(popover) { animation: none; z-index: 100; }
::view-transition-old(popover), ::view-transition-new(popover) { animation: none; }
```
- A static name is fine if only one is mounted at a time.
- Native top-layer (`popover`, `<dialog>`) settle-flicker is a browser limit.

## 72. Third-Party Overlays
- Name an always-mounted wrapper you own (e.g. a fixed full-inset, `pointer-events-none` toaster container) rather than a library container that unmounts when empty.
- Name a dialog's backdrop separately from its panel so each pins independently.

## 73. Live Root (No Root Cross-Fade)
- The root cross-fade freezes unnamed content behind a stale snapshot; hover/active styles stop rendering.
- `::view-transition-new(root)` is a live capture, so disable the root animation:
```css
::view-transition-old(root) { display: none; }
::view-transition-new(root) { animation: none; }
```
- Named/classed groups still animate above root; unnamed content swaps instantly, so regions that should fade need their own boundary.
- This removes most need to hand-name static chrome; keep names only for elements that must stack above animating groups.

# Part 10 — Interactivity During Transitions

## 74. Overlay Blocks Pointer Events
- The `::view-transition` overlay captures all pointer events while animations are in flight.
- To let clicks/hover pass through: `::view-transition { pointer-events: none; }`.
- Trade-off: clicks can hit live elements under still-moving snapshots.

## 75. Cost of Naming Interactive Elements
- Named participants are skipped by hit-testing for the transition's duration, with no CSS override — clicks fall through to what is beneath.
- Portal named popovers/menus; rendered inline in a clickable row, mid-transition clicks activate the row and read as outside-clicks that close the popover.
- Brief dead clicks during the transition remain the price of the name; weigh this before naming interactive elements.

## 76. Scroll During Transitions
- Snapshots do not scroll; keep durations short, and prefer gesture-driven transitions for scroll-driven UI.
- Avoid hash-fragment navigation, which causes scroll jumps; navigate without hash and scroll programmatically afterwards.

# Part 11 — Reduced Motion

## 77. Global Reduced-Motion Override
- Always include in the global stylesheet:
```css
@media (prefers-reduced-motion: reduce) {
  ::view-transition-old(*),
  ::view-transition-new(*),
  ::view-transition-group(*) {
    animation-duration: 0s !important;
    animation-delay: 0s !important;
  }
}
```
- Zero both duration and delay so delayed enters (offset by the exit duration) do not leave a blank gap.

# Part 12 — Timing and Easing

## 78. Duration Ranges by Interaction
- Direct toggle (expand/collapse): `100–200ms`.
- Route transition (slide): `150–250ms`.
- Loading reveal (skeleton → content): `200–400ms`.
- Shared element morph: `300–500ms`.

## 79. Exit Faster Than Enter
- Exit `150ms`, enter `210ms`, movement `400ms`.
- Delay enter by the exit duration (`var(--duration-exit)`) so the outgoing state clears first; use `both` fill so the incoming snapshot stays hidden during the delay.

## 80. Easing Assignments
- Exits fade with `ease-in` (accelerate away); enters fade with `ease-out` (decelerate into place).
- Horizontal movement uses `ease-in-out` over `--duration-move`.
- Sliding indicators use `cubic-bezier(0.5, 0, 0.2, 1)` at `220ms`.

## 81. Opacity and Motion Run on Separate Clocks
- Combine a short fade with a longer translate (e.g. `210ms` fade + `400ms` slide) in one comma-separated `animation` declaration.

## 82. Customize Timing Last
- Get structure working first, then tune durations; keep ordinary cross-fades opacity-only and scope blur to intentional morphs.

# Part 13 — Pitfalls and Visual Glitches

## 83. Everything Cross-Fades
- Bare boundaries fire on every transition (link clicks, revalidations, deferred updates) — set `default="none"` deliberately on named elements and type-keyed page boundaries.

## 84. Over-Disabling
- `default="none"` also turns off update (layout morphs) and share (named pairs without explicit share) — check it does not block an animation you want.

## 85. Persistent Chrome Slides with Page
- Missing isolation name on headers/navs; add a unique name plus isolation CSS.

## 86. Popover Flicker on Settle
- Floating element captured in root; give it a real unique name and isolation CSS.

## 87. Backdrop-Blur Flash
- Use the hide-old-snapshot workaround.

## 88. Text Ghosting
- Raster scaling of text in morphs; use the text-morph recipe.

## 89. Lost Corner Radius
- Apply `border-radius` directly to the captured element.

## 90. Section Below List Teleports
- It is outside any activated boundary, its boundary has `default="none"`, or it is not an immediate sibling of the changing content.

## 91. Skeleton Controls Slide Away
- Give matching skeleton and real controls the same name.

## 92. Opacity Dip on Reveal
- Element present in both fallback and content; render it outside the loading boundary.

## 93. Morph Dissolves Mid-Flight
- Page fade exit competing with a shared morph; remove the fade or use a directional exit.

## 94. Directional Slide Missing on Back
- History traversal carries no types; use explicit pushes for typed back motion.

## 95. Reveal Never Animates
- Type maps on a loading reveal never match; use string classes.

## 96. Page Animations Silently Dead
- A layout-level boundary wraps page boundaries; remove it.

## 97. Same-Route Update Not Animating
- A nested boundary owns the mutation; for a real identity change use key + stable name + share.

## 98. Duplicate Name Error
- Two mounted elements share a name; make names ID-unique or conditional.

## 99. Batched Intermediate States
- Updates fired during an animation are batched, so intermediate states are skipped (A→B→C→D becomes B→D).

# Part 14 — Verification

## 100. Walk Every Path
- For each navigation map row, confirm whether the boundary mounts/unmounts or stays mounted (same route).
- For named elements, confirm a pair forms; if not, confirm enter/exit provides a fallback.
- Confirm `default="none"` is not blocking a wanted animation.
- Confirm persistent elements stay static and do not slide with page content.
- Confirm loading reveals animate independently of directional navigations.
- Confirm no path produces either no animation or competing animations.

# Part 15 — Planning & Page Purpose

## 101. Plan Before Writing
- Write a plan before drafting any page; the plan is the spec.
- The plan has five sections: overview, goal, audiences, documentation plan, open questions.
- Draft the plan by hand, even when AI helps write the page later.

## 102. Declare a Content Type
- Every page declares exactly one content type: `Tutorial`, `How-to`, `Reference`, `Conceptual`, `Troubleshooting`, or `Landing`.
- Record it as metadata (for example `meta.contentType`) so the type drives tone and structure.

## 103. One Job per Page
- Each page does one job: a tutorial, a how-to, or a reference, never all three.
- Instead of a page that teaches, walks through a task and lists every option, split it into separate pages and link them.

## 104. User-Shaped Titles
- The title is the reader's question or task, not a feature name.
- Instead of a bare product or feature label, title the page around what the reader is trying to do.

## 105. Testable Goals
- State the page goal so it can be verified.
- Start the goal with a Bloom's taxonomy verb such as `configure`, `explain`, or `debug`.

## 106. Define Terms on First Use
- Define every term the first time it appears.
- Link that first mention to the term's conceptual page.

# Part 16 — Voice & Tone

## 107. Active Voice
- Write in active voice.
- Test: append "by monkeys" after the verb; if the sentence still parses, it is passive, so rewrite it.

## 108. Direct Address
- Address the reader as `you`.
- Instead of "the user can configure" or "one can configure", say "you can configure".

## 109. Imperative Steps
- Write steps as commands.
- Instead of "You will need to click…", say "Click **Add Project**."

## 110. Present Tense
- Use present tense unless you are describing future behavior.

## 111. Contractions
- Use contractions such as `you'll` and `it's` to keep the voice natural.

## 112. Careful Use of "We"
- Never use "we" to mean "you".
- Use "we" only for deliberate actions your organization itself takes.

## 113. No Rhetorical Questions
- Never pose rhetorical questions; state the point directly.

## 114. Tone Matches Content Type
- Tutorial: warm and encouraging.
- How-to: terse and direct.
- Reference: neutral and exhaustive.
- Conceptual: explain well enough that the reader could teach it back.
- Troubleshooting: empathetic, not apologetic.

# Part 17 — Clarity & Concision

## 115. Short Sentences
- Keep sentences under `20` words.

## 116. Second-Read Test
- Each sentence parses in one read at speaking pace.
- Name the subject, the action and the consequence; remove metaphor verbs and pronouns that point far back.

## 117. Short Paragraphs
- Keep paragraphs to `2`–`4` sentences.
- Split any paragraph that runs longer or covers two ideas.

## 118. Earn Every Detail
- Cut any number, name, or implementation detail that would not change what the reader understands or does.

## 119. Banned Hype Words
- Never use `easy`, `simple`, or `quick` to describe a task.
- Instead of "Deploying is easy", describe the steps and let the reader judge.

## 120. Filler Words
- Cut `very`, `just`, `really`, and `simply`.
- Instead of "Just run the command", say "Run the command."

## 121. Weasel Words
- Never use `significantly`, `many`, `often`, `typically`, or `generally`.
- Instead of "builds are typically faster", give the specific number or claim.

## 122. Vague Quantifiers
- Never use `near-zero`, `sub-second`, or `most requests`.
- Give the actual figure and cite where it comes from.

## 123. Literal Verbs over Metaphor Verbs
- Avoid `moves through`, `lands`, `carries`, and `hits`.
- Instead of "the request hits the cache", name the literal step: "the server checks the cache".

# Part 18 — AI-Writing Anti-Patterns

## 124. No Summary Transitions
- Do not recap the previous paragraph before moving on; pivot straight to the next point.
- Instead of "With this setup complete…", start with the next action or fact.

## 125. No Choppy Fragments
- Do not break one dependent idea into stop-start sentences; keep it in one sentence.

## 126. No Spec-Sheet Voice
- Avoid datasheet phrasing like `provides`, `is configurable`, and `is explicitly labeled`.
- Instead of "The option is configurable", say what the reader sets and what changes.

## 127. No Cold Opens
- Do not start a body paragraph without an antecedent; carry the prior subject forward.

## 128. No Personified Software
- Give software literal actions, not human ones.
- Instead of "hand the browser a URL", say "the browser fetches the URL".

## 129. No Template Framing
- Avoid generic framing that could sit on any page.
- Instead of "The question most teams face is whether…", open with the point specific to this page.

# Part 19 — Structure & Headings

## 130. Sentence-Case Headings
- Use sentence case for every heading from H1 to H6.
- Instead of `Getting Started With Your Project`, write `Getting started with your project`.

## 131. Title-Case Navigation Labels
- Use title case only for navigation labels, for example `Getting Started`.

## 132. Descriptive Subheadings
- Subheadings say what the section covers.
- Instead of `Caveats`, write `Caveats when self-hosting on Cloudflare`.

## 133. Open with a TL;DR
- Open every page with a short TL;DR paragraph.

## 134. Section Summaries
- Open every major section with a one-sentence summary.

## 135. Spell Out Acronyms
- Spell out every acronym on first use, for example `Content Security Policy (CSP)`.

# Part 20 — Lists

## 136. Convert List-Shaped Content
- When three or more items share a shape, put them in a list instead of a sentence.

## 137. Introduce Lists with a Colon
- Instead of a lead-in like `The options are`, write `The options are:`.

## 138. Bold-Term List Format
- Format list items as `- **Term**: description`.

## 139. List Item Punctuation
- Use periods only on items that are full sentences.
- Instead of `- Fast startup.`, write `- **Startup**: Fast on cold boots.`

# Part 21 — Code & Technical Writing

## 140. Tag Every Code Block
- Every code fence names its language.
- Instead of an untagged fence, tag it, for example ` ```ts `.

## 141. TypeScript by Default
- Prefer TypeScript for new code examples.

## 142. Short Snippets
- Keep code lines at `80` columns or fewer and snippets at `25` lines or fewer.
- Split longer snippets and connect the parts with prose.

## 143. Highlight Key Lines
- Highlight the lines that matter, for example ` ```ts {8-12} `.

## 144. Explain Every Block
- Explain each code block in prose; never drop code in without context.

## 145. Steps for Multi-Step Flows
- Wrap multi-step procedures in a steps component such as `<Steps/>`.

## 146. No "See the Full Example" Endings
- Never end a guide with "see the full example file"; the guide itself must be complete.

## 147. Current Model Strings
- Use current model identifiers in examples, such as `anthropic/claude-opus-4-7`.
- Instead of an outdated identifier such as `gpt-4o`, use a current one.

# Part 22 — Placeholders, Units & Numbers

## 148. Descriptive Text Placeholders
- Use descriptive `snake_case` placeholders.
- Instead of `<TOKEN>`, `your-token`, `xxx`, or `ABC123`, write `your_access_token_here`.

## 149. Counting Number Placeholders
- Numeric placeholders count up, for example `1234567890123`.

## 150. Space Before Units
- Put a space between a number and its unit.
- Instead of `64KB`, write `64 KB`; write `200 ms`.

## 151. Bare Seconds
- Seconds are the exception and stay bare, for example `30s`.

## 152. Numerals for Counts
- Use numerals for counts.
- Instead of "eight deployments", write "8 deployments".

# Part 23 — Formatting & Punctuation

## 153. No Dashes as Punctuation
- Replace em dashes, and hyphens used as dashes, with a colon, comma, period or a rewrite.
- Instead of "The cache—which expires daily—is shared.", write "The cache, which expires daily, is shared."

## 154. Curly Quotes
- Use curly quotes, for example `“Save”`, not straight quotes.

## 155. Ellipsis Character
- Use the single ellipsis character `…`, not three dots.
- Instead of `Loading...`, write `Loading…`.

## 156. Loading States
- End loading and progress labels with `…`, for example `Saving…` and `Loading…`.

## 157. Non-Breaking Spaces
- Use non-breaking spaces to keep glued terms on one line, for example `10&nbsp;MB` and `⌘&nbsp;K`.

## 158. Ampersand Only When Tight
- Use `&` for "and" only where space is tight, such as labels.

## 159. Bold for UI and Critical Facts Only
- Use bold only for UI elements or critical facts.
- Instead of "This step is **really** important.", write "Click **Add Project**." and bold only the control name.

## 160. Inline Code for Identifiers
- Use inline code for paths, file extensions, identifiers and short snippets, for example `/api`, `.tsx`, `body`.

## 161. No Hard Wraps
- Never hard-wrap paragraphs; each paragraph is one line in the source.

## 162. Spacing Around Blocks
- Leave one blank line before headings and before and after code blocks.

## 163. No Horizontal Rules
- Never use `---` rules to separate sections; let headings do it.

# Part 24 — Links

## 164. Descriptive Anchor Text
- Anchor text names the destination.
- Instead of "click here", write "see the pricing model page".

## 165. No Bare URLs
- Never paste bare URLs, and never use `here` or `link` as anchor text.

# Part 25 — Pricing & Money Pages

## 166. Pricing in Tables
- Present pricing in tables, with exhaustive detail.

## 167. Explain the Pricing Model
- Document the pricing model explicitly; never assume the reader understands it.
- Define what counts as one unit of usage, for example what counts as one invocation.

# Part 26 — AI-Assisted Writing & Review

## 168. Author Accountability
- The author is accountable for every word, including AI-generated content.
- Hold technical accuracy to a high bar, because language models also consume the docs.

## 169. Approved Models Only
- Use only enterprise models that do not train on your data.

## 170. Disclose AI Use
- Disclose AI assistance in the pull request description.

## 171. Human Final Review
- A human always completes the final review.
- Test pages by prompting against them to check they answer the intended questions.

## 172. Pull Request Contents
- The PR description links the plan, lists what to review, and links the preview URL.

## 173. Generous Reviews
- The author makes the final call; reviewers approve liberally.
- Use suggestion comments for small fixes and preview comments for larger feedback.
- Resolve disagreements with a short stated reason.

# Part 27 — Component Architecture

## 174. Composition over Configuration
- Let consumers compose pieces instead of adding props for every case.
- Why: each new configuration prop adds a branch the component must handle forever.
- Incorrect: adding a prop to toggle each new behavior; correct: exposing parts the consumer arranges.

## 175. Avoid Boolean Prop Proliferation
- Do not add boolean props like `isThread`, `isEditing`, `isDMThread`, or `isForwarding` to customize behavior.
- Why: each boolean doubles the possible states and creates unmaintainable nested conditionals.
- Incorrect: one `Composer` with ternaries on `isDMThread ? … : isThread ? …`; correct: separate `ChannelComposer`, `ThreadComposer`, and `EditComposer` that each compose shared parts.

## 176. Share Internals, Not a Monolithic Parent
- Variants share subcomponents rather than one parent that does everything.
- Why: each variant stays explicit about what it renders while reusing the same building blocks.
- Incorrect: one component with every mode built in; correct: small parts like `Composer.Input` reused across variants.

# Part 28 — Compound Components

## 177. Use Compound Components
- Structure complex components as a set of subcomponents that share a context.
- Why: enables flexible composition with no prop drilling and no hidden conditionals.
- Incorrect: a monolith taking `renderHeader`, `showAttachments`, `showFormatting`, `showEmojis`; correct: `Composer.Frame`, `Composer.Input`, `Composer.Footer`, `Composer.Submit` composed as needed.

## 178. Subcomponents Read Context, Not Props
- Each subcomponent pulls shared state and actions from context.
- Why: the parent does not have to thread props down to every piece.
- Incorrect: passing `value` and `onChange` into each child; correct: `ComposerInput` reads `state.input` and `actions.update` from `ComposerContext`.

## 179. Export as a Namespace Object
- Export the parts together under one name, for example `const Composer = { Provider, Frame, Input, Submit, Header, Footer, … }`.
- Why: consumers find all related parts in one place and the structure reads clearly in JSX.
- Incorrect: unrelated top-level exports with no grouping; correct: `<Composer.Footer><Composer.Submit /></Composer.Footer>`.

## 180. Consumers Compose Exactly What They Need
- Consumers include only the parts they want, in the order they want.
- Why: the rendered output is visible at the call site, with no flags hiding behavior.
- Incorrect: `showFormatting={false}`; correct: simply leaving out `<Composer.Formatting />`.

# Part 29 — State Ownership

## 181. Lift State into Provider Components
- Move state management into a dedicated provider component.
- Why: siblings outside the main UI can read and change state without prop drilling or refs.
- Incorrect: `useState` trapped inside `ForwardMessageComposer`; correct: `ForwardMessageProvider` owns state and wraps the whole dialog.

## 182. No Effect-Based State Syncing
- Do not mirror child state upward with `useEffect` and an `onInputChange` callback.
- Why: syncing on every change duplicates state and causes extra renders and drift.
- Incorrect: `useEffect(() => onInputChange(state.input), [state.input])`; correct: lift the state into a shared provider.

## 183. No Reading State Through Refs
- Do not expose internal state through a `stateRef` read at submit time.
- Why: refs bypass React's data flow and couple siblings through hidden handles.
- Incorrect: `submit(stateRef.current)`; correct: `ForwardButton` calls `actions.submit` from context.

## 184. Provider Boundary over Visual Nesting
- Components that share state need to be inside the same provider, not inside the same visual box.
- Why: buttons and previews can live anywhere in the layout and still access state.
- Incorrect: forcing `ForwardButton` inside `Composer.Frame`; correct: placing it in `DialogActions` within `ForwardMessageProvider`.

## 185. Decouple State Management from UI
- The provider is the only place that knows how state is stored.
- Why: you can swap `useState`, Zustand, or server sync without touching the UI.
- Incorrect: `ChannelComposer` calling `useGlobalChannelState` and `useChannelSync` directly; correct: `ChannelProvider` calls `useGlobalChannel` and passes `state` and `actions` to `Composer.Provider`.

## 186. Swap the Provider, Keep the UI
- Different providers can back the same composed UI.
- Why: one set of UI parts serves ephemeral forms and globally synced data alike.
- Incorrect: a separate input component per data source; correct: the same `Composer.Input` under `ForwardMessageProvider` (local state) or `ChannelProvider` (global synced state).

# Part 30 — Context Interfaces

## 187. Generic State, Actions, Meta Interface
- Define the context as a generic contract with three parts: `state`, `actions`, and `meta`.
- Why: any provider can implement it, making state dependency-injectable.
- Incorrect: `ComposerInput` calling `useChannelComposerState()` directly; correct: `ComposerInput` reads `ComposerContextValue` via `use(ComposerContext)`.

## 188. State Holds Data
- `state` holds the data the UI renders, for example `input`, `attachments`, `isSubmitting`.
- Why: UI parts read a predictable shape regardless of where data comes from.
- Incorrect: each part fetching its own data; correct: every part reading `state.input` from context.

## 189. Actions Hold Operations
- `actions` holds the operations, for example `update(updater)` and `submit()`.
- Why: UI triggers behavior without knowing how it is carried out.
- Incorrect: a button calling a sync API itself; correct: `onPress={actions.submit}`.

## 190. Meta Holds Non-State Handles
- `meta` holds supporting values such as `inputRef`.
- Why: refs and similar handles stay out of render state but remain reachable.
- Incorrect: passing refs down as props through layers; correct: `ref={meta.inputRef}` read from context.

## 191. Updater-Function Actions
- Type `update` as taking an updater, `(state) => state`.
- Why: providers built on `setState` or on a store can both satisfy it.
- Incorrect: a field-specific setter like `setInput`; correct: `update((s) => ({ ...s, input: text }))`.

## 192. Nullable Typed Context
- Create the context with an explicit type and a `null` default, for example `createContext<ComposerContextValue | null>(null)`.
- Why: the contract is typed and missing providers are detectable.
- Incorrect: an untyped context with a fake default value; correct: a typed interface with `null` until a provider supplies it.

# Part 31 — Variants over Boolean Props

## 193. Explicit Variant Components
- Create a named component per variant instead of one component with modes.
- Why: the code documents itself and impossible states disappear.
- Incorrect: `<Composer isThread isEditing={false} showAttachments showFormatting={false} />`; correct: `<ThreadComposer channelId="abc" />`, `<EditMessageComposer messageId="xyz" />`, `<ForwardMessageComposer messageId="123" />`.

## 194. Each Variant Declares Provider, UI and Actions
- A variant states which provider or state it uses, which UI parts it includes and which actions are available.
- Why: there are no boolean combinations to reason about.
- Incorrect: behavior inferred from a set of flags; correct: `EditMessageComposer` wraps `EditMessageProvider` and renders `Composer.CancelEdit` and `Composer.SaveEdit`.

## 195. Variants Still Share Parts
- Variants are self-contained but built from shared subcomponents.
- Why: you get explicit variants without duplicating implementation.
- Incorrect: copy-pasting a full input into each variant; correct: every variant reusing `Composer.Input` and `Composer.Footer`.

# Part 32 — Children over Render Props

## 196. Prefer Children for Structure
- Use `children` for composition instead of `renderX` props.
- Why: children read naturally and need no callback signatures.
- Incorrect: `renderHeader={() => <CustomHeader />}` and `renderFooter={() => …}`; correct: `<Composer.Frame><CustomHeader /><Composer.Input />…</Composer.Frame>`.

## 197. Render Props Only to Pass Data Back
- Use a render prop when the parent must hand data or state to the child.
- Why: this is the one case where a callback adds something children cannot.
- Incorrect: a render prop for static layout; correct: `renderItem={({ item, index }) => <Item item={item} index={index} />}` on a list.

## 198. Frames Accept Children
- Layout parts such as `ComposerFrame` and `ComposerFooter` just take `children: React.ReactNode` and render them.
- Why: consumers decide what goes inside without new props.
- Incorrect: a footer with `showEmojis` flags; correct: `<Composer.Footer>` wrapping whichever parts the consumer passes.

# Part 33 — Modern React APIs

## 199. Ref as a Regular Prop
- In React 19 and later, accept `ref` as an ordinary prop; no `forwardRef` wrapper.
- Why: component definitions get simpler and stay plain functions.
- Incorrect: `forwardRef<TextInput, Props>((props, ref) => …)`; correct: `function ComposerInput({ ref, ...props }: Props & { ref?: React.Ref<TextInput> })`.

## 200. use() Instead of useContext()
- In React 19 and later, read context with `use(MyContext)` instead of `useContext(MyContext)`.
- Why: `use()` can be called conditionally, unlike `useContext()`.
- Incorrect: `const value = useContext(MyContext)`; correct: `const value = use(MyContext)`.

## 201. Context as Provider
- In React 19 and later, render the context directly as the provider, for example `<ComposerContext value={{ state, actions, meta }}>`.
- Why: it removes the `.Provider` indirection.
- Incorrect: relying on extra wrapper boilerplate; correct: `<ComposerContext value={…}>{children}</ComposerContext>`.

## 202. Version Gate
- Apply these API changes only on React 19 or later; skip them on React 18 or earlier.
- Why: older versions do not support ref-as-prop or `use()`.
- Incorrect: removing `forwardRef` in a React 18 codebase; correct: keeping it until the upgrade.

# Part 34 — Native UI Feel

## 203. Native Dropdown Menus
- Rule: build dropdowns with the platform's native menu (cross-platform via `zeego/dropdown-menu`), never a hand-rolled JS menu.
- Why: native menus come with built-in accessibility, behave the way users expect on each platform, and perform better than an absolutely positioned overlay.
- Incorrect: a `useState(open)` toggle that renders a `View` with `position: 'absolute', top: 40` holding `Pressable` rows.
- Correct: `DropdownMenu.Root` > `Trigger` (wrapping the button) + `Content` > `Item` with `ItemTitle` and `onSelect`.
- Destructive actions such as Delete are flagged with the `destructive` prop on the item, so the platform styles them as dangerous rather than relying on custom red text.

## 204. Native Context Menus
- Rule: long-press actions use a native context menu (`zeego/context-menu`), not a custom popover.
- Why: users already know the long-press gesture, preview, and dismissal behaviour of system context menus; a JS imitation feels foreign and is less accessible.
- Correct structure: `ContextMenu.Root` > `Trigger` (the long-pressable content, e.g. a `View` with `padding: 20`) + `Content` > `Item` (Copy, Paste) with `ItemTitle`.

## 205. Menu Checkbox Items and Submenus
- Rule: toggles and nested options inside menus use the native menu primitives rather than custom rows.
- Checkbox: `DropdownMenu.CheckboxItem` with `value` and `onValueChange` (toggle via `prev => !prev`) plus `ItemIndicator` to show the native checkmark.
- Submenu: `DropdownMenu.Sub` > `SubTrigger` ("More Options") + `SubContent` with nested items (Settings, Help).
- Why: native check indicators and cascading submenus match system conventions and keep accessibility semantics intact.

## 206. Native Modals Over JS Bottom Sheets
- Rule: present sheets with the native `<Modal presentationStyle="formSheet" animationType="slide">` instead of JS-based bottom sheet libraries.
- Why: native sheets give swipe-to-dismiss, correct keyboard avoidance, accessibility, and UI-thread performance out of the box; low-level primitives should come from native UI.
- Incorrect: a JS `BottomSheet` driven by a ref with `snapPoints={['50%', '90%']}` and `sheetRef.current?.expand()`.
- Correct: a `visible` boolean in state, `onRequestClose={() => setVisible(false)}` to support system dismissal.

## 207. Navigator Form Sheets
- Rule: when a sheet is a route, use the navigator's native form sheet presentation.
- Correct: screen options `presentation: 'formSheet'` with `sheetAllowedDetents: 'fitToContents'` so the sheet sizes itself to its content.
- Why: the sheet inherits native detents, gestures, and transitions without custom snapping logic.

## 208. Pressable Over Touchables
- Rule: never use `TouchableOpacity` or `TouchableHighlight`; use `Pressable`.
- Why: `Pressable` is the modern, more flexible press API; legacy touchables bake in a fixed fade (e.g. `activeOpacity={0.7}`) and are being phased out.
- Impact: LOW, but it is a consistency rule for every tappable surface.

## 209. Gesture-Handler Pressable Inside Lists
- Rule: inside scrollable lists, use `Pressable` from `react-native-gesture-handler`, paired with the gesture-handler `ScrollView`.
- Why: both participate in the same gesture system, so taps and scrolls are coordinated and rows do not fire accidentally while the user is flicking.
- For animated press feedback (scale, opacity), do not use Pressable's style callback; use a tap gesture with shared values instead (see Animation & Gestures).

## 210. Native Stack Navigation
- Rule: stacks use the native stack (`createNativeStackNavigator`, or the router's default `Stack`, which is native); avoid the JS `createStackNavigator`.
- Why: native stacks are built on platform APIs (UINavigationController on iOS, Fragment on Android), so push/pop transitions and swipe-back gestures run on the UI thread and feel exactly like the platform.
- Impact: HIGH.

## 211. Native Bottom Tabs
- Rule: tabs use a native tab bar (native bottom tabs navigator or the router's `NativeTabs`); avoid the JS `createBottomTabNavigator` whenever native feel matters.
- Icons use platform symbol names: SF Symbols on iOS (`sfSymbol: 'house'`, `'gear'`, or `sf='house.fill'`) and Material names on Android (`md='home'`, `md='settings'`).
- Native tab structure: `NativeTabs.Trigger name='index'` containing `Trigger.Label` and `Trigger.Icon`.
- Why: system integration comes free: scroll-to-top on re-tapping a tab, picture-in-picture avoidance, proper safe areas, and platform accessibility.

## 212. Native Header Options Over Custom Headers
- Rule: configure headers through native options (`title`, `headerLargeTitleEnabled: true`, `headerSearchBarOptions: { placeholder: 'Search' }`) rather than replacing them with `header: () => <CustomHeader />`.
- Why: native headers give iOS large titles, integrated search bars, blur effects, and correct safe area handling automatically; a custom header loses all of it.
- Platform behaviour expected: iOS large titles, Android Material design.

## 213. Lightbox Galleries
- Rule: tap-to-fullscreen image viewing uses a native lightbox (Galeria) instead of a custom `Modal` showing a full-screen `Image`.
- Why: users expect native shared-element transitions from thumbnail to full screen, pinch-to-zoom, double-tap zoom, and pan-to-close; a plain modal gives none of these.
- Structure: wrap thumbnails in `Galeria urls={urls}` and each one in `Galeria.Image index={index}`; works with any image component.
- A single image (e.g. an avatar) still uses the same pattern with `urls={[url]}`.

## 214. Low-Res Thumbnails, High-Res Fullscreen
- Rule: show low-resolution images in the grid and pass the high-resolution URLs to the lightbox (`Galeria urls={highResUrls}` while mapping `lowResUrls`).
- Why: the grid stays light and fast, while the fullscreen view is crisp when the user zooms.

## 215. Gallery Grids in Virtualized Lists
- Rule: large photo grids wrap a virtualized list inside the lightbox container.
- Values: `numColumns={3}`, `estimatedItemSize={100}`, each cell wrapped in `Galeria.Image index={index}`.
- Why: only visible thumbnails mount while preserving the native open/close transition.

## 216. Optimized Image Component
- Rule: use `expo-image` (or a cross-platform wrapper built on it) instead of the core `Image`.
- Why: memory-efficient caching, placeholders, progressive loading, and better list performance mean fewer blank flashes and less memory pressure.
- Key props: `contentFit` (`cover`, `contain`, `fill`, `scale-down`), `recyclingKey` for list recycling.
- Impact: HIGH.

## 217. Image Placeholders and Fade-In
- Rule: give images a placeholder and a short fade-in so content does not pop in.
- Values: `placeholder={{ blurhash: '...' }}` (a blurhash string or thumbnail), `contentFit="cover"`, `transition={200}` (fade duration in ms).
- Why: a blurred preview signals content is coming and the 200 ms fade softens the swap.

## 218. Image Priority and Caching
- Rule: set loading priority and cache policy by importance.
- Values: `priority` is `low`, `normal`, or `high` (hero images use `high`); `cachePolicy` is `memory`, `disk`, `memory-disk`, or `none` (hero uses `memory-disk`).
- Why: what the user sees first loads first, and revisited images appear instantly.

# Part 35 — Animation & Gestures

## 219. Animate Only Transform and Opacity
- Rule: never animate `width`, `height`, `top`, `left`, `margin`, or `padding`; animate `transform` (translate, scale, rotate) and `opacity` only.
- Why: layout properties force layout recalculation on every frame, which drops frames; transform and opacity are GPU-accelerated and skip layout entirely.
- Everything other than transform and opacity triggers layout.
- Impact: HIGH.

## 220. Collapsing Panels via Scale
- Rule: expand/collapse by animating `scaleY` (0 to 1) with a fixed height and a top origin, plus opacity, rather than animating `height` from 0 to 200.
- Values: container `height: 200`, `transformOrigin: 'top'`, `scaleY: withTiming(expanded ? 1 : 0)`, `opacity: withTiming(expanded ? 1 : 0)`.
- Incorrect: `height: withTiming(expanded ? 200 : 0)` with `overflow: 'hidden'`.

## 221. Slide-In via Translate
- Rule: entrances slide with `translateY` and fade with opacity.
- Values: `translateY: withTiming(visible ? 0 : 100)`, `opacity: withTiming(visible ? 1 : 0)`.
- Why: smooth, GPU-only motion with no layout thrash.

## 222. UI-Thread Press Feedback
- Rule: animated press states (scale, opacity on press) use `GestureDetector` with `Gesture.Tap()` and shared values, not Pressable's `onPressIn`/`onPressOut`.
- Why: gesture callbacks run on the UI thread as worklets, so feedback is instant with no JS-thread round trip; JS callbacks lag when the JS thread is busy.
- Pattern: `onBegin` sets `pressed` to `withTiming(1)`, `onFinalize` sets it to `withTiming(0)`, `onEnd` calls the action via `runOnJS(onPress)()`.
- Values: pressed scale interpolates `[0, 1]` to `[1, 0.95]` (a 5% shrink).
- Impact: MEDIUM.

## 223. Animate From State, Not Visual Output
- Rule: shared values hold the real state (`pressed`, `progress`, `isOpen`), not the visual output (`scale`, `opacity`, `translateY`); visuals are derived via `interpolate`.
- Incorrect: a `scale` shared value set to 0.95 / 1 directly.
- Correct: `pressed` 0/1, with `scale: interpolate(pressed.get(), [0, 1], [1, 0.95])`.
- Why: one source of truth can drive several effects (add opacity or rotation with another interpolation), debugging `pressed = 1` is clearer than `scale = 0.95`, and logic is reusable.
- Impact: HIGH.

## 224. Derived Animated Values
- Rule: when one animated value is computed from another, use `useDerivedValue` (e.g. `opacity = useDerivedValue(() => 1 - progress.get())`) instead of `useAnimatedReaction` writing into a second shared value.
- Why: derived values are declarative, track dependencies automatically, and return a usable value.
- Impact: MEDIUM.

## 225. Reactions Are for Side Effects
- Rule: reserve `useAnimatedReaction` for effects that produce no value: triggering haptics, logging, calling `runOnJS`.
- Why: keeps derivation and side effects separate so animations stay predictable.

## 226. Shared Value Accessors
- Rule: read and write shared values with `.get()` and `.set()` rather than `.value` when the React Compiler is enabled.
- Why: the compiler cannot track property access; `.value` opts the component out of compiler optimisation and can behave incorrectly.
- Incorrect: `count.value = count.value + 1`. Correct: `count.set(count.get() + 1)`.
- Impact: LOW.

# Part 36 — Lists & Scrolling Performance

## 227. Virtualize Every List
- Rule: use a list virtualizer (LegendList or FlashList) instead of a `ScrollView` with mapped children, even for short lists.
- Why: virtualizers mount only visible items, cutting memory and mount time; a ScrollView renders everything upfront.
- Values: 50 items in a ScrollView means 50 components mounted when only 10 are visible; a virtualizer keeps about 10–15 mounted.
- Applies to any scrollable screen: profiles, settings, feeds, search results. Default to virtualization.
- Also give the list an `estimatedItemSize` (e.g. `80`) and a `keyExtractor` returning a stable `item.id`.
- Why: accurate estimates reduce blank areas and jumps while scrolling fast.

## 228. Stable Data References
- Rule: do not `map` or `filter` data into new objects before passing it to a virtualized list.
- Why: virtualization relies on object reference stability; new references re-render every visible item. In a search screen, mapping per keystroke re-renders the entire list on each key press.
- Correct: pass the raw stable array (`data={tlds}`) and transform inside each item.
- Impact: CRITICAL.

## 229. New Arrays With Stable Items Are Fine
- Rule: creating a new array is acceptable when its inner objects keep their identity, e.g. `tlds.toSorted((a, b) => a.name.localeCompare(b.name))`.
- Why: the list compares item references, so sorting without cloning items does not force a full re-render.

## 230. Let Items Select Their Own Dynamic Data
- Rule: instead of the parent passing fast-changing values (like a search keyword) to every row, each item reads just what it needs through a store selector (e.g. `useStore(s => s.keyword + '.' + tld.name)`).
- Why: the parent does not re-render on every keystroke; only visible items (about 20) update.
- Per-item conditional state (e.g. "is favorited") is read inside the item (`s.favorites.has(tld.id)`), so toggling one favorite re-renders one component.
- With the React Compiler, reading Context directly inside items is acceptable, slightly slower than a selector but usually negligible.

## 231. No Inline Objects in renderItem
- Rule: never build new objects inside `renderItem` as props, e.g. `user={{ id, name, avatar }}` or `style={{ backgroundColor: item.isActive ? 'green' : 'gray' }}`.
- Why: inline objects create new references each render and break memoization, so every row re-renders.
- Correct: pass `item` directly, or pass primitives and derive the style inside the memoized child (`style={[styles.row, { backgroundColor }]}`).
- Impact: HIGH.
- Static variants: define style variants once at module scope (`activeStyle`, `inactiveStyle`) and choose between them per item.
- Why: stable references let memoized rows skip re-rendering.

## 232. Primitive Props for Memoized Rows
- Rule: pass strings, numbers, and booleans to list items (`id`, `name`, `email`) rather than whole objects.
- Why: `memo()` compares by shallow reference; primitives make the comparison reliable, so rows re-render only when a real value changes.
- With the React Compiler, `memo()` and `useCallback()` are unnecessary, but reference stability still matters.
- Impact: HIGH.

## 233. Pass Only the Fields Used
- Rule: give each row only what it renders (`name`, `avatarUrl`), not the entire item.
- Why: fewer props means fewer reasons to re-render.

## 234. Hoisted Callbacks Keyed by ID
- Rule: create one callback at the list root and have items call it with their ID, or pass the `id` and build the handler inside the memoized child; never write `onPress={() => handlePress(item.id)}` inline in `renderItem`.
- Why: per-render closures defeat memoization and cause extra re-renders.

## 235. Lightweight List Items
- Rule: list items are simple render functions: no queries or data fetching, no expensive computation, minimal `useState`/`useEffect`, limited Context.
- Why: virtualized lists render many items during scroll; heavy items cause jank.
- Correct: the parent fetches once and passes pre-computed primitives (`name`, `price`, `imageUrl`).
- Prefer store selectors over Context, since Context re-renders a row when any value in it changes.

## 236. Set Lookups for Membership
- Rule: check membership with `Set.has` (the Set created once at the root) instead of `Array.includes()` inside every row.
- Why: constant-time checks keep per-row work tiny during scroll.

## 237. Right-Sized Images in Lists
- Rule: always load compressed, appropriately sized images in lists, at 2x the display size for retina.
- Values: a 100x100 thumbnail requests a 200x200 image (`?w=200&h=200&fit=cover`), never a 4000x3000 original.
- Why: full-resolution images consume excessive memory and cause scroll jank.
- Use an image component with caching and placeholder support.
- Impact: HIGH.

## 238. Item Types for Mixed Lists
- Rule: in lists with different layouts (headers, messages, images), give each item a `type`, provide `getItemType={(item) => item.type}`, and render a dedicated component per type via a switch.
- Why: items share recycling pools only with their own type, so a header is never recycled into an image cell; this avoids layout thrashing and lets TypeScript narrow each branch.
- Incorrect: one component branching on optional fields such as `isHeader` or `imageUrl`.
- Impact: HIGH.
- Size estimates: use `getEstimatedItemSize` keyed on item type for accurate estimates.
- Values: header 48, message 72, image 300, default 72.

## 239. Scroll Position Outside React State
- Rule: never store scroll position in `useState`.
- Why: scroll events fire rapidly; state updates re-render on every frame, causing render thrashing and dropped frames.
- Correct: a Reanimated shared value updated in `useAnimatedScrollHandler` (runs on the UI thread) for scroll-driven animation, or a `useRef` for non-reactive tracking.
- Impact: HIGH.

## 240. Scroll Event Throttle
- Rule: use `scrollEventThrottle={16}` (about one event per 60 fps frame).
- A higher number performs better but fires less often; unset it only when precision matters more than performance.

# Part 37 — Safe Areas & Insets

## 241. Native Safe Area Insets on Scroll Views
- Rule: put `contentInsetAdjustmentBehavior="automatic"` on the root ScrollView instead of wrapping it in `SafeAreaView` or adding manual `paddingTop: insets.top`.
- Why: iOS handles safe areas natively, including dynamic ones (keyboard, toolbars), with no layout shift, and content can scroll naturally behind the status bar.
- Impact: MEDIUM.

## 242. Tab Screens Inset Automatically
- Rule: with native tabs on iOS, the first ScrollView at the root of each tab screen gets automatic content inset adjustment, so content scrolls correctly behind the translucent tab bar.
- Opt out with `disableAutomaticContentInsets` on the trigger only when needed.

## 243. contentInset for Dynamic Spacing
- Rule: when top or bottom space can change (keyboard, toolbars, dynamic content), use `contentInset={{ bottom: offset }}` instead of `contentContainerStyle={{ paddingBottom: offset }}`.
- Why: changing padding triggers a full layout recalculation; changing `contentInset` only adjusts scroll bounds without re-rendering content.
- For static spacing that never changes, padding is fine.
- Impact: LOW.

## 244. Align Scroll Indicators With Insets
- Rule: always pair `contentInset` with matching `scrollIndicatorInsets` (same values).
- Why: keeps the scroll indicator aligned with the visible content area instead of running under toolbars.

# Part 38 — Styling & Typography/Fonts

## 245. Continuous Corner Curves
- Rule: always add `borderCurve: 'continuous'` alongside `borderRadius` (e.g. `borderRadius: 12, borderCurve: 'continuous'`).
- Why: produces the smoother, squircle-style iOS corners rather than plain circular arcs.

## 246. Gap for Spacing Between Elements
- Rule: space siblings with `gap` on the parent (e.g. `gap: 8`) instead of `marginBottom: 8` on each child.
- Why: consistent rhythm, no stray trailing margin, and cleaner layouts.

## 247. Padding Within, Gap Between
- Rule: `padding` creates space inside a container; `gap` creates space between its children.
- Values: a typical container uses `padding: 16, gap: 12`.

## 248. Native CSS Gradients
- Rule: use `experimental_backgroundImage: 'linear-gradient(to bottom, #000, #fff)'` instead of a third-party gradient component.
- Why: native CSS gradient syntax with no extra dependency.

## 249. CSS Box Shadows
- Rule: use the `boxShadow` string syntax, e.g. `'0 2px 8px rgba(0, 0, 0, 0.1)'`, instead of legacy `shadowColor`/`shadowOffset`/`shadowOpacity` objects or Android `elevation: 4`.
- Why: one consistent, cross-platform shadow definition.

## 250. Hierarchy Through Weight and Color, Not Size
- Rule: avoid multiple font sizes; keep one size and express hierarchy with weight and grayscale color.
- Incorrect: title 18, subtitle 14, caption 12.
- Correct: title `fontWeight: '600'`, subtitle `color: '#666'`, caption `color: '#999'`.
- Why: limiting font sizes creates visual consistency.

## 251. Fonts Embedded at Build Time
- Rule: embed custom fonts natively at build time (via the font config plugin) instead of loading them at runtime with `useFonts` or `Font.loadAsync`.
- Why: fonts are available at launch, with no loading state, no blank screen while `fontsLoaded` is false, and no flash of fallback text. Text simply uses `fontFamily: 'Geist-Bold'`.
- Requires a native rebuild after adding fonts.
- Impact: LOW.

## 252. Stylesheet-Based Styling
- Rule: define styles with `StyleSheet.create` or a utility-class system (Nativewind) rather than ad hoc inline objects.
- Why: centralised, stable style references keep design consistent and avoid needless re-renders.

# Part 39 — Design System Structure

## 253. Compound Components Over Polymorphic Children
- Rule: components that combine a container with text and icons are built as compound parts: `Button`, `ButtonText`, `ButtonIcon`.
- Incorrect: a `Button` accepting `children: string | ReactNode` plus an `icon` prop and checking `typeof children === 'string'` to wrap it in `Text`.
- Correct: `<Button><ButtonIcon><SaveIcon /></ButtonIcon><ButtonText>Save</ButtonText></Button>` and `<Button><ButtonText>Cancel</ButtonText></Button>`.
- Why: usage is explicit and composable, with no ambiguity about how content will render.
- Impact: MEDIUM.

## 254. Only Text Components Accept Strings
- Rule: a component may receive a string child only if it is a dedicated `*Text` component; containers never accept raw strings.
- Why: mirrors the platform rule that strings must live in `Text`, which prevents crashes and keeps typography consistent.

## 255. Import Primitives Through the Design System
- Rule: re-export primitives and third-party components (`View`, `Text`, `Button`) from a local components folder, and have app code import only from there (e.g. `@/components/view`).
- Why: one place to change appearance or implementation globally and to refactor without touching app screens.
- Start with plain re-exports; customise later without changing app code.
- Impact: LOW.

## 256. Narrow Wrapper Props
- Rule: when wrapping a primitive, ideally expose only the props you intend to support (e.g. `Pick<ViewProps, 'style' | 'children'>`).
- Why: keeps control over the implementation and stops app code depending on every underlying prop.

## 257. Dependency Hygiene
- Native dependencies must be declared directly by the app that ships them, and each dependency uses a single exact version across all packages (no `^` or `~`).
- Why: missing native declarations break native linking, and mixed versions cause duplicate code, runtime conflicts, and inconsistent behaviour.

# Part 40 — State & Rendering Correctness

## 258. Strings Live Inside Text
- Rule: every string must be rendered inside `<Text>`; a string as a direct child of `<View>` (e.g. `<View>Hello, {name}!</View>`) crashes.
- Why: the error "Text strings must be rendered within a <Text> component" is a hard crash.
- Impact: CRITICAL.

## 259. No Falsy && in JSX
- Rule: never write `{value && <Component />}` when `value` could be `""` or `0`.
- Why: those falsy values are renderable, so the app tries to render them as text outside `<Text>` and crashes in production.
- Correct: a ternary with `null` (`{count ? <Text>…</Text> : null}`), explicit boolean coercion (`!!count &&`), or explicit checks like `count > 0`.
- A lint rule that catches leaked renders (`react/jsx-no-leaked-render`) can enforce this automatically.
- Impact: CRITICAL.
- Prefer early returns (`if (!name) return null`) as the clearest form of conditional rendering; use a ternary or explicit boolean inline.

## 260. Minimal State, Derived Values
- Rule: keep the fewest state variables possible; compute anything derivable during render.
- Incorrect: `total` and `itemCount` in state synced via `useEffect`; storing `fullName` alongside `firstName` and `lastName`.
- Correct: `total = items.reduce(...)`, `itemCount = items.length`, `fullName = \`${firstName} ${lastName}\``.
- Why: redundant state causes extra re-renders and can drift out of sync, showing users stale numbers.
- Impact: MEDIUM.

## 261. State Represents Ground Truth
- Rule: React state stores the real condition (`isExpanded`), and visual values are derived (`height = isExpanded ? 200 : 0`), never synced into separate state with an effect.
- Why: a single source of truth makes logic cleaner and debugging easier.

## 262. Fallback State Instead of Initial State
- Rule: initialise user-editable state as `undefined` and resolve with `??` against the prop or server value (`const enabled = _enabled ?? fallbackEnabled`).
- Why: state represents user intent only; `undefined` means "the user hasn't chosen yet". The control keeps reflecting the default or server value as it changes (including after a refetch), and once the user interacts, their choice persists.
- Incorrect: `useState(defaultValue)`, which freezes the first value and goes stale.
- Impact: MEDIUM.

## 263. Updater Functions for Dependent State
- Rule: when the next state depends on the current one, use `setState(prev => ...)` (e.g. `setCount(prev => prev + 1)`) instead of reading the state variable in a callback.
- Why: avoids stale closures, so rapid taps are not lost.

## 264. Skip Re-Renders by Returning Previous State
- Rule: for object state (like `{ width, height }`), compare inside the updater and return `prev` when nothing changed.
- Why: returning the previous value skips the re-render.
- For primitive state, set the value directly; no comparison is needed.

## 265. Measuring Views
- Rule: measure synchronously in `useLayoutEffect` for the initial size (`getBoundingClientRect()` on newer versions, `measure()` on older ones) and keep it current with `onLayout`.
- Why: the size is available before the first paint (no layout jump), and later changes are tracked.
- Use a dispatch updater in `onLayout` for non-primitive sizes so unchanged dimensions do not re-render.

## 266. Destructure Functions Early
- Rule: with the React Compiler, destructure functions at the top of render (`const { push } = useRouter()`, `function SaveButton({ onSave })`) rather than dotting in (`router.push`, `props.onSave`).
- Why: the compiler keys its cache on the referenced values; whole objects change each render and break memoization, while destructured functions are stable.
- Impact: HIGH.

## 267. Hoist Formatters
- Rule: create `Intl.NumberFormat`, `Intl.DateTimeFormat`, and `Intl.RelativeTimeFormat` once at module scope when locale and options are static; memoize them on `locale` when the locale is dynamic.
- Why: each instantiation parses locale data and builds lookup tables, which is far more expensive than plain objects; rebuilding them in render or loops slows lists of prices and dates.
- Common hoisted formatters: currency (`style: 'currency', currency: 'USD'`), `dateStyle: 'medium'`, `timeStyle: 'short'`, `style: 'percent'`, relative time with `numeric: 'auto'`.
- Impact: LOW-MEDIUM.

# Part 41 — Performance Priorities

## 268. Impact Scale
- CRITICAL: highest priority; violations cause crashes or broken UI.
- HIGH: significant performance improvements.
- MEDIUM: moderate performance improvements.
- LOW: incremental improvements.

## 269. Critical Priorities
- Core rendering: strings inside `Text`, and no falsy `&&` in JSX (crash prevention).
- Stable object references for virtualized lists.
- Native dependencies declared where the app's native linking can find them.

## 270. High Priorities
- List performance: virtualization, inline-object avoidance, primitive props, lightweight items, compressed images, item types.
- Animation: transform and opacity only.
- Scroll: never track scroll position in React state.
- Navigation: native stacks and tabs.
- Native menus and native modals, and the optimized image component.
- Ground-truth state and early function destructuring under the compiler.

## 271. Medium Priorities
- State management: minimal state, fallback state, updater functions.
- Derived animated values and UI-thread press gestures.
- Safe areas via content inset adjustment, view measurement, modern styling, lightbox galleries, compound components, single dependency versions.

## 272. Low Priorities
- Pressable over touchables, `contentInset` for dynamic spacing, `.get()`/`.set()` shared value accessors.
- Design-system import folder, build-time fonts, and hoisted formatters (LOW-MEDIUM).

# Part 42 — Performance Doctrine

## 273. Measure Before You Optimize
- Start every performance effort from real observed signals (traffic, latency, errors, real-user vitals), never from a hunt for known anti-patterns.
- Advice not tied to observed traffic or user pain produces noisy, low-impact changes; drop it.
- Investigate only the route or component the signal points at; do not widen the search to compensate for a vague question.
- Fixes on routes with no traffic are dropped unless the issue affects every request equally (build config, global scripts, request interceptors, raw script tags).

## 274. Mechanical Thresholds Over Judgment
- Decide what to investigate with explicit, repeatable thresholds, not gut feel.
- The same input signals must always produce the same list of targets.
- Publish what was considered and skipped, with the exact reason (e.g., "cache hit rate above threshold", "95th percentile already healthy"); this is the trust mechanism.

## 275. Fewer, Evidence-Backed Fixes
- A good review yields `5`–`15` recommendations, each tied to a specific route or file plus a specific metric.
- Every fix carries before/after code and a reference that matches the project's framework version.
- Never recommend features the installed framework version does not have.
- Long lists of fixes the team cannot act on are an anti-pattern; every item needs an evidence chain.

## 276. Precise Performance, Modest Promises
- Performance numbers stay precise because they are observed: "95th percentile duration is `1,240ms`".
- Frame expected gains as ranges anchored to the observed baseline: "from `850ms` toward `~250–400ms`".
- Never make an unanchored improvement claim or invent latency, traffic, or percentages.
- Prefer under-promising: if a helper's duration was not measured, do not promise a latency drop equal to it.

## 277. Scope of User-Perceived Performance
- Bundle size matters only when it shows up as user-facing slowness (LCP, INP) or startup latency; a large build output alone is not a target.
- Slow builds with no runtime impact are out of scope.
- High error rates are reliability problems, not performance tuning targets; route them separately.

# Part 43 — Core Web Vitals

## 278. Poor-Band Thresholds
- Measure at the `p75` of real-user traffic per route.
- LCP is poor above `2500ms`.
- INP is poor above `200ms`.
- CLS is poor above `0.1`.
- Require a meaningful sample (more than `50` real-user measurements) before acting.
- Poor vitals hurt both search ranking and conversion.

## 279. One Metric, One Fix
- Treat each (route, metric) pair as its own problem; LCP, INP, and CLS have different causes and fixes.
- Never ship a generic "improve Web Vitals" recommendation.
- Do not optimize a metric that is not poor on that route.
- State the poor `p75` value and the exact mechanism behind it.

## 280. Diagnosing LCP
- LCP above `2500ms` usually means slow server response or a slow critical image.
- First determine whether the LCP element is an image before touching unrelated JavaScript.
- Check server response time (TTFB) and critical media together.

## 281. Diagnosing INP
- INP above `200ms` usually means long tasks or heavy JavaScript running on interaction.
- Inspect heavy client bundles, interaction handlers, and third-party scripts on the route.

## 282. Diagnosing CLS
- CLS above `0.1` is usually caused by images without dimensions, ads/embeds, injected UI, or fonts.
- Check reserved dimensions first, then fonts, then late-injected content.

## 283. No Data, No Claims
- When real-user vitals are missing for the window, make no claims about LCP, INP, or CLS; list it as a data gap.

# Part 44 — Images & LCP

## 284. Hero Image Priority
- Give the single most likely LCP image explicit priority (preload or high fetch priority).
- Never preload multiple candidate LCP images; it splits bandwidth and slows all of them.
- Use the current priority mechanism for your framework version; deprecated props may silently stop working.

## 285. Responsive Sizing
- Every fluid/fill image must declare `sizes` so mobile does not download desktop pixels.
- Never serve a hero at native resolution (e.g., a `4MP` image) to every viewport; responsive `sizes` is mandatory.
- Avoid oversized intrinsic dimensions relative to the rendered slot.

## 286. Optimize Real Photos, Not UI Glyphs
- Route photographs and content images (heroes, product shots, author photos, inline post images, social preview images) through an optimizing image component for modern format negotiation (WebP/AVIF).
- Never send tiny icons, SVG UI assets, or animated GIFs through image optimization just because they are images.
- Raw `<img>` tags for large catalogs of product variants are a top anti-pattern.

## 287. Source Freshness of Images
- Do not change image quality or cache TTL without checking how and when source images are updated.
- Do not change remote-source policy without reviewing the existing configuration.

## 288. Reserve Image Space
- Always give images explicit dimensions or aspect ratios so they do not shift layout when they load.

# Part 45 — Fonts & Layout Shift

## 289. Self-Host Fonts
- Self-host fonts through a build-time font loader to eliminate the third-party request, invisible-text flashes (FOIT), unstyled-text flashes (FOUT), and the layout shift that follows.
- Avoid external font stylesheet links and late-loading font classes that swap text after render.

## 290. Fix the Actual Shift Source
- Only migrate fonts when the route actually loads external font CSS or swaps text after render.
- Do not migrate fonts when CLS is caused by images, ads, embeds, or injected UI.
- Name the CLS value, the font-loading mechanism, and the exact line responsible.

## 291. Injected Content
- Ads, embeds, cookie banners, and personalization widgets must reserve their space up front or render outside the content flow.

# Part 46 — Heavy UI & Lazy Loading

## 292. Split Rarely Used UI
- Load heavy or rarely used UI on interaction, on viewport entry, or on route entry rather than in the first bundle.
- Typical candidates: menus, search overlays, personalization widgets, maps, rich editors, and large imported libraries.
- Target concrete route-local components, not generic "reduce bundle" advice.

## 293. Never Defer Essential Content
- Do not lazy-load above-the-fold content needed for initial meaning or accessibility.
- Do not disable server rendering for content that must appear in the initial HTML.

## 294. Keep Interactivity at the Leaves
- Mark only the interactive leaf (button, form, drawer) as client-side; keep the surrounding page server-rendered.
- A whole page hydrated for one interactive widget inflates JavaScript and hurts INP.

# Part 47 — Third-Party Scripts

## 295. Prove the Script Is the Problem
- Act on a third-party script only when it lines up with the poor metric and route.
- Show the specific script blocking critical rendering, hydration, or interaction.

## 296. Load After Hydration
- Defer analytics, chat widgets, marketing pixels, and tag managers until after hydration or idle.
- None of them should block LCP.
- Prefer route-local loading over global loading for scripts only one page needs.

## 297. Avoid Script Waterfalls
- Never chain multiple analytics services so each waits on the previous one; load them in parallel after hydration.
- Replace some client-side trackers with server-side event tracking where possible.

## 298. Consent Banners Without Blocking Paint
- Never render a consent banner synchronously in the document head.
- Render it after hydration and persist consent state with a tiny inline script.

## 299. Protect Required Scripts
- Do not delay required bot detection, consent, auth, or payment scripts without product evidence that it is safe.

# Part 48 — Static Shells & Streaming

## 300. Static Shell, Dynamic Holes
- Keep a static shell that renders instantly and move dynamic data behind explicit cached or runtime boundaries.
- Stream expensive widgets in behind loading boundaries; the shell renders fast and widgets fill in.
- Streaming shifts perceived latency even when the underlying queries are unchanged.

## 301. Avoid Accidental Dynamic Rendering
- Treat dynamic rendering as a bug unless it is required; first prove the page can be static, periodically regenerated, or partially static.
- Forced-dynamic flags left over from development (e.g., on a storefront homepage or blog index) are a common trap.
- A dynamic call in a shared layout makes the entire route tree beneath it dynamic.
- Keep dynamic rendering for auth, personalization, draft/preview mode, per-request redirects, and request-specific data.

## 302. Dedupe Across Boundaries
- Identical cached calls in separate loading boundaries on the same render may each re-execute; hoist the shared promise to the page level or use a cross-request cache.
- Skip deduping when calls differ in parameters or intent.

## 303. Layout-Level Blocking
- Never put user/auth loading in a shared layout when most child routes do not read the user; every child waits on it.
- Push user-specific loads into the routes that need them.

## 304. Streaming Endpoints
- Long wall-clock time on a streaming or resumable endpoint is often just a live client connection, not a bug.
- Do not cache stream endpoints or remove resumability.
- Real waste on streams: full replay instead of resuming from the last index, missing tail index, unreleased locks, unclosed streams, high CPU, or avoidable work before the first byte.

# Part 49 — Data Freshness vs Speed

## 305. Safety Before Shared Caching
- Only public, cacheable GET responses may be shared-cached.
- Rule out cookies, sessions, authorization headers, draft state, and user-specific data first.
- Never cache mutations, dashboards, account data, carts, checkout, or anything that varies per viewer.
- Never mix `private` with shared-cache directives.
- Every cache policy names mechanism, scope, TTL/freshness, and `Vary`.

## 306. Stale-While-Revalidate Defaults
- Public GET APIs: `Cache-Control: public, s-maxage=<seconds>, stale-while-revalidate=<longer>`.
- Example API policy: `s-maxage=300, stale-while-revalidate=86400`.
- Marketing pages: `s-maxage=86400, stale-while-revalidate=604800` (warm for `24h`, stale-serve for a week).
- Cache hits can drop latency from `850ms` toward `~50ms`.

## 307. Regeneration Cadence
- Prerender everything that can be prerendered.
- Docs: start around `revalidate: 3600` (hourly); blog index: around `60s`.
- Catalog pages: `60s`–`3600s`.
- CMS-driven content should revalidate on a publish webhook, not on every request or a very short timer.
- If regeneration writes exceed half of reads (`writes/reads > 0.5`), the cadence is too aggressive; lengthen it or switch to on-demand invalidation.

## 308. Freshness-Critical Data
- Never lengthen freshness windows for inventory, pricing, auth, drafts, or user-specific data without proof stale reads are acceptable.
- Never claim existing on-demand invalidation unless the matching invalidation call is verified; near-match tags do not count.

## 309. Stable Cached Output
- Never bake `new Date()`, `Date.now()`, or `Math.random()` into cached output; it forces a fresh regeneration every time even when data is unchanged.
- Replace with a build-time constant or compute it client-side after mount.

## 310. Replace Polling
- Do not poll the server for state from the client; replace with request-deduping data hooks plus on-demand revalidation triggered by the mutation that changes state.

# Part 50 — Critical Path & Server Latency

## 311. Slow-Route Thresholds
- A route is slow when `p95 > 500ms` at `>= 1,400` requests in the window.
- A route is catastrophically slow when `p95 > 1500ms` at `>= 250` requests.
- Routes with more than `50%` 5xx responses are reliability issues, not tuning targets.

## 312. Parallelize Independent Work
- Run independent awaits concurrently (`Promise.all`): e.g., user + org + billing + recent activity on a dashboard, or payment + inventory + tax in checkout.
- Sequential fan-out to several third parties for one user is the most common slow-endpoint shape.
- Never wrap dependent operations in a parallel call.
- Do not replace `Promise.allSettled` where partial-failure handling is intentional.

## 313. Never Parallelize Past an Auth Guard
- Do not run a private data fetch in parallel with the ownership or permission check that authorizes it.
- Instead, combine the guard and lookup into one query constrained by the authenticated user, tenant, or ownership key.

## 314. Slow Upstream APIs
- Flag an upstream host when `p75 > 2000ms` with `>= 500` calls in the window.
- Act only when the upstream is on a user route's critical path.
- Options: parallelize, cache shared results, trim payload, or move after the response.
- Do not blame your own runtime when the upstream owns the latency.

## 315. Response After, Side Effects Later
- Run analytics, logging, audit trails, notifications, and cache warming after the response is sent.
- Never defer work that decides the response, must fail the request, changes visible state synchronously, or needs a durable retry guarantee.

## 316. Long Jobs Off the Request Path
- Move image generation, PDF rendering, large reports, AI jobs, and multi-step batches to a background job; return a run ID and stream progress instead of blocking.

## 317. Wall Clock vs CPU
- When wall-clock latency is much higher than CPU time, the cause is waiting on I/O; inspect critical-path awaits before blaming rendering.

## 318. Per-Request Memoization and Query Shape
- Dedupe repeated data calls within a single request render.
- Eliminate N+1 queries in list pages; batch or join related records.
- Pool database connections; unpooled connections exhaust the database under load.

## 319. Cold Starts
- Cold starts add `200–800ms` per request on cache-miss paths.
- Treat cold starts as a real signal when more than `40%` of requests are cold at `>= 1,000` requests.
- Fix heavy module-scope initialization, top-level network calls, and heavy dependencies.
- Do not blame cold starts when warm requests are similarly slow; do not recommend keep-warm traffic without proof.
- Authenticated routes are more cold-start sensitive: every cold start is a user waiting.

## 320. Region Proximity
- Place compute near users and, on cache-miss paths, near the data source; proximity to data often wins.
- A misplaced region can add `100–300ms` TTFB.
- Do not expand to multiple regions without confirming the data layer is reachable without cross-region hops.

## 321. Payload Size
- Check response shape before only adding cache headers: unbounded JSON, large embedded objects, missing pagination.
- Measure payload claims in post-compression bytes.
- Only trim fields proven unnecessary for the response.

## 322. Request Interceptors
- Narrow global request interceptors to the paths that need them; heavy per-request hooks multiply latency across all traffic.
- Keep A/B variant assignment at the edge with a cached page per variant, not rendered per request.

# Part 51 — Reliability Users Feel

## 323. Error Thresholds
- Treat a route as erroring when errors exceed `250` or error rate exceeds `1%` at `>= 1,000` requests.
- Classify: app exception, timeout, payload limit, or deployment regression.
- Do not raise limits before proving the route needs more headroom.

## 324. Resilient Providers
- Critical-path features that depend on one external provider must have a fallback chain; a rate-limit from one provider otherwise becomes a user-visible outage.

## 325. Broken Links and 404s
- Investigate high-volume 404/catch-all traffic: legacy URLs, bots, or broken links.
- Do not replace a useful 404 page with a blanket rewrite or block legitimate routes without a log-only validation step.

## 326. Bot Protection Without Hurting Humans
- Recommend bot protection only with observed automated traffic (e.g., `>= 5%` bot share) or meaningful scale.
- Stage new rules from log, to challenge, to deny when false-positive risk is unproven.
- Never disable security protections to make things faster or cheaper.

# Part 52 — Performance by Site Type

## 327. AI Applications
- Stream responses and keep processes warm across requests.
- Configure an active-active fallback across model providers for critical-path agents.
- Never block the streamed response on tool-call logging or telemetry; run it after the response.
- Reuse sandboxes or sessions where isolation allows instead of creating fresh ones per request.

## 328. API Services
- Cache idempotent public GETs at the edge with `s-maxage` plus `stale-while-revalidate`.
- Rate-limit abusive clients at the edge before they reach application code.
- Parallelize external calls and independent auth/data loads.
- Move long-running work to background queues.

## 329. Content Sites
- Prerender all pages; regenerate on publish webhooks.
- Use responsive optimized images for every content image and self-hosted fonts.
- Prefetch links on hover or when visible.
- Render Markdown/MDX at build time, never per request.
- Serve search from a prebuilt index on the CDN, not a per-keystroke server query.

## 330. E-commerce
- Make catalog pages periodically regenerated (`60s`–`3600s`) with optimized product images.
- Keep cart and checkout dynamic but parallelize payment, inventory, and tax calls.
- Hydrate only the cart buttons and forms; stream the checkout shell and fill the cart drawer later.
- Keep webhooks off the user path; keep cart/auth state out of edge interceptors.

## 331. Marketing Sites
- Cache aggressively at the edge (`s-maxage=86400, stale-while-revalidate=604800`).
- Size hero images responsively; never ship native-resolution heroes to mobile.
- Defer all third-party JS post-hydration and keep consent banners off the critical path.
- Regenerate CMS sections (logos, testimonials, pricing tables) hourly or on webhook.
- Assign A/B variants at the edge with a cached static page per variant.

## 332. SaaS Dashboards
- Render the dashboard shell fast and stream expensive widgets behind loading boundaries.
- Load user, org, billing, and activity data in parallel; dedupe repeated queries per request.
- Run audit logs and analytics after the response.
- Replace client polling with deduped data hooks plus mutation-triggered revalidation.

## 333. Component-Framework Server Apps
- Prerender static routes and enable periodic regeneration on public consumer pages.
- Return independent promises from data loaders so they stream, or run them in parallel.
- Keep server request hooks light; move route-specific work into that route's loader.
- Use relative URLs for internal fetches during server rendering so they become direct calls.
- Avoid user loading in shared layouts that block every child route.
- Never regenerate dashboards, carts, checkout, account data, or drafts periodically.

# Part 53 — Communicating Recommendations

## 334. Recommendation Shape
- What: verb + change + scope, `<= 80` characters when feasible (e.g., "Add shared caching to /api/products").
- Why: `1`–`2` sentences stating the metric and code evidence with line numbers.
- Fix: numbered steps, each starting with a verb, with before/after code under `~20` lines each.
- Verify: name exactly which metric to re-check.
- Include a risk note when a change can serve stale data.

## 335. Lead With the Signal
- Open with the observed signal, the specific change, and how to verify it.
- Use observed numbers only; write "95th percentile", not "p95".
- Spell out internal shorthand ("Core Web Vitals", "performance", "requests").

## 336. Plain, Direct Voice
- Prefer "use" over "leverage", "reduce" over "optimize".
- Avoid hype words: seamlessly, effortlessly, powerful, robust, blazing, lightning-fast, cutting-edge, world-class, streamline, elevate, harness, empower, utilize.
- Avoid filler adverbs (just, simply, actually) and hedge openers (Consider, You may want to, It is important to note).
- Avoid "It's not X, it's Y" reframes and arrow symbols in prose.
- Use short bullets and tables; full sentences with punctuation.

## 337. Quality Floor
- Score each recommendation on specificity, actionability, grounding, and evidence (`0`–`1` each).
- Excellent `>= 0.85`; Good `0.70`–`0.85`; Fair `0.55`–`0.70`; Poor `< 0.55` is dropped.
- Quick wins: low effort with high priority (priority `> 40`).
- Cap account-level recommendations at `3`.

## 338. Report Transparency
- Include a "Not investigated" section listing every considered signal and why it was skipped.
- Include an "Investigated, no change recommended" section in plain language.
- Include strengths (what the project does well) and data gaps (what could not be measured).
- Observations must not contain implementation actions; they may only ask for narrower evidence (inspect logs, compare deployments, check headers).
- Frame missing prerequisites as engineering constraints: what the gap prevents and what to choose next, never as an upsell.

# Part 54 — Eliminating Waterfalls

## 339. Parallelize Independent Async Work
- Impact: CRITICAL for the whole part; waterfalls are the top performance killer because every sequential `await` adds a full network round trip. This rule itself yields 2-10× improvement.
- Rule: when async operations do not depend on each other, run them concurrently with `Promise.all()`.
- User-visible effect: pages and actions finish loading in one round trip instead of several, so content appears sooner.
- Incorrect: `await fetchUser()`, then `await fetchPosts()`, then `await fetchComments()` (3 round trips). Correct: `await Promise.all([fetchUser(), fetchPosts(), fetchComments()])` (1 round trip).

## 340. Dependency-Based Parallelization
- Impact: CRITICAL (2-10× improvement).
- Rule: when operations have partial dependencies, start each task at the earliest possible moment instead of grouping them into rigid sequential stages.
- User-visible effect: dependent data (e.g. a profile that needs a user id) loads alongside unrelated data rather than after it, cutting total wait time.
- Incorrect: `Promise.all([fetchUser(), fetchConfig()])` and then `await fetchProfile(user.id)`, so the profile waits on config for no reason. Correct: use a dependency-aware helper such as `better-all`'s `all({...})`, or create the promises up front (`profilePromise = userPromise.then(u => fetchProfile(u.id))`) and await them all together in one `Promise.all`.

## 341. Start Early, Await Late in Request Handlers
- Impact: CRITICAL (2-10× improvement).
- Rule: in API routes and server actions, kick off independent operations immediately, even before you need their results, and await them only where required.
- User-visible effect: shorter server response time for every request the UI makes.
- Incorrect: `await auth()`, then `await fetchConfig()`, then `await fetchData(session.user.id)` in sequence. Correct: create `sessionPromise` and `configPromise` right away, await the session, then `Promise.all([configPromise, fetchData(session.user.id)])`.

## 342. Defer Await Until Needed
- Impact: HIGH (avoids blocking unused code paths).
- Rule: move each `await` into the branch that actually uses its result, so early-return paths don't wait for data they ignore.
- User-visible effect: fast paths (skipped processing, not-found, validation errors) respond immediately.
- Incorrect: `await fetchUserData()` at the top, then `return { skipped: true }` without using it; or fetching permissions before checking whether the resource exists. Correct: check the skip/not-found condition first, then `await` only the data the remaining path needs.
- Most valuable when the skipped branch is taken often or the deferred operation is expensive.

## 343. Check Cheap Conditions Before Async Flags
- Impact: HIGH (avoids unnecessary async work when a synchronous guard already fails).
- Rule: in compound conditions like `flag && cheapCondition`, evaluate the cheap synchronous condition (local props, request metadata, loaded state) before awaiting the flag or remote value.
- User-visible effect: the cold path skips a network, feature-flag, or database call entirely, reducing latency.
- Incorrect: `const someFlag = await getFlag()` then `if (someFlag && someCondition)`. Correct: `if (someCondition) { const someFlag = await getFlag(); if (someFlag) ... }`.
- Keep the original order if the cheap condition is actually expensive, depends on the flag, or side effects must run in a fixed order.

## 344. Strategic Suspense Boundaries
- Impact: HIGH (faster initial paint).
- Rule: instead of awaiting data at the top of a page before returning markup, push the fetch into the component that needs it and wrap that component in `<Suspense fallback={<Skeleton />}>` so the shell renders and streams immediately.
- User-visible effect: sidebar, header and footer paint at once while only the data region shows a skeleton; the trade-off is possible layout shift when content replaces the fallback.
- Incorrect: `const data = await fetchData()` in `Page`, blocking the entire layout. Correct: an async `DataDisplay` component awaits its own data inside a Suspense boundary; or start `dataPromise = fetchData()` without awaiting and let several children read it with `use(dataPromise)` so only one fetch occurs.
- Don't use it for data that drives layout decisions, SEO-critical above-the-fold content, small fast queries where the overhead isn't worth it, or when avoiding a loading-to-content jump matters more than early paint.

# Part 55 — Bundle Size Optimization

## 345. Avoid Barrel File Imports
- Impact: CRITICAL for the whole part (smaller initial bundles improve Time to Interactive and Largest Contentful Paint); this rule costs 200-800ms of import time plus slow builds when ignored.
- Rule: import from the specific source module rather than from a barrel entry that re-exports everything.
- User-visible effect: faster cold starts and interactivity; popular icon and component libraries can have up to 10,000 re-exports, loading 1,500-2,200+ modules for a handful of components.
- Incorrect: `import { Check, X, Menu } from 'lucide-react'` loading the whole library. Correct: enable `optimizePackageImports` in the framework config so standard imports are rewritten to direct ones (keeps types and autocomplete), or use direct paths like `@mui/material/Button`.
- Gains cited: 15-70% faster dev boot, 28% faster builds, 40% faster cold starts, much faster hot reload. Watch for deep import paths that lack type definitions under strict TypeScript.
- Commonly affected: `lucide-react`, `@mui/material`, `@mui/icons-material`, `@tabler/icons-react`, `react-icons`, `@headlessui/react`, `@radix-ui/react-*`, `lodash`, `ramda`, `date-fns`, `rxjs`, `react-use`.

## 346. Dynamic Imports for Heavy Components
- Impact: CRITICAL (directly affects TTI and LCP).
- Rule: lazy-load large components that are not needed for the initial render.
- User-visible effect: the first screen becomes interactive sooner because heavy widgets (an editor of ~300KB, for example) are not in the main chunk.
- Incorrect: a static `import { MonacoEditor } from './monaco-editor'`. Correct: `dynamic(() => import('./monaco-editor').then(m => m.MonacoEditor), { ssr: false })`.

## 347. Prefer Statically Analyzable Paths
- Impact: HIGH (avoids accidental broad bundles and file traces).
- Rule: keep `import()` targets and file-system paths obvious at build time, using explicit maps of loader functions or literal paths at the call site.
- User-visible effect: smaller server bundles and better cold starts, so first responses arrive faster; also faster builds and lower memory use.
- Incorrect: `import(PAGE_MODULES[pageName])` where the map holds strings, or `path.join(process.cwd(), 'content/' + kind)`. Correct: a map of `() => import('./pages/home')` functions, and a branch that picks between literal `path.join(process.cwd(), 'content/blog')` and `'content/docs'`.
- Even a two-value variable hides the final path from static analysis and can widen output file tracing.

## 348. Conditional Module Loading
- Impact: HIGH (loads large data only when needed).
- Rule: load large modules or data sets only when the feature that uses them is activated.
- User-visible effect: users who never enable the feature never download it; those who do see a skeleton briefly while it loads.
- Incorrect: statically importing animation frames used by an optional player. Correct: in an effect, when `enabled && !frames`, call `import('./animation-frames.js')`, store the result, fall back gracefully on error, and render a `<Skeleton />` until ready.
- Guard with `typeof window !== 'undefined'` so the module is not bundled for server rendering.

## 349. Defer Non-Critical Third-Party Libraries
- Impact: MEDIUM (loads after hydration).
- Rule: analytics, logging and error-tracking don't block interaction, so load them after hydration.
- User-visible effect: the initial bundle is lighter and the page becomes interactive sooner.
- Incorrect: a static `import { Analytics }` rendered in the root layout. Correct: `dynamic(() => import(...).then(m => m.Analytics), { ssr: false })`.

## 350. Preload Based on User Intent
- Impact: MEDIUM (reduces perceived latency).
- Rule: start fetching a heavy bundle as soon as intent is signalled (hover, focus, or a feature flag turning on), before the click.
- User-visible effect: the feature opens almost instantly on click because its code is already downloaded.
- Incorrect: waiting until click to import the editor. Correct: `onMouseEnter` and `onFocus` call `void import('./monaco-editor')`; or an effect preloads when `flags.editorEnabled` becomes true.
- Guard with `typeof window !== 'undefined'` to keep preloaded modules out of the server bundle.

# Part 56 — Server-Side Performance

## 351. Authenticate Server Actions Like API Routes
- Impact: CRITICAL (prevents unauthorized access to server mutations); the server part overall is HIGH impact.
- Rule: server actions are public endpoints; verify authentication and authorization inside every action, and validate input, rather than relying on middleware, layouts or page guards.
- User-visible effect: protects user data and prevents unauthorized mutations triggered by direct calls.
- Incorrect: a `'use server'` `deleteUser` that deletes without any check. Correct: validate input with a schema, call `verifySession()`, reject if absent, check role or ownership, then mutate.

## 352. Parallel Data Fetching with Component Composition
- Impact: CRITICAL (eliminates server-side waterfalls).
- Rule: server components in a tree execute sequentially when a parent awaits before rendering children; restructure so sibling components each fetch their own data.
- User-visible effect: independent page regions load concurrently, shortening time to full content.
- Incorrect: `Page` awaits `fetchHeader()` and only then renders `<Sidebar />`, which fetches afterward. Correct: separate async `Header` and `Sidebar` components rendered side by side by a non-async `Page`, or a `Layout` that renders `Header` and receives `Sidebar` via `children`.

## 353. Parallel Nested Data Fetching
- Impact: CRITICAL (eliminates server-side waterfalls).
- Rule: when each item needs a dependent follow-up fetch, chain it inside that item's promise rather than waiting for all first-stage fetches to finish.
- User-visible effect: one slow item no longer delays the rest; for 100 items, 99 can complete while one lags.
- Incorrect: `await Promise.all(chatIds.map(getChat))` then `await Promise.all(chats.map(c => getUser(c.author)))`. Correct: `Promise.all(chatIds.map(id => getChat(id).then(chat => getUser(chat.author))))`.

## 354. Minimize Serialization at Server-Client Boundaries
- Impact: HIGH (reduces data transfer size).
- Rule: everything passed from a server component to a client component is serialized into the HTML and later payloads; pass only the fields the client uses.
- User-visible effect: lighter pages that load faster.
- Incorrect: passing a 50-field `user` object to a `Profile` that displays only `name`. Correct: pass `name={user.name}`.

## 355. Avoid Duplicate Serialization in Server Props
- Impact: LOW (reduces network payload).
- Rule: serialization dedupes by object reference, not value; don't pass both an array and a transformed copy of it. Do `.toSorted()`, `.filter()`, `.map()` on the client.
- User-visible effect: smaller payloads, faster loads, especially with primitive arrays.
- Incorrect: `usernames={usernames} usernamesOrdered={usernames.toSorted()}` (sends 6 strings for 3). Correct: send `usernames` once and sort in the client with `useMemo`.
- Impact is HIGH for `string[]`, `number[]`, `boolean[]` (all values duplicated) and LOW for `object[]` (only the array structure duplicated). Reference-breaking operations include `.slice()`, spreads, `Object.assign()`, `structuredClone()`, and JSON round-trips. Exception: pass derived data when the transform is expensive or the client doesn't need the original.

## 356. Hoist Static I/O to Module Level
- Impact: HIGH (avoids repeated file or network I/O per request).
- Rule: load static assets (fonts, logos, config, templates) once at module level rather than inside each request handler.
- User-visible effect: faster responses for generated images and server-rendered content because reads don't repeat per request.
- Incorrect: fetching `Inter.ttf` and `logo.png`, or reading `config.json`, inside `GET` on every call. Correct: create the promises (or `readFileSync` results) at module scope and `await Promise.all([fontData, logoData])` in the handler.
- Don't use for per-user or per-request assets, files that change at runtime (use a TTL cache), very large files, or sensitive data that shouldn't stay in memory.

## 357. Avoid Shared Module State for Request Data
- Impact: HIGH (prevents concurrency bugs and request data leaks).
- Rule: treat server module scope as process-wide shared memory; never store request-scoped data in mutable module variables during server rendering.
- User-visible effect: prevents one user's data appearing in another user's response and race-condition rendering bugs.
- Incorrect: `let currentUser` set in `Page` and read in `Dashboard`, which overlapping requests can overwrite. Correct: pass `user` down as a prop through the render tree.
- Safe exceptions: immutable static assets or config, deliberately designed and correctly keyed cross-request caches, and singletons that hold no request- or user-specific mutable data.

## 358. Cross-Request LRU Caching
- Impact: HIGH (caches across requests).
- Rule: per-request dedup only lasts for one request; for data reused across sequential requests within seconds (user clicks A then B), use an LRU cache.
- User-visible effect: follow-up interactions return faster because the repeat query is a cache hit.
- Incorrect: querying the database for the same user on each endpoint. Correct: an `LRUCache` with `max: 1000` and `ttl` of 5 minutes, checked before querying.
- Most effective when concurrent requests share an instance; in isolated serverless invocations, use an external store such as Redis.

## 359. Per-Request Deduplication with React.cache
- Impact: MEDIUM (deduplicates within a request).
- Rule: wrap auth checks, database queries, heavy computation and file reads in `React.cache()` so repeated calls in one render execute once.
- User-visible effect: shorter server render time when many components need the same data.
- Incorrect: a cached function taking an inline object such as `getUser({ uid: 1 })`, which always misses because equality is `Object.is`. Correct: take primitive arguments (`getUser(1)`) or reuse the same object reference.
- Framework-extended `fetch` is already memoized per request; `React.cache()` is for non-fetch async work.

## 360. Non-Blocking Post-Response Work
- Impact: MEDIUM (faster response times).
- Rule: schedule logging, analytics, notifications, cache invalidation and cleanup with `after()` so they run after the response is sent.
- User-visible effect: mutations and requests respond immediately instead of waiting for side effects.
- Incorrect: `await logUserAction(...)` before returning the response. Correct: wrap the logging in `after(async () => ...)` and return right away.
- `after()` runs even if the response fails or redirects, and works in server actions, route handlers and server components.

# Part 57 — Client-Side Data Fetching

## 361. Deduplicate Requests with a Shared Fetch Cache
- Impact: MEDIUM-HIGH (automatic deduplication); this is the headline impact of the client-fetching part.
- Rule: use a fetching hook library such as SWR so component instances share one request, a cache, and revalidation.
- User-visible effect: fewer redundant network calls and data that appears instantly from cache when components remount.
- Incorrect: `useEffect` plus `fetch('/api/users')` and `useState` in each instance. Correct: `useSWR('/api/users', fetcher)`; use an immutable variant for static config and `useSWRMutation` for mutations.

## 362. Passive Event Listeners for Scrolling
- Impact: MEDIUM (eliminates scroll delay caused by event listeners).
- Rule: add `{ passive: true }` to touch and wheel listeners that never call `preventDefault()`.
- User-visible effect: scrolling starts immediately instead of waiting for the listener, removing scroll jank.
- Incorrect: `addEventListener('touchstart', handler)` and `('wheel', handler)` with no options. Correct: pass `{ passive: true }`.
- Don't use passive for custom swipe gestures, custom zoom, or any handler that must call `preventDefault()`.

## 363. Version and Minimize Stored Client Data
- Impact: MEDIUM (prevents schema conflicts, reduces storage size).
- Rule: prefix storage keys with a version, store only the fields the UI needs, migrate old versions, and wrap every access in try/catch.
- User-visible effect: preferences survive app updates without broken state, and the app doesn't crash in private browsing, when quota is exceeded, or when storage is disabled.
- Incorrect: `localStorage.setItem('userConfig', JSON.stringify(fullUserObject))` with no error handling. Correct: `setItem('userConfig:v2', JSON.stringify({ theme, language }))` inside try/catch, plus a migration from `v1`.
- Storing minimal fields also prevents persisting tokens, PII or internal flags.

## 364. Deduplicate Global Event Listeners
- Impact: LOW (single listener for N components).
- Rule: share one global listener across all hook instances instead of registering one per instance.
- User-visible effect: less per-event work, keeping keyboard and window interactions responsive as instances multiply.
- Incorrect: a `useKeyboardShortcut` hook that calls `window.addEventListener('keydown', ...)` per use (N instances, N listeners). Correct: a module-level `Map` of callbacks per key plus a single shared subscription via `useSWRSubscription('global-keydown', ...)` that dispatches to them.

# Part 58 — Re-render Optimization

## 365. Don't Define Components Inside Components
- Impact: HIGH (prevents remount on every render); the re-render part overall is MEDIUM impact.
- Rule: never declare a component inside another component's body; define it at top level and pass the values it needs as props.
- User-visible effect: prevents inputs losing focus on every keystroke, animations restarting, scroll position resetting, and effects re-running, all caused by full remounts.
- Incorrect: `const Avatar = () => <img ... />` declared inside `UserProfile` to reach `user` and `theme`. Correct: a top-level `Avatar({ src, theme })` rendered with props.

## 366. Derive State During Render
- Impact: MEDIUM (avoids redundant renders and state drift).
- Rule: if a value can be computed from current props or state, compute it in render; don't store it in state and sync it with an effect. Use derived values or keyed resets instead of setting state in response to prop changes.
- User-visible effect: no extra render pass and no flash of stale values.
- Incorrect: `fullName` state updated by `useEffect` when `firstName` or `lastName` change. Correct: `const fullName = firstName + ' ' + lastName`.

## 367. Subscribe to Derived Booleans
- Impact: MEDIUM (reduces re-render frequency).
- Rule: subscribe to the coarse derived state you actually render on, not a continuously changing raw value.
- User-visible effect: resizing or scrolling no longer re-renders the component on every pixel, reducing jank.
- Incorrect: `useWindowWidth()` then `width < 768`. Correct: `useMediaQuery('(max-width: 767px)')`, which updates only when the boolean flips.

## 368. Defer State Reads to Usage Point
- Impact: MEDIUM (avoids unnecessary subscriptions).
- Rule: don't subscribe to dynamic state (search params, storage) when you only read it inside a callback; read it on demand in the handler.
- User-visible effect: the component no longer re-renders on unrelated URL or storage changes.
- Incorrect: `useSearchParams()` at the top of `ShareButton` just to read `ref` on click. Correct: read `new URLSearchParams(window.location.search)` inside the click handler.

## 369. Extract Expensive Work into Memoized Components
- Impact: MEDIUM (enables early returns).
- Rule: move expensive computation into a child component wrapped in `memo()` so the parent can return early (for example on loading) before any of that work runs.
- User-visible effect: loading states appear faster and parent re-renders skip expensive subtrees.
- Incorrect: `useMemo` computing an avatar above an `if (loading) return <Skeleton />`. Correct: a `memo` `UserAvatar` that computes internally, rendered only after the early return.
- With an automatic memoizing compiler enabled, manual `memo()` and `useMemo()` are unnecessary.

## 370. Stable Default Values for Memoized Props
- Impact: MEDIUM (restores memoization).
- Rule: when a memoized component has a non-primitive default prop (array, object, function), hoist the default into a module constant.
- User-visible effect: memoization actually prevents re-renders instead of silently failing.
- Incorrect: `memo(function UserAvatar({ onClick = () => {} }))`, which creates a new function every render. Correct: `const NOOP = () => {}` and `onClick = NOOP`.

## 371. Functional setState Updates
- Impact: MEDIUM (prevents stale closures and unnecessary callback recreation).
- Rule: when new state depends on previous state, use the updater form.
- User-visible effect: child components receive stable callbacks and stop re-rendering, and updates never use stale data (no lost list items).
- Incorrect: `useCallback(() => setItems([...items, ...newItems]), [items])`, or an empty deps array that captures stale `items`. Correct: `setItems(curr => [...curr, ...newItems])` with `[]` deps.
- Direct updates are fine for static values (`setCount(0)`) or values from arguments only.

## 372. Lazy State Initialization
- Impact: MEDIUM (avoids wasted computation on every render).
- Rule: pass a function to `useState` when the initial value is expensive; otherwise the expression runs on every render though it is used once.
- User-visible effect: typing and other updates stay snappy because indexes aren't rebuilt and storage isn't re-parsed per render.
- Incorrect: `useState(buildSearchIndex(items))` or `useState(JSON.parse(localStorage.getItem(...)))`. Correct: `useState(() => buildSearchIndex(items))`.
- Use for storage reads, building indexes or maps, DOM reads and heavy transforms; unnecessary for primitives, direct prop references or cheap literals.

## 373. Split Combined Hook Computations
- Impact: MEDIUM (avoids recomputing independent steps).
- Rule: when one `useMemo` or `useEffect` does independent tasks with different dependencies, split them so each reruns only for its own inputs.
- User-visible effect: changing sort order doesn't redo filtering, keeping controls responsive.
- Incorrect: a single `useMemo` that filters and sorts with deps `[products, category, sortOrder]`; one effect that tracks page views and sets the document title. Correct: a filter memo on `[products, category]` feeding a sort memo on `[filteredProducts, sortOrder]`; two separate effects.

## 374. Put Interaction Logic in Event Handlers
- Impact: MEDIUM (avoids effect re-runs and duplicate side effects).
- Rule: side effects caused by a specific user action (submit, click, drag) belong in that handler, not in a state flag plus effect.
- User-visible effect: no duplicate submissions or repeated toasts when unrelated values (like theme) change.
- Incorrect: `setSubmitted(true)` and an effect on `[submitted, theme]` that posts and shows a toast. Correct: `handleSubmit` posts and shows the toast directly.

## 375. Transitions for Non-Urgent Updates
- Impact: MEDIUM (maintains UI responsiveness).
- Rule: wrap frequent, non-urgent state updates in `startTransition`.
- User-visible effect: scrolling and typing stay smooth because urgent updates can interrupt background ones.
- Incorrect: a scroll handler calling `setScrollY(window.scrollY)` directly. Correct: `startTransition(() => setScrollY(window.scrollY))`.

## 376. Defer Expensive Derived Renders
- Impact: MEDIUM (keeps input responsive during heavy computation).
- Rule: when input drives an expensive computation or render, use `useDeferredValue` so the input updates first and the expensive result renders when the browser is free.
- User-visible effect: the search box never lags; results may briefly be stale, which can be signalled by dimming (for example opacity 0.7 while `query !== deferredQuery`).
- Incorrect: filtering `items` by `query` directly during each keystroke's render. Correct: `deferredQuery = useDeferredValue(query)` and `useMemo` filtering on `deferredQuery`.
- The computation must be in `useMemo` keyed on the deferred value or it still runs every render. Good for large list filtering and charts reacting to input.

## 377. Refs for Transient High-Frequency Values
- Impact: MEDIUM (avoids unnecessary re-renders on frequent updates).
- Rule: store rapidly changing values that don't need to drive rendering (mouse position, intervals, transient flags) in `useRef`, and update the DOM directly when needed.
- User-visible effect: smooth pointer tracking without a React render per mouse move.
- Incorrect: `setLastX(e.clientX)` on every `mousemove` to position a dot. Correct: write `lastXRef.current` and set `node.style.transform = translateX(...)` through a DOM ref.

## 378. Avoid useMemo for Simple Primitive Expressions
- Impact: LOW-MEDIUM (avoids wasted work on every render).
- Rule: don't wrap a simple expression with a primitive result (boolean, number, string) in `useMemo`; the hook and dependency comparison can cost more than the expression.
- Incorrect: `useMemo(() => user.isLoading || notifications.isLoading, [...])`. Correct: `const isLoading = user.isLoading || notifications.isLoading`.

## 379. Narrow Effect Dependencies
- Impact: LOW (minimizes effect re-runs).
- Rule: depend on primitive fields rather than whole objects, and compute derived conditions outside the effect so it runs only on meaningful transitions.
- User-visible effect: fewer redundant effect runs during resizes and updates.
- Incorrect: `[user]` when only `user.id` is used; an effect on `[width]` that runs at 767, 766, 765... Correct: `[user.id]`; `const isMobile = width < 768` and depend on `[isMobile]`.

# Part 59 — Rendering Performance

## 380. Content Visibility for Long Lists
- Impact: HIGH (faster initial render); the rendering part overall is MEDIUM impact.
- Rule: apply `content-visibility: auto` with a `contain-intrinsic-size` estimate to repeated off-screen items.
- User-visible effect: long feeds render roughly 10× faster initially; for 1000 messages the browser skips layout and paint for about 990 off-screen items, and the size hint keeps the scrollbar stable.
- Incorrect: rendering a long message list with full layout for every item. Correct: a `.message-item` class with `content-visibility: auto; contain-intrinsic-size: 0 80px`.

## 381. Resource Hints for Critical Assets
- Impact: HIGH (reduces load time for critical resources).
- Rule: tell the browser early about resources it will need, ideally from server components before HTML reaches the client.
- User-visible effect: fonts, styles and APIs are ready sooner, reducing render delay and layout or font shifts; route code prefetched on hover makes navigation feel instant.
- API guide: `prefetchDNS` for third-party domains used later; `preconnect` for APIs or CDNs used immediately; `preload` for critical current-page resources (e.g. a `woff2` font with `as: 'font'`); `preloadModule` for the likely next route's JS; `preinit` and `preinitModule` for stylesheets, scripts or modules that must execute early.
- Incorrect: letting the browser discover fonts and connections only when parsing reaches them. Correct: call `preconnect`, `preload` and `preinit` at the top of the root layout, and `preloadModule` on link hover.

## 382. Non-Blocking Script Tags
- Impact: HIGH (eliminates render-blocking).
- Rule: every script tag needs `defer` or `async`; plain scripts block HTML parsing while they download and run, delaying First Contentful Paint and Time to Interactive.
- User-visible effect: content paints without waiting for scripts.
- Incorrect: `<script src="analytics.js" />` in the head. Correct: `async` for independent scripts like analytics; `defer` for scripts that need the DOM or must keep order. In the framework, prefer its script component with a `strategy` such as `afterInteractive`.

## 383. Prevent Hydration Flicker for Client-Only Values
- Impact: MEDIUM (avoids visual flicker and hydration errors).
- Rule: for UI depending on client storage or cookies (theme, preferences, auth state), inject a small synchronous inline script that sets the DOM before hydration.
- User-visible effect: no flash of the default theme or wrong content after load, and no server-render crash.
- Incorrect: reading `localStorage` during render (breaks server rendering), or defaulting to `light` and correcting in `useEffect` (visible flash). Correct: render a wrapper with a known id plus an inline `<script>` that reads storage in try/catch and sets the wrapper's class immediately.

## 384. Preserve State with Activity for Show/Hide
- Impact: MEDIUM (preserves state and DOM).
- Rule: for expensive components that toggle visibility often, wrap them in `<Activity mode={isOpen ? 'visible' : 'hidden'}>` instead of mounting and unmounting.
- User-visible effect: menus and panels reopen instantly with scroll and form state intact.
- Incorrect: conditionally rendering `<ExpensiveMenu />` so it is rebuilt each time. Correct: keep it mounted under `Activity` and switch the mode.

## 385. Suppress Only Expected Hydration Mismatches
- Impact: LOW-MEDIUM (avoids noisy warnings for known differences).
- Rule: for values that legitimately differ between server and client (random ids, dates, locale or timezone formatting), mark only that element with `suppressHydrationWarning`.
- Incorrect: rendering `new Date().toLocaleString()` unmarked and living with warnings. Correct: `<span suppressHydrationWarning>` around it. Never use it to hide real bugs, and don't overuse it.

## 386. Animate a Wrapper Instead of the SVG
- Impact: LOW (enables hardware acceleration).
- Rule: many browsers don't GPU-accelerate CSS animations on SVG elements; wrap the SVG in a `div` and animate the wrapper.
- User-visible effect: smooth spinners and icon animations without jank.
- Incorrect: `<svg className="animate-spin">`. Correct: `<div className="animate-spin"><svg ... /></div>`. Applies to `transform`, `opacity`, `translate`, `scale` and `rotate`.

## 387. Explicit Conditional Rendering
- Impact: LOW (prevents rendering `0` or `NaN`).
- Rule: use a ternary instead of `&&` when the condition can be a falsy value that renders.
- User-visible effect: no stray "0" appearing in badges or layouts.
- Incorrect: `{count && <span>{count}</span>}`, which shows "0". Correct: `{count > 0 ? <span>{count}</span> : null}`.

## 388. Hoist Static JSX
- Impact: LOW (avoids re-creation).
- Rule: extract static markup, especially large static SVGs, into module-level constants.
- Incorrect: a component that recreates an identical skeleton element every render. Correct: `const loadingSkeleton = <div className="animate-pulse h-20 bg-gray-200" />` reused.
- An automatic memoizing compiler makes manual hoisting unnecessary.

## 389. Reduce SVG Coordinate Precision
- Impact: LOW (reduces file size).
- Rule: trim path coordinates to the precision the viewBox needs, typically 1 decimal place.
- User-visible effect: lighter icons and illustrations that download and parse faster.
- Incorrect: `M 10.293847 20.847362`. Correct: `M 10.3 20.8`; automate with an optimizer such as SVGO at `--precision=1 --multipass`.

## 390. Prefer Transitions over Manual Loading Flags
- Impact: LOW (fewer re-renders and clearer code).
- Rule: use `useTransition` for async updates instead of hand-managed `isLoading` state.
- User-visible effect: the input updates immediately, a pending indicator shows via `isPending`, newer transitions supersede older ones, and pending state resets correctly even if the work throws.
- Incorrect: `setIsLoading(true)`, await the fetch, `setIsLoading(false)`. Correct: `setQuery(value)` immediately, then `startTransition(async () => { setResults(await fetchResults(value)) })`.

# Part 60 — JavaScript Performance

## 391. Avoid Layout Thrashing
- Impact: MEDIUM (prevents forced synchronous layouts); the JavaScript part overall is LOW-MEDIUM impact.
- Rule: don't interleave style writes with layout reads (`offsetWidth`, `getBoundingClientRect()`, `getComputedStyle()`); batch writes then read, or reads then writes, and prefer toggling a CSS class.
- User-visible effect: removes jank from repeated forced reflows.
- Incorrect: set `width`, read `offsetWidth`, set `height`, read `offsetHeight`. Correct: apply all writes, then read once; best of all, toggle a class such as `highlighted-box` from props.

## 392. Defer Non-Critical Work to Idle Time
- Impact: MEDIUM (keeps UI responsive during background tasks).
- Rule: schedule analytics, saving to storage, prefetching and non-urgent transforms with `requestIdleCallback`, with a `setTimeout` fallback where unsupported.
- User-visible effect: interactions and animations stay smooth because the main thread is free.
- Incorrect: tracking, saving recent searches and prefetching synchronously right after `setResults`. Correct: each in its own `requestIdleCallback`.
- Thresholds: pass `{ timeout: 2000 }` when the work must happen within 2 seconds; chunk large jobs using `deadline.timeRemaining()` (aim for chunks under 50ms). Don't use for user-initiated feedback, renders the user is waiting on, or time-sensitive work.

## 393. Cache Repeated Function Results
- Impact: MEDIUM (avoids redundant computation).
- Rule: memoize pure functions called repeatedly with the same inputs during render in a module-level `Map`, which works outside components too.
- User-visible effect: faster renders for large lists.
- Incorrect: calling `slugify(project.name)` 100+ times for repeated names. Correct: a `cachedSlugify` backed by a `Map`; for single-value checks, a cached variable reset on change (e.g. on auth change).

## 394. Early Length Check for Array Comparisons
- Impact: MEDIUM-HIGH (avoids expensive operations when lengths differ).
- Rule: before sorting, deep-comparing or serializing arrays to compare them, check `length` first.
- User-visible effect: change detection in handlers and render loops stays cheap.
- Incorrect: `current.sort().join() !== original.sort().join()`, which also mutates the inputs. Correct: return `true` when lengths differ, otherwise compare `toSorted()` copies element by element and return on the first difference.

## 395. Immutable Sorting
- Impact: MEDIUM-HIGH (prevents mutation bugs in state).
- Rule: use `.toSorted()` instead of `.sort()` on props or state, which mutates in place.
- User-visible effect: prevents lists reordering unexpectedly and stale or inconsistent UI.
- Incorrect: `useMemo(() => users.sort(...), [users])`. Correct: `users.toSorted(...)`; fall back to `[...items].sort()` for older environments.
- Related immutable methods: `.toReversed()`, `.toSpliced()`, `.with()`. Supported in Chrome 110+, Safari 16+, Firefox 115+, Node 20+.

## 396. Index Maps for Repeated Lookups
- Impact: LOW-MEDIUM (1M ops down to 2K ops).
- Rule: replace repeated `.find()` by key with a `Map` built once.
- Incorrect: `users.find(u => u.id === order.userId)` inside `orders.map`. Correct: `const userById = new Map(users.map(u => [u.id, u]))` and `userById.get(...)`.
- For 1000 orders by 1000 users, work drops from 1M to 2K operations.

## 397. Set and Map for Membership Checks
- Impact: LOW-MEDIUM (O(n) to O(1)).
- Rule: convert arrays used for repeated membership checks into a `Set` or `Map`.
- Incorrect: `allowedIds.includes(item.id)` inside a filter. Correct: `new Set(allowedIds)` and `.has(item.id)`.

## 398. Cache Storage Reads
- Impact: LOW-MEDIUM (reduces expensive I/O).
- Rule: `localStorage`, `sessionStorage` and `document.cookie` are synchronous and slow; cache reads in an in-memory `Map` and update it on writes.
- User-visible effect: less main-thread blocking during frequent reads.
- Incorrect: `localStorage.getItem('theme')` on every call. Correct: a `getLocalStorage` helper backed by a `Map`, and a parsed cookie object built once.
- Invalidate on external changes: on the `storage` event and when `visibilitychange` makes the tab visible.

## 399. Combine Multiple Array Iterations
- Impact: LOW-MEDIUM (reduces iterations).
- Rule: merge several `.filter()` or `.map()` passes over the same array into one loop.
- Incorrect: three separate `users.filter` calls for admins, testers and inactive users. Correct: one `for...of` loop pushing into three arrays.

## 400. Map and Filter in One Pass
- Impact: LOW-MEDIUM (eliminates an intermediate array).
- Rule: use `.flatMap()` instead of `.map().filter(Boolean)`.
- Incorrect: `users.map(u => u.isActive ? u.name : null).filter(Boolean)`. Correct: `users.flatMap(u => u.isActive ? [u.name] : [])`; same for parsing where invalid inputs return `[]`.

## 401. Cache Property Access in Hot Loops
- Impact: LOW-MEDIUM (reduces lookups).
- Rule: read deep property chains and `arr.length` once before a hot loop.
- Incorrect: `obj.config.settings.value` read in every iteration. Correct: store `value` and `len` in locals first.

## 402. Return Early
- Impact: LOW-MEDIUM (avoids unnecessary computation).
- Rule: return as soon as the result is known instead of continuing to process.
- Incorrect: validating every user while tracking `hasError`. Correct: return `{ valid: false, error }` on the first failure.

## 403. Hoist Regular Expressions
- Impact: LOW-MEDIUM (avoids recreation).
- Rule: don't construct `RegExp` in render; hoist constant patterns to module scope, or `useMemo` dynamic ones keyed on their input (escaping user input).
- Incorrect: `new RegExp(query, 'gi')` on every render. Correct: a module-level `EMAIL_REGEX`, or `useMemo(() => new RegExp(escapeRegex(query), 'gi'), [query])`.
- Caution: global (`/g`) regexes keep mutable `lastIndex` state, so repeated `.test()` calls alternate results.

## 404. Linear Min and Max
- Impact: LOW (O(n) instead of O(n log n)).
- Rule: find smallest or largest items with a single loop, not by sorting.
- Incorrect: `[...projects].sort(...)[0]` to get the latest. Correct: one pass tracking `latest` (or `oldest` and `newest`), handling the empty case.
- `Math.min(...arr)` and `Math.max(...arr)` are fine for small arrays but fail or slow down on large ones, at roughly 124,000 elements in Chrome and 638,000 in Safari.

# Part 61 — Advanced Patterns

## 405. Initialize the App Once, Not Per Mount
- Impact: LOW-MEDIUM (avoids duplicate initialization); the advanced part overall is LOW impact.
- Rule: app-wide setup that must run once per load should not live in a component's `useEffect([])`, which re-runs on remount and twice in development.
- User-visible effect: no duplicate storage loads or auth checks causing redundant work or flicker.
- Incorrect: calling `loadFromStorage()` and `checkAuthToken()` in a mount effect. Correct: guard with a module-level `didInit` flag, or run it in the entry module.

## 406. Store Event Handlers in Refs for Stable Subscriptions
- Impact: LOW (stable subscriptions).
- Rule: when an effect subscribes to an event, keep the latest callback in a ref so the subscription doesn't tear down and re-attach when the callback identity changes.
- User-visible effect: fewer listener churns and no missed events during re-renders.
- Incorrect: `useEffect` on `[event, handler]` that re-adds the listener each render. Correct: update `handlerRef.current` and subscribe once on `[event]` with a listener that calls the ref; or use `useEffectEvent` on recent versions.

## 407. Effect Events for Latest Values Without Re-runs
- Impact: LOW (prevents effect re-runs).
- Rule: read the latest callback or values inside effects through `useEffectEvent` instead of listing them as dependencies.
- User-visible effect: debounced searches and timers aren't reset because a parent passed a new callback.
- Incorrect: a 300ms debounce effect with deps `[query, onSearch]`. Correct: `onSearchEvent = useEffectEvent(onSearch)` and deps `[query]`.

## 408. Keep Effect Events Out of Dependency Arrays
- Impact: LOW (avoids unnecessary effect re-runs and lint errors).
- Rule: functions returned by `useEffectEvent` intentionally change identity every render; never list them as dependencies. Depend on the real reactive values and call the effect event from inside the effect.
- User-visible effect: connections and subscriptions aren't torn down and re-established on every render.
- Incorrect: `[roomId, handleConnected]`. Correct: `[roomId]` only.
