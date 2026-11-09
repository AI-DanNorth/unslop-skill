# Unslop report: https://www.reidhoffman.org/linkedin-pitch-to-greylock/

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
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-003 Visible focus everywhere** (10x). a ""  
   Evidence: no visible focus indicator (outline: none 0px rgb(13, 91, 186))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] A11-006 Controls have accessible names** (1x). #SR7_2_1-3-1  
   Evidence: a has no accessible name  
   Fix: Add visible text or aria-label. (remedy: fix-a11y)
3. **[Floor P0] A11-009 Zoom never blocked** (1x). meta viewport  
   Evidence: zoom disabled (user-scalable=0; maximum-scale=1 blocks zoom): width=device-width,initial-scale=1,maximum-scale=1,user-scalable=0  
   Fix: Remove the restriction. (remedy: fix-a11y)
4. **[Floor P0] A11-011 Reduced motion respected** (1x). stylesheet  
   Evidence: page moves (keyframes anim-effect-boris, clockwise, donut-rotate) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
5. **[Floor P0] A11-114 Meaningful images get alt describing what they show** (1x). the 39 pitch-deck slide images, 1440 tiles 02-11  
   Evidence: dom-1440.json: 13 slide images have alt="" (the first five, e.g. e20y1cmsstuxxzr4jb0wzn3zgyp31epmj.jpeg, which carry text such as 'Find and Contact the People You Need Through...'), and 26 have only 'LinkedIn Series B Pitch Deck to Greylock: Slide N'. The numbering is also off by one (Slide06.jpg is labelled 'Slide 5'). The slides are the subject of the essay and are images of text.  
   Fix: alt="Slide 6: [the slide's headline and key bullets as written]", or a visually hidden transcript of each slide's text beneath it; fix the off-by-one numbering. (remedy: None)
6. **[Floor P0] A11-102 Heading levels step one at a time** (1x). heading outline  
   Evidence: 76 headings: 36 'Context', 36 'Advice', 2 empty h2s, and the page title 'Pitch Advice for Entrepreneurs' is an h2 (no h1). A headings list is 72 identical entries.  
   Fix: <h1>LinkedIn's Series B pitch to Greylock</h1>, then <h2>Slide 6: [slide title]</h2> with <h3>Context</h3><h3>Advice</h3> under it; remove the empty h2s. (remedy: None)
7. **[Reflex P1] LAY-003 Headings sit with their content** (37x). div.vc_column-inner > div.wpb_wrapper > div.wpb_text_column.wpb_content_element > div.wpb_wrapper > h2:nth-of-type(2)  
   Evidence: 0px above the heading but 10px below it: it reads as part of the block above  
   Fix: Increase space above headings; reduce space below. (remedy: fix-layout)
8. **[Reflex P1] CPY-005 No slop diction** (20x). div.vc_column-inner > div.wpb_wrapper > div.wpb_text_column.wpb_content_element > div.wpb_wrapper > p:nth-of-type(3)  "This past May was the 10th anniversary of LinkedIn"  
   Evidence: "just" (buzzwords/weak-intensifiers, cap budget 3, found 28)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
9. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .vc_gitem-animate .vc_btn  
   Evidence: "transition: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
10. **[Reflex P1] CPY-006 No repeated labels inside a card** (2x). div.wpb_column.vc_column_container > div.vc_column-inner > div.wpb_wrapper > div.wpb_text_column.wpb_content_element > div.wpb_wrapper  
   Evidence: "Context" repeated 37 times in one container  
   Fix: Say it once. (remedy: fix-copy)
11. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). div.vc_column-inner > div.wpb_wrapper > div.wpb_text_column.wpb_content_element > div.wpb_wrapper > h2:nth-of-type(1)  "Pitch Advice for Entrepreneurs"  
   Evidence: display text at 34px set in Roboto, a UI text face  
   Fix: Pick a display face for the brief; see substitutes in data/lexicons/fonts.yaml. (remedy: fix-typeset)
12. **[Reflex P1] LAY-001 Spacing has rhythm** (1x). whole page  
   Evidence: 8px is 88% of 300 spacing values (max 60%)  
   Fix: Tighten within groups, open between groups. (remedy: fix-layout)
13. **[Reflex P1] CPY-001 Words per screen within budget** (1x). screen 8 (y 6300-7200) at 1440px  
   Evidence: 300 words on one 900px screen (fail > 143)  
   Fix: Cut qualifiers and repeated claims; move detail to a page that is for reading. (remedy: fix-distill)
14. **[Reflex P1] CPY-002 Page length within budget** (1x). whole page  
   Evidence: 9412 words on the page (budget 675)  
   Fix: Read only hero and headings: if they tell the story, cut the rest. (remedy: fix-distill)
15. **[Reflex P1] CPY-004 Dash budget** (1x). whole page  
   Evidence: 41 em/spaced en dashes (budget 2)  
   Fix: Use a full stop, comma, colon or parentheses. (remedy: fix-copy)

7 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 36 image(s) could not load (network blocked); imagery and layout around them not verified
- capture: 11 other request(s) blocked, e.g. script https://static.getclicky.com/js
- a11y: Sweep Floor hits on zoom blocking (user-scalable=0, maximum-scale=1) and the slider-revolution header link without a name were confirmed in the evidence and not repeated.
- a11y: Focus 'covered by fixed or sticky element' hits on 'Skip to content' and the header links: the header card is sticky; not re-verified on the focus crops.
- a11y: Header nav pill links ('Books', 'Podcasts', 'Writing') keyboard behaviour on mobile menu.
- slop: Theme-level chrome (WordPress/WPBakery markup) is generic but unobtrusive; not judged as slop because the page's content and purpose are authored.
- slop: Analytics scripts blocked in capture (manifest network) do not affect the render.
