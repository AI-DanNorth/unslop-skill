# Unslop report: /home/claude/refs/ux-ui-agent-skills/tests/fixtures/critic/dashboard-no-lead.html

**Verdict (draft): fix**. Profile: balanced. 0 Floor finding(s) open.

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
| Accessibility | 8 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 9 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Reflex P1] CON-115 Match density to the product: AI/data/context-aware products (dashboards, trackers, copilo** (1x). page below the cards (y 240-900 at 1440)  
   Evidence: The page ends after the KPI row; the remaining 660px is empty. There is no breakdown, list or action, so the dashboard cannot answer the follow-up question any number raises.  
   Fix: Add the one view behind the lead metric (trend or list of what changed) [DATA NEEDED: series data] (remedy: None)
2. **[Reflex P1] CPY-005 No slop diction** (5x). html > body > main > p  "Powerful, intuitive, and beautiful reporting that "  
   Evidence: "unlock" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
3. **[Reflex P1] LAY-001 Spacing has rhythm** (2x). whole page  
   Evidence: 16px is 82% of 28 spacing values (max 60%)  
   Fix: Tighten within groups, open between groups. (remedy: fix-layout)
4. **[Reflex P1] A11-007 Headings and landmarks** (2x). body > main > div.grid4 > div.card:nth-of-type(1) > h3  "Active users"  
   Evidence: heading jumps from h1 to h3  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
5. **[Reflex P1] TYP-001 Clear type hierarchy** (1x). h3 vs body  
   Evidence: h3 17px is only 1.06x body 16px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)
6. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > main > h1  "Team overview"  
   Evidence: display text at 42px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
7. **[Reflex P1] INT-007 Stat bands need sources** (1x). body > main > div.grid4 > div.card:nth-of-type(1) > p.stat  "1,284"  
   Evidence: stat band of 4 unsourced figures: 1,284, 4,017, 3.4%, 1.1%  
   Fix: Cite each figure, use only supplied facts, or remove the band. (remedy: fix-copy)
8. **[Reflex P1] SLP-005 No uniform card kit** (1x). div.grid4: 'Active users 1,284', 'Sessions 4,017', 'Conversion 3.4%', 'Churn 1.1%'  
   Evidence: Four identical cards (same size, fill #f4f4f6, 20px radius, label + number) with no lead: T-FIVE-SECOND fails on 'what to do' and on 'what matters'; the eye has no first stop. Failed T-DEFAULT-AGENT: this is the stock 'KPI row' with nothing else.  
   Fix: Promote the one metric the team acts on to a lead block with its trend and target; set the others as a compact secondary row [DATA NEEDED: which metric the team owns and its target] (remedy: fix-layout)
9. **[Reflex P1] DVZ-103 Show one value as a stat tile (figure + worded qualifier), never a one-bar chart** (1x). each stat card  
   Evidence: T-SO-WHAT: '1,284', '4,017', '3.4%', '1.1%' have no period, no prior value, no direction and no target, so none can be judged good or bad; T-THREE-LINE: none is falsifiable as shown.  
   Fix: Conversion 3.4% (last 30 days, up from 2.9%; target 4%) [DATA NEEDED: period, prior value, target] (remedy: None)
10. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (1x). html > body > main > p  "Powerful, intuitive, and beautiful reporting that "  
   Evidence: last line is 29% of the measure at 1280px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: no forms
- focus_ring (A11-003): skipped: page has no interactive controls
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: sweep A11-003 'Tab reached no focusable element' is not a failure here; the page has no links or controls, so there is nothing to focus.
- a11y: Units and periods for the metrics are a content gap (see slop lens), not a WCAG failure.
- slop: Whether the numbers are real: fixture data, no source supplied (sweep INT-007 already notes unsourced stat band).
