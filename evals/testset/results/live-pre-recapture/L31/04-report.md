# Unslop report: https://www.informationisbeautifulawards.com/showcase/7177-this-is-a-teenager

**Verdict (draft): fix**. Profile: balanced. 7 Floor finding(s) open.

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
| Integrity | 9 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). div.page-row:nth-of-type(3) > div.page-main:nth-of-type(1) > div.page-content:nth-of-type(2) > h1 > span  "by , Jan Diehm, Amber Thomas (The Pudding)"  
   Evidence: 3.59:1 against the background behind the text (10th-percentile pixel #ffffff, worst 3.59:1; text #878787, 18px; needs 4.5:1). APCA Lc 64 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (6x). input ""  
   Evidence: no visible focus indicator (outline: none 0px rgba(53, 54, 53, 0.8))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
3. **[Floor P0] A11-008 Language and title set** (1x). <html>  
   Evidence: no lang attribute  
   Fix: Add lang and a specific title. (remedy: fix-a11y)
4. **[Floor P0] A11-010 Form fields have labels** (1x). #search_q  
   Evidence: input[type=search] has no label  
   Fix: Add a visible label element. (remedy: fix-a11y)
5. **[Floor P0] A11-005 Images have text alternatives** (1x). entry hero image and related thumbnails, dom-1440  
   Evidence: The main project image has alt="Page" and the three related-project thumbnails have alt="Medium" (file-size names, not descriptions). The hero image shows 'this is a teenager by alvin chang' over a purple silhouette.  
   Fix: Hero: alt="Title screen of This is a Teenager: a purple teenage silhouette on a dark background"; thumbnails: alt="" because the project title link follows each one (remedy: fix-a11y)
6. **[Floor P0] A11-006 Controls have accessible names** (1x). image links, focus.json stops 13, 24, 26, 28  
   Evidence: Four links have empty accessible names: the hero image link to large.jpg, and the thumbnail links to /showcase/5703-gender-and-language, /5888-on-upward-mobility and /482-raw; each thumbnail link is immediately followed by a second link to the same URL with the title.  
   Fix: Wrap thumbnail and title in one link, or give the image link aria-hidden="true" tabindex="-1"; hero link aria-label="View full-size image of This is a Teenager" (remedy: fix-a11y)
7. **[Floor P0] A11-007 Headings and landmarks** (1x). focus.json order, header  
   Evidence: Tab goes logo -> main nav (About … Sponsor, y 107) -> back up to the top utility bar (Twitter, Facebook, Register, Sign In, search at y 0-7). Visual order is utility bar first.  
   Fix: Place the utility bar before the logo in source, or use CSS order only within the same container (remedy: fix-a11y)
8. **[Reflex P1] A11-004 Target size** (11x). div.header-container:nth-of-type(1) > header > div.header-row > div.logo-container:nth-of-type(1) > a  "Information is Beautiful Awards"  
   Evidence: touch target 355x40px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
9. **[Reflex P1] A11-007 Headings and landmarks** (3x). div:nth-of-type(3) > div.page-row:nth-of-type(3) > div.page-sidebar:nth-of-type(2) > div.page-sidebar-panel.no-background:nth-of-type(1) > h5  "You be the judge"  
   Evidence: heading jumps from h1 to h5  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
10. **[Reflex P1] CPY-003 Short headline** (1x). div:nth-of-type(3) > div.page-row:nth-of-type(3) > div.page-main:nth-of-type(1) > div.page-content:nth-of-type(2) > h1  "This is a Teenager"  
   Evidence: h1 has 12 words / 61 characters (max 10 / 71): "This is a Teenager by , Jan Diehm, Amber Thomas (The Pudding"  
   Fix: Say one thing; move the rest to the sub-line. (remedy: fix-copy)
11. **[Reflex P1] A11-006 Controls have accessible names** (1x). categories links, tile 01  
   Evidence: Six category links ('Longlist', 'Gold', 'Winners', 'People, Language & Identity', 'Outstanding Studio', 'Shortlist') are separated only by spacing, with no underline or separator; body links are identified by colour weight only (black on white, no underline).  
   Fix: Render as a list (<ul>) with visible separators and underline links in content areas (remedy: fix-a11y)
12. **[Reflex P1] A11-001 Text contrast on real pixels** (1x). footer, tile 01  
   Evidence: Footer link columns ('About', 'News', 'Email', 'Twitter', 'informationisbeautiful.net') are mid-grey on #50504e charcoal; visibly low contrast in the tile while the left column is white. Sweep lists 15 contrast hits; this region is consistent with them.  
   Fix: Use the same near-white as the left footer column (#fff on #50504e is ~8:1) (remedy: fix-a11y)
13. **[Reflex P1] INT-005 No placeholder residue at ship** (1x). entry byline, 1440 tile 00  
   Evidence: "by , Jan Diehm, Amber Thomas (The Pudding)": an empty first author leaves a leading comma, while Credits lists 'Alvin Chang, Journalist-Engineer, The Pudding' who is missing from the byline.  
   Fix: "by Alvin Chang, Jan Diehm, Amber Thomas (The Pudding)" (join only non-empty names) (remedy: fix-copy)
14. **[Reflex P2] A11-003 Visible focus everywhere** (2x). a "Twitter"  
   Evidence: focus indicator visible but faint: 2.65:1 against the unfocused state (target 3.0:1, WCAG 2.4.13)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
15. **[Finish P3] A11-002 Text size floors** (4x). div.page-content:nth-of-type(2) > div.page-details:nth-of-type(2) > ul > li:nth-of-type(1) > div.value:nth-of-type(2)  "Alvin Chang, Journalist-Engineer, The Pudding"  
   Evidence: 45-character run at 14px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)

4 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- reduced_motion (A11-011): skipped: no movement in stylesheets (spinners and opacity/visibility-only keyframes excluded)
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 12 other request(s) blocked, e.g. script https://s7.addthis.com/js/300/addthis_widget.js
- a11y: Vote flow and sign-in forms not exercised.
- a11y: The two tracking pixels without alt (sweep) are 0px beacons; they should get alt="" but are not user-facing.
- a11y: Embedded project content not reviewed.
- slop: AddThis share script and analytics were blocked; share widgets absent from the render are not judged.
- slop: The embedded project itself (pudding.cool) is out of scope; only the showcase page is reviewed.
