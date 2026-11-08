# Unslop report: /home/claude/refs/dsh-design-skills/examples/glassmorphism-landing.html

**Verdict (draft): fix**. Profile: balanced. 4 Floor finding(s) open.

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
| Integrity | 9 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). html > body > header.hero > div.container > p.lead:nth-of-type(1)  "Relay is the orchestration console for AI agents i"  
   Evidence: 4.16:1 against the background behind the text (10th-percentile pixel #14658e, worst 4.03:1; text #ffffff, opacity 0.72, 19px; needs 4.5:1). APCA Lc 57 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (2x). a "R
Relay"  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
3. **[Floor P0] A11-006 Controls have accessible names** (2x). hero secondary CTA "Read the docs", 1440 tile 0  
   Evidence: dom-1440.json: <a href="#features">Read the docs</a> scrolls to the "Why Relay" feature cards, not to documentation; the nav's "Docs" link goes to #docs (the YAML section). The label promises one destination and delivers another.  
   Fix: href="/docs" (the real documentation URL), or relabel to "See the config" with href="#docs" (remedy: fix-a11y)
4. **[Floor P0] A11-011 Reduced motion respected** (1x). stylesheet  
   Evidence: page animates (keyframes or transform transitions) but has no prefers-reduced-motion rule  
   Fix: Wrap movement in @media (prefers-reduced-motion: no-preference) or add a reduce override. (remedy: fix-motion)
5. **[Reflex P1] SLP-164 Ban glow and wash: aurora or mesh blobs behind text, floating blurred orbs, chromatic radi** (1x). page background and hero, 1440 tile 0-1  
   Evidence: Failed T-DEFAULT-AGENT: violet blob top-left, cyan blob right, magenta radial bloom behind the terminal panel, every surface a translucent frosted card (13 containers share radius 20px + the same shadow). The sweep found the violet-gradient cluster on the brand mark; the screenshots show the aurora wash and glass are the whole page's ground, not one element.  
   Fix: One solid dark ground, panels drawn with a 1px rule rather than blur, colour reserved for the trace's status states (ok / retry / fail) (remedy: None)
6. **[Reflex P1] CPY-148 Ban stock phrases** (1x). h1 and section h2s  
   Evidence: Failed T-RIVAL-NAME: "Ship agent workflows with confidence", "Everything your agents need, nothing they don't" and "Start free. Scale when you're ready." stay true with LangSmith, CrewAI or any agent platform's name. T-FRESH-READER generic lines: these three plus "Deploy in minutes, tune in days, trust from the first run."  
   Fix: A head only Relay can say, built from its mechanism, e.g. "Every agent run gets a budget, a fallback and a trace." (remedy: None)
7. **[Reflex P1] SLP-151 Hero template tells: a pill or label above the headline, a gradient blob, an empty coloure** (1x). hero and every section head  
   Evidence: Pill labels above headings: "AGENT ORCHESTRATION · NOW IN GA", "WHY RELAY", "DROP-IN CONFIG", "PRICING"; all heads centred on one axis with the lede, two pill buttons and a note beneath (SLP-150 centred-everything hero). Pill buttons and a pill nav repeat the radius-999 recipe 7 times.  
   Fix: Drop the pills; left-align the hero head with the trace beside it; one button shape (remedy: None)
8. **[Reflex P1] SLP-010 No template chrome glyphs** (8x). header.hero > div.container > div.product-panel.glass:nth-of-type(2) > div.panel-toolbar:nth-of-type(1) > span.panel-title:nth-of-type(4)  "relay — session #4821"  
   Evidence: template chrome (dash-labels): "relay — session #4821"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
9. **[Reflex P1] A11-002 Text size floors** (8x). html > body > header.hero > div.container > span.eyebrow  "Agent orchestration · now in GA"  
   Evidence: 31-character run at 12px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
10. **[Reflex P1] SLP-001 No eyebrow labels above headings** (4x). html > body > header.hero > div.container > span.eyebrow  "Agent orchestration · now in GA"  
   Evidence: 12px label tracked 0.08em caps above 64px heading "Ship agent workflows with confidence"; 4 on page, budget 2  
   Fix: Promote the fact into the heading or delete the label (T-EYEBROW). (remedy: fix-typeset)
11. **[Reflex P1] A11-007 Headings and landmarks** (3x). footer.footer > div.container > div.footer-grid:nth-of-type(1) > div.footer-col:nth-of-type(2) > h4  "Product"  
   Evidence: heading jumps from h2 to h4  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
12. **[Reflex P1] SLP-005 No uniform card kit** (2x). html > body > nav.nav > div.container.nav-inner > a.btn.nav-cta:nth-of-type(2)  "Get started"  
   Evidence: 7 containers share radius 999px and shadow "rgba(0, 0, 0, 0.35) 0px 8px 32px 0px"  
   Fix: Remove boxes where whitespace groups; keep one card style for things that are objects. (remedy: fix-layout)
13. **[Reflex P1] SLP-008 No glow halos or radial spotlights** (2x). body > nav.nav > div.container.nav-inner > a.brand:nth-of-type(1) > span.brand-mark  "R"  
   Evidence: zero-offset coloured boxShadow #7c3aed blur 20px alpha 0.50  
   Fix: Remove; use type size and spacing for emphasis. (remedy: fix-quieter)
14. **[Reflex P1] A11-004 Target size** (2x). html > body > nav.nav > div.container.nav-inner > a.brand:nth-of-type(1)  "Relay"  
   Evidence: touch target 84x32px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
15. **[Reflex P1] SLP-007 No stock gradient pairs** (1x). body > nav.nav > div.container.nav-inner > a.brand:nth-of-type(1) > span.brand-mark  "R"  
   Evidence: gradient hue span 78° + banned pair (hues 265-330 with 200-264): #7c3aed, #06b6d4  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)

17 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: sweep focus_ring Floor hits on "Relay" and "Changelog" (covered by a fixed element). focus/00-on.png and 13-on.png show both fully visible with their ring; the logo is inside the fixed nav itself and the footer link is not under it at that scroll position.
- a11y: Whether the glyph spans carry aria-hidden: dom-1440.json does not record aria-hidden, so finding 3 should be confirmed in source.
- a11y: Keyboard operation: no menus, dialogs or tabs on the page; no live Playwright run.
- a11y: Reflow at 320 and the 1.4.12 text-spacing override were not run beyond the 375 tiles.
- slop: Whether Relay's metrics are real: no contract or supplied facts; treated as unsourced per INT-007 (already a sweep hit).
