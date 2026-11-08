# Unslop report: /home/claude/refs/ux-ui-agent-skills/tests/fixtures/bad/slop-screen.html

**Verdict (draft): fix**. Profile: balanced. 7 Floor finding(s) open.

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
| Integrity | 6 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (12x). html > body > div.container > div.header:nth-of-type(1) > p  "Track your key metrics — updated in real-time 🚀"  
   Evidence: 3.86:1 against the background behind the text (10th-percentile pixel #7b60f3, worst 3.84:1; text #ffffff, opacity 0.90, 14px; needs 4.5:1). APCA Lc 66 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-004 Target size** (2x). body > div.container > div.panel:nth-of-type(3) > div.row > button.icon-btn:nth-of-type(1)  "✏️"  
   Evidence: target 15x16px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
3. **[Floor P0] A11-006 Controls have accessible names** (2x). body > div.container > div.panel:nth-of-type(3) > div.row > input  
   Evidence: input[type=text] has no accessible name  
   Fix: Add visible text or aria-label. (remedy: fix-a11y)
4. **[Floor P0] A11-010 Form fields have labels** (1x). body > div.container > div.panel:nth-of-type(3) > div.row > input  
   Evidence: input[type=text] has no label  
   Fix: Add a visible label element. (remedy: fix-a11y)
5. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > div.container  
   Evidence: page is 1100px wide at a 375px viewport (sideways scroll); widest culprit 1100px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
6. **[Floor P0] INT-001 No invented metrics** (1x). KPI cards  
   Evidence: T-FILLER: "$48.2k", "3,910", "1.8%", "62" with deltas "↑ 12%", "↑ 4%", "↓ 2%", "↑ 7% from last month" and no period, source or empty/loading state. The header promises "updated in real-time" while every delta is month-over-month.  
   Fix: Bind to real data with an as-of timestamp, and design the empty and loading states (INT-159); in a mock, mark figures as sample data (remedy: fix-copy)
7. **[Floor P0] CMP-212 Never confirm success before it happened** (1x). Settings card  
   Evidence: Sub-line says "changes are saved automatically" directly above a "Save Changes" button. One of the two is false.  
   Fix: Pick one model: autosave with a visible "Saved" trace (CMP-147) and no button, or an explicit Save with no autosave claim (remedy: None)
8. **[Reflex P1] SLP-013 No emoji as icons** (4x). html > body > div.container > div.header:nth-of-type(1) > h1  "📊 Analytics Dashboard"  
   Evidence: emoji used as a label prefix: "📊 Analytics Dashboard" (3 on page)  
   Fix: Use a consistent icon set with labels, or no icon. (remedy: fix-quieter)
9. **[Reflex P1] A11-004 Target size** (2x). html > body > div.container > div.panel:nth-of-type(3) > button.btn:nth-of-type(1)  "Save Changes"  
   Evidence: touch target 124x32px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
10. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
11. **[Reflex P1] SLP-012 Look-family cluster** (2x). whole page  
   Evidence: saas-card-kit: 3 of 5 tells (card_kit (card kit detector); equal_grid (grid 251px 251px 251px 251px); stock_greys (stock grey text)); cluster minimum 3  
   Fix: Break the family on its strongest tell first; name the replacement decision. (remedy: fix-quieter)
12. **[Reflex P1] SLP-005 No uniform card kit** (1x). html > body > div.container > div.header:nth-of-type(1)  
   Evidence: 7 containers share radius 8px and shadow "rgba(0, 0, 0, 0.1) 0px 4px 6px 0px"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
13. **[Reflex P1] CLR-001 Accent footprint within budget** (1x). first screen at 1280px  
   Evidence: saturated accent covers 10.7% of the fold (fail > 8%)  
   Fix: Keep accent on the primary action, current state and one focal element. (remedy: fix-colorize)
14. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (1x). whole page  
   Evidence: 3 stock framework colours used directly: #6366f1, #9ca3af, #e5e7eb  
   Fix: Define brand tokens and use them instead of framework defaults. (remedy: fix-colorize)
15. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > div.container > div.header:nth-of-type(1) > h1  "📊 Analytics Dashboard"  
   Evidence: display text at 24px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)

8 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Sweep Floor hits verified by eye: the unlabelled email input, the 15x16px emoji buttons, the grey label contrast and the fixed 1100px container (the 375 tile renders the full 1100px layout) are all real; none disputed.
- a11y: Delete Account behaviour (confirmation, undo) cannot be exercised: no handlers in evidence.
- a11y: Keyboard operation: no menus or dialogs; no live run.
- slop: No brief or product context; T-RIVAL-NAME and T-STOCK-ORDER have no category beyond 'generic dashboard' (no finding beyond T-DEFAULT-AGENT).
- slop: Nothing on the screen is specific enough to list as a strength.
