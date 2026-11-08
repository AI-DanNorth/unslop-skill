# Web research report: real design artifacts for auditing AI slop

Extended web research run on 8 Nov 2026. The full 157-row link table is `evals/candidates/web-research.md`; this file keeps the findings and caveats that shaped the plan.

## Key findings

- **The best ready-made slop material is one benchmark.** TechAffiliate (7 Oct 2026) gave one brief to five AI builders and published all five sites: Lovable (findaistack.lovable.app), v0 (ai-stack-gold.vercel.app), Bolt (ai-stack-recommendat-7v45.bolt.host), Replit (ai-stack--techaffiliate.replit.app) and Base44 (ai-stack-techaffiliate.base44.app). The brief banned "excessive gradients", "neon AI clichés" and "generic template appearance", so the five outputs show what survives an explicit ban. These are live items L01 to L05.
- **Slop now comes in two clusters, and the auditor needs both.**
  - First-order: purple-to-blue gradient, Inter, centred hero, three cards.
  - Second-order, the "Claude look": warm cream (near #F4F1EA), a high-contrast serif with one italic terracotta phrase, tracked caps eyebrows, 01/02/03 markers. Kyle Chayka described it in The New Yorker (24 Jun 2026): "beige- and cream-colored backgrounds, rusty orange-hued accents, and large serif typefaces". Anthropic's frontend-design SKILL.md now bans "a warm cream background (near #F4F1EA)" with a terracotta accent "often near #D97757".
  - Paul Bakaus (Impeccable 3.5 changelog): "74% of GPT-5.5 pages used the cream / beige AI-default background", "76% reached for extreme negative letter-spacing on tech briefs", and 90%+ failed the contrast floor.
- **Passing a linter is not the same as not being slop.** A Medium author's Claude-"rescued" fintech page scored 100/100 on a token linter while matching every second-order tell (anup.karanjkar08, "The anti-slop look is now AI slop"). It is an adversarial case for the judgment lenses.
- **False positives are a real risk.** Anthropic's own brand, human-made purple SaaS shots on Dribbble, and anti-AI studio brands (Nimble Studio) use the same markers on purpose; Kami uses parchment and serif deliberately. Unslop has to score context and intent, not just palette. This is why brand authority and brief overrides exist (`core/precedence.md`).
- **Banning slop in the prompt doesn't fix it.** Sajib Rahman (Jiro, 9 Oct 2026): the same lazy prompt gives "the same site three times: Inter, purple gradient, three feature cards". Chayka: telling a model to avoid the tropes "just results in a different generic style".
- **Design Arena** (designarena.ai) is the largest live same-prompt comparison source, with Elo boards for websites, slides, data viz and mobile. Its outputs are generated on demand and not kept at stable URLs, so they must be captured during a voting session.
- **Origin of the indigo default:** Adam Wathan has apologised for Tailwind's indigo button becoming the AI default (via shipthemes.com).

## Caveats

- **Verification:** igloo.inc, brand.dropbox.com and animejs.com have domains inferred from award listings, and some design-system citations are indirect. Awwwards blocks automated fetching, so its pages were confirmed through search snippets only. Check links live before freezing a set.
- **Slop labels are candidates, not verdicts.** Lovable-gallery apps are AI-built by provenance, but their builders may have customised them heavily.
- **Scarce media:** no publicly linked AI-generated pitch deck, PDF report, resume or email with a stable URL was found. Kami's demo PDFs and Open Design's 56 decks are the best AI-side stand-ins, but they are skill showcases, not raw defaults. Generate raw-default decks and PDFs from one fixed prompt when needed.
- **Source quality:** several slop-taxonomy articles are agency or vendor content marketing (925 Studios, DesignRevision/Forge, Lovable's own guide). The Medium claim that Ryo Lu "coined" AI slop is unsupported. The New Yorker column is the strongest independent source for the "Claude look".
- **Not covered:** specific Godly, Siteinspire, Land-book and Mobbin pages; video beyond launch clips.
