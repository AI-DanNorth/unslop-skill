# impeccable (pbakaus/impeccable): design artifacts for Unslop calibration

Impeccable is a design skill and CLI for coding agents, with 24 steering and review commands and a deterministic slop detector of 62 rules (`npx impeccable detect`). Its companion site is impeccable.style.
The repo has few curated "inspiration" links. Its artifacts are a large detector fixture suite (flag/pass pairs), two slop landing demos, README before/after images, and a real-website corpus cited in fixture comments. The site adds a with/without gallery and slop example pages.

Clone: /home/claude/refs/impeccable (shallow, 2026-11-08). Paths below are relative to that clone. Labels follow the repo's own framing: "good" means exemplar, "With Impeccable", or a should-pass case. "slop" means an anti-pattern or should-flag case. "neutral" means a detector edge case, plumbing, or docs. "pair" means one artifact that holds both a slop half and a good half.

| # | URL or repo path | Medium | Label | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://impeccable.style | landing | good | The project's own site, with a dark lacquer and kinpaku gold brand. Its inline before/after comparisons double as a reference | README.md:13 |
| 2 | https://impeccable.style/slop | gallery | slop | Catalog of all detector rules with visual specimens (gradient text, glassmorphism, nested cards, marquees) | README.npm.md:65 |
| 3 | https://impeccable.style/antipattern-examples/old-slop-2022.html | landing | slop | Full mock page of the 2022-era AI slop look | impeccable.style/slop (WebFetch) |
| 4 | https://impeccable.style/antipattern-examples/new-slop-2025.html | landing | slop | Full mock page of the 2025-era slop look (the cream and serif era) | impeccable.style/slop (WebFetch) |
| 5 | https://impeccable.style/antipattern-examples/new-slop-2026.html | landing | slop | Fictional "Lumina" page with brutalist hype copy, a ticker, fake .exe UI, three generic cards, and 01/ section labels. Verified live | impeccable.style/slop (WebFetch) |
| 6 | https://impeccable.style/antipattern-examples/purple-gradients.html | component demo | slop | Purple-to-blue gradient tell | impeccable.style/slop |
| 7 | https://impeccable.style/antipattern-examples/lazy-cool.html | component demo | slop | Lazy "cool" aesthetic defaults | impeccable.style/slop |
| 8 | https://impeccable.style/antipattern-examples/lazy-impact.html | component demo | slop | Lazy "impact" (loud, high-volume) defaults | impeccable.style/slop |
| 9 | https://impeccable.style/antipattern-examples/thick-border-cards.html | component demo | slop | Thick-border card tell | impeccable.style/slop |
| 10 | https://impeccable.style/antipattern-examples/cardocalypse.html | component demo | slop | Cards everywhere and cards nested in cards | impeccable.style/slop |
| 11 | https://impeccable.style/antipattern-examples/layout-templates.html | web page | slop | Template-layout monoculture | impeccable.style/slop |
| 12 | https://impeccable.style/antipattern-examples/inter-everywhere.html | component demo | slop | Inter used for every role | impeccable.style/slop |
| 13 | https://impeccable.style/antipattern-examples/massive-icons.html | component demo | slop | Oversized icon tiles | impeccable.style/slop |
| 14 | https://impeccable.style/antipattern-examples/bad-contrast.html | component demo | slop | Low-contrast text | impeccable.style/slop |
| 15 | https://impeccable.style/antipattern-examples/redundant-ux-writing.html | component demo | slop | Redundant UX copy | impeccable.style/slop |
| 16 | https://impeccable.style/antipattern-examples/modal-abuse.html | component demo | slop | Modal overuse | impeccable.style/slop |
| 17 | https://impeccable.style/gallery | gallery | pair | Same brief, same model: 5 "Without Impeccable" runs and 3 "With" runs per brief. Verified live | impeccable.style nav (WebFetch) |
| 18 | https://impeccable.style/gallery#09-luxury-hotel | web page | pair | Boutique hotel, without/with runs | impeccable.style/gallery |
| 19 | https://impeccable.style/gallery#02-kids-reading | landing | pair | Children's reading, without/with runs | impeccable.style/gallery |
| 20 | https://impeccable.style/gallery#03-italian-restaurant | web page | pair | Italian restaurant homepage, without/with runs | impeccable.style/gallery |
| 21 | https://impeccable.style/gallery#01-observability | landing | pair | Observability SaaS, without/with runs (dev-tool slop hot zone) | impeccable.style/gallery |
| 22 | https://impeccable.style/gallery#07-vintage-moto-forum | landing | pair | Vintage motorcycle forum, without/with runs | impeccable.style/gallery |
| 23 | https://impeccable.style/gallery#08-perp-dex | landing | pair | Perpetual exchange (crypto), without/with runs | impeccable.style/gallery |
| 24 | https://impeccable.style/gallery#21-infra-platform | landing | pair | Infrastructure platform, without/with runs | impeccable.style/gallery |
| 25 | https://impeccable.style/cases/neo-mirai | doc-PDF | good | Case study that goes from mockup to brand toolkit to shipped page. Verified live | README.md:21 |
| 26 | https://impeccable.style/neo-mirai/index.html | web page | good | The shipped Neo Mirai conference site, a real responsive build | cases/neo-mirai (WebFetch) |
| 27 | https://impeccable.style/assets/openai_image_2_hifi.jpg + /openai_image_2_brand.jpg | gallery | good | Generated hi-fi mockup and brand toolkit boards for Neo Mirai | cases/neo-mirai (WebFetch) |
| 28 | https://impeccable.style/worlds/cards (e.g. posters-covers-sleeves-fillmore-handbill.webp, broadcast-programming-teletext-service-hero.webp, archives-microfiche-reader-hero.webp) | gallery | good | "Visual world" reference boards and heroes given to the agent as style inspiration | crates/context/src/concept_seed.rs:128; crates/context/src/serve_question.rs:1238 |
| 29 | https://impeccable.style/worlds/cards/fixture-*-family-*.webp (about 30 ids) | test fixture | neutral | Test-catalog world cards (print, canon, instruments, performed, material families) | tests/fixtures/concept-catalog/concept-ingredients.json:1 |
| 30 | https://impeccable.style/docs, /cheatsheet, /docs/new-work, /tutorials/critique-with-overlay, /research | doc-PDF | neutral | Docs site, an editorial-style reading surface | README.md:13, docs/CLI-CONTRACT.md:485 |
| 31 | docs/images/readme-without.webp | web page | slop | Villa Castagneto built without Impeccable: cream page, thin serif with italic accent, pill buttons, flat vector cards | README.md:17 |
| 32 | docs/images/readme-with.webp | web page | good | Same brief with Impeccable: full-bleed engraved night scene, condensed cream and vermilion headline, month strip | README.md:17 |
| 33 | demos/landing-demo/index.html | landing | slop | "Lumina": the Fraunces cream-peach SaaS template, which its own PRODUCT.md calls "itself an example" | demos/landing-demo/PRODUCT.md:23 |
| 34 | demos/landing-demo/classic/index.html | landing | slop | "Lumina" classic: #0a0a14 ground, Inter, purple/violet/pink/cyan tokens, the 2023-24 AI dark-gradient look | demos/landing-demo/classic/index.html:10 |
| 35 | demos/landing-demo/PRODUCT.md + DESIGN.md | doc-PDF | neutral | Brief with explicit anti-references (three-icon tiles, hero superlatives, soft-everything) | demos/landing-demo/PRODUCT.md:21 |
| 36 | tests/fixtures/antipatterns/should-flag.html | test fixture | slop | Kitchen-sink page of anti-patterns the detector must flag | tests/fixtures/antipatterns/should-flag.html:1 |
| 37 | tests/fixtures/antipatterns/should-pass.html | test fixture | good | Clean counterpart that must not flag | tests/fixtures/antipatterns/should-pass.html:1 |
| 38 | tests/fixtures/antipatterns/gpt-tells.html | test fixture | slop | "Recurring generated-UI tell fixture" | tests/fixtures/antipatterns/gpt-tells.html:1 |
| 39 | tests/fixtures/antipatterns/gpt-thin-border-wide-shadow.html | test fixture | slop | GPT signature: hairline border plus wide soft shadow | tests/fixtures/antipatterns/gpt-thin-border-wide-shadow.html:1 |
| 40 | tests/fixtures/antipatterns/ai-color-palette*.html (6 files) | test fixture | pair | AI palette (purple/violet/teal gradients) flag vs pass, including brand-hue and code-token exceptions | tests/fixtures/antipatterns/ai-color-palette.html:1 |
| 41 | tests/fixtures/antipatterns/cream-palette.html + cream-palette-tailwind.html | test fixture | slop | Warm-cream surface tell | tests/fixtures/antipatterns/cream-palette.html:1 |
| 42 | tests/fixtures/antipatterns/typography.html, typography-should-flag/pass.html | test fixture | pair | Typography anti-patterns side by side with "Good Typography" | tests/fixtures/antipatterns/typography.html:1 |
| 43 | tests/fixtures/antipatterns/overused-font*.html (5 files) | test fixture | pair | Inter and other reflex fonts, including the share-flag/pass and never-loaded cases | tests/fixtures/antipatterns/overused-font.html:1 |
| 44 | tests/fixtures/antipatterns/color.html | test fixture | pair | Color anti-patterns ("Welcome to Our Platform" in gray, purple headings) | tests/fixtures/antipatterns/color.html:1 |
| 45 | tests/fixtures/antipatterns/layout.html | test fixture | pair | Layout anti-patterns flag vs pass | tests/fixtures/antipatterns/layout.html:1 |
| 46 | tests/fixtures/antipatterns/motion.html + bounce-easing-*.html + scroll-reveal.html | test fixture | pair | Motion tells: bounce easing, scroll reveal | tests/fixtures/antipatterns/motion.html:1 |
| 47 | tests/fixtures/antipatterns/quality.html | test fixture | pair | Typography and readability quality flags | tests/fixtures/antipatterns/quality.html:1 |
| 48 | tests/fixtures/antipatterns/nested-cards*.html (5 files) | test fixture | pair | Cards in cards, with the mockup, composer, and page-frame exceptions | tests/fixtures/antipatterns/nested-cards.html:1 |
| 49 | tests/fixtures/antipatterns/icon-tile-stack.html + icon-tile-card-title.html | test fixture | slop | Rounded-square icon tile above every heading, including the shadcn CardTitle div form | tests/fixtures/antipatterns/icon-tile-card-title.html:7 |
| 50 | tests/fixtures/antipatterns/hero-eyebrow-chip.html + eyebrow-hand-off.html | test fixture | pair | Pill eyebrow chip above the hero H1 | tests/fixtures/antipatterns/hero-eyebrow-chip.html:1 |
| 51 | tests/fixtures/antipatterns/kicker-above-heading*.html | test fixture | pair | Tracked-caps kicker above headings | tests/fixtures/antipatterns/kicker-above-heading.html:1 |
| 52 | tests/fixtures/antipatterns/italic-serif-display.html | test fixture | pair | Italic serif display accent (the "Fraunces italic" tell) | tests/fixtures/antipatterns/italic-serif-display.html:1 |
| 53 | tests/fixtures/antipatterns/glow.html + radial-spotlight-glow.html + dark-gradient-ground.html | test fixture | pair | Dark glow, radial spotlight, gradient ground | tests/fixtures/antipatterns/glow.html:1 |
| 54 | tests/fixtures/antipatterns/gradient-text-*.html | test fixture | pair | Gradient text, with the shimmer-state and one-colour-ramp exceptions | tests/fixtures/antipatterns/gradient-text-states.html:6 |
| 55 | tests/fixtures/antipatterns/numbered-section-labels.html + numbered-section-markers.html | test fixture | slop | "01 /" decorative section numbering | tests/fixtures/antipatterns/numbered-section-labels.html:1 |
| 56 | tests/fixtures/antipatterns/side-accent-*.{css,html,jsx,tsx,vue,svelte,scss,sass} + side-tab-*.html + pseudo-stripe.* + border-accent-blank-lines.css + stripe-child.* | test fixture | slop | Colored left-border accent card tell, across frameworks | tests/fixtures/antipatterns/side-accent-producers.html:1 |
| 57 | tests/fixtures/antipatterns/em-dash-*.html (8 files) | test fixture | pair | Em-dash copy tell vs legitimate list and matrix uses | tests/fixtures/antipatterns/em-dash-list-separators.html:9 |
| 58 | tests/fixtures/antipatterns/marquee-ornament.html, pulsing-dot*.html, blinking-cursor.html | test fixture | pair | Ornamental motion tells (marquee, pulsing dot, typing cursor) | tests/fixtures/antipatterns/pulsing-dot-floats-and-bars.html:4 |
| 59 | tests/fixtures/antipatterns/shape-assembled-illustration.html + organic-clip-path.html | test fixture | pair | CSS-shape fake illustrations and blob clip-paths | tests/fixtures/antipatterns/shape-assembled-illustration.html:1 |
| 60 | tests/fixtures/antipatterns/hard-offset-shadow.html + tests/fixtures/hard-offset-shadow/*.html | test fixture | slop | Neo-brutalist hard offset shadow | tests/fixtures/hard-offset-shadow/colors.html:1 |
| 61 | tests/fixtures/antipatterns/mockup-structure.html + declared-mockups.html | test fixture | neutral | When product mockups or browser frames count as content (cites real sites) | tests/fixtures/antipatterns/mockup-structure.html:151 |
| 62 | tests/fixtures/antipatterns/low-contrast-*.html + *-contrast*.html (about 30 files) | test fixture | pair | Contrast flag vs pass edge cases (heavy faces, disabled controls, scrims) | tests/fixtures/antipatterns/low-contrast-resting-states.html:11 |
| 63 | tests/fixtures/antipatterns/cramped-padding*.html, flush-against-border.html, edge-flush-cards*.html | test fixture | pair | Cramped padding and flush-edge cases | tests/fixtures/antipatterns/cramped-padding-edges.html:70 |
| 64 | tests/fixtures/antipatterns/flat-type-hierarchy*.html, heading-rhythm*.html, oversized-h1*.html, skipped-heading-*.html, unbalanced-heading.html, straggler*.html | test fixture | pair | Type hierarchy and rhythm rules | tests/fixtures/antipatterns/heading-rhythm.html:58 |
| 65 | tests/fixtures/antipatterns/(remaining ~120 rule fixtures: line-length, tight-leading, wide-tracking, all-caps-body, justified-text, tiny/small/undersized text, text-overflow, first-viewport overflow, fullpage-screenshot, script-error, not-at-rest, painted/never-painted, etc.) | test fixture | pair | Rest of the 62-rule regression suite, mostly isolated flag/pass rows | tests/fixtures/antipatterns/ |
| 66 | tests/fixtures/antipatterns/framework-next-cssinjs/, framework-next-modules/, framework-next-tailwind/, framework-vite/, multifile/ | test fixture | slop | Slop components in real project shapes (Hero, FeatureGrid, Testimonials, PricingCard, StatsCard, Sidebar) | tests/fixtures/antipatterns/framework-next-cssinjs/components/Hero.tsx:1 |
| 67 | tests/fixtures/antipatterns/{jsx,vue,svelte,cssinjs,css-in-prose}-should-{flag,pass}.* | test fixture | pair | Same tells across frameworks and source syntaxes | tests/fixtures/antipatterns/jsx-should-flag.jsx:1 |
| 68 | tests/fixtures/consent/*.html (51 files) | test fixture | neutral | Cookie walls and banners shaped after real CMPs (OneTrust, Cookiebot, Tealium, Transcend) | tests/fixtures/consent/tealium.html:9 |
| 69 | tests/fixtures/overlays/*.html (26 files) | test fixture | neutral | Preloaders, splash intros, age gates, tours, Lovable badge, shaped after real sites | tests/fixtures/overlays/lovable-badge.html:9 |
| 70 | tests/fixtures/extension-scan/flagged.html + clean.html | test fixture | pair | Minimal flagged/clean pages for the Chrome extension | tests/fixtures/extension-scan/README.md:4 |
| 71 | tests/fixtures/validity/press-and-hold*.html | test fixture | neutral | Bot challenge (press-and-hold iframe) as on target.com | tests/fixtures/validity/press-and-hold.html:11 |
| 72 | tests/framework-fixtures/* (39 projects, e.g. vite8-react-pricing-cards, -modal, -tabs, nextjs-app-router, sveltekit) | test fixture | neutral | Small live-mode app shells across frameworks | tests/framework-fixtures/README.md:1 |
| 73 | tests/oracle/workspaces/* (33 workspaces, e.g. live-html, ctx-full Hero.astro, hook-project Card.tsx) | test fixture | neutral | Engine oracle projects; hook-project has Card.tsx (flag) vs Clean.tsx | tests/oracle/workspaces/hook-project/src/components/Card.tsx:1 |
| 74 | tests/oracle/workspaces/comp-basic/{comp,build}.png, comp-responsive/*.png, crates/comp/tests/fixtures/hero_{comp,build}_crop.png | test fixture | neutral | Comp vs build fidelity image pairs (mockup vs implementation) | docs/COMP-FIDELITY.md:1 |
| 75 | ui/component-review/ (theme.css, kinpaku-kit.css) | app screen | good | Impeccable's own review UI in its kinpaku design language | ui/component-review/README.md:1 |
| 76 | extension/popup/popup.html | app screen | neutral | Chrome extension popup UI | extension/popup/popup.html:1 |
| 77 | DESIGN.md (root) | doc-PDF | good | The repo's own design system spec: dark urushi lacquer, gold-leaf seams, verdigris | DESIGN.md:257 |
| 78 | Eye Magazine (eyemagazine.com) | web page | good | Named editorial reference for the brand ("design publication, not SaaS landing") | PRODUCT.md:59 |
| 79 | It's Nice That (itsnicethat.com) | web page | good | Named editorial reference | PRODUCT.md:59 |
| 80 | A List Apart (alistapart.com) | web page | good | Named editorial reference | PRODUCT.md:59 |
| 81 | https://kin-ai.replit.app | landing | slop | Twenty shadcn feature cards with bg-primary/10 icon tiles, the source of the icon-tile rule | tests/fixtures/antipatterns/icon-tile-card-title.html:9 |
| 82 | https://v0-optimus-delta.vercel.app | landing | slop | v0-built page: "99.99%" stats collide at 390px (FLAG) | tests/fixtures/antipatterns/text-overflow.html:171 |
| 83 | https://v0-compute-11.vercel.app | landing | neutral | v0-built page, nowrap headline edge case (PASS) | tests/fixtures/antipatterns/text-overflow.html:281 |
| 84 | https://articulation-hub.vercel.app | landing | neutral | Teal CTA gradient that fades only to 0.8 (palette pass), plus an intro overlay | tests/fixtures/antipatterns/ai-color-palette.html:151 |
| 85 | https://gameghost.manus.space | landing | neutral | Manus-built page: Tailwind shadow-lg purple glow on black (dark-glow edge case) | tests/fixtures/antipatterns/paint-that-shows.html:19 |
| 86 | https://mialight.app | landing | neutral | Lovable-built site with the "Edit with Lovable" badge (overlay pass) | tests/fixtures/overlays/lovable-badge.html:9 |
| 87 | https://cursorhelper.vercel.app | landing | neutral | Glow-backed fake app window in a card (mockup advisory) | tests/fixtures/antipatterns/nested-cards-mockups.html:146 |
| 88 | https://stroq.dev | landing | neutral | Terminal-window mockup nested in a section card; mono labels | tests/fixtures/antipatterns/nested-cards-mockups.html:118 |
| 89 | https://getpaidlens.com | landing | neutral | Dashboard mockup panel with an "Illustrative example" caption | tests/fixtures/antipatterns/nested-cards-mockups.html:136 |
| 90 | https://maritime.sh | landing | neutral | Scaled app-window mockup in a card | tests/fixtures/antipatterns/nested-cards-mockups.html:126 |
| 91 | https://cochat.ai | landing | neutral | Headline "gradient" with one-colour stops (not gradient text) | tests/fixtures/antipatterns/gradient-text-one-colour.html:8 |
| 92 | https://vestra.ai | landing | neutral | 6%-alpha gradient-text watermark | tests/fixtures/antipatterns/paint-that-shows.html:14 |
| 93 | https://looot.ai | landing | neutral | Recoleta declared but never loaded; blinking-eye animation | tests/fixtures/antipatterns/overused-font-never-loaded.html:8 |
| 94 | https://nitrostack.ai | landing | neutral | Highlighted code sample, palette exception | tests/fixtures/antipatterns/ai-color-palette-code-tokens.html:7 |
| 95 | https://coachcall.ai | landing | neutral | 9px chat timestamps, "Popular" badge overflow | tests/fixtures/antipatterns/small-text-labels.html:14 |
| 96 | https://tirionai.com | landing | neutral | Cinematic intro overlay (div.cine-intro) | tests/fixtures/overlays/intro-clears.html:13 |
| 97 | https://noteforge.co | landing | neutral | Fixed black splash layer | tests/fixtures/overlays/splash.html:11 |
| 98 | https://ascenix.co, https://overmindlab.ai, https://zcad.ai, https://imageto3d.studio, https://adant.ai, https://quoin.ai, https://uncoverroads.com, https://redoubt.agency, https://outreign.io, https://cronwatch.dev, https://usedefinite.com, https://coldtea.ai, https://karmaboard.app, https://suitemigration.com, https://mymanagment.net, https://improved-rotary-phone-two.vercel.app, https://leilonozap.vercel.app, https://s-1.vercel.app | landing | neutral | Corpus of small AI-era startup sites used for detector edge cases (typing indicators, pulsing dots, chips, mockups) | tests/fixtures/antipatterns/evidence-after-scan.html:14 (and others, see Notes) |
| 99 | https://stripe.com | landing | good | Run-in heading and unlabeled uptime bars cited as legitimate (PASS) | tests/fixtures/antipatterns/heading-rhythm.html:58; shape-assembled-illustration.html:167 |
| 100 | https://linear.app | landing | neutral | Box labelled as a screenshot, reported as advisory | tests/fixtures/antipatterns/declared-mockups.html:131 |
| 101 | https://framer.com | landing | neutral | aria-hidden logo-marquee duplicate; animation start values | tests/fixtures/antipatterns/declared-mockups.html:101 |
| 102 | https://apple.com | landing | neutral | Gallery panel layering; footnote-marker straggler ("audio.4") | tests/fixtures/antipatterns/low-contrast-covered-and-masked.html:8 |
| 103 | https://arc.net | landing | neutral | Masked mobile frame; opacity-dimmed resting nav states | tests/fixtures/antipatterns/low-contrast-resting-states.html:11 |
| 104 | https://raycast.com, https://ramp.com | landing | neutral | Opacity-revealed resting states (contrast edge cases) | tests/fixtures/antipatterns/low-contrast-resting-states.html:30 |
| 105 | https://resend.com | landing | neutral | One-colour alpha sheen on headings, reported as advisory gradient text | tests/fixtures/antipatterns/gradient-text-states.html:11 |
| 106 | https://cursor.com | app screen | good | "Working" shimmer label, a state rather than gradient text (pass) | tests/fixtures/antipatterns/gradient-text-states.html:7 |
| 107 | https://mercury.com | landing | good | Heavy p-0 spacing resets are not monotonous spacing (PASS) | tests/fixtures/antipatterns/monotonous-spacing-resets.html:8 |
| 108 | https://panic.com | landing | neutral | Chevrons painted over half-width ground | tests/fixtures/antipatterns/low-contrast-paint-grounds.html:12 |
| 109 | https://vercel.com | landing | neutral | Three-line clamp hides a straggler | tests/fixtures/antipatterns/straggler-clamped.html:9 |
| 110 | https://theguardian.com | web page | neutral | Most-viewed list dividers (cramped-padding edge case) | tests/fixtures/antipatterns/cramped-padding-dividers.html:9 |
| 111 | Enterprise and international corpus: bankofamerica.com, americanexpress.com, chase.com, jpmorganchase.com, citigroup.com, fanniemae.com, freddiemac.com, cvs.com, centene.com, cencora.com, hp.com, verizon.com, target.com, valero.com, exxonmobil.com, phillips66.com, telekom.de, otto.de, hse.de, cnnbrasil.com.br, kinghost.com.br, lance.com.br, inven.co.kr, gseek.kr, gamer.com.tw, walla.co.il, agora.co.il, midilibre.fr, cuisineactuelle.fr, letour.fr, people.com.cn, co-trip.jp, directus.io | web page | neutral | Non-AI real-world corpus that keeps the detector from flagging normal enterprise and news design | tests/fixtures/antipatterns/cramped-padding-edges.html:82 (and others) |

## Best audit candidates

1. **demos/landing-demo/index.html**: a complete page in the "Fraunces cream-peach SaaS template", and the repo itself calls it slop. Ideal positive control for the 2025-era look.
2. **demos/landing-demo/classic/index.html**: the same product in the older dark #0a0a14, Inter, purple/pink/cyan look. Pairs with #1 to show that Unslop catches both eras.
3. **docs/images/readme-without.webp vs readme-with.webp**: a same-brief, same-model before/after for an image-based audit. A clean binary label.
4. **impeccable.style/gallery** (7 briefs × 5 without + 3 with runs): the best paired calibration set for measuring Unslop's discrimination across domains (hotel, restaurant, kids, crypto, infra, observability).
5. **impeccable.style/antipattern-examples/new-slop-2026.html**: a full mock page of the newest brutalist-hype slop (ticker, fake .exe, CTA stacking, 01/ labels). Verified live.
6. **antipattern-examples/old-slop-2022.html + new-slop-2025.html**: an era series to check that rules aren't overfit to one fashion.
7. **tests/fixtures/antipatterns/should-flag.html + should-pass.html**: a compact ground-truth pair for regression-testing rule precision and recall.
8. **https://kin-ai.replit.app**: a real, uncontrived vibe-coded shadcn landing page that triggers the icon-tile tell.
9. **https://impeccable.style/neo-mirai/index.html**: a "good" control. It was built with the tool from a comp, so it checks for false positives on an intentional, distinctive page.
10. **https://v0-optimus-delta.vercel.app** (with https://gameghost.manus.space): real v0- and Manus-generated sites for in-the-wild slop beyond the curated fixtures.

## Notes

- The repo contains almost no curated "inspiration" URLs. Real-site mentions sit in fixture comments taken from a detector observation corpus ("observations-1006/1010", "corpus run"). Most are edge cases (PASS or advisory), not design verdicts. Labels above follow that framing.
- The 296 antipattern fixtures are grouped by rule family in rows 36-67 instead of one row per file. List them all with `git -C /home/claude/refs/impeccable ls-files tests/fixtures/antipatterns`.
- The gallery and the /slop example pages are on impeccable.style only, not in the repo (the site source isn't in this repo). They were found and spot-checked with WebFetch (5 fetches: /, /slop, /gallery, /cases/neo-mirai, new-slop-2026).
- A real-site row's label says how the fixture treats that site, not whether the whole site is slop. Re-judge with Unslop before using these as ground truth.
- impeccable.style/worlds/cards boards are inspiration images given to the agent ("style inspiration only, never to copy layout"). They suit "good reference" calibration, but they are not full pages.
