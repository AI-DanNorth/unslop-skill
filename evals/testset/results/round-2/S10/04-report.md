# Unslop report: /home/claude/refs/ui-ux-pro-max/projects/healthcare-dashboard/index.html

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
| Integrity | 6 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (15x). aside.w-64.bg-white > nav.p-4 > ul.space-y-1 > li:nth-of-type(1) > a.flex.items-center  "Dashboard"  
   Evidence: 3.27:1 against the background behind the text (10th-percentile pixel #ebf2fe, worst 3.27:1; text #3b82f6, 16px; needs 4.5:1). APCA Lc 56 (advisory)  
   Fix: Darken text or lighten ground; never thin weights on tinted ground. (remedy: fix-a11y)
2. **[Floor P0] ROB-003 No horizontal overflow** (1x). html > body.bg-slate-100.font-body > div.flex.min-h-screen > main.flex-1.ml-64  
   Evidence: page is 903px wide at a 375px viewport (sideways scroll); widest culprit 647px  
   Fix: Find the overflowing element; use min-width: 0, overflow-wrap, and avoid 100vw. (remedy: fix-harden)
3. **[Floor P0] A11-163 Charts provide a table alternative and text summary of the key insight** (1x). canvas in 'Patient Admissions Trend' and 'Department Distribution'  
   Evidence: dom-1440 elements 98 and 102 are <canvas> with no accessible name, no role="img", no fallback content and no data table; screen readers get nothing from either chart.  
   Fix: <canvas role="img" aria-label="Admissions and discharges per day, Mon to Sun; admissions peak Thursday at 65"> plus a visually-hidden <table> of the daily values (and department counts for the donut) (remedy: None)
4. **[Floor P0] A11-168 Never convey information by colour alone** (1x). Department Distribution donut and admissions chart legend  
   Evidence: Five departments are distinguished only by hue (blue, green, orange, violet, grey) with no values or direct labels on segments; Admissions vs Discharges only by blue vs green line.  
   Fix: Direct labels with counts on or beside each segment/line end, or replace with labelled bars (remedy: None)
5. **[Floor P0] A11-115 Expose correct state attributes: aria-expanded on menu/accordion triggers, aria-pressed/ar** (1x). Weekly / Monthly / Yearly period buttons  
   Evidence: Three plain <button>s acting as a single-select toggle; no aria-pressed or tab roles captured (role: null). The selected period is shown only by fill colour (missing in this render).  
   Fix: <div role="group" aria-label="Chart period"> with aria-pressed="true" on the active button (or a radiogroup), and a non-colour selected cue (weight or underline) (remedy: None)
6. **[Floor P0] A11-112 Every control has an accessible name** (1x). notification bell button, header  
   Evidence: Accessible name is "Notifications" while the visible badge reads "3" (focus.json text "3"); the unread count is either dropped from the name or read as a bare '3'.  
   Fix: <button aria-label="Notifications, 3 unread"> and aria-hidden on the visual badge (remedy: None)
7. **[Floor P0] A11-102 Heading levels step one at a time** (1x). h1 'HealthView' (sidebar logo), h2 'Healthcare Analytics'  
   Evidence: The only h1 is the product wordmark in the sidebar; the page's own title is an h2, and the KPI cards have no heading. Heading navigation starts at the logo.  
   Fix: Make the wordmark a link or plain text and set 'Healthcare Analytics' (or the page's real title) as the h1; add a visually-hidden h2 'Key metrics' over the KPI row (remedy: None)
8. **[Floor P0] A11-109 Keep reading order and screen-reader order equal to visual order.** (1x). sidebar nav links  
   Evidence: All five nav links have href="#" and none carries aria-current="page"; 'Dashboard' is the current page only by darker text colour.  
   Fix: <a href="/dashboard" aria-current="page">Dashboard</a> with a non-colour current marker (remedy: None)
9. **[Floor P0] INT-002 No default cast or fake brands** (1x). Recent Patients table and Upcoming Appointments list  
   Evidence: Patients "John Doe", "Sarah Miller", "Robert Johnson", "Emily Wilson" with emails at "@email.com"; appointments with "Michael Brown", "Lisa Anderson", "David Lee", "Jennifer Kim"; user "Dr. Roberts, Cardiologist". The sweep caught John Doe; the rest of the cast is the same default-name set. Failed T-FILLER: none of this data is real.  
   Fix: [DATA NEEDED: realistic or anonymised sample records from the client], with varied name lengths and scripts to stress the table (remedy: fix-copy)
10. **[Reflex P1] SLP-160 Ban the KPI wall: a greeting above four stat cards, or six gauges.** (1x). KPI row, 1440px y 117-289  
   Evidence: Four equal white cards, each an outline icon top-left, an arrow delta top-right and a big number over a grey label: 2,847 Total Patients / 94.2% Recovery Rate / 24 min Avg. Wait Time / 142 Beds Available. Failed T-DEFAULT-AGENT: 'healthcare analytics dashboard' yields exactly this row. Failed T-THREE-LINE: 'Recovery Rate 94.2%' is not falsifiable (recovered from what, over what period, for which cohort).  
   Fix: Lead with the one number this user acts on today [DATA NEEDED: the clinician's or administrator's primary daily metric, its period and its definition]; move the rest into a compact labelled row with periods ('vs last week') (remedy: None)
11. **[Reflex P1] DVZ-109 Trend over time: line (or sparkline inside a component)** (1x). Patient Admissions Trend chart  
   Evidence: Admissions and Discharges drawn as heavily smoothed splines with a teal area fill under one series only; the curves overshoot between daily points (Thu peak bulges above the 65 point), inventing values for counts that are integers per day.  
   Fix: Straight segments or daily bars for counts (DVZ-110), no area fill, direct labels at line ends instead of a bottom legend (remedy: None)
12. **[Reflex P1] SLP-221 Ban category-label section heads ("Features", "Our story", "Why us", "How it works"), "Mee** (1x). page header and section heads  
   Evidence: h2 "Healthcare Analytics" with sub "Overview of patient data and hospital metrics"; section heads "Recent Patients", "Upcoming Appointments", "Department Distribution". Failed T-RIVAL-NAME: every line stays true for any hospital dashboard. Failed T-FIVE-SECOND: for whom (which ward, which role) and what to do are unanswered.  
   Fix: State the scope and moment: '[DATA NEEDED: ward/clinic name], today, [date]' and put the one action (e.g. next appointment, patients awaiting review) first (remedy: None)
13. **[Reflex P1] SLP-010 No template chrome glyphs** (6x). div.bg-white.rounded-xl:nth-of-type(2) > div.p-4.space-y-3:nth-of-type(2) > div.p-4.rounded-lg:nth-of-type(1) > div.flex.items-center > span.font-medium.text-text:nth-of-type(1)  "Checkup - Michael Brown"  
   Evidence: template chrome (dash-labels): "Checkup - Michael Brown"  
   Fix: Delete, or replace with real content. (remedy: fix-copy)
14. **[Reflex P1] A11-004 Target size** (5x). div.flex.min-h-screen > main.flex-1.ml-64 > header.flex.items-center > div.flex.items-center:nth-of-type(2) > button.p-2\.5.rounded-lg  
   Evidence: touch target 42x42px at 375px (min 44px)  
   Fix: Enlarge the hit area with padding or a pseudo-element. (remedy: fix-a11y)
15. **[Reflex P1] CLR-002 No stock framework swatches as brand tokens** (3x). :root --color-slate-50  
   Evidence: token --color-slate-50: oklch(98.4% 0.003 247.858) is a stock tailwind-defaults swatch  
   Fix: Derive tokens from the brand source; tint neutrals toward the brand hue. (remedy: fix-colorize)

9 further findings are in 04-findings.json.

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: no forms
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: disputed: A11-001 'Weekly' 1.00:1 is a capture artefact: tailwind.config was ignored by the shim so the active button's primary fill is missing; re-check with the real build
- a11y: status pill colours (Recovered / In Treatment / Scheduled) could not be judged for colour-only meaning because their fills were lost in the shim
- a11y: keyboard operation of charts and View All: no live run
- slop: Tailwind was shimmed (manifest: tailwind.config ignored), so custom 'primary' and status-pill colours, the active 'Weekly' tab fill and avatar circle fills are missing from the render; colour choices were not judged
- slop: Fonts Fira Sans / Fira Code were shimmed; typeface judgment limited to roles
