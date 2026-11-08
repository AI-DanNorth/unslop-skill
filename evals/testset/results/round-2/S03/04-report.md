# Unslop report: /home/claude/refs/impeccable/demos/landing-demo/classic/index.html

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
| Integrity | 1 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (14x). body > nav.nav > div.nav-inner > div.nav-cta:nth-of-type(3) > a.pill:nth-of-type(2)  "Get started →"  
   Evidence: 2.36:1 against the background behind the text (10th-percentile pixel #c750bd, worst 2.34:1; text #ffffff, opacity 0.60, 14px; needs 4.5:1). APCA Lc 37 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] TYP-004 The intended font actually renders** (1x). body > section.features:nth-of-type(3) > div.grid:nth-of-type(2) > div.card:nth-of-type(2) > div.icon  "🔒"  
   Evidence: declared "Inter" but Noto Color Emoji drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
3. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > nav.nav > div.nav-inner > div.nav-links:nth-of-type(2)  
   Evidence: page is 694px wide at a 375px viewport (sideways scroll); widest culprit 377px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
4. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). a.btn-primary 'Join the waitlist →', 'Get early access →', a.pill 'Get started →'  
   Evidence: No :focus-visible style; focus.json shows the UA 'auto 1px rgb(117,117,117)' ring on the gradient buttons. focus/07-on.png shows a hairline grey edge on the #8b5cf6-to-#ec4899 fill that is barely distinguishable from the button's own edge and glow. On the dark nav links the UA ring is a faint grey (focus/00-on.png): visible but thin.  
   Fix: .btn:focus-visible, .pill:focus-visible, .nav a:focus-visible { outline: 2px solid #ffffff; outline-offset: 3px } (remedy: None)
5. **[Floor P0] A11-110 Keep all words as real text in reading order** (1x). nav.nav and hero CTAs at 375px  
   Evidence: Verified sweep ROB-003: at 375 the desktop nav stays on one row, the page is 694px wide, 'Get started' becomes a 84px circle at x610-694 off-canvas, and the hero column is cut at x375 (tile 375-00). The hero buttons wrap their labels ('Join the / waitlist →', 'Watch / demo') inside fixed-height boxes, clipping text. No menu button exists.  
   Fix: @media (max-width: 720px) { .nav-links { display: none } } plus a <button aria-expanded> menu; .btn { white-space: nowrap; height: auto; min-height: 48px } (remedy: None)
6. **[Floor P0] INT-151 Give each fact one value and one wording everywhere it appears** (1x). nav, hero CTAs, features card 3, CTA band  
   Evidence: Failed T-THREE-LINE on consistency: the page offers 'Join the waitlist' and 'Get early access' (not launched) while claiming 'Join thousands of teams already shipping faster with Lumina', 'From your first prototype to millions of users', 'SOC 2 compliant infrastructure', plus 'Sign in' and 'Get started'. A product cannot be both waitlist-only and in use by thousands with a SOC 2 report.  
   Fix: [DATA NEEDED: launch status]; if pre-launch, remove usage, scale and SOC 2 claims and the Sign in link; if live, drop the waitlist language (remedy: None)
7. **[Floor P0] INT-103 Never invent logo walls or customer names** (1x). section.logos and hero proof line  
   Evidence: Six customer names in grey text in place of logos (Northwind, Halcyon, Meridian, Fieldnote, Atlas & Co., Verity) on a page that is waitlist-only, plus 'Backed by top-tier investors' with no investor named. The sweep flagged three names as default names (Reflex); together they are an invented logo wall and unattributed backing claim.  
   Fix: [DATA NEEDED: real customers with permission and logo files; named investors] or remove both (remedy: None)
8. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). hero, 1440 first screen  
   Evidence: Failed T-FIVE-SECOND: '🚀 POWERED BY AI' / 'Build faster with intelligent workflows' / 'The all-in-one platform that helps modern teams ship better products in record time.' Neither what Lumina is nor who it is for ('modern teams') is answered, and the two CTAs offer different things ('Join the waitlist', 'Watch demo') from the nav ('Get started').  
   Fix: [DATA NEEDED: what Lumina does, for which team, and whether it is live]; h1 states the job, one CTA states the real next step (remedy: None)
9. **[Reflex P1] SLP-108 Use Concept/Intent as a one-vote veto: if the design survives swapping in another client's** (1x). h1, h2s, h3s  
   Evidence: Failed T-RIVAL-NAME: every heading stays true for any AI product: 'Build faster with intelligent workflows', 'Everything you need to ship faster', 'Lightning Fast', 'Enterprise Secure', 'Built to Scale', 'Ready to transform how your team builds?'. T-FRESH-READER generic lines: the h1, 'One platform. Endless possibilities. Built for the future.', the CTA h2. Concept capped at 5.  
   Fix: [DATA NEEDED: three capabilities only Lumina has, each with a mechanism or measured number] (remedy: None)
10. **[Reflex P1] SLP-138 Refuse the stock template page: hero, 3 features, (testimonials), CTA, footer** (1x). page skeleton  
   Evidence: Failed T-DEFAULT-AGENT and T-MIRROR: centred pill eyebrow + gradient h1 + two CTAs + proof line, six-name logo strip, three equal cards with gradient emoji tiles, dark gradient CTA band, one-line footer. Typing 'landing page for an AI workflow startup' returns this. The violet-gradient skin is reported by the sweep (SLP-012 cluster, gradients, glows); the skeleton and the decorative teal radial spotlight behind the hero (right, 1440 tile 00) complete it.  
   Fix: Start from the product: show its UI doing one named job on the first screen and drop the glow, pill and emoji tiles together (SLP-112: fix with a decision, not a synonym) (remedy: None)
11. **[Reflex P1] SLP-007 No stock gradient pairs** (9x). html > body > nav.nav > div.nav-inner > div.logo:nth-of-type(1)  "Lumina ✨"  
   Evidence: gradient hue span 62° + banned pair (hues 265-330 with 331-25): #8b5cf6, #ec4899  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
12. **[Reflex P1] CPY-005 No slop diction** (8x). html > body > section.features:nth-of-type(3) > div.features-head:nth-of-type(1) > h2  "Everything you need to ship faster"  
   Evidence: "Everything you need to" (stock-phrases/openers, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
13. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (6x). body > nav.nav > div.nav-inner > div.nav-cta:nth-of-type(3) > a.pill:nth-of-type(2)  "Get started →"  
   Evidence: zero-offset coloured boxShadow #8b5cf6 blur 32px alpha 0.50  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
14. **[Reflex P1] INT-002 No default cast or fake brands** (6x). html > body > section.logos:nth-of-type(2) > div.logos-inner > span:nth-of-type(1)  "Northwind"  
   Evidence: "Northwind" (default-names/fake-brands, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
15. **[Reflex P1] A11-004 Target size** (6x). body > nav.nav > div.nav-inner > div.nav-links:nth-of-type(2) > a:nth-of-type(1)  "Product"  
   Evidence: touch target 52x22px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)

17 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: verified sweep A11-001 Floor hits: white 15px text on gradient buttons measures about 3.8:1 (real); nav pill text at opacity .6 about 2.3:1 (real); 'Powered by AI' #8b5cf6 12px on violet glow about 2.6:1 (real); logo-strip names at opacity .36 about 3.3:1 (real, though if they are logos they would be exempt; here they are text)
- a11y: motion: only 0.2s 'all' hover transitions, no autoplay; sweep skipped reduced motion as no animation
- a11y: keyboard: no menus, dialogs or tabs; 'Watch demo' has no behaviour
- a11y: forms: none (waitlist has no form)
- a11y: no <main> and no skip link: sweep-reported, not repeated
- slop: No strengths recorded: nothing on the page is specific to the client; type spacing and alignment are tidy but default
- slop: T-STOCK-ORDER: hero, logo strip, three equal feature cards, CTA band = 4 stock sections plus a minimal footer, under the 5 threshold; generated read rests on T-DEFAULT-AGENT, T-MIRROR and the sweep's violet-gradient cluster
- slop: Sweep TYP-003 (Inter display) and SLP-007/008 gradient and glow hits not repeated
- slop: copy voice: no contract or brand samples supplied
