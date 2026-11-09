# Unslop report: https://cineyx.ai

**Verdict (draft): fix**. Profile: balanced. 9 Floor finding(s) open.

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
| Integrity | 5 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). section.py-24.px-6:nth-of-type(9) > div.max-w-5xl.mx-auto > div.grid.grid-cols-1:nth-of-type(2) > button.glass-card.p-6:nth-of-type(5) > p.text-xs.text-muted-foreground  "Pick a voice, clone your own, and dub in any langu"  
   Evidence: 4.22:1 against the background behind the text (10th-percentile pixel #101319, worst 4.22:1; text #a9b5c6, opacity 0.63, 12px; needs 4.5:1). APCA Lc 30 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (10x). button "Send feedback"  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
3. **[Floor P0] A11-004 Target size** (6x). div.min-h-screen.text-foreground:nth-of-type(2) > section.relative.z-10:nth-of-type(1) > div.relative.z-10:nth-of-type(2) > div.mt-12.flex:nth-of-type(2) > button.h-1\.5.rounded-full:nth-of-type(2)  
   Evidence: target 8x6px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
4. **[Floor P0] ROB-001 Content never depends on animation to appear** (3x). reduced_motion  
   Evidence: 3204 characters (84% of text) stay invisible with reduced motion  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
5. **[Floor P0] A11-112 Every control has an accessible name** (1x). 'What you can actually create' cards 1 and 3, image links  
   Evidence: dom-1440.json: <a href="/cinematic-studio?quickstart=1"> and <a href="/ai-design"> wrapping the before/after images have accessible name 'BEFORE AFTER' (taken from the corner badges); the images inside carry alt text but the badge text wins. Out of context two links both say 'BEFORE AFTER' and go to different studios.  
   Fix: aria-hidden="true" on the BEFORE/AFTER badges and aria-label="Restore and enhance old photos: open AI Design" on the link, or make the image link tabindex=-1 since 'Open AI Design' duplicates it (remedy: None)
6. **[Floor P0] A11-109 Keep reading order and screen-reader order equal to visual order.** (1x). focus order, page start  
   Evidence: focus.json stop 0 is the fixed bottom-right 'Send feedback' bug button (x1380 y832), before the logo and nav. There is no skip link and no <main> (sweep).  
   Fix: Move the feedback button to the end of the body; add <a class="skip" href="#main">Skip to content</a> first and wrap content in <main id="main"> (remedy: None)
7. **[Floor P0] A11-011 Reduced motion respected** (1x). 'Thumbnails' section, three rows of cover images  
   Evidence: dom-1440.json: div.flex.gap-3 rows run CSS animations 'marquee' 28s, 'marquee-reverse' 32s and 'marquee' 26s continuously; no pause control visible in tiles.  
   Fix: Add a pause button (and pause on hover/focus), and set animation: none under prefers-reduced-motion: reduce (remedy: fix-motion)
8. **[Floor P0] A11-121 Every function is operable by keyboard** (1x). 'Soundtracks, music, and SFX' card  
   Evidence: focus.json: an <audio controls> element (stops at x624 y2170) sits inside the card <a href="/audio-studio"> (stop at x536 y2046). Interactive content nested in a link: activating the player can follow the link, and the audio stop appears twice in the tab order.  
   Fix: Make the card a <div> with the heading as the link (stretched-link pattern) so the audio player is a sibling, not a descendant (remedy: None)
9. **[Floor P0] A11-171 Muted text on brand bands / effects / photos.** (1x). hero tagline 'AI VIDEO & CHARACTER STUDIO — NO EXPERIENCE NEEDED' (tile 1440-00)  
   Evidence: Caps tagline tracked so tight the words touch ('AIVIDEO&CHARACTERSTUDIO—NOEXPERIENCENEEDED' as rendered at 1440), mid-grey on a photo; legibility fails by eye even where contrast may pass.  
   Fix: letter-spacing: 0.02em or normal; sentence case (remedy: None)
10. **[Reflex P1] SLP-193 Ban the accented word: one word or phrase of a heading set apart by colour, weight, highli** (1x). h1 and every section h2 (tiles 1440-00, 1440-03, 1440-05)  
   Evidence: The same cyan #12c0e2 to amber #f69e23 gradient clip is applied to one word or phrase of each heading: 'MiniMax H3', 'AI that remembers your universe', 'Ecosystem of studios', 'Cineyx AI Mobile.', 'Start for free', 'Want to go all the way?'. The device repeats on 8 headings, so it no longer marks anything.  
   Fix: Plain heading colour; keep the gradient (if at all) for the logo or one hero moment (remedy: None)
11. **[Reflex P1] SLP-003 No icon tiles above every card heading** (9x). section.relative.z-10:nth-of-type(3) > div.max-w-5xl.mx-auto > div.grid.sm\:grid-cols-3:nth-of-type(2) > div.glass-card.p-6:nth-of-type(1) > div.w-12.h-12  
   Evidence: 48px tinted tile above heading "Projects & Episodes" (8 repeats)  
   Fix: Remove the tiles, or use a real image or figure that differs per card. (remedy: fix-quieter)
12. **[Reflex P1] SLP-007 No stock gradient pairs** (8x). section.relative.z-10:nth-of-type(1) > div.relative.z-10:nth-of-type(2) > div:nth-of-type(1) > h1.text-4xl.sm\:text-5xl > span.text-gradient-primary:nth-of-type(2)  "MiniMax H3"  
   Evidence: gradient hue span 149°: #12c0e2, #f69e23  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
13. **[Reflex P1] MOT-001 Motion CSS hygiene** (7x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
14. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (6x). section.relative.z-10:nth-of-type(1) > div.relative.z-10:nth-of-type(2) > div:nth-of-type(1) > div.mb-5:nth-of-type(1) > span.ml-2.inline-flex:nth-of-type(2)  "in 2K"  
   Evidence: zero-offset coloured boxShadow #dc2828 blur 24px alpha 0.55  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
15. **[Reflex P1] A11-004 Target size** (6x). div > div.min-h-screen.text-foreground:nth-of-type(2) > nav.fixed.top-0 > div.max-w-6xl.mx-auto > a.flex.items-center  
   Evidence: touch target 39x40px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)

21 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 2 other request(s) blocked, e.g. media https://cineyx.ai/__l5e/assets-v1/8f3f7b00-e9a1-4f75-971e-9a9fae85c61a/minimax-h3-pr
- a11y: disputed: sweep focus_ring marks all 40 focus stops 'covered by a fixed or sticky element'; the crops (focus/02-on.png, focus/12-on.png) show the focused items fully visible, including nav items that are themselves inside the fixed nav. Likely a detector false positive on this page.
- a11y: whether the hero carousel auto-advances (2.2.2) could not be told from stills; hero promo videos were blocked in capture
- a11y: keyboard behaviour of the carousel and language switch: no live keyboard test run
- a11y: forms: none on the captured page
- slop: hero promo videos were blocked in capture (minimax-h3-promo.mp4, seedance-2-5-promo.mp4); the hero still is a poster frame and was not judged
- slop: carousel slides 2-8 not captured
- slop: no 00-contract.md brief; judged without overrides
