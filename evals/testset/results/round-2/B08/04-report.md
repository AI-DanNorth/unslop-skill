# Unslop report: /home/claude/refs/huashu-design-en/assets/showcases/website-saas/saas-pentagram.html

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (16x). html > body > div.hero:nth-of-type(1) > div.hero-left:nth-of-type(1) > div.hero-label:nth-of-type(1)  "Business Intelligence for Modern Teams"  
   Evidence: 4.17:1 against the background behind the text (10th-percentile pixel #ffffff, worst 4.17:1; text #e63946, 12px; needs 4.5:1). APCA Lc 67 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] INT-001 No invented metrics** (9x). html > body > div.hero:nth-of-type(1) > div.hero-left:nth-of-type(1)  
   Evidence: "3x FASTER" (invented-metrics/multipliers, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
3. **[Floor P0] A11-003 Visible focus everywhere** (2x). button "WATCH DEMO"  
   Evidence: no visible focus indicator (outline: auto 1px rgb(9, 9, 9))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
4. **[Floor P0] ROB-003 No horizontal overflow** (2x). html > body > nav  
   Evidence: page is 1440px wide at a 375px viewport (sideways scroll); widest culprit 1440px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
5. **[Floor P0] A11-009 Zoom never blocked** (1x). <meta name=viewport>  
   Evidence: dom-1440.json meta viewport 'width=1440'; at 375 the desktop layout is scaled and overflows (sweep ROB-003), so phone users get ~4x-smaller text.  
   Fix: <meta name="viewport" content="width=device-width, initial-scale=1"> plus a stacked layout under ~768px (remedy: fix-a11y)
6. **[Floor P0] A11-006 Controls have accessible names** (1x). range chips '7D', '30D', '90D' in the mock  
   Evidence: dom-1440.json: the chips are <div>s with no role or tabindex, yet styled as a selected toggle ('30D' red); they look operable but cannot be reached by keyboard. Nav links all have href '#'.  
   Fix: Real <button aria-pressed> controls if interactive, or mark the whole mock aria-hidden="true" and remove control styling (remedy: fix-a11y)
7. **[Floor P0] INT-003 No fake people or hotlinked stock** (1x). bottom strip 'TRUSTED BY Stripe Notion Linear Vercel Figma'  
   Evidence: Five famous brands as grey text, no logos, links or permission; borrowed proof the sweep did not flag. The mock's 'Churn risk: Acme Corp' and 'Expansion signal: Bolt' add placeholder companies.  
   Fix: Remove, or real customers with permission [DATA NEEDED: customer list] (remedy: fix-harden)
8. **[Reflex P1] SLP-012 Look-family cluster** (2x). whole page (single screen), 1440 tile 00  
   Evidence: Failed T-DEFAULT-AGENT and T-MIRROR: split hero with eyebrow 'BUSINESS INTELLIGENCE FOR MODERN TEAMS', h1 with one accent-coloured word ('decisions,'), 'AI-powered analytics...' sub-line, primary + 'Watch Demo' CTAs, stat trio, dark product mock on the right, 'TRUSTED BY' strip. The Swiss type and red accent are a skin; removing them leaves the generic BI landing hero.  
   Fix: Keep the type and colour system, replace the content skeleton with something only this product can show [DATA NEEDED: a real product view or customer result] (remedy: fix-quieter)
9. **[Reflex P1] A11-002 Text size floors** (6x). html > body > div.hero:nth-of-type(1) > div.hero-left:nth-of-type(1) > div.hero-label:nth-of-type(1)  "Business Intelligence for Modern Teams"  
   Evidence: 38-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
10. **[Reflex P1] INT-002 No default cast or fake brands** (2x). div.hero-right:nth-of-type(2) > div.dash-bottom:nth-of-type(4) > div.data-table:nth-of-type(2) > div.data-row:nth-of-type(3) > span.data-row-label:nth-of-type(1)  "Churn risk: Acme Corp"  
   Evidence: "Acme" (default-names/fake-brands, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
11. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
12. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 13 distinct font sizes: 9, 10, 11, 12, 13, 14, 15, 17, 22, 28, 32, 52, 140 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
13. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). html > body > div.hero:nth-of-type(1) > div.hero-left:nth-of-type(1) > h1.hero-headline  "Turn data into not dashboards"  
   Evidence: display text at 52px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
14. **[Reflex P1] INT-007 Stat bands need sources** (1x). div.hero:nth-of-type(1) > div.hero-right:nth-of-type(2) > div.kpi-row:nth-of-type(2) > div.kpi-card:nth-of-type(1) > div.kpi-value:nth-of-type(2)  "$2.4M"  
   Evidence: stat band of 3 unsourced figures: $2.4M, 84.2K, 1.2%  
   Fix: Cite each figure, use only supplied facts, or remove the band. (remedy: fix-copy)
15. **[Reflex P1] A11-004 Target size** (1x). html > body > nav > a.nav-signin  "Sign In"  
   Evidence: touch target 103x36px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)

3 further findings are in 04-findings.json.

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
- a11y: Sweep's 1.00:1 contrast hit on the red '3x' is a measurement artefact (sampling the glyph itself); the numeral is visibly red on white, about 4.2:1, which passes the 3:1 large-text bar. disputed: sampled the text's own fill.
- a11y: No live keyboard test of 'WATCH DEMO'.
- slop: Lucide icons and fonts were shimmed (manifest); rendering treated as intended.
- slop: Copy voice: no brand samples supplied.
