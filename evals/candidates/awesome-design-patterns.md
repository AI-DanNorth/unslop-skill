# awesome-design-patterns (DovAmir) - design-artifact candidates
Source: README of github.com/DovAmir/awesome-design-patterns (shallow clone 2026-11-08). Mostly a software-architecture list; only the rows below are visual or renderable sites.

| # | URL | Medium | Label | Why notable | README section |
|---|-----|--------|-------|-------------|----------------|
| 1 | http://ui-patterns.com | pattern gallery | good | ~170 UI + persuasive patterns with screenshot collections from live sites (verified live, updated Oct 2026) | Front-End Development |
| 2 | https://bradfrost.github.io/this-is-responsive/patterns.html#layout | pattern gallery | good | Brad Frost's responsive layout/nav/table/form patterns, mostly linking CodePen demos (verified live) | Front-End Development |
| 3 | https://github.com/AllThingsSmitty/css-protips | doc | neutral | CSS craft tips; rule source more than an artifact | Front-End Development |
| 4 | http://clubmate.fi/oocss-acss-bem-smacss-what-are-they-what-should-i-use | doc | neutral | CSS methodology comparison article (personal blog layout) | Front-End Development |
| 5 | https://martinfowler.com/eaaDev/uiArchs.html | doc | neutral | GUI architecture essay (MVC/MVP); long-form text page with diagrams | Front-End Development > front-End Architecture |
| 6 | https://refactoring.guru/design-patterns/python | web page | good | Distinctive hand-drawn illustration system (Dmitry Zhart) on catalog cards; strong non-template identity (verified live) | Programming Language > Python |
| 7 | https://12factor.net | web page | good | Restrained, typographic single-purpose site; anti-slop reference for minimalism | Micro services & Distributed Systems |
| 8 | https://reactpatterns.com | web page | neutral | Minimal single-page code-doc site | Programming Language > React |
| 9 | https://java-design-patterns.com/patterns/ | web page | neutral | Large catalog index with tag filtering; dense listing layout | Programming Language > Java |
| 10 | https://python-patterns.guide/ | web page | neutral | Essay-style typographic site (Brandon Rhodes) | Programming Language > Python |
| 11 | https://patterns.innersourcecommons.org/ | web page | neutral | Community pattern docs site; generic doc-site template baseline | General Architecture |
| 12 | https://k8spatterns.io/ | web page | neutral | Book marketing landing page; typical hero + CTA structure | DevOps & containers |
| 13 | https://cdkpatterns.com/ | web page | neutral | Pattern catalog landing page (possibly stale/redirected) | DevOps & containers |
| 14 | https://serverlessland.com/patterns | pattern gallery | neutral | AWS card-grid gallery with filters; corporate card-grid baseline | Serverless Architecture |
| 15 | https://gcp.solutions | pattern gallery | neutral | Gallery of GCP architecture diagrams (fetch blocked by robots; liveness unconfirmed) | Cloud Architecture |
| 16 | https://docs.microsoft.com/en-us/azure/architecture/patterns | doc | neutral | Microsoft Learn docs (Fluent-based doc system), mature docs IA | Cloud Architecture |
| 17 | https://rust-unofficial.github.io/patterns/ | doc | neutral | Stock mdBook theme; "untouched default theme" baseline | Programming Language > Rust |
| 18 | https://learn-vuejs.github.io/vue-patterns/ | doc | neutral | Stock VuePress default theme; default-template baseline | Programming Language > Vue.js |

## Best audit candidates
1. http://ui-patterns.com - live pattern library plus real-site screenshot collections (doubles as a reference corpus)
2. https://refactoring.guru/design-patterns/python - custom illustration system; positive control for "distinctive"
3. https://12factor.net - typographic minimalism; positive control for restraint
4. https://bradfrost.github.io/this-is-responsive/patterns.html - responsive pattern index; test responsive/layout rules
5. https://serverlessland.com/patterns - corporate filterable card grid; tests card-grid/sameness heuristics
6. https://k8spatterns.io/ - book landing page; tests hero/CTA heuristics on a real non-AI page
7. https://java-design-patterns.com/patterns/ - dense catalog listing; tests density/hierarchy rules
8. https://python-patterns.guide/ - essay typography; tests reading measure/typography rules
9. https://rust-unofficial.github.io/patterns/ - stock mdBook theme; "default, not slop" calibration case
10. https://docs.microsoft.com/en-us/azure/architecture/patterns - mature design-system-driven docs page

## Notes
- 115 unique content URLs in the README; 18 kept, 97 out of scope (code/architecture repos, articles, books, cloud/DB/security patterns).
- No dark-pattern or visual anti-pattern galleries present; "anti patterns" links (sourcemaking, sqlcheck, microservices antipatterns) are code-level, so slop count is 0.
- Rows 6-18 are included as renderable real sites, not because the README presents them as design references.
- Spot-checked: ui-patterns.com, bradfrost patterns, refactoring.guru live; gcp.solutions unreachable (robots).
