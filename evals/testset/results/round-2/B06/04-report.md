# Unslop report: /home/claude/refs/design-taste/examples/corporate-trust.html

**Verdict (draft): fix**. Profile: balanced. 11 Floor finding(s) open.

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

1. **[Floor P0] INT-102 Never invent testimonials, quotes, reviews, ratings, review counts, awards or press lines** (1x). testimonial card, 1440-01  
   Evidence: "We found the exact step where users churned in a fifteen-minute session. Skittie paid for itself in one afternoon." — Sarah Chen, Founder, Stitchboard · 12-person team, 40k monthly users. Default-cast name plus manufactured specifics (team size, MAU) for credibility.  
   Fix: [DATA NEEDED: real, permissioned customer quote and attribution] or remove (remedy: None)
2. **[Floor P0] A11-001 Text contrast on real pixels** (5x). body > div.logos > div.container.logos-inner > div.logos-row > span:nth-of-type(1)  "Acme"  
   Evidence: 3.60:1 against the background behind the text (10th-percentile pixel #f8fafc, worst 3.60:1; text #5b6777, opacity 0.80, 15px; needs 4.5:1). APCA Lc 62 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] INT-001 No invented metrics** (2x). html > body > div.logos > div.container.logos-inner > span.logos-label  "Trusted by 4,000+ independent teams, including"  
   Evidence: "Trusted by 4,000+" (invented-metrics/social-proof-counts, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
4. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > div.logos > div.container.logos-inner > div.logos-row  
   Evidence: page is 583px wide at a 375px viewport (sideways scroll); widest culprit 390px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
5. **[Floor P0] A11-009 Zoom never blocked** (1x). pricing grid at 375 (tiles/375-03.png)  
   Evidence: At 375 the four-column pricing grid does not reflow: the SCALE column is cut off ("$9" and "/ mor" visible at the edge), "Start 14-day trial" wraps to four lines, and row cells no longer line up under their headers (Usage row columns are offset from the header columns). The sweep's overflow hit named only the logos row.  
   Fix: @media (max-width: 640px) render one stacked block per plan (plan name, price, usage, includes, button) instead of the grid (remedy: fix-a11y)
6. **[Floor P0] A11-103 Use landmarks and semantic elements** (1x). pricing grid  
   Evidence: dom-1440: the plan comparison is built from div.price-row and div cells with no table, th, row or column semantics; the PLAN / STARTER / PRO / SCALE header is visual only, so a screen reader reads a flat run ("Usage 1 project · 10k events/mo 10 projects · 500k events/mo ...").  
   Fix: <table><caption>Plan comparison</caption><thead><tr><th scope="col">…</th></tr></thead><tbody><tr><th scope="row">Usage</th><td>…</td></tr> (remedy: None)
7. **[Floor P0] A11-112 Every control has an accessible name** (1x). nav and footer links, final CTA  
   Evidence: dom-1440: "Customers", "Resources", "Sign in", "Start free trial" (nav and final CTA), "Talk to sales" and every footer link (Changelog, Status, Documentation, API reference, Blog, Contact, Privacy policy, Terms of service, Data processing, Security) have href="#"; the three pricing buttons are <button> with no form (forms.json empty). Activation goes nowhere.  
   Fix: Real destinations (<a href="/privacy">), and pricing actions as links: <a class="price-btn" href="/signup?plan=starter">Get started</a> (remedy: None)
8. **[Floor P0] A11-165 Large text, icons, focus rings, field edges, control boundaries, data marks.** (1x). secondary buttons "Talk to sales", "Get started", "Contact sales"; compliance pills  
   Evidence: Border rgb(199,208,220) 1px on white is about 1.5:1; for these outline buttons it is the only boundary.  
   Fix: border: 1px solid #7b8798 (about 3.6:1 on white) (remedy: None)
9. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). all links and buttons (focus.json)  
   Evidence: Every stop reports the browser default outline (auto 1px) with no custom :focus-visible style; sweep measured "Start 14-day trial" at 2.95:1 change, just under 3:1, because a 1px default ring on the #1f4fe0 button is barely distinct.  
   Fix: a:focus-visible, button:focus-visible { outline: 2px solid #0f1722; outline-offset: 2px } (remedy: None)
10. **[Floor P0] INT-106 Ban unsourced stat strips: 3+ figures each over a one-word label, or round, neat, unsource** (1x). hero benchmark panel, 1440-00  
   Evidence: "Customer benchmarks — 2025 cohort, n = 4,120 teams": 18.4% trial-to-paid, 9 min to first insight, 2.1% 90-day churn, with pseudo-methodology captions ("Skittie data, p75 window"; a median labelled with a p75 window). Sweep caught the 4,000+ logo-strip count; this panel adds sample-size and percentile dressing to unsourced numbers.  
   Fix: [DATA NEEDED: real cohort figures, method and date] or replace with a product capture (remedy: None)
11. **[Floor P0] INT-105 Ban invented specifics dressed as authenticity ("6:12 a.m., from the window of Room 9", "B** (1x). compliance strip and footer  
   Evidence: Pills "SOC 2 Type II", "GDPR", "ISO 27001", "EU data residency available"; footer "Founded 2021, headquartered in Berlin", "Skittie Analytics GmbH", "Uptime 99.9% SLA". None is supplied by a brief; certifications are claims with legal weight.  
   Fix: [DATA NEEDED: certifications actually held, with report dates; company facts] or omit (remedy: None)
12. **[Reflex P1] A11-004 Target size** (12x). body > nav > div.container.nav-inner > div.nav-center:nth-of-type(2) > a:nth-of-type(1)  "Features"  
   Evidence: touch target 58x17px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
13. **[Reflex P1] A11-002 Text size floors** (7x). html > body > header > div.container > p.eyebrow:nth-of-type(1)  "Product analytics for independent development team"  
   Evidence: 51-character run at 13px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
14. **[Reflex P1] CPY-005 No slop diction** (3x). section.section:nth-of-type(1) > div.container > div.section-head:nth-of-type(1) > h2  "Everything you need to understand usage"  
   Evidence: "Everything you need to" (stock-phrases/openers, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
15. **[Reflex P1] SLP-010 No template chrome glyphs** (2x). section.section:nth-of-type(3) > div.container > div.price-table:nth-of-type(2) > div.price-row:nth-of-type(3)  
   Evidence: template chrome (middot-chains): "Usage 1 project · 10k events/mo 10 projects · 500k events/mo"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)

16 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Sweep contrast hits on logo-strip names (3.60:1, #5b6777 at opacity 0.8) checked on 1440-00: real, not disputed.
- a11y: No forms present; no animation in stylesheets.
- a11y: Keyboard operation not run live; no menus, dialogs or carousels present.
- slop: No 00-contract.md: no brief override for the corporate-trust look or for the compliance claims, so they are treated as unchosen and unsupplied.
