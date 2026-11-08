# Mined rules: D09 Motion & interaction, D10 Accessibility, D15 Robustness & performance

Source short names: hallmark, uupm (ui-ux-pro-max), huashu (huashu-design), taste (taste-skill), kami, adp (awesome-design-patterns), agent (agent-skills). Section numbers are the `## N.` numbers in each source file.

---

## D09 Motion & interaction

### Frequency gate and budget
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-001 | Name every motion and its purpose before building; cut any motion whose loss would go unnoticed if it were instant. | Purpose = clarify, guide or confirm (or spatial continuity) | Reflex | J | agent §1, hallmark §323, taste §408, huashu §324 |
| MOT-002 | Default to static; treat "most pages have too much motion" as the prior. A still direction runs nothing beyond functional state changes. | Static answer is usually right | Reflex | J | hallmark §323, §84 |
| MOT-003 | Cap motion primitives per page. | ≤3 primitives (one reveal, one hover signal, one functional loop); taste: exactly 3 layers (hero entrance once, 1 dealt moment (2 on pages of 8+ sections, never 3), hover/press layer) | Reflex | H | hallmark §323, taste §407, §441 |
| MOT-004 | Animate at most 1-2 key elements per view; one hero animation. | 1-2 per view | Reflex | H | uupm §7, §237 |
| MOT-005 | Never animate everything identically: identical fade-ups on every block are banned. | 0 uniform fade-up sets | Reflex | M | taste §33, huashu §364, §324 |
| MOT-006 | Never run two self-moving things in one viewport window or two loops in one panel. | ≤1 self-moving thing per 900px-tall window | Reflex | H | taste §431, §428 |
| MOT-007 | Make content complete and readable at rest, without script and under reduced motion; motion only adds to a whole page. | Final state in markup | Floor | M | taste §408, hallmark §84, §130, kami §684 |
| MOT-008 | Never use a loader, gate, intro or delay before reading. | 0 intro gates | Reflex | M | taste §427, §33 |
| MOT-009 | Never use Lottie (or an animation library) where CSS or SVG would do; prefer CSS and `@property` first. | CSS first; GSAP only when a timeline is the product | Reflex | H | hallmark §87, §280, taste §436 |
| MOT-010 | Keep the motion layer small. | ~4KB CSS + ~4KB JS gzipped; one IntersectionObserver per feature | Finish | M | taste §625 |
| MOT-011 | Declare one motion character for the system and scale all durations by it. | Severe 0.7-0.75x, Brisk 0.85-0.9x, Calm 1.0-1.3x, Still = nothing moves | Finish | J | hallmark §340 |

### Animatable properties and performance
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-020 | Animate only `transform` and `opacity` (colour on hover). | Never `width`, `height`, `top`, `left`, `right`, `bottom`, `inset`, `margin`, `padding`, `max-height`, `flex-basis`, `grid-template-columns`, `font-size`, `letter-spacing` | Floor | M | hallmark §4, §81, §437, uupm §13, §237, agent §219, taste §411, huashu §395 |
| MOT-021 | Never write `transition: all` / `transition-property: all`; list properties explicitly. | 0 occurrences | Floor | M | hallmark §4, §81, §437, huashu §364 |
| MOT-022 | Permit `clip-path`, `filter`, `mask`, shadow, `background-position` only when named deliberately inside a dealt moment and still smooth. | Background-position only on small text spans | Reflex | H | hallmark §81, taste §411, §624 |
| MOT-023 | Never `will-change` on a whole class; apply only to the active layer and remove after settle. | Per element, temporary | Reflex | M | hallmark §81, uupm §165 |
| MOT-024 | Collapse/expand without animating height: use `grid-template-rows: 0fr -> 1fr` or `scaleY` with top origin + opacity. | Never animate `height`/`max-height` | Reflex | M | hallmark §332, agent §220, taste §426 |
| MOT-025 | Move tab/segment indicators by transform (translate + x-scale), never `width`. | 220-240ms | Reflex | M | hallmark §332, taste §419, agent §35 |
| MOT-026 | Animations must never cause reflow or CLS. | CLS contribution 0 | Floor | M | uupm §237, taste §624 |
| MOT-027 | Never interleave layout reads (`getBoundingClientRect`, `offsetWidth`) with style writes in animation/move handlers; batch reads then writes. | No layout reads in move handlers | Reflex | H | agent §391, uupm §160, taste §437 |
| MOT-028 | Animate a wrapper `div`, not the SVG element itself (no GPU acceleration on SVG). | `<div class=spin><svg/></div>` | Finish | M | agent §386 |
| MOT-029 | Keep frame work within budget. | ≤~16ms/frame (60fps); input latency ≤~100ms; tap feedback within 80-150ms (visual within 100ms) | Reflex | M | uupm §233, §241 |
| MOT-030 | Never store scroll position in reactive state; throttle scroll events. | `scrollEventThrottle=16`; debounce/throttle scroll, resize, input | Reflex | H | agent §239, §240, uupm §142, §233 |
| MOT-031 | Fake depth with 2-3 shadow tiers instead of per-card real 3D + blur on many cards. | 48 cards with translateZ+blur drop <25fps | Finish | J | huashu §402 |

### Duration and easing tokens
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-040 | Route every duration and easing through shared tokens; never raw durations or bare `ease` keywords. | One token set globally | Reflex | M | hallmark §438, uupm §8, §237 |
| MOT-041 | Use a three-step UI duration scale. | micro 120ms (press, tick, colour), short 220ms (hover, tooltip, menu), long 420ms (modal, drawer, accordion, reveal) | Reflex | M | hallmark §83, §324, §438 |
| MOT-042 | Do not treat 150-300ms as a universal law; pick by distance, complexity, platform. | 150-300ms is a starting range | Reflex | J | uupm §8, §237 |
| MOT-043 | Use interaction-specific duration ranges. | Direct toggle 100-200ms; route slide 150-250ms; loading reveal 200-400ms; shared-element morph 300-500ms; micro 0.1-0.3s; UI transitions 0.3-0.8s | Reflex | H | agent §78, huashu §337 |
| MOT-044 | Never make core UI motion long or linear. | Native micro 150-300ms ease-out | Reflex | M | uupm §143 |
| MOT-045 | Ease out on arrival, ease in on exit, ease-in-out on toggles/travel, linear only for progress, spinners, loops and scroll scrubbing. | Never browser default `ease` | Reflex | M | hallmark §82, §342, uupm §14, §237, agent §80, huashu §335, taste §410 |
| MOT-046 | Default curves: exponential ease-out for UI arrivals. | ease-out `cubic-bezier(0.16,1,0.3,1)`; ease-in `cubic-bezier(0.7,0,0.84,0)`; ease-in-out `cubic-bezier(0.65,0,0.35,1)` | Reflex | M | hallmark §438, huashu §332 |
| MOT-047 | No bounce or overshoot on UI state. | Any cubic-bezier y control point >1.05 or <-0.05 fails; a declared playful spring may touch only the primary action + one character moment | Reflex | M | hallmark §82, §324, §438, taste §410, §443, uupm §160 |
| MOT-048 | Never let a fading element linger below 0.2 opacity; never leave a picture under 0.1 opacity after scroll. | 0.2 / 0.1 | Reflex | M | uupm §237, taste §643 |
| MOT-049 | Run opacity and translate on separate clocks in one declaration (short fade, longer move). | e.g. 210ms fade + 400ms slide | Finish | M | agent §81 |
| MOT-050 | Get structure working before tuning timing; keep ordinary cross-fades opacity-only; scope blur to the specific morph. | Mid-morph blur ≤3px at 30% | Finish | J | agent §82, §32 |

### Enter/exit asymmetry
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-060 | Exit faster than enter. | Exit = 60-75% of enter (65% typical); agent tokens exit 150 / enter 210 / move 400ms | Reflex | M | hallmark §83, §324, uupm §237, §162, agent §79 |
| MOT-061 | Delay the enter by the exit duration with `both` fill so the old state clears first, unless cross-fading for continuity. | `animation-delay: var(--duration-exit)` | Finish | M | agent §27, §79 |
| MOT-062 | Always pair an enter with an exit; otherwise the old view vanishes instantly. | Every enter has an exit or explicit `none` | Reflex | H | agent §51 |
| MOT-063 | Never leave a blank gap between outgoing and incoming content. | No pure-blank gap >0.3s | Reflex | M | huashu §377 |
| MOT-064 | Cap route exit; never block navigation on animation; preload destination before exit ends. | Exit ≤~250ms | Reflex | M | uupm §162, §163 |
| MOT-065 | Give overlay/wipe transitions a max-wait timeout so slow data never stalls them. | Timeout required | Reflex | H | uupm §163 |
| MOT-066 | Animate modals/sheets from their trigger source (scale+fade or slide). | Modal panel 0.96 -> 1 over long ease-out; close ~65% ease-in | Finish | J | uupm §237, hallmark §329 |

### Stagger
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-070 | Keep per-item stagger small and capped. | 30-50ms between rows; 60-100ms between blocks; total ≤500ms; once | Reflex | M | hallmark §83, uupm §237, huashu §342, §349 |
| MOT-071 | Do not stagger more than ~8 children; on long lists use tiny delay. | ≤8 children; long lists 20-40ms/item, never >100ms/item | Reflex | M | uupm §157, §159, hallmark §330 |
| MOT-072 | Never stagger on filtering or search updates; rows may fade in on first open only. | 0 stagger on filter | Reflex | H | hallmark §338, agent §43 |
| MOT-073 | Target stagger items by stable class/attribute, not array index; animate only mounted items in virtualized lists. | Stable keys | Finish | H | uupm §159, §974 |
| MOT-074 | Give entrances direction; never plain opacity 0->1 on every element. | translateY 8-16px (10px default) | Finish | M | huashu §349, §365, uupm §156, agent §28 |
| MOT-075 | Stagger exits by reading order when many leave; simultaneous disappearance reads as a crash (video/demo). | ≥0.4 frame by reading order | Finish | J | huashu §342, §422 |

### Page load and scroll choreography
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-080 | Allow at most one page-load reveal, staggered by DOM order, once, with content visible without it. | 0.4-0.8s total (hero entrance ~1.1s max in taste) | Reflex | M | hallmark §84, §339, taste §427, §33 |
| MOT-081 | Never give every section heading its own rise; never a second hero entrance. | 1 entrance per page | Reflex | M | taste §33, §459, §427 |
| MOT-082 | Never hide the hero picture or fade it in; it may only settle. | Photo scale 1.05 -> 1 over 1.1s | Reflex | H | taste §427 |
| MOT-083 | Default to no scroll-linked motion; at most one scroll-choreography pattern per page, on structure, never body text. | 1 pattern; targets = pinned section, one display element, 2px spine, figures | Reflex | H | hallmark §341, §444, taste §436 |
| MOT-084 | Never parallax text or photos; a block drifting off the scroll counts as parallax. | Drift >4px = fail (non-tech) | Reflex | M | hallmark §87, taste §436, §437, uupm §50, §165 |
| MOT-085 | Never scroll-jack, use smooth-scroll libraries, or steer scroll by script; no scroll listeners for motion. | Native scroll only | Floor | M | taste §436, §437, uupm §50 |
| MOT-086 | Put scroll choreography inside `@supports (animation-timeline: view())` and `@media (prefers-reduced-motion: no-preference) and (min-width: 40rem)`; base CSS shows the finished layout. | Static end state is default | Floor | M | hallmark §342 |
| MOT-087 | Declare `animation-timeline` and `animation-range` after the `animation` shorthand (shorthand resets them). | Order matters | Finish | M | hallmark §342 |
| MOT-088 | Use `linear` easing for scroll-scrubbed animation; a curve detaches the page from the thumb. | linear / scrub 0.5-1.5 | Reflex | M | hallmark §342, uupm §158 |
| MOT-089 | Fall back to reveal-once via IntersectionObserver, never a scroll listener or scrub polyfill. | `rootMargin: '0px 0px -20%'` | Reflex | M | hallmark §347, §339 |
| MOT-090 | Limit pinning. | ≤1-2 pinned sections per page; pin track `min-height: 280vh`; steps in `contain 5-30% / 30-55% / 55-80%` slices | Reflex | M | uupm §158, hallmark §343 |
| MOT-091 | Give pinned sections deterministic height; recompute triggers after images and fonts load; test on mid-tier mobile. | Recalc after load | Reflex | H | uupm §158 |
| MOT-092 | Dock sticky panes below any sticky nav and unstick them under the layout breakpoint. | `top: calc(var(--banner-height,0px)+var(--space-xl))`; static under 60rem | Reflex | M | hallmark §343, §346, §257 |
| MOT-093 | Scroll moments run back on the way up and show a finished state at both ends; text in them stays live at 4.5:1 at every step. | 4.5:1 at every frame | Floor | H | taste §436, §448 |
| MOT-094 | Never let a scroll moment move cards, pricing, FAQ, quotes or footer; never cut a word mid-move. | Whole blocks only | Reflex | J | taste §436, §442 |
| MOT-095 | An IntersectionObserver only mounts; never start/stop visible loops on scroll. | Loops start on load | Finish | H | taste §435, §437 |
| MOT-096 | Retired/banned scroll tells: progress bars as chrome, scroll-spy markers, scroll-tinted grounds, count-on-view, scroll-snap, card/row/tile reveals on scroll. | 0 (taste); hallmark allows a 2px progress spine hidden <40rem | Reflex | M | taste §33, §436, hallmark §345 |

### View transitions semantics
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-100 | Match transition type to meaning: shared morph = same thing deeper; directional slide = hierarchy or ordered sequence; cross-fade = lateral swap; enter/exit = appear/disappear; slide-up = data loaded; reorder = same items new arrangement. | Semantic mapping table | Reflex | J | agent §7-§14, §3 |
| MOT-101 | Never use directional slides on lateral or unordered navigation (falsely implies depth). | Tabs = cross-fade or none | Reflex | J | agent §8, §49 |
| MOT-102 | In ordered sequences, next enters from the right, previous from the left; mirror for RTL. | Forward left/up, back right/down | Reflex | J | agent §49, uupm §237, §364 |
| MOT-103 | Background revalidation and deferred updates never animate. | `default="none"` | Reflex | H | agent §4, §58, §83 |
| MOT-104 | Prefer native `document.startViewTransition`; unsupported browsers skip gracefully. Never call it yourself when the framework manages it. | Native API | Finish | M | agent §1, §15 |
| MOT-105 | Isolate persistent chrome (header, nav, sidebar, player) with its own unique name so it does not slide with page content. | `view-transition-name: none` is a no-op | Reflex | H | agent §67, §85 |
| MOT-106 | Disable the root cross-fade (live root) so hover/active styles keep rendering. | `::view-transition-old(root){display:none}` | Finish | M | agent §73 |
| MOT-107 | Use unique, ID-prefixed transition names; only one mounted element per name. | `photo-${id}` | Floor | M | agent §39, §98 |
| MOT-108 | Never pair a shared-element morph with a fading page exit (dissolves the source mid-flight). | Directional exit or none | Reflex | J | agent §45, §93 |
| MOT-109 | Use the text-morph recipe for large text size changes (raster scaling ghosts text); apply border-radius directly on captured elements. | Hide old snapshot, `object-fit: none` | Finish | J | agent §33, §46, §88, §89 |
| MOT-110 | One shared-element pair per navigation; verify it exists in both DOM states. | ≤1 pair | Reflex | H | uupm §164, agent §42 |
| MOT-111 | Keep reveals short: the overlay is fixed and snapshots do not scroll, and it captures pointer events. | Short; consider `::view-transition{pointer-events:none}` | Reflex | J | agent §62, §74, §76 |
| MOT-112 | Render elements present in both fallback and content outside the loading boundary to avoid an opacity dip. | No dip | Finish | J | agent §60, §92 |
| MOT-113 | Hide the old snapshot of `backdrop-filter` elements to avoid a flash; isolate floating popovers to avoid settle flicker. | | Finish | J | agent §70, §71, §86, §87 |
| MOT-114 | Avoid hash-fragment navigation during transitions; navigate then scroll programmatically. | | Finish | J | agent §76 |
| MOT-115 | Pad fixed-size lists to a constant slot count instead of morphing height when that is simpler. | | Finish | J | agent §66 |

### Hover, press, focus timing
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-120 | Gate hover motion to fine pointers; never use width to detect capability. | `@media (hover:hover) and (pointer:fine)` | Reflex | M | taste §413, hallmark §311, §258 |
| MOT-121 | Give every hover affordance a focus and tap equivalent; nothing is hover-only. | Parity 100% | Floor | H | hallmark §323, taste §413, uupm §11, §232 |
| MOT-122 | One hover signal per element, on the container, raising contrast. | Colour step, or 1-2px lift, or border step | Reflex | H | hallmark §85, §311, §440, taste §414 |
| MOT-123 | Never give a non-interactive element a hover state; every linked element visibly answers the pointer. | Answer within 350ms; linked card/photo with no change = fail | Reflex | M | hallmark §85, §440, taste §414, §420, uupm §33 |
| MOT-124 | Never apply the same hover lift/scale to every card. | Same scale on ≥2 selectors or lift on ≥3 = fail | Reflex | M | hallmark §440 |
| MOT-125 | Never scale or rotate an image on hover (hallmark); if allowed, zoom inside a fixed frame only. | taste: 1.02-1.03 inside frame, >1.05 warns, 600ms in / 400ms out | Reflex | M | hallmark §85, §440, taste §421 |
| MOT-126 | Never let a hover resize anything or push a neighbour; no tilt, skew, rotate, glow, shine sweep, cursor-follow, magnetic buttons, custom cursors. | Tilted card = fail | Reflex | M | taste §413, §420, §33, hallmark §87, §459 (taste) |
| MOT-127 | Cap hover distances. | Card lift 2px (>6px warns); subtle hover <2px displacement; arrow nudge 3px; menu drop 6px | Reflex | M | taste §412, §414, uupm §153 |
| MOT-128 | Never add a delay before a button reacts; hover slower than its token is a fault. | Hover 150ms in / 120ms out; press 90ms | Reflex | M | taste §409, §415, §33 |
| MOT-129 | Give a pressed state that does not change layout bounds. | 1px drop (`translateY(1px)`) and/or scale .95-.985 | Reflex | H | hallmark §325, §311, taste §415, uupm §34, §237, §241, agent §222 |
| MOT-130 | Always attach the reverse (leave) tween so hover never sticks. | | Finish | H | uupm §154 |
| MOT-131 | Focus rings appear instantly; never animate, fade or transition the ring property. | 0ms | Floor | M | hallmark §86, §325, §441, taste §422, §632 |
| MOT-132 | Tooltips: delay on hover, none on focus; stay while the pointer moves onto them; dismiss on Escape. | Hover 800-1000ms; focus 0; opacity over micro | Reflex | M | hallmark §86, §331, §442 |
| MOT-133 | Open hover menus after intent; open all columns together; close fast. | 150ms intent; 6px drop fade; close 120ms; menu items may stagger 30ms when ≤8 | Finish | H | taste §418, hallmark §330 |
| MOT-134 | Make state transitions cancellable; set final semantic state directly; never depend on `animationend`/`transitionend` for correctness. | Rapid toggles replace prior motion | Floor | H | uupm §16, §237 |
| MOT-135 | Animations are interruptible and never block input. | | Floor | H | uupm §237 |
| MOT-136 | Disable transitions during theme switch. | | Finish | M | uupm §338 |

### Microinteraction specs
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-140 | No toast for an effect already visible; toasts are for failures and invisible effects. | No celebratory toast | Reflex | J | hallmark §88, §323, §328, §446 |
| MOT-141 | Toast timing: one corner, in over long, dwell, out faster; pause on hover/focus; error toast with retry never auto-dismisses; never steal focus. | Dwell 4-6s (uupm 3-5s) | Reflex | H | hallmark §328, uupm §99, §238 |
| MOT-142 | Spinners: delay before showing, minimum on-screen time, beside the label; text past long waits. | Show after 150-300ms, keep ≥300ms; "Loading…" past 2s | Reflex | M | hallmark §95, uupm §168 |
| MOT-143 | Never flash elaborate loaders for sub-300ms waits; use skeleton for >1s; never a bare spinner for 10s+ (stream instead). | 300ms / 1s / 10s | Reflex | H | uupm §168, §233, §113, §133 |
| MOT-144 | Skeleton shimmer as one synced background-position sweep per group; kill on mount/unmount; pause off-screen/hidden tab; static under reduced motion. | 1200-1600ms loop | Finish | H | uupm §167 |
| MOT-145 | Copy-to-clipboard: swap the label/glyph, no toast. | "Copied" 2.5s (taste glyph 1.5-2s) | Finish | J | hallmark §334, taste §425 |
| MOT-146 | Number tick: real figures only, from previous value, locale formatted, announce final value only; final value in markup. | 400-800ms (count 1000ms, 1.2s max); never count a year, price or phone | Reflex | H | hallmark §333, taste §432, huashu §356 |
| MOT-147 | Drag to reorder: handle on hover and focus, ghost at 50%, 1px drop line, snap release no spring, arrow-key reorder + live announcement. | Snap over short ease-out | Reflex | H | hallmark §335 |
| MOT-148 | Optimistic update: change at once, roll back on failure with a persistent "Try again". | Rollback over short | Reflex | J | hallmark §323, §336 |
| MOT-149 | Search as you type: debounce, quiet waiting signal, announce count once after settle. | Debounce 250ms | Reflex | H | hallmark §337, uupm §109 |
| MOT-150 | Command palette opens instantly; highlight slides, rows never move; never animate rows on filtering. | Highlight over micro | Finish | J | hallmark §338 |
| MOT-151 | Undo over confirm for reversible actions; confirm + typed name for irreversible. | Undo window 5-10s | Reflex | J | hallmark §320, uupm §39, §238 |
| MOT-152 | Validation timing: never on the first keystroke. | See Conflicts (blur vs submit) | Reflex | H | hallmark §327, uupm §70, §136, §238, taste §67 |
| MOT-153 | Floating labels are a tell; the label sits above the field and never moves. | | Reflex | M | hallmark §326 |
| MOT-154 | Haptics only for confirmations and important actions. | Short pulses ~10ms | Finish | J | uupm §31, §232 |
| MOT-155 | Drag, swipe, pinch track the finger in real time; use a movement threshold before starting a drag. | | Reflex | J | uupm §237, §232 |
| MOT-156 | Remove the 300ms tap delay; contain overscroll where pull-to-refresh is unwanted. | `touch-action: manipulation`; `overscroll-behavior: contain` | Finish | M | uupm §29, §30 |

### Loops and ambient motion
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-160 | No infinite loop except a loader, one small loop, or one declared ambient loop. | Small loop ≤4s; ambient ≥8s; card loop cycle 2.5-4s (3.2s default) | Reflex | M | hallmark §87, uupm §12, §145, taste §428 |
| MOT-161 | Every loop stops off-screen, in a hidden tab, and under reduced motion. | | Floor | H | hallmark §87, uupm §167-§169, taste §629 |
| MOT-162 | Anything moving on its own past 5s carries a visible pause control (WCAG 2.2.2). | 5s; pause disc 32px, 12px from corner, never over copy | Floor | H | hallmark §87, §443, taste §434, §632, uupm §15, §231 |
| MOT-163 | Auto-rotating content, carousels, marquees, tickers pause on hover and focus; provide prev/next and play/pause; announce slide without moving focus. | | Floor | H | hallmark §87, §443, uupm §15, §169 |
| MOT-164 | Ban decorative attention loops: pulsing dots, twinkling, flicker, hue cycling, scrambled text, typing dots, block cursors after headlines, caret blinking past five beats. | Every change shows a state, step or real data | Reflex | M | hallmark §87, taste §33, §429 |
| MOT-165 | Seed loops on their finished picture; never show an empty frame; a reset dims and rewrites, never blanks. | Rest 600ms before first cycle; hold last 10-15% | Finish | J | taste §428 |
| MOT-166 | Never auto-advance tabs or slides without a stop control; avoid timed tabs. | | Reflex | M | taste §33, §419, uupm §15 |

### Reduced motion
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-170 | Every keyframe, transform transition, scroll effect and view transition has a `prefers-reduced-motion: reduce` fallback. | 100% coverage | Floor | M | hallmark §4, §130, §439, uupm §9, §50, agent §77, kami §684 |
| MOT-171 | Default global fallback: zero durations and delays, one iteration, `scroll-behavior: auto`. | 0.01ms durations; delay 0 (prevents blank gap from delayed enters) | Floor | M | hallmark §439, uupm §348, agent §77 |
| MOT-172 | Treat reduced motion as a state, not off: spatial motion collapses to a short opacity crossfade; colours, menus and functional state still change. | 150ms crossfade allowed | Reflex | H | hallmark §84, §323, taste §439 |
| MOT-173 | Under reduced motion, every reveal shows its end state; loops hold one frame; pause buttons hide; numbers show final text; tab indicators and switches jump. | | Floor | H | hallmark §84, taste §439, §632 |
| MOT-174 | Listen to the reduced-motion setting live; offer an in-app setting where the OS gives none. | Live listener | Reflex | M | uupm §974, §144 |
| MOT-175 | Also degrade motion on phones and slow networks: heavy canvases become stills, hover effects off on touch. | Phone = <640px or touch landscape <500px tall | Reflex | H | taste §439, §444, uupm §233 |

### Pitfalls catalogue (render/timeline)
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| MOT-180 | Measure layout only after fonts are ready, plus one animation frame. | `document.fonts.ready` + rAF | Reflex | H | huashu §379 |
| MOT-181 | Frame 0 / first paint is the complete initial state; no blank or loading first frame. | | Floor | M | huashu §380, §391 |
| MOT-182 | Disable immediate-render of visible from-states (phantom effects before their moment); use fromTo with both ends. | | Reflex | J | huashu §393, §394 |
| MOT-183 | Make render state a pure function of t; no timers spanning >1s, no runtime randomness on render path (seeded PRNG). | | Reflex | H | huashu §378, §396, §406 |
| MOT-184 | No infinite repeats in rendered output; compute finite count from duration. | ceil(D / period) | Reflex | M | huashu §397 |
| MOT-185 | Never end video/demo with a fade to black; abrupt cut and hold the last frame. | Hold 0.5-1s; end fade-out 0 | Finish | J | huashu §321, §355, §373 |
| MOT-186 | Leave a perceivable pause before key results. | ≥300ms (0.5s typical) | Finish | J | huashu §321, §350 |
| MOT-187 | Reveal machine-generated text in irregular chunks, not constant per-character; user typing is per character at human speed. | Chunks of 2-5 chars at 40-120ms; typing 3 frames/char | Finish | J | huashu §351, §414 |
| MOT-188 | Never move a demo cursor in a straight line. | Quadratic Bezier + ±2px tremor, ~1.1s | Finish | J | huashu §344 |
| MOT-189 | Focus switches dim AND blur non-focused elements; return blur to 0 before scene end. | Blur 4-8px; ≤24px on large elements | Finish | J | huashu §346 |
| MOT-190 | Zoom duration scales with log of zoom ratio; never less than 1.25x zoom. | 0.55 × |log2(z2/z1)|, clamp 0.30-0.94s | Finish | M | huashu §340, §341 |
| MOT-191 | Never draw fake player chrome (progress bars, timecode, chapter counters) in frame. | | Reflex | J | huashu §202, §385 |
| MOT-192 | Never start sound on page arrival; music only after a user play action. | | Floor | M | huashu §405, taste §440 |

---

## D10 Accessibility

### Document and semantics
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| A11-001 | Set `lang` on `html`, a `<title>` in the page's own words, a one-sentence meta description. | Required | Floor | M | hallmark §132, §477, taste §639, §68 |
| A11-002 | Heading levels step one at a time; one `h1`; size with CSS, never by level. | No skipped levels | Floor | M | hallmark §132, §406, uupm §43, §230, taste §631 |
| A11-003 | Use landmarks and semantic elements; no clickable `div` soup. | `nav`, `main`, `article`, `button`, `a` | Floor | M | uupm §46, §58, §342, §968 |
| A11-004 | Label a section by a real heading when labelled by an element. | `aria-labelledby` -> heading | Reflex | M | hallmark §482 |
| A11-005 | Provide a skip link as the first focusable element, hidden until focused. | Tab reaches it first | Floor | M | hallmark §478, uupm §49, §343, taste §471, §639 |
| A11-006 | No `tabindex` above 0. | 0 occurrences | Floor | M | taste §631, §639 |
| A11-007 | Pin `[hidden]` so display rules never re-show hidden elements. | `[hidden]{display:none !important}` | Reflex | M | hallmark §480 |
| A11-008 | Hide accessible-only text with a clipped 1px box, never `display:none`. | `clip-path: inset(50%)` | Reflex | M | hallmark §479, uupm §344 |
| A11-009 | Keep reading order and screen-reader order equal to visual order. | | Floor | H | uupm §230, §244 |
| A11-010 | Keep all words as real text in reading order; never bake words into images. | | Floor | M | taste §632, §20 (photos) |
| A11-011 | Revert split-text animations on cleanup so assistive tech gets original text nodes; reserve splitting for headlines. | Headline <~8 words | Reflex | H | uupm §161 |

### Names, roles, states, ARIA patterns
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| A11-020 | Every control has an accessible name; icon-only buttons get `aria-label` in the page language. | 100% named | Floor | M | uupm §44, §121, §344, taste §631, §639 |
| A11-021 | Every `svg`, `canvas` or CSS-art element carries `aria-hidden="true"`, an `aria-label`, a labelled ancestor, or SVG `title`. | 100% | Floor | M | hallmark §476, uupm §125 |
| A11-022 | Meaningful images get alt describing what they show; decorative `alt=""`; drawn mocks `role="img"` + `aria-label`; never "render"/"illustration" or prompt text in alt. | | Floor | H | uupm §42, taste §631, §632, hallmark §122, kami §763 |
| A11-023 | Expose correct state attributes: `aria-expanded` on menu/accordion triggers, `aria-pressed`/`aria-selected` matching the visible label, `aria-current` on the current page, `aria-sort` on sortable tables. | | Floor | M | uupm §58, §343, §240, taste §631, §567 |
| A11-024 | Prefer native controls; customise selects/checkboxes only when native keyboard and SR behaviour is kept. | Native `<select>`, checkbox with `accent-color` | Reflex | H | hallmark §317, uupm §234, agent §203 |
| A11-025 | Badges are static text; chips are buttons only when actionable. | | Reflex | J | uupm §106 |
| A11-026 | Combobox: listbox below without pushing content, `aria-expanded` mirrors it, arrows cycle, Enter selects, Escape closes. | | Floor | H | hallmark §317 |
| A11-027 | Interactive canvases/objects are focusable buttons with Enter/Space; slider-like reveals use arrows, Shift, Home, End. | | Floor | H | taste §632 |
| A11-028 | Native app elements expose roles/traits and accessibility labels. | `accessibilityRole`, `accessibilityLabel` | Floor | M | uupm §121-§123 |

### Keyboard and focus
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| A11-040 | Every function is operable by keyboard; tab order follows visual order; no traps. | 100% | Floor | H | uupm §45, §230, §967 |
| A11-041 | Every interactive element has a visible `:focus-visible` ring at 3:1 against what it is drawn over; never remove outline without replacement. | ≥3:1 (reported <2.95:1 fails) | Floor | M | hallmark §129, §312, §455, uupm §32, §230, §347, taste §631 |
| A11-042 | Default ring spec. | `outline: 2px solid var(--color-focus); outline-offset: 2px`; inset on inputs; ring 2-4px | Reflex | M | hallmark §312, §483, uupm §326, §53, taste §422 |
| A11-043 | Build the focus ring from `outline`, never a border change; reserve a transparent outline at rest so the ring appears without shift. | `outline: 2px solid transparent; outline-offset:-3px` | Reflex | M | hallmark §92, §315, §449 |
| A11-044 | Switch ring colour on coloured bands so it holds 3:1 there. | 3:1 per band | Floor | M | hallmark §483, §300 |
| A11-045 | Focus not obscured (AA): sticky headers, banners, chat widgets never fully cover the focused control. | `scroll-padding-top: var(--header-height)` | Floor | H | uupm §51, §231, taste §631, §639 |
| A11-046 | Treat focus appearance and fully unobscured focus as AAA; do not present them as AA. | 2px perimeter, 3:1 state contrast | Finish | J | uupm §52, §53 |
| A11-047 | Dialogs: native `<dialog>` + `showModal()`; trap focus, Escape closes, backdrop click and visible close; `inert` behind; first focus to first interactive element; return focus to trigger. | | Floor | H | hallmark §318, §329, uupm §343, §131 |
| A11-048 | Menus: Space/Enter opens, arrows move, Esc closes, Tab closes and moves on. Tabs: arrows navigate; panels labelled by trigger. | WAI-ARIA patterns | Floor | H | uupm §343 |
| A11-049 | Move focus to main content after route changes. | | Reflex | H | uupm §239 |
| A11-050 | Popovers never live inside an `overflow:hidden` ancestor that clips them; flip near edges. | Flip within 16px of edge | Reflex | H | hallmark §319, §330 |
| A11-051 | Return keyboard focus to the parent after embedded-player clicks; forward key events. | | Finish | J | huashu §404 |
| A11-052 | Preserve system and accessibility shortcuts; offer keyboard alternatives to drag. | | Floor | H | uupm §230 |

### Targets and pointer
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| A11-060 | Web pointer targets meet WCAG 2.5.8 minimum or a documented exception. | 24×24 CSS px | Floor | M | uupm §55, §231, §126 |
| A11-061 | Touch targets outside running text meet the comfortable size; expand small controls invisibly. | 44×44 CSS px (48px coarse pointer); pseudo-element `inset:-12px` | Reflex | M | hallmark §90, §313, §258, taste §631, §643, huashu §77 |
| A11-062 | Native platforms use their own minima; never collapse into one number. | iOS 44pt, Android 48dp | Floor | M | uupm §26, §126, §232 |
| A11-063 | Keep spacing between adjacent targets. | ≥8px; fail when <32px tall or <24px wide with another target <8px away | Floor | M | uupm §27, §127, §232, taste §643 |
| A11-064 | Every drag operation has a single-pointer and keyboard alternative (WCAG 2.5.7). | Move up/down buttons beside handles | Floor | H | uupm §54, §151, §231, adp §1, hallmark §335 |
| A11-065 | No gesture-only core actions; never override system gestures (swipe-back). | Visible control for every gesture | Floor | H | uupm §28, §150, §232 |
| A11-066 | Keep primary targets away from notch, Dynamic Island, gesture bar and screen edges. | | Reflex | H | uupm §232 |
| A11-067 | Disabled uses three channels: opacity, `cursor:not-allowed`, native `disabled` (or `aria-disabled` when it must stay focusable); never opacity alone; say why near the user's attention. | opacity 0.55 (uupm 0.38-0.5) | Reflex | M | hallmark §92, §311, §321, §449, uupm §35, §238, §327 |
| A11-068 | Keep read-only visually and semantically distinct from disabled. | | Reflex | J | uupm §238 |

### Forms a11y
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| A11-080 | Every field has a visible label above it; placeholder is never the label; `aria-label` alone is not a label. | Label 4-8px above | Floor | M | hallmark §314, §92, uupm §47, §68, §122, §238, taste §67 |
| A11-081 | Placeholders show a format, never an instruction. | e.g. `01 Jan 2026` | Reflex | J | hallmark §314, adp §2 |
| A11-082 | Errors: `aria-invalid="true"`, tied via `aria-describedby`, announced via `aria-live`/`role="alert"`; never colour alone. | | Floor | M | hallmark §311, §314, §481, uupm §48, §69, §329, §346 |
| A11-083 | Error copy says what broke, why, what to do, in one sentence; no "Oops", no exclamation marks. | "Enter an email address" | Reflex | J | hallmark §95, §314, uupm §69, taste §67 |
| A11-084 | Failed submit: focus an error summary (`role="alert"`, `tabindex="-1"`, links to fields) or the first invalid field; keep inline errors. | | Floor | H | uupm §120, §238, hallmark §92, taste §67 |
| A11-085 | Required fields carry `required`/`aria-required` and a visible word or asterisk, never colour alone. | | Floor | M | hallmark §314, uupm §73, §346 |
| A11-086 | Group related fields in `fieldset` + `legend`. | | Reflex | M | uupm §346, §238 |
| A11-087 | Every field has `name`, correct `type`, `inputmode`, `autocomplete`. | `autocomplete="email"` etc. | Reflex | M | hallmark §92, uupm §71, §72, §77, taste §67 |
| A11-088 | Never block paste; allow password managers and passkeys (WCAG 3.3.8). | | Floor | M | hallmark §92, uupm §119, §152, taste §67 |
| A11-089 | Do not ask for the same information twice in one process (WCAG 3.3.7). | | Reflex | J | uupm §78, §231 |
| A11-090 | Keep repeated help in the same relative place across pages (WCAG 3.2.6). | | Reflex | J | uupm §56, §231 |
| A11-091 | Provide show/hide password toggle. | | Reflex | M | uupm §74, §139 |
| A11-092 | Handle IME composition: ignore Enter while composing; keep Shift+Enter and a visible submit. | `isComposing` or keyCode 229 | Floor | H | uupm §79, §238 |
| A11-093 | Keep submit enabled at rest; disable only while the request is in flight. | | Reflex | H | hallmark §92, §314, taste §67, uupm §36 |

### Screen reader and live regions
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| A11-100 | Announce status with a polite live region; assertive/`role=alert` only for urgent errors. | `aria-live="polite"` `aria-atomic="true"` | Floor | M | uupm §345, §124, hallmark §481 |
| A11-101 | Announce changed counts as a full contextual phrase, one status region, without moving focus; never a bare number or competing badges. | `role="status"`: "3 items in cart" | Reflex | H | uupm §59, §231 |
| A11-102 | Announce search results once after debounce, never per keystroke; drag reorder moves announced. | | Reflex | H | hallmark §335, §337 |
| A11-103 | Mark loading regions `aria-busy="true"` with SR loading text. | | Reflex | M | uupm §95, §328 |
| A11-104 | Number ticks announce only the final value. | | Reflex | H | hallmark §333 |
| A11-105 | Label AI-generated content as AI. | Visible label | Floor | J | uupm §112 |
| A11-106 | Charts provide a table alternative and text summary of the key insight; tooltips keyboard-reachable. | | Floor | H | uupm §240 |

### Contrast floors
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| A11-120 | Body text contrast against its computed background. | ≥4.5:1 (or APCA Lc 60); taste body 7:1 on plain ground | Floor | M | hallmark §411, uupm §40, §230, huashu §74, §78, taste §643 |
| A11-121 | Large text, icons, focus rings, field edges, control boundaries, data marks. | ≥3:1 (Lc 45); large = 24px+, or 18px/18.66px+ at 700 | Floor | M | hallmark §411, §456, uupm §241, §330, §240, huashu §66 |
| A11-122 | Measure contrast against real pixels: over gradients/photos test darkest and lightest stops; composite semi-transparent text through ancestors. | Fail at any stop | Floor | M | hallmark §411, §454, huashu §66, uupm §242 |
| A11-123 | Error/success colours and status backgrounds meet text contrast. | 4.5:1 | Floor | M | uupm §238, §961 |
| A11-124 | Never convey information by colour alone; add icon, text or pattern. | | Floor | H | uupm §41, §230, §106, hallmark §311 |
| A11-125 | Check contrast separately in light and dark modes; never infer dark from light. | Both modes | Floor | M | uupm §242, §149, hallmark §303 |
| A11-126 | Button text never within 5% lightness / 0.05 chroma of its fill; define accent-ink ≥4.5:1 wherever accent fills. | <1.6:1 fails | Floor | M | hallmark §412 |
| A11-127 | Muted text on brand bands / effects / photos. | Text on effects 4.5:1 (display 3:1); reading text on brand bands 7:1 | Floor | M | taste §632 |
| A11-128 | Exempt deliberate low-contrast watermark labels only in dark cinematic video; enforce AA on informational output. | 16-40% opacity labels exempt only there | Reflex | J | huashu §392 |
| A11-129 | Scrim opacity: measure the composed scrim result; never reuse one opacity blindly. | | Reflex | M | uupm §242 |

### Forced colors, text scaling, zoom
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| A11-140 | Honour OS high-contrast / forced-colors themes; use system/theme colours that adapt; never hardcoded colours that vanish. | Test in high contrast | Floor | H | uupm §961 |
| A11-141 | Work at browser zoom 200% without loss; text reflows at narrow widths and user spacing overrides (WCAG 1.4.4/1.4.10/1.4.12). | 200% zoom; `line-height` unitless; no fixed-height text boxes | Floor | H | uupm §57, §349 |
| A11-142 | Never disable zoom in the viewport meta. | `width=device-width, initial-scale=1` | Floor | M | uupm §84, §235, adp §198 |
| A11-143 | Support system text scaling (Dynamic Type, fontScale) without truncation; never disable scaling globally. | Test largest text size | Floor | H | uupm §147, §230, §146 |
| A11-144 | Breakpoints in `rem` so they follow user font size. | Never px breakpoints | Reflex | M | hallmark §257 |

### Cognitive load and timing
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| A11-160 | Disclose progressively; never hide essential information or the next action. | | Reflex | J | adp §84, uupm §238 |
| A11-161 | Chunk long strings and auto-format inputs (phone, expiry). | | Finish | J | adp §168, §2 |
| A11-162 | Prefer recognition over recall: menus, autocomplete, confirmable defaults. | | Finish | J | adp §171 |
| A11-163 | Authentication avoids cognitive function tests unless an alternative exists (WCAG 3.3.8). | Passkeys / OAuth / paste OTP | Floor | J | uupm §119 |
| A11-164 | Multi-step flows show a step indicator and allow back; long forms autosave; confirm before dismissing unsaved work. | "Step 2 of 4" | Reflex | J | uupm §98, §238, adp §8 |
| A11-165 | Provide cancel/back escape routes in modals and flows; tours are skippable. | Skip + Back on every tour step | Floor | H | uupm §230, §108, §131 |
| A11-166 | Never use flashing, alarming colour or countdowns to pressure. | | Floor | J | adp §63 |
| A11-167 | Tooltips stay hoverable and dismiss on Escape (WCAG 1.4.13). | | Floor | H | hallmark §331 |
| A11-168 | Auto-dismiss timers pause on hover/focus; error messages never time out. | | Floor | H | hallmark §328 |
| A11-169 | Provide captions on video that speaks; pause controls on autoplay. | | Floor | H | hallmark §280, uupm §117 |

---

## D15 Robustness & performance

### Hostile and edge-case content, overflow
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-001 | No horizontal scroll at any width. | 320-1920 | Floor | M | hallmark §4, §256, §425, uupm §85, taste §84, §621, kami §168 |
| ROB-002 | Set `overflow-x: clip` on `html` and `body`, never `hidden` (breaks sticky); never `100vw`, use `width:100%`. | | Floor | M | hallmark §4, §260, §425 |
| ROB-003 | Never let an element run past a 375 screen hidden only by the clip; restack instead. | | Floor | H | hallmark §425 |
| ROB-004 | Image-bearing grid tracks use `minmax(0,1fr)`; flex/grid text children shrinkable (`min-width:0`). | Bare `1fr` with media = fail | Floor | M | hallmark §4, §426, uupm §107, §236 |
| ROB-005 | Display heads carry `overflow-wrap: break-word; min-width:0`; a word of 16+ characters overflows without them. | Never `anywhere` on heads (hallmark) | Floor | M | hallmark §4, §400, huashu §122 |
| ROB-006 | URLs, IDs, user content reflow with `overflow-wrap:anywhere`; never `word-break: break-all` on prose. | | Floor | M | uupm §236 |
| ROB-007 | No text painted under an opaque box, image or other text (sticky/fixed chrome excepted); nothing on phones under a fixed bar. | 0 overlaps | Floor | M | hallmark §131, §457, taste §84 |
| ROB-008 | Nothing crosses a section edge, is sliced, or peeks behind another. | | Floor | H | taste §84, kami §682 |
| ROB-009 | Give absolutely-positioned children a positioned anchor container. | `position: relative` on parent | Reflex | M | huashu §374 |
| ROB-010 | Drive grid column counts from data or auto-flow, never a fixed CSS number paired with a data constant. | | Reflex | J | huashu §376 |
| ROB-011 | Never stack two `position:sticky; top:0`; offset the second. | | Reflex | M | hallmark §427 |
| ROB-012 | Guard CSS-only radio tabs so the page never jumps. | Radios in flow at zero size or `preventScroll` | Reflex | M | hallmark §99, §428 |
| ROB-013 | Render conditionals with a ternary when the value can be a falsy number (stray "0"). | `{count > 0 ? … : null}` | Reflex | M | agent §387 |
| ROB-014 | Never leak raw Markdown, `{{PLACEHOLDER}}`, lorem ipsum, "Title Text" or prompt fragments into visible output. | 0 | Floor | M | kami §654, §683, uupm §104, huashu §71 |
| ROB-015 | Never ship a stand-in success state: a form with no endpoint says plainly nothing was sent; no `action="#"`. | "Nothing was sent; this form is not connected yet" | Floor | H | hallmark §93, §311, taste §67 |
| ROB-016 | Verify every glyph exists in the chosen fonts; draw metakeys as CSS boxes; no tofu. | Rare glyphs ␣ ⏎ ⌘ ⌥ | Floor | H | huashu §375, kami §708 |

### Truncation
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-020 | Prefer wrapping to truncation; when truncating, use ellipsis and an operable full-text path (not hover-only). | Clamp 2-3 lines + expand | Reflex | H | uupm §101, §107, §236, §335 |
| ROB-021 | Never truncate essential text: headings, actions, errors, safety text, distinguishing names. | | Floor | H | uupm §105, taste §84 |
| ROB-022 | Badge/chip labels stay on one line; wrap chip collections before shrinking; `+n` overflow is an operable disclosure. | `white-space:nowrap` + shrinkable label | Reflex | M | uupm §107, §235 |
| ROB-023 | Button labels and primary nav links never wrap at any width; shorten first, then nowrap, then collapse to menu under 60rem. | 320-1920; labels >24 chars at risk | Reflex | M | hallmark §90, §259, §407 |
| ROB-024 | Footer links, tabs, breadcrumbs wrap to at most two lines, only for a real phrase. | ≤2 lines | Finish | M | hallmark §90, §407 |
| ROB-025 | Sentence-case table heads never wrap. | | Finish | M | hallmark §96 |
| ROB-026 | Plan metric labels against column width; stack value over label whenever any label can wrap. | e.g. 4 cols/7mm gap -> 14-18 chars | Reflex | H | kami §658, §659 |
| ROB-027 | Reserve fixed boxes for animated/swapping text (counts reserve width, card story boxes fixed height, tab panels one fixed height). | | Reflex | H | taste §419, §430, §432 |

### i18n, RTL, CJK
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-040 | Use logical properties throughout. | `margin-inline-start`, `padding-block` | Reflex | M | hallmark §263, adp §264 |
| ROB-041 | Leave room for longer translated strings. | +30-40% | Reflex | H | hallmark §263 |
| ROB-042 | Check RTL: directional motion, marquees, parallax, kinetic text, carousels, charts and icons need mirroring or review. | | Reflex | J | uupm §247, §364 |
| ROB-043 | Keep one locale per document; no bilingual stacking. | | Reflex | J | kami §61 |
| ROB-044 | Keep facts, colour and spacing tokens identical across locale variants; only font stacks differ. | | Reflex | H | kami §692, §709 |
| ROB-045 | Fail generated multi-locale pages on missing keys; hreflang, canonical, locale metadata reflect the shipped set. | | Floor | M | kami §709 |
| ROB-046 | Order mixed-script font stacks so each script gets its intended face (see Conflicts for CJK-first vs Latin-first). | | Floor | H | huashu §127, kami §51, §630 |
| ROB-047 | Ship a CJK serif subset on the web (iOS has no Chinese serif); keep subset in step with copy including alt, aria-label, placeholder, data attributes. | WOFF2, regular + one heavier, unicode-range CJK + U+201C-201D, U+2026, swap | Floor | H | kami §52 |
| ROB-048 | Never accept a sans substitution for CJK body tuned for serif; judge by the family that actually drew the text. | Judge after ≥20 ideographs | Floor | M | kami §626 |
| ROB-049 | Treat a second CJK family as a split defect. | ≥3 chars and ≥5% of CJK text | Floor | M | kami §623, §627 |
| ROB-050 | No synthetic CJK bold; real weights only; `font-synthesis:none`. | | Floor | M | kami §575, §636, hallmark §297 |
| ROB-051 | Korean breaks between words (`keep-all` or joiners in rendered copy); words >16 chars stay breakable in narrow cells. | | Floor | H | kami §582, §631 |
| ROB-052 | Long CJK compounds in narrow cells wrap rather than overflow. | | Floor | M | kami §682 |
| ROB-053 | CJK leading higher than Latin. | Body 1.7-1.8 (prose 1.8; lists 1.75; meta 1.6); titles never <1.3 | Reflex | M | kami §54, §634, huashu §121, §77 |
| ROB-054 | CJK display sizes drop ~8-10%; remove uppercase and wide tracking from CJK labels; CJK headings 0 tracking. | | Finish | J | kami §578, §580, §54 |
| ROB-055 | Never fix CJK/Latin crowding with typed non-breaking spaces; use flex gap. | ~6pt gap | Finish | M | kami §633, §59 |
| ROB-056 | Use tabular, lining numerals for every compared number (prices, metrics, versions, tables, timers). | `font-variant-numeric: lining-nums tabular-nums` | Reflex | M | kami §58, hallmark §402, uupm §236 |
| ROB-057 | Code stacks append a CJK face so CJK comments render. | Mono first, CJK last | Finish | M | kami §584 |
| ROB-058 | Prevent descender clipping in language menus. | `line-height:1.35`, `min-height:32px` | Finish | M | kami §60 |
| ROB-059 | Use text fields, not native date pickers, for dates on non-English pages. | | Finish | J | taste §67 |

### Locale formatting
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-070 | No hard-coded date or number formats; use locale-aware formatting. | `Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat` | Reflex | M | hallmark §263, uupm §102, §103, §240, huashu §356 |
| ROB-071 | Hoist formatters to module scope; memoize on locale. | | Finish | M | agent §267 |
| ROB-072 | Use one currency, one unit system, one thousands-separator and percent style per surface. | | Reflex | M | kami §167, §653 |
| ROB-073 | Mark only legitimately differing locale/timezone values to suppress hydration mismatches; never bake `new Date()`/`Math.random()` into cached output. | | Reflex | M | agent §385, §309 |
| ROB-074 | Use the single ellipsis character and progress labels ending in it. | `Loading…`, `Saving…` | Finish | M | agent §155, §156, hallmark §403 |
| ROB-075 | Glue units and shortcuts with non-breaking spaces in Latin UI copy (not between words in Charter). | `10&nbsp;MB`, `⌘&nbsp;K` | Finish | M | agent §157, kami §59 |

### Core Web Vitals and asset budgets
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-090 | Field CWV poor bands at p75 per route, with ≥50 samples before acting; no data, no claims. | LCP >2500ms, INP >200ms, CLS >0.1 | Reflex | M | agent §278, §283, uupm §233 |
| ROB-091 | Lab thresholds for rendered audits. | FCP/LCP median WARN 2.5/4.5s, FAIL 4.5/8s; CLS WARN 0.1, FAIL 0.25; blocking time WARN 1.5s, FAIL 4s | Reflex | M | taste §621 |
| ROB-092 | Page weight budgets (WARN/FAIL). | Transfer 1500/3000 KiB; images 1200/2400 KiB; largest image 350/700 KiB; JS 450/900 KiB; CSS 120/250 KiB; requests 60/110 | Reflex | M | taste §621 |
| ROB-093 | Font budgets. | Families 2/3; files 4/6; bytes 160/320 KiB | Reflex | M | taste §621 |
| ROB-094 | Treat each (route, metric) as its own problem; diagnose LCP via TTFB + critical image, INP via long tasks/handlers/3P, CLS via dimensions, fonts, injected UI. | | Reflex | J | agent §279-§282 |
| ROB-095 | Every script has `defer` or `async`; third-party (analytics, chat, pixels, consent) loads after hydration; never chain trackers. | | Reflex | M | agent §382, §296, §297, uupm §65 |
| ROB-096 | Never render consent banners synchronously in head; ads, embeds, cookie banners reserve space or render out of flow. | | Reflex | H | agent §298, §291 |
| ROB-097 | Inline critical CSS; split code per route; lazy-load heavy rarely used UI; never lazy-load above-fold essential content. | | Reflex | H | uupm §62, §67, agent §292, §293 |
| ROB-098 | Virtualize long lists; use `content-visibility:auto` + `contain-intrinsic-size` for long off-screen repeats. | Virtualize ≥50 items | Reflex | M | uupm §140, §233, agent §227, §380 |
| ROB-099 | Report performance with observed numbers and ranges, never invented gains. | | Floor | J | agent §276 |
| ROB-100 | Cap WebGL: ≤4 live contexts per page; cap DPR (1.5 heavy); pause off-screen; dispose geometries/textures; never create a renderer per mount. | 4 contexts; ~1.5MP per canvas; heavy effects ≤30fps half-res | Reflex | M | taste §626-§629, uupm §981, §1083 |
| ROB-101 | Effect module loaded but never mounted is waste. | 1-2 WARN, 3+ FAIL | Finish | M | taste §621 |
| ROB-102 | Compress and lazy-load 3D; never ship huge textures. | Never 50MB textures | Reflex | M | uupm §118 |

### Images and media
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-110 | Every image declares `width`/`height` or `aspect-ratio`. | Missing: 1-3 WARN, 4+ FAIL | Floor | M | hallmark §470, §262, taste §621, §622, agent §288, uupm §233 |
| ROB-111 | Never lazy-load the LCP element; give it `fetchpriority="high"`; preload only one LCP candidate; preloaded poster for LCP video. | | Floor | M | hallmark §89, §472, taste §622, agent §284 |
| ROB-112 | Lazy-load and async-decode below-the-fold images (not in nav menus or tab panels). | Not lazy below fold: 1-3 WARN, 4+ FAIL | Reflex | M | hallmark §262, taste §621, §623, uupm §61 |
| ROB-113 | Serve responsive images with `srcset` + `sizes` at ≤2x shown width in AVIF/WebP; never native-resolution heroes to mobile. | Oversized >2.2x shown = WARN/FAIL; upscaled <0.75x warns; standard widths 960/1280/1920 | Reflex | M | taste §621, §622, hallmark §470, agent §285, uupm §60 |
| ROB-114 | File caps. | Hero ≤400 KiB; other photos ≤250 KiB | Reflex | M | taste §622, §623 |
| ROB-115 | Below-fold photos are `img`, not CSS backgrounds. | 1-3 WARN, 4+ FAIL | Reflex | M | taste §621, §622 |
| ROB-116 | Never ship a broken image or `img` without source; style broken-image state. | Natural width 0 = fail | Floor | M | hallmark §463, huashu §66, adp §256 |
| ROB-117 | Show a loading fill (alt-ground colour or low-quality colour placeholder) behind images. | ~24px colours placeholder | Finish | M | taste §622, §623 |
| ROB-118 | Autoplay video is always `autoplay muted loop playsinline` with `poster`; under 2 MB per 10s; WebM (AV1/VP9) then H.264. | | Floor | M | hallmark §89, §280, §473 |
| ROB-119 | Prefer click-to-play with `controls`, `preload="none"`, captions; stop off-screen. | | Reflex | M | uupm §117 |
| ROB-120 | Every WebGL piece shows a poster first and falls back to a still on missing WebGL2, lost context, shader failure or empty first frame. | Panel never empty | Floor | H | taste §630 |
| ROB-121 | Use relative asset paths inside the project; never `/Users/...` or `file://`; base64-embed for single-file delivery; inline engines when opened offline. | | Floor | M | kami §638, huashu §80, §388, §389, §115(S4) |
| ROB-122 | Supply raster at 2-3x print size. | A4 at 300dpi = 2480×3508 | Reflex | M | kami §637 |
| ROB-123 | Size slide/figure images with `width:100%` + `object-fit:contain` + `max-height` ceiling, never fixed height that clips. | | Reflex | M | kami §640, §641 |
| ROB-124 | Never crop away UI text, numbers or controls for aesthetics. | | Reflex | J | kami §646 |

### Font loading
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-130 | Use `font-display: swap` (or `optional`); never invisible text. | | Reflex | M | uupm §64, §233, hallmark §297, taste §624 |
| ROB-131 | Provide metric-matched fallbacks so swap does not reflow. | `size-adjust`, `ascent-override`, `descent-override`, `line-gap-override` | Reflex | M | hallmark §297, uupm §91 |
| ROB-132 | Load only used weights; preconnect to the host; preload only critical (regular + display) fonts. | | Reflex | M | hallmark §297, taste §624, uupm §233, agent §381 |
| ROB-133 | Self-host fonts where possible; list `local()` first. | | Finish | M | agent §289, adp §240 |
| ROB-134 | Never review or sign off a render showing a fallback face or missing stylesheet. | DejaVu/Bitstream Vera in a PDF = font did not load | Floor | M | hallmark §462, kami §624, §628, §629 |
| ROB-135 | Every locally referenced font file exists before rendering; keep a remote URL fallback; if output overflows, confirm the font loaded before editing content. | | Floor | M | kami §628 |
| ROB-136 | Generated decks keep the intended font after open/export (no silent Calibri/Aptos). | | Floor | M | kami §629 |
| ROB-137 | Never pull runtime web fonts inside print figures; declare CJK stack explicitly inside SVG. | | Reflex | M | kami §630, §584 |
| ROB-138 | Read client-only preferences (theme) with a tiny inline script before first paint; no wrong-mode flash. | | Reflex | M | agent §383, hallmark §301 |

### Network, error, empty and loading states
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-150 | Every data region has four states: loading (skeleton in shape), empty (what, why, one action), error (what broke + what to do), full. | 4/4 | Floor | H | hallmark §94, §321, uupm §96, §240 |
| ROB-151 | Every control ships eight states: default, hover, focus-visible, active, disabled, loading, error, success; preview them stacked. | 8/8 | Reflex | H | hallmark §91, §311, §448 |
| ROB-152 | State priority when overlapping. | disabled > loading > active > focus > hover > default | Finish | J | uupm §324 |
| ROB-153 | Loading state keeps label readable and width stable; spinner replaces the label in a button. | | Reflex | M | hallmark §311, §321, uupm §36 |
| ROB-154 | Reserve height for helper/error text so messages never shift layout; error replaces helper in same line. | `min-height: 1lh` | Reflex | M | hallmark §92, §316, §449 |
| ROB-155 | Keep input border width constant across states; reserve ~24px right-edge slot for clear/error/spinner. | | Reflex | M | hallmark §315, §316, §449 |
| ROB-156 | Request timeouts show feedback with retry; failures keep everything typed. | | Floor | H | uupm §238, taste §67 |
| ROB-157 | Provide offline messaging and degraded modes on slow networks. | Lower-res images, fewer animations | Reflex | J | uupm §233 |
| ROB-158 | Never ship a page whose script throws on load; check console. | 0 console errors | Floor | M | hallmark §462, huashu §66, §107 |
| ROB-159 | Any broken request fails the audit. | 0 | Floor | M | taste §621 |
| ROB-160 | Empty search: "No results" plus suggestions; never a blank screen or bare "0 results". | | Reflex | M | uupm §110, hallmark §321 |
| ROB-161 | Back navigation restores scroll, filter and input state; never silently reset the nav stack. | | Reflex | H | uupm §239, §129, §132 |
| ROB-162 | All key screens reachable by deep link/URL; every CTA, docs, help and locale link resolves. | | Floor | M | uupm §239, kami §709 |
| ROB-163 | Critical external-provider features have a fallback chain. | | Reflex | J | agent §324 |

### Hidden-content detection
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-170 | Never hide content at rest so it depends on script to appear; hide only under a script-added class, or animate from visible (`@starting-style`), or a self-running CSS animation ending at full opacity. | | Floor | M | hallmark §84, §445, §347, uupm §156 |
| ROB-171 | After load, no more than 30% of the page's text is still hidden; nothing stays hidden with reduced motion, an observer that never fires after 4s, or scripts off. | 30% / 4s | Floor | M | hallmark §445, taste §437 |
| ROB-172 | Hero words may hide only until script or a safety mark; then fade by CSS alone. | 700ms safety mark, 400ms fade | Reflex | M | taste §427 |
| ROB-173 | Required content counts only when visibly rendered. Hidden = `display:none`, `visibility:hidden/collapse`, `opacity:0`, `font-size:0`, `color:transparent`, `hidden`, `aria-hidden`, zero scale/matrix, translate beyond ~-2000, `content-visibility:hidden`, `filter:opacity(0)`, offsets/text-indent ≥100%/100em or ≥2000 units, `clip:rect(0,0,0,0)`, `clip-path: inset(50%)/inset(100%)/circle(0)`, zero-size replaced or overflow-clipped boxes, SVG `fill="none"`/`fill-opacity:0` or outside viewBox. | Detector list | Floor | M | kami §675-§679 |
| ROB-174 | Ambiguous visibility fails closed: avoid conditional rules, masks, URL filters, unresolved custom properties, imported sheets and complex selectors on required content; keep visibility custom properties defined once on root. | | Reflex | M | kami §680, §681 |
| ROB-175 | Never put required facts in SVG text or nested SVG viewports; close tags properly. | | Reflex | M | kami §681 |
| ROB-176 | Never hide on phones content shown on desktop. | ≥40 words shown at 1440 and hidden at 375 = fail (nav aside) | Floor | M | hallmark §133, §435 |
| ROB-177 | Never open a table on a phone with ≥2 columns off-screen; restack rows or pin the first column; keep naming and action columns in view. | 10 columns on a phone = redesign | Floor | H | hallmark §96, §261, §435, uupm §87 |

### Rendered-page checks and widths
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| ROB-190 | Sweep standard widths. | 320, 375, 414, 768, 1024, 1280, 1440, 1920 (hero alone at 375 and 1280); taste adds 390, 820; first-screen sweep 1280/1152/1024/896/768 | Floor | M | hallmark §256, §452, uupm §81, §334, taste §641 |
| ROB-191 | Check fold viewports. | 1280×800 (hero fits), 1440×900 (one screen), 1920×1080 (container holds) | Reflex | M | hallmark §152, §453, §424 |
| ROB-192 | Check both sides of each breakpoint, a tablet width, landscape, and every locale. | | Reflex | M | kami §168, uupm §244 |
| ROB-193 | Cap and centre the container at wide sizes; grids never gain columns at 1920; text block ≤1600px. | Container 1360-1520px | Reflex | M | hallmark §4, §424 |
| ROB-194 | Use `dvh`/`svh` for heights meeting mobile chrome; never `vh` on a hero; `min-h-dvh` over `100vh`. | | Reflex | M | hallmark §260, §420, uupm §235 |
| ROB-195 | Fold safe-area insets into gutters with `viewport-fit=cover`; fixed bars reserve padding so content is not hidden. | `--gutter: max(16px, env(safe-area-inset-left))` | Reflex | M | hallmark §260, uupm §148, §235, §243 |
| ROB-196 | Phone gutters and edges. | 16px gutter; running text never within 8px of the edge | Floor | M | hallmark §431, §257 |
| ROB-197 | Body text floors. | Web body ≥16px (hallmark/taste), never running text <12px, functional <11px; huashu floor 14px web / 24px decks / 36px phone long-form; mobile inputs 16px | Floor | M | hallmark §398, §133, huashu §74, uupm §83, taste §643, adp §260 |
| ROB-198 | Avoid nested scroll regions. | | Reflex | J | uupm §235 |
| ROB-199 | Container queries for widgets whose layout depends on their box. | | Finish | J | hallmark §133, uupm §331 |
| ROB-200 | Wait for animations to settle (~2s) before capturing; 2x device scale; fresh cache-busted renders scrolled to the section. | | Reflex | M | huashu §107, kami §168 |
| ROB-201 | Test transitions in a production build with a cold cache. | | Reflex | M | agent §55 |
| ROB-202 | Rasterize every page of print/PDF output and look before shipping. | 110 dpi review, 160 standard, 300 detail, 400 for double rectangles | Floor | M | kami §706 |
| ROB-203 | Never claim a rendered check passed when it did not run; a thumbnail is not a render. | | Floor | J | hallmark §153, huashu §106 |
| ROB-204 | Check interactions by clicking through or recording; static shots cannot show them. | | Reflex | J | huashu §107 |
| ROB-205 | Never use rgba borders or semi-transparent backgrounds in print output (double rectangles). | | Floor | M | kami §689, §690 |
| ROB-206 | Never combine a closed border <1pt with radius in print. | | Reflex | M | kami §662 |
| ROB-207 | Never use negative grid line numbers in print layouts. | `1 / -1` silently dropped | Reflex | M | kami §661 |
| ROB-208 | Never rely on SVG marker auto-orientation for print arrowheads; draw manual chevrons. | 8px arm | Reflex | M | kami §642 |
| ROB-209 | Use TrueType-outline Korean fonts in PDF; verify Korean visibility in more than one viewer. | Full fonts cost ~7MB/weight | Floor | H | kami §632 |
| ROB-210 | Video deliverable hard checks. | Duration ±2%, audio present, no black head/tail frames, −14 ±4 LUFS | Floor | M | huashu §110 |

---

## Named tests
| Name | How to run | Pass condition | Source |
|---|---|---|---|
| Purpose test | For each animation, state what it communicates in a few words; ask whether anything is lost if made instant. | Every motion has a named job; instant would lose something | agent §1, hallmark §323, taste §408 |
| Walk every path | For each row of the navigation map, confirm boundary mounts/unmounts, pairs form, fallbacks exist, chrome stays static. | No path with no animation or competing animations | agent §6, §100 |
| Rapid-toggle test | Click a compact control repeatedly mid-transition. | Final semantic state correct; no stuck intermediate | uupm §16 |
| Three-condition hidden-content test | Load with reduced motion, with an IntersectionObserver that never fires for 4s, and with scripts off. | All content visible in all three | taste §437, hallmark §445 |
| Hidden text ratio | After load, measure share of text nodes hidden. | ≤30% hidden | hallmark §445 |
| Phone parity check | Count words visible at 1440 but hidden at 375 (nav excluded). | <40 words | hallmark §435 |
| Focus by tabbing | Tab through every control from page top. | Skip link first; ring visible at ≥3:1 everywhere (fail <2.95); never under header | hallmark §455, taste §639 |
| Contrast against real pixels | Sample the actual rendered pixels behind text (darkest and lightest under gradients/photos). | 4.5:1 body / 3:1 large at worst stop | hallmark §454, §411 |
| Text-run floor scan | Find visible runs ≥28 chars outside caption/footer/small elements below body floor; count label runs below label floor. | 0 body runs; <3 label runs | huashu §66 |
| Slow mobile line test | Throttle to 1.6 Mbit/s, 400ms RTT; scroll photos into view. | No frame empty 1s after on-screen when >400KB or >2x retina width | taste §622 |
| Breakpoint sweep | Screenshot at 320/375/414/768/1024/1280/1440/1920 and read by eye before automated findings. | No sideways scroll, wrapping controls, overlaps, cut text | hallmark §452, §152, taste §641 |
| Three fold questions | 1280×800: hero content all inside? 1440×900: hero exactly one screen? 1920×1080: container holds? | All yes | hallmark §453 |
| CJK line-ending audit | Across 320-1600px in WebKit and Chromium, count non-last lines ending >1.2em short and any line-start punctuation. | 0 | kami §55 |
| Mixed-family CJK check | Inspect which family drew body glyphs (not embedded list), after ≥20 ideographs. | No second family drawing ≥3 chars and ≥5% | kami §626, §627 |
| Fallback-face check | Inspect embedded/drawn fonts. | No DejaVu/Bitstream Vera/Calibri/Aptos substitution | kami §624, §629, hallmark §462 |
| Rule 0 / control experiment | Before trusting a renderer, render a known-good file of the same kind. | Renderer reproduces known-good correctly | huashu §106 |
| Count check | Compare source text vs artifact text char-by-char after stripping whitespace; compare per-page element counts. | Equal | huashu §106 |
| Cold-cache production check | Build production, clear cache, exercise transitions. | Same animations as dev | agent §55 |
| Sparse-line flag | Flag blocks whose last line is <~13% of widest line; sparse blocks taller than ~1/4 viewport. | Reviewed, not auto-failed | kami §168 |
| Frame comparison | For animations, compare captured frames rather than lint (catches 1px jitter from layout tweens). | No integer-pixel snapping | huashu §395 |
| First-second-after-cut check | Inspect captured frames at key moments and the first second after every scene change. | No clipping, collisions, empty frames, phantom effects | huashu §201, §393 |
| Five-segment climax sketch | Sketch the climax frame of each Slow-Fast-Boom-Stop segment. | Five frames differ | huashu §343 |

## Conflicts
1. Easing curve: hallmark/huashu default ease-out `cubic-bezier(0.16,1,0.3,1)` (expoOut); taste uses `cubic-bezier(.2,.8,.2,1)` for UI and `(.22,1,.36,1)` for entrance settle. Pick one per system; both are non-overshoot.
2. Overshoot/spring: hallmark (y>1.05 fails) and taste ("no bounce anywhere") ban it in UI; huashu recommends overshoot `cubic-bezier(0.34,1.56,0.64,1)` for toggles and springs; uupm §237 says "prefer spring/physics-based curves". Proposed: ban in UI (Reflex), allow in video/demo films.
3. Duration tokens: hallmark 120/220/420ms; taste hover 150/120, press 90, menu 200/120; agent exit 150 / enter 210 / move 400; uupm theme tokens 150/200/300 and "150-300ms not universal".
4. Exit ratio: hallmark 60-75%, uupm 60-70%, hallmark toasts/modals 65%.
5. Scroll reveals: taste bans any card/row/tile reveal or stagger on scroll; hallmark allows one reveal-once per page; uupm offers scroll-reveal and stagger recipes. Stricter = taste; hallmark's one-reveal is the workable default.
6. Parallax: hallmark and taste ban; uupm §165-166 offers subtle background parallax (5-15%) on decorative layers only.
7. Image hover: hallmark bans image scale on hover; taste requires 1.02-1.03 zoom inside the frame on linked photos.
8. Press feedback: uupm/agent `scale(0.95)`; taste 1px down + scale .985; hallmark 1px drop only.
9. Field focus: taste §423 transitions the field focus ring over 140ms, while taste §422 and hallmark say rings never animate.
10. Accordions: taste bans accordions (FAQ always open); hallmark/agent give height-free accordion recipes.
11. Validation timing: hallmark validates on blur once touched, then on every input; uupm validates on blur, not per keystroke; taste validates on submit only.
12. Toasts: uupm auto-dismiss 3-5s and uses success toasts; hallmark uses no toast for visible effects, 4-6s dwell, error toasts persist.
13. Disabled opacity: hallmark 0.55; uupm 0.5 / 0.38-0.5.
14. Target size: WCAG AA web 24 CSS px (uupm insists on this as the conformance number) vs hallmark/taste 44px comfort and 48px coarse pointer. Proposed: 24 = Floor, 44 = Reflex.
15. Body contrast: WCAG 4.5:1 vs taste 7:1 for body on plain ground; kami social papers 8.8:1.
16. Body size floor: hallmark/taste 16px body; huashu 14px web floor; hallmark running text never <12px.
17. CJK line breaking: huashu recommends `line-break: strict` and `text-wrap: pretty` for Chinese; kami bans `line-break: strict`, `text-wrap: pretty/balance` and `keep-all` on Chinese/Japanese (early wraps on phones).
18. Mixed-script stack order: huashu puts Latin first then CJK; kami puts CJK first in PDF/SVG and a unicode-range CJK subset first on web (Latin first hands curly quotes/ellipsis to the Latin face). Context-dependent.
19. Reduced motion fallback: agent/uupm zero all durations; hallmark/taste keep a 150ms opacity crossfade and colour changes.
20. Pinning: uupm allows 1-2 pinned sections; hallmark one scroll pattern per page; taste ties pins to the dealt moment budget.
21. LCP: agent poor >2500ms field p75; taste lab WARN 2.5s, FAIL 4.5s.
22. Spinner timing: hallmark show after 150-300ms, hold ≥300ms; uupm native spinner for ops >300ms, skeleton for >1s; taste "Sending" after 300ms.
23. Test widths: hallmark 8 widths 320-1920; uupm 320/375/414/768/1024/1440; taste 1440/1024/820/768/390/320; huashu 1920×1080/1440×900/768×1024/375×667.
24. `overflow-wrap`: hallmark says `break-word`, never `anywhere`, on display heads; uupm says `anywhere` for URLs/IDs/user content. Compatible by element type.

## Theme-specific, keep in library
- taste dealt "moments" catalogue (photo chapters, picture develops, statement lights up, pinned chapters, counter rolls, marquee, giant type, letters assemble, line carries colour, iris, cursor spotlight, liquid type/hover) and the place-vs-tech eligibility pools (taste §441-§459).
- taste hero entrance choreography: h1 lines from word masks 700ms/line, 80ms apart, followers fade up 12px 520ms 60ms apart (taste §427).
- taste nav/underline drawing specs (1px line 4px under word, draws L-to-R) and tech switch knob 16px slide (taste §417, §424).
- hallmark progress spine, sticky diptych, scrub headline recipes (hallmark §344-§346).
- huashu film recipes: Slow-Fast-Boom-Stop, keynote/one-take/office scene recipes, camera language, logo morph, 3D tilt 8°/−4°, UI demo forms (huashu §343-§423).
- kami slides "no animation by default; fade only when meaningful" (kami §671).
- kami Chinese letter conventions (2em indent, justified) and per-template CJK size tables (kami §578, §581).

## Coverage notes
- Forced-colors/high-contrast is thin (only uupm §961); no source gives `@media (forced-colors)` or `prefers-contrast` specifics.
- RTL is thin: only logical properties and a mirroring caveat; no bidi isolation, numerals, or icon-flip lists.
- Hostile-content testing (very long names, emoji, empty strings, zero/huge counts) is implied (16-char word, +30-40% strings) but no source gives a fixture list; worth authoring.
- Cognitive accessibility comes only from pattern libraries (adp); WCAG 2.2 timing (2.2.1) and seizure thresholds (2.3.1) are missing.
- Native-app motion and a11y rules (agent RN, uupm app rules) were lightly sampled; deeper mining belongs in APP/IOS/AND domains.
