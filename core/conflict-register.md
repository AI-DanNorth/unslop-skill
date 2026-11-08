# Conflict register

One recorded resolution per cross-source disagreement. A losing value is never deleted: it lives on as a profile setting or a library theme. New conflicts are added here before any card that depends on them is written. Full positions with section numbers are in `research/mining/` (Conflicts list at the end of each file).

| # | Conflict | Positions | Resolution |
|---|---|---|---|
| C01 | Em and en dashes | Banned (hallmark, impeccable, writing-guidelines, kami) vs normal punctuation (krehel, taste-skill allows 2) | strict: budget 0. balanced: cap 2 per page. Never in UI labels or headlines |
| C02 | Eyebrows above headings | Ban (hallmark, impeccable) vs 1 on a cover (kami) vs common in systems | strict: 0. balanced: flag at 3+, or inside a look-family cluster. One allowed on a cover when it carries a fact |
| C03 | Heading case | Sentence case (writing-guidelines, krehel) vs Title Case (web-interface-guidelines) | Pick one per artifact; flag inconsistency only |
| C04 | Pie and donut | Banned (hallmark) vs ≤5 or 6 slices (kami, ux-ui-agent-skills) | Allowed for 2 to 5 parts of a whole; flag 6+ |
| C05 | Red and green in charts | Never (kami) vs status colours (ux-ui-agent-skills) | Only with a second encoding (sign, icon, label) |
| C06 | Inline validation | On blur (ux-ui-agent-skills, hallmark) vs on submit (taste-skill, krehel) | On blur after first interaction, full check on submit, never per keystroke |
| C07 | Accordion FAQs | Banned (taste-skill) vs standard (web-interface-guidelines) | Allowed; flag when it hides the answers people came for |
| C08 | Weights | 400/500 only (taste-skill) vs 700 titles (ux-ui-agent-skills) vs expressive 300 to 900 (huashu) | No weight-count rule; check hierarchy contrast instead |
| C09 | Pure black and white | Banned (hallmark, kami) vs allowed (Design Rules 2, ui-ux-pro-max OLED) | Flag only when undocumented; a documented style wins |
| C10 | Bans vs options | Hard bans (taste-skill, hallmark) vs "add options, not bans" (huashu) | Look-family tells are info; finding only when they cluster (profile `look_family_cluster_min`) |
| C11 | Kami's parchment system | A house style written as rules | Lives in `library/` as a theme; its methods become general rules |
| C12 | Web body floor | 16px (hallmark, ui-ux-pro-max, taste-skill) vs 14px (kami, huashu) | 16px reading text; 14px hard floor for dense UI and app screens |
| C13 | Body contrast | 4.5:1 (WCAG, hallmark) vs 7:1 (taste-skill) | 4.5:1 Floor; 7:1 Finish target for long reading |
| C14 | Target size | 24px (WCAG 2.2) vs 44px (hallmark, taste-skill) vs 48px coarse | 24 Floor; 44 on touch Reflex; native 44pt / 48dp |
| C15 | Overshoot and springs | Banned in UI (hallmark, taste-skill) vs recommended (huashu, ui-ux-pro-max) | Banned in product UI (Reflex); allowed in video and demo films |
| C16 | Scroll reveals | None (taste-skill) vs one per page (hallmark) vs recipes (ui-ux-pro-max) | One reveal-once per page; never hides content under the three hidden-content conditions |
| C17 | Parallax, image hover zoom | Banned (hallmark) vs 5 to 15% parallax, 1.02 zoom (ui-ux-pro-max, taste-skill) | Library options, off by default; off under reduced motion |
| C18 | Reduced-motion fallback | Zero durations (agent-skills) vs 150ms crossfade (hallmark, taste-skill) | Keep opacity and colour up to 150ms; remove movement |
| C19 | Tracked caps labels | Banned small (hallmark) vs 0.08 to 0.15em (huashu) vs required tracking (kami) | If caps, then tracked; whether to use caps is decided by the label transform-delete test |
| C20 | Photo treatment, text on photos | Theme treatment + 35 to 65% scrim (hallmark) vs no filters, no text on photos (taste-skill) | Allowed when worst-pixel contrast passes; filters only when the brand system specifies |
| C21 | Placeholders by stage | Labelled grey blocks (huashu) vs none visible (hallmark, taste-skill) | Drafts: labelled slots. Ship: none (Floor at the ship gate) |
| C22 | Sample data | example.com in product mocks (hallmark) vs banned (taste-skill) | Only inside product UI mocks, never as claims, never self-labelled |
| C23 | Word budgets | ~450/page, h1 ≤7 words (hallmark) vs ~900, 2 to 8 words (taste-skill) | Profiles: strict = hallmark, balanced = 1.5×, conventional = none |
| C24 | Mirrored splits | One allowed (hallmark) vs never (taste-skill, kami) | Allowed once; flagged when alternation is the only rhythm |
| C25 | Glass panels | Banned (hallmark) vs allowed with fallbacks (ui-ux-pro-max, huashu) | Navigation and controls only, with reduced-transparency fallback and measured contrast |
| C26 | CJK line breaking | `line-break: strict`, `text-wrap: pretty` (huashu) vs banned on CJK (kami) | Follow kami for Chinese and Japanese body; the CJK line-ending audit decides |
| C27 | Toasts, destructive confirms | Auto-dismiss, "Are you sure?" (ui-ux-pro-max) vs undo-first (hallmark) | Undo beats confirm; error toasts persist; no toast when the effect is visible |
| C28 | Slide, print, social floors | 24px vs 13pt vs 18pt; 9 vs 10pt; 36 vs 24px | Normalise to share of canvas width; stricter source when it states its reason |
| C29 | Directions before building | 3 (huashu) vs 2 comps (hallmark) vs none (kami, taste-skill) | explore-directions makes 3 only when fixes fail twice or the brief is open |
| C30 | Fix-loop budget | 1 batch + 1 confirm (hallmark) vs ≤3 rounds (kami, taste-skill) | ≤3 rounds; offer directions after round 2 |
| C31 | Waivers | ≥24 chars (hallmark) vs ≥12 chars, cap 5 (taste-skill) | ≥24 chars, cap 5, 3 in a row becomes house style |
| C32 | Curly vs straight quotes | Curly (hallmark, agent-skills) vs straight unless already curly (kami) | Consistency only: flag mixed quotes |
| C33 | Display-face lists | hallmark bans DM Sans, Work Sans as body; huashu recommends some; huashu bans Fraunces | Three tiers in `data/lexicons/fonts.yaml`: banned-as-display, saturated (info), substitutes |
| C34 | Accent footprint | ≤5% (hallmark, kami) vs <3% (taste-skill) vs 5 to 10% (ui-ux-pro-max 60/30/10) | Warn >5%, fail >8% at the 1280×800 fold |
| C35 | Families per page | ≤3 (hallmark) vs ≤2 (huashu) | Warn at 3, fail at 4 |
| C36 | Gradients | Banned on non-tech pages (taste-skill) vs single-hue ≤40° (hallmark) vs subtle mono (huashu) | hallmark's numeric rule: banned hue pairs, ≤3 stops, ≤40° hue span |
| C37 | Urgency elements | Suggested (ui-ux-pro-max) vs real deadlines only (awesome-design-patterns) | Integrity wins: countdowns and scarcity must be real (Floor) |
| C38 | Easing defaults | expoOut (hallmark, huashu) vs (.2,.8,.2,1) (taste-skill) | One curve family per system; both non-overshoot; flag mixing |
| C39 | Duration tokens | 120/220/420 (hallmark) vs 150/210/400 (agent-skills) vs 150/200/300 (ui-ux-pro-max) | Any one declared scale; flag off-scale durations; exit 60 to 75% of enter |
| C40 | Test widths | Four different matrices | Web adapter: 320, 375, 414, 768, 1024, 1280, 1440, 1920 (superset) |
| C41 | LCP threshold | 2.5s field p75 (agent-skills) vs lab warn 2.5s, fail 4.5s (taste-skill) | Lab: warn 2.5s, fail 4.5s; field data reported when available |
| C42 | Spinner timing | Show after 150 to 300ms, hold ≥300ms (hallmark) vs skeleton >1s (ui-ux-pro-max) | Show after 300ms, hold ≥300ms; skeleton when >1s |
