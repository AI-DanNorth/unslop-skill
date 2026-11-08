# Unslop report: /home/claude/refs/kami/site/assets/demos/demo-agent-slides.html

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

1. **[Floor P0] A11-002 Text size floors** (6x). html > body > section.slide.cover:nth-of-type(1) > div.cover-left:nth-of-type(1) > div.meta:nth-of-type(3)  "kami slides demo · A4 landscape · 8 slides"  
   Evidence: 42-character run at 13px (hard floor 18px, dense UI 20px, body 24px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
2. **[Floor P0] DVZ-127 Start bars and areas at zero, always** (1x). slide 5 'Density beats length', bar chart 'LOADING STRATEGY vs ACCURACY'  
   Evidence: The bar for 53% is about 95px tall and the bar for 85% about 195px tall (tile 1920-03): a 2.05x height ratio for a 1.6x value ratio. From the tick positions (85% at y195, 53% at y296, axis at y390) the implied zero sits below the axis, so the value axis starts near 23%, not 0.  
   Fix: Start the bar axis at 0% (ticks 0/25/50/75/100), or switch to a dot plot if the range must be zoomed (remedy: None)
3. **[Floor P0] INT-112 Never fabricate a data series** (1x). slide 5 chart and claim; slide 4 metrics row  
   Evidence: Failed T-THREE-LINE on sourcing: 'Flat loading 53% / Layered loading 85%' accuracy and 'Context Rot sets in around 300–400K tokens regardless of the model' have no source, benchmark or date anywhere on the slide or deck. The sweep flagged the slide-4 stat band (INT-007: 20 / 4 / 10x); the chart on slide 5 is a separate unsourced data series it did not flag.  
   Fix: [DATA NEEDED: benchmark name, model, task set and date for the 53%/85% figures and the 300–400K threshold] as a source line under the chart; otherwise label it 'illustrative' and draw it without numbers (remedy: None)
4. **[Reflex P1] SLD-135 List/matrix slides: never draw all N equal** (1x). slides 2, 4, 5, 6, 7 (body column)  
   Evidence: Every content slide uses the same recipe: mono eyebrow, serif title, one-sentence claim, then a numbered list of 3 or 4 points with blue numerals, plus a right-hand visual. The points are not sequential ('Control flow lives in the tools...', 'Workflow vs Agent...'), so the 1/2/3 numbering is decoration (SLP-002) and the rhythm never breaks across 5 slides (SLD-149).  
   Fix: Keep numbering only where order matters (slide 2 loop steps); turn one slide into a single big claim or a quote, and let slide 6's 'four kinds of memory' become a 2x2 or table (remedy: None)
5. **[Reflex P1] CPY-005 No slop diction** (14x). html > body > section.slide.cover:nth-of-type(1) > div.cover-left:nth-of-type(1) > div.sub:nth-of-type(2)  "Loops, harness, context, memory: what actually mov"  
   Evidence: "harness" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
6. **[Reflex P1] SLP-010 No template chrome glyphs** (10x). html > body > section.slide.cover:nth-of-type(1) > div.cover-left:nth-of-type(1) > div.meta:nth-of-type(3)  "kami slides demo · A4 landscape · 8 slides"  
   Evidence: template chrome (middot-chains): "kami slides demo · A4 landscape · 8 slides"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
7. **[Reflex P1] SLP-006 Vary container recipes** (1x). html > body > section.slide.cover:nth-of-type(1)  
   Evidence: one box recipe on 8 elements across 3 selectors (section.slide, section.slide.cover, section.slide.ending)  
   Fix: Differentiate by role: section, object, callout, well. (remedy: fix-layout)
8. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 20 distinct font sizes: 7.5, 8, 8.5, 9, 10, 11, 12, 13, 13.5, 14, 16, 16.5, 18.5, 20, 22.5, 24.5, 42.5, 50.5, 56, 69.5 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
9. **[Reflex P1] INT-007 Stat bands need sources** (1x). body > section.slide:nth-of-type(4) > div.metrics:nth-of-type(4) > div.metric:nth-of-type(1) > div.v:nth-of-type(1)  "20"  
   Evidence: stat band of 3 unsourced figures: 20, 4, 10  
   Fix: Cite each figure, use only supplied facts, or remove the band. (remedy: fix-copy)
10. **[Reflex P1] A11-002 Text size floors** (1x). body > section.slide:nth-of-type(2) > div.body-grid:nth-of-type(3) > div:nth-of-type(1) > div.callout  "If your loop keeps growing every sprint, you are f"  
   Evidence: 98-character run at 19px (hard floor 18px, dense UI 20px, body 24px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
11. **[Reflex P1] A11-007 Headings and landmarks** (1x). every content slide title (slides 2-7)  
   Evidence: Only the cover and the ending titles are h1; the titles 'Simple core, complex surroundings', 'One turn, traced', 'Harness wins over hardware', 'Density beats length', 'Put state outside the context', 'Pseudocode over syntax' are not heading elements (dom-1920 has no h2). Each slide is a <section> with no accessible name, so a screen-reader user cannot navigate slide to slide by heading.  
   Fix: <section aria-labelledby="s5-t"><h2 id="s5-t">Density beats length</h2>...; keep one h1 for the deck title (remedy: fix-a11y)
12. **[Reflex P1] A11-113 Every svg, canvas or CSS-art element carries aria-hidden="true", an aria-label, a labelled** (1x). svgs on slides 1, 2, 3, 5  
   Evidence: Four inline svgs carry the deck's key content (loop diagram, sequence diagram, accuracy chart). The capture records no role or accessible name for them, and the chart's values exist only as svg <text> fragments read out of order ('Accuracy 85% 53% 53% Flat loading 85% Layered loading' in bodyText).  
   Fix: <svg role="img" aria-labelledby="c5-title c5-desc"><title id="c5-title">Accuracy by loading strategy</title><desc id="c5-desc">Flat loading 53%, layered loading 85%</desc>; cover rings get aria-hidden="true" (remedy: None)
13. **[Reflex P1] SLD-128 Write every title as a full declarative assertion unique to the slide, never a topic label** (1x). slide 8 ending 'Protocol first. Then parallelism.'  
   Evidence: Failed T-GHOST-DECK: titles in order read as an argument (simple core, harness over hardware, density over length, state outside context, pseudocode over syntax) until the close, which concludes on 'parallelism', a topic no slide raises. The ending does not follow from the deck.  
   Fix: A close that restates the deck's actual through-line, e.g. 'Fix the harness before the model' (from slide 4 and the ending's own sub-line), or add the missing slide on parallelism (remedy: None)
14. **[Finish P3] A11-002 Text size floors** (6x). html > body > section.slide.cover:nth-of-type(1) > div.cover-left:nth-of-type(1) > div.sub:nth-of-type(2)  "Loops, harness, context, memory: what actually mov"  
   Evidence: 78-character run at 20px (hard floor 18px, dense UI 20px, body 24px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
15. **[Finish P3] CPY-005 No slop diction** (3x). html > body > section.slide.cover:nth-of-type(1) > div.cover-left:nth-of-type(1) > div.meta:nth-of-type(3)  "kami slides demo · A4 landscape · 8 slides"  
   Evidence: "landscape" (buzzwords/dead-metaphors, context)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)

4 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
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
- a11y: sweep A11-002 Floor hits on 17px list items and 13px cover meta: disputed in part: the deck is an A4-landscape page canvas (1123px), so 1920-slide floors over-penalise; 17px here is about 13pt at A4, acceptable for print but small for projection. Kept the diagram-text finding, which fails either way
- a11y: contrast: sweep could not verify (no background-only render); spot-check of mono running heads (#6b6a64 on warm paper) estimates about 5:1, passes
- a11y: keyboard: no focusable elements; slide navigation shell (keyboard paging) not present in the capture, not tested
- a11y: image-only aspects: none; forms: none
- slop: Sweep CPY-005 'harness' hits disputed: in agent engineering 'harness' is the literal technical term (CPY-147 literal trade use), not a buzzword
- slop: Look family: warm paper, serif display, mono eyebrows and numbering touch warm-paper-serif, but the deck declares itself a kami-system demo (cover meta) and uses navy, not terracotta; treated as a deliberate house style
- slop: Canvas: slides are A4 landscape (1123x794) rendered inside a 1920 viewport; the white right side is outside the deck and not judged
- slop: copy voice: no contract or speaker notes supplied
