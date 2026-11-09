# Unslop report: https://ai-stack-gold.vercel.app/

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
| Integrity | 6 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-001 No invented metrics** (1x). section.relative.overflow-hidden:nth-of-type(1) > div.mx-auto.grid > div:nth-of-type(1) > div.mt-12.flex:nth-of-type(3) > span  "Trusted by 12,000+ curious builders"  
   Evidence: "Trusted by 12,000+" (invented-metrics/social-proof-counts, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
2. **[Floor P0] A11-112 Every control has an accessible name** (1x). header, mobile menu button at 375px (x 335, y 22, 20x20)  
   Evidence: dom-375.json: the only visible header control besides 'Get started' is a <button> whose text and accessible name are both empty (an icon-only hamburger). The sweep's control_names did not flag it.  
   Fix: <button class="md:hidden" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav"> (remedy: None)
3. **[Floor P0] A11-121 Every function is operable by keyboard** (1x). header nav: 'Find my stack', 'AI tools', 'Compare', 'About', 'Sign in'  
   Evidence: dom-1440.json: all five nav items are <button> elements with href null inside <nav>; none is a link. They cannot be opened in a new tab and are announced as buttons, not navigation.  
   Fix: <nav aria-label="Main"><a href="/tools">AI tools</a>… (real URLs for each destination) (remedy: None)
4. **[Floor P0] A11-003 Visible focus everywhere** (1x). primary CTA 'Find my AI stack' (focus/06-on.png)  
   Evidence: Focus crop shows the blue button with only a faint 1px light-grey auto outline at 50% alpha against the light page; on the #1d4ed8 fill the ring is nearly invisible. Confirms the sweep's 1.52:1 change ratio for buttons.  
   Fix: button:focus-visible { outline: 2px solid #1d4ed8; outline-offset: 2px } (remedy: fix-a11y)
5. **[Floor P0] INT-003 No fake people or hotlinked stock** (1x). hero, under the buttons  
   Evidence: Coloured initial avatars 'A', 'S', 'M', 'J' stacked next to the count: placeholder faces standing in for people. (The '12,000+' count itself is a sweep hit.)  
   Fix: Remove the avatar stack; show real users only with consent [DATA NEEDED: real user count and source] (remedy: fix-harden)
6. **[Reflex P1] SLP-012 Look-family cluster** (2x). hero, 1440px tile 00  
   Evidence: Failed T-DEFAULT-AGENT: pill badge with sparkle icon 'A better way to discover AI', h1 'Stop searching. / Start building.' with the second line coloured #1d4ed8, primary + ghost button pair, overlapping initial avatars 'A S M J', and a floating mock card on the right. Every element is the stock v0/shadcn landing hero; dom meta generator is 'v0.app'.  
   Fix: A hero built around the actual job: e.g. the goal picker itself (goal, budget, comfort level) live in the first screen, so the visitor starts using it instead of reading about it (remedy: fix-quieter)
7. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). whole page  
   Evidence: Page is 1228px tall at 1440: hero plus one three-card section, no footer, no tool list, no pricing, no about. Nav items 'AI tools', 'Compare', 'About' are <button>s with no href.  
   Fix: [DATA NEEDED: real tool catalogue, comparison content, who runs this] and a footer with contact and ownership (remedy: None)
8. **[Reflex P1] SLP-010 No template chrome glyphs** (6x). div.relative.rounded-2xl:nth-of-type(2) > div.rounded-xl.bg-\[\#f8fafc\] > div.space-y-3.py-5:nth-of-type(2) > div.flex.items-center:nth-of-type(1) > span.text-xs.font-medium:nth-of-type(2)  "01"  
   Evidence: template chrome (numbering-tokens): "01"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
9. **[Reflex P1] A11-004 Target size** (2x). div.min-h-screen.bg-\[\#f8fafc\]:nth-of-type(2) > header.sticky.top-0 > div.mx-auto.flex > div.flex.items-center:nth-of-type(2) > button.rounded-lg.bg-\[\#1d4ed8\]:nth-of-type(2)  "Get started"  
   Evidence: touch target 129x36px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
10. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). main > section.relative.overflow-hidden:nth-of-type(1) > div.mx-auto.grid > div:nth-of-type(1) > h1.max-w-xl.text-5xl  "Stop searching."  
   Evidence: display text at 60px set in Arial, a UI text face  
   Fix: Pick a display face for the brief; see substitutes in data/lexicons/fonts.yaml. (remedy: fix-typeset)
11. **[Reflex P1] SLP-014 No cards inside cards** (1x). div.relative:nth-of-type(2) > div.relative.rounded-2xl:nth-of-type(2) > div.rounded-xl.bg-\[\#f8fafc\] > div.space-y-3.py-5:nth-of-type(2) > div.flex.items-center:nth-of-type(1)  
   Evidence: card inside a card (div.relative.rounded-2xl:nth-of-type(2))  
   Fix: Keep one container level; group inside it with spacing or a rule. (remedy: fix-layout)
12. **[Reflex P1] MOT-001 Motion CSS hygiene** (1x). .transition-all  
   Evidence: "transition-property: all": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
13. **[Reflex P1] A11-103 Use landmarks and semantic elements** (1x). page landmarks  
   Evidence: landmarks: main 1, nav 1, header 1, footer 0. No contentinfo; no ownership, contact or privacy links anywhere.  
   Fix: <footer> with owner, contact and privacy links (remedy: None)
14. **[Reflex P1] SLP-002 No decorative section numbering** (1x). 'How it works' section, tile 01  
   Evidence: Failed T-STOCK-ORDER: three equal white cards labelled 01 / 02 / 03 with 'Tell us what you want to do', 'Get your personalized stack', 'Make something great'; the card bodies are one line each and the third ('Follow the steps and start building today.') says nothing. Section order: badge hero + mock, 1-2-3 steps, end. No footer.  
   Fix: Show one worked example end to end (goal in, stack out with why each tool was picked) instead of three abstract steps (remedy: fix-typeset)
15. **[Reflex P2] A11-003 Visible focus everywhere** (8x). button "Find my stack"  
   Evidence: focus indicator visible but faint: 1.52:1 against the unfocused state (target 3.0:1, WCAG 2.4.13)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)

4 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://ai-stack-gold.vercel.app/_next/static/immutable/chunks/04ohrrsckm_pd.js
- a11y: Live keyboard operation of the mobile menu (no Playwright run in this review)
- a11y: Alt text: the page has no <img> content images; tool tiles are text letters
- a11y: Forms and errors: no forms on the captured page
- a11y: Sweep Floor hits (INT-001 count, text sizes) checked against tile 00 and agree
- slop: Behaviour of the goal picker behind 'Find my AI stack' (not captured)
- slop: Brand brief: no contract overrides supplied
