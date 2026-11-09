# Unslop report: https://consile.app

**Verdict (draft): rebuild**. Profile: balanced. 8 Floor finding(s) open.

## Four-line read

- **For:** _(synthesize writes this)_
- **Works and stays:** _(synthesize)_
- **Reads generated:** _(synthesize)_
- **Broken:** _(synthesize)_

## Score

| Dimension | Score | Note |
|---|---|---|
| Concept | 5 | lens-concept: T-ONE-SENTENCE and T-KIND-FIT pass on the hero, but T-SIGNATURE finds a greeting over four stat cards, T-IDEA-CARRIES fails from the second section, T-DEFAULT-P |
| Hierarchy | 4 | lens-structure: T-FIVE-SECOND and T-SQUINT pass on the first screen, but T-STOCK-ORDER finds eleven stock sections, T-COMPOSITION-RUN finds five card grids in a row, and T-SQUI |
| Craft | 4 | lens-typography (lowest of color 5, typography 4): T-LADDER fails on h2s at six sizes and h3 card titles at five, T-HEAD-TREATMENT fails on two accent-coloured heading phrases, and T-FACE-ROLES finds a second fa |
| Accessibility | 1 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 4 | from sweep |
| Distinctiveness | 5 | lens-copy: T-FIVE-SECOND passes on the hero's '2–200' and 'Free for up to 5 people', and the security and feature cards pass T-THREE-LINE, but T-HEADING-FORM finds the pro |

Overall (draft): **3.8**

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). div.landing-hero-stage.landing-hero-bento > div.landing-bento-copy.relative:nth-of-type(2) > div.relative.flex > div.mt-6.flex > a.inline-flex.items-center:nth-of-type(1)  "Start free"  
   Evidence: 2.85:1 against the background behind the text (10th-percentile pixel #f97015, worst 2.85:1; text #ffffff, 15px; needs 4.5:1). APCA Lc 59 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] A11-003 Visible focus everywhere** (2x). button "Play Consile demo video"  
   Evidence: no visible focus indicator (outline is set but nothing visible changes, so it is clipped or the colour of the ground: solid 2px rgb(249, 112, 21))  
   Fix: Add :focus-visible { outline: 2px solid; outline-offset: 2px } in a colour at 3:1 against the ground. (remedy: fix-a11y)
3. **[Floor P0] A11-004 Target size** (2x). html > body > div:nth-of-type(2) > a:nth-of-type(4)  "SaasHunt"  
   Evidence: target 64x17px at 375px, closer than 24px to another target (WCAG 2.5.8)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
4. **[Floor P0] ROB-001 Content never depends on animation to appear** (1x). scripts_off  
   Evidence: 1830 characters (27% of text) stay invisible with JavaScript off  
   Fix: Render content visible by default; animate from visible, never to visible. (remedy: fix-harden)
5. **[Floor P0] A11-011 Reduced motion respected** (1x). 'Featured on' logo marquee, tile 01-02  
   Evidence: The badge strip is an auto-scrolling marquee (tile 02 shows cards cut at both edges mid-scroll; text repeated three times in dom). No pause control visible.  
   Fix: Add a visible pause button and stop the animation on hover/focus and under prefers-reduced-motion: reduce (remedy: fix-motion)
6. **[Floor P0] A11-006 Controls have accessible names** (1x). 'Enterprise-grade by default' grid, tile 04  
   Evidence: Seven links read "Learn more" (SAML, SCIM, Audit Log Streaming, Privileged Access, Public API, Recurring Tasks), two read "Privacy" and one "View list"; out of context they do not say where they go.  
   Fix: <a>Learn more<span class="sr-only"> about SAML 2.0 Single Sign-On</span></a> (or aria-labelledby the card heading) (remedy: fix-a11y)
7. **[Floor P0] A11-005 Images have text alternatives** (1x). marquee favicons (dom-1440 img 'favicons')  
   Evidence: 28 favicon images have alt="" while the adjacent text names the site (fine), but badge images carry promotional alts like "Consile - Run your business. All in one place. | Product Hunt" and "SaasHunt Top 1 Daily Winner" repeated 4x (duplicated marquee copies), so a screen reader hears the same badge list three times.  
   Fix: Keep alts on the first set; aria-hidden="true" on the duplicated tracks (remedy: fix-a11y)
8. **[Floor P0] INT-003 No fake people or hotlinked stock** (1x). 'Featured on' marquee, tile 02, and badges strip  
   Evidence: Social proof is a scrolling wall of launch-directory badges (SaaSHub, Product Hunt, Startup Fame, 'SaasHunt Top 1 Daily Winner', KittyLaunch, Launchstag, LaunchBuff, Boost Domain Rating, Sell With Boost, 'Made with Lovable') plus G2/Capterra tiles labelled "Peer reviews" and "Software marketplace" with no rating or review count shown.  
   Fix: Show one verifiable proof (an actual G2 rating with count and link) or remove the strip; [DATA NEEDED: real customer or review count] (remedy: fix-harden)
9. **[Reflex P1] CON-004 One idea runs the whole artifact** (1x). from 'See Consile in two minutes' to the footer, 1440px (tiles/1440-01.png to 1440-07.png)  
   Evidence: T-IDEA-CARRIES fails at the second section. After the hero, the page shows no more product UI: the demo video poster is a grey panel with five initial tiles ('PR', 'TB', 'TT', 'HR', 'LV'), then 'Why teams struggle without Consile', 'How Consile solves it', a grid of about twenty identical icon cards ('Running in Minutes, Not Months', 'SAML 2.0 Single Sign-On', 'Cookie Consent'), a stat strip, 'Choose your way in', six security cards and a FAQ. None of them shows tasks and people data joined, which is the idea.  
   Fix: Show the join the hero promises: one screen where a leave approval changes the task board, or a KPI review pulls attendance, then cut the module grid to the few that prove it (remedy: explore-directions)
10. **[Reflex P1] CON-005 One real signature on the first screen** (1x). hero product frame, 1440px (tiles/1440-00.png)  
   Evidence: T-SIGNATURE finds a stand-in (draft CON-119). The dashboard opens 'Good morning, Otto' over four stat cards ('TASKS DUE 18', 'ATTENDANCE 92%', 'PEOPLE 35', 'REVIEWS 6') and a donut '92% present', in a workspace named 'Acme Studio' and labelled 'PRODUCT PREVIEW · SAMPLE DATA'. The frame shows totals, not the product's distinct object.  
   Fix: Lead with the screen only Consile has: for example a task list where each assignee shows today's attendance or leave status beside the work (remedy: explore-directions)
11. **[Reflex P1] CON-008 Refuse the default plan** (1x). whole page, 1440px  
   Evidence: T-DEFAULT-PLAN marks five moves: three numbered problem cards ('1 Tool Overload', '2 Flying Blind', '3 Manual Busywork'); small pill eyebrows on every section ('The problem', 'The solution', 'Features', 'FAQ'); a label-and-value strip between hairlines ('27 BUILT-IN MODULES', '99.9% MONTHLY UPTIME TARGET', 'Free STARTER PLAN UP TO 5 USERS'); a closing band 'Ready to run tasks, people ops, and performance from one workspace?'; a dark footer with long link columns. The page also uses a pale ground with one orange accent.  
   Fix: Merge the two security sections, drop the problem-solution pair, and order what remains by the buyer's question (remedy: fix-layout)
12. **[Reflex P1] CON-002 Every large decision belongs to this client** (1x). headings and card titles, 1440px  
   Evidence: T-RIVAL-NAME: with Connecteam or Factorial in place of Consile, 'One Platform, Zero Chaos', 'Real-Time Team Pulse', 'Workflows That Run Themselves', 'Enterprise-grade by default', 'Built with security & compliance at the core', 'Speed is a feature' and 'Questions, answered' all stay true. The hero motto '"Connecting Teams. Empowering Work."' also holds under any rival.  
   Fix: Keep the lines that only Consile can say ('Most tools only manage projects or only manage people') and rewrite the rest from product facts (remedy: explore-directions)
13. **[Reflex P1] CPY-007 Copy that survives the rival's-name swap** (1x). hero tagline, problem cards and values list, 1440, tiles/1440-00.png and tiles/1440-06.png  
   Evidence: Failed T-RIVAL-NAME: '"Connecting Teams. Empowering Work."' (hero and footer), 'Fragmented tools create chaos', 'Without a single source of truth, managers are guessing' and the values 'Built for the human at the desk', 'Better together', 'Speed is a feature', 'Accessible to everyone' stay true under BambooHR's or Connecteam's name. The sweep's lexicon_copy hit on 'Empowering' is not repeated.  
   Fix: Cut the tagline; the line under it ('Built for growing teams of 2–200') already does its job. Replace the values list with one sentence each on what the value changes in the product, or cut it. (remedy: fix-copy)
14. **[Reflex P1] WEB-001 Performance budget** (27x). /object/public/public-assets/branding/logo_1775624848333.png  
   Evidence: image is 6250px wide but shown at 28px  
   Fix: Compress, size and lazy-load images; preload the LCP asset. (remedy: fix-harden)
15. **[Reflex P1] CPY-005 No slop diction** (15x). div.mx-auto.w-full > div.landing-hero-stage.landing-hero-bento > div.landing-bento-copy.relative:nth-of-type(2) > div.relative.flex > p.landing-hero-subtitle.mt-6:nth-of-type(1)  "Most tools only manage projects or only manage peo"  
   Evidence: "calm" (buzzwords/virtue-words, cap budget 2, found 3)  
   Fix: Replace with a specific claim only this business can make, or delete. (remedy: fix-copy)

44 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 1 image(s) could not load (network blocked); imagery and layout around them not verified
- a11y: Keyboard operation of the mobile menu, FAQ accordion and video play button (no live Playwright run).
- a11y: Forms: none on the landing page.
- a11y: Text spacing (1.4.12) override not injected.
- a11y: Sweep contrast hits on the orange accent words in the h1 ('in one workspace') look real in tile 00 (orange on peach gradient); not disputed.
- color: T-DARK-MODE: the stylesheet has a dark class variant, but the capture rendered the light scheme only, so a dark theme is not verified.
- color: One image was blocked during capture; its frame is not judged for colour.
- color: The orange and green hero orbs and the hero gradient are the sweep's SLP-007 and SLP-008 hits; the Tailwind ring token and --onboarding-muted #6b7280 are its CLR-002 hits. None are repeated.
- concept: 00-contract.md is absent; visitor mode read as Persuade from the page itself.
- concept: The demo video was not played; only its poster frame was judged.
- concept: At 375 an 'Install Consile' prompt covers the lower hero (tiles/375-00.png); it is the site's own overlay, judged for concept only as context.
- copy: T-STATE-COPY: no form on the page and async.json was not captured; the FAQ answers were collapsed and not read.
- copy: T-LONG-FORM: no long-form region; landing page.
- copy: T-TERMS: the copy sheet's variants (Tasks/TASKS, Attendance/ATTENDANCE) are CSS uppercase labels in the product mock and section eyebrows; no finding.
- copy: Copy sheet: the helper did not return the h1 (hero empty); the hero was read from tiles/1440-00.png and bodyText.
- copy: Contract: no 00-contract.md in the run; judged as a Persuade landing page.
- slop: No 00-contract.md: no brief overrides or brand facts available; orange accent treated as brand colour, not judged as a tell.
- slop: Blocked image (kittylaunch badge-light.svg) not judged.
- slop: Hero motion orbs and marquee seen only as stills.
- structure: The cookie banner was dismissed by capture prep, and one third-party badge image was blocked (manifest network); neither affects structure.
- structure: type_ladder (23 sizes), flat_hierarchy, card_kit, icon_tile and phone_parity are sweep findings and are not repeated.
- structure: At 375 a "Maybe later" button sits at y=755 in the first screen; it may be a leftover overlay, so T-PHONE-ORDER was checked for section order only, which is kept.
- typography: T-PUNCTUATION: 2 straight double quotes ("Connecting Teams. Empowering Work.") and 13 straight apostrophes, no curly marks; consistent, so no finding under C32.
- typography: T-FIGURES: the figures in the product preview ("18", "92%", "32") are illustration, and the page has no comparing table.
- typography: The product preview's 10 to 12px text and its tracked caps labels are product imagery; the sweep's text_floor marks them as incidental.
- typography: Widows and small text sizes belong to the sweep.
