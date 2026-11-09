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
| Concept | _lens_ | judgment lens required |
| Hierarchy | _lens_ | judgment lens required |
| Craft | _lens_ | judgment lens required |
| Accessibility | 5 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

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
6. **[Reflex P2] A11-003 Visible focus everywhere** (1x). a "Get started"  
   Evidence: focus indicator visible but faint: 2.92:1 against the unfocused state (target 3.0:1, WCAG 2.4.13)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
7. **[Reflex P2] A11-007 Headings and landmarks** (1x). page  
   Evidence: first focusable element is button "Accept analytics cookies", not a skip link  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
8. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (8x). div.app-width-container > div.govuk-main-wrapper.govuk-main-wrapper--l > div.govuk-grid-row > div.govuk-grid-column-two-thirds-from-desktop > h2.govuk-heading-l:nth-of-type(2)  "Get updates on the Design System"  
   Evidence: last line is 29% of the measure at 375px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
9. **[Finish P3] LAY-002 Spacing on the scale** (1x). whole page  
   Evidence: 7 off-scale spacing values: 5px, 7px, 15px, 25px, 30px, 35px, 50px (e.g. #app-site-search__input)  
   Fix: Snap to the nearest step. (remedy: fix-layout)
10. **[Finish P3] A11-112 Every control has an accessible name** (1x). header logo link  
   Evidence: dom-1440.json: the homepage link's accessible name is 'Design System', while the visible label reads 'GOV•UK Design System' (the GOV.UK wordmark is an SVG excluded from the name). A speech user saying 'click GOV.UK Design System' may not match.  
   Fix: Give the SVG <title>GOV.UK</title> and role="img" (or aria-label="GOV.UK Design System" on the link) (remedy: None)
11. **[Finish P3] A11-143 Every field has a visible label above it** (1x). header search field  
   Evidence: The search combobox has an accessible name ('Search Design system') but its only visible label is the placeholder 'Search Design System' plus a magnifier icon (tile 1440-00).  
   Fix: Acceptable for a site search per common practice; optionally a visually persistent label or keep the icon + text that does not vanish on input (remedy: None)
12. **[Finish P3] SLP-221 Ban category-label section heads ("Features", "Our story", "Why us", "How it works"), "Mee** (1x). lower half section heads (tiles 1440-01 to 1440-03)  
   Evidence: T-FRESH-READER: 'Community', 'Support', 'Roadmap', 'Principles we follow' are category labels that fit any design system site. The bodies under them are specific ('maintained by a team at the Government Digital Service'), so the cost is only scannability.  
   Fix: "Join discussions, events and co-design sessions" (the task the section offers) (remedy: None)
13. **[Finish P3] CPY-001 Words per screen within budget** (1x). screen 3 at 1440 ('Principles we follow', 'Community')  
   Evidence: 172 words on one screen (sweep); 'Principles we follow' and 'Community' are two paragraphs each of link-dense prose that would scan faster as short lists of links.  
   Fix: Keep the first sentence; list the three destinations as links (remedy: fix-distill)

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
- slop: cookie banner was dismissed by capture prep and is not part of the judgment
- slop: no 00-contract.md brief
