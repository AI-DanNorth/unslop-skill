# Live test set: capture notes

Set: `evals/testset/set1-live.yaml` (39 items). Captured 8 Nov 2026 from a Windows 11 machine with normal internet access:
`run_set.py evals/testset/set1-live.yaml ../unslop-refs ../unslop-runs-live`, then `tiles.py` on every run.
Each run's fold screenshot (1440, or 1920 for the slide), the full-page tiles where in doubt, and `manifest.json` were checked by hand.
No item redirected to another host and no item hit a bot or login block.

Cookie banners got one dismissal try: `scripts/capture/consent.json` lists host and button label, and each click is recorded in `manifest.json` `consent`.

## Status

| Item | Status | Notes |
|---|---|---|
| L01–L03, L05 | ok | Builder badges ("Edit with Lovable", "Made in Bolt", "Edit with Base44") are part of the live page and visible to reviewers. |
| L04 | **not verified** | Replit placeholder "This app isn't live yet". The app is unpublished; nothing of the original design was captured. |
| L06 | ok | Cookie banner dismissed ("Reject All") at every width. |
| L07 | ok | Cookie banner dismissed ("Reject non-essential") at every width. |
| L08 | ok | Storage banner dismissed ("Essential only") at every width. |
| L09, L10 | ok | |
| L11 | **not verified** | Page opens behind a blurred "Click anywhere to enter fullscreen" interstitial, and 41 of its own font files failed to load. |
| L12–L14 | caveat | Captured fine, but the specimen pages draw impeccable's own slop labels over the design (e.g. "LOW CONTRAST TEXT", "GRADIENT TEXT"). Blind reviewers would see the answers. Close the overlay or crop it out before review. |
| L15–L21 | ok | |
| L22 | partial | The slide animates in (it has a REPLAY control). The capture caught it before the three comparison panels filled, so they show as empty frames. |
| L23 | partial | Cookie banner dismissed at 1280 and 1440. At 375 the mobile banner's button reads "Reject", not "Reject all cookies", so it stays on the 375 capture. |
| L24–L26 | ok | L25 lists 258 blocked scripts: cancelled Next.js chunk requests. The page rendered completely. |
| L27 | ok | Cookie banner dismissed ("Reject all") at every width. |
| L28 | **not verified** | The fold shows only the lime preloader ("LOAD NORRIS"). Content below was captured, but the top screen is not the page. The capture shim failed to serve the Rive `.wasm` runtime from unpkg and jsDelivr, which is the likely cause. |
| L29 | caveat | WebGL scene renders correctly, but there is no DOM text, so the text and type detectors have nothing to read. Judge it on the screenshots. |
| L30 | **not verified** | Only the intro heading and logo render. The page below is blank white: scroll-driven content never appeared. |
| L31 | ok | |
| L32 | ok | Cookie banner dismissed ("Reject analytics cookies"). GOV.UK then shows its standard "You've rejected analytics cookies" strip at the top, which is the real post-consent page. |
| L33–L36 | ok | L33 rendered the dashboard (no login wall). L36 had its dotLottie `.wasm` blocked by the capture shim, so some illustrations may not animate. |
| L37 | **not verified** | Cookie modal covers the email. The click registered, but the site asks for a second press ("Press again to continue 0/2"), and only one try is allowed. |
| L38 | **not verified** | Same cookie modal as L37, not dismissed. |
| L39 | ok | |

Totals: 27 ok, 6 not verified (L04, L11, L28, L30, L37, L38), 6 caveat or partial (L12–L14, L22, L23, L29).

## For the next capture pass

- **Capture shim on a normal network:** `netshim.mjs` rewrites unpkg and jsDelivr requests to npm packages even when the real CDN is reachable, and it can't serve `.wasm` files. That blocked Rive (L28) and dotLottie (L36). Let CDN requests through when the network allows it, or at least pass `.wasm` through.
- **L37, L38:** add a second click for reallygoodemails.com, or set its consent cookie in the context.
- **L23 at 375:** add "Reject" as a second label for anthropic.com.
- **L22, L28, L30:** these need a longer settle, or the motion capture in next step 3 (frame sequences).
