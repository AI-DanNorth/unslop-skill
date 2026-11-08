# Unslop report: /home/claude/refs/open-design/design-templates/html-ppt-pitch-deck/example.html

**Verdict (draft): fix**. Profile: balanced. 4 Floor finding(s) open.

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
| Integrity | 2 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (16x). body.tpl-pitch-deck > div.deck > section.slide:nth-of-type(1) > div.deck-footer:nth-of-type(4) > span:nth-of-type(1)  "Alex Rivera · Founder"  
   Evidence: 3.15:1 against the background behind the text (10th-percentile pixel #ffffff, worst 3.15:1; text #8a90ad, 12px; needs 4.5:1). APCA Lc 59 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-002 Text size floors** (6x). html > body.tpl-pitch-deck > div.deck > section.slide:nth-of-type(1) > p.kicker:nth-of-type(1)  "Demo Day · Batch W26"  
   Evidence: 20-character run at 14px (hard floor 18px, dense UI 20px, body 24px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
3. **[Floor P0] INT-001 No invented metrics** (2x). slide 'TRACTION' title vs its data  
   Evidence: Title '6 months, growing 34% MoM.' but the bars read $8k, $15k, $23k, $36k, $55k, $81k: month-over-month ratios 1.88, 1.53, 1.57, 1.53, 1.47, a compound rate of about 59% MoM, not 34%. Failed T-THREE-LINE: the claim is falsifiable and the slide falsifies it.  
   Fix: State the rate the data supports ('$8k to $81k MRR in 5 months, ~59% MoM') or correct the series [DATA NEEDED: actual monthly MRR] (remedy: fix-copy)
4. **[Floor P0] A11-006 Controls have accessible names** (1x). deck navigation  
   Evidence: focus.json is empty: no focusable element on a 10-slide HTML deck. If the deck pages by arrow keys there is no visible or focusable control and no announced slide change; the '1 / 10' counter is plain text.  
   Fix: Prev/next <button>s with aria-labels and an aria-live="polite" slide counter (remedy: fix-a11y)
5. **[Reflex P1] SLP-007 No stock gradient pairs** (21x). html > body.tpl-pitch-deck > div.deck > section.slide:nth-of-type(1) > div.cover-blob:nth-of-type(2)  
   Evidence: gradient hue span 50°: #3b5bff, #7a46ff, #d94cff  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
6. **[Reflex P1] SLP-010 No template chrome glyphs** (14x). html > body.tpl-pitch-deck > div.deck > section.slide:nth-of-type(2) > span.section-num  "01"  
   Evidence: template chrome (numbering-tokens): "01"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
7. **[Reflex P1] SLP-001 No eyebrow labels above headings** (8x). html > body.tpl-pitch-deck > div.deck > section.slide:nth-of-type(1) > p.kicker:nth-of-type(1)  "Demo Day · Batch W26"  
   Evidence: 14px label tracked 0.08em caps above 86px heading "The design toolbuilt for the ."; 8 on page, budget 2  
   Fix: Promote the fact into the heading or delete the label (T-EYEBROW). (remedy: fix-typeset)
8. **[Reflex P1] LAY-003 Headings sit with their content** (8x). html > body.tpl-pitch-deck > div.deck > section.slide:nth-of-type(1) > h1.h1.anim-fade-up  "The design toolbuilt for the ."  
   Evidence: 14px above the heading but 37px below it: it reads as part of the block above  
   Fix: Increase space above headings; reduce space below. (remedy: fix-layout)
9. **[Reflex P1] INT-002 No default cast or fake brands** (2x). div.deck > section.slide:nth-of-type(8) > div.grid.g3 > div.card.team-card:nth-of-type(3) > h4  "Sam Okafor"  
   Evidence: "Okafor" (default-names/default-cast, cap budget 0, found 2)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
10. **[Reflex P1] INT-007 Stat bands need sources** (2x). div.deck > section.slide:nth-of-type(5) > div.grid.g3 > div.metric:nth-of-type(1) > div.n:nth-of-type(1)  "41M"  
   Evidence: stat band of 3 unsourced figures: 41M, $92B, 38%  
   Fix: Cite each figure, use only supplied facts, or remove the band. (remedy: fix-copy)
11. **[Reflex P1] MOT-001 Motion CSS hygiene** (2x). .progress-bar > span  
   Evidence: transition on a layout property: "width .3s var(--ease)"  
   Fix: Animate transform or opacity instead (remedy: fix-motion)
12. **[Reflex P1] SLP-012 Look-family cluster** (2x). whole page  
   Evidence: saas-card-kit: 3 of 5 tells (card_kit (card kit detector); equal_grid (grid 549.328px 549.328px 549.328px); inter_only (Inter)); cluster minimum 3  
   Fix: Break the family on its strongest tell first; name the replacement decision. (remedy: fix-quieter)
13. **[Reflex P1] SLP-004 No side-tab accent borders on cards** (1x). body.tpl-pitch-deck > div.deck > section.slide:nth-of-type(6) > div.grid.g3 > div.card.card-accent:nth-of-type(2)  
   Evidence: 3px top border, others ≤1px, radius 20px  
   Fix: Use grouping, a heading or one surface change instead. (remedy: fix-quieter)
14. **[Reflex P1] SLP-005 No uniform card kit** (1x). body.tpl-pitch-deck > div.deck > section.slide:nth-of-type(2) > div.grid.g3 > div.card:nth-of-type(1)  
   Evidence: 13 containers share radius 20px and shadow "rgba(20, 25, 60, 0.08) 0px 14px 40px 0px, rgba(20, 25, 60, 0"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
15. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 14 distinct font sizes: 12, 13, 14, 16, 22, 28, 32, 44, 56, 62, 72, 86, 180, 220 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)

9 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- dead_band (LAY-004): skipped: disabled by profile
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: disabled by profile
- focus_ring (A11-003): skipped: disabled by profile
- targets (A11-004): skipped: disabled by profile
- headings_landmarks (A11-007): skipped: disabled by profile
- phone_parity (ROB-002): skipped: disabled by profile
- overflow (ROB-003): skipped: disabled by profile
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Live keyboard paging (arrow keys) not tested.
- a11y: Sweep text-size hits (12-16px on a 1920 canvas) agreed and not repeated.
- slop: Only 6 of 10 slides were captured as tiles (doc height 10800px); slides 7-10 judged from text only.
- slop: Whether the team members are real people: names and bios not verifiable; sweep flagged a default-cast surname.
