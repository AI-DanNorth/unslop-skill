# Unslop report: /home/claude/refs/huashu-design-en/scripts/tests/fixtures/lint_reskin.html

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
| Accessibility | 2 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 4 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-005 No placeholder residue at ship** (2x). html > body > div.wrap > p  "这是一段足够长的正文，用来让体检脚本识别正文字号和字体，内容本身不重要。"  
   Evidence: "内容本身不重要" (self-labels/residue, fail)  
   Fix: Fill with real content or a visible [DATA NEEDED] slot. (remedy: fix-copy)
2. **[Floor P0] A11-008 Language and title set** (1x). <title>  
   Evidence: page has no title  
   Fix: Add lang and a specific title. (remedy: fix-a11y)
3. **[Floor P0] A11-121 Every function is operable by keyboard** (1x). div.card > a.cta '了解更多 →' (x4)  
   Evidence: The four links are <a class="cta"> with no href (dom-1440: href absent, cursor: pointer styled in CSS). Without href an anchor is not focusable and has no link role, which is why the sweep's Tab walk reached nothing. They look like links but cannot be reached or activated by keyboard.  
   Fix: <a class="cta" href="#[DATA NEEDED: destination per step]">...</a>, or remove the links if there is nowhere to go (remedy: None)
4. **[Floor P0] A11-112 Every control has an accessible name** (1x). div.card > a.cta (x4)  
   Evidence: All four links share the identical name '了解更多 →' ('Learn more') with no programmatic context (no aria-describedby, no heading inside the card); out of context a screen-reader link list reads 'Learn more' four times.  
   Fix: Visible text naming the target, e.g. '了解产地' ('About the origin'), or aria-describedby pointing at the card's heading once one exists (remedy: None)
5. **[Floor P0] INT-130 Never ship lorem ipsum, "Title Text", "[company name]", "[insert", "[NEED", {{template tok** (1x). div.wrap > p and all four card paragraphs  
   Evidence: Card copy is self-describing filler: '第一张卡片里的说明文字，也写得足够长一些。' ('Explanatory text in the first card, also written long enough'), repeated with 二/三/四. The sweep caught the lede ('内容本身不重要', 'the content itself does not matter'); the four card bodies are the same residue and were not flagged.  
   Fix: [DATA NEEDED: what actually happens at each of origin, process and roast]; until supplied, remove the cards (remedy: None)
6. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). first screen, 1440 and 375  
   Evidence: Failed T-FIVE-SECOND: the h1 '每一杯，都有一段履历。' ('Every cup has a record') and the eyebrow 'ORIGIN · PROCESS · ROAST' imply coffee, but no brand, product, audience or action appears anywhere; the only links are four identical '了解更多 →' ('Learn more') with no destination.  
   Fix: [DATA NEEDED: who roasts, what is sold, and the one action (buy, subscribe, visit)]; name it in the h1 or sub-line and give one primary link with a real href (remedy: None)
7. **[Reflex P1] SLP-138 Refuse the stock template page: hero, 3 features, (testimonials), CTA, footer** (1x). div.grid: four .card blocks  
   Evidence: Failed T-DEFAULT-AGENT and T-MIRROR: a 'how it works' 1-2-3(-4) step grid of equal rounded cards (14px radius, same soft shadow), each '0N / STEP N / two lines / Learn more →', is the stock section any brand in any category gets. The eyebrow promises three stages (Origin · Process · Roast) but the grid has four generic 'STEP' cards that name none of them.  
   Fix: Name the stages in the headings themselves (origin, processing, roast, [DATA NEEDED: fourth stage or drop it]) and lay them as a sequence that reads as one process, not four equal tiles (remedy: None)
8. **[Reflex P1] TYP-151 Disable synthetic bold/italic and load real files for every style used** (1x). h1 > em '履历' (76px, yellow)  
   Evidence: The h1 is declared in Impact, which has no CJK glyphs, so it renders in Noto Sans CJK SC (fonts.json); the em applies font-style: italic to Chinese, producing a synthetic oblique slant. The yellow italic 'one emphasised word' is the stock hero trick translated literally into a script that has no italic.  
   Fix: Set the h1 in a real CJK display face; mark emphasis with weight or colour only (font-style: normal), or drop the emphasis (remedy: None)
9. **[Reflex P1] SLP-010 No template chrome glyphs** (8x). html > body > div.wrap > div.eyebrow:nth-of-type(1)  "Origin · Process · Roast"  
   Evidence: template chrome (middot-chains): "Origin · Process · Roast"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
10. **[Reflex P1] CPY-006 No repeated labels inside a card** (2x). html > body > div.wrap  
   Evidence: "了解更多 →" repeated 4 times in one container  
   Fix: Say it once. (remedy: fix-copy)
11. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
12. **[Reflex P1] SLP-005 No uniform card kit** (1x). html > body > div.wrap > div.grid:nth-of-type(2) > div.card:nth-of-type(1)  
   Evidence: 4 containers share radius 14px and shadow "rgba(0, 0, 0, 0.1) 0px 2px 8px 0px"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
13. **[Reflex P1] LAY-140 Never squeeze a text block into a sliver (under ~16 chars wide over 4+ lines)** (1x). div.grid at 375px  
   Evidence: The grid keeps repeat(3, 1fr) at phone width: cards are 88-99px wide with text columns 40-51px, so body text wraps every 2-3 characters across 11 lines and '了解更多 →' breaks over three lines (375 tiles 00-01). The fourth card orphans on its own row at both widths (LAY-137).  
   Fix: @media (max-width: 640px) { .grid { grid-template-columns: 1fr } }; at desktop use 2x2 or 4 across for four items (remedy: None)
14. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (4x). body > div.wrap > div.grid:nth-of-type(2) > div.card:nth-of-type(1) > p  "第一张卡片里的说明文字，也写得足够长一些。"  
   Evidence: last line is 17% of the measure at 1280px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
15. **[Finish P3] A11-008 Language and title set** (1x). div.eyebrow and card labels  
   Evidence: html lang="zh" but the eyebrow 'Origin · Process · Roast' and 'STEP ONE..FOUR' are English with no lang="en" on those elements, so a Chinese voice reads them with Chinese phonetics.  
   Fix: <div class="eyebrow" lang="en">...</div>, or translate the labels (remedy: fix-a11y)

1 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 1 type roles
- fake_send (INT-004): skipped: no forms
- focus_ring (A11-003): skipped: page has no interactive controls
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: verified sweep Floor A11-003 'Tab reached no focusable element': real, caused by href-less anchors (reported above as the keyboard cause, not a duplicate)
- a11y: verified sweep Floor A11-008 missing <title>: real, <title> empty
- a11y: sweep Reflex no <main>: real
- a11y: images: none on the page
- a11y: forms: none on the page
- a11y: 320px reflow not captured
- slop: No strengths recorded: navy plus one yellow accent and the h1 line are the only decisions, and the yellow accent on navy is a stock pairing here, not argued
- slop: T-STOCK-ORDER: hero + 1-2-3 steps only (2 stock sections); short page, generated read rests on placeholder copy and default kit, not skeleton length
- slop: T-RIVAL-NAME: there is no brand name to swap; every line would hold for any coffee seller
- slop: Look family: dark-single-accent partially (navy ground L about 0.32, not below 0.20; one vivid yellow accent; mono numerals) so not counted as a cluster
- slop: copy voice: no contract or brand samples supplied
