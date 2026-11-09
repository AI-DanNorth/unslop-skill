# Unslop report: https://cal.com

**Verdict (draft): fix**. Profile: balanced. 8 Floor finding(s) open.

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
| Integrity | 1 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-001 No invented metrics** (6x). section.page-measure.section-y:nth-of-type(3) > div.\[--row\:60px\] > div.grid.grid-cols-2 > div.grid.gap-10 > p.m-0.text-sm  "spends 35% less time scheduling across support, sa"  
   Evidence: "35% less" (invented-metrics/percent-claims, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
2. **[Floor P0] A11-001 Text contrast on real pixels** (5x). div.relative.size-full > div.flex.h-full:nth-of-type(1) > div.px-5.pt-\[30px\]:nth-of-type(2) > div.mt-\[22px\].grid:nth-of-type(2) > span.relative.grid:nth-of-type(33)  "22"  
   Evidence: 1.00:1 against the background behind the text (10th-percentile pixel #ffffff, worst 1.00:1; text #ffffff, 14px; needs 4.5:1). APCA Lc 0 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] A11-003 Visible focus everywhere** (3x). button "Products"  
   Evidence: no visible focus indicator (outline: none 1px oklab(0.713655 -0.00286007 -0.0189416 / 0.5))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
4. **[Floor P0] ROB-001 Content never depends on animation to appear** (2x). observer_never_fires  
   Evidence: 3979 characters (50% of text) stay invisible when IntersectionObserver never fires  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
5. **[Floor P0] A11-006 Controls have accessible names** (2x). header logo link (first focus stop)  
   Evidence: focus.json stop 0: <a href="/"> with empty accessible name; the logo inside has no exposed text in the link name.  
   Fix: <a href="/" aria-label="Cal.com home"> (remedy: fix-a11y)
6. **[Floor P0] TYP-004 The intended font actually renders** (1x). div.ml-2.flex:nth-of-type(2) > nav.hidden.lg\:block > ul.relative.isolate > li:nth-of-type(2) > button.flex.h-9  "Products"  
   Evidence: declared "calSans" but Cal Sans drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
7. **[Floor P0] INT-005 No placeholder residue at ship** (1x). article.relative.flex:nth-of-type(5) > div.relative.grid:nth-of-type(1) > div.grid.w-\[calc\(100\%-40px\)\] > pre.m-0.grid > span:nth-of-type(4)  "config={{ layout: }}/>"  
   Evidence: "{{ layout: }}" (self-labels/residue, fail)  
   Fix: Fill with real content or a visible [DATA NEEDED] slot. (remedy: fix-copy)
8. **[Floor P0] A11-010 Form fields have labels** (1x). #faq-ask  
   Evidence: input[type=text] has no label (placeholder "Ask anything else" is not a label)  
   Fix: Add a visible label element. (remedy: fix-a11y)
9. **[Reflex P1] WEB-001 Performance budget** (34x). ng/hero/google-icon.svg?dpl=dpl_2HvtP5Myu84H8zR7pimFfQQLAxrK  
   Evidence: image is 100px wide but shown at 20px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
10. **[Reflex P1] CPY-005 No slop diction** (22x). button.flex.flex-1 > span.grid.min-w-0:nth-of-type(2) > span.font-display.text-2xl:nth-of-type(2)  "Kiaora runs mission-critical healthcare scheduling"  
   Evidence: "mission-critical" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (17x). :root --color-ring  
   Evidence: token --color-ring: #9ca3af is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)
12. **[Reflex P1] A11-004 Target size** (12x). div.contents:nth-of-type(2) > nav.sticky.top-2 > div.flex.shrink-0:nth-of-type(1) > span.inline-flex > a.flex.shrink-0  
   Evidence: touch target 101x22px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
13. **[Reflex P1] SLP-005 No uniform card kit** (8x). body.bg-\(--page-surface\).text-foreground > div.contents:nth-of-type(2) > nav.sticky.top-2 > div.flex.shrink-0:nth-of-type(3) > a.relative.inline-flex:nth-of-type(3)  "Get started"  
   Evidence: 6 containers share radius 12px and shadow "oklab(0.999994 0.0000455678 0.0000200868 / 0.16) 0px 1px 0px"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
14. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
15. **[Reflex P1] A11-002 Text size floors** (7x). div.hp-window.\@container > div.shrink-0.flex-col:nth-of-type(1) > div.flex.h-\[38px\]:nth-of-type(1) > span.relative.flex:nth-of-type(2) > span.min-w-0.flex-1  "Get Rickrolled | Rick Astley"  
   Evidence: 28-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)

20 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 16 other request(s) blocked, e.g. script https://cal.com/1100e7f5c1bf1a7d/script.js
- a11y: Scripts and two fonts were blocked in capture; menus (Products, Use cases) and the FAQ 'Ask anything else' input not exercised live.
- a11y: Broken images in capture not assessed for alt beyond what the DOM shows.
- a11y: Sweep 'no visible focus' hits on nav buttons look plausible (outline: none) but were not re-checked against crops.
- slop: Several images render as broken or beige placeholders (avatars, Salesforce and Google Meet icons, case-study video area, events demo): capture blocked scripts and two fonts (manifest network), so these are not judged as design.
- slop: Animated hero chips and tab auto-advance seen as stills only.
