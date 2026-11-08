# Design Rules by Concept

Distilled from UI/UX Pro Max — a UI/UX knowledge base: UX guidelines, motion, charts and landing patterns, brand/logo/banner/slide and token systems, 89 visual styles, 192 product-type recommendations, semantic palettes, font pairings, icon semantics, and platform-specific UI rules.

# Part 1 — Navigation

## 1. Smooth Scroll
- Rule: Anchor links should scroll smoothly to target section.
- Do: Use scroll-behavior: smooth on html element.
- Don't: Jump directly without transition.
- Platform: Web; severity: High.
- Values: `scroll-behavior: smooth` on the root `html` element.

## 2. Sticky Navigation
- Rule: Fixed nav should not obscure content.
- Do: Add padding-top to body equal to nav height.
- Don't: Let nav overlap first section content.
- Platform: Web; severity: Medium.
- Values: Body `padding-top` equal to the nav height (e.g. `80px` offset for an `80px` bar).

## 3. Active State
- Rule: Current page/section should be visually indicated.
- Do: Highlight active nav item with color/underline.
- Don't: No visual feedback on current location.
- Platform: All; severity: Medium.
- Values: Active item in primary colour plus a `2px` bottom border.

## 4. Back Button
- Rule: Users expect back to work predictably.
- Do: Preserve navigation history properly.
- Don't: Break browser/app back button behavior.
- Platform: Mobile; severity: High.
- Values: Push a history entry for every meaningful view change.

## 5. Deep Linking
- Rule: URLs should reflect current state for sharing.
- Do: Update URL on state/view changes.
- Don't: Static URLs for dynamic content.
- Platform: All; severity: Medium.
- Values: Encode filters, tabs and views in query params or the hash.

## 6. Breadcrumbs
- Rule: Show user location in site hierarchy.
- Do: Use for sites with 3+ levels of depth.
- Don't: Use for flat single-level sites.
- Platform: Web; severity: Low.
- Values: `Home > Category > Product`; use only at `3+` levels of depth.

# Part 2 — Animation

## 7. Excessive Motion
- Rule: Too many animations cause distraction and motion sickness.
- Do: Animate 1-2 key elements per view maximum.
- Don't: Animate everything that moves.
- Platform: All; severity: High.
- Values: `1-2` animated elements per view maximum; a single hero animation.

## 8. Duration Timing
- Rule: Motion duration depends on distance complexity platform and user context.
- Do: Use shared motion tokens and test that feedback stays responsive.
- Don't: Present 150-300ms or any cutoff as a universal requirement.
- Platform: All; severity: Medium.
- Values: Shared motion tokens (e.g. `200ms` colour transitions); `150-300ms` is a starting range, not a universal rule.

## 9. Reduced Motion
- Rule: Respect user's motion preferences.
- Do: Check prefers-reduced-motion media query.
- Don't: Ignore accessibility motion settings.
- Platform: All; severity: High.
- Values: `@media (prefers-reduced-motion: reduce)`.

## 10. Loading States
- Rule: Show feedback during async operations.
- Do: Use skeleton screens or spinners.
- Don't: Leave UI frozen with no feedback.
- Platform: All; severity: High.
- Values: Pulsing skeleton blocks or a spinner.

## 11. Hover vs Tap
- Rule: Hover effects don't work on touch devices.
- Do: Use click/tap for primary interactions.
- Don't: Rely only on hover for important actions.
- Platform: All; severity: High.
- Values: Primary actions bound to click/tap; hover only as enhancement.

## 12. Continuous Animation
- Rule: Infinite animations are distracting.
- Do: Use for loading indicators only.
- Don't: Use for decorative elements.
- Platform: All; severity: Medium.
- Values: Infinite spin reserved for loaders.

## 13. Transform Performance
- Rule: Some CSS properties trigger expensive repaints.
- Do: Use transform and opacity for animations.
- Don't: Animate width/height/top/left properties.
- Platform: Web; severity: Medium.
- Values: Animate `transform` (e.g. `translateY()`) and `opacity`; never `width`, `height`, `top`, `left`.

## 14. Easing Functions
- Rule: Easing should match how an element changes speed and purpose.
- Do: Use deceleration when arriving acceleration when leaving and linear for constant-rate progress.
- Don't: Reject linear easing even for steady rotation or progress.
- Platform: All; severity: Low.
- Values: `ease-out` for entry, `ease-in` for exit, `linear` for spinners and progress.

## 15. Auto-Rotating Content Controls
- Rule: Auto-rotating content needs user control.
- Do: Provide previous next and play/pause; stop on focus or hover and when reduced motion is requested.
- Don't: Auto-advance slides without a stop control.
- Platform: All; severity: High.
- Values: Pause control such as `aria-label="Pause carousel"`.

## 16. Cancellable State Transitions
- Rule: Rapid compact-control changes can interrupt an in-flight transition.
- Do: Cancel or replace prior motion; set the final semantic state directly and handle cancellation cleanup.
- Don't: Depend on animationend or transitionend for required state correctness.
- Platform: Web; severity: High.
- Values: Cancel the previous animation, then set the final state directly.

# Part 3 — Layout

## 17. Z-Index Management
- Rule: Stacking context conflicts cause hidden elements.
- Do: Define z-index scale system (10 20 30 50)
- Don't: Use arbitrary large z-index values.
- Platform: Web; severity: High.
- Values: Z-index scale `10 / 20 / 30 / 50`; no `9999`-style values.

## 18. Overflow Hidden
- Rule: Hidden overflow can clip important content.
- Do: Test all content fits within containers.
- Don't: Blindly apply overflow-hidden.
- Platform: Web; severity: Medium.
- Values: Prefer `overflow: auto` with scroll over blanket `overflow: hidden`.

## 19. Fixed Positioning
- Rule: Fixed elements can overlap or be inaccessible.
- Do: Account for safe areas and other fixed elements.
- Don't: Stack multiple fixed elements carelessly.
- Platform: Web; severity: Medium.
- Values: Fixed nav and fixed bottom bar separated by a gap and safe-area insets.

## 20. Stacking Context
- Rule: New stacking contexts reset z-index.
- Do: Understand what creates new stacking context.
- Don't: Expect z-index to work across contexts.
- Platform: Web; severity: Medium.
- Values: A parent with `z-index` (or `transform`, `opacity < 1`, `isolation: isolate`) isolates its children.

## 21. Content Jumping
- Rule: Images badges validation text and skeleton replacements can shift nearby content when they update.
- Do: Reserve appropriate space or keep async states in a stable content-driven container.
- Don't: Insert compact text or media without a layout strategy.
- Platform: Web; severity: High.
- Values: `aspect-ratio` on media; a fixed-width slot for counts and badges.

## 22. Viewport Units
- Rule: 100vh can be problematic on mobile browsers.
- Do: Use dvh or account for mobile browser chrome.
- Don't: Use 100vh for full-screen mobile layouts.
- Platform: Web; severity: Medium.
- Values: `min-height: 100dvh` instead of `100vh`.

## 23. Container Width
- Rule: Content too wide is hard to read.
- Do: Limit max-width for text content (65-75ch)
- Don't: Let text span full viewport width.
- Platform: Web; severity: Medium.
- Values: Text measure `65-75ch` (e.g. `max-width: 65ch`).

## 24. Long Token Wrapping
- Rule: URLs identifiers and user content must not force horizontal overflow.
- Do: Use overflow-wrap anywhere and let flex or grid text children shrink.
- Don't: Apply word-break break-all to all prose.
- Platform: Web; severity: High.
- Values: `min-inline-size: 0; overflow-wrap: anywhere`.

## 25. Chip Collection Reflow
- Rule: Filter chips and editable value collections must preserve labels when space or text size changes.
- Do: Wrap the collection or use an operable +n disclosure for hidden overflow values.
- Don't: Force all chips into one clipped row or hide overflow values.
- Platform: All; severity: High.
- Values: `flex-wrap: wrap` or an operable `+n` disclosure.

# Part 4 — Touch

## 26. Touch Target Size
- Rule: Touch target guidance depends on platform and web context.
- Do: Use 44pt on iOS and 48dp on Android; for web use the separate WCAG Target Size rule.
- Don't: Treat one unit or minimum as universal across platforms.
- Platform: Mobile; severity: High.
- Values: iOS `44pt`; Android `48dp`; web `24 CSS px` plus WCAG exceptions.

## 27. Touch Spacing
- Rule: Adjacent touch targets need adequate spacing.
- Do: Minimum 8px gap between touch targets.
- Don't: Tightly packed clickable elements.
- Platform: Mobile; severity: Medium.
- Values: Minimum `8px` gap between targets.

## 28. Gesture Conflicts
- Rule: Custom gestures can conflict with system.
- Do: Avoid horizontal swipe on main content.
- Don't: Override system gestures.
- Platform: Mobile; severity: Medium.
- Values: Vertical scroll is the primary gesture on main content.

## 29. Tap Delay
- Rule: 300ms tap delay feels laggy.
- Do: Use touch-action CSS or fastclick.
- Don't: Default mobile tap handling.
- Platform: Mobile; severity: Medium.
- Values: `touch-action: manipulation` removes the `300ms` delay.

## 30. Pull to Refresh
- Rule: Accidental refresh is frustrating.
- Do: Disable where not needed.
- Don't: Enable by default everywhere.
- Platform: Mobile; severity: Low.
- Values: `overscroll-behavior: contain` where refresh is not wanted.

## 31. Haptic Feedback
- Rule: Tactile feedback improves interaction feel.
- Do: Use for confirmations and important actions.
- Don't: Overuse vibration feedback.
- Platform: Mobile; severity: Low.
- Values: Short pulses (e.g. `10ms`) for confirmations only.

# Part 5 — Interaction

## 32. Focus States
- Rule: Keyboard focus, including controls inside a modal, needs a visible indicator.
- Do: Use a visible focus ring on every interactive control, including modal controls.
- Don't: Remove focus outline without replacement.
- Platform: All; severity: High.
- Values: `2px` focus ring in a contrasting colour on every control.

## 33. Hover States
- Rule: Visual feedback on interactive elements.
- Do: Change cursor and add subtle visual change.
- Don't: No hover feedback on clickable elements.
- Platform: Web; severity: Medium.
- Values: `cursor: pointer` plus a subtle background change.

## 34. Active States
- Rule: Show immediate feedback on press/click.
- Do: Add pressed/active state visual change.
- Don't: No feedback during interaction.
- Platform: All; severity: Medium.
- Values: Pressed state such as `transform: scale(0.95)`.

## 35. Disabled States
- Rule: Clearly indicate non-interactive elements.
- Do: Reduce opacity and change cursor.
- Don't: Confuse disabled with normal state.
- Platform: All; severity: Medium.
- Values: `opacity: 0.5` and `cursor: not-allowed`.

## 36. Loading Buttons
- Rule: Prevent double submission during async actions.
- Do: Disable button and show loading state.
- Don't: Allow multiple clicks during processing.
- Platform: All; severity: High.
- Values: Button `disabled` while the request runs, with an inline spinner.

## 37. Error Feedback
- Rule: Users need to know when something fails.
- Do: Show clear error messages near problem.
- Don't: Silent failures with no feedback.
- Platform: All; severity: High.
- Values: Red border plus a text message next to the field.

## 38. Success Feedback
- Rule: Confirm successful actions to users.
- Do: Show success message or visual change.
- Don't: No confirmation of completed action.
- Platform: All; severity: Medium.
- Values: Toast notification or checkmark.

## 39. Confirmation Dialogs
- Rule: Prevent accidental destructive actions.
- Do: Confirm before delete/irreversible actions.
- Don't: Delete without confirmation.
- Platform: All; severity: High.
- Values: "Are you sure?" confirmation before destructive actions.

# Part 6 — Accessibility

## 40. Color Contrast
- Rule: Text must be readable against background.
- Do: Minimum 4.5:1 ratio for normal text.
- Don't: Low contrast text.
- Platform: All; severity: High.
- Values: Minimum `4.5:1` for normal text; `#333333` on `#FFFFFF` comfortably exceeds `7:1`.

## 41. Color Only
- Rule: Convey information by color alone.
- Do: Use icons/text in addition to color.
- Don't: Red/green only for error/success.
- Platform: All; severity: High.
- Values: Red text plus an error icon (colour + shape + text).

## 42. Alt Text
- Rule: Images need text alternatives.
- Do: Descriptive alt text for meaningful images.
- Don't: Empty or missing alt attributes.
- Platform: All; severity: High.
- Values: Describe the content, e.g. `alt="Dog playing in park"`.

## 43. Heading Hierarchy
- Rule: Screen readers use headings for navigation.
- Do: Use sequential heading levels h1-h6.
- Don't: Skip heading levels or misuse for styling.
- Platform: Web; severity: Medium.
- Values: Sequential levels: `h1` → `h2` → `h3`.

## 44. ARIA Labels
- Rule: Interactive elements need accessible names.
- Do: Add aria-label for icon-only buttons.
- Don't: Icon buttons without labels.
- Platform: All; severity: High.
- Values: `aria-label="Close menu"` on icon-only buttons.

## 45. Keyboard Navigation
- Rule: Web users need complete keyboard navigation with visible focus on every operable control.
- Do: Keep tab order aligned with visual order and test every action without a pointer.
- Don't: Keyboard traps or illogical tab order.
- Platform: Web; severity: High.
- Values: Tab order follows visual order; every action testable without a pointer.

## 46. Screen Reader
- Rule: Content should make sense when read aloud.
- Do: Use semantic HTML and ARIA properly.
- Don't: Div soup with no semantics.
- Platform: All; severity: Medium.
- Values: Landmarks `<nav>`, `<main>`, `<article>` instead of generic `div`s.

## 47. Form Labels
- Rule: Inputs must have associated labels.
- Do: Use label with for attribute or wrap input.
- Don't: Placeholder-only inputs.
- Platform: All; severity: High.
- Values: `<label for="email">` or a wrapping label.

## 48. Error Messages
- Rule: Error messages must be announced.
- Do: Use aria-live or role=alert for errors.
- Don't: Visual-only error indication.
- Platform: All; severity: High.
- Values: `role="alert"` or an `aria-live` region.

## 49. Skip Links
- Rule: Allow keyboard users to skip navigation.
- Do: Provide skip to main content link.
- Don't: No skip link on nav-heavy pages.
- Platform: Web; severity: Medium.
- Values: "Skip to main content" link as the first focusable element.

## 50. Motion Sensitivity
- Rule: Parallax/Scroll-jacking causes nausea.
- Do: Honor prefers-reduced-motion and present the final readable state without parallax or scroll-jacking.
- Don't: Force scroll effects.
- Platform: All; severity: High.
- Values: `@media (prefers-reduced-motion: reduce)` shows the final static state.

## 51. Focus Not Obscured (Minimum)
- Rule: WCAG 2.2 AA requires keyboard focus to remain at least partially visible.
- Do: Offset sticky UI with scroll-padding and dismiss or move persistent overlays.
- Don't: Let headers footers banners or chat widgets fully cover focus.
- Platform: Web; severity: High.
- Values: `scroll-padding-top: var(--header-height)` for sticky headers.

## 52. Focus Not Obscured (Enhanced)
- Rule: WCAG 2.2 AAA requires keyboard focus to remain fully visible.
- Do: Keep the entire focused component unobscured by author-created content.
- Don't: Present this enhanced AAA criterion as an AA requirement or allow persistent UI to hide any part of focus.
- Platform: Web; severity: Medium.
- Values: Entire focused component unobscured (AAA).

## 53. Focus Appearance
- Rule: WCAG 2.2 AAA defines minimum area and contrast for focus indicators.
- Do: Use an indicator at least as large as a 2 CSS px perimeter with 3:1 state contrast.
- Don't: Present this enhanced AAA criterion as an AA requirement or use a thin low-contrast outline.
- Platform: Web; severity: Medium.
- Values: `outline: 2px solid currentColor; outline-offset: 2px`; `3:1` state contrast.

## 54. Dragging Movements
- Rule: WCAG 2.2 AA requires a single-pointer alternative for author-controlled drag operations.
- Do: Add buttons menus or tap-to-move controls and retain keyboard operation.
- Don't: Make dragging the only way to reorder resize or select.
- Platform: All; severity: High.
- Values: Move up / Move down buttons beside every drag handle.

## 55. Target Size (Minimum)
- Rule: WCAG 2.2 AA requires 24 CSS px pointer targets or an applicable exception.
- Do: Use at least 24 by 24 CSS px or verify spacing equivalent inline user-agent or essential exceptions.
- Don't: Assume native 44pt or 48dp guidance defines web conformance.
- Platform: Web; severity: High.
- Values: `min-width: 24px; min-height: 24px` (or spacing-equivalent exception).

## 56. Consistent Help
- Rule: WCAG 2.2 A requires repeated help mechanisms to stay in the same relative order.
- Do: Keep contact self-help and automated help in consistent locations.
- Don't: Move help controls to different locations on each page.
- Platform: All; severity: Medium.
- Values: Help menu in the same place in a shared header.

## 57. Text Reflow and Spacing
- Rule: Text must remain available at narrow widths zoom and user spacing overrides.
- Do: Use fluid sizes content-driven height and unitless line height.
- Don't: Clip text in fixed-width or fixed-height boxes.
- Platform: Web; severity: Critical.
- Values: `inline-size: min(100%, 65ch); height: auto; line-height: 1.5`.

## 58. Compact Control Semantics
- Rule: Interactive chips need a native role accessible name state keyboard operation and visible focus.
- Do: Prefer a button and expose pressed or selected state that matches the visible label.
- Don't: Use a clickable div or reveal the only action on hover.
- Platform: Web; severity: Critical.
- Values: Native `<button aria-pressed="true">` matching the visible label.

## 59. Contextual Live Badge Updates
- Rule: Async badge and count changes should announce a meaningful contextual status without moving focus.
- Do: Use one appropriate atomic status message such as 3 items in cart.
- Don't: Announce a bare number or make every badge a competing live region.
- Platform: Web; severity: High.
- Values: `role="status"` with `aria-atomic="true"`, announcing e.g. "3 items in cart".

# Part 7 — Performance

## 60. Image Optimization
- Rule: Large images slow page load.
- Do: Use appropriate size and format (WebP)
- Don't: Unoptimized full-size images.
- Platform: All; severity: High.
- Values: WebP/modern formats with `srcset` at multiple sizes.

## 61. Lazy Loading
- Rule: Load content as needed.
- Do: Lazy load below-fold images and content.
- Don't: Load everything upfront.
- Platform: All; severity: Medium.
- Values: `loading="lazy"` on below-fold media.

## 62. Code Splitting
- Rule: Large bundles slow initial load.
- Do: Split code by route/feature.
- Don't: Single large bundle.
- Platform: Web; severity: Medium.
- Values: Dynamic `import()` per route or feature.

## 63. Caching
- Rule: Repeat visits should be fast.
- Do: Set appropriate cache headers.
- Don't: No caching strategy.
- Platform: Web; severity: Medium.
- Values: `Cache-Control` headers tuned per asset type.

## 64. Font Loading
- Rule: Web fonts can block rendering.
- Do: Use font-display swap or optional.
- Don't: Invisible text during font load.
- Platform: Web; severity: Medium.
- Values: `font-display: swap` or `optional`.

## 65. Third Party Scripts
- Rule: External scripts can block rendering.
- Do: Load non-critical scripts async/defer.
- Don't: Synchronous third-party scripts.
- Platform: Web; severity: Medium.
- Values: `async` or `defer` on non-critical scripts.

## 66. Bundle Size
- Rule: Large JavaScript slows interaction.
- Do: Monitor and minimize bundle size.
- Don't: Ignore bundle size growth.
- Platform: Web; severity: Medium.
- Values: Track bundle size with an analyzer and a budget.

## 67. Render Blocking
- Rule: CSS/JS can block first paint.
- Do: Inline critical CSS defer non-critical.
- Don't: Large blocking CSS files.
- Platform: Web; severity: Medium.
- Values: Inline critical CSS; defer the rest.

# Part 8 — Forms

## 68. Input Labels
- Rule: Every input needs a visible label.
- Do: Always show label above or beside input.
- Don't: Placeholder as only label.
- Platform: All; severity: High.
- Values: Visible label above or beside every input.

## 69. Error Placement
- Rule: Each invalid field needs an inline error connected to that field.
- Do: Show a specific error below the input and reference it with aria-describedby.
- Don't: Show only a top-level error without identifying each invalid field.
- Platform: All; severity: High.
- Values: Error below the input linked via `aria-describedby="email-error"`; specific copy such as "Enter an email address".

## 70. Inline Validation
- Rule: Validate as user types or on blur.
- Do: Validate on blur for most fields.
- Don't: Validate only on submit.
- Platform: All; severity: Medium.
- Values: Validate `on blur` for most fields.

## 71. Input Types
- Rule: Use appropriate input types.
- Do: Use email tel number url etc.
- Don't: Text input for everything.
- Platform: All; severity: Medium.
- Values: `type="email"`, `tel`, `number`, `url`.

## 72. Autofill Support
- Rule: Help browsers autofill correctly.
- Do: Use autocomplete attribute properly.
- Don't: Block or ignore autofill.
- Platform: Web; severity: Medium.
- Values: `autocomplete="email"` and other correct tokens.

## 73. Required Indicators
- Rule: Mark required fields clearly.
- Do: Use asterisk or (required) text.
- Don't: No indication of required fields.
- Platform: All; severity: Medium.
- Values: Asterisk `*` or "(required)" text.

## 74. Password Visibility
- Rule: Let users see password while typing.
- Do: Toggle to show/hide password.
- Don't: No visibility toggle.
- Platform: All; severity: Medium.
- Values: Show/hide password toggle.

## 75. Submit Feedback
- Rule: Confirm form submission status.
- Do: Show loading then success/error state.
- Don't: No feedback after submit.
- Platform: All; severity: High.
- Values: Loading → Success or Error state.

## 76. Input Affordance
- Rule: Inputs should look interactive.
- Do: Use distinct input styling.
- Don't: Inputs that look like plain text.
- Platform: All; severity: Medium.
- Values: Visible border or filled background on inputs.

## 77. Mobile Keyboards
- Rule: Show appropriate keyboard for input type.
- Do: Use inputmode attribute.
- Don't: Default keyboard for all inputs.
- Platform: Mobile; severity: Medium.
- Values: `inputmode="numeric"` and similar hints.

## 78. Redundant Entry
- Rule: WCAG 2.2 A avoids requiring the same information twice in one process.
- Do: Auto-populate prior values or let users select previously entered information.
- Don't: Ask users to retype the same address or account data without necessity.
- Platform: All; severity: Medium.
- Values: Reuse a confirmed shipping address instead of asking again.

## 79. IME Composition Enter
- Rule: Korean (한글) Japanese and Chinese IME composition can use Enter to confirm text rather than submit a chat message or search.
- Do: Cancel the default action of handled Enter before guarding isComposing or legacy keyCode 229; preserve Shift+Enter and modifier policy; ignore repeats; retain a submit button for virtual keyboards.
- Don't: Send or clear text on every Enter keydown or submit from compositionend.
- Platform: Web; severity: High.
- Values: Ignore Enter while `isComposing` is true or `keyCode` is `229`; keep `Shift+Enter` for newline and a visible submit button.

# Part 9 — Responsive

## 80. Mobile First
- Rule: Design for mobile then enhance for larger.
- Do: Start with mobile styles then add breakpoints.
- Don't: Desktop-first causing mobile issues.
- Platform: Web; severity: Medium.
- Values: Mobile base styles, then `min-width` breakpoints for larger screens.

## 81. Breakpoint Testing
- Rule: Test at all common screen sizes.
- Do: Test at 320 375 414 768 1024 1440.
- Don't: Only test on your device.
- Platform: Web; severity: Medium.
- Values: Test at `320`, `375`, `414`, `768`, `1024`, `1440` px widths.

## 82. Touch Friendly
- Rule: Mobile layouts need touch-sized targets.
- Do: Increase touch targets on mobile.
- Don't: Same tiny buttons on mobile.
- Platform: Web; severity: High.
- Values: Larger buttons and spacing on mobile layouts.

## 83. Readable Font Size
- Rule: Text must be readable on all devices.
- Do: Minimum 16px body text on mobile.
- Don't: Tiny text on mobile.
- Platform: All; severity: High.
- Values: Minimum `16px` body text on mobile.

## 84. Viewport Meta
- Rule: Set viewport for mobile devices.
- Do: Use width=device-width initial-scale=1.
- Don't: Missing or incorrect viewport.
- Platform: Web; severity: High.
- Values: `<meta name="viewport" content="width=device-width, initial-scale=1">`.

## 85. Horizontal Scroll
- Rule: Avoid horizontal scrolling.
- Do: Ensure content fits viewport width.
- Don't: Content wider than viewport.
- Platform: Web; severity: High.
- Values: `max-width: 100%` on content; no element wider than the viewport.

## 86. Image Scaling
- Rule: Images should scale with container.
- Do: Use max-width: 100% on images.
- Don't: Fixed width images overflow.
- Platform: Web; severity: Medium.
- Values: `max-width: 100%; height: auto` on images.

## 87. Table Handling
- Rule: Tables can overflow on mobile.
- Do: Use horizontal scroll or card layout.
- Don't: Wide tables breaking layout.
- Platform: Web; severity: Medium.
- Values: `overflow-x: auto` wrapper or a card layout on small screens.

# Part 10 — Typography

## 88. Line Height
- Rule: Adequate line height improves readability.
- Do: Use 1.5-1.75 for body text.
- Don't: Cramped or excessive line height.
- Platform: All; severity: Medium.
- Values: Body line height `1.5-1.75` (e.g. `1.625`).

## 89. Line Length
- Rule: Long lines are hard to read.
- Do: Limit to 65-75 characters per line.
- Don't: Full-width text on large screens.
- Platform: Web; severity: Medium.
- Values: `65-75` characters per line (`max-width: 65ch`).

## 90. Font Size Scale
- Rule: Consistent type hierarchy aids scanning.
- Do: Use consistent modular scale.
- Don't: Random font sizes.
- Platform: All; severity: Medium.
- Values: Modular scale such as `12 / 14 / 16 / 18 / 24 / 32` px.

## 91. Font Loading (Typography)
- Rule: Fonts should load without layout shift.
- Do: Reserve space with fallback font.
- Don't: Layout shift when fonts load.
- Platform: Web; severity: Medium.
- Values: `font-display: swap` plus a metric-similar fallback font.

## 92. Contrast Readability
- Rule: Body text needs good contrast.
- Do: Use darker text on light backgrounds.
- Don't: Gray text on gray background.
- Platform: All; severity: High.
- Values: Near-black text (e.g. `#111827`) on white.

## 93. Heading Clarity
- Rule: Headings should stand out from body.
- Do: Clear size/weight difference.
- Don't: Headings similar to body text.
- Platform: All; severity: Medium.
- Values: Clear size and weight step (bold + larger).

## 94. Heading Line Balance
- Rule: Short multi-line headings may use balanced wrapping as a progressive visual heuristic.
- Do: Bound the measure and test natural-wrap fallback across widths fonts and locales.
- Don't: Promise an exact final line or insert blanket nonbreaking spaces or hardcoded br tags.
- Platform: Web; severity: Medium.
- Values: `max-inline-size: 20ch; text-wrap: balance`.

# Part 11 — Feedback

## 95. Loading Indicators
- Rule: Loading feedback should match the expected wait and avoid flashing for near-instant work.
- Do: Follow platform and component guidance; preserve layout focus and accessible busy status.
- Don't: Apply one timing threshold to every operation or leave long waits unexplained.
- Platform: All; severity: High.
- Values: Stable skeleton or progress element with `aria-busy="true"`.

## 96. Empty States
- Rule: Guide users when no content exists.
- Do: Show helpful message and action.
- Don't: Blank empty screens.
- Platform: All; severity: Medium.
- Values: Helpful copy plus an action, e.g. "No items yet. Create one!".

## 97. Error Recovery
- Rule: Help users recover from errors.
- Do: Provide clear next steps.
- Don't: Error without recovery path.
- Platform: All; severity: Medium.
- Values: "Try again" button plus a help link.

## 98. Progress Indicators
- Rule: Show progress for multi-step processes.
- Do: Step indicators or progress bar.
- Don't: No indication of progress.
- Platform: All; severity: Medium.
- Values: Step indicator such as "Step 2 of 4".

## 99. Toast Notifications
- Rule: Transient messages for non-critical info.
- Do: Auto-dismiss after 3-5 seconds.
- Don't: Toasts that never disappear.
- Platform: All; severity: Medium.
- Values: Auto-dismiss after `3-5` seconds.

## 100. Confirmation Messages
- Rule: Confirm successful actions.
- Do: Brief success message.
- Don't: Silent success.
- Platform: All; severity: Medium.
- Values: Brief message such as "Saved successfully".

# Part 12 — Content

## 101. Truncation
- Rule: Handle long content gracefully.
- Do: Truncate with ellipsis and expand option.
- Don't: Overflow or broken layout.
- Platform: All; severity: Medium.
- Values: Clamp to `2` lines with an expand control.

## 102. Date Formatting
- Rule: Use locale-appropriate date formats.
- Do: Use relative or locale-aware dates.
- Don't: Ambiguous date formats.
- Platform: All; severity: Low.
- Values: Relative ("2 hours ago") or locale-aware formats.

## 103. Number Formatting
- Rule: Format large numbers for readability.
- Do: Use thousand separators or abbreviations.
- Don't: Long unformatted numbers.
- Platform: All; severity: Low.
- Values: `1.2K` abbreviations or `1,234` separators.

## 104. Placeholder Content
- Rule: Show realistic placeholders during dev.
- Do: Use realistic sample data.
- Don't: Lorem ipsum everywhere.
- Platform: All; severity: Low.
- Values: Realistic sample content instead of lorem ipsum.

## 105. Essential Text Truncation
- Rule: Headings actions errors safety text and distinguishing names need complete access.
- Do: Wrap stack resize or provide a visible full-detail path.
- Don't: Clamp essential meaning only to make cards uniform.
- Platform: All; severity: Critical.
- Values: Essential labels wrap, stack, or open a full-detail view.

## 106. Compact Label Semantics
- Rule: Badges communicate state while chips or tags represent values or actions.
- Do: Choose static or interactive markup from the label's meaning and ownership.
- Don't: Make every pill clickable or encode status with color alone.
- Platform: All; severity: High.
- Values: Static status badge as plain text (e.g. "Pending"); chips as buttons only when actionable.

## 107. Compact Label Overflow
- Rule: A badge chip or pill label should stay whole on one line when practical and disclose unavoidable truncation.
- Do: Bound only unpredictable values; use nowrap with a shrinkable label; expose full text to keyboard pointer and touch users.
- Don't: Let one compact label wrap to a second line or use a hover-only tooltip.
- Platform: All; severity: High.
- Values: `white-space: nowrap` with a shrinkable `min-width: 0` label and an operable full-value disclosure.

# Part 13 — Onboarding

## 108. User Freedom
- Rule: Users should be able to skip tutorials.
- Do: Provide Skip and Back buttons.
- Don't: Force linear unskippable tour.
- Platform: All; severity: Medium.
- Values: Visible Skip and Back buttons on every tour step.

# Part 14 — Search

## 109. Autocomplete
- Rule: Help users find results faster.
- Do: Show predictions as user types.
- Don't: Require full type and enter.
- Platform: Web; severity: Medium.
- Values: Debounced suggestions in a dropdown as the user types.

## 110. No Results
- Rule: Dead ends frustrate users.
- Do: Show 'No results' with suggestions.
- Don't: Blank screen or '0 results'.
- Platform: Web; severity: Medium.
- Values: "No results" plus suggestions such as "Try searching for X instead".

# Part 15 — Data Entry

## 111. Bulk Actions
- Rule: Editing one by one is tedious.
- Do: Allow multi-select and bulk edit.
- Don't: Single row actions only.
- Platform: Web; severity: Low.
- Values: Checkbox column plus a bulk action bar.

# Part 16 — AI Interaction

## 112. Disclaimer
- Rule: Users need to know they talk to AI.
- Do: Clearly label AI generated content.
- Don't: Present AI as human.
- Platform: All; severity: High.
- Values: Visible "AI Assistant" label on generated content.

## 113. Streaming
- Rule: Waiting for full text is slow.
- Do: Stream text response token by token.
- Don't: Show loading spinner for 10s+.
- Platform: All; severity: Medium.
- Values: Stream token by token; never a bare spinner for `10s+`.

## 114. Feedback Loop
- Rule: AI needs user feedback to improve.
- Do: Thumbs up/down or 'Regenerate'.
- Don't: Static output only.
- Platform: All; severity: Low.
- Values: Thumbs up/down and a Regenerate action.

# Part 17 — Spatial UI

## 115. Gaze Hover
- Rule: Elements should respond to eye tracking before pinch.
- Do: Scale/highlight element on look.
- Don't: Static element until pinch.
- Platform: VisionOS; severity: High.
- Values: Highlight or scale elements on gaze, before the pinch.

## 116. Depth Layering
- Rule: UI needs Z-depth to separate content from environment.
- Do: Use glass material and z-offset.
- Don't: Flat opaque panels blocking view.
- Platform: VisionOS; severity: Medium.
- Values: Glass material plus z-offset to separate panels from the environment.

# Part 18 — Sustainability

## 117. Auto-Play Video
- Rule: Autoplaying media consumes data and creates motion barriers.
- Do: Prefer click-to-play; provide pause and captions; stop off-screen and honor reduced motion.
- Don't: Auto-play high-resolution loops without pause or captions.
- Platform: Web; severity: Medium.
- Values: Click-to-play with `controls`, `preload="none"` and a captions track.

## 118. Asset Weight
- Rule: Heavy 3D/Image assets increase carbon footprint.
- Do: Compress and lazy load 3D models.
- Don't: Load 50MB textures.
- Platform: Web; severity: Medium.
- Values: Compressed 3D meshes, lazy loaded; never `50MB` textures.

# Part 19 — Security & Accessibility

## 119. Accessible Authentication (Minimum)
- Rule: WCAG 2.2 AA says authentication must not depend only on a cognitive function test unless an exception applies.
- Do: Allow password managers and paste; offer passkeys OAuth or another non-cognitive method.
- Don't: Block paste or require manual OTP transcription with no alternative.
- Platform: All; severity: Critical.
- Values: `autocomplete="current-password"` with paste allowed; passkeys or OAuth as alternatives.

# Part 20 — Forms & Accessibility

## 120. Focusable Error Summary
- Rule: An error summary for failed validation complements inline field errors and must be easy to find by keyboard and screen reader users.
- Do: Place it at the top of the form; move focus to its heading or container after failed submit; link each item to its invalid field; retain inline errors.
- Don't: Replace inline errors with a visual-only summary or move focus on every blur.
- Platform: Web; severity: High.
- Values: Summary container with `role="alert"` and `tabindex="-1"`, heading "There is a problem", each item linking to its field.

# Part 21 — App Interface Rules

## 121. Icon Button Labels
- Area: Accessibility.
- Rule: Icon-only buttons must expose an accessible label.
- Do: Set accessibilityLabel or label prop on icon buttons.
- Don't: Icon buttons without accessible names.
- Platform: iOS, Android and cross-platform native; severity: Critical.
- Values: `accessibilityLabel="Close"` on icon-only pressables.

## 122. Form Control Labels
- Area: Accessibility.
- Rule: All inputs must have a visible label and an accessibility label.
- Do: Pair Text label with input and set accessibilityLabel.
- Don't: Inputs with placeholder only.
- Platform: iOS, Android and cross-platform native; severity: Critical.
- Values: Visible text label plus `accessibilityLabel="Email address"`.

## 123. Role & Traits
- Area: Accessibility.
- Rule: Interactive elements must expose correct roles/traits.
- Do: Use accessibilityRole/button/link/checkbox etc.
- Don't: Rely on generic views with no roles.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: `accessibilityRole="button"` / `link` / `checkbox`.

## 124. Dynamic Updates
- Area: Accessibility.
- Rule: Async status updates should be announced to screen readers.
- Do: Use accessibilityLiveRegion or announceForAccessibility.
- Don't: Update text silently with no announcement.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: `accessibilityLiveRegion="polite"` or an explicit announcement.

## 125. Decorative Icons
- Area: Accessibility.
- Rule: Decorative icons should be hidden from screen readers.
- Do: Mark decorative icons as not accessible.
- Don't: Have screen reader read every icon.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: Decorative icons marked not accessible / hidden from assistive tech.

## 126. Touch Target Size (Native Apps)
- Area: Touch.
- Rule: Native targets use 44pt on iOS and 48dp on Android; web WCAG 2.2 has a separate 24 by 24 CSS px minimum with exceptions.
- Do: Select 44pt for iOS and 48dp for Android at runtime; evaluate web targets separately against WCAG 2.5.8 and its exceptions.
- Don't: Collapse iOS 44pt, Android 48dp, and web 24 CSS px into one cross-platform number.
- Platform: iOS, Android and cross-platform native; severity: Critical.
- Values: iOS `44pt`, Android `48dp` chosen at runtime; web evaluated separately at `24 CSS px`.

## 127. Touch Spacing (Native Apps)
- Area: Touch.
- Rule: Adjacent touch targets need enough spacing.
- Do: Keep at least 8dp spacing between touchables.
- Don't: Cluster many buttons with no gap.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: At least `8dp` gap between touchables.

## 128. Gesture Conflicts (Native Apps)
- Area: Touch.
- Rule: Custom gestures must not break system scroll/back.
- Do: Reserve horizontal swipes for carousels.
- Don't: Full-screen custom swipe conflicting with back.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: Horizontal swipe reserved for carousels inside vertical scroll.

## 129. Back Behavior
- Area: Navigation.
- Rule: Back navigation should be predictable and preserve state.
- Do: Use navigation.goBack and keep screen state.
- Don't: Reset stack or exit app unexpectedly.
- Platform: iOS, Android and cross-platform native; severity: Critical.
- Values: Back returns to the previous screen with its state intact.

## 130. Bottom Tabs
- Area: Navigation.
- Rule: Bottom tab bar should have at most 5 primary items.
- Do: Use 3–5 tabs and move extras to More/Settings.
- Don't: Overloaded tab bar with many icons.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: `3-5` tabs maximum (e.g. Home / Explore / Profile / Settings).

## 131. Modal Escape
- Area: Navigation.
- Rule: Modals/sheets must have clear close actions.
- Do: Provide close button and swipe-down where platform expects.
- Don't: Trapping users in modal with no obvious exit.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: Visible Close button plus swipe-down where the platform expects it.

## 132. Preserve Screen State
- Area: State.
- Rule: Returning to a screen should restore its scroll and form state.
- Do: Keep components mounted or persist state.
- Don't: Reset list scroll and form inputs on every visit.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: Keep tab screens mounted or persist scroll and form state.

## 133. Loading Indicators (Native Apps)
- Area: Feedback.
- Rule: Show visible feedback during network operations.
- Do: Use ActivityIndicator or skeleton for >300ms operations.
- Don't: Leave button and screen frozen.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: Spinner or skeleton for operations over `300ms`.

## 134. Success Feedback (Native Apps)
- Area: Feedback.
- Rule: Confirm successful actions with brief feedback.
- Do: Show toast/checkmark or banner.
- Don't: Complete actions silently with no confirmation.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: Toast, checkmark or banner such as "Saved successfully".

## 135. Error Feedback (Native Apps)
- Area: Feedback.
- Rule: Show clear error messages near the problem.
- Do: Input-level error + summary banner.
- Don't: Only change border color with no explanation.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: Field-level error text plus a summary banner.

## 136. Inline Validation (Native Apps)
- Area: Forms.
- Rule: Validate inputs on blur or submit with clear messaging.
- Do: Validate onBlur and onSubmit.
- Don't: Validate on every keystroke causing jank.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: Validate on blur and on submit, not per keystroke.

## 137. Keyboard Type
- Area: Forms.
- Rule: Use appropriate keyboardType and returnKeyType.
- Do: Match email/tel/number/search types.
- Don't: Use default keyboard for all inputs.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: Keyboard types `email-address`, `phone-pad`, `numeric`, `search`; matching return key.

## 138. Auto Focus & Next
- Area: Forms.
- Rule: Guide users through form fields with Next/Done flows.
- Do: Use onSubmitEditing to focus next input.
- Don't: Force users to tap each field manually.
- Platform: iOS, Android and cross-platform native; severity: Low.
- Values: Return key focuses the next field; Done on the last.

## 139. Password Visibility (Native Apps)
- Area: Forms.
- Rule: Allow toggling password visibility securely.
- Do: Provide Show/Hide icon toggling secureTextEntry.
- Don't: Force users to type blind with no option.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: Show/Hide icon toggling secure text entry.

## 140. Virtualize Long Lists
- Area: Performance.
- Rule: Use FlatList/SectionList for lists over ~50 items.
- Do: Use keyExtractor and initialNumToRender appropriately.
- Don't: Render hundreds of items with ScrollView.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: Virtualized list for more than ~`50` items.

## 141. Image Size & Cache
- Area: Performance.
- Rule: Use correctly sized and cached images.
- Do: Use Image component with proper resizeMode and caching.
- Don't: Load full-resolution images everywhere.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: Correctly sized, cached images with an explicit resize mode (e.g. `cover`).

## 142. Debounce High-Freq Events
- Area: Performance.
- Rule: Debounce scroll/search callbacks to avoid jank.
- Do: Wrap handlers with debounce/throttle.
- Don't: Run heavy logic on every event.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: Debounce or throttle scroll and search handlers.

## 143. Duration & Easing
- Area: Animation.
- Rule: Micro-interactions should be 150–300ms with native-like easing.
- Do: Use ease-out for enter/ease-in for exit.
- Don't: Use long or linear animations for core UI.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: `150-300ms`, e.g. `200ms` with quadratic ease-out.

## 144. Respect Reduced Motion
- Area: Animation.
- Rule: Respect OS reduced-motion accessibility setting.
- Do: Check reduceMotionEnabled and simplify animations.
- Don't: Ignore user motion preferences.
- Platform: iOS, Android and cross-platform native; severity: Critical.
- Values: Skip or simplify animation when the OS reduce-motion setting is on.

## 145. Limited Continuous Motion
- Area: Animation.
- Rule: Reserve infinite animations for loaders and live data.
- Do: Use looping only where necessary.
- Don't: Keep decorative elements looping forever.
- Platform: iOS, Android and cross-platform native; severity: Medium.
- Values: Loops only for loaders and live data.

## 146. Base Font Size
- Area: Typography.
- Rule: Body text must be readable and support Dynamic Type.
- Do: Use platform fontScale and at least 14–16pt base.
- Don't: Render critical text below 12pt.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: Base body text `14-16pt`; never critical text below `12pt`.

## 147. Dynamic Type Support
- Area: Typography.
- Rule: Support system text scaling without breaking layout.
- Do: Set allowFontScaling and test large text.
- Don't: Disable scaling on all text globally.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: Font scaling enabled and tested at the largest text sizes.

## 148. Safe Area Insets
- Area: Safe Areas.
- Rule: Content must not overlap notches/gesture bars.
- Do: Wrap screens in SafeAreaView or apply insets.
- Don't: Place tappable content under system bars.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: Safe-area insets on every screen edge.

## 149. Light/Dark Contrast
- Area: Theming.
- Rule: Ensure sufficient contrast in both light and dark themes.
- Do: Use semantic tokens and test both themes.
- Don't: Reuse light-theme grays directly in dark mode.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: Semantic colour tokens per theme, e.g. dark-theme primary text `#F9FAFB`.

## 150. No Gesture-Only Actions
- Area: Anti-Pattern.
- Rule: Rely solely on hidden gestures for core actions.
- Do: Provide visible buttons in addition to gestures.
- Don't: Rely on swipe/shake only with no UI affordance.
- Platform: iOS, Android and cross-platform native; severity: Critical.
- Values: Swipe to delete plus a visible Delete button.

## 151. Dragging Alternatives
- Area: Accessibility.
- Rule: Native drag and reorder operations need a non-drag path selected for the active native runtime.
- Do: Provide named Move up/down buttons or a position menu beside drag handles; route iOS and Android behavior through the runtime platform adapter.
- Don't: Make drag, swipe, or a web-only pointer handler the only way to reorder native content.
- Platform: iOS, Android and cross-platform native; severity: High.
- Values: "Move up" / "Move down" buttons or a position menu beside drag handles.

## 152. Authentication Reuse
- Area: Forms.
- Rule: Authentication and multi-step flows should reuse prior values.
- Do: Support password managers passkeys paste and prefilled confirmed values.
- Don't: Force users to retype credentials or the same data in one flow.
- Platform: iOS, Android and cross-platform native; severity: Critical.
- Values: Password-manager autofill, passkeys and paste supported; `autoComplete="current-password"`.

# Part 22 — Motion Recipes

## 153. Subtle Hover Feedback
- Category: Hover Micro-interaction; intensity tier: Subtle.
- Trigger: hover.
- Duration: `150-200ms`; easing: `power1.out`.
- Properties: `transform`, `opacity`; displacement under `2px`.
- Do: Keep displacement under `2px` so it reads as feedback not motion.
- Don't: Animate layout-affecting props (width/height/margin) on hover.
- Performance: Runs on transform/opacity only so it stays on the compositor thread.
- Implementation: Bind enter and leave events; under reduced motion skip the tween and render the final state.

## 154. Standard Card Hover Lift
- Category: Hover Micro-interaction; intensity tier: Standard.
- Trigger: hover.
- Duration: `200-300ms`; easing: `power2.out`.
- Properties: `transform: translateY()`, `opacity`, shadow.
- Do: Pair with a matching mouseleave tween that reverses the same properties.
- Don't: Leave the hover state stuck if the pointer leaves fast; always attach the reverse tween.
- Performance: A persistent quick-setter avoids GC churn on lists with 20+ hoverable cards.
- Implementation: Reuse one persistent tween setter per property on lists with many hover targets instead of creating a new tween per event.

## 155. Magnetic Hover
- Category: Hover Micro-interaction; intensity tier: Complex.
- Trigger: hover + mousemove.
- Duration: `300-500ms`; easing: `elastic.out(1,0.4)`.
- Properties: `transform: translate(x, y)` following the pointer, pull clamped to ~`0.3`.
- Do: Clamp the pull strength (e.g. * 0.3) so the element never fully leaves its hit box.
- Don't: Apply magnetic effect to more than 1-2 focal elements per screen; it becomes noisy.
- Performance: Use will-change: transform on the target element for smoother compositing.
- Implementation: Keep a stable named pointer handler so cleanup removes the same function; under reduced motion hold x/y at the neutral final state.

## 156. Subtle Scroll Reveal
- Category: Scroll Reveal; intensity tier: Subtle.
- Trigger: scroll (viewport enter).
- Duration: `300-400ms`; easing: `power1.out`.
- Properties: `opacity`, `transform: translateY(8-16px)`.
- Do: Keep the y offset small (`8-16px`) so it reads as a fade, not a slide.
- Don't: Reveal below-the-fold content needed for SEO/crawlers as invisible-by-default without a no-JS fallback.
- Performance: Play on enter and reverse only on leave-back, which avoids re-triggering on every scroll direction change.
- Implementation: Trigger once on viewport enter; under reduced motion content renders visible immediately.

## 157. Standard Scroll Reveal
- Category: Scroll Reveal; intensity tier: Standard.
- Trigger: scroll (viewport enter).
- Duration: `400-600ms`; easing: `power2.out`.
- Properties: `opacity`, `transform: translateY()` with child stagger.
- Do: Scope the scroll trigger to the section container so it doesn't re-scan the whole page.
- Don't: Stagger more than ~8 children; beyond that the last items feel laggy.
- Performance: Disable debug markers in production; debug markers are development-only.
- Implementation: Scope the scroll observer to the section and clean up on unmount; under reduced motion render the final state.

## 158. Scroll-Scrubbed Pinned Section
- Category: Scroll Reveal; intensity tier: Complex.
- Trigger: scroll (continuous scrub).
- Duration: `tied to scroll position`; easing: `none (scrub-driven)`.
- Properties: progress-mapped `transform`/`opacity`; pinning.
- Do: Use scrub: true or a small number (0.5-1.5) instead of instant jumps so it feels tied to the scrollbar.
- Don't: Pin more than 1-2 sections per page; excessive pinning fights native scroll feel and hurts mobile UX.
- Performance: Pinning forces layout reflow; test on mid-tier mobile devices, not just desktop.
- Implementation: The pinned section needs deterministic height; recalculate trigger positions after images and fonts load; disable scrub and pin under reduced motion.

## 159. Subtle List Stagger
- Category: Stagger List; intensity tier: Subtle.
- Trigger: load or scroll.
- Duration: `250-350ms`; easing: `power1.out`.
- Properties: `opacity`, `transform: translateY()`; per-item delay `0.02-0.04s`.
- Do: Keep per-item stagger delay small (`0.02-0.04s`) for lists longer than 10 items.
- Don't: Stagger by more than `0.1s` per item on long lists; total reveal time becomes sluggish.
- Performance: For virtualized lists, only animate items currently mounted in the DOM.
- Implementation: Target items by a stable class or data attribute rather than array index so re-renders do not break targeting.

## 160. Grid Wave Stagger
- Category: Stagger List; intensity tier: Standard.
- Trigger: load or scroll.
- Duration: `300-450ms`; easing: `back.out(1.4)`.
- Properties: `opacity`, `transform: scale()/translateY()` staggered from the grid centre.
- Do: Combine with from: 'center' for a bento-grid layout to draw the eye inward first.
- Don't: Use back.out on dense data tables; the overshoot reads as sloppy on informational UI.
- Performance: Group DOM writes; avoid interleaving layout reads (getBoundingClientRect) between staggered tweens.
- Implementation: Infer rows and columns from the grid so the stagger travels as a wave; start from the centre on bento layouts.

## 161. Split-Text Headline Reveal
- Category: Stagger List; intensity tier: Complex.
- Trigger: load or scroll.
- Duration: `400-700ms`; easing: `expo.out`.
- Properties: per-character `opacity`, `transform`.
- Do: Revert SplitText on unmount/cleanup (split.revert()) to restore original text nodes for accessibility tools.
- Don't: Split-animate long paragraphs; reserve for short headlines (under ~8 words)
- Performance: Splitting text creates one element per character; keep it to headline-length copy only for DOM size.
- Implementation: Split only headline copy into characters, restore original text nodes on cleanup for assistive tech, and keep a plain fade fallback; under reduced motion render readable text immediately.

## 162. Subtle Route Fade
- Category: Page Transition; intensity tier: Subtle.
- Trigger: route change.
- Duration: `200-300ms`; easing: `power1.inOut`.
- Properties: `opacity`, small `transform` on exit/enter.
- Do: Preload the destination route's critical assets before the exit tween finishes.
- Don't: Block navigation on animation; cap exit duration at ~`250ms` so the app never feels unresponsive.
- Performance: Exit animation should always resolve faster than entrance (asymmetric timing) so back/forward feels snappy.
- Implementation: Hook into the router transition lifecycle; preload the destination before the exit finishes.

## 163. Overlay Wipe Transition
- Category: Page Transition; intensity tier: Standard.
- Trigger: route change.
- Duration: `400-600ms`; easing: `power2.inOut`.
- Properties: overlay `transform: translateY(%)`.
- Do: Show a lightweight loading indicator if the destination route's data fetch outlasts the overlay.
- Don't: Tie the overlay's reveal directly to data-fetch completion without a max-wait timeout; a slow API stalls the whole transition.
- Performance: Prefer CSS transform (yPercent) over top/left to keep the overlay animation on the compositor thread.
- Implementation: Mount the overlay at the layout root so it survives the route swap; add a max-wait timeout so slow data never stalls the wipe.

## 164. Shared-Element Route Transition
- Category: Page Transition; intensity tier: Complex.
- Trigger: route change.
- Duration: `500-800ms`; easing: `expo.inOut`.
- Properties: FLIP: measured position/size animated via `transform`.
- Do: Verify the shared element exists in both DOM states before calling Flip.from to avoid a silent no-op.
- Don't: Use shared-element transitions across more than one element pair per navigation; compounding Flips are hard to time correctly.
- Performance: Shared-element animation recalculates layout (FLIP technique) so test on low-end devices for jank.
- Implementation: Both routes must render the same element with a shared id; verify it exists in both states before animating.

## 165. Subtle Background Parallax
- Category: Parallax Scroll; intensity tier: Subtle.
- Trigger: scroll (continuous).
- Duration: `tied to scroll position`; easing: `linear (scrub)`.
- Properties: background-layer `transform: translateY(5-15%)`.
- Do: Keep the yPercent delta small (5-15) so foreground and background never desync distractingly.
- Don't: Parallax body copy; it hurts reading comfort and can trigger motion sickness.
- Performance: Will-change: transform on the parallax layer only; remove it after scroll settles to free GPU memory.
- Implementation: Apply to decorative or background layers only, never to text or controls; disable under reduced motion.

## 166. Layered Depth Parallax
- Category: Parallax Scroll; intensity tier: Standard.
- Trigger: scroll (continuous).
- Duration: `tied to scroll position`; easing: `linear (scrub)`.
- Properties: per-layer `transform` at different speeds.
- Do: Vary speed per layer (background slowest, foreground fastest) to sell the depth illusion.
- Don't: Let parallax layers overflow their container; clip with overflow: hidden on the wrapper.
- Performance: Batch all layers under one scroll-trigger container where possible instead of one per layer.
- Implementation: Use at most `3-4` layers (background slowest, foreground fastest); batch layers under one scroll container.

## 167. Skeleton Shimmer
- Category: Loading / Skeleton; intensity tier: Subtle.
- Trigger: on mount / async wait.
- Duration: `1200-1600ms loop`; easing: `sine.inOut`.
- Properties: `background-position` gradient sweep.
- Do: Use a CSS gradient background-position sweep rather than opacity pulsing; reads as 'loading' more clearly.
- Don't: Run more than one shimmer loop per skeleton group; sync them under one timeline so the wave reads as a single unit.
- Performance: Infinite loops are cheap but must be explicitly killed on unmount or they leak in SPA route changes.
- Implementation: Kill the loop when content mounts or unmounts; pause when offscreen or the tab is hidden; under reduced motion show a static skeleton.

## 168. Standard Loading Loop
- Category: Loading / Skeleton; intensity tier: Standard.
- Trigger: on mount / async wait.
- Duration: `800-1200ms loop`; easing: `power1.inOut`.
- Properties: `transform`/`opacity` loop on a loader.
- Do: Cap total loop duration under ~`1.5s` so long waits don't feel like the UI froze on a single beat.
- Don't: Use elaborate loaders for sub-`300ms` waits; they flash and feel worse than no indicator.
- Performance: Pause the timeline when the loading tab/view is not visible to save CPU on background tabs.
- Implementation: Pause/resume with visibility; under reduced motion stop the loop and show a static loading state.

## 169. Carousel Auto-Rotation
- Category: Carousel / Auto-Rotation; intensity tier: Standard.
- Trigger: timer / focus / hover / visibility.
- Duration: `user-controlled or stopped`; easing: `none`.
- Properties: slide `transform`; timer-driven.
- Do: Provide previous/next and play/pause controls; announce the current slide without moving focus.
- Don't: Auto-advance without a visible stop control or continue while focus is inside.
- Performance: IntersectionObserver stops animation offscreen; visibilitychange stops hidden-tab work; cleanup disconnects the observer and clears the timer and listeners.
- Implementation: One cancellable timer; pause on focus, hover, offscreen and hidden tab; reduced motion stops rotation and shows the active slide.

# Part 23 — Choosing Charts by Data Type

## 170. Trend Over Time
- Best chart: Line Chart.
- Alternatives: Area Chart, Smooth Area.
- Use when: Data has a time axis; user needs to observe rise/fall trends or rate of change over a continuous period.
- Avoid when: Fewer than 4 data points (use stat card); more than 6 series (visual noise); no time dimension exists.
- Data volume: `<1000 pts`: SVG; `≥1000 pts`: Canvas + downsampling; `>10000`: aggregate to intervals.
- Colour: Primary: `#0080FF`. Multiple series: distinct colors + distinct line styles. Fill: `20%` opacity.
- Accessibility risk: `low`. Use solid, dashed, and dotted line styles plus direct series labels; never distinguish series by hue alone.
- Fallback: Visible data table plus concise trend summary. Keyboard: focus reveals hover values; +/- buttons zoom; Reset restores the full range.
- Interaction: Hover + Zoom.

## 171. Compare Categories
- Best chart: Bar Chart (Horizontal or Vertical).
- Alternatives: Column Chart, Grouped Bar.
- Use when: Comparing discrete categories by magnitude; ranking or ordering is the core insight; categories `≤ 15.`
- Avoid when: Categories `> 15` (use table or search); data has time dimension (use line); showing proportions (use waffle/stacked)
- Data volume: `<20` categories: vertical bar; 20–50: horizontal bar; `>50`: paginated table.
- Colour: Each bar: distinct color. Grouped: same hue family. Always sort descending by value.
- Accessibility risk: `low`. Use direct category/value labels and group outlines or patterns; never encode category solely by bar color. Do not rely on color alone.
- Fallback: Visible sortable data table plus concise comparison summary. Keyboard: focus reveals hover values; focusable headers with Enter/Space sort and aria-sort reports direction.
- Interaction: Hover + Sort.

## 172. Part-to-Whole
- Best chart: Pie Chart or Donut.
- Alternatives: Stacked Bar, Waffle Chart.
- Use when: `≤5` categories; one dominant segment vs rest; emphasis on visual proportion over exact values.
- Avoid when: Categories `> 5`; slice differences `< 5`% (visually indistinguishable); user needs precise values; accessibility-first context.
- Data volume: Max 6 slices; beyond that switch to stacked bar `100%`.
- Colour: 5–6 max colors. Contrasting palette. Largest slice at 12 o'clock. Always label slices with %.
- Accessibility risk: `high`. Pie charts do not inherently fail WCAG; unlabeled color-only slices are inaccessible. Use direct labels and patterns, with a non-pie fallback. Do not rely on color alone.
- Fallback: Percentage data table and concise part-to-whole summary; offer a stacked bar view. Keyboard: focus reveals slice values; Enter/Space drills in; Back button returns.
- Interaction: Hover + Drill.

## 173. Correlation / Distribution
- Best chart: Scatter Plot or Bubble Chart.
- Alternatives: Heat Map, Matrix.
- Use when: Exploring relationship between two continuous variables; identifying clusters or outliers in a dataset.
- Avoid when: Variables are categorical (use grouped bar); fewer than 20 points (patterns aren't meaningful); mobile-primary context.
- Data volume: `<500 pts`: SVG; 500–5000: Canvas at 0.6–0.8 opacity; `>5000`: hexbin or aggregate first.
- Colour: Color axis: gradient (blue → red). Bubble size: relative to 3rd variable. Opacity: 0.6–0.8 to show density.
- Accessibility risk: `conditional`. Combine marker shapes with direct group labels; color may reinforce but must not be the only distinction.
- Fallback: Visible data table plus correlation summary. Keyboard: focus reveals point values; labeled start/end range inputs replace brush dragging.
- Interaction: Hover + Brush.

## 174. Heatmap / Intensity
- Best chart: Heat Map or Choropleth.
- Alternatives: Grid Heat Map, Bubble Heat.
- Use when: Showing intensity/density across a 2D grid; time-based patterns (e.g., activity by hour × day)
- Avoid when: Fewer than 20 cells (use bar); user needs to read exact values; colorblind users without pattern fallback.
- Data volume: Up to 10,000 cells efficiently; beyond that aggregate; calendar heatmap: 365 cells max per SVG.
- Colour: Gradient: Cool (blue) to Hot (red). Divergent scale for ±data. Always include numeric color legend.
- Accessibility risk: `conditional`. Print values or symbols in cells and use texture/labels in addition to the color scale. Do not rely on color alone.
- Fallback: Grid data table plus intensity summary. Keyboard: focus reveals cell values; +/- buttons zoom; Reset restores the grid.
- Interaction: Hover + Zoom.

## 175. Geographic Data
- Best chart: Choropleth Map or Bubble Map.
- Alternatives: Geographic Heat Map.
- Use when: Data has a regional/location dimension; spatial distribution is the core insight for the user.
- Avoid when: Regions have very different sizes making visual comparison misleading (use bar); mobile-primary context.
- Data volume: `<1000` regions: SVG; `≥1000`: Canvas/WebGL; global maps: tile-based rendering.
- Colour: Single color gradient per region group. Categorized colors for discrete types. Legend with clear scale breaks.
- Accessibility risk: `conditional`. Label regions directly and pair fills with boundaries or patterns; location meaning cannot depend on color alone.
- Fallback: Sortable region table plus geographic summary. Keyboard: arrow keys or labeled pan buttons move the map; +/- buttons zoom; Enter drills into a focused region; Back returns.
- Interaction: Pan + Zoom + Drill.

## 176. Funnel / Flow
- Best chart: Funnel Chart or Sankey.
- Alternatives: Waterfall (for flows).
- Use when: Sequential multi-stage process; showing conversion or drop-off rates between defined stages.
- Avoid when: Stages aren't sequential; values don't decrease monotonically (use bar); fewer than 3 stages.
- Data volume: 3–8 stages optimal; beyond 8 stages group minor steps into 'Other'.
- Colour: Stages: single color gradient (start → end). Show conversion % between each stage. Highlight biggest drop.
- Accessibility risk: `conditional`. Keep stage names and values visible and distinguish stages with text and boundaries, not only a gradient. Do not rely on color alone.
- Fallback: Linear stage table/list plus conversion summary. Keyboard: focus reveals stage values; Enter/Space drills in; Back returns.
- Interaction: Hover + Drill.

## 177. Performance vs Target
- Best chart: Gauge Chart or Bullet Chart.
- Alternatives: Dial, Thermometer.
- Use when: Single KPI measured against a defined target or threshold; dashboard summary context.
- Avoid when: No target or benchmark exists; comparing multiple KPIs at once (use bullet chart grid)
- Data volume: Single metric per gauge; for 3+ KPIs use bullet chart grid layout.
- Colour: Performance: Red → Yellow → Green gradient. Target: marker line. Threshold zones clearly differentiated.
- Accessibility risk: `low`. Place the number and target text beside the gauge and label threshold zones; red/yellow/green alone is insufficient.
- Fallback: Visible KPI/target text and a one-row data table plus status summary. Keyboard: focus reveals the same detail as hover.
- Interaction: Hover.

## 178. Time-Series Forecast
- Best chart: Line with Confidence Band.
- Alternatives: Ribbon Chart.
- Use when: Historical data + model predictions; communicating uncertainty range to non-technical stakeholders.
- Avoid when: No historical baseline; prediction confidence is too low to be useful; audience is not data-literate.
- Data volume: Keep historical window to 30–90 days for readability; forecast horizon `≤ 30`% of visible x-axis range.
- Colour: Actual: solid line `#0080FF`. Forecast: dashed `#FF9500`. Confidence band: `15%` opacity fill same hue.
- Accessibility risk: `conditional`. Use solid actual and dashed forecast lines, direct labels, and a named confidence range; hue alone is insufficient.
- Fallback: Visible forecast table plus uncertainty summary. Keyboard: focus reveals hover values; buttons toggle actual/forecast; +/- buttons zoom; Reset restores range.
- Interaction: Hover + Toggle.

## 179. Anomaly Detection
- Best chart: Line Chart with Highlights.
- Alternatives: Scatter with Alert.
- Use when: Monitoring a time-series for outliers; alerting users to unexpected spikes or dips in operational data.
- Avoid when: Anomalies are predefined categories (use bar with highlight); real-time context without a pause control.
- Data volume: Stream at `≤60fps` with Canvas; batch: up to 10,000 pts; mark anomalies as a separate data layer.
- Colour: Normal: `#0080FF` solid line. Anomaly marker: `#FF0000` circle + filled. Alert band: `#FFF3CD` background zone.
- Accessibility risk: `conditional`. Mark anomalies with a distinct shape and text annotation as well as color. Do not rely on color alone.
- Fallback: Anomaly event list/table plus narrative alert summary. Keyboard: focus reveals point details; alerts are available in the persistent list without hover.
- Interaction: Hover + Alert.

## 180. Hierarchical / Nested Data
- Best chart: Treemap.
- Alternatives: Sunburst, Nested Donut, Icicle.
- Use when: Showing size relationships within a hierarchy; overview of proportional structure (e.g., budget breakdown)
- Avoid when: Hierarchy depth `> 3` levels (too complex to read); user needs to compare sibling values precisely.
- Data volume: `<200 nodes`: SVG; 200–1000: Canvas; `>1000`: paginate or pre-filter before rendering.
- Colour: Parent nodes: distinct hues. Children: lighter shades of same hue. White separator borders: `2–3px`.
- Accessibility risk: `high`. Label hierarchy nodes and use borders/patterns as well as hue; make the tree table the primary accessible view. Do not rely on color alone.
- Fallback: Collapsible tree table plus hierarchy summary; treemap remains supplementary. Keyboard: focus reveals hover values; Enter/Space drills or expands; Back collapses/returns.
- Interaction: Hover + Drilldown.

## 181. Flow / Process Data
- Best chart: Sankey Diagram.
- Alternatives: Alluvial, Chord Diagram.
- Use when: Showing how quantities flow between nodes; multi-source multi-target distribution.
- Avoid when: Flow directions form loops (use network graph); fewer than 3 source-target pairs; mobile-primary context.
- Data volume: `<50 flows`: SVG; `≥50`: Canvas; `>200 flows`: aggregate minor flows into 'Other' node.
- Colour: Gradient from source to target color. Flow opacity: 0.4–0.6. Node labels always visible.
- Accessibility risk: `conditional`. Label source, target, and value; use line style or node symbols in addition to gradient color. Do not rely on color alone.
- Fallback: Source-to-target flow table plus flow summary. Keyboard: focus reveals hover values; Enter/Space drills into a node; Back returns.
- Interaction: Hover + Drilldown.

## 182. Cumulative Changes
- Best chart: Waterfall Chart.
- Alternatives: Stacked Bar, Cascade.
- Use when: Showing how individual positive/negative components add up to a final total (e.g., P&L, budget variance)
- Avoid when: Changes are not additive; more than 12 bars (readability breaks); audience expects a simple total.
- Data volume: 4–12 bars optimal; beyond 12 aggregate minor items into a single 'Other' bar.
- Colour: Increases: `#4CAF50`. Decreases: `#F44336`. Start total: `#2196F3`. End total: `#0D47A1`. Running total line: dashed.
- Accessibility risk: `low`. Pair increase/decrease bars with signed values and directional icons, not red/green alone. Do not rely on color alone.
- Fallback: Running-total table plus variance summary. Keyboard: focus reveals the same value as hover.
- Interaction: Hover.

## 183. Multi-Variable Comparison
- Best chart: Radar / Spider Chart.
- Alternatives: Parallel Coordinates, Grouped Bar.
- Use when: Comparing multiple entities across the same fixed set of attributes (e.g., product feature comparison)
- Avoid when: Axes `> 8` (unreadable); values need precise comparison (use grouped bar); audience unfamiliar with radar charts.
- Data volume: 2–3 datasets maximum per chart; 5–8 axes; beyond 8 axes switch to parallel coordinates.
- Colour: Single dataset: `#0080FF` at `20%` fill. Multiple: distinct hues with `30%` fill. Border: full opacity.
- Accessibility risk: `conditional`. Use line styles, point shapes, and direct series labels in addition to color. Do not rely on color alone.
- Fallback: Raw data table and grouped-bar alternative plus comparison summary. Keyboard: focus reveals values; buttons toggle series.
- Interaction: Hover + Toggle.

## 184. Stock / Trading OHLC
- Best chart: Candlestick Chart.
- Alternatives: OHLC Bar, Heikin-Ashi.
- Use when: Financial time-series with Open/High/Low/Close data; trading or investment product context only.
- Avoid when: Non-financial audience; no OHLC data available (use line chart); accessibility-first context.
- Data volume: Real-time: Canvas required. Historical: paginate by time range. Max 500 candles visible at once.
- Colour: Bullish: `#26A69A`. Bearish: `#EF5350`. Volume bars: `40%` opacity below. Body fill vs hollow for OHLC style.
- Accessibility risk: `conditional`. Use filled versus hollow candles and OHLC text values; bullish/bearish meaning cannot depend on color. Do not rely on color alone.
- Fallback: Sortable OHLC table plus daily-change summary. Keyboard: focus reveals candle values; +/- buttons zoom; Reset restores range; live updates do not steal focus.
- Interaction: Real-time + Hover + Zoom.

## 185. Relationship / Connection Data
- Best chart: Network Graph.
- Alternatives: Hierarchical Tree, Adjacency Matrix.
- Use when: Mapping connections between entities; network topology or social graph exploration context.
- Avoid when: Node count `> 500` without clustering pre-applied; user needs precise connection counts; mobile context.
- Data volume: `≤100 nodes`: SVG; 101–500: Canvas; `>500`: must apply clustering/LOD before rendering.
- Colour: Node types: categorical colors. Edges: `#90A4AE` at `60%` opacity. Highlight path: `#F59E0B`.
- Accessibility risk: `high`. Use labeled node types, shapes, and edge styles in addition to color; the adjacency view is the accessible source of truth. Do not rely on color alone.
- Fallback: Adjacency list/table and relationship summary; tree view when applicable. Keyboard: focus reveals node details; Enter drills; Move up/down/left/right buttons replace drag.
- Interaction: Drilldown + Hover + Drag.

## 186. Distribution / Statistical
- Best chart: Box Plot.
- Alternatives: Violin Plot, Beeswarm.
- Use when: Showing spread, median, and outliers of a dataset; comparing distributions across multiple groups.
- Avoid when: Fewer than 20 data points per group (distribution is not meaningful); audience unfamiliar with statistical charts.
- Data volume: Any sample size; aggregated representation so rendering is excellent at any volume.
- Colour: Box fill: `#BBDEFB`. Border: `#1976D2`. Median line: `#D32F2F` bold. Outlier dots: `#F44336`.
- Accessibility risk: `low`. Label median, quartiles, whiskers, and outliers directly; do not use color alone for statistical roles.
- Fallback: Statistics table plus distribution summary. Keyboard: focus reveals the same statistics as hover.
- Interaction: Hover.

## 187. Performance vs Target (Compact)
- Best chart: Bullet Chart.
- Alternatives: Gauge, Progress Bar.
- Use when: Dashboard with multiple KPIs side by side; space-constrained contexts where a gauge is too large.
- Avoid when: Single KPI with emphasis (use gauge); data has no defined target range; fewer than 3 KPIs.
- Data volume: Ideal for 3–10 bullet charts in a grid; scales to any count efficiently.
- Colour: Qualitative ranges: `#FFCDD2` / `#FFF9C4` / `#C8E6C9` (bad/ok/good). Performance bar: `#1976D2`. Target: black `3px` marker.
- Accessibility risk: `low`. Label every qualitative range and target with text; color is supplementary.
- Fallback: Visible KPI/target table plus status summary. Keyboard: focus reveals the same detail as hover.
- Interaction: Hover.

## 188. Proportional / Percentage
- Best chart: Waffle Chart.
- Alternatives: Pictogram, Stacked Bar 100%.
- Use when: Showing what fraction of a whole is filled; percentage progress in a visually engaging and accessible format.
- Avoid when: More than 5 categories (use stacked bar); exact values matter over visual proportion; very tight space.
- Data volume: `10×10` grid standard (100 cells); for `> 5` categories switch to stacked `100%` bar.
- Colour: 3–5 categories max. `2–3px` gap between cells. Each category a distinct accessible color pair.
- Accessibility risk: `low`. Label each category and percentage and add patterns or symbols; filled-cell color alone is insufficient.
- Fallback: Percentage table/list plus part-to-whole summary. Keyboard: focus reveals each cell value.
- Interaction: Hover.

## 189. Hierarchical Proportional
- Best chart: Sunburst Chart.
- Alternatives: Treemap, Icicle, Circle Packing.
- Use when: Exploring nested proportions where both hierarchy and relative size matter (e.g., org spend breakdown)
- Avoid when: More than 3 hierarchy levels (outer rings become unreadable); precision matters over overview; mobile.
- Data volume: `<100 nodes`: SVG; 100–500: Canvas; `>500`: filter to top N before rendering.
- Colour: Center to outer: darker to lighter hue. Each level `15–20%` lighter. Contrasting border between sectors.
- Accessibility risk: `high`. Label hierarchy levels and segments and use boundaries/patterns as well as hue; the indented list is primary. Do not rely on color alone.
- Fallback: Collapsible indented list/table plus hierarchy summary and breadcrumbs. Keyboard: Enter/Space drills or expands; Back button returns; focus reveals hover detail.
- Interaction: Drilldown + Hover.

## 190. Root Cause Analysis
- Best chart: Decomposition Tree.
- Alternatives: Decision Tree, Flow Chart.
- Use when: Decomposing a metric into contributing factors; AI-assisted analysis or BI drill-down scenarios.
- Avoid when: No clear parent-child causal relationship; audience expects a summary rather than exploration.
- Data volume: Up to 5 levels deep; limit visible nodes to 20 per level for readability; lazy-load deeper levels.
- Colour: Positive impact nodes: `#2563EB`. Negative impact nodes: `#EF4444`. Neutral connectors: `#94A3B8`.
- Accessibility risk: `low`. Name each node and contribution and use shapes/connector styles in addition to color. Do not rely on color alone.
- Fallback: Expandable tree table plus root-cause summary. Keyboard: Enter/Space drills and expands; Back collapses; dedicated expand/collapse buttons expose the same operations.
- Interaction: Drill + Expand.

## 191. 3D Spatial Data
- Best chart: 3D Scatter / Surface Plot.
- Alternatives: Volumetric Rendering, Point Cloud.
- Use when: Scientific/engineering context where Z-axis carries essential info not expressible in 2D.
- Avoid when: 2D projection conveys the same insight; mobile context; accessibility-required environments; standard business dashboards.
- Data volume: WebGL required; GPU point layers handle up to `1M` points; apply level-of-detail beyond `50,000` points.
- Colour: Depth cues: lighting and shading. Z-axis: color gradient (cool → warm). Transparent overlapping: opacity 0.4.
- Accessibility risk: `high`. Use labels, shapes, and depth-independent cues; color and 3D position cannot be the only carriers of meaning.
- Fallback: Mandatory 2D projection, data table, and spatial summary. Keyboard: rotate/pan buttons and +/- zoom controls replace pointer/VR manipulation; Reset returns the camera.
- Interaction: Rotate + Zoom + VR.

## 192. Real-Time Streaming
- Best chart: Streaming Area Chart.
- Alternatives: Ticker Tape, Moving Gauge.
- Use when: Live monitoring dashboards; IoT/ops data updating at `≥1` Hz; user needs current value at a glance.
- Avoid when: Update frequency `< 1`/min (use periodic-refresh line chart); flashing content without reduced-motion support.
- Data volume: Canvas/WebGL required. Buffer last `60–300s` of data. Downsample older data on scroll.
- Colour: Current pulse: `#00FF00` (dark theme) or `#0080FF` (light theme). History: fading opacity. Grid: dark background.
- Accessibility risk: `conditional`. Show the current value and status text and use line styles or markers in addition to color. Do not rely on color alone.
- Fallback: Streaming data table plus current-value/trend summary. Keyboard: Pause/Resume button controls updates; focus reveals values; +/- buttons zoom; Reset restores range.
- Interaction: Real-time + Pause + Zoom.

## 193. Sentiment / Emotion
- Best chart: Word Cloud with Sentiment.
- Alternatives: Sentiment Arc, Radar Chart.
- Use when: NLP output visualization; exploratory analysis of text corpus sentiment; frequency-weighted keyword overview.
- Avoid when: Precise values matter (word size is inherently imprecise); screen-reader context; corpus `< 50` items.
- Data volume: 50–5000 terms optimal. Beyond 5000: apply top-N filtering before render. Avoid on mobile.
- Colour: Positive: `#22C55E`. Negative: `#EF4444`. Neutral: `#94A3B8`. Word size maps to frequency.
- Accessibility risk: `high`. Expose every term, count, and sentiment as text; size and color are supplementary only.
- Fallback: Sortable term table/list plus sentiment summary; word cloud is supplementary. Keyboard: focus reveals word details; labeled controls filter with Space/Enter.
- Interaction: Hover + Filter.

## 194. Process Mining
- Best chart: Process Map / Graph.
- Alternatives: Directed Acyclic Graph (DAG), Petri Net.
- Use when: Analyzing event logs to visualize actual process flows; identifying bottlenecks and deviations in ops/product funnels.
- Avoid when: No event log data available; audience expects a static flowchart (use diagram tool); node count `> 100` without pre-filtering.
- Data volume: `<30 nodes`: SVG; 30–100: Canvas; `>100`: apply variant filtering (top `80%` of cases) before rendering.
- Colour: Happy path: `#10B981` thick line. Deviations: `#F59E0B` thin line. Bottleneck nodes: `#EF4444` fill.
- Accessibility risk: `conditional`. Label nodes and paths and use shapes/line styles in addition to color; bottlenecks require text annotations. Do not rely on color alone.
- Fallback: Path summary table plus bottleneck narrative. Keyboard: Move buttons replace drag; focus reveals node details; Enter activates a node; Back returns.
- Interaction: Drag + Node-Click.

# Part 24 — Landing Page Patterns

## 195. Hero + Features + CTA
- Section order: Hero with headline/image > Value prop > Key features (3-5) > CTA section > Footer.
- CTA placement: Hero (sticky) + Bottom.
- Colour strategy: Hero: Brand primary or vibrant. Features: Card bg `#FAFAFA`. CTA: Contrasting accent color.
- Effects: Hero parallax, feature card hover lift, CTA glow on hover.
- Conversion tips: Deep CTA placement. For CTA label text, verify at least `4.5:1` against the button fill; use `7:1` only when the product explicitly targets AAA normal-text contrast. Keep focus and component boundaries independently visible. Disable hero parallax under reduced motion and render its static final state.

## 196. Hero + Testimonials + CTA
- Section order: Hero > Problem statement > Solution overview > Testimonials carousel > CTA.
- CTA placement: Hero (sticky) + Post-testimonials.
- Colour strategy: Hero: Brand color. Testimonials: Light bg `#F5F5F5`. Quotes: Italic, muted color `#666`. CTA: Vibrant.
- Effects: Testimonial carousel slide animations, quote marks animations, avatar fade-in.
- Conversion tips: Social proof before CTA. Use a concise set of verified testimonials with photo, name, and role. CTA after social proof. Provide previous/next and pause controls; stop rotation on focus, hover, and reduced motion; announce slide position. Previous/next buttons and keyboard controls must expose every slide without dragging.

## 197. Product Demo + Features
- Section order: Hero > Product video/mockup (center) > Feature breakdown per section > Comparison (optional) > CTA.
- CTA placement: Video center + CTA right/bottom.
- Colour strategy: Video surround: Brand color overlay. Features: Icon color `#0080FF`. Text: Dark `#222`.
- Effects: Video play button pulse, feature scroll reveals, demo interaction highlights.
- Conversion tips: Use an interactive demo only when it explains value better than static media. Provide captions, transcript, visible play/pause controls, and a non-video fallback; do not autoplay under reduced motion. Pause media when offscreen or hidden and keep the final product state available as static content.

## 198. Minimal Single Column
- Section order: Hero headline > Short description > Benefit bullets (3 max) > CTA > Footer.
- CTA placement: Center, large CTA button.
- Colour strategy: Minimalist: Brand + white `#FFFFFF` + accent. Verify CTA label text against its button fill at `4.5:1` minimum; use `7:1` only for an explicit AAA normal-text target.
- Effects: Minimal hover effects. Smooth scroll. CTA scale on hover (subtle)
- Conversion tips: Single CTA focus. Large typography. Lots of whitespace. No nav clutter. Mobile-first.

## 199. Funnel (3-Step Conversion)
- Section order: Hero > Step 1 (problem) > Step 2 (solution) > Step 3 (action) > CTA progression.
- CTA placement: Each step: mini-CTA. Final: main CTA.
- Colour strategy: Step colors: 1 (Red/Problem), 2 (Orange/Process), 3 (Green/Solution). CTA: Brand color.
- Effects: Step number animations, progress bar fill, step transitions smooth scroll.
- Conversion tips: Progressive disclosure. Show only essential info per step. Use progress indicators. Multiple CTAs.

## 200. Comparison Table + CTA
- Section order: Hero > Problem intro > Comparison table (product vs competitors) > Pricing (optional) > CTA.
- CTA placement: Table: Right column. CTA: Below table.
- Colour strategy: Table: Alternating rows (white/light grey). Your product: Highlight `#FFFACD` (light yellow) or green. Text: Dark.
- Effects: Table row hover highlight, price toggle animations, feature checkmark animations.
- Conversion tips: Use comparison to show unique value. Highlight your product row. Include 'free trial' in pricing row.

## 201. Lead Magnet + Form
- Section order: Hero (benefit headline) > Lead magnet preview (ebook cover, checklist, etc) > Form (minimal fields) > CTA submit.
- CTA placement: Form CTA: Submit button.
- Colour strategy: Lead magnet: Professional design. Form: Clean white bg. Inputs: Light border `#CCCCCC`. CTA: Brand color.
- Effects: Form focus state animations, input validation animations, success confirmation animation.
- Conversion tips: Ask only for information necessary to deliver the lead magnet. Preview its value and show submission progress.

## 202. Pricing Page + CTA
- Section order: Hero (pricing headline) > Price comparison cards > Feature comparison table > FAQ section > Final CTA.
- CTA placement: Each card: CTA button. Sticky CTA in nav.
- Colour strategy: Free: Grey, Starter: Blue, Pro: Green/Gold, Enterprise: Dark. Cards: `1px` border, shadow.
- Effects: Price toggle animation (monthly/yearly), card comparison highlight, FAQ accordion open/close.
- Conversion tips: Highlight the plan that matches the intended audience and show actual annual savings transparently. Use FAQs to address concerns.

## 203. Video-First Hero
- Section order: Hero with video background > Key features overlay > Benefits section > CTA.
- CTA placement: Overlay on video (center/bottom) + Bottom section.
- Colour strategy: Use an overlay strong enough for text contrast. Brand accent for CTA. Light text only when the measured contrast passes.
- Effects: Video autoplay muted, parallax scroll, text fade-in on scroll.
- Conversion tips: Use video only when it demonstrates value better than static media. Add captions for accessibility. Compress video for performance. Provide captions and a visible pause control; use a static poster when reduced motion is requested. Pause video when offscreen or hidden; the reduced-motion poster must preserve the final message and CTA.

## 204. Scroll-Triggered Storytelling
- Section order: Intro hook > Chapter 1 (problem) > Chapter 2 (journey) > Chapter 3 (solution) > Climax CTA.
- CTA placement: End of each chapter (mini) + Final climax CTA.
- Colour strategy: Progressive reveal. Each chapter has distinct color. Building intensity.
- Effects: Scroll-triggered animations, parallax layers, progressive disclosure, chapter transitions.
- Conversion tips: Keep the narrative understandable without scroll-driven effects. Use progress indicator. Mobile: simplify animations. Keep DOM reading order complete; disable parallax and scroll-scrub under reduced motion. Pause scroll animation when offscreen or hidden and render each chapter in its final readable state under reduced motion.

## 205. AI Personalization Landing
- Section order: Dynamic hero (personalized) > Relevant features > Tailored testimonials > Smart CTA.
- CTA placement: Context-aware placement based on user segment.
- Colour strategy: Adaptive based on user data. A/B test color variations per segment.
- Effects: Dynamic content swap, fade transitions, personalized product recommendations.
- Conversion tips: Validate personalization with consent-aware product analytics. Requires analytics integration. Fallback for new users.

## 206. Waitlist/Coming Soon
- Section order: Hero with countdown > Product teaser/preview > Email capture form > Social proof (waitlist count)
- CTA placement: Email form prominent (above fold) + Sticky form on scroll.
- Colour strategy: Anticipation: Dark + accent highlights. Countdown in brand color. Urgency indicators.
- Effects: Countdown timer animation, email validation feedback, success confetti, social share buttons.
- Conversion tips: Explain early-access benefits without fabricated scarcity. Show a waitlist count only when it is current, verified, and dated. Provide a static launch deadline, pause decorative countdown motion when offscreen/hidden, and render the final readable timer state under reduced motion. Email form and referral actions remain keyboard operable.

## 207. Comparison Table Focus
- Section order: Hero (problem statement) > Comparison matrix (you vs competitors) > Feature deep-dive > Winner CTA.
- CTA placement: After comparison table (highlighted row) + Bottom.
- Colour strategy: Your product column highlighted (accent bg or green). Competitors neutral. Checkmarks green.
- Effects: Table row hover highlight, feature checkmark animations, sticky comparison header.
- Conversion tips: Show value vs competitors. Measure comparison performance with product-specific analytics. Be factual. Include pricing if favorable.

## 208. Pricing-Focused Landing
- Section order: Hero (value proposition) > Pricing cards (3 tiers) > Feature comparison > FAQ > Final CTA.
- CTA placement: Each pricing card + Sticky CTA in nav + Bottom.
- Colour strategy: Popular plan highlighted (brand color border/bg). Free: grey. Enterprise: dark/premium.
- Effects: Price toggle monthly/annual animation, card hover lift, FAQ accordion smooth open.
- Conversion tips: Show actual monthly and annual totals and savings transparently. Explain plan differences and address objections in the FAQ.

## 209. App Store Style Landing
- Section order: Hero with device mockup > Screenshots carousel > Features with icons > Reviews/ratings > Download CTAs.
- CTA placement: Download buttons prominent (App Store + Play Store) throughout.
- Colour strategy: Dark/light matching app store feel. Star ratings in gold. Screenshots with device frames.
- Effects: Device mockup rotations, screenshot slider, star rating animations, download button pulse.
- Conversion tips: Show real screenshots and only current verified ratings. Provide platform-specific CTAs, buttons and keyboard controls in addition to swipe, and pause any auto-rotation. Stop auto-rotation on focus, hover, offscreen/hidden, or reduced motion and render the selected screenshot as the static final state.

## 210. FAQ/Documentation Landing
- Section order: Hero with search bar > Popular categories > FAQ accordion > Contact/support CTA.
- CTA placement: Search bar prominent + Contact CTA for unresolved questions.
- Colour strategy: Clean, high readability. Minimal color. Category icons in brand color. Success green for resolved.
- Effects: Search autocomplete, smooth accordion open/close, category hover, helpful feedback buttons.
- Conversion tips: Reduce support tickets. Track search analytics. Show related articles. Contact escalation path.

## 211. Immersive/Interactive Experience
- Section order: Full-screen interactive element > Guided product tour > Key benefits revealed > CTA after completion.
- CTA placement: After interaction complete + Skip option for impatient users.
- Colour strategy: Immersive experience colors. Dark background for focus. Highlight interactive elements.
- Effects: WebGL, 3D interactions, gamification elements, progress indicators, reward animations.
- Conversion tips: Measure engagement for the specific audience and device mix. Performance trade-off. Provide skip option. Mobile fallback essential. Provide skip, keyboard, reduced-motion, and non-3D fallback paths. Pause animation when offscreen/hidden and preserve the completed final state when reduced motion is enabled.

## 212. Event/Conference Landing
- Section order: Hero (date/location/countdown) > Speakers grid > Agenda/schedule > Sponsors > Register CTA.
- CTA placement: Register CTA sticky + After speakers + Bottom.
- Colour strategy: Urgency colors (countdown). Event branding. Speaker cards professional. Sponsor logos neutral.
- Effects: Countdown timer, speaker hover cards with bio, agenda tabs, early bird countdown.
- Conversion tips: Early bird pricing with deadline. Social proof (past attendees). Speaker credibility. Multi-ticket discounts. Expose the exact deadline as text; pause decorative countdown motion offscreen/hidden and show a static final state under reduced motion.

## 213. Product Review/Ratings Focused
- Section order: Hero (product + aggregate rating) > Rating breakdown > Individual reviews > Buy/CTA.
- CTA placement: After reviews summary + Buy button alongside reviews.
- Colour strategy: Trust colors. Star ratings gold. Verified badge green. Review sentiment colors.
- Effects: Star fill animations, review filtering, helpful vote interactions, photo lightbox.
- Conversion tips: User-generated content builds trust. Show verified purchases. Filter by rating. Respond to negative reviews.

## 214. Community/Forum Landing
- Section order: Hero (community value prop) > Popular topics/categories > Active members showcase > Join CTA.
- CTA placement: Join button prominent + After member showcase.
- Colour strategy: Warm, welcoming. Member photos add humanity. Topic badges in brand colors. Activity indicators green.
- Effects: Member avatars animation, activity feed live updates, topic hover previews, join success celebration.
- Conversion tips: Preview real community value and simplify onboarding. Show member and activity counts only when current, verified, and dated; label activity as live only when backed by an active real-time source. Provide pause/update-frequency controls for moving feeds, stop work offscreen/hidden, and keep a static final state under reduced motion.

## 215. Before-After Transformation
- Section order: Hero (problem state) > Transformation slider/comparison > How it works > Results CTA.
- CTA placement: After transformation reveal + Bottom.
- Colour strategy: Contrast: muted/grey (before) vs vibrant/colorful (after). Success green for results.
- Effects: Slider comparison interaction, before/after reveal animations, result counters, testimonial videos.
- Conversion tips: Visual proof of value. Measure the outcome with product-specific analytics. Real results. Specific metrics. Guarantee offer. Provide arrow buttons and keyboard steps so dragging is not required. Arrow buttons and keyboard steps expose the same final before/after positions; reduced motion removes reveal animation.

## 216. Marketplace / Directory
- Section order: Hero (Search focused) > Categories > Featured Listings > Trust/Safety > CTA (Become a host/seller)
- CTA placement: Hero Search Bar + Navbar 'List your item'.
- Colour strategy: Search: High contrast. Categories: Visual icons. Trust: Blue/Green.
- Effects: Search autocomplete animation, map hover pins, card carousel.
- Conversion tips: Search is the primary CTA. Reduce friction with useful suggestions. For featured-listing carousels, provide previous/next and play/pause buttons, full keyboard access, and a single-pointer alternative to swiping; stop rotation on focus, hover, offscreen/hidden, or reduced motion and render the selected listing as the static final state.

## 217. Newsletter / Content First
- Section order: Hero (Value Prop + Form) > Recent Issues/Archives > Social Proof (Subscriber count) > About Author.
- CTA placement: Hero inline form + Sticky header form.
- Colour strategy: Minimalist. Paper-like background. Text focus. Accent color for Subscribe.
- Effects: Text highlight animations, typewriter effect, subtle fade-in.
- Conversion tips: Keep the form to the fields actually required and link to a sample issue. Show a subscriber count only when it is current, verified, and dated; otherwise use qualitative social proof.

## 218. Webinar Registration
- Section order: Hero (Topic + Timer + Form) > What you'll learn > Speaker Bio > Urgency/Bonuses > Form (again)
- CTA placement: Hero (Right side form) + Bottom anchor.
- Colour strategy: Urgency: Red/Orange. Professional: Blue/Navy. Form: High contrast white.
- Effects: Countdown timer, speaker avatar float, urgent ticker.
- Conversion tips: State the event time and timezone in text. Claim limited seats or live status only when current capacity or stream state is verified and timestamped. Provide pause/hide controls for the urgency ticker, stop it offscreen/hidden, keep controls keyboard operable, and render a static final state under reduced motion.

## 219. Enterprise Gateway
- Section order: Hero (Video/Mission) > Solutions by Industry > Solutions by Role > Client Logos > Contact Sales.
- CTA placement: Contact Sales (Primary) + Login (Secondary)
- Colour strategy: Corporate: Navy/Grey. High integrity. Conservative accents.
- Effects: Slow video background, logo carousel, tab switching for industries.
- Conversion tips: Path selection (I am a...). Mega menu navigation. Trust signals prominent. Provide pause/stop for video and rotating logos; stop on focus and reduced motion. Logo carousel controls must be keyboard operable; pause moving media offscreen/hidden and render a static final state under reduced motion.

## 220. Portfolio Grid
- Section order: Hero (Name/Role) > Project Grid (Masonry) > About/Philosophy > Contact.
- CTA placement: Project Card Hover + Footer Contact.
- Colour strategy: Neutral background (let work shine). Text: Black/White. Accent: Minimal.
- Effects: Image lazy load reveal, hover overlay info, lightbox view.
- Conversion tips: Visuals first. Filter by category. Fast loading essential.

## 221. Horizontal Scroll Journey
- Section order: Intro (Vertical) > The Journey (Horizontal Track) > Detail Reveal > Vertical Footer.
- CTA placement: Floating Sticky CTA or End of Horizontal Track.
- Colour strategy: Continuous palette transition. Chapter colors. Progress bar `#000000`.
- Effects: Scroll-jacking (careful), parallax layers, horizontal slide, progress indicator.
- Conversion tips: Immersive product discovery. High engagement. Keep navigation visible. Preserve a normal vertical navigation path and disable scroll-jacking under reduced motion. Pause effects when offscreen/hidden and render every chapter in its final vertical reading state under reduced motion.

## 222. Bento Grid Showcase
- Section order: Hero > Bento Grid (Key Features) > Detail Cards > Tech Specs > CTA.
- CTA placement: Floating Action Button or Bottom of Grid.
- Colour strategy: Card backgrounds: `#F5F5F7` or Glass. Icons: Vibrant brand colors. Text: Dark.
- Effects: Hover card scale (1.02), video inside cards, tilt effect, staggered reveal.
- Conversion tips: Scannable value props. High information density without clutter. Mobile stack. Keep cards usable without hover and suppress tilt/stagger/video motion under reduced motion. Pause card media offscreen/hidden and render cards in their final readable state under reduced motion.

## 223. Interactive 3D Configurator
- Section order: Hero (Configurator) > Feature Highlight (synced) > Price/Specs > Purchase.
- CTA placement: Inside Configurator UI + Sticky Bottom Bar.
- Colour strategy: Neutral studio background. Product: Realistic materials. UI: Minimal overlay.
- Effects: Real-time rendering, material swap animation, camera rotate/zoom, light reflection.
- Conversion tips: Let users inspect product details before purchase. Provide buttons and keyboard controls for rotate/zoom plus a 2D/specification fallback. Named rotate/zoom buttons and keyboard controls replace drag gestures; pause rendering offscreen/hidden and preserve the chosen configuration as the reduced-motion final state.

## 224. AI-Driven Dynamic Landing
- Section order: Prompt/Input Hero > Generated Result Preview > How it Works > Value Prop.
- CTA placement: Input Field (Hero) + 'Try it' Buttons.
- Colour strategy: Adaptive to user input. Dark mode for compute feel. Neon accents.
- Effects: Typing text effects, shimmering generation loaders, morphing layouts.
- Conversion tips: Immediate value demonstration. 'Show, don't tell'. Low friction start. Disable typing, shimmer, and morphing effects when reduced motion is requested. Pause loaders offscreen/hidden and render generated content in its final state under reduced motion.

## 225. Feature-Rich Showcase
- Section order: Hero (value prop) > Feature grid/cards (4-6) > Use cases or benefits > Social proof or logos > CTA.
- CTA placement: Hero (sticky) + After features + Bottom.
- Colour strategy: Brand primary + card bg `#FAFAFA`. Feature icons accent. CTA contrasting.
- Effects: Feature card hover lift, scroll reveal, icon micro-interactions.
- Conversion tips: Clear feature hierarchy. One key message per card. Strong CTA repetition.

## 226. Hero-Centric Design
- Section order: Full-bleed Hero (headline + visual) > Single value prop strip > Key benefit or proof > Primary CTA.
- CTA placement: Hero dominant (center/bottom) + Sticky nav CTA.
- Colour strategy: Hero: High-impact visual. Minimal text. Verify CTA label text against the button fill at `4.5:1` minimum; use `7:1` only for an explicit AAA normal-text target.
- Effects: Hero parallax or video, CTA pulse on scroll, minimal chrome.
- Conversion tips: One primary CTA. Let the hero dominate the initial viewport without hiding the next content cue. Use a static hero and non-pulsing CTA when reduced motion is requested; provide video controls. Pause hero media offscreen/hidden and keep the final hero message and CTA static under reduced motion.

## 227. Trust & Authority + Conversion
- Section order: Hero (mission/credibility) > Proof (logos, certs, stats) > Solution overview > Clear CTA path.
- CTA placement: Contact Sales / Get Quote (primary) + Nav.
- Colour strategy: Navy/Grey corporate. Trust blue. Accent for CTA only.
- Effects: Logo carousel, stat counters, testimonial strip.
- Conversion tips: Security badges. Case studies. Transparent pricing. Low-friction form. Provide pause/stop and stop the logo carousel on focus, hover, and reduced motion. Previous/next controls provide the keyboard equivalent; pause offscreen/hidden and render a static logo set under reduced motion.

## 228. Real-Time / Operations Landing
- Section order: Hero (product + live preview or status) > Key metrics/indicators > How it works > CTA (Start trial / Contact)
- CTA placement: Primary CTA in nav + After metrics.
- Colour strategy: Dark or neutral. Status colors (green/amber/red). Data-dense but scannable.
- Effects: Live data ticker, status pulse, minimal decoration.
- Conversion tips: Offer a demo or sandbox and show trust signals. Label telemetry as live only when backed by a current source, with update time and stale state. Provide pause/hide or update-frequency controls for tickers and previews, stop offscreen/hidden work, support keyboard controls, and render a static final snapshot under reduced motion.

# Part 25 — UI/UX Rule Priorities & Pre-Delivery Checklist

## 229. Rule Category Priority Order
- Work through categories in priority order: 1 Accessibility (CRITICAL), 2 Touch & Interaction (CRITICAL), 3 Performance (HIGH), 4 Style Selection (HIGH), 5 Layout & Responsive (HIGH), 6 Typography & Color (MEDIUM), 7 Animation (MEDIUM), 8 Forms & Feedback (MEDIUM), 9 Navigation Patterns (HIGH), 10 Charts & Data (LOW).
- Apply this guidance whenever a task changes how something looks, feels, moves or is interacted with; skip it for purely non-visual work.
- Before designing, extract product type (SaaS, e-commerce, portfolio, dashboard, entertainment, tool, productivity, hybrid), audience and usage context (commute, leisure, work), style keywords (playful, vibrant, minimal, dark mode, content-first, immersive) and the target platform.
- Never assume a platform or stack; a wrong default silently misroutes every recommendation.
- When no verified guidance matches, say the recommendation is a general fallback rather than presenting it as a matched result.

## 230. Accessibility Essentials
- Contrast minimum `4.5:1` for normal text, `3:1` for large text.
- Visible focus rings on interactive elements, `2–4px`; never remove focus rings.
- Descriptive alt text for meaningful images.
- Icon-only buttons need an accessible label (`aria-label` on web, accessibility label in native).
- Icon semantics depend on use: hide decorative icons beside visible text from the accessibility tree, give meaningful standalone icons a text alternative, give icon controls an accessible name plus selected/pressed/expanded state.
- Tab order matches visual order; full keyboard support.
- Use a `label` with a `for` attribute for every input.
- Provide a skip-to-main-content link for keyboard users.
- Sequential heading hierarchy `h1`→`h6` with no skipped levels.
- Never convey information by color alone; add icon or text.
- Support system text scaling (Dynamic Type) and avoid truncation as text grows.
- Respect `prefers-reduced-motion`; reduce or disable animation when requested.
- Meaningful screen-reader labels/hints and a logical reading order.
- Provide cancel/back escape routes in modals and multi-step flows.
- Preserve system and accessibility shortcuts; offer keyboard alternatives for drag-and-drop.

## 231. WCAG 2.2 Additions
- Focus not obscured (AA): sticky UI, overlays and banners must not hide the keyboard-focused control; enhanced (AAA) keeps the entire focused component visible.
- Focus appearance (AAA): verify focus indicator area and `3:1` state contrast; visible focus alone is not enough.
- Dragging alternative (AA): every author-controlled drag action needs a single-pointer and keyboard alternative.
- Web target size (AA): pointer targets at least `24×24` CSS px or a documented exception; do not substitute native units.
- Consistent help (A): repeated help mechanisms stay in the same relative order across a page set.
- Redundant entry (A): reuse information already supplied in the same process unless re-entry is essential.
- Accessible authentication (AA): allow password managers and paste; provide a non-cognitive authentication path.
- Auto-rotating carousels and moving content need pause/stop controls and must stop on focus or reduced motion.
- Announce changed counts/status as a complete contextual phrase without moving focus; use one appropriate live/status region and atomic updates only when needed.

## 232. Touch & Interaction
- Touch targets minimum `44×44pt` (iOS) / `48×48dp` (Android); extend the hit area beyond visual bounds when the icon is smaller.
- Minimum `8px`/`8dp` gap between touch targets.
- Use click/tap for primary interactions; never rely on hover alone.
- Disable buttons during async operations and show a spinner or progress.
- Place clear error messages near the problem.
- Add `cursor-pointer` to clickable web elements.
- Avoid horizontal swipe on main content; prefer vertical scroll.
- Use `touch-action: manipulation` to remove the `300ms` tap delay on web.
- Use platform-standard gestures consistently (swipe-back, pinch-zoom); never block system gestures.
- Visual press feedback (ripple, highlight, state layers); use haptics for confirmations and important actions without overuse.
- Never rely on gesture-only interactions; critical actions need visible controls.
- Keep primary targets away from notch, Dynamic Island, gesture bar and screen edges.
- Avoid pixel-perfect taps on small icons or thin edges.
- Swipe actions show a clear affordance (chevron, label, tutorial).
- Use a movement threshold before starting a drag.

## 233. Performance
- Use WebP/AVIF, responsive images (`srcset`/`sizes`) and lazy-load non-critical assets.
- Declare width/height or `aspect-ratio` to prevent layout shift; keep CLS `< 0.1`.
- Use `font-display: swap` or `optional` to avoid invisible text; preload only critical fonts.
- Prioritize above-the-fold CSS; split code by route/feature; load third-party scripts async/defer.
- Batch DOM reads then writes; reserve space for async content.
- Use `loading="lazy"` for below-the-fold images and heavy media.
- Virtualize lists of `50+` items.
- Keep per-frame work under `~16ms` for 60fps; input latency under `~100ms`; visual tap feedback within `100ms`.
- Use skeleton/shimmer instead of blocking spinners for operations `>1s`.
- Debounce/throttle scroll, resize and input events.
- Provide offline messaging and degraded modes for slow networks (lower-res images, fewer animations).

## 234. Style Selection
- Match visual style to product type and use the same style across all pages.
- Use SVG icons, never emoji, as icons.
- Choose the palette from the product and industry.
- Align shadows, blur and radius with the chosen style (glass, flat, clay).
- Respect platform idioms (iOS HIG vs Material) for navigation, controls, typography and motion.
- Make hover/pressed/disabled states visually distinct while staying on-style.
- Use one consistent elevation/shadow scale for cards, sheets and modals.
- Design light and dark variants together.
- Use one icon set and visual language (stroke width, corner radius).
- Prefer native/system controls; customize only when branding requires it.
- Use blur to indicate background dismissal, not as decoration.
- One primary CTA per screen; secondary actions visually subordinate.
- Anti-patterns: mixing flat and skeuomorphic randomly, emoji as icons.

## 235. Layout & Responsive
- Viewport meta `width=device-width initial-scale=1`; never disable zoom.
- Design mobile-first and scale up to tablet and desktop.
- Systematic breakpoints, e.g. `375 / 768 / 1024 / 1440`.
- Minimum `16px` body text on mobile (avoids iOS auto-zoom).
- Line length `35–60` characters on mobile, `60–75` on desktop.
- No horizontal scroll on mobile; no fixed px container widths.
- Use a `4pt/8dp` incremental spacing system.
- Consistent desktop max-width (`max-w-6xl` / `max-w-7xl`).
- Layered z-index scale, e.g. `0 / 10 / 20 / 40 / 100 / 1000`.
- Fixed navbars/bottom bars reserve safe padding for underlying content.
- Avoid nested scroll regions.
- Prefer `min-h-dvh` over `100vh` on mobile.
- Keep layouts readable and operable in landscape.
- Show core content first on mobile; fold or hide secondary content.
- Establish hierarchy via size, spacing and contrast, not color alone.
- Choose badge, status tag, filter chip or removable value from its semantics; keep essential labels available and disclose unavoidable truncation to pointer and keyboard users.
- Wrap chip collections before shrinking labels; make a `+n` overflow summary an operable disclosure.

## 236. Typography & Color
- Body line-height `1.5–1.75`; line length `65–75` characters.
- Match heading/body font personalities.
- Consistent type scale, e.g. `12 14 16 18 24 32`.
- Darker text on light backgrounds (e.g. `slate-900` on white); avoid gray-on-gray and body text `< 12px`.
- Use the platform type system (Dynamic Type styles / Material type roles: display, headline, title, body, label).
- Weight hierarchy: headings `600–700`, body `400`, labels `500`.
- Define semantic color tokens (primary, secondary, error, surface, on-surface); no raw hex in components.
- Dark mode uses desaturated/lighter tonal variants, not inverted colors; test contrast separately.
- Foreground/background pairs meet `4.5:1` (AA) or `7:1` (AAA).
- Functional color (error red, success green) must include icon/text.
- Prefer wrapping over truncation; when truncating use ellipsis and expose full text via tooltip/expand.
- Respect default platform letter-spacing; avoid tight tracking on body text.
- Use tabular/monospaced figures for data columns, prices and timers.
- Use whitespace intentionally to group related items and separate sections.
- Balanced heading wrapping is a progressive heuristic; never force final words together with blanket non-breaking spaces.
- Let URLs, IDs and user content reflow with `overflow-wrap: anywhere` and a shrinkable flex/grid child; never apply `word-break: break-all` to prose.

## 237. Animation
- Choose shared motion tokens by distance, complexity, platform and context; never one duration for every transition.
- Animate only `transform`/`opacity`; never width/height/top/left.
- Match loading feedback to the expected wait; avoid flashing indicators for near-instant work.
- Animate `1–2` key elements per view max.
- Decelerate on arrival, accelerate on exit, linear only for constant-rate progress or rotation.
- Every animation expresses cause and effect; state changes animate smoothly rather than snap.
- Maintain spatial continuity (shared element, directional slide); use parallax sparingly.
- Prefer spring/physics-based curves for natural feel.
- Exit animations `~60–70%` of enter duration.
- Stagger list/grid entrance by `30–50ms` per item.
- Animations are interruptible and never block input.
- Crossfade for content replacement in the same container.
- Subtle press scale `0.95–1.05`, restored on release.
- Drag/swipe/pinch track the finger in real time.
- Enter from below = deeper; exit upward = back; forward navigation moves left/up, backward right/down.
- Unify duration/easing tokens globally.
- Fading elements should not linger below opacity `0.2`.
- Modals/sheets animate from their trigger source (scale+fade or slide-in).
- Animations must not cause reflow or CLS.
- Rapid state changes cancel/replace prior micro-interactions, set the final state explicitly and never depend on an animation-end event for correctness.

## 238. Forms & Feedback
- Visible label per input; never placeholder-only labels.
- Show a specific error below the related field, linked with `aria-describedby`.
- Loading then success/error state on submit.
- For custom Enter shortcuts, keep IME composition confirmation separate from submission and provide an explicit submit button.
- Mark required fields (e.g. asterisk).
- Empty states give a helpful message and an action.
- Auto-dismiss toasts in `3–5s`; toasts never steal focus and use `aria-live="polite"`.
- Confirm before destructive actions; allow undo for destructive or bulk actions.
- Persistent helper text below complex inputs.
- Disabled elements use opacity `0.38–0.5`, cursor change and a semantic attribute.
- Reveal complex options progressively.
- Validate on blur, not keystroke.
- Use semantic input types (email, tel, number) and autocomplete attributes.
- Provide a show/hide toggle for password fields.
- Confirm completed actions briefly (checkmark, toast, color flash).
- Error messages state cause and fix, with a recovery path (retry, edit, help link).
- Multi-step flows show a step indicator and allow back navigation.
- Long forms auto-save drafts; confirm before dismissing a sheet with unsaved changes.
- Group related fields (fieldset/legend).
- Read-only state is visually and semantically distinct from disabled.
- After a failed submit with multiple errors, focus a linked error summary at the top while retaining inline errors; without a summary, focus the first invalid field.
- Mobile input height `≥44px`.
- Destructive actions use semantic danger red and are separated from primary actions.
- Form errors use an `aria-live` region or `role="alert"`; error/success colors meet `4.5:1`.
- Request timeouts show clear feedback with retry.

## 239. Navigation Patterns
- Bottom navigation max `5` items, with labels and icons; for top-level screens only.
- Drawer/sidebar for secondary navigation, not primary actions.
- Back navigation is predictable and restores scroll, filter and input state.
- All key screens reachable via deep link/URL.
- iOS: bottom Tab Bar for top-level navigation; Android: Top App Bar with navigation icon.
- Navigation items carry both icon and text; highlight the current location.
- Clearly separate primary and secondary navigation; never mix Tab + Sidebar + Bottom Nav at one level.
- Modals offer a clear close affordance (swipe-down on mobile) and are never used for primary flows.
- Search easily reachable with recent/suggested queries.
- Breadcrumbs for hierarchies `3+` levels deep on web.
- Support iOS swipe-back and Android predictive back.
- Use nav badges sparingly and clear them after a visit.
- Use an overflow/more menu instead of cramming actions.
- Large screens (`≥1024px`) prefer a sidebar; small screens use bottom/top nav.
- Never silently reset the navigation stack or jump home.
- Keep navigation placement identical across pages and reachable from deep pages.
- Move focus to the main content region after route changes.
- Separate dangerous actions (delete account, logout) from normal items.
- When a destination is unavailable, explain why rather than hiding it.

## 240. Charts & Data
- Match chart to data: trend → line, comparison → bar, proportion → pie/donut.
- Avoid pie/donut for `>5` categories.
- Accessible palettes; avoid red/green-only pairs; supplement color with patterns, textures or shapes.
- Provide a table alternative and a text summary of the key insight for screen readers.
- Always show a legend near the chart; make legends clickable to toggle series.
- Tooltips/data labels on hover (web) or tap (mobile), keyboard-reachable.
- Label axes with units; avoid rotated or truncated labels on mobile; auto-skip cramped ticks.
- Charts reflow or simplify on small screens (horizontal bars, fewer ticks).
- Meaningful empty, loading (skeleton) and error (with retry) states instead of blank axes.
- Chart entrance animations respect reduced motion.
- For `1000+` points aggregate or sample with drill-down.
- Locale-aware number, date and currency formatting.
- Interactive points/segments get `≥44pt` tap areas and keyboard navigation.
- Data lines/bars `≥3:1` against background; data text labels `≥4.5:1`.
- Direct-label small datasets; limit density per chart.
- Emphasize trends over decoration; gridlines low-contrast (e.g. `gray-200`).
- Sortable tables expose `aria-sort`; offer CSV/image export for data-heavy products.
- Drill-downs keep a clear back path; time series label granularity (day/week/month) and allow switching.

## 241. App UI Professional Polish
- Vector-only icons (SVG or platform vector) that theme and scale; no raster PNG icons.
- Pressed states change color, opacity or elevation without changing layout bounds.
- Use official brand logos with correct spacing, color and clear space; never guess or recolor.
- Icon sizes as tokens (e.g. `icon-sm`, `icon-md` = `24pt`, `icon-lg`); avoid mixing `20pt / 24pt / 28pt` randomly.
- Consistent stroke width in one layer (`1.5px` or `2px`); one filled-or-outline style per hierarchy level.
- Align icons to the text baseline with consistent padding.
- Meaningful icons and control boundaries need `≥3:1` contrast.
- Tap feedback within `80–150ms`.
- Disabled controls use native disabled semantics and do nothing on tap.
- One primary gesture per region; avoid nested tap/drag conflicts.

## 242. Light/Dark Contrast Parity
- Cards/surfaces stay clearly separated from the background in both themes.
- Body and secondary text `≥4.5:1` in both light and dark; `3:1` only for large text or non-text UI.
- Dividers and borders stay visible in both themes.
- Pressed/focused/disabled states equally distinguishable in both themes.
- Semantic color tokens mapped per theme; no per-screen hardcoded hex.
- Measure the composed scrim result against the real background; never reuse one opacity blindly.
- Test both themes; never infer dark from light.

## 243. Mobile Layout & Spacing
- Respect top/bottom safe areas for fixed headers, tab bars and CTA bars; clear status bar, navigation bar and home indicator.
- Predictable content width per device class.
- `4/8dp` spacing rhythm; vertical tiers such as `16/24/32/48`.
- Avoid edge-to-edge paragraphs on tablets.
- Increase gutters on larger widths and in landscape.
- Add content insets so lists are not hidden behind fixed bars.

## 244. Pre-Delivery Checklist
- Process: test at `375px` and landscape; verify reduced motion and largest system text; check dark contrast independently; confirm targets `≥44pt` and nothing hidden behind safe areas.
- Visual: no emoji icons; consistent icon family; official brand assets; no layout-shifting press states; semantic tokens only.
- Interaction: clear pressed feedback; minimum target sizes; shared timing tokens; clear disabled states; screen-reader order matches visual order; no conflicting gestures.
- Light/Dark: text `≥4.5:1` in both modes; borders and states distinguishable; scrims measured; both themes tested.
- Layout: safe areas; scroll content clear of fixed bars; verified on small phone, large phone and tablet in portrait and landscape; adaptive gutters; `4/8dp` rhythm; readable measure.
- Accessibility: decorative icons hidden (`aria-hidden="true"`); text alternatives; icon control names and states; labelled fields with hints and errors; color not the only indicator; reduced motion and dynamic text without breakage; focus not obscured; drag alternatives; password manager and paste allowed; carousel pause controls; error summary after failed submit.
- Web additions: `cursor-pointer` on clickables, light-mode text `4.5:1`, visible focus, chips and badges reflow without clipping, responsive checks at `375px`, `768px`, `1024px`, `1440px`.

# Part 26 — Product-Driven Design Direction

## 245. Complete Design System Recommendation
- A complete direction combines: landing pattern (section order and CTA placement), style (keywords, best-for, performance and accessibility notes), colors (primary, secondary, CTA, background, text), typography pairing with mood, key effects, anti-patterns and a pre-delivery checklist.
- Derive it from product type, industry and keywords; filter out anti-patterns for that industry.
- Example (wellness spa): Hero-Centric + Social Proof pattern (Hero, Services, Testimonials, Booking, Contact; CTA above fold and repeated after testimonials), Soft UI Evolution style, primary `#E8B4B8`, secondary `#A8D5BA`, CTA `#D4AF37`, background `#FFF5F5`, text `#2D3436`, Cormorant Garamond / Montserrat, soft shadows and gentle hovers; avoid bright neon, harsh animation, dark mode and AI purple/pink gradients.
- Industry rules can forbid styles, e.g. no AI purple/pink gradients for banking.
- Keep a global master direction; page-specific overrides take precedence over the master only for that page.

## 246. Design Dials
- Variance: low (`1-3`) centered/minimal; mid (`4-7`) balanced/modern; high (`8-10`) bold/asymmetric (Brutalism, Bento Grids).
- Motion: low subtle micro-interactions; mid standard scroll/stagger; high complex choreography (pinning, flip, split text).
- Density: low spacious (`24-96px` spacing scale) for marketing; mid standard (`16-64px`); high dense dashboard (`8-32px`).

## 247. Right-to-Left Readiness
- Rate styles and products for RTL (Arabic, Hebrew, Persian, Urdu): full = survives mirroring unchanged; partial = mirrors but icons, carousels, motion paths and charts need per-component checks; caveats = encodes reading direction (kinetic type, LTR timelines, code/terminal surfaces, maps, seat ordering).
- Flag caveat styles before recommending them and offer a mirrorable alternative for strict RTL builds.

## 248. Retheming an Existing App
- Inspect existing routes, components, styles and theme tokens first; keep component structure, behavior and logic.
- Audit hard-coded values (e.g. `bg-blue-600`, `text-[#1e293b]`).
- Map to semantic roles `background`, `surface`, `foreground`, `primary`, `border`, `ring`; add missing tokens rather than a parallel theme system.
- Migrate one component batch at a time; changing tokens alone does not affect styles that bypass them.
- After every batch verify contrast, hover/focus/disabled states, responsive layouts and every supported theme.

## 249. Resilient Text and Compact UI
- Designs must work with natural wrapping across widths, fonts and locales.
- Essential text reflows without clipping at narrow widths, zoom, text scaling and user spacing overrides.
- Compact labels stay whole when practical; unavoidable truncation needs an accessible full-value path for keyboard, pointer and touch.
- Badge meaning never relies on color alone; interactive chips need native semantics, visible focus and programmatic state; live counts need context.
- Rapid interactions may cancel animation, but final state, focus and content must remain correct.

# Part 27 — Routing Design Work

## 250. Discipline Map
- Brand identity: colors, typography, voice, logo usage, messaging, asset organization, consistency audits.
- Token system: token JSON, CSS variables, component specs, state/variant documentation, mapping tokens to the styling framework, validating token usage.
- Implementation: components, utility styling, dark mode, responsive layouts, accessible components.
- Logo: style, palette and industry guidance plus design briefs.
- Corporate identity programme: stationery, signage, vehicles, apparel mockups and presentations.
- Presentations: strategic decks with charts, copy formulas and layout patterns.
- Banners: social, ad, web hero and print banners.
- Icons: SVG icon sets in consistent styles and sizes.

## 251. Routing by Question
- "What color should this be?" and "Is this on-brand?" → brand.
- "How do I create a token?" or "Should this be a CSS variable?" → token system.
- "How do I build a button?" or "How do I add dark mode?" → implementation.
- "What logo style fits my industry?" → logo; "Design a brand identity package" → identity programme.
- "Design a Facebook cover", "Create Google ad banners", "Make a hero banner" → banner.
- "Create a pitch deck" → presentations; "Design an icon set" → icons.

## 252. Multi-Discipline Workflows
- Dependency flow: brand (colors, typography) → tokens (primitive, semantic, component) → implementation (components) → application.
- New project: define identity → create three-layer tokens → configure framework and components.
- Migration: audit and extract brand colors/fonts → formalize three-layer tokens → replace hardcoded values.
- Component creation: reference specs (states, sizes, variants) → implement.
- Complete brand package: logo → identity mockups → pitch deck.
- Social presence: banners + brand; custom icon set: icons + tokens; design language without code: brand + tokens.

# Part 28 — Logo Design

## 253. Logo Types
- Wordmark (logotype): custom typography text-only; best for established brands with distinctive, memorable, pronounceable names.
- Lettermark (monogram): initials in bold geometric sans; best for long names and firms with `2-4` letter abbreviations.
- Pictorial mark: standalone symbol; simple, scalable, memorable; requires existing brand equity.
- Abstract mark: non-representational geometry conveying values; suits tech and differentiation.
- Mascot: friendly expressive character; suits family brands, sports teams, food.
- Emblem: symbol enclosed in a badge, seal or crest; suits traditional organizations; may struggle to scale.
- Combination mark: icon + text lockup; most versatile, elements can separate later; ideal for new brands.

## 254. Aesthetic Styles
- Minimalist: clean lines, essential elements, high white space, `1-2` colors.
- Vintage/Retro: heritage feel, distressed textures, muted colors, script or slab serif.
- Luxury/Premium: gold, black, white; thin serifs or sophisticated sans.
- Geometric: mathematical precision, circles/triangles/squares, perfect symmetry.
- Organic/Natural: flowing imperfect lines, earth tones, hand-drawn feel.
- Gradient/Modern: color transitions, vibrant palettes, dimensional depth.
- Further families: Art Deco, Playful, Corporate, Neon, Grunge, Watercolor, Flat, 3D/Isometric, Line Art, Duotone, Motion-Ready, Negative Space, Monoline, Split/Fragmented, Responsive/Adaptive.

## 255. Style by Industry
- Tech startup: minimalist or abstract; geometric or gradient secondary; blues, purples, gradients; geometric sans.
- Law firm: wordmark or emblem; lettermark secondary.
- Restaurant/food: mascot or vintage badge; warm reds, oranges; friendly or script type.
- Fashion: wordmark or luxury; monogram or line art; black, gold, white; elegant serif.
- Healthcare: professional line art; blues, greens, teals; clean sans.
- Finance: corporate or emblem; navy and gold; serif or clean sans.
- Non-profit: combination or emblem; organic or hand-drawn secondary.

## 256. Logo Color Psychology
- Blue: trust, stability; finance, healthcare, tech; navy `#003366`, royal `#0055A4`, sky `#0EA5E9`; pair with white, gold, light gray.
- Red: energy, urgency; food, sports, entertainment; crimson `#DC2626`, scarlet `#EF4444`, burgundy `#9F1239`; avoid for healthcare.
- Green: growth, health, sustainability; forest `#228B22`, sage `#2E8B57`, mint `#10B981`.
- Yellow/Gold: optimism, luxury, attention; gold `#D4AF37`, amber `#F59E0B`, lemon `#FACC15`; pair with black, navy, dark brown.
- Purple: creativity, wisdom, luxury; royal `#7C3AED`, lavender `#A78BFA`, deep `#581C87`.
- Orange: friendly, youthful; tangerine `#F97316`, coral `#FB923C`, burnt `#EA580C`.
- Black for sophistication and high-end positioning; white for purity, backgrounds and negative space.
- Avoid by industry: tech avoid brown/beige; healthcare avoid red/black; finance avoid bright colors; food avoid blue (appetite suppressant); fashion avoid neon unless intentional; eco avoid neon/black; children avoid dark/muted.
- Harmonies: monochromatic (safe, cohesive), complementary (high contrast), analogous (harmonious), triadic (balanced, dynamic).
- Accessibility: `4.5:1` contrast, no red-green-only indicators, test in grayscale, consider colorblind users (`~8%` of males).
- Quick palettes: tech `#6366F1` / `#8B5CF6` / `#06B6D4`; eco `#228B22` / `#2E8B57` / `#DEB887`; luxury `#1C1917` / `#D4AF37` / `#FFFFFF`; healthcare `#0077B6` / `#00A896` / `#FFFFFF`; food `#DC2626` / `#F97316` / `#CA8A04`.

## 257. Logo Scalability Checklist
- Recognizable at `16x16` pixels (favicon).
- Clear at business-card size.
- Works in single color and in black/white.
- No tiny details that disappear when scaled.
- Works on light and dark backgrounds; horizontal and stacked layouts; mark can stand alone.

## 258. Generative Logo Prompting
- Structure: brand/industry, visual description, style keywords, palette (hex codes), mood, symbols, technical requirements.
- Always present logos on a plain white background, centered, `1:1` square or explicitly horizontal.
- Request "simple", "vector-style", "illustration, not photorealistic", "scalable", "works in single color", "crisp edges, balanced composition".
- Exclude: photorealism, realistic 3D textures, stock/clip art, multiple logos, busy backgrounds, watermarks, blur, complex detailed patterns.
- Text renders poorly; generate the mark separately from the wordmark.
- Minimalist vocabulary: clean lines, simple geometric shapes, high white space, flat, single color, negative space.
- Vintage vocabulary: heritage, distressed texture, badge style, hand-lettered, sepia, aged paper.
- Luxury vocabulary: elegant, gold accents, metallic, thin lines, serif typography, foil effect.
- Tech vocabulary: gradient colors, geometric, abstract, dynamic, clean sans-serif, circuit-like.
- Playful vocabulary: rounded shapes, bright colors, bouncy, hand-drawn elements.
- Organic vocabulary: botanical, earth tones, leaf elements, imperfect lines, biophilic.
- Variations: state what to keep, what to change and the new style direction.

# Part 29 — Icon Design

## 259. Icon Styles
- Outlined: `2px` stroke, no fill; UI interfaces and web apps.
- Filled: solid, no stroke; mobile apps and nav bars.
- Duotone: dual fill; marketing and landing pages.
- Thin: `1-1.5px` stroke; luxury and editorial.
- Bold: `3px` stroke; headers and hero sections.
- Rounded: `2px`; friendly apps, health. Sharp: `2px`; tech, fintech, enterprise.
- Flat: solid; Material/Google-style. Gradient: modern brands, SaaS.
- Glassmorphism: `1px` stroke, semi fill; modern UI, overlays.
- Pixel (gaming, retro), hand-drawn (artisan), isometric `1-2px` (tech docs, infographics), glyph (system UI, compact), animated-ready `2px` (interactive UI, onboarding).

## 260. Icon Categories
- Navigation (arrows, menus, home, chevrons), action (edit, delete, save, download, upload), communication (email, chat, phone, notification), media (play, pause, volume, camera), file (document, folder, archive, cloud), user (person, group, profile, settings), commerce (cart, bag, wallet, card), data (chart, graph, analytics, dashboard), development (code, terminal, bug, git, API), social (heart, star, bookmark, trophy), weather (sun, moon, cloud, rain), map (pin, location, compass, globe).

## 261. SVG Construction Rules
- ViewBox `0 0 24 24` (standard) or `0 0 16 16` (compact); default display size `24px`.
- Use `currentColor` for color inheritance; avoid hardcoded colors.
- Always include a `<title>` element.
- Minimal path nodes; no embedded fonts or raster images.
- Design at `24px`, test at `16px` and `48px`; export sets at `16, 24, 32, 48`.
- Outlined styles use `stroke-linecap="round"` and `stroke-linejoin="round"`.
- Produce batches of variations to compare before committing to a set.

# Part 30 — Corporate Identity Programme

## 262. Deliverable Categories
- Core identity: primary logo and variations.
- Stationery: business card, letterhead, envelope, folder, notebook, pen.
- Security/access: ID badge, lanyard, access card.
- Office environment: reception signage, wayfinding, meeting-room signs, wall graphics.
- Apparel: polo, T-shirt, cap, jacket, apron.
- Promotional: tote, gift box, USB drive, water bottle, mug, umbrella.
- Vehicle: sedan, van, truck.
- Digital: social media, email signature, presentation and document templates.
- Product: packaging box, labels, tags, retail display.
- Events: trade show booth, banner stand, table cover, backdrop.

## 263. Deliverable Specifications
- Primary logo in vector (SVG, AI, EPS) with clear-space rules, scalable favicon to billboard.
- Variations: horizontal, vertical, stacked, icon-only, monochrome black/white/reversed.
- Business card `3.5x2` inches / `85x55mm`, `300-400gsm` stock, finishes matte, spot UV, foil, emboss.
- Letterhead A4 or Letter with header for logo/contact, digital and print versions.
- Envelopes DL, C4, C5 with logo on flap or front and styled return address.
- Reception signage: 3D dimensional letters, backlit LED options, acrylic/metal/wood.
- Wayfinding: consistent icon system, clear hierarchy, ADA compliance.
- Wall graphics: mission/values displays, murals, window frosting.
- Polo: embroidery preferred, left chest, pique cotton; uniforms use department color coding and name badges.
- Vehicles: door panel branding, partial or full wrap, visible high-visibility contact details, consistent across fleet.
- Social: icon-version profile pictures, platform-specific covers, post templates.
- Email signature: HTML responsive, max `600px` width, essential contact only.
- Trade show booth: modular, easy assembly, key messaging visible.
- Promotional items: quality over quantity, useful items, brand colors prominent.

## 264. Identity Styles
- Corporate Minimal: navy `#0F172A`, white `#FFFFFF`, blue accents; Inter/Helvetica; premium matte paper; spot UV on logo; finance, legal, consulting.
- Modern Tech: `#6366F1`, `#0EA5E9`, `#10B981`; geometric sans (Outfit, Poppins); gradient prints, gloss, metallic accents.
- Luxury Premium: `#1C1917`, gold `#D4AF37`, white; Playfair, thin sans; heavy cotton paper, leather, metal; gold foil, emboss, deboss, soft-touch.
- Classic Traditional: navy, burgundy, gold; Times/Garamond; laid paper, wood; letterpress, gold emboss.
- Warm Organic: brown `#8B4513`, green `#228B22`, cream; friendly serif, organic script; kraft and recycled paper; uncoated.
- Bold Dynamic: `#DC2626`, `#F97316`, black; bold condensed sans; high-contrast gloss; sports, entertainment, gaming.
- Fresh Modern: mint `#10B981`, sky `#0EA5E9`, white; rounded sans; matte, clean; healthcare, wellness, fintech.
- Soft Elegant: pink `#F472B6`, gold, white; elegant script, thin sans; rose gold foil; beauty, wedding, spa.

## 265. Mockup Art Direction
- Describe deliverable, brand, style, colors, typography, logo placement, materials, finishes, setting and mood, rendered as photorealistic product photography with soft natural lighting and sharp focus.
- Always apply the real logo when one exists; create the logo first if none exists.
- Business card: on marble, stacked, premium paper texture, soft shadows, `45` degree angle.
- Letterhead: flat lay with envelope and pen, overhead view.
- Signage: 3D logo on lobby wall, backlit LED, brushed metal, architectural photography.
- Vehicle: urban street, `3/4` front angle, professional wrap.
- Apparel: folded polo, embroidered chest logo, fabric texture.
- Style modifiers: corporate (white space, subtle shadows, matte), luxury (dark background, dramatic rim light, gold), tech (gradients, geometric, clean surfaces), organic (kraft texture, warm light, artisan).
- Lighting: studio even, natural window light, dramatic rim, warm golden hour. Context: marble desk, wooden table, office interior, flat lay, lifestyle in-use.
- Exclude blur, distorted or misspelled text, clipart, cartoon, watermark.
- Present the programme with a hero (brand, industry, style, mood) and deliverable cards giving concept, purpose and specifications; responsive, dark theme.

# Part 31 — Banner Design (sizes & styles)

## 266. Social Banner Sizes
- Facebook cover desktop `820 × 312` (`~2.6:1`), mobile `640 × 360`, event cover `1920 × 1080`.
- Twitter/X header `1500 × 500` (`3:1`); ad banner `800 × 418`.
- LinkedIn company cover `1128 × 191` (`~6:1`); personal banner `1584 × 396` (`4:1`).
- YouTube channel art `2560 × 1440` (`16:9`) with safe area `1546 × 423`.
- Instagram story `1080 × 1920` (`9:16`); post `1080 × 1080` (`1:1`).
- Pinterest pin `1000 × 1500` (`2:3`).

## 267. Display Ad Sizes
- Medium Rectangle `300 × 250` (highest CTR, `6:5`); Leaderboard `728 × 90` (top of page, `8:1`).
- Wide Skyscraper `160 × 600`; Half Page `300 × 600`; Large Rectangle `336 × 280`.
- Mobile Banner `320 × 50`; Large Mobile `320 × 100`; Billboard `970 × 250`.

## 268. Web and Print Sizes
- Full-width hero `1920 × 600–1080`; section banner `1200 × 400`; blog header `1200 × 628`; email header `600 × 200`.
- Roll-up `850mm × 2000mm`; step-and-repeat `8ft × 8ft`; vinyl outdoor `6ft × 3ft`; trade show `33in × 78in`.

## 269. Art Direction Styles
- Minimalist (white space, single focal element, `1-2` colors, clean sans) for SaaS/tech.
- Bold Typography (type is the design, oversized letterforms) for announcements.
- Gradient/Color Wash (mesh gradients, chromatic blends) for modern brands.
- Photo-Based (full-bleed photography with text overlay) for lifestyle/e-commerce.
- Illustrated/Hand-Drawn; Geometric/Abstract (tech, fintech); Retro/Vintage (distressed, muted, halftone; F&B, craft).
- Glassmorphism (frosted panels, blur, subtle border glow) for SaaS/apps; 3D/Sculptural (product-centric depth).
- Neon/Cyberpunk (dark backgrounds, glowing accents) for gaming/events; Duotone (two-color photo treatment).
- Editorial/Magazine (grids, pull quotes) for media/luxury; Collage/Mixed Media; Retro Futurism (chrome, space-age optimism).
- Expressive/Anti-Design; Digi-Cute/Kawaii (pastels, rounded, pixel); Tactile/Sensory (puffy, embossed).
- Data/Infographic (numbers as heroes); Dark Mode/Moody (near-black, jewel tones); Flat/Solid Color; Nature/Organic; Motion-Ready/Kinetic (layered, loopable).
- Select `2–3` complementary directions per brief and state how each supports the purpose; produce `3` options by default.

## 270. Three-Zone Hierarchy
- Top: logo or main value proposition.
- Middle: supporting message and visuals.
- Bottom: CTA (button, QR code or URL).

## 271. Safe Zones
- Critical content in the central `70–80%` of the canvas.
- Keep text and CTA `50–100px` from edges.
- YouTube: keep content within the `1546 × 423px` safe area of `2560 × 1440`.
- Meta/Instagram: central `80%` to avoid UI chrome.
- Verify crop behavior at the exact target size.

## 272. Banner CTA and Typography
- One CTA per banner, high contrast, bottom-right (terminal area), min `44px` height, action verbs ("Get", "Start", "Download", "Claim").
- Max `2` typefaces; min `16px` body, `≥32px` headline; min `4.5:1` contrast.
- Max `7` words per line and `3` lines for ads.

## 273. Text-to-Image Ratio
- Ads under `20%` text (Meta penalizes heavy text).
- Social covers `60/40` image-to-text.
- Print: `70pt+` headlines for `3-5m` viewing distance; `1pt` per foot of viewing distance.

## 274. Print Production
- `300 DPI` minimum (`150 DPI` for large format).
- `3-5mm` bleed on all sides; CMYK color mode.

## 275. Banner Build and Export
- Build at exact platform dimensions; use only supplied, verified brand rules and assets; never invent brand rules.
- Prefer supplied or licensed imagery, or CSS-built gradients, forms and type.
- Keep any generated background free of text, letters and words so copy stays editable and accessible as live text.
- Export PNG at exact dimensions; verify pixel size, safe-zone crop, font loading and quality; optimize files exceeding platform limits.
- Name variants `{style}-{width}x{height}`, date-prefix time-sensitive campaigns, group variants per campaign.
- Present options side by side with style name, preview, rationale and dimensions; iterate.

# Part 32 — Social Media Imagery

## 276. Social Image Sizes
- Instagram post `1080 x 1080` (`1:1`), story/reel `1080 x 1920` (`9:16`), carousel `1080 x 1350` (`4:5`).
- Facebook post `1200 x 630`; story `1080 x 1920`.
- Twitter/X post `1200 x 675` (`16:9`); card `800 x 418`.
- LinkedIn post `1200 x 627`; article `1200 x 644`.
- Pinterest pin `1000 x 1500` (`2:3`); YouTube thumbnail `1280 x 720`; TikTok cover `1080 x 1920`; Threads post `1080 x 1080`.
- Default set when unspecified: Instagram post plus story, `3` variations.

## 277. Concept Development
- Generate `3-5` concepts varying composition, color and typography approach, aligned with brand guidelines, and approve before designing.
- Use a different style, palette or font pairing per concept for variety.
- Design each approved idea at each target size.

## 278. Social Canvas Rules
- Exact pixel canvas, no scrolling, everything in one viewport.
- High contrast; text readable at thumbnail size; test at `50%` size.
- Critical content within the central `80%`.
- One focal point and a clear reading flow.
- Brand primary dominant, secondary as accent; consider platform dark/light modes.
- Export at `2x` scale for retina quality; wait for fonts and images to load before capture.

## 279. Social Typography Hierarchy
- At `1080px` width: headline `48px` bold/black; subheadline `32px` semibold; body `24px` regular; caption `18px` regular/light; CTA `28px` bold.
- Absolute floor: `24px` headlines and `16px` body at `1080px` width.

## 280. Platform Tone
- Instagram: visual-first, text `<20%`, strong colors, lifestyle feel.
- Facebook: informative, can carry more text, eye-catching in feed.
- Twitter/X: bold headlines, contrast for dark/light modes, clear message.
- LinkedIn: professional, clean, data-driven, thought leadership.
- Pinterest: vertical, text overlay on images, how-to style.
- YouTube: face close-ups, bright colors, readable small.
- TikTok: trendy, energetic, bold type, youth-oriented.

## 281. Social Style Menu
- Minimalist (SaaS, luxury), Bold Typography (quotes), Gradient Mesh (apps), Photo-Based (e-commerce), Geometric (fintech), Glassmorphism (modern apps), Flat Illustration (education, health), Duotone (editorial), Collage (fashion, culture), 3D/Isometric (product).

## 282. Social Visual QA
- Check fonts loaded (no system fallback), no overflow or clipping, elements inside the central `80%`, text `≥4.5:1`, no misalignment; fix and re-export until all pass.
- Document design decisions: palette, typography, layout and brand alignment with reasoning, plus A/B test suggestions.

# Part 33 — Slide Layouts

## 283. Layout Selection by Goal
- Title slide (fade up), problem statement (stagger), solution overview (scale), feature grid of `3-6` cards (stagger), metrics dashboard of `3-4` KPIs (stagger-scale).
- Comparison table, timeline flow, team grid, quote testimonial, two-column split, big-number hero (count-up), product screenshot (scale), pricing cards, CTA closing (pulse).
- Decide by slide goal → emotion to trigger (color treatment) → content type (type scale) → whether to break pattern.

## 284. Slide Grid Structures
- Title: centered flex column, centered text.
- Two-column split: `1fr 1fr`, `48px` gap; single column with `24px` gap under `768px`.
- Feature grid: `3` columns, `24px` gap; `2` columns `16px` gap under `768px`; `1` column under `480px`.
- Metrics: `4` columns, `16px` gap; `2` under `768px`; `1` under `480px`.

## 285. Slide Component Variants
- Cards: icon-left (features), accent bar (highlighted), metric, avatar (team), pricing.
- Metric styles: gradient numbers, oversized `120px+`, sparkline, funnel numbers.
- Treatments: gradient glow (titles, CTAs), subtle border (problem), icon-top (features), screenshot shadow, popular highlight at scale `1.05` (pricing), background overlay, contrast pair (before/after), grayscale client logos.

## 286. Slide Frame and Type
- Lock deck to `16:9` on desktop, letterboxing when viewport ratio differs.
- Slide padding `60px`; `32px 24px` on tablet; `24px 16px` on mobile; constrain content inside a safe wrapper with `16px` gap and hidden overflow.
- Title `clamp(32px, 6vw, 80px)` with line-height `1.1`, often gradient text; tablet title `clamp(28px, 5vw, 48px)`, h2 `clamp(20px, 4vw, 32px)`, body `clamp(14px, 2.5vw, 18px)`; mobile title `clamp(22px, 6vw, 36px)`, h2 `clamp(18px, 4.5vw, 28px)`, body `clamp(12px, 3vw, 16px)`.
- Center-align content; every slide focuses on persuasion/conversion.
- Navigation: keyboard arrows/space, click to advance, `3px` progress bar, `40px` round nav buttons (`32px` on mobile), slide counter; slide crossfade `0.4s`.
- Image backgrounds use a dark gradient overlay (`0.9` → `0.7` opacity) beneath content.

## 287. Slide Motion
- Fade up: `30px` translate, `0.6s` ease-out.
- Scale in: from `0.9`, `0.5s` ease-out.
- Stagger children at `0.1s` increments.

## 288. Slide Charts and Tokens
- Use real charts (line, bar, doughnut, radar), not CSS-only bars.
- Chart container `min(80%, 600px)` wide, `clamp(200px, 40vh, 350px)` tall; line `3px`, `0.4` tension, `10%` fill; faint gridlines `rgba(255,255,255,0.05)`; hide legend for single series.
- Use tokens exclusively: primary (CTA, highlights), background, secondary, title gradient, heading and body font; never hardcode hex or font names.

## 289. Deck Strategies
- YC Seed `10-12` slides (VCs); Guy Kawasaki `10` slides in `20` min; Series A `12-15`; Product Demo `5-8`; Sales Pitch `7-10`; Problem-Solution-Benefit `3-5`; QBR `10-15`; All-Hands `8-12`; Conference Talk `15-25`; Workshop `20-40`; Case Study `8-12`; Competitive Analysis `6-10`; Board Meeting `15-20`; Webinar `20-30`.
- YC Seed order: Title/Hook, Problem, Solution, Traction, Market, Product, Business Model, Team, Financials, The Ask; arc curiosity→frustration→hope→confidence→trust→urgency.
- Sales Pitch: Personalized Hook, Their Problem, Cost of Inaction, Solution, Proof, Differentiators, Pricing/ROI, Objection Handling, CTA; arc connection→frustration→fear→hope→trust→confidence→urgency.
- Product Demo: Hook/Problem, Solution, Demo, Features, Benefits/Pricing, CTA.
- Match context: raising money (YC, Series A, Kawasaki), selling (Sales, Demo), internal (QBR, All-Hands, Board), public speaking (Talk, Workshop), proving value (Case Study, Competitive), leads (Webinar).

## 290. Duarte Sparkline Pattern Breaks
- Alternate "What Is" (pain) and "What Could Be" (hope), ending in "New Bliss".
- Break the visual pattern (e.g. full-bleed) at the `1/3` and `2/3` positions for engagement peaks.

## 291. Slide Copywriting Formulas
- PAS for problem slides: "[Pain]? Every [time], [consequence]. [Solution] fixes this."
- AIDA for CTAs/closing: bold statement, benefit, social proof, CTA.
- FAB for features: "[Feature] lets you [advantage], so you can [benefit]."
- Cost of Inaction for urgency; Before-After-Bridge for transformation and case studies.
- Map: hook → curiosity; problem → frustration; cost → fear; solution → hope; features/pricing → confidence; traction/social proof → trust; CTA → urgency.
- Headline patterns: "Stop [bad thing]", "Get [result] in [timeframe]", "[Old way] is dead. Meet [new way].", "From [pain] to [benefit]", "[Number]+ [companies] trust [product]".

# Part 34 — Brand Guidelines (voice, colour management, typography specs, logo usage, asset organisation, approval checklist)

## 292. Guideline Document Structure
- Quick reference (primary/secondary color, primary font, `3` voice traits), color palette, typography, logo usage, voice and tone, imagery, design components, image-generation style, changelog; version the document.
- Keep brand guidelines as the single source of truth and sync any change to design tokens and CSS variables together; never update one alone.
- Do not create a parallel token system beside an existing one.

## 293. Voice vs Tone
- Voice is the consistent personality; tone adapts to context (celebratory for wins, empathetic for support).
- Place the brand on spectrums: formal↔casual, simple↔complex, serious↔playful, reserved↔expressive.
- Define `3-5` traits with guardrails: confident not arrogant, friendly not unprofessional, knowledgeable not condescending, innovative not gimmicky.
- Build a voice chart (trait, meaning, do, don't) and "we are / we are not" pairs.
- Tone shifts: social more casual, support more empathetic, legal more formal, sales more confident; errors calm and solution-focused; success brief and celebratory.
- Test: does it sound like us, would a competitor say it, does it resonate, is it consistent with values.
- List prohibited terms with reasons (e.g. "revolutionary", "seamless" overused; "best-in-class" vague; "synergy" jargon; "leverage" → "use").

## 294. Messaging Framework
- Cascade: mission → vision → value proposition → positioning → key messages → proof points.
- Mission: "We [action] for [audience] by [method] so they can [outcome]."
- Value proposition: for [customer] who [need], [brand] is a [category] that [benefit]; unlike [competitors], we [differentiator].
- One primary message plus `3-5` supporting messages each tied to an audience need and proof point.
- Elevator pitches at `10`, `30` and `60` seconds; tailor message and CTA per audience segment.
- Test messages for clarity, differentiation, credibility, compellingness and consistency.

## 295. Color Palette Hierarchy
- Primary `1-2` (CTAs, headers, key elements), secondary `2-3` (accents, interactive states, illustrations), neutrals `3-5` (backgrounds, text, borders), semantic `4`.
- Semantic defaults: success `#22C55E`, warning `#F59E0B`, error `#EF4444`, info `#3B82F6`.
- Document each color with name, hex, RGB, HSL and usage, e.g. Primary Blue `#2563EB` / `rgb(37,99,235)` / `hsl(217,91%,53%)`.
- Starter neutrals: background `#FFFFFF`, surface `#F9FAFB`, text primary `#111827`, text secondary `#6B7280`, border `#E5E7EB`.

## 296. Color Ratios and Compliance
- Primary `60-70%` of a design, secondary `20-30%`, accent `5-10%` (the `60/30/10` rule).
- Off-brand tolerance max `20%` non-palette colors.
- Do: primary for main CTAs, consistent hover/active states, test all combinations, document decisions.
- Don't: more than `2-3` colors in one component, mix warm and cool without intent, pure black `#000` text (use `#111` or similar), color-only meaning.
- WCAG 2.1 AA: normal `4.5:1`, large `3:1`, UI components `3:1`; AAA: `7:1`, `4.5:1`, `4.5:1`.
- Contrast uses relative luminance: ratio = (lighter + `0.05`) / (darker + `0.05`).
- Example palettes: tech `#2563EB` / `#8B5CF6` / `#10B981` on `#F9FAFB`, text `#111827`; creative `#F97316` / `#EC4899` / `#14B8A6`; corporate `#1E40AF` / `#475569` / `#0EA5E9` on `#F8FAFC`, text `#0F172A`.
- Theme presets: ocean-professional `#3B82F6` / `#F59E0B` / `#10B981`; electric-creative `#FF6B6B` / `#9B5DE5` / `#00F5D4`; forest-calm `#059669` / `#92400E` / `#FBBF24`; midnight-purple `#7C3AED` / `#EC4899` / `#06B6D4`; sunset-warm `#F97316` / `#DC2626` / `#FACC15`.

## 297. Brand Type Scale
- Base `16px` (`1rem`), ratio `1.25` (Major Third).
- Display `3.815rem`/`61px` 700/`1.1`; H1 `3.052rem`/`49px` 700/`1.2`; H2 `2.441rem`/`39px` 600/`1.25`; H3 `1.953rem`/`31px` 600/`1.3`; H4 `1.563rem`/`25px` 600/`1.35`; H5 `1.25rem`/`20px` 600/`1.4`; Body Large `18px` 400/`1.6`; Body `16px` 400/`1.5`; Small `14px` 400/`1.5`; Caption `12px` 400/`1.4`.
- Practical desktop/mobile scale: H1 `48px`/`32px`, H2 `36px`/`28px` (or `24px`), H3 `28px`/`24px` (or `20px`), H4 `24px`/`20px`, body `16px` both; switch at `768px`.
- Font stack tokens `--font-heading`, `--font-body`, `--font-mono` with system fallbacks; load only weights `400;500;600;700` with `display=swap`.

## 298. Weights, Line Height and Tracking
- Regular `400` body; Medium `500` buttons, nav, links; Semibold `600` subheadings and buttons; Bold `700` headings and CTAs.
- Line height: headings `1.1-1.3`, body `1.5-1.6`, small `1.4-1.5`, long-form `1.6-1.75`.
- Tracking: display `-0.02em`; headings and body `0`; all caps `0.05em`; small caps `0.1em`.
- Spacing: h1/h2 `2rem` top `1rem` bottom; h3/h4 `1.5rem` / `0.75rem`; paragraphs `1rem` bottom.
- Measure: body `65-75` characters (`max-width: 65ch`); code `80-100`.
- Minimums: body `16px`, small `14px` (not for long content), caption `12px` sparingly; large text = `18px+`.
- No all caps for long text, no justified text (left-align), no weights `<400` at small sizes.
- Pairings: Inter/Inter (clean), Playfair Display/Source Sans Pro (professional), Poppins/Open Sans (startup), Merriweather/Lato (editorial).

## 299. Logo Variants and Clear Space
- Variants: full horizontal (headers, documents), stacked (square spaces, avatars), icon only (favicons, app icons), wordmark only (when icon already present).
- Color variants: full color on white/light, reversed on dark, monochrome dark or light when color is not possible.
- Clear space equals the height of the logo mark on all sides; co-brand clear space applies to both logos.
- Minimum digital width: full logo `120px` (some guides `80px`), icon `24px` (favicon) / `32px` (UI). Print: full `35mm` (some guides `25mm`), icon `10mm`.
- Backgrounds: white or light gray `#F5F5F5+` → full color or dark mono; brand primary or dark `#333`+ → reversed white; photography → ensure contrast.

## 300. Logo Misuse
- Never stretch, compress, rotate, skew, crop, rearrange or add elements.
- Never add drop shadows, gradients, strokes, outlines, transparency or effects.
- Never use unapproved colors or place on busy backgrounds.
- Co-branding: equal visual height, adequate separation, optional divider line, each logo in approved colors; side-by-side with divider or stacked with "+".
- Non-standard uses require a submitted mockup with context and documented approval.

## 301. Logo Placement Specs
- Formats: SVG preferred for web, PNG with transparency fallback, PDF for print, EPS legacy, `300dpi` PNG for documents.
- Social avatars icon-only: LinkedIn `300x300px`, Twitter/X `400x400px`, Facebook `180x180px`, Instagram `320x320px`.
- Website: header full horizontal `120-200px` wide; footer `100-150px`; favicon `32x32px`; Apple touch icon `180x180px`.
- Documents: letterhead top left; presentation icon + wordmark on title slide; report on cover and footer.

## 302. Imagery, Illustration and Icon Standards
- Photography: natural soft lighting, real people in authentic scenarios, brand colors maintained in post, clean focused composition.
- Illustration: modern flat with subtle gradients, brand palette only, `2px` consistent stroke, `4px` rounded corners.
- Icons: outlined on a `24px` base grid, `1.5px` stroke, `2px` corner radius, no fill.
- Image-generation style: prepend a fixed brand description (mood, hex colors, lighting, atmosphere) and keyword sets for lighting, mood, composition (centered, rule of thirds, minimal), treatment and aesthetic, plus visual don'ts.

## 303. Brand Component Defaults
- Buttons: primary `#2563EB` with white text, secondary transparent with `#2563EB` text, tertiary transparent with `#6B7280`, all `8px` radius.
- Spacing: xs `4px`, sm `8px`, md `16px`, lg `24px`, xl `32px`, 2xl `48px`.
- Radius: buttons `8px`, cards `12px`, inputs `8px`, modals `16px`, pills/tags `9999px`.
- Accessibility targets: text on white `7.2:1` (AAA), primary on white `4.6:1` (AA).

## 304. Asset Organization and Naming
- Organize by type: designs (campaigns, web, print), banners (social, email headers, landing pages), logos (full horizontal, icon only, monochrome, variations), videos (ads, tutorials, testimonials), infographics, generated assets by date.
- Name `{type}_{campaign}_{description}_{timestamp}_{variant}.{ext}`: type lowercase; campaign and description kebab-case (use "evergreen" for non-campaign); timestamp `YYYYMMDD`; optional variant (`dark-mode`, `1x1`, `mobile`).
- Track metadata: dimensions, size, type, tags, status, source/prompt, version, creator, approver and approval time; record version changes.
- Tags: status (draft, review, approved, archived), platform, content type, format (`1x1`, `4x5`, `9x16`, `16x9`), source; every asset needs status + platform + content-type.
- One file per variant (never combine dark/light); source files mirror the same structure; archive, don't delete; videos `> 100MB` live in cloud storage.

## 305. Asset Approval Checklist
- Quick review: serves purpose, right audience, no obvious errors, aligns with campaign.
- Logo: correct variant, clear space, minimum size, approved colors, unmodified, background-appropriate.
- Color: palette only, `60/30/10` ratio, correct semantic use, consistent.
- Typography: brand fonts and weights, hierarchy, medium-appropriate sizes, adequate line heights, no orphans/widows.
- Imagery: on-style, appropriate, quality, licensed/credited, optimized.
- Accessibility: text `≥4.5:1`, large `≥3:1`, visible focus, color not sole indicator, alt text, scannable layout, logical reading order, descriptive links.
- Copy: on-voice, right tone, no prohibited terms, clear value proposition, compelling CTA, proofread; benefits over features, no conflicting claims.
- Technical: correct format, resolution, optimized size, naming, metadata; platform dimensions; email assets under `1MB`.
- Legal: licensed stock, cleared audio, no trademark violations, authorized user content, disclosures, accurate pricing, privacy compliance.
- Sign-off per area (visual, copy, brand, technical, legal) with approver, date and version; archive prior versions after approval.
- Common fixes: logo too small → minimum size; wrong font → brand font; low contrast → adjust; off-brand color → palette color; blurry → higher-res source; weak CTA → action-oriented copy.

## 306. Brand Consistency Audit
- Visual: current logo version, clear space, palette colors and ratios, brand fonts and hierarchy, consistent image editing.
- Voice: matches personality, context-appropriate, consistent across channels, consistent terminology, capitalization and jargon level, consistent CTAs.
- Audit channels: website (home, product, blog, nav/footer), social (profiles, covers, bios, templates), email (headers, templates, signatures, automated), collateral (presentations, one-pagers, cards, promo).
- Frequency: website monthly; social, email and sales materials quarterly; full brand audit annually.

# Part 35 — Design Token Architecture (primitive / semantic / component)

## 307. Three-Layer Model
- Primitive (raw values, change rarely) → semantic (purpose aliases, change for theme switching) → component (per-component customization).
- Example chain: `--color-blue-600: #2563EB` → `--color-primary: var(--color-blue-600)` → `--button-bg: var(--color-primary)`.
- Never use raw hex in components; components reference semantic tokens, not primitives directly.
- Document every token's purpose; use HSL channels for opacity control.

## 308. Token Naming Convention
- Pattern `--{category}-{item}-{variant}-{state}`, e.g. `--color-primary`, `--color-primary-hover`, `--button-bg-hover`, `--space-section-sm`.
- Categories: color, space, font-size, radius, shadow, duration.
- Use semantic names (`destructive` not `red`, `muted` not `gray`, `primary` not `blue`).
- Organize as primitives, semantic, components and dark-mode override sections.
- Migrate flat tokens (`--button-primary-bg: #2563EB`) into primitive + semantic + component layers.
- JSON form follows the W3C Design Tokens format with `$value` and `$type`.

## 309. Primitive Color Scales
- Gray: `50 #F9FAFB`, `100 #F3F4F6`, `200 #E5E7EB`, `300 #D1D5DB`, `400 #9CA3AF`, `500 #6B7280`, `600 #4B5563`, `700 #374151`, `800 #1F2937`, `900 #111827`, `950 #030712`.
- Blue: `50 #EFF6FF`, `100 #DBEAFE`, `200 #BFDBFE`, `300 #93C5FD`, `400 #60A5FA`, `500 #3B82F6`, `600 #2563EB`, `700 #1D4ED8`, `800 #1E40AF`, `900 #1E3A8A`.
- Status: green `500 #22C55E` / `600 #16A34A`; yellow `500 #EAB308` / `600 #CA8A04`; red `500 #EF4444` / `600 #DC2626`; info = blue-500.
- Each scale has 11 shades `50`–`950`: `500` base, lighter below, darker above.

## 310. Primitive Spacing Scale
- `4px` base unit: `--space-0` 0, `px` 1px, `0-5` 2px, `1` 4px, `1-5` 6px, `2` 8px, `2-5` 10px, `3` 12px, `3-5` 14px, `4` 16px, `5` 20px, `6` 24px, `7` 28px, `8` 32px, `9` 36px, `10` 40px, `12` 48px, `14` 56px, `16` 64px, `20` 80px, `24` 96px.

## 311. Primitive Typography Scale
- Sizes: `xs 12px`, `sm 14px`, `base 16px`, `lg 18px`, `xl 20px`, `2xl 24px`, `3xl 30px`, `4xl 36px`, `5xl 48px`.
- Line heights: none `1`, tight `1.25`, snug `1.375`, normal `1.5`, relaxed `1.625`, loose `2`.
- Weights: normal `400`, medium `500`, semibold `600`, bold `700`.
- Tracking: tighter `-0.05em`, tight `-0.025em`, normal `0`, wide `0.025em`, wider `0.05em`.

## 312. Primitive Radius, Shadow, Motion and Z-Index
- Radius: none `0`, sm `2px`, default `4px`, md `6px`, lg `8px`, xl `12px`, 2xl `16px`, 3xl `24px`, full `9999px`.
- Shadows: sm `0 1px 2px 0 rgb(0 0 0 / 0.05)`; default `0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)`; md `0 4px 6px -1px`…; lg `0 10px 15px -3px`…; xl `0 20px 25px -5px`…; 2xl `0 25px 50px -12px rgb(0 0 0 / 0.25)`; inner `inset 0 2px 4px 0 rgb(0 0 0 / 0.05)`.
- Durations: `75`, `100`, `150`, `200`, `300`, `500`, `700`, `1000ms`; semantic fast `150ms`, normal `200ms`, slow `300ms`.
- Z-index: `0`–`50` in steps of `10`, then dropdown `1000`, sticky `1100`, modal `1200`, popover `1300`, tooltip `1400`.

## 313. Semantic Color Roles
- Background/foreground `gray-50`/`gray-900`; card and popover white with `gray-900` text.
- Primary `blue-600`, hover `blue-700`, active `blue-800`, foreground white.
- Secondary `gray-100` (hover `gray-200`) with `gray-900`; muted `gray-100` with `gray-500`; accent `gray-100` with `gray-900`.
- Destructive `red-600` (hover `red-700`) with white.
- Success `green-600`/white; warning `yellow-500`/`gray-900`; error `red-600`/white; info `blue-500`/white.
- Border and input `gray-200`; ring `blue-500`.
- Pair every color with a matching foreground token.

## 314. Semantic Spacing and Type Roles
- Component spacing: xs `space-1`, sm `space-2`, default `space-3`, lg `space-4`.
- Section spacing: sm `space-8`, default `space-12`, lg `space-16`.
- Page margins: x `space-4`, y `space-6`.
- Headings `2xl`/`3xl`/`4xl`; body `base` (sm and lg variants); label `sm`; caption `xs`.
- Interaction: ring width `2px`, ring offset `2px`, disabled opacity `0.5`.

## 315. Dark Mode Overrides
- Override only the semantic layer: background `gray-950` (or `gray-900`), foreground `gray-50`, card/popover `gray-900`, muted/secondary/accent `gray-800`, muted foreground `gray-400`, border/input `gray-800`.
- Semantic tokens make theme switching instant by toggling a root theme class.

# Part 36 — Component Specs

## 316. Component Token Sets
- Button: bg, fg, hover-bg, active-bg per variant (primary, secondary, outline border, ghost, destructive); padding default `space-4`/`space-2`, sm `space-3`/`space-1-5`, lg `space-6`/`space-3`; radius `md`; font `sm` medium.
- Input: bg background, border input, placeholder muted-foreground, focus border/ring = ring, error border/fg = error, disabled bg muted; padding `space-3`/`space-2`; radius `md`; font `sm`.
- Card: bg card, border, shadow default → md on hover, padding `space-6` (sm `space-4`), gap `space-4`, radius `lg`.
- Badge: padding `space-2-5`/`space-0-5`, radius full, font `xs`.
- Alert: padding `space-4`, radius `lg`.
- Dialog: overlay `rgb(0 0 0 / 0.5)`, shadow `lg`, padding `space-6`, radius `lg`, max-width `32rem`.
- Table: header bg muted, row hover muted, cell padding `space-4` × `space-3`.

## 317. Button Spec
- Variants: default (primary, white text, primary actions), secondary (`gray-100`/`gray-900`), outline (transparent, border, tertiary), ghost (transparent, subtle), link (primary text, navigation), destructive (`red-600`, white, dangerous).
- Sizes: sm `32px` high, `12px`×`6px` padding, `14px` text, `16px` icon; default `40px`, `16px`×`8px`, `14px`, `18px` icon; lg `48px`, `24px`×`12px`, `16px`, `20px` icon; icon `40px` square, `18px` icon.
- States: hover darker, active darkest, disabled muted at opacity `0.5` with `not-allowed`, loading opacity `0.7` with `wait` cursor.
- Shadow by state: default sm, hover md, active none, disabled none.
- Anatomy: optional leading icon, label, optional trailing icon.

## 318. Input Spec
- Variants: text, textarea, select, checkbox, radio, switch.
- Sizes: sm `32px` (`8px 12px`, `14px`), default `40px` (`8px 12px`, `14px`), lg `48px` (`12px 16px`, `16px`).
- States: default `gray-300` border; hover `gray-400`; focus primary border with primary `20%` ring; error `red-500` with red `20%` ring; disabled `gray-200` border on `gray-100`.
- Anatomy: optional label above; leading icon, value, trailing action; helper or error text below.

## 319. Card Spec
- Variants: default (shadow sm, `1px` border), elevated (shadow lg, no border), outline (no shadow, border), interactive (shadow sm → md, border).
- Anatomy: header (title, description), content, footer (actions).
- Padding: header `24px 24px 0`, content `24px`, footer `0 24px 24px`, gap `16px`.

## 320. Badge and Alert Specs
- Badge variants: default primary/white, secondary `gray-100`/`gray-900`, outline, destructive `red-600`, success `green-600`, warning `yellow-500`/`gray-900`.
- Badge sizes: sm `4px 8px`, `11px`, `20px` high; default `4px 10px`, `12px`, `24px`; lg `6px 12px`, `14px`, `28px`.
- Alert variants: default (info icon, `gray-50`/`gray-200`), destructive (alert icon, `red-50`/`red-200`), success (check, `green-50`/`green-200`), warning (`yellow-50`/`yellow-200`).
- Alert anatomy: icon, title, description, optional dismiss.

## 321. Dialog Spec
- Sizes: sm `384px` (confirmations), default `512px`, lg `640px` (complex forms), xl `768px` (data-heavy), full `100% - 32px` (mobile).
- Anatomy: header (title, description, close), scrollable content, footer with Cancel then Confirm right-aligned.
- Destructive confirmations state consequence plainly and pair Cancel with the destructive action.

## 322. Table Spec
- Row states: default white, hover `gray-50`, selected primary `10%`, striped `gray-50`/white.
- Alignment: text left, numbers right, status/badges center, actions right.
- Cell and header padding `12px 16px`; row height compact `40px`, default `48px`, comfortable `56px`.

## 323. Component Catalog Coverage
- Forms: button, input, select, checkbox, radio group, textarea, switch, date picker, validated form with label, control, description and message.
- Layout/navigation: card, tabs, accordion, navigation menu.
- Overlays: dialog, drawer, popover, toast, command palette, alert dialog.
- Feedback: alert, progress, skeleton. Display: table, avatar with fallback initials, badge.
- Compose complex UIs from small primitives; extract components only for true repetition.

# Part 37 — States & Variants

## 324. Interactive State Definitions
- Default: base appearance. Hover: slight color shift. Focus: focus ring. Active: darkest color. Disabled: reduced opacity. Loading: spinner plus reduced opacity.
- Priority when states overlap: disabled > loading > active > focus > hover > default.

## 325. State Transition Timing
- Color and background `150ms` ease-in-out; transform `200ms` ease-out; opacity `150ms` ease; shadow `200ms` ease-out.
- Transition only color, background-color, border-color and box-shadow on interactive elements.

## 326. Focus Ring Spec
- Ring width `2px`, offset `2px`, color primary (`blue-500`), offset color = background.
- Use `:focus-visible` with an outer box-shadow ring; never strip outlines without replacement.
- Containers highlight border with ring color on `:focus-within`.

## 327. Disabled Treatment
- Opacity `50%`, pointer events none, cursor `not-allowed`, muted background and muted-foreground text.
- Use `disabled` on form elements and `aria-disabled="true"` for semantic disabled; keep `3:1` minimum contrast.

## 328. Loading Treatment
- Spinner placement: button replaces icon or centers; input trailing; card center overlay; page viewport center.
- Children fade to opacity `0.7`, pointer events disabled; mark `aria-busy="true"` with screen-reader loading text.

## 329. Error Treatment
- Input border `red-500`, focus ring red `20%` (or `2px` background + `4px` error double ring), helper text `red-600`, icon `red-500`.
- Error message below the input, in error color, with an icon, cleared on valid input; mark `aria-invalid="true"` and link via `aria-describedby` to a `role="alert"` message.

## 330. Variant Patterns
- Color variants swap local component variables (bg/fg) to primary, secondary or destructive pairs.
- Size variants: sm `32px` height, `space-3` padding, `xs` font; default `40px`, `space-4`, `sm`; lg `48px`, `space-6`, `base`.
- Hover deepening via opacity on the base color (e.g. primary at `90%`, secondary at `80%`).
- Accessibility minimums: normal text `4.5:1`, large text `3:1`, UI components `3:1`, focus indicator `3:1`; never rely on color alone.

# Part 38 — Responsive Utilities & Breakpoints

## 331. Mobile-First Breakpoints
- Base styles apply everywhere; prefixes apply at min-widths: `sm` `640px`, `md` `768px`, `lg` `1024px`, `xl` `1280px`, `2xl` `1536px`.
- Max-width variants (`max-sm`, `max-md`, `max-lg`, `max-xl`, `max-2xl`) target below a breakpoint; combine min and max for ranges (e.g. tablet only between `md` and `lg`).
- Container queries (`@sm`…`@2xl`) respond to parent width rather than viewport.
- Custom breakpoints such as `3xl` `120rem` (`1920px`) and `tablet` `48rem` (`768px`).
- Write mobile-first (`text-base md:text-lg lg:text-xl`), never desktop-first.

## 332. Responsive Layout Patterns
- Grids progress `1` → `2` → `3`/`4` columns (e.g. `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4`).
- Stack vertically on mobile, row on desktop (`flex-col lg:flex-row`).
- Sidebar full-width on mobile, fixed `w-64` on desktop; main area padding `p-4 md:p-8`.
- Card grid gaps `gap-4 md:gap-6`; padding `p-4 md:p-6 lg:p-8`.
- Hero: section padding `py-12 md:py-20 lg:py-32`, title `text-4xl md:text-5xl lg:text-6xl`, centered on mobile and left-aligned on desktop, CTA padding `px-6 py-3 md:px-8 md:py-4`.
- Navigation: `h-16` bar; desktop links appear at `md`, mobile shows a menu button.
- Reorder content per breakpoint so the most important element comes first on mobile.
- Restrict hover effects to large screens where useful (e.g. `lg:hover:scale-105`).

## 333. Content Width and Containers
- Center containers with responsive gutters `px-4 sm:px-6 lg:px-8` and `max-w-7xl`.
- Container default padding `2rem` with `2xl` capped at `1400px`.
- Responsive max widths such as `max-w-sm md:max-w-2xl lg:max-w-4xl`.

## 334. Responsive Discipline
- Use the same breakpoints across related elements so spacing scales with layout.
- Limit to `2–3` breakpoints per element.
- Ensure core function works on mobile, then enhance.
- Testing: `320px`, `640px`, `768px`, `1024px`, `1280px`, landscape, touch targets `44x44px`, readability at all sizes, mobile navigation, browser zoom.

## 335. Utility Scales
- Spacing scale `0`, `px` 1px, `0.5` 2px, `1` 4px, `2` 8px, `3` 12px, `4` 16px, `6` 24px, `8` 32px, `12` 48px, `16` 64px, `24` 96px.
- Text sizes `xs 12px` to `5xl 48px`; weights thin `100`, light `300`, normal `400`, medium `500`, semibold `600`, bold `700`, black `900`.
- Radius `rounded` `0.25rem`, `md` `0.375rem`, `lg` `0.5rem`, `xl` `0.75rem`, `2xl` `1rem`, `full` `9999px`.
- Shadow steps sm → 2xl; colored shadows (e.g. blue at `50%`) for glow accents.
- Aspect ratios square `1:1`, video `16:9`, custom `4/3`.
- Opacity modifiers (`/75`, `/30`) on colors; gradients by direction with optional via-stop.
- Text overflow: truncate with ellipsis or clamp to `3` lines.

# Part 39 — Theming

## 336. CSS Variable Theme System
- Define theme roles as HSL channels without the wrapper (e.g. `--primary: 222.2 47.4% 11.2%`) so opacity modifiers work (`hsl(var(--primary) / 0.5)`).
- Core roles: background, foreground, card, popover, primary, secondary, muted, accent, destructive (each with foreground), border, input, ring, and `--radius`.
- Light reference: background `0 0% 100%`, foreground `222.2 84% 4.9%`, secondary/muted/accent `210 40% 96.1%`, muted foreground `215.4 16.3% 46.9%`, destructive `0 84.2% 60.2%`, border/input `214.3 31.8% 91.4%`.
- Dark reference: background `222.2 84% 4.9%`, foreground `210 40% 98%`, primary inverts to `210 40% 98%`, secondary/muted/accent/border `217.2 32.6% 17.5%`, muted foreground `215 20.2% 65.1%`, destructive `0 62.8% 30.6%`, ring `212.7 26.8% 83.9%`.
- Blue-brand variant: primary and ring `217 91% 60%`, dark background `222 47% 4%`.

## 337. Radius System
- One `--radius` drives all corners: lg = `var(--radius)`, md = `calc(var(--radius) - 2px)`, sm = `calc(var(--radius) - 4px)`.
- Default `0.5rem`; `0rem` for sharp, `1rem` for rounded personalities.

## 338. Dark Mode Implementation
- Toggle a root `dark` class; default to system preference (`prefers-color-scheme: dark`) and persist the user's choice.
- Disable transitions during theme change to avoid flashes.
- Theme toggle: ghost icon button with sun/moon crossfade-rotate and screen-reader text "Toggle theme".
- Apply dark variants to every themed element; test both themes.

## 339. Multiple Themes and Presets
- Scope alternate brand themes with data attributes (e.g. violet primary `262.1 83.3% 57.8%`, rose primary `346.8 77.2% 49.8%`).
- Base neutral presets: Slate (cool), Gray (neutral), Zinc (warm), Neutral (balanced), Stone (earthy).
- Style presets: Default (softer, more rounded) vs New York (sharper, higher contrast).

## 340. Theme Tokens in the Framework
- Map theme variables to framework color names so utilities read semantically (`bg-primary`, `text-muted-foreground`).
- Define custom tokens in the theme layer: brand scales in oklch (e.g. `--color-brand-500: oklch(0.55 0.22 264)`), fonts (`--font-display`), spacing (`--spacing-navbar: 4.5rem`, `--spacing-section: 6rem`, header `4rem`, footer `3rem`), shadows (`--shadow-glow: 0 0 20px rgba(139, 92, 246, 0.3)`), radius (`--radius-large: 1.5rem`).
- Full oklch primary scale from `50` `oklch(0.98 0.02 250)` to `950` `oklch(0.15 0.10 250)`, holding hue constant.
- Semantic oklch status: success `oklch(0.65 0.18 145)`, warning `oklch(0.75 0.15 85)`, error `oklch(0.60 0.22 25)`, info `oklch(0.65 0.18 240)`.
- Custom variants for theme scopes and ARIA states (e.g. `aria-checked`, `required`).
- Glass utility: background white at `0.1`, `blur(10px)`, `1px` border white at `0.2`.
- Base layer sets body background/foreground and antialiasing, heading weights and tight tracking, link underline offset `4`.
- Keep base, components and utilities layers separate; extract shared patterns sparingly; use `text-wrap: balance` for headings.
- Motion tokens: fast `150ms`, normal `200ms`, slow `300ms`; accordion open/close `0.2s` ease-out.

## 341. Theming Best Practices
- Use CSS variables for runtime theme switching.
- Pair each color with an appropriate foreground.
- Use semantic names; maintain WCAG AA contrast.
- Override one-offs via class names; turn repeated overrides into named variants (e.g. a gradient variant, an `xl` size at `h-14 px-10 text-lg`).
- Avoid dynamically built class names so unused styles can be purged.

# Part 40 — Component Accessibility

## 342. Accessible Primitive Foundation
- Build on unstyled primitives that follow WAI-ARIA patterns: built-in keyboard navigation, screen-reader announcements, focus management and automatic ARIA attributes.
- Use semantic elements (`button`, `nav`, `a`); never clickable `div` soup.

## 343. Keyboard Patterns
- Dialogs trap focus, auto-focus the first field, close on Esc, cycle with Tab and return focus to the trigger.
- Menus: Space/Enter opens, Arrow Up/Down moves, Esc closes, Tab closes and moves on.
- Command palette: type to filter, arrows to navigate, Enter selects, Esc closes.
- Tabs: arrow keys navigate, Space/Enter activates; panels labelled by their trigger.
- Accordion triggers expose `aria-expanded` and `aria-controls`.
- Skip link is visually hidden until focused, then appears top-left above content.

## 344. Labels and Descriptions
- Icon-only buttons get `aria-label` or visually hidden text (e.g. "Delete item", "Close dialog").
- Use `aria-describedby` for consequences (e.g. permanent account deletion).
- Visually hidden text: `1px` box, `-1px` margin, clipped, no wrap.
- Select triggers need an accessible label; checkboxes link to descriptive text.

## 345. Live Regions
- Polite live regions (`aria-live="polite"`, `aria-atomic="true"`) for status messages and toasts; assertive only for urgent errors.
- Alerts use `role="alert"` for immediate announcement.

## 346. Accessible Forms
- Always associate labels with inputs; add persistent descriptions under fields.
- Set `aria-invalid` and link errors via `aria-describedby`.
- Required fields show a visual asterisk plus hidden "(required)" text and the `required` attribute.
- Group related fields in `fieldset` with a `legend`.

## 347. Contrast and Focus in Components
- AA `4.5:1` normal / `3:1` large; AAA `7:1` / `4.5:1`.
- Avoid low-contrast pairs like `gray-400` on light or `gray-600` on dark; use the semantic muted-foreground for secondary text.
- Focus via `focus-visible` ring `2px` with ring offset `2px`; never `focus:outline-none` without a replacement.

## 348. Reduced Motion
- Under `prefers-reduced-motion: reduce`, set animation and transition durations to `0.01ms` and iteration count to `1`, or disable transitions per element.

## 349. Accessibility Testing Checklist
- All interactive elements keyboard accessible with visible focus and logical tab order.
- Screen reader announces content, form errors are announced and associated.
- AA contrast, semantic HTML, labels on icon-only buttons.
- Modal focus trap works; dropdowns and selects keyboard navigable; live regions announce updates.
- Respects reduced motion; works at browser zoom up to `200%`; skip links present.
- Audit with automated checkers, keyboard-only passes and real screen readers.

# Part 41 — Canvas/Visual Design System

## 350. Two-Phase Visual Philosophy
- First write a visual philosophy (an aesthetic movement in `4-6` paragraphs) covering space and form, color and material, scale and rhythm, composition and balance, and visual hierarchy.
- Then express it as artifacts that are `90%` visual and `10%` essential text, single page by default.
- The philosophy guides every decision; name the movement.

## 351. Visual Communication First
- Information lives in design, not paragraphs: color zones, geometric precision, spatial relationships, visual weight and tension, form and structure.
- Text is a rare, powerful gesture: never paragraphs, only essential words integrated into the visual architecture, small labels with huge impact.

## 352. Systematic Patterns
- Repeating patterns establish rhythm; perfect geometric shapes; clinical typography.
- Dense accumulation of marks and layered elements reward sustained viewing.
- Reference markers can suggest an imaginary discipline.

## 353. Design Movement Archetypes
- Concrete Poetry: massive color blocks, sculptural type (huge words, tiny labels), brutalist spatial divisions.
- Chromatic Language: color as the primary information system, geometric precision, minimal small sans labels.
- Analog Meditation: paper grain, ink bleeds, vast negative space, whispered typography, photobook pacing.
- Organic Systems: rounded forms, modular clustering, nature-derived color, labels floating in space.
- Geometric Silence: grid precision, dramatic negative space, Swiss formalism with brutalist material honesty.
- Weave niche references in subtly so they deepen the work without being literal.

## 354. Canvas Color and Type
- Limited palette of `2-5` colors in a cohesive system, each carrying meaning; define in oklch, e.g. primary `oklch(0.55 0.22 264)`, accent `oklch(0.75 0.18 45)`, neutral `oklch(0.90 0.02 264)`, dark `oklch(0.25 0.15 264)`.
- Prefer thin weights `200-300` in clean geometric sans; small sizes for labels, large for impact moments; treat type as part of the art.

## 355. Spacing and Boundaries
- Nothing falls off the page and nothing overlaps; every element within canvas boundaries.
- Proper margins are non-negotiable; breathing room and clear separation; flawless formatting.

## 356. Multi-Page Systems
- Treat pages like a coffee-table book: distinctly different yet cohesive.
- Share palette, type system, compositional approach and a philosophical thread.
- Vary focal points, spatial arrangements and patterns per page to build a progressive narrative.

## 357. Refinement and Quality Bar
- Second pass refines rather than adds: make existing elements crisper and more cohesive; polish, don't expand.
- Avoid cartoony aesthetics, text-heavy composition, random placement, overlaps, inconsistent spacing and an obviously generated look.
- Aim for museum-quality, magazine-worthy, meticulously crafted work that appears the product of countless hours.
- Execution checklist: philosophy-driven, `90/10` visual-to-text, nothing overlapping or off-page, pristine margins, cohesive, sophisticated, flawless.
- Apply to brand identity systems, posters, visual manifestos, design-system documentation, editorial and exhibition material.

# Part 42 — Choosing a Visual Style

## 358. Match the Style to the Product and Audience
- Start from the product's job and audience, not from trends: every style has a "best for" and a "do not use for" list, and the exclusions matter as much as the fit.
- Conservative, high-trust domains (finance, healthcare, legal, government, enterprise, elderly users) consistently exclude loud styles: Brutalism, Vibrant & Block-based, Y2K, Cyberpunk, Memphis, Vaporwave, Gen Z Chaos, Chromatic Aberration and Neubrutalism.
- Trust-heavy products lean on restrained styles: Minimalism & Swiss Style, Swiss Modernism 2.0, Flat Design, Soft UI Evolution, Trust & Authority, Accessible & Ethical, and Enterprise SaaS.
- Youth, entertainment, music, gaming and creative audiences are where expressive styles earn their keep: Vibrant & Block-based, Neubrutalism, Y2K, Memphis, Vaporwave, Retro-Futurism, Pixel Art, Gen Z Chaos, Kinetic Typography.
- Wellness, sustainability and calm products map to soft, natural palettes: Organic Biophilic, Nature Distilled, Neumorphism, Claymorphism, Biomimetic / Organic 2.0.
- Data products need dense, neutral styles (Data-Dense Dashboard, Minimalism, Flat Design); nearly every decorative style lists "data-heavy dashboards" or "dense data tables" as a misuse.
- Long-form reading needs calm typography and minimal motion (E-Ink / Paper, Editorial Grid / Magazine, Minimal & Direct); motion-led and maximalist styles exclude "content-heavy" and "long-form" contexts.
- When building for a specific platform (Apple, Android/Material, Microsoft, Shopify admin, Adobe tools), adopt that platform's design system and tokens instead of inventing a style; platform systems explicitly exclude products outside their ecosystem.

## 359. Use Accessibility as a Universal Baseline
- Every style, without exception, requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states and a reduced-motion alternative; treat these as non-negotiable whatever the aesthetic.
- Inclusive styles raise the bar: target `7:1` contrast for normal text, minimum `16px` body text, `3-4px` focus rings, `44x44px` touch targets and no colour-only indicators.
- High accessibility-risk styles need extra verification before shipping: Neumorphism, 3D & Hyperrealism, Retro-Futurism, Vaporwave, Dimensional Layering, Kinetic Typography, Parallax Storytelling, HUD / Sci-Fi FUI, Gen Z Chaos, Interactive Cursor Design, Chromatic Aberration.
- The recurring risks are low-contrast soft shadows (Neumorphism), text over vibrant or blurred backgrounds (Glassmorphism, Aurora, Gradient Mesh), motion and glitch effects that trigger vestibular issues, and custom cursors that hide the system pointer.
- Glass and translucent materials must always have a reduced-transparency fallback to an opaque surface.
- Accessibility styles have no "do not use" list: accessibility is universal and should be layered onto any other style.

## 360. Decide Light and Dark Mode Deliberately
- Most styles work in both modes, but several are dark-only by nature and should not be forced into light mode: Dark Mode (OLED), Cyberpunk UI, Terminal CLI, Cyberpunk Mobile HUD and Bitcoin DeFi.
- Styles that default to dark presentation include Retro-Futurism, Vaporwave, Chromatic Aberration, Modern Dark (Cinema Mobile), Kinetic Brutalism, Bold Typography (Mobile Poster) and Academia.
- Some styles are light-only: E-Ink / Paper, Neo Brutalism (Mobile) and Neumorphism (Mobile) do not translate to dark mode, because their effect depends on paper-like or light clay surfaces.
- Soft-depth and pastel styles (Neumorphism, Claymorphism, Y2K, Nature Distilled, Vintage Analog) are only conditionally dark-capable; their shadows and pastels lose definition on dark grounds.
- Realistic and 3D styles (3D & Hyperrealism, Skeuomorphism, 3D Product Preview) are conditional in both modes because lighting and materials must be re-authored per theme.
- In dark themes prefer near-black surfaces such as `#121212` or `#050506` over pure `#000000` when content scrolls, to avoid OLED smear; reserve pure black for true OLED-optimised designs.
- Use semantic colour tokens (surface, on-surface, label, accent) so a theme switch is a token swap, not a redesign.

## 361. Weigh Performance Cost Against Impact
- Most styles are low cost; the expensive ones are driven by animation, blur and large images.
- High-cost styles (3D & Hyperrealism, Skeuomorphism, Parallax Storytelling, Gen Z Chaos, 3D Product Preview, Cyberpunk Mobile HUD, Claymorphism (Mobile)) need lazy loading, level-of-detail, image optimisation and a lighter fallback for low-end devices.
- Blur-based materials (Glassmorphism, Liquid Glass, Spatial UI, Modern Dark, Bitcoin DeFi) and continuously animated styles carry moderate cost; limit the number of blurred layers and pause loops off-screen.
- Animate only `transform` and `opacity`, use GPU acceleration and `will-change: transform` sparingly, and drive scroll effects with Intersection Observer.
- Minimal and flat styles win on speed: aim for page weight under `500KB` and load time under `2s` where the style's promise is directness.

## 362. Design for Mobile First Where the Style Allows
- Mobile-native styles assume safe areas, `44-48px` touch targets, bottom navigation, haptic feedback on presses and press states instead of hover.
- Styles not recommended for mobile (3D & Hyperrealism, Skeuomorphism, Parallax Storytelling, Interactive Cursor Design, Executive Dashboard, Financial Dashboard) need a separate simplified mobile experience; cursor-driven effects simply do not exist on touch screens.
- Data-dense dashboards and many analytics views are conditional on mobile: stack cards, simplify to key metrics and keep tables horizontally scrollable.
- Replace hover-to-reveal with tap or always-visible affordances on touch devices.

## 363. Optimise for Conversion When It Is the Goal
- The highest-converting patterns are hero-centric layouts, conversion-optimised single-CTA pages, interactive product demos, kinetic typography heroes, tactile deformable controls and 3D product previews.
- Conversion styles share rules: one high-contrast primary CTA, value proposition above the fold, social proof and trust badges near the CTA, minimal form fields (`3-5`) and clear loading and success states.
- Dashboards and analytics styles are not conversion surfaces; optimise them for comprehension and decision-making instead.
- Raw, sketchy, terminal and pure neumorphic styles convert poorly; use them where personality matters more than funnel performance.
- Viral and high-energy styles (Gen Z Chaos, Kinetic Brutalism) convert through shareability and excitement rather than clarity; pair them with an unmistakable CTA.

## 364. Prefer Living Styles and Build on Parent Styles
- Many styles are specialised variants of a parent style (for example dashboard sub-types of Data-Dense Dashboard, or mobile variants of desktop styles); learn the parent's rules first and then apply the variant's refinements.
- Several early landing-page patterns and the legacy bento grid are superseded by newer patterns; use the newer versions for new work.
- Combine a structural style (grid, bento, editorial, dashboard) with a surface style (flat, glass, soft UI) and an accessibility baseline, rather than stacking several decorative styles.
- Check right-to-left support: directional motion, marquees, parallax and text animation need mirroring or review for RTL languages.

# Part 43 — General UI Styles

## 365. Minimalism & Swiss Style
- Keywords and mood: Clean, simple, spacious, functional, white space, high contrast, geometric, sans-serif, grid-based, essential
- Also known as: Minimal, Minimalism, Minimalism (Frame)
- Origin and era: 1950s Swiss; implementation complexity low
- Primary colours: Monochromatic, Black `#000000`, White `#FFFFFF`
- Secondary colours: Neutral (Beige `#F5F1E8`, Grey `#808080`, Taupe `#B38B6D`), Primary accent
- Effects and animation: Subtle hover (`200-250ms`), smooth transitions, sharp shadows if any, clear type hierarchy, fast loading
- Best for: Enterprise apps, dashboards, documentation sites, SaaS platforms, professional tools
- Do not use for: Creative portfolios, entertainment, playful brands, artistic experiments
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a minimalist landing page. Use: white space, geometric layouts, sans-serif fonts, high contrast, grid-based structure, essential elements only. Avoid shadows and gradients. Focus on clarity and functionality.
- Key properties and techniques: `display: grid`, `gap: 2rem`, `font-family: sans-serif`, `color: #000 or #FFF`, `max-width: 1200px`, `clean borders`, `no box-shadow unless necessary`
- Implementation checklist: Grid-based layout 12-16 columns; Typography hierarchy clear; No unnecessary decorations; text contrast measured against the chosen project target; Mobile responsive grid
- Design-system variables: `--spacing: 2rem`, `--border-radius: 0px`, `--font-weight: 400-700`, `--shadow: none`, `--accent-color: single primary only`

## 366. Neumorphism
- Keywords and mood: Soft UI, embossed, debossed, convex, concave, light source, subtle depth, rounded (12-16px), monochromatic
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Light pastels: Soft Blue `#C8E0F4`, Soft Pink `#F5E0E8`, Soft Grey `#E8E8E8`
- Secondary colours: Tints/shades (±`30%`), gradient subtlety, color harmony
- Effects and animation: Soft box-shadow (multiple: `-5px -5px 15px`, `5px 5px 15px`), smooth press (`150ms`), inner subtle shadow
- Best for: Health/wellness apps, meditation platforms, fitness trackers, minimal interaction UIs
- Do not use for: Complex apps, critical accessibility, data-heavy dashboards, high-contrast required
- Light mode supported; dark mode conditional (works only with careful tuning)
- Performance: low cost; no heavy rendering drivers
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Create a neumorphic UI with soft 3D effects. Use light pastels, rounded corners (12-16px), subtle soft shadows (multiple layers), no hard lines, monochromatic color scheme with light/dark variations. Embossed/debossed effect on interactive elements.
- Key properties and techniques: `border-radius: 12-16px`, `box-shadow: -5px -5px 15px rgba(0,0,0,0.1)`, `5px 5px 15px rgba(255,255,255,0.8)`, `background: linear-gradient(145deg, color1, color2)`, `transform: scale on press`
- Implementation checklist: Rounded corners `12-16px` consistent; Multiple shadow layers (2-3); Pastel color verified; Monochromatic palette checked; Press animation smooth `150ms`
- Design-system variables: `--border-radius: 14px`, `--shadow-soft-1: -5px -5px 15px`, `--shadow-soft-2: 5px 5px 15px`, `--color-light: #F5F5F5`, `--color-primary: single pastel`

## 367. Glassmorphism
- Keywords and mood: Frosted glass, transparent, blurred background, layered, vibrant background, light source, depth, multi-layer
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Translucent white: `rgba(255,255,255,0.1-0.3)`
- Secondary colours: Vibrant: Electric Blue `#0080FF`, Neon Purple `#8B00FF`, Vivid Pink `#FF1493`, Teal `#20B2AA`
- Effects and animation: Backdrop blur (`10-20px`), subtle border (`1px` solid rgba white 0.2), light reflection, Z-depth
- Best for: Modern SaaS, financial dashboards, high-end corporate, lifestyle apps, modal overlays, navigation
- Do not use for: Low-contrast backgrounds, critical accessibility, performance-limited, dark text on dark
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a glassmorphic interface with frosted glass effect. Use backdrop blur (10-20px), translucent overlays (rgba 10-30% opacity), vibrant background colors, subtle borders, light source reflection, layered depth. Perfect for modern overlays and cards.
- Key properties and techniques: `backdrop-filter: blur(15px)`, `background: rgba(255, 255, 255, 0.15)`, `border: 1px solid rgba(255,255,255,0.2)`, `-webkit-backdrop-filter: blur(15px)`, `z-index layering for depth`
- Implementation checklist: Backdrop-filter blur `10-20px`; Translucent white `15-30%` opacity; Subtle border `1px` light; Vibrant background verified; Text contrast `4.5:1` checked
- Design-system variables: `--blur-amount: 15px`, `--glass-opacity: 0.15`, `--border-color: rgba(255,255,255,0.2)`, `--background: vibrant color`, `--text-color: light/dark based on BG`

## 368. Brutalism
- Keywords and mood: Raw, unpolished, stark, high contrast, plain text, default fonts, visible borders, asymmetric, anti-design
- Origin and era: 1950s Brutalist; implementation complexity low
- Primary colours: Primary: Red `#FF0000`, Blue `#0000FF`, Yellow `#FFFF00`, Black `#000000`, White `#FFFFFF`
- Secondary colours: Limited: Neon Green `#00FF00`, Hot Pink `#FF00FF`, minimal secondary
- Effects and animation: No smooth transitions (instant), sharp corners (`0px`), bold typography (700+), visible grid, large blocks
- Best for: Design portfolios, artistic projects, counter-culture brands, editorial/media sites, tech blogs
- Do not use for: Corporate environments, conservative industries, critical accessibility, customer-facing professional
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Low
- Right-to-left support: full
- Design brief: Create a brutalist design with raw, unpolished, stark aesthetic. Use pure primary colors (red, blue, yellow), black & white, no smooth transitions (instant), sharp corners, bold large typography, visible grid lines, default system fonts, intentional 'broken' design elements.
- Key properties and techniques: `border-radius: 0px`, `transition: none or 0s`, `font-family: system-ui or monospace`, `font-weight: 700+`, `border: visible 2-4px`, `colors: #FF0000`, `#0000FF`, `#FFFF00`, `#000000`, `#FFFFFF`
- Implementation checklist: No border-radius (`0px`); No transitions (instant); Bold typography (700+); Pure primary colors used; Visible grid/borders; Asymmetric layout intentional
- Design-system variables: `--border-radius: 0px`, `--transition-duration: 0s`, `--font-weight: 700-900`, `--colors: primary only`, `--border-style: visible`, `--grid-visible: true`

## 369. 3D & Hyperrealism
- Keywords and mood: Depth, realistic textures, 3D models, spatial navigation, tactile, skeuomorphic elements, rich detail, immersive
- Origin and era: 2020s Modern; implementation complexity high
- Primary colours: Deep Navy `#001F3F`, Forest Green `#228B22`, Burgundy `#800020`, Gold `#FFD700`, Silver `#C0C0C0`
- Secondary colours: Complex gradients (5-10 stops), realistic lighting, shadow variations (`20-40%` darker)
- Effects and animation: WebGL/Three.js 3D, realistic shadows (layers), physics lighting, parallax (3-5 layers), smooth 3D (`300-400ms`)
- Best for: Gaming, product showcase, immersive experiences, high-end e-commerce, architectural viz, VR/AR
- Do not use for: Low-end mobile, performance-limited, critical accessibility, data tables/forms
- Light mode conditional (works only with careful tuning); dark mode conditional (works only with careful tuning)
- Performance: high cost; driven by animation and large images
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: not recommended on mobile
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Build an immersive 3D interface using realistic textures, 3D models (Three.js/Babylon.js), complex shadows, realistic lighting, parallax scrolling (3-5 layers), physics-based motion. Include skeuomorphic elements with tactile detail.
- Key properties and techniques: `transform: translate3d`, `perspective: 1000px`, `WebGL canvas`, `Three.js/Babylon.js library`, `box-shadow: complex multi-layer`, `background: complex gradients`, `filter: drop-shadow()`
- Implementation checklist: WebGL/Three.js integrated; 3D models loaded; Parallax 3-5 layers; Realistic lighting verified; Complex shadows rendered; Physics animation smooth `300-400ms`
- Design-system variables: `--perspective: 1000px`, `--parallax-layers: 5`, `--lighting-intensity: realistic`, `--shadow-depth: 20-40%`, `--animation-duration: 300-400ms`

## 370. Vibrant & Block-based
- Keywords and mood: Bold, energetic, playful, block layout, geometric shapes, high color contrast, duotone, modern, energetic
- Also known as: Vibrant & Block
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Neon Green `#39FF14`, Electric Purple `#BF00FF`, Vivid Pink `#FF1493`, Bright Cyan `#00FFFF`, Sunburst `#FFAA00`
- Secondary colours: Complementary: Orange `#FF7F00`, Shocking Pink `#FF006E`, Lime `#CCFF00`, triadic schemes
- Effects and animation: Large sections (`48px`+ gaps), animated patterns, bold hover (color shift), scroll-snap, large type (`32px`+), `200-300ms`
- Best for: Startups, creative agencies, gaming, social media, youth-focused, entertainment, consumer
- Do not use for: Financial institutions, healthcare, formal business, government, conservative, elderly
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design an energetic, vibrant interface with bold block layouts, geometric shapes, high color contrast, large typography (32px+), animated background patterns, duotone effects. Perfect for startups and youth-focused apps. Use 4-6 contrasting colors from complementary/triadic schemes.
- Key properties and techniques: `display: flex/grid with large gaps (48px+)`, `font-size: 32px+`, `background: animated patterns (CSS)`, `color: neon/vibrant colors`, `animation: continuous pattern movement`
- Implementation checklist: Block layout with `48px`+ gaps; Large typography `32px`+; 4-6 vibrant colors max; Animated patterns active; Scroll-snap enabled; High contrast verified (`7:1+`)
- Design-system variables: `--block-gap: 48px`, `--typography-size: 32px+`, `--color-palette: 4-6 vibrant colors`, `--animation: continuous pattern`, `--contrast-ratio: 7:1+`

## 371. Dark Mode (OLED)
- Keywords and mood: Dark theme, low light, high contrast, deep black, midnight blue, eye-friendly, OLED, night mode, power efficient
- Also known as: Dark Mode
- Origin and era: 2020s Modern; implementation complexity low
- Primary colours: Deep Black `#000000`, Dark Grey `#121212`, Midnight Blue `#0A0E27`
- Secondary colours: Vibrant accents: Neon Green `#39FF14`, Electric Blue `#0080FF`, Gold `#FFD700`, Plasma Purple `#BF00FF`
- Effects and animation: Minimal glow (text-shadow: 0 0 `10px`), dark-to-light transitions, low white emission, high readability, visible focus
- Best for: Night-mode apps, coding platforms, entertainment, eye-strain prevention, OLED devices, low-light
- Do not use for: Print-first content, high-brightness outdoor, color-accuracy-critical
- Light mode not recommended; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Low
- Right-to-left support: full
- Design brief: Create an OLED-optimized dark interface with deep black (#000000), dark grey (#121212), midnight blue accents. Use minimal glow effects, vibrant neon accents (green, blue, gold, purple), high contrast text. Optimize for eye comfort and OLED power saving.
- Key properties and techniques: `background: #000000 or #121212`, `color: #FFFFFF or #E0E0E0`, `text-shadow: 0 0 10px neon-color (sparingly)`, `filter: brightness(0.8) if needed`, `color-scheme: dark`
- Implementation checklist: Deep black `#000000` or `#121212`; Vibrant neon accents used; Text contrast `7:1+`; Minimal glow effects; OLED power optimization; No white (`#FFFFFF`) background
- Design-system variables: `--bg-black: #000000`, `--bg-dark-grey: #121212`, `--text-primary: #FFFFFF`, `--accent-neon: neon colors`, `--glow-effect: minimal`, `--oled-optimized: true`

## 372. Accessible & Ethical
- Keywords and mood: Accessible, inclusive interface, high contrast, large text (16px+), keyboard navigation, screen reader friendly, accessibility standards aware, focus state, semantic
- Origin and era: Universal; implementation complexity low
- Primary colours: Measured high-contrast pairs (`4.5:1` normal-text baseline; `7:1` enhanced target), simple primary, clear secondary, high luminosity (`7:1+`)
- Secondary colours: Symbol-based colors (not color-only), supporting patterns, inclusive combinations
- Effects and animation: Clear focus rings (`3-4px`), ARIA labels, skip links, responsive design, reduced motion, 44x44px touch targets
- Best for: Government, healthcare, education, inclusive products, large audience, legal compliance, public
- Do not use for: None - accessibility universal
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design toward enhanced accessibility criteria; verify complete-page conformance. Include: high contrast (7:1+), large text (16px+), keyboard navigation, screen reader compatibility, focus states visible (3-4px ring), semantic HTML, ARIA labels, skip links, reduced motion support (prefers-reduced-motion), 44x44px touch targets.
- Key properties and techniques: `color-contrast: 7:1+`, `font-size: 16px+`, `outline: 3-4px on :focus-visible`, `aria-label`, `role attributes`, `@media (prefers-reduced-motion)`, `touch-target: 44x44px`, `cursor: pointer`
- Implementation checklist: complete-page conformance tested against the chosen target; `7:1+` contrast checked; Keyboard navigation tested; Screen reader tested; Focus visible `3-4px`; Semantic HTML used; Touch targets 44x44px
- Design-system variables: `--contrast-ratio: 7:1`, `--font-size-min: 16px`, `--focus-ring: 3-4px`, `--touch-target: 44x44px`, `--wcag-target: enhanced`, `--keyboard-accessible: true`, `--sr-test-required: true`

## 373. Claymorphism
- Keywords and mood: Soft 3D, chunky, playful, toy-like, bubbly, thick borders (3-4px), double shadows, rounded (16-24px)
- Also known as: Claymorphism (for patients)
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Pastel: Soft Peach `#FDBCB4`, Baby Blue `#ADD8E6`, Mint `#98FF98`, Lilac `#E6E6FA`, light BG
- Secondary colours: Soft gradients (pastel-to-pastel), light/dark variations (`20-30%`), gradient subtle
- Effects and animation: Inner+outer shadows (subtle, no hard lines), soft press (`200ms` ease-out), fluffy elements, smooth transitions
- Best for: Educational apps, children's apps, SaaS platforms, creative tools, fun-focused, onboarding, casual games
- Do not use for: Formal corporate, professional services, data-critical, serious/medical, legal apps, finance
- Light mode supported; dark mode conditional (works only with careful tuning)
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a playful, toy-like interface with soft 3D, chunky elements, bubbly aesthetic, rounded edges (16-24px), thick borders (3-4px), double shadows (inner + outer), pastel colors, smooth animations. Perfect for children's apps and creative tools.
- Key properties and techniques: `border-radius: 16-24px`, `border: 3-4px solid`, `box-shadow: inset -2px -2px 8px`, `4px 4px 8px`, `background: pastel-gradient`, `animation: soft bounce (cubic-bezier 0.34, 1.56)`
- Implementation checklist: Border-radius `16-24px`; Thick borders `3-4px`; Double shadows (inner+outer); Pastel colors used; Soft bounce animations; Playful interactions
- Design-system variables: `--border-radius: 20px`, `--border-width: 3-4px`, `--shadow-inner: inset -2px -2px 8px`, `--shadow-outer: 4px 4px 8px`, `--color-palette: pastels`, `--animation: bounce`

## 374. Aurora UI
- Keywords and mood: Vibrant gradients, smooth blend, Northern Lights effect, mesh gradient, luminous, atmospheric, abstract
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Complementary: Blue-Orange, Purple-Yellow, Electric Blue `#0080FF`, Magenta `#FF1493`, Cyan `#00FFFF`
- Secondary colours: Smooth transitions (Blue→Purple→Pink→Teal), iridescent effects, blend modes (screen, multiply)
- Effects and animation: Large flowing CSS/SVG gradients, subtle `8-12s` animations, depth via color layering, smooth morph
- Best for: Modern SaaS, creative agencies, branding, music platforms, lifestyle, premium products, hero sections
- Do not use for: Data-heavy dashboards, critical accessibility, content-heavy where distraction issues
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Create a vibrant gradient interface inspired by Northern Lights with mesh gradients, smooth color blends, flowing animations. Use complementary color pairs (blue-orange, purple-yellow), flowing background gradients, subtle continuous animations (8-12s loops), iridescent effects.
- Key properties and techniques: `background: conic-gradient or radial-gradient with multiple stops`, `animation: @keyframes gradient (8-12s)`, `background-size: 200% 200%`, `filter: saturate(1.2)`, `blend-mode: screen or multiply`
- Implementation checklist: Mesh/flowing gradients applied; `8-12s` animation loop; Complementary colors used; Smooth color transitions; Iridescent effect subtle; Text contrast verified
- Design-system variables: `--gradient-colors: complementary pairs`, `--animation-duration: 8-12s`, `--blend-mode: screen`, `--color-saturation: 1.2`, `--effect: iridescent`, `--loop-smooth: true`

## 375. Retro-Futurism
- Keywords and mood: Vintage sci-fi, 80s aesthetic, neon glow, geometric patterns, CRT scanlines, pixel art, cyberpunk, synthwave
- Origin and era: 1980s Retro; implementation complexity medium
- Primary colours: Neon Blue `#0080FF`, Hot Pink `#FF006E`, Cyan `#00FFFF`, Deep Black `#1A1A2E`, Purple `#5D34D0`
- Secondary colours: Metallic Silver `#C0C0C0`, Gold `#FFD700`, duotone, `80s` Pink `#FF10F0`, neon accents
- Effects and animation: CRT scanlines (::before overlay), neon glow (text-shadow+box-shadow), glitch effects (skew/offset keyframes)
- Best for: Gaming, entertainment, music platforms, tech brands, artistic projects, nostalgic, cyberpunk
- Do not use for: Conservative industries, critical accessibility, professional/corporate, elderly, legal/finance
- Light mode supported; dark mode supported; default to dark presentation
- Performance: moderate cost; driven by animation and blur
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Build a retro-futuristic (cyberpunk/vaporwave) interface with neon colors (blue, pink, cyan), deep black background, 80s aesthetic, CRT scanlines, glitch effects, neon glow text/borders, monospace fonts, geometric patterns. Use neon text-shadow and animated glitch effects.
- Key properties and techniques: `color: neon colors (#0080FF, #FF006E, #00FFFF)`, `text-shadow: 0 0 10px neon`, `background: #000 or #1A1A2E`, `font-family: monospace`, `animation: glitch (skew+offset)`, `filter: hue-rotate`
- Implementation checklist: Neon colors used; CRT scanlines effect; Glitch animations active; Monospace font; Deep black background; Glow effects applied; `80s` patterns present
- Design-system variables: `--neon-colors: #0080FF #FF006E #00FFFF`, `--background: #000000`, `--font-family: monospace`, `--effect: glitch+glow`, `--scanline-opacity: 0.3`, `--crt-effect: true`

## 376. Flat Design
- Keywords and mood: 2D, minimalist, bold colors, no shadows, clean lines, simple shapes, typography-focused, modern, icon-heavy
- Origin and era: 2010s Modern; implementation complexity low
- Primary colours: Solid bright: Red, Orange, Blue, Green, limited palette (4-6 max)
- Secondary colours: Complementary colors, muted secondaries, high saturation, clean accents
- Effects and animation: No gradients/shadows, simple hover (color/opacity shift), fast loading, clean transitions (`150-200ms` ease), minimal icons
- Best for: Web apps, mobile apps, cross-platform, startup MVPs, user-friendly, SaaS, dashboards, corporate
- Do not use for: Complex 3D, premium/luxury, artistic portfolios, immersive experiences, high-detail
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Create a flat, 2D interface with bold colors, no shadows/gradients, clean lines, simple geometric shapes, icon-heavy, typography-focused, minimal ornamentation. Use 4-6 solid, bright colors in a limited palette with high saturation.
- Key properties and techniques: `box-shadow: none`, `background: solid color`, `border-radius: 0-4px`, `color: solid (no gradients)`, `fill: solid`, `stroke: 1-2px`, `font: bold sans-serif`, `icons: simplified SVG`
- Implementation checklist: No shadows/gradients; 4-6 solid colors max; Clean lines consistent; Simple shapes used; Icon-heavy layout; High saturation colors; Fast loading verified
- Design-system variables: `--shadow: none`, `--color-palette: 4-6 solid`, `--border-radius: 2px`, `--gradient: none`, `--icons: simplified SVG`, `--animation: minimal 150-200ms`

## 377. Skeuomorphism
- Keywords and mood: Realistic, texture, depth, 3D appearance, real-world metaphors, shadows, gradients, tactile, detailed, material
- Origin and era: 2007-2012 iOS; implementation complexity high
- Primary colours: Rich realistic: wood, leather, metal colors, detailed gradients (8-12 stops), metallic effects
- Secondary colours: Realistic lighting gradients, shadow variations (`30-50%` darker), texture overlays, material colors
- Effects and animation: Realistic shadows (layers), depth (perspective), texture details (noise, grain), realistic animations (`300-500ms`)
- Best for: Legacy apps, gaming, immersive storytelling, premium products, luxury, realistic simulations, education
- Do not use for: Modern enterprise, critical accessibility, low-performance, web (use Flat/Modern)
- Light mode conditional (works only with careful tuning); dark mode conditional (works only with careful tuning)
- Performance: high cost; driven by animation and large images
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: not recommended on mobile
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a realistic, textured interface with 3D depth, real-world metaphors (leather, wood, metal), complex gradients (8-12 stops), realistic shadows, grain/texture overlays, tactile press animations. Perfect for premium/luxury products.
- Key properties and techniques: `background: complex gradient (8-12 stops)`, `box-shadow: realistic multi-layer`, `background-image: texture overlay (noise, grain)`, `filter: drop-shadow`, `transform: scale on press (300-500ms)`
- Implementation checklist: Realistic textures applied; Complex gradients 8-12 stops; Multi-layer shadows; Texture overlays present; Tactile animations smooth; Depth effect pronounced
- Design-system variables: `--gradient-stops: 8-12`, `--texture-overlay: noise+grain`, `--shadow-layers: 3+`, `--animation-duration: 300-500ms`, `--depth-effect: pronounced`, `--tactile: true`

## 378. Motion-Driven
- Keywords and mood: Animation-heavy, microinteractions, smooth transitions, scroll effects, parallax, entrance anim, page transitions
- Origin and era: 2020s Modern; implementation complexity high
- Primary colours: Bold colors emphasize movement, high contrast animated, dynamic gradients, accent action colors
- Secondary colours: Transitional states, success (Green `#22C55E`), error (Red `#EF4444`), neutral feedback
- Effects and animation: Scroll anim (Intersection Observer), hover (`300-400ms`), entrance, parallax (3-5 layers), page transitions
- Best for: Portfolio sites, storytelling platforms, interactive experiences, entertainment apps, creative, SaaS
- Do not use for: Data dashboards, critical accessibility, low-power devices, content-heavy, motion-sensitive
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Build an animation-heavy interface with scroll-triggered animations, microinteractions, parallax scrolling (3-5 layers), smooth transitions (300-400ms), entrance animations, page transitions. Use Intersection Observer for scroll effects, transform for performance, GPU acceleration.
- Key properties and techniques: `animation: @keyframes scroll-reveal`, `transform: translateY/X`, `Intersection Observer API`, `will-change: transform`, `scroll-behavior: smooth`, `animation-duration: 300-400ms`
- Implementation checklist: Scroll animations active; Parallax 3-5 layers; Entrance animations smooth; Page transitions fluid; GPU accelerated; Prefers-reduced-motion respected
- Design-system variables: `--animation-duration: 300-400ms`, `--parallax-layers: 5`, `--scroll-behavior: smooth`, `--gpu-accelerated: true`, `--entrance-animation: true`, `--page-transition: smooth`

## 379. Micro-interactions
- Keywords and mood: Small animations, gesture-based, tactile feedback, subtle animations, contextual interactions, responsive
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Subtle color shifts (`10-20%`), feedback: Green `#22C55E`, Red `#EF4444`, Amber `#F59E0B`
- Secondary colours: Accent feedback, neutral supporting, clear action indicators
- Effects and animation: Small hover (`50-100ms`), loading spinners, success/error state anim, gesture-triggered (swipe/pinch), haptic
- Best for: Mobile apps, touchscreen UIs, productivity tools, user-friendly, consumer apps, interactive components
- Do not use for: Desktop-only, critical performance, accessibility-first (alternatives needed)
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design with delightful micro-interactions: small 50-100ms animations, gesture-based responses, tactile feedback, loading spinners, success/error states, subtle hover effects, haptic feedback triggers for mobile. Focus on responsive, contextual interactions.
- Key properties and techniques: `animation: short 50-100ms`, `transition: hover states`, `@media (hover: hover) for desktop`, `:active for press`, `haptic-feedback CSS/API`, `loading animation smooth loop`
- Implementation checklist: Micro-animations `50-100ms`; Gesture-responsive; Tactile feedback visual/haptic; Loading spinners smooth; Success/error states clear; Hover effects subtle
- Design-system variables: `--micro-animation-duration: 50-100ms`, `--gesture-responsive: true`, `--haptic-feedback: true`, `--loading-animation: smooth`, `--state-feedback: success+error`

## 380. Inclusive Design
- Keywords and mood: Accessible, color-blind friendly, high contrast, haptic feedback, voice interaction, screen reader, enhanced contrast targets, universal
- Origin and era: Universal; implementation complexity low
- Primary colours: Measured contrast pairs targeting `7:1` for normal text, avoid red-green only, symbol-based indicators, high contrast primary
- Secondary colours: Supporting patterns (stripes, dots, hatch), symbols, combinations, clear non-color indicators
- Effects and animation: Haptic feedback (vibration), voice guidance, focus indicators (`4px`+ ring), motion options, alt content, semantic
- Best for: Public services, education, healthcare, finance, government, accessible consumer, inclusive
- Do not use for: None - accessibility universal
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design for universal accessibility: high contrast (7:1+), large text (16px+), keyboard-only navigation, screen reader optimization, enhanced accessibility criteria with complete-page verification, symbol-based color indicators (not color-only), haptic feedback, voice interaction support, reduced motion options.
- Key properties and techniques: `aria-* attributes complete`, `role attributes semantic`, `focus-visible: 3-4px ring`, `color-contrast: 7:1+`, `@media (prefers-reduced-motion)`, `alt text on all images`, `form labels properly associated`
- Implementation checklist: complete-page conformance tested against the chosen target; `7:1+` contrast all text; Keyboard accessible (Tab/Enter); Screen reader tested; Focus visible `3-4px`; No color-only indicators; Haptic fallback
- Design-system variables: `--contrast-ratio: 7:1`, `--font-size: 16px+`, `--keyboard-accessible: true`, `--sr-test-required: true`, `--wcag-target: enhanced`, `--color-symbols: true`, `--haptic: enabled`

## 381. Zero Interface
- Keywords and mood: Minimal visible UI, voice-first, gesture-based, AI-driven, invisible controls, predictive, context-aware, ambient
- Origin and era: 2020s AI-Era; implementation complexity low
- Primary colours: Neutral backgrounds: Soft white `#FAFAFA`, light grey `#F0F0F0`, warm off-white `#F5F1E8`
- Secondary colours: Subtle feedback: light green, light red, minimal UI elements, soft accents
- Effects and animation: Voice recognition UI, gesture detection, AI predictions (smooth reveal), progressive disclosure, smart suggestions
- Best for: Voice assistants, AI platforms, future-forward UX, smart home, contextual computing, ambient experiences
- Do not use for: Complex workflows, data-entry heavy, traditional systems, legacy support, explicit control
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Create a voice-first, gesture-based, AI-driven interface with minimal visible UI, progressive disclosure, voice recognition UI, gesture detection, AI predictions, smart suggestions, context-aware actions. Hide controls until needed.
- Key properties and techniques: `voice-commands: Web Speech API`, `gesture-detection: touch events`, `AI-predictions: hidden by default (reveal on hover)`, `progressive-disclosure: show on demand`, `minimal UI visible`
- Implementation checklist: Voice commands responsive; Gesture detection active; AI predictions hidden/revealed; Progressive disclosure working; Minimal visible UI; Smart suggestions contextual
- Design-system variables: `--voice-ui: enabled`, `--gesture-detection: active`, `--ai-predictions: smart`, `--progressive-disclosure: true`, `--visible-ui: minimal`, `--context-aware: true`

## 382. Soft UI Evolution
- Keywords and mood: Evolved soft UI, better contrast, modern aesthetics, subtle depth, accessibility-focused, improved shadows, hybrid
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Improved contrast pastels: Soft Blue `#87CEEB`, Soft Pink `#FFB6C1`, Soft Green `#90EE90`, better hierarchy
- Secondary colours: Better combinations, accessible secondary, supporting with improved contrast, modern accents
- Effects and animation: Improved shadows (softer than flat, clearer than neumorphism), modern (`200-300ms`), focus visible, measured contrast targets
- Best for: Modern enterprise apps, SaaS platforms, health/wellness, modern business tools, professional, hybrid
- Do not use for: Extreme minimalism, critical performance, systems without modern OS
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design evolved neumorphism with improved contrast (measured contrast targets), modern aesthetics, subtle depth, accessibility focus. Use soft shadows (softer than flat but clearer than pure neumorphism), better color hierarchy, improved focus states, modern 200-300ms animations.
- Key properties and techniques: `box-shadow: softer multi-layer (0 2px 4px)`, `background: improved contrast pastels`, `border-radius: 8-12px`, `animation: 200-300ms smooth`, `outline: 2-3px on focus`, `contrast: 4.5:1+`
- Implementation checklist: Contrast measured against the chosen project target; Soft shadows modern; Border-radius `8-12px`; Animations `200-300ms`; Focus states visible; Color hierarchy clear
- Design-system variables: `--shadow-soft: modern blend`, `--border-radius: 10px`, `--animation-duration: 200-300ms`, `--contrast-ratio: 4.5:1+`, `--color-hierarchy: improved`, `--wcag-target: project-defined`

## 383. Neubrutalism
- Keywords and mood: Bold borders, black outlines, primary colors, thick shadows, no gradients, flat colors, 45° shadows, playful, Gen Z
- Origin and era: 2020s Modern; implementation complexity low
- Primary colours: `#FFEB3B` (Yellow), `#FF5252` (Red), `#2196F3` (Blue), `#000000` (Black borders)
- Secondary colours: Limited accent colors, high contrast combinations, no gradients allowed
- Effects and animation: box-shadow: `4px 4px` 0 `#000`, border: `3px` solid `#000`, no gradients, sharp corners (`0px`), bold typography
- Best for: Gen Z brands, startups, creative agencies, Figma-style apps, Notion-style interfaces, tech blogs
- Do not use for: Luxury brands, finance, healthcare, conservative industries (too playful)
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a neubrutalist interface. Use: high contrast, hard black borders (3px+), bright pop colors, no blur, sharp or slightly rounded corners, bold typography, hard shadows (offset 4px 4px), raw aesthetic but functional.
- Key properties and techniques: `border: 3px solid black`, `box-shadow: 5px 5px 0px black`, `colors: #FFDB58 #FF6B6B #4ECDC4`, `font-weight: 700`, `no gradients`
- Implementation checklist: Hard borders (`2-4px`); Hard offset shadows; High saturation colors; Bold typography; No blurs/gradients; Distinctive 'ugly-cute' look
- Design-system variables: `--border-width: 3px`, `--shadow-offset: 4px`, `--shadow-color: #000`, `--colors: high saturation`, `--font: bold sans`

## 384. Bento Box Grid
- Keywords and mood: Modular cards, asymmetric grid, varied sizes, Apple-style, dashboard tiles, negative space, clean hierarchy, cards
- Also known as: Bento Grids, Masonry Grid
- Origin and era: 2020s Apple; implementation complexity low
- Primary colours: Neutral base + brand accent, `#FFFFFF`, `#F5F5F5`, brand primary
- Secondary colours: Subtle gradients, shadow variations, accent highlights for interactive cards
- Effects and animation: grid-template with varied spans, rounded-xl (`16px`), subtle shadows, hover scale (1.02), smooth transitions
- Best for: Dashboards, product pages, portfolios, Apple-style marketing, feature showcases, SaaS
- Do not use for: Dense data tables, text-heavy content, real-time monitoring
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a Bento Box grid layout. Use: modular cards with varied sizes (1x1, 2x1, 2x2), Apple-style aesthetic, rounded corners (16-24px), soft shadows, clean hierarchy, asymmetric grid, neutral backgrounds (#F5F5F7), hover effects.
- Key properties and techniques: `display: grid`, `grid-template-columns: repeat(4, 1fr)`, `grid-auto-rows: 200px`, `gap: 16px`, `border-radius: 24px`, `background: #FFFFFF`, `box-shadow: 0 4px 6px rgba(0,0,0,0.05)`
- Implementation checklist: Grid responsive (4→2→1 cols); Card spans varied; Rounded corners consistent; Shadows subtle; Content fits cards; Hover scale (1.02)
- Design-system variables: `--grid-gap: 16px`, `--card-radius: 24px`, `--card-bg: #FFFFFF`, `--page-bg: #F5F5F7`, `--shadow: 0 4px 6px rgba(0,0,0,0.05)`, `--hover-scale: 1.02`

## 385. Y2K Aesthetic
- Keywords and mood: Neon pink, chrome, metallic, bubblegum, iridescent, glossy, retro-futurism, 2000s, futuristic nostalgia
- Origin and era: Y2K 2000s; implementation complexity medium
- Primary colours: `#FF69B4` (Hot Pink), `#00FFFF` (Cyan), `#C0C0C0` (Silver), `#9400D3` (Purple)
- Secondary colours: Metallic gradients, glossy overlays, iridescent effects, chrome textures
- Effects and animation: linear-gradient metallic, glossy buttons, 3D chrome effects, glow animations, bubble shapes
- Best for: Fashion brands, music platforms, Gen Z brands, nostalgia marketing, entertainment, youth-focused
- Do not use for: B2B enterprise, healthcare, finance, conservative industries, elderly users
- Light mode supported; dark mode conditional (works only with careful tuning)
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a Y2K aesthetic interface. Use: neon pink/cyan colors, chrome/metallic textures, bubblegum gradients, glossy buttons, iridescent effects, 2000s futurism, star/sparkle decorations, bubble shapes, tech-optimistic vibe.
- Key properties and techniques: `background: linear-gradient(135deg, #FF69B4, #00FFFF)`, `filter: drop-shadow for glow`, `border-radius: 50% for bubbles`, `metallic gradients (silver/chrome)`, `text-shadow: neon glow`, `::before for sparkles`
- Implementation checklist: Neon colors balanced; Chrome effects visible; Glossy buttons styled; Bubble shapes decorative; Sparkle animations; Retro fonts loaded
- Design-system variables: `--neon-pink: #FF69B4`, `--neon-cyan: #00FFFF`, `--chrome-silver: #C0C0C0`, `--glossy-gradient: linear-gradient(180deg, white 0%, transparent 50%)`, `--glow-blur: 10px`

## 386. Cyberpunk UI
- Keywords and mood: Neon, dark mode, terminal, HUD, sci-fi, glitch, dystopian, futuristic, matrix, tech noir
- Origin and era: 2020s Cyberpunk; implementation complexity medium
- Primary colours: `#00FF00` (Matrix Green), `#FF00FF` (Magenta), `#00FFFF` (Cyan), `#0D0D0D` (Dark)
- Secondary colours: Neon gradients, scanline overlays, glitch colors, terminal green accents
- Effects and animation: Neon glow (text-shadow), glitch animations (skew/offset), scanlines (::before overlay), terminal fonts
- Best for: Gaming platforms, tech products, crypto apps, sci-fi applications, developer tools, entertainment
- Do not use for: Corporate enterprise, healthcare, family apps, conservative brands, elderly users
- Light mode not recommended; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a cyberpunk interface. Use: neon colors on dark (#0D0D0D), terminal/HUD aesthetic, glitch effects, scanlines overlay, matrix green accents, monospace fonts, angular shapes, dystopian tech feel.
- Key properties and techniques: `background: #0D0D0D`, `color: #00FF00 or #FF00FF`, `font-family: monospace`, `text-shadow: 0 0 10px neon`, `animation: glitch (transform skew)`, `::before scanlines (repeating-linear-gradient)`
- Implementation checklist: Dark background only; Neon accents visible; Glitch effect subtle; Scanlines optional; Monospace font; Terminal aesthetic
- Design-system variables: `--bg-dark: #0D0D0D`, `--neon-green: #00FF00`, `--neon-magenta: #FF00FF`, `--neon-cyan: #00FFFF`, `--scanline-opacity: 0.1`, `--glitch-duration: 0.3s`

## 387. Organic Biophilic
- Keywords and mood: Nature, organic shapes, green, sustainable, rounded, flowing, wellness, earthy, natural textures
- Origin and era: 2020s Sustainable; implementation complexity low
- Primary colours: `#228B22` (Forest Green), `#8B4513` (Earth Brown), `#87CEEB` (Sky Blue), `#F5F5DC` (Beige)
- Secondary colours: Natural gradients, earth tones, sky blues, organic textures, wood/stone colors
- Effects and animation: Rounded corners (`16-24px`), organic curves (border-radius variations), natural shadows, flowing SVG shapes
- Best for: Wellness apps, sustainability brands, eco products, health apps, meditation, organic food brands
- Do not use for: Tech-focused products, gaming, industrial, urban brands
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a biophilic organic interface. Use: nature-inspired colors (greens, browns), organic curved shapes, rounded corners (16-24px), natural textures (wood, stone), flowing SVG elements, wellness aesthetic, earthy palette.
- Key properties and techniques: `border-radius: 16-24px (varied)`, `background: earth tones`, `SVG organic shapes (blob)`, `box-shadow: natural soft`, `color: #228B22 #8B4513 #87CEEB`, `texture overlays (subtle)`
- Implementation checklist: Earth tones dominant; Organic curves present; Natural textures subtle; Green accents; Rounded everywhere; Calming feel
- Design-system variables: `--forest-green: #228B22`, `--earth-brown: #8B4513`, `--sky-blue: #87CEEB`, `--cream-bg: #F5F5DC`, `--organic-radius: 24px`, `--shadow-soft: 0 8px 32px rgba(0,0,0,0.08)`

## 388. AI-Native UI
- Keywords and mood: Chatbot, conversational, voice, assistant, agentic, ambient, minimal chrome, streaming text, AI interactions
- Origin and era: 2020s AI-Era; implementation complexity low
- Primary colours: Neutral + single accent, `#6366F1` (AI Purple), `#10B981` (Success), `#F5F5F5` (Background)
- Secondary colours: Status indicators, streaming highlights, context card colors, subtle accent variations
- Effects and animation: Typing indicators (3-dot pulse), streaming text animations, pulse animations, context cards, smooth reveals
- Best for: AI products, chatbots, voice assistants, copilots, AI-powered tools, conversational interfaces
- Do not use for: Traditional forms, data-heavy dashboards, print-first content
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design an AI-native interface. Use: minimal chrome, conversational layout, streaming text area, typing indicators (3-dot pulse), context cards, subtle AI accent color (#6366F1), clean input field, response bubbles.
- Key properties and techniques: `chat bubble layout (flex-direction: column)`, `typing animation (3 dots pulse)`, `streaming text (overflow: hidden + animation)`, `input: sticky bottom`, `context cards (border-left accent)`, `minimal borders`
- Implementation checklist: Chat layout responsive; Typing indicator smooth; Input always visible; Context cards styled; AI responses distinct; User messages aligned right
- Design-system variables: `--ai-accent: #6366F1`, `--user-bubble-bg: #E0E7FF`, `--ai-bubble-bg: #F9FAFB`, `--input-height: 48px`, `--typing-dot-size: 8px`, `--message-gap: 16px`

## 389. Memphis Design
- Keywords and mood: 80s, geometric, playful, postmodern, shapes, patterns, squiggles, triangles, neon, abstract, bold
- Origin and era: 1980s Postmodern; implementation complexity medium
- Primary colours: `#FF71CE` (Hot Pink), `#FFCE5C` (Yellow), `#86CCCA` (Teal), `#6A7BB4` (Blue Purple)
- Secondary colours: Complementary geometric colors, pattern fills, contrasting accent shapes
- Effects and animation: transform: rotate(), clip-path: polygon(), mix-blend-mode, repeating patterns, bold shapes
- Best for: Creative agencies, music sites, youth brands, event promotion, artistic portfolios, entertainment
- Do not use for: Corporate finance, healthcare, legal, elderly users, conservative brands
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a Memphis style interface. Use: bold geometric shapes (triangles, squiggles, circles), bright clashing colors, 80s postmodern aesthetic, playful patterns, dotted textures, asymmetric layouts, decorative elements.
- Key properties and techniques: `clip-path: polygon() for shapes`, `background: repeating patterns`, `transform: rotate() for tilted elements`, `mix-blend-mode for overlays`, `border: dashed/dotted patterns`, `bold sans-serif`
- Implementation checklist: Geometric shapes visible; Colors bold/clashing; Patterns present; Layout asymmetric; Playful decorations; `80s` vibe achieved
- Design-system variables: `--memphis-pink: #FF71CE`, `--memphis-yellow: #FFCE5C`, `--memphis-teal: #86CCCA`, `--memphis-purple: #6A7BB4`, `--pattern-size: 20px`, `--shape-rotation: 15deg`

## 390. Vaporwave
- Keywords and mood: Synthwave, retro-futuristic, 80s-90s, neon, glitch, nostalgic, sunset gradient, dreamy, aesthetic
- Origin and era: 1980s-90s Retro; implementation complexity medium
- Primary colours: `#FF71CE` (Pink), `#01CDFE` (Cyan), `#05FFA1` (Mint), `#B967FF` (Purple)
- Secondary colours: Sunset gradients, glitch overlays, VHS effects, neon accents, pastel variations
- Effects and animation: text-shadow glow, linear-gradient, filter: hue-rotate(), glitch animations, retro scan lines
- Best for: Music platforms, gaming, creative portfolios, tech startups, entertainment, artistic projects
- Do not use for: Business apps, e-commerce, education, healthcare, enterprise software
- Light mode supported; dark mode supported; default to dark presentation
- Performance: moderate cost; driven by animation and blur
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a vaporwave aesthetic interface. Use: sunset gradients (pink/cyan/purple), 80s-90s nostalgia, glitch effects, Greek statue imagery, palm trees, grid patterns, neon glow, retro-futuristic feel, dreamy atmosphere.
- Key properties and techniques: `background: linear-gradient(180deg, #FF71CE, #01CDFE, #B967FF)`, `filter: hue-rotate()`, `text-shadow: neon glow`, `retro grid (perspective + linear-gradient)`, `VHS scanlines`
- Implementation checklist: Sunset gradient present; Neon glow applied; Retro grid visible; Glitch effects subtle; Dreamy atmosphere; `80s`-90s aesthetic
- Design-system variables: `--vapor-pink: #FF71CE`, `--vapor-cyan: #01CDFE`, `--vapor-mint: #05FFA1`, `--vapor-purple: #B967FF`, `--grid-color: rgba(255,255,255,0.1)`, `--glow-intensity: 15px`
- Relationship: a specialised variant of Retro-Futurism; start from the parent style's rules and apply these refinements

## 391. Dimensional Layering
- Keywords and mood: Depth, overlapping, z-index, layers, 3D, shadows, elevation, floating, cards, spatial hierarchy
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Neutral base (`#FFFFFF`, `#F5F5F5`, `#E0E0E0`) + brand accent for elevated elements
- Secondary colours: Shadow variations (sm/md/lg/xl), elevation colors, highlight colors for top layers
- Effects and animation: z-index stacking, box-shadow elevation (4 levels), transform: translateZ(), backdrop-filter, parallax
- Best for: Dashboards, card layouts, modals, navigation, product showcases, SaaS interfaces
- Do not use for: Print-style layouts, simple blogs, low-end devices, flat design requirements
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design with dimensional layering. Use: z-index depth (multiple layers), overlapping cards, elevation shadows (4 levels), floating elements, parallax depth, backdrop blur for hierarchy, spatial UI feel.
- Key properties and techniques: `z-index: 1-4 levels`, `box-shadow: elevation scale (sm/md/lg/xl)`, `transform: translateZ()`, `backdrop-filter: blur()`, `position: relative for stacking`, `parallax on scroll`
- Implementation checklist: Layers clearly defined; Shadows show depth; Overlaps intentional; Hierarchy clear; Performance optimized; Mobile depth maintained
- Design-system variables: `--elevation-1: 0 1px 3px rgba(0,0,0,0.1)`, `--elevation-2: 0 4px 6px rgba(0,0,0,0.1)`, `--elevation-3: 0 10px 20px rgba(0,0,0,0.1)`, `--elevation-4: 0 20px 40px rgba(0,0,0,0.15)`, `--blur-amount: 8px`

## 392. Exaggerated Minimalism
- Keywords and mood: Bold minimalism, oversized typography, high contrast, negative space, loud minimal, statement design
- Origin and era: 2020s Modern; implementation complexity low
- Primary colours: `#000000` (Black), `#FFFFFF` (White), single vibrant accent only
- Secondary colours: Minimal - single accent color, no secondary colors, extreme restraint
- Effects and animation: font-size: clamp(`3rem 10vw 12rem`), font-weight: 900, letter-spacing: `-0.05em`, massive whitespace
- Best for: Fashion, architecture, portfolios, agency landing pages, luxury brands, editorial
- Do not use for: E-commerce catalogs, dashboards, forms, data-heavy, elderly users, complex apps
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design with exaggerated minimalism. Use: oversized typography (clamp 3rem-12rem), extreme negative space, black/white primary, single accent color only, bold statements, minimal elements, dramatic contrast.
- Key properties and techniques: `font-size: clamp(3rem, 10vw, 12rem)`, `font-weight: 900`, `letter-spacing: -0.05em`, `color: #000 or #FFF`, `padding: 8rem+`, `single accent`, `no decorations`
- Implementation checklist: Typography oversized; White space extreme; Black/white dominant; Single accent only; Elements minimal; Statement clear
- Design-system variables: `--type-giant: clamp(3rem, 10vw, 12rem)`, `--type-weight: 900`, `--spacing-huge: 8rem`, `--color-primary: #000000`, `--color-bg: #FFFFFF`, `--accent: single color only`

## 393. Kinetic Typography
- Keywords and mood: Motion text, animated type, moving letters, dynamic, typing effect, morphing, scroll-triggered text
- Origin and era: 2020s Modern; implementation complexity high
- Primary colours: Flexible - high contrast recommended, bold colors for emphasis, animation-friendly palette
- Secondary colours: Accent colors for emphasis, transition colors, gradient text fills
- Effects and animation: @keyframes text animation, typing effect, background-clip: text, GSAP ScrollTrigger, split text
- Best for: Hero sections, marketing sites, video platforms, storytelling, creative portfolios, landing pages
- Do not use for: Long-form content, accessibility-critical, data interfaces, forms, elderly users
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Very High
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Design with kinetic typography. Use: animated text, scroll-triggered reveals, typing effects, letter-by-letter animations, morphing text, gradient text fills, oversized hero text, text as the main visual element.
- Key properties and techniques: `@keyframes for text animation`, `background-clip: text`, `GSAP SplitText`, `typing effect (steps())`, `transform on letters`, `scroll-triggered (Intersection Observer)`, `variable fonts for morphing`
- Implementation checklist: Text animations smooth; Prefers-reduced-motion respected; Fallback for no-JS; Mobile performance ok; Typing effect timed; Scroll triggers work
- Design-system variables: `--text-animation-duration: 1s`, `--letter-delay: 0.05s`, `--typing-speed: 100ms`, `--gradient-text: linear-gradient(90deg, #color1, #color2)`, `--morph-duration: 0.5s`

## 394. Parallax Storytelling
- Keywords and mood: Scroll-driven, narrative, layered scrolling, immersive, progressive disclosure, cinematic, scroll-triggered
- Also known as: Parallax
- Origin and era: 2020s Modern; implementation complexity high
- Primary colours: Story-dependent, often gradients and natural colors, section-specific palettes
- Secondary colours: Section transition colors, depth layer colors, narrative mood colors
- Effects and animation: transform: translateY(scroll), position: fixed/sticky, perspective: `1px`, scroll-triggered animations
- Best for: Brand storytelling, product launches, case studies, portfolios, annual reports, marketing campaigns
- Do not use for: E-commerce, dashboards, mobile-first, SEO-critical, accessibility-required
- Light mode supported; dark mode supported
- Performance: high cost; driven by animation and large images
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: not recommended on mobile
- Conversion focus: High
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Design a parallax storytelling page. Use: scroll-driven narrative, layered backgrounds (3-5 layers), fixed/sticky sections, cinematic transitions, progressive disclosure, full-screen chapters, depth perception.
- Key properties and techniques: `position: fixed/sticky`, `transform: translateY(calc())`, `perspective: 1px`, `z-index layering`, `scroll-snap-type`, `Intersection Observer for triggers`, `will-change: transform`
- Implementation checklist: Layers parallax smoothly; Story flows naturally; Mobile alternative provided; Performance optimized; Skip option available; Reduced motion fallback
- Design-system variables: `--parallax-speed-bg: 0.3`, `--parallax-speed-mid: 0.6`, `--parallax-speed-fg: 1`, `--section-height: 100vh`, `--transition-duration: 600ms`, `--perspective: 1px`

## 395. Swiss Modernism 2.0
- Keywords and mood: Grid system, Helvetica, modular, asymmetric, international style, rational, clean, mathematical spacing
- Also known as: Swiss Modernism
- Origin and era: 1950s Swiss + 2020s; implementation complexity low
- Primary colours: `#000000`, `#FFFFFF`, `#F5F5F5`, single vibrant accent only
- Secondary colours: Minimal secondary, accent for emphasis only, no gradients
- Effects and animation: display: grid, grid-template-columns: repeat(12 1fr), gap: `1rem`, mathematical ratios, clear hierarchy
- Best for: Corporate sites, architecture, editorial, SaaS, museums, professional services, documentation
- Do not use for: Playful brands, children's sites, entertainment, gaming, emotional storytelling
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design with Swiss Modernism 2.0. Use: strict grid system (12 columns), Helvetica/Inter fonts, mathematical spacing, asymmetric balance, high contrast, minimal decoration, clean hierarchy, single accent color.
- Key properties and techniques: `display: grid`, `grid-template-columns: repeat(12, 1fr)`, `gap: 1rem (8px base unit)`, `font-family: Inter/Helvetica`, `font-weight: 400-700`, `color: #000/#FFF`, `single accent`
- Implementation checklist: 12-column grid strict; Spacing mathematical; Typography hierarchy clear; Single accent only; No decorations; High contrast verified
- Design-system variables: `--grid-columns: 12`, `--grid-gap: 1rem`, `--base-unit: 8px`, `--font-primary: Inter`, `--color-text: #000000`, `--color-bg: #FFFFFF`, `--accent: single vibrant`
- Relationship: a specialised variant of Minimalism & Swiss Style; start from the parent style's rules and apply these refinements

## 396. HUD / Sci-Fi FUI
- Keywords and mood: Futuristic, technical, wireframe, neon, data, transparency, iron man, sci-fi, interface
- Also known as: HUD, FUI, Sci-Fi HUD, HUD/Sci-Fi FUI, Holographic / HUD, Holographic/HUD
- Origin and era: 2010s Sci-Fi; implementation complexity high
- Primary colours: Neon Cyan `#00FFFF`, Holographic Blue `#0080FF`, Alert Red `#FF0000`
- Secondary colours: Transparent Black, Grid Lines `#333333`
- Effects and animation: Glow effects, scanning animations, ticker text, blinking markers, fine line drawing
- Best for: Sci-fi games, space tech, cybersecurity, movie props, immersive dashboards
- Do not use for: Standard corporate, reading heavy content, accessible public services
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Low
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Design a futuristic HUD (Heads Up Display) or FUI. Use: thin lines (1px), neon cyan/blue on black, technical markers, decorative brackets, data visualization, monospaced tech fonts, glowing elements, transparency.
- Key properties and techniques: `border: 1px solid rgba(0,255,255,0.5)`, `color: #00FFFF`, `background: transparent or rgba(0,0,0,0.8)`, `font-family: monospace`, `text-shadow: 0 0 5px cyan`
- Implementation checklist: Fine lines `1px`; Neon glow text/borders; Monospaced font; Dark/Transparent BG; Decorative tech markers; Holographic feel
- Design-system variables: `--hud-color: #00FFFF`, `--bg-color: rgba(0,10,20,0.9)`, `--line-width: 1px`, `--glow: 0 0 5px`, `--font: monospace`

## 397. Pixel Art
- Keywords and mood: Retro, 8-bit, 16-bit, gaming, blocky, nostalgic, pixelated, arcade
- Origin and era: 1980s Arcade; implementation complexity medium
- Primary colours: Primary colors (NES Palette), brights, limited palette
- Secondary colours: Black outlines, shading via dithering or block colors
- Effects and animation: Frame-by-frame sprite animation, blinking cursor, instant transitions, marquee text
- Best for: Indie games, retro tools, creative portfolios, nostalgia marketing, Web3/NFT
- Do not use for: Professional corporate, modern SaaS, high-res photography sites
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a pixel art inspired interface. Use: pixelated fonts, 8-bit or 16-bit aesthetic, sharp edges (image-rendering: pixelated), limited color palette, blocky UI elements, retro gaming feel.
- Key properties and techniques: `font-family: 'Press Start 2P'`, `image-rendering: pixelated`, `box-shadow: 4px 0 0 #000 (pixel border)`, `no anti-aliasing`
- Implementation checklist: Pixelated fonts loaded; Images sharp (no blur); CSS box-shadow for pixel borders; Retro palette; Blocky layout
- Design-system variables: `--pixel-size: 4px`, `--font: pixel font`, `--border-style: pixel-shadow`, `--anti-alias: none`

## 398. Bento Grids (Legacy)
- Keywords and mood: Apple-style, modular, cards, organized, clean, hierarchy, grid, rounded, soft
- Origin and era: 2020s Apple/Linear; implementation complexity low
- Primary colours: Off-white `#F5F5F7`, Clean White `#FFFFFF`, Text `#1D1D1F`
- Secondary colours: Subtle accents, soft shadows, blurred backdrops
- Effects and animation: Hover scale (1.02), soft shadow expansion, smooth layout shifts, content reveal
- Best for: Product features, dashboards, personal sites, marketing summaries, galleries
- Do not use for: Long-form reading, data tables, complex forms
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a Bento Grid layout. Use: modular grid system, rounded corners (16-24px), different card sizes (1x1, 2x1, 2x2), card-based hierarchy, soft backgrounds (#F5F5F7), subtle borders, content-first, Apple-style aesthetic.
- Key properties and techniques: `display: grid`, `grid-template-columns: repeat(auto-fit, minmax(...))`, `gap: 1rem`, `border-radius: 20px`, `background: #FFF`, `box-shadow: subtle`
- Implementation checklist: Grid layout (CSS Grid); Rounded corners `16-24px`; Varied card spans; Content fits card size; Responsive re-flow; Apple-like aesthetic
- Design-system variables: `--grid-gap: 20px`, `--card-radius: 24px`, `--card-bg: #FFFFFF`, `--page-bg: #F5F5F7`, `--shadow: soft`
- Status: legacy; prefer the Bento Box Grid style for new work

## 399. Spatial UI (VisionOS)
- Keywords and mood: Glass, depth, immersion, spatial, translucent, gaze, gesture, apple, vision-pro
- Also known as: Spatial UI
- Origin and era: 2024 Spatial Era; implementation complexity high
- Primary colours: Frosted Glass `#FFFFFF` (`15-30%` opacity), System White
- Secondary colours: Vibrant system colors for active states, deep shadows for depth
- Effects and animation: Parallax depth, dynamic lighting response, gaze-hover effects, smooth scale on focus
- Best for: Spatial computing apps, VR/AR interfaces, immersive media, futuristic dashboards
- Do not use for: Text-heavy documents, high-contrast requirements, non-3D capable devices
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a VisionOS-style spatial interface. Use: frosted glass panels, depth layers, translucent backgrounds (15-30% opacity), vibrant colors for active states, gaze-hover effects, floating windows, immersive feel.
- Key properties and techniques: `backdrop-filter: blur(40px) saturate(180%)`, `background: rgba(255,255,255,0.2)`, `border-radius: 24px`, `box-shadow: 0 8px 32px rgba(0,0,0,0.1)`, `transform: scale on focus`, `depth via shadows`
- Implementation checklist: Glass effect visible; Depth layers clear; Hover states defined; Colors vibrant on active; Floating feel achieved; Contrast maintained
- Design-system variables: `--glass-bg: rgba(255,255,255,0.2)`, `--glass-blur: 40px`, `--glass-saturate: 180%`, `--window-radius: 24px`, `--depth-shadow: 0 8px 32px rgba(0,0,0,0.1)`, `--focus-scale: 1.02`

## 400. E-Ink / Paper
- Keywords and mood: Paper-like, matte, high contrast, texture, reading, calm, slow tech, monochrome
- Also known as: E-Ink Paper, E-Ink/Paper
- Origin and era: 2020s Digital Well-being; implementation complexity low
- Primary colours: Off-White `#FDFBF7`, Paper White `#F5F5F5`, Ink Black `#1A1A1A`
- Secondary colours: Pencil Grey `#4A4A4A`, Highlighter Yellow `#FFFF00` (accent)
- Effects and animation: No motion blur, distinct page turns, grain/noise texture, sharp transitions (no fade)
- Best for: Reading apps, digital newspapers, minimal journals, distraction-free writing, slow-living brands
- Do not use for: Gaming, video platforms, high-energy marketing, dark mode dependent apps
- Light mode supported; dark mode not recommended
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design an e-ink/paper style interface. Use: high contrast black on off-white, paper texture, no animations (instant transitions), reading-focused, minimal UI chrome, distraction-free, calm aesthetic, monochrome.
- Key properties and techniques: `background: #FDFBF7 (paper white)`, `color: #1A1A1A`, `transition: none`, `font-family: serif for reading`, `no gradients`, `border: 1px solid #E0E0E0`, `texture overlay (noise)`
- Implementation checklist: Paper background color; High contrast text; No animations; Reading optimized; Distraction-free; Print-friendly
- Design-system variables: `--paper-bg: #FDFBF7`, `--ink-color: #1A1A1A`, `--pencil-grey: #4A4A4A`, `--border-color: #E0E0E0`, `--font-reading: Georgia`, `--transition: none`

## 401. Gen Z Chaos / Maximalism
- Keywords and mood: Chaos, clutter, stickers, raw, collage, mixed media, loud, internet culture, ironic
- Also known as: Gen Z Chaos
- Origin and era: 2023+ Internet Core; implementation complexity high
- Primary colours: Clashing Brights: `#FF00FF`, `#00FF00`, `#FFFF00`, `#0000FF`
- Secondary colours: Gradients, rainbow, glitch, noise, heavily saturated mix
- Effects and animation: Marquee scrolls, jitter, sticker layering, GIF overload, random placement, drag-and-drop
- Best for: Gen Z lifestyle brands, music artists, creative portfolios, viral marketing, fashion
- Do not use for: Corporate, government, healthcare, banking, serious tools
- Light mode supported; dark mode supported
- Performance: high cost; driven by animation and large images
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: High (Viral)
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a Gen Z chaos maximalist interface. Use: clashing bright colors, sticker overlays, collage aesthetic, raw/unpolished feel, mixed media, ironic elements, loud typography, GIF-heavy, internet culture references.
- Key properties and techniques: `mix-blend-mode: multiply/screen`, `transform: rotate(random)`, `animation: jitter`, `marquee text`, `position: absolute for scattered elements`, `filter: saturate(150%)`, `z-index chaos`
- Implementation checklist: Colors clash intentionally; Stickers/overlays present; Layout chaotic but usable; GIFs optimized; Mobile scrollable; Performance acceptable
- Design-system variables: `--chaos-pink: #FF00FF`, `--chaos-green: #00FF00`, `--chaos-yellow: #FFFF00`, `--chaos-blue: #0000FF`, `--jitter-amount: 5deg`, `--saturate: 150%`

## 402. Biomimetic / Organic 2.0
- Keywords and mood: Nature-inspired, cellular, fluid, breathing, generative, algorithms, life-like
- Also known as: Biomimetic/Organic 2.0
- Origin and era: 2024+ Generative; implementation complexity high
- Primary colours: Cellular Pink `#FF9999`, Chlorophyll Green `#00FF41`, Bioluminescent Blue
- Secondary colours: Deep Ocean `#001E3C`, Coral `#FF7F50`, Organic gradients
- Effects and animation: Breathing animations, fluid morphing, generative growth, physics-based movement
- Best for: Sustainability tech, biotech, advanced health, meditation, generative art platforms
- Do not use for: Standard SaaS, data grids, strict corporate, accounting
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a biomimetic organic interface. Use: cellular/fluid shapes, breathing animations, generative patterns, bioluminescent colors, physics-based movement, nature algorithms, life-like elements, flowing gradients.
- Key properties and techniques: `SVG morphing (SMIL or GSAP)`, `canvas for generative`, `animation: breathing (scale pulse)`, `filter: blur for organic`, `clip-path for cellular`, `WebGL for advanced`, `physics libraries`
- Implementation checklist: Organic shapes present; Animations feel alive; Generative elements; Performance monitored; Mobile fallback; Accessibility alt content
- Design-system variables: `--cellular-pink: #FF9999`, `--chlorophyll: #00FF41`, `--bioluminescent: #00FFFF`, `--breathing-duration: 4s`, `--morph-ease: cubic-bezier(0.4, 0, 0.2, 1)`, `--organic-blur: 20px`

## 403. Anti-Polish / Raw Aesthetic
- Keywords and mood: Hand-drawn, collage, scanned textures, unfinished, imperfect, authentic, human, sketch, raw marks, creative process
- Also known as: Anti-Polish Raw
- Origin and era: 2025+ Anti-Digital; implementation complexity low
- Primary colours: Paper White `#FAFAF8`, Pencil Grey `#4A4A4A`, Marker Black `#1A1A1A`, Kraft Brown `#C4A77D`
- Secondary colours: Watercolor washes, pencil shading, ink splatters, tape textures, aged paper tones
- Effects and animation: No smooth transitions, hand-drawn animations, paper texture overlays, jitter effects, sketch reveal
- Best for: Creative portfolios, artist sites, indie brands, handmade products, authentic storytelling, editorial
- Do not use for: Corporate enterprise, fintech, healthcare, government, polished SaaS
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design with anti-polish raw aesthetic. Use: hand-drawn elements, scanned textures, unfinished look, paper/pencil textures, collage style, authentic imperfection, sketch marks, tape/sticker overlays, human touch.
- Key properties and techniques: `background: url(paper-texture.png)`, `filter: grayscale() contrast()`, `border: hand-drawn SVG`, `transform: rotate(small random)`, `no smooth transitions`, `sketch-style fonts`, `opacity variations`
- Implementation checklist: Textures loaded; Hand-drawn elements present; Imperfections intentional; Authentic feel achieved; Performance ok with textures; Accessibility maintained
- Design-system variables: `--paper-bg: #FAFAF8`, `--pencil-color: #4A4A4A`, `--marker-black: #1A1A1A`, `--kraft-brown: #C4A77D`, `--sketch-rotation: random(-3deg, 3deg)`, `--texture-opacity: 0.3`

## 404. Tactile Digital / Deformable UI
- Keywords and mood: Jelly buttons, chrome, clay, squishy, deformable, bouncy, physical, tactile feedback, press response
- Origin and era: 2025+ Tactile Era; implementation complexity medium
- Primary colours: Gradient metallics, Chrome Silver `#C0C0C0`, Jelly Pink `#FF9ECD`, Soft Blue `#87CEEB`
- Secondary colours: Glossy highlights, shadow depth, reflection effects, material-specific colors
- Effects and animation: Press deformation (scale + squish), bounce-back (cubic-bezier), material response, haptic-like feedback, spring physics
- Best for: Modern mobile apps, playful brands, entertainment, gaming UI, consumer products, interactive demos
- Do not use for: Enterprise software, data dashboards, accessibility-critical, professional tools
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Very High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a tactile deformable interface. Use: jelly/squishy buttons, press deformation effect, bounce-back animations, chrome/clay materials, spring physics, haptic-like feedback, material response, 3D depth on interaction.
- Key properties and techniques: `transform: scale(0.95) on active`, `animation: bounce (cubic-bezier(0.34, 1.56, 0.64, 1))`, `box-shadow: inset for press`, `filter: brightness on press`, `spring physics (react-spring/framer-motion)`
- Implementation checklist: Press effect visible; Bounce-back smooth; Material feels tactile; Spring physics tuned; Mobile touch responsive; Reduced motion option
- Design-system variables: `--press-scale: 0.95`, `--bounce-duration: 400ms`, `--spring-stiffness: 300`, `--spring-damping: 20`, `--material-glossy: linear-gradient(135deg, white 0%, transparent 60%)`, `--depth-shadow: 0 10px 30px rgba(0,0,0,0.2)`

## 405. Nature Distilled
- Keywords and mood: Muted earthy, skin tones, wood, soil, sand, terracotta, warmth, organic materials, handmade warmth
- Origin and era: 2025+ Handmade Warmth; implementation complexity low
- Primary colours: Terracotta `#C67B5C`, Sand Beige `#D4C4A8`, Warm Clay `#B5651D`, Soft Cream `#F5F0E1`
- Secondary colours: Earth Brown `#8B4513`, Olive Green `#6B7B3C`, Warm Stone `#9C8B7A`, muted gradients
- Effects and animation: Subtle parallax, natural easing (ease-out), texture overlays, grain effects, soft shadows
- Best for: Wellness brands, sustainable products, artisan goods, organic food, spa/beauty, home decor
- Do not use for: Tech startups, gaming, nightlife, corporate finance, high-energy brands
- Light mode supported; dark mode conditional (works only with careful tuning)
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design with nature distilled aesthetic. Use: muted earthy colors (terracotta, sand, olive), organic materials feel, warm tones, handmade warmth, natural textures, artisan quality, sustainable vibe, soft gradients.
- Key properties and techniques: `background: warm earth tones`, `color: #C67B5C #D4C4A8 #6B7B3C`, `border-radius: organic (varied)`, `box-shadow: soft natural`, `texture overlays (grain)`, `font: humanist sans-serif`
- Implementation checklist: Earth tones dominant; Warm feel achieved; Textures subtle; Handmade quality; Sustainable messaging; Calming aesthetic
- Design-system variables: `--terracotta: #C67B5C`, `--sand-beige: #D4C4A8`, `--warm-clay: #B5651D`, `--soft-cream: #F5F0E1`, `--olive-green: #6B7B3C`, `--grain-opacity: 0.1`

## 406. Interactive Cursor Design
- Keywords and mood: Custom cursor, cursor as tool, hover effects, cursor feedback, pointer transformation, cursor trail, magnetic cursor
- Origin and era: 2025+ Interactive; implementation complexity medium
- Primary colours: Brand-dependent, cursor accent color, high contrast for visibility
- Secondary colours: Trail colors, hover state colors, magnetic zone indicators, feedback colors
- Effects and animation: Cursor scale on hover, magnetic pull to elements, cursor morphing, trail effects, blend mode cursors, click feedback
- Best for: Creative portfolios, interactive experiences, agency sites, product showcases, gaming, entertainment
- Do not use for: Mobile-first (no cursor), accessibility-critical, data-heavy dashboards, forms
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: not recommended on mobile
- Conversion focus: High
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Design with interactive cursor effects. Use: custom cursor, cursor morphing on hover, magnetic cursor pull, cursor trails, blend mode cursors, click feedback animations, cursor as interaction tool, pointer transformation.
- Key properties and techniques: `cursor: none (custom)`, `position: fixed for cursor element`, `mix-blend-mode: difference`, `transform on hover targets`, `magnetic effect (JS position lerp)`, `trail with opacity fade`, `scale on click`
- Implementation checklist: Custom cursor works; Hover morph smooth; Magnetic pull subtle; Trail performance ok; Click feedback visible; Touch fallback provided
- Design-system variables: `--cursor-size: 20px`, `--cursor-hover-scale: 1.5`, `--magnetic-distance: 100px`, `--trail-length: 10`, `--trail-fade: 0.1`, `--blend-mode: difference`

## 407. Voice-First Multimodal
- Keywords and mood: Voice UI, multimodal, audio feedback, conversational, hands-free, ambient, contextual, speech recognition
- Origin and era: 2025+ Voice Era; implementation complexity medium
- Primary colours: Calm neutrals: Soft White `#FAFAFA`, Muted Blue `#6B8FAF`, Gentle Purple `#9B8FBB`
- Secondary colours: Audio waveform colors, status indicators (listening/processing/speaking), success/error tones
- Effects and animation: Voice waveform visualization, listening pulse, processing spinner, speak animation, smooth transitions
- Best for: Voice assistants, accessibility apps, hands-free tools, smart home, automotive UI, cooking apps
- Do not use for: Visual-heavy content, data entry, complex forms, noisy environments
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a voice-first multimodal interface. Use: voice waveform visualization, listening state indicator, speaking animation, minimal visible UI, audio feedback cues, hands-free optimized, conversational flow, ambient design.
- Key properties and techniques: `Web Speech API integration`, `canvas for waveform`, `animation: pulse for listening`, `status indicators (color change)`, `audio visualization (Web Audio API)`, `minimal chrome`, `large touch targets`
- Implementation checklist: Voice recognition works; Visual feedback clear; Listening state obvious; Speaking animation smooth; Fallback UI provided; Accessibility excellent
- Design-system variables: `--listening-color: #6B8FAF`, `--speaking-color: #22C55E`, `--waveform-height: 60px`, `--pulse-duration: 1.5s`, `--indicator-size: 24px`, `--voice-accent: #9B8FBB`

## 408. 3D Product Preview
- Keywords and mood: 360 product view, rotatable, zoomable, touch-to-spin, AR preview, product configurator, interactive 3D model
- Origin and era: 2025+ E-commerce 3D; implementation complexity high
- Primary colours: Product-dependent, neutral backgrounds: Soft Grey `#E8E8E8`, Pure White `#FFFFFF`
- Secondary colours: Shadow gradients, reflection planes, environment lighting colors, accent highlights
- Effects and animation: Drag-to-rotate, pinch-to-zoom, spin animation, AR placement, material switching, smooth orbit controls
- Best for: E-commerce, furniture, fashion, automotive, electronics, jewelry, product configurators
- Do not use for: Content-heavy sites, blogs, dashboards, low-bandwidth, accessibility-critical
- Light mode conditional (works only with careful tuning); dark mode conditional (works only with careful tuning)
- Performance: high cost; driven by animation and large images
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Very High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a 3D product preview interface. Use: 360° rotation, drag-to-spin, pinch-to-zoom, AR preview button, material/color switcher, hotspot annotations, orbit controls, product configurator, smooth rendering.
- Key properties and techniques: `Three.js or model-viewer`, `OrbitControls`, `touch events for rotation`, `WebXR for AR`, `canvas with WebGL`, `loading placeholder`, `LOD for performance`, `environment lighting`
- Implementation checklist: 3D model loads fast; Rotation smooth; Zoom works (pinch/scroll); AR button functional; Colors switchable; Mobile touch works
- Design-system variables: `--canvas-bg: #F5F5F5`, `--hotspot-color: #3B82F6`, `--loading-spinner: primary`, `--rotation-speed: 0.5`, `--zoom-min: 0.5`, `--zoom-max: 2`

## 409. Gradient Mesh / Aurora Evolved
- Keywords and mood: Complex gradients, mesh gradients, multi-color blend, aurora effect, flowing colors, iridescent, holographic, prismatic
- Origin and era: 2025+ Gradient Evolution; implementation complexity medium
- Primary colours: Multi-stop gradients: Cyan `#00FFFF`, Magenta `#FF00FF`, Yellow `#FFFF00`, Blue `#0066FF`, Green `#00FF66`
- Secondary colours: Complementary mesh points, smooth color transitions, iridescent overlays, chromatic shifts
- Effects and animation: CSS mesh-gradient (experimental), SVG gradients, canvas gradients, smooth color morphing, flowing animation
- Best for: Hero sections, backgrounds, creative brands, music platforms, fashion, lifestyle, premium products
- Do not use for: Data interfaces, text-heavy content, accessibility-critical, conservative brands
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design with gradient mesh aurora effect. Use: multi-color mesh gradients, flowing color transitions, aurora/northern lights feel, iridescent overlays, holographic shimmer, prismatic effects, smooth color morphing.
- Key properties and techniques: `background: conic-gradient or mesh (SVG)`, `animation: gradient flow (background-position)`, `filter: hue-rotate for shimmer`, `mix-blend-mode: screen`, `canvas for complex mesh`, `multiple gradient layers`
- Implementation checklist: Mesh gradient visible; Colors flow smoothly; Aurora effect achieved; Performance acceptable; Text remains readable; Mobile renders ok
- Design-system variables: `--mesh-color-1: #00FFFF`, `--mesh-color-2: #FF00FF`, `--mesh-color-3: #FFFF00`, `--mesh-color-4: #00FF66`, `--flow-duration: 10s`, `--shimmer-intensity: 0.3`
- Relationship: a specialised variant of Aurora UI; start from the parent style's rules and apply these refinements

## 410. Editorial Grid / Magazine
- Keywords and mood: Magazine layout, asymmetric grid, editorial typography, pull quotes, drop caps, column layout, print-inspired
- Also known as: Editorial Grid
- Origin and era: 2020s Editorial Digital; implementation complexity low
- Primary colours: High contrast: Black `#000000`, White `#FFFFFF`, accent brand color
- Secondary colours: Muted supporting, pull quote highlights, byline colors, section dividers
- Effects and animation: Smooth scroll, reveal on scroll, parallax images, text animations, page-flip transitions
- Best for: News sites, blogs, magazines, editorial content, long-form articles, journalism, publishing
- Do not use for: Dashboards, apps, e-commerce catalogs, real-time data, short-form content
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Design an editorial magazine layout. Use: asymmetric grid, pull quotes, drop caps, multi-column text, large imagery, bylines, section dividers, print-inspired typography, article hierarchy, white space balance.
- Key properties and techniques: `display: grid with named areas`, `column-count for text`, `::first-letter for drop caps`, `blockquote styling`, `figure/figcaption`, `gap variations`, `font: serif for body`, `variable widths`
- Implementation checklist: Grid asymmetric; Typography editorial; Pull quotes styled; Drop caps present; Images large/impactful; Mobile reflows well
- Design-system variables: `--grid-cols: asymmetric`, `--body-font: Georgia/Merriweather`, `--heading-font: bold sans`, `--drop-cap-size: 4em`, `--pull-quote-size: 1.5em`, `--column-gap: 2rem`

## 411. Chromatic Aberration / RGB Split
- Keywords and mood: RGB split, color fringing, glitch, retro tech, VHS, analog error, distortion, lens effect
- Origin and era: 2020s Retro-Tech; implementation complexity medium
- Primary colours: Offset RGB: Red `#FF0000`, Green `#00FF00`, Blue `#0000FF`, Black `#000000`
- Secondary colours: Neon accents, scan lines, noise overlays, error colors
- Effects and animation: RGB offset animation, glitch timing, scan line movement, noise flicker, distortion on hover
- Best for: Music platforms, gaming, tech brands, creative portfolios, nightlife, entertainment, video platforms
- Do not use for: Corporate, healthcare, finance, accessibility-critical, elderly users
- Light mode supported; dark mode supported; default to dark presentation
- Performance: low cost; no heavy rendering drivers
- Accessibility: high risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design with chromatic aberration RGB split effect. Use: color channel offset (R/G/B), glitch aesthetic, retro tech feel, VHS error look, lens distortion, scan lines, noise overlay, analog imperfection.
- Key properties and techniques: `filter: drop-shadow with offset colors`, `text-shadow: RGB offset (-2px 0 red, 2px 0 cyan)`, `animation: glitch (random offset)`, `::before for scanlines`, `mix-blend-mode: screen for overlays`
- Implementation checklist: RGB split visible; Glitch effect controlled; Scan lines subtle; Performance ok; Readability maintained; Reduced motion option
- Design-system variables: `--rgb-offset: 2px`, `--red-channel: #FF0000`, `--green-channel: #00FF00`, `--blue-channel: #0000FF`, `--glitch-duration: 0.3s`, `--scanline-opacity: 0.1`
- Relationship: a specialised variant of Retro-Futurism; start from the parent style's rules and apply these refinements

## 412. Vintage Analog / Retro Film
- Keywords and mood: Film grain, VHS, cassette tape, polaroid, analog warmth, faded colors, light leaks, vintage photography
- Origin and era: 1970s-90s Analog Revival; implementation complexity medium
- Primary colours: Faded Cream `#F5E6C8`, Warm Sepia `#D4A574`, Muted Teal `#4A7B7C`, Soft Pink `#E8B4B8`
- Secondary colours: Grain overlays, light leak oranges, shadow blues, vintage paper tones, desaturated accents
- Effects and animation: Film grain overlay, VHS tracking effect, polaroid shake, fade-in transitions, light leak animations
- Best for: Photography portfolios, music/vinyl brands, vintage fashion, nostalgia marketing, film industry, cafes
- Do not use for: Modern tech, SaaS, healthcare, children's apps, corporate enterprise
- Light mode supported; dark mode conditional (works only with careful tuning)
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design with vintage analog film aesthetic. Use: film grain overlay, faded/desaturated colors, warm sepia tones, light leaks, VHS tracking effect, polaroid frame, analog warmth, nostalgic photography feel.
- Key properties and techniques: `filter: sepia() contrast() saturate(0.8)`, `background: noise texture overlay`, `animation: VHS tracking (transform skew)`, `light leak gradient overlay`, `border for polaroid frame`, `grain via SVG filter`
- Implementation checklist: Film grain visible; Colors faded/warm; Light leaks present; Nostalgic feel achieved; Performance with filters; Images look vintage
- Design-system variables: `--sepia-amount: 20%`, `--contrast: 1.1`, `--saturation: 0.8`, `--grain-opacity: 0.15`, `--light-leak-color: rgba(255,200,100,0.2)`, `--warm-tint: #F5E6C8`

# Part 44 — Landing Page Styles

## 413. Hero-Centric Design
- Keywords and mood: Large hero section, compelling headline, high-contrast CTA, product showcase, value proposition, hero image/video, dramatic visual
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Brand primary color, white/light backgrounds for contrast, accent color for CTA
- Secondary colours: Supporting colors for secondary CTAs, accent highlights, trust elements (testimonials, logos)
- Effects and animation: Smooth scroll reveal, fade-in animations on hero, subtle background parallax, CTA glow/pulse effect
- Best for: SaaS landing pages, product launches, service landing pages, B2B platforms, tech companies
- Do not use for: Complex navigation, multi-page experiences, data-heavy applications
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Very High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a hero-centric landing page. Use: full-width hero section, compelling headline (60-80 chars), high-contrast CTA button, product screenshot or video, value proposition above fold, gradient or image background, clear visual hierarchy.
- Key properties and techniques: `min-height: 100vh`, `display: flex`, `align-items: center`, `background: linear-gradient or image`, `text-shadow for readability`, `max-width: 800px for text`, `button with hover scale (1.05)`
- Implementation checklist: Hero section full viewport height; Headline visible above fold; CTA button high contrast; Background image optimized (WebP); Text readable on background; Mobile responsive layout
- Design-system variables: `--hero-min-height: 100vh`, `--headline-size: clamp(2rem, 5vw, 4rem)`, `--cta-padding: 1rem 2rem`, `--overlay-opacity: 0.5`, `--text-shadow: 0 2px 4px rgba(0,0,0,0.3)`
- Status: legacy pattern; prefer its refreshed landing-page version for new work

## 414. Conversion-Optimized
- Keywords and mood: Form-focused, minimalist design, single CTA focus, high contrast, urgency elements, trust signals, social proof, clear value
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Primary brand color, high-contrast white/light backgrounds, warning/urgency colors for time-limited offers
- Secondary colours: Secondary CTA color (muted), trust element colors (testimonial highlights), accent for key benefits
- Effects and animation: Hover states on CTA (color shift, slight scale), form field focus animations, loading spinner, success feedback
- Best for: E-commerce product pages, free trial signups, lead generation, SaaS pricing pages, limited-time offers
- Do not use for: Complex feature explanations, multi-product showcases, technical documentation
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Very High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a conversion-optimized landing page. Use: single primary CTA, minimal distractions, trust badges, urgency elements (limited time), social proof (testimonials), clear value proposition, form above fold, progress indicators.
- Key properties and techniques: `form with focus states`, `input:focus ring`, `button: primary color high contrast`, `position: sticky for CTA`, `max-width: 600px for form`, `loading spinner`, `success/error states`
- Implementation checklist: Single primary CTA visible; Form fields minimal (3-5); Trust badges present; Social proof above fold; Mobile form optimized; Loading states implemented; A/B test ready
- Design-system variables: `--cta-color: high contrast primary`, `--form-max-width: 600px`, `--input-height: 48px`, `--focus-ring: 3px solid accent`, `--success-color: #22C55E`, `--error-color: #EF4444`
- Status: legacy; prefer the funnel 3 step conversion landing-page pattern for new work

## 415. Feature-Rich Showcase
- Keywords and mood: Multiple feature sections, grid layout, benefit cards, visual feature demonstrations, interactive elements, problem-solution pairs
- Also known as: Feature-Rich
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Primary brand, bright secondary colors for feature cards, contrasting accent for CTAs
- Secondary colours: Supporting colors for: benefits (green), problems (red/orange), features (blue/purple), social proof (neutral)
- Effects and animation: Card hover effects (lift/scale), icon animations on scroll, feature toggle animations, smooth section transitions
- Best for: Enterprise SaaS, software tools landing pages, platform services, complex product explanations, B2B products
- Do not use for: Simple product pages, early-stage startups with few features, entertainment landing pages
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a feature showcase landing page. Use: grid layout for features (3-4 columns), feature cards with icons, benefit-focused copy, alternating sections, comparison tables, interactive demos, problem-solution pairs.
- Key properties and techniques: `display: grid`, `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))`, `gap: 2rem`, `card hover effects (translateY -4px)`, `icon containers`, `alternating background colors`
- Implementation checklist: Feature grid responsive; Icons consistent style; Card hover effects smooth; Alternating sections contrast; Benefits clearly stated; Mobile stacks properly
- Design-system variables: `--card-padding: 2rem`, `--card-radius: 12px`, `--icon-size: 48px`, `--grid-gap: 2rem`, `--section-padding: 4rem 0`, `--hover-transform: translateY(-4px)`
- Status: legacy pattern; prefer its refreshed landing-page version for new work

## 416. Minimal & Direct
- Keywords and mood: Minimal text, white space heavy, single column layout, direct messaging, clean typography, visual-centric, fast-loading
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Monochromatic primary, white background, single accent color for CTA, black/dark grey text
- Secondary colours: Minimal secondary colors, reserved for critical CTAs only, neutral supporting elements
- Effects and animation: Very subtle hover effects, minimal animations, fast page load (no heavy animations), smooth scroll
- Best for: Simple service landing pages, indie products, consulting services, micro SaaS, freelancer portfolios
- Do not use for: Feature-heavy products, complex explanations, multi-product showcases
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a minimal direct landing page. Use: single column layout, maximum white space, essential content only, one CTA, clean typography, no decorative elements, fast loading, direct messaging.
- Key properties and techniques: `max-width: 680px`, `margin: 0 auto`, `padding: 4rem 2rem`, `font-size: 18-20px`, `line-height: 1.6`, `minimal animations`, `no box-shadow`, `clean borders only`
- Implementation checklist: Single column centered; White space generous; One primary CTA only; No decorative images; Page weight < 500KB; Load time < `2s`
- Design-system variables: `--content-max-width: 680px`, `--spacing-large: 4rem`, `--font-size-body: 18px`, `--line-height: 1.6`, `--color-text: #1a1a1a`, `--color-bg: #ffffff`
- Status: legacy; prefer the minimal single column landing-page pattern for new work

## 417. Social Proof-Focused
- Keywords and mood: Testimonials prominent, client logos displayed, case studies sections, reviews/ratings, user avatars, success metrics, credibility markers
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Primary brand, trust colors (blue), success/growth colors (green), neutral backgrounds
- Secondary colours: Testimonial highlight colors, logo grid backgrounds (light grey), badge/achievement colors
- Effects and animation: Testimonial carousel animations, logo grid fade-in, stat counter animations (number count-up), review star ratings
- Best for: B2B SaaS, professional services, premium products, e-commerce conversion pages, established brands
- Do not use for: Startup MVPs, products without users, niche/experimental products
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a social proof landing page. Use: testimonials with photos, client logos grid, case study cards, review ratings (stars), user count metrics, success stories, trust indicators, before/after comparisons.
- Key properties and techniques: `testimonial cards with avatar`, `logo grid (grayscale filter)`, `star rating SVGs`, `counter animations (count-up)`, `blockquote styling`, `carousel for testimonials`, `metric cards`
- Implementation checklist: Testimonials with real photos; Logo grid 6-12 logos; Star ratings accessible; Metrics animated on scroll; Case studies linked; Mobile carousel works
- Design-system variables: `--avatar-size: 64px`, `--logo-height: 40px`, `--star-color: #FBBF24`, `--metric-font-size: 3rem`, `--testimonial-bg: #F9FAFB`, `--blockquote-border: 4px solid accent`
- Status: legacy; prefer the hero testimonials cta landing-page pattern for new work

## 418. Interactive Product Demo
- Keywords and mood: Embedded product mockup/video, interactive elements, product walkthrough, step-by-step guides, hover-to-reveal features, embedded demos
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Primary brand, interface colors matching product, demo highlight colors for interactive elements
- Secondary colours: Product UI colors, tutorial step colors (numbered progression), hover state indicators
- Effects and animation: Product animation playback, step progression animations, hover reveal effects, smooth zoom on interaction
- Best for: SaaS platforms, tool/software products, productivity apps landing pages, developer tools, productivity software
- Do not use for: Simple services, consulting, non-digital products, complexity-averse audiences
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Very High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design an interactive demo landing page. Use: embedded product mockup, video walkthrough, step-by-step guide, hover-to-reveal features, live demo button, screenshot carousel, feature highlights on interaction.
- Key properties and techniques: `video element with controls`, `position: relative for overlays`, `hover reveal (opacity transition)`, `step indicators`, `modal for full demo`, `screenshot lightbox`, `play button overlay`
- Implementation checklist: Demo video loads fast; Fallback for no-JS; Step indicators clear; Hover states obvious; Mobile touch friendly; Demo CTA prominent
- Design-system variables: `--video-aspect-ratio: 16/9`, `--overlay-bg: rgba(0,0,0,0.7)`, `--step-indicator-size: 32px`, `--play-button-size: 80px`, `--transition-duration: 300ms`
- Status: legacy; prefer the product demo features landing-page pattern for new work

## 419. Trust & Authority
- Keywords and mood: Certificates/badges displayed, expert credentials, case studies with metrics, before/after comparisons, industry recognition, security badges
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Professional colors (blue/grey), trust colors, certification badge colors (gold/silver accents)
- Secondary colours: Certificate highlight colors, metric showcase colors, comparison highlight (success green)
- Effects and animation: Badge hover effects, metric pulse animations, certificate carousel, smooth stat reveal
- Best for: Healthcare/medical landing pages, financial services, enterprise software, premium/luxury products, legal services
- Do not use for: Casual products, entertainment, viral/social-first products
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a trust-focused landing page. Use: certification badges, security indicators, expert credentials, industry awards, case study metrics, compliance logos (GDPR, SOC2), guarantee badges, professional photography.
- Key properties and techniques: `badge grid layout`, `shield icons`, `lock icons for security`, `certificate styling`, `metric cards with icons`, `professional color scheme (blue/grey)`, `subtle shadows for depth`
- Implementation checklist: Security badges visible; Certifications verified; Metrics with sources; Professional imagery; Guarantee clearly stated; Contact info accessible
- Design-system variables: `--badge-height: 48px`, `--trust-color: #1E40AF`, `--security-green: #059669`, `--card-shadow: 0 4px 6px rgba(0,0,0,0.1)`, `--metric-highlight: #F59E0B`
- Status: legacy; prefer the trust authority conversion landing-page pattern for new work

## 420. Storytelling-Driven
- Keywords and mood: Narrative flow, visual story progression, section transitions, consistent character/brand voice, emotional messaging, journey visualization
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Brand primary, warm/emotional colors, varied accent colors per story section, high visual variety
- Secondary colours: Story section color coding, emotional state colors (calm, excitement, success), transitional gradients
- Effects and animation: Section-to-section animations, scroll-triggered reveals, character/icon animations, morphing transitions, parallax narrative
- Best for: Brand/startup stories, mission-driven products, premium/lifestyle brands, documentary-style products, educational
- Do not use for: Technical/complex products (unless narrative-driven), traditional enterprise software
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: High
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Design a storytelling landing page. Use: narrative flow sections, scroll-triggered reveals, chapter-like structure, emotional imagery, brand journey visualization, founder story, mission statement, timeline progression.
- Key properties and techniques: `scroll-snap sections`, `Intersection Observer for reveals`, `parallax backgrounds`, `section transitions`, `timeline CSS`, `narrative typography (varied sizes)`, `image-text alternating`
- Implementation checklist: Story flows naturally; Scroll reveals smooth; Sections timed well; Emotional hooks present; Mobile story readable; Skip option available
- Design-system variables: `--section-min-height: 100vh`, `--reveal-duration: 600ms`, `--narrative-font: serif`, `--chapter-spacing: 8rem`, `--timeline-color: accent`, `--parallax-speed: 0.5`
- Status: legacy; prefer the scroll triggered storytelling landing-page pattern for new work

# Part 45 — Dashboard and Analytics Styles

## 421. Data-Dense Dashboard
- Keywords and mood: Multiple charts/widgets, data tables, KPI cards, minimal padding, grid layout, space-efficient, maximum data visibility
- Also known as: Data-Dense
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Neutral primary (light grey/white `#F5F5F5`), data colors (blue/green/red), dark text `#333333`
- Secondary colours: Chart colors: success (green `#22C55E`), warning (amber `#F59E0B`), alert (red `#EF4444`), neutral (grey)
- Effects and animation: Hover tooltips, chart zoom on click, row highlighting on hover, smooth filter animations, data loading spinners
- Best for: Business intelligence dashboards, financial analytics, enterprise reporting, operational dashboards, data warehousing
- Do not use for: Marketing dashboards, consumer-facing analytics, simple reporting
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Not applicable
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a data-dense dashboard. Use: multiple chart widgets, KPI cards row, data tables with sorting, minimal padding (8-12px), efficient grid layout, filter sidebar, dense but readable typography, maximum information density.
- Key properties and techniques: `display: grid`, `grid-template-columns: repeat(12, 1fr)`, `gap: 8px`, `padding: 12px`, `font-size: 12-14px`, `overflow: auto for tables`, `compact card design`, `sticky headers`
- Implementation checklist: Grid layout 12 columns; KPI cards responsive; Tables sortable; Filters functional; Loading states for data; Export functionality
- Design-system variables: `--grid-gap: 8px`, `--card-padding: 12px`, `--font-size-small: 12px`, `--table-row-height: 36px`, `--sidebar-width: 240px`, `--header-height: 56px`

## 422. Heat Map & Heatmap Style
- Keywords and mood: Color-coded grid/matrix, data intensity visualization, geographical heat maps, correlation matrices, cell-based representation, gradient coloring
- Also known as: Heat Map, Heat Map & Heatmap
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Gradient scale: Cool (blue `#0080FF`) to hot (red `#FF0000`), neutral middle (white/yellow)
- Secondary colours: Support gradients: Light (cool blue) to dark (warm red), divergent for positive/negative data, monochromatic options
- Effects and animation: Color gradient transitions on data change, cell highlighting on hover, tooltip reveal on click, smooth color animation
- Best for: Geographical analysis, performance matrices, correlation analysis, user behavior heatmaps, temperature/intensity data
- Do not use for: Linear data representation, categorical comparisons (use bar charts), small datasets
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Not applicable
- Right-to-left support: full
- Design brief: Design a heatmap visualization. Use: color gradient scale (cool to hot), cell-based grid, intensity legend, hover tooltips, geographic or matrix layout, divergent color scheme for +/- values, accessible color alternatives.
- Key properties and techniques: `display: grid`, `background: linear-gradient for legend`, `cell hover states`, `tooltip positioning`, `color scale (blue→white→red)`, `SVG for geographic`, `canvas for large datasets`
- Implementation checklist: Color scale clear; Legend visible; Tooltips informative; Colorblind alternatives; Zoom/pan for geo; Performance for large data
- Design-system variables: `--heatmap-cool: #0080FF`, `--heatmap-neutral: #FFFFFF`, `--heatmap-hot: #FF0000`, `--cell-size: 24px`, `--legend-width: 200px`, `--tooltip-bg: rgba(0,0,0,0.9)`
- Relationship: a specialised variant of Data-Dense Dashboard; start from the parent style's rules and apply these refinements

## 423. Executive Dashboard
- Keywords and mood: High-level KPIs, large key metrics, minimal detail, summary view, trend indicators, at-a-glance insights, executive summary
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Brand colors, professional palette (blue/grey/white), accent for KPIs, red for alerts/concerns
- Secondary colours: KPI highlight colors: positive (green), negative (red), neutral (grey), trend arrow colors
- Effects and animation: KPI value animations (count-up), trend arrow direction animations, metric card hover lift, alert pulse effect
- Best for: C-suite dashboards, business summary reports, decision-maker dashboards, strategic planning views
- Do not use for: Detailed analyst dashboards, technical deep-dives, operational monitoring
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: not recommended on mobile
- Conversion focus: Not applicable
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design an executive dashboard. Use: large KPI cards (4-6 max), trend sparklines, high-level summary only, clean layout with white space, traffic light indicators (red/yellow/green), at-a-glance insights, minimal detail.
- Key properties and techniques: `display: flex for KPI row`, `large font-size (24-48px) for metrics`, `sparkline SVG inline`, `status indicators (border-left color)`, `card shadows for hierarchy`, `responsive breakpoints`
- Implementation checklist: KPIs 4-6 maximum; Trends visible; Status colors clear; One-page view; Mobile simplified; Print-friendly layout
- Design-system variables: `--kpi-font-size: 48px`, `--sparkline-height: 32px`, `--status-green: #22C55E`, `--status-yellow: #F59E0B`, `--status-red: #EF4444`, `--card-min-width: 280px`
- Relationship: a specialised variant of Data-Dense Dashboard; start from the parent style's rules and apply these refinements

## 424. Real-Time Monitoring
- Keywords and mood: Live data updates, status indicators, alert notifications, streaming data visualization, active monitoring, streaming charts
- Also known as: Real-Time, Real-Time Monitor
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Alert colors: critical (red `#FF0000`), warning (orange `#FFA500`), normal (green `#22C55E`), updating (blue animation)
- Secondary colours: Status indicator colors, chart line colors varying by metric, streaming data highlight colors
- Effects and animation: Real-time chart animations, alert pulse/glow, status indicator blink animation, smooth data stream updates, loading effect
- Best for: System monitoring dashboards, DevOps dashboards, real-time analytics, stock market dashboards, live event tracking
- Do not use for: Historical analysis, long-term trend reports, archived data dashboards
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Not applicable
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a real-time monitoring dashboard. Use: live status indicators (pulsing), streaming charts, alert notifications, connection status, auto-refresh indicators, critical alerts prominent, system health overview.
- Key properties and techniques: `animation: pulse for live`, `WebSocket for streaming`, `position: fixed for alerts`, `status-dot with animation`, `chart real-time updates`, `notification toast`, `connection indicator`
- Implementation checklist: Live updates working; Alert sounds optional; Connection status shown; Auto-refresh indicated; Critical alerts prominent; Offline fallback
- Design-system variables: `--pulse-animation: pulse 2s infinite`, `--alert-z-index: 1000`, `--live-indicator: #22C55E`, `--critical-color: #DC2626`, `--update-interval: 5s`, `--toast-duration: 5s`
- Relationship: a specialised variant of Data-Dense Dashboard; start from the parent style's rules and apply these refinements

## 425. Drill-Down Analytics
- Keywords and mood: Hierarchical data exploration, expandable sections, interactive drill-down paths, summary-to-detail flow, context preservation
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Primary brand, breadcrumb colors, drill-level indicator colors, hierarchy depth colors
- Secondary colours: Drill-down path indicator colors, level-specific colors, highlight colors for selected level, transition colors
- Effects and animation: Drill-down expand animations, breadcrumb click transitions, smooth detail reveal, level change smooth, data reload animation
- Best for: Sales analytics, product analytics, funnel analysis, multi-dimensional data exploration, business intelligence
- Do not use for: Simple linear data, single-metric dashboards, streaming real-time dashboards
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Not applicable
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a drill-down analytics dashboard. Use: breadcrumb navigation, expandable sections, summary-to-detail flow, back button prominent, level indicators, context preservation, hierarchical data display.
- Key properties and techniques: `breadcrumb nav with separators`, `details/summary for expand`, `transition for drill animation`, `position: sticky breadcrumb`, `nested grid layouts`, `smooth scroll to detail`
- Implementation checklist: Breadcrumbs clear; Back navigation easy; Expand animation smooth; Context preserved; Mobile drill works; Deep links supported
- Design-system variables: `--breadcrumb-separator: /`, `--expand-duration: 300ms`, `--level-indent: 24px`, `--back-button-size: 40px`, `--context-bar-height: 48px`, `--drill-transition: 300ms ease`
- Relationship: a specialised variant of Data-Dense Dashboard; start from the parent style's rules and apply these refinements

## 426. Comparative Analysis Dashboard
- Keywords and mood: Side-by-side comparisons, period-over-period metrics, A/B test results, regional comparisons, performance benchmarks
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Comparison colors: primary (blue), comparison (orange/purple), delta indicator (green/red)
- Secondary colours: Winning metric color (green), losing metric color (red), neutral comparison (grey), benchmark colors
- Effects and animation: Comparison bar animations (grow to value), delta indicator animations (direction arrows), highlight on compare
- Best for: Period-over-period reporting, A/B test dashboards, market comparison, competitive analysis, regional performance
- Do not use for: Single metric dashboards, future projections (use forecasting), real-time only (no historical)
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Not applicable
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a comparison dashboard. Use: side-by-side metrics, period selectors (vs last month), delta indicators (+/-), benchmark lines, A/B comparison tables, winning/losing highlights, percentage change badges.
- Key properties and techniques: `display: flex for side-by-side`, `gap for comparison spacing`, `color coding (green up, red down)`, `arrow indicators`, `diff highlighting`, `comparison table zebra striping`
- Implementation checklist: Period selector works; Deltas calculated; Colors meaningful; Benchmarks shown; Mobile stacks properly; Export comparison
- Design-system variables: `--positive-color: #22C55E`, `--negative-color: #EF4444`, `--neutral-color: #6B7280`, `--comparison-gap: 2rem`, `--arrow-size: 16px`, `--badge-padding: 4px 8px`
- Relationship: a specialised variant of Data-Dense Dashboard; start from the parent style's rules and apply these refinements

## 427. Predictive Analytics
- Keywords and mood: Forecast lines, confidence intervals, trend projections, scenario modeling, AI-driven insights, anomaly detection visualization
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Forecast line color (distinct from actual), confidence interval shading, anomaly highlight (red alert), trend colors
- Secondary colours: High confidence (dark color), low confidence (light color), anomaly colors (red/orange), normal trend (green/blue)
- Effects and animation: Forecast line animation on draw, confidence band fade-in, anomaly pulse alert, smoothing function animations
- Best for: Forecasting dashboards, anomaly detection systems, trend prediction dashboards, AI-powered analytics, budget planning
- Do not use for: Historical-only dashboards, simple reporting, real-time operational dashboards
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Not applicable
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a predictive analytics dashboard. Use: forecast lines (dashed), confidence intervals (shaded bands), trend projections, anomaly highlights, scenario toggles, AI insight cards, probability indicators.
- Key properties and techniques: `stroke-dasharray for forecast lines`, `fill-opacity for confidence bands`, `anomaly markers (circles)`, `tooltip for predictions`, `toggle switches for scenarios`, `gradient for probability`
- Implementation checklist: Forecast line distinct; Confidence bands visible; Anomalies highlighted; Scenarios switchable; Predictions dated; Accuracy shown
- Design-system variables: `--forecast-dash: 5 5`, `--confidence-opacity: 0.2`, `--anomaly-color: #F59E0B`, `--prediction-color: #8B5CF6`, `--scenario-toggle-width: 48px`, `--ai-accent: #6366F1`
- Relationship: a specialised variant of Data-Dense Dashboard; start from the parent style's rules and apply these refinements

## 428. User Behavior Analytics
- Keywords and mood: Funnel visualization, user flow diagrams, conversion tracking, engagement metrics, user journey mapping, cohort analysis
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Funnel stage colors: high engagement (green), drop-off (red), conversion (blue), user flow arrows (grey)
- Secondary colours: Stage completion colors (success), abandonment colors (warning), engagement levels (gradient), cohort colors
- Effects and animation: Funnel animation (fill-down), flow diagram animations (connection draw), conversion pulse, engagement bar fill
- Best for: Conversion funnel analysis, user journey tracking, engagement analytics, cohort analysis, retention tracking
- Do not use for: Real-time operational metrics, technical system monitoring, financial transactions
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Not applicable
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a user behavior analytics dashboard. Use: funnel visualization, user flow diagrams (Sankey), conversion metrics, engagement heatmaps, cohort tables, retention curves, session replay indicators.
- Key properties and techniques: `SVG funnel with gradients`, `Sankey diagram library`, `percentage labels`, `cohort grid cells`, `retention chart (line/area)`, `click heatmap overlay`, `session timeline`
- Implementation checklist: Funnel stages clear; Flow diagram readable; Conversions calculated; Cohorts comparable; Retention trends visible; Privacy compliant
- Design-system variables: `--funnel-width: 100%`, `--stage-colors: gradient`, `--flow-opacity: 0.6`, `--cohort-cell-size: 40px`, `--retention-line-color: #3B82F6`, `--engagement-scale: 5 levels`
- Relationship: a specialised variant of Data-Dense Dashboard; start from the parent style's rules and apply these refinements

## 429. Financial Dashboard
- Keywords and mood: Revenue metrics, profit/loss visualization, budget tracking, financial ratios, portfolio performance, cash flow, audit trail
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Financial colors: profit (green `#22C55E`), loss (red `#EF4444`), neutral (grey), trust (dark blue `#003366`)
- Secondary colours: Revenue highlight (green), expenses (red), budget variance (orange/red), balance (grey), accuracy (blue)
- Effects and animation: Number animations (count-up), trend direction indicators, percentage change animations, profit/loss color transitions
- Best for: Financial reporting, accounting dashboards, portfolio tracking, budget monitoring, banking analytics
- Do not use for: Simple business dashboards, entertainment/social metrics, non-financial data
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: not recommended on mobile
- Conversion focus: Not applicable
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a financial dashboard. Use: revenue/expense charts, profit margins, budget vs actual, cash flow waterfall, financial ratios, audit trail table, currency formatting, period comparisons.
- Key properties and techniques: `number formatting (Intl.NumberFormat)`, `waterfall chart (positive/negative bars)`, `variance coloring`, `table with totals row`, `sparkline for trends`, `sticky column headers`
- Implementation checklist: Currency formatted; Decimals consistent; P&L clear; Budget variance shown; Audit trail complete; Export to Excel
- Design-system variables: `--currency-symbol: $`, `--decimal-places: 2`, `--profit-color: #22C55E`, `--loss-color: #EF4444`, `--variance-threshold: 10%`, `--table-header-bg: #F3F4F6`
- Relationship: a specialised variant of Data-Dense Dashboard; start from the parent style's rules and apply these refinements

## 430. Sales Intelligence Dashboard
- Keywords and mood: Deal pipeline, sales metrics, territory performance, sales rep leaderboard, win-loss analysis, quota tracking, forecast accuracy
- Origin and era: 2020s Modern; implementation complexity medium
- Primary colours: Sales colors: won (green), lost (red), in-progress (blue), blocked (orange), quota met (gold), quota missed (grey)
- Secondary colours: Pipeline stage colors, rep performance colors, quota achievement colors, forecast accuracy colors
- Effects and animation: Deal movement animations, metric updates, leaderboard ranking changes, gauge needle movements, status change highlights
- Best for: CRM dashboards, sales management, opportunity tracking, performance management, quota planning
- Do not use for: Marketing analytics, customer support metrics, HR dashboards
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Not applicable
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a sales intelligence dashboard. Use: pipeline funnel, deal cards (kanban), quota gauges, leaderboard table, territory map, win/loss ratios, forecast accuracy, activity timeline.
- Key properties and techniques: `kanban columns (flex)`, `gauge chart (SVG arc)`, `leaderboard ranking styles`, `map integration (Mapbox/Google)`, `timeline vertical`, `deal card with status border`
- Implementation checklist: Pipeline stages shown; Deals draggable; Quotas visualized; Rankings updated; Territory clickable; CRM integration
- Design-system variables: `--pipeline-colors: stage gradient`, `--gauge-track: #E5E7EB`, `--gauge-fill: primary`, `--rank-1-color: #FFD700`, `--rank-2-color: #C0C0C0`, `--rank-3-color: #CD7F32`
- Relationship: a specialised variant of Data-Dense Dashboard; start from the parent style's rules and apply these refinements

# Part 46 — Mobile App Styles

## 431. Bauhaus (包豪斯)
- Keywords and mood: bauhaus, geometric, constructivist, primary colors, hard shadow, bold, tactile, functional, poster, mechanical, architectural
- Origin and era: 1919 Bauhaus Movement; implementation complexity medium
- Primary colours: Primary Red `#D02020`, Primary Blue `#1040C0`, Primary Yellow `#F0C020`
- Secondary colours: Background `#F0F0F0` (Off-white), Foreground `#121212` (Stark Black), Muted `#E0E0E0`
- Effects and animation: Hard offset shadows (`4px 4px 0px` black), mechanical press active:translate, no smooth hover — instant `0ms` transitions, dot grid pattern on sections, slide-over transitions
- Best for: Mobile-first apps needing high personality, onboarding flows, branding-forward product screens, artisan/design brands, editorial mobile experiences
- Do not use for: Enterprise dashboards, accessibility-critical contexts (requires extra a11y work), data-heavy screens, conservative industries
- Light mode supported; dark mode conditional (works only with careful tuning)
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a Bauhaus (包豪斯) mobile interface using bauhaus, geometric, constructivist, primary colors, hard shadow, bold, tactile, functional. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `border-radius: 0px (cards/inputs) or 9999px (buttons/FAB)`, `box-shadow: 4px 4px 0px 0px #121212`, `active:translate-x-[2px] active:translate-y-[2px] active:shadow-none`, `border: 2px solid #121212`, `font-family: Outfit`, `font-weight: 900 uppercase tracking-tighter (headlines)`
- Implementation checklist: Geometric shapes only (circle/square); Primary color blocking applied; Hard offset shadows `4px`; border-2 border-black on all elements; Mechanical press active state; Outfit Black 900 uppercase headlines; Safe area (pt-safe pb-safe) respected; Thumb-friendly h-12/h-14 touch targets; No hover states (mobile-only); Vertical rhythm single-column stack
- Design-system variables: `--color-red: #D02020`, `--color-blue: #1040C0`, `--color-yellow: #F0C020`, `--color-bg: #F0F0F0`, `--color-fg: #121212`, `--border-width: 2px`, `--shadow-hard: 4px 4px 0px 0px #121212`, `--radius-block: 0px`, `--radius-pill: 9999px`, `--font-display: Outfit`, `--font-weight-hero: 900`

## 432. Minimalist Monochrome
- Keywords and mood: monochrome, black white, editorial, austere, typographic, sharp, zero radius, high contrast, brutalist, pocket editorial, serif, mechanical
- Origin and era: 2020s Editorial Mobile; implementation complexity medium
- Primary colours: Pure Black `#000000`, Pure White `#FFFFFF`
- Secondary colours: Muted `#F5F5F5`, Dark Gray `#525252`, Border Light `#E5E5E5`
- Effects and animation: Instant inversion active state (tap → bg-black text-white, zero transition-none), no shadows (strictly 2D), full-bleed horizontal rules (`4px` black section dividers), subtle paper noise texture (opacity: 0.03), slide-in page transitions with hard edge
- Best for: Luxury fashion e-commerce mobile, editorial publications, high-end portfolio apps, experimental/avant-garde brands, digital exhibitions
- Do not use for: Entertainment, colorful brands, friendly consumer apps, anything requiring visual warmth or gradient
- Light mode supported; dark mode conditional (works only with careful tuning)
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a Minimalist Monochrome mobile interface using monochrome, black white, editorial, austere, typographic, sharp, zero radius, high contrast. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `border-radius: 0px (ALL elements including modals)`, `box-shadow: none`, `active:bg-black active:text-white transition-none`, `border-b-4 border-black (section dividers)`, `divide-y divide-black (lists)`, `font-family: Playfair Display (headers) + Source Serif 4 (body) + JetBrains Mono (labels)`, `background-image: noise SVG opacity-[0.03]`
- Implementation checklist: `0px` border-radius on ALL elements; No shadows anywhere; Instant inversion on every tap (transition-none); `4px` black line separates hero from content; Safe area respected (pt-safe pb-safe); h-14 touch targets; Sticky section headers with border-b; Typography hero: word spans full screen width; Paper noise texture on backgrounds; Menu word-label instead of icon
- Design-system variables: `--color-bg: #FFFFFF`, `--color-fg: #000000`, `--color-muted: #F5F5F5`, `--color-muted-fg: #525252`, `--color-border: #000000`, `--color-border-light: #E5E5E5`, `--radius: 0px`, `--shadow: none`, `--border-hairline: 1px solid #E5E5E5`, `--border-thin: 1px solid #000000`, `--border-thick: 2px solid #000000`, `--border-heavy: 4px solid #000000`, `--font-display: Playfair Display`, `--font-body: Source Serif 4`, `--font-mono: JetBrains Mono`
- Relationship: a specialised variant of Minimalism & Swiss Style; start from the parent style's rules and apply these refinements

## 433. Modern Dark (Cinema Mobile)
- Keywords and mood: dark mode, cinematic, ambient light, glassmorphism, deep black, indigo, glow, blur, atmospheric, reanimated, haptic, premium, layered, frosted glass, linear gradient
- Origin and era: 2020s Cinematic Mobile; implementation complexity high
- Primary colours: Deep `#020203`, Base `#050506`, Elevated `#0a0a0c`, Accent `#5E6AD2`
- Secondary colours: Foreground `#EDEDEF`, Muted `#8A8F98`, Accent Glow `rgba(94 106 210/0.2)`, Border `rgba(255 255 255/0.08)`, Surface `rgba(255 255 255/0.05)`
- Effects and animation: Expo.out Bezier(0.16,1,0.3,1) easing; spring modals (damping:20 stiffness:90); haptic-linked press (Impact Light/Medium); animated ambient light blobs (Reanimated translateX/Y slow oscillation); BlurView glassmorphism headers/nav (intensity 20); scale press 0.97 → 1.0; avoid pure `#000000` (OLED smear)
- Best for: Developer tools, pro productivity apps, fintech/trading dashboards, media/streaming platforms, AI tool interfaces, high-end gaming companion apps
- Do not use for: Consumer apps needing warmth, children's apps, health/medical contexts where dark feels harsh, high-accessibility contexts needing maximum contrast
- Light mode supported; dark mode supported; default to dark presentation
- Performance: moderate cost; driven by animation and blur
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Medium
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a Modern Dark (Cinema Mobile) mobile interface using dark mode, cinematic, ambient light, glassmorphism, deep black, indigo, glow, blur. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `borderRadius: 16 (cards/buttons)`, `background: LinearGradient #0a0a0f→#020203`, `border: StyleSheet.hairlineWidth rgba(255,255,255,0.08)`, `BlurView intensity={20} tint='dark'`, `useAnimatedStyle + withRepeat (blob oscillation)`, `Easing.bezier(0.16,1,0.3,1)`, `withSpring damping:20 stiffness:90`, `Haptics.impactAsync(ImpactFeedbackStyle.Light)`, `scale: 0.97 press`
- Implementation checklist: No pure `#000000` backgrounds; LinearGradient base screen; Animated ambient blobs (Reanimated, native driver); BlurView on tab bar and headers; borderRadius 16 on all cards; Haptic feedback on every Pressable; Bezier(0.16,1,0.3,1) easing used; Accent glow behind primary button; No solid grey borders (rgba only); Bottom sheets replace all modals
- Design-system variables: `--bg-deep: #020203`, `--bg-base: #050506`, `--bg-elevated: #0a0a0c`, `--surface: rgba(255 255 255/0.05)`, `--foreground: #EDEDEF`, `--foreground-muted: #8A8F98`, `--accent: #5E6AD2`, `--accent-glow: rgba(94 106 210/0.2)`, `--border: rgba(255 255 255/0.08)`, `--radius: 16px`, `--easing: cubic-bezier(0.16 1 0.3 1)`, `--font: Inter`
- Relationship: a specialised variant of Dark Mode (OLED); start from the parent style's rules and apply these refinements

## 434. SaaS Mobile (High-Tech Boutique)
- Keywords and mood: saas, electric blue, gradient, fintech, spring animation, dual font, glassmorphism, boutique, premium, calistoga, inter, mono, tactile, haptic, bento
- Origin and era: 2020s SaaS Mobile; implementation complexity medium
- Primary colours: Electric Blue `#0052FF`, Gradient End `#4D7CFF`
- Secondary colours: Background `#FAFAFA`, Foreground `#0F172A`, Muted `#F1F5F9`, Card `#FFFFFF`, Border `#E2E8F0`
- Effects and animation: Spring animations (mass:1 damping:15 stiffness:120); gradient buttons (0052FF→4D7CFF); scale press 0.96→1.0 with haptics; floating FAB with gentle bobbing (Reanimated); glassmorphism BlurView navigation bars; staggered fade-in entrance (Y:20→0 + opacity:0→1); pulsing status dot on section badges; layout transitions (LayoutAnimation or Reanimated entering)
- Best for: B2B SaaS mobile dashboards, fintech apps, developer tool mobile companions, marketing analytics apps, HR/operations apps, modern business productivity
- Do not use for: Pure consumer entertainment, children's apps, highly decorative lifestyle apps, contexts where Electric Blue feels too corporate
- Light mode supported; dark mode conditional (works only with careful tuning)
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a SaaS Mobile (High-Tech Boutique) mobile interface using saas, electric blue, gradient, fintech, spring animation, dual font, glassmorphism, boutique. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `borderRadius: 16 (buttons/cards)`, `LinearGradient colors={['#0052FF','#4D7CFF']}`, `shadowOpacity: 0.1`, `shadowRadius: 10`, `elevation: 4`, `Haptics.impactAsync(ImpactFeedbackStyle.Light) on press`, `withSpring({mass:1, damping:15, stiffness:120})`, `withTiming Y:20→0 opacity:0→1 staggered entrance`, `LayoutAnimation.configureNext for list updates`, `BlurView on nav bars`
- Implementation checklist: SafeAreaView wraps all screens; All touch targets ≥ 44×`44px`; Spring config used for all transitions; Gradient buttons (not flat); Haptic on every Pressable; Section badges with PulseDot; Staggered entrance animation on screen mount; JetBrains Mono for data labels; Calistoga for hero headlines; Elevation/shadow on cards
- Design-system variables: `--bg: #FAFAFA`, `--fg: #0F172A`, `--muted: #F1F5F9`, `--accent: #0052FF`, `--accent-sec: #4D7CFF`, `--card: #FFFFFF`, `--border: #E2E8F0`, `--radius: 16px`, `--shadow: shadowOpacity 0.1 shadowRadius 10`, `--spring: mass 1 damping 15 stiffness 120`, `--font-display: Calistoga`, `--font-body: Inter`, `--font-mono: JetBrains Mono`
- Relationship: a specialised variant of Soft UI Evolution; start from the parent style's rules and apply these refinements

## 435. Terminal CLI (Mobile)
- Keywords and mood: terminal, cli, matrix green, monospace, hacker, ascii, command line, developer, web3, crypto, sci-fi, OLED, retro-future, field operative
- Origin and era: Retro-Future 1980s–2020s; implementation complexity medium
- Primary colours: Matrix Green `#33FF00`, OLED Black `#050505`
- Secondary colours: Amber `#FFB000`, Muted Green `#1A3D1A`, Error Red `#FF3333`, Border Green `#33FF00`
- Effects and animation: Blinking cursor (`500ms` opacity loop), typewriter text reveal hook, scanline overlay (repeating lines 0.05 opacity), ASCII art headers, instant color inversion on press (bg-green text-black), haptic on every keystroke, boot sequence splash on launch
- Best for: Developer tools, Web3/blockchain apps, geek-culture apps, ARG games, sci-fi/noir gaming companions, hacker/security tools, creative studio portfolios
- Do not use for: Consumer products, health apps, anything requiring approachability or warmth, children's apps, standard enterprise contexts
- Light mode not recommended; dark mode supported; default to dark presentation
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Low
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Design a Terminal CLI (Mobile) mobile interface using terminal, cli, matrix green, monospace, hacker, ascii, command line, developer. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `borderRadius: 0 (ALL elements)`, `borderWidth: 1`, `borderColor: '#33FF00'`, `backgroundColor: '#050505'`, `color: '#33FF00'`, `fontFamily: 'SpaceMono-Regular' or JetBrains Mono`, `fontSize: 12 or 14 or 16 only`, `lineHeight: 1.2x fontSize`, `Haptics.impactAsync(Light) on every press`, `useAnimatedValue blink 500ms`, `hitSlop: 12px all sides for bracketed buttons`
- Implementation checklist: `0px` border-radius everywhere; ASCII-style borders on cards; Boot sequence on launch; Blinking cursor component; Typewriter hook for new content; Scanline overlay (0.05 opacity); Haptic on every button press; Footer status bar component; hitSlop on all bracketed buttons (44×44dp); Reduced motion respected
- Design-system variables: `--bg: #050505`, `--fg-primary: #33FF00`, `--fg-amber: #FFB000`, `--fg-muted: #1A3D1A`, `--fg-error: #FF3333`, `--border: #33FF00`, `--radius: 0px`, `--font: SpaceMono-Regular or JetBrains Mono`, `--font-sizes: 12 14 16 only`, `--blink-duration: 500ms`, `--scanline-opacity: 0.05`
- Relationship: a specialised variant of HUD / Sci-Fi FUI; start from the parent style's rules and apply these refinements

## 436. Kinetic Brutalism (Mobile)
- Keywords and mood: kinetic, brutalism, motion, marquee, acid yellow, uppercase, oversized, aggressive typography, street, zine, high contrast, scroll-driven, haptic, reanimated
- Origin and era: 2020s Mobile Brutalism; implementation complexity high
- Primary colours: Acid Yellow `#DFE104`, Rich Black `#09090B`
- Secondary colours: Off-white `#FAFAFA`, Dark Gray `#27272A`, Zinc `#A1A1AA`, Border Zinc `#3F3F46`
- Effects and animation: Infinite marquee (Reanimated, Linear easing, `5s` loop, hard clip), hero parallax (scale 1.0→1.3 + fade), sticky section header push, card flood inversion on press (bg→`#DFE104`, text→`#000000`), haptic Medium on every press, scroll-triggered interpolate transforms, `0px` radius, `2px` borders, `100ms` color transitions
- Best for: Immersive storytelling apps, brand flagship mobile, music/culture platforms, sports apps, underground zines, limited-edition product drops, performance dashboards
- Do not use for: Calm informational apps, healthcare, finance contexts needing trust, children's, any context where aggressive typography feels inappropriate
- Light mode supported; dark mode conditional (works only with careful tuning); default to dark presentation
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High energy
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Design a Kinetic Brutalism (Mobile) mobile interface using kinetic, brutalism, motion, marquee, acid yellow, uppercase, oversized, aggressive typography. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `borderRadius: 0`, `borderWidth: 2`, `borderColor: '#3F3F46'`, `backgroundColor: '#09090B'`, `color: '#FAFAFA'`, `fontWeight: '800 or 900'`, `letterSpacing: -1 (large) or 2 (labels)`, `lineHeight: 0.9–1.1 * fontSize`, `Reanimated withRepeat marquee timing 5000ms Easing.linear`, `Interpolate scroll→scale + opacity`, `Haptics.impactAsync(Medium)`, `scale press: 0.95`, `100ms color transitions`
- Implementation checklist: Infinite marquee rows (Reanimated, no fade edges); Hero parallax scroll (scale+opacity Interpolate); All display text uppercase; `0px` border-radius; `2px` borders; Acid yellow card flood on press; Haptic Medium on every interaction; Font scale helper (windowWidth/375*size); Safe area for massive headers; Reduced motion stops marquees
- Design-system variables: `--bg: #09090B`, `--fg: #FAFAFA`, `--muted: #27272A`, `--muted-fg: #A1A1AA`, `--accent: #DFE104`, `--accent-fg: #000000`, `--border: #3F3F46`, `--radius: 0px`, `--border-width: 2px`, `--shadow: none`, `--marquee-speed: 5000ms`, `--press-duration: 100ms`, `--font: Space Grotesk or Inter`
- Relationship: a specialised variant of Brutalism; start from the parent style's rules and apply these refinements

## 437. Flat Design Mobile (Touch-First)
- Keywords and mood: flat, 2D, no shadow, color blocking, geometric, bold, poster, icon, touch-first, minimal, clean, tailored, cross-platform
- Origin and era: 2010s–2020s Flat Mobile; implementation complexity low
- Primary colours: Blue `#3B82F6`, Emerald `#10B981`
- Secondary colours: Background `#FFFFFF`, Surface `#F3F4F6`, Text `#111827`, Amber `#F59E0B`, Border `#E5E7EB`
- Effects and animation: Immediate press feedback (scale 0.97, no delay), color section blocking (full-width contrasting View), zero elevation/shadow, solid icon containers (colored squares/circles), geometric low-opacity shape overlays, bottom tabs solid fill (no floating)
- Best for: Cross-platform apps (iOS+Android parity), information-dense dashboards, system UI, brand illustration, onboarding flows, marketing pages, icon design
- Do not use for: Ultra-premium contexts needing depth/shadow, dark-mode-first products, contexts where flat design reads as unfinished or sterile
- Light mode supported; dark mode conditional (works only with careful tuning)
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a Flat Design Mobile (Touch-First) mobile interface using flat, 2D, no shadow, color blocking, geometric, bold, poster, icon. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `shadowOpacity: 0`, `elevation: 0`, `borderRadius: 6/12/999`, `height: 48 minimum touch targets`, `spacing: 4/8/16/24/32/48 system`, `backgroundColor (section blocking)`, `Pressable scale: pressed ? 0.97 : 1`, `fontWeight: '800' heads / '600' sub / '400' body`, `letterSpacing: -0.5 heads / 1 labels`, `textTransform: 'uppercase' labels`, `strokeWidth={2.5} icons`, `borderWidth: 3/4 for featured CTAs`
- Implementation checklist: Zero elevation AND shadowOpacity on all elements; Color-blocking sections (not borders); All touch targets ≥ 48×48; No gradients on flat elements; Icons inside solid colored containers; Pressable scale feedback; Geometric shapes as bg decoration; Bold flat bottom tabs (no floating); Primary headlines much larger than body; 4pt spacing system throughout
- Design-system variables: `--bg: #FFFFFF`, `--surface: #F3F4F6`, `--fg: #111827`, `--primary: #3B82F6`, `--secondary: #10B981`, `--accent: #F59E0B`, `--border: #E5E7EB`, `--radius-sm: 6px`, `--radius-md: 12px`, `--radius-pill: 999px`, `--shadow: none`, `--elevation: 0`, `--touch-target: 48px`, `--spacing: 4 8 16 24 32 48`
- Relationship: a specialised variant of Flat Design; start from the parent style's rules and apply these refinements

## 438. Material 3 Expressive (Mobile)
- Keywords and mood: material 3 expressive, vibrant color, spring motion, adaptive components, flexible typography, contrasting shapes, android
- Also known as: Material You, Material You (MD3 Mobile), MD3 Mobile, M3 Expressive, Material Design 3 Expressive
- Origin and era: Google Material Design 3; implementation complexity medium
- Primary colours: Primary Violet `#6750A4`, Secondary Container `#E8DEF8`, Tertiary `#7D5260`
- Secondary colours: Surface `#FFFBFE`, On Surface `#1C1B1F`, Surface Container `#F3EDF7`, Outline `#79747E`
- Effects and animation: Tonal elevation (overlay colors instead of strong shadows), pill-shaped buttons and chips (borderRadius 999), emphasized easing Easing.bezier(0.2,0,0,1), state layers (pressed overlays `10–15%` opacity), Reanimated-filled label float for inputs, HapticFeedback on FAB/toggles
- Best for: Android, Wear OS, and Pixel-aligned products using Material 3 components
- Do not use for: Ultra-minimal brutalist brands, terminal/hacker aesthetics, monochrome editorial apps
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a Material 3 Expressive mobile interface with vibrant semantic color, contrasting shapes, flexible typography, adaptive components, spring motion, and reduced-motion alternatives.
- Key properties and techniques: `borderRadius: 999 (buttons/chips)`, `containerRadius: 16–28`, `backgroundColor: '#FFFBFE'`, `colorPrimary: '#6750A4'`, `colorSecondaryContainer: '#E8DEF8'`, `colorSurfaceContainer: '#F3EDF7'`, `outlineColor: '#79747E'`, `Pressable state-layer overlay (opacity 0.1–0.15)`, `Easing.bezier(0.2,0,0,1)`, `HapticFeedback.impactMedium on FAB`, `floating label using Reanimated translateY/scale`
- Implementation checklist: MD3 color tokens applied (background/surface/container); All CTAs are pill-shaped; State-layer overlays instead of opacity 0.5 hacks; Emphasized easing used for all animations; Floating label inputs implemented; FAB uses tertiary color with correct elevation; Safe areas respected for organic shapes; No pure white background; No harsh box-shadows (ambient only)
- Design-system variables: `--md3-bg: #FFFBFE`, `--md3-on-surface: #1C1B1F`, `--md3-primary: #6750A4`, `--md3-on-primary: #FFFFFF`, `--md3-secondary-container: #E8DEF8`, `--md3-on-secondary-container: #1D192B`, `--md3-tertiary: #7D5260`, `--md3-surface-container: #F3EDF7`, `--md3-outline: #79747E`, `--radius-pill: 999px`, `--easing-emphasized: cubic-bezier(0.2,0,0,1)`

## 439. Neo Brutalism (Mobile)
- Keywords and mood: neo brutalism, pop art, stickers, thick borders, cream background, hot red, vivid yellow, soft violet, hard offset shadow, mechanical press, collage
- Origin and era: 2020s Neo-Brutalism; implementation complexity high
- Primary colours: Cream `#FFFDF5`, Hot Red `#FF6B6B`, Vivid Yellow `#FFD93D`
- Secondary colours: Soft Violet `#C4B5FD`, Pure Black `#000000`, White `#FFFFFF`
- Effects and animation: Thick `4px` black borders on all major elements, hard offset shadows (`4–8px`, no blur), mechanical press: translateX/Y equal to shadow offset, slightly rotated cards/badges (`-2deg`/`2deg`), high-saturation color blocking, spring/linear animations only
- Best for: Creative tools, collab platforms, Gen Z marketing & e-commerce, portfolio sites, sticker-book style content apps
- Do not use for: Serious enterprise apps, conservative industries, sober fintech, accessibility-first contexts (must tune contrast)
- Light mode supported; dark mode not recommended
- Performance: moderate cost; driven by animation and blur
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a Neo Brutalism (Mobile) mobile interface using neo brutalism, pop art, stickers, thick borders, cream background, hot red, vivid yellow, soft violet. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `borderWidth: 4 (primary)`, `2 (secondary)`, `borderRadius: 0 or 999 (badges only)`, `backgroundColor: '#FFFDF5'`, `shadow implemented as offset View`, `transform: [{translateX:4},{translateY:4}] on PressIn`, `fontFamily: 'SpaceGrotesk-Bold'`, `fontWeight: '700/900'`, `transform: [{ rotate: '-1deg' }] on cards`, `padding: 20`
- Implementation checklist: `4px` borders on major elements; Hard offset shadow implemented via extra View; Mechanical press hides shadow; Cream canvas background; Pop-art color palette used; Cards/badges slightly rotated; No gradients or soft shadows; Only bold/black type weights; Badges slapped with absolute positioning; Anti-patterns (no subtle gray, no blur) avoided
- Design-system variables: `--bg: #FFFDF5`, `--ink: #000000`, `--accent-primary: #FF6B6B`, `--accent-secondary: #FFD93D`, `--accent-muted: #C4B5FD`, `--white: #FFFFFF`, `--border-primary: 4px solid #000000`, `--shadow-offset-small: 4px`, `--shadow-offset-medium: 8px`, `--radius: 0px`, `--radius-pill: 999px`, `--font: Space Grotesk`
- Relationship: a specialised variant of Neubrutalism; start from the parent style's rules and apply these refinements

## 440. Bold Typography (Mobile Poster)
- Keywords and mood: bold typography, editorial, poster, broadsheet, vermillion, negative space, edge-to-edge type, underline CTA, near-black, warm white
- Origin and era: Editorial 2020s; implementation complexity medium
- Primary colours: Near Black `#0A0A0A`, Warm White `#FAFAFA`
- Secondary colours: Muted `#1A1A1A`, Secondary Text `#737373`, Accent Vermillion `#FF3D00`, Border `#262626`
- Effects and animation: Hero headlines `48–72px` (`5:1` vs body size), tight tracking (`-1.5px`), edge-to-edge type, massive vertical spacing (`60px`+), underline CTAs (`2–3px` accent line), instant `200ms` transitions (no bounce), strictly `0px` radius containers, color shifts for active state instead of elevation
- Best for: Creative brand heroes, reading-focused apps, event/exhibition pages, editorial mobile experiences, landing hero sections
- Do not use for: Utility dashboards, kids apps, playful consumer products, contexts needing many icons or heavy imagery
- Light mode supported; dark mode conditional (works only with careful tuning); default to dark presentation
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a Bold Typography (Mobile Poster) mobile interface using bold typography, editorial, poster, broadsheet, vermillion, negative space, edge-to-edge type, underline CTA. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `backgroundColor: '#0A0A0A'`, `color: '#FAFAFA'`, `accent: '#FF3D00'`, `borderColor: '#262626'`, `borderRadius: 0`, `paddingHorizontal: 24`, `headline style: fontSize:56–72`, `fontWeight:'700/800'`, `letterSpacing:-1.5`, `lineHeight:1.1*fontSize`, `body: fontSize:16–18`, `lineHeight:1.6*fontSize`, `underline CTA: 2–3px height View under text`, `transition: 200ms cubic-bezier(0.25,0,0,1)`
- Implementation checklist: H1 at least 4–5× body size; All containers 0 radius; Underline CTA pattern used; Large vertical gaps between sections; No shadows or soft corners; Accent used only for interaction; Text bleeds to/over screen edges; Animation timings `200ms`; Accessible contrast ≥ `18:1`; Body text never below `16px`
- Design-system variables: `--bg: #0A0A0A`, `--fg: #FAFAFA`, `--muted: #1A1A1A`, `--muted-fg: #737373`, `--accent: #FF3D00`, `--accent-fg: #0A0A0A`, `--border: #262626`, `--font-primary: Inter Tight`, `--font-display: Playfair Display Italic`, `--font-mono: JetBrains Mono`
- Relationship: a specialised variant of Exaggerated Minimalism; start from the parent style's rules and apply these refinements

## 441. Academia (Scholarly Mobile)
- Keywords and mood: academia, library, mahogany, parchment, brass, crimson, serif, drop cap, arch-top, vignette, leather, scholarly, tactile
- Origin and era: Timeless Scholarly; implementation complexity high
- Primary colours: Mahogany `#1C1714`, Oak `#251E19`
- Secondary colours: Parchment `#E8DFD4`, Worn Leather `#3D332B`, Faded Ink `#9C8B7A`, Brass `#C9A962`, Library Crimson `#8B2635`
- Effects and animation: Deep mahogany backgrounds, oak surface cards, brass accented CTAs, arch-top hero/imagery, heavy vignette overlays, sepia-tinted images, drop caps with brass Cinzel, Roman numeral volume headings, slow timing-based animations (Easing.out poly(4)), zero neon or modern tech cues
- Best for: Knowledge management apps, deep reading tools, ritual-heavy personal brands, lore-heavy RPG/roleplay apps, culture-specific community platforms
- Do not use for: Hyper-modern tech dashboards, neon/glassmorphism, playful Gen Z branding
- Light mode supported; dark mode conditional (works only with careful tuning); default to dark presentation
- Performance: moderate cost; driven by animation and blur
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: conditional (needs a simplified mobile variant)
- Conversion focus: Medium
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a Academia (Scholarly Mobile) mobile interface using academia, library, mahogany, parchment, brass, crimson, serif, drop cap. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `backgroundColor: '#1C1714'`, `altSurface: '#251E19'`, `textColor: '#E8DFD4'`, `mutedBg: '#3D332B'`, `borderColor: '#4A3F35'`, `brass: '#C9A962'`, `crimson: '#8B2635'`, `borderRadius: 4 (default)`, `archTopRadius: 100 for hero`, `shadowOpacity:0.4 shadowRadius:6 elevation:8 for cards`, `textShadow on headings`, `vignette overlay via LinearGradient`
- Implementation checklist: Mahogany/oak/parchment palette applied; Brass used on all tappable items; Arch-top imagery used in hero/cards; Drop caps & Roman numerals used; Vignette overlay present; No sans-serif body fonts; No neon/bright modern colors; Animations use non-spring timing; Inputs use worn-leather style; Wax seal badges implemented
- Design-system variables: `--bg: #1C1714`, `--bg-alt: #251E19`, `--fg: #E8DFD4`, `--muted: #3D332B`, `--muted-fg: #9C8B7A`, `--border: #4A3F35`, `--accent-brass: #C9A962`, `--accent-crimson: #8B2635`, `--radius: 4px`, `--arch-radius: 100px`, `--shadow-card: 0 4px 6px rgba(0,0,0,0.4)`, `--font-heading: Cormorant Garamond`, `--font-body: Crimson Pro`, `--font-label: Cinzel`
- Relationship: a specialised variant of Editorial Grid / Magazine; start from the parent style's rules and apply these refinements

## 442. Cyberpunk Mobile HUD
- Keywords and mood: cyberpunk, neon, glitch, chamfered, orbitron, jetbrains, scanlines, crt, hud, matrix, military, decker
- Origin and era: Cyber-Noir; implementation complexity high
- Primary colours: Void `#0A0A0F`, Card `#12121A`
- Secondary colours: Neon Green `#00FF88`, Neon Magenta `#FF00FF`, Cyber Cyan `#00D4FF`, Neutral Text `#E0E0E0`, Alert Red `#FF3366`, Border `#2A2A3A`
- Effects and animation: Deep void background with neon radiance, chamfered 45° corners via SVG/Skia, scanline overlay, CRT flicker opacity oscillation, glitch animations (translateX ±2), neon pulses around buttons, HUD corner brackets, terminal prompt text inputs, heavy use of blurView holographic panels
- Best for: Gaming dashboards, crypto/cyberpunk apps, sci-fi companion tools, hacker OS skins, data-heavy monitoring HUDs
- Do not use for: Serious enterprise, health/finance requiring calm trust, minimal editorial apps
- Light mode not recommended; dark mode supported; default to dark presentation
- Performance: high cost; driven by animation and large images
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: with caveats (directional effects and text animation need review)
- Design brief: Design a Cyberpunk Mobile HUD mobile interface using cyberpunk, neon, glitch, chamfered, orbitron, jetbrains, scanlines, crt. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `backgroundColor: '#0A0A0F'`, `cardBg: '#12121A'`, `accent: '#00FF88'`, `accent2: '#FF00FF'`, `accent3: '#00D4FF'`, `borderColor: '#2A2A3A'`, `destructive: '#FF3366'`, `borderRadius: 0`, `chamfer via SVG path`, `shadowColor accent with animated radius`, `scanline overlay View pointerEvents='none'`, `withRepeat glitch translateX [-2,2,0]`, `Easing.steps(2)`
- Implementation checklist: Chamfered corners used instead of radius; Scanline & CRT flicker implemented; Orbitron + JetBrains Mono typography; Neon glow shadows on primary buttons; Glitch animation on active states; Prompt-style inputs with custom cursor; HUD corner brackets implemented; Safe-area system status bar styled; Reduced motion disables glitch/flicker; Icons configured with Lucide accent color
- Design-system variables: `--bg: #0A0A0F`, `--card: #12121A`, `--fg: #E0E0E0`, `--muted: #1C1C2E`, `--accent: #00FF88`, `--accent2: #FF00FF`, `--accent3: #00D4FF`, `--border: #2A2A3A`, `--destructive: #FF3366`, `--radius: 0px`, `--font-heading: Orbitron`, `--font-body: JetBrains Mono`
- Relationship: a specialised variant of HUD / Sci-Fi FUI; start from the parent style's rules and apply these refinements

## 443. Bitcoin DeFi (Mobile)
- Keywords and mood: web3, bitcoin, defi, digital gold, fintech, wallet, orange, glassmorphism, gradient, blur, holographic, trust, precision
- Origin and era: Fintech/Web3; implementation complexity high
- Primary colours: Bitcoin Orange `#F7931A`, Burnt Orange `#EA580C`, Digital Gold `#FFD600`
- Secondary colours: Void `#030304`, Dark Matter `#0F1115`, Pure Light `#FFFFFF`, Stardust `#94A3B8`, Border Dim `rgba(30,41,59,0.2)`
- Effects and animation: Deep void + dark matter surfaces, Bitcoin orange/gold gradients for CTAs, pill buttons with glowing shadows, glassmorphic BlurView nav, monospace data rows, gradient text balances + masked orange-gold, pulsing status indicators and vertical ledger timelines, ultra-thin borders, high-precision typography
- Best for: DeFi dashboards, wallets, NFT marketplaces, Web3 social, metaverse utilities, high-tech fintech brands
- Do not use for: Playful casual apps, low-tech brands, ultra-minimal editorial apps
- Light mode not recommended; dark mode supported; default to dark presentation
- Performance: moderate cost; driven by animation and blur
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a Bitcoin DeFi (Mobile) mobile interface using web3, bitcoin, defi, digital gold, fintech, wallet, orange, glassmorphism. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `backgroundColor: '#030304'`, `cardBg: '#0F1115'`, `textColor: '#FFFFFF'`, `mutedText: '#94A3B8'`, `borderColor: 'rgba(30,41,59,0.2)'`, `accentBitcoin: '#F7931A'`, `accentBurnt: '#EA580C'`, `accentGold: '#FFD600'`, `borderRadius: 24 for cards`, `radiusPill: 999 for buttons`, `BlurView intensity 20`, `LinearGradient on CTAs`, `shadowColor '#F7931A' shadowRadius up to 10`, `JetBrains Mono for numeric text`
- Implementation checklist: Void/dark-matter palette applied; Bitcoin orange/gold gradient buttons; BlurView nav implemented; Monospace for numeric data; Hairline borders on blocks; Gradient text on balances; Pulsing network status indicators; Ledger vertical timeline; Haptics on money actions; SafeArea + FlashList for heavy lists
- Design-system variables: `--bg-void: #030304`, `--bg-surface: #0F1115`, `--fg: #FFFFFF`, `--fg-muted: #94A3B8`, `--border-dim: rgba(30,41,59,0.2)`, `--accent-bitcoin: #F7931A`, `--accent-burnt: #EA580C`, `--accent-gold: #FFD600`, `--radius-card: 24px`, `--radius-pill: 999px`, `--blur-intensity: 20`, `--font-heading: Space Grotesk`, `--font-body: Inter`, `--font-mono: JetBrains Mono`
- Relationship: a specialised variant of Dark Mode (OLED); start from the parent style's rules and apply these refinements

## 444. Claymorphism (Mobile)
- Keywords and mood: claymorphism, clay, 3d, soft, bubbly, candy, playful, rounded, squish, tactile, inflate, silicone, haptic, spring
- Origin and era: Consumer/Education; implementation complexity high
- Primary colours: Vivid Violet `#7C3AED`, Hot Pink `#DB2777`
- Secondary colours: Canvas `#F4F1FA`, Soft Charcoal `#332F3A`, Emerald `#10B981`, Amber `#F59E0B`, Lavender-Gray `#635F69`
- Effects and animation: Multi-layer shadow stacks (nested View) to simulate clay depth, LinearGradient `#A78BFA`→`#7C3AED` buttons, borderRadius 40–50 outer / 32 cards / 20 buttons, Reanimated spring squish (scale 0.92 on press), BlurView glass-clay hybrid cards, floating blobs with slow ±`20px` drift, Haptics Light on every press
- Best for: Children education apps, teen social products, crypto gamification, creative tools, brand mascot-led apps
- Do not use for: Serious enterprise, high-density data, editorial reading apps, fintech trust signals
- Light mode supported; dark mode supported
- Performance: high cost; driven by animation and large images
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: full
- Design brief: Design a Claymorphism (Mobile) mobile interface using claymorphism, clay, 3d, soft, bubbly, candy, playful, rounded. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `backgroundColor: '#F4F1FA'`, `cardBg: 'rgba(255,255,255,0.7)'`, `textPrimary: '#332F3A'`, `textMuted: '#635F69'`, `accentPrimary: '#7C3AED'`, `accentSecondary: '#DB2777'`, `success: '#10B981'`, `warning: '#F59E0B'`, `radiusOuter: 50`, `radiusCard: 32`, `radiusButton: 20`, `shadowStack: 'nested View'`, `gradientButton: ['#A78BFA', '#7C3AED']`, `springDamping: 10`
- Implementation checklist: Background uses `#F4F1FA` (no pure white); Multi-layer clay shadow stack applied; Cards use blurred glass-clay hybrid; Buttons squish to scale 0.92 on press; Spring physics on all interactions; Nunito Black for headings; Background blobs drifting; Haptics on every press; Nested border radius (card 32, inner 24); Bento layout with hero span
- Design-system variables: `--bg: #F4F1FA`, `--card-bg: rgba(255,255,255,0.7)`, `--text: #332F3A`, `--muted: #635F69`, `--accent: #7C3AED`, `--accent2: #DB2777`, `--success: #10B981`, `--warning: #F59E0B`, `--radius-outer: 50px`, `--radius-card: 32px`, `--radius-button: 20px`, `--font-heading: Nunito Black`, `--font-body: DM Sans`
- Relationship: a specialised variant of Claymorphism; start from the parent style's rules and apply these refinements

## 445. Enterprise SaaS (Mobile)
- Keywords and mood: enterprise, saas, b2b, professional, indigo, violet, gradient, polished, trustworthy, clean, approachable, spring, haptic
- Origin and era: Enterprise/SaaS; implementation complexity high
- Primary colours: Indigo `#4F46E5`, Violet `#7C3AED`
- Secondary colours: Slate 50 `#F8FAFC`, White `#FFFFFF`, Slate 900 `#0F172A`, Slate 500 `#64748B`, Emerald `#10B981`, Slate 200 `#E2E8F0`
- Effects and animation: Indigo→Violet gradient primary CTAs + active tab highlights, colored card shadows `rgba(79,70,229,0.08)`, pill buttons or 12pt radius, full-width CTA at screen bottom, spring press scale 0.97, floating label inputs with animated focus border, skeletal loading pulses (Indigo/Slate tint), Bottom Sheets with drag dismiss, swipe-to-action list cards, scroll-linked title collapse
- Best for: B2B backend management, productivity tools, government and finance mobile apps, SaaS companion apps, enterprise dashboards
- Do not use for: Pure consumer entertainment, Gen-Z youth apps, gaming UI, ultra-minimal editorial
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: High
- Right-to-left support: partial (directional motion or layout needs mirroring)
- Design brief: Design a Enterprise SaaS (Mobile) mobile interface using enterprise, saas, b2b, professional, indigo, violet, gradient, polished. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `backgroundColor: '#F8FAFC'`, `surfaceBg: '#FFFFFF'`, `textPrimary: '#0F172A'`, `textMuted: '#64748B'`, `primary: '#4F46E5'`, `secondary: '#7C3AED'`, `success: '#10B981'`, `border: '#E2E8F0'`, `radiusCard: 16`, `radiusButton: 999`, `radiusInput: 8`, `shadowCard: 'rgba(79,70,229,0.08)'`, `gradientPrimary: ['#4F46E5', '#7C3AED']`, `screenPadding: 20`
- Implementation checklist: Background `#F8FAFC` applied; Indigo→Violet gradient on primary CTA; Colored card shadows (not gray); Plus Jakarta Sans typography; Floating label inputs with Indigo focus; Scale 0.97 press with haptic Medium; Bottom Tab Navigation implemented; Safe Area strict compliance; Skeletal loading placeholders; Reduced Motion fallback
- Design-system variables: `--bg: #F8FAFC`, `--surface: #FFFFFF`, `--text: #0F172A`, `--muted: #64748B`, `--primary: #4F46E5`, `--secondary: #7C3AED`, `--success: #10B981`, `--border: #E2E8F0`, `--radius-card: 16px`, `--radius-pill: 999px`, `--radius-input: 8px`, `--shadow-card: rgba(79,70,229,0.08)`, `--font: Plus Jakarta Sans`
- Relationship: a specialised variant of Soft UI Evolution; start from the parent style's rules and apply these refinements

## 446. Sketch Hand-Drawn (Mobile)
- Keywords and mood: sketch, hand-drawn, handwriting, wobbly, imperfect, paper, kalam, organic, collage, post-it, tape, offset shadow, scribble
- Also known as: Sketch Hand-Drawn
- Origin and era: Creative/Education; implementation complexity medium
- Primary colours: Red Marker `#FF4D4D`, Pencil Black `#2D2D2D`
- Secondary colours: Warm Paper `#FDFBF7`, Old Paper `#E5E0D8`, Blue Ballpoint `#2D5DA1`, Post-it Yellow `#FFF9C4`
- Effects and animation: Wobbly borderRadius (unique per corner: 15/25/20/10), borderWidth 2–3 solid/dashed, hard offset shadow via rear View (`4px`,`4px`) `#2D2D2D`, Kalam Bold headings, PatrickHand Regular body, slight rotation (`-1deg`/`1deg`) on cards, absolute SVG scribble overlays (arrows/tape/tacks), jiggle `-2deg`↔`2deg` on error, LayoutAnimation spring on layout changes, Haptics on press, paper texture repeating background
- Best for: Low-fidelity prototyping, creative brands, children/picturebook apps, education tools, journaling apps, gamified puzzles
- Do not use for: Enterprise dashboards, high-density data tables, fintech precision tools, medical or legal apps
- Light mode supported; dark mode supported
- Performance: low cost; no heavy rendering drivers
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Low-Conversion
- Right-to-left support: full
- Design brief: Design a Sketch Hand-Drawn (Mobile) mobile interface using sketch, hand-drawn, handwriting, wobbly, imperfect, paper, kalam, organic. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `backgroundColor: '#FDFBF7'`, `cardBg: '#FFFFFF'`, `textPrimary: '#2D2D2D'`, `accentRed: '#FF4D4D'`, `accentBlue: '#2D5DA1'`, `accentYellow: '#FFF9C4'`, `border: '#2D2D2D'`, `shadowView: 'offset 4px 4px #2D2D2D'`, `wobblyRadius: [15,25,20,10]`, `fontHeading: 'Kalam-Bold'`, `fontBody: 'PatrickHand-Regular'`
- Implementation checklist: Warm paper background texture applied; Kalam Bold headings; Wobbly corner radii on all cards; Hard offset shadow View (not blur); Cards slightly rotated; Button press shifts to cover shadow; SVG tape/tack decorations; PatrickHand for inputs; Jiggle error animation; Minimum 48x48 touch targets
- Design-system variables: `--bg: #FDFBF7`, `--text: #2D2D2D`, `--accent-red: #FF4D4D`, `--accent-blue: #2D5DA1`, `--postit: #FFF9C4`, `--border-width: 3px`, `--shadow-offset: 4px 4px`, `--font-heading: Kalam Bold`, `--font-body: Patrick Hand`, `--rotation-card: -1deg to 1deg`
- Relationship: a specialised variant of Anti-Polish / Raw Aesthetic; start from the parent style's rules and apply these refinements

## 447. Neumorphism (Mobile)
- Keywords and mood: neumorphism, soft ui, dual shadow, extruded, inset, clay surface, monochromatic, cool grey, haptic, ceramic, physical, depth
- Origin and era: Tools/Lifestyle; implementation complexity medium
- Primary colours: Accent Violet `#6C63FF`, Clay Base `#E0E5EC`
- Secondary colours: Text Dark `#3D4852`, Text Muted `#6B7280`, Shadow Light `rgba(255,255,255,0.6)`, Shadow Dark `rgba(163,177,198,0.7)`, Inset Background `#D1D9E6`
- Effects and animation: Full-screen `#E0E5EC` base, dual-layer shadow via nested View (light top-left + dark bottom-right), extruded convex resting state, inset concave pressed/input state, Reanimated scale 0.97 on press, shadow opacity interpolates 1→0.4 on press, Haptics Light on every interaction, 8pt grid, no blur shadows (no shadowRadius blend), nested depth (extruded card contains inset icon slot)
- Best for: Minimal hardware controls, smart home apps, aesthetic utility tools, health monitors, brand showcase pages
- Do not use for: High-density data, bright multi-color apps, apps needing strong visual hierarchy via color, dark-mode-only products
- Light mode supported; dark mode not recommended
- Performance: low cost; no heavy rendering drivers
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Low-Conversion
- Right-to-left support: full
- Design brief: Design a Neumorphism (Mobile) mobile interface using neumorphism, soft ui, dual shadow, extruded, inset, clay surface, monochromatic, cool grey. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.
- Key properties and techniques: `backgroundColor: '#E0E5EC'`, `textPrimary: '#3D4852'`, `textMuted: '#6B7280'`, `accent: '#6C63FF'`, `shadowLight: 'rgba(255,255,255,0.6)'`, `shadowDark: 'rgba(163,177,198,0.7)'`, `insetBg: '#D1D9E6'`, `radiusCard: 32`, `radiusButton: 16`, `radiusPill: 999`, `shadowOffset: 6`, `shadowRadius: 10`
- Implementation checklist: Single `#E0E5EC` base applied across all screens; Dual shadow (light+dark) implemented via nested View; Extruded resting state on cards/buttons; Inset concave state on inputs; Scale 0.97 press + shadow opacity interpolation; Haptics Light on all presses; No black shadows or white backgrounds; Nested depth pattern (extruded→inset); Accent `#6C63FF` on active/focus only; 8pt grid spacing
- Design-system variables: `--bg: #E0E5EC`, `--text: #3D4852`, `--muted: #6B7280`, `--accent: #6C63FF`, `--shadow-light: rgba(255,255,255,0.6)`, `--shadow-dark: rgba(163,177,198,0.7)`, `--inset-bg: #D1D9E6`, `--radius-card: 32px`, `--radius-button: 16px`, `--font: Plus Jakarta Sans or System`
- Relationship: a specialised variant of Neumorphism; start from the parent style's rules and apply these refinements

# Part 47 — Platform Design Systems and Materials

## 448. Liquid Glass
- Keywords and mood: dynamic material, optical glass, translucency, lensing, refraction, fluid morphing, system navigation
- Also known as: Apple Liquid Glass
- Origin and era: Apple platforms, 2025; implementation complexity high
- Primary colours: Adaptive translucent material derived from surrounding content; use color judiciously
- Secondary colours: Semantic content and system tint colors; preserve legibility and hierarchy
- Effects and animation: Lensing and refraction, adaptive translucency, and fluid morph transitions aligned to Apple platform behavior
- Best for: Apple-platform navigation, controls, and system-aligned app chrome
- Do not use for: content layers, dense reading surfaces, or custom effects without accessibility fallbacks
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Apply Apple Liquid Glass sparingly to navigation and controls. Use dynamic translucent material, lensing, and fluid transitions while keeping content clear. Respect reduced transparency and reduced motion settings.
- Key properties and techniques: `platform material`, `adaptive translucency`, `lensing`, `refraction`, `reduced transparency`, `reduced motion`
- Implementation checklist: Use for navigation and controls; Keep content on a separate layer; Apply color judiciously; Test reduced transparency; Test reduced motion; Verify text and control contrast
- Design-system variables: `--material-role: navigation-controls`, `--translucency: adaptive`, `--tint: semantic`, `--reduced-transparency-fallback: opaque`, `--motion: platform-aligned`
- Native toolkits: swiftui, uikit, appkit

## 449. Fluent 2
- Keywords and mood: fluent 2, microsoft, enterprise, calm, rounded, tokenized, cross-platform, copilot
- Also known as: Fluent UI, Microsoft Fluent 2
- Origin and era: Microsoft Fluent 2, current; implementation complexity medium
- Primary colours: Fluent neutral palette with brand and status tokens
- Secondary colours: System semantic tokens; product brand accents
- Effects and animation: Subtle depth, calm transitions, platform-adaptive motion
- Best for: Microsoft 365, Windows, Copilot, and enterprise line-of-business tools
- Do not use for: Products that should not inherit Microsoft platform conventions
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a Fluent 2 product surface using calm hierarchy, standardized corners, semantic tokens, subtle depth, and platform-aware components. Preserve Microsoft interaction patterns and accessible focus states.
- Key properties and techniques: `design tokens`, `semantic color`, `component states`, `focus-visible`, `reduced motion`
- Implementation checklist: Use official tokens and components; preserve platform conventions; test keyboard, contrast, zoom, motion preferences, and responsive behavior
- Design-system variables: `--color-primary`, `--color-surface`, `--color-on-surface`, `--radius-control`, `--motion-duration`, `--focus-ring`

## 450. Shopify Polaris
- Keywords and mood: shopify polaris, merchant admin, commerce, checkout, web components, app home
- Also known as: Polaris, Polaris Web Components
- Origin and era: Shopify Polaris, current; implementation complexity medium
- Primary colours: Shopify admin semantic tokens and merchant brand accents
- Secondary colours: System semantic tokens; product brand accents
- Effects and animation: Purposeful admin feedback and restrained transitions
- Best for: Shopify admin apps, merchant tools, checkout, customer accounts, POS, and extensions
- Do not use for: Generic marketing sites or products outside Shopify surfaces
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a Shopify Polaris merchant workflow using official web components, admin-native hierarchy, clear actions, semantic status feedback, and consistent commerce patterns. Keep scope tied to Shopify surfaces.
- Key properties and techniques: `design tokens`, `semantic color`, `component states`, `focus-visible`, `reduced motion`
- Implementation checklist: Use official tokens and components; preserve platform conventions; test keyboard, contrast, zoom, motion preferences, and responsive behavior
- Design-system variables: `--color-primary`, `--color-surface`, `--color-on-surface`, `--radius-control`, `--motion-duration`, `--focus-ring`

## 451. Adobe Spectrum
- Keywords and mood: adobe spectrum, creative tools, enterprise, content creation, tokenized, cross-platform
- Also known as: Spectrum, Adobe Spectrum Design System
- Origin and era: Adobe Spectrum; implementation complexity medium
- Primary colours: Spectrum semantic colors with product-specific accents
- Secondary colours: System semantic tokens; product brand accents
- Effects and animation: Layered depth and restrained professional motion
- Best for: Creative tools, media workflows, document products, and Adobe-adjacent enterprise software
- Do not use for: Consumer brands that do not need dense professional-tool conventions
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design an Adobe Spectrum professional tool with tokenized color, precise hierarchy, dense but legible controls, strong focus states, and cross-platform component consistency.
- Key properties and techniques: `design tokens`, `semantic color`, `component states`, `focus-visible`, `reduced motion`
- Implementation checklist: Use official tokens and components; preserve platform conventions; test keyboard, contrast, zoom, motion preferences, and responsive behavior
- Design-system variables: `--color-primary`, `--color-surface`, `--color-on-surface`, `--radius-control`, `--motion-duration`, `--focus-ring`
- Native toolkits: spectrum-web-components, react-spectrum

## 452. Spectrum 2
- Keywords and mood: spectrum 2, adobe, expressive, approachable, adaptive, inclusive, creative tools
- Also known as: Adobe Spectrum 2, S2
- Origin and era: Adobe Spectrum 2, 2023+; implementation complexity medium
- Primary colours: Spectrum 2 semantic themes with updated contrast and personalization
- Secondary colours: System semantic tokens; product brand accents
- Effects and animation: Updated depth, expressive illustration, adaptive motion
- Best for: New Adobe-style creative and document surfaces adopting Spectrum 2
- Do not use for: Products not aligned with Adobe professional workflows
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation and blur
- Accessibility: conditional risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative
- Mobile-friendliness: adaptable (works on mobile with responsive adjustments)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design a Spectrum 2 professional surface with updated typography, approachable icons, layered depth, adaptive themes, and expressive but controlled visuals. Follow official Spectrum 2 tokens and component guidance.
- Key properties and techniques: `design tokens`, `semantic color`, `component states`, `focus-visible`, `reduced motion`
- Implementation checklist: Use official tokens and components; preserve platform conventions; test keyboard, contrast, zoom, motion preferences, and responsive behavior
- Design-system variables: `--color-primary`, `--color-surface`, `--color-on-surface`, `--radius-control`, `--motion-duration`, `--focus-ring`
- Native toolkits: custom, spectrum-web-components
- Relationship: a specialised variant of Adobe Spectrum; start from the parent style's rules and apply these refinements

## 453. Apple Native Experience
- Keywords and mood: apple native experience, native app, iOS, iPadOS, macOS, SwiftUI, UIKit, AppKit, Human Interface Guidelines, platform-aware, adaptive, semantic UI, system typography, native navigation
- Also known as: Apple Native, Native Apple UI, iOS-inspired interface
- Origin and era: Apple Human Interface Guidelines, 2007-present; implementation complexity medium
- Primary colours: Adaptive system backgrounds and grouped surfaces; semantic accent, label, separator, fill, and destructive colors; avoid hard-coded appearance assumptions
- Secondary colours: Secondary and tertiary labels, grouped content surfaces, control fills, accessible accent states, light/dark semantic mapping
- Effects and animation: Content-first hierarchy, system typography roles, 8pt-aligned spacing, restrained borders and shadows, platform-appropriate corner radii, SF Symbols-style consistent icons, adaptive light/dark appearance, purposeful `150-300ms` transitions, reduced-motion and reduced-transparency fallbacks
- Best for: Native-feeling phone, tablet, and desktop apps, productivity tools, settings, forms, lists, media and utility products, responsive web apps adopting platform-aware behavior
- Do not use for: Liquid Glass as the defining visual treatment, visionOS spatial interfaces, decorative blur or gradients, dense dashboards needing unrelated platform conventions, or web layouts that must behave identically on every platform
- Light mode supported; dark mode supported
- Performance: moderate cost; driven by animation
- Accessibility: low risk; always requires text contrast of at least `4.5:1`, full keyboard operability, visible focus states, a reduced-motion alternative, semantic controls, `44px` minimum touch targets
- Mobile-friendliness: native (designed mobile-first)
- Conversion focus: Medium
- Right-to-left support: full
- Design brief: Design an Apple Native Experience interface with system typography, semantic adaptive colors, platform-aware navigation, accessible controls, grouped lists, sheets, popovers, purposeful transitions, and responsive behavior across phone, tablet, desktop, and web. Do not require Liquid Glass, blur, or gradients.
- Key properties and techniques: `system-ui`, `-apple-system`, `BlinkMacSystemFont`, `SF Pro`, `SF Symbols`, `semantic color tokens`, `color-scheme: light dark`, `env(safe-area-inset-*)`, `:focus-visible`, `@media (prefers-reduced-motion)`, `@media (prefers-contrast)`, `min-width: 44px`, `border-radius: 10-16px`, `transition: 150-300ms ease-out`
- Implementation checklist: Use semantic roles for navigation bars, tab bars, sidebars, toolbars, buttons, segmented controls, toggles, text/search fields, sheets, popovers, menus, alerts, lists, and grouped content; preserve safe areas; provide keyboard and screen-reader semantics; verify light/dark contrast; test phone, tablet, desktop, reduced motion, and reduced transparency
- Design-system variables: `--color-bg: semantic system background`, `--color-surface: grouped surface`, `--color-label-primary: semantic primary label`, `--color-label-secondary: semantic secondary label`, `--color-accent: platform accent`, `--color-separator: semantic separator`, `--font-body: system-ui`, `--space-unit: 4px`, `--radius-control: 10px`, `--touch-target: 44px`, `--motion-duration: 150-300ms`, `--focus-ring: 2px`
- Native toolkits: swiftui, uikit, appkit, react-native, custom

# Part 48 — How to Derive a Design System from a Product Brief

## 454. Classify the Product First
- Start every design system by mapping the brief to exactly one product category (e.g. `SaaS (General)`, `Healthcare App`, `Ticketing / Box Office`); every later decision hangs off that category.
- Match on the product's nature and its keywords (e.g. `b2b`, `cloud`, `subscription` → `SaaS (General)`; `indie`, `solopreneur`, `side-project` → `Micro SaaS`), not on surface words like "dashboard" alone.
- Keep the user's original brief alongside the category: its wording later triggers conditional rules, dark-mode requests and page-type overrides.
- If no category fits, fall back to safe defaults: pattern `Hero + Features + CTA`, styles `Minimalism` + `Flat Design`, colour mood `Professional`, typography mood `Clean`, effects `Subtle hover transitions`, no anti-patterns, severity `MEDIUM`.

## 455. Read the Category's Reasoning Profile
- Each category supplies a recommended page pattern, an ordered style priority, a colour mood, a typography mood, key effects, conditional decision rules, anti-patterns and a severity.
- Style priority is an ordered list joined by `+`: the first entry is the preferred style, later entries are fallbacks or blends.
- Colour mood steers palette choice; typography mood steers font pairing; the pattern steers section order and CTA placement.
- Severity `HIGH` means the category's anti-patterns are hard constraints with real cost to trust or conversion; `MEDIUM` means they are strong defaults that a clear brief may bend.

## 456. Apply Conditional Decision Rules
- Rules map a condition to one or more actions; `must_have` conditions always fire, `if_*` conditions fire only when the brief contains one of their signal words.
- Signal words match as whole words, case-insensitively (`ux` does not fire inside "luxury").
- `style:` actions are prepended to the style priority, so a triggered style outranks the category's default first choice; multiple triggered styles keep their trigger order without duplicates.
- `constraint:` actions become explicit requirements (e.g. `case-studies`, `wcag-aaa`, `virtualize-lists`) and also bias palette, type and pattern selection toward matching options.
- `pattern:` actions replace the recommended pattern (the last triggered one wins); `mode:` actions force `dark` or `light` and override every other mode signal.
- Rules are declarative data: never treat a rule as executable or let it add anything outside these four action types.

## 457. Brief Signals That Trigger Rules
- `booking`: booking, appointment, calendar; `boutique`: boutique; `casual`: casual, playful; `checkout`: checkout, payment, purchase.
- `children`: child, children, kids; `collaboration`: collaboration, multiplayer, co-edit; `competitive`: competitive, leaderboard.
- `content focused`: content, article, reading, documentation; `conversion focused`: conversion, sales, signup, purchase.
- `creative field`: creative, artist, portfolio; `crop focused`: crop, farm, agriculture; `dashboard`: dashboard, operations, monitoring.
- `data heavy`: data heavy, data-heavy, analytics, large dataset; `delivery`: delivery, courier, shipping; `discovery focused`: discover, discovery, browse, directory.
- `engagement metric`: engagement, retention, contribution; `experience focused`: experience, immersive, journey; `gamification`: gamification, badges, streak.
- `health`: health, medical, patient; `hero needed`: hero, showcase, launch; `large dataset`: large dataset, thousands, millions.
- `light mode needed`: light mode, light theme; `low performance`: low performance, low-end, slow device; `luxury`: luxury, premium, high-end.
- `medication`: medication, medicine, prescription; `meditation`: meditation, breathing, mindfulness; `minimal portfolio`: minimal portfolio, simple portfolio.
- `mobile`: mobile, phone, tablet, ios, android; `personalized`: personalized, personalised, recommendation; `pre-launch`: pre-launch, prelaunch, coming soon, waitlist.
- `salary focused`: salary, compensation, pay range; `team collaboration`: team collaboration, team workspace; `trust needed`: trust, secure, verified, authority.
- `ux focused`: ux, usability, accessibility, accessible; `video ready`: video ready, product video, demo video.

## 458. Choose the Visual Style
- Canonical reasoning beats lexical similarity: walk the (rule-adjusted) style priority in order and use the first style that exists and is active.
- A deprecated style resolves to its parent style; a style with no live parent is skipped.
- Only if no priority style resolves, score candidate styles: `+10` when every word of a priority entry appears in the style name, `+3` when it overlaps the style's keywords, `+1` for any loose word match; the highest score wins, otherwise the closest overall match.
- Retrieve candidates using the brief, the category, any triggered constraints and the first two priority styles together.
- Default when nothing resolves: `Minimalism & Swiss Style`.

## 459. Resolve Light or Dark Mode Before Picking Colours
- Decide the mode once and make palette, style labels and anti-patterns agree with it; never ship a dark-first style on a light palette next to "avoid dark mode" advice.
- Precedence: a rule-forced mode → an explicit dark request in the brief (`dark mode`, `dark theme`, `dark ui`, `dark-mode`, `darkmode`, `night mode`, `midnight`, `oled`) → a dark-first style → otherwise `light`.
- A style is dark-first when its preferred mode is `dark`, when light is not recommended but dark is supported, or when its mode notes say dark mode primary, dark primary, dark-only, dark preferred, dark focused, dark-first, dark rich, or "light mode only as exception".
- "Dark-capable" (works in both) is not dark-first and does not flip the mode.

## 460. Pick a Palette That Matches the Mode
- Prefer the palette built for the product category itself; otherwise use the best colour-mood match.
- A palette counts as dark when its background's relative luminance is below `0.18` (lightest dark background ≈ `0.026`, darkest light background ≈ `0.79`).
- In dark mode with a light category palette, keep the brand tokens (primary, secondary, accent, destructive) and derive dark surfaces: background `#0F172A`, foreground `#F8FAFC`, card `#111827`, card foreground `#F8FAFC`, muted `#1E293B`, muted foreground `#CBD5E1`, border `#334155`.
- The derived focus ring is the first of ring, accent or primary that reaches `3:1` contrast against `#0F172A`, else `#60A5FA`.
- In dark mode without a category palette, take the first dark palette among the best matches; in light mode take the top match.
- Fallback brand values: primary `#2563EB`, secondary `#3B82F6`, accent/CTA `#F97316`, background `#F8FAFC`, foreground `#1E293B`.

## 461. Express Colour as Semantic Tokens
- Define every colour by role, never by raw hex in components: `--color-primary`, `--color-on-primary`, `--color-secondary`, `--color-on-secondary`, `--color-accent`, `--color-on-accent`.
- Surface roles: `--color-background`, `--color-foreground`, `--color-card`, `--color-card-foreground`, `--color-muted`, `--color-muted-foreground`, `--color-border`.
- State roles: `--color-destructive`, `--color-on-destructive`, `--color-ring`.
- The accent role is the CTA colour; its "on" token is the CTA text colour (white if unspecified).
- Keep palette notes with the tokens so intent (e.g. why a gold accent exists) survives handoff.

## 462. Choose Typography from the Mood
- Combine the category's typography mood with the brief and constraints to pick the best-fitting heading/body pairing.
- Record heading font, body font, mood keywords, best-for context and the font import alongside the pairing.
- Default pairing when nothing fits: `Inter` for both heading and body.

## 463. Lock the Page Pattern
- The category's recommended pattern is the contract for the landing page; when it names a known pattern exactly, use it directly rather than blending it with the brief's wording.
- Capture the pattern's section order, primary CTA placement, colour strategy and conversion tactic.
- Defaults when unspecified: sections `Hero > Features > CTA`, CTA placement `Above fold`.

## 464. Settle Effects and Motion
- A chosen style's own effects and animation guidance take precedence; the category's key effects apply only when the style specifies none.
- Hover and state transitions sit in the `150-300ms` window; buttons and cards use `200ms ease`.
- Always respect `prefers-reduced-motion`.

## 465. Reconcile Anti-Patterns with the Resolved Mode
- Anti-patterns are `+`-separated clauses; present each as a separate "do not".
- When the resolved mode is dark, drop clauses that warn against dark mode (any clause mentioning `dark mode`, `dark modes` or `dark theme`).
- When the mode stays light and the category warns against dark mode, label a dark-capable style's dark support as "supported, but avoid for this product".

## 466. Tune with Design Dials
- Three optional `1-10` dials bias the system without replacing category reasoning; each buckets into `1-3`, `4-7`, `8-10`.
- Variance: `1-3` Centered / Minimal (minimalism, exaggerated minimalism, centered, symmetric, grid-based); `4-7` Balanced / Modern (modern, structured, balanced); `8-10` Bold / Asymmetric (brutalism, bento grids, asymmetric, experimental); dial keywords are placed ahead of the style priority.
- Motion: `1-3` Subtle, `4-7` Standard, `8-10` Complex; pick a motion recipe of that intensity tier.
- Density sets the spacing scale (see Spacing Scale); unset dials leave the defaults untouched.

## 467. Spacing Scale
- Standard (density `4-7`, default): xs `4px`, sm `8px`, md `16px`, lg `24px`, xl `32px`, 2xl `48px`, 3xl `64px`.
- Spacious (density `1-3`): xs `4px`, sm `8px`, md `24px`, lg `32px`, xl `48px`, 2xl `64px`, 3xl `96px`.
- Dense / Dashboard (density `8-10`): xs `2px`, sm `4px`, md `8px`, lg `12px`, xl `16px`, 2xl `24px`, 3xl `32px`.
- Usage: xs tight gaps, sm icon gaps and inline spacing, md standard padding, lg section padding, xl large gaps, 2xl section margins, 3xl hero padding; express each also in rem (px ÷ 16).

## 468. Shadow Depths
- `--shadow-sm` `0 1px 2px rgba(0,0,0,0.05)` for subtle lift.
- `--shadow-md` `0 4px 6px rgba(0,0,0,0.1)` for cards and buttons.
- `--shadow-lg` `0 10px 15px rgba(0,0,0,0.1)` for modals and dropdowns.
- `--shadow-xl` `0 20px 25px rgba(0,0,0,0.15)` for hero images and featured cards.

## 469. Baseline Component Specs
- Primary button: accent/CTA background, on-accent text, padding `12px 24px`, radius `8px`, weight `600`, `transition: all 200ms ease`, pointer cursor; hover `opacity: 0.9` + `translateY(-1px)`.
- Secondary button: transparent fill, `2px` primary border, same padding/radius/weight; text uses primary only if it reaches `4.5:1` against the background, otherwise the foreground colour.
- Card: background surface, radius `12px`, padding `24px`, `--shadow-md`, `200ms` transition; hover `--shadow-lg` + `translateY(-2px)`.
- Input: padding `12px 16px`, `1px solid #E2E8F0`, radius `8px`, font size `16px`; focus swaps border to primary and adds a `3px` primary ring at ~12% opacity instead of the default outline.
- Modal: overlay `rgba(0,0,0,0.5)` with `blur(4px)`; panel radius `16px`, padding `32px`, `--shadow-xl`, `max-width: 500px`, `width: 90%`.

## 470. Master Rules with Page Overrides
- Keep one master design system for the product; a page-specific rule set overrides the master only where it deviates, and everything else inherits.
- Never silently replace an existing master: review prior decisions first and overwrite only deliberately.
- Detect page type from the page name and brief, first match wins: dashboard/admin/analytics/data/metrics/stats/monitor/overview → Dashboard / Data View; checkout/payment/cart/purchase/order/billing → Checkout / Payment; settings/profile/account/preferences/config → Settings / Profile.
- Continue: landing/marketing/homepage/hero/home/promo → Landing / Marketing; login/signin/signup/register/auth/password → Authentication; pricing/plans/subscription/tiers/packages → Pricing / Plans; blog/article/post/news/content/story → Blog / Article.
- Continue: product/item/detail/pdp/shop/store → Product Detail; search/results/browse/filter/catalog/list → Search Results; empty/404/error/not found/zero → Empty State; otherwise infer from the page's best-fit style (dashboard/data → Dashboard, landing/marketing → Landing) or `General`.
- Layout by page style: data/dense/dashboard/grid → max width `1400px` or full width, 12-column grid, high density; minimal/simple/clean/single → `800px` single centred column, low density; otherwise `1200px` with full-width sections and centred content.

## 471. Universal Forbidden Patterns
- No emojis as icons; use one consistent SVG icon set.
- Every clickable element gets `cursor: pointer`.
- No layout-shifting hover (avoid scale transforms that move surrounding content).
- Text contrast at least `4.5:1`; focus states always visible.
- No instant state changes; transition in `150-300ms`.

## 472. Pre-Delivery Checklist
- Icons are SVG from one consistent set, never emojis.
- Pointer cursor and smooth hover states (`150-300ms`) on all interactive elements.
- Light-mode text contrast `4.5:1` minimum; visible keyboard focus states.
- `prefers-reduced-motion` respected.
- Responsive at `375px`, `768px`, `1024px`, `1440px`; no content hidden behind fixed navbars; no horizontal scroll on mobile.

## 473. Right-to-Left Readiness Levels
- `full`: the style or product mirrors cleanly with no directional rework.
- `partial`: it mirrors, but icons, carousels, motion paths and charts need per-component checks.
- `caveats`: it encodes reading direction (timelines, maps, keyboards, swipe or seat flows); say so before recommending it and propose a mirrorable alternative for strict RTL builds.
- For RTL briefs (Arabic, Hebrew, Persian, Urdu), restrict choices to `full` rows when safety matters most.

# Part 49 — SaaS, B2B & Business Tools

## 474. SaaS (General)
- Recommended pattern: `Hero + Features + CTA`
- Style priority: `Glassmorphism` → `Flat Design`; secondary `Soft UI Evolution`, `Minimalism & Swiss Style`
- Colour mood: `Trust blue + Accent contrast`
- Typography mood: `Professional + Hierarchy`
- Key effects: `Subtle hover (200-250ms)`; `Smooth transitions`
- Landing & dashboard: landing `Hero + Features + CTA`; dashboard `Data-Dense + Real-Time Monitoring`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → lead with `Minimalism & Swiss Style` style; If data heavy (brief mentions data heavy, data-heavy, analytics, large dataset) → lead with `Glassmorphism` style
- Anti-patterns (`HIGH`): avoid `Excessive animation`; `Dark mode by default`
- Key considerations: Balance modern feel with clarity. Focus on CTAs.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 475. Micro SaaS
- Recommended pattern: `Hero-Centric + Trust`
- Style priority: `Motion-Driven` → `Vibrant & Block-based`; primary recommendation `Flat Design` + `Vibrant & Block-based`; secondary `Motion-Driven`, `Micro-interactions`
- Colour mood: `Bold primaries + Accent contrast`; palette focus `Vibrant primary + white space`
- Typography mood: `Modern + Energetic typography`
- Key effects: `Scroll-triggered animations`; `Parallax`
- Landing & dashboard: landing `Minimal & Direct + Demo`; dashboard `Executive Dashboard`
- Decision rules: If pre launch (brief mentions pre-launch, prelaunch, coming soon, waitlist) → switch to `Waitlist/Coming Soon` pattern; If video ready (brief mentions video ready, product video, demo video) → `add hero video`
- Anti-patterns (`HIGH`): avoid `Static design`; `No video`; `Poor mobile`
- Key considerations: Keep simple, show product quickly. Speed is key.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 476. B2B Service
- Recommended pattern: `Feature-Rich Showcase + Trust`
- Style priority: `Accessible & Ethical` → `Minimalism & Swiss Style`; secondary `Bento Box Grid`, `Micro-interactions`
- Colour mood: `Professional blue + Neutral grey`
- Typography mood: `Formal + Clear typography`
- Key effects: `Section transitions`; `Feature reveals`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `Sales Intelligence Dashboard`
- Decision rules: Always → `case studies`, `roi messaging`
- Anti-patterns (`HIGH`): avoid `Playful design`; `Hidden credentials`; `AI purple/pink gradients`
- Key considerations: Credibility essential. Clear ROI messaging.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 477. Productivity Tool
- Recommended pattern: `Interactive Demo + Feature-Rich`
- Style priority: `Flat Design` → `Micro-interactions`; secondary `Minimalism & Swiss Style`, `Soft UI Evolution`
- Colour mood: `Clear hierarchy + Functional colors`
- Typography mood: `Clean + Efficient typography`
- Key effects: `Quick actions (150ms)`; `Task animations`
- Landing & dashboard: landing `Interactive Product Demo`; dashboard `Drill-Down Analytics`
- Decision rules: Always → `keyboard shortcuts`; If collaboration (brief mentions collaboration, multiplayer, co-edit) → `add real time cursors`
- Anti-patterns (`HIGH`): avoid `Complex onboarding`; `Slow performance`
- Key considerations: Ease of use. Speed & efficiency focus.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 478. Remote Work/Collaboration Tool
- Recommended pattern: `Feature-Rich + Real-Time`
- Style priority: `Soft UI Evolution` → `Minimalism & Swiss Style`; secondary `Glassmorphism`, `Micro-interactions`
- Colour mood: `Calm Blue + Neutral grey`
- Typography mood: `Clean + Readable typography`
- Key effects: `Real-time presence indicators`; `Notification badges`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `Drill-Down Analytics`
- Decision rules: Always → `status indicators`, `video integration`
- Anti-patterns (`HIGH`): avoid `Cluttered interface`; `No presence`
- Key considerations: Real-time collaboration. Status indicators. Video integration. Notification management.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 479. CRM & Client Management
- Recommended pattern: `Feature-Rich Showcase + Demo`
- Style priority: `Flat Design` → `Minimalism & Swiss Style`; secondary `Soft UI Evolution`, `Micro-interactions`
- Colour mood: `Professional blue + pipeline stage colors + closed-won green`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase + Demo`; dashboard `Sales Intelligence Dashboard`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Complex shadows`; `3D effects`
- Key considerations: Contact card list with avatar. Pipeline kanban board. Activity timeline. Quick-log (call/email/meeting). Deal amount + probability. Tag/segment filter. Mobile quick-actions.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 480. Inventory & Stock Management
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Flat Design` → `Minimalism & Swiss Style`; secondary `Dark Mode (OLED)`, `Accessible & Ethical`
- Colour mood: `Functional neutral + status traffic-light (green/amber/red) + scanner accent`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `Real-Time Monitoring + Data-Dense`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Complex shadows`; `3D effects`
- Key considerations: Product list/grid with thumbnails. Barcode/QR scanner. Stock level badges. Low-stock alert banner. Category/location filter. Batch edit. Reorder trigger. Audit log.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 481. Booking & Appointment App
- Recommended pattern: `Conversion-Optimized`
- Style priority: `Soft UI Evolution` → `Flat Design`; secondary `Minimalism & Swiss Style`, `Micro-interactions`
- Colour mood: `Trust blue + available green + booked grey + confirm accent`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Conversion-Optimized`; dashboard `Drill-Down Analytics`
- Decision rules: If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`
- Key considerations: Calendar strip or month picker. Available time-slot grid. Service + staff selector. Confirmation summary. Reminder push. Reschedule/cancel flow. Two-sided (provider ↔ client).
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 482. Invoice & Billing Tool
- Recommended pattern: `Conversion-Optimized + Trust`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Swiss Modernism 2.0`, `Accessible & Ethical`
- Colour mood: `Professional navy + paid green + overdue red + neutral grey`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Conversion-Optimized + Trust`; dashboard `Financial Dashboard`
- Decision rules: If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Complex shadows`; `3D effects`
- Key considerations: Invoice template with line items. Tax/discount calculation. Status badges (Draft/Sent/Paid/Overdue). PDF export + share. Payment link generation. Client address book. Recurring invoices.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 483. E-signature / Document Workflow
- Recommended pattern: `Enterprise Gateway`
- Style priority: `Minimalism & Swiss Style` → `Accessible & Ethical`; primary recommendation `Accessible & Ethical` + `Minimalism & Swiss Style`; secondary `Accessible & Ethical`, `Flat Design`
- Colour mood: `Trust navy + signature green + pending amber + neutral grey`
- Typography mood: `Professional + Document-readable typography`
- Key effects: `Signature placement highlights`; `audit trail states`
- Landing & dashboard: landing `Feature-Rich Showcase + Conversion`; dashboard `Document Pipeline Dashboard`
- Decision rules: Always → `document preview`, `signature placement`, `multi signer flow`, `audit trail`, `compliance badges`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Confusing signing flow`; `weak audit trail`; `hidden consent`
- Key considerations: Document preview with annotation. Signature placement UI. Multi-signer workflow. Audit trail. Compliance badges. Mobile signing. Expiry reminders.
- Rationale: signing flows live on trust, legibility, and irreversible action clarity (confidence `0.93`)
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 484. No-code / Low-code Builder
- Recommended pattern: `Product Demo + Features`
- Style priority: `Vibrant & Block-based` → `Bento Box Grid`; secondary `Motion-Driven`, `Glassmorphism`
- Colour mood: `Brand primary + component palette colors + canvas neutral + connect blue`
- Typography mood: `Functional + UI-focused typography`
- Key effects: `Drag-drop canvas`; `live preview sync`
- Landing & dashboard: landing `Interactive Product Demo`; dashboard `App Builder Workspace`
- Decision rules: Always → `drag drop canvas`, `component sidebar`, `logic flow editor`, `live preview`, `template gallery`; If dashboard (brief mentions dashboard, operations, monitoring) → `virtualize lists`; If ux focused (brief mentions ux, usability, accessibility, accessible) → `add progress animation`
- Anti-patterns (`HIGH`): avoid `No live preview`; `hidden logic`; `sluggish canvas`
- Key considerations: Drag-drop canvas. Component library sidebar. Logic flow visual editor. Preview pane. Template gallery. Publish button. Version history.
- Rationale: builders need visual affordance density without sacrificing preview fidelity or performance (confidence `0.89`)
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 485. Survey / Form Builder
- Recommended pattern: `Product Demo + Features`
- Style priority: `Minimalism & Swiss Style` → `Micro-interactions`; secondary `Claymorphism`, `Flat Design`
- Colour mood: `Clean white + question accent + progress green + submit blue`
- Typography mood: `Clear + Form-first typography`
- Key effects: `Conditional-logic flow`; `progress animation`
- Landing & dashboard: landing `Interactive Product Demo`; dashboard `Response Analytics Dashboard`
- Decision rules: Always → `drag drop builder`, `question library`, `conditional logic`, `theme picker`, `response dashboard`; If ux focused (brief mentions ux, usability, accessibility, accessible) → `add progress animation`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Static forms`; `hidden conditional logic`; `weak progress cues`
- Key considerations: Drag-drop form builder. Question type library. Conditional logic visualizer. Theme picker. Response dashboard with charts. Export CSV. Share link/QR/embed.
- Rationale: form builders need visible logic, easy composition, and response clarity (confidence `0.92`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

# Part 50 — Data, Monitoring & Operations

## 486. Analytics Dashboard
- Recommended pattern: `Data-Dense + Drill-Down`
- Style priority: `Data-Dense Dashboard` → `Heat Map & Heatmap Style`; secondary `Minimalism & Swiss Style`, `Dark Mode (OLED)`
- Colour mood: `Cool→Hot gradients + Neutral grey`
- Typography mood: `Clear + Functional typography`
- Key effects: `Hover tooltips`; `Chart zoom`; `Filter animations`
- Landing & dashboard: landing `N/A - Analytics focused`; dashboard `Drill-Down Analytics + Comparative`
- Decision rules: Always → `data export`; If large dataset (brief mentions large dataset, thousands, millions) → `virtualize lists`
- Anti-patterns (`HIGH`): avoid `Ornate design`; `No filtering`
- Key considerations: Clarity > aesthetics. Color-coded data priority.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 487. Smart Home/IoT Dashboard
- Recommended pattern: `Real-Time Monitoring`
- Style priority: `Glassmorphism` → `Dark Mode (OLED)`; secondary `Minimalism & Swiss Style`, `AI-Native UI`
- Colour mood: `Dark + Status indicator colors`
- Typography mood: `Clear + Functional typography`
- Key effects: `Device status pulse`; `Quick action animations`
- Landing & dashboard: landing `Interactive Product Demo`; dashboard `Real-Time Monitoring`
- Decision rules: Always → `real time controls`, `energy monitoring`
- Anti-patterns (`HIGH`): avoid `Slow updates`; `No automation`
- Key considerations: Device status. Real-time controls. Energy monitoring. Automation rules. Quick actions.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 488. Logistics/Delivery
- Recommended pattern: `Feature-Rich Showcase + Real-Time`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Dark Mode (OLED)`, `Micro-interactions`
- Colour mood: `Blue (#2563EB) + Orange (tracking) + Green`; palette focus `Blue (#2563EB) + Orange (tracking) + Green (delivered)`
- Typography mood: `Clear + Functional typography`
- Key effects: `Real-time tracking animation`; `Status pulse`
- Landing & dashboard: landing `Feature-Rich Showcase + Conversion`; dashboard `Real-Time Monitoring + Route Analytics`
- Decision rules: Always → `tracking map`, `delivery updates`
- Anti-patterns (`HIGH`): avoid `Static tracking`; `No map integration`; `AI purple/pink gradients`
- Key considerations: Real-time tracking. Delivery scheduling. Route optimization. Driver management. Status updates. Map integration.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 489. Autonomous Drone Fleet Manager
- Recommended pattern: `Real-Time + Feature-Rich`
- Style priority: `HUD / Sci-Fi FUI` → `Real-Time Monitoring`; primary recommendation `HUD / Sci-Fi FUI`; secondary `Real-Time Monitoring`, `Spatial UI (VisionOS)`
- Colour mood: `Tactical Green + Alert Red + Map Dark`; palette focus `Tactical Green #00FF00 + Alert Red + Map Dark`
- Typography mood: `Technical + Functional typography`
- Key effects: `Telemetry animations`; `3D spatial awareness`
- Landing & dashboard: landing `Real-Time Monitor`; dashboard `Geographic + Real-Time`
- Decision rules: Always → `real time telemetry`, `safety alerts`
- Anti-patterns (`HIGH`): avoid `Slow updates`; `Poor spatial viz`
- Key considerations: Real-time telemetry. 3D spatial awareness. Latency indicators. Safety alerts.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 490. Status Page / Incident Management
- Recommended pattern: `Real-Time / Operations Landing`
- Style priority: `Dark Mode (OLED)` → `Data-Dense Dashboard`; primary recommendation `Data-Dense Dashboard` + `Real-Time Monitoring`; secondary `Minimalism & Swiss Style`, `Dark Mode (OLED)`
- Colour mood: `Status green + incident red + maintenance amber + neutral dark`
- Typography mood: `Functional + Status typography`
- Key effects: `Status matrix`; `incident timeline transitions`
- Landing & dashboard: landing `Timeline + Severity Indicators`; dashboard `Real-Time Monitoring + Timeline`
- Decision rules: Always → `service status matrix`, `incident timeline`, `severity badges`, `maintenance schedule`, `uptime history`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`; If dashboard (brief mentions dashboard, operations, monitoring) → `red alert colors`
- Anti-patterns (`HIGH`): avoid `Slow dashboards`; `decorative charts`; `hidden error states`
- Key considerations: Service status matrix. Incident timeline. Severity badges. Maintenance schedule. SLA uptime history. Email/SMS subscribe.
- Rationale: operators need instant state recognition and a reliable incident chronology (confidence `0.94`)
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 491. RPA / Automation Dashboard
- Recommended pattern: `Real-Time / Operations Landing`
- Style priority: `Dark Mode (OLED)` → `Data-Dense Dashboard`; secondary `Minimalism & Swiss Style`, `Accessible & Ethical`
- Colour mood: `Dark bg + running green + failed red + queued amber + completed blue`
- Typography mood: `Functional + Operational typography`
- Key effects: `Status matrix`; `alert transitions`
- Landing & dashboard: landing `Bot Fleet Dashboard`; dashboard `Real-Time Monitoring + Process Analytics`
- Decision rules: Always → `bot status grid`, `queue depth`, `process flow`, `exception alerts`, `roi metrics`; If dashboard (brief mentions dashboard, operations, monitoring) → `virtualize lists`; If trust needed (brief mentions trust, secure, verified, authority) → `red alert colors`
- Anti-patterns (`HIGH`): avoid `Slow dashboards`; `decorative charts`; `hidden error states`
- Key considerations: Bot status grid (running/idle/failed). Queue depth. Process flow visualization. Exception handling alert. ROI metrics. Bot scheduling calendar. Audit trail.
- Rationale: automation ops need dense state surfaces, failure visibility, and ROI proof (confidence `0.93`)
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

# Part 51 — AI & Developer Tools

## 492. Design System/Component Library
- Recommended pattern: `Feature-Rich + Documentation`
- Style priority: `Minimalism & Swiss Style` → `Accessible & Ethical`; secondary `Flat Design`, `Zero Interface`
- Colour mood: `Clear hierarchy + Code-like structure`
- Typography mood: `Monospace + Clear typography`
- Key effects: `Code copy animations`; `Component previews`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `N/A - Dev focused`
- Decision rules: Always → `search`, `code examples`
- Anti-patterns (`HIGH`): avoid `Poor documentation`; `No live preview`
- Key considerations: Consistency. Developer-first approach.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 493. AI/Chatbot Platform
- Recommended pattern: `Interactive Demo + Minimal`
- Style priority: `AI-Native UI` → `Minimalism & Swiss Style`; secondary `Zero Interface`, `Glassmorphism`
- Colour mood: `Neutral + AI Purple (#6366F1)`
- Typography mood: `Modern + Clear typography`
- Key effects: `Streaming text`; `Typing indicators`; `Fade-in`
- Landing & dashboard: landing `Interactive Product Demo`; dashboard `AI/ML Analytics Dashboard`
- Decision rules: Always → `conversational ui`, `context awareness`
- Anti-patterns (`HIGH`): avoid `Heavy chrome`; `Slow response feedback`
- Key considerations: Conversational UI. Streaming text. Context awareness. Minimal chrome.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 494. Knowledge Base/Documentation
- Recommended pattern: `FAQ + Minimal`
- Style priority: `Minimalism & Swiss Style` → `Accessible & Ethical`; secondary `Swiss Modernism 2.0`, `Flat Design`
- Colour mood: `Clean hierarchy + Minimal color`
- Typography mood: `Clear + Readable typography`
- Key effects: `Search highlight`; `Smooth scrolling`
- Landing & dashboard: landing `FAQ/Documentation`; dashboard `N/A - Documentation focused`
- Decision rules: Always → `search first`, `version switching`
- Anti-patterns (`HIGH`): avoid `Poor navigation`; `No search`
- Key considerations: Search-first. Clear navigation. Code highlighting. Version switching. Feedback system.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 495. Cybersecurity Platform
- Recommended pattern: `Trust & Authority + Real-Time`
- Style priority: `Cyberpunk UI` → `Dark Mode (OLED)`; secondary `Neubrutalism`, `Minimalism & Swiss Style`
- Colour mood: `Matrix Green (#00FF00) + Deep Black`; palette focus `Matrix Green + Deep Black + Terminal feel`
- Typography mood: `Technical + Clear typography`
- Key effects: `Threat visualization`; `Alert animations`
- Landing & dashboard: landing `Trust & Authority + Real-Time`; dashboard `Real-Time Monitoring + Heat Map`
- Decision rules: Always → `real time monitoring`, `threat display`
- Anti-patterns (`HIGH`): avoid `Light mode`; `Poor data viz`
- Key considerations: Data density. Threat visualization. Dark mode default.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 496. Developer Tool / IDE
- Recommended pattern: `Minimal + Documentation`
- Style priority: `Dark Mode (OLED)` → `Minimalism & Swiss Style`; secondary `Flat Design`, `Bento Box Grid`
- Colour mood: `Dark syntax theme + Blue focus`; palette focus `Dark syntax theme colors + Blue focus`
- Typography mood: `Monospace + Functional typography`
- Key effects: `Syntax highlighting`; `Command palette`
- Landing & dashboard: landing `Minimal & Direct + Documentation`; dashboard `Real-Time Monitor + Terminal`
- Decision rules: Always → `keyboard shortcuts`, `documentation`
- Anti-patterns (`HIGH`): avoid `Light mode default`; `Slow performance`
- Key considerations: Keyboard shortcuts. Syntax highlighting. Fast performance.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 497. API Developer Portal
- Recommended pattern: `FAQ/Documentation Landing`
- Style priority: `Minimalism & Swiss Style` → `Glassmorphism`; primary recommendation `Accessible & Ethical` + `Minimalism & Swiss Style`; secondary `Glassmorphism`, `Dark Mode (OLED)`
- Colour mood: `Dark code theme + Brand accent + Syntax colors`
- Typography mood: `Monospace + Clear typography`
- Key effects: `Syntax highlighting`; `Copy-to-clipboard samples`
- Landing & dashboard: landing `Quick Start + Interactive Docs`; dashboard `N/A - Documentation focused`
- Decision rules: Always → `endpoint discoverability`, `code samples`, `auth flow clarity`, `version switching`, `rate limit visibility`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`; If ux focused (brief mentions ux, usability, accessibility, accessible) → lead with `Flat Design` style
- Anti-patterns (`HIGH`): avoid `Buried endpoints`; `Broken version switching`; `missing rate-limit state`
- Key considerations: Endpoint discoverability. Copy-paste code samples. Auth flow clarity. Version switching. Interactive playground. Rate limit visibility.
- Rationale: developer docs win on immediate code reuse and predictable auth/version discovery (confidence `0.92`)
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 498. Changelog / Release Notes
- Recommended pattern: `Newsletter / Content First`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Swiss Modernism 2.0`, `Editorial Grid / Magazine`
- Colour mood: `Neutral bg + version badge colors + date grey`; palette focus `Neutral bg + version badge colors (feat=green, fix=blue, breaking=red) + date grey`
- Typography mood: `Neutral + Versioned hierarchy`
- Key effects: `Timeline transitions`; `version badges`
- Landing & dashboard: landing `Timeline + Version List`; dashboard `N/A - Documentation focused`
- Decision rules: Always → `chronological feed`, `semver badges`, `breaking change warnings`, `copy paste install`, `version search`; If content focused (brief mentions content, article, reading, documentation) → `prioritize clarity`; If low performance (brief mentions low performance, low-end, slow device) → `reduce motion`
- Anti-patterns (`MEDIUM`): avoid `No chronological order`; `no version tags`; `noisy marketing copy`
- Key considerations: Chronological release feed. Semver badges. Breaking change warnings. Copy-paste install commands. Subscribe to feed. Search by version.
- Rationale: release notes should be skimmable, versioned, and safe to scan for breaking changes (confidence `0.90`)
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 499. Feature Flag / Config Management
- Recommended pattern: `Product Demo + Features`
- Style priority: `Dark Mode (OLED)` → `Data-Dense Dashboard`; secondary `Minimalism & Swiss Style`, `Accessible & Ethical`
- Colour mood: `Dark bg + enabled green + disabled grey + experimental amber + kill-switch red`
- Typography mood: `Functional + Technical typography`
- Key effects: `Toggle state transitions`; `rollout sliders`
- Landing & dashboard: landing `Feature List + Toggle Panel`; dashboard `N/A - Config focused`
- Decision rules: Always → `feature toggle list`, `rollout slider`, `environment switcher`, `targeting rules`, `kill switch`; If dashboard (brief mentions dashboard, operations, monitoring) → `virtualize lists`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`
- Anti-patterns (`HIGH`): avoid `Decorative visuals`; `ambiguous toggle states`; `slow performance`
- Key considerations: Feature list with on/off toggles. Percentage rollout slider. Environment selector (prod/staging). User targeting rules. Kill switch. Audit log.
- Rationale: config tools need dense state visibility and unambiguous rollout control (confidence `0.91`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 500. Open Source Project Landing
- Recommended pattern: `Hero + Features + CTA`
- Style priority: `Flat Design` → `Minimalism & Swiss Style`; primary recommendation `Dark Mode (OLED)` + `Minimalism & Swiss Style`; secondary `Accessible & Ethical`, `Flat Design`
- Colour mood: `Dark bg + language color bar + star gold + fork silver + sponsor purple`
- Typography mood: `Technical + Clear typography`
- Key effects: `Install-command copy`; `contributor stats`
- Landing & dashboard: landing `Hero + Install + Contribute`; dashboard `Contributor Analytics Dashboard`
- Decision rules: Always → `install command`, `contributor stats`, `language bar`, `issue pr status`, `sponsor cta`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`; If content focused (brief mentions content, article, reading, documentation) → lead with `Flat Design` style
- Anti-patterns (`MEDIUM`): avoid `No install command`; `weak contributor proof`; `marketing fluff`
- Key considerations: Star/fork count badges. Install command (copy-paste). Language breakdown bar. Top contributors grid. Sponsor CTA. Documentation link. Issue/pr status.
- Rationale: open-source landings succeed when setup, social proof, and maintenance status are immediate (confidence `0.90`)
- RTL: `full` — mirrors cleanly; no directional rework needed

# Part 52 — Fintech & Finance

## 501. Financial Dashboard
- Recommended pattern: `Data-Dense Dashboard`
- Style priority: `Dark Mode (OLED)` → `Data-Dense Dashboard`; secondary `Minimalism & Swiss Style`, `Accessible & Ethical`
- Colour mood: `Dark bg + Red/Green alerts + Trust blue`
- Typography mood: `Clear + Readable typography`
- Key effects: `Real-time number animations`; `Alert pulse`
- Landing & dashboard: landing `N/A - Dashboard focused`; dashboard `Financial Dashboard`
- Decision rules: Always → `real time updates`, `high contrast`
- Anti-patterns (`HIGH`): avoid `Light mode default`; `Slow rendering`
- Key considerations: High contrast, real-time updates, accuracy paramount.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 502. Fintech/Crypto
- Recommended pattern: `Trust & Authority`
- Style priority: `Minimalism & Swiss Style` → `Accessible & Ethical`; primary recommendation `Glassmorphism` + `Dark Mode (OLED)`; secondary `Retro-Futurism`, `Motion-Driven`
- Colour mood: `Navy + Trust Blue + Gold`; palette focus `Dark tech colors + trust + vibrant accents`
- Typography mood: `Professional + Trustworthy`
- Key effects: `Smooth state transitions`; `Number animations`
- Landing & dashboard: landing `Conversion-Optimized`; dashboard `Real-Time Monitoring + Predictive`
- Decision rules: Always → `security first`; If dashboard (brief mentions dashboard, operations, monitoring) → force `dark` mode
- Anti-patterns (`HIGH`): avoid `Playful design`; `Unclear fees`; `AI purple/pink gradients`
- Key considerations: Security perception. Real-time data critical.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 503. NFT/Web3 Platform
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Cyberpunk UI` → `Glassmorphism`; secondary `Aurora UI`, `3D & Hyperrealism`
- Colour mood: `Dark + Neon + Gold (#FFD700)`
- Typography mood: `Bold + Modern typography`
- Key effects: `Wallet connect animations`; `Transaction feedback`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `Crypto/Blockchain Dashboard`
- Decision rules: Always → `wallet integration`, `gas fees display`
- Anti-patterns (`HIGH`): avoid `Light mode default`; `No transaction status`
- Key considerations: Wallet integration. Transaction feedback. Gas fees display. Dark mode essential.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 504. Insurance Platform
- Recommended pattern: `Conversion + Trust`
- Style priority: `Accessible & Ethical` → `Flat Design`; primary recommendation `Minimalism & Swiss Style` + `Flat Design`; secondary `Accessible & Ethical`, `Minimalism & Swiss Style`
- Colour mood: `Trust Blue (#0066CC) + Green + Neutral`; palette focus `Trust Blue (#0066CC) + Green (security) + Neutral`
- Typography mood: `Clear + Professional typography`
- Key effects: `Quote calculator animations`; `Policy comparison`
- Landing & dashboard: landing `Conversion-Optimized + Trust`; dashboard `Claims Analytics Dashboard`
- Decision rules: Always → `quote calculator`, `policy comparison`
- Anti-patterns (`HIGH`): avoid `Confusing pricing`; `No trust signals`; `AI purple/pink gradients`
- Key considerations: Quote calculator. Policy comparison. Claims process. Trust signals. Clear pricing. Security badges.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 505. Banking/Traditional Finance
- Recommended pattern: `Trust & Authority + Feature`
- Style priority: `Minimalism & Swiss Style` → `Accessible & Ethical`; secondary `Swiss Modernism 2.0`, `Dark Mode (OLED)`
- Colour mood: `Navy (#0A1628) + Trust Blue + Gold`; palette focus `Navy (#0A1628) + Trust Blue + Gold accents`
- Typography mood: `Professional + Trustworthy typography`
- Key effects: `Smooth number animations`; `Security indicators`
- Landing & dashboard: landing `Trust & Authority + Feature-Rich`; dashboard `Financial Dashboard`
- Decision rules: Always → `security first`, `accessibility`
- Anti-patterns (`HIGH`): avoid `Playful design`; `Poor security UX`; `AI purple/pink gradients`
- Key considerations: Security-first. Account overview. Transaction history. Mobile banking. Accessibility critical. Trust paramount.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 506. Personal Finance Tracker
- Recommended pattern: `Interactive Product Demo`
- Style priority: `Glassmorphism` → `Dark Mode (OLED)`; secondary `Minimalism & Swiss Style`, `Flat Design`
- Colour mood: `Calm blue + success green + alert red + chart accents`
- Typography mood: `Modern + Clear hierarchy`
- Key effects: `Backdrop blur (10-20px)`; `Translucent overlays`
- Landing & dashboard: landing `Interactive Product Demo`; dashboard `Financial Dashboard`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`; If low performance (brief mentions low performance, low-end, slow device) → lead with `Flat Design` style
- Anti-patterns (`HIGH`): avoid `Pure white backgrounds`
- Key considerations: Category pie/donut charts. Monthly trend lines. Budget progress bars. Transaction list with swipe actions. Receipt camera. Currency formatting. Recurring entries.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 507. Expense Splitter / Bill Split
- Recommended pattern: `Minimal & Direct + Demo`
- Style priority: `Flat Design` → `Vibrant & Block-based`; secondary `Minimalism & Swiss Style`, `Micro-interactions`
- Colour mood: `Success green + alert red + neutral grey + avatar accent colors`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Minimal & Direct + Demo`; dashboard `N/A - Balance focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`; `Muted colors`; `Low energy`
- Key considerations: Group expense tracking. Debt simplification algorithm. Payment reminders. Multi-currency. Receipt photo import.
- RTL: `full` — mirrors cleanly; no directional rework needed

# Part 53 — Healthcare & Medical

## 508. Healthcare App
- Recommended pattern: `Social Proof-Focused`
- Style priority: `Neumorphism` → `Accessible & Ethical`; secondary `Soft UI Evolution`, `Claymorphism`
- Colour mood: `Calm blue + Health green`; palette focus `Calm blue + health green + trust`
- Typography mood: `Readable + Large type (16px+)`
- Key effects: `Soft box-shadow`; `Smooth press (150ms)`
- Landing & dashboard: landing `Social Proof-Focused`; dashboard `User Behavior Analytics`
- Decision rules: Always → `wcag aaa compliance`; If medication (brief mentions medication, medicine, prescription) → `red alert colors`
- Anti-patterns (`HIGH`): avoid `Bright neon colors`; `Motion-heavy animations`; `AI purple/pink gradients`
- Key considerations: Accessibility mandatory. Calming aesthetic.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 509. Senior Care/Elderly
- Recommended pattern: `Trust & Authority + Accessible`
- Style priority: `Accessible & Ethical` → `Soft UI Evolution`; secondary `Minimalism & Swiss Style`, `Neumorphism`
- Colour mood: `Calm Blue + Warm neutrals + Large text`
- Typography mood: `Large + Clear typography (18px+)`
- Key effects: `Large touch targets`; `Clear navigation`
- Landing & dashboard: landing `Trust & Authority + Social Proof`; dashboard `Healthcare Analytics`
- Decision rules: Always → `wcag aaa`, `family portal`
- Anti-patterns (`HIGH`): avoid `Small text`; `Complex navigation`; `AI purple/pink gradients`
- Key considerations: Care services. Staff qualifications. Facility tour. Family portal. Large touch targets. High contrast. Accessibility-first.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 510. Medical Clinic
- Recommended pattern: `Trust & Authority + Conversion`
- Style priority: `Accessible & Ethical` → `Minimalism & Swiss Style`; secondary `Neumorphism`, `Soft UI Evolution`
- Colour mood: `Medical Blue (#0077B6) + Trust White`; palette focus `Medical Blue (#0077B6) + Trust White + Calm Green`
- Typography mood: `Professional + Readable typography`
- Key effects: `Online booking flow`; `Doctor profile reveals`
- Landing & dashboard: landing `Trust & Authority + Conversion`; dashboard `Healthcare Analytics`
- Decision rules: Always → `appointment booking`, `insurance info`
- Anti-patterns (`HIGH`): avoid `Outdated interface`; `Confusing booking`; `AI purple/pink gradients`
- Key considerations: Services. Doctor profiles. Online booking. Patient portal. Insurance info. HIPAA compliant. Trust signals.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 511. Pharmacy/Drug Store
- Recommended pattern: `Conversion-Optimized + Trust`
- Style priority: `Flat Design` → `Accessible & Ethical`; secondary `Minimalism & Swiss Style`, `Soft UI Evolution`
- Colour mood: `Pharmacy Green + Trust Blue + Clean White`
- Typography mood: `Clear + Functional typography`
- Key effects: `Prescription upload flow`; `Refill reminders`
- Landing & dashboard: landing `Conversion-Optimized + Trust`; dashboard `Inventory Dashboard`
- Decision rules: Always → `prescription management`, `drug interaction warnings`
- Anti-patterns (`HIGH`): avoid `Confusing layout`; `Privacy concerns`; `AI purple/pink gradients`
- Key considerations: Product catalog. Prescription upload. Refill reminders. Health info. Store locator. Safety certifications.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 512. Dental Practice
- Recommended pattern: `Social Proof-Focused + Conversion`
- Style priority: `Soft UI Evolution` → `Minimalism & Swiss Style`; secondary `Accessible & Ethical`, `Inclusive Design`
- Colour mood: `Fresh Blue + White + Smile Yellow`; palette focus `Fresh Blue + White + Smile Yellow accent`
- Typography mood: `Friendly + Professional typography`
- Key effects: `Before/after gallery`; `Patient testimonial carousel`
- Landing & dashboard: landing `Social Proof-Focused + Conversion`; dashboard `Patient Analytics`
- Decision rules: Always → `before after gallery`, `appointment system`
- Anti-patterns (`HIGH`): avoid `Poor imagery`; `No testimonials`
- Key considerations: Services. Dentist profiles. Before/after. Online booking. Insurance. Patient testimonials. Friendly imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 513. Veterinary Clinic
- Recommended pattern: `Social Proof-Focused + Trust`
- Style priority: `Claymorphism` → `Accessible & Ethical`; secondary `Soft UI Evolution`, `Flat Design`
- Colour mood: `Caring Blue + Pet colors + Warm`; palette focus `Caring Blue + Pet-friendly colors + Warm accents`
- Typography mood: `Friendly + Welcoming typography`
- Key effects: `Pet profile management`; `Service animations`
- Landing & dashboard: landing `Social Proof-Focused + Trust`; dashboard `Pet Health Dashboard`
- Decision rules: Always → `pet portal`, `emergency contact`
- Anti-patterns (`MEDIUM`): avoid `Generic design`; `Hidden services`
- Key considerations: Pet services. Vet profiles. Online booking. Pet portal. Emergency info. Friendly animal imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 514. Biotech / Life Sciences
- Recommended pattern: `Storytelling + Data`
- Style priority: `Glassmorphism` → `Biomimetic / Organic 2.0`; secondary `Minimalism & Swiss Style`, `Organic Biophilic`
- Colour mood: `Sterile White + DNA Blue + Life Green`
- Typography mood: `Scientific + Clear typography`
- Key effects: `Data visualization`; `Research reveals`
- Landing & dashboard: landing `Storytelling-Driven + Research`; dashboard `Data-Dense + Predictive`
- Decision rules: Always → `data accuracy`, `clean aesthetic`
- Anti-patterns (`HIGH`): avoid `Cluttered data`; `Poor credibility`
- Key considerations: Data accuracy. Cleanliness. Complex data viz.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 515. Medication & Pill Reminder
- Recommended pattern: `Trust & Authority + Feature-Rich`
- Style priority: `Accessible & Ethical` → `Flat Design`; secondary `Minimalism & Swiss Style`, `Soft UI Evolution`
- Colour mood: `Medical trust blue + missed alert red + taken green + clean white`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Trust & Authority + Feature-Rich`; dashboard `N/A - Schedule focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`; `Color-only indicators`
- Key considerations: Multi-medication schedule. Caregiver sharing. Refill reminders. Drug interaction warnings. Large touch targets.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 516. Patient Portal / Health Records
- Recommended pattern: `Trust & Authority + Conversion`
- Style priority: `Minimalism & Swiss Style` → `Accessible & Ethical`; secondary `Minimalism & Swiss Style`, `Flat Design`
- Colour mood: `Clinical blue + health green + alert red + calm white + accessible contrast`
- Typography mood: `Professional + Readable typography`
- Key effects: `Labs timeline`; `message status states`
- Landing & dashboard: landing `Health Summary Dashboard`; dashboard `Healthcare Analytics`
- Decision rules: Always → `lab results timeline`, `medication list`, `appointment scheduling`, `message care team`, `family access`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Confusing booking`; `low contrast`; `missing lab hierarchy`
- Key considerations: Labs and results timeline. Medication list with refill. Appointment scheduling. Message care team. Immunization records. Allergy alerts. Family access proxy.
- Rationale: health records need trust, hierarchy, and fast access to the next actionable item (confidence `0.94`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 517. Telemedicine Platform
- Recommended pattern: `Trust & Authority + Conversion`
- Style priority: `Neumorphism` → `Accessible & Ethical`; secondary `Minimalism & Swiss Style`, `Soft UI Evolution`
- Colour mood: `Calm medical blue + video green + waiting amber + trust white`
- Typography mood: `Professional + Calm typography`
- Key effects: `Video-call state transitions`; `waiting-room ETA`
- Landing & dashboard: landing `Trust & Authority + Conversion`; dashboard `Healthcare Analytics`
- Decision rules: Always → `video call ui`, `appointment queue`, `symptom intake`, `prescription delivery`, `waiting room eta`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Low trust cues`; `confusing waiting state`; `tiny controls`
- Key considerations: Video call UI with screen share. Appointment queue. Symptom intake form. Prescription e-delivery. Waiting room with ETA. Post-visit summary. Insurance verification.
- Rationale: telemedicine must reduce anxiety, surface wait state, and keep control sizing forgiving (confidence `0.88`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

# Part 54 — Wellness, Fitness & Self-Care

## 518. Mental Health App
- Recommended pattern: `Social Proof-Focused`
- Style priority: `Neumorphism` → `Accessible & Ethical`; secondary `Claymorphism`, `Soft UI Evolution`
- Colour mood: `Calm Pastels + Trust colors`
- Typography mood: `Calming + Readable typography`
- Key effects: `Soft press`; `Breathing animations`
- Landing & dashboard: landing `Social Proof-Focused`; dashboard `Healthcare Analytics`
- Decision rules: Always → `privacy first`; If meditation (brief mentions meditation, breathing, mindfulness) → `add breathing animation`
- Anti-patterns (`HIGH`): avoid `Bright neon`; `Motion overload`
- Key considerations: Calming aesthetics. Privacy-first. Crisis resources. Progress tracking. Accessibility mandatory.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 519. Beauty/Spa/Wellness Service
- Recommended pattern: `Hero-Centric + Social Proof`
- Style priority: `Soft UI Evolution` → `Neumorphism`; secondary `Glassmorphism`, `Minimalism & Swiss Style`
- Colour mood: `Soft pastels (Pink Sage Cream) + Gold accents`; palette focus `Soft pastels (Pink #FFB6C1 Sage #90EE90) + Cream + Gold accents`
- Typography mood: `Elegant + Calming typography`
- Key effects: `Soft shadows`; `Smooth transitions (200-300ms)`; `Gentle hover`
- Landing & dashboard: landing `Hero-Centric Design + Social Proof`; dashboard `User Behavior Analytics`
- Decision rules: Always → `booking system`, `before after gallery`; If luxury (brief mentions luxury, premium, high-end) → `add gold accents`
- Anti-patterns (`HIGH`): avoid `Bright neon colors`; `Harsh animations`; `Dark mode`
- Key considerations: Calming aesthetic. Booking system. Service menu. Before/after gallery. Testimonials. Relaxing imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 520. Fitness/Gym App
- Recommended pattern: `Feature-Rich + Data`
- Style priority: `Vibrant & Block-based` → `Dark Mode (OLED)`; secondary `Motion-Driven`, `Neumorphism`
- Colour mood: `Energetic (Orange #FF6B35) + Dark bg`; palette focus `Energetic (Orange #FF6B35 Electric Blue) + Dark bg`
- Typography mood: `Bold + Motivational typography`
- Key effects: `Progress ring animations`; `Achievement unlocks`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `User Behavior Analytics`
- Decision rules: Always → `progress tracking`, `workout plans`
- Anti-patterns (`HIGH`): avoid `Static design`; `No gamification`
- Key considerations: Progress tracking. Workout plans. Community features. Achievements. Motivational design.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 521. Biohacking / Longevity App
- Recommended pattern: `Data-Dense + Storytelling`
- Style priority: `Biomimetic / Organic 2.0` → `Minimalism & Swiss Style`; primary recommendation `Biomimetic / Organic 2.0`; secondary `Minimalism & Swiss Style`, `Dark Mode (OLED)`
- Colour mood: `Cellular Pink/Red + DNA Blue + White`; palette focus `Cellular Pink/Red + DNA Blue + Clean White`
- Typography mood: `Scientific + Clear typography`
- Key effects: `Biological data viz`; `Progress animations`
- Landing & dashboard: landing `Data-Dense + Storytelling`; dashboard `Real-Time Monitor + Biological Data`
- Decision rules: Always → `data privacy`, `scientific credibility`
- Anti-patterns (`HIGH`): avoid `Generic health app`; `No privacy`
- Key considerations: Personal data privacy. Scientific credibility. Biological visualizations.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 522. Habit Tracker
- Recommended pattern: `Social Proof-Focused + Demo`
- Style priority: `Claymorphism` → `Vibrant & Block-based`; secondary `Micro-interactions`, `Flat Design`
- Colour mood: `Streak warm (amber/orange) + progress green + motivational accents`
- Typography mood: `Playful + Rounded + Friendly`
- Key effects: `Multi-layer shadows`; `Spring bounce`; `Soft press 200ms`
- Landing & dashboard: landing `Social Proof-Focused + Demo`; dashboard `User Behavior Analytics`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Streak calendar heatmap. Daily check-in interaction. Gamification (badges/levels/fire). Reminder push. Progress ring charts. Weekly/monthly stats. Motivational micro-copy.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 523. Meditation & Mindfulness
- Recommended pattern: `Storytelling-Driven + Social Proof`
- Style priority: `Neumorphism` → `Soft UI Evolution`; secondary `Aurora UI`, `Glassmorphism`
- Colour mood: `Ultra-calm pastels (lavender/sage/sky) + breathing animation gradient`
- Typography mood: `Subtle + Soft + Monochromatic`
- Key effects: `Dual shadows (light`; `dark)`; `Soft press 150ms`
- Landing & dashboard: landing `Storytelling-Driven + Social Proof`; dashboard `User Behavior Analytics`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Breathing circle animation. Session duration picker. Ambient sound mixer. Streak/consistency tracking. Guided audio player. Sleep timer. Minimal chrome. Slow easing transitions only.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 524. Mood Tracker
- Recommended pattern: `Storytelling-Driven + Social Proof`
- Style priority: `Soft UI Evolution` → `Minimalism & Swiss Style`; secondary `Aurora UI`, `Neumorphism`
- Colour mood: `Emotion gradient (blue sad to yellow happy) + pastel per mood + insight accent`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle hover 200ms`; `Smooth transitions`; `Clean`
- Landing & dashboard: landing `Storytelling-Driven + Social Proof`; dashboard `N/A - Mood chart focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: One-tap daily check-in. Emotion wheel selector. Mood calendar heatmap. Pattern insights. Export and share.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 525. Running & Cycling GPS
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Dark Mode (OLED)` → `Vibrant & Block-based`; secondary `Motion-Driven`, `Glassmorphism`
- Colour mood: `Energetic orange + map accent + pace zones (green/yellow/red)`
- Typography mood: `High contrast + Light on dark`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `Performance Analytics`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`; If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Pure white backgrounds`; `Muted colors`; `Low energy`
- Key considerations: Live GPS tracking. Route map. Auto-pause detection. Segment leaderboards. Training zones. Social feed. Garmin sync.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 526. Yoga & Stretching Guide
- Recommended pattern: `Storytelling-Driven + Social Proof`
- Style priority: `Organic Biophilic` → `Soft UI Evolution`; secondary `Neumorphism`, `Minimalism & Swiss Style`
- Colour mood: `Earth calming sage/terracotta/cream + breathing gradient + warm accent`
- Typography mood: `Warm + Humanist + Natural`
- Key effects: `Rounded 16-24px`; `Natural shadows`; `Flowing SVG`
- Landing & dashboard: landing `Storytelling-Driven + Social Proof`; dashboard `N/A - Session focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Pose library with illustrations. Guided sessions with audio. Breathing exercises. Progress calendar. Beginner to advanced.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 527. Sleep Tracker
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Dark Mode (OLED)` → `Neumorphism`; secondary `Glassmorphism`, `Minimalism & Swiss Style`
- Colour mood: `Deep midnight blue + stars/moon accent + sleep quality gradient (poor red to great green)`
- Typography mood: `High contrast + Light on dark`
- Key effects: `Dual shadows (light`; `dark)`; `Soft press 150ms`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `Healthcare Analytics`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`; If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Pure white backgrounds`
- Key considerations: Sleep cycle detection. Smart alarm wakes at light sleep. Snore detection. Weekly trends. Apple Health integration.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 528. Calorie & Nutrition Counter
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Flat Design` → `Vibrant & Block-based`; secondary `Minimalism & Swiss Style`, `Claymorphism`
- Colour mood: `Healthy green + macro colors (protein blue, carb orange, fat yellow) + progress circle`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `Healthcare Analytics`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`; `Muted colors`; `Low energy`
- Key considerations: Barcode scanner food log. Large database. Macro goals. Restaurant lookup. Recipe builder. AI photo food logging.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 529. Period & Cycle Tracker
- Recommended pattern: `Social Proof-Focused + Trust`
- Style priority: `Soft UI Evolution` → `Aurora UI`; secondary `Accessible & Ethical`, `Claymorphism`
- Colour mood: `Rose/blush + lavender + fertility green + soft calendar tones`
- Typography mood: `Elegant + Gradient-friendly`
- Key effects: `Flowing gradients 8-12s`; `Color morphing`
- Landing & dashboard: landing `Social Proof-Focused + Trust`; dashboard `Healthcare Analytics`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Cycle prediction. Symptom logging. Fertility window. Personalized insights. Privacy-first. Partner sharing option.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 530. Water & Hydration Reminder
- Recommended pattern: `Minimal & Direct + Demo`
- Style priority: `Claymorphism` → `Vibrant & Block-based`; secondary `Flat Design`, `Micro-interactions`
- Colour mood: `Refreshing blue + water wave animation + goal progress accent`
- Typography mood: `Playful + Rounded + Friendly`
- Key effects: `Multi-layer shadows`; `Spring bounce`; `Soft press 200ms`
- Landing & dashboard: landing `Minimal & Direct + Demo`; dashboard `N/A - Daily goal focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Tap to log quickly. Animated fill visualization. Custom reminders. Goal by weight/weather. Streak system. Widget.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 531. Fasting & Intermittent Timer
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Minimalism & Swiss Style` → `Dark Mode (OLED)`; secondary `Neumorphism`, `Flat Design`
- Colour mood: `Fasting deep blue/purple + eating window green + timeline neutral`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `N/A - Timer focused`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`; If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Pure white backgrounds`
- Key considerations: Protocol selector (16:8, 18:6, OMAD). Circular countdown timer. Fasting history log. Tips during fast. Electrolytes.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 532. White Noise & Ambient Sound
- Recommended pattern: `Minimal & Direct + Social Proof`
- Style priority: `Minimalism & Swiss Style` → `Dark Mode (OLED)`; secondary `Neumorphism`, `Organic Biophilic`
- Colour mood: `Calming dark + ambient texture visual + subtle sound wave + sleep blue`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Minimal & Direct + Social Proof`; dashboard `N/A - Player focused`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`; If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Pure white backgrounds`
- Key considerations: Sound mixer with multiple simultaneous layers. Sleep timer with fade. Custom soundscapes. Offline. Background audio.
- RTL: `full` — mirrors cleanly; no directional rework needed

# Part 55 — E-commerce, Retail & Marketplaces

## 533. E-commerce
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Vibrant & Block-based`; secondary `Aurora UI`, `Motion-Driven`
- Colour mood: `Brand primary + Success green`
- Typography mood: `Engaging + Clear hierarchy`
- Key effects: `Card hover lift (200ms)`; `Scale effect`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `Sales Intelligence Dashboard`
- Decision rules: If luxury (brief mentions luxury, premium, high-end) → lead with `Liquid Glass` style; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`HIGH`): avoid `Flat design without depth`; `Text-heavy pages`
- Key considerations: Engagement & conversions. High visual hierarchy.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 534. E-commerce Luxury
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Liquid Glass` → `Glassmorphism`; secondary `3D & Hyperrealism`, `Aurora UI`
- Colour mood: `Premium colors + Minimal accent`
- Typography mood: `Elegant + Refined typography`
- Key effects: `Chromatic aberration`; `Fluid animations (400-600ms)`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `Sales Intelligence Dashboard`
- Decision rules: If checkout (brief mentions checkout, payment, purchase) → `emphasize trust`; If hero needed (brief mentions hero, showcase, launch) → lead with `3D & Hyperrealism` style
- Anti-patterns (`HIGH`): avoid `Vibrant & Block-based`; `Playful colors`
- Key considerations: Elegance & sophistication. Premium materials.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 535. Subscription Box Service
- Recommended pattern: `Feature-Rich + Conversion`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Claymorphism`, `Aurora UI`
- Colour mood: `Brand + Excitement colors`
- Typography mood: `Engaging + Clear typography`
- Key effects: `Unboxing reveal animations`; `Product carousel`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `E-commerce Analytics`
- Decision rules: Always → `personalization quiz`, `subscription management`
- Anti-patterns (`HIGH`): avoid `Confusing pricing`; `No unboxing preview`
- Key considerations: Unboxing experience. Personalization quiz. Subscription management. Product reveals.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 536. Luxury/Premium Brand
- Recommended pattern: `Storytelling + Feature-Rich`
- Style priority: `Liquid Glass` → `Glassmorphism`; secondary `Minimalism & Swiss Style`, `3D & Hyperrealism`
- Colour mood: `Black + Gold (#FFD700) + White`; palette focus `Black + Gold (#FFD700) + White + Minimal accent`
- Typography mood: `Elegant + Refined typography`
- Key effects: `Slow parallax`; `Premium reveals (400-600ms)`
- Landing & dashboard: landing `Storytelling-Driven + Feature-Rich`; dashboard `Sales Intelligence Dashboard`
- Decision rules: Always → `high quality imagery`, `storytelling`
- Anti-patterns (`HIGH`): avoid `Cheap visuals`; `Fast animations`
- Key considerations: Elegance paramount. Premium imagery. Storytelling. High-quality visuals. Exclusive feel.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 537. Marketplace (P2P)
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Vibrant & Block-based` → `Flat Design`; secondary `Micro-interactions`, `Bento Box Grid`
- Colour mood: `Trust colors + Category colors + Success green`
- Typography mood: `Modern + Engaging typography`
- Key effects: `Review star animations`; `Listing hover effects`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `E-commerce Analytics`
- Decision rules: Always → `seller profiles`, `secure payment`
- Anti-patterns (`HIGH`): avoid `Low trust signals`; `Confusing layout`
- Key considerations: Seller/buyer profiles. Listings. Reviews/ratings. Secure payment. Messaging. Search/filter. Trust badges.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 538. Automotive/Car Dealership
- Recommended pattern: `Hero-Centric + Feature-Rich`
- Style priority: `Motion-Driven` → `3D & Hyperrealism`; secondary `Dark Mode (OLED)`, `Glassmorphism`
- Colour mood: `Brand colors + Metallic + Dark/Light`; palette focus `Brand colors + Metallic accents + Dark/Light`
- Typography mood: `Bold + Confident typography`
- Key effects: `360 product view`; `Configurator animations`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Sales Intelligence Dashboard`
- Decision rules: Always → `vehicle comparison`, `financing calculator`
- Anti-patterns (`HIGH`): avoid `Static product pages`; `Poor UX`
- Key considerations: Vehicle showcase. 360° views. Comparison tools. Financing calculator. Test drive booking. High-quality imagery.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 539. Florist/Plant Shop
- Recommended pattern: `Hero-Centric + Conversion`
- Style priority: `Organic Biophilic` → `Vibrant & Block-based`; secondary `Aurora UI`, `Motion-Driven`
- Colour mood: `Natural Green + Floral pinks/purples`; palette focus `Natural Green + Floral pinks/purples + Earth tones`
- Typography mood: `Elegant + Natural typography`
- Key effects: `Product reveal`; `Seasonal transitions`
- Landing & dashboard: landing `Hero-Centric Design + Conversion`; dashboard `E-commerce Analytics`
- Decision rules: Always → `delivery scheduling`, `care guides`
- Anti-patterns (`MEDIUM`): avoid `Poor imagery`; `No seasonal content`
- Key considerations: Product catalog. Occasion categories. Delivery scheduling. Care guides. Seasonal collections. Beautiful imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 540. Digital Products/Downloads
- Recommended pattern: `Feature-Rich + Conversion`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Glassmorphism`, `Bento Box Grid`
- Colour mood: `Product colors + Brand + Success green`; palette focus `Product category colors + Brand + Success green`
- Typography mood: `Modern + Clear typography`
- Key effects: `Product preview`; `Instant delivery animations`
- Landing & dashboard: landing `Feature-Rich Showcase + Conversion`; dashboard `E-commerce Analytics`
- Decision rules: Always → `product preview`, `instant delivery`
- Anti-patterns (`HIGH`): avoid `No preview`; `Slow delivery`
- Key considerations: Product showcase. Preview. Pricing. Instant delivery. License management. Customer reviews.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 541. Gift & Wishlist
- Recommended pattern: `Minimal & Direct + Conversion`
- Style priority: `Vibrant & Block-based` → `Soft UI Evolution`; secondary `Claymorphism`, `Flat Design`
- Colour mood: `Celebration warm pink/gold/red + category colors + surprise accent`
- Typography mood: `Energetic + Bold + Large`
- Key effects: `Large section gaps 48px`; `Color shift hover`; `Scroll-snap`
- Landing & dashboard: landing `Minimal & Direct + Conversion`; dashboard `N/A - List focused`
- Decision rules: If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Add from any URL. Price range filter. Reserved-by-others system. Occasion calendar. Collaborative list. Surprise mode.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 542. Directory / Listing Site
- Recommended pattern: `Marketplace / Directory`
- Style priority: `Flat Design` → `Bento Box Grid`; primary recommendation `Flat Design` + `Vibrant & Block-based`; secondary `Minimalism & Swiss Style`, `Bento Box Grid`
- Colour mood: `Neutral bg + category color chips + map accent + verified badge`
- Typography mood: `Scan-friendly + Neutral typography`
- Key effects: `Filter chips`; `Map/list toggle`
- Landing & dashboard: landing `Filter-Heavy Grid + Map`; dashboard `N/A - Listing focused`
- Decision rules: Always → `category tree`, `multi filter sidebar`, `map list toggle`, `verified badges`, `claim listing`; If discovery focused (brief mentions discover, discovery, browse, directory) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `No trust cues`; `Text-heavy cards`; `hidden filters`
- Key considerations: Category tree. Multi-filter sidebar. Map/list toggle. Verified badges. Reviews. Claim listing flow.
- Rationale: listings live or die on discovery speed, trust cues, and clear sort/filter affordances (confidence `0.93`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 543. Auction Platform
- Recommended pattern: `Real-Time / Operations Landing`
- Style priority: `Dark Mode (OLED)` → `Motion-Driven`; secondary `Vibrant & Block-based`, `Real-Time Monitoring`
- Colour mood: `Dark bg + bid green + outbid red + countdown amber`
- Typography mood: `Bold + Urgent typography`
- Key effects: `Countdown timer`; `live bid updates`
- Landing & dashboard: landing `Live Auction Feed + Countdown`; dashboard `N/A - Auction focused`
- Decision rules: Always → `live bid updates`, `countdown timer`, `auto bid ceiling`, `outbid notifications`, `bid history`; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Static design`; `No bid state`; `poor mobile`
- Key considerations: Real-time bid updates. Countdown timer urgency. Auto-bid ceiling. Outbid notifications. Bid history. Reserve price indicator.
- Rationale: auction flows need urgency, status clarity, and instant feedback on bid changes (confidence `0.93`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 544. Classifieds / Buy-Sell
- Recommended pattern: `Marketplace / Directory`
- Style priority: `Flat Design` → `Bento Box Grid`; primary recommendation `Flat Design` + `Vibrant & Block-based`; secondary `Minimalism & Swiss Style`, `Bento Box Grid`
- Colour mood: `Neutral bg + price green + category chips + verified seller badge`
- Typography mood: `Scan-friendly + Marketplace typography`
- Key effects: `Photo-first cards`; `map/list toggle`
- Landing & dashboard: landing `Filter-Heavy Grid + Map`; dashboard `N/A - Listing focused`
- Decision rules: Always → `photo first cards`, `multi filter sidebar`, `price negotiation`, `location radius`, `seller reputation`; If discovery focused (brief mentions discover, discovery, browse, directory) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `No trust cues`; `text-heavy pages`; `hidden filters`
- Key considerations: Category tree. Photo-first listing cards. Price negotiation. Location radius filter. Saved searches. Seller reputation. Flag/report.
- Rationale: resale discovery depends on trust, proximity, and fast comparison of nearby inventory (confidence `0.93`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 545. Review Platform
- Recommended pattern: `Product Review/Ratings Focused`
- Style priority: `Bento Box Grid` → `Vibrant & Block-based`; primary recommendation `Flat Design` + `Vibrant & Block-based`; secondary `Accessible & Ethical`, `Minimalism & Swiss Style`
- Colour mood: `Brand primary + star gold + positive green + negative red + verified blue`
- Typography mood: `Readable + Review-first typography`
- Key effects: `Rating distribution`; `verified badge emphasis`
- Landing & dashboard: landing `Hero + Rating Summary + Review Feed`; dashboard `Review Analytics Dashboard`
- Decision rules: Always → `rating summary`, `verified badge`, `photo video reviews`, `helpful votes`, `sort by recency`; If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`HIGH`): avoid `No verified badges`; `text-heavy pages`; `hidden filter controls`
- Key considerations: Star rating summary with distribution. Verified purchase badge. Photo/video reviews. Helpful/upvote. Filter by rating. Response from business. Sort by recency.
- Rationale: review UX depends on trust signals, filtering, and fast scan of the rating spread (confidence `0.94`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 546. Testimonial & Social Proof Widget
- Recommended pattern: `Hero + Testimonials + CTA`
- Style priority: `Bento Box Grid` → `Vibrant & Block-based`; primary recommendation `Vibrant & Block-based` + `Flat Design`; secondary `Motion-Driven`, `Minimalism & Swiss Style`
- Colour mood: `Brand primary + quote accent + star gold + verified blue`
- Typography mood: `Readable + Social-proof typography`
- Key effects: `Card carousel`; `photo/video cards`
- Landing & dashboard: landing `Wall-of-Love Grid`; dashboard `Engagement Analytics Dashboard`
- Decision rules: Always → `testimonial cards`, `star ratings`, `video testimonials`, `case study summaries`, `embed code`; If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`; If conversion focused (brief mentions conversion, sales, signup, purchase) → `increase playfulness`
- Anti-patterns (`MEDIUM`): avoid `No evidence badges`; `static layout`; `tiny media`
- Key considerations: Testimonial cards with photo. Star ratings. Video testimonials. Case study summaries. Filter by industry/product. Embeddable widget code. Auto-rotate carousel.
- Rationale: social proof widgets exist to compress trust into a quick, embeddable read (confidence `0.91`)
- RTL: `full` — mirrors cleanly; no directional rework needed

# Part 56 — Education & Learning

## 547. Educational App
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Claymorphism` → `Micro-interactions`; secondary `Vibrant & Block-based`, `Flat Design`
- Colour mood: `Playful colors + Clear hierarchy`
- Typography mood: `Friendly + Engaging typography`
- Key effects: `Soft press (200ms)`; `Fluffy elements`
- Landing & dashboard: landing `Storytelling-Driven`; dashboard `User Behavior Analytics`
- Decision rules: If gamification (brief mentions gamification, badges, streak) → `add progress animation`; If children (brief mentions child, children, kids) → `increase playfulness`
- Anti-patterns (`MEDIUM`): avoid `Dark modes`; `Complex jargon`
- Key considerations: Engagement & ease of use. Age-appropriate design.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 548. Micro-Credentials/Badges Platform
- Recommended pattern: `Trust & Authority + Feature`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Accessible & Ethical`, `Swiss Modernism 2.0`
- Colour mood: `Trust Blue + Gold (#FFD700)`
- Typography mood: `Professional + Clear typography`
- Key effects: `Badge reveal animations`; `Progress tracking`
- Landing & dashboard: landing `Trust & Authority`; dashboard `Education Dashboard`
- Decision rules: Always → `credential verification`, `progress display`
- Anti-patterns (`MEDIUM`): avoid `No verification`; `Hidden progress`
- Key considerations: Credential verification. Badge display. Progress tracking. Issuer trust. LinkedIn integration.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 549. Online Course/E-learning
- Recommended pattern: `Feature-Rich + Social Proof`
- Style priority: `Claymorphism` → `Vibrant & Block-based`; secondary `Motion-Driven`, `Flat Design`
- Colour mood: `Vibrant learning colors + Progress green`
- Typography mood: `Friendly + Engaging typography`
- Key effects: `Progress bar animations`; `Certificate reveals`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `Education Dashboard`
- Decision rules: Always → `progress tracking`, `video player`
- Anti-patterns (`HIGH`): avoid `Boring design`; `No gamification`
- Key considerations: Course catalog. Progress tracking. Video player. Quizzes. Certificates. Community forums. Gamification.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 550. Language Learning App
- Recommended pattern: `Feature-Rich + Social Proof`
- Style priority: `Claymorphism` → `Vibrant & Block-based`; secondary `Micro-interactions`, `Flat Design`
- Colour mood: `Playful colors + Progress indicators`; palette focus `Playful colors + Progress indicators + Country flags`
- Typography mood: `Friendly + Clear typography`
- Key effects: `Progress animations`; `Achievement unlocks`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `Learning Analytics`
- Decision rules: Always → `progress tracking`, `gamification`
- Anti-patterns (`HIGH`): avoid `Boring design`; `No motivation`
- Key considerations: Lesson structure. Progress tracking. Gamification. Speaking practice. Community. Achievement badges.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 551. Coding Bootcamp
- Recommended pattern: `Feature-Rich + Social Proof`
- Style priority: `Dark Mode (OLED)` → `Minimalism & Swiss Style`; secondary `Cyberpunk UI`, `Flat Design`
- Colour mood: `Code editor colors + Brand + Success`; palette focus `Code editor colors + Brand + Success green`
- Typography mood: `Technical + Clear typography`
- Key effects: `Terminal animations`; `Career outcome reveals`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `Student Analytics`
- Decision rules: Always → `curriculum`, `career outcomes`
- Anti-patterns (`HIGH`): avoid `Light mode only`; `Hidden results`
- Key considerations: Curriculum. Projects. Career outcomes. Alumni. Pricing. Application. Terminal aesthetic.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 552. Flashcard & Study Tool
- Recommended pattern: `Feature-Rich Showcase + Demo`
- Style priority: `Claymorphism` → `Micro-interactions`; secondary `Vibrant & Block-based`, `Flat Design`
- Colour mood: `Playful primary + correct green + incorrect red + progress blue`
- Typography mood: `Playful + Rounded + Friendly`
- Key effects: `Multi-layer shadows`; `Spring bounce`; `Soft press 200ms`
- Landing & dashboard: landing `Feature-Rich Showcase + Demo`; dashboard `Learning Analytics`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: 3D card flip animation. Spaced repetition algorithm. Deck browser. Session progress bar. Streak tracking. Timed quiz mode. Share/import decks. Rich text + image cards.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 553. Study Together / Virtual Coworking
- Recommended pattern: `Social Proof-Focused + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Soft UI Evolution`; secondary `Flat Design`, `Dark Mode (OLED)`
- Colour mood: `Calm focus blue + session progress indicator + ambient warm neutrals`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle hover 200ms`; `Smooth transitions`; `Clean`
- Landing & dashboard: landing `Social Proof-Focused + Feature-Rich`; dashboard `User Behavior Analytics`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Live study rooms with video/avatar presence. Shared focus timer. Ambient music. Goals sharing. Streak accountability.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 554. Coding Challenge & Practice
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Dark Mode (OLED)` → `Cyberpunk UI`; secondary `Minimalism & Swiss Style`, `Flat Design`
- Colour mood: `Code editor dark + success green + difficulty gradient (easy green / medium amber / hard red)`
- Typography mood: `High contrast + Light on dark`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `Student Analytics`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`; If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Pure white backgrounds`
- Key considerations: Code editor with syntax highlight. Multiple languages. Hint system. Solution explanation. Company tags. Contest mode.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 555. Kids Learning (ABC & Math)
- Recommended pattern: `Social Proof-Focused + Trust`
- Style priority: `Claymorphism` → `Vibrant & Block-based`; secondary `Micro-interactions`, `Flat Design`
- Colour mood: `Bright primary + child-safe pastels + reward gold + interactive accent`
- Typography mood: `Playful + Rounded + Friendly`
- Key effects: `Multi-layer shadows`; `Spring bounce`; `Soft press 200ms`
- Landing & dashboard: landing `Social Proof-Focused + Trust`; dashboard `Parent Dashboard`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Age-appropriate UI for 2-8. No ads. No dark patterns. Curriculum aligned. Parent progress reports. Reward system.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 556. Music Instrument Learning
- Recommended pattern: `Interactive Product Demo + Social Proof`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Dark Mode (OLED)`, `Soft UI Evolution`
- Colour mood: `Musical warm deep red/brown + note color system + skill progress bar`
- Typography mood: `Energetic + Bold + Large`
- Key effects: `Scroll animations`; `Parallax`; `Page transitions`
- Landing & dashboard: landing `Interactive Product Demo + Social Proof`; dashboard `Learning Analytics`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Interactive instrument on-screen. Sheet music display. Song library. Slow-tempo practice. Recording and playback. Teacher mode.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 557. LMS (Learning Management System)
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Flat Design` → `Accessible & Ethical`; secondary `Minimalism & Swiss Style`, `Vibrant & Block-based`
- Colour mood: `Calm blue + course category colors + grade green + alert red`
- Typography mood: `Readable + Instructional typography`
- Key effects: `Course progress`; `calendar reminders`
- Landing & dashboard: landing `Dashboard + Course Grid`; dashboard `Education Analytics Dashboard`
- Decision rules: Always → `course grid`, `assignment deadlines`, `gradebook`, `discussion forums`, `calendar integration`; If content focused (brief mentions content, article, reading, documentation) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Hidden assignments`; `poor mobile`; `cluttered navigation`
- Key considerations: Dashboard with enrolled courses. Assignment deadlines. Gradebook view. Discussion forums. File upload. Calendar integration. Mobile offline sync.
- Rationale: learning systems must stay structured, legible, and reminder-driven across devices (confidence `0.93`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

# Part 57 — Media, Publishing & Knowledge

## 558. Podcast Platform
- Recommended pattern: `Storytelling + Feature-Rich`
- Style priority: `Dark Mode (OLED)` → `Minimalism & Swiss Style`; secondary `Motion-Driven`, `Vibrant & Block-based`
- Colour mood: `Dark + Audio waveform accents`
- Typography mood: `Modern + Clear typography`
- Key effects: `Waveform visualizations`; `Episode transitions`
- Landing & dashboard: landing `Storytelling-Driven`; dashboard `Media/Entertainment Dashboard`
- Decision rules: Always → `audio player ux`, `episode discovery`
- Anti-patterns (`HIGH`): avoid `Poor audio player`; `Cluttered layout`
- Key considerations: Audio player UX. Episode discovery. Creator tools. Analytics for podcasters.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 559. Music Streaming
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Dark Mode (OLED)` → `Vibrant & Block-based`; secondary `Motion-Driven`, `Aurora UI`
- Colour mood: `Dark (#121212) + Vibrant accents + Album art colors`
- Typography mood: `Modern + Bold typography`
- Key effects: `Waveform visualization`; `Playlist animations`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `Media/Entertainment Dashboard`
- Decision rules: Always → `audio player ux`; If discovery focused (brief mentions discover, discovery, browse, directory) → `add playlist recommendations`
- Anti-patterns (`HIGH`): avoid `Cluttered layout`; `Poor audio player UX`
- Key considerations: Audio player. Playlist management. Artist pages. Personalization. Social features. Waveform visualizations.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 560. Video Streaming/OTT
- Recommended pattern: `Hero-Centric + Feature-Rich`
- Style priority: `Dark Mode (OLED)` → `Motion-Driven`; secondary `Glassmorphism`, `Vibrant & Block-based`
- Colour mood: `Dark bg + Poster colors + Brand accent`; palette focus `Dark bg + Content poster colors + Brand accent`
- Typography mood: `Bold + Engaging typography`
- Key effects: `Video player animations`; `Content carousel (parallax)`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Media/Entertainment Dashboard`
- Decision rules: Always → `continue watching`; If personalized (brief mentions personalized, personalised, recommendation) → `add recommendations`
- Anti-patterns (`HIGH`): avoid `Static layout`; `Slow video player`
- Key considerations: Video player. Content discovery. Watchlist. Continue watching. Personalized recommendations. Thumbnail-heavy.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 561. News/Media Platform
- Recommended pattern: `Hero-Centric + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Dark Mode (OLED)`, `Accessible & Ethical`
- Colour mood: `Brand colors + High contrast`; palette focus `Brand colors + High contrast + Category colors`
- Typography mood: `Clear + Readable typography`
- Key effects: `Breaking news badge`; `Article reveal animations`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Media Analytics Dashboard`
- Decision rules: Always → `mobile first reading`, `category navigation`
- Anti-patterns (`HIGH`): avoid `Cluttered layout`; `Slow loading`
- Key considerations: Article layout. Breaking news. Categories. Search. Subscription. Mobile reading. Fast loading.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 562. Magazine/Blog
- Recommended pattern: `Storytelling + Hero-Centric`
- Style priority: `Swiss Modernism 2.0` → `Motion-Driven`; secondary `Minimalism & Swiss Style`, `Aurora UI`
- Colour mood: `Editorial colors + Brand + Clean white`; palette focus `Editorial colors + Brand primary + Clean white`
- Typography mood: `Editorial + Elegant typography`
- Key effects: `Article transitions`; `Category reveals`
- Landing & dashboard: landing `Storytelling-Driven + Hero-Centric`; dashboard `Content Analytics`
- Decision rules: Always → `article showcase`, `newsletter signup`
- Anti-patterns (`HIGH`): avoid `Poor typography`; `Slow loading`
- Key considerations: Article showcase. Category navigation. Author profiles. Newsletter signup. Related content. Typography-focused.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 563. Newsletter Platform
- Recommended pattern: `Minimal + Conversion`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Swiss Modernism 2.0`, `Accessible & Ethical`
- Colour mood: `Brand primary + Clean white + CTA`; palette focus `Brand primary + Clean white + CTA accent`
- Typography mood: `Clean + Readable typography`
- Key effects: `Subscribe form`; `Archive reveals`
- Landing & dashboard: landing `Minimal & Direct + Conversion`; dashboard `Email Analytics`
- Decision rules: Always → `subscribe form`, `sample content`
- Anti-patterns (`MEDIUM`): avoid `Complex signup`; `No preview`
- Key considerations: Subscribe form. Archive. About. Social proof. Sample content. Simple conversion.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 564. Bookmark & Read-Later
- Recommended pattern: `Minimal & Direct + Demo`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Editorial Grid / Magazine`, `Swiss Modernism 2.0`
- Colour mood: `Paper warm white + ink neutral + minimal accent + tag colors`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Minimal & Direct + Demo`; dashboard `N/A - List focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Complex shadows`; `3D effects`
- Key considerations: Fast save via share sheet. Article distraction-free view. Tags and collections. Offline sync. Reading progress.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 565. Academic Journal / Scholarly Publishing
- Recommended pattern: `Newsletter / Content First`
- Style priority: `Swiss Modernism 2.0` → `Accessible & Ethical`; primary recommendation `Swiss Modernism 2.0` + `Minimalism & Swiss Style`; secondary `Editorial Grid / Magazine`, `Accessible & Ethical`
- Colour mood: `Trust navy + White + Citation blue + Serif accents`
- Typography mood: `Serif body + Formal hierarchy`
- Key effects: `Search highlight`; `Smooth scrolling`
- Landing & dashboard: landing `Content-Index + Search`; dashboard `N/A - Publication focused`
- Decision rules: Always → `abstract doi prominence`, `citation links`, `search first`, `wcag aaa`, `issue browse`; If content focused (brief mentions content, article, reading, documentation) → `prioritize clarity`; If trust needed (brief mentions trust, secure, verified, authority) → `reduce motion`
- Anti-patterns (`MEDIUM`): avoid `Low contrast`; `Visual clutter`; `motion-heavy chrome`
- Key considerations: Prioritize readability (serif body text). Clear article hierarchy. Abstract/DOI prominence. WCAG AAA. Minimal visual noise. Trust signals: ISSN, indexing badges.
- Rationale: academic credibility needs searchable citation-first navigation and restrained motion (confidence `0.88`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 566. Wiki / Encyclopedia
- Recommended pattern: `FAQ/Documentation Landing`
- Style priority: `Swiss Modernism 2.0` → `Accessible & Ethical`; primary recommendation `Minimalism & Swiss Style` + `Flat Design`; secondary `Swiss Modernism 2.0`, `Accessible & Ethical`
- Colour mood: `Clean white + link blue + heading hierarchy + citation grey`
- Typography mood: `Clear + Hierarchical typography`
- Key effects: `Table of contents sticky nav`; `search highlight`
- Landing & dashboard: landing `Search-First + Hierarchical Navigation`; dashboard `N/A - Reference focused`
- Decision rules: Always → `full text search`, `toc sidebar`, `edit history`, `interpage linking`, `print friendly`; If content focused (brief mentions content, article, reading, documentation) → `prioritize clarity`; If ux focused (brief mentions ux, usability, accessibility, accessible) → `virtualize lists`
- Anti-patterns (`MEDIUM`): avoid `No search`; `flat hierarchy`; `noisy page chrome`
- Key considerations: Full-text search bar. Table of contents sidebar. Edit history. Inter-page linking. Mobile responsive. Print-friendly.
- Rationale: reference content needs search, hierarchy, and low-friction cross-linking (confidence `0.91`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

# Part 58 — Social, Community & Communication

## 567. Social Media App
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Aurora UI`, `Micro-interactions`
- Colour mood: `Vibrant + Engagement colors`
- Typography mood: `Modern + Bold typography`
- Key effects: `Large scroll animations`; `Icon animations`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `User Behavior Analytics`
- Decision rules: If engagement metric (brief mentions engagement, retention, contribution) → `add motion`; If content focused (brief mentions content, article, reading, documentation) → `minimize chrome`
- Anti-patterns (`MEDIUM`): avoid `Heavy skeuomorphism`; `Accessibility ignored`
- Key considerations: Engagement & retention. Addictive design ethics.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 568. Creator Economy Platform
- Recommended pattern: `Social Proof + Feature-Rich`
- Style priority: `Vibrant & Block-based` → `Bento Box Grid`; secondary `Motion-Driven`, `Aurora UI`
- Colour mood: `Vibrant + Brand colors`
- Typography mood: `Modern + Bold typography`
- Key effects: `Engagement counter animations`; `Profile reveals`
- Landing & dashboard: landing `Social Proof-Focused`; dashboard `User Behavior Analytics`
- Decision rules: Always → `creator profiles`, `monetization display`
- Anti-patterns (`MEDIUM`): avoid `Generic layout`; `Hidden earnings`
- Key considerations: Creator profiles. Monetization display. Engagement metrics. Social proof.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 569. Dating App
- Recommended pattern: `Social Proof + Feature-Rich`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Aurora UI`, `Glassmorphism`
- Colour mood: `Warm + Romantic (Pink/Red gradients)`
- Typography mood: `Modern + Friendly typography`
- Key effects: `Profile card swipe`; `Match animations`
- Landing & dashboard: landing `Social Proof-Focused`; dashboard `User Behavior Analytics`
- Decision rules: Always → `profile cards`, `safety features`
- Anti-patterns (`HIGH`): avoid `Generic profiles`; `No safety`
- Key considerations: Profile cards. Swipe interactions. Match animations. Safety features. Video chat.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 570. Membership/Community
- Recommended pattern: `Social Proof + Conversion`
- Style priority: `Vibrant & Block-based` → `Soft UI Evolution`; secondary `Bento Box Grid`, `Micro-interactions`
- Colour mood: `Community brand colors + Engagement`; palette focus `Community brand colors + Engagement accents`
- Typography mood: `Friendly + Engaging typography`
- Key effects: `Member counter`; `Benefit reveals`
- Landing & dashboard: landing `Social Proof-Focused + Conversion`; dashboard `Community Analytics`
- Decision rules: Always → `member benefits`, `pricing tiers`
- Anti-patterns (`HIGH`): avoid `Hidden benefits`; `No community proof`
- Key considerations: Member benefits. Pricing tiers. Community showcase. Events. Member directory. Exclusive content.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 571. Chat & Messaging App
- Recommended pattern: `Feature-Rich Showcase + Demo`
- Style priority: `Minimalism & Swiss Style` → `Micro-interactions`; secondary `Glassmorphism`, `Flat Design`
- Colour mood: `Brand primary + bubble contrast (sender/receiver) + typing grey`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle hover 200ms`; `Smooth transitions`; `Clean`
- Landing & dashboard: landing `Feature-Rich Showcase + Demo`; dashboard `User Behavior Analytics`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Bubble UI (left/right alignment). Typing indicators. Read receipts (✓✓). Image/file preview. Emoji reactions. Group avatars. Online status dots. Swipe-to-reply.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 572. Link-in-Bio Page Builder
- Recommended pattern: `Conversion-Optimized + Social Proof`
- Style priority: `Vibrant & Block-based` → `Bento Box Grid`; secondary `Minimalism & Swiss Style`, `Glassmorphism`
- Colour mood: `Brand-customizable + accent link color + clean white canvas`
- Typography mood: `Energetic + Bold + Large`
- Key effects: `Large section gaps 48px`; `Color shift hover`; `Scroll-snap`
- Landing & dashboard: landing `Conversion-Optimized + Social Proof`; dashboard `Analytics (click tracking)`
- Decision rules: If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`; If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Drag-drop builder. Theme templates. Click analytics. Custom domain. Social icon integration. QR code export.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 573. Couple & Relationship App
- Recommended pattern: `Storytelling-Driven + Social Proof`
- Style priority: `Aurora UI` → `Soft UI Evolution`; secondary `Claymorphism`, `Glassmorphism`
- Colour mood: `Warm romantic pink/rose + soft gradient + memory photo tones`
- Typography mood: `Elegant + Gradient-friendly`
- Key effects: `Flowing gradients 8-12s`; `Color morphing`
- Landing & dashboard: landing `Storytelling-Driven + Social Proof`; dashboard `N/A - Couple focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Shared timeline. Anniversary countdowns. Secret chat. Photo albums. Love language quiz. Date night ideas.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 574. Anonymous Community / Confession
- Recommended pattern: `Social Proof-Focused + Feature-Rich`
- Style priority: `Dark Mode (OLED)` → `Minimalism & Swiss Style`; secondary `Glassmorphism`, `Soft UI Evolution`
- Colour mood: `Dark protective + subtle gradient + upvote green + empathy warm accent`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Social Proof-Focused + Feature-Rich`; dashboard `User Behavior Analytics`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`; If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Pure white backgrounds`
- Key considerations: Anonymous posting with moderation. Safety reporting. Reaction system. Trending topics. Mental health resources link.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 575. Forum / Discussion Board
- Recommended pattern: `Community/Forum Landing`
- Style priority: `Dark Mode (OLED)` → `Flat Design`; primary recommendation `Dark Mode (OLED)` + `Minimalism & Swiss Style`; secondary `Flat Design`, `Vibrant & Block-based`
- Colour mood: `Dark neutral + topic accent colors + unread indicator + reputation badge`
- Typography mood: `Readable + Community-first typography`
- Key effects: `Thread expand/collapse`; `Reply composer cues`
- Landing & dashboard: landing `Feed + Thread View`; dashboard `N/A - Discussion focused`
- Decision rules: Always → `thread list`, `reply composer`, `vote signals`, `moderation tools`, `user badges`; If content focused (brief mentions content, article, reading, documentation) → `prioritize clarity`; If ux focused (brief mentions ux, usability, accessibility, accessible) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `No moderation cues`; `cluttered threads`; `hidden post state`
- Key considerations: Thread list with pagination. Rich text editor. Quote/mention system. Upvote/downvote. User badges. Moderation tools.
- Rationale: discussion UX depends on scan-friendly threads, reputation cues, and visible moderation states (confidence `0.93`)
- RTL: `full` — mirrors cleanly; no directional rework needed

## 576. Q&A Community Platform
- Recommended pattern: `Community/Forum Landing`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Dark Mode (OLED)`, `Accessible & Ethical`
- Colour mood: `Clean white + upvote orange + accepted green + reputation gold + tag colors`
- Typography mood: `Readable + Code-friendly typography`
- Key effects: `Vote count emphasis`; `code-block highlighting`
- Landing & dashboard: landing `Feed + Thread View`; dashboard `Community Analytics Dashboard`
- Decision rules: Always → `vote count`, `code blocks`, `tag filter`, `accepted answer`, `bookmark save`; If content focused (brief mentions content, article, reading, documentation) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `No code support`; `poor vote clarity`; `hidden accepted answer`
- Key considerations: Question list with vote count. Rich code blocks. Tag filter. Reputation system. Accepted answer highlight. Comment threads. Bookmark/save.
- Rationale: Q&A works when answer ranking, code readability, and tag discovery are all obvious (confidence `0.93`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

# Part 59 — Travel, Mobility & Hospitality

## 577. EV/Charging Ecosystem
- Recommended pattern: `Hero-Centric + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Aurora UI`; secondary `Glassmorphism`, `Organic Biophilic`
- Colour mood: `Electric Blue (#009CD1) + Green`
- Typography mood: `Modern + Clear typography`
- Key effects: `Range estimation animations`; `Map interactions`
- Landing & dashboard: landing `Hero-Centric Design`; dashboard `Energy/Utilities Dashboard`
- Decision rules: Always → `charging map`, `range calculator`
- Anti-patterns (`HIGH`): avoid `Poor map UX`; `Hidden costs`
- Key considerations: Charging station maps. Range estimation. Cost calculation. Environmental impact.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 578. Travel/Tourism Agency
- Recommended pattern: `Storytelling-Driven + Hero`
- Style priority: `Aurora UI` → `Motion-Driven`; secondary `Vibrant & Block-based`, `Glassmorphism`
- Colour mood: `Vibrant destination + Sky Blue`; palette focus `Vibrant destination colors + Sky Blue + Warm accents`
- Typography mood: `Inspirational + Engaging`
- Key effects: `Destination parallax`; `Itinerary animations`
- Landing & dashboard: landing `Storytelling-Driven + Hero-Centric`; dashboard `Booking Analytics`
- Decision rules: If experience focused (brief mentions experience, immersive, journey) → lead with `Parallax Storytelling` style; Always → `mobile booking`
- Anti-patterns (`HIGH`): avoid `Generic photos`; `Complex booking`
- Key considerations: Destination showcase. Booking system. Itinerary builder. Reviews. Inspiration galleries. Mobile-first.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 579. Hotel/Hospitality
- Recommended pattern: `Hero-Centric + Social Proof`
- Style priority: `Liquid Glass` → `Minimalism & Swiss Style`; secondary `Glassmorphism`, `Soft UI Evolution`
- Colour mood: `Warm neutrals + Gold (#D4AF37)`; palette focus `Warm neutrals + Gold (#D4AF37) + Brand accent`
- Typography mood: `Elegant + Welcoming typography`
- Key effects: `Room gallery`; `Amenity reveals`
- Landing & dashboard: landing `Hero-Centric Design + Social Proof`; dashboard `Revenue Management Dashboard`
- Decision rules: Always → `room booking`, `virtual tour`
- Anti-patterns (`HIGH`): avoid `Poor photos`; `Complex booking`
- Key considerations: Room booking. Amenities showcase. Location maps. Guest reviews. Seasonal pricing. Luxury imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 580. Airline
- Recommended pattern: `Conversion + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Glassmorphism`; secondary `Motion-Driven`, `Accessible & Ethical`
- Colour mood: `Sky Blue + Brand colors + Trust`; palette focus `Sky Blue + Brand colors + Trust accents`
- Typography mood: `Clear + Professional typography`
- Key effects: `Flight search animations`; `Boarding pass reveals`
- Landing & dashboard: landing `Conversion-Optimized + Feature-Rich`; dashboard `Operations Dashboard`
- Decision rules: Always → `flight search`, `mobile first`
- Anti-patterns (`HIGH`): avoid `Complex booking`; `Poor mobile`
- Key considerations: Flight search. Booking. Check-in. Boarding pass. Loyalty program. Route maps. Mobile-first.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 581. Ride Hailing / Transportation
- Recommended pattern: `Conversion-Optimized + Demo`
- Style priority: `Minimalism & Swiss Style` → `Glassmorphism`; secondary `Dark Mode (OLED)`, `Motion-Driven`
- Colour mood: `Brand primary + map neutral + status indicator colors`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Backdrop blur (10-20px)`; `Translucent overlays`
- Landing & dashboard: landing `Conversion-Optimized + Demo`; dashboard `Real-Time Monitoring + Map`
- Decision rules: If low performance (brief mentions low performance, low-end, slow device) → lead with `Flat Design` style; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Map-centric full-screen UI. Pickup/dropoff pins + route polyline. Driver card (photo/rating/vehicle). Fare estimate. Trip timer. Safety SOS button. Payment sheet.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 582. Parking Finder
- Recommended pattern: `Conversion-Optimized + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Glassmorphism`; secondary `Flat Design`, `Micro-interactions`
- Colour mood: `Trust blue + available green + occupied red + map neutral`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Backdrop blur (10-20px)`; `Translucent overlays`
- Landing & dashboard: landing `Conversion-Optimized + Feature-Rich`; dashboard `Real-Time Monitoring + Map`
- Decision rules: If low performance (brief mentions low performance, low-end, slow device) → lead with `Flat Design` style; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Real-time availability. In-app navigation. Payment integration. Parking timer alert. Favorite spots. Street vs garage.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 583. Public Transit Guide
- Recommended pattern: `Feature-Rich Showcase + Interactive Demo`
- Style priority: `Flat Design` → `Accessible & Ethical`; secondary `Minimalism & Swiss Style`, `Motion-Driven`
- Colour mood: `Transit brand line colors + real-time indicator green/red + map neutral`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase + Interactive Demo`; dashboard `Real-Time Monitoring + Map`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`; `Color-only indicators`
- Key considerations: Real-time arrivals. Offline maps. Disruption alerts. Multi-modal routing. Fare calculation. Accessibility features.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 584. Road Trip Planner
- Recommended pattern: `Storytelling-Driven + Hero-Centric`
- Style priority: `Aurora UI` → `Organic Biophilic`; secondary `Motion-Driven`, `Vibrant & Block-based`
- Colour mood: `Adventure warm sunset orange + map teal + stop markers + road neutral`
- Typography mood: `Elegant + Gradient-friendly`
- Key effects: `Flowing gradients 8-12s`; `Color morphing`
- Landing & dashboard: landing `Storytelling-Driven + Hero-Centric`; dashboard `N/A - Trip focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Route planning with stops. Point-of-interest discovery. Gas/food/hotel along route. Offline maps. Trip sharing.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

# Part 60 — Food & Beverage

## 585. Restaurant/Food Service
- Recommended pattern: `Hero-Centric + Conversion`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Claymorphism`, `Flat Design`
- Colour mood: `Warm colors (Orange Red Brown)`; palette focus `Warm colors (Orange Red Brown) + appetizing imagery`
- Typography mood: `Appetizing + Clear typography`
- Key effects: `Food image reveal`; `Menu hover effects`
- Landing & dashboard: landing `Hero-Centric Design + Conversion`; dashboard `N/A - Booking focused`
- Decision rules: Always → `high quality images`; If delivery (brief mentions delivery, courier, shipping) → `emphasize speed`
- Anti-patterns (`HIGH`): avoid `Low-quality imagery`; `Outdated hours`
- Key considerations: Menu display. Online ordering. Reservation system. Food photography. Location/hours prominent.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 586. Bakery/Cafe
- Recommended pattern: `Hero-Centric + Conversion`
- Style priority: `Vibrant & Block-based` → `Soft UI Evolution`; secondary `Claymorphism`, `Motion-Driven`
- Colour mood: `Warm Brown + Cream + Appetizing accents`
- Typography mood: `Warm + Inviting typography`
- Key effects: `Menu hover`; `Order animations`
- Landing & dashboard: landing `Hero-Centric Design + Conversion`; dashboard `N/A - Order focused`
- Decision rules: Always → `menu display`, `online ordering`
- Anti-patterns (`HIGH`): avoid `Poor food photos`; `Hidden hours`
- Key considerations: Menu display. Online ordering. Location/hours. Catering. Seasonal specials. Appetizing photography.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 587. Brewery/Winery
- Recommended pattern: `Storytelling + Hero-Centric`
- Style priority: `Motion-Driven` → `Vintage Analog / Retro Film`; secondary `Dark Mode (OLED)`, `Organic Biophilic`
- Colour mood: `Deep amber/burgundy + Gold + Craft`; palette focus `Deep amber/burgundy + Gold + Craft aesthetic`
- Typography mood: `Artisanal + Heritage typography`
- Key effects: `Tasting note reveals`; `Heritage timeline`
- Landing & dashboard: landing `Storytelling-Driven + Hero-Centric`; dashboard `N/A - E-commerce focused`
- Decision rules: Always → `product showcase`, `story heritage`
- Anti-patterns (`HIGH`): avoid `Generic product pages`; `No story`
- Key considerations: Product showcase. Story/heritage. Tasting notes. Events. Club membership. Artisanal imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 588. Food Delivery / On-Demand
- Recommended pattern: `Hero-Centric Design + Feature-Rich`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Glassmorphism`, `Flat Design`
- Colour mood: `Appetizing warm (orange/red) + trust blue + map accent`
- Typography mood: `Energetic + Bold + Large`
- Key effects: `Scroll animations`; `Parallax`; `Page transitions`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Real-Time Monitoring + Map`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Restaurant cards with ratings. Menu category horizontal scroll. Cart bottom sheet. Real-time map tracking + driver ETA. Order status stepper. Rating post-delivery.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 589. Recipe & Cooking App
- Recommended pattern: `Hero-Centric Design + Feature-Rich`
- Style priority: `Claymorphism` → `Vibrant & Block-based`; secondary `Soft UI Evolution`, `Organic Biophilic`
- Colour mood: `Warm food tones (terracotta/sage/cream) + appetizing imagery`
- Typography mood: `Playful + Rounded + Friendly`
- Key effects: `Multi-layer shadows`; `Spring bounce`; `Soft press 200ms`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `N/A - Content focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Step-by-step with checkable instructions. Ingredient list with serving adjuster. Built-in timer per step. Cooking mode (screen-awake + large text). Save/bookmark. Share.
- RTL: `full` — mirrors cleanly; no directional rework needed

# Part 61 — Real Estate, Home & Local Services

## 590. Hyperlocal Services
- Recommended pattern: `Conversion + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Vibrant & Block-based`; secondary `Micro-interactions`, `Flat Design`
- Colour mood: `Location markers + Trust colors`
- Typography mood: `Clear + Functional typography`
- Key effects: `Map hover`; `Provider card reveals`
- Landing & dashboard: landing `Conversion-Optimized`; dashboard `Drill-Down Analytics + Map`
- Decision rules: Always → `map integration`, `booking system`
- Anti-patterns (`HIGH`): avoid `No map`; `Hidden reviews`
- Key considerations: Map integration. Service categories. Provider profiles. Booking system. Reviews.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 591. Real Estate/Property
- Recommended pattern: `Hero-Centric + Feature-Rich`
- Style priority: `Glassmorphism` → `Minimalism & Swiss Style`; secondary `Motion-Driven`, `3D & Hyperrealism`
- Colour mood: `Trust Blue + Gold + White`; palette focus `Trust Blue (#0077B6) + Gold accents + White`
- Typography mood: `Professional + Confident`
- Key effects: `3D property tour zoom`; `Map hover`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Sales Intelligence Dashboard`
- Decision rules: If luxury (brief mentions luxury, premium, high-end) → `add 3d models`; Always → `map integration`
- Anti-patterns (`HIGH`): avoid `Poor photos`; `No virtual tours`
- Key considerations: Property listings. Virtual tours. Map integration. Agent profiles. Mortgage calculator. High-quality imagery.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 592. Construction/Architecture
- Recommended pattern: `Hero-Centric + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `3D & Hyperrealism`; secondary `Brutalism`, `Swiss Modernism 2.0`
- Colour mood: `Grey (#4A4A4A) + Orange (safety) + Blueprint Blue`
- Typography mood: `Professional + Bold typography`
- Key effects: `3D model viewer`; `Timeline animations`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Project Management Dashboard`
- Decision rules: Always → `project portfolio`; If team collaboration (brief mentions team collaboration, team workspace) → `add real time updates`
- Anti-patterns (`HIGH`): avoid `2D-only layouts`; `Poor image quality`; `AI purple/pink gradients`
- Key considerations: Project portfolio. 3D renders. Timeline. Material specs. Team collaboration. Blueprint aesthetic.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 593. Coworking Space
- Recommended pattern: `Hero-Centric + Feature-Rich`
- Style priority: `Vibrant & Block-based` → `Glassmorphism`; secondary `Minimalism & Swiss Style`, `Motion-Driven`
- Colour mood: `Energetic colors + Wood tones + Brand`; palette focus `Energetic colors + Wood tones + Brand accent`
- Typography mood: `Modern + Engaging typography`
- Key effects: `Space tour video`; `Amenity reveal animations`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Occupancy Dashboard`
- Decision rules: Always → `virtual tour`, `booking system`
- Anti-patterns (`MEDIUM`): avoid `Outdated photos`; `Confusing layout`
- Key considerations: Space tour. Membership plans. Booking system. Amenities. Community events. Virtual tour.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 594. Home Services (Plumber/Electrician)
- Recommended pattern: `Conversion-Optimized + Trust`
- Style priority: `Flat Design` → `Accessible & Ethical`; secondary `Minimalism & Swiss Style`, `Accessible & Ethical`
- Colour mood: `Trust Blue + Safety Orange + Grey`; palette focus `Trust Blue + Safety Orange + Professional grey`
- Typography mood: `Professional + Clear typography`
- Key effects: `Emergency contact highlight`; `Service menu animations`
- Landing & dashboard: landing `Conversion-Optimized + Trust`; dashboard `Service Analytics`
- Decision rules: Always → `emergency contact`, `certifications display`
- Anti-patterns (`HIGH`): avoid `Hidden contact info`; `No certifications`
- Key considerations: Service list. Emergency contact. Booking. Price transparency. Certifications. Local trust signals.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 595. Architecture / Interior
- Recommended pattern: `Portfolio + Hero-Centric`
- Style priority: `Exaggerated Minimalism` → `3D & Hyperrealism`; secondary `Swiss Modernism 2.0`, `Parallax Storytelling`
- Colour mood: `Monochrome + Gold Accent + High Imagery`
- Typography mood: `Architectural + Elegant typography`
- Key effects: `Project gallery`; `Blueprint reveals`
- Landing & dashboard: landing `Portfolio Grid + Visuals`; dashboard `Project Management + Gallery`
- Decision rules: Always → `high res images`, `project portfolio`
- Anti-patterns (`HIGH`): avoid `Poor imagery`; `Cluttered layout`
- Key considerations: High-res images. Typography. Space.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 596. Home Decoration & Interior Design
- Recommended pattern: `Storytelling-Driven + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `3D Product Preview`; secondary `Organic Biophilic`, `Aurora UI`
- Colour mood: `Neutral interior palette + material texture accent + AR blue`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle hover 200ms`; `Smooth transitions`; `Clean`
- Landing & dashboard: landing `Storytelling-Driven + Feature-Rich`; dashboard `N/A - Project focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: AR room visualization. Style quiz. Product catalog with purchase links. 3D room planner. Mood board. Before/after.
- RTL: `full` — mirrors cleanly; no directional rework needed

# Part 62 — Professional Services & Careers

## 597. Legal Services
- Recommended pattern: `Trust & Authority + Minimal`
- Style priority: `Accessible & Ethical` → `Minimalism & Swiss Style`; secondary `Accessible & Ethical`, `Swiss Modernism 2.0`
- Colour mood: `Navy Blue (#1E3A5F) + Gold + White`
- Typography mood: `Professional + Authoritative typography`
- Key effects: `Practice area reveal`; `Attorney profile animations`
- Landing & dashboard: landing `Trust & Authority + Minimal`; dashboard `Case Management Dashboard`
- Decision rules: Always → `case results`, `credential display`
- Anti-patterns (`HIGH`): avoid `Outdated design`; `Hidden credentials`; `AI purple/pink gradients`
- Key considerations: Credibility paramount. Practice areas. Attorney profiles. Case results. Contact forms. Professional imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 598. Job Board/Recruitment
- Recommended pattern: `Conversion-Optimized + Feature-Rich`
- Style priority: `Flat Design` → `Minimalism & Swiss Style`; secondary `Vibrant & Block-based`, `Accessible & Ethical`
- Colour mood: `Professional Blue + Success Green + Neutral`
- Typography mood: `Clear + Professional typography`
- Key effects: `Search/filter animations`; `Application flow`
- Landing & dashboard: landing `Conversion-Optimized + Feature-Rich`; dashboard `HR Analytics Dashboard`
- Decision rules: Always → `advanced search`; If salary focused (brief mentions salary, compensation, pay range) → `highlight compensation`
- Anti-patterns (`HIGH`): avoid `Outdated forms`; `Hidden filters`
- Key considerations: Job listings. Search/filter. Company profiles. Application tracking. Resume upload. Salary insights.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 599. Freelancer Platform
- Recommended pattern: `Feature-Rich + Conversion`
- Style priority: `Flat Design` → `Minimalism & Swiss Style`; secondary `Vibrant & Block-based`, `Micro-interactions`
- Colour mood: `Professional Blue + Success Green`; palette focus `Professional Blue + Success Green + Neutral`
- Typography mood: `Clear + Professional typography`
- Key effects: `Skill match animations`; `Review reveals`
- Landing & dashboard: landing `Feature-Rich Showcase + Conversion`; dashboard `Marketplace Analytics`
- Decision rules: Always → `portfolio display`, `skill matching`
- Anti-patterns (`HIGH`): avoid `Poor profiles`; `No reviews`
- Key considerations: Profile creation. Portfolio. Skill matching. Messaging. Payment. Reviews. Project management.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 600. Resume / CV Builder
- Recommended pattern: `Product Demo + Features`
- Style priority: `Minimalism & Swiss Style` → `Accessible & Ethical`; primary recommendation `Minimalism & Swiss Style` + `Flat Design`; secondary `Swiss Modernism 2.0`, `Accessible & Ethical`
- Colour mood: `Professional navy + section accent + success green + clean white`
- Typography mood: `Professional + Resume-friendly typography`
- Key effects: `Real-time preview`; `ATS score indicator`
- Landing & dashboard: landing `Interactive Product Demo + CTA`; dashboard `Template Selection Gallery`
- Decision rules: Always → `template picker`, `section editor`, `real time preview`, `ats score`, `pdf export`; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add progress animation`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`
- Anti-patterns (`HIGH`): avoid `No live preview`; `weak ATS signals`; `decorative clutter`
- Key considerations: Template picker. Section-by-section editor. Real-time preview. ATS score indicator. PDF export. Cover letter generator. Import from LinkedIn.
- Rationale: resume tools need immediate feedback, export confidence, and minimal layout noise (confidence `0.92`)
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

# Part 63 — Government, Nonprofit & Institutions

## 601. Government/Public Service
- Recommended pattern: `Minimal & Direct`
- Style priority: `Accessible & Ethical` → `Minimalism & Swiss Style`; secondary `Flat Design`, `Inclusive Design`
- Colour mood: `Professional blue + High contrast`
- Typography mood: `Clear + Large typography`
- Key effects: `Clear focus rings (3-4px)`; `Skip links`
- Landing & dashboard: landing `Minimal & Direct`; dashboard `Executive Dashboard`
- Decision rules: Always → `wcag aaa`, `keyboard navigation`
- Anti-patterns (`HIGH`): avoid `Ornate design`; `Low contrast`; `Motion effects`; `AI purple/pink gradients`
- Key considerations: WCAG AAA mandatory. Trust paramount.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 602. Non-profit/Charity
- Recommended pattern: `Storytelling + Trust`
- Style priority: `Accessible & Ethical` → `Organic Biophilic`; secondary `Minimalism & Swiss Style`, `Editorial Grid / Magazine`
- Colour mood: `Cause-related colors + Trust + Warm`
- Typography mood: `Heartfelt + Readable typography`
- Key effects: `Impact counter animations`; `Story reveals`
- Landing & dashboard: landing `Storytelling-Driven + Trust`; dashboard `Donation Analytics Dashboard`
- Decision rules: Always → `impact stories`, `donation transparency`
- Anti-patterns (`HIGH`): avoid `No impact data`; `Hidden financials`
- Key considerations: Impact stories. Donation flow. Transparency reports. Volunteer signup. Event calendar. Emotional connection.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 603. Church/Religious Organization
- Recommended pattern: `Hero-Centric + Social Proof`
- Style priority: `Accessible & Ethical` → `Soft UI Evolution`; secondary `Minimalism & Swiss Style`, `Inclusive Design`
- Colour mood: `Warm Gold + Deep Purple/Blue + White`
- Typography mood: `Welcoming + Clear typography`
- Key effects: `Service time highlights`; `Event calendar`
- Landing & dashboard: landing `Hero-Centric Design + Social Proof`; dashboard `N/A - Community focused`
- Decision rules: Always → `service times`, `community events`
- Anti-patterns (`MEDIUM`): avoid `Outdated design`; `Hidden info`
- Key considerations: Service times. Events. Sermons. Community. Giving. Location. Welcoming imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 604. Citizen Science Platform
- Recommended pattern: `Scroll-Triggered Storytelling`
- Style priority: `Organic Biophilic` → `Motion-Driven`; primary recommendation `Organic Biophilic` + `Vibrant & Block-based`; secondary `Claymorphism`, `Motion-Driven`
- Colour mood: `Earth green + discovery orange + volunteer badge blue + data neutral`
- Typography mood: `Readable + Community-first typography`
- Key effects: `Progress badges`; `contribution feedback`
- Landing & dashboard: landing `Storytelling-Driven + Social Proof`; dashboard `Project Participation Dashboard`
- Decision rules: Always → `project cards`, `contribution tracker`, `data quality feedback`, `community forums`, `leaderboards`; If engagement metric (brief mentions engagement, retention, contribution) → `add progress animation`; If content focused (brief mentions content, article, reading, documentation) → `increase playfulness`
- Anti-patterns (`MEDIUM`): avoid `No progress feedback`; `reward-less contributions`
- Key considerations: Project cards with impact metrics. Contribution tracker. Beginner-friendly onboarding. Data quality feedback loop. Leaderboards. Community forums.
- Rationale: participation loops need visible impact, feedback, and lightweight community momentum (confidence `0.89`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 605. Crowdfunding Platform
- Recommended pattern: `Scroll-Triggered Storytelling`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Claymorphism`, `Editorial Grid / Magazine`
- Colour mood: `Brand primary + funding progress green + urgency amber + reward tier colors`
- Typography mood: `Emotional + High-contrast typography`
- Key effects: `Progress bar`; `reward-tier animations`
- Landing & dashboard: landing `Storytelling-Driven + Social Proof`; dashboard `Campaign Analytics Dashboard`
- Decision rules: Always → `progress bar`, `reward tier selector`, `backer count`, `countdown timer`, `updates feed`; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`; If engagement metric (brief mentions engagement, retention, contribution) → `add progress animation`
- Anti-patterns (`HIGH`): avoid `Static design`; `no progress bar`; `weak social proof`
- Key considerations: Funding progress bar with % goal. Reward tier selector. Backer count. Countdown timer. Updates feed. Creator profile. Risk/disclaimer section.
- Rationale: crowdfunding conversion rises when progress, scarcity, and creator story stay visible (confidence `0.92`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 606. Government Portal / Civic Services
- Recommended pattern: `Enterprise Gateway`
- Style priority: `Accessible & Ethical` → `Inclusive Design`; secondary `Flat Design`, `Inclusive Design`
- Colour mood: `Professional blue + accessibility high contrast + service category colors`
- Typography mood: `Clear + Large typography`
- Key effects: `Skip-link focus states`; `save-progress forms`
- Landing & dashboard: landing `Service Directory + Search`; dashboard `N/A - Service focused`
- Decision rules: Always → `plain language copy`, `service a z`, `save progress`, `document upload`, `appointment booking`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Ornate design`; `low contrast`; `motion effects`; `AI purple/pink gradients`
- Key considerations: Multilingual toggle. Service A-Z index. Form wizard with save-progress. Document upload. Appointment booking. Status tracker. WCAG AAA. Plain language.
- Rationale: civic flows must stay plain, accessible, and resilient for interrupted form completion (confidence `0.95`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 607. Grant / Funding Portal
- Recommended pattern: `Marketplace / Directory`
- Style priority: `Accessible & Ethical` → `Swiss Modernism 2.0`; primary recommendation `Accessible & Ethical` + `Minimalism & Swiss Style`; secondary `Accessible & Ethical`, `Swiss Modernism 2.0`
- Colour mood: `Institution navy + funding green + deadline red + neutral white`
- Typography mood: `Formal + Clear typography`
- Key effects: `Deadline countdown`; `status tracking`
- Landing & dashboard: landing `Opportunity Grid + Search`; dashboard `Application Tracking Dashboard`
- Decision rules: Always → `opportunity cards`, `eligibility checker`, `deadline countdown`, `application wizard`, `status tracker`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`HIGH`): avoid `No deadlines`; `no eligibility clarity`; `buried docs`
- Key considerations: Funding opportunity cards. Eligibility checker. Deadline countdown. Application form wizard. Document checklist. Review status tracker. Award announcement feed.
- Rationale: funding portals need deadline visibility, eligibility clarity, and a strong evidence trail (confidence `0.92`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 608. Patent / IP Database
- Recommended pattern: `Marketplace / Directory`
- Style priority: `Swiss Modernism 2.0` → `Data-Dense Dashboard`; primary recommendation `Swiss Modernism 2.0` + `Minimalism & Swiss Style`; secondary `Editorial Grid / Magazine`, `Data-Dense Dashboard`
- Colour mood: `Formal neutral + patent type chips + status badges`; palette focus `Formal neutral + patent type chips + status badges (granted/pending/rejected)`
- Typography mood: `Formal + Search-friendly typography`
- Key effects: `Full-text search highlight`; `citation graph`
- Landing & dashboard: landing `Search-First + Results Grid`; dashboard `N/A - Search focused`
- Decision rules: Always → `full text search`, `classification tree`, `citation graph`, `prior art comparison`, `legal status tracker`; If data heavy (brief mentions data heavy, data-heavy, analytics, large dataset) → `virtualize lists`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`
- Anti-patterns (`HIGH`): avoid `No search`; `no citation graph`; `visual clutter`
- Key considerations: Full-text patent search. Classification tree. Citation graph. Prior art comparison. Patent family view. PDF download. Legal status tracker.
- Rationale: IP discovery depends on precise search, citation context, and legal-status visibility (confidence `0.89`)
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 609. Research Lab / University Department
- Recommended pattern: `Portfolio Grid`
- Style priority: `Swiss Modernism 2.0` → `Editorial Grid / Magazine`; primary recommendation `Swiss Modernism 2.0` + `Minimalism & Swiss Style`; secondary `Editorial Grid / Magazine`, `Accessible & Ethical`
- Colour mood: `Institutional navy + white + research-area accents + serif headings`; palette focus `Institutional navy + white + research area accent colors + serif headings`
- Typography mood: `Academic + Clear typography`
- Key effects: `Publication cards`; `people grid`
- Landing & dashboard: landing `Overview + People + Publications`; dashboard `N/A - Academic focused`
- Decision rules: Always → `pi bio`, `member grid`, `publication list`, `open positions`, `funding acknowledgments`; If content focused (brief mentions content, article, reading, documentation) → `prioritize clarity`; If trust needed (brief mentions trust, secure, verified, authority) → `reduce motion`
- Anti-patterns (`MEDIUM`): avoid `Low hierarchy`; `no publication filtering`; `cluttered visuals`
- Key considerations: PI bio and research focus. Current members grid. Publication list with links. Open positions. Lab facilities photos. Funding acknowledgments.
- Rationale: lab pages must present publications, team structure, and open opportunities with high credibility (confidence `0.91`)
- RTL: `full` — mirrors cleanly; no directional rework needed

# Part 64 — Creative, Portfolio & Content Creation

## 610. Creative Agency
- Recommended pattern: `Storytelling-Driven`
- Style priority: `Brutalism` → `Motion-Driven`; secondary `Retro-Futurism`, `Editorial Grid / Magazine`
- Colour mood: `Bold primaries + Artistic freedom`
- Typography mood: `Bold + Expressive typography`
- Key effects: `CRT scanlines`; `Neon glow`; `Glitch effects`
- Landing & dashboard: landing `Storytelling-Driven`; dashboard `N/A - Portfolio focused`
- Decision rules: Always → `case studies`; If boutique (brief mentions boutique) → `increase artistic freedom`
- Anti-patterns (`HIGH`): avoid `Corporate minimalism`; `Hidden portfolio`
- Key considerations: Differentiation key. Wow-factor necessary.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 611. Portfolio/Personal
- Recommended pattern: `Storytelling-Driven`
- Style priority: `Motion-Driven` → `Minimalism & Swiss Style`; secondary `Brutalism`, `Aurora UI`
- Colour mood: `Brand primary + Artistic`; palette focus `Brand primary + artistic interpretation`
- Typography mood: `Expressive + Variable typography`
- Key effects: `Parallax (3-5 layers)`; `Scroll-triggered reveals`
- Landing & dashboard: landing `Storytelling-Driven`; dashboard `N/A - Personal branding`
- Decision rules: If creative field (brief mentions creative, artist, portfolio) → lead with `Brutalism` style; If minimal portfolio (brief mentions minimal portfolio, simple portfolio) → `reduce motion`
- Anti-patterns (`MEDIUM`): avoid `Corporate templates`; `Generic layouts`
- Key considerations: Showcase work. Personality shine through.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 612. Photography Studio
- Recommended pattern: `Storytelling-Driven + Hero-Centric`
- Style priority: `Motion-Driven` → `Minimalism & Swiss Style`; secondary `Aurora UI`, `Glassmorphism`
- Colour mood: `Black + White + Minimal accent`
- Typography mood: `Elegant + Minimal typography`
- Key effects: `Full-bleed gallery`; `Before/after reveal`
- Landing & dashboard: landing `Storytelling-Driven + Hero-Centric`; dashboard `N/A - Portfolio focused`
- Decision rules: Always → `portfolio showcase`; If booking (brief mentions booking, appointment, calendar) → `add calendar system`
- Anti-patterns (`HIGH`): avoid `Heavy text`; `Poor image showcase`
- Key considerations: Portfolio gallery. Before/after. Service packages. Booking system. Client galleries. Full-bleed imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 613. Marketing Agency
- Recommended pattern: `Storytelling + Feature-Rich`
- Style priority: `Brutalism` → `Motion-Driven`; secondary `Vibrant & Block-based`, `Aurora UI`
- Colour mood: `Bold brand colors + Creative freedom`
- Typography mood: `Bold + Expressive typography`
- Key effects: `Portfolio reveals`; `Results animations`
- Landing & dashboard: landing `Storytelling-Driven + Feature-Rich`; dashboard `Campaign Analytics`
- Decision rules: Always → `portfolio`, `results metrics`
- Anti-patterns (`HIGH`): avoid `Boring design`; `Hidden work`
- Key considerations: Portfolio. Case studies. Services. Team. Creative showcase. Results-focused. Bold aesthetic.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 614. Generative Art Platform
- Recommended pattern: `Showcase + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Gen Z Chaos / Maximalism`; secondary `Bento Box Grid`, `Dark Mode (OLED)`
- Colour mood: `Neutral (#F5F5F5) + User Content`; palette focus `Neutral #F5F5F5 (Canvas) + User Content`
- Typography mood: `Minimal + Content-focused typography`
- Key effects: `Gallery masonry`; `Minting animations`
- Landing & dashboard: landing `Bento Grid Showcase`; dashboard `Gallery / Portfolio`
- Decision rules: Always → `fast loading`, `creator attribution`
- Anti-patterns (`HIGH`): avoid `Heavy chrome`; `Slow loading`
- Key considerations: Content is king. Fast loading. Creator attribution. Minting flow.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 615. Photo Editor & Filters
- Recommended pattern: `Feature-Rich Showcase + Interactive Demo`
- Style priority: `Minimalism & Swiss Style` → `Dark Mode (OLED)`; secondary `Motion-Driven`, `Flat Design`
- Colour mood: `Dark editor background + vibrant filter preview strip + tool icon accent`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Feature-Rich Showcase + Interactive Demo`; dashboard `N/A - Editor focused`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Pure white backgrounds`
- Key considerations: Non-destructive editing. Filter preview carousel. Histogram. RAW support. Batch export. Social share direct.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 616. Short Video Editor
- Recommended pattern: `Feature-Rich Showcase + Hero-Centric`
- Style priority: `Dark Mode (OLED)` → `Motion-Driven`; secondary `Vibrant & Block-based`, `Glassmorphism`
- Colour mood: `Dark background + timeline track accent colors + effect preview vivid`
- Typography mood: `High contrast + Light on dark`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Feature-Rich Showcase + Hero-Centric`; dashboard `N/A - Timeline editor focused`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`
- Anti-patterns (`HIGH`): avoid `Pure white backgrounds`
- Key considerations: Multi-track timeline. Licensed music library. Text overlays. Auto-captions. Export 9:16 / 16:9 / 1:1.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 617. Drawing & Sketching Canvas
- Recommended pattern: `Interactive Product Demo + Storytelling`
- Style priority: `Minimalism & Swiss Style` → `Dark Mode (OLED)`; secondary `Anti-Polish / Raw Aesthetic`, `Motion-Driven`
- Colour mood: `Neutral canvas + full-spectrum color picker + tool panel dark`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Interactive Product Demo + Storytelling`; dashboard `N/A - Canvas focused`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Pure white backgrounds`
- Key considerations: Pressure sensitivity. Infinite canvas (pan/zoom). Layer management. Undo history. Export PNG/PSD/SVG.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 618. Music Creation & Beat Maker
- Recommended pattern: `Interactive Product Demo + Storytelling`
- Style priority: `Dark Mode (OLED)` → `Motion-Driven`; secondary `Cyberpunk UI`, `Glassmorphism`
- Colour mood: `Dark studio background + track colors rainbow + waveform accent + BPM pulse`
- Typography mood: `High contrast + Light on dark`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Interactive Product Demo + Storytelling`; dashboard `N/A - DAW focused`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`
- Anti-patterns (`HIGH`): avoid `Pure white backgrounds`
- Key considerations: Touch piano and drum pad. Loop browser. MIDI support. Export MP3/WAV. Low-latency audio engine.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 619. Meme & Sticker Maker
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Vibrant & Block-based` → `Flat Design`; secondary `Gen Z Chaos / Maximalism`, `Claymorphism`
- Colour mood: `Bold primary + comedic yellow + viral red + high saturation accent`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `N/A - Creator focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`; `Muted colors`; `Low energy`
- Key considerations: Template library. Caption text overlay. Font variety. Reaction sticker packs. Share to all platforms. Fast creation.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 620. AI Photo & Avatar Generator
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `AI-Native UI` → `Aurora UI`; secondary `Glassmorphism`, `Minimalism & Swiss Style`
- Colour mood: `AI purple + aurora gradients + before/after neutral`
- Typography mood: `Elegant + Gradient-friendly`
- Key effects: `Flowing gradients 8-12s`; `Color morphing`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `N/A - Generation focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Style selection. Multiple output variations. Privacy policy prominent. Fast generation. Credits/subscription system.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 621. Wallpaper & Theme App
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Vibrant & Block-based` → `Aurora UI`; secondary `Glassmorphism`, `Motion-Driven`
- Colour mood: `Content-driven + trending aesthetic palettes + download accent`
- Typography mood: `Energetic + Bold + Large`
- Key effects: `Large section gaps 48px`; `Color shift hover`; `Scroll-snap`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `N/A - Gallery focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Category browsing. Preview on device. Daily wallpaper auto-set. Widget matching. Creator uploads. Resolution auto-fit.
- RTL: `full` — mirrors cleanly; no directional rework needed

# Part 65 — Gaming

## 622. Gaming
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `3D & Hyperrealism` → `Retro-Futurism`; secondary `Motion-Driven`, `Vibrant & Block-based`
- Colour mood: `Vibrant + Neon + Immersive`; palette focus `Vibrant + neon + immersive colors`
- Typography mood: `Bold + Impactful typography`
- Key effects: `WebGL 3D rendering`; `Glitch effects`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `N/A - Game focused`
- Decision rules: If competitive (brief mentions competitive, leaderboard) → `add real time stats`; If casual (brief mentions casual, playful) → `increase playfulness`
- Anti-patterns (`HIGH`): avoid `Minimalist design`; `Static assets`
- Key considerations: Immersion priority. Performance critical.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 623. Casual Puzzle Game
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Claymorphism` → `Vibrant & Block-based`; secondary `Micro-interactions`, `Motion-Driven`
- Colour mood: `Cheerful pastels + progression gradient + reward gold + bright accent`
- Typography mood: `Playful + Rounded + Friendly`
- Key effects: `Multi-layer shadows`; `Spring bounce`; `Soft press 200ms`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `N/A - Game focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Satisfying match/clear animations. Progressive difficulty. Daily challenges. No-skip tutorials. Offline play.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 624. Trivia & Quiz Game
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Vibrant & Block-based` → `Micro-interactions`; secondary `Claymorphism`, `Flat Design`
- Colour mood: `Energetic blue + correct green + incorrect red + leaderboard gold`
- Typography mood: `Energetic + Bold + Large`
- Key effects: `Haptic feedback`; `Small 50-100ms animations`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `Leaderboard Analytics`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Timer pressure UX. Category selection. Streak system. Real-time multiplayer. Daily quiz mode.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 625. Card & Board Game
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `3D & Hyperrealism` → `Flat Design`; secondary `Motion-Driven`, `Dark Mode (OLED)`
- Colour mood: `Game-theme felt green + dark wood + card back patterns`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `N/A - Game focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`
- Key considerations: Real-time or async multiplayer. Game state sync. Tutorial mode. Match history. ELO rating system.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 626. Idle & Clicker Game
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Claymorphism`, `3D & Hyperrealism`
- Colour mood: `Coin gold + upgrade blue + prestige purple + progress green`
- Typography mood: `Energetic + Bold + Large`
- Key effects: `Scroll animations`; `Parallax`; `Page transitions`
- Landing & dashboard: landing `Feature-Rich Showcase`; dashboard `N/A - Progress focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Offline progress calculation. Satisfying number animations. Upgrade tree clarity. Prestige system. Optional ads.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 627. Word & Crossword Game
- Recommended pattern: `Minimal & Direct + Demo`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Swiss Modernism 2.0`, `Micro-interactions`
- Colour mood: `Clean white + warm letter tiles + success green + shake red`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Minimal & Direct + Demo`; dashboard `N/A - Game focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Complex shadows`; `3D effects`
- Key considerations: Daily challenge with shareable results. Physical keyboard feel. Difficulty levels. Dictionary hints. Streak stats.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 628. Arcade & Retro Game
- Recommended pattern: `Feature-Rich Showcase + Hero-Centric`
- Style priority: `Pixel Art` → `Retro-Futurism`; secondary `Vibrant & Block-based`, `Motion-Driven`
- Colour mood: `Neon on black + pixel palette + score gold + danger red`
- Typography mood: `Nostalgic + Monospace + Neon`
- Key effects: `Subtle hover (200ms)`; `Smooth transitions`
- Landing & dashboard: landing `Feature-Rich Showcase + Hero-Centric`; dashboard `N/A - Score focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Instant play with no login. Game Center leaderboards. Haptic feedback on collision. Offline. Controller support.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

# Part 66 — Events, Entertainment & Culture

## 629. Wedding/Event Planning
- Recommended pattern: `Storytelling + Social Proof`
- Style priority: `Soft UI Evolution` → `Aurora UI`; secondary `Glassmorphism`, `Motion-Driven`
- Colour mood: `Soft Pink (#FFD6E0) + Gold + Cream`; palette focus `Soft Pink (#FFD6E0) + Gold + Cream + Sage`
- Typography mood: `Elegant + Romantic typography`
- Key effects: `Gallery reveals`; `Timeline animations`
- Landing & dashboard: landing `Storytelling-Driven + Social Proof`; dashboard `N/A - Planning focused`
- Decision rules: Always → `portfolio gallery`, `planning tools`
- Anti-patterns (`HIGH`): avoid `Generic templates`; `No portfolio`
- Key considerations: Portfolio gallery. Vendor directory. Planning tools. Timeline. Budget tracker. Romantic aesthetic.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 630. Event Management
- Recommended pattern: `Hero-Centric + Feature-Rich`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Glassmorphism`, `Aurora UI`
- Colour mood: `Event theme colors + Excitement accents`
- Typography mood: `Bold + Engaging typography`
- Key effects: `Countdown timer`; `Registration flow`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Event Analytics`
- Decision rules: Always → `registration`, `agenda display`
- Anti-patterns (`HIGH`): avoid `Confusing registration`; `No countdown`
- Key considerations: Event showcase. Registration. Agenda. Speakers. Sponsors. Ticket sales. Countdown timer.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 631. Sports Team/Club
- Recommended pattern: `Hero-Centric + Feature-Rich`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Dark Mode (OLED)`, `3D & Hyperrealism`
- Colour mood: `Team colors + Energetic accents`
- Typography mood: `Bold + Impactful typography`
- Key effects: `Score animations`; `Schedule reveals`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Performance Analytics`
- Decision rules: Always → `schedule`, `roster`
- Anti-patterns (`HIGH`): avoid `Static content`; `Poor fan engagement`
- Key considerations: Schedule. Roster. News. Tickets. Merchandise. Fan engagement. Action imagery.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 632. Museum/Gallery
- Recommended pattern: `Storytelling + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Motion-Driven`; secondary `Swiss Modernism 2.0`, `3D & Hyperrealism`
- Colour mood: `Art-appropriate neutrals + Exhibition accents`
- Typography mood: `Elegant + Minimal typography`
- Key effects: `Virtual tour`; `Collection reveals`
- Landing & dashboard: landing `Storytelling-Driven + Feature-Rich`; dashboard `Visitor Analytics`
- Decision rules: Always → `virtual tour`, `exhibition info`
- Anti-patterns (`HIGH`): avoid `Cluttered layout`; `No online access`
- Key considerations: Exhibitions. Collections. Tickets. Events. Virtual tours. Educational content. Art-focused design.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 633. Theater/Cinema
- Recommended pattern: `Hero-Centric + Conversion`
- Style priority: `Dark Mode (OLED)` → `Motion-Driven`; secondary `Vibrant & Block-based`, `Glassmorphism`
- Colour mood: `Dark + Spotlight accents + Gold`
- Typography mood: `Dramatic + Bold typography`
- Key effects: `Seat selection`; `Trailer reveals`
- Landing & dashboard: landing `Hero-Centric Design + Conversion`; dashboard `Booking Analytics`
- Decision rules: Always → `showtimes`, `seat selection`
- Anti-patterns (`HIGH`): avoid `Poor booking UX`; `No trailers`
- Key considerations: Showtimes. Seat selection. Trailers. Coming soon. Membership. Dramatic imagery.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 634. Local Events & Discovery
- Recommended pattern: `Hero-Centric Design + Feature-Rich`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Glassmorphism`, `Flat Design`
- Colour mood: `City vibrant + event category colors + map accent + date highlight`
- Typography mood: `Energetic + Bold + Large`
- Key effects: `Scroll animations`; `Parallax`; `Page transitions`
- Landing & dashboard: landing `Hero-Centric Design + Feature-Rich`; dashboard `Event Analytics`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Muted colors`; `Low energy`
- Key considerations: Location-based discovery. Category filters. RSVP flow. Map view. Friend attendance. Organizer tools. Reminders.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 635. Conference / Symposium Landing Page
- Recommended pattern: `Event/Conference Landing`
- Style priority: `Swiss Modernism 2.0` → `Accessible & Ethical`; primary recommendation `Swiss Modernism 2.0` + `Minimalism & Swiss Style`; secondary `Editorial Grid / Magazine`, `Accessible & Ethical`
- Colour mood: `Academic navy + track color chips + gold keynote + neutral white`
- Typography mood: `Academic + Hierarchical typography`
- Key effects: `Speaker grid`; `agenda reveal`
- Landing & dashboard: landing `Hero + Agenda + CFP`; dashboard `N/A - Event focused`
- Decision rules: Always → `speaker grid`, `multi track agenda`, `cfp countdown`, `venue map`, `sponsor tiers`; If trust needed (brief mentions trust, secure, verified, authority) → `prioritize clarity`; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`MEDIUM`): avoid `Ornate design`; `unclear schedule`; `hidden speaker info`
- Key considerations: Speaker grid. Multi-track agenda. CFP deadline countdown. Venue map. Sponsor tiers. Early-bird pricing. Proceedings download.
- Rationale: event pages need strong credibility, schedule clarity, and deadline pressure (confidence `0.90`)
- RTL: `full` — mirrors cleanly; no directional rework needed

## 636. Ticketing / Box Office
- Recommended pattern: `Event/Conference Landing`
- Style priority: `Vibrant & Block-based` → `Motion-Driven`; secondary `Dark Mode (OLED)`, `Glassmorphism`
- Colour mood: `Event theme colors + available green + sold-out red + seat map neutral`
- Typography mood: `Bold + Event typography`
- Key effects: `Seat-map hover states`; `countdown urgency`
- Landing & dashboard: landing `Event Grid + Seat Map`; dashboard `Sales Analytics Dashboard`
- Decision rules: Always → `event cards`, `seat map`, `cart countdown`, `qr ticket`, `refund policy`; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `No seat-map feedback`; `hidden fees`; `weak mobile`
- Key considerations: Event cards with date/venue. Interactive seat map. Cart with countdown. QR code ticket. Will-call pickup. Group discounts. Refund policy.
- Rationale: ticketing must make inventory, urgency, and purchase confidence visible at once (confidence `0.93`)
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

# Part 67 — Personal Productivity, Utilities & Privacy

## 637. Notes & Writing App
- Recommended pattern: `Minimal & Direct`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Swiss Modernism 2.0`, `Soft UI Evolution`
- Colour mood: `Clean white/cream + minimal accent + editor syntax colors`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Minimal & Direct`; dashboard `N/A - Editor focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Complex shadows`; `3D effects`
- Key considerations: WYSIWYG or Markdown toggle. Folder/tag organization. Full-text search. Cloud sync. Typography-first. Distraction-free zen mode. Slash-command palette.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 638. Weather App
- Recommended pattern: `Hero-Centric Design`
- Style priority: `Glassmorphism` → `Aurora UI`; secondary `Motion-Driven`, `Minimalism & Swiss Style`
- Colour mood: `Atmospheric gradients (sky blue → sunset → storm grey) + temp scale`
- Typography mood: `Modern + Clear hierarchy`
- Key effects: `Backdrop blur (10-20px)`; `Translucent overlays`
- Landing & dashboard: landing `Hero-Centric Design`; dashboard `N/A - Utility focused`
- Decision rules: If low performance (brief mentions low performance, low-end, slow device) → lead with `Flat Design` style
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Location auto-detect. Hourly horizontal scroll + daily/weekly list. Animated weather icons. Air quality index. UV/wind/humidity chips. Radar map overlay. Widget-friendly layout.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 639. Timer & Pomodoro
- Recommended pattern: `Minimal & Direct`
- Style priority: `Minimalism & Swiss Style` → `Neumorphism`; secondary `Dark Mode (OLED)`, `Micro-interactions`
- Colour mood: `High-contrast on dark + focus red/amber + break green`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Dual shadows (light`; `dark)`; `Soft press 150ms`
- Landing & dashboard: landing `Minimal & Direct`; dashboard `N/A - Utility focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Large centered countdown digits. Circular progress ring. Session/break auto-switch. Session history log. Custom interval settings. Sound + haptic alerts. Focus stats chart.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 640. Scanner & Document Manager
- Recommended pattern: `Feature-Rich Showcase + Demo`
- Style priority: `Minimalism & Swiss Style` → `Flat Design`; secondary `Dark Mode (OLED)`, `Accessible & Ethical`
- Colour mood: `Clean white + camera viewfinder accent + file-type color coding`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase + Demo`; dashboard `N/A - Tool focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Complex shadows`; `3D effects`
- Key considerations: Camera capture with auto-edge detection. Crop/rotate/enhance. OCR text extraction overlay. PDF multi-page creation. Folder tree organization. Cloud sync. Share/export. Batch scan mode.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 641. Calendar & Scheduling App
- Recommended pattern: `Feature-Rich Showcase + Demo`
- Style priority: `Flat Design` → `Micro-interactions`; secondary `Minimalism & Swiss Style`, `Soft UI Evolution`
- Colour mood: `Clean blue + event category accent colors + success green`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase + Demo`; dashboard `N/A - Calendar focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`
- Key considerations: Event color coding. Week/month/day views. Recurring events. Conflict detection. Multi-calendar sync.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 642. Password Manager
- Recommended pattern: `Trust & Authority + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Accessible & Ethical`; secondary `Dark Mode (OLED)`, `Swiss Modernism 2.0`
- Colour mood: `Trust blue + security green + dark neutral`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle hover 200ms`; `Smooth transitions`; `Clean`
- Landing & dashboard: landing `Trust & Authority + Feature-Rich`; dashboard `N/A - Vault focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Color-only indicators`
- Key considerations: Security-first. Zero-knowledge architecture. Biometric unlock. Breach alert dashboard. Password generator.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 643. Voice Recorder & Memo
- Recommended pattern: `Interactive Product Demo + Minimal`
- Style priority: `Minimalism & Swiss Style` → `AI-Native UI`; secondary `Flat Design`, `Dark Mode (OLED)`
- Colour mood: `Clean white + recording red + waveform accent`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle hover 200ms`; `Smooth transitions`; `Clean`
- Landing & dashboard: landing `Interactive Product Demo + Minimal`; dashboard `N/A - Recording focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Waveform display. Background recording. Auto-transcription (AI). Tag/organize. Cloud sync.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 644. Translator App
- Recommended pattern: `Feature-Rich Showcase + Interactive Demo`
- Style priority: `Flat Design` → `AI-Native UI`; secondary `Minimalism & Swiss Style`, `Micro-interactions`
- Colour mood: `Global blue + neutral grey + language flag accent`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase + Interactive Demo`; dashboard `N/A - Utility focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`
- Key considerations: Real-time camera translation (OCR). Voice input and output. Offline mode. Conversation mode. Phrasebook.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 645. Calculator & Unit Converter
- Recommended pattern: `Minimal & Direct`
- Style priority: `Neumorphism` → `Minimalism & Swiss Style`; secondary `Flat Design`, `Dark Mode (OLED)`
- Colour mood: `Dark functional + orange operation keys + clear button hierarchy`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Dual shadows (light`; `dark)`; `Soft press 150ms`
- Landing & dashboard: landing `Minimal & Direct`; dashboard `N/A - Utility focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Scientific mode toggle. Live currency rates. Calculation history. Widget support. Gesture input.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 646. Alarm & World Clock
- Recommended pattern: `Minimal & Direct`
- Style priority: `Dark Mode (OLED)` → `Minimalism & Swiss Style`; secondary `Neumorphism`, `Flat Design`
- Colour mood: `Deep dark + ambient glow accent + timezone gradient`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Minimal & Direct`; dashboard `N/A - Utility focused`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Pure white backgrounds`
- Key considerations: Gentle wake (gradual volume). Timezone visualizer. Sleep tracking integration. Smart alarm skip. Bedtime mode.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 647. File Manager & Transfer
- Recommended pattern: `Feature-Rich Showcase + Demo`
- Style priority: `Flat Design` → `Minimalism & Swiss Style`; secondary `Accessible & Ethical`, `Dark Mode (OLED)`
- Colour mood: `Functional neutral + file type color coding (PDF orange, doc blue, image purple)`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase + Demo`; dashboard `N/A - File tree focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Complex shadows`; `3D effects`
- Key considerations: Folder tree navigation. File type preview. Wireless P2P transfer. Cloud integration. Compress and extract.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 648. Email Client
- Recommended pattern: `Feature-Rich Showcase + Demo`
- Style priority: `Flat Design` → `Minimalism & Swiss Style`; secondary `Micro-interactions`, `Soft UI Evolution`
- Colour mood: `Clean white + brand primary + priority red + snooze amber`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Feature-Rich Showcase + Demo`; dashboard `N/A - Inbox focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Complex shadows`; `3D effects`
- Key considerations: Unified inbox. Swipe actions (archive/delete/snooze). Priority sorting. Smart reply. Unsubscribe tool.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 649. VPN & Privacy Tool
- Recommended pattern: `Trust & Authority + Conversion-Optimized`
- Style priority: `Minimalism & Swiss Style` → `Dark Mode (OLED)`; secondary `Cyberpunk UI`, `Accessible & Ethical`
- Colour mood: `Dark shield blue + connected green + disconnected red + trust accent`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle glow`; `Neon accents`; `High contrast`
- Landing & dashboard: landing `Trust & Authority + Conversion-Optimized`; dashboard `N/A - Connection focused`
- Decision rules: If light mode needed (brief mentions light mode, light theme) → `provide theme toggle`; If conversion focused (brief mentions conversion, sales, signup, purchase) → `add urgency colors`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`; `Pure white backgrounds`
- Key considerations: One-tap connect. Server selection by country. No-log policy prominent. Speed indicator. Kill switch. Protocol choice.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 650. Emergency SOS & Safety
- Recommended pattern: `Trust & Authority + Social Proof`
- Style priority: `Accessible & Ethical` → `Flat Design`; secondary `Dark Mode (OLED)`, `Minimalism & Swiss Style`
- Colour mood: `Alert red + safety blue + location green + high contrast critical`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Trust & Authority + Social Proof`; dashboard `N/A - Safety focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`; `Color-only indicators`
- Key considerations: One-tap SOS. Emergency contacts auto-notify. Live location sharing. Fake call feature. Safe walk mode. Local emergency numbers.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

# Part 68 — Lifestyle, Family & Pets

## 651. Pet Tech App
- Recommended pattern: `Storytelling + Feature-Rich`
- Style priority: `Claymorphism` → `Vibrant & Block-based`; secondary `Micro-interactions`, `Flat Design`
- Colour mood: `Playful + Warm colors`
- Typography mood: `Friendly + Playful typography`
- Key effects: `Pet profile animations`; `Health tracking charts`
- Landing & dashboard: landing `Storytelling-Driven`; dashboard `User Behavior Analytics`
- Decision rules: Always → `pet profiles`; If health (brief mentions health, medical, patient) → `add vet integration`
- Anti-patterns (`MEDIUM`): avoid `Generic design`; `No personality`
- Key considerations: Pet profiles. Health tracking. Playful UI. Photo galleries. Vet integration.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 652. Childcare/Daycare
- Recommended pattern: `Social Proof-Focused + Trust`
- Style priority: `Claymorphism` → `Vibrant & Block-based`; secondary `Soft UI Evolution`, `Accessible & Ethical`
- Colour mood: `Playful pastels + Safe colors + Warm`; palette focus `Playful pastels + Safe colors + Warm accents`
- Typography mood: `Friendly + Playful typography`
- Key effects: `Parent portal animations`; `Activity gallery reveal`
- Landing & dashboard: landing `Social Proof-Focused + Trust`; dashboard `Parent Dashboard`
- Decision rules: Always → `parent communication`, `safety certifications`
- Anti-patterns (`HIGH`): avoid `Generic design`; `Hidden safety info`
- Key considerations: Programs. Staff profiles. Safety certifications. Parent portal. Activity updates. Cheerful imagery.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 653. Diary & Journal App
- Recommended pattern: `Storytelling-Driven`
- Style priority: `Soft UI Evolution` → `Minimalism & Swiss Style`; secondary `Neumorphism`, `Sketch Hand-Drawn (Mobile)`
- Colour mood: `Warm paper tones (cream/linen) + muted ink + mood-coded accents`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle hover 200ms`; `Smooth transitions`; `Clean`
- Landing & dashboard: landing `Storytelling-Driven`; dashboard `N/A - Personal focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Calendar month-view entry. Mood tag selector (emoji/color). Photo/voice attachment. Writing prompts. Privacy lock (FaceID/PIN). Search across entries. Export to PDF.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 654. Grocery & Shopping List
- Recommended pattern: `Minimal & Direct + Demo`
- Style priority: `Flat Design` → `Vibrant & Block-based`; secondary `Claymorphism`, `Micro-interactions`
- Colour mood: `Fresh green + food-category colors + checkmark accent`
- Typography mood: `Bold + Clean + Sans-serif`
- Key effects: `Color shift hover`; `Fast 150ms transitions`; `No shadows`
- Landing & dashboard: landing `Minimal & Direct + Demo`; dashboard `N/A - List focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`; `Muted colors`; `Low energy`
- Key considerations: Category-grouped list. Tap-to-check interaction (with strikethrough). Quantity stepper. Share list with family. Store aisle sorting. Barcode scan to add. Frequently bought suggestions.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 655. Parenting & Baby Tracker
- Recommended pattern: `Social Proof-Focused + Trust`
- Style priority: `Claymorphism` → `Soft UI Evolution`; secondary `Vibrant & Block-based`, `Accessible & Ethical`
- Colour mood: `Soft pastels (baby pink/sky blue/mint/peach) + warm accents`
- Typography mood: `Playful + Rounded + Friendly`
- Key effects: `Multi-layer shadows`; `Spring bounce`; `Soft press 200ms`
- Landing & dashboard: landing `Social Proof-Focused + Trust`; dashboard `User Behavior Analytics`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Feed/sleep/diaper quick-log buttons. Growth percentile chart. Milestone timeline with photos. Multiple child profiles. Partner invite + shared access. Pediatric reference. One-handed operation.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 656. Wardrobe & Outfit Planner
- Recommended pattern: `Storytelling-Driven + Feature-Rich`
- Style priority: `Minimalism & Swiss Style` → `Motion-Driven`; secondary `Aurora UI`, `Soft UI Evolution`
- Colour mood: `Clean fashion neutral + full clothes color palette + accent`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle hover 200ms`; `Smooth transitions`; `Clean`
- Landing & dashboard: landing `Storytelling-Driven + Feature-Rich`; dashboard `N/A - Wardrobe focused`
- Decision rules: If ux focused (brief mentions ux, usability, accessibility, accessible) → `prioritize clarity`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Photo catalog of clothes. AI outfit suggestions. Calendar integration. Capsule wardrobe. Season filtering.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 657. Plant Care Tracker
- Recommended pattern: `Storytelling-Driven + Social Proof`
- Style priority: `Organic Biophilic` → `Soft UI Evolution`; secondary `Claymorphism`, `Flat Design`
- Colour mood: `Nature greens + earth brown + sunny yellow reminder + water blue`
- Typography mood: `Warm + Humanist + Natural`
- Key effects: `Rounded 16-24px`; `Natural shadows`; `Flowing SVG`
- Landing & dashboard: landing `Storytelling-Driven + Social Proof`; dashboard `N/A - Plant collection focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Inconsistent styling`; `Poor contrast ratios`
- Key considerations: Plant database with care guides. Watering reminders. Growth photo timeline. AI health diagnosis. Collection sharing.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 658. Book & Reading Tracker
- Recommended pattern: `Social Proof-Focused + Feature-Rich`
- Style priority: `Swiss Modernism 2.0` → `Minimalism & Swiss Style`; secondary `E-Ink / Paper`, `Soft UI Evolution`
- Colour mood: `Warm paper white + ink brown + reading progress green + book cover colors`
- Typography mood: `Professional + Clean hierarchy`
- Key effects: `Subtle hover 200ms`; `Smooth transitions`; `Clean`
- Landing & dashboard: landing `Social Proof-Focused + Feature-Rich`; dashboard `N/A - Library focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Excessive decoration`
- Key considerations: Barcode scan to add. Progress percentage. Annual reading goal. Notes and quotes. Friends activity. Genre stats.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 659. Family Calendar & Chores
- Recommended pattern: `Feature-Rich Showcase + Social Proof`
- Style priority: `Flat Design` → `Claymorphism`; secondary `Accessible & Ethical`, `Vibrant & Block-based`
- Colour mood: `Warm playful + member color coding + chore completion green`
- Typography mood: `Playful + Rounded + Friendly`
- Key effects: `Multi-layer shadows`; `Spring bounce`; `Soft press 200ms`
- Landing & dashboard: landing `Feature-Rich Showcase + Social Proof`; dashboard `N/A - Family hub focused`
- Decision rules: If trust needed (brief mentions trust, secure, verified, authority) → `add testimonials`
- Anti-patterns (`HIGH`): avoid `Complex shadows`; `3D effects`
- Key considerations: Member color coding. Chore assignment rotation. Recurring events. Shared shopping list. Allowance tracking.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

# Part 69 — Emerging & Frontier Tech

## 660. Agriculture/Farm Tech
- Recommended pattern: `Feature-Rich Showcase`
- Style priority: `Organic Biophilic` → `Flat Design`; secondary `Minimalism & Swiss Style`, `Accessible & Ethical`
- Colour mood: `Earth Green (#4A7C23) + Brown + Sky Blue`
- Typography mood: `Clear + Informative typography`
- Key effects: `Data visualization`; `Weather animations`
- Landing & dashboard: landing `Feature-Rich Showcase + Trust`; dashboard `IoT Sensor Dashboard`
- Decision rules: Always → `sensor dashboard`; If crop focused (brief mentions crop, farm, agriculture) → `add health indicators`
- Anti-patterns (`MEDIUM`): avoid `Generic design`; `Ignored accessibility`; `AI purple/pink gradients`
- Key considerations: Crop monitoring. Weather data. IoT sensors. Yield tracking. Market prices. Sustainable imagery.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 661. Space Tech / Aerospace
- Recommended pattern: `Immersive + Feature-Rich`
- Style priority: `HUD / Sci-Fi FUI` → `Dark Mode (OLED)`; secondary `Glassmorphism`, `3D & Hyperrealism`
- Colour mood: `Deep Space Black + Star White + Metallic`
- Typography mood: `Futuristic + Precise typography`
- Key effects: `Telemetry animations`; `3D renders`
- Landing & dashboard: landing `Immersive Experience + Hero`; dashboard `Real-Time Monitoring + 3D`
- Decision rules: Always → `high tech feel`, `precision data`
- Anti-patterns (`HIGH`): avoid `Generic design`; `No immersion`
- Key considerations: High-tech feel. Precision. Telemetry data.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 662. Quantum Computing Interface
- Recommended pattern: `Immersive + Interactive`
- Style priority: `HUD / Sci-Fi FUI` → `Dark Mode (OLED)`; secondary `Glassmorphism`, `Spatial UI (VisionOS)`
- Colour mood: `Quantum Blue (#00FFFF) + Deep Black`; palette focus `Quantum Blue #00FFFF + Deep Black + Interference patterns`
- Typography mood: `Futuristic + Scientific typography`
- Key effects: `Probability visualizations`; `Qubit state animations`
- Landing & dashboard: landing `Immersive/Interactive Experience`; dashboard `3D Spatial Data + Real-Time Monitor`
- Decision rules: Always → `complexity visualization`, `scientific credibility`
- Anti-patterns (`HIGH`): avoid `Generic tech design`; `No viz`
- Key considerations: Visualize complexity. Qubit states. Probability clouds. High-tech trust.
- RTL: `caveats` — layout encodes reading direction; flag this before recommending and offer a mirrorable alternative for strict RTL builds

## 663. Spatial Computing OS / App
- Recommended pattern: `Immersive + Interactive`
- Style priority: `Spatial UI (VisionOS)` → `Glassmorphism`; primary recommendation `Spatial UI (VisionOS)`; secondary `Glassmorphism`, `3D & Hyperrealism`
- Colour mood: `Frosted Glass + System Colors + Depth`
- Typography mood: `Spatial + Readable typography`
- Key effects: `Depth hierarchy`; `Gaze interactions`
- Landing & dashboard: landing `Immersive/Interactive Experience`; dashboard `Spatial Dashboard`
- Decision rules: Always → `depth hierarchy`, `environment awareness`
- Anti-patterns (`HIGH`): avoid `2D design`; `No spatial depth`
- Key considerations: Gaze/Pinch interaction. Depth hierarchy. Environment awareness.
- RTL: `full` — mirrors cleanly; no directional rework needed

## 664. Sustainable Energy / Climate Tech
- Recommended pattern: `Data + Trust`
- Style priority: `Organic Biophilic` → `E-Ink / Paper`; secondary `Data-Dense Dashboard`, `Swiss Modernism 2.0`
- Colour mood: `Earth Green + Sky Blue + Solar Yellow`
- Typography mood: `Clear + Informative typography`
- Key effects: `Impact viz`; `Progress animations`
- Landing & dashboard: landing `Interactive Demo + Data`; dashboard `Energy/Utilities Dashboard`
- Decision rules: Always → `data transparency`, `impact visualization`
- Anti-patterns (`HIGH`): avoid `Greenwashing`; `No real data`
- Key considerations: Data transparency. Impact visualization. Low-carbon web design.
- RTL: `partial` — mirrors, but check icons, carousels, motion paths and charts per component

## 665. Digital Signage / Kiosk
- Recommended pattern: `Immersive/Interactive Experience`
- Style priority: `Flat Design` → `Dark Mode (OLED)`; primary recommendation `Minimalism & Swiss Style` + `Dark Mode (OLED)`; secondary `Flat Design`, `Motion-Driven`
- Colour mood: `High contrast + brand accent + touch target emphasis`; palette focus `High contrast + brand accent + touch target emphasis (56px min)`
- Typography mood: `Large + Immediate typography`
- Key effects: `Auto-rotate transitions`; `large touch feedback`
- Landing & dashboard: landing `Full-Screen Immersive`; dashboard `N/A - Display focused`
- Decision rules: Always → `single purpose layout`, `touch targets`, `auto rotate content`, `offline fallback`, `brightness aware palette`; If mobile (brief mentions mobile, phone, tablet, ios, android) → `optimize touch targets`; If low performance (brief mentions low performance, low-end, slow device) → `reduce motion`
- Anti-patterns (`MEDIUM`): avoid `Tiny tap targets`; `scroll-heavy layout`; `flashy motion`
- Key considerations: Full-screen single-purpose layout. Touch targets ≥56px. Auto-rotate content. Offline fallback. Brightness-aware color palette. No scroll.
- Rationale: kiosk UI must survive bad lighting, low attention, and partial offline operation (confidence `0.88`)
- RTL: `full` — mirrors cleanly; no directional rework needed

# Part 70 — Semantic Colour Token Structure

## 666. Token roles

- Every palette defines the same role set: `primary`, `on-primary`, `secondary`, `on-secondary`, `accent`, `on-accent`, `background`, `foreground`, `card`, `card-foreground`, `muted`, `muted-foreground`, `border`, `destructive`, `on-destructive`, `ring`.
- `primary` carries the brand and the main interactive surfaces; `secondary` is a lighter or adjacent tint of the same hue family for supporting controls.
- `accent` is the call-to-action or highlight colour and is usually a contrasting hue to primary (e.g. trust blue + orange CTA, indigo + emerald CTA).
- `background`/`foreground` define the page; `card`/`card-foreground` define raised surfaces; `muted`/`muted-foreground` define subdued fills and secondary text; `border` separates surfaces.
- `destructive` is reserved for delete/error actions and is never reused as a brand accent.

## 667. On-colour pairing

- Every fill colour has a paired `on-` colour for text and icons placed on it; pick the pair by luminance, not by brand preference.
- Use white `#FFFFFF` on dark or saturated fills (most blues, navies, violets, reds) and black `#000000` or near-black `#0F172A` on bright or mid-tone fills (cyan, emerald, amber, orange, pink, light tints).
- Every on-colour pair meets at least `4.5:1` contrast (WCAG AA for normal text); in practice the lowest pair sits around `4.6:1`.
- When a brand accent fails contrast, darken it rather than abandoning the hue (e.g. orange `#F97316` becomes `#EA580C`, emerald `#10B981` becomes `#059669`, gold `#CA8A04` is darkened) and keep the original for decorative use only.
- `card-foreground` always equals `foreground`, so text styles do not change between page and card.

## 668. Neutral and state tokens

- Light themes use a white card `#FFFFFF` on a lightly tinted background (e.g. `#F8FAFC`, `#F0F9FF`, `#FDF2F8`) so cards lift without shadows.
- Dark themes use a slightly lifted navy/charcoal card (e.g. `#192134`, `#0E1223`, `#1B1B30`) on a near-black background (`#020617`, `#0F0F23`, `#0F172A`, `#000000`).
- `muted-foreground` is slate `#475569` on light themes and lighter slate `#94A3B8` on dark themes; it still clears `4.5:1` against its muted fill.
- `destructive` defaults to red `#DC2626` with white text on light themes; dark themes often use brighter `#EF4444` with black text so the red stays legible on black.
- Background-to-foreground contrast is high in every palette (minimum around `5.9:1`, usually far above).

## 669. Focus ring

- `ring` normally equals `primary` so focus states feel on-brand.
- When primary is too dark to see on a dark background (navy or charcoal primary on near-black), set the ring to white `#FFFFFF`.
- When primary is a bright mid-tone on a light background (orange, amber, sky blue, pink), set the ring to black `#000000` for a visible focus outline.
- Never let the focus ring disappear into the background; it must contrast with both the page and the focused control.

# Part 71 — SaaS, Productivity & Business Software Palettes

## 670. SaaS (General) palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#EA580C` / on `#000000`
- Background `#F8FAFC` / fg `#1E293B`; Card `#FFFFFF` / fg `#1E293B`; Muted `#E9EFF8` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Trust blue + orange CTA contrast. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 671. Micro SaaS palette

- Primary `#6366F1` / on `#000000`; Secondary `#818CF8` / on `#0F172A`; Accent `#059669` / on `#000000`
- Background `#F5F3FF` / fg `#1E1B4B`; Card `#FFFFFF` / fg `#1E1B4B`; Muted `#EBEFF9` / fg `#475569`; Border `#E0E7FF`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#6366F1`
- Character: Indigo primary + emerald CTA. Accent darkened from `#10B981` to meet contrast; keep the original hue for decoration only.

## 672. B2B Service palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#0369A1` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#020617`; Card `#FFFFFF` / fg `#020617`; Muted `#E8ECF1` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0F172A`
- Character: Professional navy + blue CTA.

## 673. Analytics Dashboard palette

- Primary `#1E40AF` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#F8FAFC` / fg `#1E3A8A`; Card `#FFFFFF` / fg `#1E3A8A`; Muted `#E9EEF6` / fg `#475569`; Border `#DBEAFE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E40AF`
- Character: Blue data + amber highlights. Accent darkened from `#F59E0B` to meet contrast; keep the original hue for decoration only.

## 674. Productivity Tool palette

- Primary `#0D9488` / on `#000000`; Secondary `#14B8A6` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#F0FDFA` / fg `#134E4A`; Card `#FFFFFF` / fg `#134E4A`; Muted `#E8F1F4` / fg `#475569`; Border `#99F6E4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0D9488`
- Character: Teal focus + action orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 675. Design System/Component Library palette

- Primary `#4F46E5` / on `#FFFFFF`; Secondary `#6366F1` / on `#000000`; Accent `#EA580C` / on `#000000`
- Background `#EEF2FF` / fg `#312E81`; Card `#FFFFFF` / fg `#312E81`; Muted `#EBEEF8` / fg `#475569`; Border `#C7D2FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#4F46E5`
- Character: Indigo brand + doc hierarchy. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 676. Remote Work/Collaboration Tool palette

- Primary `#6366F1` / on `#000000`; Secondary `#818CF8` / on `#0F172A`; Accent `#059669` / on `#000000`
- Background `#F5F3FF` / fg `#312E81`; Card `#FFFFFF` / fg `#312E81`; Muted `#EBEFF9` / fg `#475569`; Border `#E0E7FF`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#6366F1`
- Character: Calm indigo + success green. Accent darkened from `#10B981` to meet contrast; keep the original hue for decoration only.

## 677. Knowledge Base/Documentation palette

- Primary `#475569` / on `#FFFFFF`; Secondary `#64748B` / on `#FFFFFF`; Accent `#2563EB` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#1E293B`; Card `#FFFFFF` / fg `#1E293B`; Muted `#EAEFF3` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#475569`
- Character: Neutral grey + link blue.

## 678. CRM & Client Management palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Professional blue + deal green.

## 679. Inventory & Stock Management palette

- Primary `#334155` / on `#FFFFFF`; Secondary `#475569` / on `#FFFFFF`; Accent `#059669` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F2F3F4` / fg `#475569`; Border `#E6E8EA`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#334155`
- Character: Industrial slate + stock green.

## 680. Booking & Appointment App palette

- Primary `#0284C7` / on `#000000`; Secondary `#0EA5E9` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#F0F9FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#EFF7FB` / fg `#475569`; Border `#E0F0F8`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0284C7`
- Character: Calendar blue + available green.

## 681. Invoice & Billing Tool palette

- Primary `#1E3A5F` / on `#FFFFFF`; Secondary `#2563EB` / on `#FFFFFF`; Accent `#059669` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F3F5` / fg `#475569`; Border `#E4E7EB`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A5F`
- Character: Navy professional + paid green.

## 682. Scanner & Document Manager palette

- Primary `#1E293B` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#2563EB` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F2F3` / fg `#475569`; Border `#E4E5E7`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E293B`
- Character: Document grey + scan blue.

## 683. Calendar & Scheduling App palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Calendar blue + event green.

## 684. File Manager & Transfer palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Folder blue + file amber.

## 685. Email Client palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#DC2626` / on `#FFFFFF`
- Background `#FFFFFF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Inbox blue + priority red.

## 686. Family Calendar & Chores palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#059669` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Family blue + chore green.

## 687. Study Together / Virtual Coworking palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Focus blue + session green.

## 688. Status Page / Incident Management palette

- Primary `#16A34A` / on `#000000`; Secondary `#22C55E` / on `#0F172A`; Accent `#DC2626` / on `#FFFFFF`
- Background `#F0FDF4` / fg `#14532D`; Card `#FFFFFF` / fg `#14532D`; Muted `#E8F0F1` / fg `#475569`; Border `#BBF7D0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#16A34A`
- Character: Operational green + incident red + maintenance amber.

## 689. Changelog / Release Notes palette

- Primary `#475569` / on `#FFFFFF`; Secondary `#64748B` / on `#FFFFFF`; Accent `#059669` / on `#000000`
- Background `#F8FAFC` / fg `#1E293B`; Card `#FFFFFF` / fg `#1E293B`; Muted `#EAEFF3` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#475569`
- Character: Feature green + fix blue + breaking red badges.

## 690. Digital Signage / Kiosk palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E293B` / on `#FFFFFF`; Accent `#EF4444` / on `#000000`
- Background `#020617` / fg `#F8FAFC`; Card `#0E1223` / fg `#F8FAFC`; Muted `#1A1E2F` / fg `#94A3B8`; Border `#334155`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: High contrast dark + brand accent + large touch targets.

## 691. E-signature / Document Workflow palette

- Primary `#1E3A5F` / on `#FFFFFF`; Secondary `#2563EB` / on `#FFFFFF`; Accent `#16A34A` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#E9EEF5` / fg `#475569`; Border `#CBD5E1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A5F`
- Character: Trust navy + signature green + audit trail.

## 692. Feature Flag / Config Management palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E293B` / on `#FFFFFF`; Accent `#16A34A` / on `#0F172A`
- Background `#020617` / fg `#F8FAFC`; Card `#0E1223` / fg `#F8FAFC`; Muted `#1A1E2F` / fg `#94A3B8`; Border `#334155`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Enabled green + disabled grey + experimental amber.

## 693. No-code / Low-code Builder palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#A78BFA` / on `#0F172A`; Accent `#EC4899` / on `#000000`
- Background `#FAF5FF` / fg `#4C1D95`; Card `#FFFFFF` / fg `#4C1D95`; Muted `#ECEEF9` / fg `#475569`; Border `#DDD6FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Builder purple + component pink + canvas neutral.

## 694. Resume / CV Builder palette

- Primary `#1E3A5F` / on `#FFFFFF`; Secondary `#2563EB` / on `#FFFFFF`; Accent `#16A34A` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#E9EEF5` / fg `#475569`; Border `#CBD5E1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A5F`
- Character: Professional navy + section accent + success green.

## 695. RPA / Automation Dashboard palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E293B` / on `#FFFFFF`; Accent `#16A34A` / on `#0F172A`
- Background `#020617` / fg `#F8FAFC`; Card `#0E1223` / fg `#F8FAFC`; Muted `#1A1E2F` / fg `#94A3B8`; Border `#334155`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Dark terminal + running green + failed red + queued amber.

## 696. Survey / Form Builder palette

- Primary `#0D9488` / on `#000000`; Secondary `#2DD4BF` / on `#0F172A`; Accent `#D97706` / on `#000000`
- Background `#F0FDFA` / fg `#134E4A`; Card `#FFFFFF` / fg `#134E4A`; Muted `#E8F1F4` / fg `#475569`; Border `#5EEAD4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0D9488`
- Character: Question teal + progress green + submit blue.

# Part 72 — Developer, Security & Deep-Tech Palettes

## 697. AI/Chatbot Platform palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#A78BFA` / on `#0F172A`; Accent `#0891B2` / on `#000000`
- Background `#FAF5FF` / fg `#1E1B4B`; Card `#FFFFFF` / fg `#1E1B4B`; Muted `#ECEEF9` / fg `#475569`; Border `#DDD6FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: AI purple + cyan interactions. Accent darkened from `#06B6D4` to meet contrast; keep the original hue for decoration only.

## 698. Smart Home/IoT Dashboard palette

- Primary `#1E293B` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#22C55E` / on `#0F172A`
- Background `#0F172A` / fg `#F8FAFC`; Card `#1B2336` / fg `#F8FAFC`; Muted `#272F42` / fg `#94A3B8`; Border `#475569`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Dark tech + status green.

## 699. Coding Bootcamp palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E293B` / on `#FFFFFF`; Accent `#22C55E` / on `#0F172A`
- Background `#020617` / fg `#F8FAFC`; Card `#0E1223` / fg `#F8FAFC`; Muted `#1A1E2F` / fg `#94A3B8`; Border `#334155`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Terminal dark + success green.

## 700. Cybersecurity Platform palette

- Primary `#00FF41` / on `#0F172A`; Secondary `#0D0D0D` / on `#FFFFFF`; Accent `#FF3333` / on `#000000`
- Background `#000000` / fg `#E0E0E0`; Card `#0C130E` / fg `#E0E0E0`; Muted `#181818` / fg `#94A3B8`; Border `#1F1F1F`; Destructive `#EF4444` / on `#000000`; Ring `#00FF41`
- Character: Matrix green + alert red.

## 701. Developer Tool / IDE palette

- Primary `#1E293B` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#22C55E` / on `#0F172A`
- Background `#0F172A` / fg `#F8FAFC`; Card `#1B2336` / fg `#F8FAFC`; Muted `#272F42` / fg `#94A3B8`; Border `#475569`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Code dark + run green.

## 702. Space Tech / Aerospace palette

- Primary `#F8FAFC` / on `#0F172A`; Secondary `#94A3B8` / on `#0F172A`; Accent `#3B82F6` / on `#000000`
- Background `#0B0B10` / fg `#F8FAFC`; Card `#1E1E23` / fg `#F8FAFC`; Muted `#232328` / fg `#94A3B8`; Border `#1E293B`; Destructive `#EF4444` / on `#000000`; Ring `#F8FAFC`
- Character: Star white + launch blue.

## 703. Quantum Computing Interface palette

- Primary `#00FFFF` / on `#0F172A`; Secondary `#7B61FF` / on `#000000`; Accent `#FF00FF` / on `#000000`
- Background `#050510` / fg `#E0E0FF`; Card `#101823` / fg `#E0E0FF`; Muted `#1D1D28` / fg `#94A3B8`; Border `#333344`; Destructive `#EF4444` / on `#000000`; Ring `#00FFFF`
- Character: Quantum cyan + interference purple.

## 704. Autonomous Drone Fleet Manager palette

- Primary `#00FF41` / on `#0F172A`; Secondary `#008F11` / on `#000000`; Accent `#FF3333` / on `#000000`
- Background `#0D1117` / fg `#E6EDF3`; Card `#182424` / fg `#E6EDF3`; Muted `#25292F` / fg `#94A3B8`; Border `#30363D`; Destructive `#EF4444` / on `#000000`; Ring `#00FF41`
- Character: Terminal green + alert red.

## 705. Spatial Computing OS / App palette

- Primary `#FFFFFF` / on `#0F172A`; Secondary `#E5E5E5` / on `#0F172A`; Accent `#FFFFFF` / on `#0F172A`
- Background `#888888` / fg `#000000`; Card `#999999` / fg `#000000`; Muted `#E5E7EB` / fg `#5F6673`; Border `#CCCCCC`; Destructive `#FF3B30` / on `#000000`; Ring `#000000`
- Character: Glass white + system blue. Accent darkened from `#007AFF` to meet contrast; keep the original hue for decoration only.

## 706. Password Manager palette

- Primary `#1E3A5F` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#059669` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#10192E` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Vault dark blue + secure green.

## 707. Coding Challenge & Practice palette

- Primary `#22C55E` / on `#0F172A`; Secondary `#059669` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#10242E` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#22C55E`
- Character: Code green + difficulty amber on dark.

## 708. VPN & Privacy Tool palette

- Primary `#1E3A5F` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#22C55E` / on `#0F172A`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#10192E` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Shield dark + connected green.

## 709. API Developer Portal palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E293B` / on `#FFFFFF`; Accent `#22C55E` / on `#0F172A`
- Background `#020617` / fg `#F8FAFC`; Card `#0E1223` / fg `#F8FAFC`; Muted `#1A1E2F` / fg `#94A3B8`; Border `#334155`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Code dark + endpoint green + syntax colors.

## 710. Open Source Project Landing palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E293B` / on `#FFFFFF`; Accent `#A16207` / on `#FFFFFF`
- Background `#020617` / fg `#F8FAFC`; Card `#0E1223` / fg `#F8FAFC`; Muted `#1A1E2F` / fg `#94A3B8`; Border `#334155`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Dark code + star gold + fork silver + sponsor purple.

# Part 73 — Finance, Commerce & Marketplace Palettes

## 711. E-commerce palette

- Primary `#059669` / on `#000000`; Secondary `#10B981` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#ECFDF5` / fg `#064E3B`; Card `#FFFFFF` / fg `#064E3B`; Muted `#E8F1F3` / fg `#475569`; Border `#A7F3D0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#059669`
- Character: Success green + urgency orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 712. E-commerce Luxury palette

- Primary `#1C1917` / on `#FFFFFF`; Secondary `#44403C` / on `#FFFFFF`; Accent `#A16207` / on `#FFFFFF`
- Background `#FAFAF9` / fg `#0C0A09`; Card `#FFFFFF` / fg `#0C0A09`; Muted `#E8ECF0` / fg `#475569`; Border `#D6D3D1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1C1917`
- Character: Premium dark + gold accent. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 713. Financial Dashboard palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E293B` / on `#FFFFFF`; Accent `#22C55E` / on `#0F172A`
- Background `#020617` / fg `#F8FAFC`; Card `#0E1223` / fg `#F8FAFC`; Muted `#1A1E2F` / fg `#94A3B8`; Border `#334155`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Dark bg + green positive indicators.

## 714. Fintech/Crypto palette

- Primary `#F59E0B` / on `#0F172A`; Secondary `#FBBF24` / on `#0F172A`; Accent `#8B5CF6` / on `#000000`
- Background `#0F172A` / fg `#F8FAFC`; Card `#222735` / fg `#F8FAFC`; Muted `#272F42` / fg `#94A3B8`; Border `#334155`; Destructive `#EF4444` / on `#000000`; Ring `#F59E0B`
- Character: Gold trust + purple tech.

## 715. NFT/Web3 Platform palette

- Primary `#8B5CF6` / on `#000000`; Secondary `#A78BFA` / on `#0F172A`; Accent `#FBBF24` / on `#0F172A`
- Background `#0F0F23` / fg `#F8FAFC`; Card `#1E1D35` / fg `#F8FAFC`; Muted `#27273B` / fg `#94A3B8`; Border `#4C1D95`; Destructive `#EF4444` / on `#000000`; Ring `#8B5CF6`
- Character: Purple tech + gold value.

## 716. Subscription Box Service palette

- Primary `#D946EF` / on `#000000`; Secondary `#E879F9` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#FDF4FF` / fg `#86198F`; Card `#FFFFFF` / fg `#86198F`; Muted `#F0EEF9` / fg `#475569`; Border `#F5D0FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#D946EF`
- Character: Excitement purple + urgency orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 717. Luxury/Premium Brand palette

- Primary `#1C1917` / on `#FFFFFF`; Secondary `#44403C` / on `#FFFFFF`; Accent `#A16207` / on `#FFFFFF`
- Background `#FAFAF9` / fg `#0C0A09`; Card `#FFFFFF` / fg `#0C0A09`; Muted `#E8ECF0` / fg `#475569`; Border `#D6D3D1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1C1917`
- Character: Premium black + gold accent. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 718. Insurance Platform palette

- Primary `#0369A1` / on `#FFFFFF`; Secondary `#0EA5E9` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#F0F9FF` / fg `#0C4A6E`; Card `#FFFFFF` / fg `#0C4A6E`; Muted `#E7EFF5` / fg `#475569`; Border `#BAE6FD`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0369A1`
- Character: Security blue + protected green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 719. Banking/Traditional Finance palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E3A8A` / on `#FFFFFF`; Accent `#A16207` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#020617`; Card `#FFFFFF` / fg `#020617`; Muted `#E8ECF1` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0F172A`
- Character: Trust navy + premium gold. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 720. Job Board/Recruitment palette

- Primary `#0369A1` / on `#FFFFFF`; Secondary `#0EA5E9` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#F0F9FF` / fg `#0C4A6E`; Card `#FFFFFF` / fg `#0C4A6E`; Muted `#E7EFF5` / fg `#475569`; Border `#BAE6FD`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0369A1`
- Character: Professional blue + success green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 721. Marketplace (P2P) palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#A78BFA` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#FAF5FF` / fg `#4C1D95`; Card `#FFFFFF` / fg `#4C1D95`; Muted `#ECEEF9` / fg `#475569`; Border `#DDD6FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Trust purple + transaction green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 722. Digital Products/Downloads palette

- Primary `#6366F1` / on `#000000`; Secondary `#818CF8` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#EEF2FF` / fg `#312E81`; Card `#FFFFFF` / fg `#312E81`; Muted `#EBEFF9` / fg `#475569`; Border `#C7D2FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#6366F1`
- Character: Digital indigo + buy green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 723. Personal Finance Tracker palette

- Primary `#1E40AF` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#101A34` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Trust blue + profit green on dark.

## 724. Expense Splitter / Bill Split palette

- Primary `#059669` / on `#000000`; Secondary `#10B981` / on `#000000`; Accent `#DC2626` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F0F8F6` / fg `#475569`; Border `#E1F2ED`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#059669`
- Character: Balance green + owe red.

## 725. Auction Platform palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E293B` / on `#FFFFFF`; Accent `#16A34A` / on `#0F172A`
- Background `#020617` / fg `#F8FAFC`; Card `#0E1223` / fg `#F8FAFC`; Muted `#1A1E2F` / fg `#94A3B8`; Border `#334155`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Dark luxury + bid green + outbid red + urgency.

## 726. Classifieds / Buy-Sell palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#16A34A` / on `#000000`
- Background `#EFF6FF` / fg `#1E40AF`; Card `#FFFFFF` / fg `#1E40AF`; Muted `#E9EFF8` / fg `#475569`; Border `#BFDBFE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Listing blue + price green + seller badge.

## 727. Crowdfunding Platform palette

- Primary `#D97706` / on `#000000`; Secondary `#F59E0B` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FCF6F0` / fg `#475569`; Border `#FAEEE1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#D97706`
- Character: Funding progress amber + goal green + urgency.

## 728. Review Platform palette

- Primary `#F59E0B` / on `#0F172A`; Secondary `#FBBF24` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FCF6F0` / fg `#475569`; Border `#FAEEE1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#000000`
- Character: Star gold + positive green + negative red.

## 729. Testimonial & Social Proof Widget palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#A78BFA` / on `#0F172A`; Accent `#F59E0B` / on `#0F172A`
- Background `#FAF5FF` / fg `#4C1D95`; Card `#FFFFFF` / fg `#4C1D95`; Muted `#ECEEF9` / fg `#475569`; Border `#DDD6FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Trust purple + quote gold + verified blue.

# Part 74 — Health, Wellness & Care Palettes

## 730. Healthcare App palette

- Primary `#0891B2` / on `#000000`; Secondary `#22D3EE` / on `#0F172A`; Accent `#059669` / on `#000000`
- Background `#ECFEFF` / fg `#164E63`; Card `#FFFFFF` / fg `#164E63`; Muted `#E8F1F6` / fg `#475569`; Border `#A5F3FC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0891B2`
- Character: Calm cyan + health green.

## 731. Mental Health App palette

- Primary `#8B5CF6` / on `#000000`; Secondary `#C4B5FD` / on `#0F172A`; Accent `#059669` / on `#000000`
- Background `#FAF5FF` / fg `#4C1D95`; Card `#FFFFFF` / fg `#4C1D95`; Muted `#EDEFF9` / fg `#475569`; Border `#EDE9FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#8B5CF6`
- Character: Calming lavender + wellness green. Accent darkened from `#10B981` to meet contrast; keep the original hue for decoration only.

## 732. Beauty/Spa/Wellness Service palette

- Primary `#EC4899` / on `#000000`; Secondary `#F9A8D4` / on `#0F172A`; Accent `#8B5CF6` / on `#000000`
- Background `#FDF2F8` / fg `#831843`; Card `#FFFFFF` / fg `#831843`; Muted `#F1EEF5` / fg `#475569`; Border `#FBCFE8`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EC4899`
- Character: Soft pink + lavender luxury.

## 733. Fitness/Gym App palette

- Primary `#F97316` / on `#0F172A`; Secondary `#FB923C` / on `#0F172A`; Accent `#22C55E` / on `#0F172A`
- Background `#1F2937` / fg `#F8FAFC`; Card `#313742` / fg `#F8FAFC`; Muted `#37414F` / fg `#CBD5E1`; Border `#374151`; Destructive `#EF4444` / on `#000000`; Ring `#F97316`
- Character: Energy orange + success green.

## 734. Childcare/Daycare palette

- Primary `#F472B6` / on `#0F172A`; Secondary `#FBCFE8` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#FDF2F8` / fg `#9D174D`; Card `#FFFFFF` / fg `#9D174D`; Muted `#F1F0F6` / fg `#475569`; Border `#FCE7F3`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#000000`
- Character: Soft pink + safe green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 735. Senior Care/Elderly palette

- Primary `#0369A1` / on `#FFFFFF`; Secondary `#38BDF8` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#F0F9FF` / fg `#0C4A6E`; Card `#FFFFFF` / fg `#0C4A6E`; Muted `#E7EFF5` / fg `#475569`; Border `#E0F2FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0369A1`
- Character: Calm blue + reassuring green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 736. Medical Clinic palette

- Primary `#0891B2` / on `#000000`; Secondary `#22D3EE` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#F0FDFA` / fg `#134E4A`; Card `#FFFFFF` / fg `#134E4A`; Muted `#E8F1F6` / fg `#475569`; Border `#CCFBF1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0891B2`
- Character: Medical teal + health green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 737. Pharmacy/Drug Store palette

- Primary `#15803D` / on `#FFFFFF`; Secondary `#22C55E` / on `#0F172A`; Accent `#0369A1` / on `#FFFFFF`
- Background `#F0FDF4` / fg `#14532D`; Card `#FFFFFF` / fg `#14532D`; Muted `#E8F0F1` / fg `#475569`; Border `#BBF7D0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#15803D`
- Character: Pharmacy green + trust blue.

## 738. Dental Practice palette

- Primary `#0EA5E9` / on `#0F172A`; Secondary `#38BDF8` / on `#0F172A`; Accent `#0EA5E9` / on `#0F172A`
- Background `#F0F9FF` / fg `#0C4A6E`; Card `#FFFFFF` / fg `#0C4A6E`; Muted `#E8F2F8` / fg `#475569`; Border `#BAE6FD`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#000000`
- Character: Fresh blue + smile yellow. Accent darkened from `#FBBF24` to meet contrast; keep the original hue for decoration only.

## 739. Veterinary Clinic palette

- Primary `#0D9488` / on `#000000`; Secondary `#14B8A6` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#F0FDFA` / fg `#134E4A`; Card `#FFFFFF` / fg `#134E4A`; Muted `#E8F1F4` / fg `#475569`; Border `#99F6E4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0D9488`
- Character: Caring teal + warm orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 740. Biotech / Life Sciences palette

- Primary `#0EA5E9` / on `#0F172A`; Secondary `#0284C7` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#F0F9FF` / fg `#0C4A6E`; Card `#FFFFFF` / fg `#0C4A6E`; Muted `#E8F2F8` / fg `#475569`; Border `#BAE6FD`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#000000`
- Character: DNA blue + life green. Accent darkened from `#10B981` to meet contrast; keep the original hue for decoration only.

## 741. Biohacking / Longevity App palette

- Primary `#FF4D4D` / on `#000000`; Secondary `#4D94FF` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#F5F5F7` / fg `#1C1C1E`; Card `#FFFFFF` / fg `#1C1C1E`; Muted `#F2EEF2` / fg `#475569`; Border `#E5E5EA`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FF4D4D`
- Character: Bio red/blue + vitality green. Accent darkened from `#00E676` to meet contrast; keep the original hue for decoration only.

## 742. Habit Tracker palette

- Primary `#D97706` / on `#000000`; Secondary `#F59E0B` / on `#0F172A`; Accent `#059669` / on `#000000`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FCF6F0` / fg `#475569`; Border `#FAEEE1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#D97706`
- Character: Streak amber + habit green.

## 743. Meditation & Mindfulness palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#8B5CF6` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#FAF5FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F7F3FD` / fg `#475569`; Border `#EFE7FC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Calm lavender + mindful green.

## 744. Mood Tracker palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#6366F1` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#FAF5FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F7F3FD` / fg `#475569`; Border `#EFE7FC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Mood purple + insight amber.

## 745. Running & Cycling GPS palette

- Primary `#EA580C` / on `#000000`; Secondary `#F97316` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#201C27` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EA580C`
- Character: Energetic orange + pace green on dark.

## 746. Yoga & Stretching Guide palette

- Primary `#6B7280` / on `#FFFFFF`; Secondary `#78716C` / on `#FFFFFF`; Accent `#0891B2` / on `#000000`
- Background `#F5F5F0` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F6F6F7` / fg `#475569`; Border `#EDEEEF`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#6B7280`
- Character: Sage neutral + calm teal.

## 747. Sleep Tracker palette

- Primary `#4338CA` / on `#FFFFFF`; Secondary `#6366F1` / on `#000000`; Accent `#7C3AED` / on `#FFFFFF`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#131936` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Night indigo + dream violet on dark.

## 748. Calorie & Nutrition Counter palette

- Primary `#059669` / on `#000000`; Secondary `#10B981` / on `#000000`; Accent `#EA580C` / on `#000000`
- Background `#ECFDF5` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F0F8F6` / fg `#475569`; Border `#E1F2ED`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#059669`
- Character: Healthy green + macro orange.

## 749. Period & Cycle Tracker palette

- Primary `#BE185D` / on `#FFFFFF`; Secondary `#EC4899` / on `#000000`; Accent `#7C3AED` / on `#FFFFFF`
- Background `#FDF2F8` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FBF1F5` / fg `#475569`; Border `#F7E3EB`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#BE185D`
- Character: Blush rose + fertility lavender.

## 750. Medication & Pill Reminder palette

- Primary `#0284C7` / on `#000000`; Secondary `#0891B2` / on `#000000`; Accent `#DC2626` / on `#FFFFFF`
- Background `#F0F9FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#EFF7FB` / fg `#475569`; Border `#E0F0F8`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0284C7`
- Character: Medical blue + alert red.

## 751. Water & Hydration Reminder palette

- Primary `#0284C7` / on `#000000`; Secondary `#06B6D4` / on `#000000`; Accent `#0891B2` / on `#000000`
- Background `#F0F9FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#EFF7FB` / fg `#475569`; Border `#E0F0F8`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0284C7`
- Character: Refreshing blue + water cyan.

## 752. Fasting & Intermittent Timer palette

- Primary `#6366F1` / on `#000000`; Secondary `#4338CA` / on `#FFFFFF`; Accent `#059669` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#151D39` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#6366F1`
- Character: Fasting indigo on dark + eating green.

## 753. Patient Portal / Health Records palette

- Primary `#0284C7` / on `#000000`; Secondary `#0891B2` / on `#000000`; Accent `#16A34A` / on `#000000`
- Background `#F0F9FF` / fg `#0C4A6E`; Card `#FFFFFF` / fg `#0C4A6E`; Muted `#E8F2F8` / fg `#475569`; Border `#BAE6FD`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0284C7`
- Character: Clinical blue + health green + alert red.

## 754. Telemedicine Platform palette

- Primary `#0891B2` / on `#000000`; Secondary `#22D3EE` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#F0FDFA` / fg `#134E4A`; Card `#FFFFFF` / fg `#134E4A`; Muted `#E8F1F6` / fg `#475569`; Border `#CCFBF1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0891B2`
- Character: Medical teal + video green + waiting amber.

# Part 75 — Education, Knowledge & Research Palettes

## 755. Educational App palette

- Primary `#4F46E5` / on `#FFFFFF`; Secondary `#818CF8` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#EEF2FF` / fg `#1E1B4B`; Card `#FFFFFF` / fg `#1E1B4B`; Muted `#EBEEF8` / fg `#475569`; Border `#C7D2FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#4F46E5`
- Character: Playful indigo + energetic orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 756. Micro-Credentials/Badges Platform palette

- Primary `#0369A1` / on `#FFFFFF`; Secondary `#0EA5E9` / on `#0F172A`; Accent `#A16207` / on `#FFFFFF`
- Background `#F0F9FF` / fg `#0C4A6E`; Card `#FFFFFF` / fg `#0C4A6E`; Muted `#E7EFF5` / fg `#475569`; Border `#BAE6FD`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0369A1`
- Character: Trust blue + achievement gold. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 757. Online Course/E-learning palette

- Primary `#0D9488` / on `#000000`; Secondary `#2DD4BF` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#F0FDFA` / fg `#134E4A`; Card `#FFFFFF` / fg `#134E4A`; Muted `#E8F1F4` / fg `#475569`; Border `#5EEAD4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0D9488`
- Character: Progress teal + achievement orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 758. Language Learning App palette

- Primary `#4F46E5` / on `#FFFFFF`; Secondary `#818CF8` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#EEF2FF` / fg `#312E81`; Card `#FFFFFF` / fg `#312E81`; Muted `#EBEEF8` / fg `#475569`; Border `#C7D2FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#4F46E5`
- Character: Learning indigo + progress green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 759. Flashcard & Study Tool palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#8B5CF6` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#FAF5FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F7F3FD` / fg `#475569`; Border `#EFE7FC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Study purple + correct green.

## 760. Kids Learning (ABC & Math) palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#F59E0B` / on `#0F172A`; Accent `#EC4899` / on `#000000`
- Background `#EFF6FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Learning blue + play yellow + fun pink.

## 761. Music Instrument Learning palette

- Primary `#DC2626` / on `#FFFFFF`; Secondary `#9A3412` / on `#FFFFFF`; Accent `#D97706` / on `#000000`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FCF1F1` / fg `#475569`; Border `#FAE4E4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DC2626`
- Character: Musical red + warm amber.

## 762. Academic Journal / Scholarly Publishing palette

- Primary `#1E3A5F` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#B45309` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#E9EEF5` / fg `#475569`; Border `#CBD5E1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A5F`
- Character: Scholarly navy + citation gold + serif accent.

## 763. Forum / Discussion Board palette

- Primary `#475569` / on `#FFFFFF`; Secondary `#64748B` / on `#FFFFFF`; Accent `#2563EB` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#1E293B`; Card `#FFFFFF` / fg `#1E293B`; Muted `#EAEFF3` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#475569`
- Character: Neutral grey + topic accent + unread indicator.

## 764. Wiki / Encyclopedia palette

- Primary `#1E3A8A` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#7C3AED` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#1E40AF`; Card `#FFFFFF` / fg `#1E40AF`; Muted `#E9EEF5` / fg `#475569`; Border `#BFDBFE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A8A`
- Character: Knowledge blue + link purple + clean white.

## 765. Citizen Science Platform palette

- Primary `#15803D` / on `#FFFFFF`; Secondary `#22C55E` / on `#0F172A`; Accent `#D97706` / on `#000000`
- Background `#F0FDF4` / fg `#14532D`; Card `#FFFFFF` / fg `#14532D`; Muted `#E8F0F1` / fg `#475569`; Border `#BBF7D0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#15803D`
- Character: Discovery green + volunteer badge + data neutral.

## 766. Conference / Symposium Landing Page palette

- Primary `#1E3A5F` / on `#FFFFFF`; Secondary `#2563EB` / on `#FFFFFF`; Accent `#A16207` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#E9EEF5` / fg `#475569`; Border `#CBD5E1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A5F`
- Character: Academic navy + gold keynote + track chips.

## 767. Grant / Funding Portal palette

- Primary `#1E3A5F` / on `#FFFFFF`; Secondary `#2563EB` / on `#FFFFFF`; Accent `#16A34A` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#E9EEF5` / fg `#475569`; Border `#CBD5E1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A5F`
- Character: Institution navy + funding green + deadline urgency.

## 768. LMS (Learning Management System) palette

- Primary `#0D9488` / on `#000000`; Secondary `#2DD4BF` / on `#0F172A`; Accent `#D97706` / on `#000000`
- Background `#F0FDFA` / fg `#134E4A`; Card `#FFFFFF` / fg `#134E4A`; Muted `#E8F1F4` / fg `#475569`; Border `#5EEAD4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0D9488`
- Character: Education teal + course amber + grade green.

## 769. Patent / IP Database palette

- Primary `#475569` / on `#FFFFFF`; Secondary `#64748B` / on `#FFFFFF`; Accent `#A16207` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#1E293B`; Card `#FFFFFF` / fg `#1E293B`; Muted `#EAEFF3` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#475569`
- Character: Formal neutral + patent type chips + status badges.

## 770. Q&A Community Platform palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#0891B2` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Knowledge blue + accepted green + reputation gold.

## 771. Research Lab / University Department palette

- Primary `#1E3A5F` / on `#FFFFFF`; Secondary `#2563EB` / on `#FFFFFF`; Accent `#A16207` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#E9EEF5` / fg `#475569`; Border `#CBD5E1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A5F`
- Character: Institutional navy + research accent + serif headings.

# Part 76 — Media, Entertainment & Gaming Palettes

## 772. Gaming palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#A78BFA` / on `#0F172A`; Accent `#F43F5E` / on `#000000`
- Background `#0F0F23` / fg `#E2E8F0`; Card `#1E1C35` / fg `#E2E8F0`; Muted `#27273B` / fg `#94A3B8`; Border `#4C1D95`; Destructive `#EF4444` / on `#000000`; Ring `#7C3AED`
- Character: Neon purple + rose action.

## 773. Podcast Platform palette

- Primary `#1E1B4B` / on `#FFFFFF`; Secondary `#312E81` / on `#FFFFFF`; Accent `#F97316` / on `#0F172A`
- Background `#0F0F23` / fg `#F8FAFC`; Card `#1B1B30` / fg `#F8FAFC`; Muted `#27273B` / fg `#94A3B8`; Border `#4338CA`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Dark audio + warm accent.

## 774. Music Streaming palette

- Primary `#1E1B4B` / on `#FFFFFF`; Secondary `#4338CA` / on `#FFFFFF`; Accent `#22C55E` / on `#0F172A`
- Background `#0F0F23` / fg `#F8FAFC`; Card `#1B1B30` / fg `#F8FAFC`; Muted `#27273B` / fg `#94A3B8`; Border `#312E81`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Dark audio + play green.

## 775. Video Streaming/OTT palette

- Primary `#0F0F23` / on `#FFFFFF`; Secondary `#1E1B4B` / on `#FFFFFF`; Accent `#E11D48` / on `#FFFFFF`
- Background `#000000` / fg `#F8FAFC`; Card `#0C0C0D` / fg `#F8FAFC`; Muted `#181818` / fg `#94A3B8`; Border `#312E81`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Cinema dark + play red.

## 776. News/Media Platform palette

- Primary `#DC2626` / on `#FFFFFF`; Secondary `#EF4444` / on `#000000`; Accent `#1E40AF` / on `#FFFFFF`
- Background `#FEF2F2` / fg `#450A0A`; Card `#FFFFFF` / fg `#450A0A`; Muted `#F0EDF1` / fg `#475569`; Border `#FECACA`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DC2626`
- Character: Breaking red + link blue.

## 777. Magazine/Blog palette

- Primary `#18181B` / on `#FFFFFF`; Secondary `#3F3F46` / on `#FFFFFF`; Accent `#EC4899` / on `#000000`
- Background `#FAFAFA` / fg `#09090B`; Card `#FFFFFF` / fg `#09090B`; Muted `#E8ECF0` / fg `#475569`; Border `#E4E4E7`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#18181B`
- Character: Editorial black + accent pink.

## 778. Theater/Cinema palette

- Primary `#1E1B4B` / on `#FFFFFF`; Secondary `#312E81` / on `#FFFFFF`; Accent `#CA8A04` / on `#0F172A`
- Background `#0F0F23` / fg `#F8FAFC`; Card `#1B1B30` / fg `#F8FAFC`; Muted `#27273B` / fg `#94A3B8`; Border `#4338CA`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Dramatic dark + spotlight gold.

## 779. Voice Recorder & Memo palette

- Primary `#DC2626` / on `#FFFFFF`; Secondary `#EF4444` / on `#000000`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FFFFFF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FCF1F1` / fg `#475569`; Border `#FAE4E4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DC2626`
- Character: Recording red + waveform blue.

## 780. Casual Puzzle Game palette

- Primary `#EC4899` / on `#000000`; Secondary `#8B5CF6` / on `#000000`; Accent `#F59E0B` / on `#0F172A`
- Background `#FDF2F8` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FDF4F8` / fg `#475569`; Border `#FCE9F2`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EC4899`
- Character: Cheerful pink + reward gold.

## 781. Trivia & Quiz Game palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#7C3AED` / on `#FFFFFF`; Accent `#F59E0B` / on `#0F172A`
- Background `#EFF6FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Quiz blue + gold leaderboard.

## 782. Card & Board Game palette

- Primary `#15803D` / on `#FFFFFF`; Secondary `#166534` / on `#FFFFFF`; Accent `#D97706` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#0F1F2B` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#15803D`
- Character: Felt green + gold on dark.

## 783. Idle & Clicker Game palette

- Primary `#D97706` / on `#000000`; Secondary `#F59E0B` / on `#0F172A`; Accent `#7C3AED` / on `#FFFFFF`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FCF6F0` / fg `#475569`; Border `#FAEEE1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#D97706`
- Character: Coin gold + prestige purple.

## 784. Word & Crossword Game palette

- Primary `#15803D` / on `#FFFFFF`; Secondary `#059669` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#FFFFFF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F0F7F3` / fg `#475569`; Border `#E2EFE7`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#15803D`
- Character: Word green + letter amber.

## 785. Arcade & Retro Game palette

- Primary `#DC2626` / on `#FFFFFF`; Secondary `#2563EB` / on `#FFFFFF`; Accent `#22C55E` / on `#0F172A`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#1F1829` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DC2626`
- Character: Neon red+blue on dark + score green.

## 786. White Noise & Ambient Sound palette

- Primary `#475569` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#4338CA` / on `#FFFFFF`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#131B2F` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Ambient grey + deep indigo on dark.

# Part 77 — Creative, Social & Lifestyle Palettes

## 787. Creative Agency palette

- Primary `#EC4899` / on `#000000`; Secondary `#F472B6` / on `#0F172A`; Accent `#0891B2` / on `#000000`
- Background `#FDF2F8` / fg `#831843`; Card `#FFFFFF` / fg `#831843`; Muted `#F1EEF5` / fg `#475569`; Border `#FBCFE8`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EC4899`
- Character: Bold pink + cyan accent. Accent darkened from `#06B6D4` to meet contrast; keep the original hue for decoration only.

## 788. Portfolio/Personal palette

- Primary `#18181B` / on `#FFFFFF`; Secondary `#3F3F46` / on `#FFFFFF`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FAFAFA` / fg `#09090B`; Card `#FFFFFF` / fg `#09090B`; Muted `#E8ECF0` / fg `#475569`; Border `#E4E4E7`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#18181B`
- Character: Monochrome + blue accent.

## 789. Social Media App palette

- Primary `#E11D48` / on `#FFFFFF`; Secondary `#FB7185` / on `#0F172A`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FFF1F2` / fg `#881337`; Card `#FFFFFF` / fg `#881337`; Muted `#F0ECF2` / fg `#475569`; Border `#FECDD3`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#E11D48`
- Character: Vibrant rose + engagement blue.

## 790. Creator Economy Platform palette

- Primary `#EC4899` / on `#000000`; Secondary `#F472B6` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#FDF2F8` / fg `#831843`; Card `#FFFFFF` / fg `#831843`; Muted `#F1EEF5` / fg `#475569`; Border `#FBCFE8`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EC4899`
- Character: Creator pink + engagement orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 791. Dating App palette

- Primary `#E11D48` / on `#FFFFFF`; Secondary `#FB7185` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#FFF1F2` / fg `#881337`; Card `#FFFFFF` / fg `#881337`; Muted `#F0ECF2` / fg `#475569`; Border `#FECDD3`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#E11D48`
- Character: Romantic rose + warm orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 792. Photography Studio palette

- Primary `#18181B` / on `#FFFFFF`; Secondary `#27272A` / on `#FFFFFF`; Accent `#F8FAFC` / on `#0F172A`
- Background `#000000` / fg `#FAFAFA`; Card `#0C0C0C` / fg `#FAFAFA`; Muted `#181818` / fg `#94A3B8`; Border `#3F3F46`; Destructive `#EF4444` / on `#000000`; Ring `#FFFFFF`
- Character: Pure black + white contrast.

## 793. Freelancer Platform palette

- Primary `#6366F1` / on `#000000`; Secondary `#818CF8` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#EEF2FF` / fg `#312E81`; Card `#FFFFFF` / fg `#312E81`; Muted `#EBEFF9` / fg `#475569`; Border `#C7D2FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#6366F1`
- Character: Creative indigo + hire green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 794. Marketing Agency palette

- Primary `#EC4899` / on `#000000`; Secondary `#F472B6` / on `#0F172A`; Accent `#0891B2` / on `#000000`
- Background `#FDF2F8` / fg `#831843`; Card `#FFFFFF` / fg `#831843`; Muted `#F1EEF5` / fg `#475569`; Border `#FBCFE8`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EC4899`
- Character: Bold pink + creative cyan. Accent darkened from `#06B6D4` to meet contrast; keep the original hue for decoration only.

## 795. Generative Art Platform palette

- Primary `#18181B` / on `#FFFFFF`; Secondary `#3F3F46` / on `#FFFFFF`; Accent `#EC4899` / on `#000000`
- Background `#FAFAFA` / fg `#09090B`; Card `#FFFFFF` / fg `#09090B`; Muted `#E8ECF0` / fg `#475569`; Border `#E4E4E7`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#18181B`
- Character: Canvas neutral + creative pink.

## 796. Photo Editor & Filters palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#6366F1` / on `#000000`; Accent `#0891B2` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#171939` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Editor violet + filter cyan on dark.

## 797. Short Video Editor palette

- Primary `#EC4899` / on `#000000`; Secondary `#DB2777` / on `#FFFFFF`; Accent `#2563EB` / on `#FFFFFF`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#201A32` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EC4899`
- Character: Video pink on dark + timeline blue.

## 798. Drawing & Sketching Canvas palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#8B5CF6` / on `#000000`; Accent `#0891B2` / on `#000000`
- Background `#1C1917` / fg `#FFFFFF`; Card `#262321` / fg `#FFFFFF`; Muted `#231B28` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Canvas purple + tool teal on dark.

## 799. Music Creation & Beat Maker palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#6366F1` / on `#000000`; Accent `#22C55E` / on `#0F172A`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#171939` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Studio purple + waveform green on dark.

## 800. Meme & Sticker Maker palette

- Primary `#EC4899` / on `#000000`; Secondary `#F59E0B` / on `#0F172A`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FFFFFF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FDF4F8` / fg `#475569`; Border `#FCE9F2`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EC4899`
- Character: Viral pink + comedy yellow + share blue.

## 801. AI Photo & Avatar Generator palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#6366F1` / on `#000000`; Accent `#EC4899` / on `#000000`
- Background `#FAF5FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F7F3FD` / fg `#475569`; Border `#EFE7FC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: AI purple + generation pink.

## 802. Link-in-Bio Page Builder palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#7C3AED` / on `#FFFFFF`; Accent `#EC4899` / on `#000000`
- Background `#FFFFFF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Brand blue + creator purple.

## 803. Wardrobe & Outfit Planner palette

- Primary `#BE185D` / on `#FFFFFF`; Secondary `#EC4899` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#FDF2F8` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FBF1F5` / fg `#475569`; Border `#F7E3EB`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#BE185D`
- Character: Fashion rose + gold accent.

## 804. Couple & Relationship App palette

- Primary `#BE185D` / on `#FFFFFF`; Secondary `#EC4899` / on `#000000`; Accent `#DC2626` / on `#FFFFFF`
- Background `#FDF2F8` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FBF1F5` / fg `#475569`; Border `#F7E3EB`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#BE185D`
- Character: Romance rose + love red.

## 805. Anonymous Community / Confession palette

- Primary `#475569` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#0891B2` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#131B2F` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Protective grey + subtle teal on dark.

## 806. Wallpaper & Theme App palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#EC4899` / on `#000000`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FAF5FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F7F3FD` / fg `#475569`; Border `#EFE7FC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Aesthetic purple + trending pink.

# Part 78 — Hospitality, Food, Travel & Events Palettes

## 807. Restaurant/Food Service palette

- Primary `#DC2626` / on `#FFFFFF`; Secondary `#F87171` / on `#0F172A`; Accent `#A16207` / on `#FFFFFF`
- Background `#FEF2F2` / fg `#450A0A`; Card `#FFFFFF` / fg `#450A0A`; Muted `#F0EDF1` / fg `#475569`; Border `#FECACA`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DC2626`
- Character: Appetizing red + warm gold. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 808. Travel/Tourism Agency palette

- Primary `#0EA5E9` / on `#0F172A`; Secondary `#38BDF8` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#F0F9FF` / fg `#0C4A6E`; Card `#FFFFFF` / fg `#0C4A6E`; Muted `#E8F2F8` / fg `#475569`; Border `#BAE6FD`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#000000`
- Character: Sky blue + adventure orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 809. Hotel/Hospitality palette

- Primary `#1E3A8A` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#A16207` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#1E40AF`; Card `#FFFFFF` / fg `#1E40AF`; Muted `#E9EEF5` / fg `#475569`; Border `#BFDBFE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A8A`
- Character: Luxury navy + gold service. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 810. Wedding/Event Planning palette

- Primary `#DB2777` / on `#FFFFFF`; Secondary `#F472B6` / on `#0F172A`; Accent `#A16207` / on `#FFFFFF`
- Background `#FDF2F8` / fg `#831843`; Card `#FFFFFF` / fg `#831843`; Muted `#F0EDF4` / fg `#475569`; Border `#FBCFE8`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DB2777`
- Character: Romantic pink + elegant gold. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 811. Bakery/Cafe palette

- Primary `#92400E` / on `#FFFFFF`; Secondary `#B45309` / on `#FFFFFF`; Accent `#92400E` / on `#FFFFFF`
- Background `#FEF3C7` / fg `#78350F`; Card `#FFFFFF` / fg `#78350F`; Muted `#EDEEF0` / fg `#475569`; Border `#FDE68A`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#92400E`
- Character: Warm brown + cream white. Accent darkened from `#F8FAFC` to meet contrast; keep the original hue for decoration only.

## 812. Brewery/Winery palette

- Primary `#7C2D12` / on `#FFFFFF`; Secondary `#B91C1C` / on `#FFFFFF`; Accent `#A16207` / on `#FFFFFF`
- Background `#FEF2F2` / fg `#450A0A`; Card `#FFFFFF` / fg `#450A0A`; Muted `#ECEDF0` / fg `#475569`; Border `#FECACA`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C2D12`
- Character: Deep burgundy + craft gold. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 813. Airline palette

- Primary `#1E3A8A` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#EA580C` / on `#000000`
- Background `#EFF6FF` / fg `#1E40AF`; Card `#FFFFFF` / fg `#1E40AF`; Muted `#E9EEF5` / fg `#475569`; Border `#BFDBFE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A8A`
- Character: Sky blue + booking orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 814. Event Management palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#A78BFA` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#FAF5FF` / fg `#4C1D95`; Card `#FFFFFF` / fg `#4C1D95`; Muted `#ECEEF9` / fg `#475569`; Border `#DDD6FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Excitement purple + action orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 815. Food Delivery / On-Demand palette

- Primary `#EA580C` / on `#000000`; Secondary `#F97316` / on `#000000`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FFF7ED` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FDF4F0` / fg `#475569`; Border `#FCEAE1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EA580C`
- Character: Appetizing orange + trust blue.

## 816. Recipe & Cooking App palette

- Primary `#9A3412` / on `#FFFFFF`; Secondary `#C2410C` / on `#FFFFFF`; Accent `#059669` / on `#000000`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F8F2F0` / fg `#475569`; Border `#F2E6E2`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#9A3412`
- Character: Warm terracotta + fresh green.

## 817. Grocery & Shopping List palette

- Primary `#059669` / on `#000000`; Secondary `#10B981` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#ECFDF5` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F0F8F6` / fg `#475569`; Border `#E1F2ED`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#059669`
- Character: Fresh green + food amber.

## 818. Local Events & Discovery palette

- Primary `#EA580C` / on `#000000`; Secondary `#F97316` / on `#000000`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FFF7ED` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FDF4F0` / fg `#475569`; Border `#FCEAE1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EA580C`
- Character: Event orange + map blue.

## 819. Road Trip Planner palette

- Primary `#EA580C` / on `#000000`; Secondary `#0891B2` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#FFF7ED` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FDF4F0` / fg `#475569`; Border `#FCEAE1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EA580C`
- Character: Adventure orange + map teal.

## 820. Ticketing / Box Office palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#1E293B` / on `#FFFFFF`; Accent `#16A34A` / on `#0F172A`
- Background `#020617` / fg `#F8FAFC`; Card `#0E1223` / fg `#F8FAFC`; Muted `#1A1E2F` / fg `#94A3B8`; Border `#334155`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Event theme colors + available green + sold-out red.

# Part 79 — Local Services, Property, Mobility & Industry Palettes

## 821. Pet Tech App palette

- Primary `#F97316` / on `#0F172A`; Secondary `#FB923C` / on `#0F172A`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FFF7ED` / fg `#9A3412`; Card `#FFFFFF` / fg `#9A3412`; Muted `#F1F0F0` / fg `#475569`; Border `#FED7AA`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#000000`
- Character: Playful orange + trust blue.

## 822. EV/Charging Ecosystem palette

- Primary `#0891B2` / on `#000000`; Secondary `#22D3EE` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#ECFEFF` / fg `#164E63`; Card `#FFFFFF` / fg `#164E63`; Muted `#E8F1F6` / fg `#475569`; Border `#A5F3FC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0891B2`
- Character: Electric cyan + eco green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 823. Hyperlocal Services palette

- Primary `#059669` / on `#000000`; Secondary `#10B981` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#ECFDF5` / fg `#064E3B`; Card `#FFFFFF` / fg `#064E3B`; Muted `#E8F1F3` / fg `#475569`; Border `#A7F3D0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#059669`
- Character: Location green + action orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 824. Real Estate/Property palette

- Primary `#0F766E` / on `#FFFFFF`; Secondary `#14B8A6` / on `#0F172A`; Accent `#0369A1` / on `#FFFFFF`
- Background `#F0FDFA` / fg `#134E4A`; Card `#FFFFFF` / fg `#134E4A`; Muted `#E8F0F3` / fg `#475569`; Border `#99F6E4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0F766E`
- Character: Trust teal + professional blue.

## 825. Logistics/Delivery palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#EA580C` / on `#000000`
- Background `#EFF6FF` / fg `#1E40AF`; Card `#FFFFFF` / fg `#1E40AF`; Muted `#E9EFF8` / fg `#475569`; Border `#BFDBFE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Tracking blue + delivery orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 826. Agriculture/Farm Tech palette

- Primary `#15803D` / on `#FFFFFF`; Secondary `#22C55E` / on `#0F172A`; Accent `#A16207` / on `#FFFFFF`
- Background `#F0FDF4` / fg `#14532D`; Card `#FFFFFF` / fg `#14532D`; Muted `#E8F0F1` / fg `#475569`; Border `#BBF7D0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#15803D`
- Character: Earth green + harvest gold. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 827. Construction/Architecture palette

- Primary `#64748B` / on `#FFFFFF`; Secondary `#94A3B8` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#F8FAFC` / fg `#334155`; Card `#FFFFFF` / fg `#334155`; Muted `#EBF0F5` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#64748B`
- Character: Industrial grey + safety orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 828. Automotive/Car Dealership palette

- Primary `#1E293B` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#DC2626` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#E9EDF1` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E293B`
- Character: Premium dark + action red.

## 829. Coworking Space palette

- Primary `#F59E0B` / on `#0F172A`; Secondary `#FBBF24` / on `#0F172A`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FFFBEB` / fg `#78350F`; Card `#FFFFFF` / fg `#78350F`; Muted `#F1F2EF` / fg `#475569`; Border `#FDE68A`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#000000`
- Character: Energetic amber + booking blue.

## 830. Home Services (Plumber/Electrician) palette

- Primary `#1E40AF` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#EA580C` / on `#000000`
- Background `#EFF6FF` / fg `#1E3A8A`; Card `#FFFFFF` / fg `#1E3A8A`; Muted `#E9EEF6` / fg `#475569`; Border `#BFDBFE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E40AF`
- Character: Professional blue + urgent orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 831. Florist/Plant Shop palette

- Primary `#15803D` / on `#FFFFFF`; Secondary `#22C55E` / on `#0F172A`; Accent `#EC4899` / on `#000000`
- Background `#F0FDF4` / fg `#14532D`; Card `#FFFFFF` / fg `#14532D`; Muted `#E8F0F1` / fg `#475569`; Border `#BBF7D0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#15803D`
- Character: Natural green + floral pink.

## 832. Architecture / Interior palette

- Primary `#171717` / on `#FFFFFF`; Secondary `#404040` / on `#FFFFFF`; Accent `#A16207` / on `#FFFFFF`
- Background `#FFFFFF` / fg `#171717`; Card `#FFFFFF` / fg `#171717`; Muted `#E8ECF0` / fg `#475569`; Border `#E5E5E5`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#171717`
- Character: Minimal black + accent gold. Accent darkened from `#D4AF37` to meet contrast; keep the original hue for decoration only.

## 833. Sustainable Energy / Climate Tech palette

- Primary `#059669` / on `#000000`; Secondary `#10B981` / on `#0F172A`; Accent `#059669` / on `#000000`
- Background `#ECFDF5` / fg `#064E3B`; Card `#FFFFFF` / fg `#064E3B`; Muted `#E8F1F3` / fg `#475569`; Border `#A7F3D0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#059669`
- Character: Nature green + solar gold. Accent darkened from `#FBBF24` to meet contrast; keep the original hue for decoration only.

## 834. Ride Hailing / Transportation palette

- Primary `#1E293B` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#2563EB` / on `#FFFFFF`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#10182B` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#FFFFFF`
- Character: Map dark + route blue.

## 835. Parking Finder palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#059669` / on `#000000`; Accent `#DC2626` / on `#FFFFFF`
- Background `#F0F9FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Available blue/green + occupied red.

## 836. Public Transit Guide palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#0891B2` / on `#000000`; Accent `#EA580C` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Transit blue + line colors.

## 837. Home Decoration & Interior Design palette

- Primary `#78716C` / on `#FFFFFF`; Secondary `#A8A29E` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#FAF5F2` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F6F6F6` / fg `#475569`; Border `#EEEDED`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#78716C`
- Character: Interior warm grey + gold accent.

## 838. Directory / Listing Site palette

- Primary `#059669` / on `#000000`; Secondary `#10B981` / on `#0F172A`; Accent `#D97706` / on `#000000`
- Background `#ECFDF5` / fg `#064E3B`; Card `#FFFFFF` / fg `#064E3B`; Muted `#E8F1F3` / fg `#475569`; Border `#A7F3D0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#059669`
- Character: Category green + verified badge + map accent.

# Part 80 — Public Sector, Legal & Community Palettes

## 839. Government/Public Service palette

- Primary `#0F172A` / on `#FFFFFF`; Secondary `#334155` / on `#FFFFFF`; Accent `#0369A1` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#020617`; Card `#FFFFFF` / fg `#020617`; Muted `#E8ECF1` / fg `#475569`; Border `#E2E8F0`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0F172A`
- Character: High contrast navy + blue.

## 840. Legal Services palette

- Primary `#1E3A8A` / on `#FFFFFF`; Secondary `#1E40AF` / on `#FFFFFF`; Accent `#B45309` / on `#FFFFFF`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#E9EEF5` / fg `#475569`; Border `#CBD5E1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E3A8A`
- Character: Authority navy + trust gold.

## 841. Non-profit/Charity palette

- Primary `#0891B2` / on `#000000`; Secondary `#22D3EE` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#ECFEFF` / fg `#164E63`; Card `#FFFFFF` / fg `#164E63`; Muted `#E8F1F6` / fg `#475569`; Border `#A5F3FC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0891B2`
- Character: Compassion blue + action orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 842. Membership/Community palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#A78BFA` / on `#0F172A`; Accent `#16A34A` / on `#000000`
- Background `#FAF5FF` / fg `#4C1D95`; Card `#FFFFFF` / fg `#4C1D95`; Muted `#ECEEF9` / fg `#475569`; Border `#DDD6FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Community purple + join green. Accent darkened from `#22C55E` to meet contrast; keep the original hue for decoration only.

## 843. Newsletter Platform palette

- Primary `#0369A1` / on `#FFFFFF`; Secondary `#0EA5E9` / on `#0F172A`; Accent `#EA580C` / on `#000000`
- Background `#F0F9FF` / fg `#0C4A6E`; Card `#FFFFFF` / fg `#0C4A6E`; Muted `#E7EFF5` / fg `#475569`; Border `#BAE6FD`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0369A1`
- Character: Trust blue + subscribe orange. Accent darkened from `#F97316` to meet contrast; keep the original hue for decoration only.

## 844. Church/Religious Organization palette

- Primary `#7C3AED` / on `#FFFFFF`; Secondary `#A78BFA` / on `#0F172A`; Accent `#A16207` / on `#FFFFFF`
- Background `#FAF5FF` / fg `#4C1D95`; Card `#FFFFFF` / fg `#4C1D95`; Muted `#ECEEF9` / fg `#475569`; Border `#DDD6FE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#7C3AED`
- Character: Spiritual purple + warm gold. Accent darkened from `#CA8A04` to meet contrast; keep the original hue for decoration only.

## 845. Sports Team/Club palette

- Primary `#DC2626` / on `#FFFFFF`; Secondary `#EF4444` / on `#000000`; Accent `#DC2626` / on `#FFFFFF`
- Background `#FEF2F2` / fg `#7F1D1D`; Card `#FFFFFF` / fg `#7F1D1D`; Muted `#F0EDF1` / fg `#475569`; Border `#FECACA`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DC2626`
- Character: Team red + championship gold. Accent darkened from `#FBBF24` to meet contrast; keep the original hue for decoration only.

## 846. Museum/Gallery palette

- Primary `#18181B` / on `#FFFFFF`; Secondary `#27272A` / on `#FFFFFF`; Accent `#18181B` / on `#FFFFFF`
- Background `#FAFAFA` / fg `#09090B`; Card `#FFFFFF` / fg `#09090B`; Muted `#E8ECF0` / fg `#475569`; Border `#E4E4E7`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#18181B`
- Character: Gallery black + white space. Accent darkened from `#F8FAFC` to meet contrast; keep the original hue for decoration only.

## 847. Emergency SOS & Safety palette

- Primary `#DC2626` / on `#FFFFFF`; Secondary `#EF4444` / on `#000000`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FFF1F2` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FCF1F1` / fg `#475569`; Border `#FAE4E4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DC2626`
- Character: Alert red + safety blue.

## 848. Government Portal / Civic Services palette

- Primary `#1E40AF` / on `#FFFFFF`; Secondary `#3B82F6` / on `#000000`; Accent `#16A34A` / on `#000000`
- Background `#EFF6FF` / fg `#1E3A8A`; Card `#FFFFFF` / fg `#1E3A8A`; Muted `#E9EFF5` / fg `#475569`; Border `#BFDBFE`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#1E40AF`
- Character: Professional blue + service green + accessibility.

# Part 81 — Personal Utilities & Trackers Palettes

## 849. Chat & Messaging App palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#6366F1` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#FFFFFF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Messenger blue + online green.

## 850. Notes & Writing App palette

- Primary `#78716C` / on `#FFFFFF`; Secondary `#A8A29E` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F6F6F6` / fg `#475569`; Border `#EEEDED`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#78716C`
- Character: Warm ink + amber accent on cream.

## 851. Weather App palette

- Primary `#0284C7` / on `#000000`; Secondary `#0EA5E9` / on `#000000`; Accent `#F59E0B` / on `#0F172A`
- Background `#F0F9FF` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#EFF7FB` / fg `#475569`; Border `#E0F0F8`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#0284C7`
- Character: Sky blue + sun amber.

## 852. Diary & Journal App palette

- Primary `#92400E` / on `#FFFFFF`; Secondary `#A16207` / on `#FFFFFF`; Accent `#6366F1` / on `#000000`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F8F3F0` / fg `#475569`; Border `#F1E8E2`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#92400E`
- Character: Warm journal brown + ink violet.

## 853. Timer & Pomodoro palette

- Primary `#DC2626` / on `#FFFFFF`; Secondary `#EF4444` / on `#000000`; Accent `#059669` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#1F1829` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DC2626`
- Character: Focus red on dark + break green.

## 854. Parenting & Baby Tracker palette

- Primary `#EC4899` / on `#000000`; Secondary `#F472B6` / on `#000000`; Accent `#0284C7` / on `#000000`
- Background `#FDF2F8` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FDF4F8` / fg `#475569`; Border `#FCE9F2`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EC4899`
- Character: Soft pink + trust blue.

## 855. Bookmark & Read-Later palette

- Primary `#D97706` / on `#000000`; Secondary `#F59E0B` / on `#0F172A`; Accent `#2563EB` / on `#FFFFFF`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FCF6F0` / fg `#475569`; Border `#FAEEE1`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#D97706`
- Character: Warm amber + link blue.

## 856. Translator App palette

- Primary `#2563EB` / on `#FFFFFF`; Secondary `#0891B2` / on `#000000`; Accent `#EA580C` / on `#000000`
- Background `#F8FAFC` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F1F5FD` / fg `#475569`; Border `#E4ECFC`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#2563EB`
- Character: Global blue + teal + accent orange.

## 857. Calculator & Unit Converter palette

- Primary `#EA580C` / on `#000000`; Secondary `#F97316` / on `#000000`; Accent `#2563EB` / on `#FFFFFF`
- Background `#1C1917` / fg `#FFFFFF`; Card `#262321` / fg `#FFFFFF`; Muted `#2C1E16` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#EA580C`
- Character: Operation orange on dark.

## 858. Alarm & World Clock palette

- Primary `#D97706` / on `#000000`; Secondary `#F59E0B` / on `#0F172A`; Accent `#6366F1` / on `#000000`
- Background `#0F172A` / fg `#FFFFFF`; Card `#192134` / fg `#FFFFFF`; Muted `#1F1E27` / fg `#94A3B8`; Border `rgba(255,255,255,0.08)`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#D97706`
- Character: Time amber + night indigo on dark.

## 859. Plant Care Tracker palette

- Primary `#15803D` / on `#FFFFFF`; Secondary `#059669` / on `#000000`; Accent `#D97706` / on `#000000`
- Background `#F0FDF4` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F0F7F3` / fg `#475569`; Border `#E2EFE7`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#15803D`
- Character: Nature green + sun yellow.

## 860. Book & Reading Tracker palette

- Primary `#78716C` / on `#FFFFFF`; Secondary `#92400E` / on `#FFFFFF`; Accent `#D97706` / on `#000000`
- Background `#FFFBEB` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#F6F6F6` / fg `#475569`; Border `#EEEDED`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#78716C`
- Character: Book brown + page amber.

## 861. Gift & Wishlist palette

- Primary `#DC2626` / on `#FFFFFF`; Secondary `#D97706` / on `#000000`; Accent `#EC4899` / on `#000000`
- Background `#FFF1F2` / fg `#0F172A`; Card `#FFFFFF` / fg `#0F172A`; Muted `#FCF1F1` / fg `#475569`; Border `#FAE4E4`; Destructive `#DC2626` / on `#FFFFFF`; Ring `#DC2626`
- Character: Gift red + gold + surprise pink.

# Part 82 — Font Pairings

## 862. Pairing principles

- Pair for contrast of role, not of everything: a characterful heading face (serif, display, geometric) over a neutral, highly readable body face.
- Serif + Sans reads as elegant, editorial or authoritative; Sans + Sans reads as modern and product-like; Mono + Sans reads as technical; Display/Script + Sans reads as playful or emotional.
- A single family with weight steps (e.g. 400 body, 600 subheads, 700–800 headings) is the simplest, most coherent system for dashboards, SaaS and design systems.
- Display, script and all-caps faces are for headlines and accents only; never set body text, financial figures or legal text in them.
- Triple stacks assign a third face (usually mono or engraved caps) strictly to labels, tags, dates and data.
- For non-Latin markets choose a family with full script support (CJK, Arabic, Hebrew, Thai, Vietnamese); RTL scripts need RTL-aware layout.
- Use tight leading (`0.9`–`1.2`) and negative tracking for large headlines, `1.4`–`1.6` leading for body, and positive tracking (`+1`–`+3`) for small uppercase labels.
- Respect system font scaling; never lock text to fixed pixel sizes that ignore user preferences.

## 863. Classic Elegant

- Heading `Playfair Display`; body `Inter`; type `Serif + Sans`
- Mood: elegant, luxury, sophisticated, timeless, premium, editorial
- Best for: Luxury brands, fashion, spa, beauty, editorial, magazines, high-end e-commerce
- Notes: High contrast between elegant heading and clean body. Perfect for luxury/premium.

## 864. Modern Professional

- Heading `Poppins`; body `Open Sans`; type `Sans + Sans`
- Mood: modern, professional, clean, corporate, friendly, approachable
- Best for: SaaS, corporate sites, business apps, startups, professional services
- Notes: Geometric Poppins for headings, humanist Open Sans for readability.

## 865. Tech Startup

- Heading `Space Grotesk`; body `DM Sans`; type `Sans + Sans`
- Mood: tech, startup, modern, innovative, bold, futuristic
- Best for: Tech companies, startups, SaaS, developer tools, AI products
- Notes: Space Grotesk has unique character, DM Sans is highly readable.

## 866. Editorial Classic

- Heading `Cormorant Garamond`; body `Libre Baskerville`; type `Serif + Serif`
- Mood: editorial, classic, literary, traditional, refined, bookish
- Best for: Publishing, blogs, news sites, literary magazines, book covers
- Notes: All-serif pairing for traditional editorial feel.

## 867. Minimal Swiss

- Heading `Inter`; body `Inter`; type `Sans + Sans`
- Mood: minimal, clean, swiss, functional, neutral, professional
- Best for: Dashboards, admin panels, documentation, enterprise apps, design systems
- Notes: Single font family with weight variations. Ultimate simplicity.

## 868. Playful Creative

- Heading `Fredoka`; body `Nunito`; type `Display + Sans`
- Mood: playful, friendly, fun, creative, warm, approachable
- Best for: Children's apps, educational, gaming, creative tools, entertainment
- Notes: Rounded, friendly fonts perfect for playful UIs.

## 869. Bold Statement

- Heading `Bebas Neue`; body `Source Sans 3`; type `Display + Sans`
- Mood: bold, impactful, strong, dramatic, modern, headlines
- Best for: Marketing sites, portfolios, agencies, event pages, sports
- Notes: Bebas Neue for large headlines only. All-caps display font.

## 870. Wellness Calm

- Heading `Lora`; body `Raleway`; type `Serif + Sans`
- Mood: calm, wellness, health, relaxing, natural, organic
- Best for: Health apps, wellness, spa, meditation, yoga, organic brands
- Notes: Lora's organic curves with Raleway's elegant simplicity.

## 871. Developer Mono

- Heading `JetBrains Mono`; body `IBM Plex Sans`; type `Mono + Sans`
- Mood: code, developer, technical, precise, functional, hacker
- Best for: Developer tools, documentation, code editors, tech blogs, CLI apps
- Notes: JetBrains for code, IBM Plex for UI. Developer-focused.

## 872. Retro Vintage

- Heading `Abril Fatface`; body `Merriweather`; type `Display + Serif`
- Mood: retro, vintage, nostalgic, dramatic, decorative, bold
- Best for: Vintage brands, breweries, restaurants, creative portfolios, posters
- Notes: Abril Fatface for hero headlines only. High-impact vintage feel.

## 873. Geometric Modern

- Heading `Outfit`; body `Work Sans`; type `Sans + Sans`
- Mood: geometric, modern, clean, balanced, contemporary, versatile
- Best for: General purpose, portfolios, agencies, modern brands, landing pages
- Notes: Both geometric but Outfit more distinctive for headings.

## 874. Luxury Serif

- Heading `Cormorant`; body `Montserrat`; type `Serif + Sans`
- Mood: luxury, high-end, fashion, elegant, refined, premium
- Best for: Fashion brands, luxury e-commerce, jewelry, high-end services
- Notes: Cormorant's elegance with Montserrat's geometric precision.

## 875. Friendly SaaS

- Heading `Plus Jakarta Sans`; body `Plus Jakarta Sans`; type `Sans + Sans`
- Mood: friendly, modern, saas, clean, approachable, professional
- Best for: SaaS products, web apps, dashboards, B2B, productivity tools
- Notes: Single versatile font. Modern alternative to Inter.

## 876. News Editorial

- Heading `Newsreader`; body `Roboto`; type `Serif + Sans`
- Mood: news, editorial, journalism, trustworthy, readable, informative
- Best for: News sites, blogs, magazines, journalism, content-heavy sites
- Notes: Newsreader designed for long-form reading. Roboto for UI.

## 877. Handwritten Charm

- Heading `Caveat`; body `Quicksand`; type `Script + Sans`
- Mood: handwritten, personal, friendly, casual, warm, charming
- Best for: Personal blogs, invitations, creative portfolios, lifestyle brands
- Notes: Use Caveat sparingly for accents. Quicksand for body.

## 878. Corporate Trust

- Heading `Lexend`; body `Source Sans 3`; type `Sans + Sans`
- Mood: corporate, trustworthy, accessible, readable, professional, clean
- Best for: Enterprise, government, healthcare, finance, accessibility-focused
- Notes: Lexend designed for readability. Excellent accessibility.

## 879. Brutalist Raw

- Heading `Space Mono`; body `Space Mono`; type `Mono + Mono`
- Mood: brutalist, raw, technical, monospace, minimal, stark
- Best for: Brutalist designs, developer portfolios, experimental, tech art
- Notes: All-mono for raw brutalist aesthetic. Limited weights.

## 880. Fashion Forward

- Heading `Syne`; body `Manrope`; type `Sans + Sans`
- Mood: fashion, avant-garde, creative, bold, artistic, edgy
- Best for: Fashion brands, creative agencies, art galleries, design studios
- Notes: Syne's unique character for headlines. Manrope for readability.

## 881. Soft Rounded

- Heading `Varela Round`; body `Nunito Sans`; type `Sans + Sans`
- Mood: soft, rounded, friendly, approachable, warm, gentle
- Best for: Children's products, pet apps, friendly brands, wellness, soft UI
- Notes: Both rounded and friendly. Perfect for soft UI designs.

## 882. Premium Sans (DM Sans)

- Heading `DM Sans`; body `DM Sans`; type `Sans + Sans`
- Mood: premium, modern, clean, sophisticated, versatile, balanced
- Best for: Premium brands, modern agencies, SaaS, portfolios, startups
- Notes: One family with balanced weights covers every role in premium sans layouts.

## 883. Vietnamese Friendly

- Heading `Be Vietnam Pro`; body `Noto Sans`; type `Sans + Sans`
- Mood: vietnamese, international, readable, clean, multilingual, accessible
- Best for: Vietnamese sites, multilingual apps, international products
- Notes: Be Vietnam Pro excellent Vietnamese support. Noto as fallback.

## 884. Japanese Elegant

- Heading `Noto Serif JP`; body `Noto Sans JP`; type `Serif + Sans`
- Mood: japanese, elegant, traditional, modern, multilingual, readable
- Best for: Japanese sites, Japanese restaurants, cultural sites, anime/manga
- Notes: Noto fonts excellent Japanese support. Traditional + modern feel.

## 885. Korean Modern

- Heading `Noto Sans KR`; body `Noto Sans KR`; type `Sans + Sans`
- Mood: korean, modern, clean, professional, multilingual, readable
- Best for: Korean sites, K-beauty, K-pop, Korean businesses, multilingual
- Notes: Clean Korean typography. Single font with weight variations.

## 886. Chinese Traditional

- Heading `Noto Serif TC`; body `Noto Sans TC`; type `Serif + Sans`
- Mood: chinese, traditional, elegant, cultural, multilingual, readable
- Best for: Traditional Chinese sites, cultural content, Taiwan/Hong Kong markets
- Notes: Traditional Chinese character support. Elegant pairing.

## 887. Chinese Simplified

- Heading `Noto Sans SC`; body `Noto Sans SC`; type `Sans + Sans`
- Mood: chinese, simplified, modern, professional, multilingual, readable
- Best for: Simplified Chinese sites, mainland China market, business apps
- Notes: Simplified Chinese support. Clean modern look.

## 888. Arabic Elegant

- Heading `Noto Naskh Arabic`; body `Noto Sans Arabic`; type `Serif + Sans`
- Mood: arabic, elegant, traditional, cultural, RTL, readable
- Best for: Arabic sites, Middle East market, Islamic content, bilingual sites
- Notes: RTL support. Naskh for traditional, Sans for modern Arabic.

## 889. Thai Modern

- Heading `Noto Sans Thai`; body `Noto Sans Thai`; type `Sans + Sans`
- Mood: thai, modern, readable, clean, multilingual, accessible
- Best for: Thai sites, Southeast Asia, tourism, Thai restaurants
- Notes: Clean Thai typography. Excellent readability.

## 890. Hebrew Modern

- Heading `Noto Sans Hebrew`; body `Noto Sans Hebrew`; type `Sans + Sans`
- Mood: hebrew, modern, RTL, clean, professional, readable
- Best for: Hebrew sites, Israeli market, Jewish content, bilingual sites
- Notes: RTL support. Clean modern Hebrew typography.

## 891. Legal Professional

- Heading `EB Garamond`; body `Lato`; type `Serif + Sans`
- Mood: legal, professional, traditional, trustworthy, formal, authoritative
- Best for: Law firms, legal services, contracts, formal documents, government
- Notes: EB Garamond for authority. Lato for clean body text.

## 892. Medical Clean

- Heading `Figtree`; body `Noto Sans`; type `Sans + Sans`
- Mood: medical, clean, accessible, professional, healthcare, trustworthy
- Best for: Healthcare, medical clinics, pharma, health apps, accessibility
- Notes: Clean, accessible fonts for medical contexts.

## 893. Financial Trust

- Heading `IBM Plex Sans`; body `IBM Plex Sans`; type `Sans + Sans`
- Mood: financial, trustworthy, professional, corporate, banking, serious
- Best for: Banks, finance, insurance, investment, fintech, enterprise
- Notes: IBM Plex conveys trust and professionalism. Excellent for data.

## 894. Real Estate Luxury

- Heading `Cinzel`; body `Josefin Sans`; type `Serif + Sans`
- Mood: real estate, luxury, elegant, sophisticated, property, premium
- Best for: Real estate, luxury properties, architecture, interior design
- Notes: Cinzel's elegance for headlines. Josefin for modern body.

## 895. Restaurant Menu

- Heading `Playfair Display SC`; body `Karla`; type `Serif + Sans`
- Mood: restaurant, menu, culinary, elegant, foodie, hospitality
- Best for: Restaurants, cafes, food blogs, culinary, hospitality
- Notes: Small caps Playfair for menu headers. Karla for descriptions.

## 896. Art Deco

- Heading `Poiret One`; body `Didact Gothic`; type `Display + Sans`
- Mood: art deco, vintage, 1920s, elegant, decorative, gatsby
- Best for: Vintage events, art deco themes, luxury hotels, classic cocktails
- Notes: Poiret One for art deco headlines only. Didact for body.

## 897. Magazine Style

- Heading `Libre Bodoni`; body `Public Sans`; type `Serif + Sans`
- Mood: magazine, editorial, publishing, refined, journalism, print
- Best for: Magazines, online publications, editorial content, journalism
- Notes: Bodoni's editorial elegance. Public Sans for clean UI.

## 898. Crypto/Web3

- Heading `Orbitron`; body `Exo 2`; type `Sans + Sans`
- Mood: crypto, web3, futuristic, tech, blockchain, digital
- Best for: Crypto platforms, NFT, blockchain, web3, futuristic tech
- Notes: Orbitron for futuristic headers. Exo 2 for readable body.

## 899. Gaming Bold

- Heading `Russo One`; body `Chakra Petch`; type `Display + Sans`
- Mood: gaming, bold, action, esports, competitive, energetic
- Best for: Gaming, esports, action games, competitive sports, entertainment
- Notes: Russo One for impact. Chakra Petch for techy body text.

## 900. Indie/Craft

- Heading `Amatic SC`; body `Cabin`; type `Display + Sans`
- Mood: indie, craft, handmade, artisan, organic, creative
- Best for: Craft brands, indie products, artisan, handmade, organic products
- Notes: Amatic for handwritten feel. Cabin for readable body.

## 901. Startup Bold (Outfit + Rubik)

- Heading `Outfit`; body `Rubik`; type `Sans + Sans`
- Mood: startup, bold, modern, innovative, confident, dynamic
- Best for: Startups, pitch decks, product launches, bold brands
- Notes: Outfit for display headings, Rubik for body text.

## 902. E-commerce Clean

- Heading `Rubik`; body `Nunito Sans`; type `Sans + Sans`
- Mood: ecommerce, clean, shopping, product, retail, conversion
- Best for: E-commerce, online stores, product pages, retail, shopping
- Notes: Clean readable fonts perfect for product descriptions.

## 903. Academic/Research

- Heading `Crimson Pro`; body `Atkinson Hyperlegible`; type `Serif + Sans`
- Mood: academic, research, scholarly, accessible, readable, educational
- Best for: Universities, research papers, academic journals, educational
- Notes: Crimson for scholarly headlines. Atkinson for accessibility.

## 904. Dashboard Data

- Heading `Fira Code`; body `Fira Sans`; type `Mono + Sans`
- Mood: dashboard, data, analytics, code, technical, precise
- Best for: Dashboards, analytics, data visualization, admin panels
- Notes: Fira family cohesion. Code for data, Sans for labels.

## 905. Music/Entertainment

- Heading `Righteous`; body `Poppins`; type `Display + Sans`
- Mood: music, entertainment, fun, energetic, bold, performance
- Best for: Music platforms, entertainment, events, festivals, performers
- Notes: Righteous for bold entertainment headers. Poppins for body.

## 906. Minimalist Portfolio

- Heading `Archivo`; body `Space Grotesk`; type `Sans + Sans`
- Mood: minimal, portfolio, designer, creative, clean, artistic
- Best for: Design portfolios, creative professionals, minimalist brands
- Notes: Space Grotesk for distinctive headers. Archivo for clean body.

## 907. Kids/Education

- Heading `Baloo 2`; body `Comic Neue`; type `Display + Sans`
- Mood: kids, education, playful, friendly, colorful, learning
- Best for: Children's apps, educational games, kid-friendly content
- Notes: Fun, playful fonts for children. Comic Neue is readable comic style.

## 908. Wedding/Romance

- Heading `Great Vibes`; body `Cormorant Infant`; type `Script + Serif`
- Mood: wedding, romance, elegant, script, invitation, feminine
- Best for: Wedding sites, invitations, romantic brands, bridal
- Notes: Great Vibes for elegant accents. Cormorant for readable text.

## 909. Science/Tech

- Heading `Exo`; body `Roboto Mono`; type `Sans + Sans`
- Mood: science, technology, research, data, futuristic, precise
- Best for: Science, research, tech documentation, data-heavy sites
- Notes: Exo for modern tech feel. Roboto Mono for code/data.

## 910. Accessibility First

- Heading `Atkinson Hyperlegible`; body `Atkinson Hyperlegible`; type `Sans + Sans`
- Mood: accessible, readable, inclusive, WCAG, dyslexia-friendly, clear
- Best for: Accessibility-critical sites, government, healthcare, inclusive design
- Notes: Designed for maximum legibility. Excellent for accessibility.

## 911. Sports/Fitness

- Heading `Barlow Condensed`; body `Barlow`; type `Sans + Sans`
- Mood: sports, fitness, athletic, energetic, condensed, action
- Best for: Sports, fitness, gyms, athletic brands, competition
- Notes: Condensed for impact headlines. Regular Barlow for body.

## 912. Luxury Minimalist

- Heading `Bodoni Moda`; body `Jost`; type `Serif + Sans`
- Mood: luxury, minimalist, high-end, sophisticated, refined, premium
- Best for: Luxury minimalist brands, high-end fashion, premium products
- Notes: Bodoni's high contrast elegance. Jost for geometric body.

## 913. Tech/HUD Mono

- Heading `Share Tech Mono`; body `Fira Code`; type `Mono + Mono`
- Mood: tech, futuristic, hud, sci-fi, data, monospaced, precise
- Best for: Sci-fi interfaces, developer tools, cybersecurity, dashboards
- Notes: Share Tech Mono has that classic sci-fi look.

## 914. Pixel Retro

- Heading `Press Start 2P`; body `VT323`; type `Display + Sans`
- Mood: pixel, retro, gaming, 8-bit, nostalgic, arcade
- Best for: Pixel art games, retro websites, creative portfolios
- Notes: Press Start 2P is very wide/large. VT323 is better for body text.

## 915. Neubrutalist Bold

- Heading `Lexend Mega`; body `Public Sans`; type `Display + Sans`
- Mood: bold, neubrutalist, loud, strong, geometric, quirky
- Best for: Neubrutalist designs, Gen Z brands, bold marketing
- Notes: Lexend Mega has distinct character and variable weight.

## 916. Academic/Archival

- Heading `EB Garamond`; body `Crimson Text`; type `Serif + Serif`
- Mood: academic, old-school, university, research, serious, traditional
- Best for: University sites, archives, research papers, history
- Notes: Classic academic aesthetic. Very legible.

## 917. Spatial Clear

- Heading `Inter`; body `Inter`; type `Sans + Sans`
- Mood: spatial, legible, glass, system, clean, neutral
- Best for: Spatial computing, AR/VR, glassmorphism interfaces
- Notes: Optimized for readability on dynamic backgrounds.

## 918. Kinetic Motion

- Heading `Syncopate`; body `Space Mono`; type `Display + Mono`
- Mood: kinetic, motion, futuristic, speed, wide, tech
- Best for: Music festivals, automotive, high-energy brands
- Notes: Syncopate's wide stance works well with motion effects.

## 919. Gen Z Brutal

- Heading `Anton`; body `Epilogue`; type `Display + Sans`
- Mood: brutal, loud, shouty, meme, internet, bold
- Best for: Gen Z marketing, streetwear, viral campaigns
- Notes: Anton is impactful and condensed. Good for stickers/badges.

## 920. Bauhaus Geometric

- Heading `Outfit`; body `Outfit`; type `Geometric Sans + Single Weight`
- Mood: bauhaus, geometric, constructivist, bold, uppercase, architectural, mechanical, poster, tactile
- Best for: Bauhaus mobile apps, bold editorial mobile, design-forward branding apps, art/culture platforms
- Notes: Single-family system: Outfit `900` uppercase with very tight tracking for heroes; Outfit `700` uppercase for buttons and nav; Outfit `500` for body. Scale aggressively: roughly `36`–`48px` headlines on mobile.

## 921. Minimalist Monochrome Editorial

- Heading `Playfair Display`; body `Source Serif 4`; type `Serif + Serif + Mono (Triple Stack)`
- Mood: monochrome, editorial, austere, typographic, pocket manifesto, luxury, high contrast, brutalist mobile
- Best for: Luxury fashion mobile apps, editorial publications, digital exhibitions, portfolio apps, high-contrast e-reader aesthetics
- Notes: Triple stack: Playfair Display `900`, tight tracking, leading `0.9` for heroes at roughly `48`–`60px` so words break graphically; Source Serif 4 `300`–`600` for body; JetBrains Mono `400`–`500` uppercase with wide tracking for tags, dates and labels. No UI sans-serif at all — 100% serif and mono.

## 922. Modern Dark Cinema (Inter System)

- Heading `Inter`; body `Inter`; type `Sans + Mono`
- Mood: dark, cinematic, technical, precision, clean, premium, developer, professional, high-end utility
- Best for: Developer tools, fintech/trading, AI dashboards, streaming platforms, high-end productivity apps
- Notes: Single-family precision system: Inter `700` (tracking `-1.5`) for Display `48pt`; Inter `600` (tracking `-0.5`) for H1 `32pt` / H2 `24pt`; Inter `400` for body `16pt`; Inter `500` uppercase, tracking `+1.2` for labels. Major headers can use a white-to-translucent gradient (`#FFFFFF` to `rgba(255,255,255,0.7)`).

## 923. SaaS Mobile Boutique (Calistoga + Inter)

- Heading `Calistoga`; body `Inter`; type `Display Serif + Sans + Mono`
- Mood: saas, boutique, electric, warm, editorial, bold, premium, fintech, business, dual font, human warmth
- Best for: B2B SaaS mobile, fintech apps, analytics dashboards, marketing tools, operations platforms
- Notes: Tri-stack: Calistoga for heroes `36`–`42pt`, leading `1.1` (adds human warmth); Inter `400`–`600` for body/UI `16`–`18pt`; JetBrains Mono `12pt` uppercase, tracking `1.5` for data labels and section badges. Section H2 `28`–`32pt`, labels `12pt`. Avoid italic Calistoga except for editorial callouts.

## 924. Terminal CLI Monospace

- Heading `JetBrains Mono`; body `JetBrains Mono`; type `Mono + Mono (Single Family)`
- Mood: terminal, cli, hacker, monospace, matrix, developer, retro-future, command line, precision, OLED
- Best for: Developer tools, Web3/blockchain apps, hacker aesthetic, sci-fi games, ARG, security tools, geek-culture portfolios
- Notes: Single monospace system: only JetBrains Mono (Space Mono as fallback). Strict sizes `12` / `14` / `16pt` only. Weight `400` (bold ruins mono character). Line height `1.2x` for density, normal letter spacing. All UI labels uppercase; ASCII borders and text-based progress bars.

## 925. Kinetic Brutalism (Space Grotesk)

- Heading `Space Grotesk`; body `Space Grotesk`; type `Geometric Sans (Single Dominant)`
- Mood: kinetic, brutalist, aggressive, uppercase, oversized, display, motion, street, bold, high-energy, zine
- Best for: Music/culture apps, sports platforms, brand flagship mobile, performance dashboards, underground product drops
- Notes: Dominant single family: Space Grotesk `700` for display, `400`–`600` for body and support. Scale: hero `60`–`120pt` (scaled to screen width), section `40`–`50pt`, card titles `28`–`32pt`, body `18`–`20pt`, labels `12pt`. All display, buttons and nav uppercase; tracking `-1` on large type, `+2` on labels; line height `0.9`–`1.1x`. Sans-serif system fallback; scale with pixel density.

## 926. Flat Design Mobile (System Bold)

- Heading `Inter`; body `Inter`; type `Sans + Sans`
- Mood: flat, clean, system, bold, geometric, cross-platform, icon, poster, minimal, functional, responsive
- Best for: Cross-platform apps, dashboards, system UI, onboarding, marketing pages, informational apps, icon-heavy interfaces
- Notes: System-first: Inter primary, falling back to the platform system sans. Headlines weight `800`, tracking `-0.5`; subheads `600` at `18`; body `400`, line height `24`; labels `700` uppercase, tracking `1`. With no shadows, thick weights carry all hierarchy; use poster-like size contrast (body `16pt` vs headline `40pt+`). Avoid italic.

## 927. Material You MD3 (Roboto System)

- Heading `Roboto`; body `Roboto`; type `Sans (System Default)`
- Mood: material design 3, md3, android, google, tonal, friendly, rounded, accessible, adaptive
- Best for: Android apps, cross-platform tools, productivity software, data-heavy B2B dashboards, enterprise mobile
- Notes: Material 3 type scale: Display Large `56/400/64`; Headline Large `32/500/40`; Title Large `22/500/28`; Body Large `16/400/24`; Label Medium `12/500/16`. Buttons and labels tracking `0.1px`. Use system Roboto on Android and bundle it on iOS for parity. Stay within weights `300`–`700`.

## 928. Neo Brutalism Mobile (Space Grotesk Bold)

- Heading `Space Grotesk`; body `Space Grotesk`; type `Geometric Sans (Bold-Only)`
- Mood: neo brutalism, pop art, loud, bold, heavy, stickers, mechanical, high contrast, cream, gen-z
- Best for: Creative tools, Gen-Z marketing, e-commerce for youth culture, content portfolios, collage-style apps
- Notes: Single weight: Space Grotesk `700` everywhere. Display `48`–`64px`, heading `24`–`32px`, body `18`–`20px` for deliberate brutalist density, labels `14px` all caps, tracking `2`. Buttons and nav uppercase. Bold sans fallback; no italic or thin weights.

## 929. Bold Typography Mobile (Inter Poster)

- Heading `Inter`; body `Playfair Display`; type `Sans + Serif (Display) + Mono`
- Mood: bold typography, editorial, poster, near-black, vermillion, luxury, type-as-hero, manifesto, high-contrast
- Best for: Creative brand flagships, reading platforms, event apps, flash pages, luxury mobile experiences
- Notes: Tri-stack: Inter `600`–`800` for UI and display (tracking `-1.5px` heroes, `-0.5px` subheads); Playfair Display Italic only for pull quotes; JetBrains Mono for labels and stats. Scale `12` labels, `16` body, `22` subhead, `32` section, `40` H2, `56` H1, `72px` hero statement. Line height `1.1` headlines, `1.6` body. Keep links visibly identifiable; never fake buttons with styled underlines.

## 930. Academia Mobile (Cormorant + Crimson + Cinzel)

- Heading `Cormorant Garamond`; body `Crimson Pro`; type `Serif + Book Serif + Engraved (Triple Stack)`
- Mood: academia, library, mahogany, parchment, brass, scholarly, prestige, antique, victorian, leather
- Best for: Knowledge management apps, scholarly reading tools, personal brand portfolios, RPG games, cultural community platforms
- Notes: Triple stack: Cormorant Garamond Medium for all headings (`32`–`40px`, tight leading); Crimson Pro Regular for reading text (`16`–`18px`, line height `24`–`26px`); Cinzel SemiBold for all-caps labels, overlines and section prefixes (`10`–`12px`, tracking `2`–`3px`). Drop caps: `60px` Cinzel in brass `#C9A962`; section prefixes like VOLUME I/II/III in Cinzel `10px`. No sans-serif anywhere.

## 931. Cyberpunk Mobile (Orbitron + JetBrains Mono)

- Heading `Orbitron`; body `JetBrains Mono`; type `Tech Display + Mono`
- Mood: cyberpunk, neon, glitch, hud, sci-fi, dark, matrix green, magenta, chamfered, tactical
- Best for: Gaming companion apps, fintech/crypto, data visualization, dark brand apps, cyberpunk narrative games
- Notes: Dual stack: Orbitron `700`–`900` for H1 (`42px`, uppercase, tracking `4`, weight `900`); JetBrains Mono `400`–`500` for all body and data (`14px`, tracking `1`). Labels `10px` uppercase at `0.7` opacity. Scale H1 `42`, H2 `28`, section `20px`. Body monospace only, no mixed sans; monospace system fallback.

## 932. Web3 Bitcoin DeFi (Space Grotesk + Inter + Mono)

- Heading `Space Grotesk`; body `Inter`; type `Geometric Sans + Sans + Mono (Triple)`
- Mood: web3, bitcoin, defi, digital gold, fintech, crypto, trustless, luminescent, precision, dark
- Best for: DeFi protocols and wallets, NFT platforms, metaverse social apps, high-tech brand landing pages
- Notes: Tri-stack: Space Grotesk `600`–`700` for headings; Inter `400`–`600` for body and UI; JetBrains Mono Medium for all data, stats, prices and hashes. Buttons Inter Bold uppercase, tracking `1.5`. Balance figures can use an orange-to-gold gradient. Scale H1 `36`–`42px`, H2 `24`–`28px`, body `16`–`18px`, mono labels `12`–`14px`.

## 933. Claymorphism Mobile (Nunito + DM Sans)

- Heading `Nunito`; body `DM Sans`; type `Display Rounded + Geometric Sans`
- Mood: claymorphism, clay, rounded, playful, candy, bubbly, soft, 3d, children, education, tactile, spring, nunito, dm sans
- Best for: Children education apps, teen social, brand mascot apps, creative tools, fintech gamification
- Notes: Dual stack: Nunito Black `900` or ExtraBold `800` for all headings (rounded terminals mandatory); DM Sans Medium `500` for body. Scale hero `48/52` tracking `-1`, section `32/38`, card title `22/28`, body `16/24`. Never Nunito for body (too decorative small); never below `700` for headings. Remove extra font padding so text centres in rounded buttons.

## 934. Enterprise SaaS Mobile (Plus Jakarta Sans)

- Heading `Plus Jakarta Sans`; body `Plus Jakarta Sans`; type `Geometric Sans (Single Family)`
- Mood: enterprise, saas, b2b, professional, indigo, modern, approachable, legible, ios dynamic type, android scaling
- Best for: B2B SaaS apps, productivity tools, government and finance mobile apps, admin dashboards, enterprise onboarding
- Notes: Single family: ExtraBold `800` for screen titles/hero (line height `1.1`–`1.2`), Bold `700` section headers, SemiBold `600` card titles and buttons, Regular `400` body (line height `1.4`–`1.5`). Must honour platform dynamic type and font scaling. Buttons uppercase, tracking `0.5`. Captions `12px` Regular; muted text slate `#64748B`.

## 935. Sketch Hand-Drawn Mobile (Kalam + Patrick Hand)

- Heading `Kalam`; body `Patrick Hand`; type `Handwritten + Handwritten (Dual)`
- Mood: sketch, hand-drawn, handwriting, human, imperfect, organic, paper, kalam, patrick hand, education, journal, creative
- Best for: Journaling apps, prototype tools, children's picturebook apps, creative platforms, gamified puzzle apps
- Notes: Dual handwritten stack: Kalam Bold `700` for headings (felt-tip, intentional messiness); Patrick Hand Regular for body (legible yet human). Heading `28`–`36px` with line height adjusted for descenders; body `16`–`18px`, line height `1.5`; labels `14px`. Vary sizes slightly between neighbours for spontaneity. Left-align long body text. Never use for financial figures or legal text.

## 936. Neumorphism Mobile (Plus Jakarta Sans + System)

- Heading `Plus Jakarta Sans`; body `Plus Jakarta Sans`; type `Geometric Sans (System Fallback)`
- Mood: neumorphism, soft ui, monochromatic, cool grey, minimal, physical, depth, ceramic, system font, utility
- Best for: Smart home controls, minimal tools, aesthetic dashboards, health monitors, brand showcase pages
- Notes: Plus Jakarta Sans Bold/Medium (or the system sans) on a monochrome `#E0E5EC` surface. Heading `24`–`32px` Bold `700`, tracking `-0.5`; body `16px` Medium `500`, line height `1.4`; caption `12px` Regular. Primary text `#3D4852` (`7.5:1` on `#E0E5EC`), muted `#6B7280` (`4.6:1`). Accent `#6C63FF` only for active labels or focus. Never italic or thin weights — they vanish against embossed surfaces.

# Part 83 — Icon Semantics & Usage

## 937. General icon rules

- Choose the most semantically precise icon for the meaning, even beyond a curated set; keep one visual icon family per surface and use a second family only as a consistent fallback.
- Default style is outline at regular weight; default size `20px` for UI controls, `24px` for emphasised feature icons, `32px` for feature anchors.
- Decide the context by use: decorative (beside visible text) must be hidden from assistive tech; meaningful (no equivalent visible text) needs a text alternative; interactive (inside a control) needs an accessible name on the control.
- Toggle controls driven by icons must expose state (pressed / expanded) as well as a name.
- Every icon in the set may appear in decorative, meaningful or interactive contexts; its semantic role says how it is most often used.
- Spinners (e.g. `circle-notch`) rotate continuously to signal loading and should be paired with a text alternative.

## 938. Navigation icons

- `list` — means hamburger menu navigation toggle bars; use for mobile navigation drawer toggle sidebar; role `interactive`
- `arrow-left` — means back previous return navigate; use for back button breadcrumb navigation; role `interactive`
- `arrow-right` — means next forward continue navigate; use for forward button next step cta; role `interactive`
- `caret-down` — means dropdown expand accordion select; use for dropdown toggle accordion header; role `interactive`
- `caret-up` — means collapse close accordion minimize; use for accordion collapse minimize; role `interactive`
- `house` — means homepage main dashboard start; use for home navigation main page; role `meaningful`
- `x` — means close cancel dismiss remove exit; use for modal close dismiss button; role `interactive`
- `arrow-square-out` — means open new tab external link; use for external link indicator; role `interactive`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 939. Action icons

- `plus` — means add create new insert; use for add button create new item; role `interactive`
- `minus` — means remove subtract decrease delete; use for remove item quantity decrease; role `interactive`
- `trash` — means delete remove discard bin; use for delete action destructive; role `interactive`
- `pencil-simple` — means pencil modify change update; use for edit button modify content; role `interactive`
- `floppy-disk` — means disk store persist save; use for save button persist changes; role `interactive`
- `download-simple` — means export save file download; use for download file export; role `meaningful`
- `upload-simple` — means import file attach upload; use for upload file import; role `meaningful`
- `copy` — means duplicate clipboard paste; use for copy to clipboard; role `meaningful`
- `share` — means social distribute send; use for share button social; role `interactive`
- `magnifying-glass` — means find lookup filter query; use for search input bar; role `interactive`
- `funnel` — means sort refine narrow options; use for filter dropdown sort; role `interactive`
- `gear` — means gear cog preferences config; use for settings page configuration; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 940. Status icons

- `check` — means success done complete verified; use for success state checkmark; role `meaningful`
- `check-circle` — means success verified approved complete; use for success badge verified; role `meaningful`
- `x-circle` — means error failed cancel rejected; use for error state failed; role `meaningful`
- `warning` — means warning caution attention danger; use for warning message caution; role `meaningful`
- `warning-circle` — means info notice information help; use for info notice alert; role `meaningful`
- `info` — means information help tooltip details; use for information tooltip help; role `meaningful`
- `circle-notch` — means loading spinner processing wait; use for loading state spinner; role `meaningful`
- `clock` — means time schedule pending wait; use for pending time schedule; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 941. Communication icons

- `envelope` — means email message inbox letter; use for email contact inbox; role `meaningful`
- `chat-circle` — means chat comment bubble conversation; use for chat comment message; role `meaningful`
- `phone` — means call mobile telephone contact; use for phone contact call; role `meaningful`
- `paper-plane-tilt` — means submit dispatch message airplane; use for send message submit; role `meaningful`
- `bell` — means notification alert ring reminder; use for notification bell alert; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 942. User & account icons

- `user` — means profile account person avatar; use for user profile account; role `meaningful`
- `users` — means team group people members; use for team group members; role `meaningful`
- `user-plus` — means add invite new member; use for add user invite; role `interactive`
- `sign-in` — means signin authenticate enter; use for login signin; role `meaningful`
- `sign-out` — means signout exit leave logout; use for logout signout; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 943. Media icons

- `image` — means photo picture gallery thumbnail; use for image photo gallery; role `meaningful`
- `video` — means movie film play record; use for video player media; role `interactive`
- `play` — means start video audio media; use for play button video audio; role `interactive`
- `pause` — means stop halt video audio; use for pause button media; role `interactive`
- `speaker-high` — means sound audio speaker music; use for volume audio sound; role `meaningful`
- `microphone` — means microphone record voice audio; use for microphone voice record; role `meaningful`
- `camera` — means photo capture snapshot picture; use for camera photo capture; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 944. Commerce icons

- `shopping-cart` — means cart checkout basket buy; use for shopping cart e-commerce; role `meaningful`
- `shopping-bag` — means purchase buy store bag; use for shopping bag purchase; role `meaningful`
- `credit-card` — means payment card checkout stripe; use for payment credit card; role `interactive`
- `currency-dollar` — means money price currency cost; use for price money currency; role `meaningful`
- `tag` — means label price discount sale; use for price tag label; role `meaningful`
- `gift` — means present reward bonus offer; use for gift reward offer; role `meaningful`
- `percent` — means discount sale offer promo; use for discount percentage sale; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 945. Data & analytics icons

- `chart-bar` — means analytics statistics graph metrics; use for bar chart analytics; role `meaningful`
- `chart-pie` — means statistics distribution breakdown; use for pie chart distribution; role `meaningful`
- `trend-up` — means growth increase positive trend; use for growth trend positive; role `meaningful`
- `trend-down` — means decline decrease negative trend; use for decline trend negative; role `meaningful`
- `pulse` — means activity heartbeat monitor live; use for activity monitor pulse; role `meaningful`
- `database` — means storage server data backend; use for database storage; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 946. File icons

- `file` — means document page paper doc; use for file document; role `meaningful`
- `file-text` — means document text page article; use for text document article; role `meaningful`
- `folder` — means directory organize group files; use for folder directory; role `meaningful`
- `folder-open` — means expanded browse files view; use for open folder browse; role `meaningful`
- `paperclip` — means attachment attach file link; use for attachment paperclip; role `meaningful`
- `link` — means url hyperlink chain connect; use for link url hyperlink; role `meaningful`
- `clipboard` — means paste copy buffer notes; use for clipboard paste; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 947. Layout & view icons

- `grid-four` — means tiles gallery layout dashboard; use for grid layout gallery; role `meaningful`
- `list-bullets` — means rows table lines items; use for list view rows; role `meaningful`
- `columns` — means layout split dual sidebar; use for column layout split; role `meaningful`
- `arrows-out` — means fullscreen expand enlarge zoom; use for fullscreen maximize; role `meaningful`
- `arrows-in` — means reduce shrink collapse exit; use for minimize reduce; role `meaningful`
- `sidebar` — means panel drawer navigation menu; use for sidebar panel; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 948. Social & feedback icons

- `heart` — means like love favorite wishlist; use for like favorite love; role `meaningful`
- `star` — means rating review favorite bookmark; use for star rating favorite; role `meaningful`
- `thumbs-up` — means like approve agree positive; use for like approve thumb; role `meaningful`
- `thumbs-down` — means dislike disapprove disagree negative; use for dislike disapprove; role `meaningful`
- `bookmark` — means save later favorite mark; use for bookmark save; role `meaningful`
- `flag` — means report mark important highlight; use for flag report; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 949. Device icons

- `device-mobile` — means mobile phone device touch; use for mobile smartphone; role `meaningful`
- `device-tablet` — means ipad device touch screen; use for tablet device; role `meaningful`
- `monitor` — means desktop screen computer display; use for desktop monitor; role `meaningful`
- `laptop` — means notebook computer portable device; use for laptop computer; role `meaningful`
- `printer` — means print document output paper; use for printer print; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 950. Security icons

- `lock` — means secure password protected private; use for lock secure; role `meaningful`
- `lock-open` — means open access unsecure public; use for unlock open; role `meaningful`
- `shield` — means protection security safe guard; use for shield protection; role `meaningful`
- `key` — means password access unlock login; use for key password; role `meaningful`
- `eye` — means view show visible password; use for show password view; role `meaningful`
- `eye-slash` — means hide invisible password hidden; use for hide password; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 951. Location icons

- `map-pin` — means location marker place address; use for location pin marker; role `meaningful`
- `map-trifold` — means map directions navigate geography location; use for map directions; role `meaningful`
- `compass` — means compass direction pointer arrow; use for navigation compass; role `meaningful`
- `globe` — means world international global web; use for globe world; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 952. Time & history icons

- `calendar` — means date schedule event appointment; use for calendar date; role `meaningful`
- `arrows-clockwise` — means reload sync update refresh; use for refresh reload; role `meaningful`
- `arrow-counter-clockwise` — means undo back revert history; use for undo revert; role `meaningful`
- `arrow-clockwise` — means redo forward repeat history; use for redo forward; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 953. Development icons

- `code` — means develop programming syntax html; use for code development; role `meaningful`
- `terminal` — means console cli command shell; use for terminal console; role `meaningful`
- `git-branch` — means version control branch merge; use for git branch; role `meaningful`
- `github-logo` — means repository code open source; use for github repository; role `meaningful`
- Style: outline, regular weight, `20px`; allowed contexts: decorative, meaningful, interactive

## 954. Bold typography icon system

- Outline, regular weight; `20px` for UI controls, `32px` for feature anchors.
- Icons must be paired with a monospace text label; standalone icons only for standard navigation such as a back arrow.
- Colour only in the single accent `#FF3D00`.

## 955. Cyberpunk HUD icon system

- Outline, regular weight, `24px`, in the accent matrix green `#00FF88`.
- Simulate neon glow with an accent-coloured shadow (opacity `0.6`, blur radius `8`) on a square-cornered wrapper (radius `0`); avoid rounded icon containers.
- Always pair each icon with a monospace data label.

## 956. Academia icon system

- Thin weight for an engraved feel, about `22px`, in brass `#C9A962`.
- Prefer book, scroll, key and quill metaphors; avoid sharp geometric, tech-inspired, neon or saturated icons.
- Wrap icons in a circle with a `1px` brass border; every icon-only navigation item needs an accessible label.

## 957. Bitcoin DeFi icon system

- Outline, regular weight, `24px`, in bitcoin orange `#F7931A`.
- Wrap icons in a circular frosted-blur container with a `1px` `#F7931A` border and an orange glow (opacity `0.4`, blur radius `8`) for a holographic node effect.
- Prefer finance and data icons (trend-up, wallet, shield, layers); label every data icon in monospace.

# Part 84 — Choosing Typefaces from a Large Library

## 958. Narrowing a large font library

- Filter first by category: sans serif (the largest group, ~37%) for UI and body, serif for editorial and authority, display and handwriting (together ~42%) only for headlines and accents, monospace (under 3%) for code and data.
- Use stroke class (sans, serif, slab serif) to find body-safe faces even among display families; a slab-serif stroke suits sturdy, mechanical or retro headlines.
- Treat display, handwriting and symbol classifications as non-text faces; never use them for long reading copy.
- Prefer variable families (weight axis most common; width, optical size and slant also available) so one file covers the whole weight scale and optical sizing.
- Check script subsets (latin-ext, vietnamese, cyrillic, greek, CJK) before committing; pan-script families such as Noto are the safe fallback for multilingual products, and popularity rank is a proxy for rendering maturity.

# Part 85 — Cross-Platform UI Principles

## 959. Semantic Design Tokens
- Rule: every color, spacing, radius and type value comes from a named, centralized token, never a literal scattered in components. Severity: Medium–High.
- Do: name tokens by intent (`primary`, `primary-foreground`, `success`, `warning`, `danger`, `background`), and give each surface token a matching foreground token.
- Don't: repeat hex codes in selectors, templates or per-element setters; name tokens by visual appearance ("blue-ish") so the intent is hidden.
- Applies everywhere: CSS custom properties / `@theme` on the web, `ThemeData`/`ColorScheme` in Flutter, Material 3 tokens in Compose and Angular Material, resource dictionaries in XAML, looked-up colors in JavaFX.

## 960. Dark Mode and Theme Variants
- Rule: support light and dark from day one; every custom token needs a value in both schemes. Severity: Medium–High.
- Do: follow the system preference by default and let users override it; switch themes in one central place (a theme service or root provider).
- Don't: ship light-only themes, define a token for only one scheme, or let individual screens or controllers pick their own theme.
- Hardcoded colors are the most common cause of dark-mode breakage on every platform.

## 961. High Contrast and Status-Color Contrast
- Rule: honor OS high-contrast / contrast themes and check that text stays readable on every status background. Severity: High.
- Do: use system or theme brushes that adapt to contrast themes; check text on success, warning, danger and selected-row backgrounds.
- Don't: assume brand colors are accessible; use hardcoded colors that disappear in high contrast.

## 962. Type Scale and User Text Scaling
- Rule: use a fixed type scale and respect the user's text-size setting. Severity: High (scaling) / Low (scale).
- Do: pick sizes from the scale (e.g. `text-sm`/`base`/`lg`/`xl`, `MaterialTheme.typography`); support Dynamic Type (iOS), `TextScaler` (Flutter) and platform font scaling (Uno, Android).
- Don't: use arbitrary font sizes, hardcoded `sp`/pt values outside the type system, or layouts that break when text grows.

## 963. Spacing Rhythm
- Rule: all gaps come from one spacing scale applied the same way everywhere. Severity: Low–Medium.
- Do: use container-level gap/spacing (`gap-*`, `space-y-*`, `SizedBox`, `Arrangement`, shared Insets constants) and group related controls visibly.
- Don't: use magic-number margins, per-child margins to fake gaps, or negative margins to patch layout bugs.

## 964. Constraint-Based Layout over Fixed Sizes
- Rule: layouts grow and shrink with the window or screen; fixed pixel sizes are the exception. Severity: Medium–High.
- Do: use proportional and auto sizing (`*`/`Auto`, `Expanded`, `hgrow`/`vgrow`, `.frame(maxWidth: .infinity)`, Min/Max width) and wrap overflowing content in a scroll container.
- Don't: use absolute positioning for resizable screens, lock every control to a fixed width/height, or clip content without a way to scroll.

## 965. Choosing the Right Layout Primitive
- Rule: pick the simplest container that expresses the layout intent. Severity: Medium.
- Do: use linear stacks (Row/Column, StackPanel, VBox/HBox, VStack/HStack) for simple flows, a grid for forms and 2D layouts, docking/border shells for app frames, and overlap containers (Box/ZStack/Stack) only when children truly overlap.
- Don't: use a grid with one column for a list, or an overlap container as a column.

## 966. Shallow Visual Trees
- Rule: keep layout nesting shallow; deep trees cost measure/layout time and are hard to maintain. Severity: Medium–High.
- Do: adjust layout with modifiers or attached properties instead of wrapper elements; pull deep subtrees out into reusable components.
- Don't: nest 10+ levels, wrap content in extra containers just for padding, or use extra divs/panels to hide default templates.

## 967. Visible Focus and Full Keyboard Operability
- Rule: every function works from the keyboard and focus is always visible. Severity: High.
- Do: keep focus rings (web: `focus-visible:ring-2` with `ring-offset-2`), keep a logical tab order, and add access keys, mnemonics and keyboard accelerators for frequent actions.
- Don't: remove outlines without a replacement, or build interactions that only work with a mouse or with touch.

## 968. Accessible Names and Semantic Controls
- Rule: use the control that matches the job and give every interactive element an accessible name. Severity: High.
- Do: use button for actions, links for navigation, checkbox/toggle for booleans; label icon-only buttons (`aria-label`, `accessibilityLabel`, `contentDescription`, `AutomationProperties.Name`, `accessibleText` + tooltip).
- Don't: make clickable divs or TextBlocks with click handlers, render a button that acts as a link, or ship unlabeled icon buttons.

## 969. Form Labels and Validation Feedback
- Rule: every field has a visible, associated label, and errors appear next to the field at the right moment. Severity: High.
- Do: associate labels with controls (`htmlFor`/`id`, field wrappers, `setLabelFor`); show errors once a field has been touched or on submit; on long forms, add a summary at the top plus inline messages; keep user input after a validation failure.
- Don't: use a placeholder as the only label, show every error on page load, show one generic alert after submit, or clear fields when validation fails.

## 970. Loading, Busy and Progress States
- Rule: every async action shows feedback and blocks duplicate activation. Severity: High.
- Do: show skeletons that match the final layout for content loading, spinners or rings for indeterminate work, progress bars for determinate work, and disable the triggering control while busy (`aria-busy`, CanExecute=false).
- Don't: show a blank screen while loading, leave a button clickable during submit, or use a spinner where a content skeleton fits.

## 971. Error Containment and Recovery
- Rule: a failure in one region must not take down the whole UI, and the user must keep their context. Severity: High.
- Do: put error boundaries at feature level with a recovery action; show retryable errors inline; keep form and table state after a service failure.
- Don't: let one render error unmount the app, clear the screen on a network failure, or silently swallow rejected promises.

## 972. Empty States
- Rule: empty lists and tables explain why they are empty and what to do next. Severity: Low.
- Do: set placeholder content with guidance or a next action.
- Don't: leave blank white areas that look broken.

## 973. Motion Timing and Purpose
- Rule: motion explains state changes and never delays work. Severity: Medium.
- Values: UI transitions 150–300ms (desktop reveal/hover/selection 150–250ms); avoid 1000ms+ for UI elements.
- Do: add short transitions to hover and state changes; use built-in implicit animations for simple cases and timelines for sequences.
- Don't: change hover states instantly with no transition, put long timelines on every layout change, use continuous unbounded animations, or make understanding depend on animation.

## 974. Reduced Motion
- Rule: respect the OS reduced-motion setting everywhere, and update live if it changes. Severity: High.
- Do: gate decorative and auto-playing motion (`motion-reduce:animate-none`, `accessibilityReduceMotion`, `prefers-reduced-motion` listener); offer an in-app setting where the OS gives no signal.
- Don't: ignore the preference, or read it once at startup and never again.

## 975. Virtualized Lists and Stable Item Identity
- Rule: long collections render only visible items, and every item has a stable key. Severity: High.
- Values: virtualize from roughly 50–100+ items.
- Do: use virtualized lists (FlatList, ListView.builder, LazyColumn, LazyVStack, virtualizing panels, TableView) and key items by stable IDs.
- Don't: map thousands of items inside a plain scroll container, or use the array index as the key for dynamic lists (state and animations attach to the wrong rows).

## 976. Responsive Main Thread
- Rule: the UI thread only renders and handles input; heavy work runs elsewhere. Severity: High.
- Do: run I/O asynchronously, push CPU work to background tasks, and send results back to the UI thread through the platform dispatcher.
- Don't: run network, file or database work in click handlers, block on async results (`.Result`/`.Wait()`), or touch UI objects from background threads.

## 977. Layout Stability
- Rule: reserve space for content that loads late so nothing jumps. Severity: High.
- Do: give images and media explicit dimensions or an aspect ratio, give SVGs intrinsic `width`/`height`, and use skeletons sized like the real content.
- Don't: let images set the layout after they load, or let content pop in and push other content around.

## 978. Built-In Components Before Custom Ones
- Rule: use the platform's or design system's component for a standard pattern (dialog, sheet, tabs, toast, date picker, search box, navigation shell) before building a custom one. Severity: Medium.
- Do: change built-ins with variants, size props and lightweight overrides.
- Don't: rebuild a dialog, hamburger menu or tab control by hand; edit library source; copy full templates to make small tweaks.

## 979. Touch Targets and Input Parity
- Rule: touch targets are at least 44px, and every pointer interaction has a touch equivalent. Severity: High.
- Values: `min-h-11 min-w-11` (44px); enlarge small icons with `hitSlop` or padding.
- Do: give visible press feedback (ripple or opacity change) and handle touch alongside mouse.
- Don't: ship tiny tap targets, press interactions with no feedback, or mouse-only interaction.

## 980. Announcing Dynamic Changes
- Rule: content that changes without a page change is announced to assistive tech, and ARIA state tracks UI state. Severity: Medium.
- Do: use live regions (`aria-live`) for async updates; bind state attributes (`aria-expanded`) to real state.
- Don't: update content silently, or leave ARIA values fixed while the UI changes.

## 981. Verify on Real Targets
- Rule: test visuals, themes and assistive tech on each target platform and device. Severity: High.
- Do: test just below, at and just above each breakpoint; test with VoiceOver, TalkBack and Narrator; test real phones as well as simulators; test each renderer and OS.
- Don't: only test on your development device, or assume themes render the same everywhere.

# Part 86 — Web Utility-CSS & Component Libraries

## 982. Utility Theme Tokens
- Rule: declare semantic tokens in a CSS-first `@theme` so semantic utilities like `bg-primary` are generated. Severity: Medium.
- Do: `@theme { --color-primary: oklch(...) }`, then use `bg-primary` / `text-primary`.
- Don't: use arbitrary CSS-variable utilities for registered tokens, or repeat raw palette utilities in components.
- Use `@utility` for reusable custom utilities (e.g. `content-auto` → `content-visibility: auto`); use arbitrary values (`w-[350px]`) only for genuine one-offs.

## 983. Utility Color, Opacity and Gradients
- Rule: use modern color syntax. Severity: Low–Medium.
- Do: opacity modifiers `bg-black/50`, `text-white/80`; gradients `bg-linear-to-r from-… to-…`; dark variants `dark:bg-gray-900 dark:text-white`.
- Don't: use separate opacity classes, or the deprecated `bg-gradient-to-*`.

## 984. Content Width and Page Gutters
- Rule: cap readable content width and scale side padding with the viewport. Severity: Medium.
- Values: `max-w-7xl mx-auto`; padding `px-4 sm:px-6 lg:px-8`.
- Don't: run content full width on large screens, or use the same padding at every size.

## 985. Mobile-First Breakpoints
- Rule: base classes target mobile and breakpoint prefixes add larger layouts. Severity: Medium–High.
- Do: `text-sm md:text-base`, `w-full md:w-1/2`, `w-full md:max-w-xl`; toggle visibility with `hidden md:block` / `hidden md:flex`.
- Don't: build desktop-first, use a fixed desktop width at every viewport, or serve different content per breakpoint.

## 986. Container Queries
- Rule: components that live in containers of different widths respond to the container, not the viewport. Severity: Medium.
- Do: `@container` with `@lg:grid-cols-2`; use container-size queries when both dimensions matter.
- Don't: install the retired container-query plugin.

## 987. Grid, Flex and Sizing Utilities
- Rule: space items with container gaps and align with flex utilities. Severity: Low–Medium.
- Values: `gap-4`/`gap-6`/`gap-8`, `space-y-4`, `items-center justify-between`, `shrink-0`, `size-*` for squares (`size-6`).
- Don't: put margins on individual items, nest wrappers just to align, or use the old `flex-shrink-0` / separate `h-*` `w-*` for squares.

## 988. Stacking Order
- Rule: z-index uses a documented scale. Severity: Medium–High.
- Values: `z-0 z-10 z-20 z-30 z-40 z-50`; fixed nav and modals `fixed top-0 z-50`; decorative backgrounds `-z-10`.
- Don't: use arbitrary z-index values, rely on DOM order for overlays, or give backgrounds a positive z-index.

## 989. Readable Text
- Rule: body copy is comfortable to read and headings wrap well. Severity: Medium.
- Values: body `leading-relaxed` (1.625); rich text `prose prose-lg`; headings `max-w-xl text-balance`.
- Don't: use the default tight leading for body text, write custom markdown styles, or force line breaks with `<br>` or blanket nonbreaking spaces.

## 990. Overflow-Resilient Text
- Rule: long URLs, IDs and user text must not widen or break layouts. Severity: High.
- Do: use `truncate` or `line-clamp-2`; put `wrap-anywhere` on unpredictable text and `min-w-0` on its flex parent.
- Don't: apply `break-all` globally, or leave a flex child at its intrinsic minimum width.

## 991. Chips, Badges and Compact Labels
- Rule: compact labels stay on one line, and collections wrap instead of clipping. Severity: High.
- Do: collections `flex flex-wrap gap-2`; one label `min-w-0 whitespace-nowrap truncate`; dismiss icons `shrink-0`.
- Don't: clip a fixed-height row, let text wrap inside a pill, or let the dismiss icon shrink.

## 992. Images and Media Framing
- Rule: frame images with an aspect ratio and fit mode. Severity: Medium–High.
- Do: `aspect-video` / `aspect-square` with `object-cover w-full h-full` (or `object-contain`) and `overflow-hidden rounded-lg`; inline SVG `class="size-6" width="24" height="24"`.
- Don't: stretch or distort images, or leave containers with no ratio.

## 993. Buttons
- Rule: buttons use consistent sizes and show every state. Severity: Medium–High.
- Values: `px-4 py-2 text-sm` (default) or `px-6 py-3` (large); mobile minimum `min-h-11 min-w-11`.
- Do: while loading, disable and set `aria-busy="true"`; disabled `disabled:opacity-50 disabled:cursor-not-allowed`; icon buttons get an `aria-label` or `sr-only` text.
- Don't: mix ad-hoc sizes, or leave a loading button clickable.

## 994. Form Controls
- Rule: inputs share one height and have clear focus, disabled and placeholder styles. Severity: Medium–High.
- Values: `h-10 w-full px-3`; focus `focus:ring-2 focus:ring-offset-2` (keyboard-only: `focus-visible:ring-2`); placeholder `placeholder:text-gray-400`.
- Don't: mix input heights, remove the focus outline, or use dark placeholder text.

## 995. Cards
- Rule: cards share structure and clickable cards respond to hover. Severity: Low–Medium.
- Values: `rounded-lg shadow-md p-6` (or `rounded-2xl shadow-lg p-6`); inner `space-y-4`; hover `hover:shadow-lg transition-shadow`.
- Don't: mix card styles, or give clickable cards no hover feedback.

## 996. State-Driven Styling Without JS
- Rule: style from parent or sibling state with variants, not scripts. Severity: Low.
- Do: `group-hover:*`, `peer-checked:*`, `hover:bg-gray-100 transition-colors`.
- Don't: use JavaScript for simple visual state.

## 997. Utility Motion
- Rule: use built-in animations and keep them gentle. Severity: Medium–High.
- Do: `animate-pulse`/`animate-spin`/`animate-ping`; pair `animate-bounce` with `motion-reduce:animate-none`; `transition-all duration-200`.
- Don't: write custom keyframes for simple effects, or run several unbounded bounce animations at once.

## 998. Reliable Style Generation
- Rule: class names must be complete, static strings so their styles are actually generated. Severity: High.
- Do: map variants to full tokens (`{ red: 'bg-red-500', blue: 'bg-blue-500' }`).
- Don't: build partial class names with interpolation; those styles silently never appear.
- Use `@apply` sparingly; prefer utilities in markup.

## 999. Component Library Semantic Theming
- Rule: theme through semantic OKLCH variables in `:root` and `.dark`, exposed via `@theme inline`. Severity: High.
- Do: define complete light and dark sets (e.g. `.dark { --background: oklch(0.145 0 0) }`) and `--primary` / `--primary-foreground` pairs; set chart series colors in a chart config.
- Don't: hardcode palette colors in components, leave out dark tokens, or keep legacy space-separated HSL snippets.

## 1000. Variants, Sizes and Composition
- Rule: express visual differences through variant and size props; use className only for one-off overrides. Severity: Medium.
- Do: `variant="destructive"`, `size="sm"`/`"lg"`; add new variants (e.g. `xl: h-14 px-8`); build from compound parts (Card → CardHeader → CardTitle → CardContent).
- Don't: write inline conditional class soup, edit component source for a one-off, or build one component with dozens of props.

## 1001. Choosing the Right Overlay
- Rule: each overlay type has one job. Severity: Medium–High.
- Do: Dialog for forms and details; AlertDialog with Cancel/Action for destructive confirmations; Sheet (with an explicit `side`) for navigation, filters and settings; Popover for floating contextual panels with set `align`/`side`; DropdownMenu with groups and separators for action lists; Tooltip for icon buttons and truncated text.
- Don't: use a plain Dialog for confirmations, a Dialog for side content, a Popover for action lists, or the `title` attribute as a tooltip.

## 1002. Dialog Structure and Focus
- Rule: modals have a title and description and handle focus themselves. Severity: High.
- Do: always include DialogHeader, DialogTitle and DialogDescription (or title/description props); let the component trap focus and restore it on close.
- Don't: open unlabeled modals, write custom focus handling, or override built-in ARIA.

## 1003. Library Form Primitives
- Rule: build forms from Field + Label + Control + Error primitives. Severity: High.
- Do: `Field`, `FieldLabel htmlFor`, `FieldError`; validate with a schema (Zod, Valibot, Yup, Joi); pick when validation runs (e.g. on blur and change).
- Don't: leave inputs unlabeled, render error text that isn't linked to its field, or assume every keystroke validates by default.

## 1004. Data Display Components
- Rule: tabular data uses semantic tables; large data is paginated or virtualized. Severity: Medium–High.
- Do: Table with header, body, rows and head cells; data tables with sorting, filtering and pagination; turn on virtualization once row rendering is a measured bottleneck; tree components for hierarchies; segmented progress with an explicit max.
- Don't: lay out tables with div grids, leave out thead/tbody, or render huge datasets unpaginated.

## 1005. Charts in Component Libraries
- Rule: theme charts through tokens and label every series. Severity: Low–Medium.
- Do: name each series (key + label); theme with chart variables (`--ui-chart-1` to `--ui-chart-6`); use themed tooltips; donut charts take one row per slice and one value key.
- Don't: hardcode series colors in every chart, or hand-roll SVG for basic charts.

## 1006. Toasts, Alerts and Skeletons
- Rule: transient messages are toasts, persistent messages are inline alerts, and loading content uses skeletons. Severity: Medium.
- Do: mount one toaster in the root layout; use semantic toasts (`toast.success`, `toast.error`); show inline alerts with title, description and color; size skeletons to the real content (`h-4 w-[200px]`, avatar `h-12 w-12 rounded-full`).
- Don't: put toasters on individual pages, use toasts for static messages, or use generic skeleton sizes or a spinner for content.

## 1007. App Navigation Components
- Rule: use library navigation primitives with a responsive toggle built in. Severity: Medium.
- Do: sidebar with a mobile trigger; dashboard sidebar/panel/navbar groups; tabs with a default value; accordion `type="single" collapsible` or `multiple` chosen on purpose; a grouped command palette for search; breadcrumbs from item arrays; asides that hide below `lg`.
- Don't: hand-build sidebars or tab state, or give command palettes flat, ungrouped items.

## 1008. Link vs Action Semantics
- Rule: navigation renders an anchor and actions render a button, even when they look alike. Severity: High.
- Do: style anchors with button variants; compose with `asChild` (Radix) or `render` (Base UI) and the right semantic element.
- Don't: render a button that pretends to be a link; use `href` for internal routing when the framework link (`to`) is available.

## 1009. Semantic Color Props
- Rule: color props carry meaning (`primary`, `success`, `warning`, `error`, `neutral`). Severity: Medium.
- Do: register extra semantic names (e.g. `tertiary`) and map them to palettes; define custom palettes with every shade from 50 to 950; set component default variants centrally.
- Don't: use hardcoded palette colors, define only one shade, or use `!important` overrides or guessed slot names.
- Variant set: solid, outline, soft, subtle, ghost, link. Size set: xs, sm, md, lg, xl.

## 1010. Library Motion Tokens
- Rule: retime all component motion through one easing token. Severity: Low.
- Values: `--ease-out: cubic-bezier(0.16, 1, 0.3, 1)`.
- Don't: override transition timing separately on each component.

## 1011. Auto Loading and Rejection Feedback
- Rule: async buttons and forms show loading automatically, and rejected input gets feedback. Severity: Low–Medium.
- Do: auto-loading buttons bound to the click promise; disable the form while it submits; show a toast or field error for rejected file uploads; display selection limits (e.g. checkbox max 3) in the legend.
- Don't: silently ignore files that fail `accept`, or block extra selections with no explanation.

## 1012. Color-Mode Toggles and Hydration
- Rule: theme toggles must not cause a hydration mismatch. Severity: Medium.
- Do: use the built-in color-mode button or select (system/light/dark); wrap custom toggles in a client-only boundary with a same-size placeholder.
- Don't: read the color mode directly in server-rendered markup.

## 1013. Resizable Panels
- Rule: resizable split layouts must not jump when they hydrate. Severity: High.
- Do: give the splitter a stable id; give a default size to every panel or to none; persist sizes with an auto-save id.
- Don't: mix sized and unsized panels in server-rendered output, or rebuild drag resizing and its keyboard support yourself.

## 1014. Icons and Locale
- Rule: icons follow one naming format and one collection set; locale and direction propagate from the root. Severity: Low–High.
- Do: `i-lucide-home` format; use leading/trailing icon props; override default icons (loading, close) centrally; pass the locale at the root and set `lang` and `dir` on `<html>`.
- Don't: use legacy `lucide:home` syntax, or translate built-in component strings instance by instance.

# Part 87 — Web Frameworks (React/Next/Vue/Nuxt/Svelte/Astro/Angular/Laravel)

## 1015. Semantic Markup in Components
- Rule: templates use real elements (`button`, `nav`, `main`). Severity: High.
- Do: keep ARIA bound to state (`:aria-expanded="isOpen"`); use fragments to avoid extra wrapper divs.
- Don't: make clickable divs, set static ARIA values, or use direct DOM writes (`innerHTML`) in place of template bindings.

## 1016. Modal Focus Management
- Rule: modals trap focus and return it to the trigger on close. Severity: High.
- Do: trap focus in modals and restore it to the triggering element.
- Don't: open dialogs with no focus handling.

## 1017. Accessible Framework Forms
- Rule: labels are associated, submission goes through the form, and errors render per field. Severity: High.
- Do: `htmlFor` paired with an input `id`; handle `onSubmit`; render per-field errors (e.g. `@error('field')`); refill fields with old input after a server-side failure; show errors after a field is touched.
- Don't: rely on placeholder-only labels, `onClick`-only submits, a single dump of all errors at the top, or empty fields after a failed validation.

## 1018. Pending and Optimistic UI
- Rule: show submission status and expected results while a mutation is in flight. Severity: Medium–High.
- Do: track pending state with action state hooks; read form status from a child of the form; apply optimistic updates inside an action or transition; disable controls during server round-trips (`wire:loading.attr="disabled"`).
- Don't: give no feedback during in-flight requests, or call optimistic setters outside an action.

## 1019. Input Responsiveness
- Rule: rapid typing must not stall the UI. Severity: Medium.
- Do: debounce, or defer search and filter values (`useDeferredValue`); run expensive validators on blur or submit (`updateOn: 'blur'`); use live validation only where instant feedback adds value.
- Don't: filter or validate expensively on every keystroke.

## 1020. Route Loading and Streaming
- Rule: show the route shell immediately and stream slow parts. Severity: Medium–High.
- Do: add a route-level loading UI (`loading.tsx`); wrap slow data in Suspense boundaries; use a static shell with dynamic holes; resolve route data before activation to avoid a flash of empty state; handle pending and error states on every fetch.
- Don't: wait for all data before rendering anything, ignore loading states, or fetch initial data in mount effects that cause empty flashes.

## 1021. Error Boundaries and Error Pages
- Rule: contain errors at route or section level and offer a reset. Severity: High.
- Do: route-level error UI with a reset function; local error boundaries for subtrees; clear the error and redirect to recover; keep user-facing status messages short and generic.
- Don't: let errors crash the whole app, use the global error page for local failures, or show detailed internals in error messages.

## 1022. Optimized Images
- Rule: use the framework's image component for sizing, formats and lazy loading. Severity: High.
- Do: give `width`/`height` or `fill` inside a relative parent; set `priority` only on the above-the-fold hero/LCP image; serve responsive sources and formats with picture elements; lazy-load images below the fold.
- Don't: use raw `<img>` for local or CMS images, leave out dimensions, set priority on every image, or serve one size to every screen.

## 1023. Web Font Loading
- Rule: self-host fonts with no layout shift. Severity: Medium.
- Do: use the framework's font loader; apply the font once on the root layout body; prefer one variable font file; preload critical fonts.
- Don't: use external font links, set fonts per page, or ship a separate file for each weight.

## 1024. Hydration Without Flicker
- Rule: server and client markup must match, and client-only values must not flash. Severity: High.
- Do: wrap browser-only content in client-only boundaries; set theme and client-only values with a small inline script before hydration; use class-based dark mode with a toggle that sets the class on `<html>`.
- Don't: render different content on server and client, set the theme in a mount effect (causes a flash), or use media-query-only dark mode that users cannot override.

## 1025. Client-Side Navigation and Scroll
- Rule: internal links use the framework link for instant, prefetched navigation. Severity: High.
- Do: use framework link components; set `scroll={false}` for tabs and pagination; keep layouts persistent so headers and sidebars don't remount; prefetch on interaction for low-priority links.
- Don't: use plain `<a>` for internal routes, always jump to the top on navigation, or reload the full layout on every visit.

## 1026. Islands and Deferred Hydration
- Rule: ship zero JavaScript for static content and hydrate interactive parts only when needed. Severity: High.
- Do: `client:visible` below the fold and `client:idle` for non-critical parts; defer blocks `on viewport`; lazy components and lazy hydration; lazy or non-blocking fetches for secondary data; lazy-load heavy dialogs and modals.
- Don't: put `client:load` on everything, hydrate the whole page like an SPA, or eagerly load every component.

## 1027. Progressive Enhancement
- Rule: core content and navigation work before or without JavaScript. Severity: High.
- Do: make sure basic navigation works without the client router; use server-backed form actions where submission must work before hydration.
- Don't: require client routing for basic navigation, or claim progressive enhancement for client-only actions.

## 1028. Page and Element Transitions
- Rule: transitions keep visual continuity across navigation and state changes. Severity: Low–Medium.
- Do: enable the client router in the shared head; name morphing elements (`transition:name`); persist media players across navigation (`transition:persist`); use different enter and exit transitions (`in:fly out:fade`); scope list transitions locally (`|local`).
- Don't: use the removed `<ViewTransitions />` component, re-initialize persistent media on every navigation, or let ancestor transitions trigger on list items.

## 1029. Scoped Styles and Theming
- Rule: component styles are scoped by default, and theme values cross component boundaries as CSS custom properties. Severity: Medium.
- Do: use scoped `<style>` blocks; style the host element with `:host`; use global escapes sparingly (`:global`, `is:global`, `ViewEncapsulation.None`) for base or third-party styles; use Material 3 token theming.
- Don't: make all styles global, hardcode hex values in component styles, add wrapper divs just for styling, or override library CSS with deep selectors.

## 1030. Keyed List Rendering
- Rule: lists update in place using stable keys. Severity: High.
- Do: `track item.id`, `{#each items as item (item.id)}`, a stable `key` with `v-for`.
- Don't: track by index for dynamic data, or put `v-if` on the same element as `v-for`.
- Server-rendered views paginate large datasets and render pagination links; never render an entire large table in one response. Severity: High.

## 1031. Local UI State Without Round-Trips
- Rule: purely visual toggles (dropdowns, tooltips) use client-side state, not server calls. Severity: Medium.
- Do: lightweight client directives (`x-data`, `x-show`, `x-transition`); lazy-load heavy server components when they become visible.
- Don't: make server round-trips just to toggle visibility.

## 1032. Social Previews and Head Metadata
- Rule: every shareable page has a title, description, canonical URL and Open Graph image. Severity: Medium.
- Do: generate metadata per route; include `ogTitle`, `ogDescription` and `ogImage`; centralize head tags in a shared component.
- Don't: leave pages with missing social preview images or no metadata.

# Part 88 — Mobile (React Native, Flutter, SwiftUI, Jetpack Compose)

## 1033. React Native Styling and Platform Fit
- Rule: define styles with the platform style system and lay out with flexbox. Severity: Medium–High.
- Do: `StyleSheet.create`; `flexDirection`/`alignItems`/`justifyContent`; branch per platform with `Platform.select` or `.ios`/`.android` files; read sizes from `useWindowDimensions`.
- Don't: create inline style objects in render, position everything absolutely, use identical styles on both platforms, or use fixed pixel sizes for screen-dependent layout.

## 1034. React Native Lists
- Rule: long lists are virtualized and cheap to render. Severity: High.
- Values: use FlatList from about 50 items.
- Do: `keyExtractor` with stable IDs; memoize row components; `getItemLayout` for fixed-height rows; a smaller `windowSize` for memory on large lists.
- Don't: render a ScrollView with `.map`, key by index, or pass an inline render function.

## 1035. Touch Feedback and Hit Areas
- Rule: every touchable responds visibly and has a large enough hit area. Severity: Medium.
- Do: `Pressable` with ripple or opacity feedback; `hitSlop` on icons and small buttons.
- Don't: use touch targets with no feedback, or tiny targets.

## 1036. Keyboard-Aware Forms
- Rule: the software keyboard never hides the focused input, and the keyboard type matches the field. Severity: High.
- Do: `KeyboardAvoidingView`; set `keyboardType` per input (email, numeric, phone); in SwiftUI, manage focus with `@FocusState`.
- Don't: let content sit hidden behind the keyboard, or show the default keyboard for every field.

## 1037. Mobile Image Handling
- Rule: remote images have dimensions, a fit mode and caching. Severity: Medium–High.
- Do: give `width`/`height` for network images; set `resizeMode` to `cover` or `contain`; use a cached, performant image component (with blur placeholders) in heavy lists.
- Don't: show network images with no dimensions, or stretch images.

## 1038. Native-Thread Animation and Gestures
- Rule: animations and gestures run on the UI thread. Severity: High.
- Do: use worklet-based animation (Reanimated) and native gesture recognition.
- Don't: drive complex animations or gesture tracking from the JS thread.

## 1039. Android Back and Predictive Back
- Rule: handle the system back gesture deliberately on every screen. Severity: High.
- Do: back handling tied to screen focus (RN `useFocusEffect` + `BackHandler`); Flutter `PopScope` with `onPopInvokedWithResult` for predictive back (Android 14+).
- Don't: ignore the back button, or use the deprecated `WillPopScope`.

## 1040. Flutter Layout Widgets
- Rule: compose layouts from linear and flex widgets and adapt to constraints. Severity: Medium.
- Do: `Column`/`Row`; `Expanded`/`Flexible` to fill space; `SizedBox` for gaps; `LayoutBuilder` for adaptive layouts; slivers in a `CustomScrollView` for custom scroll effects.
- Don't: use `Stack` for simple linear layouts, fixed sizes inside flex containers, `Container` only for spacing, nested ListViews, or 10+ levels of nesting.

## 1041. Flutter Theming
- Rule: the app theme comes from `ThemeData` with a Material 3 `ColorScheme`, light and dark. Severity: Medium.
- Do: read values from `Theme.of(context)`; set `darkTheme` on the app.
- Don't: hardcode colors, set individual color properties outside the scheme, or ship a light theme only.

## 1042. Flutter Lists and Rebuild Scope
- Rule: build lists lazily and keep rebuilds small. Severity: High.
- Do: `ListView.builder`; `itemExtent` for uniform rows; keys on stateful items; `const` widgets; isolate changing widgets; `RepaintBoundary` around animations.
- Don't: build large lists from a children array, call `setState` on a high-level parent, or repaint the full screen.

## 1043. Flutter Motion
- Rule: use implicit animations for simple changes and controllers for sequences. Severity: Low–Medium.
- Do: `AnimatedContainer`/`AnimatedOpacity`; `AnimationController` for complex sequences; `Hero` for shared-element navigation.
- Don't: hand-build shared-element transitions.

## 1044. Async UI States
- Rule: async-built UI covers loading, error and empty states as well as success. Severity: High.
- Do: check `ConnectionState` in Future/Stream builders; `ProgressView` (SwiftUI); `ActivityIndicator` (RN); model Compose state as a sealed type (`UiState.Loading`, …).
- Don't: render only the success state, show an empty screen while loading, or represent state with loose boolean flags.

## 1045. Mobile Accessibility Semantics
- Rule: every meaningful element exposes a label and role to the screen reader. Severity: High.
- Do: `accessibilityLabel` + `accessibilityRole` (RN); `Semantics` (Flutter); `.accessibilityLabel` + correct traits (SwiftUI); `contentDescription` + `Modifier.semantics` (Compose).
- Don't: leave elements unlabeled, or assign the wrong role.

## 1046. SwiftUI Layout and Modifier Order
- Rule: lay out with stacks, and remember that modifier order changes rendering. Severity: High.
- Do: `VStack`/`HStack`/`ZStack`; lazy stacks for 100+ items; `.frame(maxWidth: .infinity)` for flexible width; put the background before the padding when it should cover the padding; use design-system spacing values; make repeated styling a `ViewModifier`.
- Don't: use `GeometryReader` for simple layouts, magic-number spacing, or conditionals that change a view's identity.

## 1047. SwiftUI Navigation and Lists
- Rule: use current navigation containers and built-in list editing. Severity: Medium.
- Do: `NavigationStack` for single-column, `NavigationSplitView` for two or three columns; `.navigationDestination(for:)`; `List` with `onDelete`/`onMove`; `Form` for settings screens.
- Don't: use `NavigationView` in new code, build custom swipe-to-delete, or hand-group settings rows.

## 1048. SwiftUI Motion and Dynamic Type
- Rule: animate state changes and respect accessibility settings. Severity: High.
- Do: `withAnimation` / `.animation(.spring())`; check `accessibilityReduceMotion`; use scalable fonts and layouts.
- Don't: use fixed font sizes, or ignore motion preferences.

## 1049. Compose Layout
- Rule: keep layouts flat and state layout intent with modifiers, arrangement and alignment. Severity: High.
- Do: `Modifier.padding()` instead of wrapper boxes; `Row`/`Column` for linear content; `Box` only for overlapping content; `Arrangement`/`Alignment`; shared layout composables.
- Don't: nest Box → Column → Box → Row, apply `fillMaxSize` everywhere, use intrinsic sizing unless necessary, or hack spacing manually.

## 1050. Compose Scrolling
- Rule: one virtualized scroll container per axis. Severity: High.
- Do: `LazyColumn` with `key = id`.
- Don't: use `Column.verticalScroll()` for long content, or nest scroll containers.

## 1051. Compose Theming and Typography
- Rule: all values come from Material 3 tokens. Severity: Medium–High.
- Do: `MaterialTheme.colorScheme` and `MaterialTheme.typography`.
- Don't: hardcode colors or `sp` text sizes.

## 1052. Compose State That Survives
- Rule: UI state survives configuration changes, and expensive objects are remembered. Severity: High.
- Do: `rememberSaveable` for user-visible state; `remember` for scroll and animation state; `derivedStateOf` to limit recomposition; collect state with lifecycle awareness.
- Don't: use plain `remember` for state that should survive rotation, or recompute derived values on every recomposition.

## 1053. Compose Motion
- Rule: animation is a UI concern and uses the built-in animation APIs. Severity: Low–Medium.
- Do: `AnimatedVisibility` and `animate*AsState`.
- Don't: write manual animation loops, or put animation logic in the view model.

# Part 89 — Desktop (WPF/UWP/WinUI/Avalonia/Uno/JavaFX)

## 1054. Desktop Layout Panels
- Rule: choose panels by role. Severity: Medium–High.
- Do: Grid with row and column definitions for complex layouts and forms; StackPanel/VBox/HBox for toolbars and simple stacks; DockPanel or BorderPane for the app shell (menu on top, sidebar on the left, last child fills); GridPane for forms; RelativePanel for layouts that reflow.
- Don't: use Canvas or absolute positions for forms, nest StackPanels to fake docking, or hack alignment with margins instead of attached properties.

## 1055. Desktop Sizing and Overflow
- Rule: content resizes predictably at any window size and DPI. Severity: Medium–High.
- Do: star (`*`) and `Auto` sizing; MinWidth/MaxWidth; computed sizes; grow priorities and column constraints; ScrollViewer around long forms.
- Don't: use fixed pixel widths on resizable content, or clip content with no scroll.

## 1056. Centralized Styles and Resources
- Rule: themes live in shared, merged resource dictionaries. Severity: Medium.
- Do: put shared styles and brushes in app-level merged dictionaries; set default looks with implicit styles (TargetType, no key); build keyed variants with `BasedOn`; use style classes in CSS-based toolkits; split styles into modular files.
- Don't: put inline colors and font sizes on each element, redefine brushes on every page, or repeat setters across variants.

## 1057. Theme Resources for Light, Dark and Contrast
- Rule: theme-aware colors resolve through theme dictionaries keyed Light, Dark and HighContrast. Severity: High.
- Do: use ThemeResource for adaptive colors (WinUI/UWP/Uno); use DynamicResource for brushes that follow the active variant (Avalonia); use system colors for high contrast (WPF); follow the OS theme by leaving the app's requested theme unset, and set Light or Dark only after the user chooses an override.
- Don't: hardcode hex values that break in dark mode, use StaticResource for values that should follow the theme, or define one root brush with no dark or high-contrast variant.
- Prefer static resources for values that never change at runtime, and freeze brushes that never change.

## 1058. Lightweight Styling Before Templates
- Rule: change control sub-properties by overriding resource keys; replace the whole template only when necessary. Severity: Medium–High.
- Do: lightweight resource overrides for small tweaks; a full control template when the built-in look really isn't enough; data templates for item presentation.
- Don't: copy a full template for a color change, nest panels to hide the default template, or rely on `ToString` for display.

## 1059. Fluent Design Materials
- Rule: use the platform's materials and choose them by how long a surface lives. Severity: Medium.
- Do: Mica on long-lived main window backgrounds and Acrylic on transient flyouts and overlays; set the system backdrop directly on the window; use the Fluent theme mode on .NET 9+ (Light, Dark, System); use built-in rounded corners and depth.
- Don't: put Acrylic on the main window or Mica on flyouts, hand-roll blur and shadow effects, or use legacy Aero styling in new Windows 11 apps.

## 1060. Selector-Based Styling and States
- Rule: in CSS-like XAML toolkits, style states with pseudoclasses and scoped selectors. Severity: Medium–High.
- Do: `:pointerover`, `:pressed`, `:focus`; `>` for direct children and a space for descendants; start from the Fluent or Simple base theme.
- Don't: use WPF-style implicit TargetType styles or triggers there, write overly broad selectors, or build a theme from scratch.
- In visual-state toolkits, define states with VisualStateManager setters instead of toggling visibility from code-behind.

## 1061. Adaptive Window Layouts
- Rule: layout adapts at standard window-width breakpoints and per form factor. Severity: High.
- Values: adaptive triggers at 640 (small) and 1008 (large) epx `MinWindowWidth`.
- Do: put adaptive triggers inside visual states; use per-platform and per-form-factor values in markup; design for phone, tablet, desktop and console where relevant.
- Don't: use fixed single-size layouts, or set XAML properties from OS checks in code-behind.

## 1062. App Shell and Command Surfaces
- Rule: top-level navigation and commands use the standard shell controls. Severity: Medium–High.
- Do: NavigationView (Left, Top or LeftCompact, with footer items); CommandBar with app bar buttons; BreadcrumbBar for hierarchies; SplitView for master-detail; TabControl for tabs; a native menu bar on macOS; a shell with a stable navigation toolbar and a central workspace.
- Don't: build custom hamburger menus or StackPanel toolbars, or replace the whole window for every feature.

## 1063. Desktop Back Navigation
- Rule: provide an in-app back affordance tied to a real back stack. Severity: Medium–High.
- Do: an in-app back button styled like the system one plus the platform back-request handler; navigation-view back events in WinUI; a router back stack in other toolkits.
- Don't: use the deprecated title-bar back button, ignore system back signals, or leave users with no way back to the previous view.

## 1064. Native Desktop Controls
- Rule: standard needs map to built-in controls. Severity: Low–Medium.
- Do: InfoBar for success, warning and error status; TeachingTip for feature discovery; ContentDialog for modals; NumberBox with min/max and spin buttons for numbers; Expander for collapsible settings groups; ProgressRing (indeterminate) and ProgressBar (determinate); AutoSuggestBox/AutoCompleteBox for search; ToggleSwitch for on/off settings; built-in date and time pickers; avatar controls with fallback initials; Flyout/MenuFlyout for contextual actions; a system tray icon with a native menu.
- Don't: build custom status panels, overlay panels as dialogs, parse numbers by hand, use checkboxes for settings toggles, draw text-based loading indicators, or fake a tray icon with a borderless window.

## 1065. Command-Driven Enabled State
- Rule: actions are commands whose availability drives the enabled state, and async commands block re-entry. Severity: Medium–High.
- Do: CanExecute returning false to disable buttons, re-evaluated when inputs change; async relay commands that disable themselves while running and support cancellation; command parameters for item-specific actions.
- Don't: bind IsEnabled to a separate flag, use `async void` click handlers, or fire-and-forget background work from a button click.

## 1066. Desktop Keyboard Shortcuts
- Rule: frequent actions have keyboard accelerators bound to commands. Severity: Medium–High.
- Do: input or key bindings on the window; keyboard accelerators with modifiers; hotkeys on command sources; scene-level filters; mnemonics with unique letters; access keys; XY focus for gamepads.
- Don't: write manual KeyDown handlers that swallow shortcuts, or add duplicate key handlers on every control.

## 1067. Desktop Screen-Reader Support
- Rule: every interactive control has an automation name, and section headers declare a heading level. Severity: High.
- Do: `AutomationProperties.Name`; `AutomationProperties.HeadingLevel`; label-for links on form fields; accessible text plus a tooltip on icon buttons; test with Narrator and Accessibility Insights.
- Don't: ship controls without names, use the same level for all text, or skip accessibility testing.

## 1068. DPI and Crisp Rendering
- Rule: the UI stays sharp at every display scale. Severity: Medium.
- Do: device-independent units and vector graphics; per-monitor DPI awareness (PerMonitorV2); choose bitmap interpolation for scaled images; generate multi-resolution assets from a single SVG source.
- Don't: use pixel bitmaps that blur at high DPI, keep the default system-DPI awareness on Windows 10/11, or accept blurry or aliased scaled images.

## 1069. Custom Title Bars
- Rule: extend content into the title bar through the platform API, keeping system caption buttons and drag regions. Severity: Medium.
- Do: extend content into the title bar and register the custom title element or region.
- Don't: hardcode chrome height, build custom caption buttons that break with theme or size changes, or remove decorations and drag the window by hand.

## 1070. Desktop UI Thread Responsiveness
- Rule: never freeze the window. Severity: High.
- Do: async/await for I/O; background tasks for CPU work; marshal back through the UI dispatcher or queue; report progress with progress objects bound to progress bars and labels.
- Don't: run synchronous I/O on the UI thread, poll shared variables for progress, or block on tasks from the UI thread (deadlock).

## 1071. Large Desktop Lists
- Rule: item controls virtualize and render progressively. Severity: High.
- Do: keep default virtualization (enable it explicitly on tree views); incremental loading as the user scrolls; render secondary template content in later phases (`x:Phase`); defer rarely shown UI (`x:Load=False`); use compiled bindings in item templates; keep templates flat; apply list changes in bulk (`setAll`/`addAll`).
- Don't: swap in non-virtualizing item panels, load whole datasets up front, nest panels deeply in item templates, or add rows one at a time to a visible list.

## 1072. Desktop Transitions
- Rule: navigation keeps visual continuity with short, purposeful motion. Severity: Low–Medium.
- Values: 150–250ms for reveal, hover and selection.
- Do: connected (shared-element) animations between pages; crossfade or slide page transitions; implicit property transitions; a setting to turn off decorative animation.
- Don't: swap content abruptly, drive property animations with timers, or animate every layout change with long timelines.

## 1073. High-Density Enterprise Tables
- Rule: data-heavy screens use dense, sortable, filterable tables, not cards. Severity: High.
- Do: compact row height, clear columns, sorting, filtering and a selection summary; secondary row actions in context menus or a side detail panel; server-side paging; placeholders for empty tables; badges and row styles that show workflow state; disable actions by state.
- Don't: use card grids for large datasets, put many buttons in every row, load all records and filter in the UI, or show status only as free text.

## 1074. Enterprise Forms
- Rule: long forms are split into titled sections with inline errors plus a summary. Severity: Medium–High.
- Do: section grouping and progressive disclosure; error labels or pseudo-classes next to invalid fields; input formatters for numbers, dates and masks; modal dialogs with an owner that return structured results.
- Don't: put dozens of inputs in one unbroken grid, show one alert after Save, reject input only after submit, or open unmanaged windows for confirmations.

## 1075. Long-Running Operations
- Rule: imports, exports, syncs and reports show progress and can be cancelled. Severity: High.
- Do: a cancel button bound to the task's running state; inline retry messages that keep user input.
- Don't: force users to wait or kill the app, or clear the screen when something fails.

## 1076. Toolkit Themes and Icons
- Rule: start from a maintained modern theme and add a thin brand layer on top. Severity: Medium–High.
- Do: a neutral enterprise light/dark theme pair as the base; brand CSS added after the base; semantic tokens (`app-primary`, `app-success`, `app-warning`, `app-danger`) as looked-up colors; documented style classes before custom ones; a consistent icon font with semantic classes.
- Don't: edit the base theme's source CSS, make playful themes the enterprise default, create one-off classes for every button variant, use emoji as toolbar or menu icons, or apply blur, drop shadow and glow to every node (keep subtle shadows for elevated surfaces).
- A theme alone is not a design system; shell, navigation, table density and validation rules still need defining.

## 1077. Role-Aware Navigation
- Rule: menus, toolbars and shortcuts all follow the same permission model. Severity: High.
- Do: build navigation items from commands that declare their required roles.
- Don't: hide a button in one place while its shortcut still works.

## 1078. State Continuity Across Lifecycle
- Rule: users keep their place across suspend, close and restart. Severity: Medium–High.
- Do: save state on suspend (async saves get a deferral, about 5 seconds); persist on window close for desktop targets that never suspend; restore window and UI state on launch; swap center content instead of rebuilding the scene.
- Don't: ignore lifecycle events and lose user state, or rebuild the whole window on every navigation click.

## 1079. Startup Experience
- Rule: never show a blank window while the runtime starts. Severity: Medium.
- Do: show a branded splash overlay until the first view renders (especially for WebAssembly targets); load large images in the background.
- Don't: leave users on a blank white page, or decode many full-size images synchronously at startup.

## 1080. Localized UI Text
- Rule: all user-facing strings come from resource files per language. Severity: High.
- Do: resource IDs (`x:Uid`) on every user-facing string.
- Don't: hardcode language-specific text in markup or code.

## 1081. Cross-Platform Rendering Parity
- Rule: confirm visual output on every renderer and OS. Severity: High.
- Do: choose a Skia renderer for pixel-perfect consistency; check that an API is implemented on each platform before using it; test themes and rendering on every active target.
- Don't: assume native rendering everywhere, or assume Windows output matches other platforms.

# Part 90 — 3D & WebGL (three.js)

## 1082. Renderer Setup and Page Compositing
- Rule: use one renderer per page, and let the canvas blend into the surrounding HTML. Severity: Critical.
- Do: reuse a single WebGL renderer and swap scene content; set `alpha: true` and let CSS on the parent provide the background.
- Don't: create a renderer on every mount or scene change (browsers allow only about 8–16 GPU contexts), or set a solid clear color when HTML must show behind the canvas.

## 1083. Pixel Ratio and Antialiasing
- Rule: cap the pixel ratio and set antialiasing when the renderer is created. Severity: High.
- Values: `Math.min(window.devicePixelRatio, 2)`; going from 2x to 3x multiplies pixel count by 2.25 with no visible gain.
- Do: pass `antialias: true` in the constructor options.
- Don't: pass the raw device pixel ratio, or try to enable antialiasing after construction (it has no effect).

## 1084. Camera Framing
- Rule: frame the subject on purpose before the first render. Severity: Medium.
- Values: FOV 45–75; 75 for general interactive scenes, 45–55 for product close-ups; avoid above 90 (fisheye) or below 30 without an artistic reason.
- Do: set the camera position and `lookAt` explicitly.
- Don't: leave the camera at the origin with no target, where the subject may sit behind the camera or look microscopic.

## 1085. Camera Control Model
- Rule: match camera control to the experience. Severity: High.
- Do: orbit controls for model viewers and free exploration; a scripted, scroll-driven camera rig for product reveals; if orbit controls aren't available, rotate in spherical coordinates so both drag axes respond.
- Don't: allow free orbit during a scripted reveal (users can orbit away before it finishes), or move only `camera.position.x` (vertical drag is silently ignored).

## 1086. Responsive Canvas
- Rule: size the canvas from its container and keep the aspect ratio correct. Severity: High.
- Do: size from the canvas's `clientWidth`/`clientHeight`; watch the container with a ResizeObserver; update `camera.aspect` and call `updateProjectionMatrix()` on every resize; handle touch events alongside mouse and normalize the coordinates.
- Don't: size to the window when the canvas sits in a container, let the aspect ratio go stale (the scene stretches), or leave touch users with no interaction.

## 1087. Lighting and Shadows
- Rule: lit materials need at least ambient fill plus a directional key light, and shadows are selective. Severity: Critical–High.
- Do: an ambient light plus a directional light for standard and Phong materials; enable the shadow map before setting any cast or receive flags; cast shadows only from the key light and the most important meshes; drop lights entirely when every material is unlit.
- Don't: use standard materials with no lights (the scene renders black), set cast-shadow flags without enabling the shadow map (no shadows appear), or turn shadows on for every object including particles.

## 1088. Materials and Color Management
- Rule: choose material cost by need, share instances, and keep color management on. Severity: Medium–High.
- Do: unlit basic material for HUDs, overlays and flat decorative objects; standard material for physical objects; one shared material for identical meshes; default color management with an sRGB output color space and suitable tone mapping; set `transparent: true` before tweening opacity.
- Don't: light flat UI elements, create a new material per mesh in loops, or disable color management or use removed encoding properties.

## 1089. Geometry Budget
- Rule: spend triangles where users look. Severity: Medium–Critical.
- Values: hero objects 32–64 segments; background objects 8–16.
- Do: build all geometry before the animation loop and share one geometry across meshes; use level-of-detail swaps for distant objects; add exponential fog when view distance exceeds 100 units, for atmosphere and implicit far culling.
- Don't: construct geometry inside the frame loop (VRAM runs out within seconds), or give every sphere 64+ segments.

## 1090. Instancing and Particles
- Rule: repeated objects and particles render in single draw calls. Severity: High–Critical.
- Values: instanced meshes from 50+ identical objects; start particle systems at 1000–3000 (default 3000); above 50,000 causes sustained frame drops on mid-range phones.
- Do: build particles as points on buffer geometry with typed arrays; set `needsUpdate = true` after every per-frame buffer change; profile on real mobile hardware before raising counts.
- Don't: use hundreds of separate meshes as particles, start at 100,000+ particles, or mutate buffers without flagging them (positions never update on screen).

## 1091. Frame Loop and Timing
- Rule: rendering runs on the display's frame clock with delta-time motion and pauses when hidden. Severity: Critical–High.
- Do: drive rendering only with `requestAnimationFrame` or `setAnimationLoop`; update the timer once per frame and reuse the delta; pass `null` to the loop on `visibilitychange` to pause in hidden tabs.
- Don't: render on `setInterval`/`setTimeout`, use the deprecated Clock, update the timer more than once per frame, or keep rendering in hidden tabs.

## 1092. Smooth Motion and Sequencing
- Rule: pointer-follow motion eases, and multi-step motion uses timelines. Severity: Medium–High.
- Values: lerp `value += (target - value) * alpha` with alpha 0.03–0.1; scroll scrub `scrub: 1` (1-second cinematic lag).
- Do: timelines for any sequence of more than two steps and for scroll-linked camera paths; tween object properties directly.
- Don't: snap straight to the target, juggle boolean flags and frame counters for sequences, or move the camera from enter/leave callbacks (it snaps instead of scrubbing).

## 1093. Pointer Picking and Hover Feedback
- Rule: picking is correct, cheap, and shows feedback. Severity: Critical–Medium.
- Do: create one shared raycaster; store the pointer position in `pointermove`; convert to normalized device coordinates with Y negated (X from -1 to +1 left to right, Y from +1 to -1 top to bottom); set the ray from the camera before intersecting, inside the frame loop; pass the recursive flag for groups and loaded models; switch the cursor to `pointer` on hit and back to `auto` on miss.
- Don't: create raycasters in mouse handlers, forget the Y negation (hits come out mirrored), intersect a stale ray, or give no hover cue.

## 1094. 3D Accessibility and Motion Safety
- Rule: the canvas has a text alternative, and auto-motion follows the user's preference live. Severity: High–Medium.
- Do: `role="img"` and a descriptive `aria-label` on the canvas; gate auto-rotation, particles and camera drift on a live `prefers-reduced-motion` listener.
- Don't: ship a canvas screen readers can't see, or read the preference only once at startup.

## 1095. GPU Resource Cleanup
- Rule: free GPU memory when objects leave the scene so performance holds over time. Severity: Critical–High.
- Do: dispose of geometry, material and every texture map before removing an object; track loaded textures and dispose of them on teardown; traverse loaded models to set shadow and material options on each child mesh.
- Don't: remove objects without disposing of them, or load textures with no cleanup path.

# Part 91 — React Rendering Performance

## 1096. Eliminate Async Waterfalls
- Rule: independent data loads run in parallel and start as early as possible. Severity: Critical.
- Do: run independent awaits together with `Promise.all`; start promises early and await them late; move awaits into the branches that need them; compose server components so sibling fetches run in parallel.
- Don't: await sequentially when calls don't depend on each other, await at the top of a function and block every branch, or chain fetches in a parent component.

## 1097. Stream the Shell First
- Rule: show surrounding UI immediately and stream slow data in. Severity: High.
- Do: wrap async components in Suspense boundaries.
- Don't: hold the whole page render for data.

## 1098. First-Load Bundle Weight
- Rule: ship only what the first view needs. Severity: Critical–Medium.
- Do: import from source paths instead of barrel files; dynamically import heavy components; load feature-only modules when the feature turns on; load analytics and logging after hydration.
- Don't: import from barrel/index files, import heavy components at the top level, or put analytics in the main bundle.

## 1099. Intent-Based Preloading
- Rule: start loading heavy chunks when users signal intent. Severity: Medium.
- Do: preload on hover or focus.
- Don't: wait for the click to start loading.

## 1100. Lean Server-to-Client Payloads
- Rule: send only the fields the client renders, and never re-fetch the same data. Severity: High.
- Do: pass only the fields client components need; dedupe server requests per render; cache data shared across requests; schedule logging and analytics after the response is sent.
- Don't: pass whole objects across the boundary, or block the response on non-critical work.

## 1101. Client Data Deduplication
- Rule: client fetches are cached and deduplicated, and global listeners are shared. Severity: Medium–Low.
- Do: use a stale-while-revalidate data hook; use a shared subscription for global listeners.
- Don't: fetch manually in effects, or register one listener per component instance.

## 1102. Narrow Re-render Scope
- Rule: components subscribe only to the state they render. Severity: Medium.
- Do: read state on demand inside callbacks; subscribe to derived booleans, not continuous values; use primitive effect dependencies; use functional `setState(curr => …)`; initialize expensive state lazily; move expensive work into memoized components that can return early.
- Don't: subscribe to state used only in handlers, depend on object references, or compute expensive values before an early return.

## 1103. Non-Urgent Updates
- Rule: frequent, non-urgent updates must not block input. Severity: Medium.
- Do: mark them as transitions (`startTransition`).
- Don't: block the UI on every state change.

## 1104. Memoization Policy
- Rule: let the compiler memoize first; add manual memoization only where profiling shows a real cost. Severity: High–Low.
- Do: profile before optimizing; use `useMemo`, `useCallback` or `memo` where profiling proves a bottleneck; memoize context values; hoist static JSX and RegExps to module scope.
- Don't: wrap everything in memo hooks by default, create inline objects in hot props, or pass a new context object on every render.

## 1105. Off-Screen and Toggled Content
- Rule: skip rendering what isn't visible, and keep expensive toggled views mounted. Severity: High–Medium.
- Do: `content-visibility: auto` on long lists; an Activity boundary to keep state and DOM for components that toggle.
- Don't: render every list item immediately, or unmount and remount expensive panels on each toggle.

## 1106. Flicker-Free Client Values
- Rule: client-only values (theme, locale prefs) apply before hydration. Severity: Medium.
- Do: inject a small synchronous inline script.
- Don't: set them in an effect, which causes a visible flash.

## 1107. DOM and Animation Efficiency
- Rule: minimize reflows and animate on GPU-friendly layers. Severity: Medium–Low.
- Do: batch style changes through class toggles or `cssText`; animate a wrapper div around an SVG, not the SVG itself.
- Don't: change styles one property at a time, or animate SVG elements directly.
- Conditional rendering: use an explicit ternary when the condition may be `0` or `NaN`; `&&` with a falsy number renders a stray `0`. Severity: Low.

## 1108. Hot-Path JavaScript
- Rule: work that runs on every render or interaction stays cheap. Severity: Medium–Low.
- Do: use Map/Set for repeated lookups; cache property access and storage reads; combine iterations into one loop; check lengths first and return early; find min/max in one loop instead of sorting; use `toSorted()` to avoid mutating.
- Don't: call `.find()` or `.includes()` in loops, chain multiple filters, read storage on every call, or sort to find extremes.
