# Unslop report: https://impeccable.style/antipattern-examples/old-slop-2022.html

**Verdict (draft): fix**. Profile: balanced. 7 Floor finding(s) open.

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
| Integrity | 2 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). body > nav.nav > div.nav-inner > div.nav-cta:nth-of-type(3) > a.pill:nth-of-type(2)  "Get started →"  
   Evidence: 2.36:1 against the background behind the text (10th-percentile pixel #c750bd, worst 2.34:1; text #ffffff, opacity 0.60, 14px; needs 4.5:1). APCA Lc 37 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > nav.nav > div.nav-inner > div.nav-links:nth-of-type(2)  
   Evidence: page is 694px wide at a 375px viewport (sideways scroll); widest culprit 377px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
3. **[Floor P0] A11-113 Every svg, canvas or CSS-art element carries aria-hidden="true", an aria-label, a labelled** (1x). feature card icons and wordmark  
   Evidence: dom-1440.json: div.icon elements contain raw emoji text '⚡', '🔒', '📈', the eyebrow reads '🚀 POWERED BY AI', the logo text is 'Lumina ✨'. With no aria-hidden, screen readers announce 'high voltage', 'locked', 'chart increasing', 'rocket', 'sparkles' before each heading.  
   Fix: <div class="icon" aria-hidden="true">⚡</div>; <span aria-hidden="true">✨</span> in the logo (remedy: None)
4. **[Floor P0] A11-112 Every control has an accessible name** (1x). every link on the page  
   Evidence: dom-1440.json: all 11 links have href="#" ('Product', 'Pricing', 'Docs', 'Sign in', 'Watch demo', 'Join the waitlist →'...). Each announces as a link but goes nowhere; 'Watch demo' implies a video that does not exist.  
   Fix: Real destinations, or <button> for in-page actions; remove links with no target (remedy: None)
5. **[Floor P0] A11-175 Work at browser zoom 200% without loss** (1x). nav at 375 (tile 375-00)  
   Evidence: Confirms sweep ROB-003: at 375 the nav does not collapse; all five links, 'Sign in' and a circular 'Get started' blob sit in one row, pushing the page to 694px so the hero renders in the left half with an empty dark right half.  
   Fix: @media (max-width: 720px) { .nav-links { display:none } } plus a disclosure button with aria-expanded (remedy: None)
6. **[Floor P0] A11-171 Muted text on brand bands / effects / photos.** (1x). hero h1 gradient text and primary buttons  
   Evidence: Confirms sweep A11-001: 'Get started →' is white at 0.6 opacity over pink #c750bd (2.36:1); the h1 gradient ends in #ec4899 pink on #0a0a14, and 'Join the waitlist →' white on the pink end of its gradient is 3.85:1 at 15px.  
   Fix: Solid #fff text on a solid #6d28d9 fill (7:1+), no opacity on button text (remedy: None)
7. **[Floor P0] INT-003 No fake people or hotlinked stock** (1x). logo strip under hero (tile 1440-01)  
   Evidence: 'Backed by top-tier investors' followed by six wordmark-style names 'Northwind, Halcyon, Meridian, Fieldnote, Atlas & Co., Verity' set as grey text: these are stock placeholder company names presented as social proof.  
   Fix: Remove the strip, or [DATA NEEDED: real investors or customers with permission to show logos] (remedy: fix-harden)
8. **[Reflex P1] SLP-222 Swap / rival's-name test: any head still true with a competitor's name (or the same trade ** (1x). hero h1 and sub-line, 1440 tile 00  
   Evidence: Failed T-RIVAL-NAME and T-FIVE-SECOND: 'Build faster with intelligent workflows' / 'The all-in-one platform that helps modern teams ship better products in record time. Powered by AI, designed for humans.' stays true for any of hundreds of tools; the first screen never says what the product does or for whom. Concept capped at 5.  
   Fix: [DATA NEEDED: what Lumina actually does, for which team, and one concrete outcome] (remedy: None)
9. **[Reflex P1] SLP-007 No stock gradient pairs** (9x). html > body > nav.nav > div.nav-inner > div.logo:nth-of-type(1)  "Lumina ✨"  
   Evidence: gradient hue span 62° + banned pair (hues 265-330 with 331-25): #8b5cf6, #ec4899  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
10. **[Reflex P1] CPY-005 No slop diction** (8x). html > body > section.features:nth-of-type(3) > div.features-head:nth-of-type(1) > h2  "Everything you need to ship faster"  
   Evidence: "Everything you need to" (stock-phrases/openers, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (6x). body > nav.nav > div.nav-inner > div.nav-cta:nth-of-type(3) > a.pill:nth-of-type(2)  "Get started →"  
   Evidence: zero-offset coloured boxShadow #8b5cf6 blur 32px alpha 0.50  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
12. **[Reflex P1] INT-002 No default cast or fake brands** (6x). html > body > section.logos:nth-of-type(2) > div.logos-inner > span:nth-of-type(1)  "Northwind"  
   Evidence: "Northwind" (default-names/fake-brands, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
13. **[Reflex P1] A11-004 Target size** (6x). body > nav.nav > div.nav-inner > div.nav-links:nth-of-type(2) > a:nth-of-type(1)  "Product"  
   Evidence: touch target 52x22px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
14. **[Reflex P1] SLP-010 No template chrome glyphs** (5x). html > body > section.hero:nth-of-type(1) > div.eyebrow:nth-of-type(1)  "🚀 Powered by AI"  
   Evidence: template chrome (emoji-bullets): "🚀 Powered by AI"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
15. **[Reflex P1] SLP-013 No emoji as icons** (3x). body > section.features:nth-of-type(3) > div.grid:nth-of-type(2) > div.card:nth-of-type(1) > div.icon  "⚡"  
   Evidence: emoji used as an icon: "⚡" (3 on page)  
   Fix: Use a consistent icon set with labels, or no icon. (remedy: fix-quieter)

15 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no movement in stylesheets (spinners and opacity/visibility-only keyframes excluded)
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://impeccable.style/js/detect-antipatterns-browser.js
- a11y: the page's own antipattern-detector script was blocked by capture prep; it is not part of the design
- a11y: keyboard: no menus, dialogs or custom controls to test
- a11y: forms: none
- slop: no 00-contract.md brief; nothing on the page is specific enough to protect as a strength
- slop: all links are href="#" so no downstream pages exist to check
