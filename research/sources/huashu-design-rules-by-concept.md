# Design Rules by Concept

Distilled from the Huashu Design collection (English port), with all Chinese source material translated. Each concept is followed by its rules; exact values are kept wherever the source gives them.

# Part 1 — Philosophy & Stance

## 1. Designer identity
- Act as a designer, not a programmer who writes HTML; HTML is only the medium (like Figma, AE, InDesign). The delivery standard defines you, not the tool.
- Hold the bar: output nobody can tell was made by AI. Aim for "which studio made this?", not "decent, for AI".
- Commit to hitting that bar before starting; the limit is usually commitment, not capability.
- Draw on the methods and taste of top designers and studios.

## 2. Know your own default aesthetic
- Recognize that, unconstrained, you drift to: warm cream backgrounds, high-contrast serif headlines, terracotta accents, all-caps eyebrows, 01/02/03 numbering (Claude's own palette, one of the most common 2026 AI looks).
- Grow every design out of the subject instead of falling back to this home look, every single time.
- Never treat Anthropic/Claude brand colors as a "safe default".

## 3. Work as a studio (roles)
- Art Director: set direction, judge taste, kill what isn't good enough (absent → "everything's okay" mediocrity).
- Brand Researcher: find real assets (logo, product shots, UI), understand the brand's temperament (absent → brand drawn from imagination, fake at a glance).
- Visual Designer: layout, color, typography, hierarchy (absent → elements piled up with no order).
- Motion Designer: timing, easing, rhythm (absent → stiff, PPT-transition-like animation).
- Front-End Engineer: implement precisely (absent → great mockup, warped build).
- Copywriter: every sentence serves the design (absent → Lorem ipsum / "Title Text" placeholders).
- Change the lead role when the medium changes: slides must not look like web pages, animation must not look like a dashboard, an app prototype must not look like a manual. Decide who leads before starting.

## 4. Breadth of exploration
- Think as long as needed; quality depends on how many options you ran through and killed.
- "One thousand no's for every yes": many candidates, few deliverables.

## 5. Context over invention
- Grow hi-fi design from existing context (design system, codebase, shipped product, brand assets, loved references); drawing from thin air is the last resort and always produces generic work.
- Treat context quality as the ceiling of design quality; 10 minutes collecting context beats 1 hour of hi-fi from nothing.
- When there is no context, ask the user before forcing through.
- Expect brand-from-zero work to land at ~60–65 points; existing-context work is the difference between a 65- and a 90-point design.

## 6. Form grows from content
- Derive form from content, not from a style library; the library is ammunition and starting points, not quota or dogma.
- When the user supplies content, a brand or references, grow the design from there; don't force-fit the library.
- At delivery, write one line on "where the form grew out of the content".

## 7. Restraint and boldness
- Spend boldness in one place: one element to be remembered, everything around it quiet. One detail at 120%, the rest at 80%.
- "Check the mirror before leaving the house and take one accessory off."
- When you think "adding this would look nicer", treat it as a sign of AI slop; do the most minimal version first and add only when the user asks.
- Make structural elements (borders, numbering, dividers, small labels) carry information; ask what each says before adding it.

## 8. Add options, not bans
- When output feels monotonous or "too AI", add candidates and references first; don't reach for bans first.
- Constraints only remove options; removing options doesn't produce good design.
- Any new ban must first survive a round of blind picks.

## 9. Honesty
- Never fabricate: no invented data, testimonials, quotes, logo walls, typeface names or product facts.
- When you don't know, say so, ask, or leave a placeholder.
- Rather go without than go bad: an inferior asset is a deduction; empty is better.
- Never claim you have seen a reference you haven't.

## 10. User authority
- When a reviewer's high score conflicts with the user's choice, the user wins.
- On such a conflict, list the observable differences (color, density, materials, structure), ask exactly one question, record the answer as a preference.
- When the current project conflicts with a recorded lesson, the project wins; then fix the lesson.

# Part 2 — Workflow

## 11. Kickoff (every design task)
- Before starting, recall this user's verbatim preferences and past lessons for the topic.
- Review what recent deliveries looked like (last 8) and proactively steer away from the recurring few.
- Determine the available material tier before designing.
- Treat none of these as blocking: no records → continue.
- Respect a preference's scope: one noted "only for certain material types" must not become a default for every design.

## 12. Routing by medium
- Web pages, landing pages, official sites, dashboards, desktop UI prototypes → web rules.
- Slides, PPT, pitch decks, courseware, reports → deck rules.
- Infographics, data viz, long-form images → infographic rules.
- Xiaohongshu (RED) image-text posts, covers, carousels → Xiaohongshu rules.
- Mobile app / iOS prototypes → app-prototype rules.
- Animation, video, launch films, product demos, narrated video → motion rules.
- Critique / scoring / "does it look good" → critique method.
- Pure mechanical operations (HTML→PDF/PPTX, screenshots, bug fixes, text edits) → no three-direction gate.
- Stack signals when several hit: "coffee-themed PPT" = deck rules + three-direction gate; coffee is a subject, not a brand — no logo hunt.

## 13. Stage 0 · Fact verification before assumption
- Whenever the task touches existence, release status, version or specs of a specific product, technology, event or person, web-search to verify FIRST, before asking questions.
- Write verified facts into a product-facts file; if search can't confirm, ask the user.
- The moment "I remember X hasn't launched" or "X should be at vN" arises, stop and search (cost ~10 seconds vs 1–2 hours of rework; e.g. asserting DJI Pocket 4 "hasn't launched" when it had launched 4 days earlier cost 2 hours).
- Never make claims from training memory.

## 14. Stage 1 · Understand the requirement
- Don't re-ask anything already asked in the three-direction phase; new tasks that skipped the gate get one round of questions; small fixes skip questions.

## 15. Stage 2 · Explore resources, extract core assets
- Read the design system, links, screenshots, code; run the Core Asset Protocol for specific brands.
- Confirm before starting: physical products have product photos; digital products have logos and UI screenshots; colors extracted from real HTML/SVG. If anything is missing, stop and fill the gap.

## 16. Stage 3 · The five form questions (before each page, screen or shot)
- Narrative role: hero / transition / data / quote / ending?
- Viewer distance: 10cm phone / 1m laptop / 10m projection? (determines font size and density)
- Visual temperature: quiet / excited / calm / authoritative / gentle / sad?
- Capacity estimate: sketch 3 five-second thumbnails; check the content actually fits.
- Visual motif: what element, structure or metaphor is unique to this content and would appear for no other subject? If you can't answer, you're still drawing straws from style labels.
- Only after answering, state the design system (color, type, layout rhythm, component patterns); the system serves the answers.
- Checkpoint: say the five answers + system out loud and wait for the user's nod before writing code.

## 17. Stage 4 · Project folder
- Put the main HTML and needed assets in one project folder; don't bulk-copy >20 files.
- Save into the project directory, not Downloads; direction drafts go in a design-demos subfolder.
- Use descriptive filenames ("Landing Page.html"); copy the old version (v2) before a major rework.
- Split a single file >1000 lines into multiple components.

## 18. Stage 5 · Alignment pass (assumptions + placeholders, 5–15 minutes)
- At the top of the HTML, write assumptions + reasoning + unresolved questions like a junior reporting to a manager (audience, tone with its basis in the user's words, main flow, intended colors, open data/image questions).
- Build structure with labeled placeholders ("[Main title spot]", "[CTA button]").
- End with: "if the direction is wrong, now is the lowest-cost time to change."
- Checkpoint: show the user early (even gray blocks with labels), wait for feedback before writing components.

## 19. Stage 6 · Full pass
- Fill placeholders with real components, make variations, add Tweaks.
- Show the user again halfway; don't wait until fully done.

## 20. Stage 7 · Detail polish
- Micro-adjust font size, spacing, contrast; tune animation timing; handle edge cases; refine the Tweaks panel.

## 21. Stage 8 · Verify
- Screenshot, check console errors, run the design check (red lights must be fixed, yellow lights removed).
- Checkpoint: eyeball it in a real browser yourself before delivery — AI-written interactions are often buggy.

## 22. Stage 9 · Deliver and feed back
- Keep the summary extremely short: caveats + next steps only (e.g. "page 4 data is fake, awaiting real data"; suggest opening and reporting which page/spot is off).
- Don't list every page's content, repeat the tech used, or praise your own design.
- Log the delivered look into the look ledger; harvest lessons worth remembering.

## 23. Checkpoint principle
- At each checkpoint, stop, say "I've done X, next I plan Y — confirm?" and actually wait.
- "Continue" authorizes moving to the next step, not skipping the gate inside the current one.
- Fixing a misunderstanding early is ~100× cheaper than late; no heroic one-shot attempts.

## 24. Exception handling
- Requirement too vague: list 3 possible directions (e.g. landing page / dashboard / product detail) to pick — don't fire 10 questions.
- "Stop asking, just do it": skip questions (fill assumptions), but still run the three-direction gate; only on explicit "don't show three versions / one is enough" drop to 1 main + 1 variant, recording the verbatim words.
- Reference images conflict with brand specs: stop, name the specific contradiction ("screenshot is serif, spec says sans"), let the user pick.
- Starter components fail: check known errors, else downgrade to pure HTML+CSS.
- Time pressure (<30 minutes): skip the alignment pass, single option, label delivery "not early-confirmed".
- Restraint vs product information density: when the selling point is AI, data or context-awareness (dashboard, tracker, copilot, health, expense tracking), go high-density — at least 3 differentiated, content-bearing pieces of information per screen; decorative icons still out.
- Off-script events: first tell the user in one sentence what happened, then handle; never decide silently.

## 25. Asking questions
- Ask exactly one round per project; in gated tasks at most 3 questions + one request for all reference materials.
- Pick the questions that most affect the outcome; don't ask everything; infer what you can and note the basis.
- List all questions at once for batch answering; never one-by-one back-and-forth.
- Must ask: new tasks, vague tasks, no design context, single vague requirement. May skip: small fixes, follow-ups, clear PRD + screenshots + context.
- If the user doesn't respond, fill assumptions with best judgment (marked as assumptions) and keep going; replace follow-up questions with something visible.
- Use a markdown checklist when no structured-question UI exists.

## 26. Must-ask question bank (5 categories)
- Design context (most important): existing design system / UI kit / component library and where; brand guidelines, color/type specs; reference screenshots; codebase.
- If "none": help find (project directory, reference brands); if still none say "I'll work from generic intuition, which usually doesn't match your brand — provide references first?"
- Variation dimensions: beyond the three directions, which dimensions to vary (don't ask how many directions — fixed at three).
- Fidelity and scope: wireframe / mockup / full hi-fi with real data; one screen / one flow / whole product; must-include elements.
- Tweaks: which parameters to adjust live (color / font size / spacing / layout / copy / feature flag); will the user keep tweaking after.
- Task-specific: at least 4 details. Landing page: conversion action, primary audience, competitor references, who provides copy. iOS onboarding: number of steps, user actions, skip path, target retention. Animation: duration, final use (video/website/social), rhythm (fast/slow/segmented), must-appear keyframes.

## 27. Handling uncertainty
- Don't know how: be honest, ask, or placeholder — don't fabricate.
- Contradictory description: point it out; let the user pick.
- Task too big: break into steps, show the first step, then proceed.
- Technically difficult effect: state the boundary, offer alternatives.

## 28. Constrained / weak-runtime degradation
- No parallelism → build directions serially; before each, read only the spec and its own direction card; don't reference already-built versions.
- Still tight → 1 full main version + 2 lightweight variants (first screen or one page only), still writing all three direction cards; each variant follows its own card ("cards are cheap, reskins are expensive").
- Read only the rules for the current medium.
- Decks: deliver 2 representative pages first, batch the rest after direction confirmation.
- Turn checkpoint Q&A into an assumption list inside the output; still write gate files.
- Degrading sacrifices process only — never the real-asset protocol, the readability floors, or the three-direction gate.

## 29. Gate files (checkpoint = file; missing file = step not done)
- Brand spec: required for any design involving a specific brand or product.
- Direction-approved record: which versions were shown, screenshot paths, the user's verbatim pick — required before implementation; hard-blocked before rendering any film ≥45s.
- Director's notes (storyboard cards + visual density clauses): required before any animation ≥20s.
- Skipping must be explicitly said by the user and written into the corresponding gate file.

# Part 3 — Gathering Design Context

## 30. Context priority (high → low)
- 1 User's design system / UI kit (tokens, type specs, icon system) — best case.
- 2 User's codebase: read theme/colors/tokens/variables files, specific components (Button, Card), layout scaffold, global stylesheets.
- 3 User's released product: screenshot it (e.g. 1920×1080) or have user provide screenshots.
- 4 Brand guidelines / logo / marketing materials / slide templates.
- 5 Competitor reference: get the URL or screenshot; never work from a vague training-data impression.
- 6 Known design systems as fallback: Apple HIG, Material Design 3, Radix Colors, shadcn/ui, Tailwind default palette — tell the user it's a starting point, not final.

## 31. Reading context
- List file structure first; find style/theme/component files.
- Read token files and lift exact hex/px values; read 2–3 representative components (hover, shadow, border, padding patterns); read the global stylesheet (resets, font loading).
- Trust code more than Figma/screenshots.
- Copy exact values (hex, spacing scale, font stack, radius); never redraw from memory.
- You've truly lifted context only after reading 30+ specific values; don't glance and work from impression.
- Codebase size: <50 files read all; 50–500 focus on components dir, all style/token/theme files, 2–3 full-page components; >500 let the user specify focus — seek accuracy, not completeness.
- Figma links: don't expect direct conversion; ask for screenshots + specific color/spacing values or code export; tell the user you can see visuals but can't extract precise values from screenshots.
- When user says "none": ask about previous project designs, company marketing site colors/type, logo style, admired products.

## 32. Vocalize the system
- Before building, state the extracted system: colors (with source file), typography (display/body/mono), spacing scale (e.g. 4, 8, 12, 16, 24, 32, 48, 64), shadow patterns (e.g. `0 1px 2px rgba(0,0,0,0.04)` subtle card, `0 10px 40px rgba(0,0,0,0.1)` elevated modal), radii (e.g. small 4px, cards 12px, buttons 8px), component vocabulary; wait for confirmation.
- Example statement: primary + background + accent with sources, display + body fonts, rhythm, imagery plan, "at most 2 background colors".

## 33. Designing from nothing (fallback)
- Warn explicitly: output will "look okay but lack uniqueness"; offer to collect references first.
- If proceeding: pick a clear aesthetic direction (brutally minimal, editorial/magazine, brutalist/raw, organic/natural, luxury/refined, playful/toy, retro-futuristic, soft/pastel) and tell the user.
- Use Radix Colors for palette, shadcn/ui for component vocabulary, Tailwind spacing (multiples of 4) as skeleton.
- Choose a distinctive font pairing, never Inter/Roboto: Instrument Serif + Geist Sans; Cormorant Garamond + Inter Tight; Bricolage Grotesque + Söhne (paid); Fraunces + Work Sans (Fraunces already overused); JetBrains Mono + Geist Sans (technical).
- Record every key decision with reasoning in HTML comments (e.g. primary in oklch with rationale, display/body choice, "no gradients — committed to minimal", spacing 8px base, 8/13/21/34).

# Part 4 — Core Asset Protocol (brands & products)

## 34. Triggers
- Trigger ① making materials for a brand (Stripe, Linear, Anthropic, Notion, DJI, the user's own company…), whether or not the user supplied materials.
- Trigger ② any recognizable product or brand appearing in the design (comparisons, rankings, reviews, introductions) — the most often missed.
- Fetch as many official logos as there are products named; never "use what's there, skip what's not".
- A generic subject (coffee, history, fitness) is not a brand — no logo hunt.
- Precondition: verify the brand/product exists and its status first.

## 35. Assets over specs (recognition ranking)
- Logo: highest recognition — required for every brand.
- Product image/render: extremely high — required for physical products.
- UI screenshots: extremely high — required for digital products.
- Color values: medium, auxiliary (often clash when the first three are absent).
- Fonts: low, auxiliary.
- Character keywords: low, for self-check.
- Violations: extracting only colors + fonts without logo/product/UI; substituting CSS silhouettes or hand-drawn SVG for real product images; forcing through without telling the user when assets can't be found.
- Better to stop and ask for assets than fill with generic content.

## 36. Five steps (never silently skipped)
- 1 Ask: list the whole asset checklist at once, by priority — logo (SVG/hi-res PNG), product image/official render, UI screenshots, color list (HEX/RGB), font list (display/body), brand guidelines PDF / Figma / brand site link. Don't just ask "do you have brand guidelines?".
- 2 Search official channels: logo at /brand, /press, /press-kit, brand.<domain>, inline header SVG; product images on product detail hero + gallery, launch film frames, press releases; UI on App Store/Google Play, site screenshots, demo video frames; colors in inline CSS / Tailwind config / guidelines PDF; fonts via stylesheet links / guidelines. Fallback searches: "<brand> logo download SVG", "<brand> press kit", "<brand> <product> official renders", "<brand> app screenshots".
- 3 Download with three fallback paths per type. Logo order: icon aggregation sources first for digital/SaaS/AI products (highest hit rate; light/dark + wordmark; monochrome glyph recolorable) → standalone official file/brand page → inline SVG extracted from homepage → site favicon at 256px → official social avatar (400×400/800×800). Don't give up after one static path; most sites are SPAs returning empty shells.
- Verify each downloaded logo is a real SVG/PNG (not a ~106-byte placeholder or HTML shell; SVG must start with `<svg`).
- Product images order: official product page hero (usually 2000px+) → press kit → launch video frames → Wikimedia Commons → AI generation from the real product image as reference; never hand-draw with CSS/SVG.
- UI screenshots: store screenshots (may be mockups — compare), official screenshots section, demo video frames, official launch posts, the real interface if the user has an account.
- 4 Verify + extract: logo — exists, opens, at least two versions (dark/light backgrounds), transparent background; product image — at least one 2000px+, cutout or clean background, multiple angles (main, detail, scene); UI — real resolution (1x/2x), latest version, no user-data contamination; colors — tally hex values across real assets, top 20, filter black/white/gray.
- Beware demo-brand contamination: a product screenshot may show a demo customer's brand color (e.g. a tool demoing a tea brand's red) — when two strong colors appear, distinguish them.
- Recognize brand facets: marketing-site colors can differ from product-UI colors (e.g. warm beige + orange site vs charcoal + lime UI); both real — pick the facet for the delivery scenario.
- 5 Freeze into a brand spec covering: collection date, sources, completeness (complete/partial/inferred); logo (main, reverse version, use cases, forbidden distortions: no stretching/recoloring/outlines); product images (main view e.g. 2000×1500, details, scene, use cases); UI screenshots; palette (primary/background/ink/accent with source, forbidden colors); typography (display/body/mono); signature details (the "120%" ones); restricted zones (e.g. "doesn't use blue"); 3–5 character keywords.

## 37. Execution discipline after the spec
- Reference asset files from the spec; never substitute CSS silhouettes / hand-drawn SVG.
- Use the logo as an image of the real file, never redrawn; same for product images.
- Inject colors as CSS variables (`--brand-*`) from the spec and use only those; adding an ad-hoc color requires changing the spec first ("consistency by structure, not willpower").

## 38. "5-10-2-8" asset quality gate (non-logo assets)
- Search 5 rounds across channels (official site, press kit, social, video frames, Wikimedia, account screenshots); don't use first-page results.
- Gather at least 10 candidates before filtering.
- Pick 2 good ones; using everything = visual overload.
- Each must score ≥8/10; below 8, don't use — use an honest placeholder (gray block + label) or reference-based AI generation.
- Score on: resolution ≥2000px (≥3000px for print/large screen); copyright clarity (official > public domain > free stock > suspected stolen = 0); fit with brand character keywords; light/composition/style consistency between the 2; standalone narrative ability (not decoration).
- 8 is the floor for "the other 80%"; hero assets need 9–10. A 7-point asset is a deduction.
- Logo exception: if it exists you must use it, regardless of score — even a 6-point logo is 10× better than none.

## 39. Failure fallbacks
- Logo unfindable: stop and ask the user.
- Physical product image unfindable: reference-based AI generation → ask the user → honest placeholder marked "product image pending".
- Digital UI unfindable: ask for screenshots from their account → official demo video frames; don't pad with a mockup generator.
- Colors unfindable: sample colors from the subject and real photos in the direction cards, assumptions flagged.
- Forbidden: silently forcing through with CSS silhouettes / generic gradients.

## 40. Cost logic
- Protocol ≈ 30 minutes (logo 5 + 3–5 product/UI images 10 + colors 5 + spec 10) vs 1–2 hours rework or restart when skipped.
- Anti-examples: guessing a brand is orange from memory when it's #1783FF blue (full rework); mistaking a demo brand's red for the product's color; launch animation with no logo or product shot → generic black + orange tech animation with zero recognition; colors never frozen → off-by-a-bit hex by page 3; five-product comparison deck with zero logos fetched.

# Part 5 — The Three-Direction Gate

## 41. Gate rules
- Trigger 100% for any task producing new visual design; no exemption for specified styles or brands.
- Show three directions as real drafts; execute only after the user picks.
- Present and stop — end the turn and wait, including in unattended sessions.
- A style word narrows interpretation space, it doesn't transfer the choice: "Apple style" → three interpretations within the Apple context ("a context, not a design").
- Only exemptions (record verbatim words/reason): user explicitly says skip this session; iterations after a direction was picked in the same project; non-design mechanical operations.
- Never let the user pick a style from words alone; a choice made before visuals exist is invalid.

## 42. Why (lessons from blind tests)
- Reskins fail: three versions sharing one skeleton with swapped colors/fonts are spotted at a glance — differences must land in layout structure / information organization, not palette.
- Forced big-idea metaphors fail: pages became filing cabinets, library cards, subway maps, prescription slips; the subway map recurred across unrelated briefs; lost 3 of 4.
- Too many bans fail: capping warm-paper serif and flagging look families pushed all three into pale cool tidy grids — "too tidy, too boring"; lost both briefs. The approved versions under the old way were dark + single accent and warm-paper serif.
- More options won: two candidates per logic, thumbnails first, specimens seen, references screenshotted — won both briefs ("clearly better this time").

## 43. Phase 1 · Brief + references up front
- The project's one round of questions, at most 3: audience / core message / emotional tone / output format.
- In the same round ask for all reference material: project name, logo / brand colors / VI / type spec, any site or screenshot with "exactly this feeling"; if none, "your call" settles it.
- No response → best-judgment assumptions, marked, keep moving.
- Concrete brand/product named → also run the Core Asset Protocol; all three directions share the same real assets and differ in interpretation.

## 44. Phase 2 · Consultant-style restatement
- Restate essential need, audience, scenario, emotional tone, and unspoken expectations.
- End with "I'll build 3 real versions in different directions for you to see" — never "which direction do you want".

## 45. Phase 3 · Freeze the spec
- Write a shared spec: what the project is, audience and scenario, core message as bullets, emotional tone, output format and dimensions (required, identical across all three), known constraints, image needs.
- The spec says only "what to say", never "what it looks like".

## 46. Phase 3.5 · Materials up front
- Decide the material tier; fetch all content-required real images and every named product's logo, shared across directions (named-product logo sub-gate must pass before building).

## 47. Phase 4 · Six candidates → six thumbnails → three
- Before writing, check user preferences/lessons and the look ledger (recent looks and references used — don't reuse them).
- View the style specimen overview for the medium's section (web / deck / infographic / app / Xiaohongshu, plus the cross-medium Chinese & East Asian section) to know each style done right.

## 48. Logic A · Best designer (×2)
- Ask: with unlimited budget, which studio/designer worldwide best fits "this user, this subject"? Pick two of different temperaments (one bold, one restrained; or one Western, one East Asian).
- Adopt their design thinking and build from scratch; don't imitate the look of a single work.
- Don't keep landing on the same names; beyond Pentagram, Kenya Hara, Vignelli consider Lü Jingren, Kohei Sugiura, Ikko Tanaka, Kazunari Hattori, Irma Boom, Experimental Jetset, Collins, Studio Dumbar.

## 49. Logic B · Real-world reference (×2)
- Pick two real works in the SAME medium whose quality you're certain of: apps → Apple Design Award apps; websites → Awwwards winners, brand official sites; decks → publications and proposals; infographics → press graphics (SND, Malofiej winners).
- Same-medium references transfer layout directly; cross-medium ones (deck as Penguin cover, app as herbarium sheet) came out over the top or boring — let cross-medium references lend only color or type relationships, not layout.
- Verify existence by search, then screenshot it and actually look; a reference written only as a name yields the model's average impression.
- Write what is borrowed as concrete rules: number of grid columns, headline-to-body size ratio, dominant color share, image-text relationship.
- If screenshot fails (anti-scraping, WebGL black screen), use a write-up page or image of the work or ask the user; if impossible, write "have not seen it with my own eyes" on the card.
- Treat a near-blank screenshot (pixels differing from the dominant color by >24 brightness under 0.8%) as "not seen"; WebGL black screens ≈0.4%, the emptiest minimal design ≈1.5%.

## 50. Logic C · Seconds roulette (×2)
- Take current seconds S; draw style number `S % (style count in section) + 1` from the matching section and `S % 12 + 1` from the Chinese & East Asian section.
- Open the drawn style's specimen first and see it done right before writing the card.
- If the draw lands in the same family as one of the last 3 ledger deliveries, move to the next number.
- If fidelity <70%, note which part was downgraded.
- Purpose: take you somewhere you wouldn't have gone on your own.

## 51. Specified style or brand
- All six candidates produce interpretations inside that context; colors may all sit under brand constraints (compare skeletons only); roulette draws only context-compatible styles.

## 52. Direction card fields (write six)
- Logic and source: which designer / which work (with source and screenshot) / which style at which number.
- What is borrowed: concrete rules (grid, type relationships, color proportions, image-text relationship).
- Lead material: real photos, generated images, procedural textures, data-as-image, giant type…
- Skeleton: layout structure in one sentence.
- Where the daring goes: the one boldest spot; everything else serves content.
- Where the form grew out of the content: which thing only this subject could have.
- Example (artisanal three-generation soy sauce brewery): Kenya Hara — generous whitespace, material as protagonist, very few words, real clay vats and sunning yard, one screen/one image/one sentence slow vertical pace, full-bleed salt-frost hero, "sauce suns 180 days so the pace slows"; award-winning Japanese food maker site — vertical titles vs horizontal captions, two-color ratio, thin-ruled sections, only two colors, "family recipe" presence; roulette "Media-Grade Editorial Brutalism" — large type-size contrast, modular grid, an oversized character for "sauce" cut into the hero, "one character tells the whole sauce house".

## 53. Thumbnails
- Draw all six on one page, each cell the candidate's most crucial screen (web first screen, deck cover, infographic opening, app main screen), ~480×300, with real fonts, real palette, real skeleton, real headline; details may be omitted.
- Screenshot and look; when a cell looks wrong, swap the source and redraw it — don't wait for the full build.

## 54. Picking three (criteria in order)
- 1 Good enough standing alone: presentable to anyone; what the thumbnail can't hold up the full version won't rescue.
- 2 Different from one another: different skeletons, different temperatures (bold/neutral/quiet needn't all appear but not all the same), not crowding one look family.
- 3 No collision with recent projects' looks and references.
- 4 Not trying too hard: at most one of the three may turn the page into a prop/physical replica, default to a universal metaphor (subway map, terminal command line, newspaper front page, dashboard), or max out saturation and font sizes — and only when content truly needs it.
- Over-device test: remove the device — if the information gets clearer, it was too much.
- Don't need one per logic (e.g. two best-designer + one roulette is fine); keep the other three as alternates and show them.
- Don't let all three be pure typography.

## 55. Building the three
- Give each builder only the spec + its own card (with screenshot/specimen) + shared materials; independent contexts, no cross-referencing.
- Use the user's real content, no Lorem; same content across all three, only design differs.
- Apply hard readability floors (see Part 7).
- Single-file HTML with images/logos embedded as base64.
- Decks: 2 representative pages per direction.
- Multi-screen app prototypes: don't line up a row of phones; compose a display board.
- Screenshot at 1440×900 (decks 1920×1080).
- Draft forms per medium: web/infographic/prototype — 1 full HTML + screenshot per direction; decks — 2 representative pages; animation — 1 direction board (genuinely rendered keyframe + palette + one-line positioning + reference name); covers/single images — 1 real render; multi-page Xiaohongshu sets — cover + 1 inner page.
- Confirm there really are 3 full versions before moving on.
- After building: run the design check, the three-way comparison and the ledger check; on a collision swap in an alternate or change the skeleton — not the colors.

## 56. Presenting
- Lay out the three screenshots together, each with its card summary (logic & source, what's borrowed, lead material) and its form-from-content line.
- Attach the thumbnail overview: "the other three are alternates — if one catches your eye, I'll build it out".
- End the turn and wait.

## 57. After the pick
- Record shown versions, screenshot paths, the user's verbatim words.
- Record clear taste statements verbatim ("zero AI feel", "too plain", "more like a magazine", "over the top") with their scope.
- Build mixed picks ("A's layout + C's colors") as asked; note which fields were mixed (more useful than which color).
- After delivery log the look plus its source (designer/work/style) so the reference is steered away from next time.

# Part 6 — Anti-AI-Slop Rules

## 58. The 2026 AI default look — look families (not banned)
- 1 Warm cream background (near #F4F1EA) + high-contrast serif headings + terracotta accent (near #D97757) — Claude's own palette.
- 2 Near-black background + a single bright accent (acid green or vermilion).
- 3 Newspaper layout: hairline column rules, zero border radius, dense columns.
- 4 SaaS card kits: identical rounded cards, same radius, same light-gray shadow, gradients as decoration.
- Using a family is not wrong (they look good and win approval); what's wrong is all three directions crowding into the same family, or every project looking like this.

## 59. Template chrome (delete by default)
- All-caps letter-spaced eyebrow line above every heading.
- "A · B · C" middot chains.
- "WORD — snippet" labels.
- #0B0B0B or #111 instead of black (catch by eye).
- Monospace for small data labels.
- Trailing "→" on links and buttons.
- Recoloring or italicizing exactly one word in a headline.
- All-caps for every small label.
- Unnecessary small labels above content.
- 01/02/03 numbering for content that isn't a sequence.
- If the brief asks for them, keep them; otherwise delete the whole structure — swapping a symbol (e.g. middot → full-width space) to dodge detection is not a fix.

## 60. Last generation's slop (still out)
- Aggressive gradient backgrounds: purple→pink→blue full-screen, rainbow gradients, background mesh gradients. If a gradient is needed: subtle, monochromatic, intentional (e.g. button hover).
- Rounded card + left border accent (e.g. radius 12px, 4px colored left border, 16px padding); instead use background contrast, weight/size contrast, a plain divider, or no card.
- Emoji decoration unless the brand uses emoji (e.g. Notion, Slack); especially no 🚀 ⚡️ ✨ 🎯 💡 before headings, no ✅ in feature lists, no emoji arrow in CTAs (a plain standalone arrow is fine). Use a real icon library (Lucide/Heroicons/Phosphor) or a placeholder.
- SVG imagery: never draw people, scenes, devices, objects or abstract art in SVG; a gray rectangle labeled "illustration placeholder 1200×800" is 100× better. SVG allowed only for real icons (16×16–32×32), geometric decorative shapes, data-viz charts.
- CSS silhouettes standing in for real product shots.
- Too much iconography: not every heading/feature/section needs an icon.
- Data slop: "10,000+ happy customers", "99.9% uptime" without real data, decorative icon+number+word metric cards, fake-data mock tables.
- Quote slop: fabricated testimonials or famous quotes.
- Fabricated logo walls.
- AI tech clichés: gradient spheres, digital rain, blue circuit boards, robot faces; replace literal symbols with abstract metaphors (e.g. the metaphor of "conversation" rather than a chat-bubble icon).
- Cyber-neon: deep-blue base (#0D1117) + neon glow (unless the user's brand requires it).

## 61. Typography traps
- Avoid overused faces: Inter, Roboto, Arial/Helvetica, bare system stacks, Fraunces, Space Grotesk; flag Inter/Roboto/Arial/Helvetica/system-ui as display fonts (UI text face used as display).
- Use a distinctive display + body pairing: serif display + sans body (editorial), mono display + sans body (technical), heavy display + light body (contrast), variable font for hero weight animation.
- Underrated faces: Instrument Serif, Cormorant, Bricolage Grotesque, JetBrains Mono.
- Never invent typeface names.

## 62. Color traps
- Don't invent a whole unfamiliar color system from scratch.
- Strategy: brand colors → use them, interpolate missing tokens in oklch; reference available → eyedrop from screenshots; from zero → sample from the subject (materials, origins, artifacts, dominant colors in real photos): sample → converge → justify.
- Define colors in oklch; derive light/dark variants at the same hue (e.g. primary oklch(0.62 0.14 155), light 0.85 0.06 155, dark 0.42 0.15 155).
- Don't invert colors for dark mode; re-tune saturation, contrast, accents — or skip dark mode.

## 63. Layout traps
- Don't overuse bento grids unless the information structure genuinely suits it.
- Avoid the big hero + 3-column features + testimonials + CTA landing template.
- Don't make every grid card identical: vary sizes, mix image and text-only cards, span columns.

## 64. Counterexamples
- When the task is to showcase slop, isolate it in an honest counterexample container: dashed border + "counterexample · don't do this" corner tag; don't pollute the page's main tone.

## 65. Decision quick reference
- Gradient? Most likely no. Emoji? No. Rounded card + left border? No. SVG hero illustration? No, placeholder. Decorative quote? Ask for a real one. Row of icon features? Ask first. Inter? Swap. Purple gradient? Swap for a color scheme with a basis.

## 66. Mechanically enforced checks — RED (must fix before delivery)
- Page fails to open.
- Any broken image (visible image with natural width 0).
- Any console/page error.
- Body text below floor: any visible text run ≥28 characters not inside a caption/footer/small/aside/sup/sub/figcaption/credit/footnote/meta element with rendered size < body floor (default 14px; decks 24; 1080-wide phone long-form 36).
- Label text below floor: 3 or more visible text runs below label floor (default 12px; decks 16; phone long-form 28).
- Insufficient contrast anywhere: ratio < 4.5:1 for normal text, < 3:1 for large text (≥24px, or ≥18.66px at weight ≥700); semi-transparent text blended with background (opacity multiplied through ancestors) before computing; SVG text measured at rendered (scaled) size; backgrounds resolved from the element's own fill, then elements underneath (sibling plates count), white if none.

## 67. Mechanically enforced checks — YELLOW (template chrome; delete)
- ≥3 eyebrow labels: uppercase (CSS or ≥3 Latin letters all caps), ≥2 Latin letters, letter-spacing ≥0.06em, size ≤15px.
- ≥2 " · " middot separators.
- Any "WORD — snippet" label (1–20 caps chars, space, em dash, space, text).
- ≥2 trailing "→" on links/buttons/pointer elements.
- ≥4 monospace labels ≤14px.
- Any h1/h2 containing an inline em/i/span/strong/b/mark covering ≤40% of the headline text with a different color, style or font.
- ≥3 short (≤6 char) "0N" numbering tokens — ask whether the content is really a sequence.
- Display (largest text) font is Inter, Roboto, Arial, Helvetica, system-ui or -apple-system.
- Any relative-path image (not data:/http(s):/blob:) — single-file deliveries must inline base64.
- No detectable text (all images/canvas) — findings rest on the screenshot palette alone.

## 68. Mechanically detected look families (info only)
- Warm-paper serif: background lightness L>0.9 with warm hue 40–110° and chroma ≥0.003, plus terracotta (#D97757 within oklab distance 0.07) or serif headline.
- Dark single-accent: background L<0.2 with exactly one vivid palette color (chroma >0.15).
- Hairline newspaper: ≥8 elements >200px wide with 1px borders and >90% of large boxes at zero radius.
- Card kit: same radius + same shadow repeated ≥4 times.
- Background classes: light (L>0.9) neutral white (chroma <0.003) / warm paper / tinted; dark (L<0.28) near-black (chroma <0.03) / tinted; mid tinted (chroma >0.04) / grey.

## 69. Mechanically enforced distinctness (three directions & ledger)
- Collision if palettes nearly identical: area-weighted symmetric mean nearest oklab distance < 0.06.
- Collision if layout skeletons highly similar: correlation of normalized 32×20 edge maps > 0.55 (reskins are caught by skeleton, not color).
- Collision if same background class + same serif/sans headline + same display font.
- Flag all three directions sharing one background class ("three variants of a single temperament").
- Flag all three directions landing in the same look family (one or two in it is fine).
- Brand-constrained mode: compare skeletons only; ignore skeleton for forms naturally identical (several devices side by side).
- Any unreadable direction fails the comparison; never approve directions that couldn't all be inspected.
- Ledger: a trait recurring in ≥max(2, 50%) of the last 8 deliveries is "recurring" — at least one direction must not land there again.
- If every direction collides with recent projects, let at least one leave the recurring look entirely.

## 70. Xiaohongshu image checks (enforced)
- Canvas 1242×1660 (3:4); body floor 42px, label floor 32px at 1242 wide (= 36/28 at 1080 wide).
- ✗ any text below label floor; ✗ text wrapping ≥2 lines and ≥16 chars below body floor.
- ✗ text outside the page (clipped >2px).
- ✗ text across a seam in panorama strips (crossing a 1242px joint by >4px).
- ✗ text overlapping text (boxes overlap after trimming 20% of height top and bottom).
- ! text covered by another element (sticker, color block) at left/middle/right points; ! text over an image box.
- ! text crowded against a small text-less color block (long edge <120px), e.g. a collapsed grid.
- Mark intentional stacking explicitly; passing checks doesn't mean shippable — review every image.
- At most 18 images per post.

# Part 7 — Content Guidelines & Scale

## 71. No filler
- Every element must earn its place; solve empty space with composition (contrast, rhythm, whitespace), not content.
- Filler tests: remove it — does the design get worse? If no, remove. What real problem does it solve? If "less empty", delete. Is it backed by real data? If not, don't write it.
- No Lorem ipsum, no "Title Text".

## 72. Ask before adding material
- Ask before adding another paragraph/page/section; the user knows the audience, added content has cost, unilateral additions break the junior-designer relationship.

## 73. Create the system up front
- State the planned system verbally (colors with sources, typography, rhythm, imagery plan, at most 2 background colors) and get confirmation before starting.

## 74. Readability floors (no style exempt)
- Web body ≥14px, labels ≥12px.
- Deck body ≥24px, labels ≥16px.
- 1080-wide long-form images for phones: body ≥36px, labels ≥28px (canvas pixels).
- Body contrast ≥4.5:1.
- Whitespace must be composition, not missing content; overdone quiet styles (dead white + microscopic type) look like broken renders and lose to baselines.

## 75. Slides (1920×1080)
- Body minimum 24px, ideal 28–36px.
- Titles 60–120px; section titles 80–160px; hero headlines 180–240px.
- Labels, annotations, chart ticks ≥16px.
- 1 core viewpoint per page.

## 76. Print
- Body minimum 10pt (≈13.3px), ideal 11–12pt; titles 18–36pt; captions 8–9pt.

## 77. Web & mobile
- Body ≥14px (16px for elderly-friendly); mobile body 16px (avoids iOS auto-zoom).
- Hit targets ≥44×44px.
- Line height 1.5–1.7 (Chinese 1.7–1.8).

## 78. Contrast
- Body vs background ≥4.5:1 (WCAG AA); large text ≥3:1.

## 79. Typographic "taste tax" & CSS tools
- Headings `text-wrap: balance`; body `text-wrap: pretty`.
- Chinese: `text-spacing-trim: space-all`, `hanging-punctuation: first`; use 「」 corner quotes for Chinese.
- Use CSS Grid with named areas, subgrid to align card content, container queries, `:has()`, `color-mix(in oklch, …)` for hovers (e.g. primary 85% + black), designed thin scrollbars, view transitions.
- Glassmorphism only with restraint (e.g. blur 20px saturate 150%, white 70% mix).

## 80. Single-file & delivery hygiene
- Embed images and logos as base64 in single-file deliverables (relative paths break when the file moves).
- Persist playback position of fixed-size content (slides, animation) across reloads.
- Open in a browser / screenshot and actually look before delivering.

# Part 8 — Materials & Textures

## 81. Principles
- Pick each direction's lead material first; don't let all three be pure typography.
- When type is the material, make it deliberate: type becoming the image (giant type, vertical setting, cropping), not default headline + body.
- Fetch every content-required image before designing; for animals, places, people, products, history, images are content (a parrot site with no parrot = failure; animal page with no animal photo = failure). When in doubt, treat as content-required.
- Design only after materials are in — not color-block placeholders filled in later.
- Real-image honesty test: remove the image — does information lose anything? No loss = decoration, don't add. No stock "inspiration images".
- Never hand-draw people, animals, physical objects or scenes in SVG; use real photos, generated images or an honest placeholder. Geometry, icons, data graphics, map linework exempt; silhouette masks only for composition (cropping photos, building shapes), never as a product stand-in.
- For the user or their own product, use real personal assets first; ask if missing; never fabricate.
- Fetch every named product's logo, one by one; keep filling gaps; only when truly unfetchable use an honest placeholder and say so.

## 82. Tier 0 (always available)
- Real photos from public-domain/open collections (Wikimedia Commons, Met, Art Institute, Biodiversity Heritage Library) and Unsplash/Pexels, ~1600px wide, with license info.
- Procedural materials: SVG turbulence + displacement filters for paper grain, noise, ink bleed, misregistered print; layered radial gradients for light/volume; mask/clip-path for silhouettes and crops; blend modes for overprint; canvas-generated contour lines, dot grids, flow fields, star charts, fabric textures (fixed random seed for reproducible screenshots); procedural 3D geometry/materials/lighting.
- Data as image: numbers become the main visual — a page-spanning scale, objects scaled to proportion, a route on a map — not three big number cards.
- Physical replicas: tickets, labels, ID cards, instruction sheets, postcards, newspaper spreads with paper stock, punch holes, stamps, creases.
- Type as image: oversized glyphs sliced out of frame, vertical setting, glyphs interlocking with images.

## 83. Tier 1 (image generation available)
- Generate one atmosphere/hero probe image per direction at the direction-board stage so the user picks something visible.
- After the pick, generate hero images, illustration, textures, people, scenes.
- Prompt with concrete visual features and real reference names, not adjectives like "premium feel" or "minimalist".
- Generated images must pass the honesty test; generate brand product images from official reference images, never from thin air.

## 84. Tier 2 (specialist add-ons)
- Use richer capabilities (image prompt methods, art/narration animation styles, publication-grade layouts, procedural 3D, flowing diagrams) when present.

## 85. Missing capability
- Never block: drop to T0, continue, and tell the user in one line at delivery what more they could get; recommend only the relevant add-on, no catalog pitching.
- Trust the user's word over capability detection.

## 86. Failed-fetch fallback
- 1 Nothing in public-domain libraries → Unsplash/Pexels.
- 2 Nothing suitable anywhere → generate from a reference image if T1 available.
- 3 Still nothing → continue with an honest "image to be added" placeholder and say so at delivery; degrade and continue, don't stop.

# Part 9 — Variations & Tweaks

## 87. Good variations
- Explore possibility space, not choice paralysis; let the user mix and match.
- Clear dimensions: each variation varies one dimension (A vs B only color, C vs D only layout).
- Gradient: from by-the-book conservative to bold novel.
- Label each variation with what it explores.
- Static visual comparison → side-by-side labeled grid; interaction/option differences → one complete prototype with a Tweak to switch (e.g. login layout: left copy + right form / top logo + center form / full-screen background + floating form).

## 88. Exploration matrix (pick 2–3 dimensions)
- Visual: minimal / editorial / brutalist / organic / futuristic / retro.
- Color: monochrome / dual-tone / vibrant / pastel / high-contrast.
- Typography: sans-only / sans+serif contrast / all serif / monospace.
- Layout: symmetric / asymmetric / irregular grid / full-bleed / narrow column.
- Density: sparse breathing / medium / information dense.
- Interaction: minimal hover / rich micro-interaction / exaggerated large animation.
- Material: flat / layered shadows / texture / noise / gradient.

## 89. When to add Tweaks
- When the user asks to adjust parameters or switch versions; when variations need comparing; or when a few instructive tweaks would show the possibility space.
- Default: add 2–3 tweaks to every design (color theme / font size / layout variant) even unasked.

## 90. Tweak design principles
- Expose real, discrete, considered options (e.g. corner style: none / subtle / heavy), not continuous sliders whose intermediate values look ugly (e.g. no 0–50px radius slider).
- At most 5–6 options; more becomes a configuration page.
- Defaults must be a complete, publishable design; what the user sees with the panel closed is the deliverable.
- Group options when many (Visual: primary color, font size, dark mode / Layout: density, sidebar position / Content: data volume, state).
- Panel closed by default as a small button (bottom-right), expands on click, never covers content.
- Persist state across reloads; key shared tweaks per project; handle storage failure gracefully (e.g. private mode).
- Link related tweaks where sensible (dark mode switches text color automatically).

## 91. Typical tweak sets
- General: primary color (picker), font size (12–24px slider), typeface (display vs body), dark mode toggle.
- Slide decks: theme (light/dark/brand), background (solid/gradient/image), font contrast (decorative vs restrained), density (minimal/standard/dense).
- Product prototypes: layout A/B/C, interaction speed 0.5×–2×, data volume 5/20/100 items, state (empty/loading/success/error).
- Animations: speed 0.5×–2×, looping (once/loop/ping-pong), easing (linear/easeOut/spring).
- Landing pages: hero style (image/gradient/pattern/solid), CTA copy variants, structure (single column/two column/sidebar).

# Part 10 — Multi-Perspective Parallel Exploration

## 92. When to use
- Enable: user asks for different directions / more versions; first version done and user unhappy but can't articulate; multi-platform distribution; client hasn't locked a style but has time/token budget (repeated revisions ≈5× cost).
- Don't enable: clear style references and only 1 version wanted; simple motion graphic/icon animation; deadline <30 minutes.

## 93. Choosing perspectives
- Choose perspectives with extremely high visual differentiation to prevent convergence.
- Span 3 geographic cultures (e.g. Western film / Japanese design / Hong Kong Chinese), 3 eras (1960s / 1970s / 2010s+), 3 media (film / graphic design / installation art).
- Each must carry a signature that is the exact opposite of the generic SaaS aesthetic.
- Example set: modern publishing baseline (terracotta + classic-paperback serif + Vignelli grid, the "safe tasteful" choice); Wes Anderson (symmetric composition, chapter cards, decorative borders, magazine/industrial-catalogue feel); Saul Bass (cut-paper silhouettes, Trajan caps, big type, strong diagonals); Wong Kar-wai (letterboxing, slow pacing, hazy glow, Chinese-first serif); Massimo Vignelli (strict grid, 3-color rule, no ornament); Kenya Hara (white space, no chrome, ma/interval); Yayoi Kusama (obsessive repetition, single strong color, dots).

## 94. Perspective briefs (8 fields each)
- Project background (shared); methodology template to read (shared); deliverable checklist (4 items); the artist's DNA; structure reference (e.g. 4–6 shots for 30s); real, readable end cards; key constraints (e.g. 30s, 1920×1080, opens from file, web fonts); verification checklist + completion report format.
- Artist DNA in 6 fields: palette (specific HEX), typography (specific names + fallbacks), visual language (core rules), signature elements, rhythm (how it differs), style-hardened anti-slop.
- Make each perspective concrete down to work + year (e.g. Anderson → The French Dispatch 2021, Moonrise Kingdom 2012; WKW → In the Mood for Love 2000, 2046 2004; Vignelli → 1972 NYC Subway map, Knoll manual, The Vignelli Canon; Hara → MUJI 1995–2023, White; Kusama → Infinity Mirrored Rooms 2013–2023) to capture specific DNA, not the genre average.
- Stress "do not repeat the baseline's aesthetic" in every brief.

## 95. Style-hardened anti-slop
- Add per-style forbidden zones on top of generic anti-slop, e.g.: Bass — no Helvetica (too clean); Vignelli — no rounded corners (all 90°); Hara — no gradients, no sans-serif display; Kusama — no modern SaaS look; Anderson — no cyber color schemes; WKW — no Inter (serifs).

## 96. Running & reviewing
- Run perspectives independently in parallel; expect ~16% failure (1 of 6); on failure re-run with the same brief; if partially complete, fill missing screenshots rather than re-running.
- Do substantive work while waiting (fix baseline bugs, write the review framework, prepare the summary); don't poll.
- Review on 5 dimensions (1–10 each): Distinctiveness, Coherence, Anti-slop, Story arc, Pause-and-look (detail density).
- Ask 3 top-level questions: screenshot-worthy (would trigger a pause and share)? memorable in one line? timeless (won't look cheap 5 years later)?
- Assign each version a use case by platform/audience rather than only picking a winner (e.g. dense baseline → product page; magazine feel → long-article hero; nostalgic → cultural content platforms; poster-like frames → design community; minimalist → client demos/static screenshots; high-impact → short viral video). Marketing is platform-specific multiplexing.
- A clear brief lets multiple independent executors produce consistently high quality; writing long director's notes first is reproducible.

# Part 11 — Critique Method & Scoring

## 97. Dimension 0 · Concept / Intent (highest weight, first gate)
- 9–10: unique idea growing from the user's content with an irreplaceable visual motif.
- 7–8: clear intent; motif relates to content but would barely survive a similar theme swap.
- 5–6: style but no concept — looks nice, says nothing.
- 3–4: generic template reskinned; concept layer zero.
- 1–2: wrong style, pure decorative pile-up.
- Ask: can you state the idea in one sentence? (If not, there is none.)
- Cover all text and logos — is the theme still recognizable? (For type-as-motif layouts ask instead whether the typographic treatment would hold under a different theme.)
- Would it hold with a different client/product name? If yes = template → cap this dimension at ≤5.
- Does the form have a content-derived unique motif?
- One-vote veto: when Concept ≤5, cap the overall score at 6.0; fix the concept before discussing execution.

## 98. Dimension 1 · Philosophy alignment
- 9–10 every detail has a philosophical basis; 7–8 direction right, a few details drift; 5–6 intent visible but other styles mixed in; 3–4 surface imitation; 1–2 unrelated.
- Check signature techniques of the chosen designer/agency; color/type/layout conformity; self-contradictions (e.g. Kenya Hara stuffed full of content).

## 99. Dimension 2 · Visual hierarchy
- 9–10 gaze flows as intended, zero friction; 7–8 clear with 1–2 blurred spots; 5–6 headline vs body distinct but middle levels muddled; 3–4 flat, no entry point; 1–2 chaotic.
- Headline-to-body size contrast at least 2.5×; establish 3–4 clear levels via color/weight/size; whitespace guides the eye; pass the squint test.

## 100. Dimension 3 · Craft quality
- 9–10 pixel-precise; 7–8 1–2 tiny issues; 5–6 inconsistent spacing, unsystematic color; 3–4 obvious misalignment, too many colors; 1–2 draft-like.
- Use a unified spacing system (8pt grid); consistent spacing between like elements; usually ≤3–4 colors; usually ≤2 typeface families; precise edge alignment.

## 101. Dimension 4 · Functionality
- 9–10 every element serves the goal; 7–8 a little trimmable decoration; 5–6 decoration distracts; 3–4 form over function; 1–2 drowned in decoration.
- Delete any element — worse? If not, delete. CTAs/key info most visible; no "because it looks good" elements; density matches medium (PPT not dense, PDF can be denser).

## 102. Dimension 5 · Originality
- 9–10 refreshing, distinctive expression within the framework; 7–8 own thinking; 5–6 template-like; 3–4 heavy clichés (e.g. gradient spheres for AI); 1–2 entirely template/stock.
- Avoid clichés; include personal expression; seek "unexpected but sensible" decisions.

## 103. Scenario priorities (Concept always first)
- WeChat cover/images: most Originality, Hierarchy; secondary Philosophy; relax Functionality.
- Infographic: most Functionality, Hierarchy; secondary Craft; relax Originality (accuracy first).
- PPT/Keynote: most Hierarchy, Functionality; secondary Craft; relax Originality (clarity first).
- PDF/white paper: most Craft, Functionality; secondary Hierarchy; relax Originality (professionalism first).
- Landing page/corporate site: most Functionality, Hierarchy; secondary Originality; relax nothing.
- App UI: most Functionality, Craft; secondary Hierarchy; relax Philosophy (usability first).
- Xiaohongshu images: most Originality, Hierarchy; secondary Philosophy; relax Craft (atmosphere first).

## 104. Top 10 common problems & fixes
- 1 AI tech clichés → abstract metaphors instead of literal symbols.
- 2 Weak type-size hierarchy (<2.5×) → titles at least 3× body (body 16px → title 48–64px).
- 3 Too many colors (5+, no structure) → 1 primary + 1 secondary + 1 accent + gray scale.
- 4 Inconsistent spacing → 8pt grid, spacing only 8/16/24/32/48/64px.
- 5 Insufficient whitespace → at least 40% of area (60%+ for minimalist styles).
- 6 Too many typefaces (3+) → at most 2 (1 title + 1 body), vary weight and size.
- 7 Inconsistent alignment → one alignment globally (left recommended).
- 8 Decoration over content → delete any decoration whose removal doesn't hurt.
- 9 Cyber-neon abuse (#0D1117 + neon glow) → a more distinctive scheme.
- 10 Density mismatched to medium → PPT 1 core viewpoint per page; cover 1 visual focus; infographic layered presentation; PDF denser with clear navigation.

## 105. Review output format
- Overall X.X/10 with tier: Excellent 8+ / Good 6–7.9 / Needs improvement 4–5.9 / Failing <4 (cap 6 when Concept ≤5).
- Per-dimension score with one-sentence explanation (Concept stated as the design's idea in one sentence).
- Strengths (Keep) in design language.
- Problems (Fix) sorted by severity, tagged Fatal / Important / Improvement, each with current state, why it's a problem, and a specific fix with values.
- Quick Wins: the 3 highest-impact fixes doable in 5 minutes.
- Optionally visualize the dimensions as a radar chart.

# Part 12 — Verification

## 106. Rule 0 · Verify your verification tools
- Before trusting any render, confirm the renderer renders correctly; untrusted tools hand out fake green lights.
- A thumbnail is not a render; never use simplified previews as acceptance (one let 4 text-overlap bugs through across 20 pages).
- Some office-suite renderers drop fonts/CJK text (tofu blocks); layout may be trustworthy but text not.
- Distinguish tool vs artifact problems with a control experiment: render a known-good file of the same kind.
- Trust ranking: OS quick-look thumbnails ✗; headless office suite ⚠ (layout ok, fonts may drop); real layout-engine export ✓ (automation first choice); the target app opened by human eyes ✓ (final).
- Never drive a GUI by injecting keystrokes (they land in the user's active window); use document-level export APIs or look manually.
- Pair with a renderer-independent mechanical check: character-by-character text comparison (source vs artifact equal after stripping whitespace) and per-page element counts — "a renderer can fool the eye, but not a count".

## 107. Checklist after every HTML output
- 1 Browser render: does it open?
- 2 Console errors (most common: JS error → white screen).
- 3 Multiple viewports for responsive designs: 1920×1080, 1440×900, 768×1024, 375×667.
- 4 Interactions (tweaks, animations, toggles): click through or record video; static shots can't show them.
- 5 Decks: screenshot slide by slide.
- Wait for animations to settle (~2 seconds) before capturing; use 2× device scale for retina shots; capture full page, viewport and specific elements as needed.

## 108. Common failures
- White screen: check script integrity hashes, style-object naming conflicts, cross-file component exports, JSX syntax errors (use the non-minified compiler to see them).
- Animation lag: profile for layout thrashing; animate transform and opacity only.
- Wrong fonts: check font URL accessibility and fallbacks; show fallback first for slow CJK fonts.
- Misalignment: global border-box sizing, margin/padding reset, inspect grid overlays.

## 109. Self-review mindset
- Always review yourself; AI code often has interaction bugs, misaligns on scroll, breaks narrow, forgets dark mode, has components that don't respond after a tweak.
- 1 minute of verification saves 1 hour of rework.

## 110. Video artifact hard checks
- Validate resolution/frame rate, duration within ±2%, audio stream present (no audio track = half-finished) unless an intermediate, no black frames at head/tail (unless a deliberate cinematic black open), loudness −14 ±4 LUFS for final films; any failure = do not deliver.

# Part 13 — Learned Lessons & Evolution

## 111. Three ledgers
- Taste profile: the user's verbatim preferences, their picks among directions and what they mixed.
- Look ledger: each delivery's background family, primary palette, headline font, layout-skeleton fingerprint, project, source note.
- Experience & pitfalls: observed (one project) vs verified (recurred across ≥2 projects or measured).
- Keep the user's verbatim words and taste private to them.

## 112. Three moments
- Before kickoff: recall preferences + topic lessons; review the last 8 deliveries' looks and recurring traits.
- While working: record user reactions (rejections, "too plain", mixed picks like "A's structure + C's colors") verbatim on the spot; don't reconstruct at wrap-up.
- After wrap-up (approval or user stops weighing in): log the look; harvest evidence; the direction-approved record is the most direct evidence of taste — see which logic and intensity they lean toward, not just which colors.
- Tell the user when you record a taste statement ("I've noted that line in this machine's taste profile"); if they decline, don't record.

## 113. What's worth recording
- Record only when all three hold: not obvious; saves the next project time or detours; this project produced evidence.
- Every entry needs topics and evidence (verbatim quote, project/file, measurement); unverifiable entries are hearsay.
- Preferences must quote the user verbatim and state scope ("their covers use warm paper" ≠ "every design uses warm paper"); preferences written as global defaults caused monotony.
- Order: 1 correct a contradicting entry in place (don't append a contradiction; search for the old claim everywhere); 2 turn it into an automated check + test if measurable; 3 otherwise write it down.
- Promote general lessons only when seen in two projects or measured and true for anyone; one user's taste never becomes a general rule.
- Experience never expands authorization (never implies permission to publish, spend money or contact anyone).
- Mark lessons that stop holding as superseded with what replaced them.

## 114. Promotion ladder
- recorded (observed) → reproduced (verified) → written into guidance / kickoff must-checks → automated check + test → engine default.

## 115. Verified lessons (S1–S8)
- S1: unconstrained directions slide to warm cream + high-contrast serif + terracotta; don't let all three crowd into one family.
- S2: palette/font-only reskins sharing one skeleton are recognized at a glance; skeletons must differ; beware overcorrecting into forced metaphors.
- S3: overdone quiet/whitespace styles become dead white + microscopic text; floors (web 14, deck 24, phone long-form 36, contrast 4.5:1) exempt no style.
- S4: single-file HTML with relative image paths breaks when moved (six product buttons broke, review lost); always base64.
- S5: forced big-idea metaphors turned pages into props / universal metaphors (subway map twice in 4 briefs; won 1 of 4); at most one of three; apply the remove-the-device test.
- S6: bans to dodge the AI look produced pale, cool, tidy, boring results (lost both briefs); add options, not bans.
- S7 (observed): same-medium award-winning references won; cross-medium references were over the top or boring; cross-medium may lend only color/type relationships.
- S8: two candidates per logic + thumbnails + specimens + screenshotted references won both briefs; add candidates before bans.

## 116. Pit ledger (other recorded pitfalls)
- Different projects drifting to look alike → check against the look ledger.
- Swapping " · " for a full-width space to dodge the chrome check → delete the structure instead.
- Quiet look overdone → floors enforced.
- Skipping direction confirmation before a long film → whole film reworked (210s case); gate long renders.
- A specified style used as an excuse to skip three directions → style words not exempt.
- Asserting from memory a product "hasn't launched" → verify first.
- Pulling only brand colors and skipping the logo → comparison deck failed; logo checklist mandatory.
- Export silently dropping bare text beside an SVG → compare text content after export.
- App prototypes lining up 5–6 equally spaced phones → every direction looks boring; compose a display board.
- Decks: pages carrying their own page numbers fight the shell's numbering — don't add them; only ≤5-page decks go single-file (a 13-pager lost its overview wall).
- Animation giving every scene its own layout + fade-up = a narrated PPT.
- Faking content-essential images with CSS color blocks.
- Personal memory archives (e.g. a travel photo archive) should be complete ("try not to leave any out") — scoped to photo archives only, not product UIs.
- Showcase practice: in factual decks cite sources on every slide (e.g. a black-hole-photo lecture: black ground, photos as protagonist, labels written directly on the image); sample a dark ground from the darkest part of the artwork being presented; when two directions open with the same hero image, swap one.

# Part 14 — Typography (Latin + CJK / mixed scripts, pairing, scales, hierarchy)

## 117. Typesetting decision order
- Reason in this order, each step constraining the next: (1) content type → (2) language composition → (3) style temperature → (4) font names last.
- Content type (long-form reading / data-dense / marketing display / UI) sets the scale ratio and body size.
- Language composition (pure Chinese / mixed CJK-Latin / pure Latin) sets the fallback chain and line-height baseline.
- Style temperature (quiet / neutral / bold) sets the source of contrast in the pairing.
- Never start with "pick a nice font": doing so makes content have zero influence on typesetting and produces same-looking pages.
- When the user/brand has its own fonts, use those first; these rules apply only when there is no font spec.
- The same style label applied to different content must yield different typesetting (do not copy the same sizes every time).

## 118. Modular type scale
- Derive sizes by multiplying the body size by a fixed ratio, level by level; never guess.
- 1.2 (minor third): gentle, many levels without clamor — dashboards, doc sites, information-dense UI.
- 1.25 (major third): general-purpose, safe — most web pages, product landing pages.
- 1.333 (perfect fourth): headings clearly pop — editorial long-form, marketing pages, reports.
- 1.5 (perfect fifth): dramatic, very few levels — posters, slides, one-line-per-screen heroes.
- Body: 16–18px; Chinese body 17–18px (dense hanzi strokes look more crowded than Latin at the same size).
- Reference values at 1.25: caption 12–13px (captions, meta, EXIF-style small print); small 14px (helper notes, tables); body 16–18px; h3 ≈1.25×; h2 ≈1.56×; h1 ≈1.95×; display 3×–8× (outside the scale).
- More than 5 levels is out of control — cut. More than 6 levels is an anti-pattern (hierarchy devalues).
- Display/hero mega-type is a layout element, not a hierarchy level: size it by the fraction of viewport it occupies (vw-based), not by the scale.

## 119. Fluid type
- Use clamp() for display tiers to avoid stiff large screens and overflowing small ones.
- h1: `clamp(2rem, 1.2rem + 3.5vw, 4.5rem)`.
- Display: `clamp(3rem, 1rem + 9vw, 9rem)`.
- Body: narrow range only, `clamp(1rem, 0.95rem + 0.3vw, 1.125rem)` (16→18px); do not let body swing widely.

## 120. Line length (measure)
- Line length affects readability more than font choice; runaway line length is the #1 readability problem.
- Latin body: 45–75 characters, best 66 → `max-width: 65ch`.
- Chinese body: 22–38 characters per line, best 28–32 → `max-width: 36em` (scales with font size).
- Captions/sidebars: 15–20 Chinese characters (narrow containers).
- Chinese runs shorter because hanzi carry more information per width; overlong lines make the next line start hard to find.
- Never allow ~60 hanzi per line on a big screen; always set a max-width.

## 121. Line height (leading)
- Line height is a function of line length: longer lines need more leading.
- Display mega-type (1–2 lines): Latin 0.95–1.1; Chinese 1.1–1.25.
- Headings h1–h3: Latin 1.1–1.3; Chinese 1.3–1.4.
- Short-line body (<30 chars/line): Latin 1.4–1.5; Chinese 1.6–1.7.
- Long-line body (near cap): Latin 1.6; Chinese 1.8–2.0.
- Chinese runs ~0.2 higher than Latin across the board (full-square glyphs lack lowercase gaps; tight leading smears).
- Chinese body baseline: 17px / line-height 1.8.

## 122. Line breaking and wrapping
- Headings: `text-wrap: balance` (balances multi-line headings, kills orphan lines) — only for headings ≤4 lines (algorithm caps at 6 lines, has a performance cost).
- Body: `text-wrap: pretty` globally (eliminates end-of-line orphans; strong effect in Latin, mild in Chinese).
- Chinese: `line-break: strict` (no periods/commas at line start, no opening quotes at line end).
- `overflow-wrap: break-word` so long URLs/Latin strings do not burst containers.

## 123. Font pairing logic (Latin)
- Decide the source of contrast before pairing: formal contrast, same-family interlock, or epoch contrast.
- Formal contrast: serif display × sans body (classic) — x-heights must interlock or the visual size jumps.
- Same-family interlock: a superfamily on one skeleton (zero risk, cost is blandness).
- Epoch contrast: classical × modern glyphs — tension appears only with 200+ years of pedigree gap; a ~50-year gap just looks messy.

## 124. Ten open-source Latin pairings (display + body)
- Newsreader + Geist — formal contrast; screen-optimized transitional serif, high x-height interlocks with Geist; the legitimate Fraunces substitute. Quiet.
- Source Serif 4 + Source Sans 3 — same-family interlock; cap-height and weight rhythms aligned; reports/docs never fail. Quiet.
- EB Garamond + IBM Plex Sans — epoch contrast (16th-c. old-style × 2017 grotesque, 400 years); Garamond's low x-height needs compensation at the same size (+8% starting point; systematic fix `font-size-adjust`). Quiet/literary.
- Lora + Hanken Grotesk — formal contrast; brush-feel medium-contrast serif; Hanken is an open near-relative of the Söhne vibe. Neutral.
- Instrument Serif + Geist — only one weight (400), display-only; body must be sans. Becoming overused by AI tools — be wary when you "want to look distinctive". Neutral.
- Schibsted Grotesk + Source Serif 4 — inverted (grotesque display, serif body), media feel; the substitute now that Space Grotesk is ubiquitous; newsroom pedigree. Neutral.
- Bricolage Grotesque + Newsreader — Bricolage's ink traps/irregular details show only at large sizes (native display); rough × refined with a quiet serif body. Bold.
- Archivo (Expanded/Black) + Inter — poster structure; Archivo's wide black weights carry the pressure; Inter only as 14–16px body workhorse. Bold.
- Cormorant Garamond + Work Sans — high-contrast luxury; Cormorant only works at ≥40px (hairlines break smaller); fashion / cosmic-catalog aesthetics. Bold.
- Geist Mono / JetBrains Mono + Geist — mono as protagonist, command-line/engineering feel; mono only for labels/numbering/code — a full body paragraph in mono is a disaster (line length inflates ~30%). Neutral/technical.

## 125. Overused fonts and substitutes
- Fraunces as display (default "tasteful" pick of 2023–2025 AI tools) → Newsreader, Libre Caslon Text.
- Inter as display (designed for small UI text; uniform and expressionless large) → Archivo, Anton, Schibsted Grotesk.
- Space Grotesk (lazy "techy" answer, crypto/AI landing pages) → Schibsted Grotesk, Familjen Grotesk.
- Playfair Display (lazy "elegance", wedding-invitation vibe) → Cormorant (more extreme), DM Serif Display (chunkier, more naive).
- "High-contrast serif × warm cream background" is a look family, not a banned font: allowed, but do not use it on every project or crowd all three design directions into it.
- Inter everywhere (display + body) is the #1 fingerprint of AI-generated pages.

## 126. Chinese font map (open-source / free commercial)
- Noto Serif SC — Songti serif, publishing-canonical, 7 weights; Heavy works as display. Quiet–neutral.
- Noto Sans SC — Heiti sans; "the Inter of Chinese": reliable, expressionless; fine default body, no personality. Fallback for any temperature.
- LXGW WenKai — Kai (script), handwritten warmth; literary/educational/personal-blog body and quotations. Quiet/warm.
- LXGW Neo XiHei — leaner, more breathable screen sans than Noto Sans; comfortable long reading. Quiet.
- Smiley Sans — rare native italic Chinese sans, sporty; headings only (body text dizzies). Bold.
- Huiwen Mingchao — old metal-type Ming print feel; book covers, cultural display. Neutral–bold/vintage.
- Jinghua Laosong — blocky, hard-stroked heading Song; newspaper-masthead feel. Bold/vintage.
- Yuanliu Ming / Yuan Yang Ming — Ming type preserving traditional glyph details; first choice for Traditional Chinese. Quiet/classical.
- Glow Sans — modern geometric sans, multi-width (Compressed works as narrow tall display). Neutral–bold/modern.
- MiSans / HarmonyOS Sans / OPPO Sans — vendor UI sans with a bit more personality; right for app prototypes. Neutral.
- Body text only from serif / sans / kai; everything else is display type.
- Use Smiley Sans / old Song / Ming only when display needs personality; never set whole paragraphs in them (fatigue after ~200 characters).
- Max two Chinese font families per page (load: 5–15MB per file; and consistency).

## 127. Mixed CJK–Latin fallback chain
- Put the Latin font first, then the Chinese font, then system Chinese, then generic: e.g. `"Geist", "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif`; serif: `"Source Serif 4", "Noto Serif SC", "Songti SC", serif`.
- Reason: font-family matches per character; Latin fonts contain no CJK, so hanzi fall through. Chinese-first lets the Chinese font's (usually ugly) bundled Latin eat every Latin character — an anti-pattern.
- Never delegate Chinese to the bare `sans-serif` default (Windows → SimSun/Microsoft YaHei, macOS → PingFang: two different faces across devices).
- Do not default-fill a serif for display; choose per subject.

## 128. Mixed-script size and baseline compensation
- Latin lowercase looks smaller than hanzi at the same size (x-height ~half the em vs full square).
- Fix 1: `font-size-adjust: from-font` on :root (normalizes fallback by x-height).
- Fix 2: choose a tall-x-height Latin face (Geist, Inter, Source Sans) so mixed setting lines up naturally.
- Latin words "sinking" in Chinese lines: prefer a taller-x-height Latin face; in display only, nudge Latin spans with `vertical-align: -0.02em` to `-0.06em`; never in body text.

## 129. Numbers and data typography
- Digits always render through the Latin font (guaranteed by the fallback chain).
- Tables/data: `font-variant-numeric: tabular-nums` (plus `slashed-zero` so 0 and O don't confuse); without it columns jitter and credibility drops.

## 130. CJK–Latin spacing
- Do not hand-type spaces between Chinese and English (reject "Pangu spacing"); the gap comes from the fonts' side-bearings in the fallback chain.

## 131. Chinese has no italics — emphasis substitutes
- Never apply `font-style: italic` to hanzi (faux shear deforms strokes).
- Italic emphasis → weight change, `font-weight: 600` (only if the font has that weight).
- Italic book titles/quotes → highlighter background `linear-gradient(transparent 60%, #FFE9A8 60%)`.
- Italic quotation blocks → switch the whole quote to LXGW WenKai (Kai is Chinese's native quotation voice).
- Italic proper names → color, or emphasis dots `text-emphasis: dot`.
- Globally `font-synthesis: none` (no synthetic italic/bold — better no emphasis than deformed glyphs; synthetic bold smears strokes into ink blobs).

## 132. Chinese punctuation
- Use corner brackets 「」『』, not curly quotes "" (curly quotes in Chinese fonts are full-width Latin-shaped placeholders that float).
- `line-break: strict` as baseline.
- Hanging punctuation: `hanging-punctuation: first allow-end` (Safari only); cross-browser, `text-indent: -0.5em` for paragraph-opening quotes (else first line looks indented half a character).
- Consecutive full-width punctuation: `font-feature-settings: "halt"` (line-end compression) or `"palt"` (full proportional width, needs letter-spacing); apply `"halt" 1` to Chinese display type.

## 133. Chinese letter-spacing
- Body: 0 to 0.05em (beyond 0.05em words shatter and reading speed drops).
- Headings 24–48px: 0 (square forms are evenly spaced already).
- Display >60px: -0.02em to 0 (slight tightening; more negative collides strokes).
- All-caps Latin micro-labels: 0.08–0.15em — the only scenario for wide positive tracking, uppercase Latin only (e.g. `.label { text-transform: uppercase; letter-spacing: 0.1em; font-size: 12px }`).
- Never apply the Latin "-0.05em on display" habit to Chinese.
- Latin display needs tightening; adding +0.05em to Latin headings (common AI mistake) makes them look like loose placeholders.

## 134. Chinese display mega-type
- Weight contrast is the primary weapon: e.g. Noto Serif SC Heavy 900 against Light 300 on one screen — more tension than swapping fonts, zero load cost.
- Thin/high-contrast strokes (Song fine horizontals, Cormorant-like) hold only at large sizes; below 24px they break — body must return to Heiti / medium stroke.
- Heavy-stroke faces (Heiti Black, old Song) carry too much ink at extreme sizes; density gaps between sparse and dense characters get amplified — step headings down a weight.
- Vertical writing (`writing-mode: vertical-rl`) is a Chinese-only display weapon: book-spine headings, poems, indexes; Latin/digits inside use `text-orientation: upright` or `text-combine-upright: all` (two-digit numbers combine upright).

## 135. Weights
- Do not limit to 400/700 only (page goes flat, hierarchy carried only by size); use 300–900 as expressive dimensions with variable fonts.

## 136. Body font features
- Body: `font-feature-settings: "liga" 1, "calt" 1` (standard ligatures on, fancy features off).

## 137. Chinese font loading
- Prefer Google Fonts Noto SC (auto-split into unicode-range chunks).
- Self-hosted personality fonts must be subset: body to ~3,500 common characters; display to characters actually used (a poster may need ~20 characters, <50KB).
- `font-display: swap` always (never blank-screen waiting on Chinese fonts).

## 138. Typography anti-patterns (checklist)
- Inter for display and body.
- Chinese left to system `sans-serif`.
- Faux italic / faux bold.
- Positive tracking on Latin display headings.
- No max-width on text.
- More than 6 size levels.
- Only two weights.
- Data without tabular-nums.
- Chinese body in display fonts.
- Chinese font first in a mixed fallback chain.

---

# Part 15 — Slide Decks (structure, layouts, per-slide rules, editable PPTX)

## 139. Delivery chain
- Always build the HTML presentation first (keyboard paging, fullscreen); it is the source. PDF and PPTX are derived snapshots.
- Automatically produce a vector PDF on completion (text stays copyable/searchable); produce editable PPTX only when asked.
- Confirm delivery format before starting: HTML only → full visual freedom; + PDF → same freedom; + editable PPTX → write under the hard constraints from line one (no gradients, no web components, no complex SVG). Not confirming costs 2–3 hours of rework.
- "HTML presentation + editable PPTX" is not a conflict (constrained HTML still presents in-browser). "PPTX + animation/web components" is a genuine contradiction — tell the user and let them choose.
- Archive/records → PDF; collaborators fine-tuning text → editable PPTX (accept font fallback); live presentation unchanged → PDF; HTML as primary medium → browser, export as backup.
- PDF is the true destination for a visual-first deck, not a compromise.
- If PPTX need is discovered late: first choice PDF; second, rewrite an editable version from the visual draft; never hand-build PowerPoint coordinates as the first reaction (permanent maintenance debt).

## 140. Showcase-first production
- For decks ≥5 pages, never write page 1 → last straight through.
- First make the 2 page types with the biggest visual difference; get the user to confirm the grammar (masthead, fonts, color, spacing, structure, bilingual ratio); then batch the remaining N−2 reusing it.
- Recommended pairs: B2B brochure → cover + philosophy/emotion page; brand launch → cover + product highlights; data report → big-data visual + conclusions; courseware → chapter cover + knowledge-point page.
- When exploring three directions, each direction produces 2 representative pages (cover + data page, etc.) inside one shared shell; only the visuals change.

## 141. Publication grammar (B2B brochure / product promo / long report decks)
- Per-page skeleton: masthead strip (logo 22–28px · "A Product Brochure" left; Issue · Date · URL right) + horizontal rule; kicker (short brand-color dash + uppercase label, e.g. "CHAPTER XX · SECTION NAME"); H1; English subtitle; divider; content block (two columns 60/40, 2×2 grid, or list); footer with section name left and "XX / total" right.
- H1: Chinese Noto Serif SC 900, 80–140px depending on information volume; color only the key words in the brand primary (never the whole line).
- English subtitle: Lora italic 26–46px; brand signature words bold + primary-color italic.
- Body: Noto Serif SC 17–21px, line-height 1.75–1.85.
- Accent highlights: primary color + bold, max 3 per page.
- Background: warm off-white #FAFAFA + extremely faint radial noise `rgba(33,33,33,0.015)` for paper feel.

## 142. Rotating the visual protagonist
- Never let every page be "text + one screenshot"; rotate the protagonist type:
- Cover typography (large type + masthead + pillar) → home / chapter cover.
- Single oversized character/portrait → introducing one concept/character.
- Group photo / avatar cards side by side → team / user cases.
- Advancing timeline cards → long-term relationship, evolution.
- Knowledge graph / connected nodes → collaboration, flow.
- Before/After cards + middle arrow → change, difference.
- Product UI screenshot + outlined device frame → specific feature.
- Half-page big quote → emotion / problem / quote page.
- Real-person avatars + testimonial cards (2×2 or 1×4) → testimonials.
- Large-type back cover + URL ellipse/pill button → CTA / ending.

## 143. Information density per slide
- Each page: 1 core message + 3–4 supporting points + 1 visual protagonist; anything more → split to a new page.
- Example: 2×2 paragraphs + 3 credos (7 blocks) is crowded; 1×3 restores breathing room.
- Viewers look at a page ~10 seconds; one memory point beats four.
- List/matrix pages: don't draw all N items equal; enlarge today's ~5 points as protagonists, shrink the rest (e.g. 16) into background hints.
- Big-number pages: the number is the protagonist; caption ≤3 lines.
- Quote pages: leave whitespace between quote and attribution.
- Keep adjusting until the whitespace makes you slightly uneasy; self-audit "is data the protagonist?" and "is text squished?".

## 144. Deck system statement
- Before building, state the system and get confirmation, e.g.: background colors at most 2 (90% white + 10% dark section dividers); display + body typefaces; rhythm (section dividers full-bleed color + white text, regular slides white); imagery (hero slides full-bleed photos, data slides charts).

## 145. Slide layouts
- Title: solid background + huge title + subtitle + author/date.
- Section divider: colored background + section number + section title.
- Content: white background + title + 1–3 bullets.
- Data: title + big chart/number + brief explanation.
- Image: full-bleed photo + small bottom caption.
- Quote: whitespace + huge quote + attribution.
- Two-column: left/right comparison (vs, before/after, problem/solution).
- Use at most 4–5 layouts in one deck.
- Assign each page one narrative role (cover, transition, data, quote, closing); the layout changes with the role.

## 146. Slide type scale (1920×1080 canvas)
- Body minimum 24px, ideal 28–36px.
- Labels/annotations ≥16px.
- Titles 60–120px.
- Hero type 180–240px.
- Design for viewing from ~10 m.
- Generic projection hierarchy (pt): title 40pt+, body 24pt+, notes 16pt+.
- Demo values seen: eyebrow mono 14px tracking 0.24em uppercase, accent color, 24px below; H1 serif 92px weight 500, line-height 1.08, tracking -0.01em; subtitle sans 22px line-height 1.5, max-width 780px; accent hairline 80×2px, 48px below; slide padding 96px 120px.

## 147. Visual rhythm
- Color rhythm: mostly white + occasional colored dividers + occasional dark stretches.
- Density rhythm: some text-heavy, some image-heavy, some whitespace quote pages.
- Size rhythm: normal titles + occasional giant hero text.
- Never make every slide look the same (that's a template, not design).

## 148. Data slides
- Don't default to "three big numbers + a bar chart".
- First ask the relationship: proportion → real objects scaled to the ratio; change → one narrative curve; composition → a whole taken apart; comparison → left/right juxtaposition; scale → one oversized object.

## 149. Canvas, units, page chrome
- HTML deck canvas: 1920×1080px fixed; use px, never vw/vh/% (scaling handled uniformly with letterboxing).
- Vertical deck: 1080×1920 (9:16).
- Single-slide padding example: 120px; section padding 80px 120px.
- Page numbers live only in the presentation shell; slide content never carries its own page number or progress marker (they fight, e.g. "02/03" vs "6/16").
- Slide numbering starts at 1, never 0; label slides meaningfully (e.g. "04 Problem statement").
- Remember playback position across refresh; support hash jump to slide N.
- Print: each page exactly one 1920×1080 (or A4) page, nothing cropped; `@page { size: 1920px 1080px; margin: 0 }`; no trailing blank page.

## 150. Deck architecture choice
- Default multi-file: each slide a standalone 1920×1080 page, combined in an index with iframes (scope isolation, per-page verification, parallel work).
- Single-file only for ≤5–10 page pitches needing cross-page shared state or in-deck animation, when no overview wall is needed.
- Shared tokens only: palette, type scale, spacing scale, canvas lock, identical header/footer chrome. Never put single-page layout classes in shared tokens.
- Single-file: never put display/layout on the section itself; hide non-active (`display: none !important`), put flex/grid on `.active` or an inner wrapper.

## 151. Deck overview / presenter shell
- Default entry is an overview: grid ~60% / infinite gallery ~40% (varies; can be pinned).
- Grid overview: real pages, cards 16:9, radius 9px, gap 20px, shadow `0 16px 34px rgba(40,34,24,.20), 0 3px 10px rgba(40,34,24,.12)`; hover scale 1.18 with deeper shadow; warm light background radial #f4f1e9 → #e7e3d8; perspective 2200px, origin 50% 42%.
- Grid adaptivity: if all fit, tilt slightly and center; if too many, keep comfortable card size and scroll vertically (never postage stamps); compute columns from page count + viewport; flatten the tilt as rows grow.
- Make the card wall one tilted plane (no nested 3D) so clicks are reliable; hover via 2D scale.
- Infinite gallery: dark radial #1b1610 → #0a0805, tilt rotateX 18° rotateZ -9° scale 1.22, slow drift (~80s loop), breathing scale 1.0→1.045 over 26s, hover pauses drift, card radius 8px, vignette `inset 0 0 240px 70px rgba(8,6,3,.62)`; base card width ~300px.
- Gallery thumbnails ≥1000px wide (default 1600px) or they blur on hover zoom.
- Shell chrome: counter pill bottom-right 20px, 13px tabular-nums, rgba(0,0,0,.65); overview button top-left; side click zones 15% width with 44×44 round hints; start button pill bottom-right 26px, 13×24px padding, 15px.
- Overview title: 13px, tracking 0.22em, uppercase, top 24px, centered.

## 152. Speaker notes
- Only when asked. Write the actual words (not an outline), conversational, Nth note = Nth slide, 200–400 characters each, mark emphasis/pauses/stress.
- With notes, minimize on-slide text and focus on impactful visuals.

## 153. Export-safe glyphs
- Avoid emoji in exported decks (headless renderers lack color emoji → empty boxes); use text symbols ✦ ✓ ✕ → · — or plain text ("Email · 23").
- Wait for webfonts (~3.5 s) before capturing, or self-host, else Chinese falls back to system sans.

## 154. Editable PPTX — canvas size
- Body 960pt × 540pt = 13.333″ × 7.5″ (PowerPoint 16:9 "Wide" layout) — default. Equivalent: 1280×720px or 13.333in×7.5in.
- 720pt × 405pt (10″ × 5.625″) only for a specified legacy widescreen template.
- 1920×1080px (20″ × 11.25″) is non-standard for built-from-scratch PPTX: fonts look abnormally small projected. Size is physical, not resolution.
- Body size must match the layout within ±0.1″.
- When inheriting a client template, the canvas follows the template (e.g. 26.67″ × 15″); with a 1920px HTML canvas mapped to 1920pt, 1 CSS px = 1 pt.

## 155. Editable PPTX — hard constraints (build-from-scratch route)
- All text inside `<p>`, `<h1>`–`<h6>`, `<ul>`/`<ol>`; no bare text in a div; a `<span>` cannot be a standalone text frame (only an inline override inside p/h).
- No CSS gradients (linear/radial count as background-image); use solid colors, or fake transitions with stepped solid flex blocks, or a pre-rendered PNG image.
- Background/border/shadow only on divs, never on text tags (p, h*, ul, ol, li); wrap the text in an outer div that carries them.
- No `background-image` on divs; images always as `<img>`; to layer text on a picture, position the image and text as separate elements.
- No `::before`/`::after` decorative text; no margin on inline elements (span/em/strong); no web components; no complex SVG decoration.
- Lists: real ul/li, never manual "•".
- Keep large text ≥0.5″ from the bottom edge (presentation mode partially covers it); content must not overflow 540pt vertically.
- Example template values: page title 36pt bold #1A1A1A at top 40pt / left-right 60pt; subtitle 16pt #555, 10pt below; card h2 24pt white bold, p 14pt rgba(255,255,255,.85); card padding 12pt 16pt, radius 4pt; list 16pt with 24pt indent; solid background e.g. #FEFEF9.
- Write titles as assertive sentences, not topics.
- Each p/h becomes its own text box; to keep one editable multi-paragraph box, merge paragraphs into one text box (alignment and line-height then come from the first paragraph — only merge when alignment is uniform; no nested merges; no child shapes inside a merged box).
- Visually driven HTML passes these constraints <30% of the time — never force it; use the rendered-coordinates route or PDF instead.
- These are OOXML physics: text lives in text frames; shape and text frame are separate objects; arbitrary-angle gradients unsupported; pictures must be real image files.

## 156. Editable PPTX — downgrading a visual draft (when rewriting)
- State losses up front (gradients, web components, complex SVG) and offer PDF vs rewrite.
- Retain: color system, information hierarchy, core copy, layout skeleton, page rhythm.
- Downgrade: gradient → solid or flex segments; web component → paragraph HTML; complex SVG → simplified image or solid geometry; shadows → removed/near-none (e.g. 2pt border for separation); custom fonts → toward system fonts; animated hero → static first frame.
- Deliver a before/after list (e.g. "title purple gradient → solid #5B3DE8").
- Deliver both: visual-draft PDF + editable PPTX.
- Refuse rewrite when: core value is animation/interaction (50%+ info lost), >30 pages (>2 hours), or design depends on precise SVG/custom filters.

## 157. Editable PPTX — from rendered layout (existing visual drafts / client templates)
- Use measured post-render coordinates; zero refactoring of flex/centering/bare text.
- Never mix this route with the build-from-scratch route in one project.
- Inherit client templates: keep their master/layouts/theme/palette; delete sample slides; let the layout supply logos and shared elements (don't draw them into content) so master edits propagate; remove hidden full-screen solid masks in layouts.
- Collapse HTML whitespace (source newlines/indents otherwise become real line breaks).
- Base margins/line spacing on the largest run's font size, not the container's inherited size.
- Count lines by overlapping y-ranges, not by unique tops.
- Split mixed-size lines at `<br>` into separate text frames (each with its own line height).
- For text that was single-line in HTML, turn word-wrap off (shrink-wrapped flex frames have zero slack; last character drops otherwise).
- Don't set exact line spacing on single-line paragraphs (line box > actual gap; text gets pushed down).
- Verify in a real presentation engine (Keynote/PowerPoint/WPS), not quick-look thumbnails; LibreOffice layout is trustworthy but may lose Chinese. Run a control test with the client's original template.
- Compare exported text against the browser's rendered text (independent source) to catch silent text loss; compare image/shape counts per page.
- Delivery font ≠ layout font: lay out with a font installed locally; carry the client's spec font name (e.g. Microsoft YaHei) in the PPTX. Safe for Chinese-dominant decks (CJK full-width is monospace, wraps unchanged); Latin-dominant decks need separate verification.
- Font fallback between web measurement and PowerPoint rendering causes overflow/misalignment — review every page; install fonts on target or fall back to system-ui.

---

# Part 16 — Web Pages

## 158. Hero
- Open with the most distinctive thing in the subject's world: one headline, one image, one stretch of animation, one playable demo, or one interactive moment.
- "Big number + small label + row of supporting data + gradient garnish" is the default answer — use only when truly best.
- Same for the "big hero + three feature columns + testimonials + CTA" template.
- Convey core value within 5 seconds above the fold; hero height 100vh.

## 159. Landing page structure
- Desktop design width 1440px, responsive down to 320px.
- Clear CTA.
- Scroll narrative: problem → solution → proof → action.
- Mobile adaptation and loading speed are part of the design.

## 160. Web hard rules
- Body text ≥14px (≥16px on mobile).
- Tap targets ≥44×44px.
- Body-text contrast ≥4.5:1.
- Verify at least at 1440 (×900) and 375 (×812) widths.
- Interactions must really work: navigation, tabs, expanders, form states; zero console errors.
- No invented data, testimonials, or logo walls; use honest placeholders or ask.
- Motion: one choreographed page load beats fade-up on every block; motion responding to user actions (expand, confirm) is the good kind.

## 161. Web build order
- Three directions, each a full page + hero screenshot + full-page screenshot.
- After the pick: write assumptions + placeholder structure first, then fill components.
- Add live tweak controls (colors, type sizes, copy) only after structure and rhythm are settled.
- Tweak dimensions demonstrated: palette (warm ↔ cool), type (serif ↔ sans), density (sparse ↔ dense).
- Warm palette example: bg #F6EFE6, panel #FFFFFF, ink #1A1918, dim #8B867E, hairline rgba(0,0,0,.08), accent #D97757. Cool: bg #0E1620, panel #17222E, ink #E8EEF5, dim #7A8A9B, hairline rgba(255,255,255,.08), accent #5A8CB8.
- Density example: sparse card padding 22px, title 18px, text 13px/1.45; dense padding 12px 14px, title 13px, text 11px/1.3 with extra cards revealed.
- Hero title example: serif 86px, line-height 1.02, tracking -0.02em; sub serif 20px/1.6; eyebrow mono 11px tracking 0.24em accent; preview body padding 54px 72px 60px.

## 162. Presentation frames
- Present web pages inside a browser-window frame (URL bar + tab bar); desktop apps inside a desktop window shell; compare static variants side by side on a canvas.

## 163. Iterate early
- Show rough drafts early in small iterations (e.g. v1 at 15 min, v2 at 25 min, v3 at 35 min) rather than one all-at-once 3-hour reveal.

## 164. Direction fallback (when the user is unsure)
- Offer three distinct roads, e.g.: Eastern space (Kenya Hara: ma/emptiness, terracotta, vast whitespace, paper grain); Information architecture (Pentagram: strict grid, high contrast, editorial); Experimental edge (David Carson: broken type, brutal geometry, visual shock).

---

# Part 17 — Infographics

## 165. Viewer distance and container
- Set viewing distance and container first.
- Mobile feed: 1080 wide; the first screen (~1080×1350) must stand alone — title, hero visual, single strongest number.
- Print/large screen: fix physical size and viewing distance first, then type sizes.
- Embedded in an article: follow body width; text in the image no smaller than body text.

## 166. Infographic formats
- Vertical long: 1080×1920 (mobile reading). Horizontal: 1920×1080 (embedded). Square: 1080×1080 (social).
- Hierarchy: title → key data → details; visual guide lines along the reading path; icons/charts only to aid comprehension.

## 167. Infographic type floors
- On a 1080-wide canvas: body ≥36px, labels ≥28px (a 1080 image shrinks ~2.8× to ~390pt on a phone → lands at 13–14pt).
- Print/large screens computed separately from actual viewing distance.

## 168. Data as protagonist
- Use only numbers the user gave or that can be verified; label illustrative figures as such. Inventing data is ten times worse than leaving space empty.
- Pick the form from the relationship: proportion → real objects/areas scaled to the ratio; change → one curve or timeline; routes/space → map; composition → a whole taken apart; scale → one oversized object + a familiar reference object.
- One color = one meaning; write the legend on the image.
- Prefer real images, public-domain scientific illustration, and maps as lead material over a platter of icons.
- No decorative distortion of data.

## 169. Infographic build
- Three directions with genuinely different skeletons (map, timeline, field guide, single giant object, narrative sequence) — but never force a metaphor just to differ.
- After the pick, proofread every number and unit; export at the target width; re-slice to platform specs.

---

# Part 18 — Social / Xiaohongshu (RED) Cards

## 170. Xiaohongshu canvas
- Canvas 1242×1660 (near 3:4); exact 3:4 at 1080×1440 also fine (convert sizes proportionally). Square 1:1 1080×1080 acceptable.
- Max 18 images per post.
- First image (cover) competes in a two-column feed and decides click-through.

## 171. Xiaohongshu type floors
- On 1242-wide: body ≥42px, labels ≥32px (= 36/28 at 1080).
- Cover title ≥100px, finished within two lines (gets ~1/3 screen width in the feed).
- High-contrast serifs (Bodoni-like) lose thin strokes below 100px on phones ("4" reads as "1"); use Song serif or sans for small numbers; high-contrast numbers on covers ≥200px.
- If a small cell can't fit 32px text, merge into "the remaining N" or show image only — never shrink text.

## 172. Xiaohongshu platform constraints in design
- No external links, QR codes, WeChat IDs, or emails in images; point people with "search xxx on GitHub" or "drop a comment below".
- No absolute claims ("the best", "No. 1 in the industry", "the only one"); ordinals like "step one" are fine; rephrase superlatives concretely ("worth every penny").
- Disclose AI-generated imagery as required; credit author + license on image or post body for CC BY images.
- Text under ~20% of image area for image-generated social pictures; vivid but tasteful color; lifestyle/texture/atmosphere feel.

## 173. Xiaohongshu paradigms (pick by content)
- Own product recognizable at a glance → Product Notebook (borrow the product UI's paper, controls, assets).
- Content in a row (object set, timeline, pipeline) → Panorama Strip (several images join into one).
- Nature/knowledge/culture long-form needing authority, magazine feel → Specimen Journal.
- Numeric conclusions, rankings, lists → Index Ink, or Area Infographic.
- Events (launch, retrospective, method write-up) → Daily Paper.
- One item per card, collectible (species, products, people, tools) → Trading Cards.
- Slow content, stories, single-object close-up → Blank & Vertical.
- Three directions must land on three different paradigms; each shows cover + the hardest inner page (single-cover jobs: one cover each).
- A paradigm is only a skeleton: derive colors from content/brand; use the user's real materials.

## 174. Laying out a carousel set
- Cover: one hook (number, conclusion, or contrast) + one hero visual; title 8–14 Chinese characters; no table of contents on the cover.
- Image 2 answers "what is this"; each middle image tells exactly one thing (one headline, one picture); last image lands the next step (where to find, how to use, what to comment).
- Whole set is one system: same headers, page numbers, colors, fonts; rotate composition on adjacent images (big image, list, numbers, comparison).
- Cover carries no page number.
- Panorama strip: width 1242×N; protagonist straddles the seam (~2/3 on left image, ~1/3 on right); every image still has its own title and stands alone; continuous lines/horizons drawn as one continuous element, not per-image segments; no text crossing a seam.
- Check: no text escaping the page, no two text blocks pressed together, no text covered by images or squeezed against small color blocks; bottom cards/number bars must not collide with page number/footer (check the last image); no orphan word on a title's last line; grid not collapsed to one column.

## 175. Other social / editorial image specs
- WeChat article cover: 2.35:1 (900×383 or 1200×510); visual impact, minimal or no text (title overlays), moderate saturation (white reading environment), recognizable as a thumbnail, clear focal point.
- Article body illustrations: 16:9 (1200×675) most versatile; 1:1 (800×800) for emphasis; 4:3 (1200×900) for information-dense; serve the argument, one core concept, not decoration; precise data tables as rendered layout rather than generated imagery.

---

# Part 19 — App & iOS Prototypes

## 176. Device specs
- iOS: 390×844pt (iPhone 15); iPhone 15 Pro frame 393×852 logical.
- Android: 360×800dp. Tablet: 1024×1366pt (iPad Pro).
- Minimum tap area 44×44pt; standard status bar / navigation bar / tab bar; moderate density on mobile.

## 177. iPhone 15 Pro device frame (exact values)
- Bezel: 12px padding, #000, outer radius 60px, `0 0 0 2px #1f2937, 0 20px 60px rgba(0,0,0,.3)`; screen radius 48px.
- Dynamic Island: 124×36, top 12px, centered, fully rounded, black.
- Status bar: height 54px, padding 0 32px, 16px weight 600 system font; time left, signal/wifi/battery right, clear of the island and vertically centered on its midline. Signal bars 3px wide at heights 4/6/9/11, gap 2; battery 26×12, 1.5px border, radius 3, cap 2×6.
- Content area starts at top 54px and ends 34px above the bottom.
- Home indicator: 140×5, bottom 10px, radius 999, rgba(0,0,0,.3) light / rgba(255,255,255,.5) dark.
- Never hand-draw island/status bar/home indicator/bezel ad hoc — use a precise standard frame (hand-drawn ones put status items under the island or the first line under the island).
- Alternative showcase phone (film): 440×900 body, radius 58, screen 416×876 radius 46, island 120×34 top 14, status bar 15px with 18px top padding, content from top 64.

## 178. Prototype delivery format
- Default (don't ask): tile 4–6 main screens, each phone independently interactive (tab bar switches, buttons/cards/toggles clickable, modals open).
- >6 screens: show the 4–6 most important; the rest reachable via in-phone navigation.
- Exceptions only on explicit request: static overview only; or a single phone running one full flow (onboarding).
- Each phone lands on a different main screen; a label line beside each (e.g. 13px #666 italic, 8px above).
- Clickable elements get pointer cursor + hover feedback.
- Run click-through tests (enter details, key annotations, tab switching) with zero runtime errors before delivery.

## 179. Display board composition
- Never line up 5–6 equal phones evenly in a row ("too tidy, too boring").
- Hierarchy (first choice): enlarge the most representative screen 1.2–1.4× at the visual center; scatter the rest smaller at uneven heights.
- Flow chaining: order by real task; thin lines from tapped element to destination screen, caption beside the line.
- Close-up: beside one screen, a 2–3× close-up of a key component (signature interaction, data viz, crafted control).
- Contextual backdrop: board background from the app's context (real photos, subject colors, materials), not blank white.
- Board typography: own title area — app name, one-line positioning, screen labels, in the direction's type and colors.
- Board background and type follow the direction (dark direction → dark board); every phone stays clickable; each phone ≥300px wide.
- The three directions' boards must differ in composition.

## 180. Real imagery
- Fetch real images by default (public-domain museum collections for art/history; royalty-free photo libraries for lifestyle; user's own assets); no crude SVG drawings, no beige placeholder cards.
- Honesty test: "if removed, would information suffer?" Decorative images (article list covers, profile scenic headers, settings banners) → don't add (AI slop). Content images (museum portraits, product photos, map places) → must add. Atmospheric texture behind diagrams → allowed at opacity ≤0.08.
- Honest placeholder only when all sources fail, copyright is unclear, or user asks.

## 181. App taste anchors
- Typography: display chosen per subject from the pairing table; system font (-apple-system) for body. Avoid SF Pro or Inter everywhere.
- Color: sampled from the subject and real photos, one primary color throughout; avoid multi-color clustering unless data has ≥3 categorical dimensions.
- Density (default restrained): one fewer container layer, one fewer border, one fewer decorative icon; avoid every card having icon + tag + status dot.
- Density (high, exception): for intelligence/data/context-aware products (AI tools, dashboards, trackers, copilots, Pomodoro, health, expenses) every screen shows ≥3 visible differentiating pieces of info (non-decorative data, reasoning snippets, state inference, contextual relations).
- Detail signature: one screenshot-worthy texture (faint oil-painting texture, serif italic quote, full-screen black waveform).
- One detail at 120%, the rest at 80%; subtraction is a fallback, not a universal law.

## 182. Example app screen values (Pomodoro demo)
- Screen padding 40px 28px.
- Kicker mono 12px tracking 0.22–0.24em.
- Screen title serif 48px weight 300, line-height 1.02, tracking -0.035em.
- Hero timer serif 168px weight 200, line-height 0.95, tracking -0.04em, separator in accent.
- Ring timer 320×320; inside 86px weight 200 tracking -0.03em.
- Stats hero 120px weight 200 tracking -0.04em with 28px weight-300 unit.
- Primary CTA pill height 62px, 17px weight 500, tracking 0.04em; action buttons 14px 32px padding, 14px.
- Settings list radius 14px, rows 22px 24px, key 16px sans, value mono 13px.
- Toggle 48×28 with 22×22 knob.
- Floating pill tab bar height 58px, radius 999, tabs mono 10px tracking 0.1em, icons 18×18.
- Bar chart height 200px, gap 10px, bars radius 6px 6px 0 0, inactive bars 15% ink; axis mono 10px.
- Light screen palette: bg #F5F4F0, ink #1A1918, dim #8B867E, accent #D97757.

---

# Part 20 — Product Gallery Showcases

## 183. When to use a gallery wall
- Use for: 10+ real outputs shown at once; professional audiences sensitive to polish; a restrained, exhibition-like, premium, spacious feel; focus and overview simultaneously.
- Avoid for: single-product focus (use a product hero), emotion/story-driven pieces (timeline narrative), small/portrait screens (tilt blurs).

## 184. Gallery palette and type
- Light gallery: bg #F5F5F7, warm variant #FAF9F5, ink #1D1D1F, ink-80 #3A3A3D, ink-60 #545458, muted #86868B, dim #C7C7CC, hairline #E5E5EA; single accent (e.g. terracotta #D97757 / deep #B85D3D).
- Re-derive colors from each subject — warm off-white + terracotta is a top AI default look.
- Never pure black background (looks like a movie, not adoptable work).
- One hue accent only; everything else grayscale + white.
- Type stacks: serif EN + serif CN + sans + mono → "publication" not "internet product"; Inter only looks too internet.

## 185. Floating card
- White card, radius 14px, padding 6px (the mounting mat), 1px hairline border.
- Two-layer shadow: `0 20px 60px -20px rgba(29,29,31,.12)` + `0 6px 18px -6px rgba(29,29,31,.06)`.
- Aspect 16:9; inner image radius 9px (smaller than card for visual nesting), object-fit cover.
- No edge-to-edge tiles (no padding/border/shadow = infographic density, not exhibition); missing shadow/hairline looks like a slide template.

## 186. D tilted wall
- Viewport perspective 2400px, origin 50% 45%.
- Canvas 4320×2520 (2.25× viewport) to leave pan room; 8-column grid, gap 40px, padding 60px.
- Transform rotateX 14°, rotateY -10°, rotateZ -2°.
- Sweet spots: rotateX 10–15° (more looks like a party VIP backdrop); rotateY ±8–12°; rotateZ ±2–3° (human touch; without it the tilt looks cheap); perspective 2000–2800px (<2000 fisheye, >3000 near-orthographic).

## 187. ×2 selection grid
- Two 800px columns, gap 56px vertical × 64px horizontal.
- Corner entry vectors: ±700px x, ±500px y.

## 188. Gallery motion patterns
- Four-corner convergence 0.8–1.2s: slide from corners, scale 0.85→1.0, ease-out.
- Selected-card enlarge 0.8s: 1.0→1.28; others fade + blur (to 1.5px) + drift to corners (blur, not plain fade — simulates depth of field).
- Ripple expansion 1.7s: cards fade in with delay ∝ distance from center (max 0.8s delay, 0.7s each); whole gallery scales 1.25→0.94 (camera pull-back).
- Sinusoidal pan: sine + linear drift; period 0.09–0.15 rad/s (~30–50s per oscillation), drift 5–8px/s, amplitude 120–220px, clamp ±900px so edges never show. Use continuous frame-driven motion, never stepped timers or looping keyframes (stutters).
- Focus overlay: a flat (untilted) element above the tilted wall; scale from tile (~400×225) to center (960×540); background dims to 45% opacity and brightness -30% — never fully masked.
- Focus image must use the original full-resolution image, not the compressed tile thumbnail; preload originals.
- Example 25s timeline: intro 0–4s, selection 3.9–7.8s, ripple 8.3–10s, pan from 8.6s, four focus beats ~1.7s each with ~0.6s gaps (11–19.6s), wall-off 21.1–21.8s, brand in 21.8–22.7s, hold to 25s.
- Derive all state from time t (seamless loop via t mod duration; any frame seekable).

## 189. Gallery texture and branding
- Overlay faint SVG fractal noise (baseFrequency 0.85, 2 octaves) at 0.5 opacity on light backgrounds so they don't look flat.
- Corner brand label: top 48px, left 72px, mono 12px, tracking 0.22em, uppercase, muted color; like a museum label; only in the wall scene, fading in/out.
- Closing wordmark: sans 148px weight 700, tracking -0.045em (Apple-style large type); accent character in accent color at lighter weight 500 for contrast.

---

# Part 21 — Scene Templates (format specs)

## 190. Composition formula
- Style DNA + scene template + specific content description.

## 191. WeChat article cover / header
- 2.35:1 (900×383 or 1200×510); visual impact first; minimal or no text; moderate saturation; thumbnail-legible; one focal point.
- Suitable styles: Pentagram, Build, Sagmeister, Kenya Hara, Field.io.

## 192. Body / concept illustrations
- 16:9 1200×675; 1:1 800×800; 4:3 1200×900; one core concept; serve the argument; light/dark to match article tone.
- Styles: chosen by article tone.

## 193. Infographic scene
- 1080×1920 vertical / 1920×1080 horizontal / 1080×1080 square; title → key data → details; guided eye path; accurate data.
- Styles: Fathom, Müller-Brockmann, Stamen, Takram.

## 194. Presentation scene
- 16:9 1920×1080; 16:10 1920×1200.
- One core message per slide; title 40pt+, body 24pt+, notes 16pt+; generous whitespace; image-to-text ratio at least 60:40; consistent colors/fonts/spacing.
- Styles: Pentagram, Müller-Brockmann, Build, Kenya Hara, Fathom.

## 195. PDF whitepaper / technical report
- A4 portrait 210×297mm (595×842pt); Letter 216×279mm (612×792pt).
- ~66-character line width, line-height 1.5–1.8; chapter navigation; unified header/footer/page numbers; charts integrated with body; reference/annotation system; sophisticated cover.
- Styles: Müller-Brockmann, Fathom, Information Architects, Takram, Irma Boom.

## 196. Landing page scene
- 1440px desktop, responsive to 320px; hero 100vh; value in 5 seconds; clear CTA; problem → solution → proof → action.
- Styles: Locomotive, Pentagram, Build, Resn, Active Theory.

## 197. App UI scene
- iOS 390×844pt, Android 360×800dp, iPad Pro 1024×1366pt; 44pt tap targets; consistent design system; standard bars.
- Styles: Takram, Build, Information Architects, Pentagram.

## 198. Xiaohongshu image scene
- 3:4 1080×1440 optimal; 1:1 1080×1080; text <20% area; vivid but tasteful; lifestyle feel.
- Styles: Sagmeister, Build, Neo Shen, Experimental Jetset.

## 199. Example: warm-professional tech cover
- Takram-like: elegant concept diagrams, soft tech aesthetic (rounded corners, gentle shadows), charts as art, modest sophistication, neutral natural colors (beige, soft gray, muted green); at 1200×510 with minimal text.

---

# Part 22 — Motion Module Basics

## 200. Classify the film first
- Short animation/concept demo (<1 min, no narration) → storyboard then animate.
- Product UI as protagonist → UI showcase forms (screenshot camera moves vs rebuilt UI), cursor with arcing paths and click ripples.
- Launch film/brand promo → direction boards, then detailed director's notes.
- Long narrated video (≥1 min) → write voiceover script first, then picture.
- Lots of same-kind material (20+ items; message is scale) → gallery-style scenes.
- Multiple versions/platforms → parallel perspectives.

## 201. Motion flow
- Three direction boards: each 1–2 genuinely rendered hero keyframes + palette strip + one-line positioning + reference work; directions differ in motion language and materials, not just color.
- Storyboard cards before animating (every shot as a moving cover image, with camera column and acceptance frames); films ≥20s need visual-density clauses or they come back as wireframes.
- Camera moves (zoom/pan/transitions) are budgeted and follow inter-shot grammar.
- Inspect captured frames at key moments and the first second after each scene change (clipping, collisions, empty frames).
- Render at 60fps for final output.

## 202. Two most common motion failures
- "A slideshow with voiceover": independent layouts per scene + text fade-ups + whole-page opacity transitions. Instead: 1–2 hero elements persist across scenes; each segment is a state change of that element; scenes morph rather than cut.
- Fake chrome inside the frame (progress bar, timecode, copyright strap): the frame carries narrative content only.

## 203. Sound
- Default delivery includes SFX + BGM; silent is half-finished; BGM alone is one-third done.
- Cue density: launch hero ~6 SFX per 10s; tool demos 0–2 per 10s.
- Skip sound only when the user says no audio / visuals only / own voiceover.

## 204. Motion details from showcases
- Default main easing: exponential ease-out (older cubic ease-out `1-(1-t)^3` acceptable); ease-in-out cubic for symmetric moves.
- Film grain overlay on dark stages: fractal noise at ~2–2.5% opacity, overlay blend.
- Watermark/label on dark stage: mono 13–14px, tracking 0.2em, uppercase, rgba(255,255,255,.16), top ~36–40px left ~48–56px.
- Terminal card: width 620px, radius 14px, 1px hairline, header dots 11px, body mono 20px line-height 1.7, padding 32px 28px; blinking block cursor 10×24 in accent.
- Window mock: 1400×788, radius 14px, chrome bar 44px; split-screen windows 820×580, radius 12, gap 56px.
- UI tweak transitions ~240–280ms with `cubic-bezier(.2,.8,.2,1)`; hover lifts ~.28–.34s `cubic-bezier(.2,.7,.2,1)`.
- Brand closing wordmark example: serif 72px, tracking -0.02em, line-height 1.
- Animation output may carry a small creator credit; never on slides, infographics, prototypes, or web pages; unofficial tributes to third-party brands get an "Unofficial · " prefix.
- Long films (≥45s) require an approved direction before final render.

# Part 23 — Style-Selection Principles

## 205. Library positioning
- Treat the style library as "ammunition to flip through when you have no ideas", not a mandatory checklist. When the user supplies content, brand or references, unfold the design from those — never force a library style onto them.
- The goal is to help users avoid the worst, not to dictate what good design must look like; good design grows from real needs.
- Root cause of "every default looks identical": bold styles that depend on image generation (particles, light effects, hand-drawing) collapse when everything falls back to HTML, leaving only minimalism. Therefore tag every style with its fidelity under pure HTML/CSS with no image generation, and prefer styles that survive that fallback.

## 206. Look at the specimen before reading the description
- Study a visual example of a style before working from its name; a model that works from the name alone produces its averaged impression of the style.
- Borrow the layout and temperament of a specimen, never its subject matter or numbers (specimen content is fictional).

## 207. Choose the style family by output shape, not subject
- Clickable website / landing page / corporate site → Web styles.
- Anything paged through (deck, presentation) → Slide styles.
- An image or set of images with data as the protagonist, readable on its own without interaction → Infographic styles.
- App / mobile prototype → App styles.
- Social image posts / covers / carousels (3:4 vertical) → Social-card styles; every specimen doubles as a template.
- East Asian design traditions are cross-medium — any output shape may draw from them; especially consult them for Chinese-language content (Western references applied to a Chinese layout usually leave nothing but the color scheme).
- Dashboard prototypes are product UI → Web styles. A data page embedded in a deck → Slide styles (it gets paged through).

## 208. Temperature system (Bold / Neutral / Quiet)
- Tag every style Bold, Neutral or Quiet. Deliberately make Bold the majority of the pool: the model's determinism bias drifts toward quiet minimalism, so the pool ratio must push back toward bold.
- When proposing three directions, never let all three land on the same temperament (e.g. all "cream white + whitespace + one accent color").

## 209. Fidelity tiers
- ≥90% fidelity: build it confidently.
- 70–90%: the main body is doable; a few details downgrade.
- <70% (e.g. Memphis aged textures): explicitly state in the output which parts are downgraded to flat color blocks; never pretend to reproduce the original texture.
- Styles that need real photos (dark gallery, white-box gallery, map-as-protagonist) use honest placeholders in prototypes; fetch real images before building for real.

## 210. Fonts
- List open-source substitutes for every style (Inter, Geist, Manrope, Space Grotesk, Fraunces, Playfair, etc.); never specify paid fonts (Söhne, Circular, etc.).
- Font names in style entries are example anchors too: run display+body pairing through your pairing logic and "overused fonts" list first; when the overused list conflicts with a style entry, the overused list wins (e.g. if an entry says Fraunces, swap in the named substitute).

## 211. Color Derivation Protocol — Sample → Converge → Justify
- Treat every hex in a style entry as an example anchor, never a formula. The same style applied to different content must derive different colors; copying entry hex values is "slop with better taste" — 100 users get 100 identically colored outputs and color carries zero information.
- Step 1 Sample: take the primary from three sources, never from thin air — (1) brand assets (eyedrop the logo/existing VI), (2) real imagery in the content (dominant colors of product screenshots/photos), (3) cultural context (the color memory the theme carries). Picking from thin air = drawing lots from model priors, always landing on the same few trendy colors.
- Step 2 Converge: use oklch to compress the palette to 2–3 chromatic colors + 1 neutral set. Write neutrals as a lightness sequence (e.g. L 0.15 / 0.35 / 0.65 / 0.92 / 0.98). Keep chromatic colors apart by hue angle ΔH ≥ 60° or lightness gap ΔL ≥ 0.3.
- Step 3 Justify: write one sentence of "why this color" in output comments or delivery notes (e.g. "Primary taken from the ochre in the user's logo, chroma pushed down to 0.08 to simulate ink"). If you cannot write that sentence, you are copying a formula — the sentence is an anti-slop gate, not a ritual.

## 212. Print color texture — chroma budget
- Low saturation reads more premium because ink on paper never reaches screen RGB saturation (narrow CMYK gamut, paper absorbs ink, ambient light grays it down); deliberately lowering chroma borrows print's texture memory.
- Large background areas: oklch chroma 0.01–0.04 (paper feel, not harsh).
- Brand primary / accent: chroma 0.08–0.15 (ink feel, eye-catching but not plasticky).
- Small highlights (buttons/links): chroma 0.15–0.22 (keeps energy; small areas only).
- Full-bleed wash >0.25: use with caution — screen-phosphor look; only for deliberately "electronically native" styles (Wrapped-style, candy).

## 213. Cultural context of hue
- Red: Forbidden City vermilion (orange-leaning, gray-tinged, low L low C, darker/muddier than cola red) → traditional/dignified; cola red (high-saturation true red) → consumer/excitement. Dropping chroma moves it from store shelf to palace wall.
- Blue: Japanese indigo/lapis navy (deep, purplish-gray) → handcrafted/calm; tech blue #0066FF family → SaaS/efficiency. #0066FF is the model's favorite default blue — ask whether you are drawing lots before using it.
- Green: matcha/moss (yellow-leaning, low saturation) → natural/Japanese; neon #39FF14 → terminal/hacker.
- Yellow: gamboge/mustard (brown-gray tinge) → vintage print; warning/Mailchimp yellow → eye-catching/playful. Grayness decides "old book page" vs "hard hat".
- White: cream paper #F5F0E8 → publication/warm; pure #FFF → laboratory/Swiss. A 2% color-temperature shift in the background is a temperament divide.

## 214. Image-generation-only styles (exclude from default pool)
- Exclude these unless the user confirmably has image generation; under pure HTML they become severely degraded mocks. They are not "bad", just the wrong medium (native medium = generated images, not DOM):
  - WebGL particle systems (Active Theory) — impossible in CSS.
  - Generative/algorithmic art (Field.io) — static SVG gives only rigid simplifications.
  - Illustrative gamified interaction (Resn) — needs hand-drawn assets.
  - Real-time creative-coding brushwork (Zach Lieberman).
  - Recursive fractal parameter art (Raven Kwok) — CSS cannot reach the complexity.
  - Cinematic volumetric lighting / concept art (Ash Thorp) — CSS lighting is a degradation.
  - Sci-fi FUI holograms (Territory Studio) — need many layered glow assets.
  - Organic ink-wash bleed (Neo Shen) — CSS gradients ≠ ink wash.
  - Handmade color explosions (Sagmeister & Walsh) — the clashing-color skeleton is doable (merged into Memphis Maximalism and Mono-Brand Type-as-Hero) but handmade texture is not.

## 215. Default aesthetic no-go zone (user brand may override)
- Ban the "GitHub-dark lazy fix": uniform deep-blue base #0D1117 + generic cyan/purple neon glow. Only this overused combo is banned, not all dark styles.
- Keep dark styles with authorial intent: cinematic dramatic lighting, warm cyberpunk (orange/cyan), sports-poetry dark-field narratives, Linear dark glow, black big-number stage, candy lecture stage.
- Ban: aggressive purple-gradient universal formula; emoji as icons; rounded cards with a left colored-border accent (unless the brand uses it); personal signatures/watermarks on cover images.

## 216. Prompting when image generation is available (mood, not layout)
- Prefer short prompts over long; describe mood and content instead of 30 lines of layout detail.
- Diversity killers: specifying color ratios (60/25/15), dictating layout positions, listing every element.
- Creativity sparks: describe mood ("warm like Sunday morning"), cite a specific aesthetic ("Pentagram editorial feel"), describe what the audience should feel.

---

# Part 24 — Web Styles

## 217. Media-Grade Editorial Brutalism (giant grotesk pressing small body text) — Bold · 98%
- Reference: Bloomberg Businessweek (Richard Turley 2010–14 redesign); Neue Haas Grotesk lineage. Use for media/publishing, AI launches, brand heroes, research covers, opinion headers.
- Palette: pure black #000 + pure white #FFF + hyperlink blue #0000EE (underlined), accents signal orange-red #FF433D and terminal green #00A33E.
- Type: Inter (for Helvetica/Neue Haas) + Geist Mono for labels/code. Headline 120px+ left-aligned, tight tracking, set directly on 14–16px body — extreme size contrast.
- Specimen tokens: h1 900 weight 296px, line-height 0.8, letter-spacing −0.075em (CJK −0.09em), nowrap, bleeding near left edge (left 20px); body 16px/1.5 weight 500 in a 350px column with white backing over the headline; masthead 22px/900 −0.03em; mono labels 12–13px weight 600 uppercase +0.04–0.06em; column heads 28px/1.1 900 −0.04em; big stat 76px/0.85 900 −0.06em.
- Grid/rules: modular grid with 1px black column rules and 4px black heavy rules for major breaks (masthead bottom, section top, totals row); 4-column bottom band (1.1fr 1fr 1fr 1fr); right data sidebar with 1px row rules; one inverted black column (white text) as a color block.
- Signature: deliberately no whitespace, high density; red tag chips (#FF433D bg, black 13px mono); colored ■/● category keys in label color; nav strip separated by vertical 1px rules with the final item pushed right in red.
- Implement with CSS Grid + borders, clamp() for oversized type, zero assets.

## 218. Neo-Brutalism Clashing Info Stream — Bold · 95%
- Reference: The Verge 2022 redesign. Use for media, AI aggregators, event landings, rankings, info cards.
- Palette: electric purple #5200FF, magenta #E1306C, bright yellow #F8E000, near-black #08080D, white; specimen adds mint #3CFFD0. Leave clashing blocks unsoftened.
- Type: Space Grotesk (for PolySans) headlines/labels + serif body (Fraunces); CJK headlines 900 −0.03em.
- Specimen tokens: page on #08080D; cards 3px solid #08080D border + hard offset shadow 6px 6px 0 (hero gets white border + magenta 6px shadow); buttons 3px border + 5px 5px 0 shadow, 900 20px; hero h2 72px/1.04; card h3 30px/1.1; numbers 72px/1 −0.05em; body serif 600 16px/1.55; labels 700 13px uppercase +0.08em boxed by 2px currentColor border.
- Layout: grid 1.55fr 1fr 1fr × 1.25fr 1fr, 16px gap, hero spanning two rows; near-zero radius.
- Signature: logo chip yellow with 3px white border rotated −2°; highlighted phrase on yellow rotated −1.5°; rotated "ticket" sticker (8°) overhanging card edge; list rows separated by 3px black rules; photo placeholder as 135° stripes (#6a2bff/#5200FF, 14px); hover = clashing color inversion; "unfinished interface" vibe.

## 219. Memphis Maximalism (clashing blocks + offset overlaps + vintage type) — Bold · 72%
- Reference: Gucci Vault concept store; Memphis movement; Sagmeister's rebellious DNA. Use for concept stores, creative events, brand experiments, Y2K retro, holiday campaigns.
- Palette: aged cream base #EBDDBF + cream #F6EEDC; vintage red #C8382B, mustard #E9A800, cobalt #1F3FA8, purple #6B3FA0, olive #6B7A2A; ink #1B1B1B. Intentionally inharmonious.
- Type: DM Serif Display / heavy CJK serif (title 900 124px/0.95 −0.04em, rotated −4°, second line indented 90px in red with 5px 5px 0 black text-shadow) + Bungee decorative (prices 100px) + Space Mono (nav/info 16–17px bold).
- Texture: dot grain via radial-gradient rgba(60,40,10,.12) 1px on 7px grid.
- Signature: absolutely positioned color blocks rotated ±3–14° (rectangles, circles, CSS-border triangles); vinyl record via repeating-radial-gradient grooves; scattered tag-chip nav (3px border, each rotated differently) as an easter-egg; cards with 3px border + 8px 8px 0 hard shadow rotated ±3–4°; wavy SVG line (6px stroke, round caps); 3×4 dot matrix.
- Downgrade: real aged textures impossible → flat blocks + mix-blend/contrast filters; geometric-collage version holds, archival-aged version degrades — flag it.

## 220. Friendly Geometric Candy (raised 3D buttons, gamified) — Bold · 85%
- Reference: Duolingo (Feather Bold). Use for education, consumer app landings, gamified and mass-friendly products, sign-up pages.
- Palette: Duo green #58CC02 (shadow #58A700), duck yellow #FFC800 (shadow #E5A800), sky blue #1CB0F6 (shadow #1899D6), white base, text #3C3C3C, secondary #777, neutral border #E5E5E5 (shadow #CFCFCF); tinted pills #FFF4CC / #DDF4FF.
- Type: Baloo 2 / Nunito extra-bold (wordmark 800 34px; buttons 900 20px +0.04em; headline CJK 900 62px/1.16 −0.02em; sub 700 22px/1.5).
- Specimen tokens: buttons radius 18px, padding 18px 34px, hard bottom shadow 0 5px 0 darker-same-hue; outline button white + 2px #E5E5E5 border + 0 4px 0 #E5E5E5; stat cards radius 20px, 2px border, 0 4px 0 shadow; panel radius 28px; progress bar 22px tall radius 12px with inset 0 −5px 0 rgba(0,0,0,.12); path nodes 76px circles (current 92px) with 0 7px 0 shadow and a 6px yellow ring; locked node gray.
- Signature: pressable buttons (:active translateY(4px) and drop shadow), super-round corners, mascot slot (CSS shapes/emoji placeholder — slight downgrade), progress bubbles, streak and points pills.

## 221. Pure-CSS Geometric Illustration + Responsive Morphing — Bold · 80%
- Reference: Lynn Fisher (lynnandtonic.com). Use for personal homepages, creative 404s, playful landings, tech blog headers, designer self-promo.
- Palette: 2–4 high-contrast flats, changing per breakpoint. Specimen: cream #FFF3D6 page, navy #14213D art ground/text, sun yellow #FFC93C, teal #2EC4B6, coral #FF5D5D, white.
- Type: Rubik / Archivo bold geometric; headline 900 76px/1.02 −0.03em with one word on a coral highlight block.
- Signature: one set of ~11 div shapes (circles, half-domes radius 999px 999px 0 0, quarter-circles radius 100% 0 0 0, rain-drop bars, striped block via repeating-linear-gradient 14px) recomposed into a different picture at each breakpoint (e.g. 1200 / 760 / 390); show thumbnails of each breakpoint (scale .46) labeled; main art with 12px 12px 0 coral hard shadow; zero images.
- Difficulty is design thinking, not technique; hand-craft each shape.

## 222. Bold Big-Type Editorial (black-and-white fashion poster) — Bold · 88%
- Reference: Jacquemus, Rik Oostenbroek, Domestika. Use for fashion e-commerce, portfolios, features, manifestos, course covers, big-type report versions.
- Palette: black/white + one restrained accent — blush #E8C4C0 or true red.
- Type: Archivo Expanded / Anton display + Playfair Display high-contrast serif. Specimen: CJK serif 350px/0.88 −0.07em stacked one character per line; Anton 150px/0.9 uppercase with a Playfair italic 700 130px word in blush; Anton 90px numeric (e.g. a time "14′20″"); caption heading italic 700 28px; nav 16px +0.14em.
- Layout: hard 1:1 split — white half / black half; giant type wrestling negative space; photo placeholder block in blush; 36px edge margins.
- Signature: screen-filling headlines (vh/clamp), luxury whitespace, left-right counterpoint.

## 223. Cosmic Retro-Futurism (vintage space catalog) — Bold · 75%
- Reference: Perplexity Comet launch site (black/blue/cream; 2001: A Space Odyssey). Use for AI launches, manifesto pages, countdowns, futuristic landings.
- Palette: black #0A0A0A + cream paper #F0EAD8 + cobalt-peacock #2B4F91; muted label blue #aab6cf; low saturation like astronomy catalogs.
- Type: Cormorant Garamond / EB Garamond high-contrast serif + Space Mono. Specimen: CJK serif title 700 118px/1.02 −0.03em with an italic Cormorant 500 64px subtitle in cobalt; lead serif 18px/1.8; mono 13px uppercase +0.1–0.14em for plate numbers, coordinates ("N 31°14′ · E 121°28′") and figure captions ("FIG. 14 — orbit diagram, not to scale").
- Layout: cream panel (~2/3) + black side panel with schedule rows (1px cream-alpha rules, mono dates); outlined CTA with arrow.
- Signature: SVG orbital ellipses rotated −24° (1.2px solid, dashed "3 7", 0.8px outer), a cobalt planet disc with offset outline ring, small black planet dots, cardinal tick marks, one cobalt parabola.
- Downgrade: the "space falling to Earth" video transition → CSS scroll parallax + SVG orbit rotation.

## 224. Cinematic Sound-Viz Dark — Bold · 72%
- Reference: ElevenLabs; Saul Bass titles × audio interfaces. Use for voice/audio AI, music tech, podcasts, media releases, cinematic heroes.
- Palette: #000 base, white text, blue→purple gradient waveform #2F6BFF → #6A5CFF → #B26BFF; muted text #c9c9d6 / #b4b4c6 / #d8d8e6; card border #2a2a38, label #8f93ff.
- Type: Inter / Sora. Headline 900 108px/1.02 −0.04em; sub weight 300 24px/1.5; timestamp Sora 600 40px; card label 500 13px uppercase +0.1em.
- Specimen tokens: full-width waveform of 5px rounded bars (rx 2.5, 8px pitch) symmetric about a center line, opacity .95; left-to-right black fade overlay (rgba .75 → .35 at 35% → 0 at 60%) so the title reads over the wave; 3 cards radius 18px, 1px border, vertical gradient #0d0d16→#050508, 128px tall; white capsule CTA radius 99px.
- Downgrade: live Web Audio/Canvas spectrum impossible in CSS — static waveform or bouncing div bars only.

## 225. Pixel-Game Side-Scroller (8-bit narrative) — Bold · 70%
- Reference: Robby Leonardi's interactive resume (SNES tribute). Use for creative resumes, playful campaigns, gamified landings, easter-egg pages.
- Palette per level: forest green #4CAF50/#2E7D32 + sky #5DADE2; space purple #2C2A4A with volcano orange #E8743B/#8C3A1E; seabed cyan #1ABC9C/#117A65 with foam #BFEFE6; UI night #12101f; highlight yellow #FFE066.
- Type: Press Start 2P / VT323 (HUD 14px, level tags 13px) + bold sans (level names 900 44px with 3px 3px 0 black shadow).
- Specimen tokens: terrain from 16px SVG blocks with 16px lighter top cap (shape-rendering:crispEdges); 4px star pixels; HUD bar 56px with 4px white bottom border, heart blocks 16px; 4px dividers between levels; dialog box 4px white border + double outline (0 0 0 4px night, 0 0 0 8px yellow); pixel buttons 4px border + 4px 4px 0 black shadow.
- Signature: per-level color change, parallax layers, scroll-triggered displacement, image-rendering:pixelated, sprite animation via background-position steps, game-HUD UI.
- Downgrade: hand-drawn pixel characters → simple CSS-block sprites.

## 226. Bauhaus Geometric (geometric mark + flat illustration system) — Neutral · 90%
- Reference: Khan Academy rebrand (Wonder Blocks); Bauhaus composition. Use for education, logo systems, infographics, children's products, event key visuals.
- Palette: red #E63946, yellow #FFB703, blue #0077B6, black #111, warm white #F4F1EA; flat, no gradients.
- Type: Poppins / Manrope geometric. Headline CJK 900 88px/1.0 −0.03em with one word in blue; tag 600 14px uppercase +0.18em led by a red dot.
- Layout: left 3×3 grid of 230×250 tiles, each a flat geometric composition (circles, quarter-circles, half-domes, clip-path triangles, 20px stripes); right info column.
- Signature: 14px black bar with yellow end cap (90px) as a divider; list rows with 2px black top rule, 44px geometric glyph (circle/square/triangle) + title + number; solid red rectangular CTA; no radius except circles.

## 227. Dark Editorial Two-Color Sidebar Portfolio — Neutral · 96%
- Reference: brittanychiang.com v4. Use for portfolios, developer products, tech brand sites, resumes, AI tool landings.
- Palette: navy #0A192F, card #112240, slate text #8892B0, light #A8B2D1, headings #CCD6F6, single neon accent #64FFDA; divider #233554.
- Type: Inter + JetBrains Mono. Name 44px/1.1 700 −0.5px; role 20px 500; body 16px/1.65; nav 13px uppercase +1.6px; dates 12.5px uppercase.
- Layout: left sticky sidebar (~470px, 90px left padding) + right scroll column; section heads "01." in accent mono + title + 1px line flex-filling to the right.
- Signature: nav items with a 32px line that grows to 64px when active; tag pills accent text on rgba(100,255,218,.1) radius 999px 12px; highlighted job card rgba(17,34,64,.7) radius 6px; faint radial blue glow rgba(29,78,216,.15) 520px; hover underline slide-in.

## 228. Warm Editorial (cream paper + terracotta + serif/sans) — Neutral · 97%
- Reference: Anthropic/Claude brand (Styrene × Tiempos); Penguin/Pelican typography. Use for AI product sites, corporate brand sites, long-form reading, ebooks, reports, training.
- Palette: paper #F5F0E8, ink #191919, terracotta #CC785C / #D97757 (specimen clay #C4623F), mute #6B645A, rule #D9D1C3, body #2a2622.
- Type: Fraunces / Newsreader (serif headlines, replacing Tiempos) + Inter (replacing Styrene). Specimen: h1 Fraunces 600 46px/1.25 −0.5px; dek serif 18px/1.8 muted with bottom rule; body serif 17px/1.95; drop cap 66px/.82 clay; side issue number Fraunces italic 76px clay; pull quote italic 20px/1.55 clay with 2px clay top rule; running head and folio 13px +1.5px.
- Layout: book-like single reading column ~560px (max-width), metadata sidebar with hairline-divided label/value pairs, pull quote in the outer margin; line-height ≈1.7–1.95.
- Pitfall: this is the look the model slides into most thoughtlessly (it is Claude's own palette). Use only when chosen deliberately; never let all three directions crowd here; skip it if used recently.

## 229. Linear Dark Glow + Bento (glassmorphism bento) — Neutral · 85%
- Reference: Linear / Cursor ("The Linear Look"). Use for SaaS/AI sites, dev tools, tech heroes, feature showcases, dark dashboard demos.
- Palette: near-black #08090A, brand #5E6AD2, glow gradient #4EA7FC → #B59AFF, text #F7F8F8, muted #8A8F98, hairline rgba(255,255,255,.08).
- Type: Inter / Geist with tight negative tracking + Geist Mono. h1 52px/1.15 600 −1.8px filled with vertical gradient #fff 30% → #8A8F98 via background-clip:text; stat numbers 44px −1.5px in the glow gradient.
- Specimen tokens: top aura radial-gradient (rgba(94,106,210,.55) → rgba(78,167,252,.12) 60%) blurred 30px above the hero; pill badge 13px with brand-tinted border/bg radius 999px; bento grid 1.5fr 1fr 1fr × 2 rows, 14px gap; cards radius 16px, vertical white-alpha gradient .06→.015, 1px hairline, backdrop-filter blur(12px), plus a masked 1px gradient border (blue at 0%, transparent 35–65%, purple at 100%).
- Signature: glowing gradient borders, bento blocks, frosted glass, centered hero, fake product UI from color blocks (downgrade for real screenshots), gradient mini bar charts.

## 230. Angled Fluid Gradient — Neutral · 92%
- Reference: Stripe (gradient banner, Söhne). Use for SaaS/fintech landings, heroes, launches, event banners, AI marketing.
- Palette: gradient band #635BFF → #8A5CFF → #00B8F0 → #7AE6C0 → #FF7AB8 → #FFB35C at 100°; navy text #0A2540; body #425466; meta #697386; rule #E3E8EE.
- Type: Inter / Hanken Grotesk (for Söhne). h1 60px/1.1 700 −2px white on gradient; feature h4 21px −0.3px; numbered labels 13px 700 +1px brand color.
- Specimen tokens: band skewY(−9deg), height ~740px offset upward, plus a soft white radial highlight; capsule buttons (dark navy solid + translucent white outline); floating white receipt card radius 14px, rotated −1.5°, layered shadow 0 30px 60px −12px rgba(50,50,93,.35) + 0 18px 36px −18px rgba(0,0,0,.3); 3-column features each topped with a 2px navy rule.
- Signature: angled cut boundaries, rational grid over expressive gradient; optional slow CSS gradient animation.

## 231. Utility-First Colorful Docs — Neutral · 98%
- Reference: Tailwind CSS docs. Use for technical docs, API refs, design-system sites, tutorials, knowledge bases, help centers.
- Palette: Sky #38BDF8 (active #0EA5E9 / #0284C7), teal→cyan→sky gradient #2DD4BF → #22D3EE → #38BDF8; slate #0F172A / #334155 / #475569 / #64748B / #94A3B8 / #E2E8F0 / #F1F5F9 / #F8FAFC; category hues pink #EC4899, purple #A855F7, green #10B981, amber #F59E0B.
- Type: Inter + JetBrains Mono / Fira Code. h1 36px/1.2 700 −1px; lead 17px/1.7; h2 22px; code 14.5px/1.75.
- Layout: three columns — 272px left nav, ~660px content, ~268px right TOC; 64px top bar; 4px rainbow gradient bar under it.
- Specimen tokens: nav groups headed by a category-colored ● dot; active item with 1px sky left border; code block #0F172A radius 12px with tab bar, syntax: keyword #F472B6, string #7DD3FC, comment #64748B, number #A78BFA, prompt #34D399; note callout #F0F9FF bg, #BAE6FD border, radius 10px; param table with category pills (pink #FCE7F3/#BE185D, purple #F3E8FF/#7E22CE, green #D1FAE5/#047857); search box with ⌘K kbd.
- Only dark-mode toggle/copy needs JS; zero light effects.

## 232. Terminal-Core Soft-Futurism (mono + isometric cubes) — Neutral · 80%
- Reference: Cursor; terminal aesthetics × Teenage Engineering minimalism. Use for AI coding tools, CLI landings, dev infra, terminal products.
- Palette: charcoal #0B0D14, warm white #F2F0EF, muted #8E8D96, hairline rgba(242,240,239,.12); accent purple #9D8CFF, button gradient #7C6CFF → #4F8CFF; terminal green #7CE3B0, orange #FFB38A.
- Type: Geist Mono / JetBrains Mono as protagonist + Inter support. h1 in mono 500 46px/1.3 −1.5px with an accent phrase and a block cursor (0.5em × 0.9em accent bar).
- Specimen tokens: radial purple glow behind terminal; install command chip with "$" + copy; buttons radius 2px; terminal window 1px hairline + rgba(11,13,20,.85) + 0 0 80px purple glow, 36px title bar with three 9px dots, 15px/1.85 mono; ASCII bar charts (█ ░); bento stat strip using 1px gaps on a hairline background (4 cells 1.2fr 1fr 1fr 1fr, mono 20px values).
- Signature: SVG isometric cube (three faces at different alpha fills, accent strokes), restrained gradient glows, industrial minimalism.

## 233. Functional Brutalism (gray hairlines + system fonts + blue links) — Quiet · 98%
- Reference: Are.na / Lobsters / Quartz; Müller-Brockmann grids + Tufte density. Use for communities/UGC, aggregators, knowledge bases, mobile-first feeds, geek products.
- Palette: near-white #FBFBFB, text #111, divider #E0E0E0 (inner #EEE), link #0000EE, visited #551A8B, meta #666; tags #F0F0F0 bg + #CFCFCF border; hot tag #FFE9A8 / #E0C766.
- Type: system-ui stack (-apple-system) / IBM Plex Sans fallback; body 16px/1.4; title links 17px 500 no underline; meta 13.5px.
- Layout: list + 300px sidebar; rows grid 48px vote column (1px right rule) | title | 90px comment count; 9px row padding; sidebar tables with right-aligned counts.
- Signature: hairline gray dividers everywhere, blue links, compact spacing, information density first, no assets, no JS.

## 234. Gallery Dark (deep black void + single large image + EXIF small type) — Quiet · 75%
- Reference: Glass (glass.photo), Bottega Veneta; darkroom + Apple Photos. Use for photo portfolios, luxury e-commerce, immersive visuals, premium product display.
- Palette: #0A0A0A base; artwork supplies the only color; text grays #9A9A9A / #8A8A8A / #7E7E7E, faint EXIF #666, titles #D8D8D8–#E6E6E6.
- Type: Inter weight 300 + optional Cormorant serif (wordmark 21px +3px; work title italic 23px).
- Layout: centered single image ~680×444, huge negative-space frame; caption row beneath: title left, EXIF right in tabular-nums 13px/1.8 (e.g. "ISO 3200 · 35 mm · f/2.0 / 30 s × 42 stacked"); pager "← prev · 07 / 24 · next →" 13px +2px.
- Signature: UI recedes, wide-tracked tiny labels, image owns the viewport. Placeholders lose the soul — fetch real photography.

## 235. Swiss Monochrome (pure black/white + Geist + razor corners) — Quiet · 98%
- Reference: Vercel / Next.js docs; Vignelli. Use for dev docs, tech corporate sites, AI sites, SaaS landings, minimalist reports.
- Palette: #000 / #FFF + grays #888 / #A1A1A1 / #444 / #333 (borders) / #111 (header cell); zero color or a touch of link blue.
- Type: Geist + Geist Mono. h1 76px/1.08 700 −3px; sub 19px/1.6 gray; stat numbers 44px 600 −2px; labels 12px mono +1px.
- Specimen tokens: border-radius 0 everywhere; 1px #333 borders forming a reference table and a 4-column stat grid; one inverted white cell; white solid button + outlined mono button showing an API path; triangle logo glyph.
- Signature: pure black/white, sharp corners, precise grid, triangle/arrow markers, hairline borders.

## 236. Kenya Hara White Gallery (Japanese white box) — Quiet · 80%
- Reference: cosmos.so, Aesop; Kenya Hara's "white" + Swiss grid. Use for high-end e-commerce, creative galleries, curation, portfolios, boutiques, moodboards.
- Palette: #FAFAFA base, #0A0A0A text, faint dividers #EFEFEF, secondary #555/#666; content images supply all color (specimen placeholders in muted coffee tones #D9CFC1, #B8A58E, #6F5A47, #EEEAE4…).
- Type: Inter light (300) / Cooper Hewitt; wordmark 400 15px +8px; nav 13px +4px; captions 12.5px +2px; intro title 300 20px +6px, intro body 14px/2.1 +2px.
- Layout: narrow 200px left intro column + 4-column masonry (28px column gap, staggered column offsets 0/56/0/28px, image heights vary 150–260px); 24px hairline rule as ornament.
- Signature: extreme whitespace, content-first receding UI, waterfall curation. Downgrade: silky inertial scrolling and image entrance easing (≈60% of the premium feel) only approximated with CSS transitions.

---

# Part 25 — Slide / Deck Styles

## 237. Neo-Swiss Billboard Editorial — Bold · 98%
- Reference: big-number editorial AI/SaaS pitch decks (Scribe, Flock Safety), Businessweek infographics, Pentagram. Use for fundraising, QBRs, annual retros, launch key pages.
- Palette: #FFFFFF or #0A0A0A base + one high-saturation accent (electric blue #2D5BFF / neon green #00E676 / brand orange #FF6B2C) + grid lines #E5E5E5.
- Type: Inter / Geist + Geist Mono numbers; tabular-nums, tight tracking.
- Specimen tokens: hero number 900 330px −0.075em in accent with unit at 150px; headline 900 46px/1.2 beneath; header strip mono 13px +0.06em with 2px black underline; 4-column KPI row under a 1px black top rule with #E5E5E5 vertical dividers — mono label 12px, value 700 44px −0.04em (units at 22px), note 16px/1.45 #444; right-aligned context note.
- Master layouts: (1) single-word color-block section page; (2) giant number filling half the screen (≈3.2× the next size) + small caption; (3) left-right split comparison; (4) full-bleed flat line/bar chart (div or inline SVG).
- Signature: billboarding giant type, strict baseline grid, zero illustration, zero 3D.

## 238. Black Big-Number Stage — Bold · 97%
- Reference: Jobs' 2007 iPhone keynote, Lei Jun's Xiaomi SU7 Ultra launch, Spotify Wrapped, Presentation Zen. Use for launch keynotes, thought-leadership talks, all-hands, emotional reviews.
- Palette: #000 + #FFF max contrast; one brand accent per page (Xiaomi orange #FF6900 / Spotify green #1ED760 / Apple blue #2997FF); captions #a1a1a6, footer #86868b.
- Type: Geist / Inter / Source Han Sans (for SF Pro). Specimen: centered number 800 360px −0.07em tabular, decimal point colored accent, unit 800 130px; line 700 44px; one-line comparison 400 22px gray ("Previous generation: 4.7 s."); footer 14px +0.08em.
- Master layouts: centered giant one-liner title; data climax (giant number + unit + one-line caption); two-column parameter comparison (accent vs gray); single-slide slogan. Massive negative space; drop product photos and go pure text (closer to Zen).

## 239. Mono-Brand Type-as-Hero — Bold · 96%
- Reference: Spotify Wrapped, Mailchimp Brand Book (Collins), Netflix red-black. Use for brand/marketing strategy, campaign pitches, culture pages, key visuals.
- Palette: one brand color edge-to-edge (Spotify #1ED760 / Mailchimp #FFE01B / Netflix #E50914) + black or white type — two clashing layers.
- Type: Inter / Manrope / Archivo extra-bold (for Circular/Cavendish); weight 900 + negative letter-spacing so type becomes image.
- Specimen tokens: hero CJK 900 262px/0.9 −0.07em floor-to-ceiling, second line indented 178px; bottom black band 176px tall holding a 900 168px number in brand green + 900 40px statement (key phrase in green) + small right-aligned stats; top-right wordmark 800 16px +0.14em.
- Master layouts: full color block + reversed giant type; two color blocks split top/bottom or left/right; giant numbers filling frame.

## 240. Full-Bleed Gradient Manifesto — Bold · 82%
- Reference: Zuora "Tell a Different Story" (Andy Raskin), Nike "Just Do It", NatGeo spreads. Use for proposal vision pages, brand manifestos, keynote pivots, mission slides.
- Palette: full-bleed CSS gradient (specimen 118° #FF7A18 → #F4413F 46% → #C2186B) or flat bleed; reversed white type.
- Type: Archivo / Anton / Manrope extra-bold. Specimen: Anton 158px/0.92 uppercase three-line slogan; eyebrow 800 16px +0.2em; native-language translation 900 46–56px under a 2px white 70%-alpha rule; bottom row with hashtag slogan (#…) and logistics 800 18px +0.14em.
- Master layouts: gradient + centered manifesto; promised-land vision page; customer logo wall (grayscale SVG/text grid).
- Gradients allowed, particles/light effects not. Missing documentary photography costs ~15% fidelity.

## 241. Candy-Color Lecture Stage (single-concept stage) — Bold · 94%
- Reference: Harvard CS50 (David Malan), Lessig / Takahashi method, Presentation Zen. Use for courseware, tech lectures, concept explanations, code teaching.
- Palette: deep black #0A0A0A with faint vignette (radial ellipse 62% 58% at 50% 42%, #1b1424 → #0A0A0A 72%); rotating candy colors for the giant word — magenta #FF2D95, cyan #00E5FF, yellow #FFD500, green #39FF14.
- Type: Inter extra-bold + JetBrains Mono. Specimen: one concept word 900 300px −0.04em centered in magenta; mono caption 22px cyan written as a code comment ("// …"); code block #141414, 1px #2a2a2a border, radius 10px, 20px/1.55 mono, syntax keyword magenta / function yellow / number green / comment #7a7a7a.
- One concept per screen, minimal text, stage-spotlight feel (vignette, not particles).

## 242. Playful Maximalist Editorial (Collins-style) — Bold · 75%
- Reference: Mailchimp Brand Book (Collins 2018), New Yorker cartoon sensibility, Cooper rounded serif, Cavendish yellow. Use for brands with attitude, agency pitches, culture town halls, anti-SaaS-minimal marketing.
- Palette: fluorescent yellow #FFE01B full field + black #111 + a little clashing color (specimen red #E8472B, blue #2B6BFF).
- Type: Fraunces (adjustable roundness) / Bree Serif replacing Cooper + Inter body. Specimen: CJK serif 900 112px/1.06 headline with one word reversed (yellow on black) rotated −4°; sub serif 500 22px/1.65; kicker 700 15px +0.12em; Fraunces 900 120px number rotated −6°.
- Signature: geometric color blocks (circle, half-dome rotated 14°, black square rotated −8° carrying a number) standing in for the whimsical illustration; white sticky note with 3px black border rotated 3° carrying a self-aware aside ("No renderings on this page. On purpose."); wavy 5px SVG line, round caps.
- Downgrade: the hand-drawn character is the core and is impossible without image generation — ~20% fidelity loss; replace with geometric blocks/emoji/rotated text.

## 243. Irreverent Pop (Reddit-style) — Bold · 80%
- Reference: Reddit Ads sales deck, David Carson typography, 90s web retro, Memphis. Use for Gen-Z brands, meme marketing, creator audiences, deliberately unserious proposals.
- Palette: Reddit orange-red #FF4500 full field + cream window #FFF6D8 + black + yellow #FFE01B + terminal green #39FF14.
- Type: Archivo / Space Grotesk mixed with Inter. Specimen: headline CJK 900 108px with one word struck through (12px orange line-through); outlined giant stat Archivo 900 150px cream with 5px black text-stroke (paint-order stroke fill) + 8px 8px 0 black shadow, rotated 4°.
- Signature: fake OS windows (4px black border, 8px 8px 0 shadow, black title bar "file.exe  _ □ ×") rotated −3° / 1.5°; circular yellow sticker (148px, 4px border, rotated 12°); retro "VISITOR 004812" hit counter in green-on-black; label chips rotated −6°; fun→facts rhythm (a meme page pivoting into a serious data window with yellow-highlighted numbers). No blur shadows.

## 244. Maximalist 3D-Type (Wrapped-style Y2K inflated) — Bold · 78%
- Reference: Spotify Wrapped 2022/2023/2025, Memphis, Y2K, duotone portraits. Use for emotional annual reviews, personal data cards, vertical share cards, year-end.
- Palette: clashing full-bleed magenta #FF2E93 + cyan #00D9E8 (clip-path slanted panel) + orange #FF8A00 bottom band; number yellow #FFE600; duotone #FF2E93 → #2B1BFF.
- Type: Archivo Black / Anton + Clash Display for numbers. Specimen: number 300px −0.06em with stepped text-shadow extrusion (2px increments to 24px, color stepping #FF8A00 → #E0600A → #B03C00 → #7A2400, plus 28px 34px 30px rgba(0,0,0,.35) soft drop) and transform perspective(900px) rotateX(8deg) rotateZ(−5deg).
- Signature: arch-top portrait slot (radius 150px 150px 24px 24px) with duotone gradient + 45° white-line overlay; black pill kicker rotated −3°; hashtag in bottom band; vertical story card variant. Metallic finish → background-clip:text gradient (~15% loss).

## 245. Bento Grid — Neutral · 95%
- Reference: Apple keynote bento era, MBB bento decks (2024–26), Stripe annual-report metric cards, Pitch.com QBR. Use for feature roundups, consulting/QBR data, sales results, metrics pages.
- Palette: #F5F5F7 or cream (or near-black) base + brand primary (specimen #0071E3) + 1–2 accents; text #1d1d1f, secondary #6e6e73 / #424245; track #e8e8ed.
- Type: Inter / Geist + Geist Mono numbers; title 900 40px; mono labels 12px +0.08em; values 800 52px/1 −0.04em tabular (hero card 108px), units 20–34px.
- Specimen tokens: grid-template-areas "a b b c" / "a d e c" / "f f e g" (cols 1.25fr 1fr 1fr 1fr), 16px gap; cards white radius 24px, 1px rgba(0,0,0,.06) border, shadow 0 1px 2px rgba(0,0,0,.04) + 0 8px 24px rgba(0,0,0,.04); hero card filled brand color; one insight per card — number, line icon in 34px tinted rounded square (radius 10px), area sparkline at card bottom (10% fill), 10px progress bar, 16-dot progress grid.
- Signature: unequal-height cards, rounded corners + hairlines, breathing room, zero pasted images.

## 246. Dark Hairline Terminal (Neo-Swiss dark) — Neutral · 94%
- Reference: Linear pitch deck, Vercel design language, CS50; Inter Tight + JetBrains Mono. Use for dev-tool launches, tech roadshows, engineering reporting.
- Palette: near-black #0D0D0F / panel #111113, hairline #262629, single purple-blue accent #5B5BD6 / #7C7CFF; text #EDEDEF, secondary #A1A1AA, mono labels #8B8B93, prompt dim #6B6B73.
- Type: Inter Tight headlines (600 92px/1.08 −0.035em, key phrase in accent) + JetBrains Mono labels (13px uppercase +0.08em).
- Specimen tokens: 1px hairline frame inset 48px; 56px header row with an 8px accent square before the product name; command box 1px hairline on #111113 (16px/1.8 mono); 4-cell stat strip 128px with hairline dividers, values 500 40px.
- Signature: 1px hairline grid, mono labels, extreme whitespace, near-black not pure black; subtle glow via faint border/shadow only. Avoid the #0D1117 deep-blue no-go base — use neutral near-black.

## 247. Two-Font Consulting (Bower-style) — Neutral · 90%
- Reference: McKinsey 2019 brand (Wolff Olins, Bower), BCG Executive Perspectives. Use for consulting reports, exec briefings, industry research, authoritative proposals.
- Palette: deep blue #051C2C × white binary + one highlight (BCG green #00805A; light green #5FD3A6 on dark), warm-gray base #EFEBE4; body #27394A; label #3C4C5B; footer rule #C9C2B6.
- Type: Playfair Display / Fraunces serif headlines + Inter body. Specimen: action title serif 700 44px/1.28 in the top-left (key phrase green); kicker 13px uppercase +0.14em green; body 19px/1.8; numbers serif 700 70px.
- Specimen tokens: thin-line pattern — SVG lines 14px apart rotated −32°, 55% opacity, fading left via gradient, in the top-right corner; 56px × 3px navy rule; data cards white with 3px navy top border, one highlighted card navy with green top border; wide card spanning 2 columns; source footnote 12px under a 1px rule with page number.
- Master layouts: conclusion-style action title top-left; thin-line pattern decor; magazine left/right division (conclusion text + visuals); big-number data cards. Grayscale photo treatment skippable.

## 248. Diagram-Driven Isotype (enterprise diagram arrows) — Neutral · 88%
- Reference: Salesforce decks, Isotype (Neurath), Zelazny's Say It With Charts, Rosling/Gapminder. Use for platform/architecture explainers, customer journeys, process methodologies, ecosystem maps.
- Palette: enterprise blues #1B6FD1 / #2E83E0 / #4A98EC / navy #0B2545 on #F4F7FB; product-line codes orange #E8833A, teal #2BA58A, purple #7B5CC4; base layer #8FA6C4 / #DDE6F2; secondary text #4A5F7A.
- Type: Inter / IBM Plex Sans; title 700 34px; section labels 700 13px +0.12em blue with bilingual tag ("JOURNEY", "PLATFORM").
- Specimen tokens: chevron journey flow — 92px tall steps with clip-path arrow notches (28px), overlapping −12px, darkening per step; layered architecture rows (130px navy label tab + 2px navy bordered cell tray, 6px gaps, base layer muted); 3×3 icon grid of 128px tiles with 2px navy borders and uniform-stroke line icons (2.4px, round caps/joins); color legend of 12px squares.
- Master layouts: horizontal journey arrow flow; layered platform diagram; iconified capability grid; 2×2 / waterfall / pyramid. Process as narrative.

## 249. Diagrammatic Minimalism (single master diagram) — Neutral · 95%
- Reference: Sinek's Golden Circle, Bauhaus abstraction, "one diagram rules the room". Use for theoretical frameworks, TED-style ideas, model visualization, single-concept keynotes.
- Palette: off-white #FAF9F6 + black #111 + one accent (specimen #E4572E) + light gray fill #EDEBE6.
- Type: Manrope / Jost (Futura). Title 900 40px/1.3; body 18px/1.85 with the key word in accent; uppercase labels 26px 700 +3px embedded in shapes, bilingual ("WHAT · …", "HOW · …", "WHY").
- Specimen tokens: three nested circles r 300 / 200 / 100, bottom-aligned (offset centers), 3px black strokes, innermost filled accent with white label; one curved arrow with SVG marker; "inside → out" label; case-comparison block under a 2px rule.
- Master layouts: single geometric master diagram (concentric circles / triangle / matrix); inside-out arrows; contrasting cases.

## 250. Narrative Sparkline (Duarte-style) — Neutral · 91%
- Reference: Nancy Duarte's Resonate sparkline, An Inconvenient Truth. Use for presentation structure, change narratives, before/after, data story arcs.
- Palette: dark #0D1320 (or white) base; past/gray line #B8C2D6; orange turning-point accent #FF8A1F; guide lines #3A4560; labels #9AA6BA.
- Type: Inter + Geist Mono for dates. Title 900 38px/1.3 with key phrase orange; kicker 14px +0.16em.
- Specimen tokens: two dashed reference lines ("WHAT COULD BE" top, "WHAT IS" bottom; 1.5px, dash "3 7"); smooth cubic-Bézier wave oscillating between them (gray 4px stroke, then orange 5px stroke from the turning point on), ending by climbing out of the frame top-right; annotation dots (gray hollow r7 / orange filled r9, 3px stroke) with mono date + caption placed above peaks / below troughs.
- Master layouts: full-width oscillating wave; annotations pinned on the wave; stacked comparison waves; a single line alone on black; progressive reveal via stroke-dashoffset.

## 251. Assertion-Evidence / Tufte Information Design — Quiet · 93%
- Reference: Michael Alley's Assertion-Evidence (validated at Penn State), MBB action titles, Tufte data-ink, Minto pyramid. Use for academic/engineering reports, rigorous consulting pages, policy research, technical reviews.
- Palette: white/very light warm #FFFEFB + black #1A1A1A + one restrained accent (deep blue or brick red #A63A2B); axis text #444, source #666.
- Type: Source Serif / Lora full-sentence title (specimen Source Serif 4 700 38px/1.36, ~1000px wide) + Inter body; chart labels 15px.
- Specimen tokens: one chart under the title; black 2.2px data polyline with 3px dots (endpoints 4.5px); dashed accent least-squares trend (2px, "7 5"); range-frame axes offset 24–30px from the data, spanning only the data range, short 6px ticks; annotations as text beside data points (no legend, no gridlines); source line bottom-left 13px describing data and method.
- Rules: full sentences, not noun phrases; zero bullets; zero chartjunk; high data-ink ratio.

## 252. Institutional Swiss Minimal — Quiet · 96%
- Reference: Sequoia 10-page template, Airbnb 2009 seed deck, Müller-Brockmann, Vignelli. Use for investor roadshows, standard proposals, problem-solution narratives, decoration-free proposals.
- Palette: white + black/gray text (#111 / #333 / #6A6A6A) + one accent (Airbnb coral #FF5A3C; specimen #E5452B).
- Type: Inter / Helvetica Now. Specimen: top title band 176px with 1px bottom rule, accent label 600 14px +0.08em, one-sentence title 700 44px/1.3; three columns (56px gap) each with a 3px black top rule (first column accent), number label, h2 700 26px, body 19px/1.75, and a bottom-anchored big number 700 64px with 18px gray caption.
- Master layouts: centered logo + slogan; top title band + three balanced columns (Problem / Solution / Validation); TAM layered big numbers (nested squares); 2×2 competitor matrix in CSS Grid + borders. One message per slide.

## 253. Editorial Longform (magazine long-form flow) — Quiet · 95%
- Reference: Stripe Annual Letter, Amazon six-pagers, Benedict Evans, Stripe Press. Use for annual letters, long thought pieces, internal updates, research-report reading.
- Palette: off-white #FBFAF8 + deep ink #1B1A22 (body #2B2A33, meta #6A6872) + brand punctuation (Stripe purple #635BFF); card border #DAD7D0, track #E8E5DE.
- Type: Newsreader / Source Serif body + Inter support; tabular numbers. Specimen: masthead 13px +0.14em with 1px ink rule; h1 serif 600 50px/1.25; byline 14px; two-column prose (column-gap 44px) 19px/1.95 justified; pull quote 600 30px/1.45 with 4px purple left border; side giant number serif 500 150px/0.9 −0.04em in purple; inline metric card white + 1px border with 6px progress bar; folio "— 02 —".
- Rules: prose, not bullets; ~65ch line length; inline data cards; oversized numbers as paragraph anchors.

## 254. Humanist Rounded Cards (Khan-style) — Quiet · 80%
- Reference: Khan Academy Wonder Blocks, Source Serif Pro, forest green. Use for education products, approachable courseware, nonprofit decks, warm brand proposals.
- Palette: forest green #14BF96 / #0A5C4B / deep #0A3D32, cream base #FBF6EC, mint tint #D9F2EA, warm accents #F6C453, #EE9B5B, #5B8BD6; placeholder tints #BFE8DB / #F9DDBB / #D5E3F6; note #FFF1CC; chip #F1ECDF.
- Type: Source Serif 4 headlines (700 46px/1.3; card titles 26px) + Nunito Sans / Inter body (19px/1.75; card text 16px/1.65).
- Specimen tokens: pill eyebrow (radius 999px, mint bg, green text 700 14px); green pill CTA; cards white radius 28px, shadow 0 6px 22px rgba(10,61,50,.10), inner photo slot radius 18px built from overlapping colored circles + "photo here" pill; chip row (radius 999px, 14px 700); yellow note card radius 24px rotated 1.2°.
- Downgrade: real teacher/student photography → green-family geometric blocks/emoji figures (~18% loss). Keep the imperfect, approachable warmth.

## 255. Dense Research Report (Meeker-style) — Quiet · 92%
- Reference: Mary Meeker Internet Trends (BOND), CB Insights State of AI, MGI Year in Charts, FT/Bloomberg. Use for trend reports, industry retros, dense briefings, market maps.
- Palette: white + one brand blue (#0066FF; darker label #0050CC; mid #7FAEFF) as stepped monochrome highlight, everything else gray #C4CAD4; KPI tint #F2F6FF; near-zero whitespace.
- Type: Inter + IBM Plex Sans + tabular Geist Mono numbers. Specimen: header 12px +0.08em with 2px blue rule; conclusion-sentence title 900 30px/1.3 (key phrase blue); panel titles "Figure N" 700 14px + gray unit note; KPI values mono 600 34px blue; chart text 12px; footnote 12px/1.5 under 1px #CCC rule with page number.
- Layout: grid 1.25fr 1fr 0.8fr × 2 rows (14px × 24px gaps), tall chart spanning 2 rows; each panel topped by a 1px black rule; bars gray with the highlighted period/last value in blue and bold value labels; stacked bars in blue-ramp.
- Master layouts: conclusion title + full-page single chart; logo-grid market map; KPI cards; dense multi-chart grid + footnotes. Always include source footnotes.

## 256. All-Text Manifesto (Netflix/Amazon-style) — Quiet · 97%
- Reference: Netflix Culture Deck (2009), Amazon six-pagers, Tufte anti-PowerPoint, Matthew Carter. Use for culture manifestos, values talks, deep memos, anti-PPT documents.
- Palette: pure white or black (#0A0A0A) + one accent (Netflix red #E50914) as the only highlight; prose #C9C9C9, emphasis #fff.
- Type: Newsreader / Source Serif (reading-grade) or Inter (manifesto); Archivo extra-bold for titles. Specimen: quote CJK serif 900 58px/1.42 with key clause red; prose 21px/2 in a 640px column; key coined term bold white with a 2px red underline; footer 14px +0.08em.
- Rules: one viewpoint per slide; golden-quote assertion or prose; zero bullets, zero images; candid conversational tone; institutional-term highlights (a named test/practice); appendix as an ultra-minimal table; silent-read document feel.

---

# Part 26 — Infographic / Data Styles

## 257. Infographic family boundary
- Put a deliverable here when it is one image (or a set) with data as the protagonist, readable without interaction. Clickable → web; paged → slides.

## 258. Personal Annual Report (Feltron-style) — Bold · 94%
- Reference: Nicholas Felton Annual Reports 2005–14 (2006–11 in MoMA), Stefanie Posavec, Businessweek specials. Use for personal/team annual summaries, quantified self, product year-in-review, long-cycle audits.
- Palette: uncoated warm white #F3EEE4 + one vermilion through everything #D8341C + slate blue second series #4B6479 + a third color bound to exactly one meaning, never reused (ochre #C99A2E = "rides after 22:00" only); ink #1B1B1B.
- Type: Archivo / Helvetica Neue tight giant numbers + Inter footnotes. Specimen: title 900 26px −0.02em with a red slash; top strip of 5 giant numbers 900 66px/0.95 −0.045em (lead one 86px red) each with 13px unit + italic gray footnote; module heads 700 13px +0.08em prefixed by red module numbers "02".
- Grid: 3px ink rules for major bands, 1px ink rules between modules; dense small type.
- Four-piece master set: giant-number strip; polar period chart (24h or 12 months, stacked colored wedges, hand-computed SVG angles); calendar heat grid (one cell/day, red intensity = value, with legend); a full-width time/geography band. Plus stacked share bar and ranked table.
- Signature: treating trivial personal data like a corporate annual report; must stay readable printed in black and white.

## 259. Explanation Graphics (Nigel Holmes-style) — Bold · 76%
- Reference: Nigel Holmes (TIME 1978–94; Explanation Graphics 1994); center of the chartjunk debate. Use for pop-science, explaining complexity to laypeople, mass-media column art, children's/educational material.
- Palette: 3–4 saturated flats + black outlines; specimen bg #FFE9A8, ink #161616, red #EF4B3C, blue #2E86DE, green #2FB67C, yellow #FFC93C, pink #FF8FB1, violet #B28CFF.
- Type: Nunito / Baloo 2 rounded + Caveat (or a handwritten CJK face) for annotations. Specimen title display 66px/1.12 with one word as a red badge (4px border, radius 14px, rotated −2°, 5px 5px 0 shadow); amounts Baloo 800 34px; handwritten notes 26px rotated ±3° with hand-drawn SVG arrows (4px round strokes).
- Signature: chart drawn as a physical metaphor — banknote stacks (each bill 128×17, 3px outline, radius 5px, alternating ±5px offsets and ±0.7° rotation) where each bill = a fixed amount, stated in a key card (white, 4px border, radius 18px, rotated 1.5°); thermometer gauges, running-track progress; little human figures; thick outlines; zero gradients; humor.
- Downgrade: the soul is hand-drawn illustration; under pure HTML it degrades to geometric blocks — flag it explicitly; generate illustration elements when image generation exists.

## 260. Cross-Section Epic (SCMP Arranz-style) — Bold · 55%
- Reference: Adolfo Arranz (SCMP; Malofiej golds; Kowloon Walled City "City of Anarchy"). Use for architecture/history/machine anatomy, one long sheet holding ten minutes of reading, museum-grade science communication.
- Palette: dark ground (deep ink/brown radial #2A2018 → #1D1711) + warm highlight #FF9A3D + aged paper line color #E9CFA2 + text #F1E3C8 / #E7D8BC.
- Type: Source Serif (titles; specimen CJK serif 900 34px) + Inter callouts (15px/1.5, heads serif 700 18px); kicker 600 14px +0.2em orange.
- Signature: one giant sheet, isometric or straight section; dense numbered callouts (26px orange circles) with leader lines ringing the subject; 45° hatch for poché walls; feTurbulence grain at 10% opacity in screen blend; scale bar ("0 — 10 m section A–A′").
- Rule: pure HTML cannot draw the hand-drawn section — it needs illustration assets; without them do not fake it, switch styles. HTML carries only the callout layer and zoom/scroll interaction.

## 261. Magazine Pop Data (Businessweek-style) — Bold · 90%
- Reference: Businessweek (Turley years), WIRED chart pages, Economist Graphic Detail. Use for business/tech media charts, opinion art, square social images, charts in article posts.
- Palette: two clashing primaries (fluorescent yellow #F6EE00 + black #0E0E0E, or magenta + navy) + paper white #F5F2EA; no third color to soften.
- Type: Archivo Black / Anton condensed heavy + IBM Plex Sans captions; size contrast >10× (specimen: headline display 126px/1.02 stacked one phrase per line on a yellow half-panel; stat Anton 252px "+41%" with 100px superscript %; captions 12px/1.45).
- Signature: one chart, one argument; headline states the conclusion; black bars with yellow Anton values (44px; highlighted final bar wider and 62px) bleeding off the bottom edge; dashed 3px policy-change divider with "before / after →" labels; chart bleeding past the type area via negative margins.

## 262. ISOTYPE Pictorial Statistics (Neurath–Arntz) — Bold · 88%
- Reference: Otto Neurath & Gerd Arntz, 1920s Vienna. Use for population/social/policy data, low-literacy public communication, educational posters.
- Palette: limited spot colors flat-filled — black #1A1A1A, red #C8321F, blue #2A5A89, ochre #D6A022 on paper #F0E8D6; no gradients, no shadows.
- Type: Jost / Archivo (Futura substitutes). Title 700 44px/1.1 with a red 17px +0.28em overline label; category names 900 30px with Latin small caps 14px +0.2em; totals 700 32px.
- Core rule: repeat the same icon N times to show quantity; never enlarge an icon to mean "more" — the heart of the system. Fractions shown by cropping the last icon (half icon = half unit).
- Signature: silhouette icon arrays in horizontal rows (58px icons, 6px gap), text labels on the left, rows between 2px black rules, a key box (3px border) "icon = 200 units; half = 100", top 14px black bar with red segment; extreme order.

## 263. Data Humanism (Lupi-style) — Bold · 80%
- Reference: Giorgia Lupi (Pentagram), Dear Data with Stefanie Posavec; "data is people, not numbers". Use for personal/emotional data, small-sample thick description, private experience as atlas, non-quantified dimensions.
- Palette: journal beige #F5EEDD + ink #2B2620 + 4–5 soft colors each bound to one meaning — coral #E4604A, pine #2E6A58, mustard #DFA22B, ink-violet #5A4080; none decorative. Dot texture rgba(43,38,32,.08) 1px on 22px.
- Type: Georgia / Source Serif titles (900 32px/1.25) + Inter legends (16px); handwritten annotations 22px rotated ±2°.
- Rules: fix a visual language first (size, shape, spike count, tail length each encode one dimension); always include a "how to read this" legend that teaches decoding; arrange elements along an organic dotted Bézier path (1.4px, dash "2 6"), no grid.
- Implement glyphs parametrically in SVG (radius, spikes, tail bound to fields). Only true hand-drawn stroke is out of reach.

## 264. Scrollytelling (The Pudding-style) — Bold · 85%
- Reference: The Pudding, NYT Upshot, Reuters Graphics. Use for complex arguments revealed step by step, long data stories, web-native features.
- Palette: switch by chapter but keep one accent throughout; specimen navy #13213B, accent #FFD23F, text #F4F1E8, muted #8EA0C2, inactive bars #4B6C9E.
- Type: Inter / Source Serif. Inactive steps 500 19px/1.6 at 50% opacity; active step 700 31px/1.4 with highlighter emphasis (linear-gradient transparent 58%, accent 33% alpha 58%).
- Layout: text steps on the left, graphic morphs on the right; vertical progress rail with dots (done / active with 6px accent halo / pending); chapter label "CH.03 / 05".
- Rules: the graphic is never swapped, only morphed; each screen advances exactly one variable; text and graphic strictly bound; show a ghost of the previous state (dashed baseline); threshold line labeled in accent; full panorama at the end.
- Deliverable must be a web page (IntersectionObserver + transitions); exporting to PDF/PNG kills the narrative — don't choose it when a static image is wanted.

## 265. Cartographic Lead (Stamen-style) — Bold · 65%
- Reference: Stamen Design (2001, Watercolor and Toner tiles). Use for geographic distributions, urban/transit/environment, location-as-narrative.
- Palette: the basemap sets the tone (watercolor or monochrome Toner); specimen dark #0E0F10 with text #F2F0EA / #CFCBC2, accent #FF5B2E; graticule white at 7%/16% alternating opacity.
- Type: Inter / IBM Plex Sans (+ IBM Plex Mono for coordinates/kickers 12px +0.14em); title 900 36px/1.2.
- Signature: map fills the type area; restrained high-contrast data layer (proportional circles, flow lines, dashed storm track with time stamps); tiny legend pressed into a corner; geography's shape is the composition.
- Rule: needs real GeoJSON and a basemap — never hand-draw a fake map; with data, draw an inline SVG projection; otherwise switch style (or honestly mark the basemap slot with a dashed box).

## 266. Newsroom Chart System (FT-style) — Neutral · 96%
- Reference: FT Chart Doctor and Visual Vocabulary — pick by relationship: Deviation / Correlation / Ranking / Distribution / Change-over-Time / Part-to-Whole / Magnitude / Spatial. Use for finance/industry data, where correct chart type beats pretty, chart series needing one standard.
- Palette: pink-orange newsprint #FFF1E5 + text #33302E, subtitle #66605C, grid #E6D9CE/#E0D2C6; series claret #990F3D, teal #0D7680, navy #0F5499. Single-hue ramp for continuous; contrasting pair for deviations.
- Type: Inter / Source Sans + mono (IBM Plex Mono) for axis figures; kicker 700 13px +0.12em claret; headline 800 38px/1.25 = the takeaway; subtitle 20px stating definitions/index base (e.g. "Jan 2019 = 100").
- Signature: small claret tab (64×10) at the top-left edge; chart stripped of frames, horizontal grid only, baseline (=100) darker 1.4px; source credited bottom-left (non-negotiable); optional "VISUAL VOCABULARY · CHANGE OVER TIME · LINE" tag bottom-right.
- Rule: consult the vocabulary and choose the chart type from the data relationship before aesthetics.

## 267. Computational Portrait (Fathom-style) — Neutral · 78%
- Reference: Ben Fry / Fathom (Processing co-creator; Visualizing Data). Use for very large datasets, letting data grow its own shape, genetics/transit/time series.
- Palette: white or near-black #07080B + hairlines + one hue's transparency stacking (specimen two directions: cool rgb(150,200,255) and warm rgb(255,214,…) additive).
- Type: Inter light (300 38px title with one 500-weight phrase) + Roboto Mono labels 12–13px +0.14em.
- Signature: no summaries — the full data (thousands of individual traces) drawn with hairlines and globalCompositeOperation "lighter" so density forms the figure; shape decided by the algorithm, not layout; minimal axis labels.
- Rule: Canvas mandatory at volume; requires the real full dataset — a small sample cannot produce the density.

## 268. Beautiful Information (McCandless-style) — Neutral · 90%
- Reference: David McCandless, Information is Beautiful. Use for pop-science comparisons, rankings, mass-audience aggregation, shareable charts.
- Palette: many colors, but a harmonized ring of equal lightness and saturation (vary hue only, e.g. hues 205 / 22 / 330 / 145 / 275), not random clashes; page #fbf9f4, text #1c2b33, meta #5a6b73.
- Type: Nunito Sans / Inter; title 900 34px −0.5px with bilingual subtitle and encoding note ("square area = tonnes per year").
- Signature: area-means-quantity chart types (squarified treemap, bubbles, Sankey via SVG Béziers); labels pressed directly onto blocks; legend embedded; dozens of entries in one image; footnote that area uses one scale across the image and color only marks category.

## 269. Open Research Data (Our World in Data-style) — Neutral · 94%
- Reference: Our World in Data (Oxford GCDL) — interactive charts, written definitions, downloadable data. Use for rigorous subjects, data that must survive scrutiny, long-horizon trends.
- Palette: white + well-separated, non-shouting categorical colors (#c15065, #3b6fa3, #2b8c6a) + gray #bdbdbd for non-essential series; top accent bar 6px #a2559c; grid #e4e4e4 dashed "3 3", baseline #999.
- Type: Lato / Inter; headline Playfair Display 700 36px/1.25 (one-sentence takeaway) #4e4e4e; subtitle 17px with definitions and time range; axis 14px.
- Signature: labels at line ends (collision-avoided, ≥19px apart) instead of a legend; highlighted series 2.6px with end dot, grays 1.6px; footer under 1px rule with source, definition/method, and license ("CC BY 4.0, raw CSV downloadable").

## 270. Speculative Tech Diagram (Takram-style) — Neutral · 84%
- Reference: Takram (Tokyo/London design-engineering, speculative design). Use for tech concept diagrams, future scenarios, white-paper art, product-architecture narratives.
- Palette: warm-gray sand #e8e3d6 + low-saturation naturals — moss #7c8f6e, terracotta #b0694c — + metallic gray #8a877a / #6d6b60; text #4a4a44 / #3b3b36.
- Type: Inter light (300) / Noto Sans JP + Cormorant (titles 300 46px/1.3 +0.06em with italic 22px English subtitle); kicker 12px uppercase +0.32em; body 16px/2.1 +0.12em; footnote 12px +0.28em.
- Signature: charts as installations — concentric 300° arc dial (radii 70–270, 0.5px strokes), hour ticks, data as dot sizes, arc stroke widths, hollow circles; generous whitespace; precision-instrument geometry; line weight restrained to 0.5–1px; considered Chinese-English mixed setting.

## 271. Pictogram System (Otl Aicher-style) — Neutral · 92%
- Reference: Otl Aicher, 1972 Munich Olympics; Ulm school grid. Use for flowcharts, wayfinding/guides, multilingual settings, any icon set needing consistency.
- Palette: restricted (Olympic light blue #7fb5da, green #97c46f, silver #c9ced2) + black #111 on #eef1f2.
- Type: Jost / Archivo (Univers substitutes); title 700 36px under a 4px black rule; labels short sans 17px 700 + English caps 12px +0.08em.
- Rules: every icon on one 8×8 grid, equal stroke weight (specimen 11px), only 0° / 45° / 90° directions, butt caps, miter joins; always pair icons with short labels; leave the grid visible (show a large construction tile with white grid lines).
- Layout: 4-column tile grid (162×207 tiles, 6px gaps) of colored squares with icon + label.

## 272. Tufte Small Multiples — Quiet · 95%
- Reference: Tufte, Envisioning Information (small multiples, sparklines). Use for many-dimension comparisons, grouped time series, one variable across dozens of slices.
- Palette: white + black lines (#111, 1.4px) + one accent flagging the anomaly (#c8312b, 2px); baseline #999 0.6px.
- Type: Source Serif titles (600 30px/1.3 — the finding as a sentence) + Inter tiny labels (13px name, 12px peak value right-aligned).
- Fatal rule: all panels share one axis range (e.g. 0–3 m); mismatched ranges destroy comparability.
- Layout: 5×4 grid of identical panels (≈206×118, 16/20px gaps); peak dot per panel; zero legends, zero gridlines; subtitle states the shared scale and what red means.

## 273. Topological Transit Map (Beck/Vignelli-style) — Quiet · 86%
- Reference: Harry Beck 1933 London Underground; Vignelli 1972 NYC Subway. Use for flows, networks, org charts, system topologies — where connections matter more than distance.
- Palette: white + one saturated solid per line (red #e0312b, blue #1c5bb8, green #1f9d55, orange #f08a00).
- Type: Jost / Inter; station names can be caps; title 700 34px; legend 16px with 34×10 line swatches.
- Rules: segments only 0° / 45° / 90°; stations evenly spaced; sacrifice geographic accuracy for readability (state "schematic, not to scale"); interchanges as hollow circles with thick black ring; lines 14px stroke, round joins, butt caps.

## 274. Ma & Emptiness (Kenya Hara-style) — Quiet · 82%
- Reference: Kenya Hara's "White", MUJI — whitespace is a vessel for imagination. Use for brand annual reports, slow narratives, a little important data, occasions demanding gravity.
- Palette: rice-paper white #f7f5ef + ink #2b2a28 + very pale grays #a9a59b / #6b6861 + one tiny dot of vermilion #c4402f.
- Type: Noto Serif SC / Source Han Serif (weights 200–300) + Inter (12px +0.3em). Specimen: one number 200 weight 176px with small unit; one two-line sentence 18px/2 +0.2em; vertical tag 16px +0.5em at top right.
- Layout: one data point per screen, placed off-center at a golden/edge position; tick strip of hairlines (1px, 8px pitch) with one red tick and dot annotated.
- Risk: highest-risk style — whitespace must be composition with a clear visual anchor, or it reads as "page failed to render"; body text still ≥14px — never shrink type for mood.

## 275. Bookcraft Data (Irma Boom-style) — Quiet · 80%
- Reference: Irma Boom (Dutch book designer, MoMA collection). Use for long data reports, annual reports kept like publications, deep image-text content.
- Palette: paper #eee5d0 + one or two inks (red #d5361d, ink #1c1a17); color blocks pressing across whole pages.
- Type: Fraunces / EB Garamond + Archivo contrast. Specimen: number Fraunces 900 312px rotated −90° reversed out of a full-height red block; vertical CJK title 900 64px +0.12em (writing-mode vertical-rl); three-column text 18px/1.62; inline data figures Fraunces 900 40px red inside the prose; section labels Archivo 700 12px +0.2em uppercase with 2px top rule.
- Signature: asymmetric type area, extreme size spread, rotated/vertical text, data embedded in the text flow, chapter pages separated by full-bleed color.
- Paper stock and trim impossible — compensate with typographic tension.

## 276. Scientific Figure Plate — Quiet · 96%
- Reference: Nature/Science figure conventions; USGS/NASA plates. Use for research findings, method comparisons, peer-review texture, multi-panel figures.
- Palette: white + colorblind-safe blue #0072B2 vs orange #E69F00 (never red-green) + gray #555.
- Type: Inter / Source Sans 3 + Roboto Mono tick labels (12px); "Figure 2 | title" 20px; panel letters a b c bold 22px.
- Rules: panels labeled (a)(b)(c); long paragraph caption beneath (16px/1.55) defining each panel, statistics (*P < 0.05, test, correction), mean ± s.e.m., n; error bars with caps; axes with tick marks (1.2px); zero decoration.

## 277. Swiss Grid Report (Müller-Brockmann-style) — Quiet · 97%
- Reference: Grid Systems in Graphic Design; Ulm; Swiss annual-report tradition. Use for corporate/institutional annual reports, long-running document series.
- Palette: white + black + one accent (specimen #e0311f).
- Type: Inter / Archivo (Helvetica substitutes). Specimen: hero number 800 330px/.86 −0.05em red spanning 7 columns; lead h2 700 30px/1.3 in columns 8–12; stats 800 64px −0.03em with 20px units; labels 14px 500.
- Grid: 12 columns of 70px, 24px gutters (1104px total) — optionally show column tints at 3.5% accent; elements snap to columns; flush left, ragged right; 6px black top rule, 2px black rule above stats row.
- Signature: visible grid logic, non-centered setting, hierarchy via size and spacing, never decoration; whitespace that never reads as empty.

---

# Part 27 — App Styles

## 278. App presentation board (shared conventions)
- Present app styles on a display board: 2–3 phone screens (≈360×760, radius 36–52px) staggered in position, scale (0.84–1.18) and sometimes rotation (±2–5°); the composition itself is part of the demonstration. Include one "detail zoom" screen or floating card cropped at a larger scale.
- Phone frame: double ring shadow (0 0 0 9px near-black, 0 0 0 11px mid-gray) + deep drop (0 24–40px 40–80px); a 100×28px black dynamic-island pill at top; 50px status bar (9:41).
- The board background echoes the style (faceplate grid, contour lines, gradient blobs, glow radials).
- Photo/viewfinder slots are gradient placeholders labeled "photo goes here"; avatars are initial-letter dots, never drawn portraits.

## 279. Hardware Panel (Teenage Engineering OP-1 / EP-133) — Bold · 85%
- Use for audio/creation tools, samplers, metronomes, recording and hardware-companion apps, geeky utilities.
- Palette: near-black screen #0B0B0B, signal orange #FF5A1F (pressed edge #C23D0C), off-white keys #E9E9E4 (edge #B4B4AE), dark pads #232323 (edge #151515), light-gray faceplate #D8D8D4 with #C6C6C1 grid lines (50px), labels #8C8C88 / #A7A7A2.
- Type: Doto dot-matrix for LCD readouts (900; 58px main readout, 20–44px secondary) falling back to Space Mono; silkscreen labels all-caps, 13px bold, +0.14em; CJK labels in Noto Sans SC.
- Specimen tokens: 4×4 pad grid (aspect-ratio 1, radius 12px, 10px gap) with "pressed-in thickness" inset 0 −4px 0 darker; knobs 58px radial-gradient (light at 35% 30%) with a 4×18px orange pointer rotated via a CSS variable; faders 26px off-white caps with an orange center tick and 0 3px 0 shadow; waveform editor with orange loop markers and 18% orange region; parameter rows with 1px dividers.
- Rule: exactly one accent per screen — orange only for "currently active"; never flood the screen.

## 280. Liquid Glass (iOS 26 design language) — Bold · 70%
- Reference: Apple Liquid Glass (WWDC 2025; iOS 26 / macOS Tahoe 26) — translucent material refracting surrounding content. Use for native-feel weather/fitness/media apps, system utilities, "content first, controls floating", concept demos.
- Palette: set by the background content — high-saturation gradients (coral #FF9A5A → magenta #F45B8B → indigo #6A4CD6 → #143B8F; teal #0F8F9E → #18C0A8 → #E6F6A8; #1B2A6B → #4D4AC2 → #F27A9B); board gradient #0F2A63 → #2A56C8 → #18A5C9 → #7BE3C6 with blurred color blobs.
- Glass recipe: background linear-gradient(135deg, rgba(255,255,255,.34), rgba(255,255,255,.08)); backdrop-filter blur(22px) saturate(180%); 1px rgba(255,255,255,.45) stroke; inset 0 1.5px 0 rgba(255,255,255,.7) top highlight + inset 0 −1px 0 rgba(255,255,255,.18); drop 0 12px 30px rgba(8,25,70,.28).
- Type: Inter (for SF Pro) + Noto Sans SC; big numbers 84px 700 −3px; card values 54px −2px.
- Layout: content edge to edge; controls float as capsules — 52px circular buttons, cards radius 30px, bottom sheet radius 44px with 44×5 grab handle, tab bar a floating 64px capsule (radius 34px) inset 24px from edges, active tab a lighter pill.
- Pitfall: glass is invisible on flat grounds (reads as gray block) — background must have real color depth. Refraction/specular effects are beyond CSS; state the downgrade.

## 281. Playful Tactile (Not Boring series, Andy Works) — Bold · 70%
- Reference: (Not Boring) Weather/Calculator/Timer/Habits; Habits won a 2022 Apple Design Award; saturated color, haptics, 3D motion. Use for small utilities (timers, habits, weather, calculators), young audiences, a feature "fun enough to screenshot".
- Palette: one full-bleed saturated primary per screen — orange #FF7A2D, lavender #B6A2FF, acid green #D4FF3F — with near-black #1B1330 text; accent yellow #FFE45C, violet toggle #6A3DFF.
- Type: Bricolage Grotesque 800 (giant numbers 66–92px, −3 to −5px) + Noto Sans SC 900.
- Thickness recipe (layered box-shadow): solid bottom edge 0 8px 0 darker hue + inset 0 4px 0 rgba(255,255,255,.55) highlight + 0 16px 20px rgba(0,0,0,.25) soft. Buttons radius 26px; cards radius 30px white with 0 8px 0 rgba(60,30,150,.35).
- Signature: one protagonist per screen (raised dial built from radial-gradient sphere + inner bowl + 26px solid underside; thermometer tube with gradient fill; toggle that visibly presses in via inset shadow); cards tilted −2°; screens rotated ±5°.
- Static images carry only material; haptics/motion exist as transitions only — say so honestly.

## 282. Friendly Fintech (Monzo-style) — Bold · 90%
- Reference: Monzo Hot Coral (~#FF4F40) from the translucent card, deep navy #091723–#14233C, rounded humanist sans, capsule buttons, conversational copy. Use for bookkeeping, saving/budgeting, payments, youth finance — "serious money in a friendly voice".
- Palette: coral #FF4F40 large on top + white rounded panels; pots in pastels yellow #FFD66B, blue #9AD8FF, green #C8F0CE, pink #F9B9E8, purple #D8CBFF; navy #14233C; secondary #6B778C / #55627A; income green #1E9E4F; warm off-white screen #FFF4EF.
- Type: Figtree (for Monzo Sans) + Noto Sans SC; balance 58px+ 800 −2px; screen titles 30px 800 −0.5px.
- Specimen tokens: colored top zone with balance + three capsule actions (white primary, rgba(255,255,255,.22) secondary; radius 30px); white sheet rising like a drawer (radius 34px 34px 0 0); two-column "pots" grid (radius 28px, min-height 150px, 8px progress bar); transaction rows with 46px initial-letter circle icons on lighter/darker tints of the same hue; donut via conic-gradient; navy pill CTA radius 40px.
- Signature: full-bleed brand color, 28–34px radii, capsule buttons, letter icons (no literal pictures), conversational subheads ("where the money went this month").

## 283. Pro Camera (Halide-style) — Bold · 85%
- Reference: Halide (Lux Optics; ADA winner; one-handed, inspired by pro camera controls; Ambrotype typeface mimics etched lettering; histogram, waveform, zebras, focus peaking). Use for camera/recording/measurement/oscilloscope tools, glanceable one-handed adjustment, low-light use.
- Palette: pure black #000 + bright yellow #FFCC00 (selected parameter and center scale line only) + gray-white #EDEDED readouts; ticks #9A9A9A / #CFCFCF; labels #8A8A8A. (Yellow is an orientation choice, not a claim about the product's palette.)
- Type: JetBrains Mono digits/scales (parameter values 20px 500; big readout 120px 500 −6px) + Noto Sans SC labels (13–14px 700 +0.08–0.1em).
- Specimen tokens: viewfinder ~520px gradient placeholder with rule-of-thirds grid (1px white 25%); translucent histogram box (rgba(0,0,0,.55), radius 6px); zebra highlight warning = repeating-linear-gradient 135° yellow 3px stripes every 9px; lens chips .5 / 1× / 3 (selected yellow); bottom parameter row (shutter / ISO / exposure / WB); ruler scale: short ticks 2px every 14px + long ticks 2px every 70px in two layers, ends faded via mask-image (transparent → black 22% → 78% → transparent), 3px yellow center line with glow; 70px shutter ring.
- Rule: exactly one yellow focal point per screen; yellow in at most three places.

## 284. Topo Outdoor (Gaia GPS / AllTrails) — Neutral · 90%
- Use for hiking/cycling/trail-running routes, outdoor logging, camping/map tools, map-as-protagonist mobile UI.
- Palette: parchment #EFEBDA, contour brown #C09A68 (every fifth line bold as index contour, 2.4px vs 1.3px), woodland green #D8E4C4, water blue #BFDDE6, track orange-red #E4572E with white casing; panels #FBFAF2; labels #6B6A58; dark chip #1F2A24; difficulty chips — easy #CFE8CF/#1F5A2A, moderate #FDE6B8/#7A4A00, hard #F6C9C0/#8A2410.
- Type: Barlow Condensed 700 for readouts (40px stats) + Noto Sans SC; labels 13px 700 +0.06em.
- Specimen tokens: track = two stacked paths (9px white under 5px orange, round caps/joins); start/end/waypoint dots with 3px white rings; floating chips radius 12px; bottom stat panel radius 22px with three big numbers (distance / elevation gain / time) + elevation profile area chart (25% fill); list cards radius 18px with mini contour thumbnail (96×72) + difficulty chip; board background carries the same contours.
- Pitfall: contours must be irregular nested closed curves — concentric circles/ellipses read as fake instantly.

## 285. Feed Waterfall (two-column card stream, Xiaohongshu-style) — Neutral · 92%
- Use for content communities, discovery/guide/local-review apps, e-commerce content feeds, any product whose decision entry is "cover image + title".
- Palette: white cards #FFF on light gray #F5F5F7; brand red #FF2442 reserved for the selected-tab underline, the plus button, "follow", and liked state; text #222, meta #777; hashtags #3A5BA8; chips #F4F4F6 (selected #222).
- Type: system CJK sans (Noto Sans SC); card titles 15px/1.35 500 clamped to 2 lines; detail title 20px 700; body 16px/1.7.
- Specimen tokens: two columns, 6px gutter, cards radius 10px, covers of different heights (≈120–220px; ratios ~1:1 to 3:4) for stagger; fixed bottom row: 20px initial-letter avatar + handle + heart icon + like count; top channel tabs with a 22×3px red underline; 84px bottom nav with a red 50×36 rounded-rect plus in the center; detail page with outlined red "follow" pill and a bottom comment bar.
- Implementation: two flex columns (column direction, cards flex:none); line-clamp 2.

## 286. Command Palette (Raycast-style) — Neutral · 90%
- Use for developer/productivity tools, CLI companions, internal ops panels, any product where "search is the action".
- Palette: canvas #07080A (with faint red and blue corner radials at 12–14%), panel #121315, selected row #202225, hairline #242728, footer #0E0F11; text #E8EAEC, secondary #7A7F84; command icon blocks red #FF6363, blue #52A9FF, green #59D499, purple #8A63F5, yellow #FFC531, neutral #3A3E42.
- Type: Inter body + JetBrains Mono keycaps/logs; input 20px; rows 17px 500; group subheads 13px 600 +0.04em.
- Specimen tokens: 62px input row with a 2×24px red cursor bar; grouped single-line list ("Suggestions" / "Commands"), each row: 30px radius-8 color-block icon + name + gray subtitle + right-aligned keycaps; selected row radius 10px light-gray highlight; keycaps = gradient #2B2E31→#1C1E20, 1px #34373A border with darker bottom #111, radius 6px, 0 2px 0 shadow; 52px bottom action bar ("Open command ↵" / "More actions ⌘K"); log view with colored status words.
- Rule: hierarchy through tonal steps, not shadows — only the outer window gets one deep drop (0 40px 90px rgba(0,0,0,.7)). Present desktop panel crop + phone adaptation.

## 287. Health Color-Code (Apple Health / Oura) — Neutral · 92%
- Use for health/sleep/fitness/vitals, dashboards compressing many metrics into "how was today", wearable companions.
- Palette: #000 ground, cards #1C1C1E, tracks #2C2C2E, labels #8E8E93 / #C7C7CC; status semantics blue #3498FF (best), yellow #FFCC00 (middling), red #FF453A (attention); ring colors #FA114F / #92E82A / #1EEAEF; sleep stages #2A2A78 / #3A3AA0 / #5E5CE6 / #64D2FF, awake #FF9F0A.
- Type: Inter + Noto Sans SC; hero score 76px+ 800 −3px; titles 28px 800; labels 14px 700.
- Specimen tokens: rings via SVG circle + stroke-dasharray (track = same hue at low brightness); component bars 8px radius 4px; sleep hypnogram as variable-height columns (3px gap); trend line over a translucent "normal range" band; status pills = translucent same-hue ground (≈16–18% alpha) + same-hue text (#5FB0FF / #FFD43B / #FF6B61), radius 12px; cards radius 22px.
- Rule: color is the conclusion; keep status colors and ring colors in separate lanes on one screen — never blend into a rainbow.

## 288. Native Polish (Things 3-style) — Quiet · 95%
- Reference: Things 3 (Cultured Code; two ADAs; "like a clean, crisp sheet of paper"; This Evening section; titled separators; tasks expand into cards; draggable Magic Plus). Use for native productivity — tasks, to-dos, notes, calendars; heavy daily-use tools; "no fatigue after long use".
- Palette: white #FFF, near-black #1D1D1F, one blue #3478F6 (checkmarks, links, plus button only), yellow star #F6C21B for "Today", gray #8A8F9B secondary; hairline #ECEDF0; section blue #4A62D6; tag #EEF1F6 / #6B7280.
- Type: Inter (or system stack) + Noto Sans SC; large titles 32px 700 −0.5px; rows 17px 500; meta 14px.
- Specimen tokens: rounded-square checkbox 22px, 2px #B9BEC9 border, radius 7px (completed = gray fill #C6CAD3 + rotated check pseudo-element, text struck through #A3A8B3); row hairline indented to start right of the checkbox (left 58px); group titles small bold + underline; moon icon for "This Evening" via inset box-shadow crescent; floating 62px blue circular plus (0 8px 18px rgba(52,120,246,.4)); expanded task card radius 22px with two shadows (0 2px 6px rgba(0,0,0,.06) + 0 26px 60px rgba(40,50,80,.25)); project progress pie via conic-gradient.
- Motion (expand, check) can't show statically — build structure only.

## 289. Gentle Encouragement (Gentler Streak, dark variant) — Quiet · 80%
- Reference: Gentler Streak (Slovenia; 2024 ADA Social Impact; personal progress over comparison; "Activity Path" from rest to active in soft blue-green). The official UI is bright; this is a deep-night variant on its tone. Use for fitness/recovery/sleep/mindfulness, habit products for people who give up easily, turning "falling behind" from guilt into understanding.
- Palette: deep-night gradient #18213A → #202C4A (board to #2B3555), cards #26335A, tracks #1B2644; low-saturation pastels mint #9BE0CC (deep #6FC3B0), lavender #BAC3FA, peach #F4D0A8; text #EAF0FF, labels #9FB0D6 / #A9B8DB; blurred background orbs.
- Type: Nunito rounded + Noto Sans SC; titles 28px 800; big values 40px 800.
- Specimen tokens: only 28px-radius cards stacked vertically; core card = round-capped gradient curve path (mint → lavender → peach) with one white location dot; pastel status pills (18–20% alpha grounds); monthly dot calendar 7 columns (rest days peach at 80% opacity); feeling slider with white knob; mint CTA radius 24px.
- Copy rules: suggestion phrasing ("today is a good day for an easy walk"), never "X% completed"; statements and suggestions only — no red, no exclamation marks, no rankings; "the streak isn't broken — rest is part of the plan".

## 290. Editorial Reader (Matter / Readwise Reader) — Quiet · 90%
- Use for read-it-later, long-form reading, highlight/note management, article/podcast aggregation — products whose goal is "finished reading".
- Palette: warm paper #FBF8F1, ink #26221C, ochre red #B5532A (source names, progress bars, settings values), highlighter yellow #F4D35E; rules #E4DDCC; meta #8B8272; excerpt #5C5547; note bg #F7F2E6; board #DDD6C8.
- Type: Literata + Noto Serif SC body (18px/1.85, justified); serif titles 20–30px; UI labels Inter small sans 13px 600 +0.02–0.08em.
- Specimen tokens: reading queue of pure-text entries — source · duration, serif title, two-line summary, 3px progress line, no thumbnails; narrow centered reading column; dark selection toolbar (#26221C, radius 14px, items with white-space:nowrap so CJK labels never wrap into a vertical stack) with highlight-color dots; highlighter mark = linear-gradient(transparent 12%, yellow 12%, yellow 92%, transparent 92%) (closer to a hand sweep than a flat background); highlight card with 4px yellow left border + note box, radius 6px, deep shadow.

---

# Part 28 — East Asian Design Traditions (cross-medium)

## 291. Premise of East Asian layout
- Treat Chinese layout as its own grammar — vertical setting, type area (the text block), column rules, title slips, Hanzi structure — not "Western style + a Chinese font".
- Every proposal set may draw one East Asian style in addition to the medium-specific one; run the color derivation protocol first.
- Handwritten title slips, aged paper, real photos, lead-type and woodblock texture are impossible in pure HTML/CSS — downgrade honestly and say which.
- Cite designers/works only where verified; a style's visual DNA is a synthesis of its layout language, not a pixel copy of any single work.

## 292. Lü Jingren Bookcraft — Quiet · 85%
- Reference: Lü Jingren, "master of the book jacket" — Zhu Xi's Thousand Character Classic (paper carrying the breath of a stele rubbing), China Memories: Treasures of 5,000 Years (honorable mention, Best Book Design from All Over the World 2009), Elegant Objects in the Sleeve: Suzhou Folding Fans (China's Most Beautiful Book 2010). Book design as a systems project in dialogue with the text (editing, binding, printing as one).
- Use for art-book/annual-report spreads, long features, oral history/archives, exhibition catalogs, slow-reading content; web long-reads; deck chapter title pages.
- Palette: warm paper #F4EFE4 (gutter shade #E6DFCE; desk #D9D2C3), deep ink #26221D, secondary #5C544A / #6D6453, cinnabar #B2301F used in exactly one place (one large character or one seal).
- Type: Noto Serif SC for headings/body (Latin and digits from its built-ins) + Noto Sans SC for running heads and margin-note labels.
- Specimen tokens: two 560×680 pages side by side; gutter linear-gradient shadow (page 92%→100% to #E6DFCE) simulating the binding dent; chapter page = one large cinnabar character (140px) + 36×2px rule + title 600 38px/1.5 +0.14em + sub 16px/2 — everything else whitespace; text page: type area rides high and hugs the gutter, small head margin, very large foot margin; body 17px/2.05 justified, 2em first-line indent, line-height >2; pull line 600 19px with one cinnabar word; fore-edge margin-note column (120px, 13px/1.8, cinnabar 12px labels "Note 01"); 38px cinnabar seal block with one character; tiny running heads and folios (12–13px +0.2em).
- Downgrade: paper fibers, foil, slipcases, page turning → flat paper + shadow.

## 293. Song Block-Print Leaf — Quiet · 80%
- Reference: Song-dynasty woodblock leaf format — frame (Northern Song mostly double-ruled left/right; Southern Song adds thin black fold lines and ear tabs), ruled column grid, center-seam fish-tail marks (single black, double black, floral) carrying short title and leaf number; Zhejiang editions neat and orderly, Sichuan editions stately and vigorous with airy pages; collectors' vermilion collation marks.
- Use for observation/archival/source-document pages, a report's "raw record" pages, culture-brand content, deck quote pages, features needing an "ancient-book" feel.
- Palette: pale yellow paper #EDE0BC (desk #E4D6B0, inner vignette inset 0 0 60px rgba(120,90,30,.18)), ink #1F1B16, vermilion #B3261E; caption brown #6B5A36.
- Type: Noto Serif TC (traditional woodblock body; closest to a Song cut); Noto Serif SC for simplified content; avoid Latin, or keep it in the body family.
- Specimen tokens: one leaf centered with frame thick outside / thin inside (2px border + 1px outline offset 5px); vertical columns 53px wide with 1px column rules, 27px text, right-to-left order (row-reverse flex, writing-mode vertical-rl); center seam 84px wide with 5px black fold bands and clip-path inverted-triangle fish tails (34×26), vertical abbreviated title (25px +0.3em) and leaf number, carver's name at bottom; vermilion annotations as small vertical red characters (17px) in the head margin; red emphasis dots via text-emphasis (filled circle, over right) and small red rings (9px) beside key words; red 34px seal.
- Rule: no ornament anywhere on the leaf — every bit of information lives inside the rules.
- Downgrade: uneven ink density, irregular stroke weight, damaged paper → uniform ink + pale yellow tone.

## 294. Republic-Era Book Jacket — Neutral · 70%
- Reference: covers of the Lu Xun / Tao Yuanqing generation — Tao designed Wandering (1926), The Grave, Dawn Blossoms Plucked at Dusk, Tales of the Tang and Song; Lu Xun designed covers himself (e.g. Call to Arms), mostly type-driven, spare.
- Use for book covers and flat-lay jackets, album/script/travelogue covers, culture landing heroes, exhibition posters, cultural packaging.
- Palette: three colors in all — low-saturation earthy yellow / gray-green paper (specimen #CFC3A0; desk #BDB6A6), ink #1E1B17, a touch of vermilion #B02A1C; slip paper #EFE8D3; secondary #4B4338.
- Type: LXGW WenKai (handwritten kai) for titles and slips (alternative Ma Shan Zheng, heavier and rougher); Noto Serif SC for author/captions; almost no Latin.
- Specimen tokens: back (470) / spine (70) / front (560) laid flat in three columns; fine double-line border (2px + 1px inset 5px) inset 30px; white title slip 92×300 with 1px border, title vertical 76px +0.14em; author and subtitle as vertical lines (19px +0.3em; 15px +0.22em); spine title vertical 34px and a 20px vermilion square; motifs as flat geometric shapes (mountains, sun, ripples) with hatching; barcode box and imprint/price line on back; large whitespace.
- Downgrade: handwritten slip → handwritten-kai font; aged paper, foil, misregistered color → flat paper.

## 295. Shanghai Moderne Deco (calendar poster) — Bold · 78%
- Reference: yuefenpai calendar-poster ads (late-Qing Shanghai, peak 1920s–30s; painters Zheng Mantuo, Hang Zhiying, Xu Yongqing; carbon-dust watercolor); 1930s–40s Shanghai Art Deco read as "modeng".
- Use for posters, brand promo pages, coffee/tea/food packaging and campaigns, retro landings, calendars and seasonal material.
- Palette: deep ink-green #17352F, gold #C9A24A (bright #E6BE5B), vermilion #9E2A1D (light #E6684F), cream paper #EBD9AE / #F6E7C0.
- Type: ZCOOL XiaoWei display for headlines (92px/1.0 +0.04em vermilion with solid offset text-shadow 5px 5px 0 gold) + Noto Serif SC 900 subheads + Noto Sans SC calendar/small text (Latin digits ride along; swap Latin to Josefin Sans for stronger Deco).
- Specimen tokens: double frame — 6px gold outer border + 2px dark inner line inset 8px; left art panel on deep green with symmetric geometry: radiating fans (suns), concentric circles, stepped ziggurat towers; embedded calendar panel (7-column grid, tabular numerals, gold weekday heads, Sunday in red, today in a vermilion cell, month in display face with English name +0.3em); vermilion bottom strip with shop name and address (700 18px +0.24em); era-style date line.
- Downgrade: carbon-dust portraits impossible (and don't draw portraits in SVG) → pure geometry; a geometric coffee cup replaces the human figure.

## 296. Experimental Hanzi Poster — Bold · 85%
- Reference: Han Jiaying (b. 1961 Tianjin, AGI; Hanzi "from stroke to structure, from character to page, from surface to space"; V&A collection); Kan Tai-keung (b. 1942 HK; Hanzi + ink wash; Bank of China logo from an ancient coin). Common thread: Hanzi as structural material to take apart.
- Use for exhibition/event posters, manifesto pages, deck covers/section pages, feature long-image heroes, course covers.
- Palette: black #0E0E0E + paper white #EFEBE1 + one accent (vermilion #E4351E); text #222, meta #555.
- Type: Noto Sans SC 900 titles (64px/1.1, emphasis words switch to accent) + Noto Serif SC lead-in (18px/1.8); the giant character uses no font — build it from geometric blocks.
- Specimen tokens: one character ~600×700 filling half the frame, broken by stroke into independent blocks, some displaced or swapped for a slash of accent color; right column: row of 80px stroke-breakdown cards (2px top rule, numbered 1–5, stroke names) reusing the same paths with one stroke highlighted; info grid with accent labels (900 +0.2em) under a 2px rule; vertical side notes 13px +0.3em; bilingual mono-ish kicker ("SHI · 5 STROKES").
- Rules: verify stroke count and order first; choose characters with 4–6 strokes; complex characters don't suit.

## 297. Hong Kong Street Signs — Bold · 80%
- Reference: HK hand-lettered and neon signs; 1940s–70s "Beiwei" lettering (square forms, crisp entries/exits/turns) popularized by Au Kin-kung, Su Shijie, Cheuk Siu-hang; vertical, stacked, CJK+English; HK Neon Signs archive (400+ documented since 2015).
- Use for retail/F&B/record-store/night-market brands, event posters, promo landings, nightlife features, decks needing "live on the street".
- Palette: midnight wall #0C0D16 → #171826 with faint 2px brick-grid lines (rgba white 3.5%); signs in saturated solids — red #D5201A, yellow #F7C600, blue #133B96, green #0E8A55 — framed in cream #FFF1C9 with outer glow (0 0 30–40px same-hue at 40–55%); LED board #120808 with red #FF3B2E glowing text; chalkboard #201C28. (Palette is a synthesis of night signage, not sourced sign by sign.)
- Type: Noto Sans TC 900 (vertical/small signs; main vertical 138px/1.02 with 6px 6px 0 dark-red hard shadow) + Noto Serif TC 900 (horizontal sign titles 84px with 5px 5px 0 navy shadow) + Archivo Black (English subheads 17px +0.34em).
- Signature: signs stacked floor upon floor — one vertical sign pinning the next, horizontals layered and occluding; cream double frames (8px border + 4px same-color ring); a small red LED board; a handwritten chalkboard price list with dashed row dividers and tabular yellow prices; power lines (2px dark, slightly rotated) crossing the frame; dense info, big type.
- Downgrade: real Beiwei brushwork and bent neon tubes → heavy Noto Sans + Noto Serif display weights.

## 298. Traditional Chinese Colors · Solar-Term Palette — Neutral · 90%
- Reference: Traditional Colors of China: The Aesthetics of Color in the Forbidden City (Guo Hao & Li Jianming; organized by the four seasons; 384 colors; 24 solar-term color cards). Beginning of Spring maps to names like piaobi (pale jade blue), huangbaiyou (drifting yellow-white), songhua (pine pollen), xiangye (pale leaf yellow), haitianxia (sea-sky sunset glow).
- Use for web heroes, seasonal/time-based products, deck contents pages, travel/outdoors, brand palette pages, infographics with a built-in timeline.
- Palette: organize by traditional color names, not "red/green/blue". Specimen bar sequence (solar term → color name → approx hex): Beginning of Spring pale jade #8CC7B5; Rain Water willow-dyed #B4C98B; Awakening of Insects bean green #A3B87A; Spring Equinox peach-bloom #F0AEB2; Clear and Bright bamboo green #789262; Grain Rain sky-water jade #5FB3A1; Beginning of Summer turquoise #2B9C8E; Lesser Fullness pale leaf yellow #D8C26A; Grain in Ear gamboge #F2B91A; Summer Solstice azurite #1B5E9B; Minor Heat moon white #CFE8EE; Major Heat lotus red #E27A8B; Beginning of Autumn autumn-fragrance #C9B03A; End of Heat apricot yellow #F2A93A; White Dew undyed silk #EEE9DC; Autumn Equinox amber #C1832B; Cold Dew cinnabar #D8411F; Frost's Descent ochre #A05A3A; Beginning of Winter dai blue-black #3C4558; Minor Snow crow-blue #4B5666; Major Snow plain #E6E3DA; Winter Solstice ink #26241F; Minor Cold indigo #2B4A6B; Major Cold cang gray-blue #6B7B8C. Page base warm paper #F5F0E4 + ink #26221D; current term's color (cinnabar) becomes the page accent.
- Type: Noto Serif SC (hero 900 84px/1.14; body 19px/1.95; color names vertical 600 21px +0.2em) + Noto Sans SC (nav 15px +0.16em; labels; solar-term names vertical 13px).
- Signature: 24 vertical color bars across the page bottom (162px tall), each labeled with term and color name; the current term's bar rises (232px), widens (flex 1.6), enlarges its label; text color auto-switches dark/light by bar luminance; "solar term = navigation" (the unique layout move); body on warm paper + ink, pattern restrained to nearly nothing; info card with 1px ink border and 4-swatch strip; nav active item underlined in accent.
- Pitfall: hexes approximate each name (sources differ); in real projects use colors you source yourself — not a standard color card.

## 299. Sugiura Information Mandala — Bold · 72%
- Reference: Kohei Sugiura (b. 1932 Tokyo; researcher of Asian imagery; mandalas and Asian cosmology; "all things reflecting one another"; ~5,000 books incl. ~1,700 Kodansha Gendai Shinsho covers; Time-Distance Map diagrams; "Mandala" exhibition 1980).
- Use for infographics, event posters, annual/cyclical data pages, pop-science features, deck overview pages.
- Palette: near-black warm base #14110E + gold #D9A93B + vermilion #D8402A + off-white #EDE6D3 (secondary #CFC8B5, fine #8F897A).
- Type: Noto Serif SC (large vertical title 900 62px/1.12 +0.08em in gold; ring text; vertical subtitle 17px +0.3em) + Noto Sans SC (captions 16px/1.65; labels 13px 700 +0.22em vermilion).
- Signature: centered concentric ring chart — outer ring solar terms + tick marks, middle ring colored sectors (e.g. visible star regions), inner ring 12 small moon-phase circles, one red dot at center; numbered dots with leader lines to captions around it (①②③④); a time-distance map strip (bottom-left); a data table with 2px top rule and gold tabular values; vertical and horizontal setting coexisting; high density but every block maps to a disc position. Generate sectors, ticks and circumferential rotated text by script.
- Downgrade: overprints, special inks, spine-spanning designs → flat fills.

## 300. Ikko Tanaka Geometric — Neutral · 90%
- Reference: Ikko Tanaka (1930–2002), fusing Japanese tradition with the International Style; Nihon Buyo poster (1981, geisha built from squares/rectangles on a grid); Seibu Theatre posters from 1973; Seibu Group CD from 1975; co-founded MUJI's visual identity from 1980; draws on Rinpa.
- Use for exhibition/film-festival/performance posters, manifesto pages, deck covers, cultural-institution heroes.
- Palette: rice paper #F1EBDD, red #D9381E, black #1A1A1A, mustard #E6B52A, a touch of steel blue #3C6E8F.
- Type: Noto Serif SC 900 large vertical title (108px +0.06em) + Noto Sans SC info (17px/1.7) + Zen Kaku Gothic New small English (15px +0.38em vertical; labels 13px +0.3em red).
- Specimen tokens: 560px square art on a 70px unit grid (cells 280 / 140 / 70) — squares, circles, quarter-circles (border-radius on one corner), semicircles; stripe band via repeating-linear-gradient 35px (theater curtain); info grouped under small red labels (Dates / Venue / Theme / Tickets); 2px black rule at the bottom; 26px red sun dot. Fans, sun, stripes = traditional motifs transcribed into geometry.
- Downgrade: silkscreen registration, paper grain → flat fills.

## 301. Hattori Playful Offset — Bold · 75%
- Reference: Kazunari Hattori (b. 1964 Tokyo; AD, Tama Art University professor; Kewpie Half ads, Ryūkō Tsūshin AD, Mitsubishi Ichigokan Museum logo; Yusaku Kamekura Award 2004); signature: replacing halftone dots with stripes (from his 2007 "Flag" poster).
- Use for posters, covers, event/media brand pages, weather/lifestyle content that should feel "not serious but very deliberate".
- Palette: paper #F3EFE2, ink #111, stripe blue #2F7FF2 and coral-red #F0553E, yellow #F2DE2B.
- Type: Noto Sans SC 900 (giant characters 640px; digits 74px tabular) + ZCOOL KuaiLe playful titles (60px, each character riding higher/lower than the last) + Noto Sans SC info column.
- Specimen tokens: giant character filled with horizontal stripes via background-clip:text + repeating-linear-gradient (9px stripe / 9px gap), duplicated in a second color and offset ~36px/30px like misregistered overprint; tilted solid blocks (yellow rotated 6°, black rotated −4° holding reversed numbers, coral circle 150px); one thick hand-drawn wavy SVG line (round caps); info rows dead straight with 3px black rules.
- Rules: concentrate playfulness in one place; keep the info column rigid; pick low-stroke characters (e.g. the characters for water, mountain, cloud) — complex ones turn to mush.

## 302. Sato Minimal Symbol — Neutral · 92%
- Reference: Kashiwa Sato — 2006 UNIQLO rebrand (red square + heavy white lettering + katakana, red/white evoking the Japanese flag); AD of the Cupnoodles Museum; "a brand needs one strong symbol".
- Use for brand launches, product landings, deck covers, app splash screens, startup heroes.
- Palette: at most three colors — solid red ≈#E60012 full-bleed half, white, black #111; a hint of blue #0B5FFF in the system swatch; body gray #444 / #555.
- Type: Noto Sans SC 900 (logotype character 330px −0.04em white; headline 54px/1.32) + Archivo 800/900 Latin/digits (romanization 40px +0.5em; stats 30px).
- Specimen tokens: 640px red half with one centered character + spaced romanization; white half info zone with near-zero ornament; 2×2 four-color swatch block (red/black/white-with-border/blue, 40px squares); stat row divided by thick 6px top rules in three colors (red / black / blue); black rectangular CTA with +0.3em tracking.
- Rule: zero images, zero gradients; difficulty is restraint, not implementation.

## 303. Japanese Lifestyle Magazine Dense (POPEYE / BRUTUS) — Neutral · 78%
- Reference: POPEYE (1976, Magazine House, "Magazine for City Boys") and BRUTUS (1980); both logos by AD Seiichi Horiuchi (POPEYE logo 1976; he did every 70s issue; also AD of an・an).
- Use for annual-report/data spreads, city and lifestyle content, deck data pages, guide/checklist long images, infographics.
- Palette: black on white; yellow marker #FFE600; handwritten pen red #E4261B and blue #1A4FD6; heatmap single hue rgba(255,92,0, 0.06→0.99); map ground #F7F7F2.
- Type: Noto Serif SC 900 big headlines (54px/1.12 −0.02em, keyword with yellow marker underline gradient from 58%) + Noto Sans SC body (16px/1.75) + Long Cang handwritten annotations (22px rotated −3°) + Archivo Narrow running heads, folios, big data digits (34px; 12px +0.2em).
- Specimen tokens: two 600px pages side by side split by a 1px rule; left: headline + lede + route map in a 2px-bordered box with numbered black 26px dots and handwritten red/blue notes ("Most congested in the morning!", "dedicated lane here, recommended ◎"); right: 3×3 data grid with heavy 2px top rule + 1px cell rules, each cell number + label + numbered tag, one or two cells accented yellow or black; a 24×7 heatmap grid (13px rows, 2px gaps) + "how to read" note; running heads and page numbers in condensed Latin spanning both pages.
- Note: the "handwritten annotations + diagrams" trait is a synthesis; photo collages and halftone dots impossible — mark photo slots honestly with color blocks.

---

# Part 29 — Social Card Styles (Xiaohongshu image posts, 3:4)

## 304. Social card format and shared kit
- Format: 3:4 vertical images 1242×1660, at most 18 per set, swiped sideways; image 1 is the cover. Render each page as a fixed box; a continuous strip spans n × 1242 px.
- Type floors on a 1242-wide canvas (scaled from 1080-wide body 36 / label 28): body ≥42px (line-height 1.6), labels ≥32px (line-height 1.4); never shrink below when swapping in real content. Edge margin 84px.
- Sample kit tokens (example anchors — derive from the user's brand/content): paper #F7F6F2, dot #D8D6CE, ink #211F1C, ink2 #5C5852, gray #726D66, line #E6E3DB, accent sun yellow #FFD447, accent-tint #FFF1BF, accent text #4D3E00, warm shadow rgb(60,40,0).
- Fonts: display Figtree + Noto Sans SC; sans Noto Sans SC / PingFang SC / Source Han Sans SC; serif Noto Serif SC / Songti SC / Source Han Serif SC; Latin Figtree / Inter.
- Dot-grid paper: radial-gradient dots 2.4px on a 40px grid offset 20px.
- Stickers: cut-out subjects with warm two-layer drop shadow (0 16px 18px at 17% + 0 2px 3px at 12%).
- Page numbers bottom-right "01 / N" in 800 label size +2px tracking.
- All eight specimens use one subject (an open-source bird-sticker project) so only layout differs — borrow the layout, never the topic.

## 305. Specimen Journal (natural-history plate) — Neutral · 90%
- Reference: natural-history plates and nature-magazine covers — fine-rule masthead, oversized serif digits, one hero specimen taking half the page, sidebar of small data. Use for nature, pop-science, culture long-form, knowledge notes needing authority and a magazine feel.
- Visual DNA: dot-grid paper; masthead (Song serif 900 64px +4px) over a 2px ink rule with issue number; one ~330px high-contrast serif digit as protagonist (−10px tracking); hero sticker under the digit, rotated −3°, breaking out of the column rule; 2–3 sidebar facts "big number (serif 900 92px) + two-line caption"; huge serif title (900 126px/1.18); footer with 1px rule and italic Latin species name.
- Inner page: numbered checklist (52px ink circles via CSS counters; highlighted item in accent) + same-numbered dots (56px, white 6px ring) on the hero; a scale ruler (thin 6px line + markers) showing pass line and score.
- Fonts: Noto Serif SC 900 (titles, small digits) + Bodoni Moda only for digits ≥100px (thin hairlines of high-contrast serifs break on phones — a "4" reads as "1") + Noto Sans SC body. No downgrades.

## 306. Product Notebook (sticker notebook) — Neutral · 95%
- Reference: the product's own interface (paper surface, capsule buttons, stickers) + native journal/collage notes. Use for your own product/app/brand content so readers recognize "that's the thing" at a glance — friendly, collectible, most native-feeling.
- Visual DNA: the app's paper + dot grid as base; black capsules (72px tall, radius 36px) as labels/step numbers, white variant with soft shadow; giant count (900 230px −8px); 2×3 sticker grid with names; white card radius 44px slightly rotated (−2°) with soft warm shadows (0 22px 50px 12% + 0 2px 6px 6%); translucent yellow tape strip (170×52, rgba(255,212,71,.55)) carrying the big title; stamp labels (accent tint, 3px accent-text border, radius 12px) rotated −6°; highlighter underline (gradient 58%→92%).
- Inner page: white-card "review checklist" — rows 92px with 3px dashed dividers and 54px ink check squares (radius 14px), a ring score (170px circle, 12px accent border), two number cards.
- Fonts: Figtree 900 digits + Noto Sans SC 700/900. No downgrades.

## 307. Index Ink — Bold · 95%
- Reference: Swiss index pages and data annual reports — ink ground, one monochrome accent, even grid, numbered rows. Use for numeric conclusions, rankings, lists, comparisons; covers that must stand out from afar in the feed.
- Cover: ink ground; 340px yellow digit (−14px tracking) across the upper part; 72px title; 5×3 hairline grid of small images (180px cells, 2px rgba(255,255,255,.22) rules) below; huge title 110px.
- Inner page: paper ground; one giant black digit (380px, −16px) + two-line title (96px); 340×22 accent bar; 6px ink rule; numbered table rows (grid 90px number / 330px item / rest description, 2px ink row rules, numbers 800 gray); bottom proportion bar flexed by real values, part solid, part hatch-filled (repeating-linear-gradient), with pass/fail totals (96px, second in gray).
- Fonts: Figtree 900 + Noto Sans SC 900. No downgrades.

## 308. Panorama Strip (continuous carousel) — Bold · 90%
- Reference: horizontal handscrolls, continuous picture books; the "several images join into one picture" swipe. Use for content that lines up: a set of objects, a timeline, a pipeline, a route — built to keep people swiping right.
- Visual DNA: three images are one picture; one through-running line (power line or horizon) links them; the protagonist straddles each seam, ≈2/3 visible on the left image and ≈1/3 on the right; each image still stands alone with its own big digit or title and one sentence; page numbers just 01 02 03.
- Line construction: a cosine sag curve whose period spans two images (≈2484px) with a phase offset so the low point never lands on a seam (base ≈1080px, sag ≈90px, 5px round-cap stroke); stand stickers on the line at their measured claw position (measure each sticker's foot point by hand once); never let text cross a seam — check when slicing.
- Fonts: Figtree 900 + Noto Sans SC 700/900 (digits 160–210px).

## 309. Daily Paper (newspaper front page) — Neutral · 80%
- Reference: newspaper front page — masthead, double rules, headline, column-set body, drop cap, halftone grayscale photo, news-in-brief box. Use for "event" content: launches, retrospectives, deep method write-ups, year-end summaries.
- Visual DNA: newsprint #F2EDE1 + ink #1D1B18 with fine noise (inline SVG feTurbulence fractalNoise baseFrequency .9, 2 octaves, ~8% alpha, 240px tile); Song-serif masthead 900 168px with very wide letter-spacing (+40px), English masthead name in Bodoni Moda; 6px double rule separating masthead from body; headline 900 104px/1.2 with one digit swept by a yellow highlighter (gradient 60%→92%); images desaturated and contrast-boosted (grayscale(1) contrast(1.25) brightness(1.02)); serif body column 500 42px/1.62 justified with a 150px drop cap (::first-letter); boxed brief (3px ink border).
- Inner page: boxed big score (Bodoni), a row of small grayscale diagram images at the bottom.
- Downgrade: true halftone dots impossible — approximated with grayscale + contrast filters.
- Fonts: Noto Serif SC 900/500 + Bodoni Moda.

## 310. Trading Cards — Bold · 85%
- Reference: collectible card games and field-guide cards — gold frames, rarity tags, numbering, stat bars. Use for one-item-per-card collectible lists: species, products, people, tools, cities.
- Visual DNA: dark tabletop radial gradient (120% 80% at 50% 30%, #3A342C → #1E1B17); cards radius 36px with 14px gold gradient frame (135°: #F6D77A → #B98A2E 45% → #F3D27A 70% → #A8781F) around a paper core #FBFAF6 radius 26px; deep shadow 0 30px 60px rgba(0,0,0,.45); cover = one big card over a smaller one tilted −8° / 3°; each card: name, Latin name, rarity tag (radius 12px; e.g. green #2E7D4F / endangered red #C2462E / vulnerable amber #D88A1A), dot-grid image window (radius 18px, 2px dots on 28px), # number, two stat bars (16px, radius 8px, widths computed from real values).
- Inner page: 3×3 card pack (340×400 minis) sorted by one real value.
- Downgrade: foil reflections → multi-stop gradients.
- Fonts: Figtree 800/900 digits + Noto Sans SC 700/900.

## 311. Blank & Vertical — Quiet · 90%
- Reference: vertically set Chinese books and seals; art books with one thing per page. Use for slow content, stories, single-object close-ups, quotable lines; slip one or two into a set to let readers breathe.
- Visual DNA: paper #F8F6F0; vast blank space; large vertical Song-serif title aligned right (900 104–120px, +10–12px tracking, line-height 1.5); thin long vertical subtitle (label size +8px); one vermilion seal (120px square #B8322A, radius 10px, vertical characters 900 44px in #F8E9E2; smaller 96px seal for a score); subject small and isolated landing lower-left; one line of numbering top-left ("No. 3465 / 11064", +6px); short 2px rule + Latin name (Bodoni) at the bottom; inner page vertical body text at body size, line-height 2.
- Rule: whitespace comes from layout, not shrinking type — vertical body text stays ≥42px. No downgrades.
- Fonts: Noto Serif SC 900/500.

## 312. Area Infographic (treemap + waffle) — Neutral · 95%
- Reference: treemaps (Ben Shneiderman, early 1990s) and waffle charts. Use for conclusion pages with hard numbers whose proportions must read at a glance: composition, distribution, completion rates.
- Cover: squarified treemap where area = quantity (≈1074×1180), cells white with 4px paper-colored gaps; big cells embed the hero sticker bottom-right, small cells carry only name + number; cells too small for 32px text get no text and merge into "the remaining N" — never shrink the type.
- Inner page: waffle grid (41 columns of 23.4px cells, 3px gaps, radius 3px), each cell = a fixed quantity (e.g. 1 cell = 10), four color tiers; legend below written with real numbers (44px swatch, 52px 900 numbers, label text).
- Implement squarify in ~20 lines of JS; waffle in CSS Grid. No downgrades.
- Fonts: Figtree 900 + Noto Sans SC 900.

---

# Part 30 — Showcase Lessons (3 philosophies × 8 scenarios)

## 313. Showcase matrix purpose
- Keep a prebuilt set of 8 scenarios × 3 styles = 24 samples to show users "what this style looks like when built" while recommending directions.
- Scenario canvas sizes: article cover 1200×510; deck data slide 1920×1080; vertical infographic 1080×1920; website scenarios (personal homepage, AI tool directory, AI writing tool, SaaS landing page, developer docs) 1440×900.

## 314. Three reference philosophies
- Pentagram / Michael Bierut — information-architecture school: restrained black and white, Swiss grid, strong typographic hierarchy, red accent #E63946.
- Build Studio — minimalist school: luxury whitespace (70%+), subtle weight range (200–600), warm gold #D4A574, refined.
- Takram — Eastern-philosophy school: soft technology feel, natural colors (beige / gray / green), rounded corners, charts treated as art.

## 315. Using showcases in recommendations
- Matching priority: (1) exact scenario match → show that scenario; (2) no exact match but similar type → show the nearest (e.g. "product site" → SaaS landing page); (3) no match → skip samples and generate live.
- Side-by-side comparison: show the same scenario in all three styles together; order Pentagram (rational, restrained) → Build (luxurious minimal) → Takram (soft, warm).

## 316. Pentagram moves by scenario
- Cover: giant red "8" + Swiss grid lines + data bars.
- Deck data slide: a 260px "95.7" anchor number + red / gray / light-gray comparison bar chart.
- Vertical infographic: giant "93→22" before/after number + numbered blocks + CSS data bars.
- Personal homepage: 112px name + Swiss-grid columns + editorial numbering.
- AI directory: square-cornered search box + numbered tool list + uppercase category labels.
- AI writing tool: 86px headline + wireframe editor mockup + grid feature columns.
- SaaS landing: black/white split columns + structured dashboard + 140px "3x" anchor.
- Dev docs: left nav sidebar + square-cornered code blocks + red string highlighting.

## 317. Build moves by scenario
- Cover: ultra-thin-weight single word floating in 70% whitespace + thin warm-gold line.
- Deck data slide: three groups of 120px ultra-thin numbers floating + warm-gold gradient comparison bars.
- Vertical infographic: extreme whitespace + soft-shadow cards + warm-gold connector lines.
- Personal homepage: glassmorphism nav + floating stat cards + ultra-thin weights.
- AI directory: rounded search box + refined white tool cards + pill tags.
- AI writing tool: floating editor card + warm-gold CTA + luxurious writing experience.
- SaaS landing: floating dashboard card + SVG area chart + warm-gold gradient.
- Dev docs: centered floating code card + soft shadow + warm-gold icons.

## 318. Takram moves by scenario
- Cover: 8-node radial flow diagram presented as an artwork on beige.
- Deck data slide: SVG radar chart + three overlaid colors + rounded data cards.
- Vertical infographic: SVG ring chart + organic-curve flow diagram + frosted-glass cards.
- Personal homepage: paper texture + small circular avatar + hairline dividers + asymmetric layout.
- AI directory: organically staggered card layout + soft category tags + diagram-style connections.
- AI writing tool: poetic serif headline + organic editor + flow diagram.
- SaaS landing: rounded bar charts + process nodes + soft earth tones.
- Dev docs: beige code blocks + flow-diagram connections + dashed-border feature cards.

# Part 31 — Animation Principles

## 319. Motion designer identity
- Treat every on-screen element as a physical object with mass, inertia, elasticity and overflow, never as a number being interpolated.
- Aim to make the viewer believe the screen is a space they could reach into; refuse "PowerPoint-style" fade-in/fade-out animation.
- When no rule covers a situation, or rules conflict, decide by taste (the beauty criteria below), not by guessing.
- Break a rule only when you can name which beauty criterion the break serves; if you can't, don't break it.

## 320. Core beliefs
- Animation is physics, not easing curves: each easing choice answers "how heavy is this element, how much friction does it have?" (linear is a number; expoOut is an object).
- Time allocation matters more than curve shape: a uniform rhythm is a tech demo; rhythm makes narrative. Slowing down at the right moment beats the right easing at the wrong moment.
- Yielding to the audience is harder than showing off: pausing ~0.5s before a key result is craft. Default machine output (pause-free, max density) is amateur; practice restraint.

## 321. Taste criteria (what is beautiful)
- Physical weight: at the end of a move the element "lands" steadily, it doesn't merely "stop".
- Yielding: leave a perceivable pause of ≥300ms before key information appears.
- Whitespace: end with an abrupt cut + hold, never a fade to black; the final frame is crisp and decisive.
- Restraint: polish exactly one place in the film to "120%"; keep the other 80% just right. Showing off everywhere is a cheap signal.
- Hand-feel: curves not straight lines; irregularity not mechanical interval rhythm; a sense of breathing.
- Respect: show the tweaking, show bugs being fixed; don't hand over "magic". Present the product as a collaborator, not a magician.

## 322. First-impression self-check
- Optimize only for the audience's first reaction: "fairly smooth" = good (characterless); "really smooth" = good+; "it looks like it floated up off the desk" = great (physical weight achieved); "this doesn't look machine-made" = great+; "I want to screenshot and share this" = great++.
- Correct technique + right taste = great; correct technique + empty taste = good; wrong technique = not in the door.

## 323. Three layers of animation-as-physics
- Layer 1 narrative rhythm: Slow-Fast-Boom-Stop time allocation.
- Layer 2 motion curves: Expo Out / Overshoot / Spring; reject linear.
- Layer 3 expressive language: show process, hand-drawn mouse arcs, logo morph-and-collapse.

## 324. Content first, animation second
- First decide what information to convey, then use motion to serve it; never pick a fancy effect and stuff content into it.
- Treat animation as signal, not decoration: a fade-in says "look here"; if everything fades in the signal dies.
- Write the timeline scene by scene before building components.
- Prepare all images/icons/fonts up front; hunting assets mid-build breaks rhythm.

## 325. Example scene-by-scene timeline (20s explainer)
- 0:00–0:03 problem appears (fade in) → 0:03–0:06 problem expands (zoom + pan) → 0:06–0:09 solution slides in from right → 0:09–0:12 solution explanation (text reveal) → 0:12–0:15 result (count-up + chart reveal) → 0:15–0:18 one-sentence summary held static for 3s → 0:18–0:20 CTA or end.

## 326. Segmented teaching structure
- Split explanation into phases: problem (e.g. 0–4s), approach (4–10s), result (10–16s), with a caption layer that persists across the whole duration (0–20s).
- Overlap adjacent segments slightly (e.g. a second element starting at 2s while the first runs 0–3s) rather than butting them end to end.

## 327. Segment duration and reading speed
- Never let a single narrative segment exceed 10s: say one thing per ≤10s, then move on.
- Budget reading time: ~100–150ms per CJK character, 300–500ms per word; give each sentence at least 3s on screen.
- Don't hold a static frame longer than ~5s; interesting visual change should be dense.

## 328. Process over magic
- Show parameter tweaking and slider dragging rather than one-click perfect results.
- Show an error and its fix rather than one-shot success.
- Show edit redlines (deletions red, additions green) rather than delivering a finished draft at once.
- Doing the opposite of "one-click magic" is the source of brand distinctiveness.

## 329. Neutral base colors with temperature
- Never use pure #FFFFFF or #000000 as the base; use warm or cool neutrals that read as paper / canvas / desktop.
- Take the actual color values from the brand, not from motion rules.

## 330. Serif + sans dual typography
- Use serif for brand/narration ("taste"), sans-serif + monospace for UI/code/data ("function").
- A single font family is always wrong.

## 331. One accent threads every anchor
- Use one accent color as the single thread through all visual anchors (prompt, selected item, cursor, brand hyphen, focus ring). Transfer the method, not a specific palette.

---

# Part 32 — Timing & Easing Tokens

## 332. Default primary easing: expoOut
- Use expoOut = 1 − 2^(−10t) as the default for entries; CSS equivalent cubic-bezier(0.16, 1, 0.3, 1).
- Rationale: its first 30% reaches ~90% of travel, like physical damping / something heavy landing. Plain cubic easeOut 1−(1−t)³ isn't sharp enough (start not fast enough, stop not steady enough).
- Use expoOut for: card rise-in, panel entry, terminal fade, focus overlay, ripple shockwave, brand floating up.
- Still use cubic/quad easeOut for: focus out-ramps, symmetric micro-animations, light motion on secondary elements (caption fades).

## 333. Overshoot
- Use overshoot (easeOutBack, c1 = 1.70158) for toggles, button pops, emphasis interactions; CSS cubic-bezier(0.34, 1.56, 0.64, 1).

## 334. Spring
- Use spring (easeOutElastic, amplitude 1, period 0.3 / 2π/3) for geometry reset, physical settling, UI wobble.
- For adjustable-damping springs use a closed-form (time-pure) spring: dampingFraction 1.0 = calm settle with no overshoot; 0.6–0.7 ≈ the standard elastic bounce; e.g. response 0.4, dampingFraction 0.65; always use the spring's own computed duration.
- Never use frame-integrating real-time spring libraries for rendered output (non-deterministic under seek).

## 335. easeIn / easeOut / easeInOut / linear
- easeIn (t², power1.in): exits, disappearing, anticipation prep segments.
- easeOut (quad): light secondary motion.
- easeInOut (quad, symmetric): continuous motion such as mouse-trajectory interpolation and position changes.
- linear: only constant-velocity mechanical motion (scrolling captions, constant camera pans, time-mapping drivers); forbidden on element effects.
- Rule of thumb: entries expoOut, exits easeIn, toggles overshoot.

## 336. Anticipation curve
- Dip opposite to −0.3 over the first 20% (quadratic), then smoothstep-recover over the remaining 80%.
- Apply only to transforms (y / scale / rotation), never to opacity or color (it overshoots below 0).

## 337. Duration tiers
- Micro-interactions: 0.1–0.3s (button hover, card expand, tooltip).
- UI transitions: 0.3–0.8s (page switch, modal, list item join).
- Narrative segments: 2–10s each (concept phase, chart reveal, scene transition).
- Default tween duration when unspecified: 0.6s with expoOut.

## 338. Frame-based reference (30fps)
- 1f ≈ 33ms; express UI-demo timings in frames (e.g. 3f/char, 8f blink period, 16f push).

## 339. Camera easing tokens
- Active pushes/pulls: power3.inOut (cubic in-out).
- Follow shots / focus shifts: cubic-bezier(0.33, 0, 0.15, 1).
- Large camera pull-back: expo.inOut.
- Background color change between scenes: sine.inOut over ~0.8s, staying in the same hue family.

## 340. Logarithmic zoom duration
- Never use fixed durations for zooms; scale duration with log of zoom ratio: dur = 0.55 × |log2(z2/z1)|, clamped to 0.30–0.94s (so 1→2x = exactly 0.55s and every zoom amplitude has consistent visual speed).
- When the zoom span exceeds 2x, stretch duration logarithmically; no spring overshoot on camera zooms.

## 341. Camera budget
- Space adjacent camera-move starts ≥2.6s apart; allow ≤4–5 camera moves per 15s window; don't zoom by less than 1.25x (too subtle to read).
- Hold ≥1.2s after a camera move lands before moving again.

## 342. Stagger tokens
- Lists/rows/cards: 30ms stagger, translateY 10px→0, ~0.3–0.4s each, expoOut.
- Multi-panel emergence: 30ms each from center outward, y 24→0, scale 0.96→1, 0.5s.
- Batch exits: stagger ≥0.4f by reading order.

---

# Part 33 — Best Practices

## 343. Slow-Fast-Boom-Stop five-segment structure
- S1 Trigger ~15% (slow): give reaction time, establish realism; single action, lots of whitespace.
- S2 Generate ~15% (medium): one clear visual wow moment, no action stacking.
- S3 Process ~40% (fast): show control/density/detail; stagger, text reveals and focus switches live here.
- S4 Boom ~20%: camera pull-back / 3D pop-out / multi-panel emergence.
- S5 Landing ~10% (still): brand mark + abrupt cut; final ~0.5s is a deliberate hold.
- 15s mapping: 2s / 2s / 6s / 3s / 2s.
- Forbid uniform rhythm, sustained high density with no peaks, and fade-out endings.
- Self-check: sketch the climax frame of each of the 5 segments; if the 5 look alike, the rhythm isn't built.

## 344. Mouse trajectory: arc + hand tremor
- Never move a cursor in a straight line; model "accelerate → arc → decelerate with correction → click".
- Use a quadratic Bézier: start → control point offset from the target (e.g. target −200px x, +80px y) → target.
- Add ±2px tremor (noise, or two incommensurate sines), converging to zero near the target.
- Drive with symmetric easeInOut over ~1.1s.
- Click: anticipation shrink to scale 0.85 over ~0.08s (easeIn), then rebound to 1 over ~0.25s with overshoot.

## 345. Logo morph-and-collapse
- Never simply fade a logo in; morph it out of the previous visual in the final 1–2s (morph / rotate / converge) so the narrative collapses onto the brand.
- Low-cost version: collapse the previous element to a color block (scale 1→0.1 over ~0.5s, expoOut, translate toward center, blur 0→6px), then expand the logo from that block (scale 0.1→1 over ~0.6s with overshoot, blur 6→0px), starting ~0.35s into the collapse (~150ms overlap = fast cut with motion blur); hide the collapsed element over 0.15s; then hold — no further motion.

## 346. Focus switch = dim + defocus + flash
- Never change opacity alone; non-focused elements must also blur or they stay "sharp" and don't recede.
- Recipe at intensity f (0→1): brightness 1−0.5f, saturate 1−0.3f, blur 4f px (4–8px range), opacity 0.4 + 0.6(1−f); ramp over ~0.5s expoOut.
- After focus completes, flash a white overlay at the focus point: rgba(255,255,255,0.3)→0 over 150ms ease-out.
- On release, return blur to 0 (≈0.5s, ease in-out) before handing to the next scene; a scene ending mid-blur reads as a render glitch.
- Keep blur on large elements ≤24px; prefer dim + moderate blur over maxed blur.

## 347. Shared-element transition (FLIP)
- When a button becomes an input, transition the same element between two states; never cross-fade two different elements.
- Lay the element out at its final state and express the start state as transform (translate + scaleX/scaleY from start/final ratio, origin top-left), ~0.6s expoOut.
- Delay inner text/placeholder (fade in ~0.3s starting ~0.4s in) to hide scale distortion.

## 348. Breathing expansion (width first, then height)
- Never stretch width and height simultaneously: first 40% of time expand width only (height stays small, ~12%); height starts at ~30% and runs to 100% (overlapping), both expoOut. "Unfold, then fill with water."
- Reveal panel content only after the shell finishes (~75% in), fading in with y 8→0 over ~0.35s.
- If border/corner detail matters, use a fixed shell + clip-path reveal instead of scaling.

## 349. Staggered fade-up
- Delay each row/card by 30ms; translateY 10px→0 and opacity 0→1 over ~30% of the sprite (≈0.3–0.4s), expoOut.
- Never let all entries be plain opacity 0→1; give them direction.

## 350. Hold before key results
- Hover ~0.5s on the loading state before a key result appears — nothing moves; then reveal (e.g. scale 0.94→1, 0.7s expoOut).
- Never cut seamlessly from generation to result.

## 351. Chunk reveal for machine-generated text
- Never pop AI output character-by-character at a constant interval (reads as old movie subtitles).
- Reveal 2–5 characters / a word or punctuation-bounded chunk at a time at irregular 40–120ms intervals; precompute the schedule with a seeded random.

## 352. Anticipation → Action → Follow-through
- Prep: scale 1→0.95 over the first 20% (~0.12s, easeIn).
- Action: 0.95→1.05 over 20–70% (~0.30s, expoOut).
- Follow-through: 1.05→1 over 70–100% (~0.35s, spring/elastic).
- Action alone with no prep and settle looks like PowerPoint.

## 353. D perspective + translateZ layering
- Container perspective 2400px, perspective-origin 50% 30% (slightly looking down).
- Tilt the grid rotateX 8°, rotateY −4° (the "golden" asymmetric angle: camera looking down from the desk's top-left). >10° looks fallen over; <5° reads as shear, not perspective.
- Vary depth per element (e.g. every 3rd +30px, every 5th −20px, every 7th +60px translateZ).
- Entrance: rise from head-on (0°,0°) to 8°/−4° over ~1.4s expoOut.

## 354. Diagonal pan with incommensurate frequencies
- Move X and Y together (diagonal drift), never purely one axis.
- Use different frequencies to avoid closed Lissajous loops: e.g. X = sin(t·0.22)·40px, Y = sin(t·0.35)·30px; or yoyo sine-inOut tweens with periods 4.6s (x 40px) and 2.9s (y 30px). Keep repeat counts finite (cover the visible duration).

## 355. Abrupt-stop ending
- End with no tweens after the logo settles; extend the piece 0.5–1s past the last tween so the final frame holds.
- If there's music, trim it with a ~0.4s volume fade while visuals stay frozen.
- Set end-scene fade-out to 0.

## 356. Number count-up
- Count from 0 to target over ~0.6–1.2s with expoOut, snapping to integers; add thousands separators via locale formatting.

## 357. Basic fade / slide
- Fade-in: complete within the first 30% of the element's time window, then hold opacity 1.
- Slide-in: travel ~100px from the chosen direction, completing in the first 40% of the window, opacity tied to progress, easeOut/expoOut.

## 358. Scene recipe A · Keynote drama
- Use for major launches/hero films where visual wow leads.
- Strong Slow-Fast-Boom-Stop arc; expoOut throughout + a little overshoot.
- SFX density high (~0.4/s), SFX pitched to the music's scale; music: IDM / minimal tech electronica, cool and precise.
- S4 signature: sharp camera pull-back + drop (scale →0.78, y −40px, ~1.1s expo in-out); ending: logo morph → single ethereal note → abrupt cut.

## 359. Scene recipe B · One-take tool film
- Use for developer tools / productivity / flow-state.
- Sustained steady flow, no obvious peaks, no Boom; ending equally abrupt.
- Easing: spring + expoOut (settling, not exploding).
- SFX density 0 — music-driven editing; lo-fi hip-hop / boom-bap at 85–90 BPM (at 88 BPM one bar ≈ 2.73s); place key UI actions exactly on kick/snare transients ("the groove is the interaction sound").

## 360. Scene recipe C · Office efficiency narrative
- Use for enterprise/docs/spreadsheet/calendar products.
- Hard cuts between scenes (fast ~0.15s opacity cuts, not long cross-fades) + dolly in/out (scene enters at scale 1.06→1 over 1.2s expoOut).
- Easing: overshoot for toggles, expoOut for panels.
- SFX density medium (~0.3/s), UI clicks dominant; music: jazzy instrumental, minor key, 90–95 BPM.
- Include exactly one highlight: a 3D pop-out / float-off-the-plane moment, done once.
- Choose one recipe per product; never mix.

## 361. Visual density in briefs
- A brief with only narrative + camera comes back as wireframes; always specify: (1) a visual density standard — magnitude of detail per screen (skeleton rows, legends, textures, secondary elements) plus an acceptance line like "pause on any frame and it doesn't embarrass itself next to the benchmark"; (2) a concrete reference benchmark to borrow workmanship from; (3) a global atmosphere checklist — ground-line anchoring, soft component shadows, paper/surface texture, a personified companion element, idle micro-motion on static parts (breathing / cursor / micro-advance).
- The cure for "empty and boring" is the atmosphere layer, not the primary components.
- Separate motion skeleton (timeline, camera, morph path, text timing) from visual craft (components, density, atmosphere); if motion passes review, re-skin rather than re-choreograph.

## 362. Audio pairing
- Keep a 6–8dB loudness gap between music and SFX.
- Match SFX density to product personality (A/B/C).

## 363. Pre-delivery checklist
- Slow-Fast-Boom-Stop not uniform; default easing expoOut; toggles overshoot; 30ms list stagger; 0.5s hold before key results; chunk reveal for generated text; focus switch includes blur; logo morphs, never fades; no pure black/white base; serif + sans hierarchy; abrupt-cut ending; arced mouse; SFX density per recipe; music/SFX 6–8dB gap.

---

# Part 34 — Pitfalls

## 364. Uniform-speed "transition: all 0.3s ease"
- Symptom: everything moves at the same speed, mechanical. → Fix: expoOut + per-element stagger.

## 365. Opacity-only entrances
- Symptom: no sense of direction. → Fix: pair with translateY 10→0 + anticipation.

## 366. Logo fade-in
- Symptom: no narrative closure. → Fix: morph / converge / collapse-expand.

## 367. Straight-line mouse
- Symptom: subconscious machine feel. → Fix: Bézier arc + ±2px tremor.

## 368. Constant-interval per-character typing for AI output
- Symptom: old-subtitle look. → Fix: chunk reveal at random 40–120ms.

## 369. No pause before key result
- Symptom: viewer misses it. → Fix: 0.5s hold.

## 370. Focus via opacity only
- Symptom: background stays sharp, doesn't recede. → Fix: opacity + brightness + blur.

## 371. Pure black/white backgrounds
- Symptom: cyberpunk look / glare fatigue. → Fix: tinted neutrals.

## 372. Equal speed everywhere
- Symptom: no rhythm. → Fix: Slow-Fast-Boom-Stop.

## 373. Fade-out ending
- Symptom: indecisive tail, video ends dark/transparent. → Fix: abrupt cut, hold last frame, end-scene fade-out = 0.

## 374. Missing positioning anchor
- Symptom: absolutely positioned decorations float off-screen (e.g. 200px below) because they anchor to an outer container. → Fix: give every container of absolute children position: relative; walk ancestors to confirm the anchor.

## 375. Rare glyphs render as tofu
- Symptom: symbols like ␣ ␀ ↩ ⏎ ⌘ ⌥ ⌃ ⇧ show blank. → Fix: confirm every character exists in the chosen fonts; draw metakeys as CSS boxes (inline-flex, padding 4px 14px, 1.5px accent border, radius 4px, mono, 0.3em size, 0.2em tracking, uppercase); verify emoji or use SVG.

## 376. Hard-coded grid counts
- Symptom: grid misaligns when data count changes (6 items, 5 columns). → Fix: drive column count from data (CSS variable) or auto-flow; never pair a fixed CSS number with a data constant.

## 377. Blank gaps between scenes
- Symptom: out-fade 0.6s + in-fade 0.6s + 0.2s stagger ≈ 1s blank; viewers think it froze. → Fix: overlap out and in (start both ~0.4s early as a cross-fade), or keep an anchor element visible across the switch; no pure-blank gap >0.3s.

## 378. Non-seekable animation state
- Symptom: timer-chained states can't be scrubbed back; frame-by-frame renders scramble. → Fix: make render(t) a pure function of t; if side effects are unavoidable, keep a fired-set with explicit reset; no animation timers spanning >1s.

## 379. Measuring before fonts load
- Symptom: positions computed with fallback-font widths stay permanently offset (~500ms later fonts arrive). → Fix: measure only after fonts are ready, plus one extra animation frame to commit layout.

## 380. Blank or loading first frame
- Symptom: video opens on 2s of blank/white flash. → Fix: frame 0 must be the complete initial state with final layout; start the clock only once assets are ready.

## 381. Start-offset / clock drift on boot
- Symptom: loading time counted into the first frame's delta, so the recording starts L seconds in (e.g. starts at t=5, loops, and the true beginning appears at the end). → Fix: initialize the frame clock with a null sentinel so the first tick has dt=0; don't start playing until fonts are ready; signal "t=0" on the same frame as the first render.

## 382. Looping during recording
- Symptom: the last 0.5–1s of the video jumps back to scene 1. → Fix: disable looping when recording; clamp to duration − 0.001s so the final frame persists.

## 383. Warmup frames leaking into the recording
- Symptom: the first seconds show mid-animation then a restart. → Fix: warm up (load fonts) in a separate, unrecorded session; record from a fresh state at t=0. Trimming can't hide warmup frames.

## 384. Debug chrome in the video
- Symptom: progress bars / replay buttons / counters / phase labels appear in the export. → Fix: mark all control/debug chrome as non-recorded and hide it on export.

## 385. Fake player chrome drawn in-frame
- Symptom: a decorative progress bar/timecode ("00:42 ──── PROJECT"), chapter counter "CH 03/06" or version "v0.3.1" collides with real player controls; reads as a bug. → Fix: don't draw progress, timecode, credit bars or chapter counters; every element must belong to a scene's narrative (keep), be control chrome (hide on export), or be deleted. If a bar is narratively essential, make it different in position, form and palette. Check a still frame: anything that looks like player UI, or duplicated progress/time info, goes.

## 386. Hard-coded colors on cross-scene elements
- Symptom: chapter labels/scene numbers/watermarks vanish on a scene with an inverted (dark) background — no error raised. → Fix: inherit currentColor from the scene, offer an invert option, or compute contrast from the scene background; check one representative frame per scene.

## 387. fps by interpolation breaks playback
- Symptom: motion-interpolated 60fps files black-screen in some players. → Fix: default to simple frame duplication for 60fps; use interpolation only after testing in target players. Perceived smoothness gain for CSS animation is minimal; the 60fps label mainly helps platform recognition. Use a broadly compatible H.264 profile (high, level 4.0). Default render 25fps.

## 388. External engine fails on local open
- Symptom: page goes black when double-clicked because externally linked scripts are blocked. → Fix: for single-file delivery, inline the animation engine; verify by opening the file directly with no server.

## 389. CDN dependencies break on restricted networks
- Symptom: framework/compiler/fonts fail to load; JSX runs untranspiled ("Unexpected token '<'"). → Fix: inline frameworks locally, precompile JSX at build time (including the engine itself), use system fonts (e.g. PingFang SC / Songti SC for Chinese), base64-inline images (compress large backgrounds to JPEG first).

## 390. CSS transitions under seek rendering
- Symptom: transition-driven states freeze at the start value or stop randomly in frame-by-frame renders (wall-clock, not timeline). → Fix: express every render-path state change as a tween or pure function of t; likewise ban WAAPI element.animate() and CSS keyframe animation for render-critical motion. Hover transitions in interactive-only states are fine.

## 391. Proxy-driven first frame not painted
- Symptom: frame 0 shows uninitialized DOM because the update callback doesn't fire at t=0. → Fix: explicitly render t=0 (and apply camera state) once after building the timeline.

## 392. Contrast checks vs dark cinematic style
- Symptom: deliberate low-contrast watermarks/labels (16–40% opacity) flood accessibility errors. → Fix: exempt contrast for dark cinematic pieces only; for light informational output enforce WCAG AA 4.5:1, since errors there are real.

## 393. fromTo immediate-render phantoms
- Symptom: short-lived effects (sparks, click circles, ripples, dust) appear seconds before their moment because the visible from-state renders at build time. → Fix: disable immediate render on every fromTo with a visible from-state, or set hidden initially then tween to; check each scene's opening frame for stray effects.

## 394. Use fromTo, not from
- Symptom: from-tweens snapshot start state at registration and misalign after repeated seeking. → Fix: always declare both ends explicitly.

## 395. Tweening layout properties
- Symptom: width/height/top/left/fontSize/letterSpacing/margin/padding snap to integer pixels; slow ease tails "bunch then jump 1px" (letter-spacing jitter). → Fix: scaleX/scaleY + origin for size; x/y offsets for position; scale for font size; per-character x for tracking; hard-code layout and move via transform. Judge by frame comparison, not lint.

## 396. Runtime randomness / clocks
- Symptom: each render differs. → Fix: no Math.random / Date.now / performance.now / input events on the render path; use a seeded PRNG (e.g. mulberry32 with a fixed seed) and pre-generate all random values before building the timeline.

## 397. Infinite repeats
- Symptom: undefined render length. → Fix: no infinite repeat; compute a finite count from visible duration (ceil(D / period)). Don't pad length with empty tweens; set duration explicitly.

## 398. Blurry text under zoom
- Symptom: transform: scale() zoom (esp. in 3D) blurs text; >2x undeliverable, because the browser rasterizes at layout size then enlarges the bitmap. → Fix: zoom the camera layer with layout-level CSS zoom (text re-rasterizes sharp); divide translate by zoom; this is the sole permitted layout-tween exception and only on the world/camera layer. Use 2x full-page screenshots minimum; for close-ups cross-fade in a 4x slice over 6f during the push.

## 399. Flattened 3D
- Symptom: perspective + preserve-3d set but everything renders flat. → Fix: no overflow:hidden, filter, opacity<1 or clip-path on any intermediate layer between camera and 3D children; put such effects only on innermost elements.

## 400. Pan exposes edges
- Symptom: blank borders appear when the camera pans. → Fix: oversize the world by ≥ max pan amplitude + 8% on all sides; backgrounds must cover the bleed; screenshot both endpoints of each pan.

## 401. Camera and element fighting over transforms
- Symptom: messy camera work. → Fix: separate layers — viewport (fixed) → camera (camera transforms only) → world (element animation only); captions/badges in a static HUD sibling.

## 402. Uneven performance from real 3D per card
- Symptom: per-card translateZ + shadow blur on 48 cards drops below 25fps. → Fix: fake depth with 2–3 shadow tiers (≈<5% visual difference, ~10x cheaper).

## 403. Grain overlays kill GIF compression
- Symptom: animated noise makes every frame differ, bloating GIFs. → Fix: drop noise; use base color + warm shadows (keeps ~90% of paper feel, ~60% smaller GIF). Two-pass palette GIF: ~30s 1080p → ~3MB.

## 404. Embedded-player click/focus capture
- Symptom: side paging click zones (e.g. 22vw) swallow the embedded play button; keyboard arrows stop working after clicking inside the embed. → Fix: restrict click zones vertically (e.g. top 12vh, bottom 25vh) to leave the play buttons clear; forward key events and return focus to the parent after clicks.

## 405. Autoplay sound
- Symptom: blocked or intrusive audio. → Fix: start music only after a user play action; provide a small mute button top-right; never force sound on page arrival.

## 406. Timer-chained scheduling
- Symptom: fragile, undebuggable sequencing. → Fix: one global timeline object and a single per-frame render computing all scenes' opacity/transform.

---

# Part 35 — UI Demo / Product Walkthrough Animation

## 407. Core claim
- Quality in product animation comes from real UI + cinematic camera, not effects. One real screenshot with one restrained push-in beats ten layers of hand-built fake UI. If it "lacks tech feel", fix UI realism and camera, never add particles/glow/cyber gradients.

## 408. Visibility invariant
- Keep the cursor and the in-progress UI operation inside the visible area (with an 8% safety margin) at every moment; otherwise reduce zoom, merge shots, or don't shoot it.
- If a target is off-screen, move the camera first, then the cursor ("shot first, then action").

## 409. Visual language grows from the product
- Extract the product's own tokens (typeface, corner radius, palette, grid) and only reuse or restrainedly extend them; borrow motion grammar and pacing, re-skin per product.

## 410. Path choice: screenshot vs rebuild vs hybrid
- Interface only needs to be looked at (push / tour / hover / compare) → real screenshot in a device frame + 2.5D camera moves (hours).
- Interface is the narrative subject with elements entering/responding/changing → pixel-faithful HTML rebuild (days).
- ~90% static, ~10% alive → hybrid: screenshot base + key elements as transparent slices animated at original coordinates (half a day; right for most client work).
- In the hybrid, every slice must settle back into its real slot after animating; a card hovering off-grid reads as fake.
- Hybrid steps: 2x full-page base in a device frame → cut moving elements as slices by coordinate table → cover the baked-in original with a background patch (optionally an accent breathing outline that brightens and vanishes at landing) → animate slice on the patch, ending in its slot → during close-ups cross-fade 4x slices over 6f.
- Use a device frame (browser or desktop window) as the "real software" signal; a bare floating screenshot reads as a sticker. Drop the frame once zoom passes ~2x.
- Asset trio: 2x full-page screenshot (DPR ≥2), transparent element slices (4x preferred), coordinate table {x,y,w,h} per slice.
- No hand-built fake UI or mockup generators; if rebuilding, measure typeface/radius/spacing/icons against the screenshot and compare captured frames side-by-side — "roughly similar" is worse than the screenshot.

## 411. One shot, one form
- Each shot tells one form; each form is protagonist only once per film (forms may recur in other shots).

## 412. Form ① hero close-up / 3D showcase
- Camera: rotateY 34° dominant, rotateX only 8°, perspective 1200px; side angle beats top-down.
- Push: hold full page at zoom 0.78 for one beat, then 16f push to zoom 2.6.
- Action arc: rise 10f (cubic-bezier(0.2,1.25,0.3,1)) → hover 54f (sine bob 4px amplitude, 40f period, translateZ 110px) → reseat 18f landing with press scale 0.997; lock-to-land ≈3.3s (first drafts are almost always too fast).
- Contour beam: rounded-rect stroke runs two loops — 14f fast/bright, then 20f slow/weak (opacity 0.62); speed must differ; beam goes to the protagonist only once per film.
- Double shadow grows with lift: 0 8·lift px …, 0 46·lift px 90·lift px.
- Spotlight: wanders through 4 intermediate stations, then locks on card center; pool radius 620→420→360; +6% pulse at lock; outer vignette 0.16→0.42.
- Optional floating annotation: two serif lines in the same 3D space, translateZ 92px, bob period 44f (near but out of sync with 40f).
- Avoid tail drift (e.g. zoom 2.6→2.58); hold must be truly still; don't open with many dancing cards; no per-card glints.
- Pair with dolly-in + still hold after lock.

## 413. Form ② interface build-up
- Build order: chrome (window/title bar) → skeleton gray bars → content blocks stagger → data (numbers/charts) last.
- Three-stage reveal: sketch layer (re-seed every 5f to "boil") → decisive switch-to-real (8f accelerating shrink-back + spring skeleton pop) → skeleton rows stagger at 6f → revealed rows stagger at 13f, 12f within a row. Keep stages strictly isomorphic; don't soften the switch into a cross-fade.
- Word entrance: 2.5f/word rising 14px; last word of last row arrives +14f (half a beat late) as the "loading complete" full stop.
- Row embedding: row i cue = 12 + 9i frames, 12f flight, perspective 900px, translateY −120·air, rotateX 16°·air flattening to 0 (the rotateX flattening is what reads as "embedding"); 2px accent seam on bottom edge expands from center in 5f, fades in 8f.
- Document block-by-block: block g cue = 6 + 3.5g frames, each block wipes in 8f; a single accent caret follows the newest block only. Fit block count × beat to budget — cut blocks, don't speed up.
- Measure skeleton row heights against the real screenshot; keep sketch level detail-free; no real customer names in mock copy.
- Camera: gentle 1→1.34 push during reveal; no lateral moves while the interface changes.

## 414. Form ③ user typing simulation
- Speeds: body 3f/char, terminal 2f/char, decorative small text 0.7f/char.
- Cursor solid while typing, then 8f-period blink after finishing (blinking mid-type reads as lag).
- Occasional typo: over-type 1–2 chars, pause 4–6f, backspace, retype — scripted deterministically in advance.
- Leave 11f (~0.37s) between finishing typing and the UI responding.
- Code: color each token as it completes; never recolor the block afterward.
- On screenshots, patch out the baked placeholder (keep the icon) before typing over it.
- Never chunk user typing (reads as the field generating itself); chunks are for AI output only.
- Camera moves/pushes to the field first, then locks during typing.

## 415. Form ④ cursor operation narrative
- Double-ring click ripple: two concentric rings starting 3f apart, radius 14→54px and 14→78px; expand out-cubic 22f, fade linear 26f (compact: 10f each).
- Click anticipation: cursor scale 0.85 over ~3f (easeIn) → overshoot rebound.
- Hover linkage: target lights up the same frame the cursor enters (brightness +6% or hairline outline) and retracts on exit; declare windows by trajectory progress.
- Separate operation cursors (clicks with payloads) from performance cursors (named collaborators); don't mix in one shot.
- Duet: two named cursors approach, orbit with up/down arc split R≈270px, nameplates swap light/dark as a handoff; one cursor eases in enlarged as a transition wipe; all Bézier.
- Ensemble: 5 colored cursors fly in staggered at 0/5/9/13/17f with spring; resident dual-frequency sine drift 0.055/0.021 rad/f, amplitude ±46/30px; nameplates fade in 12f late; after converging decay drift to 25% (never fully still).
- Keep nameplate color constant per identity; drifting cursors never cover content being read.
- After a confirming click, push 16f to zoom ≈2.2 into the detail view.

## 416. Form ⑤ UI state transitions on a timeline
- Convert prototype mechanics to timeline equivalents: click listeners → timeline positions; class toggles + transitions → explicit tweens; display toggles → opacity/visibility tweens; :hover → declared linkage windows; random → seeded pre-generation.
- Modal/command palette: background dims over 10f to rgba(20,20,20,0.45) + 10px blur; panel −20px → overshoot +8px (9f) → settle (6f); rows stagger 4f each.
- Tab switch: indicator FLIP-glides first; old content fades 5f sinking 8px, new fades in 8f rising; content trails the bar by half a beat.
- Route push: new page enters full-width from the right in 12–16f; old page retreats 30% of the distance same direction and dims (parallax, not conveyor belt).
- One state change per shot; camera still at the moment of change, moving only after.

## 417. Form ⑥ 3D interface tour
- Steep-tilt glide (camera still, page moves): page at rotateY −60° (acceptable 55–65°; −45° too flat, beyond −70° unreadable), glides past at uniform speed — for volume/texture.
- Graze-face tour (camera moves, pages still): pages float 120–180px high; camera tours face-on — for readable content.
- Never move page and camera together (disorientation).
- Group stagger: staggered starts with overlapping descents ("a batch arriving").
- Cross-fade ≥8f between segments; no hard cuts.
- Waterfall wall variant: 3 columns, rotateX 20°, perspective 1000px, column loop periods differing ≥25% (e.g. 12/9/14s), middle column reversed.
- Textures ≥2x. Shots before and after must be still.

## 418. Form ⑦ long-page scroll narrative
- One exponential-out curve covering the full distance in 50f ("violent scroll, gradual stop"); no segmented deceleration.
- Motion blur from per-frame displacement only; still frames always sharp.
- At stop: target row scale 1.03, others dim to 0.38 (never 0).
- Budget: ≥2.6–3.0s between scroll-brakes; ≤4–5 per 15s; hold each stop ≥1.2s.
- No push-in during scroll; one light 1.3x push into the target row allowed after a full stop.

## 419. Form ⑧ feature callouts
- Style annotations one layer apart from the UI (serif / handwritten feel / accent color).
- Annotation line: stroke draw 12–18f out-cubic; text fades in 5f after the line arrives.
- Highlight frame: rounded outline expands in 8f + outer dim 0.3 (beyond 0.5 = interrogation lamp).
- Loupe: circular, 2–3x high-res slice (not magnified base), 2px outline + soft shadow, pops in 8f overshoot, follows with 10–14f easing; max one per shot.
- Explanation card: in 3D space at ~90px translateZ with bob near but out of sync with the subject.
- Before/after slider: fast flick 12f (out-cubic 8%→76%, rebound to 70%) → stop 18f → slow sweep 48f to freeze at 40%; speed ratio 5:1 (<3:1 is imperceptible); handle velocity-driven scaleX stretch peaking 1.18. Same layout and camera for both; "before" must be the real old state.
- Badges in content area, never covering avatars.
- Push camera to 1.3–1.45x so target fills ~80% of view; lock during annotation.

## 420. Energy skeleton for a product film
- Brand opening 8–12%: no UI; wordmark holds ≥1s.
- Single-protagonist legend 12–15%: form ① or ②; one slot per film.
- Feature ramp 55–65%: forms ③④⑤⑦⑧ alternating, one feature per shot; use callouts as low-energy breathers.
- Release finale 13–16%: 3D tour family-photo, then sign-off.
- Plan hold/rest frame budgets first, then place effects.

## 421. Sound hooks per form (after visuals lock)
- Hero: big whoosh on rise, sparkle on beam, single snap on reseat.
- Build-up: pop on switch-to-real, very light tick per row, soft chime on the late last word.
- Typing: key sounds exactly as long as the typing.
- Click: loudest sound in the film; ripples silent.
- State: soft pop for modal, fast whoosh for route push.
- Tour/scroll: silence or light hum; one muffled thud on hard brake.
- Callout: light draw friction; slider whoosh + rebound tick, slow sweep silent.

## 422. Pacing iron rules
- Run interactions at real human speed (3f/char, travel before clicks, breath before responses).
- Hold the whole board still 0.5s after mass motion settles.
- Stagger exits at ≥0.4f by reading order; simultaneous disappearance reads as a crash.
- One shot, one effect.
- True stillness at the end: no micro zoom/opacity drift in holds.

## 423. Three directions = three camera readings
- Offer three directions as three camera-narrative interpretations of the same UI assets (e.g. hero legend / build-up / tour + scroll), each with 2–3 keyframe thumbnails — not three skins.

---

# Part 36 — Animation Recipes

## 424. Timeline skeleton with labeled beats
- Build a paused, synchronously constructed timeline with default ease expoOut, 0.6s; place labels at 0 / 15% / 30% / 70% / 90% of total duration; leave the post-S5 tail empty for the hold. Transition scenes with opacity cross-fade + displacement, never display toggling.

## 425. Stage + sprite time windows
- Model the piece as a stage with total duration and sprites with [start, end] windows exposing local progress 0→1; interpolate properties within sub-ranges of that progress.

## 426. Seek-safe chunk reveal
- Split text at punctuation/whitespace, precompute cumulative times with seeded 40–120ms gaps, drive a linear proxy over the total, and each frame recompute visible text from t (correct when scrubbing back). Start ~0.3s into S2.

## 427. Seek-safe mouse path
- Proxy p 0→1 over ~1.1s easeInOut; per frame compute quadratic Bézier position plus sin-based tremor ±2px × (1−p); then click 0.85 scale (0.08s) → 1 (0.25s overshoot).

## 428. Blur via variables
- Animate blur through a custom property used inside filter; set will-change: filter only on elements whose blur actually animates.

## 429. Focus tween
- Single tween of non-focused tiles' focus variable to 1 and opacity 0.4 over 0.5s expoOut; flash 0.15s at +0.5s; release at +2.5s over 0.5s.

## 430. Proxy-driven legacy render
- Drive an existing pure render(t) with a linear proxy tween over the full duration (easing lives inside render); render(0) once after registration. Use only for migration; write new work as native labeled tweens for inspectability.

## 431. Camera proxy rig
- Camera state object {cx, cy, zoom, rotX, rotY, rotZ, perspective 1200}; planar mode: translate(960 − cx·zoom, 540 − cy·zoom) scale(zoom) on a 1920×1080 viewport; 3D mode: perspective × zoom, layout zoom on world, translate divided by zoom, then rotateY/X/Z.
- Shot syntax: establishing micro-push 1.06→1 over 3.0s power2.out (only if piece >14s and first shot >7s); push to target (e.g. 1→1.8x) with log duration, power3.inOut; hold ≥1.2s; mid-distance focus shift pans directly without returning to 1x, ~0.7s follow ease; closing pull-out 0.55s + ≥0.8s full-frame hold.

## 432. Counter-scaled annotations
- Prefer captions in a static HUD; for annotations that must follow world elements at constant size, apply scale(1/zoom), and animate their entrance on child elements.

## 433. Multi-layer parallax
- Derive every layer from the same camera displacement × factor (e.g. 0.35 / 0.7 / 1.4); factor ratio between layers ≥2x; ≤4 layers.

## 434. Gallery ripple entrance
- Each card's delay = (distance from grid center / max distance) × 0.8s; each card enters over 0.7s expoOut; total ripple ~1.7s; simultaneously scale the canvas 1.25→0.94 (pull-back reveal).

## 435. Variable-weight morph
- Animate font weight instead of size: wordmark 100→700 over ~0.7–0.9s expoOut with tracking −0.045→−0.048em; headline lines 100/120→300/400 over the entrance + 0.3–0.6s, combined with a 16–24px rise. Requires a variable font; static fonts jump.

## 436. Two-tier fake depth shadows
- Assign each card near/mid/far shadow tiers deterministically (e.g. sin(i·1.7)+cos(i·0.73)); near: 0 32px 80px −22px at ~0.22 alpha (warm brown) / far: 0 14px 40px −16px at ~0.10; transforms never change per frame.

## 437. Sine + drift pan
- Pan = sin(t·0.12)·220 − 8t (X), cos(t·0.09)·120 − 5t (Y) (lighter variant: 180/6 and 100/4); clamp to ±900/500px (or ±600/400). Different X/Y frequencies plus linear drift → never predictable, gentle "boat sway" under tilt.

## 438. Typed terminal command with blinking cursor
- Reveal a command linearly over ~2.2s; cursor alternates full / 0.25 opacity at 2.5Hz-derived steps; terminal rises 28px→0 on a 0.6s expoOut entrance.

## 439. Click ring glyph
- Ring scales 0.5→2.2 while opacity 0.8→0 over 0.8s ease-out; accompany with a 0.4s horizontal shake ±3px.

## 440. Simulated slider drag
- Thumb travels 58%→72%→62% (overshoot and correct) with easeInOut halves over ~1.9s; a second slider 40%→55%; or 30%→70% during a hold; fill follows the thumb.

## 441. Scene exit with shrink + blur
- Exit a framed UI by scaling 1→0.92 and blurring 0→6px over ~0.6s while fading with easeOut; enter at scale 0.94→1 with expoOut.

## 442. Card styling for gallery
- 8×6 grid, gap 40px, padding 60px, 16:9 cards with 14px radius, 6px inner padding, image radius 9px, hairline border.

---

# Part 37 — Cinematic Patterns

## 443. Pattern A · Dashboard + cinematic overlay
- Default state shows a complete static dashboard explaining the workflow at a glance; a small accent play button sits bottom-right (not a big central overlay).
- Play floats a ~22s cinematic over it, runs once (not looped), then fades back to the dashboard.
- Never default to a black screen with a central play icon.

## 444. Pattern B · Scenes, not steps
- Split into 5 full-screen scenes, one focal thing each: Invoke (user input trigger, terminal typing) 3–4s → Process (core workflow visual) 5–6s → Result/Insight (distilled artifacts) 4–5s → Output (files/diff/numbers) 3–4s → Hero reveal (big type + value proposition) 4–5s.
- Total ≈22s: <18s ends before viewers engage; >25s loses patience.
- Drive all scenes from one global timeline and per-frame render; no linear easing.

## 445. Pattern C · Independent visual language per demo
- Derive each demo's visuals from its own core metaphor (e.g. collect→distill→write = floating/radiating orbit, pentagon, typed document, serif-italic big number; loop→evaluate→ratchet = spinning ring, side-by-side diff, hill-climb curve, gear + gain tag).
- Test: cover the copy — if you can't tell demos apart, it's laziness.

## 446. Pattern D · Real generated assets
- Use a consistent set of generated object images (e.g. one 4×2 grid, white background, 60px breathing room, unified style, cut into transparent PNGs) instead of emoji or hand-drawn SVG; 4×2 avoids last-row compression; white background eases cutouts.

## 447. Pattern E · Music + SFX dual track
- Music drone bed + ~11 SFX cues: whoosh at 0.10s (terminal rises), enter at 3.0s, slide-in at 4.0s, 5 sparkles across 5–9s on key process nodes, click at 14s (switch to output), logo reveal at 17.8s, type sound every 2 characters.
- Levels: music 0.32, SFX 0.55, sparkle 0.7, logo reveal 0.85.
- Require a play action for audio; small mute top-right.

## 448. Static dashboard layer
- 3-column grid (or 1 large + 2 small); each panel answers one question: pipeline/flow, snapshot/state, trajectory/evolution, examples/gallery, example input→output strip.
- Dense but no data slop (every number means something); same color family as the cinematic.

## 449. Dev affordances for long animations
- Provide seek-to-second, autoplay-skip and a small replay button (top-right, mono 10px, 0.28em tracking, uppercase, faint accent border, 6px backdrop blur) — kept out of recordings.

## 450. Gallery Ripple + Multi-Focus orchestration
- Use when you have 20+ (ideally 30+) visually consistent assets and need to express scale × depth; narrative = Scale (ripple ~1.5–1.7s) → Gaze (focus ×4, ~8s) → calm exit.
- Prerequisites: ≥20 assets (e.g. 48 slots looping 32 images), consistent aspect/tone, each readable when enlarged to ~960px wide, landscape or square frame.
- Fallbacks: <20 assets → 3–5 cards in a static row + focus one at a time; inconsistent style → cover + 3 chapter heroes; information-poor → data dashboard or quote + big type; portrait → vertical scroll + sticky cards.
- Quick check: <15 assets stop, 15–25 make do, 25+ use; 4 random assets must look like one set; narrative must be breadth × depth.
- Don't use for feature demos, data-reading content, cause-and-effect stories, 3–5 assets, or 9:16.

## 451. Gallery structure
- Viewport 1920×1080 with perspective 2400px; oversized canvas 4320×2520 (2.25x viewport) for a "peeking at a bigger world" pan; tilt rotateX 14°, rotateY −10° (plus rotateZ −2° variant), base scale 0.94; focus overlay centered above (z 40).

## 452. Multi-focus rhythm
- 4 focuses of 1.7s each with 0.6s breathers (e.g. 11.0–12.7, 13.3–15.0, 15.6–17.3, 17.9–19.6s).
- Inside each: 0.4s in (expoOut), ~0.9s hold at full intensity, 0.4s out (easeOut).
- Background: opacity to 40%, brightness 68%, saturate 65% (lighter variant: dim 0.55 with brightness −0.3·d, saturate −0.4·d) — darken and desaturate together so the foreground pops.
- Focus overlay grows 400×225 → 960×540, with 3-layer shadow + 3px accent ring.
- Overlay statements on the gallery: 0.4s expoOut in, 0.4s easeOut out, ~1.7s each, 0.3s apart.

## 453. Corner brand signature
- During busy middle sections show a small corner mark at ~16% opacity (≈0.22 white on dark), 10–12px, wide tracking (~0.24em), uppercase mono; off at the opening and off for the brand reveal.

---

# Part 38 — Hero Animation Case-Study Lessons

## 454. Thirty-second act structure (beats)
- Act 0 homage/setup 0–4s: framed UI in 0.3–1.2s (opacity expoOut, scale 0.94→1), live tweaks 1.4–3.3s, accent swap 2.1–2.5s, caption in 1.6–2.2s / hold to 3.3 / out 3.3–3.8 (rise 14px), exit 3.4–4.0s with shrink 8% + blur 6px.
- Pivot line 3.9–4.6 in / hold to 4.9 / out 4.9–5.3, rise 16px, weight 120→300.
- Four statement cards (~2.5s, ~2.6s, ~2.3s, ~2.8s): each in ~0.6–1.0s, hold 1.2–1.7s, out 0.5s, next starting 0.1s before previous ends (cross-overlap); glyph enters 0.15s after card; strike-through the key word 0.5s into hold; shake/drag action ~0.3s into hold.
- Terminal 15.6–16.2 in, type 16.4–18.6, out 18.9–19.4.
- Gallery in 19.1–19.9 (overlapping terminal exit), ripple 19.9–21.6, pan from 20.2, two overlay statements 21.7–23.4 and 23.7–25.4, out 25.5–26.2.
- Thesis line 26.1–27.0 in / hold to 28.0 / out 28.0–28.4 (rise 24px, weight 100→300).
- Brand 28.3–29.0 in, weight morph 28.7–29.4 (100→700), farewell line 29.0–29.6 (rise 12px), secondary-language line 29.3–29.8, URL 29.5–30.0; then hold on final frame (no loop when finished).
- Scene in = expoOut; scene out = easeOut; elements rise 12–28px.

## 455. Lessons distilled
- expoOut as primary easing beat cubic out for weight, shockwave, settling.
- Warm paper background with a single terracotta-style accent compresses well and "breathes"; noise grain ruined compression.
- Two-tier shadows replace real 3D at ~10x lower cost.
- Weight variation reads more cinematic and "modern" than scaling (inner fullness, like inflating, not pushing closer).
- A faint corner brand anchors attention after the ripple burst and survives screenshots.
- Pure linear pan is predictable; sine + drift keeps every second new.

# Part 39 — Camera Language

## 456. Camera thesis: budget-driven, not effects-driven
- Treat every camera change as an attention expense managed like a budget; once the budget is spent, drop even good shots.
- Visibility invariant: whatever the audience should look at must be inside the visible area at every moment, including an 8% safety margin; if a shot violates this, reduce zoom, merge shots, or don't shoot it.
- Cinematic feel = camera moves × light/shadow × rhythm × sound; a passing grade on all four beats maxing one.
- Prefer slow over fast: when unsure of a duration, pick the longer one; when unsure whether to move the camera, don't.
- Ask of every move: "which question does this answer for the audience?" If no answer, don't move.
- Speed is felt through acceleration, not uniform speed: use a short accelerating segment + long ease-out instead of halving the duration; uniform motion reads as cheap slideware.
- Camera position serves readability: face information-dense shots head-on; text close-ups use a lateral camera (rotY dominant, very small rotX); no global one-size tilt; no handheld shake in product promos by default.

## 457. Camera budget numbers
- Interval between adjacent camera changes: ≥2.6–3.0s (restrained tier 5.0s); below 2.6s viewers get dizzy.
- Camera changes per any 15s window: ≤4–5 (restrained tier ≤3); if exceeded, cut the weakest-motivated shot — never compress intervals.
- Shots per minute: restrained ≤4/min, normal ≤6/min ("room to breathe, not MTV").
- Push-in floor: 1.25x (below is imperceptible shaking); sole exception: 1.06x establishing micro-push.
- Push-in ceiling: 2.3x (restrained tier 1.8x); beyond that, swap to a higher-resolution source asset rather than pushing further.
- Enter the shot 0.15s before the action (camera arrives first); linger 1.2s after the action finishes before moving on.
- Don't give isolated actions shorter than 1.2s their own shot ("no pump for every click").

## 458. Push in
- Use for "look here next": focusing on one specific UI element / number / keyword; rising tension.
- Zoom tiers 1.3 / 1.45 / 1.8 / 2.3; duration from the logarithmic formula; enter 0.15s early.
- Never push below 1.25x; never push during full-screen changes (scrolling, page switching, video playback) — causes dizziness; never move mid-narration (move on pause).
- The endpoint must be a nameable concrete anchor (logo, key number, that button, that line of code, a facial expression); never push into background texture, atmosphere, or decoration. If you can't name the anchor with a noun, delete the move.

## 459. Pull out
- Use to reveal the full picture/context ("it belongs to a larger system") and for finales.
- Duration from the same logarithmic formula; finale pull-out 0.55s + ≥0.8s full-frame pause.
- No "out-in-out" pumping: if the gap between shots is smaller than the transition duration, go straight to the next shot without returning to 1x.

## 460. Pan
- Use to transfer between two mid-distance focal points (normalized distance 0.22–0.45) or sweep across side-by-side elements.
- Pan only at combined zoom ≥1.25.
- Prefer diagonal pans via dual-frequency sine: X/Y frequency ratio 0.22:0.35, amplitude 30–40px; pure single-axis pans feel mechanical.
- Don't pan between focal points farther than 0.45 — drop the shot instead.
- World/canvas must bleed beyond the viewport by ≥ max pan amplitude + 8% on all sides, or panning exposes blank edges.

## 461. Orbit
- Use for single-protagonist texture close-ups / building the hero's legend (strongest physicality).
- rotY dominant, perspective 1100–1200px; measured positions rotX 46 / rotY −30 / rotZ 9 → rotX 42 / rotY 26 / rotZ −7.
- Any single showcase technique gets to be the protagonist only once per film.
- Forbidden on information-dense frames — face text head-on.

## 462. Dolly zoom (and the fake recipe)
- Use only for a "worldview inversion" reveal: subject unchanged, context drastically changes; at most once per film; without a narrative drop it is showing off.
- Fake version: subject pinned (or ≤1.02x breath); background scales 1 → 2.0–2.5 while opacity drops to ≤0.6; duration ≥1.2s.

## 463. Static
- Default for text reading, real-human-speed interaction demos, information-dense shots, and whenever budget runs low; always legitimate.
- Brand wordmark settles and holds ≥1s; 0.5s stillness after mass motion finishes; opening subject action arc ≥3s.
- Write why a static shot is static.

## 464. Zoom vs dolly selection
- Zoom (pure scale): no parallax, reads as "one image enlarged"; clean and informational; use for flat content (interfaces, documents, charts).
- Dolly (perspective + forward Z): parallax, reads as "camera advancing through space"; use when content has a foreground/subject/background hierarchy worth seeing.
- Real-3D verdict: ≤8 elements → real Z layering; ≥20 elements → fake depth with shadow/blur/brightness; 8–20 → real 3D only if the shot needs parallax.

## 465. Camera rig structure
- Use a fixed viewport (overflow hidden, holds perspective) → camera layer (camera transforms only) → world layer (all content; element animations only here); captions/chrome live in a HUD layer that is a sibling of the camera and doesn't follow it.
- Camera motion and element animation must never fight over the same transform.
- For annotations that must follow a world element at constant size, apply a counter-transform scale(1/zoom) updated each frame.
- Transform-origin = push-in target point (set origin to target center, then scale).
- Camera keyframe model: {frame, cx, cy, zoom, rotX, rotY, rotZ, persp}; cx/cy = world point aimed at. Flat mode on 1920×1080: translate(960 − cx·zoom, 540 − cy·zoom) scale(zoom), origin 0 0 (use W/2, H/2 at other sizes).
- 3D mode: outer perspective = persp·zoom, perspective-origin 960/540; inner uses layout-level zoom with Tx = 960/zoom − cx, Ty = 540/zoom − cy, then rotateY/X/Z, origin cx cy, preserve-3d.
- Typical measured camera: full-page zoom 0.78 → close-up 2.6; side shot rotY 34 / rotX 8 / persp 1200 (side beats top-down).
- Any intermediate layer with overflow hidden, filter, or opacity <1 flattens 3D; apply filters only on the innermost layer.
- When following a moving point, check each frame that the target stays visible; if it exits, hold zoom and pull back only along the offending axis — the camera gives way rather than losing the target.

## 466. Sharp text when zooming in 3D
- Scaling via transform rasterizes at layout size then enlarges the bitmap — text blurs, undeliverable above 2x. Use layout-level zoom on the world layer so text re-rasterizes sharp; divide translations by zoom.
- Bitmap assets: capture full-page screenshots at 2x; prepare separate 4x single-element captures for close-ups, crossfaded over the low-zoom texture for 6 frames during the push.
- Depth of field is atmosphere only: a top gradient band with blur + mask, never true per-layer DoF.

## 467. Camera easing
- Active push/pull: cubic-bezier(0.65,0,0.35,1) (power3 in-out); never linear, never spring overshoot.
- Follow move (camera chasing an action already started): cubic-bezier(0.33,0,0.15,1) — light departure, long brake.
- Sustained idle drift: sine in-out yoyo or linear — the only case uniform camera speed is allowed; banned for moves with start/end points.
- Cursor/focus follow smoothing: ~0.15s smoothing; Catmull-Rom path interpolation; zero-phase (forward+backward) smoothing.
- Conflict rule: single push/pull → power3 in-out; compound/multi-segment continuous moves → (0.33,0,0.15,1).

## 468. Logarithmic zoom duration
- duration = 0.55 × |ln(zoom₂/zoom₁)| / ln 2, clamped to [0.30, 0.94]s.
- 1→2x = 0.55s; 1→1.3x ≈ 0.30s (floor); 0.78→2.6x = 0.94s (ceiling). Never use fixed durations for zooms.

## 469. Zoom tiers and framing
- 1.06x establishing micro-push (only below-1.25 tier; felt as "alive", not as zoom).
- 1.3x light push: suggestive focus, doesn't interrupt global reading.
- 1.45x medium push: one panel / one code block.
- 1.8x heavy push: one button / one number (restrained ceiling).
- 2.3x ceiling: extreme close-up; source must hold (2x/4x captures).
- Framing: scale = 0.8 / max(target normalized width, height), then clamp into tier; content fills 80% of view, 20% breathing room — never fill the frame.

## 470. Inter-shot grammar (anti-dizziness)
- Dizziness comes from how shots connect; "out-in-out" pumping and far diagonal jumps cause most of it.
- For adjacent shots with gap <1.5s, by normalized focal distance: <0.22 → merge into one shot framed on the combined bounding box; 0.22–0.45 → change to a pan at a wider zoom (≥1.25); >0.45 → drop the weaker shot. Never film two far focal points back to back.
- Tight gaps (gap < transition duration): transition directly from current zoom to the next shot's zoom/focus; don't return to 1.0x.
- Pull-out-then-push-in is allowed only when the gap is ≥1.5s.

## 471. Establishing shot, finale, move on pause
- Establishing: if the film is >14s and the first formal shot comes after 7s, start at a 1.06x center micro-push and ease back to full frame over 0–3.0s.
- Finale: pull the final framing in early — 0.55s pull-out + ≥0.8s full-frame pause; always end on a still full frame, never mid-push. A "hard stop + hold" ending must hold on the full frame.
- Move on pause: cut on action, move on pause; in narrated films snap camera moves to the nearest speech silence, at most 0.8s earlier, only earlier, never later; use sentence-break gaps as snap points.

## 472. Transitions — six visible styles (for large energy drops)
- Pick by energy drop; exactly one style per seam; transition frames come out of adjacent shots' budgets. Acclaimed release films have no bare cuts.
- Flash-wash (high→high, strong section shift): white peak 2–4 frames with 5 frames ramp each side; only at the cut point, not decoration.
- Dip-to-dark (high→low, emotional downturn): dim to ~rgba(20,20,20,0.9), total ≤0.6s; don't linger or viewers think it ended.
- Defocus-handoff (mid→mid, same-level topic switch): outgoing blur 0→8px overlapping incoming 8→0px for ≥8 frames; keep large blur areas ≤24px.
- Title card (chapter separation): hold ≥1s, 0.3s transition each side; ≤2 per film.
- Whip-pan (low→high spike): hold ≥20 frames at both ends, whip 1.5 screens in 8 frames, peak ≥300px/frame so it blurs convincingly; too slow = just a pan.
- Mask-wipe (spatial transfer through one interface into another): mask-edge easing (0.4,0,0.6,1); mask shape must come from an element already on screen (window/card corners).

## 473. Transitions — hidden cuts and travel
- Flash-cut: a white flash straddling a hard cut, 5 frames each side.
- Foreground-occlusion cut: switch scene at the instant a foreground element (card, panel, hand) sweeps full screen.
- Motion-blur cut: hard cut on the peak frame of high-speed motion, matched direction both sides.
- Shared-element settle: an element from shot A moves continuously into its new position in shot B; must be the same identity; avoid large shape change.
- Letterform-counter traversal: push through a large letter's counter (O, 0) into the next scene; counter ≥1/3 screen height; traversal at the 0.94s ceiling duration.
- Selection: big energy drop → one of the six; want it unnoticed → hidden cut; spatially continuous → travel. Hard cuts must always be wrapped by one of these.

## 474. Multi-layer parallax
- Layer speed coefficients: far 0.35 / mid 0.7 / near 1.4 × camera displacement.
- Adjacent layer speed ratio ≥2× (1.2× is unreadable); ≤4 layers.
- Derive every layer from one camera state (multiply x/y by coefficient); no per-layer independent tweens.

## 475. Motion-derived signals
- Velocity blur: velocity by central difference; trigger only when zoom speed >0.6/s; intensity min(10, v×5)px; blur only during motion, still frames always sharp.
- Lagged follow layers: shadow lags 2 frames, afterimage 4 frames; afterimage as motion-blur substitute = 5% path lag + 6px blur + opacity 0.25·(1−t).
- Residual settle after a hard stop: e^(−d·t)·sin(2π·f·t), f≈0.1, damping≈0.15, 1–2 sways, amplitude ≤3px; only for whip-pan/hard-brake moves, never active in-out moves.
- All signals must be pure functions of time (seek-safe).

## 476. Camera self-check (after writing the timeline)
- Every move answers a question; no zoom <1.25x except 1.06x establishing; intervals ≥2.6s and ≤4–5 per 15s; log-formula durations; power3 in-out for push/pull; merge/pan/drop verdict applied, no consecutive far jumps; tight gaps cut across; establishing push if >14s and first shot >7s; ends on still full frame ≥0.8s; narrated moves snapped ≤0.8s earlier to gaps; camera isolated in its own layer; sharp 3D text; one style per seam, no bare cuts; parallax ≥2× ratio, ≤4 layers; blur only in motion.
- Order: set budget/vocabulary at script/storyboard stage; set implementation and seams before writing the timeline; run the checklist before delivery.

---

# Part 40 — Storyboarding

## 477. When to storyboard and how heavy
- Never skip storyboarding, even for 5s pieces; skipping produces timeline thinking ("what appears at which second") instead of visual thinking ("what this frame looks like"). A storyboard card costs minutes; skipping costs reworking the film (case: motion passed, visuals vetoed in one vote).
- <20s animation/motion graphic/demo: lightweight storyboard card (one line per shot).
- ≥20s: written director's document whose minimum is the full eight-field storyboard card.
- Launch film / brand promo / "Apple-level" expectation: full 10,000-word director's notes.
- For "quick animation" requests, don't impose the heavy process — but still draw storyboard cards.

## 478. Every shot is first a moving cover image
- A good cover = 1 concrete protagonist + ≤3 active elements + 1 clear gaze guide.
- Cover test: pause any random frame; it must work directly as a cover.
- Lay out the frozen frame first, then choreograph motion.

## 479. Law 1 · Cover test
- Each frozen frame: 1 protagonist + ≤3 active elements + 1 focal point; "≤3" is a per-frame invariant, not a per-scene total.
- When new elements enter, old ones exit (fade, retreat to background, blur+dim); count on-screen elements at each time; if over budget, cut an entrance or exit earlier.
- Self-check: pause at three random times; no frame exceeds 3 active elements.

## 480. Law 2 · Zoom endpoint = concrete anchor
- Zoom/push endpoints only: brand logo, key number, a specific button, a line of code, a facial expression. Never textures/atmosphere/decoration.
- Write the anchor for every camera push; no anchor → delete the move. Zoom <1.25x isn't worth doing (except 1.06x establishing).

## 481. Law 3 · Gaze/arrow = motion script
- The guide line in the frozen frame is the camera instruction: camera follows gaze, pushes along the arrow, pans along reading direction.
- One guide line per scene; if none is findable, fix the composition rather than inventing a move.
- Self-check: show the frame for 3s; viewer's gaze path matches the planned camera motion.

## 482. Law 4 · Text and image on two tracks
- Big text per shot: hard cap 2–6 characters/words; main copy best at 2–4. Text carries the hook, image carries atmosphere; don't make the image act out the text.
- Two-beat entrance: action word slams in first, the attributive color block fills in after (e.g., "Tested" full-screen, then the model-name color block).
- Text lands in reserved negative space; never covers the protagonist or focal point.
- Decorative text is solid strong color; hollow white text with colored outline is forbidden.
- Self-check: cover the image — hook remains; cover the text — composition holds.

## 483. Law 5 · Percentage spatial language
- Write composition at percentage granularity (e.g., "screenshot top-right 60% with perspective, character bottom-left 25%, big text against screenshot's top edge, 10% safe margin all edges"); it maps directly to layout values.
- Each shot's composition must contain ≥3 percentage numbers.

## 484. Law 6 · Foreground / midground / background
- State all three layers and who occludes whom; it is parallax material (0.35/0.7/1.4 coefficients, ≥2× ratio, ≤4 layers).

## 485. Law 7 · Setup → payoff
- Each scene's opening frame leaves a gap (unfinished bridge, unrevealed number, half-blank screen); the shot's motion closes it. The previous shot's payoff can be the next shot's setup.
- Anti-pattern: opening frame shows everything, then elements merely animate in place ("moving poster").
- Self-check: put opening and ending frames side by side — viewer can say what got fulfilled.

## 486. Law 8 · Objectify with process
- Turn abstract concepts into visible physical actions with process: "connect" = bridge assembling segment by segment; "price cut" = $89 crossed out digit by digit into $29; "AI-heavy" = manuscript filling with tidy gray blocks.
- Translate how the concept "happens" first, then pick art style. Imagery must be summarizable by one verb (assemble, cross out, grow, land).

## 487. Law 9 · Style × composition are orthogonal
- Fix the style skin once for the whole film (palette, fonts, materials, background logic); change the composition template scene by scene (centered close-up → three-column grid → diagonal split).
- Scene change = composition change, never style change.
- Self-check: any two shots show no style difference but clearly different composition.

## 488. Law 10 · Forbidden aesthetics carry over
- Avoid glowing particles, data streams, holographic HUDs, cyber-neon, deep-navy #0D1117 + neon glow. Tech feel = real UI screenshots as floating 3D cards + clean big text + light background.
- If anything "glows", justify it one by one or remove it.

## 489. Law 11 · 3-meter test
- The largest word in any paused frame must be readable from 3m; never shrink type because "it moves anyway" — animation sizes go bigger, not smaller.
- Self-check: shrink a keyframe to phone size; the largest word stays readable.

## 490. Shot-size system
- Extreme long 0.78x (whole scene + negative space; opening establishing, closing group shot).
- Long 1x (1.06x establishing) — narrative baseline, home of most shots.
- Medium 1.3–1.45x — one functional block; feature-demo workhorse.
- Close-up 1.8x — single component / data point.
- Extreme close-up 2.3x max — concrete anchors.
- Intermediate values (1.5x, 2.0x) are legal; tiers just give names numeric meaning.

## 491. Shot-size rhythm between shots
- Adjacent shots differ by ≥1 tier (same-tier cuts read as a glitch).
- Avoid two-tier jumps (e.g., 0.78x → 2.3x); if deliberate, cushion with a transition (white flash / whip-pan).
- Close focus → merge; mid distance → pan one tier wider; far → drop a shot or insert a long-shot bridge.
- Size-change duration uses the log formula [0.30, 0.94]s.
- Shot-size changes ≥2.6s apart, ≤4–5 per 15s.
- Always end on a long/extreme long shot with ≥0.8s full-frame pause.

## 492. Energy skeleton for multi-shot films (≥10s)
- Opening 8–12% of runtime, low energy, brand/theme reveal; wordmark hold ≥1s.
- Single-protagonist portrait 12–15%, low-medium, slowest segment; one complete action arc (enter → hover → settle) ≥3s; highest production quality.
- Feature ramp 55–65%, medium-high alternating with low; one unique feature per shot; after every 1–2 feature shots insert a breathing text card.
- Closing 13–16%, film peak; group shot + sign-off; return to long shot.
- Breathing text card: 2–6 characters of big text + full-screen negative space + zero decoration (1 active element); never make it another information shot.
- ≤15s pieces: use either the slow-fast-boom-stop curve or the skeleton; >20s: skeleton for shot order, slow-fast-boom-stop feel inside each shot.

## 493. Scheduling discipline
- 1) List features, count shots N. 2) Carve out inviolable static time first: wordmark hold ≥1s, 0.5s still after batch motion, opening action arc ≥3s, ending ≥0.8s long-shot pause, 0.5s hover before a key result. 3) Remaining time to motion, alternating high/low — never two high-energy shots in a row. 4) Pick a transition per seam; transition frames come out of adjacent shots, not added.

## 494. Lightweight storyboard card (eight fields)
- Columns: # | time | shot size | camera move + motivation | composition (percentages) | key motion | transition to next | acceptance frame numbers. All eight required.
- Time: start–end seconds; transitions included in the shot.
- Shot size: tier + zoom value.
- Camera: move + one-sentence motivation; static needs a reason; every push names its anchor.
- Composition: percentages + fore/mid/background.
- Key motion: one motion effect per shot.
- Transition: never blank, never "direct cut" (bare cut only as a deliberate hidden cut).
- Acceptance frames: pre-write 1–2 frame numbers per shot; capture exactly these after implementation.

## 495. Worked example: 12s product storyboard (1920×1080, 30fps, 360 frames; screenshot-organizer product)
- Shot 1, 0–2.0s, long 1x: static, last 0.3s light push to 1.06x (establishing + suspense). Messy screenshot pile center 70%; big text "3000 screenshots" in top 20% negative space; 10% margin; two foreground screenshots overlap the pile. Screenshots land with 30ms stagger; two-beat text ("3000" slams, "screenshots" block follows). → defocus-handoff. Frames f30/f55.
- Shot 2, 2.0–3.5s, extreme close-up 2.3x: push 1x→2.3x, anchor = date tag bottom-right of one screenshot. Single screenshot 80% centered, 2° perspective, tag at bottom-right 15%; others blur back. Push with synced background blur+dim. → shared-element settle (screenshot shrinks into next shot beside input). f85.
- Shot 3, 3.5–6.0s, medium 1.4x: horizontal pan following cursor; guide = cursor arc. UI 85% with perspective, logo top-left 10%, search box centered 55% width, cursor arcs in from bottom-left 25%. Typing 3 frames/character + chunked result reveal; 0.4s breath after typing. → mask-wipe (result panel edge unfolds into grid). f130/f165.
- Shot 4, 6.0–8.5s, long 1x: pull 1.4x→1x to show scale. 3-column category grid 85%, color-tag headers, top 15% reserved for next numbers. Cards stagger into columns, 30ms between columns; 0.5s still after full board. → flash-wash. f210/f250.
- Shot 5, 8.5–10.5s, close-up 1.8x: static — key result hold. "3000 → 12 categories" center 60%, action word largest; large negative space. Digit roll with tabular numerals; 0.6s hold after settling. → shared-element settle (numbers shrink/rise for logo). f290.
- Shot 6, 10.5–12s, long 1x: static finale. Logo centered 12%, one-line slogan below at 8%, rest blank. Logo morph-closure; final frame hold ≥1s. End. f330/f359.
- Pattern: setup shot → ramp alternating sizes (2.3x → 1.4x → 1x, no same-tier cuts, no two-tier jumps) → peak hold → long-shot finale; ≤3 active elements per frame.

## 496. Thumbnail (gray-box) pass
- Build a temporary page with one 1920×1080 section per keyframe using only solid blocks + text labels (dark gray for protagonist "product UI 85%", color block for text area, light gray for foreground). No motion, fonts, color, or shadows — beautifying now is avoiding composition problems.
- Do only 3–5 keyframes: opening setup, portrait hero, one ramp frame, peak, finale.
- Capture them at 1920×1080 and compare side by side.
- Three acceptance questions: with labels hidden, do the 5 compositions differ? Does each pass the cover test? Can you point to each guide line? Any "no" → fix before coding.
- Keep the gray-box as the composition baseline to compare against when implementation drifts.
- The chosen direction board (hero still + palette + character sentence) is effectively thumbnail #1; the pass expands it into the keyframe sequence.

## 497. Transition choice by narrative relationship
- Time jump ("three days later") → title card / flash-wash; alt whip-pan.
- Spatial move within one interface → one continuous pan, no cut; alt hidden cut.
- Comparison (before/after, A vs B) → mask-wipe; alt split-screen hard cut + white flash.
- Progression/causality → shared-element settle (previous element becomes next protagonist); alt morph.
- Large energy gap (breathing card → high-energy shot) → flash-wash / white flash-cut; alt whip-pan.
- Small energy gap (adjacent feature shots) → defocus-handoff / cross-fade ≥8 frames; alt hidden cut.
- One seam, one form (white flash + whip-pan together is slop); transitions carved from shot budgets; zero bare cuts.
- Narrated films: cuts and transitions snap to speech gaps, only earlier, ≤0.8s.

## 498. Storyboard done definition
- Table complete (8 fields per shot); every frame checked at least against cover test, guide line, percentage composition; no same-tier consecutive cuts or two-tier jumps; hold budget carved first and breathing cards inserted; a transition written at every seam; 3–5 gray-box frames passed; acceptance frames pre-written.
- When an implementation is vetoed, first diagnose: motion-skeleton problem or visual-craft problem; the storyboard usually doesn't need rewriting.

---

# Part 41 — Launch-Film Direction

## 499. When to use the full director's-notes workflow
- Trigger for ≥20s work with brand narrative, slogan reveal, or wide promotion, especially with explicit quality expectations ("Super Bowl", "Apple-level", "10x detail").
- Ask three questions; any "yes" triggers: Does it carry brand narrative (thesis/slogan/upgrade ritual)? Will viewers pause, screenshot, make posters/covers? Is there an "I want it like X" reference?
- Triggers: SaaS upgrade promo; Apple/Super Bowl-tier (add multi-perspective parallel); 30s brand launch film; explicit "write a 10,000-word script first". Don't trigger: simple logo motion graphic, onboarding demo, narrated tutorial (use the narration workflow); single hero animation depends on spec level.
- Before writing notes, pass a three-direction gate: present one direction board per direction (real hero keyframe still + palette + character sentence + references); expand notes only around the chosen direction. Style keywords don't exempt this.

## 500. Why write first
- Writing the script is thinking; writing code is executing. Executing first makes every shot an on-the-spot decision → uniform rhythm, colliding slogans, no arc. Script-first implementation passed in one go with every paused frame holding up.
- All creative decisions get fixed before code; implementation is faithful translation.

## 501. Five-part structure (10,000–12,000 words; missing any part = incomplete)
- Part I Director's Statement (~1,500–2,000 words): what the film is NOT; one-line thesis viewers remember; 5–8 specific visual references (work + year) and what's borrowed from each; three audience profiles (primary/secondary/outer) with a commitment to each; rhythm philosophy (slow beat / acceleration / peak / gentle close) and which second the climax lands (not necessarily last). End with a concrete "will not do" list.
- Part II Visual System (~1,500–2,500 words): palette ≥8–10 colors each with HEX + function + max frame share; typography ≥6 size levels each with font + weight + size + tracking + usage; grid (canvas, margins, columns, baseline, safe zones, golden-ratio anchors); animation system (≤4 easings, duration dictionary, stagger rules, scene-transition rules); chrome elements with position + entry/exit timing; audio system (30s layered BGM curve + SFX dictionary of 10+ cues with timecode, volume, frequency band); per-shot anti-slop checklist of 10–15 items. Derive every value from this system; never invent values in the shot list.
- Part III Story Arc (~500–800 words): Act I Setup = first 1/5 (0–6s of 30s); Act II Escalation = middle 2/3; Act III Payoff = final 1/4 (transcendence, slogan, brand stamp). Include an emotion curve and climax marker.
- Climax placement: for 30s, climax at ~22–25s, not 29s; final seconds are resolution/decay. Climax at the end → "strong start, weak finish".
- Part IV Shot-by-shot (~5,000–7,000 words, ~60% of length): 12–15 shots, 400–700 words each, fields 30–80 words each.
- Part V Production Manifest (~800–1,200 words): font loading with preconnect; pasteable color variables; BGM sourcing criteria + generation prompt keywords + backup libraries; SFX dictionary per cue (file + volume by timecode); keyframe verification plan of 12–15 timecodes with items per frame; recording parameters (fps/codec/bitrate/preset); audio mix command with audio-stream verification; deliverables (mp4, 60fps mp4, gif, poster png, silent mp4, shot list csv); hour-level time estimate.

## 502. Shot fields (11 per shot, all required)
- SHOT NN · NAME; TIMECODE (start/end + duration); FUNCTION (one sentence in the arc); VISUAL (composition, positions, motion direction); CAMERA (shot size mapped to zoom tier + move + motivation; static justified; push anchor); TYPE (font/size/tracking/leading/color/alignment); ANIM (per-element in/out timing, easing, duration, stagger, delay); AUDIO (music beat + SFX cues); CHROME (which corner elements are on/fading/pulsing); ANTI-SLOP (checks passed + its "120% detail signature"); WHY (carry-over from previous shot + hook into next).
- After writing, test deletion: if any single shot can be removed and the film still holds, delete it.

## 503. Writing tips
- Speak as a director, not a PM: "This is the hero shot — if the audience pauses anywhere, I want it here," not "This shot displays features." First person + judgment preserves decision traces.
- Cite specific works with year and director and the exact technique borrowed (e.g., "Designed by Apple in California", 2013, Mark Romanek — slow beats + serif + big white canvas), never "Apple-inspired".
- One first principle for the film; every palette/type/rhythm/chrome decision must trace back to it; untraceable = decoration, delete.
- Negative lists protect more than positive ones (no purple gradients, emoji, lorem ipsum, Inter display, drawn people, rounded cards with left-border accent).
- Re-read the notes 30 minutes after writing before implementing: find redundant shots, too-big narrative jumps (add transition), misplaced climax (move), chrome misaligned with shot count. 30 minutes saves ~2 hours.

## 504. Notes → implementation
- Reuse standard stage/sprite/easing/interpolate components; paste the color variables verbatim; map element timing exactly to the shot timecodes, adding no shots; build chrome as independent components driven by time; destination content must be genuinely readable (no fake bar lines) — the most-cited detail signature.
- Capture and verify keyframes right after finishing each shot (freeze-at-time URL parameter), not at the end.

## 505. Keyframe verification
- Make every animation freezable at an arbitrary time via a URL time parameter.
- Batch-capture ~13 timecodes for a 30s film (e.g., 0.5, 2.5, 4.9, 7.0, 10.5, 13.5, 16.5, 19.0, 21.5, 23.4, 25.5, 28.0, 29.9) at 1920 wide with ~2.5s settle wait.
- Each capture: nothing overflows the 1920×1080 canvas; tracking/leading correct; key typographic details (colored period, em-dash, italic, small caps) recognizable; chrome positions/states correct; anti-slop passes; a "worth pausing on" 120% detail exists.
- Never skip keyframe verification and go straight to recording — guaranteed rework.

## 506. Multi-perspective parallel direction
- When direction is unsettled, produce several versions in parallel from distinct director/artist DNAs (e.g., publishing-house baseline; Wes Anderson symmetry + vintage + chapter cards; Saul Bass paper-cut + 60s big type + geometric cuts; Wong Kar-wai CJK serif + slow motion + nostalgia; Massimo Vignelli modernist grid + red/black; Kenya Hara minimal whitespace; Yayoi Kusama polka dots + repetition + single strong color).
- Each brief: same background and methodology template, artist DNA of 30–50 words (palette, type, visual language, rhythm, signature, reinforced anti-slop), same task list, same constraints (30s, 1920×1080, local file, web fonts). ~30–60 minutes for 6 versions.
- Never let versions see each other (they converge to average); instruct each not to repeat the baseline aesthetic. Compare only at review: decision table, same-moment keyframe side-by-side, vote.

## 507. Launch-film anti-patterns
- Condensed 1,000-word notes (always miss a Visual System subsection) — go full or skip.
- 5–8 shots for 30s — need 12–15 shots (2–3s each); few shots = uniform rhythm = no climax.
- Delivering notes without the animation — deliver both, notes as design rationale.
- Deferring detail decisions to recording time — recording can't make creative decisions.

## 508. Worked example 30s film — premise and statement
- Spec: 30s · 1920×1080 · 25fps · no voiceover. Thesis film for a Markdown converter's v2.0: "Markdown is the new typewriter." World view: "md is the source code; everything else is product." Capability chain extended from 4 to 6 outputs — framed as the source's radius of influence, not a feature list.
- What it is not: not a feature tour (open → 6 features slide by → logo + slogan → end). Every second must "tell", not "display". If viewers remember one thing: "md is the source code"; features are bonus.
- Reference dialogue and lessons: "Designed by Apple in California" (2013, Mark Romanek) — white ground + serif = design about design; slow beats (captions half a beat slower than reading speed to force lingering); whispered narration (share, don't sell). With no voiceover, push typography and timing to 200%. Apple Silicon launch films (2020–24) — typography can dance; a few characters can disappear, appear, scale, rotate, explode, and reassemble as protagonist across 30s. Hero = the characters "md" + an orange period. Anthropic brand language (2024–26) — terracotta + serif + geometric abstraction as an anti-slop model; inherit but more restrained: terracotta only as accent <8% of frame, 92% ivory and ink. Penguin Classics (since 1947; post-1961 Marber grid) — typographic courage: big serif + one black rule + no illustration; slogan words ARE the image. Pentagram (Scher/Bierut) — spacing and size ratios are math, not intuition. Kenya Hara "White" (2008) — white is a sensibility; ≥60% negative space every shot; negative space is content. Vignelli — "If you can design one thing, you can design everything": no per-shot extra fonts or radii; all shots share one palette, three typefaces, four easing curves.
- Audiences: A existing users (~60% of traffic) — within 30s must know new capabilities 5 (publication-grade PDF) and 6 (standard EPUB) and see visible pro detail (printer crop marks, e-reader frame); those two shots ~3s each with a "★ NEW" tag. B aware non-users (~25%) — realize md should be their source of truth; 6 outputs, one command; the gathering shot shows PDF/DOCX/PPTX/XLSX/HTML absorbed into md. C unfamiliar designers/editors/publishers (~15%) — leave an impression of publishing-house taste unlike other AI tools; the anti-slop checklist exists for them.
- Rhythm plan: 0–3s slow beat (type breathes character by character); 3–6s first acceleration (md is born, six file cards fly in); 6–22s second acceleration (six capabilities, ~3s each, no letup); 22–26s peak (two-line slogan reveal, all chrome in sync); 26–30s gentle close (capability map fades in, last second = brand stamp + faint piano tail). Planned climax ~22s, not 29s (29 = resolution). (The detailed emotion curve later places the emotional peak at 24.5s; keep climax in the 22–25s band.)
- Will-not-do list: no purple gradients (generic "tech" formula, reads as cyber slop); no emoji icons; no drawn people/hands/abstract figures (always misproportioned); no Inter/Roboto/Arial display; no cyber neon / navy #0D1117; no stacked effects (an effect used twice is decoration, three times is slop); no lorem ipsum (all dummy text readable and on-message, e.g., "md is the source. Anything else is product."); no stock photos (about typography, not lifestyle); no progress bar/timecode/copyright bar (that's player chrome and collides with real players); the hero must not look identical in every scene — distinct state per shot, same core glyph.
- Positioning line: "A 30-second film about source-of-truth thinking, made for designers who write and writers who design."

## 509. Worked example — visual system
- Palette (name · HEX · function · max share): Ivory paper #FAFAF6 main ground 60–70%; Mist #F2EDE4 secondary background <15%; Mica #E6E1D6 hairlines/dividers/card borders <5%; Smoke #6B6B6B secondary text/metadata <5%; Cinder #3D3530 secondary dark brown-black <10%; Ink #1A1A1A main black/text 20–25%; Charred #2A2620 deepest brown-black for cover cards <5%; Terracotta #C2410C main accent 5–8%; Terra Hot #E55D21 highlight only when NEW tag flashes <1%; Terra Deep #8B2D08 terracotta shadow <1%.
- Palette laws: no color outside the ten in any shot; terracotta family combined <10% of frame; text only in Ink, Cinder, Smoke, or Terracotta.
- Type scale: Display XXL serif 700 slogan 200px, −0.035em; Display XL serif 700 capability number 48px, −0.020em; Display L serif 600 hero glyph 300–480px, −0.040em; Display M serif 600 chapter title 32–44px, −0.015em; Body L serif 400 18–22px, 0; Body M CJK serif 500 20–26px, +0.04em; Italic serif 400 quotes/subtitles, +0.01em; Mono S 500 labels/counter, +0.18em; Mono XS 700 NEW/version chip 11–14px, +0.22em; typing caret = 3px-wide block.
- Fonts: preconnect to font host; one merged request for all weights; start the clock only after fonts are fully loaded (measured load 800–1500ms).
- Grid: 1920×1080 canvas; 80px safe margin all sides; content area 1760×920; 12 columns of 132px with 16px gutters; 8px baseline — all vertical positions multiples of 8 unless visually justified. Anchors: upper third y=360, lower third y=720, center y=540 (hero default), golden upper y=412, golden lower y=668. Top 60px = chrome zone; bottom 60px = watermark/metadata; central 800×600 = hero zone (every hero lands inside).
- Easings (only four): expoOut 1−2^(−10t) default for ~90% of entrances; overshoot cubic-bezier(0.34,1.56,0.64,1) for NEW tag pops/button reveals; linear for background fades and texture drift; expoIn 2^(10(t−1)) for ~10% of exits.
- Durations: character stagger 30–50ms; small element entrance 300ms; medium element 500ms; hero morph 700–900ms; slogan entrance 800ms; scene overlap 300ms; exits 200–300ms — exits always faster than entrances.
- Stagger: adjacent delays 30–80ms (never 0, never >100ms); 6 pills = 250ms total (~50ms each); slogan characters = 280ms total (~30ms × 10).
- Scene transitions: always cross-dissolve + soft scale, never hard cut; outgoing last 300ms opacity 1→0, scale 1→0.96; incoming first 300ms opacity 0→1, scale 1.04→1; shots overlap 0.3s.
- Chrome A top-left capability counter (0–22s): pulse dot + "CAP·01" label + 6-dot progress; mono 12px, tracking 0.24em; Ink label, terracotta current dot, Mica upcoming dots; next dot fills hollow→solid over 500ms expoOut on each scene change.
- Chrome B top-right version chip (2–30s): "● PRODUCT · v2.0"; mono 13px bold, 0.22em; terracotta dot + ink label; fades in at 2s over 600ms; dot breathes every 4s (opacity 1→0.6→1 over 1500ms ease-in-out).
- Chrome C bottom-center timeline ticker (7–22s): six capability names joined by a line with a progress dot sliding left→right; mono 11px, 0.18em; current in terracotta bold, others Smoke; fades in at 7s over 500ms.
- Chrome D bottom-right watermark (always): mono 10px, 0.24em, rgba(26,26,26,0.32), fully static.
- Chrome E paper texture (always): noise + very slow 0.3% scale breathing, opacity ≤0.04 — almost invisible but makes the frame breathe.
- BGM layers: L0 room tone 0–30s; L1 single piano note every 1.2s, 0–8s; L2 piano arpeggio 3–22s; L3 cello drone 8–22s; L4 faint sub-kick cinematic 4/4 pulse 15–22s; L5 full string swell 22–26s; L6 decay + reverb tail 26–30s leaving piano + reverb. Style target: Max Richter "On the Nature of Daylight", Ólafur Arnalds "Re:member", Jóhann Jóhannsson "Orphée".
- SFX dictionary: keyboard clicks 0.5–2.0s, ×12, −18dB, 30ms each; cursor blink tick 2.0–2.8s, −28dB; md morph swell (soft whoosh + bloom) 2.8–3.2s, −16dB; file-card whoosh ×6 5.5–8.0s, −20dB, 200ms each; absorb/ink-drop splash 8.0–8.4s, −16dB; paper rustle 8.5–9.0s, −22dB; single chimes for capabilities 2/3/4 at 9.0/12.0/15.0s, −18dB; double chime + glow for NEW 5 at 18.0s and NEW 6 at 21.0s, −14dB; ascending build sweep 22.0–22.6s, −10dB; deep impact for slogan line 1 at 22.6s and line 2 at 23.4s, −8dB; pen on paper 24.0–24.4s, −22dB; final ink stamp 29.0–29.5s, −14dB. (Shot-level timings below shift some of these; follow the shot list.)
- Frequency isolation: BGM 40Hz–2kHz; whooshes/chimes 2–8kHz; impacts in sub 40–120Hz, overlapping the cello, so duck the BGM −3dB under impacts.
- Per-shot anti-slop checklist: no purple at any saturation; no rounded card + left-border accent (except an honest Mica border on destination cards); no emoji icons; no drawn figures; no off-palette colors; no Inter/Roboto/Arial display; all tracking/leading/sizes from the type system; vertical positions multiples of 8; terracotta <10% of the shot; at least one detail worth screenshotting when paused; transition is cross-dissolve + scale, not hard cut; the shot "yields" visually to the next at its end (not filled to the last frame).

## 510. Worked example — story arc and emotional beats
- Act I Setup 0–6s: the question "what is the source of truth?" — Shot 1 blank page 0–1.5s; Shot 2 cursor 1.5–3.0s; Shot 3 transformation 3.0–5.0s; Shot 4 gathering begins (overlaps Act II).
- Act II Escalation 6–22s: md radiates six output chains — Shot 4 gathering 5.0–8.5s; Shot 5 md→html 8.5–11.5s; Shot 6 html→md 11.5–14.5s; Shot 7 md→docx 14.5–17.5s; Shot 8 NEW md→pdf 17.5–20.5s; Shot 9 NEW md→epub 20.5–22.5s (overlaps Act III by 0.5s).
- Act III Payoff 22.5–30s: Shot 10 convergence 22.5–24.0s; Shot 11 "ONE SOURCE." 24.0–26.5s; Shot 12 "SIX FORMS." 26.5–29.0s; Shot 13 sign-off 29.0–30.0s.
- Beats: 2.0s first keyboard click (viewer enters); 3.0s md is born (first awe); 8.0s six cards absorbed into md ("md is the source" first clicks); 18.0s first NEW tag (existing users go "oh"); 22.5s all chrome gathers (tension peak); 24.5s "SIX FORMS." lands — emotional climax; 30.0s md stamp rests — resolution.

## 511. Worked example — Shot 01 "Blank Page" (0.00–1.50s)
- Function: open, invite the viewer in, give emptiness its time. Entire frame Ivory paper; nothing else but faint paper texture.
- Anim: texture opacity 0→0.04 over 500ms linear; 0.5–1.5s pure hold so eyes adapt to the white; at 1.4–1.5s the cursor position begins to exist (invisible) at x=860, y=540.
- Audio: room tone fades in over 300ms to −38dB; no SFX. Chrome: all hidden.
- Anti-slop: no logo, no "Loading…", no brand pre-roll, no gradient or effects; texture has presence but never steals focus.
- Why: like the 2013 Apple film, giving blankness time tells viewers to slow down; opening with logo and chrome scatters attention for the remaining 30s. These 1.5s are among the most important.

## 512. Worked example — Shot 02 "The Cursor" (1.50–3.00s)
- A 3×56px Ink block cursor at x=860, y=540 blinks twice (0.7s cycle × 2), then "# markdown.md" types out in mono 500, 56px, Ink, −0.01em, centered on y=540; keyboard click per character; cursor blinks once more after the 13th character.
- Anim: cursor opacity 0→1 in 200ms at 1.50s; blink 1 at 1.50–1.85s (off 200 / on 200ms); blink 2 at 1.85–2.20s; 13 characters at 50ms intervals over 2.20–2.85s (650ms), each fading + 1px slide down, 180ms expoOut; final blink 2.85–3.00s.
- Audio: first piano note at 1.50s, −22dB; 13 key clicks, −18dB, 30ms each; 200ms silence after the last blink to make room for the morph.
- Anti-slop: realistic terminal blink cadence (not a 0.1s sci-fi flicker); rhythmic real typing, not all-at-once; a designed mono font, not system default; the exact 3px caret width is the expert-noticed detail.
- Why: markdown is a verb — keystrokes turning characters into structure; the cursor is the smallest unit of writing; establishes "we are writing markdown" before the morph.

## 513. Worked example — Shot 03 "The Transformation" (3.00–5.00s)
- Morph "# markdown.md" into hero "md.": 3.00–3.30s the "#" and other letters fade out (expoOut) leaving "md"; 3.30–4.10s "md" morphs mono→serif, 56→480px, weight 500→600, same Ink, stays centered (800ms expoOut, using ghost-residue overlap + scale + opacity, never an abrupt swap); 4.10–4.80s terracotta period appears bottom-right (fade + scale 0.6→1, overshoot, 700ms); 4.80–5.00s period settles; a 320px × 2px terracotta accent rule grows from center outward 30px below (300ms expoOut).
- End frame: "md." serif 600, 480px, −0.04em, centered on y=540, ink letters + terracotta period, rule beneath; everything else empty.
- Audio: piano note 2 at 3.00s −20dB, note 3 at 4.20s −18dB (accumulating); soft whoosh at 3.00–3.20s −16dB; subtle bloom at 4.10s −20dB; short paper rustle at 4.80s −22dB.
- Chrome: version chip fades in from 4.50s over 600ms at top 78px / right 80px; others stay hidden until ≥6s.
- Anti-slop: true glyph morph with ghost residue, not fade-out/fade-in; the terracotta period is the hero's signature and persists in every later shot; the accent rule returns under the slogan for bookending; −0.04em tracking makes m and d nearly touch without contact.
- Why: hero is born here; mono→serif = from "typing" to "publishing"; next shot pushes the hero up to make room for products.

## 514. Worked example — Shot 04 "Gathering" any→md (5.00–8.50s)
- Hero slides from y=540 up to y=280 and shrinks to 220px (5.00–5.30s, 300ms expoOut); capability counter enters at 5.30s showing 01.
- Six 130×180px file cards (white, Mica border, 24° top-right fold) — each a readable mini-demo, not fake bars: PDF (two columns, header, page number "— 12 —", tiny real text); DOCX (heading, italic subtitle, 6 paragraph lines); PPTX (title + simple bar chart); XLSX (6×4 grid with numbers); EPUB (e-reader page, "Chapter 01"); HTML (browser chrome with three dots + URL bar + title + paragraph).
- Flight: launch from below at y=1140, one every 0.18s starting 5.60s, each flies 1.1s along a parabola toward the hero's period (~x=1010, y=370); mid-flight they fan 220px apart; absorbed by scale 1→0.5 + opacity 1→0 + converging to a point; last absorbed ~7.60s.
- Tagline "everything → md" (CJK serif italic 36px, Ink; arrow in serif italic terracotta) 60px below, fades in 400ms with 12px rise at 7.60–8.20s; hold 8.20–8.50s.
- Audio: piano arpeggio enters at 5.00s, −26→−20dB; whoosh per card launch, 200ms, −20dB; ink-drop on final absorb, −16dB; paper rustle with tagline, −22dB.
- Chrome: counter on (01), chip on, ticker off, watermark and texture on.
- Anti-slop: cards readable when paused mid-flight; parabolic (gravity) not straight (computer) paths; absorption (scale + position together), not stacking; no glow/particles on the hero; arrow glyph instead of "to".
- Why: Act II's door — three micro-beats in 3.5s: hero yields; products appear; all return to md.

## 515. Worked example — Shot 05 "First Flower" md→html (8.50–11.50s)
- Establishes the reusable pipeline pattern: md left, destination right, arrow + label between, destination card with staggered internal reveal of 6–8 typographic levels, genuinely readable content.
- Hero slides to x=480, y=540 at 220px (8.50–8.80s). Destination 480×560px card at x=1400: essay title serif 600 32px Ink; small-caps metadata mono 11px 0.18em Smoke; 60×3px terracotta rule; 5 lines of readable essay in serif 400 18px, line-height 1.7 ("md is the source of truth. Anything else is product. We write once. Publish six ways. The river forks; the spring stays the same."); italic 14px signature; bottom mono 10px label. White + Mica border + 24° fold.
- A 1.5px solid terracotta line grows 0→380px from the hero's period (8.80–9.10s, expoOut); arrowhead pops at 9.10s (200ms overshoot); label "md → html" mono bold 14px terracotta 0.14em, 30px above the line, enters 9.20–9.40s (fade + 8px slide, 300ms); card enters 9.40–10.10s (700ms expoOut, scale 0.85→1); internals 10.10–10.80s: title 0 → metadata +200ms → rule +400ms → body lines 60ms cascade → signature +1000ms → bottom label +1100ms; 10.80–11.50s hold with micro-breath scale 1→1.005 (600ms, half a cycle).
- Ticker enters at 9.80s at y=1000. Counter → 02.
- Audio: cello drone enters 9.00s, −30→−24dB; capability chime at 9.00s −18dB; paper rustle on card −22dB; micro ticks per text line −26dB.
- Anti-slop: real readable essay; paused-readable bottom label; no glow for the conversion; solid line, not dashed/dotted (avoid tutorial look); small-caps metadata at 0.18em is the 120% detail.
- Why: repeating the pattern lets viewers recognize it by the second instance and feel "again — but NEW" by the sixth.

## 516. Worked example — Shot 06 "Reverse Flow" html→md (11.50–14.50s)
- Previous card shrinks to bottom-right and fades (11.50–11.80s); the only dark shot in the film: 480×560 Charred card showing markdown source in mono 14px — heading in terracotta, quote lines italic Smoke, bold word in Mica bold, list items "1 source / 6 forms / ∞ outputs" in Smoke, bottom label mono 10px; fold in Cinder.
- Arrow grows right→left (11.80–12.10s), arrowhead pointing left at 12.10s, label "html → md" 12.20–12.40s, card 12.40–13.10s, six lines 13.10–13.80s at 100ms each with character-by-character typewriter cascade, hold 13.80–14.50s.
- Audio: L1+L2+L3 continue; chime at 12.00s −18dB; rustle at 12.40s; faint key-click per line −26dB, 100ms apart.
- Chrome: counter 03; ticker dot slides to html→md.
- Anti-slop: deliberate contrast to signal "source code"; syntax colors from the publishing palette, not editor dark themes; reverse arrow is straight + flipped, not a U-turn, for structural consistency.
- Why: proves the pipeline is bidirectional; placing the reverse capability third maximizes cognitive surprise.

## 517. Worked example — Shot 07 "Publisher Grade" md→docx (14.50–17.50s)
- Back to light ground. 480×580 chapter opening page: right-aligned italic running header 9px Smoke 0.14em; "CHAPTER · 01" mono bold 11px terracotta 0.22em; title serif 700 36px Ink, line-height 1.05; italic 14px subtitle Smoke; full-width 3px terracotta rule; 10 Mica placeholder paragraph bars 6px tall, widths 76–95%; centered page number "— 1 —" mono 10px Smoke 0.18em using true em-dashes.
- Anim: exit 14.50–14.80s; arrow 14.80–15.10s; arrowhead + label 15.10s; card 15.30–16.10s; internals 16.10–17.00s: header 0 → chapter +100ms → title +300ms → subtitle +500ms → rule +700ms → bars +850ms with 60ms cascade → page number +1600ms; hold 17.00–17.50s.
- Audio: BGM swells +2dB at 15.00s; chime at 15.00s −18dB; rustle at 15.30s.
- Anti-slop: no explanatory caption; Mica bars honestly signal "layout preview, not content"; running header is the 1%-of-designers detail; most saturated capability shot, matching the mid-arc build.
- Why: shows md isn't only for the web and sets up print context for the two NEW shots.

## 518. Worked example — Shot 08 "★ NEW · Print" md→pdf (17.50–20.50s)
- Visual intensity noticeably above shots 5–7. NEW tag beside the counter: "★ NEW" mono bold 13px terracotta 0.22em in a terracotta-bordered box (6×12px padding; border 1.5–4px). Two fanned PDFs: A4 behind at +5° (360×460, "A4 · 210×297mm" label mono bold 10px terracotta 0.2em, serif 22px title, 7 Mica bars) and a 176×240mm book format in front at −3° (290×410, serif 19px title, 6 bars); L-shaped 2px Smoke crop marks at each corner. Arrow and label fully terracotta.
- Anim: exit 17.50–17.80s; NEW tag at 17.70s scales 0.8→1.1→1.0 over 400ms overshoot with a brief faint terracotta glow; arrow + label 17.80–18.10s; front PDF 18.20–18.60s (400ms expoOut, scale 0.85→1, rotate −8°→−3°); back PDF 18.50–18.90s (scale 0.85→1, 0°→+5°, 300ms stagger); internals 18.90–19.70s; four crop marks at 19.70s in 80ms cascade; hold to 20.50s.
- Audio: sub-kick pulse enters 18.00s at −32dB; NEW double chime + soft glow + reverb tail at 17.70s, −14dB — one of the film's most important cues; paper rustle per PDF −22dB; faint ink stamp with crop marks at 19.70s −22dB.
- Chrome: counter 05 + NEW tag; version-chip dot pulses in sync; ticker dot at md→pdf, that label +0.5px larger.
- Anti-slop: NEW is a typographic mark, not an emoji/sticker; fan + rotation suggests opening, not cheap stacking; crop marks prove print-readiness; no glow/particles — typography and SFX carry "new"; bilingual paper-size label respects local book formats.
- Why: must instantly read as new AND prove real publication quality; NEW tag + crop marks + fanned pair + exact sizes do both. The next NEW shot must rise one more notch.

## 519. Worked example — Shot 09 "★ NEW · Ebook" md→epub (20.50–22.50s)
- Shorter (2.0s vs 3.0s): the NEW + destination pattern is learned, so accelerate.
- 460×470 e-reader window card: three window dots, 22px corner radius, 2px Ink border; Charred cover area with brand label mono bold 10px terracotta 0.22em, title "On / Markdown" serif 700 30px Ivory with a deliberate line break (Penguin-cover homage), 40×2px terracotta rule, italic 14px author in Smoke, footer "Books · 1 of 24 · EPUB 3" mono 10px Smoke 0.14em.
- Anim: exit 20.50–20.80s; NEW tag stays lit at 20.70s (no re-pop — already established); arrow + label 20.80–21.10s; card 21.20–21.80s (600ms expoOut, scale 0.88→1); internals 21.30–22.00s: dots 0 → brand +200 → "On" +400 → "Markdown" +480 → rule +700 → author +850 → footer +1000ms; hold 22.00–22.50s.
- Audio: BGM +3dB swell at 22.00s; NEW chime at 20.70s, −14dB, a half-step higher than shot 8 so the two NEW shots relate musically; subtle window click at 21.20s −24dB; page-turn rustle at 21.40s.
- Chrome: counter 06 — all six dots filled; chip pulse amplitude ×1.5; ticker dot reaches far right.
- Anti-slop: no real reader-app logos (IP risk) — window chrome implies "reader"; no e-ink gray filter; realistic chapter metadata.
- Why: closes Act II (6/6) and starts the build to the climax; shortening 3.0→2.0s signals acceleration.

## 520. Worked example — Shot 10 "The Convergence" (22.50–24.00s)
- Bridge shot, can't be empty waiting. Last card exits and counter + ticker fade (22.50–22.80s, 300ms linear) — chrome leaves once its job is done. Hero slides back to center x=960 and grows 220→300px (22.50–23.00s, 500ms expoOut).
- Six capability labels appear on a circle r=380px, every 60°, clockwise from the top, mono bold 14px 0.16em (first four Smoke, two new terracotta), 80ms stagger, 300ms fade + 20px outward slide (22.80–23.40s); hold 23.40–23.80s; all fade together 200ms linear while hero shrinks to 180px (23.80–24.00s).
- Audio: all-layer swell +4dB from 23.00s; percussion drops one beat at 23.50s for sudden-silence tension; faint clicks per label −30dB; ascending sweep 23.50–24.00s.
- Chrome: chip stays, internal spacing tightens slightly.
- Anti-slop: labels settle at fixed positions then fade together — never orbit around the hero (planet-spinner slop); the 23.40s frame is the only full capability panorama — best marketing screenshot.
- Why: all flows return to the source; hero shrinks to become the slogan's brand stamp.

## 521. Worked example — Shot 11 "ONE SOURCE." (24.00–26.50s)
- Hero slides to top-left (x=128, y=88), 180→56px, 300ms expoOut — becomes the corner brand stamp.
- "ONE SOURCE." serif 700, 168px, −0.03em, line-height 0.95, Ink, centered at baseline y=460; letter-by-letter reveal from 24.20s, 30ms stagger across 11 positions (space reserves layout), each character fade + 12px slide down + scale 0.92→1.0, 260ms expoOut; complete by ~24.50–25.00s; hold 25.00–26.00s to be read; 320×3px terracotta rule grows from center 30px below at 26.00–26.30s; hold to 26.50s.
- Audio: swell peaks at 24.50s (loudest so far −6dB); full strings (cello + violin + viola); deep bass impact + short reverb at 24.20s, −8dB — strongest cue; faint pen stroke at 26.00s −22dB.
- Chrome: version chip cross-dissolves to a slightly larger form (16→18px), dot pulse ×2.
- Anti-slop: letter stagger, not whole-word fade; 30ms is tuned (60ms would drag); 168px verified to clear the second line; the slogan's period is terracotta, echoing the hero's period.
- Why: thesis line; hero retreats so slogan is protagonist and stamp is signature — no competition.

## 522. Worked example — Shot 12 "SIX FORMS." (26.50–29.00s)
- Second line "SIX FORMS." serif 700, 168px, −0.03em, terracotta, centered at baseline y=720; mirror reveal with 30ms stagger but slide UP 12px + scale 0.92→1, 260ms expoOut; complete at 27.20s; short hold to 27.30s.
- Six capability pills centered at y=820, 14px apart: mono bold 14px 0.16em, 10×18px padding, 1.5px border; first four Ink text/border, transparent; two new ones terracotta text/border on very pale tint #FFF7F0 with a 9px terra-hot "NEW" mini badge at −8/−10px top-right; left→right 80ms stagger, fade + 4px rise, 300ms (27.30–27.80s).
- Subline (CJK serif italic 26px, Ink, 0.04em) "md is the source code; everything else is product." at y=890, fade + 8px rise 400ms (27.80–28.30s); full static hold 28.30–29.00s — the film's stillest frame so viewers finish reading.
- Audio: BGM loudest of the film −4dB at 27.20s then sustains; impact at 26.50s slightly heavier than the first, −7dB; metallic clicks per pill −24dB, 50ms; faint pen flourish at 27.80s.
- Anti-slop: Ink line = source, terracotta line = products (meaningful color, not decoration); pale tint instead of orange fill; tiny badge at the standard detail position; native CJK punctuation; the 28.30s frame contains everything (slogan + six capabilities + subline + stamp + version) — use as thumbnail/poster/cover.
- Why: resolution — thesis then antithesis + synthesis.

## 523. Worked example — Shot 13 "Sign-off" (29.00–30.00s)
- 29.00–29.20s hold; 29.20–29.60s all slogan elements fade out simultaneously, 400ms linear, no stagger (the frame "settles"); 29.40–29.80s the corner stamp grows 56→88px and slides (128,88)→(960,540), 400ms expoOut; 29.80–30.00s a shorter, finer 120×2px terracotta rule grows beneath (200ms expoOut); final hold at 30.00s (loop to 0 if looping).
- Final frame has only four elements: centered "md." (serif 600, 88px), accent rule, top-right chip, bottom-right watermark.
- Audio: decay into L6 from 29.00s; strings fade at 29.40s leaving piano + reverb; silence + room tone at 30.00s; ink stamp + soft reverb at 29.40s, −14dB; faint rustle at 29.80s.
- Anti-slop: no "Thank you"/"Made with love"; no giant logo zoom; eye path = terracotta dot → rule → version chip; last 0.2s of silence gives breathing room.
- Why: bookend — blank ivory page at 0s, ivory page + one glyph at 30s; "full" is just one simple source.

## 524. Worked example — production manifest
- Fonts: preconnect to font hosts; one stylesheet request with serif weights 300–700 + italics 400/500, mono 400/500/700, CJK serif 400/500/700/900.
- BGM: generate a 30s minimal cinematic piece — prompt keywords: minimal cinematic piano, slow tempo 60bpm, single piano notes, sparse arpeggio, low cello drone, subtle sub-kick percussion, swelling strings at climax, decay to silence, no vocals, 30 seconds; fall back to royalty-free libraries searched for "minimal cinematic". Minimum: 30s length, 44.1kHz, target −16 LUFS integrated.
- SFX mapping by event: key clicks, soft tick, whoosh-bloom, short whooshes, ink drop, paper turn, single chimes, warm double chime, ascending sweep, deep impacts, pen stroke, ink stamp.
- Keyframe plan (16): 0.5 blank page (texture doesn't steal focus); 2.5 typing (blink cadence + mono); 3.8 morph (ghost residue + scale curve); 5.0 hero settled (480px + terracotta dot); 7.0 cards in flight (parabola + readable content); 8.4 tagline (CJK italic); 10.5 html card (essay readable); 13.5 md source (syntax colors); 16.5 docx (chapter title + page number); 19.0 PDFs (crop marks visible); 21.5 epub (reader chrome); 23.4 capability ring (panorama); 25.0 line 1 (tracking + terracotta period); 27.5 both lines + pills; 28.5 marketing frame; 29.9 final hold (stamp + rule). Each: no overflow beyond 1920×1080; tracking/leading correct; anti-slop passes; key details (terracotta dot, em-dash page number, small caps) recognizable.
- Recording: 30s, 25fps, 1920×1080; H.264, yuv420p, 12 Mbps (~45MB for 30s), high profile, slow preset (quality over speed); optional 60fps derivative.
- Mixing: BGM at −18dB, then each SFX cue delayed to its timecode and mixed without normalization; AAC 192k; verify audio stream = AAC, 44.1 or 48kHz, 2 channels, duration 30.0s.
- Deliverables: main MP4 (30s, 1080p, 25fps, with audio, ~50MB); 60fps version (~80MB, for X/YouTube); GIF (<8MB, for article embeds); silent MP4 (for re-scoring); poster PNG from t=28.5s; director's notes; source; shot list CSV with timecodes and key parameters.
- Time estimate: implementation 4–6h; keyframe verification 1h; silent recording 5–10min; BGM 30min; SFX cueing + mix 2–3h; GIF 5min; poster 10min; delivery 10min; total 8–11h.
- First principle: "A typographic film about the source, starring one 'md.' glyph." If a decision can't trace back to it, don't do it.
- Lessons from the sample's own drift: keep counts consistent (the notes say 12 shots and "5 colors/3 fonts/4 easings" while specifying 13 shots and 10 colors) and keep the SFX dictionary synced with per-shot cue times — reconcile on the 30-minute re-read.

---

# Part 42 — Voiceover & Narration

## 525. Narration-first principle
- Write and synthesize the narration first; the audio's measured durations drive the visuals (for 5–20 minute explainers, tutorials, long-form knowledge videos).
- Failure mode #1: a slideshow with voiceover.
- For pieces <60s, a silent animation + post-dubbing suffices; no timeline driving needed. Pure-music videos skip this too. Real recordings can replace synthesized voice with the same downstream flow.

## 526. Rule 1 · One continuous motion narrative
- Make one continuous film, not N scenes; choose 1–2 hero elements present from t=0 to the end.
- Each cue is a state change of the hero (position/size/color/perspective/form), not a new element.
- Scene boundaries exist in the script, never on screen.
- Example skeleton (md vs html essay): opening — the two words face off at center (md at 50/35%, html at 50/65%, scale 1); md-side — md grows (≈x78/y50, scale 1.6) while html retreats to a corner (≈x92/y8, scale 0.25, opacity 0.4) with data flooding around md; html-side — reversed; the-real-question — both return to center with "≠" between; the-split — pushed to opposite sides, gap widening; activity-proof — alternate flashes along a timeline; closing — settle into final answer positions.
- Morph from the previous scene's state to the current over the first ~45% of the scene, capped at 2.0s, with expoOut; hold the rest.
- Add subtle breathing so every frame moves: scale × (1 + sin(t·0.6)·0.012).
- Hero glyphs in the example: 360px, weight 800, line-height 1; md #1B4965, html #C04A1A.
- Counter-example: per-scene independent layouts with full-page opacity cross-switches and monotone fade-up cues (opacity p, translateY (1−p)·30px) → "flipping keynote pages".

## 527. Rule 2 · No hard cuts between scenes
- Morph scene A's core elements into B rather than cross-fading A out and B in; elements persist and only change position/form; the hero shares one persistent node across scenes.
- The subtitle bar is the only non-hero persistent entry and exits together with the hero's motion.
- Scene-specific auxiliary elements (data cards, quotes) enter with expoOut + stagger and exit with a fade overlapping the next scene — never hard-cut.

## 528. Rule 3 · Every frame must move
- Pause on an arbitrary (non-cue) frame; if completely still, add underlying motion.
- Always run something: hero scale 1↔1.02 on a 5-second loop; background translateX 0↔−20px slow drift; data cards keep subtle noise-driven translateY jitter after entering; or camera pan/parallax.

## 529. Rule 4 · Easing, stagger, hold baseline
- Easing: expoOut cubic-bezier(0.16,1,0.3,1) as main axis; overshoot for emphasis; spring for landings. Forbidden: linear, default ease.
- Multi-element entry: 30ms stagger; never everything at once.
- Before key cues: hold 0.3–0.5s (previous elements rest 0.3s, then the cue fires); never jump to the next scene right after a line.
- Ending: stop abruptly and hold the last frame 1s; no fade to black.

## 530. First-viewer reaction scale
- "A slideshow with voiceover" = fail, redo; "visuals switch with the sound" = below passing, hero missing or not spanning; "this thing moves" = passing but forgettable; "I want to keep watching" = good pacing; "I want to screenshot this" = great.
- Test on someone fresh, or yourself 24 hours later.

## 531. Narration script format
- Front matter: title; optional voice; speed 0.5–2.0 (default 1.0); gap = silence between scenes, default 0.3s (examples use 0.4s and 0.5s).
- Scenes marked with lowercase-hyphen IDs (e.g., what-is, scene-1).
- Place cue markers in the middle of key sentences at the exact word where the visual should fire; the instant after the cue is the trigger.
- Write for rhythm with short sentences — long sentences come out flat in TTS.
- Strange punctuation or emoji cause mis-parsing and wrong scene lengths — remove them.
- If a subtitle line splits badly, move the cue (cues subdivide scenes) rather than adjusting line-break logic.

## 532. Measured timeline
- Split each scene at cues, synthesize each chunk separately, and accumulate measured durations; never estimate timing linearly from character counts.
- Keep per-scene start/end/duration, per-chunk relative and absolute times, per-word/character timestamps, and per-cue absolute times.
- Listen to the whole voiceover before designing; if pacing is off, revise the script — this step sets the quality ceiling.
- Answer the iron-rule questions before designing: what is the hero, what state per scene, how it morphs between scenes.
- Cue ramp default: 0.6s from 0→1 after firing.

## 533. Workflow (10 steps)
- 1 write script (it is the source); 2 synthesize voiceover + timeline; 3 listen to all of it, revise script if needed; 4 define hero states and morphs; 5 build the animation driven by the timeline; 6 live preview with audio; 7 first-viewer check (fail → back to 4); 8 record and mix voice; 9 optional BGM (educational/tech/tutorial mood); 10 deliver live HTML + final MP4.

## 534. Subtitles
- On by default — long narration without subtitles loses retention.
- No background bar, no blur backdrop (it weighs down the frame).
- Light backgrounds: dark ink #1a1a1a with white glow; dark backgrounds: white text with ~rgba(0,0,0,0.85) glow. Never white text with black outline on light backgrounds.
- Size 32px at 1080p (<24px unreadable; >40px steals focus).
- Sans-serif CJK UI fonts (serif reads as movie subtitles).
- Position bottom 90px, not hugging the edge.
- Line length ≤12–13 characters (mixed CJK/Latin: Latin letters and digits count 0.5); >15 can't be read on mobile.
- Line-breaking: split at sentence-ending punctuation first (。！？ / . ! ?), then merge clauses at weak punctuation (，、；：) up to the max length; hard-cut only as rare fallback; never cut across a sentence period or mid-word.
- Karaoke mode: highlight the word being spoken (default brand orange #e8590c), whole line shown; falls back to normal chunk mode without word timestamps.

## 535. Recording and sync considerations
- Live playback follows the audio's current time; video recording runs a self-driven clock from 0 with seek support.
- Out-of-sync live playback: preload the audio. Stutter in recordings: reduce heavy box-shadow/blur or pre-composite.

## 536. Worked narration script A — "md or html — it's a dumb question" (gap 0.5s; ~3 min 21 s; 7 scenes; 21 cues)
- opening: "A couple of days ago, [cue: thariq] Thariq from the Claude Code team posted a viral essay. The title was one line: HTML is the new markdown. He said he barely writes md files anymore; he has AI generate HTML for everything. Five million reads, and X immediately erupted. One camp is the md camp, [cue: two-camps] who think md is the source code of the AI era. The other camp thinks Thariq is right — HTML is the ultimate answer."
- md-side: "The md camp's evidence is actually solid. Look at AGENTS.md, released by OpenAI last year — [cue: agents-md] used by 60,000+ projects; AWS, Anthropic, Google, Microsoft, OpenAI — half of AI — donated it together to the Linux Foundation as an open standard. Karpathy's llm-wiki is essentially three layers of markdown; a single CLAUDE.md file, 50,000 stars. Cloudflare measured it: [cue: token-saving] the same blog post is 16,000 tokens in HTML and only 3,000 in md. 80% saved. GitHub also said it officially: documentation no longer describes code — [cue: doc-is-code] documentation is code."
- html-side: "But the html camp isn't wrong either. I agree with several of Thariq's arguments. First, spatial information. [cue: spatial] Diffs, call graphs, architecture diagrams inherently have spatial dimensions; md flattens them into a line of text, html can lay them side by side — comprehension is on a different order. Second, dynamic experience. [cue: dynamic] When prototyping, what color a button turns when pressed, what easing curve — no amount of text helps; html lets you see it. Third, structured reading. [cue: structured] Collapsible sections, tabbed code blocks, sidebar glossaries — that's a different thing from the same words stacked linearly. Anthropic's Live Artifacts have already upgraded HTML from static output to interactive dashboards that pull live data."
- the-real-question: "After reading it all I want to say: [cue: reveal] these two are arguing over a dumb question. Both sides won. But they won different questions. The md camp answers [cue: question-md] what we write with. The html camp answers [cue: question-html] what we show people. Those are two questions. How could one replace the other?"
- the-split: "I think the real question is this. md and html aren't substitutes — [cue: split] it's a division of labor. Before, you wrote md and read md yourself. You had to compromise, so md won. But since AI arrived, [cue: ai-changes] there's a new situation for the first time. Production cost can be absorbed by AI. The heavy cost of HTML, AI carries for you. You only consume. A need that used to require compromise has been split into two extreme optima. The production end must be light, fast, token-efficient — [cue: md-side-win] that's md. The consumption end must be rich, visual, shareable — [cue: html-side-win] that's html. Each end reaches its own summit. The compromise in the middle — nobody needs it anymore."
- activity-proof: "The cleanest living example is Thariq himself. In March he published a Skills guide, [cue: thariq-march] stressing the core is still markdown. In May he published HTML is the new markdown. Same person, [cue: same-person] each end at its summit, no conflict. The Karpathy–Lex Fridman pair is the same. The core is a markdown wiki, [cue: karpathy-lex] the shell is dynamic HTML. Lex didn't replace Karpathy; he added a consumption layer on top of Karpathy's base."
- closing: "So next time you feel like arguing about this, [cue: final] ask yourself one thing first. Are you facing 'writing' or 'viewing'? Writing — [cue: md-final] use md. Viewing — [cue: html-final] use html. The tools handle the switch for you. You can put down your stance."

## 537. Worked narration script B — "What is a token" (gap 0.4s; 4 scenes; 4 cues)
- intro: "Have you ever wondered — [cue: question] when we talk with AI, how does AI actually understand what we say?"
- token-1: "The answer is it doesn't understand characters at all — [cue: reveal] it only recognizes tokens."
- token-2: "You can think of a token as AI's smallest unit of information. For example, the four characters for 'artificial intelligence' — [cue: split] to AI may be two tokens: 'artificial' and 'intelligence'."
- ending: "So next time you see a phrase like 'million-token context', [cue: context] you'll know it's saying how many of these little chunks AI can remember at once."

## 538. Narration pacing rules drawn from the scripts
- One short sentence per line; average line ≈25 characters (essay) — each line ≈3–4s of speech; a line of 35+ characters is the upper end (short explainer).
- Essay density: ~670 CJK characters + Latin terms over ~201s ≈ 3.3 CJK characters/s plus terms; ~29s per scene; ~1 cue every ~9.6s; 2–4 cues per scene.
- Explainer density: one idea per scene, one cue per scene, 1–2 sentences per scene.
- Open with a hook: a recent event or a direct question to the viewer ("Have you ever wondered…").
- Place each cue right before the payload word/number/concept (a statistic, a named artifact, the reveal word), not at sentence start.
- Structure arguments as setup (two camps) → evidence each side (numbered "First/Second/Third", each with its own cue) → reveal ("it's a dumb question") → reframe (division of labor) → proof by example → call-back closing.
- Use concrete numbers as cue anchors (60,000 projects; 50,000 stars; 16,000 vs 3,000 tokens; 80%).
- Land the reveal with very short consecutive lines ("Both sides won." / "But they won different questions.") — staccato raises emphasis.
- Close with a parallel, symmetric pair ("Writing — use md. Viewing — use html.") and a cue on each half; final line releases tension ("You can put down your stance.").
- Close by calling back to the opening frame/question and give the viewer a reusable takeaway ("next time you see…").

---

# Part 43 — Audio Design & Mixing

## 539. Dual-track system (mandatory)
- Always design two independent layers: SFX beat layer (0.2–2s, punchy, frame-aligned tight sync, ≥800Hz band) and BGM ambient bed (continuous 20–60s, section-level loose sync, <4kHz band).
- BGM-only animation feels crippled — the picture moves but nothing answers in sound; this is the root of cheapness.

## 540. Levels and loudness
- BGM volume 0.40–0.50 relative to full scale; SFX 1.00.
- BGM sits 6–8dB below SFX peaks; prominence comes from the gap, not SFX loudness.
- Mix without normalization (normalization flattens dynamics).
- If SFX are harsh: drop SFX to 0.7 and BGM to 0.3, preserving the gap.
- Final BGM master target ≈ −16 LUFS integrated, 44.1kHz minimum; launch-film BGM bed placed around −18dB under SFX cues in the −8 to −30dB range.

## 541. Frequency isolation
- Low-pass BGM at 4kHz; high-pass SFX at 800Hz — ear sensitivity peaks at 2–5kHz (presence band); a full-band BGM masks SFX there.
- Cinematic variant: BGM 40Hz–2kHz; whooshes/chimes 2–8kHz; impacts 40–120Hz with BGM ducked −3dB under them.

## 542. Fades
- BGM fade-in 0.3s; BGM fade-out 1.5s at the end (N−1.5s); SFX use their own envelopes (no extra fades). A simpler music-add path uses 0.3s in / 1s out.

## 543. SFX density
- Feature-dense tool demo: ~9 per 10s; meditative dev-tool piece: 0 per 10s; balanced productivity: ~4 per 10s.
- Calm/focused personalities: 0–3 per 10s, BGM carries; lively/info-heavy: 6–9 per 10s, SFX drives.
- Don't sound every beat; cutting 30–50% of cues makes the rest more dramatic; whitespace is more premium than density.

## 544. Cue priority
- P0 must-have: typing, click/selection (decision moments), focus switch (protagonist changes), logo reveal.
- P1 recommended: element enter/exit (modal, card), completion/success, AI generation start/end, major scene transitions.
- P2 optional: hover/focus-in, progress ticks, decorative ambience.

## 545. Sync precision
- Same frame (0ms): clicks, focus switches, logo landings.
- 1–2 frames early (≈−33ms): fast whooshes (anticipation).
- 1–2 frames late (≈+33ms): landings/impacts (physics).
- Every SFX within ±1 frame of its visual beat.
- Advanced: design the SFX timeline first and align visuals to it; SFX chasing visuals tends to feel ±1 frame off.

## 546. Stacking limits
- Max 2 SFX at the same instant; 3 allowed only if BGM is below 0.3.
- Clear other SFX around brand impacts — leave a 0.2s gap before the landing.
- Keep SFX under 0.5s and cue spacing ≥0.2s to avoid smearing.

## 547. BGM selection
- Product launch/tech demo → minimal synth + piano; tutorial/tool usage → warm instructional or near-imperceptible lo-fi ambient; education/explainer → curious, warm, bright (light guitar/e-piano); marketing/promo → upbeat electronic with build + drop; keep an alternate per style.
- Avoid strong-beat music that clashes with SFX rhythm; use ambient/minimal synth.
- Skip BGM when: shorter than 10s (never establishes); focused/meditative personality; scene already has ambience or voiceover; SFX density is already high. 0 SFX + pure lo-fi BGM can also be premium.

## 548. Scene recipes
- A Product launch hero, 25s: tech BGM at 45%, <4kHz; ~6 SFX/10s; typing ×4 at 0.6s intervals → enter → cards converge ×4 staggered 0.2s → click on selection → whoosh on ripple → focus ×4 → logo thud 1.5s; BGM 0.45 / SFX 1.0, no normalization.
- B Tool feature demo, 30–45s: tutorial BGM at 50%; 0–2 SFX/10s; BGM + voiceover drive; SFX only at decisive moments (save, command completes).
- C AI generation demo, 15–20s: tech BGM or none; ~8 SFX/10s; input → type + enter; processing → AI-process loop 1.2s (loop 2–3 times); complete → completion tone; result → sparkle.
- D Pure-atmosphere long shot, 10–15s: no BGM; 3–5 carefully designed solo SFX, each the protagonist; for single-product slow motion and close-ups.

## 549. Timbre matching
- Warm beige/paper visuals → wooden/soft timbres (soft clicks, paper snaps); cold dark tech → metallic/digital (beeps, pulses, glitches); hand-drawn/playful → cartoonish (boing, pop, zap). Warm-beige example: mechanical key + soft card snap + cinematic bass logo hit.

## 550. Audio QA checklist
- SFX peak − BGM peak gap 6–8dB; BGM LP 4kHz + SFX HP 800Hz; no normalization; BGM 0.3s in / 1.5s out; density matched to personality; all cues ±1 frame; logo sound ~1.5s.
- Solo test: mute BGM — SFX alone carries rhythm; mute SFX — BGM alone has emotional contour. Each layer must stand alone.
- Final deliverable audio: AAC 192k, 44.1 or 48kHz, stereo, duration equal to video.
- Some social-feed players mute autoplay — not a defect; GIFs are silent anyway.

---

# Part 44 — Sound Effects Usage

## 551. Library principles
- Target keynote-grade clarity: 44.1kHz, tight, minimal, no added reverb unless ambient.
- Generation/search prompts need three parts: physical description (object + action), texture/style qualifier (keynote-style, iOS-style, cinematic, retro), exclusions (no reverb, clean studio, minimal). Bad: "click sound". Good: "crisp UI button click, clean modern interface sound, high pitched". Bad: "magic". Good: "bright twinkling stars, high-pitched glittery chime, fairy dust".

## 552. Category: Keyboard (tactile input)
- Single key 0.5s (mechanical key press); rapid typing 1.5s (prompt input); backspace 0.5s (low-pitched thud); spacebar 0.5s (soft, wide, flat); enter 0.5s (crisp, tactile confirm).

## 553. Category: UI (tactile decisions)
- Standard click 0.5s (crisp); soft click 0.5s (secondary buttons/links, mid pitch); focus/selection tone 0.5s; hover 0.5s (barely audible tick); mobile finger tap 0.5s (muted thud); toggle on 0.5s (satisfying flip).

## 554. Category: Transition (element enter/exit)
- Standard whoosh 0.5s; fast whoosh 0.6s (title flash-in, tab switch); horizontal swipe 0.7s (carousels); slide-in 0.6s (panels, drawers; soft whoosh with arrival); dissolve 0.8s (image fades; airy shimmer).

## 555. Category: Container (cards, modals)
- Card snap into place 0.5s; card flip 0.7s (front/back); stack collapse 0.8s (list aggregation; paper taps); modal open 0.6s (whoosh + thud).

## 556. Category: Feedback (state)
- Success chime 1.0s (two ascending bell tones); error tone 0.7s (soft descending two-note); notification pop 0.6s (toasts); achievement 1.5s (triumphant rising arpeggio, milestones).

## 557. Category: Progress (passage of time)
- Loading tick 0.5s (soft short pulse, progress beat); completion 0.8s (two ascending tones); generation start 0.8s (soft rising shimmer).

## 558. Category: Impact (brand landings, key moments)
- Logo thud 0.7s; long cinematic logo hit 1.5s (bass with shimmer tail); stamp slam 1.0s (verification/sealing); drop thud 0.7s (object landing on wood).

## 559. Category: Magic (AI, transformation)
- Sparkle 0.8s (highlights, surprises); AI processing hum 1.2s (thinking state, loopable); transform 1.0s (morph; rising shimmer whoosh + sparkle tail).

## 560. Category: Terminal (CLI/code demos)
- Command execute 0.5s (crisp digital beep + tick); output appear 0.6s (rapid digital ticks); cursor blink 0.5s (soft rhythmic pulse; idle ambience loop).

## 561. Category: Foley/cinematic (launch-film palette)
- Paper turn/rustle for card and page entries (≈−22dB); ink drop for absorption (≈−16dB); pen stroke/flourish for rules and sublines (≈−22dB); ink stamp for sign-off (≈−14dB); single chimes per step (≈−18dB); warm double chime for "new" moments (≈−14dB, second one a half-step higher); ascending sweep for build-ups (≈−10dB); deep impacts for slogan lines (−8/−7dB, second slightly heavier); faint ticks per text line (≈−26 to −30dB); room tone bed (≈−38dB).

## 562. Selection decision tree
- Tactile (typing/clicking/swiping) → keyboard or UI; element enter/exit → transition; card/modal ops → container; success/failure/notification → feedback; progress/time → progress; brand landings/key moments → impact; AI/transformation → magic; command line/code → terminal.

## 563. Recommended sequences
- Terminal: type 0.5 → enter 0.5 → execute 0.5 → output 0.6; cursor blink as idle loop.
- Card selection: hover 0.5 → soft click 0.5 → card snap 0.5 (advanced: card flip).
- AI generation: start 0.8 → processing 1.2 → sparkle 0.8 → complete 0.8 (error tone on failure).
- Logo reveal: fast whoosh 0.6 (build) → cinematic logo hit 1.5 (landing) → sparkle 0.8 (tail); simple: whoosh → logo thud.
- Mobile UI: tap 0.5 → slide-in 0.6 → toggle 0.5; finish with success chime or notification pop.
- Dashboard/data viz: loading tick 0.5 × N → complete 0.8 (data lands) → achievement 1.5 (showstopper).
- Form submit: soft click 0.5 → loading tick ×2 (1.0s) → success chime 1.0; failure: error tone 0.7.
- Magic transform (morphs, before/after, AI rewrite): fast whoosh 0.6 → transform 1.0 → sparkle 0.8.

---

# Part 45 — Video Export Specs

## 564. When to export
- Only after the animation runs fully, is verified at each time point, and the client has watched it in the browser; never export with known bugs — changes cost far more after export.

## 565. Default formats (produce all three)
- MP4 25fps: 1920×1080, H.264, CRF 18; ~1–2MB per 30s of flat animation; for article embeds, short-video channels, YouTube.
- MP4 60fps: 1920×1080, H.264, CRF 18; default by frame duplication (max compatibility); motion interpolation only on explicit request; for true 60fps, render per-frame from a seekable clock; ~1.5–3MB per 30s; for high-frame-rate showcases, portfolios.
- GIF: 960×540, 15fps, palette-optimized; ~2–4MB per 30s (≈3MB typical); for X, READMEs, chat previews. Width options: 960 default, 1280 sharper/larger, 600 loads faster on X.
- High-quality launch-film master: H.264, yuv420p, high profile, slow preset, ~12 Mbps (~45–50MB per 30s); 60fps version ~80MB; GIF <8MB.

## 566. Real-time recording vs per-frame seek rendering
- Real-time headless capture is locked to 25fps, includes black loading frames to trim (≈2.2s default trim; font wait ≈1.5s, raise for many fonts), and needs interpolation for 60fps.
- Per-frame seek rendering gives true native fps at any value, no black lead-in, deterministic output independent of machine load; default 60fps, 4 parallel workers, wait 2 animation frames after each seek (raise for layout-heavy pieces); slower for long videos and uses disk for frames. Requires the animation to be driven by a seekable clock.
- Two-stage render: fast preview at 30fps first; final at 60fps only after eye-check and frame-check pass (a 600-frame 1080p 60fps render ≈20s).

## 567. fps interpolation caveats
- Motion-compensated interpolation (bidirectional estimation, overlapped block compensation, variable block size) works well for transform motion (translate/scale/rotate) but can ghost on pure fades and its output may fail to open in some native players — test on the target player before delivery; default to frame duplication.

## 568. GIF palette
- Always two-pass: generate a palette specific to this clip (diff stats), then encode with Bayer dithering scale 5 and rectangle diff mode (updates only changed regions). Single-pass generic palettes muddy subtle palettes (beige + orange). Bayer dithering is smoother than none for fades at slightly larger size.

## 569. Music add-on behavior
- Trim music to video length; 0.3s fade-in + 1s fade-out; copy video stream without re-encode; audio AAC 192k.

## 570. Pre-flight checklist
- Runs end-to-end with no errors; frame 0 is the full initial state (not an empty loading state); last frame is a stable end state; fonts/images/emoji render; duration setting matches the animation; looping disabled while recording; final element does not fade out on the last frame; required small watermark present (bottom 24px / right 32px, 11px mono, 0.15em tracking, rgba(0,0,0,0.4) on light, rgba(255,255,255,0.35) on dark; prefix "Unofficial · " for third-party brand work).

## 571. Delivery note
- Provide a table of file / format / specs / size and note how 60fps was produced (duplication by default; interpolated versions flagged; true 60fps via seek render) and that GIFs are palette-optimized. Offer other sizes/frame rates.

## 572. Follow-up requests
- Too large: MP4 CRF 23–28; GIF to 600 wide or 10fps.
- GIF blurry: 1280 wide, or offer MP4 instead.
- Vertical 9:16: re-render at 1080×1920 from source.
- Watermark: text overlay or PNG overlay.
- Transparent background: MP4 has no alpha — use WebM VP9 with alpha, APNG, ProRes 4444 MOV (yuva444p12le, keeps soft shadows semi-transparent; ~15MB per 4s; for editing handoff), WebM (smaller, for transfer), or RGBA PNG sequence for compositing; set page background transparent with no base color.
- Lossless: CRF 0 + veryslow preset (~10× size).

## 573. Deliverables set for launch films
- Main MP4 with audio; 60fps MP4; GIF; silent MP4 backup (for re-scoring); poster PNG of the marketing frame; design rationale document; source; shot list CSV.

---

# Part 46 — Reviewing AI-Generated Video (Checklist)

## 574. When to run automated review
- After the final 60fps render, before delivery/mixing; again after the SFX mix (onset cross-check needs an audio track); again after re-renders fixing major issues. Not at the 30fps test stage (resolution/pacing not final).
- It replaces a full manual re-watch but not frame-by-frame extraction review.
- Always provide the director's notes as context so intent can be distinguished from bugs.

## 575. Three-layer pipeline
- Objective detection first (deterministic, misses nothing): silence detection to build the SFX onset timeline (the vision model cannot hear audio); freeze detection to list fully static segments ≥3s.
- Model review per 60s segment, compressed to 1280 wide / 15fps / CRF 28 (~0.5MB per minute for flat animation), with checklist + director's notes + that segment's onsets/static segments, timestamps mapped to the original.
- Low-res full-video pass at 960 wide / 10fps for cross-segment narrative coherence, hero continuity, overall pacing.
- Merge into one report; keep per-segment raw notes and objective data in an appendix. Measured: 210s video → 6 calls, 6–10 minutes.

## 576. Review checklist
- ① Black frames / incomplete render.
- ② Text cropping / typos.
- ③ Overlapping / occluding elements.
- ④ Narrative coherence — classify every transition in the three-layer vocabulary (flash-wash, dip-to-dark, defocus-handoff, title card, whip-pan, mask-wipe; hidden cut; shared-element settle, letterform traversal); any unwrapped hard cut = bare cut, flagged important.
- ⑤ Hero continuity.
- ⑥ Pacing dead segments (objective static list + judgment: deliberate hold vs genuinely dead).
- ⑦ SFX cueing (onset vs on-screen event cross-check).
- ⑧ Unbalanced composition / empty space.

## 577. Severity levels
- Fatal = must fix before delivery; Important = noticeably impairs viewing; Suggestion = nice to have.

## 578. Known limits — judge these yourself
- Audio choice, volume, BGM mood can't be judged by a model that can't hear; check ⑦ only one-way.
- 1–2 frame flickers, subtle jitter, exact color drift, sub-pixel alignment are missed — use frame extraction.
- Transition calls skew strict: at 15fps a fast crossfade may read as a hard cut; contradictions between segment and full pass are "inconclusive" — extract frames to confirm before changing.
- "Hold vs dead" is opinion; long b-roll holds under voiceover often pass — judge when watching the film alone.
- Failed calls must be reported honestly with the uncovered time range; never fabricate results.
- Lesson: model-only dead-segment detection caught 3/14; adding freeze detection caught all. Objective detection is the floor; the model handles semantics. The model did catch inter-act transition and hero-break problems but misreported fades as hard cuts.

---

# Part 47 — Frame-Based Rendering Considerations

## 579. Determinism
- Rendering is a headless browser seeking frame by frame; every visual state must be a pure function of time.
- No wall-clock time, no unseeded randomness, no runtime network fetches; use seeded random functions.
- CSS transitions and class toggles follow the wall clock and break under seeking — convert them to time-based interpolation inside the render function.
- Derived motion signals (velocity blur, lagged layers, damped settle) and parallax must be computed from camera/time state, not independent tweens.
- Render the initial state explicitly at t=0 (update callbacks don't fire at time zero, leaving the first frame uninitialized); beware "from-to" tweens that render their start state immediately (phantom frames).

## 580. Timeline and composition structure
- Drive everything from one paused master timeline (or a proxy tween that advances t from 0 to duration linearly and calls render(t)).
- Each timed element declares start, duration, and track; root declares duration and dimensions explicitly.
- Video assets muted; audio as separate tracks (BGM/voiceover can render with the film or be mixed afterward).
- Fix the page to the canvas size (e.g., 1920×1080); remove resize/fit logic, replay buttons, and self-running loops when converting live demos.

## 581. Fonts and assets
- Fonts must be fully loaded before the clock starts (or embedded deterministically at compile time); declare local system fonts explicitly.
- Use higher-resolution captures (2x full, 4x close-up slices) for zoomed content; layout-level zoom keeps 3D text sharp — per-frame relayout costs render time only, not output quality (live preview may drop frames; the render is what counts).

## 582. Validation gates before final render
- Zero errors on lint, runtime, layout, motion, and contrast audits before rendering. Contrast gate (WCAG 4.5:1) conflicts with dark cinematic styles using 16–40% opacity watermarks/decorative text — skip it only for dark cinematic work; never for light informational outputs where contrast failures are real.
- Verify outputs for audio stream presence, black frames, loudness, and duration.

## 583. Choosing a render route
- New animation projects: deterministic frame-seek pipeline (supports 3D, physics, shaders, Lottie, particles).
- Weak runtimes / single-file deliverables / interactive demos: lightweight self-contained stage; no video pipeline needed for interaction.
- Long narrated videos: the narration-timeline pipeline (dual clock, subtitles, TTS timeline) takes precedence.
- Batch parametrized videos: a template-driven programmatic video tool.
- Design language (narrative structure, easing system, dual-track audio) always governs; the renderer is only an implementation tool.

## 584. SFX cue tables
- Keep cues as a three-column table (seconds / sound / volume dB); edit the table and re-run the mix (~10s per regeneration) rather than hand-editing mixes.
