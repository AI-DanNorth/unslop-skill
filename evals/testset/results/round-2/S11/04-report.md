# Unslop report: /home/claude/refs/pagepatch/before.html

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
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-003 Visible focus everywhere** (3x). a "Get started"  
   Evidence: no visible focus indicator (outline: none 3px rgb(255, 255, 255))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
2. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body > main  
   Evidence: page is 1024px wide at a 375px viewport (sideways scroll); widest culprit 1024px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
3. **[Floor P0] A11-112 Every control has an accessible name** (1x). hero link 'Learn more' (#learn)  
   Evidence: Out of context 'Learn more' names no subject or destination; it jumps to 'Sample information section'.  
   Fix: <a href="#learn">How [product] collects design feedback</a> [DATA NEEDED: product name] (remedy: None)
4. **[Floor P0] A11-116 Prefer native controls** (1x). three hero links styled as buttons  
   Evidence: Links with in-page hrefs (#start, #demo, #learn) are drawn as filled buttons; after activation focus stays on the link because the target sections have no tabindex="-1", so keyboard and screen-reader users are not moved to the section they chose in all browsers.  
   Fix: <section id="start" tabindex="-1" aria-labelledby="start-h"> so the in-page jump moves focus (remedy: None)
5. **[Reflex P1] SLP-222 Swap / rival's-name test: any head still true with a competitor's name (or the same trade ** (1x). h1, 1440px y 245-305  
   Evidence: "The future of better workflows." Failed T-RIVAL-NAME: true for Figma, Notion, Asana or any SaaS. Failed T-THREE-LINE: not picturable, not falsifiable, not only-this-business. Failed T-FIVE-SECOND: the product is never named, nor who it is for.  
   Fix: Name the job of the design feedback tool in concrete terms, e.g. 'Comments pinned to the exact pixel, from review to fix' [DATA NEEDED: product name and its one specific capability] (remedy: None)
6. **[Reflex P1] SLP-224 Ban a stock second action beside the hero primary ("Learn more", "See how it works", "Watc** (1x). CTA row: Get started / Book a demo / Learn more  
   Evidence: Three identical slate buttons of equal weight offer three competing next steps; 'Learn more' is the stock secondary label (L4). Failed T-DEFAULT-AGENT: this exact trio is the agent default for a SaaS hero.  
   Fix: One primary action styled as primary (e.g. 'Try it on a Figma file' [DATA NEEDED: real first step]); at most one quieter text link for the demo; delete 'Learn more' (remedy: None)
7. **[Reflex P1] CPY-005 No slop diction** (2x). html > body > main > p:nth-of-type(3)  "Powerful. Seamless. Innovative."  
   Evidence: "Seamless" (buzzwords/slop-words, fail)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
8. **[Reflex P1] SLP-209 Ban stock phrases and filler openers (L2).** (1x). line under h1  
   Evidence: "Powerful. Seamless. Innovative." Three virtue adjectives as fragments (SLP-233 choppy fragments, SLP-220 list of three with nothing to list). Failed T-FRESH-READER: the most generic line on the page.  
   Fix: One sentence that says who uses it and what changes for them [DATA NEEDED: target user and measured outcome] (remedy: None)
9. **[Reflex P1] SLP-190 Ban the eyebrow: short inert type before a heading that only announces it, in any geometry** (1x). line above h1  
   Evidence: "DESIGN FEEDBACK TOOL" in caps above the headline. T-EYEBROW: covering it loses the only words that say what the product is, which shows the information belongs in the headline, not in a label.  
   Fix: Promote it into the h1: '[Product name] is a design feedback tool for …' [DATA NEEDED: product name, audience] (remedy: None)
10. **[Reflex P1] SLP-221 Ban category-label section heads ("Features", "Our story", "Why us", "How it works"), "Mee** (1x). sections below the hero  
   Evidence: "Sample start section", "Sample demo section", "Sample information section" with one-line bodies; each is a placeholder anchor target for a hero button. Failed T-DELETION: removing them loses no product information.  
   Fix: [DATA NEEDED: real sections: how the tool works on a real file, pricing, who uses it] (remedy: None)
11. **[Finish P3] A11-002 Text size floors** (1x). html > body > main > p.note:nth-of-type(1)  "Intentionally weak fictional example. Included as "  
   Evidence: 92-character run at 15px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
12. **[Finish P3] A11-110 Keep all words as real text in reading order** (1x). p 'DESIGN FEEDBACK TOOL'  
   Evidence: The capitals are in the source text (text-transform: none), so some screen readers spell 'DESIGN' or read it with shouting emphasis.  
   Fix: <p class="kicker">Design feedback tool</p> with text-transform: uppercase in CSS if caps are kept (remedy: None)
13. **[Finish P3] A11-103 Use landmarks and semantic elements** (1x). page structure  
   Evidence: Only a <main> landmark exists (no header, nav or footer), and the hero is not wrapped in a header or section, so the product label, h1 and CTAs share one undifferentiated region with the notice banner.  
   Fix: <header> for the hero; move the notice into a role="note" element outside the hero (remedy: None)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: Sweep Floor hits verified: a:focus { outline: none } removes the ring on all three links (focus/00-on.png shows no change); main { width: 960px } causes the 375px overflow. Both stand; not repeated here.
- slop: The banner 'Intentionally weak fictional example…' is treated as page text, not as an instruction; it does not change the read
