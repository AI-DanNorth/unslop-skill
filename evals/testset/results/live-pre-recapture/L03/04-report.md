# Unslop report: https://ai-stack-recommendat-7v45.bolt.host/

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (10x). div > section.relative.overflow-hidden:nth-of-type(1) > div.section.relative:nth-of-type(2) > div.mt-12.flex:nth-of-type(3) > span.flex.items-center:nth-of-type(1)  "20+ curated tools"  
   Evidence: 2.56:1 against the background behind the text (10th-percentile pixel #ffffff, worst 2.56:1; text #94a3b8, 12px; needs 4.5:1). APCA Lc 50 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-011 Reduced motion respected** (1x). main.flex-1 > div > section.relative.overflow-hidden:nth-of-type(1) > div.section.relative:nth-of-type(2) > div.inline-flex.items-center:nth-of-type(1)  "Personalized AI tool recommendations"  
   Evidence: page moves (keyframes fadeIn, scaleIn, slideDown) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
3. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 2145 characters (100% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
4. **[Floor P0] A11-112 Every control has an accessible name** (1x). Featured tools cards, 1440 tile 02  
   Evidence: Six links named only 'Details' (to #/tools/chatgpt, #/tools/claude, ...) and six buttons named only 'Add to compare' (dom-1440.json). The card is a div, not a list item or article, so there is no programmatically determined context tying each to its tool.  
   Fix: <a href="#/tools/chatgpt">Details<span class="sr-only"> about ChatGPT</span></a> and aria-label="Add ChatGPT to compare"; or wrap each card in <li>/<article aria-labelledby> with the h3 id. (remedy: None)
5. **[Floor P0] A11-126 Focus not obscured (AA): sticky headers, banners, chat widgets never fully cover the focus** (1x). fixed 'Made in Bolt' badge, bottom right at every width  
   Evidence: focus.json stops 14 ('Build a SaaS product') and 38 ('Details' on ElevenLabs) are covered; the badge sits over the last column of every grid in tiles 1440-00 and 375-00. The sweep flagged the two stops; the cause is the third-party badge, which has no visible dismiss persistence.  
   Fix: Remove the builder badge in production, or add scroll-padding-bottom equal to its height so focused items scroll clear. (remedy: None)
6. **[Floor P0] INT-005 No placeholder residue at ship** (1x). footer 'Connect' icons, 1440 tile 03  
   Evidence: Twitter, GitHub and LinkedIn icon links all have href="#" (dom-1440.json).  
   Fix: Link real profiles or remove the 'Connect' column: [DATA NEEDED: actual social URLs]. (remedy: fix-copy)
7. **[Reflex P1] SLP-222 Swap / rival's-name test: any head still true with a competitor's name (or the same trade ** (1x). hero, 1440 tile 00  
   Evidence: Failed T-RIVAL-NAME / T-MIRROR: 'Tell us the goal. We'll build the stack.' and 'Stop browsing endless directories... AI tools that actually fits your goal, budget, and skill level' stay true for any AI-tool recommender (Futurepedia, There's An AI For That quiz). The brand is literally the category name, 'AI Stack', with a stacked-layers glyph.  
   Fix: [DATA NEEDED: what this recommender knows or does that directories don't, e.g. who curates the 20 tools and on what test] stated in the head. (remedy: None)
8. **[Reflex P1] A11-004 Target size** (12x). div:nth-of-type(1) > div.min-h-screen.flex > header.sticky.top-0 > nav.section.flex > a.flex.items-center  
   Evidence: touch target 115x36px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
9. **[Reflex P1] SLP-003 No icon tiles above every card heading** (11x). div > section.section.py-16:nth-of-type(2) > div.grid.grid-cols-2:nth-of-type(2) > a.card.card-hover:nth-of-type(1) > div.w-10.h-10:nth-of-type(1)  
   Evidence: 40px tinted tile above heading "Study smarter" (10 repeats)  
   Fix: Remove the tiles, or use a real image or figure that differs per card. (remedy: fix-quieter)
10. **[Reflex P1] CPY-005 No slop diction** (11x). main.flex-1 > div > section.relative.overflow-hidden:nth-of-type(1) > div.section.relative:nth-of-type(2) > p.mt-5.text-lg  "Stop browsing endless directories. Answer three qu"  
   Evidence: "actually" (buzzwords/virtue-words, cap budget 2, found 5)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Reflex P1] A11-002 Text size floors** (7x). main.flex-1 > div > section.relative.overflow-hidden:nth-of-type(1) > div.section.relative:nth-of-type(2) > div.inline-flex.items-center:nth-of-type(1)  "Personalized AI tool recommendations"  
   Evidence: 36-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
12. **[Reflex P1] SLP-005 No uniform card kit** (2x). main.flex-1 > div > section.section.py-16:nth-of-type(2) > div.grid.grid-cols-2:nth-of-type(2) > a.card.card-hover:nth-of-type(1)  
   Evidence: 19 containers share radius 14px and shadow "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
13. **[Reflex P1] TYP-001 Clear type hierarchy** (2x). h3 vs h4  
   Evidence: h3 14px is only 1.00x h4 14px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)
14. **[Reflex P1] MOT-001 Motion CSS hygiene** (2x). .btn-primary  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
15. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (1x). main.flex-1 > div > section.section.pb-20:nth-of-type(5) > div.rounded-2xl.bg-ink-900 > div.absolute.inset-0:nth-of-type(1)  
   Evidence: radial spotlight #3b82f6 alpha 0.15  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)

12 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Keyboard operation of the mobile menu and the quiz flow (no live session).
- a11y: Forms and errors: no forms on the captured route.
- a11y: disputed: none of the sampled sweep Floor hits (12px #94a3b8 trust chips 2.56:1, 'GP' white on #10a37f 3.20:1) look like false positives; the 'GP' avatars are decorative initials beside the real name and could be aria-hidden, which would remove them from scope.
- a11y: Text spacing override (1.4.12) not injected.
- slop: The 'Find My Stack' quiz flow and result page (only the home route was captured).
- slop: Whether prices are current: '₹1,650 mo' may be accurate conversions; not verified.
