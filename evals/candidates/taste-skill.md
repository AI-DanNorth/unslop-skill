# taste-skill (github.com/leonxlnx/taste-skill) — example artifacts for Unslop calibration
Shallow clone at /home/claude/refs/taste-skill (v2.5.1, single skill `design-taste-frontend`). Repo paths below are relative to that clone; S = skills/taste-skill.

| # | URL or repo path | Medium | Label | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://www.figma.com | landing | good | Named "the bar" for every build; hero fills first screen, tile-wall feature cards, dark footer | S/SKILL.md:26; S/references/layout-v4.md:12; cards.md:4 |
| 2 | https://x.ai | landing | good | Co-reference with Figma; Grok 2x2 card grid, dark cards with daylight painting behind UI | S/SKILL.md:26; S/references/cards.md:4,16 |
| 3 | https://linear.app | landing | good | Benchmark for "show the product big in one app frame" (PR list beside full-width diff) | S/references/sections-library.md:436-440; cards.md:84 |
| 4 | https://cursor.com | landing | good | Cited with Linear/Vercel for showing the real app window across the wrap | S/references/sections-library.md:436 |
| 5 | https://vercel.com | landing | good | Same "product itself, big" exemplar | S/references/sections-library.md:436 |
| 6 | https://tasteskill.dev | web page / gallery | good | Repo's own site (live, checked): gallery of coffee shop, club night, architects, contracts builds + a before/after comparison | README.md:9 |
| 7 | https://tastecode.dev | landing | neutral | Repo's companion desktop app site (TasteCode) | README.md:11,19 |
| 8 | https://github.com/Leonxlnx/taste-skill/releases/tag/v2.0.0 | video | good | "Launch film" showing skill output | README.md:76 |
| 9 | examples/v2/coffee-storefront.webp | web page (screenshot) | good | Generated coffee-shop page, drawn storefront as hero | README.md:67 |
| 10 | examples/v2/night-dates.webp | web page (screenshot) | good | Generated techno-night page, dates set into an archive photo | README.md:68 |
| 11 | examples/v2/coffee-roast.webp | web page (screenshot) | good | Coffee page section: roast in four real photographs | README.md:71 |
| 12 | examples/v2/coffee-questions.webp | web page (screenshot) | good | FAQ as stacked index cards (anti-accordion) | README.md:72 |
| 13 | examples/v2/CREDITS.md | doc-PDF | neutral | Photo provenance for the 4 examples (Wikimedia/Met), useful for "real photo" checks | README.md:76 |
| 14 | S/assets/starter.html | web page | good | The template every build starts from; passes the kit checker at 1440/390 | README.md:125; CHANGELOG.md:21 |
| 15 | S/assets/layout/hero-{split,centred,product,photo,place,collage,editorial,word,film,statement,triptych}.html (11 files) | landing (hero) | good | 11 tested hero layouts, each a full page model said to pass checker with no FAIL | README.md:127; CHANGELOG.md:21 |
| 16 | S/assets/moments/_demo/in-page.html | web page | good | Place-business page model with moments mounted in a real page | CHANGELOG.md:21 |
| 17 | S/assets/moments/_demo/in-page-service.html | web page | good | Service-business page model | CHANGELOG.md:21 |
| 18 | S/assets/moments/_demo/in-card.html | component demo | neutral | Moment inside a card | (file) |
| 19 | S/assets/moments/gallery.html + 19 `*/demo.html` | gallery | neutral | Scroll/hover moments catalogue; repo itself flags giant-type-pass, iris-opens, letters-assemble etc. as "graphic tricks" for calm pages | S/references/moments.md:28-31 |
| 20 | S/assets/moments/giant-type-pass/demo.html | component demo | slop (in context) | "A photograph inside letters reads as a template trick" on place/service pages | S/references/moments.md:30 |
| 21 | S/assets/ui/index.html, S/assets/ui/cards.html (+19 `ui/*/fragment.html`) | gallery / app screen | good | Real-product UI fragments (chat, calendar, diff-review, pipeline-board, terminal-run...) inside lit feature cards | README.md:129 |
| 22 | S/assets/components/index.html (+20 `fx-*/component.html`) | gallery | neutral | Component lab: pricing, stat, chart, map, globe, tabs, search, logos | (file) |
| 23 | S/assets/effects/gallery.html, S/assets/effects/lab.html | gallery | neutral | 28 shader grounds (grain-gradient, aurora, gradient-mesh...) reserved for tech/gaming only | README.md:130 |
| 24 | S/assets/objects/index.html (+14 `*/demo.html`) | gallery | neutral | Procedural 3D "print" objects, product render/turntable; repo warns renders without the real product read as random 3D | S/references/effects-objects.md:22-27 |
| 25 | S/assets/scenes/*/demo.html (11) | component demo | neutral | Scroll scenes (powers-of-ten, letter-physics, fixed-hero-object...) | README.md:130 |
| 26 | S/assets/diagrams/demo.html, lab.html | diagram | good | Node-and-line diagrams with real brand marks | README.md:129 |
| 27 | S/assets/icons/demo.html | gallery | neutral | Real brand/UI icon set rendering | README.md:144 |
| 28 | S/assets/backgrounds/demo.html, check.html | component demo | neutral | Background/band treatments | (file) |
| 29 | S/assets/motion/demo.html | component demo | neutral | Micro-interaction/motion tokens | (file) |
| 30 | S/assets/layout/fonts.html | component demo | neutral | Font pairing specimens dealt per page kind | (file) |
| 31 | S/assets/objects/product-render/specs/*.png, objects/print-*/fallback*.png | social card / image | neutral | Static fallback stills of 3D objects (light/dark) | (files) |
| 32 | assets/readme-tastecode.webp / -dark.webp | social card | neutral | README promo banner | README.md:21-22 |
| 33 | (described) code-review page: one small diff card centred on a sage panel | landing | slop | Scored ~3.5 pts under Linear; product shown only as fragments on coloured panels | S/references/sections-library.md:438-440; cards.md:82-84 |
| 34 | (described) cargo-bike page that never showed the bike | landing | slop | Scored 3/10; render + props read as random 3D objects | S/references/effects-objects.md:25-27; photos.md:63 |
| 35 | (described) robot arm shown as silk shader + order form; unnamed game as abstract effect | landing | slop | Effect standing in for the subject lost to pages showing the thing | S/references/effects-usage.md:43-44 |
| 36 | (described) drawn SVG arm as a robot maker's hero | landing | slop | Drawing replacing the product photo | S/references/sections-library.md:179-180 |
| 37 | (described) halftone over hero photograph | landing | slop | Read as broken/low-res at every width | S/references/effects-creative.md:120-121 |
| 38 | (described) contour pattern standing in for a map | component demo | slop | Judges marked it a fake drawing | S/references/effects-creative.md:125-126 |
| 39 | (described) card > grid-paper panel > white UI card | component demo | slop | Read as three nested boxes | S/references/cards.md:53-54 |
| 40 | (described) fintech page at 117 words/screen | landing | slop | Read as wordy (budget 60-80) | S/references/copy.md:93 |
| 41 | (described) footer with 18-20 photo credit links | web page | slop | "Credit wall" | S/references/copy.md:137; photos.md:243 |
| 42 | (described) "Names and figures on this page are examples" footer note | web page | slop | Read as an apology / placeholder tell | S/references/cards.md:305-306 |
| 43 | (described) 480x688 diff in div.hero__art cut by the fold at 820 | landing | slop | fold-card FAIL | S/references/layout-v4.md:121-122 |
| 44 | https://interfaces.dev | web page | neutral (sponsor) | Design-engineering magazine by Jakub Krehel; interactive demos (live, checked) | README.md:32-36 |
| 45 | https://reactbits.dev | gallery | neutral (sponsor) | Animated React component library (live) | README.md:40-47 |
| 46 | https://img.ly | landing | neutral (sponsor) | CreativeEditor SDK | README.md:50 |
| 47 | https://www.sent.dm | landing | neutral (sponsor) | Messaging API landing | README.md:54 |
| 48 | https://github.com/Leonxlnx/taste-skill-classics | gallery | neutral | Older skills (high-end-visual-design, minimalist-ui, brutalist) — likely more examples | README.md:158 |
| 49 | https://github.com/Leonxlnx/imagegen-skills | gallery | neutral | Image-to-code / brandkit skills | README.md:159 |

## Best audit candidates
1. https://tasteskill.dev — live gallery with a before/after pair; the single best good-vs-slop calibration source.
2. examples/v2/coffee-storefront.webp + coffee-roast + coffee-questions — one brief, three screenshots; "good" by the repo's standard, a non-tech place page.
3. examples/v2/night-dates.webp — event/nightlife page, different register for contrast.
4. https://www.figma.com — the repo's declared bar; real, human-designed control.
5. https://x.ai — second declared bar; dark-mode card grid control.
6. https://linear.app — exemplar for product-in-app-frame; pair against row 33's failed pattern.
7. S/assets/starter.html — AI-generated baseline every build starts from; tests whether Unslop flags the house template itself.
8. S/assets/layout/hero-*.html (11) — same system, 11 hero layouts; good for checking false positives and template sameness across outputs.
9. S/assets/effects/gallery.html — shader grounds (gradient-mesh, aurora, grain) that are classic AI-slop tropes when misapplied; tests context-sensitive flagging.
10. S/assets/moments/giant-type-pass/demo.html — repo-labelled "template trick"; a concrete in-repo slop specimen.

## Notes
- The repo's bad examples (rows 33-43) are described test outcomes only; no files or URLs ship for them.
- The "study of 327 sites" and "41 company sites" (layout-v4.md:16, cards.md:4) are cited without any list of URLs.
- No slide decks, emails, or PDFs exist in the repo; mediums are web pages, components, galleries and screenshots.
- icons-credits.json holds hundreds of brand homepage URLs. These are icon sources, not design exemplars, so they are excluded.
- Spot-checked live: tasteskill.dev, tastecode.dev, interfaces.dev, reactbits.dev.
