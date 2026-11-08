# Unslop report: /home/claude/refs/impeccable/tests/fixtures/antipatterns/should-pass.html

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
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-007 Headings and landmarks** (1x). page  
   Evidence: dom-1440.json landmarks: main 0, header 0. All content sits directly in body; with three sections and no landmark there is no 'skip to content' target. (Sweep reported missing main; added here: the h2 sections are plain div.section with no region roles either.)  
   Fix: <main><h1>…</h1><section aria-labelledby="clean-cards">…</section>…</main> (remedy: fix-a11y)
2. **[Reflex P1] CLR-116 Treat a framework default or banned look as not-a-brand** (1x). whole page, 1440 tiles 00-01  
   Evidence: Failed T-DEFAULT-AGENT: page #f9fafb, headings #111827, section heads #6b7280, dark cards #1f2937/#111827, badge #dbeafe/#1d4ed8, side rules in Tailwind blue, violet and emerald, all in Inter. Every value is a framework default; nothing was picked for this document.  
   Fix: One neutral ramp tinted toward a chosen hue and one accent; a heading face that is not the UI face (or Inter used deliberately at a contrasting weight). (remedy: None)
3. **[Reflex P1] CPY-005 No slop diction** (10x). html > body > p.intro  "None of these should be flagged. They're all inten"  
   Evidence: "intentional" (buzzwords/virtue-words, cap budget 2, found 3)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
4. **[Reflex P1] TYP-001 Clear type hierarchy** (2x). h3 vs body  
   Evidence: h3 19px is only 1.17x body 16px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)
5. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (1x). whole page  
   Evidence: 8 stock framework colours used directly: #111827, #1e293b, #1f2937, #374151, #3b82f6, #6b7280  
   Fix: Define brand tokens and use them instead of framework defaults. (remedy: fix-colorize)
6. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > h1  "Clean Patterns: Should Pass"  
   Evidence: display text at 24px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
7. **[Reflex P1] CPY-004 Dash budget** (1x). whole page  
   Evidence: 3 em/spaced en dashes (budget 2)  
   Fix: Use a full stop, comma, colon or parentheses. (remedy: fix-copy)
8. **[Reflex P1] A11-007 Headings and landmarks** (1x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
9. **[Reflex P1] CPY-108 Never write "latest", "new", a version number or market figure without an as-of date** (1x). card 4, 'No border at all'  
   Evidence: Failed T-DELETION: the blue 'New' pill asserts nothing that is new; removing it loses no fact, state or grouping.  
   Fix: Remove the badge, or replace it with a real state ('Added in v1.4, [date]'). [DATA NEEDED: what changed and when] (remedy: None)
10. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (8x). html > body > h1  "Clean Patterns: Should Pass"  
   Evidence: last line is 21% of the measure at 375px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
11. **[Finish P3] A11-002 Text size floors** (6x). html > body > div.section:nth-of-type(1) > div.card-rounded:nth-of-type(1) > p  "Subtle 1px border all around. Clean and intentiona"  
   Evidence: 52-character run at 14px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
12. **[Finish P3] A11-007 Headings and landmarks** (1x). h2 section heads vs h3 card titles  
   Evidence: Programmatic outline is correct (h1 > h2 > h3) but the h2s render smaller (18px vs 18.72px) and lighter (#6b7280 vs #111827) than their h3s. A sighted low-vision reader using magnification sees the card titles as the section heads.  
   Fix: h2 { font-size: 1.75rem; color: #111827 } so visual and programmatic levels agree. (remedy: fix-a11y)
13. **[Finish P3] LAY-004 No dead bands** (1x). every section at 1440  
   Evidence: Cards are fixed at about 448px and left-aligned; at 1440 roughly 70% of each row is empty while the section rules run the full 1360px width, so the rules frame nothing.  
   Fix: Lay the cards in an auto-fit grid (repeat(auto-fit, minmax(20rem, 1fr))) or cap the whole document container at ~60rem so rule and content share a width. (remedy: fix-layout)

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
- a11y: disputed: focus_ring 'Tab reached no focusable element' is not a defect here; the page has no links, buttons or inputs, so there is nothing to focus
- a11y: Verified sweep text_floor hits (14px card body) are real on tile 1440-00; dark-card body #9ca3af on #1f2937 checked by eye and the sweep did not flag it
- a11y: forms, motion, images: none present
- a11y: live keyboard testing: nothing interactive to test
- slop: Purpose: this is a component reference sheet, not a client site; T-RIVAL-NAME and T-MIRROR are weak tests here and were not scored as findings
- slop: T-STOCK-ORDER: three groups of cards, 0 stock sections
- slop: lexicon words and em dashes already reported by the sweep; not repeated
