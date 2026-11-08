# Design Rules by Concept

Distilled from the Leonxlnx/taste-skill collection. Each concept is followed by its rules; exact values are kept wherever the source gives them.

# Part 1 — Philosophy and stance

## 1. The bar
- Build the website a good company would ship: say plainly what is sold, show the real thing on every screen, look made for this client, not from a template and not like an art piece.
- Use figma.com and x.ai as the quality bar; beside their frames the page must read as a professional company site.
- Go past the reference sites: they still let a neighbour section show in a one-section shot; the house does not.
- Make the hero the work, not a mood: the client's product, place or work, never a colour field.
- Get the look from heights and padding only: every section exactly one or two screens.

## 2. House rules that win over everything else
- No caption or description under any image, render or visual; licence credits go in one footer line.
- Every visual renders, never an empty ground, at 1440, 1024, 768 and 390.
- One section per screen: the hero alone on the first screen; every section exactly one or two screens tall at 1440x900; no second section heading peeking in (sole exception: a live photo-chapters moment, three or four screens).
- Equal left and right content edges.
- Hover micro-animations everywhere they apply: linked card lifts 2px, photo zooms 1.02-1.03 inside its frame, buttons step on hover and press on click, underlines draw, card loops cycle in 2.5-4 s, repeat and restart on hover.
- Every hero enters once on load; every page carries one dealt moment, two on a long page.
- More and better real photographs where they fit; nicer backgrounds, better heroes, layouts and fonts.
- Real full-colour icons (a known product's real icon, never a drawn one).
- Small diagram visuals in cards: a hub with branches; one input, a main processor, three parallel lanes; pulses running along the lines.
- Shader effects and big scenes only where the trade has a technical subject (tech, AI, developer tools, gaming, fintech, hardware); never on a local cafe, bakery, guesthouse or shop: those get photographs.
- Addresses: street and district only (no street: the district); no house number, postcode or coordinates; no register or VAT numbers; no phone in a real format; contacts on `.example`.

## 3. Deal, never choose by taste
- Deal palette, type pairing, hero layout, nav, footer, close, rhythm, button look and mark from lists; keep a history so consecutive pages differ.
- Take the first palette and first pairing dealt; take the next only when the first clashes with the client's own logo or photographs, or the pairing fails the hero line stress test.
- Never deal the same hero within three pages.
- Write one sentence on why the palette fits the trade.
- Write all copy first, then plan the page as screens, then build.

## 4. Plain truth over style
- Say what it is and what it does, in words a stranger understands in five seconds.
- Every sentence must be one you would say out loud to a customer.
- No metaphors, poetry, invented terms or ad wording (the single permitted brand line aside).
- Study reference sites only for how they are written (plain, category first); never copy their words, code, pictures or signature effect.
- Precedence: nothing invented, nothing bracketed or left open on the page, no captions, the h1 names the category, buttons are a verb plus an object. These override every voice/register choice.
- The fix for model-sounding copy is facts and decisions, never synonyms: a word swapped for its synonym becomes the next tell.

# Part 2 — Reading the brief: kinds, modes and plans

## 5. The kind of business decides everything
- Classify first: software (app, SaaS, AI, developer tool, fintech/banking app, a studio selling its own software), gaming (a game, a studio launching its game), tech (hardware or a tech device: drone, robot arm, keyboard), product (any other physical product or brand: chair, bike, coffee beans online), service (people are hired: clinic, law firm, agency, creative studio, trade), place (people come to it: cafe, bar, bakery, restaurant, guesthouse, small hotel, shop, florist, bike shop, gym, local studio).
- Treat a maker that also opens its door or teaches (ceramics studio, bakery with web shop) as a place; its web shop becomes the goods section. It is a product only when nothing happens at the door.
- Treat estate, travel and insurance agents as service, never AI product; a kitchen fitter as a workshop.
- Reserve effects, scenes, loops, counts, CSS grounds, dark pages and dark heroes for tech (software, gaming, tech) only.
- Build "other" pages from photographs, flat colour, type, real icons, the hero entrance, its dealt moment (photo- or type-led) and the hover layer.
- Write down: the kind, what is sold, who buys it, the one main action (the transaction: Book a room, Order a cake, Start a free trial; a place with neither: Get directions) and the real material (logo, screens, photographs, prices, address, hours).

## 6. Write the plan first
- Line 1: the page kind. Line 2: the dealt structural choices (nav, footer, close, rhythm, button style, mark). Then one line per section: its id, its one idea, its picture (and that picture's kind), its screen count, and (tech) which section holds the effect, scene or moment.
- Choose nav, footer, close, rhythm, button style and logo mark at random from the kind's allowed list, never by taste; re-deal one only when its recipe's use does not fit. Record any re-deal and its reason.
- Re-deals when there is no photograph: picture-card navs become a split nav with no panel, or a centred nav; a photo close becomes the head row of the wordmark close without the name (h2 and one line left, main button right, on the container lines); a full-width media band becomes "space" rhythm (a game keeps it with a setting photograph); a place's photo hero becomes the statement hero on the brand-colour ground.

## 7. Asset use by kind
- Card loops and counts: software, gaming, hardware only.
- Real tool icons: software, hardware; product/service only tools really used; never on a place.
- Feature cards and UI fragments: lead on software (none on gaming); hardware its app; product/service only an app the client runs; never on a place.
- Diagram cards: software and hardware 0-2, pulsing; product/service 0-1, still; place none.
- CSS grounds: software/hardware 0-2 dealt; product/service/place flat tokens.
- Shader grounds: tech only, the one effect.
- Creative parts: product/service only plain fx-photo and still fx-map; place only still fx-map.
- Award-site moments: 1-2 on every kind (photo- and type-led off tech).
- Big scenes: 0-1 on software/gaming/hardware; never elsewhere.

## 8. What each kind gets: pictures, effects, moments
- Tech: lead picture = the client's UI (hardware: its photographs or CAD render, else stand-in photographs of its kind — never an effect or an order form alone; a game: its name and art, else its name over a stand-in photo of its setting; render only when 3D is asked). One effect (a live ground, a WebGL part, an object or a big scene). One card group of still grounds from the effect's family (with a big scene: the lit ground, no effect grounds). 1–2 moments (one may be in the hero). 0–1 big scene. 0–2 pulsing diagram cards. One timed loop plus one per card group. 0–2 CSS grounds.
- Product/service (other): lead = its photographs (no photographs: stand-in photographs of its kind; render only if 3D asked). No effect. Card panels hold the client's photograph. 1–2 photo/type moments. No scene. 0–1 still diagram. No loops. Flat tokens.
- Place: its photographs (a remote place: its region's landscape). No effect, no card grounds, no diagrams, no loops, flat tokens; 1–2 photo/type moments.

## 9. Deal lists by kind: nav, footer, close, rhythm, buttons, mark
- Software: nav-mega|nav-cards|nav-centre; footer-dark|footer-statement|footer-columns; close-type|close-word; dark-band|surface-pairs|space; solid|pill|tonal|arrow; wordmark|initial|arc|ring|stack|dots.
- Gaming: nav-mega|nav-centre|nav-cards; footer-dark|footer-statement; close-word|close-type; dark-band|media-band|space; solid|pill|block; wordmark|initial|arc|ring|stack|dots.
- Product and hardware: nav-cards|nav-split|nav-mega; footer-columns|footer-dark; close-photo|close-type|close-word; dark-band|brand-band; arrow|solid|block|pill; wordmark|initial|arc|ring|stack|dots.
- Service: nav-mega|nav-split|nav-centre; footer-visit|footer-dark|footer-columns; close-type|close-photo; surface-pairs|dark-band|space; solid|tonal|block|arrow; wordmark|initial|arc|ring|stack|dots.
- Tech lit ground: sand|sky|sage.
- Radius: sharp for fintech and developer tools, soft by default, round for consumer apps, square on a place.

## 10. Place page plan
- Let photographs lead: 12 to 20 on the full page, 8 to 12 compact; under 8 frames makes the 3-screen short page, whatever the trade.
- Make the hero a photograph whenever a frame fits (a remote place: its region's landscape).
- Put the visit block on screen two, never inside the first; then the offer, the place, orders or booking.
- Deal different compositions for the offer and the place; never two sections round one picture.
- Use one type moment (the address or name set large).
- One main action a screen.
- Set list text at 16px.
- Use flat grounds, square photographs, one button style, the phone action bar, the dealt moments.
- No effect, ground, loop, fragment, diagram or tab on a place.
- Every text on a place 4.5:1 or more; every word on the brand band 7:1.
- Never colour inside a word on a place.
- A short page (under 8 photographs) carries picture-develops on a section photograph, or with no photograph, word-highlight in a one-screen statement section.
- A place page totals 3 to 6 screens (enforced).

## 11. Place: plan and length
- The nav is not a screen; the closing footer counts as one; a 2-screen section counts two.
- Full page: 12 to 20 photographs, 2 to 3 per screen, at most 6 screens: hero, visit, the offer (optionally a second offer), the place, then orders or booking when taken (last before the footer, replacing the close), closing footer. Over 6 screens, drop the place, never the booking.
- Compact page: 8 to 12 photographs, 4 or 5 screens: hero, visit, offer, [the place], closing footer.
- Short page: under 8 usable photographs: 3 screens, 2,700px max at 1440.
- The photograph count decides the length, not the trade.
- Photos by section, all distinct: hero 1; visit 1 (0 with a map); menu or prices 1; rooms 2 to 6; goods 4; the place 3 (row), 1 (story) or a wall; orders 2 or 3, or booking 1; close 1. Nav panel photos don't count.
- The hero is always a photograph when any frame fits; a remote place (guesthouse, lodge, inn) leads with its region's landscape (in testing a remote guesthouse shown as a type band scored 3.5). Statement hero on the brand ground only with no frame of the region and no lead.

## 12. Place: section order by trade
- Cafe: menu as text with its composition; the place (composition or story); beans or goods only if sold.
- Bakery: goods with prices; orders (one card per kind); the process (strip or trio, one screen max); several shops as a ruled list each with its street.
- Guesthouse/small hotel: hero = the region's landscape; location as the visit (how to arrive, address moment fits); rooms; the house (shared spaces, breakfast; bleed for the land, no labels); booking. Check-in/out beside rooms and in the footer.
- Shop/bookshop: new in (goods with Add); categories as a plain text list; one story row; footer with each shop's address, hours and newsletter. Nav: four to six category words (four on split nav).
- Bike shop: visit and workshop (repair turnaround); workshop prices as ruled rows with "Book a service"; new in (cut-outs on white, name, price); brands as a plain text list; story.
- Florist: notice line with delivery area, cut-off and price; delivery and visit as screen 2; bouquets (four 4:5 tiles with "from" prices); weddings and events (three photos of real installations, what to send); workshops as ruled rows.

## 13. Place: look
- Palette made for the trade, never shared between two builds of the same trade; only light, low-saturation grounds. Justify it in one sentence from the trade (e.g. "a flour-white ground and the terracotta of a bread oven's tiles"). Client colours (shopfront, logo, bag label) replace it, the ground from walls, paper or shopfront.
- Grounds: palette ground and surface, one full surface band at most, one brand band, no other dark section; flat colour only.
- Accent once: primary button, focus ring and the colour-band close; a client colour darkened until its label passes 4.5:1 and it passes 3:1 on both grounds.
- Type: display 400, text 400 and 500; serif head + plain sans for bakery, restaurant, guesthouse; one plain sans in two weights for shop, bike shop, florist, studio; a soft sans for cafe or yoga studio.
- Motion: hover layer only and visible (underlines, 1.03 zoom with 2px lift, buttons step and press, arrows 3px); hero enters once on load; only the dealt moment's section moves on scroll.
- Rhythm options: surface-pairs (offer on one full alternate band; visit panel on alternate), space (one ground), colour-band (the close on the brand colour; then no name set across the footer).

## 14. Place: the short page (under 8 photographs)
- Three screens (2,700px max at 1440; four with no photograph): hero, one one-screen section holding the visit and the offer, closing footer.
- One or two photos: the best is the hero's, the other the section's. None: a statement hero on the brand ground (h1, sub-line, inverted button) and the section has no picture.
- The section is open type on the page ground, never a card or ground box: the offer as ruled text in groups (prices visible), then the visit block as three span-4 columns (address, hours with today marked, access; phone only if given). A maker's story is one 20/30 paragraph at the head of the visit block.
- With a photo: groups and photo in one top-aligned row, photo last, top level with group labels; visit block under at a large gap. Three groups: each span-3 with a 1:1 photo on span-3 (282x282). Two groups: each span-3 with a 3:2 photo on span-6 (588x392). Content ~560px at 1440. (A 4:3 span-6 runs to 852px, past the 828 limit.)
- Every group same row count; every name fits one line beside its price on span-3 (~24 characters).
- Under 640: section two screens tall, the photo after the groups at 16:9.
- Nav: three or four words, one per group, each to its group's anchor.
- Re-dealt without pictures: split nav no panel, close as the wordmark close's head row without the name; either the brand band or the name set wide in the footer, not both.
- Its one moment: a "picture develops" reveal on the section photo (needs half the container or more); with no photo, add one one-screen statement section (12 to 40 words from the brief) after the hero, making four screens (3,600px).
- Drops: no place section, no second offer, no place composition, type moment or rooms layout.
- Tablet (640 to 1023): the section stays one screen (content 600 to 830px at 768x1024) by keeping the three groups and three visit columns side by side (~700px). With a photo: two screens at tablet: screen 1 the h2 and the photo full width to the screen's bottom padding (h2 kept to one line), screen 2 the groups across and the visit columns (content 1,640 of 2,048 at 768).
- Grows to compact at 8 good photos, full at 12.

## 15. Product and service page plan
- Let photographs lead: the product, the people, the rooms, the work; two or more a screen on a product page.
- Use real icons for the tools a studio uses; one still diagram at most; flat grounds and one brand band.
- No shader effect, print, grain, gradient, scene or loop (dealt moments only); WebGL only for a product render the brief asks for.
- Show a physical product with no photographs in stand-in photographs of the same kind of thing (listed for the client); a render only when the brief asks for 3D; never a drawing, mood stock or a set of props.

## 16. Every product page
- Show the product big where it stands whole (most of its frame, or on the ground at anchor scale), never mid-size in a grey rounded panel on a grey ground.
- Use a different picture each section; never one view twice.
- Picture every headline promise (a family bike shows the child bench).
- Use dealt compositions, no structure twice, one contrasting ground.
- Make the colour swatch change the picture; show every colour once.
- State no fact twice.
- Hero product at 80% of the content width target; under 60% FAILs, 60-80% WARNs (at 1000px+).
- Deal only the product, photo and film heroes on a product page (split, word, statement, triptych cannot show the product at 80% width).

## 17. Product: plan
- Order: nav, hero, the range/line-up within the first three sections, two or three feature sections (one benefit each, own composition), specs, proof (review or press line), [visit map for a showroom], [FAQ ≤5], closing footer with newsletter.
- Two or three photographs a screen; product whole in three sections max; use, parts and people in the rest; a grid of 4 to 8 cut-outs on one backdrop allowed.
- Prices are "from" prices on cards or a table; never a plan table or monthly switch; only given prices ("Price on request" or none otherwise).
- Big: in the hero and at least one more section the product's long side spans 80 to 100% of its frame's width (or runs off an edge) or stands on the section ground at anchor scale (8+ of 12 columns at 1440; full column at 390). Never mid-size in a grey rounded panel on a grey ground (in testing: 5.5, creativity 4.5, "a safe grey template").
- Every headline promise shown in a picture ("takes four crates" shows four crates readably); else add the picture or cut the promise.
- One contrasting-ground section (dark band or brand band) holding the strongest view; the rest one flat ground; frames take the page radius; never panel in panel.
- Colour swatches swap the product picture; every colour offered shown at least once (one colour per section); an offered-never-shown colour is a fault.
- Buttons step on hover and press on click; a linked feature card lifts 2px and its picture zooms 1.03.
- No photographs: licensed stand-ins of the same kind of thing whole or in use (never a part for the whole), no readable maker's name or logo, no face passed as a customer, one light and grade; the full product page, hero first, order card last. Never a split hero holding only an order form or an effect; the order card is its own last section.
- A render only when 3D is asked for: one crafted studio render of this product, each section a different view, stills by default, props only where a headline needs them; copy never calls it a render.
- Allowed: nav cards/split/mega; footer columns/dark; close photo/type/word; rhythm dark band/brand band; buttons arrow/solid/block/pill.
- Never: a photograph of something else; app screens it doesn't have; logo rows; tabs; anything apologising for what's missing.
- Effect only for a technical product.

## 18. Service: plan (clinics, firms, agencies, studios, trades)
- Order: nav, hero, services list (one line and "from" price each; peek list when each has its own photo), work (grid of 3 to 6 project photos or photo pair), steps, people row, proof (a given quote), [pricing two or ruled price rows], [FAQ], booking form with address, closing footer.
- Pictures: the work, the team at work, the rooms; one or two a screen; real icons for tools a studio really uses.
- Allowed: nav mega/split/centre; footer visit/dark/columns; close type/photo; rhythm surface pairs/dark band/space; buttons solid/tonal/block/arrow.
- Never: product UI the firm doesn't run; stock handshakes; logos of invented clients; tabs.

## 19. Tech page plan
- Let the client's own subject lead at true size.
- Software: show its own UI as live HTML showing what it works on (a code-review tool: a red and green diff with its Accept action) in one app-frame across the full content width, never a generic dashboard or only fragments on panels.
- App-frame: a list pane beside the open item; stacks at tablet width; shows the open item alone on a phone.
- Cards: fragments on lit panels, pulsing diagrams, real icons.
- Hardware: its photographs, else stand-in photographs of its kind (render only on a 3D ask); never a split hero of only an order form or a drawn SVG.
- Game: its name in the h1, a launch line, its world as full-bleed key art (else its name set large over stand-in photographs of its setting); an effect never in its place. A game never deals the statement or word hero.
- One effect by deal (a shader ground in the hero or the one visual frame, a WebGL part, an object or one big scene) and one or two moments in their own sections.
- No card moves with the scroll.

## 20. Software: plan (incl. AI, developer tools, fintech)
- Order: nav, hero, [logo row docked in the hero], full app window as section 2 or 3, two or three feature sections in different layouts (2x2, bento, split, tabs tour, chapter, steps), [integrations as a fan-in or hub diagram card; big grid only for 9+ tools], [quote with stat or customer stories; with neither, pricing or FAQ is the calm section], [pricing three, two or comparison table], FAQ, closing footer.
- Pictures: client screens as live UI, else fragments showing the product's own subject; diagrams for connections; real icons for tools it works with.
- Allowed: nav mega/cards/centre; footer dark/statement/columns; close type/word; rhythm dark band/surface pairs/space; buttons solid/pill/tonal/arrow. Tabs only here, click only.
- Never: stock people at screens; an object render in place of the product; a product shown only as small fragments centred on coloured panels.

## 21. Gaming: plan
- Order: nav, hero (the game, named), [trailer frame], the world (one or two full-bleed sections), what you do (screenshot strip as 3 to 5 open cards, one verb each: sail, salvage, rebuild, each with its capture), [a game system as a diagram card: matchmaking, saves, stores], platforms and editions (real store/platform marks, "from" prices), [press lines or quote], [FAQ], closing footer with the main action (Add to Steam wishlist, Pre-order).
- Hero names the game: h1 = name and genre ("Northline, a co-op survival game"), ≤40 characters on the product stage, ≤32 on the photo hero; or the client's wordmark over an h1 naming the genre. Lead carries launch date or status ("Out 12 March on Steam", "Early access now", "Coming to PC"); never an invented date.
- Key art in the hero and world sections, full bleed, one grade.
- No art files: hero type-led over a photograph of the game's setting (3 to 5 frames of one light and grade, nothing readable, no faces); name set large in a box or straight on a dark empty part; world section takes the widest frame full bleed in a media or dark band with the h2 above; one shader effect only in a section of its own, never on photos.
- Platforms: real Steam, PlayStation, Epic marks; Xbox and Nintendo named in type, never a drawn mark.
- Allowed: nav mega/centre/cards; footer dark/statement; close word/type; rhythm dark band/media band/space; buttons solid/pill/block.
- Never: a hero that doesn't name the game; abstract effect, pattern or statement hero for key art; UI fragments, dashboards, SaaS widgets; a toy object, drawn vector or empty panel for the world; stock players at screens.
- In testing, a game page not naming the game with an abstract effect lost 3.5 to 5.5 against one with launch date, world scene, feature cards and platform icons.

# Part 3 — Anti-slop bans

## 22. Visual bans: page furniture and chrome
- No popups, newsletter modals, chat bubbles, help pills, back-to-top squares, badges, award strips or asks in a modal.
- No entry gate, loader/preloader, custom cursor or wheel capture.
- No progress, drag or meter bars; no scoring or progress bars with filled tracks as comparison visuals.
- No modal confirmation on forms.
- No accordion FAQs: answers open in full.
- No version labels in the hero ("V0.6", "INVITE-ONLY PREVIEW", "BETA") unless the brief is a product launch.
- No version footers ("v1.4.2", "Build 0048") on marketing pages.
- No decoration text strips at the hero bottom ("BRAND. MOTION. SPATIAL.").
- No locale, city, time or weather strips ("Lisbon, working with founders").
- No scroll cues ("Scroll", "↓ scroll", "Scroll to explore").
- Zero decorative status dots by default.
- No section-numbering eyebrows ("00 / INDEX", "001 · Capabilities", "06 · how it works"); no 01/02/03 numbering on content that has no order.
- No floating top-right sub-text in section headings.
- No div-based fake product UI (invented task lists, dashboards, terminals built from styled divs); a UI fragment is the client's real UI rebuilt at true size with the client's own content.
- No hand-rolled SVG icons; no drawn look-alike of a real logo.
- No outlined boxes; no resting shadows.
- No tilt, no carousels, no timed tabs.

## 23. Visual bans: page-level anti-patterns
- One object in more than three sections; one view twice; a promise not shown; a colour offered and never shown; a fact repeated.
- Product shown mid-size in a grey rounded panel on a grey ground.
- Software shown only as small fragments centred on coloured panels.
- Invented proof, quotes, customers, figures or dates; logo walls; big stat rows; check-icon lists.
- The main action worded differently in different places, or extra filled buttons elsewhere.
- Words, scrims or gradients on photographs; rounded/filtered place photographs.
- Empty, grey or "coming soon" asset frames; any apology or "example" note.
- Carousels, marquees, swipe rows, scroll-triggered card motion, timed tabs.
- Stock people at screens, stock handshakes, mood stock.
- Links to pages that don't exist; a bare "#".
- Tabs on product, service or place; plan tables for non-subscriptions.

## 24. Visual bans: cards
- A big fragment dead centre with even ground all round; a dialog alone on a ground.
- Three levels of boxes; a pattern behind a window or list.
- A fade over the point; a 1 to 23px sliver at any edge.
- Dark ground behind dark UI on a dark page.
- Accent on every chip, date and keyword; brand colours mixed with ink marks; glossy 3D blobs.
- A loop over 5s without pause; a spinner, caret or pulse running in a still picture.
- A card or panel moving with scroll or lighting up on scroll into view.
- One rendering context per panel, or a still ground left running.
- Any "sample", "example" or "to follow" note, an apologising caption, or a placeholder (bracketed names, fake street, lorem ipsum).

## 25. Visual bans: effects
- An effect, print, grain, gradient or WebGL on a non-tech page; an effect where a photograph or the product belongs.
- A print, dither, grade or filter over any photograph.
- A live effect or moving canvas inside a card; a card animating on scroll.
- Effects in fixed layers, behind body copy, or as a page-long canvas.
- Two pointer effects; two lit borders; two filled headlines; a glow spilling onto text or round a button; glass/frosted looks; blend modes on text.
- Patterns or prints behind UI windows; focal grounds behind big windows or text; a noise/fog ground holding content; a contour or dot pattern pretending to be a map.
- Effects in type that read badly: fluted glass, caustics, halftone or engraving in letters; effects in digits on white; silk/glass/metal sheen in pills or bars; moving traces or halftone in charts; grid pulse in charts.
- Landscapes painted in the accent hue only; warm accent muddied into dark grounds; complementary accent mixed into a colour page; orb grounds in feature cards; small dialogs centred on empty grounds.
- Violet or lavender anywhere; fixed hues not from the palette.
- Copying another site's code, assets or signature device — take only the generic idea, built with the client's content.

## 26. Visual bans: objects and scenes
- A render by default for a product without photographs (photographs first); an object of another kind; random 3D props; a split hero with only an order form; a drawn SVG or loose primitives standing in for the product.
- Objects animated by scroll outside their scene; objects over moving grounds; UI fragments over objects; objects centred dead with even ground; more than two objects in view or more than one turning per group.
- The same product view twice on a page; the product whole in more than three sections; renders in grey panels.
- A big scene on a non-tech page or without the brief's real assets; a scene as hero when it rests in two screens; moments in or beside the scene section; a scene beside another effect.
- Gauges, counters or readouts under a scene object; scrims or gradients behind scene text; chips or labels flying with the scroll; SVG clips repainted per frame.
- Using the smooth "studio" look of the dither object next to real product shots (reads as toys).

## 27. Visual bans: UI mocks
- Fragments centred with even ground around them; floating whole sheets; content cut through its point (the button that gets clicked, the newest notification, the reviewed line).
- Invented words, numbers, clients or apps; figures the brief doesn't give; grey-box or look-alike app logos; wordmarks too small to read.
- A progress bar as its own card or a page loader; a calendar with Apply/Clear buttons; a changing label showing two words at once; empty windows between loop cycles.
- Fragments on patterned grounds; two loops on one screen below the hero.

## 28. Visual bans: what never appears on a place page
- No effect, WebGL, canvas, CSS gradient, grain, glass, print, scene, loop, count, UI fragment or diagram; at most one dealt scroll moment (two on a long page) in its own section.
- No feature or plan cards, tabs, accordions, switches, logo rows, timelines, fact strips (address or hours as labels), calendar card, map of an ungiven street.
- No rating, review, figure or quote not in the brief.
- No words on a photograph; no rounded or filtered photos; no see-through or blurred nav.
- No outline, pale, blurred or rotated display type; no two-tone headline, filled-plus-outline button pair, dotted timeline rail, carousel.
- No dark section except the one brand band.
- Interface: one ground, one ink, hairlines, one button style; photos, type and flat colour carry the page.

## 29. Layout bans
- No swipe rows, sideways scrollers or cut carousels; nothing scrolls sideways at any width.
- No near-empty screens; no covered or cut text; no sliced heading and no ellipsis.
- No lopsided sections or empty middles; no text against the screen edge.
- No mirrored or alternating splits.
- No block bleeding out to one viewport edge only.
- No `border-top` + `border-bottom` on every row of long lists; a long list (more than 5 items) deserves a different component than a divided list.
- No strip sections: a short quote, logo row, stat row or FAQ merges into the section above.
- No bento with empty middle or trailing cells: N items = exactly N cells.

## 30. Type bans
- Never Inter, Roboto, Open Sans, Lato, Montserrat, Poppins, Space Grotesk, Plus Jakarta Sans or the system look.
- No tracked capitals or small caps; no all-caps labels.
- No marker highlights or coloured bars behind words (alternative: a loud single-field palette may spend one highlighter swipe behind one word).
- No monospace outside code (alternative: tech, software and gaming pages carry a mono face for UI fragments).
- Headlines no more than two lines (alternative: the hero h1 at most three lines at every width).
- No text on an SVG curve.
- No emoji as bullets.

## 31. Colour bans: palette
- No violet or lavender in the page's own design (accent, ground, gradient, effect colour, tint); real third-party logos keep theirs.
- A token with OKLCH hue between about 270 and 330 degrees turns to 255 (blue) or 345 (rose), whichever is nearer; a violet deal is dealt again (enforced at chroma > 0.05, hue 275-330).
- No cream-and-terracotta palettes (alternative: the palette library allows a flour-white and terracotta palette for bakeries and cafes, with terracotta only on the main button and the brand band).
- No gradients (alternative: on tech pages a code-drawn gradient light is allowed as a ground; non-tech pages stay flat).
- One accent across the whole page, never two.

## 32. Colour bans: grounds and backgrounds
- Gradients, grain, texture, glass, halos or patterns on non-tech pages; pure-white panels on cream pages; charcoal or violet "dark" grounds.
- More than one dark body section, or a dark section right under the hero; dark heroes/pages on non-tech kinds.
- Rules or borders between sections; bands inside sections; inset coloured boxes as grounds; ground changes on wrappers.
- Two-stop linear gradients as decoration; visible gradient rings; animated grain; grain over UI, text or photographs; more than one texture per page; more than two dealt grounds; two loud grounds side by side; grounds that change a section's height.
- A ruled grid over tables, pricing or lists; arcs outside the close.

## 33. Motion bans
- A card, row or tile that reveals, staggers, slides or fades in on scroll; parallax on text or photos; scroll scrubs outside the dealt moment/scene section; scroll-snap, scroll-tinted grounds, progress lines, scroll-spy markers, count-on-view.
- Scroll-jacking or smooth-scroll libraries; any animation library on non-tech pages.
- A section heading that rises on every section; a second hero entrance; an entrance longer than about 1.1s; an entrance that hides text already readable; loaders, gates, intros.
- A card that tilts, flips, scales, follows the pointer or glows at the cursor; a magnetic button; a replaced cursor.
- Carousels, auto-advancing sliders, timed tabs, rotating notices, logo marquees.
- Random blinking: twinkling dots, glitter, flicker, hue cycling, scrambled text — every change must show a state, a step or real data.
- A loop that plays once (outside a card story replay); a card loop cycle over 4s; two loops in one panel; two self-moving things in one 900px window.
- A hover slower than its token; an overshooting/bouncing ease; a delay before a button reacts; an animated focus ring; a second underline/indicator style; animated width, height, margin, padding or max-height; accordions.
- Typing dots, lone pulsing dots, block cursors after headlines outside a looping visual.
- No slider or crossfade between screens or products in the hero; no entrance that hides words.
- Identical fade-ups on every block are banned.
- No tilt: a tilted hovered card FAILs.

## 34. Imagery bans: captions (enforced)
- No figcaption in a figure holding a visual; no element with a caption/figcaption/img-cap/photo-cap/legend class under a visual.
- Banned caption phrases near a visual (FAIL): "made in code", "made with code", "placeholder", "illustration", "rendering", "render of", "pictured", "photo of", "picture of", "image of", "view of", "shown above/here/below", "fig. N", "figure N", "caption", "(sample)", "(example)", a line starting "sample"/"example".
- FAIL a line saying where a picture comes from: "not ours", "a similar bar", "stock photo", "for illustration"; or explaining it: "this photo shows", "photographs follow".
- WARN a muted line of 2 rows or less and 15px or less within 32px under a visual of 120x80px+, or a small line over its lower half; WARN a licence credit under a picture.
- Applies to any visual 120x80px or larger; a caption line counts within 32px of its bottom, overlapping 40% of the narrower width.

## 35. Imagery bans: photographs
- Captions, labels, "sample" notes or credits under/on pictures; a credit wall of per-photo links.
- Text on place photographs; scrims, gradients, fades or blur to make text legible on photos.
- Stock as the hero, a room, a shopfront, a product or a person; more than one in three pictures from stock; mood stock; trade clichés; faces as staff/customers; other businesses' signs and rooms; other regions' landscapes.
- The same frame twice (crops and mirrors included); three near-identical frames; mixed grades and lighting; HDR beside snapshots.
- Photographs that start invisible, are revealed on scroll, or develop under a mask (outside the dealt develop moment); empty or half-loaded frames.
- A row picture blown up as a hero; upscaled phone crops.
- Drop shadows on cut-outs; borders, shadows or overlays on place photographs.
- No stock photograph passed off as the client's product, people or place; never show a stand-in with another maker's name or logo.
- No product page that never shows the product.
- No halftone, dither or engraving canvas over a photograph on product, place or service pages (FAIL).
- No decorative photo-credit captions ("Field study no. 12 · Ines Caetano").
- No pills or labels overlaid on images.

## 36. Imagery bans: the photography never-list
- Another business's identifiable room, counter, sign, cup, bag or product as the client's (a whole meeting room, lounge or breakfast room counts); a machine with its maker's name; a named bar's whole room.
- A face as staff, guest or customer (use hands, backs, faces out of frame). Another place's coast, street or landmark as the client's; a lone house on a hotel page.
- Trade clichés: latte art from above, beans filling the frame, the croissant-and-cappuccino still life, a made bed, flour thrown on black, a whole figure.
- Mood stock (curtain, plant shadows, sky, grass, forest, fog, aurora, waterfall), an animal or vehicle, a recognisable viewpoint, AI images, composites, Street View, a sight far from the place; a gradient, grain, pattern or shader standing in for a photo.
- The same stock frames repeated across builds; a soft frame (e.g. a rusty chain) only when no sharper one exists, never as lead.

## 37. Copy bans: slop words
- One is a FAIL: delve(s), tapestry, testament to, realm, embark, beacon, multifaceted, paradigm, myriad, plethora, meticulous(ly), intricate, interplay, garner, boasts (for "has"), elevate(s/d/ing), unlock(s), unleash(es), empower(s/ing), harness, supercharge(d), turbocharge, seamless(ly), effortless(ly), cutting-edge, revolutionary, revolutionize/revolutionise, transformative, holistic, next-level, world-class, best-in-class, game-changer/game changer/game-changing, state-of-the-art, bespoke, synergy, leverage, reimagine(d/ing), next-generation, next-gen, powerful, robust, nestled, unparalleled, unrivaled/unrivalled.
- Literal trade uses pass: harness (a climbing harness), unlock a door/bike/locker, elevated train/terrace/view, seamless knit/socks/pipes, bespoke tailoring/joinery/kitchens, leverage up to 1:30, tapestry weaving/workshop, intricate lace/carvings/dovetails, powerful + a figure with unit (2,000 W motor), robust steel/oak/frame; realm and embark on gaming pages; beacon on gaming, tech and software pages.
- The client's own name stays (Elevate Pilates).
- Each word stands in for a fact; replace it with that fact: "seamless" with the setup steps, "robust" with the failure case, "powerful" with the figure; otherwise the step count, the material, the place.

## 38. Copy bans: stock phrases
- One is a FAIL: "in today's fast-paced/digital/modern/ever-changing/busy", "unlock the power/potential", "harness the power", "the future of X is here/now", "say goodbye to", "whether you're a", "look no further", "join thousands/millions/hundreds of", "trusted by teams/businesses/companies/brands/people worldwide/everywhere/around the world", "imagine a world", "ready to transform/take your/elevate/level up", "ever-evolving", "one-stop shop", "take it/your X/things to the next level", "it's/this is/we're not just a/an/another", "not only ... but also", "here's the thing", "let that sink in", "let's dive in", "it's important/worth to note/noting", "in/with just a few clicks", "we've got you covered", "the possibilities are endless", "at your fingertips", "X made simple/easy".

## 39. Copy bans: residue and placeholders
- One is a FAIL: lorem ipsum; [company/brand/business/product name]; "Certainly!"; "I hope this helps"; "as an AI"; "[insert"; "[NEED"; {{template tokens}}; "Great question!"; markdown bold (**x**) or ## headings leaked into a rendered page.
- The strongest single tell: a conversation or template pasted into the page.
- No bracketed placeholder or "(sample)" tag in visible text; no "to be added", TODO, "your name here" or template sample text; no "Beispielstraße"; no printed .example or example.com address; no phone of zeros, one repeated digit, 555-01xx or 1234567.
- No "sample", "(sample)", "examples" or "illustrative" tag, note or asterisk footnote; a given target value is worded inside the sentence ("target 2 days").
- No note saying names and figures are examples; never more than two lines tagging figures as samples.
- No link to # and no empty href: write the real words or leave the element out.
- "Coming soon" only for what is actually stated as coming.

## 40. Copy bans: devices with budgets
- Over budget = WARN; a device at twice its budget plus one or more is a tic: FAIL.
- Two-fragment headings "X. Y." (up to 14 words; "Twelve rooms. Three ways to stay."): budget 1. Fix: a name with a claim under it, a verb and its thing, or a plain sentence.
- Number-pair headings "Four X, one Y" ("Four projects, four very different problems."): budget 1 (alternative: 0 to 1, as the most repeated model habit). Fix: say what the section holds.
- Contrast frames (", not Y", isn't, not just, rather than, instead of, without the, not by), all forms counted together: budget 2; an FAQ buyer question is not the device. A suppressed "not X but Y" returns as "rather than", "instead of", "without the". Fix: state the positive fact alone.
- Negation runs "No X, no Y" ("No forms, no back-and-forth."): budget 1; keep only if each item is a refusal a buyer can check.
- Virtue words about the business: honest(ly), calm(ly), quiet(ly), actually, genuine(ly), truly, simply, thoughtful(ly), carefully, intentional(ly), steady, dependable: budget 2 (alternative: 0 about ourselves, with literal uses such as a quiet room, calm water, genuine parts, a motor that runs quietly allowed up to 2). A page never calls itself honest; fix with an admission or a fact.
- Dry closing line on a paragraph ("They hold spoons now."): budget 2, never in a row; the same joke on unrelated sites is the tell. Fix: end on information; humour moves to microcopy.
- Pun on the name or its metaphor: 1, never the h1; never run the name's metaphor into the ground (a brand called Kiln that "fires" every section).
- -ing riders (", ensuring/enabling/allowing/empowering/helping/letting/giving/making it/creating/delivering/fostering"; ", ensuring a smooth start"): budget 1, WARN only.
- "Since [year]": once, where it matters, and real.
- Response-time promises ("within 24 hours", "Within two working days" everywhere): one, only if the brief gives it, in the same words wherever it repeats.
- Puffery (serves as, stands as, pivotal, crucial, plays a key/vital role, in the heart of, where X meets Y, as seen in, the world of): budget 0, WARN; write "is" or "has".
- Staged reveals and process talk ("The result?", "Why does this matter?", "One thing changed: X", "this section", "This section shows", "below we", "Below, you'll find", "here are N reasons", "we've added"): budget 0; the page never talks about itself or how it was built.
- Em dashes in body: budget 2 (WARN above); use a comma, colon, parentheses or a full stop (alternative: zero em dashes anywhere, in headlines, eyebrows, pills, body, quotes, attribution, captions, buttons and alt text; use a hyphen or restructure).
- Exclamation marks: none.
- Footer sign-off line: 0.
- Proof figures ("3x faster", "10,000+ teams", "98% satisfied", round, neat, unsourced): only when the brief gives them, with unit, in a sentence; never rounded or invented.
- Stat strips (a run of 3+ short number lines with no sentence; a row of 3 or 4 figures each over a one-word label under the hero or story): only figures the brief gives, never invented KPIs; each number goes in the sentence it proves; a menu's prices, a timetable or a single-unit column is not a strip.
- Step numbers (01, 02): only steps that happen in order (booking steps); none on order-free features; WARN at 6+.
- Eyebrow/kicker labels: one or two a page (WARN at 5+); a heading that names the thing needs none.
- Quoted testimonials: only quotes the brief gives, word for word, with name and role or town; none is fine.
- Lists of three: only when there are three things; never in consecutive sentences.

## 41. Copy bans: punctuation and shapes
- Em dashes everywhere; exclamation marks in body copy; emoji as bullets; an arrow after every link regardless of link.

## 42. Copy bans: dead metaphors
- landscape, ecosystem, journey (unless travel), "in the X space", hub, "the world of", "where X meets Y", "in the heart of". Name the street or the thing.

## 43. Copy bans: second-generation tells that look like good copy
- The house voice (meta tell): warm, wry, modest, literary for every client. Fix: a register chosen per client.
- Invented specifics (ban): "6:12 a.m., from the window of Room 9", "Batch No. 047", "38% fewer re-runs". Fix: real details only, else a plainer line.
- The origin template: "In [year], [two first names] found [an old hardware store] and kept [one original detail]." Fix: the real story; none given, no story section.
- Polished testimonials: always three, each a small story with a number and punchline. Fix: none unless real, word for word.
- Section template: eyebrow, claim heading, short lede, 3 or 4 cards in every section; "Kind words" over quotes; step numbers on parallel features; a small label over each section heading; "Most popular" on the middle plan (alternative: the three-plan pricing pattern keeps one "Most popular" badge on the featured middle plan). Fix: shape from the reader's questions.
- Perfect evenness: every card same length, every paragraph same arc. Fix: spend words where facts are richest; one section may run long, one may be two lines.
- Microcopy left unwritten: hand-tuned hero over stock error and thank-you. Fix: write it in the register.
- The stale year: a copyright line older than this year.

## 44. Copy bans: default-cast names
- Person names come only from the brief; never the default cast: Priya (Raman, Shah, Nair), Okafor (Daniel, Amara), Raman, Natarajan, Sarah J., Elara, Aisha, Lena M., Marcus, Dana, Tomas, Nora, Mara (and Theo), Isla, Maya, Ines, Jess.
- Never the fictional company names Fieldnote, Kestrel, Halcyon, Brightloop, Acme, Northwind, Lumen, Nimbus, Zenith, Apex, Vertex; as the page's own brand Fieldnote, Kestrel, Halcyon, Lumen and Nimbus FAIL.
- A mock's names fit its town and generation; a coined brand is none of these, and is coined only after searching it.

## 45. Copy bans: button labels
- Never: learn more, read more, view more, show more, discover, discover more, explore, explore more, more, mehr erfahren, weitere infos, click here, find out more, see more, begin, an example, details, more info, go.

## 46. Copy bans: footer copy
- Hold facts only: the brand, the current year, Privacy, Terms, the credits line.
- No sign-off lines ("Made/designed/built/crafted/roasted/baked... in/by/with", "Every ... .", "Since ... .").
- Keep the copyright year current.

## 47. Copy bans: sentence rhythm
- Let length follow meaning; WARN when sentence-length spread is under 4 words (15+ sentences).
- WARN when over 30% of sentences are 4 words or fewer.

## 48. Copy bans: general
- Metaphors and "where X meets Y"; slogans, greetings and boasts in the hero; questions as headlines; exclamation marks; all-caps labels; invented capitalised concepts ("the Proof Layer"); unexplained programme names; jokes or slang in labels; mood paragraphs; a literary quote as a full-screen band.
- A sign-off or a pun in the footer; the model's default voice.

## 49. Copy bans: why model copy reads as model copy
- One voice for every client: warm, wry, modest, a little literary, mildly against big companies; a CI tool and a yoga studio sound alike.
- Same devices in every section: a strip of three invented figures, two-fragment headings ("Short menu. Long list of regulars."), "X, not Y", "No X. No Y.", a dry joke closing each paragraph, a footer pun.
- Sincerity said instead of shown (honest, calm, quiet, actually, simply, carefully).
- Detail invented to look specific (batch number, a minute of the morning, an unmeasured percentage, the same names).
- Professional copy differs in five ways: details are true (often inconvenient); each device used once where it lands hardest; each brand has its own voice; it takes risks (names an enemy, admits a limit); pages are uneven, leaving out what has nothing true to say.
- Root cause: missing input; with no facts a model fills a template with plausible inventions.

## 50. Copy bans: severity and cause of tells
- Severity: ban (one is a tell), cap (fine once, a tell when repeated), context (counts only beside other tells). One tell proves little; clusters and repetition are the signal.
- Cause: models pick phrasing that fits the most pages; tuning smooths toward safe, positive, dense prose; the odd true fact is replaced by a claim fitting any business. The specific must come from input, never style rules; every banned habit needs a positive move beside it or the nearest substitute appears.

## 51. Copy bans: over-correction traps
- No em dashes -> breeds comma splices, full stops only -> counter: colons, brackets, semicolons where natural.
- No "not X but Y" -> "rather than", "instead of", "without the" -> count them together; state the positive.
- No hype words -> calm vocabulary (quietly, steady, honest, practical) -> a fact in place of any adjective.
- Avoid threes -> everything in pairs -> list as many items as there are.
- Be specific -> invented numbers and anecdotes -> the fact sheet, or a plainer line.
- Short punchy sentences -> a drumbeat of fragments -> one sentence per section may run long.
- End strong -> a moral or quip on every paragraph -> end on information.
- Add personality -> a joke in every section -> a humour budget spent in microcopy.
- Vary section length -> one huge and one tiny section on every page -> length follows the material.
- One rule pack on every page -> a new uniform house style -> sameness check across pages.

## 52. Copy bans: not tells (leave alone)
- Perfect grammar. Plain "is" and "has". "In order to". A transition word on its own. Title case when it is the client's house style. One "no card needed" when true. A provable narrow superlative. A refrain repeated on purpose. A list of three when there are three things. Copy the client wrote themselves. Selling on a sales page: persuasion is the genre; the test is whether it stands on facts.

# Part 4 — Design-system foundations

## 53. One system
- Never add a second grid, spacing scale, type scale, radius, button, card, hairline, fade or link style.
- One button shape, one radius family, one card recipe, one hairline, one corner-control size, one link look, one block template repeated.
- One button pair, one card style, one radius scale, one link look; text links in 3+ looks WARN.
- Two boxes deep at most; never text in a box in a box.
- One height per card row and per tile kind, page-wide.

## 54. Base
- Use `*{box-sizing:border-box}`, `html,body{margin:0}` and viewport meta `width=device-width, initial-scale=1, viewport-fit=cover`.
- Set `<html lang>` to the page language; hyphenate headings (`hyphens: auto`) for words of 10 letters or more.
- Put the skip link first in the header's wrap ("Skip to content" in the page language), hidden until the first Tab, then shown over the logo.

## 55. Spacing
- Use only 4, 8, 12, 16, 24, 32, 48, 64, 96, 128 (`--s-1` to `--s-10`) for every margin, gap and padding.
- Heading to content 48px (32 on a phone).
- Cards 24px apart (12 on a phone).

## 56. Rhythm tokens (desktop / under 640px)
- `--nav` 72 / 56 (the fixed header).
- `--padt` 120 / 96 (section top padding; the h2 sits here).
- `--padb` 72 / 48 (section bottom padding, plus `--bar`).
- `--gut` 80 / 24 (place 120 from 1024): wrap side margin; wrap 1280 wide, 1200 on a place.
- `--hgap` 48 / 40 (place 40 / 24): header to hero words.
- `--hpadb` 64 / 24: hero bottom padding (plus `--bar`).
- `--bar` 0, or `calc(64px + env(safe-area-inset-bottom))` with the phone action bar under 640.
- Tablet gutter 48px; never widen it.

## 57. Type faces
- Use one family, or a display face plus a text face with fixed jobs; never three.
- At most four font files; load from Google Fonts with `display=swap`; a fallback face never shows.
- Word and editorial heroes need a face with a weight or width axis.
- Tech, software and gaming carry a mono face for UI fragments; a product page only when an app or code is shown; service and place never.
- A place is dealt one serif, one plain sans and one soft sans to choose among.
- Italic only for quotes, attributions and contact lines; load real italic weights, never faked.

## 58. Type weights
- Headlines at display weight: 400 on product, service and place; 500 on tech.
- Carry headlines by size and tight tracking (-0.5% to -4.5% at 40px and up), never bold-and-big.
- Text 400 and 500 only (500 for labels, buttons, card titles, today's row, strong).
- 600 loaded only for the nav mark's initial tile.
- Never 700 or 800 (the letters moment aside).
- No light weight under 20px.

## 59. Type sizes (1440 / 390)
- h1 72/38 (each hero has its own token), h2 48/30, h3 and quotes 28/24, lead and card titles 20/18, body 16 with line height 26, small 14, labels 13 at 500 in sentence case, stat 38/28 (under the h2).
- Place: h1 48/53 desktop and 32/37 phone; h2 32/40 and 24/30 (token `clamp(24px, .762vw + 21px, 32px)`); names 20/28 and 18/26; sub-line 20/30 and 18/28; body 16/26; small 14/20; labels 13/16.
- Each level at least 1.3x the next from 1024 (1.2x below); WARN h3s within 1.3x of h2s.
- Nothing under 13px (notes, legal line, dropdown heads, image text).
- Lines at most 62 characters (`.measure`).
- One size per kind of element across the page (every card title, address, figure).
- A figure never outgrows the h2 or h1, at 390 too (a figure 1.08x the h2 or more FAILs).
- Display text 40px+ outside a grid item counts as a heading; a statement set at h2 size is a fault; a footer wordmark may be larger.
- No heading whose letters are smaller than the text under it; h1 > h2 > h3, one size each.
- Headline or section heading of 22+ words or 4+ lines at desktop WARNs.
- Every word is live text, never baked into a picture; text never shrinks to fit.

## 60. Readable text
- Text people read (sub-lines, card lines, list items, answers) 16px or more, line height 1.5 to 1.8, in ink at 7:1 or more.
- Muted (4.5:1+) only for labels, dates, meta and a heading's grey run-on.
- Large text (24px+) in a muted half or inactive row at least 3:1.
- Never 14px paragraphs or 15px grey card text.
- The hero has one quieter level of small text at most (a grey fact line, or a pill above the h1).
- Highlight by contrast, never by colour; colour inside a word once a page at most.
- Sentence case everywhere; labels 13px at 500.
- Curly quotes; never break a number from its unit (never "250 / W").
- A heading's grey half is its own sentence with a stop before it: `<h2>Send invoices in minutes. <span class="muted">Clients pay by card.</span></h2>`.

## 61. Colour
- Keep the interface 90 to 95% neutral; colour comes from photographs, the product, the work and real logos.
- One near-black ink, often warm, never `#000`, for text, hairlines (12 to 15% of it), button borders, interface glyphs and a designed mark.
- Real logos keep their own full colours, never redrawn or tinted; a fictional client's mark is designed, not borrowed.
- One accent at most, from the client (product, shopfront paint, tiles, bag label): the primary button (the only filled accent), focus ring, links, state in visuals, small marks, the one brand band; under 3% of a screen elsewhere.
- Accent label 4.5:1 on the accent; accent 3:1 on the ground.
- Three ground tokens (main, alt, dark), a brand band on product and place; more than three flat grounds across the page WARNs (a lit ground or photograph is no ground).
- Dark pages and dark heroes for tech only; the dark evening grade tech only.
- Choose the grade (light or evening) once on load or by a click, never by scrolling.
- Keep violet third-party logos small (an icon tile, a diagram node), or print them mono, or leave them out.
- Place palettes: light, low saturation grounds.

## 62. Radius
- sharp 4/6/8, soft 8/12/20 (default), round 10/16/24 (sm/md/lg).
- `--r-lg` cards and frames, `--r-md` panels, `--r-sm` controls, `--r-btn` buttons.
- Software windows one radius (12 to 20) with a 1px line.
- Place: `--r-lg: 0; --r-md: 0; --r-sm: 2px; --r-btn: 2px` (square photographs and cards, 2px buttons).

## 63. Buttons
- Two styles only: primary and secondary; 44px high (48 on a place, with the block look and in the phone bar); the nav button the same height, never smaller.
- Label 16px, 24px side padding, at most two in a row, full width on a phone.
- Deal the look once (solid|pill|tonal|arrow|block); markup never changes.
- Exactly one filled button marks the main action in any view; every secondary takes one style; text links use one link style.
- XL button once, in the type close.
- Never a slanted, gradient, ghost or shadowed button, or a third style.
- Drawn arrow as the primary's last child where the look shows one; one arrow style a page, only on actions that need one.
- A filled button with no outline under 1.3:1 against its surrounding ground WARNs.
- At most two hero actions (more FAILs); main action on five buttons or more WARNs.
- One action at most twice a screen (3+ FAILs).
- Every CTA passes WCAG AA contrast.

## 64. Nav
- Fixed, full width, `--nav` tall, opaque ground, a 1px hairline under it from first paint, z-index 10, the same at every scroll depth.
- No blur, transparency, shrink, hide, shadow, colour flip or floating pill; nothing else on the page is sticky.
- Logo on the left line, main button ending on the right line; a gap over 24px or pieces past the edges FAIL.
- Logo: the client's SVG, else the dealt mark plus the name at 20px in the display face; the footer repeats it.
- Four to six plain one-word nouns at 15px/500 that never wrap, each with its own anchor (place: Menu, Rooms, Workshop, Visit, About).
- A second action as a plain word only when the client has one (Sign in, Gift cards); the main action as the one button.
- One word may open a full-width flat panel on hover after 150ms; on other kinds the panel has no shadow, only its ground and a 1px line.
- Current page: `aria-current` on one word at most, a 2px bar under it; a bar with 3+ section links that never marks the current section WARNs.
- 640 to 1023: keep the primary button beside the 44x44 menu button, never only logo and menu (FAIL when 240px+ free); the menu button takes the secondary look.
- Under 640: a full-screen menu sheet with 56px rows, closing on any tap; a place adds the street and the week's hours at its foot.
- Phone action bar (required on a place): fixed at the foot, on the ground with a 1px top hairline, one 342x48 main action or two 165x48 buttons; never covers a label or link; appears only after the hero's main button scrolls off; hides while the same action shows on screen; inert when hidden.
- A dropdown whose 3+ entries share one target WARNs.

## 65. Footer
- The close and the footer are one section (`footer.closing`, one screen; two rows: the dealt close, then the directory and legal row); no separate closing band.
- Types: columns, dark (name large, columns right; a step darker on a dark page), statement (lit ground; tech), visit (address large with the way there and hours beside).
- Legal row: brand, current year, Privacy, Terms (Imprint only with real company details), the one credits line.
- Socials stay empty unless the brief gives accounts.
- Credits: one footer line ("Photographs via Unsplash and Wikimedia Commons") linking a credits page; never one link per photograph; more than 2 photographer/licence links in the footer FAILs; at 1000px+ more than one credit line FAILs (narrower: a second block, over 220 characters or five lines).
- Footer column heads are h3.

## 66. Cards, lists, hours
- Open tiles for rooms, models and people; rows for menus, prices and specs, a 1px rule closing each row inside the content edges.
- FAQs open in full.
- Opening hours as a dl of day/time pairs; mark today's row at weight 500; "Open now, until 16:00" / "Closed, opens Tuesday at 7:30" only from real hours, never from assumed ones.
- Cards of one class in two title faces, or 4+ siblings in two fills, FAIL the card family; 3+ text-only cards WARN.
- Four cards drawn one way FAIL; any one card layout in more than two sections FAILs.
- Plan cards or a ticked price table for something that is no subscription WARN.

## 67. Forms
- One recipe for every form (booking, enquiry, call request, newsletter); a named booking system replaces the form with its link.
- Never `action="#"`, an empty action or a submit a script swallows; without a form service, a mailto on `.example`.
- Fields 48px, labels 14px, input text 16px (phone too), tap targets 44px, six fields at most, one column under 640.
- Every field has a visible label above it naming what goes in ("Arrival", "Guests"); a placeholder is never the label; `aria-label` alone is not one.
- Right field types: email with autocomplete email; tel only when the brief asks to collect a phone; autocomplete name; inputmode numeric for counts; text fields for dates on non-English pages; allow paste; the button stays live.
- Validate on submit, never while typing; each failed field gets `aria-invalid` and a reason under it naming the field and what to type ("Write an email address with an @"); focus the first failed field; the status line says how many.
- One status line under the button: "Sending" after 300ms, then confirmation or failure; a failure keeps everything typed.
- Success only after a real send; a mailto stand-in shows no success line; never a modal.
- The button is the main action word for word ("Request a table"); the sent line uses the button's words ("Your table request is in. We reply within a day."); a line under the form says when the reply comes.

## 68. Head and share
- Title "Name: what it is for whom or where"; a one-sentence meta description, never the same words.
- og:title, og:description, og:type, og:image and twitter:card summary_large_image; the image is a still of the page's own hero.
- Favicon: the client's logo, else the dealt mark (24x24 path in ink; initial on a rounded square).
- theme-color: the page ground.
- Canonical only with the client's real domain.

# Part 5 — Layout system

## 69. Frame and grid baseline
- Desktop reference 1440 wide: content container 1280 wide at x 80 to 1360 (a local place page: 1200 at x 120 to 1320); 12 columns, gutter 24.
- Phone reference 390 wide: container 342 wide at x 24 to 366.
- Place page column spans (1200 column, gap 24): span-2 180, span-3 282, span-4 384, span-5 486, span-6 588.
- Type baseline: h1 72, h2 48 at 1440. Never add a size the type scale lacks; a missing value becomes a named token.
- Every block stands on the container's two lines or runs edge to edge; never bleed out to only one viewport edge.
- Test layouts at 1440, 1280, 1024, 768 (and 820 tablet portrait) and 390.

## 70. Grid
- 12 columns, 24px gap (12 under 640).
- Picture wall: its own grid with a gap of 0 or 2px.

## 71. The judge tile
- The screen at scrollY = k x H (k x 900 at 1440x900, k x 844 at 390x844) shows exactly one section, the hero included.
- `scroll-padding-top: 0; scroll-behavior: auto` so anchor jumps land on a tile.
- Plan the page as a list of screens before building.

## 72. Page shell
- Body renders only the header nav, main, the closing footer and on a phone the action bar; nothing else is fixed.
- Only sections in main; no bands.

## 73. Section box
- Height `calc(var(--h,1) * 100svh)`, `--h` 1 or 2; padded `--padt` above and `--padb + --bar` below.
- Under 640px non-hero sections use `100lvh` and `--hm`; on a phone a section is at least its screens and grows with its content.
- The wrap is a section's only in-flow child; a layer sits beside it.
- Never min-height alone, never dvh, never a third screen, never a height set by script.
- One h2 per section, first content, top-aligned at `--padt` (120, 96 phone), 48 under the header in the tile; never centre content vertically; never a second h2; no h2 in the hero.
- Section height tolerance 2px (3-8px WARN).

## 74. Section height in screens
- Every section is exactly one or two screens tall; plan each section's screen count (1 or 2) from its content height before building.
- One screen under the fixed header = viewport height minus nav (828 at 1440x900; 788 at 390x844).
- Content box of one screen ≈ 708 at 1440x900 (viewport minus 120 top padding minus 72 bottom padding minus any phone bar).
- The heading comes first in every section, top padding under its top; heading block to visual gap 48.
- A visual sized to fit one screen after its heading: height = `clamp(280, screen content box − heading (~160 for a two-line h2 + sub-line) − 48, 720)`; auto height under 1024.
- Never vertically centre a short block in a tall screen (it hides that it is short).
- Tablet (768x1024 and 820): re-plan screens; 832px per screen at 768x1024; each section's stacked content must fit its screens, else two screens or less; the first screen ends on a whole picture or a clear bleed. Note the tablet count when it differs ("2 at 768").
- Phone keeps the desktop's grounds, photographs and order; each photograph comes after its text.

## 75. Content windows at 1440x900 (one screen holds 708px, y 120 to 828)
- Under 360: merge into the section above, or add the picture it lacks.
- 360 to 495: one screen, a warning: give it its picture.
- 495 to 708: one screen.
- 708 to 1,320: no height fits: cut to 708, split into two sections (each 495+ with its own h2), or use two groups.
- 1,320 to 1,608: two screens (1,200 to 1,320 warns).
- Over 1,608: split.
- At 390: one screen holds 464 to 700 minus bar; two hold 1,268 to 1,544 minus bar.
- Split or cut a long feature grid; never shrink it.

## 76. Tablet (640 to 1023; judged at 768x1024 and 820x1180)
- Up to 832px stacked content at 768x1024: one screen.
- 832 to 1,130: cut to one screen (lower picture height, a fill frame, drop the grey line or a fourth card).
- 1,130 to 1,856: two screens there; no card row across the screen line at 1024.
- Splits stack text first; panel cards take the full row; no row half empty.

## 77. Two groups in two screens
- Each row at most 708px; row 1 the h2 and first group (360 to 708), row 2 the rest (420 to 708), no second h2, starting `--padt` under the second screen's top.
- A total of 708 to 780 has no legal height: add or cut up to 72px.
- Phone: four open tiles stack into two screens with 180px panels and 32px between tiles.

## 78. Fill and air
- Fill 0.55 or more (0.40 WARN); the gap to next content then at least 2x padding (192px; 144 + bar on a phone).
- 128-480px between the content of two sections (112-420 on a phone); 64-600 / 56-560 WARN band.
- Empty area over 35% of a section inside its container WARNs, over 50% FAILs.
- Another section may peek 8px at most (24px WARN), never a whole heading; two sections' headings whole on one screen at 3% of scroll positions at most (5% phone).
- A short block is merged or given its picture, never centred alone in an empty screen.
- A price, quote, question or closing section with no picture, icon or mock WARNs; a quote or closing call text-only FAILs; two or more text-only sections FAIL.

## 79. Separation
- Separate sections by a full-width ground change or space only; no rules, shadows or inner hairlines between or inside sections; no inset coloured box standing in for a ground.
- Band padding inside should match space outside its edge.
- No content flush on an edge where the ground changes.

## 80. Scroll exceptions
- The big scene (tech) and a dealt scroll moment (every kind) run inside their own section, which stays exactly 1H or 2H; photo-chapters is (hold + 1) screens live (3H for three chapters, 4H for four or five).
- Pin only with `position: sticky` inside that box; nothing else is sticky.

## 81. Equal edges and columns
- One wrap for header, every section and footer: `width: min(100% - 2 * var(--gut), 1280px)`; lines at x 80 and 1360 at 1440 (place 1200 at x 120 to 1320), x 24 and 366 at 390.
- Equal margins 64-120px desktop, 16-24px phone (enforced).
- Column starts at 1440: 80, 189, 297, 406, 515, 623, 732, 841, 949, 1058, 1167, 1275; spans 3 = 302, 4 = 410, 5 = 519, 6 = 628, 7 = 737.
- Place (1200): starts 120, 222, 324, 426, 528, 630, 732, 834, 936, 1038, 1140, 1242; spans 282, 384, 486, 588, 690.
- Phone: one 342 column or two 165 tiles 12 apart; nothing narrower than 165.
- Every block starts on the left line or a column start; every right-ending block ends on a column end, the last on the right line.
- Anything wider than half the wrap runs the full wrap.
- Card rows (6+6, 4+4+4, 3+3+3+3): first card on the left line, last on the right, all one height, every row full.
- Two text lines only: the left line and the page's split line (right column start k = 5, 6 or 7: x 623, 732 or 841; a place always 6/6 at 732); use one split pair on every split.
- Second column of splits starting at three places or more WARNs; text starting on more than two left lines fails.
- Centred text moves left: h1, section heads, close and pricing heads start on the left line; no centred or right-aligned block wider than half the wrap; one or two centred section headings among left-aligned ones WARN.

## 82. Splits
- Text left, visual right, top-aligned, on every split: never mirrored, never alternating.
- The h2 and its intro sit on the left line above the grid.
- A filled column is a card and may pad its text 48px; text never inset in a bare column.
- Phone: text then visual, both 342; a stacked visual under 24px from the text above WARNs.
- A picture centred on a text column 120px+ taller WARNs.

## 83. Pictures in the layout
- A photograph spans 0 to the viewport as a layer, or starts and ends on column lines (628, 410, 302 wide; place 588, 384, 282).
- No photograph taller than 708px outside the hero.
- Full bleed only for layers covering 90% or more of the section (`aria-hidden`; the hero holds one layer); never out to one side only.
- A cut window is cut by its frame inside the wrap.

## 84. Nothing broken
- Nothing crosses a section edge, is cut off (no sliced heading, no ellipsis), staggered or peeking behind another; no dead space beside a short text.
- Nothing scrolls sideways at any width; nothing past the screen at 320.
- On a phone nothing lies on anything else or under a fixed bar.
- One column at 390, buttons full width, a full-screen menu.
- Phone buttons follow one width rule.

## 85. Margin and frame discipline
- Strong pages hold their margins within a few pixels; off-centre drift from 16px WARNs.
- About one text section in a hundred leaves half the width empty: avoid lopsided sections and empty middles.
- 82% of text sections open with a heading: no untitled sections, no blank gaps, no text against the screen edge, no small titles, one h1.

# Part 6 — Section design principles and page rhythm

## 86. Every section shows the real thing
- Every section carries a picture: a photograph, a portrait, real icons, the client's UI, a diagram card, or (tech only) the effect.
- Picture-less sections allowed only for a price list, an FAQ, a specs table, a booking form, or a statement moment's own section, each once; two picture-less sections are never neighbours (sole exception: the short place page with no photographs).
- A quote needs a face, or it merges into the section above.
- The picture takes a real share: half a tile or more, 50/50 in a split, a whole screen as a layer.
- The close is its own picture: a photograph, the big button, or the name set wide.

## 87. One object never carries the page
- The object shown whole (product photo, game key art, app window) leads the hero and at most two more sections: three "object" sections maximum.
- Every other picture section uses another kind of visual the brief supports; no kind more than twice.
- A new angle, a recolour, a mirror, a smaller file or a crop of the whole counts as the object again.
- A use photograph counts as "use" only when its setting fills half the frame or more and the object is one thing in it.
- Visual kinds per page kind (object whole: hero + 2; others carry the rest):
- Software: object = the app window; others = UI fragments of its subject on cards, diagram card, real tool icons, a type moment, a named quote with face, the effect or scene.
- Gaming: object = key art (none: setting photograph under the game's name); others = the world (in-engine shots, else setting photos), the crew at work (screenshots), the trailer frame, the screenshot strip, a type moment, real platform marks.
- Tech hardware: object = product photo or client CAD render (a render only when 3D is asked for); others = its use at a bench or in place, parts close up, motion video frame, a diagram card held still, a type moment (one figure set large), a context photo of the trade (workshop, lab).
- Product: object = product photo; others = its use (loaded, carried, at home), people with it, close-ups of parts, a still diagram card, a type moment, a context photo of where it lives.
- In testing, one object in six sections capped scores at 4 to 4.5.
- Plan at most three "object" lines in the page plan.
- Carry the rest with another kind of visual: a game's world and crew; hardware in use at the bench, its parts close up, an exploded view; a still diagram card, a type moment, a context photograph.

## 88. Designed slots for the client's own assets
- Trailer, key art, in-engine screenshots, CAD renders, exploded model or motion video each get a slot that reads finished now: the frame at the file's final ratio holding a stand-in photograph (the game's setting, the product's kind in use).
- Never an empty, grey, black or broken frame; never a line saying a file is missing or coming.
- Slot types: trailer/motion video frame, screenshot strip (3 to 5 framed captures), CAD/render frame, exploded frame; key art fills the hero's stage.
- Each named client asset (trailer, key art, screenshots, CAD renders, motion video) reads finished now: a real `<video>` with a stand-in poster, a play control only when there is something to play, three to five stand-in photographs of the world, a CAD frame; never empty.

## 89. One idea per section
- One h2, one idea, at most one action besides the main one (a pair only in the hero, or "compare" beside "buy" on a product).
- A two-screen section holds one list, table or form, or one idea in two groups; never two ideas.

## 90. The main action
- The main action reads word for word the same in the nav, the hero, the close (or booking) and the phone action bar; nowhere else as a filled button.
- A place whose main action is "Get directions" keeps it out of the nav.
- Phrase it as a verb and an object.

## 91. Merge short blocks
- A quote, logo row, stat row or FAQ that alone would be under 495px tall (464 at 390) becomes the last element of the section above, 64 to 96px under its content, with no heading or ground of its own.
- An FAQ that reaches 495px with answers open is its own section.

## 92. Repetition limits
- Any card layout (2x2, bento, three cards, split card, open tiles) at most twice per page.
- Neighbouring sections never share a layout (exception: a chapter series).
- Software, product, service: a calm section (quote, prices, FAQ) after at most two visual ones; the back third of the page calm before the close.
- Repeat the section scaffold (head, padding, ground logic) so it is learned once.

## 93. Proof as small exact objects
- Proof only from the brief: a named quote with a face, a footnoted figure, press lines, a rating line, real customer logos with permission. Without it, leave proof out; never invent.
- Never: a row of big stat numbers, filler stat strips, check-icon lists, a customer-logo wall.

## 94. Depth: two boxes at most
- A card and its picture panel, or a panel and its UI; never three levels.
- A card whose panel holds UI drops its own box (open card: words on the page ground, panel under them with four rounded corners) or runs the panel flush to its sides and bottom.
- An inset panel holds only a picture.

## 95. Links on a one-page site
- Every nav word, button and footer link goes to an anchor on the page; the logo to the top.
- The main action links to where it is done: the booking form, the order section, the visit block for directions, else a mailto.
- Never link to the footer's contact anchor from outside the footer; never generic page paths or a bare "#".
- Privacy, Terms, Imprint go to small pages written for them (Imprint only with real company details), or are left out.

## 96. Motion in sections
- Fragments hold their finished picture; one loop per card group, split or wide frame, with a pause button.
- Nothing moves because the page scrolled.
- Non-tech kinds: no loops.

## 97. Visual type selection
- UI: the client's screens or rewritten fragments showing the product's own subject; none on gaming.
- Diagram cards when the point is how things connect: tech 0 to 2 (with pulses), product and service one held still, place none.
- Real icons for every tool, app or file type the page names, in their own colours; other kinds only tools the client really uses.
- Shader grounds: tech only.

## 98. Place: designed variety without effects
- Never two sections built round one picture: the visit keeps its 6/6 split with one photo; every other photographed section takes a composition; the offer and the place each a different one; neighbours never the same.
- Text beside a single photograph happens once a page besides the visit (story or booking).
- In testing, place pages where every section was text beside one picture scored creativity 2.5 to 4.
- Square corners, one grade, no words on any photograph.

## 99. Page-wide hard rules
- One accent across the whole page; one corner-radius system per page.
- Hero: headline at most 2 lines, subtext at most 20 words and 4 lines, CTAs visible without scroll (alternative: h1 at most three lines; sub-line 15 to 30 words).
- Nav a single line at desktop, at most 80px tall.
- A "Used by / Trusted by" logo row under the hero uses real SVG logos, never plain-text wordmarks (alternative: no logo wall; at most one still docked row of up to six real customer logos given with permission, on software and product pages only).
- Across 8 sections, at least 4 different layout families.
- One theme (light, dark or auto) for the whole page; no mid-page flips.
- Italic display words with descenders (y g j p q) need line height 1.1 minimum plus a bottom padding reserve.
- Reduced motion is mandatory for any non-trivial motion; a page claiming motion must actually animate.
- At least four real pictures on a page (SVG drawings do not count); fewer than two real photographs warns.
- One loud signature move, feedback on every control, a poster on every clip (alternative to an earlier rule of a choreographed entrance per section and one moving picture per screen: only the hero entrance, one or two dealt moments and the hover layer move).
- A focal point on the first screen; the title readable 1.2 s after load.

## 100. Story order
- Tell the page as a story: say what it does, show it, prove it, let people explore.
- Software: hero, full app window by section 2 or 3, two or three feature layouts, integrations, proof, pricing, FAQ, close.
- Product: hero, line-up within the first three sections, features, specs, proof, FAQ, close (order card last).
- Service: hero, services, work, steps, people, proof, pricing, FAQ, booking, close.
- Place: hero, visit (always screen 2), offer, the place, orders/booking, close.
- Gaming: hero naming the game, trailer, world, what you do, system diagram, platforms, proof, FAQ, close.

## 101. Rhythm devices
- Dark band: one inverse-ground section at the page's middle or later, holding the strongest visual.
- Media band: one full-width photograph layer section mid-page (never on a place).
- Surface pairs: one surface-ground band of one or two sections.
- Space: one ground, sections parted by space only.
- Brand band (product): one section in the brand's own colour in the second half.
- Place colour band: the close on the brand colour.
- No hairline rhythm (rules between sections).
- Product: exactly one contrasting ground; the rest one flat ground.
- A dark footer never sits directly under another dark section.

## 102. Calm and visual alternation
- Card layouts at most twice per page; neighbours never share a layout (except a chapter series); splits keep one side (text left) throughout.
- Two picture-less sections never adjacent.
- Bleed never right after the hero; split never right after a bleed; product statement never right after a same-width hero frame; a bento never next to another card grid.
- Two loops never on one screen below the hero; in a chapter series only every other chapter loops.

## 103. Worked sequence: software example
- Hero split (open invoice as a document with a "paid" notification over its edge); full app window (invoice list + client thread); 2x2 features (payments matched, reminder toggles, a lanes diagram, a client question); a one-screen statement section with a word-highlight moment; split text-left (receipts file grid on plain lit ground); tabs tour on the dark band; integrations as a fan-in diagram; pricing three; FAQ; close. No logo row or quote without real customers.

## 104. Worked sequence: product example
- Hero photo (the desk in a real room); product statement (cut-out, three facts: load 120 kg, height 65 to 130 cm, delivery in 3 weeks); line-up (three sizes from €1,290); split (oak grain photo); photo band ("Built to order in Porto"); split again (the handset, a photograph, never UI); specs beside a frame photo; proof merged; FAQ (four); close. Flat grounds, no effect.
- Without photos (desk lamp): hero lamp whole; statement with dial close-up and three facts; split showing the warm pool of light (lamp cut by the frame edge); three steps; specs with component brand icons; live order card (named finish swatches, delivery, price); lamp whole twice only; FAQ; close.

## 105. Worked sequence: gaming example
- Hero film (trailer poster, h1 "Kelpmoor, a co-op sailing game", "For 1 to 4 players. Coming to Steam in spring.", "Add to Steam wishlist"); world as a photo pair of in-engine shots; statement with a letters-assemble moment; what you do (three open cards: sail, salvage, rebuild); world again as media band (key art, h2 on its calm sky); platforms and editions; FAQ; close.

## 106. Worked sequence: place example
- Pottery studio: place hero (workshop in morning light; "Pottery classes in Leipzig-Plagwitz"; "Book a class"); visit (street set large, weekly hours, step-free entrance, 4:3 shopfront); offer on the surface band (classes and prices as two groups beside tall-small: class at the wheel tall, glazed bowl small); the place as a trio (workshop, drying shelf, hand trimming a foot ring); booking (class room photo beside form); visit footer (name capped at 12vw, one credits line). Fourteen photographs, no effect.

## 107. Worked sequence: service example
- Dental clinic: hero split (treatment room, 4:5); services list (six treatments from €95 beside reception photo); steps (book online, check-up, plan: a photo each); people row (four dentists); pricing two (fixed prices); FAQ merged with a patient quote; booking form with address and hours; close.

# Part 7 — Section patterns library

## 108. Navigation bar (shared)
- Fixed, opaque, 72px tall (56 on a phone), 1px hairline, identical at every scroll depth; spans the container width.
- A panel opens after 150ms of hover with a fade and a 6px drop; a click on the word goes to its section (never blocked).
- One phone sheet with Esc support; rows 56px.
- The nav main action is the primary button at the one button height.
- Logo mark beside the name (wordmark, initial, arc, ring, stack, dots; place adds petal, leaf); a client's own logo replaces it; same in nav and footer.
- Tone variant (bar on the inverse ground): tech only.
- Never see-through or blurred (place rule; opaque everywhere by default).

## 109. Nav: mega menu
- Use: software with 6 to 12 feature pages, or a company with several product lines.
- Bar: logo, 4 to 6 one-word links (a chevron only on those that open), then Sign in (plain link, only for apps with accounts) and the primary.
- Menu panel full width under the bar, on the grid: two or three link columns on span-3, then one picture card on span-3 ending at x 1360 (start column 10 with two columns).
- Column: a small label heading over 3 or 4 links, each the feature name (1 to 3 words) with one grey line of at most 30 characters (3 to 7 words).
- Picture card: a 160px panel with one fragment at its corner, 24px in, cut by right and bottom with a fade, showing the newest feature, held still, on the lit ground. No icons in columns.
- Small menus (Resources, Company): same panel, plain columns, no card.
- Phone: sheet rows of 56px; menus expand in place on tap (no height animation); the card becomes a plain row; two buttons full width at the foot.
- Mistakes: bar narrower than container or links wrapping; chevrons on plain links; menu off the grid; a second picture card; grey lines over 30 characters; vague labels ("Solutions", "Platform").

## 110. Nav: picture cards
- Use: two to four distinct products each with a real screen or photo, a studio with three service lines and real work, or a place's offer.
- Menu: three cards on span-4 (410 wide), each a 200px panel with that product's fragment at its corner (fade bottom-right) or its photograph filling the panel; title one line; one grey line of at most 52 characters, inside the card. Resources as plain link columns.
- Place variant: three span-4 cards at 384x288 (4:3), client photo, name at 16/500 and the "from" price; no fragment, ground or shadow.
- Phone: each card a row, title over its line, picture hidden.
- Mistakes: one seed on all three; panels of different heights; text on the panel; titles wrapping; names meaningless alone ("Flow", "Pulse").

## 111. Nav: centred words
- Use: the quietest bar; software and services with four or five plain words.
- Link group centred on the page axis; logo on the left line; main action on the right line; never wrapping at 1024.
- Menus as the mega menu's small menus.
- Phone: logo left, toggle right.
- Mistakes: group so wide it touches logo or button at 1024; a second row.

## 112. Nav: split (name in the middle)
- Use: a place, shop, restaurant or studio people visit.
- Links in the left third (exactly four words), logo (mark and name, 28px display face) on the centre line, actions in the right third; no word wraps at 1024.
- One word (Rooms, Menu, Classes, Shop) opens a panel of three or four photograph cards on span-3 (place: four at 282x212, 4:3) with name and "from" price inside each.
- Actions: the primary plus at most one plain word the client really has (e.g. Gift cards), else none.
- Phone: logo left, toggle right; a place adds street and weekly hours at the sheet's foot.
- Mistakes: unequal thirds pushing the logo off centre; more than four words; UI fragments in the menu; a second link row; a shadow on the open panel.

## 113. Proof: logo row
- Use: software and product only; only real customers whose logos may be shown; docked under the hero's content (at most 96px).
- 14px grey line on the left line, 24px above the row ("Clinics using Ferrow" form: who uses it, plain).
- One row across the container: up to six logos, 28px tall, each in full original colours.
- Still: no marquee, light band, fade or tiles; a logo never moves.
- Phone: hidden unless the hero still ends by viewport − 24 − action bar; then a 3-column grid.
- Mistakes: non-customer or invented wordmarks; marquee; mono or dimmed marks; boasting line; a logo row on a service or place page.

## 114. Proof: quote with stat
- Use: a named customer (from the brief) says what changed, beside one number that backs it.
- Merged into the section above under 495px, else its own section on the surface ground.
- Quote on span-8, stat aside on span-3 starting col 10, both from one top line.
- Blockquote 28px, at most 40 words; 32px below, the person: a 40px photo (or company logo), name over role and company.
- Stat value 38 at 1440 (28 at 390) with a grey line of up to eight words.
- Phone: quote, person, then stat with a 1px hairline 24px above.
- Copy: a before and an after, no praise words ("We used to rebuild the rota every Sunday night. Now it takes twenty minutes on Friday." / "20 min" "to plan a week of shifts").
- Still; on tech the number may be filled with the effect only if that is the page's one effect.
- Mistakes: invented quote; stock or missing portrait; slogan stat; count-up animation.

## 115. Proof: customer stories row
- Use: three named customers, one measured result each (B2B software, studios, products sold to businesses).
- Head row: h2 left, "All customer stories" link right on its bottom line; 48px below, three span-4 cards.
- Card: logo 28px high (or name as card title); 24px; story title (one line, ≤7 words); one line; "Read the story" link; then a flush panel with a stat fragment at the corner (24px in, 40px down), cut by right and bottom with a fade. Service/studio: a photo of each customer's work fills the panel.
- 1024 to 1279: two cards, then the third across. 768 and 390: one column.
- Stat: what was counted (≤28 characters), whole numbers, a change chip, "Before x · After y".
- Tech: first card's stat loops; others still.
- Mistakes: un-named customers; a percentage as the count; a carousel; turning them into quote cards.

## 116. Feature: product statement
- Use: products (never place); never straight after a hero frame of the same width.
- Statement on span-8: h2 48px, at most 4 lines, first sentence in ink, the rest muted in the same paragraph.
- 48px below: a wide frame on span-12 at 2:1 holding the cut-out photo centred, at least 64px from every edge.
- 48px below: three facts on span-4 each: 1px hairline, value at 28px with unit, a grey label.
- Technical product variant: the client's render or object, large and right of centre, facts at lower left inside the frame.
- Phone: h2 at 30px, frame square, facts as a list.
- Example facts: "1,100 lm" Brightness, "2,700 to 6,500 K" Colour, "9 W" Power.
- Motion: cut-out none; technical object a slow turn answering the pointer, with pause button.
- Mistakes: slogan; grey part as a second paragraph; cut-out in a box or touching the edge; wrong-kind object; facts that are claims.

## 117. Feature: 2x2 grid
- Use: four equal-weight features in one screen, each with its own small working visual; if one matters more, use the bento.
- Head with an h2 that runs on in grey (≤12 words including grey part); 48px below, four span-6 cards.
- Two boxes deep: light page = open cards (title and lines on page ground, panel under); dark page = card box with a flush panel.
- Card: title (verb + concrete object), two lines in ink (16 to 20 words), then a 336px panel.
- Fragment placements (vary at least three across the four): a rising chat/search/stat centred, max 400 wide, 56px down, out through the bottom by ≥24px; a short stack (notifications ≤26-character titles, checklist, integrations) low at 100% − 180px with its last row cut; toggles anchored right (32px in, 56px down) cut by the bottom; a compact window at corner 24/28 on a device panel whose bar names the app and status; a diagram card filling the panel.
- Not in this slot: calendar (month must show whole), document or code (wider than the 324 slot at 1024).
- 1024: panels 372 wide, fitted fragments narrow to 324. 768 and 390: one card per row.
- No buttons in the cards.
- Tech: card ground with one seed per panel, no drift; four different fragments/diagrams; real app icons. Product/service: a photo of each feature fills its panel.
- Motion: first card loops; others still and play while the pointer rests; linked cards lift 2px.
- Mistakes: card moving on scroll; panels out of line; a fourth text line; sample text; noun titles ("Peace of mind"); three boxes deep; a widget dead centre; a 1 to 23px ground strip under a fragment.

## 118. Feature: bento
- Use: one main feature large and four small (software with a lead feature, or a product with photos of its main part and four details).
- Row one: span-8 + span-4; row two: three span-4. One panel height for the group (336px).
- Every card: title, two lines in ink, then the panel, two boxes deep.
- Wide card: window at corner (40/48, cut by right and bottom, faded) or a file grid wider than the panel (680 wide).
- Small cards (panel 347 at 1440, fitted slot 256): one fragment cut by the bottom: a narrowing one centred and rising; toggles anchored right; or a wider one (stat, notification, cursor) at true width at corner (24 in, 40 down) cut by right and bottom.
- 1024 to 1279: wide card across the row, four small two by two. 768 and 390: one per row.
- Copy: wide card a verb + object; small cards 2 to 4 words; small-card copy never over two lines.
- Motion: wide card loops; four small still; never two loops in one bento.
- Product: photos in every panel, one look.
- Mistakes: text placed differently across cards; calendar/document/code in a small card; a bento next to another card grid.

## 119. Feature: split, text left
- Use: the workhorse for software, products and studios: one thing it does, a few sentences, three facts, beside a picture showing exactly that.
- Top-aligned grid: text on span-5 (h2; 24; two or three sentences at 20px; 24; up to three short facts as plain lines; 24; one link); frame on span-6 starting col 7 at 5:4 (square on a phone).
- Main piece always cut by the bottom, never floating with ground on four sides: window or screenshot at corner 56/56 cut right and bottom; file grid wide (680); narrower pieces (doc, code, chat, search, checklist) rising, centred, 56px down; short pieces (slider, toggles) 40px down, cut below the second row.
- One small result piece (cursor, notification) only over a window/screenshot at its lower-right edge (24 in, −40), never over the first rows.
- Product/service: frame holds the photo of the part or work the text names (628x471), never UI.
- 1024 to 1279: frame 436 to 564 wide, main piece alone. 768 and 390: text first, frame 48px below, full width.
- Copy: heading = the job and its result; sentences in the order the picture plays.
- Motion (tech): one loop.
- Mistakes: not top-aligned; four-line h2; picture showing something the text doesn't say; a button pair instead of one link; a second split on the other side (splits never mirror).

## 120. Feature: tabs tour
- Use: software only; three to six jobs one at a time in a frame that stays still; click only, never timed.
- Left span-5: head (h2, grey line), then 3 to 6 real tab buttons, each controlling a panel (two sentences and a link) and its screen.
- Right: frame on span-6 starting col 7 with a fade; one slot per tab placed like the split's main piece, cut by the bottom; every panel one fixed height so the frame never resizes.
- Phone: tabs wrap onto rows (never a swipe row); frame 48px under the active panel.
- Labels: verb + object, 2 or 3 words, one grammar ("Book a session", "Move an appointment").
- Motion: indicator slides on click; only the shown screen loops.
- Mistakes: tabs built as plain divs; noun labels; frame changing size; the same fragment on two tabs; tabs on product, service or place.

## 121. Feature: chapter
- Use: one feature area in depth; two to four in a row for a platform (the one place neighbours may share a layout); usually a two-screen section.
- Top-aligned: h2 on span-5; on span-6 start 7 a grey paragraph (~25 words) with a link.
- 64px below: a wide 16:7 frame: the area's main screen rising, 64px down; the one action piece over its right edge.
- 48px below: four span-3 items: a feature name and one grey line.
- Phone: text first; square frame keeps the main screen; four names as a list.
- Motion: one loop per chapter; in a series only every other chapter loops; nothing scroll-revealed or scrubbed.
- Mistakes: half-transparent or tilted fragments; the action covering the main screen's only readable rows; repeats that change the template.

## 122. Feature: full app window (product shown whole)
- Use: every software page has one, in the hero or within the first three sections; never on gaming, product, service or place.
- One real app window across the container: the list pane beside the open item, the app's own chrome.
- Pane pairings: code review = pull-request list + diff with comment and Apply in its top 250px; support/inbox/CRM/agents = conversations + open thread; docs/contracts = documents + page with a marked phrase; CI/deploys = runs + pipeline board or terminal run; booking = bookings + calendar.
- List rows: person, item and detail ("Retry settle jobs · +4 −3"), the product's own status chips, one-word sidebar labels.
- Write 9+ rows and enough open-item lines (24+ for a diff) that both panes run past the frame's bottom, cut under a 64px fade; never an empty strip under the last row.
- One screen: top-aligned h2 on span-5, grey paragraph (~25 words) with one link on span-6 start 7; 48px below, the window fills the rest (~1280x550).
- Columns 5fr list / 7fr open; 1px divider; one border, radius and shadow for the whole window.
- 1024 to 1279: list 4 columns (sidebar hidden), open 8. 768 to 1023: list on top (bar, column heads, four whole rows, 252px), open item under it to the foot. 390: the open item alone, its own header as chrome.
- One box: the window is the frame; no panel, card or ground behind it (on a dark band the dark surface).
- A second piece (cursor, notification) only over the open pane's lower-right, never over the list.
- Copy: h2 names what the window shows; paragraph gives the steps in window order.
- Motion: one loop in the open item; list still; nothing scrolls inside.
- In testing: a product shown only as one small card centred on a coloured panel scored ~3.5 points under a full app window.
- Mistakes: open item alone on a lit panel; list and item as two boxes with ground between; pane ending in empty white; sample rows; a fragment stretched to pane height.

## 123. Feature: steps
- Use: how the product is used, in order, each step's result shown; only with three real steps.
- Head (the heading holds the count: "Set up X in 3 steps"), then three span-4 cards: step number, title (verb + object, one line), one or two lines in ink, then a 336px panel (service: a photo of the step) with one fragment placed as bento small cards.
- Not calendar, file grid, document or cursor in steps.
- No arrows or lines between cards.
- 1024 to 1279: two then one across. 768 and 390: one column.
- Motion: first card loops; never chained or staggered.
- Mistakes: arrows, stair-stepped cards, huge display numerals, panels of different heights.

## 124. Photo band (full-width photograph layer)
- Use: the page's media section (product and service; never place); once per page.
- One screen: the photograph as the full-bleed layer; on its calm, dark side an h2 of at most eight words, one line, an optional link.
- Or light variant with dark words on a pale crop.
- No scrim, gradient or box. A muted film (tech only) with a pause button.
- Phone: a phone crop with a calm area, or the words under it on the ground.
- Mistakes: two bands; words over the subject or a busy area; reusing the hero's photograph.

## 125. Photo pair
- Use: two photographs side by side (inside/out, detail/whole, two cases); a light section between heavier ones.
- h2 and one line above; two photos on span-6, 4:5 or 4:3, one ratio, one light. Nothing under them.
- Phone: one column.
- Mistakes: different light; captions or titles under pictures; three or more (use a row of three).

## 126. Product line-up
- Use: the models or sizes of a product, picture first, each with a "from" price, within the first three sections (8 of 15 good product sites show the range early).
- Head row (h2 "Three sizes", link "Compare sizes"); three span-4 tiles (four span-3 for four).
- Tile: the cut-out on the alternate ground (contained, 32px in) or a photo from one angle, then inside padding: name, "from €1,290", one facts line ("Top 140 x 70 cm · 65 to 130 cm").
- Every model at one scale on one backdrop, or one camera angle. No line-up without a picture of every model.
- Phone: one column, or two-up at 165.
- Mistakes: plan cards with checks and a featured badge; a monthly price; mixed angles and scales.

## 127. Rooms list
- Tiles: a 4:3 photo of the whole room, the name, the facts, the "from" price with its season, "Book this room".
- Mistakes: rooms as plan cards with checks or badges; a calendar standing in for photos; a price without its season; rooms alternating sides.

## 128. Services list
- Use: what a clinic, firm or trade does; a list beside one photo of the work, never a grid of icon cards.
- Top-aligned: h2, one line and a ruled list on span-5 (name, one-line description, "from €95" value right; a link under the list); photo on span-6 start 7 at 4:5 or 4:3.
- At most eight rows (else link elsewhere). Prices shown.
- Phone: text and list first, photo 48px under.
- Example row: "Check-up and clean" / "Every six months, 40 minutes" / "from €95".

## 129. Peek list (row-driven photograph)
- Use: a short list beside one photograph that swaps to the row under pointer, focus or tap; every row needs its own photo (else services list).
- Top-aligned: 3 to 6 focusable rows on span-5 (name, one line in ink, value right); photo frame on span-6 start 7, one photo per row, none lazy.
- Swap instant (200ms fade on tech); mark the row in view.
- 768 and 390: list first, photo 48px under; tap changes it.
- Mistakes: a row without its own photo; same photo twice; caption on the photo; more than six rows; list on the right.

## 130. People row
- Use: the real team a client will meet (service or small maker).
- Head, then four span-3 portrait tiles: portrait 4:5 at top, then inside padding name, role, one line on what they do.
- Phone: two-up at 165.
- Mistakes: stock or invented portraits; mixed light and grounds; more than eight people.

## 131. Integrations
- Use real full-colour icons. When the point is what feeds the product, a fan-in or hub diagram card with real icons on the spokes, inside a feature section.
- Up to eight tools: four span-6 cards, each titled by the tool ("Syncs with Notion and Dropbox"), two lines, a 336px panel with an integrations fragment (fitted, max 380, low at 100% − 180px), a file grid (680 wide), or a hub diagram with the product at centre.
- Big grid only for 9+ tools the brief lists: one span-12 frame (48 padding), eight 72px tiles across (24 column gap, 32 row gap), icon over name label; no "See all integrations" link.
- Phone: cards one column; tiles four across at 64px.
- Never drawn or tinted logos; never tools it doesn't support; never more than five tiles in a card.
- Motion (tech): first card loops or the hub pulses.

## 132. Calendar frame
- Use: tech only, with real dates: the client's real month beside what the dates are for.
- As the split, the frame one height at every width so the month shows whole (min-height 600), calendar alone, fitted (max 440), 48px down. No second piece.
- Correct weekday for the 1st, leading out-of-month days, one marked day, three event rows; "today" only in the current month.
- Phone: text first; frame 600 tall.
- Mistakes: wrong weekday; sample month; calendar scaled or cut through its rows.

## 133. Timeline rail
- Use: four dated moments in order (releases, a history); software and product only, never place.
- Head row with h2 and link; 48px below, four span-3 items: a 200px panel on top, then the rail row (1px line to the next column, an 8px still dot, the newest dot in the accent), date label, title, one sentence ≤10 words.
- Phone: one column, rail vertical.
- Motion: at most one loop in the newest panel (tech); nothing on the rail moves.
- Mistakes: zig-zag points; pulsing dot; panels of different heights.

## 134. Dimension drawing
- Use only beside a product's specs, on a page whose photographs already show the product.
- Side view as one vector in true proportions (1 unit = 1mm; viewbox = product + 6%), two or three dimension lines with figures.
- Never the hero, never the only picture, never on hardware, never on a page without photographs.

## 135. Menu in type
- A menu or price list in readable type beside a photo; product sold by weight/size reads the same ("250 g · €14").
- Mistakes: ragged prices or two currency formats; each dish in its own card; menu only as PDF or image; tabs or accordion.

## 136. Visit and map
- Use: where, when open, how to get there, with 2 to 6 practical rows (parking, dogs, step-free access, check-in); showrooms, studios, services with a door.
- The page's split: text (h2, address as street and district, hours with time zone, phone/email only if given, the main action and "Get directions"); right, a baked still street map with the pin on the street line (only for a street the brief gives), else a shopfront photo.
- With a district only: "See the area"; a town only: no map link.
- Phone: text first, map or photo 342 wide.
- Mistakes: map embed or screenshot; map of an ungiven street; moving route; credit on the map; "today" from the visitor's clock.

## 137. Booking form
- Use: the one task of a place or service page; a booking system link replaces it when the client has one.
- The page's split: text left (h2 "Book a room", what happens next, contact if given); form right on the alternate ground, 48 padding, never over a photo, texture or glass.
- At most six fields (dates, guests, name, email), primary button, status line, reply line ("We reply within a day").
- Visible labels; each error under its field; correct input types and autocomplete; text fields not native date pickers on a non-English page.
- Phone: text first, form full width, one field per row.
- Button = the main action word for word.
- Mistakes: form that sends nowhere; more than six fields; success message with no send; placeholder as only label; error only in red or only at top; a modal.

## 138. Client asset slot: trailer / motion video frame
- Its own section after the hero (or the world section), h2 above, frame across the container at 16:9.
- At 16:9 across the container it's ~700px tall at 1440x900, so cap height to one screen under its heading (720 max; auto under 1024 so tablet/phone keep 16:9); the poster sits letterboxed on the dark ground.
- Poster = a stand-in photo that reads as the film's first frame (game: widest setting photo; hardware: the same kind of machine at work).
- Play control real or absent, never dead; with no file, no controls; centre the play disc.
- With a file, tech may play muted looped with a pause button; poster only under reduced motion and on phones; never with sound.

## 139. Client asset slot: screenshot strip
- Three to five frames styled as captures, 16:9, same size (a trio or a row of four; phone one column); square corners or page radius; no device chrome, shadow or caption.
- Stand-ins: one grade across the strip, no two of one place or series, cover-cropped 16:9.
- As "what you do" cards: three to five open cards, each a verb over its capture.

## 140. Client asset slot: CAD, exploded, key art
- CAD/render frame: the product section's split frame or a bleed, render on a light flat ground, square corners; its stand-in is a product-kind photo no other section uses; counts as one of the object's three sections.
- Exploded frame: the parts section's picture; else close-up photos of parts.
- Key art: the hero's picture and the world band.
- Mistakes: a named slot left out; empty, grey or black frame; play button that does nothing; a source pointing at a missing file; caption saying the file is coming; one stand-in in every slot.

## 141. Pricing: three plans
- Use: software; three plans side by side, the middle recommended, optional monthly/yearly switch.
- Head on the left line: "Pricing", one grey line, and the switch (two tab buttons). 48px below, three span-4 plan cards; the middle featured with a "Most popular" badge.
- Each: name, who it's for, price with "/month", a billing line in both modes, full-width button (primary only in the middle), 5 to 7 included lines.
- From 1024 rows align across cards (subgrid) so buttons and lines align; cards never change height on switching.
- Phone: one column in plan order.
- Copy: "Priced per restaurant. Try any plan free for 14 days."; Team: "For restaurants with 15 to 50 staff", €59/month.
- No ground; still. Tech: featured plan's border may get a lit edge (one light runs round it on hover/focus, ~4.6s) when that is the page's one effect; its badge then quiet ink.
- Mistakes: cards changing height on the switch; a saving that doesn't match prices; plans for something that is no subscription (product, place).

## 142. Pricing: two plans
- Use: free + paid, or two fixed prices for a service; what both include said once.
- Grid: span-4 left with h2 "Pricing", grey line, the every-plan inclusions and a link; two plan cards on span-4 start 5 and span-4 start 9 (name, who for, price, button, 5 to 7 lines), recommended featured.
- Phone: one column.
- Mistakes: buttons at different heights; repeating the every-plan list in cards.

## 143. Comparison table
- Use: plans or models, or the product vs how the job is done today, row by row.
- Feature on span-4; two options on span-4 start 5 and start 9, or three options on span-2 each.
- Header row on the main ground with each option's name, price and a button (primary only for the recommended).
- Group headings as small labels; rows 48px each closed by a 1px rule; cells a check (screen-reader "Included"), a grey dash ("Not included") or a short value. Nothing sticky.
- Phone: each option its own block of rows; never sideways scroll.

## 144. Specs
- Product specs as ruled spec rows or a comparison table, beside a photograph (e.g. of the frame).
- No fact twice: a stat strip takes the three figures that sell (load, range, price); spec rows take the rest (sizes, weight, motor, battery, warranty). One fact, one place, one wording.

## 145. FAQ
- Use: the buyer's last questions (price, data, cancelling, formats); every answer open on load; no accordion.
- The page's split: left the h2 "Questions", a grey line and a contact link; right 5 to 8 items (question as h3, answer under, each closed by a 1px rule).
- Product: five questions at most.
- Questions in the buyer's words ≤60 characters; answers under 50 words starting with the answer ("Yes. Cancel in Settings and you are not billed again.").
- Merged into the section above under 495px.
- Phone: one column.
- Mistakes: questions the company wants asked; dodging answers; closed answers.

## 146. Close (shared)
- The close is row 1 of the closing footer, on the footer's own ground, never a band of its own; it asks for the main action once more, word for word.

## 147. Close: type and big button
- Use: any kind; no picture: the button is the picture.
- h2 (≤8 words, on the left line), optional small muted line (trial terms, opening hours), then the XL primary button.
- Software: button across the container, 88px tall, label in the display face at 32px. Product and service: 640 wide, 72 tall (a full-width slab reads blunt on a clinic).
- Phone: full width, 48px tall, 18px label.
- Example: "Plan next week's rota in ten minutes" / "Start free trial" / "Free for 14 days. No card needed."
- Mistakes: a second button; the big button elsewhere on the page; a ground behind it.

## 148. Close: photograph
- Use: place (always), product, service: the main action beside a photo of the place or the product in use.
- Head row (h2 ≤8 words, one line such as "Open today 7:30 to 16:00", the main action), then the client's photo line to line down to the links; never used above, never with words on it.
- Place: a 1:1 photo on span-5 with words beside it; on a brand-colour band every word at 7:1 contrast and the button inverted.
- Phone: words and full-width button, then the photo.
- Mistakes: reusing the hero photo; words over the photo; a band out to the viewport.

## 149. Close: wordmark
- Use: software, product, service (never on a place's colour band).
- h2 and button on one head row, then the client's name as one line set across the container line to line in the display face (sized per breakpoint, never scaled by transform).
- Phone: head stacked, name across 342.
- Mistakes: name larger than fits at 1024; the name repeated in a footer wordmark.

## 150. Footer: columns
- Use: the quiet footer on the base ground (software, products, services).
- Company block on span-4 (logo, one line ≤8 words in the display face at 28px); four link columns on span-2, named and ordered as the nav, each link a page section, Contact to the contact anchor; the newsletter field once ("Subscribe") when the page has one; legal row: brand and year, Privacy, Terms, (Imprint only with real details), empty socials, credits line last.
- Phone: columns two-up, legal row stacked.
- Mistakes: columns differing from the nav; links to non-existent pages; drawn or coloured social icons; effects in the footer.

## 151. Footer: dark
- Use: software and product (the one dark band at the end).
- Inverse ground: company block on span-4 (mark and name at 48px in the display face), four span-2 columns, legal row. On a dark page a step darker than the page with a hairline on top.
- Phone: name at 30px, columns two-up.
- Mistakes: a second dark section right above it.

## 152. Footer: visit
- Use: a place's or local firm's footer: where it is, set large, with the way there and hours.
- Address on span-7 (street and district on two lines; district alone if no street), 32/40 on a place, 48px elsewhere, in the display face; one line on the way there (stop, minutes on foot) and a "Get directions" link (no button).
- "Opening hours" on span-4 start 9 with today marked (in the place's time zone).
- Then nav row (logo, nav words, Contact), legal row with one credits line last; on a place the name set wide across the container in the display face at weight 400, at most 12vw (~170px at 1440), except on the colour band or with the name moment.
- Phone: address 24 to 30px, hours under, nav row wrapping.
- Mistakes: hours differing from the visit section; today from the visitor's clock; a map in the footer; an email/phone not given.

## 153. Footer: statement slab
- Use: tech only: close and footer as one designed slab on the lit ground (sand, sky, sage or painting).
- Inset 8px from the window's sides and bottom with large-radius corners; the close as the big-button close, 96px to the columns, then the legal row.
- Phone: full bleed, square corners.
- Mistakes: a second big button; an effect on it.

## 154. Phone action bar
- Required on places; holds the main action (order or booking) as one full-width button; without either, Get directions (primary; "See the area" with no street) and Call (secondary, only with a given phone).
- Hidden on the first phone screen until the hero's button scrolls away, and off any screen already showing one of its actions.

## 155. Place: visit section
- Always screen 2, directly after the hero.
- A panel on the alternate ground, 48 padding, on span-6 only (a ground box 80%+ wide is a band), beside a 1:1 or 4:3 photo of the shopfront straight-on or the room from the door; 6/6, panel left.
- With the address moment: h2 and the street set large across the container above the split (photo then 4:3), the panel opens with the open-now line. Else the panel's top line is the h2 "Visit" with the open-now line at its right (never a 13px eyebrow); open-now only with given hours.
- 16px below, two columns 24 apart: address on two lines at 20/30 linked to the map, phone as a call link only if given, then one secondary button ("Get directions" when the main action is something else and a street is given; "See the area" with a district only; "Call" only with a phone; else none); the week's hours (days left, times right in tabular figures, one line per day or range, one size; a holiday change as one line above).
- Under both at most two 44px rows: access, delivery (area, price, cut-off), check-in/out, repair turnaround, "By appointment".
- Phone: panel first (24 padding, address 18/28), then the photo at 342 growing from its ratio up to 4:5 to fill what's left so the screen ends in the photo.
- Hours, address and directions never only in the footer.
- Map only with a given street: a baked still in the photo's frame, pin on the street line; never an embed, contour or dot pattern.

## 156. Place: the offer (menu or prices)
- Head row: h2 on the left line, one line ≤40 characters (32/40; 24/30 at 390); at its right on its baseline one 16px line and a link ("Full menu", "See all"); 56px to content.
- Strip composition: three groups on span-4, the four-detail strip under them. Pair or tall-small: two groups on span-3 at left, photos on the right span-6, top level with group labels.
- Paired groups hold the same number of rows.
- Group: 13px label (weight 500, ink), 12px air, no rule under it; then rows each closed by a 1px rule (none above the first): name 16/24/500 left, price right in tabular figures, optional description 16/24 muted; rows 44px (64 with description); at most 6 with descriptions or 8 without, the rest behind the head-row link.
- Always text, whole, prices visible: never image, PDF, tabs or accordion. Phone: one column, photos after the first group.

## 157. Place: rooms
- h2 "Rooms and prices", side line ("Breakfast 8 to 10. Check-in from 15, check-out by 11.").
- Each room: 4:3 photo of the whole room, straight-on, window light; 20px; name (20/28); facts 16/24 muted ("2 guests · 18 m² · garden side"); "from" price with season at 16/24; "Book this room" link.
- Row layout: three on span-4 (384x288) or four on span-3 (282x212). Two rooms always side layout.
- Side layout: the head as first cell at the left line, top-aligned with tiles (two rooms span-4; three span-3; four in 2x2 on span-4 over two screens).
- Five or six rooms: rows of three on span-4 in a two-screen section. Phone: one column, 342x256, 48 apart.

## 158. Place: goods
- Four linked cards on span-3, 1:1 at 282x282 (bouquets 4:5 at 282x352); one ratio per grid; one backdrop, angle and light.
- Card: a flat fill one step off the ground or a 1px hairline; no shadow, radius or pill; under the photo only the name (two-line slot, 16/500) and price; an outline Add button aligned across the row where it sells online.
- One or two full rows. Phone: two-up at 165, four or six, then a full-width button to the range; no swipe row.

## 159. Place: orders
- Three kinds on span-4 under the head row, or two beside the head in the first span-4.
- Each: 4:3 photo of this business's own goods (384x288), 1px hairline, 13px label, title 20/28, one or two sentences 16/26 with lead time, collection point and "from" price, one text link with arrow.
- An events kind says what to send: date, venue, guests, budget.

## 160. Place: booking
- Head row ("Book a room"; "We reply within a day."), then a 4:3 photo on span-6 (588x441) beside the form on the alternate ground at the same height, 48 padding: arrival and departure on one row, guests and name on the next, email, main action, reply line at 14px.

## 161. Place: notice line and splits
- Notice line (delivery cut-off, changed hours): one still 14px line with a number above the h1, repeated where the fact belongs; never rotating.
- Splits 6/6, text left, top-aligned, never mirrored; phone text first.

## 162. Place: display-type moment
- One per page, dealt as address or name.
- Address: street and district set large right under the visit h2 ("Find us" at h2 size): display weight, `clamp(48px, 7vw, 104px)`, line-height 1.02, letter-spacing −0.03em; one or two lines on the left line; drawn underline on hover; linked to the map. No street given: district alone, never invented.
- Name: the close becomes the wordmark close; its photo goes to the place's composition.
- Ink on the ground or brand band; never outline, pale, rotated or on a photo. Then the footer's wide name is capped at 12vw or left out.

## 163. Place: hover and actions
- Every photo that leads somewhere is a link and zooms 1.03 inside its frame while its card lifts 2px; head-row links carry an arrow that moves 3px; nav words draw their underline. Each section after the hero holds at least one such link.
- One main action a screen; a transaction is the nav's and hero's button and appears elsewhere only in the booking/close and phone bar.
- Get directions is never repeated: hero button + phone bar (+ nav button on desktop: two per screen max); nav says "Visit" as a word; visit block adds no second button for it; footer gives the address linked, never a button (in testing three copies read as clutter).
- List text 16/24 minimum (menu rows, descriptions, room facts, hours); muted colour, never smaller size, marks a description; 13px only for group labels.

## 164. Composition: bleed
- Head row on the container (its line at the right), then one photograph across the whole viewport, 1440x560, nothing on it.
- Phone: 390x488 (4:5 crop).
- Once a page; never right after the hero; the split never right after a bleed.

## 165. Composition: pair
- Two photographs on span-6, same ratio: 4:3 at 588x441, or 4:5 at 588x735 in a two-screen section; tops level; head row above.
- Phone: stacked, 342 wide, 24 apart.

## 166. Composition: trio (offset)
- Three photos: span-5 at 4:5 (486x607), span-4 at 1:1 (384x384), span-3 at 4:3 (282x212); tops on one line; three sizes of one subject family (the room, its table, a cup).
- Phone: first at 342 wide, the other two two-up at 165.

## 167. Composition: strip (details)
- Four 1:1 details on span-3 (282x282) or six on span-2 (180x180), line to line: hands, tools and materials of one trade; under the section's text or groups.
- Phone: two-up at 165, four at most.

## 168. Composition: tall-small
- A tall 4:5 photo on span-6 (588x735) at the left line; on span-5 at the right the h2, its lines and link at top, and a 1:1 on span-3 (282x282) at the bottom, its foot level with the tall one's.
- Phone: text, tall at 342, small at 165.

## 169. Composition: wall and story
- Wall: head row then a wall of photos line to line, gap 0 or 2px; phone two-up.
- Story: 6/6, text left (h2 one or two lines, three to six lines at 20/30 on who runs it, since when and what exactly, one link), a 4:3 photo of people at work right (588x441). One story row a page. No names under photos. Phone: text first.

## 170. Composition use by section
- The offer deals pair, strip or tall-small: strip runs under the menu's groups; pair and tall-small take the photo slot beside them (groups narrow to span-6).
- The place deals bleed, trio, strip, pair, wall or story (re-deal while it equals the offer's).
- Product picture sections deal from bleed, pair, trio, strip, tall-small, plus split (once, never right after a bleed) and the order section (last, a form, not counted as the split). Product meanings: bleed = product at anchor scale across the viewport; pair = two views one ratio; trio = whole, part, detail; strip = four part close-ups the rows name; tall-small = product in use tall, a detail small.

# Part 8 — Hero archetypes

## 171. Hero frame
- Exactly the first screen, `100svh`; padding-top nav + photo + hgap (120 at 1440, 96 on phone); padding-bottom hpadb + bar (64; 24 + bar on phone); content ends by y 836 at 1440x900.
- The hero ends at the fold, 1px either way; content between the nav and 24px above the fold.
- Nothing of the next section shows at 1440, 1280, 1024, 820, 768 and 390.
- Content: optional notice line, the h1, the sub-line, at most two buttons (a place one), the picture.
- One plain claim, never a slogan; no caption under the picture, no second float card, no three button styles.
- Buttons above the fold at every width; the main button below the first screen FAILs.
- h1 first, top at y 120 (96 phone), at most three lines at every width, never smaller than an h2 (28 to 60px on phone).
- Notice line: one 14px line in the body face with a number, 4.5:1, 16px above the h1; never a bar above the header.
- The picture ends inside the hero: a layer behind words, beside them in a split, or above/below only if the whole hero ends by H - 24; a frame under the words ends by y 836 (about 296px under a 356px text block); larger becomes a layer.
- Never a first screen ending on a visual cut by the fold; never half a picture under the text.
- At 768 and 820 the first screen ends on a whole element (24px+ above the hero foot) or a clear bleed (a cover photo, or a fragment cut through 96px+ of rows under a bottom fade, its point above the fade); never 1 to 95px of a box under the fold.
- Below 1024 over-pieces hide; give the main piece a fluid width, never fixed.
- Docked strip (software and product only): one row under the hero content, at most 96px, still (real customer logos with permission, a rating the brief gives, or three facts); hidden on phone unless it ends by H - 24 - bar; service and place dock nothing.
- Phone: text first; a photograph above it only when the whole hero ends by H - 24 - bar; hero buttons stack unless both fit on one line.
- Allowed hero types: full-bleed still photograph, a product whole on a stage, an inset frame, a statement followed by the work; tech only: a film in a frame or behind text (muted, inline, poster first, a pause button) or a 3D hero (poster first).
- On other kinds a film is a still that plays on a click.
- Every hero has one motion of its own at most, resting under reduced motion and on a phone.
- A hero fails with a picture out to one viewport edge, a hero taller than the screen, the visual above the text on a phone, words over the busy part of a picture, a second float card, a slogan, a caption.

## 172. Hero: shared rules
- Exactly one screen (`100svh`) with the fixed header (72, 56 on phone) over its top.
- Words start 48px under the header (y 120 at 1440x900; y 96 at 390x844; 40 and 24 under a place's photograph).
- Content ends 64px above the fold (24 on phone, plus the action bar); nothing of the next section shows.
- Blocks stand on the container lines (x 80 and 1360 at 1440; 24 and 366 at 390) or run edge to edge; never to one viewport edge only.
- Nothing laid over a photograph to make words readable: no scrim, gradient, veil or blur.
- Hero content box height at 1440x900: 716 (900 − 72 − 48 − 64).
- Lead size 20/30 at 1440, 17 at 390 (line-height 1.5), max 42ch; headlines balanced.
- Every hero enters once on load; on non-tech kinds and places nothing else moves by itself (live words, collage sets and loops rest on their first or finished picture; pointer-driven letters and hover stay).
- Choose the hero at random weighted by business type and the material really available; type-only heroes (word, statement) only when there is no strong photograph or film.
- h1 sizes (1440 / 390): split, product, film, centred 72/40; photo 80/44; collage 64/40; editorial 156/56; word 144/54; statement 56/34; triptych 52/40; place 48/32. Scales linearly between 390 and 1440, times the font pairing's optical scale.

## 173. Hero copy and picture (all heroes)
- h1 names the category and the buyer or place in 2 to 8 words.
- Sub-line 15 to 30 words: how it works and the main benefit, with one hard fact (place: 80 characters with today's hours).
- Primary as verb + object; one quieter secondary (place: none).
- Picture is the work: product in use, the place or the people; a phone for an app (device 280x570, 8px bezel, radius 32, one fragment in its phone layout); one window for a web app (window at corner, 56/56 offset, cursor or notification piece over its lower-right edge); a technical product's object on the lit ground (tech only).
- App downloads as text buttons ("Download for iPhone"), never store badges beside the system buttons.
- Window heroes: at most two pieces; the main may loop (tech, with pause button), the second holds still; never tilted or scaled, never sample text, never a lone fragment floating in the middle.

## 174. Hero selection by business type
- Software: collage and centred (strongest), split, word, statement, triptych; product stage and film occasionally.
- Product: product stage (strongest), photo, film.
- Service: split and statement (strongest), photo, word, film.
- Gaming: photo and film (strongest), product stage; never word, statement or any UI hero.
- Place: always the place photo hero.

## 175. Hero archetypes at a glance (composition at 1440 / at 390 / motion)
- split: text span-5; picture span-6 start-7, top-aligned with the h1, ending on the right line; one opaque float card lower left / text then picture (at least 240 tall) / the float card's dot (tech).
- photo: full-bleed photograph layer, words on its calm dark side on six columns (h1 80, two lines), four facts at the foot / photo cut to the top, words under it on the ground / none.
- product: head row (h1 cols 1-7 on two lines; lead and buttons stacked on cols 9-12, foot aligned with the h1), then the product big with nothing on it; a photograph edge to edge to the fold, square corners; or a cut-out/render across the wrap on the page ground, no box, gradient or radius, stage down to 24 above the fold (1280x566 at 1440x900; e.g. a bike 1046 wide, 82% of the wrap) / stacked; photo screen width, a render 86% of the column (294 of 342) / none (a render is a still).
- editorial: the headline is the picture, 156px on three lines across the wrap, one or two photographs set in the line as pills / 56px on four lines / pills open once on load (tech). (alternative: this hero is retired in the later rule set because pictures sit inside the headline.)
- collage: text span-5; a lit frame span-6 start-7 with the product window cut by its bottom, one looping result card / the window alone / one card loop (tech).
- word: oversized h1 (144px, two lines) with one live underlined word last; lead and buttons span-6, four facts span-5 start-8 / 54px on three lines / the live word, two rounds then rest (tech only).
- film: a cinema frame on the lines holding the poster, h1 white on a calm part, play disc at its foot / frame, then words / plays on a click.
- statement: one calm sentence (56px, two lines) over the page ground, lead, buttons, four facts / 34px on three lines / none.
- triptych: h1 52 on span-3, a collage of three to five pieces on span-6 start-4 changing sets every 2.8 s, one large button ending on the right line / collage 342 wide, button full width / set change (tech only).
- centred: pill, centred h1 72 with the mark inline, lead, two pill buttons, then a lit frame across the wrap holding the product window, fading over its last 18% / the window less its list column / the window's story (tech); the only hero on the page axis.
- Deal word and statement only without a strong photograph.

## 176. Hero: place photograph above words (layout values)
- One still full-bleed photograph of the place under the header with nothing on it (no text, scrim, gradient, fade or box), words on the ground below.
- 1440: photo 480px tall (y 72 to 552, subject in the middle 640px), hgap 40px; h1 48/53 on columns 1-6 (x 120 to 708, y 592, at most three lines); from the split line (x 732) the sub-line at 20/30 (kind of place, where, today's hours; at most two lines, 80 characters) and one filled 48px main button 24px under it; the row ends by about y 760, never past 836.
- A shop or bookshop may use a letterbox in the column: 1200 x 504, 24px under the header (photo 528px).
- 640 to 1023: photograph at most 56vw tall, words stacked under, hero ending by H - 24.
- 390: photograph at least 390 x 292 (subject centred), may grow to 390 x 488 at most (about 390 x 480 at 390x844, 4:5 phone crop) so the screen ends on the button; hgap 24, h1 32/37 (max three lines), sub-line 18/28, one 342 x 48 button; stack ends at H - 24.
- The photograph is real, of this place, in daylight: the room from the door, the counter with the machine, bread on shelves, the shopfront with customers, the workshop stand, an arrangement in a real room, the best room or the house; never a mood shot, scenery, cut-out or hazy file; a florist never opens without flowers.

## 177. Hero: place photograph above words (alternative values and mistakes)
- Use: the only place hero (bakeries, cafes, guesthouses, shops), never for other kinds.
- The client's own photo full-bleed under the header, nothing on it: y 72 to ~552, height min(480, 53svh) (1440x477 at 900 tall); subject in the middle 640px.
- On the ground under it: h1 on columns 1 to 6 (x 120 to 708), 40px under the photo, 48/53 on 2 lines (≤48 characters, 3 lines max on phone); from column 7 (x 732): sub-line (≤2 lines, 20/30), then one filled 48px button 24px under it; row ends ~y 750.
- Phone: photo 390x293 (4:3) at y 56 (below 1024: 56vw, max 46svh), then h1 32/37 (≤3 lines) from y 373 with 24 gap, sub 18/28 (opening days and time), one full-width 48px button.
- The visit block is screen 2, never in screen 1.
- Mistakes: words, scrim, gradient or box on the photo; any other hero type on a place; visit/address in the first screen; stock photo for the client's place; rounded photo corners; two buttons or a pill button.

## 178. Hero: place copy
- What, where and one fact: h1 ≤40 characters ("Bakery on Mill Street, Leith"); sub-line ≤80 ("Sourdough, rye and cardamom buns from 7:30, Tuesday to Sunday."); one button, the main action.

## 179. Hero: split, picture right
- Use: service (strongest), software; text left, the real thing right, both whole on the first screen (product in use, the place, the people; a phone or one window for software).
- Text span-5 (519), top-aligned: first line (notice line or h1) on the picture's top line, y 120. Optional notice line 14px at y 120, 16 to the h1.
- h1 72/1.02 on ≤3 lines (≤45 characters), from y 158 with notice (120 without, capitals trimmed to the picture's top); lead 20/30 ≤3 lines max 42ch, 24 under h1; buttons 44 tall, 32 under the lead.
- Visual span-6 from column 7 (628x716 at x 732, y 120), ending on the right line, as tall as the content box, radius large on all four corners.
- Optional float card: one opaque card 300 wide, flat (hairline, no shadow), 24px in from the picture's lower-left, showing a live fact (out of the oven at 10:30, next free slot); its dot breathes every 2.4s.
- Phone: h1 40 on 2 lines, lead 17/25.5 on 4 lines, buttons stacked full width (44 + 12 + 44), visual 342 × remaining (≥240), 32 under buttons, cover-cropped round the subject.
- Software: one loop inside the window or phone.
- Mistakes: picture bleeding to one viewport edge; faces cropped; picture above text on phone; picture under six columns; float card covering the subject; a second float card.

## 180. Hero: full-bleed photograph, words on calm side
- Use: product, service, gaming (strongest); one strong photo with a calm area (sky, wall, cloud, shadow); never software; never place.
- Photo edge to edge under the header, at least 1920 wide, positioned to keep the subject off the words.
- Words in the left six columns (628) on the calm side, in a solid box of the page's colours (padding 48, large radius), movable left/right/top; or no box: words straight on a dark (or light, empty) calm part.
- h1 80/1.02 (≤32 characters, ≤3 lines, max ~14ch), from y 231 in its box; lead 20/30 on 3 to 4 lines max 42ch; buttons 44, the page's own pair.
- With no box only: a hairline and four facts on span-3 docked 48px above the photo's foot.
- Phone: photo a layer under the header at 42svh (354), words under it on the page ground; h1 44 on 2 lines from y 450, lead 17 on 4 lines, buttons stacked; facts hidden (next section carries them). From 1023 down: 56vw, max 46svh.
- Game without art: the game's name as the h1 set large on a setting photo.
- Mistakes: words on a busy part; a photo not showing the place/product; an upscaled photo under 1920px; a carousel; scrim, gradient or veil; words on a busy or pale area.

## 181. Hero: product stage
- Use: product (strongest), software, gaming; the product itself big under one head row.
- Head row: at 1280+ h1 on columns 1 to 7 (2 lines, ≤40 characters), lead and buttons stacked on columns 9 to 12 with their foot on the h1's foot; 1024 to 1279 h1 on 1 to 6, lead and buttons on 7 to 12; under 1024 stacked.
- h1 72 on 2 lines from y 131; lead 20/30 on 3 lines, 411 wide; buttons 44; head ends at y 278.
- Stage: a render or cut-out on span-12 (1280), 32 under the head, down to 24 above the fold, on the page's ground (no box, gradient or radius), its frame reaching 7% past the stage's top and bottom so the product fills the stage height; stage 1280x566 at y 310.
- The widest view spans 80%+ of the container (a bike's side: 1046 of 1280, 81.7%; a three-quarter view at 818, 63.9%, is too narrow). Measured fill: 86% at 1024, 768 and 390.
- A photograph instead: full screen width down to the fold, square corners, cropped so the product spans 80%+.
- Phone: stage 342 × what the head leaves (394), product 86% (294 wide) centred; photo at its own ratio (390x293).
- Nothing on the product: no hotspots by default; only when asked: one to three 32px discs each opening a 230px spec card (phone: card under its disc, 16px inside the stage).
- Game variant: name in the h1 (or wordmark above), date/status in the lead, key art on the stage; an effect only behind it.
- Mistakes: object small in an empty stage; object in a rounded box or on a gradient panel; three-quarter view of a long product; object cut by the stage; words on the stage; UI cards over the product; a second object; a game stage holding an abstract effect or toy object; a game hero not naming the game.

## 182. Hero: editorial type with inline pictures (retired)
- Retired; do not use: pictures inside a headline break the "no picture inside a headline" rule.
- (Former form: three lines of 156px left-aligned type, leading 0.98, ≤34 characters, with one or two 0.8em-tall pill photos 1.7 to 2.1em wide in the line, never two in one line; lead on span-6 and buttons on columns 9 to 12 under a hairline at the foot; 56px on 4 lines max on phone.)
- Mistakes it was prone to: mood pictures instead of work; centred headline; slogan; a frame under the type.

## 183. Hero: UI collage cut by its frame
- Use: software only; text left, the main window on a lit ground on the right six columns, cut by the frame's right and bottom edges, one small result card over its lower-left.
- Text span-5 (519), top-aligned, h1's capitals on the art frame's top line (y 120); h1 64/1.02 on ≤3 lines (≤48 characters); lead 20/30; buttons 44; one muted proof line 24 under them.
- Art frame span-6 from column 7 (628x716 at x 732, y 120), large radius all corners; lit ground (sand, sky, sage or painting) with one soft light, or an effect (no grain alone).
- Window: 64px from the frame's left and top, running 28px past the right edge; its content keeps 48px clear at the right so the cut falls in empty margin after the status chips; no time column.
- Small card: 300 wide, 32px in from the frame's lower-left, over the window; loop: finished first, hold 1.8s, three steps arrive 0.7s apart, hold; restarts on pointer enter; pause disc bottom-right.
- Phone: art 342 × remaining (≥220), 32 under text; window alone, 16 in, sidebar and quantity column hidden, chips whole; small card hidden.
- Mistakes: frame bleeding to a viewport edge; window cut on all four sides; status column cut; more than one small card; frosted wrapper round the window; UI text under 12px; a status chip cut by the edge.

## 184. Hero: oversized headline with one live word
- Use: service, software; type does the work when there is no strong photograph, film, UI or object; never gaming.
- h1 144/0.92 across span-12 from the left line, two locked lines (≤28 characters), the live word last; block centred in the hero.
- Live word slot as wide as its widest word, so no line reflows; the accent underline 0.05em thick under the live word only.
- Foot 64 under the h1: lead 20/30 on 3 lines on span-6 with buttons (44) 32 under; four facts as a column (label left, value right, rows of 50, hairlines) on span-5 from column 8, ending on the right line.
- Motion: a new word every 2s for two rounds, then rests on the first, replays on pointer enter; letters near the pointer thicken (+200 weight) and widen (+10%) on a font with a width axis; phone and reduced motion hold the first word.
- Phone: h1 54 on 3 lines; facts 2x2 under the buttons.
- Mistakes: a slogan (must say what is sold); more than four words in rotation; a word that turns the line into nonsense; underline on the whole headline; a font without weight axis; a line rebreaking when the word changes; stacking a second word-rotate effect; using it when photographs exist.

## 185. Hero: cinema frame (film poster)
- Use: product, service, gaming (strongest), software; a client with a real film, or a strong photograph with a calm dark foot.
- One rounded frame on span-12 (1280x716 at x 80, y 120), from 16 under the nav to 16 above the fold; the poster in it.
- Words in a solid box of the page's inverse ground at the frame's lower-left, 32px in, max 600 wide (h1 15ch, lead 42ch), padding 48; h1 72 on ≤3 lines (≤42 characters) from y 358; never on a scrim.
- Play control at the frame's right foot, 64px in: a 64px white disc, its label 20px in a solid pill of the inverse ground, running time 14px under it. It plays the film in the frame with controls or links to the film's page; never autoplays sound.
- Phone: frame 342x724 at y 96; box across the frame's foot, 12 in, padding 24; play disc (52) and label first, then h1 40 on 3 lines, lead 17, buttons stacked.
- Mistakes: a play button with no film; words over the busy part; autoplay with sound; a stock poster; frame narrower than the container; scrim or gradient to carry white words.

## 186. Hero: quiet statement over a ground
- Use: service (strongest), software; a company whose product is trust or a service, with no strong picture; never gaming; never with photo, film, UI or object available (except a place's last resort on the brand ground).
- One calm sentence: h1 56/1.1 on 2 lines (≤54 characters, max 21ch) from the left line, top at y 120 (y 184 with a news pill: pill 32 tall at y 120 only for real news, then 32 gap).
- 24 to the lead (20/30, 3 to 4 lines max, max 42ch), 32 to buttons (44).
- Four facts on span-3 under a hairline docked at the hero's foot (64 above the fold).
- The ground carries the look: a dark horizon with a lit rim rising behind the facts, a grainy lit-tone field, a halo, dusk, or (software) slow liquid blobs with a pause disc.
- Phone: h1 34 on 3 lines; facts 2x2; place page top gap 24.
- Mistakes: a pale wash that reads as an empty page; a ground fighting the words; centred statement; a second visual; a lead over three lines; liquid letter effects on a headline over six words.

## 187. Hero: triptych (headline, collage, button)
- Use: software; a product with many outputs (design tool, menu or print tool, shop with several lines).
- Three columns: headline span-3 (302) centred in the screen height (from y 365), 52/1.04 on 3 lines (≤34 characters) with a 16/24 line under it; collage span-6 from column 4 (628x716 at x 406, y 120); one large button span-3 from column 10, right edge on the right line, 64 tall with a 20px label in the page's primary style.
- Each collage set: three to five pieces (photos, a printed piece, a small UI card) placed in percentages, overlapping only where no text sits; one piece per set ends at 96% x 96% and the pause disc sits on its corner.
- Sets crossfade (0.7s) every 2.8s; nothing moves inside a set; phone holds set one.
- Phone: headline 40 on 2 lines; collage 342 × remaining (≥300); button 56 tall full width under the collage.
- Mistakes: pieces sliding, scaling or tilting; a piece cut by the collage edge; more than five pieces; a set that resizes; button styled differently from the primary; a piece over another's text; the pause disc on empty ground or over text.

## 188. Hero: centred headline over one window
- Use: software whose product is one window or one assistant.
- Centred block on the page axis, max 880: news pill 32 at y 120, 16, h1 72 on 2 lines (≤36 characters, max 16ch) with the mark inline, 16, grey lead 20/30 on ≤2 lines max 52ch, 28, two pill buttons (44) centred.
- Then a lit frame on span-12 (1280), 32 under the buttons, down to the hero's foot, its last 18% fading out (solid to 82%); at 1440 it shows its top 335px.
- Window 880 wide, 32 under the frame's top; the key exchange (question on one line, tool line, two-line answer, Send and Edit) ends 278px into the frame, above the fade; a side column may run into the fade.
- Loop: the question stays; tool line, answer and actions arrive ~0.9s apart, hold 2.4s, replay; the ground drawn once and held.
- Phone: frame 342 × what the words leave (≥240), fading over its last 28px; window = frame width less 32, 16 in, list column, right bar label and tool line hidden; exchange ends ~230px in, above the fade.
- Mistakes: a lone fragment floating mid-frame; a third button; frame wider than the container; dark UI on a dark ground; hero taller than one screen; window cut through its first rows; the exchange inside the fade.

# Part 9 — Cards

## 189. Why great cards look expensive
- The card is barely there: one step off the page, a hairline, generous padding; colour lives inside the panel.
- The panel holds a real lit picture (painted landscape, grain field, mesh, satin), never a flat two-stop gradient or a line/dot pattern; on a dark page it is the brightest thing in the card.
- The UI on it is real product at true size, cut by the panel's edge: a glimpse of something bigger.
- One thing moves per card group, inside a panel (tech); the card never moves by itself.
- Everything lines up: panel edge with text edge, radii nested, titles level across a row.

## 190. Card box
- Fill one clear step off the page: light = white on `#f3f3f1`; dark = `#151517` on `#070708`. Or no border when the photo or flat fill is the card.
- Border 1px, ink at 8 to 14%; dark cards add a 1px inner top highlight (white 5 to 7%).
- No blurred shadow at rest (a hard zero-blur offset allowed); a linked card may show a soft shadow on hover only and lifts 2px; non-linked cards don't lift.
- Never tilted, never a carousel: rows show whole cards; press quotes stack.
- Radius 20 (18 on phone). Padding 32 from 1024, 28 below, 24 on phone; never under 24; text always inside. A filled split panel pads 48.

## 191. Card text
- Title one line at the card-title size (20, 18 on phone), weight 500.
- 8px, then at most two lines at 16/24 in body ink (84% ink), at most 46ch; never small grey text.
- All running text in a card is 16/24 in that ink (points, stat lines, plan lines, a quote's name and role, bar labels). Muted small text only for labels ("/ month", a section tag).
- Lines held at two from 1024 so titles and panels align across a row.
- 32px from the last line to the panel. One panel height per card group; add a phone value when tiles stack into two screens (e.g. 180px holds four two-line tiles in two phone screens).
- Never 15px muted card text.

## 192. Two levels, never three
- Card > panel (a lit picture) > fragment. The panel reads as a picture: a soft field with no border lines, grid, ruling or dots.
- Never card > patterned panel > white UI card; never a fragment that is itself a card of text cards; never a text card inside a card; never glass.

## 193. Panel types
- Default: side edges on the text column, runs off the card's bottom, top radius 12, the lower 60 to 65% of the card (264 to 340px tall).
- Inset: even 8px margin; radius = card radius − margin (20 − 8 = 12), never under 6. Every panel in a row one ratio (4:3 or 16:10) and one inset. A smaller UI card on it is solid (never frosted), 40 to 60% of the panel's width, offset so the bottom or right edge cuts it.
- Flush: runs to the card's side and bottom edges (image band).
- Top: on top with 8px margin, the card's lines below (tall cards).
- Device: a status row on the card (app name, muted context, quiet status with a still dot), then the ground as its screen, radius 12, running off the bottom; the row is not a frame of its own.
- A 1px inner edge sits over the ground and any fragment it cuts; a vignette calms the ground where the fragment sits.

## 194. Panel grounds
- Shader grounds in panels: tech pages only, one card group per page, still, from the family of the page's one effect, never the hero effect's id; a new seed per panel.
- Product/service panels: the client's photo (zooming 1.02 to 1.03 when linked), real icons or a still diagram on a flat ground. Place: no feature cards.
- Behind a fragment, a soft field (painted landscape, grain gradient, gradient mesh, silk folds). Never grid pulse, ruled grounds, contours, dot terrain, ridgelines, halftone or dither behind a window, list or card (those are pictures on their own).
- Panels holding UI get a light palette, same in both themes: on dark pages clearly lighter than the card (3:1+), so page, card, panel and UI are never four near-black layers; on light, a clear step darker than white UI.
- Palettes: painting bg `#a3b0b6` accent `#c49a6c` (level mist over warm sand, fully soft; blur 1, brush 0.35, slope 0, hill 0.3, horizon 0.62); sand bg `#d9ccb7` surface `#e9e0d2` ink `#2a2622` accent `#a8794a`; sky bg `#c6d3df` surface `#d6e0e9` ink `#25303a` accent `#3f6a92` (silk takes `#7f9fbd`); sage bg `#cdd6c6` surface `#dce3d6` ink `#262d24` accent `#6c8e63`.
- At most one painted panel per card group (one per page better). Never a blue sky over a green hill with a diagonal crest (stock wallpaper). Never violet or lavender.
- Hold every card ground still; calm it where the bottom fade shows it.
- A ground must show something behind something; a strip of effect under a stat or text line, holding nothing, is decoration: leave the card plain.

## 195. Feature cards with inset panels
- A 2×2 of cards, each a title and two grey lines, then an inset panel with its own 8px margin (panel radius = card radius − margin). The panel holds a bright ground and one UI window that runs out through the panel's bottom edge — no empty space under the last row.
- Ground: painterly landscape (default) or grain gradient, still, drawn once as pictures.
- The window shows the feature with real labels (an invoice, a checkout, payouts, an invite).
- At most two panels run a short pointer demo (glide, click, state changes, rest), one per row.
- Mix four panels, e.g. day, a grain, dusk, meadow — no two panels alike (vary horizon, side, slope).
- Rejected: a small dialog centred on an empty ground; an orb/sphere ground; a landscape painted in the accent hue only (reads as a filter; an orange accent turns rust-red); a warm accent mixed into a dark ground or a complementary accent mixed into a colour page (mud).

## 196. Landscape lights for panels
- Day: a pale sky over hills stepping down to a near slope; graphite hills under a warm accent, blue-grey under a cool one, the accent itself when green or neutral; deeper shades of the page colour on a colour page.
- Dusk: a deep blue sky lit gold only along the horizon, dark hills with a lit crest, whatever the accent (a blue glow under a blue accent just reads as darker day); gold leans warm with a warm accent but stays between amber and gold (red-orange turns crests rust). On a colour page, a light shade of the page colour.
- Meadow: daylight as a photograph shows it, whatever the page — clear blue sky paling to the horizon, a blue far ridge, sunlit grass (on a blue colour page the sky is the page colour). One per grid.
- Grain panel: a light warm ground under a warm accent, a deep one under a cool accent, the page colour's own shades on a colour page.

## 197. Card motion
- One loop per card group (the one whose motion shows the point); every other fragment holds its finished picture; phones hold all but voice.
- Pause button on every loop: a solid 32px disc in page colours, beside the card's title at the right of the text column (title keeps 44px clear); in a panel or frame outside a card, 12px in from the bottom-right; a fragment with no panel gets it under its bottom-right in 44px kept free.
- Anything moving by itself more than 5s gets a pause button.
- Loops start on the finished picture; never an empty window or greyed text; rewritten text appears in under 0.8s, no word below 72% ink (4.5:1 on white).
- Cycle 2.5 to 4s, repeating, restarting when pointer or focus enters; an all-held card plays its top fragment while the pointer stays; keyboard focus plays a held fragment once.
- Stop off screen; still under reduced motion; nothing moves on scroll.
- A cut tile hides its name rather than half a word. Counts keep their words, only the figure changes.

## 198. Card visual devices
- Control drives the ground: a slider changes the panel effect as the thumb moves; make it the group's loop; compact version fits a centred focal tile.
- Data cut out of UI: stat bars cut out so the ground shows through.
- Number filled with an effect: a still canvas under white text with darken blend on dark (black text, lighten, on light).
- Live voice orb: on dark a pale nebula with specks; on light a CSS pearl with accent and ink clouds turning slowly; the accent only as a thin ring; never a dark glass ball on a light card.
- A real object as the whole picture of a top panel on a lit palette, centred; it turns, never tilts the card.
- Lit border on the one featured object: quiet accent hairline at rest; on hover/focus one light runs round the edge (~4.6s) then fades; never on scroll or view.

## 199. Pictures on cards at mid widths
- 640 to 1023: a card with a panel takes the full row.
- 1024 to 1279: span-4 cards with a panel go two-up, so a span-4 panel is never under 304px.

## 200. Card type: feature 2x2
- Four span-6 cards, each its own small working visual (headline, two lines, panel with a smaller piece on it); detailed in the 2x2 section pattern.

## 201. Card type: bento
- One span-8 lead + span-4 on row one, three span-4 on row two; one panel height; detailed in the bento section pattern.

## 202. Card type: split card
- Text beside one panel; a filled split panel pads 48; wide panels allow terminal up to 560 and pipeline at 680+.

## 203. Card type: stat card
- A number and one line (e.g. "64%"); leave plain unless the ground shows something behind; a stat may cut its bars out of the UI or be filled with the effect.

## 204. Card type: integrations card
- Real tool icons in full colour on light tiles; at most five tiles in a card; the connecting app not placed last.

## 205. Card type: testimonial card
- A named quote with a face; quote cards stack, never carousel; name and role at 16/24 in ink.

## 206. Card type: pricing / plan card
- One featured plan; aligned rows across cards; lit edge only as the page's one effect; badge in quiet ink when the edge is lit.

## 207. Card type: tall cards
- Panel on top with 8px margin, lines below; fade 40px on short panels.

## 208. Card type: open card
- No box: words on the page ground, the panel below with four rounded corners; used when the panel holds UI on a light page.

## 209. Card type: object card
- Tech only: a real object as the panel's whole picture, mounted near view, turning, with pause.

# Part 10 — Typography pairing library

## 210. Type pairing system rules
- All faces are Google Fonts, loaded in one request with exact axes and `display=swap`.
- Headline weight: 400 or 500 on tech pages (software, tech, gaming; clamp 400 to 500, using each pairing's tech weight), 400 everywhere else. Text 400; 500 for buttons and labels. Sentence case.
- Display tracking given in em, clamped between -0.045 and 0; a separate tighter tracking at hero (XL) size.
- Scale is a multiplier on the display size (normalises optical size across faces); place pages always use scale 1 and stretch 100%.
- A "letters" axis (wght or wdth) enables a word/editorial hero moment; with a weight axis it lifts the weight by 200 (load up to 700). Static faces have none.
- Mono only on tech pages (or when asked), never on place pages; default mono JetBrains Mono 400 to 500 when a pairing has none.
- Fallback stacks: serif/slab display -> Georgia, serif; sans -> system-ui, sans-serif; mono -> ui-monospace, SFMono-Regular, Menlo, Consolas, monospace.
- Picking: the kind's suitability score (1 to 3) counts cubed (3 is 27x a 1); recently used faces are dimmed, not removed; when dealing three, avoid repeating a class.
- Place pages pick by trade group: serif for bakery, hotel, restaurant, wedding; plain sans for retail, workshop, studio, clinic, law, agency; soft sans for wellness, cafe.
- Suitability scores below: kinds tech / software / gaming / product / service on 1 to 3.

## 211. Type: Geist (neo-grotesk)
- Display Geist 400 to 600 (tech weight 500), stretch 100%, tracking -0.035em, XL -0.045em, scale 1, wght axis. Text Geist 400 to 600. Mono Geist Mono 400 to 500.
- Scores: tech 3, software 3, gaming 1, product 1, service 1. Moods: precise, technical, calm.
- Use for developer tools, AI, infrastructure, fintech: exact, plain and fast.

## 212. Type: Host Grotesk (neo-grotesk)
- Display Host Grotesk 400 to 600 (tech 500), stretch 100%, tracking -0.035, XL -0.04, scale 1, wght. Text Host Grotesk. Mono JetBrains Mono 400 to 500.
- Scores: tech 2, software 3, service 2, product 1. Moods: calm, precise.
- Use for software, studios, agencies wanting a quiet, exact page.

## 213. Type: Instrument Sans display (neo-grotesk)
- Display Instrument Sans 400 to 600, wdth 75 to 100 (tech 500), stretch 96%, tracking -0.028, XL -0.036, scale 1.04, wght. Text Instrument Sans (wdth 75 to 100). Mono DM Mono 400/500 static.
- Scores: tech 1, software 3, product 1, service 2. Moods: precise, friendly, calm.
- Use for design and productivity software, studios, modern agencies.

## 214. Type: Mona Sans (neo-grotesk)
- Display Mona Sans 400 to 600, wdth 75 to 125 (tech 500), stretch 104%, tracking -0.03, XL -0.04, scale 0.96, wdth axis. Text Mona Sans. Mono Geist Mono 400 to 500.
- Scores: tech 2, software 2, gaming 2, product 2. Moods: technical, bold, precise.
- Use for hardware, platforms, games studios: a little wide, firm, modern.

## 215. Type: Hanken Grotesk (neo-grotesk)
- Display Hanken Grotesk 400 to 600 (tech 400), stretch 100%, tracking -0.03, XL -0.038, scale 1, wght. Text Hanken Grotesk. Mono DM Mono 400/500.
- Scores: software 1, product 2, service 3. Moods: calm, trusted.
- Use for clinics, law, advice, agencies: friendly and trusted without a trace of tech.

## 216. Type: Schibsted Grotesk (neo-grotesk)
- Display Schibsted Grotesk 400 to 600 (tech 400), stretch 100%, tracking -0.035, XL -0.042, scale 0.98, wght. Text same. Mono JetBrains Mono.
- Scores: software 2, service 3, product 1. Moods: bold, trusted.
- Use for media, agencies, services wanting a sturdy editorial voice.

## 217. Type: Onest (neo-grotesk)
- Display Onest 400 to 600 (tech 400), stretch 100%, tracking -0.035, XL -0.04, scale 1, wght. Text Onest. Mono JetBrains Mono.
- Scores: software 2, service 2, product 1. Moods: calm, trusted.
- Use for software and services wanting an even, open, readable page.

## 218. Type: Funnel Display / Funnel Sans (neo-grotesk)
- Display Funnel Display 400 to 600 (tech 400), stretch 100%, tracking -0.03, XL -0.04, scale 0.98, wght. Text Funnel Sans 400 to 600. Mono DM Mono 400/500.
- Scores: software 3, product 1, gaming 1, service 1. Moods: friendly, bold.
- Use for consumer apps and products with a friendly, bright voice.

## 219. Type: Manrope (geometric)
- Display Manrope 400 to 600 (tech 500), stretch 100%, tracking -0.035, XL -0.045, scale 0.97, wght. Text Manrope. Mono JetBrains Mono.
- Scores: tech 2, software 2, product 1, service 1. Moods: precise, friendly.
- Use for fintech, data and AI products: clean geometric forms, open numbers.

## 220. Type: IBM Plex Sans (neo-grotesk)
- Display IBM Plex Sans 400 to 600, wdth 85 to 100 (tech 500), stretch 100%, tracking -0.025, XL -0.035, scale 0.98, wght. Text IBM Plex Sans. Mono IBM Plex Mono 400/500.
- Scores: tech 3, software 2, service 1. Moods: technical, trusted.
- Use for developer tools, security, data infrastructure: engineered and sober.

## 221. Type: Sora / Figtree (geometric)
- Display Sora 400 to 600 (tech 400), stretch 100%, tracking -0.035, XL -0.045, scale 0.9, wght. Text Figtree 400 to 600. Mono Martian Mono 400 to 500.
- Scores: tech 2, gaming 3, software 1. Moods: technical, bold.
- Use for games, web3-free fintech, hardware: a wide geometric face with a clear text partner.

## 222. Type: Archivo (wide)
- Display Archivo 400 to 600, wdth 62 to 125 (tech 500), stretch 110%, tracking -0.025, XL -0.035, scale 0.9, wdth axis. Text Archivo. Mono Martian Mono.
- Scores: product 3, tech 1, gaming 2, service 1. Moods: bold, technical.
- Use for hardware, vehicles, equipment, games: a broad, firm face.

## 223. Type: Anybody / Onest (wide)
- Display Anybody 400 to 600, wdth 50 to 150 (tech 400), stretch 115%, tracking -0.02, XL -0.03, scale 0.86, wdth axis. Text Onest 400 to 600. Mono Martian Mono.
- Scores: gaming 2 only. Moods: playful, bold.
- Use for game studios and esports: a wide energetic headline over a calm text face.

## 224. Type: Bricolage Grotesque / Figtree (soft grotesk)
- Display Bricolage Grotesque 400 to 600, opsz 12 to 96, wdth 75 to 100 (tech 400), stretch 96%, tracking -0.03, XL -0.04, scale 1, wght. Text Figtree. Mono DM Mono 400/500.
- Scores: software 1, product 3, service 1, gaming 1. Place group: soft. Moods: friendly, playful, warm.
- Use for consumer products and brands with character, studios, kitchens that sell online.

## 225. Type: Red Hat Display / Red Hat Text (neo-grotesk)
- Display Red Hat Display 400 to 600 (tech 500), stretch 100%, tracking -0.025, XL -0.035, scale 1, wght. Text Red Hat Text 400 to 600. Mono IBM Plex Mono 400/500.
- Scores: service 3, software 1, product 1. Moods: trusted, friendly.
- Use for trades, finance advice, health and schools: steady and approachable.

## 226. Type: Gabarito / Figtree (geometric)
- Display Gabarito 400 to 600 (tech 400), stretch 100%, tracking -0.03, XL -0.04, scale 0.98, wght. Text Figtree. Mono DM Mono.
- Scores: software 2, service 1, gaming 1. Place group: soft. Moods: friendly, playful.
- Use for consumer apps and casual games: round and friendly.

## 227. Type: Chivo (neo-grotesk)
- Display Chivo 400 to 600 (tech 400), stretch 100%, tracking -0.03, XL -0.04, scale 0.96, wght. Text Chivo. Mono Chivo Mono 400 to 500.
- Scores: tech 2, software 2. Moods: technical, calm.
- Use for developer and data tools: grotesk with a matching mono.

## 228. Type: Outfit (geometric)
- Display Outfit 400 to 600 (tech 400), stretch 100%, tracking -0.03, XL -0.04, scale 1, wght. Text Outfit. Mono DM Mono.
- Scores: software 2, product 1, gaming 1, service 1. Place group: soft. Moods: friendly, precise.
- Use for apps and consumer brands: clean geometric forms.

## 229. Type: Epilogue (neo-grotesk)
- Display Epilogue 400 to 600 (tech 400), stretch 100%, tracking -0.035, XL -0.045, scale 0.97, wght. Text Epilogue. Mono JetBrains Mono.
- Scores: tech 2, software 2, gaming 2, product 1. Moods: precise, bold.
- Use for platforms, tools, games studios: a sharp, slightly condensed grotesk.

## 230. Type: Familjen Grotesk (neo-grotesk)
- Display Familjen Grotesk 400 to 600 (tech 400), stretch 100%, tracking -0.03, XL -0.04, scale 1, wght. Text same. Mono IBM Plex Mono.
- Scores: tech 1, software 2, gaming 1, product 1. Moods: technical, calm.
- Use for software with an editorial edge, creative tools.

## 231. Type: Urbanist (geometric)
- Display Urbanist 400 to 600 (tech 500), stretch 100%, tracking -0.03, XL -0.04, scale 1, wght. Text Urbanist. Mono DM Mono.
- Scores: tech 1, software 2, gaming 1, product 1. Moods: friendly, precise.
- Use for apps, fintech, consumer software: soft geometric forms.

## 232. Type: Reddit Sans (neo-grotesk)
- Display Reddit Sans 400 to 600 (tech 500), stretch 100%, tracking -0.03, XL -0.04, scale 1, wght. Text same. Mono JetBrains Mono.
- Scores: tech 2, software 2, gaming 1. Moods: calm, precise.
- Use for platforms, communities, AI tools: open and even.

## 233. Type: SUSE (neo-grotesk)
- Display SUSE 400 to 600 (tech 500), stretch 100%, tracking -0.03, XL -0.04, scale 1, wght. Text SUSE. Mono JetBrains Mono.
- Scores: tech 2, software 1, gaming 1. Moods: technical, precise.
- Use for infrastructure, security, developer platforms: firm, slightly technical.

## 234. Type: Albert Sans (neo-grotesk)
- Display Albert Sans 400 to 600 (tech 500), stretch 100%, tracking -0.025, XL -0.035, scale 1, wght. Text Albert Sans. Mono DM Mono.
- Scores: service 2, product 2, software 1. Place group: plain. Moods: calm, refined.
- Use for shops, studios, small services: one quiet sans in two weights.

## 235. Type: Figtree (geometric)
- Display Figtree 400 to 600 (tech 500), stretch 100%, tracking -0.025, XL -0.035, scale 1, wght. Text Figtree. Mono DM Mono.
- Scores: software 1, product 2, service 2. Place group: plain. Moods: friendly, calm.
- Use for friendly shops, studios and services.

## 236. Type: Work Sans (neo-grotesk)
- Display Work Sans 400 to 600 (tech 500), stretch 100%, tracking -0.025, XL -0.035, scale 1, wght. Text Work Sans. No mono of its own.
- Scores: service 2, product 1. Place group: plain. Moods: calm, trusted.
- Use for bike shops, studios, trades: sturdy and plain.

## 237. Type: Rethink Sans (neo-grotesk)
- Display Rethink Sans 400 to 600 (tech 500), stretch 100%, tracking -0.025, XL -0.035, scale 1, wght. Text Rethink Sans. No mono.
- Scores: service 2, product 2. Place group: plain. Moods: calm, friendly.
- Use for florists, studios, small shops: soft and readable.

## 238. Type: Instrument Sans plain (neo-grotesk, place only)
- Display Instrument Sans 400 to 600, wdth 75 to 100 (tech 500), stretch 100%, tracking -0.02, XL -0.03, scale 1, no letters axis moment. Text Instrument Sans.
- No kind scores (place pages only). Place group: plain. Moods: calm, precise.
- Use for shops and studios that sell design and objects.

## 239. Type: Instrument Serif / Instrument Sans (serif)
- Display Instrument Serif, static single weight 400, stretch 100%, tracking -0.012, XL -0.016, scale 1.12, no axis. Text Instrument Sans 400 to 600, wdth 75 to 100.
- Scores: product 3, service 2. Moods: refined, calm, classic.
- Use for brands, studios, firms wanting a refined editorial voice.

## 240. Type: Fraunces / Figtree (serif)
- Display Fraunces 400 to 600, opsz 9 to 144, SOFT 0 to 100, WONK 0 to 1; set axes SOFT 30, WONK 0 (tech 400), stretch 100%, tracking -0.02, XL -0.028, scale 1, wght. Text Figtree.
- Scores: product 3, service 1. Place group: serif. Moods: warm, friendly, classic.
- Use for bakeries, roasters, food and homeware brands: a soft, warm serif.

## 241. Type: Newsreader / Hanken Grotesk (serif)
- Display Newsreader 400 to 600, opsz 6 to 72 (tech 400), stretch 100%, tracking -0.018, XL -0.025, scale 1.06, wght. Text Hanken Grotesk.
- Scores: service 3, product 1. Place group: serif. Moods: trusted, refined, calm.
- Use for bookshops, guesthouses, advisers, schools: a calm text serif.

## 242. Type: Source Serif 4 / Libre Franklin (serif)
- Display Source Serif 4 400 to 600, opsz 8 to 60 (tech 400), stretch 100%, tracking -0.02, XL -0.026, scale 1, wght. Text Libre Franklin 400 to 600.
- Scores: service 3. Place group: serif. Moods: trusted, classic.
- Use for law, finance, health, schools, bookshops: sober and readable.

## 243. Type: EB Garamond / Jost (serif)
- Display EB Garamond 400 to 600 (tech 400), stretch 100%, tracking -0.012, XL -0.018, scale 1.12, wght. Text Jost 400 to 600.
- Scores: product 2, service 1. Place group: serif. Moods: classic, refined, calm.
- Use for wine rooms, bookshops, old guesthouses, patisseries: classical and quiet.

## 244. Type: Literata / Figtree (serif)
- Display Literata 400 to 600, opsz 7 to 72 (tech 400), stretch 100%, tracking -0.02, XL -0.026, scale 1, wght. Text Figtree.
- Scores: service 2, product 1. Place group: serif. Moods: trusted, warm, calm.
- Use for bookshops, libraries, cafes with a reading corner: made for reading.

## 245. Type: Lora / Nunito Sans (serif)
- Display Lora 400 to 600 (tech 400), stretch 100%, tracking -0.015, XL -0.02, scale 1.02, wght. Text Nunito Sans 400 to 600.
- Scores: product 1, service 1. Place group: serif. Moods: warm, classic.
- Use for roasters, bakeries, delis: warm, brushed serif forms.

## 246. Type: Besley / Albert Sans (serif)
- Display Besley 400 to 600 (tech 400), stretch 100%, tracking -0.02, XL -0.026, scale 1, wght. Text Albert Sans.
- Scores: product 2, service 1. Place group: serif. Moods: warm, bold, classic.
- Use for cafes, bakeries, bars: a warm, slightly slab serif.

## 247. Type: Vollkorn / Work Sans (serif)
- Display Vollkorn 400 to 600 (tech 400), stretch 100%, tracking -0.015, XL -0.02, scale 1.04, wght. Text Work Sans.
- Scores: product 1, service 1. Place group: serif. Moods: warm, classic.
- Use for bakeries, delis, bookshops: dark, sturdy, bread-like serif.

## 248. Type: Zilla Slab / Rethink Sans (slab)
- Display Zilla Slab static 400, 500, 600 (tech 400), stretch 100%, tracking -0.018, XL -0.024, scale 1.02, no axis. Text Rethink Sans.
- Scores: product 2, service 2. Place group: serif. Moods: warm, trusted, bold.
- Use for workshops, bike shops, outfitters, trades: a friendly slab.

## 249. Type: Nunito (soft)
- Display Nunito 400 to 600 (tech 400), stretch 100%, tracking -0.02, XL -0.03, scale 1, wght. Text Nunito.
- Scores: product 1, service 1. Place group: soft. Moods: friendly, warm.
- Use for cafes, bakeries, kids and wellbeing: rounded and easy.

# Part 11 — Palette library

## 250. Palette token roles and derivation
- Roles: bg (page ground), surface (one step for tiles, panels, inputs), ink (all type), muted (secondary lines), accent (the one colour: button/links), accentInk (text on accent), fields (full-section flat grounds with their own ink).
- Surface default when absent: ink mixed 5% into bg. Muted default: bg mixed 45% into ink.
- Muted must reach 4.6:1 on both bg and surface: step it 8% toward ink until it does, keeping its hue.
- Accent ink: keep the given ink if contrast with accent is at least 4.5:1, else choose the most readable of `#ffffff`, `#111111`, ink, bg.
- The one inverse band: a dark field of the palette (lightness under 0.4) on a light page, or a light field on a dark page; else the ink. Inverse ink = bg if contrast at least 7:1, else white/`#111111`; inverse surface = inverse ink mixed 7%; inverse muted = inverse ink at 38% into inverse bg, made readable.
- Inverse accent: the accent if contrast against inverse bg at least 3:1 and (inverse bg chroma under 0.03 or hue distance over 20 degrees), else inverse ink.
- Buttons and links use the accent when its contrast with bg is at least 2.2:1, else the ink.
- Dark-ground palettes are for tech pages (software, tech, gaming) only.
- Place pages use light, quiet grounds only: lightness at least 0.8 and RGB channel spread at most 0.12.
- Take palettes made for the trade first; take the next only when the first clashes with the client's own logo or photographs; avoid recently used palettes; justify the choice by what the ground and accent answer in the trade (room, material, goods), never an invented fact.
- Never violet or lavender in the page's own palette.

## 251. Palette: Sheet and biro
- Tags light-neutral, mono-accent. Trades: saas, devtool, fintech, law, clinic, retail.
- bg `#ffffff`, surface `#f4f4f4`, ink `#111111`, muted `#6b6b6b`, accent `#1a4be0`, accentInk `#ffffff`. Field `#111111` / ink `#ffffff`.
- White page, black type, one grey for secondary lines, pale grey step for tiles and inputs; footer may invert to black. Blue only for text links and the one button; nothing else tinted.

## 252. Palette: Frost and slate
- Tags light-neutral. Trades: clinic, wellness, saas, fintech, law, hardware.
- bg `#f7f9fa`, surface `#ecf0f2`, ink `#1f3038`, muted `#5d6b72`, accent `#0d7480`, accentInk `#ffffff`.
- Cool white plus one paler blue-grey step; type in dark slate, not black. Teal once per screen max: primary button or one small detail beside the product photo.

## 253. Palette: Rose grey, green
- Tags light-neutral. Trades: cafe, bakery, studio, wellness, wedding, retail.
- bg `#ebe5e3`, surface `#e1dad7`, ink `#2b2622`, muted `#6a615d`, accent `#0f7d45`, accentInk `#ffffff`.
- One rosy grey top to bottom, brown-black text, grey secondary lines; pictures keep the page's photo treatment (greyscale only if the page is black-and-white). Green only on the current-page link and one footer button.

## 254. Palette: Newsprint and brass
- Tags light-neutral. Trades: agency, studio, restaurant, workshop, law.
- bg `#e8e8e3`, surface `#dcdcd6`, ink `#181715`, muted `#63625c`, accent `#bfb21a`, accentInk `#181715`. Field `#181715` / `#e8e8e3`.
- Warm paper grey with near-black type above; whole sections flip to near-black with paper-grey type; no tinted sections. Brass yellow marks one small detail per screen (the button or a single word).

## 255. Palette: Stone and blueprint
- Tags light-neutral. Trades: workshop, hardware, agency, studio, devtool.
- bg `#dfdedb`, surface `#d3d2ce`, ink `#26251e`, muted `#5f5d55`, accent `#2456d6`, accentInk `#ffffff`.
- Stone paper, near-black and grey text. One image at a time printed in accent blue as its only ink; same blue fills the single button.

## 256. Palette: Navy on white
- Tags light-neutral, photographic-neutral. Trades: hotel, retail, consumer-product, clinic.
- bg `#ffffff`, surface `#f4f4f2`, ink `#1f2b4d`, muted `#6a7186`, accent `#f7941d`, accentInk `#1f2b4d`. Fields `#05070a` / `#ffffff`; `#e3e1dc` / `#1f2b4d`.
- White pages with navy type between full-bleed photographs, opening on near-black, closing on a warm grey footer. Tangerine is one small tab or button, never larger than a thumbnail.

## 257. Palette: Three stones
- Tags light-neutral, photographic-neutral. Trades: hotel, wellness, wedding, studio, law, clinic.
- bg `#eeecea`, surface `#e4e1dd`, ink `#333231`, muted `#6b6763`, accent `#5c6b54`, accentInk `#ffffff`. Field `#cdc3b6` / `#333231`.
- Three close stone tones: lightest page, middle panels, darkest a single band; charcoal type. Saturated colour left to photos and backdrops; grey-green fills the button only.

## 258. Palette: Putty and black
- Tags light-neutral, photographic-neutral. Trades: cafe, restaurant, workshop, studio, hardware, consumer-product.
- bg `#dedad3`, surface `#d3cec6`, ink `#0a0a0a`, muted `#5c5852`, accent `#256f82`, accentInk `#ffffff`.
- Warm putty page, pure black for all type and main shapes. Only tint is teal: one button or a single marker near photographs.

## 259. Palette: Sand and moss
- Tags light-neutral, earth. Trades: cafe, bakery, hotel, wellness, restaurant, consumer-product.
- bg `#ddd6c6`, surface `#d2cab8`, ink `#2a2a26`, muted `#59574e`, accent `#4f6238`, accentInk `#ffffff`. Field `#3f5a2a` / `#ffffff`.
- Sand grey with charcoal type; one deep leaf-green band may close the page. Moss green reserved for buttons; brighter greens/blues only through photos.

## 260. Palette: Bone, green, chocolate
- Tags light-neutral, earth. Trades: cafe, bakery, restaurant, hotel, retail.
- bg `#e5e1d8`, surface `#dad5ca`, ink `#2a1d17`, muted `#6b5b51`, accent `#456f3a`, accentInk `#ffffff`. Field `#456f3a` / `#ffffff`.
- Bone ground, chocolate-brown text. Green spent on one large flat block (about a third of a screen) and the button; other colour from photos.

## 261. Palette: Lunar and bronze
- Tags dark-neutral. Trades: hardware, ai, fintech, game.
- bg `#111111`, surface `#1c1c1c`, ink `#f2f2f2`, muted `#8f8f8f`, accent `#a08672`, accentInk `#111111`.
- Soft black, panels one step lighter, white text, grey secondary lines; photos supply all colour. Muted bronze on small markers and the one button only.

## 262. Palette: Night and sky blue
- Tags dark-neutral. Trades: ai, devtool, saas, fintech, game.
- bg `#0a0d14`, surface `#131824`, ink `#e9edf3`, muted `#8891a1`, accent `#5ab9fc`, accentInk `#0a0d14`.
- Blue-black ground, slate panels, silver-white text; no section changes colour. Sky blue marks buttons and links only.

## 263. Palette: Green-black and bone
- Tags dark-neutral, earth. Trades: ai, devtool, hardware, game.
- bg `#161c1a`, surface `#1f2725`, ink `#e3e2da`, muted `#8e948d`, accent `#9fc7b8`, accentInk `#161c1a`.
- Bone type on green-black throughout; panels and drawn details barely lighter than ground; photos supply colour. Pale jade for the booking/contact button alone.

## 264. Palette: Black and crimson
- Tags dark-neutral, mono-accent. Trades: game, hardware.
- bg `#0a0a0a`, surface `#151515`, ink `#efefef`, muted `#8c8c8c`, accent `#b11226`, accentInk `#ffffff`. Field `#efefef` / `#0a0a0a`.
- Black with off-white text and mid-grey texture over nearly the whole page; last sections may invert to off-white with black type. Deep crimson sparingly: a few characters in a heading, a slider fill, the one button.

## 265. Palette: Forest and lime
- Tags dark-neutral, earth. Trades: game, devtool, ai.
- bg `#0f1f10`, surface `#162a17`, ink `#ffffff`, muted `#9aa39a`, accent `#c6f19d`, accentInk `#0f1f10`. Fields `#000000` / `#ffffff`; `#ffffff` / `#0f1f10`.
- Forest green, black and white sections alternate, forest green holding the most; photos in moss greens and stone browns. Pale lime only on small squares (arrow buttons, closing wordmark).

## 266. Palette: Charcoal and sage
- Tags dark-neutral, photographic-neutral. Trades: hardware, ai, fintech.
- bg `#1c1c1c`, surface `#262626`, ink `#f1f1ef`, muted `#9a9b96`, accent `#8fa68e`, accentInk `#1c1c1c`. Field `#c8c5ba` / `#1c1c1c`.
- Charcoal with off-white text; one section may flip to pale concrete with dark text. Colour from photos; grey sage for the single button and a control's active state.

## 267. Palette: Warm black, gold
- Tags dark-neutral, photographic-neutral. Trades: game, hardware, fintech.
- bg `#0c0a08`, surface `#181512`, ink `#ffffff`, muted `#8f8a84`, accent `#c9a45a`, accentInk `#0c0a08`.
- Warm near-black, bright photos against it, pure white small type; panels warm to brown-black. Gold for one text link or small button per screen, never a field.

## 268. Palette: Graphite and orange
- Tags mono-accent, dark-neutral. Trades: hardware, devtool, game.
- bg `#18191b`, surface `#222427`, ink `#eff0f1`, muted `#9c9ea3`, accent `#ff4a1f`, accentInk `#18191b`. Field `#eff0f1` / `#18191b`.
- Graphite and cool light-grey sections alternate, graphite about two thirds; photos calm and low in colour. Safety orange marks the buttons, one thick solid bar across the top of the page, and the highlighted item in a list or chart.

## 269. Palette: Soot and lime
- Tags mono-accent, dark-neutral. Trades: devtool, ai, saas, game.
- bg `#0f0f0f`, surface `#1a1a1a`, ink `#ffffff`, muted `#8f8f8f`, accent `#dafa9c`, accentInk `#0f0f0f`. Fields `#ffffff` / `#0f0f0f`; `#dafa9c` / `#0f0f0f`.
- Soot-black opening and close bracket white middle sections, all black/white/grey. Pale lime is the single action colour: every button, and at most one headline set in it on dark.

## 270. Palette: Plum-black and pink
- Tags mono-accent, dark-neutral. Trades: game, ai.
- bg `#0d060b`, surface `#1b0e17`, ink `#ffffff`, muted `#9a8f97`, accent `#ff488b`, accentInk `#0d060b`. Fields `#470c35` / `#ffffff`; `#ffffff` / `#101421`.
- Near-black and plum top and bottom bracket a white middle with navy-black text. Hot pink only for primary buttons, chart bars and map markers; never fills a section.

## 271. Palette: Signal red, white
- Tags mono-accent. Trades: restaurant, retail, agency, consumer-product, hardware.
- bg `#ffffff`, surface `#f2f2f2`, ink `#0a0a0a`, muted `#6b6b6b`, accent `#d92b21`, accentInk `#ffffff`. Field `#000000` / `#ffffff`.
- White ground, black text, paper grey for filled panels, one full black band allowed. Signal red is the only colour: the button and a few solid blocks, never a word in a headline.

## 272. Palette: Greys and mint
- Tags mono-accent. Trades: saas, ai, fintech, consumer-product.
- bg `#ffffff`, surface `#f3f3f3`, ink `#232323`, muted `#6e6e6e`, accent `#a1ffcb`, accentInk `#232323`. Fields `#a1ffcb` / `#232323`; `#232323` / `#ffffff`.
- White, near-black and two greys on a board of flat tiles. Mint floods a few whole tiles (one statement, one figure, the closing call to action) and nowhere else.

## 273. Palette: Cool grey, cobalt
- Tags mono-accent. Trades: devtool, saas, ai, fintech, hardware.
- bg `#eef0f3`, surface `#e2e5ea`, ink `#0b0c0e`, muted `#5d6470`, accent `#1f2de6`, accentInk `#ffffff`. Field `#1f2de6` / `#ffffff`.
- Cool pale grey, near-black type, nothing else tinted. Cobalt starts as the button and one highlighted sentence, takes one whole section as a flat field with white text, then returns as a single button block.

## 274. Palette: Bottle ink, yellow
- Tags mono-accent. Trades: bakery, cafe, retail, consumer-product.
- bg `#f7f7f7`, surface `#ebebeb`, ink `#0d2a1c`, muted `#5f6b64`, accent `#f6e016`, accentInk `#0d2a1c`. Field `#f6e016` / `#0d2a1c`.
- Off-white with all type in near-black bottle green. Yellow the only saturated note: the button or one small object on most screens, plus one later section fully yellow.

## 275. Palette: Teal on paper
- Tags two-tone. Trades: clinic, law, wellness, fintech, saas.
- bg `#f7f9f8`, surface `#ebf0ee`, ink `#06525c`, muted `#2f737d`, accent `#06525c`, accentInk `#f7f9f8`. Field `#06525c` / `#f7f9f8`.
- Cool white paper and one teal for every word, shape and button; no black anywhere. Accent is the same teal filled solid for the button and one inverted band with paper-coloured type.

## 276. Palette: Navy and pink
- Tags two-tone, single-field. Trades: agency, game.
- bg `#1a2039`, surface `#212846`, ink `#f9a3c0`, muted `#b9879c`, accent `#f9a3c0`, accentInk `#1a2039`.
- One navy field for the entire page; pink does everything else (name, headings, body) and fills one solid button.

## 277. Palette: Blush and aubergine
- Tags two-tone. Trades: wedding, studio, agency, consumer-product.
- bg `#edccbe`, surface `#e8c2b2`, ink `#351a2b`, muted `#6c4857`, accent `#351a2b`, accentInk `#edccbe`. Field `#351a2b` / `#edccbe`.
- Blush and dark aubergine alternate as full fields and are each other's text colour, roughly equal shares. No third colour: the button is a solid block of whichever is not the ground.

## 278. Palette: Cobalt on sand
- Tags two-tone. Trades: bakery, cafe, studio, retail, agency, workshop.
- bg `#e6dbc7`, surface `#ddd0b9`, ink `#062b8a`, muted `#3a5aa8`, accent `#062b8a`, accentInk `#e6dbc7`.
- Sand paper and one cobalt do everything (text, drawings, solid shapes). Button is a cobalt block with sand type; no black or second hue.

## 279. Palette: Oxblood and grey
- Tags two-tone. Trades: restaurant, law, agency, retail, studio.
- bg `#e2e2e2`, surface `#d6d6d6`, ink `#7d0c14`, muted `#7a4a4e`, accent `#7d0c14`, accentInk `#e2e2e2`. Field `#7d0c14` / `#e2e2e2`.
- Deep red text on grey paper for most of the page, then pale grey text on a solid red field for one long section and the footer. Photos calm and low in colour; button a solid red block.

## 280. Palette: Olive on bone
- Tags two-tone, earth. Trades: restaurant, hotel, wellness, bakery, studio, law.
- bg `#ecebe7`, surface `#e1dfd9`, ink `#38450f`, muted `#5d683a`, accent `#38450f`, accentInk `#ecebe7`. Field `#38450f` / `#ecebe7`.
- Bone page, every word in one olive; footer inverts to solid olive with bone text. Photos supply all other colour; button the same olive, filled.

## 281. Palette: Burgundy and bubblegum
- Tags two-tone. Trades: agency, game.
- bg `#3d0012`, surface `#4d0519`, ink `#ff99d3`, muted `#c77aa0`, accent `#ff99d3`, accentInk `#3d0012`.
- Deep burgundy ground for the whole page, bubblegum pink for every word. Button and a control's active state solid pink with burgundy type; product photos supply other colour.

## 282. Palette: Bottle green, gold
- Tags two-tone, earth. Trades: restaurant, game.
- bg `#133621`, surface `#1a4429`, ink `#f4d96c`, muted `#b3a55e`, accent `#f4d96c`, accentInk `#133621`.
- Bottle green page, warm gold for all type, panels one step lighter. Button solid gold with green text; photos kept dark and warm.

## 283. Palette: Cobalt field
- Tags single-field. Trades: agency, game.
- bg `#0034eb`, surface `#002fd6`, ink `#ffffff`, muted `#dfe4f2`, accent `#e9e34a`, accentInk `#111111`.
- One electric cobalt fills everything with white and pale type; photos keep their colour and are shown large. A single yellow dot or button is the only other colour.

## 284. Palette: Mustard and black
- Tags single-field. Trades: agency, consumer-product.
- bg `#e1ac10`, surface `#cd9d0f`, ink `#0b0b0b`, muted `#4d3d0a`, accent `#24338f`, accentInk `#ffffff`.
- One warm mustard field with black ink only. Royal blue is the single interruption: a sliver along one edge or one small button.

## 285. Palette: Carmine field
- Tags single-field. Trades: agency, game.
- bg `#9c1220`, surface `#8a101c`, ink `#ffffff`, muted `#f0b9bd`, accent `#ffd9dc`, accentInk `#9c1220`. Field `#2a2a2a` / `#ffffff`.
- Deep red bookends or fills the page with white type and pale pink secondary lines; work shown between sits on flat charcoal to keep its colours. Button a pale pink block with red type.

## 286. Palette: Bubblegum and lime
- Tags single-field. Trades: consumer-product, agency.
- bg `#ff87ab`, surface `#ff739d`, ink `#0a0a0a`, muted `#6b1f3a`, accent `#def915`, accentInk `#0a0a0a`. Field `#0a0a0a` / `#ff87ab`.
- Flat bubblegum pink with black type throughout. Fluorescent lime for action only: menu button, one highlighter swipe behind a word, the main button.

## 287. Palette: Sky and navy
- Tags single-field. Trades: consumer-product, agency.
- bg `#6bb4ee`, surface `#7dbdf0`, ink `#0e1822`, muted `#1b3d5c`, accent `#ff5a1f`, accentInk `#0e1822`. Fields `#ffffff` / `#0e1822`; `#0e1822` / `#ffffff`.
- Sky blue behind everything, white cards on top, navy for all text and the footer. Orange for buttons and one highlighted word: orange against blue is the single clash.

## 288. Palette: Orange and black
- Tags single-field, two-tone. Trades: agency, consumer-product.
- bg `#ff7a1f`, surface `#ff8633`, ink `#050f16`, muted `#5a2306`, accent `#050f16`, accentInk `#ff7a1f`. Field `#ffffff` / `#050f16`.
- Hot orange is the page with blue-black type, flipping at a hard horizontal seam to a white section when content needs rest. Button a solid blue-black block with orange text; other colour from objects shown.

## 289. Palette: Tobacco and olive
- Tags single-field, earth. Trades: restaurant, game.
- bg `#472913`, surface `#55321a`, ink `#e4e0cf`, muted `#b39f84`, accent `#525e1b`, accentInk `#e4e0cf`. Fields `#c79a3e` / `#2b170a`; `#525e1b` / `#e4e0cf`.
- Tobacco brown with bone type; photos in browns and ochre. One olive block holds the main text or the button; a single ochre band may break the brown once.

## 290. Palette: Poster chapters
- Tags flat-loud. Trades: agency, game, consumer-product.
- bg `#e6e0d2`, surface `#dcd5c5`, ink `#1a1a1a`, muted `#5f5b52`, accent `#18bc42`, accentInk `#1a1a1a`. Fields `#ed4b44` / `#0f0f0f`; `#1a1a1a` / `#e6e0d2`; `#18bc42` / `#1a1a1a`; `#f2c21a` / `#1a1a1a`; `#e6e0d2` / `#1a1a1a`.
- Each chapter one flat field in turn (coral red, near-black, bone, green, yellow) with black or bone type, no tints between. Green doubles as the button accent on bone or black.

## 291. Palette: Blue, red, black
- Tags flat-loud. Trades: agency, devtool.
- bg `#ffffff`, surface `#f3f3f3`, ink `#0a0a0a`, muted `#6b6b6b`, accent `#1f30e0`, accentInk `#ffffff`. Fields `#1f30e0` / `#ffffff`; `#ff3b1f` / `#0a0a0a`; `#0a0a0a` / `#ffffff`; `#050a5c` / `#ffffff`.
- Three flat poster colours own whole sections (electric blue, red-orange, black), white for areas showing the product. No tints between; blue is the button on white.

## 292. Palette: Charcoal and primaries
- Tags flat-loud. Trades: game, agency.
- bg `#191919`, surface `#242424`, ink `#ffffff`, muted `#9a9a9a`, accent `#0c7866`, accentInk `#ffffff`. Fields `#d71e1e` / `#ffffff`; `#1e4bd7` / `#ffffff`; `#0c7866` / `#ffffff`; `#ffe927` / `#111111`.
- Charcoal ground with flat primaries on whole panels (red, blue, teal green, yellow), each against a different one. White type, black on yellow; teal green is the button on charcoal.

## 293. Palette: Ultramarine and yellow
- Tags flat-loud. Trades: agency, game.
- bg `#1423b8`, surface `#1220a6`, ink `#ffffff`, muted `#e4e2d6`, accent `#1fc27a`, accentInk `#0a0a0a`. Fields `#1423b8` / `#ffffff`; `#000000` / `#ffffff`; `#f7dd47` / `#000000`; `#e9479f` / `#000000`.
- Sections in sequence: ultramarine, black, yellow, ultramarine again; white type on blue/black, black on yellow. Green the only small accent, never larger than a button.

## 294. Palette: Candy chapters
- Tags flat-loud. Trades: consumer-product, game.
- bg `#ffd249`, surface `#f5c63c`, ink `#0a0a0a`, muted `#5e4a0a`, accent `#f53fd6`, accentInk `#0a0a0a`. Fields `#ffd249`, `#ffffff`, `#ffc4ef`, `#a4f6f8`, `#f9a21f` (all ink `#0a0a0a`).
- Each section one flat candy colour: yellow, white, pink, cyan, orange; all type black. Magenta for buttons alone.

## 295. Palette: Orange, sky, lime
- Tags flat-loud. Trades: consumer-product, agency.
- bg `#ff8126`, surface `#ff8d3a`, ink `#111111`, muted `#5c2a05`, accent `#de194b`, accentInk `#ffffff`. Fields `#ff8126` / `#111111`; `#4db3ff` / `#111111`; `#c5f53d` / `#111111`; `#161615` / `#f2f2f2`.
- Ground changes while reading: orange, then sky blue, then acid lime, one near-black band between; type black on all three. Crimson is one small button per field.

## 296. Palette: Post red, mustard
- Tags flat-loud. Trades: agency, restaurant.
- bg `#e2dccf`, surface `#d7d0c1`, ink `#2a1110`, muted `#6b524c`, accent `#4a6f84`, accentInk `#ffffff`. Fields `#dc1928` / `#ffffff`; `#952625` / `#ffffff`; `#e0a912` / `#2a1110`; `#4a6f84` / `#ffffff`; `#e2dccf` / `#2a1110`.
- Post red and bone alternate as full fields, red holding the opening and close. Mustard, slate blue and maroon for whole card frames; slate blue also fills the one button.

## 297. Palette: Grey, mint, orange
- Tags flat-loud. Trades: agency, saas.
- bg `#ffffff`, surface `#f5f5f5`, ink `#000000`, muted `#666666`, accent `#a7ff9c`, accentInk `#000000`. Fields `#c5c5c5` / `#000000`; `#a7ff9c` / `#000000`; `#ff6831` / `#000000`; `#000000` / `#ffffff`.
- Black on white to start, then sections flood with flat mid-grey, acid mint and orange in turn; photos inside keep the page's treatment. Mint is also the button on white and black.

## 298. Palette: Report blocks
- Tags flat-loud. Trades: agency, fintech.
- bg `#ffffff`, surface `#f6f6f6`, ink `#000000`, muted `#5f5f5f`, accent `#fe7141`, accentInk `#000000`. Fields `#fe7141` / `#000000`; `#d1ddd3` / `#000000`; `#f0ff1c` / `#000000`; `#000000` / `#f4f4f4`.
- White base with flat blocks of orange, sage, acid yellow and black on whole modules (figure tiles, quote panels, chapter bands). Black text on every colour, off-white on black; orange is also the button.

## 299. Palette: Card pastels
- Tags pastel-fields. Trades: agency, saas, consumer-product, studio.
- bg `#f7f7f5`, surface `#ebebe8`, ink `#000000`, muted `#666662`, accent `#d0106f`, accentInk `#ffffff`. Fields `#97cef6`, `#bbf697`, `#fed878`, `#6ef8fb` (all ink `#000000`).
- Neutral paper and black type; each card/tile gets its own flat pastel (sky, lime, amber, cyan), never two alike side by side. Magenta reserved for the logo, the email line and text links.

## 300. Palette: Mint and pink
- Tags pastel-fields. Trades: fintech, saas, bakery, retail.
- bg `#f8f8f8`, surface `#eeeeee`, ink `#0a0a0a`, muted `#6a6a6a`, accent `#1f6b3a`, accentInk `#ffffff`. Fields `#c3edce`, `#f8c7c9`, `#ffffff` (ink `#0a0a0a`).
- Near-white base, black type; mint and pink the only colours, each standing for one side of the product. First as small circles, then full-screen section fields; deep green only for the button.

## 301. Palette: Swapping pastels
- Tags pastel-fields. Trades: agency, studio, consumer-product, ai.
- bg `#c3d7e5`, surface `#d0e0eb`, ink `#141414`, muted `#4a5068`, accent `#0f5257`, accentInk `#ffffff`. Fields `#c3d7e5`, `#efd3da`, `#e6dccd`, `#cfd3cb`, `#f9cdbd` (ink `#141414`).
- One flat pastel is the whole background, swapping per project or chapter: pale sky, pink, sand, sage, peach. Type and one solid box stay near-black on all five; dark teal only for the button.

## 302. Palette: Blush, sage, slate
- Tags pastel-fields, earth. Trades: studio, wedding, agency, consumer-product.
- bg `#a6b3bc`, surface `#b2bdc5`, ink `#1c1c1c`, muted `#38424a`, accent `#2c3620`, accentInk `#e3e2da`. Fields `#a6b3bc` / `#1c1c1c`; `#b7c8be` / `#1c1c1c`; `#d6c4b8` / `#1c1c1c`; `#2c3620` / `#e3e2da`.
- Slate blue-grey, sage and blush as soft flat blocks, one per chapter or menu tile, dark type; one deep olive block anchors the close with pale type. Olive also the button; sea and sky photos do the rest.

## 303. Palette: Candy on black
- Tags pastel-fields. Trades: game, ai.
- bg `#000000`, surface `#0d0d0d`, ink `#ffffff`, muted `#999999`, accent `#93f1f7`, accentInk `#000000`. Fields `#9ae187`, `#93f1f7`, `#f3ea7a`, `#fbb65c`, `#b9e2ff` (ink `#000000`).
- Black ground and dark photos take nearly all the surface. Only flat colour: a solid block behind each title, a new candy pastel per project (mint, cyan, lemon, orange, sky); cyan default for the button.

## 304. Palette: Sky and sand
- Tags pastel-fields. Trades: consumer-product, agency, studio.
- bg `#cbe4f2`, surface `#bcdcee`, ink `#0a0a0a`, muted `#44606e`, accent `#b0298f`, accentInk `#ffffff`. Fields `#cbe4f2` / `#0a0a0a`; `#f1e3b5` / `#0a0a0a`; `#ffc013` / `#0a0a0a`; `#0a0a0a` / `#f2f2f2`.
- Sky blue and sand yellow as the constant ground, each holding whole sections, black text throughout. Saturated colour only as small solid objects; magenta for the contact card and its button.

## 305. Palette: Studio grey
- Tags photographic-neutral. Trades: hardware, consumer-product.
- bg `#a8a8aa`, surface `#b4b4b6`, ink `#0e0e0e`, muted `#3a3a3c`, accent `#1f5c49`, accentInk `#ffffff`. Field `#1b1b1c` / `#ffffff`.
- One mid grey as both page and studio backdrop, so the photographed object seems to stand on the page; black type, one black band late. Colour only from the product; racing green for the single button.

## 306. Palette: Walnut and tan
- Tags photographic-neutral, earth. Trades: hardware, game.
- bg `#2b2216`, surface `#382d1e`, ink `#e4e2da`, muted `#a39a8b`, accent `#bda38b`, accentInk `#2b2216`. Field `#bda38b` / `#1c150d`.
- Dark walnut opening and close with bone type; middle may turn flat tan around honey-lit photos. No bright accent: tan fills the one button on walnut.

## 307. Palette: Warm paper and walnut
- Tags light-neutral, earth. Trades: cafe, bakery, hotel, wedding, studio, retail.
- bg `#f7f3ec`, surface `#ede6da`, ink `#2a2622`, muted `#665e55`, accent `#7a4a2c`, accentInk `#ffffff`.
- Warm off-white, brown-black type, one darker paper step for the visit panel and goods cards. Walnut brown is the one button, the focus ring and the links; photos carry other colour.

## 308. Palette: Flour and terracotta
- Tags light-neutral, earth. Trades: bakery, cafe, restaurant, retail, workshop.
- bg `#f6f1e7`, surface `#ebe3d4`, ink `#2b241e`, muted `#6a5f54`, accent `#a3472b`, accentInk `#ffffff`.
- Flour-white ground, warm brown-black type, sand step for panels. Terracotta red is the main button and the brand band, never a second fill; photos of ovens, tiles and bread bring warmth.

## 309. Palette: Linen and harbour blue
- Tags light-neutral. Trades: hotel, wellness, wedding, cafe, clinic.
- bg `#f3f1ec`, surface `#e6e2d9`, ink `#1d2530`, muted `#5a6270`, accent `#2c5877`, accentInk `#ffffff`.
- Linen white, blue-black type, one greyer linen step for the booking form and room cards. Muted harbour blue is the one button and the brand band; nothing else tinted.

## 310. Palette: Limewash and ochre
- Tags light-neutral, earth. Trades: bakery, hotel, studio, workshop, restaurant.
- bg `#f4efe5`, surface `#e7dfcf`, ink `#29251e`, muted `#675e51`, accent `#8c6418`, accentInk `#ffffff`.
- Limewashed off-white, near-black brown type, straw step for panels. Ochre is the button and focus ring, darkened so its white label reads; ground stays quiet under warm photos.

## 311. Palette: Clay and pine
- Tags light-neutral, earth. Trades: wellness, hotel, cafe, workshop, studio.
- bg `#efe9e0`, surface `#e2d9cb`, ink `#22261f`, muted `#5f6158`, accent `#2e5b44`, accentInk `#ffffff`.
- Pale clay, green-black type, darker clay step for panels. Pine green is the one button and may fill the brand band at the close; wood, stone and plants in photos match it.

## 312. Palette: Chalk and tomato
- Tags light-neutral, mono-accent. Trades: restaurant, cafe, retail, bakery.
- bg `#f8f5ef`, surface `#ede7dc`, ink `#1f1b18`, muted `#645c54`, accent `#b8381f`, accentInk `#ffffff`.
- Chalk white, near-black type, one warm step for the menu panel. Tomato red is the order button and the brand band, nowhere else; the menu stays black type on the ground.

## 313. Palette: Plaster and rose
- Tags light-neutral. Trades: wedding, retail, bakery, wellness, studio.
- bg `#f6f0eb`, surface `#ebe0d9`, ink `#2c2325`, muted `#6a5d5e`, accent `#9a3c4c`, accentInk `#ffffff`.
- Pale plaster, warm near-black type, pinker plaster step for panels. Deep rose is the one button and the brand band; flowers and fabric in photos carry softer colour.

## 314. Palette: Steel and orange
- Tags light-neutral, mono-accent. Trades: workshop, hardware, retail, consumer-product.
- bg `#eeeeeb`, surface `#e1e1dd`, ink `#1c1d1f`, muted `#5c5e62`, accent `#c2501b`, accentInk `#ffffff`.
- Light steel grey, graphite type, one darker grey step for panels and price rows. Workshop orange is the one button and the focus ring; tools and bikes in photos bring their own colour.

# Part 12 — Copy and voice

## 315. Rule 1: the h1 names the category
- 2 to 8 words: the category (payroll app, dental clinic, standing desk) plus, for an unknown brand, the buyer or the place.
- A place: what and where in 40 characters max ("Bakery on Mill Street, Leith"; "Six-room guesthouse on a fjord").
- A game: its name and genre ("Kelpmoor, a co-op sailing game"), or its wordmark over an h1 naming the genre; the launch date or status is the hard fact.
- Never a riddle, a command, a mood, or a brand line sitting over a plain sub-line.

## 316. Rule 2: one hard fact on the first screen
- The first screen holds one hard fact: a number, a place, a price or a date.

## 317. Rule 3: every heading has a naming noun
- Every heading contains a noun that names a thing: the product, a part of it, the place, a section noun (prices, rooms, menu, opening hours, questions, getting here, visit) or a digit.
- One brand line per page at most, never the h1. It is the page's single figure of speech or pun, and it must have a fact in the line under it.

## 318. Rule 4: buttons are verb plus object
- 1 to 5 words: a verb and an object.
- Accepted lead verbs: book, buy, order, pre-order, reserve, try, start, get, download, compare, see, watch, read, find, join, subscribe, sign (sign up), contact, add, send, configure, request, call, email, message, visit, plan, check, apply, create, open, view, copy, shop, schedule, talk, chat, log, register, rent, hire, claim, ask, save, pay, upgrade, choose, pick, enquire, inquire, donate, install, wishlist.
- A bare noun only where the link opens that very thing.
- Literal even when the register is playful: the button says what happens next.

## 319. Rule 5: few actions, one wording each
- At most 2 actions in the hero (1 on a place page); at most 10 distinct button/link labels per page.
- The main action names the transaction (Book a room, Order a cake, Start a free trial). On a place: the order or booking action, else "Get directions"; never a side event.
- One screen shows the main action at most twice (desktop: nav button + hero button; phone: hero only; hide the sticky phone bar on a screen already showing it). A third copy on one screen is a failure.

## 320. Plain versions of vague lines
- Formula: category noun first, then one count, place or price, no figure of speech.
- "Every shift, sorted" -> "Shift planning for restaurant teams".
- "Where the city climbs" -> "Climbing gym with 180 routes in Leipzig-Plagwitz".
- "Come climb" -> "Day pass 14 €, shoes included".
- "A second read of every word" -> "AI proofreader for book publishers".

## 321. Hero sub-line
- Software, product, service: how it works plus the main benefit, 15 to 30 words, one line to two sentences; one fact or one mechanism, never a row of adjectives.
- A place: the fact, 80 characters max, with today's hours ("Sourdough, rye and cardamom buns from 7:30, Tuesday to Sunday."); a hotel gives the rooms and the town.

## 322. Section headings
- Name the thing ("Rooms and prices", "Works with your tools") or make a short plain claim ("Pays staff on the same day"); 1 to 6 words, max two lines.
- Allowed shapes: noun phrase; "we do X for Y"; verb with its object ("Send invoices from the van").
- Never: a bare command ("Get started", "Come climb"), a question (FAQ entries excepted), a colon heading, a line that only makes sense after reading the page ("Continuity slips", "It reads everything you decide").
- Heading with a grey second half = two sentences: first ends with a full stop before the muted span ("Rooms and prices. Breakfast included." with the second in muted grey); never two phrases running into one.

## 323. Card titles and body length
- Card title: a verb and an object ("Warns about double shifts"), one line, real words; never a coy label ("The market run").
- Under a heading: one line to two sentences, 10 to 40 words.
- Card body: 1 or 2 sentences, max 25 words, in the buyer's words with one concrete detail.
- No paragraph over five lines at 1440px.
- Let a price sell, not a mood heading ("Rooms from 140 € a night, breakfast included").
- Card length varies with the material: a card the facts know more about may run longer than its neighbours.

## 324. Words per screen
- Product page 47 words per screen, place 44, service 34; page total about 900 words max (footer excluded). Long copy goes to sub-pages.
- Tech word budget (software, gaming, hardware): 60 to 80 words per screen at 1440, counted outside UI mocks, diagrams and code (headings, lines, card titles/bodies, buttons, labels). Over 80 reads as wordy (a fintech page at 117 words/screen tested as wordy).
- Cut order when over: (1) a second sentence under a heading, (2) card bodies to one sentence of 12 to 18 words, (3) a fourth card, (4) a list that a UI fragment already shows. The UI says the rest.
- WARN over about 80 words a screen across the page, or a section over 90.

## 325. Numbers in copy
- Numbers sit in sentences with their unit ("4.5 hours a week"), uneven where real (212, 38%).
- A real claim that needs a source gets a numbered footnote near the footer (13px and up).
- Odd human numbers beat round big ones ("eleven people came to the first tasting", "45 seconds per side").
- Every number sits beside the claim it proves.

## 326. Pictures and live text
- Pictures stand beside short copy, never in place of it; words never stand where a photograph fits.
- Every word is live text.
- No caption, label or description under or on any visual: not "A drawing made in code", "Photographs follow", "Representative image", no name/price/link line under a bare picture, no hashtags. A heading names the set; a sold item's name and price sit inside its card's padding.

## 327. Form words
- A label says what goes in ("Arrival", "Guests"); never a question, never a placeholder in place of a label.
- An error names the field and what to type ("Write the day you want to come").
- The sent line names what was sent in the button's own words ("Your table request is in. We reply within a day.").

## 328. Naming
- Names are coined (not dictionary words, not an existing business) unless given. Never the names models keep coining (Kestrel, Halcyon, Lumen, Nimbus, Fieldnote and the default cast below).
- Search a coined name with its trade ("name coffee") and as a domain; if a business in that trade or a famous person has the exact name in the first 10 results, coin another.
- Person names only from the given facts.

## 329. Links and newsletter
- Links go where their label says (a page section or an existing page); never "here", never two labels to one target, never a link to a closed answer.
- Newsletter: asked once, in or just above the footer, "Subscribe" or "Sign up", email field only; never in a modal, never twice.

## 330. Self-check by reading aloud
- Read each line aloud to a customer: is it clear what the product does? If not, rewrite.

## 331. The fact sheet (before writing)
- Fields and where each goes:
- What it is: one plain sentence, no adjective -> h1 and sub-line.
- For whom / not for whom -> h1 or sub-line, one FAQ line.
- What they do today instead (spreadsheet, big rival, the bakery across town, nothing) -> pain line, comparison.
- The true difference, with proof -> claims worth a heading.
- Customer words (reviews, emails, quotes) -> pain line, headings.
- Numbers, each with source -> sentences, facts strip.
- People (given names, roles) -> about block, a quote.
- Odd true details (history, object, ritual, house word, the awkward bit) -> texture.
- A limit (what it does not do, who it is wrong for, what is closed) -> one admission per page.
- An enemy: a habit or category ("re-typing invoices"), never the reader -> pain line, one section.
- The offer (price, trial, booking terms, the one action) -> buttons, the close.
- An empty field stays empty: its section shrinks or goes.
- A thin brief is no reason to stop: write the best page the facts allow.
- When asking for copy input, ask at most six questions in one message, most useful first: who switched to you from what and why; the one number you would bet on; the objection you hear most; what you are bad at or not for; a strange true detail of how you work; three real customer messages.
- Limits and enemies come from the facts or plain facts of the trade ("closed Mondays", "Mac only", "no lift; rooms on three floors"); an invented flaw is still an invention.

## 332. The voice card
- Default voice is out unless requested: warm, wry, modest, slightly literary, deadpan-twist endings, calling itself honest/calm/quiet.
- Pick one register by buyer, price and the client's real character; when undecided, take the one least like the last page written.
- Card template: Voice (register); Pairs ("exact, not cold; sure, not loud; dry only in the empty state"); Person ("you" for what the buyer gets, "we" for the work; product is subject in feature lines); Sentences (mostly 8 to 16 words; one long one per section where it explains); Humour (none in hero, prices, FAQ); House words (the client's own nouns, same word every time); Never (virtue words about ourselves, a pun on the name, a strip of claims).
- Copy the client's own voice first (writing sample, old site, their wording); it overrides the register menu but never the five rules or integrity rules.
- Nine-trades test: picture the voice on nine businesses in nine other trades; if it suits any, push it further toward this client.
- Voice holds, tone moves: hero and story carry most voice; prices, FAQ, booking and forms go plain (readers are anxious); errors and confirmations short and kind.
- Registers never bend the h1/heading/button rules; voice lives in fact choice, sentence shape, the admission and microcopy.

## 333. Shape from the reader's questions
- Reader order: what is this, is it for me, why believe you, how does it work, what does it cost, what if it goes wrong, what do I do now.
- Awareness sets the start: unaware of the problem -> open sub-line on a moment they recognise; know the problem -> name it in customer words, then the product; comparing -> lead with the mechanism; know the client -> product, offer, price, action.
- A section exists only if there is true material for it; five full sections beat eight padded ones. On a place, the photographs set the section count.
- Counts follow content: four features = four cards, one quote = one quote, two plans = two plans; zero testimonials is normal.
- Find an organising idea (the menu as the page, a timetable, a founder's letter, one object carried through) and let it break the template once.
- Not the skeleton (eyebrow, claim heading, two-line lede, three cards, figures in every section). Vary contents: list, table, short letter, one longer paragraph (max five lines), a heading with one line under it.

## 334. Drafting rules
- Facts where adjectives want to go: "fast" is followed within the sentence by the figure or mechanism; remaining adjectives are physical or measurable (wood-fired, 58 mm, ground-floor).
- Proper nouns over categories: tools by name, the street, the river, the bus line.
- Mechanism in verb-led steps; how it works persuades more than how good it is.
- Pain in the customer's words before the product.
- One admission per page, said plainly.
- Proof beside its claim, from named outsiders.
- Risk reversal beside the button only when true ("Free for 14 days, no card").
- Microcopy carries voice: form labels and errors, sent message, empty states, 404, newsletter confirmation, cookie notice.
- Sentence length follows meaning: short lands a point, long carries an explanation; not every line punchy, not variety by rule.
- Repeat the product's name rather than cycling "the platform, the tool, the solution".

## 335. Register 0: the model's default (avoid)
- Warm, wry, modest, a little literary, mildly anti-big-company; paragraphs end on a deadpan twist; sincerity via honest, calm, quiet, actually; strip of figures, three polished quotes, footer pun.
- Use only when the client asks for it, and then within the device budget.
- Choose one register per client; borrow at most a single move from a second. None is the default; when undecided take the one least like the last page.

## 336. Register 1: facts only
- Sounds like: "Kessler Partners advises family firms on succession. Founded 1994, nine partners, offices in Basel and Freiburg."
- Moves: plain declaratives with names, dates, counts; third person or terse first person; exclusivity shown by a rule or fact, never an adjective.
- Fits: strong track record, professional services, B2B infrastructure, clubs, consultants.
- Fails when facts are weak: reads as an empty CV.

## 337. Register 2: technical and dry, with proof
- Sounds like: "Every pull request gets its own database, seeded from last night's backup. Branch in 4 seconds; delete it on merge."
- Moves: label paired with a hard figure; mechanism in verb-led steps; real commands, UI strings and file names on the page; the enemy is a category ("most preview setups"); jargon kept for experts or translated once; product as sentence subject.
- Fits: developer tools, infrastructure, APIs, technical software.
- Fails when it becomes a spec dump with no pain named, or abstractions ("power and alignment").

## 338. Register 3: the founder's letter
- Sounds like: "We ran a print shop for eleven years and lost a day a week to quotes. So we built the quoting tool we wanted, and now 300 shops use it."
- Moves: first person; a named habit or category as enemy; the reader's pain in their words; a deliberate refrain; an argument carried across sections within length limits; a plain human sign-off in the text (never the footer).
- Fits: products with a stance, small software companies, founder-led, against how things are done.
- Fails when the stance is put on or the founder has no real argument.

## 339. Register 4: self-aware and playful
- Sounds like: "Hot sauce from one farm in Kent. Medium is hot. Hot is a mistake you make once."
- Moves: straight face about a small product; joke in the sub-line or a card with the fact right under it; house words; microcopy in full voice; failures on display. Hype words stay out even ironically.
- Fits: drinks, snacks, small consumer goods, small studios, playful apps.
- Fails when jokes are random, aimed at the customer, or on a serious purchase (money, health).

## 340. Register 5: literary and formal
- Sounds like: "A balm for hands worn by cold water and rope. Citrus, cedar, a little smoke. 75 ml, 34 euro."
- Moves: exact, slightly raised vocabulary; "clients" not "customers"; sensory notes in tight lists; materials and botanicals by name; never an exclamation mark; the price plain on the button.
- Fits: skincare, fragrance, design objects, high-end retail.
- Fails when ornate without being exact ("a luxurious ritual of the senses").

## 341. Register 6: proper nouns and restraint
- Sounds like: "The old customs house above the harbour, built 1871. Eight rooms face the strait; the ferry to the island leaves below the terrace at 7:40."
- Moves: places, history, buildings, geography do the work; unhurried physical verbs (overlook, stroll, reside); no prices in the hero, no quotes; story in three sentences and a date. The word "luxury" never appears.
- Fits: luxury hotels, heritage houses, architecture practices, galleries.
- Fails when there is no real place or history to name.

## 342. Register 7: sensory facts, second person, present tense
- Sounds like: "You order at the counter beside the roaster. The cardamom buns come out at 8:00 and again at 11:00."
- Moves: what the reader will see, smell, hear or carry, each a literal fact (oven, hour, floor, weight); craft as a repeated step and a constraint; one defining absence ("no mirrors in the studio"); odd human numbers. Never a metaphor or mood paragraph.
- Fits: cafes, food, bars, fitness, yoga, spas, anything consumed with the body.
- Fails when every section turns sensory; prices and booking stay plain.

## 343. Register 8: historical scene
- Sounds like: "In 1958 the tram stopped outside, and the bakery opened at five for the drivers. It still does."
- Moves: opens on a dated moment, not the brand; streets, furniture and people named; old photographs as evidence, never captioned.
- Fits: restaurants, family firms, anything with real lineage.
- Fails when history is invented or generic ("rooted in tradition").

## 344. Register 9: plain-spoken activist
- Sounds like: "Every jacket we sell, we take back. In 2025 that was 3,140 jackets, and 2,200 went back on sale."
- Moves: mission in one measurable sentence; hard subject said plainly; admits its own harm; buttons that act on the mission; proof in numbers and reports.
- Fits: mission-led consumer brands, non-profits, firms with real impact figures.
- Fails when the mission is a paragraph of abstract nouns ("inspiring healthier communities").

## 345. Register 10: refusal and narrowness
- Sounds like: "We repair bicycles. Not e-bikes, not scooters. Bicycles, in two days, at the bench you can see from the street."
- Moves: positioned by what it will not do; scarcity as an honest limit; makers named when known; a ritual as community.
- Fits: makers, small batches, specialists, single-product companies.
- Fails when the refusal is invented to sound focused (and it spends the page's one negation run).

## 346. Register 11: the product as the hero
- Sounds like: "The X2 runs 140 minutes on a charge and climbs a 2 cm sill. It maps the flat on the first run."
- Moves: almost no "we"; product is the subject of every sentence; any turn of phrase is followed at once by a spec; one moment from life ("crumbs under the sofa at 22:00").
- Fits: hardware, physical products, apps with one strong feature.
- Fails when a play on words has no fact under it.

## 347. Register 12: hurried and conversational
- Sounds like: "Packaging for small food brands, by three people in one studio in Bristol (the one who answers the phone also draws the box)."
- Moves: talks to one busy person; asides in brackets; self-deprecation; casual section labels that still name the thing; permission to leave.
- Fits: small studios, freelancers, portfolios, founder-led direct-to-consumer brands.
- Fails when chummy ("We get it.") or jokes replace information.

## 348. Register-to-trade matching (starting points)
- Cafe, roastery, bakery: try 7 sensory, 8 historical, 4 playful; avoid 0 default.
- Developer tool, infrastructure: 2 technical-dry, 3 founder's letter; avoid 4 playful in the hero.
- Software for small businesses: 3 founder's letter, 11 product as hero; avoid abstract "power and alignment".
- AI product: 2 technical-dry, 11 product as hero; avoid "magic", "superpowers".
- Agency, studio: 1 facts only, 12 hurried, 4 playful; avoid stacked category nouns ("digital brand experience company").
- Portfolio: 12 hurried, 1 facts only; avoid a list of credits with no person in it.
- Luxury hotel: 6 restraint; avoid the word "luxury".
- Guesthouse, small hotel: 12 hurried, 7 sensory, 6 restraint; avoid "boutique", "curated experiences".
- Fitness, yoga: 7 sensory, 10 refusal; avoid "the best version of yourself".
- Architecture: 6 restraint, 1 facts only; avoid "spaces that inspire".
- Course, teaching: 3 as the teacher's letter, 7 sensory for a physical skill; avoid "transform your life".
- Skincare, beauty: 5 literary, 10 refusal; avoid "clean", "glow" with no ingredient.
- Finance: 1 facts only, 3 founder's letter; avoid jokes about money worries, unsourced savings.
- Hardware, appliances: 11 product as hero, 2 technical-dry; avoid adjectives where the spec should be.
- Game: the game's own world and tone, 12 for the studio; avoid the default register on the store page.
- Drinks, snacks: 4 playful, 9 activist; avoid 0 default.
- Repair shop, trade: 10 refusal, 1 facts only; avoid "passion", "quality you can trust".
- Wedding, events, photography: 7 sensory, 12 hurried; avoid "capturing your special day".

## 349. Move: hero forms that name the category
- Professional heroes are 2 to 9 words, one clause, never two stacked adjectives.
- Category and buyer: "Payroll app for restaurant teams" (software, unknown service).
- Category and place: "Bakery on Mill Street, Leith" (every place).
- Category and a true, unexpected promise: "Tax return app that asks eleven questions" (known category, real twist).
- Category and one striking customer: "Rota planner for the night shift at three hospitals" (customer is real and may be shown).
- Category and scope: "Card payments for market stalls" (infrastructure, B2B with real scope).
- Category, place and year: "Guesthouse on the lake shore since 1962" (year is real).
- A narrow superlative: "The only ferry to the island in winter" (provable, next line says how).
- Name and genre: "Kelpmoor, a co-op sailing game" (a game).

## 350. Move: non-h1 hero devices
- Greeting, reader's state of mind, question, imperative, enemy, twisted idiom, product news never take the h1; they may take the sub-line, a section's first line, the close, or the one brand line, each with a fact beside it.
- Reader's state: "Three hundred emails since Friday? The inbox sorts them by sender before you open it."
- Enemy/habit/category: "Most booking forms ask for your life story. Ours asks for two dates."
- Product news, plain: "New this spring: the 12-litre model, same price."

## 351. Move: section headings
- Default: name with a claim under it ("Rooms and prices" / "Six rooms, all with the lake on one side").
- Verb and the thing, where the reader acts: "Send invoices from the van", "Plan the week's shifts"; never a bare command.
- Plain claim with its noun: "Pays staff on the same day".
- A real figure: "212 routes, reset every Tuesday".
- Questions only in the FAQ; the line under the close's heading may ask once, plainly, if the register allows.

## 352. Move: about and story
- Start in a real moment, not a thesis (the day the oven arrived, the first market stall, the season the river flooded the cellar).
- Anecdotes, a timeline or questions, never value pillars ("Our values: quality, community, passion" is the weakest about page there is).
- Failure and luck belong in the plot when real (the first plan that failed, the landlord who said yes).
- Founders as people, not titles, and only real names.
- Values as behaviours with numbers ("We pay growers twice the market price"): a rule, not an adjective.
- End in a modest present tense, not a vision ("Eleven of us now, and the same oven.").
- Say how to reach them: the form, the street, the hours.
- Portfolio about: one line on what the person does (a deflating word welcome), what they make and for whom, one or two dated projects, one sentence of belief, availability as a plain date.

## 353. Move: features and how it works
- Mechanism in verb-led steps: "Forward the invoice. The app reads the total and the due date. It pays on the day you choose."
- Outcome first, feature as proof: "Nobody misses a shift change", then how the reminder works.
- A moment, not a use case: "Your drummer cancels at six; the stand-in gets the set list at 6:01."
- Real values in examples (times, sizes, amounts), never "customisable".
- The product doing the work: UI fragments with the client's own data, names, numbers; on tech pages the UI carries most words.
- Names are copy: rooms, plans, blends, models used the same way every time.
- Card: title (verb + object) and one or two sentences; length varies with material.

## 354. Move: proof
- Only real material: quotes word for word with name and role or town, figures with source, logos of real customers who may be shown.
- Let others say the superlatives, fully attributed.
- Rough beats polished: a real quote stays as written, lowercase and all.
- A rule instead of a claim: "Every frame is brazed by the person who measured you".
- None is fine: craft, luxury and small places often show no testimonials; photographs and facts carry the page.

## 355. Move: prices, FAQ, booking (the plain zone)
- Tone drops to facts; the reader is anxious here.
- Perks priced and literal: "Late checkout until 14:00 for 15 euro", "Bike hire 12 euro a day".
- Risk reversal beside the button only when true: "Cancel up to two days before, free".
- Admit limits in the FAQ: "Android comes next year; today it is iPhone only."
- Ask the buyer's real objection and answer flatly: "Can I take my data out? Yes: every table exports as CSV, any time."

## 356. Move: buttons and the close
- Verb and real object: "Book a room", "Order a cake", "Start a free trial".
- A low-pressure exit for browsers where the register fits: "See the rooms first".
- The close restates the hero's promise with one fact and repeats the main action word for word.

## 357. Move: microcopy
- Write all microcopy in the register; a stock form error under a hand-tuned hero gives the game away.
- Form error: "Mondays we are closed: choose a day from Tuesday to Sunday."
- Sent message: "Your table request is in. We answer before noon the next day." (real time)
- Empty state: "No notes yet. Your first meeting lands here when it ends."
- 404: "This page moved. The menu and the hours are one click up."
- Newsletter confirmation: "Subscribed. The next letter goes out on the first Sunday of the month." (real rhythm)
- Field hint: "Only for this booking." (only what is actually promised)

## 358. Move: the footer
- Facts only: legal row (brand, this year, Privacy, Terms, credits line), street and district, hours on a place.
- No sign-off, no pun on the name.

## 359. Move: numbers and humour
- Odd human numbers beat round big ones; every number in a sentence beside its claim.
- Humour points at ourselves, never the customer; lives in brackets, asides and microcopy, not at the end of every paragraph. None on a serious purchase (money, health) beyond microcopy.
- Rhythm on purpose, once: a run of short sentences painting a scene, a list ending on a surprise, one long sentence beside a short one.

# Part 13 — Icons

## 360. Real logos, never look-alikes
- A page that names a tool shows that tool's real logo in its own colours (a Google Docs file card carries the Google Docs icon; a Word file the Word file-type icon).
- Never draw a look-alike; never a letter in a circle or a generic page glyph where a real icon exists.
- Icons are fixed SVGs from the brand's own artwork, served with the page; nothing fetches, tints or judges an icon at runtime.

## 361. Icon sets and precedence
- Brand logos, full colour (about 1,500 brands; CC0): first choice.
- One-colour brand marks painted in the brand hex (Simple Icons, CC0): fallback only where no colour mark exists. Used for Google Docs, Sheets, Slides, Forms, Chat, Tasks, Calendly, Evernote, QuickBooks, Revolut, and console/game-store marks (PlayStation, Epic Games, Riot, Battle.net, itch.io, Roblox, EA, Ubisoft, Rockstar, Valve, CurseForge, Modrinth, GOG).
- File types in colour (VS Code icons, MIT): pdf, markdown, zip, Word, Excel, PowerPoint etc.; a document type, never a brand. 38 file types: pdf, docx, xlsx, pptx, gdoc, gsheet, gslides, txt, md, json, yaml, xml, html, css, js, ts, py, sql, zip, image, svg, video, audio, font, epub, psd, ai, figma-file, sketch-file, keynote, odt, ods, odp, eml, log, cert, db, default.
- Interface glyphs (Lucide, ISC): one line set only, never a second line set.
- Xbox and Nintendo have no permitted mark: name the console in type, never draw it. A game's store row is Steam, PlayStation and Epic Games.
- Google editors appear in their brand blue, green and yellow. Microsoft Office marks are not available: a Word/Excel/PowerPoint file card uses the file-type icon (docx, xlsx, pptx).
- Unverified-licence brand collections are not used.

## 362. Trademark use
- Nominative use only: name tools the product really works with, never imply endorsement.
- Footer carries "Product names and logos are trademarks of their owners"; keep a credits record per icon (file, set, source, licence, trademark flag, brand site).

## 363. Interface glyph style
- Lucide line style: 24x24 viewBox, fill none, stroke currentColor, stroke-width 2, round linecaps, round linejoins.
- A glyph is inline SVG and takes the text colour (muted variant = muted colour; accent variant = accent colour).

## 364. Choosing colour vs one-colour
- Brand or file type: the full-colour icon first; a one-colour mark only where listed.
- One-colour (mono) is better in a row of customer logos, footer social links, and where a brand has no colour version. A multi-tone mark in mono keeps its detail: paper-coloured parts are cut out of the silhouette, not filled solid.
- Black marks (GitHub, Apple, X) are flagged "ink": turned white on a dark ground.
- White marks (Notion) are flagged "paper": shown black on a light ground (inverted), as drawn on dark.
- Wordmark-only logos (Stripe, NVIDIA, Go) are flagged wide and get a wide tile.
- Light marks that vanish on a light tile are excluded (Wise, Klarna dropped).

## 365. The violet rule for logos
- "Never violet or lavender" governs the page's own palette, never a third-party logo; logos are not recoloured.
- Judge by share of coloured fills that are violet (deep navy is not violet).
- Half or more violet (Stripe, Twitch, Google Forms, Terraform, Datadog, ClickUp, Loom, Kotlin, C#, .NET, Bootstrap, ESLint): flagged; a tool the product really uses keeps its own colours explicitly; otherwise it prints in the text colour. A grey stand-in of a known logo is a fault. Mono only for a customer-logo row.
- Under half (Figma 20%, Google Drive 14%): printed as drawn; the real logo makes the page look official.

## 366. Icon sizes and shapes
- Sizes: 16, 20, 24, 28, 32, 36, 40, 48, 56px (default 24). Nothing animates.
- Marks are cropped to their measured drawing with 2% margin; file-type icons are not cropped.
- Shape classes by cropped proportion: wide over 1.8:1, landscape over 1.25:1, tall under 0.8:1 (Google Docs, Figma).
- Bare wordmark: height 0.7x the size, max width 4.5x the size, so a mixed row has even weight.
- In a tile: landscape mark sized to 70% of tile width (max height 80%); portrait mark to 68% of tile height (max width 80%); square mark at 60% of the tile.
- File cards, integration grids and "reads from" lists use real icons at 20 to 40px, never a grey box; a logo keeps its own proportions and colours.

## 367. Icon tile
- Default tile 40px; variants 24, 32, 40, 48, 56, 72px; radius = 0.28x tile; round variant 50%.
- Tile fill: white mixed 72% with the page background; 1px inset line border plus shadow 0 1px 2px ink at 7%.
- On dark grounds: a light tile (ink 94% into bg), no line, so every brand colour reads and black marks need no inversion.
- Wide tile for wordmarks: 2.4x tile width, mark about 1.7 tiles wide, max 80% width and 58% height.
- Flat tile: inset line only. Glyph tile: ink 5% into bg (9% on dark), no shadow. Accent tile: accent 12% into bg (22% on dark), glyph in accent. Ink tile: ink fill, bg-coloured glyph (on dark: ink 10% into bg with a line). Brand tile: accent fill, white mark (black marks inverted). Ghost tile (one-colour marks on dark brands): ink 6% over transparent plus inset line.

## 368. Icon chip, row, stack
- Chip: height 32px, padding 0 12px 0 8px, gap 8px, pill radius, card/surface fill, 1px inset line, 14px text, icon 18px. Large chip: 40px tall, padding 0 16px 0 10px, gap 10px, 16px text, icon 22px. Wordmark in chip 2.2x wide, max 0.9x height. Chip rows gap 8px. On dark, bare marks in chips get a light plate (3px padding, 7px radius).
- List row: gap 14px, padding 12px 0, 1px top border between rows; title 16px weight 500 line-height 1.3; meta 14px muted; trailing value 14px muted with 16px icon.
- Connection state: 6px dot plus word; on = green (`#2f9e5b` default) dot with ink text; off = muted dot.
- Avatar stack: tiles overlap by -10px, each with 2px bg-coloured ring; "+N" pill 40px (32px small), ink 8% fill, muted 13px weight 500.

## 369. Integration grid and logo wall
- Grid: auto-fill columns min 168px, gap 16px; cell padding 20px, gap 14px, radius 12px, card fill, 1px inset line; name 16px weight 500; meta 14px muted.
- Mosaic: one outline, cells divided by 1px hairlines (gap 1px over line colour), outer radius 20px; cell hover ink 3% tint.
- Logo wall: tiles only, no names; 64px tiles, auto-fill min 64px, gap 12px; wide tiles span 2 columns.
- Fixed column grids: 2 cols; 3 or 4 cols from 640px, falling back to 2 under 640px.

## 370. File card
- Row card: gap 14px, padding 14px 16px, radius 12px, card fill, inset line; icon 36px (wordmark 1.9x wide, landscape 1.15x); name 16px weight 500; meta 14px muted. List gap 10px.
- Tile card: icon on top, name below, gap 12px, padding 18px, icon 40px (wordmark 2.1x).
- On dark: icon gets a light plate (4px padding, 10px radius).
- Under 480px: row titles wrap; 2-column file-tile grids collapse to 1 column with icon beside text.

## 371. Feature points with glyphs
- Point list gap 16px; each point: 36px tile with 18px glyph, gap 14px; title weight 500 line-height 1.3; text muted 14px, line-height 1.5, 2px top margin.

# Part 14 — Diagrams

## 372. When a diagram vs a UI fragment
- Diagram when the point is how things connect: tools it reads from, one input split into parallel jobs, many sources into one place, two systems in sync, steps in order, regions.
- UI fragment when the point is what the user sees or does (a drafted reply, a calendar, a dashboard). Never a diagram of a screen.

## 373. Diagram budget per page
- One diagram per section, two per page max on tech pages; product or service page: one, held still (no motion).
- A place page has none.
- Gaming: a diagram shows a system of the game (matchmaking, saves, stores), never in place of the game's own pictures.

## 374. Diagram sizes
- Card panel about 560 x 340; section about 1200 x 560. A flat drawing takes the next size up when it fits; size can be forced to band or card.
- Panel min height 264px (300px for vertical orientation), growing to what the nodes need.

## 375. Diagram layouts
- hub: a centre and its tools; with children a mind map; with radial shape a web.
- ring: logos or regions on an orbit.
- tree: one thing branching out.
- lanes: one input, a core, parallel lanes (three threads).
- fanin: many into one; bowtie: many into one and out to many.
- sync: two systems with records crossing.
- timeline: steps done in turn.
- grid: files into a pipeline.
- free: your own nodes at fractions of the box and listed edges (with separate compact positions for phone).
- Start from a preset, then rename every label, icon and number to the client's own.

## 376. Diagram labels
- A tool by its name (Gmail, Zendesk), a step by its result (Reply drafted, Label printed), a place by its city; 1 to 3 words.
- Real-looking numbers in meta (2,481; 14 ms).
- No jargon nodes ("Orchestration layer", "AI engine"): the core is called what the product calls it.
- Up to 8 spokes, up to 12 nodes in a card; crowded means it should be a list.
- No caption under the diagram; the card title says what it shows; alt text in the spec for screen readers.
- Tool marks in own colours, never a letter in a circle; a core without an icon is a pill with its name. A missing icon falls back to the name's first letter, which is not acceptable on a finished page.
- Violet-majority marks drawn in text colour; black marks take ink; wordmarks get a 2:1 slot and their tile becomes a pill.

## 377. Diagram motion
- One cycle of 2.5 to 4 s per diagram card (default 3.2 s); its own loop, repeating.
- Ripple program: each spoke/branch/route starts a beat after the previous (stagger 0.24 to 0.5 s), fitted to one cycle, lines fading in the rest.
- Below the hero, two loops never share a screen: beside a looping fragment one of the two holds still.
- Restarts from first beat on pointer enter (mouse, pen) or keyboard focus in.
- Runs only on screen. On phone (under 640px) and under reduced motion it holds one still frame: the busiest moment. A loop that runs gets a pause control.
- The light: gradient comet with a glow and a bright head (or head-only dot). Accent appears only as the light and what it reaches; lines are hairlines; the core is an ink tile. The card never moves; nothing starts on scroll.
- Hover steps back fast (220ms); light fades off a node slowly (900ms); hit state 160ms.

## 378. Diagram grounds and lines
- Grounds by default: rings round a hub; none under an orbit, timeline or sync; dots for flows; the diagram leading a section adds glow.
- Product/service still diagram: ground none, pulse none; pattern, glow and pulses are tech only.
- Hub spokes are straight rays from the core's rim (variants: curve, elbow, swirl); flows bend in rounded elbows.
- Line width 1.25px; line colour ink at 18%; faint ink 10%; border ink 11%; dot grid ink 15% (13% on dark), dot radius 0.9px.
- Idle edge: faint, dashed 2 4. Spoke track: dashed 1 4.5.
- Comet stroke = line width + 1px; glow stroke 9px at 0.26 opacity (0.34 dark); core halo 0.08 opacity (0.13 dark); glow ground strength 15% (20% dark).
- Easing `cubic-bezier(.2,.7,.2,1)`.

## 379. Diagram nodes
- Base font 500 13px/1.25 text face; meta 400 12px mono, muted; sub-lines 12px weight 400 muted; captions 12px/16px weight 450 muted (ink when hit or done), caption sub 11px/14px mono.
- Node fill: one step lighter than the card on dark, white on light; 1px border; radius = small radius (8px) + 2px; shadow 0 1px 2px black 5% plus 0 8px 18px -12px black 22%.
- Hit state: border accent 55% mix, 3px accent ring at 14%.
- Icon slot 18px.
- Pill node: 32px tall, padding 0 12px 0 8px (tight: 0 9px 0 7px, gap 6px).
- Card node (sections, 900px and wider): padding 7px 14px 7px 7px, gap 10px, radius +4px; 32px logo box with 18px icon.
- Tile node 40px (icon 20px); disc node (orbit) 44px round (icon 22px).
- Core node: 56px, radius +8px, icon 26px, ink gradient tile (or accent tone); name inside under the icon, wrapping in two balanced lines at 148px max, 12px weight 560; core pill 42px tall, 14px weight 560, icon 20px.
- Done state: 15px status ring (1.25px ink 22% hairline) fills with accent and a 10px check; on icon tiles a 15px corner check badge offset -5px.

## 380. Diagram preset: hub-tools
- Types: software, product, service. Layout hub.
- Core "Agent" (bot glyph); spokes Gmail, Slack, Notion, Google Drive, Salesforce, Zendesk.
- Alt: the agent connects those six tools.

## 381. Diagram preset: hub-branches
- Types: software, tech. Hub with children (mind map).
- Core "Search" (search glyph). Drive -> Q3 plan (Google Docs), Budget (Google Sheets); Notion -> Roadmap, Onboarding (file-text glyph); GitHub -> api, web (git-branch glyph); Gmail -> Invoices (receipt glyph), Contract.pdf (pdf).

## 382. Diagram preset: hub-web
- Types: software, tech. Hub, radial shape.
- Core "Knowledge base" (layers glyph). Sales -> HubSpot, Salesforce; Support -> Zendesk, Intercom; Engineering -> GitHub, Linear; Finance -> QuickBooks, Xero.

## 383. Diagram preset: hub-stack
- Types: tech, software. Core "API" (server glyph); spokes Postgres, Redis, Kafka, Stripe, Sentry, Grafana.

## 384. Diagram preset: hub-stores
- Types: gaming. Core "Your game" (gamepad-2 glyph); spokes Steam, Epic Games, PlayStation, itch.io, Roblox.

## 385. Diagram preset: ring-apps
- Types: software, product. Core "Workspace" (layers); ring of 8: Gmail, Slack, Google Drive, Notion, HubSpot, GitHub, Zoom, Google Calendar.

## 386. Diagram preset: ring-regions
- Types: software, tech, gaming. Core "Edge" (globe); ring of map-pin regions with latency: Frankfurt 8 ms, London 11 ms, Virginia 14 ms, São Paulo 21 ms, Sydney 19 ms, Tokyo 12 ms.

## 387. Diagram preset: ring-edge
- Types: tech, software. Core "Platform" (layers); ring Cloudflare, AWS, Vercel, Docker, Kubernetes, Postgres.

## 388. Diagram preset: ring-servers
- Types: gaming, tech. Core "Servers" (server); ring with ping: Frankfurt 18 ms, Virginia 24 ms, Tokyo 21 ms, São Paulo 32 ms, Sydney 29 ms, Dubai 26 ms.

## 389. Diagram preset: tree-orders
- Types: product, service, software. Root "Order 4821" (Shopify).
- Payment (credit-card) -> Card charged, Receipt sent (done); Stock (package) -> 2 items reserved (done); Shipping (truck) -> Label printed, Courier booked (done).

## 390. Diagram preset: tree-release
- Types: tech, software. Root "Pull request 482" (GitHub).
- Build (container) -> Lint, 212 tests (done); Preview (Vercel) -> Deployed (done); Review (git-pull-request) -> Approved, Merged (done).

## 391. Diagram preset: lanes-agent
- Types: software, tech. Input "Support inbox" (Gmail, sub "support@") -> core "Agent" (bot) -> lanes: Reply drafted (pen-line, "Waits for you"), Ticket updated (Zendesk, "Zendesk #2210"), Lead added (Salesforce); all done.

## 392. Diagram preset: lanes-media
- Types: software, tech, gaming. Curved lines.
- Input "Upload" (video, 2.4 GB) -> core "Encoder" (cpu) -> 1080p (film, H.264), Thumbnails (image, 12), Captions (captions, EN DE) -> output "Published" (globe, done).

## 393. Diagram preset: lanes-deploy
- Types: software, tech, gaming. Curved.
- Input "git push" (GitHub, main) -> core "Build" (box) -> Frankfurt fra1, Virginia iad1, Tokyo hnd1 (server glyph, done).

## 394. Diagram preset: lanes-render
- Types: tech, gaming, software. Curved.
- Input "Render job" (file-code, 4,800 frames) -> core "Scheduler" (cpu) -> GPU 0, GPU 1, GPU 2 (microchip, 1,600 frames each, done) -> output "Movie" (film, done).

## 395. Diagram preset: lanes-matchmaking
- Types: gaming. Curved.
- Input "Queue" (gamepad-2, 12,480 waiting) -> core "Matchmaker" (swords) -> Europe 8 ms, North America 14 ms, Asia 12 ms (server, done) -> output "Match start" (play, done).

## 396. Diagram preset: fanin-warehouse
- Types: software, tech, service.
- Sources: Shopify (Orders), PayPal (Payments), Postgres (App data), Google Ads (Spend), HubSpot (Contacts), Zendesk (Tickets) -> target "Warehouse" (database) -> then "Dashboard" (chart-column, live).

## 397. Diagram preset: fanin-telemetry
- Types: tech, software.
- Sources: Prometheus (Metrics), OpenTelemetry (Traces), Sentry (Errors), Docker (Logs) -> "Collector" (database) -> "Alerts" (bell-ring, 3 open).

## 398. Diagram preset: bowtie-events
- Types: software, tech.
- Sources Shopify (Orders), PayPal (Payments), iOS app (smartphone, Sessions) -> core "Events" (zap) -> Mailchimp (Campaigns), HubSpot (Contacts), Snowflake (Warehouse), Intercom (Messages).

## 399. Diagram preset: bowtie-model
- Types: tech, software.
- Sources Google Docs (1,240 files), Slack (38 channels), GitHub (64 repos) -> core "Model" (brain) -> Answers (message-square, In chat), Summaries (file-text, Every Monday), Alerts (bell-ring, On a change).

## 400. Diagram preset: sync-crm
- Types: software, service.
- Left Postgres (prod): Contacts 2,481, Companies 312, Deals 96; link "Two-way" (refresh-cw); right HubSpot (CRM) with the same rows and counts.

## 401. Diagram preset: sync-saves
- Types: gaming.
- Left Console (gamepad-2, PS5): Saves 12, Trophies 48, Friends 63; link "Cloud save" (refresh-cw); right PC (monitor, Steam) with same rows.

## 402. Diagram preset: timeline-onboarding
- Types: software, product, service.
- Signed up 09:02 (user-plus), Email verified 09:03 (mail-check), Bank connected 09:10 (landmark), First invoice 09:24 (file-text), Paid 11:40 (banknote). Uneven, real-looking timestamps.

## 403. Diagram preset: timeline-season
- Types: gaming.
- Alpha March (flask-conical), Closed beta June (users), Early access September (rocket), Launch February (trophy), Season 1 April (swords).

## 404. Diagram preset: grid-documents
- Types: software, service. Group "Your files".
- Sources Google Docs, Word (docx), Excel (xlsx), PDF, Notion, Gmail -> stages Read (scan-text), Check (list-checks), Report (file-check, 3 notes).

## 405. Diagram preset: grid-assets
- Types: gaming, tech. Group "Your assets".
- Sources Blender, Photoshop, Audio, Video, Images, Fonts (file-type icons) -> Import (download), Compress (package), Build (box, 2.1 GB).

## 406. Diagram preset: free-approval
- Types: software, service, product. Free layout.
- Nodes: Request (file-text, €1,240) at 0.17,0.5 (phone 0.5,0.14); Manager (user) at 0.47,0.5 (phone 0.5,0.42); Approved (check, done) at 0.8,0.29 (phone 0.27,0.74); Rejected (x) at 0.8,0.71 (phone 0.73,0.74).
- Edges: Request->Manager straight; Manager->Approved elbow; Manager->Rejected elbow, idle (dashed, unused branch).

# Part 15 — Motion principles and tokens

## 407. The three layers of motion (every page)
- Give every page exactly three layers of motion and nothing else: (1) the hero's entrance on load, once; (2) one dealt "moment" in a section of its own (two on a long page of eight sections or more, never three); (3) the hover/press layer on every link, button, linked card and linked photograph, plus the swaps a click or tap makes.
- Treat a missing hover state, a missing hero entrance or a missing moment as a fault on every kind of page (a hovered card or button that shows no change loses points).
- On place, product or service pages make the moment photo- or type-led (photographs that change in place, a photograph that develops, a statement that lights up); keep shader/WebGL effects for tech, gaming and software only. A cafe, bakery, guesthouse or shop gets photographs, never a shader.
- On tech, gaming and software pages additionally allow: loops inside a card's visual (diagram pulses included), one timed loop in the hero or the one framed visual, one count, and the one effect and/or scene. Other pages get none of these: no ticker, marquee, slideshow, looping picture, pulsing dot or count.
- An "open now" line may be filled once at load; the panel must read correctly without it.
- A product render is a still by default; live only when explicitly asked, at most one live render, with a pause button in its corner, and a still on phones and under reduced motion.

## 408. Purpose of every motion
- Name each motion and its purpose in a few words before building ("hero entrance: the name arrives first, then what to do"; "photo chapters: three rooms shown in the space of one"; "hover: every link answers"). Cut any motion with no purpose.
- Make content complete and readable at rest, without script and under reduced motion; motion only ever adds to a page that is already whole.

## 409. Duration tokens
- Hover in: 150ms. Hover out: 120ms. Press: 90ms.
- Menu/panel opening: 200ms. Menu close: 120ms.
- Indicator travel (tab pill): 240ms.
- Image zoom in: 600ms; image zoom out: 400ms.
- Card lift: 180ms in, 120ms out.
- Field focus ring: 140ms.
- Loop cycle default: 3.2s (range 2.5–4s).
- Tech loop tokens: digit roll 700ms, count 1000ms (1.2s max), level bars 0.6s, bob 3.2s.
- Reveal inside a moment: 600–1,000ms. Photograph developing: 1.6–1.8s.

## 410. Easing curves
- Use one UI ease-out for every UI step: `cubic-bezier(.2,.8,.2,1)`.
- Use `cubic-bezier(.22,1,.36,1)` for an entrance settling (the hero, a moment, a digit roll, springs).
- Use `cubic-bezier(.65,0,.35,1)` only for travel (something moving from A to B).
- Use linear for loops and drifts.
- Never let a curve pass its mark: no bounce, no overshoot, anywhere.

## 411. Animatable properties
- Animate only transform, scale and opacity (a hover may also change colours). Never animate width, height, top, left, margin, padding, max-height.
- Inside a dealt moment only, a few more cheap properties may move, each named deliberately: clip-path (a wipe), filter (a photograph developing), the colour of words (a statement lighting up) and, on tech only, a background position (a photograph passing through type).
- Exception: a tab indicator may take the new tab's size at once (not tween width) — prefer scale-from-old-size to scale 1.

## 412. Motion distances
- Card lift: 2px. Photo zoom: 1.02–1.03. Arrow nudge: 3px. Menu drop: 6px. Button step: 1px up (2px on extra-large buttons; none on text-link secondary buttons). Press: 1px down and scale .985 (text-link secondary: scale only). Use no other distances.
- Phone sheet/menu: fades in with an 8px move.

## 413. Hover gating and input parity
- Run hover motion only for a fine pointer (`(hover: hover) and (pointer: fine)`); keyboard focus shows the same state on any device.
- Make every hover control also work by tap and keyboard, with a visible focus state.
- Never let a hover resize anything or push a neighbour. No rotate, skew, glow, shine sweep or chip glide.

## 414. Hover thresholds
- A linked card lifts 2px (more than 6px WARNs); a photo zooms 1.02-1.03 inside its frame (past 1.05 WARNs; a card growing past 1.03 WARNs).
- Every button, link, linked card and linked photograph visibly answers the pointer within 350ms; a linked card or photo with no change FAILs.
- Under reduced motion only colours change.

## 415. Buttons (hover/press)
- On hover, step the fill 14% toward the ink (an outline button gains a faint fill and a stronger border) and lift the box 1px (2px on XL).
- On press, sink it to 1px below rest and scale .985, so a hover state and a press state each show a move.
- Text-link secondary buttons (arrow/block looks) keep their underline and do not step; their press is scale .985 only.
- Timing: 150ms in, 120ms out, 90ms press. Never add a delay before a button reacts. Never a magnetic button.

## 416. Arrow glyph
- Move an inline arrow 3px right on hover and settle back (150/120ms). One arrow style per page.

## 417. Links and underlines
- Use one underline style, at regular weight. Running-text links rest on a faint 1px hairline; an ink line draws left-to-right on hover and leaves to the right.
- Nav and footer words rest bare, darken on hover and draw a 1px line 4px under the word.
- Timing 150/120ms. Never a second underline or indicator style.

## 418. Navigation and menus
- Nav words take the drawn underline; never a gliding pill on any kind of site.
- Open a mega/dropdown panel after 150ms of hover intent; fade it in with a 6px drop, all columns together as one surface (never column after column); close in 120ms. With one open, hovering the next word swaps it at once.
- Chevron turns 180° on tech; flips instantly on other kinds.
- Mark the current page with a 2px bar under its nav word, still.
- A menu curtain is a flat 40% dim — no glass, no blur.

## 419. Tabs (software only, click only)
- One indicator slides to the clicked tab by transform alone (takes the new tab's size at once, starts scaled to the old one and settles to scale 1), 240ms: an ink pill with its label in the ground colour.
- Swap the panel in 200ms at most; give every panel one fixed height.
- No tabs on non-software pages. Never timed (auto-advancing) tabs.

## 420. Cards on hover
- A card with a link lifts 2px, its border darkens a step, optional soft shadow only on hover (blur 24px, 10% ink at most); 180ms in, 120ms out.
- A card without a link does nothing.
- Never tilt, flip, scale, follow the pointer or glow at the cursor.

## 421. Photographs on hover
- A photograph inside a linked card or link scales 1.02–1.03 inside its frame (frame overflow hidden), 600ms in, 400ms out. The frame, card and boxes never grow.
- Never dim, fade or overlay a hovered photograph; on a place page a photograph never changes opacity.
- A product card's name underlines together with the image zoom.
- A photograph outside a link does nothing — so on a place page make every photograph that leads somewhere a link (a room to its booking, goods to their card) so the hover shows in every section.
- No tilt, rotation, or Ken Burns at rest.

## 422. Focus ring
- Draw a 2px ring in the action colour, offset 2px, drawn in full inside the frame where focus lands. No transition: a focus ring never animates.

## 423. Form fields
- Focus: the action-colour border plus a 3px soft ring, 140ms.

## 424. Switches and checkboxes (tech)
- Knob slides 16px and stretches 4px while pressed, by transform (180ms slide, 90ms press). The tick fades in while growing from 70% to full size (160ms). On other kinds they jump.

## 425. Copy button (tech)
- The glyph swaps to a check in place, holds 1.5–2s, then returns (150ms).

## 426. FAQ and accordions
- Show every FAQ answer open: no accordion. Nothing ever animates height, max-height or padding.

## 427. Hero entrance (every page)
- Once on load, the h1 rises line by line out of word masks: 700ms per line, lines 80ms apart, at most 240ms between first and last; each word starts wholly under its mask.
- Then everything after it in its column (lead, each button, facts) fades up 12px, 520ms each, 60ms apart, starting when the last line is halfway up. A line above the h1 (a notice, a pill) arrives with the first line.
- The hero picture is never hidden and never fades: a photograph settles from scale 1.05 to 1 over 1.1s inside its frame; a window, object or collage settles from .98 over 900ms, as one block (words inside a pictured menu card never step on their own). A panel the words sit on stands from first paint.
- Total about 1.1s, ease `cubic-bezier(.22,1,.36,1)`, transform/scale/opacity only, once per visit, never again on scroll.
- A headline that is already live/interactive (a live word, letters that answer the pointer, a picture inside the line) rises whole instead of line by line.
- Hide only the words, and only until the script takes over or a 700ms safety mark passes; if the script is later than that, fade the words in over 400ms and settle the picture by CSS alone. Without script, under reduced motion and in print, the hero stands as written.
- Never a loader, a gate, a delay before reading, a second entrance, a section heading that rises on every section, or an entrance that hides text a visitor could already be reading.
- A hero that holds a big scene with its own load motion uses the scene as its entrance.

## 428. Loops inside a card's visual (tech)
- One cycle is 2.5–4s (3.2s default), then repeat. Seed the loop on its finished picture and never show an empty window: rest 600ms on the finished picture before the first cycle (a hand-written CSS loop may start at once); hold the finished picture for the last 10–15% of each cycle; a reset dims and rewrites, never blanks.
- Pointer or keyboard focus entering its card restarts the loop from the top (not within its first 800ms). A paused loop stays paused. The card, its panel and the window never move: no zoom, tilt or camera pan inside the window.
- One subject per cycle (a pointer clicks, a status turns, a bar fills, a line is written): one change every 1–2s, each change 300ms or less. Several subjects: the next one each cycle. A changing label never shows two words at once.
- One fragment loop per card group; other fragments hold their finished picture and play only while the pointer rests on their card. A small diagram card's pulse is that card's loop, on the same cycle, restart and pause rules.
- Below the hero, never two loops on one screen: in a group with a pulsing diagram, hold the fragments still, or hold the diagram (it then plays under the pointer).
- Keep a 48px band clear in a looping visual for the pause button.

## 429. Life signs (inside the looping visual only)
- Spinner: 1s per turn, 12–16px, then a check.
- Live dot: 2.4s (the dot still, a ring grows and fades).
- Caret: 1s with a hard step, inside a field only.
- Level bars: 0.6s.
- No typing dots, no lone pulsing dot elsewhere, no block cursor after a headline.

## 430. Card stories (each in a box of fixed height)
- A prompt types at 12–20 characters/second and holds.
- An answer streams about one bubble per second.
- A notification enters at the top; the oldest leaves through the fade.
- A checklist ticks about once per second.
- A calendar's events fade in one by one.
- A pointer glides about 200px in 1s, presses (scale .96 at least, with a 28px ring) and holds.
- A speaker or avatar front item changes no more than every 3s. A chart stays still.

## 431. Tech motion budget
- One timed loop per page, in the hero or the one framed visual, in any form (a story, a reel, a lit border, a live ground, a turning object, a marquee); its life signs are part of it.
- One timed loop plus the one effect at most; with a live effect in the hero, no other timed loop runs. Never two self-moving things within one 900px-tall window; never two loops in one panel.
- Card loops (one per card group), diagram pulses (one per diagram card) and dealt moments are outside this count.

## 432. Counts (numbers that tick)
- One count per page (a hero count or the counter moment, never both): on load in the hero (1000ms, 1.2s max), or as a dealt counter moment in its own section.
- Only on open ground — never in a card, panel or framed visual. Reserve its width. Put the final figure in the markup; show it under reduced motion, without script and on phones.
- Never count a year, price or phone number. A live counter changes only its last one to three digits.

## 433. Load motion (tech)
- Besides the hero entrance, at most one load-once motion inside the framed visual (a visual assembling, 600–1200ms), settled by 1.5s. A click swap: 400–600ms. No gate, loader or intro.

## 434. Pause control
- Anything still moving 5s after it is seen gets one round pause button per panel: a solid 32px disc, 12px in from the bottom-right (in a card, beside its title), always shown or fading in on hover/focus, same size and place on every card, never over copy, never on a still.
- A click freezes the frame and swaps to a play glyph. Scroll-driven moments need none. (Objects use a 36px disc in the panel's bottom-right corner.)
- Required by WCAG 2.2.2 for every loop that runs on its own longer than about 5s; under reduced motion loops hold one state and the button is hidden.

## 435. Loop start/stop
- Start timed loops on load; never start, stop or resume them on scroll. An intersection observer only mounts lazily.
- A canvas may skip drawing off screen only on a clock from load, so no visible start shows on return. A hidden tab may pause everything.

## 436. Scroll behaviour
- Outside the dealt moment's section (and a tech page's big scene), nothing animates on scroll, on every kind: no card/row/tile reveal (fade, rise, stagger, mask wipe), no parallax or drift, no scroll-snap, scroll-tinted ground, progress line, scroll-spy marker or count-on-view.
- No text moving at another speed than the page; the page is never held or steered by script (no scroll-jacking, no smooth-scroll libraries); no animation library at all on non-tech pages.
- A moment may hold its own section with `position: sticky` while the page scrolls natively.
- A scroll moment is scrubbed to the scrollbar (runs back on the way up) and shows a finished state at both ends; an enter moment runs once (1.6–1.8s for a developing photograph).
- Moment text is live and visible without the motion (opacity 1, 4.5:1 contrast at every step).
- A moment section stays 1 or 2 screens tall (photo chapters: 3 or 4 live, about two thirds of a screen per chapter).
- A scroll moment never moves a card, a photograph (outside its own job), pricing, an FAQ, a quote block or the footer.
- Drive scroll moments with native scroll-linked animation timelines, or a passive scroll read written to a custom property once per frame, or (tech only) a scroll-trigger scoped to that section without its pin.

## 437. Scroll thresholds
- Under reduced motion everything rests and nothing stays hidden; anything animating in on scroll or still moving 1.5 s after appearing FAILs.
- No content hidden until a script reveals it (checked with reduced motion, with an observer that never fires after 4 s, and with scripts off).
- A section, card or frame drifting more than 4px off the scroll on a non-tech page is parallax: FAIL.
- An IntersectionObserver only mounts, never starts or stops visible motion.
- No scroll listeners; no layout reads in move handlers.

## 438. Header and phone action bar
- The header and the phone action bar look the same at every scroll position.
- The phone bar comes up only once the hero's button has scrolled away, and steps down while the screen shows one of its actions (240ms; instant under reduced motion).

## 439. Reduced motion, no script, phones
- Under reduced motion: colours still change; menus fade; a press shows as a deeper tone instead of a move; tab indicator and switch knob jump to place; the tick appears at full size; the underline appears without travelling (transitions limited to opacity and colours).
- The hero stands as written. Every loop, effect, moment and scene shows its finished frame; marquees stand as a still (wrapped) row; numbers show final text; pause buttons are hidden.
- On a phone: card loops and effects hold their finished picture or poster; heavy canvases become stills; no hover states, no pointer simulations. The hero still enters, and phone-light moments run, so a phone page still moves in two places.

## 440. Video (tech only)
- Hero or framed visual only, as the effect or loop: muted, inline, poster first, a 6–12s loop or a story that plays once and holds its last frame, with a pause button; separate phone and desktop files.
- On other kinds: a still that opens the film on a click. Never autoplay video on non-tech pages. Never sound on entry.

# Part 16 — Moments

## 441. Moment budget and allocation
- One moment on a short page; two on a long page (eight sections or more), in two different sections; never three; each moment id at most once.
- Deal moments at random from the pool that fits the page kind and rotate through all eligible ones before repeating (never the same one twice in a row; the last three stay out). Never choose by taste.
- Place/product/service pages draw from photo chapters, pinned chapters (product, service), picture develops (film look) and statement lights up. Software/gaming/tech draw from every dealt moment except photo chapters and picture develops.
- On place/product/service with two moments: one statement moment plus one section moment (photographs), or picture-develops beside one chapters moment (one runs once on enter, the other follows the scroll).
- Photo chapters and pinned chapters never share a page: photo chapters tells a story in full-width photographs one chapter at a time; pinned chapters walks through steps listed beside one frame (how a booking or order goes).
- A place's short page (under 8 photographs) skips the type moment: its one moment is picture-develops on the section's photograph, or, with no photograph, statement-lights-up in a one-screen statement section (page totals four screens).
- On non-tech pages never use: anything with a shader, WebGL, liquid or pointer effect; anything that reads as a graphic trick (iris, line carrying colour, letters assembling, halftone develop, giant type with photo — a photo inside letters reads as a template trick, muddies a warm palette and is a parallax); a loop (marquee); a count.
- Never two of one kind (hover and liquid count as one pointer effect), never two of one slot, never two that avoid each other. A moment that needs a photograph only when the page has real photographs. A moment with nothing real to carry is re-dealt.
- A tech hero moment (0 or 1, never on a big-scene hero): liquid hover on split/photo heroes; cursor spotlight on product/collage/film/centred heroes; liquid type on a statement hero (headline of six words or fewer); none on others. Off on touch; rests under reduced motion. Two moments in total at most.
- A moment counts as one of a tech page's "beats" against the big scene.

## 442. Moment placement
- A moment sits on a hero, a statement, one section, a transition or the close — never in a card, a plan, a result or a bento cell. Nothing on a card moves on scroll.
- Statement moments are a section of their own with the h2 first; a marquee or counter row merges into the section above as its last row; a transition's host is the whole section on the new ground.
- Every section stays one or two screens tall, live and at rest, except the two chapters moments (photo chapters: hold+1 screens live, max four; both as tall as their content at rest).
- Moment text sits in the normal container: its words end on the page's left and right edges.
- A transition's cover is an inset panel inside the host section with an even gutter on every side and card corners (never touching section edges); its line or ring stays inside the panel; every heading, paragraph, button and picture appears whole, never cut by the line or disc.
- Never in the big scene's section or the one beside it.
- No moment in the place hero itself.
- Scroll moments open inside an inset panel with an even gutter and reveal each block whole; no word is cut mid-move.

## 443. Moment timing and behaviour
- Nothing blinks, bounces or overshoots. Settle ease `cubic-bezier(.22,1,.36,1)`; 600–1,000ms per reveal; 1.6–1.8s for a photograph developing.
- A scrubbed wipe or change takes about half of its chapter's share of the scroll and holds for the rest.
- Each transition and letters-assemble finishes before the section's top is a fifth of the screen down, so any screenshot shows one whole finished section.
- A loop runs its rounds and rests, or carries a pause button.
- Content readable without the motion: words in the markup, in their finished place; a moment never hides a headline on load.
- Photo-led moments on non-tech pages carry the client's own photographs (or vetted ones), each used once on the page, with real copy; never a stand-in picture just to give the moment something to move.
- No captions on moment photographs; credit goes in the footer line.
- Moments take the page's tokens (ground, ink, muted, accent, line, display face).

## 444. The still rule (every moment)
- Every moment has a static variant for phones and reduced motion, and a finished state without script or when its module fails.
- "Phone" = under 640px wide, or a touch screen turned sideways under 500px tall.
- Phone-light moments (one picture or one paragraph at a time; transform, clip, filter or colour; no WebGL) still run on phones: statement lights up, picture develops (film), photo chapters (from 600px viewport height). Every other moment shows its still on phones.
- Hover moments do nothing on touch screens.
- Decide the still state at mount; chapter moments re-check on resize.

## 445. Moment cost and pointer exclusivity
- No WebGL in any moment except liquid hover (tech only, one context, only near the screen, plain photograph when WebGL or the shader fails).
- Liquid type is one SVG filter on one headline, active only while a ripple is alive.
- Every other moment costs CSS variables, a transform or clip, and a passive listener.
- One pointer effect per page: a hover or liquid moment rules out a filled button effect, a card spotlight and an object that turns to the pointer, and vice versa.
- Never deal a moment that would push the page's live WebGL contexts over 4.

## 446. Photo chapters (place, product, service; scroll)
- Use for a short story in 3–5 photographs (the room, the kitchen, the workshop, a day of a tour), one chapter each (a number, a title and two lines), under one h2 and a short lead; all photographs of one place/product/job, none used elsewhere on the page.
- One photograph the width of the page's edges; each next photograph is uncovered over the last from its foot upward, settling from a slight zoom; a panel in the page ground at the photo's lower left changes to the chapter halfway through the wipe.
- About two thirds of a screen of scroll per chapter; the wipe takes under half of it, the photo holds the rest. Live height = hold + 1 screens: hold 2 for three chapters (3 screens), hold 3 for four or five (4 screens max). At rest as tall as its chapters, one screen at least.
- Runs at every width on screens 600px tall or more, phones held upright included (panel across the photo's foot). Under 600px tall: chapters stacked, each photograph over its words.
- Reduced motion: nothing pinned; chapters side by side, each photo over its title and lines (stacked on phones).
- Avoid with pinned chapters. No WebGL, no canvas.

## 447. Picture develops (place, product, service; enter, once)
- One large photograph with a clear subject, at least half the container wide (the section's subject, never a thumbnail — a small picture developing reads as a loading state).
- Film look (the only dealt look): it comes up out of the paper like a print in the developer tray — pale, flat and colourless first, darks arriving before light tones, then colour — while settling from a slight zoom. About 1.6s, once; transform plus a CSS filter, no canvas. Runs on phones.
- Print look (kept, never dealt): a two-tone halftone in ground and ink, darkest cells first, giving way to the photograph; cell 9px (range 6–14), about 1.8s, timed not scrubbed, one 2D canvas freed when done. Prints best on a clear subject against a plain field; an all-mid-tone picture becomes a blur of dots.
- Focus defaults to the centre (0.5, 0.5). Reduced motion: the photograph stands.
- Avoid with liquid hover and photo parallax.

## 448. Statement lights up / word highlight (every kind; scroll)
- One statement of 12–40 words, on its own ground or beside one picture: the one statement a page stands on.
- Rests at half ink (readable, about 4:1) and turns to ink word by word as it crosses the middle of the screen; one strong word turns to the accent instead. Runs back on the way up.
- Scrub range: first word turns when the statement's top is at 0.85 of screen height, last word when its bottom is at 0.45.
- Runs on phones (colour change only, no layout change, no pin). Reduced motion/no script: whole statement in ink, accent word in accent.
- Avoid with giant-type-pass.

## 449. Pinned chapters (tech, product, service; scroll)
- One feature section of 2–4 steps (3 default), a title and two lines each, one picture or screen per step.
- The section holds on screen for one screen of scroll (live section exactly two screens): the step in hand opens its two lines at the left; one frame at the right crossfades and settles to that step's picture. Each step gets a quarter to a half screen of scroll.
- Live only from 1024px wide on a screen at least 640px tall. Otherwise static: from 640px a row per step (text left, visual right, at most 30svh tall); below that each step stands with its 16:9 visual under it.
- Avoid with photo chapters, closing lift, line-carries-colour.

## 450. Counter rolls (tech; enter, once)
- 1–4 (2–4 typical) proof figures the brief actually gives (a price, a count, a time), each with a short caption; never an invented outcome ("98% satisfied").
- Digits roll once like an odometer when the row comes on screen; each strip starts and ends on the real digit, so at rest the row never reads as zeros; the right-most column turns most (one more turn per column).
- Duration 1400ms, stagger 90ms between figures. Whole numbers read best (tabular figures make a decimal point or comma as wide as a digit).
- Phones and reduced motion: the figures stand. Never in a card. One count per page.

## 451. Marquee row (tech; loop)
- One row of 6–14 real words (trades, cities, formats) moving slowly sideways in a loop, fading at both edges; pauses under the pointer, runs only on screen, carries a pause button.
- Speed 36px/s (range 16–80), gap 64px between items.
- Never logos (a logo never moves) and never invented clients. Reduced motion/phone: the words in a wrapped row. Weight lower than others (0.8).

## 452. Giant type, picture passing (tech; scroll)
- A statement of 2–4 words at 12vw, with one line under it; a photograph shows through the letters under a 35% ink tint and passes upward through the type as the section crosses the screen.
- Travel 60% of the picture's spare height; horizontal focus 50%; vertical centre 62% (the lower half shows).
- Photograph: mid-to-dark tones with detail; never a pale sky (reads lavender in a letter).
- Phone: photograph stands still in the letters, type at 19vw. Reduced motion: picture stands still in the letters.
- Avoid with statement lights up.

## 453. Letters assemble (tech; scroll)
- A statement of 2–5 words (up to about 28 letters), set very large, with one or two lines under it. Letters start scattered, shifted and turned and fly into the line one after another (first letters first) as the statement rises; whole before it reaches the middle of the screen.
- Spread 1 (range 0.4–1.6); scrub from statement top at 1.0 to 0.5 of the screen. Each letter's start is seeded so it scatters the same way every time.
- Phone/reduced motion: the statement as written (smaller on phone).
- Avoid with giant type, statement lights up, lines rise, counter rolls.

## 454. Line carries the colour (tech; transition, scroll)
- For a section on a new ground (inverse or surface) after a different one; one or two screens with its h2 first.
- The section keeps its new ground edge to edge; inside, an inset panel in the old ground (even gutter, card corners) is cleared by a one-pixel accent line climbing from its foot to its top: below the line the section's ground and words, above it the old ground. Each block fades in whole only once the line is above all of it — no word ever cut.
- The line starts at 0.45 of the section's rise.
- Phone/reduced: the section on its own ground, no panel, no line.
- Avoid with pinned chapters, closing lift, iris opens.

## 455. Iris opens (tech; transition, scroll)
- Same host conditions as the line transition. Inside an inset panel in the old ground, a disc opens in the middle of the visible area, widening with a hairline accent ring at its edge; each block stays hidden until the disc holds all of it, then fades in whole.
- Disc centre default (0.5, 0.5) of the visible part.
- Phone/reduced: the section on its own ground, no panel, no ring.
- Avoid with pinned chapters, closing lift, line carries colour.

## 456. Cursor spotlight (tech hero; pointer)
- A soft light on the hero's lit ground follows the pointer with a short lag and reveals a fine dot grid around it; drifts back to its rest spot when the pointer leaves.
- Rest position (0.72, 0.28); radius 420px; dot grid on. Pure CSS gradients driven by two custom properties, no canvas.
- Touch/reduced/no script: the light rests at its spot.
- Needs a hero frame on a lit ground holding the product. Avoid with liquid hover.

## 457. Liquid type (tech hero or statement; pointer)
- A very large headline of 2–6 words ripples and stretches like type seen through water where the pointer crosses it, settling back to crisp type within about a second.
- Strength 1 (0.3–1.6); ripple reach 0.3 of headline width (0.1–0.6). The distortion map drifts slightly with pointer position and time so the ripple flows rather than sits. One SVG filter, active only while moving.
- Touch/reduced: headline as written. Avoid with liquid hover and cursor spotlight.

## 458. Liquid hover (tech hero or section; hover; 1 WebGL context)
- The pointer pushes a photograph like water: the picture bends along the pointer's path with a wet shine (bright crest, shaded trough, lit from upper left) and a hair of colour split along the push; the ripple diffuses away in 1–2 seconds back to the plain picture.
- Strength 0.7 (0.1–1); brush radius 0.14 (0.05–0.3); decay 0.985 per 16.7ms (0.9–0.995), frame-rate independent. Use a small dead zone so no residue freezes a warp in the picture.
- Photograph: hard edges and detail (a coast, a building, a street); a flat sea or sky shows no ripple. Mid-to-dark tones; never violet or lavender.
- Phone/touch/reduced/no WebGL: the plain photograph, no canvas.
- Avoid with picture develops, cursor spotlight, photo parallax.

## 459. Retired moments (do not use)
- Headline arrives (word-by-word hero rise, 38ms apart): replaced by the universal hero entrance; a second headline motion is a second entrance.
- Lines rise (section heading rising line by line, 90ms apart): repeats the hero entrance.
- Closing lift (last section scrolls away like a sheet uncovering a closing photograph): needs its own closing section and puts words on a gradient over a photograph.
- Window parallax (wide photo moving slower than the page): a parallax reads as a template trick on every kind.
- Word rotate (one headline word changing every 2s, three rounds): duplicates a live-word hero.
- Magnetic button: removed entirely.

# Part 17 — Scenes

## 460. Who gets a big scene
- Tech pages only (software incl. AI, developer tools, fintech; tech incl. hardware and networks; gaming). Never on a place, service or plain product page: they get photographs.
- At most one per page, and only when the brief has what the scene needs (own photographs, own screen, own words; a game's key art and in-engine shots count as its photographs). No need met, no scene — never a stand-in for the client's pictures.
- Deal at random among scenes that fit the section, page type and brief, weighted, avoiding the last three used.
- A big scene is the page's one effect: no shader ground, no WebGL part beside it. Never pair with a moment it avoids or its "twin".
- The hero holds one screen at rest, so a scene can be the hero only if it rests in one screen; scenes resting in two screens go below the hero as a two-screen section with an h2.
- The rest of the page stays calm; one or two section moments allowed, never in the scene's section or the one beside it.
- Object scenes draw an object of the client's own trade only (a deck of cards for a card-game engine, a globe for an edge network); never an object of another trade.

## 461. Scene height and hold
- The scene section stays exactly one or two screens in the rhythm, words under the nav. Live it is hold + 1 screens; default hold 1 → two screens (1800px at 1440×900).
- At rest (phone, reduced motion, no script) keep the scene's rest height as a minimum height; never a fixed height (it would cut the composition or overrun the next section).
- A rest composition that fills under half its screen at 390px reads empty — fix it.

## 462. Scene rules
- Readable without it: the words are real text, in reading order; the finished composition says everything the scene says.
- Native scroll only: the stage sticks for the hold; nothing captures the wheel.
- Phones (under 768px) get the finished composition, except type scenes marked "light" (no depth, nothing overlapping).
- Reduced motion, no script, failed module: the finished composition (= the hold's end). Object scenes show the object's still and mount no WebGL.
- WebGL: one context at most per scene, from the page's shared budget of four, mounted only while live and within one screen of the viewport, destroyed on leave; a still under it whenever WebGL or the shader fails.
- Nothing moving crosses words being read; statements read whole at every rest.
- Text over a photograph stands on a flat band of the page ground or on the photo's calm dark part at 4.5:1 (3:1 for display text); never a scrim or gradient over a photograph.
- Cost: transform, opacity and clip-path on fixed-size layers; never width, height or an SVG clip repainted every frame.
- No captions explaining the scene; no card chrome, chips or labels flying with the scroll.

## 463. Descend through the weather (tech, gaming; below the hero; rest 2 screens)
- First screen sinks through a cloud deck onto the place below: a full-bleed photograph from above the weather behind a flat ground-colour band across the foot (name, one line, action); two cloud layers rise at different speeds; the band leaves as cloud reaches it; a wall of mist fills the frame for a breath while one short line rises through it; the frame clears from the bottom, under a cloud ceiling, onto the second photograph, where a two-line statement rises on a band at the foot.
- Cloud drawn once from layered noise in the page's own mist tint. No word straight on a photograph.
- Needs two photographs of the client's own site/world (one high or above cloud: a launch site, test range, data centre on its plain, a game world from above; one from below with a calm lower half); a one-word name, a sentence of 8–14 words, a 3–7-word cloud line, a two-line statement.
- Never: without own high/low pictures; a software page whose product is a screen; place pages; pasted stock clouds; as the hero. Weight 0.7.
- Avoid with fixed hero object, powers-of-ten, fly-into-shape, shaped window; avoid cursor spotlight moment.

## 464. Shaped window over a fixed world (tech, gaming; below the hero; rest 2 screens)
- One full-bleed photograph of the client's site stays still behind a shutter painted in the page ground; two tall level windows side by side show the site through a mullion under the title; scroll widens them outward, closes the bar into one window, holds a beat, then scales the shutter past the screen edges so the reader pushes into the place; a flat ground band rises across the foot carrying the chapter's one word, then lede and action.
- Shutter = five flat pieces moved by transform: no mask edge, no hairline, no word on the photograph.
- Needs one wide photo of the client's own site/world; a title of 3–7 words, one word of 6–12 letters, a lede of 18–32 words, one action.
- Never: screen-product software pages; place pages; two different pictures in the two windows; a word under 4 letters; as the hero. Weight 0.7.

## 465. Fixed hero object (tech, gaming; below the hero; rest 2 screens; 1 WebGL)
- One product stays on its own layer and turns with the scroll while the first chapters pass beneath: opens with title and action in the clear half, glides to the other side as each chapter's copy and spec list rise where it was; a chapter marked dark brings the inverse ground up behind it. The markup carries the object's still; the render draws over it only while live and near.
- Needs one object (a modelled object of the client's own kind, or the client's cut-out photograph); a title, one line, one action; 1–4 chapters of a heading, two lines and 3–6 spec rows.
- Never: a gauge, counter or frame readout under the object; copy over the object; a second moving ground; an object of another trade; a print effect on a product page; as the hero.

## 466. Powers-of-ten pull-back (software, tech; product section; rest 1 screen)
- Opens on the product's interface filling the whole screen; the camera pulls back at a steady rate (scale eased in log space so it never seems to stop) until the interface is the screen of a device on the page's lit ground; the device settles into its slot at the right; heading, copy and action arrive at the left.
- Needs the product UI at true size (16:10 screenshot or HTML); a label, heading, line, action.
- Never the hero (its first screen has no headline or action); never a stock room as the place; never a drawn device with a notch, keyboard or stand (a thin bezel is enough); never two devices.
- Phone: copy over the device, a 4:5 crop of the screen.

## 467. Product assembles into its action (software only; product section; rest 1 screen)
- The product's working screen builds itself in story order while held: opens on its first rows with its box only as tall as its content; each step slides the next part in from the foot, newest rows in the accent for a beat, the step's caption taking ink in the list beside it; then rows fold back into the one action (nearest first), the box closes round it and goes, and the action stands alone, larger, with its state beside it and one closing line centred under it. The action stays a real button.
- Needs the real screen as HTML in its finished state, parts tagged by step; 4–6 real user steps of 4–10 words each; the action labelled with the figure the screen built; a closing line of 4–8 words.
- Never: a screenshot cut into parts; a counter or progress bar; a heading that miscounts steps; beside the hero's product window; hardware/game pages.

## 468. Parts lock into the whole (software only; product section; rest 1 screen)
- Opens on one huge word alone (a year, a figure, a name); it steps back into its place in the product's interface while the panels fly in from the four edges and lock into one screen; 2–4 detail layers ink in one by one (data, comments, an agent's edit); the finished screen steps aside into a column at least 580px wide beside the heading and a short spec list (3–4 rows). No caption.
- Never: an illustration drawn for the page; a screenshot cut into tiles; a screen without meaningful parts; non-software pages.

## 469. Fly into the shape (software, tech, gaming; between/product; rest 1 screen)
- The brand's own mark, a clean clip of its true shape with the next chapter's photograph already inside and the chapter title on its face, rises to centre, turns to face you, and the camera flies into it — it grows about its inscribed circle until its edges rush past every screen side and the photograph fills the page; then a flat ground band rises across the foot with the title and first sentence. The title on the face grows with the mark, never faster.
- Clip is a CSS clip-path in page pixels, never an SVG clip repainted per frame.
- Needs the client's solid mark as one closed path in a 100×100 box (monogram, emblem, symbol — never a plain circle); one photo with a calm dark middle (no scrim/gradient/veil); a 2–6-word title on two lines and a 10–18-word sentence.
- Never: an extruded, bevelled or shaded mark; generic circle/square; a bright photograph; words on the photo outside the band. Weight 0.9.

## 470. Letter physics (software, tech, gaming; statement; rest 1 screen; phone light)
- A bold claim stands readable on the inverse ground, breathes in and flies apart in 3D in one short burst: each letter leaves along its own line from the centre with spin and a little gravity, middle letters rushing nearest the viewer, each gone before the screen edge cuts it. As the last letters leave, a one-sentence answer comes out of depth, whole, and lands at the claim's size on the page ground; an optional dark photo behind it comes up like a room's lights, dimmed to the ground under the words.
- Claim 12–36 characters (never over 40); answer 16–60 characters.
- Phone: letters fade and drift instead of flying in depth.
- Never: a glow or blurred type under the answer; calm or clinical briefs (reads loud); physical-product pages.

## 471. Dot becomes the full stop (software, tech, gaming; statement; rest 1 screen; phone light)
- One large dot drops onto the ground; the claim grows out of it to the left one whole word at a time, the first word right behind the drop; the dot steps right and a step smaller with each word until it is exactly the sentence's own full stop as the last word lands. Optional second beat: cut the ground to inverse in one step and set one supporting line under the claim.
- Needs a claim of 4–6 words ending in a full stop, in a display face whose full stop is a round dot; optional line of 8–16 words; the section after on the inverse ground if the cut is used.
- Phone: same stage, nothing overlapping, claim on two rows.
- Never an accent on the dot; never 7+ words; never right after another type scene. Weight 0.8.

## 472. Letter bar floods the ground (software, tech, gaming; between/statement; rest 1 screen)
- A 2–4-word statement stands on one line at display size with one straight-stemmed letter (l or I) at screen centre; the camera zooms on that letter until only its stem is left — a flat column of ink that widens to full bleed and becomes the next section's ground; the next statement (4–8 words + one line) arrives inside the column while the outgoing words' edges are still in frame.
- The stem is a solid column rasterised once at full size, never the glyph scaled up; the ground is one layer clipped by clip-path; the next section sits on the same ground, no seam.
- Never an accent on the column; never a stem letter with a curl, bar or serif; never a light section after it. No pictures. Weight 0.6.

## 473. Object through giant type (software, tech, gaming; statement; rest 1 screen; 1 WebGL)
- A short quote in huge capitals fills the held stage; one object falls down the wall: each line parts at its word gap and its halves open round the object's silhouette (wide enough never to cover a letter), then close behind it; each line turns from muted to full ink as the object reaches it. In the last line the object swells toward the camera, tips and falls away; the quote stands closed in ink with its credit.
- Quote 10–18 words in 3–5 lines of 9–13 characters with the gap near the middle; credit of 5 words max.
- Never: an archive or B/W photo as the object; a line over 13 characters; an eyebrow above the quote; an object of another trade; place pages.

# Part 18 — Effects

## 474. The effect gate
- Effects (shader, canvas, WebGL, print passes, scroll-driven drives, effect grounds, objects, scenes, tech moments, film/3D hero, timed loops) are for tech, software (incl. AI and developer tools) and gaming, and for a product page with a technical subject (hardware, devices).
- Never on a place, ordinary product brand or shop, service firm, agency or studio. There, photographs, type and flat colour carry the page.
- Banned on those pages: canvas and WebGL, autoplay video, any CSS gradient (grounds, panels, glows, scrims), SVG pattern or texture grounds, backdrop-filter (nav too), filter, blend modes, mask-image, glass, grain, halftone, dither, duotone, print, effect grounds, scenes, card loops, counts, SVG animation, GIFs, Lottie, custom cursors, any scroll or animation library.
- Allowed there: the hero entrance; one or two photo/type moments; a baked still street map; a plain photograph with copy; real icons; a still diagram (not on a place); on a physical product whose brief asks for 3D, its own product render (stills by default, live only on request, at most one live, on the flat ground, poster beneath).

## 475. Subject before effect
- An effect never stands where the product, the device or the game's world should be (a robot arm shown as a silk shader and an order form, or an unnamed game shown as an abstract effect, both lost to pages that showed the thing).
- Hardware with no photographs takes stand-in photographs of the same kind of machine at work; a game with no art sets its name large over stand-in photographs of its setting, full bleed in the world section.
- When a product render is the picture, the page's one effect may sit behind it as the stage ground (renders are transparent over their frame); it counts as the beat and shares the four contexts; it never replaces the picture or sits beside it as a second focal visual.
- Every visual that is not the effect, a card ground, a moment, the scene or a product render is a real UI capture or a real photograph. A photograph is never filtered, printed, dithered or graded on any page.

## 476. Tech effect budget and beats
- One effect: one live ground (the hero ground, or a ground inside the one framed visual window under an h2), or one WebGL part, or one object, or one big scene. A grain, dither or texture CSS ground counts as the effect.
- Never in a fixed layer, never behind body copy, never a page-long canvas; a 3D world lives in the hero only.
- Card grounds: one card group may hold quiet grounds from the effect's family, drawn once and held as pictures (contexts freed) — not a second live effect. With a big scene: no effect grounds outside a moment; card panels take the lit ground.
- Beats = the effect, the scene and the moments; up to three on tech. Never two in one section or in neighbouring sections; a calm section between them; the back third of the page calm before the close. CSS grounds, card grounds, diagrams, card loops and hovers are not beats.
- Two effect ids per page at most outside the moments; each panel its own seed. No echo of the effect in the close, no pattern panel, no focal tile.
- One pointer effect per page; never a replaced cursor, never a magnetic button.

## 477. Effect budget: hard caps
- Zero WebGL on non-tech kinds (except a product render the brief asks for); non-tech pages load no animation library.
- At most 4 live WebGL contexts per page (hard cap); more than 12 created over the scroll WARNs, 24 FAILs (on effect-led pages WARN above 8 created).
- One effect and at most one big scene; a second big scene, or an effect ground beside the big scene, FAILs.
- One effect id in more than two sections FAILs.
- A real-time 3D model stays near 2 MB compressed, with a poster; video ships separate phone and desktop files.

## 478. Quiet vs focal grounds
- Quiet grounds are an even field that holds UI (grain gradient, painterly landscape, gradient mesh, silk folds, fluted glass): a soft field behind UI, never a pattern. Use only quiet grounds for a slot carrying a big window.
- Focal grounds have a subject (orb sphere, spotlight cone, god rays, aurora curtains, caustics, prism, light leak, soft light bars, ASCII shade, dotted globe, ridgeline): alone in the hero, nothing over them except one compact UI piece — never a big window, a screenshot or text.
- When a slot holds UI (window, fragment, card group), exclude patterns and prints: ruled grounds, grid pulse, contour lines, dot terrain, dotted globe, ridgeline, halftone screen, Bayer dither, ASCII shade, line engraving, duotone grade.
- Behind a UI fragment use a soft lit field (painterly landscape, grain gradient, gradient mesh, silk folds), never a line, grid or dot pattern.

## 479. Effect dealing and pairing
- Deal effects at random per slot (hero, card group, band/closing CTA, footer), only from effects made for the page's palette kind (light, dark, colour) and slot; never the same id twice on a page; less likely to repeat recent ids or a second pick from an already-dealt family; never two that avoid each other.
- A visual on an inverse (dark) ground takes an effect made for dark palettes.
- If nothing fits a slot, drop the slot.
- "Named only" effects (never dealt, only placed when content calls for them): dotted globe (global reach: payments, infrastructure, logistics, networks), duotone grade (never on a client photograph), edge glow (the lit border of the one key object: prompt box or featured plan), ridgeline (a divider band).
- Seed each effect so its composition is fixed; without a seed it changes every load.

## 480. Where effects sit
- The effect sits in the hero (a hero frame holding a fade-bottom stage, or the hero's layer), or in the one framed visual under an h2 (window up to 1280×540 at 1440; 342×256 at 390), or in the scene's own section. One framed visual per page.
- A hero with an effect in a frame is a 5/7 or 6/6 split with the visual on the right, or moves the effect to its own section. An effect as the hero's layer (a game world, a focal ground) keeps the words on its calm part at 4.5:1.
- Split frame: a window placed at the corner, 56/56 in, cut by the right and bottom edges; a second piece (cursor dialog, notification) only over a window's lower-right edge, hidden from 1024–1279px and on phones. Text and UI never share a half.
- The lit ground (tech) goes to every ground that holds UI, so page, card, panel and UI are never four near-black layers.

## 481. Text over effects
- Only on the effect's quiet part at 4.5:1 or more. Set the effect's calm zone (calmX/calmY 0–1 of the frame) to where the text sits; the effect keeps that area quiet.
- A noise or fog ground never holds content.
- Put text and UI inside the effect element; the canvas sits beneath them.

## 482. Effect motion behaviour
- An effect reacts to the pointer or to time (only scenes and moments react to scroll); after assembling it holds — no constant churn.
- Ambient cycles 4s or longer; drift of a few px per second; 2–10% of pixels changing per 0.9s.
- Still at rest or with a pause button; poster first; still fallback under reduced motion, on phones and when WebGL fails. Pointer play off on touch. No sound on entry.
- One-shot transitions (a tile flip, a melt, a crack) only once, on a click or as a hero reveal, inside the framed visual.
- A glow only on a dark ground, once, behind the key object in the hero or framed visual, still, never spilling onto text or round a button.
- Ray marching only in a dark hero, at half resolution.
- Halftone and dither only as a still ground, never on a photograph.
- Blend modes only for a job inside the effect (a glint), never on text. No glass or frosted look on any kind.

## 483. Effect colour
- Every effect takes all its colours from the page palette (ground, surface, ink, muted, accent, accent-ink), mixed in OKLab/OKLCH. Never a fixed hue; never violet or lavender.
- Draw as ink (pale on dark pages, deep on light) or near the accent with labels at 4.5:1; match the card tone steps.
- Only three natural-colour exceptions: the meadow landscape (blue sky over grass), the gold horizon of dusk, and a map's water and parks (natural blue and green mixed into the land).
- Pass each surface only its own effect's parameters — one effect's numbers mean something else to another (contour lines' opacity 0.32 and calm 0.55 left dot terrain almost blank).

## 484. Grain gradient (family grain; quiet; slow; low cost; all palettes; hero/card/band/footer)
- Soft shapes in page colours drift slowly under fine film grain, like a printed texture.
- Defaults: speed 0.5 (0–2), softness 0.45, warp 0.6, grain 0.6, scatter 0.5, tint 0.5, contrast 0.55, calm 0.5, grain motion 1. Hold still (speed 0, grain motion 0) under any object or as a card ground.
- Use for feature-card panels, small shapes (chips, pills, bars: still grain, low contrast), a button fill (even, low contrast, moving only while pointed at), bar charts (still, low contrast).

## 485. Film light leak (grain; focal; slow; low; dark/colour; hero/card/band)
- Light bleeds in from one edge of a dark or coloured frame: blown-out core, soft fringe, fine moving film grain.
- Defaults: intensity 0.8, spread 0.45, halation 0.3, grain 0.04 (0–0.1), vignette 0.25, breathe 12s (6–20), warp 0.65, calm 0.5.

## 486. ASCII shade (dither; focal; slow; mid; all palettes; hero/card/footer)
- A slowly turning sphere (or cloud, or wave) made only of monospace characters, sparse dots to dense signs, reading as code.
- Defaults: cell 12px (9–20), speed 0.08 (0–0.5), scale 0.5, fill 0.5, accent 0.05 (≤0.2), calm 0.6. Never behind UI.

## 487. Bayer dither (dither; quiet; slow; low; all; hero/card/band/footer)
- A soft glow drawn in crisp square pixels with ordered dither, in two or three page colours.
- Defaults: speed 0.4, pixel 2 (1–8), tones 3 (2–3), intensity 0.9, spread 0.6, ramp 0.15, detail 0.4, scale 0.4, calm 0.55. A pattern: never behind UI.

## 488. Halftone screen (dither; quiet; slow; low; all; hero/band)
- A gradient field or big lit sphere printed as a rotated screen of round dots that grow in shadows, like a zoomed magazine print.
- Defaults: cell 10px (5–24), angle 30° (0–90), contrast 1.4 (0.6–3), size 1, drift 0.02, calm 0.5.
- Never in type, never in a chart area (its tone runs across the frame, emptying half the area), never on a photograph, never behind UI.

## 489. Line engraving (dither; quiet; still; low; all; hero/card/band)
- Fine parallel lines that swell in shadows and bend over rolling hills or around a big sphere, like banknote engraving.
- Defaults: pitch 6px (4–14), line width 0.1–0.9, angle 20°, bend 0.6 (0–1.5), cross-hatch 0.5, guilloche 0, calm 0.5. Never in type, never behind UI.

## 490. Aurora curtains (mesh; focal; slow; mid; dark/colour; hero/band/footer)
- Curtains of light folding in S-curves across a night sky, bright at the hem with soft glow below, fading upward in long rays, swaying slowly.
- Defaults: speed 0.05 (0–0.3), bands 3 (1–4), height 0.66, ray detail 0.6, waviness 0.55, intensity 1.3, stars 0.25, calm 0.6 at (0.3, 0.78).
- Allowed inside letters and digits on dark/colour pages, still.

## 491. Gradient mesh (mesh; quiet; slow; mid; all; hero/card/band)
- Soft islands of page colours blend over a slowly folding surface, lit where it folds; an optional thin mesh grid on top (lines 0–16, default 0).
- Defaults: speed 0.06, warp 0.65, relief 0.5, softness 0.55, angle −12°, tint 0.6, calm 0.4. A soft field behind UI.

## 492. Painterly landscape (mesh; quiet; slow; mid; all; hero/card)
- A soft, out-of-focus landscape painted in broad dabs: sky, hazy far hills, a near hill with a lit crest, to sit under a UI window.
- Defaults: horizon 0.45 (0.3–0.7), slope 14° (0–30), side 0 (−1–1), hill Y 0.12, blur 0.6, brush 0.6, grain 0.03, drift 0.02, calm 0.4 at (0.5, 0.55). Render at 0.6 resolution.
- Default ground for feature-card inset panels, drawn still once.

## 493. God rays (light; focal; slow; mid; dark/colour; hero/band)
- Bundles of light shafts fall from above the frame through haze, uneven in width, with a few soft drifting motes.
- Defaults: origin (0.3, −0.2), tilt 22°, spread 60, density 0.35, intensity 0.7, falloff 1.2, speed 0.04, dust 0.3, tint 0.5, calm 0.5 at (0.22, 0.72).

## 494. Light orb (light; focal; slow; mid; all; hero/card/band)
- One sphere with a slowly turning nebula, a bright rim and specks of light: glowing in a dark field on light-text pages, a dark glass ball on others.
- Defaults: size 0.36 (0.12–0.6), rim 0.8, inner contrast 0.5, stars 60 (0–200), glow 0.35, speed 0.05, pulse 0.
- Never as a feature-card panel ground. Avoid with dotted globe.

## 495. Prism light (light; focal; slow; low; dark only; hero/band/card)
- A soft white beam crosses a dark room, breaks into a widening fan of colour and lands as a glowing spectrum on the far wall.
- Defaults: split point (0.28, 0.4), bend 30°, fan spread 0.42, hue spread 55° (20–70), beam width 0.006, haze 0.5, sway 0.02, calm 0.4.

## 496. Soft light bars (light; focal; slow; low; all; hero/card/band/footer)
- Four to seven soft, nearly upright bars of light grouped to one side, like light through slats, breathing slowly beside an empty gap for text.
- Defaults: speed 0.5, tilt 0.5, softness 0.6, glow 0.8, breathe 0.5, haze 0.5, stipple 0.4, grain 0.5, calm 0.55.

## 497. Stage spotlight (light; focal; slow; low; dark/colour; card/hero)
- One slanted stage light from out of frame falls through drifting haze and lands as a soft floor pool, for a product or UI on stage.
- Defaults: x 0.5, lean 0.3, width 0.22, pool Y 0.8, haze 0.45, edge 0.5, intensity 1, speed 0.12, calm 0.4 at (0.2, 0.3).

## 498. Water caustics (light; focal; slow; mid; all; card/hero/band)
- Curved lines of light, bright where they gather and faint where they spread, drifting like sunlight on a pool floor.
- Defaults: scale 5 (1.5–8), sharpness 3, speed 0.15, intensity 0.75, distortion 0.62, depth 0.6, calm 0.5. Render only its flat floor net.
- Never in type.

## 499. Edge glow (light; border; named only; card)
- Light runs around the edge of a card or prompt box: a bright head with a long fading tail that washes the box as it passes.
- Defaults: radius 14px, width 1.4px (0.5–3), glow 26px, bloom 0.6, segment 0.4, speed 140 (20–400), count 1 (max 2), idle 0.35, wash 0.5.
- Only for the one key object (prompt box or featured plan). One lit border per page.

## 500. Dot terrain (pattern; quiet; slow; mid; all; hero/card/band)
- Rolling land as a cloud of points, like a laser scan, lit from one side, heaving in slow waves toward a soft horizon.
- Defaults: spacing 14px (8–40), dot 3px, amplitude 0.17, wave scale 0.8, speed 0.08, opacity 0.85, shade 0.75, crest 0.85, horizon 0.24, fog 0.4, haze 0.35, calm 0.9. Never behind UI. Avoid with dotted globe.

## 501. Grid pulse (pattern; quiet; slow; low; all; hero/card/band)
- A fine hairline grid with signals running along the lines; nodes and cells they pass light and fade, like a circuit trace.
- Defaults: cell 48px (16–128), line opacity 0.1, pulses 6 (0–12), tail 2.5, speed 150, turn chance 0.25, glow 0.6, trace 0.6.
- Never in charts (its traces blink at random); never behind UI.

## 502. Ruled dot ground (pattern; quiet; slow; low; all; card/band)
- A fine dot ruling with a small cross on every fourth node over a grainy ground; a wide soft light drifts across.
- Defaults: cell 16px (12–28), major every 4, ink 0.5, focus 0.6, speed 0.8, reach 0.5, grain 0.5.
- Use for a technical product's panel that holds no UI, or still inside data areas; never behind a window or fragment.

## 503. Topographic contours (pattern; quiet; slow; low; all; hero/card/band/footer)
- Thin contour lines with accent index lines over stepped elevation tints and faint hillshade, slowly breathing.
- Defaults: levels 24 (6–60), scale 1.6, line width 1px, index every 5, opacity 0.35, speed 0.02, octaves 3, tint 0.6, shade 0.5, calm 0.75.
- Never as a stand-in for a map (judged a fake drawing); never behind UI.

## 504. Dotted globe (pattern; focal; slow; mid; named only)
- A globe of fine dots with real continents turns slowly, bright at the front and fading at the rim, while one thin arc at a time lifts between two cities.
- Defaults: speed 3.5 (0–12), size 0.72, spacing 7px, dot 1.05px, land 0.38, sea 0.16, back 0.12, arcs 6 (0–12), glow 0.55, tilt 16°.
- Only as the effect, only for global reach (global, network, infrastructure, payments, logistics). Avoid with orb and dot terrain.

## 505. Ridgeline (pattern; focal; slow; low; named only; band)
- Stacked thin lines rising into a few clean peaks, front lines hiding those behind, one line in the accent.
- Defaults: lines 36 (12–90), peak 0.38, envelope 0.35, line width 1.2px, speed 0.03, span 0.84, focus 0.5. Lines rise on the side away from the copy.
- Never dealt alone (reads as a record cover).

## 506. Fluted glass (material; quiet; slow; mid; all; card/hero/band)
- A pane of ribbed glass over soft page colours; each rib bends a thin slice of what is behind.
- Defaults: rib width 28px (10–80), angle 0°, distortion 0.5, highlight 0.15, shadow 0.16, blur 0.1, speed 0.03, calm 0.4.
- Never in type (on a colour ground it paints thick accent bars through letters); no glass sheen in pills or bars.

## 507. Silk folds (material; quiet; slow; low; all; hero/card/band)
- Large unevenly spaced folds of satin in one page colour (a muted tint on light pages), with a broad soft sheen moving slowly.
- Defaults: tone 0 (0–2), scale 1, folds 0.6, sheen 0.6, speed 0.05, grain 0.02, angle 25°.
- Allowed in letters and digits (dark and colour pages), still. No silk sheen in a pill or bar.

## 508. Duotone grade (photo; still; named only)
- A section photograph graded into two or three page tones with still grain; without one, a calm study of window light clear of text.
- Defaults: tones 3, contrast 0.45, grain 0.4, scrim 0.5. Never on a client's photograph — in practice never on a page photo.

## 509. Retired effects (never use)
- Riso print, ink bloom, liquid chrome, metaballs, brushed metal, paper texture, terrazzo speckle (reads as a kitchen floor), marble warp (zebra stripes), pixel mosaic (broken JPEG blocks), Truchet arcs (thick grey worms), soft particles (stock bokeh).

## 510. WebGL creative parts (under the one-effect rule)
- Every part holding a WebGL context is the page's one effect: dither object, filled headline or stat, globe, avatar ring, logo light, progress light, prompt glow, edge-glow plan, card spotlight, button fill. It sits in the hero or the one framed visual, or serves a dealt moment in its own section; never beside a live hero ground.
- Everything else stays quiet: a search glow only while focused; one ring on the recommended plan; chips with still grain. One lit border per page (prompt or pricing).
- Nothing moves with scroll; a card never moves by itself; motion lives inside a visual (a pointer clicking in a UI window, rotors spinning up under the pointer, a seat swivelling after it).
- Logos never move and show in full colours (no logo marquee or logo-light effect). A drawn decorative band between sections is not a section.

## 511. Effect techniques (concepts)
- Still render: an effect with speed and drift 0 is drawn once as it nears the screen, copied into a plain picture and its context freed; stills draw one after another so only one context is held at a time. Never leave a still mounted with a running frame loop; never give a still a pause button.
- Type fill: the glyphs of an element show the effect via an overlay next to (not inside) the element, so text stays real HTML.
- Windows: one canvas seen through many shapes (chips, bars, cards).
- Ring: a host shown only in its padding — a 1.5px border of the effect.
- Glow: a host blurred into a soft light behind one object.
- Draw an effect 20–25px larger than its box and clip it.

## 512. When to use each effect part
- Feature card: a 2×2 of product features — not for features with nothing to show in a window.
- Dither object: the product as an object with no photograph — not decoration, not a studio render.
- Filled headline: the hero or closing line, filling 2–3 words — never body text, never two filled lines on a page.
- Filled stat: 2–4 proof numbers from the brief at the stat size (38px at 1440) — never small numbers, count-ups or invented figures. On a light page, stat digits take a plain ink fade instead (an effect in digits on white reads as scratched metal).
- Button fill: the one primary call to action (or one pair), fading in on hover/focus, context held only while pointed at (freed 4s later) — never every button.
- Prompt glow: the hero prompt box of an AI or dev product — not ordinary forms.
- Search glow: docs or command search, only while focused — never a field that always glows.
- Effect tabs: a product tour or dashboard preview — not navigation.
- Icon tiles: a feature grid with drawn glyphs — not brand logos.
- Card spotlight: a row of plain feature cards (security, admin) — not on a page with another pointer effect.
- Globe: products with global reach — not local businesses.
- Street map: visit/contact — not a product without a place.
- Chart: one metric over time — never decoration without numbers; default fill is a plain accent fade under the line (or still ruled ground); never an effect drawing its own grid or moving traces over a chart.
- Bars: monthly figures on a labelled scale — never more than 16 bars; still low-contrast grain fill.
- Photo: the client's own photograph of the subject in colour — never mood stock, blank notebooks or filters.
- Avatar ring: calls, presence, a team list — not static team grids.
- Pricing glow: the recommended plan only — never all plans.
- Progress light: only inside a product window as its own import/setup step — never a progress bar as a card or visual of its own, never page loaders.

## 513. Picking an effect per surface
- Feature-card panels: painterly landscape (with a scene light) or grain gradient; ruled ground only for a technical panel holding no UI.
- Inside letters and digits: silk folds or aurora curtains (dark and colour pages), still. Never fluted glass, caustics, halftone or line engraving in type.
- Inside small shapes (chips, pills, bars): grain gradient with still grain, low contrast; no silk, glass or metal sheen.
- Inside data: a plain accent fade under a line, or still ruled ground; bars take still low-contrast grain. Never halftone in a chart area.
- Button fill: an even, low-contrast grain that moves only while pointed at; no blobs that settle at one end.
- A photograph or dither object takes no dealt effect.
- Replace every number, name and stand-in with the client's own; a figure the brief does not give is left out, never invented or tagged "sample".

# Part 19 — Backgrounds

## 514. The three ground tokens (every kind)
- Use only three section/panel grounds: main, alt, dark — one to three colours down the page, footer included, in the same order at 390px. Photograph layers and tech CSS grounds don't count among them.
- Better grounds come from fewer, better colours.

## 515. Main ground
- White, or a tint of lightness 0.80–0.97 with low saturation (channel spread 0.12 or less), taken from the client: a place's walls, paper or shopfront (by trade, never one fixed off-white for every place; white for a shop that sells mostly online), a product's photo backdrop, warm greys for a service, blue-leaning or cool grey for software.
- Covers 55% of the page's height or more (60% on software and product). Never pure-white panels on a cream page.

## 516. Alt ground
- Same hue (within 20°), 0.06–0.15 darker in lightness, never under 0.70 (e.g. `#ffffff` → `#f2f2ef`; `#f7f3ec` → `#ede6da`). For panels, tiles, cards and at most one full band.

## 517. Dark ground
- Lightness 0.05 or less: near-black (`#111`–`#1a1a1a`) or the deepest shade of the brand hue; never charcoal, never violet.
- One dark body section at most (one screen tall), at the page's middle or later, never right under the hero; the footer may be dark.
- A dark page (main ground 0.02 or darker) and a dark hero are for tech only.

## 518. Brand band (product and place)
- One section in the brand's own colour (from product or shopfront) may replace the dark band, once, in the second half.
- On a place: lightness 0.03–0.60, saturation 0.25 or more, never a neutral near-black. Every word on it takes the colour that passes 7:1 (darken the brand colour until it does; 7:1 clears both reading text and 4.5:1 labels); the primary button is inverted.
- Otherwise saturated colour lives in the accent and pictures; one mid-tone section at most, never as the main ground.

## 519. Ground changes
- Change grounds in big blocks at section edges. Never on an inner wrapper; no border-top or rule between sections; no band inside a section (a box of 80%+ width with its own ground holding the heading); no inset coloured box standing in for a ground. A frame holding a visual is fine.
- A ground never changes a section's height. A soft ground fades over 120px; a hard ground keeps its colour on the whole box; an inset panel aligns to the container lines.

## 520. Non-tech kinds stay flat
- Product, service, place: every ground and panel a flat colour; photographs shown as they are. No gradient (hard-stop two-tone included), grain, paper, halo, texture, pattern, glass, contour, canvas, backdrop blur, gradient mask, or shadow/tint on the interface.

## 521. Grounds in frames (tech)
- One effect per page (only in the hero or one designated visual frame) and one card group's still shader grounds, each panel its own seed.
- Every other tech frame: the lit ground plain, a flat alternate-ground panel, a photograph or a diagram.
- Product, service and place frames hold photographs on flat colour; never a code/shader ground.

## 522. Tech CSS grounds: general rules
- Sixteen CSS-drawn grounds (no WebGL). Ink keeps 7:1 and muted 4.5:1 on every palette within the ground's text zone.
- At most two dealt grounds per page beyond the tokens, each once, never on a card, never two strong ones as neighbours, one loud one at most, never two that avoid each other.
- Every page of five sections or more holds one coloured ground (band, field or stage).
- A ground with grain, dither or texture (grain, field, stage, deep) or motion (liquid) counts as the page's one effect; with another effect dealt, choose others. The section holding an effect or scene brings its own ground.
- Weights: 1 calm (reads as the page), 2 medium (a visible change of ground), 3 loud (the one section a screen remembers).
- Kinds: soft (paints no colour of its own, fades into the page top and bottom, neighbours anything); hard (a band with its own colour and edges; can be a rounded inset panel on the grid); page (whole page or one wrapper); panel (a rounded vivid panel behind one visual, with no text of its own — every word on it sits on a card).
- Tints lean to the accent (hue guard: never violet or lavender); strength knob default 1.
- Minimum height of a ground section: min(88svh, 860px) for hard grounds, min(76svh, 760px) for soft.
- The lit ground (sand, sky, sage, painting) is tech only: behind UI, in a closing band, in the footer statement; it's the tone of band and field.

## 523. Ground: mist (soft, weight 1)
- Airy soft colour fields, a wash of light in two neighbouring hues. For a section head over a row of three open cards, a feature list, any section needing a little colour. Hero/body. Avoid with halo, top glow, liquid, dusk.

## 524. Ground: halo (soft, weight 1)
- One light behind one thought. For a centred statement or closing line (heading, a few lines, a button); position the light where the heading sits. Hero/body/close. Avoid with mist, liquid, arcs.

## 525. Ground: ruled (soft, weight 1, strict)
- A grid that is the page's own frame: its first and last rules lie on the container's edges, fades toward top and bottom, clear behind the heading. For a centred hero/statement or a section with one big visual. Never over a table, pricing, a list or any section drawing its own row rules. Avoid with dots, arcs.

## 526. Ground: dots (soft, weight 1)
- Quiet dot field in margins and corners, clear behind heading and words, with a pool of light behind the heading. For a centred section with a row of figures, a logo row, integrations. Avoid with ruled, arcs.

## 527. Ground: arcs (soft, weight 1, strict)
- Rings rising from below (x.ai-footer style). Only for the closing call to action or the section above the footer: heading and button over rings. Avoid with ruled, dots, halo, horizon, liquid.

## 528. Ground: liquid (soft, weight 2, animated)
- Two slow blobs of neighbouring hues drifting, transforms only. For a CTA or hero with a heading and two buttons. One per page; it is the page's moving thing (no other looping effect in view); runs on a clock from load with a pause disc; holds still under reduced motion. Avoid with mist, halo, top glow, arcs, photo, stage.

## 529. Ground: grain (hard, weight 2, never dealt)
- A tinted field with fine film grain, a light corner and two neighbouring hues; for a split with text left and one UI card right. Counts as the effect.

## 530. Ground: paper (page, weight 1, never dealt)
- A page ground that is never flat: fine grain and faint tint at top and bottom; shows through soft grounds, covered by hard ones.

## 531. Ground: dusk (hard, weight 1)
- One tone melts into the next with no edge; both ends melt into whatever the page paints there. For a quote with one big number, a proof section, a section between two plain ones. Avoid with mist, grain.

## 532. Ground: top glow (page, weight 1)
- Light under the nav that the page lifts out of: a glow from the top edge and a thin lit line, wrapping nav and hero. The hero's ground for software and service-style tech pages. Avoid with mist, liquid.

## 533. Ground: band (hard, weight 3, coloured)
- A coloured band in the page's second tone (the lit ground or a brand tone), lit from one corner, deeper in the other. For one big number and a UI card, or one statement with a button. On a dark page, the one light band. Tint variant: second tone a pale tint of the accent's own colour (a mint for a teal accent). Avoid with field, grain, stage.

## 534. Ground: field (hard, weight 3, coloured, texture)
- A grainy gradient in one family of colour (peach beside sand, cyan beside sky) with a light sweep (Figma's sand tile). For a centred heading over one or two UI cards; best as a rounded inset panel. Avoid with band, grain, stage.

## 535. Ground: stage (panel, weight 2, coloured, texture, strict)
- The accent as a grainy mesh that one card floats on (Figma's colour tiles): the panel behind the one UI card/window beside a section's text. Never behind a heading. On a strong-colour page it takes the accent's hue; with a grey accent, the lit ground's colour. Avoid with field, grain, band, liquid.

## 536. Ground: photo (hard, weight 3, strict)
- A photograph layer for a media band, a closing photo (and, on tech, a hero). Words sit lower-left (text zone left 60%, lower 40%) or in the middle of the left side (left 45%); a pale photo takes dark words.
- Words only in the hero and one closing band, on the photo's calm dark part; position the subject separately for phones. Needs a vetted photograph with a calm area. Avoid with horizon, deep, liquid.
- Scrims and gradients over photographs stay banned here too; prefer the calm part or a flat band.

## 537. Ground: horizon (hard, weight 3, strict)
- A dark band with a lit curve like a planet's rim, brightest at the top. For a statement the page is sure of (security, scale, a promise) with a button above the horizon; the page's one dark band. Words stay above the lit curve (top 58%). Avoid with deep, photo, arcs.

## 538. Ground: deep (hard, weight 2, texture, strict)
- Near-black with a cool pool at the top, a lit lip and grain (x.ai style). For a feature section with two or three UI cards (chat, code, voice) — the dark ground UI reads best on. Avoid with horizon, photo.

## 539. Ground modifiers
- Inset: a hard ground as a rounded panel whose left/right edges sit on the container's.
- On a dark page a band or field is inset automatically (a pale full-bleed slab would be the brightest thing); allow full-bleed only deliberately.

## 540. Code-drawn ground craft (tech)
- Calm and specific as a studio photograph: one light, one palette, grain noticed only up close.
- Colours from tokens (ground, ground-2, ink, tone, tone-hi = L +0.12, tone-lo = L −0.18), mixed in OKLCH, ground chroma under 0.12.
- Build a gradient light first: a radial with four to six stops in one hue, then grain 4–10%; every dark gradient gets a static dither; never a two-stop linear gradient as decoration (linear only as an edge fade inside a visual); a two-tone seam is a hard stop.
- Grain only inside the one effect: one tile made at load, never animated, never over UI, text or photographs.

## 541. Recipe: lit studio sweep
- Behind a cut-out or UI window: an elliptical radial 50–60% × 40–50%, centre 35–42% down, a faint floor bounce, grain 4–6%, a soft contact shadow.

## 542. Recipe: corner glow
- For a dark footer, closing band or pricing card: a radial near one corner, radius 110–130%, five eased stops so no ring shows.

## 543. Recipe: painterly field
- Under a UI window or closing band: four to six large ellipses in the tones, blurred 60–120px, drawn 10% oversize and cropped, plus grain.

## 544. Recipe: spotlight floor
- For a hardware stage or dark hero on a dark page: a light pool 70% wide, a blurred shadow running away from the object, side vignettes.

## 545. Recipe: product-colour wash
- For a hardware card or model switch: a radial from below in the product's tint; cross-fades on a click, never on scroll.

## 546. Recipe: woven tile and ordered dither
- One texture per page at most: a band, the footer or a technical panel.

## 547. Recipe: grid marks and hairline ledgers
- Dots or plus signs at column crossings, 12–18% ink, only on one dark technical band, a data panel or the footer, never over text.
- A hairline ledger (header cells, a line-up, footer frame) is 1px repeated sibling rules at 12–15% ink, never between sections.

# Part 20 — Photography and image treatment

## 548. Role of photographs by kind
- A place (cafe, bakery, guesthouse, shop, studio) is its photographs: two or three on every screen, the client's own.
- Software leads with its real interface; a photograph there is a real person or the real product.
- A game leads with its own art (key art, in-engine shots, trailer poster), never library frames; with no art, its name set large over a stand-in photograph of its setting; a render of its world only if 3D is asked.
- A physical product without photographs is still shown in photographs (client's, else stand-ins).
- A photograph never stands where an effect, a drawing or an empty box would; and nothing (box, grid, effect) stands in for a photograph.

## 549. Source hierarchy
- 1. The client's own (shot for the page or on a phone). Tag every image with its source and subject.
- 2. Vetted stock library frames — detail slots only (hands, tools, materials, a process: an oven, dough, a roasting drum, stems, a hammer on a bar). Never the hero, a room, a shopfront, a product or a person; never more than 1 in 3 of the page's pictures. Only frames rated 7+/10, with no whole figure, no animal, no vehicle, no landmark, no mood frame.
- 3. Licensed live-search stand-ins (CC0, CC BY, CC BY-SA, public domain; JPEG 1600px wide or more; not paintings, drawings, maps, logos or posters; one file per series) for what the library lacks (a product's kind, a yoga studio, a bike workshop bench, a hotel's building and rooms, a wedding, a game's setting).
- 4. Nothing: the real UI, or type; a product's own render only if 3D is asked. Never a near fit, never mood in place of the subject.
- Thin trades get at most as many library frames as exist (e.g. wine 0, bar 0, office 3, florist 3, farm 3, shop 3, wellness 3, bakery 4; smith 4, instrument maker 1, weaving 0, letterpress 0). A workshop gets only its own craft's frames (a smith's page never shows a weaver's loom).

## 550. Choosing photographs: further rules
- Use real photographs; none twice (compared by content; a FAIL on a product page).
- Hero, menu, visit, contact, booking and closing sections get no library frame; nor land, sky and street.
- Never a mood picture in place of a detail of the section's subject.
- A bakery gets ovens, dough and loaves; a florist stems and buds; a workshop only frames of its own craft.
- Live-search stand-ins: CC0, CC BY, CC BY-SA or public domain JPEGs at least 1600px wide; no NC or ND licences; no paintings, maps, logos or renders.
- Never pass library frames off as the client's own room, staff or product.

## 551. Vetting a stand-in
- Look at every candidate full size. Keep it only if: the subject is sharp, in plain colour; no readable name, sign or logo of another business (crop it out or drop it); no face presented as staff, guests or customers; no landmark passed off as the client's place; one light and grade with the rest of the page.
- Write new alt text (the file's title names someone else's place). List every stand-in for the client with the photo to shoot in its place; nothing on the page says it's a stand-in.
- Search in plain words, two or three (long phrases find nothing): a product's own words ("cargo bicycle", "desk lamp", then "… detail" and the place it lives); a game's setting ("flooded coastal town", "desert mining town", "city at night in rain"). Minimum 1200px for a row picture.
- Trade search vocabularies: yoga/pilates/spa (yoga studio, yoga class, pilates studio, sauna interior); pottery (pottery wheel, pottery studio, ceramics workshop); art/design/photo studio; bike workshop (bicycle workshop, repair stand, mechanic, city bicycle, cargo bicycle); hotel/guesthouse/inn (facade, room, bedroom, inn exterior — building and rooms always from search, never library); wedding (ceremony, table, bouquet, reception, rings); restaurant (kitchen, interior, chef plating); workshop by craft (woodworking, blacksmith forge, tools); bakery (bread, counter, baker dough); cafe (coffee shop interior, espresso machine); florist (shop, flower market); salon (barber shop, hair salon).

## 552. No client photographs: shoot advice
- Say so plainly: strong pages run on a half-day shoot with a local photographer, then a one-morning phone shoot, then products on one backdrop; stock covers details only.
- Shot list: shopfront straight on; the room from the door; the counter or bench; three products on one surface; hands at work; one detail; each room of a guesthouse. 1x lens, window light, no flash, no filter, landscape and portrait.
- Product shot list: the product on one plain backdrop, three angles, a detail of each part the page names, the product in use.

## 553. Draft page and the short page
- A draft place page with no client photos lifts the 1-in-3 cap and aims for 8–12 frames (a cafe 8–12; a guesthouse about 9 detail frames), repeating subjects per row.
- If, after exhausting stock and live search, the page has under eight frames, build the short page (2,700px tall at most at 1440), whatever the trade.
- Draft hero: a full-bleed top photograph with nothing on it. A hero the stock cannot fill stays empty — never a row picture blown up. Never a latte-art close-up or a soft hazy older file as an opener.
- A place whose trade leads with land (guesthouse, lodge, remote inn) leads with its named region's landscape; a place hero always carries a photograph when any frame fits; a type-only statement hero only when no frame exists.
- Land is only ever the client's own region: never another region's land, a cafe's street, or the sky. A broader place tag than the client's place is never used (a frame tagged only "Iceland" is not "Reykjavik").

## 554. A product without photographs
- Never mood stock (no forest for "the ride", no groceries for "what it carries"), never another trade's frames.
- Show the product in photographs: a picture the brief supplies first (cut-out, CAD view, own render), else stand-ins of the same kind of thing whole and in use (a cargo bicycle for a cargo-bike brand, never a wheel for a bicycle), close-ups of named parts, where it lives; no maker name/logo/badge readable; no face passed off as a customer; one light and grade across the set.
- It's the full product page, never the short page. (A cargo-bike page that never showed the bike scored 3/10.)
- A shop/workshop/rental for every make is a place: parts and basket loads from stock, workshop bench and whole bikes from search.

## 555. Photographs on product, service and place pages
- Photographs lead every main section: the client's own, else licensed stand-ins; one look and grade; shown plain; credited in one footer line.
- No caption, name, price or link line under a bare picture; a sold item's name and price sit inside its card's padding.

## 556. Ratios and layout
- Place pages use 4:5, 4:3 and 1:1 only; other kinds add 3:2. One ratio per row, equal sizes in a row; one dominant picture per screen or a row of three or four.
- Frames sit on the container lines (x 120–1320 on a place at 1440, 80–1360 elsewhere; 342px wide at 390). Full-bleed only as a hero or section layer. Left and right edges stay the same down the page.
- A wide row picture keeps a 66.7% ratio at every width. Object-position at the subject's focus so a phone's square crop keeps the cup or hand.
- Never carousels or sideways-scrolling rows.

## 557. One visual world
- One light, one grade, one register across the set. Hard sun on one product, or a low-key set on dark timber or steel, only if the whole set matches. Never studio black with daylight, HDR beside a snapshot, two photographers' grades.
- Black-and-white is one deliberate frame at most.
- Never the same frame twice on a page (a smaller file, crop or mirror is the same frame), never three near-identical frames.
- Mixed light gets a crop and one ratio system, not an effect.

## 558. Hero photograph
- Plain full colour. On a place: a full-bleed top photograph about 480px tall with nothing on it and the words below. A software or product hero ends inside the screen.
- Deliver full width (`sizes 100vw`, never a vh term), high fetch priority, eager; a 780×975 (4:5) crop for phones under 640px with the subject inside the middle 342px; let the place hero photo grow on phones into the space its words leave. A 4:3 source shown taller on a phone is upscaled — avoid.
- The hero's 2x at 1440 needs 2880px wide; stock heroes (largest file within 400KB, 1200–1800px) look soft on retina — another reason to replace with the client's own.

## 559. Section photography patterns
- Rooms: one detail per room beside its facts; a place's rooms are the client's photographs first; never a whole room/lounge/breakfast room from stock.
- Menu or goods: the list in plain text beside the offer's composition; never one photograph per line, never tabs.
- Photo bands: product one or two; place one (a bleed composition), never next to the hero; a place closes on a 1:1 shopfront photograph with no words.
- Place compositions vary (bleed, pair, trio, strip, tall-small); never two sections built round one picture.

## 560. Text on photographs
- Never on a place. Elsewhere only in the hero and one closing band, on a calm part that is empty and dark (or light) at both desktop and phone crop, or in a solid box, or off the photograph.
- No scrim, gradient, fade or blur over a photo for legibility. Contrast 4.5:1 (3:1 display text).
- At 768px a 3:2 lead is cropped to its middle: if that puts words over the subject, move them under it as on a phone.
- Every full-bleed photo carrying words has its own 390px crop with the subject inside the middle 342px.
- Never words over the busy part of a picture; avoid detail or bright and shadow patches (5-95% luminance spread) under words.

## 561. Photograph with copy
- The client's photograph in natural colour, the copy on its calm, dark corner (white type, no scrim); in a link it zooms 1.02–1.03 inside its frame.
- Words on a photograph only in the hero and one band per page, never on a place.
- No filter over it (no halftone, dither, dissolve, print, duotone, blur). Takes no effect; no WebGL; under reduced motion the zoom is off. Credit in the footer line.

## 562. Cut-outs, supplier images, illustration
- Cut-outs only of the client's own subject (transparent), on the page ground or one backdrop, no drop or fake shadow; never stock, never people or buildings.
- Supplier/maker images only inside a product grid, only what is sold, never the hero.
- Illustration only when the client already owns it, still.

## 563. Visible from first paint
- A photograph is never in an element starting at opacity 0, clipped or moved for a scroll reveal, never under a print, dissolve or mask that develops on load, never replaced by a video. An empty, grey or half-loaded frame at any width (1440, 1024, 768, 390) is a fault.
- (The one exception is the dealt picture-develops moment.)

## 564. No treatment on page photographs
- No halftone, dither, duotone, engraving, grain, glitch, filter or blend mode on any page photograph, and no canvas over half of it. A print is a tech page's one effect, on a non-photo ground.

## 565. Corners and frames
- Place photographs: square corners, no border, shadow, overlay or frame.
- Product and service: one radius for every photograph.
- Software windows: one radius of 12–20px.

## 566. Captions and credits
- No caption, label, description, credit, "sample" or example note on or under any picture. A sold item's name and price sit inside its card's padding.
- The place's name goes in the alt text. Every word on a page is live text, never baked into an image.
- Credits are ONE footer line in the legal row (e.g. "Photographs via Unsplash and Wikimedia Commons" — sources, not photographers, at most 110 characters) that opens a credits list page giving each photographer, licence and source, with "adapted" after any frame cropped beyond its frame or printed. Never a credit link per photograph (18–20 links read as a credit wall). Public-domain frames still name the photographer. The client's own photos need no credit.

# Part 21 — Product renders and print objects

## 567. When to use an object at all
- One strong object moment per page; never beside a second effect or over a moving ground.
- Place, service and every non-tech page: no object, print or scene; plain photographs lead. Exception: a product whose brief asks for 3D shows its own render.
- Product with photographs: the photograph leads.
- Any physical product without photographs: photographs first (client's, cut-out, CAD view, else stand-ins), never a render by default. Pages carried by a render and a fixed set of props read as random 3D objects.
- A render only when the brief asks for 3D or a render (a configurator, "show it in 3D", a product existing only as a model). Then it leads the hero, then appears whole in at most two more sections, each a different view, big in its frame, never in a grey panel; part close-ups carry the others.
- Software/AI/games with art: a print object as a print on the card it's about (a globe for regions); a game's own world object for an object scene.
- Never an object of another kind (a wheel is not a bicycle; a cup doesn't show a coffee machine), a drawn SVG, a model of loose primitives, mood stock or another maker's product. Never a split hero holding only an order form.
- Never over the hero photograph or in place of the client's photographs.

## 568. Print objects (modelled everyday things)
- Shown as a studio render (default: its own materials, accent on one part, soft shadows, softbox reflections) or, on software/tech/AI/games pages only, as a print of that render (halftone, engraving, dither, ASCII/type). A product page shows the render.
- Idle: turns slowly; hover: light follows the pointer and the object leans toward it; click/Enter: one small step.
- Cup and saucer: porcelain cup of coffee, glaze outside in the accent, white porcelain inside and saucer; one turn in 36s; click: rings run across the coffee and settle; prints halftone/engraving. For ceramics/tableware/home goods; on software, a card about a break, routine or morning.
- Bicycle wheel: road wheel, black tread with tan sidewalls, alloy rim with valve, 24 spokes laced to a two-flange hub in the accent; sways through three-quarter views and rolls slowly; click spins up (max about 220°/s), click again runs down; halftone print renders spokes as solid lines. For wheel/wheel-part makers; on software, motion, speed or a mechanism. Never a whole bicycle.
- Desk lamp: balanced-arm, heavy stepped base with turret, two pairs of rods, two chrome coil springs hooked to a crossbar, knuckle joints with chrome caps, domed shade with vent cowl and rolled rim; base and shade in clear-coated accent enamel, graphite rods; sways about its base with profile always readable; click switches on (bulb and inner shade glow; in the render a warm pool falls on the desk; on light paper the paper there turns warm; prints leave the pool out). Reads best on dark paper when lit. For lighting/furniture; on software, focus, reading or working late.
- Desk globe: real coastlines on a tilted axis, brass half meridian, turned walnut stand; Earth turns slowly while the stand sways a little; click flicks it to spin up and run down; prints as engraving. Sea takes the accent only if blue or teal (a green or orange sea reads as land); otherwise the render keeps a deep ocean blue and a print puts the accent on the land. For maps/globes; on software, regions, countries, languages or shipping.
- Playing cards: a loose stack, ace of diamonds face up (an A and small pip in two corners), backs with white border and fine diamond lattice in the accent; turns slowly in a loose spread; click fans them wide, again gathers. For card/board games; on games or software, play, a hand, a draw or a deal.
- Never captioned; never called a render, drawing, illustration, model, sample, stand-in or "made in code". Name the thing plainly in its accessible label ("A desk lamp, switched on").

## 569. Object placement presets
- Card: in a panel, large, cut by the bottom-left edge (x.ai/Figma feature-card style), keeping the bottom-right corner clear for the pause button; cut less in a near-square panel (phone). Card text sits above the panel, never over the object.
- Tile: whole, standing low in a square/top tile, title and text under it.
- Hero: large, right of centre in a wide frame, text in the clear left half; in a near-square frame (phone) smaller and low under the text.
- None: centred on its own paper (demo only). Never centred dead in a card panel with even ground all round.
- Size 0.3–1.8 of the frame (over 1 runs off the edges); offset x/y −0.6 to 0.6; floor shadow 0–1.6.

## 570. Object rules
- One object per card group turns by itself; the others hold still until pointed at or clicked; at most two in view; never over a moving ground (the ground holds still: speed 0, grain motion 0). On a product page a plain lit ground or the page surface.
- The object is the picture: no UI fragment over it, no second effect beside it.
- Never animated by scroll (except inside its dealt object scene); it moves only by its own slow turn, the pointer and a click.
- Colours: on a dealt ground, draw on that ground's paper with an ink that reads and the page accent; else page tokens. Accent on one part only. Until the ground has drawn, lay the ground's paper flat beneath so a dark-paper print never stands on a pale undrawn panel.
- Keyboard: the object is a button (toggle state for on/off) with a focus ring inside the panel; Enter or Space takes the step.
- Reduced motion: one still frame at rest angle, no turn, no hover light, no pause button; a click shows the step at once.
- A poster (pre-drawn picture in the page palette) shows at once and the live picture cross-fades over it; the poster stays when WebGL is missing, a shader fails, or the first frame comes out empty — never an empty ground.
- Model the real thing (proportions, parts, materials) so the render reads as a product shot, not a drawing; check at 1440, 820 and 390 on light and dark paper; if it still looks cheap after two honest tries, drop it.

## 571. Product render: purpose and placement
- A studio render of any physical product composed from a spec of its real parts: real materials (painted metal, alloy, chrome, rubber, wood, fabric, leather, plastic, light), soft studio light and shadows, a softbox in glossy parts, a floor shadow, the page accent on parts that ask for it. One product render per page.
- Place shares of the frame filled by the product's bounds (tighter axis), always centred: stage 0.86, hero 0.88, tile 0.84, card 0.9; fill override 0.3–1.2.
- Transparent over the frame's ground, floor shadow included; the frame loses fill, border and padding: no panel, no grey box. Words never over the product or beside it within the frame; words stand outside it.
- In the product hero the stage spans the wrap, the frame runs 7% past its top and bottom so the product is as tall as the stage; its widest view spans 80%+ of the wrap at 1440 (a city bike's side view 1046 of 1280px; three-quarter 818).
- In the hero and one more section the product's long side is 80–100% of its frame, or a close-up runs it off the edges.

## 572. Product render: views
- A different view in every section; the product whole in three sections at most; never the same view twice on a page (not even in two sizes).
- Widest view in the hero (a bike's side; a lamp's or arm's three-quarter); another angle; a close-up on the part a section talks about; the loaded/in-use scene where copy promises what it carries.
- Standard views: three-quarter (default angle −32°), side, side-left, front, rear, top, low — offer only those the product draws well (a bike from above reads as lying on its side, so omit top).
- Close-ups frame the named parts, centred, filling the place's share; the rest of the product runs off the frame edges (the frame clips it), never a hard cut inside; shot wide enough (up to 2:1 wide, 1:1.25 tall) and cropped evenly round the parts' centre. Example close-up framing: saddle at angle −42°, elevation 16°, margin 1.3; drive at −18°, 10°, 1.15; lamp shade at −58°, 24°, 1.3; gripper at −40°, 14°, 1.35.
- Every promise in a headline is shown in a picture (a child seat with belts, the crates, a lamp's light on the desk).

## 573. Product render: stills, live and swatches
- Stills by default (pre-rendered transparent images per view and colourway, light and dark ground variants, half-size in the srcset) — no canvas and no WebGL on the page. Live turning only when asked; at most one live context; the first live render turns, a second holds still.
- Phones (max-width 700px or coarse pointer) and reduced motion: one sharp still frame, context freed. A turning product has a pause button in its frame's bottom-right corner.
- Colour swatches on the order card drive the frames they name: one pressed per group; on click the frames swap to that colour's still. Every colour offered shows once on the page.
- Default turn: sway, amplitude 26°, period 22s (examples: bike sway 22°/24s at −34°; lamp 24°/22s at −38°; robot arm 14°/28s at −26°); or spin at 10°/s; or still. Camera elevation default about 12°.
- Example colourways: bike moss green `#1f6f5c`, deep blue `#2c4f7c`, cream `#e2d8c3`, signal red `#b3332a`; lamp ember orange `#d9542b`, soft black `#2a2b2e`, sage `#8ea489`; arm signal blue `#2b5fd9`, safety orange `#e0702b`, graphite `#3a3d42`.

## 574. Product render: modelling the spec
- Axes: x = the product's front, y = up, z = across toward the viewer at angle 0. Any unit; the model is normalised so its largest side is one unit and set on the floor at its lowest point. Model from real measurements — proportions are most of what makes it read as the thing.
- Part types: tube (radius, taper, flat/round caps — frame tubes, posts, rods, tapered robot links); beam (flat bars, cranks, rails, drone arms); box (housings, bodies, pedals, grippers, crates); panel (plates, lids, screen backs, a hull deck); cylinder/disc (bases, hubs, motors, lenses, rotors); sphere/ellipsoid (bulb, bell, knob, buoy); torus (rings, chainring, status light); joint (hinge knuckle with caps); wheel (tyre, rim, hub, spokes, spoked/disc/solid, sidewall colour, spin); shade (closed→open end, two radii, thickness, bulge — lamp shades, bells, horns, speaker cones); seat (saddle/cushion); basket (wire/slats/solid — baskets, crates, bins, trays); arc (mudguards, handles, hoops, bent frames); spring (springs, coiled cords); path (handlebars, cables, bent tubes, crane rope).
- Fillet blends where parts meet (welded tubes, cast bodies); seams cut panel lines (robot shell, base groove).
- Materials: paint (enamel/powder coat; accent colour from the page), metal (brushed alloy), chrome (polished), steel (dark stainless: spokes, wire), rubber (tyres, pads, grips), plastic (satin), wood (oiled, with rings: oak, walnut), fabric (fine weave), leather, light (emits; switchable by click). Finishes: gloss, satin, matte. Any material may glow 0–1 (a lit inner face, e.g. 0.45 inside a shade).
- Motion groups: up to four, each turning about a pivot and axis by rest + amplitude × sine of a period, chained parent→child (robot yaw 26°/13s → shoulder 9°/11s → elbow 13°/9s → wrist 20°/7s, with phase offsets). Joints move only while the product turns; stills, phones and reduced motion show the rest pose.
- Scenes and props (only where a headline's promise needs one, at a size the section can read; a use photograph is better): child seat (high back, wings, cushion, shoulder and lap belts to a red buckle, footrests), bench (1–3 seats with belts and buckles), slatted crate (fruit, bottles, loaves, parcels), pannier or tote bag, parcel (tape and label), tray of parcels (0–4), desk, 1–3 books, mug of coffee, sheet of paper. Props at real size in metres, standing on the floor. A lamp scene may throw a warm light pool on props' upward faces. No scene and no prop by default.
- Craft: include the details that name the thing (a bike's spokes, chain, mudguards, saddle springs; a lamp's springs, knobs, cord; a robot's caps, seams, gripper pads; a barge's bollards, cables, lamps). Accent on the part a maker would paint; metals and rubber stay themselves. Check at 1440 and 390.
- Part budget: about 20 parts costs like a print object; 60–70 (a bike with spokes) fine on a laptop GPU, slow on CPU; keep a spec under 90 parts and a scene under about 110. Example complexity: city bike 64 parts, desk lamp 19, robot arm 28.
- It cannot do: text or logos on the product, transparent glass, draping cloth, freeform organic shells (a shoe, car body, face, creature), anything thinner than about a texel. Those need the client's photographs or renders. A game composes machines, buildings and props, never a character. A hard device shell (drone, camera, sensor) is rounded boxes, cylinders and fillets at real measurements.
- Never a product of another kind, never on a place page, never captioned or called a render/model/illustration; on tech an effect may sit behind it, never beside it as a second beat.

## 575. Objects in dither (tech; product as object with no photograph)
- A real thing built as a lit 3D form printed in ordered dither in five page tones: ground, shade, ink, accent and deep accent. Use as the hero picture or one split section's visual when the product has no photograph yet.
- Objects: over-ear headphones on their cups; an office chair on five castors; a mirrorless camera with a zoom lens; a camera drone with four rotors.
- Idle: sways slowly on its spot. Pointed at: turns to the pointer, light comes from the pointer, and it answers with its working part — sound rings from the cups; the seat swivels after the pointer (base stays); the lens zooms out as the pointer rises and its focus ring turns; rotors spin up into discs and the drone lifts off its legs and tips toward the pointer.
- The accent paints one part (ear cups; seat and back; body band and shutter; drone shell); its shaded side is deep accent, never grey.
- Only an object the product really is or sells, on a tech page; one per page; no caption — the heading/copy names it with one real fact.
- A product none of the four fits gets its own photographs or a modelled render, never the nearest of these four and never mood stock.
- Use the print look, never the smooth studio look (its edges stair-step at one sample per pixel and it reads as a toy next to real product shots); never for a shop or product page.
- Runs at 20fps, one evaluation per dither cell (a ninth of CSS pixels). Reduced motion: one still, no context, no pause button. No WebGL: a line drawing of the same object with its accent part filled.
- It is a drawing of the product, never a filter: no photograph is ever dithered or halftoned (a halftone over a hero photo read as broken and low-res at every width).

## 576. Photo print treatments (crafted moments; tech/design-tool/gaming only, never on page photos)
- A print is one crafted moment on a software, AI, design-tool or gaming page — the page's one photo band or a feature tile whose subject is the photograph (an imaging tool printing a picture) — one per page (a row of three only on a page about prints). In current practice keep prints to a showcase; never print a page's photographs, never over the hero photo or a section's main photo (reads as broken/low-res), never on local-business pages.
- The print is there from its first frame: no entry, no dissolve, nothing moves at rest. Text never over the print; a small UI card may sit on a corner, never over the subject. No caption explaining it. Credit as "adapted".
- On a dark page pick a darker (dark or mid tone) photograph; a pale one prints as a large light plate.
- Print on the page's surface tone so the frame reads as a sheet; give the frame an explicit aspect ratio (e.g. 4:5) and card radius.
- Fallback: the photograph itself greyed into the palette (multiplied on light paper, screened on dark), never an empty frame.
- Touch: a tap shows the hover state at the finger for 1.6s; lifting the finger doesn't end it.
- Reduced motion: the same still print; hover still answers, without easing.

## 577. Photo print: halftone
- One-ink halftone: round dots of the page ink (or accent) on one 45° screen, on surface-tone paper; its tone curve keeps near-whites as clean paper and deepest shadows solid, with a dotted outline along edges (outline 0.4) so a pale object on a pale wall keeps its shape. Dot pitch 5px; shares under 0.1 print no dot.
- Best: one clear subject in clear light on a plain ground (product, object, building); high-key photos print clean. A busy mid-grey texture (knitwear, foliage) prints as an even checker — pick another. Coarse on purpose: never for a face read small.
- Hover: a loupe (round lens, hairline rim, soft shadow) shows the photo in its own colours magnified 1.35×.

## 578. Photo print: engraving
- Intaglio plate: diagonal ink lines swell in shadows, taper to hairlines in light and bend over forms, over a light wash of the photo's own colour on surface paper; parts lighter than paper print as bare paper; a colour cast in the lights is dropped (a white table stays white). Line pitch 4.5px.
- Best: one object or building in strong light and shade; strongest on light paper; weak on a busy interior (lines fill every surface).
- Hover: lines part around the cursor like under a lens and the photograph shows through.

## 579. Photo print: dither
- Three-colour grain of crisp square cells like a riso print: the photo's deepest colour, its most colourful one, and the surface as paper (found by clustering); tone dithered by blue-noise threshold (even grain) or 8×8 Bayer (retro). Cell 2px. The lightest 0.1 of tones print no grain (near-whites as clean paper). Two tones (ink and paper) read most graphic.
- Best: an object or building in clear light, white subjects included.
- Hover: the photo develops through the grain in a soft circle about a third of the frame's short side, coarser grain at its rim; a quick stroke leaves a short fading trail.

## 580. Photo scene: split reveal
- One photograph split by a line: one side an amplitude halftone in page ink, the other the photo itself; dots near the seam take the photo's colour so the print turns back into the picture at the line.
- Halftone cell 5–8px from panel size (×1.15 on a dark ground), screen 45°, rest split 0.5 (or the entry's), halftone on the left by default; optional side chips (never under 480px wide; off by default).
- Hover: the line follows the pointer on a smooth spring; drag on touch; keyboard slider (arrows, Shift for bigger steps, Home/End). Still at rest.
- Made for: a photograph a photo/design/print tool works on, a device a tech company makes, a game's key art.

## 581. Photo scene: dither sequence
- 2–6 photographs that belong together (a device from several sides, stages of what software makes, a game's scenes — never a random or mood set), ordered-dithered in page palette, played like a slow film loop.
- Each frame holds 2.2s, then wipes to the next over 1.5s at up to 30fps; the cut is a dithered wipe on a slight diagonal with a one-cell accent line on its leading edge; a small pill counts frames (01 / 04) or shows captions on a segmented timeline. Cell 2–3px.
- Hover scrubs the timeline; drag on touch. Pause disc. Reduced motion: first frame still.

## 582. Photo scene: dot object
- One object cut out of a photo shot on a seamless plain ground (or a cut-out PNG) rebuilt from dots that take the photo's tone, so dots draw the form, not just the outline. Gap 4.2–7.5px; fills 0.78 of the panel; 3,000–8,000 dots.
- Hover: a loupe (radius 70–150px) where dots take the real colour and swell until they almost touch.
- Only with a plain-ground shot or cut-out; a busy or sunlit background doesn't cut out (use split reveal).

## 583. Photo scene: exploded layers
- One photograph taken apart into four sheets standing in perspective: photo on top, a halftone in the accent, an ordered dither in ink and a tone-contour plate at the bottom (halftone and dither on clear sheets); at rest a neat stack a card's thickness apart.
- Hover: sheets open apart, prints come up, the stack leans to the pointer; labels on leader lines from a dot on each sheet's right edge (only where the panel is 560px+ wide), only in the client's words (its layers/passes), never the technique names. Sheet aspect 1.2–1.6. Tap opens/closes on touch.
- For the one moment of software that works in layers or passes (imaging, design, print, map, document tools).

## 584. Photo scene: product turntable (generic object)
- A generic thing (rangefinder camera, wooden side chair, cylindrical speaker, glazed cup) on a studio turntable with a degree scale, 8×8 ordered dither, one canvas pixel per cell; the camera fitted so the platter is never cut.
- Steps round 15° every 1.7s, each step landing on a stiff damped spring; nothing drawn between steps; start angle −30°. Moving across it clicks the turntable round step by step (one full turn across the panel) and leans the key light to the pointer. Cell 2–3px.
- Only on a feature card about a kind of thing the software handles (cameras in a rental inventory, a chair in a furniture marketplace, a speaker an audio app controls). Never the client's own product, never on a product page.

## 585. Photo and object scenes: shared rules
- One scene per screen, at most two per page; one moving scene per group (others hold until pointed at); shared 32px pause disc in the bottom-right corner.
- Still or nearly still at rest; never animate on scroll; drawn finished.
- It paints its own ground: put it in a plain panel, never over a dealt effect ground.
- Fallback: the plain photograph cover-cropped at its focus; the panel never stays empty.

## 586. Object GPU classes
- Print objects: high cost per frame (raymarch), only while moving near the screen; at rest one sharp frame kept; all objects on a page share 2 contexts.
- Photo prints: low, still at rest; one context each, at most 3.
- Photo scenes: low, drawn only while moved or stepping; at most 2 contexts.
- Product render: no context for stills; a "render once" still frees its context; live = 1 context, high cost growing with parts.

# Part 22 — UI mock components

## 587. UI fragments in frames
- Paste real product UI at its true size, never scaled; rewrite every name, number, subject, app and logo to the client's. Never sample text.
- Edge rule: every fragment edge keeps 24px clear or is cut by 24px or more with a fade; holds at 1440, 1280, 1024, 768. Phone: fragment placed 16px in, top 24px down.
- A width-fitted slot takes only a fragment whose minimum width fits: 324 in a 2x2 card at 1024, 256 in a span-4 card.

## 588. Fragment content
- Show the product's own subject as its users see it: code review = real red/green diff with comment and Apply; invoicing = an invoice; booking = its calendar; CI = its pipeline. Never a generic dashboard, chat or stat card as stand-in.
- Cards show parts; the product whole once, big, in the full app window.
- Gaming: no UI fragments; feature cards are open cards for what you do (one verb each) holding an in-engine shot.
- Real live UI at true size: 13px text, 12px meta, never under 11px; weights 400 and 500; real data and real app marks.
- Minimum widths: chat 140, checklist 160, slider 215, toggles 230, search 240, terminal 280, calendar 280, diff review 280, pipeline 280, stat 285, cursor 290, files 300, notification 340, code 365, document 400, window 456.
- A phone mock or UI card runs past its panel only where the panel clips it, never past the container.
- Fragment surface white on light, `#1c1d20` on dark (one step lighter than the `#151517` card); 1px border at 12%; radius 12; layered shadow only inside the panel.
- Primary button, on-switches and the product's mark are ink. The accent appears once per fragment (the row worked on, the marked date, the last bar, the dragged slider); ranges, keywords, numbers, today's dot and status chips are ink tints. Never a row of green dots.
- Real icons in their own colours on a light tile on every surface; one treatment per set (never colour beside ink marks); small inline marks beside text stay ink; glyph marks only (wordmarks illegible at tile size).

## 589. Fragment placement
- Corner: 28 to 40px from top-left, cut by right and bottom (19 of 41 sites studied).
- Rise: starts 24 to 56px down and leaves through the bottom (chat, voice, calendar).
- Right: anchored top-right; narrows on small panels rather than cutting text.
- Low stack (notifications): top at 100% − 180px, last row cut.
- Over: a second fragment over the first's lower-right edge; a cursor dialog only ever here, over a window.
- Centre: only a small control (≤ ~250x130) on a focal tile; never a window or dialog; capped at panel minus 24 a side (16 on phone).
- Fit: keeps true width on wide panels, centred with even ground both sides, narrows on small ones (no 1 to 23px sliver at 1024). Windows relayout: rows stack under 540px, sidebar goes under 420px.
- Wide: a fluid grid set wider than the panel, always running 64px+ past the right edge.
- To-edge: wrapper reaches 72px past the bottom so growing fragments (chat, doc, stat, voice) are always cut.
- Vary placements across a group: a 2x2 shows at least three; never one card layout four times.

## 590. Fragment edges and fades
- Every edge keeps 24px of ground or is cut by 24px+ (16px a side on phone).
- A cut never slices text: fade the last 64px (40px on short panels like tall cards).
- A fade never crops the point: it covers only context (row below the change, a chat's input, later paragraphs, a list's last rows). Keep the point above 100% − fade height (put the moving row near the top, e.g. the integration target third not last; lower the start; shorten the fade).
- Fade only where an edge cuts.
- Measure at 1440, 1024, 768, 390; phone places fragments 16px in both sides, cut only at the bottom.

## 591. Fragment rules (all mocks)
- One loop per card group; every other fragment holds its finished picture and plays only while the pointer is on its card. On phones, on non-tech pages and on places every fragment is held still.
- Cycle 2.5–4s, finished picture held for at most 15% of it, repeating while on screen, starting 0.6s after the fragment shows; the pointer entering its card restarts it; a "two cycles then rest" option exists. Pause button in the panel's bottom-right corner. Nothing moves under reduced motion.
- A fragment never writes words of its own: every state it shows comes from the page's own markup or options — write the client's real product content, real labels, real app names.
- Placement vocabulary: at the corner (cut by right and bottom edges with a bottom-right fade), rising (cut by the bottom edge with a bottom fade), at right, laid over another window's lower-right edge, centred (only a small control on a focal tile), fit (max width), wide (wider than the panel, cut by its edges), to the edge.
- Never centred with even ground all round; content runs out of the panel's edge so it reads as part of a bigger product. Keep the point of the loop (the clicked button, the newest item, the changed line) clear of the fade.
- Real app marks always in their own colours on light tiles (same on light and dark), one treatment for the whole set, local files; never a grey box or look-alike; use only apps the product really works with.
- On a soft lit field, never on a pattern ground.

## 592. Mock: app window (queue)
- Window dots, breadcrumb with the app's real icon, search; sidebar with counts; a list of conversations (people, subjects, status, age); the assistant takes each open row: Working, then Replied. 600×378 (compact 456px).
- Place at the corner 24–40px in, cut by right and bottom edges (bottom-right fade), or fit to show full width; responsive: rows stack name over subject under 540px, sidebar goes under 420px; no column ever sliced. Pair with the approve-click dialog over its lower-right edge.
- For product overview, support, inbox, workspace, SaaS, admin, agents. Loop about 2.6s: two queue steps.

## 593. Mock: chat with sources
- A customer's question, an answer written word by word with two sources (a real app icon and a help article), the customer's thanks and an input. 400×392.
- Rising, to the edge, fit max 400px, 32–56px down, bottom fade: input always past the bottom edge; answer and sources clear of the fade. Answer max three lines; real sources.
- Loop about 3s: typing dots 0.8s, the answer's last sentence rewritten in place in under 0.8s (never below 72% ink), sources return one by one.
- For AI assistants, support, search answers, messaging, Q&A.

## 594. Mock: approve with a click (cursor dialog)
- A drafted reply waiting for approval: text, the action it carries (a refund with amount) and two buttons; the pointer glides to the main button and clicks; it spins, reads Sent and the status turns Sent. 360×262.
- Only laid over the lower-right edge of a window (24px/24px offsets; in a split or hero frame run 40px out through the bottom, button still in view). Never alone, never centred on a ground, never cut through its buttons (the click is the point).
- Loop about 2.8s. For automation, agents, approvals, one-click actions, publishing, workflows.

## 595. Mock: notification stack
- Three notifications (assistant handing over, a person taking over, a count) with avatars and times; a new one slides in on top, the oldest leaves. 380×208.
- A short stack sits low: rising, fit max 380px, 32px in, top offset (100% − 180px), bottom fade so its third row is cut like neighbouring windows and the newest stays clear; or over a window's lower edge.
- Loop about 2.8s. For handoffs, activity, alerts, teams, status, real-time.

## 596. Mock: rules with switches
- A titled list of four rules (label, grey line, switch); one switch flips at a time (changed row takes the accent) and the count's first figure follows. 380×290.
- At corner or right (32px in, 56px down), cut by the bottom with a fade. Loop about 2.6s: two switches flip in turn; back to the page's state every six.
- For settings, permissions, rules, policies, preferences, controls.

## 597. Mock: number with a bar chart
- A dashboard card: label and period, one big number with its change, 14 daily bars (the last in the accent). Bars fall back to the previous period and rise to this one; the number stays on this period to match the copy. Optional bars cut out of the card so the effect ground shows through (then turn the panel vignette off). 420×296.
- At corner or right, cut by the bottom. Loop about 2.9s. For analytics, results, growth, reports, dashboards, KPIs.

## 598. Mock: search with a typed query
- A command bar: query types in, three results with matches in bold, selection steps down, keyboard hints at the foot. 380×280.
- Loop about 3s; extra queries one per cycle. For search, command menus, knowledge bases, navigation.

## 599. Mock: connected apps (integrations)
- A list of apps with real marks, what each does and its state; the pointer clicks Connect on one, it spins, then Connected. The default for any integrations card. 380×282.
- At corner or right 32–40px in, cut by the bottom through a row below the one that connects; on a soft ground; or over a window. Loop about 2.8s.

## 600. Mock: property panel (slider)
- A design tool's property card: icon, name, two sliders with values, a three-way switch; the first thumb glides between values; optionally it drives the effect ground beneath (e.g. grain 0.15–0.95) so the control visibly changes the picture (Figma's Texture tile). Full 288×268; compact 248×128.
- Full: rising fit max 288px, horizontally max(24px, 50% − 144px), 40px down, cut below its second slider. Compact: centred on a focal tile — the one fragment allowed in the calm middle.
- Only the figure changes while the thumb moves; words and unit stay. Loop about 3.3s. For design tools, customisation, branding, settings, editors.

## 601. Mock: voice call with an orb
- Status and timer, the assistant's orb, who's talking, captions lighting word by word, a bar with mute, waveform and end call. On dark: a live orb effect (pale nebula with specks); on light: a CSS pearl with accent and ink clouds turning slowly and a few specks. 264×336.
- Rising, to the edge, fit, 32px down, cut through its bar's lower half at most (orb, caption, waveform clear of the fade).
- Loop about 2.75s: wave runs, caption spoken word by word in under 0.8s (never below 72% ink), timer counts on. For voice, calls, AI assistants, phone support, speech.

## 602. Mock: file tiles
- A status pill over a grid of file tiles, each with its app's real mark or a plain file glyph (PDF red), a name and its app; each tile is read in turn and gets a check; the status line counts in the page's words. 440×340, fluid 300–560px.
- At corner, wide (680px), bottom-right fade: four columns cut by the right edge, rows leaving through the bottom; never centred; two columns on a phone.
- Loop about 3.2s: a wave across the grid. For imports, supported formats, uploads, documents, sync.

## 603. Mock: calendar with dates
- A month with one dated range and, under it, the dates that matter as rows (date tile, title, one line); the pointer sets the range; each row lights as its day is reached; one single date may be ringed; mark today. No Apply or Clear — it shows a plan, not a picker. 440×452, fluid 280–440px.
- Use the client's real dates. Loop about 3.2s. For dates, deadlines, rounds, booking, scheduling, planning.

## 604. Mock: code with a highlighted line
- An editor pane with two tabs, eight lines of code, one highlighted line and a one-line note on the change below; token colours for keyword, function, number, comment. 400×284.
- Loop about 3s: the highlight moves through three changed lines, a note naming each. For developer tools, code review, APIs, AI coding, docs.

## 605. Mock: code review on a diff
- One pull-request file: path with its real language mark and +/− counts, hunk header, fourteen unified-diff lines (removed red, added green, old/new numbers in the gutter), a reviewer's one-line suggestion under its line naming the change. The Apply button steps (lifted, ringed), is pressed for 140ms, spins (two turns, 0.5s); the reviewed line becomes removed with the suggestion added under it, counts update, "Applied" replaces the button; then status leaves first, the diff resets, and only then the button returns. Finished picture held about 10% of a ~3s cycle. 480×428, fluid 280–760px.
- Hunk counts must match the lines written. Every row starts with a filled gutter (changed rows red/green, others faint grey) so rows keep one left edge. The comment carries the fragment's one accent: a short 2px bar beside its text, set in from the edge to keep a gap from the red/green rows; avatar tone kept off the add/remove hues.
- Place at corner or rising, fit max 480px, 32–40px in, cut by the bottom with a fade; reviewed line, suggestion, comment and button within the top 250px; the diff runs on two more context lines so it's cut by 32px+ at every width (112px at 480px wide); a panel 400px+ tall would show the diff's end — add offset or shorten. Never cut by the right edge (the button is at the comment's right). Responsive: under 500px the hunk header starts after one gutter; under 440px one 26px gutter, rows at 11/16, function name leaves the hunk header, wrapped code hangs 2ch. File path collapses repo first (under 470px) then folders (under 340px) so the file name always shows whole. On phones give the panel 340px+.

## 606. Mock: terminal with a test run
- A terminal pane (repo, shell, branch): a command at the prompt, a thin meter, one line per test file with count and time, a blank row, a two-line summary, a status line with a green check and the run's duration, a fresh prompt with caret. 440×286, fluid 280–560px.
- Loop about 3.1s: the command retyped at 50–80ms per character; each file line arrives running (a spinner turning once per second, for 0.15s) and ticks as the meter fills; summary and green check follow while the older run scrolls up a row at a time (each departing top line fades out whole); fresh prompt; finished picture held about 13%.
- Each line a 20px row that ellipsizes, never wraps; a blank line is an empty row, never a margin. Ticks on file lines stay in ink: the status line's check is the only green and strongest mark; the meter's thin bar is the one accent.
- Rising, fit max 440px, 32–40px in and down, whole with 24px+ ground under it; never cut (the short fresh prompt can't carry a fade); not to the edge. Wide: up to 560px (path column stops at 28 characters). Under 380px test counts go; under 300px branch and parent folder go (prompt reads ~/api).

## 607. Mock: document with marks
- A page of a document (e.g. a returns policy) with marked phrases and a note beside the current one: issue kind, what's wrong, where else it appears; runs off the panel's bottom edge (a cut page, never a whole sheet floating). 440×330.
- At corner, to the edge, bottom fade, 32–40px in; first mark in the top half so its note never lands in the fade. A mark with no note stays a quiet underline.
- Loop about 3s: two marks in turn, each sweeping in with its note sliding up. For review, comments, AI checks, compliance, policies, contracts.

## 608. Mock: check list
- A titled list of five steps with a progress bar; the next step ticks (check draws, label struck) until all done; the count's first figure follows. 340×268.
- Rising, fit max 340px, 40px down: whole with 24px+ ground under it, or cut by 24px+ through its last step only (ticking steps, count and bar never in the fade).
- Loop about 3s. For onboarding, setup, tasks, launch, compliance, progress.

## 609. Mock: pipeline run
- A CI run: repo, branch, run number, total time, status chip; the commit with a Cancel button; five steps on a rail (checkout, install, test, build, deploy) each with its tool's real mark on a light tile; done steps with ink-outlined check and time; the running step with a turning accent ring and bar; waiting steps muted reading "Queued". 420×290, fluid 280–960px; rows under 680px, a row of bordered nodes with the running step's log from 680px.
- Loop about 3.4s: from the written picture (the run partly done) the running bar fills, turns done with its time, next starts, to the last; the run passes and holds 0.7s; Re-run is pressed and every step returns straight to the written picture, held 0.45s (about 13%). Only figures change; total adds the steps.
- Place whole: rising fit max 420px, 32–40px down, 24px+ ground under it (panel 350px+), no fade — never cut through the steps. Wide: at corner in a large panel (about 300px tall with log), bottom-right corner clear for pause.
- For CI/CD, deploys, developer tools, data pipelines, automation, build status.

## 610. Mock: apps around the product (second choice)
- Fourteen real app marks in a 5×3 field around the product's own mark (the 8th position), each joined by a hairline; in turn one app connects: its line lights and runs, its tile takes the accent ring, its name appears. 456×272.
- At corner, wide 560px, bottom-right fade: set wider than the panel and cut by right and bottom so it reads as part of a bigger map; on a still soft ground, never a pattern.
- Only for a platform whose point is the number of things it connects, with marks that read at 26px (glyphs, never wordmarks); otherwise use the integrations list. Loop about 2.8s: three apps in turn.

## 611. Developer-tool fragments in card panels
- Diff review: corner or rise fitted, max 480 (up to 760), 32 to 40px in, cut by the bottom with a fade; reviewed line, suggestion, comment and Apply in the top 250px; diff runs two context lines further so a 352px panel at 36px down cuts by 32px+ (never under 24px past the edge); never cut by the right edge; on phone give its panel 340px+; the file's real mark on a light tile; accent is the short bar beside the comment.
- Terminal run: rise fitted, max 440 (560 in wide panels), 32 to 40px in and down, always whole with 24px+ ground under it; never cut or faded; status line with its green check one row above the bottom; the green check is the one green and strongest mark; meter bar the one accent; ticks ink.
- Pipeline board: whole, rise fitted max 420, 32 to 40px down, 24px+ ground under, no fade; in a large panel at full width (680+) as a row of nodes with a ~300px log; bottom-right kept clear for the pause button; waiting steps say "Queued"; each step's real tool mark, one treatment; loop rests on the done state.

## 612. Dashboard app screens
- Allow quiet borders, small labels, repeated panels and tables.
- Ban heavy shadows, glass, icons in tinted squares, rainbow charts, placeholder data, text under 11px, a sidebar left on the phone, ragged rows, a thin first screen, landing-page titles and figures, a dead strip beside the canvas, colour sprawl.
- Name each screen's one question and its one finding; design empty, zero, loading and error states.

# Part 23 — Contacts, honesty and content truth

## 613. Contacts and facts
- No house number, postcode beside its town, map coordinates, register/VAT/tax number, real-format phone or tel: link in text, links or structured data.
- Nothing invented but a coined brand name and, on a place, plausible hours and prices, each marked as assumed; never an open-now line from assumed hours.
- One fact, one wording; one day given two opening-hour ranges FAILs.

## 614. What may be assumed
- Prices, address, hours and dates come from the facts given. Only two things may be assumed: a coined brand name, and on a place, plausible hours and prices for the trade, uneven and in local currency (3.60, not 4.00).
- A product or service with no price given says "Price on request" or shows none.
- Mark every assumed value and never drive an "open now" line from assumed hours.

## 615. No invented proof
- No invented reviews, ratings, review counts, quotes, testimonials, statistics, customer counts, customer names, portraits, clients, awards, press lines or products.
- Customer logos only for real, named customers that may be shown. A real tool keeps its real icon in its own colours, never a drawn imitation.
- Without proof: a strip of plain given facts, or nothing.

## 616. Credits and each fact once
- Credits: one short line at the end of the footer naming only the sources, never photographers ("Photographs via Unsplash and Wikimedia Commons"), max 110 characters, one line from 1024px, linking to the credits list. Never one credit link per photo (18 to 20 credit links read as a credit wall). Map data credits join that line.
- A page showing real logos adds "Product names and logos are trademarks of their owners".
- Each fact (opening time, price, address) has one value and one wording, repeated word for word only where it belongs (hero, visit panel, phone sheet, close, footer); never two hours for one day.

## 617. Contacts: address
- Street and district only ("Elmgatan, Malmö-Möllevången"); never a house number, postcode or coordinates.
- One street address per page (visit block and footer, also at 390px), never readable only on a sign in a photo. Several shops: each name, then its street. A by-appointment studio says so.
- No street given: print district only ("Eimsbüttel, Hamburg"), or the town if no district; never invent a street or number.

## 618. Contacts: maps
- No map loads with the page; never an iframe.
- "Get directions" opens an OpenStreetMap search for street + district, no coordinates, no route; on phone the address opens the same search.
- No street: link says "See the area" and searches district + town. Only a town: no map link and no directions button at all.
- A drawn map only for a given street (still image, pin on the street line, never on a building); never a real map for a tradesperson's home street.

## 619. Contacts: phone, imprint, email, web, social
- Phone: none unless given. No number, no tel: link, no Call button; a "Request a call" form may stand in.
- No imprint page and no company details (register number, VAT/tax id, company number, managing director, court). Legal row = brand, current year, Privacy, Terms, credits line; Imprint link only when real company details are given.
- Email: a form, or an "Email us" button with a placeholder-domain mailto. Never print an email address, a domain or a social handle. Social links stay empty unless accounts are given.

## 620. Street map of the place (visit/contact; every kind with a door)
- Show the real streets around the place as a map app would, in page colours; a contour pattern standing in for a map was judged a fake drawing.
- Bake once from open map data: streets in four classes, water (sea from coastlines), parks, rails/trams, up to 14 street names along the straightest part of each street; about 55KB (18KB gzipped) for 3×2km of city.
- Fit pin, walk and both names into the free part of the frame (right of the card from 900px wide; under 900px the card sits below and the map takes full width), never closer than about 1m per pixel; names on the side the walk does not leave by (above/below on phones). Street names only where they fit their street and clear every other label.
- Light pages: white streets with a hairline casing on land one step darker than the page. Dark pages: lighter streets on land one step lighter. Water and parks keep a natural blue and green mixed into the land.
- Walk route only on tech pages whose brief names a station (nearest station 150m–1.6km away), with minutes at 80m per minute; on hover/focus of the directions link the walk draws from station to door and the pin's halo answers once. On place/other pages: no walk, no minutes chip, nothing moves. Nothing moves at rest or on scroll.
- Pin sits on the street line, never on a building. The card states the walk in words ("5 minutes on foot from … tram stop") and names street and district only. Directions open a search for street + district, never coordinates or a route link; coordinates never appear on the page.
- The map-data credit joins the footer's one credits line, never on or under the map.
- No data or no street given in the brief: no map — the visit shows its photograph. Never a contour or dot fallback as a map.

# Part 24 — Performance and accessibility

## 621. Performance budgets (WARN above / FAIL above)
- Transfer (text gzipped): 1500 / 3000 KiB.
- Images total: 1200 / 2400 KiB; largest single image 350 / 700 KiB.
- JS parsed: 450 / 900 KiB; CSS: 120 / 250 KiB.
- Requests: 60 / 110.
- Font families 2 / 3; font files 4 / 6; font bytes 160 / 320 KiB.
- img without width and height (or aspect-ratio): 1-3 WARN, 4+ FAIL.
- img below the fold not lazy: 1-3 WARN, 4+ FAIL.
- Oversized images (natural over 2.2x the shown width): 1-3 WARN, 4+ FAIL; upscaled (natural under 0.75x shown) warns.
- Photos as CSS/SVG background below the fold: 1-3 WARN, 4+ FAIL.
- Live WebGL contexts: FAIL above 4.
- Long tasks / blocking time (median, WebGL off): 8 / 1.5 s WARN, 20 / 4 s FAIL.
- FCP / LCP median: 2.5 / 4.5 s WARN, 4.5 / 8 s FAIL.
- Layout shift median: 0.1 WARN, 0.25 FAIL.
- Effect module loaded but never mounted: 1-2 WARN, 3+ FAIL.
- Any broken request or sideways overflow: FAIL.

## 622. Image delivery
- AVIF or WebP through srcset at 2x the shown width, never more (full-bleed hero 2880w at 1440, 780w at 390).
- Hero under 400 KiB; every other photograph under 250 KiB.
- width and height (or aspect-ratio) on every image, an alt-ground fill while loading.
- Lazy and decoding async below the first screen, never lazy in it; the hero eager with `fetchpriority high`.
- A photo below the fold is an img, not a CSS background.
- On a slow mobile line (1.6 Mbit/s, 400 ms) a photo frame still empty 1 s after coming on screen FAILs when over 400 KB, over twice a retina phone's width, or never loads.
- A phone photo 3x or more wider than drawn with no srcset WARNs.

## 623. Image weight caps
- Every non-hero picture lazy-loaded, async-decoded, width and height set, sizes equal to the shown width. A photo in a nav menu or tab panel is not lazy.
- File caps: hero 400KB, any other 250KB; page image total about 2,400KiB max. Provide a 1200px-wide WebP minimum; optional low-quality colour placeholder (24px colours) behind the picture.
- A full-bleed band may use the largest file only within the 250KB cap.

## 624. Fonts and scripts
- Preload the regular and the display weight, `font-display swap`, request only used weights.
- CLS under 0.1: reserve space for images, nav and counters.
- Animate transform and opacity (colours too); background-position only on small text spans; never height, padding or layout.
- Deferred modules; import only modules the page mounts.

## 625. Motion layer weight
- Motion layer small (about 4KB CSS + 4KB JS gzipped); one intersection observer per feature.

## 626. WebGL context budget
- At most 4 live WebGL contexts per page at once (a laptop's integrated GPU shares about 2GB with everything; too many canvases crash it), counting the effect, moments' canvases, scenes, objects and any live product render.
- All print objects share 2 live contexts (so baked grounds plus one effect stay within 3); photo scenes at most 2; photo prints at most 3 (a fourth waits showing its still; keep such a page to 3 live); product render 0 (stills) or 1 (live); a big scene at most 1; a liquid-hover moment 1.
- Only things that move hold a context. Stills render once and free their context. Effect-ground libraries free idle off-screen contexts first beyond a high ceiling (14).

## 627. Card ground performance limits
- Still card grounds drawn once near the screen at up to 2 device pixels, kept as images, contexts freed one at a time.
- A live driven ground at 1 device pixel, drawing only on change.
- One live context type per page (hero ground, driven ground, voice orb, hover light, or object); library cap 3 live contexts; page cap 4 live at once.
- Objects mount near screen, destroyed off screen; one per card group; never two objects plus a moving ground in one view; at most 1 CSS px per pixel (0.75 when large), ~1.5 megapixels.

## 628. Resolution and frame-rate caps
- Per-pixel and raymarched work at 1 sample per CSS pixel at most (0.75 when the canvas is large, past about 0.48–1 megapixel) and about 1.5 megapixels per canvas, whatever the device pixel ratio; device pixel ratio capped at 1.5 for heavy work (effect grounds generally 1.75 unless crisp pixels are needed).
- Noise, particles and ray marching at half resolution and 30fps or less. A noise ground is one baked texture drifting on time.
- Dither runs at one texel per cell, its canvas one pixel per cell, scaled up crisp. Dither object at 20fps; turntable and sequence wipes at 30fps max.
- Halftone and engraving prints may render up to 2 canvas px per CSS px for sharp dots/lines, still under 1.5MP. Each pixel reads the photograph 2–5 times from mipmaps; no loops.
- A render at rest is redrawn once at up to one texel per canvas pixel (1.2 megatexels max) so the picture that stays is sharp. Slow frames lower texels first, then march steps, then stop the turn.
- Still grounds drawn at up to 2 device pixels; a ground a fragment drives stays live near the screen only, at 1 device pixel.
- No MSAA in scene canvases (a soft outer pixel instead); static buffers; nothing per frame on the CPU.

## 629. GPU lifecycle
- Everything pauses off screen and in a hidden tab; scene and print contexts freed 1.5s after leaving the screen (objects beyond 40% of a screen away) and recreated before return.
- A button-fill context is held only while pointed at and freed 4s later; a search glow only while focused.
- Shader compile speed: keep shaders small; avoid helpers called many times (a helper called 16 times took 40s to compile on one Windows GPU path); loops counted by a uniform avoid inlining blow-ups.
- Never use a GLSL ES reserved word (flat, smooth, sample, filter, input, output…) as a name: real laptop GPUs reject what CPU renderers compile; a struct field named "flat" once left a hero empty.

## 630. Always a picture
- Every WebGL piece shows a poster first and keeps a still fallback when WebGL2 is missing, the context is lost, the shader fails to compile/link, or the first frame comes out empty/one flat colour. Effect grounds fall back to a CSS picture in the same colours. A panel is never empty.

## 631. Accessibility basics
- Every control has a name; icon-only buttons get an `aria-label` in the page language.
- Content photographs have alt saying what they show; decorative `alt=""`; a drawn mock `role="img"` with `aria-label`.
- Headings step down one level at a time (h1, h2, h3).
- No `tabindex` above 0.
- Focus ring 2px in the action colour, 3:1 on the ground, shown at once, never animated; a focused control is never hidden under the fixed header.
- Menu button carries `aria-expanded`.
- Tap targets 44px tall outside running text.

## 632. Accessibility of effects and motion
- Text on effects, photographs or grounds at 4.5:1 (3:1 for display text); reading text on brand bands 7:1; ground palettes keep ink 7:1 and muted 4.5:1.
- Every loop running on its own over about 5s has a pause button (WCAG 2.2.2); reduced motion holds one state and hides pause buttons.
- Under reduced motion: effects show one still frame; objects one still, context freed at once, no hover, click shows the step at once; photo prints and scenes stay still but still answer the pointer, without easing.
- Interactive objects are focusable buttons with visible focus and Enter/Space actions; slider-like reveals are keyboard-operable (arrows, Shift, Home, End).
- Accessible names describe what the picture shows in plain words, never "render" or "illustration".
- Pointer play off on touch; touch equivalents for hover prints (tap holds 1.6s; drag to scrub).
- All words are real text in reading order; scenes and moments readable without script.
- Animated tab indicator, switches and underlines snap under reduced motion; focus rings never animate.

# Part 25 — Quality gate and pre-ship checklist

## 633. Check: first screen
- Says what is sold, for whom or where, with one hard fact; the hero fills it alone at every width, its main button inside it.

## 634. Check: screens and sections
- Every section 1 or 2 screens, h2 first and top-aligned, no neighbour's heading or picture in its tile, nothing sparse, no section half empty.

## 635. Check: edges
- Every block on the wrap lines or grid columns, nothing out to one side, no sideways scroll.

## 636. Check: visuals
- Every visual draws at 1440, 1024, 768 and 390; a refused effect shows its still fallback.
- No caption; credits in one footer line; no placeholder, sample note or printed .example address.

## 637. Check: kind fit
- Outside tech no effect ground, print or scene; the product big, whole in three sections at most, a new picture each; each named asset in its slot; real icons in their own colours; flat grounds on other; a place deals two different compositions and one type moment.

## 638. Check: motion
- Everything answers the pointer, nothing tilts; hero enters once; one or two moments; loops 2.5-4 s; pause past 5 s; reduced motion rests; at most four contexts.

## 639. Check: keyboard and head
- Every control named, alt on pictures, visible labels, headings one level at a time, no `tabindex` above 0; Tab reaches the skip link first, its ring shows at once and never under the header; the menu button says its state; lang, title, description and share tags.

## 640. Check: system and copy
- One button pair, one card style, one radius scale, one link look; two boxes deep at most; one heading scale, faces loaded; text contrast.
- Headings name things, buttons verb + object, at most two hero actions, one action twice a screen at most, grey half its own sentence, one fact one wording, links land, forms send, errors under fields, no slop.

## 641. Check: widths
- Check 1440, 1024, 820, 768, 390 and 320; first-screen sweep at 1280, 1152, 1024, 896, 768.
- Read every screenshot by eye: nothing tilted, staggered, cut or overlapping.

## 642. Check: copy
- Count the countable tells; fix every failure; fix each warning or keep it deliberately with a reason.
- Rival's-name test: put a rival's name, or the same trade in another town, into the h1, sub-line and each heading; any line still true says nothing about this client; rewrite from the fact sheet.
- Sameness across pages: read first headings of all pages side by side; a shared cadence or joke is a tic; break it.
- Read aloud as the client; cut every sentence they would not say about themselves.
- Over-correction check: look for the habit that replaced the one removed ("rather than" multiplying, all fragments, everything in pairs, a deleted joke with nothing in its place). A rule that made a sentence worse is broken on purpose.
- Fresh-reader test: give only the page text and ask what this is, who it is for, why this over the alternative, what it costs, what would make them hesitate, and which three lines sound like any other website. Never iterate to beat an AI detector.

## 643. Measured thresholds
- Tap size: targets outside running text under 44px tall WARN; under 32px tall or 24px wide with another target under 8px away FAIL.
- Visual empty: under 6 colours, 99.8% one colour (canvas or mount 98%) FAILs; 6+ colours with under 0.2% detail is a smooth gradient: WARN; a picture left under 0.1 opacity after scrolling FAILs.
- Dark card ground behind UI under 3:1 WARNs.
- Text contrast on plain ground: body 7:1, captions/labels/muted 4.5:1, large type 4.5 and 3.
- Running text under 16px WARNs.
- Copy actions: 2 in the hero, 10 labels, one wording.
- Judge section rhythm at 1440x900, 768x1024 (and 820x1180) and 390x844.

## 644. Copy severity levels
- FAIL: residue, leftover markers or markdown, slop words, stock phrases, any device at twice its budget plus one or more, a coined default brand name.
- WARN: over budget, riders, puffery, reveals, repeated promises, proof figures, em dashes over 2, exclamation marks, cast names, footer sign-offs, stale year, stat strips, eyebrows 5+, step numbers 6+, sentence rhythm.

## 645. Gate discipline
- Fix every FAIL; fix copy WARNs or justify them.
- At most three fix rounds; at most 5 waivers (more is itself a FAIL: fix instead); a waiver needs a reason of 12+ characters.
- Treat a missing hero entrance and a page with no moment as blocking.
