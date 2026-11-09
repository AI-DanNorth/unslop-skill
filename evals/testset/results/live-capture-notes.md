# Live test set: capture notes

Set: `evals/testset/set1-live.yaml` (39 items). Final capture 9 Nov 2026 (UTC), from a Windows 11 machine with normal internet access:
`run_set.py evals/testset/set1-live.yaml ../unslop-refs ../unslop-runs-live --only L01,...,L39`, then `tiles.py` on every run.
I checked each run's fold screenshot (1440px, or 1920px for the slide), the tiles where in doubt, and `manifest.json` by hand.
No item redirected to another host, and none hit a bot check or login wall.

## How the capture was made

- **Network mode `direct`** (`manifest.network.mode`). `netshim.mjs` now checks whether Google Fonts and jsDelivr are reachable and turns itself off if they are, so pages load their real fonts, CDN scripts and `.wasm` runtimes. The first pass (8 Nov) used the shim, which blocked Rive on L28 and dotLottie on L36. Set `UNSLOP_NET=shim` to force the old behaviour in a sandbox.
- **Page prep per host** (`scripts/capture/page-prep.json`). Each rule is listed below and recorded in `manifest.prep.applied`. Cookie banners get their reject or essential-only button wherever one exists.

| Host | Prep | Items |
|---|---|---|
| consile.app, cineyx.ai, gradloom.app, stripe.com | one click on the reject or essential-only button | L06, L07, L08, L27 |
| anthropic.com | "Reject all cookies", or "Reject" on the mobile banner | L23 |
| design-system.service.gov.uk | "Reject analytics cookies", then "Hide cookie message" | L32 |
| reallygoodemails.com | "Allow all cookies" (the only dismiss button; up to 2 presses, 1 was enough) | L37, L38 |
| impeccable.style | block `/js/detect-antipatterns-browser.js`, which draws the tool's own slop labels over the specimen; the homepage (L19) doesn't load it | L12–L14 |
| gameghost.manus.space | click the "Click anywhere to enter fullscreen" splash, then "Use essential only" | L11 |
| skill-huasheng.vercel.app | wait 8 s for the slide to finish building | L22 |
| brand.dropbox.com | scroll-driven page: 12 wheel-scroll viewport frames max (3 used); `tiles.py` uses these frames as the tiles | L30 |

## Status

| Item | Status | Notes |
|---|---|---|
| L01–L03, L05 | ok | The builder badges ("Edit with Lovable", "Made in Bolt", "Edit with Base44") are part of the live page, so reviewers will see them. |
| L04 | **not verified** | Replit placeholder "This app isn't live yet". The app is unpublished, so the design no longer exists to capture. |
| L06–L08 | ok | Banner dismissed at every width. |
| L09 | ok | |
| L10 | ok | The headline is a typewriter animation, so it can show part-typed ("The platform to…"). That's how the site behaves. |
| L11 | caveat | Splash and privacy banner dismissed. 41 of the site's own font files fail even on a direct network: they 307-redirect to signed CloudFront URLs. The type you see is a fallback, so treat font findings as not verified. |
| L12–L14 | ok | Overlay script blocked; the specimens render without labels. |
| L15–L21 | ok | |
| L22 | ok | Captured after the build animation. All three comparison panels are filled. |
| L23 | ok | Banner dismissed at every width. |
| L24–L27 | ok | L25's 258 "blocked" scripts are cancelled Next.js chunk prefetches; the page renders completely. |
| L28 | ok | Renders properly now that the Rive runtime loads, instead of the stuck preloader from the first pass. |
| L29 | caveat | The WebGL scene renders correctly, but the page has no DOM text, so the text and type detectors have nothing to read. Judge it on the screenshots. |
| L30 | caveat | Scroll-driven page. The tiles are wheel-scroll viewport frames, which show what a visitor sees. The full-page `shot-*.png` and `bg-*.png` show only the intro, so the pixel-contrast detectors aren't reliable here. |
| L31–L36 | ok | L33 rendered the dashboard (no login wall). L36's dotLottie illustrations now load. |
| L37, L38 | ok | Cookie modal dismissed at every width; the email is unobstructed. |
| L39 | ok | |

Totals: 35 ok, 1 not verified (L04), 3 with a caveat (L11, L29, L30).

## Capture gaps found during blind review (live round 1), and what was done

The fold check missed these. The reviewers found them further down the pages and marked them not verified instead of judging them. All 39 items were then recaptured (9 Nov 2026) with the fixes below. Round-1 lens files stay archived in `results/live-round-1/`.

| Gap | Items | Fix |
|---|---|---|
| Scroll-reveal sections never painted: instant `scrollTo` doesn't trigger reveal-on-scroll observers or smooth-scroll libraries | L10, L16, L18, L20, L28, L36 | `settle()` now also does a real mouse-wheel pass (30 s budget) before screenshots and in the hidden-content scroll test. L10 and L16 now render fully, and L18 has 1 blank tile left (its drag-to-compare strip). |
| Scroll-position-driven sections (pinned or scrubbed): no full-page shot can show them | L20, L28, L36 (and L30 before) | `scrollFrames: 12` in `page-prep.json`. The tiles are now viewport frames taken while wheel-scrolling, all with content. |
| L36 cookie banner (IBM, no reject option; not in the page text) | L36 | Confirmed in the scroll frames. Added "Accept All" for carbondesignsystem.com, and it was dismissed at every width. |
| Headings whose words sit in child spans recorded empty; `<br>` glued words together ("Intakeand integrations") | L05, L10, L25 | `extract.js` now treats `<br>` as a space, and `h1_words` reads the whole heading (`blockText`). The L25 reviewer's run-together accessible-name finding was a capture artifact. |
| L29's own `App3D-*.js` request failed | L29 | Not fixable from capture; status changed from caveat to partial. |
| L21 lazy gallery thumbnails, blocked demo video; L26 some blocked scripts and fonts | L21, L26 | Partly covered by the wheel pass (lazy images). Leftovers are recorded in each manifest. |

`run_set.py` per-item timeout raised from 600 to 900 s: L28 takes about 540 s with the wheel pass.
