# Unslop report: https://ai-stack-techaffiliate.base44.app/

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
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-003 Visible focus everywhere** (6x). a "Build a website
Plan, build and launch a site"  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
2. **[Floor P0] A11-001 Text contrast on real pixels** (5x). main.flex-1 > section.container-page.mt-28:nth-of-type(3) > div.mt-10.grid > div.bg-card.p-7:nth-of-type(1) > span.font-mono.text-sm  "01"  
   Evidence: 3.75:1 against the background behind the text (10th-percentile pixel #ffffff, worst 3.75:1; text #ee491b, 14px; needs 4.5:1). APCA Lc 64 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] A11-006 Controls have accessible names** (2x). THE DIRECTORY tool cards, 1440 tile 03  
   Evidence: Six buttons whose accessible name is only 'Compare' (dom-1440 buttons after h3 Claude, Perplexity, NotebookLM, ElevenLabs, Lovable, Gamma); a screen-reader button list gives six identical 'Compare' entries.  
   Fix: <button aria-label="Add Claude to compare">+ Compare</button> (keep the visible word 'Compare' at the start of the name for 2.5.3) (remedy: fix-a11y)
4. **[Floor P0] A11-002 Text size floors** (1x). div.flex.min-h-screen:nth-of-type(1) > main.flex-1 > section.container-page.pt-14:nth-of-type(1) > div > p.eyebrow.flex:nth-of-type(1)  "AI tool stacks, not directories"  
   Evidence: 31-character run at 11px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
5. **[Floor P0] A11-011 Reduced motion respected** (1x). stylesheet  
   Evidence: page animates (keyframes or transform transitions) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
6. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 2766 characters (100% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
7. **[Reflex P1] SLP-002 No decorative section numbering** (1x). How it works band, tile 1440-01  
   Evidence: Orange mono '01', '02', '03' over 'Share your goal', 'Set budget and skill', 'Get your workflow' in three equal cells.  
   Fix: Delete the band; the 'Question 1 of 3' picker already demonstrates the steps. (remedy: fix-typeset)
8. **[Reflex P1] A11-004 Target size** (11x). div:nth-of-type(1) > div.flex.min-h-screen:nth-of-type(1) > header.sticky.top-0 > div.container-page.flex > a.group.flex  
   Evidence: touch target 106x32px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
9. **[Reflex P1] SLP-010 No template chrome glyphs** (10x). main.flex-1 > section.container-page.mt-28:nth-of-type(3) > div.mt-10.grid > div.bg-card.p-7:nth-of-type(1) > span.font-mono.text-sm  "01"  
   Evidence: template chrome (numbering-tokens): "01"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
10. **[Reflex P1] A11-002 Text size floors** (9x). section.container-page.mt-16:nth-of-type(2) > div.mt-8.grid:nth-of-type(2) > div:nth-of-type(1) > a.group.flex > span.mt-1.hidden:nth-of-type(3)  "Research, notes and revision that stick"  
   Evidence: 39-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
11. **[Reflex P1] SLP-001 No eyebrow labels above headings** (7x). div.flex.min-h-screen:nth-of-type(1) > main.flex-1 > section.container-page.pt-14:nth-of-type(1) > div > p.eyebrow.flex:nth-of-type(1)  "AI tool stacks, not directories"  
   Evidence: 11px label tracked 0.14em caps above 84px heading "Tell us the goal."; 6 on page, budget 2  
   Fix: Promote the fact into the heading or delete the label (T-EYEBROW). (remedy: fix-typeset)
12. **[Reflex P1] MOT-001 Motion CSS hygiene** (6x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
13. **[Reflex P1] TYP-002 Sizes on a declared ladder** (2x). whole page  
   Evidence: 10 distinct font sizes: 11, 12, 14, 16, 17, 18, 20, 36, 48, 84 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
14. **[Reflex P1] CPY-006 No repeated labels inside a card** (2x). div:nth-of-type(1) > div.flex.min-h-screen:nth-of-type(1) > main.flex-1 > section.container-page.mt-28:nth-of-type(4)  
   Evidence: "See full stack" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
15. **[Reflex P1] WEB-001 Performance budget** (2x). ia.base44.com/images/public/builder-assets/symbol-orange.png  
   Evidence: image is 512px wide but shown at 20px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)

11 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: A11-001 contrast 1.15:1 on 'Build a SaaS product' (text #171412 over a #000000 sample) is most likely the fixed black Base44 badge sampled behind the card; the card itself is white.
- a11y: Keyboard operation of the mobile menu and the /find question flow: no live keyboard test run.
- a11y: Forms and error handling: no forms on the home page (forms.json).
- a11y: Text spacing override (1.4.12) not injected.
- slop: Result pages (/results, /find): only the home page was captured.
- slop: The 'Edit with Base44' badge is platform chrome, not judged as design.
