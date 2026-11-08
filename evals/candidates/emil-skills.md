# emil-skills — real design/motion artifacts cited in emilkowalski/skills
Source: https://github.com/emilkowalski/skills (shallow clone at /home/claude/refs/emil-skills). Labels reflect how the repo presents each item; "inferred" = named without a URL. Repo paths are relative to the clone.

| # | URL or repo path | Medium | Label | Why notable (one line) | Source file:line |
|---|---|---|---|---|---|
| 1 | https://sonner.emilkowal.ski | component demo | good | Author's toast lib; held up as the model of cohesive easing/duration, transitions-not-keyframes, swipe in entry direction | README.md:60; skills/emil-design-eng/SKILL.md:559-577; skills/animation-performance/SKILL.md:20 |
| 2 | https://vaul.emilkowal.ski/ | component demo | good | Author's drawer; the reference iOS-sheet curve cubic-bezier(0.32,0.72,0,1)/500ms, momentum drag, velocity dismiss | skills/gestures/SKILL.md:12,70-81 |
| 3 | https://emilkowal.ski/ui/7-practical-animation-tips#4.-choose-the-right-easing | doc | good | Article with live interactive demos of ease-in vs ease-out on enter | README.md:33 |
| 4 | https://emilkowal.ski/ui/agents-with-taste | doc | good | Author's essay on agent slop; shows an interactive Linear logo built with Claude Code | README.md:37 |
| 5 | https://emilkowal.ski/ui/you-dont-need-animations | doc | good | Restraint thesis; embedded demos (Raycast-style command menu, Sonner, Linear marketing) | skills/remove-animations/SKILL.md:20; skills/find-animation-opportunities/SKILL.md:20 |
| 6 | https://emilkowal.ski/ | doc | good | Author's site; source of the distilled audit philosophy, many inline motion demos | skills/improve-animations/AUDIT.md:3 |
| 7 | https://animations.dev (inferred URL form) | doc | good | Author's course, the stated source of the review bar | skills/review-animations/SKILL.md:23 |
| 8 | http://aiforui.dev/ | web page | neutral | Author's "AI for Designers and Engineers" course landing page (live) | README.md:1 |
| 9 | https://aiforui.dev/skills | web page | neutral | Newsletter signup page for the skills | README.md:21 |
| 10 | https://skills.sh/emilkowalski/skills | gallery | neutral | Skills directory listing for this repo | README.md:7 |
| 11 | https://www.raycast.com (inferred) | app screen | good | Command palette with NO open/close animation, cited 5x as "optimal" for keyboard-triggered UI | skills/emil-design-eng/SKILL.md:79; skills/animate/SKILL.md:48; skills/remove-animations/SKILL.md:40; skills/improve-animations/AUDIT.md:16; skills/review-animations/STANDARDS.md:14 |
| 12 | https://linear.app (inferred) | web page | good | Author's former employer, named as experience base; essay praises Product Intelligence marketing animation as purposeful | README.md:13 (+ you-dont-need-animations article, spot-check) |
| 13 | https://vercel.com/dashboard (inferred) | app screen | slop | Dashboard tab indicator used Motion shared-layout anim and dropped frames during page load; fixed by CSS | skills/emil-design-eng/SKILL.md:509; skills/animation-performance/SKILL.md:114 |
| 14 | https://family.co (inferred) | app screen | good | Family wallet's drawer: list items enter/exit with tuned opacity + height | skills/emil-design-eng/SKILL.md:583 |
| 15 | Apple Dynamic Island (https://www.apple.com/iphone/ , inferred) | motion demo | good | Canonical "alive" morph; spring-driven size change in both dimensions | skills/emil-design-eng/SKILL.md:154; skills/animation-vocabulary/SKILL.md:50; skills/review-animations/STANDARDS.md:63; skills/choreograph/SKILL.md:84 |
| 16 | iOS Control Center (inferred, https://support.apple.com/guide/iphone/use-and-customize-control-center-iph59095ec58/ios) | motion demo | good | Modules "grow up and out toward your finger" — trajectory telegraphs end state | skills/apple-design/SKILL.md:151 |
| 17 | iOS overscroll rubber-banding (inferred, any iOS scroll view) | motion demo | good | Reference feel for boundary resistance/damping | skills/animation-vocabulary/SKILL.md:61; skills/emil-design-eng/SKILL.md:456 |
| 18 | iOS native sheet / push transition (inferred) | motion demo | good | Reference timing: sheet curve 0.32,0.72,0,1; push 350ms | skills/gestures/SKILL.md:72; skills/animate-expo/SKILL.md:137,149 |
| 19 | WWDC 2018 "Designing Fluid Interfaces" (https://developer.apple.com/videos/play/wwdc2018/803/ , inferred) | motion demo | good | Primary source of apple-design skill: interruptible, velocity-inheriting springs | skills/apple-design/SKILL.md:16 |
| 20 | WWDC 2020 "The Details of UI Typography" (https://developer.apple.com/videos/play/wwdc2020/10175/ , inferred) | doc | good | Source of optical sizing / tracking / leading rules | skills/apple-design/SKILL.md:228 |
| 21 | WWDC 2026 "Principles of Great Design" (developer.apple.com/videos, inferred) | doc | good | Source of the eight design principles used as reasoning names | skills/apple-design/SKILL.md:249 |
| 22 | https://www.embla-carousel.com (inferred) | component demo | good | Cited with Vaul as correct exponential-decay momentum in carousels | skills/apple-design/SKILL.md:139 |
| 23 | https://base-ui.com | component demo | good | Recommended primitives; exposes --transform-origin for origin-aware popovers | skills/pick-ui-library/SKILL.md:32; skills/improve-animations/AUDIT.md:53 |
| 24 | https://cmdk.paco.me | component demo | good | Recommended ⌘K palette | skills/pick-ui-library/SKILL.md:33 |
| 25 | https://input-otp.rodz.dev | component demo | good | Recommended OTP input | skills/pick-ui-library/SKILL.md:35 |
| 26 | https://github.com/pmndrs/leva | component demo | good | Recommended tweak/control panel GUI | skills/pick-ui-library/SKILL.md:36 |
| 27 | https://joshpuckett.me/dialkit | component demo | good | Alternative control panel (dial UI) | skills/pick-ui-library/SKILL.md:36 |
| 28 | https://motion.dev | doc | good | Recommended animation lib (springs, layout, exit) with demo gallery | skills/pick-ui-library/SKILL.md:42 |
| 29 | https://number-flow.barvian.me | motion demo | good | Recommended digit-transition component vs re-rendered text | skills/pick-ui-library/SKILL.md:43,82 |
| 30 | https://torph.lochie.me/ | motion demo | good | Recommended animated text morphing | skills/pick-ui-library/SKILL.md:44 |
| 31 | https://cobe.vercel.app | motion demo | good | Recommended lightweight WebGL globe | skills/pick-ui-library/SKILL.md:45 |
| 32 | https://github.com/vercel/satori | doc | good | Recommended OG-image renderer | skills/pick-ui-library/SKILL.md:46 |
| 33 | https://shiki.style | doc | good | Recommended syntax highlighting | skills/pick-ui-library/SKILL.md:47 |
| 34 | https://github.com/benjitaylor/liveline | component demo | good | Recommended real-time streaming chart | skills/pick-ui-library/SKILL.md:55 |
| 35 | https://recharts.org | component demo | good | Recommended general charts | skills/pick-ui-library/SKILL.md:56 |
| 36 | https://dndkit.com | component demo | good | Recommended drag-and-drop | skills/pick-ui-library/SKILL.md:64 |
| 37 | https://virtuoso.dev | component demo | good | Recommended virtualization | skills/pick-ui-library/SKILL.md:65 |
| 38 | https://zustand.docs.pmnd.rs | doc | neutral | State library (not visual) | skills/pick-ui-library/SKILL.md:71 |
| 39 | https://github.com/lukeed/clsx | doc | neutral | className utility (not visual) | skills/pick-ui-library/SKILL.md:72 |
| 40 | https://cva.style | doc | neutral | Variant styling utility | skills/pick-ui-library/SKILL.md:73 |
| 41 | https://github.com/pacocoursey/next-themes | doc | good | No-flash theme switching | skills/pick-ui-library/SKILL.md:74 |
| 42 | https://easing.dev/ | gallery | good | Recommended easing-curve reference with previews | skills/animate/SKILL.md:120; skills/emil-design-eng/SKILL.md:123; skills/review-animations/STANDARDS.md:37 |
| 43 | https://easings.co/ | gallery | good | Second recommended easing-curve gallery | skills/animate/SKILL.md:120; skills/emil-design-eng/SKILL.md:123 |
| 44 | https://docs.swmansion.com/react-native-gesture-handler/docs/components/reanimated_swipeable/ | doc | good | Reference swipe-to-delete row (RN) | skills/animate-expo/RECIPES.md:177 |
| 45 | https://docs.expo.dev/guides/keyboard-handling/ | doc | neutral | Keyboard-synced UI reference | skills/animate-expo/RECIPES.md:255 |
| 46 | https://docs.expo.dev/router/advanced/modals/#form-sheet-presentation | doc | good | Native form-sheet presentation reference | skills/animate-expo/RECIPES.md:335 |
| 47 | Sonner early version w/ CSS @keyframes enter (https://github.com/emilkowalski/sonner history, inferred) | component demo | slop | Keyframes restarted on interrupt, toasts jumped when a 2nd toast arrived | skills/gestures/SKILL.md:42; skills/emil-design-eng/SKILL.md:569 |
| 48 | Vaul early version w/ inherited CSS var drag (https://github.com/emilkowalski/vaul history, inferred) | component demo | slop | Drag lagged past ~20 list items due to inherited CSS variable recalculation | skills/gestures/SKILL.md:29; skills/animation-performance/SKILL.md:146 |
| 49 | Radix / shadcn/ui (https://www.radix-ui.com , https://ui.shadcn.com , inferred) | component demo | neutral | Listed only as stacks to inventory during audit; shadcn is a common AI-default baseline | skills/improve-animations/SKILL.md:42 |
| 50 | skills/prototype/PICKER.md | component demo | good | Verbatim spec (markup, CSS, keyboard) for a variant-switcher harness — buildable artifact | skills/prototype/PICKER.md:1-197 |
| 51 | skills/animate/RECIPES.md | motion demo | good | 14 code recipes (button press, popover, tooltip, modal, drawer, toast, hold-to-confirm, tab indicator, scroll reveal, drag-dismiss…) | skills/animate/RECIPES.md:9-313 |
| 52 | skills/choreograph/RECIPES.md | motion demo | good | Multi-element choreography recipes (stagger, crossfade in resizing container, shared layout carry) | skills/choreograph/RECIPES.md:5-238 |
| 53 | skills/animate-expo/RECIPES.md | motion demo | good | React Native recipes (bottom sheet, swipe delete, collapsing header, toast) | skills/animate-expo/RECIPES.md:87-367 |
| 54 | skills/emil-design-eng/SKILL.md (hold-to-delete code) | motion demo | good | clip-path 2s linear press / 200ms ease-out release reference interaction | skills/emil-design-eng/SKILL.md:419-429,591-601 |
| 55 | skills/break-ui/CATALOG.md | doc | neutral | Worst-case data catalogue (names, emails, URLs, counts, time, states) to stress any artifact | skills/break-ui/CATALOG.md:9-135 |
| 56 | ui-cheatsheet.md | doc | good | 11 problem→fix pairs (tabular-nums, scale 0.97, transform-origin, 65ch…) | ui-cheatsheet.md:1-16 |
| 57 | performance-cheatsheet.md | doc | good | 7 motion perf fixes (no transition: all, blur<20px…) | performance-cheatsheet.md:1-15 |
| 58 | skills/review-animations/STANDARDS.md + skills/improve-animations/AUDIT.md | doc | good | Target values usable as audit thresholds | STANDARDS.md:1-187; AUDIT.md:1-115 |
| 59 | https://example.com/workspaces/acme/projects/q3-launch/docs/9f8e7d6c5b4a?tab=comments&filter=unresolved | doc | neutral | Placeholder long URL test string, not a real artifact | skills/break-ui/CATALOG.md:40 |

## Best audit candidates
1. https://sonner.emilkowal.ski — good-motion baseline: toast stacking, swipe, interrupt retargeting.
2. https://vaul.emilkowal.ski — good gesture baseline: drawer drag, momentum, snap, iOS curve.
3. Raycast command palette — positive "no animation" case; tests that the auditor does not demand motion.
4. https://emilkowal.ski/ui/7-practical-animation-tips — side-by-side ease-in (slop) vs ease-out (good) demos.
5. https://emilkowal.ski/ui/you-dont-need-animations — restraint demos; calibration for over-animation flags.
6. https://number-flow.barvian.me — good number transition vs AI-default text re-render.
7. https://base-ui.com — origin-aware popovers; checks transform-origin rule.
8. https://family.co (inferred) — list enter/exit opacity+height choreography.
9. Vercel dashboard tab indicator (inferred) — documented real-world perf slop (main-thread layout anim).
10. https://cmdk.paco.me — command menu baseline to compare against animated AI-generated palettes.

## Notes
- Repo has no screenshots/HTML example pages; in-repo artifacts are code recipes and specs (rows 50-58).
- Explicit "bad" artifacts are only historical states (Vercel tab, early Sonner, early Vaul); generic slop patterns (fade-in every section, hover-scale cards, animated ⌘K) are described but not tied to sites.
- Spot-checks: aiforui.dev, animations.dev, two emilkowal.ski articles reachable; vaul.emilkowal.ski blocked by robots (not confirmed dead).
- pick-ui-library rows are "good" as recommended defaults; several (zustand, clsx, cva) are non-visual and low value for visual audits.
- Apple/WWDC URLs are inferred; WWDC 2026 session URL not verified.
