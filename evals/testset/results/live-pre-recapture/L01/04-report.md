# Unslop report: https://findaistack.lovable.app/

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (9x). div.mx-auto.grid > div.relative.h-\[440px\]:nth-of-type(2) > div.floaty.absolute:nth-of-type(2) > div.mt-3.flex > span.rounded-full.bg-brand\/10:nth-of-type(1)  "Video"  
   Evidence: 4.26:1 against the background behind the text (10th-percentile pixel #ddeafb, worst 4.26:1; text #275ef9, 12px; needs 4.5:1). APCA Lc 62 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-011 Reduced motion respected** (1x). hero right column, three div.floaty cards ('Your goal', 'Recommended stack', 'Workflow')  
   Evidence: dom-1440.json: animation 'floaty' 7s (translateY 0 to -14px) on three text-bearing cards; CSS keyframes loop with no pause control. A prefers-reduced-motion override exists, so this is 2.2.2 only, not 2.3.3.  
   Fix: Stop after one or two cycles (animation-iteration-count: 2) or add a visible pause toggle; keep the existing reduced-motion override (remedy: fix-motion)
3. **[Floor P0] A11-109 Keep reading order and screen-reader order equal to visual order.** (1x). goal card grid, third card 'Create content' at 1440  
   Evidence: focus.json stop 13 ('CONTENT Create content...') is covered=true: the fixed 'Edit with Lovable' badge (bottom right, tile 1440-00) sits over the card when it receives focus. Confirms sweep focus_ring hit.  
   Fix: Remove the builder badge from production, or add scroll-padding-bottom equal to its height so focused items scroll clear (remedy: None)
4. **[Floor P0] A11-115 Expose correct state attributes: aria-expanded on menu/accordion triggers, aria-pressed/ar** (1x). header USD / INR toggle  
   Evidence: Two plain <button type=button> elements 'USD' and 'INR'; the selected currency is shown only by a black pill fill (tile 1440-00). dom-1440.json records no role or pressed state on either.  
   Fix: <button aria-pressed="true">USD</button><button aria-pressed="false">INR</button> inside role="group" aria-label="Currency" (remedy: None)
5. **[Reflex P1] SLP-012 Look-family cluster** (1x). whole page, 1440 and 375  
   Evidence: Failed T-DEFAULT-AGENT: pale blue-grey page (oklch 0.973 0.006 264), Inter body with Space Grotesk display, one royal-blue accent, pill badge 'Personalized AI tool bundles' with status dot, white rounded-2xl cards with hairline border and soft shadow, black pill 'View details' buttons. This is the saas-card-kit look family end to end; the 'Edit with Lovable' badge in tile 1440-00 confirms the builder default was shipped unchanged.  
   Fix: Pick one visual decision that belongs to a 'stack builder' (e.g. stacked-layer motif, or a real recommendation output as the hero) and let the kit recede; [DATA NEEDED: brand direction] (remedy: fix-quieter)
6. **[Reflex P1] SLP-169 Ban imitation material: a hero "product UI" built from styled divs with invented figures, ** (1x). hero right column  
   Evidence: Floating mock cards 'Your goal / Start a YouTube channel', 'Recommended stack', 'Workflow 1-2-3' over a pale gradient slab: a static dashboard-style mock with illustrative data, the standard 'product UI floating in the hero' device.  
   Fix: Show the real first question of the flow inline so the hero is the product, or one real recommendation output with a link (remedy: None)
7. **[Reflex P1] A11-004 Target size** (12x). body > div.flex.min-h-screen > header.sticky.top-0 > div.mx-auto.flex > a.flex.items-center  
   Evidence: touch target 109x32px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
8. **[Reflex P1] MOT-001 Motion CSS hygiene** (6x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
9. **[Reflex P1] CPY-005 No slop diction** (4x). section.relative.overflow-hidden:nth-of-type(1) > div.mx-auto.grid > div.lg\:col-span-6:nth-of-type(1) > div.mt-8.flex:nth-of-type(1) > a.inline-flex.items-center:nth-of-type(1)  "Find my stack"  
   Evidence: arrow glued to label "Find my stack →" (3 on page)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
10. **[Reflex P1] CPY-006 No repeated labels inside a card** (2x). body > div.flex.min-h-screen > main.flex-1 > section.mx-auto.max-w-7xl:nth-of-type(3) > div.mt-8.grid:nth-of-type(2)  
   Evidence: "No-code" repeated 4 times in one container  
   Fix: Say it once. (remedy: fix-copy)
11. **[Reflex P1] A11-002 Text size floors** (1x). main.flex-1 > section.relative.overflow-hidden:nth-of-type(1) > div.mx-auto.grid > div.lg\:col-span-6:nth-of-type(1) > span.inline-flex.items-center  "Personalized AI tool bundles"  
   Evidence: 28-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
12. **[Reflex P1] A11-105 Provide a skip link as the first focusable element, hidden until focused.** (1x). page start  
   Evidence: First focusable is the logo link 'AAI Stack' (the 'A' logo glyph text is read into the name, so it announces 'A AI Stack').  
   Fix: aria-hidden="true" on the 'A' logo tile; add a skip link to #main as the first focusable (remedy: None)
13. **[Reflex P1] SLP-005 No uniform card kit** (1x). 'What are you trying to accomplish?' grid and 'AI Tools Directory' grid (tiles 1440-00 to 1440-02)  
   Evidence: Ten identical goal cards (caps blue label, h3, one-line description) in a 3-column grid leaving one orphan card ('Design faster') alone on the last row, then six identical tool cards each ending in a full-width black 'View details' pill. Failed T-STOCK-ORDER: badge hero with mock UI, stat trio, equal feature cards, equal product cards, table, minimal footer = 5 stock sections in stock order.  
   Fix: Make the goal picker an actual control (a single select row or chip set that leads into the questionnaire) and drop the duplicate per-card 'View details' buttons; let the card itself be the link (remedy: fix-layout)
14. **[Reflex P1] SLP-001 No eyebrow labels above headings** (1x). goal and tool cards, hero badge  
   Evidence: Every card carries a tracked caps label above its heading that repeats the heading: 'VIDEO' over 'Start a YouTube channel', 'DESIGN' over 'Design faster', 'WRITING' over 'Grow a blog'; plus the pill eyebrow 'Personalized AI tool bundles' above the h1.  
   Fix: Delete the caps labels on goal cards (the heading already says it); keep category only on tool cards if it is a filter (remedy: fix-typeset)
15. **[Reflex P1] INT-007 Stat bands need sources** (1x). hero stat row  
   Evidence: '17 curated tools · 5 budget tiers · 3 questions' stat trio under the CTAs; the stat band is filler proof (counts of the product's own config, not outcomes).  
   Fix: Drop the row, or replace with one concrete example output (remedy: fix-copy)

8 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 9 other request(s) blocked, e.g. script https://findaistack.lovable.app/assets/index-D6y6A1Qr.js
- a11y: keyboard operation of the mobile menu and the questionnaire flow: no live keyboard testing, and site scripts were blocked during capture
- a11y: forms and errors: no forms on the captured page
- a11y: reflow at 320px not separately inspected; 375 tiles show no horizontal scroll
- slop: no 00-contract.md brief in the run directory; judged without brand overrides
- slop: site scripts were blocked in capture (manifest network.blocked), so the interactive flow behind 'Find my stack' was not seen
