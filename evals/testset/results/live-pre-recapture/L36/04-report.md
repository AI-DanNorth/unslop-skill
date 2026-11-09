# Unslop report: https://carbondesignsystem.com

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

1. **[Floor P0] A11-003 Visible focus everywhere** (11x). a "Data visualization"  
   Evidence: focused element is covered by a fixed or sticky element  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
2. **[Floor P0] A11-004 Target size** (2x). div.cds--sm\:col-span-4.cds--md\:col-span-2:nth-of-type(1) > div.cxp--footer__nav > ul > li.cxp--footer__nav-item:nth-of-type(3) > a.cds--link  "Terms of use"  
   Evidence: target 82x20px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
3. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 728 characters (100% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
4. **[Floor P0] A11-006 Controls have accessible names** (1x). cookie banner and hero tiles  
   Evidence: A link named only 'here' (#truste_domain_list) and a 'cookie preferences' link with href javascript:void(0) acting as a button. Hero tiles 'Start designing' / 'Start developing' are fine.  
   Fix: <a href="#truste_domain_list">list of IBM domains</a>; <button type="button">Cookie preferences</button> (remedy: fix-a11y)
5. **[Reflex P1] A11-004 Target size** (10x). li.cds--side-nav__item:nth-of-type(1) > button.cds--side-nav__submenu  
   Evidence: touch target 241x40px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
6. **[Reflex P1] LAY-004 No dead bands** (4x). y 1584-3200 at 1280px  
   Evidence: 1616px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
7. **[Reflex P1] ROB-001 Content never depends on animation to appear** (2x). page after load  
   Evidence: 82% of text is hidden after load and scrolling (max 30%; menus and dialogs excluded)  
   Fix: Start visible; animate from visible. (remedy: fix-harden)
8. **[Reflex P1] MOT-001 Motion CSS hygiene** (2x). div.cds--g10.cds--layer-one:nth-of-type(2) > div > div.cds--white.cds--layer-one:nth-of-type(1) > div.cxp--side-nav-wrapper.cxp--side-nav-wrapper--expanded:nth-of-type(2) > nav.cds--side-nav__navigation.cds--side-nav  
   Evidence: 9 elements transition "all" (0.15s): every property change animates, including layout  
   Fix: List the properties: transition: transform 160ms, opacity 160ms (remedy: fix-motion)
9. **[Reflex P1] WEB-001 Performance budget** (1x). page  
   Evidence: lab LCP 5216ms (fail > 4500ms)  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
10. **[Reflex P1] A11-006 Controls have accessible names** (1x). first focus stop / header  
   Evidence: Sweep: first focusable is an unnamed button (the side-nav toggle) rather than a skip link; focus.json then lists the logo link at 0,0 and the header icon buttons 'Search', 'Employee login', 'Switch sites' before the side nav and main content.  
   Fix: Add <a class="cds--skip-to-content" href="#main-content">Skip to main content</a> as first element; aria-label="Open menu" on the toggle (remedy: fix-a11y)
11. **[Reflex P1] A11-011 Reduced motion respected** (1x). scroll-linked sections, tiles 02-07  
   Evidence: Sections are revealed by scroll position (blank screens between them in the capture; 76% of text hidden after load). Content that only appears through scroll-driven animation is unavailable when motion or scripts fail.  
   Fix: Under prefers-reduced-motion: reduce and without JS, render all sections statically in flow (remedy: fix-motion)
12. **[Reflex P1] CPY-005 No slop diction** (1x). section statements, tiles 04 and 11  
   Evidence: Failed T-FRESH-READER / T-RIVAL-NAME on the large statement lines: "Pre-built, reusable assets that enable teams to build consistent digital experiences faster." and "Carbon thrives because it is built by the community, for the community. Help us build it even stronger." Swap in Material or Polaris and both stay true.  
   Fix: A statement only Carbon can make, e.g. counts and names: [DATA NEEDED: number of components, frameworks supported (React, Web Components...), IBM products using it] (remedy: fix-copy)
13. **[Reflex P2] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 3 font families render: IBM Plex Sans SmBld, IBM Plex Sans, IBM Plex Serif ExtLt  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
14. **[Reflex P2] A11-007 Headings and landmarks** (1x). page  
   Evidence: first focusable element is button "", not a skip link  
   Fix: Fix levels in markup and size with CSS. (remedy: fix-a11y)
15. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (1x). section.cxp--hero.cxp--hero--dots-visible > div.cxp--hero__left:nth-of-type(1) > div.cxp--hero__text-group:nth-of-type(3) > div.cxp--hero__body > p  "Carbon is IBM’s enterprise-ready, open-source desi"  
   Evidence: last line is 31% of the measure at 1280px (3 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- flat_hierarchy (TYP-001): skipped: only 1 type roles
- fake_send (INT-004): skipped: no forms
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 6 other request(s) blocked, e.g. script https://cloud.ibm.com/analytics/build/bluemix-analytics.min.js
- a11y: Side-nav disclosure buttons and search field not exercised live.
- a11y: Hero illustration's text alternative not found in DOM summary; assumed decorative.
- a11y: Blocked scripts may cause some empty sections; contrast of unrendered sections not checked.
- slop: Cookie consent (TrustArc) was not dismissed and sits in the focus order; not judged as design.
- slop: Many scripts were blocked (manifest network), which may explain some empty scroll sections; motion not judged from stills.
