# Unslop report: /home/claude/refs/kami/site/assets/demos/demo-musk-resume.html

**Verdict (draft): fix**. Profile: balanced. 4 Floor finding(s) open.

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
| Integrity | 4 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-007 Headings and landmarks** (1x). whole document  
   Evidence: dom-794.json contains no h1-h6 elements and no landmarks: the name "Elon Musk", the section titles (Summary, Experience, Open Source & Indie Work, Judgment & Conviction, Public Impact, Core Skills, Education) and the company names are all styled divs/spans.  
   Fix: <h1> for the name, <h2> for each section title, <h3> for each company row head; the PDF export then carries tagged headings and bookmarks (remedy: fix-a11y)
2. **[Floor P0] A11-006 Controls have accessible names** (1x). Public Impact and writing/talks links, tile 2  
   Evidence: Link names do not match destinations: "@elonmusk" -> https://tesla.com/blog, "Master Plan Part Deux" -> https://youtube.com/ted, "First Principles Thinking in Engineering" -> https://spacex.com.  
   Fix: Point each link at the item it names, or remove the <a> and keep plain text (remedy: fix-a11y)
3. **[Floor P0] INT-135 Ban fake contact data: example.com/.example addresses printed as real, phone numbers of ze** (1x). header contact line, tile 0  
   Evidence: "em@example.com" printed as the contact email beside a real handle (x.com/elonmusk) and a real city (Austin, TX), linked as mailto:em@example.com.  
   Fix: [DATA NEEDED: real contact email] or remove the field (remedy: None)
4. **[Floor P0] INT-151 Give each fact one value and one wording everywhere it appears** (1x). links in Public Impact and Open Source sections, tile 2  
   Evidence: dom-794.json hrefs: "@elonmusk" -> https://tesla.com/blog; "Master Plan Part Deux" -> https://youtube.com/ted; "First Principles Thinking in Engineering" -> https://spacex.com. Each link names one thing and opens another.  
   Fix: href="https://x.com/elonmusk"; link each talk and post to its own URL, or unlink it: [DATA NEEDED: source URLs] (remedy: None)
5. **[Reflex P1] SLP-010 No template chrome glyphs** (5x). html > body > div.header:nth-of-type(1) > div.contact:nth-of-type(2) > span.role:nth-of-type(1)  "Founder · Chief Engineer · CEO"  
   Evidence: template chrome (middot-chains): "Founder · Chief Engineer · CEO"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
6. **[Reflex P1] CPY-006 No repeated labels inside a card** (1x). html > body > section:nth-of-type(2)  
   Evidence: "founder" repeated 3 times in one container  
   Fix: Say it once. (remedy: fix-copy)
7. **[Reflex P1] A11-001 Text contrast on real pixels** (1x). inline emphasis in impact rows and skills, tiles 0-3  
   Evidence: Non-link phrases ("400+ launches", "7,000+ satellites", "7M+ vehicles delivered", "122 days", "first reusable orbital booster") are set in the same navy rgb(27,54,93) with no underline as the real links "SpaceX" and "Tesla"; neither is underlined.  
   Fix: Underline real links (text-decoration: underline; text-underline-offset: 2px) and render emphasis as font-weight: 600 in body ink (remedy: fix-a11y)
8. **[Reflex P1] INT-007 Stat bands need sources** (1x). metric row under the name, tile 0  
   Evidence: Four bare figures with no dates or sources: "30 yrs building hard tech", "6 cos founded / co-founded", "400+ Falcon launches", "7M+ Tesla vehicles". The sweep's stat_band did not fire (print profile). Later lines add more unsourced valuations: "Valued at $350B (2024)", "* $900B", "xAI valued at $50B".  
   Fix: Date each figure and keep the source in a footnote ("Falcon 9 launches to [DATA NEEDED: as-of date], source: [DATA NEEDED]"), or drop the band; the experience rows already carry the numbers (remedy: fix-copy)
9. **[Reflex P1] INT-105 Ban invented specifics dressed as authenticity ("6:12 a.m., from the window of Room 9", "B** (1x). Experience timeline and xAI impact row, tiles 0-1  
   Evidence: Borrowed-authority lines that fail T-THREE-LINE (not falsifiable, attributed to no one): "Built physical infrastructure others called impossible.", "Colossus in 122 days, a pace the industry called implausible", "Every major OEM announced EV transition within 5 years of Model 3", "The industry assumption that rockets were expendable was gone within 24 months."  
   Fix: State the fact and stop: "Colossus: 100K H100 GPUs, 122 days from concept to training." (remedy: None)
10. **[Reflex P1] CPY-208 Keep a true count from the client's set** (1x). "Open Source & Indie Work" section, tiles 1-2  
   Evidence: The section heading promises open-source and indie work; its content is a philosophy line ("First-principles founder across hard tech. Approach: ..."), two company rows (SpaceX $350B, Tesla $900B) and a Falcon 9 landing callout. Its right-hand meta repeats the Experience meta ("1995 - present · Founder-engineer across six hard-tech companies"). "125 followers on GitHub" is the only open-source fact.  
   Fix: Cut the section, or rename it to what it holds ("Approach") and drop the repeated company rows (remedy: None)
11. **[Finish P3] A11-008 Language and title set** (1x). document metadata  
   Evidence: Title is "Elon Musk · Resume"; no description or author metadata was captured for PDF export.  
   Fix: Add <meta name="author" content="Elon Musk"> and <meta name="description">; export with document title shown in the PDF title bar (PRN-121) (remedy: fix-a11y)
12. **[Finish P3] TYP-165 Never set text ≤15px in uppercase, small caps or tracked past 0.03em (labels, captions, th** (1x). row labels ROLE / ACTIONS / IMPACT and Core Skills labels, tiles 0-3  
   Evidence: T-LABEL-TRANSFORM: 12px uppercase tracked navy labels repeat 12 times (ROLE/ACTIONS/IMPACT x4) and the skill labels wrap mid-phrase in caps ("CAPITAL · CRISIS / MGMT", "MANUFACTURING / · SCALE", with the middot starting a line). In sentence case at body weight the labels read as well and stop wrapping.  
   Fix: Sentence-case labels, untracked, 'Capital and crisis management'; widen the label column to fit the longest label on one line (remedy: None)
13. **[Finish P3] INT-151 Give each fact one value and one wording everywhere it appears** (1x). date ranges throughout  
   Evidence: Three date styles: "1995 - Present" and "1995 - present" (hyphen, mixed case), "2016.07" for writing and talks, "1992 - 1997" for education.  
   Fix: One format with an en dash: "1995–present", "Jul 2016" (remedy: None)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- accent_footprint (CLR-001): skipped: disabled by profile
- flat_hierarchy (TYP-001): skipped: only 0 type roles
- dead_band (LAY-004): skipped: disabled by profile
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: disabled by profile
- focus_ring (A11-003): skipped: disabled by profile
- targets (A11-004): skipped: disabled by profile
- headings_landmarks (A11-007): skipped: disabled by profile
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- phone_parity (ROB-002): skipped: disabled by profile
- overflow (ROB-003): skipped: disabled by profile
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Sweep contrast was not verified on pixels (no background render); computed ratios above are from declared colours on a flat ground.
- a11y: Focus order and keyboard: print medium, focus checks disabled by profile.
- a11y: Tagged-PDF output itself was not inspected; only the HTML source of the export.
- a11y: The middot separators at 1.13:1 are decorative; not reported.
- slop: Factual accuracy of claims about a real person was not verified (no supplied facts); findings flag unsourced framing, not truth.
- slop: The capture is a screen render: @page margins (11mm 13mm) do not apply on screen, so the flush-left text is a capture artefact; Charter fell back to Liberation Serif, so type colour differs from the intended render.
- slop: Page balance (PRN-117) not measured without a paged PDF render.
