# Unslop report: https://impeccable.style/antipattern-examples/new-slop-2025.html

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
| Integrity | 1 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-001 No invented metrics** (2x). html > body > section.hero:nth-of-type(1)  
   Evidence: "Trusted by 10,000+" (invented-metrics/social-proof-counts, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
2. **[Floor P0] A11-001 Text contrast on real pixels** (1x). html > body > section.cta-section:nth-of-type(4) > span.section-number  "03"  
   Evidence: 2.87:1 against the background behind the text (10th-percentile pixel #1f1a15, worst 2.87:1; text #a8431f, 11px; needs 4.5:1). APCA Lc 21 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > section.logos:nth-of-type(2) > div.logos-inner  
   Evidence: page is 720px wide at a 375px viewport (sideways scroll); widest culprit 724px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
4. **[Floor P0] A11-112 Every control has an accessible name** (1x). all links (nav, hero CTAs, CTA band)  
   Evidence: dom-1440.json: all 10 links have href="#". 'Product', 'Pricing', 'Docs', 'Watch demo' and both trial links go nowhere; activating them only jumps to the top of the page.  
   Fix: <a href="/pricing">Pricing</a>; for 'Watch demo' a <button> that opens a dialog with a captioned video (remedy: None)
5. **[Floor P0] A11-011 Reduced motion respected** (1x). logo strip (div.logos-inner), h1 caret, logo dot  
   Evidence: dom-1440.json: logo-marquee 12s animation on the logo strip, blink-cursor 0.9s on span.fake-cursor in the h1 and pulse-status 1.8s on the logo dot, all running continuously; no pause control is visible in the tiles.  
   Fix: Add a pause button for the marquee (or make it static), and set animation: none on .fake-cursor and .logo-dot; also wrap all three in @media (prefers-reduced-motion: no-preference) (remedy: fix-motion)
6. **[Floor P0] INT-005 No placeholder residue at ship** (1x). every link  
   Evidence: dom-1440.json: all 10 links (Product, Solutions, Pricing, Customers, Docs, Sign in, Get started, Start free trial, Watch demo, Start your free trial) have href="#". 'SOC 2 compliant infrastructure' is claimed with no link or proof.  
   Fix: Real destinations; link the SOC 2 report or remove the claim [DATA NEEDED: audit report] (remedy: fix-copy)
7. **[Reflex P1] CPY-005 No slop diction** (9x). html > body > section.features:nth-of-type(3) > div.features-head:nth-of-type(1) > h2  "Everything you need to ship great products"  
   Evidence: "Everything you need to" (stock-phrases/openers, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
8. **[Reflex P1] SLP-010 No template chrome glyphs** (7x). html > body > section.hero:nth-of-type(1) > span.section-number  "01"  
   Evidence: template chrome (numbering-tokens): "01"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
9. **[Reflex P1] INT-002 No default cast or fake brands** (6x). html > body > section.logos:nth-of-type(2) > div.logos-inner > span:nth-of-type(1)  "Northwind"  
   Evidence: "Northwind" (default-names/fake-brands, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
10. **[Reflex P1] A11-004 Target size** (6x). body > nav.nav > div.nav-inner > div.nav-links:nth-of-type(2) > a:nth-of-type(1)  "Product"  
   Evidence: touch target 52x22px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
11. **[Reflex P1] SLP-002 No decorative section numbering** (4x). html > body > section.hero:nth-of-type(1) > span.section-number  "01"  
   Evidence: section number "01" (11px) beside heading "Build faster with workflows for modern t"; 3 on page  
   Fix: Remove the numbers or make them real steps. (remedy: fix-typeset)
12. **[Reflex P1] A11-002 Text size floors** (4x). html > body > section.hero:nth-of-type(1) > div.trust:nth-of-type(3)  "Trusted by forward-thinking teams worldwide"  
   Evidence: 43-character run at 13px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
13. **[Reflex P1] SLP-001 No eyebrow labels above headings** (3x). html > body > section.hero:nth-of-type(1) > div.eyebrow:nth-of-type(1)  "AI-native workflows"  
   Evidence: 12px label tracked 0.16em caps above 88px heading "Build faster with workflows for modern t"; 3 on page, budget 2  
   Fix: Promote the fact into the heading or delete the label (T-EYEBROW). (remedy: fix-typeset)
14. **[Reflex P1] SLP-013 No emoji as icons** (3x). body > section.features:nth-of-type(3) > div.grid:nth-of-type(2) > div.card:nth-of-type(1) > div.icon  "⚡"  
   Evidence: emoji used as an icon: "⚡" (3 on page)  
   Fix: Use a consistent icon set with labels, or no icon. (remedy: fix-quieter)
15. **[Reflex P1] SLP-012 Look-family cluster** (3x). whole page  
   Evidence: warm-paper-serif: 5 of 6 tells (cream_bg (page #faf6ef); terracotta_accent (#c8552b); serif_display (Fraunces); eyebrows (eyebrow detector); numbered_labels (numbered labels)); cluster minimum 3  
   Fix: Break the family on its strongest tell first; name the replacement decision. (remedy: fix-quieter)

10 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://impeccable.style/js/detect-antipatterns-browser.js
- a11y: Live keyboard and reduced-motion behaviour (no Playwright run); sweep reduced_motion did not fire, so the CSS may already respect the preference
- a11y: Forms: none on page
- a11y: disputed: none; sweep contrast hit on '03' (2.87:1 on the dark CTA band) agrees with tile 02
- slop: Brand brief: none supplied
- slop: Watch demo target (href=#)
