# How Unslop got here (7 to 8 Nov 2026)

A record of what was done, what was decided and what was learned, so a new session can continue without the original conversation. The plan itself is `docs/PLAN.md` (exported from the claude.ai Project plan doc, which stays the source of truth).

## Timeline

1. **Synthesis and plan.** The 20 docs in the claude.ai Project "Design Reviewing System" (now `research/sources/`) were synthesised into a skill-system plan:
   - an orchestrator plus control, lens, media-adapter and remedy bundles;
   - domains D00 to D20, a rule card schema, Floor/Reflex/Finish tiers, gate files and profiles.
2. **Deep mining.** Six miners read the seven largest sources concept by concept (brief: `research/mining/BRIEF.md`), and the 13 smaller sources were mined inline (`research/mining/G-inline-sources.md`). The output was 2,099 candidate rule rows, about 190 named tests (about 60 after merging), about 120 conflicts and 12 lexicons. Condensed reader notes on four sources are in `research/notes/`.
3. **Phase 1 build.** This covered:
   - core contracts, data (thresholds, lexicons, look families, stress fixtures) and 53 curated rule cards (now 56) plus 2,099 mined drafts;
   - Playwright capture with the check-the-checker control page, and 52 sweep detectors;
   - the seeded-defect self-test, report synthesis and the CLI;
   - eight skills.
4. **Example hunt.** One agent per source repo (23) plus a web research task collected 1,883 candidate examples (`evals/candidates/`; the web findings are in `research/web-research-report.md`). Design-Patterns-In-Kotlin turned out to be software patterns only and was dropped.
5. **Test set 1.** 52 local items (`evals/testset/set1.yaml`): known slop, controls, borderline, critic fixtures, other media and image-only. There are also 39 live sites (`set1-live.yaml`), not yet run because the cloud workspace reaches GitHub only.
6. **Calibration.** Two rounds of blind review by six reviewer agents (`evals/testset/LENS-BRIEF.md`). Results and adjudication are in `evals/testset/results/`.

## Decisions (all reversible)

| Decision | Choice | Why |
|---|---|---|
| Rendering | Playwright in the plugin's own scripts | Same page, same findings; the exit test depends on it |
| Default profile | balanced | Strict is for Persuade and Experience surfaces; conventional for enterprise UI |
| Contrast | WCAG 2.2 ratios are Floor; APCA reported as advice | The mined thresholds are in WCAG terms |
| Skill folders | Flat (`skills/lens-slop/`) | The plugin loader discovers one level only |
| Mined rules | Kept as `status: draft` cards (101+), curated cards are 001-099 | Lenses can cite drafts as advice; only curated cards block |
| Look families | Tells are info; a finding only when they cluster (profile minimum) | Settles the "bans vs options" conflict (C10) |
| Text-size floor | Floor below 12px; Reflex 12 to 14px; Finish 14 to 16px | Small meta text is common on good sites and is not a WCAG failure |
| Focus indicator | Invisible or covered is Floor; visible but under 3:1 is Reflex | 3:1 change contrast is WCAG 2.4.13 (AAA) |
| Hidden content | Content lost under reduced motion, a stuck observer or scripts off is Floor; a large hidden share at load is Reflex | Menus, dialogs and tabs hide content legitimately |
| Specific copy on a stock skeleton | T-STOCK-ORDER: 5 or 6 stock sections caps the read at mixed; 7 or more is generated | Real model output (hallmark's bare pages) was under-called |
| Commit identity | AI-DanNorth noreply address | GitHub credits commits by email |

## What calibration taught us

- **Capture fidelity comes first.** Fonts, npm CDNs, Tailwind and absolute site URLs failed silently in a sandbox, and the audit then judged pages that weren't what their authors built. The fix is `scripts/capture/netshim.mjs` (Fontsource via npm, npm CDN packages, the Tailwind browser build with a config bridge, host mapping to local copies) plus recording everything blocked as "not verified".
- **Measure where the glyphs are.** Sampling an element's whole box caught hairlines and icons. Making text `color: transparent` also wiped `currentColor` backgrounds. Contrast now samples each text node's line boxes on a background render that hides glyphs with `-webkit-text-fill-color`.
- **Fixed-canvas media are not web pages.** Social cards, slides, print and diagrams need their own widths, floors and switched-off responsive checks (`skills/media-*/thresholds.yaml`).
- **Most "good" labels in the source repos are self-praise of AI output.** In the adjudication, 10 of 17 disagreements were the label, not the system. Agreement with source labels is a weak metric; a human spot-check and real human-made exemplars (the live set) are needed.
- **What the scripts miss, the reviewers catch:** invented proof in bare stat bands, placeholder copy in other languages, arithmetic that doesn't add up (I06 waterfall, M07 MoM claim), self-describing demo copy, and links without href. Several of these became detectors; the arithmetic checks belong in a future data-viz lens.
- **Still untestable from screenshots:** motion (S12/G10) and async interaction (C01).

## Mistakes to avoid repeating

- A cleanup glob (`rm -rf runs/*/0[1-4]*`) deleted round-1 review outputs. Archive rounds with `archive_round.sh` before re-capturing.
- Passing the expected label into `run.json` would have leaked answers to the reviewers. Expected labels live only in the manifests.
- Early commits used the claude.ai login email, which GitHub credited to a different account (ghostwarwick-tech). The repo identity is now set in `CLAUDE.md`.
