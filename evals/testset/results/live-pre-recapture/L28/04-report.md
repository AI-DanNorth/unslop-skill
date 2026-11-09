# Unslop report: https://landonorris.com

**Verdict (draft): fix**. Profile: balanced. 7 Floor finding(s) open.

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

1. **[Floor P0] A11-003 Visible focus everywhere** (3x). button "Open navigation menu"  
   Evidence: no visible focus indicator (outline: none 3px rgb(17, 17, 18))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] A11-001 Text contrast on real pixels** (2x). div.c.home-hero > div.home-hero-touch-controls-w:nth-of-type(4) > div.home-hero-touch-desc-w > div.touch-desc-inner:nth-of-type(1) > div.text-eyebrow.touch-desc  "tap to lock"  
   Evidence: 1.08:1 against the background behind the text (10th-percentile pixel #fcfcfa, worst 1.08:1; text #f4f4ed, 8px; needs 4.5:1). APCA Lc 0 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] A11-004 Target size** (2x). div.footer-inner-layout > div.footer-links-w:nth-of-type(1) > div.footer-links-col:nth-of-type(1) > div.footer-links-layout:nth-of-type(2) > a.text-link-w.w-inline-block:nth-of-type(1)  
   Evidence: target 42x17px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
4. **[Floor P0] A11-011 Reduced motion respected** (2x). stylesheet  
   Evidence: page moves (keyframes translateXLeft, translateXRight) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
5. **[Floor P0] A11-112 Every control has an accessible name** (1x). all hover-swap links and buttons (header, menu, footer, CTAs)  
   Evidence: dom-1440.json accessible names are doubled because the hover duplicate text is not hidden: 'Store STORE', 'HomeHome', 'On TrackOn Track', 'CalendarCalendar', 'tiktoktiktok', 'instagraminstagram', 'business enquiries business enquiries', 'Las Vegas LAS VEGAS gp GP', 'view on track VIEW ON TRACK'.  
   Fix: Add aria-hidden="true" to the duplicate (animated) span so the name is read once: <span aria-hidden="true" class="hover-copy">STORE</span> (remedy: None)
6. **[Floor P0] A11-103 Use landmarks and semantic elements** (1x). page landmarks and headings  
   Evidence: landmarks: main 1, nav 0, header 0, footer 0. The h1 'Lando Norris' and section h2s ('ON', 'TRACK', 'OFF', 'Helmets') are hidden copies while the visible headings are empty h2 elements (text drawn as split spans/images). No skip link; first focusable is the logo link.  
   Fix: One heading per section with its real text ('On track', 'Off track', 'Helmets hall of fame'); wrap the menu in <nav aria-label="Main">, the bottom links in <footer>; add a skip link (remedy: None)
7. **[Floor P0] A11-125 Switch ring colour on coloured bands so it holds 3:1 there.** (1x). focus ring on light hero (focus/03-on.png, 'Go to home')  
   Evidence: The focus ring is a solid 2px lime rgb(210,255,0) outline. On the off-white hero (#fcfcfa) lime gives about 1.1:1, so the ring around the centre LN mark is barely visible in the crop; it only works on the dark sections.  
   Fix: Add a dark second ring on light areas: outline: 2px solid #d2ff00; box-shadow: 0 0 0 4px #111 (or switch to a dark outline inside .is-light sections) (remedy: None)
8. **[Reflex P1] WEB-001 Performance budget** (28x). page  
   Evidence: lab LCP 7204ms (fail > 4500ms)  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
9. **[Reflex P1] A11-004 Target size** (10x). body > div.nav:nth-of-type(2) > div.nav-inner:nth-of-type(1) > div.page-ln4-pos:nth-of-type(2) > a.nav-middle.w-inline-block  
   Evidence: touch target 26x26px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
10. **[Reflex P1] A11-002 Text size floors** (5x). div.c.home-hero > div.home-hero-next-race-w:nth-of-type(2) > div.home-hero-next-race-top:nth-of-type(2) > div.text-eyebrow:nth-of-type(2) > span.line  "Next Race"  
   Evidence: label at 8px (label floor 12px; 36 such)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
11. **[Reflex P1] LAY-004 No dead bands** (4x). y 801-1672 at 1280px  
   Evidence: 871px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
12. **[Reflex P1] TYP-002 Sizes on a declared ladder** (2x). whole page  
   Evidence: 19 distinct font sizes: 8.5, 10, 12, 13.5, 14, 15, 16.5, 20, 25, 26.5, 32, 60, 62.5, 70, 72.5, 93.5, 97.5, 106, 110 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
13. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: 0 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
14. **[Reflex P1] MOT-001 Motion CSS hygiene** (1x). .scroll-indicator-bar  
   Evidence: transition on a layout property: "height"  
   Fix: Animate transform or opacity instead (remedy: fix-motion)
15. **[Reflex P1] A11-126 Focus not obscured (AA): sticky headers, banners, chat widgets never fully cover the focus** (1x). all 26 focus stops  
   Evidence: focus.json marks every stop covered=true, including footer links at y 13,200+; something fixed (likely the full-screen canvas or a pinned layer) sits over focused elements.  
   Fix: pointer-events: none and a lower z-index on the decorative fixed layer, or raise :focus-visible elements (position: relative; z-index above the layer) (remedy: None)

4 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 1 type roles
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 17 other request(s) blocked, e.g. fetch https://landonorris.com/avljl2rk9q5pNjdiNWEwMmRjNWQzMzg5NjBiMTdhN2U5/ga/g/c?v=2&tid=
- a11y: Helmet image alt text: the DOM capture does not record alt values
- a11y: Reduced-motion and canvas behaviour live (sweep says no prefers-reduced-motion rule; not re-tested)
- a11y: disputed: sweep A11-001 hits at 1.00:1 on 'results' are likely captured mid reveal animation, not the final colour
- slop: The hero and several scroll-pinned sections (tiles 01, 03-07) painted as flat colour: WebGL/scroll-driven content did not render in the full-page capture. Not judged as design.
- slop: Store section heading in tile 11 is near-invisible dark-on-dark; likely captured mid-reveal animation (sweep contrast 1.00:1 hits on 'results' are probably the same cause).
