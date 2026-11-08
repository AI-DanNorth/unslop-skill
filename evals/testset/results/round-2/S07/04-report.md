# Unslop report: /home/claude/refs/huashu-design-en/scripts/tests/fixtures/lint_slop.html

**Verdict (draft): fix**. Profile: balanced. 6 Floor finding(s) open.

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (10x). html > body > div.wrap > h1 > em  "履历"  
   Evidence: 2.77:1 against the background behind the text (10th-percentile pixel #f4f1ea, worst 2.77:1; text #d97757, 76px; needs 3.0:1). APCA Lc 50 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] INT-005 No placeholder residue at ship** (2x). html > body > div.wrap > p  "这是一段足够长的正文，用来让体检脚本识别正文字号和字体，内容本身不重要。"  
   Evidence: "内容本身不重要" (self-labels/residue, fail)  
   Fix: Fill with real content or a visible [DATA NEEDED] slot. (remedy: fix-copy)
3. **[Floor P0] A11-008 Language and title set** (2x). <title>  
   Evidence: page has no title  
   Fix: Add lang and a specific title. (remedy: fix-a11y)
4. **[Floor P0] A11-006 Controls have accessible names** (2x). a.cta x4, all cards  
   Evidence: dom-1440.json: the four a.cta elements have no href (cursor:pointer only); focus.json is empty and the sweep reports 'Tab reached no focusable element'. The links look actionable but cannot be reached or activated by keyboard.  
   Fix: <a class="cta" href="/origin">…</a> with a real destination, or remove the link styling if there is nowhere to go. (remedy: fix-a11y)
5. **[Floor P0] A11-007 Headings and landmarks** (1x). card labels 'STEP ONE'-'STEP FOUR'  
   Evidence: The only heading is h1; each card's title is a div.num plus a styled div. Screen-reader heading navigation finds one heading for a five-block page.  
   Fix: <h2>…</h2> per card with a descriptive name; keep the number as aria-hidden decoration if kept at all. (remedy: fix-a11y)
6. **[Floor P0] A11-002 Text size floors** (1x). .grid at 375 (tiles 375-00, 375-01)  
   Evidence: At 375 the three-column grid holds: card text wraps every 2-3 characters and '了解更多 →' breaks over three lines; card three runs to the right edge (x 266-366). Content is technically present but unreadable as running text.  
   Fix: @media (max-width: 40rem) { .grid { grid-template-columns: 1fr } } (remedy: fix-typeset)
7. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). first screen, 1440  
   Evidence: Failed T-FIVE-SECOND: the first screen says 'every cup has a record' but not what is sold, to whom, or what to do. The only actions are four identical '了解更多 →' links with no destination.  
   Fix: A sub-line naming the product and the visitor's action (order beans / visit the café / subscribe). [DATA NEEDED: business kind and primary action] (remedy: None)
8. **[Reflex P1] TYP-004 The intended font actually renders** (1x). h1, '履历'  
   Evidence: CSS sets h1 to Georgia, serif and h1 em to italic, but Georgia has no CJK glyphs: the headline renders in the fallback CJK sans (Noto Sans CJK SC) and '履历' is a synthetic slant. The 'serif display with italic accent' is a Latin-font recipe applied to Chinese text.  
   Fix: Name a CJK display face (e.g. Noto Serif SC / Source Han Serif) and mark emphasis with weight or colour, not a faked oblique. (remedy: fix-typeset)
9. **[Reflex P1] CPY-005 No slop diction** (1x). eyebrow and h1  
   Evidence: Failed T-RIVAL-NAME and T-FRESH-READER: 'ORIGIN · PROCESS · ROAST' and '每一杯，都有一段履历' stay true for any specialty roaster in any town. Generic lines: the eyebrow, the h1, and '了解更多 →'.  
   Fix: A head only this roaster can say: a named origin, a roast date, a place. [DATA NEEDED: one specific fact] (remedy: fix-copy)
10. **[Reflex P1] SLP-010 No template chrome glyphs** (8x). html > body > div.wrap > div.eyebrow:nth-of-type(1)  "Origin · Process · Roast"  
   Evidence: template chrome (middot-chains): "Origin · Process · Roast"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
11. **[Reflex P1] SLP-012 Look-family cluster** (2x). whole page  
   Evidence: warm-paper-serif: 4 of 6 tells (cream_bg (page #f4f1ea); terracotta_accent (#d97757); serif_display (Noto Sans CJK SC); eyebrows (5 tracked caps labels)); cluster minimum 3  
   Fix: Break the family on its strongest tell first; name the replacement decision. (remedy: fix-quieter)
12. **[Reflex P1] SLP-005 No uniform card kit** (1x). html > body > div.wrap > div.grid:nth-of-type(2) > div.card:nth-of-type(1)  
   Evidence: 4 containers share radius 14px and shadow "rgba(0, 0, 0, 0.1) 0px 2px 8px 0px"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
13. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). html > body > div.wrap  
   Evidence: "了解更多 →" repeated 4 times in one container  
   Fix: Say it once. (remedy: fix-copy)
14. **[Reflex P1] A11-007 Headings and landmarks** (1x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
15. **[Reflex P1] SLP-002 No decorative section numbering** (1x). card headers, all four cards  
   Evidence: Failed T-DELETION and T-LABEL-TRANSFORM: '01' and 'STEP ONE' say the same thing twice; removing either loses nothing. With caps and 0.18em tracking removed, 'Step one' is still an empty label: no step is named.  
   Fix: One heading per card that names the step, e.g. 'Origin: [farm, region]', 'Roast: [profile]'. [DATA NEEDED: the real steps] (remedy: fix-typeset)

2 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 1 type roles
- fake_send (INT-004): skipped: no forms
- focus_ring (A11-003): skipped: page has no interactive controls
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Sweep Floor hits verified: contrast on h1 em '履历' (2.77:1 at 76px) and on #d97757 over white are real; no disputes
- a11y: forms: none on the page
- a11y: live keyboard and text-spacing injection: not run, judged from DOM and focus.json
- slop: T-STOCK-ORDER: only 2 sections (hero, step cards), so the count test does not apply; the read rests on the look-family cluster and empty copy
- slop: brief and contract: no 00-contract.md in the run, so no override could be checked
- slop: body copy and placeholder text: already reported by the sweep (INT-005), not repeated
