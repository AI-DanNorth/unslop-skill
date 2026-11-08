# krehel-skills (github.com/jakubkrehel/skills) — real artifacts for Unslop calibration
Repo cites almost no third-party sites; most value is the author's own sites/demos (d) and in-repo Good/Bad code pairs (c). Spot-checked live 2026-11-08: interfaces.dev, jakub.kr, skills.sh.

| # | URL or repo path | Medium | Label | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://interfaces.dev/ | landing | good | Author's design-engineering magazine; plugin homepage; editorial product landing (live) | README.md:1, README.md:9, .claude-plugin/plugin.json:9 |
| 2 | https://interfaces.dev/cheat-sheet | doc | good | Free "Interface cheat sheet" issue, same rules as skills, rendered (found via spot-check) | inferred from interfaces.dev homepage |
| 3 | https://interfaces.dev/make-interfaces-feel-better | doc | good | Skill landing page linked from magazine (found via spot-check) | inferred from interfaces.dev homepage |
| 4 | https://jakub.kr/ | web page | good | Author's personal site; minimalist design-engineer portfolio (live) | README.md:9 |
| 5 | https://jakub.kr/writing/details-that-make-interfaces-feel-better | doc | good | Article with inline interactive demos of the polish rules (radius, optical alignment, shadows) | jakub.kr homepage (spot-check) |
| 6 | https://jakub.kr/work/shared-layout-animations | component demo | good | Motion shared-layout demos; matches better-ui animation rules | jakub.kr homepage (spot-check) |
| 7 | https://jakub.kr/work/gradients | component demo | good | Interactive gradient explainer | jakub.kr homepage (spot-check) |
| 8 | https://jakub.kr/components/oklch-colors | component demo | good | OKLCH color component; pairs with better-colors | jakub.kr homepage (spot-check) |
| 9 | https://jakub.kr/work/drag-gesture | component demo | good | Drag gesture demo | jakub.kr homepage (spot-check) |
| 10 | https://jakub.kr/work/motion-gestures | component demo | good | Motion gesture demos | jakub.kr homepage (spot-check) |
| 11 | https://interfere.com/ (inferred) + /blog/how-we-built-interferes-new-website | landing | good | Author's employer site he built; real production SaaS landing | jakub.kr homepage (spot-check) |
| 12 | https://skills.sh/jakubkrehel/skills | gallery | neutral | Skill registry listing page for this repo | README.md:5 |
| 13 | https://github.com/jakubkrehel/skills | doc | neutral | Repo README itself | .claude-plugin/plugin.json:10 |
| 14 | https://ho1jr3x2dcwdu3t5.public.blob.vercel-storage.com/interfaces-og-image.png | web page (image) | good | Interfaces OG card; static brand visual | README.md:2 |
| 15 | https://developer.apple.com/design/human-interface-guidelines (inferred) | doc | good | Apple HIG cited as 44x44pt hit-target standard | skills/better-accessibility/hit-areas.md:11 |
| 16 | https://m3.material.io/ (inferred) | doc | good | Material Design cited as 48x48dp target standard | skills/better-accessibility/hit-areas.md:12 |
| 17 | https://www.radix-ui.com/colors (inferred) | doc | good | Radix 12-step role-based scale preferred for new systems | skills/better-colors/palette-structure.md:36-39 |
| 18 | https://tailwindcss.com/docs/colors (inferred) | doc | neutral | Tailwind lightness ramp; "white on 500 fails 4.5:1" anti-default | skills/better-colors/SKILL.md:77, palette-generation.md:42 |
| 19 | https://colorjs.io/ | doc | neutral | Library recommended for palette generation/conversion | skills/better-colors/palette-generation.md:28 |
| 20 | https://www.w3.org/TR/WCAG22/ (inferred) | doc | good | Accessibility standard all a11y rules are graded against | skills/better-accessibility/SKILL.md:106 |
| 21 | https://rsms.me/inter/ (inferred) | doc | neutral | Inter named as default sans (Helvetica, Inter, Geist) | skills/better-typography/choosing-fonts.md:10 |
| 22 | https://vercel.com/font (inferred, Geist) | doc | neutral | Geist named as default sans | skills/better-typography/choosing-fonts.md:10 |
| 23 | https://motion.dev/ (inferred) | doc | neutral | Motion library; MotionConfig reducedMotion recipe | skills/better-ui/animations.md:170 |
| 24 | skills/teardown/assets/viewer.html | component demo | good | Full in-repo HTML viewer page: tokens, light/dark, centered drawing, compact controls | skills/teardown/assets/viewer.html:1; spec in skills/teardown/preview-page.md:1-40 |
| 25 | skills/state-machine/switcher.md (HTML template) | component demo | neutral | Throwaway state-switcher page template | skills/state-machine/switcher.md:30 |
| 26 | skills/variant/picker.md (HTML template) | component demo | neutral | Variant picker page template | skills/variant/picker.md:30 |
| 27 | skills/better-ui/surfaces.md (concentric radii pair) | component demo | good vs slop | Same radius on nested surfaces = bad | skills/better-ui/surfaces.md:12,21,32,39 |
| 28 | skills/better-ui/surfaces.md (icon-button padding) | component demo | good vs slop | Equal padding pushes trailing icon outward | skills/better-ui/surfaces.md:54,60 |
| 29 | skills/better-ui/icons.md (stroke weight, filled-everywhere tabs) | component demo | good vs slop | 1.5px stroke vs bold label; all-filled tab icons lose state | skills/better-ui/icons.md:16,22,65,68 |
| 30 | skills/better-ui/animations.md (interruptible, hover replay) | component demo | good vs slop | Snapping close; every hover replays full entrance | skills/better-ui/animations.md:14,23,141,147 |
| 31 | skills/better-ui/enter-exit.md | component demo | good vs slop | Dramatic exit that steals focus vs subtle exit | skills/better-ui/enter-exit.md:139,146 |
| 32 | skills/better-ui/performance.md | component demo | good vs slop | `transition: all` anti-pattern | skills/better-ui/performance.md:10,17,27,43 |
| 33 | skills/better-colors/color-usage.md (every action colored) | component demo | good vs slop | All buttons colored so nothing is primary; accent on headings | skills/better-colors/color-usage.md:10,14,38,42 |
| 34 | skills/better-colors/color-usage.md (token misuse) | component demo | slop | Separator/text tokens repurposed by eye | skills/better-colors/color-usage.md:26,29 |
| 35 | skills/better-layout/grouping-and-alignment.md (dividers, edges, order) | component demo | good vs slop | Uniform spacing + lines; three leading edges; key fact last; RTL-breaking | skills/better-layout/grouping-and-alignment.md:14,18,52,56,78,91,97 |
| 36 | skills/better-layout/grouping-and-alignment.md (action as text) | component demo | good vs slop | Action indistinguishable from description text | skills/better-layout/grouping-and-alignment.md:35,38 |
| 37 | skills/better-layout/spacing-and-adaptivity.md | component demo | good vs slop | Icon buttons packed at 4px; button glued to edges w/ 100vw; viewport query card; German overflow | skills/better-layout/spacing-and-adaptivity.md:16,22,37,44,129,144 |
| 38 | skills/better-typography/spacing-and-sizing.md | component demo | good vs slop | Card description at heading line-height | skills/better-typography/spacing-and-sizing.md:53,56 |
| 39 | skills/better-typography/variable-fonts-and-opentype.md | component demo | good vs slop | Weight via raw `font-variation-settings` tag | skills/better-typography/variable-fonts-and-opentype.md:45,55 |
| 40 | skills/better-accessibility/semantics-and-aria.md | component demo | good vs slop | div-as-button vs native button; icon-only naming | skills/better-accessibility/semantics-and-aria.md:23,26,50,55 |
| 41 | skills/better-accessibility/hit-areas.md | component demo | good | Pseudo-element hit-area extension (CSS + Tailwind) | skills/better-accessibility/hit-areas.md:24,45 |
| 42 | skills/better-writing/SKILL.md (empty state) | component demo | good vs slop | "Shrug" empty state vs orientation + next step | skills/better-writing/SKILL.md:105,108 |
| 43 | skills/interface-review/removed-signals.md | doc | neutral | Regression signal table (removed aria/focus/reduced-motion etc.) usable as diff-audit checklist | skills/interface-review/removed-signals.md:5-17 |

## Best audit candidates
1. https://interfaces.dev/ — author's own polished landing; strong "good" anchor.
2. https://jakub.kr/writing/details-that-make-interfaces-feel-better — rules rendered live; ground truth for better-ui.
3. https://jakub.kr/ — minimal portfolio; tests false-positive rate on restrained design.
4. https://interfaces.dev/cheat-sheet — dense reference page; typography/layout calibration.
5. https://jakub.kr/components/oklch-colors — color component demo; better-colors anchor.
6. https://jakub.kr/work/shared-layout-animations — motion demos; animation-rule anchor.
7. https://interfere.com/ (inferred) — production SaaS landing by the author.
8. skills/teardown/assets/viewer.html — self-contained HTML tool page in repo; renders offline.
9. skills/better-colors/color-usage.md:38-42 — "every action colored" button row; clean slop/good pair.
10. skills/better-layout/grouping-and-alignment.md:14-97 — five slop/good layout pairs; render as fixtures.

## Notes
- Repo is rules-only: no screenshots, no showcase/inspiration lists, no cited third-party "bad" sites. "Slop" exists only as inline Bad code snippets.
- Rows 2-3, 5-11 come from WebFetch of the author's sites, not the repo; rows marked (inferred) give likely URLs for named references.
- Good/Bad snippet rows (27-42) are small; wrap each in a minimal HTML page to use as fixtures.
- Repo clone: /home/claude/refs/krehel-skills (shallow, plugin v1.19.0).
