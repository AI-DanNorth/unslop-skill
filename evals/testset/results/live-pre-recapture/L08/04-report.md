# Unslop report: https://gradloom.app

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (1x). div.route-enter.relative > div.min-h-dvh > footer.py-14.px-4 > div.max-w-6xl.mx-auto > p.text-xs.text-muted-foreground\/70  "© 2026 GradLoom · Europe 🇪🇺"  
   Evidence: 3.46:1 against the background behind the text (10th-percentile pixel #fcfbf8, worst 3.46:1; text #585651, opacity 0.70, 12px; needs 4.5:1). APCA Lc 61 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 1489 characters (100% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
3. **[Floor P0] A11-114 Meaningful images get alt describing what they show** (1x). hero figure (x 758, y 200, 531x372 at 1440)  
   Evidence: dom-1440.json: the hero <svg> is aria-hidden="true"; the <figcaption> reads only 'Example: a Computer Science graduate looking for work in Poland.' The three outcomes drawn in the svg ('Data Analyst 87% match', 'BI Developer 80% match', 'Product Analyst 74% match') are hidden from assistive technology.  
   Fix: Add a visually hidden list inside the figure: <ul class="sr-only"><li>Data Analyst, 87% match</li><li>BI Developer, 80% match</li><li>Product Analyst, 74% match</li></ul>, or extend the figcaption (remedy: None)
4. **[Floor P0] A11-126 Focus not obscured (AA): sticky headers, banners, chat widgets never fully cover the focus** (1x). skip link 'Skip to main content' (focus stop 0)  
   Evidence: focus.json stop 0 has covered=true: the skip link appears at y 16 under the sticky header (confirms sweep focus_ring hit). It is the right first stop but is obscured when it shows.  
   Fix: .skip-link:focus { position: fixed; top: 8px; left: 8px; z-index: 100 } (above the header's z-index) (remedy: None)
5. **[Floor P0] A11-110 Keep all words as real text in reading order** (1x). whole page, scripts off  
   Evidence: Sweep ROB-001: 100% of text is invisible with JavaScript off; manifest also lists the React, motion and Supabase bundles. Confirms the page is client-rendered only (noted, not repeated as a new sweep hit).  
   Fix: Pre-render the marketing page (static HTML) so content exists before hydration (remedy: None)
6. **[Reflex P1] A11-004 Target size** (7x). div.min-h-dvh > header.sticky.top-0 > nav.max-w-7xl.mx-auto > div.flex.items-center:nth-of-type(1) > a.flex.items-center  
   Evidence: touch target 115x28px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] SLP-010 No template chrome glyphs** (4x). div.rounded-xl.border > figure.mt-8.rounded-lg > dl.mt-4.grid > div.col-span-2:nth-of-type(3) > dd.font-semibold.text-primary  "SQL · Power BI · Statistics"  
   Evidence: template chrome (middot-chains): "SQL · Power BI · Statistics"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
8. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (3x). :root --color-slate-50  
   Evidence: token --color-slate-50: oklch(98.4% .003 247.858) is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)
9. **[Reflex P1] MOT-001 Motion CSS hygiene** (3x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
10. **[Reflex P1] LAY-003 Headings sit with their content** (2x). #hero-title  "Find the careers your studies and skills lead to."  
   Evidence: 16px above the heading but 24px below it: it reads as part of the block above  
   Fix: Increase space above headings; reduce space below. (remedy: fix-layout)
11. **[Reflex P1] WEB-001 Performance budget** (2x). https://gradloom.app/assets/gradloom-logo-128-CgTEFjmv.webp  
   Evidence: image is 128px wide but shown at 28px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
12. **[Reflex P1] SLP-012 Look-family cluster** (2x). whole page  
   Evidence: warm-paper-serif: 3 of 6 tells (cream_bg (page #fcfbf8); terracotta_accent (#d05418); serif_display (Fraunces)); cluster minimum 3  
   Fix: Break the family on its strongest tell first; name the replacement decision. (remedy: fix-quieter)
13. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (1x). footer.py-14.px-4 > div.max-w-6xl.mx-auto > div.flex.items-center > span.relative.inline-flex:nth-of-type(1) > span.absolute.inset-0  
   Evidence: radial spotlight #0a6154 alpha 0.28  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
14. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 10 distinct font sizes: 12, 14, 15, 16, 17, 18, 20, 24, 36, 56 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
15. **[Reflex P1] CPY-001 Words per screen within budget** (1x). screen 2 (y 900-1800) at 1440px  
   Evidence: 166 words on one 900px screen (fail > 143)  
   Fix: Cut qualifiers and repeated claims; move detail to a page that is for reading. (remedy: fix-distill)

8 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 4 other request(s) blocked, e.g. script https://gradloom.app/assets/react-Bb2K1COE.js
- a11y: Live keyboard check of the About/Legal dropdowns and mobile menu (no Playwright run)
- a11y: Dark-mode contrast (only light theme captured)
- a11y: Forms: the roadmap form is on /career-setup, not captured
- a11y: disputed: none; sweep contrast hit on the footer '© 2026 GradLoom' at 3.46:1 agrees with tile 02
- slop: Brand brief: no contract overrides supplied, so the look family cannot be confirmed as chosen
- slop: Pages behind 'Build my roadmap' (not captured)
