# Unslop report: https://diagramdesign.dev/

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
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). observer_never_fires  
   Evidence: 545 characters (7% of text) stay invisible when IntersectionObserver never fires  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
2. **[Floor P0] A11-006 Controls have accessible names** (1x). Install section, 7 copy cards  
   Evidence: Seven controls are labelled only "COPY" (sweep repeated_label: 'Copy' x7); out of context a screen-reader list reads 'Copy, Copy, Copy...'. Instruction says 'CLICK ANY CARD TO COPY' with no confirmation text captured.  
   Fix: <button aria-label="Copy Claude Code install commands">Copy</button> plus a polite live region announcing 'Copied' (remedy: fix-a11y)
3. **[Floor P0] A11-003 Visible focus everywhere** (1x). 'AXONOMETRIC PLAN FIG. 04B ENLARGE' button  
   Evidence: Sweep focus_ring: focused element covered by the fixed header. focus.json confirms covered=true at y 3528 while the neighbouring FIG. 04A button is not covered.  
   Fix: html { scroll-padding-top: <header height> } so focused targets scroll clear of the bar (remedy: fix-a11y)
4. **[Reflex P1] SLP-010 No template chrome glyphs** (11x). section.hero:nth-of-type(1) > div.wrap > div.titleblock.rise:nth-of-type(1) > div:nth-of-type(2) > b  "Claude Code · Codex · Pi"  
   Evidence: template chrome (middot-chains): "Claude Code · Codex · Pi"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
5. **[Reflex P1] A11-002 Text size floors** (6x). header.bar > div.wrap.bar-in > a.brand:nth-of-type(1) > span > span.sub  "diagramdesign.dev"  
   Evidence: label at 10px (label floor 11px; 25 such)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
6. **[Reflex P1] WEB-001 Performance budget** (4x). https://diagramdesign.dev/assets/gallery/exploded.webp  
   Evidence: image is 2400px wide but shown at 553px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
7. **[Reflex P1] SLP-012 Look-family cluster** (3x). whole page  
   Evidence: warm-paper-serif: 4 of 6 tells (terracotta_accent (#bf4520); serif_display (Instrument Serif); italic_serif_hero (italic serif headline); eyebrows (154 tracked caps labels)); cluster minimum 3  
   Fix: Break the family on its strongest tell first; name the replacement decision. (remedy: fix-quieter)
8. **[Reflex P1] SLP-006 Vary container recipes** (2x). section.hero:nth-of-type(1) > div.wrap > div.hero-grid:nth-of-type(2) > div > div.proof.rise:nth-of-type(3)  
   Evidence: one box recipe on 7 elements across 4 selectors (div.proof.rise, div.spec.rise, div.stamp-block, ul.deltas.rise)  
   Fix: Differentiate by role: section, object, callout, well. (remedy: fix-layout)
9. **[Reflex P1] TYP-002 Sizes on a declared ladder** (2x). whole page  
   Evidence: 19 distinct font sizes: 9, 9.5, 10, 10.5, 11, 12, 12.5, 13, 14, 15, 16, 16.5, 17, 19, 22, 24, 30.5, 48, 80 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
10. **[Reflex P1] CPY-006 No repeated labels inside a card** (2x). section:nth-of-type(7) > div.wrap > div.sheets:nth-of-type(2)  
   Evidence: "Copy" repeated 7 times in one container  
   Fix: Say it once. (remedy: fix-copy)
11. **[Reflex P1] A11-006 Controls have accessible names** (2x). header theme toggle, tile 00  
   Evidence: The theme switch is one button named 'DARK LIGHT' with the active option shown only by a black fill on 'LIGHT'.  
   Fix: <button aria-pressed="false" aria-label="Dark theme">…</button>, or a two-option radiogroup with aria-checked (remedy: fix-a11y)
12. **[Reflex P1] SLP-001 No eyebrow labels above headings** (1x). whole page, mono labels  
   Evidence: Sweep counts 154 tracked caps labels and 198 mono labels: 'FIG. 00 · THE SKILL AT WORK', '17S · NO SOUND', 'FIG. 02A / FIRST PASS · NO SKILL', '45 TYPES · 6 AGENTS · 0 BUILD STEPS', section sub-lines like 'IT RUNS INSIDE THE AGENT YOU ALREADY USE. NOTHING NEW TO OPEN, NOTHING TO EXPORT.' set as caps mono.  
   Fix: Keep FIG. numbers where a figure is referenced; set the section sub-lines and the quote attribution in sentence-case body type (remedy: fix-typeset)
13. **[Reflex P1] SLP-005 No uniform card kit** (1x). 'What you get' section  
   Evidence: Six equal feature blocks ('45 visual types', 'Brand-matched in ~60s', 'Self-contained HTML + SVG', 'Imports draw.io, Mermaid & Excalidraw', 'Optional accessible motion', 'Accessible by default') plus a three-up benefit row ('One accent, not six.', 'Real hierarchy.', 'Structure you can read.') in fragment-period style.  
   Fix: Annotate the before/after figure directly with these three points (callouts on FIG. 02B) and drop the separate three-up row (remedy: fix-layout)
14. **[Reflex P2] A11-003 Visible focus everywhere** (1x). button "AXONOMETRIC PLAN
FIG. 04B
ENLARGE"  
   Evidence: focused element is partly hidden by a fixed or sticky element (WCAG 2.4.12)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
15. **[Finish P3] A11-002 Text size floors** (7x). section:nth-of-type(3) > div.wrap > div.sec-head:nth-of-type(1) > p.note.rise  "Same content, two passes: Claude on its own, then "  
   Evidence: 72-character run at 11px (hard floor 9px, dense UI 11px, body 12px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)

2 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- accent_footprint (CLR-001): skipped: disabled by profile
- dead_band (LAY-004): skipped: disabled by profile
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: disabled by profile
- targets (A11-004): skipped: disabled by profile
- headings_landmarks (A11-007): skipped: disabled by profile
- phone_parity (ROB-002): skipped: disabled by profile
- overflow (ROB-003): skipped: disabled by profile
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. media https://diagramdesign.dev/assets/demo-light.mp4
- a11y: Gallery thumbnails lazy-loaded and not rendered at capture; their in-place contrast not checked.
- a11y: Demo video blocked; captions/controls for FIG. 00 unverified (it says '17S · NO SOUND').
- a11y: Animated axonometric examples (separate pages) and the enlarge dialog's Escape/focus return not tested live.
- slop: Gallery thumbnails (01-45) render blank: images are loading=lazy and were not loaded at capture (complete=false, natural width 0). Not judged as design.
- slop: Demo video (demo-light.mp4) blocked in capture; FIG. 00 not judged.
- slop: Medium recorded as diagram, but the artifact is a landing page for a diagram tool; judged as web.
