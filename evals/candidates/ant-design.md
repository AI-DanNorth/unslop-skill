# Ant Design: real design artifacts for Unslop calibration
Source: github.com/ant-design/ant-design (sparse clone at /home/claude/refs/ant-design, docs/ + README + DESIGN.md + components/*/demo listing). Baseline for the "conventional" enterprise-UI profile.

| # | URL or repo path | Medium | Label | Why notable | Source |
|---|---|---|---|---|---|
| 1 | https://preview.pro.ant.design/dashboard/analysis | dashboard | good | Canonical Pro analytics dashboard: KPI cards, trend charts, ranking table; reference "conventional" dashboard | Pro route (spot-checked live, SPA); visualization-page spec |
| 2 | https://preview.pro.ant.design/dashboard/monitor | dashboard | good | Monitor template cited by the spec as the model monitoring dashboard | docs/spec/visualization-page.en-US.md:91 |
| 3 | https://preview.pro.ant.design/dashboard/workplace | dashboard | good | Workbench home (to-dos, shortcuts, activity); matches the Workbench spec | Pro route (not linked in repo); docs/spec/research-workbench.en-US.md:38 |
| 4 | https://preview.pro.ant.design/list/table-list | app screen | good | Query table: filter form, toolbar, batch actions, pagination | docs/spec/research-list.en-US.md:56 |
| 5 | https://preview.pro.ant.design/list/card-list | app screen | good | Card-list template; useful against "identical card grid" slop rules | docs/spec/research-list.en-US.md:76 |
| 6 | https://preview.pro.ant.design/profile/basic | app screen | good | Basic detail page: flat Descriptions plus tables, no unneeded folding | docs/spec/detail-page.en-US.md:50 |
| 7 | https://preview.pro.ant.design/profile/advanced | app screen | good | Advanced detail: header, steps, tabs, dense multi-section info | docs/spec/detail-page.en-US.md:86 |
| 8 | https://preview.pro.ant.design/user/login | form | good | Login template referenced from the Form Page spec | docs/spec/research-form.en-US.md:187 |
| 9 | https://preview.pro.ant.design/user/register | form | good | Register template; label, validation and help-text conventions | docs/spec/research-form.en-US.md:195 |
| 10 | https://preview.pro.ant.design/form/step-form | form | good | Multi-step form, an example of the Steps navigation pattern | Pro route (not linked in repo); docs/spec/navigation.en-US.md:96 |
| 11 | https://preview.pro.ant.design/form/advanced-form | form | good | Long grouped enterprise form with footer toolbar | Pro route (not linked in repo); docs/spec/research-form.en-US.md |
| 12 | https://preview.pro.ant.design/result/success | app screen | good | Result page template (status, next actions, details) | Pro route; docs/spec/research-result.en-US.md:102 |
| 13 | https://preview.pro.ant.design/exception/403 | app screen | good | Exception template (403/404/500) with recovery action | Pro route; docs/spec/research-exception.en-US.md:53-73 |
| 14 | https://preview.pro.ant.design/account/settings | app screen | good | Settings screen, side menu and form sections | Pro route (not linked in repo) |
| 15 | https://ant.design | landing | neutral | Design-system marketing homepage; tests hero and landing rules on a non-AI site | README.md:46; .dumi/pages/index/index.tsx |
| 16 | https://ant.design/components/overview | gallery | good | Index of all components with thumbnails | README.md:101 |
| 17 | https://ant.design/theme-editor | app screen | good | Real tool UI: token panel and live preview | docs/react/customize-theme.en-US.md:185; .dumi/pages/theme-editor |
| 18 | https://pro.ant.design | landing | neutral | Pro product and docs site | README.md:106; docs/spec/cases.en-US.md:35 |
| 19 | https://procomponents.ant.design | design-system doc | good | ProTable, ProForm and ProLayout demos: high-density enterprise screens | README.md:107 |
| 20 | https://charts.ant.design (https://ant-design-charts.antgroup.com) | gallery | good | Official chart gallery; dataviz baseline | README.md:110; docs/react/recommendation.en-US.md:13 |
| 21 | https://antv.antgroup.com/en | landing | neutral | AntV visualisation family site | docs/react/recommendation.en-US.md:13 |
| 22 | https://mobile.ant.design | design-system doc | good | Mobile system: tests mobile and touch rules | README.md:108 |
| 23 | https://mini.ant.design | design-system doc | neutral | Mini-program component set | README.md:109 |
| 24 | https://landing.ant.design | landing | neutral | Landing-page template builder (circa 2017); real pre-AI generic marketing templates | README.md:112; docs/resources.en-US.md:42 |
| 25 | https://motion.ant.design | design-system doc | neutral | Motion library site and demos | README.md:113 |
| 26 | https://ant.design/docs/spec/cases | gallery | neutral | "Who's using" showcase page (best-practice cases plus logos) | docs/spec/cases.en-US.md:1-45 |
| 27 | https://tech.antfin.com | landing | neutral | Showcase: Ant Financial Technology | docs/spec/cases.en-US.md:19 |
| 28 | https://en.oceanbase.com/docs/ | app screen | neutral | Showcase: OceanBase Cloud docs and console | docs/spec/cases.en-US.md:27 |
| 29 | https://data.aliyun.com/product/sc | landing | neutral | Showcase: Alibaba Cloud StreamCompute (link may have moved) | docs/spec/cases.en-US.md:43 |
| 30 | https://lobehub.com | landing | neutral | Live cases-page logo; modern AI product built on antd, useful to test where antd and AI aesthetics meet | ant.design/docs/spec/cases (live); README.md:17 |
| 31 | https://coderabbit.ai | landing | neutral | Live cases-page logo; AI dev-tool marketing site | ant.design/docs/spec/cases (live); README.md:17 |
| 32 | https://youmind.com | landing | neutral | Live cases-page logo | ant.design/docs/spec/cases (live) |
| 33 | https://tractian.com | landing | neutral | Live cases-page logo; industrial SaaS | ant.design/docs/spec/cases (live) |
| 34 | https://ant.design/docs/spec/buttons | design-system doc | good and bad | 7 Do / 5 Don't: one primary per group, no two icons, verb labels, no dividers | docs/spec/buttons.en-US.md:52-189 |
| 35 | https://ant.design/docs/spec/copywriting | design-system doc | good and bad | 18 correct/wrong pairs on UI copy: tone, absolutes, time precision, word order | docs/spec/copywriting.en-US.md:25-210 |
| 36 | https://ant.design/docs/spec/alignment | design-system doc | good and bad | 2 pairs: single visual starting point; label/number alignment | docs/spec/alignment.en-US.md:17-39 |
| 37 | https://ant.design/docs/spec/contrast | design-system doc | good and bad | 1 pair: weak versus strong contrast ("Don't be wimp") | docs/spec/contrast.en-US.md:17 |
| 38 | https://ant.design/docs/spec/data-entry | design-system doc | good and bad | 1 pair: Switch does not need a Save button | docs/spec/data-entry.en-US.md:103 |
| 39 | https://ant.design/docs/spec/data-format | design-system doc | good and bad | 3 pairs: number, amount and date formatting | docs/spec/data-format.en-US.md:28-115 |
| 40 | https://ant.design/docs/spec/feedback | design-system doc | good and bad | 1 pair: important failure needs a modal, not a toast | docs/spec/feedback.en-US.md:129 |
| 41 | https://ant.design/docs/spec/icon | design-system doc | good and bad | 4 pairs: stroke consistency, rounded corners, legibility, no faux-3D | docs/spec/icon.en-US.md:55-85 |
| 42 | https://ant.design/docs/spec/research-empty | design-system doc | good and bad | 1 pair: explicit empty-state prompt versus a blank area | docs/spec/research-empty.en-US.md:35-39 |
| 43 | https://ant.design/docs/spec/research-form | design-system doc | good and bad | 1 Do / 4 Don't: mixed controls, redundant placeholders, multi-column ban | docs/spec/research-form.en-US.md:43-229 |
| 44 | https://ant.design/docs/spec/research-navigation | design-system doc | good and bad | 1 Do / 2 Don't: menu hover paths, in-page actions in the utility bar | docs/spec/research-navigation.en-US.md:129-171 |
| 45 | https://ant.design/docs/spec/research-result | design-system doc | good and bad | 5 Do / 3 Don't for result pages | docs/spec/research-result.en-US.md:48-79 |
| 46 | https://ant.design/docs/spec/stay | design-system doc | good and bad | 2 Do / 1 Don't: undo instead of confirm dialogs | docs/spec/stay.en-US.md:19-21 |
| 47 | https://ant.design/docs/spec/visualization-page | design-system doc | good and bad | 3 Do / 1 Don't plus dashboard templates (presentation, monitor, analytics) | docs/spec/visualization-page.en-US.md:42-182 |
| 48 | DESIGN.md (repo root) | design-system doc | good and bad | Agent-facing DESIGN.md with token front-matter and 10 text Do/Don't rules (one primary, no ad-hoc accents, 4px grid, named easings) | DESIGN.md:1, 303-314 |
| 49 | https://ant.design/docs/spec/layout | design-system doc | good | Grid, 8px spacing and screen-size rules | docs/spec/layout.en-US.md |
| 50 | https://ant.design/docs/spec/colors | design-system doc | good | Palette generation, functional-colour restraint | docs/spec/colors.en-US.md:80 |
| 51 | https://ant.design/docs/spec/font | design-system doc | good | System font stack, type scale, line height | docs/spec/font.en-US.md |
| 52 | https://ant.design/docs/spec/data-display | design-system doc | good | Table, list and card selection guidance | docs/spec/data-display.en-US.md |
| 53 | https://ant.design/docs/spec/data-list | design-system doc | good | Filtering, sorting and list patterns | docs/spec/data-list.en-US.md |
| 54 | https://ant.design/docs/spec/navigation | design-system doc | good | Nav types: side, top, breadcrumb, tabs, steps | docs/spec/navigation.en-US.md |
| 55 | https://ant.design/docs/spec/motion | design-system doc | good | "Avoid dramatic and complicated animations" | docs/spec/motion.en-US.md:98 |
| 56 | https://ant.design/docs/spec/visual | design-system doc | good | Chart-type selection and visualisation rules | docs/spec/visual.en-US.md |
| 57 | https://ant.design/docs/spec/shadow | design-system doc | good | Elevation levels; a counterpoint to glow and heavy-shadow slop | docs/spec/shadow.en-US.md |
| 58 | https://ant.design/docs/spec/dark | design-system doc | good | Dark-mode principles | docs/spec/dark.en-US.md |
| 59 | https://ant.design/docs/spec/research-workbench | design-system doc | good | Workbench and new-user-guide templates (screenshots) | docs/spec/research-workbench.en-US.md:38-100 |
| 60 | https://ant.design/docs/spec/research-exception | design-system doc | good | 404/403/500 templates | docs/spec/research-exception.en-US.md:40-73 |
| 61 | https://ant.design/docs/spec/research-list | design-system doc | good | List-page spec plus table/card templates | docs/spec/research-list.en-US.md |
| 62 | https://ant.design/docs/spec/detail-page | design-system doc | good | Detail-page spec: "display as flat as possible" | docs/spec/detail-page.en-US.md:21 |
| 63 | https://ant.design/docs/spec/research-message-and-feedback | design-system doc | good | Message, notification and modal selection | docs/spec/research-message-and-feedback.en-US.md |
| 64 | https://ant.design/docs/spec/illustration | design-system doc | neutral | Illustration system; tests illustration and stock-art rules | docs/spec/illustration.en-US.md |
| 65 | components/layout/demo/side.tsx (ant.design/components/layout) | app screen | good | Sider + header + content shell: the classic admin layout | components/layout/demo/side.tsx |
| 66 | components/layout/demo/top-side.tsx | app screen | good | Top nav plus side menu, with breadcrumb | components/layout/demo/top-side.tsx |
| 67 | components/layout/demo/fixed-sider.tsx | app screen | good | Long-scroll content with fixed sider | components/layout/demo/fixed-sider.tsx |
| 68 | components/table/demo/row-selection-and-operation.tsx | component demo | good | Batch-action table pattern | components/table/demo/row-selection-and-operation.tsx |
| 69 | components/table/demo/fixed-columns-header.tsx | component demo | good | Dense wide table with fixed columns and header | components/table/demo/fixed-columns-header.tsx |
| 70 | components/table/demo/edit-row.tsx | component demo | good | Inline row editing | components/table/demo/edit-row.tsx |
| 71 | components/table/demo/summary.tsx | component demo | good | Totals row; numeric alignment test | components/table/demo/summary.tsx |
| 72 | components/table/demo/dynamic-settings.tsx | component demo | neutral | Settings playground for every table prop; good for state-variant sweeps | components/table/demo/dynamic-settings.tsx |
| 73 | components/table/demo/virtual-list.tsx | component demo | good | Large-data virtual table | components/table/demo/virtual-list.tsx |
| 74 | components/form/demo/advanced-search.tsx | form | good | Collapsible search form above a table | components/form/demo/advanced-search.tsx |
| 75 | components/form/demo/register.tsx | form | good | Full registration form: validation, tooltips, agreement | components/form/demo/register.tsx |
| 76 | components/form/demo/login.tsx | form | good | Minimal login form | components/form/demo/login.tsx |
| 77 | components/form/demo/complex-form-control.tsx | form | good | Compound inputs within one item | components/form/demo/complex-form-control.tsx |
| 78 | components/form/demo/form-in-modal.tsx | form | good | Create-in-modal flow | components/form/demo/form-in-modal.tsx |
| 79 | components/card/demo/grid-card.tsx | component demo | neutral | Card grid; tests the "identical cards" heuristic on non-slop | components/card/demo/grid-card.tsx |
| 80 | components/statistic/demo/card.tsx | component demo | good | KPI stat cards with up/down deltas (a restrained KPI tile) | components/statistic/demo/card.tsx |
| 81 | components/descriptions/demo/border.tsx | component demo | good | Bordered key-value detail block | components/descriptions/demo/border.tsx |
| 82 | components/list/demo/vertical.tsx | component demo | good | Article feed list with actions | components/list/demo/vertical.tsx |
| 83 | components/result/demo/success.tsx (+404.tsx) | component demo | good | Result and exception states | components/result/demo/ |
| 84 | components/steps/demo/nav.tsx | component demo | good | Navigation-style steps | components/steps/demo/nav.tsx |
| 85 | components/menu/demo/inline.tsx | component demo | good | Inline side menu | components/menu/demo/inline.tsx |
| 86 | components/empty/demo/customize.tsx | component demo | good | Custom empty state with CTA | components/empty/demo/customize.tsx |
| 87 | components/border-beam/demo/basic.tsx (ant.design/components/border-beam) | component demo | slop | New "BorderBeam" decorative animated glowing border: an AI-era trend effect shipped inside a conservative DS, a positive control for decoration/glow rules | components/border-beam/demo/basic.md:7 |

## Best audit candidates
1. #1 preview.pro.ant.design/dashboard/analysis: full analytics dashboard, the conventional reference.
2. #2 /dashboard/monitor: monitoring dashboard explicitly endorsed by the visualisation spec.
3. #4 /list/table-list: the archetypal enterprise query-table screen.
4. #7 /profile/advanced: dense detail page with header, steps and tabs.
5. #11 /form/advanced-form (or #9 /user/register): long real-world form.
6. #34 spec/buttons: 7/5 Do/Don't pairs that map straight onto the hierarchy and primary-CTA rules.
7. #35 spec/copywriting: 18 correct/wrong pairs, the richest UX-writing calibration set.
8. #43 spec/research-form plus #47 spec/visualization-page: Do/Don't pairs for forms and dashboards.
9. #48 DESIGN.md: machine-readable tokens plus Do/Don'ts; tests the audit against a declared system.
10. #87 border-beam demo: a slop-trend positive control inside a "good" system, to check that the audit catches glow/beam decoration even in conventional contexts.

## Notes
- Do/Don't images are PNGs on gw.alipayobjects.com that render inside ant.design/docs/spec/*; each pair is marked with `preview-img good|bad` in the source markdown.
- Pro routes #3, #10, #11, #12, #13, #14 are standard Ant Design Pro routes that the repo does not link. Only /dashboard/analysis was spot-checked (live SPA, title "Ant Design Pro").
- Component demos are live at ant.design/components/<name> (each demo has an anchor); repo paths need only `components/<name>/demo` in the sparse checkout.
- The cases page (#26) loads its logo list (#30-33) at runtime; that list does not appear in docs/spec/cases.en-US.md.
- Everything here is pre-AI, conventional enterprise style. Expect few true slop hits; use it to measure false positives in the "conventional" profile.
