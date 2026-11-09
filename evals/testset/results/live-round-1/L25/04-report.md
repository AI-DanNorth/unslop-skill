# Unslop report: https://linear.app

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
| Integrity | 4 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). div.WS84WW_frameWrapper:nth-of-type(4) > div.WS84WW_frame > nav.Mmx1Wq_sidebar > div:nth-of-type(3) > button.Mmx1Wq_navItem.Mmx1Wq_collapsible:nth-of-type(1)  "Workspace"  
   Evidence: 1.86:1 against the background behind the text (10th-percentile pixel #141516, worst 1.86:1; text #62666d, opacity 0.58, 12px; needs 4.5:1). APCA Lc 9 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-004 Target size** (7x). div.WS84WW_frame > nav.Mmx1Wq_sidebar > div.ImRUSq_root.ImRUSq_align-center:nth-of-type(1) > div.ImRUSq_root > button.Mmx1Wq_searchButton:nth-of-type(1)  
   Evidence: target 14x14px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
3. **[Floor P0] INT-005 No placeholder residue at ship** (3x). div.KFZpfa_activityList:nth-of-type(10) > div.KFZpfa_activityListRow > div.KFZpfa_activityText:nth-of-type(2) > span:nth-of-type(1) > span.sc-KOGVz.dYCPFa:nth-of-type(2)  "Todo"  
   Evidence: "Todo" (self-labels/residue, fail)  
   Fix: Fill with real content or a visible [DATA NEEDED] slot. (remedy: fix-copy)
4. **[Floor P0] A11-003 Visible focus everywhere** (2x). a "Skip to content →"  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
5. **[Floor P0] A11-006 Controls have accessible names** (2x). div > div._5l06ia_container.MwJdiW_root:nth-of-type(1) > main._5l06ia_content > div._7bwwmq_root._7bwwmq_wide:nth-of-type(2) > a.MR81zG_logosLink.Fzcv4W_focusRingInset  
   Evidence: a has no accessible name  
   Fix: Add visible text or aria-label. (remedy: fix-a11y)
6. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 922 characters (14% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
7. **[Reflex P1] SLP-007 No stock gradient pairs** (22x). div._7bwwmq_root._7bwwmq_wide:nth-of-type(2) > div:nth-of-type(1) > div.-B0yXq_root:nth-of-type(9) > div.WS84WW_wrapper > div.WS84WW_background:nth-of-type(1)  
   Evidence: gradient 4 stops: #08090a, #08090a, #08090a, #d0d6e0  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
8. **[Reflex P1] CPY-005 No slop diction** (19x). div.KFZpfa_commentCard.Fzcv4W_edgeHighlightRing:nth-of-type(6) > div.KFZpfa_commentEntry:nth-of-type(3) > div.ImRUSq_root.ImRUSq_align-center > div.ImRUSq_root.ImRUSq_align-baseline > span.sc-KOGVz.jwDQSd:nth-of-type(3)  "just now"  
   Evidence: "just" (buzzwords/weak-intensifiers, cap budget 3, found 5)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
9. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .rWdRxW_action  
   Evidence: "transition: all var(--speed-highlightFadeOut) var(--ease-out": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
10. **[Reflex P1] A11-002 Text size floors** (7x). div.KFZpfa_body.KFZpfa_contentColumn:nth-of-type(1) > div.KFZpfa_activityList:nth-of-type(4) > div.KFZpfa_activityListRow:nth-of-type(1) > div.KFZpfa_activityText:nth-of-type(2) > span:nth-of-type(1)  "created the issue via on behalf of"  
   Evidence: 34-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
11. **[Reflex P1] A11-004 Target size** (5x). div.TZTsQG_innerWrapper > ul.TZTsQG_list > li.TZTsQG_logoItem.TZTsQG_item:nth-of-type(1) > div > a.TZTsQG_logoLink.I_mUeq_root  
   Evidence: touch target 104x32px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
12. **[Reflex P1] LAY-004 No dead bands** (4x). y 74-280 at 1280px  
   Evidence: 206px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
13. **[Reflex P1] SLP-005 No uniform card kit** (3x). div.KFZpfa_panel > div.KFZpfa_viewBody:nth-of-type(2) > div.KFZpfa_body.KFZpfa_contentColumn:nth-of-type(1) > div.KFZpfa_chatBox:nth-of-type(11) > div.GkoSzG_panel  
   Evidence: 5 containers share radius 12px and shadow "rgba(0, 0, 0, 0.25) 0px 2px 32px 0px"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
14. **[Reflex P1] SLP-010 No template chrome glyphs** (3x). div:nth-of-type(2) > div.KFZpfa_panel > div.KFZpfa_viewBody:nth-of-type(2) > div.KFZpfa_body.KFZpfa_contentColumn:nth-of-type(1) > div.KFZpfa_activityList:nth-of-type(4)  
   Evidence: template chrome (middot-chains): "Linear created the issue via Slack on behalf of Karri · 2min"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
15. **[Reflex P1] A11-007 Headings and landmarks** (3x). div.KFZpfa_panel > div.KFZpfa_viewBody:nth-of-type(2) > div.KFZpfa_body.KFZpfa_contentColumn:nth-of-type(1) > div.KFZpfa_title:nth-of-type(1) > h3.sc-KOGVz.bFMHeH  "Faster app launch"  
   Evidence: heading jumps from h1 to h3  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)

16 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 258 other request(s) blocked, e.g. script https://static.linear.app/web/_next/static/chunks/rnPQlBzV.js
- a11y: Sweep contrast hits inside the product mock ('Workspace', 'Favorites' 1.86:1; activity lines 2.21:1) are real for the pixels but sit inside an illustration; if the mock is made inert and described (finding 1) they become decorative.
- a11y: Product and Resources menus: no live keyboard test of open/close and Escape.
- a11y: 14 script chunks were blocked (manifest network): animated sections may differ from a full load.
- slop: disputed: sweep SLP-012 violet-gradient (#6d78d5, gradient pair) comes from product-mock accents such as the Slack send button and status colours, not from a page look; INT-005 'Todo' residue is a real workflow state in the board mock.
- slop: Several sections render partly dark/empty in the 1440 tiles (agent windows); 14 script chunks were blocked (manifest network), so some animation states are missing.
