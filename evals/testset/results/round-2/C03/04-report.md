# Unslop report: /home/claude/refs/ux-ui-agent-skills/tests/fixtures/critic/empty-state-floating.html

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
| Accessibility | 9 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > main > h1  "Reports"  
   Evidence: display text at 42px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
2. **[Reflex P1] A11-007 Headings and landmarks** (1x). h2 'No data'  
   Evidence: The empty message is marked as an h2, so heading navigation lists 'No data' as a section of the page rather than a status; 'SECTION 01' is a <p> styled as a label that a screen reader reads as body text with no meaning.  
   Fix: <section aria-labelledby="rep"><h2 id="rep">Reports list</h2><p role="status">No reports yet...</p></section> (remedy: fix-a11y)
3. **[Reflex P1] CMP-244 State each fact once where it does work** (1x). div.empty: h2 'No data', p 'There is nothing to show.'  
   Evidence: Failed T-FIVE-SECOND on 'what to do': the only content on the Reports page says there is nothing, twice ('No data' and 'There is nothing to show.' state one fact twice), with no reason and no action. T-FRESH-READER: both lines fit any app.  
   Fix: Say why it is empty and what makes reports appear, with one action: 'No reports yet. Reports appear after your first data import.' + button 'Import data' [DATA NEEDED: what populates Reports and the action that starts it] (remedy: None)
4. **[Reflex P1] SLP-002 No decorative section numbering** (1x). p.eyebrow 'SECTION 01' under h1 'Reports'  
   Evidence: T-EYEBROW: covering 'SECTION 01' (12px tracked caps) loses nothing; there is no section 02, no navigation and no section name. The sweep's numbered_labels and eyebrow detectors did not fire on it.  
   Fix: Delete it, or replace with a real identifier (workspace or date range) [DATA NEEDED: report scope] (remedy: fix-typeset)
5. **[Reflex P1] LAY-003 Headings sit with their content** (1x). div.empty at 1440 (x 625-815, y 135-190)  
   Evidence: The page header is left-aligned at x 373 while the empty block is centred in the 727px column, so it floats mid-page detached from the heading; the remaining ~700px below is blank (tile 1440-00).  
   Fix: Align the empty state to the content's left edge, or give it a bordered region the size of the eventual report list so it reads as that list's empty state (remedy: fix-layout)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: no forms
- focus_ring (A11-003): skipped: page has no interactive controls
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: sweep A11-003 'Tab reached no focusable element' is not a focus-visibility failure; the page simply has no controls (the missing action is a content gap, reported in the slop lens).
- slop: Whether reports can exist at all (loading vs error vs truly empty) cannot be told from one static state.
