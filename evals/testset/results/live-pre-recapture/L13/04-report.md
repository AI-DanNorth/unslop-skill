# Unslop report: https://impeccable.style/antipattern-examples/new-slop-2025.html

**Verdict (draft): rebuild**. Profile: balanced. 6 Floor finding(s) open.

## Four-line read

- **For:** _(synthesize writes this)_
- **Works and stays:** _(synthesize)_
- **Reads generated:** _(synthesize)_
- **Broken:** _(synthesize)_

## Score

| Dimension | Score | Note |
|---|---|---|
| Concept | 1 | lens-concept: T-ONE-SENTENCE, T-RIVAL-NAME, T-SIGNATURE, T-KIND-FIT, T-MIRROR and T-DEFAULT-AGENT all fail, T-DEFAULT-PLAN marks four moves, and the sweep finds every tell of |
| Hierarchy | 4 | lens-structure: T-SQUINT finds a clear h1 on the first screen, but T-STOCK-ORDER finds five stock sections, T-ANATOMY finds no product view, and T-FIVE-SECOND fails at 375 wher |
| Craft | 3 | lens-color (lowest of color 3, typography 3): T-COLOUR-SOURCE finds a look family's palette with no brand behind it, T-ACCENT-DOSAGE finds the accent on display type and labels while every button is ink, an |
| Accessibility | 1 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 1 | from sweep |
| Distinctiveness | 1 | lens-copy: T-FRESH-READER cannot say what Lumina does, T-RIVAL-NAME leaves every heading, the sub-line and all three feature cards true for any SaaS product, and T-CADENCE |

Overall (draft): **1.8**

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-001 No invented metrics** (1x). html > body > section.hero:nth-of-type(1)  
   Evidence: "Trusted by 10,000+" (invented-metrics/social-proof-counts, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
2. **[Floor P0] A11-001 Text contrast on real pixels** (1x). html > body > section.cta-section:nth-of-type(4) > span.section-number  "03"  
   Evidence: 2.87:1 against the background behind the text (10th-percentile pixel #1f1a15, worst 2.87:1; text #a8431f, 11px; needs 4.5:1). APCA Lc 21 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > section.logos:nth-of-type(2) > div.logos-inner  
   Evidence: page is 698px wide at a 375px viewport (sideways scroll); widest culprit 724px  
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
7. **[Reflex P1] CON-003 The idea fits in one sentence** (1x). hero, 1440px and 375px (tiles/1440-00.png, 375-00.png)  
   Evidence: T-ONE-SENTENCE fails. The eyebrow 'AI-NATIVE WORKFLOWS', the h1 'Build faster with intelligent workflows for modern teams' and the sub-line 'The all-in-one platform that helps product teams ship better software in record time. Powered by AI, designed for humans.' never say what a workflow in Lumina is or does. T-MEMORY after one look: 'a peach glow behind a big serif with one orange italic word', a mood, not a thing.  
   Fix: [DATA NEEDED: what Lumina does, for whom, and one thing it does that others do not], then an h1 that names it (remedy: explore-directions)
8. **[Reflex P1] CON-014 Software shows its own UI at work** (1x). whole page, 1440px  
   Evidence: T-KIND-FIT and T-SIGNATURE fail. The kind is software for product teams, yet the page has no screenshot, no product frame and no image of any kind: the DOM lists no image wider than 150px. The first screen's only picture is a peach radial glow over a grid of hairlines (the sweep's glow and gradient hits). 'Watch demo' is the only hint that a product exists.  
   Fix: Lead with the product at work: one real workflow in the Lumina interface on the first screen [DATA NEEDED: product screenshot] (remedy: explore-directions)
9. **[Reflex P1] CON-009 No look picked for the category or by default** (1x). whole page, 1440px  
   Evidence: T-MIRROR and T-DEFAULT-AGENT fail. Cream ground #faf6ef, Fraunces display with one italic terracotta word ('intelligent' in #c8552b), small numbered section labels '01', '02', '03', a letter-spaced eyebrow and a grid-paper hero are the cream-serif-clay look the sweep names warm-paper-serif (6 of 6 tells). Typing 'landing page for an AI workflow tool, warm and editorial' into an agent produces this page.  
   Fix: Choose the look from the product's own material once it exists; move at least one axis off the spent look, for example the accent first (CON-137) (remedy: fix-colorize)
10. **[Reflex P1] CON-002 Every large decision belongs to this client** (1x). h1, h2s and feature cards, 1440px (tiles/1440-01.png, 1440-02.png)  
   Evidence: T-RIVAL-NAME: with Notion, Linear or Asana in place of Lumina, 'Build faster with intelligent workflows for modern teams', 'Everything you need to ship great products', 'One platform. Endless possibilities.', 'Lightning Fast', 'Enterprise Secure', 'Built to Scale' and 'Ready to transform how your team builds?' all stay true. The logo row 'Northwind, Halcyon, Meridian, Fieldnote, Atlas & Co., Verity' is set as italic text, not logos (the sweep's default_names flags these).  
   Fix: Headings built from facts only Lumina has [DATA NEEDED: product facts, real customers] (remedy: explore-directions)
11. **[Reflex P1] CON-008 Refuse the default plan** (1x). whole page, 1440px  
   Evidence: T-DEFAULT-PLAN marks four moves: small numbered labels on every section ('01', '02', '03'); three equal feature cards with emoji icons (lightning, padlock, chart); a dark closing band 'Ready to transform how your team builds?' with one button; a pale ground with one careful accent. The page is hero, logo row, three cards, closing band and a one-line footer, the stock order.  
   Fix: Replace the three cards with one section that shows a real workflow end to end (remedy: fix-layout)
12. **[Reflex P1] CPY-007 Copy that survives the rival's-name swap** (1x). h1, sub-line and both h2s, 1440, tiles/1440-00.png and tiles/1440-01.png  
   Evidence: Failed T-RIVAL-NAME and T-FRESH-READER: 'Build faster with intelligent workflows for modern teams', 'The all-in-one platform that helps product teams ship better software in record time. Powered by AI, designed for humans.', 'Everything you need to ship great products' and 'Ready to transform how your team builds?' stay true under Linear's, Asana's or any product tool's name. From the text alone a reader cannot say what a 'workflow' in Lumina is, what it costs or why it beats another tool. The sweep's stock-phrase hits on the two h2s and 'Join thousands of' are not repeated.  
   Fix: Name the job Lumina does and for whom in the h1. [DATA NEEDED: what Lumina actually does and the one thing it does differently] (remedy: fix-copy)
13. **[Reflex P1] CPY-005 No slop diction** (9x). html > body > section.features:nth-of-type(3) > div.features-head:nth-of-type(1) > h2  "Everything you need to ship great products"  
   Evidence: "Everything you need to" (stock-phrases/openers, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
14. **[Reflex P1] SLP-010 No template chrome glyphs** (7x). html > body > section.hero:nth-of-type(1) > span.section-number  "01"  
   Evidence: template chrome (numbering-tokens): "01"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
15. **[Reflex P1] INT-002 No default cast or fake brands** (6x). html > body > section.logos:nth-of-type(2) > div.logos-inner > span:nth-of-type(1)  "Northwind"  
   Evidence: "Northwind" (default-names/fake-brands, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)

35 further findings are in 04-findings.json.

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
- color: T-DARK-MODE: the page is light and no dark theme is declared; the stylesheet flags show some sheets were unreadable, so a dark variant is not verified.
- color: The peach radial wash and grid behind the hero (the #f6e2d1 area, 31.6% of the page render) are the sweep's SLP-007 and SLP-008 hits and are not repeated.
- color: The capture blocked one script, /js/detect-antipatterns-browser.js, as page preparation; it does not change the page's colours.
- concept: 00-contract.md is absent; visitor mode read as Persuade from the page itself.
- concept: A detector script on the host was blocked by capture prep (manifest.prep); it is not part of the page design.
- concept: At 375 the header and hero do not fit the viewport (tile 375-00 shows the page wider than the screen); that is a layout issue for another lens.
- copy: T-STATE-COPY: no form on the page and async.json was not captured.
- copy: T-LONG-FORM: no long-form region; landing page of 166 words.
- copy: T-TERMS: no term is used 3 or more times.
- copy: Strengths: none listed; no line carries a fact only this client has.
- copy: Contract: no 00-contract.md in the run; judged as a Persuade landing page.
- slop: Brand brief: none supplied
- slop: Watch demo target (href=#)
- structure: The 375 capture overflows sideways to 698px (overflow, Floor); T-PHONE-ORDER was read for section order only, which is kept. The overflow belongs to the sweep and lens-a11y.
- structure: Capture prep blocked the page's own anti-pattern detector script (manifest prep); this is capture context, not a design choice.
- structure: heading_rhythm, flat_hierarchy and type_ladder are sweep findings and are not repeated.
- typography: T-LABEL-TRANSFORM: the tracked caps "AI-NATIVE WORKFLOWS" and the 11px "01", "02", "03" section numbers are the sweep's eyebrow and numbered_labels hits.
- typography: T-FIGURES: no figures compare on the page.
- typography: T-PUNCTUATION: no quote marks or ellipses on the page.
- typography: Stylesheet flags: the type table could not read the stylesheets (unreadable_sheets), so tabular-nums and text-wrap are unknown.
- typography: The 375 overflow itself belongs to layout and robustness.
