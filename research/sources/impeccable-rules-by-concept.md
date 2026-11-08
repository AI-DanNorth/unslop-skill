# Design Rules by Concept

Distilled from Impeccable — a design vocabulary for anti-AI-slop frontend work: the craft floor, typography, colour, layout, motion, new-work process, design interventions (bolder, quieter, distill, delight…), critique and audit methods, and the enforced slop-detection rules.

# Part 1 — Design Philosophy & Vocabulary

## 1. Out-of-Distribution Craft
- Work as an award-winning design director would: production-grade output, a clear point of view, a deep grasp of what the client and its users need, and exceptional craft.
- The goal is design that sits outside the statistical average of generated interfaces; the "tasteful default" is the failure mode, not the safe bet.
- When torn between refined and committed, commit.

## 2. Finish the Job
- No hedging, no shortcuts: the deliverable is complete, except assets the person must provide.
- Every brief requirement is present and findable within seconds.
- Ship real content, working controls, and every interaction state, not a static picture of a page.

## 3. Scale Ambition to the Surface
- Persuasive and experiential surfaces get full commitment: bold, distinct work with a point of view.
- Task and reading surfaces show ambition as precision and restraint; patterns the visitor already knows earn their place there.
- Ambition is a property of the surface's mode, not of the product or the designer's mood.

## 4. The Brief Wins
- Honor pinned aesthetics, eras, materials, fonts, and palettes even when they conflict with a saturated-pattern warning.
- Redirecting a clear brief toward your own taste is failure.
- A brief's own words can earn back almost any default on the "refuse" list; your habit cannot.

## 5. Refinement Preserves, Redesign Replaces
- Refinement keeps the incumbent identity, behavior, copy, and everything outside scope.
- Ask before replacing factual copy or adding claims.
- Redesign keeps product truth, content, function, native affordances, and constraints, but treats the old look as evidence and anti-reference.
- In a redesign, choose a whole replacement visual world and replace the documented design system.
- Never split the difference by polishing a look that has been discarded.

## 6. Visual Authority Is Evidence
- A missing written design system does not make a project greenfield; the shipped code, tokens, assets, and screenshots are the visual authority.
- Inspect target and incumbent visual truth before editing anything.
- When the product cannot run, start from committed screenshot or visual-regression references, verify they are current against tokens and components, and compare theme and variant captures.

## 7. Verify by Looking
- Verify by looking at the rendered result at the sizes it ships at.
- Batch the checks: fix everything one look shows before looking again, rather than re-checking after every tweak.
- Every verification answer cites rendered or source evidence; a bare "yes" is not verification.
- A clean automated scan is a floor, not proof of good design.

## 8. Loaded Symbols Stay Out of the Decoration
- A subject's world does not license emblems tied to militarism, supremacy, or hate movements as motifs, badges, or ornament (for example the Rising Sun flag's rays, the Confederate battle flag, Nazi-era insignia and their stylised variants).
- Reach for that world's neutral forms instead.
- Content that documents such a symbol as fact stays as it is.

## 9. The Floor Is Not the Ceiling
- Mechanical quality checks never pick the direction.
- With every check green, spend the page on the committed visual world.

# Part 2 — Visitor Modes

## 10. Persuade
- The visitor decides and acts; design is the product: landing pages, marketing, campaigns, pricing.
- Earn attention and action.
- Ship real imagery when the brief needs it; follow the committed world, not category habit.
- Display type, colour, and motion may carry the voice; composition may be asymmetric, fluid, or intentionally disruptive.

## 11. Operate
- The visitor completes a task: app UI, dashboards, editors, admin, settings, tools.
- Scanability, consistency, native expectations, and the real usage scene outrank expression.
- Brand lives in precise details.
- Predictable structure, stable density, and navigable linearity are affordances.

## 12. Read
- The visitor understands something: docs, articles, guides, help, changelogs.
- Structure for comprehension first, then make the reading experience worth staying in.
- Stability, scanability, and measure come first; a single well-tuned family and a fixed role scale are often right.

## 13. Experience
- The visitor is inside the work itself: portfolios, galleries, showcases.
- Let the artifact lead from the first viewport; the interface recedes.

## 14. Choosing the Mode
- Choose the mode from the requested surface, not the product.
- A tool's landing page is still Persuade; a fashion house's documentation is still Read; a docs index is Read, not Persuade.
- Record the mode per surface, never as a product-wide setting.

## 15. Native Platforms
- On iOS and Android, follow platform conventions for navigation, insets, adaptation, touch targets, type scaling, and Reduce Motion behaviour.
- Do not apply web-only tooling or effects to native screens.

# Part 3 — The Craft Floor (non-negotiables)

## 16. Floor Precedence
- A pinned brief or committed visual world overrides any floor item except a line marked as a ban.
- Build to the floor without announcing the checklist.
- Each floor item is a check on the built result, not an intention.

## 17. Contrast Floor
- Body and placeholder text `≥4.5:1`; large text `≥3:1`.
- On coloured surfaces, tint secondary text from that hue or from the foreground; never grey.

## 18. Depth Floor
- Shadows carry an offset and a soft blur.
- A zero-offset coloured halo is decoration, not depth.

## 19. Spacing Floor
- Tight groups, generous separation.
- More space above a heading than below it.
- Read the computed values rather than trusting the intent.

## 20. Type Floor
- Body measure `65–75ch`.
- Display size max `6rem`.
- Tracking floor `-0.04em`; `-0.02em` to `-0.03em` usually reads better.
- Balanced headings; obvious steps in scale and weight.
- Run the real copy at every breakpoint and fix anything that overflows.

## 21. Motion Floor
- One authored moment, not scattered effects and not one identical entrance on every section.
- Exponential ease-out from an already-visible default state.
- Reach past transform and opacity: blur, backdrop-filter, clip-path, mask, and shadow belong to the palette when they stay smooth.

## 22. States Floor
- Hover, disabled, loading, error, and empty states all exist.
- Plus real content, working controls, responsive composition, and keyboard focus.

## 23. Browser Surfaces
- The parts you did not draw still carry the design: text selection, the caret, custom scrollbars, focus rings, underline offset, and numerals in tabular data.
- All of these ship with browser defaults that belong to no design system; theme them from the palette.
- This is the cheapest signal that a page was built rather than assembled, and the one most reliably skipped.

## 24. Copy as Design Material
- Use the product's own language.
- Controls name their action.
- Errors name the problem and the recovery.

## 25. Elevation Declared Once
- Declare elevation once: a border or a shadow, not both.
- A `1px` border under a wide soft shadow is the "ghost card".
- Card radii stay at `12–16px`; pills are for small controls.

## 26. Material Honesty
- Claims and configuration come from supplied truth; label illustrative values honestly.
- Never invent testimonials, customers, benchmarks, pricing, licensing, or deployment facts.
- Naming a concept and then ironizing it is not a claim.

# Part 4 — AI-Slop Tells

## 27. Reading the Refuse List
- These are the category's defaults, not absolute bans: the brief's own words can earn any of them back (except where marked as a ban).
- Reaching for one when the axis is free means you were not deciding.
- Recognising one means rewriting the element, not softening it.

## 28. The Generic Default Page
- Inter for everything.
- Purple-to-blue gradients.
- Cards nested in cards.
- Grey text on coloured backgrounds.
- A rounded-square icon tile above every heading.
- The "tasteful default": cream page, thin serif, italic accent, pill buttons, flat vector illustrations in rounded cards.

## 29. Identical Card Grids
- Same-size cards of icon plus heading plus text as the page structure.
- Cards are the lazy container.
- Nested cards are always wrong.

## 30. The Hero-Metric Template
- Big number, small label, supporting stats, accent colour: refuse it as a reflex layout.
- Sparkline decorations and "boost your productivity" copy belong to the same cliché family.

## 31. Eyebrows Above Headings (ban)
- A kicker or eyebrow label above a heading is a ban; no brief earns it back.
- The heading carries its own weight: delete the label and let the heading speak.
- Eyebrows on every section read as machine scaffolding.

## 32. Numbered Section Markers
- No `01 / 02 / 03` section numbers unless the sequence itself carries information the reader needs.

## 33. Modal by Reflex
- No modal for a task that needs neither interruption nor protected focus.

## 34. Gradient Text
- No gradient-filled text; emphasis comes from weight or size.

## 35. Decorative Glass
- No glass and blur as decoration rather than as a specific effect.
- Glassmorphism, glowing particles, neon accents, and cyan-on-black are generic AI-tool marketing.

## 36. Side-Stripe Borders
- No coloured `border-left` or `border-right` above `1px` on cards, list items, callouts, or alerts.

## 37. Hard Offset Shadows
- No hard offset shadows (`box-shadow: 4px 4px 0`) outside a world that is actually neobrutalist.
- The zero-blur block shadow is a costume, not a depth system; a world that did not choose it never earns it as a default.

## 38. Decorative Chrome Standing In for Content
- No sparklines, progress rings, or soft-shadowed rounded rectangles standing in for content.

## 39. Monospace as Costume
- Monospace is for code, data, or measurement, never a costume for "technical".

## 40. System Display Faces
- No system display face (Impact, Arial Black, the platform sans) as the display voice of an own-world page.
- Source and self-host a face whose character matches the approved lettering; the closest installed font is a failure, not a fallback.

## 41. Glyph Icons
- No Unicode glyphs or emoji standing in for an icon system.
- Icons are drawn, from a real library or authored SVG, in one consistent stroke and weight.

## 42. Geometric Occlusion Masks
- No circle, polygon, or radial-gradient cutout approximating a photographic subject's edge; it reads worse than omitting the effect.
- Derive an alpha matte from the actual image, or produce a cut-out asset.

## 43. Theme by Habit
- Do not pick light or dark by product category.
- Pick it from the use scene: who, where, and under what ambient light.

## 44. Sketchy Illustration
- Real illustration or none.
- Sketch-style SVG scenes, "doodle" treatments, and turbulence-noise grain read as amateur.
- This bans SVG imitating pictures, never SVG doing geometry: crisp vector shapes, diagrams, animated linework, and shader effects remain first-class media.
- A shaded, perspectived, or figure-bearing illustration is a picture even in line-art style; geometry means shapes that can be specified exactly.

## 45. Fake Background Texture
- Backgrounds are surfaces, textured only from the subject's world.
- `repeating-linear-gradient` stripes and two-axis grid overlays need an actual canvas, map, blueprint, or measuring tool under them.
- No synthetic dot rails, fake dust strokes, or pseudo-circuit motifs that create rendering artifacts.
- No decorative calibration marks that do not align with real content.

## 46. Motion Slop
- One identical fade-and-rise entrance on every section.
- Generic hover lift, parallax layers, and scroll reveals presented as a concept.
- Bounce and elastic easing by reflex.

# Part 5 — Typography

## 47. Typographic Authority and Fit
- Identify which faces, weights, and roles are established, and whether they fit the product and world or are unexamined defaults.
- Every family must be necessary; never introduce a second family without a clear role only it can perform.
- Improve typography inside the established world; replacing faces that would create a new identity is a redesign.

## 48. Role-Based Hierarchy
- Heading, body, label, metadata, and data roles must be distinguishable at a glance, without reading the copy.
- Adjacent sizes or weights that are too close cannot carry different jobs.
- Combine size, weight, space, and tone deliberately instead of asking size alone to do all the work.
- Use the fewest roles and families that make the hierarchy unmistakable.

## 49. Setting the Type System
- Before editing, state the roles needed, the intended contrast between them, the reading measure and density, the authoritative faces and weights, and performance, localisation, and accessibility constraints.
- Name role tokens by purpose, not by value.
- Keep repeated roles identical across screens and states.

## 50. Enumerated Type Ramp
- Use a deliberate, enumerated scale, not a collection of arbitrary values.
- Adding a step is a design decision, not a convenience.
- Near-identical sizes that no reader can tell apart (e.g. six steps between `13.7px` and `15.4px`) are noise; collapse them.
- Only fluid display roles may land between steps.

## 51. Body Size and Measure
- `1rem` / `16px` is the ordinary web body floor unless a dense role, platform convention, or user setting justifies otherwise.
- Keep prose in the `45–75ch` range.
- Tune line height inversely with measure: wider lines need more leading.
- Tune line height to the face, width, language, and contrast, not a universal ratio.

## 52. Light Text on Dark
- Compensate on all three perceptual axes: slightly more line height, a touch more tracking, and one step more weight when the face needs it.
- Long copy on dark surfaces needs air: line-height `1.65` to `1.8`, max width `65` to `75ch`.

## 53. Responsive Display Type
- Marketing display type may respond to available space (`clamp()`), when useful.
- Keep dense product and reading surfaces spatially predictable.

## 54. OpenType and Numerals
- Use numeric, tabular, code, and label features when the content benefits.
- Tabular data gets tabular numerals.

## 55. Font Delivery
- Load only the font assets and weights actually used.
- Provide metric-compatible fallbacks; avoid invisible text and disruptive reflow during loading.
- Stress-test with missing weights and font fallback.

## 56. Accessible Type
- Preserve browser zoom, user font settings, Dynamic Type, and platform text scaling.
- Stress-test long headings, localisation expansion, zoom, and narrow containers.

## 57. Paragraph Rhythm
- Use paragraph spacing or first-line indentation as the paragraph signal, not both; combining them double-marks the boundary.

## 58. Line Breaks
- `text-wrap: balance` on headings and short centred blocks; `text-wrap: pretty` on body copy (both progressive).
- `pretty` pulls a word down beside a lone last word; it does not fill the last line, and a two-word tail is fine.
- In a column too narrow for either to help, edit the copy or widen the column.
- Break a heading by hand only between phrases, and check the break at every width; a hard break landing mid-line on a phone is worse than the default wrap.
- An uneven break can carry meaning (a headline landing on one word, a poster line, a pull quote): make it deliberate and keep it rare.

## 59. Tracked Caps
- Tracked uppercase labels are for short system markers only.
- Never write full sentences in tracked caps.

## 60. Type Never Decorates at Comprehension's Expense
- Do not make type decorative at the expense of comprehension.

# Part 6 — Layout & Spacing

## 61. Diagnose Before Moving Boxes
- Layout turns product priority into reading order, grouping, rhythm, and usable space; diagnose the structural problem first.
- Layout work changes structure inside the established world; identity replacement is a redesign.

## 62. The Squint Test
- With detail blurred, you can still identify the primary element, the secondary element, and the major groups, in order.

## 63. Grouping by Proximity
- Group by meaning; use proximity before adding containers or decoration.
- Watch for containers compensating for weak proximity.
- Keep distinct content visually distinct without turning every group into an isolated component.

## 64. Rhythm Through Contrast
- Create cadence through deliberate contrast between tight and generous intervals.
- One spacing value repeated everywhere gives everything equal weight.

## 65. Spacing Scale
- Use a documented spacing scale rather than one-off values.
- A `4`-unit base provides the useful middle steps an `8`-only scale misses.
- Use `gap` for sibling rhythm when it expresses the relationship more directly than child margins.

## 66. Structure Matches Content
- The topology must match the content and task; repeated cards, columns, or sections must be genuinely equivalent, not a framework default.
- Hierarchy follows product priority, not framework defaults.
- Choose the simplest structural model that expresses the relationships.

## 67. Spatial Thesis
- Before editing, name the primary reading or task path; what belongs together and what separates; which element leads and which supports; the intended density and rhythm; and how structure changes across containers, viewports, input modes, and content extremes.

## 68. Density
- Information per region fits use frequency, decision complexity, and visitor mode.

## 69. Structural Responsiveness
- Reorder, collapse, reflow, or reveal based on what remains important; responsive behaviour is structural, not just shrinking.
- Prefer container-aware components when the same component appears in different contexts.
- Check narrow, intermediate, wide, zoomed, and localised states.
- DOM, focus, keyboard, touch, and assistive-technology order must agree with visual order.

## 70. Extremes and Edge Cases
- Test long content, empty states, overlays, sticky elements, safe areas, and small touch targets for structural failure.
- Keep touch targets usable even when their visible marks are small.

## 71. Depth and Optical Correction
- Use depth only when it clarifies state or hierarchy.
- Make optical corrections only after inspecting the rendered result.

## 72. Repetition and Variation
- Variation is not a goal by itself.
- Repetition supports recognition; break it only when content or priority changes.

## 73. Grouping Without Nested Cards
- Group 2 to 6 items with a bento: a 12-column grid with tile spans (e.g. `8/4`, `6/6`, `4/8`) and tight gutters (`8px`) on a single plinth, instead of nesting cards.
- No wide rounded cards; keep cards compact, flat, and sharply bounded.

# Part 7 — Colour

## 74. Colour Has a Job
- Introduce colour as hierarchy, meaning, and atmosphere.
- Decoration without a relationship to hierarchy, state, content, or the visual world is not a colour strategy.
- Preserve confirmed brand and semantic conventions; adding colour is not a licence to replace the identity.

## 75. Colour by Mode
- Persuade and Experience: colour may carry the voice and own large regions.
- Operate and Read: colour encodes action, selection, status, wayfinding, and reading hierarchy; rarity gives an accent force.

## 76. Audit Before Choosing
- Identify confirmed brand colours; current surface, text, action, and semantic roles; places where greyscale obscures hierarchy or state; contrast failures and colour-only communication; light/dark and data-visualisation needs.

## 77. Name a Strategy
- Before editing, name the emotional temperature, dominant relationship, contrast range, and colour dosage.
- The strategy follows the brief and world, not a fixed percentage rule (no reflexive 60-30-10).

## 78. Roles, Not Swatches
- Canvas and elevated surfaces.
- Primary and secondary text.
- Action, focus, and selection.
- Borders and separators.
- Success, warning, error, and information.
- Data categories or scales when needed.
- Define primitive values plus semantic tokens; theme changes remap semantic roles.

## 79. Hue From Meaning
- Choose hue from product meaning and visual direction, never from a default category association.
- For a new web palette, prefer OKLCH: lightness and chroma adjust predictably.
- Otherwise use the project's existing colour space.

## 80. Dose the Strongest Colour
- Let the strongest colour own a deliberate region or role instead of scattering tiny accents.
- Keep the primary action easy to find; do not spend its colour on decoration.

## 81. Neutrals
- Tint neutrals only when the brand hue genuinely creates cohesion; neutral grey is valid when it serves the world.
- Never pure black or pure white as surfaces.
- On coloured surfaces, derive secondary text from the foreground or surface hue, not washed-out generic grey.

## 82. Semantic Consistency
- Keep semantic meanings consistent, but respect platform and domain conventions instead of assuming fixed hues.

## 83. Contrast Minimums
- Body text `4.5:1`.
- Large text `3:1`.
- Controls, icons, and focus indicators `3:1`.
- Verify computed pairs, never eyesight alone: interactive states, overlays, text on images, disabled content, both themes.
- Simulate common colour-vision deficiencies.

## 84. Never Colour Alone
- Information conveyed by colour also needs text, shape, iconography, or position.
- In data, separate series with distinct lightness, chroma, shape, label, or pattern.

## 85. OKLCH Ramps
- Vary lightness and reduce chroma near white and black.
- Do not keep high chroma at extreme lightness just to make the math uniform.
- Prefer explicit colours over chains of translucent overlays when alpha would make contrast context-dependent.

## 86. Dark Mode Composition
- Design dark-mode surface elevation and contrast explicitly; never invert the light theme mechanically.
- Light and dark themes are each composed.

## 87. Colour Verification
- Every colour has a stable role or a world-specific atmospheric purpose.
- Attention lands on the intended action, content, or state.
- The palette holds across quiet, dense, interactive, error, and empty states.
- The result is recognisably this product, not a generic "colourful" treatment.

# Part 8 — Motion

## 88. Motion Has a Job
- Motion explains state, relationship, and hierarchy, or creates one authored moment the surface has earned.
- Decoration without purpose is animation debt.
- Do not animate a static area merely because it exists.

## 89. Where Motion Belongs
- Acknowledge an action.
- Make a state change or spatial relationship legible.
- Preserve continuity through navigation or layout change.
- Direct attention at a meaningful moment.
- Embody the selected visual world.

## 90. Motion by Mode
- Persuade and Experience: motion may carry the voice; prefer one rehearsed focal sequence to repeated section reveals.
- Operate and Read: motion serves feedback, state, and continuity; keep routine transitions fast and never make users wait through page-load choreography.

## 91. Motion Thesis
- Focal moment: the one sequence or interaction that deserves authorship, if any, drawn from this product and surface concept.
- Continuity: the state, layout, or navigation changes that need explanation.
- Feedback: the controls and outcomes that need acknowledgement.
- Budget: which effects are expensive and how often they run.
- A generic fade-and-rise, hover lift, parallax layer, or scroll reveal is not a thesis.

## 92. Material by Meaning
- Continuity and relationship: shared-element motion, FLIP transforms, view transitions, deliberate spatial movement.
- Focus and depth: bounded blur, filter, backdrop, light, or shadow changes.
- Reveal and composition: masks, clip paths, cropping, controlled occlusion.
- Material and energy: colour, gradient position, texture, distortion, or shaders where world and runtime support them.
- State and feedback: the smallest change that makes cause and result unmistakable.
- Do not stack techniques for spectacle; one strong material idea carried through the focal sequence is usually enough.

## 93. Stagger
- Sibling stagger is appropriate when a list appears as a list.
- Cap the total delay.
- Never reinterpret every scrolled section as a staggered list.

## 94. Duration Scale
- `100–150ms`: immediate feedback.
- `150–300ms`: routine state change.
- `300–500ms`: layout, overlay, or view transition.
- `500–800ms`: a deliberately authored focal entrance.
- Long feedback feels like latency.

## 95. Easing
- Exit faster than entrance.
- Natural deceleration for confident arrivals: `cubic-bezier(0.16, 1, 0.3, 1)`.
- No bounce or elastic curves by reflex.
- Hover: slight upward transform or brightness shift; no bounce.

## 96. Implementation Choices
- CSS transitions and keyframes for declarative state and bounded sequences.
- Web Animations API or the existing motion library for interruption, sequencing, and dynamic values.
- View Transitions or shared-element techniques when continuity across states is the point.
- Scroll-driven motion only when the scroll relationship itself carries meaning, with a solid fallback.
- Do not add a dependency for an effect the existing stack can express cleanly.

## 97. Performance Hygiene
- Keep content visible in the default state so a failed script never hides the page.
- Avoid animating layout-driving properties (`width`, `height`, `top`, `left`, margins); use FLIP, transforms, or grid techniques.
- Bound blur, filter, shadow, canvas, and shader work to isolated regions.
- Apply `will-change` only during a known animation.
- Measure on target devices; do not assume transform means fast.

## 98. Reduced Motion and Control
- Every web animation needs a `prefers-reduced-motion` path with an intentional alternative.
- Reduce or remove spatial movement while preserving opacity, colour, and state transitions that carry meaning.
- Reduced motion means fewer and gentler animations, not disabling all motion; confirming feedback stays legible.
- Respect autoplay and sound preferences; nonessential loops stop when offscreen or hidden.

## 99. Motion Verification
- Interruption and repeated use behave correctly.
- Removing an animation would lose meaning or authored character, not merely decoration.
- Expensive effects stay smooth on the target device.

# Part 9 — Shaping a Brief Before Building

## 100. Discovery Before Direction
- Do not write code or choose visual direction until the job is understood.
- Ask two or three related questions per round, then wait; one round is the default.
- Do not dump a questionnaire, repeat settled facts, or turn obvious facts into menus: assert the likely reading and invite correction.
- A sparse prompt requires at least one answer round; a precise prompt may need only a compact confirmation.
- Never ask for CSS values or canned aesthetic lanes.

## 101. Purpose, People, Outcome
- What is the surface for, and what problem must it solve?
- Who reaches it, in what situation and state of mind?
- What must they understand or do, and what does success look like?
- What is uniquely true here that a neighbouring product or generic template could not claim?

## 102. Material, Behaviour, Boundaries
- What real content, evidence, data, and assets must it carry, with realistic minimum, typical, and maximum ranges?
- Which states matter: first-run, empty, loading, error, success, permissions, overflow, expert use?
- What fidelity, breadth, and interactivity are intended?
- What must remain untouched, and what would make it feel wrong even if polished?
- Which platform, performance, accessibility, localisation, or delivery constraints are binding?

## 103. The Smallest Useful Brief
- Job and audience, including visitor mode.
- Outcome and proof: primary action, success, real evidence, product-specific truth.
- Selected direction: visual authority, structural/interaction thesis, sequence, focal moment.
- Scope and boundaries, including explicit anti-goals.
- States and content ranges.
- Interaction and layout intent (hierarchy, topology, responsiveness, feedback), not CSS.
- Constraints and open decisions a builder must not invent.
- Use three to five bullets when the task is settled; the full structure only for ambiguous or multi-screen work.
- Mark assumptions plainly when no one can answer.

# Part 10 — Routing a Design Request

## 104. Make It Bolder
- For safe, bland, or forgettable designs: amplify scale contrast, colour commitment, and point of view.

## 105. Make It Quieter
- For aggressive or overstimulating designs: tone down competing accents, effects, and noise.
- Also the fix for slop families like gradient text and decorative glow.

## 106. Distill
- For cluttered surfaces: strip to the essence and remove what the page does not need.

## 107. Colourise
- For a flat, grey, or monochromatic interface: add strategic colour as role and hierarchy.

## 108. Typeset
- For weak hierarchy, wrong fonts, or arbitrary sizing; also the fix for eyebrow and tracked-label slop.

## 109. Fix the Layout
- For broken spacing, rhythm, grouping, or reading order.

## 110. Animate
- For missing transitions and interaction feedback; adds purposeful motion.

## 111. Add Delight
- For correct but personality-free surfaces: add memorable, product-specific touches.

## 112. Overdrive
- For surfaces that have earned spectacle: shaders, spring physics, scroll-driven effects, pushing past conventional limits.

## 113. Clarify
- For unclear UX copy, labels, and error messages.

## 114. Harden
- For production readiness: errors, internationalisation, overflow, and edge cases.

## 115. Adapt
- For different devices, screen sizes, and input modes.

## 116. Optimize
- For slow loading and rendering performance.

## 117. Onboard
- For first-run flows, empty states, and activation.

## 118. Polish
- The final quality pass before shipping; the natural hand-off after any focused intervention once its job holds.
- The right move when a review scored low or found blocking issues.

## 119. Critique vs Audit
- Critique: a UX design review scored against usability heuristics, ranking what to fix first.
- Audit: a technical quality report (accessibility, performance, theming, responsive behaviour) with findings ranked from `P0` (blocking) to `P3` (polish).
- A surface that has never been reviewed is a strong candidate for critique first.

## 120. Planning and System Capture
- Plan UX before building when the job, audience, or states are unclear.
- When code exists but no visual system is documented, capture it first so changes stay on-brand.
- Extract repeated patterns into reusable tokens and components.

## 121. Routing Heuristics
- Scope the intervention to the changed surface; narrow targets beat whole pages reviewed at a glance.
- Many contrast or quality problems point to an audit or a polish pass.
- A specific slop family points to its matching move (gradient text or eyebrows to quieter or typeset; flat grey palette to colourise).
- Recommend two or three pointed next moves with one-line reasons; never act on a recommendation without confirmation.
- If two interventions fit, ask once.

# Part 11 — A Worked Design System (Neo Kinpaku)

## 122. North Star
- "Neo Kinpaku": a dark lacquer interface marked by Japanese gold leaf and precise technical geometry.
- It should feel like a crafted object: black urushi, irregular kinpaku seams, quiet measurement marks, circuit traces, controlled verdigris oxidation.
- Refined, technical, physical; expensive and deliberate, but still useful.
- Restraint in chrome, brilliance in texture.
- Explicitly rejects: italic serif hero, magenta accent, generic AI-tool neon.

## 123. Brand Anchors
- Kinpaku Gold `oklch(84% 0.19 80.46)`: primary accent; CTAs, active state, wordmark, key rules, focus.
- Verdigris Patina `oklch(70% 0.12 188)`: secondary accent; improved states, live indicators, hover emphasis, contrast point.
- Dark Ink `oklch(14% 0.018 95)`: foreground on gold; never theme-remapped.

## 124. Surfaces (Dark)
- Lacquer Black `oklch(7% 0.006 95)`: page ground; warm and mineral, not neutral black.
- Lacquer Deep `oklch(4% 0.004 95)`: deepest insets and footer.
- Raised Lacquer `oklch(11% 0.006 95)`: panels, cards, demo frames.
- Graphite `oklch(15% 0.008 95)`: inputs, inactive tiles.
- Graphite 2 `oklch(19% 0.008 95)`: one step above graphite; pills and inactive chrome.

## 125. Text Tiers
- Champagne `oklch(91% 0 0)`: headlines, strong, important labels.
- Body `oklch(88% 0 0)`.
- Muted `oklch(72% 0 0)`: captions, meta.
- Faint `oklch(62% 0 0)`: subdued labels.
- Mute Deep `oklch(52% 0 0)`: disabled.
- Text carries no warmth at any tier; warmth lives in accents and surfaces.

## 126. Gold Ramp
- Pale `oklch(86% 0.07 84)`: hover lift, pale fills.
- Rich `oklch(77% 0.13 82)`: active CTA, severity-medium.
- Deep `oklch(61% 0.085 78)`: borders, subdued icons, large diagrams.
- Rule `oklch(78% 0.12 82)`; Rule Rich `oklch(77% 0.14 82)` as alpha bases.
- Glints for leaf texture: `oklch(95% 0.04 84)`, `oklch(98% 0.04 84)`, `oklch(94% 0.07 82)`, `oklch(98% 0.035 84)`.
- Default hairline `oklch(78% 0 0 / 0.16)` (neutral); strong hairline `oklch(74% 0.09 82 / 0.6)` (gold) for active borders and focus.

## 127. Patina Ramp and State
- Patina Pale `oklch(82% 0.07 188)`; Patina Deep `oklch(49% 0.08 188)`; Patina Rule `oklch(70% 0.105 190)`; Patina Text `oklch(76% 0.088 190)`.
- Vermilion Warning `oklch(58% 0.15 35)` (light variant `oklch(52% 0.16 35)`): errors and anti-pattern warnings only, sparingly.
- Success `oklch(45% 0.18 145)`, on paper `oklch(40% 0.10 145)`, soft `oklch(95% 0.05 145)`.

## 128. Light Theme (Paper)
- Paper `oklch(97% 0.012 95)`; deep `oklch(94% 0.014 95)`; raised `oklch(99% 0.008 95)`.
- Ink `oklch(18% 0.02 95)`; text `oklch(25% 0.018 95)`; muted `oklch(45% 0.015 95)`; faint `oklch(55% 0.012 95)`; disabled `oklch(65% 0.01 95)`.
- Gold is gated by size on paper: large display accents stay gold, but body- and label-size gold fails contrast and is never used.
- Small accents, links, active nav, and inline code switch to patina deep `oklch(49% 0.08 188)`; small labels fall back to muted ink.

## 129. Colour Rules
- Gold carries brand: if a single accent must represent the brand, it is gold.
- Patina has meaning: improvement, live state, or contrast against gold; never generic decoration.
- Texture budget: leaf and patina textures only on brand-bearing moments (hero seams, CTA fills, dividers, major swatches); generic cards stay flat.
- OKLCH only for new colours; hex only in third-party or imported assets.
- Never hand-type colour values or font sizes outside the token set; a missing value is either a token to add or a deliberate bespoke moment.

## 130. Type Faces
- Display: Alumni Sans (fallbacks Albert Sans, Arial, sans-serif), a thin hairline cut.
- Body and UI: Albert Sans (fallbacks Avenir Next, Helvetica Neue, Arial, system-ui).
- Mono: SFMono-Regular, Roboto Mono, Consolas.

## 131. Type Roles
- Wordmark: Alumni Sans, `400`, uppercase, `1.125rem`, tracking `0.15em`, line-height `1`.
- Display h1: `clamp(3.4rem, 6.5vw, 5.6rem)`, weight `100`, line-height `1.02`, tracking `-0.01em`.
- Headline h2: `clamp(2.6rem, 4vw, 3.4rem)`, weight `300`, line-height `1.04`.
- Title h3: Albert Sans `1.125rem`, `500`, line-height `1.35`.
- Body: Albert Sans `1rem`, `400`, line-height `1.8`.
- Eyebrow: mono `0.6875rem`, `500`, uppercase, tracking `0.18em`.
- Mono label: mono `0.6875rem`, `500`, tracking `0.22em`; categories, nav metadata, table headers.

## 132. Type Ramp
- Steps (px at a 16px root): `8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 24, 28, 32, 40, 48, 56, 64, 72, 80, 88`.
- `11` eyebrow/tag; `12` meta and inline code; `14` dense body and controls; `16` default body; `18` lead; `20` card titles; `24` subsection; `28–32` section heads; `40–88` display.
- Every literal size lands on a step (tolerance `±0.5px`); only fluid display roles fall between.

## 133. Type Rules
- Weight inversion: section h2s (`300`) read heavier than the hero h1 (`100`) so the hero breathes and sections are grounded; never normalise them.
- Two faces: the thin display cut never goes below `1.2rem`; smaller text uses the body face.
- Wordmark holds weight `400` because the thin cut reads too light at lockup size.

## 134. Spacing Scale
- `8px`, `16px`, `24px`, `32px`, `48px`, `80px`, `112px`.
- Section container max-width `1320px`.

## 135. Radii
- `0`, `2px`, `3px` (code), `4px`, `5px`, `6px`, `7px`, `8px`, `10px`, `12px`, `14px`, `16px`, pill `999px`.
- Small radii throughout; buttons `2px`, cards and inputs `4px`.

## 136. Elevation and Material
- Mostly flat; depth comes from material contrast, hairline borders, texture, and subtle inset light.
- Panel setback: `0 24px 70px oklch(2% 0.004 95 / 0.42)`, large framed modules only.
- CTA lift: `0 18px 48px oklch(2% 0.004 95 / 0.4)` plus a small inset highlight.
- Patina glow: `0 0 22px oklch(70% 0.105 190 / 0.24)`, tiny live indicators only.
- No default card shadow; hairline first, `1px`, before any shadow.
- No glass: translucency only in overlays, never decorative blur panels.
- Text never sits directly on high-contrast leaf texture; add a lacquer veil or move texture to an edge.
- Brand-bearing material (leaf, dust, oxidation) uses raster or generated assets, not hand-drawn SVG approximations; code geometry is for hairlines, grids, and UI structure.

## 137. Buttons
- Primary: gold fill or leaf texture, dark ink text, `1px` border, `2px` radius, min-height `58px`, padding `0 38px`; hover to Kinpaku Pale.
- Secondary: transparent, gold text, strong gold hairline border; secondary actions only.
- Ghost: text-only gold.
- Hover: slight upward transform, brighter gold, or patina border; no bounce.
- Focus: patina outline with `4px` offset.

## 138. Inputs, Cards, Navigation
- Input: Lacquer Deep fill, champagne text, default hairline border, `4px` radius, padding `14px 16px`.
- Card: Raised Lacquer, body text, default hairline border, `4px` radius, `24px` padding; compact, flat, never nested.
- Nav link: champagne at rest, gold on hover.

## 139. Tool Chrome
- Floating tool bars: Lacquer Deep always, `1px` neutral hairline `oklch(92% 0 0 / 0.13)`, radius `8px`, shadow `0 16px 36px -12px oklch(0% 0 0 / 0.6)`, no gold halo.
- Gold reserved for the brand mark and active control, not the container outline.
- Active toggle: neutral graphite pill `oklch(27% 0 0)` with gold text; exit hover in vermilion.

## 140. Proof Objects and Signature Moments
- A before/after comparison is a proof object: dark grid field, straight gold seam, gold handle, readable labels; the "before" side may show slop colours, the frame stays in-system.
- Dividers carry brand only with real leaf, dust, or verdigris texture; otherwise straight hairlines.
- The footer may carry the strongest oxidation accent: gold seam plus patina edge as a final signature.
- Calibration and circuit geometry is structure, especially around product proof, and must align with real content.

## 141. Component Reuse
- Reach for an existing primitive before inventing a class; group with the bento, not new card types.
- Section scaffolding: container, header, heading, subhead; an eyebrow is optional and skipped where per-section eyebrows read as scaffolding.
- Invent only when the system truly lacks the shape, and flag recurring inventions for promotion into the system.

# Part 12 — Product Principles

## 142. Practice What You Preach
- A design product's own site must pass its own anti-pattern tests; shipping anything it would flag is a loss.

## 143. Show, Don't Tell
- Demonstrate quality through execution, not words about quality; the site is the demo.
- The visual system must never hide the product proof: demos, sliders, audit tables, examples, docs, and pricing stay understandable.

## 144. Expert Confidence
- Direct, opinionated, decisive; no hedging.
- Personality: expert, decisive, editorial.
- Direct (no "maybe consider"), specific (no "improve the vibe"), rooted in craft (no hype).

## 145. Editorial Over Marketing
- Feel like a design publication rather than a SaaS landing page: long-form reading, considered typography, breathing room.
- Avoid hero-metric layouts, identical-card feature grids, sparkline decoration.
- Do not educate people who already know they have the problem; solve it.

## 146. Purposeful Restraint
- Every element earns its place; nothing decorative without function.
- Nothing included because "landing pages usually have that".

## 147. Accessibility Baseline
- WCAG 2.1 AA on all pages.
- Contrast verified with real checks, not eyeballing.
- All interactive elements keyboard-navigable with visible focus.
- `prefers-reduced-motion` respected for every animation.
- Semantic HTML first; ARIA as a supplement, never a workaround.
- Copy readable at an 8th-grade level; jargon only when precisely needed.

## 148. Narrow Targets
- A single section reviewed closely beats a whole page at a glance.
- Design is strongest when iterating on interfaces that already exist.

# Part 13 — Copy Voice

## 149. Make It Specifically Yours
- For every paragraph, point to the sentence that makes it specifically yours; if you cannot, it is generic by default.
- Swap the product name for a competitor's: if nothing becomes false, the copy is interchangeable.

## 150. Openings and Closings
- Open with the reader's wrong belief, your strongest claim, or the example; no "in this guide", no "let's dive in".
- Close by handing off the next move; do not summarise. End on the strongest sentence, a directive, or just stop.

## 151. Position and Specificity
- Take a position someone could disagree with; if the paragraph inverts without changing meaning, it has none.
- Name names, use numbers: write "54 KB", not "lightweight".
- Replace hollow confidence ("powerful") with a concrete fact.
- Write the recommendation instead of synthetic pros-and-cons balance.

## 152. Sentence Craft
- Verbs lead; active voice; cut nominalisations.
- Vary sentence length on purpose (long, long, short); uniform rhythm is the deepest AI tell.
- Allow fragments for rhythm.
- Plain words; technical terms only where something rests on them.
- Prose carries arguments; bullets only for parallel options.
- Concrete over comprehensive; leave things out.
- Read it aloud and fix anything you stumble over.

## 153. Banned Diction
- "load-bearing", "highest-leverage", "biggest unlock", "data-driven", "reflex defaults".
- "seamless", "robust", "elevate", "empower", "underscore", "pivotal", "tapestry", "delve".
- "in today's…", "gone are the days", "whether you're…", "let's dive in", "in summary", "in conclusion", "moreover", "furthermore".

## 154. Banned Punctuation
- No em dash (`—`); pick the real relationship with comma, colon, semicolon, period, or parentheses.
- No double hyphen ` -- ` as a substitute.

## 155. Structural Tells
- Negation pivots ("It's not just X, it's Y"); replace with a direct positive claim.
- Triadic everything; vary list counts to 1, 2, or 4.
- The five-paragraph essay shape on every page.
- Uniform paragraph length; insert a four-word sentence or a one-line paragraph.
- Stacked hedges ("it might potentially be useful to consider").

# Part 14 — Starting New Work: Discovery & Brief

## 156. Decide What Is Already True
- Before designing anything new, review the existing design system record, representative screens, tokens, components, and assets.
- Classify the situation first: redesign, established world, incomplete brand, or no visual authority. Each demands a different amount of invention.
- Product truth (purpose, content, function, constraints) and durable visual decisions are separate authorities; keep surface-specific strategy separate from both.

## 157. Redesign Posture
- Preserve product truth, content, function, constraints, and explicit brand commitments.
- Replace the old visual world rather than polishing it.
- Treat the old look as evidence of what the subject is, not authority over what it becomes.

## 158. Established World Posture
- When a coherent identity already exists in the built product, inherit it, even if it was never written down.
- Document an undocumented coherent identity instead of inventing a replacement.

## 159. Incomplete Brand Posture
- Preserve confirmed assets and recognizable traits.
- Expand the system together with the stakeholder for the surface in hand.

## 160. No Visual Authority
- When nothing visual is established, create a new world together with the stakeholder; never alone and never by default.

## 161. Local Additions Inherit
- A section, component, feature, or state inside an established surface inherits that surface.
- Never turn a local addition into a new identity exercise.

## 162. Ask What Will Change the Work
- Before implementation, ask two or three related questions; a precise request needs only a compact confirmation.
- Skip settled facts, but never skip the confirmation: a settled visual system does not settle this surface's purpose or concept.
- Across all modes, ask what success looks like, what must remain untouched, and what would make a polished result feel wrong.
- Never ask stakeholders for CSS values or canned aesthetic lanes ("minimal or bold?").

## 163. Surface Modes
- Identify the surface's mode before designing; it governs what the opening must do and how far the world may reach into the page.
- **Persuade**: ask who must act, what they should believe, and which real proof, content, or assets earn that belief.
- **Operate**: ask about the task, information, important states, frequency, and constraints.
- **Read**: ask about the reader's question, source material, structure, and wayfinding.
- **Experience**: ask what leads, how exploration unfolds, and which interaction or transition matters.

## 164. Choose the Right Amount of Invention
- Match invention to scope: extending a surface, creating a whole surface in an established world, and creating or replacing a world are three different processes.
- Never run a concept tournament for a local extension or a precisely specified narrow request; shape those directly.

## 165. Extending an Existing Surface
- Inherit its world and its composition.
- Resolve only the new purpose, content, hierarchy, states, interaction, and how the addition joins the surrounding experience.
- Do not change the durable design system unless the stakeholder approves a durable system change.

## 166. Whole Surface Inside an Established World
- Keep the visual system fixed; vary only composition.
- Derive five to seven materially different structures from the content, task, and user behavior, ordered by resonance.
- Use a random draw to choose which three reach the stakeholder, breaking the habit of always showing your top-ranked idea while still giving a real choice.
- Present the three as full cards of equal salience, with options to steer or re-draw; every card visualizes composition, not identity.
- Anchor any visual comp of the new surface on a screenshot of a representative existing page; prose paraphrases of a design system drift, pixel references do not.
- Without image generation, give each card an HTML sketch of the first viewport, or a wireframe schematic as fallback.
- Locking a card is the approval: a locked image comp becomes the approved comp; a locked sketch becomes the composition the build must match.

# Part 15 — Design Context Capture

## 167. Purpose of the Product Record
- Capture durable product truth separately from the visual world; product discovery never invents a visual direction.
- Update an existing product record instead of creating a competing authority.
- In a sub-application that inherits shared context, confirm which facts are shared versus app-specific before recording.
- Never silently overwrite an existing record.

## 168. Starting States for Context Capture
- No product record: explore, interview, and write it.
- Record exists: ask what is stale or missing; do not reopen confirmed fields without a reason.
- Legacy record: add only durable missing facts; an absent platform means `web` unless evidence says otherwise.
- Only a visual record exists: leave it untouched and create the product record.
- Redesign or rebrand request: preserve confirmed product truth unless the stakeholder changes it; visual replacement happens later.

## 169. Explore Before Asking
- Scan enough evidence that the stakeholder never repeats known facts: product docs and copy, app boundaries, features, workflows, routes, roles, names, logos, legal and proof assets, brand commitments, platform and accessibility signals.
- Treat existing evidence as a hypothesis, not approval.
- Note visual maturity without documenting, extending, or replacing the world at this stage.

## 170. Platform Hypothesis
- Classify the platform as `web`, `ios`, `android`, or `adaptive` (one product that genuinely adapts its design language per OS).
- Mobile web remains `web`; a native wrapper around a website does not make its design language native.
- Confirm an ambiguous platform separately.
- Once a native platform is confirmed, load that platform's conventions before any design work.

## 171. Interview for Product Truth
- Ask only about material gaps the evidence and request do not answer strongly.
- Keep rounds to at most three focused questions; require at least one real answer or approval round before writing a new record.
- Confirm inferences rather than asserting them.
- Start with the unknowns that most change future decisions: who the primary user is, in what situation, doing what job; what the product makes possible and its meaningfully different mechanism; what durable constraints, assets, evidence, or facts must be preserved.
- Add a round only for a material gap in audience, brand commitment, evidence, or accessibility.
- Record undecided facts as undecided instead of inventing them.
- Probe once with a real question before concluding no one can answer; if you must infer, label every inferred fact and disclose the substitution up front.

## 172. Stack Decision
- When there is no existing framework and the request implies building, the technology stack is the stakeholder's decision: ask once (plain static HTML/CSS, a specific framework, or your recommendation) plus any deploy constraint.
- Record "delegated" when they leave it to you, so later work knows the choice was offered.

## 173. Keep Aesthetics Out of Discovery
- Do not ask for aesthetic direction, emotional feel, visual references, colors, typography, or style during product discovery.
- If the stakeholder volunteers a binding visual constraint, record it without expanding it.

## 174. What Belongs in Product Truth
- Users, jobs, workflows, purpose, success, positioning, operating context.
- Capabilities, constraints, terminology, evidence, platform, accessibility.
- Confirmed voice, assets, and brand commitments.

## 175. What Does Not Belong in Product Truth
- Visual worlds, palettes, typography, components, or page concepts.
- Visitor mode, narrative, CTA or proof sequence, or other surface strategy.
- Invented testimonials, customers, benchmarks, pricing, licensing, or deployment claims.
- A requirement to decide every optional field.

## 176. Product Record Structure
- Sections: Platform, Stack (greenfield only), Users, Product Purpose, Positioning, Operating Context, Capabilities and Constraints, Brand Commitments, Evidence on Hand, Product Principles, Accessibility & Inclusion.
- Positioning names the mechanism or claim a neighboring product could not truthfully copy.
- Evidence on Hand lists real content and assets, and explicitly states absences future work must not fabricate.
- Product Principles: three to five durable strategic principles, no visual recipes.
- Write only confirmed facts and explicitly marked open decisions; omit irrelevant sections rather than filling them with generic prose.
- Write the product record before any visual-world or surface-concept work; notes or later design prose are no substitute.

## 177. Build-Path Default
- When image generation is available, ask once how new showcase surfaces should start: comp-first (an image sets the bar before code; bolder composition, slower, the build must match the image) or code-first (build directly; ambition written into a direction contract and audited at the finish; leaner, faster).
- State the trade in the question itself; the names mean nothing to someone meeting them for the first time.
- Clarify that app screens and documents are built code-first either way.
- Record only the value the stakeholder chose; a recommendation is not an answer, and a value taken from silence is a default nobody set.
- If unanswered, record nothing and state which path this session takes (comp-first for landing or showcase surfaces, code-first for app screens and documents).
- Keep this workflow preference out of product truth.

## 178. Wrap-Up of Context Capture
- Summarize captured facts and deliberately undecided facts.
- Do not offer a visual system record merely because one is missing.
- Recommend the next step from actual state: an early project names the first surface; a coherent undocumented interface gets documented; an existing surface needing work gets a scoped improvement.

# Part 16 — Establishing Direction

## 179. Name the Mechanism and Scene
- Before generating directions for a new or replacement world, name in one sentence the product's unique mechanism, the audience's real scene, its cultural home, and what this first surface must prove.

## 180. Identify the Rut
- Name the page this category always ships and its predictable opposite; both are the rut and are excluded from the candidate list.
- When the brief paints its own picture (a product name, a titled artifact, a governing metaphor), its literal reading joins the rut: spend at most one candidate on it.

## 181. Derive Seven Candidates from the Audience's World
- List seven concrete visual systems, artifacts, places, or rituals the audience knows by heart, ordered by resonance.
- For each, write one line on why it resonates and can carry the mechanism, and one on how it looks: ground and main colors, type voices, and the one recognizable signature.
- Include the audience's graphic and screen traditions, not only physical objects: notation, publications, identity programs, data graphics, and the interfaces it reads daily.
- A nameable abstract system (a poster school, a documentation standard) is as concrete a candidate as any artifact.
- Ask what this thing would look like as a physical object, and what its world looked like before the web.
- Count near-duplicates once.
- When more than three of the seven share one material family, you stopped at the most obvious artifact; dig until the list spans at least three families.

## 182. Tools-as-Costume Rule
- On Operate or Read surfaces, never derive candidates from the tools and instruments the audience operates: a terminal, scope, or control panel handed to a working screen comes back as a costume.
- On Persuade or Experience surfaces, the audience's tools count toward the rut: spend at most one candidate on them.

## 183. Complete Directions
- Turn each candidate into a complete direction that joins a reusable visual world to a concrete first-surface experience.

## 184. Every Direction Must Be Viable
- Every relationship and claim a direction visualizes must be true.
- Each needs a real palette, a component family, a distinctive composition with one product-specific experience, and workability at full-surface scale within available assets, tools, and performance budget.
- A candidate that fails on truth is replaced before selection, never rescued by it.

## 185. Truth Binds Claims, Not Demonstrations
- In greenfield work, author whatever illustrative material the concept needs at full fidelity.
- Label synthetic material wherever a visitor could mistake it for the real thing, and hand over a list of what to replace with real material.
- Never invent commercial or factual claims: prices, customers, benchmarks, endpoints, or capabilities the product lacks.
- Refusing a bold direction because its demonstration data does not exist yet is timidity disguised as honesty.

# Part 17 — Exploring Variants & Comps

## 186. Random Assignment Against Convergence
- Use a random draw to assign the direction to build; randomness keeps every project from converging on the category default.
- Never write artifact code for a new world before the direction is assigned and acknowledged.

## 187. Fusing Challengers
- Weigh outside "challenger" worlds against the assigned direction by fusing them first: the challenger supplies form and system grammar, the product supplies every fact, clarity wins conflicts.
- Judge on exactly two axes: audience identification and product clarity.
- Close each with a verdict decided before any borrowing: wins (beats on both axes, becomes the build candidate), competitive (holds one axis, stays a full alternate), or declined (loses both).
- Losing to strong grounded material is a valid outcome.

## 188. Donation, Not Clothes
- A declined challenger still donates: name the one discipline of its system the assigned direction lacks and raise the direction to match.
- Transfer ambition and system discipline (a palette's total commitment, a grid's density courage, a form's structural honesty), never the challenger's surface treatment.
- A button shadow or display face is clothes, not discipline; a lifted motif is a costume note; one world owns the page.
- Write each raise as its own named line in the presented direction; a raise nobody can read did not happen.

## 189. Presenting a Direction
- Present one direction fully committed, already raised: world, first viewport, visitor path, signature interaction, cross-surface reach, and honest risk.
- Give every card identical anatomy: thesis, palette, materials, first viewport, honest risk.
- Show winning and competitive challengers as full alternates with a one-line case; show declined ones demoted, compact and quiet, with their verdict and what was kept, never silently dropped and still adoptable.
- Hold at most three full-card challengers; the verdict informs the choice, never pre-empts it.
- When fewer full cards qualify than requested, present the honest smaller hand, explain why in one line, and offer a re-draw; never promote a declined option to fill a slot.

## 190. Designer's Pick Card
- Add exactly one card for your own top-ranked grounded candidate when it was not assigned, with an honest risk line naming its familiarity.
- Never two picks, never a ranked list: a lineup invites the safest card.
- The pick never takes the lead position.
- Familiar and effective is a legitimate destination, not a failure of nerve.

## 191. The Standing Exit (Category Standard)
- Every direction round offers one quiet, permanent alternative: the category standard, played straight.
- Never recommend it, never weigh it against the assigned direction, never let it soften the others.
- When chosen, make convention the commitment: ask for two or three products it should sit alongside, make their craft level the bar, and execute at full fidelity without irony or smuggled quirk.

## 192. Re-Drawing Directions
- Offer re-draw with an optional one-line steer in three registers: plain (fresh hand, same spread), safer (remaining conventional candidates plus the category standard against named competitors), bolder (foreign forms only, full commitment).
- The register is the stakeholder's steering, never yours to pre-select.
- Re-drawing eliminates every direction already shown; after two consecutive re-draws, ask what quality is missing.
- Re-draw on your own only on named factual grounds (the direction cannot carry the product's truth or task); taste is never grounds, nor is a look mismatch.
- A stakeholder- or brief-pinned direction always beats the draw.

## 193. Resolving Collisions with Pinned Constraints
- Preserve every pinned constraint field by field.
- In open dimensions, the assigned direction still binds through its topology, controls, state vocabulary, and ritual.
- When only its materials conflict with a pinned look or brand commitment, translate that material expression and name the translation.

## 194. Decision Comps at Full Fidelity
- When image generation exists, render each card as that direction's north-star comp: the real surface, its first viewport plus the start of the next section, real product name and content, no invented commercial claims, in the card's own palette, type, and material world, fully committed.
- Fairness between cards means equal fidelity in each card's own grammar, one surface, one aspect ratio; never shared unfinishedness.
- Frame comps at the surface's own aspect: portrait at device viewport for native or mobile-first, landscape for desktop web; a phone screen comped landscape is a broken frame.
- A template skeleton stays the template whatever world paints it, including your own pick.
- Produce in reading order: assigned card, pick, full-card hand, category standard; declined challengers get no comp.
- Without image generation, carry identity in palette chips and facts; that presentation is complete, and every challenger's art is demoted to a thumbnail so salience encodes the verdict, not which cards happen to have images.

## 195. Comp-Led vs Code-Led
- Operate and Read surfaces are code-led: working screens and documents come out better built than pictured.
- Persuade and Experience surfaces take the recorded default, comp-led when image generation exists.
- Comp-led: the chosen comp is law and the finish review audits the build against it; boldest composition, fix rounds expected.
- Code-led: no apology; the chosen sketch is the composition to match, and ambition moves into the written contract (first viewport, a named signature interaction, a motion grammar) audited in behavior. Code-led is not a discount on commitment.
- A stakeholder flipping the path binds that session only; ask once afterward whether to keep it as the standing default.

## 196. Reference Worlds Are Working Systems
- When a catalog or reference world wins, carry its palette, material, type, composition, topology, controls, states, and responsive rules into the product as far as the mode allows; it is not a mood board.
- Use the reference's rendered quality boards to set the craft bar (finish, commitment, art direction), never the composition.

# Part 18 — Committing the World

## 197. Color Strategy Before Colors
- Choose a strategy before choosing colors: Restrained (world-tinted neutrals plus one accent), Committed (one saturated color carries `30-60%` of the surface), Full palette (`3-4` named roles), or Drenched (the surface is the color).
- Restrained suits screens people operate or read, where color must still do real jobs.
- Persuade and Experience surfaces have permission for the bolder strategies; take them when the brief allows.
- Commit color at page scale: fields that own whole regions, not accents scattered on a neutral ground.

## 198. Dark or Light from the Scene
- Never default to dark or light; write one sentence of physical scene (who uses this, where, under what light) and let it force the answer.

## 199. Choosing Typefaces
- Choose faces like objects from the subject's world, in the mode's register.
- Operate and Read surfaces are well served by system stacks and workhorse UI faces.
- Persuade and Experience surfaces want faces with a point of view.
- Treat these as reflex defaults that signal you stopped looking: `Fraunces`, `Playfair Display`, `Cormorant`, `Lora`, `Crimson`, `Newsreader`, `Syne`, `Space Grotesk`, `Space Mono`, `IBM Plex`, `Inter` as display, `DM Sans`, `DM Serif`, `Outfit`, `Plus Jakarta Sans`, `Instrument Sans`.
- Using one requires a reason no other face could satisfy; a subject association (books want serif, bookshops want hand-lettering, tech wants mono) is never that reason.

## 200. Generic-Look Calibration
- Recognize the four looks generated interfaces cluster around: warm cream ground with high-contrast serif display and terracotta or signal-red accent; near-black with one neon accent and glowing edges; broadsheet-editorial hairlines, italic display serif, small tracked mono labels; flat saturated ink with black boxes, hard offset shadows, heavy condensed display type.
- All are legitimate when the brief calls for them; landing in one when the brief left aesthetics free means the self-check failed.
- Self-check: if someone could guess the aesthetic from the category alone, or from category-plus-avoidance, rework until neither is obvious.

## 201. Energy Is Not the Enemy of Trust
- Negative brief constraints (no gamification, no hype) rule out those devices, not exuberance.
- Adjectives describing product behavior (quiet support, calm coaching) do not dictate the surface's energy.

## 202. Warm Subjects Are Not a Cream License
- Bookish, warm, family, or child-facing subjects do not soften the calibration; book cloth, thread, jackets, endpapers, and shelf ephemera span the saturated spectrum.
- Cream plus serif for a book subject is the default wearing the subject's clothes; treat a first instinct of cream, paper, parchment, ivory, or lamplight on an unpinned Persuade surface as already spent and rework from saturated materials.

## 203. Pinned World, Full Range
- A brief-pinned world pins the world, not its softest rendition; keep its full material range in play.
- A rendition matching what any generator ships for that world fails the self-check at execution.

# Part 19 — Recording the Direction

## 204. Direction Contract
- Before building, record the chosen direction as a short contract (about `150` words) in six blocks.
- THESIS: the one idea this surface owns and the category-default arrangement it refuses.
- OWN-WORLD: palette and component language specific enough to be recognizable with all content removed.
- STORY: what the visitor understands, believes, and does.
- FIRST VIEWPORT: the exact composition, what is where at what scale, and where the primary action sits.
- FORM: the chosen form and its position on the ranked candidate list.
- FINISH: the exit condition: unreviewed and undocumented is unfinished.
- If any block reads like a mood, the direction is not decided yet.

## 205. Contract Stays Out of the Product
- Never embed the direction contract in shipped code or any delivered artifact: comments, hidden DOM, templates, data attributes, serialized state, metadata, or accessibility-only text.

## 206. Surface Brief Scope
- Keep the per-surface brief small: scope and visitor mode; audience, job, action or task, proof and content, constraints; chosen direction and memorable moment; unresolved decisions.
- Do not copy global product truth or design tokens into it.

## 207. Document the World from the Build
- On a new world, write the design system record at the finish from what was built; a rulebook written before the build gets defended against reality instead of describing it.
- A new world shipped without its design system record is incomplete.
- An ordinary extension does not rewrite the design system record.

# Part 20 — Visualizing Concepts & Assets

## 208. Comps Do Not Reopen the World
- A comp tests composition, narrative, hierarchy, density, focal moment, signature use, and image requirements; it is not a second identity workshop.
- Hold palette, type direction, material language, component character, imagery stance, and motion grammar fixed.
- Never generate a palette artifact, ask new atmosphere questions, introduce a new type voice, or invent a new motif at this stage; if the world cannot support the concept, return to the concept shortlist.

## 209. Three Compositional Options
- Render three distinct high-fidelity comps of the requested surface; one comp invites rubber-stamping, three expose the composition worth building.
- When a decision comp exists, it is option one; generate two more that vary what it held fixed, from the direction in words rather than using the first comp as input, or all three collapse into one layout.
- A variant that is a tidier simplification of the first adds no choice.
- When multiple concepts were shortlisted, spread the three across them; when one is committed, vary what leads, topology, sequence, density, hierarchy, focal composition, or interaction framing.
- Show enough beyond the opening to prove the concept can govern the whole surface.

## 210. Writing a Comp Prompt
- Keep prompts short, `150` to `300` words, carrying only what the image model cannot know; a prompt that specifies everything returns a template.
- Open with the surface type and product name, rendered edge to edge with crisp readable text and no browser window, device, or desk around it.
- State the product and visitor's job with real content: names, numbers with units, the offer or state, claims at honest certainty, and the next action by name.
- Name what leads (summary-led, timeline-led, offer-led, reference-led) and the parts in reading order, a phrase each.
- Describe the frame in one line: mark and name, navigation, utility controls, far edge; a page without navigation says so.
- Leave sizes, positions, colors, and component styling out, except pinned colors, typefaces, or brand elements, which are content.

## 211. Carrying the Look into a Comp
- On an established world, pass a screenshot of a representative page as reference; state what carries over (chrome, palette, type, component character) and what must not (its own content; a lifted banner or hero is leakage).
- With reference boards, attach them and state they are style inspiration adapted into a working product, layout and content not to be copied; describing the style in words as well overrides the picture.
- Without images, carry the look in two to four sentences of concrete visual law: ground and main colors with their jobs, type voices, one signature; never list every color or describe components one by one.

## 212. Comp Self-Checks
- If the render could hang as a poster or reads as a photograph with text on it, it is not a comp; regenerate.
- Point at the subject: a render depicting the world but nothing of the subject fails, however faithful its atmosphere.
- The visitor's job must be readable from the image alone; if the mode cannot be named from the render with no caption, regenerate with the job as the prompt's spine.
- Commitment is depth: one dominant move plus supporting material, type, and spacing; other regions hold still at real reading size.
- A second element competing with the lead at the same scale is shouting; busy is louder, not bolder.

## 213. One Approval Point
- Show all three comps together; ask what should carry forward, what feels false to the world, and whether to approve, combine, revise, or reject.
- Do not begin code until the stakeholder approves or explicitly delegates; a delegated choice uses the brief and product truth, states the evidence, and is disclosed immediately.
- Approval refines the task concept; it does not modify the design system record.
- Record which comp was approved so the approval survives across sessions.

## 214. The Approved Comp Becomes a Spec
- Translate the approved comp into semantic, responsive, accessible code; never recompose it. Keeping palette and mood while redrawing topology is a second art direction.
- Never rasterize core UI text or controls.
- Never substitute a different visual driver after approval without asking.
- Core UI text, responsive behavior, accessibility, semantics, and interaction states remain implementation responsibilities.

## 215. Medium Follows the Pixels
- Decide each region's medium from what the pixels are, never what feels buildable.
- Figures, product objects, machinery, any illustration with perspective, shading, or drawing skill, and any named texture (woven cloth, paper grain, leather, brushed metal) ship as raster images.
- Text, controls, chrome, diagrams with countable elements, flat shape systems, and anything that must move, scale, or respond are built in code.
- Faking a sculpted finish in CSS or a torn edge with a many-vertex `clip-path` is the quiet deletion of the approved design.
- Dropping an image-native region is a scope decision the stakeholder makes at approval, never a silent flattening later.

## 216. Image Provenance
- Every raster in a shipped artifact carries its provenance: the exact generation prompt for produced images, the origin for sourced, stock, or pre-existing ones.
- Generated imagery is material, not a claim; evidence rules bind assertions, testimonials, and photographs presented as real, not render fidelity.
- A raster abandoned in a revision is deleted in the same pass.

# Part 21 — Building from an Approved Comp

## 217. The Comp Is a Measured Contract
- An approved comp is a spatial contract, not a mood board; only the stakeholder can downgrade its authority, in explicit words.
- Builders systematically believe their recreation of an image succeeded when it did not; measure the screen against the comp instead of trusting memory.
- Comp-faithful builds demand sustained precision; if the build capacity is limited, choose the code-led path up front.

## 218. Measure and Map Regions
- Lay a coordinate grid over the comp and name every salient region by span, each with a note describing what the comp shows there.
- Classify regions as painted (plate, image, texture) or code-drawn (text, control, chrome).
- Leave no comp ink unnamed: what is never named can never be missing.
- Never treat a text, control, or chrome region larger than a quarter of the comp as one element; name the elements inside it.
- Split regions by what varies independently; a framed view is a frame over its own image region.
- Callout lines and arrows annotating a drawing belong to that drawing's image, with only labels set as text.
- An image region's box must hold the whole artwork with a margin, unless the page really crops it there.

## 219. Measure Type, Don't Guess
- Read the comp's cap height, width class, and weight from the pixels, then rank candidate faces by shape similarity at that cap height with the region's real words.

## 220. Nothing Outside the Spec
- Anything not in the measured spec does not exist on the page: no borders, rules, containers, or chrome the comp does not show.
- Only three concessions exist: fonts (closest obtainable face), icon glyphs (the pictogram only, never a control's chrome, so chevrons, arrows, dropdown borders, and button shapes are the comp's), and genuine comp defects such as misspellings.
- Inline SVG past an icon's budget (under `64px`, a few paths) is an illustration and must be a raster; a chart drawn from live data is a chart.

## 221. Image Plates Before Page Code
- Regenerate every raster region at asset resolution from its comp crop, UI text removed; at least `1.5x` the region's size.
- Isolated ink, figures, and objects use native transparent PNG to sit on the page's own ground; photos and textures stay opaque.
- A texture is a clean patch mirror-tiled to size, generated only when no clean patch exists.
- Verify alpha, white foregrounds, fine edges, and clear holes on both light and dark grounds; never chroma-key.
- A crop of the comp is a reference, never a shipping pixel; never edit, composite into, or regenerate the approved comp.
- Have the stakeholder review the plates and which regions code draws before page code is written; a page written before its plates exists draws its material in CSS.

## 222. Hero First
- Build only the first viewport first, at the comp's dimensions, with the comp's words verbatim; rewording is a stated decision after the hero matches.
- Place every image plate at its box before any text or control, then lay the semantic layer over it from the spec's palette and boxes.
- Serve fonts from the project's own files; avoid hosted font stylesheets.
- Treat numeric misses as the edit ("cap height `78px` in the build, `103px` in the comp").
- Diagnose regions in order: missing needs material, contradicted needs structure re-derived from the box, drift is where size and spacing edits belong.
- After three failed attempts, present the first viewport for stakeholder review instead of iterating.
- The hero is where a build's ambition is won or lost; a retry costs minutes, a rebuild at the end costs the project.

## 223. Sections, Motion, Responsive
- Build remaining sections inside the spec's system: the same corner language, line weights, and palette, nothing the comp never shows; uncovered regions inherit the recorded system.
- Orchestrate the signature interaction, reveals, and motion once rather than scattering them.
- Make the first viewport hold at common desktop widths (`1280` to `1600`), not only the comp's exact size: fluid columns, no fixed-pixel grid that wraps `100px` narrower, sizes proportional to the viewport rather than px floors.
- When a region is pushed below the first viewport, resize what sits above it rather than moving it alone.
- Verify at `1440` wide desktop and `390` wide mobile.

# Part 22 — Building with Full Commitment

## 224. Build the Assigned Direction
- Build the assigned direction, not a safer interpretation; the form supplies structure, reading order, component conventions, and native motion, the product supplies every fact.
- Commit every atom: nav, buttons, inputs, and links rebuilt in the form's vocabulary; a stock component inside a committed form is a lapse.
- Land the first build fully committed; later passes clarify, never dilute.
- In unattended work, the safe rendition is the known risk.

## 225. The First Viewport Is a Thesis
- Demonstrate the mechanism immediately, at the scale the form has in life; never trap the concept inside a standard hero or card shell.
- Memory test: if someone left after one viewport, what would they describe an hour later? If the answer is a mood, the concept has not committed.

## 226. Prove, Don't Claim
- Show the subject doing its job: the interface at work, the mechanism dramatized, specifics a competitor could not copy-paste.
- Author demonstration data at full fidelity and label it synthetic; claims stay uninventable.

## 227. Author Assets; Never Substitute Chrome
- Great surfaces live on carefully made content: names, entries, copy, covers, thumbnails, textures.
- In greenfield work every blank is yours to author at production fidelity; no section is omittable.
- Gradients, glass, generic icon tiles, and many-vertex `clip-path` polygons where an authored asset belongs are the gap wearing chrome.

## 228. Build the Form's Web Leverage
- When the chosen world names a technique (canvas, WebGL, view transitions, generative motion), build the technique itself, not a static imitation.

## 229. Pace the Scroll Like a Studio
- Vary density, scale, image, motion, and quiet inside one grammar; a dense passage earns a quiet one.
- End the page anchored by a real close.
- Use one spacing rhythm throughout, with more space above a heading than below it.

## 230. Real Imagery
- Use real, verified imagery when the brief implies it; search for the subject's physical object rather than the category.
- One decisive photo beats five mediocre ones; verify that stock image URLs resolve.

## 231. Motion as Material
- Give the page the form's native motion once, orchestrated, rather than scattered hover effects.
- Bound expensive effects and keep content visible by default.
- Preserve semantics, accessibility, performance, responsiveness, conventions, and working behavior throughout.

# Part 23 — Inspecting & Finishing

## 232. Inspection Rounds
- Inspect every target size in one batched round: desktop and mobile on web; each shipped device class per OS on native; plus the stakeholder's actual viewport when known, since the width that breaks is the one they see first.
- On anything interactive, drive every reachable state (open, closed, hover, focus, error, empty, overlong content) and check for overlap and clipping.
- Critique the render against the request and the direction contract, fix material gaps in a batch, and confirm with one final round; two rounds is the ceiling.
- Never judge fidelity from one full-page thumbnail; compare region by region against the comp.
- On a Persuade surface, a first-time visitor should know what this is, why it matters, and what to do within seconds, in the form's own vocabulary.

## 233. Valid Evidence Only
- Settle or disable entrance motion before capturing; an element hidden by animation timing reads as missing and gets "fixed" into a regression.
- Capture full-page shots from the document top, and comp comparisons at the comp's own pixel dimensions.
- Open every capture and confirm it shows what it claims: no blank regions, no wrong section, no half-loaded state.

## 234. Independent Finish Review
- Have the finish reviewed by a fresh reviewer with no inherited context; one who shares the builder's framing inherits its optimism.
- Give the reviewer the original request, confirmed answers, the direction contract, the captures, the quality bar references, and the approved or reference comp.
- On native platforms, review in the platform's conventions rather than the web's.

## 235. Four Review Dispositions
- **Recapture**: the evidence failed, not the build; recapture and run a full review again.
- **Rebuild**: fidelity failed wholesale; re-derive the named regions immediately and send for a fresh full review.
- **Ship**: nothing owed; report the verdict at its scope.
- **Fix**: apply material fixes in one batch, recapture the same viewports, and have each fix scored resolved, partial, or unresolved.
- Two fix rounds is the budget for unattended work; when attended, the stakeholder decides whether to ship or fund another round.
- Stop the moment a round resolves nothing; work only from the reviewer's findings, never a re-opened private hunt.

## 236. Honest Verdicts
- Report the verdict under its own word and at its actual scope; "all three fixes resolved" is not "no issues remain".
- Never announce a table with open material findings as a pass.
- When the stakeholder answers a ship with contrary evidence (their screenshot, a named mismatch), that evidence outranks every capture you made; get a fresh full review rather than patching and self-certifying.

## 237. Document at the Finish
- After the last correction on a new world or approved system change, record the design system from the built result, with tokens, not prose alone.
- For ordinary extensions, compare the build to the incumbent system, preserve it, and report pre-existing drift without repairing it unasked.
- Finish only when review and documentation are complete.

# Part 24 — Generating Design Variants

## 238. Fast Variant Lane
- Variants should arrive from a single sentence naming an element, a direction, and a count; the speed lives in tooling, never in the design work, which is planned and accepted with full rigor.
- Variants are a web, in-browser practice; on native platforms, revise the source bolder or quieter instead.

## 239. Parsing a Variant Request
- A number in the request is the count; with no number, generate `3`; cap at `8`.
- Map direction wording onto a fixed vocabulary: bold, bolder, stronger, punchier → bolder; quiet, calmer, softer, toned down → quieter; simpler, minimal, stripped → distill; refined, tightened, polished → polish; font and type words → typeset; color words → colorize; arrangement and spacing words → layout; device and breakpoint words → adapt; motion words → animate; playful words → delight; rule-breaking words → overdrive.
- Intent without a vocabulary word ("make it feel like a bank", "warmer", "more premium") becomes a general design pass with the wording as the brief.
- An action plus extra intent ("bolder, but keep it monochrome") keeps the action and carries the rest as a constraint.
- When the wording names no direction ("better", "improve", "nicer", "different", "fresh", "redesign", "some options", "alternatives"), ask one question offering the vocabulary; "surprise me" becomes a general pass.

## 240. Targeting the Element
- When a repeated component is named in plural ("the pricing cards"), target the container that holds the set, so one scoped style restyles every instance.
- Prefer a unique class as the target, then a landmark plus class; avoid ids, since each variant mounts a copy.

## 241. Planning Variants
- Lock identity first, then the mode, then choose three different primary axes so variants differ meaningfully, then apply a squint test.
- Each variant is a complete replacement of the element; the moves open to a full redesign (promoted tier, restructured set, reordered card, different surface) are open here too.
- Expose adjustable knobs where useful so the stakeholder can tune the keeper.
- When product and design context are missing, extract identity from the element itself rather than interviewing.
- Do not restyle variants to appease automated findings while they are in preview.

## 242. Accepting a Variant
- On accept, move the chosen variant's rules into the stylesheet that already owns the element with real selectors, bake in chosen knob values, and remove all preview scaffolding and markers.
- Leave the stakeholder seeing the accepted design with no preview chrome.

# Part 25 — Onboarding Flows

## 243. Onboarding's Real Job
- Get users to first value as fast as possible; onboarding's job is not to teach the product but to reach the moment that proves it is worth their time.
- Get users to value quickly, not teach everything possible.

## 244. Questions Before Designing Onboarding
- What are users trying to accomplish; what is confusing; where do they get stuck or drop off; what is the "aha moment"?
- What is their experience level (beginners, power users, mixed), motivation (exploring vs required by work), time commitment (`5` minutes vs `30`), and known alternatives (competitor vs new to category)?
- What is the minimum they must learn to succeed, the key action (first project, first invite), and the success measure (completion rate, time to value)?

## 245. Show, Don't Tell
- Demonstrate with working examples, not descriptions.
- Provide real functionality in onboarding, not a separate tutorial mode.
- Use progressive disclosure: one thing at a time.

## 246. Make It Optional
- Let experienced users skip; never block access to the product.
- Provide "Skip" or "I'll explore on my own" options.

## 247. Time to Value
- Reach the aha moment as soon as possible; front-load the most important concepts.
- Teach the 20% that delivers 80% of the value; save advanced features for contextual discovery.

## 248. Context Over Ceremony
- Teach features when users need them, not upfront.
- Treat empty states as onboarding opportunities; place tooltips and hints at the point of use.

## 249. Respect User Intelligence
- Don't patronize or over-explain; be concise and clear.
- Assume users can figure out standard patterns.

## 250. Welcome Screen
- State a clear value proposition, what users will learn or accomplish, an honest time estimate, and a skip option.

## 251. Account Setup
- Ask for minimal required information and collect more later.
- Explain why each piece of information is requested.
- Use smart defaults, and social login when appropriate.

## 252. Core Concept Introduction
- Introduce `1-3` core concepts, not everything, in simple language with examples.
- Make it interactive when possible, and show progress ("step 1 of 3").

## 253. First Success
- Guide users to accomplish something real, with pre-populated examples or templates.
- Celebrate completion without overdoing it, and give clear next steps.

## 254. Empty States as Onboarding
- Every empty state says what will appear here ("Your recent projects will appear here"), why it matters, and how to start ("Create project" or "Import from template").
- Add visual interest (illustration or icon, not text on a blank page) and contextual help ("Watch 2-min tutorial").
- First use: emphasize value and offer a template.
- User cleared: light touch, easy to recreate.
- No results: suggest a different query and offer to clear filters.
- No permissions: explain why and how to get access.
- Error: explain what happened and offer retry.

## 255. Contextual Tooltips
- Appear at the relevant moment (first time the user sees the feature) and point directly at the element.
- Give a brief explanation plus benefit, with dismiss, "Don't show again", and optional "Learn more".

## 256. Feature Announcements and Progressive Onboarding
- Highlight new features on release: what's new and why it matters, tryable immediately, dismissable.
- Teach features as users encounter them, mark new or unused features with badges, and unlock complexity gradually.

## 257. Guided Tours
- Use only for complex interfaces, significant product changes, or domain-heavy tools.
- Spotlight specific elements and dim the rest; keep tours to `3-7` steps.
- Let users click through freely, include "Skip tour", and make tours replayable from help.
- Prefer interaction over passivity (users click real buttons), focus on workflow not features ("Create a project", not "This is the project button"), and supply sample data so actions work.

## 258. Interactive Tutorials
- Use when users need hands-on practice, concepts are unfamiliar, or stakes are high.
- Provide a sandbox with sample data, clear objectives ("Create a chart showing sales by region"), step-by-step guidance, validation, and a graduation moment.

## 259. In-Product Help
- Provide contextual help links, a keyboard shortcut reference, searchable help, and video for complex workflows.
- Use a `?` icon near complex features, "Learn more" links in tooltips, and shortcut hints on controls (`⌘K` on a search box).
- Modals trap focus, use a backdrop, and close on ESC.

## 260. Show Onboarding Once
- Track completion and seen states, respect dismissals, and never show initial onboarding to returning users.
- Measure completion and drop-off points.

## 261. Onboarding Anti-Patterns
- Forcing users through long onboarding before they can use the product.
- Obvious, patronizing explanations.
- Repeating the same tooltip after dismissal.
- Blocking all UI during a tour.
- A separate tutorial mode disconnected from the real product.
- Overwhelming information upfront.
- A hidden or hard-to-find "Skip".

## 262. Verifying Onboarding
- Test with real users for time to completion, comprehension, whether they take the next step, skip rate (high may mean too long or not valuable), completion rate (low means simplify), and time to first value.

# Part 26 — Extracting a Design System from Existing UI

## 263. Discover Before Extracting
- Find the existing design system or shared UI and understand its component organization, naming conventions, token structure, and conventions.
- If no system exists, do not create one unilaterally; agree on location and structure first.

## 264. What to Look For
- Repeated components: similar patterns used `3+` times (buttons, cards, inputs).
- Hard-coded values: colors, spacing, typography, shadows that should be tokens.
- Inconsistent variations: multiple implementations of one concept.
- Composition patterns: repeating layouts or interactions (form rows, toolbar groups, empty states).
- Type styles: repeated font-size, weight, and line-height combinations.
- Animation patterns: repeated easing, duration, or keyframe combinations.

## 265. The Rule of Three
- Extract only what is used `3+` times with the same intent; premature abstraction is worse than duplication.
- Grow systems incrementally: extract what is clearly reusable now, not what might someday be.

## 266. Plan the Extraction
- Decide which elements become components, which values become tokens, which variants each component needs, names that match existing patterns, and the migration path for existing uses.

## 267. Enrich What You Extract
- Components get a clear props API with sensible defaults, proper variants, built-in accessibility (ARIA, keyboard navigation, focus management), and usage examples.
- Tokens get clear primitive vs semantic naming, hierarchy, and guidance on when to use each.
- Patterns get when-to-use guidance, examples, and variations.

## 268. Migrate and Clean Up
- Find every instance, replace systematically, verify visual and functional parity, and delete the old implementations.
- Update the component catalog and token documentation with examples.

## 269. Extraction Anti-Patterns
- Extracting one-off, context-specific implementations without generalization.
- Components so generic they are useless.
- Ignoring existing system conventions.
- Skipping typed props or prop documentation.
- A token for every single value; tokens need semantic meaning.
- Merging things that differ in intent: two similar-looking buttons serving different purposes stay separate.

# Part 27 — Documenting a Design System

## 270. When to Document
- When a coherent incumbent system exists but is unrecorded.
- When the first implementation of a new world is complete and its provisional decisions need to be made permanent.
- When the existing record has drifted from the design.
- Before a large redesign, to capture the current state as a reference.
- Never silently overwrite an existing record; show it and offer refresh, overwrite, or merge.

## 271. Tokens Are Normative, Prose Is Context
- Put machine-readable tokens first and let prose explain how to apply them.
- Never define a token value in two places, and never restate a different value in prose.
- Keep only tokens the project actually uses; empty scale keys or fabricated tokens pollute the spec.

## 272. Token Conventions
- Reference tokens as `{path.to.token}` (e.g. `{colors.primary}`, `{rounded.md}`); components may reference primitives, primitives never reference each other.
- Colors accept any valid CSS color; hex is the portable default, but preserve an incumbent `rgb()`, `hsl()`, `oklch()`, or wide-gamut source when it is canonical. Never split the source of truth.
- Token groups are limited to `colors`, `typography`, `rounded`, `spacing`, `components`; shadows, motion, focus rings, and breakpoints live in an extension layer.
- Component sub-tokens are limited to `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`.
- Keep the project's own scale names (`oxblood-deep`, `surface-container-low`); don't rename to generic defaults.
- Express variants as sibling names (`button-primary`, `button-primary-hover`, `button-primary-active`).
- Key colors by descriptive slug (`oxblood-deep`, `editorial-magenta`), not `blue-800`.
- Typography is one entry per role (`display`, `headline`, `title`, `body`, `label`) with only real props: `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`, `fontFeature`, `fontVariation`.

## 273. Canonical Section Order
- Use exactly: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.
- Omit irrelevant sections rather than inventing rules; never rename sections even slightly ("Colors", not "Color Palette & Roles").
- Put responsive layout in Layout, depth in Elevation & Depth, radius and form language in Shapes, per-component behavior in Components, and motion with the world or component it affects.

## 274. Finding the Assets
- Search in priority order: CSS custom properties (`--color-`, `--font-`, `--spacing-`, `--radius-`, `--shadow-`, `--ease-`, `--duration-`), utility-framework theme config, CSS-in-JS theme objects, token files, the main component library (button, card, input, navigation, dialog), the global stylesheet, and computed styles sampled from the rendered site (body, h1, links, buttons, cards), which catch values tokens miss.
- If nothing exists to extract, offer to establish a seed direction instead; never silently switch.

## 275. Auto-Extracting Structure
- Colors: group into Primary, Secondary, Tertiary, Neutral; with only one accent, use Primary plus Neutral and omit the rest rather than inventing them.
- Typography: map sizes and weights to display, headline, title, body, label; note font stacks and the scale ratio.
- Elevation: catalogue the shadow vocabulary; a flat, tonally layered system is a valid answer stated explicitly.
- Components: for button, card, input, chip, list item, tooltip, nav, record radius, color assignment, hover and focus treatment, and internal padding.
- Layout: grid, container, breakpoints, rhythm, density. Shapes: radius, corners, borders, clipping, recurring forms.

## 276. Qualitative Language Comes from the Stakeholder
- Ask in two rounds of at most three questions each.
- Creative North Star: one named metaphor for the whole system ("The Editorial Sanctuary", "The Lab Notebook"); offer `2-3` options honoring brand personality.
- Overview voice: mood adjectives, a `2-3` sentence aesthetic philosophy, and any confirmed anti-reference.
- Color character: descriptive names ("Deep Muted Teal-Navy", not "blue-800"), `2-3` options per key color.
- Elevation philosophy: flat, layered, or lifted; are shadows ambient or structural?
- Component philosophy in one phrase ("tactile and confident" vs "refined and restrained").
- Carry product truth only when it is a durable brand commitment that constrains the visual system.

## 277. Writing Each Section
- Overview: lead with the North Star, `2-3` paragraphs on personality, density, and philosophy, only confirmed rejections, ending with Key Characteristics.
- Colors: one sentence of palette character, then each color with descriptive name, value, and where and why it is used.
- Typography: display, body, and label faces with fallbacks, a character line, and a hierarchy giving weight, size or clamp, line height, and purpose; include a body measure like `65–75ch`.
- Elevation & Depth: say whether depth comes from shadows, tonal layering, or both; if no shadows, say so and how depth is conveyed; list each shadow with its exact value and use.
- Components: lead each with a character line, then shape, color assignment, states, distinctive behavior; cover buttons (shape, primary, hover and focus, secondary or ghost), chips, cards (corners, background, shadow strategy, border, padding), inputs (stroke, focus, error, disabled), navigation (default, hover, active, mobile), and any signature component.
- Do's and Don'ts: concrete guardrails grounded in the incumbent system or chosen world, each led with "Do" or "Don't"; never promote a task-specific concept into a system-wide prohibition.

## 278. Named Rules
- Express doctrine as memorable named rules: "The [Name] Rule." plus a short, forceful statement, `1-3` per section.
- Example: "The One Voice Rule. The primary accent is used on `≤10%` of any given screen. Its rarity is the point."
- Example: "The Flat-By-Default Rule. Surfaces are flat at rest; shadows appear only in response to state."

## 279. Writing Style for System Docs
- Descriptive over technical: "Gently curved edges (`8px` radius)" beats "rounded-lg"; lead with description, exact value in parentheses.
- Functional over decorative: explain where and why each token is used, not just what it is.
- Be decisive where evidence is decisive; use softer language for provisional guidance.
- Use concrete audit tests only when grounded in the observed system or a confirmed decision; one-sentence tests beat paragraphs of principle.
- Group colors by role, not by hex or hue order.

## 280. Extension Layer
- Hold what tokens cannot: per-color tonal ramps, canonical OKLCH when hex is approximate, display names, shadow tokens, motion tokens (e.g. `cubic-bezier(0.4, 0, 0.2, 1)` standard easing), breakpoints (e.g. `640px`), component snippets, and the narrative.
- Generate an `8`-step tonal ramp per color: dark to light, same hue, chroma reduced near white and black, lightness stepped from about `15%` to `95%`; reuse an existing tonal scale if one is defined.
- Carry the narrative verbatim from the prose; do not reword.

## 281. Component Specimens
- Document a tight set of `5-10` components: buttons (each variant separately), input, navigation, chip, card, plus distinctive signature components; skip utilities and wrappers.
- Make specimens self-contained: expand utility classes into literal CSS, reference root custom properties where they exist, otherwise resolve literal values.
- Inline icons as SVG at about `16-24px`.
- Include `:hover`, `:focus-visible`, and meaningful `:active` states; a default-only snapshot feels dead.
- Ship only distinctive CSS, no universal resets; prefix classes (e.g. `ds-btn-primary`) to avoid collisions.
- With no component library yet, synthesize canonical primitives from tokens so there is always something to render.

## 282. Seed Documentation (Pre-Implementation)
- Never create a visual identity without durable product context; establish product truth first.
- A seed requires a concrete first surface so the world and its first expression are chosen together.
- Mark the record clearly as a seed established before implementation.
- Populate the chosen thesis, palette strategy, type character, spatial grammar, depth behavior, and form language as invariants; leave unestablished values as `[to be resolved during implementation]`.
- Omit Components entirely and include no tokens beyond name and description; real tokens arrive once code exists.
- Keep the first surface's composition in its own brief; never promote it into the global world.

## 283. Confirm and Refine
- Show the full record, highlighting non-obvious creative choices (descriptive color names, atmosphere language, named rules), and offer to revise sections or add missed patterns.

## 284. Documentation Pitfalls
- Pasting raw class names instead of descriptive language.
- Documenting every token instead of what is actually reused.
- Inventing components that don't exist.
- Duplicating product truth; the visual record is strictly visual.
- Replacing canonical sections with near-synonyms.
- Inventing top-level token groups outside the supported set.

# Part 28 — Making It Bolder

## 285. Bolder Is Amplification, Not Effects
- Apply when one existing section reads flat against a page whose system has already shipped.
- Raise one part to the conviction the rest of the page already implies; the surrounding page, its system and its conventions are the given.
- Reject the reflex answer first: reaching for more effects (glows, gradients, extra motion) is the opposite of bold.
- If the request arrives while a direction is still being chosen, treat it as a call for a fresh direction, not a refinement.

## 286. Scope Is Sovereign
- "Everything else stays" is literal: touch only the named target.
- Do not restyle neighbors or migrate the page to a new idea.
- Banned: adding colors, fonts, radii, shadows or system primitives the surface does not already own.
- If the system genuinely cannot express the direction, stop and ask, naming the exact addition and the job it would do.

## 287. Diagnosing Why a Section Reads Flat
- Compare the target with what its neighbors already do: display type at full strength, structural devices that carry meaning, the signature motif, density and pacing.
- A flat section usually quietly opts out of the system's own strongest moves.
- The most reliable fix brings the target up to the expressive level its neighbors reach, in the system's own vocabulary.

## 288. Amplifying What the System Owns
- Reuse the existing motif and type scale at full strength, turned up for this section rather than invented for it.
- The bolder version should look more like the same brand, not less.
- Keep content true: existing claims are part of the scope; preserve them unless replacements are supplied, and ask for real evidence if the direction needs it.

## 289. Commit, Then Clarify
- Half-measures read as noise; make the one decisive move completely.
- Quiet everything around the move so it is legible.
- If every element got louder, the section got flatter.
- Give the target its own rhythm: a peak in the scroll, a shift in density or pace, not more of the same.

## 290. The Skeleton Test
- Strip the copy from the planned section and study the bare structure.
- The skeleton should still say what the section is and why it matters through hierarchy and system devices alone.
- If it only works once the words return, the boldness lives in text size, not design.
- An image placeholder names a job, an anchor and a piece of evidence, never a cue for a decorative stock photo.

## 291. Bolder Exit Checks
- Everything outside the target is unchanged.
- No new color, font or primitive appeared unasked.
- Conventions the section carried, especially anything that drives an action, still work the same way.
- The section is unmistakably the same brand, only more sure of itself.

# Part 29 — Making It Quieter

## 292. Quiet Design Needs Precision
- Apply when a design is too loud, aggressive or overstimulating.
- Quiet design is harder than bold design; subtlety without intent collapses to generic.
- Generic quiet looks like gray text on white, one sans at a uniform weight and a grid of identical cards; restraint still needs a point of view.
- Ask rather than guess when purpose, audience, what works or the core message are unclear.

## 293. Quieter by Visitor Mode
- Persuade and Experience surfaces: more restrained palette, more whitespace, more typographic air; drama reduced, not eliminated, and the point of view intact.
- Operate and Read surfaces: reduce visual noise with fewer background accents, flatter cards, less color and less motion so the tool disappears into the task.

## 294. Identifying Intensity Sources
- Color saturation that is too bright.
- Contrast extremes from too much high-contrast juxtaposition.
- Visual weight from too many bold, heavy elements competing.
- Animation excess and overly dramatic effects.
- Complexity from too many elements, patterns or decorations.
- Scale where everything is large and loud with no hierarchy.

## 295. Color Refinement
- Shift from full saturation to `70-85%` saturation.
- Replace bright colors with muted tones and use fewer colors more thoughtfully.
- Let neutrals dominate and use color as accent (the `10%` rule).
- Keep high contrast only where it matters most.
- Use warm or cool tinted grays instead of pure gray.
- Never put gray text on a colored background; use a darker shade of that color or transparency.

## 296. Visual Weight Reduction
- Reduce font weights: `900 → 600`, `700 → 500`; decrease sizes where appropriate.
- Build hierarchy through weight, size and space rather than color and boldness.
- Increase breathing room and reduce density.
- Thin borders, lower their opacity, or remove them.

## 297. Simplifying Decoration
- Remove gradients, shadows, patterns and textures that do not serve a purpose.
- Reduce border-radius extremes and simplify custom shapes.
- Flatten layering; reduce blur effects, glows and stacked shadows.

## 298. Motion Reduction
- Shorten travel distances to `10-20px` instead of `40px`.
- Keep functional motion; remove decorative flourishes.
- Replace dramatic effects with gentle feedback.
- Use ease-out-quart for smooth, understated motion; never bounce or elastic.
- Remove animations entirely when they serve no clear purpose.

## 299. Composition Refinement
- Reduce scale jumps; smaller contrast between sizes feels calmer.
- Bring rogue elements back onto the grid.
- Replace extreme spacing variations with a consistent rhythm.

## 300. Quieter Banned Moves
- Making everything the same size or weight; hierarchy still matters.
- Removing all color; quiet is not grayscale.
- Eliminating all personality.
- Sacrificing affordances on functional elements.
- Making everything small and light; some anchors are needed.
- Verify: still functional, still distinctive, easier to read for long periods, restrained rather than absent.

# Part 30 — Distilling / Simplifying

## 301. Simplicity Removes Obstacles, Not Features
- Strip a design to its essence: remove redundant elements, repeated information, decorative noise and cosmetic complexity.
- Every element must justify its existence.
- Find the ONE primary user goal and the `20%` that delivers `80%` of the value.
- Expect to say no to good ideas to make room for great execution.

## 302. Diagnosing Complexity
- Too many elements: competing buttons, redundant information.
- Excessive variation: too many colors, fonts, sizes and styles without purpose.
- Information overload: everything visible at once with no progressive disclosure.
- Visual noise: unnecessary borders, shadows, backgrounds.
- Confusing hierarchy and feature creep (too many options or paths).

## 303. Information Architecture Simplification
- Remove secondary actions and redundant information.
- Hide complexity behind clear entry points: accordions, modals, step-through flows.
- Merge similar buttons, consolidate forms, group related content.
- Hierarchy: ONE primary action, few secondary actions, everything else tertiary or hidden.
- If it is said elsewhere, do not repeat it here.

## 304. Visual Simplification
- Use `1-2` colors plus neutrals, not `5-7`.
- One font family, `3-4` sizes maximum, `2-3` weights.
- Remove borders, shadows and backgrounds that do not serve hierarchy or function.
- Flatten nesting; never nest cards inside cards.
- Cards are not needed for basic layout; use spacing and alignment instead.
- Use one spacing scale and remove arbitrary gaps.

## 305. Layout Simplification
- Replace complex grids with simple vertical flow where possible.
- Move sidebar content inline or hide it.
- Use available width generously instead of complex multi-column layouts.
- Pick left or center alignment and stick with it.
- Leave generous white space.

## 306. Interaction Simplification
- Fewer buttons and options; the paradox of choice is real.
- Smart defaults: make common choices automatic and ask only when necessary.
- Prefer inline editing over modal flows.
- Remove steps from flows wherever possible.
- ONE obvious next action, not five competing ones.

## 307. Content Simplification
- Cut filler, not meaning.
- Active voice: "Save changes", not "Changes will be saved".
- Plain language over jargon; scannable short paragraphs, bullets and clear headings.
- Remove marketing fluff and hedging.
- No headers restating intros, no repeated explanations: say it once.

## 308. Component Simplification
- Remove dead styles and unused components; flatten component trees.
- Consolidate similar styles.
- Question variant sprawl: `3` variants often cover `90%` of cases instead of `12`.

## 309. Distill Banned Moves
- Removing necessary functionality; simplicity is not feature-less.
- Sacrificing accessibility (clear labels still required).
- Mystery minimalism that leaves things unclear.
- Removing information users need to decide.
- Eliminating hierarchy entirely.
- Oversimplifying complex domains; match complexity to actual task complexity.
- Record why removed features went and whether they need an alternative access point; verify faster task completion and lower cognitive load.

# Part 31 — Adding Delight

## 310. Delight Is Character Through Useful Moments
- Delight is product character revealed through a useful interaction, a humane response or an unexpectedly considered detail, never a layer of generic whimsy.
- Persuade and Experience surfaces: personality may run through voice, composition, motion and discovery while the artifact stays the focus.
- Operate and Read surfaces: concentrate delight at first use, completion, recovery or mastery; reliability carries everything else.

## 311. Finding Delight Opportunities
- Effort worth acknowledging.
- Waiting that can become informative.
- An empty or first-use state that can orient.
- An error or recovery moment that needs empathy.
- An interaction whose physical or verbal response can express the brand.
- A useful capability people might enjoy discovering.
- Never manufacture a celebration for an ordinary click.

## 312. One Delight Thesis
- State in one sentence what the user should feel and why that feeling belongs to this product.
- Choose the smallest system that delivers it: a distinctive response to a meaningful action, product-specific language, a transition with recognizable material behavior, an illustration, sound, haptic or environmental detail from the product world, or a discovery that reveals real utility.
- Derive the treatment from product mechanism and visual world, not a stock catalog.

## 313. Delight by Emotional Moment
- Success: match the response to effort and consequence; milestones may expand, routine saves should simply feel certain.
- Waiting: show truthful progress or product-specific activity; never fake work or delay completion to stage a flourish.
- Empty and first use: make the next action clear before adding personality.
- Error and recovery: lead with the problem and the recovery; warmth helps, jokes must not trivialize loss, money, privacy or blocked work.
- Repeated interaction: still satisfying on the hundredth use; variation only when coherent and predictable.
- Discovery: reward curiosity without hiding required functionality.
- Copy uses the product's own language; generic whimsy is worse than neutral clarity.

## 314. Protecting the Experience From Delight
- Never delay, block or obscure the primary task.
- Never override platform conventions or accessibility.
- Never add unrequested factual claims.
- Never play sound without consent or ignore mute settings.
- Never make it mandatory, unskippable or exhausting on repeat.
- Keep dependency and asset cost proportional to the moment; stop nonessential loops when hidden.
- Scale celebration intensity to frequency and consequence.

## 315. Delight Verification
- The moment is specific enough that a neighboring product could not use it unchanged.
- It improves comprehension, confidence, motivation or emotional recovery.
- The interface stays fast and obvious without the flourish.
- Muted, keyboard, touch, screen-reader and localized paths all work.

# Part 32 — Going All-Out (Overdrive)

## 316. Context Defines Extraordinary
- Push an interface past conventional limits using the full power of the browser, not only visual effects.
- A particle system on a creative portfolio impresses; on a settings page it embarrasses.
- A settings page with instant optimistic saves and animated state transitions is also extraordinary.
- Ask what would make a user of THIS interface say "that's nice".
- Enhance how existing features feel; new product capabilities (real-time collaboration, offline support) are product decisions, not UI enhancements.

## 317. Propose Directions Before Building
- This is the intervention most likely to misfire.
- Sketch `2-3` directions varying technique, ambition and aesthetic, each with what it looks and feels like.
- State each direction's trade-offs (browser support, performance cost, complexity) inside the option itself.
- Build only the direction that is confirmed.

## 318. Extraordinary by Surface Type
- Visual and marketing surfaces: scroll-driven reveals, shader backgrounds, cinematic page transitions, generative art responding to the cursor.
- Functional UI: a dialog morphing from its trigger, a table rendering `100k` rows at `60fps`, streaming validation, drag-and-drop with spring physics.
- Performance-critical UI: search filtering `50k` items without a flicker, forms that never block the main thread.
- Data-heavy interfaces: GPU-rendered charts for massive datasets, animated transitions between data states, force-directed layouts that settle naturally.

## 319. Cinematic Transitions Toolkit
- View Transitions for shared-element morphing (list item into detail page, button into dialog); same-document works everywhere, cross-document lacks Firefox.
- `@starting-style` to animate from `display: none` with CSS only.
- Spring physics (mass, tension, damping) instead of cubic-bezier for natural motion.
- Scroll-driven animations (`animation-timeline: scroll()`) for parallax, progress and reveals; Firefox is flag-only, so always provide a static fallback.

## 320. Rendering Beyond CSS
- WebGL for shader effects, post-processing and particles.
- WebGPU for next-gen GPU compute; always fall back to WebGL2.
- Canvas 2D or OffscreenCanvas in a worker for custom or heavy rendering off the main thread.
- SVG filter chains (displacement, turbulence, morphology) for organic distortion.
- `@property` to animate gradients and complex values; Web Animations API for composable, cancellable, reversible choreography.

## 321. Making Data and Performance Feel Alive
- Virtual scrolling renders only visible rows for tens of thousands of items.
- Canvas/WebGL charts for datasets too large for SVG/DOM.
- Morph between chart states instead of replacing them.
- Web Workers and WASM move heavy computation off the main thread to prevent jank.
- Audio requires a user gesture and explicit opt-in; device APIs (orientation, light, location) sparingly and with permission.

## 322. Progressive Enhancement Is Non-Negotiable
- Every technique degrades gracefully; the experience without it must still be good.
- Gate features with capability checks (`@supports (animation-timeline: scroll())`, WebGPU then WebGL2 then CSS-only).
- Never use bleeding-edge APIs without a functional fallback.

## 323. Overdrive Performance Rules
- Target `60fps`; if it drops below `50fps`, simplify.
- Lazy-initialize heavy resources (WebGL contexts, WASM modules) only when near the viewport.
- Pause off-screen rendering.
- Test on real mid-range devices; never ship effects that jank there.

## 324. Polish and Focus in Overdrive
- The gap between cool and extraordinary is the last `20%`: spring easing, stagger offsets, subtle secondary motion.
- Verify effects visually in a running browser; code that runs can still stutter, ease wrong or land on the wrong frame.
- Never layer multiple competing extraordinary moments; focus creates impact, excess creates noise.
- Never use technical ambition to mask weak fundamentals.
- Tests: the wow test, the removal test (does anyone notice it gone?), the device test, the brand-context test.

# Part 33 — Clarifying Copy & UX

## 325. Auditing Interface Language
- Read the whole interaction path, not isolated strings.
- Flag ambiguous nouns and verbs, internal jargon, vague labels and states, missing consequences or timing, inconsistent terms and capitalization, redundant headings and helper text, text that breaks at real widths or in translation, and tone that ignores stress or risk.
- Ask before changing factual claims, legal meaning or domain-specific terms.

## 326. Message Hierarchy Per State
- Decide the one fact the user needs now, the next available action, supporting context that changes the decision, and the right tone.
- Say each idea once; if the heading explains the state, the intro adds new information or disappears.

## 327. Action and Navigation Labels
- Use a specific verb plus object when the outcome is not obvious.
- Describe what will happen, not the gesture that triggers it.
- Keep the same noun and verb for the same concept everywhere.
- Destructive actions name the object and consequence; prefer undo over confirmation when recovery is safe.
- Confirmations name the action on both message and button; banned labels: `Yes`, `No`, `OK`, `Submit`.

## 328. Form Copy
- Persistent labels; placeholders are examples, never labels.
- State format and eligibility requirements before submission.
- Explain why information is requested only when it is not obvious.
- Treat required and optional consistently.
- Validation says what needs attention and how to fix it, without blame, near the field and announced accessibly.

## 329. Actionable Error Messages
- Answer what failed, why (when known and useful), and how to recover or what alternative remains.
- Never make internal codes the primary message.
- Never promise a cause or resolution the system cannot know.
- Treat privacy, payment, deletion, access loss and blocked work seriously: warmth welcome, jokes not.

## 330. Loading, Empty and Success Copy
- Loading text names the real operation and sets an honest expectation for meaningful waits; show determinate progress when available and never invent it.
- Empty states distinguish first use, no results, filtered out, no permission and failure, and offer the next useful action.
- Success confirms the outcome and mentions the next consequence only when it changes what the user should do; routine success is brief.

## 331. Helper Text and Links
- Helper text answers an implicit question instead of restating the control.
- Put uncommon detail behind progressive disclosure.
- Link text makes sense out of context; icon-only controls need accessible names.

## 332. Voice, Accessibility and Localization in Copy
- Voice stays consistent; tone adapts to the moment.
- Write complete translatable messages, never concatenated fragments; keep variables structured so translators can reorder.
- Allow expansion instead of abbreviating prematurely.
- Alt text conveys the image's information; decorative images get empty alt.
- Screen-reader names match visible labels; never let punctuation, color or icons carry meaning alone.
- Keep a terminology glossary; never vary words for literary effect.
- Verify at target widths and `200%` zoom; final copy is as short as possible without losing meaning or recovery.

# Part 34 — Hardening (Edge Cases, Errors, i18n)

## 333. Designing for Imperfect Data
- Designs that only work with perfect data are not production-ready.
- Test extreme inputs: very long text (names of `100+` characters), empty or single-character text, emoji, RTL, accents, millions and billions, `1000+` list items, `50+` options, and no data.
- Test errors: offline, slow, timeout, `400`, `401`, `403`, `404`, `500`, validation, permission, rate limiting, concurrent operations.

## 334. Text Overflow and Wrapping
- Single-line truncation with ellipsis (`overflow: hidden; text-overflow: ellipsis; white-space: nowrap`).
- Multi-line clamp at a set number of lines (e.g. `3`).
- Allow wrapping with `overflow-wrap: break-word` and `hyphens: auto`.
- Flex and grid children need `min-width: 0` (grid also `min-height: 0`) to shrink below content size.
- Containers must expand with text; test at `200%` zoom.

## 335. Minimum Readable Text Sizes
- Body text `16px` minimum on mobile; `14px` only for genuinely secondary text.
- Inputs under `16px` trigger forced zoom in iOS Safari and break form layouts.
- Use `clamp()` for fluid marketing type.

## 336. Text Expansion for Translation
- Budget `30-40%` extra space for translations; German often runs `30%` longer than English.
- Banned: fixed widths on text containers or buttons (`w-24` style); size buttons with padding instead.
- Use flex/grid layouts that adapt to content.

## 337. RTL Support
- Use logical properties: `margin-inline-start`, `padding-inline`, `border-inline-end`, never left/right.
- Mirror directional icons under `[dir="rtl"]` (e.g. `scaleX(-1)` on arrows).

## 338. Arabic-Script Specifics
- Preserve the Zero-Width Non-Joiner (`U+200C`) used in Persian and Kurdish compounds; never strip or normalize it.
- Store Persian ی (`U+06CC`) and ک (`U+06A9`) as typed, but treat them as equivalent to Arabic ي (`U+064A`) and ك (`U+0643`) for search and validation.
- Use locale-aware digits (Eastern Arabic-Indic numerals for `fa-IR`, `ar-SA`) through locale number formatting, never hardcoded Western digits.
- Respect calendars: Solar Hijri for Persian users, Hijri for many Arabic-speaking users.

## 339. Character Sets, Dates, Numbers and Plurals
- UTF-8 everywhere; test CJK and emoji (`2-4` bytes) and Latin, Cyrillic and Arabic scripts.
- Format dates, numbers and currency with locale APIs (`1/15/2024` vs `15.1.2024`, `1,000` vs `1.000`).
- Banned: English-only pluralization logic; use a proper plural-rules library.

## 340. Network and API Error Handling
- Explain what happened, offer a retry button, offer offline mode where applicable, handle timeouts.
- `400`: show validation errors. `401`: redirect to login. `403`: permission error. `404`: not-found state. `429`: rate-limit message. `500`: generic error plus support route.
- Banned: generic "Error occurred" messages and blocking the whole interface when one component errors.

## 341. Form Validation Resilience
- Inline errors near fields with clear, specific messages and suggested corrections.
- Do not block submission unnecessarily; always preserve user input on error.
- Show constraints up front (e.g. "Letters and numbers only, up to `100` characters") tied to the field.
- Validate on the client for UX, always on the server for trust; sanitize inputs and rate-limit.

## 342. Empty, Loading and Large-Data States
- Empty: no items, no results, no notifications, no data, each with a clear next action.
- Loading: initial, pagination, refresh; say what is loading ("Loading your projects…") and give time estimates for long operations.
- Large datasets: pagination or virtual scrolling plus search and filter; never load `10,000` items at once.

## 343. Concurrency and Double Submission
- Disable the submit button while loading to prevent double submission.
- Handle race conditions; use optimistic updates with rollback and conflict resolution.
- Test by clicking submit `10` times rapidly.

## 344. Interrupted Gestures
- Applies to custom sliders, drag surfaces and scrollable control strips.
- A second pointer landing mid-drag must not hijack the drag; the first keeps its pointer or ends cleanly.
- On `pointercancel`, `lostpointercapture`, release outside the control or window `blur`, clear dragging state and release capture.
- The next tap or drag must work without a reload.
- State honestly whether gesture evidence came from emulation, synthesized touch, which engine, or a physical device.

## 345. Permission and Degradation States
- Distinguish no permission to view, no permission to edit and read-only, each with a clear explanation why.
- Core functionality works without scripts; images carry alt text; use feature detection, not browser detection, with fallbacks for unsupported CSS.

## 346. Accessibility Resilience
- Every function reachable by keyboard in a logical tab order; focus managed in modals; skip links for long content.
- Proper labels, live regions for dynamic changes, semantic structure.
- Test Windows high contrast mode; never rely on color alone.

## 347. Performance Resilience
- Progressive image loading, skeleton screens, optimistic UI, offline caching for slow connections.
- Clean up listeners, subscriptions, timers and pending requests.
- Debounce search input at `300ms`; throttle scroll handlers at `100ms`.
- Test throttled to 3G, offline, with a screen reader and keyboard only.

# Part 35 — Optimizing Performance

## 348. Measure Before Optimizing
- Identify the actual bottleneck for this interface, fix it, then measure again; do not optimize what is not slow.
- Measure Core Web Vitals, load time, bundle size, runtime frame rate and memory, and network waterfall.
- Ask what is slow, why, how bad (perceivable, annoying, blocking) and who is affected.
- Fix the biggest bottleneck first; ignore micro-optimizations while major issues remain.

## 349. Core Web Vitals Targets
- LCP under `2.5s`: optimize hero images, inline critical CSS, preload key resources, render on the server.
- INP under `200ms`: break up long tasks, defer non-critical scripts, move heavy work to workers.
- CLS under `0.1`: set dimensions on images and video, use `aspect-ratio` (e.g. `16 / 9`), reserve space for embeds, never inject content above existing content.

## 350. Image Optimization
- Modern formats (WebP, AVIF).
- Never load a `3000px` image for a `300px` slot; use `srcset` and `sizes` (e.g. `400w`, `800w`, `1200w`).
- Compress at `80-85%` quality, usually imperceptible.
- Lazy-load below-the-fold images only; never lazy-load above-the-fold content.

## 351. Script and CSS Weight
- Split code by route and component; tree-shake and remove unused dependencies.
- Lazy-load heavy components such as charts.
- Remove unused CSS, inline critical CSS and load the rest async.
- Use CSS containment for independent regions.

## 352. Font Loading
- `font-display: swap` or `optional`.
- Subset fonts (e.g. `unicode-range: U+0020-007F` for Basic Latin).
- Preload critical fonts, limit weights loaded, use system fonts where appropriate.

## 353. Loading Strategy and Network
- Load critical resources first; async/defer the rest; prefetch likely next pages.
- Combine small files, use SVG sprites for icons, inline small critical assets, remove unused third-party scripts.
- Paginate APIs, request only needed fields, compress responses, set caching headers, serve static assets from a CDN.
- Adapt loading to connection quality and prioritize requests.

## 354. Rendering Performance
- Avoid layout thrashing: batch all reads, then all writes.
- Flatter, smaller DOM trees render faster.
- Use `content-visibility: auto` for long content and virtual scrolling for very long lists.
- Bound expensive paint areas for blur, filter and shadow effects; smaller and isolated is faster.

## 355. Animation Performance
- Animate `transform` and `opacity` for reliable movement; blur, filters, masks, clip paths, shadows and color shifts are allowed when they add meaningful polish.
- Avoid casually animating layout properties (`width`, `height`, `top`, `left`, margins).
- Target `16ms` per frame (`60fps`); use frame-synced scripting and CSS animations where possible.
- Use `will-change` sparingly; on everything it creates layers and wastes memory.
- Use intersection observation to trigger lazy loading and reveals.

## 356. Framework Re-render Discipline
- Memoize expensive components and computations; avoid creating inline functions in render.
- Minimize re-renders, debounce expensive operations, lazy-load routes.

## 357. Verifying Performance Wins
- Compare before/after metrics and track real-user monitoring.
- Test on low-end Android, not just a flagship phone; throttle to 3G.
- Desktop browsers on fast connections are not representative.
- Never sacrifice accessibility or break functionality for speed; check that it feels faster.

# Part 36 — Adapting Across Screens

## 358. Adaptation Is Rethinking, Not Scaling
- Adapting to another screen, device, platform or use case means rethinking the experience, not scaling pixels.
- Identify source assumptions (large screen, mouse, fast connection) and target context: device, input method, screen constraints, connection, usage posture (on-the-go glance vs focused desk use), platform expectations.
- List what won't fit, what won't work (hover on touch, tiny targets) and what is inappropriate.

## 359. Desktop to Mobile
- Single column, vertical stacking, full-width components, bottom navigation.
- Touch targets `44x44px` minimum, never hover-dependent; more spacing between targets.
- Bottom sheets instead of dropdowns; controls within thumb reach (bottom is easier than top).
- Progressive disclosure, primary content first, secondary in tabs or accordions, shorter copy, text `16px` minimum.
- Hamburger or bottom navigation, sticky headers for context, back button in flow.

## 360. Tablet Hybrid
- Two-column layouts, side panels, master-detail (list plus detail).
- Adapt to orientation (portrait vs landscape).
- Support touch and pointer; keep `44x44px` targets while allowing denser layouts than phone.
- Side navigation drawers and multi-column forms where appropriate.

## 361. Mobile to Desktop
- Multi-column layouts, always-visible side navigation, multiple panels at once.
- Constrain with max-width; do not stretch to 4K.
- Add hover detail, keyboard shortcuts, context menus, drag and drop, Shift/Cmd multi-select.
- Show more upfront: wider data tables, richer visualizations, more detail.

## 362. Print Adaptation
- Page breaks at logical points; remove navigation, footer and interactive elements.
- Black and white or limited color; proper binding margins.
- Expand shortened content (full URLs, hidden sections); add page numbers, headers, print date and title; convert charts to print-friendly forms.

## 363. Email Adaptation
- `600px` max width, single column, inline styles, table-based layout for client compatibility.
- Large obvious button CTAs rather than text links; no hover states.
- Deep-link to the web app for complex interactions.

## 364. Breakpoints
- Typical ranges: mobile `320px-767px`, tablet `768px-1023px`, desktop `1024px+`.
- Prefer content-driven breakpoints: start narrow, stretch until the design breaks, add a breakpoint there.
- Three usually suffice (`640`, `768`, `1024px`); use `clamp()` for fluid values between them.
- Write mobile-first with `min-width` queries; desktop-first makes mobile load unnecessary styles.

## 365. Layout Adaptation Techniques
- Grid and flexbox reflow; container queries adapt to the container, not the viewport.
- Use `display: none` sparingly; hidden content still downloads.
- Navigation in three stages: hamburger plus drawer on mobile, compact horizontal on tablet, full with labels on desktop.
- Tables become cards on mobile using block display with per-cell labels.
- Use native disclosure elements for content that collapses on mobile.

## 366. Detect Input, Not Screen Size
- Screen size does not reveal input: touchscreen laptops, tablets with keyboards.
- Fine pointer: e.g. `8px 16px` button padding; coarse pointer: e.g. `12px 20px`.
- Apply hover effects only under `(hover: hover)` (e.g. `translateY(-2px)` lift); use active states for touch.
- Never rely on hover for functionality.

## 367. Safe Areas
- Pad with `env(safe-area-inset-*)` on all four sides for notches, rounded corners and home indicators.
- Use fallbacks such as `max(1rem, env(safe-area-inset-bottom))`.
- Enable `viewport-fit=cover` in the viewport meta.

## 368. Responsive Images and Art Direction
- `srcset` with width descriptors plus `sizes` (e.g. `(max-width: 768px) 100vw, 50vw`) lets the browser pick by viewport and pixel ratio.
- Use the picture element with media sources when different crops or compositions are needed, not just resolutions.

## 369. Custom Control Gesture Checks
- A slider can pass every width check and still refuse to drag on iOS.
- Tap it, then drag it with the target input; the drag must complete, not just start.
- A swipe along the page's scroll axis across the control scrolls the page without activating it; a drag starting on the control along its axis moves the control, not the page.
- Screenshots and resized viewports verify layout, never gestures; Chromium is not Safari.

## 370. Cross-Screen Banned Moves
- Hiding core functionality on mobile.
- Assuming desktop means a powerful device, or that all mobiles are powerful.
- Different information architecture across contexts.
- Breaking platform expectations; forgetting landscape; ignoring touch on desktop.
- Generic breakpoints applied blindly; device detection instead of feature detection; separate mobile and desktop codebases.
- Trusting emulation alone: it misses real touch, CPU limits, latency, font rendering and browser chrome; test at least one real iPhone, one real Android, a tablet, and extremes of `320px` and 4K.

# Part 37 — Adapting to Native

## 371. Native Adaptation Assessment
- Identify source assumptions (phone-only, portrait-only, one platform's idioms, a website).
- Identify the target device class (phone, tablet, foldable), orientation, platform and posture (one-handed on the go vs two-handed at rest).
- Find what breaks: navigation that doesn't fit, layouts that stretch instead of restructure, gestures or controls that don't exist there.

## 372. Phone to Tablet
- Restructure, never stretch; a scaled-up phone UI on a tablet is the failure mode.
- Switch structure with size classes (iOS) or window size classes (Android).
- Tab bar stays or becomes a sidebar on iPad; Android navigation bar becomes a rail or drawer at expanded width.
- Use the width: split view, master-detail, multi-column grids, popovers where phones used sheets.
- Multitasking can hand a phone-width window on a tablet; size-class-driven layout handles both.

## 373. Orientation and Foldables
- Landscape restructures into side-by-side panes and repositioned controls; never clip or letterbox.
- Lock orientation only when the task truly demands it, never to dodge a layout bug.
- Foldables react to posture and hinge; test folded, unfolded and tabletop.

## 374. Translating Idioms Between iOS and Android
- Tab bar ↔ navigation bar, rail or drawer.
- Edge-swipe back and back chevron ↔ predictive Back gesture and button.
- Switch, segmented control, system pickers ↔ Material switch, chips, Material pickers.
- Action sheet ↔ bottom sheet or Material dialog.
- SF Symbols, SF Pro, Dynamic Type ↔ Material Symbols, Roboto, sp scaling.
- Semantic system colors and materials ↔ Material color roles and tonal elevation.
- System push/sheet transitions ↔ container transform, shared-axis, fade-through.
- Rebuild navigation and controls in the target's vocabulary; carry over only the brand's expressive layer (palette intent, type accent, motion personality) through the target's theming.

## 375. Web to Native
- Reconform, don't reflow.
- Replace web navigation with the platform model, HTML-shaped controls with platform controls, hover affordances with touch-first ones, px type with Dynamic Type or sp.
- Hold the result to the full platform rules.

## 376. Native Implementation Rules
- Drive structure from size classes, never device-model checks.
- Respect safe areas and window insets in every configuration (notch, hinge, status bar, keyboard).
- Simulators for breadth, hardware for truth: at least one phone and one tablet per shipped platform, both orientations, split screen where supported.
- Banned: stretched phone layouts on tablets, porting one platform's controls onto the other, hiding core functionality on small devices.

# Part 38 — iOS Design Rules

## 377. The iOS Trust Test
- Would a fluent iPhone user trust this app or pause at off-spec controls?
- The tell is "ported from a website": reinvented navigation bars, custom back gestures, web-shaped buttons, hover-dependent affordances.
- Platform conventions govern structure, navigation and interaction in every mode; brand expresses through tint, type, motion and content.
- Default to platform components; depart only for a reason the user would thank you for.

## 378. iOS Layout and Navigation
- Lay out inside safe-area insets; no controls under the notch, Dynamic Island, home indicator or rounded corners.
- Tab bar for `2–5` top-level sections (sections, never actions), navigation stack for hierarchy, sheet for self-contained tasks.
- No custom global navigation and no mixed metaphors.
- Never disable or overlay the left-edge swipe-back gesture.
- Large titles on top-level screens, collapsing to inline on scroll; deep detail screens stay inline.

## 379. iOS Touch Targets
- `44×44 pt` minimum for every tappable control, with breathing room between adjacent targets.

## 380. iOS Typography
- Use system text styles (Large Title through Caption) so text follows Dynamic Type; no hard-coded point sizes.
- SF Pro / SF Compact carries body, labels and controls; a brand face may appear only in display moments.
- `11 pt` floor; Body is `17 pt`.

## 381. iOS Color and Materials
- Semantic system colors (label, secondaryLabel, systemBackground, separator, tint); raw hex breaks in Dark Mode and increased contrast.
- Dark Mode is a first-class appearance: design and test both.
- One tint color drives interactive elements; decoration is not its job.
- System materials for blur and translucency behind bars and sheets; no hand-rolled glassmorphism.

## 382. iOS Components and Controls
- Use platform controls: switch, segmented control, stepper, system pickers, action sheets, alerts, context menus, swipe actions; reinventing them is the most common native slop.
- SF Symbols for icons (baseline-aligned, type-aware, weight and scale variants); never mix in a web icon set.
- Sheet for a focused dismissible sub-task, full-screen cover for immersion, clear Cancel/Done, honor swipe-to-dismiss unless data loss needs a guard.
- Grouped/inset lists for settings-shaped content; no bespoke card stacks.

## 383. iOS Motion and Verification
- System transitions: push slides, sheets rise, dismiss reverses the entrance; custom transitions that fight navigation disorient.
- Honor Reduce Motion with crossfades instead of parallax and large slides.
- Capture screenshots from the simulator, never a browser, for every shipped device class (an iPhone, and an iPad when targeted).
- Check Dark Mode and a large Dynamic Type size to catch truncation; say whether evidence came from simulator or hardware.

# Part 39 — Android Design Rules

## 384. The Android Trust Test
- Would a fluent Android user trust this app or trip on off-spec components?
- The common tell is an iOS app wearing Android's skin: iPhone-style bottom-only nav, a back arrow ignoring system Back, Cupertino switches and dialogs.
- Material 3 governs structure, navigation and interaction; brand expresses through its theming (color roles, type scale, shape, motion).
- A Material-everywhere cross-platform app still owes iPhone hardware safe-area insets, Reduce Motion and edge-swipe back.

## 385. Android Layout and Navigation
- Navigation bar (bottom, `3–5` destinations) at compact width; navigation rail or drawer at expanded width; never ship a phone bottom bar untouched on a tablet.
- System Back always works: honor predictive Back and the Back button; never trap or hijack it.
- Edge-to-edge with status bar, navigation bar, display cutout and keyboard insets so nothing hides behind system UI.
- Top app bar for screen context, paired with a FAB when the screen has one primary action.

## 386. Android Touch Targets
- `48×48 dp` minimum for every target, with at least `8 dp` between them.

## 387. Android Typography
- Map text to Material roles (Display, Headline, Title, Body, Label, each large/medium/small); never hand-pick sizes per screen.
- Roboto is the system face; theme a brand face through the type scale while keeping body, labels and controls legible.
- Use `sp` units, never fixed px, so type follows system font size.

## 388. Android Color and Theming
- Material color roles (primary, on-primary, surface, surface-variant, secondary-container, outline, error); raw hex breaks light/dark and contrast variants.
- Dynamic Color from the wallpaper on Android `12+` where it fits, with a static fallback.
- Dark theme is a first-class scheme, never a quick invert.
- Convey elevation through standard tonal surface levels (plus shadow where appropriate); no arbitrary drop shadows.

## 389. Android Components and Motion
- Material components: filled/tonal/outlined/text buttons, FAB, switches, chips, snackbars, bottom sheets, dialogs, navigation bar/rail/drawer; never port iOS controls or invent equivalents.
- One FAB for one primary action; never stack FABs or spend one on a secondary task.
- Snackbars for transient feedback (actionable when useful); dialogs only for decisions that must interrupt.
- Material motion: container transform, shared-axis, fade-through with standard easing and durations; honor Remove animations with a crossfade or instant cut.

## 390. Android Verification
- Capture from an emulator or device, never a browser, for every shipped device class.
- Check dark theme and font scale `1.3` to catch clipped labels; restore settings afterward.
- Emulators give breadth; gestures, refresh rates and performance need hardware.

# Part 40 — Design Modes

## 391. Persuade Mode
- Applies to marketing and conversion surfaces where the design is what the visitor judges, so the world may own and structure the page.
- The opening makes the offer intelligible and desirable, exposes a clear action and demonstrates something only this product can prove.
- The action is the working form visitors came for (route-and-dates search, open appointment slots, add to cart); a decorative link to it elsewhere does not count.
- Conversion lives inside the form's own vocabulary: a one-line hook, a visible primary action, a legible reading order.
- A committed form that hides the offer or the action has not finished translating.

## 392. Experience Mode
- Applies to portfolio and work-led surfaces: the work itself leads from the first viewport.
- When the world's source is itself an interface language, the surface may carry its native grammar across navigation, content, controls and states, within native platform conventions.

## 393. The World Carries the Page, Never Pictures It
- A facade, shutter or book can be what the page is built on; a viewport painted whole as a facade, book cover or poster with no working parts is a picture, not a website.
- Material coverage is wanted: the world's material is the ground and major surfaces, its type sets the headlines; a world reduced to an accent on a neutral template is the default with a sticker.
- Coverage is not performance: limit how many regions act out the concept; the rest stay in the world's material without performing.
- Banned templates: the split hero (copy one side, product the other, badge row under it) and a centred headline over a row of equal cards.

## 394. Parts Must Still Work Where the World Puts Them
- Navigation set into a facade still reads as links; copy on a shutter reads as set text; an action on a door plaque is plainly clickable.
- Text reads against whatever sits behind it; sections keep a steady vertical rhythm; the primary action is unmistakable; the next section starts as a section.
- Fix a poster by making its parts work in place, never by moving them into a standard layout on the world's colour.

## 395. The Single-Object Rule
- When the world is an object, the page is that one object seen once, at one scale, from one point of view, in its real form.
- A book opens to two pages on one gutter, never a third panel; a spine carrying navigation belongs to the same book.
- More content goes on the object's own surfaces or the next spread below, never on extra copies or impossible folds.
- Alternative compositions each go further, never cleaner: more structure carried by the world (still one dominant move), a larger or stranger focal move, or a composition the category would not attempt.

## 396. Read Mode
- Applies to docs, guides, articles and changelogs: the visitor came to understand something, so the page is first a document of its kind.
- The reader's question leads; comprehension and wayfinding stay intact at every step.
- The world owns the frame (masthead, navigation rail, ground, title and section openers, how code, tables and callouts are set) and commits fully there.
- The reading column stays calm: a reading face, real contrast, a real measure, nothing performing behind text.
- The world never supplies the reading order or replaces navigation with something a reader must learn.

## 397. Read Mode Rules
- Best sources: reference books, type specimens, timetables, field guides, technical manuals, scholarly apparatus, newspaper wayfinding.
- Tools, instruments or fictional interfaces become costumes on a reading page; take only type, palette, density and one signature move.
- Design the first viewport as the document shell: navigation and current location, title and opening that answers the question, the column, and the way forward (contents, headings, next/previous).
- Measure about `60 to 75` characters with body near `16px` on the web; native apps use the platform body style and readable width.
- Monospace is for code, parameters and small labels, never running text or default headings.
- Code, tables, notes and figures use standard forms in the world's type and palette; the signature move is one system used where it earns its place, never a frame around every element.
- Variants change navigation model (sidebar tree, top tabs, inline contents), column and margin system, reference density and signature placement, never the column; each must differ at thumbnail size.
- Self-check: can the reader tell where they are and read comfortably? Cover the name: if it could be any product's docs, push the frame further; if it reads as an artifact before a document, pull the world back from the column.

## 398. Operate Mode
- Applies to apps, dashboards, settings, tables and tools: the visitor came to get a job done, so the page is first a working product of its category.
- A category-fluent user should know where everything is before noticing the world.
- The world lends exactly four things: type, palette, density and one signature move; never layout, navigation model or controls.
- Colour does real jobs: a committed shell palette (coloured rail or header, tinted ground), state colours, data series, selection and the signature move.
- A grey screen with one accent is the category default without the category's polish, not restraint.

## 399. Operate Mode Rules
- Tools and instruments from the audience's world (terminal, scope, control panel, cockpit) return as costumes; take only the four contributions.
- Design the first viewport as the product shell: navigation, work areas and their jobs, the data read first and its states, then the signature move.
- Name the signature move concretely (service health drawn as a transit map, a schedule set in timetable column rhythm); a world that shows only as a colour scheme has not found its move.
- Every control is a standard one: buttons, tabs, inputs, selects, filters, sortable table headers, navigation that reads as navigation.
- Banned costumes: function-key bars, command prompts, instrument bezels, ruled ledger paper standing in for a table.
- Finish bar is the best product in the category: aligned grid, consistent spacing, real type scale, clear hierarchy; the signature move adds to that, never replaces it.
- Use realistic data with plausible values and units and show one meaningful state (alert, degraded service, empty filter result).
- State colours (red critical, amber degraded) sit on the palette only where they carry meaning; a headline number that moves shows recent history with the change onset marked.
- Variants change organisation (side rail, top bar, command-first), work-area division, leading data, density, signature placement; more world texture or ornament goes the wrong way.

# Part 41 — Operational Interfaces

## 400. Earned Familiarity
- Applies to app UIs, admin dashboards, settings, data tables, tools and authenticated surfaces.
- Test: can a category-fluent user trust the interface immediately, or must they pause at every subtly-off component?
- The failure mode is strangeness without purpose: over-decorated buttons, mismatched controls, gratuitous motion, display fonts in labels, invented affordances.
- The tool should disappear into the task.

## 401. Product Typography
- One well-tuned sans family can carry headings, buttons, labels, body and data.
- Use a fixed rem scale, not fluid clamp-sized headings.
- Tighter scale ratio of `1.125–1.2` between steps.
- Prose keeps `65–75ch` line length; data and compact UI can run denser; tables at `120ch+` are fine.
- Read surfaces take these typography and consistency rules, with prose measure and navigation mattering more than density.

## 402. Product Color
- Restrained is the default floor; a surface can earn Committed (one category colour carrying a report, a drenched onboarding welcome).
- Standardize a state vocabulary: hover, focus, active, disabled, selected, loading, error, warning, success, info.
- Accent only for primary actions, current selection and state indicators, never decoration.
- A second neutral layer for sidebars, toolbars and panels, slightly cooler or warmer than the content surface.
- Banned: heavy colour or full-saturation accents on inactive states.

## 403. Product Layout and Components
- Responsive behavior is structural (collapse sidebar, responsive table, breakpoint-driven columns), not fluid type.
- Every interactive component ships default, hover, focus, active, disabled, loading and error states.
- Skeletons for loading, not spinners in the middle of content.
- Empty states teach the interface, never just "nothing here".
- Consistent affordances: same button shape, same form-control vocabulary, same icon style; if "save" looks different in two places, one is wrong.
- Overlays must escape clipping containers (`overflow: hidden`/`auto`); use dialog, popover, fixed positioning or a portal.

## 404. Product Motion
- `150–250 ms` on most transitions; users are in flow.
- Motion conveys state change, feedback, loading or reveal, nothing else.
- No orchestrated page-load sequences.

## 405. Product Bans and Permissions
- Banned: decorative motion, inconsistent components across screens, display fonts in labels, buttons or data, reinvented affordances (custom scrollbars, odd form controls, non-standard modals), modal as first thought.
- Exhaust inline and progressive alternatives before reaching for a modal.
- Permitted: system fonts and familiar sans defaults, standard navigation (top bar plus side nav, breadcrumbs, tabs, command palettes), high density, consistency over surprise with delight saved for moments.

# Part 42 — Region Mapping a Page

## 406. What a Region Map Is
- A region map names what is actually visible in an approved comp before producing assets.
- It is neither a page build nor an asset approval.
- Each region has a stable id, a kind, a note and exactly one bound (pixel box, normalized box or grid cells) measured on the original comp's dimensions.

## 407. Bounding Regions Accurately
- Compare every bound against the original, inspecting excluded foreground pixels as well as geometry.
- Bound separate text elements separately so artwork in the gaps stays visible.
- A container describes the layout extent of its children and never replaces them.
- Overlapping non-container boxes mask their full area, including empty space inside them.
- Zero errors does not certify accuracy and coverage warnings are hints, not proof; correct and re-inspect.
- Automatic horizontal banding is scaffolding, not element identification.

## 408. Containment
- A parent container region encloses child regions; parent and children keep separate ids and crops.
- Containment never transfers approval from parent to child.

## 409. Split by What Varies Independently
- Separate content the site swaps (room photos, products, people), moving parts (anything a hover or signature interaction moves) and structure (frames, surrounds, ornament).
- A window with open shutters onto a room is three kinds of region: the surround as a plate with a transparent opening, the room as an image beneath, and each shutter as its own plate.
- Overlapping regions are composited in the page; a single raster that bakes a frame together with the view it opens onto should be flagged and split.

## 410. Painted Material
- A text, control or chrome region whose crop looks painted (many colours, soft gradients) is suspect.
- Classify painted material (a figure, a photograph, a metal or paper surface) as plate, image or texture, rather than leaving it as code-drawn text or chrome.
- Comp crops are reference evidence only, never production assets.

# Part 43 — Design Critique Method

## 411. Stable Target
- Resolve the critique to one concrete surface (a specific page, component, or URL) before judging anything.
- Prefer the source of a surface over a transient preview address when both identify it; addresses drift, sources do not.
- "The homepage" means the actual index page; "the settings modal" means its primary component; "this page" means the current view.
- Honor a standing list of accepted or ignored findings: drop matching findings silently rather than re-raising them.

## 412. Two Independent Assessments
- Run two separate assessments: a design-director review (judgment) and an evidence pass (automated scan plus rendered inspection).
- Keep them isolated: neither may see the other's output until synthesis.
- Finish the judgment review before any automated findings enter the synthesis; deterministic output still anchors judgment.
- A run that collapses both into one context is degraded and must say so up front, never silently.
- An evidence pass that is skipped without a genuine failure makes the critique a failed critique.
- Viewable surfaces require rendered inspection, not source reading alone, whenever a browser is available.
- Native app surfaces get the judgment review alone; web-markup scanning does not apply, and an empty scan of native source must not be read as clean.

## 413. Evidence Hygiene
- Each assessment inspects in its own fresh view; never reuse a view another pass already touched.
- Never claim a visible overlay or annotation exists unless it was actually rendered in the page.
- For multi-view surfaces, inspect `3-5` representative pages, not just the first.
- For single-window desktop apps, assessments take turns and each leaves the window exactly as found (route, scroll, theme, open panels); keep the window on screen or pixel contrast reads are skipped.
- Prefer test profiles and test data when inspecting a running app.
- Any temporary server started for inspection runs in the background with a known stop method and is stopped before reporting.

## 414. Synthesis
- Weave the two assessments together; never concatenate them.
- Note where judgment and automated scan agree, what the scan caught that judgment missed, and which scan findings are false positives.
- The full structured critique is the deliverable; never replace it with a summary and a link.
- Write the whole report first; the follow-up questions are the last thing, with nothing after them.
- A critique ends either with targeted questions or an explicit "questions skipped" line naming the reason; ending on the report alone is incomplete.

## 415. Critique Voice
- Be direct: vague feedback wastes everyone's time.
- Be specific: "the submit button," not "some elements."
- Say what is wrong and why it matters to users.
- Give concrete fixes; cut "consider exploring..." entirely.
- Prioritize ruthlessly: if everything is important, nothing is.
- Do not soften criticism; honest feedback is what ships good design.

# Part 44 — Critique Dimensions

## 416. Design Specificity
- Start here: does the composition, interaction, and visual language feel authored for this product, or could an unrelated product use it unchanged?
- Make this judgment before seeing any automated findings.
- Cover overall coherence, structural sameness, category-interchangeable choices, and missed opportunities for product character.
- Summarize automated findings separately, with counts and locations, and flag false positives.

## 417. Holistic Design Review
- Judge hierarchy, information architecture, emotional fit, discoverability, composition, typography, color, accessibility, states, copy, and edge cases.
- Think like a design director, not a linter.
- Return: specificity verdict, heuristic scores, cognitive load, emotional journey, `2-3` strengths, `3-5` priority issues, persona red flags, minor observations, and provocative questions.

## 418. Emotional Journey
- Apply the peak-end rule: the most intense moment and the final moment dominate the remembered experience.
- Find emotional valleys: points of confusion, anxiety, or let-down along the primary path.
- Check for reassurance at high-stakes moments (payment, deletion, submission, irreversible choices).

## 419. Overall Impression
- Give a brief gut reaction: what works, what does not, and the single biggest opportunity.

## 420. What Is Working
- Highlight `2-3` things done well and say specifically why they work.
- Never skip positive findings; they tell the team what to preserve and replicate.

## 421. Priority Issues
- List the `3-5` most impactful design problems, ordered by importance.
- For each: name the problem, why it matters to users or goals, and a concrete fix.
- Tag each with a severity from `P0` to `P3`.

## 422. Minor Observations and Questions to Consider
- Collect smaller issues worth addressing as quick notes, separate from priority issues.
- Close the analysis with provocative questions that could unlock better solutions, e.g. "What if the primary action were more prominent?", "Does this need to feel this complex?", "What would a confident version of this look like?"

# Part 45 — Cognitive Load

## 423. Three Types of Cognitive Load
- Intrinsic load is the task's inherent complexity: you cannot remove it, only structure it.
- Manage intrinsic load by breaking tasks into discrete steps, scaffolding (templates, defaults, examples), progressive disclosure, and grouping related decisions.
- Extraneous load is caused by bad design and is pure waste: eliminate it ruthlessly.
- Sources of extraneous load: navigation that requires mental mapping, unclear labels, visual clutter, inconsistent patterns, unnecessary steps between intent and result.
- Germane load is the good effort of learning toward mastery.
- Support germane load with gradual disclosure, consistent patterns that reward learning, confirming feedback, and onboarding that teaches through action rather than walls of text.

## 424. Cognitive Load Checklist
- Single focus: can the primary task be completed without competing elements distracting?
- Chunking: is information in digestible groups of `≤4` items?
- Grouping: are related items visually grouped (proximity, borders, shared background)?
- Visual hierarchy: is it immediately clear what is most important?
- One thing at a time: can the user settle one decision before the next?
- Minimal choices: `≤4` visible options at any decision point?
- Working memory: does the user need to remember something from a previous screen to act here?
- Progressive disclosure: is complexity revealed only when needed?
- Scoring: `0-1` failures = low load (good); `2-3` = moderate (address soon); `4+` = high (critical fix).
- Report every decision point with more than `4` visible options.

## 425. Working Memory Rule
- People hold `≤4` items in working memory at once (Cowan's revision of Miller's law).
- Count the distinct options, actions, or facts a user must consider simultaneously at each decision point.
- `≤4` items: manageable; `5-7`: pushing the limit, group or disclose progressively; `8+`: overloaded, users skip, misclick, or abandon.
- Action buttons: `1` primary, `1-2` secondary, the rest grouped in a menu.
- Navigation: `≤5` top-level items, the rest grouped under clear categories.
- Long-form articles: one reading path; gather related links into a single block at the end rather than mid-flow.
- Documentation sidebars: `≤4` sibling choices visible per level before grouping.
- Portfolio and gallery indexes: one decision per screen (which piece to open), not filter, sort, and tag controls at once.

## 426. Common Cognitive Load Violations
- Wall of options: `10+` choices with no hierarchy; fix by grouping, highlighting a recommendation, and disclosing progressively.
- Memory bridge: info from step 1 needed at step 3; keep context visible or repeat it where needed.
- Hidden navigation: users must build a mental map; always show current location (breadcrumbs, active states, progress).
- Jargon barrier: domain language forces translation; use plain language and define unavoidable terms inline.
- Visual noise floor: every element has equal weight; establish one primary element, `2-3` secondary, everything else muted.
- Inconsistent pattern: similar actions behave differently; same type of action gets the same type of UI.
- Multi-task demand: reading, deciding, and navigating at once; sequence the steps.
- Context switch: jumping between screens, tabs, or modals to gather info for one decision; co-locate what each decision needs.

# Part 46 — Usability Heuristics

## 427. Heuristic Scoring Discipline
- Score all ten heuristics on a `0-4` scale; a `4` means genuinely excellent, not "good enough."
- Most real interfaces score `20-32` out of `40`.
- Pair each score with its key issue, or note that it is solid.
- A heuristic that genuinely cannot apply may be scored `n/a` with a one-line reason; Flexibility and Efficiency and Help and Documentation commonly are on persuasive or experiential surfaces (landing pages, campaigns, portfolios).
- The maximum is `4` × the number of heuristics scored: `/40` when all apply, `/32` when two are `n/a`; never print `/40` over a partial set.
- When comparing scores over time, note when runs scored different heuristic sets; they are not like-for-like.

## 428. Heuristic Rating Bands
- `36-40` Excellent: minor polish only, ship it.
- `28-35` Good: address weak areas, solid foundation.
- `20-27` Acceptable: significant improvements needed before users are happy.
- `12-19` Poor: major UX overhaul required, core experience broken.
- `0-11` Critical: redesign needed, unusable as is.
- With `n/a` heuristics, read the band from percentage: `90%+` Excellent, `70%+` Good, `50%+` Acceptable, `30%+` Poor, below that Critical (e.g. `24/32` = `75%` = Good).

## 429. Visibility of System Status
- Check loading indicators for async work, confirmation of actions (save, submit, delete), progress for multi-step processes, current location in navigation, and inline form validation rather than submit-only.
- `0` no feedback, user guessing; `1` rare feedback; `2` partial, major gaps; `3` most operations give clear feedback; `4` every action confirms and progress is always visible.

## 430. Match Between System and Real World
- Check familiar terminology, information order matching expectations, recognizable icons and metaphors, audience-appropriate language, and natural reading flow.
- `0` pure tech jargon; `1` requires domain expertise; `2` mixed, jargon leaks; `3` mostly natural, an occasional term needs context; `4` speaks the user's language throughout.

## 431. User Control and Freedom
- Check undo/redo, cancel on forms and modals, clear routes back to safety, easy clearing of filters, search, and selections, and escape from long or multi-step flows.
- `0` users get trapped, refresh is the only way out; `1` obscure exits; `2` main flows escapable, edge cases not; `3` most actions exit and undo; `4` undo, cancel, back, and escape everywhere.

## 432. Consistency and Standards
- Check consistent terminology, same action giving same result everywhere, platform conventions, visual consistency (color, type, spacing, components), and same gesture meaning same behavior.
- `0` feels like different products stitched together; `1` similar things look or behave differently; `2` main flows match, details diverge; `3` occasional deviation, nothing confusing; `4` cohesive and predictable.

## 433. Error Prevention
- Check confirmation before destructive actions, constraints against invalid input (date pickers, dropdowns), smart defaults, clear labels, and autosave with draft recovery.
- `0` no guardrails; `1` few safeguards; `2` common errors caught, edge cases slip; `3` most error paths blocked proactively; `4` errors nearly impossible through smart constraints.

## 434. Recognition Rather Than Recall
- Check visible rather than buried options, contextual help (tooltips, inline hints), recent items and history, autocomplete and suggestions, and text labels on icons.
- `0` heavy memorization of paths and commands; `1` many hidden features; `2` main actions visible, secondary hidden; `3` most things discoverable; `4` users never need to memorize.

## 435. Flexibility and Efficiency of Use
- Check keyboard shortcuts for common actions, customization, recents and favorites, bulk/batch actions, and power features that do not complicate the basics.
- `0` one rigid path; `1` few alternatives; `2` basic keyboard support, limited bulk; `3` keyboard nav and some customization; `4` multiple paths, power features, customizable.

## 436. Aesthetic and Minimalist Design
- Check that only necessary information shows at each step, hierarchy directs attention, color and emphasis are purposeful, and no decorative clutter competes.
- `0` everything competes equally; `1` too much noise; `2` main content clear, periphery noisy; `3` focused with minor noise; `4` every element earns its pixel.

## 437. Error Recognition, Diagnosis, and Recovery
- Check plain-language messages (no codes for users), specific problem identification ("Email is missing @", not "Invalid input"), actionable recovery, errors shown near their source, and non-blocking handling that never wipes the form.
- `0` cryptic codes or no message; `1` "Something went wrong" with no guidance; `2` names the problem, not the fix; `3` identifies problem and next steps; `4` pinpoints, suggests a fix, and preserves the user's work.

## 438. Help and Documentation
- Check searchable help, contextual help (tooltips, hints, guided tours), task-focused rather than feature-focused organization, concise scannable content, and access without leaving context.
- `0` no help anywhere; `1` hard to find or irrelevant; `2` FAQ or docs exist, not contextual; `3` searchable and mostly task-focused; `4` the right info at the right moment.

## 439. Issue Severity
- `P0` Blocking: prevents task completion; fix immediately.
- `P1` Major: significant difficulty or confusion (or a WCAG AA or platform-guideline violation); fix before release.
- `P2` Minor: annoyance with a workaround; fix in the next pass.
- `P3` Polish: no real user impact; fix if time permits.
- Tiebreaker: "Would a user contact support about this?" If yes, it is at least `P1`.
- Not everything can be `P0`; keep `P3`s few, because a long tail of minor issues buries the ones that matter.

# Part 47 — Persona and Audience Checks

## 440. Persona Method
- Select `2-3` archetypes most relevant to the interface and walk the primary user action as each.
- Report specific red flags naming exact elements and interactions that failed; never write generic persona descriptions.
- Example form: "No keyboard shortcuts; primary action takes 8 clicks; forced modal onboarding; high abandonment risk."

## 441. Impatient Power User
- Expert with similar products; hates hand-holding; skips onboarding; looks for shortcuts, bulk select, batch edit, automation; abandons anything slow or patronizing.
- Can the core task be done in under `60` seconds? Are there shortcuts? Can onboarding be skipped entirely? Do modals dismiss with Esc? Is there a power path?
- Red flags: forced or unskippable tutorials, no keyboard path for primary actions, slow unskippable animations, one-at-a-time workflows where batch is natural, redundant confirmations for low-risk actions.

## 442. Confused First-Timer
- Never used this kind of product; reads everything; hesitates at the unfamiliar; misreads jargon; takes labels literally; abandons rather than figures it out.
- Is the first action obvious within `5` seconds? Are all icons labeled with text? Is there contextual help at decision points? Does terminology assume prior knowledge? Is there a back or undo at every step?
- Red flags: icon-only navigation, unexplained jargon (e.g. raw "404 Not Found"), no visible help, ambiguous next steps after an action, no confirmation of success.

## 443. Accessibility-Dependent User
- Uses a screen reader and keyboard-only navigation; may have low vision, motor impairment, or cognitive differences; tabs linearly; relies on labels and heading structure; cannot perceive hover-only cues; may zoom to `200%`.
- Can the full primary flow be completed by keyboard? Are all interactive elements focusable with visible focus? Do images have meaningful alt text? Does text meet `4.5:1` contrast? Are loading, success, and error changes announced?
- Red flags: click-only interactions, missing or invisible focus indicators, meaning by color alone (red = error, green = success), unlabeled fields or buttons, time limits without extension, custom components that break screen-reader flow.

## 444. Deliberate Stress Tester
- Probes past the happy path: empty states, very long strings, special characters, emoji, RTL text, pasted spreadsheet data; navigates backwards, refreshes mid-flow, opens multiple tabs.
- What happens at `0` items, `1000` items, very long text? Do errors recover or leave the UI broken? Is state preserved on refresh? Do features appear to work but produce wrong results?
- Red flags: silent failures, errors exposing technical details or leaving broken UI, empty states with no guidance ("No results" alone), data lost on refresh or navigation, inconsistent behavior between similar interactions.

## 445. Distracted Mobile User
- One-handed, thumb only, frequently interrupted, switching apps, low patience, possibly on a slow connection, prefers taps over typing.
- Are primary actions in the thumb zone (bottom half)? Is state preserved on leave and return? Does it work on `3G`? Are autocomplete and smart defaults used? Are touch targets at least `44×44pt`?
- Red flags: key actions at the top of the screen, progress lost on interruption, large text inputs where selection would do, heavy assets on every page with no lazy loading, tiny or crowded tap targets.

## 446. Persona Selection by Interface Type
- Landing or marketing: first-timer, stress tester, mobile user (first impressions, trust, mobile).
- Dashboard or admin: power user, accessibility user.
- E-commerce or checkout: mobile user, stress tester, first-timer.
- Onboarding flow: first-timer, mobile user.
- Data-heavy or analytics: power user, accessibility user.
- Form-heavy or wizard: first-timer, accessibility user, mobile user.

## 447. Project-Specific Personas
- When real audience and brand context exists, derive `1-2` extra personas for the primary archetype the standard five miss.
- Define each with a profile (`2-3` traits), behaviors (`3-4`), and red flags (`3-4` things that would alienate them).
- Never invent audience details; with no real context, use only the standard personas.

# Part 48 — Critique Follow-Up

## 448. Targeted Follow-Up Questions
- Ask `2-4` questions maximum, each tied to specific findings; never ask a generic "who is your audience?"
- Each question offers `2-3` concrete answer options, not open-ended prompts.
- Priority direction: which of the top `2-3` issue categories to tackle first.
- Design intent: if tone mismatched, was it intentional? Offer `2-3` tonal directions (warmer, bolder, more playful) that would fix what was found.
- Scope: everything, top `3` only, or critical issues only.
- Constraints (only if relevant): which areas are off-limits or already done.
- Skipping questions is allowed only when fewer than `3` priority issues were found; count them rather than judging by feel.

## 449. Action Plan From Critique
- Order recommendations by the user's stated priorities first, then by impact.
- Map every priority issue to a concrete action; skip actions that address zero issues.
- Respect chosen scope and off-limits areas.
- Each action carries enough context to know what to focus on.
- End with a final polish step whenever any fixes were recommended, and re-critique after fixes to measure improvement.

# Part 49 — Web Audit Checklist

## 450. Audit Stance
- An audit is a technical, code-level check of what is measurable and verifiable, not a design critique.
- Document issues; do not fix them during the audit.
- Score five dimensions `0-4` each, total `/20`.
- Verify every automated finding in context before reporting; never report unverified false positives.
- Explain the impact of every issue and make every recommendation specific and actionable.
- Record each issue with severity, location, category, user impact, the standard it violates, and the recommended fix.

## 451. Accessibility Audit
- Text contrast below `4.5:1`, or below `3:1` for large text (`7:1` for AAA).
- Reduced-motion preference needs an intentional alternative that preserves state change and hierarchy; flag a global `0.01ms` kill that destroys useful feedback, flashing above threshold, and motion that blocks focus, reading, or task completion.
- Interactive elements lacking roles, labels, or states.
- Missing focus indicators, illogical tab order, keyboard traps.
- Improper heading hierarchy, missing landmarks, divs used as buttons.
- Missing or poor image descriptions.
- Inputs without labels, poor error messaging, missing required indicators.
- `0` inaccessible (fails WCAG A); `1` major gaps (few labels, no keyboard nav); `2` partial; `3` WCAG AA mostly met; `4` AA fully met, approaching AAA.

## 452. Performance Audit
- Layout thrashing: reading and writing layout properties in loops.
- Expensive animation: casual layout-property animation, unbounded blur/filter/shadow, effects that visibly drop frames.
- Images without lazy loading; unoptimized assets.
- `will-change` applied broadly or left on at rest; it is a targeted hint for known expensive animations, not a baseline.
- Unnecessary imports and unused dependencies; unnecessary re-renders and missing memoization.
- `0` severe (layout thrash, nothing optimized); `1` major (no lazy loading, expensive animation); `2` partial; `3` mostly optimized; `4` fast, lean, well optimized.

## 453. Theming Audit
- Hard-coded colors outside design tokens.
- Broken dark mode: missing variants, poor dark-theme contrast.
- Wrong or mixed token types.
- Values that do not update on theme switch.
- `0` everything hard-coded; `1` minimal tokens; `2` tokens exist but used inconsistently; `3` minor hard-coded values; `4` full token system with flawless dark mode.

## 454. Responsive Audit
- Fixed widths that break on mobile.
- Touch targets under `44×44px`; WCAG AA (SC 2.5.8) requires at least `24×24` CSS px unless an exception applies (spacing, equivalent control, inline text, user-agent styling, essential size).
- Spacing exception passes when a `24` CSS px circle centered on the target overlaps no other target and no other undersized target's circle.
- Broken touch interaction: custom sliders, drag surfaces, and scrolling control strips whose gesture fails under touch, swallows page scroll, loses the drag to scroll, or sticks after an interrupted gesture.
- Code tells of broken touch: mouse-only handlers, no `touch-action` on a pointer-drag surface, drag state never cleared on cancel, lost capture, or blur.
- Exercise gestures with real or synthesized touch where possible (a rendered viewport proves layout, not the gesture) and state what produced the evidence and what stayed untested.
- Horizontal overflow on narrow viewports; layouts that break when text size increases; missing mobile/tablet variants.
- `0` desktop-only; `1` many failures; `2` works on mobile with rough edges; `3` minor target or overflow issues; `4` fluid at all viewports, proper targets, gestures work under touch.

## 455. Implementation Integrity Audit
- Treated as the critical dimension; give a pass/fail verdict first: does the implementation express a coherent, product-specific system?
- Look for repeated implementation shortcuts, design-system drift, misleading or decorative content, and structure interchangeable with an unrelated product.
- Keep deterministic findings separate from visual judgment and call out false positives.
- `0` systemic drift; `1` major repeated failures; `2` several verified issues; `3` minor isolated issues; `4` coherent and intentional.

## 456. Audit Rating Bands and Reporting
- `18-20` Excellent (minor polish); `14-17` Good (address weak dimensions); `10-13` Acceptable (significant work); `6-9` Poor (major overhaul); `0-5` Critical (fundamental issues).
- Executive summary: total score and band, issue counts by severity, top `3-5` critical issues, next steps.
- Identify systemic patterns rather than one-offs, e.g. "hard-coded colors in 15+ components" or "touch targets consistently under 44px across mobile."
- Include positive findings: good practices to maintain and replicate.
- Order recommendations `P0` first, then `P1`, then `P2`, ending with a polish pass.

# Part 50 — Native App Audit

## 457. Native Audit Stance
- Audit native apps from source against the platform's own conventions (Human Interface Guidelines, Material); browser tooling does not apply.
- Same five-dimension, `/20` structure and bands as the web audit; `P1` includes platform-guideline violations.
- Record the violated guideline for each issue; location is screen, file, and line.

## 458. Native Accessibility
- Interactive elements without accessibility labels, traits/roles, or state announcements.
- Illogical reading or focus order, unreachable controls, focus lost on navigation.
- Fixed point sizes defeating Dynamic Type (iOS) or px instead of sp (Android); layouts that clip or overlap at large sizes.
- Touch targets below `44 pt` (iOS) or `48 dp` (Android), or crammed without spacing.
- Reduce Motion ignored: parallax and large slides with no crossfade alternative.
- Text failing contrast in either light or dark appearance.
- `0` screen reader unusable; `1` unlabeled controls, no scaling; `2` labels exist, order or scaling breaks; `3` minor gaps; `4` labeled, ordered, scales cleanly, Reduce Motion honored.

## 459. Native Performance
- Heavy work at launch before first frame.
- Long content without list virtualization or recycling.
- Synchronous work in scroll or gesture paths; dropped frames at `60/120 Hz`.
- Unnecessary re-renders or recompositions; missing memoization or keys.
- Full-size images decoded for thumbnails; no image caching.
- Bloated bundle or binary; unused dependencies.
- `0` janky everywhere; `1` unvirtualized lists, slow launch; `2` partial; `3` minor improvements possible; `4` fast launch, smooth scroll, lean.

## 460. Native Appearance and Theming
- Raw hex instead of semantic system colors (iOS), Material color roles (Android), or tokens.
- Missing dark variants, poor dark contrast, quick inverts.
- Android 12+ Dynamic Color with no static fallback scheme, or ignored where it fits.
- Hand-rolled visual materials where system materials or tonal elevation are expected.
- `0` hard-coded everything; `2` tokens used inconsistently; `4` semantic throughout, both appearances first-class.

## 461. Platform Conformance
- The critical native dimension; verdict first: does this read as a native app or a ported website? Be brutally honest and list violations.
- Broken system gestures: edge-swipe back disabled (iOS), predictive Back hijacked (Android).
- Inset violations: content under the notch, Dynamic Island, home indicator, status bar, or keyboard.
- Off-platform navigation: custom global nav, overloaded tab bars, one platform's patterns on the other.
- Web-shaped controls: HTML-style buttons, custom toggles, hover-dependent affordances.
- Icon drift: mixed icon sets instead of the platform's symbol set.
- System drift: repeated shortcuts or decorative patterns conflicting with product, platform, or design system.
- `0` web port, nothing native; `1` `3-4` kinds of heavy violation; `2` `1-2` noticeable; `3` subtle issues; `4` fully native, a fluent user trusts every screen.

## 462. Native Adaptivity
- Tablets rendering a stretched phone layout instead of using size classes.
- Landscape clipped, ignored, or locked without reason.
- Inputs hidden behind the keyboard; no inset adjustment.
- Split View or multi-window breaking layout.
- Foldables: hinge-unaware layouts on posture change.
- `0` one screen size only; `1` landscape or tablet broken; `2` partial; `3` minor edge cases; `4` adapts across sizes, orientations, and windowing.

# Part 51 — Polish Pass

## 463. Polish Is Refinement
- Polish never conceals a redesign: preserve the incumbent visual world, content, behavior, and everything out of scope.
- If the concept itself is wrong, say so and recommend a redesign or bolder direction rather than smuggling in a replacement.
- An automated scan result is evidence of defects, not proof of quality; inspect the rendered experience and the real interaction path.
- A clean scan never replaces visual judgment.

## 464. Classifying Drift
- Read the design system, tokens, shared components, patterns, and neighboring flows first; without a formal system, follow coherent project conventions.
- Missing token: the system needs a reusable value.
- One-off implementation: an existing shared component or pattern should replace it.
- Conceptual mismatch: flow, information architecture, or hierarchy differs from comparable product areas.
- Local defect: the implementation is simply incomplete or inconsistent.
- Fix the cause at the narrowest correct level; ask when a binding system principle cannot be inferred.

## 465. Polish Evidence
- Use the feature yourself at representative sizes: desktop and mobile on web; shipped device classes on native.
- Establish whether the path is functionally complete, the quality bar and time available, known constraints or deliberately unfinished work, and the states, content lengths, roles, and input methods users will meet.
- Use any current prior critique's high-severity findings as one input, but always do an independent pass.

## 466. Polish Triage Order
- 1: broken or blocked tasks, data loss, misleading state, inaccessible paths.
- 2: missing loading, empty, error, success, disabled, and permission states.
- 3: flow, hierarchy, responsive, and design-system drift.
- 4: visual and motion inconsistencies.
- 5: code and asset cleanup.
- Do not perfect one corner while the rest stays below the same bar.

## 467. Flow and Hierarchy Polish
- Match neighboring mental models, terminology, disclosure, routing, save behavior, and optimistic or pessimistic update patterns.
- Make the primary task and current state obvious without flattening everything to equal weight.
- Connect arrival, transition, empty, and recovery paths instead of treating screens as isolated.

## 468. Layout and Type Polish
- Align to the grid and spacing scale; fix optical as well as mathematical alignment.
- Group related content tightly; separate distinct groups generously.
- Keep same-role typography consistent; test measure, wrapping, localization expansion, zoom, and font loading.
- Verify every supported viewport, not just the current screenshot.

## 469. Color, Imagery, and Icon Polish
- Use semantic tokens and keep color meanings stable across themes.
- Verify text, control, and focus contrast in every state.
- Keep icon families, stroke weight, sizing, and optical alignment coherent.
- Prevent image layout shift with correct aspect ratios, responsive sources, and useful alt text.

## 470. Interaction and State Polish
- Every control needs default, hover, focus, active, disabled, loading, error, and success behavior.
- Preserve visible keyboard focus, logical tab order, labels, and platform-appropriate touch targets.
- Keep motion coherent, interruptible, and performant; never add animation merely to make polish visible.
- Validate long, missing, localized, offline, slow, and permission-limited content where the product can meet it.

## 471. Content and Code Polish
- Keep terminology, capitalization, punctuation, and factual copy consistent; ask before changing claims.
- Remove debug output, dead code, unused imports, obsolete styles, and polish-created duplication.
- Replace custom implementations with shared components where the system owns the pattern.
- Promote genuinely reusable values to tokens; never create a system abstraction for one local exception.

## 472. Polish Verification
- Walk the whole path again with mouse, keyboard, and touch where applicable.
- Check mobile, intermediate, and wide layouts on web; phone and tablet size classes in both supported orientations on native.
- Check loading, empty, error, success, disabled, long-content, and missing-content states.
- Check zoom, contrast, focus, semantics, and screen-reader names.
- Check console errors, layout shift, interaction latency, and image loading; supported browsers on web; supported OS versions, runtime warnings, and dropped frames on native.
- Check agreement with the design system, neighboring features, and agreed scope.
- Finish by reviewing the diff for accidental churn, orphaned code, redundant values, and temporary artifacts; document only narrow intentional exceptions.
- Ship only when the feature is functionally complete and consistently finished across the path.

# Part 52 — Plan and Asset Review

## 473. Review Before Code
- On comp-led builds, review assets and the production plan once every raster region has its plate, before any page code exists.
- The approved comp is the reference.
- The reviewer judges two things: the plates that will ship, and which regions code will draw.
- A painted region planned as code is the most expensive mistake a comp-led build makes; this checkpoint exists to catch it.
- Text, controls, and chrome are judged later, in the assembled first viewport.
- Apply the reviewer's decisions as given; never substitute your own favorable verdict, and never approve on their behalf.
- An unattended review is pending work, not an approval; do not build past it.

## 474. Acting on Review Decisions
- Approve: once every item is approved and the inventory confirmed, move to the first viewport.
- Revise a plate: regenerate it in place with the feedback.
- Revise with split: break an asset into layers: a frame plate with a transparent opening at the same box, the content seen through it as its own image at the opening's box, and each moving part (a shutter, a door) as its own plate; name each layer after the original region.
- Revise a plan item: resize or extend a raster region, split a material into its own plate, or adjust a code region.
- Reclassify: move a code region to a raster kind and rewrite its description to name the material.
- Missing: add the region, producing its plate if raster.
- Any spec change, or a plate replaced after acceptance, requires a new review round; unchanged decisions carry over so only changes are re-shown.

## 475. First Viewport Review
- Assemble the first viewport from the approved plates and plan, and gate it before human review; human review does not waive integrity checks.
- After `3` failed first-viewport attempts, or `3` failed responsive attempts before acceptance, stop iterating and let the human eye decide.
- Acceptance closes human review for that build; never ask again for plan, asset, or assembly approval.
- After acceptance, numeric readings become advisories, but material vetoes still hold: a missing or unreferenced plate, an SVG illustration, an organic clip, a clipped plate, invented ink, failed rendered presence.
- A text, control, or chrome region missing from the accepted screenshot is settled by acceptance; a missing plate is a question for the user.
- If the build drifts from the accepted screenshot, restore what was accepted.
- The accepted first viewport is the visual direction for the rest of the page; it is calibration, not a claim the rest was reviewed.
- A later explicit user change is a new task.
- Keep the real page and its behavior; never strip behavior to pass review.

# Part 53 — Finish Review

## 476. Fresh-Eyes Finish Review
- Review the finished artifact against its direction contract, the approved comp, and the chosen world's quality bar.
- Inventory the comp's salient elements in your own words before reading the builder's contract or summary; a review anchored on the builder's abstraction inherits what it dropped.
- Calibrate against the comp and the quality bar, never against the visible effort.
- The builder's narration of fixes is not evidence; only what captures show counts.

## 477. Capture Evidence Check
- Before anything else, verify every required capture exists and is valid: the full viewport set (web: desktop and mobile; native: one per shipped device class) plus any reported user viewport.
- Valid means no black or blank regions, content matching what the capture claims, the document top visible on full-page captures, and dimensions sensible for the viewport.
- A missing capture fails exactly like a malformed one: a viewport nobody captured is a viewport nobody inspected.
- When any capture fails, demand recapture and review nothing else; a verdict on broken evidence launders the breakage into approval.

## 478. Process Persistence Check
- The product brief exists.
- On comp-led builds, every build phase before review is closed or explicitly skipped; an open or failed phase is a material finding.
- A skipped comp round (the build ran from a world description alone) is a material finding that outranks craft.
- A forced phase is a material finding unless the user downgraded the comp in their own quoted words.
- A first-viewport fidelity score under `0.72`, or no proof of reproduction, means the reproduction ran unproven.
- Comps that exist without a recorded approval pick mean the approval point was skipped.
- When the design-system document predates the build (extension or redesign), it must match the built world.

## 479. Fidelity Matrix
- Start from measured per-region verdicts; every region scored missing or contradicted stays so unless the paired crop proves the score wrong, with a stated reason.
- A region scored match still gets an eye for lettering character and material, which numbers do not measure.
- Check topology, reading order, focal scale, overlaps and z-order, density, signature geometry, the primary action's treatment, navigation items and icons, headline levels and scale relationships.
- A CTA the comp physically works, dissolves, or stamps is a signature element; a plain-rectangle rendition is contradicted.
- Classify every salient element: match, acceptable adaptation, missing, contradicted, or added without approval.
- An adaptation is intentional only when it cites the user answer, brief, accessibility need, or product truth that forced it; an uncited deviation is a defect.
- A missing signature element, changed topology, or unapproved added content fails fidelity and outranks every craft point.
- The comp is the spec for composition, topology, element inventory, density, lettering character, and material; it is not a pixel spec for semantics, accessibility, or responsive reflow, and that allowance covers translation, never replacement.

## 480. Mandatory Type Row
- Compare the display lettering's character, compression, width, weight, contrast, and terminals against the comp.
- A face of a different character is contradicted however well the layout matches.

## 481. Mandatory Material Row
- An element rendered as flat CSS or clean vector where the comp shows painted, textured, dimensional, or photographic material is contradicted regardless of placement; medium is part of the promise.
- Without an approved comp, judge type and material against the stated world and its real materials.
- Faked physicality (CSS bevels, embossing, stamped-metal or chalk effects imitating a material never actually rendered) is contradicted on its face; imitation material is the most reliable mark of machine-made design.

## 482. Mandatory Ground Row
- Compare the page field's value and temperature against the comp, sampled from pixels on both sides rather than from memory, as the net on-screen result where texture paints over the base.
- A ground warmer or cooler than the comp's is contradicted however faithful the layout.
- Hunt drift toward default renditions: warm cream on light grounds, blue-black slate on dark.
- Without a comp, a color the stated world names is the target; when it names none, there is no ground authority and the review says so rather than inventing a target.

## 483. Rebuild Threshold
- When material is contradicted on the focal element, or contradiction is the rule rather than the exception, stop listing repairs: the first fix is a rebuild of named regions with the assets to produce.
- A patch list against a rejected page launders rejection into approval.
- A fix that needs an asset says so explicitly ("produce this region as a raster asset"), never as a style tweak that invites a CSS answer.
- A rebuild return gets a fresh full review, not scoring of the directive alone.

## 484. Reference Comps on Code-Led Builds
- A comp used only as critique reference is provocation, not spec: no element matrix, no adaptation citations, no asset obligations.
- Its one contribution is what the image dared that the build did not; worthwhile dares enter as ordinary ordered fixes.

## 485. Quality Ceiling Check
- Against the world's quality bar, name the native devices the build left unused: frame, depth, lettering treatment, ornament density, motion.
- The quality bar governs commitment and finish, never composition.

## 486. Contract Promise Check
- Verify the direction contract was genuinely derived (its concept reference is present and corroborated); a missing or uncorroborated reference means the concept step was skipped, a material fix ahead of craft.
- For each block of the direction contract (thesis, own world, story, first viewport, form), does the render keep the promise?
- Apply the memory test to the first viewport: what would a visitor remember?

## 487. Truth Check
- Demonstration data is authored and labeled synthetic.
- No invented commercial claims; unanswered claims appear as marked placeholders, not silent omissions.
- Every raster region ships as its produced plate, not a gradient, inline SVG, or many-vertex clip standing in for it.
- Every produced asset is visibly present in the captures; an asset at near-zero opacity or buried behind a wash is a compliance token, not shipped material.

## 488. Craft Floor Check
- Hold the captures against the refuse list: kickers and eyebrows, hard offset shadows outside a neobrutalist world, glyph icons, system display faces, gradient text, side stripes, and the rest.
- A banned element is a material fix even when the comp shows it; comp fidelity cannot authorize what the floor refuses.

## 489. Finish Disposition
- Exactly four outcomes: recapture, rebuild, fix, ship.
- Derived, never felt: recapture when evidence failed; rebuild when the rebuild threshold fired; fix when any material fix exists; ship only when there are no material fixes and no contradicted or missing rows.
- A page a design director would send back is fix at best however functional; a page whose focal craft sits far below the comp is rebuild however complete its structure.
- The disposition is reported verbatim and may not be softened.
- Return: process check, fidelity matrix, unused ceiling devices, ordered material fixes (fidelity ahead of craft, at most `8`, each one line tied to a check or promise), and one line naming what must not be diluted while fixing; no praise, no summary prose.

## 490. Verdict Pass After Fixes
- On post-fix captures, score each prior material fix as resolved, partial, or unresolved, based only on what the new captures show.
- A fix answered mechanically (positions moved but the named quality still absent) is partial at best.
- Name at most `3` regressions the fix batch introduced; no new hunt.
- User-supplied screenshots contradicting a prior verdict trigger a new full review with the user's captures as primary evidence.
- Unresolved or partial findings can never recompute to ship; a ship here covers the scored fixes, not the whole surface.

# Part 54 — Asset Quality

## 491. Production, Not Redesign
- Asset production is cleanup of an approved reference, not new art direction.
- Preserve the reference's visual role, silhouette, palette, lighting, material, texture, camera angle, and composition.
- Keep perspective only when it belongs to the object or scene; strip presentation chrome (card transforms, shadows, rounded clipping, borders, layout) that code should draw.
- Never add objects, restyle, or reinterpret; never produce anything the inventory does not list.

## 492. Plate Definition
- Every raster region ships as a plate: the region regenerated at asset resolution with the same subject, composition, palette, lighting, and material, with UI text and page chrome removed.
- Plate resolution: at least `1.5x` the comp region's pixel size, at the region's aspect.
- Code draws text, controls, radius, shadow, and layout; the plate carries what code cannot draw.
- Crops of the comp are references, never shipping pixels; a shipped crop is how a beautiful comp becomes a blurry site.
- Region kinds: plate, image, texture (raster); text, control, chrome (code).

## 493. Transparent Versus Opaque
- An isolated figure, object, or line drawing on the page ground is a transparent cutout.
- A photograph, full-frame illustration, or texture stays opaque.
- Cutouts preserve reference placement, clear margins, white paint, fine edges, and interior holes.
- Use native alpha; never chroma-key or flatten transparent output; a painted checkerboard is not transparency.

## 494. Plate Inspection
- Compare each plate beside its crop for subject, placement, scale, palette, and style.
- For cutouts, verify a real alpha channel and composite on both light and dark grounds: white paint stays solid, interior holes clear, fine edges free of halos.
- Inspect glass and soft shadows carefully; partial alpha alone does not guarantee convincing translucency.
- On a miss, tighten the brief and regenerate once; after two misses keep the better plate and flag the named drift for review.

## 495. Frame Plates
- A window, doorway, or arch is a transparent cutout with an opening kept fully transparent.
- Verify the opening's alpha: no baked view, no glow or vignette halo across it.
- The content seen through the opening is its own image region, produced at the opening's size.

## 496. Decision Comps
- A decision comp renders one direction as a north-star first viewport at full fidelity: the product and the visitor's job with real content, what leads, parts in reading order, and the frame.
- Take the look from the direction's world: its reference images, or two to four sentences of concrete look.
- A native app or mobile-first surface is a portrait frame at device viewport, never a landscape default.
- Every sibling comp renders at the same fidelity, one surface, one aspect, each in its own grammar; equal commitment keeps the comparison honest.
- Real product name and real content only; never invent commercial claims, prices, benchmarks, or dates.
- Claim exclusions do not remove a medium the world has not excluded: a subject that lives in photographs keeps its photographs.
- A brief too thin to compose from is reported, never padded from imagination.

# Part 55 — Comp Fidelity

## 497. Why Builds Drift From Comps
- Builds lose comps through invented chrome the comp never showed, materials flattened to CSS, illustrations approximated as SVG or clip paths, produced textures buried under opaque washes, and a first viewport with the comp's section order but none of its craft.
- Self-judging a reproduction from memory of an image is unreliable; translate mechanically wherever pixels are involved.
- Keep judgment for what it is good at: structure, semantics, controls, motion, responsive logic.
- Code-led builds look better only because they have no target to fail against.

## 498. Fidelity Scoring Axes
- Structure: blurred grayscale similarity with a small translation tolerance.
- Color: quantized histogram overlap plus dominant-palette match.
- Detail: high-frequency energy ratio per cell, i.e. did the material survive?
- Bands: do horizontal section boundaries line up?
- Weight by region kind: a plate region is judged mostly on detail, a text region on structure.
- Per-region verdicts: match, drift, missing, contradicted.
- Calibration: a comp shifted `12px` still scores about `87%` (match); a recolored comp drops to about `34%`; sibling comps of the same world score `55-59%` against each other, which separates "same design" from "same world, different composition."

## 499. Fidelity Thresholds
- First viewport must reach at least `0.72` with no region missing and at most a third contradicted.
- Each plate must score at least `0.5` against its reference crop and be at least `1.5x` the region's pixel width.
- Human pass judgments sit at about `68-73%` overall; fails ranged `43-68%`.
- Above the first-viewport floor, numeric readings (ink colors, letter-spacing, line pitch, strip heights, box positions) advise rather than block and belong to the polish pass before responsive work.
- Hard vetoes hold at any score: a missing region, a contradicted plate or text block, an inline-SVG illustration, a clipped plate, invented ink.
- A passed plate is judged on placement (present in its box, at its box), not pixel identity with the comp.

## 500. Region Inventory
- Name every comp region by grid span with a kind (plate, image, texture, text, control, chrome); anything not in the inventory does not exist on the page.
- Every region needs a description.
- A code-drawn kind whose description names painted material (drawings, illustrations, technical diagrams) is refused; it must be raster.
- No text, control, or chrome region may cover more than a quarter of the comp unless it is explicitly a container.
- Text and control regions snap to the largest ink mass in their span so one box does not straddle two elements.
- A plate box whose artwork runs off its edge is refused; artwork must not be clipped.
- Any override of a classification rule must stay visible in the record, never silently vanish.

## 501. Typography Fidelity
- Choose faces by measured shape, not by name: glyph width and x-height relative to cap height, stem width, stroke contrast, serif ratio, ink density, vertical ink profile.
- Match cap height, width class, weight class, and tracking to the comp.
- Check per text region: cap height, line count, ink density, line pitch, first-line offset, ink color, and letter-spacing against the comp crop.
- Common type misses: wrong face, too thick, wrong size, wrong line height, different wraps, wrong position, extra space above, text color changed (e.g. black rendered white), letter-spacing too wide.
- Below about `10px` cap height, size by the box rather than by face matching.
- Estimated sizing without measurement has inflated headlines to `186-247%` of the comp's cap height; measure.

## 502. Invented Ink and Missing Content
- Never add hallucinated kickers, dividers, legends, buttons, decorative squares, or extra copy the comp lacks; strong ink over a calm comp area is invented content (veto at about `4%` of the frame or two strongly inked cells).
- A region with under `15%` of the comp's detail is missing, e.g. a footer or bottom menu pushed below the fold.
- Navigation bars and header strips must match the comp's height; a header divider too far down is a fidelity miss.
- Controls sit in their comp box and position.

## 503. Material and Asset Fidelity
- Never ship a painted region as SVG; inline-SVG illustrations are banned, while icon-sized single-path SVG (roughly `13-42px`) is legitimate.
- Organic clip shapes (a polygon with `10+` off-grid vertices, or a path with `3+` curves) standing in for torn, cut, or painted edges are refused; geometric clips (cut corners, diagonals, hexagons, arrows, circles, insets) pass.
- A raster buried under a wash with all stops at `≥0.9` alpha and no blend mode, or shown at opacity under `0.15`, counts as not shipped; lighter tints, blends, and visible opacities pass.
- Produced assets must be placed and referenced; correct assets left unused on disk are a fidelity failure.
- Never ship a resampled crop of the comp as an asset (crops are never allowed).
- Do not add shadow or depth the comp does not have; flat on the comp means flat on the build.

## 504. Controls and Icons Fidelity
- Close-enough icon glyphs are acceptable.
- Arrows, chevrons, dropdown chrome, and control borders and fills belong to the comp and are held like text.
- Wrong, undersized, or missing icons remain reviewable even where not measured.

## 505. Acceptable Deviations
- A deviation that genuinely improves the result (a color that fixes contrast, a label moved for clarity) is allowed when the contract justifies it, but the comp wins at the first viewport and the change belongs to a stated later pass.
- Flat operational surfaces (dashboards, editors) have few or no plates; region inventory and diffing still apply.

# Part 56 — Banned AI Copy Phrases & Patterns

## 506. Marketing Buzzwords
- Never write `streamline your`, `empower your`, `supercharge your`, `unleash your`, `unleash the power`, `leverage the power` or `harness the power`. These verbs describe no action the product performs and are instant generated-copy tells.
- Never use `best-in-class`, `industry-leading`, `world-class`, `enterprise-grade`, `next-generation`, `cutting-edge`, `mission-critical`, `best of breed`, `future-proof` / `future proof`. Unprovable superlatives read as filler.
- Never write `transform your business`, `revolutionize`, `game-changer` or `game changing`. Hype verbs promise change without naming what changes.
- Never write `seamless experience`, `seamlessly integrate`, `drive engagement`, `drive growth` or `drive results`. Name the specific integration or the specific metric instead.
- Never write `built for the modern`, `trusted by leading` or `trusted by the world`. Vague social proof with no named customer reads as invented.
- A single buzzword on the page is enough to fail. Replace it with a concrete verb and noun that says literally what the product does.

## 507. Aphoristic Cadence
- Never close three or more sections with a short rebuttal pair such as `X. No Y.` or `X. Just Y.` One instance can be voice; three is a template.
- Never use the manufactured-contrast aphorism `Not a feature. A platform.` (`Not a/an …` followed by a short counter-sentence) as a recurring section closer.
- Limit punchy two-sentence rebuttals to once per page. The repetition, not the single line, is what reads as machine cadence.

## 508. Em-Dash Saturation
- Limit em-dashes in body copy: never reach `8` or more em-dashes (`—` or `--`) at a density of roughly one per `500` characters of body text.
- A long article with a handful of em-dashes is fine; saturation is the tell. Prefer commas, colons, periods or parentheses.
- Count encoded dashes too (`&mdash;`); the reader sees the same glyph however it was typed.

## 509. Theater Framing
- Never dismiss a practice as `… theater`: `security theater`, `compliance theater`, `growth theater`, `privacy theater`, `process theater`, `productivity theater`, `innovation theater`, `alignment theater`, `metrics theater` and similar. It is a recurring generated-copy tic.
- Say plainly what the thing does or fails to do instead of calling it a performance of itself.
- Literal uses (a performing-arts venue, a military theater of operations) are not this pattern.

## 510. Redundant Repeated Labels
- Never render the same literal text `3` or more times in structurally distinct spots inside a single card or panel. It is usually a status or label wired into every template slot.
- Say it once, in the slot where it matters most.
- Navigation, menus, tables and select lists legitimately repeat text and are exempt.

## 511. Concrete Over Generic Copy
- Always name the specific verb and noun of what the product does in place of a category claim.
- Replace unnamed social proof with named customers, numbers or quotes, or drop it.
- Read every headline aloud: if it fits any product in the category, rewrite it.

# Part 57 — Typography Tells

## 512. Overused Typefaces
- Avoid the old monoculture faces as the primary face: `Inter`, `Roboto`, `Open Sans`, `Lato`, `Montserrat`, `Arial`, `Helvetica`.
- Avoid the newer generated-UI wave: `Fraunces`, `Instrument Sans`, `Instrument Serif`, `Geist`, `Geist Sans`, `Geist Mono`, `Mona Sans`, `Plus Jakarta Sans`, `Space Grotesk`, `Recoleta`. Each wave of generated interfaces converges on the same handful.
- A face counts as the page's choice once it sets at least `5%` of the rendered characters; a stray fallback label below that share does not.
- A brand's own house face on its own properties (for example a search company's sans on its own domains) is not a lapse.
- Choose a face that gives the interface personality rather than one chosen by default.

## 513. Flat Type Hierarchy
- Separate dominant heading and body sizes by at least `1.25×` at one or more steps. Below that at every step the hierarchy reads flat.
- The rule applies once at least `3` text roles (headings, paragraphs, list items, table cells, quotes, captions) are present.
- A weight step of `200` or more between roles (for example `400` body under `600`+ headings, held by about `80%` of the role) can carry hierarchy in place of size.

## 514. Italic Serif Hero Headline
- Never set the primary hero headline (an `h1`, or an `h2` at `48px` or more) in an oversized italic serif such as `Fraunces`, `Recoleta`, `Playfair` or `Newsreader` italic. It has become the universal startup landing hero.
- Set it roman, or move to a non-serif display face.
- Editorial and magazine registers may want this deliberately; judge by context.

## 515. Oversized Full-Sentence Headline
- Never set an `h1` of `40` or more characters at `72px` or larger when it fills `28%` or more of the viewport height or `25%` or more of its area.
- A punchy one- or two-word headline at display size is fine; a long sentence blown up crowds everything else out of the first viewport.
- Set long headlines smaller, or tighten the copy.

## 516. Crushed Letter Spacing
- Never tighten reading copy past `-0.07em` of letter-spacing; characters lose their own shapes.
- Display type (`40px` and above) may go tighter, but never past `-0.09em`.
- Tighten display type optically, not destructively.

## 517. Wide Tracking on Body Text
- Never track body text wider than `0.05em`. Wide spacing breaks natural character groupings and slows reading.
- Reserve wide tracking for short uppercase labels of `40` characters or fewer on a single line.

## 518. All-Caps Body Text
- Never set a run of `80` or more characters of an element's own text in uppercase. All-caps strips the ascender and descender shapes readers recognise words by.
- Buttons, navigation items and short labels in caps are a convention and are fine.

## 519. Hero Eyebrow Chip
- Never place a tiny uppercase, letter-spaced label (`14px` or smaller, tracked at `1.6px` or at least `0.08em`) directly above an oversized hero headline (`48px` or more).
- The same shape rendered as a pill chip above the hero is equally banned.
- Drop the eyebrow, fold the kicker into the headline, or run it as a real breadcrumb.

## 520. Kicker Above Any Heading
- Never put a tiny tracked uppercase or small-caps label as its own block directly above a heading, repeated or not. The heading should carry its own weight.
- A label counts as a kicker when it sits over an `h1`–`h4` of at least `20px`, is no larger than `14px` (or `45%` of the heading size, never past `16px`) and is tracked at `0.06em` or more.
- Dated meta lines (a byline with a year, a `·` or `/` separated breadcrumb) and document numbering (`Section 3`, `Chapter Two`, `Article 12`) are not kickers.
- Delete the label; if the words matter, work them into the heading or the body.

## 521. Numbered Section Labels
- Avoid tiny numeric index labels (`01`, `02`, `03`…) riding beside section headings, section after section. Two or more is the pattern.
- A label counts when it is `13px` or smaller (or up to `45%` of its heading, never over `16px`) and the heading is at least `1.3×` its size.
- Let hierarchy, content and rhythm carry the sequence instead of the page numbering its own chapters.

## 522. Tight Leading
- Never set multi-line reading text below `1.3×` line-height.
- Use `1.5`–`1.7` for body copy so lines breathe.
- Display type at `24px` or more sets its own leading and may go below `1.3`.
- Lead text from `20px` to `23px` running no more than `3` lines may go down to `1.15`, never below.
- Short labels in capitals may go to solid (`1.0`) but never under it, or their lines collide.

## 523. Justified Text in Narrow Columns
- Never justify text without hyphenation in a column of `45` characters per line or fewer; word spaces stretch into rivers.
- Use left alignment, widen the measure, or enable `hyphens: auto` if justification is a must.
- Scripts that justify on a character grid or by elongating glyphs (CJK, Thai, Arabic) are not affected.

## 524. Display Versus Reading Sizes
- Treat `40px` and above as display type, where tighter tracking and leading are craft; below it, type is reading copy and keeps the reading floors.
- Never apply display-type liberties (negative tracking, sub-`1.3` leading) to paragraph-sized text.

## 525. Card Titles
- Set a card title at `16px` or more and weight `600` or more, and keep it to `80` characters or fewer; longer text is body copy, not a title.

## 526. Handwriting Faces
- Reserve script and handwriting faces (`Caveat`, `Pacifico`, `Great Vibes`, `Allura`, `Sacramento`, `Satisfy`, `Parisienne` and similar) for short signatures, never for reading copy or UI labels.

# Part 58 — Colour & Gradient Tells

## 527. Purple and Violet Palette
- Never use purple or violet gradients as the hero or accent treatment. The stock violets `#7c3aed`, `#8b5cf6`, `#a855f7`, `#9333ea`, `#7e22ce`, `#6d28d9`, `#6366f1`, `#764ba2`, `#667eea` are the most recognisable generated-UI tells.
- Never set headings (`h1`–`h3`), or large text of `20px`+ with saturation of `0.3` or more, in a violet hue between `260°` and `310°`.
- Never pair a purple "from" stop with a purple "to" stop in a gradient.

## 528. Blues Are Not the Violet Tell
- Blues between `197°` and `260°` are ordinary accents and are not the purple tell; sky blues are blues, not cyans.
- Do not drift a brand blue toward indigo `#6366f1` or a violet blend; that is where it becomes the tell.

## 529. Cyan-on-Dark Neon
- Avoid flat neon cyan ink (hue `170°`–`197°`, saturation `0.4` or more) on a dark ground, especially once a second tell hue such as violet joins it.
- A gradient in one of the tell hues is the tell on its own; flat neon ink is charged once paired with another tell colour.
- Muted, greyed teals are fine accents.

## 530. When a Gradient Counts as Palette
- A gradient needs a surface: one at least `8px` on a side and `256px²` in area. Hairline rails and underline dots are not palette.
- Stops painted under `0.15` alpha are a tint, not a colour decision.
- A gradient whose every stop is one colour (within `12` per channel), or a single-colour fade that keeps `0.75`+ alpha throughout, is a flat fill.
- Past `24px` of blur a gradient becomes atmosphere and no longer reads as a hue choice.

## 531. Gradient Text
- Never clip a multi-colour gradient to text (headings, metrics, hero words). It is decorative, not meaningful, and a common generated tell.
- Use solid colours for text.
- A "gradient" whose stops are all the same colour is a solid fill and is fine.

## 532. Cream and Beige Default Surface
- Avoid a warm cream or beige page background as the reflexive "tasteful" surface: every channel at `209` or more, red ≥ green ≥ blue, and red exceeding blue by `6`–`48`.
- Bands covering the body count just as much as the body background itself.
- Choose a background from a deliberate palette, not the safe warm off-white.

## 533. Glowing Shadow Accents
- Never use a zero-offset chromatic halo (box-shadow or text-shadow) as a glow on any background.
- Never put a coloured, blurred shadow on a dark background; it is the default "cool" generated look.
- A glow is visible once its blur scaled by its ink alpha reaches `3px`, and it lifts its surface by `20` or more.
- Small indicator lights (a status dot, a caret) whose halo exceeds `2×` their own area are indicators, not treatment.
- Use neutral elevation shadows and subtle, purposeful lighting instead.

## 534. Shade Versus Coloured Light
- A dark shadow (HSL lightness under `0.25`) within `50°` of its surface's hue is shade and is fine.
- A shadow in a hue far from its surface, or a bright one, reads as coloured light and is a glow.

## 535. Radial-Gradient Halo
- Never wash a dark page with a chromatic radial gradient saturated at the centre and fading to transparent. It is the glow tell drawn with a gradient.
- Ground the surface with a solid or subtly shifted background.

## 536. Radial Spotlight Glow
- Never drop an accent-coloured radial "spotlight" behind a hero or section copy when it carries `0.14` or more effective alpha and reaches `1.30:1` contrast or more against its surface.
- Faint washes under those values read as ground and are fine.
- Let the surface stand on its own, or light the composition with a deliberate material accent rather than floating coloured haze.

## 537. Repeating-Gradient Stripes
- Avoid repeating-gradient stripes as surface decoration; they are a recurring generated-UI signature.
- Reach for a deliberate texture or leave the surface plain.

## 538. Decorative Grid-Line Background
- Avoid backgrounds drawn with two or more hairline linear-gradient layers tiled on a fixed pixel cell to fake a grid or line field.
- Reserve grid overlays for real canvas, map, blueprint or measurement surfaces.
- A single hairline (a divider or rail) is not a grid.

## 539. Faint Root Washes
- A page-level gradient whose every stop is under `0.1` alpha leaves the base fill as the colour the visitor reads; judge the page by that fill.
- Never rely on a faint wash to change the mood of a surface; commit to a real background colour.

# Part 59 — Layout & Spacing Tells

## 540. Monotonous Spacing
- Never let one spacing value dominate: if more than `60%` of spacing values (rounded to a `4px` grid) are the same and there are `3` or fewer distinct values across `10`+ declarations, the layout has no rhythm.
- Use tight groupings for related items and generous separations between sections.

## 541. Heading Rhythm
- Always give a heading more space above it than below it; it binds to the content it introduces.
- When `2` or more headings on a page sit as close or closer to the block above as to their own content, every section reads as a caption of the previous one.
- Open up the space above each heading.

## 542. Line Length
- Never let text lines run past about `80` characters; the eye loses its place returning to the next line.
- It fails when more than one rendered line runs long (`2`+ lines over the limit).
- Add a `max-width` of `65ch`–`75ch` to text containers.

## 543. Body Text at the Viewport Edge
- Never let body paragraphs sit closer than `16px` to the left or right viewport edge, or `12px` on viewports `480px` wide or narrower.
- Give containers at least `16px` (ideally `24`–`32px`) of horizontal padding, or a `max-width` with auto margins.
- If body text runs past the viewport edge, constrain the widest element rather than adding padding.
- Text in a fixed bar may sit near the edge, but never within `4px` of it.

## 544. Phone Gutters
- On viewports `480px` wide or narrower, keep at least `12px` of gutter on both sides of body text; prefer `16px`.
- Test every page at phone width; a layout that only fits a desktop measure is broken.

## 545. Cramped Padding
- Always inset text inside bordered, outlined or coloured containers by at least `8px`, ideally `12`–`16px`.
- Vertical inset should be at least `max(4px, 0.3 × font size)`; horizontal inset at least `max(8px, 0.5 × font size)`.
- Small chips under `28px` tall still need at least `0.25em` of air around their glyphs (up to `4px`).
- A wrapper whose child text lands flush against its visible border or fill is cramped too.

## 546. Content Overflowing Its Container
- Never let content render wider than its container when the spill is clipped, collides with another box, or reaches the viewport edge. A spill of `16px` or more counts.
- Let text wrap, constrain widths, or give the region a deliberate scroll affordance.

## 547. Clipped Positioned Children
- Avoid wrapping absolutely positioned tooltips, menus and popovers in an `overflow: hidden` or `clip` container that cuts them off.
- Let the overflow be visible, or move the positioned layer out of the clip. This is advisory: most clips are intended.

## 548. Cards Flush Against the Scroller Edge
- Never let cards in a horizontal scroller or tab panel sit flush against one edge at rest while keeping a gutter on the other; rounded corners get cut off.
- Keep a consistent inset on both sides. Usually the panel is sized wider than its clip box.

## 549. Unbalanced First-Viewport Columns
- Never let one column of a multi-column opening section run far past the fold while its sibling fits in one viewport; the short column floats in dead space.
- Balance the columns, cap the tall one, or let long content flow below the opening row.

## 550. Slider Tracks
- A horizontal track that runs past one side of the viewport by `16px` or more than the other is a slider; give it a visible scroll affordance and matching insets.
- A row centred past both edges equally is layout, not a track.

## 551. Text Occlusion
- Never paint text under an opaque element or a second run of text. Decorative boxes, stacked layers or leaked inline padding must sit beside the words, not on them.
- Give overlapping layers room, or move the text out from under the layer above.
- A deliberate gate blur of `4px` or more (a teaser behind sign-in) is not a reading surface and does not count.

# Part 60 — Card & Component Tells

## 552. Side-Tab Accent Border
- Never put a thick coloured border on one side of a rounded card. It is the single most recognisable generated-UI tell.
- A side counts as an accent at `2px` or more when the other sides are `1px` or less, or it is at least twice as thick as any other side.
- The card counts as rounded at `4px` of corner radius or more on the corners away from the stripe.
- On a square box a coloured left or right rule of `3px` or more still reads as the tab.
- Use a subtler accent, or remove it entirely.

## 553. Circles and Badges Are Exempt
- A coloured arc on a circle (width and height within `1.1×`, corners at least half the shorter side) is a spinner or ring, not a side-tab.
- Small badge spans and callout rules on blockquotes and navigation are established conventions, not card tells.

## 554. Top and Bottom Accent Bands
- Never put a `3`–`12px` coloured band along the top or bottom of a card rounded away from it.
- A band across a square section or header is a rule, not a card tell.

## 555. Border Accent on Rounded Element
- Never pair a `2px`+ coloured accent border on one edge with a border radius on the same card; the border clashes with the corners.
- Remove the border or the radius.

## 556. Stripe Children and Inset-Shadow Stripes
- Never fake a side-tab with an empty narrow coloured child at the card edge, a pseudo-element bar, or an inset box-shadow (`inset 3px 0 0 …`).
- These are the same tell drawn another way.

## 557. Status Stripes on Rows
- Avoid coloured `2`–`6px` stripes down one side of a table row or cell as status markers when the colour has chroma of `0.07` or more.
- Hover, selection and current-row indicators are fine; a stripe marking state is the tell.

## 558. Nested Cards
- Never place cards inside cards. It creates visual noise and excessive depth.
- Flatten the hierarchy with spacing, typography and dividers.
- An inner box only counts as a card when its fill differs from its surface by `8` or more on some channel, or it has a shadow or border.

## 559. Card Edges Must Read
- A card only reads as a separate surface when its fill differs from its ground by at least `8` on some channel, or it carries a border or shadow.
- Never stack near-identical fills to fake depth; use spacing and dividers.

## 560. Icon Tile Stacked Above Heading
- Never place a small rounded-square icon container (`32`–`128px` square, aspect `0.7`–`1.4`, with a visible tint of `0.05`+ alpha or a border) directly above a heading.
- This exact shape is the universal generated feature-card template.
- Put the icon beside the heading, or let it sit in flow without its own container. A circular container is not this shape.

## 561. Hairline Border with Wide Shadow
- Avoid giving every card in a row of `3` or more both a hairline border and a wide, diffuse shadow (`32px`+ blur).
- One floating panel earns both. Across a row, commit to one: a defined edge or a soft elevation.

## 562. Hard Offset Shadow
- Review any visible, unblurred shadow displaced by `4px` or more. It can belong to an intentional neobrutalist direction.
- This is a review prompt, not a ban: keep it if it fits the intended design.

# Part 61 — Decorative Clutter

## 563. Bounce and Elastic Easing
- Avoid easing curves named `bounce`, `elastic`, `wobble`, `jiggle` or `spring`, and cubic-bezier curves whose y control points leave the `-0.1`–`1.1` range.
- Real objects decelerate smoothly; use exponential easing (ease-out-quart, quint or expo).

## 564. Pulsing Status Dot
- Never animate a small round dot (`2`–`16px`, aspect within `1.5`) with a looping pulse to simulate liveness.
- Reserve pulse for indicators tied to genuinely live, changing data; a static labelled indicator is calmer and honest.

## 565. Decorative Blinking Cursor
- Avoid a blinking text cursor animated into a hero or landing section within the first `1200px`; it fakes typing where no input exists.
- Real editable fields draw their own caret.

## 566. Auto-Scrolling Marquee
- Never use continuously auto-scrolling content (a `<marquee>` element or an infinite horizontal loop animation).
- It demands attention it has not earned and hides half its content at any moment. Let readers move at their own pace.

## 567. Organic Clip-Path Contours
- Never fake a torn edge, blob or silhouette with a `clip-path: polygon()` of `10` or more arbitrary vertices, or a curved `clip-path: path()`.
- Derive an alpha matte from the real image, or ship a cut-out raster.
- Keep clip-path for geometry: cut corners, diagonals, hexagons, zigzags, vertices on the `0/50/100` grid.

## 568. Buried Raster
- Never bury a background image under a near-opaque gradient wash (`0.9` alpha or more) or put a raster at near-zero opacity. The texture never reaches the screen.
- Let the material show (a tint under `0.9` alpha, a blend mode, a visible opacity) or remove the file.

## 569. Ghost Wordmarks and Ghost Words
- Treat giant display type (`120px`+, or `3×` the largest `h1` and at least `80px`) painted at `0.25` opacity or less as a shape, not text.
- Words set aside from reading (aria-hidden, no pointer events, behind the page) at contrast of `1.5:1` or less are background ornament; never put real content there.

## 570. Background Textures
- Keep textures behind text at `0.3` opacity or less, drawn in cells of `64px` or smaller, or tiles of `256px` or smaller, so the surface underneath still reads.
- Dot patterns may lay no more than `0.15` of ink over their cell.
- Paint fainter than `0.1` is a wash, not a surface; never rely on it for contrast.

# Part 62 — Iconography & Illustration

## 571. Shape-Assembled Illustrations
- Never build a hero-sized visual (`200px` or more on each side) from a pile of primitives: `8` or more rects, circles, ellipses or polygons making up at least `25%` of the drawn shapes, in `3`+ fills.
- It reads as placeholder clip art. Use real artwork, a photograph or a deliberately drawn graphic.
- Icons, logos and data graphics (an equal-width bar series, a chart) are fine at their scale.

## 572. Broken or Placeholder Images
- Never ship an image with an empty, missing or placeholder source; it renders as a broken-image box.
- Use real images, generated assets, or remove the tag.

## 573. Raster Icons and Blur-Up Placeholders
- A raster `48px` or smaller on either axis is an icon; anything larger is a picture and must actually show.
- A faint raster under a blur of `4px` or more is a loading placeholder, not finished imagery.

## 574. Emoji and Icon-Font Glyphs
- Treat emoji-only runs and icon-font glyphs as icons, not text; never rely on them to carry reading content.
- Text with no letters or digits (a lone circle, a pair of braces) is ornament.

## 575. Mockup Furniture
- Interface mockups drawn on the page (a window at least `120×80px` with `3`+ text runs, a device frame, three title-bar dots) are illustration.
- Sentence-length copy inside a mockup is still copy and must stay legible.
- Hide decorative mockups from assistive technology deliberately, rather than leaving them half-legible.

# Part 63 — Line Breaks & Text Rendering

## 576. Stragglers
- Avoid a paragraph whose last line holds a single word filling `30%` or less of the widest line, in columns of `30`+ characters.
- Set `text-wrap: pretty` on body copy, edit the last sentence, or bind the last two words with a no-break space. Keep it if the break is intended.

## 577. Unbalanced Headings
- Avoid a wrapped heading of up to `3` lines whose last line is under `35%` of the line above it, often one word alone.
- Set `text-wrap: balance` on headings, or rewrite to fit. Balance is only honoured on blocks of `6` lines or fewer.
- Blocks with fewer than `3` words, or heading columns under `20` characters wide, cannot rebalance and are exempt.

## 578. Skipped Heading Levels
- Never skip heading levels (an `h1` then an `h3` with no `h2`). Screen readers navigate by the outline.

## 579. Content Invisible at Rest
- Never ship content that stays at opacity `0` or visibility hidden after reveal scripts have run. Failing at `200`+ characters of text with `150`+ hidden and more than `30%` hidden.
- Make content visible by default and let scripts enhance its entrance instead of gating its existence.

## 580. Letter-by-Letter Reveals
- Split-text reveals of `3` or more words must land fully visible; never leave a run of words parked at its first frame.
- Make the final state the default, and treat the animation as an enhancement.

## 581. Uncaught Script Errors
- Never ship a page that throws an uncaught exception or fails to parse on load. Broken scripts silently kill reveals and interactions and can leave most of the page invisible.
- Fix the error before judging anything else.

## 582. Text Partly Off-Screen
- A text run counts as read only when at least `25%` of its width and `50%` of a single line's glyph band shows inside its clipping ancestors.
- Never park a visible line cut through its x-height at the edge of an overflow box.

# Part 64 — Contrast & Legibility

## 583. WCAG Contrast Floors
- Always meet `4.5:1` contrast for body text and `3:1` for large text (`24px`, or `18.67px` bold at `700`+).
- Ratios just under the bar (`4.2`–`4.5:1` normal, `2.8`–`3:1` large) are advisory; anything lower is a failure.
- Text under `1.25:1` is as good as gone; fix colour before anything else about it.
- Fonts named as heavy cuts (`Bold`, `Black`, `Semibold`) count as bold for the large-text threshold.

## 584. Gray on Colour
- Never set gray text on a coloured background; it looks washed out.
- A background reads as colour when its channels spread `40` or more (more on near-black grounds), or a pale tint at OKLCH lightness `0.9`+ has chroma `0.09`+.
- Use a darker shade of the background hue, or white / near-white.

## 585. Hover and Placeholder Contrast
- Always keep hover states at the same `4.5:1` / `3:1` contrast as resting states.
- Always score placeholder text, translucent placeholders included, against the field it sits on.

## 586. Gradient Backgrounds Under Text
- Always check text against the part of the gradient it actually sits on, not only the average.
- When the stops under the text cannot be known, check against the worst stop.

## 587. Frosted Glass Over Text
- A blurred translucent layer hides the text beneath it once its alpha reaches `0.75` and its blur is at least `8px` and a third of the text's font size.
- Never let a frosted header or bar slide over readable text at rest.

## 588. Light Text Needs a Painted Ground
- Text with relative luminance of `0.4` or more cannot be read on a white canvas; always paint the ground it relies on, never assume it.

## 589. Tiny Body Text
- Never set body text with more than `20` characters below `12px`. Use at least `14px`; `16px` is ideal.

## 590. Undersized Functional Text
- Never set links, buttons, nav items, labels, table cells, meta rows or timecodes below `11px`, even in a footer.
- Only non-interactive legal smallprint may drop to `10px`.
- Adding a tiny step to the type ramp does not make tiny text legible.
- Superscripts, subscripts, visually hidden text and code or terminal contexts are exempt; decorative letter-spaced micro-labels are not.

## 591. Decorative Text Exemptions
- Avatar initials (one or two letters, centred in a `12`–`72px` near-square box), version or build stamps, handwritten signatures and mockup labels have no reading job and are advisory, not failures.
- Never use these exemptions to hide real copy at low contrast.

# Part 65 — Design-System Consistency

## 592. Fonts Outside the System
- Never use a font family that is not declared in the project's documented typography. Use the system, or add the face to it deliberately.

## 593. Colours Outside the System
- Avoid literal colours outside the documented palette and its tonal ramps. Allow `6` per channel of drift; anything further is a new colour.
- Shadow colours may drift by `0.02` alpha.
- Make new colours an intentional addition to the system, not drift.

## 594. Radii Outside the System
- Avoid border-radius values off the documented rounded scale; allow `0.5px` tolerance.

## 595. Font Sizes Outside the Ramp
- Avoid literal font sizes off the documented type ramp; allow `0.5px` tolerance.

## 596. Brand and Category Colour
- A hue that paints a full-width band (`90%`+ of viewport width, or `20%`+ of its area) or a header bar (`50%`+ width) is the brand colour, matched within `12°`.
- A role carrying `6` or more distinct hues (separated by `5°`+) is category coding, not palette drift.

## 597. Fix System Drift Immediately
- Correct font, colour, radius and size drift at the moment it is introduced; drift compounds.
- Fix broken images, overflow, edge-touching text, low contrast, gray-on-colour, tiny text, gradient text and glow shadows at once as well; they are mechanical and unambiguous.

## 598. Tokens Over Literals
- Always reference a documented token for colour, radius, size and shadow rather than a literal value, so the system can change in one place.

# Part 66 — Rendered-Page Quality Checks

## 599. Judge What Actually Renders
- Judge contrast, glow and palette by the painted result, not the declaration: a layer at opacity `0.02` or less paints nothing.
- Translucent fills between `0.1` and `0.9` alpha must be composited over what is behind them before scoring.
- Covers count as opaque only at `0.95` alpha or more.

## 600. Hidden Subtrees
- Content declared `inert` or `aria-hidden="true"` is out of the page on purpose; never put readable content there.
- Parked carousel slides, closed menus and marquee duplicates are expected to be hidden.

## 601. Reveal Animations
- Elements dimmed to `0.1` opacity or less at rest are hidden; peers held at `0.5` or less by a shared class are a stalled reveal.
- Animations must finish within `60` seconds; looping content must not vanish below `0.1` opacity.

## 602. Form Labels
- Always place a text label within `24px` of its field, or within `96px` when found up to `4` levels away. Labels should be `40` characters or fewer.

## 603. Separator Lists
- Lists of `3` or more short terms (up to `6` words or `60` characters each) joined by separators are metadata, not prose.

## 604. Covers Over Content
- A layer hides what is under it only at `0.95` opacity or alpha; anything less is translucent and the text beneath must still meet contrast.
- Pictures and video laid over text at `0.95` opacity or more cover it completely; never park content there.

## 605. Fixed Bars
- Fixed bars that cover less than `50%` of the viewport height are overlays; never let them cover body content at rest.

# Part 67 — Severity Guide

## 606. Errors
- Treat uncaught script errors and content invisible at rest as errors: they break the page and block every other judgment.

## 607. Warnings
- Treat side-tabs, overused fonts, flat hierarchy, gradient text, the AI colour palette, cream surfaces, nested cards, monotonous spacing, pulsing dots, glows, halos, spotlights, marquees, icon tiles, italic serif heroes, eyebrows, kickers, buzzwords, aphoristic cadence and oversized headlines as warnings that should be fixed.
- Treat broken images, low contrast, gray-on-colour, line length, cramped padding, edge-touching text, tight leading, skipped headings, justified narrow text, tiny and undersized text, all-caps body, wide tracking, overflow and occlusion as quality warnings.

## 608. Advisories
- Treat bounce easing, blinking cursors, shape-assembled illustrations, hard offset shadows, numbered section labels, em-dash overuse, clipped positioned children, stragglers, unbalanced headings, off-system colours, radii and sizes, hairline-plus-shadow rows, repeating stripes, grid-line backgrounds and theater framing as advisories: review against intent rather than remove automatically.
- Contrast ratios just under the bar, and text in avatars, stamps, signatures and mockups, report as advisory.

## 609. Intentional Exceptions
- Waive a finding only when the choice is deliberate and fits the design direction (an editorial italic serif, a neobrutalist offset shadow, a brand's house font).
- Never treat a waiver as a reason to skip the reason behind the rule.
