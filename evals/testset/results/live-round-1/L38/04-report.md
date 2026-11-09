# Unslop report: https://reallygoodemails.com/emails/welcome-to-apple-arcade

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
| Integrity | 4 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (16x). div.fzoqgU.kTqceP:nth-of-type(1) > nav.dZAGkW > ol.czaAKm > li.fghBKR:nth-of-type(1) > a  "Home"  
   Evidence: 3.95:1 against the background behind the text (10th-percentile pixel #ffffff, worst 3.95:1; text #808080, 16px; needs 4.5:1). APCA Lc 67 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (10x). a ""  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
3. **[Floor P0] INT-001 No invented metrics** (3x). div.fPSBzf.iRgpoQ:nth-of-type(2) > div.ddgODW.gPeiPq:nth-of-type(2) > div.fPSBzf.iHMUPj > a.featured__wrapper > small.featured__text  "Ad: 5 days. Full migration. Up to 35% less. Omnise"  
   Evidence: "35% less" (invented-metrics/percent-claims, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
4. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 161 characters (31% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
5. **[Floor P0] ROB-003 No horizontal overflow** (1x). div.eLANVt:nth-of-type(1) > div.navbar_component.w-nav > div.navbar_container:nth-of-type(1) > div.navbar10_menu-button.w-nav-button:nth-of-type(3) > div.menu-icon5  
   Evidence: page is 383px wide at a 375px viewport (sideways scroll); widest culprit 48px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
6. **[Floor P0] A11-110 Keep all words as real text in reading order** (1x). email preview (img at x 75, y 312, 894x3868)  
   Evidence: dom-1440.json: the entire email is one <img>; none of its text ('You're Going to Love It Here', body copy, CTAs, legal text) is in the page text. A separate 'Text' tab exists in the toolbar, but the default 'Desktop' view gives screen-reader users only the image's alt (value not recorded in capture).  
   Fix: Render the email HTML in an <iframe title="Email: Welcome to Apple Arcade"> by default, or give the image alt="" with an adjacent link 'Read the email as text' pointing to the Text tab (remedy: None)
7. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (34x). :root --bzTONN  
   Evidence: token --bzTONN: #8b5cf6 is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)
8. **[Reflex P1] A11-004 Target size** (12x). body.__className_f44d07 > div.eLANVt:nth-of-type(1) > div.navbar_component.w-nav > div.navbar_container:nth-of-type(1) > a.navbar_logo-link.w-nav-brand  
   Evidence: touch target 100x41px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
9. **[Reflex P1] CPY-005 No slop diction** (8x). div.fPSBzf.iRgpoQ:nth-of-type(2) > div.ddgODW.gPeiPq:nth-of-type(2) > div.fPSBzf.iHMUPj > div.bCShOO.cYzMrZ > a.ervFBh.kNmSrs  "Sign up to Really Good Emails for free"  
   Evidence: "Really" (buzzwords/weak-intensifiers, cap budget 3, found 8)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
10. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .profileButton  
   Evidence: "transition: all var(--duration-normal) var(--ease-in-out)": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
11. **[Reflex P1] A11-007 Headings and landmarks** (3x). page  
   Evidence: 0 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
12. **[Reflex P1] WEB-001 Performance budget** (2x). naws.com/ads-images/09f311cf-4922-4019-9702-c95efcce363a.png  
   Evidence: image is 1080px wide but shown at 24px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
13. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html.__variable_f44d07.w-mod-ix > body.__className_f44d07 > div.eFGelv:nth-of-type(3) > div.fzrkfx.fzrkfc:nth-of-type(2) > h2.hEYtOD.ijJXBY  "You might also like"  
   Evidence: display text at 30px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
14. **[Reflex P1] ROB-001 Content never depends on animation to appear** (1x). page after load  
   Evidence: 49% of text is hidden after load and scrolling (max 30%; menus and dialogs excluded)  
   Fix: Start visible; animate from visible. (remedy: fix-harden)
15. **[Reflex P1] ROB-002 Phone parity** (1x). div.navbar_searchbar_wrapper:nth-of-type(2) > button.fPSBzf.bYPztT > kbd.ddgODW.gPJqiE  "Ctrl K"  
   Evidence: 40 words shown at 1440px are hidden at 375px (4 elements)  
   Fix: Reflow instead of hiding. (remedy: fix-layout)

4 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 3 other request(s) blocked, e.g. fetch https://reallygoodemails.com/api/banner
- a11y: Alt value of the email image (not recorded in the DOM capture; sweep img_alt did not flag it)
- a11y: Live keyboard behaviour of the 'Find inspiration' / 'Create emails' <details> menus and the Ctrl K search
- a11y: Sweep Floor hits (focus covered by sticky header, missing main/h1, breadcrumb contrast 3.95:1) agree with tile 00
- slop: The surrounding Really Good Emails gallery chrome (header, ad slot, 'You might also like' grid) is host UI, not the artifact under review; not judged for slop beyond noting it.
- slop: The email is shown as a single raster image (894x3868); live HTML email rendering, dark mode and client quirks were not available.
