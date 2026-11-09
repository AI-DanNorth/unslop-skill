# Unslop report: https://ui-ux-pro-max-after.theroost.dev

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
| Integrity | 9 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-003 Visible focus everywhere** (2x). a "Telegram"  
   Evidence: no visible focus indicator (outline: solid 3px rgb(37, 99, 235))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] A11-001 Text contrast on real pixels** (1x). html > body > a.vr-badge:nth-of-type(2)  "Powered by Vibe Rooster"  
   Evidence: 3.54:1 against the background behind the text (10th-percentile pixel #fefeff, worst 3.54:1; text #64748b, opacity 0.85, 11px; needs 4.5:1). APCA Lc 63 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] A11-006 Controls have accessible names** (1x). Pending feed, 'Copy' button, tile 00  
   Evidence: Button accessible name is 'Copy' only; out of context it does not say what is copied (the line 'Ask Harbor for the revised PO before Friday.').  
   Fix: <button aria-describedby="pending-email-1">Copy<span class="sr-only"> email task</span></button> (remedy: fix-a11y)
4. **[Floor P0] A11-010 Form fields have labels** (1x). Draft reply field, tile 00 (y 842)  
   Evidence: focus.json stop 11 is a focusable div (not textarea) containing 'Thanks for the update. Can you send the revised PO by Thursday?'; forms.json is empty, so it is not a form control. The visible label 'Unsent reply to Harbor' is not shown to be tied programmatically.  
   Fix: <label for="draft-harbor">Unsent reply to Harbor</label><textarea id="draft-harbor">…</textarea> (or role="textbox" aria-multiline="true" aria-labelledby on the div) (remedy: fix-a11y)
5. **[Reflex P1] SLP-012 Look-family cluster** (2x). top of page, 1440 tile 00  
   Evidence: Failed T-DEFAULT-AGENT and T-MIRROR: 'internal ops dashboard' yields exactly this first screen: a row of three equal white cards ('Open threads 128', 'Waiting on us 14', 'Pipeline $42.6k'), segmented filter pills, a bordered table with a tinted header, on #F8FAFC with #3B82F6/#1E293B tokens (sweep stock_swatches).  
   Fix: Lead with the one thing the weekly ops reader acts on (the Urgent table) and fold the three counts into its header line, e.g. 'Urgent · 3 of 128 open threads · $42.6k pipeline' (remedy: fix-quieter)
6. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (4x). :root --color-secondary  
   Evidence: token --color-secondary: #3B82F6 is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)
7. **[Reflex P1] SLP-006 Vary container recipes** (2x). main > section.stats.reveal:nth-of-type(1) > div.stat:nth-of-type(1)  
   Evidence: one box recipe on 6 elements across 4 selectors (div.stat, li.type-done, li.type-draft, li.type-user)  
   Fix: Differentiate by role: section, object, callout, well. (remedy: fix-layout)
8. **[Reflex P1] LAY-004 No dead bands** (2x). y 1100-1429 at 1280px  
   Evidence: 329px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
9. **[Reflex P1] A11-004 Target size** (2x). html > body > a.vr-badge:nth-of-type(2)  "Powered by Vibe Rooster"  
   Evidence: touch target 141x28px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
10. **[Reflex P1] TYP-001 Clear type hierarchy** (1x). h2 vs body  
   Evidence: h2 16px is only 1.00x body 16px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)
11. **[Reflex P1] INT-007 Stat bands need sources** (1x). main > section.stats.reveal:nth-of-type(1) > div.stat:nth-of-type(1) > div.stat-value:nth-of-type(2)  "128"  
   Evidence: stat band of 3 unsourced figures: 128, 14, $42.6k  
   Fix: Cite each figure, use only supplied facts, or remove the band. (remedy: fix-copy)
12. **[Reflex P1] ROB-002 Phone parity** (1x). #h-urgent  "Urgent"  
   Evidence: 124 words shown at 1440px are hidden at 375px (44 elements)  
   Fix: Reflow instead of hiding. (remedy: fix-layout)
13. **[Reflex P1] MOT-001 Motion CSS hygiene** (1x). .skip-link  
   Evidence: transition on a layout property: "top var(--dur-fast) var(--ease-out)"  
   Fix: Animate transform or opacity instead (remedy: fix-motion)
14. **[Reflex P1] A11-007 Headings and landmarks** (1x). segmented filters and sortable column, tile 00  
   Evidence: '7 days' and 'All' are shown selected by white fill and blue text only; the sortable 'Account' header is a link (?sort=name) with a double-chevron icon. Capture cannot confirm aria-pressed or aria-sort.  
   Fix: aria-pressed="true" on the active segment buttons (or role=radiogroup with aria-checked); aria-sort="none|ascending" on the Account th (remedy: fix-a11y)
15. **[Reflex P1] SLP-004 No side-tab accent borders on cards** (1x). Urgent table row 'Harbor and Co' and insight callout, tiles 00-01  
   Evidence: A 3px red left border marks the flagged table row and a 4px orange left border frames the note "Harbor has gone quiet after the price change...".  
   Fix: Let the 'Blocked' status carry the row; set the note as a plain paragraph under a small heading 'Suggested next step' (remedy: fix-quieter)

3 further findings are in 04-findings.json.

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
- a11y: No live keyboard test of the filter pills, the details/summary 'How this note was chosen', or 'Remove filter Owner: Ada'.
- a11y: Text spacing (1.4.12) not injected.
- slop: No 00-contract.md; the page says it is styled by a named skill's design system, so palette choices are judged as unchosen defaults, not brand.
- slop: The before/after comparison page was not opened.
