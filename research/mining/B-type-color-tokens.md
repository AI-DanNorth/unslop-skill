# Miner B: Typography, Colour & Surface, Tokens & System

Source short names: hallmark (HM), ui-ux-pro-max (UU), huashu-design (HS), taste-skill (TS), kami (KM), awesome-design-patterns (ADP), agent-skills (AS). Section numbers are the `## N.` headings.

---

## D05 Typography

### Families and pairing
| ID | Rule (imperative, specific) | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-001 | Limit a page to a display face and a body face (one family may do both); a third face is allowed only as an outlier with exactly one role | max 2 families + 1 outlier (wordmark, headline figure, or code); never 4+; 5+ hard fail | Reflex | M | HM §52, §290, §391; TS §57; HS §126 (max 2 CJK families) |
| TYP-002 | Count one family at multiple weights as one family; never load more than four font files | ≤4 font files | Reflex | M | HM §52; TS §57 |
| TYP-003 | Do not set the display/heading face in a UI text face or system face | banned display: Inter, Roboto, Open Sans, Poppins, Lato, Arial, Helvetica, Helvetica Neue, Segoe UI, system-ui, -apple-system | Reflex | M | HM §62, §390; HS §60, §61, §125; TS §30 |
| TYP-004 | Treat Inter (or any single UI sans) as both display and body as the top AI fingerprint; replace unless brand-mandated | Inter everywhere = #1 fingerprint | Reflex | M | HS §125, §138; HM §291 |
| TYP-005 | Do not use the over-defaulted faces as display or body unless requested or already in the project | Inter, Roboto, Open Sans, Lato, Poppins, Source Sans, Nunito, Montserrat, Raleway, Work Sans, DM Sans, Plus Jakarta Sans, Space Grotesk, system-ui, Arial, Helvetica; body serif Merriweather/Lora/Georgia; mono Courier New/system mono | Reflex | M | HM §291; TS §30; HS §61 |
| TYP-006 | Require an argument before using a saturated "tasteful" face | Playfair Display, Cormorant Garamond, DM Serif Display, Fraunces, Instrument Serif, Recoleta, Space Grotesk, Hubot Sans, Bebas Neue, Unbounded (display); Geist, Instrument Sans, Mona Sans (whole page) | Reflex | H | HM §292; HS §124, §125 |
| TYP-007 | Swap overused faces for named substitutes of the same build | Fraunces→Newsreader / Libre Caslon Text; Inter display→Archivo / Anton / Schibsted Grotesk; Space Grotesk→Schibsted / Familjen Grotesk; Playfair→Cormorant / DM Serif Display | Reflex | J | HS §125 |
| TYP-008 | Decide the source of pairing contrast before picking names: formal (serif×sans), same-family superfamily, or epoch contrast | epoch contrast needs ≥200 years pedigree gap; ~50 years looks messy | Finish | J | HS §123 |
| TYP-009 | In a serif×sans pairing, match x-heights or the visual size jumps; compensate low-x-height faces | e.g. EB Garamond +8% or `font-size-adjust` | Finish | H | HS §123, §124 |
| TYP-010 | Choose type in order: content type → language mix → style temperature → font names last; same label on different content must yield different typesetting | 4-step order | Reflex | J | HS §117 |
| TYP-011 | Pick a face by setting the real headline in 2–3 candidates of the chosen class and judging on the page; never by name, reputation or subject association | 2–3 candidates | Finish | J | HM §290 |
| TYP-012 | Use free/OFL faces unless a licence is confirmed; never specify paid faces (Söhne, Circular) as delivered fonts | Google Fonts / Fontshare default | Floor | H | HM §290, §293; HS §210; KM §53 |
| TYP-013 | Never invent typeface names | name must resolve to a real family | Floor | M | HS §61 |
| TYP-014 | Give the wordmark its own face (or the display cut/heaviest weight) on tone-rich work; a wordmark that is the body face at 600 is the undesigned default | wordmark ≠ body@600 | Finish | J | HM §64, §296 |
| TYP-015 | When a face the page is about is not supplied, name it first in the display token as a font slot, use a free same-build stand-in, and say so | one caption disclosure | Floor | J | HM §64 |
| TYP-016 | Do not set a full body paragraph in a monospace face | mono inflates line length ~30% | Reflex | M | HS §124; HM §61 |
| TYP-017 | Use monospace only for code, figures, measurements, times, prices, versions, or when mono is the declared material; mono on labels/captions/meta/table heads is costume | flag ≥4 mono labels ≤14px | Reflex | M | HM §61, §396, §298; HS §59, §60; TS §30; stageshow §13 |
| TYP-018 | Use display-only faces (single weight, hairline) only at display sizes | Instrument Serif 400 only; Cormorant ≥40px; thin/high-contrast strokes break <24px | Reflex | M | HS §124, §134 |
| TYP-019 | Prefer variable fonts; one variable file gives every weight | — | Finish | M | HM §290, §297 |
| TYP-020 | When the brand/user has fonts, use those first; brand fonts override all pairing rules | — | Floor | J | HS §117; HM §137 |

### Scale and hierarchy
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-021 | Derive sizes from a fixed modular ratio from the body size; never guess sizes | 1.2 dense UI/docs; 1.25 general web; 1.333 editorial; 1.5 posters/slides | Reflex | M | HS §118; HM §54; UU §90, §297 |
| TYP-022 | Use a fixed (non-fluid) scale on app screens | ratio 1.125–1.2, no fluid heads | Reflex | M | HM §54, §348 |
| TYP-023 | Keep every font size on a declared step; list distinct sizes after edits and collapse neighbours | flag off-scale neighbours like 12.5/13.5/14.5/17.5 | Reflex | M | KM §35; UU §90 |
| TYP-024 | Cap hierarchy levels | >5 levels cut; >6 is anti-pattern | Reflex | M | HS §118, §138 |
| TYP-025 | Separate adjacent heading levels decisively | each level ≥1.3× the next from 1024px (≥1.2× below); warn h3 within 1.3× of h2; hero ≈1.5× section head, section ≈2× item title | Reflex | M | TS §59; HM §170 |
| TYP-026 | Keep the section head (h2) large enough on marketing pages | median h2 below hero ≥40px at 1440 (target ~52px) | Reflex | M | HM §170, §399 |
| TYP-027 | Size display/hero mega-type by viewport fraction, not the scale; it is a layout element | display 3×–8× body | Finish | J | HS §118 |
| TYP-028 | Use `clamp()` for display tiers; keep body clamp narrow | h1 `clamp(2rem,1.2rem+3.5vw,4.5rem)`; display `clamp(3rem,1rem+9vw,9rem)`; body `clamp(1rem,0.95rem+0.3vw,1.125rem)` | Finish | M | HS §119; HM §55, §487 |
| TYP-029 | Fit headline size to its length | ≤20 chars full display (single word up to 7rem); 21–50 display; 51–90 small display or split; >90 rewrite | Reflex | M | HM §56 |
| TYP-030 | Keep headings to two lines (hero h1 ≤3 lines at every width); warn 22+ words or 4+ lines | — | Reflex | M | TS §30, §59 |
| TYP-031 | Never let a figure outgrow the h1/h2, and never let a heading's letters be smaller than the text under it | figure ≥1.08× h2 fails | Reflex | M | TS §59 |
| TYP-032 | Use one size per kind of element across the page (every card title, address, figure the same) | — | Reflex | M | TS §59 |
| TYP-033 | Create hierarchy with size, weight and space; when a step is unclear, widen the gap or skip a weight rather than adding an in-between size or a decorative rule | — | Reflex | J | KM §47; UU §93 |
| TYP-034 | Never size headings by level; never skip a heading level | step one level at a time | Floor | M | HM §406 |
| TYP-035 | Never shrink text to fit or to hide a content problem; cut or split instead | — | Reflex | J | KM §187, §408; TS §59; HS §171 |
| TYP-036 | Keep every word as live text, never baked into an image | — | Floor | M | TS §59 |

### Size floors per medium
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-037 | Web body text floor | 16px body (stricter, preferred); absolute prose floor 14px | Floor | M | HM §59, §398; UU §83, §298; TS §60; HS §74, §77; KM §34 |
| TYP-038 | Web running/functional text floor | running ≥12px; functional ≥11px; nothing ≤13px for notes/legal/image text (TS); 12px only for micro-labels/badges, never prose | Floor | M | HM §59, §398; TS §59; KM §34, §187; UU §236 |
| TYP-039 | Set form input text ≥16px on mobile to prevent iOS zoom | 16px | Floor | M | ADP §228, §260; HS §77 |
| TYP-040 | Native apps: base body 14–16pt, never critical text <12pt; support Dynamic Type / font scaling and test at largest size | — | Floor | H | UU §146, §147, §236 |
| TYP-041 | Slide (1920×1080) floors | body ≥24px (ideal 28–36); labels/ticks ≥16px; titles 60–120px; hero 180–240px; projected pt: title 40+, body 24+, notes 16+ | Floor | M | HS §75, §146; KM §34 |
| TYP-042 | Print/PDF floors | body ≥9pt (ideal 10–12pt); captions 8–9pt; named dense exceptions 8–8.5pt only for compact tables, running footers, resume timelines | Floor | M | KM §32, §34, §187; HS §76 |
| TYP-043 | Phone-viewed images (1080 wide) floors | body ≥36px, labels ≥28px; at 1242 wide body ≥42px, labels ≥32px; cover title ≥100px within 2 lines | Floor | M | HS §74, §167, §171 |
| TYP-044 | Social card (1080) floor | headlines ≥24px, body ≥16px absolute; recommended headline 48, sub 32, body 24, caption 18, CTA 28 | Floor | M | UU §279 |
| TYP-045 | Convert print pt to screen and slide correctly | screen px ≈ pt×1.33; slide caption pt×2.67 | Finish | M | KM §33, §34 |
| TYP-046 | Recalibrate embedded diagram text so it matches body | raise standalone sizes 1.8–2.0× when a 1000-unit drawing renders at ~0.47 scale | Reflex | M | KM §414 |
| TYP-047 | Use Song/sans or ≥200px for small numbers on phone covers when using high-contrast serifs | high-contrast serif loses thin strokes <100px | Reflex | M | HS §171 |
| TYP-048 | No light weight under 20px; no weights <400 at small sizes | — | Reflex | M | TS §58; UU §298 |

### Weights
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-049 | Limit running weights and pick them as extremes | ≤3 weights page-wide, e.g. 300/800 or 400/700 | Reflex | M | HM §53, §392 |
| TYP-050 | Load only the weights used | — | Reflex | M | HM §53, §297; UU §297 |
| TYP-051 | Disable synthetic bold/italic and load real files for every style used | `font-synthesis: none` | Floor | M | HM §53, §297, §488; KM §38; HS §131; TS §57 |
| TYP-052 | Carry display headlines with size and tight tracking rather than bold-and-big | display weight 400–500 typical | Finish | J | TS §58, §210 |
| TYP-053 | Use a single weight for a head: one weight, one style, one colour | — | Reflex | M | HM §57, §370 |
| TYP-054 | Reduce body weight on dark grounds (light-on-dark reads heavier); on raster dark social cards raise to 500 instead because it rasterises thin | web dark: −50 units (400→350); dark social card: all text 500 | Finish | H | HM §300; KM §171 |

### Leading
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-055 | Lead web body text in range | 1.5–1.65 (UI); prose pages 1.65–1.75 | Reflex | M | HM §59; UU §88, §236, §298; HS §77; TS §60 |
| TYP-056 | Never lead multi-line prose under 1.3 | 1.3 floor | Floor | M | HM §59, §398 |
| TYP-057 | Lead display heads tight and tighter as they grow; 1.2 reads as inherited | 1.0–1.15; mixed-case poster may reach 0.92 | Reflex | M | HM §55, §496; HS §121 |
| TYP-058 | Never set wrapping uppercase display under 1.0 | 1.02–1.08 recommended; non-wrapping caps lockup ≥1.02 | Floor | M | HM §55, §394, §298 |
| TYP-059 | Scale leading with line length | short lines (<30 chars) 1.4–1.5; long lines ~1.6 | Finish | M | HS §121; KM §40 |
| TYP-060 | Lead print body tighter than web | print reading 1.50–1.55; dense 1.40–1.45; 1.60+ on print body forbidden; 1.00–1.05 forbidden except extreme display | Reflex | M | KM §39, §40, §179 |
| TYP-061 | Use unitless line-height | `body{line-height:1.5}` | Reflex | M | ADP §241; UU §57 |
| TYP-062 | Give menus/controls with descenders enough leading to avoid clipping | `line-height:1` clips; use ~1.35 | Floor | M | KM §60 |

### Tracking
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-063 | Tighten Latin display tracking; never add positive tracking to Latin headings | regular width −0.02 to −0.04em; condensed/heavy 0 to −0.015em; clamp −0.045 to 0; touching letters is a fault | Reflex | M | HM §55, §496; TS §58, §210; HS §133, §138 |
| TYP-064 | Keep body copy at default tracking; never track body for effect | 0; never past 0.05em | Reflex | M | HM §59; KM §41; UU §236 |
| TYP-065 | Never set text ≤15px in uppercase, small caps or tracked past 0.03em (labels, captions, th, nav, tags, chips, meta, bylines, counts) | legal: wordmark, logo, ticker, 2–5 letter acronyms; controls ≤0.04em only when display voice is uppercase | Reflex | M | HM §60, §395, §298; TS §30; HS §59 |
| TYP-066 | Never define a label-tracking token at all | — | Reflex | M | HM §395, §492 |
| TYP-067 | Halve print tracking at slide scale; display at 40pt+ looks scattered at print values | eyebrow max 3px; display −0.5pt | Finish | M | KM §42 |

### Measure, wrapping, orphans
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-068 | Cap running-prose measure on the text element | 45–75ch, default `max-width:65ch`; screen prose ≲720px; TS caps at 62 chars | Floor | M | HM §59, §397; UU §89, §298; HS §120; KM §45; TS §59 |
| TYP-069 | Never render lines averaging ≥88 characters over ≥3 lines | 88 chars | Floor | M | HM §397 |
| TYP-070 | Never squeeze a block into a sliver | <8em (~16 chars) wide over ≥4 lines fails; short ledes/captions <200 chars may sit from 28ch | Reflex | M | HM §397 |
| TYP-071 | Set heading measure in ch on the heading element, not the wrapper | h1 20ch, h2 30ch, h3 40ch, small display ~24ch, lead 52ch | Finish | M | HM §58, §488; UU §94 |
| TYP-072 | Balance heads and pretty-wrap body (Latin) | `text-wrap: balance` on h1/h2/≥40px (≤4 lines); `text-wrap: pretty` on body | Reflex | M | HM §58, §400; HS §79, §122; UU §94 |
| TYP-073 | No one-word last line on a paragraph and no stub ending a 2–3 line head, checked at 375 and 1280 | stub <35% of previous line | Reflex | M | HM §58, §401 |
| TYP-074 | Place manual `<br>` only between phrases and verify at phone width; no blanket nbsp hacks | check at 375px | Reflex | H | HM §56, §401; UU §94 |
| TYP-075 | Give display heads `overflow-wrap: break-word` and `min-width:0`; never `anywhere` | words ≥16 chars overflow otherwise | Floor | M | HM §400; HS §122 |
| TYP-076 | Never let a button label or primary nav link wrap from 320 to 1920 | labels >24 chars at risk; footer links/tabs/breadcrumbs ≤2 lines | Floor | M | HM §407 |
| TYP-077 | Never justify without `hyphens:auto`; default left-aligned ragged right | — | Reflex | M | HM §59, §404; UU §298; KM §46 |
| TYP-078 | Centre only short display lines (cover title, short subtitle, one callout); never centre paragraphs or lists | — | Reflex | M | KM §46, §179 |
| TYP-079 | Never use all caps for running text | — | Reflex | M | HM §59; UU §298 |
| TYP-080 | Let text reflow at narrow widths, zoom and user spacing overrides; never clip in fixed-height boxes | `inline-size:min(100%,65ch); height:auto` | Floor | M | UU §57 |
| TYP-081 | Prefer wrapping over truncation; if truncating, use an ellipsis and expose full text | — | Floor | H | UU §236; TS §29 |

### Head treatments and emphasis
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-082 | Never set one word of a heading apart by colour, italic, weight, underline, stroke or highlight | flag inline em/i/span/strong/mark covering ≤40% of h1/h2 text with different colour/style/font; exception: theme signature, once, hero only | Reflex | M | HM §57, §370, §393; HS §59, §60 |
| TYP-083 | Get head stress from a line break or a second line at a second size | — | Finish | J | HM §57, §298 |
| TYP-084 | Use an italic display system only if declared on the token, applied to every head at that level, true italic | no synthesis | Reflex | M | HM §57, §393 |
| TYP-085 | Write headings in sentence case | — | Reflex | M | HM §298; TS §60 |
| TYP-086 | Keep underlines and highlights restrained | underline ≤2px thick, offset ≤0.25em; highlighter band behind x-height, not baseline | Finish | M | HM §405 |
| TYP-087 | Emphasise a number with colour or size, not colour plus bold | — | Finish | J | KM §184 |
| TYP-088 | Keep labels in the body face a step smaller, sentence case, untracked | — | Reflex | M | HM §60, §395 |

### Numerals and typographic details
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-089 | Use tabular figures wherever numbers compare (tables, stats, prices, axes, counts, display figures ≥24px) | `font-variant-numeric: tabular-nums` | Reflex | M | HM §63, §298, §402, §307; HS §129, §138; KM §58, §190 |
| TYP-090 | Add lining figures where digit height matters and when CJK and Latin digits mix | `lining-nums tabular-nums`; Georgia has only oldstyle, so lead with a digits-only face (U+0030-0039) | Reflex | M | KM §58, §190 |
| TYP-091 | Add slashed zero in data/IDs where 0 and O can confuse | `slashed-zero` | Finish | M | HS §129 |
| TYP-092 | Set figures in the body face when the display face's oldstyle figures ignore `lining-nums` | e.g. Bespoke Slab | Finish | H | HM §294 |
| TYP-093 | Use typographic quotes, apostrophes and a true ellipsis | “ ” ’ …; never straight quotes or `...` | Reflex | M | HM §63, §403; AS §155; TS §60 |
| TYP-094 | Keep a number with its unit using a non-breaking space; never break number from unit | `10 MB`, `⌘ K`, `200 ms`; seconds bare `30s` | Reflex | M | HM §63; TS §60; AS §150, §151 |
| TYP-095 | Use numerals for counts in UI copy | "8 deployments" | Finish | M | AS §152 |
| TYP-096 | Hang punctuation on pull quotes and optically align display caps/quotes/bullets | big-head opening quote ≈ −0.46em | Finish | J | HM §63, §496; KM §44 |
| TYP-097 | Scale currency glyphs without `vertical-align: super` | `font-size:0.74em; line-height:1; translateY(0.015em)` | Finish | M | KM §59 |
| TYP-098 | Enable standard ligatures only on body | `"liga" 1, "calt" 1` | Finish | M | HS §136 |
| TYP-099 | Author maths as typeset LaTeX, never Unicode pseudo-formulas or screenshots | — | Reflex | M | KM §191 |

### CJK and multilingual
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-100 | Never leave Chinese text to the bare `sans-serif`/system default | — | Floor | M | HS §127, §138 |
| TYP-101 | Order mixed fallback chains by render target: on web without unicode-range put Latin first, then CJK, then system CJK, then generic; in PDF/SVG, or with a CJK-only unicode-range subset, CJK leads | e.g. `"Geist","Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif` | Floor | H | HS §127; KM §51 |
| TYP-102 | Include a CJK fallback in every font-family that may render CJK, including mono, `pre`, `code`, footers, SVG labels | missing-glyph boxes otherwise | Floor | M | KM §30, §189 |
| TYP-103 | Never put PingFang (sans) in a serif stack; iOS has no Chinese serif, so self-host a subset | subset: regular + one heavier, WOFF2, CJK-only unicode range + full-width punct + U+201C–201D, U+2026 | Floor | M | KM §52, §189 |
| TYP-104 | Keep the CJK subset in step with all copy, including alt, aria-label, placeholder, data attributes | missing glyph silently falls back | Floor | M | KM §52 |
| TYP-105 | Subset self-hosted CJK display fonts; never block render on CJK fonts | body ~3,500 chars; display = used chars (<50KB); `font-display: swap` | Floor | M | HS §137 |
| TYP-106 | Lead CJK body looser than Latin | ~+0.2 over Latin; Chinese body 17px/1.8; long prose 1.8, lists 1.75, meta 1.6 (1.7 at phone) | Reflex | M | HS §121; KM §54; HS §77 |
| TYP-107 | Set CJK body measure shorter than Latin | 22–38 chars, best 28–32 → `max-width:36em`; captions 15–20 | Reflex | M | HS §120 |
| TYP-108 | Size Chinese body slightly larger than Latin | 17–18px | Finish | M | HS §118 |
| TYP-109 | Keep CJK tracking near zero; never apply Latin negative display tracking to CJK | body 0–0.05em (KM: 0.3pt with TsangerJinKai02); headings 0; display >60px −0.02 to 0 | Reflex | M | HS §133; KM §41, §49, §54 |
| TYP-110 | Never italicise hanzi; substitute weight, highlighter, Kai face or emphasis dots | `text-emphasis: dot` | Floor | M | HS §131 |
| TYP-111 | Use corner brackets 「」『』 for Chinese quotes; replace full-width parentheses on slides | — | Finish | M | HS §79, §132; KM §50 |
| TYP-112 | Do not hand-type spaces between Chinese and Latin (Pangu spacing) | — | Finish | M | HS §130 |
| TYP-113 | Apply `halt` to compress consecutive full-width punctuation | `font-feature-settings:"halt" 1` | Finish | M | HS §132; KM §52 |
| TYP-114 | Normalise mixed-script x-height | `font-size-adjust: from-font`; tall-x-height Latin; display-only nudge `vertical-align:-0.02 to -0.06em` | Finish | M | HS §128 |
| TYP-115 | Never set whole paragraphs in CJK display faces | fatigue after ~200 chars | Reflex | M | HS §126, §138 |
| TYP-116 | Korean screen pages: use system sans unless a Hangul serif subset (2,350+ syllables) ships | — | Reflex | H | KM §56 |
| TYP-117 | Confirm the font that actually drew CJK text before calling a document verified; re-check page fit after a font swap | fallback adds ~0.3pt/line | Floor | H | KM §189 |

### Font loading
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TYP-118 | Never show invisible text while fonts load | `font-display: swap` (or `optional`) | Floor | M | HM §63, §297; UU §64, §91; HS §137; TS §57 |
| TYP-119 | Pair each web font with a metric-matched fallback of the same build so the swap does not reflow the fold | `size-adjust`, `ascent-override`, `descent-override`, `line-gap-override`; grotesk→system-ui, serif→Georgia | Reflex | M | HM §63, §297; UU §91 |
| TYP-120 | Preconnect to the font host; preload critical WOFF2; one `<link>` per source (one family per request where the service may drop extras) | — | Finish | M | HM §297, §493; AS (preload) |
| TYP-121 | Prefer self-hosting via a build-time loader where CLS from fonts is measured; fix the actual shift source | CLS >0.1 investigate | Reflex | M | AS §289, §290 |
| TYP-122 | Native apps: embed fonts at build time, not runtime `loadAsync` | — | Reflex | M | AS §251 |
| TYP-123 | List `local()` sources before `url()` in `@font-face` | — | Finish | M | ADP §240 |
| TYP-124 | Never review or sign off a page rendering a fallback face | — | Floor | M | HM §462; TS §57 |
| TYP-125 | Measure text layout only after fonts load | — | Floor | M | HS §379 |

---

## D06 Colour, contrast & surface

### Palette architecture and derivation
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-001 | Define colour in OKLCH and derive variants at constant hue | e.g. primary `oklch(0.62 0.14 155)`, light `0.85 0.06 155`, dark `0.42 0.15 155` | Reflex | M | HM §65, §387; HS §62; UU §340 |
| CLR-002 | Source colour from brand assets, real imagery in the content, or cultural context (Sample → Converge → Justify); never from model priors or a style entry's example hex | write a one-sentence "why this colour" note | Reflex | J | HS §62, §211; HM §134 |
| CLR-003 | Converge to 2–3 chromatic colours plus one neutral set | chromatic colours separated by ΔH ≥60° or ΔL ≥0.3 | Reflex | M | HS §211 |
| CLR-004 | Write neutrals as a lightness sequence | e.g. L 0.15/0.35/0.65/0.92/0.98; 5–9 neutrals between paper and ink | Finish | M | HS §211; HM §65 |
| CLR-005 | Set paper and ink in band | light paper L 92–98, C 0.005–0.015; dark paper L 12–18, C 0.008–0.015; ink on light L 16–24, on dark L 88–96 | Reflex | M | HM §65, §300 |
| CLR-006 | Tint every neutral toward the anchor hue; no zero-chroma greys on a page with an anchor hue | chroma ≥0.005 (range 0.005–0.018); modern-minimal exempt | Reflex | M | HM §65, §409, §486; HS §329 |
| CLR-007 | Keep neutral temperature consistent; do not mix warm and cool neutrals without intent | warm: R≈G>B; cool: R<G<B; neutral R=G=B | Reflex | M | KM §14; UU §296 |
| CLR-008 | Neutrals never follow the accent; a cool accent does not license cool surfaces | — | Reflex | J | KM §23 |
| CLR-009 | Use one accent with a paired accent-ink and a focus colour on its hue | accent C 0.12–0.22; focus C 0.18–0.22, L within 5% of accent | Reflex | M | HM §65; KM §22; TS §61 |
| CLR-010 | One accent across the page, never two (unless a declared full-palette posture) | — | Reflex | M | TS §31; HM §68; HS §331; KM §10 |
| CLR-011 | Spend chroma by area | backgrounds C 0.01–0.04; primary/accent 0.08–0.15; small highlights 0.15–0.22; full-bleed >0.25 only for deliberately screen-native styles | Finish | M | HS §212 |
| CLR-012 | Never use a framework default palette as tokens | flag `#0f172a #1e293b #6366f1 #8b5cf6 #3b82f6 #f8fafc #64748b` (slate-900, indigo-500, violet-500, blue-500…) or ≥5 stock utility shades | Reflex | M | HM §70, §387 |
| CLR-013 | Question the model's favourite defaults before using them | `#0066FF` tech blue; `#D97757` terracotta; `#0D1117` + neon | Reflex | M | HS §60, §213, §58 |
| CLR-014 | Do not use violet/lavender in the page's own palette (accent, ground, gradient, glow, tint) | OKLCH hue 275–330 at C >0.05 → rotate to 255 or 345 | Reflex | M | TS §31, §250 |
| CLR-015 | Never theme a real brand from memory; extract colours from its live stylesheets and record the source | cluster to 3–6 recurring values; primary = most-used saturated value on interactive elements; refresh after 90 days | Floor | H | HM §134 |
| CLR-016 | Treat a framework default or banned look as not-a-brand; replace and say so | — | Reflex | J | HM §137 |
| CLR-017 | Lock the accent before filling any layout; on product sites take it from the product, else show candidates and let the owner choose | — | Reflex | J | KM §21, §185 |
| CLR-018 | Keep the interface 90–95% neutral; colour comes from photographs, product, work and real logos | — | Reflex | H | TS §61 |
| CLR-019 | Keep at most 2–3 colours in one component; ≤20% off-palette colours | — | Reflex | M | UU §296 |
| CLR-020 | Never define a colour by alpha; alpha is for overlays and shadows only; register solid tints instead of `rgba()` fills | translucent tags print a double rectangle | Reflex | M | HM §70; KM §17, §183; stageshow §29 §55 |
| CLR-021 | Reflect cultural hue meaning: drop chroma/add grey for traditional, raise for consumer | vermilion vs cola red; indigo vs #0066FF | Finish | J | HS §213 |
| CLR-022 | Treat a custom palette as too close to an existing theme when it shares paper band and display class and accent hue is within 20° (or 10° on hue alone) | — | Reflex | M | HM §415 |
| CLR-023 | Do not let multiple concept directions collapse to one palette | mean nearest oklab distance <0.06 = collision; three directions same background class = collision | Reflex | M | HS §69, §208 |

### Accent dosage, postures, footprint
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-024 | Declare a colour posture before building: restrained, committed, full palette, or drenched | committed: one colour 30–60% via field/paper; full: 3–4 named roles; drenched: surface is the colour | Reflex | J | HM §68 |
| CLR-025 | Keep the accent a signal under the restrained posture | ~5% of any viewport; fail >8% of the 1280×800 fold (atmospheric warn >20%, fail >30%); TS: <3% outside primary button/band | Reflex | M | HM §67, §410; KM §11, §181; TS §61 |
| CLR-026 | Restrict accent to active nav, focus ring, link hover, the primary control, the one argued chart series, and state | — | Reflex | J | HM §67; HM §144 |
| CLR-027 | Never paint a page-scale surface in the accent without a declared committed/full/drenched posture | page-scale = body, section, header, footer, hero, band, ≥40vh or ≥320px tall, inset-0 overlay; tints <0.3 alpha OK | Reflex | M | HM §410 |
| CLR-028 | Never set display-size text in the accent | ≥48px text is ink | Reflex | M | HM §410 |
| CLR-029 | Limit brand-colour accents per page/document | ≤3 accent instances per page; never several highlight colours | Finish | M | KM §184 |
| CLR-030 | Keep `destructive` reserved for delete/error; never reuse as brand accent | — | Floor | J | UU §666 |
| CLR-031 | Cap grounds per page | 3 ground tokens (main, alt, dark); >3 flat grounds warn; at most 2 background colours in a deck | Reflex | M | TS §61; HS §73, §144 |

### Contrast (WCAG and APCA)
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-032 | Body text contrast floor | ≥4.5:1 or APCA Lc 60; target 7:1 for reading text | Floor | M | HM §69, §411; UU §40, §296; HS §74, §78; TS §60 |
| CLR-033 | Large text, icons, focus rings, field edges | ≥3:1 or APCA Lc 45; large = ≥24px or ≥18px @700 | Floor | M | HM §69, §411, §455, §456; UU §296 |
| CLR-034 | Muted/secondary text is still body text | muted ≥4.5:1 (TS 4.6:1) on paper and on paper-2/surface; reserve muted for labels, dates, meta | Floor | M | HM §485; TS §60, §250; UU §668 |
| CLR-035 | Pair every fill with an on-colour chosen by luminance; accent-ink on accent | ≥4.5:1; button text must not be within 5% L and 0.05 C of its fill (fail <1.6:1) | Floor | M | HM §69, §412; UU §313, §667; KM §22; TS §61 |
| CLR-036 | When a brand accent fails contrast, darken it in lightness steps, keeping hue; keep the original for decoration only | e.g. #F97316→#EA580C | Reflex | M | UU §667; KM §22 |
| CLR-037 | Swap text colour in the same rule that paints a dark surface | any surface L <50% sets its own text colour | Floor | M | HM §69, §412 |
| CLR-038 | Never put grey text on a coloured surface | — | Reflex | M | HM §69, §412 |
| CLR-039 | Measure contrast against the real pixels behind text: every gradient stop, the darkest and lightest image region, and the textured result | worst stop fails = needs its own ground | Floor | M | HM §411, §454, §282; UU §242 |
| CLR-040 | Text over photographs sits on the calmest region over an ink scrim, or a solid plate | scrim 35–65% from text edge; ≥4.5:1; never centred white type over a busy frame | Floor | H | HM §274; UU §242 |
| CLR-041 | Never convey information by colour alone; never red and green as the only signal | colour + icon/shape + text | Floor | H | HM §70; UU §41, §236; KM §421 |
| CLR-042 | Focus ring must contrast with both page and focused control; switch ring colour on coloured bands | ≥3:1 (fail <2.95:1); default `outline:2px solid` offset 2px; inclusive styles 3–4px | Floor | M | HM §455, §483, §300; UU §347, §669, §360 |
| CLR-043 | Accent as button on ground needs visible separation | accent ≥3:1 on ground (TS); filled button <1.3:1 against surrounding ground warns; use accent for links only if ≥2.2:1 else ink | Reflex | M | TS §61, §63, §250 |
| CLR-044 | Avoid known low-contrast pairs | gray-400 on light, gray-600 on dark, gray-on-gray | Floor | M | UU §92, §347 |
| CLR-045 | Theme cross-scene/overlay elements from the scene (currentColor or computed contrast), never hard-coded | — | Floor | H | HS §386 |
| CLR-046 | Field edges at 3:1 drawn in the muted colour or as a one-step-off fill | — | Floor | M | HM §456 |

### No pure absolutes / neutrals
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-047 | Never use pure black or white as surface or text | ban `#000`, `#fff`, `oklch(0%…)`, `oklch(100%…)`; tint C ≥0.005; modern-minimal may use white paper | Reflex | M | HM §66, §408; HS §329; TS §61; KM §12; UU §296 |
| CLR-048 | Never use cool-grey stock surfaces on a warm system | e.g. `#f8f9fa`, `#f3f4f6` | Reflex | M | KM §12 |
| CLR-049 | Do not create a fifth text grey; keep text levels to the declared set and never use a grey lighter than the last text step for copy | e.g. 4 text levels | Reflex | M | KM §13 |

### Dark mode
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-050 | Derive dark mode by recipe; never `filter: invert()` or flipped greys; never reuse light-theme greys | — | Floor | M | HM §71, §299; HS §62; UU §149, §236, §242 |
| CLR-051 | Resolve light or dark mode before picking colours and make palette, style and anti-patterns agree | — | Reflex | J | UU §459, §465 |
| CLR-052 | Dark paper and ink bands | paper L 12–18% anchor-tinted (never #000); ink L 92–96% (never #fff); near-black `#121212`/`#050506` over `#000` unless true OLED | Reflex | M | HM §300, §303; UU §360 |
| CLR-053 | Elevation in dark mode is lighter, never darker | +3% L per level; cards always lighter than canvas | Floor | M | HM §300, §302, §76 |
| CLR-054 | Re-derive the accent for dark | chroma −0.02 to −0.04, L +5–10%; hue never moves on any token | Reflex | M | HM §300, §299 |
| CLR-055 | Re-space neutral L steps between new paper and ink; keep every chroma tint | — | Reflex | M | HM §300 |
| CLR-056 | Check dark hairlines against paper-2, not just paper | rule L ~26–34% | Reflex | M | HM §300 |
| CLR-057 | Hold every contrast pairing identically in both modes; fix the derivation, never the requirement | — | Floor | M | HM §299, §303; UU §242 |
| CLR-058 | Turn drop shadows off on dark; use lightness steps or an inset hairline ring | `box-shadow: inset 0 0 0 1px var(--color-rule)` | Reflex | M | HM §302; stageshow §29 |
| CLR-059 | Keep one heading colour on dark | all headings ink | Finish | M | HM §302 |
| CLR-060 | Never invert/brightness-filter raster images for dark; pick dark/mid-tone photos or plate light ones | — | Reflex | M | HM §302 |
| CLR-061 | Re-derive chart marks for dark (chroma down, L up), gridlines from dark rule; halve sparkline fill opacity | — | Reflex | M | HM §302, §309 |
| CLR-062 | Give duotone/multiply plates and grain a dark-mode pair; grain specks turn light | — | Reflex | H | HM §302, §284 |
| CLR-063 | Set `color-scheme: light dark` on `:root` | — | Reflex | M | HM §301; UU §371 |
| CLR-064 | Prevent wrong-mode flash: read stored mode before first paint; explicit attribute beats media query; disable transitions during theme change | — | Reflex | M | HM §301; UU §338 |
| CLR-065 | Ship dual mode only when asked; a dark theme is not a dual-mode page | — | Finish | J | HM §299 |
| CLR-066 | Do not force light-only material styles (neumorphism, e-ink, clay/pastel) into dark | — | Reflex | J | UU §360 |
| CLR-067 | Keep surfaces, dividers and pressed/focused/disabled states distinguishable in both themes | — | Floor | H | UU §242 |

### Gradients, glow, glass
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-068 | Ban the slop gradient pairings anywhere, text clips included | purple→blue (stop in 265–330° with one in 200–264°); purple→pink (purple with 331–25°); cyan 170–230° on dark (paper L <40%); counts only stops C >0.04, alpha >0.05 | Reflex | M | HM §70, §371; HS §60 |
| CLR-069 | Cap gradient stops | ≤3 stops; no two-stop decorative gradients; no rainbow or full-screen mesh | Reflex | M | HM §70; TS §32; HS §60 |
| CLR-070 | Do not clip gradients to text, except a single-hue token ramp | stops ≤40° hue apart, still passing contrast | Reflex | M | HM §70, §372 |
| CLR-071 | Ban glow and wash: aurora/mesh blobs behind text, floating blurred orbs, chromatic halos, coloured zero-offset glow | orb = positioned pseudo-element blur >40px; glow = blur >20px, C >0.04; atmospheric max 2 fixed radial blooms each 20–30% of canvas, never animated | Reflex | M | HM §70, §373; HS §60 |
| CLR-072 | Do not use glass panels (backdrop blur over translucent near-white/near-black) by default; where a system style requires glass, keep it to navigation/controls, text ≥4.5:1, and an opaque reduced-transparency fallback | restrained recipe e.g. blur 10–20px, saturate 150% | Reflex | H | HM §373; UU §359, §367, §448; HS §79; TS §32 |
| CLR-073 | Get depth from lightness steps and neutral shadows with real offset, not colour | — | Reflex | J | HM §70, §373 |
| CLR-074 | Do not use gradients in chart marks; a sparkline fade-fill is the one sanctioned chart gradient | — | Reflex | M | HM §306 |

### Shadows and elevation
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-075 | Use at most one shadow recipe; default card shadow none | e.g. `0 1px 2px oklch(20% 0.01 h / 0.05)` or `0 0 0 1px oklch(30% 0.01 h / 0.06)` | Reflex | M | HM §76, §488; KM §75 |
| CLR-076 | Tint shadows from the ink with real offset; never pure-black heavy shadows | ban `0 2px 8px rgba(0,0,0,0.3)` and kin; light lift `0 1px 2px @5%` + `0 18px 40px -22px @22%` | Reflex | M | HM §498; KM §75 |
| CLR-077 | Never combine a 1px hairline border with a wide soft shadow | blur ≥24px | Reflex | M | HM §76, §378 |
| CLR-078 | Card: border or shadow, never both; never stack fill + border + radius + shadow on one component | — | Reflex | M | HM §74; KM §74, §75 |
| CLR-079 | Reserve shadows for things that float (popovers, real screenshots, dialogs); never to make an ordinary card important; no resting blurred shadow on cards | linked card may lift 2px on hover | Reflex | J | KM §75; TS §216, §1485 |
| CLR-080 | Elevated surfaces are never darker than their canvas | — | Floor | M | HM §76, §302 |
| CLR-081 | Avoid the "product chrome" look | tight grotesk @600 on near-white, one blue accent, 1px border under soft shadow | Reflex | J | HM §76 |
| CLR-082 | Avoid the SaaS card kit | same radius + same shadow repeated ≥4 times; same box recipe on ≥6 selectors | Reflex | M | HS §58, §68; HM §377 |
| CLR-083 | No mark shadows or 3D in charts; no shadowed or gradient buttons | — | Reflex | M | HM §306; TS §63 |

### Surfaces and borders
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-084 | Climb the surface ladder in order and vary rungs by seam | whitespace → 1px hairline → tinted well (paper-2/3, no border) → card | Reflex | J | HM §74, §385 |
| CLR-085 | Step paper tones for wells and bands | ~3–4% L per step | Finish | M | HM §495, §300 |
| CLR-086 | Never white cards on a tinted page, a card in a card, a bordered box in a well, or more than two boxes deep | — | Reflex | M | HM §74, §375; TS §32, §53, §94 |
| CLR-087 | Draw lines only to separate regions, encode state, or carry data; delete decorative ticks, side bars, callout edges | — | Reflex | J | KM §73 |
| CLR-088 | Never use a thick coloured side stripe on a card | ≥3px one side; e.g. radius 12 + 4px left accent | Reflex | M | HM §374; HS §60 |
| CLR-089 | Use one divider language; no border-top+bottom on every row of long lists (>5 items) | — | Reflex | M | HM §74; TS §29 |
| CLR-090 | Avoid a sub-1pt closed border plus radius (renders as double ring) | — | Finish | M | KM §196 |
| CLR-091 | Edge photographs with an inset hairline outline rather than a border | ~6–8% ink | Finish | M | HM §498 |
| CLR-092 | Ghost (outline-only filler) cards are a tell | — | Reflex | H | HM §74 |

### Radius
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-093 | Make nested radii concentric | inner = outer − padding, ≥2px | Reflex | M | HM §78; HS §1300 (inner 9 in card 14); stageshow §18 |
| CLR-094 | Use one radius per nesting level from one radius family | e.g. lg cards/frames, md panels, sm controls; md = r−2px, sm = r−4px | Reflex | M | HM §78; TS §62; UU §337 |
| CLR-095 | Limit pill radius to controls, tags, badges | pill on ≥5 non-control selectors is a tell | Reflex | M | HM §78, §377, §497; KM §195 |
| CLR-096 | Match radius to material/genre | print-like 0–2px; modern-minimal 8px; atmospheric 12px; print docs 2–6pt (≥8pt screen only) | Finish | J | HM §497; KM §76, §195 |
| CLR-097 | Never use radius alone to create emphasis | — | Finish | J | KM §76 |
| CLR-098 | Image radii scale | `min(1vw, var(--radius-card))` | Finish | M | HM §78 |
| CLR-099 | iOS/RN: add continuous corner curves | `borderCurve: 'continuous'` | Finish | M | AS §245 |
| CLR-100 | Apply radius directly to view-transition captured elements | radius is lost otherwise | Reflex | M | AS §89 |

### Texture
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-101 | Use texture only when the theme names it or the lineage is print; one artifact family per page | grain/halftone/misregistration/scanline/deckle, never two | Reflex | M | HM §281, §289; TS §32 |
| CLR-102 | Cap texture opacity | page-wide ≤0.08; card/plate ≤0.15; under body text ≤0.05; low-frequency wash (baseFrequency ≤0.02) ≤0.12 | Floor | M | HM §282 |
| CLR-103 | Never animate texture; make overlays inert | `pointer-events:none; aria-hidden="true"`; CSS/data-URI SVG only | Reflex | M | HM §283; TS §32 |
| CLR-104 | Never put grain or halftone under/over type, UI or photographs | — | Reflex | M | HM §285; TS §32 |
| CLR-105 | Build grain to read as discrete specks | feTurbulence fractalNoise baseFrequency 0.85, numOctaves 2, alpha = noise×9−4, tile 200px | Finish | M | HM §284 |

### Browser surfaces
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| CLR-106 | Theme the parts you did not draw from the palette | `::selection`, `caret-color`, `scrollbar-color`, focus ring, underlines | Finish | M | HM §72, §414 |

---

## D04 Tokens & system

### Tiers and naming
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TOK-001 | Keep one token file as the single source of truth; every other format is a translation | — | Reflex | M | HM §138, §349; UU §307 |
| TOK-002 | Never write a colour or font-family literal outside the token block (rules, inline styles, components) | no raw hex in components | Reflex | M | HM §413; UU §236, §242, §307, §461, §288 |
| TOK-003 | Never write a raw spacing length where a token of that value exists; allow at most three deliberate optical nudges | off-scale nudges ≤3 | Reflex | M | HM §73, §416 |
| TOK-004 | Layer tokens primitive → semantic → component; components reference semantic, never primitives | `--color-blue-600` → `--color-primary` → `--button-bg` | Reflex | M | UU §307, §308 |
| TOK-005 | Name tokens by role, never by value | `--color-ink` not `--color-black`; `destructive` not `red`; `muted` not `gray` | Reflex | M | HM §65, §138; UU §308 |
| TOK-006 | Follow a consistent naming pattern | `--{category}-{item}-{variant}-{state}` | Finish | M | UU §308 |
| TOK-007 | Keep one name per role across sibling products; change value, keep name, record why; no synonyms | — | Reflex | M | KM §24; HM §491 |
| TOK-008 | Use canonical names | gutter (not page-gutter), container (not page-max), ease-out (not ease-standard) | Finish | M | HM §491 |
| TOK-009 | Map onto a project's existing token names (`--background`, Tailwind `@theme`) rather than adding a parallel set | — | Reflex | J | HM §349, §138 |
| TOK-010 | Declare every extra token in the source file; nothing downstream uses an undeclared name | — | Floor | M | HM §348 |
| TOK-011 | Never ship a token still holding a placeholder value | — | Floor | M | HM §494 |
| TOK-012 | Keep scales (space, type, easing, duration, layers) with the tokens | — | Reflex | M | HM §138, §348 |

### Required token set
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TOK-013 | Define the required colour roles | paper, ink, muted, rule, accent, accent-ink, focus; full palette adds paper-2, paper-3, ink-2; plus error, success | Reflex | M | HM §348, §484 |
| TOK-014 | Alternatively, cover the shadcn-style role set, each fill with a foreground | background, foreground, card, popover, primary, secondary, muted, accent, destructive (each +foreground), border, input, ring, radius | Reflex | M | UU §313, §336, §461, §666 |
| TOK-015 | Define type, shape and motion tokens | display/body/outlier fonts, text steps, display tracking, display weight; card radius, pill radius, hairline, card shadow; ease-out/in/in-out, 120/220/420ms | Reflex | M | HM §348, §484 |
| TOK-016 | Pair every fill token with an on-colour token; `card-foreground` equals `foreground` | — | Floor | M | UU §313, §667 |
| TOK-017 | Validate token contrast pairs at definition time | ink-2/paper, muted/paper, muted/paper-2, accent-ink/accent ≥4.5:1 | Floor | M | HM §485 |
| TOK-018 | Enforce neutral chroma floor at token level | paper…rule C ≥0.005 | Reflex | M | HM §486 |
| TOK-019 | Use a fixed z-index ladder token | e.g. 1, 10, 100, 200, 300, 400, 500, 600 (base→tooltip) | Reflex | M | HM §77, §489; UU §312 |
| TOK-020 | Use one spacing scale on a 4px base | HM: 2,4,8,12,16,24,40,64,96,144; TS: 4…128; values >2px multiples of 4 | Reflex | M | HM §73, §416, §417; TS §55; UU §310, §467 |
| TOK-021 | Use one type scale token set | e.g. 0.8125, 0.875, 1, 1.25, 1.5625, 1.953, 2.441rem (1.25) | Reflex | M | HM §487; UU §311 |

### One system / drift detection
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TOK-022 | Never add a second grid, spacing scale, type scale, radius family, button, card recipe, hairline or link style | text links in ≥3 looks warn | Reflex | M | TS §53 |
| TOK-023 | Detect value drift: list distinct sizes/colours/radii/shadows in the stylesheet and confirm each maps to a declared step | — | Reflex | M | KM §35; HM §413 |
| TOK-024 | Detect container monotony: same box recipe on ≥6 selectors | — | Reflex | M | HM §377 |
| TOK-025 | When a component wants a new value, take the nearest existing step; amend the system with a variants section rather than overriding locally | — | Reflex | J | KM §35; HM §140 |
| TOK-026 | Keep diagrams and charts on the document system | 0 new colours, 0 new fonts | Reflex | M | KM §339 |
| TOK-027 | Treat one token renamed in one place and not another as a drift bug | — | Reflex | M | KM §24 |

### Theme parity
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TOK-028 | Override only the semantic layer per theme; a theme switch is a token swap, not a redesign | — | Reflex | M | UU §315, §360; HM §301 |
| TOK-029 | Put light tokens at base and only the moving tokens in the dark block, mirrored under `prefers-color-scheme` for unset mode | `[data-mode="dark"]` + `@media (prefers-color-scheme: dark){:root:not([data-mode])}` | Reflex | M | HM §301 |
| TOK-030 | Scope alternate brand themes with data attributes | — | Finish | M | UU §339 |
| TOK-031 | Test both themes numerically; never infer dark from light | — | Floor | M | HM §303; UU §242 |

### Framework mapping and export
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TOK-032 | Tailwind v4: put colour/font/text/tracking/radius/shadow/ease tokens in `@theme static`; base styles in `layer(base)` | — | Finish | M | HM §350 |
| TOK-033 | Never name a token `--spacing-<name>` in Tailwind v4 | `--spacing-xl:40px` makes `max-w-xl` 40px | Floor | M | HM §350 |
| TOK-034 | Put `@import` of tokens before any rule (after last import) | CSS drops a later `@import` silently; Tailwind v3 imports above `@tailwind` | Floor | M | HM §138, §349, §351 |
| TOK-035 | Watch Tailwind name collisions on partial adoption | `--text-xs/sm/lg/xl/2xl/3xl`, `--ease-*` | Reflex | M | HM §350 |
| TOK-036 | Keep design annotations in the source stylesheet (Tailwind strips comments) | — | Finish | M | HM §350 |
| TOK-037 | shadcn mapping: keep shadcn `accent` (hover surface) and `muted` out of the system's own accent/muted meaning, or rename | — | Reflex | J | HM §353 |
| TOK-038 | Export DTCG JSON with `$type` on every token; keep OKLCH as strings; note hex conversion is lossy; fluid sizes export max | — | Finish | M | HM §352; UU §308 |
| TOK-039 | Extend the framework theme rather than inlining arbitrary values | — | Reflex | M | HM §138 |
| TOK-040 | Treat existing stylesheets as append-only; reuse the project's token names | — | Reflex | J | HM §138 |
| TOK-041 | Import primitives through a local design-system layer so appearance changes in one place | — | Finish | M | AS §255 |

### Extraction and documentation
| ID | Rule | Values / thresholds | Tier | Check | Sources |
|---|---|---|---|---|---|
| TOK-042 | Read context in priority order: user design system → codebase tokens/components → live product screenshots → brand guidelines → competitor reference → known system fallback (declared as a starting point) | — | Reflex | J | HS §30 |
| TOK-043 | Lift exact values from token files and 2–3 representative components; trust code over Figma/screenshots; never redraw from memory | ≥30 specific values before claiming context | Floor | H | HS §31; HM §134 |
| TOK-044 | State the extracted/planned system before building and get confirmation | colours with source file, display/body/mono, spacing scale, shadows, radii, component vocabulary, ≤2 backgrounds | Reflex | J | HS §32, §73, §144 |
| TOK-045 | Lock a system only on request or when work spans >1 page; write it from actual tokens (~45 lines); never overwrite an existing system | — | Finish | J | HM §139 |
| TOK-046 | After lock, every later decision defers to the system; pages differ only in shape | — | Reflex | J | HM §140 |
| TOK-047 | Record decisions and waivers at the top of the stylesheet; never record a pass count you did not verify | within first 40 lines | Floor | H | HM §141; HS §33 |
| TOK-048 | Keep palette notes with tokens so intent survives handoff; document each colour with name, value and usage | — | Finish | J | UU §461, §295, §307 |
| TOK-049 | A theme must not prescribe small caps, label tracking, eyebrows, uppercase labels tracked >0.045em, raw durations, named black/white, colour literals | theme description <8,000 bytes | Reflex | M | HM §492 |
| TOK-050 | Register any new semantic/state colour formally before use; off-palette values are violations | — | Reflex | M | KM §16, §17 |

---

## Named tests
- **Squint test**: blur the words (or squint); each section must keep a shape and the page a heavy/light rhythm; pass = hierarchy reads without text. HM §151, §210.
- **Label transform-delete test**: remove `text-transform` and tracking from a label and reread; if the body face a step smaller says the same, the caps/tracking were machine costume. HM §60.
- **Eyebrow deletion test**: delete the short line above a heading; if nothing but a name for what follows was lost, it was an eyebrow. HM §369.
- **"Why this colour" sentence (Sample→Converge→Justify)**: write one sentence tracing each primary to brand asset, content imagery or culture; failure to write it = copied formula. HS §211.
- **Warm-grey mnemonic**: inspect `rgb()`; warm = R≈G>B; cool R<G<B or neutral R=G=B fails on a warm system. KM §14.
- **Ladder audit**: list every distinct font size in the stylesheet; pass = each is a declared step. KM §35.
- **Accent footprint count**: at the 1280×800 fold, sum solid accent fills, large accent headings and accent bands; pass ≤5%, fail >8% (restrained). HM §67, §410.
- **Gradient-stop contrast**: compute text contrast against every gradient stop / darkest and lightest image pixels; pass = worst stop meets floor. HM §411, §454.
- **Dark verification**: run every token contrast pair numerically in both modes; pass = identical targets met. HM §303.
- **Near-theme distance**: same paper band + display class + accent hue within 20° (10° hue-only) = too close. HM §415.
- **Palette collision (oklab)**: area-weighted symmetric mean nearest oklab distance <0.06 between directions = collision. HS §69.
- **Look-family detectors**: warm-paper serif (bg L>0.9, hue 40–110°, C≥0.003 + terracotta within oklab 0.07 of #D97757 or serif head); dark single-accent (bg L<0.2, one colour C>0.15); hairline newspaper (≥8 elements >200px with 1px borders, >90% zero radius); card kit (same radius+shadow ≥4). HS §68; HM §386.
- **Line deletion test**: hide a line/rule; if meaning, state, grouping and navigation survive, delete it and restore the pause with spacing. KM §73.
- **CJK line-ending audit**: across 320–1600px in WebKit and Chromium, count non-last lines ending >1.2em short and any line-start punctuation. KM §55.
- **Widow check**: inspect paragraphs and 2–3 line heads at 375 and 1280; pass = no single-word last line, no stub <35%. HM §401.
- **Font-actually-rendered check**: confirm the drawn face (not the declared stack) before sign-off; fallback visible = fail. HM §462; KM §189.
- **Context-lift threshold**: count specific values read from the codebase; <30 = still working from impression. HS §31.
- **Brand attestation**: brand spec carries source URL and "derived, not remembered"; refresh 90 days. HM §134.

## Conflicts
1. **Web body floor**: 16px (HM, UU, TS reading text) vs 14px prose (KM, HS web). Card uses 16 as floor for web body, 14 as hard absolute.
2. **Body leading**: web 1.5–1.65 (HM), 1.5–1.75 (UU), 1.5–1.8 (TS); print 1.50–1.55 with 1.60+ banned (KM). Medium-specific; keep both.
3. **Weights**: HM ≤3 weights as extremes; HS says "only two weights" is an anti-pattern, use 300–900 expressively; KM serif 400/500 only, ban 100/900; TS text 400/500, never 700/800; UU headings 600–700.
4. **Tracked caps labels**: HM bans >0.03em at ≤15px and any uppercase labels; HS allows uppercase Latin micro-labels 0.08–0.15em; KM makes +0.5–1pt mandatory on all-caps overlines; UU all caps 0.05em, small caps 0.1em.
5. **Banned faces**: HM bans Lora/Merriweather body, Work Sans, DM Sans, Inter as body; HS recommends Lora+Hanken, Cormorant+Work Sans, Archivo+Inter (Inter body); TS library ships Fraunces, Instrument Serif, Lora pairings; UU defaults Inter/Inter; KM uses Inter for Korean Latin UI.
6. **Mono for labels**: HM bans mono labels outside code; HS lists Geist/JetBrains Mono for labels/numbering in technical direction; TS allows mono UI fragments on tech pages.
7. **text-wrap balance/pretty**: required on Latin (HM, HS); banned on CJK (KM §55) while HS says pretty helps mildly on Chinese and recommends `line-break: strict` which KM bans.
8. **CJK fallback order**: HS Latin first always; KM CJK first in PDF/SVG and when a unicode-range subset is used.
9. **Accent footprint**: HM ~5% fail 8%; KM ≤5%; TS <3% outside button/band; UU 60/30/10 puts accent at 5–10%.
10. **Pure black**: HM bans #000/#fff; UU allows #000 for true OLED and #111 as text; HS lists `#0B0B0B`/`#111` "instead of black" among template chrome.
11. **Glass**: HM bans glass panels; UU permits glassmorphism/Liquid Glass with contrast and reduced-transparency fallback; HS allows restrained glass.
12. **Gradients**: TS bans gradients on non-tech pages; HM allows ≤3 stops outside banned hue pairs.
13. **Card shadow/radius defaults**: HM card shadow none, radius 4px; UU card radius 12px + shadow-md, hover lift; KM flat 8px screen; TS soft 8/12/20.
14. **Dark weight**: HM reduce body weight 50 on dark; KM raise all dark social-card text to 500 (raster).
15. **Hierarchy method**: AS §250 (RN) says one font size, hierarchy via weight/grey; all others use a modular scale.
16. **Colour channel format**: UU HSL channels for opacity modifiers; HM OKLCH and no alpha-defined colours.
17. **z-index ladder**: HM 1–600 vs UU 0–50 then 1000–1400. Pick one per project; rule is "one fixed ladder".
18. **Font hosting**: HM/TS Google Fonts default; AS prefers self-hosted build-time loading.
19. **Muted contrast target**: HM 4.5:1, TS 4.6:1, TS reading text 7:1.

## Theme-specific, keep in library
- kami parchment system: `#f5f4ed` parchment, `#faf9f5` ivory, ink-blue `#1B365D`, four warm text greys, registered tints `#EEF2F7`/`#E4ECF5`, Charter serif stack, one serif per page, two-weight serif, chart series order (KM §11–20, §180–184, §316–320, §420).
- hallmark exemplar papers (editorial, atmospheric dark, modern-minimal, playful OKLCH sets), display pairings by direction, rules-as-structure double rule (HM §495–499).
- taste-skill typography pairing library (40 faces with tracking/scale) and palette library (e.g. "Sheet and biro") (TS §210–251).
- ui-ux-pro-max industry palettes and shadcn HSL references, Tailwind gray/blue scales (UU §309, §336, §670+).
- huashu Chinese font map, ten Latin pairings, style-library specimen tokens (HS §124, §126, §217+).
- Texture recipes (halftone, misregistration, scanline, deckle) for print-lineage themes (HM §285–288).

## Coverage notes
- APCA covered only as Lc 60/45 equivalents; no full APCA lookup table by size/weight in sources.
- OKLCH ramp math is thin: only hue-constant ramps, chart L steps 12–15%, dark +3%/accent offsets; no gamut-mapping guidance.
- Token drift detection is described as manual audits; no tooling specs (e.g. stylelint configs).
- awesome-design-patterns contributed little beyond CSS basics; agent-skills only RN styling and font loading.
- Elevation scale for multi-level shadows (beyond "one recipe") mostly from UU stock values, which HM treats as slop.
