# Stageshow (benjitaylor/skills): review for Unslop

Source: https://github.com/benjitaylor/skills, commit `299140f` (4 Nov 2026), MIT licence (Benji Taylor; the brand SVGs carry their own licences). The repo holds one skill, `stageshow`. Read 9 Nov 2026.

## What it is

Stageshow is a **generator**, not an auditor. It builds faux product UI for marketing pages in React: hero shots, feature cards, bento tiles and cursor demos. Around the generator sit four things Unslop can use:

1. **Written rules with numbers** (`references/craft.md`, `framing.md`, `motion.md`, `bento.md`, `annotations.md`): about 400 rules for a still frame, its framing and its motion.
2. **An in-page checker** (`scripts/film-checks.mjs`, 2,120 lines): about 55 named DOM detectors, plus a gate of 24 "lines that are never intentional" (`references/rehearse.md`).
3. **A motion recorder** (`scripts/jumps-core.mjs`, `motion-watch.mjs`). It records every element's box on every animation frame and reports one-frame snaps, drift between neighbours, hard clip edges, and things that appear with no entrance.
4. **Teaching pairs** (`teaching/`, `references/teaching.md`): the same scene twice, with exactly one fault on the bad side. There are 18 motion pairs, 13 detail stills, 9 whole scenes, 8 style faults and 6 details.

Its review method (`references/review.md`, `verify.md`) is close to Unslop's: a fresh reviewer who never sees the builder's reasons, findings that each cite a frame, and a handover that lists what was not checked.

## Where it overlaps with what Unslop already has

| Stageshow | Unslop today |
|---|---|
| "Could it be any product in its category?" (review.md) | `T-MIRROR`, `T-DEFAULT-AGENT` in lens-concept |
| Purple slop, glow, gradient text (teaching, Style) | `neon_violet`, `glow`, `gradient`, violet-gradient look family |
| Emoji as icons | `emoji_icons` detector, D03-SLP rule |
| Tracked capitals on labels | eyebrow and type checks |
| "Product captures and mockups" | 9 rows in `rules/D13-IMG.yaml` (no detector, and lens-imagery is not built) |
| Empty or gapped capture is "inconclusive", never a pass | "Capture must be honest" (CLAUDE.md) |

## What is new to Unslop

**Slop tells that no current rule or detector catches:**

- **AI shorthand:** a sparkle, wand or star icon as generic "AI" decoration, or a gradient "AI" chip. Today only the emoji ✨ is caught, not an SVG sparkle.
- **Invented mark:** a one-letter tile in a brand colour beside a real company's name (`detectInventedMark`).
- **Mixed icons:** filled and outline glyphs in one nav, list or toolbar, or a hand-drawn glyph whose stroke differs from its neighbours. Stageshow calls this "the first tell of generated UI".
- **The five ways a mockup fails** (SKILL.md): Too much, Wireframe, Boxed, Flat, Bland. AI landing pages very often put a fake dashboard in the hero, and nothing in Unslop judges it. This vocabulary fits lens-imagery.
- **Skeleton ladder:** a list where wordless bars outnumber real rows, which reads unfinished.

**Craft checks with thresholds** (Finish tier, measurable from the DOM):

- `near-tangent`: edges 1 to 3 px apart.
- `nested radius`: the outer radius should equal the inner radius plus the padding.
- `unit wrapped`: a stat's unit on its own line (pairs with `stat_band`).
- `tight inset`: words under 8 px from a card's edge.
- `uneven padding` and `uneven inset`.
- `onion skin`: translucent fills overlapping.
- `clipped glyph`.
- `fat row`, `loose list` and `empty pane`, which pair with `dead_band`.

**Motion checks** that Unslop's interaction capture does not yet record:

- **One-frame snap:** a box jumps more than 2 px between still frames.
- **Drift:** neighbours gliding on different curves.
- **Appears with no entrance, or vanishes with no exit.**
- **Content swap:** a label replaced in one frame instead of moving.
- **Anchor drift:** an open popover moving as its list changes.

**Method for verify-fix:**

- "Clearing a line by hiding, removing or marking the thing it points at is a bug." A verify-fix must reject a "fix" that hides the flagged element.
- "Ten runs, gate green, frame unchanged: stop. Fresh eye."
- Exit codes for the gate: 0 passed, 1 findings, 2 inconclusive, 3 unstable page. "No issues detected is not approval."

## Where each piece goes

| Phase / step | What to take | How |
|---|---|---|
| **Research (now, cheap)** | The rules in craft, framing, motion, bento and teaching | Add as source 21 (`research/sources/stageshow-rules-by-concept.md`) and mine rows into D03 slop, D07 layout, D08 components, D09 motion and D13 imagery with source ids. **Scope every framing and motion row to "product illustration / mockup"**, because the rules are written for marketing demos, not product UI. |
| **Conflict register** | Clashes this source creates | 0.8 to 1 s storytelling arrivals vs Unslop's UI duration rules (Stageshow agrees: "UI feedback stays as quick as the real product"). "Monospace never for a technical product's labels" vs sources that allow it. "Lucide deliberately, never reflexively" vs neutral sources. Each resolves by scope: illustration vs interface. |
| **Phase 1 detectors (next detector batch)** | `ai_sparkle`, `invented_mark`, `mixed_icons`, `near_tangent`, `unit_wrapped`, `nested_radius` | Re-implement as Python detectors over the DOM JSON; port the logic, not the code (it is tied to the `.ss-*` kit classes and stage pixels). `extract.js` must record more: SVG fill vs stroke and stroke width per icon, the icon's library class (`lucide-sparkles` and the like), and border radius and padding on nested boxes. Each needs a threshold, a curated card, a `data-seed` and a clean control. **Tier Reflex or Finish, never Floor.** The 148 Floor false positives in live round 1 came from exactly this kind of geometric check on real sites. |
| **Motion capture (CLAUDE.md step 3, before the live recapture)** | The `jumps-core` per-frame geometry recorder | Add to `interact.mjs`: during each recorded transition, sample element boxes per animation frame, then report snaps, drift, and appear or vanish with no transition into `motion.json`. `detectors_motion.py` reads it. Do this before recapturing the live set, so the recapture carries the evidence. |
| **Phase 2: lens-motion** | `motion.md` (Changing text and values; appear, travel, leave; Loops) and the 18 motion teaching pairs | Tests such as "every change moves", "nothing pops", "result follows press feedback", "a reset has a visible cause" and "a spinner turns before it is visible". Loop and story rules apply only to demo videos and hero animations. |
| **Phase 2: lens-imagery** | `framing.md` (20 rules, 17 layouts), the five failure modes, Icons and logos | A "product mockup" test block, used whenever a page shows faux UI: one hero, at most two satellites, crop only filler, no plate behind the window, no window floating with even margins, real words only on the subject, real icons from one set, real logos. |
| **Phase 2: lens-components** | `craft.md` Spacing and alignment, Type; `layout-core.mjs` control padding audit | Button-state, inset and alignment tests. |
| **Phase 2: verify-fix** | review.md, verify.md, the gate exit codes | The anti-hiding rule, the "stop after repeated green with unchanged frames" rule, and inconclusive as a separate outcome. Unslop's `not_investigated` already matches REHEARSAL.md's "Not checked". |
| **Evals: a new test set** | The teaching pairs and the 38 gold examples | Run the Stageshow playground (`npm run dev`, Node 20.19+) and capture `?capture=<name>` routes. Bad and good halves become a controlled set where one fault is the only difference: the cleanest calibration Unslop could have for the Style tells (purple slop, glow, capitals, invented icons, AI shorthand, onion skin, tiny text, over-detailed). The answer key goes only in the `set*.yaml` manifest. Gold examples are "made" controls for the mockup tests, but they are illustrations of an author's taste, not ground truth for product UI. |
| **Media** | Phone and window chrome conventions (Chrome and devices) | Feeds `media-app` and `media-social` (device frames, iOS banner proportions, nothing under the island). |

## What not to take

- The React kit, the examples as code, and the generator workflow: Unslop audits; it does not build.
- The brand SVGs: trademarks under separate licences.
- The product studies (Figma, Linear, Slack and others) as "good" controls. They imitate real products, so they test likeness, not taste.
- Thresholds as-is: they are in stage design pixels for a 720 × 340 frame. Re-derive each on Unslop's controls before it ships.

## Risks

- **Taste presented as rule.** Many rules are one designer's house style (two easing curves, 12 px insets, Lucide "never reflexively"). Mined rows should be Finish or advice, and conflicts go in the register.
- **Kit coupling.** Most detectors skip `.ss-*` classes or rely on the kit's structure. On arbitrary sites they will over-fire until they are re-tuned.

## Suggested order

1. Mine it as source 21 and add the conflicts. Half a day, no code risk.
2. Add the per-frame geometry recorder to `interact.mjs` before the live recapture (step 3).
3. Build the teaching-pair test set, so the next detectors have controls before they ship.
4. Build the detector batch (`ai_sparkle`, `invented_mark`, `mixed_icons` first) against that set and the 14 live human controls.
5. Fold the mockup tests into lens-imagery, the motion tests into lens-motion, and the anti-hiding rule into verify-fix, as each is built.
