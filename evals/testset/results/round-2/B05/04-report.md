# Unslop report: /home/claude/refs/design-taste/examples/dark-tech.html

**Verdict (draft): fix**. Profile: balanced. 8 Floor finding(s) open.

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
| Integrity | 2 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-102 Never invent testimonials, quotes, reviews, ratings, review counts, awards or press lines** (1x). testimonial section, 1440-01  
   Evidence: "We found the exact step where users churned in a fifteen-minute session. Skittie paid for itself in one afternoon." — Sarah Chen, founder of Stitchboard. Sarah Chen is the canonical default-cast testimonial name; the sweep's default_names did not fire.  
   Fix: [DATA NEEDED: a real customer quote with permission, name and company] or remove the section (remedy: None)
2. **[Floor P0] A11-001 Text contrast on real pixels** (15x). html > body > header > div.container > p.kicker.mono:nth-of-type(1)  "// Product analytics for indie founders"  
   Evidence: 4.24:1 against the background behind the text (10th-percentile pixel #08090a, worst 4.24:1; text #5e6ad2, 12px; needs 4.5:1). APCA Lc 29 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] INT-001 No invented metrics** (1x). html > body > div.logos > div.container.logos-inner > span.mono  "Trusted by 4,000+ indie teams"  
   Evidence: "Trusted by 4,000+" (invented-metrics/social-proof-counts, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
4. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > div.logos > div.container.logos-inner > div.logos-row  
   Evidence: page is 531px wide at a 375px viewport (sideways scroll); widest culprit 384px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
5. **[Floor P0] A11-009 Zoom never blocked** (1x). 375 width: nav, metrics panel, feature grid (tiles 375-00, 375-01)  
   Evidence: At 375 the logo and first link collide ("skittie.devFeatures"), "Deploy now" wraps to two lines and sits past the 375 edge, the metrics panel and the three feature cards stay three columns so "churn_90d" and "cohorts.smart" run off-screen, and the page is 531px wide. The sweep reported only the logos row as the overflow culprit.  
   Fix: @media (max-width: 640px) { .feature-grid, .metric-grid, .price-grid { grid-template-columns: 1fr } .nav-links { gap: 12px } .nav-links a { display: none } } (or a menu button) (remedy: fix-a11y)
6. **[Floor P0] A11-115 Expose correct state attributes: aria-expanded on menu/accordion triggers, aria-pressed/ar** (1x). all six CTAs: Deploy now, Start free trial, Book a demo, Get started, Start 14-day trial, Contact sales, Start your free trial →  
   Evidence: dom-1440: each is a <button type="submit"> with no href and no enclosing form (forms.json is empty), so activating any of them does nothing and they are announced as buttons although they read as navigation.  
   Fix: <a class="nav-cta" href="/signup">Start free trial</a> (and equivalents for demo, pricing tiers and contact) (remedy: None)
7. **[Floor P0] A11-165 Large text, icons, focus rings, field edges, control boundaries, data marks.** (1x). ghost buttons "Book a demo", "Get started", "Contact sales"  
   Evidence: Boundary is border 1px rgba(255,255,255,0.16) on a transparent fill over #08090a, about 1.5:1 against the page; it is the only cue separating these buttons from body text.  
   Fix: border: 1px solid rgba(255,255,255,0.45) (about 3.4:1 on #08090a) (remedy: None)
8. **[Floor P0] INT-103 Never invent logo walls or customer names** (1x). logo strip under hero, 1440-00  
   Evidence: "Trusted by 4,000+ indie teams" next to text-and-glyph pseudo-logos "acme", "fathom", "baseline", "radar", "promptly" (acme is the placeholder company). Sweep caught the 4,000+ count; the invented logo wall itself was not flagged.  
   Fix: [DATA NEEDED: real customer names with permission] or delete the strip (remedy: None)
9. **[Reflex P1] IMG-105 Never use CSS silhouettes, styled-div "product UI" or bevelled fakes as stand-ins for real** (1x). hero metrics panel, 1440-00  
   Evidence: A styled-div dashboard titled "skittie:live — metrics" with a green "● live" dot showing trial_to_paid 18.4%, time_to_value 9m, churn_90d 2.1%, "median, n=4,120": a fake live product UI with fake data standing in for a screenshot.  
   Fix: A real screenshot or recording of a Skittie funnel, or [DATA NEEDED: product capture] (remedy: None)
10. **[Reflex P1] A11-004 Target size** (9x). body > nav > div.container.nav-inner > div.nav-links:nth-of-type(2) > a:nth-of-type(1)  "Features"  
   Evidence: touch target 57x17px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
11. **[Reflex P1] A11-002 Text size floors** (6x). html > body > header > div.container > p.kicker.mono:nth-of-type(1)  "// Product analytics for indie founders"  
   Evidence: 39-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
12. **[Reflex P1] SLP-010 No template chrome glyphs** (5x). section.section:nth-of-type(3) > div.container > div.price-grid:nth-of-type(2) > div.price-card.featured:nth-of-type(2) > p.price-name:nth-of-type(1)  "PRO — MOST POPULAR"  
   Evidence: template chrome (dash-labels): "PRO — MOST POPULAR"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
13. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (3x). body > nav > div.container.nav-inner > div.nav-links:nth-of-type(2) > button.nav-cta  "Deploy now"  
   Evidence: zero-offset coloured boxShadow #5e6ad2 blur 24px alpha 0.20  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
14. **[Reflex P1] SLP-009 No neon violet or cyan on headings** (3x). div.panel.metrics-panel:nth-of-type(2) > div.metric-grid:nth-of-type(2) > div.metric-cell:nth-of-type(1) > p.metric-value:nth-of-type(2) > span.accent  "%"  
   Evidence: violet text #5e6ad2 (oklch hue 275, chroma 0.16) at 26px  
   Fix: Derive the accent from brand, imagery or culture (Sample, Converge, Justify). (remedy: fix-colorize)
15. **[Reflex P1] CPY-005 No slop diction** (3x). section.section:nth-of-type(1) > div.container > div.section-head:nth-of-type(1) > h2  "Everything you need to grow"  
   Evidence: "Everything you need to" (stock-phrases/openers, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)

13 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Sweep contrast hits on #5c6370 12px mono labels (3.17:1, 3.30:1) checked against 1440-00 and 1440-01: real, not disputed.
- a11y: No forms present, so error handling not applicable.
- a11y: No animation in stylesheets; motion not applicable.
- a11y: Keyboard operation not run live; no menus, dialogs or carousels present.
- slop: No 00-contract.md: no brief override recorded for the dark-single-accent look, so it is treated as unchosen.
- slop: Buttons render in Liberation Sans fallback (form controls not inheriting Space Grotesk); already in sweep type_ladder, not repeated.
