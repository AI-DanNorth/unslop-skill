# Unslop report: /home/claude/refs/kami/site/assets/demos/demo-tesla.html

**Verdict (draft): fix**. Profile: balanced. 2 Floor finding(s) open.

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
| Accessibility | 6 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (1x). 图 1 candlestick chart, tiles 794-00/01  
   Evidence: Up and down days are told apart only by fill colour: navy #1b365d (上涨) vs grey (下跌), both solid bodies. Their contrast with each other is about 2:1 and in a black-and-white print they are close to the same dark grey. The legend is two colour swatches.  
   Fix: Use the print convention: hollow body (stroke only) for up days, filled for down days, or add a pattern; keep the colour as a second cue. (remedy: fix-a11y)
2. **[Floor P0] A11-005 Images have text alternatives** (1x). figure > svg  
   Evidence: dom-794.json: the svg has no role, title or aria-label; the figcaption carries the meaning but is not tied to the graphic, so assistive tech reads axis tick labels ('420 400 380… 3/26 4/1…') as loose text in the HTML/PDF tag tree.  
   Fix: <svg role="img" aria-labelledby="fig1-cap">…</svg><figcaption id="fig1-cap">…</figcaption>; mark tick labels aria-hidden. (remedy: fix-a11y)
3. **[Reflex P1] SLP-010 No template chrome glyphs** (3x). html > body > div.report-header:nth-of-type(1) > div.ticker-block:nth-of-type(1) > div.ticker-sub:nth-of-type(3)  "汽车与能源 · NASDAQ · 利润率在恢复，但资本开支的账单到了"  
   Evidence: template chrome (middot-chains): "汽车与能源 · NASDAQ · 利润率在恢复，但资本开支的账单到了"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
4. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 12 distinct font sizes: 11, 11.5, 12, 12.5, 13.5, 14.5, 16, 18.5, 20, 21.5, 32, 37.5 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
5. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). html > body > table.financial.compact:nth-of-type(1)  
   Evidence: "--" repeated 6 times in one container  
   Fix: Say it once. (remedy: fix-copy)
6. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (6x). html > body > h2.with-rating:nth-of-type(1)  "投资逻辑"  
   Evidence: last line is 4% of the measure at 794px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
7. **[Finish P3] INT-108 Match the source's precision** (2x). 财务概览 table, tile 794-01  
   Evidence: Failed T-THREE-LINE (falsifiable) for one column: FY2024 and Q1 2026 are given exactly ($97.7B, $477M, $0.13) but FY2025 is all approximations ('~$3.0B', '~$0.86', '~17%', '~4%'), and FY2024/FY2025 free cash flow and capex are '--' although those are reported figures. The '--' and '~' are honest, but the table mixes reported and estimated values without saying which is which.  
   Fix: Fill reported FY figures from the 10-K, or footnote the column: 'FY2025 为估算' and '-- = 未披露'. [DATA NEEDED: FY2024/FY2025 FCF and capex] (remedy: None)
8. **[Finish P3] A11-007 Headings and landmarks** (1x). 风险与总结 2x2 grid and verdict rows  
   Evidence: Risk titles (资本开支, 交付疲软, HW3 淘汰, 竞争与关税) and verdict labels (多头核心…新建仓) are styled divs, not headings or a definition list, so the tagged PDF loses the label-to-text relationship.  
   Fix: <h3> for risk titles; <dl><dt>多头核心</dt><dd>…</dd></dl> for the verdict rows. (remedy: fix-a11y)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- accent_footprint (CLR-001): skipped: disabled by profile
- fallback_face (TYP-004): not-verified: 2 font request(s) were blocked by the capture network
- dead_band (LAY-004): skipped: disabled by profile
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: disabled by profile
- focus_ring (A11-003): skipped: disabled by profile
- targets (A11-004): skipped: disabled by profile
- headings_landmarks (A11-007): skipped: disabled by profile
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- phone_parity (ROB-002): skipped: disabled by profile
- overflow (ROB-003): skipped: disabled by profile
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 2 other request(s) blocked, e.g. font https://cdn.jsdelivr.net/gh/tw93/Kami@main/assets/fonts/TsangerJinKai02-W05.ttf
- a11y: Image-free print medium: focus order, keyboard, targets, reflow and motion are not applicable
- a11y: contrast on real pixels: no background-only render for this medium; spot-checked from DOM colours instead
- a11y: pagination: capture is a continuous 794px render, so page-break splitting (PRN-109) was not checked
- slop: disputed: chrome_glyphs (SLP-010) on '汽车与能源 · NASDAQ · 利润率在恢复…' is a false positive; T-EYEBROW passes because the line carries sector, exchange and the thesis
- slop: typeface: the intended body face (TsangerJinKai) was blocked by the capture network; the render uses Noto Serif CJK fallback, so type voice was not judged
- slop: factual accuracy of the Tesla figures: not verified against filings
- slop: T-STOCK-ORDER: 0 web stock sections; not applicable to a print note
