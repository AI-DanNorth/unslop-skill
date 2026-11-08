# Unslop report: /home/claude/refs/huashu-design-en/assets/showcases/ppt/ppt-build.html

**Verdict (draft): fix**. Profile: balanced. 5 Floor finding(s) open.

## Four-line read

- **For:** _(synthesize writes this)_
- **Works and stays:** _(synthesize)_
- **Reads generated:** _(synthesize)_
- **Broken:** _(synthesize)_

## Score

| Dimension | Score | Note |
|---|---|---|
| Concept | _lens_ | judgment lens required |
| Hierarchy | _lens_ | judgment lens required |
| Craft | _lens_ | judgment lens required |
| Accessibility | 1 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 7 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (16x). html > body > div.container > div.top-row:nth-of-type(1) > div.eyebrow:nth-of-type(1)  "GLM-4.7 Open-Source Model"  
   Evidence: 2.16:1 against the background behind the text (10th-percentile pixel #fafaf8, worst 2.16:1; text #b0aca4, 10px; needs 4.5:1). APCA Lc 42 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-002 Text size floors** (9x). html > body > div.container > div.top-row:nth-of-type(1) > div.eyebrow:nth-of-type(1)  "GLM-4.7 Open-Source Model"  
   Evidence: 25-character run at 10px (hard floor 18px, dense UI 20px, body 24px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
3. **[Floor P0] A11-168 Never convey information by colour alone** (1x). accented GLM-4.7 values "95.7", "73.8%", "87.4" in the comparison rows  
   Evidence: The winning value and bar are marked only by terracotta rgb(212,165,116), 2.13:1 against the ground, so the highlighted values are also the least legible text in each row.  
   Fix: .comp-val.gold { color: #8a5a2b; font-weight: 600 } (about 5:1, plus weight as a second cue) (remedy: None)
4. **[Floor P0] A11-165 Large text, icons, focus rings, field edges, control boundaries, data marks.** (1x). comparison bars for Claude 3.5 and GPT-4o  
   Evidence: Comparator bars are thin light-grey lines on a near-white track (visible in 1920-00 at y 653 and 675), well under 3:1 against the track; the bar length is the data.  
   Fix: Bars at #767676 or darker, 4px+ thick, with the track removed or lightened (remedy: None)
5. **[Floor P0] INT-101 Never invent a metric, customer count, uptime, speed multiple, saving or percentage the us** (1x). comparison rows under each figure  
   Evidence: Comparator scores are implausible for the named models: "Claude 3.5 88.2" and "GPT-4o 83.6" on AIME 2025, when those models are publicly reported far lower on AIME. No source is given beyond "Benchmark Evaluation 2025 / Official Results" at 10px. The +7.5 to +20.5 margin in the insight line is derived from these figures.  
   Fix: [DATA NEEDED: sourced comparator scores with model version and evaluation date] and a visible source line, e.g. "Source: <report>, <date>" (remedy: None)
6. **[Reflex P1] CPY-005 No slop diction** (3x). html > body > div.container > div.title-area:nth-of-type(2) > div.subtitle:nth-of-type(2)  "First open-source model to achieve state-of-the-ar"  
   Evidence: "state-of-the-art" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
7. **[Reflex P1] A11-002 Text size floors** (3x). body > div.container > div.hero-data:nth-of-type(3) > div.metric-card:nth-of-type(1) > div.metric-name:nth-of-type(2)  "AIME 2025"  
   Evidence: label at 12px (label floor 16px; 22 such)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
8. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 9 distinct font sizes: 10, 11, 12, 13, 14, 28, 40, 48, 112 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
9. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > div.container > div.title-area:nth-of-type(2) > div.main-title:nth-of-type(1)  "Coding Capability"  
   Evidence: display text at 40px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
10. **[Reflex P1] INT-007 Stat bands need sources** (1x). body > div.container > div.hero-data:nth-of-type(3) > div.metric-card:nth-of-type(1) > div.metric-value:nth-of-type(1)  "957"  
   Evidence: stat band of 3 unsourced figures: 957, 738, 874  
   Fix: Cite each figure, use only supplied facts, or remove the band. (remedy: fix-copy)
11. **[Reflex P1] CPY-192 Make slide titles full declarative assertions, unique per slide** (1x). title area vs footer insight  
   Evidence: Failed T-GHOST-DECK / T-SO-WHAT: the title "Coding Capability Breakthrough." is a label any model launch could use (T-RIVAL-NAME holds for any vendor), while the assertion "open-source models can compete at the frontier ... margins of +7.5 to +20.5 points" is 13px grey text at the bottom-left.  
   Fix: Promote the claim to the title, e.g. "GLM-4.7 leads all three coding benchmarks by 7.5 to 20.5 points" (once the comparators are sourced) (remedy: None)
12. **[Reflex P1] SLP-001 No eyebrow labels above headings** (1x). top-left and bottom-right  
   Evidence: Wide-tracked uppercase micro labels: "GLM-4.7 OPEN-SOURCE MODEL" (10px, letter-spaced), "ZHIPU AI" preceded by a terracotta hairline rule, plus tracked caps metric names "SWE-BENCH VERIFIED". T-DELETION: the eyebrow repeats what the title and figures already say.  
   Fix: Drop the eyebrow; put "GLM-4.7" in the title and the source in a legible footer line (remedy: fix-typeset)
13. **[Reflex P1] SLP-012 Look-family cluster** (1x). hero figures and title period  
   Evidence: Terracotta (#d4a574) dot replaces the decimal point in "95.7", "73.8", "87.4" and ends the title "Breakthrough."; with the off-white ground and caps eyebrows this is 3 tells of the warm-paper family (terracotta_accent, eyebrows, near-cream ground) on one slide. The sweep did not cluster it because the display face is sans.  
   Fix: Plain decimals in the figure colour; spend the single accent only on the GLM-4.7 rows, where it encodes 'ours' (remedy: fix-quieter)
14. **[Finish P3] A11-110 Keep all words as real text in reading order** (1x). hero figures  
   Evidence: dom-1920 text for the first figure is "957" with the decimal point in a separate decorative span; if the dot span is hidden or styled as a glyph, the value is extracted as 957, not 95.7.  
   Fix: Keep the real '.' character in the figure's text and colour it via a span that stays in the text flow, or add aria-label="95.7" on the figure (remedy: None)
15. **[Finish P3] A11-103 Use landmarks and semantic elements** (1x). whole slide  
   Evidence: dom-1920: no heading elements; the title "Coding Capability Breakthrough." is div.main-title and metric names are divs; no landmarks.  
   Fix: <h1 class="main-title"> and <h2> for each benchmark name, so PDF export tags and screen readers get an outline (remedy: None)

1 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 0 type roles
- dead_band (LAY-004): skipped: disabled by profile
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: disabled by profile
- focus_ring (A11-003): skipped: disabled by profile
- targets (A11-004): skipped: disabled by profile
- headings_landmarks (A11-007): skipped: disabled by profile
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- phone_parity (ROB-002): skipped: disabled by profile
- overflow (ROB-003): skipped: disabled by profile
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Keyboard, focus and target checks skipped: fixed-canvas slide with no interactive elements (sweep disabled them by profile).
- a11y: Sweep text_floor hits (10-14px on a 1920 slide) checked against the tile: real, not disputed.
- a11y: Projection or PDF export not tested.
- slop: No 00-contract.md: the 'Build Studio Style' in the page title suggests a chosen house style, but no brief records it, so the warm-paper tells are treated as unchosen.
- slop: Benchmark figures for GLM-4.7 itself were not independently verified.
