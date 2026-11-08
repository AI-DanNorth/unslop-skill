# Kami (tw93/Kami): real artifact inventory
Print-first document design system (PDF/PNG/PPTX): parchment `#f5f4ed`, ink-blue `#1B365D`, single serif. Clone at /home/claude/refs/kami; paths below are repo-relative. Every demo ships as .html + .pdf + .png, which makes the set unusually good for print and slide media.

| # | URL or repo path | Medium | Label | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://kami.tw93.fun/ (+ index-zh/tw/ja/ko.html) | gallery | good | Official site and gallery (output samples, social cards, "built with Kami"). Live as of 2026-11-08 | README.md:109; site/index.html |
| 2 | https://pake.run | web page | good | Real product landing page built with Kami's landing-page system. Live | README.md:175 |
| 3 | https://miaoyan.app | web page | good | Real landing page built with Kami. Live | README.md:180 |
| 4 | https://mole.fit | web page | good | Real paid-product landing page built with Kami (pricing, FAQ). Live | README.md:185 |
| 5 | site/assets/showcase/{pake,miaoyan,mole}-landing-{en,zh}.png | web page (screenshot) | good | Frozen screenshots of rows 2-4 in EN and ZH, useful for stable baselines | README.md:175-185 |
| 6 | site/assets/showcase/kami-landing.png | web page (screenshot) | good | Screenshot of Kami's own landing page, used as og/primary image | site/index-ja.html:152 |
| 7 | site/assets/demos/demo-musk-resume.{html,pdf,png} | resume | good | 2-page founder resume with public-figure data; first README showcase item | README.md:25 |
| 8 | site/assets/demos/demo-resume-ko.{html,pdf,png} | resume | good | Korean 2-page resume (Hangul serif) | site/index-ko.html:228 |
| 9 | site/assets/demos/demo-kami-print.{html,pdf,png} | one-pager | good | Chinese one-pager in the white-paper print variant | README.md:30, :165 |
| 10 | site/assets/demos/demo-mole.{html,pdf,png} | one-pager | good | English product brief, 1 page | README.md:47 |
| 11 | site/assets/demos/demo-tesla.{html,pdf,png} | doc-PDF | good | Chinese equity report (2 pp) with inline SVG charts and a dense metrics layout | README.md:35 |
| 12 | site/assets/demos/demo-agent-slides.{html,pdf,png} (+ pages/*-1..8.webp) | slide deck | good | 8-slide keynote; design.md calls it the "approved" slide type scale | README.md:40; references/design.md:898 |
| 13 | site/assets/demos/demo-letter.{html,pdf,png} | doc-PDF | good | Chinese recommendation letter, 1 page | README.md:52 |
| 14 | site/assets/demos/demo-changelog.{html,pdf,png} | doc-PDF | good | Mole v1.7.1 release notes | README.md:57 |
| 15 | site/assets/demos/demo-kaku.{html,pdf,png} | doc-PDF (portfolio) | good | Japanese 7-page portfolio | README.md:62 |
| 16 | site/assets/demos/demo-waza.{html,pdf,png} | doc-PDF | neutral | Waza one-pager demo, not linked from the README or the site | (file only) |
| 17 | site/assets/demos/demo-social-cards-{mole,kaku,pake,miaoyan}-en.{html,jpg} | social card | good | 4 card sets (cover/list/text/screenshot) on four paper colors | README.md:76-91 |
| 18 | site/assets/demos/demo-social-cards-{mole,kaku,pake,miaoyan}-zh.{html,jpg} | social card | good | Chinese versions of row 17 | README_CN.md:76-91 |
| 19 | site/assets/demos/demo-social-cards.{html,pdf,png} | social card | neutral | "10 life best practices" card set, unlinked | (file only) |
| 20 | site/assets/showcase/kami-reliable-documents-twitter-en.{html,png}; kami-v1.10-architecture-twitter.{html,png} | diagram / social card | good | Architecture diagrams sized for X posts | site/assets/showcase/ |
| 21 | site/assets/illustrations/travel-spatialvla.png | diagram | good | AI-image redraw of a paper figure following the Kami prompt; README calls it "no manual touch-up" | README.md:195 |
| 22 | site/assets/illustrations/travel-tesla-optimus.png | diagram | good | Patent-figure "evidence layout" illustration | README.md:200 |
| 23 | site/assets/illustrations/travel-3d-representations.png | diagram | neutral | Third illustration, unlinked | (file only) |
| 24 | site/assets/og.png | social card | neutral | Site og:image | site/index-ja.html:22 |
| 25 | plugins/kami/skills/kami/assets/templates/one-pager{,-en,-ko}.html | template | neutral | One-pager template in CN, EN and KO | SKILL.md:68 |
| 26 | .../templates/letter{,-en,-ko}.html | template | neutral | Formal letter | SKILL.md:69 |
| 27 | .../templates/resume{,-en,-ko}.html | template | neutral | Exactly-2-page resume | SKILL.md:70 |
| 28 | .../templates/portfolio{,-en,-ko}.html | template | neutral | 3-6 page portfolio | SKILL.md:71 |
| 29 | .../templates/long-doc{,-en,-ko}.html | template | neutral | 6-15 page long report | SKILL.md:72 |
| 30 | .../templates/slides-weasy{,-en,-ko}.html; slides{,-en}.py; marp/slides-marp{,-en}.{md,css} | template (slide deck) | neutral | Three deck paths: WeasyPrint, python-pptx and Marp | SKILL.md:73; :41-42 |
| 31 | .../templates/equity-report{,-en,-ko}.html | template | neutral | Dashboard, thesis and risk report | SKILL.md:74 |
| 32 | .../templates/changelog{,-en,-ko}.html | template | neutral | Release notes | SKILL.md:75 |
| 33 | .../templates/landing-page{,-en,-ko}.html (+ llms/robots/sitemap/vercel examples) | template (web page) | neutral | Landing-page system with {{PLACEHOLDER}} slots | SKILL.md:76 |
| 34 | .../templates/social-cards{,-en,-ko}.html | template (social card) | neutral | 1242x1660 3:4 cards | SKILL.md:77 |
| 35 | .../assets/diagrams/architecture-board.html | diagram | good | Poster-size five-layer board containing a real terminal-emulator demo | references/diagrams.md:14, :65 |
| 36 | .../assets/diagrams/{architecture,flowchart,layer-stack,swimlane,state-machine,timeline,tree,quadrant,venn}.html | diagram | neutral | Structural SVG diagram templates | references/diagrams.md:14-26 |
| 37 | .../assets/diagrams/{bar-chart,line-chart,donut-chart,candlestick,waterfall}.html | diagram (chart) | neutral | Generated chart templates | references/diagrams.md:27-28 |
| 38 | .../assets/diagrams/{sequence,class,er}.html (+ src/*.mmd) | diagram | neutral | Mermaid-authored diagrams re-themed to the palette | references/mermaid.md |
| 39 | scripts/tests/corpus/density/flag/*.html (4) | doc-PDF fixture | slop | Labelled fixtures for sparse or underfilled pages (e.g. sparse-60, last-63) | scripts/tests/test_corpus.py:1-5 |
| 40 | scripts/tests/corpus/density/pass/*.html (4) | doc-PDF fixture | good | Edge cases just inside the fill threshold | scripts/tests/test_corpus.py:1-5 |
| 41 | scripts/tests/corpus/orphans/flag/*.html (4) | doc-PDF fixture | slop | Paragraphs that end on a one- or two-word line | scripts/tests/test_corpus.py:1-5 |
| 42 | scripts/tests/corpus/orphans/pass/*.html (4) | doc-PDF fixture | good | Acceptable last-line lengths | scripts/tests/test_corpus.py:1-5 |
| 43 | scripts/tests/corpus/resume_balance/flag/*.html (4) | resume fixture | slop | Unbalanced 2-page resumes (p1 at 97%, thin continuation page, one-page) | scripts/tests/test_corpus.py:1-5 |
| 44 | scripts/tests/corpus/resume_balance/pass/*.html (4) | resume fixture | good | Balanced page fills (84-94%) | scripts/tests/test_corpus.py:1-5 |
| 45 | https://github.com/cathrynlavery/diagram-design | gallery (repo) | good | Credited as the inspiration for Kami's diagrams and anti-slop table | references/diagrams.md:692 |
| 46 | https://github.com/tt-a1i/archify | diagram (repo) | good | Credited for the semantic-geometry approach | references/diagrams.md:339 |
| 47 | https://github.com/lukilabs/beautiful-mermaid; https://agents.craft.do/mermaid | diagram (tool) | neutral | Mermaid renderer Kami re-themes | README.md:160; references/mermaid.md:13 |
| 48 | https://github.com/tw93/Kaku, https://github.com/tw93/Waza | web page (repo) | neutral | Sibling projects in the same "trilogy" | README.md:16 |

## Best audit candidates
1. demo-agent-slides.pdf (#12): **slide**. A curated 8-slide deck that the repo calls the approved scale; good positive baseline for a deck.
2. demo-musk-resume.pdf (#7): **resume/print**. A 2-page resume with real content.
3. demo-tesla.pdf (#11): **doc-PDF/print**. Dense report with charts; tests chart and hierarchy rules.
4. demo-kami-print.pdf (#9): **one-pager/print**, white-paper variant; contrast with the parchment default.
5. demo-mole.pdf (#10): **one-pager/print** in English.
6. demo-kaku.pdf (#15): **multi-page portfolio/print** (JP).
7. corpus resume_balance + orphans flag/pass (#41-44): **print fixtures with ground-truth labels**, ready for checking detector precision.
8. mole.fit (#4): live landing page with pricing and FAQ in the same house style; an editorial counterpoint to SaaS slop.
9. demo-social-cards-*-en.jpg (#17): **social cards**, a medium that is scarce elsewhere.
10. architecture-board.html (#35): poster-size diagram, scarce elsewhere.

## Notes
- The repo names no external URLs as bad examples. All "slop" material is either text in references/anti-patterns.md (57 numbered bad/fix rows, no artifacts) or the synthetic flag fixtures in scripts/tests/corpus.
- Everything is one author's house style, so it is a positive set for "editorial/print" and not a broad sample. Treat it as a single aesthetic.
- Spot-checked live (WebFetch, 2026-11-08): kami.tw93.fun, mole.fit, pake.run, miaoyan.app.
- Corpus fixtures are tiny synthetic HTML files, and their labels come from the repo's layout gates (density, orphans, resume balance), not from taste.
- The README links point to `skills/kami/...`, but the actual path is `plugins/kami/skills/kami/...`.
