# Unslop report: https://skill-huasheng.vercel.app/slides/slide-03b-deepseek-cover.html

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (13x). html > body > div.stage > div.chapter:nth-of-type(1)  "IN PRACTICE"  
   Evidence: 2.65:1 against the background behind the text (10th-percentile pixel #0a0a0a, worst 2.64:1; text #5c5447, 13px; needs 4.5:1). APCA Lc 16 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-002 Text size floors** (8x). html > body > div.stage > div.meta:nth-of-type(2)  "SCENE · DEEPSEEK V4COVER FOR WECHAT"  
   Evidence: 35-character run at 12px (hard floor 18px, dense UI 20px, body 24px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
3. **[Floor P0] A11-011 Reduced motion respected** (2x). stylesheet  
   Evidence: page animates (keyframes or transform transitions) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
4. **[Floor P0] A11-171 Muted text on brand bands / effects / photos.** (1x). right-panel step glosses and left-panel muted text  
   Evidence: Confirms sweep A11-001 by eye on tile 1920-00: grey-brown italic glosses ('Midjourney / DALL·E / SDXL', '没风格、没受众、没视角', 'Pentagram / Takram / Build') at 13px sit at about 2.6:1 on #0a0a0a; on a projector with ambient light these disappear. They carry content (what the generic agent skipped), not decoration.  
   Fix: Raise to at least #a39a8a (about 7:1) and 20px+ on a 1920 canvas, or cut the glosses (remedy: None)
5. **[Floor P0] A11-110 Keep all words as real text in reading order** (1x). three output thumbnails  
   Evidence: dom-1920.json: alt texts are 'Pentagram · DeepSeek V4', 'Takram · DeepSeek V4', 'Build · DeepSeek V4'. They name the school but not what each cover shows, and the thumbnails' own text ('几乎贴近前沿，价格只是零头。', '深度求索 V4 在百万 token 中思考。') is unreadable at 320px and absent from the alt.  
   Fix: alt="Takram direction: warm paper cover, headline '深度求索 V4 在百万 token 中思考', triangle diagram, quiet serif" (remedy: None)
6. **[Reflex P1] SLP-012 Look-family cluster** (1x). whole slide  
   Evidence: Near-black #0a0a0a ground, Source Serif display with gold italic emphasis ('帮我做个公众号头图', 'huashu-design 启动后'), IBM Plex Mono tracked labels, hairline dividers and a centred 'VS' rule, numbered 1-5 step list, folio '02B / 09'. This is the hairline-newspaper family transposed to dark (serif + italic + mono labels + hairlines). T-MIRROR: a different talk on a different tool would get the same chrome.  
   Fix: If this is the speaker's deliberate deck identity, record it in the brief; otherwise drop the mono chrome and let the serif headline and images carry the slide (remedy: fix-quieter)
7. **[Reflex P1] SLP-010 No template chrome glyphs** (5x). html > body > div.stage > div.compare:nth-of-type(4) > div.panel:nth-of-type(1)  
   Evidence: template chrome (middot-chains): "A 通用 AI / Agent DEFAULT → 收到 prompt，直接调图模型Midjourney / DALL·"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
8. **[Reflex P1] A11-002 Text size floors** (4x). html > body > div.stage > div.takeaway:nth-of-type(5) > span:nth-of-type(1)  "普通 AI：给你 。：给你 —— 然后你选。这就是「装进 AI 的工作流」做的事。"  
   Evidence: 41-character run at 18px (hard floor 18px, dense UI 20px, body 24px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
9. **[Reflex P1] CPY-005 No slop diction** (3x). div.output:nth-of-type(3) > div.triplet:nth-of-type(2) > div.ccard:nth-of-type(2) > div.cname:nth-of-type(2) > span.school  "EAST · QUIET"  
   Evidence: "QUIET" (buzzwords/virtue-words, cap budget 2, found 3)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
10. **[Reflex P1] TYP-002 Sizes on a declared ladder** (2x). whole page  
   Evidence: 14 distinct font sizes: 9, 10, 11, 12, 13, 14, 15, 17, 18, 24, 30, 38, 54, 74 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
11. **[Reflex P1] SLP-007 No stock gradient pairs** (1x). #slop  
   Evidence: gradient 4 stops + hue span 59° + banned pair (hues 265-330 with 331-25): #1a0c2e, #3b1a5a, #7c2d9c, #c9447b  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
12. **[Reflex P1] CLR-001 Accent footprint within budget** (1x). first screen at 1920px  
   Evidence: saturated accent covers 8.1% of the fold (fail > 8%)  
   Fix: Keep accent on the primary action, current state and one focal element. (remedy: fix-colorize)
13. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). div.slop.show:nth-of-type(2) > div.text:nth-of-type(1) > div.big:nth-of-type(1)  "DeepSeek"  
   Evidence: display text at 54px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
14. **[Reflex P1] CPY-004 Dash budget** (1x). whole page  
   Evidence: 4 em/spaced en dashes (budget 2)  
   Fix: Use a full stop, comma, colon or parentheses. (remedy: fix-copy)
15. **[Reflex P1] ROB-001 Content never depends on animation to appear** (1x). page after load  
   Evidence: 42% of text is hidden after load and scrolling (max 30%; menus and dialogs excluded)  
   Fix: Start visible; animate from visible. (remedy: fix-harden)

6 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 0 type roles
- dead_band (LAY-004): skipped: disabled by profile
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: disabled by profile
- focus_ring (A11-003): skipped: disabled by profile
- targets (A11-004): skipped: disabled by profile
- headings_landmarks (A11-007): skipped: disabled by profile
- phone_parity (ROB-002): skipped: disabled by profile
- overflow (ROB-003): skipped: disabled by profile
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: fixed-canvas slide: reflow (1.4.10) and target size not applicable
- a11y: the purple exhibit cover's low-contrast caption is part of a quoted counter-example and was not scored
- a11y: keyboard navigation between slides: only one slide captured
- slop: the step-by-step reveal animation and REPLAY behaviour (captured after an 8s wait, final state only)
- slop: other slides of the deck (T-GHOST-DECK needs the full title run; only slide 02B was captured)
- slop: no 00-contract.md brief: cannot tell whether the dark editorial look is the presenter's established identity
