# web-interface-guidelines (vercel-labs) — real artifacts cited
Source: https://github.com/vercel-labs/web-interface-guidelines (shallow clone at /home/claude/refs/web-interface-guidelines; files: README.md, AGENTS.md, command.md, install.sh). Liveness spot-checked (WebFetch returned content) for #1, #2, #3, #13, #16.

| # | URL or repo path | Medium | Label (as presented) | Why notable | Source file:line |
|---|---|---|---|---|---|
| 1 | https://vercel.com/design/guidelines | doc | good | The repo's own rendered docs site; it's a Vercel/Geist page that should follow its own rules | install.sh:4 |
| 2 | https://www.w3.org/WAI/ARIA/apg/patterns/ | gallery | good | Reference keyboard/focus implementations for every widget (menu, dialog, tabs, combobox) | README.md:7, README.md:9, AGENTS.md:7 |
| 3 | https://nuqs.dev | web page | good | Shown as the model for "URL as state"; site has a live playground (nuqs.dev/playground) | README.md:17 |
| 4 | https://x.com/JohnPhamous/status/1657083267299028992 | component demo | good | "Prediction cones" demo for forgiving submenu hover interactions | README.md:23 |
| 5 | https://x.com/emilkowalski_/status/1962500739336462340 | component demo | good | Tooltip group timing: first tooltip delayed, later ones instant | README.md:24 |
| 6 | https://x.com/witsdev/status/2105095515817861298 | component demo | good | Desktop rubber-band overscroll suppression demo | README.md:26 |
| 7 | https://x.com/JohnPhamous/status/1831380516509278561 | component demo | good | "Northern lights" animation, cited as delight that is deliberate and justified | README.md:43 |
| 8 | https://x.com/JohnPhamous/status/1760444698857230360 | component demo | good | Optical alignment ±1px before/after demo | README.md:54 |
| 9 | https://x.com/JohnPhamous/status/1636427186566762496 | component demo | good | Right-click nav logo to show a brand-assets menu (Vercel pattern) | README.md:86 |
| 10 | https://x.com/JohnPhamous/status/1816160187839107342 | component demo | good | theme-color meta matches browser chrome to page background | README.md:139 |
| 11 | https://x.com/JohnPhamous/status/1724491202148675590 | component demo | good (fix) / slop (banding shown) | Dark-gradient banding from CSS masks compared with the background-image fix | README.md:142 |
| 12 | https://vercel.com/font | web page | good | Geist / Geist Mono font page, cited for tabular numbers | README.md:71 |
| 13 | https://react-scan.com/ | web page | neutral | Re-render profiling tool cited as a reference (product landing page) | README.md:115 |
| 14 | https://github.com/inokawa/virtua | doc | neutral | Virtualization library for large lists | README.md:120 |
| 15 | https://www.npmjs.com/package/motion | doc | neutral | JS animation library; ranked below CSS and WAAPI in the stated preference order | README.md:41 |
| 16 | https://apcacontrast.com/ | web page | good | APCA contrast calculator, preferred over WCAG 2 checking | README.md:137, AGENTS.md:153 |
| 17 | https://webaim.org/resources/contrastchecker/ | web page | neutral | WCAG 2 contrast checker, presented as the less-accurate alternative | README.md:137 |
| 18 | https://title.sh/ | web page | good | Chicago title-case tool for headings and buttons | README.md:152 |
| 19 | https://web.dev/articles/content-visibility | doc | neutral | content-visibility: auto technique reference | README.md:120 |
| 20 | https://web.dev/articles/replace-gifs-with-videos | doc | neutral | Supports "video over GIF" (animated GIF is a flagged anti-pattern) | README.md:127 |
| 21 | https://developer.apple.com/documentation/webkit/delivering-video-content-for-safari#Use-MP4-Video-Instead-of-Animated-GIFs | doc | neutral | Safari MP4-in-<picture> technique | README.md:128 |
| 22 | https://developer.chrome.com/blog/full-accessibility-tree | doc | neutral | How to verify accessible names in the DevTools a11y tree | README.md:81 |
| 23 | https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html | doc | neutral | Gesture alternative requirement | README.md:32 |
| 24 | https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html | doc | neutral | Autoplay over 5 s needs pause/stop/hide controls | README.md:46 |
| 25 | https://www.w3.org/WAI/media/av/ | doc | neutral | Captions and transcripts for media | README.md:85 |
| 26 | https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior (+ @media/pointer, inert, env(), Web Workers MDN pages) | doc | neutral | MDN references for cited CSS/HTML features | README.md:26, 31, 58, 126 |
| 27 | https://support.apple.com/guide/mac-help/change-appearance-settings-mchlp1225/mac | doc | neutral | macOS "Show scroll bars: Always", used to test for stray scrollbars | README.md:59 |
| 28 | https://react.dev/learn/react-developer-tools | doc | neutral | Re-render tracking tool | README.md:115 |
| 29 | https://destroytoday.com/ | web page | neutral | Personal site of a credited reviewer (Jonnie Hallman), likely a well-crafted designer site | README.md:198 |
| 30 | https://pa.co | web page | neutral | Personal site of a credited reviewer (Paco Coursey) | README.md:198 |
| 31 | https://joebell.studio/ | web page | neutral | Personal site of a credited reviewer (Joe Bell) | README.md:198 |
| 32 | https://vercel.com/careers?function=Design | web page | neutral | Vercel product page, the publisher's own live UI | README.md:194 |
| 33 | command.md (Anti-patterns list) | doc | slop | 14 code-level anti-patterns to flag (zoom disabled, transition: all, outline-none, div onClick, unlabeled icon buttons, GIFs, etc.); no concrete bad artifacts | command.md:152-167 |
| 34 | command.md (Output Format sample: src/Button.tsx, src/Modal.tsx, src/Card.tsx) | doc | slop | Hypothetical audit-output sample (an output schema to calibrate against, not real files) | command.md:169-191 |
| 35 | AGENTS.md | doc | good | MUST/SHOULD/NEVER condensed rule set for agents | AGENTS.md:1 |

## Best audit candidates
1. https://vercel.com/design/guidelines: the guideline publisher's own page; test whether Unslop passes a page built to these rules (a likely true negative).
2. https://www.w3.org/WAI/ARIA/apg/patterns/ (individual pattern example pages): reference-correct keyboard/focus/ARIA widgets, an a11y "gold" baseline.
3. https://nuqs.dev (+ /playground): developer landing page with a live demo; checks URL-state and deep linking.
4. https://vercel.com/font: Geist type specimen page; tests typography, tabular numbers and dark theme with color-scheme.
5. https://react-scan.com/: dev-tool marketing landing page, a likely mid-ground case for slop patterns (gradients, hero clichés).
6. https://apcacontrast.com/: tool UI with dense controls; tests forms, labels and contrast.
7. https://destroytoday.com/: hand-crafted designer personal site, a non-template control.
8. https://pa.co: minimalist designer personal site, a non-template control.
9. https://joebell.studio/: designer studio site, a non-template control.
10. https://x.com/JohnPhamous/status/1724491202148675590: before/after for gradient banding, the only cited visual that shows a bad state next to the fix.

## Notes
- The repo has no example artifacts (HTML, screenshots, demo pages): only 3 markdown rule files and an installer.
- No real site is named as a bad example. "Slop" here exists only as rule-level anti-patterns (command.md:152) and a hypothetical audit-output sample.
- The x.com demos are short videos or GIFs inside tweets. Medium is labelled "component demo", but the tweets need login and are hard to audit automatically.
- Liveness was confirmed for #1, #2, #3, #13 and #16 (apcacontrast came back as an archived capture). The rest were not checked.
- The Vercel copywriting rules (README.md:144-172) are brand-specific, so do not treat their absence as slop.
