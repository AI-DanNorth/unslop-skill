# Unslop report: https://ai-stack--techaffiliate.replit.app/

**Verdict (draft): fix**. Profile: balanced. 1 Floor finding(s) open.

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
| Accessibility | 6 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] TYP-004 The intended font actually renders** (1x). body > div.err-box > div.message:nth-of-type(1) > div.title-box:nth-of-type(2) > h1  "This app isn't live yet"  
   Evidence: declared "Replit Diatype" but Segoe UI drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
2. **[Reflex P1] LAY-004 No dead bands** (2x). y 1-217 at 1280px  
   Evidence: 216px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
3. **[Reflex P1] A11-004 Target size** (2x). div.err-box > div:nth-of-type(2) > div.footer-item:nth-of-type(1) > div.repl-links:nth-of-type(2) > a  "Learn how to publish your app on Replit"  
   Evidence: touch target 247x19px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
4. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
5. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). body > div.err-box > div.message:nth-of-type(1) > div.title-box:nth-of-type(2) > h1  "This app isn't live yet"  
   Evidence: display text at 24px set in Segoe UI, a UI text face  
   Fix: Pick a display face for the brief; see substitutes in data/lexicons/fonts.yaml. (remedy: fix-typeset)
6. **[Finish P3] A11-002 Text size floors** (3x). body > div.err-box > div.message:nth-of-type(1) > div.description-box:nth-of-type(3) > h2  "We couldn't find a Replit App at this address. If "  
   Evidence: 106-character run at 14px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
7. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (1x). body > div.err-box > div.message:nth-of-type(1) > div.description-box:nth-of-type(3) > h2  "We couldn't find a Replit App at this address. If "  
   Evidence: last line is 22% of the measure at 375px (3 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- spacing_monotony (LAY-001): skipped: only 9 spacing values
- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. font https://ai-stack--techaffiliate.replit.app/__replco/static/fonts/ReplitDiatypeVariabl
