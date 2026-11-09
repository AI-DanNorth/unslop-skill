# Unslop report: https://kin-ai.replit.app

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (2x). div.min-h-screen.bg-background:nth-of-type(1) > main.relative.z-10 > section.container.mx-auto:nth-of-type(1) > h1.text-5xl.sm\:text-7xl > span.text-primary  "with your family."  
   Evidence: 1.06:1 against the background behind the text (10th-percentile pixel #bfc0c3, worst 1.00:1; text #00d1c3, 48px; needs 3.0:1). APCA Lc 0 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] ROB-001 Content never depends on animation to appear** (2x). observer_never_fires  
   Evidence: 2734 characters (60% of text) stay invisible when IntersectionObserver never fires  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
3. **[Floor P0] A11-011 Reduced motion respected** (1x). stylesheet  
   Evidence: page moves (keyframes enter, exit) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
4. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). hero primary CTA 'Get KinAI for Free' and header 'Download', 1440  
   Evidence: focus.json stop 3: outline 'none', focus shown only as a 1px rgb(0,209,195) ring on a button filled with the same #00d1c3; focus/03-on.png is indistinguishable from the resting state apart from the existing glow.  
   Fix: .btn:focus-visible { outline: 2px solid #f8fafc; outline-offset: 3px; } (remedy: None)
5. **[Reflex P1] SLP-151 Hero template tells: a pill or label above the headline, a gradient blob, an empty coloure** (1x). hero, 1440 tile 00 and 375 tile 00  
   Evidence: Failed T-MIRROR: pill badge with bolt icon 'Now with a guided family setup' above a centred two-tone h1 'Share your local AI / with your family.' with the second line in the accent cyan, glowing pill CTA + ghost second CTA, on a near-black page with a radial teal wash. This is the stock dark AI-product hero; a neighbouring local-LLM app would get the same.  
   Fix: Open on the product: the 'What Mom asks stays Mom's' welcome screenshot is the strongest image; put it beside a plain head instead of below the fold in a frame. (remedy: None)
6. **[Reflex P1] A11-004 Target size** (11x). div.min-h-screen.bg-background:nth-of-type(1) > nav.fixed.top-0 > div.container.mx-auto > div.flex.items-center:nth-of-type(1) > a  
   Evidence: touch target 79x25px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] CPY-005 No slop diction** (10x). div > div.min-h-screen.bg-background:nth-of-type(1) > main.relative.z-10 > section.container.mx-auto:nth-of-type(1) > p.text-xl.text-muted-foreground  "One Mac hosts KinAI and connects to your local LLM"  
   Evidence: "simple" (buzzwords/weak-intensifiers, cap budget 3, found 8)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
8. **[Reflex P1] WEB-001 Performance budget** (9x). https://kin-ai.replit.app/icon.svg  
   Evidence: image is 512px wide but shown at 32px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
9. **[Reflex P1] MOT-001 Motion CSS hygiene** (6x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
10. **[Reflex P1] SLP-009 No neon violet or cyan on headings** (5x). div.min-h-screen.bg-background:nth-of-type(1) > main.relative.z-10 > section.container.mx-auto:nth-of-type(1) > h1.text-5xl.sm\:text-7xl > span.text-primary  "with your family."  
   Evidence: neon cyan #00d1c3 on dark ground  
   Fix: Derive the accent from brand, imagery or culture (Sample, Converge, Justify). (remedy: fix-colorize)
11. **[Reflex P1] SLP-010 No template chrome glyphs** (5x). nav.fixed.top-0 > div.container.mx-auto > div.flex.items-center:nth-of-type(1) > a > div.whitespace-nowrap.inline-flex  "v0.2.148"  
   Evidence: template chrome (fake-versions): "v0.2.148"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
12. **[Reflex P1] SLP-005 No uniform card kit** (2x). main.relative.z-10 > section.container.mx-auto:nth-of-type(3) > div.grid.grid-cols-1:nth-of-type(2) > div:nth-of-type(1) > div.rounded-xl.border  
   Evidence: 27 containers share radius 16px and shadow "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
13. **[Reflex P1] CPY-004 Dash budget** (2x). whole page  
   Evidence: 12 em/spaced en dashes (budget 2)  
   Fix: Use a full stop, comma, colon or parentheses. (remedy: fix-copy)
14. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 9 distinct font sizes: 12, 14, 16, 18, 20, 24, 30, 36, 72 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
15. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). div > div.min-h-screen.bg-background:nth-of-type(1) > main.relative.z-10 > section.container.mx-auto:nth-of-type(1) > h1.text-5xl.sm\:text-7xl  "Share your local AI"  
   Evidence: display text at 72px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)

15 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: focus_ring 'focused element is covered by a fixed or sticky element' fires on all 29 stops, including the hero CTA; focus/03-on.png shows the CTA fully visible, so the cover is likely a full-page fixed background layer, not a real obstruction.
- a11y: disputed: contrast on h1 span 'with your family.' (1.06:1 against #bfc0c3) — the tile shows cyan on near-black, clearly legible; the sampler read the gradient-clipped first line, not the background.
- a11y: disputed in part: contrast hits on feature cards with text opacity 0.15-0.70 ('Guided Family Setup', 'Parallel Research') are fade-in animation frames; the real defect is ROB-001 (content depends on IntersectionObserver), already in the sweep.
- a11y: Carousel auto-advance and pause control (2.2.2): needs a live session.
- a11y: Keyboard operation of tabs and accordion not run live.
- slop: Carousel slides beyond the first (only the active slide is visible in the tiles).
- slop: Install-guide tabs other than 'Mac Host'.
