---
name: lens-a11y
description: Phase 3 accessibility lens. Covers the WCAG 2.2 AA judgments the sweep cannot measure (alt text quality, link purpose, reading and focus order, use of colour, error handling, motion, reflow, keyboard traps) and verifies sweep Floor hits are real. Use inside an Unslop run, or when the user asks for an accessibility review of a captured page.
---

# Lens: accessibility (D10, WCAG 2.2 AA floor)

Accessibility findings are Floor unless stated: never waivable. The sweep already measured contrast on real pixels, text-size floors, focus visibility, target size, names, labels, alt presence, headings, landmarks, lang, title, zoom blocking, reduced motion and hidden content. Your job is what needs a reader and a keyboard.

## Inputs

`00-contract.md`, `01-evidence/` (`dom-*.json`, `focus.json` with `focus/*.png`, screenshots), `02-mechanical.json` (A11, ROB hits), `rules/A11.yaml` (11 curated cards plus about 90 mined drafts with WCAG and source references).

## Checks (record each in `tests_run`)

1. **Verify the sweep's Floor hits.** Open the screenshot region for 3 to 5 of them. If one is a false positive (for example a decorative text layer), add it to `not_investigated` as "disputed: <reason>" so `synthesize` can note it; never delete it.
2. **Alt text quality (1.1.1).** For each content image in `dom-1440.json`, does the alt say what the image tells the reader? Decorative images should have `alt=""`.
3. **Link and button purpose (2.4.4, 2.5.3).** Read accessible names out of context: does each say where it goes or what it does? Does the visible label appear in the accessible name?
4. **Focus order (2.4.3).** Read `focus.json` in order against the screenshot: does focus follow the visual reading order? Any jumps, traps or invisible stops (focus on off-screen elements)?
5. **Keyboard operation (2.1.1, 2.1.2).** For menus, dialogs, carousels, tabs and custom controls you can see, run a short Playwright check: open with Enter or Space, close with Escape, and confirm Tab leaves. Record the script output as evidence.
6. **Use of colour (1.4.1).** Are links in body text distinguishable without colour (underline or 3:1 against surrounding text)? Are states, errors or chart series shown by colour alone?
7. **Non-text contrast (1.4.11).** Input borders, icons that carry meaning and focus rings against adjacent colours: 3:1.
8. **Reflow (1.4.10) and text spacing (1.4.12).** At 320px (capture `full` includes it): no two-direction scrolling, no clipped text. Optionally inject `* { line-height: 1.5 !important; letter-spacing: .12em !important; word-spacing: .16em !important }` and look for clipping.
9. **Forms and errors (3.3.1, 3.3.3).** Submit empty and invalid values: is each error text, next to the field, programmatically tied, and specific about the fix?
10. **Motion and timing (2.2.2, 2.3.1).** Anything that moves for more than 5 seconds needs pause; nothing flashes more than 3 times a second.
11. **Headings and landmarks (1.3.1, 2.4.6).** Do headings describe their sections? Is the main content in `main`?

## Writing findings

- `$RUN/03-lenses/a11y.json`, shape as `skills/unslop/templates/lens-output.json`.
- Cite the WCAG success criterion in `why` (for example "WCAG 2.2 2.4.4 Link Purpose").
- Rule ids: the matching A11 card. If only a draft card fits, use its id; if none fits, use `A11-001`-style nearest curated card and say so.
- Up to 10 findings, Floor first. Do not repeat sweep hits.
- Be specific in `after`: the exact attribute, element or CSS to add.

## Gate

`$RUN/03-lenses/a11y.json` exists, parses, and every finding names a success criterion and evidence.
