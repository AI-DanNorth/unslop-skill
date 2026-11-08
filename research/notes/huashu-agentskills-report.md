# agent-skills (Vercel-style rule packs) — condensed
- NOT SKILL.md structure doc. Rule packs: view transitions, writing, React composition, React Native, perceived perf, React perf.
- Rule schema: id, rule, why, incorrect, correct, impact (CRITICAL/HIGH/MEDIUM/LOW), check_type mechanical|judgment, values, applies_when predicate (version gates).
- Lifecycle per skill: inventory → classify into table/map → check in priority order → verify walk.
- Motion semantics vocabulary (morph=same thing deeper; slide=hierarchy; crossfade=lateral; slide-up=data arrived). Timing exit 150/enter 210/move 400.
- AI-writing tells list (summary transitions, fragments, spec-sheet voice, cold opens, personified software, template framing, "not X it's Y").
- Evidence doctrine: never act w/o observed signal; same inputs same outputs; publish skipped & why; never invent numbers; 5-15 findings; observations ≠ actions.
- Recommendation shape: What (≤80 chars) / Why (evidence w/ line refs) / Fix (steps + before/after) / Verify / risk. Quality floor: specificity, actionability, grounding, evidence 0-1; drop <0.55.
- Report transparency: Not investigated (why), investigated no change, strengths, data gaps.
- Site-type router table (P52).
- Proposed D18 engineering/code quality (optional pack).

# huashu-design — condensed
- Full design-agent OS. Stages 0-9 (verify facts → understand → assets → 5 form questions per screen → folder → alignment pass → full pass → polish → verify → deliver + ledger).
- Checkpoints: "done X, next Y — confirm?" and wait. GATE FILES: checkpoint is a file; missing file = step not done. Skips must be user-stated and recorded. Degradation: can cut process, never real-asset protocol, readability floors, gate.
- Routing by medium: web, deck, infographic, social, app, motion, critique, mechanical (no gate); signals stack; read only current medium's rules (lazy load).
- Independent builder/reviewer contexts.
- Know your default look: cream #F4F1EA + serif + terracotta #D97757 + caps eyebrows + 01/02/03. Four look families (warm-paper serif, dark single-accent, hairline newspaper, SaaS card kit) — flag clusters not ban ("add options not bans", blind tests).
- Critique rubric D0 Concept (veto: ≤5 caps overall at 6.0), Philosophy, Hierarchy, Craft, Functionality, Originality 1-10; scenario weights per medium; tiers Excellent 8+/Good 6-7.9/Needs work 4-5.9/Failing <4. Template test (different client name → cap ≤5), cover-the-text test, remove-the-device test.
- Output: score+tier, one line per dimension, Keep, Fix (Fatal/Important/Improvement with values), 3 Quick Wins.
- Top-10 problems list (scale <2.5×, 5+ colours, off-scale spacing, whitespace <40%, 3+ faces, mixed alignment, decoration>content, cyber-neon #0D1117, density mismatch, AI clichés).
- RED/YELLOW mechanical detectors: per-medium body floors (14px web / 24px deck / 36px phone long-form), label floors, contrast w/ ancestor opacity, technical (broken img, console errors); YELLOW eyebrows, middots, arrows, mono labels, recoloured H1 span, 0N numbering, banned display fonts. Look-family oklch detectors. Distinctness vs last 8 deliveries (oklab distance <0.06, edge-map corr >0.55).
- Colour: Sample (brand, imagery, culture) → Converge in oklch (2-3 chromatic, ΔH≥60 or ΔL≥0.3) → Justify in one sentence. Chroma budget bg 0.01-0.04, accent 0.08-0.15. #0066FF model's default blue.
- Font substitutes (Fraunces→Newsreader; Inter display→Archivo/Anton/Schibsted; Space Grotesk→Schibsted).
- Verify the verifier (thumbnail ≠ render; control experiment; text diff).
- Lessons ledgers + promotion ladder observed→reproduced→guidance→automated check→engine default.
- Render checklist widths 1920/1440/768/375, click through, per-slide screenshots, wait 2s, 2× scale.
- MEDIUM: Slides strongest (HTML→PDF, PPTX on request; showcase-first: 2 most different pages first; 1 message+3-4 points+1 protagonist; 4-5 layouts max; body 24-36px, titles 60-120, hero 180-240; editable PPTX 960×540pt OOXML constraints). Print/PDF body ≥10pt, A4/Letter, @page. Native iOS 390×844, Android 360×800, display boards. Social Xiaohongshu 1242×1660. Infographic 1080 wide body ≥36px. Video/film extensive (Slow-Fast-Boom-Stop, camera, storyboard, audio −14 LUFS, AI video review 3-layer).
- Proposed: D19 exploration & direction gating (3-direction gate); D00b memory/ledgers; D20 video/film.
