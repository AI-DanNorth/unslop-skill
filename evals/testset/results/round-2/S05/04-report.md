# Unslop report: /home/claude/refs/design-taste/examples/before.html

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
| Integrity | 3 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). html > body > nav > div.container.nav-inner > button.nav-cta  "Get Started Free"  
   Evidence: 4.33:1 against the background behind the text (10th-percentile pixel #7f5ff4, worst 4.30:1; text #ffffff, 14px; needs 4.5:1). APCA Lc 75 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] INT-001 No invented metrics** (2x). html > body > div.logos:nth-of-type(1)  "Trusted by 4,000+ indie teams"  
   Evidence: "Trusted by 4,000+" (invented-metrics/social-proof-counts, fail)  
   Fix: Use the real figure with its source, a [DATA NEEDED] slot, or nothing. (remedy: fix-copy)
3. **[Floor P0] A11-006 Controls have accessible names** (2x). nav (Features, Pricing, Docs, Blog) and footer (Privacy, Terms, Twitter, Status)  
   Evidence: dom-1440.json: all 8 <a> elements have no href, so none appears in focus.json (the 7 focus stops are all buttons). A keyboard user cannot reach the page's navigation or legal links at all.  
   Fix: <a href="#features">Features</a>, <a href="#pricing">Pricing</a>, real URLs for Docs, Blog, Privacy, Terms, Twitter, Status (remedy: fix-a11y)
4. **[Floor P0] TYP-004 The intended font actually renders** (1x). section.features:nth-of-type(1) > div.container > div.feature-grid > div.feature-card:nth-of-type(1) > div.feature-icon  "📊"  
   Evidence: declared "Inter" but Noto Color Emoji drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
5. **[Floor P0] ROB-003 No horizontal overflow** (1x). body > section.pricing:nth-of-type(3) > div.container > div.price-grid > div.price-card:nth-of-type(3)  
   Evidence: page is 499px wide at a 375px viewport (sideways scroll); widest culprit 145px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
6. **[Floor P0] A11-005 Images have text alternatives** (1x). testimonial rating and hero chart, 1440 tiles 0-2  
   Evidence: The rating is five "★" characters with no text equivalent (read as "black star" five times); the hero bar chart is eight unlabeled divs with no role, title or alt, so assistive tech gets nothing or noise.  
   Fix: <div class="stars" role="img" aria-label="Rated 5 out of 5">; chart wrapper role="img" aria-label="Example weekly active users chart" or aria-hidden="true" if decorative (remedy: fix-a11y)
7. **[Floor P0] INT-002 No default cast or fake brands** (1x). logo strip and testimonial, 1440 tiles 1-2  
   Evidence: Logo strip is styled text of invented or placeholder brands: "ACME ▸ FATHOM ▸ BASELINE ▸ RADAR ▸ PROMPTLY" (Acme is the canonical placeholder company; Fathom is a real analytics competitor). Testimonial: "— Sarah Chen, founder of Stitchboard" with ★★★★★, a default-cast name with no photo, link or date. The sweep's default_names detector did not fire.  
   Fix: [DATA NEEDED: real customer names with permission and a real quote], or remove both blocks (remedy: fix-copy)
8. **[Reflex P1] CPY-148 Ban stock phrases** (1x). h1, section h2s and CTA band  
   Evidence: Failed T-RIVAL-NAME: "Know exactly what your users do.", "Everything you need to grow", "Simple pricing", "Stop guessing. Start knowing." all stay true under PostHog, Mixpanel or Amplitude. T-FRESH-READER generic lines: these four plus "Join 4,000+ founders who understand their product."  
   Fix: Build the head from the one specific idea already on the page: analytics for indie founders without a data team or "a second mortgage", e.g. a head that states the price-and-setup difference (remedy: None)
9. **[Reflex P1] SLP-151 Hero template tells: a pill or label above the headline, a gradient blob, an empty coloure** (1x). hero, 1440 tile 0  
   Evidence: Pill above the headline "New · AI Insights ✨" (sparkle emoji, an unrelated AI feature announcement on an analytics page), a two-tone indigo-violet-fuchsia gradient h1, a lavender radial wash behind it, all centred (SLP-150).  
   Fix: Drop the pill and the wash; set the h1 in solid ink; left-align the hero with the product view beside it (remedy: None)
10. **[Reflex P1] SLP-013 No emoji as icons** (3x). section.features:nth-of-type(1) > div.container > div.feature-grid > div.feature-card:nth-of-type(1) > div.feature-icon  "📊"  
   Evidence: emoji used as an icon: "📊" (3 on page)  
   Fix: Use a consistent icon set with labels, or no icon. (remedy: fix-quieter)
11. **[Reflex P1] A11-007 Headings and landmarks** (3x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
12. **[Reflex P1] SLP-007 No stock gradient pairs** (2x). html > body > header > h1  "Know exactly what your users do."  
   Evidence: gradient hue span 45°: #6366f1, #8b5cf6, #d946ef  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
13. **[Reflex P1] CLR-001 Accent footprint within budget** (1x). first screen at 1280px  
   Evidence: saturated accent covers 10.2% of the fold (fail > 8%)  
   Fix: Keep accent on the primary action, current state and one focal element. (remedy: fix-colorize)
14. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (1x). whole page  
   Evidence: 3 stock framework colours used directly: #0f172a, #6366f1, #64748b  
   Fix: Define brand tokens and use them instead of framework defaults. (remedy: fix-colorize)
15. **[Reflex P1] TYP-001 Clear type hierarchy** (1x). h3 vs body  
   Evidence: h3 18px is only 1.12x body 16px (min 1.25x)  
   Fix: Adopt a scale (1.25 to 1.5) and assign roles to steps. (remedy: fix-typeset)

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
- a11y: Sweep contrast hits spot-checked: the logo-strip line "TRUSTED BY 4,000+ INDIE TEAMS" (#94a3b8 on white, 2.56:1) and the badge text are visibly faint in tile 1440-01; the button hits at 4.3:1 on the gradient are plausible. None disputed.
- a11y: Sweep ROB-003 overflow at 375 (pricing card 3 forces 499px) not re-checked beyond the sweep.
- a11y: Keyboard operation: no menus, dialogs or tabs; no live Playwright run.
- slop: Inter was shimmed in capture; render assumed close to intended.
