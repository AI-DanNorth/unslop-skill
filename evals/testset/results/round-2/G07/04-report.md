# Unslop report: /home/claude/refs/ux-ui-agent-skills/examples/sample-app/preview.html

**Verdict (draft): fix**. Profile: balanced. 3 Floor finding(s) open.

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
| Integrity | 9 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-124 Build the focus ring from outline, never a border change** (1x). .btn:focus-visible, #name, #notify (focus.json stops 00-04)  
   Evidence: focus.json shows outline: none on every control with the ring drawn only as box-shadow (0 0 0 2px #fff, 0 0 0 4px #2563eb). The ring is visible in the normal render (focus/03-on.png) but box-shadow is removed in Windows forced-colours mode, leaving no focus indicator.  
   Fix: .btn:focus-visible { outline: 2px solid transparent; outline-offset: 2px; box-shadow: var(--shadow-focus-ring); } (transparent outline becomes visible in forced-colours) or use outline: 2px solid var(--color-action-primary); outline-offset: 2px (remedy: None)
2. **[Floor P0] A11-168 Never convey information by colour alone** (1x). KPI deltas (Revenue, Active users, Churn, NPS)  
   Evidence: Direction is carried by arrow icon plus colour plus visually hidden 'increase'/'decrease' text (bodyText includes "12% increase"), so 1.4.1 is met for direction. But sentiment is carried by colour only and is wrong for Churn: a decrease shown in the error red. A colour-relying reader is told churn got worse.  
   Fix: Colour by sentiment and add a visible word: "↘ 2% (improved)"; sr text "down 2%, an improvement" (remedy: None)
3. **[Floor P0] A11-115 Expose correct state attributes: aria-expanded on menu/accordion triggers, aria-pressed/ar** (1x). #themeBtn "Dark"  
   Evidence: The theme toggle is a plain button whose label is "Dark"; no role or pressed state was captured (role: null). Out of context a screen-reader user hears "Dark, button" and cannot tell whether it is the current theme or the action, nor its state after activation.  
   Fix: <button id="themeBtn" aria-pressed="false">Dark theme</button>, toggling aria-pressed with the theme; or label it as the action "Switch to dark theme" (remedy: None)
4. **[Reflex P1] SLP-182 Never use a framework's default palette as tokens** (1x). :root tokens, whole page  
   Evidence: Every surface and text token is a stock Tailwind swatch (#111827, #4b5563, #e5e7eb, #6b7280, #f9fafb) with blue-600 #2563eb as the only action colour and Inter as the only family. Failed T-DEFAULT-AGENT: 'analytics dashboard with light/dark theme' in any agent yields this exact palette and face. The sweep flagged the swatches; the judgment here is that nothing in the skin was chosen.  
   Fix: Derive the action colour and greys from the product's own brand [DATA NEEDED: brand colour and display face]; keep the token structure, which is good, and change only the values (remedy: None)
5. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (4x). :root --color-text-primary  
   Evidence: token --color-text-primary: #111827 is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)
6. **[Reflex P1] A11-004 Target size** (4x). #themeBtn  
   Evidence: touch target 86x40px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] SLP-010 No template chrome glyphs** (3x). body > div.container:nth-of-type(1) > div.topbar > div:nth-of-type(1) > p.subtle  "Last 30 days · one shared theme · light + dark"  
   Evidence: template chrome (middot-chains): "Last 30 days · one shared theme · light + dark"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
8. **[Reflex P1] A11-007 Headings and landmarks** (2x). page  
   Evidence: no <main> landmark  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
9. **[Reflex P1] TYP-003 No UI text faces as display type** (1x). body > div.container:nth-of-type(1) > div.topbar > div:nth-of-type(1) > h1.page-title  "Analytics"  
   Evidence: display text at 30px set in Inter, a UI text face  
   Fix: Try Archivo, Anton, Schibsted Grotesk (remedy: fix-typeset)
10. **[Reflex P1] INT-007 Stat bands need sources** (1x). body > div.container:nth-of-type(1) > section.grid:nth-of-type(1) > div.card:nth-of-type(2) > div.card__value:nth-of-type(2)  "3,910"  
   Evidence: stat band of 3 unsourced figures: 3,910, 1.8%, 62  
   Fix: Cite each figure, use only supplied facts, or remove the band. (remedy: fix-copy)
11. **[Reflex P1] SLP-218 Ban staged reveals and self-reference ("The result?", "Why does this matter?", "this secti** (1x). topbar subline under h1 'Analytics', and Settings section lede, 1440px and 375px  
   Evidence: Subline reads "Last 30 days · one shared theme · light + dark"; Settings lede reads "Same theme, same primitives, second page." Both describe the demo's construction to a developer, not anything a user of this analytics screen needs. Failed T-FRESH-READER: these are the two lines a fresh reader flags as fitting any design-system sample.  
   Fix: "Last 30 days, to 09:00 UTC today" under Analytics; drop the Settings lede or replace with what the settings govern, e.g. "Name shown on exported reports" [DATA NEEDED: what the display name is used for] (remedy: None)
12. **[Reflex P1] DVZ-103 Show one value as a stat tile (figure + worded qualifier), never a one-bar chart** (1x). Churn card, 1440px row 2 centre  
   Evidence: Churn 1.8% shows a red down-arrow "2%" (class .down, --color-feedback-error-icon). A fall in churn is good news, yet it is coloured as the error state; the colour is tied to arrow direction, not to whether the change is good.  
   Fix: Map colour to sentiment, not direction: give the delta a data-sentiment="good|bad" and render churn down in the success colour; label it "down 0.04 pts" or "down 2% (better)" (remedy: None)
13. **[Reflex P1] SLP-160 Ban the KPI wall: a greeting above four stat cards, or six gauges.** (1x). metric grid, 1440px y 124-424  
   Evidence: T-STOCK-ORDER: title + action buttons, KPI hero, three equal stat cards (repeat(3,1fr)), settings card, footnote. The three-up stat row (Active users / Churn / NPS) with identical card, radius and shadow is the KPI-wall pattern, partly redeemed by the full-width revenue hero with its explanatory note. Only 2 stock sections, so the skeleton itself does not cap the read.  
   Fix: Give each secondary metric its context the way Revenue has one (e.g. a one-line definition or the period's absolute change), or set them as a compact inline row rather than three identical cards (remedy: None)
14. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (1x). html > body > div.container:nth-of-type(1) > section.section:nth-of-type(2) > p.subtle  "Same theme, same primitives, second page."  
   Evidence: last line is 15% of the measure at 375px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
15. **[Finish P3] A11-150 Every field has name, correct type, inputmode, autocomplete.** (1x). #name (Display name)  
   Evidence: dom-1440 field record: name: "", autocomplete: null for a personal-name field.  
   Fix: <input id="name" name="display_name" type="text" autocomplete="nickname"> (remedy: None)

3 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Delete-account dialog keyboard behaviour (Escape, focus trap, focus return) and its role/aria-modal: the modal is a div.modal and role attributes were not captured; no live Playwright run in this review
- a11y: dark theme contrast (A11-169): only light theme captured
- a11y: error handling for the DELETE confirmation input: not submitted
- slop: dark theme render: only the light theme was captured
- slop: brand: no contract or brand colours supplied, so the Tailwind palette cannot be checked against a brief
