# Unslop report: https://vercel.com/design/guidelines

**Verdict (draft): fix**. Profile: balanced. 2 Floor finding(s) open.

## Four-line read

- **For:** _(synthesize writes this)_
- **Works and stays:** _(synthesize)_
- **Reads generated:** _(synthesize)_
- **Broken:** _(synthesize)_

## Score

| Dimension | Score | Note |
|---|---|---|
| Concept | 9 | lens-concept: T-OWN-SYSTEM, T-KIND-FIT, T-ONE-SENTENCE, T-RIVAL-NAME and T-IDEA-CARRIES pass for a Read page with one content type; it cut every marketing device (no hero ima |
| Hierarchy | 7 | lens-structure: T-HEADINGS-READ, T-LEFT-EDGES and T-FIVE-SECOND pass, but T-SQUINT finds the seven category heads set at body size, so the groups in an 8,815px list do not hold |
| Craft | 7 | lens-typography (lowest of color 9, typography 7): T-TYPE-SOURCE, T-FACE-ROLES, T-LEADING and T-MEASURE pass for a Read page; T-LADDER fails because section heads have no size or weight step over the text, and T |
| Accessibility | 1 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | 9 | lens-copy: T-RIVAL-NAME, T-THREE-LINE and T-TERMS pass on almost every item because each names a property, a number or a browser; only the intro's first sentence 'Interfac |

Overall (draft): **4** (open Floor caps at 4)

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-003 Visible focus everywhere** (11x). a "Vercel Home"  
   Evidence: no visible focus indicator (outline is set but nothing visible changes, so it is clipped or the colour of the ground: solid 2px rgb(16, 16, 16))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] A11-009 Zoom never blocked** (2x). meta viewport  
   Evidence: zoom disabled (maximum-scale=1 blocks zoom): width=device-width,initial-scale=1,maximum-scale=1  
   Fix: Remove the restriction. (remedy: fix-a11y)
3. **[Reflex P1] CPY-007 Opening line that survives the rival's-name swap** (1x). intro under the h1, 1440, tiles/1440-00.png  
   Evidence: Failed T-RIVAL-NAME on one line: 'Interfaces succeed because of hundreds of choices.' would open any design guideline page. The sentences after it are the page's own ('a living, non-exhaustive list', 'some specific to React/Next.js').  
   Fix: Open with the scope sentence that follows: what the list covers and for which stack. (remedy: fix-copy)
4. **[Reflex P1] A11-004 Target size** (12x). html.VEU71W_className.gb9FOq_className > body.tailwind.tailwind-no-preflight > div.min-h-screen.py-4:nth-of-type(2) > div.text-gray-900.max-w-\(--breakpoint-lg\) > a.focus-visible\:outline-2.focus-visible\:outline-focus  
   Evidence: touch target 20x17px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
5. **[Reflex P1] MOT-001 Motion CSS hygiene** (8x). .\!transition-all  
   Evidence: "transition-property: all !important": transition all animates layout and paint properties  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
6. **[Reflex P1] A11-007 Headings and landmarks** (3x). page  
   Evidence: 4 visible h1 elements (expected 1)  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
7. **[Reflex P1] CPY-001 Words per screen within budget** (1x). screen 2 (y 900-1800) at 1440px  
   Evidence: 292 words on one 900px screen (fail > 143)  
   Fix: Cut qualifiers and repeated claims; move detail to a page that is for reading. (remedy: fix-distill)
8. **[Reflex P1] CPY-002 Page length within budget** (1x). whole page  
   Evidence: 2226 words on the page (budget 675)  
   Fix: Read only hero and headings: if they tell the story, cut the rest. (remedy: fix-distill)
9. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). div.min-h-screen.py-4:nth-of-type(2) > div.text-gray-900.max-w-\(--breakpoint-lg\) > main > div.-mb-4 > ul.pl-5.mb-4:nth-of-type(8)  
   Evidence: "Instead of say ." repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
10. **[Reflex P1] CPY-018 Error copy that does not name the fix** (1x). 'Vercel-specific' > 'Copywriting', 'Default to positive language', 1440, lower 1440 tiles  
   Evidence: Failed T-STATE-COPY on the page's own example: 'Instead of "Your deployment failed," say "Something went wrong—try again or contact support."' The recommended line names neither what failed nor the cause, and the next rule on the page, 'Error messages guide the exit. Don't just state what went wrong—tell the user how to fix it', contradicts it.  
   Fix: Make the example name the object and the next step, in the same form as the API key example below it: what failed (the deployment), why if known, and where to go (the build logs). (remedy: fix-copy)
11. **[Reflex P1] LAY-006 Hierarchy survives the squint** (1x). category heads Interactions to Design, tiles 1440-00 to 1440-07, 1440px  
   Evidence: In dom-1440.json the seven category h2s ("Interactions" at y=317 to "Design" at y=6313) are 16px, the same size as the body and the bold rule leads under them ("Keyboard works everywhere.", "Clear focus."). The later part heads ("Vercel-specific", "Integrate with Agents", "Join Vercel") are 24px. Under the squint the category heads read at the same weight as each rule lead.  
   Fix: Set the category heads one step up (at least the 24px used for the part heads) or add space above them, so each category starts visibly. (remedy: fix-typeset)
12. **[Reflex P1] LAY-016 Anatomy fits the visitor's job** (1x). top of page, tile 1440-00, 1440px and 375px  
   Evidence: The page has no nav landmark and no list of categories; the first screen goes from the intro paragraph straight into the 119 rule items (the start-line count gives 119 blocks at x=380). The category heads are anchor links, so targets exist, but nothing links to them. The page is 8,815px tall at 1440 and 14,211px at 375.  
   Fix: Add a short list of the category anchors under the intro, or a sticky list in the empty left margin at 1440 (the column starts at x=360). (remedy: fix-layout)
13. **[Reflex P1] TYP-020 Weight steps are clear** (1x). section heads (a elements "Interactions", "Layout", "Content", "Forms", "Performance", "Design", "Copywriting"), 1440 and 375 (tiles/1440-00.png, middle)  
   Evidence: dom-1440.json gives every section head at 16px, weight 500, white, 24px line height. The bold lead-in of each rule below it ("Keyboard works everywhere.") is also 16px, at weight 550 in #ededed. The body text is 16px at 400. The type table finds only two size steps on the page: the 32px h1 and 16px for everything else. A section head is therefore lighter than the rule titles it groups, and only the space above it marks it.  
   Fix: Section heads one clear step up (for example 20 to 24px at weight 600), so the h1, section and rule levels each have their own size (remedy: fix-typeset)
14. **[Reflex P2] TYP-002 Sizes on a declared ladder, families limited** (1x). whole page  
   Evidence: 3 font families render: Geist, Geist Mono, GeistSans  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
15. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (1x). div.min-h-screen.py-4:nth-of-type(2) > div.text-gray-900.max-w-\(--breakpoint-lg\) > main > div.-mb-4 > p.mb-4.leading-7:nth-of-type(1)  "Interfaces succeed because of hundreds of choices."  
   Evidence: last line is 12% of the measure at 1280px (3 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)

1 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 2 type roles
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 other request(s) blocked, e.g. script https://vercel.com/vc-ap-b3331f/_next/static/immutable/chunks/2gg0fzzdd7hc9.js
- a11y: dom-1440 records empty text for the h2 elements (#interactions etc.); the visible labels exist, so this is treated as a capture limitation, not a missing name.
- a11y: Copy button next to the install command (32x32, classes outline-none) was not focus-tested live.
- a11y: The install command is clipped at 1440 ('--skill web-design-guide...'); horizontal scroll inside a code block is allowed under 1.4.10, keyboard scrollability not tested.
- color: T-LINE-DELETION: the page has no repeated rules or borders apart from the code-chip outlines, which mark code, so the test has nothing to remove.
- color: The light theme: the stylesheet declares color-scheme and a theme class, but the capture rendered the dark scheme only, so the light theme is not verified.
- color: CLR-009: #ffffff on the section headings is the documented --geist-foreground token, so it is not a finding (conflict C09).
- color: The focus_ring Floor hits (A11-003) belong to the sweep and lens-a11y and are not repeated.
- concept: 00-contract.md is absent; visitor mode read as Read (reference guidelines) from the page itself.
- concept: T-DELETE-PICTURE was skipped: the page has no lead image, which suits its job.
- concept: One script was blocked in capture (manifest.network); the anchor-link icons that appear on hover were not judged.
- copy: T-LONG-FORM: ran on the one region the copy sheet lists (3 paragraphs, 95 words): 0 passive, 0 hedges, 0 vague attributions, 2 -ly adverbs; no finding. The page is a reference list, not running prose.
- copy: T-STATE-COPY on live states: no form on the page and async.json was not captured; only the example error copy in the text was judged.
- copy: Sweep: the repeated_label hit 'Instead of say .' comes from element text with the inline quoted examples stripped; bodyText shows the full examples, so it was not used as evidence.
- copy: T-TERMS: '10 MB' and '10MB' appear because the rule quotes the wrong form as its counter-example; 'AGENTS'/'agents' is the file name AGENTS.md; no finding.
- copy: Contract: no 00-contract.md in the run; judged as a Read (docs) page.
- slop: disputed: INT-005 placeholder_residue hits ('Placeholders signal emptiness.', 'Use consistent placeholders.') are guideline text about form placeholders, not leftover placeholder copy.
- slop: Page length (2,226 words, sweep CPY-002) is appropriate for a reference document; not treated as slop.
- structure: T-STOCK-ORDER and T-COMPOSITION-RUN: a Read page, where composition variety does not apply.
- structure: words_per_screen (292 words on screen 2) and page_words (2,226) are sweep findings; that density fits a reference list, so T-DENSITY-FIT passes.
- structure: One script chunk was blocked during capture (manifest network); copy buttons and similar interactions were not checked.
- typography: T-FONT-RENDERED: fonts.json lists both "Geist" and "GeistSans" as drawn faces; they are the same family under two names, and the sweep's type_ladder family count of 3 includes that duplicate.
- typography: T-HEADLINE-FIT: the only heading is the 24-character h1 on 1 line at 1440 and 2 at 375; the section heads are links, not headings, which is the structure lens's to judge.
- typography: T-FIGURES: no figures compare on the page.
- typography: T-MEASURE: 4 paragraphs run over 75 characters at 1440 (maximum 87), none at 88 or more; not a finding.
- typography: Wrapped controls in the type table are inline links in running text, which may wrap.
