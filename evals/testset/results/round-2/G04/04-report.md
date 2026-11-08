# Unslop report: /home/claude/refs/hallmark/skills/hallmark/scripts/fixtures/exemplars/playful.html

**Verdict (draft): fix**. Profile: balanced. 1 Floor finding(s) open.

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

1. **[Floor P0] A11-001 Text contrast on real pixels** (5x). main > section.hero:nth-of-type(1) > div.container.hero__inner:nth-of-type(2) > p.lead.hero__lead  "A 200-capacity music venue in Hull, with this mont"  
   Evidence: 4.33:1 against the background behind the text (10th-percentile pixel #a25305, worst 4.20:1; text #e6e3d9, 18px; needs 4.5:1). APCA Lc 64 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Reflex P1] LAY-004 No dead bands** (2x). y 1521-1701 at 1280px  
   Evidence: 180px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
3. **[Reflex P1] CLR-001 Accent footprint within budget** (1x). first screen at 1280px  
   Evidence: saturated accent covers 80.8% of the fold (fail > 8%)  
   Fix: Keep accent on the primary action, current state and one focal element. (remedy: fix-colorize)
4. **[Reflex P1] A11-004 Target size** (1x). html > body > header.slab > div.container.slab__inner > a.wordmark  "The Boiler Room"  
   Evidence: touch target 159x17px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
5. **[Reflex P1] INT-147 Avoid the wireframe page: too many empty image slots** (1x). "Room for two hundred" section, 1440 tiles 2-3  
   Evidence: Failed T-DELETION/T-FRESH-READER on the copy: the section's only text is the captions "Doors open at 7pm." and "The first band is on at 8pm.", which repeat the hero h1 "Doors 7pm. First band 8pm." word for word; the room's capacity is also stated in the hero lead, this h2, and the facts table ("200 capacity"). Three photo slots plus a full-bleed one carry the section (photos blocked in capture, so the images themselves are not judged).  
   Fix: Captions that say what the photo shows about this room ([DATA NEEDED: stage size, bar, standing or seated, accessibility of the room]), or cut to one photo (remedy: None)
6. **[Reflex P2] A11-003 Visible focus everywhere** (2x). a "THIS MONTH’S GIGS"  
   Evidence: focus indicator visible but faint: 2.88:1 against the unfocused state (target 3.0:1, WCAG 2.4.13)  
   Fix: Use :focus-visible with a 2px ring offset 2px in a contrasting colour. (remedy: fix-a11y)
7. **[Reflex P2] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 3 font families render: Archivo, Anybody, Archivo Narrow  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
8. **[Finish P3] CPY-148 Ban stock phrases** (1x). hero h1  
   Evidence: T-RIVAL-NAME: "Doors 7pm. First band 8pm." is a schedule line any small venue could print; the specific ownership comes only from the lead ("A 200-capacity music venue in Hull"). As a poster convention it is a defensible choice, so this is a Finish note, not a Reflex.  
   Fix: Keep the poster form but let the h1 carry the venue or the next act once the bill exists ("[DATA NEEDED: next headliner]. Doors 7pm.") (remedy: None)
9. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (2x). section.listing:nth-of-type(2) > div.container.listing__grid > div.listing__text > p.lead  "Every gig goes up here with its night, its price a"  
   Evidence: last line is 18% of the measure at 1280px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
10. **[Finish P3] A11-002 Text size floors** (1x). section.listing:nth-of-type(2) > div.container.listing__grid > div.listing__text > a.btn.btn--secondary  "Hear when tickets go on sale"  
   Evidence: 28-character run at 14px (hard floor 12px, dense UI 14px, body 16px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
11. **[Finish P3] A11-007 Headings and landmarks** (1x). header nav at 375px  
   Evidence: dom-375.json: "This month", "The room" and "Hull" are hidden (vis false) with no menu control; only the wordmark and "Tickets" remain. The footer nav repeats all four, so destinations stay reachable at the page end.  
   Fix: Show the three links as a second header row at 375px, or add <button aria-expanded aria-controls> to reveal them (remedy: fix-a11y)
12. **[Finish P3] A11-010 Form fields have labels** (1x). on-sale signup form, tile 4  
   Evidence: forms.json: submit shows "Nothing was sent: this form is not connected yet."; whether it is announced (role=status / aria-live) is not recorded.  
   Fix: <p role="status" id="onsale-msg"> and aria-describedby="onsale-msg" on the email field (remedy: fix-a11y)
13. **[Finish P3] INT-006 At most two missing-fact slots** (1x). listing table and Find us, tiles 1 and 3  
   Evidence: Two missing-fact slots, within the cap of two: "This month's line-up to be announced" (the listing table, the page's reason to exist, has no rows) and "Hull, street address to be announced". The hero's primary CTA "THIS MONTH'S GIGS" lands on the empty table.  
   Fix: [DATA NEEDED: this month's gigs with night, band, price, ticket link]; until it exists, make "How tickets work" or the signup the primary hero action (remedy: fix-copy)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 6 image(s) could not load (network blocked); imagery and layout around them not verified
- a11y: disputed: sweep contrast Floor hits on the hero h1 (2.50:1) and lead (4.33:1, 3.96:1). The hero photo was blocked in capture, so the text was measured against the orange fallback gradient, not the intended photo and overlay; re-measure with the image loaded.
- a11y: Sweep focus_ring hits (2.88:1 and 2.91:1 on the hero buttons) are marginal and plausible; not disputed.
- a11y: Alt text: images were blocked and no <img> elements are present in dom-1440.json; figures have captions only.
- a11y: Whether the empty-state table row spans all four columns (colspan) is not recorded.
- a11y: Keyboard operation: no menus, dialogs or carousels; no live Playwright run.
- slop: All six Wikimedia photos were blocked; the orange and teal blocks are fallbacks, so imagery, hero overlay and photo choice were not judged.
- slop: Fonts were shimmed (Anybody, Archivo, Archivo Narrow).
