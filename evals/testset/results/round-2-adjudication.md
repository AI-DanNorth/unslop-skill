# Test set 1, round 2: adjudication of disagreements

Expected labels come from the source repos, and most "good" labels are a repo praising its own AI output. Each disagreement below was checked against the blind reviewers' cited evidence (`results/round-2/<ID>/03-lenses/`) and sorted by cause. The adjudicator is the orchestrating session, not an independent human. A designer should spot-check the rows marked *contested*.

## Disagreements

| Item | Expected | Unslop | Cause | Evidence the call rests on |
|---|---|---|---|---|
| G06 design-taste after.html | good | generated | **label generous** | "Trusted by 4,000+", "Sarah Chen, Stitchboard", Acme logos, LIVE DATA metrics with no source; 5 of 6 warm-paper tells; 577px wide at 375 |
| B04 dsh japanese-minimal | good | generated | **label generous** | six stock sections in stock order; seal, vertical inscription and Chinese numerals unrelated to the product; `lang="ja"` on an English page |
| B06 design-taste corporate-trust | good | generated | **label generous** | 8 stock sections; pseudo-statistics ("n = 4,120", median labelled p75); unlinked SOC 2 / ISO pills |
| B08 huashu saas-pentagram | good | generated | **label generous** | same stock BI hero as B07 reskinned; invented 3x / 50% / 99.9%; famous-brand trust strip; viewport fixed at 1440 |
| I05 avoid-ai-design "after" | good | generated | **label generous** | the redesign kept the Northwind/Lumen logo wall and the unsourced 12,000+ / 4.9 / 99.99% band |
| M02 kami resume | good | mixed | **label generous** | placeholder em@example.com; three links to the wrong pages; no headings |
| G07 ux-ui sample-app | good | mixed | **label generous** | UI copy describes the demo ("one shared theme · light + dark") on stock Tailwind grey and blue |
| G05 impeccable should-pass | good | mixed | **fixture semantics** | "should pass" means "the slop detector must not flag it", not "good design"; stock Tailwind greys throughout |
| G08 huashu lint_clean | good | mixed | **fixture semantics** | passes a lint, but its body copy is text addressed to the lint script |
| G11 huashu xhs_ok | good | generated (low) | **fixture semantics** | a type-size fixture; all copy is placeholder by design |
| G09 pagepatch hero.html | good | mixed | *contested* | reviewer: tracked mono kicker, italic accent word, four disclaimers (over-correction). A human could fairly call this good |
| G12 ux-ui showcase | good | mixed | *contested* | stock revenue-dashboard kit and sample cast, but specific captions; a current-week bar drawn tallest with no axis |
| G10 transitions tuned | good | mixed | **limitation: motion** | the difference from S12 is motion only; still captures cannot show it |
| S12 transitions generic | slop | mixed | **limitation: motion** | as G10 |
| C01 critic async-lies | slop | mixed | **limitation: interaction** | the seeded defect is async behaviour that a static capture does not exercise |
| I01 hallmark fieldbook bare | slop | mixed | **partial** | 5 stock sections cap the read at mixed; specific farm copy. Still 6 slop findings, so the verdict is fix, not ship |
| I02 hallmark relay bare | slop | mixed | **partial** | 6 stock sections, dark single-accent look, unsourced stat band; capped at mixed |

## Adjusted reading

- Clear-cut items scored: 44. Raw agreement: 27.
- Disagreements caused by generous or fixture labels: 10. In each, the system's call rests on cited, checkable evidence.
- Limitations (motion, interaction): 3. These need frame capture and scripted interaction, not threshold changes.
- Partial (real model output called mixed rather than generated): 2. Both still produce fix-level findings.
- Contested: 2.
- **System errors confirmed: none.** Leaving out the 3 motion and interaction rows (not testable from still captures) leaves 41 items. Counting the label and fixture rows as correct calls, agreement is **37 of 41 (90%)**. The other 4 are the 2 partials and the 2 contested rows. If the partials count as catches (both produce fix-level findings), agreement is 39 of 41.

## What this does not show

- No live sites were audited (the workspace reaches GitHub only). The five same-prompt builder outputs, award winners and design systems are still pending.
- Almost every "good" item is AI-made. The set has no verified human-made exemplar except Kami's documents, so false-positive risk on real human work is untested.
- The adjudicator is not independent. Two human spot-checks would make these numbers trustworthy: one on the "label generous" rows, one on the contested rows.

## Follow-up (9 Nov 2026): motion and interaction capture

The three "limitation" rows (G10, S12, C01) are now testable. Capture records transition frames at 0–600 ms (reduced motion off and on) and runs primary actions with the network slowed and a forced failure. The new detectors are `motion` (MOT-002) and `async_state` (CMP-001, plus INT-008 for false success).

- **Manifest correction:** `example.html` only honours `?style=` together with `embed=1`. The old S12 and G10 paths both rendered the same side-by-side compare page, with the modals in iframes. They now point at `example.html?embed=1&style=generic` (S12) and `example.html?embed=1` (G10). The labels are unchanged; the round-2 lens reads were of the compare page.
- **S12:** caught. The menu enters from 0.85 scale (Reflex), the tab slides 30 px (Reflex), and the easing is the default `ease` (Finish).
- **G10:** clean. Its motion is 120–150 ms with `cubic-bezier(0.22,1,0.36,1)`, entrance scale 0.97 and 8 px travel.
- **C01:** caught. It says "Draft project created" at 186 ms but makes no request and changes nothing else (INT-008, Floor).

Still not measured: exit transitions, hover-only motion, and transitions inside iframes (recorded as not verified).
