# design-taste (madebymustafa/design-taste) — real artifacts for Unslop calibration
Shallow clone at /home/claude/refs/design-taste (last commit 2026-08-15). Repo paths are relative to that clone. Nearly all artifacts are in-repo: one brief ("Skittie — Product analytics for indie founders") built as a slop baseline plus 10 genre-pack versions.

| # | URL or repo path | Medium | Label | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | examples/before.html | landing | slop | Default-agent baseline: Inter, slate-900, indigo→violet gradient CTA, frosted sticky nav, centered hero + feature cards; textbook AI-default page | README.md:25; gallery/README.md:17 |
| 2 | examples/after.html | landing | good | Same copy/sections as #1 in editorial-minimal (Fraunces + IBM Plex Mono, warm paper, vermillion); a direct controlled pair | README.md:25, README.md:43 |
| 3 | examples/brutalist-industrial.html | landing | good | Blueprint grid rules, heavy caps (Archivo), mono coordinates, one signal color | README.md:44; gallery/README.md:21 |
| 4 | examples/quiet-luxury.html | landing | good | Ivory/ink, brass-oxblood accent, serif italics; "private bank annual report" | README.md:45; gallery/README.md:22 |
| 5 | examples/dark-tech.html | landing | good | Linear/Vercel-school dark; tests whether an auditor wrongly flags restrained dark-SaaS as slop | README.md:46; gallery/README.md:23 |
| 6 | examples/playful-color.html | landing | good | Sticker-poster type, thick outlines, hard offset shadows; loud-but-intentional | README.md:47; gallery/README.md:24 |
| 7 | examples/retro-print.html | landing | good | Riso: halftone, misregistration, Anton + Newsreader | README.md:48; gallery/README.md:25 |
| 8 | examples/japanese-minimal.html | landing | good | Negative space as layout, mincho serif, one vertical text element, hanko red | README.md:49; gallery/README.md:26 |
| 9 | examples/neo-brutalism.html | landing | good | Ink borders on everything, 6px hard shadows, chunky pills; neo-brutalism is itself a common AI trend, so a good edge case | README.md:50; gallery/README.md:27 |
| 10 | examples/corporate-trust.html | landing | good | Deliberately conventional (12-col, 3-col features, one deep blue #1F4FE0, system type); tests whether "conventional" gets mislabeled as slop | README.md:51; skills/corporate-trust/SKILL.md:40 |
| 11 | examples/cinematic-motion.html | landing | good | 858-line GSAP "site-of-the-day" page: pinned scenes, scrubbed counter, drag carousel, live CSS product screen; heaviest motion test | README.md:52; gallery/README.md:29 |
| 12 | gallery/before/before.png | web page (screenshot) | slop | 1440px full-page capture of #1 | gallery/README.md:17; scripts/capture-screenshots.mjs:13 |
| 13 | gallery/{10 packs}/before.png | web page (screenshot) | slop | Identical copies of #12, one per pack folder, not distinct artifacts | gallery/README.md:20-29 |
| 14 | gallery/{10 packs}/after.png | web page (screenshot) | good | Full-page 1440×900 static captures of #2–#11; good for image-only audit input | gallery/README.md:20-29 |
| 15 | gallery/launch-grid.png | gallery | good | One board showing all ten identities from one brief | README.md:126 |
| 16 | media/cinematic-motion-demo.gif (+ .mp4) | doc (video demo) | neutral | 39s before→after screen film (default agent, then cinematic-motion) | README.md:13-15 |
| 17 | https://raw.githubusercontent.com/madebymustafa/design-taste/main/media/cinematic-motion-demo.mp4 | doc (video demo) | neutral | Hosted copy of #16 | README.md:15 |
| 18 | https://github.com/madebymustafa/design-taste | doc | neutral | Repo README is the only docs site. No GitHub Pages: madebymustafa.github.io/design-taste returned an error | README.md:82 |
| 19 | https://linear.app (inferred) | landing | good | Named exemplar of the dark-tech school and of "Linear-style minimal" | skills/dark-tech/SKILL.md:4; skills/design-taste/SKILL.md:33 |
| 20 | https://vercel.com (inferred) | landing | good | Named exemplar of the dark-tech school | skills/dark-tech/SKILL.md:4; README.md:46 |
| 21 | https://stripe.com (inferred) | landing | good | Named in "Linear/Vercel/Stripe-dark school" | skills/dark-tech/SKILL.md:4 |
| 22 | https://www.awwwards.com (inferred) | gallery | good | Cited as the benchmark for horizontal pinned galleries and calm motion | skills/taste-gsap/SKILL.md:36, :62 |
| 23 | Magma studio site (URL unknown, inferred, low confidence) | portfolio | good | "Magma-school" drag carousels cited as the reference pattern | skills/taste-gsap/SKILL.md:37 |
| 24 | https://placehold.co | neutral (asset service) | slop | Placeholder images cited as a sign of an unfinished, slop page | skills/taste-code-craft/SKILL.md:55 |

## Best audit candidates
1. examples/before.html: pure AI-default slop baseline (positive control).
2. examples/after.html: same content, editorial-minimal; paired negative control for #1.
3. examples/dark-tech.html: tests whether dark SaaS gets falsely flagged.
4. examples/corporate-trust.html: tests whether "intentionally conventional" gets falsely flagged.
5. examples/neo-brutalism.html: a trendy style that could be slop or taste; boundary case.
6. examples/cinematic-motion.html: motion- and GSAP-heavy; covers motion, reduced-motion and performance rules.
7. examples/japanese-minimal.html: extreme whitespace; tests density and "empty" heuristics.
8. examples/playful-color.html: loud, saturated palette; tests color-restraint rules for false positives.
9. gallery/before/before.png vs gallery/editorial-minimal/after.png: image-only audit of the pair.
10. https://linear.app (inferred): a real-world version of the dark-tech exemplar, to compare against #3.

## Notes
- All 11 HTML pages share one brief and the same copy, so they isolate visual identity from content. They are agent-generated, and the "good" ones were made by agents using these skills (they are not human-designed).
- There are only 11 distinct visual artifacts: the 10 pack before.png files are duplicates, and the after.png files are screenshots of the HTML pages.
- Apart from the repo itself, the repo cites no external exemplar URLs. Linear, Vercel, Stripe, Awwwards and Magma are named only, so their URLs are inferred.
- The slop vocabulary (indigo-purple gradient hero, "Get started free" purple button, three feature cards, Inter, rounded-2xl) is at skills/design-taste/SKILL.md:42-50 and README.md:5.
- Liveness was spot-checked for one URL (the GitHub Pages site), which failed. The other URLs were not fetched.
