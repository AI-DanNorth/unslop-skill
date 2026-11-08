# Motion Design Rules by Concept

Distilled from the transitions.dev UI-motion collection. Each concept is followed by its rules; exact values are kept wherever the source gives them.

# Part 1 — Motion philosophy & principles

## 1. Usage over nearest number
- Infer what a motion does first (modal close, dropdown open, tooltip, badge appear, page slide, text reveal, shake, hover lift), then pick the value whose documented usage matches.
- A value is not wrong for being 20ms off; it is wrong when it does not fit its usage.
- A `300ms` modal close maps to the `150ms` quick token because both are "modal close", not because the numbers are close.
- If a value's usage matches no token usage, leave it untouched and label it "no matching token usage"; never force a swap because a number is close.
- For keyframe-driven motion, judge the duration and easing of the animation that drives the keyframes.

## 2. One shared motion scale
- Keep one shared scale of durations, easings, distances, scales and blurs, and reference it everywhere instead of ad-hoc values.
- Scripted orchestration reads its durations from the same shared tokens so script timing stays in sync with the stylesheet.
- Plain CSS transitions and keyframes plus small orchestration are sufficient; no motion library is needed.

## 3. Prefer the lightest motion that fits
- When two motions could fit, choose the lower-overhead one: card resize over panel reveal, dropdown over modal, success check over a full modal celebration.
- Choose the heavier surface only when the design clearly calls for it.
- Treat the success check as animation-only; pair it with the icon swap when you also need to go from a spinner to the check.

## 4. Animate the pieces, not the container
- Animate the badge dot, not the trigger; animate the page sections, not the page container.
- Split content into semantic chunks and stagger them instead of animating a single wrapper.

## 5. Name exact properties
- Never use `transition: all`; enumerate the animated properties (e.g. `transform, opacity, filter`) so unrelated style changes do not animate for free.
- A hover transition must cover every property the hover changes, or that property snaps.

## 6. Every motion has an exit and a reduced-motion fallback
- Overlays and components must animate out; never pop out or unmount instantly.
- Every motion ships a `prefers-reduced-motion: reduce` fallback that keeps the final state visible.

## 7. Cross-blur as the house signature
- Pair blur with opacity ("cross-blur") so short travels read as full opens and swaps feel resolved.
- Use blur to soften a swap or slide; never on a plain fade or a color/theme change.

## 8. Clean state hygiene
- After a close animation, remove the closing state after the close duration so the next open starts from the resting pre-open scale, not the closing scale.
- To replay a keyframe or entrance: remove the state, force a reflow, re-add the state.
- Keep orthogonal states separate (error state vs shake state) so one can replay without flickering the other.
- Write the first position of measured indicators (tabs pill) with transitions suspended, or they animate in from zero.

# Part 2 — Motion tokens

## 9. Duration tokens
- `40ms` stagger: per-item stagger offset.
- `80ms` micro: tooltip appear delay, success-check path delay, a shake segment, stagger for a few large items.
- `150ms` quick: modal close, dropdown close, text swap, tooltip appear, fills.
- `250ms` fast: icon swap, dropdown open, modal open, tabs sliding, page slide.
- `350ms` medium: panel close, toast close (toast open in its recipe), morph open, like pop.
- `400ms` slow: panel open, skeleton content reveal, input clear.
- `500ms` very slow: emphasis moments, badge appear, text reveal, success check.
- Longer one-offs: `600ms` particles, `1000ms` tilt return and input-clear total, `1400ms` reel spin, `2000ms` shimmer and status holds.
- Design-system shorthand: `150ms` small feedback; `250ms` menus and toggles; `350–400ms` panels and modals; `500ms` large reveals.
- Any transition over 1 second is too slow for UI chrome (ambient loops and one-off returns excepted).

## 10. Easing tokens
- `cubic-bezier(0.22, 1, 0.36, 1)` smooth-out: the house default (ease-out-quint feel); modal, dropdown and panel open and close, page slide, resize, any position change, follows, indicators, stroke draws, cross-blurs, returns.
- `ease-in-out`: symmetric in-place cross-fades (icon swap, text swap, text reveal, skeleton reveal, thinking swaps, matrix loader).
- `ease-out`: tooltip open and close.
- `linear`: continuous loops (shimmer, skeleton pulse, spinners).
- `cubic-bezier(0.4, 0, 0.2, 1)`: standard ease with no overshoot, for a badge closing.
- `cubic-bezier(0.16, 1, 0.3, 1)`: very long-tail decelerating spins (counter reels) and generation drawing.
- Nudge generic `ease`, `ease-in` or hand-rolled curves toward smooth-out only for surface motion (open/close, slide, resize, position); leave the other token easings untouched, each carries its own intent.
- Never use `linear` on surfaces or `ease-in` on hover.

## 11. Overshoot / spring curve family
- Family shape `cubic-bezier(0.34, Y, 0.64, 1)`; Y controls bounce strength.
- Y `1.25`: plus-to-menu morph open (gentle).
- Y `1.35`: success-check Y-bob, toggle thumb.
- Y `1.36` (bounce token): badge pop open, playful confirmations.
- Y `1.45`: number pop-in.
- Y `1.96`: like-button pop.
- Y `3.85` (bounce-strong token): springy hover-out return (avatar group).
- Overshoot belongs to entrances and releases only; never apply it to closes, which use smooth-out or the standard ease.

## 12. Distance tokens
- Distances are non-resting translates that settle to 0.
- `4px` micro: text swap.
- `6px` small: small error-shake segment.
- `8px` base: badge diagonal reveal, page slide, large error-shake segment, digit rise, thinking-state swap.
- `12px` medium: text reveal, input clear.
- `16px`: toast rise.
- `30px` large: check badge appear.
- `40px`: morph lateral slide, success-check bob.
- Panels travel about `50%` of their own height; stacked layers peek `12px` per depth.
- Scale distance down with frequency and up with ceremony (in-place swap 4px, page slide 8px, one-off celebratory badge 30px).
- Treat any translate over about `40px` (except a full panel or drawer) as sluggish; pull it toward `8px`.
- Enter from small offsets (`4–8px`); never slide whole screens.

## 13. Scale tokens
- Scales are non-resting pre-scales that settle to 1.
- `0.96` large: modal open and close.
- `0.97` medium: dropdown open, toast, morph content, banner arrival.
- `0.98` small: tooltip open.
- `0.99` tiny: dropdown close.
- `0.25`: icon-swap outgoing scale (deep, intentional melt).
- Bigger surfaces start further away (0.96); small hints barely scale (0.98–0.99).
- A pre-scale below about `0.9` reads as a zoom and rarely fits UI chrome; snap it to the usage token (a 0.8 modal becomes 0.96).

## 14. Blur tokens
- Blurs are non-resting pre-blurs that settle to 0.
- `1px`: streaming words.
- `2px` small: the default cross-blur (panel reveal, icon swap, text swap, skeleton reveal, number pop-in, toast, badge).
- `3px` medium: page slide, text reveal.
- `4px`: soft exits.
- `8px` large: success check open token; alternative: the success-check recipe uses `10px`.
- Blur can be missing as well as off-token: when usage calls for one (a page slide with no blur), add `3px`.
- Always declare `blur(0)` explicitly at rest, never an unset filter, so the cross-blur interpolates.

# Part 3 — Choosing a transition

## 15. Match the visible element first, then the verb
- Trigger with a small dot floating on top: notification badge.
- Trigger with a surface growing from it: anchored, origin-aware dropdown; centered modal when there is no anchor.
- Surface sliding into a region of the page: panel reveal.
- Two screens, list to detail or step 1 to step 2: page side-by-side slide.
- Element changes width or height: card resize.
- Label changes in place and old and new share letters at start or end ("Copy code" to "Copied", "Follow" to "Following"): text morph.
- Text changes in place and the texts share nothing ("Processing" to "Done"): text states swap.
- Values update because the data behind a view changed (chart period, currency, unit): soft text swap on every changed value.
- Donut or ring chart: even gaps, smallest corner radius, segments morph on data change.
- Two icons in the same slot: icon swap.
- A number updates quietly: number pop-in; with event-like fanfare: spinning counter.
- Confirmation, success or "done" moment: success check (pair with icon swap from a spinner).
- Hovering an item in a horizontal stack (avatars, chips, segmented buttons, tag pills): avatar group hover.
- Form validation error or "this is wrong" feedback: error shake.
- Clearing a text field: input clear with dissolve.
- Placeholder that loads then swaps to content: skeleton loader and reveal.
- In-progress or "thinking" text: shimmer text.
- Small set of mutually exclusive options with a moving highlight: sliding tabs.
- Hover or focus hint over a trigger: tooltip.
- Stacked headline plus supporting line entering with rhythm: staggered texts reveal.
- Card reacting in 3D to the pointer: card hover tilt.
- Circular trigger that becomes the surface it opens: plus-to-menu morph; a separate popover that merely grows from the trigger is a dropdown.
- Header with a collapsible body: accordion.
- Transient confirmation that needs no response: toast; one that needs a response: modal.

## 16. When not to guess or replace
- If nothing clearly matches, present the options rather than guessing.
- Tie-break toward the lower-overhead pattern.
- Propose a replacement only when the current motion is clearly a hand-rolled version of a known pattern or lacks the structure its usage needs.
- If it already is the right pattern, change nothing.

# Part 4 — Open/close asymmetry, stagger & timing

## 17. Open/close asymmetry
- Opening is an invitation; closing gets out of the way: closes are faster and quieter than opens.
- Dropdown `250/150ms`; modal `250/150ms`; panel `400/350ms`; toast `350/250ms`; plus-morph `350/250ms`; banners `350/250ms`; badge `500/180ms`; tooltip `150/50ms`; checkbox `350/150ms`.
- Rule of thumb: exits are about `60%` (up to 70%) of enter duration.
- Put distance and blur on the enter phase; the exit may drop or shrink them so a close does not fling content.
- Bounce on entrances only; exits use calm curves.
- Decouple exits from entrances: an exit is a single quiet fade, not a reverse replay of the reveal.
- Put the close duration on the base rule and the open duration on the open-state rule so one state toggle gives asymmetry.

## 18. Symmetric exceptions
- Do not split these into open/close timings; they read as one reversible motion: page side-by-side `250ms`, tabs sliding `250ms`, accordion `250ms`, icon swap `250ms`, text swap `150ms`.
- Card hover tilt follows and the learn-more arrow uses `350ms` both ways.

## 19. Hover in vs hover out
- Hover in: quick and direct, `≤250ms`, smooth-out.
- Hover out: softer and springier; may take longer and use `cubic-bezier(0.34, 3.85, 0.64, 1)` so the row settles instead of snapping; the one place the out is more elaborate than the in.
- Direction-aware easing on the same property: set the timing function immediately before writing the new values.
- Never let hover shift layout (padding, margin, width).

## 20. Stagger
- Stagger offset `40ms` per item; `80ms` for a few large items.
- Keep total stagger (offset × count) under about `300ms` so the last item does not feel late.
- For long lists cap the number of staggered items or shrink the offset (8 items × 120ms = 960ms is too late; use 40ms).
- Alternative (interface principle): stagger semantic chunks by about `100ms`.
- Line N of a reveal is delayed `40ms × (N − 1)` so the eye lands on the headline first.

## 21. Delay
- Intent delay `80ms` (tooltip appear, success-check path draw) filters accidental triggers or sequences two things.
- Never use delay to pad a slow animation; if motion feels late, trim the duration first.
- Reserve delay for stagger, intent gating and deliberate sequencing.
- Never delay a close or a hover-out; dismissal must feel instant.
- Put a delay on the show rule only so hiding never waits.

## 22. Combining motions
- Spinner to check: success check plus icon swap.
- Thinking states: shimmer plus the states swap.
- Donut morph pairs with the soft text swap on center and legend values.
- Banner stacking reuses the toast entrance.
- Run parallel layers with independent durations and easings when each conveys something different (success-check lanes; badge slide vs pop).
- Combine a continuous ambient loop with discrete short swaps; the entering copy trails the exit by a small gap.

# Part 5 — Transition recipes

## 23. Card resize
- Use when a container's width or height changes with layout state (compact to expanded card, collapsing panel, list row toggling detail).
- Animate `width` and `height` only, `300ms` `cubic-bezier(0.22, 1, 0.36, 1)` (example 260×180 ↔ 160×100).
- Alternative: `250ms` reads more responsive for direct-manipulation size changes.
- Drive it by changing the size directly; no scripting needed.
- Hint `will-change: width, height`.
- Prefer it over the panel reveal when only size changes.
- Reduced motion: size snaps.

## 24. Number pop-in
- Use for counters, prices, balances, any number that updates quietly.
- Animate each character independently from translate `8px` × direction multiplier, opacity 0, blur `2px` to rest.
- `500ms`, `cubic-bezier(0.34, 1.45, 0.64, 1)`, fill both.
- Default direction x `0`, y `1` (digits rise from below); use multipliers 1, −1, 0 to change direction.
- Stagger the last two characters: second-to-last `70ms`, last `140ms`, so decimals feel alive without chaos.
- Alternative: stagger `70ms` per digit index across the changed digits.
- Keep leading characters shared by old and new still; pop only the changed tail (1,299 to 1,305: "1," stays, "305" pops).
- Lay digits out inline, baseline-aligned, with tabular numerals.
- Replay: remove the animating state, re-render digits, reflow (or double animation frame), re-add.
- Reduced motion: no animation.

## 25. Spinning counter (slot-machine reels)
- Use for numbers that change with fanfare (points, prices, follower counts, KPIs).
- One clipped vertical 0–9 reel per digit, `30px` cells, tabular numerals; separators stay static.
- Each strip holds (spins + 1) × 10 + 1 cells; snap to 0 with no transition, reflow, then translate by −(spins × 10 + digit) × `30px` with spins `3`.
- `1400ms` `cubic-bezier(0.16, 1, 0.3, 1)`; stagger columns `90ms` each, left to right.
- Vertical-only motion blur starting at `3px`, decaying linearly to 0 across each column's own delayed window; a uniform blur would smear sideways.
- Soft-fade the window edges with a mask (transparent 0%, opaque 22% to 78%, transparent 100%) instead of a hard crop.
- A reel needs several full rotations, a steep ease-out, a column cascade and a decaying directional blur.
- Reduced motion: no transition, no blur.

## 26. Notification badge
- Use for a small badge appearing on a trigger (bell, inbox, button); the trigger never moves.
- Position absolutely at about top `-6px`, right `-8px`, non-interactive.
- Open: wrapper slides diagonally from translate(`-8.2px`, `12.4px`) to 0 over `260ms` smooth-out.
- Open: dot scale 0 → 1 over `500ms`, opacity over `400ms`, blur `2px` → 0 over `500ms`, all `cubic-bezier(0.34, 1.36, 0.64, 1)`, origin center.
- Close: scale 0, opacity 0, blur `2px` over `180ms` `cubic-bezier(0.4, 0, 0.2, 1)`, no slide, no bounce.
- Slide and pop run on independent clocks on separate elements.
- Reduced motion: no slide, no pop.

## 27. Text states swap (sequential)
- Use for status text where the texts share nothing ("Processing…" to "Done", "Save" to "Saved").
- Phase 1: old text exits up `-4px`, blur `2px`, opacity 0.
- Phase 2: change the text and jump to `+4px` below, blurred, invisible, with no transition.
- Phase 3: reflow and release back to rest.
- `150ms` per phase, `ease-in-out`, on transform, filter, opacity; total `300ms` because it reads as a step.
- Reduced motion: no transition.

## 28. Text morph (shared letters)
- Use for short labels sharing letters at start or end ("Copy code" to "Copied", "Follow" to "Following", "Check in" to "Checked in").
- Keep the shared prefix and suffix still; cross-blur only the differing middle (opacity, blur `2px`) over `180ms` smooth-out.
- Ease the middle's width from old to new over `240ms` smooth-out so the surrounding button or tooltip resizes smoothly.
- Restore plain text after max(180, 240) + `40ms`; on rapid changes start from the latest target.
- Hide the outgoing copy from assistive tech.
- Reduced motion: no transitions.

## 29. Soft text swap (in-place value)
- Use for values updating in place with no movement (chart totals on period change, price on currency change, readings on unit change).
- Old and new cross-blur at the same time in the same spot (opacity, blur `2px`) over `200ms` `ease-in-out`, no gap.
- Ease width over `240ms` smooth-out so neighbors glide.
- Right-align values in lists so both texts share the right edge.
- Apply only to values that changed; whole panels can change at once.
- Reduced motion: no transitions.

## 30. Menu dropdown
- Use for contextual menus, dropdowns, popovers anchored to a trigger.
- Origin-aware: transform-origin on the trigger's side (top-left, top-center, top-right, bottom-left, bottom-center, bottom-right); default top left.
- Closed rest: scale `0.97`, opacity 0, non-interactive.
- Open: to scale 1, opacity 1 over `250ms` smooth-out.
- Close: to scale `0.99`, opacity 0 over `150ms`, non-interactive immediately; close faster and shrink less than you grew.
- Clear the closing state (or unmount) after `150ms` so the next open starts from 0.97.
- Animate transform and opacity only.
- Reduced motion: no transition.

## 31. Modal
- Use for dialogs and overlays conceptually on top of the page, not anchored.
- Origin center; closed rest scale `0.96`, opacity 0, non-interactive.
- Open `250ms`, close `150ms` back to `0.96`, both smooth-out; unmount or clean up after the close.
- Reduced motion: no transition.

## 32. Panel reveal
- Use for a panel sliding into an existing container (detail panel inside a card, expanding section).
- Closed: translateY about half the panel's own height (example `100px`; demo 187px × 0.5 = `93.5px`), opacity 0, blur `2px`, non-interactive.
- Open `400ms`, close `350ms`, both smooth-out.
- Run translate, opacity and blur on the same duration and ease so a half-height travel reads as a full open while staying calm.
- Clip with an overflow-hidden wrapper if the closed state must be fully hidden.
- Reduced motion: no transition.

## 33. Page side-by-side slide
- Use for two screens side by side (list to detail, wizard steps).
- Stack both pages in one area; inactive page opacity 0, non-interactive, blur `3px`, parked page 1 at `-8px`, page 2 at `+8px`.
- Active page opacity 1, translateX 0, blur 0.
- Opacity and transform/filter `250ms` smooth-out; incoming stagger `0ms` (tunable).
- Provide an exit-slide switch that turns the slide and blur off so pages only fade, used on first paint.
- Animate the page sections, not the container.
- Reduced motion: no transition.

## 34. Icon swap
- Use to cross-fade two icons in one slot (hamburger to close, sun to moon, play to pause).
- Stack both icons in the same grid cell.
- Incoming opacity 1, blur 0, scale 1; outgoing opacity 0, blur `2px`, scale `0.25`; simultaneous, `250ms` `ease-in-out`.
- Alternative: scale 0.25 → 1, opacity 0 → 1, blur `4px` → 0; with a spring, `duration 0.3, bounce 0` (bounce always 0); without one, cross-fade both icons with `cubic-bezier(0.2, 0, 0, 1)`.
- Never set `will-change` on the icons: it freezes the raster at the 0.25 start scale and large icons scale up blurry.
- Reduced motion: no transition.

## 35. Success check
- Use when status goes pending or unknown to success (payment processed, file uploaded, form saved) so the moment feels earned.
- Four parallel lanes, each `500ms`: opacity 0 → 1, rotate `80deg` → 0, blur `10px` → 0 (all smooth-out), Y-bob `40px` → 0 on `cubic-bezier(0.34, 1.35, 0.64, 1)`.
- SVG path stroke-draws dashoffset full length → 0 over `500ms` smooth-out, delayed `80ms`.
- Dash length = measured path length rounded up by 1 (19.42 becomes `20`); too short pre-reveals the stroke, too long draws past the end.
- Round line caps hide sub-pixel overshoot; let the SVG overflow so the stroke never clips.
- Cold load is hidden with no animation; fill forwards so it rests visible.
- Success states are usually persistent; the appear is the motion.
- Alternative exit: fade 1 → 0 and blur 0 → `4px` over `500ms` smooth-out only, no rotate, bob or path reversal, so it dissolves in place.
- Replay from visible: reset, reflow, re-enter.
- Reduced motion: no animation; opacity 1 with the path fully drawn.

## 36. Avatar group hover (distance-falloff lift)
- Use for horizontal stacks (avatars, chips, badge clusters, segmented buttons, tag pills, reactions) for a magnetic "comb" signal.
- Hovered item lifts `-4px` and scales `1.05`; neighbors lift `-4px × 0.45^distance` (−1.8px, −0.81px…); non-hovered items stay at scale 1.
- Apply translateY before scale so scale does not amplify the lift.
- `320ms` both ways; hover-in `cubic-bezier(0.22, 1, 0.36, 1)`, leave `cubic-bezier(0.34, 3.85, 0.64, 1)`.
- Set the timing function immediately before writing offsets so the springy curve applies only on leave; never hard-set it.
- Reset all offsets when the pointer leaves the whole group, not each item.
- Reduced motion: no transform, no transition.

## 37. Error state shake
- Use for validation errors and any percussive "wrong, try again" hint (wrong PIN, duplicate tag, name taken) without an alert.
- Four legs: 0 → `+6px` (`80ms`) → `-6px` (`80ms`) → `+4px` overshoot (`60ms`) → 0 (`60ms`); total `280ms`.
- Keyframe stops 0%, `28.57%`, `57.14%`, `78.57%`, 100%; each leg eases with its own `cubic-bezier(0.22, 1, 0.36, 1)`; recompute stops if leg ratios change.
- Border to error color over `150ms` ease-out; back from error over `280ms` ease-out.
- Keep border width constant across states so the tween never shifts content.
- Error message: visible immediately on error with an opacity fade over `280ms` ease-out; delay hiding visibility by `280ms` so the fade-out stays painted.
- Hold the error `3000ms` (long enough to read), then fade border and message back to neutral.
- Restart the hold timer on every new error; cancel it and clear the error as soon as the user types.
- Keep error state and shake state separate; the shake alone works as a hint jiggle.
- Clear the shake state about `20ms` after it ends.
- Reduced motion: no shake; color and message change remain.

## 38. Input clear with dissolve
- Use when clearing a text field (search clear button, filter reset).
- A mirror of the old text flies down `12px`, opacity → 0, blur → `2px` over `400ms` smooth-out; the real text is hidden while the mirror owns the glyphs.
- Placeholder falls in from `-12px`, opacity `0.9` → 1, blur `2px` → 0, `400ms` smooth-out.
- Per-word streak glow: starts after `50ms`, rises linearly to peak at `15%` of the remaining time, falls linearly to 0 by the `1000ms` total; peak opacity `0.42`; spread `1.5`.
- Each streak: four stacked elliptical radial gradients at the bottom edge, offsets 0, +0.45, −0.4, +0.15 of half-width; width factors 0.8, 0.55, 0.65, 0.9; heights 7, 8, 6, 5px; alphas 0.22, 0.18, 0.16, 0.14; half-width = max(word width × 0.45, `8px`) × spread.
- Blend `multiply` in light mode; in dark mode `screen`, about `0.85` opacity, white gradients.
- The rise/peak/fall envelope needs per-frame scripting; it cannot be a static keyframe.
- Preserve focus through the clear; ignore re-triggers while a clear runs.
- Reduced motion: suppress the glow.

## 39. Skeleton loader and reveal
- Use for placeholders that load then reveal content (list rows, cards, profile headers).
- Pulse the skeleton children's opacity 1 → `0.5` → 1 over `1000ms` `ease-in-out`, once by default.
- Put the pulse on children so the skeleton layer's opacity and blur stay free for the reveal.
- Reveal: skeleton to opacity 0 and blur `2px` while content goes from opacity 0, blur `2px` to rest, both `400ms` `ease-in-out`, so it reads as one motion.
- Stack skeleton and content in one slot for a layout-free swap.
- Replay by snapping back to loading with transitions off for one reflow.
- Reduced motion: no cross-fade, no pulse.

## 40. Shimmer text
- Use for loading or "thinking" labels that should feel alive without a spinner.
- Base text `#7c7c7c`; a duplicate layer of the text carries a highlight `#0d0d0d` band clipped to the glyphs.
- Gradient transparent 0–40%, highlight at 50%, transparent 60–100% (a narrow 20% band); background size `400%`.
- Sweep background-position 100% → 0% over `2000ms` linear infinite.
- Dark theme alternative: base `#9a9a9a`, highlight `#f5f5f5`.
- Pure CSS, slow and linear.
- Reduced motion: static muted text.

## 41. Thinking states (AI status line)
- Use for an AI status line narrating steps ("Setting up a workplace", "Running a command", "Browsing files").
- Shimmer each state (`2000ms` linear sweep) while it holds `2000ms`.
- Swap: outgoing exits up `-8px`, blur `2px`, opacity 0; incoming enters from `+8px` below; both `150ms` `ease-in-out`.
- Outgoing and incoming overlap, incoming held back `50ms`, so a swap costs one 150ms, not two; remove outgoing after 150 + 50ms.
- Size the box to the longest state (hidden sizer) so it never resizes mid-swap; centered, or left-aligned if states share a left edge.
- Announce as a status region.
- Reduced motion: no transition, transform, blur, shimmer or cycling.

## 42. Reasoning stream
- Use for reasoning previews, live log tickers, changelog streams in a fixed viewport.
- Step the transcript up 2 line-heights every `840ms` hold; each step `500ms` smooth-out.
- Stepped scrolling reads as thinking better than continuous linear scroll.
- Fade top and bottom `28px` edges with a mask, not painted gradients, so any background works.
- Loop seamlessly: render the transcript twice and subtract one copy's height with no transition when passed.
- Reduced motion: no transform, loop disabled.

## 43. Streaming text (word-by-word resolve)
- Use for model output arriving word by word.
- Each word resolves opacity 0 → 1, blur `1px` → 0 over `350ms` smooth-out, one word every `60ms`, so about 6 words resolve at once.
- No movement, only focus and opacity, so layout never shifts.
- Prefer it over a typewriter: it reads as condensing into place, not keystrokes.
- Replay: wipe words hidden with transitions off, reflow, restore, then reveal.
- Reduced motion: words fully visible, no blur.

## 44. Matrix dot loader
- Use where a spinner is too loud: beside a status line, inside a compact button, in a table cell.
- 4×4 grid of `2px` dots with `2px` gaps; base `#d9d9d9`, active `#85858f` (dark `#3a3a3e` / `#b8b8c2`).
- Color pulses base → active at `15%` → base by `45%`, held to 100%, `1200ms` `ease-in-out` infinite; the short active window keeps only a few dots lit.
- Variants are per-dot delay tables on one keyframe.
- Scan: column × cycle/10 (0, 120, 240, 360ms).
- Twinkle: order [7,2,11,5,14,9,0,12,3,15,6,10,13,1,8,4] × cycle/16; every dot fires once per cycle, never clumped.
- Orbit: clockwise ring [1,2,7,11,14,13,8,4] × cycle/8; center dots hold still.
- Pulse: inner [5,6,9,10] first, the rest `0.16` × cycle (`192ms`) behind.
- Rounded variants hide corners [0,3,12,15].
- Reduced motion: no animation.

## 45. Sliding tabs (segmented control)
- Use for segmented controls, view switchers, filter segments.
- One shared pill behind the labels tweens translateX and width to the active tab's measured offset and width over `250ms` smooth-out.
- Label color muted `rgba(15,15,15,0.8)` → active `#0f0f0f` on the same clock; hovered inactive tabs also go active.
- Bar `#f1f1f1`, `3px` padding and gap, radius `48px`; tabs and pill `30px` tall, tab padding `4px 12px`; pill `#ffffff`, top `3px`; labels above the pill.
- On first paint and resize, place the pill with transitions suspended (off, write, reflow, restore).
- Reduced motion: no transitions.

## 46. Tooltip (shared, traveling)
- Use for hover and focus hints shared by a group of triggers (toolbar buttons, icon rows, avatar stacks).
- Appear after `80ms`: opacity 0 → 1, scale `0.98` → 1 over `150ms` ease-out, origin bottom center.
- Disappear immediately, no delay, `50ms` ease-out.
- One bubble per group: when already showing, travel x and width to the next trigger over `160ms` smooth-out with no delay; when hidden, snap geometry so only the appear plays.
- Animate translate and scale as independent properties so travel and appear run on separate clocks.
- Show on pointer enter and focus; hide on blur and on leaving the group.
- Bubble `8px` above, padding `8px 12px`, radius `8px`, background `#ffffff`, text `#2f2f2f`, shadow `0 0 0 1px rgba(0,0,0,.06), 0 2px 6px rgba(0,0,0,.05), 0 4px 42px rgba(0,0,0,.06)`.
- Reduced motion: no transition.

## 47. Staggered texts reveal
- Use for headline plus supporting line (hero copy, empty states, onboarding).
- Each line translateY `12px`, blur `3px`, opacity 0 → rest over `500ms` smooth-out; line N delayed `40ms × (N − 1)`.
- Flip to shown on the next animation frame so the entering transition is not batched away.
- Exit: one quiet `200ms` ease opacity fade for every line, no delay, no Y return, no blur, no stagger; transform and blur snap back instantly; clear after 200ms.
- Reduced motion: no transition.

## 48. Card hover tilt with glare
- Use for product cards, membership cards, feature tiles, cover art that should feel physical.
- Pointer normalized 0..1 (clamped): rotateY = (px − 0.5) × max; rotateX = (0.5 − py) × max.
- `perspective(1000px)` with preserved 3D; peak tilt `14deg` (10–16deg reads tasteful); alternative maxima `32deg` (component default) and `40deg` (live demo).
- While moving follow over `400ms` smooth-out (a smoothed follow, not raw 1:1); on leave return flat over `1000ms` smooth-out.
- Optional speed sensitivity: smoothed speed (EMA `0.72`), reference `1.2` px/ms, factor = 0.15 + 0.85 × min(1, speed × sens / 1.2); off by default.
- Glare at the pointer: three white radial circles (`95px` 0.48 → 0.06 at 52% → 0 at 84%; `200px` 0.22 → 0.04 at 58% → 0 at 78%; `360px` 0.10 → 0 at 88%), screen-blended, fading to `0.32` over `300ms` smooth-out.
- Track the pointer on a flat outer wrapper that never transforms, or rotating edges slip from under the cursor and hover flickers.
- Touch: disable touch scrolling on the wrapper and capture the pointer on press so tap-hold-drag tilts; reset on release or cancel; mouse resets on leave.
- Card radius `12px`, clipped overflow.
- Reduced motion: flat, no tracking.

## 49. Plus-to-menu morph
- Use when a circular trigger becomes the surface it opens (+ FAB, compose button).
- Box grows from `40×40` radius `40px` to panel size (example `183×172`) radius `20px`, anchored to a corner so it grows out of the button.
- Open `350ms` `cubic-bezier(0.34, 1.25, 0.64, 1)`; close `250ms` smooth-out; never merge the two eases.
- Plus: opacity → 0 `200ms`, slide `-40px` `350ms`, blur `2px` `200ms`; icon scales `0.97` and rotates `45deg` into an ×.
- Menu: from translateX `40px`, scale `0.97`, blur `2px`, opacity 0 to rest (opacity and blur `200ms`, transform `350ms`); plus and menu slide 40px in opposite directions as a lateral hand-off.
- Alternative close anticipation: the closing surface nudges to (`5px`, `5px`) at 35% and back over `700ms` smooth-out.
- Clip overflow on the morphing box.
- Mirror state to expanded; close on outside click and Escape.
- Reduced motion: no transitions.

## 50. Accordion
- Use for disclosures, FAQs, settings groups, filter sections, "show more".
- Animate height via grid rows `0fr` ↔ `1fr` (no measuring), `250ms` smooth-out both ways.
- Inner content opacity 0 → 1 and blur `2px` → 0 on the same clock.
- Chevron flips `scaleY(1)` → `scaleY(-1)` over `250ms`, passing through a flat line; origin center, path symmetric, non-scaling stroke.
- Clip overflow and put padding on the inner element, never the track, or a strip stays visible.
- Mirror state to expanded.
- Reduced motion: no transitions.

## 51. Toast
- Use for transient confirmations rising from the bottom ("Saved", "Copied", "Message sent").
- Closed: translateY `16px`, scale `0.97`, blur `2px`, opacity 0.
- Open `350ms`, close `250ms`, smooth-out: arriving deliberate, leaving snappy.
- Animate opacity, transform, filter.
- Reduced motion: no transition.

## 52. Banner stacking
- Use for overlapping notifications; newest stays legible while the queue is acknowledged.
- Arrival from translateY `60px` (alternative `80px`), scale `0.97`, blur `2px`, opacity 0 to rest over `350ms` smooth-out.
- Depth 1: up `12px`, scale `0.94`, opacity `0.6`, blur `1px`; depth 2: up `24px`, scale `0.88`, opacity `0.36`, blur `2px`; origin bottom center; max 3 visible.
- The fourth arrival pushes the oldest out: up `36px`, scale `0.82`, opacity 0, blur `2px` over `250ms`, removed `60ms` later.
- Hover spreads into a list: older banners climb (100% + `8px`) × depth at scale 1, opacity 1, blur 0; newest stays put.
- Drive spread from pointer geometry, holding until the pointer leaves the taller spread column, because gaps belong to no element.
- Release the entering banner in the same task after a reflow; a frame hop can be skipped when throttled.
- Swap transform-origin only while the element is at identity.
- One depth-index swap animates the whole stack.
- Reduced motion: no transitions, transforms or blur.

## 53. Like button
- Use for like, favorite, heart toggles that deserve a tiny celebration.
- Fill and color to `#f40051` over `150ms` smooth-out.
- Pop 1 → `0.82` (30%) → 1 over `350ms` `cubic-bezier(0.34, 1.96, 0.64, 1)`: anticipation squeeze then spring.
- Burst 8 particles of `2.5px`: 0% opacity 0, scale 0.4 at center; 20% opacity 1, scale 1 at 25% of the vector; 100% opacity 0 at full vector (about `20px`), end scale; `600ms` ease-out, fill forwards.
- Re-randomize per like: angle 360/8 × i ± `16deg`; distance 20px × `0.68–1.18`; duration 600ms × `0.78–1.22`; delay `0–70ms`; end scale `0.35–0.75`; size × `0.6–1.4`.
- Celebrate only on like; unliking reverses the fill with no particles.
- Scale an HTML wrapper, never the inline SVG.
- Reduced motion: no pop, no burst; fill remains.

## 54. Learn-more hover arrow
- Use for "Learn more", "See all", "Continue" links with a trailing chevron.
- On hover slide the chevron `2px` toward the reading direction and rotate its arms apart `±8deg` about the apex (pivot `10px 8px` in view-box space), non-scaling stroke.
- `350ms` in and out, smooth-out; pure CSS.
- Hover-only; never communicate anything essential through it.
- Reduced motion: no transitions.

## 55. Checkbox check
- Use for checkboxes, to-do completion, multi-select rows.
- Box background and shadow fill over `150ms`; checkmark stroke-draws over `350ms` smooth-out, delay `0ms`.
- Uncheck reverses the stroke over `150ms` with no draw: slower draw in, faster erase out.
- Dash length = measured path length rounded up (placeholder `15`).
- Transition the dash offset (not a keyframe) so a mid-draw uncheck reverses cleanly.
- Reduced motion: no transitions.

## 56. Toggle switch
- Use for on/off switches (settings rows, theme toggles, feature flags).
- Thumb travels `14.66px` over `350ms` `cubic-bezier(0.34, 1.35, 0.64, 1)`, fill both.
- Double bounce: overshoot past the end by `1px` at `55%`, back by `0px` at `80%`, settle at 100%; off mirrors.
- Track color cross-fades on its own clock (`0ms` default, instant).
- Do not play the bounce on page load; enable it only after the first interaction.
- Reduced motion: thumb snaps.

## 57. Donut chart morph
- Use for donut or ring charts whose data changes (period switch, filter).
- Straight parallel gaps of `3px`, corners `2px` (the smallest radius in the system); example `140×140`.
- Morph every segment from old share to new over `400ms` smooth-out in the same chart; never re-render or slide.
- Keep segment order constant across data sets.
- Dim non-hovered segments to opacity `0.2` over `150ms` smooth-out on legend hover.
- Update center and legend values with the soft text swap at the same time.
- Reduced motion: draw new values instantly.

# Part 6 — Generative/AI UI loading states

## 58. When to use a generation animation
- Headline: traced-glyph text variant; subtitle or eyebrow: small-text variant (one dotted line per line); photo: image variant.
- Mixed hero: auto (text `≥32px` traced, smaller text gets a dotted line, images as image).
- An AI feature returns UI (component, chart, summary card, draft): play the wireframe generation when the result arrives.
- A launch page or demo telling a "built by AI" story: add generation texts, played on scroll into view.
- Several elements at once (grid of results): wireframe on each with about `260ms` delay per item; texts fit around one element only.
- Not for small inline UI (badge, single button, anything under about `120px`) or UI that appears often (route changes, list rows); use a skeleton or texts reveal instead.
- A generation animation is a moment, not a loading state; while data loads show a regular skeleton, then play the generation over the real UI.
- Unsure: plain wireframe mode only.

## 59. UI wireframe generation
- Default drawing `2400ms`; whole run ≈ duration × `1.09` (about 2.6s).
- Keep between `1600ms` (parts too short to read) and `3600ms` (feels like waiting); change only duration, all phases scale together.
- Dot field `0–0.30` of duration, rippling from center, matrix rain until about `0.86`.
- Probe line `0.02–0.24`, sweeping left to right lighting dots.
- Guides `0.04–0.30`, along edges past corners.
- Outline `0.10–0.42`, traced from top center both ways; particles land, corner handles pop, size label counts up with a build timer.
- Parts `0.28–0.74`: each box, text line, icon in document order.
- Reveal `0.74–1.055`; clean `0.84–1.04` (dot field and guides fade).
- Drawing easing `cubic-bezier(0.16, 1, 0.3, 1)`; reveal easing `cubic-bezier(0.22, 1, 0.36, 1)`.
- Reveal the real UI top to bottom behind a scan line, fading in and sharpening from `3px` blur while the drawing wipes away; extend the clip about `80px` so the shadow arrives without a pop.
- Draw lines as small round dots that keep flowing in the drawing direction.
- Measure from the element: outline and corner radius; boxes are descendants with background, border or image plus media and form controls; skip boxes over `60%` of the element and blurred layers; text lines from line rects; inline icons up to `120px` path by path.
- Key elements (default 5): interactive first (buttons, inputs, links, tabs, switches), then largest boxes; each gets guides, handles and a size label; a targeting reticle with coordinate readout follows the part being drawn.
- Trace at most `60` parts (largest kept); about `30` for busy components so it reads as a sequence, not noise.
- Exclude decorative layers, live charts and video from the drawing.

## 60. Glyph-traced headline generation
- Build `3000ms`; whole run ≈ duration × `1.06`; keep `2000–4500ms`; give long headlines more (`3600ms` for three lines) or lower the fade stagger.
- Glyphs traced `0.06–0.76` of duration, about `0.16` each, overlapping, outer shape before counters, ease-out; clean `0.86–1.04`.
- Each glyph fades in `140ms` after its outline finishes, over `90ms` ease-out, `90ms` apart; never before its own outline is done.
- Spread glyph starts on sequence ease `[0.37, -0.02, 0.73, 0.88]` (gentle in-out).
- Sequence presets: linear; ease-in (sparse then crowding); ease-out (burst then settle); ease-in-out; smooth-out (most text early, last characters settle slowly).
- Fade by character (default), by word, or with a gradient mask sweeping left to right.
- Particles flying to each glyph start: on; focus bracket, coordinate readout and type guides (cap height, x-height, baseline, descender, font spec): off by default, on for a technical look.
- Trace at most `140` glyphs; the rest only ink in.
- Never trace body copy; paragraphs get dotted lines.
- Outline simplification tolerance `0.3px`.
- Disable automatic optical sizing on traced headlines so outlines match.

## 61. Small-text generation
- One dotted line per text line drawn left to right with a moving head and end caps, `0.12–0.78` of duration, lines sequenced on the sequence ease.
- Characters fade in as the stroke passes them.
- Keep to short copy (eyebrow, subtitle, caption, label); long body text simply appears.

## 62. Image generation reveal
- Images in one block start `0.04–0.16` of duration apart.
- Frame `0–0.2`: dotted frame from top center both ways, corner handles, size label, live status (sketch count, dot count, color %, resolving %).
- Sketch `0.08–0.38`: iso-tone contour lines at six tone levels on a `3px` grid, smoothed, strokes up to `240px`, finer dots (`0.75×` dot size).
- Screen `0.2–0.56`: fine halftone, `3–5px` cells, sweeping in from top-left; dot size by tone with local contrast lifted; luminance stretched between the 1st and 99th percentile.
- Color `0.52–0.68`: grey dots cross into a dot matrix in the photo's own colors.
- Photo `0.64–0.88`: the photo fades in over its color dots, sharpening from `6px` blur.
- On dark pages flip the halftone (light dots grow with brightness).
- Honor the image's fit and position; unreadable images get the frame and an even dot screen only.

## 63. Generation texts (build log, style panel, step line)
- Build log left of the element: a header like `LOG // PARTS 06/09`, one line per part (id, type, position, size) with a progress bar ending `[  ok  ]`; show the last 11 lines for text and image variants.
- Style panel right of the element: tokens then a rule per part (real radius, type, colors, transition), typed at a steady rate with a caret; footer shows tokens/sec, line count, WRITING / READY; keep it under about 60 lines.
- Step line under the element: one step at a time with a pulsing dot (`6px`, scale `0.6` → 1, `560ms` ease-in-out alternate).
- Default UI steps "Planning layout", "Drawing structure", "Writing styles", "Adding motion", ending in a named done step ("Invite modal ready"); text and image steps "Setting type", "Tracing glyphs", "Sampling images", "Inking"; write steps for the product.
- Placement: side panels only with `≥150px` free on each side; else one strip under the element; else steps only; else nothing.
- Draw only where the page is empty; give the element room (centered with min-height).
- Steps sit `28px` (UI) / `24px` (text) below; the under-strip `56px` (UI) / `64px` (text) below.
- Keep panels quieter than the UI.

## 64. Generation overlay styling
- Keep the drawing monochrome grey as a working layer; the real UI brings color.
- Light: line `#9a9a9a`, strong (heads, handles, reticle, labels) `#6c6c6c`, dot ink `rgba(13,13,13,0.32)` (halftone 0.5), surface `#ffffff`, panel text `#0d0d0d`, muted `#8b8b8b`.
- Dark: line `#6f6f6f`, strong `#a3a3a3`, ink `rgba(245,245,245,0.3)` (halftone 0.5), surface `#181818`, text `#f2f2f2`, muted `#8f8f8f`.
- Dot size `2.1px`; guides `1.6px` (UI) / `1.5px` (text) dashed `0 5`; handles `1px`; reticle `1.2px`; moving heads r `2.4`; flyers r `1.6`; end caps r `1.7`.
- Monospace labels `9px` (`0.02–0.04em` tracking); small and tag labels `7.5px` (tags uppercase, `0.05em`); panels `7.5px/11px`, `0.03em`; panel headers `0.08em` with a dotted underline; step line `11px/18px`, `8px` gap.
- Keep neutral greys close to the page's text colors.

## 65. Generation pitfalls
- Run only after layout settles, fonts load and images decode; never on a hidden element (generate after tabs or accordions open).
- Do not add your own entrance, mask, opacity or filter on the element during the run.
- Avoid running while the element scrolls inside an overflow container; play once in view.
- Do not force texts into dense layouts; fall back to plain wireframe.
- Never gate interaction on it; for anything users wait on repeatedly, use a skeleton loader.
- Keep the overlay hidden from assistive tech with no pointer input; keep the element itself in the accessibility tree.
- Reduced motion: skip the drawing and texts, fade the element in over `200ms` ease-out.

# Part 7 — Polishing & auditing existing motion

## 66. Polish scope
- Scan every motion source: stylesheets, inline styles, CSS-in-JS, style blocks, utility arbitrary values, animation variants; read keyframes through the animation that drives them.
- Check all five dimensions: durations, easings, translate distances, `scale()`, `blur()`.
- Apply the higher-order rules too: open/close asymmetry, hover in/out, stagger totals, delays, not just on-grid values.
- A polish pass maps values onto the scale; whole-pattern replacements are a separate job.
- Report only values that should change, as usage: from → token (value) — reason.

## 67. Applying polish
- Replace hardcoded values with token references when the tokens are available; otherwise write the token's literal value.
- Keep the existing unit and format (`0.25s` vs `250ms`) unless switching to a token reference.
- Touch only the motion values; no reformatting, no unrelated edits, small diff.
- Motion-only: if a fix would touch component logic, stop.
- Fix set: values onto the scale by usage, hover transitions covering what hover changes, a reduced-motion guard, named properties instead of `transition: all`.

## 68. Hygiene checks
- Flag `transition: all`.
- Flag animating `width`, `top`, `box-shadow` instead of `transform` and `opacity`.
- Flag `will-change` misuse.
- Flag missing `prefers-reduced-motion`.
- Flag same-purpose transitions using different values across the product.

## 69. Review finding types
- Pattern mismatch: component motion built wrong (animates height or top, no exit, pops in, unmounts instantly).
- Off-scale: value off the scale for its usage (modal close 300ms, scale 0.8, linear easing on surfaces, ease-in on hover).
- Known pattern available: a hand-rolled component a standard recipe covers (informational, no penalty).
- Untransitioned overlay: modals, tooltips, dropdowns that pop in or out.
- Hover without transition: hover states that snap.
- Layout animation: hover shifts that move layout (padding, margin, width).
- Transition all: animates layout and hurts performance.
- Slow duration: any transition over 1 second, including through tokens.
- Hardcoded duration: literals instead of shared motion tokens.
- No reduced motion: animation without a guard.
- Inconsistent durations: too many distinct duration values across the product.

## 70. Per-component review
- For each component (modal, dropdown, popover, tooltip, toast, drawer, accordion, tabs, toggle, checkbox, badge, skeleton), read open and close timing, easing, scale, travel, exit and animated properties.
- Compare with its reference recipe by usage; mark each as matching, off the scale, built wrong, or hand-rolled.
- Describe fixes in user-noticeable terms ("Opens in 250ms instead of 800ms", "Animates out when it closes instead of disappearing instantly").
- Re-check after fixing and report the change.

# Part 8 — Live refinement method

## 71. Refine on the running component
- The running component is the preview: no play button or scrubber; apply edits as live, reversible overrides and re-trigger the interaction.
- Group transitions into component → phases (open, close) → member elements (panel, backdrop, staggered items) on one shared timeline, one lane per member-property, so stagger and delays line up.
- Always report both phases, including the close phase not currently on screen; take opposite-phase timings from the state-variant rules; never invent timings.
- Accepted changes go back to the correct state rule per member; edit only that phase's rule.

## 72. Small refinement (token tweaks)
- Infer usage from label and selector; propose a change only where the value differs from its usage token.
- Covers duration, delay, easing, plus scale, blur and distance lanes.
- Apply the polish rules: closes faster and quieter, hover in fast and out soft, stagger totals under about 300ms, 80ms intent delays, never delay a close.
- Each suggestion: title, from → to, minimal change, one-sentence reason in usage terms ("A size change reads as direct manipulation — 250ms is more responsive than 400ms").
- If nothing should change, suggest nothing.

## 73. Replace transition
- Suggest exactly one whole-pattern replacement matching the inferred usage, with the token duration and easing for its phase; if none genuinely fits, suggest nothing.
- Prefer the lower-overhead pattern on ties; never replace what is already the right pattern.
- Snapping to the nearest token is only a fallback; usage-aware matching (300ms modal close → 150ms, dropdown open → 250ms) requires reasoning about intent.

# Part 9 — Make interfaces feel better principles

## 74. Concentric radius
- Outer radius = inner radius + padding.
- Never the same radius on parent and child.

## 75. Optical alignment
- When geometric centering looks off, align optically (icon buttons, play triangles, asymmetric icons) via padding or by fixing the icon.

## 76. Shadows over borders
- Layer multiple transparent shadows for depth instead of solid borders; shadows adapt to any background.

## 77. Interruptible motion
- Use transitions for interactive state changes so they can be interrupted mid-flight; reserve keyframes for staged one-shot sequences.

## 78. Split and stagger entrances
- Split content into semantic chunks and stagger each by about `100ms`.

## 79. Subtle exits
- Exit with a small fixed translateY instead of a full height; exits softer than enters.

## 80. Icon animation
- Animate icons with opacity, scale and blur, never visibility toggles: scale `0.25` → 1, opacity 0 → 1, blur `4px` → 0.
- With a spring: `duration 0.3, bounce 0`; without: keep both icons present and cross-fade with `cubic-bezier(0.2, 0, 0, 1)`.

## 81. Typography details
- Antialiased font smoothing on the root (macOS).
- `font-variant-numeric: tabular-nums` on any dynamically updating number.
- `text-wrap: balance` on headings; `text-wrap: pretty` on body to avoid orphans.

## 82. Image outlines
- 1px low-opacity outline: `rgba(0,0,0,0.1)` in light, `rgba(255,255,255,0.1)` in dark.
- Never tinted neutrals; they read as dirt.

## 83. Scale on press
- `scale(0.96)` on press; never below `0.95`; allow disabling where motion distracts.

## 84. Skip animation on first render
- Prevent enter animations on initial page load, while verifying intentional entrances still play.

## 85. Hit areas
- Prefer `44×44px` for touch; at least `40×40px` in dense desktop UI.
- Extend hit areas with a pseudo-element; never let two hit areas overlap.

# Part 10 — Modern design-system rules

## 86. Color palette
- Page `#f9f9f9` / dark `#131313`; surface `#ffffff` / `#1d1d1d`; text `#0d0d0d` / `#f2f2f2`.
- Muted (secondary text, icons) `#6c6c6c` / `rgba(202,202,202,.7)`; hairline `rgba(0,0,0,.08)` / `rgba(255,255,255,.08)`.
- Accent (primary action, selection, focus) `#17181c` / `#ffffff`; on-accent `#ffffff` / `#0d0d0d`.
- Grey areas are transparent ink `rgba(0,0,0,.02)` / `rgba(255,255,255,.03)`, never solid grey hex.
- Chip and quiet-button fill `rgba(0,0,0,.04)` (hover .06, pressed .08); dark `rgba(255,255,255,.07)` (hover .10, pressed .08).
- Skeleton fill `rgba(0,0,0,.06)` / `rgba(238,238,239,.1)`.
- Soft accent (badges, selected rows) `rgba(0,115,229,.06)` with `rgba(0,83,227,.8)` text; dark `rgba(0,115,229,.16)` with `rgba(122,168,255,.95)`.
- Blue is for soft accents and links, never the primary button.
- Accent only on one primary action, selection or focus ring; never large areas; most UI neutral.

## 87. Typography
- Inter Variable with optical sizing on; body weight 400; changing numbers tabular.
- Extra large `60/70/500` (hero temperature, price, balance only); display large `40/48/500`; display `28/34/500`; title `16/22/500`; subtitle and card title `15/20/500`; body (labels, menu items, buttons, paragraphs) `13/20/400`; caption `12/16/400`.
- Button and badge labels weight 500.
- Two weights (400, 500), two text colors (fg, muted), one paragraph style.
- No uppercase, no letter-spacing, no eyebrows, no opacity on text.

## 88. Spacing, shape and sizes
- Spacing scale `8, 12, 16, 24, 32px`; `6px` icon-to-label inside a button, `8px` outside.
- Radii: controls pill `40px`; menu items `8px`; menus and popovers `12px`; cards and panels `24px` with `24px` padding (scale both down for smaller cards); small chips `6px`; inputs `10px`; nested radii concentric.
- Heights: buttons and inputs `36px`; menu items and compact buttons `32px`; chips `28px`.

## 89. Surfaces and depth
- Prefer layered shadows to borders.
- Material (menus, popovers, floating cards): `0 4px 42px rgba(0,0,0,.06), 0 2px 6px rgba(0,0,0,.05), 0 0 0 1px rgba(0,0,0,.06)`; dark `0 1px 3px rgba(0,0,0,.04), inset 0 1px 0 rgba(255,255,255,.04), inset 0 0 0 1px rgba(196,196,196,.08)`.
- Resting card: `0 0 0 1px rgba(0,0,0,.04), 0 8px 32px -4px rgba(0,0,0,.06), 0 1px 3px 0 rgba(0,0,0,.04)`.
- Edge effects wrapping a card: the outer wrapper is the card (surface, radius, exact shadow); the effect sits 1px under the ring (margin −1px, radius +1px); no extra ring, never split the shadow.
- Idle glow effects stay softly on at rest; beam-type effects pause at rest.
- Hairline dividers: 1px, about 49% of border strength, fading out toward both ends.
- Top and bottom bars inside a card: `16px` padding all round, even when the body uses 24px.

## 90. Components
- Primary button: pill, `36px`, padding `0 12px` (`10px` on the side of a 16px icon), gap `6px`, `13/20` weight 500, accent fill, on-accent text, shadow `0 1px 2px 0 rgba(0,0,0,.2)` (dark `.4`); hover slightly lighter; press 97%.
- Secondary button: pill, chip fill, fg text, no border.
- Icon button: `32px` circle, transparent, chip fill on hover; icons `16px`, `1.5px` stroke, round caps and joins, current color.
- Raised round button (mic, play, add): surface fill, `0 1px 3px 0 rgba(0,0,0,.04), inset 0 0 0 1px rgba(0,0,0,.08), inset 0 -1px 0 0 rgba(0,0,0,.08)`; dark `0 1px 1px 0 rgba(0,0,0,.24), inset 0 0 0 1px rgba(255,255,255,.04), inset 0 1px 0 0 rgba(255,255,255,.06)` on `rgba(255,255,255,.04)`; hover adds 2% ink.
- Input: `36px`, radius `10px`, surface fill, 1px hairline shadow; focus = `3px` soft-accent ring plus 1px accent.
- Menu: material surface, radius `12px`, padding `6px`, items `32px` with radius `8px` and chip hover; items with an icon pad `6px` on the icon side instead of `8px`.
- Tabs and segmented controls: chip track with a sliding surface pill.
- Toggle: `32×20` track, chip when off, accent when on, white knob with soft shadow.
- Focus ring: `0 0 0 2px surface, 0 0 0 4px accent`.

## 91. Press feedback
- Press scales down over `150ms` `cubic-bezier(.22,1,.36,1)` and eases back over the same 150ms on release; never instant.
- Depth by size so travel is always about 1–2px: wide buttons and clickable cards (`≥200px`) 99%; regular and pill buttons 97%; round and icon buttons up to 64px 95%.

## 92. Motion in the design system
- `150ms` small feedback; `250ms` menus and toggles; `350–400ms` panels and modals; `500ms` large reveals.
- Exits faster than enters (about 60%).
- Default easing smooth-out; light bounce `cubic-bezier(0.34, 1.36, 0.64, 1)` for playful confirmations.
- Enter from small offsets (`4–8px`), scale `0.96–0.99`, blur `2–8px`; never slide whole screens.
- Every state change animates; under reduced motion keep opacity only.

# Part 11 — Performance & interruptibility

## 93. Compositor-friendly properties
- Animate transform, opacity and filter; restrict width and height animation to resize-type motions (card resize, text width easing, accordion grid rows).
- Never animate padding, margin or top for hover or layout.
- Use individual `translate`, `rotate`, `scale` properties to give each part of a motion its own duration and curve.

## 94. will-change and rasterization
- Use `will-change` sparingly, only for transform, opacity, filter, and only when first-frame stutter appears; never `will-change: all`.
- Never on elements that scale up from small values (icon swap): the raster freezes at the start scale.
- Scale an HTML wrapper, never an inline SVG; transformed SVG can rasterize at 1× and pixelate on hi-DPI.

## 95. Interruptibility
- Prefer transitions over keyframes wherever reversal can happen mid-flight (checkbox dash offset, hover follows).
- Hold the latest target as the source of truth during rapid changes (text morph, tooltip travel).
- Restart timers on new triggers; cancel them on user correction (typing clears an error).
- Ignore re-triggers while a one-shot runs (input clear).
- Disable pointer events on closed and closing surfaces immediately.

## 96. Replay and first paint
- Replay idiom: remove the state, force reflow (layout read or double animation frame), re-add.
- Before animating measured geometry: snap with transitions off, reflow, restore.
- Flip entrances on the next animation frame so the transition is not batched away.
- Do not play enter animations or toggle bounces on first page load.

## 97. Scripting budget
- Use per-frame scripting only when an envelope cannot be expressed declaratively (dissolve glow envelope, decaying reel blur).
- Track the pointer on flat, non-transforming wrappers.
- Drive hover-spread states from pointer geometry when gaps between elements belong to no element.

# Part 12 — Reduced motion & accessibility

## 98. Reduced-motion guard
- Every animation gets a `prefers-reduced-motion: reduce` guard; never remove it.
- Drop transitions and animations (or keep opacity only) while preserving final states.
- Show end states fully: success check at opacity 1 with the full stroke; words fully visible.
- Remove filters and blurs; flatten tilt and hover transforms; stop shimmer and loader loops.
- Keep meaningful non-motion feedback: error color and message, like fill, toggle position.
- Skip heavy particle effects and per-word glows entirely.
- Generation overlays fade the element in over `200ms` ease-out instead of drawing.

## 99. Interaction accessibility
- Never convey essential information by hover motion alone; keyboard focus and touch rest in the default state.
- Show tooltips on focus as well as hover; hide on blur.
- Mirror state to accessibility attributes: expanded, selected, checked, status regions, tooltip descriptions.
- Close menus and morph surfaces on outside click and Escape.
- Keep focus in a field while clearing it.
- Hide outgoing duplicate copy and decorative overlays from assistive tech and make them non-interactive.
- Respect hit areas of at least 40×40px (44×44px on touch).

# Part 13 — Recurring techniques & layering tricks

## 100. Recurring values
- Dominant curve `cubic-bezier(0.22, 1, 0.36, 1)` for nearly every open, close, slide, resize, follow, indicator, stroke draw, cross-blur and return.
- Overshoot family `cubic-bezier(0.34, Y, 0.64, 1)` with Y 1.25, 1.35, 1.36, 1.45, 1.96, 3.85 by bounce strength.
- Keyword eases: ease-in-out for in-place swaps, ease-out for tooltips, linear for loops.
- Asymmetry: close ≈ 60–70% of open; clean hover-in, springy release; tooltip slow in (80ms + 150ms) vs instant out (50ms).
- Blur as motion: 1px words, 2px default cross-blur, 3px page and text reveal, 4px soft exits, 10px success entrance.

## 101. Stagger patterns
- Fixed per-index delays: `40ms` text lines, `60ms` streamed words, `70ms` digits, `90ms` reels.
- Exponential falloff by distance: `0.45^d`.
- Baked shuffle tables for twinkles so every element fires once per cycle without clumping.
- Random jitter for particles: `±16deg` angle, about ±22% duration, `0–70ms` delay, re-seeded every play so it never repeats.

## 102. Layering tricks
- Duplicate text in a pseudo-element with `background-clip: text` for glyph-only shimmers.
- Mask-image linear gradients for soft window edges (`22%/78%` reels, `28px` reasoning stream) instead of painted overlays.
- Screen blend for glare and light; multiply for streaks in light mode, flipped to screen in dark mode.
- Vertical-only Gaussian blur for motion streaks, since uniform blur smears sideways.
- Stack swapping layers in one grid cell or slot so swaps never shift layout.
- Split an icon into parts and rotate them about a shared pivot for an "opening" affordance; 2px travel is enough.
- Flip symmetric icons with `scaleY(-1)` and a non-scaling stroke instead of morphing paths.
- Animate fr-row interpolation for intrinsic-height expansion.
- Encode stack depth as stepped translate, scale, fade and blur per index.
- Calibrate stroke dash length to the measured path length rounded up by 1.
- Keyframe overshoots explicitly (55% / 80% stops) on top of a springy curve for a tactile double bounce.
- One keyframe plus a delay table yields many loader personalities.

# Part 14 — Anti-patterns

## 103. Timing anti-patterns
- Tuning by nearest number instead of usage; forcing tokens onto mismatched usages.
- Splitting symmetric motions (page slide, tabs, accordion, icon swap, text swap) into open/close timings.
- Bouncing or overshooting a close; delaying a close or hover-out.
- Adding delay to fix motion that feels late; padding slow animations with delay.
- Total stagger over about 300ms; 120ms per-item stagger on long lists.
- Transitions over 1 second on UI chrome.
- Linear easing on surfaces; ease-in on hover; fixed timing functions where direction-aware easing is needed.

## 104. Value anti-patterns
- Pre-scale below about 0.9 on UI chrome.
- Translates over about 40px on non-panel elements; sliding whole screens.
- Blur on plain fades or color/theme changes.
- Unset filter instead of explicit `blur(0)` when cross-blurring.
- Hardcoded stroke dash lengths instead of measuring the path.

## 105. Structure anti-patterns
- `transition: all`; animating height, top, width, padding or margin for hover or layout.
- Overlays popping in or out with no transition; components with no exit or that unmount instantly.
- Animating a single container instead of inner pieces.
- Replaying a reveal in reverse on exit.
- Playing enter animations on first load; a tabs pill animating in from 0; a toggle bounce on load.
- Missing reflow between state removal and re-add; leaving closing states uncleaned.
- Merging error and shake states.
- Letting a status box resize mid-swap.
- Padding on a collapsing grid track.
- Morphing SVG paths for chevrons.
- Tracking the pointer on the tilting element.
- `will-change` on scaled icons or `will-change: all`; transforming inline SVGs directly.
- Multiply-blend glows left on in dark mode.

## 106. Visual anti-patterns
- Same radius on parent and child; geometric centering of asymmetric icons.
- Hard solid borders between sections instead of layered transparent shadows.
- Solid grey hex for tinted areas.
- Tinted-neutral image outlines.
- Accent color on large areas; blue primary buttons.
- Uppercase, letter-spacing, eyebrows or opacity on text.
- Press scale below 0.95; instant press feedback; overlapping hit areas; hit areas under 40×40px.
- Non-tabular changing numbers causing layout shift.

## 107. Generative-UI anti-patterns
- Using a generation animation as a loading state, on tiny inline UI (under about 120px), or on frequently appearing UI.
- Running before fonts, images or layout settle, or on hidden elements.
- Colored generation drawings instead of monochrome.
- Tracing body copy glyph by glyph.
- Forcing log or style panels into dense layouts.
- Durations outside `1600–3600ms` (UI) or `2000–4500ms` (text and image).
- Gating interaction on the animation finishing.
