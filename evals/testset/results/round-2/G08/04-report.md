# Unslop report: /home/claude/refs/huashu-design-en/scripts/tests/fixtures/lint_clean.html

**Verdict (draft): fix**. Profile: balanced. 6 Floor finding(s) open.

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

1. **[Floor P0] INT-005 No placeholder residue at ship** (5x). html > body > div:nth-of-type(2) > p  "这里是第二段正文，同样写得足够长，用来让脚本识别正文的字号与字体设置是否达标。"  
   Evidence: "用来让脚本" (self-labels/residue, fail)  
   Fix: Fill with real content or a visible [DATA NEEDED] slot. (remedy: fix-copy)
2. **[Floor P0] A11-008 Language and title set** (1x). <title>  
   Evidence: page has no title  
   Fix: Add lang and a specific title. (remedy: fix-a11y)
3. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > div.hero:nth-of-type(1) > div.side:nth-of-type(2)  
   Evidence: page is 414px wide at a 375px viewport (sideways scroll); widest culprit 154px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
4. **[Floor P0] A11-007 Headings and landmarks** (1x). div.big '截图归位'  
   Evidence: The visual headline is a <div class="big">, so the page has no heading at all; the sweep reported '0 visible h1', and the judgment here is that the only candidate heading exists but is not marked up.  
   Fix: <h1 class="big">截图<br>归位</h1> inside <main> (remedy: fix-a11y)
5. **[Floor P0] A11-009 Zoom never blocked** (1x). <head>  
   Evidence: dom-1440 meta is empty: there is no <meta name="viewport">. Real phones will lay the page out at about 980px and scale it down, making the 17px body text about 6px; the 375 capture shows the narrow layout only because the harness forced the width.  
   Fix: <meta name="viewport" content="width=device-width, initial-scale=1"> (remedy: fix-a11y)
6. **[Floor P0] A11-175 Work at browser zoom 200% without loss** (1x). 375px hero  
   Evidence: At 375px the fixed 2fr/1fr grid keeps the navy panel, which squeezes the claim to two characters per line (375-00.png: 四千 / 八百 / 张截 …), 20 lines for one sentence, and the page is 414px wide (sweep).  
   Fix: @media (max-width: 40rem) { .hero { grid-template-columns: 1fr; } .big { font-size: clamp(64px, 22vw, 140px); padding: 24px; } .side { padding: 24px; } } (remedy: None)
7. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). first screen  
   Evidence: T-FIVE-SECOND: 'what' is half answered (截图归位, 'screenshots back in place', and the side claim), 'for whom' is not answered, and 'what to do' has no answer: there is no product name, link, download or price anywhere on the page.  
   Fix: Add the product name and one action under the claim [DATA NEEDED: product name, platform, download or purchase link] (remedy: None)
8. **[Reflex P1] LAY-001 Spacing has rhythm** (2x). whole page  
   Evidence: 60px is 75% of 16 spacing values (max 60%)  
   Fix: Tighten within groups, open between groups. (remedy: fix-layout)
9. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: 0 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
10. **[Reflex P1] LAY-004 No dead bands** (1x). navy side panel, 1440px x 960-1440 y 0-640  
   Evidence: The navy panel is a third of the first screen and holds one 17px sentence at its top; about 500px of solid navy sits below it. The left 2fr column is also empty under the headline. T-SCREEN-BY-SCREEN: screen 1 has its reason (the headline); the panel does not earn its area.  
   Fix: Put the evidence in the panel: the claim set large (4,800 → 37), or a real before/after of a screenshot folder [DATA NEEDED: real capture] (remedy: fix-layout)
11. **[Finish P3] TYP-004 The intended font actually renders** (1x). headline '截图归位' and body  
   Evidence: Headline stack is Impact, "Arial Black", sans-serif at weight 900 and body Helvetica, Arial; none has Chinese glyphs, so every character falls back to Noto Sans CJK SC Regular (fonts.json) with synthetic bold. The intended heavy poster face never renders.  
   Fix: font: 900 140px/0.95 "Source Han Sans SC", "Noto Sans SC", "PingFang SC", sans-serif (a CJK family with a real Heavy weight) (remedy: fix-typeset)
12. **[Finish P3] TYP-001 Clear type hierarchy** (1x). headline line-height, 1440px  
   Evidence: At line-height 0.9 the two lines '截图' and '归位' touch: the bottom of 截/图 meets the top of 归/位 (tile 1440-00, y ~185-200). CJK ideographs fill the em box, so a Latin-tuned 0.9 leading collides.  
   Fix: line-height: 1.0 to 1.05 for CJK display (remedy: fix-typeset)
13. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (2x). html > body > div.hero:nth-of-type(1) > div.side:nth-of-type(2) > p  "四千八百张截图，整理成三十七个文件夹。每一张都能用一句话找回来，全程离线。"  
   Evidence: last line is 11% of the measure at 1280px (3 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
14. **[Finish P3] A11-101 Set lang on html, a <title> in the page's own words, a one-sentence meta description.** (1x). <html lang>  
   Evidence: lang="zh" without script; the text is Simplified Chinese.  
   Fix: <html lang="zh-Hans"> (or zh-CN), and add <title>截图归位</title> (remedy: None)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 0 type roles
- fake_send (INT-004): skipped: no forms
- focus_ring (A11-003): skipped: page has no interactive controls
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: focus order and keyboard: the page has no focusable element (sweep), so nothing to walk; that absence is covered by the slop lens (no action)
- a11y: verified sweep Floor hits: no <title> (stands), residue paragraph (stands)
- slop: brief and audience: no contract, so whether a poster-only page was intended cannot be checked
