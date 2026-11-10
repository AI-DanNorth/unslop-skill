# Live recapture with interaction and the live recorder (9 Nov 2026)

All 39 live sites in test set 1 were recaptured with interaction capture: transition frames, the live (real-time) motion recorder, and slowed-network actions. L28 ran with `--no-interact`. Every site was then swept with the detectors added since live round 1. The lens judgments from live round 1 are archived in `live-pre-recapture/`, and the score uses them unchanged. Full table: `live-recapture-calibration.md`.

## Result

Verdict agreement stays at **29 of 34** (L04 not verified). The same five sites are wrong as in `live-round-1-after-fixes.md`: L11, L15, L19, L20 and L21. One of them improved: L20 (a human control) moves from slop to borderline, because region-aware sweeping now leaves out its exhibit sections.

## Capture fixes the recapture forced

| Site | Failure | Fix |
|---|---|---|
| L11, L34 | A click opened a popup. Its request has no frame yet, so `req.frame()` threw inside the route guard and ended the capture. | The guard blocks a frameless navigation and logs it (`popup blocked`). |
| L29, L30 | The fonts pass waited 30 s for `load`, with no fallback. | The later passes (fonts, focus, fake-send, performance) use `goLoad`: they wait 45 s for `load`, then fall back to DOMContentLoaded and note it. |
| L36 | Hit the 900 s timeout, which `run_set.py` did not catch, so the whole run stopped. | `run_set.py` reports a timeout and moves on. Each item can set its own `timeout`; L36 is set to 1500 s and finishes in 366 s. |

## New detectors on the 20 good controls

Share of sites each detector fires on, by expected label:

| Detector | Slop | Good | Read |
|---|---|---|---|
| `nested_radius` | 43% | 5% (L20) | separates |
| `ai_sparkle` | 36% | 5% (L26) | separates. Cal.com puts a real Lucide `sparkles` icon on an AI nav link. The tell is genuine, even on a human site. |
| `motion_snap` | 7% (L09) | 0% | rare, clean |
| `unit_wrapped` | 7% (L10) | 0% | rare, clean |
| `near_tangent` | 21% | 10% (L19, L33) | weak. It is Finish tier, so it was left as is. |
| `mixed_icons` | 0% | 15% (L19, L25, L26) | stroke check only; see below |
| `invented_mark` | 0% | 0% | silent on live |

### Changes made on this evidence

- **`mixed_icons`, fill check:** `min_each` raised from 2 to 3. On Linear (L25) it fired on status glyphs (4 filled, 2 outline), a state convention. On the L06 footer it fired on social logos (2 filled, 3 outline). Neither is a mixed icon set. The seed now has 3 of each kind.
- **`mixed_icons`, stroke check:** unchanged. On L26 a 24 px folder at 1.75 px sits beside icons at 1.1 px. On L19 one 1.5 px glyph sits among 2 px ones. Scaled to rendered size, the weights still differ, so these hits are true but minor (Finish).
- **Reduced-motion Floor:**
  - The scale change now counts only when both axes change, so an accordion growing taller is a reveal, not a zoom.
  - Boxes under 24 px (`reduced_min_px`) are left out. On Carbon (L36), a 16 px chevron turning 180° in 110 ms grew its bounding box 41% mid-turn, which read as a zoom.
  - The slop Floors stay (L06, L07, L09: 12 to 57 px of movement under `reduce`). So do the L34 Ant Design dialogs, which move 240 to 302 px under `reduce` (a real failure).

### Motion checks that do not separate yet

| Check | Slop | Good |
|---|---|---|
| reduced_motion (Floor) | L06, L07, L09 | L34 (real) |
| duration (Reflex) | L07 | L18, L20, L23 |
| easing `ease` (Finish) | L06, L08 | L21, L23, L34, L36, L37 |
| layout (Reflex) | L07, L09 | L18, L23 |
| travel (Reflex) | none | L18, L23 |

Human sites use long showpiece transitions: L18 deals cards for 790 ms, and L20's tabs run 750 ms. They also use the browser's default `ease`. These checks change no verdict, so their thresholds were left alone. They are inputs for the motion lens, which can tell a showpiece from UI feedback, and are not reasons to tune on hit counts.
