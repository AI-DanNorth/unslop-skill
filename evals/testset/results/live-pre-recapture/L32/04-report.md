# Unslop report: https://design-system.service.gov.uk

**Verdict (draft): fix**. Profile: balanced. 1 Floor finding(s) open.

## Four-line read

- **For:** _(synthesize writes this)_
- **Works and stays:** _(synthesize)_
- **Reads generated:** _(synthesize)_
- **Broken:** _(synthesize)_

## Score

| Dimension | Score | Note |
|---|---|---|
| Concept | 9 | lens-concept: T-OWN-SYSTEM, T-KIND-FIT, T-ONE-SENTENCE, T-RIVAL-NAME and T-IDEA-CARRIES pass because the design system's home page is set entirely in its own components; it c |
| Hierarchy | 8 | lens-structure: T-FIVE-SECOND, T-HEADINGS-READ and T-LEFT-EDGES pass cleanly (18 text blocks on one start line); T-ANATOMY finds the three main entry points placed under the ne |
| Craft | 9 | lens-color (lowest of color 9, typography 9): T-COLOUR-SOURCE, T-PALETTE-ROLES, T-ACCENT-DOSAGE and T-SURFACE-LADDER pass: what was cut is everything but the brand blue, one ink and two pale grounds, with n |
| Accessibility | 5 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | 9 | lens-copy: T-FIVE-SECOND, T-RIVAL-NAME and T-LABEL-READ pass on the hero, every h2 and every 'Browse our ...' label; only the Community paragraph's 'a strong community sit |

Overall (draft): **4** (open Floor caps at 4)

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] TYP-004 The intended font actually renders** (1x). div.govuk-header.govuk-header--full-width-border:nth-of-type(1) > div.govuk-header__container.app-width-container > div.govuk-header__logo.app-header-logo:nth-of-type(1) > a.govuk-header__homepage-link > span.govuk-header__product-name  "Design System"  
   Evidence: declared "GDS Transport" but . drew the text  
   Fix: Fix the font load (path, format, font-display) or declare the face you actually ship. (remedy: fix-typeset)
2. **[Reflex P1] SLP-010 No template chrome glyphs** (5x). #\31 5-october-2026-weve-released-govuk-frontend-v660  "15 October 2026: We’ve released GOV.UK Frontend v6"  
   Evidence: template chrome (fake-versions): "15 October 2026: We’ve released GOV.UK Frontend v6.6.0"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
3. **[Reflex P1] A11-004 Target size** (3x). div.govuk-service-navigation.govuk-service-navigation--inverse:nth-of-type(2) > div.govuk-width-container > div.govuk-service-navigation__container > nav.govuk-service-navigation__wrapper.app-service-navigation__wrapper > button.govuk-service-navigation__toggle.govuk-js-service-navigation-toggle  "Menu"  
   Evidence: touch target 78x25px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
4. **[Reflex P1] CLR-001 Accent footprint within budget** (1x). first screen at 1280px  
   Evidence: saturated accent covers 50.7% of the fold (fail > 8%)  
   Fix: Keep accent on the primary action, current state and one focal element. (remedy: fix-colorize)
5. **[Reflex P1] CPY-001 Words per screen within budget** (1x). screen 3 (y 1800-2700) at 1440px  
   Evidence: 172 words on one 900px screen (fail > 143)  
   Fix: Cut qualifiers and repeated claims; move detail to a page that is for reading. (remedy: fix-distill)
6. **[Reflex P1] CPY-008 Adjective claim where a mechanism belongs** (1x). 'Community' section, 1440, tiles/1440-02.png  
   Evidence: Failed T-THREE-LINE: 'The GOV.UK Design System is for everyone that works on government services, with a strong community sitting behind it. It brings together the latest research, design and development from across government to make sure it's representative and relevant for its users.' 'strong', 'latest' and 'representative and relevant' cannot be pictured or proven false; the next sentence ('joining our discussions, events and co-design collaborations') says what the community does.  
   Fix: State the mechanism: how many departments contribute, or how a component moves from a community proposal to release. [DATA NEEDED: contributor count or contribution route] (remedy: fix-copy)
7. **[Reflex P1] LAY-016 Anatomy fits the visitor's job** (1x). "What's new" and "Get updates on the Design System" before "Styles / Components / Patterns", tiles 1440-00 to 1440-01, 1440px and 375px  
   Evidence: In dom-1440.json the h2 order is "What's new" (y=575), "Get updates on the Design System" (y=855), then "Styles", "Components", "Patterns" (y=1106). At 375 the three entry points start at y=1210, the second phone screen down.  
   Fix: Move the Styles, Components and Patterns row directly under the hero, and put "What's new" and the email sign-up after it. (remedy: fix-layout)
8. **[Reflex P1] LAY-011 Every section has mass** (1x). "Roadmap" section, tile 1440-03, 1440px  
   Evidence: The last section is a 36px "Roadmap" head over one two-line sentence with one link, about 170px of content between a divider and the footer.  
   Fix: Merge the roadmap link into the "Community" or "Support" section, where the upcoming-components link already sits. (remedy: fix-layout)
9. **[Reflex P2] A11-003 Visible focus everywhere** (1x). a "Get started"  
   Evidence: focus indicator visible but faint: 2.92:1 against the unfocused state (target 3.0:1, WCAG 2.4.13)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
10. **[Reflex P2] A11-007 Headings and landmarks** (1x). page  
   Evidence: first focusable element is button "Accept analytics cookies", not a skip link  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
11. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (8x). div.app-width-container > div.govuk-main-wrapper.govuk-main-wrapper--l > div.govuk-grid-row > div.govuk-grid-column-two-thirds-from-desktop > h2.govuk-heading-l:nth-of-type(2)  "Get updates on the Design System"  
   Evidence: last line is 29% of the measure at 375px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
12. **[Finish P3] LAY-002 Spacing on the scale** (1x). whole page  
   Evidence: 7 off-scale spacing values: 5px, 7px, 15px, 25px, 30px, 35px, 50px (e.g. #app-site-search__input)  
   Fix: Snap to the nearest step. (remedy: fix-layout)
13. **[Finish P3] A11-112 Every control has an accessible name** (1x). header logo link  
   Evidence: dom-1440.json: the homepage link's accessible name is 'Design System', while the visible label reads 'GOV•UK Design System' (the GOV.UK wordmark is an SVG excluded from the name). A speech user saying 'click GOV.UK Design System' may not match.  
   Fix: Give the SVG <title>GOV.UK</title> and role="img" (or aria-label="GOV.UK Design System" on the link) (remedy: None)
14. **[Finish P3] A11-143 Every field has a visible label above it** (1x). header search field  
   Evidence: The search combobox has an accessible name ('Search Design system') but its only visible label is the placeholder 'Search Design System' plus a magnifier icon (tile 1440-00).  
   Fix: Acceptable for a site search per common practice; optionally a visually persistent label or keep the icon + text that does not vanish on input (remedy: None)
15. **[Finish P3] SLP-221 Ban category-label section heads ("Features", "Our story", "Why us", "How it works"), "Mee** (1x). lower half section heads (tiles 1440-01 to 1440-03)  
   Evidence: T-FRESH-READER: 'Community', 'Support', 'Roadmap', 'Principles we follow' are category labels that fit any design system site. The bodies under them are specific ('maintained by a team at the Government Digital Service'), so the cost is only scannability.  
   Fix: "Join discussions, events and co-design sessions" (the task the section offers) (remedy: None)

1 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: sweep A11-003 'Get started focus indicator faint 2.92:1' — the GOV.UK focus style on the inverse (white) button on blue is a yellow fill with black underline, which reads clearly; 2.4.13 is AAA and the measured value is just under 3:1.
- a11y: keyboard operation of the 'Menu' toggle and search autocomplete: no live test
- a11y: motion: none observed
- color: T-DARK-MODE: the stylesheet contains a prefers-color-scheme: dark query, but the capture rendered the light scheme only, so any dark styling is not verified.
- color: CLR-009: #ffffff is the main ground and is GOV.UK's documented background colour, so it is not a finding (conflict C09).
- color: The accent_footprint hit (CLR-001) and the faint focus on "Get started" (A11-003) belong to the sweep and are not repeated.
- concept: 00-contract.md is absent; visitor mode read as Read (documentation home) from the page itself.
- concept: The cookie banner was dismissed by capture prep (manifest.prep); its design was not judged.
- copy: T-STATE-COPY: the email sign-up is a link, not a form on this page; async.json was not captured.
- copy: T-LONG-FORM: the copy sheet lists no long-form region.
- copy: Contract: no 00-contract.md in the run; judged as a Read/Operate documentation home with the GOV.UK style guide as the brand authority the page names.
- slop: cookie banner was dismissed by capture prep and is not part of the judgment
- slop: no 00-contract.md brief
- structure: T-STOCK-ORDER and T-COMPOSITION-RUN: a Read page, where composition variety does not apply.
- structure: words_per_screen (172 words on screen 3) and off_scale_spacing are sweep findings and are not repeated; 172 words is within what a Read page should carry.
- structure: The cookie banner was dismissed by capture prep (manifest prep).
- typography: T-FIGURES: the only figures are a date and a version number ("15 October 2026", "v6.6.0") that do not compare.
- typography: T-WIDOWS: the sweep's 8 widows hits at 375 are short last lines in body paragraphs; none is caused by a heading measure or a manual break.
- typography: T-LADDER at 375: the h1/h2 step falls to 1.19x, which TYP-009 allows below 1024 wide.
- typography: One paragraph at 1440 runs 76 characters a line, one over the 75 limit; not a finding.
