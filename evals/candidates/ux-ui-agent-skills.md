# ux-ui-agent-skills (plugin87/ux-ui-agent-skills, v3.0.0): real design artifacts for Unslop calibration
Clone: /home/claude/refs/ux-ui-agent-skills. Live demo: https://plugin87.github.io/ux-ui-agent-skills/ (spot-checked: index and /terminal/ both fetched). Repo paths are relative to the clone; every `examples/*` page is also at `<live demo>/<path minus "examples/">`.

| # | URL or repo path | Medium | Label | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://plugin87.github.io/ux-ui-agent-skills/ (examples/index.html) | gallery | good | Repo's own demo index: 56 pages, with a slop-vs-kit before/after slider | README.md:60 |
| 2 | tests/fixtures/bad/slop-screen.html | test fixture | slop | Canonical "AI default" dashboard: indigo-purple gradient, emoji in h1, 4 equal cards, blue Delete; 10 gates reject it | README.md:119; tests/meta/browser-gates.test.mjs:223 |
| 3 | .github/images/before-slop.png | test fixture | slop | Screenshot of #2 used as the README "Statistical defaults" exhibit | README.md:113 |
| 4 | examples/thumbs/compare-slop.png + compare-kit.png | gallery | slop / good | Matched 1280x500 pair (slop-screen vs sample-app) for the demo slider | scripts/screenshot_docs.mjs:98 |
| 5 | examples/sample-app/preview.html | app screen | good | "Built to the rules" twin of #2: one hero metric, red Delete, light/dark | README.md:87, 114 |
| 6 | examples/sample-app/Settings.tsx (+ Dashboard.tsx, StatCard.tsx) | app screen | neutral | React source of reference app; once shipped a blue Delete that the HTML twin did not | README.md:420 |
| 7 | tests/fixtures/bad/indigo-gradient.html | test fixture | slop | "Generated-looking hero": hardcoded indigo gradient, slop_tells HIGH | tests/meta/browser-gates.test.mjs:172 |
| 8 | tests/fixtures/bad/one-sided-border.html | test fixture | slop | Four callouts with the tinted one-side accent bar (house-banned cliche) | tests/meta/owner-rules.test.mjs:90 |
| 9 | tests/fixtures/bad/emoji.html | test fixture | slop | Emoji used as icons/decoration | tests/meta/python-gates.test.mjs:17 |
| 10 | tests/fixtures/bad/bold-body.html | test fixture | slop | No display type: heading is just bolder body (fails 2.5x scale rule) | tests/meta/browser-gates.test.mjs:176 |
| 11 | tests/fixtures/bad/blue-delete.html | test fixture | slop | Destructive action wearing primary blue (token-by-intent) | tests/meta/browser-gates.test.mjs:60 |
| 12 | tests/fixtures/bad/low-contrast.html | test fixture | slop | Grey-on-white body text below AA | tests/meta/browser-gates.test.mjs:25 |
| 13 | tests/fixtures/bad/oklch.html | test fixture | slop | Low contrast hidden inside oklch() colours | tests/meta/browser-gates.test.mjs:31 |
| 14 | tests/fixtures/bad/hover-fail.html | test fixture | slop | Passes at rest, fails contrast on hover | tests/meta/browser-gates.test.mjs:47 |
| 15 | tests/fixtures/bad/unlabelled.html | test fixture | slop | Icon button with no accessible name | tests/meta/browser-gates.test.mjs:52 |
| 16 | tests/fixtures/bad/tiny-target.html | test fixture | slop | Sub-24px tap target (WCAG 2.5.8) | tests/meta/browser-gates.test.mjs:56 |
| 17 | tests/fixtures/bad/overflow-280.html | test fixture | slop | Horizontal overflow at 280px | tests/meta/browser-gates.test.mjs:64 |
| 18 | tests/fixtures/bad/fold-hinge.html | test fixture | slop | Fold-aware layout that puts content on the iPhone Duo hinge | tests/meta/browser-gates.test.mjs:70 |
| 19 | tests/fixtures/bad/dead-key-toggle.html | test fixture | slop | Toggle that works by mouse only | tests/meta/browser-gates.test.mjs:92 |
| 20 | tests/fixtures/bad/div-button-no-tabindex.html | test fixture | slop | role=button div unreachable by keyboard | tests/meta/browser-gates.test.mjs:100 |
| 21 | tests/fixtures/bad/spacing.html | test fixture | slop | Unequal card heights, touching controls | tests/meta/browser-gates.test.mjs:104 |
| 22 | tests/fixtures/bad/thai.html | test fixture | slop | Thai leading too tight, compounds split at line end | tests/meta/browser-gates.test.mjs:116 |
| 23 | tests/fixtures/bad/clipped.html | test fixture | slop | Silently clipped text | tests/meta/browser-gates.test.mjs:130 |
| 24 | tests/fixtures/bad/motion-reveal.html | test fixture | slop | Content only revealed by entrance animation (lost under reduced motion) | tests/meta/browser-gates.test.mjs:134 |
| 25 | tests/fixtures/bad/leaky-modal.html | test fixture | slop | Modal with no focus trap | tests/meta/browser-gates.test.mjs:159 |
| 26 | tests/fixtures/bad/fake-sort.html | test fixture | slop | Sort header draws aria-sort chevron, sorts nothing | tests/meta/browser-gates.test.mjs:164 |
| 27 | tests/fixtures/bad/physical-margin.html | test fixture | slop | Physical offsets that do not mirror in RTL | tests/meta/browser-gates.test.mjs:168 |
| 28 | tests/fixtures/bad/desktop-first.html | test fixture | slop | Desktop-first CSS with mobile patched via max-width | tests/meta/mobile-first.test.mjs:36 |
| 29 | tests/fixtures/bad/economy/hero-fills-screen.html | test fixture | slop | Hero eats the whole first screen | tests/meta/screen-economy.test.mjs:24 |
| 30 | tests/fixtures/bad/economy/first-screen-is-all-image.html | test fixture | slop | Nothing to read or do above the fold | tests/meta/screen-economy.test.mjs:24 |
| 31 | tests/fixtures/bad/economy/hollow-box.html | test fixture | slop | Large box carrying almost nothing | tests/meta/screen-economy.test.mjs:24 |
| 32 | tests/fixtures/bad/economy/infinite-spinner.html | test fixture | slop | Decoration that animates forever | tests/meta/screen-economy.test.mjs:24 |
| 33 | tests/fixtures/bad/economy/image-wider-than-viewport.html + unsized-eager-image.html | test fixture | slop | Overwide image; unsized eager image below fold (CLS) | tests/meta/screen-economy.test.mjs:24 |
| 34 | tests/fixtures/bad/hardcoded.css, theme-refs/, low-contrast-tokens.json, unresolved-alias.json | test fixture | slop | Non-visual token/CSS defects (hardcoded hex/px, broken var refs) | tests/meta/python-gates.test.mjs:58-92 |
| 35 | tests/fixtures/critic/dashboard-no-lead.html ("Team overview") | test fixture | slop | Seeded taste defects D1-D3: no focal point, page doesn't end, marketing filler; passes all 52 gates | evals/critic-answer-key.json; README.md:450 |
| 36 | tests/fixtures/critic/empty-state-floating.html ("Reports") | test fixture | slop | D4-D6: floating empty state, no way forward, fake label; passes all gates | evals/critic-answer-key.json |
| 37 | tests/fixtures/critic/list-identical.html ("Welcome") | test fixture | slop | D7-D10: 40 identical cards, hidden overflow, scaffolding shipped, generic display type | evals/critic-answer-key.json |
| 38 | tests/fixtures/critic/async-lies.html ("Projects") | test fixture | slop | D11-D14: loading reuses disabled, toast lies, two primaries, three equal plans | evals/critic-answer-key.json |
| 39 | tests/fixtures/good/clean-panel.html, clean.html | test fixture | good | Passing counterparts used as negative controls | tests/meta/browser-gates.test.mjs:20 |
| 40 | tests/fixtures/good/{oklch,fold-aware,spacing,thai,trapped-modal,skeleton-respects-reduce,mobile-first}.html | test fixture | good | Paired "done right" versions of #13, #18, #21, #22, #25, #24, #28 | tests/meta/browser-gates.test.mjs:38-210 |
| 41 | evals/out/blind-2026-08-25/billing-settings/index.html ("Acme Studio") | app screen | neutral | Cold-start agent output: 14/14 gates but /critique verdict "rework" | README.md:152-185 |
| 42 | evals/out/blind-2026-08-25/first-run-empty/{empty,one-project,forty-projects}.html | app screen | neutral | Blind agent empty states; critic: empty state reads as failed load, toast lies | README.md:172-178 |
| 43 | evals/out/billing-settings/index.html ("Northwind") | app screen | neutral | In-session (contaminated) eval output, 8/13 then 14/14 | evals/RESULTS.md:8 |
| 44 | evals/out/first-run-empty/{empty,one-project,many-projects}.html | app screen | neutral | In-session empty/one/many states | evals/RESULTS.md:9 |
| 45 | evals/out/data-density/index.html ("Orders") | dashboard | neutral | Dense table eval; had a sort header that sorted nothing | evals/RESULTS.md:10 |
| 46 | evals/out/notification-center/index.html | app screen | neutral | Notification eval output; 4.24:1 unread-row contrast fail on first pass | evals/RESULTS.md:11 |
| 47 | examples/showcase/index.html ("Atlas revenue console") | dashboard | good | Hero metric at 3x body, three differently shaped breakdowns, real sort | README.md:79-83 |
| 48 | examples/terminal/index.html ("Meridian Terminal") | dashboard | good | Density test: 10 inline-SVG chart types, no chart lib | README.md:72-76 |
| 49 | examples/templates/checkout.html (Northfield Supply) | app screen | good | E-commerce checkout screen | examples/index.html:373 |
| 50 | examples/templates/crm.html (Cadence CRM pipeline) | app screen | good | CRM pipeline/kanban | examples/index.html:376 |
| 51 | examples/templates/daw.html (Verge Audio) | app screen | good | Audio workstation session UI | examples/index.html:379 |
| 52 | examples/templates/tracing.html (Lumen Observability) | dashboard | good | Distributed-trace waterfall | examples/index.html:382 |
| 53 | examples/templates/orbital.html (Aurora Constellation) | dashboard | good | Satellite ops console | examples/index.html:385 |
| 54 | examples/templates/logistics.html (Vantage Freight) | dashboard | good | Shipment control | examples/index.html:388 |
| 55 | examples/templates/soc.html (Ravenline SOC) | dashboard | good | Security operations center | examples/index.html:391 |
| 56 | examples/templates/mes.html (Kirkwall Manufacturing) | dashboard | good | Factory line MES | examples/index.html:394 |
| 57 | examples/templates/rail.html (corridor control) | dashboard | good | Rail traffic control | examples/index.html:397 |
| 58 | examples/templates/trial.html (Northfield Oncology) | dashboard | good | Clinical-trial readout | examples/index.html:400 |
| 59 | examples/templates/banking.html (Harbor Bank) | app screen | good | Consumer banking accounts | examples/index.html:403 |
| 60 | examples/templates/emr.html (Meridian Health) | app screen | good | Patient chart / EMR | examples/index.html:406 |
| 61 | examples/templates/atc.html (Nordvik Control) | dashboard | good | Air-traffic approach sector | examples/index.html:409 |
| 62 | examples/templates/grid.html (Nordkraft TSO) | dashboard | good | Power-grid control | examples/index.html:412 |
| 63 | examples/templates/genomics.html (Helix) | app screen | good | Variant table for BRCA2 | examples/index.html:415 |
| 64 | examples/templates/editor.html (Harbour Cut) | app screen | good | Video editor timeline | examples/index.html:418 |
| 65 | examples/templates/warehouse.html (Brightpath) | dashboard | good | Fulfilment floor control | examples/index.html:421 |
| 66 | examples/templates/dispatch.html (Meridian Mobility) | dashboard | good | Fleet dispatch | examples/index.html:424 |
| 67 | examples/templates/training.html (atlas-7b-sft) | dashboard | good | ML training-run console | examples/index.html:427 |
| 68 | examples/templates/weather.html (Aldren Head) | dashboard | good | Forecast desk | examples/index.html:430 |
| 69 | examples/sites/launch/index.html ("Plinth by Nordun") | landing | good | Product-launch marketing page | examples/index.html:347 |
| 70 | examples/sites/store/index.html + product.html ("Pellwood") | web page | good | Furniture shop listing + product detail | examples/index.html:350 |
| 71 | examples/sites/journal/index.html | web page | good | Thai long-form editorial with self-hosted Thai fonts | examples/index.html:353 |
| 72 | examples/sites/local/index.html ("Ton Makham") | web page | good | Local restaurant site | examples/index.html:356 |
| 73 | examples/sites/gov/index.html | web page | good | Thai public-service licence renewal page (fictional) | examples/index.html:359 |
| 74 | examples/apple-demo/index.html | landing | good | Apple-direction page generated from library/apple/DESIGN.md | examples/index.html:457 |
| 75 | examples/brandkit-demo/index.html | design system | good | Generated brand foundation, verified | examples/index.html:458 |
| 76 | examples/foldable/index.html | component demo | good | iPhone Duo five-viewport simulator | examples/index.html:460 |
| 77 | examples/component-states/*.html (23 harnesses: button, input, form-controls, select, search, datepicker, fileupload, modal, drawer, command-palette, context-menu, overlays, tabs, navigation, app-shell, card, data-table, data-display, charts, feedback, toast, misc, edge-cases) | component demo | good | Every component in all 8 states, light/dark | examples/index.html:445 |
| 78 | examples/golden/ (Button.tsx, Modal.tsx, components.css) | component demo | good | Golden reference components | examples/golden/README.md:1 |
| 79 | .github/social/card.html | web page | neutral | Social preview card source | .github/social/card.html:1 |
| 80 | design-systems/library/ (2,144 DESIGN.md; 2,087 "measured from the live site") | design system | neutral | Per-brand specs with measured tokens; each names its live domain | README.md:9; design-systems/catalog.md:10 |
| 81 | https://linear.app | landing | good | Archetype "High-End Agency" kin | taste/aesthetic-systems.md:33; library.json:1047 |
| 82 | https://www.apple.com | landing | good | Same archetype; cinematic product tiles | taste/aesthetic-systems.md:33; library.json:107 |
| 83 | https://vercel.com | landing | good | Same archetype; Geist, near-white canvas | taste/aesthetic-systems.md:33; library.json:2037 |
| 84 | https://stripe.com | landing | good | Same archetype | taste/aesthetic-systems.md:33; library.json:1773 |
| 85 | https://superhuman.com | landing | good | Same archetype; warm off-white plus colour cards | taste/aesthetic-systems.md:33; library.json:1794 |
| 86 | https://www.notion.com | landing | good | "Editorial Minimalism" kin | taste/aesthetic-systems.md:41; library.json:1305 |
| 87 | https://www.wired.com | web page | good | Editorial Minimalism kin; news front page | taste/aesthetic-systems.md:41; library.json:2098 |
| 88 | https://www.warp.dev | landing | good | "Industrial Brutalism" kin | taste/aesthetic-systems.md:49; library.json:2073 |
| 89 | https://www.theverge.com | web page | good | Industrial Brutalism kin; tech magazine | taste/aesthetic-systems.md:49; library.json:1919 |
| 90 | https://www.duolingo.com | landing | good | "Warm Soft-SaaS" kin | taste/aesthetic-systems.md:57; library.json:573 |
| 91 | https://www.intercom.com | landing | good | Warm Soft-SaaS kin | taste/aesthetic-systems.md:57; library.json:902 |
| 92 | https://zapier.com | landing | good | Warm Soft-SaaS kin; cream canvas, one orange | taste/aesthetic-systems.md:57; library.json:2138 |
| 93 | https://elevenlabs.io | landing | good | "Dark-Tech / Cinematic" kin | taste/aesthetic-systems.md:66; library.json:605 |
| 94 | https://runway.com (runwayml) | landing | good | Dark-Tech kin | taste/aesthetic-systems.md:66; library.json:1582 |
| 95 | https://cursor.com | landing | good | Dark-Tech kin; warm cream grounds | taste/aesthetic-systems.md:66; library.json:475 |
| 96 | https://www.revolut.com | landing | good | Dark-Tech kin; photographic hero | taste/aesthetic-systems.md:66; library.json:1555 |
| 97 | https://www.spacex.com | landing | good | Dark-Tech kin; full-bleed photo on black | taste/aesthetic-systems.md:66; library.json:1733 |
| 98 | https://www.shopify.com | landing | good | Dark-Tech kin; near-black cinematic | taste/aesthetic-systems.md:66; library.json:1664 |
| 99 | https://www.schwab.com/ | landing | neutral | Library spec with explicit "measured at" URL | design-systems/library.json:374 |
| 100 | https://www.pepsi.com/ | landing | neutral | Library spec with explicit "measured at" URL | design-systems/library.json:1410 |
| 101 | https://electronics.sony.com | web page | neutral | Library spec read from live :root vars (3-tier tokens in the wild) | design-systems/library/sony/DESIGN.md:4, 602 |
| 102 | https://design-system.service.gov.uk/ | design system | neutral | Official source for library/gov-uk | design-systems/library/gov-uk/DESIGN.md:219 |
| 103 | https://service-manual.nhs.uk/design-system | design system | neutral | Official source for library/nhs | design-systems/library/nhs/DESIGN.md:278 |
| 104 | https://designsystem.digital.gov/ | design system | neutral | USWDS, source for library/digital-gov | design-systems/library/digital-gov/DESIGN.md:161 |
| 105 | https://atlassian.design/ | design system | neutral | Source for library/atlassian-design | design-systems/library/atlassian-design/DESIGN.md:191 |
| 106 | https://designsystem.maersk.com/ | design system | neutral | Source for library/maersk | design-systems/library/maersk/DESIGN.md:247 |
| 107 | https://design.klm.com/ | design system | neutral | Source for library/klm | design-systems/library/klm/DESIGN.md:485 |

## Best audit candidates
1. tests/fixtures/bad/slop-screen.html: the textbook AI-default dashboard with a gate-by-gate verdict table to calibrate against (README.md:121-132).
2. examples/sample-app/preview.html: the matched "good" twin of #1, the cleanest A/B pair.
3. tests/fixtures/critic/*.html (4 pages, 14 seeded defects, answer key in evals/critic-answer-key.json): taste-only slop that passes every objective gate, ideal for scoring the judgement layer.
4. tests/fixtures/bad/indigo-gradient.html: isolated generated-looking hero.
5. tests/fixtures/bad/one-sided-border.html: isolated side-stripe callout cliche.
6. evals/out/blind-2026-08-25/: real cold-start agent output, gates pass but critic says "rework" (borderline cases).
7. examples/showcase/index.html (Atlas): claimed-good dashboard with deliberate hierarchy; good false-positive test.
8. examples/terminal/index.html: very dense dashboard; tests whether Unslop over-flags density.
9. examples/sites/launch + store: kit-built marketing/e-commerce pages; check whether they still carry AI tells.
10. https://linear.app vs https://zapier.com: real-world contrasting archetypes for "good" calibration on the live web.

## Notes
- The repo is about gates more than galleries: almost all "bad" items are single-defect fixtures paired with a "good" twin (tests/fixtures/good).
- All "good" examples are self-authored by the maintainer's kit; they pass the repo's own 52 gates but that is a correctness claim, not proof of taste (the README says so).
- The 2,144-spec library is aggregated in row 80; only archetype-cited sites and a few explicit source URLs are listed individually. Domains for others are in design-systems/library.json descriptions.
- Plugin-eval prompts (plugin-evals/) and evals/briefs/ are text-only briefs, not artifacts, and are omitted.
- Liveness: the GitHub Pages index and /terminal/ fetched OK; third-party URLs were not checked.
