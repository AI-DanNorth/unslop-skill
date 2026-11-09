# Unslop report: https://ant.design/docs/spec/buttons

**Verdict (draft): fix**. Profile: balanced. 10 Floor finding(s) open.

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
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (10x). tbody > tr.ant-descriptions-row > td.ant-descriptions-item > div.ant-descriptions-item-container > span.ant-descriptions-item-label.ant-descriptions-item-no-colon:nth-of-type(1)  "Docs"  
   Evidence: 3.35:1 against the background behind the text (10th-percentile pixel #ffffff, worst 3.35:1; text #000000, opacity 0.45, 14px; needs 4.5:1). APCA Lc 61 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (10x). input ""  
   Evidence: no visible focus indicator (outline: none 3px rgba(0, 0, 0, 0.88))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
3. **[Floor P0] A11-005 Images have text alternatives** (10x). div.clearfix.preview-image-boxes:nth-of-type(2) > div.preview-image-box > div.preview-image-wrapper:nth-of-type(1) > div.ant-image.css-i19pbt > img.ant-image-img.preview-img  
   Evidence: img without alt: com/mdn/rms_08e378/afts/img/A*guusTZ6ZPxkAAAAAAAAAAABkARQnAQ  
   Fix: Write what the image tells the reader, or alt="" if it tells nothing. (remedy: fix-a11y)
4. **[Floor P0] A11-006 Controls have accessible names** (10x). div:nth-of-type(4) > div.clearfix.preview-image-boxes:nth-of-type(2) > div.preview-image-box > div.preview-image-wrapper:nth-of-type(1) > div.ant-image.css-i19pbt  
   Evidence: div has no accessible name  
   Fix: Add visible text or aria-label. (remedy: fix-a11y)
5. **[Floor P0] A11-004 Target size** (8x). div.css-i19pbt.css-var-_R_afsua_ > div.ant-anchor > div.ant-anchor-link:nth-of-type(2) > div.ant-anchor-link:nth-of-type(1) > a.ant-anchor-link-title  
   Evidence: target 96x19px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
6. **[Floor P0] A11-010 Form fields have labels** (2x). div.ant-row.css-i19pbt > div.ant-col.ant-col-xs-0:nth-of-type(2) > div.acss-745902 > div.dumi-default-search-bar:nth-of-type(1) > input.dumi-default-search-bar-input  
   Evidence: input[type=text] has no label (placeholder "Type keywords..." is not a label)  
   Fix: Add a visible label element. (remedy: fix-a11y)
7. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 4506 characters (99% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
8. **[Floor P0] A11-175 Work at browser zoom 200% without loss** (1x). article header and body at 375px, tile 375-00  
   Evidence: At 375px the right-hand anchor TOC ('Design Principal', 'Types', 'Common Butto...') keeps about 150px of the width, leaving the content column ~170px: 'Edit this page' and 'LLMs.md' wrap one or two characters per line, 'Design Principal' breaks over two lines at h2 size, and the button-type demo shrinks to an unreadable thumbnail.  
   Fix: @media (max-width: 768px) { .ant-anchor-wrapper { display: none } } or move the TOC into a collapsible 'On this page' disclosure above the content. (remedy: None)
9. **[Floor P0] A11-105 Provide a skip link as the first focusable element, hidden until focused.** (1x). header and left nav, focus.json  
   Evidence: focus.json: 18 header stops (logo, search, nav, four unnamed avatar links, version select, 中/En, RTL, theme buttons) then the full left-nav tree (Introduction ... Contrast and beyond) all precede the article; the 40-stop capture ends inside the left nav without reaching 'Button'. There is no skip link or main landmark target to jump to content.  
   Fix: <a class="skip-link" href="#main-content">Skip to content</a> as the first focusable, with id="main-content" on the article. (remedy: None)
10. **[Floor P0] A11-114 Meaningful images get alt describing what they show** (1x). Do / Don't diagrams, 1440 tiles 01-03  
   Evidence: The guidance itself lives in the images (e.g. Don't: three blue primary buttons in one group; Do: primary + default + dropdown ordering). The caption text below covers only the verdict, and the images have no alt (sweep), so a screen-reader user gets 'Do / 1. Emphasize on the primary action' without the example it refers to.  
   Fix: alt="Don't: a button group with three primary (blue) buttons side by side" — one sentence per diagram describing the arrangement shown. (remedy: None)
11. **[Reflex P1] WEB-001 Performance budget** (14x). /gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg  
   Evidence: image is 200px wide but shown at 32px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
12. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .ant-anchor-wrapper .ant-anchor .ant-anchor-link-title  
   Evidence: "transition: all var(--ant-motion-duration-slow)": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
13. **[Reflex P1] A11-004 Target size** (4x). section.acss-1feyapq > div.css-i19pbt.css-var-_R_afsua_ > div.ant-anchor > div.ant-anchor-link:nth-of-type(1) > a.ant-anchor-link-title  "Design Principal"  
   Evidence: touch target 112x19px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
14. **[Reflex P1] TYP-001 Clear type hierarchy** (2x). h3 vs h4  
   Evidence: h3 18px is only 1.12x h4 16px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)
15. **[Reflex P1] A11-002 Text size floors** (2x). div.ant-anchor > div.ant-anchor-link:nth-of-type(3) > div.ant-anchor-link:nth-of-type(1) > a.ant-anchor-link-title > span  "How to Decide Button Placement?"  
   Evidence: 31-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)

12 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 image(s) could not load (network blocked); imagery and layout around them not verified
- capture: 17 other request(s) blocked, e.g. fetch https://analytics.google.com/g/collect?v=2&tid=G-QFWN0KYHTY&gtm=45je6b41v878122329za
- a11y: disputed: fallback_face 'declared AlibabaSans but Alibaba Sans drew the text' is the same family under a different name, not a missing font.
- a11y: Keyboard operation of the version select, language toggle and anchor TOC (live session).
- a11y: Dark mode and RTL variants.
- slop: Other spec pages and the components demo site.
- slop: Chinese-language version (only En captured).
