# ui-ux-pro-max (nextlevelbuilder/ui-ux-pro-max-skill)

A BM25-searchable "design intelligence" skill: CSV databases of 80+ UI styles, 192 palettes, 74 font pairings and UX rules, plus sub-skills for slides, banners, logos and brand. It also ships a "Claude Website Design Stack" with a Playwright audit.
Real exemplar URLs are rare. The data cites brand *systems* (Apple HIG, Material 3, Fluent 2, Polaris) and brand-styled looks ("Apple-style", "Linear") instead of specific pages. Most of the useful artifacts are the repo's own demos, a before/after pair and the repo's own marketing site.

| # | URL or repo path | Medium | Label | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://skill-fixture-before.theroost.dev | dashboard | neutral (labelled "before", plain baseline) | Plain-HTML ops dashboard ("Northline weekly ops") with no design system; the control half of a pair | README.md:435 |
| 2 | https://ui-ux-pro-max-after.theroost.dev | dashboard | good (presented as the "after" improvement) | The same dashboard restyled using only the skill's generated design system (Swiss / dense / "Dashboard Data" type) | README.md:435 |
| 3 | https://uupm.cc | landing | good (the repo's own flagship site) | Dark navy hero with blue-to-orange gradient wordmark, glow blobs, pill "works with" badges, 6 stat cards. Reads as a textbook AI-SaaS landing | README.md:1, README.md:32 |
| 4 | screenshots/website.png | landing (screenshot) | good (own site) | Static capture of uupm.cc hero; ready-made image input for a visual audit | README.md:33 |
| 5 | https://uupm.cc/demo/pet-grooming | web page | good (own demo) | Only dedicated demo on the site (Pet Grooming & Spa), likely skill-generated output (found via WebFetch of uupm.cc) | uupm.cc (linked from README.md:1) |
| 6 | https://uupm.cc/#styles | gallery | neutral | Style gallery rendering every styles.csv entry (built from gallery/ Next.js app) | README.md:227-228 |
| 7 | gallery/ (app/page.tsx, components/StylePreview.tsx, PhoneMockup.tsx) | gallery | neutral | Source of the style gallery: auto-generated previews of 80+ named styles, one per style | gallery/app/page.tsx:1 |
| 8 | projects/saas-landing/index.html | landing | neutral (unreferenced demo, implicitly skill output) | "SaaSify - Streamline Your Workflow": Poppins/Open Sans, Tailwind blue-500 + orange CTA, backdrop-blur nav. Generic SaaS template | projects/saas-landing/index.html:1 |
| 9 | projects/portfolio-dark/index.html | web page | neutral (unreferenced demo) | "Alex Chen - Full Stack Developer": Space Grotesk/Archivo, 8x bg-gradient-to-br with to-purple-600/pink/emerald, backdrop-blur cards. Dense AI-default markers | projects/portfolio-dark/index.html:1 |
| 10 | projects/healthcare-dashboard/index.html | dashboard | neutral (unreferenced demo) | "HealthView - Analytics Dashboard": Fira Sans/Code, Chart.js, Tailwind default palette (#3B82F6/#10B981/#8B5CF6) | projects/healthcare-dashboard/index.html:1 |
| 11 | stack/examples/juniper-audit/screenshots/*.png (360/390/768/1024/1440/1920) | landing (screenshots) | good ("genuinely well-built") | Real financial-services marketing homepage, full-page at 6 viewports; has an existing audit report to compare against | stack/examples/juniper-audit/README.md:27 |
| 12 | stack/examples/juniper-audit/report.md + report.json | doc-PDF (audit report) | neutral | Ground-truth heuristic findings (focus-visible, 14 small tap targets, 1 contrast) to compare Unslop output against | stack/examples/juniper-audit/report.md:1 |
| 13 | https://3dviz.dev/ | landing | good (sister project promoted) | Cream (#fffaf2) storybook 3D-skill landing; possible "cream + serif" warm-default check | README.md:71 |
| 14 | https://cdn.nextlevelbuilder.io/skills/3dviz/harness-village.gif | video | neutral ("visual inspiration, not a benchmark") | Animated 3D fantasy village scene with camera navigation | README.md:63, README.md:67 |
| 15 | https://github.com/viettranx/3dviz-pro-max | gallery | neutral | Sister repo with demos and media provenance (docs/demos/README.md) | README.md:52 |
| 16 | https://nextlevelbuilder.io | landing | neutral (publisher's other project) | Publisher's studio site | README.md:44 |
| 17 | https://goclaw.sh | landing | neutral | Publisher's other product landing | README.md:44 |
| 18 | https://agentkit.best | landing | neutral | Publisher's other product landing | README.md:44 |
| 19 | https://tose.sh | landing | neutral | Publisher's other product landing | README.md:44 |
| 20 | Apple Human Interface Guidelines / Apple native apps (styles.csv "Apple Native Experience") | app screen | good (canonical system style) | Named platform system the skill emulates; real reference = developer.apple.com/design | src/ui-ux-pro-max/data/styles.csv:90 |
| 21 | Apple Liquid Glass (iOS/macOS 26) | app screen | good with caveat ("apply sparingly") | 2025 Apple material; useful for checking glass overuse | src/ui-ux-pro-max/data/styles.csv:15 |
| 22 | Apple marketing pages ("Apple-style" bento, #F5F5F7) | landing | good (style origin) | Origin of the Bento grid style, now an AI-default trope; apple.com product pages are the real exemplar | src/ui-ux-pro-max/data/styles.csv:40, :54 |
| 23 | Linear (linear.app) as a bento-grid origin ("2020s Apple/Linear") | landing | good (style origin) | Cited as a source of the bento look; linear.app is the real page | src/ui-ux-pro-max/data/styles.csv:54 |
| 24 | Figma- and Notion-style interfaces | app screen | good (cited fit for Neubrutalism) | Brands named as fits for neubrutalism | src/ui-ux-pro-max/data/styles.csv:39 |
| 25 | Google Material Design 3 Expressive (m3.material.io) | app screen | good (system style) | Mobile system reference | src/ui-ux-pro-max/data/styles.csv:76 |
| 26 | Microsoft Fluent 2 (Microsoft 365, Windows, Copilot) | app screen | good (system style) | Enterprise system reference with named real products | src/ui-ux-pro-max/data/styles.csv:86 |
| 27 | Shopify Polaris (Shopify admin, checkout) | app screen | good (system style; "not for generic marketing sites") | Merchant-admin reference with explicit scope limit | src/ui-ux-pro-max/data/styles.csv:87 |
| 28 | "AI purple/pink gradients" (e.g. #6366F1 / #7C3AED "AI Purple") | landing | slop (anti-pattern for banking/wellness) | Repo's own named anti-pattern, though colors.csv still recommends AI purple for AI products | README.md:119, README.md:190; colors.csv:19 |
| 29 | Three "AI-slop defaults": cream+serif+terracotta; near-black+acid accent; hairline broadsheet | landing | slop | Concrete slop archetypes to source exemplars for | stack/CLAUDE.md:23 |
| 30 | https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design | doc-PDF | good ("kills AI slop defaults") | Cited anti-slop taste layer | stack/README.md:17 |
| 31 | YC seed deck library (ycombinator.com/library) | slide deck | good (cited source) | Source of the "YC Seed Deck" slide strategy; real decks to fetch | cli/assets/skills/design-system/data/slide-strategies.csv:2 |
| 32 | Guy Kawasaki 10/20/30 rule (guykawasaki.com) | slide deck | good (cited source) | Source of a deck strategy | cli/assets/skills/design-system/data/slide-strategies.csv:3 |
| 33 | Nancy Duarte "Resonate" sparkline | slide deck | good (cited source) | Narrative deck structure; Duarte talks are real examples | cli/assets/skills/design-system/data/slide-strategies.csv:7 |
| 34 | TED Talk guidelines | slide deck | good (cited source) | Conference-talk deck reference | cli/assets/skills/design-system/data/slide-strategies.csv:11 |
| 35 | cli/assets/skills/slides/references/html-template.md (mirror: design/references/slides-html-template.md) | slide deck (template) | good (skill's own template) | HTML deck template with Chart.js and a dark 135deg gradient overlay on Pexels photos. Likely generates stock-photo decks | cli/assets/skills/slides/references/html-template.md:279 |
| 36 | cli/assets/skills/design-system/data/slide-backgrounds.csv + scripts/fetch-background.py (~20 Pexels office/tech photos) | slide deck (assets) | neutral | Hardcoded stock backgrounds ("abstract-tech gradient-dark", "futuristic office") are a stock-photo slop source | cli/assets/skills/design-system/scripts/fetch-background.py:166 |
| 37 | https://ui.shadcn.com/themes | component demo | good (recommended) | Theme generator recommended for theming; the default shadcn look is a common AI baseline | cli/assets/skills/ui-styling/references/shadcn-theming.md:220 |
| 38 | https://ui.shadcn.com | component demo | good (recommended) | Component library docs and demos | cli/assets/skills/ui-styling/SKILL.md:331 |
| 39 | https://tailwindui.com | component demo | good (recommended) | Tailwind UI templates; widely copied by AI output | cli/assets/skills/ui-styling/SKILL.md:334 |
| 40 | https://v0.dev | gallery | good (recommended "AI UI Generator") | Source of a huge volume of AI-generated UIs; a good place to mine slop samples | cli/assets/skills/ui-styling/SKILL.md:336 |
| 41 | https://coolors.co / https://colorhunt.co | gallery | good (recommended palette tools) | Palette galleries | cli/assets/skills/brand/references/color-palette-management.md:183, :186 |
| 42 | https://www.npmjs.com/package/ui-ux-pro-max-cli | web page | neutral | CLI package page (own) | README.md (16 refs across READMEs) |

## Best audit candidates

1. **theroost before/after dashboards (#1, #2)**: the only true before/after pair. It tests whether Unslop scores "after" better and whether it flags "after" as generic Swiss-template.
2. **uupm.cc homepage (#3, #4)**: a design-skill vendor's own site showing near-every AI-SaaS trope (gradient wordmark, glow blobs, stat-card row, pill badges). A strong likely-slop positive.
3. **projects/portfolio-dark/index.html (#9)**: dense purple/pink gradients plus backdrop-blur. A clear slop positive, and a local file that is easy to render.
4. **projects/saas-landing/index.html (#8)**: the "SaaSify" generic SaaS landing with Poppins and Tailwind defaults. A baseline slop sample.
5. **projects/healthcare-dashboard/index.html (#10)**: an AI-default dashboard (Tailwind palette, Chart.js). Tests dashboard-specific rules.
6. **Juniper audit screenshots and report (#11, #12)**: a real, human-built site with an existing heuristic report. Good as a "good / not slop" control and for comparing a11y findings.
7. **uupm.cc/demo/pet-grooming (#5)**: skill-generated output on a non-tech vertical. Tests "soft pink + gold + Cormorant" template slop.
8. **3dviz.dev (#13)**: a cream warm-palette landing. Checks the "cream + serif" slop default from stack/CLAUDE.md:23 against an intentional brand.
9. **Slides HTML template (#35, #36)**: the only deck artifact. Generating one deck from it gives a slide-medium slop sample (stock photos plus a gradient overlay).
10. **apple.com product page or linear.app (#22, #23)**: the cited origins of the bento trope. Use them as "good originals" to check that Unslop doesn't penalize the source of a pattern.

## Notes
- Data CSVs (styles, products, colors, typography) are generic recipes, not exemplars. Brand mentions are limited to Apple, Linear, Figma, Notion, Material, Fluent and Polaris, with no page URLs. Rows #20-27 and #31-34 need URLs resolved by hand.
- The projects/ demos are not referenced anywhere in the repo docs, so their labels are inferred. They are most likely early skill outputs.
- The repo is internally inconsistent: it warns against "AI purple/pink gradients" but recommends #7C3AED/#6366F1 "AI purple" for AI products (colors.csv:19, :132).
- WebFetch spot-checks: both theroost URLs, uupm.cc and 3dviz.dev returned page content (uupm.cc served an older "57 styles" version). No screenshots were taken.
- Clone: /home/claude/refs/ui-ux-pro-max (shallow, last commit 2026-11-08).
