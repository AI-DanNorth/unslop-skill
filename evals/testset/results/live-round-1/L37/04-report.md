# Unslop report: https://reallygoodemails.com/emails/see-you-next-week

**Verdict (draft): fix**. Profile: balanced. 8 Floor finding(s) open.

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
| Integrity | 2 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). div.fzoqgU.kTqceP:nth-of-type(1) > nav.dZAGkW > ol.czaAKm > li.fghBKR:nth-of-type(1) > a  "Home"  
   Evidence: 3.95:1 against the background behind the text (10th-percentile pixel #ffffff, worst 3.95:1; text #808080, 16px; needs 4.5:1). APCA Lc 67 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (10x). a ""  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
3. **[Floor P0] INT-001 No invented metrics** (4x). div.fPSBzf.iRgpoQ:nth-of-type(2) > div.ddgODW.gPeiPq:nth-of-type(2) > div.fPSBzf.iHMUPj > a.featured__wrapper > small.featured__text  "Ad: 5 days. Full migration. Up to 35% less. Omnise"  
   Evidence: "35% less" (invented-metrics/percent-claims, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
4. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 172 characters (33% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
5. **[Floor P0] ROB-003 No horizontal overflow** (1x). div.eLANVt:nth-of-type(1) > div.navbar_component.w-nav > div.navbar_container:nth-of-type(1) > div.navbar10_menu-button.w-nav-button:nth-of-type(3) > div.menu-icon5  
   Evidence: page is 383px wide at a 375px viewport (sideways scroll); widest culprit 48px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
6. **[Floor P0] A11-114 Meaningful images get alt describing what they show** (1x). the email preview image (894x1257 at 1440)  
   Evidence: dom-1440.json: alt="See you next week." (the subject line). The image contains all of the email's information: 'Action packed. WWDC24 June 10–14', 'Watch the keynote. Monday, June 10, at 10:00 a.m. PT. Streaming from Apple Park on apple.com.', 'Add to calendar', the legal footer. A screen-reader user gets only the subject. The 'Text' tab may hold the text version, but the image itself fails.  
   Fix: alt="Apple WWDC24 email: glowing Apple logo; 'Action packed. WWDC24, June 10–14. Watch the keynote Monday June 10 at 10:00 a.m. PT, streaming from Apple Park on apple.com.' Add to calendar." or aria-describedby pointing at the Text tab panel (remedy: None)
7. **[Floor P0] A11-171 Muted text on brand bands / effects / photos.** (1x). inside the email: legal footer and grey body lines (tile 1440-01)  
   Evidence: Footer 'TM and © 2024 Apple Inc. ... If you prefer not to receive commercial email from Apple ... click here' is mid-grey at about 12px (rendered smaller in the scaled image) on black; by eye it is under 4.5:1, and the unsubscribe link is 'click here'.  
   Fix: In the source email: #a1a1a6 or lighter on black and link text 'Unsubscribe from Apple marketing email' (remedy: None)
8. **[Floor P0] A11-126 Focus not obscured (AA): sticky headers, banners, chat widgets never fully cover the focus** (1x). fixed 'Legal and Privacy info' button bottom right  
   Evidence: Tile 1440-00 and 375-00: the fixed pill overlaps the ad at 1440 and the email preview at 375; sweep focus_ring marks several stops as covered by a fixed element.  
   Fix: Put the legal link in the footer flow, or add scroll-padding-bottom equal to its height (remedy: None)
9. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (34x). :root --bzTONN  
   Evidence: token --bzTONN: #8b5cf6 is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)
10. **[Reflex P1] A11-004 Target size** (12x). body.__className_f44d07 > div.eLANVt:nth-of-type(1) > div.navbar_component.w-nav > div.navbar_container:nth-of-type(1) > a.navbar_logo-link.w-nav-brand  
   Evidence: touch target 100x41px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
11. **[Reflex P1] CPY-005 No slop diction** (8x). div.fPSBzf.iRgpoQ:nth-of-type(2) > div.ddgODW.gPeiPq:nth-of-type(2) > div.fPSBzf.iHMUPj > div.bCShOO.cYzMrZ > a.ervFBh.kNmSrs  "Sign up to Really Good Emails for free"  
   Evidence: "Really" (buzzwords/weak-intensifiers, cap budget 3, found 10)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
12. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .profileButton  
   Evidence: "transition: all var(--duration-normal) var(--ease-in-out)": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
13. **[Reflex P1] A11-007 Headings and landmarks** (3x). page  
   Evidence: 0 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
14. **[Reflex P1] WEB-001 Performance budget** (2x). naws.com/ads-images/e010cac2-c11c-45f2-95be-2c092c52194b.png  
   Evidence: image is 275px wide but shown at 24px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
15. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html.__variable_f44d07.w-mod-ix > body.__className_f44d07 > div.eFGelv:nth-of-type(3) > div.fzrkfx.fzrkfc:nth-of-type(2) > h2.hEYtOD.ijJXBY  "You might also like"  
   Evidence: display text at 30px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)

5 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 6 other request(s) blocked, e.g. fetch https://reallygoodemails.com/api/banner
- a11y: the Text and Code tabs were not opened, so whether the text alternative is complete is not verified
- a11y: several site scripts were blocked during capture (manifest network.blocked); dropdown menus (summary/details) not exercised
- a11y: cookie banner accepted by capture prep; not part of the judgment
- slop: the gallery page's Omnisend ad and the 'You might also like' grid are third-party content around the artifact and were not judged as part of it; the sweep's INT-001 '35% less' hit is in that ad
- slop: email rendered as a flattened PNG by the gallery; live HTML of the email not available
- slop: no 00-contract.md brief
