# Unslop report: /home/claude/refs/design-taste/examples/after.html

**Verdict (draft): fix**. Profile: balanced. 9 Floor finding(s) open.

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (13x). body > header > div.container.hero-grid > div:nth-of-type(1) > p.kicker.mono:nth-of-type(1)  "Analytics for founders, not data teams"  
   Evidence: 3.53:1 against the background behind the text (10th-percentile pixel #f5f1ea, worst 3.53:1; text #e34a2b, 11px; needs 4.5:1). APCA Lc 58 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-002 Text size floors** (6x). body > header > div.container.hero-grid > div:nth-of-type(1) > p.kicker.mono:nth-of-type(1)  "Analytics for founders, not data teams"  
   Evidence: 38-character run at 11px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
3. **[Floor P0] A11-006 Controls have accessible names** (2x). hero 'Book a demo →'  
   Evidence: dom-1440.json: a.cta-text 'Book a demo →' has href '#pricing'. It does not book anything; it scrolls to pricing.  
   Fix: Point it at a booking page, or relabel 'See pricing'. (remedy: fix-a11y)
4. **[Floor P0] A11-007 Headings and landmarks** (2x). testimonial  
   Evidence: The quote is a blockquote but the attribution 'Sarah Chen — Founder, Stitchboard' sits outside it in a separate styled line with no figure/figcaption or cite, so the speaker is not programmatically tied to the quote.  
   Fix: <figure><blockquote>…</blockquote><figcaption>Sarah Chen, Founder, Stitchboard</figcaption></figure> (remedy: fix-a11y)
5. **[Floor P0] INT-001 No invented metrics** (1x). html > body > div.logos > div.container.logos-inner > div.logos-label.mono:nth-of-type(1)  "Trusted by 4,000+ indie teams"  
   Evidence: "Trusted by 4,000+" (invented-metrics/social-proof-counts, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
6. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > div.logos > div.container.logos-inner > div.logos-row:nth-of-type(2)  
   Evidence: page is 577px wide at a 375px viewport (sideways scroll); widest culprit 474px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
7. **[Floor P0] A11-005 Images have text alternatives** (1x). logo strip svgs  
   Evidence: Each customer name is a span with an unlabelled inline svg glyph (▲, ◠, ≡, ○, ›) and no aria-hidden; they are announced as unnamed images or skipped inconsistently.  
   Fix: <svg aria-hidden="true" focusable="false">…</svg> (remedy: fix-a11y)
8. **[Floor P0] INT-102 Never invent testimonials, quotes, reviews, ratings, review counts, awards or press lines** (1x). testimonial block, tiles 1440-01/02  
   Evidence: Failed T-FILLER: one large italic quote 'We found the exact step where users churned in a fifteen-minute session. Skittie paid for itself in one afternoon.' attributed to 'Sarah Chen — Founder, Stitchboard'. Sarah Chen is a stock generated name, Stitchboard has no link or logo, and the quote follows the polished testimonial formula (a number, a punchline).  
   Fix: [DATA NEEDED: a real customer quote with permission and a link], or remove the block. (remedy: None)
9. **[Floor P0] INT-101 Never invent a metric, customer count, uptime, speed multiple, saving or percentage the us** (1x). hero right column, tile 1440-00  
   Evidence: 'TRIAL → PAID 18.4%', 'MEDIAN TIME TO VALUE 9 min', 'CHURN, 90 DAYS 2.1%' with the note '— LIVE DATA, NO QUERIES WRITTEN'. Whose data is not stated: if it is a sample dashboard it is presented as fact, if it is Skittie's own it is unsourced. The sweep caught the logo-strip count; these three were not flagged.  
   Fix: Label it as an example ('Example: a 3-person SaaS, March') with a real screenshot, or remove. [DATA NEEDED: source of the figures] (remedy: None)
10. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). section sequence  
   Evidence: Hero with metric panel > logo strip (Acme, Fathom, Baseline, Radar, Promptly) > three equal feature rows 01-03 > single testimonial > three pricing tiers with 'PRO — MOST POPULAR' > centred CTA band 'Stop guessing. Start knowing.' > footer. Six stock sections in stock order; restyling them as hairline rows does not change the skeleton.  
   Fix: Cut the logo strip and CTA band; replace the three feature rows with one worked example (a funnel question answered end to end). (remedy: None)
11. **[Reflex P1] SLP-010 No template chrome glyphs** (8x). body > nav > div.container.nav-inner > div.nav-links:nth-of-type(2) > a:nth-of-type(1)  "01 — Features"  
   Evidence: template chrome (numbering-tokens): "01 — Features"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
12. **[Reflex P1] A11-004 Target size** (8x). body > nav > div.container.nav-inner > div.nav-links:nth-of-type(2) > a:nth-of-type(1)  "01 — Features"  
   Evidence: touch target 65x36px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
13. **[Reflex P1] SLP-002 No decorative section numbering** (5x). section.section:nth-of-type(1) > div.container > div.section-head:nth-of-type(1) > div > p.section-num.mono  "01 — Approach"  
   Evidence: section number "01 — Approach" (11px) beside heading "Everything you need to grow"; 5 on page  
   Fix: Remove the numbers or make them real steps. (remedy: fix-typeset)
14. **[Reflex P1] CPY-005 No slop diction** (5x). section.section:nth-of-type(1) > div.container > div.section-head:nth-of-type(1) > div > h2  "Everything you need to grow"  
   Evidence: "Everything you need to" (stock-phrases/openers, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
15. **[Reflex P1] SLP-001 No eyebrow labels above headings** (4x). body > header > div.container.hero-grid > div:nth-of-type(1) > p.kicker.mono:nth-of-type(1)  "Analytics for founders, not data teams"  
   Evidence: 11px label tracked 0.14em caps above 99px heading "Know exactly your users do."; 4 on page, budget 2  
   Fix: Promote the fact into the heading or delete the label (T-EYEBROW). (remedy: fix-typeset)

13 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Verified the sweep's #e34a2b contrast hits on tile 1440-00 (red kicker and white-on-red button text at 12px both look light); no disputes
- a11y: button behaviour: 'Start free' buttons have no form or href; whether a script handles them was not tested
- a11y: live keyboard tests not run
- slop: eyebrows, numbered labels, Acme logo, '4,000+' and em-dash counts: reported by the sweep, not repeated
- slop: brief: no 00-contract.md, so no declared editorial brand could be checked
