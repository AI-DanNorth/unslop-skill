---
name: intake
description: Phase 0 of an Unslop audit. Establishes what the artifact is, who it is for, which visitor mode and medium apply, which profile and brand authority govern, and writes the run contract (00-contract.md). Use when the unslop orchestrator starts a run, or when the user asks to set up or change an audit's brief.
---

# Intake

Write `$RUN/00-contract.md` from `skills/unslop/templates/contract.md`. Fill every field. Ask the user **at most one round** of questions, and only for fields you cannot infer from the request, the artifact, or the repository. If the user is not there to answer, take the most reasonable reading, write it in the contract with "(assumed)" and carry on.

## Fields and how to fill them

1. **Target**: URL or file path. Check it opens (a quick `curl -I` or file check) before writing it.
2. **Medium**: `web` for anything that renders in a browser (marketing page, docs, dashboard). Phase-1 build supports `web` only; for other media, say so and stop unless the user wants the web checks anyway (slides exported as HTML, for example).
3. **Visitor mode**: Persuade (marketing, sales), Operate (product UI, tools), Read (docs, articles, reports) or Experience (portfolio, campaign). Infer from the page: a pricing table and hero CTA is Persuade; a data table with filters is Operate.
4. **Profile**: `strict` for Persuade and Experience surfaces that must look made, not generated; `balanced` (default) for most; `conventional` for enterprise, regulated or native-app UI. Name why.
5. **Brand authority**: is there a brand or design system that outranks the defaults? If the user names one, record its location. If the site is live, note "brand-extract not yet available in this build; brand values taken from the page's own tokens".
6. **Brief overrides**: anything the user explicitly wants that a rule would flag (an eyebrow style, a 900-word page). These become notes, not findings, unless the rule is Floor (`core/precedence.md`).
7. **Supplied facts**: every metric, customer name and quote the user confirms is real. The `invented_metrics` detector skips these (`supplied:` list).
8. **Lenses**: default `slop, a11y` in this build; `concept` and `structure` are also built and run when selected. List the lenses you are not running and why.
9. **Stage**: draft or ship. At ship, placeholders are Floor (conflict C21).

Then set `run.json` `profile` and `medium` to match, and write any brief overrides into `run.json` as `overrides: {detector: {key: value}}` (for example `invented_metrics: {supplied: ["99.95% uptime"]}`).

## Gate

`00-contract.md` exists and has no empty field. Tell the orchestrator the run directory and the profile.
