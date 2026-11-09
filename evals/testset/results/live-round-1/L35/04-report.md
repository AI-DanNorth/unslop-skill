# Unslop report: https://vercel.com/design/guidelines

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
| Integrity | 4 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-003 Visible focus everywhere** (11x). a "Vercel Home"  
   Evidence: no visible focus indicator (outline: solid 2px rgb(16, 16, 16))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] INT-005 No placeholder residue at ship** (3x). strong.font-medium.text-gray-1000\/90 > a.relative.text-current > span.relative.z-10:nth-of-type(1)  "Placeholders signal emptiness."  
   Evidence: "Placeholders" (self-labels/residue, fail)  
   Fix: Fill with real content or a visible [DATA NEEDED] slot. (remedy: fix-copy)
3. **[Floor P0] A11-009 Zoom never blocked** (2x). meta viewport  
   Evidence: maximum-scale=1 blocks zoom  
   Fix: Remove the restriction. (remedy: fix-a11y)
4. **[Floor P0] TYP-004 The intended font actually renders** (1x). div.text-gray-900.max-w-\(--breakpoint-lg\) > main > div.-mb-4 > ul.pl-5.mb-4:nth-of-type(1) > li.mb-3.text-copy-16:nth-of-type(5)  "font size is ≥ 16px on mobile to prevent iOS Safar"  
   Evidence: declared "GeistSans" but Geist Mono drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
5. **[Reflex P1] A11-004 Target size** (12x). html.VEU71W_className.gb9FOq_className > body.tailwind.tailwind-no-preflight > div.min-h-screen.py-4:nth-of-type(2) > div.text-gray-900.max-w-\(--breakpoint-lg\) > a.focus-visible\:outline-2.focus-visible\:outline-focus  
   Evidence: touch target 20x17px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
6. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .\!transition-all  
   Evidence: "transition-property: all !important": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
7. **[Reflex P1] A11-007 Headings and landmarks** (3x). page  
   Evidence: 4 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
8. **[Reflex P1] CPY-001 Words per screen within budget** (1x). screen 2 (y 900-1800) at 1440px  
   Evidence: 292 words on one 900px screen (fail > 143)  
   Fix: Cut qualifiers and repeated claims; move detail to a page that is for reading. (remedy: fix-distill)
9. **[Reflex P1] CPY-002 Page length within budget** (1x). whole page  
   Evidence: 2226 words on the page (budget 675)  
   Fix: Read only hero and headings: if they tell the story, cut the rest. (remedy: fix-distill)
10. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). div.min-h-screen.py-4:nth-of-type(2) > div.text-gray-900.max-w-\(--breakpoint-lg\) > main > div.-mb-4 > ul.pl-5.mb-4:nth-of-type(8)  
   Evidence: "Instead of say ." repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
11. **[Reflex P2] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 3 font families render: Geist, Geist Mono, GeistSans  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
12. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (1x). div.min-h-screen.py-4:nth-of-type(2) > div.text-gray-900.max-w-\(--breakpoint-lg\) > main > div.-mb-4 > p.mb-4.leading-7:nth-of-type(1)  "Interfaces succeed because of hundreds of choices."  
   Evidence: last line is 12% of the measure at 1280px (3 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://vercel.com/vc-ap-b3331f/_next/static/immutable/chunks/2gg0fzzdd7hc9.js
- a11y: dom-1440 records empty text for the h2 elements (#interactions etc.); the visible labels exist, so this is treated as a capture limitation, not a missing name.
- a11y: Copy button next to the install command (32x32, classes outline-none) was not focus-tested live.
- a11y: The install command is clipped at 1440 ('--skill web-design-guide...'); horizontal scroll inside a code block is allowed under 1.4.10, keyboard scrollability not tested.
- slop: disputed: INT-005 placeholder_residue hits ('Placeholders signal emptiness.', 'Use consistent placeholders.') are guideline text about form placeholders, not leftover placeholder copy.
- slop: Page length (2,226 words, sweep CPY-002) is appropriate for a reference document; not treated as slop.
