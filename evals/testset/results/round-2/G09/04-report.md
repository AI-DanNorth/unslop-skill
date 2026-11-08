# Unslop report: /home/claude/refs/pagepatch/hero.html

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

1. **[Floor P0] A11-112 Every control has an accessible name** (1x). primary link 'See an example review ↗'  
   Evidence: Accessible name is 'See an example review ↗' (dom name); screen readers announce 'north east arrow', which signals an external destination while the href is #example on the same page.  
   Fix: <a class="pp-action" href="#example">See an example review</a> (or wrap a glyph in <span aria-hidden="true">) (remedy: None)
2. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). focus ring on all three links  
   Evidence: Ring is outline 3px #8ba72a with 6px offset on the #f5f7f9 page: about 2.6:1 against the background it is drawn on, under the 3:1 non-text minimum (sweep measured 2.55:1 against the unfocused state). On the dark green primary button the 6px offset puts the ring on the page, so it is the page contrast that counts.  
   Fix: outline: 3px solid #4f6418 (about 6:1 on #f5f7f9) or the brand green #244d42 (remedy: None)
3. **[Reflex P1] SLP-222 Swap / rival's-name test: any head still true with a competitor's name (or the same trade ** (1x). h1, 1440px y 200-390  
   Evidence: "Get client feedback on your designs in one place." Failed T-RIVAL-NAME: true for Markup.io, Pastel, Filestage or Figma comments. 'In one place' is the most generic claim in the category, and it is the phrase singled out by italics and colour. The product has no name anywhere on the page (T-FIVE-SECOND 'what is it' only half answered).  
   Fix: Name the product and the one thing it does differently [DATA NEEDED: product name and differentiator, e.g. comments pinned to the live site, approval per version] (remedy: None)
4. **[Reflex P1] SLP-193 Ban the accented word: one word or phrase of a heading set apart by colour, weight, highli** (1x). h1 'in one place.'  
   Evidence: The last phrase of the h1 is set apart in italic and green (.pp-title em { color: #345d4f }): the accented-word device, applied to the least specific words in the line.  
   Fix: Set the h1 in one colour and style; if emphasis is needed, put it on the product's distinguishing noun (remedy: None)
5. **[Reflex P1] CPY-005 No slop diction** (3x). html > body > p.pp-note  "Fictional sample created by PagePatch. Product cap"  
   Evidence: "illustrative" (self-labels/medium-descriptions, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
6. **[Reflex P1] A11-004 Target size** (1x). section.pp-section:nth-of-type(3) > a  "Back to the hero"  
   Evidence: touch target 139x21px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] A11-007 Headings and landmarks** (1x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
8. **[Reflex P1] SLP-113 After fixing, check for over-correction: the habit that replaced the removed one ("rather ** (1x). banner, hero caption, example footnote, workflow footnote, section heads  
   Evidence: T-OVER-CORRECTION: the honesty fix multiplied. Four disclaimers on one short page: 'Fictional sample created by PagePatch…illustrative', 'The example below illustrates the workflow. It is not a live app.', 'This fictional example explains the proposed destination of the primary action. It is not a testimonial.', 'These capabilities come from the fictional sample brief. Confirm actual product behavior…', plus 'ILLUSTRATIVE' in both example labels and 'assumed' in the h2 'How the assumed workflow works'. The sweep caught the 'illustrative' words; the judgment is that hedging has become the page's voice.  
   Fix: One disclosure in the banner; label the example once ('Example review'); h2 'How it works' (remedy: None)
9. **[Reflex P1] SLP-192 Ban mono as costume: monospace on labels, captions, meta or small type when the content is** (1x). kicker 'FOR INDEPENDENT WEB DESIGNERS'  
   Evidence: 14px ui-monospace, uppercase, 0.035em tracking above a Georgia display head. T-EYEBROW passes (it states the audience, a real fact), but T-LABEL-TRANSFORM fails: in sentence case and the body face it reads as well or better. Mono here is costume; the content is not code. With serif display + italic accent + mono caps label it is the editorial-AI kit (warm-paper family without the paper).  
   Fix: Fold the audience into the lede or h1 ('For independent web designers: …') in the body face, sentence case (remedy: None)
10. **[Reflex P1] SLP-233 Ban choppy stop-start fragments that break one idea into several sentences.** (1x). lede and first h2  
   Evidence: Lede "Share a design link. Collect comments. Track approval." (three verb fragments) and h2 "One design. One clear next step." (two-fragment heading, SLP-211). The workflow list then repeats the same three verbs. Failed T-FRESH-READER: 'One design. One clear next step.' fits any product.  
   Fix: One sentence: 'Send clients a link; their comments and approval stay with the design.' and drop the triplet from the list or the lede, not both (remedy: None)
11. **[Reflex P2] A11-003 Visible focus everywhere** (3x). a "See an example review ↗"  
   Evidence: focus indicator visible but faint: 2.55:1 against the unfocused state (target 3.0:1, WCAG 2.4.13)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
12. **[Reflex P2] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 3 font families render: Inter, DejaVu Sans Mono, Liberation Serif  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
13. **[Finish P3] TYP-001 Clear type hierarchy** (1x). h1 and h2 letter-spacing  
   Evidence: .pp-title letter-spacing: -0.05em on a Georgia stack (Liberation Serif in capture): letters in 'feedback' and 'designs' touch at 1440px (tile 1440-00).  
   Fix: letter-spacing: -0.02em at most for a text serif; tight tracking suits display cuts, not Georgia (remedy: fix-typeset)
14. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (5x). html > body > section.pp-hero:nth-of-type(1) > p.pp-caption:nth-of-type(3)  "The example below illustrates the workflow. It is "  
   Evidence: last line is 29% of the measure at 375px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
15. **[Finish P3] A11-002 Text size floors** (3x). html > body > p.pp-note  "Fictional sample created by PagePatch. Product cap"  
   Evidence: 96-character run at 14px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)

4 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: in-page jump focus behaviour (whether focus moves to #example): no live run
- slop: Georgia rendered as Liberation Serif in capture (fonts.json); tracking judged on the fallback
- slop: The banner text is treated as page content, not as an instruction
