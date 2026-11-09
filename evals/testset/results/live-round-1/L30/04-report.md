# Unslop report: https://brand.dropbox.com

**Verdict (draft): fix**. Profile: balanced. 3 Floor finding(s) open.

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

1. **[Floor P0] A11-003 Visible focus everywhere** (7x). a "Voice & Tone"  
   Evidence: no visible focus indicator (outline: auto 1px rgb(16, 16, 16))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] A11-001 Text contrast on real pixels** (4x). button.tile-menu-tile.nav-button > div.nav-button-content:nth-of-type(3) > div.nav-button-title-container:nth-of-type(1) > h3.nav-button-title.nav-button-title-1:nth-of-type(1)  "At Dropbox, our Brand Guidelines help us infuse ev"  
   Evidence: 1.21:1 against the background behind the text (10th-percentile pixel #f7faff, worst 1.21:1; text #0061fe, opacity 0.13, 24px; needs 3.0:1). APCA Lc 10 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] A11-011 Reduced motion respected** (2x). button.tile-menu-tile.nav-button > div.home-logo-container.w-embed:nth-of-type(4) > svg.home-logo > path  
   Evidence: page animates (keyframes or transform transitions) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
4. **[Reflex P1] MOT-001 Motion CSS hygiene** (5x). #nav-button  
   Evidence: 1 elements transition "all" (0.6s): every property change animates, including layout  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
5. **[Reflex P1] A11-004 Target size** (4x). div.outro-info:nth-of-type(3) > div.outro-links:nth-of-type(2) > a.outro-link.w-inline-block:nth-of-type(1)  
   Evidence: touch target 163x20px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
6. **[Reflex P1] A11-007 Headings and landmarks** (4x). page  
   Evidence: 0 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
7. **[Reflex P1] LAY-004 No dead bands** (2x). y 228-569 at 1280px  
   Evidence: 341px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
8. **[Reflex P1] A11-005 Images have text alternatives** (1x). credits line  
   Evidence: bodyText reads 'Dropbox Brand Studio 🤝 Daybreak Studio': the emoji between the two credit links is announced as 'handshake'.  
   Fix: <span aria-hidden="true">🤝</span><span class="sr-only">with</span> (remedy: fix-a11y)
9. **[Reflex P2] A11-003 Visible focus everywhere** (1x). a "Logo"  
   Evidence: focus indicator visible but faint: 1.79:1 against the unfocused state (target 3.0:1, WCAG 2.4.13)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
10. **[Finish P3] CPY-005 No slop diction** (2x). div.outro-paragraphs:nth-of-type(1) > p.p:nth-of-type(1)  "These guidelines are meant to help you create thin"  
   Evidence: "ecosystem" (buzzwords/dead-metaphors, context)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Finish P3] A11-002 Text size floors** (2x). div.outro-paragraphs:nth-of-type(1) > p.p:nth-of-type(1)  "These guidelines are meant to help you create thin"  
   Evidence: 193-character run at 14px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://www.dropbox.com/pithos/privacy_consent
- a11y: disputed: A11-001 contrast 1.76:1 on 'Imagery' sampled a white #ffffff background; the title sits on the maroon tile, where pink #ffafa5 is about 5:1. Likely the white gutter between tiles.
- a11y: Sweep focus_ring hits (no visible indicator on 'Voice & Tone', 'Typography'; 'Logo', 'Color', 'Imagery', 'Motion' covered by a fixed element) were not re-verified in focus crops.
- a11y: Capture used 3 scroll frames (manifest prep); motion between frames not seen. No main landmark (sweep) not repeated.
- slop: The page is a scroll-driven sequence; the capture used 3 scroll frames as tiles (manifest prep), so in-between motion states were not seen.
- slop: Content of the eight sub-pages (Framework, Logo, Color, ...) not captured.
