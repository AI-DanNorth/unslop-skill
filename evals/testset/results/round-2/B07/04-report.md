# Unslop report: /home/claude/refs/huashu-design-en/assets/showcases/website-saas/saas-build.html

**Verdict (draft): fix**. Profile: balanced. 10 Floor finding(s) open.

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). body > nav > ul.nav-links > li:nth-of-type(1) > a  "Product"  
   Evidence: 4.28:1 against the background behind the text (10th-percentile pixel #fafaf8, worst 4.28:1; text #777777, 14px; needs 4.5:1). APCA Lc 68 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] INT-001 No invented metrics** (6x). html > body > div.hero > div.hero-text:nth-of-type(1)  
   Evidence: "3x Faster" (invented-metrics/multipliers, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
3. **[Floor P0] A11-002 Text size floors** (3x). body > div.hero > div.hero-text:nth-of-type(1) > div.hero-badge:nth-of-type(1) > span  "Business Intelligence for Modern Teams"  
   Evidence: 38-character run at 10px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
4. **[Floor P0] ROB-003 No horizontal overflow** (2x). html > body > nav  
   Evidence: page is 1440px wide at a 375px viewport (sideways scroll); widest culprit 1440px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
5. **[Floor P0] A11-009 Zoom never blocked** (1x). <meta name=viewport>  
   Evidence: dom-1440.json meta viewport is 'width=1440'; tile 375-00 renders the full desktop layout scaled down, so text is ~4x smaller on a phone and the sweep's ROB-003 overflow follows from it.  
   Fix: <meta name="viewport" content="width=device-width, initial-scale=1"> plus a single-column layout below ~768px (remedy: fix-a11y)
6. **[Floor P0] A11-003 Visible focus everywhere** (1x). 'Start Free Trial' and 'Get Started' (dark buttons)  
   Evidence: focus/06-on.png: the focused 'Start Free Trial' shows no visible ring; focus.json records the UA default 'auto 1px rgb(115,115,115)' with no offset, which disappears against the #1a1a1a fill. Sweep's focus_ring did not flag it.  
   Fix: .btn:focus-visible { outline: 2px solid #1a1a1a; outline-offset: 3px } (remedy: fix-a11y)
7. **[Floor P0] A11-006 Controls have accessible names** (1x). nav links 'Product', 'Pricing', 'Docs', 'Blog', 'Sign In'; buttons 'Watch Demo', 'Get Started'  
   Evidence: focus.json: every nav link has href '#'; 'Watch Demo' is a <button> with no dialog or target. Links that go nowhere fail their stated purpose.  
   Fix: Real hrefs (/pricing, /docs ...) or remove the items until the pages exist (remedy: fix-a11y)
8. **[Floor P0] A11-005 Images have text alternatives** (1x). svg chart in 'Performance Overview' (648px wide)  
   Evidence: The area chart svg has no name or role; it carries the only trend data in the mock.  
   Fix: aria-hidden="true" if decorative, else role="img" aria-label describing the trend (remedy: fix-a11y)
9. **[Floor P0] INT-003 No fake people or hotlinked stock** (1x). trust bar, bottom of fold: 'Trusted by teams at Stripe Notion Linear Vercel Figma'  
   Evidence: Five famous brand names set as grey text with no logos, links or case studies; the sweep's invented_metrics caught the stats but not this borrowed proof. These are the stock 'logo strip' cast for dev-tool landing pages.  
   Fix: Remove, or list real customers with permission [DATA NEEDED: actual customer names] (remedy: fix-harden)
10. **[Floor P0] DVZ-107 Never use decorative icon+number+word metric cards with unbacked data** (1x). right-hand 'Performance Overview' card  
   Evidence: Dashboard mock with '$2.4M REVENUE', '84.2K USERS', '1.2% CHURN', '$142 ARPU', an unlabelled smooth area line, and cards 'AI Insight: Revenue Acceleration ... grew 23%' and 'Predicted: Q3 Target On Track ... 89% probability'. No axes, no dates, no source; T-DELETION: removing it loses only decoration because none of the data is real.  
   Fix: A real screenshot of the product on demo data labelled as such, or an annotated single view of one insight [DATA NEEDED: product screenshot] (remedy: None)
11. **[Reflex P1] SLP-012 Look-family cluster** (2x). hero, 1440 tile 00 (the whole page)  
   Evidence: Failed T-DEFAULT-AGENT: 'landing page for an AI analytics tool' yields exactly this: eyebrow 'BUSINESS INTELLIGENCE FOR MODERN TEAMS', h1 'Turn data into decisions, not dashboards.' with italic 'decisions' and a terracotta period, sub-line, 'Start Free Trial' + 'Watch Demo', stat trio, product mock right, logo strip. Cream #fafaf8 page, terracotta accent and an italic display word put it in the warm-paper-serif family's tells (cream_bg, terracotta_accent, eyebrows) applied to a sans.  
   Fix: Lead with one real thing the product does on real data [DATA NEEDED: an actual product screenshot or a named customer's outcome]; drop the eyebrow and the accent-period flourish (remedy: fix-quieter)
12. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). page as a whole  
   Evidence: T-FIVE-SECOND: what it is (BI tool) is answered; for whom ('modern teams') and why this one are not. The page ends after the fold with a 189px empty band and no product, pricing or proof sections, so nav items 'Product', 'Pricing', 'Docs', 'Blog' all point to '#'.  
   Fix: [DATA NEEDED: audience, product sections] then sections a buyer in this category expects (how it works on their data, pricing) (remedy: None)
13. **[Reflex P1] A11-002 Text size floors** (7x). div.hero-dashboard:nth-of-type(2) > div.dashboard-card > div.dash-bottom-row:nth-of-type(4) > div.insight-card:nth-of-type(1) > div.insight-title:nth-of-type(2)  "AI Insight: Revenue Acceleration"  
   Evidence: 32-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
14. **[Reflex P1] LAY-004 No dead bands** (2x). y 673-862 at 1280px  
   Evidence: 189px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
15. **[Reflex P1] A11-004 Target size** (2x). html > body > nav > div.nav-right:nth-of-type(2) > a.nav-signin  "Sign In"  
   Evidence: touch target 45x17px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)

6 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Sweep contrast hits on #777/#888/#aaa/#bbb greys verified visually in tile 1440-00 (stat labels, sub-line and mock labels are visibly faint): agreed, not repeated.
- a11y: Keyboard behaviour of 'Watch Demo' (no live test).
- slop: Copy voice: no brand samples supplied.
- slop: Lucide icons were shimmed (manifest: 'npm lucide@latest'); icon rendering treated as intended.
