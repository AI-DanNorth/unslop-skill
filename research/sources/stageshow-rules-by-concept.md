# Faux Product UI Rules by Concept

Distilled from Stageshow (benjitaylor/skills, commit `299140f`, 4 Nov 2026, MIT; the brand SVGs carry their own licences): a skill that builds faux product UI for marketing pages (hero shots, feature cards, bento tiles and cursor demos) and rehearses it with a film checker. Read from `SKILL.md` and `references/` (craft, framing, motion, bento, annotations, backgrounds, brands, choreography, looks, products, rehearse, review, verify, teaching).

**Scope.** Every rule here is written for a *product illustration*: a mockup, product shot or demo animation of an interface, seen on a marketing page, docs page or feature card. It is not a rule for the product UI itself. Story, framing, loop and pace rules in particular apply only to illustrations and demo animations. Rules that only concern Stageshow's React kit, its class names or its film tooling are left out; their underlying principle is kept where one exists. Pixel values are in the source's stage design pixels (a hero beside copy is designed at about 720 × 340, shown at 1:1).

# Part 1 — The one idea and how a mockup fails

## 1. The one idea
- A product illustration reads as a real product, simplified to what the viewer needs, framed with intent, and every motion has a cause.
- It is a believable interface, framed in its space, as one still or a short animation in which one thing happens; the viewer recognises the screen and sees the thing happen.
- Most of the quality is decided before any code: write down where it sits, the focal object, the action, the payoff and what can be left out.

## 2. The five ways a mockup fails
- **Too much:** real text in every row, numbers everywhere, everything packed. The more detail, the more it looks generated.
- **Wireframe:** two gray blobs and a button; built too small, or stripped of what made it recognisable.
- **Boxed:** a whole window shrunk into a card with even margins: a screenshot pasted in, not a product shot.
- **Flat:** every object the same weight in the same bordered card; the eye has nowhere to land.
- **Bland:** a gray window with a cursor, whatever the brief said. The brief's look and energy (a blueprint, glass over colour, a Dynamic Island, a mascot) are the point.
- The fix: a full, structured screen in quiet grays, real words only on what the story is about, placeholder lines for the rest, room to breathe, and a crop that puts the eye where the story is. Simplify the words, not the context.
- An empty corner, a void under a list, rows spread to fill a pane, a window floating on a plate: unfinished, not calm.

## 3. Faults that come back every round
- Content that swaps instead of moving.
- Gray bars where the eye lands; filler belongs at the edges.
- A plate behind the window, or a window floating with air on four sides.
- Empty bands, cut controls and cut shadows.
- Stock AI and made-up logos: sparkles, purple, a letter in a coloured square.
- Busy rows and uneven insets.
- Long holds and a reset with no cause.
- A text selection that is not under the I-beam.
- A status bar or home indicator drawn by hand.
- A centred amount centred together with its currency sign.

## 4. The exacting-designer test
- Look at the frame the way the most exacting designer you know would: the one who screenshots the single wrong thing and sends it back with "what is this?" (a dot off its avatar, a unit on its own line, a grabber under the island, copy touching a card). If you can picture that screenshot, you have found the next fix.
- Compare against the best reference beside it: if yours is the emptier, flatter or smaller one, that is the first fix.

## 5. Medium, place and size
- Decide still or animation (loop, once in view, or on hover), the page, its ground and its width before building.
- Design at the size it will be seen: about 720 × 340 for a hero beside copy, 900 to 1100 wide for a full-width hero, 400 × 300 for a card, shown at 1:1.
- Never under about 320 wide for a demo; a bento tile or a satellite card may be smaller.
- Every demo that can sit in a phone column ships a compact design at the column's width (about 358 in a 390 viewport): a redesign, not a squeeze.

# Part 2 — The still frame: restraint

## 6. A word budget
- Count the real strings: the title, the thing acted on, what is typed, the result; usually 3 to 7. The rest is placeholder bars.
- A word budget is not an element budget: a calendar needs a populated week, a search a collection, a filter enough rows.
- Keep only the text needed to recognise the product and follow the beat; extra logs and timestamps are noise.
- When the output is the subject (a log, a diff, a terminal), real lines are the content: short and few, the rest of the screen quiet.

## 7. Words on the subject, bars at the edges
- Bars are the product's filler; the subject is words. Bars where the eye lands read unfinished.
- In a still the subject is real words and values; a sidebar or list of bars beside it is filler and fine.
- Label and value match: both words or both bars. A blank pill beside a real control is dead; leave it out.
- Placeholder widths vary row to row (60, 45, 70, 52).
- A placeholder bar follows the text rules: it never touches or runs under an avatar, badge, icon or bar, and sits in the same line box as the text it replaces.
- Bars keep their lines' white space, not their line pitch: 6 and 5px bars want 7px between.

## 8. Lists and the skeleton ladder
- Where the story touches a list, two or three real rows and at most as many bars.
- Skeleton ladder: at realistic fidelity, a list in frame (4+ rows) where the wordless rows (at least 3) outnumber the worded ones reads unfinished.
- At realistic fidelity a list of six or more rows has at most as many placeholders as real rows.
- Named avatars take their own colour; gray discs are filler only.
- Keep the domain's signature content (album art, thumbnails, avatars); swapped for the feature's signal it is a generic list.

## 9. Small surfaces
- In a small surface (a popover, a card, a tile) a row is one line: avatar, name, value. No gray bar under a real name there.
- One number gets to be big; the rest are lines.
- A terminal is a character grid: a spinner and a tick share one `1ch` cell; each line owns its mark, swapped in place.

## 10. Say it once
- One clear signal for the feature, not repeated in header, satellite and every row; a second confirmation only when it differs.
- No masthead for a fictional name: no monogram, logo, sidebar and nav in every crop; a real mark only when recognition needs it.
- The product's name appears only when the brief leans on it and the real product would show it there (a notification's app name, the app's own title bar).

## 11. Simplify and compose
- Simplify before polishing: the fewest surfaces and strings that explain the product, then borders and badges only where earned.
- Simplification keeps the character: cut repeated framing before meaningful imagery; an empty white card is not the cure.
- Judge the silhouette before the details: at thumbnail size the subject, the support and the empty space make one picture.
- Compose objects, not an inventory of cards: hierarchy from proportion, space, material and ground, not more boxes.
- The heaviest marks sit on what the story is about; never a 2px black underline under a gray bar.
- Nothing outsized: the hero element sits in proportion to a real screen.
- A specimen still describes one plausible app: title, toolbar, navigation and body agree.
- Density follows the story: would a person do this here? No element quota; enlarge content before adding anatomy.

## 12. Space follows the story
- The payoff gets the room; no empty band mid-window while the result is pushed into the crop.
- No gap above a card, no cream under a phone's last row, no void between a stat's label and its number.
- Empty pane: a void under a pane's or screen's content is a fault; put more product into it until it runs off the crop, or crop the pane; never spread the rows.
- Loose list: rows spread out to fill a pane, with more air between them than they are tall, is a fault.
- Fat row: a one-line row three times taller than its words is a fault.
- A short history sits at the top of its pane under the header, never pinned to the bottom with a void above.
- Dots, halos, badges and focus rings sit fully inside the content edge.
- Check imagery at its smallest size and over every surface it crosses; a pale thumbnail can look see-through.

# Part 3 — Type in a mockup

## 13. Type
- Fit the text before fixing the box: a control's border-box holds content, padding and border; flex centring does not make it fit.
- Small text gets a line height of at least 1.3 and insets on every side.
- Real sizes, then scale: 11 to 15px UI text, scaled with the stage; never 7px type. Text under 10px at widths under 600 reads small.
- Tiny text (9 to 10px type shrunk to fit more in) reads as a wireframe: 13 to 14px names, 11 to 12px metadata, fewer rows.
- One family: the product's or the system stack. Monospace only for code, identifiers and aligned numbers, never a technical product's labels. In a code demo, real syntax-highlighted code with sans-serif labels and copy: monospace belongs to the code, not the whole scene.
- Sentence case unless the real product uses capitals; hierarchy from spacing and one weight step. Tracked capitals on headings, labels and buttons are a style fault.
- No real headings: a faux app's title is not an `h1` to `h6`; the demo lives inside someone else's page outline.
- Unsized text: text left at the page's 16px baseline because nothing sized it is a fault.

# Part 4 — Spacing and alignment

## 14. Insets and control gaps
- Words keep a 12px inset from the edge of a window, card, panel or hovered row; under 8px is a tight inset. Bars may bleed; words do not.
- A button keeps 8 to 12px from the field, line or card edge above it; under 8px it reads as touching, much more and it drifts off from the field it belongs to.
- A floating card (a comment popup, a toast) pads the same all round, measured to the avatar's and button's edges, not their words.
- Carry the inset round the bottom; a comfortable top does not excuse a cramped action.
- Content clears the bar above it: a first heading sits at least the side inset below a toolbar or title bar's rule.
- Uneven padding: a card or tile whose content sits about a third closer to one edge than the side inset is a fault. Uneven inset: a bar, pill or row of controls whose children sit much closer to one end than the other. Uneven gutters: a window or panel in a tile much closer to one side than the other.

## 15. Rows and stacks
- Row padding is 12px, 8px for a dense list.
- A title over its subtitle reads as one item: 4 to 6px of ink between the lines (a 1.3 line height plus a 2px gap); under 3px is tight, past 10px in a small label is loose. The air comes from the row's padding.
- Whitespace groups: a title sits closer to its metadata than to the next record; never spread lines equally to fill a frame.

## 16. Nothing touches
- Text never touches a neighbouring box: a fixed gap of 8 to 12px, never leftover `space-between`. Text within 5px of a box is touching.
- A status dot, badge or ring is not a column: in the gutter or on the avatar, 6px clear, inside the row's inset; within 5px of the avatar or text is a tight mark.
- A control hugs its content; never stretched with its contents at one end (lopsided).
- Fix overflow by fitting the content, not by widening the container; re-measure padding after.
- Content running past the width it was laid out in, or closing its row's gap, spills its slot.

## 17. Optical centring
- Centre a label on its letters, not its line box: capitals sit low in a plain line box, so a label beside an icon, in a pill, or an initial in a disc reads low. Trim to cap height and baseline.
- Field text centres cap height to baseline.
- Centre on the visible face: take tracking back; a pair centres as a pair.
- Align the reading edge, then the visible ink: a small icon aligns with the title's first line.
- A centred amount centres its digits: `$45` centred as one string sits right of centre to the eye. The currency sign hangs off the left, outside the centring; a rolling amount rolls only the digits.
- Centre glyphs by eye: shift a play triangle toward its point by a sixth of its width.
- A number in a progress ring centres on its digits with proportional figures, trimmed to cap height.

## 18. Nested shapes
- Nested shapes pad evenly (a pill inside a field, an icon inside a button: the same distance from every edge), and the outer radius equals the inner radius plus that padding.
- A popup under a field draws its ring inset so its sides line up with the field's.
- Two rounded clips sharing an edge with different radii (a double corner) are a fault: give one the corner.

## 19. Near-tangents and edges
- No near-tangents: edges 1 to 3px apart read as an accident. Line them up exactly, or part them by at least the gutter and never under 8px.
- Don't end just short of an edge: real room, or move it down and crop it.

## 20. Columns
- Columns line up: every row shares one grid template with fixed tracks; optional content keeps its track empty; bars vary inside their track.
- A body under an avatar row starts at the name's edge, not under the avatar.

## 21. Hover, pressed and open states
- Links have no hover surface; a control gets a surface visible at rest.
- Hover and selection fills are inset and rounded unless the real product draws square fills.
- A trigger with its popover open keeps its pressed look.
- A filled button keeps its colour under the pointer: one step of its own colour, never a gray swap.

## 22. Progress rings
- A progress ring is one track and one arc with round caps, never butt-capped dashes chopped into segments.

# Part 5 — Icons and logos

## 23. Icons come from a set
- Imagery earns its place: real imagery or a good icon, never invented illustration; gray art only for empty states.
- Icons come from a set, never from your hand: the product's own pack first, otherwise a set chosen on purpose, used at one size and one stroke width throughout.
- A glyph drawn by hand is the first tell of generated UI: its weight never matches its neighbours.
- No hand-drawn marks (pin, cursor, badge, ringed dot, chip, contactless arcs); use real assets or leave them out.
- A drawn mark gets a close-up beside the real thing, seen as a stranger would; zoom every hand-drawn thing at 4x.

## 24. Choosing a set
- Choose a set on purpose: filled SF-style glyphs for Apple, Material Symbols for Android, else Phosphor, Iconoir, Radix, Tabler or Heroicons; Lucide deliberately, never reflexively.
- Apple chrome uses SF-style glyphs; a Lucide glyph only where no system glyph exists.

## 25. One family, one stroke, one size
- One family, one stroke weight, one size (14 to 16px) per scene; equal boxes can still hide a heavy fill beside a thin outline.
- Mixed icons: filled and outline glyphs side by side in one nav, list or toolbar are a fault.
- Small icons are filled: at 14px and under, and in tinted tiles, use the filled style; thin outlines go wiry.
- Icons are one opaque colour; fade with opacity on the whole svg; no duotone. A translucent ink paints darker wherever strokes cross (onion skin).
- Even glyphs in even boxes; an odd icon in an even box snaps when motion ends.
- An icon drawn past its box (a clipped glyph) is a fault.
- Fixed boxes don't shrink: an icon button or chip in a flex row keeps its size.
- Invented icons (glyphs drawn for the demo, in rainbow tiles, filled beside outlined) are a style fault; colour only where it carries status.

## 26. Emoji are content
- Emoji are content, never icons. A playful look rounds the icons; it does not swap them for emoji. Emoji stay in messages and reactions.

## 27. AI shorthand
- AI features get no sparkle, wand or star, and no purple as the AI colour. Show what the AI does.
- Sparkles, wands and gradient "AI" chips say nothing about the feature: use the product's own mark, or a plain label that says what happens.
- The product's own icon is fine even when it is a sparkle; a sparkle as generic AI decoration is not.

## 28. Invented marks and real logos
- No invented logo: a letter or glyph in a coloured square is not the product's mark. Use the product's real mark, or a plain text wordmark.
- A real company named in the scene carries its real mark, never an initial in a brand-coloured tile: that is an invented logo beside a real name. A real name and a fake mark together are the one thing never shipped.
- A fictional product may use a neutral initial tile; never an initial or a hand-drawn approximation in place of a real mark that exists.
- Use current real artwork from the official brand source; third-party icon catalogues keep outdated colours and logos.
- Logos keep original proportions and colours, `object-fit: contain`, never stretched; keep native colours even in a monochrome UI.
- A mark that ships as a glyph on a solid square field is shown as the glyph alone in its brand colour on the same tile as the other marks.
- Optical sizing: a narrow mark and a full mark get the same presence; tall marks need air above and below, wide marks show in full.
- Use only the integrations the scene needs: a small row explains a relationship; it does not fill spare space with logos. Equal tracks, marks aligned by eye.
- Never a look-alike of another product's logo.

# Part 6 — Colour, looks and grounds

## 29. Colour in a mockup
- One neutral family for window, sidebar and cards; a coloured ground or another material differs on purpose.
- Five inks and one accent to start; status colours mean status.
- No redundant tonal borders: try the fill alone; add the border for separation, state, or because the product draws it.
- Quiet is not faint: check text, actions and surface against the real ground.
- A gradient or glow serves the story or goes. Glow (coloured light on the card, button or status) is a neon template: one soft neutral shadow instead.
- Purple slop: a violet-to-pink gradient ground, gradient text and a tinted card read as generated. Use the product's own neutrals and one accent on the thing that matters.
- The hero isn't outlined to point at it: an accent ring with a soft halo around the card the story is about reads as a focus state nobody gave it, and a dot beside its label is a mark with no meaning. A ring is for a field that really has focus.
- In mono, mark the thing acted on with a solid step in surface and weight, never a translucent wash.
- Nothing translucent overlaps (onion skin): stacked chips or cards take opaque fills.
- On dark themes depth comes from a lighter surface, not shadow.
- A light document over a dark workspace stays a readable light document with its own foreground and edge.
- Status colour stays legible: success, pending and disabled distinct.
- Contrast has a purpose: a near-black strip for no reason is a hole.
- Colour changes between distant hues take about 200ms (they pass through mud however done).
- A light pass does not prove dark: check every theme shipped.

## 30. Looks from the product's own tokens
- Use the product's own look whenever there is one: its real colours, radii and type read as the product, not as a generic mock.
- From a codebase: find the tokens (custom properties, Tailwind config, theme files) or read the computed styles of a real button, input, menu and card, and map them.
- From a public site: take the values, not the assets; no unlicensed fonts or images.
- A look sets tokens only; the scene keeps the product's own motion habits and real timing.
- Check it: a still of the demo beside a screenshot of the real product at the same scale; accent, gray temperature, radii and type match at a glance.

## 31. Grounds
- Choose the ground for what it does: a quiet solid gives dense UI room; a colour field or pattern makes a sparse picture distinctive; keep a calm area behind useful text.
- A vivid ground does not also need vivid controls, a coloured shadow and a glow.
- Texture supports a material; it does not sit over text or stand in for hierarchy.
- Never present a CSS landscape as a photograph; a drawn "photo" reads as generated however much grain and haze it gets.
- Grounds support the subject; a muddy halo standing in for foreground contrast does not.
- An object drawn as a tile gets one light source, a real material and a shadow that agrees with its neighbours; a drawn payment card keeps its real anatomy (chip about an eighth of the width, a third of the way down).

# Part 7 — Chrome and devices in a mockup

## 32. Chrome
- Does the frame help? Browser chrome only when the browser is part of the picture; a desktop app gets its real chrome.
- Chrome for the task: a sharing panel needs a document, permissions and an action; a browser bar explains nothing.
- Never draw platform chrome from memory; open the real app or a screenshot first.
- Columns run the full height of their window; a column that stops short leaves a seam.
- A document that is not the hero is content: a ruled page with real margins, not another window.
- Several windows: choose the active step; quieter contrast and shadow push the others back. Three equally loud surfaces compete even when all of them fit.
- Platform conventions are not placeholders: Messages' blue, a macOS window's lights, an iOS banner at true size stay. Send back an invented accent or a redrawn system control, never the convention.
- A messaging app on an iPhone keeps Messages' conventions unless the brief gives it a look.
- Balance a top bar: one control and an empty side reads as unfinished.

## 33. Phones
- System surfaces keep their real proportions; never shrink the iOS clock. Notifications stay at true iOS proportion; a phone so small its notification needs enlarging is too small.
- A notification is one bold title over its message with a real app icon.
- Nothing sits under the Dynamic Island; a sheet or grabber starts below the status bar.
- The status bar and home indicator are true to iOS, never drawn by hand.
- A phone is lit from its first frame: never dimmed, blacked out or faded up.
- A phone background has a job (a lock screen for notification stories); never invented home-screen icons.
- A phone may straddle a window but never covers the amount it explains.
- A phone cropped at the top loses its status bar and nav bar together.
- A banner is native width and never cut by the crop.
- A satellite phone starts at 40% of the window's visible width and at least 220px wide; let it run off the bottom rather than shrink.

# Part 8 — Framing

## 34. Hero and satellites
- One hero object, at most one or two satellites (a receipt, a phone, a detail card) that carry the point.
- Satellites straddle the hero's edge, about half outside, never fully inside or floating apart; fully outside, tie back with a 1px leader ending in a dot.
- Two satellites are two kinds, not a stack: never two cards of one width on one edge (twin satellites).
- A satellite covers chrome, not content: straddle where the window has a sidebar, header or margin.
- Related surfaces get different jobs and weights; the result sits in the hero's quiet margin, never hiding settings, trigger or payoff.
- Anchored UI (popover, menu, toast) is not a satellite; it sits where the product would put it.
- A satellite arrives at the beat it pays off, carrying its payload, or is present from the first frame; never an empty parked object.

## 35. Crop only filler
- Keep what identifies the product: a title, the real chrome, the rows that give the action a reason. Logo and nav are not required.
- Crop only filler: the payoff, the action, what the cursor touches and every real word stay whole; a list, diff or terminal may run one line off a bled bottom edge.
- A button, chip or shadow sliced by the frame edge is the usual fault; a placeholder action the crop would slice is removed, not sliced.
- Crop 10 to 40% of the hero off stage: the window or phone fills at least two thirds of the stage's width and runs off an edge.
- Labelled controls stay whole; shapes that read when cut (a card, a slider track, a row of avatars) run off by a third or more.
- What the story opens stays in frame, a gutter from every edge on every frame.
- Is a bleed a deliberate crop, not a sliver? Every edge where screen meets stage fades, bleeds with intent, or is a real window edge.

## 36. One gutter
- One gutter, measured in the final crop: the hero's inset from the stage edge; every other edge distance in the frame matches it.
- A full gutter or well past, on every edge: crossing by under 24px or stopping a few pixels short is a mistake.
- On a coloured stage the hero is inset 8 to 20% from the sides and runs off the bottom.
- No dead corners at rest or anywhere in the loop.

## 37. The page is the ground
- The page is the ground: on a white or dark page, no plate (a backdrop or tinted field the window floats on) and no panel behind the device.
- A hero's window bleeds or fills; whole and centred with air on four sides, it floats.
- A whole window with even gutters is valid only when its contents read and the brief asks; unframed is the developer's call, with an even margin at least as deep as the shadow.
- The stage is the shot: never a stage boxed in another ground.
- A window keeps its device's shape: whole, 1.25:1 or wider; bled, what shows is at least square. Fix by crop or layout, never by squashing.

## 38. Depth and tilt
- Start flat and frontal; earn a tilt by comparing with the straight version at final size. Depth from shadow, z-order, scale and opacity; perspective only when asked.
- Distinct depth: a tighter shadow on a satellite sitting on the hero, a hairline and long faint fall for a lone surface; the shadow on the outlined shape, never a wrapper.
- One figure language across a page of demos: one ground, one gutter, one window shadow, one radius set; a different shadow says something or is a mistake.
- Tilt earns its keep for paper (a loose pile of receipts or tickets at small alternating angles, about -6, 4 and -2 degrees), the straightest on top and the only one with words.

## 39. Fades
- Fades are for sliding tracks, stacks and charts, and for one crop: a window fading out at its foot over its last third, over filler only, by mask not colour overlay.
- Never fade a side, never fade the focal content, never fade more than one window in a scene.

## 40. Layout recipes
- Corner bleed for a hero beside copy (inset 10% top and left, 15 to 35% past right and bottom); pinned bottom bleed for a card or tile (inset 8 to 12% left, right and top, 15 to 35% past the bottom); a phone pinned from the top.
- Satellite focus: the hero cropped hard as context, a satellite 30 to 40% of hero width carrying the story.
- Wide hero: a 900 to 1100px window at 1:1, inset top, off the bottom.
- Device pair: desktop about 75 to 80% wide, phone straddling the right edge about a third outside, present from frame one.
- Many of one: a grid of one small thing off every edge, one tile in focus by depth, the only one with words.
- Close-up: the whole window scaled 1.3 to 1.6x, chrome and all, the subject row whole.
- Stacked cards: two components at one width and left edge, 12px apart, the lower off the bottom.
- Monochrome row: other companies' windows in grayscale, faded at the foot, where their brand colours would fight.
- The layouts are recipes, not a requirement to crop every product.

## 41. Small formats
- Small formats crop harder: a 400px card holds a third of a dashboard at full size, not all of it at a third.
- Size the design for the slot: a lone card in a 680px column wants 500 to 560 wide so its text reads at 15 to 20px.
- A desktop screen scaled into a small slot passes an overflow check while its text becomes unreadable: reflow before shrinking.
- Moving a window keeps the bleed: after any move or resize, recheck what the crop cuts.

# Part 9 — Bento grids

## 42. Bento as one picture
- A bento grid is one picture made of tiles, not five demos side by side. A grid where every tile is a cropped window reads as generated however well each window is made.
- Not every tile is UI: about a third to a half of the tiles show product UI; the rest are stats, statements, objects, diagrams, collections or photos.
- One hero: one tile is bigger (two columns or two rows) and carries the richest picture. Four equal tiles of heading and bars read as a template.
- A UI tile shows one thing, not a window: crop to the single component the tile is about, at real size or larger. Window chrome appears at most once in a grid, on the hero.
- Neighbours contrast: alternate kinds like a checkerboard; two window crops never sit side by side.
- Say each thing once across the set: no real string, avatar, colour mark or chrome repeats from tile to tile.
- Every tile is a specific moment with its words on it; no tile that is a title over bars.

## 43. Bento tiles and copy
- Big type is a tile: one real number at display size (48 to 72px as shown), a short lead, a one-line label, at most one coloured glyph. Real figures, never "10x" filler.
- The number sits close under its copy or fills the tile; a stat pinned to the bottom of a tall tile with a void above reads as missing content.
- A stat is one line: the number and its unit never wrap (unit wrapped); size the number to fit, or move the unit into the lead line.
- Copy is short and outside the picture: one to four words or one sentence, at most one supporting sentence; never a paragraph or a bullet list. Tile copy is page type, 17 to 24px, never the 12px of the UI inside the tile.
- One frame, varied contents: tiles share radius, gap, padding and copy position; the gap equals the tiles' inner padding or a clear fraction of it.
- Compose the grounds together; don't repeat the same gradient or spend every accent everywhere.
- Give motion one place to lead: a supporting tile does one small thing, once as the grid scrolls in, staggered 80 to 120ms in reading order, or on hover for that tile alone. Several competing loops leave the eye nowhere to land.
- Never scale the whole grid as one picture: tile titles shrink with it (15px titles drawn at 9.5px). Important text stays at least 10px at a 320px host.
- A drawn "photo" tile reads as generated; with no licensed photo, pick another kind of tile.
- Never centre a picture about as wide as the tile so it touches both edges or loses a few pixels to each.
- An inner fixed-width picture must not slice a window halfway across a wider tile and leave a blank strip beside it.

# Part 10 — Annotations and connecting lines

## 44. Annotations
- An annotation explains one relationship; if the layout already makes it obvious, leave the line out. More connections do not make a fuller explanation.
- Design the product before its annotations: a line that attaches perfectly cannot rescue faint text or weak hierarchy.
- A leader is a fine line with two clear ends: 1px (1.5px at hero scale) in a quiet ink, landing 4 to 6px short of the object, ending in a 4px dot or a gap; straight or one bend; never through another surface.
- Direction shows transfer: a request and its response start from different ends; a decorative two-headed line cannot say that.
- Moving dots only while data is flowing, on a fixed route; never on a finished one-off request; static under reduced motion.
- One relationship, one colour, rather than a hue per joined input.
- An annotation is not permission to cover the result it explains.
- A bad example on a page of demos is marked in the page's own annotation style, never with crosses or scrawls.

# Part 11 — Motion in a demo animation

## 45. Story shape
- Pick the shape from what the product is valued for: how it feels to use (one satisfying gesture), a flow in an app (a few screens as one continuous object), or what the system does (the consequence lands somewhere else; usually no cursor).
- Beauty decides: the calmer, fuller, better-framed version beats the one with more story.
- A hero loop is 10 to 16 seconds; three to five beats building to a payoff; one gesture and a response can be enough.
- Open on a finished screen that works as a still; the first real content is on screen before the beat.
- Motion without hierarchy: cover each moving element in turn; if the story gets clearer without it, cut it.
- No cursor move you can't explain; between a richer story and a calmer frame, choose the frame.

## 46. The payoff and the poster
- The payoff is visible at the shown size: a panel, a window coming forward, a clear state change. A 16px avatar at the edge is not a payoff.
- The payoff arrives full: a panel or card opens with its content, never a blank surface for a quarter second.
- The poster is the frame most people see (a thumbnail, reduced motion, a screenshot): choose the beat that tells the story on its own, leave the result on screen, and never pick a frame caught mid-change.
- Cover the motion and ask what happened; if the poster can't answer, choose another beat.

## 47. Loops
- A reset removes what the loop added as one thing, with a seen cause where one exists (undo, clear, close), an exit around an anchor, or a snap while hidden.
- Every reset has a cause or is invisible.
- A loop never plays a navigation backwards; undo the state in place in a quick reverse stagger (last change first, about 70ms apart).
- Data never rewinds in view.
- No dead air at the seam: within about a second of the exit ending, the next action has begun.
- Exiting around an anchor: what the story added leaves in one reverse stagger within half a second, 40 to 80ms apart, while product content stays.
- The payoff holds for 2s before the exit; nothing on screen sits still for more than three seconds.
- A second scene earns its length by adding something new; repeating the beat doubles the loop for nothing.
- A looping video starts on a calm frame, never mid fast motion.
- A loop keeps a complete product picture: open on context and return to it.

## 48. Pace and easing
- Storytelling motion is unhurried, on two curves: travel `cubic-bezier(0.45, 0, 0.1, 1)`; arrival from nowhere `cubic-bezier(0.25, 0.8, 0.25, 1)` over 0.8 to 1s. Judge distance and overlap, not duration.
- Travel has a departure, clear travel and a soft arrival.
- UI feedback stays as quick as the real product; only storytelling motion slows down. Feedback starts on the input; a presentation delay feels unresponsive.
- Choose durations and easings together by job; one easing everywhere flattens the hierarchy.
- Related responses overlap: a changed setting leads its label, then its dependents; a confirmation still follows its cause. Dependent changes that all start together read as one jolt.
- Stagger groups in reading order 40 to 80ms apart within a scene; 80 to 120ms between tiles of a grid.
- A small expressive icon may overshoot while its card and text settle without bounce.
- Holding a result means stop: a useful still needs no new pulse or repeated count.
- Phone in-app responses are UIKit-quick: `cubic-bezier(0.3, 0.75, 0.1, 1)` over 0.5s.

## 49. Changing text and values
- Every change moves: text that turns into a pill, a menu replaced by another in one frame, a number that jumps are faults.
- Change only what changed: animate the changed span and move what follows by its measured width.
- A status word that changes rolls in one slot, never two spans crossfading in place (they read as a smudge); several rows changing at once cascade about 60ms apart.
- Decide a control's footprint before its label transition; button states share one slot; a button whose label changes changes on itself, never swapped for a second button.
- Added content opens its space with its neighbour: an icon's width and gap open together while the label travels.
- A right-pinned value changes against that edge.
- Numbers roll last digit first, unchanged digits still; hold the completed value.
- Result follows press feedback: a small press and surface response before the result.
- An object keeps its identity when it changes (a plus becoming a close rotates the same strokes).
- A spinner turns before it is visible and keeps turning through its fade out.
- Inspect the glyphs, not only the box: text can shimmer or shift as layers settle.

## 50. Appear, travel, leave
- Nothing pops: everything has an entrance and stays mounted until its exit finishes.
- No holes or blank frames: what replaces something arrives as it leaves.
- Neighbours make room continuously as the newcomer arrives; a new row carries the rows below it.
- A resizing surface moves size, position and content as one transition, never stretching its text, and retargets from its current geometry when interrupted.
- Keep header, outer surface and action positions steady while variable content changes inside.
- Solid things do not fade through: windows, phones and cards arrive by moving, opaque or nearly.
- Cards, toasts, pills and reactions arrive whole from just above, never uncovered by a hard edge; clip only rows of text.
- Content arrives after its container.
- A popup fits before its first frame; it never corrects its size while opening.
- An open surface holds its anchor: a popover or menu is pinned by the edge it opened from (anchor drift is a fault).
- A dashed edge never changes size; border style does not transition.
- A moving edge never slices text.
- One object, one trip, ending in its final place; after motion nothing moves (no handoff shift, no settle snap).
- Landings are soft: decelerate over the last third, no bounce, no ring pulse.
- A thing that grows as it travels takes the long settle (600ms or more).
- A page swap inside one window keeps the chrome and crossfades only the body (200ms, an 8px rise); never slide whole pages sideways.
- Look at every motion finding: fix the real ones, name the intentional, never cut good motion to quiet a detector.

## 51. The cursor
- No cursor means no stand-in: never walk a focus ring, halo or spotlight between controls.
- The elements decide the cursor's kind (I-beam over text, hand over links, resize on edges), switching mid-path, never after arriving.
- The cursor never covers the words it clicks: aim inside the target but off its text.
- The cursor rests on empty surface between beats, near its next move, never on an unused control.
- A state the click sets fades in quickly (about 150ms), never switching on in one frame.
- The cursor stays where the press happened while the result changes size.
- Every move travels to the next action, follows a held object or clears the way.
- Keyboard stories show the keys.
- Touch on a phone uses a touch indicator, never the macOS arrow.

## 52. Drags and selection
- A pointer drag is one motion; a drag starts where the thing is, with a fixed grab offset.
- A text selection reads left to right from a word boundary and stays under the I-beam every frame.
- A carried card is held, not slid: scale 1.03, deeper shadow, a degree or two of tilt, the whole card tilting with its words; it settles flat on drop.
- Drop targets never travel; a held item rides with the cursor exactly.
- A swipe is a flick: a third of the screen in about a quarter second; a swiped row stays in its list with its action as the row's own back.

## 53. Scrolling and the camera
- Nothing scrolls unless the pointer is on it; scrolling starts with whole rows.
- The camera needs a reason: push in only when the payoff would be too small to read; the zoom never rescues a weak frame.
- One push-in per story, in and back out; the cursor holds still while the view moves.

## 54. Choreography of a change
- Start with a readable still and a short account of the change: the frame that holds still, the state that starts things, the dependent responses, the destination and the hold.
- Timing has different jobs: direct feedback starts on the input; travel has departure, travel and arrival; related updates each take their own time; holding a result means stop.
- Use a fixed, local soft mask where a track enters and leaves; don't soften the whole interface, blur every transition or use a mask to hide bad resting geometry.
- Under reduced motion the motion shows the poster, still and complete; drop presentation waits, keep task timing and reading time.

# Part 12 — Teaching pairs

## 55. Style faults
- Purple slop: a violet-to-pink gradient ground, gradient text and a tinted card read as generated.
- Tiny text: 9 to 10px type shrunk to fit more in reads as a wireframe.
- Over-detailed: a branch, hash, author, duration and badge on every row makes every row the subject; real detail on the one row the story is about.
- Glow: coloured light on the card, button or status is a neon template.
- Capitals: tracked caps on headings, labels and buttons.
- Invented icons: glyphs drawn for the demo, in rainbow tiles, filled beside outlined.
- AI shorthand: sparkles, wands and gradient "AI" chips.
- Onion skin: an icon in a translucent ink paints darker wherever its strokes cross or join.

## 56. Motion faults
- Instant label replacement; result without press feedback; a new row shoving its neighbours; an object losing its identity; a skipped exit; an interrupted motion restarting; a landing jumping at handoff; a loop erasing accumulated work with no cause; added content shifting its neighbour; a list jumping around a new row; a changing action shoving another; surface and content resizing separately; a drag starting from the wrong point; a spinner beginning after appearing; text shifting as it settles; a label hitting a hard edge; scrolling revealing a harsh crop; dependent changes starting together.
- Matching endpoint screenshots prove nothing about the frames between.

## 57. Composition faults
- Several equally loud windows compete even when all fit; a whole application shown as an unreadable thumbnail; a new result that is one thin row in a long list loses to the list; four equal tiles of heading and bars; a phone covering the amount it explains; tinting everything alike on a coloured ground removes the separation.
- Draw a chart on from its start: the line draws left to right and the end dot lands when the line reaches it.
- Choose copy that fits: names, emails and values whose length suits the layout; no truncated chips, wrapped names or ragged labels.

## 58. Making a comparison
- Change one thing: same content, layout, endpoints and input timing; only the behaviour being taught differs.
- Say the exact difference under each side; make it readable at normal speed.

# Part 13 — Review and verification method

## 59. Lines that are never intentional
- A gate of faults that are never judgment calls: framing faults, a cut action, tight or loose stacks, tight marks, tight insets, skeleton ladders, onion skin, wrapped units, unsized text, clipped glyphs, loose lists, fat rows, empty panes, emoji icons, anchor drift, uneven padding, mixed icons, tight controls, invented marks, uneven insets, uneven gutters, avatar misalignment, content spilling its slot, and a selection drifting from the I-beam.
- Clearing a line by hiding, removing or marking the thing it points at is a bug; a fresh eye re-judges every line called intentional.

## 60. Fresh-eye review
- The reviewer gets the frames, the URL, the checklist and the references; never the builder's plan, reasons or rehearsal notes.
- First question: does this composition answer this product and this page, or could it be any product in its category? A layout the brief did not shape is a finding even when every check passes.
- Start from the brief's own words: if it says "white page", a tinted plate is the first finding.
- The bar for a finding is a frame; a predicted failure is not a finding, and neither is a predicted pass.
- Rank by how much of the scene it spoils, not by how easy it is to fix: framing, then hierarchy and density, then motion, then polish.
- Do not soften a finding because the build is nearly there. Say what you could not check; if nothing, say "nothing" and list the frames looked at.

## 61. Verification
- Every answer comes from a frame you looked at, never from the code. Fix the largest visible failure first, re-shoot, return to the top.
- Empty, short or gapped recordings are inconclusive, not a pass; "no issues detected" is not approval.
- A contact sheet misses a one-frame flash; a checker can flag a jump and still miss a wrong path, an implausible gesture, a bad story or an unreadable crop. Say what the tools covered and what you watched yourself.
- Ten runs, gate green, frame unchanged: stop and get a fresh eye.
- Hand over with a record of what was captured (widths, looks, states, reduced motion), what was changed, the assumptions, what is unresolved and what was not checked.
