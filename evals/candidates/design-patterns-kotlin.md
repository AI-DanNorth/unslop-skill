# design-patterns-kotlin (dbacinski/Design-Patterns-In-Kotlin)
Software (GoF) design patterns written in Kotlin: one README of text and code plus Kotlin test files. It has nothing for visual design auditing: no images, UML, diagrams, docs site or UI.

| # | URL or repo path | Medium | Label (good / slop / neutral) | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://github.com/dbacinski/Design-Patterns-In-Kotlin (README.md) | doc (GitHub-rendered Markdown) | neutral | The only artifact. A long code-reference README (1099 lines). It could serve as a weak control sample for doc structure only (TOC, headings, code blocks) | README.md:1-1099 |
| 2 | https://github.com/ochococo/Design-Patterns-In-Swift | doc / repo (external) | neutral | Linked as the inspiration. Its README is also text and code only, so it is equally off-topic | README.md:7 |

## Notes
- Repo contents: README.md, LICENSE, Gradle files, and patterns/src/test/kotlin/*.kt (17 pattern files). No image files.
- Running `grep` for `![`, .png, .svg, .jpg and .gif in the README returns nothing, so there are no UML or class diagrams to use as diagram-audit samples.
- The other links (Wikipedia, blackwasp.co.uk GoF sheet, Twitter, a Mockito article) are text references with no visual design value.
- Recommendation: drop this repo from the calibration set.
