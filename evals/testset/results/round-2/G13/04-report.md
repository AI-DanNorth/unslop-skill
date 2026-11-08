# Unslop report: /home/claude/refs/diagram-design/skills/diagram-design/assets/example-architecture.html

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

1. **[Floor P0] A11-002 Text size floors** (1x). svg labels 'CONTENT' (7px), 'HTTPS', 'RESP', 'SSR', 'READ MDX', 'QUERY' (8px), legend text (8.5px)  
   Evidence: Verified sweep hits in tile 1440-00: the arrow labels that name each connection are the smallest text in the diagram, and 'RESP' is partly overlapped by the dashed return arrow head.  
   Fix: >= 12px for edge labels and legend (scale svg text, not the page) (remedy: fix-typeset)
2. **[Floor P0] A11-001 Text contrast on real pixels** (1x). 'Cloud' node fill and 'Store' vs 'Cloud' legend swatches; Cloudflare node border  
   Evidence: The Cloudflare node uses a ~#e8e8e8 fill and light grey border on the #f4f4f4 page; the 'Store' and 'Cloud' swatches differ only by a faint fill, well under 3:1 against each other and the page.  
   Fix: Border >= #8a8f99 (3:1) and a distinct pattern or label for cloud vs store (remedy: fix-a11y)
3. **[Reflex P1] A11-002 Text size floors** (5x). html > body > div.frame > p.eyebrow  "Architecture · Diagram Design"  
   Evidence: label at 11px (label floor 11px; 26 such)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
4. **[Reflex P1] A11-007 Headings and landmarks** (1x). page structure  
   Evidence: No <main> landmark (landmarks all 0). The svg does include <title> 'Content site in production' and a good <desc>, but whether it is exposed (role="img" with aria-labelledby) is not recorded in the capture.  
   Fix: <main><figure><svg role="img" aria-labelledby="t d">...</svg></figure></main> (remedy: fix-a11y)
5. **[Reflex P1] SLP-002 No decorative section numbering** (1x). Cloudflare node ('01') and Astro Origin node ('02')  
   Evidence: 32px pale mono watermarks '01' and '02' sit in the bottom-right of two nodes and overlap the sub-labels ('cache' runs into '01', 'MDX' into '02') in tile 1440-00. T-DELETION: removing them loses nothing; only two of five nodes are numbered and the order is already shown by arrows.  
   Fix: Delete both watermarks (remedy: fix-typeset)
6. **[Reflex P2] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 3 font families render: Geist Mono, Instrument Serif, Geist  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
7. **[Finish P3] DVZ-101 Draw a diagram only if it out-teaches a paragraph** (1x). whole diagram  
   Evidence: T-DIAGRAM-EARNS is borderline: five nodes in one chain with a fork ('Reader -> Cloudflare -> Astro Origin, which reads the MDX bundle and queries the CMS') fit in one sentence, and the svg's own <desc> says exactly that. The diagram earns its place only if it shows what prose cannot (cache hit vs miss, build-time vs request-time reads).  
   Fix: Show the cache-hit return from Cloudflare and mark whether 'READ MDX' happens at build or per request [DATA NEEDED: build vs runtime read] (remedy: None)
8. **[Finish P3] SLP-010 No template chrome glyphs** (1x). node tag chips 'EXT', 'EDGE', 'ORIG', 'BUN', 'CMS' and the 'CONTENT' group label  
   Evidence: Each node carries a 7-8px mono chip repeating its type or name ('CMS' above 'Content CMS'); types are also given by fill in the 8-item legend. T-LABEL-TRANSFORM: the chips add no fact the node title or legend does not.  
   Fix: Drop the chips (or the legend's node-type rows) so each fact appears once; legend keeps only arrow meanings (remedy: fix-copy)
9. **[Finish P3] LAY-004 No dead bands** (1x). y ~190-350 and y ~780-900 at 1440  
   Evidence: The diagram occupies a 230px-tall strip; ~160px of empty dotted grid separates the title from the first node and the svg is 576px tall for a 300px drawing.  
   Fix: Crop the viewBox to the drawing plus margin so the title sits with the diagram (remedy: fix-layout)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- accent_footprint (CLR-001): skipped: disabled by profile
- flat_hierarchy (TYP-001): skipped: only 1 type roles
- spacing_monotony (LAY-001): skipped: only 2 spacing values
- dead_band (LAY-004): skipped: disabled by profile
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: disabled by profile
- focus_ring (A11-003): skipped: page has no interactive controls
- targets (A11-004): skipped: disabled by profile
- headings_landmarks (A11-007): skipped: disabled by profile
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- phone_parity (ROB-002): skipped: disabled by profile
- overflow (ROB-003): skipped: disabled by profile
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: sweep A11-003 'Tab reached no focusable element' is not a failure; the diagram has no controls.
- a11y: Reflow at 375 not captured for this item (only 1440 evidence).
- slop: Correctness of the architecture itself (whether MDX is read at runtime) not verifiable from the artifact.
