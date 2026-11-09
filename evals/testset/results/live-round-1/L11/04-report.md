# Unslop report: https://gameghost.manus.space

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
| Integrity | 9 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (13x). div.gg-engagement.flex > div.flex.min-w-0:nth-of-type(2) > a.flex.min-w-0 > span.min-w-0:nth-of-type(2) > span.block.text-\[10px\]:nth-of-type(2)  "1 subscribers"  
   Evidence: 3.68:1 against the background behind the text (10th-percentile pixel #050101, worst 3.67:1; text #ffffff, opacity 0.40, 10px; needs 4.5:1). APCA Lc 24 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (7x). input ""  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
3. **[Floor P0] A11-006 Controls have accessible names** (5x). div.h-\[100dvh\].bg-black:nth-of-type(1) > div.gg-desktop-topbar.hidden:nth-of-type(4) > div.gg-discord-search.flex-1:nth-of-type(2) > div.relative > input.file\:text-foreground.placeholder\:text-muted-foreground  
   Evidence: input[type=text] has no accessible name  
   Fix: Add visible text or aria-label. (remedy: fix-a11y)
4. **[Floor P0] TYP-004 The intended font actually renders** (2x). div:nth-of-type(1) > div.h-\[100dvh\].bg-black:nth-of-type(1) > div.gg-desktop-instructions.hidden:nth-of-type(6) > div.flex.items-center:nth-of-type(2) > span:nth-of-type(1)  "made with"  
   Evidence: declared "Share Tech Mono" but Consolas drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
5. **[Floor P0] A11-009 Zoom never blocked** (1x). meta viewport  
   Evidence: maximum-scale=1 blocks zoom  
   Fix: Remove the restriction. (remedy: fix-a11y)
6. **[Floor P0] A11-010 Form fields have labels** (1x). div.h-\[100dvh\].bg-black:nth-of-type(1) > div.gg-desktop-topbar.hidden:nth-of-type(4) > div.gg-discord-search.flex-1:nth-of-type(2) > div.relative > input.file\:text-foreground.placeholder\:text-muted-foreground  
   Evidence: input[type=text] has no label (placeholder "Search games..." is not a label)  
   Fix: Add a visible label element. (remedy: fix-a11y)
7. **[Floor P0] A11-007 Headings and landmarks** (1x). focus.json order  
   Evidence: Tab order: search -> header buttons -> footer links 'TOS/EULA', 'Privacy', 'Upload a Game' (y 868) -> 'Enter Fullscreen' (y 16) -> Like / Follow / PLAY (y 540-600) -> FILTER dock. Focus jumps bottom-to-top before reaching the main action.  
   Fix: Reorder DOM so header -> game info and actions -> carousel -> footer; put 'Enter Fullscreen' in the header group (remedy: fix-a11y)
8. **[Floor P0] A11-011 Reduced motion respected** (1x). full-bleed background scene and theme audio  
   Evidence: Background is an animated game scene (transition-all 1s layers) and the page requests 'ps5_theme_*.mp3' (manifest network). A speaker icon button (x 1230) has no accessible name (sweep). No visible pause for the motion.  
   Fix: Do not autoplay audio; give the toggle aria-label="Mute music" with aria-pressed; add a pause for the background and honour prefers-reduced-motion (remedy: fix-motion)
9. **[Floor P0] A11-004 Target size** (1x). carousel selection state  
   Evidence: The selected cover is shown only by a cyan glow ring (1440 tile 00) with no text or aria-current; 'NEW GAME' vs 'COMING SOON' are distinguished by yellow vs teal badge colour as well as text (text present, fine).  
   Fix: aria-current="true" (or aria-selected in a listbox) on the selected cover and a non-colour cue such as scale plus outline thickness (remedy: fix-a11y)
10. **[Reflex P1] A11-004 Target size** (12x). div:nth-of-type(1) > div.h-\[100dvh\].bg-black:nth-of-type(1) > div.md\:hidden.absolute:nth-of-type(5) > div.flex.items-center:nth-of-type(2) > button.inline-flex.items-center:nth-of-type(1)  
   Evidence: touch target 36x36px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
11. **[Reflex P1] WEB-001 Performance budget** (9x). https://gameghost.manus.space/gg-logo.png  
   Evidence: image is 519px wide but shown at 43px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
12. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
13. **[Reflex P1] A11-002 Text size floors** (7x). div:nth-of-type(1) > div.h-\[100dvh\].bg-black:nth-of-type(1) > div.gg-desktop-instructions.hidden:nth-of-type(6) > div.flex.items-center:nth-of-type(2) > span:nth-of-type(2)  "by Alex St. Louis for gamers everywhere"  
   Evidence: 39-character run at 13px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
14. **[Reflex P1] SLP-007 No stock gradient pairs** (4x). div:nth-of-type(1) > div.h-\[100dvh\].bg-black:nth-of-type(1) > div.gg-desktop-instructions.hidden:nth-of-type(6) > div.flex.items-center:nth-of-type(2) > span:nth-of-type(1)  "made with"  
   Evidence: gradient 4 stops + hue span 42° + banned pair (hues 265-330 with 200-264): #7b9ccc, #a78bfa, #93c5fd, #c4b5fd  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
15. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (3x). :root --color-slate-50  
   Evidence: token --color-slate-50: oklch(98.4% .003 247.858) is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)

13 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 1 type roles
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 53 other request(s) blocked, e.g. script https://plausible.io/js/script.file-downloads.hash.outbound-links.pageview-props.re
- a11y: No live keyboard run: arrow-key carousel, filter dock and Escape behaviour unverified.
- a11y: Fonts (Exo 2) blocked; contrast of fallback rendering only.
- a11y: Contrast hits on '1 subscribers' and gradient cart button not disputed; they look real in the tile.
- slop: Exo 2 display font and theme audio were blocked (manifest network); typography judged on the fallback face only.
- slop: Background is a video/animated scene seen as a still; motion not judged.
- slop: Rights to commercial game covers (Simpsons, Super Monkey Ball, Stormgate) are outside this lens.
