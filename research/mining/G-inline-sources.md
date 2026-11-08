# G: rules mined from the 13 sources read in full (impeccable, diagram-design, ux-ui-agent-skills, krehel, transitions-dev, taste-vault, design-taste, writing-guidelines, web-interface-guidelines, dsh, Design Rules 1, Design Rules 2, Concepts and rules)

## Named tests and methods
| Test | How | Pass | Source |
|---|---|---|---|
| Squint test | Blur the render | Primary, secondary and groups still identifiable in order | impeccable §62 |
| Template / rival-name swap | Swap product name for a competitor's | Something becomes false | impeccable §149, design-taste §6 |
| Memory test | Leave after first viewport | Visitor can describe a thing, not a mood | impeccable §225 |
| Skeleton test | Strip copy from the section | Structure alone says what it is and why it matters | impeccable §290 |
| Removal test | Remove the effect | Someone notices it gone | impeccable §324 |
| 50th-use test | Imagine 50th use today | Animation still wanted, else cut | Design Rules 1 §2 |
| Frequency gate | Classify interaction frequency | 100+/day: no motion; tens: ≤150ms opacity; occasional: standard; rare: delight | Design Rules 1 §2 |
| Second-read test | Read at speech pace once | Every sentence parses first time | writing-guidelines §18 |
| "By monkeys" test | Append "by monkeys" to the verb | If it still parses, passive: rewrite | writing-guidelines §10 |
| Model-as-reader test | Give a model only the page + goal | It can complete the task | writing-guidelines §86 |
| 8-second read | First third, no scroll | What / who / do answered | design-taste §39 |
| Pre-flight "default agent" kill question | Could typing "landing page" into an agent produce this? | No | design-taste §6, §62 |
| Block coherence test | Drop new block beside existing one | A stranger can't tell they were authored separately | ux-ui-agent-skills §32 |
| Render-and-click | Screenshot every state both themes, click every control | Every declared state changes something visible | ux-ui-agent-skills §7 |
| Seeded-defect proof | Plant a known defect | Every check rejects its seed; include a positive control | ux-ui-agent-skills §262 |
| Remove test (diagram) | Can any node/arrow/label be removed or merged? | No | diagram-design §5 |
| Diagram-earns-its-place | Would a paragraph or table teach as much? | No | diagram-design §4 |
| Reproduction diff | Screenshot build at comp size, compare region by region | Named largest divergence; fidelity ≥0.72 first viewport | impeccable §497-499 |
| Variant judging | One at a time, full size, real neighbours, real data | Never thumbnails, no pre-picked favourite | krehel §115, Design Rules 1 §25 |
| Diff review classification | Classify each finding | Introduced / Regression / Pre-existing (≤3 courtesy) | krehel §112 |
| Stress matrix | Content length × shape × quantity × container × state × environment | Nothing visibly breaks | krehel §113 |
| Cognitive load checklist | 8 checks (single focus, chunking ≤4, grouping, hierarchy, one decision, ≤4 options, working memory, disclosure) | 0-1 fails low; 2-3 moderate; 4+ critical | impeccable §424 |
| Heuristic scoring | Nielsen 10 at 0-4 | Bands 36-40 excellent … <12 critical; n/a allowed with reason | impeccable §427-428 |
| Persona walk | 2-3 of: power user, first-timer, a11y-dependent, stress tester, distracted mobile | Specific red flags named | impeccable §440-446 |
| Before/after ritual | Same prompt with and without guidance, same viewport | Guidance is the only variable | design-taste §94 |
| Fair comparison | Freeze brief, refs, assets, model settings | Never declare a universal winner from one output | taste-vault §83 |
| Too-close / too-generic repair | Reopen refs vs render | Name the combination that makes them alike, or 3 principles missed | taste-vault §17 |

## Highest-value rules (by domain)

### Concept / direction (D02, D20)
- Choose visitor mode per surface: Persuade, Operate, Read, Experience; ambition scales to the mode (impeccable §10-14).
- Name the rut (the page this category always ships + its predictable opposite); both excluded (impeccable §180).
- Derive 7 candidates from the audience's world spanning ≥3 material families; tools-as-costume banned on Operate/Read (impeccable §181-182).
- Direction contract: THESIS, OWN-WORLD, STORY, FIRST VIEWPORT, FORM, FINISH (~150 words); never shipped in the artifact (impeccable §204-205).
- Every look needs one bold move; without it the aesthetic drifts generic (taste-vault §3).
- Distill each reference to its single most stealable idea; never transfer subject+palette+placement as a package (taste-vault §1, §11).
- Decision block before UI: Domain, Audience & tone, Mood (one adjective), Motion depth, Layout family, Reference anchor; vague values ("clean") are non-decisions (ux-ui-agent-skills §9).
- Generic-look calibration: four clusters (cream+serif+terracotta; near-black+neon; broadsheet hairlines+italic serif+mono labels; flat ink+hard offset shadows) legitimate only when the brief calls for them (impeccable §200).

### Slop tells with numeric definitions (impeccable Part 56-63)
- Side-tab border: ≥2px on one side when others ≤1px, on ≥4px radius card; square box ≥3px (§552).
- Icon tile above heading: 32-128px square, tint ≥0.05 alpha or border (§560).
- Eyebrow/kicker: ≤14px (≤45% heading, ≤16px), tracked ≥0.06em, over h1-h4 ≥20px (§520).
- Numbered section labels: ≥2, ≤13px beside headings ≥1.3× (§521).
- Hero eyebrow chip: ≤14px tracked ≥0.08em above ≥48px headline (§519).
- Italic serif hero h1/h2 ≥48px (§514). Oversized sentence headline: ≥40 chars at ≥72px filling ≥28% viewport height (§515).
- Violet hue 260-310° on headings/large text sat ≥0.3; purple-to-purple gradients (§527). Cyan-on-dark neon hue 170-197° sat ≥0.4 (§529).
- Cream surface: all channels ≥209, R≥G≥B, R−B 6-48 (§532).
- Glow: zero-offset chromatic halo; visible when blur×alpha ≥3px (§533). Radial spotlight ≥0.14 alpha & ≥1.30:1 (§536).
- Monotonous spacing: >60% of values one 4px-rounded value, ≤3 distinct across 10+ (§540).
- Heading rhythm: ≥2 headings closer to block above than their own content (§541).
- Repeated label: same literal text ≥3× in one card (§510). Em-dash saturation ≥8 at ≥1 per 500 chars (§508). Aphoristic cadence "X. No Y." ≥3 (§507). "… theater" framing (§509).
- Flat hierarchy: dominant sizes <1.25× apart with ≥3 roles (§513).
- Hairline border + wide shadow (≥32px) on every card in a row of ≥3 (§561).
- Shape-assembled illustration: ≥200px, ≥8 primitives, ≥3 fills (§571).
- Pulsing status dot 2-16px looping (§564); blinking cursor in hero first 1200px (§565); marquee (§566).
- Organic clip-path ≥10 vertices or curved path (§567). Buried raster under ≥0.9 alpha wash or <0.15 opacity (§568).
- Default agent baseline: Inter only, linear-gradient(135deg,#6366f1,#8b5cf6), violet radial glow, scattered radii 6/8/10/12/16/24/pill (design-taste §5).
- Slop screen anatomy: 4 equal stat cards repeat(4,1fr), emoji stat icons, #9ca3af labels on white, single 8px radius, same 0 4px 6px shadow, fixed 1100px container, h1 1.7× body, gradient primary + indigo "Delete Account" (ux-ui-agent-skills §28).
- Concepts list tells: tags & pills, excessive italics, Instrument Serif, negative kerning, over-detailed UI, overused dividers, colour shades/opacities, bordered containers, over-detailed diagrams, verbose text, code breadcrumbs, section numbering, eyebrows, dithering, ASCII images, squircles, excessive mono, ALL CAPS subtitles, gradient backgrounds, periods in titles (Concepts and rules).
- 2026 trend list to treat as "spent looks" not bans: dithering, ASCII over video, infinite canvases, disco logos, Renaissance branding, Monet backgrounds, dark gradient heros, pixel loaders, one italic word, cream bg, all-caps eyebrows, pulsing live dots, sparkle icons, liquid glass, three icon cards, decorative flowcharts, endless marquees, squircles, pretext wrapping (Concepts and rules).

### Typography
- Body measure 65-75ch (≤80 fail); reading text leading ≥1.3, body 1.5-1.7; lead 20-23px ≤3 lines ≥1.15; caps labels ≥1.0 (impeccable §522).
- Display ≥40px may track to −0.09em; reading copy never below −0.07em; body tracking ≤0.05em (§516-517).
- All-caps runs ≥80 chars banned (§518). Justified text in ≤45-char columns without hyphenation banned (§523).
- Weight floors: <18px use ≥400; 100-300 only ≥28px (krehel §32). Rare >3 fonts (§31).
- Starter scale: Display 36/1.1/600, Title 24/1.2/600, Heading 18/1.3/600, Body 16/1.5/400, Caption 13/1.4/400 (krehel §33).
- Display ≥2.5× body; ≥2.0× minimum (ux-ui-agent-skills §20). Never `text-transform` for content case; store natural case (krehel §42).
- `text-wrap: balance` headings (≤6 lines), `pretty` body; straggler <30% width in ≥30-char column flagged (impeccable §576-577).
- Inputs ≥16px on mobile; never disable zoom (krehel §44, web-interface §11-12).
- Light text on dark: +leading, +tracking, +1 weight step; long copy 1.65-1.8 (impeccable §52).
- Thai leading per font (Sukhumvit ~1.35, Anuphan ~1.43, Noto Sans Thai ~1.49); never negative tracking on Thai; nowrap names/counts (ux-ui-agent-skills §57).

### Colour & surface
- Ramp role steps 1-12 (page, subtle, component, hover, active, subtle border, border/focus, hovered border, solid, solid hover, low-contrast text, high-contrast text); solid fill one step darker than mid (krehel §52).
- Ramp construction: lightness steps 0.04-0.05 L light end, 0.07-0.10 mid; drop steps closer than 0.03 L; never pure black/white ends (krehel §53).
- Status hues ≥15° from accent; "one colour one meaning", anything within 15° counts as same (krehel §57, §61).
- Contrast fix order: change L first, hold hue; pick text polarity by measuring both; crossover ~56% OKLCH L (krehel §65).
- Increased contrast: widen gap ≥0.15 L, aim Lc 90 body (krehel §67).
- Gradient interpolation: oklab default, add middle stop for opposite hues; noise for banding (krehel §68).
- APCA levels: Lc 90 body preferred, 75 min body, 60 non-body content, 45 large/headlines/fine icons, 30 spot text/solid icons, 15 non-text (web-interface §197).
- Destructive never wears primary; affirmative never wears danger; same destructive label same accent everywhere (ux-ui-agent-skills §17, §61).
- Shadows: ≥2 layers (ambient + direct); light: 1px ring + lift + ambient; dark: single white ring 0.08/0.13; keep transparent 1px border for forced colours (krehel §10, web-interface §76).
- Image outline 1px inset −1px at 10% pure black/white, never tinted (krehel §11).
- Elevation declared once: border OR shadow; card radii 12-16px (impeccable §25). Concentric radius outer = inner + padding (+border) (krehel §8).
- DSH per-style locks: radius ranges (0 brutal, ≤4 deco, 8-12 dark SaaS, ≥16 bento/soft, 20 glass); effect caps (glass ≤60% area, neumorphic ≤40% elements, gold <15%) (dsh §2).
- Signature style checklist: chromatic budget, accent rule, surface rhythm, shadow/corner/border policy, emphasis mechanism, type roles, signature detail, prohibitions, interaction physics, tone (Design Rules 2 §83).

### Layout & composition
- One thing leads per view; never four equal stat cards or three equal plan cards (ux-ui-agent-skills §21, §30).
- Variance mandate: adjacent sections never share column structure + alignment; archetypes bounded hero, asymmetric split 7/5, bento, editorial stack, offset, band, index list (§31).
- Screen economy: media ≤60vh; card >35% viewport must be ≥30% filled; h1 + primary action visible at 390×844; images ≤500KB/page; no infinite decorative animation (§33).
- Narrow defences: inputs `inline-size:100%; min-inline-size:0`; `minmax(min(Npx,100%),1fr)`; `overflow-wrap:anywhere` for tokens; reset list padding (§36).
- No horizontal overflow at 280-951px incl. 1.25× root font; foldable widths 382/385/594/669/951 (§35, §37).
- Spacing: outer > inner always; gap between groups ≥2× within (krehel §72); ≥8px between controls; 12px bordered controls, 24px borderless glyphs (krehel §78).
- Peek 16-32px past scroll edge to hint hidden content; name disclosure contents (krehel §77).
- Bento: no dead cells; tiles dense or don't bento (ux-ui-agent-skills §47, taste-vault §4).
- Body text ≥16px from viewport edge (≥12px ≤480px) (impeccable §543-544). Cramped padding: inset ≥max(8px, 0.5×font) horizontal (§545).
- Unbalanced first-viewport columns flagged (§549).
- Section spacing 96-160px (design-taste §23); hero headline clamp(3rem,8vw,7rem) leading 0.95-1.05 (§9).
- Landing: 8-second read, selling sequence (hero, proof, problem, mechanism ≤3, proof, how ≤3 steps, pricing ≤3 tiers middle highlighted, close), one primary CTA per viewport, same CTA label hero and close (design-taste §39-42).

### Components & states
- Eight states: default, hover, focus, active, disabled, loading, error, selected; read-only and filled for inputs (ux-ui-agent-skills §92).
- Loading: show-delay 150-300ms, min visible 300-500ms; skeleton mirrors final layout (web-interface §26-27).
- Submit stays enabled until submit; then aria-disabled + spinner beside label + idempotency key (web-interface §35, krehel §92).
- Destructive confirm: title asks, button answers with verb+object, type-to-confirm for high stakes, default focus safe option (ux-ui-agent-skills §116).
- Undo for frequent reversible actions; confirm only irreversible/affects others/many items (krehel §108).
- Toasts: success/info 4-6s, errors persist, max 3, pause on hover/focus, never move focus (ux-ui-agent-skills §129).
- Native select ban (ux-ui-agent-skills §26) — CONFLICT with web-interface (native first). Resolve: allow native; flag only if unstyled chevron misfit.
- URL as state: filters, tabs, pagination; push for navigation, replace for typing (web-interface §207-209).
- Hit targets 24px min, 44 touch; prediction cones on submenus; tooltip group delay then instant (web-interface §8-10, §17).
- Kanban/flows: from diagram-design for diagram types only.

### Motion
- Easing: entering/exiting ease-out; moving ease-in-out; hover ease; constant linear; never ease-in on UI. Strong curves: out cubic-bezier(0.23,1,0.32,1), in-out (0.77,0,0.175,1), drawer (0.32,0.72,0,1) (Design Rules 1 §4).
- Durations: press 100-160ms, tooltip 125-200, dropdown 150-250, modal/drawer 200-500; UI <300ms; exits ~20% faster (Design Rules 1 §5); transitions-dev: close ≈60-70% of open; tokens 150/250/350/400/500.
- Never from scale(0); start 0.9-0.97 + opacity; origin at trigger; modals centred (Design Rules 1 §6). Press scale 0.96-0.97, never <0.95 (krehel §17, transitions-dev §83).
- Choreography roles Lead/Support/Decoration/Static; one entrance per container; product stagger 30-80ms, ≤~300ms total, first ~6 items; marketing 100-150ms (Design Rules 1 §11).
- Remove: hover lift on non-primary cards, infinite pulses/shimmers/orbs, spinners for <300ms ops, in-app route transitions (Design Rules 1 §14).
- Use-case mapping before tokens: match usage not nearest number (transitions-dev §1, §15).
- Pre-scale <0.9 or translate >40px (non-panel) = off-scale (transitions-dev §12-13). Blur 2px default cross-blur; never on plain fades/theme changes (§14).
- Suppress all transitions during theme swap (krehel §26). Skip state animations on first load (§24).
- Springs: critically damped by default; bounce 0.1-0.3 only with momentum; dismiss on velocity >~0.11px/ms (Design Rules 1 §9-10).

### Accessibility (web-interface-guidelines is canonical)
- ARIA authoring patterns per component (accordion, alert, alertdialog, breadcrumb, button, carousel, checkbox, combobox, dialog, disclosure, feed, grid, link, listbox, menu, menubutton, meter, radio, slider, spinbutton, switch, table, tabs, toolbar, tooltip, tree, treegrid, window splitter) with keys, focus, ARIA, pitfalls (§113-141).
- Landmarks ≤7, labelled when repeated, role name not in label (§142-151).
- Pause/stop/hide for motion >5s; flash ≤3/s; auto-update needs control with no grace (§161-165).
- Single-pointer alternative to every drag (2.5.7) with pattern list (§153-154).
- Inert regions need visible cue (§177-178). Safe-area env() with fallbacks (§180-181).
- Automated scanners catch ~30-57% of issues; manual protocol mandatory (ux-ui-agent-skills §185).

### Copy
- Writing-guidelines MUST rules: active voice, "you", imperative steps, present tense, sentences <20 words, paragraphs 2-4 sentences, TL;DR first, define terms on first use, spell out acronyms, descriptive subheadings (flag Overview/Caveats/Notes), sentence case headings, lists from 3+ items introduced with colon, snake_case placeholders, `64 KB` units, numerals, curly quotes, `…`, nbsp in units/shortcuts, bold only for UI elements or critical facts, descriptive anchors, no hard wrap, no `---` (writing-guidelines).
- Content types: Tutorial / How-to / Reference / Conceptual / Troubleshooting / Landing; one page one job; goal verb from Bloom's levels (§4, §7).
- Tone by stakes: warm on success/onboarding; neutral routine; calm plain errors; serious data loss (krehel §100, ux-ui-agent-skills §198).
- Status copy: "Saving changes…" → "Changes saved" → "Changes not saved. Check your connection and try again." → partial "9 of 12 uploaded. Retry 3 failed" (krehel §110).
- Toggle labelled for ON state; no "we" in errors; match "tap/click/select" to input (krehel §101-106).
- Copy voice (impeccable §149-155): verbs lead, vary sentence length, take a position, name numbers ("54 KB" not "lightweight"), banned diction list, negation pivots, triads, uniform paragraph length, stacked hedges.

### Data viz & diagrams (diagram-design canonical)
- Budgets: ≤9 nodes, ≤12 arrows, ≤2 accents, ≤2 callouts; detail levels faithful ≤24 zoned / balanced ≤12 / simplified ≤7; degrade ladder fixed order (§57-62).
- Connectors orthogonal r=8 elbows, ports ≥8px from corners, fan ≥12px apart, never shared attach point, bridge less important at crossings, no transit behind non-endpoint boxes (§36-40).
- Labels ≤14 chars caps on masks 6-10px clear; legend strip at bottom (§51-53).
- Chart honesty: one linear scale, never truncate magnitude axes, round once and draw from the rounded number, disclose omissions, never coerce missing to zero (§298-301).
- Bubble area ∝ value (r = K√v) (§324); ridgeline one amplitude for all (§334); waterfall carries and exact reconciliation (§351-353); sankey columns sum equal (§355).
- Skin-neutral legend wording: "stronger contrast is larger", never "darker is larger" (§297, §397-398).
- Fidelity ledger on every redraw: source count, drawn count, merges/drops (§63, §154).
- Rendered checks: no ink past SVG box (>8px beyond 2px guard), min-width = viewBox width, ≤1px page overflow at 1600 and 390, zero console errors (§371-381).

### Imagery
- Medium follows the pixels: figures, objects, textures, perspective illustration ship as raster; text, controls, diagrams as code (impeccable §215).
- Image provenance recorded for every raster (§216). Plates ≥1.5× region size, native alpha, never chroma-key (§492-494).
- Image recipe: lock style, subject as slot, STRICT palette clause, exclude text/logos/UI, specify focal + mobile crop (taste-vault §20).
- Icon stroke matches text weight: 400 → 1.5px, 500-600 → 2px, 700 → 2.5px rendered; one library per surface; outline default, fill for active (krehel §12-13).
- RTL icon flips: back/forward, chevrons, list glyphs, send; never logos, checkmarks, clocks, media playback (krehel §15).

### Robustness
- Worst-case data matrix: long/short/missing/one-letter/non-Latin names, emoji, RTL, unbreakable URLs, +30% translation, counts 0/1/1000+ (Design Rules 1 §19).
- Truncation strategy: wrap identifying text; end-truncate metadata; middle-truncate paths/hashes; never truncate numbers, amounts, dates; always a way to full value (Design Rules 1 §20).
- Mobile web native feel: hover gated (hover:hover)(pointer:fine), 100dvh shells / 100svh heroes never 100vh, touch-action manipulation, overscroll contain, theme-color, inputmode/enterkeyhint (Design Rules 1 §21).
- Performance: budget 8ms/frame at 120Hz; profile on mid-range phone; virtualise >50 items; content-visibility auto + contain-intrinsic-size (Design Rules 1 §15, web-interface §186-188).

### Media from inline sources
- iOS: tab bar 2-5 sections; never block edge-swipe back; 44pt; Body 17pt, 11pt floor; SF Symbols; semantic system colours; Dark Mode first-class (impeccable §377-383).
- Android: nav bar 3-5 at compact, rail/drawer expanded; predictive Back; 48dp +8dp spacing; Material roles; sp; Dynamic Color w/ fallback; one FAB (§384-390).
- Print adaptation: page breaks at logical points, remove nav, expand URLs, page numbers/print date (§362). Email 600px, inline styles, tables, button CTAs (§363).
- Docs content types and pricing pages: tables, every limit documented in one all-limits table (writing-guidelines §72-75).
