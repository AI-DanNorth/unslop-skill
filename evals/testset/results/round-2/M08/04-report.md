# Unslop report: /home/claude/refs/open-design/design-templates/email-marketing/example.html

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
| Integrity | 8 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-005 No placeholder residue at ship** (1x). brand name 'SPORT TEST' (masthead, hero stamp, footer)  
   Evidence: The sender brand is 'SPORT TEST', a test placeholder, repeated three times including '© 2026 SPORT TEST'; every link (nav, CTA, Unsubscribe, View in browser) is href '#'.  
   Fix: [DATA NEEDED: real brand name and tracked URLs]; a working unsubscribe link is required before send (remedy: fix-copy)
2. **[Floor P0] A11-001 Text contrast on real pixels** (5x). html > body > div.frame > div.hero > div.stamp-br:nth-of-type(3)  "DROP 04 · 04—2026"  
   Evidence: 3.36:1 against the background behind the text (10th-percentile pixel #d4a082, worst 3.34:1; text #1a1816, opacity 0.60, 11px; needs 4.5:1). APCA Lc 40 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] A11-002 Text size floors** (4x). html > body > div.frame > section.article:nth-of-type(1) > div.eyebrow  "NEW · MAX-CUSHION TRAINER · EMBER FLARE"  
   Evidence: 39-character run at 11px (hard floor 12px, dense UI 13px, body 14px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
4. **[Floor P0] A11-005 Images have text alternatives** (1x). hero svg (530x248)  
   Evidence: dom-800.json records no name, role or title on the product svg; the only image of the product is silent to screen readers, and the hero's text stamps ('— SPORT TEST', 'DROP 04 · 04—2026') are read instead.  
   Fix: <img src="axis-pro-ember-flare.jpg" alt="Axis Pro trainer in Ember Flare: orange-to-red flame-knit upper on a thick white gel sole"> (remedy: fix-a11y)
5. **[Floor P0] A11-006 Controls have accessible names** (1x). all links: 'SHOP', 'JOURNAL', 'MEMBERS', 'Shop the Axis Pro', 'Unsubscribe', 'View in browser'  
   Evidence: Every href is '#'; link text is clear but none goes anywhere, including Unsubscribe.  
   Fix: Real destination URLs for each link (remedy: fix-a11y)
6. **[Floor P0] A11-003 Visible focus everywhere** (1x). CTA 'SHOP THE AXIS PRO' and nav links  
   Evidence: focus.json: all six links rely on the UA 'auto 1px' outline; on the #1a1816 CTA button a 1px dark ring is not distinguishable (focus/03-on.png).  
   Fix: a:focus-visible { outline: 2px solid #d8482b; outline-offset: 3px } (remedy: fix-a11y)
7. **[Reflex P1] EML-101 Size email header art to the standard email width** (1x). whole email build  
   Evidence: dom-800.json: layout is divs/sections with CSS aspect-ratio, radial gradients, an @media query and an inline <svg> hero; no tables, no <img>. Gmail and Outlook strip SVG and most of this CSS, so the hero and layout will not render as captured.  
   Fix: Table-based 600px layout with inline styles and a hosted raster hero image (remedy: None)
8. **[Reflex P1] A11-002 Text size floors** (5x). body > div.frame > header.masthead > div.wordmark > span.est:nth-of-type(3)  "EST · 2024"  
   Evidence: label at 11px (label floor 12px; 6 such)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
9. **[Reflex P1] SLP-010 No template chrome glyphs** (3x). html > body > div.frame > section.article:nth-of-type(1) > div.eyebrow  "NEW · MAX-CUSHION TRAINER · EMBER FLARE"  
   Evidence: template chrome (middot-chains): "NEW · MAX-CUSHION TRAINER · EMBER FLARE"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
10. **[Reflex P1] A11-004 Target size** (3x). html > body > div.frame > section.article:nth-of-type(1) > a.cta  "Shop the Axis Pro"  
   Evidence: touch target 240x40px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
11. **[Reflex P1] SLP-007 No stock gradient pairs** (1x). html > body > div.frame > div.hero  
   Evidence: gradient 6 stops: #ffd6b8, #000000, #f59a6c, #000000, #c9c4b8  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
12. **[Reflex P1] CPY-004 Dash budget** (1x). whole page  
   Evidence: 4 em/spaced en dashes (budget 2)  
   Fix: Use a full stop, comma, colon or parentheses. (remedy: fix-copy)
13. **[Reflex P1] A11-001 Text contrast on real pixels** (1x). inline accent 'Ember Flare' in body copy  
   Evidence: Sweep measured #d8482b on #f4efe7 at 3.76:1; the italic accent is also the only signal it is a product name. Confirmed visible in tile 800-02.  
   Fix: Darken accent text to #b23a20 (>= 4.5:1) and keep italic (remedy: fix-a11y)
14. **[Reflex P1] IMG-121 Label any redraw "schematic" or "concept"** (1x). hero (800 tile 00, y 80-590)  
   Evidence: The product, the only reason for the email, is a hand-drawn inline SVG shoe (flat orange upper, five curved strokes, a white flash, a bracket for a sole) floating on a CSS radial-gradient glow. T-COVER-TEXT: with text hidden this reads as a generic shoe icon, not the Axis Pro in 'Ember Flare' and its 'painterly flame-knit upper' that the copy describes.  
   Fix: A real product photograph of the Ember Flare colourway as a hosted <img> at 600px email width with alt text [DATA NEEDED: product photography] (remedy: None)
15. **[Reflex P1] SLP-012 Look-family cluster** (1x). masthead, hero stamps, eyebrow, spec labels  
   Evidence: Warm-paper family tells the sweep could only partly measure: cream #f4efe7 page, terracotta #d8482b accent, italic accent words ('AXIS PRO.', 'Ember Flare'), and tracked mono caps with middot chains on every label: 'EST · 2024', '— SPORT TEST', '— EMBER FLARE', 'DROP 04 · 04—2026', 'NEW · MAX-CUSHION TRAINER · EMBER FLARE', 'SPECIFICATIONS · WOMEN'S'. T-DELETION: the three hero corner stamps and 'EST · 2024' carry no fact the reader needs.  
   Fix: Keep one label (the eyebrow, rewritten as a fact like 'Ships 4 April'); drop the stamps and EST badge (remedy: fix-quieter)

2 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- accent_footprint (CLR-001): not-verified: fold-800.png not captured
- flat_hierarchy (TYP-001): skipped: only 2 type roles
- dead_band (LAY-004): skipped: disabled by profile
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: no forms
- headings_landmarks (A11-007): skipped: disabled by profile
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Email-client accessibility (role="presentation" on layout tables, Outlook rendering) cannot be assessed from a browser capture.
- a11y: Sweep text-size hits on 11px mono labels agreed and not repeated.
- slop: Rendering in real email clients (only a browser capture exists); preheader text not present in the DOM capture.
