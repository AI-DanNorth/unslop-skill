# Unslop report: /home/claude/refs/ux-ui-agent-skills/tests/fixtures/critic/async-lies.html

**Verdict (draft): fix**. Profile: balanced. 2 Floor finding(s) open.

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
| Accessibility | 3 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-006 Controls have accessible names** (1x). p#toast below the action buttons  
   Evidence: The status message slot is an empty <p id=toast> with no role recorded in dom-1440.json; results of 'Create draft project' and 'Export' are written there visually.  
   Fix: <p id="toast" class="toast" role="status" aria-live="polite"></p>, and write failures with role="alert" (remedy: fix-a11y)
2. **[Floor P0] A11-001 Text contrast on real pixels** (1x). CSS .btn.is-busy and .btn[disabled]  
   Evidence: Busy and disabled states are shown only with opacity: 0.5 on a #1d4ed8 button with white text; this halves text contrast and the busy state has no text or aria-busy/aria-disabled change.  
   Fix: Keep text contrast >= 4.5:1, change the label ('Creating...') and set aria-busy="true" or aria-disabled="true" on the button (remedy: fix-a11y)
3. **[Reflex P1] CON-113 Declare one content type per page/document and give each page one job (tutorial, how-to, r** (1x). top of page, div.plans above h2 'Your projects'  
   Evidence: A page titled 'Projects' leads with a three-tier pricing row ('$9 / month', '$29 / month', '$99 / month') before the user's own projects. Failed T-MIRROR: the stock three-tier pricing block would be dropped into any SaaS screen the same way.  
   Fix: Lead with the project list and its create action; move plan choice to billing or a single upgrade line tied to a real limit [DATA NEEDED: which plan limit the user is hitting] (remedy: None)
4. **[Reflex P1] A11-007 Headings and landmarks** (3x). body > main > div.plans:nth-of-type(1) > div.card:nth-of-type(1) > h3  "Starter"  
   Evidence: heading jumps from h1 to h3  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
5. **[Reflex P1] TYP-001 Clear type hierarchy** (2x). h2 vs h3  
   Evidence: h2 20px is only 1.18x h3 17px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)
6. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > main > h1  "Projects"  
   Evidence: display text at 42px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
7. **[Reflex P1] LAY-001 Spacing has rhythm** (1x). whole page  
   Evidence: 16px is 65% of 54 spacing values (max 60%)  
   Fix: Tighten within groups, open between groups. (remedy: fix-layout)
8. **[Reflex P1] SLP-005 No uniform card kit** (1x). div.plans, 3 x div.card  
   Evidence: Three identical cards (same radius 20px, #f4f4f6 fill, 1px border, name/price/button) with no feature, limit or difference stated; deleting the cards' shells loses nothing (T-DELETION). The plans cannot be compared: nothing says what $29 buys over $9.  
   Fix: State the one difference that sets each plan apart [DATA NEEDED: seat or project limits per plan], or render as a compact comparison row (remedy: fix-layout)
9. **[Finish P3] CLR-002 No stock framework swatches as brand tokens** (1x). :root --color-action-primary  
   Evidence: Action colour #1d4ed8 is Tailwind blue-700 used as the only accent; the sweep's stock_swatches did not flag it.  
   Fix: A product-owned accent [DATA NEEDED: brand colour], kept at >= 4.5:1 with white text (remedy: fix-colorize)

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
- a11y: Keyboard and live-region behaviour after clicking buttons: no live testing run.
- a11y: Whether ARIA attributes exist on #toast: dom capture does not record aria-* attributes.
- a11y: Sweep skip-link hit (first focusable is 'Choose Starter'): agreed, low impact on a page this short.
- slop: Async behaviour of 'Create draft project', 'Export' and plan buttons (the empty #toast and .btn.is-busy suggest optimistic or fake success states) could not be observed from static evidence; needs a live click test with the network blocked (T-FAKE-SEND / INT-004).
- slop: T-FRESH-READER: only two content lines exist ('Website redesign', 'Mobile app'), both placeholder-like project names; not raised as a finding.
