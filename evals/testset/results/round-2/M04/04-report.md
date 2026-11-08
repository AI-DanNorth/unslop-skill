# Unslop report: /home/claude/refs/kami/site/assets/demos/demo-social-cards-mole-en.html

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
| Accessibility | 7 | from sweep |
| Usability | _lens_ | judgment lens required |
| Integrity | 10 | from sweep |
| Distinctiveness | _lens_ | judgment lens required |

Caps: an open Floor finding caps the overall score at 4; Concept at 5 or below caps it at 6.

## Findings

1. **[Floor P0] A11-001 Text contrast on real pixels** (1x). meta line 'Tw93 Open Source Family' (#8e9db3 on #1B365D)  
   Evidence: Computed 4.40:1 at 30 px regular on the 1242 canvas; it passes as large text on the full-size image but once the card is viewed in a feed (about 2.8x smaller, SOC-109) it becomes ~11 px text at 4.4:1, below the 4.5:1 normal-text threshold.  
   Fix: --social-ink-muted: #a3b0c3 (about 5.5:1 on #1B365D) (remedy: fix-a11y)
2. **[Reflex P1] A11-002 Text size floors** (1x). html > body.paper-ink > section.card.cover > div.meta:nth-of-type(1)  "Tw93 Open Source Family"  
   Evidence: 23-character run at 30px (hard floor 28px, dense UI 32px, body 36px)  
   Fix: Raise to the floor; cut words rather than shrink. (remedy: fix-typeset)
3. **[Reflex P1] SLP-214 Cap virtue words about the business (honest, calm, quiet, actually, genuine, truly, simply** (1x). tagline under h1, y 420-470  
   Evidence: "A quiet keeper for your Mac." Failed T-RIVAL-NAME: CleanMyMac, Stats or iStat Menus could all carry it. Failed T-THREE-LINE: not picturable, not falsifiable. 'Quiet' is a virtue word about the product (SLP-135 house voice: warm, modest, literary).  
   Fix: Say the job the screenshot proves, e.g. 'CPU, memory, disk and battery in the menu bar; cleans what you uninstall' [DATA NEEDED: Mole's own one-line description] (remedy: None)
4. **[Finish P3] A11-114 Meaningful images get alt describing what they show** (1x). img in .photo  
   Evidence: alt="Mole menu bar status panel" names the image but not what it tells; when posted, the platform alt text should carry the key facts the card shows.  
   Fix: alt="Mole's menu bar panel: health score 100, CPU 14%, memory 72%, disk 292 GB free, battery 80%, top processes by memory"; reuse as the post's alt text (remedy: None)
5. **[Finish P3] SOC-112 Test thumbnail legibility** (1x). screenshot panel, y 655-1550  
   Evidence: The app panel occupies about 350 x 900 px of a 1050 px wide frame; the rest is macOS wallpaper. At feed size (canvas shown ~2.8x smaller) the panel's 11-13 px-equivalent labels (CPU 14%, Top Processes) fall to about 4 px. Failed T-THUMBNAIL for the product evidence.  
   Fix: Crop to the panel (or its top half: score 100, CPU, MEM, Disk) and scale it up so the key readings stay legible in the feed (remedy: None)

## Quick wins

_(synthesize picks 3)_

## Keep

_(synthesize)_

## Not investigated

- accent_footprint (CLR-001): not-verified: fold-1242.png not captured
- flat_hierarchy (TYP-001): skipped: only 1 type roles
- spacing_monotony (LAY-001): skipped: only 6 spacing values
- dead_band (LAY-004): skipped: disabled by profile
- words_per_screen (CPY-001): skipped: disabled by profile
- page_words (CPY-002): skipped: disabled by profile
- h1_words (CPY-003): skipped: disabled by profile
- fake_send (INT-004): skipped: disabled by profile
- focus_ring (A11-003): skipped: disabled by profile
- targets (A11-004): skipped: disabled by profile
- headings_landmarks (A11-007): skipped: disabled by profile
- reduced_motion (A11-011): skipped: no animation or movement in stylesheets
- phone_parity (ROB-002): skipped: disabled by profile
- overflow (ROB-003): skipped: disabled by profile
- distinctness (SLP-011): skipped: no ledger yet (skills/ledger records deliveries)
- redesign_loss (PRC-002): skipped: redesign workflow only (no baseline_run in run.json)
- a11y: focus order, keyboard, forms, reflow: not applicable to a fixed 1242x1660 social canvas
- a11y: the exported image's alt text on the posting platform is outside this artefact
- slop: Charter is not installed in the capture environment; the type rendered as Liberation Serif (fonts.json), so the face itself was not judged
- slop: other cards in the set: only the cover was captured
