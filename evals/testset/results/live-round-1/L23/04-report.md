# Unslop report: https://www.anthropic.com

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
| Integrity | 2 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-001 No invented metrics** (4x). div.Bo9kyq_container > div.fUM8lW_cards > article.fUM8lW_card:nth-of-type(2) > div.fUM8lW_titleBlock > p.tOQyXa_body-4.fUM8lW_description  "Claude Sonnet 5.5 is a clear upgrade over Claude S"  
   Evidence: "30% less" (invented-metrics/percent-claims, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
2. **[Floor P0] ROB-001 Content never depends on animation to appear** (3x). reduced_motion  
   Evidence: 161 characters (11% of text) stay invisible with reduced motion  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
3. **[Floor P0] TYP-004 The intended font actually renders** (2x). nav.UTJ3Tq_bar > div.UTJ3Tq_start:nth-of-type(1) > div > div._7u0keW_root > a.f9ZZrG_button.f9ZZrG_corner-full  "News"  
   Evidence: declared "anthropicSans" but Anthropic Sans Web Text drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
4. **[Floor P0] A11-003 Visible focus everywhere** (1x). a "Skip to main content"  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
5. **[Floor P0] A11-126 Focus not obscured (AA): sticky headers, banners, chat widgets never fully cover the focus** (1x). skip link 'Skip to main content'  
   Evidence: focus.json / sweep: the skip link is first but reported covered by the sticky header when focused. Verified it is the first focus stop; covering confirmed by the sweep flag only.  
   Fix: .skip-link:focus { position: fixed; top: 8px; left: 8px; z-index: (header z-index + 1) } (remedy: None)
6. **[Reflex P1] A11-004 Target size** (12x). body > header.UTJ3Tq_root > nav.UTJ3Tq_bar > div.UTJ3Tq_logo:nth-of-type(2) > a  
   Evidence: touch target 35x24px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). @media (prefers-reduced-motion: no-preference)  
   Evidence: "transition: all .2s var(--ease-in-out-quart)": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
8. **[Reflex P1] A11-002 Text size floors** (4x). li.xiAwRW_slide:nth-of-type(1) > article.xiAwRW_card > a.xiAwRW_link.xiAwRW_anchor > div.xiAwRW_copy:nth-of-type(2) > span.tOQyXa_caption-1.xiAwRW_summary  "Our effort to confront the most significant challe"  
   Evidence: 99-character run at 13px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
9. **[Reflex P1] SLP-006 Vary container recipes** (2x). nav.UTJ3Tq_bar > div.UTJ3Tq_start:nth-of-type(1) > div > div._7u0keW_root > a.f9ZZrG_button.f9ZZrG_corner-full  "News"  
   Evidence: one box recipe on 6 elements across 6 selectors (#base-ui-_R_3ataq6btb_, #base-ui-_R_3btaq6btb_, #base-ui-_R_3ctaq6btb_, #base-ui-_R_6qnaq6btb_)  
   Fix: Differentiate by role: section, object, callout, well. (remedy: fix-layout)
10. **[Reflex P1] A11-112 Every control has an accessible name** (2x). announcement cards, 'System Card' rows  
   Evidence: dom-1440.json: three links with the accessible name 'View' (to /document/claude-haiku-5-5-system-card, …sonnet…, …opus…). In a links list they read 'View, View, View'. The row label 'System Card' is not part of the link name.  
   Fix: <a href="…" aria-label="View Claude Haiku 5.5 system card">View</a> (or include visually hidden text) (remedy: None)
11. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). main > article > section.ZSMdoa_root.ZSMdoa_flushTop:nth-of-type(3) > div.Bo9kyq_container > div.fUM8lW_cards  
   Evidence: "Read announcement" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
12. **[Reflex P1] A11-007 Headings and landmarks** (1x). div.Bo9kyq_container > div.fUM8lW_cards > article.fUM8lW_card:nth-of-type(1) > div.fUM8lW_titleBlock > h3.tOQyXa_headline-5.fUM8lW_title  
   Evidence: heading jumps from h1 to h3  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
13. **[Reflex P2] CPY-001 Words per screen within budget** (1x). screen 2 at 1440px  
   Evidence: 121 words on one 900px screen (warn > 120)  
   Fix: Cut qualifiers and repeated claims; move detail to a page that is for reading. (remedy: fix-distill)
14. **[Finish P3] A11-002 Text size floors** (3x). div.Bo9kyq_container > div.fUM8lW_cards > article.fUM8lW_card:nth-of-type(1) > div.fUM8lW_titleBlock > p.tOQyXa_body-4.fUM8lW_description  "Claude Haiku 5.5 is our fastest, most capable smal"  
   Evidence: 133-character run at 15px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
15. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (3x). li.xiAwRW_slide:nth-of-type(3) > article.xiAwRW_card > a.xiAwRW_link.xiAwRW_anchor > div.xiAwRW_copy:nth-of-type(2) > h3.tOQyXa_headline-5.xiAwRW_title  "Responsible scaling policy"  
   Evidence: last line is 31% of the measure at 375px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)

3 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://www.anthropic.com/_next/static/chunks/2jjnafy-v_mvn.js
- a11y: Image alt values are not recorded in the DOM capture; card images sit inside links that already have full text names, so alt="" would be correct. Sweep img_alt reported no misses.
- a11y: Live keyboard check of the header dropdowns and footer accordions
- a11y: disputed: sweep A11-007 'heading jumps from h1 to h3' on the announcement cards is real but minor; a hidden h2 ('2026 Public Benefit Report') sits in the carousel
- slop: Hero carousel slides other than the one captured
- slop: Sweep INT-001 hits on '30% less' and '40% less' are disputed: they are product claims tied to linked announcements and system cards, not invented metrics
