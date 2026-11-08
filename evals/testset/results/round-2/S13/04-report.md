# Unslop report: /home/claude/refs/huashu-design-en/scripts/tests/fixtures/xhs_bad.html

**Verdict (draft): fix**. Profile: balanced. 5 Floor finding(s) open.

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
| Integrity | 8 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] SOC-130 Social visual QA: fonts loaded, no overflow/clipping, inside central 80%, ≥4.5:1, aligned** (1x). canvas 1, right edge (x 1100-1364 of a 1242 canvas) and lower-left  
   Evidence: "跑出页面的字" starts at x 1100 and is 264px wide, so it is cut at the 1242 edge (tile 1242-00 shows "跑出页" and half a glyph); "压在下面的字" and "压在上面的字" are absolutely positioned 40px/10px apart and print on top of each other; "被色块盖住的字" at y 1220 sits under the #cc0000 block (60,1200,500x120) and is invisible.  
   Fix: Lay text in normal flow inside an 80% safe zone (x 124-1118) and keep blocks out of text boxes; re-export until nothing clips or overlaps (remedy: None)
2. **[Floor P0] A11-008 Language and title set** (2x). <html>  
   Evidence: no lang attribute  
   Fix: Add lang and a specific title. (remedy: fix-a11y)
3. **[Floor P0] A11-109 Keep reading order and screen-reader order equal to visual order.** (2x). canvas 1, "被色块盖住的字" under the red block  
   Evidence: The p at (80,1220) is fully covered by div (60,1200,500x120) background #cc0000 painted on top; the text exists in the DOM and is read by assistive tech and text extraction but is invisible to sighted readers.  
   Fix: Move the block out of the text box, or give the text z-index above it with 4.5:1 contrast on #cc0000 (white text on #cc0000 is 5.9:1) (remedy: None)
4. **[Floor P0] A11-009 Zoom never blocked** (1x). canvas 1 right edge; canvas 3 seam  
   Evidence: "跑出页面的字" is clipped by overflow:hidden at x 1242 (only "跑出页" visible); "这一行跨过了接缝" will be split across two exported images.  
   Fix: Constrain text boxes with max-width inside the canvas (left + width <= 1118) instead of relying on overflow clipping (remedy: fix-a11y)
5. **[Floor P0] INT-005 No placeholder residue at ship** (1x). all three canvases  
   Evidence: Every text line is placeholder that names its own defect: "小字标签" (small label), "这是一段折成好几行的正文，字号太小……" (a paragraph whose font is too small), "跑出页面的字", "压在下面的字", "被色块盖住的字", "网格塌下来压到这行说明", "这一行跨过了接缝". The sweep's placeholder detector did not catch Chinese self-describing filler.  
   Fix: [DATA NEEDED: the post's title, body copy and images] (remedy: fix-copy)
6. **[Reflex P1] CON-114 Answer the five form questions before each page/screen/shot: narrative role, viewer distan** (1x). canvas 1 as cover  
   Evidence: Failed T-FIVE-SECOND: the first canvas has no title, no hero image and no hook, only a small label and a paragraph; a reader cannot tell what the post is about, who it is for, or why to swipe. Canvas 2's six dark squares (a collapsed grid) overlap the caption "网格塌下来压到这行说明".  
   Fix: Cover = one hook headline matching the post title plus one real visual (SOC carousel cover rules); later cards carry one point each (remedy: None)
7. **[Reflex P1] SOC-124 Panorama strip: protagonist straddles seam (~2/3 left, ~1/3 right)** (1x). canvas 3 (section.xhs-strip, 2484 wide)  
   Evidence: "这一行跨过了接缝" spans x 1100-1452 across the 1242 seam of a two-panel strip; when the feed splits the strip, the line is cut in half on both images.  
   Fix: Keep text wholly inside one panel (x <= 1118 or >= 1366); only the image subject may straddle the seam (remedy: None)
8. **[Reflex P1] SOC-109 Type floors on phone-viewed canvases (image shrinks ~2.8× on phone)** (1x). canvas 1 label and body  
   Evidence: "小字标签" is 24px and the body paragraph 34px on a 1242px canvas; the canvas shrinks about 3x in the phone feed, so these read at roughly 8px and 11px.  
   Fix: label >= 32px, body >= 40px on a 1242 canvas (remedy: None)
9. **[Finish P3] A11-002 Text size floors** (1x). html > body > section.xhs-page:nth-of-type(1) > p:nth-of-type(2)  "这是一段折成好几行的正文，字号太小，在手机上读起来会很吃力。"  
   Evidence: 30-character run at 34px (hard floor 28px, dense UI 32px, body 36px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
10. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (1x). html > body > section.xhs-page:nth-of-type(1) > p:nth-of-type(2)  "这是一段折成好几行的正文，字号太小，在手机上读起来会很吃力。"  
   Evidence: last line is 14% of the measure at 1242px (3 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- accent_footprint (CLR-001): not-verified: fold-1242.png not captured
- flat_hierarchy (TYP-001): skipped: only 0 type roles
- spacing_monotony (LAY-001): skipped: only 2 spacing values
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
- a11y: Sweep Floor hits A11-008 (no lang, no title) confirmed from dom-1242: lang and title are empty; for an exported image they matter only in the HTML source.
- a11y: Keyboard, focus, forms and motion: none present on a static social canvas.
- a11y: Contrast not machine-verified (no background render); judged visually.
- slop: No 00-contract.md and no real content, so T-RIVAL-NAME, T-MIRROR and T-THREE-LINE had nothing to test beyond the placeholder lines.
- slop: Look-family check: none apply (white ground, default sans-serif, one red block); slop here is absence of design, not a default style.
