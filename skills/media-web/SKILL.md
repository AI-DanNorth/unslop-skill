---
name: media-web
description: Media adapter for web pages (marketing pages, docs sites, dashboards rendered in a browser). Sets web floors, capture widths and fold geometry, and adds web-only judgments (folds, page anatomy, Core Web Vitals) for Unslop runs whose medium is web.
---

# Media adapter: web

The adapter changes numbers, not rules. Lenses read the same rule cards; this adapter decides which values they use on the web and which web-only checks apply.

## Values (override `data/thresholds.yaml` via `skills/media-web/thresholds.yaml`)

| Item | Web value | Source |
|---|---|---|
| Body text floor | 16px reading text; 14px dense UI | conflict C12 |
| Label floor | 12px | huashu §66 |
| Targets | 24px Floor (WCAG 2.5.8), 44px on touch Reflex | conflict C14 |
| Widths | 320, 375, 414, 768, 1024, 1280, 1440, 1920 | conflict C40 |
| Folds | 1280×800, 1440×900, 1920×1080 | hallmark §453 |
| Words per 900px screen | strict 80/95, balanced 120/143 | hallmark §20, conflict C23 |
| LCP (lab) | warn 2.5s, fail 4.5s | conflict C41 |

## Web-only judgments for the lenses

- **Three fold questions** (hallmark §453): at 1280×800, is all hero content inside the first screen? At 1440×900, is the hero one screen? At 1920×1080, does the container hold (no stretched lines, no lonely hero)?
- **Screen-by-screen** (T-SCREEN-BY-SCREEN): scroll `shot-1440.png` in 900px steps; every screen needs a reason to exist.
- **Page anatomy** (T-ANATOMY): the primary action sits where category sites put it; the category's own sections are present.
- **Phone parity**: the 375 capture must carry the same content, reflowed rather than hidden (detector `phone_parity`).

## Not in this build

Field Core Web Vitals (only lab LCP), cookie banners and consent flows, and dark-mode parity captures. List them under "Not investigated" when they matter to the brief.
