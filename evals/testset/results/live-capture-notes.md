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

## Capture gaps found during blind review (live round 1)

The fold check missed these; the reviewers found them further down the pages. Each reviewer marked them not verified rather than judging them. They go to the round-1 adjudication.

- **Scroll-reveal sections never painted** (blank bands in the full-page tiles): L10 and L20 (judged from DOM text), L18 tiles 03–07, L28 pinned and WebGL sections, L36 scroll-linked sections, L16 "Reach them / Send follow-up" section (invisible but focusable). Same cause as L30: `settle()` scrolls with instant `scrollTo`, which doesn't trigger these animations. This is a system-level capture limitation; `scrollFrames` (L30) is a per-host workaround, not a fix.
- **L29:** the site's own `App3D-*.js` request failed (`manifest.network.blocked`), so only the intro planet rendered. Downgraded from caveat to partial.
- **L21:** lazy-loaded gallery thumbnails never rendered, and the demo video was blocked.
- **L26:** some scripts and two fonts were blocked; several images show as broken.
- **L36:** the reviewer reported a cookie banner covering focus stops. Unconfirmed: no banner text appears in `dom-1440.json`, so it may be in an iframe or at another width.
- **`extract.js`:** a reviewer saw empty heading text for headings that wrap their text in child elements (L05, L10, L25). Not yet checked; it would affect the heading detectors.
