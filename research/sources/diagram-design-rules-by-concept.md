# Design Rules by Concept

Distilled from Diagram Design — an editorial diagram and chart system: philosophy, tokens, primitives, layout budgets, 40+ diagram and chart types, motion, and the quality checks every diagram must pass.

# Part 1 — Editorial Diagram Philosophy

## 1. Deletion as the Quality Move
- The highest-quality move is usually deletion.
- A schematic is not done when everything is added; it is done when nothing can be removed.
- Every node represents a distinct idea; two nodes that always travel together are one node.
- Every connection carries information; if a relationship is obvious from layout, remove the line.

## 2. Target Density
- Aim for density `4/10`: technically complete, but never so dense it needs a guide.
- Above `9` nodes, the subject is probably two diagrams.
- Splitting into an overview plus detail beats shrinking content to fit.

## 3. Focal Accent as Editorial Voice
- The accent is editorial, not a flag or a signaling system.
- Apply the accent to `1–2` focal elements per diagram, never more.
- Accenting `5` nodes erases the signal; if tempted to accent `4` things, the focal point has not been decided yet.
- Everything that is not focal is drawn in ink, muted, or soft.
- More nodes never buy more focal elements; the accent ceiling stays at `2` at every detail level.

## 4. When a Diagram Earns Its Place
- Draw only when a reader will learn more from the visual than from prose, a table, or a bulleted list.
- Ask first: would the reader learn more from this than from a well-written paragraph? If no, do not draw.
- Lists of things belong in a table or bullets.
- Attribute-only before/after comparisons belong in a table; topology changes belong in an architecture delta.
- One-shape "diagrams" should just be written as a sentence.
- If a `3`-column table communicates the same thing, pick the table.

## 5. Remove Test
- Ask whether any node can be removed while the reader still understands.
- Ask whether any two nodes can be merged because they always travel together.
- Ask whether any arrow can be removed because layout already makes the relationship obvious.
- Ask whether any label can be removed because color or shape already signals it.

## 6. Confirm the Plan Before Drawing
- State the chosen visual type, any semantic pattern, the size preset, and anything the complexity budget will force out before rendering.
- Let the requester redirect when reachable; otherwise proceed and note assumptions beside the deliverable.
- Skip the pause only when type, size, and content are already pinned exactly.

## 7. Static by Default
- A diagram is static unless motion is requested or materially clarifies ordered change.
- Motion never changes the static meaning or raises the complexity budget.
- Motion modes are `none` (default), `reveal`, `step`, and `loop`.
- Animated output must convey its complete meaning without JavaScript, and under reduced-motion preference shows the complete static frame with playback hidden or disabled.

# Part 2 — Choosing a Diagram Type

## 8. Semantic Pattern First, Visual Type Second
- When behavior, state, enforcement, or risk carries the meaning, choose one primary semantic pattern first, then the nearest visual type for layout.
- If no pattern matches, choose the visual type directly.
- The pattern owns semantic primitives and its tighter budget; the type owns layout grammar.
- A semantic pattern may add behavior-specific primitives, never a second layout grammar.

## 9. Behavioral Pattern Routing
- Fan-in, queue depth, finite capacity, or a bottleneck: fan-in queue pattern drawn as a data flow.
- Repeated Question / Input / Governance / Output slots across stages: stage framework with semantic slots drawn as a process.
- Conversation or loose input becoming a structured durable artifact: unstructured-to-structured pattern drawn as a data flow.
- Two rule traces needing pass / fail / skipped / not-reached states and the first divergence: paired policy-evaluation traces drawn as a flowchart.
- Trust boundaries plus permitted and forbidden ingress or deploy paths: secure paved road drawn as an architecture diagram.
- Controls grouped by where they are enforced: governance / control catalog drawn as a layer stack.
- Defenses compensating for prior gaps with residual risk propagating: compensating security layers drawn as a layer stack.
- Hierarchical, ID-addressable decomposition needing per-block I/O, constraints, and a code link: traceable block decomposition drawn as a tree.
- One subject progressing through phases, waits, retries, cancellation, and terminal outcomes: lifecycle phase map drawn as a state machine.

## 10. Structural and System Types
- Components and connections in one snapshot, including nested admin vs traffic scopes: architecture.
- Structural change between synchronized Before / After topologies with a changes ledger: architecture delta.
- Legacy landscape by phase or department showing the before state: IT current-state.
- Where software runs (zones, hosts, artifacts, replicas, ports): deployment.
- What depends on what, with fan-in and cycles a tree cannot express: dependency graph.
- End-to-end data stack on a container cluster: high-level.
- Multi-tier data storage with quality levels and access policies: medallion.
- Integration topology of a data platform (sources, core, consumers): data platform integration.
- Per-role or per-component access permissions: security matrix.

## 11. Behavior and Process Types
- Decision logic with branches: flowchart.
- Time-ordered messages between actors: sequence.
- States, transitions, and guards: state machine.
- Cross-functional process with handoffs: swimlane.
- Multi-actor sequential process with data handoffs: process.
- Role-scoped data flow showing who does what at each step: data flow.
- Reinforcing cycle where the last step feeds the first and a hub accumulates state: loop / flywheel.
- What a person does across stages and how it feels: user journey.
- Customer actions vs what the service hides, with a line of visibility: service blueprint.
- Work in progress by state with WIP limits and blocked items: kanban.
- Narrative backbone sliced into releases with a cut line: story map.

## 12. Hierarchy and Structure Types
- Hierarchy through containment or scope: nested.
- Parent-to-children relationships: tree.
- Human / agent / team ownership, reporting, routing, escalation: org chart.
- Stacked abstraction levels: layer stack.
- Ranked hierarchy or conversion drop-off: pyramid / funnel.
- Overlap between sets: Venn.
- Causes of one observed effect grouped by category: fishbone.
- Entities, fields, and relationships: ER / data model; physical tables with SQL types, constraints, indexes, and column-level foreign keys: database schema.
- Classes with operations, inheritance, composition: UML class.
- Parts of one object pulled apart along one axis (teardown, unboxing, assembly order): exploded axonometric.
- One floor or site seen from above at an angle: axonometric plan.
- Value chain against evolution: Wardley map.

## 13. Quantitative Chart Types
- Quantitative comparison across categories: bar (including dumbbell).
- Start total bridged to end total by signed contributions: waterfall.
- Part-of-whole where relative size is the story: treemap (and marimekko).
- Cross-tabulated data with fill encoding value: heatmap.
- Continuous trends over time: line; change between exactly two states: slopegraph; one distribution per series: ridgeline; rank movement across snapshots: bump; streamgraph also lives here.
- Tasks and phases on a timeline: Gantt; events positioned in time: timeline.
- Correlation of two variables: scatter; three variables: bubble; one variable as a dot per item: beeswarm; five-number summary per group: box plot.
- Two-axis positioning or prioritization: quadrant.
- Multiple entities scored across `3–5` criteria: radar / spider.
- One series across cyclic categories (angle = category, radius = magnitude): polar.
- A quantity splitting and merging across stages with band width as amount: Sankey.

## 14. Tie-Breaking Rules
- If two types seem useful, pick the dominant axis.
- If the content is past the complexity budget, split into overview plus detail rather than choosing a denser type.

# Part 3 — Palette & Tokens

## 15. Semantic Roles Over Hex
- Refer to every color by semantic role (`paper`, `paper-2`, `ink`, `ink-strong`, `muted`, `soft`, `rule`, `rule-solid`, `accent`, `accent-tint`, `link`), never by inline hex.
- `paper`: page background and default node fill; `paper-2`: diagram container background and secondary fill.
- `ink`: primary text and primary stroke; `ink-strong`: high-contrast text on warm accent fills.
- `muted`: secondary text and default arrow stroke; `soft`: sublabels and boundary labels.
- `rule`: hairline borders; `rule-solid`: stronger borders and baselines.
- `accent`: focal elements only (`1–2` max); `accent-tint`: fill for accent-bordered boxes.
- `link`: HTTP / API calls and external arrows.

## 16. Light Skin Values
- `paper` `#f5f5f5` (white-smoke); `paper-2` `#ececec`.
- `ink` `#2d3142` (jet-black); `ink-strong` `#111111`.
- `muted` `#4f5d75` (blue-slate); `soft` `#5a6580`.
- `rule` `rgba(45,49,66,0.12)`; `rule-solid` `#bfc0c0` (silver), or `rgba(79,93,117,0.25)` in the full editorial layout.
- `accent` `#bf4520` (burnt-tangerine); `accent-tint` `rgba(191,69,32,0.08)`.
- `link` `#2e5aa8`.

## 17. Dark Skin Values
- `paper` `#2d3142`; `paper-2` `#393e53`.
- `ink` `#f5f5f5`; `ink-strong` `#111111`.
- `muted` `#bfc0c0` (silver); `soft` `#949eb2`.
- `rule` `rgba(245,245,245,0.12)`; `rule-solid` `rgba(191,192,192,0.25)`.
- `accent` `#f08a59`; `accent-tint` `rgba(240,138,89,0.10)`.
- `link` `#739fdf`.

## 18. Light-to-Dark Inversion
- Any `rgba(45,49,66, X)` in light becomes `rgba(245,245,245, X)` in dark: same opacity, RGB flipped.
- The accent shifts slightly brighter in hue to read on dark paper.
- Arrow marker fills follow the skin: light `#4f5d75` / `#bf4520` / `#2e5aa8`; dark `#bfc0c0` / `#f08a59` / `#739fdf`.

## 19. Brand Palette Derivation
- The default skin maps to a five-color brand palette: jet-black `#2d3142`, silver `#bfc0c0`, white-smoke `#f5f5f5`, atomic-tangerine, blue-slate `#4f5d75`.
- Raw atomic-tangerine reads only `2.86:1` on paper, too faint for arrows or labels, so the accent is the same hue darkened to `#bf4520` until it clears `4.5:1` as text.
- Derived tokens (`soft` as a darker slate, `rule` as ink at opacity, `link` as a saturated blue-slate variant) cover roles the brand palette does not name and are held to the same contrast contract.

## 20. Contrast Contract
- Regular text, including any `soft`, `link`, or `accent` used as text: minimum `4.5:1` against its actual background.
- Large text (`24px+`, or `18.7px+` at weight `600+`): minimum `3:1`.
- Essential non-text marks (lines, arrows, borders, focus outlines, data points): minimum `3:1` against the adjacent color.
- Decorative rules and translucent tints (`rule`, `rule-solid`, `paper-2`, `accent-tint`, fills at opacity) have no minimum but are never the only carrier of meaning.
- A token used in several roles must pass each one; `accent` is held to `4.5:1` because it also labels.
- Composite translucent colors over paper before measuring; a value passing at full strength can fail at `0.5` opacity.
- Measure text on `accent-tint` or `paper-2` against that surface, not paper.
- Default ratios: light `accent` `4.71:1`, `soft` `5.34:1`, `link` `6.13:1`, `muted` `6.11:1` on `#f5f5f5`; dark `accent` `5.21:1`, `soft` `4.78:1`, `link` `4.76:1` on `#2d3142`.

## 21. Series Palette for Multi-Series Charts
- Use only for chart types that must distinguish overlapping entities (for example radar); the accent stays reserved for the focal series.
- `series-1` sage `#7c8f6f` / dark `#9caf8f`; `series-2` dusty-blue `#5e7a9b` / dark `#82a0c0`; `series-3` mustard `#b8915a` / dark `#d3ad7a`; `series-4` rust-brown `#9c6b50` / dark `#b88670`; `series-5` slate `#6e6479` / dark `#8d8298`.
- Series fills sit at `0.18` opacity in light and `0.22` in dark; strokes use the full color.
- Never backfill series colors into non-chart types; architecture, swimlane, and similar types keep muted-ink variants.

## 22. Skin Customization Constraints
- Every text token (`ink`, `muted`, `soft`, `link`, `accent`) must clear `4.5:1` on paper in both skins.
- Pick exactly one accent color; two accents erase the focal signal.
- No rainbow palettes: from an 8-color brand pick `3` (paper, ink, accent) and turn the rest into muted variants.
- Paper is warm-neutral (cream, bone, or light grey with warmth), never pure white, which reads sterile.
- After re-skinning, verify the accent still reads as focal against the new paper.

## 23. Background Treatment
- Default background is a single clean `paper` fill with no pattern.
- Dotted paper is opt-in for long-form editorial hero diagrams: a `22×22` pattern of `r=0.9` dots at `ink @ 0.10` (dark: `rgba(245,245,245,0.08)`), overlaid at about `0.55–0.6` opacity.
- Never use the dot pattern inside a product page, slide, or card; texture compounds with surrounding chrome and reads as noise.
- Never wrap the diagram in a secondary container background by default.

# Part 4 — Typography

## 24. Three-Family System
- Use exactly three families: serif, sans, mono; never more.
- Instrument Serif for the page title and italic callouts; Geist (sans) for human-readable names; Geist Mono for technical content.
- If brand typography is all sans, keep Instrument Serif for title and callout anyway; the contrast is load-bearing.
- Load weights Instrument Serif `400` regular and italic, Geist `400/500/600`, Geist Mono `400/500/600`.
- Every family stack ends in a generic fallback: `'Geist', system-ui, sans-serif`; `'Instrument Serif', 'Noto Serif', 'Noto Serif KR', serif`; `'Geist Mono', ui-monospace, monospace`.

## 25. Type Roles
- `title`: Instrument Serif, `1.75rem`, weight `400` (page H1, letter-spacing `-0.02em`, line-height `1.1–1.15`).
- `node-name`: Geist, `12px`, weight `600`, for human-readable labels.
- `sublabel`: Geist Mono, `9px`, weight `400`, for port, protocol, URL, field type.
- `eyebrow`: Geist Mono, `7–8px`, weight `500`, tracked `0.18em`, uppercase, for type tags and axis labels.
- `arrow-label`: Geist Mono, `8px`, weight `400`, tracked `0.06em`.
- `callout`: Instrument Serif italic, `14px`, weight `400`, editorial asides only.
- Page eyebrow above the title: Geist Mono `0.66rem`, weight `500`, tracked `0.18em`, uppercase, muted.
- Responsive H1: `clamp(1.5rem, 2.4vw + 0.75rem, 2rem)` minimal, `clamp(1.75rem, 3vw + 1rem, 2.5rem)` full editorial.

## 26. Mono Is for Technical Content Only
- Mono carries ports, commands, URLs, protocols, and field types.
- Names go in Geist sans, never in mono.
- Never use mono as a blanket "dev" font, and never JetBrains Mono anywhere.

## 27. Type Ramp Discipline
- Every font size is a role value for the active size preset or a named exception; anything else is a bug, not a new size.
- Dense annotation (legend keys, axis ticks, chart data labels, source lines, in-box tags): Geist Mono or Geist regular, `7–11`, half steps allowed.
- Chart series or row names (bar category, line series, Gantt row, matrix header): Geist `600` at `10–11`.
- Group or entity heading: Geist `600` at `14`.
- Decorative watermark numerals at or under `0.08` opacity may use any size.
- Exceptions are bound to font and weight: a Geist `600` name cannot borrow the `7` annotation size, and a mono tick cannot borrow the `14` heading size.

## 28. Text Width Budget
- Budget each character, not per writing system: Latin advance `0.60em` sans and `0.62em` mono; every wide or full-width character costs `1em`; nonspacing marks cost nothing.
- Sum the width times font size, add padding, and round the box up to the next multiple of `4`.
- Never estimate mono at a narrower ratio; undersized budgets (about `0.47em`) clip labels.
- Fallback faces have different metrics, so keep the `8px` label padding intact rather than trimming boxes to the primary face.

## 29. Korean and Chinese Labels
- Extend the family on the individual text element (`'Geist', 'Noto Sans KR', …` or `'Geist', 'Noto Sans TC', …`) rather than swapping the skin.
- Titles take the serif equivalent (`'Instrument Serif', 'Noto Serif KR', serif` / `'Noto Serif TC'`) so mixed titles do not split across faces.
- Sublabels stay Latin; ports, protocols, field types, and URLs remain in Geist Mono and are never translated.
- Hangul and Han have a `12px` floor; if a name does not fit at `12px`, cut the name, never shrink the type.
- In arrow-label, eyebrow, and legend slots, CJK text switches register to `12px` sans at weight `500`, no tracking, no uppercase, with a `16px`-tall mask rect; Latin labels in the same diagram keep mono.
- Full-width punctuation costs `1em` and is the part most often dropped from width budgets.
- Japanese and Chinese, and Simplified vs Traditional, each need their own fallback stacks.

## 30. Cyrillic Labels
- Geist and Geist Mono cover Cyrillic, so Cyrillic labels keep the Latin treatment with no register switch.
- Titles extend to `'Instrument Serif', 'Noto Serif', serif`, with Noto Serif placed ahead of any CJK serif.
- Wide Cyrillic sans letters overshoot the `0.60em` budget (for example a `10`-character name at `12px` budgeted `72px` draws near `76px`); leave the overshoot in padding and measure in the browser.
- Preserve printed labels exactly; never transliterate or re-case a string a reader matches to a physical object, and drop the uppercase transform for that label instead.

## 31. Offline Font Mode
- In system-font mode ship no font link; keep every stack as written so installed faces still resolve and others get the platform face.

# Part 5 — Stroke, Line & Arrow Language

## 32. Stroke Weights
- `stroke-thin` `0.8` for tag-box outlines, leaf nodes, and hairline separators.
- `stroke-default` `1` for most strokes and node borders.
- `stroke-strong` `1.2` for emphasis strokes and connectors.

## 33. Arrow Roles
- Default arrows are `muted`, for internal and generic connections.
- Accent arrows mark the primary, highlighted, or headline path.
- Link arrows mark HTTP / API calls and external systems.
- Dashed `5,4` on any color marks optional, passive, return, or async flows.
- Arrow labels may take the color of their arrow (for example link-colored `HTTPS`, accent-colored `TLS`).

## 34. Arrowhead Markers
- Define all three markers always: default, accent, and link.
- Marker geometry: `markerWidth="8"`, `markerHeight="6"`, `refX="7"`, `refY="3"`, triangle points `0 0, 8 3, 0 6`, `orient="auto"`, filled in the matching role color.

## 35. Draw Order
- Draw arrows before boxes so lines sit behind nodes.
- Every node starts with an opaque paper mask rect so arrows never bleed through translucent fills.

## 36. Orthogonal Connectors Only
- Connectors between off-axis nodes are rounded right-angle elbows with quarter-arc bends of `r=8` (`r=6` minimum in tight layouts).
- Use a straight line only when both endpoints share an x or y coordinate; diagonal slants are an automatic fail.
- Two-bend elbows turn at the horizontal midpoint between source and destination.
- When the destination sits noticeably above or below, enter through its top or bottom edge with a single-bend L-path.
- A connector leaves and enters perpendicular to the edge it touches, at a port on the straight part of the edge at least `8px` from a corner.
- Never run a segment along a border (horizontal from a top/bottom edge, vertical from a side edge); it reads as an arrow out of the corner.

## 37. No Overlapping Connectors
- Two connectors never share a stroke path, run on top of each other, or stack on any segment.
- Offset routes that want to overlap by `12px` or more so each stays independently traceable.
- Stacked connectors signal nodes too close together or a diagram over budget; redesign or split.

## 38. Bridge at Crossings
- When two orthogonal arrows must cross once, add an `8px`-radius semicircular hop (`16px` wide) on the less important arrow.
- Bridge the passive, secondary, write-back, dashed, or muted arrow; draw the more important arrow uninterrupted; never bridge both.

## 39. Fanned Attach Points
- No two connectors share one attach point on a box.
- For `N` connectors on an edge of length `L`, attach point `k` sits at `L * k / (N + 1)` from the leading corner.
- Keep adjacent attach points `12px` or more apart (`8px` on very small boxes).
- Parallel connectors in the same direction stay `12px` or more apart along their entire length.
- Route each fanned connector orthogonally from its own point with no merging strokes near the box.

## 40. No Transit Behind Non-Endpoint Boxes
- Reroute any connector that would pass behind a box that is neither its source nor destination.
- Only when the box is geometrically unavoidable (a cross-cutting footer service or layer bar on the only straight path): dash the stroke `4,3`, put the label at the visible end, and land no marker on the intervening box.
- When in doubt, reroute; the exception is not a shortcut around layout work.

# Part 6 — Node & Container Primitives

## 41. Node Box Anatomy
- Layer order: opaque paper mask rect, styled box at `rx=6` with stroke-width `1`, rectangular type tag, name, sublabel.
- Type tag: rectangle at `rx=2` (never a pill), about `22–28` wide by `12` tall, inset `8` from the left and `6` from the top, stroke at `0.8` in the node stroke color at `0.40` opacity, transparent fill.
- Tag text: eyebrow mono `7px`, tracked `0.06–0.08em`, centered, in the stroke color at `0.8` opacity.
- Name: Geist `12px` weight `600` in ink, centered; sublabel: Geist Mono `9px` in muted, about `16px` below the name.
- Standard node box height is about `54–56` with a minimum of `48` (standard ramp).

## 42. Node Type Treatments
- Focal (`1–2` max): fill `accent-tint`, stroke `accent`.
- Backend / API / step: fill `#ffffff`, stroke `ink`.
- Store / state / database: fill `ink @ 0.05`, stroke `muted`.
- External / cloud: fill `ink @ 0.03`, stroke `ink @ 0.30`.
- Input / user: fill `muted @ 0.10`, stroke `soft`.
- Optional / async: fill `ink @ 0.02`, stroke `ink @ 0.20` dashed `4,3`.
- Security / boundary: fill `accent @ 0.05`, stroke `accent @ 0.50` dashed `4,4`.

## 43. Vary Node Treatment
- Identical boxes for every node erase hierarchy; differentiate by type treatment and size.

## 44. Radius Scale
- `radius-sm` `4` for small tags; `radius-md` `6` for node boxes; `radius-lg` `8` for containers and rings.
- Maximum box radius is `6–10px` or none; never large rounded "2xl" corners.

## 45. Region and Boundary Containers
- Region boundaries are transparent rects at `rx=8` with stroke `ink @ 0.18`, width `1`, dashed `6,4`.
- Boundary labels sit inside the top-left in mono `8px`, weight `500`, tracked `0.12em`, uppercase, muted.
- Security groups use stroke `accent @ 0.45` dashed `4,4` with an accent-tinted mono label.

## 46. Zones for Dense Diagrams
- Above `9` nodes, every node belongs to a labeled zone: `2–4` zones, hairline-bordered, `paper-2` fill, mono uppercase zone label at top-left.
- An unzoned `20`-node diagram is a wiring diagram, not a schematic.
- Zones are painted first, so label masks may overlap them safely.

## 47. Watermark Numerals
- A faded mono numeral (for example `01`, `02`) at `40px`, weight `600`, `ink @ 0.06`, right-aligned in the lower part of a node, may mark sequence without competing.

## 48. Diagram Container
- Default container is clean and borderless; the diagram sits directly on page paper.
- Optional framed variant for card-heavy or hero layouts: `paper-2` background, `1px` `rule` border, `8px` radius, `1.5rem` padding.
- Do not reach for the frame by default; extra chrome fights the figure.

## 49. Summary Cards
- Never use three identical generic cards; vary widths, for example `1.1fr 1fr 0.9fr`, in a `2–3` column grid.
- Card background `#ffffff` (a slight lift from paper without shadow), `1px` border in the rule color, `6px` radius, `1.25rem` padding.
- No box-shadow on cards or anything else.
- Card header: a `7px` round dot (ink, muted, accent, link, or soft) beside a Geist `0.875rem` weight `600` heading, separated by a hairline.
- Card list items in muted at `0.8125rem`, line-height `1.55`, with an em-dash bullet at low ink opacity.

## 50. Page Structure
- Header: eyebrow, serif title, optional subtitle in sans muted (`1rem`, line-height `1.55`, max `52ch`).
- Then the diagram container, optional summary cards, and a footer colophon in mono muted/soft (`0.72rem`, tracked `0.06em`) above a hairline top border.
- Content frame maximum width about `1200px`.

# Part 7 — Labels & Annotations

## 51. Arrow Label Rules
- Arrow labels are at most `14` characters, all caps, centered on the segment midpoint.
- Every arrow label sits on an opaque paper mask rect (about `12px` tall, `rx=2`).
- Keep a visible `6–10px` gap between the mask edge and the stroke; the mask never touches or overlaps its connector.
- A typical placement puts the mask `14px` above the line (`8px` text height plus `6px` gap).
- On vertical segments, place the label beside the line with the same `6–10px` horizontal gap.
- On two-bend elbows, labels sit on the vertical segment, centered on the midpoint between the corners.
- Never use vertical writing-mode text; it is unreadable.

## 52. Label Masks and Later Nodes
- A label mask must not overlap any node drawn after it; the node fill would cover part of the text and leave a fragment on its border.
- Place labels on segments running through open canvas, clearing the source node's far edge before the mask starts.
- A mask fully inside a node is a badge chip and is fine.

## 53. Legend Strip
- The legend is a horizontal strip at the bottom, after all nodes, never floating inside the diagram area.
- Separate it with a hairline at `ink @ 0.10`, width `0.8`, inset `30px` from each side.
- Head it with "LEGEND" in eyebrow mono `8px`, tracked `0.14em`, muted.
- Space items horizontally about `160px` apart; swatches about `14×10` at `rx=2`.
- Expand the viewBox height by about `60px` for the strip; nothing else lives there.
- The legend covers every type used and nothing extra.

## 54. Editorial Callouts
- A callout is an italic-serif aside, like marginalia, marking a detail without competing with the diagram grammar.
- Text: Instrument Serif italic `14px`.
- Leader: a dashed Bézier curve (`4,3`), stroke width `1`, ending in an `r=2` landing dot.
- Neutral: text ink, leader `ink @ 0.40`; focal: text accent, leader `accent @ 0.50`; tertiary: text muted, leader `ink @ 0.30`.
- Place callouts in margins (top-right, bottom-left), never inside the active diagram area.
- Maximum `2` callouts per diagram; more becomes commentary rather than signal.
- Never use italic sans or italic mono; the serif-plus-italic pairing is load-bearing.
- Never use a solid leader, which reads as a flow arrow.
- Never cross primary arrows or lifelines with a callout; offset to a clear margin.
- Never use a callout for what the element should label directly.

## 55. Audience-Appropriate Wording
- Engineer: exact component names; sublabels with protocol, port, version, image tag; edge labels like `POST /v2/orders`, `SQL`, `gRPC`; never vague verbs like "connects to".
- Mixed (default): component names with acronyms expanded; technology only where it changes a decision; plain-verb edges (`verifies`, `writes`, `notifies`); no ports, versions, or codenames.
- Executive: capabilities and outcomes; no sublabels; business verbs (`approves`, `pays out`); no vendors, infrastructure, or protocols.
- Keep node names, sublabels, and edge labels at the same audience level.
- Never invent detail to fill a slot; keep an unexplained identifier and ask.
- Keep the source vocabulary for proper nouns; generalizing a product is fine for executives, renaming it to a different product is a factual error.

## 56. Accessible Figure Naming
- Every diagram is an accessible image with a title and a one-sentence description.
- The title is the subject's short name, roughly the page heading, `60` characters or fewer.
- The description states what the diagram shows in content terms, not geometry; a shape-by-shape narration is worse than none.
- Name identifiers per diagram and variant (for example `loop`, `loop-dark`, `loop-full`), never bare shared names.
- Purely decorative glyphs are hidden from assistive technology.

# Part 8 — Layout Budget & Density Limits

## 57. Universal Complexity Budget
- Maximum `9` nodes per diagram.
- Maximum `12` arrows or transitions.
- Maximum `2` accent elements.
- Maximum `2` annotation callouts.
- Motion: maximum `8` steps, `12` marked items, `2` simultaneous items.
- If any limit is exceeded, split into overview plus detail.
- Per-type and semantic-pattern budgets can only tighten these limits.

## 58. Per-Type Budgets: Structure and Systems
- Architecture delta: `8` unique components, `10` relationships, `8` ledger entries.
- Architecture containment: `2` admin bands, `4` traffic scopes, `8` nodes.
- Deployment: `3` zones, `6` nodes, `8` paths, `9` artifacts.
- Dependency graph: `9` nodes, `14` edges, `4` ranks, `1` cycle.
- ER: `8` entities; database schema: `5` tables, `8` shown columns, `6` foreign keys.
- UML class: `7` classes, `8` relationships, `5` members per compartment.
- Nested: `6` nesting levels; tree depth `4`; org chart depth `4` and `12` nodes; layer stack `6` layers; pyramid `6` layers; Venn `3` circles.
- Exploded axonometric: `5` parts, `5` levels, `1` focal part, three detail levels.
- Axonometric plan: `8` tagged rooms or buildings, `40` boxes, `1` focal.
- Wardley map: `9` components, `12` links, `2` movement arrows.

## 59. Per-Type Budgets: Process and Behavior
- Sequence: `5` lifelines; `1` combined fragment by default (`2` only if each is single-region opt/loop); `2` alt regions; fragment nesting `1`.
- Swimlane: `5` lanes.
- Kanban: `5` columns, `12` cards total, `4` per column.
- User journey: `6` stages, `3` rows, `2` pain markers.
- Service blueprint: `6` stages; customer, frontstage, and backstage layers required; evidence and support optional; `1` focal cell.
- Story map: `5` activities, `3` slices, `12` cards.
- Fishbone: `6` bones with `3` sub-causes each.
- Sankey: `3` stages, `8` nodes, `12` flows.

## 60. Per-Type Budgets: Charts
- Quadrant: `12` items.
- Radar: `5` axes, `5` series, `1` focal series.
- Polar: `8` categories, `1` series, `1` focal category.
- Bar chart: `8` bars; waterfall: `8` bars including totals, `1` subtotal.
- Treemap: `8` cells.
- Line chart: `5` series.
- Gantt: `12` tasks.
- Scatter: `30` points; box plot: `8` series, `8` outliers, `1` focal series.

## 61. Detail Levels
- Faithful: up to `24` nodes (zoned), `32` edges, every port, protocol, and version; only exact duplicates merge.
- Balanced (default): up to `12` nodes, `16` edges, technical sublabels on at most `4` nodes; leaf clusters collapse.
- Simplified: up to `7` nodes, `9` edges, no sublabels; capabilities and sequence only, infrastructure disappears.
- Faithful is the only level allowed past the universal budget: zoned above `9` nodes, split above `24`.
- Connector rules never relax at any detail level.
- Above `24` nodes, produce an overview with zones as nodes plus one detail diagram per zone; never ship a `40`-node single canvas.

## 62. Degrade Ladder
- When content exceeds the level, cut in order and stop as soon as it fits; never cut ad hoc.
- First drop decorative cells: sticky notes, free-floating text, title blocks, watermarks, a source legend (notes worth keeping become callouts, max `2`).
- Then merge exact duplicates into one node labeled with a count, for example `Worker ×N`.
- Then collapse leaf clusters into their container.
- Then drop degree-1 sinks that do not change the story (monitoring hooks, log buckets, archive tiers).
- Then drop cross-cutting infrastructure (logging, metrics, secrets, CI): always at simplified; keep at most one at balanced, and only if it is the subject.
- If still over budget, split into overview plus detail; splitting beats shrinking.

## 63. Fidelity Reporting
- Whenever output is smaller than its source, report what was merged, collapsed, dropped, and kept in full; the diagram's reader cannot see what is missing.
- A redraw is bounded by its source: never invent a component to fill a layout, and never silently drop one.
- Redraw rather than convert: discard source coordinates, colors, fonts, and shape quirks; keep components, relationships, grouping, and direction.
- Never reproduce an automatic renderer's layout; it imports mechanical spacing and routing instead of editorial layout.

# Part 9 — Spacing & Grid

## 64. The 4px Grid
- Structural geometry divides by `4`: node origins, widths, heights, gaps, and padding.
- Off-grid by design: type sizes, radii, data-derived positions, text baselines, arrow markers, `.5` offsets that keep `1px` strokes crisp, stroke widths, opacity, and the `22×22` dot pattern.

## 65. Allowed Dimension Values
- Node width / height: `80`, `96`, `112`, `120`, `128`, `140`, `144`, `160`, `180`, `200`, `240`, `320`.
- Gap between nodes: `20`, `24`, `32`, `40`, `48`.
- Padding inside boxes: `8`, `12`, `16`.
- Border radius: `4`, `6`, `8`.

## 66. Minimum Gaps and Box Heights by Size Class
- Standard and print: node box minimum height `48`, minimum node gap `24`.
- Presentation: node box minimum height `64`, minimum node gap `40`.

## 67. Margins and Safe Areas
- Keep a `40px` outer margin on every preset; content never touches the viewBox edge.
- The bottom `60px` is the legend strip and nothing else lives there.
- Social link cards keep the outer `64px` clear on every side because platform crops are unpredictable.
- Slides keep the bottom `80px` clear when the deck has a footer bar.

## 68. Fit-to-Content Canvas
- Round the content bounding box up to the next multiple of `4`, then add `40px` margin on every side plus `60px` at the bottom for the legend.

# Part 10 — Output Specs

## 69. Self-Contained Deliverable
- Produce a single self-contained page: embedded CSS, inline SVG, no external images, no external resources except web fonts.
- Static by default; minimal inline JavaScript only for explicit animation controls.
- Vector and raster exports are derived from the page and contain only the diagram itself; editorial wrappers (header, cards) drop by design.
- Never produce export files unprompted.

## 70. Size Presets
- `doc-inline` (default): viewBox `0 0 960 600`, `8:5`, `1920×1200` at 2x, standard ramp; body-width diagrams.
- `doc-wide`: `0 0 1280 720`, `16:9`, `2560×1440`, standard ramp; full-width docs and wikis.
- `slide-16x9`: `0 0 1280 720`, `16:9`, `2560×1440`, presentation ramp.
- `slide-4x3`: `0 0 1024 768`, `4:3`, `2048×1536`, presentation ramp.
- `social-og`: `0 0 1200 632`, about `1.9:1`, `2400×1264`, presentation ramp.
- `social-square`: `0 0 1080 1080`, `1:1`, `2160×2160`, presentation ramp.
- `print-a4-landscape`: `0 0 1120 792`, about `1.41:1`, `3360×2376` at 3x, print ramp.
- `print-a3-landscape`: `0 0 1584 1120`, about `1.41:1`, `4752×3360` at 3x, print ramp.
- `print-letter-landscape`: `0 0 1056 816`, about `1.29:1`, `3168×2448` at 3x, print ramp.
- `fit`: derived from content, 2x, standard ramp; for vector hand-off.
- Every preset dimension is divisible by `4`.
- Default minimal canvases: light `960×600`; dark `1000×600`; full editorial `1000×720`.

## 71. Destination Mapping
- Blog post, README, docs site: page embed or 2x raster at `doc-inline`.
- Slide decks: 2x raster at `slide-16x9`.
- Further vector editing: vector at `fit`.
- Social / link card: 2x raster at `social-og`.
- Printed handout or PDF deck: 3x raster at `print-a4-landscape`.
- Internal wiki: 2x raster at `doc-wide`.

## 72. Type Ramp per Size Class
- Title: standard `28`, presentation `40`, print `32`.
- Node name: standard `12`, presentation `16`, print `12`.
- Sublabel: standard `9`, presentation `12`, print `9`.
- Arrow label: standard `8`, presentation `12`, print `8`.
- Eyebrow / tag: `8` at every size class.
- Scale the ramp with the preset so projected slides stay readable from the back row; never use the standard ramp on a slide.
- If a slide layout does not fit at the presentation ramp, drop a detail level rather than shrinking type.

## 73. Holding Readable Width on Narrow Screens
- The SVG's minimum width equals the active preset's viewBox width, so the type ramp is never silently scaled down.
- Pinning a smaller minimum shrinks type below every floor (a `12px` name on a `1280` canvas pinned at `900` draws at `8.4px`).
- Wrap the SVG in a local container with `overflow-x: auto` so a phone scrolls the diagram, not the page.
- Centered grid or flex items holding the SVG need `max-width: 100%; min-width: 0` so the wrapper can scroll.
- The scrolling wrapper must sit inside any `overflow: hidden` ancestor, or the diagram is clipped with no scrollbar.
- For print, release both overflow and minimum width (placed after the base rule) so the drawing scales whole: smaller but whole beats sharp but cut off.

## 74. Variants
- Minimal light (default): warm paper, diagram plus title, screenshot-ready.
- Minimal dark: for dark-mode sites, slides, and high-contrast posts.
- Full editorial: header, subtitle, diagram, summary cards, footer; for long-form posts where the diagram is the hero.
- Consultant 2×2 scenario matrix: a quadrant-only special for strategy-style scenarios.
- Sketchy and terminal are optional overlays or replacements described separately.

# Part 11 — Sketchy Style

## 75. Purpose of the Hand-Drawn Register
- A displacement filter wobbles every stroke and edge slightly, turning a minimal variant hand-drawn without changing layout.
- Use for essays, blog posts, or newsletters where the diagram is the hero of a narrative page.
- Use for a "working sketch" register signaling something mid-thought rather than final.

## 76. Filter Parameters
- Fractal-noise turbulence with `baseFrequency` `0.02` (range `0.01–0.04`; lower is lazy and wavy, higher is jittery).
- `numOctaves` `2` (range `1–3`; `2` is plenty).
- Displacement `scale` `1.5` default (range `1–6`: `1` barely there, `2` visible, `4+` cartoon).
- Change the seed integer for a different random pattern; filter region `-2%` / `104%`.

## 77. Filter Shapes, Never Text
- Apply the filter to a group of shapes only; displaced text becomes illegible.
- Keep all text in a sibling group outside the filtered group so labels stay crisp.

## 78. When Not to Go Sketchy
- Not for technical documentation, where precision matters.
- Not for diagrams with dense labels or tight alignments, where the filter reads as noise.
- Avoid on dark variants, where wobble reads as an artifact; test first.

# Part 12 — Terminal Style

## 79. Terminal Register
- A full-page CLI-window skin: titlebar with three dots, a `$` prompt line, monospace throughout.
- Use for dev-tool and CLI-product launches, technical social cards, and screenshots for dark-mode-heavy developer feeds.
- Never for editorial long-form posts, brand-matched output, or audiences not fluent in reading `$`, `#`, and titlebar dots as chrome.

## 80. Terminal Palette
- `terminal-page` `#0a0a0a` (behind the window); `terminal-paper` `#141414` (window body, node fill); `terminal-bar` `#1b1b1b` (titlebar).
- `terminal-border` `#2b2b2b` (window border, hairlines).
- `terminal-ink` `#f5f5f5`; `terminal-muted` `#9a9a9a`; `terminal-soft` `#5c5c5c` (inactive dots, spokes).
- `terminal-accent` `#ff5a36`; `terminal-accent-tint` `rgba(255,90,54,0.12)`.
- This is a fixed second skin; it does not follow brand tokens or the light/dark inversion.
- Swap tokens one-to-one inside the diagram: paper, ink, muted/soft, accent/accent-tint to their terminal equivalents; the inverted-fill focal node pattern still applies.

## 81. Terminal Window Chrome
- Window: `terminal-paper` background, `1px` `terminal-border` border, `12px` radius.
- Titlebar: `terminal-bar` background with a `1px` border-bottom.
- Three `10px` titlebar dots: one `terminal-accent`, two `terminal-soft`; never a red/yellow/green traffic-light triad.

## 82. Terminal Typography
- Everything is monospace; drop serif and sans entirely.
- Page title in bold mono prefixed with `# ` so it reads as a comment line.
- The eyebrow becomes a shell prompt: `$ ` in accent, the command in muted.
- Run every role `1–2px` above the default scale: node name `14px`, sublabel and arrow label `9–10px`, hub label `18px`.

## 83. Terminal Accent and Black Rules
- One accent only; a second emphasis uses terminal ink via weight or size, never a second hue.
- Never pure black `#000000`; true black clips on OLED and in print.
- An optional dot grid stays at `rgba(255,255,255,0.06–0.08)`, a barely visible texture.

# Part 13 — Icons

## 84. Icon Style
- Icons are monochrome on a `24×24` grid and inherit color from their parent so they adapt to any skin.
- Generic icons are stroked at `1.5px` with round caps and joins and no fill, matching the hairline language.
- Brand silhouettes are filled shapes.
- Do not mix stroked and filled styles in one diagram unnecessarily.

## 85. Icon Sizing and Placement
- Default size is `24×24`; position and resize with a translate-plus-scale group rather than redrawing.
- Set color on the parent group so the icon follows the role color (ink, muted, accent) of its node.
- Icons are decorative and hidden from assistive technology; the node name carries the meaning.

## 86. Icon Selection
- Choose by the concept a node represents, from families: compute (laptop, phone, desktop, server, container, VM), people (user, users, admin, robot/agent), network (cloud, internet, CDN, firewall, VPN, load balancer, gateway, DNS), data (database, file, log, queue, cache, bucket, backup, search), orchestration (pod, node, service, deployment, ingress, volume), actions (API, request, response, sync, lock, key, alert), and DevOps (branch, terminal, pipeline, bug, monitoring, test).
- Use a vendor or product mark only when the specific product is the point; otherwise prefer the generic concept icon.
- Brand marks are for documentation and illustration only and keep their trademarks.

# Part 14 — Anti-Patterns

## 87. Generic "AI Slop" Signals
- Dark mode with cyan or purple glow looks technical without any design decisions.
- JetBrains Mono, or any mono, as a blanket "dev" font.
- Identical boxes for every node.
- Three equal-width summary cards as the default; vary widths.
- Shadows on any element; borders are in, shadows are out.
- Large rounded corners; keep radius `6–10px` or none.
- Accent on every "important" node.

## 88. Label and Legend Failures
- A legend floating inside the diagram area, colliding with nodes.
- Arrow labels with no masking rect, letting the line bleed through.
- Labels touching or sitting on their own stroke.
- Vertical writing-mode text on arrows.

## 89. Connector Failures
- Diagonal slants between off-axis nodes.
- Overlapping or stacked paths, and shared attach points.
- Masks clipped by a node painted later.
- Transit behind a non-endpoint box.
- Any breach of the six connector rules is an automatic fail.

## 90. Layout and Process Failures
- Reproducing an automatic renderer's layout instead of an editorial one.
- Shipping default-skinned diagrams into a branded context without deciding on the skin.
- Shrinking type to fit content instead of splitting or dropping a detail level.
- Pure white paper, a second accent hue, or more than three type families.

# Part 15 — Semantic Patterns

## 91. Pattern Before Type
- Semantic patterns describe what a system does; visual types describe how information is arranged.
- Choose a pattern first when behavior, state, enforcement, or risk is load-bearing, then use its nearest visual type as the layout grammar.
- If no pattern matches, choose a visual type directly.
- Use one primary pattern per figure; a second pattern may supply at most one supporting primitive.
- If two patterns both need full treatment, split into an overview figure and a detail figure.
- Labels and outcomes must remain complete in a static frame.

## 92. Pattern Composition
- The pattern may specialize status, boundary, queue, or propagation primitives; the chosen visual type still owns page axis, connector grammar, spacing, and type-specific limits.
- Apply the stricter of the pattern budget and the visual-type budget.
- Semantic cells and statuses are never permission to exceed the nine-node overview target.
- Use stable text for states and outcomes; color, motion, and position reinforce meaning but never carry it alone.
- Animation is a presentation layer, not another pattern; add it only when motion is requested or materially clarifies ordered change.

## 93. Fan-In Queue and Bottleneck
- Use when several producers converge on one reviewer, service, gate, or constrained resource, and the story depends on arrival rate, queue depth, wait, capacity, or backpressure.
- Required: distinct sources, fanned ingress, an ordered queue with visible slots and a count, a capacity/service-rate label, one constrained service point, and admitted plus deferred/rejected outcomes.
- Label units (`8/hour`, `3 slots`), never just "high".
- Budget: `≤5` sources, `≤5` queue slots, one bottleneck, two outcomes, `≤9` primary nodes; aggregate excess sources into a named cohort.
- Avoid equal-width pipelines that hide contention, arrows merged before they can be traced, capacity implied only by box size, decorative pile-ups, animation that reorders items, and red alone meaning overloaded.
- Static fallback: show the representative final queue, numeric count/capacity, bottleneck label, and both outcome paths; a still must reveal why work waits.
- Nearest type: Data flow by default; Process when service stages, rather than sources, dominate.

## 94. Stage Framework With Semantic Slots
- Use when a lifecycle or operating model repeats the same semantic questions across stages (commonly Question, Input, Governance, Output) and cross-stage comparability matters more than timing.
- Required: ordered stage headers, a consistent slot grid, explicit empty/not-applicable slots, stage-to-stage handoff, stable slot labels, and one primary output per stage.
- Preserve slot order in every stage.
- Budget: `3–6` stages, `3–4` slot kinds, `≤20` populated cells, `≤2` lines per cell; split detail when a cell needs prose.
- Avoid stages that invent their own internal layout, slot meaning encoded only by position, fake precision from dozens of cells, confusing stage order with ownership lanes, and shrinking text to keep one canvas.
- Static fallback: render the full stage × slot matrix with handoffs and explicit `—` or `Not applicable` entries; never depend on staged reveal to teach the schema.
- Nearest type: Process; Swimlane only when repeated rows represent owners rather than semantic slots.

## 95. Unstructured Input to Structured Artifact
- Use when dialogue, notes, prompts, or a rambling request are elicited, normalized, and written into a durable brief, ticket, record, or schema.
- Required: source utterance(s), clarifying questions, extracted field/value pairs, a named transformation, the durable artifact boundary, provenance links from statements to fields, and a missing/unknown state.
- Budget: `≤4` exchanges, `≤6` artifact fields, one transformation, `≤3` provenance links; show representative content, not a transcript.
- Avoid an "AI magic" sparkle between two boxes, an artifact drawn as another chat bubble, fields with no source, invented certainty for missing facts, and typing animation as the only readable copy.
- Static fallback: a short source excerpt beside the completed labeled artifact, with at least one provenance mapping and any unknown fields visible.
- Nearest type: Data flow; Process when elicitation has several ordered gates.

## 96. Paired Policy-Evaluation Traces
- Use when two otherwise similar requests reach different outcomes and the reader needs rule-by-rule state and the first divergence.
- Use status words `PASS`, `FAIL`, `SKIPPED`, `NOT REACHED`, always as text plus symbol/shape.
- Run the same ordered rules on both traces and show the differing inputs and final outcomes.
- Mark the first divergence with a labeled marker.
- Distinguish `SKIPPED` (applicable flow intentionally bypassed) from `NOT REACHED` (evaluation stopped earlier).
- Budget: exactly `2` traces, `3–6` rules, one first divergence, `≤12` status cells, one outcome per trace; move rule prose to notes if labels exceed one line.
- Avoid independently ordered flows, green/red dots without words, treating skipped and not-reached as synonyms, highlighting every difference, and continuing a denied trace as if downstream rules ran.
- Static fallback: all rule states and both outcomes at once, with a persistent bracket/line and label for the first divergence.
- Nearest type: Flowchart; Sequence only when actor messages and time are also load-bearing.

## 97. Secure Paved Road
- Use when a supported route from intake/build to deployment is the point: trust boundaries, privileged moments, permitted versus forbidden ingress, approved versus blocked deploy paths.
- Required: labeled trust boundaries, actors and identities, permitted ingress with a positive text label, forbidden ingress terminating at the boundary, approved deployment path, blocked bypass path, privileged gate, isolated runtime, audit destination.
- Distinguish routes with different line styles and stop symbols in addition to color.
- Budget: `≤3` trust zones, `≤8` components, `≤10` paths, `≤2` forbidden paths, one privileged gate; split control detail into a catalog figure.
- Avoid a dashed box called "security" with no route semantics, forbidden arrows crossing into the protected zone, unlabeled secrets or identity, every component styled as trusted, and a bypass path that visually rejoins the approved route.
- Static fallback: every boundary and both permitted/forbidden routes; blocked paths must visibly stop before entry or deployment.
- Nearest type: Architecture.

## 98. Governance and Control Catalog
- Use when a control inventory must be understood by where it is enforced (authoring, workspace, merge, deploy/runtime, or another named surface).
- Required: enforcement-surface groups, named controls, enforcement actor (`code`, `platform`, `human`), timing (`write`, `merge`, `deploy`, `run`), bypassability or exception route, coverage/gap notation.
- Budget: `3–5` surfaces, `3–7` controls per surface, `≤24` controls total, `≤3` attributes per control; summarize counts only when the item list exists elsewhere.
- Avoid 35 tiny pills, grouping by vague themes instead of enforcement point, mixing aspirations with enforced controls, icons without control names, and claiming defense-in-depth without showing surface coverage.
- Static fallback: the complete grouped catalog with surface headers and text labels for actor and timing; preserve gaps and exceptions.
- Nearest type: Layer stack; a security matrix when role permissions dominate.

## 99. Compensating Security Layers
- Use when no layer is perfect, each defense covers a failure left by the previous one, and residual risk must visibly narrow, transfer, or remain.
- Required: ordered threat/risk input, named layers, each layer's mitigation, explicit limitation or escape, a residual-risk carrier between layers, final residual risk and consequence/response.
- Show reduction with labels or decreasing measures, never area alone.
- Budget: `3–5` layers, one primary risk thread, `≤2` mitigations per layer, one final residual-risk statement; split unrelated threats into separate figures.
- Avoid implying the final layer makes risk zero, equal opaque slabs with no propagation, treating audit as prevention, shrinking shapes without numeric or verbal meaning, and reversing prevention/detection/recovery order unexplained.
- Static fallback: the complete chain — initial risk → mitigation → escaped risk at every layer → final residual risk and response.
- Nearest type: Layer stack; Nested when containment boundaries carry the meaning.

## 100. Traceable Block Decomposition
- Use when a system must decompose into individually citable sub-elements with stable identifiers, each traceable to its parent, its inputs/outputs, and its implementation.
- It documents structure, not process; sequences of actions belong in Flowchart or Swimlane.
- Give each block a stable dotted ID (e.g. `PAY-001-02`) shown as a compact badge in the node's type-tag chip, never as a connector-adjacent label.
- Name blocks with noun phrases ("Fraud Screening"), not verb phrases.
- Parent-child structure uses the tree's own elbow connector; add no new connector semantics or connector labels.
- Show at most one short inbound and one short outbound port label per block in the sublabel slot, and only when both fit without crowding; omit by default.
- Keep inputs, outputs, constraints, assumptions, and implementation paths in node metadata, never as additional visible text.
- Budget: the tree's root + 3 tiers, 5 per level, and the global 9-node ceiling; larger hierarchies split into linked per-subsystem diagrams.
- Avoid four-sided Input/Control/Output/Mechanism boxes, input/output arrows between siblings or cousins, ID badges with no matching metadata, and treating the visible diagram as the complete record.
- Always static; every badge, name, and port label must be legible in one frame.
- Nearest type: Tree.

## 101. Lifecycle Phase Map
- Use when one subject advances through named phases while waits, retries, cancellation, recovery, and terminal outcomes matter as much as the happy path.
- Required: a left-to-right primary phase rail of `4–5` ordered phases, a separate interruption/recovery band, a separate terminal-outcome band, labeled transitions, and distinct terminal boxes for cancellation and failure.
- Budget: `4–5` primary phases, `≤2` wait/recovery states, `≤2` terminal states, `≤9` states, `≤10` transitions.
- Avoid actor lifelines disguised as phases, request/response exchanges, every implementation guard, interruption states on the primary rail, cancellation and failure collapsed into one color-only state, and retry loops with no labeled re-entry point.
- Static fallback: full rail, every supporting state, both terminals, all labeled transitions; position and band labels distinguish progress, interruption, and termination without color.
- Nearest type: State Machine; Sequence when actor messages or timing carry the story.

# Part 16 — Motion in Diagrams

## 102. Static by Default
- Animation explains a complete static diagram; it never supplies missing meaning.
- Default mode is `none`: a complete, stable, script-free figure.
- Add motion only when explicitly requested or when it materially clarifies order, accumulation, evaluation, containment, or propagation.
- Motion never rescues an over-dense or unlabeled static diagram.

## 103. Motion Modes
- Choose exactly one mode per figure: `none`, `reveal`, `step`, or `loop`.
- `none`: default; also the print, screenshot, export, and reduced-motion state.
- `reveal`: one deterministic autoplay run ending complete; never auto-replays.
- `step`: paused semantic states advanced by the viewer; for teaching, comparison, and policy traces.
- `loop`: one decorative token repeating without changing meaning; cycle `≥3s`.
- Only `loop` repeats; queue state, typing, field values, policy outcomes, containment, and audit entries use `reveal` or `step` and finish complete.

## 104. Reveal Is the Only Autoplay
- `reveal` may run once on initial load when motion was requested, then stays complete.
- It never restarts on viewport re-entry, tab return, or without an explicit Replay.
- The anti-pattern is repeated or attention-trapping autoplay, not any motion before interaction.

## 105. Complete Source Frame
- Every semantic node, label, connector, status, and outcome is present and visible before enhancement.
- Only an initialized motion state may hide or transform items; a failure before initialization leaves the complete figure visible.
- No-JavaScript, print, static capture, and exported states all show the complete frame with controls and decorative tokens hidden.

## 106. Motion Timing Clock
- `--motion-fast: 160ms`.
- `--motion-step: 480ms` (transition duration).
- `--motion-hold: 720ms` (time per step).
- `--motion-total` = step count × hold, and `≤8000ms`.
- Default example: 5 steps × 720ms = `3600ms`.
- Slower physical reveals (exploded or plan views) use `--motion-step: 600ms`, `--motion-hold: 900ms`, 3 steps, `--motion-total: 2700ms`.
- Derive delays from integer steps; no randomness, springs, or transition-event timing.
- Allowed ranges: transitions `160–600ms`, holds `400–1200ms`, total autoplay `3–8s`.

## 107. Motion Easing and Entry
- Easing: `cubic-bezier(.2,.8,.2,1)` for opacity and transform.
- Hidden items rest at `opacity: .12` and `translateY(8px)`, then settle to `opacity: 1` and no transform.
- Path draws animate dash offset linearly over one step, on a decorative duplicate with `pathLength="1"`, stroke-width `3`, accent color.
- Flow tokens travel linearly over `3.2s`.
- Labels on lifted parts fade in over `--motion-fast`, linear, delayed by `--motion-step`.
- Items appearing from above may start at `translateY(-16px)` and `opacity: 0`.

## 108. Step Order and Budget
- Number items with integer steps `1–8`; DOM order follows narrative order.
- At most `2` items enter per step.
- `≤8` semantic steps (target `3–6`), `≤12` marked items, `≤2` drawn paths with one active, one flow-token loop.
- Translation `≤24px` everywhere, except an exploded part travelling straight up by exactly its declared explode distance.
- Completion exposes all items; Replay resets to step 0; Pause holds and resume continues from the same step.
- Pause when the page is hidden and do not catch up later.

## 109. Motion Primitives
- Path draw: decorative duplicate over a labeled base connector; `≤2` paths.
- Staggered reveal: opacity plus translate `≤8px`; `≤8` steps, `12` items.
- Queue counter: stable slots plus a visible numeric count; `≤5` items, never reorder.
- Typing/field population: full accessible string with a clipped decorative overlay; `≤32` typed characters or `6` fields.
- Policy evaluation: ordered rule rows with text statuses and a current-row outline; `3–6` rules, `2` traces.
- Flow token: hidden-from-assistive-tech token on a fixed path; one token, loop `≥3s`.
- Containment: reveal children, then a persistent labeled boundary; one boundary transition.
- Audit append: chronological rows with stable timestamp/sequence; `≤5` rows.
- Every primitive carries text, count, symbol, pattern, or outline in addition to color.

## 110. What Never Animates
- Never animate layout coordinates, connector routes, the viewBox, node dimensions, or semantic text.
- Avoid zoom, parallax, bounce, shake, glow, particles, and indefinite blinking.
- Nothing flashes or changes luminance more than three times per second.
- Never encode pass/fail, queue fullness, or outcome by hue alone.

## 111. Playback Controls
- Every interactive `step` figure has native Play, Pause, Replay, Previous, and Next buttons outside the SVG.
- Targets `≥44×44px`, padding `8px 12px`, `1px` muted border, radius `4px`, `600 12px` sans label.
- Visible focus ring `3px` solid accent with `2px` offset; hover shifts border to accent.
- Disabled controls at `opacity: .45`; play/pause expose pressed state.
- Controls sit in a row with `8px` gaps, `16px` above, separated by a `1px` rule.
- Show a visible step label ("Step 3 of 5") in `500 12px` mono, muted, right-aligned, plus visible keyboard instructions.

## 112. Keyboard Behavior
- `ArrowRight` advances, `ArrowLeft` goes back, `Home` resets, `End` completes.
- `Space` toggles play/pause unless focus is already on a native control; unmodified `R` replays.
- Never intercept `R` with Control, Command, or Alt held; never capture keys from inputs, links, or unrelated regions.
- Never move focus as the frame changes.
- Controls act only on their own figure; state never crosses figure boundaries.

## 113. Reduced Motion and Accessibility
- Under reduced-motion preference, initialize at the complete static frame, hide and disable all playback controls, and hide decorative movement.
- State that playback is unavailable; never announce partial steps beside a complete frame.
- The figure's title and description describe the complete meaning, not the animation.
- Decorative overlays are hidden from assistive technology; semantic text exists once in the accessibility tree.
- Announce user actions politely (e.g. "Step 3 of 5: first divergence"); do not announce every autoplay frame.

## 114. Deterministic Capture
- Static capture must be exact: two captures at the same viewport, fonts, and scale are pixel-identical.
- Wait for fonts to be ready before capture; never capture after an arbitrary wall-clock delay.
- Exports are the static final state unless a named intermediate step is explicitly requested.

# Part 17 — Diagnosing & Fixing Bad Diagrams

## 115. Should This Be a Diagram
- Ask whether a reader would learn more from the diagram than from a well-written paragraph; if not, don't draw.
- Lists of anything become a table or bullets.
- Before/after attribute comparisons become a table.
- A one-shape "diagram" becomes a sentence.
- Diagrams that change every sprint and live with code are better as text-based diagrams that diff.

## 116. Over-Budget Figures
- Default ceiling is `9` nodes and `12` arrows; beyond that, split into overview plus detail.
- Never shrink text to keep one canvas.
- The highest-quality move is usually deletion; every node earns its place.
- Target density `4/10`.

## 117. Accent Overuse
- Reserve the single accent for `1–2` focal elements the reader should see first.
- Coral or accent on every box is a failure; demote everything non-focal to the ink ramp.

## 118. Forbidden Decorations
- No shadows, ever; ground objects with their own base instead of a contact shadow.
- No diagonal connectors; use rounded orthogonal elbows.
- Do not make it look like an auto-layout renderer's output.

## 119. Label Collisions
- An arrow label sits `6–10px` clear of its own connector.
- Paint order is background → zones → arrows → labels → nodes, so a label mask that overlaps a later-painted node renders as a fragment on the node border.
- A label mask may overlap an earlier-painted zone container, and a mask fully inside a node is a legal badge chip.
- Connectors never pass behind non-endpoint boxes.
- Label placement is a geometric property: verify coordinates rather than trusting the eye.

## 120. Grid Drift
- Every coordinate, width, and gap is divisible by `4`; off-grid placement is what makes diagrams feel machine-generated.
- Exception: data-driven coordinates (e.g. running totals) round to the nearest pixel, because snapping would misstate values.

## 121. Off-Looking Skin
- When a new palette looks wrong on some types, tune `muted` first; it is usually too dark or too light against the new paper.
- Check the new skin across every type, not just one example.

## 122. Clipped or Blank Edges
- Keep the `40px` safe margin; never pad or crop a finished diagram to fit a frame.
- An SVG holds its readable width (minimum width equals viewBox width) so the type ramp is never silently scaled down; narrow screens scroll the diagram, not the page.
- In print, let the diagram scale down to the sheet: smaller but whole beats sharp but cut off.

## 123. Readiness Checklist
- State the chosen type, pattern, size, and planned cuts before rendering.
- The result opens offline as one file, with no network requests beyond fonts (none with system fonts).
- Screen readers announce the title and description.
- Reduced motion shows the complete static frame.
- After brand onboarding, diagrams use the brand's paper, ink, accent, and fonts.

# Part 18 — Brand & Style Profiles

## 124. Semantic Color Roles
- The skin uses `5–7` roles: `paper`, `paper-2`, `ink`, `muted`, `accent`, `rule`, plus a link role.
- `paper`: background of the body or dominant large region.
- `ink`: primary body-text color.
- `muted`: secondary text (captions, meta).
- `accent`: most-used brand color (CTA, link, heading accent).
- `paper-2`: container/card background slightly darker than paper.
- `rule`: hairline color, expressed as ink at about `0.12` opacity.
- Always reference roles by name, never by raw hex value.

## 125. Default Skin
- Paper `#f5f5f5` (white smoke), ink `#2d3142` (jet black), accent `#bf4520` (darkened tangerine that clears `4.5:1` as text), muted `#4f5d75` (blue slate), rule `rgba(45,49,66,0.12)`.
- Text roles clear `4.5:1` and essential marks clear `3:1` on both light and dark paper.

## 126. Typography Roles
- Title: Instrument Serif (also italic callouts).
- Node names: Geist sans.
- Technical sublabels: Geist Mono — for ports, URLs, field types, not a blanket "dev" aesthetic.
- When extracting from a brand: `<h1>` family → title, body family → node names, code/pre family → sublabels.
- If a brand has only one family, keep the defaults for missing roles; never force a mono face the brand doesn't use.

## 127. Brand Font Fidelity
- Never replace a detected brand family with a generic serif, system-ui, or monospace stack just to avoid a dependency; the font is part of the visual system.
- Record family and weight for heading, body, and technical labels and trace each to its source.
- Carry publicly available families with exact names and weights; preserve intentional system stacks in order.
- Custom-hosted or paid fonts are labeled `fallback` unless separately approved and packaged; never claim an exact match.
- Verify the rendered family; a declared family that failed to load does not pass.
- Figures with their own stylesheet may intentionally differ from the site's global type; inspect them separately.

## 128. Offline Fonts
- A font source of `system` makes the diagram request nothing; stacks fall back to the platform's serif, sans, and mono faces.
- Choosing system fonts counts as a customization worth preserving.

## 129. Contrast Constraints
- `ink` on `paper` `≥4.5:1`; `muted` on `paper` `≥4.5:1` for body text at diagram sizes (`9–12px`).
- Accent must be the most saturated color, not muted-ish or near-grey.
- Paper should not be pure white; fall back to `#fafaf7` to preserve the warm-neutral feel unless pure white is confirmed intentional.
- If a check fails, propose an adjusted value and explain why.

## 130. Dark Variant
- Generate dark values by inversion: ink-based rgba tints become tints of the dark ink (`rgba(ink-rgb, X)`).
- For dark-first brands, treat their dark paper as the default and generate the light variant by inversion (or ask which is primary).

## 131. Crowded Brand Palettes
- With `6+` brand colors and no clear hierarchy, pick one as accent and demote the rest to muted variants or ignore them.
- With multiple accent candidates, list them and let the owner pick; don't guess.
- With multiple themes, ask which one becomes the diagram skin.

## 132. Token Extraction Heuristics
- Variable names containing `background`, `bg`, `paper`, `surface`, `canvas` → paper.
- `foreground`, `text`, `body`, `ink`, `on-surface` → ink.
- `muted`, `subtle`, `secondary`, `caption` → muted.
- `accent`, `brand`, `primary`, `cta`, `highlight` → accent.
- `border`, `rule`, `divider`, `outline` → rule.
- `mono`, `code`, `pre` → sublabel font.
- Declared design tokens take priority over values inferred from prose or rendered pages.
- Prefer text-heavy pages (blog, docs) over imagery-only homepages; sample `2–3` pages and merge signals.
- If brand fonts can't be replicated, skin only the colors and keep default typography.

## 133. Brand Fidelity Receipt
- When matching a brand, report sampled sources, detected paper/ink/muted/accent/surface/rule values, title/body/technical families with weights, `exact` or `fallback` per font role, and any figure-specific overrides.
- Flag low-confidence mappings so they can be corrected before applying.
- Show only the token changes as a diff; everything else stays the same.
- Brand onboarding stays pending until a human views a representative output and approves palette, typography, contrast, and rendering.

## 134. Named Client Profiles
- A profile is a complete style-guide snapshot, not a partial override, so it is simple to inspect and never needs merge interpretation.
- One project selects one profile; parallel client workspaces each read their own profile and never overwrite a shared skin.
- Keep a pristine `default` profile as the recovery copy of the shipped skin; never snapshot a customized skin as default.
- Profile names are lowercase slugs `[a-z0-9][a-z0-9-]{0,63}`.
- Saving and loading copy token values byte-for-byte; never normalize, reorder, or reinterpret them.
- When a newer schema adds roles, backfill only missing rows from shipped defaults and keep every existing value.
- A missing selected profile is never silently replaced by another client's skin.

## 135. Never Ship Default Into a Brand
- On first use in a project still on the default skin, pause and offer brand onboarding, manual tokens, a saved profile, or an explicit default.
- Treat a skin as customized if any semantic role, font family, or font source differs from defaults; don't infer from accent alone.

# Part 19 — Briefing a Diagram

## 136. Confirm Before Drawing
- Before drawing, state the visual type, optional semantic pattern, size preset, and what the complexity budget will cut.
- Keep one type, one size, one destination per request.

## 137. The Four Dials
- Format: `html`, `svg`, `png`, `html+png` — SVG for vector editing, PNG for slides, HTML for the web.
- Size: `doc-inline`, `doc-wide`, `slide-16x9`, `slide-4x3`, `social-og`, `social-square`, `print-a4-landscape`, `print-a3-landscape`, `print-letter-landscape`, `fit`.
- Detail: `faithful` (`≤24` nodes, zoned), `balanced` (`≤12`), `simplified` (`≤7`).
- Audience: `engineer`, `mixed`, `executive` — changes wording, not count.
- Infer what the destination makes obvious; ask once only when a choice materially changes the result.

## 138. Size Changes the Type Ramp
- Size sets both the viewBox and the type ramp: a projected slide gets `16px` node names, not `12px`.
- `doc-inline` for docs, `slide-16x9` for decks, `social-og` for cards, `fit` for vector hand-off.

## 139. Audience Wording
- Engineer: full technical detail (`Auth Service / JWT · RS256 · :8443`).
- Mixed: plain function (`Auth Service / token check`).
- Executive: the outcome (`Sign-in`).
- Preserve proper nouns; expand acronyms once.

## 140. Brief Contents
- Name the system, list nodes (`≤9`), name `1–2` focal elements, choose size and format.
- For brand-first work: match the brand, approve tokens, save a profile, then draw.

## 141. Name the Story
- Write the diagram's story in one sentence first; anything not serving it is a cut candidate.
- Choose `1–2` focal nodes the reader should look at first — sometimes the entry point or the new component, not the busiest node.

## 142. Do-Not List
- No renderer look-alike, no shadows, no accent on every box, no diagonal connectors, no more than nine nodes in one figure.

# Part 20 — Restyling Imported Diagrams

## 143. Redraw, Not Convert
- An import is a redraw: the source supplies content (components, relationships, grouping, direction), never geometry, palette, fonts, or shape styling.
- A converter that preserved the source layout would just be the source tool's output with different fonts.

## 144. Discard Source Geometry
- Start from a blank viewBox chosen by the size preset; never draw first and crop after.
- Hand-dragged positions land on odd pixels; lay out from scratch on the `4px` grid with dominant flow left→right or top→bottom, aligned zones, and even gaps.
- Auto-layout renderer positions are never recreated.
- Declared direction (`TD`, `LR`, `RL`, `BT`) is a hint; the target type's conventions may override it.

## 145. Discard Source Palette
- Source color is a signal about role, not a color to keep; six source fills never become six output fills.
- The palette is one accent plus the ink ramp.
- Blue generic components → white fill, ink stroke (backend/API).
- Green "ok/primary" → ink treatment; accent only if focal.
- Orange "attention/queue" → ink treatment; accent only if focal.
- Red "failure/risk/legacy" → optional/async treatment: dashed ink at `0.20`.
- Purple "external/third-party" → external/cloud treatment: ink at `0.03` fill.
- Grey "infrastructure" → store/state or zone container.
- Unfilled → backend/API.
- A branded source is redrawn in the project's own skin.

## 146. Map Shapes to Treatments
- Cylinders → flat store/state box (ink at `0.05` fill, muted stroke), never a 3-D barrel.
- Rhombus → decision diamond only in a flowchart; elsewhere a normal box, or an edge label when it's a single decision inside an architecture.
- Actor → input/user treatment or the user icon.
- Cloud → external/cloud treatment.
- Notes → annotation callouts, `max 2`, or drop.
- Vendor icons → matching monochrome icon inheriting the current color.
- Custom images/logos → nearest icon or a labeled box; never re-embed source images.
- Floating text → drop or fold into a zone label.
- Containers, subgraphs, and frames → quiet zone frames; they group, they don't act.

## 147. No Imitated Hand-Drawn Strokes
- Do not imitate a whiteboard's sketchy stroke; it is the source tool's skin.
- If a hand-drawn feel is explicitly wanted, apply the sketchy treatment to a clean layout, not a reproduction of the source wobble.

## 148. Reroute Every Connector
- Source waypoints are dead weight; they show how tangled the original was, not how to route.
- Rounded orthogonal elbows, fanned attach points, no overlaps — no exceptions for imported content.
- Never preserve diagonal connectors.
- Invisible layout links create nodes but no drawn edge; edge length markers are ranking hints.

## 149. Prune Edges
- Drop edges the layout already implies (e.g. downward flow in a stack).
- Keep edges that carry a label, cross a zone boundary, or run against the dominant direction.
- Dangling edges with deleted endpoints are source rot; omit them.

## 150. Rewrite Labels
- Source labels are written by the author for the author: `svc-auth-prod-v2` becomes `Auth Service`.
- Expand whiteboard shorthand into names a reader can use.
- Strip markup; preserve proper nouns and meaning.
- Never romanize CJK or non-Latin labels; use font fallback.
- If labels are empty, ask what the boxes are; never invent names.
- Infer roles from labels (`DB`, `queue`, `user`) when the source has no shape vocabulary, and say so.

## 151. Preserve Meaningful Structure
- Keep meaningful edge labels, state guards, decision branches, sequence order and fragments, ER cardinality and fields, container membership, and flow direction.
- Cycles meaningful to the flow become labeled loops (e.g. a self-loop as a retry loop).

## 152. Pick the Target Type From Content
- Source shape vocabulary is a hint, not an instruction; people draw rectangles because rectangles are on the toolbar.
- Lifelines → Sequence; tables/rows of fields → ER; aligned lanes → Swimlane; rhombus with labeled yes/no → Flowchart; mostly ellipses with cycles → State; cloud icon families → Architecture; nested containers with few edges → Nested; single-entry fan-out → Tree or Org chart; neighbour-only stacks → Layer stack; dated labels on one axis → Timeline or Gantt; anything else → Architecture.
- Override when content disagrees (diamonds asking "which service?" are architecture), and say so in one line.

## 153. Degrade Ladder
- Compress in fixed order: decorations, then duplicates, then leaf clusters, then infrastructure.
- Drop unconnected nodes first (usually legends, titles, abandoned notes), then collapse the author's own groups.
- Sources with `40+` nodes never get `faithful`; propose overview plus per-zone detail before drawing.
- Multi-page or multi-block sources yield one independently typed diagram per page; never merge them onto one canvas unless asked.
- Never add components to fill space; imports stay bounded by source meaning.

## 154. Fidelity Ledger
- Every import reports source count, drawn count, and every merge, collapse, and drop.
- Example: "balanced · 12 source nodes → 8 drawn; collapsed decision → edge label; dropped 1 unconnected sticky note; kept the request path in full."
- Never drop content silently; the owner knows the source and will notice.

# Part 21 — Export Fidelity

## 155. Diagram-Only Exports
- SVG and PNG exports contain only the diagram; editorial headers, summary cards, and footers are dropped.
- Never wrap HTML chrome into an SVG via foreign objects; too fragile across renderers.
- For the full editorial layout, use a full-page screenshot or print to PDF instead.

## 156. PNG Sizing
- PNG pixel size = viewBox × scale; the size decision was made when the diagram was drawn.
- Default scale `2` (docs, wiki, projected slides): `1280×720` → `2560×1440`.
- Print/PDF handout: scale `3` → `3840×2160`.
- Inline thumbnail or email: scale `1` → `1280×720`.
- Fractional scales within `1–4` hit exact sizes: `scale = target_width / viewBox_width` (e.g. `960` wide at `1200px` → `1.25`).
- Never scale below `1` (soft-focuses type); redraw at a smaller preset instead.
- Never scale past `4`; redraw at a larger preset instead.
- If the target aspect ratio differs from the viewBox, offer a redraw at the matching preset; padding or cropping breaks the `40px` safe margin.

## 157. Transparent PNG Background
- PNGs always have a transparent background so they sit on any slide or doc color without a white halo.

## 158. Self-Contained SVG
- Carry the diagram's own styles into the SVG so class-styled shapes don't export as black boxes.
- Keep the figure's own color tokens scoped to the figure.
- Carry the page's text color and font family onto the figure, since strokes using current color and unstyled text inherit them.
- Drop page chrome rules (body, headings, cards, header, footer, layout).
- Keep print-only styling inside its print condition so it never becomes screen paint.

## 159. Unique IDs When Inlining
- Prefix every reusable definition (markers, patterns, gradients, filters, clip paths, masks, symbols) with the figure's slug so a light figure beside its dark twin doesn't share arrowheads.
- Keep per-figure, per-variant title and description IDs so accessible names stay unique.

## 160. Strict-Consumer Color Safety
- Some slide importers paint rgba and `transparent` as opaque black, turning a faint tint into a solid block that swallows its label.
- Convert rgba fills/strokes to hex plus an opacity attribute, and `transparent` to `none`, when alpha can be preserved.
- Keep rgba wherever inherited or overriding paint makes splitting unsafe.

## 161. Font Portability
- Vector exports render correctly in modern browsers, but tools that don't fetch fonts will substitute typography.
- For pixel-perfect portability, prefer PNG.
- With a system font source, the SVG makes no font request.

## 162. Motion Exports
- Export the explicit complete static frame after fonts are ready; never at an arbitrary delay.
- Controls and decorative tokens are absent; all semantic labels and relationships remain.
- Export only a named intermediate step when explicitly asked.

## 163. Export Is Manual
- Never emit SVG or PNG automatically alongside a diagram; export only on request.
- Export never modifies the source or adds scripts or export buttons.

## 164. Block Metadata Registry
- For traceable block diagrams, a structured registry is a projection of block metadata exactly as authored — never inferred, summarized, or supplemented.
- Blocks appear in document order; root blocks omit parent; absent fields are omitted, not empty.
- No timestamps, so identical sources produce identical output.

# Part 22 — Design Decisions & Rationale

## 165. Static, Script-Free Output
- Diagrams are shared as single files and embedded in posts, decks, and docs, so default output is static with no script.
- When motion is requested, one reviewed, fixed controller is used verbatim; it cannot be extended per diagram.
- Bespoke interaction (click-to-expand, filtering) is out of scope.

## 166. Behavior Is a Separate Axis
- New behaviors become semantic patterns routed onto existing visual types rather than new types, to avoid ballooning the taxonomy and diluting selection.
- A pattern owns semantic primitives and a tighter budget, never a second layout grammar.
- A new visual type is admitted only for a genuinely new layout grammar no existing type provides.

## 167. Rejected Types
- C4 views are a zoom-level convention over architecture, not a new grammar.
- AI-agent/RAG architecture is boxes, arrows, and a decision loop — a pattern over architecture.
- Mindmap is a radial restatement of a tree.
- UML use case ovals carry no structure and rarely survive an editorial cut.
- Pie/donut: lists of anything become a table.
- Git graphs and packet diagrams: narrow audiences, weak editorial fit.
- Activity diagrams route to swimlane plus flowchart; a fork/join bar alone doesn't earn a type.
- Event flows route to data flow via the fan-in queue pattern.

## 168. Admitted Layout Grammars
- Sankey: band width encodes a quantity that splits and merges.
- Fishbone: angled category bones converging on one effect.
- Wardley map: value chain × evolution axes with dependency links and movement.
- Kanban: state census in columns with WIP limits and no connectors.
- User journey: stage grid plus a sentiment curve.
- Deployment: zones containing hosts containing versioned artifacts, with replica counts and protocol:port paths.
- Dependency graph: ranked DAG allowing many parents and representable cycles.
- UML class: three-compartment boxes where the arrowhead carries the relationship meaning.
- Story map: narrative backbone crossed by release slices and a cut line.
- Database schema: foreign keys anchored column-row to column-row with types, constraint chips, and index compartments; entity-level ER stays separate.
- Treemap: recursive area subdivision.
- Polar: angle for ordered cyclic categories, linear radius for one quantity.
- Heatmap: grid cells whose fill opacity encodes a value across two categorical axes.

## 169. Connector Exemptions
- Orthogonal elbows are mandatory, with narrow exemptions scoped to one element each: Sankey ribbons, fishbone bones, Wardley dependency links, journey sentiment curves.
- Kanban, story map, and service blueprint simply have no connectors.
- Plain straight lines are reserved for connecting elements that share a level.

## 170. Waterfall as Running Total
- A waterfall anchors totals at the floor, floats signed bridges between running levels, and carries the running total across every gap.
- Budget: `8` bars including both totals, at most `1` subtotal.
- Sign is encoded by fill weight, not hue: increases take the default tint, decreases are hollow, so direction survives greyscale and color-vision deficiency.
- Accent stays editorial: `≤1` focal bridge.
- Data coordinates round to the nearest pixel and are exempt from the 4px grid; snapping would move money that doesn't exist.
- Two-endpoint comparisons go to a dumbbell instead.

## 171. Architecture Delta
- Compare two system states as Before · Changes · After: two equal grids joined by an exact change ledger.
- Unchanged components keep identical local positions and stable identities across both snapshots; a real relocation needs an explicit MOVED record.
- Status reflects actual difference: ADDED, REMOVED, CHANGED (different semantics), MOVED (different position), REWIRED (different endpoints).
- `changed moved` and `changed rewired` may combine; presence/absence and unchanged are exclusive.
- Each difference has exactly one visible ledger entry; a two-change object has two.
- Budget: `8` components, `10` relationships, `8` ledger entries.
- Carry each state with text plus shape/dash; color is secondary and accent stays editorial.
- Attribute-only comparisons remain tables; a single snapshot uses Architecture.

## 172. Exploded Axonometric
- Draw one object in `2:1` dimetric projection with parts pulled apart along one axis at equal gaps.
- Parts sitting side by side in the assembled object share a level and explode together.
- Slab, box, and cylinder are one rounded prism at different corner radii; a container is that prism with a cavity.
- No contact shadow; the bottom part grounds the object.
- Labels sit in a leader column with straight leaders that start on the part and cross no other part.
- Budget: `5` parts, `5` levels, `1` focal part.
- In motion, the figure opens assembled and lifts apart once; each part travels straight up exactly its explode distance.
- Canonical stills stay static; animated versions are separate.

## 173. Axonometric Plan
- One floor or site from above at an angle: boxes on a shared plate in real positions, painted back to front.
- Depth order is topological — A before B when A lies entirely behind B and outlines overlap; sorting on `x + y` draws long walls over the desk in front.
- Walls cut at desk height so every room reads from one view.
- Tags sit on the floors or roofs they name, paint last, never overlap, and every room or building has one.
- Budget: `8` tagged rooms or buildings, `40` boxes, `1` focal.
- A phased reveal moves each building `16px`, within the motion limit.

## 174. Service Blueprint
- A shared stage grid with required customer / frontstage / backstage rows split by a line of visibility; optional evidence and support rows.
- Stages are equal columns; stage order is the sequence, so no connector arrows are drawn.
- Wait times and system names are cell text.
- Budget: `6` stages, `1` focal cell.

## 175. Traceable Blocks on a Tree
- Tree, not Nested (single chain can't show siblings) or Architecture (flat, max 3 zones).
- Noun-phrase names, because the figure documents structure, not functions.
- Three-tier visibility resolves minimalism versus rich metadata: ID badge, name, and at most one port label on the canvas; full record in metadata; longer text in a generated registry.
- A hand-maintained parallel record is rejected because it drifts from the diagram.

## 176. Verified Label Geometry
- Label placement against nodes is an explicit rule checked from coordinates, because review missed clipped labels across many shipped figures.
- A rule that only lives in prose ships broken examples.

# Part 23 — Cookbook Recipes

## 177. First Diagram in a Project
- Check the skin first; offer onboarding, a profile, or an explicit default if it's still shipped defaults.
- Confirm type, pattern, size, and cuts before drawing.
- Write one self-contained file; never overwrite reference specimens.
- Run the pre-output checklist: orthogonal connectors, `4px` grid, `≤9` nodes unless split, accent on `≤2` focals.

## 178. Selection Cheat Sheet
- Fan-in, queues, bottlenecks → fan-in queue → Data flow.
- Repeated stage slots → stage framework → Process.
- Messy input to durable artifact → unstructured → structured → Data flow.
- Two policy traces, first divergence → paired traces → Flowchart.
- Trust boundaries → secure paved road → Architecture.
- Controls by enforcement layer → governance catalog → Layer stack.
- Compensating defenses, residual risk → compensating layers → Layer stack.
- If a table or paragraph is clearer, don't draw.

## 179. Architecture for Docs
- Brief: system, `≤9` nodes, `1–2` focal, `doc-inline`, HTML; confirm type and cuts first.

## 180. Deck Redraw
- Redraw a source for a `16:9` slide at `simplified` detail for an `executive` audience, as PNG.

## 181. Text Diagrams in a README
- Import every block at `doc-wide`, `balanced` detail, `mixed` audience, and report the fidelity ledger.

## 182. Brand Then Diagram
- Match the brand, approve the tokens, save a named profile for the project, then draw.

## 183. Containment Architecture
- When hierarchy itself is the claim, nest administrative bands and traffic boxes in one snapshot: dashed `rx=4` bands for billing and permissions, solid `rx=8` boxes for networks, managed services outside every subnet.

## 184. Core Design System
- One accent, `1–2` focal elements.
- Three families: serif title and italic callouts, sans node names, mono technical sublabels.
- `1px` hairline borders, no shadows, max border-radius `10px`.
- Every coordinate, width, and gap divisible by `4`.
- Annotation callouts: italic serif with a dashed Bézier leader for margin asides.
- Sketchy hand-drawn filter suits essays, not technical docs.
- Icons are monochrome and inherit the current color so they follow the skin.

# Part 24 — System Architecture Diagrams

## 185. Architecture — Layout & Zones
- Use for system overviews, integration maps and infrastructure topology: the question is "what talks to what".
- Group components by tier or trust boundary (frontend → backend → data; public → private). Run the primary flow left→right or top→down, pick one direction and hold it for the whole figure.
- Z-order is fixed: background → zones → arrows → nodes. Drawing connectors before boxes lets node fills hide line ends.
- Use 1–2 accent focal nodes at most: the primary integration point, the primary data store, or the key decision node.
- Zone rect: `rx="8"`, fill `ink @ 0.02`, stroke `ink @ 0.10`, `stroke-width="0.8"`. A fill stronger than a 2% wash competes with node fills.
- Zone eyebrow label: 7px eyebrow face, `letter-spacing="0.14em"`, centred, on a 12px-tall `rx="2"` paper mask at `zone_y + 4`, text baseline at `zone_y + 13`.
- Colour the zone label with the `soft` role, never ink at an opacity. Something like `ink @ 0.40` composites differently on each paper and can drop near 2.2:1 at 7px.
- Header gap: keep ≥16px (12–16px minimum) between the zone eyebrow and the first enclosed node. Zone `y` = node_top − 32.
- Dashed boundary rectangles mark regions (VPC, security group, trust zone). Their labels sit on a paper-coloured mask over the boundary line.
- At most 3 flat zones per diagram. More than that reads as a swimlane, so use that type instead.
- Pitfalls: every box in accent so hierarchy collapses; a bidirectional arrow where one direction is obvious; a legend floating inside the diagram area.

## 186. Architecture — Connector Routing
- Rounded right-angle (orthogonal) connectors are mandatory for any off-axis connection. A diagonal line between off-axis nodes is a hard fail.
- Two-bend elbow with corner radius `8`, where mid = (x1+x2)/2: `M x1,y1 H mid-8 Q mid,y1 mid,y1+8 V y2-8 Q mid,y2 mid+8,y2 H x2`. Flip the vertical signs for right+up.
- Use a plain straight line only when the endpoints share the same x or y.
- Standard solid connector: `stroke-width="1.2"`, one `marker-end`.
- Arrow labels on an elbow sit on the vertical segment, centred on `mid` and vertically between the two corners.
- Port selection: when the destination sits clearly above or below the source, enter its top or bottom edge with a single-bend L-path. Leave the source by the side facing the destination's column, run horizontally, turn once, then run vertically into the destination.
- Every segment leaves its box perpendicular to the edge it starts on. Never start a horizontal segment on a top or bottom edge: it hides behind the node fill and the arrow seems to grow out of the corner.
- Keep left/right destination ports for connections that travel mainly horizontally. A mainly vertical path entering from the side looks like it punctures the node face.
- Fan the ports when several connectors share a side edge, and keep each port ≥8px from a corner so it never lands on the corner radius.

## 187. Architecture — Crossings & Dashed Paths
- Optional, return, async and passive flows use `stroke-dasharray="4,3"` at a lighter `stroke-width="1"`. They follow the same orthogonal routing, port-selection and hop rules as solid paths. The dash carries meaning, not a different routing grammar.
- When two orthogonal arrows must cross, add a hop (bridge) on the less important one. The more important arrow stays unbroken.
- Horizontal hop over a vertical at `cx`: `H cx-8 a 8,8 0 0,1 16,0 H x2`, an 8px-radius semicircular bump. A vertical hop over a horizontal uses `a 8,8 0 0,0 0,16`.
- Bridge the passive, secondary, write-back, dashed or muted arrow. When dashed and solid cross, the dashed one always hops. Never bridge both.

## 188. Architecture — Containment Scopes
- Use containment when the network hierarchy itself is the claim and the reader must see what sits inside which scope. Flattening two levels into one eyebrow (`VNET · SNET-APP`) misrepresents the hierarchy.
- Connectors keep the architecture grammar. Containment geometry follows nested rules: consistent insets, one eyebrow per level, fills stepping up inward.
- Two scope kinds that never substitute for each other. An **administrative** scope (billing, permissions, lifecycle, carries no traffic) is a full-width horizontal band with a 24px header. A **traffic** scope (packets cannot cross without an explicit rule) is the standard zone box, `rx=8`.
- The shapes must differ, not only the colours, because greyscale still has to tell an admin band from a traffic box.
- Node kinds: compute workloads sit inside a traffic scope; private endpoints sit inside a traffic scope and name the managed service they reach; managed PaaS belongs to an administrative scope.
- Peering paths name the two traffic scopes they join.

## 189. Architecture — Containment Placement & Budget
- Never put a managed service (database, storage, PaaS) inside a subnet or VPC. It sits in the administrative band that owns it, and only its private endpoint lives in the subnet. A database drawn inside a subnet tells the reader that subnet's security rules protect it, which is false.
- Sibling axis: sibling traffic scopes at one level share one axis. Under an administrative band, a parent wider than tall (or square) lays its children out as a row on one shared `y`. A parent taller than wide lays them out as a column on one shared `x`.
- Nested children take the perpendicular axis: children of a scope in a row form a column, and their children form a row again. Never mix axes at one level.
- Budget: ≤2 administrative bands, ≤4 traffic scopes, ≤8 nodes, 2 accent elements. Split per subscription/account when a figure goes over.
- Draw every scope in place with its own x/y/width/height. Never position scopes with transforms, nested viewports, style rules or animation.

## 190. Architecture Delta — Panels & Mental Map
- Use to explain a migration, service extraction, infrastructure redesign or integration change as two synchronised topology snapshots. It shows what survives, appears, disappears, changes, moves or reconnects.
- Not for: a single snapshot (architecture); attribute-only differences with no topology story (comparison table); ordered phases or requests over time (timeline or sequence). A delta has exactly two states and claims no migration order, downtime or causality.
- Three panels in one reading order: **Before · Changes · After**. Both topology panels share width, height and internal grid. The centre is a short change ledger, not a third topology. Name each snapshot with a meaningful version or date.
- Keep the mental map stable: copy the Before coordinates into After. Move a retained component only when the move is part of the story and has a MOVED entry. Never lay out each panel independently.
- Grid: 4px pitch by default. Every component's local x, y, width and height is a multiple of the pitch. The two panel origins share one y.
- Budget: ≤8 unique components, ≤10 unique relationships, ≤8 ledger entries across the comparison. A retained ID counts once. A component that is both changed and moved uses two ledger entries. Split big migrations into subsystems or phases and never drop edges to fit.
- Connectors use architecture's rounded orthogonal routing, drawn before components. A stable relationship may take a new route to reach a moved component without counting as rewired.
- Small screens: keep the three-panel comparison in a horizontal scroll region with a visible scroll hint. Do not shrink labels until they are illegible, and do not stack the snapshots into separately scaled pictures.

## 191. Architecture Delta — Change Vocabulary
- Colour is secondary. Every change must read from text plus a shape or line treatment. Unchanged objects stay quiet context, and the single accent marks the editorial focus. Do not use five status colours.
- `unchanged`: plain solid outline, no ledger entry.
- **ADDED**: `+` badge or plus marker, solid outline. Present only in After.
- **REMOVED**: `−` badge plus a dashed outline or path. Present only in Before.
- **CHANGED**: `Δ` badge or inset rule, plus an explicit old → new description in the ledger.
- **MOVED**: direction or position marker plus a ledger entry naming the relocation. Applies to components only.
- **REWIRED**: a distinct dash or endpoint marker, with old → new endpoints written out. Applies to relationships only. Swapping source and target counts as a rewire.
- A component can be "changed moved" and a relationship "changed rewired". Unchanged, added and removed never combine with other states.
- A node missing from After is not a removal unless there is a REMOVED entry. Do not draw an ADDED edge to dodge explaining a rewire. A replacement component gets a new identity with separate REMOVED and ADDED entries; sitting in the same spot does not make it the same object.

## 192. Architecture Delta — Identity & Ledger
- Print the same stable ID in both states next to the human-readable name. Names, responsibilities, versions and protocols are semantic attributes, so an identity survives a rename when the underlying object survives.
- Mark an object changed if and only if its semantic signature (for example `orders-api:v2;mode=enqueue`) differs. Moving or rewiring alone never changes the signature.
- A retained component's position differs if and only if it is MOVED. A size change also requires CHANGED.
- Ledger: one short entry per (object, change) pair. Start with the uppercase change word, name the object, state the actual difference ("CHANGED orders — direct dispatch → enqueue"). Wrap long entries onto extra lines at a readable measure.
- The ledger covers exactly the implied changes: nothing missing, nothing duplicated, nothing for unchanged objects.
- Pitfalls: two independently arranged snapshots that invent movement; a ledger that only says "updated"; positions drifting without a MOVED entry; edges redrawn to new targets while still described as the same endpoints; treating the comparison as an executable migration plan.

## 193. Deployment — Nesting Levels
- Use for where software actually runs: hosts, VMs, pods and managed services placed in environment or network zones, with replica counts and versions. Architecture says what talks to what. Deployment says what is installed where, behind which boundary, and how many copies.
- If there is no placement decision to show (no zone boundary, replica count or version that matters), draw an architecture diagram. Logical architecture with hostnames bolted on is the classic failure.
- Level 1, **Zone**: a real environment or network boundary (`edge`, `prod / eu-west-1`, `data`). `rx=8`, fill `ink @ 0.02`, stroke `ink @ 0.20` dashed `4,4`. Uppercase tracked eyebrow at 8px (7px when tight), top-left, on a paper mask over the border. Draw zones first.
- Level 2, **Infrastructure node**: the standard node box at `rx=6`, with a rectangular type tag (`rx=2`, not a pill) reading `POD` / `VM` / `MANAGED` / `CDN` in the top-left.
- Level 3, **Artifact chip**: 24px tall, `rx=4`, fill `ink @ 0.05`, stroke `muted`. Image or service name left-aligned at 12px, version tag (`v2.4.1`) right-aligned at 9px. Stack co-located artifacts such as sidecars with an 8px gap.

## 194. Deployment — Replicas, Paths & Focal
- A node running N copies gets one replica badge (`x3`), right-aligned in its own small `rx=2` box in the node's top-right, 8px eyebrow. Never draw one node per replica.
- Network paths are orthogonal elbows labelled with protocol and port at 8px (`HTTPS:443`, `TLS:5432`). Unlabelled paths are wasted: protocol and port are the content.
- Colour by boundary: a path that crosses a zone boundary is `link` blue; a path inside one zone is `muted`. Async or replication paths are dashed `5,4`.
- Two accent elements at most: the single point of failure or the newly introduced piece. Example: a primary database (accent-tint fill, accent stroke) and its replication path to the standby (accent, dashed).
- Budget: ≤3 zones, ≤6 infrastructure nodes, ≤9 artifact chips, ≤8 network paths, ≤2 accent elements. Over budget → one diagram per environment.
- Pitfalls: zones that are only visual grouping; artifact chips without a version; vendor-icon soup in place of named nodes; staging and production side by side without a separating boundary.

## 195. Dependency Graph — When & Ranking
- Use only when the data shows what a tree cannot: a node with more than one parent (a shared dependency) or a cycle. If every node has one parent and nothing points back, draw a tree and say so.
- Ranked layers: rank 0 (entry points nothing depends on) at the top, deeper ranks below, rank rows `120px` apart.
- Forward edges point downward across ranks, or run horizontally within one rank. They never point upward, except the one marked cycle.
- Rank first, always. An unranked hairball is unreadable, and ranking is the structure, not polish.
- Nodes: standard box, `rx=6`, `160px` wide, `56px` tall. Draw one node per package, module or service, never per file.
- All connector rules apply: `r=8` elbows, 6–10px label margin, hops at crossings, attach points fanned ≥12px apart, no connector behind a box it doesn't connect to, no label mask clipped by a later node.

## 196. Dependency Graph — Treatments, Badges & Cycle
- Internal package/service: white fill + `ink` stroke. External/third-party: `ink @ 0.03` fill + `ink @ 0.30` stroke. Leaf with no outgoing edges: `ink @ 0.05` fill + `muted` stroke.
- Label external dependencies with version and registry in the sublabel (`v3.23 · npm`).
- Fan-in badge on every node: an 8px eyebrow count (`4 in`) in a small `rx=2` box at the top-right. The highest fan-in node is the structural story, so size nothing to compete with it. Without the badges the type loses its reason to exist.
- The cycle: at most one back-edge, the editorial point of the figure. `accent` stroke, dashed `5,4`, accent arrowhead, routed around the outside of the node stack (never through the middle or behind an unrelated node), with a masked 8px `CYCLE` label at its visible end.
- The two nodes the cycle touches keep their normal treatment. The 2 accent elements are the back-edge and its label, and nothing else in the graph is accent.
- Budget: ≤9 nodes, ≤14 edges, ≤4 rank layers, 1 highlighted cycle, 2 accent elements. Over budget → collapse a leaf cluster into an aggregate node (`+6 leaves`) and say so in a caption. Never silently drop nodes.

# Part 25 — Data Platform Overviews

## 197. High-Level — Purpose & Inputs
- Use for an end-to-end data-stack overview (ingestion → storage → query → analytics → visualisation) deployed on a container orchestrator. It combines a phase chevron banner, a deployment boundary, an orchestration bar, identity/cross-cutting footers and an optional right strip of vertical chevrons.
- Treat it as fully parametric: every coordinate comes from a small list of inputs (chevrons, sources, components, connections). The same inputs must always give the same picture, so never invent geometry on the fly.
- Inputs: ordered horizontal chevrons (each spanning 1+ columns); external sources (≤4); components of kind `node` (box in the cluster), `bar` (strip across the cluster top, usually orchestration) or `cross-cutting` (strip below the cluster); explicit connections; exactly one focal node.
- Reserved concern names that always render as vertical chevrons: Orchestration, Security, Observability, Governance, Backup.
- If no focal node is named, default to the first node under the Storage phase.

## 198. High-Level — Chevron Banner
- The banner is the legend that maps visual columns to functional phases. Never omit it.
- Banner at `y=4`, height `28`. Column base unit = floor-to-4 of effective width ÷ total columns. Each chevron is ≥`120` wide and a multiple of 4. The last chevron absorbs the remainder.
- Effective width is `1000`, or `964` when a right strip exists (28px strip + 8px margin). Every horizontal element ends at the effective width, and nothing goes in the 8px band.
- Chevron points are 12px deep. First: `(x0,4) (x1-12,4) (x1,18) (x1-12,32) (x0,32)`. Middle: the same plus a notch `(x0+12,18)`. Last: flat right end with the notch.
- Fills alternate between two dark band steps. Labels in a fixed light band-label colour, 7px mono eyebrow, `letter-spacing 0.14em`, centred at the chevron centre, `y=21`.
- One chevron may take a colour override (≤2 per diagram) to pair with a same-coloured component, e.g. a red Security chevron above a red Identity bar. The override changes the polygon fill only; the label stays band-label, and the neighbours' alternation does not shift.

## 199. High-Level — Source Zone & Cluster
- Source zone (external systems): `x=4, y=40`, width = first chevron width − 8, height `336`. Dashed stroke `ink @ 0.20`, `0.8`, `6,3`, `rx=6`, fill `ink @ 0.02`. The dashed border is what says "outside the cluster", so never make it solid.
- Source nodes: width = zone − 8, height `64`, first top `y=60`, `16` gap, role badge `EXT`. Cap at 4 sources, otherwise split.
- Cluster boundary: starts 4px after the source zone and runs to the effective width. `y=40`, height `336`. Solid stroke `ink @ 0.18`, `1.2`, `rx=8`, fill `ink @ 0.02`. Orchestrator icon and label sit bottom-left inside it.
- Canvas height = max(`540`, strip bottom + `112`). `112px` is reserved for the legend, and the canvas grows with each extra cross-cutting row.

## 200. High-Level — Bars & Cross-Cutting Rows
- Orchestration bar (inside the cluster): inset `12` from the cluster edges, `y=52`, height `44`. Stroke `ink @ 0.18` `0.8`, `rx=4`, fill `ink @ 0.05`. Name centred, subtitle below, tool icon at the far right.
- Cross-cutting rows (identity, observability, backup, lineage, secrets) stack below the cluster: `y = 388 + k·44`, height `40`, spanning the body width. Stroke `ink @ 0.20` `0.8`, `rx=6`, fill `ink @ 0.05`.
- Identity applies to every component, so its bar spans the full width outside the cluster. Never put it inside the cluster boundary.
- Cross-cutting rows emit no edges.

## 201. High-Level — Component Nodes
- Node `152 × 80`. Its centre x must equal its phase chevron's centre x. This is non-negotiable and is what makes the banner a real legend.
- Several nodes in one phase stack vertically: first top `y=120` if a bar sits above the column, else `64`, then gap `16`.
- Anatomy: role badge top-left (12px high, e.g. `COLL`, `STORE`, `VIRT`); 24×24 monochrome icon top-right; name centred at `+44`, 11px sans semibold; subtitle at `+56`, 8px mono muted.
- Regular node: white fill, stroke `ink @ 0.25`, width `1`. Focal node: fill `accent @ 0.08`, accent stroke `1.2`, accent title. Exactly one focal node, usually the storage hub.

## 202. High-Level — Right Strip (Vertical Chevrons)
- Reserve a 28px right strip at `x=972` only when at least one vertical concern exists. Never draw a vertical chevron over the cluster.
- The strip runs from `y=40` to the last cross-cutting row's bottom (min `428`), split evenly with floor-to-4 heights. The last absorbs the remainder, and neighbours share edges with no gap.
- Shapes run top to bottom: first is flat-topped and pointed at the bottom, middles are notched on top and pointed below, last is notched on top and flat at the bottom. Point and notch depth `12`.
- Labels: band-label colour, 7px mono, `0.14em`, rotated −90°, centred on the segment.
- Pairing is 1:1 and mandatory: each vertical chevron pairs with exactly one bar or cross-cutting row, and vice versa. Count of verticals = bars + cross-cutting rows. If any are unpaired the diagram is incomplete, so stop and ask.
- Order top-down: the bar-paired concern (Orchestration) first, then cross-cutting concerns in the order their rows appear. Vertical chevrons hold no nodes and emit no edges; they label a column of concern.

## 203. High-Level — Connector Styles
- Style comes from topology, never from preference:
  - `primary`: accent, `1.2`, solid, accent arrowhead. Required on every edge touching the focal node.
  - `secondary`: muted, `1.0`, solid. The default for non-focal edges.
  - `trigger`: muted, `1.0`, dashed `4,3`, small arrowhead. Required on every edge from a bar.
  - `query`: `ink @ 0.30`, `1.0`, dashed `4,3`. For read-back edges.
- Exactly four arrowheads. Standard `8×6` (refX 7). Small `6×5` (refX 5). Plus accent and dim (`ink @ 0.45`) variants.
- Exit and entry: source → cluster node and node → node leave the right edge and enter the left. Bar → node leaves the bottom of the bar and enters the top of the node.
- Orthogonal elbows, ≤2 bends, `8px` quadratic corners. Draw all connectors before any node. One end marker per path, never both ends.
- Label every primary and secondary edge in small mono on an opaque paper mask. Trigger and query edges stay unlabelled.
- Avoid crossings by rerouting through the chevron-divider trunk. If one is unavoidable, the later path takes a 6px hop.

## 204. High-Level — Fan-Out & Branching
- Source fan-out: trunk at `cluster_x − 8`. Path: right edge → H to trunk → V to target centre → H into the target's left.
- Component fan-out: trunk 4px past the source phase's chevron divider, same H–V–H pattern.
- At most 3 outgoing edges per node. A node fanning out to 4+ is secretly the hub, so make it explicit (usually the focal node).
- Bar drops are straight verticals from the bar bottom to each target's top at the target's centre x, in trigger style. Bar drops never bend.
- Several sources into one target: stagger the entry y evenly, `top + 8 + k·(h − 16)/(N − 1)`, so arrowheads don't pile up.

## 205. High-Level — Colour Overrides & Dark Mode
- A component colour override is a semantic flag, not decoration. Light: container fill `C @ 0.06`, stroke `C @ 0.35` (`1` for nodes, `0.8` for bars), badge stroke `C @ 0.40`, badge text `C @ 0.85`, icon and name in `C`. Subtitles stay muted. Connectors never change colour.
- Never on the focal node (accent wins) or on source nodes. Max 2 coloured components besides the focal node. If you want a coloured edge, pick a different connector style instead.
- Semantic palette: `#b85450` rust-red for security/identity; `#5a7d9a` slate-blue for observability; `#7a8c47` olive for governance/lineage; `#8c6d3f` warm brown for backup/DR. A random hex per component is exactly the failure to avoid.
- Dark mode: express everything as a role at an opacity so it inverts by itself. Differences: muted text → `ink @ 0.65`; dashed border `0.20 → 0.22`; node fill white → `ink @ 0.06`; node stroke `0.25 → 0.20`; focal fill `0.08 → 0.12`; band alternation moves one step lighter.
- The phase banner needs a dark band with a light label in both modes, so it uses fixed tokens that don't invert: `#2d3142`, `#3d4460`, `#4a5270` and label `#f5f5f5` (≥7:1 against every band). On a re-skin, derive three steps from the brand's darkest neutral and keep the label ≥4.5:1 against all three.
- Pitfalls: missing banner; node off its chevron centre; more than one focal node; solid external zone; solid bar edges; a source fanning out to >3 with no hub.

# Part 26 — Data Flow & Integration Diagrams

## 206. Data Flow — When & Grid
- Use to show how a data pipeline moves across organisational roles: who starts, processes, publishes and consumes, over 4–6 steps with typed payloads and role-scoped access. For a business process (approvals, tickets), use a swimlane.
- Lanes (1–4 roles) run top to bottom. Steps (1–6) are columns left to right. Over 4 lanes or 6 steps, split into two diagrams.
- Geometry: label column `140`, step slot `112`, right pad `28`, header `36`, lane `80`. Width = 140 + steps·112 + 28 (5 steps → `728`). Height = 36 + lanes·80 + legend, with legend `80`, or `100` when a colour row is present.
- Step centre = `140 + j·112 + 56`. Lane top = `36 + k·80`.
- Background: 22×22 dot grid (`r=0.8`, `ink @ 0.10`). Odd lanes tinted `ink @ 0.018`. Lane dividers and the label-column border are hairlines, `ink @ 0.12` `0.8`. Tint at most one lane by choice; tinting every lane is decoration.
- Lane label: two uppercase eyebrow lines, muted, at lane mid −4 and +8. Lane labels are identifiers, so never use the node-name face for them.
- Step header: a pill `32×16`, `rx=8`, at `y=6`, fill `ink @ 0.12`, number at `y=14`, muted label at `y=29`.

## 207. Data Flow — Node Anatomy & Chips
- Node `100×64` at (step centre − 50, lane top + 8). Empty cells render nothing: no placeholder box, chip or text.
- Inside: role chip `18×10` `rx=3` top-left (6px eyebrow, 600, lane key such as `ENG`); title at `+23`, node-name 9px; sub at `+35`, 6.5px muted; tool at `+47`, 6.5px soft.
- Node titles use the node-name role, never the page-title role.
- Data-type chips `16×8` `rx=3` at the bottom. Input is always bottom-left (`x+4, y+54`), output always bottom-right (`x+80, y+54`). Reading a row then traces the payload's transformation.
- Chip codes and colours: `WB` web `#6e6479`; `DB` dataset/raw `#5e7a9b`; `TB` table `#b8915a`; `FL` file/report `#9c6b50`; `LS` live stream `#4a7c59`. White 5px eyebrow text, weight 700. At most 2 chips per node, and a source or sink may omit one.
- Chip colour (payload format) and node colour (concern) are separate axes. Never conflate them.

## 208. Data Flow — Arrows & Focal Triad
- Four styles from topology:
  - `muted`: `1.0`, solid. A standard hand-off.
  - `trigger`: muted, dashed `4,3`, unlabelled. A governance action enabling downstream work.
  - `accent`: `1.2`. The focal cross-role hand-off, exactly one per diagram and labelled.
  - `link`: `1.0`. Published, externally consumed output.
- Arrowheads `6×6`, refX 5. Draw all arrows before node rects.
- Single bend only, horizontal first then vertical, with an `8px` quadratic corner and no diagonals. Leave from the right edge. Enter from the left in the same lane, or from the top or bottom across lanes.
- Only the accent arrow carries a label: a short payload phrase (`anon data`) on a paper mask with 6px padding. Every other arrow stays unlabelled.
- The focal triad has exactly one of each: a focal step (accent pill `accent @ 0.20`), a focal node (the one that receives the hand-off; accent border and role chip, ink title, fill `accent @ 0.07`), and the focal arrow into it. If any slot has zero or more than one, stop and ask.

## 209. Data Flow — Colour Overrides & Legend
- A node override in light mode: fill `C @ 0.06`, stroke `C @ 0.35`, role chip `C @ 0.18`, chip text and title in `C`. Sub, tool and data chips stay unchanged.
- A step override: pill `C @ 0.20` with text `C`. A lane override: tint `C @ 0.04` with the label in `C`.
- Dark mode uses `C` lightened about 15% (e.g. `#b85450 → #d97a78`).
- Never colour focal elements or arrows. Max 3 coloured elements in total across nodes, lanes and steps, besides the focal pair.
- Legend rows are horizontal strips introduced by a category label at `x=144`:
  - STEPS: the header pills, focal one in accent.
  - DATA TYPE: chips actually used, followed by the hint "left chip = input · right chip = output".
  - CONCERN: only when overrides exist; includes the accent swatch.
  - FLOW: one sample per arrow style used.
- Never stack the legend vertically inside a box.

## 210. DP Integration — When & Anatomy
- Use when the question is "what surfaces does this platform expose, and over what wire?". It is a hub-and-spoke integration topology wrapped in an explicit platform layer, with no phase axis. Phase chevrons belong to the high-level overview, not here.
- Anatomy: sources in a left column (0–6), a platform zone in the middle (rows of nodes and full-width bars), consumers in a right column (0–6), and footer bars below for layer-wide services.
- Canvas width `1200`. Columns: left at `x=40`, right at `x=1000`, both `160` wide. Rows start at `y=92` with stride `88` (node `64` + gap `24`). Column height = max(`336`, n·88 − 24).
- Side-column nodes `160×64`, fill `muted @ 0.06`, stroke `soft` `1`.
- Platform zone: `x=260, y=72, w=696`, same height as the columns. Zone label on a paper mask across the top border. Zone stroke `ink @ 0.32`.
- Footer bars: `52px` below the zone, height `56`, `8` gap, spanning `x=40` to `1160`. Canvas height = max(`600`, footer bottom + `84`).

## 211. DP Integration — Platform Rows
- Platform contents are an ordered stack of bars (full zone width minus `16` padding each side) and rows (N nodes spread evenly).
- Bar height `44`, or `56` when focal. Row height `72`, gap `16`.
- Anchor the first node row to side-column row 2 so its connectors stay straight: primary row top = `col_node_y(1) − 4` (≈`176`). Place bars above and below it with a cursor.
- Canonical stack: focal query bar `y=104 h=56`, node row `y=176 h=72`, scheduler bar `y=324 h=44`. The bottom bar deliberately lines up with side row 4.
- Even node spacing inside a row: width = (696 − 32 − (N−1)·16)/N. Fixed-width nodes centred on chosen columns also work if you note the deviation.
- Non-focal bar: fill `ink @ 0.05`, stroke `ink @ 0.32`. Focal: fill `accent @ 0.08`, stroke accent.

## 212. DP Integration — Connectors
- Five styles from topology:
  - `primary`: accent, `1.4`. Any edge touching a focal component, and every query-engine → consumer edge (the serve-flow rule).
  - `secondary`: muted, `1.2`. The default.
  - `federated`: link, `1.0`, dashed `4,3`. Federation queries from a source to the query engine.
  - `trigger`: muted, dashed `4,3`, unlabelled. Every edge from a bar.
  - `auth`: accent, `1.2`, dashed `5,4`. From a footer to the zone bottom edge only.
- Every primary, secondary, federated and auth edge carries a protocol label (`JDBC`, `SFTP`, `IMAP`, `ODBC`, `HTTPS`, `REST`, `AUTH`) at 8px on a paper mask with a 6–10px gap. Never draw one bus arrow from "sources" to "the platform".
- Routing: ≤2 bends, `r=8` corners, one end marker, never a start marker. Draw all connectors before rects.
- Fan-out: when one node feeds N targets on one side, stagger the exit y by 8px per edge (e.g. `124, 132, 140, 148`) and stagger the vertical runs in the corridor too.
- Avoid crossings by rerouting through the corridors. If one is unavoidable, the later path takes a 6px hop.

## 213. DP Integration — Focal Pair & Layer-Wide Services
- Exactly two focal components: the storage hub and the federation/query engine. These two are what make it a platform rather than a pile of tools. Everything else stays ink or muted.
- Identity, policy, secrets, logging, observability, audit and mTLS root authenticate or serve every component. Connect each to the bottom edge of the platform zone with one AUTH line, never to a specific tool. Wiring identity to one component understates its scope.
- One footer: the line runs at the zone centre x. Several footers: offset each line by `32px` around the centre so stacked footers don't overlap. AUTH labels sit just above the arrowhead.
- Footers and identity sit outside the zone because identity gates the layer from outside.
- Colour overrides mirror the high-level ones (fill `0.06`, stroke `0.35`, badge `0.40/0.85`). Max 2 besides the focal pair. Never on focal components or connectors. Per-tool rainbow colours inside the zone are banned.
- Density: this type intentionally goes over the usual 9-node budget (14–20 nodes: 4–6 sources, ~5 platform, 4–6 consumers, 1–3 footers). The count of integration surfaces is the claim. Merge identical sources (`4 × MariaDB`) or split by plane when it gets unwieldy, but never collapse ≥3 distinct sources into one node.

# Part 27 — Storage Tiers & Access Grids

## 214. Medallion — When & Canvas
- Use for a multi-tier storage layout where each tier is a quality or access level of the same dataset (raw → anonymised → staging → aggregated → archive). It shows what each bucket holds, who writes it, with what tool and format, and how data is promoted.
- Use a process diagram instead for role-lane workflows, and the high-level overview for cluster architecture.
- 3–6 tier columns. Tier `172×380`, gap `16`, left pad `16`, right pad `100`. Width = 16 + n·172 + (n−1)·16 + 100 (5 tiers → `1040`).
- An `80px` arc band above the tiers holds the promotion arcs. Tier top `y=80`. Height = 80 + 380 + (72 if path cards) + 16 → `548` / `476`.
- Background is plain paper, no dot grid.

## 215. Medallion — Tier Card Anatomy
- Card `rx=6`. A tinted header band `40px` tall plus a 10px extension in the same tint.
- Tier title at `y=106`, node-name 13px weight 700, ink. Bucket name at `y=144`, sublabel, muted (accent on the focal tier).
- Four fields with a 16px inset and 140px text width. Field labels (node-name 11px, ink) at `180/220/260`: Tool, Format, Writer. Then an example section at `360`, with lines at `374/388`.
- Field values wrap to 2 lines inside a 140×24 box at 1.25 line-height. The 26px gap to the next label absorbs the second line.
- Every tier shows a concrete example payload (survey rows, claims, customer records). Without it the diagram turns abstract.
- Tier styles:
  - `outer` (raw): white fill, `muted` 1.0 stroke, band `muted @ 0.10`.
  - `default`: white fill, `ink` 1.0 stroke, band `ink @ 0.06`.
  - `focal`: fill `accent @ 0.07`, accent `1.6` stroke, band `accent @ 0.14`.
  - `cold` (archive only): `paper-2` fill, `muted` stroke dashed `5,3`, band `muted @ 0.18`.
- On the focal tier only the bucket name and example lines turn accent. Tool, format and writer stay muted so the card doesn't drown in accent.

## 216. Medallion — Promotion Arcs
- Promotions always run left → right between adjacent tiers as cubic arcs over the top, anchored at the tiers' top centres: `M cx_i,80 C cx_i,0 cx_j,0 cx_j,80`. The peak lands at `y≈20`, and the arrowhead plunges straight down into the next header band.
- Consecutive arcs share their anchor points, so each tier top reads as a joint: data arrives, transforms and leaves.
- Styles: `normal` muted `1.4`; `focal` accent `1.6` (automatic for the arc into the focal tier); `lifecycle` muted `1.4` dashed `4,3` (usually into the archive).
- The arc into a colour-overridden tier takes that colour (stroke, label and a matching arrowhead) at width `1.4`. The arc out of it reverts. Focal beats colour.
- Labels sit inside the arc at (midpoint, `y=50`): uppercase arrow-label face, 10px, `0.08em`, coloured like the stroke. They need no mask because the curve peaks well above them. Keep labels ≤14 characters (`PII REMOVE`, `AGGREGATE`, `LIFECYCLE`).
- Never draw horizontal lines through the tier gaps, bidirectional promotions or backflow.

## 217. Medallion — Path Cards, Colour & Focal
- Optional 0–2 write-method cards below the tiers: `y=476`, height `56`, each `460` wide in the 5-tier layout. White fill, stroke `ink @ 0.20` `1`, `rx=6`. Tag chip `h=12 rx=2` with stroke `ink @ 0.30`. Title at `+30` (11px), sub at `+46` muted.
- Path cards describe how data moves (a SQL path versus a notebook path), never what a tier holds.
- Tier colour override: fill `C @ 0.07`, stroke `C` at `1.4`, band `C @ 0.14`. Bucket and examples in `C`; the title stays ink. Never on the focal tier. Never combine a custom colour with the cold dashed style. Max 2 besides the focal tier.
- Palette additions: warm yellow `#c9a23a` for analytical or working zones; olive `#7a8c47` for data products or publication.
- Exactly one focal tier, defaulting to the tier consumers query (usually Aggregated). Its incoming arc turns accent; its outgoing arc keeps the declared style.

## 218. Security Matrix — When & Grid
- Use to audit who can do what: rows are platform components, columns are roles or directory groups, and each cell holds a permission. Use an integration diagram instead when the question is who can talk to what. The matrix shows what each role can do, not how access is granted.
- 2–6 role columns and 2–14 component rows. Over that, split (human roles vs service accounts; storage vs compute vs observability).
- Geometry: left pad `12`, component column `208`, gap `12`, role column `148`, role gap `16`, right pad `48`. 4 roles → width `920`.
- Header `y=72 h=52`. Rows start at `y=140`, height `36`, stride `40`. Legend 20px below the last row. Height = legend top + `44` (8 rows → `520`).
- Plain paper background. No connectors at all; the information lives entirely in the cells.

## 219. Security Matrix — Headers, Rows & Cells
- Component header cell: white, stroke `ink @ 0.12` `0.8`, `rx=6`, two lines: "Component" (11px) and "vs. AD group" (muted sublabel).
- Role banners: solid `ink` fill, `rx=6`. Role name in white at 11px (`y=92`), group code in white at 0.85 opacity (`y=108`).
- Component label cell: white, `rx=4`, name left-aligned 12px in from the edge, optional hint (`SSO`, `S3 API`) right-aligned and muted.
- Value cells: `rx=4`, stroke `ink @ 0.12` `0.6`, value centred at 10px, baseline at row + 22.
- Closed level vocabulary drives the styling; the displayed text is free (`Admin`, `R/W`, `SELECT`, `Login`):
  - `full`: `ink @ 0.08` fill, ink text, weight 600.
  - `rw`: white fill, ink text, 400.
  - `read`: `muted @ 0.08` fill, muted text.
  - `none`: paper fill, soft text, default "No access".
- `none` means no access, never TBD. Do not render an unknown permission as "No access".
- Legend: hairline separator, a muted "LEGEND" eyebrow, then `14×12` `rx=2` swatches for the levels actually used, about 120px apart, on one line.

## 220. Security Matrix — Focal & Colour
- Zero or one focal cell: the single access rule that sets this platform's posture apart (e.g. consumers may only `SELECT` from the aggregated catalogue). Fill `accent @ 0.07`, accent stroke `1.4`, accent text 600. Value at row + 18, plus an optional second line at row + 30 (8px, 0.85 opacity).
- Per-cell colour: fill `C @ 0.08`, stroke `C @ 0.45` `1.0`, text in `C`.
- Per-row colour tints the label cell only. Per-role colour recolours the banner only, with white text if the colour is dark, otherwise ink. Overrides never spread into the matrix body.
- Keep total coloured entities ≤5, and coloured cells ≤2 besides the focal cell. Avoid whole-row or whole-column tints: they turn the matrix into a list.
- Palette meanings here: rust-red for elevated or break-glass access, slate for quality gates, olive for approved, yellow for sandbox, brown for archive.

# Part 28 — Spatial & Exploded Views

## 221. Exploded Axonometric — When to Use
- Use for one object or system in parallel projection with its parts pulled apart along one axis and labelled: device teardowns, unboxing, assembly order, or a stack the reader should see as physical parts of one thing.
- Not for: ordered abstraction levels with notes (layer stack); if nothing has a footprint or thickness, use the stack. Not for connections (architecture), since an exploded view has no arrows and position on the axis is the only relationship. Not for unordered containment (nested) or for where software runs (deployment).
- Show 2–5 parts, listed bottom to top.

## 222. Exploded Axonometric — Projection
- Use a 2:1 dimetric projection: ground axes at `26.565°`, so edges land on whole pixels when model units are multiples of 4.
- Project every point through one function: `screen = (ox + x − y, oy + (x + y)/2 − z)`. Never place a coordinate by hand.
- A rounded-rectangle footprint of radius `r` projects to straight edges joined by elliptical quarter arcs with `rx = r·√2`, `ry = r/√2`. `r=0` gives a slab, small `r` a product corner, `r = w/2 = d/2` a cylinder.
- Insetting an outline keeps the corner centres fixed and shrinks the radius.
- Draw faces as plain paths and polygons with the projected points. No CSS 3D, canvas, WebGL or transforms for geometry. Labels always stay horizontal.

## 223. Exploded Axonometric — Parts, Levels & Gap
- Each part is a rounded prism plus at most two levels of detail on its top face, the face the reader sees.
- Explode vertically: parts move straight up, nothing rotates, and the bottom part stays at `z=0`. Never explode along two axes or slide parts sideways.
- Parts that sit side by side in the assembled object (a board next to a battery) share a level and lift together.
- One gap between every pair of levels: `max(k × top-face height, 3 × thickest solid part)`, rounded up to a multiple of 4. Top-face height = `(w + d)/2` of the largest footprint. `k = 0.5` is the floor; use `0.75` when a tall part would hide the focal part. Containers don't count toward thickness.
- Clearance: if a leader would cross a part, or two labels come within `36px`, raise the gap in steps of 4. Fix collisions within one level by moving a part in plan.
- Never use unequal gaps or shrink the gap to fit the canvas. Raise `k` or cut a part.

## 224. Exploded Axonometric — Paint Order & Frame
- Paint the bottom level first. Within a level, paint parts farther back (smaller `x + y`) first.
- Split containers: the back half (silhouette, rim, cavity, floor) paints before the parts inside, and the outer walls and front rim paint after. This keeps a tray correct both assembled and exploded.
- Trace lines run straight up through the left and right extremes of the bottom part's outline to the underside of the top part, and paint before every part.
- Canvas `1000` wide. The object and a `240px` label column are centred together. Height follows the exploded object plus a `40px` top margin.

## 225. Exploded Axonometric — Face Shading
- Light comes from the top left, so the left face is lighter than the right. Always shade: an outline-only box flips like a Necker cube.
- Every face is an opaque base plus an ink overlay, never a translucent fill alone, so hidden parts never show through.
- Light mode: base `#ffffff`; top = base; left = base + `ink @ 0.07`; right = base + `ink @ 0.15`.
- Dark mode: base `paper-2`; top + `ink @ 0.10`; left = base; right + `paper @ 0.45`.
- Focal part, light: accent at `0.10 / 0.20 / 0.32` (top/left/right). Dark: accent `0.18` top with neutral sides.
- Lines: silhouette ink `1.2`; inner edges ink at `0.55`, `0.8` (dark `0.45`); detail lines ink `0.55` at `0.6–0.8`; trace lines ink `0.30`, `0.8`, dashed `4,3`.
- No contact shadows, gradients on solid faces or glow.

## 226. Exploded Axonometric — Labels & Detail
- One label per part, all in one column to the right: the part name (600, 16px, one or two words) above a technical sublabel (10px, muted, `0.08em` tracking).
- Leader: horizontal, `0.8px`, ink `0.40`, starting 6px right of a 2px dot on the part's right extreme at mid-thickness and ending 12px short of the column. Leaders never bend, cross a part or cross each other.
- The focal part's dot, leader and sublabel take the accent; its name stays ink. At most one focal part. Never fade other parts with opacity, because translucency exposes the edges behind.
- No numbered callouts, no legend, no labels on or angled with the faces, no second label column.
- Detail has three levels at most: the form, insets on the top face (screen, cell outline, well), and micro detail (chips, lenses, a logo). Keep insets ≥4 units inside the face edge and clipped to the face.
- For many identical pieces (keycaps, switches), draw one small prism per piece inside the grid envelope.

## 227. Exploded Axonometric — Motion
- Optionally open on the assembled object and explode once, which shows how the parts fit.
- The top level lifts first. Each part moves straight up by (exploded z − assembled z). The bottom level stays put, and its label and the trace lines arrive last.
- Hide labels instantly on the closed frame and fade each in after its part settles, otherwise labels pile up on the closed object.
- Static, no-script, reduced-motion, print and export states all show the exploded frame. The lift is the one exception to the usual 24px movement limit; nothing else moves.

## 228. Axonometric Plan — When to Use
- Use for one floor or site seen from above at an angle, with what stands on it: an office floor with rooms and furniture, a campus, a warehouse, a store. Use it when the reader needs rooms or buildings in relation to each other in one view.
- Not for: parts pulled apart (exploded; a plan has one plate and nothing explodes); containment without geography (nested); software placement (deployment); a list of rooms and capacities (table).
- Use the same 2:1 dimetric projection function and face shading as the exploded view. Every element is a rounded prism on the plate.

## 229. Axonometric Plan — Plate, Walls & Objects
- Plate: one floor slab `6` units thick, or a site `8` units with a small corner radius. Nothing extends past its edge.
- Walls `6` units thick, cut at desk height (`~22` units) so no wall hides a room. Doors are gaps. At a junction, run one wall through and stop the other at its face; never overlap them.
- Furniture and buildings are shaded boxes, with heights to scale with each other. No two footprints ever overlap.
- Roads, paths and floor tints are flat fills on the plate (`ink @ 0.07`) with no thickness. A road may have a dashed centre line, `ink @ 0.25`, `6,5`.
- Racks: tall boxes with a shelf line every `14` units and an upright every `30`. Run rack rows along x so the lit face and the aisles show.
- Trees: a canopy cylinder `8` units up on a short trunk, canopy top `rule-solid` (light) or `soft` (dark). Keep them small and off every footprint.
- Canvas `1000` wide with the plate centred. Height follows the plate plus its tallest box plus a `48px` top margin.

## 230. Axonometric Plan — Paint Order, Tags & Focal
- Paint the plate, then flat marks, then boxes back to front in topological order: A paints before B when A lies entirely behind B (`A.x1 ≤ B.x0` or `A.y1 ≤ B.y0`) and their outlines overlap. A plain `x + y` sort fails on long walls.
- Tags stay horizontal: name (600, 12px) over a sublabel (8px), on an opaque paper backing with a hairline rule, `32px` tall, width rounded up to a multiple of 4.
- A room's tag sits on open floor inside the room; a building's tag sits on its roof. Tags paint after every box so walls never cut them.
- Tags never overlap. Move a tag before shortening its name. Use one or two words, no leaders and no numbered key. Never tilt tags onto the floor plane.
- One room or building takes the accent: a focal room gets an accent floor tint and an accent tag, a focal building gets the accent face ramp and tag. Furniture inside a focal room stays neutral.
- Optional motion: reveal phased buildings or zones step by step (≤2 items per step), each dropping 16px and fading in. Walls and unphased rooms stay static.

# Part 29 — Service & State Maps

## 231. Service Blueprint — When to Use
- Use to show how a service runs across a few stages: what the customer does, what they see, and what stays hidden. The line of visibility carries the figure. Use it when the reader must see that a failure is a billing job, a queue or a fraud check even though the customer row looks like a simple retry.
- Not for: sentiment with no backstage (journey); hand-offs as arrows between owners (swimlane); a state census (kanban); scope slices (story map); bands with no stage columns (layer stack).
- If you cannot name a frontstage/backstage split, it is not a blueprint.

## 232. Service Blueprint — Grid & Layers
- Stages are equal columns, left → right in narrative order. Layers are labelled rows, top → bottom. No connector arrows: stage order is the sequence.
- Canvas `1280×720`. Left margin `96` for layer labels: 8px mono uppercase, horizontal, right-aligned at `x=88`. Never set layer labels vertically.
- Use 4–6 stages, e.g. 5 × `208px` with `16px` gutters (column x = `96 + i·224`). Every cell in a column shares its header's x.
- Layer order:
  1. Physical evidence (optional, `48`).
  2. Customer actions (`64`).
  3. Line of interaction.
  4. Frontstage (`64`).
  5. Line of visibility.
  6. Backstage (`64`).
  7. Line of internal interaction.
  8. Support (optional, `48`).
- Hairlines take an 8px band. Interaction and internal-interaction lines are `1px` rule. The visibility line is heavier: `2px` ink at `0.55`, which must clear 3:1 on paper (`0.45` fails on light paper). It spans the plot in the frontstage/backstage gap.

## 233. Service Blueprint — Cells, Focal & Honesty
- One action per stage per layer, 12px, one line, centred. An optional second muted mono line names a system or wait (`dunning-job · 4h`). Never more than two lines.
- Customer and frontstage cells: paper/white with ink stroke, `rx=4`. Backstage and support cells take a light ink tint so the band below the line reads as hidden work.
- Required layers are complete: every stage has customer, frontstage and backstage cells. An empty slot still takes its column and prints `—` or "Not applicable".
- At most one focal cell: the failure, wait or hand-off the figure exists for, usually on or below the line. Fill `rgba(191,69,32,0.12)` (dark `rgba(240,138,89,0.18)`), accent stroke, accent 600 text. Never put accent on every failing cell.
- Legend strip after a hairline, three keys in order: visibility line, backstage layer, focal cell.
- Pitfalls: no visibility line, or one in the wrong gap; a sentiment curve (that's a journey); arrows across layers (that's a swimlane); more than 6 stages.

## 234. IT Current-State — When & Zones
- Use for the "before" picture of a modernisation proposal: the legacy landscape grouped by phase or department, with pain points flagged, file hand-offs labelled (CSV / Excel / Email / Copy) and pre-platform tooling visible. It is the companion to the integration topology, showing the gap the proposal closes.
- 2–4 zones in one orientation, horizontal (zones left → right, components stacked) or vertical. Never mix orientations.
- Zone: `y=52`, height `360`, gap `20`, pads `16`. Fill `ink @ 0.02`, stroke `ink @ 0.10` `0.8`, `rx=8`.
- Zone label: uppercase eyebrow ≤14 characters, `soft`, `0.14em`, on a paper break in the top border at `x+20`.
- Zone width ≈ `200 + 24` per component, e.g. `256 / 360 / 272` gives `960` across 3 zones.
- 1–5 components per zone, ≤16 in total. Over that, split.
- Canvas height = content bottom + `40` legend + `24` (`500` with no footer).

## 235. IT Current-State — Components
- Component: inset `20`, height `56` (`68` focal with a two-line sub, `72` with two sub lines), gap `32`, first at zone top + 28.
- 24×24 monochrome catalogue icon at left + 12, vertically centred. Name at `x+44`. Sub (10px muted) 14px under the name's baseline. Use real icons, never tiny text badges like `DB` or `APP` as icons.
- Kinds:
  - Standard: white fill, ink stroke `1`.
  - Focal: fill `accent @ 0.07`, accent `1.4` stroke, sub line 1 in accent.
  - External: white fill, muted stroke dashed `4,3`, meaning outside our scope.
- ≤2 focal components, the narrative pain points or bottlenecks. Zero is fine. More than 2 means two stories, so split. For "bad but not headline-bad", use rust-red `#b85450` instead.
- Colour override: fill `C @ 0.06`, stroke `C @ 0.45`, name in `C`. Icon and sub unchanged. ≤3 per diagram, never on focal. Olive `#7a8c47` can mark the surviving system the new platform keeps.
- Footer bars (≤3) for layer-wide services: full width, height `56`, fill `ink @ 0.03`, stroke `ink @ 0.18`, `rx=8`, name 14px and sub 12px. No connectors come out of them.

## 236. IT Current-State — Connectors & Marker Visibility
- Use rounded right-angle quadratic bends at `r=8`, never diagonals. In the same zone, adjacent components join with a straight vertical. Across zones: exit right → H → bend → V into the top (destination below) or bottom (destination above).
- Styles: neutral muted `1.0`; link `1.2`; accent `1.4`. Dashed `4 3` when flagged. Any edge touching a focal component turns accent automatically.
- A backward (right → left or upward) reference is allowed only when an endpoint is external, and it must be dashed.
- The arrowhead must touch the destination edge, never stop short or end at the centroid.
- Marker visibility: with an `8`-wide marker at refX `7`, the head's body extends 7px back along the path. Approach so the body stays outside the box: down into a top edge, right into a left edge, left into a right edge, up into a bottom edge. Going up into a top edge or down into a bottom edge leaves only 1px visible.
- When the source row overlaps the destination's y range, prefer a straight side-edge entry. When it's offset, detour through the nearest zone background to reach a side edge, or go over the box and come down into its top.
- Fan several entries on one edge at ≥12px (e.g. 16px spacing: `108 / 124 / 140`).

## 237. IT Current-State — Connector Labels & Legend
- Labels are uppercase, ≤8 characters, 9px, 600, `0.08em`, coloured like the stroke, with an optional 12px icon to the left inside the mask.
- Place the label near the source end, offset perpendicular to the line, never mid-segment on the stroke:
  - Right exit: centre at `src_right + 6 + w/2`, `src_cy − 14`.
  - Bottom exit: `src_cx + 6 + w/2`, `src_bot + 14`.
  - On H-then-V routes, bind it to the early horizontal run.
- Mask: `18px` tall, `rx=3`, paper fill (ink in dark mode), width = text + 12 (or + 30 with an icon). Draw it after its line.
- Legend: hairline at content bottom + 16, swatches at + 36, only for styles and kinds actually used (data flow, pain point, external, bottleneck).

# Part 30 — Hierarchy & Containment

## 238. Layer Stack — Anatomy
- Use for ordered abstraction levels: OSI, CSS cascade, context hierarchy, tech stacks, memory hierarchy. Layers must actually be hierarchical; otherwise use a swimlane or architecture.
- Full-width horizontal bands stacked vertically, all with the same x and width. 4–6 layers, `56–72px` high, `800–880px` wide in a `1000px` canvas (e.g. `840 × 64`).
- Each row, left → right:
  - Index tag (`L3`, `07`, `APPLICATION`), 8–9px eyebrow, tracking `0.14em`.
  - Layer name, 14–16px, 600, just right of centre-left.
  - Note at the far right, 9–10px muted, right-aligned, `0.08em`.
- Dividers: 1px hairline `ink @ 0.12`. Outer silhouette 1px ink or muted.

## 239. Layer Stack — Styling & Pitfalls
- Fills: alternate subtle shades (paper / paper-2, e.g. white / `#f5f5f5` / `#ececec`), or all paper with hairlines. Pick one and hold it.
- A direction indicator sits in the left margin outside the stack: a thin vertical rule (`ink @ 0.30`) with an arrow and eyebrow label (`abstraction ↑`, `packets ↓`).
- Exactly one focal layer (bottleneck, the layer under discussion): accent stroke plus tint fill `accent @ 0.08`, with its tag and note in accent.
- Pitfalls: skipped numbering without explanation; every layer a different colour so the hierarchy disappears; uneven heights for no reason.

## 240. Nested Containment
- Use for hierarchy through containment: scope boundaries, trust zones, folder nesting, blast radius. Outer = broader, inner = more specific.
- 3–5 rounded rects, `rx=8`, with consistent insets: `24–32px` horizontal and `32–36px` vertical (e.g. 32px steps each way). Irregular padding looks accidental.
- Each level labelled top-left in 7–8px eyebrow, `0.14em`, on a paper mask (16px tall) over the ring's top border.
- Strokes step from faint outside to strong inside: `ink @ 0.30 → 0.35 → 0.45 →` muted → accent at the innermost focal.
- Fills step up inward: `0.015 → 0.02 → 0.025 → 0.03 →` accent tint (`accent @ 0.06`) on the innermost. The innermost label turns accent, 600.
- Optional folded-corner file glyph per level (20×20, 4px fold) hints at contents. 1–2 italic callout asides at most.
- Pitfalls: more than 6 levels (information vanishes inward); content inside rings that isn't part of the hierarchy; accent on more than one level.

## 241. Tree — Layout
- Use for org charts, taxonomies, file trees, decision breakdowns, skill trees, and dependency trees with a single parent everywhere.
- Root at the top with children fanning out below, or root at the left fanning right.
- Nodes `rx=6`, `120–180px` wide, `40–52px` tall (e.g. `160×48`). Name 12px 600 with an optional 9px sublabel and a small `rx=2` type tag top-left. Use two node widths at most.
- Max depth 4 (root + 3 tiers). Max breadth 5 per level. Deeper trees go on separate pages.
- Exactly one accent node: the root or one critical leaf, never both. Focal fill `accent @ 0.08`.
- Optional tier labels in the left margin: 8px mono, tracked `0.18em`.

## 242. Tree — Connectors
- Orthogonal bus connectors only. The parent drops a short vertical, a horizontal bus spans the siblings, and each child gets a short vertical drop into its top edge. Never diagonal.
- Stroke 1px muted. E.g. parent bottom → bus 40px below → children 40px below the bus.
- Draw connectors before nodes.
- Leaves can be marked with a thinner `0.8` stroke or a different fill, or simply left to their terminal position.
- Never skip a level (a parent wired straight to a grandchild).

# Part 31 — Data Models & Schemas

## 243. ER / Data Model
- Use for conceptual and logical models, API resource relationships and domain models, where the story is entities and cardinality. For physical tables with SQL types and column-to-column foreign keys, use a database schema.
- Entity box in two sections. Header: an `ENTITY` type tag plus the name in the node-name face, on a faint tint (`ink @ 0.04`) separated by a hairline (`ink @ 0.22`). Body: fields one per line in the sublabel face; primary keys prefixed `#`, foreign keys prefixed `→`. Use natural height by content; never pad boxes to equal heights.
- Relationship lines join boxes, with cardinality at each end (`1`, `N`, `0..1`, `1..*`) in 8–10px mono, 10–12px from the entity edge, on a small paper mask. Use consistent notation at both ends.
- An optional verb label ("has", "belongs to") sits centred on the line on a mask.
- Lay out so most relationships are straight. Group related entities by cluster rather than drawing an arrow for every foreign key.
- The aggregate root or central entity takes the accent.

## 244. Database Schema — Table Box
- Use for the physical schema: real tables, SQL types, constraints, indexes and column-to-column foreign keys. Use it when deletion behaviour or a column type is the point; use ER when discussing what an entity is.
- Header band: `schema.table` (`public.orders`), 12px 600, with a rectangular `TABLE` tag (`rx=2`, not a pill), separated by a hairline.
- Column rows are a fixed `24px` so connectors anchor predictably. Column name 12px left, SQL type 9px muted right (`uuid`, `numeric(12,2)`, `timestamptz`), constraint chips between them (`PK`, `FK`, `UQ`, `NN`; `rx=2`, 8px eyebrow). Even rows tinted `ink @ 0.02`.
- Overflow: the last row reads `+ N more columns` in 9px muted. Never truncate silently.
- Optional INDEXES compartment after a hairline: 8px eyebrow heading, then the index names that matter to the story at 9px.
- Missing SQL types are a defect, since the type is half the content. Don't put constraint chips on every row until they become noise.

## 245. Database Schema — Foreign Keys, Grouping & Focal
- Each FK runs from the vertical centre of its source column row to the vertical centre of the referenced column row, never box to box (that's ER). Use rounded orthogonal elbows with hops at crossings.
- Label each FK with its referential action at 8px (`ON DELETE CASCADE`, `RESTRICT`, `SET NULL`) on a mask with a 6–10px gap. An unlabelled FK hides what a reviewer is looking for.
- FKs on different rows are fanned by the 24px row pitch. When two land on the same row and edge, offset them `±8px` around the row centre, inside the band and ≥12px apart.
- Tables in a non-default schema sit in a group rect: `rx=8`, `ink @ 0.02` fill, `ink @ 0.20` stroke dashed `4,4`, with an 8px uppercase schema eyebrow top-left. Draw it first.
- Focal: the one destructive FK (edge and label count as one) plus the table it cascades into, which gets accent tint on its header band only. With no destructive FK, accent nothing; never promote an arbitrary table.
- Budget: ≤5 tables, ≤8 rows per table, ≤6 FKs, 2 accent elements. Over that, show a subsystem and say so in a caption. Never mix conceptual entity names with physical table names.

## 246. UML Class — Compartments
- Use only when operations or the inheritance/composition vocabulary are the point. With no inheritance and no operations, use ER.
- Other UML diagrams have their own homes: sequence → sequence diagram; state machine → state diagram; component and deployment → architecture; activity → swimlane or flowchart.
- One box per class (`rx=6`) split by full-width hairlines into up to three compartments, with heights following content.
- Name compartment: centred, 12px 600. Interfaces get an 8px `«interface»` line above the name. Abstract classes set the name in italic. Use guillemets only where needed.
- Attributes: 9px, left-aligned, one combined string per line (`+ name: Type`); visibility `+` public, `-` private, `#` protected.
- Operations: `+ method(arg): Return`. Leave out empty compartments. Never list getters and setters.
- ≤5 members per compartment; overflow becomes a `…` line.
- Accent goes on the focal class (the one being implemented or extended), with accent-tint fill and accent stroke. Its inbound inheritance/realisation edges count together as the second accent element.

## 247. UML Class — Relationship Vocabulary
- Inheritance: solid line, large hollow triangle at the parent (paper fill, ink stroke).
- Realisation: dashed `5,4`, the same hollow triangle.
- Composition (the part dies with the whole): solid, filled ink diamond at the owner end.
- Aggregation (the part lives independently): solid, hollow diamond at the owner end. Never use composition and aggregation interchangeably.
- Association: solid with a plain open arrowhead, multiplicity at both ends.
- Dependency (uses): dashed `4,3`, plain open arrowhead.
- Multiplicities (`1`, `0..*`, `1..*`) at 8px, 10–12px off the box edge, on an opaque mask.
- The legend shows all six relationships even when the body uses fewer; it is the complete grammar reference.
- Connectors: orthogonal `r=8` elbows, hops, fanned attach points ≥12px apart, masked labels, drawn before boxes. Prefer layouts where edges are straight or single-elbow. Every edge needing a hop means you're over budget.
- Budget: ≤7 classes (4–5 is normal), ≤8 relationships, 2 accent elements. Over that, split by package.

# Part 32 — Org Structures

## 248. Org Chart — Layout
- Use for human teams, agent teams, escalation maps, role ownership and routing, where the reader needs who owns what. Use a tree when the nodes are generic. Use a swimlane when the question is process; for "who does what?", use an org chart.
- The root owner or front door sits top centre as the single accent node: the person, team or agent that receives ambiguous work. Fill `accent @ 0.08`.
- Tier 1 (departments, pods, queues) sits horizontally aligned. Tier 2 (owners, specialists): over 8 specialists, group them under pod nodes.
- Orthogonal bus connectors: vertical drop → horizontal bus → vertical drops, 1px muted, no diagonals. E.g. a 200×48 root, 160×48 nodes, tiers about 150px apart, tier eyebrows (9px mono) in the left margin with hairline tier separators.
- Each node answers three things: name (node-name), how to invoke it (handle, queue, issue prefix, trigger; sublabel), and scope (2–4 terse words, never a job description).

## 249. Org Chart — Treatments & Budget
- Front door: focal (accent tint + accent stroke). Team/pod/department: white + ink. Individual agent or owner: store or external treatment, depending on whether it is live. Gap or needs-setup: dashed optional styling, never hidden. Approval gate: security treatment, separate from the reporting line.
- Show not-yet-live or unwired owners dashed rather than as normal owners. Missing routes are operationally important.
- Put escalation and approval rules in a small side callout or footer strip, never as extra org nodes. Keep the legend in the bottom strip, not floating in the chart.
- Budget: ≤12 visible nodes (otherwise an overview chart plus detail charts per pod), ≤4 tiers, ≤5 direct reports per parent (add grouping nodes beyond that), 1 accent node, ≤2 side callouts.
- Pitfalls: identical boxes for everyone, which hides the front door, specialists and gaps; full job descriptions in nodes; repeating handles in body text when the sublabel already carries them.

# Part 33 — Process & Flow

## 250. Process map — when to use and the parametric grid
- Use for sequential business processes with several actors where the reader must see who does what, what data enters and leaves each step, and which tools are used. If payloads and tools don't matter, use a simple swimlane. If the point is onstage vs offstage work, use a service blueprint.
- The grid is lanes (rows, 1–6 actors, top to bottom) × steps (columns, 1–12, left to right). Treat it as parametric: the same inputs must always produce identical geometry.
- Canvas: label column 140 px wide; step slot 112 px (100 px node + 12 px corridor); right pad 28. Width = 140 + n_steps × 112 + 28 (11 steps → 1400). Header strip 36 px; lane height 80; legend 80 px (100 px when a concern-color row is needed). Height = 36 + n_lanes × 80 + legend.
- Lane top = 36 + k·80; lane middle = lane top + 40. Step center = 140 + 8 + j·112 + 50 (198, 310, 422 …), which includes an 8 px gutter inside the content area.
- Node = 100×64 at (step_cx − 50, lane_top + 8), leaving an 8 px margin above and below inside the lane.
- Background: paper, then a 22×22 dot grid (r 0.8, ink @ 0.10, layer opacity 0.55). Alternate lanes get an ink @ 0.018 tint from x=140 rightward. Lane dividers are ink @ 0.12, 0.8 px hairlines. The label-column border is ink @ 0.20, 1 px.
- Step header: a numbered pill (16×16, rx 8, or 20 wide for two-digit numbers) at y=8, filled ink @ 0.12. The label sits below it at y=32 in uppercase mono, 6 px, weight 500, tracked 0.12em, muted. Keep step labels to 9 characters or fewer and abbreviate rather than wrap.
- Lane labels: uppercase mono, 8 px, tracked 0.08em, muted, centered in the label column. Use one or two lines (±4 px around the lane middle).
- Budget: 6 lanes, 12 steps. Above that, split into an overview plus a detail diagram.

## 251. Process map — node anatomy and data-type chips
- Node contents, top to bottom:
  - a 14×10 role chip (rx 2) at the top-left, showing the lane's 3-letter actor key, 6 px weight 600. Use the lane key, never the step number, so an excerpted node still says who does it.
  - a title at +26, 9 px sans semibold.
  - an "input → output" line at +40, 6.5 px mono muted.
  - a tool line at +52, 6.5 px mono soft.
  - two 16×8 data chips (rx 2) at +54: input at bottom-left (x+4), output at bottom-right (x+80).
- Default node: white fill, ink @ 0.25 stroke. In dark mode use ink @ 0.04 fill and ink @ 0.20 stroke.
- An empty cell renders nothing: no placeholder box, no badge, no text.
- Drop the input chip on first-step nodes and the output chip on last-step nodes.
- If a title needs two lines, either grow the node to 72 px or omit the chips. The default is to omit the chips.
- Chip codes form their own semantic axis for payload format:
  - LS sage #7c8f6f (list/task)
  - DB dusty-blue #5e7a9b (dataset)
  - TB mustard #b8915a (analysis table)
  - FL rust-brown #9c6b50 (file/report)
  - WB slate #6e6479 (public/web release)
  - Chip text is white mono, 5 px, weight 700. Omit the chip when the payload is unknown.
- A node may carry both a payload chip color and a concern color. They describe different things.

## 252. Process map — connectors, focal slots, and color overrides
- There are three connector styles, and topology decides which one applies:
  - normal: muted, 1.0, filled arrow
  - focal-in/out: accent, 1.2, accent arrow, on every edge touching the focal node
  - trigger: muted, 1.0, dashed 4,3, small arrow (6×5), for orchestration and scheduler edges
- Routing is a single right-angle bend. Exit from the node's right edge at the lane middle, run to a corridor 8 px before the destination center, and turn with an 8 px quadratic curve. Enter the top when the destination is lower and the bottom when it is higher. Same-lane neighbours use a straight horizontal line.
- Never draw diagonals, enter from the left, or exit from a node's top or bottom. Draw every connector before any node rectangle. Use exactly one end marker and never a start marker.
- Process arrows carry no labels. The step number and the lane already say what's happening. Label only a non-step concept such as a re-test loop or an escalation, using 6.5 px mono on a paper mask.
- Avoid crossings: reassign steps or split the diagram rather than routing around.
- Focal slots: exactly one focal step (header chip at accent @ 0.20 with accent number and label), one focal node (accent border and accent role chip, title stays ink, fill accent @ 0.08), and that node's focal-in/out edges.
- Concern colors can override up to 3 elements, nodes, lanes and steps combined. Never put one on a focal element (accent wins) and never on an arrow.
  - Node override: fill C @ 0.06, stroke C @ 0.35, role chip C @ 0.18, title C. Sublabel and tool text stay muted and soft.
  - Lane override: stripe C @ 0.04 and label C. Use it on at most 1 lane.
  - Dark mode: lighten C by about 15%.
- Recommended concern palette (the same palette across all diagram types):
  - rust-red #b85450: governance, security, training
  - slate-blue #5a7d9a: quality, validation, monitoring
  - olive #7a8c47: published outputs
  - warm-brown #8c6d3f: archive, backup

## 253. Process map — legend and dark mode
- The legend strip starts at x=144 with rows STEPS, DATA TYPE ("left chip = input · right chip = output"), an optional CONCERN row, and FLOW. Show only the swatches actually used. Row y-offsets from the legend top are 16 / 37 / 58 / 79.
- Dark mode swaps only role tokens; every derived value stays a role at an opacity. Opacity bumps: lane tint 0.018 → 0.025, label-column divider 0.20 → 0.22, focal chip 0.20 → 0.22, focal node fill 0.08 → 0.12.
- Default nodes switch from white to ink @ 0.04 fill with an ink @ 0.20 stroke.
- The dot grid (ink @ 0.10), dividers (ink @ 0.12) and default chip fill stay the same.

## 254. Flowchart — shape vocabulary
- Use for decision logic, algorithms, "should I…?" branching, onboarding routing, and support triage.
- Shape tells the reader the node type, so never use fill color for it:
  - Oval (rx 20): start and end. Fill ink @ 0.03, stroke ink @ 0.30.
  - Rectangle (rx 6): step. White fill, 1 px ink stroke.
  - Diamond (polygon, about 200×96): decision, 3 exits at most. White fill, ink stroke.
  - Filled ink dot (r 4): merge point where branches rejoin.
- Typical node: 160×48. Name in sans 12 px weight 600; optional mono 9 px muted sublabel. Two-line diamond text is 14 px apart.
- Flow runs top to bottom with about 24–40 px vertical gaps between shapes.
- Draw arrows first: muted, 1.2 px, filled 8×6 marker.
- Legend title "LEGEND · SHAPE CARRIES TYPE" (mono 8 px, tracked 0.18em). Swatches for oval, rectangle, diamond, happy path, and branch.

## 255. Flowchart — branching, accent, and pitfalls
- Label every outgoing branch with a mono 8 px uppercase word (YES / NO), tracked 0.12em, on a paper-colored mask (12 px tall, rx 2).
- A common layout: one answer continues straight down the main spine and the other exits sideways to a terminal oval. Pick a convention and keep it for every diamond.
- Put accent on the happy path or on the single most consequential decision, never on every decision. The focal path's arrow is accent, 1.4 px with an accent marker. Its branch label is accent, and the focal end oval gets accent tint (accent @ 0.08) with an accent stroke.
- If two arrows must cross, add a small arc jump on one of them.
- Pitfalls: fill color used for node type; a diamond with 4+ exits (nest diamonds instead); unlabeled decision branches.

## 256. Swimlane — layout
- Use for cross-functional processes, RACI-style flows, vendor handoffs, and multi-team shipping workflows. If the subject is what the customer sees versus what stays hidden, with no arrows, use a service blueprint instead.
- Lanes are horizontal rows, one per actor, about 80 px tall. Labels sit in the left margin as uppercase mono eyebrows (9 px, tracked 0.18em, muted), not rotated.
- Hairlines: lane dividers at ink @ 0.10. Outer top and bottom edges plus the actor-column divider (x≈160) are heavier at ink @ 0.22.
- Each step is a rectangle (rx 6, about 120–140×48, white fill, ink stroke) inside its owner's lane. Name in sans 11 px weight 600; mono 8 px muted sublabel. A step never straddles two lanes: pick one owner.
- Lanes don't need equal step counts; a lane with one step is fine.

## 257. Swimlane — handoffs and emphasis
- Edges that cross a lane boundary are the most important ones.
  - Within a lane: a short horizontal arrow (muted, 1.2 px).
  - Across lanes: exit right, make one rounded turn (8 px quadratic curve), and enter the destination's top. If the steps are stacked, go straight down.
  - Revision or loop-back edges: dashed (5,4 or 4,3).
- Put accent (1.4 px, accent marker, accent label) on the single handoff that adds the most coupling or latency. The focal outcome step takes the accent-tint fill with an accent stroke.
- Use handoff labels sparingly (HANDOFF, REVISE, DEPLOY TRIGGER): mono 8 px uppercase on a paper mask.
- Legend: step, focal outcome, within-lane step, revision loop, critical handoff.
- Pitfalls: unlabeled lanes; a step drawn across two lanes; arrows snaking back and forth. Reorder the steps so the flow runs mostly straight.

## 258. Loop — when to use and anatomy
- Use for reinforcing cycles, flywheels, and feedback or operating loops: the last step feeds the first, and a shared hub accumulates state. Both motions show at once. Work moves clockwise around the ring, and each pass writes back to the center.
- Use a flowchart if the path ends, branches toward an outcome, or never truly returns. Use a plain cycle if the center doesn't accumulate state. The dashed write-back spokes are what make it a Loop; without them it's only a circular process.
- Budget: 5–8 stations and exactly one hub (two hubs means two diagrams). At most one focal station, and zero is allowed. Above 8 stations, split into an overview plus detail.
- Station order carries meaning: station 0 sits at the top and the rest proceed clockwise. The last station always connects back to the first; if that return isn't real, draw a flowchart.
- The hub holds accumulated state (memory, standards, evidence, policy), not a seventh step. Give it one name and one short sublabel.
- Canonical sizes: station 160×64, hub 200×104, ring radius 240, margin 64. With 6 stations: canvas 1040×680 with the center at (520,340).

## 259. Loop — geometry
- Station angle θk = −90° + k·360°/N; center = C + R(cos θ, sin θ). Snap station rectangles to a 4 px grid while keeping paired stations symmetric. Keep ring intersection points at 3 decimals so every arc stays on the same circle.
- Ring connectors are circular arcs on the station circle itself (`A R R 0 0 1`: same radius, large-arc 0, clockwise sweep 1). Each runs from the source box's clockwise exit intersection to just before the destination box's entry intersection.
- Pull the endpoint back by the marker overhang: φ_end = φ_entry − 1.2/R for a 1.2 px stroke and a tip at x=8 with refX 7. The arrow tip then lands on the box edge.
- Never mix arcs with straight or orthogonal ring segments. The gaps must read as pieces of one continuous circle.
- Spokes are true radii. The start is where the ray leaves the station edge: distance = min(half_w/|ux|, half_h/|uy|). The end stops a 6 px gap (4–8 px range) outside the hub stroke.
- The canvas must contain the circle's extremes, the station boxes, the markers, and the margin. Never shrink it until something clips.

## 260. Loop — styling and pitfalls
- Station: paper fill, ink stroke, medium radius, sans name, sublabel.
- Hub: the only dark element (ink fill, paper text), slightly larger than a station.
- Focal station: accent-tint fill, accent stroke, name may be accent.
- Ring flow: solid muted line, default arrowhead, clockwise only.
- Write-back spokes: dashed 5,4 in soft, reduced emphasis, soft arrowhead, pointing inward.
- Spoke labels are optional: uppercase mono in soft, on an opaque paper mask, 6–10 px clear of the stroke. Label only a curated subset.
- Draw order: paper and dots → ring arcs → spokes → label masks and labels → stations → hub → text.
- Connectors never overlap. The ring stays outside the hub. If two spokes leave one edge, keep them at least 12 px apart.
- Pitfalls:
  - two hubs
  - solid spokes, which look like primary flow
  - uneven station angles
  - arc and orthogonal segments mixed on the ring
  - routes through the hub (enlarge R instead)
  - accent on several stations
  - more than 8 stations
  - a "loop" that never returns

# Part 34 — Interaction & State

## 261. Sequence diagram — anatomy and lifelines
- Use for request/response flows, protocol exchanges, multi-actor interactions over time, API traces, incident reconstructions, and auth or token-refresh paths with branching.
- Actors sit as boxes in one row at the top: about 144–160×56, rx 6, with a small type tag (about 28–32×12, rx 2) at the top-left. Underlay each actor box with a paper rectangle so tinted fills stay opaque. Use the standard treatments: external actors soft-tinted, cloud actors ink @ 0.03 with an ink @ 0.30 stroke, the focal actor accent tint with an accent stroke.
- Lifelines are dashed (3,3) vertical lines at ink @ 0.20–0.22, 1 px, running from each actor to the bottom, drawn behind everything. Space lifelines about 220–320 px apart.
- Time flows top to bottom. A message never points upward.
- Activation bar: 8 px wide on the lifeline, fill ink @ 0.06, muted stroke 0.8, covering the span the actor holds control. Stack bars for nested calls, and close every bar.
- A self-message is a short U-loop (out about 36 px, down about 32 px, back) with its label to the right.
- Budget: 5 lifelines, 12 messages, 2 accent elements at most. Above that, split into a happy-path overview and a failure or refresh detail.

## 262. Sequence diagram — message kinds
- Sync call: solid muted line, or link-blue (#2e5aa8) when calls need a separate color, with a filled marker.
- Return: always dashed (5,4) with a filled marker. Muted, or matching the originating call color in multi-hop stacks. Never solid, and never an open head.
- Async or fire-and-forget: dashed muted with an open arrowhead. The open head is an unfilled polyline (0 0, 8 3, 0 6), stroke muted at 1.2.
- Headline success: solid accent, 1.4 px, accent marker. Use it on 1, at most 2, messages. Focal actor strokes don't count toward this budget.
- Labels: mono 8 px uppercase, tracked 0.08em, centered over the arrow on a 12 px paper mask (rx 2), about 4 px above the line. Never let a label sit over another lifeline: shorten it or move it into a gap.
- Leave at least 24 px between consecutive messages, on a 4 px grid. Common pitch is 40–48 px.

## 263. Sequence diagram — combined fragments (alt / opt / loop)
- When the flow branches (valid vs invalid token, retry, optional step), draw a frame. Never use free-floating if/else arrow clusters.
- Frame: rect rx 4, fill ink @ 0.02 (ink @ 0.04 in dark mode), stroke ink @ 0.22. It spans only the participating lifelines and sits at least 12 px outside the outermost lifeline centers so activation bars stay inside.
- Operator tab: 40×16 at the top-left, rx 2, paper fill, same stroke. Text ALT / OPT / LOOP in uppercase mono 8 px, tracked 0.12em, muted. Never use the sans node font.
- Guards: mono 8 px, tracked 0.04em, left-aligned at frame x+12 within the first ~20 px under the tab, e.g. `[token valid]`, `[else · 401]`, `[retry ≤ 3]`. The first message sits at least 24 px below the guard.
- alt has 2 regions at most, separated by a dashed (4,3) ink @ 0.20 divider inset 8 px from each side, on the 4 px grid, at least 16 px clear of messages. opt and loop have one region.
- Default to one fragment per diagram; allow two only if both are single-region opt or loop. Nesting depth is 1 at most. Never nest alt inside alt; split into two diagrams instead.
- Put accent on one headline success across the whole diagram, usually the happy-path return in the first alt region. Never accent both branches.
- Out of scope: par, critical, break, ref; create/destroy, found/lost messages, duration bars. Don't invent them.

## 264. Sequence diagram — pitfalls
- Upward-pointing messages, which reverse time.
- Activation bars that never close.
- Swimlane-style lanes instead of lifelines; they're a different grammar.
- If/else drawn as two unframed arrow clusters.
- A fragment frame covering actors with no messages inside it.
- Fragment operator in the sans node font instead of mono.
- A filled arrowhead on an async message, or an open arrowhead on a return.
- Accent on both alt branches, or on more than 2 messages.

## 265. State machine — layout and notation
- Use for finite state logic: order status, auth state, connection lifecycle, form wizard, job queue. For messages between actors over time, use a sequence diagram instead.
- States are rounded rectangles (rx 8, about 160×80). Name in sans 14 px weight 600; mono 9 px muted sublabel; a small outlined "STATE" tag (40×12, rx 2, mono 7 px) in the top-left corner.
- Start is a filled ink dot (r 6). End is a ringed dot: outer r 8 outline plus inner filled r 5.
- Transitions carry the label `event [guard] / action`, leaving out unneeded parts. Use mono 8 px uppercase, tracked 0.08em, on a paper mask. Every transition is labeled, because what triggers it is the point.
- Forward transitions are straight muted 1.2 px arrows along the dominant direction (left to right or top to bottom). Back-edges curve, e.g. a dashed 5,4 cubic arching above the row. Self-loops curve above the state.
- Rearrange states before accepting crossing transitions.

## 266. State machine — emphasis and pitfalls
- Put accent on the one state the reader should notice, typically the error state or the happy completion. Give it accent tint (accent @ 0.08), an accent stroke, and an accent tag outline (accent @ 0.50). Its incoming transition may be accent at 1.4 px.
- Mark archived or inactive states with ink @ 0.05 fill and a muted stroke.
- Rule of thumb: more transitions than twice the number of states usually means two state machines.
- "From any state" transitions: write one annotation (`* → Error on timeout`) instead of drawing edges from every state.
- Pitfalls: unlabeled transitions; spaghetti from global transitions; crossings that could be fixed by reordering.

## 267. Lifecycle phase map — banded state variant
- Use when one subject's journey is the story: 4–5 primary phases, plus separate wait/recovery states and terminal outcomes. Use a plain state machine when dense events and guards dominate.
- Three horizontal bands, each labeled in the top-left with mono 8 px tracked 0.14em: WAIT / RECOVERY (top), PRIMARY PHASES (middle rail), TERMINAL OUTCOMES (bottom). Band containers are rx 8 with a faint ink @ 0.035 fill and an ink @ 0.12 stroke.
- Primary phases: 150×72 rx 8 boxes in one row about 30 px apart, joined by straight arrows. The final success phase is the accent-tinted focal state with a small ring-dot glyph inside, and its incoming transition is accent at 1.4 px.
- Supporting wait/retry states: paper fill, muted dashed (5,4) stroke. They connect to the rail with orthogonal up/over/down paths, dashed for error and retry.
- Terminal outcomes use ink @ 0.04 fill with a muted stroke. Tell them apart with text, shape, and dash (e.g. a 1.5 px 3,3 dashed stroke for failure), never with extra colors.
- Every transition is labeled with a short mono verb (SUBMIT, APPROVE, RETRY, CANCEL) on an opaque mask.

# Part 35 — Time & Planning

## 268. Timeline — axis and events
- Use for release history, project milestones, incident timelines, roadmaps, and changelogs.
- Draw a horizontal hairline baseline through the middle (1 px, muted @ ~0.45) with end caps and boundary ticks (16 px tall, ink @ 0.20). Put date labels in mono 8 px, tracked 0.14em.
- Events are filled ink dots (r 4) on the baseline. Labels alternate above and below, joined by a 1 px drop line (ink @ 0.30, about 56 px long). Each label stacks a date eyebrow (mono 8 px muted) over a name (sans 12 px weight 600), with an optional mono 9 px sublabel.
- Major milestones get an accent dot (r 6), an accent drop line, an accent date, and a slightly larger name (14 px). Keep these to one or two.
- An optional ambient year watermark (mono 72 px, ink @ 0.06) can sit behind each year region.

## 269. Timeline — honesty and density
- The time scale must be honest. Unequal intervals get unequal spacing; never fake even spacing for looks.
- If one region is too dense, break the axis visibly rather than compressing it silently.
- Always label the axis unit, so the reader never has to ask "what unit is this?".
- Labels that crowd without a vertical offset become illegible. Alternate sides, and extend the drop lines to stagger further.

## 270. Gantt chart — grid and bars
- Use for plans with explicit start and end dates grouped into phases, when temporal overlap, parallel tracks, and milestone order must read at a glance.
- Left label column x=20–200: task names in sans 11 px weight 600, phase labels as 7 px eyebrows above each group. The timeline runs from x=200 to about 956–960.
- Pitch = timeline width ÷ total periods (e.g. 756 px ÷ 12 weeks = 63 px). Bar width = (end − start) × pitch.
- Rows are 40 px. Bars are 24 px tall, rx 4, with 8 px top padding. The bar label sits inside at x+8, baseline row+25, sans 10 px weight 600.
- Time-axis labels: mono 8 px just above the first row (y≈56), with a hairline separator at y≈64. Week gridlines are faint dashed (3,3) hairlines at ink @ 0.08.
- Phase zones sit behind each phase's rows (fill ink @ 0.02, stroke ink @ 0.10) with about 16–20 px between zones and an eyebrow label in the top-left.

## 271. Gantt chart — emphasis and limits
- Exactly one focal bar, for the key deliverable or the critical-path task: fill accent @ 0.12, accent stroke, accent label. All other bars use muted @ 0.15 fill, a muted stroke, and an ink label.
- An optional today or milestone marker is a vertical dashed muted line at the current period.
- Limits: 12 tasks (beyond that, split or collapse to a phase view); 5 parallel tracks per phase at most.
- Leave dependency arrows out of a first version unless they're essential. Never put start and end dates inside bar labels; the axis carries them.
- Pitfall: equal visual weight for every bar.

## 272. Kanban board — structure
- A kanban board is a state census, not a flow, and it has no connectors at all. If it needs an arrow anywhere, it's a swimlane or a process map.
- Up to 5 vertical columns, each 240 px wide, with 32 px gutters. Column background is ink @ 0.02 with no border.
- Header band: the column name in sans 12 px weight 600, left-anchored, and a right-anchored WIP chip. The chip is a rectangular tag (rx 2, never a pill) showing `n/limit` in mono 8 px. Queue and terminal columns show a bare `n`. Every in-process column states a limit. A full-width hairline rule sits under the header.
- Cards: column width minus 16 px padding per side, 56 px tall, rx 6, 12 px apart. Title in sans 12 px weight 600; sublabel `TICKET-ID · owner` in 9 px muted.
- Draw order: background → column fills → header text and chips → header rules → cards (box, blocked bar, title, sublabel) → legend.

## 273. Kanban board — card states and the accent budget
- Each card is in exactly one of four states:
  - default: white fill, ink stroke
  - blocked: fill accent @ 0.05, full accent stroke dashed 4,4, and a 4 px accent bar on the left edge
  - waiting or external: fill ink @ 0.02, stroke ink @ 0.20 dashed 4,3
  - done: fill ink @ 0.05, muted stroke
- When a column's count exceeds its limit, the WIP chip's stroke and text turn accent.
- The over-limit chip plus one blocked card use the whole 2-accent budget. Don't spend accent anywhere else.

## 274. Kanban board — density and pitfalls
- Budget: 5 columns, 4 cards per column, 12 cards total. When a column overflows, aggregate it into a count card ("+14 more") so the column never runs off the canvas.
- Queue and terminal columns show a bare count; everything in between must state a limit, because without one a column can't show it's over budget.
- Pitfalls:
  - arrows between cards
  - one card per person (an org chart in disguise)
  - in-process columns without WIP limits
  - accent on every blocked card (one or two read as signal; a column of accent is noise)
  - an unbounded Done column (cap it and note the archive point in a sublabel or footnote)
  - pill-shaped WIP tags, which read as status badges from another design language

# Part 36 — User & Product Maps

## 275. User story map — anatomy
- Use for the whole user story laid out so you can cut the first release. Narrative order runs left to right and priority runs top to bottom.
- Not a kanban board (no state columns) and not a user journey (no sentiment). Without release slices it is neither.
- Backbone: up to 5 activities as header cards, 200 px wide, rx 6, fill ink @ 0.05, muted stroke, 24 px gutters. Each card shows an eyebrow "ACTIVITY n" (8 px uppercase tracked) above the name (sans 12 px weight 600).
- Walking skeleton: under each activity, its user steps as 32 px cards (rx 4, white fill, ink stroke, 12 px), one or two per activity. Reserve room for two so row bottoms align.
- Release slices: full-width horizontal bands with a label (MVP, RELEASE 2, LATER) in a 96 px left margin, eyebrow 8 px. Backgrounds alternate ink @ 0.02 and none.
- Story cards: 48 px tall, rx 4, in their activity's column. Title in 12 px weight 600; 9 px sublabel such as `RPT-114 · 3pt`.
- If any slice has a gap, add dashed column separators (0.8 px, 4,4, 0.10 opacity) running from below the backbone to the last slice, drawn before the cards.

## 276. User story map — release cut, accent, and pitfalls
- The release cut is the editorial point of the map. Draw a full-width 1.5 px accent rule just under the MVP band, with a masked 8 px mono label RELEASE CUT at its right end.
- The second and last accent goes on the single riskiest story: fill accent @ 0.05, accent dashed 4,4 stroke, and a small rectangular RISK tag (rx 2).
- Legend: default story card, highest-risk treatment, release-cut line.
- Budget: 5 activities, 3 slices, 12 story cards, 4 cards per slice. When over, split by activity or collapse a slice into a count card.
- Pitfalls:
  - no cut line, which leaves a backlog in a grid
  - columns ordered by priority instead of narrative
  - stories that are technical tasks rather than user-visible outcomes
  - slices named by date (Q3) instead of scope
  - more than 3 slices
  - two personas on one map

## 277. User journey map — stage grid and content rows
- Use for what one person does across the stages of an experience and how each stage feels. If you can't name a feeling for every stage, use a process map or timeline. Not for system flows with no human in them.
- Stage headers: 5 equal columns, 200 px wide with 24 px gutters, after a 64 px left margin (col_left = 64 + i·224). Six stages at most. Each header is an eyebrow "STAGE n" (8 px) over the stage name (12 px weight 600), centered.
- Content rows: up to 3 bands under the sentiment band.
  - ACTIONS: 12 px sans, one short line per stage.
  - TOUCHPOINTS: 9 px muted.
  - An optional metric or owner row, styled like touchpoints.
- Row labels are uppercase eyebrows in the left margin, horizontal, never rotated or written vertically. Full-width hairlines separate the rows.
- One persona per map; overlaid curves erase each other.

## 278. User journey map — sentiment curve
- The sentiment band is what makes this a journey map: 160 px tall, directly under the headers.
- Three reference hairlines (rule @ 0.10, 80 px apart) for HIGH / NEUTRAL / LOW. Labels are 8 px muted eyebrows, end-anchored in the left margin.
- Five ordinal levels: HIGH, MED-HIGH, NEUTRAL, MED-LOW, LOW. Snap every stage to one of them. Never use a numeric 0–100 scale or emoji. Only the levels actually used need labeled hairlines.
- The curve is a smooth 1.5 px muted line through one r 5 dot per stage, placed at the stage column's center.
- The curve is a data line, so the orthogonal-elbow connector rule doesn't apply to it. Any other connector does follow that rule.
- The trough stage's dot and its incoming segment are accent. Everything else on the curve is muted.

## 279. User journey map — pain markers and accent budget
- Pain markers sit only on the trough: small dashed tag boxes (rx 2, accent @ 0.50 stroke dashed 3,3, no fill or a faint tint, 16 px tall) under that stage's action, labeled in mono 8 px with the friction. Two at most, stacked if needed.
- Accent budget is exactly 2: the trough dot with its segment, and the pain markers.
- Legend: hairline above, 160–180 px between entries. Three keys in order: sentiment line, trough highlight (required, since the dip is the finding), pain-marker tag.
- Pitfalls: no curve; more than 6 stages (split acquisition from retention); numeric axis; emoji; pain markers on every stage; vertical text labels.

# Part 37 — Cause & Analysis

## 280. Fishbone (Ishikawa) — structure
- Use for structured root-cause analysis of one observed effect, with causes grouped by category. It shows what was investigated, not just the conclusion.
- Not for a chronology of failures; use a timeline or sequence diagram for that.
- Spine: a horizontal ink line, 1.2 px, at the vertical center. It ends in an arrow into an effect box at the right-hand head. The box states the observed symptom or measurement, never the fix.
- Bones are straight diagonals at a fixed 60° to the spine, alternating above and below and evenly spaced. These bones and their sub-cause ticks are the only exemption from the orthogonal-elbow connector rule; callouts and cross-references still use rounded elbows.
- Each bone ends in a category tag box (rx 4, not a pill), sans 12 px weight 600.
- Sub-causes are 32 px horizontal ticks in soft, branching off the bone. Labels are 9 px, end-anchored just past the tick's open end.
- Draw order: background → spine → bones → ticks → tag boxes → effect box → legend.

## 281. Fishbone (Ishikawa) — geometry and budget
- With the head (effect box left edge) at x=HEAD and the spine at y=CY: attach_x(k) = HEAD − 160 − 160k. The far end is offset (−96, ∓168), an integer approximation of 60°. Odd bones go above, even below.
- Reference with HEAD=1200, CY=320: bones attach at 880 / 720 / 560 / 400 / 240, with tags at y=152 above and y=488 below.
- Ticks sit at m/6 along the bone (m = 2, 4 for two ticks; m = 3 for one): tick = (attach − 16m, CY ∓ 28m). The label goes at x = tick − 36, y = tick − 4 above the spine or +12 below.
- Five bones is the ceiling on a 1200-head canvas. A sixth clips, so widen the head and the canvas by at least 160 each, together.
- Budget: 3 sub-causes per bone, 18 in total.
- Focal pair, and the only accent: the confirmed root-cause bone (accent line, accent-tint tag with accent stroke) and the effect box (accent tint, accent stroke).
- Pitfalls:
  - sub-causes that restate the category
  - bones with no sub-causes
  - more than one root cause accented
  - a generic 6M template with empty categories (name categories from the actual investigation)

# Part 38 — Conceptual Models & Positioning

## 282. Venn / set overlap — construction
- Use for intersections of concepts or domains, shared attributes, "where A meets B", and frames like desirable × feasible × viable.
- Use 2 or 3 circles. With 4 or more, switch to a matrix.
- Each set has its own stroke tone (ink, muted, soft), 1 px. Fills are very low opacity (ink @ 0.04, muted @ 0.05, soft @ 0.05) so they compound naturally where circles overlap.
- Radii are equal when sets are comparable and proportional when they're meaningfully different. Never fake equal sizes. Keep centers and radii divisible by 4. Example: r 140 with centers (500,180), (428,320), (572,320).
- Isolate an intersection by chaining clipPaths: clip to circle A, then B, and fill circle C inside both.

## 283. Venn / set overlap — labels and focal region
- Set labels go in each circle's non-overlapping lobe or outside it, never across a stroke. Name in sans 12–14 px weight 600; optional mono 9 px uppercase sublabel, tracked 0.14em.
- Intersection labels sit centered in the overlap, 12 px weight 600. If the overlap is small, use a leader line to a label in clear space.
- One focal intersection, the sweet spot, gets the emphasis. Options: an accent label stroke, a clip-bounded accent @ 0.10 tint, or a solid ink fill with white text and a 75%-opacity sublabel.
- Pitfalls: unlabeled regions; circles that don't overlap when overlap is the point; dishonest equal sizes; accent on several regions; labels sitting on strokes.

## 284. Pyramid / funnel — construction
- Use for hierarchy of needs, priority ranks, value pyramids, conversion funnels, and content-importance stacks. Not for non-hierarchical data; use a tree or bar chart.
- Choose one orientation and never mix them. A pyramid points up: the narrow apex is the rarest or most valuable layer. A funnel points down: the narrow end is the conversion group.
- 4–6 layers, each a 4-point trapezoid polygon, 56–72 px tall (64 is typical). Widths shrink linearly. In a true pyramid the apex is a single triangle with the same slope as the layers below. Real funnel data must use proportional widths.
- Inside each layer: name centered in sans 12–14 px weight 600, sublabel in mono 9–10 px muted. An optional side annotation, mono 9 px tracked 0.08em, sits right of the layer edge (counts, or drop-off such as −40%).
- Fill either with subtle graded tints, or with an all-light fill and hairline dividers (ink @ 0.12). Pick one. The outer silhouette is 1 px muted or ink.

## 285. Pyramid / funnel — emphasis and pitfalls
- Accent goes on one layer only: the apex of a pyramid, the conversion layer of a funnel, or the critical bottleneck. Give it accent tint, an accent stroke, and an accent annotation. Never the base.
- An optional axis arrow in the left margin with an eyebrow label (e.g. "rarer ↑", "drop-off ↓"). Keep that text horizontal.
- An italic one-line footnote under the figure can state the thesis (e.g. "The base funds the apex.").
- Legend: the focal layer swatch, a supporting-layer swatch, and an honesty note such as "Layer width is honest."
- Pitfalls: 7+ layers; dishonest widths; accent on the base; a pyramid used for data that isn't a hierarchy.

## 286. Quadrant (2×2) — standard positioning matrix
- Use for prioritization (impact × effort), positioning (reach × frequency), portfolio maps, and 2×2 decision frames where the position inside a cell carries meaning.
- The axis cross is 1 px ink (about ink @ 0.45) through the center. Shorten each arrow 60–80 px inside the canvas edge so labels can sit past the tips.
- Axis labels are minimal: one uppercase word at each tip, mono 9 px regular weight, tracked 0.18em. No arrow glyphs, no parentheticals, no HIGH/LOW modifiers, never at the midpoint, never on the axis line.
- Optional quadrant corner tags (DO FIRST, MAJOR PROJECTS, QUICK WINS, AVOID): mono 9 px tracked 0.18em. Only the focal quadrant's tag is accent and weight 600.
- Items are small ink dots (r 4) with labels 8–10 px to the right (sans 11 px muted). Labels never cross an axis, and no item sits on an axis line, since that makes its quadrant ambiguous.
- The single "do first" item gets an accent dot (r 6) and an ink weight-600 label. An optional accent @ 0.03 wash may tint that quadrant only.
- Around 12 items at most; cluster or split beyond that. Never fill the four quadrants with different colors, because position is the signal.

## 287. Quadrant — scenario-matrix variant (consultant 2×2)
- Use for four futures, archetypes, or strategic options across two independent drivers (scenario planning, strategy decks). The reader should come away with four named bets, not a point cloud. Don't use it when position within a cell matters.
- Axes run across a range, not a measurement: 1.2 px ink, double-ended, with outward markers at both ends (about 9×7). The cross passes between the cells, not through them. Tips sit 20–40 px beyond the outermost cell edge.
- Axis labels are one word per tip, mono 9 px regular, tracked 0.18em, in ink:
  - top: middle-anchored, about 12 px above the tip
  - bottom: middle-anchored, about 20 px below
  - left: end-anchored, 12 px out, vertically centered
  - right: start-anchored, 12 px out, vertically centered
- Four equal cells (240×160, 280×180, or 300×160), rx 6, with a 40–60 px gap from the axis cross.
  - Non-focal cells: fill ink @ 0.04, stroke muted @ 0.28.
  - Cell content: corner tag `NN · DIMENSION-A / DIMENSION-B` (mono 8 px, tracked 0.18em, muted), then a scenario title (sans 16 px weight 600), then a 1–3 line description (11 px muted, left-aligned, 16 px leading).
- Exactly one focal cell: accent-tint fill (accent @ 0.06), 1.2 px accent stroke, accent corner tag at weight 600, and an accent @ 0.04 wash over the whole quadrant behind it.
- The corner tag words must match the axis labels exactly; a mismatch reads as a bug.
- Keep the warm paper, dot grid, serif page title, and legend strip (swatches "headline bet" and "candidate future"). Never name cells "Scenario 1–4" in a finished piece. 3×3 or 2×3 grids are different diagrams.

## 288. Wardley map — axes and components
- Use to place the components of a value chain against how evolved each one is: what to build, what to buy, what's about to move. It's a strategy map, not an architecture diagram, so no runtime topology, protocols, or request direction.
- Y axis is the value chain, from "Visible to the user" at the top to "Invisible" at the bottom. Write the axis words as stacked horizontal text lines at the axis ends, never rotated. The axis line is a solid rule at 0.20 opacity, with no numeric ticks, since visibility is ordinal.
- X axis is evolution in four qualitative bands (Genesis | Custom-built | Product | Commodity), separated by three dashed (4,4) rule hairlines at 0.10. Band labels run along the bottom as 8 px uppercase tracked muted eyebrows.
- Place each component in a band, not at a numeric score such as "6.5".
- Components are r 6 circles with paper fill and a 1 px ink stroke. The name sits 12 px above the dot, middle-anchored, sans 12 px weight 600. Use the optional 9 px muted qualifier below the dot sparingly.

## 289. Wardley map — dependencies and movement
- Dependency links are thin straight lines (muted, 0.8 px) from a component down to what it depends on, with no arrowhead. This is the map's one exemption from the orthogonal-elbow rule, because position is the data.
- Every component links to something; delete orphans.
- Movement is a short right-pointing accent arrow, dashed 5,4, with an accent marker, from the dot's edge toward the next band. It only ever points right; a left-pointing arrow is a contradiction.
- Leave movement arrows unlabeled; the legend's "Evolving" swatch covers what they mean. Add a label only for something the arrow can't say on its own, such as a timeframe ("BY Q3") or a driver ("VENDOR LOCK-IN").
- If you add a label, mask it (mono 8 px, 6–10 px clear of the stroke). First check that the band below the arrow isn't crossed by the component's own fanning links and the band above isn't taken by its name; if neither is clear, drop the label.
- Accent budget is 2: the moving component's dot (accent-tint fill, accent stroke) and its arrow, or two movers sharing those slots.

## 290. Wardley map — density and pitfalls
- Budget: 9 components, 12 dependency links, 2 movement arrows, 2 accent elements. Beyond 2 movement arrows the map stops making one point and becomes a forecast nobody can act on.
- The legend strip goes at the bottom with a hairline above, with the canvas extended about 60 px for it. It includes an "Evolving" swatch (accent dot plus dashed accent arrow).
- Pitfalls:
  - treating evolution as a 0–10 maturity score
  - numeric ticks on the value-chain axis
  - components with no links
  - right-to-left movement
  - rotated or vertical axis text
  - architecture semantics such as request direction or protocols

# Part 39 — Chart Principles

## 291. Shared Plot Frame
- Draw every Cartesian chart inside a `0 0 1000 500` viewBox with plot margins left `80px`, bottom `60px`, top `40px`, right `40px`; the plot band runs `x` `80 → 960`, `y` `40 → 420`.
- Put the x-axis baseline at `y=420` and the y-axis rule at `x=80`, running `y=40` to `y=420`.
- Place the rotated value-axis caption at `x=24` (e.g. `rotate(-90 24 230)`); a horizontal value axis takes the un-rotated form instead.
- Area charts without axes (treemap, marimekko, slopegraph gutters) use the plot `x` `40 → 956`, `y` `40 → 420` so the legend still lands where readers of bar, line and scatter expect it.

## 292. House Legend Rhythm
- Put the legend in a horizontal strip at the bottom: hairline rule at `y=462`, the `LEGEND` eyebrow and the source line at `y=478`, key swatches at `y=488` with key text on baseline `y=496`–`497`.
- Default area-key swatch is a `16×8px` rect matching the mark's fill and stroke; line-type keys are a `24px` line plus its dot so stroke weight is visible.
- Circular keys centre at `cy=493` so they share the `497` text baseline with rect keys.
- Right-align the source line in mono `8px` on the `LEGEND` row; it states what is encoded, the dataset, the date, the bounds, the bucket size and any omissions.
- Keep the legend rhythm identical across chart types even where it falls off the `4px` grid; consistency across the family beats grid purity.

## 293. The 4px Grid and Data Exemption
- Snap designed constants (axis positions, gutters, caption baselines, legend rows, bar x-positions and widths, box heights) to the `4px` grid.
- Never snap data-scaled coordinates (endpoint y-values, bubble centres, segment boundaries, bar tops); round them to the nearest whole pixel instead, at most `0.5px` off.
- When grid snapping or gutters move area, measure the damage as relative error `(drawn − true) ÷ true`, never as percentage points.

## 294. One Accent Rule
- Use exactly one accent element per figure; "everything is important" means nothing is.
- The accent marks the editorially focal item — the one the title is about — never automatically the biggest, best or worst value.
- Default accent tokens: `#bf4520` on light paper, `#f08a59` on dark paper.
- Never let the accent be the only carrier of data: position, labels and the legend naming the focal item in words must carry it redundantly.
- Carry focus with stroke weight or shape as well as tone (e.g. `2.4px` focal vs `1.2px` other), because weight survives greyscale and both skins.

## 295. Ink Opacity Ramp Instead of Hue
- When every series or item is labelled where it sits, use an `ink` opacity ramp plus one accent, never a hue per series; hue would re-encode what labels already say.
- Reserve the categorical series palette (`series-1` sage, `series-2` dusty-blue, `series-3` mustard, `series-4` rust-brown, `series-5` slate) for charts where hue is the only way to follow a series (multi-series line, radar); apply it in order and never skip slots.
- Never use rainbow fills; one hue per cell destroys rank reading and the one-accent rule.
- Remember `ink` is a role, not a colour: identical opacities composite darker on light paper and lighter on dark.

## 296. Skin Tokens and Contrast
- Default light skin: paper `#f5f5f5`, ink `#2d3142`, muted `#4f5d75`, accent `#bf4520`; dark skin: paper `#2d3142`, ink `#f5f5f5`, muted `#bfc0c0`, accent `#f08a59`.
- Measured contrast on light paper: `ink` `11.8:1`, `muted` `6.11:1` (`7.07:1` on dark), default accent `4.71:1` (`5.21:1` on dark), `soft` `3.48:1`.
- Data strokes and graphical objects must clear `3:1` (WCAG 1.4.11); text must clear `4.5:1`.
- Never set text in `soft`; it fails AA everywhere. Keep labels `ink` (names) and `muted` (values), including on the focal item — an accent label is the most common way to fail contrast while looking deliberate.
- Resolve every token against its own skin column; carrying a light-skin ink into the dark skin can composite to `1.000:1` and erase the mark.

## 297. Skin-Neutral Legend Wording
- Name ramp direction by contrast or strength, never by lightness: "strongest tone", "stronger contrast is larger", "faintest fill is the largest bubble" — never "darker is larger".
- A lightness word ships false in one of the two skins while rendering perfectly in both; only reading the dark variant catches it.

## 298. Honest Scales
- One finite, nonzero, linear scale per quantitative axis, shared by every mark.
- Never truncate a magnitude axis (bars, waterfalls, bubbles, box plots, polar); state any tight bounds in the source line where truncation is legitimate (slopegraph).
- Never use a log scale without declaring it; prefer not at all where area or angle is read.
- Crowded marks are data: never nudge a mark off its true value to make room for a label — shrink marks, drop labels, or reduce items instead.

## 299. Round Once, Draw From the Rounded Number
- Round each value once, then derive the printed label, the declared metadata and the drawn geometry all from that rounded number, so they are three statements of one fact.
- Print one complete number per value label; a unit suffix is fine (`208ms`), a separator that changes the value or a second number is not.
- If displayed rounding stops parts reconciling with a printed total, carry more precision or disclose it (`PARTS ROUNDED, MAY NOT SUM`).

## 300. Disclose Omissions
- Never silently drop a series, row, column, cell, layer or item; a missing part makes the remaining picture a lie.
- Count anything omitted in the footnote or source line, and say why.
- Never coerce a missing value to zero, and never interpolate to complete a line or shape.

## 301. Bind Every Meaningful String
- Every visible string that carries meaning (names, values, captions, ticks, legend totals) should be bound to the data it describes, so labels cannot be swapped between marks while every number stays correct.
- Every label must sit nearer its own mark than any other mark.
- Bake offsets into coordinates; never position data marks or bound labels with transforms or CSS geometry.

## 302. Paper Underlays and Masks
- Paint a paper-fill underlay of identical geometry beneath every translucent data mark (bars, cells, bubbles, boxes) so gridlines and background patterns do not show through.
- Put a paper-fill rect mask behind point labels that sit over data.
- Never use an opaque mask over a filled band (e.g. a sankey ribbon); it reads as a hole punched in the diagram.

## 303. Editorial Restraint
- No 3-D extrusion, shadows, depth or rounded bridge bars on any chart.
- Gridlines are faint: `ink @ 0.08`, `0.8px`; axis lines `ink @ 0.25`, `1px` on light (`ink @ 0.20` on dark).
- Omit gridlines whenever marks print their own values or the axis carries no scale.

# Part 40 — Line Charts

## 304. When to Use a Line Chart
- Use for continuous trends over time or a sequential index when direction and rate of change between points is the message.
- Use `4–12` data points; fewer → a summary stat, more → aggregate into periods.

## 305. Line Axes and Gridlines
- Space x-axis time/index labels evenly below the plot in the `arrow-label` role at `8px`, centred on each point x.
- Draw `4–6` horizontal y-gridlines at regular intervals, `ink @ 0.08`, `0.8px`.
- Include zero on the y-axis when absolute magnitude matters; do not start lines off a shared zero baseline unless annotated.

## 306. Line Series Limits and Styling
- Cap multi-series line charts at `5` series; more is visual mush — reduce or split.
- Focal series in `accent`, others in `series-1` → `series-4` in order.
- Draw lines as polylines with no fill and `stroke-linejoin="round"`: focal `1.8px`, others `1.2px`.

## 307. Vertex Dots
- Put vertex dots (`r=4`, filled) only on the focal series; other series are line only.
- Never put dots on every series once there are `4+` series.

## 308. Area Fill
- Optionally fill the focal series only, closing to the `y=420` baseline at `0.08` opacity, and only when the area meaning matters.

## 309. Smoothing and Gaps
- Use straight segments between sampled points; spline curves invent values between samples — a polyline is honest.
- Never connect discontinuous data segments; leave a visible gap.

# Part 41 — Bar Charts

## 310. When to Use a Bar Chart
- Use for comparing one discrete quantity across categories or time intervals.
- Vertical columns are default; switch to horizontal bars when labels are long or there are more than `8` categories.

## 311. Bar Count and Width
- Use `4–8` bars; more than `8` → group into periods or split the chart.
- Bar width must be `≥ 50%` of the column pitch; the gap never exceeds the bar (typical pitch `110px`, bar `72px`).

## 312. Bar Axes and Labels
- Y-axis labels right-aligned at `x=72` (`8px` left of the plot), `arrow-label` role `8px`, `muted`.
- Category labels centred below each bar in the `node-name` role `11px`, weight `600`.
- Never rotate category labels more than `45°`; shorten labels or go horizontal.
- Value labels in the `arrow-label` role `8px`, baseline `8px` above the bar top; focal label in accent, others `muted`.
- Always start the y-axis at `0`; a truncated bar axis distorts the magnitude ratio.

## 313. Bar Focal Treatment
- One focal bar max: `accent @ 0.12` fill with `accent` stroke.
- All other bars: `muted @ 0.15` fill with a `1px` `muted` stroke.

## 314. Grouped and Stacked Bars
- Grouped bars: at most `2` bars per category — `accent` for the primary series, `series-1` for the secondary.
- Stacked bars: `accent` on the focal segment, muted tints for the rest, and print the total at the top of each stack.

## 315. Dumbbell Layout
- Use a dumbbell for a two-state comparison where the distance between ends is the message (before/after, two cohorts, target vs actual); exactly two series — a third dot makes it a dot plot.
- Horizontal only; left margin `200px`, plot `x` `200 → 960`, `y` `40 → 420`; row labels right-aligned at `x=188`, `node-name` `11px` `600` `ink`.
- Row pitch by count: `4` rows → pitch `88` from `y=96`; `5` → `64` from `96`; `6` → `64` from `76`; `7` → `52` from `72`; `8` → `48` from `68`.
- Vertical gridlines at each tick `ink @ 0.08`, `0.8px`, spanning `y 56 → 408`; at the domain floor the axis line (`ink @ 0.25`, `1px`, `y 40 → 420`) replaces the gridline.
- Tick labels centred under gridlines at `y=440`; axis title in the `eyebrow` role `7px`, tracked `0.14em`, centred at `x=580`, `y=456`.
- Position: `x = 200 + (v − floor) ÷ (ceil − floor) × 760`, rounded to the nearest integer pixel.

## 316. Dumbbell Marks and Contrast
- Dots `r=6`: reference end hollow (paper fill, `muted` stroke `1.5px`), focal end solid `accent` with a `1px` `ink` stroke — shape, not hue, carries the pairing.
- The solid dot repeats on every row; do not additionally accent a "most changed" row.
- Connector `ink @ 0.55`, `1px` on light (`3.19:1`), `ink @ 0.40` on dark (`3.24:1`), drawn before both dots so they cap it; the `0.25` axis weight (`1.60:1`) is too faint.
- Value labels sit outside the pair by geometry: left label right-anchored at `min(x) − 12`, right label left-anchored at `max(x) + 12`, baseline `y + 4`, `8px` `muted`.
- Floor exception: when `x_left − 12 < 200`, centre that label above its dot at baseline `y − 10` to avoid colliding with the row label.
- Legend: hollow key then solid key, plus the row order.

## 317. Dumbbell Minimum Gap
- Two `r=6` marks touch at `12.75px` separation and read as one blob below about `16px`.
- Never widen the separation; keep true positions and shrink both marks (`r=4` touches at `8.75px`), or print both values and mark the row as too close to resolve.

## 318. Dumbbell Honesty
- Domain follows the data's range, never its observed extremes: all `≥ 0` → `floor = 0`, round `ceil` up; all `≤ 0` → `ceil = 0`, round `floor` down; mixed signs bracket both and draw a zero line at axis weight; all zero → finite fallback `floor = 0`, `ceil = 1`.
- Narrowing the domain inflates gaps (an 8-point gap is `61px` on `0–100` and `152px` on `40–80` across `760px`).
- Label both endpoints with real values; state the row order (by endpoint, signed change, absolute change, or a natural order).
- The connector is a gap, not a trajectory; never narrate it as movement.
- A row missing an endpoint is disclosed, never imputed or silently dropped.

# Part 42 — Scatter & Bubble

## 319. When to Use a Scatter Plot
- Use for correlation and distribution of two continuous variables, clusters, outliers and high/low performers.
- Plot `5–30` points; fewer → describe in prose; more → bin into density contours or use a beeswarm.

## 320. Scatter Axes
- X axis at `y=420`, Y at `x=80`; `4–6` gridlines per axis at equal intervals; tick labels in the `arrow-label` role `8px`.
- Include zero when absolute position matters; exclude it when the range is tiny and far from zero.

## 321. Scatter Points
- Standard point `r=5`, `muted @ 0.20` fill + `1px` `muted` stroke over a paper underlay.
- Focal point `r=6`, `accent @ 0.15` fill + `1.2px` `accent` stroke.

## 322. Scatter Labelling and Overlays
- Label at most `2–3` points (the focal and notable outliers), `8px`, on a paper mask.
- Add a trend line only when the trend is visually obvious: `ink @ 0.25`, dashed `4,3`; never force a fit onto scattered data.
- Optional quadrant dividers: light dashed lines at the median x and y, quadrant names in `8px` `muted`.
- Never encode a third value with ad-hoc point size on a plain scatter; use a bubble chart.

## 323. Bubble Chart Use and Budget
- Use when three quantities per item matter jointly (x, y, magnitude); not for categorical third values or magnitudes spanning several orders.
- Plot `5–15` bubbles; above `15` areas stack into a density cloud.

## 324. Bubble Area Encoding
- Area encodes the value, never radius: `r = K·√value` with one constant `K` for the figure, sized so the largest bubble stays inside the plot (e.g. `K = 1.4` giving `10.8–42px`).
- Radius proportional to value is the unforgivable error — a `6×` value reads as `36×` the ink.
- State the area scale in the source line; a non-positive magnitude cannot be a bubble — omit it and say so.

## 325. Bubble Drawing and Colour
- Paint largest bubbles first so small ones are never buried; give each a paper underlay.
- Ink opacity ramp runs faintest-on-largest (`0.14` largest → `0.35` smallest) as ink-mass compensation, not an encoding; the legend says which end is which.
- Every bubble keeps a `muted` stroke for edge contrast; one accent bubble for the editorially focal combination.
- Bind `4–6` axis ticks per axis to the numbers they print; label the focal plus at most `2–3` outliers.
- Axes include zero or the source line states the bounds; never move a bubble to stop overlaps.

# Part 43 — Distributions

## 326. Choosing a Distribution Form
- Beeswarm: one distribution where every unit deserves a mark (`20–300` items).
- Box plot: comparing the five-number summary across `3–8` groups.
- Ridgeline: comparing the silhouettes of `3–12` distributions on one x-scale.
- A single distribution with no comparison is a histogram; past `~300` items bin into one.

## 327. Beeswarm Axis
- One horizontal value axis at `y=420` with `4–6` bound ticks in `8px` and vertical gridlines only; the swarm axis has no scale and gets no ticks or horizontal rules.
- Linear scale only; a log axis must be declared and is best avoided.
- State in the legend or source line that vertical spread is packing, the axis bounds, and any omissions.

## 328. Beeswarm Packing
- One dot per item, all at one radius (e.g. `r=4`), focal included.
- Greedy dodge around a midline (e.g. `y=230`) alternating above/below at pitch `2r+2`; any collision-free arrangement is legitimate.
- No two dots may overprint; overlap closer than two radii (`0.5px` slack) turns density into false darkness.
- Never move a dot along the value axis; dots sharing a value share a position (within `1px`) and dodge apart.
- Never sort the dodge by a second variable or draw the midline as if it were a scale.

## 329. Beeswarm Colour and Labels
- One identical non-focal fill for every dot (e.g. `ink @ 0.55`) plus a `0.75px` `muted` stroke; density reads as thickness, never tone.
- At most one accent dot (`accent @ 0.55` fill, `1.2px` accent stroke).
- Label the focal dot plus outliers, at most `6`, `8px` small-caps on paper masks, one tier per label, alternating sides, with hairline leaders; names must be non-empty and unique.

## 330. Box Plot Layout
- Horizontal only; category labels in a `160px` left margin, right-aligned at `x=148`, `node-name` `11px` `600`; value scale starts at `x=160`.
- `3–8` series; below `3` use a table, above `8` split overview from detail.
- One box per series, height `32px`, centred on its row, `rx=2`, over a paper underlay.
- Median is a vertical `1.5px` `ink` line through the box at q2 — the only full-strength ink mark.
- Linear value axis from a stated floor, ideally zero.

## 331. Box Plot Five-Number Rules
- Order must hold: `wlo ≤ q1 ≤ q2 ≤ q3 ≤ whi`; box left is q1, right is q3; width encodes the IQR — never pad it for a label.
- Tukey fences: whiskers run to the last inlier inside `q1 − 1.5·IQR` and `q3 + 1.5·IQR`, with `16px` caps.
- Outliers are `r=4` dots strictly outside both whiskers and fences; never draw an inlier as a dot or park an outlier on the fence; show at most `8` outliers per series.

## 332. Box Plot Colour
- Non-focal boxes `muted @ 0.15` fill + `muted` stroke; one focal box `accent @ 0.12` fill + `1.2px` accent stroke.
- Outliers inherit their series stroke; the median stays `ink` on every row.

## 333. Ridgeline Layout
- `3–12` ridges, `8–40` bins each.
- One baseline per ridge at a fixed pitch (e.g. `y` `152/208/264/320/376`, pitch `56px`), each with a baseline rule (`ink @ 0.25`, `1px`) across the full bin run.
- x-run `320 → 680`, e.g. `13` bins `30px` apart; names right-aligned ending at `x=304`, ranges starting at `x=696`, `16px` clear of the plot, baseline `+3.5px`.
- Bin ticks in the `eyebrow` role `9px` at `y=400`, tracked `0.14em`; x-axis caption at `y=424`.
- No gridlines; baselines are the rules.

## 334. Ridgeline Shape Rules
- One amplitude for every ridge, stated in the source line; per-ridge normalisation is the unforgivable error.
- Straight segments between bins closed with `Z`; no smoothing — splines invent extrema between bins.
- First and last bins are zero so each outline starts and ends on its own baseline; no vertex below the baseline; never clip mid-mass.
- Overlap the row above, but no peak may reach the baseline two rows up; fix collisions with more pitch, never a smaller amplitude.
- Height is share (normalised per series count), not volume — say so in the source line.
- Print each ridge's range (first to last nonzero bin) in x-axis units.

## 335. Ridgeline Colour
- Focal ridge: `accent` stroke `2.4px`, fill `accent @ 0.16`; others: ink ramp stroke `0.80 → 0.62` (floor `0.53`) top to bottom at `1.2px`, fill `ink @ 0.12`.
- The accent marks the unusual shape, not the slowest performer.

# Part 44 — Rank & Change

## 336. Slopegraph Use
- Use for change between exactly two comparable states across several series, read as direction, steepness and crossings.
- `4–10` series; fewer → a sentence; more → endpoint labels collide. Three or more states → line or bump chart.
- Never for two variables in different units (use a scatter).

## 337. Slopegraph Layout
- Two vertical axis rules, `y` `40 → 420`, at `x=320` and `x=680`; keep the `360px` run narrower than the `380px` plot height so slopes spread (`4°` to `35°`).
- Left gutter: names right-aligned ending `x=272`, values ending `x=304`; right gutter: values from `x=696`, names from `x=728`; size gutters to the longest name.
- State captions in the `eyebrow` role `9px`, centred at `y=440`, tracked `0.14em`.
- No gridlines; endpoints print their own values.
- Dots at both endpoints: `r=3` non-focal, `r=4` focal; never curve the connector.

## 338. Slopegraph Colour
- One accent plus an ink ramp `0.80 → 0.62` ordered by left-hand value; hard floor `0.53` (`3.03:1`), with `0.62` at `3.84:1`.
- The ramp separates range ends, not neighbours; labels, not tone, distinguish series.
- Focal stroke `2.4px` vs `1.2px`; non-focal names weight `500`, focal `600`, names `11px` `ink`, values `9px` `muted`.

## 339. Slopegraph Honesty
- Both axes share the same scale, units and origin; a shifted origin tilts every slope by a constant.
- A tight domain is fine if stated in the source line (e.g. `100–550ms`); log scaling is not.
- Label both endpoints with real values; drop a series missing an endpoint and say so.
- Never move an endpoint for its label; merge or drop series that coincide at both ends and disclose it.
- The line is a connector, not a trajectory: never read intermediate values or date a crossing.

## 340. Bump Chart Use
- Use for rank movement across `3–6` ordered snapshots with `4–8` series, when position, not magnitude, is the story.
- Two snapshots → slopegraph; magnitude stories → line chart.

## 341. Bump Chart Layout
- One axis rule per snapshot evenly pitched (e.g. `x` `320/440/560/680`), slopegraph gutters (`272`/`304` left, `696`/`728` right).
- Rank rows on a fixed pitch, e.g. `y = 88 + 56 × (rank − 1)`; every vertex lands exactly on its row and on the grid.
- Straight segments, dots at every vertex (`r=3`, focal `r=4`); never subway curves.
- Name and rank (`#1…#6` sigil) at first and last appearance, on the series' own row and in the outboard gutter of the end it names.
- Snapshot captions `eyebrow` `9px`, centred under each axis; no gridlines.

## 342. Bump Chart Honesty
- State the ranking key and tie-break in the source line; each snapshot's ranks are a permutation of `1..N` — no ties, no skipped ranks.
- A changed ranking definition between snapshots invalidates the chart.
- Draw late entry/early exit as absence, never interpolation; never smooth a tie into a crossing; never nudge a vertex off its row.
- Colour as slopegraph: ink ramp `0.80 → 0.62` ordered by first-snapshot rank, one accent on the story series (often the one that fell), `2.4px` vs `1.2px`.

# Part 45 — Part-to-Whole

## 343. Treemap Use and Layout
- Use when one total decomposes into parts and the question is "what dominates, and by how much?"; not for exact ranked values, quantity-less containment or traceable hierarchies.
- Squarified layout: sort descending, lay rows against the shorter side so aspect ratios stay near `1`; never stripes.
- `4–8` cells; beyond `8` group the tail into a named "Other" cell.
- Snap edges to the `4px` grid with a `4px` gutter; keep each cell within a few percent of its true share (relative error, e.g. worst case `2.7%`, never beyond `8%`).
- State the encoding in the source line (`AREA = POPULATION`); nest at most two levels in a static figure.

## 344. Treemap Fill and Stroke
- Rank-ordered ink ramp `0.16 → 0.04`; contrast ceiling for `muted` value text is `0.16` on light and `0.14` on dark.
- Every cell `1px` `ink @ 0.30` hairline, `rx=2`; one focal cell `accent @ 0.16` fill with `1.5px` accent stroke.
- Never use mid-tone fills (solid accent or `50%` ink); they fail contrast against both light and dark text.
- Legend names the ramp direction by contrast ("stronger contrast is larger").

## 345. Treemap Labelling Tiers
- Labels inside the cell, top-left, `16px` inset: name `node-name` `12–14px` `600`, value `sublabel` `9px` on the next line.
- Large cells: name + value + share; medium: name + value; small: a honest 3-letter mono abbreviation.
- Slivers: no text; if at least `12×12px`, a filled `ink` disc `r=5` with a paper `i`, name and share in the legend; below `12px`, identify by legend only.
- Labels and markers must never cross the cell boundary; never rotate a label to fit, never shrink a cell for its label.

## 346. Treemap Honesty
- Area is the only encoding: never clip, floor or log-scale a cell, never drop a small one; merge undrawable parts into a named "Other".
- If several cells are invisible at target size, use a bar chart.
- Watch the smallest cell hardest — it absorbs the grid's residue.

## 347. Marimekko Use
- Use for a two-way part-of-whole: column width is category share, segment height is within-category share, area is joint share.
- `3–8` columns, `2–5` series; beyond that use "Other"; one series → bar chart; equal-width columns are a 100% stacked bar.

## 348. Marimekko Layout
- Treemap plot; column captions at `y=438`, `sublabel` `9px`, centred, printing name and share of the whole (`web · 31%`).
- Constant `4px` gutters between columns; every column full plot height; segments tile with no gaps, separated by hairlines only.
- One series order top to bottom in every column (largest overall total on top); an absent series is omitted, never drawn at zero height.
- Label tiers by segment height: `≥ 56px` → name `12px` `600` + amount/share `9px`; `32–55px` → `11px`/`9px`; below → info mark or nothing; widths under `~24px` take the mark.
- Keep the canvas at `min-width: 760px` inside a local horizontal scroller on narrow screens.

## 349. Marimekko Colour and Honesty
- Ink ramp per series, not per cell: `0.16 → 0.10 → 0.05` light, `0.14 → 0.09 → 0.04` dark; one accent segment with `1.5px` accent stroke.
- Width, height and area must all match the amounts (relative error); never widen or pad for a label.
- State unit, period and total in the source line, and say when amounts are illustrative.

## 350. Waterfall Use and Layout
- Use when a start total becomes an end total through signed contributions and the running total is the story.
- Vertical columns only, narrative order; `3–8` bars including both totals and at most `1` subtotal; merge the tail into a named "Other" bridge.
- Equal-width bars, bar `≥ 50%` of pitch (e.g. width `96` on a `144px` pitch from `x=112`).
- Totals anchor at the baseline; bridges float between the running totals before and after.

## 351. Waterfall Carries
- A horizontal carry crosses every gap at the running-total level, edge to edge: `ink @ 0.55` `1px` light, `ink @ 0.40` dark.
- A floating bar with no carry is bars at odd heights.

## 352. Waterfall Sign and Emphasis
- Sign by fill weight, not hue: increases `muted @ 0.15` fill + `muted` stroke; decreases hollow (paper fill, same stroke).
- Totals heaviest: `ink @ 0.08` fill, `1px` `ink` stroke.
- At most one focal bridge: `accent @ 0.12` fill, accent stroke, accent label.
- Totals and increases label at `top − 8`; decreases label at `bottom + 12`; deltas print an explicit `+`/`−`.
- Never green-up/red-down; never mix units mid-walk.

## 353. Waterfall Honesty
- Start plus every signed bridge must equal each subtotal and the end total exactly (exact decimal arithmetic).
- Bridges span exactly their two running levels (within `0.75px`); carries sit at the level they transport.
- Drop zero bridges and mention them in prose; a zero or negative start total is invalid.
- Domain follows the dumbbell rule; never truncate.

## 354. Sankey Use
- Use when a quantity splits and merges across stages and band thickness must carry data; a single narrowing quantity is a funnel, a plain step sequence is a process diagram.
- Exactly `3` stage columns; max `8` nodes, `12` ribbons, `2` accent elements (a focal path's ribbons count as one); over budget → two linked sankeys.

## 355. Sankey Nodes and Scale
- Nodes are vertical bars `12px` wide, solid `ink`, no stroke; height proportional to quantity.
- One px-per-unit constant `k` for every node and ribbon; round to `4px` at the node level so outgoing ribbons sum exactly to the bar; rounding never exceeds one `4px` step.
- Choose quantities that are multiples of `4/k` when the data is yours.
- Every column must sum to the same total; volume that leaves must appear as a named final-column node.
- Minimum ribbon `4px`; anything thinner folds into an "other" band.

## 356. Sankey Ribbons
- Filled closed ribbons, not stroked lines; both Bézier control points at the horizontal midpoint between columns (`C midX,y0 midX,y1 targetX,y1`) so bands meet bars horizontally.
- A ribbon keeps one width end to end; each flow gets its own offset range at a node.
- No arrowheads; direction comes from left-to-right order.
- Ordinary ribbons `muted @ 0.18`; the focal path `accent @ 0.28`, painted last among ribbons; never per-flow rainbow.
- Order nodes to minimise crossings; no two ribbons may cross more than once.

## 357. Sankey Labels
- Name `node-name` `12px` `600`, quantity under it `sublabel` `9px` `muted`.
- Column 1 labels outside left (`end` anchor), column 3 outside right (`start`), column 2 centred vertically in the gutter above its bar (`middle`), on clean paper with no mask.
- Column headers `eyebrow` `8px`, uppercase, tracked.
- Draw order: background → headers → ordinary ribbons → accent ribbons → bars → labels → legend; extend the canvas `~60–100px` for the legend.

## 358. Streamgraph Use
- Use to show a total and its composition breathing across many periods; `3–24` periods, `2–6` layers.
- Not for exact values, two or three periods, a single series, or rank stories.

## 359. Streamgraph Layout
- Period columns evenly spaced `x` `80 → 960` (e.g. `12` columns at `80px`), symmetric baseline at `y=230` (baseline = `−total/2`), not painted.
- One shared linear scale (e.g. `1.25px` per unit), stated with bucket size in the source line.
- Catmull-Rom boundaries at `1/6` chord with vertices on true values; never move a vertex to tame overshoot.
- Fixed stack order, largest totals innermost; `1px` paper hairlines between layers.
- Period captions `arrow-label` `8px` at `y=440`, tracked `0.08em`; no y-ticks, no gridlines; annotate at most one landmark period.
- Legend `16×8` keys with each layer's total (`Unit · 789 min`); totals equal the sum of the layer's values.

## 360. Streamgraph Colour and Honesty
- One accent layer plus ink ramp `0.78 → 0.30`, strongest on the largest; adjacent tones `≥ ~0.15` apart; no text on any layer.
- Layer names contain no digits (`End-to-end`, not `E2E`).
- Zero periods pinch to zero thickness; never bridge, resample or drop them; no layer dropped silently.
- Never use a wiggle-minimised or bottom-pinned baseline.

# Part 46 — Matrices

## 361. Heatmap Use
- Use for cross-tabulated data where one row × column combination stands out and the reader scans the whole matrix.

## 362. Heatmap Layout
- Margins: left `160px` (row labels), top `64px` (column labels), right `40px`, bottom `120px` (legend).
- Cells `116×56px`, gap `4px`; max `6` columns × `5` rows at that size; minimum cell width `80px`.
- `3–7` rows, `3–8` columns; fewer → table, more → unreadable cells.
- Row labels right-aligned at `x=148`, `sublabel` `9px`; column labels centred above, `9px`; axis titles `eyebrow` `7px` small-caps.
- Optional value text `8px` centred; flip to paper text when fill opacity `≥ 0.40`; focal text must clear `4.5:1` against the composited fill.

## 363. Heatmap Fill Ramp
- One ink ramp, monotone non-decreasing with value (e.g. `opacity = max(0.07, value ÷ max_non_focal × 0.65)`); equal values share opacity.
- Lowest non-focal cell `≥ 0.05`, highest `≤ 0.70`.
- One focal cell (`accent @ 0.85` fill, `1.2px` accent stroke), excluded from the ramp's scale, its value stated in the footnote.
- Never a hue per row/column; diverging multi-hue ramps only for signed data with a meaningful centre.
- Use a discrete LOW–HIGH ramp strip, not a continuous colour bar; footnote bounds must match actual non-focal min and max.

## 364. Heatmap Completeness
- Draw the complete rows × columns grid; a missing cell reads as zero.
- Name every row and column; note exclusions in the footnote.
- Values are finite and non-negative.

# Part 47 — Radial

## 365. Polar Chart Use
- Use for one quantitative series across `4–8` categories whose clockwise order is meaningful.
- Multiple series → radar; non-cyclic categories → bar; more than `8` ordered buckets → line.
- Never for qualitative profile wheels, negative values, log scales or unequal sectors.

## 366. Polar Encoding
- Scale minimum is exactly `0`, maximum finite and `> 0`; no donut hubs or non-zero inner baselines.
- `theta = start_angle + sign × 2π × i ÷ N` with start `−90°` (twelve o'clock), clockwise by default; `radius = R × v ÷ max`.
- Value is a ray from centre; ray length is exactly proportional to the value; no filled wedges, sectors or gradient bands.
- Zero values draw no ray and no marker but keep the spoke and print `0`; never add a minimum ray.
- Keep input order; never sort categories by value; never coerce missing to zero.

## 367. Polar Geometry and Styling
- Canvas `0 0 1000 520`, centre `(500, 230)`, `R = 160`.
- Five rings at `20/40/60/80/100%` (`r = 32, 64, 96, 128, 160`), `0.8px`, no fill; spokes centre to `R` at `0.8px`, no arrowheads.
- Non-focal rays `2px` `muted`, marker `r=4`; focal ray `2.4px` accent, marker `r=5`; markers `1.2px` stroke, constant size.
- Ring labels on the first axis only, `8px`.
- Category labels at `R + 28`, `node-name` `11px` semibold, horizontal; numeric labels at `R + 44`, `8px`, one per category, unit in the subtitle.
- Anchor `middle` within `15°` of vertical, `start` on the right, `end` on the left; never rotate labels tangentially.
- At most one focal category; the chart must read in greyscale.

## 368. Radar Use
- Use for comparing `3–5` entities across `3–5` quantitative criteria on one normalised `0–N` scale.
- More than `5` axes or series → split or use a table; `2` series → bar or table.
- Normalise every axis to the same scale; never mix non-quantitative axes.

## 369. Radar Grid
- Regular polygon, first axis at `−90°`, clockwise.
- Five polygon rings at `0.2/0.4/0.6/0.8/1.0` radius: inner four at `rule` `0.10` opacity, outer at `rule-solid` `0.20`; spokes `0.20`, no arrowheads.
- Grid starts at `0`; never start the inner ring higher to amplify differences.
- Axis labels one word, `node-name` `11px` `600`, `16px` outside the outer ring; scale ticks only on the top axis, `8px` `muted`, anchored at `cx − 6`.

## 370. Radar Series
- Polygon stroke `1.5px` with fill at `0.18` (`0.22` dark); focal stroke `1.8px` in accent.
- Vertex dots `r=4` only on the focal series.
- Draw non-focal series smallest area first, then focal, then focal dots, then legend.
- Legend `16×8` swatches, `~140px` apart; use only as many series colours as non-focal entities.

# Part 48 — Rendered Diagram Checks

## 371. Nothing Painted Past the SVG Box
- Never let strokes, markers, arrowheads or filter bleed spill outside the SVG's own box; judge by painted ink, not by element geometry, because geometry ignores stroke width and markers.
- Treat a spill as real once more than `8` pixels of new ink appear beyond a `2px` guard band, with a per-channel change above `16`; smaller differences are just antialiasing.
- Check spill at full size and at `0.25x` scale so overshoot of a few pixels and overshoot several viewports wide are both caught.

## 372. Nested Clipping Wrappers
- Never rely on `overflow: visible` on the SVG alone; a clipping wrapper around it can still cut the drawing off silently.
- Keep the chain of clipping ancestors shallow (no more than `4` levels deep) so every level can be released and inspected.
- Never place a diagram inside a scrolling ancestor; scrolled content cannot be verified for clipping and is reported as unmeasurable rather than clean.

## 373. Content Inside the ViewBox
- Keep every painted point within `2px` of the viewBox edges; anything further out is clipped, so grow the viewBox or move the content inside it.
- Never move, hide or clip measured marks with CSS (transform, display, visibility, x/y, width/height, animation, offset, clip, mask), because their painted position then stops matching their attributes.

## 374. Never Collapse an SVG
- Never ship an SVG that renders at `0` width or `0` height; a collapsed diagram is an invisible diagram.

## 375. No Sideways Page Scroll
- Keep horizontal page overflow at or under `1px` at desktop `1600×1000` and at phone `390×844`; anything more drags the whole document sideways.

## 376. Clean Runtime
- Ship with zero page errors, zero console errors and zero failed local assets; a broken reference is a broken diagram even if the rest paints.
- Measure the final, complete static frame: render with motion forced static and wait for web fonts to settle before judging layout.

## 377. Wide Diagrams on Phones
- Give any SVG wider than the viewport its own local horizontal scroller rather than letting it widen the page.
- Never let an `overflow: hidden` ancestor (such as terminal-style window chrome) cut a wide SVG off with no scroller; the content becomes unreachable and no page-overflow symptom reveals it.

## 378. Pin Min-Width to the ViewBox Width
- Set the SVG's `min-width` exactly equal to its viewBox width; a missing or smaller min-width scales the whole drawing down and drags the type ramp under every legibility floor.
- Remember the arithmetic: a `12px` node name on a `1280` viewBox pinned at `900` draws at `8.4px`.

## 379. Per-Type Legibility Floors
- Keep a waterfall SVG at least `720px` wide so its `8px` labels stay readable.
- Keep a hand-drawn (sketch-style) canvas at its full `900px` labeled width.
- Keep a marimekko at its `760px` canvas, since its `9–11px` segment labels on a `1000`-unit viewBox become unreadable at phone width.

## 380. Preview Frames
- Keep an embedded diagram preview at least `400px` tall on phones so the preview never collapses beneath wrapped controls.

## 381. Export Matches the Canvas
- Export PNGs at scale 1 exactly as wide as the viewBox; a narrower image means something scaled or clipped the drawing.
- Confirm a node placed near the right edge of the widest preset survives export; if it vanishes, an ancestor clipped the SVG during capture.

# Part 49 — Label Geometry & Collisions

## 382. Fixed Paint Order
- Paint in the order background, zones, arrows, labels, nodes; this order is what makes label overlap a defect rather than a style choice.
- Let labels overlap zone containers freely (zone eyebrows depend on it), because zones paint before labels.

## 383. Label Masks Never Under Later Nodes
- Never let a label's masking plate land partly inside a node painted after it; the node fill covers it and the text reads as a fragment sitting on the node border.
- Move a clipped label onto a free segment of its connector instead.
- Allow a mask fully inside a node only as a deliberate badge chip (EXT, EDGE, ORIG).

## 384. Shape Vocabulary
- Size a node at least `60×40` so it fits a title and a sublabel.
- Size a label mask `20–200` wide and `8–14` tall; the upper width covers long mono plates and the wider plates CJK labels need at the same glyph count.

## 385. Label Clearance
- Keep an arrow label `6–10px` clear of its connector.

## 386. Orthogonal Connectors
- Route every connector as horizontal and vertical segments (within `0.5px` of axis-aligned); turn corners as rounded right-angle elbows, never as diagonals.
- Allow radial spokes only for loop write-backs, the one documented exception.

## 387. Never Ride a Node Border
- Never run a connector along a node's edge (within `1px` for more than `4px`); it hides behind the node fill and the arrow appears to start at the corner.
- Leave a node perpendicular to the edge the port sits on.

## 388. Keep Ports Off Corners
- Keep every connector endpoint at least `8px` from a node corner, where the rounded corner makes the port ambiguous.

## 389. Fan Shared Ports
- Space two connectors leaving (or arriving at) one node edge at least `12px` apart, or `8px` on an edge shorter than `48px`.
- Exempt only a head-to-tail chain joint, where one arrow ends exactly where the next begins.

## 390. No Stacked Trunks
- Never draw two connectors within `1px` of each other along a continuous stretch longer than `4px`, straight or curved; offset one route by at least `12px` so each arrow stays traceable.
- Count forks and merges from their shared point; they may touch only at the joint.

## 391. Readable Path Data
- Write connector paths with absolute M/L/H/V/Q/C/A commands so their routing can be verified; a connector nobody can read must not pass as correct.

# Part 50 — Contrast & Light/Dark Polarity

## 392. Contrast Thresholds
- Hold regular text to `4.5:1`, large text to `3:1`, and essential non-text marks (lines, arrows, borders, data points) to `3:1` against the background they sit on.
- Exempt only decorative rules and translucent tints from a minimum.
- Measure every token in both the light and the dark skin.

## 393. Strictest Use Wins
- Hold a token used in several roles to the strictest one; accent is measured at the text bar even though most of its uses are strokes.
- Apply the same to ink, muted and link, which serve as both text and marks; soft and ink-strong are text roles.

## 394. Composite Before Measuring
- Flatten translucent colors over paper before measuring contrast; an rgba value has no contrast of its own.
- Keep paper fully opaque so it can anchor every ratio.

## 395. Text on Accent Fills
- Measure the high-contrast label color against the heaviest accent fill it sits on, accent at `0.85` alpha over paper, not against plain paper.

## 396. Classify Every Token
- Give every new skin role an explicit contrast use before it ships; an unclassified, missing or unparseable token is a defect, never a silent pass.

## 397. Tone Is a Role, Not a Color
- Remember that an ink opacity ramp composites darker as it strengthens on light paper and lighter on dark paper; one ramp reads in opposite lightness directions across skins.
- Never write a legend like "darker is larger" that is true in one skin and false in its sibling.

## 398. Name Ramps by Contrast
- Phrase tone legends on the contrast axis ("stronger contrast is larger", "fainter means smaller"); contrast against its own paper does not flip with the skin, so one sentence stays true in every variant.
- Never fix a dark variant by inverting the word; that swaps one skin-specific string for another and lets variants drift apart.

## 399. Back Every Tone Claim with a Ramp
- Draw at least `3` rank-bearing translucent fills sharing one ink color for any directional tone claim.
- Give ramp members distinct ranks and opacities that move strictly one way as rank rises; steps closer than `1e-4` in luminance or `1e-3` in contrast read as flat.
- Declare the paper color (or a full-bleed backdrop) so the ramp can be composited; an unverifiable claim is a failure, not a pass.
- Paint the accent cell in a different ink so it never joins the ramp.

## 400. Phrase Claims Checkably
- State tone claims as tone + connector + magnitude ("stronger is larger", or its mirror "larger means stronger").
- Never leave a tone word within `6` words of a magnitude word in a loose construction; either use the supported form or separate the words so the copy no longer reads as a claim.

# Part 51 — Skin/Token Discipline

## 401. Palette Only
- Use only colors from the semantic roles, series palette and terminal skin tables, plus white.
- Refer to colors by role (paper, ink, muted, soft, rule, accent) rather than by hex in prose.
- Derive every rgba value from a palette color's exact RGB triple; translucency is allowed, new hues are not.

## 402. Never Pure Black
- Never use `#000`, `#000000` or `rgb(0,0,0)`; the darkest text is the near-black high-contrast role.

## 403. Accent Budget
- Spend the accent on the focal element only, `1–2` per diagram at most.

## 404. Approved Type Families
- Use Instrument Serif, Geist and Geist Mono, with the approved serif, sans and CJK fallbacks (Noto, Hiragino, Yu Gothic, PingFang, Microsoft YaHei/JhengHei, Apple SD Gothic Neo, Malgun Gothic) and generic keywords.
- Never introduce an arbitrary family or an unapproved weight variant of a fallback.

## 405. Fonts from One Source
- Load web fonts only through a Google Fonts css2 stylesheet over HTTPS on the exact official host; look-alike hosts, other paths and protocol-relative links are refused.
- Provide an offline variant that drops the font link and falls back to system fonts.

## 406. Self-Contained Files
- Never reference external resources: no remote src or srcset, no CSS @import, no non-fragment `url()`, no image-set, no external links.
- Allow data URLs only for images.

## 407. Nothing Executable
- Never use inline event-handler attributes, `javascript:` URLs (even disguised with control characters or CSS escapes), srcdoc, or base, embed, object or iframe elements.

## 408. One Canonical Controller
- Allow at most one script, and only the reviewed motion controller copied verbatim with its single scoping attribute; any edit, second script or type override is refused.

# Part 52 — Accessibility of Diagrams

## 409. Image Role
- Give every non-decorative diagram SVG `role="img"`; each diagram file needs at least one such SVG.

## 410. Valid ViewBox
- Give every diagram SVG a viewBox of four finite numbers "min-x min-y width height" with positive width and height; commas or spaces may separate them.

## 411. Title First
- Make a `<title>` the first child of the SVG, non-empty and no more than `60` characters.

## 412. Real Description
- Include a non-empty `<desc>` that says what the diagram shows.

## 413. Labelled By Title Then Desc
- Point aria-labelledby at the title id then the desc id, and make sure both ids resolve inside that SVG.

## 414. Slug-Prefixed Naming IDs
- Prefix title and desc ids with the diagram's slug (`<slug>-title`, `<slug>-desc`); never use bare `id="title"` or `id="desc"`.
- Keep naming ids unique across the document, so multiple diagrams on one page never steal each other's names.

## 415. No Leftover Placeholders
- Resolve bracketed template placeholders before shipping; only an unfilled template may keep `[diagram-slug]-title` and `[diagram-slug]-desc`.

## 416. Decorative SVGs
- Mark purely decorative SVGs (icons, ornaments) `aria-hidden="true"`; they are then exempt from naming rules, and a nested icon belongs to its parent diagram.

## 417. Unique IDs Everywhere
- Never duplicate an id anywhere in the HTML or SVG.

# Part 53 — Motion Checks

## 418. Motion Is Optional and Bounded
- Pick one mode: none, reveal, step or loop, on exactly one motion root.
- Declare a step count from `1` to `8` (`0` allowed only for none) as a plain decimal integer.
- Limit a diagram to `12` motion items.

## 419. Contiguous Steps
- Number semantic steps contiguously from `1` to the declared count, never outside it.
- Put no more than `2` semantic items on one step.

## 420. Accessible Motion Items
- Give every semantic motion item an aria-label that does not depend on color.
- Mark decorative motion items `aria-hidden="true"` and `focusable="false"`.

## 421. Visible by Default
- Never hide motion items in source; the static fallback must be complete and visible with JavaScript off.
- Hide items for animation only under the progressive-enhancement class, added after the first render succeeds.
- Include a noscript note explaining the complete static frame.

## 422. Loop Mode Stays Minimal
- Keep loop mode script-free with no playback controls or live status.
- Allow at most one semantic item and one decorative token in a loop.
- Scope any infinite animation to loop mode only.

## 423. Full Controls for Controlled Modes
- Give reveal and step modes one in-root control group with play, pause, replay, previous and next.
- Add a live status with `role="status"`, `aria-live="polite"` and `aria-atomic="true"`, placed outside the control group.

## 424. Fallbacks
- Provide a reduced-motion fallback that hides controls, a print fallback, and a deterministic static override for screenshots.
- Report "playback controls unavailable" in static and reduced-motion states.

## 425. Keyboard and Background Behavior
- Support arrow keys to step, Space to play/pause, Home to reset and R to replay, ignoring presses with Ctrl, Meta or Alt held.
- Pause when the tab goes to the background.
- Stop immediately on the final step.

## 426. Deterministic Timing
- Time motion with single timeouts; never use repeating intervals or randomness, so every frame is reproducible.
- Validate any requested test frame as a non-negative safe integer no larger than the step count, and wait for fonts before capture.

## 427. Semantic Pattern Before Visual Type
- Choose the semantic pattern first, then the visual type; patterns never expand the visual-type taxonomy.
- Give each pattern selection triggers, required primitives, a complexity budget, anti-patterns, a static fallback and the nearest visual type.

## 428. Policy Evaluation Traces
- Show trace outcomes as text states (PASS, FAIL, SKIPPED, NOT REACHED, FIRST DIVERGENCE), never by color alone.
- End the persistent trace connector exactly at the first FAIL, before the not-reached rows and the denied outcome.
- Run a two-trace policy comparison in step mode with exactly five semantic steps.

# Part 54 — Architecture Containment & Delta Rules

## 429. Two Scope Kinds
- Draw admin bands as horizontal rectangles with `rx=4` and a dashed stroke.
- Draw traffic boxes with `rx=8` and a solid stroke.
- Include at least one admin band and at least one traffic box.

## 430. Containment Budget
- Limit a containment diagram to `2` admin bands, `4` traffic scopes and `8` nodes.

## 431. Node Kinds and Placement
- Classify each node as compute, endpoint or managed.
- Place managed (PaaS) nodes in an admin band, never inside a traffic scope.
- Place compute and endpoint nodes inside a traffic box.
- Point every endpoint at a managed node; only endpoints may carry a target.

## 432. Innermost Parent
- Parent every scope and node to the innermost scope that geometrically encloses it; only the outermost scope may omit a parent.
- Never form parent cycles, and keep each child fully inside its parent's bounds.

## 433. Sibling Axes
- Lay sibling traffic scopes on one shared axis without overlap.
- Turn nested children perpendicular to their parent's axis (rows inside columns, columns inside rows).

## 434. Peerings
- Join exactly two distinct traffic scopes with each peering.

## 435. 4px Grid
- Put every scope and node bound on the `4px` grid.

## 436. Literal Geometry
- Draw bounds as plain rects with real x/y/width/height; never move checked elements with transforms, moving CSS, nested SVG viewports, stylesheet overrides or geometry animation.

## 437. Before and After Panels
- Show exactly two snapshots, before and after, side by side left-to-right on one baseline, with matching grid width, height and pitch.
- Move panels only by a single translation; never transform the objects inside them.

## 438. Change Statuses
- Mark every object unchanged, added, removed, changed, moved or rewired; unchanged, added and removed are exclusive.
- Mark after-only objects added and before-only objects removed.
- Mark changed if and only if the signature differs, moved if and only if the local position differs, rewired if and only if endpoints differ; a size change requires changed.
- Never change a retained object's kind.

## 439. Delta Relationships
- Make every relationship endpoint resolve to a component in the same snapshot and visibly meet its perimeter within `2px`.
- Include at least one relationship.

## 440. Delta Budget
- Limit a delta to `8` unique components and `10` unique relationships.

## 441. Change Ledger
- List `1–8` ledger entries as visible text outside both snapshots.
- Begin each entry with its uppercase change word and explain it.
- Cover every change exactly once; no missing and no unexpected entries.

## 442. Nothing Hidden
- Never hide snapshot objects or ledger entries, and never put them in non-rendering containers.

# Part 55 — Exploded & Axonometric Geometry

## 443. Projection Is the Truth
- Project every part with iso(x, y, z) = [x − y, (x + y)/2 − z], and keep every silhouette vertex within `0.05` of its declared box's projection.
- Draw projected rounded corners as `2:1` ellipses (radius r becomes `r√2 × r/√2`) with arc flags `0 0 1`.

## 444. Levels Explode Together
- Use at least `2` parts, number levels `0` to n−1, put all parts of a level at one z, and keep the bottom level at `z = 0`.

## 445. Equal, Generous Gaps
- Keep every gap between levels equal to the declared gap.
- Make the gap at least the larger of `0.5×` the top-face height and `3×` the thickest non-container part.

## 446. Leaders
- Run every leader horizontally from its part's right extreme, never crossing another part.

## 447. Exploded Labels
- Give each part exactly one label of one or two words.
- Align labels in one column at least `36px` apart.

## 448. One Focal Part
- Put the accent on exactly one part, room or building.

## 449. Trace Lines
- Draw trace lines vertical and dashed.

## 450. Position Comes from Geometry
- Never use SVG transforms or CSS transforms anywhere in a projected figure; static parts carry no style attribute.
- Animate a part only through a single lift value equal to its exploded z minus its closed z.

## 451. Plan Boxes on the Plate
- Stand every wall, furniture piece, building or tree on the plate top, inside the plate, with no overlapping footprints; tree canopies sit `8` above the plate on their trunk.
- Paint boxes back to front; never draw a box after one in front of it.

## 452. Plan Tags
- Center each tag on its declared plan point, drawn `16px` above its projection, with the point inside the room or on the roof it names.
- Give each room or building exactly one tag of one or two words, matching its name, and never overlap tags.

# Part 56 — Service Blueprint Rules

## 453. Layer Order
- Stack layers top to bottom: optional evidence, customer, frontstage, backstage, optional support.
- Require customer, frontstage and backstage; never duplicate or reorder a layer.

## 454. Line of Visibility
- Draw exactly one horizontal visibility line across the plot, between the frontstage bottom and backstage top within `±2px`.
- Keep every evidence, customer and frontstage cell above it, and every backstage and support cell below it.
- Give the line at least `3:1` contrast against paper after combining rgba alpha, stroke-opacity and opacity.

## 455. Shared Stage Grid
- Keep every cell inside its stage header's column, left and right edges.
- Make columns equal width and gutters equal and non-negative.

## 456. Census
- Give every stage a customer, frontstage and backstage cell; mark a deliberately empty cell "—" or "Not applicable".

## 457. Focal Discipline
- Mark at most one focal cell, and paint no other row mark in the accent.

## 458. Blueprint Budget
- Limit a blueprint to `6` stages and the canonical layers only.

## 459. Print-Readable Cells
- Make each cell's visible text contain its own name, so the meaning survives print.

## 460. Static Marks
- Never move or resize cells, headers, rule lines or text with transforms or CSS; state positions and sizes as attributes.

# Part 57 — Sequence Diagram Rules

## 461. Return Arrows
- Draw ordinary returns dashed; reserve the accent arrowhead for the single headline success return.
- Use an open arrowhead for asynchronous messages.

## 462. Combined Fragments
- Frame an ALT with one visible operator tab and two regions split by one dashed divider.
- Label regions with visible bracketed guards, such as `[token valid]` and `[else …]`.

## 463. Bound Response Labels
- Bind each response label in the failure region to a real return arrow directly beneath it; legend samples never stand in for story messages.

## 464. Activation Bars
- Draw activation bars `8` wide on the lifeline, spanning from the initial call through the headline success return.

## 465. Text Positioning
- Let guard and label spans inherit their parent text position; never reposition spans or override SVG geometry or paint in CSS.

## 466. Sequence Budget
- Limit to `5` lifelines, `12` messages, `1` combined fragment (`2` only if each is a single-region opt or loop), `2` alt regions, nesting depth `1`, and `2` accent elements (prefer `1` with fragments).
- Split over budget into an overview (happy path) and a detail (failure or refresh path).

## 467. Simple Paths Stay Simple
- Keep a plain happy-path sequence free of fragment tabs.

# Part 58 — Self-Review Checklist

## 468. Whole Document
- Confirm the file ends with `</html>`, contains no U+FFFD replacement characters, closes every container tag it opens, and never leaves a raw-text element open.

## 469. Safety Pass
- Confirm no remote assets beyond the approved font stylesheet, no executable attributes or URLs, and no script other than the canonical controller.

## 470. Accessibility Pass
- Confirm every diagram SVG has role img, a first-child title, a non-empty desc, slug-prefixed unique ids and aria-labelledby naming title then desc.

## 471. Geometry Pass
- Confirm painted content stays inside each viewBox, with nothing moved by CSS.

## 472. Motion Pass
- When motion is present, confirm one root, a valid mode, the step and item budgets, visible fallbacks, and the complete control and status set for controlled modes.

## 473. Offline Pass
- When the diagram must work offline, remove the font link and confirm it reads in system fonts.
