# agent-skills (vercel-labs/agent-skills) — design artifact candidates
Mostly engineering skills (React perf, RN, composition, view transitions); design rules live in external repos the skills fetch. Paths are relative to /home/claude/refs/agent-skills. "slop→good" = Incorrect/Correct code pair (Incorrect half is the flagged artifact).

| # | URL or repo path | Medium | Label | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://github.com/vercel/next-app-router-playground/tree/main/app/view-transitions | component demo | good | Cited as "Vercel's reference implementation" of view transitions (shop, shared-element morph, directional slides) | skills/react-view-transitions/README.md:44 |
| 2 | https://app-router.vercel.app/view-transitions | app screen | good | Live deploy of #1 (not cited directly; resolved via WebFetch): product grid → detail morph, directional pagination | derived from skills/react-view-transitions/README.md:44 |
| 3 | https://vercel.com/blog/how-we-made-the-vercel-dashboard-twice-as-fast | doc | good | Real product case study (Vercel Dashboard, Lighthouse 51→94); spot-checked live | skills/react-best-practices/rules/js-cache-function-results.md:80 |
| 4 | https://vercel.com/blog/how-we-optimized-package-imports-in-next-js | doc | neutral | Vercel engineering post backing barrel-import rule | skills/react-best-practices/rules/bundle-barrel-imports.md:60 |
| 5 | https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md | doc | good | Actual rule source for web-design-guidelines audit (100+ UI rules); HTTP 200 | skills/web-design-guidelines/SKILL.md:26 |
| 6 | https://raw.githubusercontent.com/vercel-labs/writing-guidelines/main/command.md | doc | good | Rule source for writing/prose audit (UI copy, docs voice); HTTP 200 | skills/writing-guidelines/SKILL.md:26 |
| 7 | https://skills.sh/vercel-labs/agent-skills | gallery | neutral | Repo's own skills directory/listing page | README.md:7 |
| 8 | https://agentskills.io/ | doc | neutral | Agent Skills format spec site | README.md:5 |
| 9 | https://zeego.dev/components/dropdown-menu | component demo | good | Native menus recommended over JS-drawn dropdowns | skills/react-native-skills/rules/ui-menus.md:174 |
| 10 | https://github.com/nandorojo/galeria | component demo | good | Recommended native image gallery/lightbox | skills/react-native-skills/rules/ui-image-gallery.md:104 |
| 11 | https://legendapp.com/open-source/legend-list | component demo | good | Recommended virtualized list component | skills/react-native-skills/AGENTS.md:2895 |
| 12 | https://docs.expo.dev/router/advanced/native-tabs | doc | good | Native tab bar recommended over JS tabs | skills/react-native-skills/rules/navigation-native-navigators.md:188 |
| 13 | https://reactnavigation.org/docs/native-stack-navigator | doc | good | Native stack navigator reference | skills/react-native-skills/rules/navigation-native-navigators.md:185 |
| 14 | https://oss.callstack.com/react-native-bottom-tabs/docs/guides/usage-with-react-navigation | doc | good | Native bottom tabs library | skills/react-native-skills/rules/navigation-native-navigators.md:186 |
| 15 | https://docs.expo.dev/versions/latest/sdk/image/ | doc | good | expo-image (placeholder/blurhash, caching) | skills/react-native-skills/rules/ui-expo-image.md:66 |
| 16 | https://docs.swmansion.com/react-native-gesture-handler/docs/gestures/tap-gesture | doc | good | Animated press-state reference | skills/react-native-skills/rules/animation-gesture-detector-press.md:95 |
| 17 | https://react.dev/reference/react/ViewTransition | doc | neutral | Canonical ViewTransition API docs | skills/react-view-transitions/references/patterns.md:3 |
| 18 | https://nextjs.org/docs/app/guides/view-transitions | doc | neutral | Next.js view-transitions guide | skills/react-view-transitions/references/nextjs.md:7 |
| 19 | https://github.com/w3c/csswg-drafts/issues/10930 | doc | neutral | Spec issue: named VT elements skip hit-testing mid-transition (interaction bug) | skills/react-view-transitions/references/patterns.md:123 |
| 20 | https://csstriggers.com/ | doc | neutral | Which CSS props trigger layout/paint | skills/react-best-practices/rules/js-batch-dom-css.md:107 |
| 21 | skills/react-view-transitions/references/css-recipes.md | component demo | good | Copy-paste motion recipes: fade, slide, directional nav, shared morph, text morph, scale, sliding tab indicator, reduced motion (:301) | skills/react-view-transitions/references/css-recipes.md:1 |
| 22 | skills/react-view-transitions/references/patterns.md (Searchable Grid, Card Expand, Sliding Indicator) | component demo | good | Full JSX UI patterns with motion intent | skills/react-view-transitions/references/patterns.md:5, :41, :137 |
| 23 | skills/react-view-transitions/SKILL.md "When to Animate" + "Choosing Animation Style" tables | doc | good | Anti-gratuitous-motion rule: every transition must communicate continuity; no directional slides for lateral nav | skills/react-view-transitions/SKILL.md:14-41 |
| 24 | skills/react-native-skills/rules/ui-styling.md (font-size pair) | code pair | slop→good | Incorrect: 18/14/12px size ladder; Correct: one size, hierarchy via weight + grey (#666/#999) — opinionated typography rule | skills/react-native-skills/rules/ui-styling.md:72 |
| 25 | skills/react-native-skills/rules/ui-styling.md (borderCurve, gap, gradient, boxShadow) | code pair | slop→good | Continuous corners, gap over margins, CSS boxShadow/gradient strings | skills/react-native-skills/rules/ui-styling.md:12, :22, :47, :61 |
| 26 | skills/react-native-skills/rules/ui-menus.md | code pair | slop→good | JS-drawn dropdown vs native menu | skills/react-native-skills/rules/ui-menus.md:14 |
| 27 | skills/react-native-skills/rules/ui-native-modals.md | code pair | slop→good | JS bottom sheet vs native formSheet modal | skills/react-native-skills/rules/ui-native-modals.md:15 |
| 28 | skills/react-native-skills/rules/ui-pressable.md | code pair | slop→good | Touchable* vs Pressable | skills/react-native-skills/rules/ui-pressable.md:13 |
| 29 | skills/react-native-skills/rules/ui-safe-area-scroll.md | code pair | slop→good | SafeAreaView padding vs contentInsetAdjustmentBehavior | skills/react-native-skills/rules/ui-safe-area-scroll.md:12 |
| 30 | skills/react-native-skills/rules/ui-scrollview-content-inset.md | code pair | slop→good | Padding hacks vs contentInset | skills/react-native-skills/rules/ui-scrollview-content-inset.md:15 |
| 31 | skills/react-native-skills/rules/ui-expo-image.md | code pair | slop→good | RN Image vs expo-image | skills/react-native-skills/rules/ui-expo-image.md:12 |
| 32 | skills/react-native-skills/rules/ui-image-gallery.md | code pair | slop→good | Hand-rolled lightbox vs Galeria | skills/react-native-skills/rules/ui-image-gallery.md:15 |
| 33 | skills/react-native-skills/rules/animation-gpu-properties.md | code pair | slop→good | Animating height/width vs transform/opacity | skills/react-native-skills/rules/animation-gpu-properties.md:12 |
| 34 | skills/react-native-skills/rules/animation-gesture-detector-press.md | code pair | slop→good | JS press state vs UI-thread press animation | skills/react-native-skills/rules/animation-gesture-detector-press.md:15 |
| 35 | skills/react-native-skills/rules/navigation-native-navigators.md | code pair | slop→good | JS stack/tabs vs native navigators | skills/react-native-skills/rules/navigation-native-navigators.md:22 |
| 36 | skills/react-native-skills/rules/design-system-compound-components.md | code pair | slop→good | Polymorphic children vs compound Button parts | skills/react-native-skills/rules/design-system-compound-components.md:16 |
| 37 | skills/react-native-skills/rules/fonts-config-plugin.md | code pair | slop→good | Runtime useFonts (FOUT/splash delay) vs build-time fonts | skills/react-native-skills/rules/fonts-config-plugin.md:13 |
| 38 | skills/react-native-skills/rules/list-performance-images.md | code pair | slop→good | Full-res images in lists vs compressed thumbnails | skills/react-native-skills/rules/list-performance-images.md:14 |
| 39 | skills/react-native-skills/rules/rendering-text-in-text-component.md | code pair | slop→good | Bare strings vs Text (crash) | skills/react-native-skills/rules/rendering-text-in-text-component.md:13 |
| 40 | skills/react-best-practices/rules/rendering-hydration-no-flicker.md | code pair | slop→good | Theme/client-state flash on hydrate vs inline pre-paint script | skills/react-best-practices/rules/rendering-hydration-no-flicker.md:12 |
| 41 | skills/react-best-practices/rules/rendering-usetransition-loading.md | code pair | slop→good | Manual isLoading spinner state vs useTransition pending UI | skills/react-best-practices/rules/rendering-usetransition-loading.md:12 |
| 42 | skills/react-best-practices/rules/rendering-animate-svg-wrapper.md | code pair | slop→good | Animating <svg> directly vs wrapper div (GPU) | skills/react-best-practices/rules/rendering-animate-svg-wrapper.md:12 |
| 43 | skills/react-best-practices/rules/rendering-svg-precision.md | code pair | slop→good | Over-precise SVG path coords | skills/react-best-practices/rules/rendering-svg-precision.md:12 |
| 44 | skills/react-best-practices/rules/rendering-content-visibility.md | code pair | good | content-visibility:auto for long lists (example only, no bad half) | skills/react-best-practices/rules/rendering-content-visibility.md:12 |
| 45 | skills/react-best-practices/rules/rendering-conditional-render.md | code pair | slop→good | `count && <X/>` renders stray "0" in UI | skills/react-best-practices/rules/rendering-conditional-render.md:12 |
| 46 | skills/composition-patterns/rules/architecture-avoid-boolean-props.md | code pair | slop→good | Boolean-prop-soup component (isThread, isEditing…) vs composition | skills/composition-patterns/rules/architecture-avoid-boolean-props.md:14 |
| 47 | skills/composition-patterns/rules/architecture-compound-components.md | code pair | slop→good | Monolithic Composer vs compound parts | skills/composition-patterns/rules/architecture-compound-components.md:14 |
| 48 | skills/composition-patterns/rules/patterns-explicit-variants.md | code pair | slop→good | Mode flags vs explicit variant components | skills/composition-patterns/rules/patterns-explicit-variants.md:14 |
| 49 | skills/composition-patterns/rules/patterns-children-over-render-props.md | code pair | slop→good | renderX props vs children composition | skills/composition-patterns/rules/patterns-children-over-render-props.md:14 |
| 50 | packages/react-best-practices-build/test-cases.json | code pair | slop→good | Fixture corpus: 69 bad + matching good snippets auto-extracted from all react-best-practices rules (mostly perf, not visual) | packages/react-best-practices-build/test-cases.json:1 |

## Best audit candidates
1. #2 app-router.vercel.app/view-transitions — live, real Vercel-built UI with intentional motion; good positive control for motion rules.
2. #1 next-app-router-playground/app/view-transitions — source of #2; lets the audit pair rendered screen with code.
3. #24 ui-styling.md font-size pair — explicit typography "slop vs good" claim; useful for testing whether Unslop agrees (one size + grey hierarchy is itself debatable).
4. #21 css-recipes.md — concrete motion tokens/keyframes incl. reduced-motion; test motion-duration/easing and a11y checks.
5. #23 SKILL.md "When to Animate" — explicit anti-gratuitous-animation stance; calibration text for motion-slop rules.
6. #40 rendering-hydration-no-flicker.md — theme flash anti-pattern; maps to dark-mode/FOUC checks.
7. #46/#47 boolean-props / compound Composer pairs — component-API slop typical of AI-generated UI code.
8. #26/#27 native menu & modal pairs — "custom JS widget instead of platform control" slop on mobile.
9. #45 `&&` rendering stray "0" — small visible UI bug class AI code commonly ships.
10. #5 web-interface-guidelines command.md — the actual 100+ rule set this repo audits with; cross-check against Unslop rule catalogue.

## Notes
- No in-repo HTML demos, templates, screenshots, or showcase galleries exist; design-relevant content is code snippets and Markdown rules.
- web-design-guidelines and writing-guidelines SKILL.md files are thin fetchers; their rules live in vercel-labs/web-interface-guidelines and vercel-labs/writing-guidelines (fetched command.md files contain no example-site URLs except Vercel AI Gateway/Sandbox doc links in writing-guidelines).
- Excluded as non-design: vercel-optimize (~100 vercel.com/nextjs/svelte/astro/nuxt doc links, CLI-output fixtures), deploy/CLI skills, example.com placeholders, and ~60 React perf code pairs with no visual surface.
- Liveness: #2 and #3 fetched OK via WebFetch; #5, #6 returned HTTP 200 via curl; GitHub tree URL #1 returned 403 to curl (repo confirmed via git ls-remote).
