# F (source 21) — Stageshow: product illustrations, mockups and demo animations

Source: `research/sources/stageshow-rules-by-concept.md` (Stageshow, benjitaylor/skills @ `299140f`, MIT). Source key: stageshow. § = numbered concept in that file. Decision record: `research/notes/stageshow-review.md`.

This file is named `F-…` so that `scripts/build/build_rules.py` (glob `[A-F]-*.md`, sorted) reads it last: its rows get the next free id for each prefix and no existing card id moves. Do not insert rows into the earlier mining files for this source; add to this file.

**Scope.** Stageshow is written for faux product UI on marketing and docs pages. Every row in an area marked *product illustration* applies only to a mockup, product shot or demo animation of an interface, never to the product UI itself. Spacing, icon and text-change rows hold for real UI too, but their pixel values are stage design pixels (a 720 × 340 hero shown at 1:1): re-derive them on Unslop's controls before a detector uses them. Tiers: Reflex only for clear slop tells; everything else is Finish advice. Nothing here is Floor.

Rows where Stageshow says the same as an existing row were not repeated; `stageshow §N` was added to that row's sources instead (mined id → card id): A SLP-062 → SLP-162, SLP-064 → SLP-164, SLP-073 → SLP-173, SLP-091 → SLP-191, SLP-092 → SLP-192; B TYP-017 → TYP-117, CLR-020 → CLR-120, CLR-058 → CLR-158, CLR-093 → CLR-193; C LAY-027 → LAY-120, LAY-069 → LAY-146; D MOT-062 → MOT-137, MOT-063 → MOT-138, MOT-075 → MOT-147, MOT-164 → MOT-219, MOT-165 → MOT-220, MOT-173 → MOT-225; E IMG-004 → IMG-104, IMG-020 → IMG-120, IMG-064 → IMG-164, IMG-065 → IMG-165, IMG-071 → IMG-171, IMG-074 → IMG-174. Ids inside rows below ("related card …") are card ids.

## D03 Slop detection

### Slop tells in faux product UI and product illustrations
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| SLP-001 | Ban AI shorthand: a sparkle, wand or star glyph, or a gradient "AI" chip, as generic decoration for an AI feature, and purple used as "the AI colour". Show what the AI does, with the product's own mark or a plain label. The product's own icon is fine even when it is a sparkle. | SVG sparkle/wand/stars glyph (e.g. `lucide-sparkles`, `wand-2`) or ✨ beside an AI label; chip with gradient fill reading "AI"; violet accent used only on AI surfaces | Reflex | H | stageshow §27 §55 |
| SLP-002 | Ban the invented mark: a letter or glyph in a coloured square standing in for a logo, above all a one-letter tile in a brand colour beside a real company's name. Use the real mark or a plain text wordmark; a neutral initial tile only for a fictional product. | real company name + adjacent 1-letter tile in a saturated fill; related card IMG-171 | Reflex | H | stageshow §28 §59 |
| SLP-003 | Flag mixed or hand-made icons, "the first tell of generated UI": filled and outline glyphs side by side in one nav, list or toolbar; a hand-drawn glyph whose stroke weight differs from its neighbours; invented glyphs in rainbow tiles. | one group: fill mode differs, or stroke width differs at one size; ≥3 icon tiles of different hues with no status meaning; related card IMG-165 | Reflex | H | stageshow §23 §25 §55 |
| SLP-004 | Flag the skeleton ladder: a list where wordless placeholder rows outnumber the real rows, or gray bars sit where the eye lands. Real words on the subject, bars only beside it and where the crop cuts. | list ≥4 rows in frame, ≥3 wordless, wordless > worded (realistic fidelity) | Reflex | M | stageshow §7 §8 §59 |
| SLP-005 | Flag the over-detailed mockup ("Too much"): real text, numbers and badges on every row, so every row is the subject. Real detail on the one row the story is about. | e.g. branch, hash, author, duration and badge on each row | Reflex | J | stageshow §2 §55 |
| SLP-006 | Don't outline the featured card to point at it: an accent ring with a soft halo reads as a focus state nobody gave it, and a dot beside its label is a mark with no meaning. Lift it with its own surface, the raised shadow or an accent label. | accent ring + coloured halo on a non-focused card | Reflex | H | stageshow §29 |

## D07 Layout & composition

### Product illustration framing (illustrations and mockups only, not product UI)
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-001 | In a product illustration, show one hero object and at most one or two satellites (a receipt, a phone, a detail card) that carry the point. | ≤2 satellites | Finish | J | stageshow §34 |
| LAY-002 | In a product illustration, a satellite straddles the hero's edge about half outside, never fully inside or floating apart; fully outside, tie it back with a 1px leader ending in a dot. | ~50% outside; leader 1px + dot | Finish | H | stageshow §34 |
| LAY-003 | In a product illustration, two satellites are two kinds (different size and kind), never two cards of one width on one edge. | twin satellites = fault | Finish | J | stageshow §34 |
| LAY-004 | In a product illustration, a satellite covers the hero's chrome or margin, never its content, settings, trigger or payoff; anchored UI (popover, menu, toast) is not a satellite and sits where the product puts it. | — | Finish | J | stageshow §34 |
| LAY-005 | In a product illustration, bleed the hero rather than box it: the window or phone fills at least two thirds of the frame's width and runs off an edge, with 10 to 40% cropped. A whole window with even air on four sides floats ("Boxed") unless the brief asks for it. | crop 10-40%; width ≥0.67 of frame; shapes that read when cut run off ≥1/3 | Finish | H | stageshow §2 §35 §37 |
| LAY-006 | In a product illustration, the page is the ground: no plate (a backdrop or tinted field) behind a window or device on a white or dark page, and never a stage boxed inside another ground. | — | Finish | H | stageshow §37 §60 |
| LAY-007 | In a product illustration, use one gutter: the hero's inset from the frame edge, matched by every other edge distance in the frame; each edge gets a full gutter or well past it. | crossing an edge by <24px or stopping a few px short = fault | Finish | H | stageshow §36 |
| LAY-008 | In a product illustration, leave no dead corner: no empty frame corner at rest or anywhere in the loop; fix crop or layout first. | — | Finish | J | stageshow §36 |
| LAY-009 | In a product illustration, a window keeps its device's shape: whole at 1.25:1 or wider; bled, the visible part at least square; fix by crop or layout, never by squashing. | ≥1.25:1 whole; ≥1:1 visible when bled | Finish | M | stageshow §37 |
| LAY-010 | In a product illustration on a coloured stage, inset the hero 8 to 20% from the sides and run it off the bottom, so the ground frames it on three sides. | 8-20% | Finish | M | stageshow §36 |
| LAY-011 | In a product illustration, start flat and frontal; earn a tilt against the straight version at final size; perspective only when asked. Paper stacks are the one place tilt earns its keep. | stack angles about -6, 4, -2 deg, offset 12-20px; only the top card has words | Finish | J | stageshow §38 |
| LAY-012 | In a product illustration, fade only sliding tracks, stacks and charts, plus at most one window fading out at its foot over its last third, by mask over filler; never fade a side or the focal content. | track mask 32px; stack/chart last 25-30%; ≤1 faded window per scene | Finish | H | stageshow §39 |
| LAY-013 | In a product illustration, recompose for small slots instead of shrinking: crop harder, size the design for the slot, ship a compact design for a phone column. | lone card in 680px column 500-560 wide (text 15-20px); compact at 358 in a 390 viewport; demo never <320 wide | Finish | H | stageshow §5 §41 |
| LAY-014 | Across a page of product illustrations, keep one figure language: one ground, one gutter, one hero shadow, one radius set; a different shadow says something or is a mistake. | — | Finish | M | stageshow §38 |
| LAY-015 | In a product illustration, pick the first layout by medium: corner bleed beside copy, pinned bottom bleed in a card or tile, a phone pinned from the top; try a second layout before forcing the first. | corner bleed: inset 10% top/left, 15-35% past right/bottom; pinned bottom: inset 8-12% left/right/top, 15-35% past bottom; wide hero 900-1100px at 1:1 | Finish | J | stageshow §40 |

### Spacing and alignment inside mockups (values in stage px; principles hold for dense UI)
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-016 | Avoid near-tangents: edges 1 to 3px apart read as an accident; line them up exactly, or part them by at least the gutter. | 1-3px = fault; parted ≥8px | Finish | M | stageshow §19 |
| LAY-017 | Keep a button or chip 8 to 12px from the field, line or card edge above it; carry the inset round the bottom; a floating card pads the same on every side, measured to visible edges. | <8px = tight control | Finish | M | stageshow §14 |
| LAY-018 | Flag uneven padding and insets: content about a third closer to one edge than the side inset, controls bunched at one end of their bar, or a panel much closer to one side of its tile. | asymmetry ≥33% of the side inset | Finish | M | stageshow §14 |
| LAY-019 | Size rows to their content: row padding 12px (8px dense); never a one-line row three times taller than its words, nor rows spread wider apart than they are tall to fill a pane. | fat row ≥3x text height; loose list: gap > row height | Finish | M | stageshow §12 §15 |
| LAY-020 | Leave no empty pane: a void under a pane's content reads unfinished; add product until it runs off the crop, or crop the pane, never spread the rows. | — | Finish | H | stageshow §2 §12 |
| LAY-021 | Set a title and its subtitle as one item, and a title closer to its metadata than to the next record. | 4-6px ink between lines; <3px tight; >10px loose in small labels | Finish | M | stageshow §15 |
| LAY-022 | Text never touches a neighbouring box: a fixed gap, never leftover `space-between`. | gap 8-12px; <5px = touching | Finish | M | stageshow §16 |
| LAY-023 | Keep a status dot or badge clear of the avatar and text it marks, inside the row's inset; a dot is not a column. | 6px clear; <5px = tight mark | Finish | M | stageshow §16 |
| LAY-024 | Centre optically: labels on cap height (trim the line box), an amount on its digits with the currency sign hung outside, a play triangle shifted toward its point. | play glyph shift 1/6 of its width | Finish | J | stageshow §17 |
| LAY-025 | Line up columns: every row on one grid template with fixed tracks; optional content keeps its track empty; a body under an avatar row starts at the name's edge. | — | Finish | M | stageshow §20 |

### Bento grids of product illustrations
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-026 | Don't make every bento tile a cropped window: a third to a half of the tiles show product UI, the rest are stats, statements, objects, diagrams, collections or photos. Every tile a window reads as generated. | UI tiles 1/3-1/2 | Reflex | H | stageshow §42 |
| LAY-027 | In a bento grid, a UI tile shows one component, not a window; window chrome appears at most once (on the hero), and two window crops never sit side by side. | ≤1 set of chrome per grid; 0 adjacent window crops | Finish | H | stageshow §42 |
| LAY-028 | Say each thing once across a bento set: no real string, avatar, colour mark or chrome repeats from tile to tile. | 0 repeated strings | Finish | M | stageshow §42 |
| LAY-029 | Set a stat tile as one real number with its unit on one line, a short lead and a one-line label, close under its copy; never a stat pinned to the bottom of a tall tile with a void above, never "10x" filler. | number 48-72px as shown; ≤1 coloured glyph; unit never wraps | Finish | M | stageshow §43 |
| LAY-030 | Keep bento tile copy outside the picture and at page size: one to four words or one sentence, at most one supporting sentence; never scale the whole grid as one image so its titles shrink. | tile copy 17-24px; important text ≥10px at a 320px host | Finish | M | stageshow §43 |
| LAY-031 | Give bento tiles one frame and varied contents: shared radius, gap, padding and copy position; the gap equals the inner padding or a clear fraction of it; never a picture about as wide as its tile touching both edges. | — | Finish | M | stageshow §43 |

### Annotations on product illustrations
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| LAY-032 | Use a leader line only to explain one relationship the layout does not already show: a fine line in a quiet ink, straight or one bend, landing short of the object, never through another surface or over the result it explains. | 1px (1.5px at hero scale); lands 4-6px short; 4px end dot | Finish | M | stageshow §44 |
| LAY-033 | Make transfer lines directional: a request and its reply start from different ends; moving dots only while data flows, static under reduced motion; one colour per relationship. | — | Finish | J | stageshow §44 |

## D08 Components, states & flows

### Controls and states (from faux UI; principles hold for real UI)
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CMP-001 | Fit the text before the box: a control's border-box holds content, padding and border; small text gets a line height of at least 1.3 and an inset on every side. | line-height ≥1.3 | Finish | M | stageshow §13 |
| CMP-002 | A control hugs its content, never stretched with its contents at one end; fix overflow by fitting the content, not widening the container. | lopsided = fault | Finish | M | stageshow §16 |
| CMP-003 | A filled button keeps its colour under the pointer (one step of its own colour, never a gray swap); a trigger with its popover open keeps its pressed look; links have no hover surface, controls have a surface at rest. | — | Finish | H | stageshow §21 |
| CMP-004 | Inset and round hover and selection fills inside their list, unless the real product draws square fills. | — | Finish | M | stageshow §21 |
| CMP-005 | Give a button's states one slot: reserve the longest label's footprint, and change a label or icon on the same button, never by swapping in a second element. | check shortest, longest and pending labels | Finish | H | stageshow §49 |
| CMP-006 | Draw a progress ring as one track and one arc with round caps, never butt-capped dashes; centre its number on the digits. | — | Finish | M | stageshow §17 §22 |
| CMP-007 | Inside an embedded product illustration, a faux app's title is not a real heading: no `h1` to `h6` in the demo, which lives inside someone else's page outline. | 0 headings inside the illustration root | Finish | M | stageshow §13 |

## D09 Motion & interaction

### Demo animation: story and payoff (product illustration / demo animation only)
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-001 | In a demo animation, tell three to five beats building to one payoff; one gesture and its response can be enough; cut any motion whose removal makes the story clearer. | hero loop 10-16s | Finish | J | stageshow §45 |
| MOT-002 | In a demo animation, choose the poster frame (thumbnail, reduced motion, screenshot) as the beat that tells the story on its own, with the result on screen, never a frame caught mid-change. | — | Finish | H | stageshow §46 |
| MOT-003 | In a demo animation, make the payoff visible at the shown size and arrive full (never a blank surface for a quarter second), then hold it before the exit; nothing sits still much longer. | payoff hold 2s; no still >3s | Finish | J | stageshow §46 §47 |
| MOT-004 | In a demo animation, a satellite arrives at the beat it pays off, carrying its payload, or is present from the first frame; never an empty parked object. | — | Finish | J | stageshow §34 §45 |

### Demo animation: loops and resets (product illustration / demo animation only)
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-005 | In a looping demo, give every reset a seen cause (undo, clear, close) or make it invisible; remove what the loop added as one thing; never play a navigation backwards. | reverse stagger, last change first, ~70ms apart, all within 0.5s | Finish | J | stageshow §47 |
| MOT-006 | In a looping demo, data never rewinds in view: snap it back while hidden or bring the next loop's data in as new. | — | Finish | J | stageshow §47 |
| MOT-007 | In a looping demo, leave no dead air at the seam and start on a calm frame. | next action within ~1s of the exit | Finish | M | stageshow §47 |
| MOT-008 | In a looping demo, a second scene earns its length by adding something new; never repeat the beat. | — | Finish | J | stageshow §47 |

### Demo animation: pace and easing (product illustration / demo animation only)
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-009 | In a demo animation, storytelling motion is unhurried on two curves, judged by distance and overlap; this never applies to product UI (conflict register). | travel `cubic-bezier(0.45, 0, 0.1, 1)`; arrival from nowhere `cubic-bezier(0.25, 0.8, 0.25, 1)` over 0.8-1s | Finish | M | stageshow §48 |
| MOT-010 | In a demo animation, UI feedback stays as quick as the real product and starts on the input; only storytelling motion slows down. | phone in-app `cubic-bezier(0.3, 0.75, 0.1, 1)` 0.5s | Finish | J | stageshow §48 |
| MOT-011 | In a demo animation, related responses overlap in causal order (a setting, then its label, then its dependents); dependent changes never all start at once, and a result follows its cause. | — | Finish | J | stageshow §48 §54 §56 |
| MOT-012 | In a demo or bento grid, give motion one place to lead: a supporting tile does one small thing once as the grid scrolls in, or on hover for that tile alone; never several competing loops. | stagger 40-80ms within a scene, 80-120ms between tiles, reading order | Finish | H | stageshow §43 §48 |

### Changing text, values and surfaces (from demo animations; principles hold for UI transitions)
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-013 | Every change moves: no label replaced in one frame, no menu swapped for another in one frame, no number that jumps; text rolls, a surface morphs, a submenu slides. | content swap in 1 frame = fault | Finish | H | stageshow §49 §56 |
| MOT-014 | Change only what changed: animate the changed span and move what follows by its measured width; a status word rolls in one slot, never two spans crossfading in place. | rows changing together cascade ~60ms apart | Finish | H | stageshow §49 |
| MOT-015 | Added content opens its space with its neighbour: an icon's width and gap open while the label travels; a new row carries the rows below it; neighbours make room continuously. | — | Finish | H | stageshow §49 §50 |
| MOT-016 | Show press feedback before the result: a small press and surface response, then the state change. | — | Finish | J | stageshow §49 §56 |
| MOT-017 | An object keeps its identity when it changes: a plus becoming a close rotates the same strokes rather than swapping icons. | — | Finish | J | stageshow §49 |
| MOT-018 | A spinner is already turning when it becomes visible and keeps turning through its fade out. | — | Finish | M | stageshow §49 §56 |
| MOT-019 | Solid things do not fade through: windows, phones and cards arrive by moving, opaque or nearly; a half-transparent phone is a ghost. | — | Finish | J | stageshow §50 |
| MOT-020 | Cards, toasts and pills arrive whole from just above, never uncovered by a hard edge; a moving edge never slices text; clip only rows of text. | — | Finish | H | stageshow §50 §56 |
| MOT-021 | A popup fits before its first frame and an open popover or menu holds the edge it opened from while its content changes. | anchor drift = fault; reserve the longest list's height | Finish | M | stageshow §50 |
| MOT-022 | A resizing surface moves size, position and content as one transition, never stretching its text, and retargets from its current geometry when interrupted. | — | Finish | H | stageshow §50 §56 |
| MOT-023 | After motion nothing moves: one object, one trip, ending in its final place; the handoff frame matches size, place and look; landings decelerate with no bounce or ring pulse. | snap >2px on the settle frame = fault | Finish | M | stageshow §50 |
| MOT-024 | A dashed edge never changes size and border style never transitions; fade a dashed layer over the solid one instead. | — | Finish | M | stageshow §50 |
| MOT-025 | Change colour between distant hues quickly, letting the label carry the slower motion. | ~200ms | Finish | M | stageshow §29 §48 |

### Demo animation: cursor, drags and camera (product illustration / demo animation only)
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-026 | In a demo animation, explain every cursor move: it travels to the next action, follows a held object or clears the way; it rests on empty surface between beats and stays where the press happened. | — | Finish | J | stageshow §51 |
| MOT-027 | In a demo animation, the cursor never covers the words it clicks, and its kind follows the element under it (I-beam over text, hand over links), switching mid-path. | — | Finish | J | stageshow §51 |
| MOT-028 | In a demo without a cursor, never walk a focus ring, halo or spotlight between controls as a stand-in; states and timing carry the story. | — | Finish | J | stageshow §51 |
| MOT-029 | In a demo animation, a state the click sets fades in, never switching on in one frame. | ~150ms in and out | Finish | M | stageshow §51 |
| MOT-030 | In a demo animation, a drag is one motion that starts where the thing is with a fixed grab offset; a carried card is held, not slid; drop targets never travel; a text selection stays under the I-beam every frame. | carried card scale 1.03, deeper shadow, 1-2 deg tilt of the whole card | Finish | H | stageshow §52 |
| MOT-031 | In a demo animation, push the camera in only when the payoff would be too small to read; one push-in per story, in and back out, the cursor still while the view moves; the zoom never rescues a weak frame. | ≤1 push-in | Finish | J | stageshow §53 |
| MOT-032 | In a phone demo, use a touch indicator, never the desktop arrow; act where people do (tap the notification, act in the app), and throw a swipe at the finger's speed. | swipe a third of the screen in ~0.25s; thrown page 0.5s `cubic-bezier(0.25, 1, 0.5, 1)` | Finish | J | stageshow §51 §52 |
| MOT-033 | In a demo animation, a page swap inside one window keeps the chrome and crossfades only the body; never slide whole pages sideways. | 200ms with an 8px rise | Finish | M | stageshow §50 |

## D13 Imagery & iconography

### Product illustrations and mockups: content (illustrations only, not product UI)
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| IMG-001 | Judge every faux UI or product mockup against the five ways it fails: Too much (packed, real text everywhere), Wireframe (gray blobs, built too small), Boxed (whole window shrunk into a card), Flat (every object the same weight), Bland (a gray window whatever the brief said). | any one = finding | Reflex | J | stageshow §2 |
| IMG-002 | In a product illustration, budget the words, not the elements: the title, the thing acted on, what is typed and the result are real; the rest is quiet placeholder. A calendar still needs a populated week. | 3-7 real strings | Finish | H | stageshow §6 |
| IMG-003 | In a product illustration, put real words and values where the eye lands and bars at the edges; label and value are both words or both bars; placeholder widths vary row to row. | widths vary, e.g. 60, 45, 70, 52; no blank pill beside a real control | Finish | H | stageshow §7 |
| IMG-004 | In a product illustration, where the story touches a list show two or three real rows and at most as many bars; in a small surface a row is one line; one number gets to be big. | — | Finish | M | stageshow §8 §9 |
| IMG-005 | In a product illustration, keep the domain's signature content (album art, thumbnails, avatars) and give named avatars their own colour; gray discs are filler only. | — | Finish | J | stageshow §8 |
| IMG-006 | In a product illustration, say it once: the feature's signal appears once, a fictional product gets no masthead, monogram or nav in every crop, and the product name shows only where the real product would show it. | — | Finish | J | stageshow §10 |
| IMG-007 | In a product illustration, compose objects, not an inventory of cards: hierarchy from proportion, space, material and ground; the heaviest marks on the story; nothing outsized against a real screen; judge the silhouette at thumbnail size. | — | Finish | J | stageshow §11 §57 |
| IMG-008 | Build a product illustration in the product's own look: map its real tokens (accent, grays, radii, type, control height) from code or computed styles, taking values not assets, and check a still beside a real screenshot at the same scale. | accent, gray temperature, radii and type match at a glance | Finish | J | stageshow §30 |
| IMG-009 | In a product illustration, use type at real UI sizes at the shown size; text shrunk to fit more rows reads as a wireframe. | UI text 11-15px; names 13-14px, metadata 11-12px; never <10px at widths <600 | Finish | M | stageshow §13 §55 |
| IMG-010 | In a product illustration, use chrome for the task: browser chrome only when the browser is part of the picture, a desktop app with its real chrome, never platform chrome drawn from memory; platform conventions (Messages blue, macOS window lights, iOS banner size) are not placeholders. See the conflict register for drawn chrome. | columns run the full window height | Finish | J | stageshow §32 §60 |
| IMG-011 | In a product illustration with several windows, choose the active step; quieter contrast and shadow push the others back. | 3 equally loud surfaces = fault | Finish | J | stageshow §32 §57 |
| IMG-012 | In a product illustration with a phone, keep the system's real proportions: nothing under the Dynamic Island, true status bar and home indicator, notifications at true size and never cut, lit from the first frame, no invented home-screen icons, never covering the amount it explains. | satellite phone ≥40% of the window's visible width and ≥220px; cropped at the top loses status bar and nav together | Finish | J | stageshow §33 |
| IMG-013 | In a product illustration, take icons from the product's own pack first, else one set chosen on purpose; small icons are filled; icons are one opaque colour with no duotone; even glyphs in even boxes; no glyph drawn past its box. | 14-16px, one size per scene; filled at ≤14px and in tinted tiles | Finish | M | stageshow §23 §24 §25 |
| IMG-014 | Give a drawn object tile one light source, a real material and the real object's anatomy; a drawn card that gets proportions wrong gives itself away. | payment card chip ~1/8 card width, a third of the way down | Finish | J | stageshow §31 |
| IMG-015 | Choose an illustration's ground for what it does: a quiet solid for dense UI, a colour field for a sparse picture, a calm area behind text; a vivid ground does not also need vivid controls, a coloured shadow and a glow; texture never sits over text. | — | Finish | J | stageshow §31 |
| IMG-016 | Follow the brief's look in full ("Bland" is a failure): a styled brief gets its colours, radii, mascot and motion, still built to the craft rules. | — | Finish | J | stageshow §2 §11 |

## Named tests
- **Five failure modes** — Name which of Too much, Wireframe, Boxed, Flat, Bland a mockup shows; pass = none. stageshow §2
- **Exacting-designer screenshot** — Picture the one wrong thing a strict designer would screenshot and send back; pass = you can't. stageshow §4
- **Any product in its category** — Could this composition belong to any product in the category? A layout the brief did not shape is a finding. stageshow §60
- **Poster test** — Cover the motion and ask what happened; the poster frame must answer. stageshow §46
- **Gold beside it** — Put the still beside the closest good reference at shown size; say the one difference; if yours is emptier, flatter or smaller, that is the first fix. stageshow §4 §60
- **Anti-hiding** — A "fix" that hides, removes or marks the element a finding points at is rejected. stageshow §59
- **Ten green runs** — Ten runs, gate green, frame unchanged: stop and get a fresh eye. stageshow §61
- **Inconclusive capture** — An empty, short or gapped recording is inconclusive, never a pass; "no issues detected" is not approval. stageshow §61

## Conflicts
Recorded in `core/conflict-register.md` as C45 to C50:
1. Storytelling arrivals of 0.8-1s, 10-16s hero loops and 2s payoff holds (stageshow §45 §47 §48) vs UI duration scales (hallmark §83 420ms long; transitions-dev §9 "over 1 second is too slow for UI chrome"; uupm §143 (card MOT-128)).
2. Monospace never for a technical product's labels (stageshow §13; hallmark §396; huashu §59) vs mono labels in a technical direction (huashu §124; taste §30 §57).
3. "Lucide deliberately, never reflexively" (stageshow §24) vs Lucide as the default set (hallmark §278; ux-ui-agent-skills §161; taste §361).
4. Faux product UI with window and device chrome (stageshow §32 §33) vs bans on drawn chrome and styled-div product UI (hallmark §117 §118; huashu §407 (card VID-144)).
5. Small icons filled (stageshow §25) vs line icons with round caps (taste §361, hallmark §278 via IMG-067; kami §409 for diagrams).
6. Stagger 40-80ms in a scene and 80-120ms between grid tiles (stageshow §43 §48) vs 30-50ms rows and 60-100ms blocks (hallmark §83).

## Theme-specific, keep in library
- The kit's two shadow tokens, 38px window chrome, 12px window radius, `--ss-*` look tokens and the four built-in looks (light, dark, blueprint, glass).
- The 17 layout recipes beyond the summary in LAY-015, and the bento kinds-of-tile table: starting recipes, not rules.
- Dynamic Island timings (500ms underdamped growth, 380ms shrink delayed 120ms, press squeeze 0.965) and filter values.
- macOS 26 Finder specifics; Messages conventions on iPhone.

## Coverage notes
- Thresholds are stage design pixels for a ~720 × 340 frame; none is calibrated on Unslop's controls.
- Detector candidates from this source (ai_sparkle, invented_mark, mixed_icons, near_tangent, unit_wrapped, nested_radius) are not built; they need curated cards, thresholds and seeds (see the review note).
- Review and verification method (§59-§61) maps to PRC and verify-fix; not mined as rows here because Unslop's review method already matches it (see the review note).
