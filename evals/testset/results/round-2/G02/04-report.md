# Unslop report: /home/claude/refs/hallmark/skills/hallmark/scripts/fixtures/exemplars/modern-minimal.html

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
| Accessibility | 1 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 7 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (2x). figure.slot.app > div.ui > div.ledger:nth-of-type(3) > div.ledger__row.is-open:nth-of-type(5) > span.fig.late:nth-of-type(3)  "2 Oct"  
   Evidence: 4.49:1 against the background behind the text (10th-percentile pixel #f9e4de, worst 4.49:1; text #bb3d31, 13px; needs 4.5:1). APCA Lc 63 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Reflex P1] SLP-119 Flag product-chrome sameness: tight grotesk at weight 600, near-white ground, one blue acc** (1x). whole page surface, 1440 and 375  
   Evidence: T-MIRROR on the surface only: tight heavy grotesk display, warm near-white ground (oklch 0.97 0.006 55), a single salmon/red accent, every button and status as a pill (Sign up, Start for £8 a month, See a reminder, All/Chasing/Paid chips, Sent/Paid badges) and an 8px-radius soft-shadow panel recipe on four figures (sweep card_kit). A neighbouring fintech brief would get the same skin. The display face was meant to be General Sans (blocked at capture), so the exact face was not judged.  
   Fix: Keep pills for status badges only (where they mean state) and give buttons a different shape; take one cue from invoices themselves (ruled ledger lines, tabular figures already in Geist Mono) into the page chrome (remedy: None)
3. **[Reflex P1] A11-002 Text size floors** (10x). div.slot.client > div.client__in > div.doc.mail:nth-of-type(1) > p.mail__foot > span  "Sent by Tilly for Example Studio"  
   Evidence: 32-character run at 13px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
4. **[Reflex P1] A11-004 Target size** (6x). body > header.site > div.container.site__in > a.wordmark  "Tilly"  
   Evidence: touch target 47x25px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
5. **[Reflex P1] LAY-004 No dead bands** (4x). y 698-920 at 1280px  
   Evidence: 222px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
6. **[Reflex P1] INT-002 No default cast or fake brands** (3x). figure.slot.app > div.ui > div.ledger:nth-of-type(3) > div.ledger__row.is-open:nth-of-type(5) > span:nth-of-type(2)  "Example Kitchen"  
   Evidence: "Example Kitchen" (default-names/fake-specifics, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
7. **[Reflex P1] SLP-005 No uniform card kit** (1x). main > section.hero:nth-of-type(1) > div.container.hero__grid > figure.slot.app  
   Evidence: 4 containers share radius 8px and shadow "oklch(0.2 0.01 35 / 0.05) 0px 1px 2px 0px, oklch(0.2 0.01 35"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
8. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 22 distinct font sizes: 9.5, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 16, 17, 21, 22, 24, 25, 26, 28, 52, 84, 240 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
9. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). #hero-head  "Never writefollowing up”again."  
   Evidence: display text at 84px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
10. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). section.hero:nth-of-type(1) > div.container.hero__grid > figure.slot.app > div.ui > div.ledger:nth-of-type(3)  
   Evidence: "Paid" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
11. **[Reflex P1] ROB-002 Phone parity** (1x). figure.slot.app > div.ui > div.ui__bar:nth-of-type(1) > span.ui__chips:nth-of-type(2) > span.ui__chip:nth-of-type(2)  "Clients"  
   Evidence: 114 words shown at 1440px are hidden at 375px (62 elements)  
   Fix: Reflow instead of hiding. (remedy: fix-layout)
12. **[Reflex P1] A11-113 Every svg, canvas or CSS-art element carries aria-hidden="true", an aria-label, a labelled** (1x). figure.slot.app (hero, #replies) and figure.showcase > div.slot.client  
   Evidence: The product mocks are built from live HTML text with no role, accessible name or aria-hidden (dom-1440: name null, ariaHidden null). A screen reader reads them inline as page content: 'Tilly Invoices Clients Replies 2 Search invoices New invoice Invoices All Chasing Paid Outstanding £4,520.00 No. Client Due Amount Status 0045 Example Press...' (bodyText), roughly 250 words of mock UI, including fake control labels ('Search invoices', 'New invoice') that are not controls. Only the showcase has a figcaption.  
   Fix: <figure class="slot app" role="img" aria-label="Tilly's invoice list: seven invoices, £4,520 outstanding, invoice 0042 to Example Kitchen being chased with reminder 2 due today"> with the inner .ui aria-hidden="true"; or keep it readable but add a <figcaption> naming it as a screen of the app (remedy: None)
13. **[Reflex P2] CPY-001 Words per screen within budget** (1x). screen 4 at 1440px  
   Evidence: 137 words on one 900px screen (warn > 120)  
   Fix: Cut qualifiers and repeated claims; move detail to a page that is for reading. (remedy: fix-distill)
14. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (3x). section.q.q--replies:nth-of-type(4) > div.container.split > div.split__text > p.lead  "Tilly files the reply with the invoice it answers,"  
   Evidence: last line is 25% of the measure at 375px (3 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
15. **[Finish P3] A11-002 Text size floors** (2x). div.slot.client > div.client__in > div.doc.inv:nth-of-type(2) > div.inv__lines:nth-of-type(4) > span:nth-of-type(1)  "Menu illustrations, six dishes"  
   Evidence: 30-character run at 15px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)

6 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fallback_face (TYP-004): not-verified: 1 font request(s) were blocked by the capture network
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 image(s) could not load (network blocked); imagery and layout around them not verified
- capture: 1 other request(s) blocked, e.g. stylesheet https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600&display=swap
- a11y: sweep A11-002 label hits (10-11px) are all inside product mocks; real but subordinate to the mock-labelling finding
- a11y: sweep A11-004 targets: wordmark and nav links 25px tall at 375, real for 'Pricing' (no other route except footer)
- a11y: focus ring on the dark pricing band: accent red against near-black is under 3:1, but the ring hugs light cream controls where it exceeds 3:1 (focus/06-on.png, 07-on.png); judged passing
- a11y: forms errors: email field not submitted with invalid value live; required/aria-invalid wiring not visible
- a11y: photo alt: the one photo was blocked and is a CSS background on figure.photo with no name; could not confirm whether it is decorative
- a11y: reflow at 320px not captured; 375 reflows cleanly, mock tables lose columns by design (sweep ROB-002)
- slop: Display face: General Sans stylesheet blocked at capture, so the sweep's TYP-003 'Inter as display' hit is a fallback artefact; disputed
- slop: Photograph content: blocked at capture; judged from the footer credit only
- slop: 'Example Press / Films / Kitchen ...' sample names: sweep INT-002 already reports; they are honest self-labels but trip INT-134, left to synthesis
- slop: T-STOCK-ORDER: hero with product mock, then question sections, then pricing band with signup, footer: 2 stock sections
- slop: copy voice: no contract or brand samples supplied
