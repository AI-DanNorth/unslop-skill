# Unslop report: https://stripe.com

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). div.payments-graphic__terminal-screen > div.payments-graphic__terminal-transaction-button:nth-of-type(6) > div.payments-graphic__terminal-transaction-button-text > div.payments-graphic__terminal-transaction-button-text-values > div:nth-of-type(1)  "Continue"  
   Evidence: 2.41:1 against the background behind the text (10th-percentile pixel #ffe0d1, worst 2.41:1; text #ff6118, 10px; needs 4.5:1). APCA Lc 41 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-006 Controls have accessible names** (10x). div.logo-carousel > div.logo-carousel__marquee-container > ul.logo-carousel__marquee > li.logo-carousel__item:nth-of-type(1) > a.hds-link  
   Evidence: a has no accessible name  
   Fix: Add visible text or aria-label. (remedy: fix-a11y)
3. **[Floor P0] A11-003 Visible focus everywhere** (7x). button "Accept and optimise payments globally – online and in person"  
   Evidence: no visible focus indicator (outline: none 3px rgb(0, 0, 0))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
4. **[Floor P0] A11-002 Text size floors** (3x). div.dom-graphic__content.dom-graphic__content--horizontal-scale-left > div.no-code-graphic__card > div.no-code-graphic__messages-wrapper:nth-of-type(1) > div.no-code-graphic__messages > div.no-code-graphic__message.no-code-graphic__message--received:nth-of-type(1)  "Hi, I’m looking for a simple day cream with SPF?"  
   Evidence: 48-character run at 10px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
5. **[Floor P0] ROB-001 Content never depends on animation to appear** (3x). reduced_motion  
   Evidence: 697 characters (9% of text) stay invisible with reduced motion  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
6. **[Floor P0] A11-010 Form fields have labels** (1x). #newsletter-email  
   Evidence: input[type=email] has no label (placeholder "Enter work email" is not a label)  
   Fix: Add a visible label element. (remedy: fix-a11y)
7. **[Floor P0] A11-166 Measure contrast against real pixels: over gradients/photos test darkest and lightest stop** (1x). hero h1 continuation over the ribbon (tile 1440-00, x 850-1130, y 270-420)  
   Evidence: The words 'your revenue.', 'services and', 'from' render in a blended purple (sampled about rgb(118,85,252)) directly over the pink/orange ribbon (sampled rgb(254,125,126) and rgb(190,170,252)): roughly 1.9:1 to 2.5:1. The sweep's contrast hits are all inside product mock graphics and did not catch this.  
   Fix: Keep the headline column clear of the ribbon (max-width or ribbon starting right of the text), or add a white text-shadow/backplate at 4.5:1 on the darkest stop (remedy: None)
8. **[Floor P0] A11-011 Reduced motion respected** (1x). customer logo marquee under the hero  
   Evidence: div.logo-carousel__marquee scrolls continuously (logos cut off at the left edge, 'AI' in tile 1440-00); dom-1440.json has no control named pause/stop/play.  
   Fix: A visible pause button, and pause on hover and focus (remedy: fix-motion)
9. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). product bento expand buttons ('Accept and optimise payments globally – online and in person', 'Enable any billing model' ...)  
   Evidence: Confirms sweep A11-003: focus.json records outline: none on these card buttons; the small expand icon at the card corner is the only affordance and shows no ring.  
   Fix: .bento-card button:focus-visible { outline: 2px solid #533afd; outline-offset: 2px } (remedy: None)
10. **[Reflex P1] SLP-222 Swap / rival's-name test: any head still true with a competitor's name (or the same trade ** (1x). mid and lower section heads (tiles 1440-04 to 1440-07)  
   Evidence: T-RIVAL-NAME / T-FRESH-READER: 'The backbone of global commerce', 'Powering businesses of all sizes', 'Flexible solutions for every business model.', 'Build a foundation for your startup that enables faster growth' all stay true with Adyen or PayPal swapped in. The hero and the stats under these heads are specific; the heads are not.  
   Fix: Lead with the number the section proves, e.g. 'US$1.9tn processed in 2025' as the head (remedy: None)
11. **[Reflex P1] A11-004 Target size** (12x). nav.hds-navigation-menu.navigation-menu > a.hds-link.navigation-menu-home-link  
   Evidence: touch target 60x25px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
12. **[Reflex P1] SLP-003 No icon tiles above every card heading** (8x). section.section-row.section-row-gap:nth-of-type(1) > div.section-row.section-row-gap:nth-of-type(2) > div.columns.columns--auto > div.feature-detail:nth-of-type(1) > div.charm-icon:nth-of-type(1)  
   Evidence: 40px tinted tile above heading "Professional services." (8 repeats)  
   Fix: Remove the tiles, or use a real image or figure that differs per card. (remedy: fix-quieter)
13. **[Reflex P1] CPY-005 No slop diction** (8x). div.testimonial-carousel-container:nth-of-type(2) > div:nth-of-type(1) > div.testimonial-carousel__cards > div.testimonial-card.testimonial-carousel__card:nth-of-type(3) > q.testimonial-card__quote  "With Stripe, we're able to integrate new features "  
   Evidence: "quickly" (buzzwords/weak-intensifiers, cap budget 3, found 5)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
14. **[Reflex P1] CPY-006 No repeated labels inside a card** (5x). div.dom-graphic__content.dom-graphic__content--horizontal-scale-left > div.connect-platform-graphic > div.connect-platform-graphic__payment-card:nth-of-type(1) > div.connect-platform-graphic__payment-card-content.connect-platform-graphic__payment-card-content--daybreak-yoga:nth-of-type(3) > div.connect-platform-graphic__payment-screen.connect-platform-graphic__payment-screen--order-details:nth-of-type(2)  
   Evidence: "US$999.00" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
15. **[Reflex P1] SLP-007 No stock gradient pairs** (4x). div.billing-plan-graphic__plan-content > div.billing-plan-graphic__usage:nth-of-type(3) > div.billing-plan-graphic__usage-bar:nth-of-type(2) > div.billing-plan-graphic__usage-progress-wrapper > div.billing-plan-graphic__usage-progress  
   Evidence: gradient hue span 156°: #7232f1, #fb76fa, #ffcf5e  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)

21 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 2 other request(s) blocked, e.g. fetch https://r.stripe.com/0
- a11y: disputed: sweep A11-007 '2 visible h1 elements' — the second h1 is aria-hidden=true and visually stacked on the first for a blend effect; only one is exposed.
- a11y: disputed: all 15 sweep contrast hits are text inside illustrative product mock graphics ('Continue', 'Weiter', 'taro.yamada@example.com'); these are part of pictures and may be exempt under 1.4.3 if the graphics are marked aria-hidden; confirm they are hidden from AT.
- a11y: stats band captured mid-animation (numbers faded); contrast there not verified
- a11y: keyboard operation of mega-menus and the testimonial carousel: no live keyboard test
- slop: stats band (tile 1440-04) was captured mid-animation, numbers partly faded; not judged
- slop: no 00-contract.md brief; brand ownership of the ribbon and indigo judged from general knowledge of the site
