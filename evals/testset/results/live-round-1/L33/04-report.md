# Unslop report: https://preview.pro.ant.design/dashboard/analysis

**Verdict (draft): fix**. Profile: balanced. 12 Floor finding(s) open.

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
| Integrity | 7 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). div > div.ant-pro-global-header-header-actions.css-tql0nm > span.ant-pro-global-header-header-actions-avatar.css-tql0nm > div.ant-dropdown-trigger > span:nth-of-type(2)  "ProUser"  
   Evidence: 3.35:1 against the background behind the text (10th-percentile pixel #fefefe, worst 3.35:1; text #000000, opacity 0.45, 14px; needs 4.5:1). APCA Lc 61 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (6x). ul "Welcome
Admin
Dashboard
Analysis
Monitor
Workplace
Form
List"  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
3. **[Floor P0] A11-006 Controls have accessible names** (6x). div.ant-tabs-extra-content:nth-of-type(3) > div.acss-6b2xdh > div.ant-picker.ant-picker-range:nth-of-type(2) > div.ant-picker-input.ant-picker-input-start:nth-of-type(1) > input  
   Evidence: input[type=text] has no accessible name  
   Fix: Add visible text or aria-label. (remedy: fix-a11y)
4. **[Floor P0] TYP-004 The intended font actually renders** (2x). li.ant-menu-item.ant-menu-item-only-child:nth-of-type(1) > span.ant-menu-title-content > a > div.ant-pro-base-menu-inline-item-title.css-tql0nm > span.ant-pro-base-menu-inline-item-text.css-tql0nm:nth-of-type(2)  "Welcome"  
   Evidence: declared "AlibabaSans" but Alibaba Sans drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
5. **[Floor P0] A11-009 Zoom never blocked** (2x). meta viewport  
   Evidence: zoom disabled: width=device-width,user-scalable=no,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0  
   Fix: Remove the restriction. (remedy: fix-a11y)
6. **[Floor P0] A11-010 Form fields have labels** (2x). div.ant-tabs-extra-content:nth-of-type(3) > div.acss-6b2xdh > div.ant-picker.ant-picker-range:nth-of-type(2) > div.ant-picker-input.ant-picker-input-start:nth-of-type(1) > input  
   Evidence: input[type=text] has no label (placeholder "Start date" is not a label)  
   Fix: Add a visible label element. (remedy: fix-a11y)
7. **[Floor P0] A11-005 Images have text alternatives** (1x). div.ant-pro-global-header-header-actions.css-tql0nm > span.ant-pro-global-header-header-actions-avatar.css-tql0nm > div.ant-dropdown-trigger > span.ant-avatar.ant-avatar-circle:nth-of-type(1) > img  
   Evidence: img without alt: bjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png  
   Fix: Write what the image tells the reader, or alt="" if it tells nothing. (remedy: fix-a11y)
8. **[Floor P0] A11-008 Language and title set** (1x). <html>  
   Evidence: no lang attribute  
   Fix: Add lang and a specific title. (remedy: fix-a11y)
9. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 537 characters (100% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
10. **[Floor P0] A11-163 Charts provide a table alternative and text summary of the key insight** (1x). all charts (17 <canvas> elements: sparklines, sales bar chart, donut, store rings, time series)  
   Evidence: dom-1440.json: every chart is a <canvas> with no role, no accessible name and no fallback content or adjacent data table (except the search table). The monthly sales bars (1月-12月), the category donut values and the store time series exist only as pixels.  
   Fix: <canvas role="img" aria-label="Monthly sales 2026, highest April about 1,180"></canvas> plus a visually hidden or toggleable <table> of the series (remedy: None)
11. **[Floor P0] A11-168 Never convey information by colour alone** (1x). store conversion tabs 'Stores 0' to 'Stores 5'  
   Evidence: Tile 01: each tab shows '转化率' (conversion rate) beside a ring chart but no number; the value is conveyed only by the arc length of a canvas ring.  
   Fix: Print the percentage next to the label (e.g. '转化率 30%') and expose it in the tab's accessible name (remedy: None)
12. **[Floor P0] INT-005 No placeholder residue at ship** (1x). store ranking list and search table, tiles 00-01  
   Evidence: Placeholder residue: ranking rows '工专路 0 号店' to '工专路 6 号店' all show the same '323,234'; search keywords are '搜索关键词-0' to '搜索关键词-4'; donut shows '其他: 1,231' and '母婴产品: 1,231'; 'Stores 0' to 'Stores 5' tabs. (Sweep counted the repeated 323,234; the indexed names and 'Stores N' are added here.)  
   Fix: For a demo, realistic distinct sample data with a visible 'Sample data' tag; in any real use, [DATA NEEDED: store names and figures] (remedy: fix-copy)
13. **[Reflex P1] A11-004 Target size** (12x). div > div > div.ant-pro-global-header-header-actions.css-tql0nm > div.ant-pro-global-header-header-actions-item.css-tql0nm:nth-of-type(1) > button.ant-btn.css-tql0nm  
   Evidence: touch target 36x36px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
14. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). :where(.css-tql0nm).ant-tooltip-unique-container-visible  
   Evidence: "transition: all var(--ant-motion-duration-slow)": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
15. **[Reflex P1] A11-007 Headings and landmarks** (2x). div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-row.css-tql0nm > div.ant-col.ant-col-xs-24:nth-of-type(2) > div.acss-16j1xqq > h4.acss-98erv7  "门店销售额排名"  
   Evidence: heading jumps from h1 to h4  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)

11 further findings are in 04-findings.json.

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
- capture: 10 other request(s) blocked, e.g. fetch https://analytics.google.com/g/collect?v=2&tid=G-59NF1VHHPF&gtm=45je6b41v9124153953z
- a11y: Live keyboard behaviour of the date-range picker, tabs and chart brush
- a11y: Language attribute: sweep already flags missing lang (content is Chinese and English mixed)
- a11y: Reflow at 375px: KPI cards and charts stack to one column; no new failure beyond the sweep zoom_blocked hit
- slop: Interaction states (date range picker, tab switches, brush) not exercised
- slop: Whether the placeholder data is intended: judged as a template demo, which is what the page is
