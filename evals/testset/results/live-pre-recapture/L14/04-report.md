# Unslop report: https://impeccable.style/antipattern-examples/new-slop-2026.html

**Verdict (draft): fix**. Profile: balanced. 6 Floor finding(s) open.

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
| Integrity | 8 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-002 Text size floors** (1x). main > section.hero:nth-of-type(1) > div.hero-copy:nth-of-type(1) > span.fine-print  "NO CREDIT CARD. NO BS. JUST BETTER WORK."  
   Evidence: 40-character run at 10px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
2. **[Floor P0] ROB-003 No horizontal overflow** (1x). div.dashboard-wrap:nth-of-type(2) > div.sticker:nth-of-type(2)  
   Evidence: page is 384px wide at a 375px viewport (sideways scroll); widest culprit 120px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
3. **[Floor P0] A11-011 Reduced motion respected** (1x). black ticker band under the hero (main > div.ticker), all widths  
   Evidence: Continuously scrolling marquee '✦ WORK SMARTER ✦ SHIP LOUDER ✦ BREAK THE MOLD ✦ MAKE BIG MOVES' (tile 1440-00 shows it cut mid-word 'K SMARTER') with no pause control; it runs alongside the hero and features.  
   Fix: Add a pause button (or pause on hover/focus) and stop the animation under @media (prefers-reduced-motion: reduce). (remedy: fix-motion)
4. **[Floor P0] A11-110 Keep all words as real text in reading order** (1x). ticker band  
   Evidence: dom-1440.json: the ticker's 8 spans are real text with no aria-hidden, so the four slogans are read twice in a row ('✦ WORK SMARTER ... ✦ WORK SMARTER ...'), including the ✦ glyph each time.  
   Fix: aria-hidden="true" on the duplicated half (or the whole decorative ticker) and on the ✦ glyphs. (remedy: None)
5. **[Floor P0] A11-112 Every control has an accessible name** (1x). nav 'How it works' and hero CTAs  
   Evidence: focus.json: 'How it works', 'LET'S GO ↗' and 'START MAKING MOVES ↗' all go to #workspace (the decorative window mock); 'SHOW ME HOW' goes to #features. Labels do not describe the destination, and the ↗ arrow (usually 'opens elsewhere') is read aloud as 'north east arrow' on in-page anchors.  
   Fix: Name the real destination ('Start a free trial') and link to it; wrap the arrow in <span aria-hidden="true">. (remedy: None)
6. **[Floor P0] INT-005 No placeholder residue at ship** (1x). nav and hero CTAs  
   Evidence: 'How it works', 'LET'S GO ↗' and 'START MAKING MOVES ↗' all link to #workspace, which is the decorative window mock; there is no how-it-works section and no sign-up. 'SHOW ME HOW' goes to #features (three cards).  
   Fix: Point CTAs at a real sign-up [DATA NEEDED: URL]; remove 'How it works' until that section exists. (remedy: fix-copy)
7. **[Reflex P1] SLP-222 Swap / rival's-name test: any head still true with a competitor's name (or the same trade ** (1x). hero, 1440 tile 00  
   Evidence: Failed T-RIVAL-NAME and T-FIVE-SECOND: 'YOUR WORK. MINUS THE WORK.' / 'The all-in-one workspace for teams that refuse to play small. Less chaos. More shipping. Zero boring.' is true for Notion, ClickUp, Monday or any tool. After five seconds you cannot say what Lumina does, for whom, or what 'START MAKING MOVES' starts.  
   Fix: [DATA NEEDED: the one job Lumina does and for whom] as the head; a CTA that names the action ('Start a free workspace'). (remedy: None)
8. **[Reflex P1] A11-002 Text size floors** (8x). section.features:nth-of-type(2) > div.feature-grid > article.feature:nth-of-type(1) > p  "Supercharge your workflow and turn big ideas into "  
   Evidence: 70-character run at 13px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
9. **[Reflex P1] CPY-005 No slop diction** (4x). section.features:nth-of-type(2) > div.feature-grid > article.feature:nth-of-type(1) > p  "Supercharge your workflow and turn big ideas into "  
   Evidence: "Supercharge" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
10. **[Reflex P1] LAY-003 Headings sit with their content** (2x). main > section.hero:nth-of-type(1) > div.hero-copy:nth-of-type(1) > h1  "YOUR WORK. MINUS THE"  
   Evidence: 20px above the heading but 25px below it: it reads as part of the block above  
   Fix: Increase space above headings; reduce space below. (remedy: fix-layout)
11. **[Reflex P1] SLP-013 No emoji as icons** (2x). section.features:nth-of-type(2) > div.feature-grid > article.feature:nth-of-type(2) > div.feature-icon  "✳"  
   Evidence: emoji used as an icon: "✳" (2 on page)  
   Fix: Use a consistent icon set with labels, or no icon. (remedy: fix-quieter)
12. **[Reflex P1] SLP-010 No template chrome glyphs** (2x). section.features:nth-of-type(2) > div.feature-grid > article.feature:nth-of-type(3) > div.feature-icon  "⚡"  
   Evidence: template chrome (emoji-bullets): "⚡"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
13. **[Reflex P1] SLP-007 No stock gradient pairs** (1x). main > section.hero:nth-of-type(1)  
   Evidence: gradient 4 stops: #171717, #000000, #171717, #000000  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
14. **[Reflex P1] CLR-001 Accent footprint within budget** (1x). first screen at 1280px  
   Evidence: saturated accent covers 59.4% of the fold (fail > 8%)  
   Fix: Keep accent on the primary action, current state and one focal element. (remedy: fix-colorize)
15. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 11 distinct font sizes: 10, 11, 12, 13, 16, 19, 22, 27, 32, 38, 84 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)

7 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- contrast (A11-001): not-verified: 2 failing text run(s) not verified: rendered colour differs from the CSS colour (blend, background-clip or overlay)
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://impeccable.style/js/detect-antipatterns-browser.js
- a11y: disputed: contrast on h1 mark 'WORK.' (1.00:1, #171717 on #171717) — tile 1440-00 shows black text on a lavender #c4b5fd block; the sampler hit the block's black offset shadow, not its fill.
- a11y: Focus ring appearance not opened in focus/*.png beyond the sweep (no focus_ring hits).
- a11y: No forms; no images with alt to assess (icons are text glyphs, covered by the sweep's emoji_icons hit).
- slop: Page footer labels itself an example ('Fictional product · Impeccable design-pattern example'); judged as the artifact shown, not its intent.
- slop: Blocked script /js/detect-antipatterns-browser.js (site overlay tool), recorded in manifest; not part of the design.
