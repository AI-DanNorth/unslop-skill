# Unslop report: /home/claude/refs/hallmark/skills/hallmark/scripts/fixtures/exemplars/editorial.html

**Verdict (draft): fix**. Profile: balanced. 3 Floor finding(s) open.

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
| Accessibility | 3 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-114 Meaningful images get alt describing what they show** (1x). figure.hero__photo, figure.cup__note > div.photo, figure.cup__cup > div.photo  
   Evidence: The three content photographs are painted as CSS backgrounds on a figure/div (dom-1440: no img elements, backgroundImage on .hero__photo and .photo, no role or accessible name). The cup figures have figcaptions ('Six coffees a week', 'Sold in 250 g bags') but these caption facts, not the picture; the hero photo has nothing.  
   Fix: <img src="..." alt="[DATA NEEDED: what the photo shows, e.g. beans cooling in the roaster tray]" width height> inside each figure, or role="img" aria-label on the div if it must stay a background (remedy: None)
2. **[Floor P0] A11-122 Every interactive element has a visible :focus-visible ring at 3:1 against what it is draw** (1x). fieldset.seg radios #kind-bag / #kind-sub (order band)  
   Evidence: focus.json stop 6 lands on the radio input itself, a 1x1px visually hidden element at x69 y2886; its focus crop (focus/06-on.png) shows only a corner of a border, and whether the visible label 'One 250 g bag' gains a ring could not be confirmed from the evidence. The ring colour on this band is oklch(0.94 0.02 80) (cream) against indigo, which would pass if it is drawn on the label.  
   Fix: .seg input:focus-visible + label { outline: 2px solid oklch(0.94 0.02 80); outline-offset: 3px } (remedy: None)
3. **[Floor P0] IMG-130 Never pass library frames off as the client's own room, staff, product or region** (1x). #cup figures and hero photo (images blocked at capture; judged from footer credits)  
   Evidence: Footer credits three Wikimedia Commons library photos, one titled 'Coffee roasting machine, The Roastery, Coaltown Coffee, Ammanford, Wales'. It sits under the heading 'From a York drum to your kettle', so another roastery's machine is presented as this York roastery's drum.  
   Fix: [DATA NEEDED: a photograph of Fenwick and Daughters' own roaster]; until then use a detail-slot library frame that does not claim to be the York drum (IMG-132) or relabel the heading (remedy: None)
4. **[Reflex P1] CON-102 Name the visitor's job and build from where real sites in that category put the action, wh** (1x). whole page; order band  
   Evidence: Failed T-ANATOMY: a roastery site's core section is the coffees themselves (names, origins, notes, price). This page never names one of the six coffees, gives no price for a bag or a subscription, and the order band asks for name and email with only 'One 250 g bag' / 'A subscription' to choose from.  
   Fix: [DATA NEEDED: this week's six coffees and the bag and subscription prices]; put a coffee list above the order form and the price beside each choice (remedy: None)
5. **[Reflex P1] LAY-004 No dead bands** (3x). y 1481-1662 at 1280px  
   Evidence: 181px empty band  
   Fix: Remove the empty band or fill it with content that earns the space. (remedy: fix-layout)
6. **[Reflex P1] A11-004 Target size** (3x). footer.letter > div.container.letter__inner > div.letter__foot > nav.letter__nav > a:nth-of-type(1)  "The day book"  
   Evidence: touch target 85x22px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
7. **[Reflex P1] TYP-002 Sizes on a declared ladder** (1x). whole page  
   Evidence: 9 distinct font sizes: 14, 16, 20, 21, 31, 32, 52, 60, 84 (max 8)  
   Fix: Collapse sizes to the scale; drop the extra family. (remedy: fix-typeset)
8. **[Reflex P1] CPY-128 Say each fact once, where it does work** (1x). hero sub-line, 'Written in the day book' ledger, cup figcaptions, order h2  
   Evidence: Failed T-DELETION on the ledger: its five rows ('Coffees roasted each week 6', 'Weight of each bag 250 g', 'Ways to buy By the bag, or by subscription', 'Roastery York', 'Roasting since 1921') repeat the h1 and hero sub-line; only the bag weight is new. 'Six coffees' appears 3 times, '250 g' 4 times, 'York' 3 times, '1921' twice. The page has about five facts and spends a full screen restating them.  
   Fix: [DATA NEEDED: the six coffees (name, origin, roast, price per 250 g bag) and subscription terms]; let the ledger hold those rows instead of restating the hero (remedy: None)
9. **[Finish P3] CON-144 Avoid forced big-idea metaphors (filing cabinets, library cards, subway maps, prescription** (1x). #daybook ledger and footer 'letter'  
   Evidence: Failed T-REMOVE-DEVICE: the 'day book' metaphor (No./Entry/Kept columns, double hairline rules, 'fibre' paper texture on the hero plate) and the footer's 'letter' sign-off could be removed and the page would be no less clear. The device dresses five facts as a ledger rather than recording anything a day book would (roast dates, batches).  
   Fix: Either make it a real day book ([DATA NEEDED: roast date and batch per coffee this week]) or drop the metaphor and present the facts plainly (remedy: None)
10. **[Finish P3] ROB-004 No widows in headings and short paragraphs** (3x). section.cup:nth-of-type(3) > div.container > div.split.cup__head:nth-of-type(1) > p.lead  "Fenwick and Daughters roasts the coffee. The cup i"  
   Evidence: last line is 34% of the measure at 1280px (2 lines)  
   Fix: text-wrap: balance on headings, pretty on paragraphs (Latin only). (remedy: fix-polish)
11. **[Finish P3] A11-109 Keep reading order and screen-reader order equal to visual order.** (1x). masthead at 375px  
   Evidence: At 375 the masthead links 'The day book' and 'Order' are display-hidden (dom-375 vis false, 0x0) with no menu replacing them; the only route to the order form from the top is the hero buttons.  
   Fix: Keep 'Order' visible at 375 (e.g. right of the wordmark at 44px height) or provide a menu button (remedy: None)
12. **[Finish P3] CPY-143 Never print "Made with ♥", "<3", or a sign-off line in the footer** (1x). footer.letter: 'With thanks from the roastery,' above wordmark  
   Evidence: Footer closes with a sign-off line 'With thanks from the roastery,' then the name set at 52px, a third repetition of the wordmark on the page.  
   Fix: Remove the sign-off; use the footer for the address, opening or dispatch days ([DATA NEEDED]) and the credit line (remedy: None)
13. **[Finish P3] CPY-113 Never invent specifics to look specific** (1x). #cup lead; order lead  
   Evidence: T-FRESH-READER generic lines: 'The cup is yours to make.', 'Tell the roastery which you would like, and where to reach you.', 'Five lines the roastery keeps to.' None is a heading; they are the only lines that would fit any roaster.  
   Fix: A line only this roastery can say, e.g. [DATA NEEDED: grind or brew guidance they give, dispatch day] (remedy: None)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- capture: 3 image(s) could not load (network blocked); imagery and layout around them not verified
- a11y: verified sweep A11-004: footer links at 375 are 22px tall (real, but inline-in-text exception may apply for the credit links)
- a11y: no sweep Floor hits to verify
- a11y: forms and errors: not submitted live; required/aria-invalid wiring not visible in the evidence
- a11y: keyboard operation: no menus, dialogs or carousels present
- a11y: motion: no animation in stylesheets (reduced_motion skipped by sweep)
- a11y: reflow at 320px not captured; 375 shows no horizontal scroll or clipping
- a11y: use of colour: footer credit links are underlined; nav links rely on position, not colour
- slop: Photography: all three images were blocked at capture (manifest network.blocked), so photo choice, crop and quality were not judged; hero and cup panels show only the placeholder gradient
- slop: T-STOCK-ORDER: hero, ledger (stat-like), two-photo row, order CTA band with form, footer: 3 stock sections, under threshold
- slop: Look family: cream ground and display serif-like face hit 2 warm-paper-serif tells, but the accent is indigo not terracotta and there are no eyebrows; read as chosen, not reported
- slop: copy voice: no contract or brand samples supplied
