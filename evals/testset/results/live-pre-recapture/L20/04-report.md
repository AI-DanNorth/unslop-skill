# Unslop report: https://www.tasteskill.dev/

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

1. **[Floor P0] A11-003 Visible focus everywhere** (2x). button "Coffee shop"  
   Evidence: no visible focus indicator (outline is set but nothing visible changes, so it is clipped or the colour of the ground: solid 2px rgb(194, 65, 12))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] A11-001 Text contrast on real pixels** (2x). hero sub-line, tile 1440-00  
   Evidence: The last line of the sub-line 'they build look designed, not generated.' (about 19px regular, white) sits on the brightest part of the gradient (about #e8611c); white on that orange is roughly 3.2:1. The sweep did not list it, so this needs a pixel check.  
   Fix: End the orange stop lower (below the CTA row) or darken the gradient behind the text block so it stays at or under #a8400f. (remedy: fix-a11y)
3. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). observer_never_fires  
   Evidence: 3513 characters (81% of text) stay invisible when IntersectionObserver never fires  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
4. **[Floor P0] A11-006 Controls have accessible names** (1x). App screens dashboard demo and footer wordmark  
   Evidence: bodyText shows rolling-digit counters as full 0-9 columns ('Orders 0 1 2 3 4 5 6 7 8 9 0 1 2 ...', 'Revenue € 0 1 2 ...') and the footer wordmark as single letters 'T a s t e S k i l l'; assistive tech reads the digit strips and spelled letters.  
   Fix: Give each counter <span class="sr-only">1,284</span> and aria-hidden="true" on the digit columns; give the wordmark aria-label="Taste Skill" and aria-hidden on the letters. (remedy: fix-a11y)
5. **[Reflex P1] SLP-007 No stock gradient pairs** (14x). html.google_sans_flex_18a1855e-module__rX4Nqq__variable.google_sans_code_f545e08f-module__whGjwG__variable > body.min-h-dvh > main > section.hero:nth-of-type(1) > div.hero-top:nth-of-type(1)  
   Evidence: gradient 7 stops: #140a05, #2a1309, #7a2306, #ff5b14, #ff7a2e  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
6. **[Reflex P1] A11-004 Target size** (12x). html.google_sans_flex_18a1855e-module__rX4Nqq__variable.google_sans_code_f545e08f-module__whGjwG__variable > body.min-h-dvh > nav.nav > a.nav-logo  "Taste Skill"  
   Evidence: touch target 97x23px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] SLP-010 No template chrome glyphs** (9x). section.section.feats-section:nth-of-type(4) > div.wrap-wide.feats:nth-of-type(2) > article.feature.feat:nth-of-type(3) > div.feature-copy:nth-of-type(2) > p  "Since v2.1 it tells a page from an app screen and "  
   Evidence: template chrome (fake-versions): "Since v2.1 it tells a page from an app screen and builds adm"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
8. **[Reflex P1] CPY-005 No slop diction** (8x). div.nf > div.nf-layer.nf-slop:nth-of-type(1) > div.nf-h.o:nth-of-type(1) > span.w:nth-of-type(1) > span  "Revolutionize"  
   Evidence: "Revolutionize" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
9. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (7x). section.hero:nth-of-type(1) > div.hero-top:nth-of-type(1) > div.hero-glow:nth-of-type(1) > div.hero-sun:nth-of-type(2) > div.hero-sun-core  
   Evidence: radial spotlight #ff9652 alpha 0.62  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
10. **[Reflex P1] A11-002 Text size floors** (7x). div.frag.fs > div.fs-body:nth-of-type(3) > div.fs-row:nth-of-type(2) > span.fs-text:nth-of-type(2) > span.fs-title:nth-of-type(1)  "385 degrees cinnamon roast coffee"  
   Evidence: 33-character run at 14px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
11. **[Reflex P1] LAY-004 No dead bands** (4x). y 864-1456 at 1280px  
   Evidence: 592px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
12. **[Reflex P1] SLP-005 No uniform card kit** (3x). body.min-h-dvh > main > section.sponsors:nth-of-type(2) > div.wrap > ul.cells  
   Evidence: 4 containers share radius 20px and shadow "rgba(20, 10, 5, 0.05) 0px 0px 0px 1px, rgba(20, 10, 5, 0.04)"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
13. **[Reflex P1] CPY-006 No repeated labels inside a card** (3x). div.wrap-wide.feats:nth-of-type(2) > article.feature.feat:nth-of-type(1) > div.feature-art:nth-of-type(1) > div.feat-float:nth-of-type(2) > div.frag.fs  
   Evidence: "CC BY-SA" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
14. **[Reflex P1] A11-007 Headings and landmarks** (3x). div.nf-layer.nf-slop:nth-of-type(1) > div.nf-card.o:nth-of-type(4) > div.nf-card-t > div.nf-ct-o:nth-of-type(1) > h4  "Lightning Fast"  
   Evidence: heading jumps from h2 to h4  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
15. **[Reflex P1] TYP-001 Clear type hierarchy** (2x). h3 vs h4  
   Evidence: h3 17px is only 1.00x h4 17px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)

14 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- contrast (A11-001): not-verified: 1 failing text run(s) not verified: rendered colour differs from the CSS colour (blend, background-clip or overlay); 190 failing text run(s) not verified: below the first viewport on a scroll-driven page (see the scroll frames); 8 failing text run(s) not verified: no glyphs painted at the DOM rect
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 13 image(s) could not load (network blocked); imagery and layout around them not verified
- capture: 1 other request(s) blocked, e.g. script https://www.tasteskill.dev/_next/static/chunks/07snibxr9ibip.js?dpl=dpl_p6tE71r3jRS
- a11y: disputed: contrast and lexicon hits inside the NoteFlow demo ('Unlock' 3.76:1, '🚀' 3.78:1) belong to an intentional bad example; the fix is to make the demo an image (finding 3), not to fix its colours.
- a11y: Much of the 1440 capture is blank (content waits on IntersectionObserver; sweep hidden_content): alt text and the before/after stepper could not be checked visually.
- a11y: No live keyboard test of the mobile menu, the tabs or the stepper.
- slop: disputed: sweep SLP-012 violet-gradient family and the 'Revolutionize', 'Unlock', 'cutting-edge', 'seamless' lexicon hits come from the 'NoteFlow' demo inside 'Before and after', which is labelled 'The default ... The page every agent ships': a quoted bad example, not the page's own look or copy.
- slop: Large parts of the 1440 capture are blank (tiles 03, 04, 09, 10, 11; sweep dead_band and hidden_content 81% when IntersectionObserver never fires): judged from dom-1440 text and the 375 tiles; one script chunk was blocked (manifest network).
