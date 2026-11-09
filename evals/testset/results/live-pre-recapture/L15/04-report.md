# Unslop report: https://skill-fixture-before.theroost.dev

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
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (2x). button.vr-hitl-chip > span.vr-hitl-meta:nth-of-type(2)  "1/5"  
   Evidence: 4.22:1 against the background behind the text (10th-percentile pixel #f1f1f2, worst 4.22:1; text #64748b, 11px; needs 4.5:1). APCA Lc 65 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] ROB-003 No horizontal overflow** (1x). section:nth-of-type(7) > table  
   Evidence: page is 773px wide at a 375px viewport (sideways scroll); widest culprit 749px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
3. **[Floor P0] A11-007 Headings and landmarks** (1x). section labels 'Urgent', 'Pending', 'Empty', tile 1440-00  
   Evidence: These bold labels head their sections visually, but dom-1440 lists only h1 'Northline weekly ops' and h2 'Reach them', 'Campaign tracker', 'Finish your review'; the first three sections have no heading.  
   Fix: <h2>Urgent</h2>, <h2>Pending</h2>, <h2>Empty</h2> (and wrap the page body in <main>) (remedy: fix-a11y)
4. **[Floor P0] A11-006 Controls have accessible names** (1x). filter buttons All / People / Money  
   Evidence: Sweep selector shows 'button.filter.active' on All, but in tile 1440-00 the three buttons look identical; no visible or (from the DOM capture) programmatic selected state.  
   Fix: <button class="filter" aria-pressed="true">All</button> plus a visible selected style (filled background or underline) (remedy: fix-a11y)
5. **[Floor P0] A11-004 Target size** (1x). Campaign tracker table at 375px, tile 375-01  
   Evidence: Verified sweep overflow hit: the table pushes the page to 773px at a 375px viewport; the whole page scrolls sideways, not just the table.  
   Fix: Wrap the table in <div role="region" aria-label="Campaign tracker" tabindex="0" style="overflow-x:auto"> (remedy: fix-a11y)
6. **[Reflex P1] A11-004 Target size** (10x). body > section:nth-of-type(2) > div.filter-bar > p:nth-of-type(1) > button.filter.active:nth-of-type(1)  "All"  
   Evidence: touch target 42x34px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] CPY-006 No repeated labels inside a card** (2x). section:nth-of-type(7) > table  
   Evidence: "; VibeRooster fork safe to delete" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
8. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
9. **[Reflex P1] A11-006 Controls have accessible names** (2x). 'Owner: Ada' filter chip  
   Evidence: Button accessible name is 'Remove' (focus stop 4); out of context it does not say what is removed.  
   Fix: <button class="chip-remove" aria-label="Remove filter: Owner Ada">Remove</button> (remedy: fix-a11y)
10. **[Reflex P1] SLP-006 Vary container recipes** (1x). section:nth-of-type(3) > table.table-styled > tbody > tr.tier-gold.highlight:nth-of-type(1) > td:nth-of-type(1)  "Harbor and Co"  
   Evidence: one box recipe on 177 elements across 3 selectors (td, td.negative, td.positive)  
   Fix: Differentiate by role: section, object, callout, well. (remedy: fix-layout)
11. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > header > h1  "Northline weekly ops"  
   Evidence: display text at 32px set in Segoe UI, a UI text face  
   Fix: Pick a display face for the brief; see substitutes in data/lexicons/fonts.yaml. (remedy: fix-typeset)
12. **[Reflex P1] LAY-001 Spacing has rhythm** (1x). whole page  
   Evidence: 8px is 93% of 845 spacing values (max 60%)  
   Fix: Tighten within groups, open between groups. (remedy: fix-layout)
13. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (4x). html > body > header > p:nth-of-type(2)  "Basic HTML: a readable font, spacing, and table bo"  
   Evidence: last line is 20% of the measure at 375px (4 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
14. **[Finish P3] CPY-006 No repeated labels inside a card** (2x). Urgent table Status column and Pending list, tile 1440-00  
   Evidence: State word and detail are run together with no separator or styling: 'Blocked stale 9 days', 'Waiting pending reply', 'Clear warm', 'Draft Unsent', 'Done Yesterday Intro sent to the Boston plant manager.' They read as garbled phrases rather than a status plus a note.  
   Fix: Render the state as a label and the detail as text: "Waiting — pending reply" or a status pill followed by the note. (remedy: fix-copy)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: The 'Review required 1/5' chip and 'Finish your review' form (three unlabelled inputs and a textarea in dom-1440) look like an injected review widget, not page content; their labels were not judged. Sweep contrast hit on its '1/5' (4.22:1, 11px) is real for that widget.
- a11y: No live keyboard test of the filter buttons or the review widget.
- a11y: Text spacing override (1.4.12) not injected.
- slop: The floating 'Review required 1/5' chip and the 'Finish your review' form appear to be an injected review widget (vr-hitl classes), not page design; not judged.
- slop: Visual polish (hierarchy, spacing, table design) belongs to other lenses; the page states it is a 'before' fixture with basic styling.
