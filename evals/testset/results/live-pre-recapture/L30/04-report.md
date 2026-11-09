# Unslop report: https://brand.dropbox.com

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
| Accessibility | 1 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-003 Visible focus everywhere** (2x). a "Imagery"  
   Evidence: focused element is entirely hidden by a fixed or sticky element (WCAG 2.4.11)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
2. **[Floor P0] A11-011 Reduced motion respected** (1x). intro sequence, tiles 1440-00 / 01 and 375-00  
   Evidence: The intro statements are revealed by scroll: the sweep found the same sentence at 13%, 16% and 21% opacity in successive frames, and the 375 frame shows the text alone on a mostly blank screen. With no prefers-reduced-motion rule (sweep), the reveal and the animated logo run for everyone.  
   Fix: @media (prefers-reduced-motion: reduce) { .home-logo-container, .button-title-1 { transition: none; opacity: 1 } } (remedy: fix-motion)
3. **[Reflex P1] MOT-001 Motion CSS hygiene** (5x). #nav-button  
   Evidence: 1 elements transition "all" (0.6s): every property change animates, including layout  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
4. **[Reflex P1] A11-004 Target size** (4x). div.outro-info:nth-of-type(3) > div.outro-links:nth-of-type(2) > a.outro-link.w-inline-block:nth-of-type(1)  
   Evidence: touch target 163x20px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
5. **[Reflex P1] A11-007 Headings and landmarks** (4x). page  
   Evidence: 0 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
6. **[Reflex P1] LAY-004 No dead bands** (2x). y 228-703 at 1280px  
   Evidence: 475px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
7. **[Reflex P1] A11-005 Images have text alternatives** (1x). credits line  
   Evidence: bodyText reads 'Dropbox Brand Studio 🤝 Daybreak Studio': the emoji between the two credit links is announced as 'handshake'.  
   Fix: <span aria-hidden="true">🤝</span><span class="sr-only">with</span> (remedy: fix-a11y)
8. **[Reflex P2] A11-003 Visible focus everywhere** (1x). a "Motion"  
   Evidence: focused element is partly hidden by a fixed or sticky element (WCAG 2.4.12)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
9. **[Finish P3] CPY-005 No slop diction** (2x). div.outro-paragraphs:nth-of-type(1) > p.p:nth-of-type(1)  "These guidelines are meant to help you create thin"  
   Evidence: "ecosystem" (buzzwords/dead-metaphors, context)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
10. **[Finish P3] A11-002 Text size floors** (2x). div.outro-paragraphs:nth-of-type(1) > p.p:nth-of-type(1)  "These guidelines are meant to help you create thin"  
   Evidence: 193-character run at 14px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): not-verified: 1 stylesheet(s) could not be read; a prefers-reduced-motion rule may be in them
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://www.dropbox.com/pithos/privacy_consent
- a11y: disputed: A11-001 contrast 1.76:1 on 'Imagery' sampled a white #ffffff background; the title sits on the maroon tile, where pink #ffafa5 is about 5:1. Likely the white gutter between tiles.
- a11y: Sweep focus_ring hits (no visible indicator on 'Voice & Tone', 'Typography'; 'Logo', 'Color', 'Imagery', 'Motion' covered by a fixed element) were not re-verified in focus crops.
- a11y: Capture used 3 scroll frames (manifest prep); motion between frames not seen. No main landmark (sweep) not repeated.
- slop: The page is a scroll-driven sequence; the capture used 3 scroll frames as tiles (manifest prep), so in-between motion states were not seen.
- slop: Content of the eight sub-pages (Framework, Logo, Color, ...) not captured.
