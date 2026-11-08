# Unslop report: /home/claude/refs/ui-ux-pro-max/projects/portfolio-dark/index.html

**Verdict (draft): fix**. Profile: balanced. 7 Floor finding(s) open.

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
| Integrity | 5 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] INT-002 No default cast or fake brands** (1x). hero h1, nav mark, footer  
   Evidence: Failed T-DEFAULT-AGENT: 'Hi, I'm Alex Chen', 'AC' monogram, 'Full Stack Developer'. Alex Chen is a stock generated name and there is no photo, no real link (GitHub, LinkedIn, X all href '#'), no employer, no location.  
   Fix: [DATA NEEDED: the owner's real name, photo and profile links] (remedy: fix-copy)
2. **[Floor P0] A11-001 Text contrast on real pixels** (7x). html > body.bg-background.font-body > nav.fixed.top-6 > div.max-w-6xl.mx-auto > a.bg-primary.hover\:bg-cta:nth-of-type(2)  "Let's Talk"  
   Evidence: 3.68:1 against the background behind the text (10th-percentile pixel #3b82f6, worst 3.68:1; text #ffffff, 16px; needs 4.5:1). APCA Lc 69 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
3. **[Floor P0] A11-006 Controls have accessible names** (2x). hero 'Download CV'  
   Evidence: dom-1440.json: 'Download CV' is an a with href '#contact'. It downloads nothing; it scrolls to the contact form.  
   Fix: <a href="/cv.pdf" download>Download CV (PDF, 120 KB)</a> (remedy: fix-a11y)
4. **[Floor P0] A11-007 Headings and landmarks** (2x). Featured Projects cards  
   Evidence: Project cards contain h3 titles but are not links and contain no links; a keyboard or screen-reader user (like anyone) has no way to open a project. focus.json goes straight from the hero to the form inputs.  
   Fix: <h3><a href="/work/[slug]">[Project name]</a></h3> with the card made clickable via the heading link. (remedy: fix-a11y)
5. **[Floor P0] A11-010 Form fields have labels** (1x). contact form  
   Evidence: forms.json: the form has action null and method get; pressing 'Send Message' made one request and produced no new text, so a user gets no confirmation or error. Fields have visible labels, but placeholders ('John Doe', 'john@example.com') are example data and no field shows a required state or error message.  
   Fix: action pointing at a real endpoint; required + aria-invalid on failure, an error text tied with aria-describedby, and an aria-live="polite" status after send. (remedy: fix-a11y)
6. **[Floor P0] A11-005 Images have text alternatives** (1x). hero and about decorative graphics  
   Evidence: The 'AC' circle, '</>' tile, palette tile and person-silhouette avatar are decorative; the 'AC' text inside the circle is read aloud as 'A C' a second time after the h1. Confirm they are aria-hidden.  
   Fix: aria-hidden="true" on the decorative containers. (remedy: fix-a11y)
7. **[Floor P0] INT-106 Ban unsourced stat strips: 3+ figures each over a one-word label, or round, neat, unsource** (1x). About section stats, tile 1440-03  
   Evidence: '5+ Years Experience', '50+ Projects Completed', '30+ Happy Clients': round plus-suffixed figures over one-word labels with no client named anywhere on the page; 'Happy Clients' is the stock label.  
   Fix: Name three clients or employers with dates instead of counts. [DATA NEEDED: real work history] (remedy: None)
8. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). section order  
   Evidence: T-STOCK-ORDER for a portfolio: split hero with avatar > 2x2 project cards > three-column skills list with icon tiles (Frontend / Backend / Tools & DevOps) > About with stat trio > centred 'Let's Work Together' form > footer with social icons. Every section is the stock portfolio section in the stock order; 'Portfolio', 'Expertise', 'About Me', 'Get In Touch' kickers sit over each.  
   Fix: Lead with the work (one case study, real screenshot) and fold skills into it; cut the stat trio and the quote. (remedy: None)
9. **[Reflex P1] SLP-007 No stock gradient pairs** (9x). body.bg-background.font-body > nav.fixed.top-6 > div.max-w-6xl.mx-auto > a.font-heading.font-bold:nth-of-type(1) > span.gradient-text  "AC"  
   Evidence: gradient banned pair (hues 265-330 with 200-264): #3b82f6, #8b5cf6  
   Fix: Use a flat fill or a single-hue ramp. (remedy: fix-colorize)
10. **[Reflex P1] CPY-005 No slop diction** (7x). section.min-h-screen.flex:nth-of-type(1) > div.max-w-6xl.mx-auto > div.grid.lg\:grid-cols-2 > div:nth-of-type(1) > p.text-muted.text-lg:nth-of-type(2)  "I craft digital experiences that blend beautiful d"  
   Evidence: "powerful" (buzzwords/weak-intensifiers, cap budget 3, found 6)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)
11. **[Reflex P1] A11-004 Target size** (4x). html > body.bg-background.font-body > nav.fixed.top-6 > div.max-w-6xl.mx-auto > a.font-heading.font-bold:nth-of-type(1)  
   Evidence: touch target 25x28px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
12. **[Reflex P1] SLP-003 No icon tiles above every card heading** (3x). section.py-24.px-6:nth-of-type(3) > div.max-w-6xl.mx-auto > div.grid.md\:grid-cols-3:nth-of-type(2) > div.bg-surface.p-8:nth-of-type(1) > div.w-14.h-14:nth-of-type(1)  
   Evidence: 56px tinted tile above heading "Frontend" (3 repeats)  
   Fix: Remove the tiles, or use a real image or figure that differs per card. (remedy: fix-quieter)
13. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (3x). :root --color-primary  
   Evidence: token --color-primary: #3B82F6 is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)
14. **[Reflex P1] LAY-003 Headings sit with their content** (3x). section.min-h-screen.flex:nth-of-type(1) > div.max-w-6xl.mx-auto > div.grid.lg\:grid-cols-2 > div:nth-of-type(1) > h1.font-heading.text-5xl  "Hi, I'm"  
   Evidence: 16px above the heading but 24px below it: it reads as part of the block above  
   Fix: Increase space above headings; reduce space below. (remedy: fix-layout)
15. **[Reflex P1] LAY-004 No dead bands** (2x). y 712-901 at 1280px  
   Evidence: 189px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)

10 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: contrast 1.00:1 on 'Let's Talk', 'View My Work' and 'Send Message' (white on white) is a capture artefact: the Tailwind v3 config with bg-primary was ignored by the v4 shim, so the button fills never rendered
- a11y: disputed: tag-pill contrast (e.g. #00d3f2 on #e5f7fb at 1.64:1) may also be shim colours, not the authored palette; re-run with the real Tailwind config before reporting
- a11y: focus visibility and non-text contrast of inputs not judged for the same reason
- a11y: reflow at 375 not judged beyond the sweep: the layout depends on the un-rendered config
- slop: Render fidelity: the capture shimmed Tailwind v4 for the v3 play CDN and ignored tailwind.config, so the intended dark theme, primary button fills, input borders and custom fonts (Archivo, Space Grotesk) did not render. Background, button visibility, Inter display and type-scale judgments were not made from these screenshots
- slop: eyebrow-like kickers, lexicon counts and gradient pairs: reported by the sweep, not repeated
