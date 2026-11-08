# Unslop report: /home/claude/refs/hallmark/skills/hallmark/scripts/fixtures/slopped.html

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

1. **[Floor P0] INT-001 No invented metrics** (6x). html > body > main > section.hero:nth-of-type(1) > p.promo  "Trusted by 50,000+ teams shipping 10x faster."  
   Evidence: "10x faster" (invented-metrics/multipliers, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
2. **[Floor P0] A11-011 Reduced motion respected** (2x). stylesheet  
   Evidence: page animates (keyframes or transform transitions) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
3. **[Floor P0] A11-001 Text contrast on real pixels** (1x). html > body > main > section.hero:nth-of-type(1) > p.promo  "Trusted by 50,000+ teams shipping 10x faster."  
   Evidence: 4.35:1 against the background behind the text (10th-percentile pixel #ffffff, worst 4.35:1; text #e91e63, 16px; needs 4.5:1). APCA Lc 68 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
4. **[Floor P0] A11-114 Meaningful images get alt describing what they show** (1x). section.gallery img:nth-of-type(1) and img:nth-of-type(2)  
   Evidence: alt="Product screenshot one" and alt="Product screenshot two"; both images fail to load (naturalWidth 0), so the alt text is all a sighted or screen-reader user gets, and it names a slot, not content.  
   Fix: alt describing what the screen shows, e.g. alt="[DATA NEEDED: what the screenshot shows, e.g. the sync settings panel with two connected tools]"; fix the src so the file exists (remedy: None)
5. **[Floor P0] A11-113 Every svg, canvas or CSS-art element carries aria-hidden="true", an aria-label, a labelled** (1x). section.hero > svg (grey circle, 120x40 at y183)  
   Evidence: Inline svg with no aria-hidden, no role, no title or aria-label (dom-1440: name null, role null). It is decorative.  
   Fix: <svg aria-hidden="true" focusable="false">...</svg> (remedy: None)
6. **[Floor P0] INT-102 Never invent testimonials, quotes, reviews, ratings, review counts, awards or press lines** (1x). section.voices: blockquote and attribution  
   Evidence: Failed T-THREE-LINE: '"It changed everything for our team."' is not picturable, not falsifiable and not specific to this business, and it is attributed to 'Jane Doe, Head of Operations' with no company. The sweep flagged the name (INT-002); the quote itself is an invented testimonial.  
   Fix: [DATA NEEDED: a real customer quote with full name, role and company, used with permission] or remove the section (remedy: None)
7. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). first screen, 1440 and 375 (nav, h1, promo line)  
   Evidence: Failed T-FIVE-SECOND: the first screen says 'Unleash hyperproductivity-supercharged workflows' and 'Get started'. It never says what Nexus is (a sync tool? a project tracker?), who it is for, or what 'Get started' leads to. The only CTA is an unstyled browser-default button beside the wordmark.  
   Fix: [DATA NEEDED: what Nexus does in one plain clause, who uses it, and what the button starts (trial, demo, download)]; then an h1 built from that clause and a button labelled with that action (remedy: None)
8. **[Reflex P1] SLP-108 Use Concept/Intent as a one-vote veto: if the design survives swapping in another client's** (1x). h1, h2, h3, blockquote (whole page)  
   Evidence: Failed T-RIVAL-NAME: with any workflow SaaS name swapped in, every heading stays true: 'Unleash hyperproductivity-supercharged workflows', 'Everything, seamlessly', 'Magic sync', 'It changed everything for our team.' T-FRESH-READER generic lines: the h1, the h2 and the quote, all of them headings or the hero. Concept capped at 5.  
   Fix: [DATA NEEDED: the specific thing Nexus syncs, between which tools, and one concrete outcome]; each heading should name that object or mechanism (remedy: None)
9. **[Reflex P1] SLP-012 Look-family cluster** (1x). whole page, 1440  
   Evidence: Failed T-DEFAULT-AGENT: 'landing page for a productivity SaaS' plausibly yields exactly this kit: #8b5cf6 to #3b82f6 gradient-clip headline (violet-gradient family: ai_purple + gradient_pair), Poppins display over Inter body, sparkle-emoji feature icon, a mono wordmark, a '01 / FEATURES' eyebrow, a two-up product screenshot row and a one-line testimonial. Individually swept; together they form a cluster of 6+ default tells across two look families (violet-gradient, saas-card-kit).  
   Fix: Pick one direction from the product itself (its UI, its data, its users' vocabulary) and drop the gradient, emoji and eyebrow together rather than swapping each for a synonym (SLP-112) (remedy: fix-quieter)
10. **[Reflex P1] CON-147 Software lead picture is the client's own UI showing what it works on (code review = diff ** (1x). section.gallery (two images, 720px each)  
   Evidence: Both images have alt 'Product screenshot one' / 'Product screenshot two' and render broken (naturalWidth 0; files shot-1.png and shot-2.png absent, not blocked by capture per manifest). The page therefore shows no product at all; even the alt text describes a slot, not a screen.  
   Fix: [DATA NEEDED: real captures of Nexus in a telling state (IMG-117)] with alts that say what each screen shows (remedy: None)
11. **[Reflex P1] SLP-010 No template chrome glyphs** (7x). html > body > main > div.features__head > span.eyebrow  "01 / FEATURES"  
   Evidence: template chrome (numbering-tokens): "01 / FEATURES"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
12. **[Reflex P1] CPY-005 No slop diction** (3x). html > body > main > section.hero:nth-of-type(1) > h1  "Unleash hyperproductivity-supercharged workflows"  
   Evidence: "Unleash" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
13. **[Reflex P1] INT-002 No default cast or fake brands** (2x). html > body > main > section.voices:nth-of-type(4) > p  "Jane Doe, Head of Operations"  
   Evidence: "Jane Doe" (default-names/placeholder-people, fail)  
   Fix: Use supplied names, or remove the testimonial. (remedy: fix-copy)
14. **[Reflex P1] SLP-007 No stock gradient pairs** (1x). html > body > main > section.hero:nth-of-type(1) > h1  "Unleash hyperproductivity-supercharged workflows"  
   Evidence: gradient banned pair (hues 265-330 with 200-264): #8b5cf6, #3b82f6  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
15. **[Reflex P1] TYP-001 Clear type hierarchy** (1x). h3 vs body  
   Evidence: h3 19px is only 1.17x body 16px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)

11 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: verified sweep Floor A11-001: #e91e63 promo text on white measures 4.35:1 at 16px, real failure
- a11y: verified sweep A11-004: 'Get started' is an unstyled browser button 82x21px, real
- a11y: keyboard operation: no menus, dialogs or custom widgets present; live keyboard test not run
- a11y: forms and errors: no forms on the page
- a11y: reflow at 320px: only 375 captured; at 375 nothing clips, but html { overflow-x: hidden } could hide overflow at narrower widths
- a11y: use of colour: no in-text links exist; gradient h1 is 32px bold (large text), stops #8b5cf6/#3b82f6 both exceed 3:1 on white
- slop: T-STOCK-ORDER: sections are hero, numbered feature head, one feature card, two-image gallery, testimonial: 4 stock sections, below the 5 threshold, so the generated read rests on T-DEFAULT-AGENT and clusters, not skeleton
- slop: No strengths recorded: nothing on the page is specific to the client
- slop: broken gallery images are missing source files, not capture blocks; judged as absent product evidence, not as a styling choice
- slop: copy voice: no contract or brand samples supplied (00-contract.md absent)
