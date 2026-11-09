# Unslop report: https://www.usehallmark.com/

**Verdict (draft): fix**. Profile: balanced. 3 Floor finding(s) open.

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

1. **[Floor P0] A11-003 Visible focus everywhere** (2x). a "Skip to the page"  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
2. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). observer_never_fires  
   Evidence: 210 characters (33% of text) stay invisible when IntersectionObserver never fires  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
3. **[Floor P0] A11-138 Every drag operation has a single-pointer and keyboard alternative (WCAG 2.5.7).** (1x). 'Made with Hallmark' wheel (ul.wheel__ring, 15 cards)  
   Evidence: Copy says 'Drag the wheel to look around.' dom-1440.json shows the wheel cards as links but no previous/next buttons or other single-pointer control for rotating the ring.  
   Fix: Add <button aria-label="Previous build"> and <button aria-label="Next build"> beside the wheel, and rotate on Left/Right arrow keys when a card has focus (remedy: None)
4. **[Reflex P1] A11-004 Target size** (12x). html.js > body > header.nav > div.wrap.nav__in > a.brand:nth-of-type(1)  
   Evidence: touch target 113x24px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
5. **[Reflex P1] WEB-001 Performance budget** (8x). /www.usehallmark.com/assets/cmp/fieldbook-hallmark-full.webp  
   Evidence: image is 500KB (max 400KB)  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
6. **[Reflex P1] LAY-004 No dead bands** (4x). y 769-984 at 1280px  
   Evidence: 215px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
7. **[Reflex P1] SLP-005 No uniform card kit** (3x). section.hero.is-proofed:nth-of-type(1) > div.fan:nth-of-type(3) > div.fan__hand > a.card.card--desk:nth-of-type(1)  
   Evidence: 5 containers share radius 14px and shadow "rgba(15, 15, 14, 0.06) 0px 2px 4px 0px, rgba(15, 15, 14, 0.4"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
8. **[Reflex P1] SLP-007 No stock gradient pairs** (2x). section.hero.is-proofed:nth-of-type(1) > div.bg:nth-of-type(1) > span.guides.guides--l:nth-of-type(1)  
   Evidence: gradient 8 stops: #fc4c02, #fc4c02, #000000, #000000, #d4d4cf  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
9. **[Reflex P1] TYP-002 Sizes on a declared ladder** (2x). whole page  
   Evidence: 9 distinct font sizes: 13, 15, 16, 17, 20, 24, 51.5, 64, 83 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
10. **[Reflex P1] A11-002 Text size floors** (1x). section.sec:nth-of-type(2) > div.wrap.reveal > p.cmp-note  "The issue counts come from Hallmark’s linter. Scro"  
   Evidence: 90-character run at 13px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
11. **[Reflex P1] ROB-001 Content never depends on animation to appear** (1x). page after load  
   Evidence: 66% of text is hidden after load and scrolling (max 30%; menus and dialogs excluded)  
   Fix: Start visible; animate from visible. (remedy: fix-harden)
12. **[Reflex P1] MOT-001 Motion CSS hygiene** (1x). stylesheet  
   Evidence: overshoot easing cubic-bezier(0.3, 1.35, 0.5, 1) (y beyond 0..1.05)  
   Fix: Use a non-overshoot curve such as cubic-bezier(0.16, 1, 0.3, 1) (remedy: fix-motion)
13. **[Reflex P1] A11-121 Every function is operable by keyboard** (1x). comparison tabs 'Farm records / Bank reconciliation / Webhook API'  
   Evidence: dom-1440.json: three <button role="tab">; no role="tablist" container or aria-selected/aria-controls recorded in the capture, and all three are separate Tab stops in focus.json (stop 14 is only 'Farm records'; the other two do not appear, suggesting roving tabindex). Visual selected state is fill colour only (black pill vs plain text).  
   Fix: <div role="tablist" aria-label="Example prompt"><button role="tab" aria-selected="true" aria-controls="cmp-panel">… with Left/Right arrow keys moving between tabs (remedy: None)
14. **[Reflex P1] A11-109 Keep reading order and screen-reader order equal to visual order.** (1x). hero theme fan (focus stops 4-12)  
   Evidence: focus.json: the fanned theme cards take focus in DOM order Atelier (y 646), Furrow (524), Cobalt (488), Studio, Ribbon, Dose, Coral, Bloom, then Furrow again; 'Furrow' appears twice (stops 5 and 12) linking to the same themes/furrow/.  
   Fix: Remove the duplicate card from the tab order (tabindex="-1" and aria-hidden on the repeat) and keep DOM order equal to left-to-right visual order after each deal (remedy: None)
15. **[Reflex P1] A11-011 Reduced motion respected** (1x). headline word animation (h1.hl.is-run)  
   Evidence: The h1 is built from per-word spans plus 'ghost' spans ('A', 'The') with an slash svg animating a word swap; the sweep flags overshoot easing cubic-bezier(0.3, 1.35, 0.5, 1). Ghost spans are aria-hidden, so the read name is fine, but the swap animation is not shown with a reduced-motion alternative in the evidence.  
   Fix: @media (prefers-reduced-motion: reduce) { .hl__ghost { display: none } .hl__w { animation: none } } (remedy: fix-motion)

6 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Content in tiles 1440-03..07 did not paint in the capture (scroll-reveal); its visual contrast and reflow were not checked.
- a11y: Image alt text: dom capture does not record alt values; sweep img_alt reported no misses.
- a11y: Live keyboard checks of tabs, slider and wheel (no Playwright run).
- slop: Tiles 1440-03 to 07 and 375-04 onward are blank: scroll-reveal sections never painted in the full-page capture (sweep ROB-001: 66% hidden after load). Focus crops (e.g. focus/31-on.png 'Show all 50 themes') show the content renders when scrolled to, so the empty bands are a capture limit and were not judged as design.
- slop: Brand brief: none supplied
