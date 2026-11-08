# Unslop report: /home/claude/refs/dsh-design-skills/examples/dark-saas-landing.html

**Verdict (draft): fix**. Profile: balanced. 6 Floor finding(s) open.

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
| Integrity | 6 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (16x). html > body > header.hero > div.container > span.eyebrow  "Agent orchestration · now in GA"  
   Evidence: 4.44:1 against the background behind the text (10th-percentile pixel #010102, worst 4.44:1; text #5e6ad2, 13px; needs 4.5:1). APCA Lc 29 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-006 Controls have accessible names** (2x). hero 'Read the docs →'  
   Evidence: dom-1440.json: a.btn-secondary 'Read the docs →' has href '#features'; activating it scrolls to the feature cards, not documentation. The nav 'Docs' link points to '#docs', which has no matching section.  
   Fix: <a href="/docs">Read the docs</a> (real target), or relabel 'See what Relay does' if it stays an in-page link. (remedy: fix-a11y)
3. **[Floor P0] A11-005 Images have text alternatives** (2x). feature card icons, tile 1440-01  
   Evidence: Icons are Unicode text in div.card-icon (⌁ ◉ ↻ ▤ ⇄ ⚑) with no aria-hidden; screen readers announce them ('electric arrow', 'fisheye', 'clockwise open circle arrow') before each heading.  
   Fix: <div class="card-icon" aria-hidden="true">⌁</div> (remedy: fix-a11y)
4. **[Floor P0] A11-002 Text size floors** (1x). nav at 375, tile 375-00  
   Evidence: At 375 the Features / Pricing / Docs / Changelog links are removed and there is no menu button: focus.json at 1440 has them, the 375 render shows only Relay, Sign in and Get started. Primary navigation is lost on phones.  
   Fix: Add a <button aria-expanded="false" aria-controls="nav-links">Menu</button> that reveals the list, or keep the four links in a scrollable row. (remedy: fix-typeset)
5. **[Floor P0] A11-007 Headings and landmarks** (1x). page structure  
   Evidence: header, nav and footer landmarks exist but no main (sweep). Additionally there is no skip link: the first focus stop is the brand link, then 6 nav items before content.  
   Fix: <a class="skip" href="#main">Skip to content</a> as first child of body; wrap hero-to-CTA in <main id="main">. (remedy: fix-a11y)
6. **[Floor P0] INT-002 No default cast or fake brands** (1x). nav, pricing CTAs, footer (dom-1440.json hrefs)  
   Evidence: Failed T-FILLER: 'Sign in', 'Get started', all three pricing buttons, 'Get started free' and 11 of 13 footer links point to '#'. 'Read the docs →' goes to #features, not docs. 'Privacy · Terms · Security' is a plain span, not links. The footer is a link farm of destinations that do not exist.  
   Fix: Ship only links with real targets; cut Roadmap/Careers/Blog/Status until they exist; make the legal items real links. [DATA NEEDED: actual URLs] (remedy: fix-copy)
7. **[Reflex P1] CPY-005 No slop diction** (1x). hero h1 and section heads  
   Evidence: Failed T-RIVAL-NAME: 'Ship agent workflows with confidence', 'Everything your agents need, nothing they don't' and 'Start free. Scale when you're ready.' stay true for any agent-ops vendor (LangSmith, Langfuse, AgentOps). These are the three generic lines from T-FRESH-READER, and two of them are the hero and a section head.  
   Fix: Lead with the specific promise the body already makes: 'Every agent run gets a budget, a trace and a retry. No loop rewrite.' (remedy: fix-copy)
8. **[Reflex P1] A11-002 Text size floors** (11x). html > body > header.hero > div.container > span.eyebrow  "Agent orchestration · now in GA"  
   Evidence: 31-character run at 13px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
9. **[Reflex P1] A11-004 Target size** (10x). html > body > nav.nav > div.container.nav-inner > a.brand  "Relay"  
   Evidence: touch target 70x23px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
10. **[Reflex P1] SLP-010 No template chrome glyphs** (8x). header.hero > div.container > div.terminal:nth-of-type(2) > div.terminal-bar:nth-of-type(1) > span.term-title:nth-of-type(4)  "relay — session #4821"  
   Evidence: template chrome (dash-labels): "relay — session #4821"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
11. **[Reflex P1] SLP-001 No eyebrow labels above headings** (4x). html > body > header.hero > div.container > span.eyebrow  "Agent orchestration · now in GA"  
   Evidence: 13px label tracked 0.03em caps above 72px heading "Ship agent workflowswith confidence"; 4 on page, budget 2  
   Fix: Promote the fact into the heading or delete the label (T-EYEBROW). (remedy: fix-typeset)
12. **[Reflex P1] LAY-004 No dead bands** (2x). y 882-1053 at 1280px  
   Evidence: 171px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
13. **[Reflex P1] CPY-004 Dash budget** (2x). whole page  
   Evidence: 10 em/spaced en dashes (budget 2)  
   Fix: Use a full stop, comma, colon or parentheses. (remedy: fix-copy)
14. **[Reflex P1] A11-007 Headings and landmarks** (2x). footer.footer > div.container > div.footer-grid:nth-of-type(1) > div.footer-col:nth-of-type(2) > h4  "Product"  
   Evidence: heading jumps from h2 to h4  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
15. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 12 distinct font sizes: 12, 12.5, 13, 14, 15, 17, 20, 32, 36, 40, 48, 72 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)

12 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Sweep focus_ring hits (indicator 1.5:1 against unfocused) not re-verified against focus/*.png crops; no dispute raised
- a11y: eyebrow #5e6ad2 at 4.44:1 is a near miss; confirmed real by measurement but low impact
- a11y: forms: none on the page; live keyboard tests not run
- slop: brief: no 00-contract.md, so whether the indigo-on-black look is a declared brand could not be checked
- slop: eyebrows, em dashes, Inter display, type ladder: reported by the sweep, not repeated
