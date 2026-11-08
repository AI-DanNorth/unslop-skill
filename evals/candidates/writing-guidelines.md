# writing-guidelines (vercel-labs/writing-guidelines): example inventory

Repo is 3 rule files (README.md, AGENTS.md, command.md), no example folder, no docs site. Almost every "example" is an inline incorrect/correct copy pair; live URLs are Vercel docs cited as canonical link targets. Clone: /home/claude/refs/writing-guidelines

| # | URL or repo path | Medium | Label (as repo presents it) | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://vercel.com/docs/vercel-sandbox (now canonical at /docs/sandbox) | doc | good | Cited as canonical product doc to link to; live, follows the house style (sentence-case H1/H2, TL;DR opener, bold/description lists, pricing table) | command.md:149 |
| 2 | https://vercel.com/docs/ai-gateway | doc | good | Cited as canonical product doc; live; user-shaped H2 ("Call AI models across providers…"), requirement/handling table | command.md:149 |
| 3 | https://vercel.com/ai-gateway/models | web page | neutral | Model catalog link target; dense catalog UI with "Loading status…" copy (ellipsis rule visible in the wild) | command.md:150 |
| 4 | https://vercel.com/d?to=%2F%5Bteam%5D%2F~%2Fai-gateway%2Fapi-keys&title=AI+Gateway+API+Keys | web page | neutral | Format example for dashboard deep links (requires login) | command.md:148 |
| 5 | https://en.wikipedia.org/wiki/Bloom%27s_taxonomy | web page | neutral | Reference for verb-driven, testable page goals | README.md:10 |
| 6 | https://agents.md/ | web page | neutral | AGENTS.md format spec the repo targets | README.md:140 |
| 7 | https://vercel.com/careers | web page | neutral | Hiring link only | README.md:146 |
| 8 | https://raw.githubusercontent.com/vercel-labs/writing-guidelines/main/command.md | doc | neutral | Repo's own review prompt, distributed raw | README.md:136 |
| 9 | https://raw.githubusercontent.com/vercel-labs/writing-guidelines/main/AGENTS.md | doc | neutral | Repo's own MUST/SHOULD/NEVER ruleset, distributed raw | README.md:142 |
| 10 | https://github.com/vercel-labs/writing-guidelines | doc | neutral | Repo's only "site" (GitHub README); no separate docs site | (repo root) |
| 11 | README.md | doc | good | Guidelines written in their own style (no em dashes, sentence-case headings, bold/description bullets); usable as a "clean" prose fixture | README.md:1 |
| 12 | AGENTS.md | doc | neutral | Terse rule list incl. "AI-generated tells" section | AGENTS.md:33 |
| 13 | command.md output sample (fake audit of content/docs/sandbox.mdx, ai-gateway.mdx, cron.mdx) | UI copy sample | neutral | Ready-made file:line finding format; lists 15 slop findings (feature-shaped title "Vercel Sandbox", "easy", "...", `<TOKEN>`, "64KB", "Caveats", em dash, Title Case H1) | command.md:228-255 |
| 14 | "Vercel MCP Server" → "Make your SaaS work in ChatGPT" | incorrect-correct pair | slop → good | Feature-shaped vs user-question title | README.md:9 |
| 15 | "the page will be updated by monkeys" → "Vercel updates the page" | incorrect-correct pair | slop → good | Passive voice test ("by monkeys") | README.md:15 |
| 16 | "the user" / "one can" → "you" | incorrect-correct pair | slop → good | Direct address | README.md:16 |
| 17 | "You will need to click **Add Project**" → "Click **Add Project**" | incorrect-correct pair | slop → good | Imperative steps | README.md:17; command.md:27 |
| 18 | `we` as stand-in for `you` → "we recommend", "we deprecated" only | incorrect-correct pair | slop → good | Pronoun misuse | README.md:21 |
| 19 | `easy`, `simple`, `quick` → "one command", "default settings", "most projects don't need this" | incorrect-correct pair | slop → good | Banned pressure words with concrete replacements | README.md:22; command.md:37 |
| 20 | `very`, `just`, `really`, `simply` | incorrect-correct pair (incorrect only) | slop | Filler words to cut | README.md:23 |
| 21 | "Configure Environment Variables" → "Configure environment variables" (nav: "Configuring Environment Variables") | incorrect-correct pair | slop → good | Sentence case headings vs title-case nav labels | README.md:36-37; command.md:66 |
| 22 | "Caveats" → "Caveats when self-hosting on Cloudflare"; also `Overview`, `Notes` | incorrect-correct pair | slop → good | Generic one-word subheadings | README.md:39; command.md:199 |
| 23 | "Content Security Policy (CSP) blocks inline scripts" | incorrect-correct pair (correct only) | good | Acronym spelled out on first use | README.md:41 |
| 24 | `<TOKEN>`, `xxx`, `your-token`, `ABC123` → `your_access_token_here`, `1234567890123` | incorrect-correct pair | slop → good | Placeholder conventions | README.md:65-67; command.md:104-106 |
| 25 | `64KB`, `5kb`, `200MS` → `64 KB`, `5 KB`, `200 ms`, `30s` | incorrect-correct pair | slop → good | Unit formatting | README.md:68; command.md:205 |
| 26 | "eight" → "8 deployments" | incorrect-correct pair | slop → good | Numerals for counts | README.md:69 |
| 27 | Em dash / dash as punctuation → colon, comma, period | incorrect-correct pair | slop → good | Classic AI-prose tell, banned outright | README.md:73; command.md:189 |
| 28 | Straight quotes → curly; `...` → `…`; "Loading..." → "Loading…" | incorrect-correct pair | slop → good | UI-copy typography (loading states) | README.md:74-76; command.md:212 |
| 29 | "With this setup complete…", "Now that we've explored…" → "In practice…", "The catch is…" | incorrect-correct pair | slop → good | AI tell: summary-style transitions | command.md:49; AGENTS.md:35 |
| 30 | "Previously this was manual. Now it's automatic. This saves time." → one sentence | incorrect-correct pair | slop → good | AI tell: stop-start fragments (concrete passage) | command.md:50; AGENTS.md:36 |
| 31 | `provides`, `is configurable`, `is explicitly labeled` | incorrect-correct pair (incorrect only) | slop | AI tell: spec-sheet voice | command.md:51; AGENTS.md:37 |
| 32 | Cold-open body paragraph → carry subject with "Because…", "Once…" | incorrect-correct pair | slop → good | AI tell: no antecedent | command.md:52; AGENTS.md:38 |
| 33 | "hand the browser a URL" → "the browser fetches the URL"; "the token holds…" → "the token is stored…" | incorrect-correct pair | slop → good | AI tell: personified artifacts | command.md:53; AGENTS.md:39 |
| 34 | "The question most teams face is whether…" | incorrect-correct pair (incorrect only) | slop | AI tell: template framing | command.md:54; AGENTS.md:40 |
| 35 | `significantly`, `many`, `often`, `typically`, `generally` | incorrect-correct pair (incorrect only) | slop | Weasel words | command.md:43; AGENTS.md:29 |
| 36 | `near-zero`, `sub-second`, `most requests` → "99.37% of requests see zero cold starts" | incorrect-correct pair | slop → good | Vague quantifier vs cited figure | command.md:44 |
| 37 | `moves through`, `lands`, `carries`, `hits` → literal step | incorrect-correct pair | slop → good | Metaphor/cadence verbs | command.md:45 |
| 38 | Bare URLs, `here`/`link` anchors → anchor names destination | incorrect-correct pair | slop → good | Link copy | command.md:147; AGENTS.md:110 |
| 39 | "See `train.py`" / "see the full example file" → inline code | incorrect-correct pair | slop → good | Drop-and-run docs | command.md:100; README.md:61 |
| 40 | `anthropic/claude-sonnet-4`, `gpt-4o`, DALL-E → `anthropic/claude-opus-4-7`, `google/gemini-3.1-flash-image-preview` | incorrect-correct pair | slop → good | Stale model strings (Vercel-specific, will itself go stale) | README.md:128; command.md:154, 210 |

## Best audit candidates

1. #30 stop-start passage: a full, quotable AI-tell sentence trio with a clear fix; ideal copy-lens fixture.
2. #29 summary transitions: exact openers to pattern-match, plus replacement openers.
3. #33 personified artifacts: two concrete before/after phrases; tests semantic, not keyword, detection.
4. #36 vague quantifier → cited figure: shows the "specific number" fix with a real example sentence.
5. #19 easy/simple/quick with concrete replacements: high-frequency marketing slop in UI and docs.
6. #14 feature-shaped vs user-question title: tests headline/hero copy judgment.
7. #13 command.md sample output: 15 labeled findings in file:line form; doubles as an expected-output fixture for the audit report format.
8. #27 + #28 typography (em dash, straight quotes, "Loading..."): deterministic, regex-checkable checks.
9. #1 vercel.com/docs/sandbox: live "good" doc page to run a full audit against as a near-clean control.
10. #34 + #31 template framing and spec-sheet voice: incorrect-only, so good for testing whether the auditor proposes its own fix.

## Notes

- No images, screenshots, HTML, or example directories in the repo; it is copy/docs rules only, so it serves the copy lens, not visual lenses.
- Many rules appear 3 times (README, AGENTS.md, command.md); table cites the clearest occurrence plus mirrors.
- Spot-checked live (2026-11-08): vercel.com/docs/vercel-sandbox (serves /docs/sandbox), /docs/ai-gateway, /ai-gateway/models, agents.md. All resolved.
- The live Vercel pages break some of the repo's own rules (e.g., "Fast startup… start in milliseconds", "often dwarfed"), useful as mild-violation fixtures.
- Repo homepage metadata could not be queried (GitHub API not enabled for this session).
