# Unslop report: /home/claude/refs/dsh-design-skills/examples/japanese-minimal-landing.html

**Verdict (draft): fix**. Profile: balanced. 9 Floor finding(s) open.

## Four-line read

- **For:** _(synthesize writes this)_
- **Works and stays:** _(synthesize)_
- **Reads generated:** _(synthesize)_
- **Broken:** _(synthesize)_

## Score

| Dimension | Score | Note |
|---|---|---|
| Concept | _lens_ | judgment lens required |
| Hierarchy | _lens_ | judgment lens required |
| Craft | _lens_ | judgment lens required |
| Accessibility | 1 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 7 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). html > body > header.hero > div.container > span.eyebrow:nth-of-type(1)  "Agent orchestration · now in GA"  
   Evidence: 1.02:1 against the background behind the text (10th-percentile pixel #c3272b, worst 1.02:1; text #6b675e, 11px; needs 4.5:1). APCA Lc 0 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] ROB-003 No horizontal overflow** (2x). html > body > header.hero > div.container > span.vertical-inscription:nth-of-type(3)  "静寂に進む — Relay 二〇二六"  
   Evidence: page is 1288px wide at a 1280px viewport (sideways scroll); widest culprit 25px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
3. **[Floor P0] A11-002 Text size floors** (1x). html > body > header.hero > div.container > span.eyebrow:nth-of-type(1)  "Agent orchestration · now in GA"  
   Evidence: 31-character run at 11px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
4. **[Floor P0] A11-101 Set lang on html, a <title> in the page's own words, a one-sentence meta description.** (1x). <html lang>  
   Evidence: dom-1440 lang is "ja" while all body copy is English; screen readers will read the whole page with Japanese pronunciation rules.  
   Fix: <html lang="en"> and lang="ja" only on the Japanese inscription span (if kept) (remedy: None)
5. **[Floor P0] A11-113 Every svg, canvas or CSS-art element carries aria-hidden="true", an aria-label, a labelled** (1x). span.seal '信', span.vertical-inscription, feature numerals 壹 贰 叁  
   Evidence: Decorative glyphs are plain text with no aria-hidden (ariaHidden: null); a screen reader reads '信' and '静寂に進む — Relay 二〇二六' between the hero lede and the trace, and '壹' before 'Intelligent routing'.  
   Fix: <span class="seal" aria-hidden="true">信</span>; same for .vertical-inscription and the numerals (remedy: None)
6. **[Floor P0] A11-112 Every control has an accessible name** (1x). hero secondary button 'Read the docs'  
   Evidence: 'Read the docs' points to #features, not to documentation; nav 'Docs' points to #docs and footer 'Documentation' to '#'. The label promises a destination the link does not reach.  
   Fix: <a href="/docs">Read the docs</a> [DATA NEEDED: docs URL] (remedy: None)
7. **[Floor P0] A11-109 Keep reading order and screen-reader order equal to visual order.** (1x). hero at 375px  
   Evidence: At 375px the red seal '信' sits over the start of the eyebrow, clipping 'AGENT' to 'NT ORCHESTRATION · NOW IN GA' (375-00.png); at 1440 and 1280 the vertical inscription pushes the page 8px wider than the viewport (sweep ROB-003).  
   Fix: display:none for .seal and .vertical-inscription below 768px, or remove them (remedy: None)
8. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). all links and buttons (focus.json, 20 stops)  
   Evidence: Every stop relies on the browser default 'outline: auto 1px'; on the vermilion #c3272b buttons ('Start free', 'Start 14-day trial', 'Get started free') a 1px dark auto ring against red is weak and not guaranteed 3:1 against both the red fill and the cream page.  
   Fix: a:focus-visible, .btn:focus-visible { outline: 2px solid #1a1a1a; outline-offset: 3px; } (remedy: None)
9. **[Floor P0] INT-001 No invented metrics** (1x). stat band and hero trace  
   Evidence: "99.99% Runs w/o intervention", "−42% Median token cost", "12ms p95 overhead", "2.3M Runs / 30 days" with no source, baseline or period for the −42%; the trace also claims "p95 latency 12ms" for a 2m14s run. Failed T-THREE-LINE on −42% (compared with what?).  
   Fix: [DATA NEEDED: measured figures with source, period and baseline], or remove the band (remedy: fix-copy)
10. **[Reflex P1] SLP-209 Ban stock phrases and filler openers (L2).** (1x). h1 and section heads  
   Evidence: h1 "Ship agent workflows with confidence"; h2 "Everything your agents need, nothing they don't"; "Start free. Scale when you're ready."; CTA "Put your agents to work — with a leash."; footer "Built for engineers who ship." Failed T-RIVAL-NAME: swap in LangSmith, CrewAI or any orchestration tool and every head stays true. Failed T-FRESH-READER: these are the generic lines.  
   Fix: A head only Relay can say, built from its own trace: e.g. 'Every agent run gets a budget, a retry and a trace' [DATA NEEDED: confirm these are Relay's defining guarantees] (remedy: None)
11. **[Reflex P1] SLP-150 Fail a centred-everything hero: title, lede, action and mark stacked on one centred axis** (1x). every section  
   Evidence: Hero, Why Relay, Drop-in config, Pricing and CTA all stack eyebrow + centred serif head + centred grey lede on one axis; pricing tiers are centred text too. Only the feature list and footer break the axis.  
   Fix: Pick one axis (left) and let the trace panel and code block sit asymmetrically against the copy (remedy: None)
12. **[Reflex P1] SLP-010 No template chrome glyphs** (8x). header.hero > div.container > div.product-panel:nth-of-type(2) > div.panel-toolbar:nth-of-type(1) > span.panel-title:nth-of-type(4)  "RELAY — SESSION #4821"  
   Evidence: template chrome (dash-labels): "RELAY — SESSION #4821"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
13. **[Reflex P1] A11-002 Text size floors** (7x). html > body > header.hero > div.container > p.hero-note:nth-of-type(2)  "NO CREDIT CARD REQUIRED · DEPLOY ON YOUR OWN INFRA"  
   Evidence: 50-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
14. **[Reflex P1] SLP-001 No eyebrow labels above headings** (5x). html > body > header.hero > div.container > span.eyebrow:nth-of-type(1)  "Agent orchestration · now in GA"  
   Evidence: 11px label tracked 0.30em caps above 56px heading "Ship agent workflowswith confidence"; 4 on page, budget 2  
   Fix: Promote the fact into the heading or delete the label (T-EYEBROW). (remedy: fix-typeset)
15. **[Reflex P1] LAY-004 No dead bands** (2x). y 1211-1409 at 1280px  
   Evidence: 198px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)

14 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: keyboard operation: no menus, dialogs or custom controls present
- a11y: disputed: A11-001 eyebrow 'Agent orchestration · now in GA' at 1.02:1 is measured against the red seal that overlaps it at narrow widths; on the cream page the eyebrow grey is about 5:1. The overlap itself is reported above.
- slop: Whether the client asked for a Japanese aesthetic: no contract supplied. Even if asked, the mixed Chinese/Japanese glyphs stand.
