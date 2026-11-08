# Unslop report: /home/claude/refs/ux-ui-agent-skills/examples/showcase/index.html

**Verdict (draft): fix**. Profile: balanced. 4 Floor finding(s) open.

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

1. **[Floor P0] A11-003 Visible focus everywhere** (2x). button "30 days"  
   Evidence: no visible focus indicator (outline: none 3px rgb(36, 39, 41))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] A11-005 Images have text alternatives** (1x). svg.chart x5 (NRR bars, plan donut, 3 region sparklines)  
   Evidence: dom-1440.json records no name, role or title on any svg.chart; the weekly bar values and region trends exist only as drawing, with no table or text equivalent (the sparklines' percentages are given, the bars' values are not).  
   Fix: role="img" aria-label="Net recurring revenue by week, weeks 21-27: ..." on each chart, or a visually hidden <table> of the weekly values (remedy: fix-a11y)
3. **[Floor P0] A11-001 Text contrast on real pixels** (1x). bar chart (hero), plan donut, region sparklines  
   Evidence: T-GRAYSCALE: the partial week is distinguished only by orange vs blue; donut segments by hue only (legend dots); region lines by hue only (blue, orange, violet). Status badges do carry text ('Healthy', 'At risk', 'Churning'), which passes.  
   Fix: Add a pattern or outline to the partial bar plus a direct label 'Wk 27 (partial)'; label donut segments in place (remedy: fix-a11y)
4. **[Floor P0] INT-001 No invented metrics** (1x). hero card 'NET RECURRING REVENUE', bar chart  
   Evidence: Caption says 'Week 27 is the current, partial week.' yet the orange week-27 bar is the tallest of seven; a partial week out-earning every full week is implausible and the chart has no y-axis values to check it. Failed T-THREE-LINE (not falsifiable from the chart).  
   Fix: Show week-27 as a hatched or outlined partial bar at its real (lower) value with axis ticks; [DATA NEEDED: weekly NRR values] (remedy: fix-copy)
5. **[Reflex P1] DVZ-106 Never ship decorative dashboards: donut walls, gauge rows, KPI confetti** (1x). whole page, 1440 tiles 00-01  
   Evidence: Order is sidebar nav + search/avatar bar > hero KPI with bar chart > KPI stack (NRR, churn, pipeline) > donut 'Revenue by plan' > ranked bars 'Largest accounts' > sparklines 'Expansion by region' > sortable table > activity feed. Failed T-DEFAULT-AGENT and T-MIRROR: every block is the stock admin-dashboard kit and would be generated for any B2B revenue console.  
   Fix: Pick the one question this console answers first (e.g. which renewals are at risk this month) and let that block lead; demote or drop panels that do not serve it (remedy: None)
6. **[Reflex P1] A11-004 Target size** (12x). body > div.shell > aside.side > nav.nav > a:nth-of-type(1)  "Overview"  
   Evidence: touch target 118x40px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] INT-002 No default cast or fake brands** (9x). div.card:nth-of-type(2) > ol.rank > li:nth-of-type(1) > span.row:nth-of-type(1) > span.name:nth-of-type(1)  "Northwind Logistics"  
   Evidence: "Northwind" (default-names/fake-brands, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
8. **[Reflex P1] SLP-006 Vary container recipes** (2x). table > thead > tr > th:nth-of-type(1)  
   Evidence: one box recipe on 35 elements across 3 selectors (td, td.num, th)  
   Fix: Differentiate by role: section, object, callout, well. (remedy: fix-layout)
9. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). main > div.page:nth-of-type(2) > div.head > div:nth-of-type(1) > h1  "Revenue overview"  
   Evidence: display text at 30px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
10. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). table > tbody  
   Evidence: "Healthy" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
11. **[Reflex P1] A11-007 Headings and landmarks** (1x). focus stop 9: section.hero card 'NET RECURRING REVENUE'  
   Evidence: focus.json stop 9 is a <section> with tabindex showing only a 1px auto outline (focus/09-on.png): a non-interactive card is a tab stop with no name or purpose announced.  
   Fix: Remove tabindex, or give it role="region" aria-label="Net recurring revenue" and the same 2px teal ring as other controls (remedy: fix-a11y)
12. **[Reflex P1] A11-006 Controls have accessible names** (1x). footer link 'ux-ui-agent-skills'  
   Evidence: focus.json stop 15 records an empty text for this link and 1px default outline; nav links use a 2px teal ring, footer links fall back to the browser default.  
   Fix: Apply the shared :focus-visible ring to footer links (remedy: fix-a11y)
13. **[Reflex P1] DVZ-113 Part-to-whole: stacked horizontal bar preferred** (1x). card 'REVENUE BY PLAN'  
   Evidence: A 4-segment donut (Enterprise 46%, Growth 31%, Team 15%, Starter 8%) with a separate legend list repeating the numbers; T-DELETION: removing the donut loses nothing the list does not already say.  
   Fix: One stacked horizontal bar labelled in place, or just the four-row list (remedy: None)
14. **[Reflex P2] CLR-001 Accent footprint within budget** (2x). first screen at 1280px  
   Evidence: saturated accent covers 6.2% of the fold (warn > 5%)  
   Fix: Keep accent on the primary action, current state and one focal element. (remedy: fix-colorize)
15. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (3x). section.hero:nth-of-type(1) > div.stack:nth-of-type(2) > div.card:nth-of-type(1) > p.muted:nth-of-type(3)  "expansion outpaced churn in 5 of 6 segments."  
   Evidence: last line is 24% of the measure at 375px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)

2 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: aria-selected / aria-sort state on tabs and sortable headers: not in the dom capture.
- a11y: Reflow at 320px and the horizontally scrolling nav at 375 (tile shows 'Accounts' cut at the edge): not checked live.
- slop: Sort behaviour of table headers and tab switching (no live interaction).
- slop: Footer credit line 'Built with ux-ui-agent-skills ... Every pixel here is token-driven and gate-verified' treated as a showcase credit, not product copy.
