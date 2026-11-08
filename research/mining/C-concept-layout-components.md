# C — Concept & taste / Layout & composition / Components, states & flows

Sources: hallmark (HM), taste-skill (TS), huashu-design (HU), kami (KM), ui-ux-pro-max (UX), awesome-design-patterns (ADP), agent-skills (AS). Section numbers are `§N` inside each file.
Reference viewport is 1440x900 unless a row says otherwise.

---

## D02 Concept & taste

### Brief reading, kind and job
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CON-001 | Classify the business kind before any design decision; write down kind, what is sold, buyer, the one main action, and the real material on hand | Kinds: software, gaming, tech hardware, product, service, place (+ "other") | Reflex | J | TS §5, UX §229, UX §454 |
| CON-002 | Name the visitor's job and build from where real sites in that category put the action, which sections they are built around, and how they end | Jobs: subscribe, book, visit, attend, buy, try, sign up, hire, join, listen | Reflex | J | HM §17, HM §203 |
| CON-003 | Treat a maker that opens its door or teaches as a place (its web shop becomes a goods section); estate/travel/insurance agents are services, never AI product | — | Reflex | J | TS §5 |
| CON-004 | Infer genre from the brief: AI/generative/music/video/voice/dark → atmospheric; SaaS/API/infra/B2B/dev tool → modern-minimal; playful/kids/games/community → playful; else editorial. When two non-default genres fire, offer one either-or or pick and say so | 4 genres | Reflex | J | HM §8, HM §240-243 |
| CON-005 | Read a vague tone word ("modern", "clean") through the genre; never ask about it, and never accept "clean and modern" as a tone | Tone must be an extreme: editorial, brutalist, soft, utilitarian, luxury, playful, technical, austere + 4-8 word vibe | Reflex | J | HM §6, HM §235 |
| CON-006 | Detect scope: one named element ("just the X") is a component; a screen someone works in is an app screen; ambiguous "a pricing section" defaults to component after one question | — | Reflex | J | HM §9, HM §142 |
| CON-007 | Choose the style family by output shape, not subject (clickable site → web; paged → slides; standalone data image → infographic; app → app; 3:4 posts → social) | Dashboard prototype = web; data page in a deck = slides | Reflex | J | HU §207, KM §207-208 |
| CON-008 | Inventory material before shape: list Real (every supplied name, number, place, date, image), Pictures (what is shown and its source), Absent (every proof the page will not have) | 3 lists | Reflex | J | HM §7, HM §236, KM §143 |
| CON-009 | Let the inventory pick the shape: a page with pictures leads with them; a page of words carries type and facts (long document, letter, index-first, manifesto) | — | Reflex | J | HM §7, HM §236 |
| CON-010 | Ask once (one message, max 3-4 questions): material, audience, use (one action), tone; skipped fields are opt-outs to infer and state in one line | ≤3 questions (HU), 4 fields (HM) | Reflex | J | HM §6, HU §43 |
| CON-011 | Never infer facts: a number, quote or logo not given is absent; a picture not given is a stand-in in a replaceable slot | — | Floor | H | HM §6, HU §9 |
| CON-012 | Before asking, read what exists (locked design system, brand spec, fonts, palette, spacing, motion libs, framework); a locked system overrides every other choice | — | Reflex | J | HM §5, HU §5 |
| CON-013 | Declare one content type per page/document and give each page one job (tutorial, how-to, reference, conceptual, troubleshooting, landing) | 1 type per page | Reflex | J | AS §102-103, KM §207 |
| CON-014 | Answer the five form questions before each page/screen/shot: narrative role, viewer distance, visual temperature, capacity (three thumbnails), unique visual motif | 10cm phone / 1m laptop / 10m projection | Reflex | J | HU §16 |
| CON-015 | Match density to the product: AI/data/context-aware products (dashboards, trackers, copilots) show ≥3 differentiated content-bearing facts per screen; others default restrained | ≥3 facts/screen | Reflex | J | HU §16, HU §181 |

### Direction, specificity and boldness
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CON-020 | Commit the whole plan before markup: shape, direction, chrome, hero, signature, sections, material, stated once as a compact summary | Stop narrating after the 2nd restatement | Reflex | J | HM §10, TS §6 |
| CON-021 | Treat a visual direction as material (palette balance, type voice, surfaces), never as content or order; two briefs in one direction must yield two different pages | — | Reflex | J | HM §11 |
| CON-022 | Give every page one signature: the brief's strongest real thing at its best, on the first screen; on an app screen it is the object the tool is known by (ledger, timeline, queue) | 1 per page, first screen | Reflex | J | HM §13, HU §7 |
| CON-023 | A number drawn as marks, a greeting over four stat cards, or a gradient garnish is not a signature | — | Reflex | J | HM §13, HU §158 |
| CON-024 | Spend boldness in one place: one detail at 120%, the rest at 80%; take one accessory off before shipping | 1 bold move | Reflex | J | HU §7, HU §181, TS §99 |
| CON-025 | Let one idea run the page top to bottom; an idea that stops at the hero is a template with a good hero | — | Reflex | J | HM §15, HM §158 |
| CON-026 | Summarise a direction as an Idea (one sentence) and a Look (ground, ink, accent, faces, each with its source); if the idea cannot be stated in one sentence there is none | 1 sentence | Reflex | J | HM §15, HU §97 |
| CON-027 | Write one line at delivery on where the form grew out of the content; the motif must be something only this subject has | 1 line | Finish | J | HU §6, HU §52 |
| CON-028 | Go wide then choose: sketch three directions as far apart as possible (two lines each), build the one a design lead would fight for, never the safest | 3 directions; HU: 6 candidates → 6 thumbnails → 3 | Reflex | J | HM §15, HU §41, HU §47 |
| CON-029 | Make direction differences land in layout structure and information organisation, never only palette/fonts (reskins fail) | Skeleton edge-map correlation >0.55 = collision | Reflex | H | HU §42, HU §69 |
| CON-030 | Never let all three directions share one temperature or look family; at most one may turn the page into a prop/physical replica or universal metaphor (subway map, terminal, newspaper, dashboard) | — | Reflex | H | HU §54, HU §208, HU §69 |
| CON-031 | Don't let all three directions be pure typography; keep the other candidates as visible alternates | — | Finish | J | HU §54, HU §56 |
| CON-032 | Same-medium references transfer layout; cross-medium references may lend only colour or type relationships | — | Reflex | J | HU §49 |
| CON-033 | Never claim to have seen a reference you have not; a near-blank screenshot (<0.8% pixels differing >24 brightness) counts as not seen | 0.8% / 24 | Floor | M | HU §9, HU §49 |
| CON-034 | Write what a reference lends as concrete rules (grid columns, headline:body ratio, dominant colour share, image-text relationship) | — | Finish | J | HU §49, HU §52 |
| CON-035 | Grow the design from existing context (design system, codebase, shipped product, brand, references); building from nothing is the last resort | Context work ~90 pts vs from-zero ~60-65 | Reflex | J | HU §5 |
| CON-036 | When output feels "too AI", add candidates and references first; any new ban must survive a round of blind picks | — | Finish | J | HU §8, HU §42 |
| CON-037 | Bespoke work: every large decision belongs to this client (subject, place, materials, numbers, how its people talk); clean means exact (few type sizes far apart, one spacing rhythm, aligned edges), not empty | — | Reflex | J | HM §14 |
| CON-038 | Set aside the page you would make anyway and its obvious twist; neither ships | — | Reflex | J | HM §15, HU §2 |

### Default looks and template refusal
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CON-040 | Refuse the default plan: split hero (head left, picture right), three numbered steps, label/value rows between hairlines, closing band with a form, dark footer under huge wordmark, small grey labels, pale ground with one careful accent | Two of these in one plan = the plan is the template | Reflex | J | HM §15 |
| CON-041 | Refuse the spent looks: cream/beige paper + high-contrast serif + clay/terracotta accent; near-black + one neon; pale ground + one timid accent; purple→blue; a hue picked for the category (blue software, green health) | Warm paper: bg L>0.9, hue 40-110°, terracotta ≈#D97757 within oklab 0.07 | Reflex | H | HM §16, HU §2, HU §58, HU §68 |
| CON-042 | To escape the cream/serif/clay look move one axis: accent first, paper second, display face last | — | Finish | J | HM §16 |
| CON-043 | Treat look families as allowed but rationed: a trait recurring in ≥max(2, 50%) of the last 8 deliveries is "recurring" and at least one direction must leave it | Ledger of last 8 | Reflex | M | HU §58, HU §69 |
| CON-044 | Shape must differ from the last three builds on the six-axis fingerprint; compare against a recorded fingerprint, never memory | Share ≤3 of 6 axes with any of the last 3 | Reflex | M | HM §12, HM §233-234, HM §519 |
| CON-045 | Never deal the same hero within three pages; keep a deal history so consecutive pages differ | 3 pages | Reflex | M | TS §3 |
| CON-046 | Refuse the "subject painted on instead of known": paper/grain surfaces, stamps, dials, knobs as ornament, bevels, engravings, drawings of the thing | — | Reflex | J | HM §16, HM §127 |
| CON-047 | Refuse AI tech clichés (gradient spheres, digital rain, circuit boards, robot faces) and the GitHub-dark lazy fix (#0D1117 + cyan/purple glow); use abstract metaphors | — | Reflex | H | HU §60, HU §104, HU §215 |
| CON-048 | Never treat Anthropic/Claude brand colours or a framework default as a safe default or as a "brand" | — | Reflex | H | HU §2, HM §137 |
| CON-049 | Avoid forced big-idea metaphors (filing cabinets, library cards, subway maps, prescription slips); remove the device — if information gets clearer it was too much | — | Reflex | J | HU §42, HU §54 |
| CON-050 | Lock a design system only on request or when work spans more than one page; after locking, pages share direction/type/accent and differ only in shape; amend via a variants section, never override locally | — | Reflex | J | HM §139-140 |

### Business-kind fit (what each kind may carry)
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CON-060 | Reserve effects, scenes, loops, counters, CSS/shader grounds, dark pages and dark heroes for tech (software, gaming, hardware); build other kinds from photographs, flat colour, type, real icons | — | Reflex | H | TS §5, TS §7, TS §25 |
| CON-061 | Software lead picture is the client's own UI showing what it works on (code review = diff with Accept), never a generic dashboard or fragments only | Full app window in hero or sections 2-3 | Reflex | J | TS §19-20, TS §122, TS §588 |
| CON-062 | A game hero names the game and genre (h1 ≤40 chars) with launch date/status; never an abstract effect, statement or UI hero | ≤40 chars (≤32 on photo hero) | Reflex | H | TS §21 |
| CON-063 | Product pages show the product big: long side 80-100% of its frame in hero + ≥1 section; under 60% FAIL, 60-80% WARN; never mid-size in a grey rounded panel on grey | 80% target | Reflex | M | TS §16-17 |
| CON-064 | Place pages lead with photographs; the hero is always a photograph when any frame fits (remote place: its region's landscape); visit block on screen 2 | 3-6 screens | Reflex | H | TS §10-11 |
| CON-065 | Services show the work, the team at work, the rooms; never product UI the firm doesn't run, stock handshakes, invented client logos | — | Reflex | J | TS §18 |
| CON-066 | One object (product photo, key art, app window) leads the hero and at most two more sections; every other picture section uses another visual kind, no kind more than twice | Object in ≤3 sections | Reflex | H | TS §87 |
| CON-067 | Picture every headline promise ("takes four crates" shows four crates); else add the picture or cut the promise | — | Reflex | J | TS §16-17 |
| CON-068 | Industry rules can forbid styles (e.g. no AI purple/pink gradients for banking); filter the category's anti-patterns out of the direction | Severity HIGH = hard constraint | Reflex | J | UX §245, UX §455 |
| CON-069 | Pick three candidate shapes for the domain from different families (grid-, document-, poster-, product-led), never near-twins | See shape trios | Reflex | J | HM §235 |
| CON-070 | Developer docs and developer marketing are different briefs (walkthrough → Workbench; landing → Bento + Stat-Led) | — | Reflex | J | HM §235 |
| CON-071 | App screens disappear into the task: marketing rules step aside (no hero, fold, word budget, section rhythm, reveal on load); the direction lends palette, faces, radius, surfaces, never layout or navigation | — | Reflex | J | HM §143, HM §159 |

### Critique and scoring
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CON-080 | Score Concept/Intent first; if Concept ≤5 cap the overall at 6.0 and fix concept before execution | Concept 1-10; veto ≤5 → overall ≤6.0 | Reflex | J | HU §97, HU §105 |
| CON-081 | Score six axes 1-5 before shipping (philosophy, hierarchy, execution, specificity, restraint, variety); anything under 3 triggers revision; name the weakest axis and its fix; never invent a weakness | <3 revise | Reflex | J | HM §151, HM §515 |
| CON-082 | Specificity 5 = could belong to no other product; 3 = fits the category. Philosophy 5 = an argument a reader could disagree with | — | Reflex | J | HM §151 |
| CON-083 | Weight critique by scenario (landing: functionality + hierarchy, relax nothing; app UI: functionality + craft; infographic: functionality + hierarchy; slides: hierarchy + functionality); concept always first | — | Finish | J | HU §103 |
| CON-084 | Review output: overall X.X/10 with tier (8+ excellent, 6-7.9 good, 4-5.9 needs work, <4 failing), Keep list, Fix list tagged Fatal/Important/Improvement with values, three 5-minute Quick Wins | — | Finish | J | HU §105 |
| CON-085 | Finish review: at most eight findings ranked by cost to the page; a direction you would not have chosen is not a finding; close by naming what must not be diluted | ≤8 findings | Finish | J | HM §157, HM §155 |
| CON-086 | Review with fresh eyes (no inherited context), hero alone first, then finished page; act on the verdict's first word: recapture / rebuild / fix / ship | — | Reflex | J | HM §155, HM §520 |
| CON-087 | When the user's choice conflicts with a high reviewer score, the user wins; list observable differences, ask one question, record the preference | — | Floor | J | HU §10 |
| CON-088 | Waive a Reflex rule only with the rule named, guard evidence, and a page-specific reason sharing a word with the page; same rule waived 3 builds running or >3 waivers on a page = codify as house style | Reason ≥24 chars (HM) / ≥12 (TS); ≤5 waivers (TS) | Reflex | M | HM §3, HM §521, TS §645 |
| CON-089 | Never write a pass count or rendered check you did not run; a fabricated pass is slop | — | Floor | J | HM §141, HM §153 |
| CON-090 | Test against benchmark briefs that tempt defaults: no-numbers early product, component-not-page, same theme twice, vague prompts (dog walking, meditation app, band site) | — | Finish | J | HM §523 |

---

## D07 Layout & composition

### Focal point and hierarchy
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-001 | Put a focal point on the first screen; the title is readable 1.2s after load | 1.2s | Reflex | H | TS §99 |
| LAY-002 | Pass the squint test: with words blurred, each section keeps a shape and the page a rhythm of heavy and light | — | Reflex | J | HM §210, HM §151, HU §99 |
| LAY-003 | Keep headline-to-body size contrast ≥2.5x (fix: title ≥3x body, e.g. 16 → 48-64px) and 3-4 clear levels via size/weight/colour | ≥2.5x | Reflex | M | HU §99, HU §104 |
| LAY-004 | Hero head ≈1.5x section head; section head ≈2x item title | e.g. 84 / 52 / 25px | Finish | M | HM §170 |
| LAY-005 | Render the median h2 below the hero at ≥40px at 1440 (36px h2 under 84px hero reads as a page of small things); long-document/letter/photographic shapes may use inline heads | ≥40px | Reflex | M | HM §35, HM §170 |
| LAY-006 | Build hierarchy from size, weight and space, never colour alone or ornament; never radius alone for emphasis | — | Reflex | J | UX §235, KM §177-178 |
| LAY-007 | Use one primary axis per page (left-, right-biased, top-heavy, bottom-weighted); centre-biased is a default, not a choice | — | Reflex | J | HM §33 |
| LAY-008 | Never more centred heading groups than left-aligned ones; one or two centred section heads among left-aligned ones WARN | centred ≤ left | Reflex | M | HM §32, HM §434, TS §81 |
| LAY-009 | Keep one alignment globally (left recommended); left-align body, centre only short display lines; no centred paragraphs or lists | — | Reflex | M | HU §104, KM §179 |
| LAY-010 | Scroll the page one screen at a time: every screen holds something big enough to be its reason; this outranks every detail finding | — | Reflex | J | HM §157, HM §210 |
| LAY-011 | Read only the headings and the hero: if they tell the story, the rest is the right length | — | Finish | J | HM §30 |
| LAY-012 | Give a diagram/figure 1-2 focal elements; five accented nodes means nothing was decided; focal must match the caption's emphasized word | ≤2 focal; accent area ≤5% | Reflex | H | KM §350-351 |

### Grouping, proximity and spacing scale
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-020 | Put at least twice the space above a heading as below it; a head with space above <0.75x space below and ≥12px short is crowding; boxes <200px tall exempt | above ≥2x below | Reflex | M | HM §37, HM §430, KM §64 |
| LAY-021 | Run a screen page on three spacing steps: inside a block, head-to-content, section-to-section | 3 steps | Reflex | M | KM §64 |
| LAY-022 | Keep every padding, margin and gap on one spacing scale; values >2px are multiples of 4; at most three optical nudges | HM: 2,4,8,12,16,24,40,64,96,144; TS: 4..128; base 4px | Reflex | M | HM §73, HM §416-417, TS §55, UX §235, KM §62 |
| LAY-023 | Never write a raw length where a spacing token of that value exists | — | Reflex | M | HM §73, HM §416 |
| LAY-024 | Use `gap` for siblings, `margin` only to break the flow | — | Finish | M | HM §73 |
| LAY-025 | Head and its lede 16-24px apart; head block to section content 48-64px (40 tight); grid items column-gap apart horizontally and 48-64px vertically; card/well padding 32-40px | 16-24 / 48-64 / 32-40px | Finish | M | HM §171, TS §74 |
| LAY-026 | When a heading block feels dense, open its internals (title-to-lede) before touching macro rhythm | — | Finish | J | KM §65 |
| LAY-027 | Pad text inside a filled or side-bordered box >100x30px by ≥max(8px,0.5em) sides and ≥max(4px,0.3em) top/bottom (em part capped 24/12px) | — | Floor | M | HM §79, HM §431 |
| LAY-028 | Keep running text ≥8px from a phone edge; use a 16px phone gutter | 16px | Floor | M | HM §79, HM §431, TS §81 |
| LAY-029 | Group related fields/items with whitespace first; repeated rows carry no ornament (connector lines, badges, index numbers become noise by the 5th repeat) | — | Finish | J | UX §236, KM §67 |
| LAY-030 | Use a density dial to pick the scale: low/marketing 24-96px, mid 16-64px, high/dashboard 8-32px | — | Finish | J | UX §246 |

### Container, grid and edges
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-040 | Use one centred, capped container per page; at 1920 gutters grow, measure and grids do not | HM: 1440 cap, 64 gutter (1312 content); TS: 1280 wrap at x80-1360; cap 1360-1520 at 1920 | Floor | M | HM §4, HM §39, HM §167, HM §424, TS §69, TS §81 |
| LAY-041 | Keep one container width (≥900px), one primary button style, at most two column gaps below the hero, one radius per nesting level | — | Reflex | M | HM §32, HM §434, TS §53 |
| LAY-042 | Lay sections on a 12-column grid so left edges line up from nav to footer | gap 32 (HM) / 24 (TS), 12 under 640 | Reflex | M | HM §168, TS §70 |
| LAY-043 | Start every block on the left line or a column start; end right-ending blocks on a column end; anything wider than half the wrap runs the full wrap | — | Reflex | M | TS §81 |
| LAY-044 | Hold equal left/right margins; off-centre drift from 16px WARNs | 64-120px desktop, 16-24 phone | Reflex | M | TS §81, TS §85 |
| LAY-045 | Never bleed a block out to only one viewport edge; stand on the container lines or run edge to edge (stage visual may bleed off outer edge) | — | Reflex | M | TS §69, TS §83, HM §47 |
| LAY-046 | Use at most two text start lines (the left line and one split line); text starting on more than two left lines fails | split at col 5, 6 or 7 | Reflex | M | TS §81 |
| LAY-047 | Never let a text block run wider than 1600px or a grid gain columns at wide sizes; cap `vw`-sized visuals with max-width | 1600px | Reflex | M | HM §38, HM §424 |
| LAY-048 | Let section body fill the width: its widest row reaches 10 of 12 columns; a narrow text block with the right half empty is the sparse page's signature | 10/12 cols | Reflex | M | HM §176, TS §85 |
| LAY-049 | Hold prose measure at 60-75ch on desktop (35-60 on mobile); long-document/letter shapes 50-65ch | 65-75ch | Reflex | M | UX §23, UX §235, KM §179, HM §213, HM §223 |
| LAY-050 | Use CSS Grid for page layout, Flexbox inside components; container queries for widgets whose layout depends on their box | — | Finish | M | HM §38, HM §133, HU §79 |
| LAY-051 | Outer section owns background and block padding; inner container owns width and only padding-inline; never a padding shorthand on the inner container | — | Reflex | M | HM §169 |
| LAY-052 | Two-column rows: cap both tracks and put slack on the outer trim, never in the gutter between copy and its visual | — | Finish | M | KM §66, KM §161 |

### Grids, cards, bento
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-060 | No empty cell and no orphan on a grid's last row; change the count or columns; logo rows split evenly (3+3, never 5+1) | — | Reflex | M | HM §38, HM §432, KM §168 |
| LAY-061 | Image-bearing grid tracks use `minmax(0, 1fr)`, never bare `1fr` | — | Floor | M | HM §4, HM §426 |
| LAY-062 | Flex children that shrink take `min-width: 0`; icons/images `flex-shrink: 0`; unequal-height flex rows take a deliberate `align-items` | — | Reflex | M | HM §38, HM §433 |
| LAY-063 | Never squeeze a text block into a sliver (under ~16 chars wide over 4+ lines) | <16 chars | Reflex | M | HM §38 |
| LAY-064 | Refuse three equal columns of icon-above-heading tiles; vary widths/heights, mix image and text cards, span columns | — | Reflex | H | HM §124, HU §63 |
| LAY-065 | Reserve cards for content that is independently interactive or of a different kind; never a card in a card, white cards on a tinted page, or a bordered box in a well | depth ≤2 boxes | Floor | M | HM §4, HM §74, TS §94, TS §192 |
| LAY-066 | Climb the surface ladder in order: whitespace → 1px hairline → tinted well → card (border or shadow, never both); climb different rungs at different seams | — | Reflex | H | HM §74 |
| LAY-067 | Never repeat one card recipe identically (same radius + same shadow ≥4 times = card kit) or one container recipe on ≥6 selectors | 4 / 6 | Reflex | M | HU §68, HM §78 |
| LAY-068 | Grid composition: 3-4 items across (or 2x2), each with photo/large figure/title big enough to carry the cell, equal heights, aligned tops, ≥240px | ≥240px | Finish | M | HM §180 |
| LAY-069 | Bento: 4-6 tiles (shape: 6-9 blocks) in mixed spans (8+4 over 4+4; 7+5 over 5+7), rows 280-360px, ≥2 tiles with a visual, one tile clearly the lead | — | Finish | M | HM §181, HM §212, TS §118 |
| LAY-070 | Use bento only when there are many small equally valid things; avoid when the message is one hero idea; never a bento next to another card grid | — | Reflex | J | HM §212, HU §63, TS §102 |
| LAY-071 | One card height per row; titles level across a row; lines held so panels align | — | Finish | M | TS §53, TS §191 |
| LAY-072 | Never scroll inside a card; truncate with an expand path | — | Reflex | M | ADP §82 |

### Section anatomy, mass and density
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-080 | One idea per section: one h2, at most one action besides the main one | — | Reflex | J | TS §89, HM §30 |
| LAY-081 | A head and a paragraph are a head block, never a section; give every section mass: visual ≥300px (HM §176: 360), three across spanning ≥70%, list/table ≥3 rows, ≥2 form fields, or a statement at section size | — | Reflex | M | HM §34, HM §176, HM §429 |
| LAY-082 | Below the hero, a body spanning <72% of the container at 1440 that is not a statement is thin; a one-line (≤40 words) band + action allowed once a page | 72% | Reflex | M | HM §34, HM §429 |
| LAY-083 | Fix thinness with mass (bigger visual, ~10-column body, head at section size, statement) or merge; never with more words or a smaller gap | — | Reflex | J | HM §34, HM §172, KM §258 |
| LAY-084 | Section height usually 520-900px; under 360px only for a band, at most twice a page | 520-900px | Finish | M | HM §177 |
| LAY-085 | Merge short blocks: a quote, logo row, stat row or FAQ under ~495px becomes the last element of the section above, 64-96px under its content | <495px | Finish | M | TS §91, TS §75 |
| LAY-086 | Empty area >35% of a section inside its container WARN, >50% FAIL; fill ≥0.55 (0.40 WARN) | 35/50% | Reflex | M | TS §78 |
| LAY-087 | Never vertically centre a short block in a tall screen to hide that it is short | — | Reflex | J | TS §74, TS §78 |
| LAY-088 | Paged documents: body pages 60-80% fill; warn trailing whitespace >25%; sparse at 50% empty; last page may close at 40-60% | — | Reflex | M | KM §256, KM §322 |
| LAY-089 | Fix a sparse page by merging up, merging down, or removing it; never filler prose, restated headings, invented stats or space-filling callouts | — | Floor | J | KM §258, HU §71 |
| LAY-090 | Scan rendered pages for sparse blocks taller than ~¼ viewport, empty grid slots or lone items in multi-column rows | ¼ vh | Reflex | M | KM §168 |
| LAY-091 | Every element earns its place: remove it — if the design is not worse, delete; "less empty" is not a job | — | Reflex | J | HU §71, HU §101 |
| LAY-092 | A section whose content names itself (menu, timetable, track list, product screen) may go without a head block | — | Finish | J | HM §174 |
| LAY-093 | Head block: h2 ≤6 words at section size, ≤1 lede line, on cols 1-6/1-7 or split (head 1-5, line 7-12, baselines aligned); centred only over a symmetric body | ≤6 words | Finish | M | HM §175 |

### Section rhythm and page structure
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-100 | Leave ≥120px between sections at 1440 (64 where the paper changes; <112 on shared paper is short) and never make every gap identical | 120/144/176 mixed | Reflex | M | HM §36, HM §172, HM §418 |
| LAY-101 | Earn space by mass: a 144px gap frames a 700px section and is a hole under a 200px one | — | Finish | J | HM §172 |
| LAY-102 | Run section spacing as one responsive ladder and scale the whole set by one factor (~0.75) when it reads too airy/tight, never nudge one gap | e.g. 96/72, 72/54, 56/42 | Finish | M | KM §68 |
| LAY-103 | Use 3-6 different compositions per page and never the same one twice in a row; any card layout at most twice per page | 3-6; ≥4 layout families across 8 sections | Reflex | M | HM §195, HM §205, TS §92, TS §99 |
| LAY-104 | Never more than two neighbours with the same skeleton; head-then-block repeated reads as a template | — | Reflex | J | HM §174, HM §41 |
| LAY-105 | Follow a dense section (grid, table, bento, index) with a quiet one (statement, showcase); after at most two visual sections place a calm one; back third calm before the close | — | Finish | J | HM §206, TS §92 |
| LAY-106 | Pick one divider language per page and vary its weight/placement by seam; same rule at the same gap at every seam is the template | — | Reflex | J | HM §74, HM §234 |
| LAY-107 | Use one or two bands (change of paper) per page; at least one full-width visual on a product page | 1-2 bands | Finish | M | HM §205 |
| LAY-108 | Photographs take ¼-⅓ of the page below the hero and never lead two sections in a row | ≤45% on photographic/portfolio shapes | Finish | M | HM §205, HM §219 |
| LAY-109 | Two picture-less sections are never neighbours; a quote or closing call that is text-only FAILs on marketing pages | — | Reflex | M | TS §78, TS §86, TS §102 |
| LAY-110 | Splits: text and visual centre on each other within 60px; neither column leaves >⅕ of the row empty | 60px / 20% | Reflex | M | HM §177 |
| LAY-111 | Never zigzag splits; mirror at most once a page (or never); vary weight via a larger lead row rather than A-B-A-B alternation; change ratio between two splits (5/7, 4/8, 6/6) | ≤1 mirror | Reflex | M | HM §178, HM §205, TS §82, KM §161, KM §270 |
| LAY-112 | Split visual ≥440px tall at 4:3 to 4:5 (portrait for product photos) | ≥440px | Finish | M | HM §178 |
| LAY-113 | Showcase: one visual across all 12 columns at 16:9-21:9, ≥560px; at most two smaller beneath at 8+4 or 7+5, never three equal frames | ≥560px | Finish | M | HM §179 |
| LAY-114 | Statement: one sentence over 8-10 columns in 2-3 lines from section size to display size, once a page | once | Finish | M | HM §186 |
| LAY-115 | Rows composition: 3-5 full-width rows parted by hairlines, 72-120px each; title on cols 1-5, line/figure on 6-12 | — | Finish | M | HM §182 |
| LAY-116 | Rail: 5+ items past the container edge with the next one cut, scroll-snap, touch + keyboard scrollable, focusable and labelled | ≥5 items | Finish | M | HM §189, HM §248 |
| LAY-117 | Pinned: one sticky visual on 6-7 columns while 3-4 short panels scroll past, each changing what it shows; static under 60rem | — | Finish | M | HM §190, HM §227 |
| LAY-118 | Index: 6-20 rows of the brief's own items with facts in columns, lead row larger | 6-20 rows | Finish | M | HM §192 |
| LAY-119 | Never more than one scroll-choreography pattern per page; never on body text | 1 | Reflex | M | HM §42, HM §341 |
| LAY-120 | Never two `position: sticky; top: 0` elements; offset a sticky section head by nav height; raise scroll-padding for a tall sticky nav | — | Floor | M | HM §43, HM §427 |
| LAY-121 | One theme (light/dark/auto) for the whole page; no mid-page flips; a dark footer never directly under another dark section | — | Reflex | M | TS §99, TS §101 |

### Page anatomy by visitor job and page type
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-130 | Never build from the default run (hero, three features, CTA, footer / figures, steps, email band); order follows the argument the page makes | — | Reflex | J | HM §17, HM §41, HM §204, HU §63, HU §158 |
| LAY-131 | Lead with the strongest real thing after the hero; tell the page as story: what it does → show it → prove it → explore/act | problem → solution → proof → action | Reflex | J | HM §204, TS §100, HU §159 |
| LAY-132 | Steps only for a process the visitor really goes through, with three real steps; figures row only for three numbers stated outright, never derived | 3-4 stages | Reflex | J | HM §185, HM §204, TS §123 |
| LAY-133 | Subscribe: action in/as the hero (name, one line, email field); latest/sample issue; archive as dated index; may close on a second field | — | Reflex | J | HM §19, UX §217 |
| LAY-134 | Book: booking picker (party, date, time) or next free times opened from nav and hero and repeated beside menu/classes, never only at the foot; ends on hours, address, booking | — | Reflex | J | HM §20 |
| LAY-135 | Visit: today's hours and address in nav or hero; what's on now; dated rows for what's coming; getting there | — | Reflex | J | HM §21, TS §155 |
| LAY-136 | Attend: tickets in the nav from the first screen; date and place are the headline; lineup, schedule, tiers with prices, venue, questions | — | Reflex | J | HM §22, UX §212 |
| LAY-137 | Buy: product with price and options as an offer, often the hero; range with prices, product in use, how it's made, delivery/guarantee; email field in footer, not the close | — | Reflex | J | HM §23, HM §194, TS §17 |
| LAY-138 | Try: store/download buttons under the head, one per named platform; features as named moments in screens, not icon tiles | — | Reflex | J | HM §24 |
| LAY-139 | Sign up: "Start free" in nav and hero with terms in one line; product at work, named moments, code sample, pricing with period switch, questions; never ends on a newsletter | — | Reflex | J | HM §25, TS §20 |
| LAY-140 | Hire: plain contact in nav and after the work; the work is the page (project index: name, client, year, place); no form needed | — | Reflex | J | HM §26 |
| LAY-141 | Join: join/"your first visit" in the hero; a session shown, schedule, priced membership rows, first-visit guidance | — | Reflex | J | HM §27 |
| LAY-142 | Listen: new release with listen/watch/order side by side; contents as index; dates as rows with ticket links; earlier work as covers | — | Reflex | J | HM §28 |
| LAY-143 | Place page: hero, visit (screen 2), offer, the place, orders/booking, close; one main action per screen; 3-6 screens total | 12-20 photos full / 8-12 compact / <8 short (3 screens, ≤2700px) | Reflex | M | TS §10-12, TS §100 |
| LAY-144 | Software page: hero, full app window by section 2-3, 2-3 feature sections in different layouts, integrations, proof, pricing, FAQ, close | — | Reflex | J | TS §20, TS §100 |
| LAY-145 | Service page: hero, services list with "from" prices, work, steps, people, proof, pricing, FAQ, booking with address, close | — | Reflex | J | TS §18, TS §100 |
| LAY-146 | Proof comes in the category's own form (menu, lineup, issues, record), never a generic band of numbers | — | Reflex | J | HM §17, HM §518 |
| LAY-147 | Build a section with no supplied content as a clearly sample-shaped stand-in that states no fact a visitor could take as true; a section made only of facts nobody gave is one line + a text slot, or waits | — | Floor | J | HM §18 |
| LAY-148 | SaaS section deck: deal cards by role (spec sheet, worked example, changelog, comparison, pricing, FAQ, CTA strip, footer); drop ≥1 base card and promote or reorder one pair; <5 cards = landing strip | ≥5 cards | Reflex | J | HM §237-239 |
| LAY-149 | Material-dependent cards exist only with material: logo row needs permitted customer marks; testimonials need verbatim quotes with name/role/company; three features need three named capabilities with captures | — | Floor | J | HM §238, TS §93, HU §60 |

### Macrostructures (page shapes)
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-160 | Design the page the brief asks for, then name the shape; reaching into the catalogue first collapses everything into the same three shapes | 21 named shapes | Reflex | J | HM §211 |
| LAY-161 | Bento shape: display head over first row; grid starts in or right under the first screen; blocks hold supplied figures/quotes only | 6-9 blocks | Finish | J | HM §212 |
| LAY-162 | Stat-Led shape only with a supplied figure carrying unit and source, paired with a worded headline; never the hero's only words | — | Floor | J | HM §215, HM §48 |
| LAY-163 | Quote-Led only with a verbatim supplied quote with name, role, company | — | Floor | J | HM §220 |
| LAY-164 | Workbench: real captures are the content, each a figure with a factual caption; no browser/device chrome | — | Reflex | J | HM §216 |
| LAY-165 | Long Document: inline section heads, single column, 60-65ch, line-height ≥1.65, CTA as an in-paragraph link | — | Finish | M | HM §213 |
| LAY-166 | Catalogue / Portfolio / Index / Ecosystem shapes put content on the first screen; heading never pushes the first row below the fold | — | Reflex | M | HM §222, HM §224, HM §229, HM §231 |
| LAY-167 | Narrative Workflow: stage number inside the heading (never a separate label); vary the stage object; three stages holding the same object read as three features | — | Reflex | J | HM §225 |
| LAY-168 | Map/Diagram shape: SVG drawn from the real system with a text legend; collapses to an ordered list or scroll wrapper under 60rem | — | Reflex | H | HM §230 |
| LAY-169 | Specimen look only for type, publishing or writing briefs (the field's most-copied look) | — | Reflex | J | HM §221 |

### Hero rules and fold geometry
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-180 | Keep headline, lede, primary action and the visual's focal point visible at 1280x800 without scrolling | 1280x800 | Floor | M | HM §4, HM §45, HM §422 |
| LAY-181 | Make the hero exactly one screen at 1440x900: next section starts between y 760 and 900 (ending before 84% is short, past 908 is long); nothing of the next section shows | 760-900 | Reflex | M | HM §45, HM §423, TS §171 |
| LAY-182 | At 1920x1080 the container holds, hero text ≥120px from the edge, and the hero still fits | — | Reflex | M | HM §45, HM §424 |
| LAY-183 | Size heroes in `dvh`/`svh`, never `vh`; an undeclared hero ≥92dvh needs a deliberate posture | 92dvh | Reflex | M | HM §48, HM §420-421, UX §22, TS §171 |
| LAY-184 | Centre hero content: space below 1.0-1.5x space above (settled, banner, corridor, stage); ledge inverts | 1.0-1.5x | Reflex | M | HM §46, HM §199, HM §423 |
| LAY-185 | No dead band: >160px of nothing between the hero's lowest content and the fold FAILs; grow the visual or head, never add copy | 160px | Reflex | M | HM §46, HM §199, HM §423 |
| LAY-186 | Hero visual: 6-7 columns and ≥60% of screen height (520px at 1440x900), or a portrait object at 75% on 4-5 columns; centre within 60px of text block centre; 48-120px from text | 60% / 60px / 48-120px | Reflex | M | HM §47, HM §200, HM §423 |
| LAY-187 | Never leave hero text ending 240px short of its visual; never pin the visual to the viewport edge (stage may bleed off outer edge) | 240px | Reflex | M | HM §423 |
| LAY-188 | Delete the picture in your head: if the screen says the same thing, the picture is too weak or too small | — | Reflex | J | HM §47 |
| LAY-189 | Never stack title, lede, action and mark all on one centred axis; prefer ≤2 centred elements with one breaking alignment | — | Reflex | H | HM §48, HM §421, HM §516 |
| LAY-190 | Hero without a visual: head grows to display size across 8-12 columns, or use Banner posture with the first section starting by 640px | 640px | Finish | M | HM §201 |
| LAY-191 | Hero postures: Settled, Stage, Banner (50-60% screen), Ledge, Corridor (≤44ch), Poster (92-100dvh), Counter (the action is the visual), Index (content is the visual); pick from the job and vary across projects | — | Finish | J | HM §197-198 |
| LAY-192 | Text-beside-picture hero is the most common generated hero; take it only when the picture is the strongest thing available | — | Reflex | J | HM §197 |
| LAY-193 | Refuse hero template tells: pill/label above headline, gradient blob, empty coloured box where a picture belongs, drawn illustration, counting marks, two filled buttons, version/BETA pill, mono-caps strip | — | Reflex | H | HM §51, HM §156, TS §22 |
| LAY-194 | A working form is a section or a close, not the default hero; a split hero holding only an order form is banned | — | Reflex | J | HM §200, TS §17, TS §26 |
| LAY-195 | Primary hero button below the first screen FAILs at every width; main button inside the hero at 1440, 1280, 1024, 820, 768, 390 | — | Floor | M | TS §171, TS §633 |
| LAY-196 | No caption under the hero picture, no second float card, no scrim/gradient/veil/blur laid over a photo to make words readable; put words on the photo's calm part | — | Reflex | H | TS §171-173 |
| LAY-197 | Docked strip under hero (software/product only): ≤96px, still, real permitted logos, a given rating or three facts | ≤96px | Finish | M | TS §171 |
| LAY-198 | Build and review nav + hero alone before building below; a hero that fails with correct copy changes its visual, not its copy | — | Reflex | J | HM §50, HM §155 |
| LAY-199 | Hero entrance: one settle 0.4-0.8s total from an already-visible default; never fade+sweep+scale on one element, bounce, starfield, mouse parallax or auto-rotating carousel | 0.4-0.8s | Reflex | M | HM §49, TS §172 |

### Word budgets
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-210 | Hero headline ≤7 words / ≤50 characters (TS: 2-8 words, ≤2 lines; ≤3 lines at every width) | ≤7 words | Reflex | M | HM §44, HM §202, TS §99, TS §171, TS §173 |
| LAY-211 | Hero carries at most two text blocks before its actions: headline + one sentence ≤12 words, then 1-2 actions | ≤12 words lede | Reflex | M | HM §31, HM §44 |
| LAY-212 | About 80 words per 900px window at 1440 (labels and cells included) | 80 words/screen | Floor (house) | M | HM §4, HM §31 |
| LAY-213 | At most 450 visible words on a landing page; fullness comes from scale and pictures, never words | 450 | Reflex | M | HM §30 |
| LAY-214 | Section heads ≤6 words; section intros one line; paragraphs two short sentences; lists of four items (3-word label + 10-word line) | — | Reflex | M | HM §105, HM §175 |
| LAY-215 | Single-line surfaces at 1280: hero tagline, feature subtitles, benefit points, gallery captions, ledes ≤~12 words; at 375: price line, platform line, CTA labels, chips; a near-wrap (one word away) fails | — | Reflex | M | KM §145 |
| LAY-216 | Fix wraps by container geometry first, then shorter wording; never shrink font, force a break, or shave padding | — | Reflex | J | KM §145 |
| LAY-217 | When copy is verbatim from the client, copy-budget rules report as notes only | — | Reflex | J | HM §3 |
| LAY-218 | Slides: one core viewpoint per page; a point past three lines splits the slide; 1 assertion + 3-5 items or 1 chart + 2-3 callouts | — | Reflex | M | HU §75, KM §257, KM §670 |
| LAY-219 | Section and page counts: 6-9 sections incl. hero and footer (5 on a thin brief, never fewer; over 9 merge); height follows content, never padded toward a target | 6-9 | Reflex | M | HM §30, HM §173, HM §419 |

### Responsive structure and breakpoints
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-230 | No horizontal scroll at any width 320-1920; `overflow-x: clip` on html and body (never `hidden`), `width: 100%` never `100vw` | 320-1920 | Floor | M | HM §4, HM §80, HM §425, UX §85, TS §84 |
| LAY-231 | Check widths 320, 375, 414, 768, 1024, 1280, 1440, 1920 (+ 820 tablet); fold at 1280x800, 1440x900, 1920x1080; full page at 1440 and 375 | — | Reflex | M | HM §152, HM §256, UX §81, TS §641 |
| LAY-232 | Use few shared breakpoints in rem, written in one direction; add one only where content breaks; never px breakpoints; 2-3 per element max | HM: 60rem (layout), 40rem (type) | Reflex | M | HM §257, UX §334, ADP §198 |
| LAY-233 | Under 60rem: gutters 24px, section gaps 80/96/120, grids to one column, tilts/clips drop, sticky panes unstick, heroes collapse to content height | — | Finish | M | HM §257, HM §417 |
| LAY-234 | Under 40rem: gutters 16px, section gaps 56/72/96, column gap 16, display sizes step down, margin captions inline | — | Finish | M | HM §257, HM §417 |
| LAY-235 | Every composition stacks in reading order (head block, then body); a split's visual comes after its text; bento lead tile first; rails stay rails; schedule becomes one column per day | — | Reflex | M | HM §196, TS §74, TS §82 |
| LAY-236 | Grids go 4 → 2 → 1 (two across, then one under 40rem); visuals keep aspect ratio and drop their min-height | — | Finish | M | HM §196, ADP §204, ADP §208 |
| LAY-237 | Never hide on a phone content shown on desktop (≥40 words at 1440 hidden at 375, nav aside) | 40 words | Reflex | M | HM §133, HM §435 |
| LAY-238 | Collapse every desktop sidebar or filter column into a menu or disclosure | — | Reflex | M | HM §133, HM §256, ADP §205 |
| LAY-239 | Keep source order logical; visual reorder must not make tab order confusing | — | Floor | M | ADP §206, UX §230 |
| LAY-240 | Use `clamp()` for continuous size; media queries for discrete layout; detect capability with `(hover: hover)` / `(pointer: coarse)`, never width; never device-sniff | — | Reflex | M | HM §258, ADP §77 |
| LAY-241 | Fold safe areas into the gutter with `viewport-fit=cover`: `max(16px, env(safe-area-inset-left))`; fixed bars reserve padding for content beneath | — | Floor | M | HM §260, UX §19, UX §148, UX §243 |
| LAY-242 | Ship the viewport meta `width=device-width, initial-scale=1`; never disable zoom | — | Floor | M | UX §84, UX §235, ADP §198 |
| LAY-243 | Avoid nested scroll regions; nothing scrolls sideways except a rail or a table that says so | — | Reflex | M | UX §235, HM §196 |
| LAY-244 | Leave room for 30-40% longer strings and use logical properties for i18n | 30-40% | Reflex | M | HM §263, KM §161 |
| LAY-245 | Mobile density inversion: images first, feature copy compressed to 1-2 sentences | — | Finish | J | KM §148 |
| LAY-246 | Tablet first screen ends on a whole element (≥24px above hero foot) or a clear bleed; never 1-95px of a box under the fold | — | Finish | M | TS §171 |
| LAY-247 | Edge-to-edge paragraphs on tablets are banned; gutters grow on larger widths and in landscape | — | Finish | M | UX §243 |

---

## D08 Components, states & flows

### Eight states
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-001 | Ship every interactive control with all eight states: default, hover, focus-visible, active, disabled, loading, error, success | 8 | Floor | H | HM §91, HM §311, HM §142 |
| CMP-002 | Preview components with every state rendered stacked and labelled, each forced by a helper class beside the real pseudo-class | — | Finish | M | HM §91, HM §142 |
| CMP-003 | Hover inside `@media (hover: hover)` with one signal only (colour step, 1px lift, or border step); never on non-interactive elements; never hover-only | 1 signal | Reflex | M | HM §85, HM §311, KM §148, UX §232 |
| CMP-004 | Focus ring at once, never animated: `outline: 2px solid var(--focus); outline-offset: 2px`, inset on inputs; ≥3:1 against element and page | 2px / 3:1 | Floor | M | HM §86, HM §312, UX §32, UX §326 |
| CMP-005 | Active: a 1px drop or one step darker (press scale 0.95-1.05 if scale), released on pointer up; pressed state never changes layout bounds | 1px | Finish | M | HM §311, HM §325, UX §34, UX §241 |
| CMP-006 | Disabled uses three channels: reduced opacity, `cursor: not-allowed`, native `disabled` (or `aria-disabled` when it must stay focusable); never opacity alone; keep 3:1 | opacity 0.55 (HM) / 0.38-0.5 (UX) | Floor | M | HM §92, HM §311, UX §238, UX §327 |
| CMP-007 | A disabled control near the user's attention says why it is disabled | — | Reflex | J | HM §321 |
| CMP-008 | Loading: inline progress, label stays readable, width does not jump; `aria-busy="true"` | — | Reflex | M | HM §311, UX §328 |
| CMP-009 | Error: error colour on border plus message plus `aria-invalid`; never colour alone | — | Floor | M | HM §311, UX §329 |
| CMP-010 | Success shows the result itself from the server's answer; no success state where no request was made | — | Floor | J | HM §311, HM §93, ADP §55 |
| CMP-011 | State priority when overlapping: disabled > loading > active > focus > hover > default | — | Finish | M | UX §324 |
| CMP-012 | Read-only is visually and semantically distinct from disabled | — | Reflex | M | UX §238 |
| CMP-013 | Pressed/focused/disabled states stay equally distinguishable in both themes; re-check contrast in hover state | — | Floor | M | UX §242, KM §157 |

### Buttons and CTA discipline
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-020 | One filled primary per view (a dialog counts as its own page); never two filled buttons side by side | 1 | Reflex | M | HM §90, HM §154, TS §63, UX §234 |
| CMP-021 | Secondaries outlined or typographic, never louder than the primary; two button styles only (primary + secondary); no third, gradient, ghost-on-ghost, slanted or shadowed button | 2 styles | Reflex | M | HM §90, TS §63, KM §149 |
| CMP-022 | Legitimate pair = filled primary + outlined/text action that goes elsewhere; a brand-outlined ghost beside a brand-filled primary reads as a second offer | — | Reflex | J | HM §51, KM §149, KM §267 |
| CMP-023 | Primary = the action most visitors take first; ghost for low-commitment try, filled for the revenue action; never three hero buttons | ≤2 hero actions | Reflex | M | KM §149, KM §267, TS §63 |
| CMP-024 | Marketing controls 44-52px tall; app UI 32-40px with a 44px hit target (48 on coarse pointers); at most two button sizes ≥6px apart | — | Floor | M | HM §90, HM §145, HM §258, TS §63 |
| CMP-025 | Button labels and primary nav links never wrap at any width 320-1920: shorten, then `nowrap`, then collapse the row behind a menu | — | Reflex | M | HM §90, HM §259, KM §145 |
| CMP-026 | Label = verb + object ("Book a fitting", "Download for Mac"); "Continue" only as a flow's 2nd step; no "Buy now" urgency, no price in the CTA, no glued arrow, no stock second action ("Learn more", "Get started", "Book a demo") | — | Reflex | M | HM §106-107, HM §125, KM §150, KM §273, TS §90 |
| CMP-027 | The main action reads word for word the same in nav, hero, close and phone action bar, and is a filled button nowhere else; main action on ≥5 buttons WARNs | ≤4 instances | Reflex | M | TS §63, TS §90, TS §146 |
| CMP-028 | Delete takes a secondary style unless deleting is the page's one action; destructive actions use danger colour and are separated from primary actions | — | Reflex | J | HM §90, UX §238 |
| CMP-029 | Explicit `type` on every button | — | Floor | M | HM §90 |
| CMP-030 | Prevent double submission: disable only while the request is in flight, never at rest; show inline spinner replacing the label | — | Reflex | M | HM §92, HM §314, UX §36, UX §232 |
| CMP-031 | Mobile hero button pair: one row from the text edge, label-width, never stretched to equal halves, never centred; verify at 320 and 375 in the longest locale | 42px tall, min 128px, 12px apart | Finish | M | KM §151 |
| CMP-032 | Icon-only buttons expose an accessible name; target ≥24x24 CSS px web (WCAG 2.5.8), 44pt iOS, 48dp Android; 8px between targets; expand small hit areas with an invisible pseudo-element | — | Floor | M | UX §26, UX §121, UX §126, UX §231, HM §313 |
| CMP-033 | One link behaviour site-wide; brand colour on non-links (FAQ questions, section titles) misleads | 1 link look | Reflex | M | KM §152, TS §53 |
| CMP-034 | Copy-to-clipboard swaps its label to "Copied" for ~2.5s; no toast | 2.5s | Finish | M | HM §334, HM §232 |

### Forms and validation
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-040 | Visible label above every field; never placeholder as label; floating labels are the tell | — | Floor | M | HM §314, HM §326, UX §68, UX §238 |
| CMP-041 | Placeholder shows a format (01 Jan 2026), never an instruction | — | Reflex | J | HM §314 |
| CMP-042 | Right `type`, `inputmode`, `autocomplete` and `name` on every field; 16px input text on mobile; mobile input height ≥44px | 16px / 44px | Floor | M | HM §92, UX §71-72, UX §77, UX §238, TS §67 |
| CMP-043 | Validate on blur once touched, then on every input; never on the first keystroke; never only on submit | — | Reflex | M | HM §314, HM §327, UX §70, UX §136 |
| CMP-044 | Error under its field in one sentence: what broke, why, what to do; linked by `aria-describedby`, `aria-invalid="true"`, live region or `role="alert"` | — | Floor | M | HM §314, UX §69, UX §238 |
| CMP-045 | The error replaces the helper in the same reserved line (`min-height: 1lh`), never adds a second line; layout never jumps | 1lh | Reflex | M | HM §92, HM §316, HM §327 |
| CMP-046 | After a failed submit, focus a linked error summary or the first invalid field; a failure keeps everything typed | — | Floor | M | HM §92, UX §238, TS §67 |
| CMP-047 | Required fields carry a visible word/asterisk and `aria-required`, never colour alone | — | Floor | M | HM §314, UX §73 |
| CMP-048 | Never block paste; support password managers and passkeys; show/hide password toggle | — | Floor | M | HM §92, UX §74, UX §152, UX §231 |
| CMP-049 | Constant border width across states; focus ring is an `outline` reserved transparent at rest; never transition border-width, padding or height | — | Reflex | M | HM §92, HM §315-316 |
| CMP-050 | Field edge ≥3:1 (a hairline rule colour never passes); reserve a ~24px right-edge slot for clear/error/spinner | 3:1 | Floor | M | HM §315-316 |
| CMP-051 | Input matches the height of the button beside it; never input and button sharing one border; one-field form ~20rem wide | — | Finish | M | HM §92, HM §316 |
| CMP-052 | Prefer native controls (select, checkbox, radio, range); custom only when native keyboard and screen-reader behaviour is kept; textarea `resize: vertical`, ≥6rem | — | Reflex | M | HM §317, UX §234 |
| CMP-053 | Honest forms: an unconnected endpoint says "Nothing was sent" and never prints "Sent/Thanks/You're on the list" | — | Floor | J | HM §93, HM §251, TS §137 |
| CMP-054 | Success echoes the result ("The date goes to [address]"); failure says what to do ("Try again in a minute"); status line "Sending" after 300ms | 300ms | Reflex | J | HM §251, TS §67 |
| CMP-055 | Ask only the fields needed; booking forms ≤6 fields; don't ask for the same information twice in one process (WCAG redundant entry) | ≤6 | Reflex | M | TS §137, UX §78, UX §201 |
| CMP-056 | Group related fields with fieldset/legend; persistent helper text under complex inputs; reveal complex options progressively | — | Reflex | M | UX §238 |
| CMP-057 | Never preselect consent, newsletter, privacy or cost-bearing options or business-favouring defaults | — | Floor | M | ADP §20, ADP §39 |
| CMP-058 | Long forms autosave drafts with a visible trace; confirm before dismissing a sheet with unsaved changes | — | Reflex | J | UX §238, ADP §8 |
| CMP-059 | IME composition Enter never submits: ignore Enter while `isComposing` or keyCode 229; keep Shift+Enter newline and a visible submit button | — | Floor | M | UX §79, UX §238 |
| CMP-060 | No modal confirmation on forms | — | Reflex | M | TS §22, TS §137 |

### Navigation
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-070 | Decide and name the nav; the default AI nav (wordmark left, inline links, button right, hairline under) is a reflex | — | Reflex | J | HM §40, HM §516 |
| CMP-071 | Nav is one line, 56-80px tall, sized to real destinations; three-part bar only for ≥4 real destinations; side rail only where a sticky object earns it | 56-80px | Reflex | M | HM §40, HM §209, TS §99 |
| CMP-072 | Nav carries the job's own action word (Book, Tickets, Shop, Listen, Start free); nav actions quieter than the hero's | — | Reflex | J | HM §17, HM §40 |
| CMP-073 | Text links one weight across states; state shown by colour or soft background, never a primary fill; current location highlighted | — | Reflex | M | HM §40, UX §3, UX §239 |
| CMP-074 | Under ~60rem links that no longer fit go behind a menu (real `<button aria-expanded>`); a tab row scrolls sideways rather than wrapping | — | Reflex | M | HM §40, ADP §209 |
| CMP-075 | Logo links home with an accessible label; add an explicit Home link where users land deep | — | Floor | M | HM §40, ADP §73 |
| CMP-076 | Fixed/sticky nav never obscures content or the focused control (WCAG 2.2 focus not obscured) | — | Floor | M | UX §2, UX §231 |
| CMP-077 | Every nav word, button and footer link lands on a real anchor or page; never a bare "#" or links to pages that don't exist | — | Floor | M | TS §95, KM §275 |
| CMP-078 | Hover menus open after ~150ms and close with a 200-300ms delay; never script-only; a click on the word still goes to its section | 150 / 200-300ms | Finish | M | TS §108, ADP §74, ADP §76 |
| CMP-079 | Bottom tab bar 3-5 items with icon + label, top-level only; never mix tab + sidebar + bottom nav at one level | 3-5 | Reflex | M | UX §130, UX §239 |
| CMP-080 | Sidebar earned by more than ~7 destinations (≥1024px), collapses to a menu under 60rem | >7 | Reflex | M | HM §144, UX §239 |
| CMP-081 | Breadcrumbs only for hierarchies ≥3 levels deep; never on the top page, never as the only navigation | ≥3 levels | Reflex | M | UX §6, UX §239, ADP §68 |
| CMP-082 | Back is predictable and restores scroll, filter and input state; never silently reset the stack; focus moves to main content after route change | — | Floor | M | UX §4, UX §129, UX §132, UX §239 |
| CMP-083 | State lives in the URL (filters, tabs, pagination, views); key screens deep-linkable | — | Reflex | M | HM §145, UX §5, UX §239 |
| CMP-084 | Tabs for 2-9 sections with short names, single line, never stacked rows; tab indicator moves by transform, never width | 2-9 | Reflex | M | ADP §66-67, HM §332 |
| CMP-085 | Tabs use `role="tablist"`, `aria-selected`, roving tabindex, arrow keys; without script every panel shows in order; click only, never timed | — | Floor | M | HM §249, TS §120 |
| CMP-086 | Skip-to-content link first in tab order, visible on focus | — | Floor | M | HM §255, UX §230, TS §639 |
| CMP-087 | Separate dangerous items (delete account, log out) from normal ones; explain an unavailable destination rather than hiding it | — | Reflex | J | UX §239 |
| CMP-088 | Use a phone action bar only after the hero's button scrolls off, hidden while the same action is on screen, never covering labels | — | Finish | M | TS §64, TS §154 |

### Footer and close
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-095 | End on what the visitor came to do (booking, buy box, download, next date and address, latest issue) or the last strong section; never the stock email band on a non-subscribe job | email close ≈1 in 5 | Reflex | J | HM §29, HM §128, HM §207 |
| CMP-096 | A close asks for the main action once more, word for word, with one button and no second button | — | Reflex | M | TS §146-147, HM §237 |
| CMP-097 | The default AI footer (four link columns, social row, copyright) is a reflex; footer 200-400px; link columns only for a hub with a real sitemap and named as the nav | 200-400px | Reflex | J | HM §40, HM §208, HM §516, TS §150 |
| CMP-098 | Footer links at body weight; never invent a poetic closing line or ethos; "All rights reserved" as stock line is suspect | — | Finish | J | HM §40, HM §106, KM §275 |

### Modals, overlays, menus, toasts
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-100 | Treat a modal as the last answer after inline editing and disclosure; never for primary flows, errors, success or warnings; avoid on mobile | — | Reflex | J | HM §144, ADP §70, UX §239 |
| CMP-101 | Use native `<dialog>` + `showModal()`: focus trap, Escape, backdrop; `inert` page behind; close on Escape, backdrop click and a visible close control | — | Floor | M | HM §318, UX §131 |
| CMP-102 | Pin a customised dialog: `position: fixed; inset: 0; margin: auto; height: fit-content; max-height: min(80dvh, 40rem)` | — | Finish | M | HM §318 |
| CMP-103 | Dialog footer: Cancel then Confirm, right-aligned; destructive confirmation states the consequence plainly | sm 384 / 512 / 640 / 768px | Finish | M | UX §321 |
| CMP-104 | Undo over confirm: reversible actions run at once with Undo for 5-10s; irreversible ones confirm and make the user type the name of what is destroyed | 5-10s | Reflex | J | HM §320, HM §145, UX §238 |
| CMP-105 | Popovers/menus via Popover API with anchor positioning that flips near the edge; never inside an `overflow: hidden` ancestor | flip within 16px | Reflex | M | HM §319, HM §330 |
| CMP-106 | Tooltips wait 800-1000ms on hover, 0 on focus; persist while hovered; dismiss on Escape (WCAG 1.4.13); never hover-only for essential info | — | Floor | M | HM §86, HM §331, UX §107 |
| CMP-107 | No toast when the effect is already visible; toasts for failures and invisible effects only; never celebratory | — | Reflex | J | HM §88, HM §323, HM §328 |
| CMP-108 | Toasts from one corner, never steal focus, `aria-live="polite"`, pause on hover/focus; an error toast carries one retry and does not auto-leave | dwell 4-6s (HM) / 3-5s (UX) | Reflex | M | HM §328, UX §99, UX §238 |
| CMP-109 | Use one z-index scale; never arbitrary 9999 | HM: 1/10/100/200/300/400/500/600 | Reflex | M | HM §77, HM §322, UX §17 |
| CMP-110 | No popups, newsletter modals, chat bubbles, help pills, back-to-top squares, award strips, entry gates or preloaders on marketing pages | — | Reflex | M | TS §22 |

### Tables and data regions
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-120 | Tables: sentence-case heads that never wrap, horizontal rules only, no outer border/card, no tinted header bar, no vertical grid lines, full width | — | Reflex | M | HM §96, KM §95, KM §97 |
| CMP-121 | Text left, numbers right with tabular figures, actions right; the column naming the row one step heavier | — | Reflex | M | UX §322, HM §183, KM §92 |
| CMP-122 | Row heights: compact 40, default 48, comfortable 56; marketing tables 56-72px, about five rows | — | Finish | M | UX §322, HM §96, HM §183 |
| CMP-123 | Tables before cards in dense contexts; lists past five items become a table | >5 | Reflex | J | HM §96, HM §145 |
| CMP-124 | On a phone keep the naming and action columns in view: restack each row as a labelled block or pin the first column; never open a table with ≥2 columns off-screen; ten columns on a phone is a redesign | — | Floor | M | HM §96, HM §261, HM §435, TS §143 |
| CMP-125 | Stripe only for many similar columns, multi-line or ≥8 rows when tracking fails; low contrast; start without | ≥8 rows | Finish | J | KM §93, ADP §93 |
| CMP-126 | Sort only tables >~10 rows; sortable tables expose `aria-sort`; filters on groupable columns only; bulk select with action bar for repetitive edits | >10 rows | Finish | M | ADP §94, ADP §92, UX §111, UX §240 |
| CMP-127 | Every data region draws four states: loading (skeleton in the content's shape), empty, error, full; drawing only full is a quarter of the screen | 4 | Floor | H | HM §94, UX §240 |
| CMP-128 | Dashboards: one currency and unit system; no rows silently aggregated into "other"; one meaningful default range; implementation detail stays off the surface | — | Reflex | J | KM §167 |
| CMP-129 | App stats are the product's own figures in tabular numerals; no icon tile, gradient or unmeasured trend arrow | — | Reflex | M | HM §145, HM §75 |
| CMP-130 | Virtualize lists of ~50+ items; pagination for ordered/jumpable lists, infinite scroll only for browsing flow | 50 | Reflex | M | UX §140, UX §233, ADP §80, ADP §85 |

### Pricing
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-140 | Show the actual price with 2-3 tiers; "Contact sales" on every tier says the brand doesn't trust the buyer | 2-3 tiers | Reflex | J | HM §237, TS §141-142 |
| CMP-141 | Emphasise the recommended tier with its button and a word, never a different card colour or negative margins (a taller tier is a grid sibling on explicit rows) | — | Reflex | M | HM §97, TS §141 |
| CMP-142 | Align buttons and rows across tiers (subgrid); cards never change height on a monthly/yearly switch | — | Reflex | M | HM §97, TS §141-142 |
| CMP-143 | Savings shown must match the prices; show real monthly and annual totals | — | Floor | M | TS §141, UX §202, UX §208 |
| CMP-144 | Never plan tables or monthly switches for non-subscriptions (product, place); use "from" prices on cards, "Price on request" or none if not given | — | Reflex | J | TS §17, TS §23, HM §239 |
| CMP-145 | Each plan: name, who it's for, price + period, billing line, one button, 5-7 included lines; say every-plan inclusions once, not in each card | 5-7 lines | Finish | M | TS §141-142 |
| CMP-146 | Comparison table rows 48px with 1px rule; cells use check (SR "Included"), dash ("Not included") or short value; on phone each option its own block, never sideways scroll | 48px | Finish | M | TS §143 |
| CMP-147 | Explain the pricing model and define the unit of usage | — | Reflex | J | AS §166-167 |
| CMP-148 | Reference/anchor and struck-through prices must be real prices actually charged | — | Floor | J | ADP §169, KM §273 |
| CMP-149 | Put offers beside the cancel button, never in front of it; no hidden links, stacked confirmations or guilt copy; never invent trial deadlines or reset timers | — | Floor | J | ADP §64-65 |

### Empty, loading, error, success
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-160 | Empty state: one line naming what is empty, one on why it matters, one action; never a bare "No results" or blank screen; don't overload with options | 3 lines, 1 action | Reflex | J | HM §95, HM §321, UX §96, ADP §52 |
| CMP-161 | No-results search shows suggestions ("Try searching for X") | — | Reflex | J | UX §110 |
| CMP-162 | Error copy: what happened, why if known, what to do, with a recovery path (retry, edit, help link); no "Oops", no exclamation marks | — | Reflex | J | HM §95, UX §97, UX §238 |
| CMP-163 | Spinner after 150-300ms, shown ≥300ms, beside the label; "Loading…" text past 2s; skeleton for >1s or known shape; never a bare spinner 10s+ | 150-300ms / 2s / 10s | Reflex | M | HM §95, HM §321, UX §113, UX §133, UX §233 |
| CMP-164 | Reserve space for async content (aspect-ratio, fixed slots for counts/badges) so nothing shifts; CLS < 0.1 | CLS < 0.1 | Floor | M | UX §21, UX §233 |
| CMP-165 | Optimistic update: change at once, roll back on failure with a persistent "Try again"; success says nothing | — | Finish | J | HM §323, HM §336 |
| CMP-166 | Request timeouts show clear feedback with retry; offline messaging and degraded modes | — | Reflex | J | UX §238, UX §233 |
| CMP-167 | Never confirm success before it happened; never block progress with a success state | — | Floor | J | ADP §55, HM §311 |
| CMP-168 | Announce changed counts/status as a complete phrase without moving focus; search result count once after debounce | debounce 250ms | Reflex | M | UX §231, HM §337 |

### Onboarding
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-180 | Every tour step has visible Skip and Back; never a forced linear tour | — | Floor | M | UX §108, UX §230 |
| CMP-181 | Let people browse first; ask for an account only when they try something that needs it (lazy registration, guest access); never bury sign-in | — | Reflex | J | ADP §30, ADP §34-35 |
| CMP-182 | Don't force email verification before a useful first session where abuse risk is low | — | Finish | J | ADP §33 |
| CMP-183 | Welcome screen only when the next step isn't obvious; never a feature tour or chain of modals; not at every login | — | Reflex | J | ADP §37 |
| CMP-184 | Coachmarks/hotspots: a few at most (1-2 hotspots per screen), placed off their target, never mid-task, never for must-act info; fix usability first | ≤2 | Reflex | J | ADP §47-48 |
| CMP-185 | Onboarding checklist: each task links to where it's done and auto-checks; compact, dismissible, retired when complete; never tick tasks not done | — | Finish | J | ADP §50 |
| CMP-186 | Ask for system permissions when the user reaches the feature, never at launch; never disguise a screen as the system dialog | — | Floor | J | ADP §43 |
| CMP-187 | Multi-step flows show "Step N of M" and allow back; each wizard step fits above the fold; give experts a faster path | — | Reflex | M | UX §98, UX §238, ADP §21, ADP §23 |
| CMP-188 | Template galleries keep a "Blank" option; suggested next action is one clear step, dismissible, never upgrades/invites before value | — | Finish | J | ADP §53-54 |
| CMP-189 | Role-based invites never default to broad permissions | — | Floor | J | ADP §42 |
| CMP-190 | Usage meters show "used of total", what's counted, when it resets; warn at ~80%; at the limit block only the next action; red only for reached limits | 80% | Reflex | M | ADP §63 |

### Search, settings, data entry
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-200 | Autocomplete: debounced, ranked by relevance, ≤~10 suggestions, matched part highlighted, Esc closes, typing reopens; not an overview of all options | ≤10, debounce 250ms | Reflex | M | ADP §101, UX §109, HM §337 |
| CMP-201 | Search reachable with recent/suggested queries; docs/marketplace heroes may make search the primary CTA | — | Finish | J | UX §239, UX §210, UX §216 |
| CMP-202 | Command palette opens at once on ⌘K or `/`, input keeps focus, arrows move a highlight, Enter selects, Escape closes; rows never animate on filtering | — | Finish | M | HM §338 |
| CMP-203 | Settings hold rarely changed preferences; frequent actions go in a toolbar | — | Reflex | J | ADP §16 |
| CMP-204 | Drag/reorder always has a single-pointer and keyboard alternative (Move up/down, arrow keys + live region) | — | Floor | M | ADP §1, UX §151, UX §231, HM §335 |
| CMP-205 | No gesture-only actions: swipe-to-delete also has a visible Delete; pull-to-refresh also has a visible refresh or auto-update | — | Floor | M | UX §150, ADP §91 |
| CMP-206 | Chip collections wrap or use an operable +n disclosure; badges are static text, chips are buttons only when actionable; status never by colour alone | — | Reflex | M | UX §25, UX §106-107 |
| CMP-207 | Essential text (headings, actions, errors, distinguishing names) is never clamped to make cards uniform; clamp + ellipsis is the only truncation gesture | titles 2 lines, summaries 4 | Reflex | M | UX §105, KM §159 |
| CMP-208 | Inplace edit only for one/few simple values; never mix editable text with links | — | Finish | J | ADP §6 |

### Conversion / landing section patterns
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-220 | Proof only from the brief: a named quote with a face, a footnoted figure, real press lines, permitted logos; never big stat rows, filler stat strips, check-icon lists or logo walls | — | Floor | J | TS §93, HM §4, HU §60 |
| CMP-221 | Show counts (subscribers, waitlist, stars, users) only when current, verified and dated | — | Floor | J | UX §206, UX §217, KM §276 |
| CMP-222 | Scarcity, countdowns, limited seats and "X viewing" only when real and timestamped; expose deadlines as text | — | Floor | J | ADP §142, UX §212, UX §218 |
| CMP-223 | Testimonial walls: real attributed quotes only, ordered by credibility, ~9-12 before expansion, one "Show all", never pushing pricing out of reach; replace quotes with expired facts | 9-12 | Reflex | J | KM §163, KM §272 |
| CMP-224 | FAQ: questions in the buyer's words (≤60 chars), answers start with the answer (≤50 words / 1-2 sentences); first question is positioning; 5-8 questions | 5-8 | Reflex | M | TS §145, KM §274 |
| CMP-225 | Gallery of real captures: 3-6 panels; captions add information, never repeat the heading | 3-6 | Finish | M | KM §269 |
| CMP-226 | Feature copy answers "so what?" in 2-3 sentences; mechanics fold into FAQ; principles 4-6 | — | Finish | J | KM §270-271 |
| CMP-227 | Any carousel/auto-rotation has prev/next, pause, keyboard access, stops on hover/focus/reduced motion/offscreen, and announces position | — | Floor | M | UX §196, UX §209, UX §231, HM §87, HM §254 |
| CMP-228 | Loops >5s carry a visible pause control (WCAG 2.2.2) and stop off-screen and under reduced motion | 5s | Floor | M | HM §87, HM §254, TS §24 |
| CMP-229 | Present features and metadata as a definition list (term one weight heavier), not icon tiles | — | Finish | M | HM §98 |
| CMP-230 | State each fact once where it does work; a fact in ≥4 sections reads as filler; the price appears at most twice | ≤2 price mentions | Reflex | M | HM §109, TS §16, KM §273 |
| CMP-231 | Never mark a missing fact with lorem or bracketed placeholders on the page; use a dashed inline fill span that reads naturally, ≤2 per page | ≤2 | Reflex | M | HM §250, TS §24, UX §104 |
| CMP-232 | Never apologise for missing material ("coming soon", "example", empty/grey frames); give named client asset slots a finished-looking stand-in at the final ratio | — | Reflex | H | TS §23, TS §88, TS §140 |
| CMP-233 | No div-built fake product UI (invented dashboards, task lists, terminals); a UI fragment is the client's real UI at true size with their content | text ≥11px, 13/12 default | Floor | J | TS §22, TS §587-588, HM §238 |
| CMP-234 | UI fragments: every edge keeps 24px of ground or is cut by ≥24px with a fade; a fade never covers the point; never centred with even ground on all sides | 24px; fade 64px | Finish | M | TS §587, TS §590-591 |

### AI-product UI patterns
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-250 | Label AI-generated content visibly; never present AI as human | — | Floor | M | UX §112 |
| CMP-251 | Stream responses token by token; never a bare spinner for 10s+ | 10s | Reflex | M | UX §113, AS §327 |
| CMP-252 | Offer refinement after output (regenerate, thumbs, refine); make clear whether a refinement replaces or adds | — | Reflex | J | UX §114, ADP §59 |
| CMP-253 | Suggested prompts for new users of open-ended input, refreshed with context; no generic or show-off examples | — | Finish | J | ADP §58 |
| CMP-254 | Cite sources when output draws on documents/data/web; never cite a source that doesn't support the claim; group markers by sentence/paragraph | — | Floor | J | ADP §60 |
| CMP-255 | Chat UI: minimal chrome, streaming text, context awareness; chat input Enter respects IME composition | — | Reflex | J | UX §493, UX §79 |
| CMP-256 | Show an AI product's real subject in the hero/fragments (a queue being worked, an answer with real sources), not a generic chat bubble or gradient orb | — | Reflex | J | TS §588, TS §592-593, HU §60 |
| CMP-257 | Atmospheric genre (AI-creative): canvas first, then the tool; accent only in canvas treatment, focus rings, small tags; no glow shadows, mesh gradients or glass panels | ≤2 fixed radial blooms 20-30% each | Reflex | H | HM §242 |
| CMP-258 | Never gate the first experience of value; scatter no gates so widely the free product feels like an ad | — | Reflex | J | ADP §61 |

### App screens
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-270 | App colour restrained: accent marks the primary action, current selection and state only; a second neutral carries sidebars, toolbars, panels | — | Reflex | J | HM §144, TS §588 |
| CMP-271 | Keep the project's own shell; a new one is a top bar; standard patterns (tabs, breadcrumbs, command palette) beat invented ones | — | Reflex | J | HM §144 |
| CMP-272 | Density is the design: controls 32-40px with 44px hit target, one container recipe, even density across the screen | — | Reflex | M | HM §145, HM §159 |
| CMP-273 | App motion is state only, micro/short durations, nothing orchestrated; no reveal on load | 120-220ms | Reflex | M | HM §143, HM §145, UX §143 |
| CMP-274 | Use native menus, sheets, stacks, tab bars and headers on mobile instead of JS imitations | — | Reflex | J | AS §203-212 |
| CMP-275 | Prototype boards: never 5-6 equal phones in a row; enlarge the key screen 1.2-1.4x, others smaller at uneven heights; every phone ≥300px wide and clickable | 1.2-1.4x | Finish | M | HU §178-179 |
| CMP-276 | Never hand-draw a browser or OS window or device chrome ad hoc; use a precise standard frame or none | — | Floor | J | HM §4, HU §177, HM §216 |

---

## Named tests
- **Mirror test** — Ask whether a neighbouring brief in the same category would get this exact shape, hero, nav, footer and first section. Pass: no; if yes, change one decision and name it. (HM §12)
- **Rival's-name / competitor-name test** — Put the nearest rival's name (or the same trade in another town) into the h1, sub-line and every heading. Pass: no line stays true. (HM §14, TS §642; HU §97 "different client name" caps Concept ≤5)
- **Swap test (headings)** — Read headings alone; any head that would work on a competitor's page fails and gets a noun only this brief has. (HM §101, HM §157)
- **Anatomy test** — Could this exact sequence of sections sit under a different business's name? Is the job's action where real category sites put it? Are the category's own sections present? Pass: no / yes / yes. (HM §17, HM §518)
- **Squint test** — Blur the words; each section keeps a shape and the page a heavy/light rhythm. Hierarchy score 5 requires it. (HM §210, HM §151, HU §99)
- **Delete-the-picture test** — Remove the hero image mentally; if the screen says the same thing the picture is too weak or small. (HM §47)
- **Cover-text test** — Cover all text and logos; the theme should still be recognisable (type-led layouts: would the treatment hold under another theme?). (HU §97)
- **One-sentence idea test** — State the design's idea in one sentence; if you can't, Concept fails. (HU §97, HM §15)
- **Over-device test** — Remove the device/metaphor; if information gets clearer, it was too much. (HU §54)
- **Filler test** — Remove an element: worse? If not, delete. What real problem does it solve? If "less empty", delete. Backed by real data? If not, don't write it. (HU §71, HU §101)
- **Mirror-before-leaving** — Before shipping, take one accessory off. (HU §7)
- **Eyebrow test** — Delete the small line above a heading; if only a name for what comes next was lost, it was an eyebrow. (HM §111)
- **Headings-and-hero read** — Read only the hero and headings; if they tell the story the page is the right length. (HM §30)
- **Screen-by-screen scroll** — Scroll at 1440x900 one screen at a time; every screen needs something big enough to be its reason; outranks all detail findings. (HM §157, HM §210)
- **Judge tile** — Screenshot at scrollY = k x H (900 at 1440, 844 at 390); each tile shows exactly one section, no neighbour's heading. (TS §71, TS §78)
- **Five-second test** — A stranger understands what is sold, for whom, in five seconds; first screen conveys core value. (TS §4, HU §158)
- **Thumbnail capacity test** — Sketch three five-second thumbnails per screen (~480x300 with real fonts/palette/skeleton) to check content fits before building. (HU §16, HU §53)
- **Fingerprint / repetition test** — Record six axes (heading placement, body composition, divider language, button voice, image treatment, reveal); share ≤3 with any of the last three builds. (HM §233-234, HM §519)
- **Distinctness test (directions)** — Palette oklab mean distance <0.06, skeleton edge-map correlation >0.55, or same bg class + serif/sans + display face = collision. (HU §69)
- **Six-axis pre-emit critique** — Score philosophy, hierarchy, execution, specificity, restraint, variety 1-5; <3 revises; name weakest axis. (HM §151, HM §515)
- **Concept veto** — Concept ≤5 caps overall at 6.0. (HU §97)
- **Fresh-eyes review** — Review hero alone then full page with no build memory; rescore fixes resolved/partial/unresolved. (HM §155, HM §520)
- **Fresh-reader test** — Give only page text; ask what it is, who for, why over alternatives, cost, hesitation, and which three lines sound like any site. Never iterate to beat a detector. (TS §642)
- **Comp reproduction check** — Screenshot the build at comp dimensions; compare mass, interval, entry (where the eye lands first); name the largest divergence. (HM §149)
- **Phone parity test** — No ≥40 words shown at 1440 and hidden at 375; no table opening with ≥2 columns off-screen. (HM §435)
- **Single-line sweep** — Listed one-line surfaces hold one line at 1280 and 375 in every locale; one wrap found means sweep all. (KM §145)
- **Benchmark briefs** — Run no-numbers product, component-not-page, same-theme-twice, vague-prompt briefs to surface defaults and fabrication. (HM §523)

## Conflicts
- **Container**: HM 1440 cap / 64 gutter (1312 content), 1360-1520 cap at 1920; TS 1280 wrap at 1440; KM 1120; UX max-w-6xl/7xl (1152/1280), 1400 at 2xl. Keep "one capped centred container" as the rule; record value per system.
- **Column gap**: HM 32px; TS 24px (12 under 640).
- **Spacing scale**: HM 2,4,8,12,16,24,40,64,96,144; TS 4..128 (incl. 32, 48); HU 8pt only (8/16/24/32/48/64); UX 4/8. All agree on a 4px base.
- **Section gap**: HM 120/144/176 mixed (≥120); TS 128-480 between content (WARN 64-600); KM ladder 96/72. HM requires variation; TS requires a repeated scaffold.
- **Section height**: TS mandates every section exactly 1 or 2 screens (house rule); HM uses 520-900px sections. Treat TS screen-tiling as theme/house-specific.
- **Hero sub-line**: HM ≤12 words; TS 15-30 words (also "≤20 words, ≤4 lines"). HM headline ≤7 words vs TS 2-8 words.
- **Hero height**: HM/TS exactly one screen; HU says 100vh (conflicts with vh ban: use svh/dvh); HM Banner posture 50-60%.
- **Split mirroring**: HM allows one mirror/swap a page; TS and KM never mirror (text left always).
- **FAQ**: TS no accordion, all answers open; KM collapses FAQ by default on phone; HM conversational FAQ allows disclosures; UX uses accordions.
- **Carousels/tabs**: TS bans carousels, marquees and tabs outside software; UX and KM allow auto-rotation (KM 4500ms) with pause controls. Floor is the controls; whether to use them is Reflex.
- **Toasts**: UX success toasts auto-dismiss 3-5s; HM bans toasts for visible effects, dwell 4-6s, error toasts persist.
- **Disabled opacity**: HM 0.55; UX 0.5 or 0.38-0.5.
- **Destructive confirm**: UX "Are you sure?" dialog; HM undo-first, type-to-confirm for irreversible; TS no modal confirmation on forms.
- **Validation**: HM on blur then every input; UX native on blur + submit, not per keystroke.
- **Pricing emphasis**: HM by button and a word, never card colour; TS "Most popular" badge on middle card; UX colours per tier (reject as slop).
- **Price display**: KM never display-size the price; HM allows "a price set huge because it is the offer" as a signature.
- **Breakpoints**: HM two rem breakpoints (60rem/40rem); KM 880/480; UX 375/768/1024/1440 or 640/768/1024/1280/1536.
- **Prose measure**: UX/HM 60-75ch; KM document body fills the container (no article max-width) but screen prose ~720px.
- **Bento**: HM composition 4-6 tiles, shape 6-9 blocks; TS 1 large + 4 small (span-8+4 then 3x span-4); HU "don't overuse".
- **Eyebrow on hero**: KM allows one hero eyebrow (category + version); HM/HU ban eyebrows.
- **Z-index**: HM 1/10/100/200/300/400/500/600; UX 10/20/30/50 or 0/10/20/40/100/1000.
- **Table row height**: HM 56-72 marketing; UX 40/48/56 app.
- **Logo row**: HM requires permitted customer marks, no "Trusted by" line; TS allows one docked row of ≤6 permitted logos ≤96px; both forbid invented marks.
- **Nav**: TS fixed, opaque, 72px, identical at every scroll depth; HM 56-80px, many types incl. floating pill and retracting banner.
- **Choosing**: TS "deal at random, never by taste"; HU/HM "go wide, pick the one a design lead would fight for".

## Theme-specific, keep in library
- KM invariants: parchment #f5f4ed, single ink-blue #1B365D accent, warm greys, one serif, no italic, no bold — kami theme only.
- TS deal lists (nav-mega/nav-cards/…; footer-dark/statement/…; rhythm dark-band/surface-pairs/space), card radius 20, lit panel grounds (sand/sky/sage/painting), shader effects per kind.
- TS one-section-per-screen tiling with `--padt` 120 / `--padb` 72 and section heights 1H/2H.
- HM type scale 84/60/52/25/21/16/14 and twelve-column math at 1440 (column 80, gap 32).
- HM genre "allowed/refused" lists (editorial fleurons and drop caps; atmospheric blur pill; playful hard-offset shadows).
- HU iPhone 15 Pro frame values and Pomodoro demo values; HU warm/cool tweak palettes.
- KM landing button recipe (pill 999px, 13px 28px padding, min 158px) and gallery transition values.
- TS place-page palette/photograph counts per trade (cafe, bakery, guesthouse, florist).

## Coverage notes
- awesome-design-patterns has rich onboarding/AI/persuasion patterns but few numeric thresholds; rows lean on "use when" logic.
- agent-skills contributes little to D02/D07/D08 beyond page-purpose, pricing-model and native-mobile component rules.
- AI-product UI is thin across sources (UX §112-114, ADP §58-60, TS mocks); settings and search have few specifics.
- Dashboard layout (UX Part 45) and slide layouts (KM Part 17, HU Part 15) were only skimmed; slide/deck composition belongs with SLD-.
- Grouping/proximity beyond heading spacing (Gestalt laws) is barely stated in any source.
