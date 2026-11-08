# Unslop report: /home/claude/refs/huashu-design-en/assets/showcases/ppt/ppt-pentagram.html

**Verdict (draft): fix**. Profile: balanced. 3 Floor finding(s) open.

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (18x). html > body > div.left-col:nth-of-type(6) > div.model-tag:nth-of-type(1)  "Open-Source Model"  
   Evidence: 2.85:1 against the background behind the text (10th-percentile pixel #ffffff, worst 2.85:1; text #999999, 11px; needs 4.5:1). APCA Lc 55 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-002 Text size floors** (11x). html > body > div.top-bar:nth-of-type(1) > span.top-label:nth-of-type(1)  "Benchmark Report 2025 Coding Performance"  
   Evidence: 40-character run at 12px (hard floor 18px, dense UI 20px, body 24px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
3. **[Floor P0] INT-001 No invented metrics** (1x). left column key message and top bar  
   Evidence: 'First open-source model to achieve SOTA across all three major coding benchmarks' but the first benchmark is labelled 'AIME 2025 / Mathematical Reasoning', not coding; '#1 OPEN-SOURCE RANKING' is shown while the chart compares only against closed models (Claude 3.5, GPT-4o), so no open-source rival is on the slide. Source line is 'Benchmark data sourced from official evaluation reports, 2025' with no report named. Failed T-THREE-LINE (not falsifiable as stated).  
   Fix: "Leads Claude 3.5 and GPT-4o on AIME 2025, SWE-bench Verified and τ²-bench" and a footnote naming each report and date [DATA NEEDED: report citations; open-source comparison set if '#1' is kept] (remedy: fix-copy)
4. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 11 distinct font sizes: 11, 12, 13, 14, 15, 16, 18, 32, 48, 80, 200 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
5. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > div.left-col:nth-of-type(6) > div.model-name:nth-of-type(2)  "GLM-"  
   Evidence: display text at 48px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
6. **[Reflex P1] INT-007 Stat bands need sources** (1x). html > body > div.data-area:nth-of-type(7) > div.bench-col:nth-of-type(1) > div.bench-hero:nth-of-type(3)  "95.7"  
   Evidence: stat band of 3 unsourced figures: 95.7, 73.8, 87.4  
   Fix: Cite each figure, use only supplied facts, or remove the band. (remedy: fix-copy)
7. **[Reflex P1] A11-002 Text size floors** (1x). html > body > div.top-bar:nth-of-type(1) > span.top-label:nth-of-type(1) > span.red  "/"  
   Evidence: label at 12px (label floor 16px; 30 such)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
8. **[Reflex P1] A11-007 Headings and landmarks** (1x). slide structure  
   Evidence: No headings or landmarks in dom-1920.json (main:0); 'GLM-4.7' and benchmark names are divs, so an exported PDF or screen reader gets no reading structure; reading order puts the top-bar label before the model name.  
   Fix: <h1> for the slide title, <h2> per benchmark column; tagged PDF on export (remedy: fix-a11y)
9. **[Reflex P1] CPY-128 Say each fact once, where it does work** (1x). '95.7' in the left hero, the AIME column number, and the GLM-4.7 AIME bar  
   Evidence: T-DELETION: the 200px '95.7' hero and the 80px '95.7' AIME column header can each be removed without losing a fact; the same figure appears three times within 900px. The left hero also picks AIME, the one non-coding benchmark, as the lead number on a 'coding performance' slide. The columns then repeat 'big number + bar chart' three times, the stock data-slide shape SLD-136 warns against.  
   Fix: Make the hero the slide's argument (e.g. '+20.5 on SWE-bench Verified', the largest coding margin) and keep each benchmark's score once, on its bar (remedy: None)
10. **[Reflex P1] LAY-004 No dead bands** (1x). columns 2-4, y ~610-900 at 1920  
   Evidence: Between the '+x VS CLOSED-SOURCE BEST' lines and the summary row sits a ~290px empty band across all three benchmark columns (tile 1920-00); the left column is empty from y 560 to the footer.  
   Fix: Move the summary row up under the bars or enlarge the bars to use the height (remedy: fix-layout)
11. **[Finish P3] SLP-001 No eyebrow labels above headings** (1x). top bar, column heads and labels: 'BENCHMARK REPORT / 2025 CODING PERFORMANCE', 'OPEN-SOURCE SOTA' (x3), 'OPEN-SOURCE MODEL', 'AIME 2025 SCORE', 'BENCHMARKS WON'  
   Evidence: About 30 tracked-caps labels; 'OPEN-SOURCE SOTA' appears in the top-right, bottom-right and (as 'OPEN SOURCE') in the outline badge. T-LABEL-TRANSFORM: the badge and the second 'OPEN-SOURCE SOTA' lose nothing when removed.  
   Fix: Keep one instance (top bar); delete the badge and the footer repeat (remedy: fix-typeset)
12. **[Finish P3] SLD-128 Write every title as a full declarative assertion unique to the slide, never a topic label** (1x). T-GHOST-DECK on the slide title  
   Evidence: The only title is the label 'BENCHMARK REPORT / 2025 CODING PERFORMANCE'; the assertion lives in 16px grey body text. Read as a ghost deck, the slide says 'benchmark report', not what was found.  
   Fix: An assertion title: 'GLM-4.7 leads closed models on all three benchmarks' (if the claim survives the fix above) (remedy: None)

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
- a11y: Keyboard and focus: static slide with no controls (focus.json empty or irrelevant).
- a11y: Sweep text-size hits (11-16px against an 18px slide floor) agreed and not repeated.
- slop: Benchmark figures themselves were not fact-checked against external reports.
- slop: Only one slide captured; deck-level narrative (T-GHOST-DECK across slides) not possible.
