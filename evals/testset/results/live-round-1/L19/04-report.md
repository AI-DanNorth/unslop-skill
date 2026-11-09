# Unslop report: https://impeccable.style

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
| Integrity | 6 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). div.fn:nth-of-type(1) > div.fn-form:nth-of-type(2) > span.fn-btn:nth-of-type(5) > span.fn-sw.is-grow:nth-of-type(2) > span.fn-b:nth-of-type(1)  "Submit"  
   Evidence: 4.21:1 against the background behind the text (10th-percentile pixel #b14ece, worst 4.21:1; text #fcfcfc, 13px; needs 4.5:1). APCA Lc 73 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] ROB-001 Content never depends on animation to appear** (3x). reduced_motion  
   Evidence: 171 characters (2% of text) stay invisible with reduced motion  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
3. **[Floor P0] A11-109 Keep reading order and screen-reader order equal to visual order.** (1x). testimonial marquee under the hero  
   Evidence: focus.json stops 13-39 are all testimonial cards (the capture's 40-stop budget runs out inside the wall); dom-1440.json lists every card link twice (the loop copy is a live, focusable duplicate, e.g. 'Impeccable > Claude design Mertcan Yüzer' ×2). A keyboard user must tab through 60+ links of praise before reaching 'Detects and removes AI slop.', and a screen reader reads each quote twice.  
   Fix: Add aria-hidden="true" and inert to the duplicated track; make only the first copy focusable, or make cards non-links with a single 'Read all on X' link. (remedy: None)
4. **[Reflex P1] WEB-001 Performance budget** (21x). https://impeccable.style/assets/pi-logo.svg  
   Evidence: image is 150px wide but shown at 22px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
5. **[Reflex P1] CPY-005 No slop diction** (17x). div.t-marquee-row > div.t-marquee-track > div.t-marquee-set:nth-of-type(1) > a.t-card.t-card--plinth:nth-of-type(5) > blockquote.t-card-quote  "When anyone asks me about design for frontend I al"  
   Evidence: "very" (buzzwords/weak-intensifiers, cap budget 3, found 5)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
6. **[Reflex P1] A11-004 Target size** (12x). html > body.home-kinpaku.kinpaku-chrome > header.site-header > a.site-header-brand  
   Evidence: touch target 121x34px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] SLP-010 No template chrome glyphs** (10x). a.slop-pattern-item.slop-pattern-item--markers:nth-of-type(8) > span.slop-pattern-specimen.slop-pattern-specimen--markers > span.slop-target.slop-target--markers > span:nth-of-type(1) > b  "01"  
   Evidence: template chrome (numbering-tokens): "01"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
8. **[Reflex P1] SLP-007 No stock gradient pairs** (7x). section.slop-teaser-section.slop-pattern-section:nth-of-type(2) > div.slop-pattern-board > a.slop-pattern-item.slop-pattern-item--soft-card:nth-of-type(2) > span.slop-pattern-specimen.slop-pattern-specimen--soft-card  
   Evidence: gradient 4 stops: #2d333d, #000000, #2d333d, #000000  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
9. **[Reflex P1] LAY-004 No dead bands** (4x). y 1982-2143 at 1280px  
   Evidence: 161px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
10. **[Reflex P1] SLP-001 No eyebrow labels above headings** (3x). div.hotel-suites:nth-of-type(2) > div.hotel-suites-row > article.hotel-card:nth-of-type(1) > div.hotel-card-body:nth-of-type(2) > p.hotel-card-kicker:nth-of-type(1)  "Suite"  
   Evidence: 9px label tracked 0.20em caps above 24px heading "Garden Suite"; 3 on page, budget 2  
   Fix: Promote the fact into the heading or delete the label (T-EYEBROW). (remedy: fix-typeset)
11. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (3x). div.hotel-site:nth-of-type(1) > div.hotel-suites:nth-of-type(2) > div.hotel-suites-row > article.hotel-card:nth-of-type(1) > div.hotel-card-photo:nth-of-type(1)  
   Evidence: radial spotlight #e4d8ab alpha 0.70  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
12. **[Reflex P1] SLP-009 No neon violet or cyan on headings** (3x). a.slop-pattern-item.slop-pattern-item--markers:nth-of-type(8) > span.slop-pattern-specimen.slop-pattern-specimen--markers > span.slop-target.slop-target--markers > span:nth-of-type(1) > b  "01"  
   Evidence: violet text #5954cc (oklch hue 280, chroma 0.18) at 27.2px  
   Fix: Derive the accent from brand, imagery or culture (Sample, Converge, Justify). (remedy: fix-colorize)
13. **[Reflex P1] SLP-014 No cards inside cards** (3x). div.slop-pattern-board > a.slop-pattern-item.slop-pattern-item--nested:nth-of-type(6) > span.slop-pattern-specimen.slop-pattern-specimen--nested > span.slop-target.slop-target--nested > span.slop-nested-card:nth-of-type(2)  
   Evidence: card inside a card (span.slop-target.slop-target--nested)  
   Fix: Keep one container level; group inside it with spacing or a rule. (remedy: fix-layout)
14. **[Reflex P1] INT-002 No default cast or fake brands** (3x). li.fn-li:nth-of-type(2) > span.fn-nm:nth-of-type(2) > b > span.fn-sw > span.fn-b:nth-of-type(1)  "Mara Okafor"  
   Evidence: "Okafor" (default-names/default-cast, cap budget 0, found 3)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
15. **[Reflex P1] SLP-004 No side-tab accent borders on cards** (2x). div.hero-proof-panel.is-active:nth-of-type(1) > div.hero-proof-layer.hero-proof-layer--before:nth-of-type(1) > div.hero-proof-canvas.hero-proof-canvas--polish > article.proof-polish.proof-polish--before  
   Evidence: 7px left border, others ≤1px, radius 8px  
   Fix: Use grouping, a heading or one surface change instead. (remedy: fix-quieter)

18 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 11 other request(s) blocked, e.g. fetch https://www.google-analytics.com/g/collect?v=2&tid=G-TEXGHC7V34&gtm=45je6b41v9247027
- a11y: Several sweep contrast/text-size hits ('Submit' 4.21:1 on #b14ece, 'MO'/'JL'/'PN' avatars) sit on the deliberate sample interface inside the command console; they are real rendered text so not disputed, but they are demo content.
- a11y: Whether the testimonial wall auto-scrolls (2.2.2): tiles show cards cut at both edges but no motion evidence.
- a11y: Live keyboard test of the role=slider faders and the /polish /distill /clarify toggles.
- a11y: Gallery thumbnails appear blank in tiles; images report complete in dom, so treated as a capture timing artefact.
- slop: Explore-directions thumbnails render as blank grey in tiles 1440-06 although dom reports the images complete; likely a fade-in not triggered by capture, not judged as design.
- slop: Gallery, Docs and Slop sub-pages.
