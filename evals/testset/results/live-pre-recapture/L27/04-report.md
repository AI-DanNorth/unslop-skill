# Unslop report: https://stripe.com

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
| Integrity | 9 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-003 Visible focus everywhere** (10x). button "Accept and optimise payments globally – online and in person"  
   Evidence: no visible focus indicator (outline: none 3px rgb(0, 0, 0))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] A11-001 Text contrast on real pixels** (4x). #stat-historical-uptime-description  "for Stripe services"  
   Evidence: 3.06:1 against the background behind the text (10th-percentile pixel #2d2684, worst 3.03:1; text #6480b2, 16px; needs 4.5:1). APCA Lc 27 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] ROB-001 Content never depends on animation to appear** (2x). observer_never_fires  
   Evidence: 1054 characters (13% of text) stay invisible when IntersectionObserver never fires  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
4. **[Floor P0] A11-166 Measure contrast against real pixels: over gradients/photos test darkest and lightest stop** (1x). hero h1 continuation over the ribbon (tile 1440-00, x 850-1130, y 270-420)  
   Evidence: The words 'your revenue.', 'services and', 'from' render in a blended purple (sampled about rgb(118,85,252)) directly over the pink/orange ribbon (sampled rgb(254,125,126) and rgb(190,170,252)): roughly 1.9:1 to 2.5:1. The sweep's contrast hits are all inside product mock graphics and did not catch this.  
   Fix: Keep the headline column clear of the ribbon (max-width or ribbon starting right of the text), or add a white text-shadow/backplate at 4.5:1 on the darkest stop (remedy: None)
5. **[Floor P0] A11-011 Reduced motion respected** (1x). customer logo marquee under the hero  
   Evidence: div.logo-carousel__marquee scrolls continuously (logos cut off at the left edge, 'AI' in tile 1440-00); dom-1440.json has no control named pause/stop/play.  
   Fix: A visible pause button, and pause on hover and focus (remedy: fix-motion)
6. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). product bento expand buttons ('Accept and optimise payments globally – online and in person', 'Enable any billing model' ...)  
   Evidence: Confirms sweep A11-003: focus.json records outline: none on these card buttons; the small expand icon at the card corner is the only affordance and shows no ring.  
   Fix: .bento-card button:focus-visible { outline: 2px solid #533afd; outline-offset: 2px } (remedy: None)
7. **[Reflex P1] SLP-222 Swap / rival's-name test: any head still true with a competitor's name (or the same trade ** (1x). mid and lower section heads (tiles 1440-04 to 1440-07)  
   Evidence: T-RIVAL-NAME / T-FRESH-READER: 'The backbone of global commerce', 'Powering businesses of all sizes', 'Flexible solutions for every business model.', 'Build a foundation for your startup that enables faster growth' all stay true with Adyen or PayPal swapped in. The hero and the stats under these heads are specific; the heads are not.  
   Fix: Lead with the number the section proves, e.g. 'US$1.9tn processed in 2025' as the head (remedy: None)
8. **[Reflex P1] A11-004 Target size** (12x). nav.hds-navigation-menu.navigation-menu > a.hds-link.navigation-menu-home-link  
   Evidence: touch target 60x25px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
9. **[Reflex P1] SLP-003 No icon tiles above every card heading** (8x). section.section-row.section-row-gap:nth-of-type(1) > div.section-row.section-row-gap:nth-of-type(2) > div.columns.columns--auto > div.feature-detail:nth-of-type(1) > div.charm-icon:nth-of-type(1)  
   Evidence: 40px tinted tile above heading "Professional services." (8 repeats)  
   Fix: Remove the tiles, or use a real image or figure that differs per card. (remedy: fix-quieter)
10. **[Reflex P1] CPY-005 No slop diction** (8x). div.testimonial-carousel-container:nth-of-type(2) > div:nth-of-type(1) > div.testimonial-carousel__cards > div.testimonial-card.testimonial-carousel__card:nth-of-type(3) > q.testimonial-card__quote  "With Stripe, we're able to integrate new features "  
   Evidence: "quickly" (buzzwords/weak-intensifiers, cap budget 3, found 5)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Reflex P1] CPY-006 No repeated labels inside a card** (5x). div.connect-platform-graphic > div.connect-platform-graphic__dashboard-browser:nth-of-type(2) > div.browser-graphic > div.browser-graphic__page:nth-of-type(2) > div.connect-platform-graphic__dashboard  
   Evidence: "Canada" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
12. **[Reflex P1] SLP-007 No stock gradient pairs** (4x). div.billing-plan-graphic__plan-content > div.billing-plan-graphic__usage:nth-of-type(3) > div.billing-plan-graphic__usage-bar:nth-of-type(2) > div.billing-plan-graphic__usage-progress-wrapper > div.billing-plan-graphic__usage-progress  
   Evidence: gradient hue span 156°: #7232f1, #fb76fa, #ffcf5e  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
13. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (2x). div.modular-solutions-bento-card__content-inner > div.modular-solutions-bento-card__graphic > div.billing-plan-graphic__wrapper > div.billing-plan-graphic__background:nth-of-type(1) > div.billing-plan-graphic__background-gradient-1:nth-of-type(1)  
   Evidence: radial spotlight #533afd alpha 0.80  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
14. **[Reflex P1] TYP-001 Clear type hierarchy** (2x). h2 vs h3  
   Evidence: h2 32px is only 1.23x h3 26px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)
15. **[Reflex P1] TYP-002 Sizes on a declared ladder** (2x). whole page  
   Evidence: 17 distinct font sizes: 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 26, 32, 48, 56 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)

19 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- reduced_motion (A11-011): not-verified: 8 stylesheet(s) could not be read; a prefers-reduced-motion rule may be in them
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 2 image(s) could not load (network blocked); imagery and layout around them not verified
- capture: 12 other request(s) blocked, e.g. fetch https://r.stripe.com/0
- a11y: disputed: sweep A11-007 '2 visible h1 elements' — the second h1 is aria-hidden=true and visually stacked on the first for a blend effect; only one is exposed.
- a11y: disputed: all 15 sweep contrast hits are text inside illustrative product mock graphics ('Continue', 'Weiter', 'taro.yamada@example.com'); these are part of pictures and may be exempt under 1.4.3 if the graphics are marked aria-hidden; confirm they are hidden from AT.
- a11y: stats band captured mid-animation (numbers faded); contrast there not verified
- a11y: keyboard operation of mega-menus and the testimonial carousel: no live keyboard test
- slop: stats band (tile 1440-04) was captured mid-animation, numbers partly faded; not judged
- slop: no 00-contract.md brief; brand ownership of the ribbon and indigo judged from general knowledge of the site
