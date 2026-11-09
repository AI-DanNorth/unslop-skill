# Unslop report: https://linear.app

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
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). div > div._5l06ia_container.MwJdiW_root:nth-of-type(1) > main._5l06ia_content > div._7bwwmq_root._7bwwmq_wide:nth-of-type(2) > p.sc-KOGVz.igJSCV  "Powering the companies building the future"  
   Evidence: 3.45:1 against the background behind the text (10th-percentile pixel #08090a, worst 3.45:1; text #62666d, 12px; needs 4.5:1). APCA Lc 23 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-004 Target size** (7x). div.WS84WW_frame > nav.Mmx1Wq_sidebar > div.ImRUSq_root.ImRUSq_align-center:nth-of-type(1) > div.ImRUSq_root > button.Mmx1Wq_searchButton:nth-of-type(1)  
   Evidence: target 14x14px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
3. **[Floor P0] ROB-001 Content never depends on animation to appear** (2x). observer_never_fires  
   Evidence: 273 characters (4% of text) stay invisible when IntersectionObserver never fires  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
4. **[Floor P0] A11-003 Visible focus everywhere** (1x). hero product mock (sidebar) and Slack thread mock  
   Evidence: focus.json stops 12-22 are the mock's sidebar buttons ('Linear', 'Pulse', 'Inbox', 'My issues', 'Reviews', 'Initiatives', 'Projects', 'Faster app launch', 'Agent tasks', 'Agent Insights', 'UI Refresh'), and stops 25-26 are 'Send message' / 'Schedule for later' in the Slack illustration. A keyboard user tabs through 13 controls of a picture before reaching real content.  
   Fix: Add inert (or tabindex="-1" plus aria-hidden="true") to the mock containers and give each a short text description (role="img" aria-label="Linear issue view showing..."). (remedy: fix-a11y)
5. **[Reflex P1] SLP-007 No stock gradient pairs** (22x). div._7bwwmq_root._7bwwmq_wide:nth-of-type(2) > div:nth-of-type(1) > div.-B0yXq_root:nth-of-type(9) > div.WS84WW_wrapper > div.WS84WW_background:nth-of-type(1)  
   Evidence: gradient 4 stops: #08090a, #08090a, #08090a, #d0d6e0  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
6. **[Reflex P1] CPY-005 No slop diction** (19x). div.KFZpfa_commentCard.Fzcv4W_edgeHighlightRing:nth-of-type(6) > div.KFZpfa_commentEntry:nth-of-type(3) > div.ImRUSq_root.ImRUSq_align-center > div.ImRUSq_root.ImRUSq_align-baseline > span.sc-KOGVz.jwDQSd:nth-of-type(3)  "just now"  
   Evidence: "just" (buzzwords/weak-intensifiers, cap budget 3, found 5)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
7. **[Reflex P1] A11-002 Text size floors** (8x). div.KFZpfa_body.KFZpfa_contentColumn:nth-of-type(1) > div.KFZpfa_activityList:nth-of-type(4) > div.KFZpfa_activityListRow:nth-of-type(1) > div.KFZpfa_activityText:nth-of-type(2) > span:nth-of-type(1)  "created the issue via on behalf of"  
   Evidence: 34-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
8. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .rWdRxW_action  
   Evidence: "transition: all var(--speed-highlightFadeOut) var(--ease-out": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
9. **[Reflex P1] A11-004 Target size** (5x). div.TZTsQG_innerWrapper > ul.TZTsQG_list > li.TZTsQG_logoItem.TZTsQG_item:nth-of-type(1) > div > a.TZTsQG_logoLink.I_mUeq_root  
   Evidence: touch target 104x32px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
10. **[Reflex P1] LAY-004 No dead bands** (4x). y 74-280 at 1280px  
   Evidence: 206px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
11. **[Reflex P1] SLP-005 No uniform card kit** (3x). div.KFZpfa_panel > div.KFZpfa_viewBody:nth-of-type(2) > div.KFZpfa_body.KFZpfa_contentColumn:nth-of-type(1) > div.KFZpfa_chatBox:nth-of-type(11) > div.GkoSzG_panel  
   Evidence: 5 containers share radius 12px and shadow "rgba(0, 0, 0, 0.25) 0px 2px 32px 0px"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
12. **[Reflex P1] SLP-010 No template chrome glyphs** (3x). div:nth-of-type(2) > div.KFZpfa_panel > div.KFZpfa_viewBody:nth-of-type(2) > div.KFZpfa_body.KFZpfa_contentColumn:nth-of-type(1) > div.KFZpfa_activityList:nth-of-type(4)  
   Evidence: template chrome (middot-chains): "Linear created the issue via Slack on behalf of Karri · 2min"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
13. **[Reflex P1] A11-007 Headings and landmarks** (3x). div.KFZpfa_panel > div.KFZpfa_viewBody:nth-of-type(2) > div.KFZpfa_body.KFZpfa_contentColumn:nth-of-type(1) > div.KFZpfa_title:nth-of-type(1) > h3.sc-KOGVz.bFMHeH  "Faster app launch"  
   Evidence: heading jumps from h1 to h3  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
14. **[Reflex P1] TYP-002 Sizes on a declared ladder** (2x). whole page  
   Evidence: 14 distinct font sizes: 10, 11, 12, 13, 14, 15, 16, 18, 20, 24, 32, 48, 64, 72 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
15. **[Reflex P1] LAY-003 Headings sit with their content** (2x). div > div._5l06ia_container.MwJdiW_root:nth-of-type(1) > main._5l06ia_content > div._7bwwmq_root._7bwwmq_wide:nth-of-type(2) > h2.sc-KOGVz.jaIwvI  "Purpose-built for modern teams with AI workflows a"  
   Evidence: 0px above the heading but 135px below it: it reads as part of the block above  
   Fix: Increase space above headings; reduce space below. (remedy: fix-layout)

14 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 260 other request(s) blocked, e.g. script https://static.linear.app/web/_next/static/chunks/C6dSw-Yh.js
- a11y: Sweep contrast hits inside the product mock ('Workspace', 'Favorites' 1.86:1; activity lines 2.21:1) are real for the pixels but sit inside an illustration; if the mock is made inert and described (finding 1) they become decorative.
- a11y: Product and Resources menus: no live keyboard test of open/close and Escape.
- a11y: 14 script chunks were blocked (manifest network): animated sections may differ from a full load.
- slop: disputed: sweep SLP-012 violet-gradient (#6d78d5, gradient pair) comes from product-mock accents such as the Slack send button and status colours, not from a page look; INT-005 'Todo' residue is a real workflow state in the board mock.
- slop: Several sections render partly dark/empty in the 1440 tiles (agent windows); 14 script chunks were blocked (manifest network), so some animation states are missing.
