# Unslop report: https://v0-optimus-delta.vercel.app

**Verdict (draft): fix**. Profile: balanced. 9 Floor finding(s) open.

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (17x). div.jsx-d0fb98a0b853be6f.grid:nth-of-type(2) > div.jsx-d0fb98a0b853be6f.space-y-0:nth-of-type(1) > button.jsx-d0fb98a0b853be6f.w-full:nth-of-type(2) > div.jsx-d0fb98a0b853be6f.flex > span.jsx-d0fb98a0b853be6f.font-display  "II"  
   Evidence: 1.30:1 against the background behind the text (10th-percentile pixel #090603, worst 1.30:1; text #fafaf8, opacity 0.12, 30px; needs 3.0:1). APCA Lc 0 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] INT-001 No invented metrics** (7x). div.max-w-7xl.mx-auto:nth-of-type(1) > div.grid.lg\:grid-cols-12:nth-of-type(2) > div.lg\:col-span-4.flex:nth-of-type(2) > div.p-8.border:nth-of-type(1) > p.font-display.text-3xl  "99.99% uptime"  
   Evidence: "99.99% uptime" (invented-metrics/percent-claims, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
3. **[Floor P0] A11-006 Controls have accessible names** (6x). div.max-w-7xl.mx-auto:nth-of-type(1) > div.grid.lg\:grid-cols-12:nth-of-type(2) > div.lg\:col-span-4.flex:nth-of-type(2) > div.flex.gap-2:nth-of-type(2) > button.h-2.transition-all:nth-of-type(1)  
   Evidence: button[type=submit] has no accessible name  
   Fix: Add visible text or aria-label. (remedy: fix-a11y)
4. **[Floor P0] TYP-004 The intended font actually renders** (4x). div.flex.gap-16 > div.flex.gap-16:nth-of-type(1) > div.flex.items-baseline:nth-of-type(1) > span.text-sm.text-muted-foreground:nth-of-type(2) > span.block.font-mono  "NETFLIX"  
   Evidence: declared "JetBrains Mono" but Instrument Sans drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
5. **[Floor P0] A11-004 Target size** (2x). div.max-w-7xl.mx-auto:nth-of-type(1) > div.grid.lg\:grid-cols-12:nth-of-type(2) > div.lg\:col-span-4.flex:nth-of-type(2) > div.flex.gap-2:nth-of-type(2) > button.h-2.transition-all:nth-of-type(1)  
   Evidence: target 8x8px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
6. **[Floor P0] A11-011 Reduced motion respected** (2x). h1.text-\[clamp\(3rem\,12vw\,10rem\)\].font-display > span.block:nth-of-type(2) > span.relative.inline-block > span.inline-flex:nth-of-type(1) > span.inline-block.animate-char-in:nth-of-type(1)  "b"  
   Evidence: page moves (keyframes char-in, devLineReveal, enter) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
7. **[Floor P0] ROB-001 Content never depends on animation to appear** (2x). observer_never_fires  
   Evidence: 2085 characters (42% of text) stay invisible when IntersectionObserver never fires  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
8. **[Floor P0] A11-007 Headings and landmarks** (1x). hero h1  
   Evidence: dom-1440 records the h1 with empty text; bodyText shows the rotating word split into one span per letter ('to c r e a t e'), while the tile shows 'to build'. Screen readers may read single letters or a word that changes under them.  
   Fix: <h1>The platform to <span class="sr-only">build</span><span aria-hidden="true">(animated letters)</span></h1> (remedy: fix-a11y)
9. **[Floor P0] INT-003 No fake people or hotlinked stock** (1x). hero stat marquee and testimonial, 1440 tiles 00 and 08  
   Evidence: Stats credited to real companies with no source: '20 days saved on builds NETFLIX', '98% faster deployment STRIPE', '300% throughput increase LINEAR', '6x faster to ship NOTION'; testimonial 'Optimus transformed our deployment pipeline...' from 'Sarah Chen, CTO, Meridian Labs' with 'KEY RESULT 10x faster deployments'.  
   Fix: [DATA NEEDED: a real customer, a measured result and permission to name them], or remove the marquee and the testimonial (remedy: fix-harden)
10. **[Reflex P1] CPY-005 No slop diction** (22x). div.group.relative:nth-of-type(3) > div.flex.flex-col > div.flex-1.grid:nth-of-type(2) > div:nth-of-type(1) > p.text-lg.text-muted-foreground  "Work together seamlessly. Live preview, instant fe"  
   Evidence: "seamlessly" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Reflex P1] A11-004 Target size** (11x). main.relative.min-h-screen > header.fixed.z-50 > nav.mx-auto.transition-all > div.flex.items-center > a.flex.items-center  
   Evidence: touch target 114x32px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
12. **[Reflex P1] MOT-001 Motion CSS hygiene** (7x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
13. **[Reflex P1] SLP-010 No template chrome glyphs** (5x). div:nth-of-type(2) > div.group.relative:nth-of-type(1) > div.flex.flex-col > div.shrink-0:nth-of-type(1) > span.font-mono.text-sm  "01"  
   Evidence: template chrome (numbering-tokens): "01"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
14. **[Reflex P1] SLP-002 No decorative section numbering** (4x). div.max-w-7xl.mx-auto > div.grid.md\:grid-cols-3:nth-of-type(3) > div.relative.p-8:nth-of-type(1) > div.mb-8:nth-of-type(1) > span.font-mono.text-xs  "01"  
   Evidence: section number "01" (12px) beside heading "Starter"; 3 on page  
   Fix: Remove the numbers or make them real steps. (remedy: fix-typeset)
15. **[Reflex P1] LAY-004 No dead bands** (4x). y 1124-1303 at 1280px  
   Evidence: 179px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)

14 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://v0-optimus-delta.vercel.app/_next/static/chunks/4ee6091cb6e16beb.js
- a11y: Mobile menu and testimonial carousel keyboard behaviour: no live keyboard test.
- a11y: Several sections render blank in the capture (sweep hidden_content: 40% of text hidden after load); their contents were not checked visually.
- a11y: One script chunk was blocked (manifest network); some states may differ from a full load.
- slop: Several sections render as empty bands in the capture (dead_band / hidden_content in the sweep): judged on DOM text where tiles were blank.
- slop: One script chunk was blocked (manifest network); some animated content may be missing for that reason, not by design.
