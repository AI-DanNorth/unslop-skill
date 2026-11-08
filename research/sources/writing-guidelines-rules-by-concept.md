# Design Rules by Concept

Distilled from the Writing Guidelines (clear, agent-readable docs and product prose), merged across their long-form, checklist and review versions, plus the learning-goal taxonomy they reference.

# Part 1 — Guiding Principles

## 1. Docs Are Hundreds of Small Decisions
- Good docs succeed because of hundreds of small, deliberate choices (an ellipsis, a heading, a placeholder); treat each as a decision, not a default.
- Rules carry strength levels: MUST = non-negotiable, SHOULD = default unless there's a reason, NEVER = a flagged anti-pattern.
- Write for two readers at once: humans and language models. Docs are consumed by models too, so wrong docs train wrong models.
- Audit every generated page against the full list; AI drafts reliably miss these details.

## 2. Reviewing for Compliance
- Report findings tersely: the issue plus its exact location, one per line.
- Skip explanation unless the fix is non-obvious; no preamble.
- Mark clean files explicitly as passing so silence isn't ambiguous.
- Show the fix inline where it's mechanical (`"..." → "…"`, `"64KB" → "64 KB"`, `<TOKEN> → your_access_token_here`).

# Part 2 — Planning a Page

## 3. Plan Before You Write
- MUST: every page starts with a five-section plan: overview, goal, audiences, documentation plan, open questions.
- One plan does three jobs: it is the brief for drafting (including the prompt for an AI draft), the test spec for the finished page, and the description reviewers read.
- Write the plan by hand; it is the spec the writer (human or model) works against.

## 4. Pick a Content Type Early
- MUST: declare one content type up front: `Tutorial`, `How-to`, `Reference`, `Conceptual`, `Troubleshooting`, or `Landing`.
- The type drives the shape, the tone and the structure of the page.
- MUST: one page does one job: a tutorial OR a how-to OR a reference, never all three at once.

## 5. Title Around the User's Question
- MUST: titles are user-shaped (the reader's question or goal), not feature-shaped (the engineer's name for the thing).
- Example: a page titled with the product name ("X Server") vs. a page titled "Make your SaaS work in ChatGPT": same content, different title, very different search surface.

## 6. Goals Are Testable
- SHOULD: express the page goal with an action verb from the learning-objectives taxonomy (`configure`, `explain`, `debug`).
- A goal is good if you could hand it to a reader (or a model) and ask "does this page enable this?" and get a yes/no answer.

## 7. Choosing Goal Verbs by Depth of Learning
- Six ascending levels of learning, useful for pitching a page's goal: Remember → Understand → Apply → Analyze → Evaluate → Create.
- Remember: recall or recognise facts (`list`, `recall`, `identify`): fits reference pages.
- Understand: organise and summarise ideas (`explain`, `summarize`, `describe`): fits conceptual pages.
- Apply: use knowledge in a new situation (`configure`, `deploy`, `use`): fits tutorials and how-tos.
- Analyze: break information into parts and relate them (`debug`, `compare`, `diagnose`): fits troubleshooting.
- Evaluate: judge against criteria (`choose`, `assess`, `decide`): fits comparison and decision pages.
- Create: combine elements into something new (`build`, `design`, `compose`): fits end-to-end guides.
- Treat the levels as a guide, not a strict ladder; real tasks mix several, and lower levels are not less important.

## 8. Define Every Term on First Use
- MUST: define (and link to its conceptual page) every term the first time it appears.
- The cost of the link is zero; the cost of a reader bouncing on unfamiliar jargon is the whole page.

## 9. Multi-Audience Pages
- Open with a short shared section everyone can read, then split into technical subsections per audience.

# Part 3 — Voice

## 10. Active Voice
- MUST: write in active voice.
- The "by monkeys" test: append "by monkeys" to the verb. If "the page will be updated by monkeys" still parses, it's passive; rewrite to name the actor ("The platform updates the page").

## 11. Direct Address
- MUST: address the reader as `you` when they are acting.
- NEVER `the user`, `one can`, or similar distancing constructions.

## 12. Imperative for Steps
- MUST: steps use the imperative: "Click **Add Project**", not "You will need to click **Add Project**".
- The imperative is shorter, more honest, and consistent with how commands and APIs document themselves.

## 13. Short Sentences
- SHOULD: target sentences under `20` words.

## 14. Contractions
- SHOULD: use contractions (`you'll`, `it's`); they reduce stiffness and add warmth.

## 15. Present Tense
- MUST: write in present tense unless describing genuinely future behaviour.

## 16. Limit "We"
- Use `we` only for deliberate actions by the organisation ("we recommend", "we deprecated").
- NEVER use `we` as a stand-in for `you` ("we click Save" → "click Save").

## 17. No Rhetorical Questions
- NEVER ask rhetorical questions; they read as marketing.

## 18. The Second-Read Test
- MUST: every sentence parses on one read at speech pace.
- If you have to re-read to parse it, rewrite by naming the subject, the action and the consequence.
- Kill metaphor verbs and pronouns that reach back several sentences for their referent.

# Part 4 — Banned and Weak Words

## 19. Banned Reassurance Words
- NEVER describe reader actions as `easy`, `simple` or `quick`.
- They sound friendly but pressure the reader (if it's "easy" and they're stuck, they feel stupid) and read as marketing.
- Replace with a concrete description: "one command", "default settings", "most projects don't need this".

## 20. Filler Words
- NEVER use `very`, `just`, `really`, `simply`; cut or rewrite the sentence.

## 21. Weasel Words
- NEVER use vague qualifiers like `significantly`, `many`, `often`, `typically`, `generally`.
- Replace with a specific number or a specific claim.

## 22. Vague Quantifiers
- NEVER use `near-zero`, `sub-second`, `most requests` without data.
- Give the figure and cite it: `99.37% of requests see zero cold starts`.

## 23. Filler and Metaphor Verbs
- NEVER reach for cadence verbs like `moves through`, `lands`, `carries`, `hits`.
- Name the literal step that happens instead.

## 24. Earn Every Detail
- MUST: cut any number, name or implementation detail if a more general phrasing wouldn't change the reader's understanding or action.
- Specificity is required where it informs; it's noise where it doesn't.

# Part 5 — AI-Generated Tells

## 25. Summary-Style Transitions
- NEVER open a paragraph by recapping the last one (`With this setup complete…`, `Now that we've explored…`).
- Pivot straight to the next point instead (`In practice…`, `The catch is…`).

## 26. Stop-Start Fragments
- NEVER split one dependent idea into choppy fragments ("Previously this was manual. Now it's automatic. This saves time.").
- Join them into one sentence; short sentences for deliberate emphasis are still fine.

## 27. Spec-Sheet Voice
- NEVER write like a system reading a datasheet (`provides`, `is configurable`, `is explicitly labeled`).
- Rewrite around what the reader does or what happens.

## 28. Cold-Open Paragraphs
- NEVER start a body paragraph with a sentence that works as a standalone heading and has no antecedent.
- Carry the prior subject forward with connective openings (`Because…`, `Once…`).

## 29. Personified Artifacts
- NEVER have machines perform human-physical actions: `hand the browser a URL` → `the browser fetches the URL`; `the token holds…` → `the token is stored…`.

## 30. Reused Template Framing
- NEVER use framings that could open any page (`The question most teams face is whether…`).
- The angle must come from this page's specific subject.

# Part 6 — Tone by Content Type

## 31. Tutorial
- Warm, encouraging, predictable structure, no traps.
- Picture walking a new colleague through their first deploy.
- List prerequisites up front; link a working sample project for multi-step tutorials.

## 32. How-To
- Terse and direct. The reader is mid-task: get them out.

## 33. Reference
- Neutral, exhaustive, quotable. Assume the reader will quote you in a bug report.
- Organise reference docs by surface (API, command, option); organise educational docs by reader task.

## 34. Conceptual
- Explain as if the reader will teach it back to someone tomorrow.
- Examples and analogies are welcome here in a way they are not in a how-to.

## 35. Troubleshooting
- Empathetic but not apologetic: acknowledge the error, then go straight to the fix.

# Part 7 — Headings and Structure

## 36. Sentence Case for Page Headings
- MUST: page headings `H1` through `H6` use sentence case: "Configure environment variables", not "Configure Environment Variables".
- NEVER Title Case in page headings.

## 37. Title Case for Navigation Labels
- MUST: sidebar/nav labels use title case: "Configuring Environment Variables".
- The page H1 is a sentence; the nav entry is a label. Keep page title and nav label as separate fields.
- Nav names are scannable and start with action verbs.

## 38. Descriptive Subheadings
- MUST: subheadings are descriptive, not cute or generic: "Caveats when self-hosting on Cloudflare", not "Caveats".
- The reader should be able to guess the section's content from the heading alone.
- Flag single generic-word subheadings: `Overview`, `Caveats`, `Notes`.

## 39. Topics Start with Summaries
- MUST: every page opens with a one-paragraph TL;DR of what it covers.
- MUST: every major section opens with a summary sentence.
- A reader arriving from search should know whether to keep reading by the end of the first line.

## 40. Acronyms
- MUST: spell out acronyms on first use: "Content Security Policy (CSP) blocks inline scripts"; afterwards, just "CSP".

## 41. Paragraph Length
- MUST: keep paragraphs to `2–4` sentences.
- Split any paragraph that runs longer or covers two ideas.

# Part 8 — Lists

## 42. When to Use a List
- MUST: three or more list-shaped items in a paragraph become a list; fewer stay as prose.

## 43. Bulleted vs Numbered
- Bulleted for unordered items; numbered for ordered ones (lifecycles, sequential steps).

## 44. List Mechanics
- MUST: always introduce a list with a colon.
- NEVER end list items with periods unless they are full sentences.
- MUST: term/description items use the format `- **Term**: description` with the colon after the bold term.

# Part 9 — Code in Docs

## 45. Language Tags
- MUST: every code block has a language tag; syntax highlighting depends on it.

## 46. Default Language
- SHOULD: default to TypeScript for new examples unless the surface is genuinely language-agnostic.

## 47. Multi-Step Flows
- MUST: wrap consecutive steps in a visible step component so the reader sees the structure.

## 48. Highlight Load-Bearing Lines
- SHOULD: highlight the lines that matter (e.g. `{8-12,23-37}`) so readers find the change in a larger block.

## 49. Snippet Size
- SHOULD: `≤80` columns per line and `≤25` lines per snippet.
- Split longer blocks with explanatory prose in between.

## 50. Omit Defaults and Repetition
- Don't repeat default values or variable definitions across snippets; reference a shared variable.

## 51. Comments vs Prose
- Keep comments in code minimal; explain in prose between blocks.
- MUST: explain what every code block does; never "drop and run".

## 52. Inline Everything
- NEVER end a guide with "see the full example file". The guide is the deliverable; all code lives inline.

## 53. Locale-Safe Samples
- In code samples, use locale formatting APIs for dates and numbers rather than hardcoded formats.

## 54. Current Model Identifiers
- Always use the latest model identifiers in examples; outdated model names make docs look stale and teach outdated usage.

# Part 10 — Placeholders, Units and Numbers

## 55. Text Placeholders
- MUST: text placeholders are descriptive `snake_case`: `your_access_token_here`.
- Snake case lets the reader double-click to select the entire placeholder before pasting their real value.
- NEVER `<TOKEN>`, `xxx`, `your-token`, `ABC123`, or generic ALL_CAPS.

## 56. Number Placeholders
- MUST: number placeholders count up: `1234567890123`.
- Recognisable as fake, predictable, clearly not a real ID.

## 57. Data Sizes and Units
- MUST: a space plus an uppercase unit: `64 KB`, `5 KB`, `200 ms`.
- Exception: seconds are written bare: `30s`.
- Flag bare or mis-cased units: `64KB`, `5kb`, `200MS`.
- Consistency across every page lets readers develop scanning habits.

## 58. Numerals for Counts
- MUST: "8 deployments", not "eight deployments".

# Part 11 — Typography and Punctuation

## 59. No Dashes as Punctuation
- NEVER use em dashes (`—`) or hyphens (`-`) as sentence punctuation.
- Use colons, commas, periods, or rephrase the sentence.

## 60. Curly Quotes
- MUST: curly quotes (`“ ”`, `‘ ’`), never straight (`"`, `'`).

## 61. Ellipsis Character
- MUST: `…`, never three dots `...`.
- Loading states end with `…`: `Loading…`, `Saving…`, `Generating…`.

## 62. Non-Breaking Spaces
- MUST: glue terms that must not wrap apart with non-breaking spaces: `10&nbsp;MB`, `⌘&nbsp;K`, multi-word brand names.

## 63. Ampersands
- SHOULD: use `&` instead of "and" only where space is constrained (nav labels, buttons); write "and" in prose.

# Part 12 — Emphasis and Inline Code

## 64. Bold Has Two Jobs
- MUST: bold marks UI elements ("Click **Add Project**") or a critical fact, nothing else.
- NEVER bold for emphasis-for-emphasis' sake. If you reach for bold to add tone, the sentence is weak; rewrite it.

## 65. Inline Code
- MUST: use inline code for paths, file extensions, identifiers and short snippets: `/api`, `.tsx`, `body`, `query`, `req`.
- Rule of thumb: if it would look weird without a monospace font, monospace it.

# Part 13 — Links

## 66. Descriptive Anchor Text
- MUST: anchor text names the destination.
- NEVER bare URLs, or `here` / `link` as anchor text.

## 67. Link Terms to Concepts
- Link each term on first appearance to its canonical conceptual page.
- Link to canonical product docs where relevant rather than duplicating them.

## 68. Deep Links into the Product
- Use a consistent, standard deep-link format when pointing readers to a specific screen in the product, with a readable title.
- Every product surface that exposes a feature links to its docs.

# Part 14 — Source Formatting

## 69. Don't Hard-Wrap
- NEVER hard-wrap prose; each paragraph is one line in source, and the editor wraps.

## 70. Blank Lines
- MUST: one blank line before headings, and one before and after code blocks.
- No extra blank lines between elements that aren't paragraph breaks.

## 71. No Horizontal Rules
- NEVER use `---` rules between sections; headings provide structure.

# Part 15 — Pricing and Money Pages

## 72. Uncompromising Detail
- Err on the side of "too much"; this is the one place to over-explain.
- Clarity and transparency above all else.

## 73. Tables for Pricing
- MUST: present pricing in tables.

## 74. Never Assume the Model
- MUST: document the pricing model explicitly.
- NEVER assume the reader knows the pricing model, or whether their workload counts as one billable unit or several.

## 75. Limits
- Document every limit, and keep a single all-limits table in sync whenever a limit is added or changed.

# Part 16 — Quality Checklist

## 76. Findability
- Every page sits in the right navigation category.
- The product UI links to the docs from any surface that exposes the feature.

## 77. Accuracy
- Code samples actually run.
- Screenshots map 1:1 to the current UI and use a consistent fictional demo account so they look uniform and expose no customer data.

## 78. Relevance
- Include code samples wherever applicable, in the default language, with step components for multi-step flows.

## 79. Clarity
- The overview answers who, what, where and why.
- High-level use cases are laid out; new products get a quickstart.
- Tutorials list prerequisites and link a working sample project.
- Steps are detailed, not vague.
- Add visual aids to confusing sections.
- When multiple paths exist, recommend the simplest one.

## 80. Completeness
- Limits are documented and the all-limits table is updated.
- The content plan was followed and its goals are addressed.

## 81. Readability
- Nav names are scannable and use action verbs.
- Content types are used accurately.
- Subheadings are descriptive; topics start with summaries.
- Code blocks are formatted correctly; active voice wherever warranted.

# Part 17 — Writing with AI

## 82. Accountability
- MUST: you are accountable for content you ship, however it was produced. An AI-drafted page is your page.
- You are the final arbiter: the model proposes, you dispose.

## 83. Accuracy Standard
- MUST: hold technical accuracy to a high bar; docs feed future models.

## 84. Data Safety
- MUST: use only enterprise-grade models that don't train on your data, especially for unreleased products.

## 85. Plan-First Drafting
- Plan by hand first; let the model work against the plan.
- Review the model's own plan before it starts writing.
- Instruct the model to follow the house rules and the checklist.

## 86. Test the Page with a Prompt
- Use a model as the first reader: "Given this plan's goal, can you complete the task using only this page?"
- If it can't, the page isn't done.

## 87. Disclose and Review
- MUST: disclose AI use (model, and prompts if useful) so the team learns which workflows work.
- MUST: a final human review, always.

# Part 18 — Review Culture

## 88. Review Requests
- The review request links the plan, lists exactly what to review, and links a rendered preview.
- Route feedback through the review request, not side channels.

## 89. Ownership
- The author is accountable, not the reviewer; reviewers flag, authors decide.
- Reviewers are liberal with approvals: iteration speed matters more than gatekeeping.

## 90. Comment Types
- Use inline suggestions for small text fixes; comment on the rendered preview for anything bigger, so feedback carries visual context.

## 91. Disagreement
- Disagreement is fine: reject with a one-line reason and move on.
- File follow-ups for anything that won't land in this change.

# Part 19 — Anti-Patterns to Flag

## 92. Voice and Wording Red Flags
- Passive voice (fails the "by monkeys" test).
- `easy`, `simple`, `quick` describing reader actions.
- Filler: `very`, `just`, `really`, `simply`.
- Weasel words: `significantly`, `many`, `often`, `typically`, `generally`.
- Vague quantifiers without a cited figure: `near-zero`, `sub-second`, `most requests`.
- Metaphor verbs: `moves through`, `lands`, `carries`, `hits`.
- "We" standing in for "you"; rhetorical questions.
- Sentences that need a second read; paragraphs over `4` sentences or covering two ideas.

## 93. AI-Tell Red Flags
- Recap transitions (`With this setup complete…`).
- Stop-start fragments.
- Spec-sheet voice (`provides`, `is configurable`).
- Cold-open paragraphs with no antecedent.
- Personified artifacts (`hand the browser a URL`).
- Template framing (`The question most teams face is whether…`).

## 94. Structure Red Flags
- Title Case in page headings.
- Generic one-word subheadings (`Overview`, `Caveats`, `Notes`).
- Pages or sections with no opening summary.
- Acronyms used before being spelled out.
- Missing content type; feature-shaped titles; pages doing several jobs.

## 95. Typography Red Flags
- Em dashes or hyphens used as punctuation.
- Straight quotes; three dots instead of `…`; `Loading...` instead of `Loading…`.
- Bare units (`64KB`, `5kb`, `200MS`).
- Bold used for emphasis rather than UI elements or critical facts.
- Bare URLs or `here`/`link` anchor text.

## 96. Code and Placeholder Red Flags
- Code blocks without a language tag.
- Plain JS where TypeScript is the convention.
- Blocks over `25` lines with no prose between.
- Generic placeholders: `<TOKEN>`, `xxx`, `your-token`, `ABC123`.
- "See the full example file" instead of inlining.
- Outdated model identifiers; hardcoded date/number formats in samples.

## 97. Source Red Flags
- Hard-wrapped paragraphs.
- `---` horizontal rules between sections.
