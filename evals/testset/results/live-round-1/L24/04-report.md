# Unslop report: https://www.nimblestudio.com/story/creating-an-anti-ai-brand-in-times-of-artificial-everything

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
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (5x). div.padding-global > div.container-large.m-flex-hr > div.banners_wrapper > div.banner_content > a.banner-link.mobile:nth-of-type(2)  "Discovery our cutting-edge AI offering →"  
   Evidence: 2.85:1 against the background behind the text (10th-percentile pixel #2ba2e3, worst 2.40:1; text #ffffff, 14px; needs 4.5:1). APCA Lc 59 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] TYP-004 The intended font actually renders** (2x). div.padding-global > div.container-large.m-flex-hr > div.banners_wrapper > div.banner_content > a.banner-link.desktop:nth-of-type(1)  "Discovery our cutting-edge AI offering →"  
   Evidence: declared "Suisseintl" but Suisse Int'l drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
3. **[Floor P0] A11-011 Reduced motion respected** (1x). stylesheet  
   Evidence: page animates (keyframes or transform transitions) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
4. **[Floor P0] A11-102 Heading levels step one at a time** (1x). article section 'What This Visual Language Is Actually Saying', 1440 tiles 03-05  
   Evidence: The five numbered points ('1. Craft and intention.' ... '5. Rebellion against algorithmic homogenization.') are <p><strong> (p:nth-of-type(12), p:nth-of-type(20)), not h3s or a list; they look like subheads but are not in the heading outline.  
   Fix: <h3>1. Craft and intention.</h3> (or an <ol> whose items start with the bold lead). (remedy: None)
5. **[Floor P0] A11-112 Every control has an accessible name** (1x). 'Have you read these?' cards, 1440 tile 11  
   Evidence: Three links named 'Read story →' each go to a different article; the card titles are separate links. Out of context the links list shows three identical 'Read story → ' entries with the arrow read as 'right arrow'.  
   Fix: Make the whole card one link named by the title, or add <span class="sr-only"> OpenAI DevDay: 25 releases</span> and aria-hidden on the arrow. (remedy: None)
6. **[Reflex P1] CPY-005 No slop diction** (23x). div.padding-global > div.container-large.m-flex-hr > div.banners_wrapper > div.banner_content > a.banner-link.desktop:nth-of-type(1)  "Discovery our cutting-edge AI offering →"  
   Evidence: "cutting-edge" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
7. **[Reflex P1] A11-004 Target size** (12x). div.padding-global > div.container-large.m-flex-hr > div.banners_wrapper > div.banner_content > a.banner-link.mobile:nth-of-type(2)  "Discovery our cutting-edge AI offering →"  
   Evidence: touch target 254x17px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
8. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .card-large  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
9. **[Reflex P1] WEB-001 Performance budget** (6x). 805d6e7e2f7790c7a8/66dff213472f9f364f3bca0c_nimble-black.svg  
   Evidence: image is 2224px wide but shown at 160px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
10. **[Reflex P1] SLP-007 No stock gradient pairs** (2x). nav.nav.navigation > section.banner_component  
   Evidence: gradient hue span 71° + banned pair (hues 265-330 with 200-264): #2fdbfb, #2442bb, #726fb0  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
11. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 10 distinct font sizes: 14, 16, 18, 19, 20, 22.5, 24, 32, 40, 48 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
12. **[Reflex P1] CPY-001 Words per screen within budget** (1x). screen 7 (y 5400-6300) at 1440px  
   Evidence: 294 words on one 900px screen (fail > 143)  
   Fix: Cut qualifiers and repeated claims; move detail to a page that is for reading. (remedy: fix-distill)
13. **[Reflex P1] CPY-002 Page length within budget** (1x). whole page  
   Evidence: 1899 words on the page (budget 675)  
   Fix: Read only hero and headings: if they tell the story, cut the rest. (remedy: fix-distill)
14. **[Reflex P1] SLP-012 Look-family cluster** (1x). whole page  
   Evidence: violet-gradient: 3 of 4 tells (ai_purple (#2442bb); gradient_pair (banned gradient pair); scattered_radii (10 radii: 100px, 12px, 160px, 16px, 1px, 20px)); cluster minimum 3  
   Fix: Break the family on its strongest tell first; name the replacement decision. (remedy: fix-quieter)
15. **[Reflex P1] CPY-153 Ban summary transitions and template framing** (1x). article body, 1440 tiles 02-09  
   Evidence: Failed T-OVER-CORRECTION: the prose leans on model cadence: 'The question isn't whether this is a trend. It obviously is. The question is why...', 'Let me be direct about something...', 'this isn't a nostalgia movement. This isn't Gen Z wanting... This is something stranger and more deliberate.', 'This isn't random aesthetic preference. It's a coordinated signal about five things:', 'The implication is clear.', 'Not making machines feel warm. Making the organizations...', fragment runs 'Heritage typography. Craft traditions. The texture of film photography. Hand-drawn marks.'  
   Fix: State the claim directly with the author's own evidence: 'In our NimbleFest brief to Ruben, five signals came up:' (remedy: None)

7 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 34 other request(s) blocked, e.g. script https://www.nimblestudio.com/story/%E2%80%9Chttps://sdk.intent.upflowy.com/upflowy-
- a11y: Sweep fallback_face Floor hits ('declared Suisseintl but Suisse Int'l drew the text') look like a naming mismatch for the same family, not a missing font: disputed: same face rendered under a different family name.
- a11y: Keyboard operation of the Industries/Technologies mega-menu dropdowns (live session needed).
- a11y: Countdown in the NimbleFest screenshot is a static image, so 2.2.2 does not apply here.
- slop: Sweep look_family 'violet-gradient' rests on the promo bar gradient and scattered radii; the article body itself does not show that family.
- slop: Whether the speaker portraits are generated (the article shows an AI workflow canvas of portrait variations); not judged as fake people because the article discloses the process.
