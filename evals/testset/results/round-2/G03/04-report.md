# Unslop report: /home/claude/refs/hallmark/skills/hallmark/scripts/fixtures/exemplars/atmospheric.html

**Verdict (draft): fix**. Profile: balanced. 1 Floor finding(s) open.

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
| Accessibility | 7 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 7 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-003 Visible focus everywhere** (1x). a "Skip to content"  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
2. **[Reflex P1] CPY-005 No slop diction** (1x). bar/shop pair, 1440 tile 2  
   Evidence: Failed T-RIVAL-NAME and T-THREE-LINE: "The bar / Open a bottle and stay." and "The shop / Take one home." stay true for any wine bar with a retail shelf; neither line is picturable to this place or falsifiable.  
   Fix: One concrete fact each, e.g. [DATA NEEDED: corkage or by-the-glass detail for the bar; shop price range or takeaway discount] (remedy: fix-copy)
3. **[Reflex P1] LAY-004 No dead bands** (4x). y 726-944 at 1280px  
   Evidence: 218px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
4. **[Reflex P1] TYP-001 Clear type hierarchy** (1x). h1 vs h2  
   Evidence: h1 84px is only 1.00x h2 84px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)
5. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). main > section.nights:nth-of-type(3) > div.container  
   Evidence: "Closed" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
6. **[Reflex P1] A11-004 Target size** (1x). html.js > body > header.nav > nav.nav__pill > a.wordmark  "Night Cellar"  
   Evidence: touch target 121x20px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] INT-006 At most two missing-fact slots** (1x). list section, tasting section and Find us footer, all widths  
   Evidence: Three dashed missing-fact slots on one page: "The full list: link to come.", "The next date is to be announced.", "Address to be announced". The data_slots detector did not count them because they are not literal [DATA NEEDED] text.  
   Fix: [DATA NEEDED: street address] at minimum; publish the list link and the next tasting date, or cut the list link until it exists (remedy: fix-copy)
8. **[Reflex P1] INT-145 Cut a row, column or line that would hold only a missing fact** (1x). Find us section, 1440 tile 3-4  
   Evidence: Heading "Find us after five." at display size is followed only by "Address to be announced" and two footer links; the hero's secondary CTA "Find us" and the nav item both land here.  
   Fix: [DATA NEEDED: street address, nearest station, map link]; until then drop the "Find us" CTA from the hero and nav (remedy: None)
9. **[Reflex P1] INT-176 Framing must not distort the fact** (1x). nav pill status, all widths  
   Evidence: Static text "Open tonight from 5pm" sits in the header, while the hours table says Monday to Wednesday are "Closed". The capture shows no script making it conditional.  
   Fix: Compute it from the day ("Open tonight from 5pm" / "Closed tonight, open Thursday"), or replace with the fixed "Thu to Sun from 5pm" (remedy: None)
10. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (2x). section.hero:nth-of-type(1) > div.container.hero__grid > div.hero__text > p.lead  "A shop and bar with 140 bottles on the list."  
   Evidence: last line is 21% of the measure at 375px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
11. **[Finish P3] A11-007 Headings and landmarks** (1x). header nav at 375px  
   Evidence: dom-375.json: the nav links "The list", "Tastings", "Find us" are display:none with zero rects, and no menu button exists; the 375 header shows only the wordmark and "Open tonight from 5pm". The footer repeats only "The list" and "Tastings".  
   Fix: Keep the three links visible in a second row at 375px, or add a <button aria-expanded="false" aria-controls="nav-links">Menu</button>; add "Find us" to the footer links (remedy: fix-a11y)
12. **[Finish P3] A11-010 Form fields have labels** (1x). tasting signup form, 1440 tile 3  
   Evidence: forms.json: submitting shows "Nothing was sent: this form is not connected yet." The capture does not say whether that text is in a role="status" / aria-live region, and the input has no aria-describedby.  
   Fix: Render the message in <p role="status" id="signup-msg"> and set aria-describedby="signup-msg" on #email when shown (remedy: fix-a11y)
13. **[Finish P3] TYP-001 Clear type hierarchy** (1x). h1 "Natural wine after five." vs h2 "Four nights a week, Thursday to Sunday.", 1440  
   Evidence: The hours h2 renders at the same 84px as the h1 (sweep flat_hierarchy hit) and, being two long lines, is visually heavier than the hero on tile 2.  
   Fix: Set the hours h2 to --text-section (clamp(2rem, 2.5vw + 1rem, 3.5rem)) like the other h2s (remedy: fix-typeset)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 3 image(s) could not load (network blocked); imagery and layout around them not verified
- a11y: disputed: sweep focus_ring Floor hit on "Skip to content" (covered by a fixed element). focus/00-on.png shows the skip link fully visible with its ring at x16; the fixed header pill starts at x419, so the overlap is the header's transparent full-width box, not a visual cover.
- a11y: Alt text: the three photographs were blocked in capture and no <img> elements appear in dom-1440.json, so alt quality could not be judged.
- a11y: Keyboard operation: no menus, dialogs, carousels or tabs on the page; no live Playwright run.
- a11y: Form validation messages for an invalid email were not exercised.
- a11y: Text-spacing override (1.4.12) not injected.
- slop: Photography: all three Wikimedia images were blocked in capture; the gradient frames are fallbacks, not design choices, so T-DELETION on imagery was not judged.
- slop: Fonts were shimmed (Young Serif, Instrument Sans); the render is assumed close to intended.
