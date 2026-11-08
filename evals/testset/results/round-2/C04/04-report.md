# Unslop report: /home/claude/refs/ux-ui-agent-skills/tests/fixtures/critic/list-identical.html

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
| Accessibility | 7 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 1 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-005 No placeholder residue at ship** (2x). table rows 'Invoice 1000' to 'Invoice 1023'  
   Evidence: Every row is 'Acme Corp / Paid / $420.00'; only the number changes and dates cycle 2026-03-01..09 three times, so Invoice 1009 (2026-03-01) is dated before Invoice 1008 (2026-03-09). Failed T-FILLER: the data is not real and the table cannot be read for anything (no unpaid, no different customer, no outlier).  
   Fix: [DATA NEEDED: real or realistic invoice records with varied customers, statuses and amounts]; dates monotonic with invoice numbers (remedy: fix-copy)
2. **[Reflex P1] CON-113 Declare one content type per page/document and give each page one job (tutorial, how-to, r** (1x). h1 'Welcome'  
   Evidence: T-FIVE-SECOND: 'Welcome' says nothing about the page (an invoice list), who it is for or what to do; T-FRESH-READER lists it as a line that fits any app.  
   Fix: Invoices, with a one-line summary (e.g. 'n unpaid, $x due this week') [DATA NEEDED: real totals] (remedy: None)
3. **[Reflex P1] INT-002 No default cast or fake brands** (8x). div.scroller > table > tbody > tr:nth-of-type(1) > td:nth-of-type(2)  "Acme Corp"  
   Evidence: "Acme" (default-names/fake-brands, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
4. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > main > h1  "Welcome"  
   Evidence: display text at 42px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
5. **[Reflex P1] LAY-001 Spacing has rhythm** (1x). whole page  
   Evidence: 12px is 98% of 513 spacing values (max 60%)  
   Fix: Tighten within groups, open between groups. (remedy: fix-layout)
6. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). html > body > main > div.scroller > table  
   Evidence: "Acme Corp" repeated 24 times in one container  
   Fix: Say it once. (remedy: fix-copy)
7. **[Reflex P1] A11-001 Text contrast on real pixels** (1x). div.scroller (table region) at 1440 and 375  
   Evidence: The Date column is cut at the region edge at 1440 and Status/Amount/Date are off-screen at 375 with no visible scroll cue (no shadow, scrollbar or 'scroll for more'); the region is focusable with aria-label 'Invoices, scrolls horizontally' and a 3px ring (focus/01-on.png), so keyboard and screen-reader users are covered but sighted pointer users may not know columns exist.  
   Fix: Edge shadow on the scroll container, or reflow rows into stacked cards below 600px (remedy: fix-a11y)
8. **[Reflex P1] TYP-001 Clear type hierarchy** (1x). table columns 'Status' and 'Amount', 1440  
   Evidence: Status is plain grey text identical for all rows and Amount is left-aligned prose-style, so nothing in the list can be scanned for state or size; the 'Date' column is clipped at the container edge even at 1440 (table 768px inside a 695px box).  
   Fix: Right-align amounts with tabular figures, show status as a labelled badge only when not 'Paid', widen the container or drop the redundant 'Invoice' prefix so all columns fit at desktop (remedy: fix-typeset)
9. **[Reflex P2] A11-007 Headings and landmarks** (2x). page  
   Evidence: first focusable element is input "", not a skip link  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 1 type roles
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: th scope attributes not recorded in the capture.
- a11y: Sweep skip-link hit agreed; low impact on this page.
- slop: Behaviour of the 'Debug mode' toggle (no live interaction).
