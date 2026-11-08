# Unslop report: /home/claude/refs/ui-ux-pro-max/projects/saas-landing/index.html

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
| Integrity | 1 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). html > body.bg-background.font-body > nav.fixed.top-4 > div.max-w-7xl.mx-auto > a.bg-cta.hover\:bg-orange-600:nth-of-type(2)  "Get Started"  
   Evidence: 2.80:1 against the background behind the text (10th-percentile pixel #f97316, worst 2.80:1; text #ffffff, 16px; needs 4.5:1). APCA Lc 58 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] INT-001 No invented metrics** (6x). html > body.bg-background.font-body > section.pt-32.pb-20:nth-of-type(1) > div.max-w-7xl.mx-auto > p.text-lg.md\:text-xl  "Join 10,000+ teams who trust SaaSify to automate t"  
   Evidence: "10,000+ teams" (invented-metrics/social-proof-counts, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
3. **[Floor P0] A11-005 Images have text alternatives** (2x). logo strip svgs, tile 1440-00  
   Evidence: dom-1440.json: five svg.h-8 wordmarks (Stripe, Notion, Linear, Vercel, Figma) have no accessible name, role or title; a screen reader gets 'Trusted by industry leaders' followed by nothing.  
   Fix: <svg role="img" aria-label="Stripe">…</svg> for each (if the strip stays). (remedy: fix-a11y)
4. **[Floor P0] A11-006 Controls have accessible names** (2x). hero 'Watch Demo'  
   Evidence: href '#demo' but no element with id 'demo' exists in the DOM; activating it does nothing. 'Get Started' and 'Start Free Trial' both go to '#cta', which only repeats the same buttons.  
   Fix: Link to a real video (with captions) or a demo page; give the trial buttons a real signup href. (remedy: fix-a11y)
5. **[Floor P0] A11-007 Headings and landmarks** (1x). page  
   Evidence: nav and footer but no main (sweep) and no skip link; the fixed floating nav (nav.fixed.top-4) is 77px tall and could cover focused section headings when jumping via #features/#pricing (no scroll-margin-top observed).  
   Fix: Skip link + <main id="main">; section[id] { scroll-margin-top: 6rem }. (remedy: fix-a11y)
6. **[Floor P0] INT-103 Never invent logo walls or customer names** (1x). logo strip, tile 1440-00  
   Evidence: 'TRUSTED BY INDUSTRY LEADERS' over Stripe, Notion, Linear, Vercel and Figma wordmarks. These are real companies placed as customers of a placeholder product with no source; the sweep caught '10,000+ teams' but not the logo wall.  
   Fix: Remove the strip until there are customers who have agreed to be named. [DATA NEEDED: permitted customer logos] (remedy: None)
7. **[Floor P0] INT-102 Never invent testimonials, quotes, reviews, ratings, review counts, awards or press lines** (1x). testimonials, tiles 1440-01/02  
   Evidence: Three five-star cards from 'Sarah Mitchell, VP Operations, TechCorp', 'James Chen, CTO, ScaleUp Inc', 'Amanda Rodriguez, Founder, GrowthLab': stock names, placeholder companies, initials avatars, and quotes built to formula ('reduced our manual work by 80%', 'ROI was visible within the first month', 'Best investment we've made').  
   Fix: [DATA NEEDED: real, attributable quotes], or remove the section. (remedy: None)
8. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). whole page, tiles 1440-00 to 03 and dom-1440.json text  
   Evidence: Failed T-STOCK-ORDER (9 stock sections): centred hero > stat band (10K+, 99.9%, 50M+, 4.9) > 'TRUSTED BY INDUSTRY LEADERS' logo strip > 'Everything You Need to Scale' three equal icon cards > 'Loved by Teams Worldwide' three testimonial cards > 'Simple, Transparent Pricing' three tiers with 'Most Popular' > 'Ready to Transform Your Workflow?' CTA band > four-column link-farm footer. Failed T-DEFAULT-AGENT: 'landing page for a workflow automation SaaS' produces this verbatim.  
   Fix: [DATA NEEDED: what the product automates, for whom, and a real screenshot]; build the first screen around one workflow shown end to end. (remedy: None)
9. **[Reflex P1] CON-118 Give every page one signature: the brief's strongest real thing at its best, on the first ** (1x). first screen  
   Evidence: Failed T-FIVE-SECOND: the hero says 'automate tasks, boost productivity, and scale their operations' but never which tasks or for which team; there is no product image anywhere on the page. A visitor cannot tell what SaaSify does.  
   Fix: A head naming the job, e.g. '[Product] turns [specific trigger] into [specific outcome] for [team]'. [DATA NEEDED: the actual job] (remedy: None)
10. **[Reflex P1] CPY-005 No slop diction** (20x). html > body.bg-background.font-body > section.pt-32.pb-20:nth-of-type(1) > div.max-w-7xl.mx-auto > h1.font-heading.text-4xl  "Streamline Your Workflow"  
   Evidence: "Streamline" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (5x). :root --color-gray-100  
   Evidence: token --color-gray-100: oklch(96.7% 0.003 264.542) is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)
12. **[Reflex P1] SLP-003 No icon tiles above every card heading** (4x). section.py-24.px-4:nth-of-type(3) > div.max-w-7xl.mx-auto > div.grid.md\:grid-cols-3:nth-of-type(2) > div.bg-white.p-8:nth-of-type(1) > div.w-12.h-12  
   Evidence: 48px tinted tile above heading "Instant Automation" (3 repeats)  
   Fix: Remove the tiles, or use a real image or figure that differs per card. (remedy: fix-quieter)
13. **[Reflex P1] A11-004 Target size** (4x). html > body.bg-background.font-body > nav.fixed.top-4 > div.max-w-7xl.mx-auto > a.font-heading.font-bold:nth-of-type(1)  "SaaSify"  
   Evidence: touch target 93x32px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
14. **[Reflex P1] A11-007 Headings and landmarks** (2x). footer.bg-text.py-16 > div.max-w-7xl.mx-auto > div.grid.md\:grid-cols-4:nth-of-type(1) > div:nth-of-type(2) > h4.font-semibold.text-white  "Product"  
   Evidence: heading jumps from h2 to h4  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
15. **[Reflex P1] MOT-001 Motion CSS hygiene** (2x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)

7 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: all 1.00-1.01:1 contrast hits (nav 'Get Started', hero 'Start Free Trial', Pro tier text, CTA band) are a capture artefact: the Tailwind v3 config defining bg-cta/bg-primary/bg-text was ignored by the v4 shim, so dark fills never rendered. Re-capture with the real Tailwind runtime before reporting contrast
- a11y: reflow, non-text contrast and focus-ring visibility not judged for the same reason
- a11y: live keyboard tests not run
- slop: Render fidelity: Tailwind v3 config was ignored by the v4 shim, so the Pro tier, CTA band, primary buttons and footer render white on white; colours, fonts (Poppins/Open Sans intended) and the CTA band layout were judged from dom-1440.json text, not the screenshots
- slop: slop words, '10,000+ teams', '99.9% Uptime' and the stat band: reported by the sweep, not repeated
