# Review: external "unslop" writing skill (9 Nov 2026)

An external skill, also called "Unslop", lists 31 numbered prose tells (content, language, style, chatbot residue, filler, jargon, plain speech). It edits text. This repo audits designed artifacts, including their copy. This note records what was adopted, what was not, and the evidence for each.

## Test

Each candidate the repo doesn't already enforce was turned into a pattern and run against the visible text (`dom-1440.json` `bodyText`) of the 38 verified live items in test set 1 (14 slop, 4 borderline, 20 good).

| Pattern | Slop | Borderline | Good | Items |
|---|---|---|---|---|
| additionally | 0 | 0 | 1 | L39 |
| enhance | 1 | 0 | 1 | L07, L19 |
| showcase | 0 | 1 | 2 | L17, L31, L34 |
| vibrant | 0 | 1 | 0 | L17 |
| numerous | 0 | 0 | 1 | L39 |
| in order to | 0 | 0 | 1 | L39 |
| enduring, foster, underscore, boasts, utilize, facilitate, nexus, north star, bedrock, substrate, modality | 0 | 0 | 0 | – |
| due to the fact, vague attribution ("experts believe", "studies show"), "the future looks bright", "let me know if", "you're absolutely right" | 0 | 0 | 0 | – |
| -ing rider (", highlighting the…"), false range ("from startups to enterprises") | 0 | 0 | 0 | – |

None of the candidates separates slop from good on web pages. Where they fire at all, they fire mostly on human controls (L39 is a long human essay, and L31 and L34 are human-made). AI landing-page copy has its own vocabulary, which `data/lexicons/buzzwords.yaml` and `stock-phrases.yaml` already cover.

## Decisions

| External rule | Repo status | Decision |
|---|---|---|
| 7 AI vocabulary, 8 "serves as", 9 "not just X but Y", 20 chatbot phrases (part), 23 filler (part), 26 jargon (part), 31 plain words (part) | `buzzwords` (slop-words, puffery, dead-metaphors), `stock-phrases` (not-x-but-y, chat-residue, openers) | Already covered. The new terms were not added because the evidence above shows no separation and some false-positive risk. |
| 13 ban em dashes outright | `CPY-004` dash budget (active) | Not adopted. A budget fits designed copy; an outright ban conflicts with typography cards that use the em dash correctly. |
| 19 straight quotes | `D05-TYP` wants typographic quotes on designed pages | Not adopted. It conflicts with the repo's typography card; the external rule targets markdown and code. |
| 17 sentence-case headings | `D05-TYP` draft "Write headings in sentence case" | Already a draft card. A title-case detector could follow if a round shows it separates (L17 "Everything You Need for Beautiful UI" is one example). |
| 3 -ing riders, 10 rule of three, 15 bold, 18 emoji | Draft cards CPY-158, CPY-161, CPY-212, CPY-252; `emoji_icons` detector | Already drafts. They go to `lens-copy` (phase 2). |
| 5 vague attributions, 11 synonym cycling, 12 false ranges, 24 hedging, 25 generic conclusions, 27–33 plain speech, passive voice, adverbs, mannered prose, over-compression | Not in the repo | For `lens-copy` (phase 2) on **long-form** content only (articles, docs, emails, reports). Example: the L24 reviewer found model cadence in the article prose, which the mechanical lexicons don't catch. |
| 14 colon overuse, 16 inline-header lists | Not in the repo | Adopted as writing style for Unslop's own output. |
| 27–33 plain speech (whole set) | – | **Adopted** for Unslop's own findings and reports: `core/report-format.md`, "Writing style". |

## Follow-up

- When `lens-copy` is written (phase 2), add the long-form tells above as draft cards in `research/mining/` with this note as the source. Scope them to long-form media, and test them on the same live items before promoting.
