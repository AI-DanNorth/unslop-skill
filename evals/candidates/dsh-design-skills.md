# dsh-design-skills — example inventory

A skill pack for DeepSeek Harness (zhaiyateng/dsh-design-skills, MIT) with 10 "aesthetic style" SKILL.md specs (tokens, component rules, forbidden lists, acceptance checklists) meant to stop vibe-coded sites from looking AI-made.
Every example uses one fictional product ("Relay", an agent-orchestration console) as a landing page in 10 styles. Each style has an HTML demo, a PNG screenshot, and a live GitHub Pages gallery.

| # | URL or repo path | Medium | Label (as presented) | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://zhaiyateng.github.io/dsh-design-skills/ | gallery | good | Live gallery with all 10 styles side by side, same content each time (confirmed live 2026-11-08). | README.md:17-21; gh-pages-src/README.md:3 |
| 2 | https://zhaiyateng.github.io/dsh-design-skills/dark-saas-landing.html | landing | good | Live Linear-style dark SaaS landing: terminal hero, 6 feature cards, a 4-stat row, YAML block, 3-tier pricing (confirmed live). The other 9 demos use the same path pattern `<style>-landing.html`. | scripts/deploy-pages.sh:14-15,30 |
| 3 | examples/dark-saas-landing.html | landing | good | Linear-inspired dark style. Its forbidden list bans purple/blue gradient backgrounds as the main AI-look offender. Classic dev-tool SaaS template structure. | README.md:41; skills/dark-saas/SKILL.md:66-72 |
| 4 | examples/apple-minimal-landing.html | landing | good | Apple-style minimal white: thin weights, large whitespace, no gradients. | README.md:41; skills/apple-minimal/SKILL.md:59 |
| 5 | examples/neo-neumorphism-landing.html | landing | good | Soft UI with double-shadow emboss. Low contrast by design, so expect accessibility conflicts. | README.md:41; skills/neo-neumorphism/SKILL.md:19,63 |
| 6 | examples/brutalism-landing.html | landing | good | Neo-brutalist: no radius, thick borders, dense layout. The deliberate anti-template style. | README.md:41; skills/brutalism/SKILL.md:59 |
| 7 | examples/glassmorphism-landing.html | landing | good | Frosted glass over a vivid blue-purple-pink gradient, which is a known AI-trope combination that the repo requires. | README.md:41; skills/glassmorphism/SKILL.md:13,70 |
| 8 | examples/japanese-minimal-landing.html | landing | good | Serif-led (Mincho/Noto Serif) zen layout with one vermilion accent and no motion. | README.md:41; skills/japanese-minimal/SKILL.md:14,58 |
| 9 | examples/bento-grid-landing.html | landing | good | Bento card wall, an AI-default layout pattern. The spec tries to discipline it with grid alignment and a 12-24px gap. | README.md:41; skills/bento-grid/SKILL.md:64 |
| 10 | examples/cyberpunk-landing.html | landing | good | Neon cyan/magenta on dark with glow. Heavy on trope-style decoration. | README.md:41; skills/cyberpunk/SKILL.md:67 |
| 11 | examples/vaporwave-landing.html | landing | good | Synthwave pink-purple sky gradient (6 gradient uses). Retro novelty style. | README.md:41; skills/vaporwave/SKILL.md:60 |
| 12 | examples/art-deco-landing.html | landing | good | Gold and emerald 1920s geometric serif style, aimed at luxury brands. | README.md:41; skills/art-deco/SKILL.md:58 |
| 13 | assets/dark-saas-landing.png | landing (screenshot) | good | Promo screenshot of #3, presented as the "after". | README.md:35 |
| 14 | assets/apple-minimal-landing.png | landing (screenshot) | good | Screenshot of #4. | README.md:35 |
| 15 | assets/neo-neumorphism-landing.png | landing (screenshot) | good | Screenshot of #5. | README.md:35 |
| 16 | assets/brutalism-landing.png | landing (screenshot) | good | Screenshot of #6. | README.md:35 |
| 17 | assets/glassmorphism-landing.png | landing (screenshot) | good | Screenshot of #7. | README.md:35 |
| 18 | assets/japanese-minimal-landing.png | landing (screenshot) | good | Screenshot of #8. | README.md:39 |
| 19 | assets/bento-grid-landing.png | landing (screenshot) | good | Screenshot of #9. | README.md:39 |
| 20 | assets/cyberpunk-landing.png | landing (screenshot) | good | Screenshot of #10. | README.md:39 |
| 21 | assets/vaporwave-landing.png | landing (screenshot) | good | Screenshot of #11. | README.md:39 |
| 22 | assets/art-deco-landing.png | landing (screenshot) | good | Screenshot of #12. | README.md:39 |
| 23 | gh-pages-src/index.html | gallery | neutral | Source of the gallery page: a 10-card screenshot grid built from a JS `styles` array. | gh-pages-src/index.html:88-97 |
| 24 | https://linear.app (implied; no URL given) | web page | good | Named as the exemplar for dark-saas. Tokens are distilled from awesome-design-md's linear.app DESIGN.md. | skills/dark-saas/SKILL.md:3-7; references/dark-saas-tokens.md:3 |
| 25 | https://www.apple.com (implied; no URL given) | web page | good | Named as the exemplar for apple-minimal and bento-grid (cites 17px body text on the Apple site). | skills/apple-minimal/SKILL.md:7,43; skills/bento-grid/SKILL.md:3-4 |
| 26 | https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/linear.app/DESIGN.md | doc-PDF | neutral | Upstream design-token spec for Linear. A reference source, not an artifact. | THIRD_PARTY_NOTICES.md:14 |

## Best audit candidates

1. **#2 / #3 dark-saas demo**: closest to the stock AI SaaS landing page (terminal hero, 6 feature cards, 99.99% stat row, 3-tier pricing). Tests whether Unslop flags structural slop even when the palette is disciplined.
2. **#7 glassmorphism demo**: requires the blue-purple-pink gradient plus blur. A likely true-positive slop case for the token and palette rules.
3. **#9 bento-grid demo**: the bento wall is an AI-default layout. Good for testing pattern-level detection against a "disciplined" version.
4. **#10 cyberpunk demo**: neon glow on dark. Tests the glow and decoration rules and contrast checks.
5. **#11 vaporwave demo**: gradient-heavy novelty style. Tests whether Unslop separates an intended retro style from lazy default gradients.
6. **#6 brutalism demo**: the anti-template style. A useful negative or edge control for checking false positives.
7. **#8 japanese-minimal demo**: serif, restrained, one accent. Likely the cleanest example, so a good "should pass" calibration point.
8. **#5 neo-neumorphism demo**: deliberately low contrast. Tests accessibility rules overriding the style intent.
9. **#4 apple-minimal demo**: a generic "clean white" landing. Tests the line between minimal and bland/template.
10. **#1 gallery**: the same copy and structure in 10 skins. Ideal for checking that Unslop scores structure and copy consistently and not just the visual skin.

## Notes

- The repo has no bad/slop examples. Every artifact is presented as a "good" output. The only slop signals are the per-skill forbidden lists (e.g. "purple/blue large gradient backgrounds = worst AI-look offender", "default Tailwind gray-*", "rainbow card walls").
- All 10 demos are AI-built and share identical content (Relay), which makes them a controlled set: style varies, content does not.
- Real-site exemplars (Linear, Apple) are named but never linked. The rows above give their canonical homepages.
- Only one medium appears (landing page). There are no decks, docs, dashboards, diagrams or emails.
- The README's "before / after" claim means the 10 styles as "after". No "before" artifact is included.
