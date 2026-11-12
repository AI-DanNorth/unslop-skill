# lens-integrity, blind round 1 (11 Nov 2026)

Three blind reviewers ran `lens-integrity` (LENS-BRIEF-PHASE2) on 38 live sites of test set 1, using the captures from 9 Nov 2026. L04 was left out because it is not verified. The judgments and claims tables (without PNGs) are in this folder.

## Result

| Expected | Sites | Read | Integrity score | Mean | Lens Floors |
|---|---|---|---|---|---|
| slop | 14 | 3 generated, 4 mixed, 7 made | 2, 3, 3, 4, 7, 7, 7, 8, 9, 9, 9, 9, 9, 9 | 6.8 | L02, L10, L12, L13 |
| borderline | 4 | 2 mixed, 2 made | 7, 7, 7, 9 | 7.5 | none |
| good | 20 | 20 made | 7 (1 site), 8 (6), 9 (13) | 8.6 | none |

- **No false Floors:** the lens puts no Floor on any of the 20 human-made sites. Its four Floors all have positive evidence on the page:
  - L10: brand-credited round results with no case study, a logo wall of invented names, and a "live" counter frozen across captures.
  - L12 and L13: "Backed by" or "Trusted by 10,000+" over the default-name list.
  - L02: "Trusted by 12,000+" next to initials-only avatars.
- **Integrity is a truth check, not a slop detector.** Seven slop sites read "made": many generated pages invent no proof. L14 and L15 label themselves as fixtures or examples, and the lens read them as such (conflicts C21 and C22). The low scores separate cleanly: nothing human-made scores under 7, and four slop sites score 4 or below.
- **Findings on human sites are small and real:**
  - Contradictory counts: L21 says 44 against 45, L17 says 29 against 14, and L39 says $4.7MM against $4 million.
  - L31: an empty byline slot.
  - L24: unsourced survey figures.
  - L27: an 8-decimal live ticker with no method.
  - L26: a customer's own revenue growth presented as the product's result.

  All of these are Reflex or Finish.

## Sweep hits the lens disputes

| Site | Detector | Hit | Lens reading |
|---|---|---|---|
| L26 | `invented_metrics` (3 Floors) | "35% less", "50% more", "99.99% uptime SLA" | Figures from named customers' case studies, linked to their stories, plus a contract term |
| L38 | `invented_metrics` (Floor) | "You pay up to 35% less" | A labelled third-party ad; the claim is the advertiser's |
| L16, L33 | `stat_band` | Seed tiles and demo dashboards | Fixture or template demo data |
| L07 | `default_names` | "Vertex" | Google Cloud Vertex AI is a real product |

The round-1 live adjudication already decided L26: there is "no safe mechanical exemption, because the same rule would clear L10's fake brand-credited claims". So the thresholds are unchanged. What is new is that a lens now gives an evidenced dispute, and synthesize has no way to act on it.

**Open design question for the scoring rubric:** should a lens's evidenced dispute of a sweep Floor demote that Floor to Reflex in synthesize? The demotion would be recorded and auditable, and would apply only when the lens cites the evidence (a linked case study, an "Ad" label, a fixture label). Until that is decided, these hits stay Floor and go to adjudication.
