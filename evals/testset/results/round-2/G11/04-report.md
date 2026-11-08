# Unslop report: /home/claude/refs/huashu-design-en/scripts/tests/fixtures/xhs_ok.html

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
| Integrity | 8 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-008 Language and title set** (2x). <html>  
   Evidence: no lang attribute  
   Fix: Add lang and a specific title. (remedy: fix-a11y)
2. **[Floor P0] INT-005 No placeholder residue at ship** (1x). whole canvas  
   Evidence: Head "大标题 / 第二行！" (literally 'big title / second line!'), body "正文四十二像素……用来确认检查不会冤枉干净的页面" ('42px body ... to confirm the check does not wrong a clean page'), label "标签三十二" ('label thirty-two'). All placeholder that names its own spec.  
   Fix: [DATA NEEDED: post title, body and label text] (remedy: fix-copy)
3. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (1x). html > body > section.xhs-page > p  "正文四十二像素，折成两行也不算违规，这是一段足够长、会换行的正文内容，用来确认检查不会冤枉干净的页面"  
   Evidence: last line is 8% of the measure at 1242px (3 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
4. **[Finish P3] A11-110 Keep all words as real text in reading order** (1x). h1 "大标题第二行！"  
   Evidence: dom-1242: the h1 text is "大标题第二行" with the line break forced by a narrow width (480px), and the '！' is a separate red span; text extraction reads the two lines as one run with no break or space.  
   Fix: Use an explicit <br> (or two spans with display:block) so the visual line break is also in the text (remedy: None)
5. **[Finish P3] LAY-004 No dead bands** (1x). y 700 to 1560 of the 1242x1660 canvas (tile 1242-01 is entirely white)  
   Evidence: About 860px, more than half the canvas height, is empty between the body paragraph and the bottom label; there is no image or visual.  
   Fix: Fill the band with the post's real visual (photo or screenshot), or move the label up under the body and crop the canvas to content (remedy: fix-layout)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- accent_footprint (CLR-001): not-verified: fold-1242.png not captured
- flat_hierarchy (TYP-001): skipped: only 2 type roles
- spacing_monotony (LAY-001): skipped: only 0 spacing values
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
- a11y: Sweep Floor hits A11-008 (no lang, no title) confirmed in dom-1242 (title and lang empty); they matter for the HTML source, not the exported image.
- a11y: Keyboard, focus, forms and motion: not applicable to a static social canvas.
- a11y: Contrast not machine-verified (no background render); judged from DOM colours.
- slop: No real content or 00-contract.md, so T-RIVAL-NAME, T-MIRROR and T-THREE-LINE had nothing beyond placeholder lines to test.
- slop: Default sans-serif face (no font specified) not counted against the read, since no brand typography is defined.
