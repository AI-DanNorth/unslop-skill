# Unslop report: /home/claude/refs/impeccable/tests/fixtures/antipatterns/should-flag.html

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
| Accessibility | 5 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Reflex P1] SLP-004 No side-tab accent borders on cards** (6x). html > body > div.cards:nth-of-type(1) > div.border-r-4.border-purple-500:nth-of-type(2)  
   Evidence: 4px right border, others ≤1px, radius 4px  
   Fix: Use grouping, a heading or one surface change instead. (remedy: fix-quieter)
2. **[Reflex P1] A11-002 Text size floors** (3x). html > body > div.cards:nth-of-type(3) > div.card.card-css-top:nth-of-type(4) > p  "Top border from style block."  
   Evidence: 28-character run at 13px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
3. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
4. **[Reflex P1] SLP-012 Look-family cluster** (2x). whole page  
   Evidence: saas-card-kit: 3 of 5 tells (card_kit (card kit detector); inter_only (Inter); stock_greys (stock grey text)); cluster minimum 3  
   Fix: Break the family on its strongest tell first; name the replacement decision. (remedy: fix-quieter)
5. **[Reflex P1] SLP-005 No uniform card kit** (1x). html > body > div.cards:nth-of-type(2) > div.card.card-shorthand-left:nth-of-type(1)  
   Evidence: 4 containers share radius 6px and shadow "rgba(0, 0, 0, 0.1) 0px 1px 3px 0px"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
6. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (1x). whole page  
   Evidence: 6 stock framework colours used directly: #111827, #1f2937, #3b82f6, #4b5563, #6b7280, #9ca3af  
   Fix: Define brand tokens and use them instead of framework defaults. (remedy: fix-colorize)
7. **[Reflex P1] TYP-001 Clear type hierarchy** (1x). h2 vs h3  
   Evidence: h2 14px is only 1.00x h3 14px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)
8. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > h1  "Anti-Patterns: Should Flag"  
   Evidence: display text at 32px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
9. **[Reflex P1] LAY-001 Spacing has rhythm** (1x). whole page  
   Evidence: 16px is 77% of 88 spacing values (max 60%)  
   Fix: Tighten within groups, open between groups. (remedy: fix-layout)
10. **[Reflex P1] CLR-110 One accent across the page, never two (unless a declared full-palette posture)** (1x). accent strips across all four sections  
   Evidence: Seven unrelated accent hues on one page with no meaning attached: blue, purple, red (Tailwind side-tab), blue, violet, green, red (CSS side-tab), blue, purple, emerald (top/bottom), cyan, violet, pink (dark mode). T-DELETION: recolouring them all one hue loses no information.  
   Fix: One accent token, or none; if variety is needed for detector coverage, vary the property (width, side, shorthand) and keep the hue constant (remedy: None)
11. **[Reflex P1] TYP-165 Never set text ≤15px in uppercase, small caps or tracked past 0.03em (labels, captions, th** (1x). section heads "TAILWIND SIDE-TAB", "CSS SIDE-TAB", "TOP/BOTTOM + ROUNDED", "DARK MODE"  
   Evidence: Failed T-LABEL-TRANSFORM: the h2s are 14px uppercase, tracked and grey, the same size as the h3 card titles (sweep flat_hierarchy: h2 14px = h3 14px). Set in sentence case they read as well or better, so the caps are costume and the only thing separating sections from cards.  
   Fix: h2 at 20-24px sentence case, untracked, body colour: "Tailwind side-tab" (remedy: None)
12. **[Finish P3] A11-002 Text size floors** (9x). html > body > div.cards:nth-of-type(3) > div.border-b-4.border-purple-500:nth-of-type(2) > p.text-sm.text-gray-600  "Bottom accent on rounded card."  
   Evidence: 30-character run at 14px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
13. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (1x). html > body > div.cards:nth-of-type(4) > div.border-l-4.border-cyan-400:nth-of-type(1) > p.text-sm.text-gray-400  "Dark background doesn't make the side-tab OK."  
   Evidence: last line is 18% of the measure at 375px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
14. **[Finish P3] LAY-156 Empty area >35% of a section inside its container WARN, >50% FAIL** (1x). every section at 1440, right two thirds  
   Evidence: Cards are capped at 448px wide and left-aligned while section rules run the full 1376px; about 65% of each section's container is empty at 1440 (tiles 0-1).  
   Fix: Grid the specimens: grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)) so each section fills its rule, or cap the whole page at ~720px so the rules match the cards (remedy: None)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- focus_ring (A11-003): skipped: page has no interactive controls
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: sweep focus_ring Floor hit "Tab reached no focusable element". The page contains no links, buttons or form controls (dom-1440.json, focus.json is empty), so there is nothing that must take focus; 2.4.7 is not applicable. A skip link is unnecessary on a page with no repeated blocks.
- a11y: Alt text, link purpose, forms, keyboard operation, motion: none present on the page.
- a11y: Reflow: 375 tiles show single-column cards with no horizontal scroll; 1.4.12 spacing override not injected.
- slop: Purpose: this is a scanner fixture, not a client page, so T-RIVAL-NAME, T-MIRROR, T-THREE-LINE and T-STOCK-ORDER have no client or category to test against; recorded as run, no finding.
- slop: Tailwind was shimmed with @tailwindcss/browser@4; small differences from the original v3 render are possible.
