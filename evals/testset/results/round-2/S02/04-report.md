# Unslop report: /home/claude/refs/impeccable/demos/landing-demo/index.html

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

1. **[Floor P0] INT-001 No invented metrics** (2x). html > body > section.hero:nth-of-type(1)  
   Evidence: "Trusted by 10,000+" (invented-metrics/social-proof-counts, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
2. **[Floor P0] TYP-004 The intended font actually renders** (1x). body > section.features:nth-of-type(3) > div.grid:nth-of-type(2) > div.card:nth-of-type(2) > div.icon  "🔒"  
   Evidence: declared "Inter" but Noto Color Emoji drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
3. **[Floor P0] A11-011 Reduced motion respected** (1x). stylesheet  
   Evidence: page animates (keyframes or transform transitions) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
4. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > nav.nav > div.nav-inner > div.nav-links:nth-of-type(2)  
   Evidence: page is 698px wide at a 375px viewport (sideways scroll); widest culprit 377px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
5. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). a.pill 'Get started', a.btn-primary 'Start free trial →', CTA band 'Start your free trial →'  
   Evidence: focus.json shows every stop uses the browser default 'auto 1px rgb(16,16,16)' outline. On the near-black primary buttons (#1f1a17 fill) that ring is dark-on-dark: focus/07-on.png for 'Start free trial →' shows no visible ring at all. On the dark CTA band the ring sits on the dark ground as well.  
   Fix: .btn:focus-visible, .pill:focus-visible { outline: 2px solid #c8552b; outline-offset: 3px } and on .cta-section use a cream ring (outline-color: #faf6ef) (remedy: None)
6. **[Floor P0] A11-110 Keep all words as real text in reading order** (1x). nav.nav at 375px  
   Evidence: Verified sweep ROB-003: at 375 the full desktop nav stays in one row (tile 375-00), pushing the page to 698px wide; 'Get started' sits off-canvas at x 615-698 and the hero is cut at the right. No menu button replaces the links. Users must scroll in two directions.  
   Fix: @media (max-width: 720px) { .nav-links { display: none } } plus a <button aria-expanded> menu, keeping 'Get started' visible (remedy: None)
7. **[Floor P0] INT-103 Never invent logo walls or customer names** (1x). section.logos: 'Northwind Halcyon Meridian Fieldnote Atlas & Co. Verity'  
   Evidence: Six customer names set as italic serif text in place of logos, directly under 'Trusted by 10,000+'. The sweep flagged three as default names (Reflex); as a group they form an invented logo wall presented as customers, which is an integrity failure. 'Meridian', 'Atlas & Co.' and 'Verity' are the same kind of stock name and were not flagged.  
   Fix: [DATA NEEDED: real customers who agreed to be named, with their logo files] or remove the strip (remedy: None)
8. **[Floor P0] INT-101 Never invent a metric, customer count, uptime, speed multiple, saving or percentage the us** (1x). features card 2 and 3 body copy  
   Evidence: Failed T-THREE-LINE: 'SOC 2 compliant infrastructure with end-to-end encryption. Your data is safe, always.' and 'From your first prototype to millions of users' are compliance and scale claims with no source, report or date. The sweep caught '10,000+' but not these.  
   Fix: [DATA NEEDED: SOC 2 report type and date, link to trust page]; else drop the claim (remedy: None)
9. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). hero, 1440 first screen  
   Evidence: Failed T-FIVE-SECOND: 'Build faster with intelligent workflows for modern teams' / 'The all-in-one platform that helps product teams ship better software in record time. Powered by AI, designed for humans.' The audience (product teams) is named, but what Lumina is (a tracker? CI? a spec tool?) is never said, and there is no picture of the product on any screen.  
   Fix: [DATA NEEDED: the one job Lumina does and its object, e.g. what it takes in and what it produces]; show the product UI doing it under the hero (CON-147) (remedy: None)
10. **[Reflex P1] SLP-108 Use Concept/Intent as a one-vote veto: if the design survives swapping in another client's** (1x). h1, h2s, h3s, CTA band  
   Evidence: Failed T-RIVAL-NAME: with Linear, Height or any workflow tool swapped in, every heading stays true: 'Build faster with intelligent workflows for modern teams', 'Everything you need to ship great products', 'Lightning Fast', 'Enterprise Secure', 'Built to Scale', 'Ready to transform how your team builds?'. T-FRESH-READER generic lines: the h1, 'One platform. Endless possibilities. Built for teams who care about craft.', and the CTA h2. Concept capped at 5.  
   Fix: [DATA NEEDED: three things only Lumina does, each with its mechanism or number]; headings name those things (remedy: None)
11. **[Reflex P1] SLP-138 Refuse the stock template page: hero, 3 features, (testimonials), CTA, footer** (1x). page skeleton: nav, hero, logos, features, CTA band, footer  
   Evidence: Failed T-MIRROR and T-DEFAULT-AGENT: centred eyebrow + h1 with one italic accent word + two CTAs + 'Trusted by 10,000+' line, then a six-name logo strip, three equal cards with emoji in rounded tiles, a dark 'Ready to transform' band. 'landing page for an AI workflow tool' yields this exactly. The warm-paper serif cluster (sweep SLP-012) is the paint; the skeleton underneath is the stock SaaS page.  
   Fix: Change one structural decision and name it: lead with the product UI on the first screen and let a real workflow run down the page instead of three equal cards (remedy: None)
12. **[Reflex P1] CPY-005 No slop diction** (7x). html > body > section.features:nth-of-type(3) > div.features-head:nth-of-type(1) > h2  "Everything you need to ship great products"  
   Evidence: "Everything you need to" (stock-phrases/openers, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
13. **[Reflex P1] INT-002 No default cast or fake brands** (6x). html > body > section.logos:nth-of-type(2) > div.logos-inner > span:nth-of-type(1)  "Northwind"  
   Evidence: "Northwind" (default-names/fake-brands, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
14. **[Reflex P1] A11-004 Target size** (6x). body > nav.nav > div.nav-inner > div.nav-links:nth-of-type(2) > a:nth-of-type(1)  "Product"  
   Evidence: touch target 52x22px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
15. **[Reflex P1] SLP-013 No emoji as icons** (3x). body > section.features:nth-of-type(3) > div.grid:nth-of-type(2) > div.card:nth-of-type(1) > div.icon  "⚡"  
   Evidence: emoji used as an icon: "⚡" (3 on page)  
   Fix: Use a consistent icon set with labels, or no icon. (remedy: fix-quieter)

13 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: verified sweep Floor ROB-003 overflow at 375: real (see reflow finding, which adds the off-canvas CTA and missing menu)
- a11y: verified sweep Floor A11-011 reduced motion: stylesheet animates (button transforms); not verified visually, no capture of motion
- a11y: sweep Floor TYP-004 (emoji drawn by Noto Color Emoji): typographic, not an a11y failure; disputed as a11y Floor
- a11y: keyboard operation: no menus, dialogs or tabs exist; 'Watch demo' has no behaviour to test
- a11y: forms: none
- a11y: no <main> landmark and no skip link: sweep-reported, not repeated
- slop: T-STOCK-ORDER: hero, logo strip, three equal feature cards, CTA band = 4 stock sections plus a minimal footer, under the 5 threshold; generated read rests on T-MIRROR, T-DEFAULT-AGENT and the look-family cluster
- slop: Look family warm-paper-serif already reported by sweep (SLP-012); not repeated
- slop: copy voice: no contract or brand samples supplied
