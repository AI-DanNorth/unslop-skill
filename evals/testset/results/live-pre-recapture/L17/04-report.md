# Unslop report: https://uupm.cc

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
| Integrity | 8 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). nav.fixed.top-4 > div.px-4.sm\:px-6 > div.flex.items-center > div.flex.items-center:nth-of-type(2) > a.inline-flex.items-center:nth-of-type(2)  "Premium"  
   Evidence: 3.84:1 against the background behind the text (10th-percentile pixel #387ef5, worst 3.84:1; text #ffffff, 14px; needs 4.5:1). APCA Lc 71 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (5x). a "View Demo"  
   Evidence: no visible focus indicator (outline: auto 1px rgb(241, 241, 241))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
3. **[Floor P0] A11-002 Text size floors** (3x). div.max-w-3xl.mx-auto > div.space-y-4:nth-of-type(2) > div.glass-card.p-5:nth-of-type(7) > div.bg-gray-900.rounded-lg:nth-of-type(2) > div.text-gray-500:nth-of-type(1)  "<!-- Pet Grooming Landing -->"  
   Evidence: 29-character run at 11px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
4. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 809 characters (16% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
5. **[Floor P0] A11-112 Every control has an accessible name** (1x). nav, GitHub star button  
   Evidence: focus.json stop 6: link accessible name is '146.9k' only (GitHub icon has no text). Out of context it does not say it goes to the GitHub repo.  
   Fix: <a aria-label="Star on GitHub, 146.9k stars"> or visually hidden 'GitHub stars:' before the number (remedy: None)
6. **[Floor P0] A11-115 Expose correct state attributes: aria-expanded on menu/accordion triggers, aria-pressed/ar** (1x). gallery filter chips ('All', 'SaaS', 'Education', 'Pet Services' ... 'Creative')  
   Evidence: Filter buttons at y4896 are plain <button>s; the active filter is shown by fill colour only and dom-1440.json records no role or pressed state.  
   Fix: aria-pressed="true|false" on each chip inside role="group" aria-label="Filter demos"; announce 'Showing 6 of 39 demos' in an aria-live="polite" region (remedy: None)
7. **[Floor P0] A11-168 Never convey information by colour alone** (1x). gallery footer line (tile 1440-06)  
   Evidence: '39 demos available • 20 categories • 26 light • 13 dark' distinguishes its terms only by colour (blue, orange, green) and the 'Light'/'Dark' badges on cards rely on white vs black fill; the colours carry no extra meaning, but the 'Colors:' swatch rows on each demo card present palettes as colour dots only with no text values.  
   Fix: Add hex values as text or a title/aria-label per swatch ('#3B82F6 primary') (remedy: None)
8. **[Reflex P1] SLP-193 Ban the accented word: one word or phrase of a heading set apart by colour, weight, highli** (1x). h1 and every h2  
   Evidence: Blue #2563eb to orange #f97316 gradient on the last word of each heading: 'UI UX Pro Max', 'Beautiful UI', 'How It Works', 'Build with Us', and others (18 gradient hits in sweep). The h2s are split so the gradient word sits in a separate span ('Supported' + gradient, 'How It' + gradient).  
   Fix: Plain headings; reserve the gradient for the wordmark only (remedy: None)
9. **[Reflex P1] SLP-007 No stock gradient pairs** (18x). main.flex-1 > div.min-h-screen.bg-light-bg > main > section.relative.min-h-screen:nth-of-type(1) > div.absolute.inset-0:nth-of-type(1)  
   Evidence: gradient 6 stops: #2563eb, #000000, #f97316, #000000, #3b82f6  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
10. **[Reflex P1] CPY-005 No slop diction** (13x). main > section.section-padding.bg-light-surface:nth-of-type(6) > div.max-w-7xl.mx-auto > div.text-center.mb-12:nth-of-type(1) > p.text-lg.text-light-muted  "Explore more tools and platforms built by our team"  
   Evidence: "supercharge" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Reflex P1] A11-004 Target size** (12x). div.flex.min-h-screen:nth-of-type(2) > nav.fixed.top-4 > div.px-4.sm\:px-6 > div.flex.items-center > a.flex.items-center  
   Evidence: touch target 28x28px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
12. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (7x). :root --color-primary-light  
   Evidence: token --color-primary-light: #3b82f6 is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)
13. **[Reflex P1] WEB-001 Performance budget** (7x). https://uupm.cc/thumbnails/luxury-ecommerce.png  
   Evidence: image is 873KB (max 400KB)  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
14. **[Reflex P1] SLP-002 No decorative section numbering** (6x). div.max-w-3xl.mx-auto > div.space-y-4:nth-of-type(2) > div.glass-card.p-5:nth-of-type(1) > div.flex.items-center:nth-of-type(1) > div.w-7.h-7  "1"  
   Evidence: section number "1" (12px) beside heading "Your Prompt"; 6 on page  
   Fix: Remove the numbers or make them real steps. (remedy: fix-typeset)
15. **[Reflex P1] SLP-010 No template chrome glyphs** (5x). section.section-padding.bg-light-surface:nth-of-type(6) > div.max-w-7xl.mx-auto > div.text-center.mb-12:nth-of-type(1) > div.inline-flex.items-center > span:nth-of-type(1)  "🚀"  
   Evidence: template chrome (emoji-bullets): "🚀"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)

21 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 15 other request(s) blocked, e.g. fetch https://www.google-analytics.com/g/collect?v=2&tid=G-K2FCTVRB44&gtm=45je6b41h1v92429
- a11y: disputed: sweep A11-003 flags 'View Demo' and 'Show Prompt' with no visible focus (outline auto 1px light grey); on the dark ground a light 1px auto outline is visible but thin; recorded as not verified from crops.
- a11y: the typing-cursor animation in the install line ('uipro init --ai claude▋') could be a 2.2.2 issue if it loops; not determinable from stills
- a11y: keyboard operation of filters and 'Load More': no live test
- a11y: light theme not captured
- slop: gallery thumbnails rendered as empty dark boxes in tiles (lazy images loaded after the screenshot; alt and src are present in dom-1440.json), so the demo imagery was not judged
- slop: light theme (theme toggle) not captured
- slop: no 00-contract.md brief
