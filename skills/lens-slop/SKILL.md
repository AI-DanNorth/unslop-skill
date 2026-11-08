---
name: lens-slop
description: Phase 3 judgment lens for AI-default slop. Judges whether a design reads as made or generated, using named tests (rival's-name swap, mirror, default-agent question, deletion, filler, fresh reader) on top of the sweep's measured tells and look-family clusters. Use inside an Unslop run, or when the user asks "does this look AI-made?" about a captured page.
---

# Lens: slop (D03, with D02 concept and D18 integrity cues)

You judge one thing: **does this read as made for this client, or as the default output of a model?** You work from the evidence in `$RUN/01-evidence/` and the sweep results in `$RUN/02-mechanical.json`. You never see other lenses' output.

## Inputs to read, in this order

1. `00-contract.md`: visitor mode, profile, brief overrides, supplied facts.
2. `01-evidence/fold-1440.png`, `shot-1440.png`, `shot-375.png`: look at them yourself before reading any numbers.
3. `02-mechanical.json`: hits from `eyebrow`, `numbered_labels`, `icon_tile`, `card_kit`, `gradient`, `glow`, `neon_violet`, `chrome_glyphs`, `lexicon_copy`, `look_family`, `invented_metrics`, `default_names`. These are already findings; do not repeat them. Use them as context for what you judge.
4. `data/look-families.yaml` and `data/lexicons/` for the vocabulary of tells.
5. `rules/SLP.yaml`: the curated cards (SLP-001 to 012) plus about 150 draft cards mined from the sources. Drafts are advice: cite one when it names what you see, with its id.

## Tests to run (record each in `tests_run`)

Run these on the actual page text and screenshots. Each failed test is a finding that cites the test id from `core/tests/tests.yaml`.

| Test | Do | A finding when |
|---|---|---|
| T-RIVAL-NAME | Put the nearest competitor's name into the h1, sub-line and every heading | Any line stays true. If the whole page still holds, also note "Concept capped at 5" |
| T-MIRROR | Would a neighbouring brief in this category get this hero, nav, footer and first section? | Yes. Name the one decision to change |
| T-DEFAULT-AGENT | Could typing "landing page for <category>" into an agent produce this? | Yes. Say which parts |
| T-FIVE-SECOND | First screen only: what is it, for whom, what to do? | Any of the three is unanswered |
| T-THREE-LINE | For each claim: picturable, falsifiable, only-this-business? | A claim fails all three (cap 3 examples) |
| T-DELETION | Remove each decorative image, divider, badge and icon in turn | Nothing is lost (it is filler) |
| T-STOCK-ORDER | List the sections in order; mark stock ones (mock hero, logo strip, equal feature cards, 1-2-3 steps, stat band, testimonial cards, three pricing tiers, FAQ, CTA band, link-farm footer) | 5 or more in stock order. 7 or more means the read is `generated` even when the copy is specific: specific words on a default skeleton are still a default page |
| T-OVER-CORRECTION | If this page was already "unslopped", look for the substitute habit (fragments, "rather than", pairs) | The substitute multiplies |
| T-FRESH-READER | Read only the text; list the 3 lines that would fit any site | Always list them; they are findings when they are headings or the hero |

Then look at the whole: count which look-family tells you can see that the sweep could not measure (a stock 3D blob image, a dashboard mock with fake data, a testimonial wall of initials). Judge clusters, never single tells (conflict C10): one tell is a choice, three are a default.

## Writing findings

- Output `$RUN/03-lenses/slop.json` in the shape of `skills/unslop/templates/lens-output.json`.
- At most 8 findings, ranked by how much of the page they make read as generated. A thin, generic first screen outranks every detail.
- Each finding: a rule id (an SLP card, or CON/CPY/INT where it fits better), tier, where, **evidence you can point to** (quoted text, a screenshot region, a test result), before, after, why, and the test id.
- Tier: Reflex for slop, Floor only for integrity (invented proof, fake people) the sweep missed, Finish for polish.
- Respect the brief: if the contract records an override for a tell, do not report it.
- `strengths`: name what is specific and must not be diluted by fixes. Always at least one if anything qualifies.
- `overall_read`: one of `made` (reads as designed for this client), `mixed` (specific in places, default in others) or `generated` (reads as a model's default output), plus `confidence` (`low`, `medium`, `high`) and one sentence of reason. Decide it from the screenshots and tests, not from the count of sweep hits. Specific copy does not rescue a stock skeleton (T-STOCK-ORDER), and a recognisable look family chosen without a reason in the contract counts against `made`. A page can have many mechanical hits and still read as made, or none and read as generated.
- Never write an "after" that invents facts. Where content is missing, the after is `[DATA NEEDED: what]`.

## Gate

`$RUN/03-lenses/slop.json` exists, parses, and every finding cites evidence and a test or rule id.
