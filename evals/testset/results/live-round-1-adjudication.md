# Test set 1 live, round 1: adjudication of disagreements

The labels come from the citing sources. "good" on L18 to L22 means a skill author praising their own site, and "good" on L23 to L36 means a human-made control. Each disagreement below was checked against the blind reviewers' cited evidence (`results/live-round-1/<ID>/03-lenses/`) and the mechanical evidence. The adjudicator is the orchestrating session, not an independent human. Rows marked *contested* need a designer's spot-check.

Round 1 scored **27 of 34** clear-cut items (`live-round-1-calibration.md`). L04 is not verified: the Replit app is unpublished.

## Disagreements in round 1

| Item | Expected | Unslop (round 1) | Cause | Evidence the call rests on |
|---|---|---|---|---|
| L24 Nimble article | good | borderline | **system error** (fixed) | Lens: made (medium). The violet-gradient family came from the promo strip's gradient (#2442bb) plus `scattered_radii` (10 radii). The reviewer disputed it: "the article body itself does not show that family". |
| L25 Linear | good | borderline | **system error** (fixed) | Lens: made (high). The family came from product-mock accents (#6d78d5 Slack send button), a gradient pair and 13 radii. The reviewer disputed it. |
| L27 Stripe | good | borderline | **system error** (fixed) | Lens: made (high). The family came from Stripe's own indigo #533afd, the brand ribbon glow and 9 radii. The reviewer: "deliberate brand assets, not defaults". |
| L19 impeccable.style | good | borderline | **limitation: exhibits** | Lens: made (medium), "built around its own product: an interactive before/after specimen that labels the tells it removes". The dark-single-accent and violet-gradient tells fire on the slop specimens the page exhibits on purpose. A page-level sweep can't tell an exhibit from the page's own look. |
| L20 tasteskill.dev | good | slop | *contested* | Lens: mixed (medium). The cited stock wrapper: dark-to-orange glow hero, announcement pill, an eyebrow on every section, a "Stop guessing, start deciding." CTA band, and a pair-and-fragment copy formula. The violet family is partly the labelled "NoteFlow" bad example (an exhibit, as on L19). Without the family the read is still mixed, which scores borderline. A human could fairly call the page good. |
| L21 diagramdesign.dev | good | slop | *contested* | Lens: mixed (medium). The page uses the current warm-paper editorial default (cream grid, Instrument Serif with the italic terracotta payoff "won't hate.", 154 tracked caps labels), but on a drafting-sheet concept that suits a diagram product. Both look families fire on measured tells. The label is the author's own claim. |
| L15 skill-fixture-before | slop | good | **fixture semantics** | The source labels it the "before" fixture: plain HTML "before a style skill". The reviewer: "deliberately unstyled… nothing on it is a model's default look". It is unstyled, not generated, so the "slop" label means "needs styling", not "AI slop". |
| L11 gameghost | slop | slop (round 1); borderline after the fix | **partial** | Lens: mixed (medium). The violet/cyan gradient buttons and glow ring are real tells, but the console concept is deliberate. After `scattered_radii` was removed, the violet family needs purple, a banned pair and glow; L11 has no glow hit, so the verdict is now borderline. It keeps 30 Floor and 11 slop-type findings, so the verdict is still fix. |

Borderline items (L16, L17, L22, L38) are not scored. L17 (borderline, read as slop) matches the lens: "the page itself is the dark SaaS template it sells".

## Floor findings on the human controls (L23 to L36)

Every Floor hit on the controls was treated as a system error until proven otherwise. Three verification passes checked them hit by hit against crops, the DOM, CSS, `focus.json`, a curl of the live HTML, and Playwright probes of the live sites (reports summarised here; scratch copies were not kept in the repo).

| Detector group | Hits checked | Real | False positive | Unverifiable |
|---|---|---|---|---|
| fallback_face, invented_metrics, placeholder_residue, lang_and_title, hidden_content | 45 | 8 | 36 | 1 |
| contrast (about 100 sampled), text_floor, targets | 127 | 65 | 58 | 4 |
| focus_ring, control_names, img_alt, form_labels, reduced_motion, zoom_blocked | 112 | 47 | 54 | 11 |
| **Total** | **284** | **120** | **148** | **16** |

**Main false-positive causes, all fixed** (commits `d514b70`, `03d910e`):
- **Text treated as body copy.** Text inside aria-hidden illustrations and product mock-ups was scored as reading text (L25, L26, L27). It is now demoted to Reflex as incidental under WCAG 1.4.3, not dropped.
- **Focus "covered" was a box-overlap test.** It flagged skip links and transparent shells: 45 stops on L23, L27, L28 and L36. It is now a 9-point paint-stack test, and only full cover is Floor.
- **Accessible names ignored child icons.** `aria-label` on child svg or role=img icons was not read (Stripe logo links, Ant icons).
- **Font names compared literally.** For example "anthropicSans" vs "Anthropic Sans Web Text". Child `<code>` and `<strong>` faces, obfuscated names and CJK fallback were also counted as missing fonts.
- **Integrity matches on real content.**
  - Comparative claims that name their baseline were treated as invented metrics (L23: "than Opus 5").
  - "Todo", JSX `{{…}}` and prose about the placeholder attribute were treated as residue.
- **Capture artifacts.**
  - Mid-transition ghost glyphs in the background render.
  - Below-fold text on scroll-driven pages.
  - The reduced-motion hidden-content test didn't scroll.

**What remains is real.** Human-made sites do fail WCAG:
- Ant Design's rgba(0,0,0,.45) secondary text and 4.10:1 blue (L33, L34).
- Vercel's #101010 focus ring on a #0a0a0a page, plus `maximum-scale=1` (L35).
- No `lang` attribute (L31, L33).
- Spec images with no alt (L34).
- 17–20px footer targets (L28, L34, L36).

A Floor is an accessibility failure, not a slop call. None of the controls is read as slop.

Floor count on the controls, round 1 → after the fixes: L23 10→2, L24 8→6, L25 29→24, L26 18→23, L27 39→16, L28 25→8, L29 1→0, L30 12→2, L31 29→23, L32 1→1, L33 36→22, L34 48→51, L35 15→11, L36 13→13. A few counts rose (L26, L34) because Floors are now sorted ahead of Reflex before the 15-hit cap, so real Floors the cap used to hide now show.

## Look-family changes (evidence: 84 items, both sets)

| Tell | Slop | Good | Change |
|---|---|---|---|
| violet-gradient `scattered_radii` | 29% | 27% | Removed. It was one of the three tells on all five good sites the family flagged. |
| hairline-newspaper `hairlines` / `zero_radius` / `mono_labels` | 42 / 13 / 23% | 51 / 22 / 29% | The family now needs every tell (`cluster_extra: 1`). |
| `italic_serif_hero`, `italic_serif` | 0% | 0% | Bug: only the heading element was checked, so the italic accent word in a child span was missed. Fixed: they now fire on 3 slop and 3 good items. |

## Result after the fixes (recaptured 9 Nov 2026)

| Set | Round 1 | After the fixes |
|---|---|---|
| Live, clear-cut | 27 / 34 | **29 / 34** (`live-round-1-after-fixes.md`) |
| Local, clear-cut (regression check, round-2 lens reads re-scored on new captures) | 27 / 44 | 27 / 44, unchanged (`local-recapture-after-fixes.md`) |

Live disagreements left: L11 (partial), L15 (fixture semantics), L19 (limitation: exhibits), L20 and L21 (contested).

**Adjusted reading.**
- Counting L15 as correct gives **30 of 34**.
- Leaving out L19, which a page-level sweep can't test, gives **30 of 33**.
- If the partial L11 counts as a catch, since it still produces fix-level findings, agreement is **31 of 33**.
- The two left are the contested rows.

**System errors still open:** none confirmed among the disagreements. Mechanical false positives that remain:
- L26's attributed customer metrics (Deel, Storyblok): no safe mechanical exemption, because the same rule would clear L10's fake brand-credited claims.
- `targets` on dense footers: real by the letter of WCAG 2.5.8, but Floor may be too strict for footer link lists. That is a policy call for the plan.

## What this does not show

- The adjudicator is not independent. The *contested* rows (L20, L21) and the fixture row (L15) need the human spot-check.
- Exhibit pages (L19, L20) need region-aware sweeping, such as ignoring sections labelled as examples. That is listed for phase 2.
- Capture time: L28 takes about 740 s with the wheel pass and scroll frames, close to `run_set.py`'s 900 s limit. Run it alone, not in a parallel batch.
- 14 human controls is a small sample, and the live sites change: capture dates are in `live-capture-notes.md`.
