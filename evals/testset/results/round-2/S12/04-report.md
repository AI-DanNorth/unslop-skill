# Unslop report: /home/claude/refs/transitions-dev/example.html?style=generic

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
| Integrity | 9 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-112 Every control has an accessible name** (2x). #compareIframeOff and #compareIframeOn  
   Evidence: dom-1440.json: both iframes have empty text and no title or aria-label attribute recorded; focus.json stops 01-14 land on these frames with an empty name.  
   Fix: <iframe id="compareIframeOff" title="Share dialog with default transitions"> and title="Share dialog with tuned transitions" on #compareIframeOn (remedy: None)
2. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). Invite button focus state, inside both panes (focus/05-on.png)  
   Evidence: Focus on Invite shows only a pale grey halo (token --primary-focus-ring: rgba(0,0,0,0.3), about #b3b3b3 on white, roughly 2:1 against the white modal).  
   Fix: .invite:focus-visible { outline: 2px solid #1b1b1b; outline-offset: 2px } (remedy: None)
3. **[Floor P0] A11-143 Every field has a visible label above it** (1x). "Add people" input in both dialogs  
   Evidence: Screenshot shows no visible label; the only text is the placeholder "Add people" in --text-placeholder #9e9e9e on a near-white fill (about 2.6:1). Iframe DOM was not captured, so a hidden aria-label could not be confirmed.  
   Fix: <label for="invite-email" class="visually-hidden">Add people by name or email</label> plus a placeholder at #676767 or darker (remedy: None)
4. **[Floor P0] A11-104 Label a section by a real heading when labelled by an element.** (1x). pane labels "Generic AI output" / "With Transitions Skill"  
   Evidence: dom-1440: both labels are span.compare-pane-label inside .compare-pane-heading; no heading element exists on the page, so the two regions have no navigable names.  
   Fix: <h2 class="compare-pane-label" id="pane-off">...</h2> and wrap each pane in <section aria-labelledby="pane-off"> (remedy: None)
5. **[Floor P0] A11-009 Zoom never blocked** (1x). 375 width, top of first pane (tiles/375-00.png)  
   Evidence: The fixed "Dark mode" toolbar button sits on the same line as "Generic AI output" and abuts its end; on scroll it stays fixed over pane content.  
   Fix: At max-width 600px make .toolbar position: static (or reserve top padding equal to its height) so it never overlaps content (remedy: fix-a11y)
6. **[Reflex P1] INT-002 No default cast or fake brands** (1x). both dialogs, member rows and General access avatar stack (1440 and 375)  
   Evidence: Names are the top of a baby-name list with a matching @gmail.com address: "Mila Johnson / mila@gmail.com", "Liam Davis", "Ella Taylor", "Olivia Cole", "Ava Davis", "Noah Hart"; the 375 render shows a different random set ("Emma Cole", "James Moore", "Emma Wilson"). Sweep default_names did not fire because the names live inside the iframes.  
   Fix: One fixed, plausible team for the demo product, e.g. names and a company domain the author chooses once ([DATA NEEDED: demo team names and domain]) (remedy: fix-copy)
7. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). whole first screen, 1440  
   Evidence: Failed T-FIVE-SECOND: the only text on the page is "Dark mode", "Generic AI output" and "With Transitions Skill" (dom-1440 bodyText). The two panels render identically at rest, so a visitor cannot tell what differs or what to do (click Invite, open the Full access menu, switch to Publish).  
   Fix: One line above the panes naming the interaction to try, e.g. "Switch to Publish or open an access menu in each pane and compare the resize" (remedy: None)
8. **[Reflex P1] CON-114 Answer the five form questions before each page/screen/shot: narrative role, viewer distan** (1x). left vs right pane, member lists  
   Evidence: Left pane lists Mila Johnson / Liam Davis / Ella Taylor, right pane Olivia Cole / Ava Davis / Noah Hart; content is randomised independently per pane.  
   Fix: Identical content in both panes so motion is the only variable (remedy: None)
9. **[Reflex P1] MOT-001 Motion CSS hygiene** (5x). .modal-card  
   Evidence: transition on a layout property: "height     var(--resize-dur) var(--resize-ease),
        min"  
   Fix: Animate transform or opacity instead (remedy: fix-motion)
10. **[Reflex P1] A11-007 Headings and landmarks** (3x). page  
   Evidence: 0 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
11. **[Reflex P1] A11-004 Target size** (1x). #themeToggle  "Dark mode"  
   Evidence: touch target 94x34px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
12. **[Finish P3] INT-003 No fake people or hotlinked stock** (1x). avatar circles in every member row and the General access stack  
   Evidence: manifest.json network.blocked lists 7+ hotlinked images.unsplash.com portrait URLs (photo-1534528741775, photo-1507003211169, ...) used as avatars for the invented users. (Their broken render here is from blocked network and is not judged.)  
   Fix: Local initials or neutral avatar shapes, or self-hosted images the author owns (remedy: fix-harden)
13. **[Finish P3] SLP-012 Look-family cluster** (1x). pane labels, 1440  
   Evidence: Red cross / green check badge pair above "Generic AI output" vs "With Transitions Skill"; T-FRESH-READER lines that fit any comparison page: "Generic AI output", "With Transitions Skill".  
   Fix: Neutral labels naming what each pane does (e.g. "Default CSS transitions" / "Tuned transitions") and let the motion make the case (remedy: fix-quieter)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 0 type roles
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 20 image(s) could not load (network blocked); imagery and layout around them not verified
- a11y: disputed: sweep focus_ring hits (10) on iframe "" are false positives: focus moves into the frame and the inner controls show rings (focus/03-on.png Copy link, 04-on.png input); only the iframe element itself has outline none.
- a11y: Iframe internals (labels, ARIA on dropdowns, Escape handling) not in the captured DOM; judged from screenshots only.
- a11y: Keyboard operation of the access dropdowns and Share/Publish tabs not run live.
- a11y: Motion: overshoot easing already flagged by sweep (MOT-001); reduced-motion behaviour inside frames not tested.
- slop: Motion itself (the actual subject of the page): captures are static, so the transition differences between panes were not judged.
- slop: No 00-contract.md in the run directory; category and brief inferred from page text.
- slop: Avatar images blocked by network; their visual appearance not judged.
