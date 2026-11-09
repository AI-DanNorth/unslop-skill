# Unslop report: https://messenger.abeto.co

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
| Accessibility | 4 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-121 Every function is operable by keyboard** (1x). #global-ui controls: four .side-button (right edge, 65x65 at x 1345), .dialog-button, ten .emoji-bg cells, .continue-button (174x58 centred)  
   Evidence: dom-1440.json lists 17 visible control-shaped elements, all plain <div> with no role, no accessible name, no text and not interactive; focus.json has 0 stops. Nothing on the page can be reached by Tab.  
   Fix: <button type="button" class="continue-button">Continue</button>; side buttons as <button aria-label="[DATA NEEDED: what each does, e.g. Map, Sound]">; emoji cells as a radiogroup or buttons with aria-label per emoji. (remedy: None)
2. **[Floor P0] A11-113 Every svg, canvas or CSS-art element carries aria-hidden="true", an aria-label, a labelled** (1x). #webgl canvas (full viewport)  
   Evidence: The whole experience is a WebGL canvas with no text alternative: body text is empty (dom bodyText ''), no h1, no main (sweep), and the canvas carries no aria-label or fallback content.  
   Fix: <canvas role="img" aria-label="Messenger: a small illustrated planet where you deliver letters"> plus a visually hidden <h1>Messenger</h1> and a short text description of how to play inside <main>. (remedy: None)
3. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: 0 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
4. **[Finish P3] CON-121 Let one idea run the page top to bottom** (1x). first screen, 1440 tile 00 and 375 tile 00  
   Evidence: Failed T-FIVE-SECOND (in this capture): the first screen is the planet alone on teal with no visible title, prompt or control; the only words are in the meta description ('It's a small planet, but someone's gotta make the deliveries.'). The 'continue-button' and checklist panels exist in the DOM but render empty.  
   Fix: Show the game name 'Messenger' and a 'Click to start' prompt over the intro until the 3D scene is interactive. (remedy: None)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 0 type roles
- spacing_monotony (LAY-001): skipped: only 0 spacing values
- words_per_screen (CPY-001): skipped: no text
- fake_send (INT-004): skipped: no forms
- focus_ring (A11-003): skipped: page has no interactive controls
- reduced_motion (A11-011): skipped: no movement in stylesheets (spinners and opacity/visibility-only keyframes excluded)
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://messenger.abeto.co/assets/App3D-DwM1eiaC.js
- a11y: The App3D script was blocked during capture, so in-game UI, dialogs and keyboard handling (which may exist in the canvas layer) could not be checked; the findings rest on the DOM shell that did load.
- a11y: Motion (2.2.2) and reduced-motion behaviour of the rotating world; contrast of in-game text (none rendered).
- a11y: Reflow at 320px: tile 375-00 shows the canvas scaling; no text to clip.
- slop: Blocked script https://messenger.abeto.co/assets/App3D-DwM1eiaC.js (manifest network): the interactive world, UI buttons, emoji panel and checklist content did not render, so gameplay UI and any copy are not verified.
- slop: Motion and interaction (scripted clicks) not captured.
