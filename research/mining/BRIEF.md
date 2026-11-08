# Mining brief (shared by all miners)

We are building "Unslop", a Claude skill system that audits and fixes AI-made design artifacts (web pages, app screens, slide decks, documents/PDF, diagrams/charts, social cards, email, video). Each audit rule becomes a "rule card".

Sources on disk (markdown, numbered concepts, `# Part` and `## N.` headings):
/home/claude/sources/{hallmark, ui-ux-pro-max, huashu-design, taste-skill, kami, awesome-design-patterns, agent-skills}.md

Method: use `grep -n` with keywords for your domains across ALL seven files, then Read the matching sections (offset/limit). Do not try to read files whole. Read enough to capture exact values.

Output: write ONE markdown file to the path given in your task. Structure:

## <Domain ID> <Domain name>
### <Sub-area>
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
- ID: domain prefix + number (SLP-001, TYP-001, CLR-001, TOK-001, LAY-001, CMP-001, CON-001, MOT-001, A11-001, ROB-001, CPY-001, DVZ-001, IMG-001, BRD-001, INT-001, WEB-, APP-, IOS-, AND-, SLD-, PRN-, SOC-, EML-, VID-, PRC- for process).
- Tier: Floor (a11y, truth, broken render; never waivable) / Reflex (slop default or craft error; waivable with reason) / Finish (polish).
- Check: M (mechanical, script-checkable from DOM/CSS/text/raster) / J (judgment) / H (hybrid).
- Sources: short names + section numbers, e.g. "hallmark §412, kami §77".

Rules:
- MERGE duplicates across sources into one row; list all sources on that row.
- Keep exact numbers. Prefer the stricter well-justified value; note disagreements in a final "Conflicts" list rather than picking silently.
- Skip pure house-style aesthetics that only fit one theme (put them in a short "Theme-specific, keep in library" list instead).
- Also capture NAMED TESTS / METHODS (e.g. "ghost deck test", "squint test") in a "Named tests" list: name, how to run it, pass condition, source.
- Target 60-150 rows per domain where material exists. Dense, no prose padding.
- Finish with: "Coverage notes" (what was thin), max 5 lines.

Return to the caller only: the file path, row counts per domain, and the 10 most valuable new rules (one line each). Do not paste the whole file back.
