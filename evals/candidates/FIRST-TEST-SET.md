# Proposed first test set (draft, for review)

Picked from evals/candidates/ALL-candidates.csv (1,883 rows, 1,786 unique, from 23 repos plus web research). Labels are what each source claims, not audit results.

**Reachability:** repo files render locally. Live URLs cannot be captured from the cloud workspace (its network allowlist blocks them); they need the linked computer or a browser session. Each row below says which.

## Real AI-builder output in the wild (should be flagged) — live
| # | Target | Medium | Why |
|---|---|---|---|
| R1 | https://findaistack.lovable.app/ , https://ai-stack-gold.vercel.app/ , https://ai-stack-recommendat-7v45.bolt.host/ , https://ai-stack--techaffiliate.replit.app/ , https://ai-stack-techaffiliate.base44.app/ | landing | one brief, five builders (Lovable, v0, Bolt, Replit, Base44); brief banned gradients and glass |
| R2 | https://consile.app , https://cineyx.ai , https://gradloom.app | landing | featured Lovable-built products |
| R3 | https://kin-ai.replit.app , https://v0-optimus-delta.vercel.app , https://gameghost.manus.space | landing | real builder sites cited by impeccable |
| R4 | Medium: anup.karanjkar08 "anti-slop look is now AI slop" page | landing | cream/serif page that scores 100/100 on a token linter: adversarial |
| R5 | github.com/funboy322/avoid-ai-design before/after images | landing (image) | first-order and second-order slop specimens |

## Known slop and same-brief pairs (should be flagged) — repo files unless noted
| # | Target | Medium | Why |
|---|---|---|---|
| 1 | hallmark `skills/hallmark/scripts/fixtures/slopped.html` | landing | ~27 tells listed in its header comment: ready ground truth |
| 2 | hallmark fieldbook / relay / closewise "bare" vs "hallmark" screenshots | landing (image) | same prompt, 26 / 18 / 11 issues vs 0 |
| 3 | impeccable `demos/landing-demo/index.html` and `/classic/` | landing | two slop eras: cream-Fraunces 2025 and dark-purple 2022 |
| 4 | https://impeccable.style/antipattern-examples/new-slop-2026.html (+ 2022, 2025) | landing | era series, live |
| 5 | https://impeccable.style/gallery | landing set | 7 briefs × 5 runs without + 3 with the skill |
| 6 | design-taste `examples/before.html` vs `after.html` | landing | identical copy, slop vs restyled |
| 7 | ux-ui-agent-skills `tests/fixtures/bad/slop-screen.html` vs `examples/sample-app/preview.html` | dashboard | textbook AI dashboard and its fixed twin |
| 8 | ux-ui-agent-skills `tests/fixtures/critic/*.html` + `evals/critic-answer-key.json` | app screens | 14 taste defects that pass every mechanical gate: tests the lenses |
| 9 | huashu `scripts/tests/fixtures/lint_slop / lint_reskin / lint_clean.html` | landing | slop, reskinned, clean |
| 10 | ui-ux-pro-max `projects/portfolio-dark`, `projects/saas-landing` | landing | uncurated skill output full of defaults |
| 11 | https://skill-fixture-before.theroost.dev vs https://ui-ux-pro-max-after.theroost.dev | dashboard | live before/after |
| 12 | https://kin-ai.replit.app, https://v0-optimus-delta.vercel.app, https://gameghost.manus.space | landing | real AI-builder sites in the wild |
| 13 | PagePatch hero (github.com/l-portet/pagepatch-free-hero) before.html vs hero.html | landing | AI hero with 5 explained fixes |
| 14 | https://transitions.dev/example.html?embed=1&style=generic vs ?embed=1 | motion | same modal, generic vs tuned motion |
| 15 | diagram-design `plausible-wrong.png` vs `waterfall-light.png`; Mermaid raw vs redraw | diagram | looks right, numbers wrong |

## Controls that should mostly pass (false-positive checks) — live unless noted
| # | Target | Medium | Why |
|---|---|---|---|
| 16 | https://preview.pro.ant.design/dashboard/analysis, /list/table-list, /form/advanced-form | dashboard, form | conventional enterprise UI ("conventional" profile) |
| 17 | https://ant.design/docs/spec/buttons, /copywriting | design-system doc | explicit do/don't pairs |
| 18 | https://vercel.com/design/guidelines; https://www.w3.org/WAI/ARIA/apg/patterns/ | docs, components | rule-built pages and reference accessible widgets |
| 19 | https://carbondesignsystem.com, https://atlassian.design, https://www.bbc.co.uk/gel | design system | strict, mature systems |
| 20 | https://linear.app, https://cal.com | landing | widely imitated originals: tests "don't punish the source" |
| 21 | https://www.anthropic.com | landing | the "warm editorial" look the repos call an AI default: deliberate brand or slop? |
| 22 | http://www.csszengarden.com | web page | 200+ designs over identical HTML |
| 23 | ui-ux-pro-max `stack/examples/juniper-audit/` | web page | real financial site with an existing audit to compare against |
| 24 | https://sonner.emilkowal.ski, https://vaul.emilkowal.ski | motion | good motion baselines |
| 24a | https://landonorris.com , https://messenger.abeto.co , https://brand.dropbox.com | landing | Awwwards / CSSDA sites of the year 2025 (human exemplars) |
| 24b | https://design-system.service.gov.uk | design system | accessibility-first baseline |
| 24c | https://www.nimblestudio.com/story/creating-an-anti-ai-brand-in-times-of-artificial-everything | landing | human studio using the cream/terracotta look on purpose |

## Non-web media (scarce)
| # | Target | Medium | Why |
|---|---|---|---|
| 25 | kami `site/assets/demos/demo-agent-slides.pdf`, `demo-musk-resume.pdf`, `demo-tesla.pdf` | slides, print | decks and print, one house style |
| 26 | huashu `assets/showcases/ppt/` + https://skill-huasheng.vercel.app | slides | 1920×1080 decks, live keynote |
| 27 | open-design `design-templates/html-ppt-pitch-deck`, `email-marketing` | slides, email | the only email sample found |
| 28 | huashu `xhs_bad.html` / `xhs_ok.html` | social card | labelled bad/ok social cards |
| 29 | https://www.informationisbeautifulawards.com/showcase/7177-this-is-a-teenager , .../6972-swiss-mountains... | data viz, print | IIB 2024 gold (live) |
| 30 | https://www.reidhoffman.org/linkedin-pitch-to-greylock/ | slides | real human pitch deck with known flaws (live) |
| 31 | https://reallygoodemails.com/emails/see-you-next-week , /welcome-to-apple-arcade | email | real emails; one flagged for weak alt text (live) |
| 32 | https://skill-huasheng.vercel.app/slides/slide-03b-deepseek-cover.html | slides | slop vs designer, same slide (live) |
