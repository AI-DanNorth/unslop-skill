# Unslop report: https://consile.app

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). div.landing-hero-stage.landing-hero-bento > div.landing-bento-copy.relative:nth-of-type(2) > div.relative.flex > h1.font-display.text-\[2\.6rem\] > span.hero-title-word.hero-title-accent:nth-of-type(11)  "in"  
   Evidence: 1.14:1 against the background behind the text (10th-percentile pixel #fa842c, worst 1.01:1; text #f97015, 42px; needs 3.0:1). APCA Lc 0 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-002 Text size floors** (2x). div.flex.min-h-\[26rem\]:nth-of-type(2) > div:nth-of-type(1) > p.truncate.text-\[11\.5px\]:nth-of-type(2)  "Here's what's happening with your team today."  
   Evidence: 45-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
3. **[Floor P0] A11-004 Target size** (2x). html > body > div:nth-of-type(2) > a:nth-of-type(4)  "SaasHunt"  
   Evidence: target 64x17px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
4. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 1830 characters (27% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
5. **[Floor P0] A11-003 Visible focus everywhere** (1x). 'Featured on' marquee, focus.json stops 16-18  
   Evidence: focus.json: Tab lands on 'Visit Consile on SaaSHub', 'Visit Consile on Product Hunt' and 'G2 Peer reviews' at x = -3052 (off-screen copies of the scrolling marquee), and then on ~15 badge links all at y 1824; the marquee duplicates the list three times so keyboard users tab through the same links repeatedly, some invisible.  
   Fix: Add aria-hidden="true" and inert to the duplicated marquee copies; keep one focusable set in view (remedy: fix-a11y)
6. **[Floor P0] A11-011 Reduced motion respected** (1x). 'Featured on' logo marquee, tile 01-02  
   Evidence: The badge strip is an auto-scrolling marquee (tile 02 shows cards cut at both edges mid-scroll; text repeated three times in dom). No pause control visible.  
   Fix: Add a visible pause button and stop the animation on hover/focus and under prefers-reduced-motion: reduce (remedy: fix-motion)
7. **[Floor P0] A11-006 Controls have accessible names** (1x). 'Enterprise-grade by default' grid, tile 04  
   Evidence: Seven links read "Learn more" (SAML, SCIM, Audit Log Streaming, Privileged Access, Public API, Recurring Tasks), two read "Privacy" and one "View list"; out of context they do not say where they go.  
   Fix: <a>Learn more<span class="sr-only"> about SAML 2.0 Single Sign-On</span></a> (or aria-labelledby the card heading) (remedy: fix-a11y)
8. **[Floor P0] A11-005 Images have text alternatives** (1x). marquee favicons (dom-1440 img 'favicons')  
   Evidence: 28 favicon images have alt="" while the adjacent text names the site (fine), but badge images carry promotional alts like "Consile - Run your business. All in one place. | Product Hunt" and "SaasHunt Top 1 Daily Winner" repeated 4x (duplicated marquee copies), so a screen reader hears the same badge list three times.  
   Fix: Keep alts on the first set; aria-hidden="true" on the duplicated tracks (remedy: fix-a11y)
9. **[Floor P0] INT-003 No fake people or hotlinked stock** (1x). 'Featured on' marquee, tile 02, and badges strip  
   Evidence: Social proof is a scrolling wall of launch-directory badges (SaaSHub, Product Hunt, Startup Fame, 'SaasHunt Top 1 Daily Winner', KittyLaunch, Launchstag, LaunchBuff, Boost Domain Rating, Sell With Boost, 'Made with Lovable') plus G2/Capterra tiles labelled "Peer reviews" and "Software marketplace" with no rating or review count shown.  
   Fix: Show one verifiable proof (an actual G2 rating with count and link) or remove the strip; [DATA NEEDED: real customer or review count] (remedy: fix-harden)
10. **[Reflex P1] CPY-005 No slop diction** (15x). div.mx-auto.w-full > div.landing-hero-stage.landing-hero-bento > div.landing-bento-copy.relative:nth-of-type(2) > div.relative.flex > p.landing-hero-subtitle.mt-6:nth-of-type(1)  "Most tools only manage projects or only manage peo"  
   Evidence: "calm" (buzzwords/virtue-words, cap budget 2, found 3)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Reflex P1] SLP-003 No icon tiles above every card heading** (13x). div.grid.grid-cols-1:nth-of-type(2) > a.block.min-w-0:nth-of-type(1) > div.rounded-card.border > div.p-5.md\:p-6 > div.h-10.w-10:nth-of-type(1)  
   Evidence: 40px tinted tile above heading "SAML 2.0 Single Sign-On" (12 repeats)  
   Fix: Remove the tiles, or use a real image or figure that differs per card. (remedy: fix-quieter)
12. **[Reflex P1] A11-004 Target size** (11x). div.rounded-card.border > div.flex.items-start > div.flex-1.min-w-0:nth-of-type(2) > div.flex.items-center > button.inline-flex.items-center  "Maybe later"  
   Evidence: touch target 92x32px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
13. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
14. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (6x). div:nth-of-type(1) > div.min-h-dvh.bg-background > section.landing-hero-section.landing-hero-shell:nth-of-type(1) > div.mx-auto.w-full > div.landing-hero-stage.landing-hero-bento  
   Evidence: radial spotlight #f97015 alpha 0.20  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
15. **[Reflex P1] A11-007 Headings and landmarks** (4x). div.min-w-0.flex-1:nth-of-type(3) > div.grid.min-w-0 > section.min-w-0.overflow-hidden:nth-of-type(1) > header.mb-2.flex > h3.text-\[12px\].font-semibold  "Tasks"  
   Evidence: heading jumps from h1 to h3  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)

19 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 image(s) could not load (network blocked); imagery and layout around them not verified
- a11y: Keyboard operation of the mobile menu, FAQ accordion and video play button (no live Playwright run).
- a11y: Forms: none on the landing page.
- a11y: Text spacing (1.4.12) override not injected.
- a11y: Sweep contrast hits on the orange accent words in the h1 ('in one workspace') look real in tile 00 (orange on peach gradient); not disputed.
- slop: No 00-contract.md: no brief overrides or brand facts available; orange accent treated as brand colour, not judged as a tell.
- slop: Blocked image (kittylaunch badge-light.svg) not judged.
- slop: Hero motion orbs and marquee seen only as stills.
