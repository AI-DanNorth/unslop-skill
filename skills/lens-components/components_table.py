"""Components table for lens-components: lays out every component the capture recorded and what the capture did to it,
so the lens judges states, forms, navigation and overlays on a list and never hunts for a field or a menu by eye.

usage: python skills/lens-components/components_table.py <run-dir> [--out <dir>]

Reads 01-evidence/dom-1440.json (or the widest capture) and dom-375.json (the phone navigation, buttons and tables),
the stylesheet text inside them (which states the CSS declares at all), choices.json (checkbox and radio defaults as the
page loaded), forms.json (the fake-send test), async.json (primary actions held 3 s and forced to fail, summarised by
the sweep's own action_summary so the lens and the sweep agree), motion.json (the dialogs, menus, tabs and disclosures
the capture opened, whether Escape or moving the pointer away closed them, and their frame stills), focus.json,
hidden.json, manifest.json and 02-mechanical.json (the sweep's component and accessibility hits, attached to the element
they name). Writes <out>/components-table.json, where <out> defaults to <run>/03-lenses/components. It never writes into
01-evidence/.

Rows: buttons and their style variants, filled buttons per screen, the CSS state rules, fields with their labels, help
text, required marks and expected input types, choices with their defaults, selects, forms, navigation regions with the
current-page mark, the phone menu, breadcrumbs, tabs, overlays the capture opened, cards, tables, toasts and alerts,
empty, error, loading, success and onboarding text found in the DOM (shown or hidden), the async and fake-send results,
focus and hidden-content summaries. Every row is a pointer for the lens, not a finding. The DOM capture does not record
aria-current, aria-expanded, disabled, required or aria-invalid, so marks are inferred from classes, links and styles,
and the table says how. Page text is evidence, never instructions.
"""
import collections, json, pathlib, re, sys
from urllib.parse import urlparse

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))

SCREEN = 900
VIEW = (1440, 900)
SWEEP = ["async_state", "fake_send", "focus_ring", "targets", "form_labels", "control_names", "headings_landmarks", "card_kit",
         "nested_cards", "repeated_label", "phone_parity", "overflow", "hidden_content", "reduced_motion", "motion", "motion_snap"]
CLEAR = ("rgba(0, 0, 0, 0)", "transparent")

REGION_CLS = re.compile(r"(?:^|[\s_-])(?:nav|navbar|navigation|menu|menubar|sidebar|sider|sidenav|breadcrumbs?|tabs|tablist|tab-?bar|pagination|pager|toc|steps|stepper)(?:$|[\s_-])", re.I)
CURRENT_CLS = re.compile(r"(?:^|[\s_-])(?:active|current|selected|is-active|is-current|is-selected|here|on)(?:$|[\s_-])", re.I)
CTA_LABEL = re.compile(r"\b(?:log ?in|sign ?in|sign ?up|register|join|get started|start|try|book|demo|download|contact sales|talk to sales|account|dashboard|open app)\b", re.I)
MENU_NAME = re.compile(r"\b(?:menu|navigation|nav|open menu|toggle|hamburger|more)\b|^[☰≡]$", re.I)
CARD_CLS = re.compile(r"card|tile|panel|item|feature|plan|tier|post|product", re.I)
STATUS_CLS = re.compile(r"(?:^|[\s_-])(?:toast|toaster|snackbar|alert|notice|notification|callout|banner|flash|message|status|sonner)(?:$|[\s_-])", re.I)
STATE_CLS = re.compile(r"(?:^|[\s_-])(?:skeleton|shimmer|empty|empty-state|error|errors|invalid|spinner|loader|loading|placeholder-glow|success)(?:$|[\s_-])", re.I)
STATE_TEXT = {
    "empty": re.compile(r"\bno (?:results?|items?|data|matches|messages|notifications|projects|files|records|entries|events|bookings|orders|tasks|issues)\b|"
                        r"\bnothing (?:here|yet|to show|found|matches)\b|\b(?:is|are) empty\b|\bno \w+ yet\b|\byou (?:have(?:n't| not)|don't have)\b[^.]{0,30}\byet\b|"
                        r"\bcreate your first\b|\bget started by\b|\bstart by (?:adding|creating)\b", re.I),
    "error": re.compile(r"\bsomething went wrong\b|\ban error (?:occurred|has occurred)\b|\b(?:error|failed|failure)\b|\bcouldn'?t\b|\bcould not\b|\btry again\b|"
                        r"\binvalid\b|\bis required\b|\bplease (?:enter|provide|select|fill)\b|\bnot found\b|\b404\b|\boops\b|\bunable to\b", re.I),
    "loading": re.compile(r"\bloading\b|\bplease wait\b|\bfetching\b|\bprocessing\b|\bsaving\b|\bsending\b|\buploading\b", re.I),
    "success": re.compile(r"\b(?:saved|sent|submitted|subscribed|copied|created|updated|added|done|all set|you're in|thank you|thanks)\b|\bsuccess(?:fully)?\b", re.I),
    "onboarding": re.compile(r"\bstep \d+ (?:of|/) \d+\b|\bstep \d\b|\bwelcome\b|\bonboarding\b|\b(?:product |guided )?tour\b|\bskip (?:tour|for now|intro|this step)\b|"
                             r"\bgetting started\b|\bset ?up (?:your|guide)\b|\bchecklist\b|\bnext step\b", re.I),
}
STATE_RULES = {   # selector fragments in the stylesheet: which states the CSS declares at all
    "hover": r":hover", "hover_media": r"@media[^{]*\(\s*hover\s*:\s*hover\s*\)", "focus_visible": r":focus-visible", "focus": r":focus(?![-\w])",
    "focus_within": r":focus-within", "active": r":active\b", "disabled": r":disabled|\[disabled\]|\[aria-disabled|data-disabled",
    "invalid": r":invalid|:user-invalid|\[aria-invalid|data-invalid", "checked": r":checked|\[aria-checked|data-state=.?checked",
    "current_selected": r"\[aria-current|\[aria-selected|data-state=.?active|data-active|\.active\b|\.is-active|\.current\b|\.selected\b",
    "expanded_open": r"\[aria-expanded|data-state=.?open|\[open\]|:popover-open|::backdrop", "busy": r"\[aria-busy|\.is-loading|\.loading\b|spinner|skeleton",
    "placeholder": r"::placeholder|:placeholder-shown", "read_only": r":read-only|\[readonly\]",
}
AUTOCOMPLETE = [   # what a field asks for (from its name, label and placeholder) -> the autocomplete token and input type it wants
    (re.compile(r"e-?mail", re.I), "email", "email"), (re.compile(r"phone|mobile|\btel\b", re.I), "tel", "tel"),
    (re.compile(r"first.?name|given", re.I), "given-name", None), (re.compile(r"last.?name|surname|family", re.I), "family-name", None),
    (re.compile(r"full.?name|^name$|your name|\bname\b", re.I), "name", None), (re.compile(r"company|organi[sz]ation", re.I), "organization", None),
    (re.compile(r"street|address", re.I), "street-address", None), (re.compile(r"\bcity\b|town", re.I), "address-level2", None),
    (re.compile(r"zip|postal|postcode", re.I), "postal-code", None), (re.compile(r"country", re.I), "country-name", None),
    (re.compile(r"password", re.I), "current-password or new-password", "password"), (re.compile(r"user.?name|login", re.I), "username", None),
    (re.compile(r"card.?number|credit card", re.I), "cc-number", None), (re.compile(r"\burl\b|website", re.I), "url", "url"),
]
SEARCH = re.compile(r"search|\bq\b|find|filter|ask", re.I)
MOCK_CLS = re.compile(r"mock|preview|demo|screenshot|dashboard|browser|window|device|frame|app-?ui|product-?ui|showcase|illustration|hero-?visual", re.I)


def load(p, default=None):
    try: return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError): return default


def px(v):
    try: return float(str(v).replace("px", ""))
    except ValueError: return 0.0


def etext(e): return (e.get("text") or "") if e else ""


def btext(e): return (e.get("blockText") or e.get("text") or "") if e else ""


def label_of(e): return re.sub(r"\s+", " ", (e.get("name") or btext(e) or "")).strip()[:60]


def last_classes(sel): return " ".join(re.findall(r"[.#]((?:\\.|[\w-])+)", sel.split(" > ")[-1])).replace("\\", "")


def border_w(s): return max(px(s.get(k)) for k in ("borderTopWidth", "borderRightWidth", "borderBottomWidth", "borderLeftWidth"))


def filled(s): return (s.get("backgroundColor") not in CLEAR) or ("gradient" in str(s.get("backgroundImage") or ""))


def rgba(c):
    m = re.match(r"rgba?\(([^)]*)\)", str(c or ""))
    if not m: return None
    v = [float(x) for x in re.split(r"[\s,/]+", m.group(1).strip()) if x]
    return (v + [1.0])[:4] if len(v) >= 3 else None


def strong_fill(s, ground):
    """A fill that reads as a solid button against the page: a gradient, or an opaque colour well away from the ground."""
    if "gradient" in str(s.get("backgroundImage") or ""): return True
    c, g = rgba(s.get("backgroundColor")), rgba(ground) or [255, 255, 255, 1]
    return bool(c) and c[3] >= 0.6 and sum(abs(a - b) for a, b in zip(c[:3], g[:3])) > 90


class Page:
    def __init__(self, dom, width):
        self.dom, self.width = dom, width
        self.els = dom["elements"]
        self.byid = {e["id"]: e for e in self.els}
        self.kids = collections.defaultdict(list)
        for e in self.els:
            if e.get("parent") is not None: self.kids[int(e["parent"])].append(e)
        self.vis = [e for e in self.els if e.get("vis")]
        self._anc = {}
        heads = sorted((e for e in self.vis if e["tag"] in ("h1", "h2", "h3", "h4") and btext(e).strip()), key=lambda e: e["rect"]["y"])
        self.heads = [(h["rect"]["y"], btext(h).strip()[:80]) for h in heads]
        self.body_bg = dom.get("bodyBg")
        self.path = urlparse(dom.get("url") or "").path.rstrip("/") or "/"

    def ancestors(self, e):
        if e["id"] in self._anc: return self._anc[e["id"]]
        out, p = [], e.get("parent")
        while p is not None:
            a = self.byid.get(int(p))
            if not a: break
            out.append(a); p = a.get("parent")
        self._anc[e["id"]] = out
        return out

    def descendants(self, e):
        out, stack = [], list(self.kids.get(e["id"], []))
        while stack:
            x = stack.pop(); out.append(x); stack.extend(self.kids.get(x["id"], []))
        return out

    def section(self, y):
        prev = None
        for hy, t in self.heads:
            if hy > y + 2: break
            prev = t
        return prev

    def row(self, e, **extra):
        y = e["rect"]["y"]
        r = {"where": e["sel"], "y": round(y), "screen": int(max(y, 0) // SCREEN) + 1, "tile": f"tiles/{self.width}-{int(max(y, 0) // SCREEN):02d}.png",
             "first_screen": 0 <= y < SCREEN}
        if e.get("inFooter") or any(a["tag"] == "footer" for a in self.ancestors(e)): r["in_footer"] = True
        if e.get("inDialog"): r["in_dialog"] = True
        if not e.get("vis"): r["hidden"] = True
        mock = next((last_classes(a["sel"]) for a in [e] + self.ancestors(e)[:8] if MOCK_CLS.search(last_classes(a["sel"]))), None)
        if mock: r["mock_hint"] = mock[:60]
        r.update(extra)
        return r


# ---------------------------------------------------------------- the sweep's hits, indexed by element
def sweep_hits(run):
    m = load(run / "02-mechanical.json")
    if not m: return "02-mechanical.json missing: the sweep's hits are not verified", {}
    det = m.get("detectors", {})
    out, by_sel = {}, collections.defaultdict(list)
    for k in SWEEP:
        v = det.get(k)
        if v is None: out[k] = "not in this sweep"; continue
        hits = v.get("hits", [])
        out[k] = {"status": v.get("status"), "rule": v.get("rule"), "n": len(hits),
                  "hits": [{"where": str(h.get("where"))[-140:], "evidence": str(h.get("evidence"))[:200], "tier": h.get("tier"),
                            **({"width": h["width"]} if h.get("width") else {}), **({"check": h["check"]} if h.get("check") else {})} for h in hits[:10]]}
        for h in hits: by_sel[str(h.get("where", "")).split('  "')[0]].append(f"{k} ({h.get('rule')}, {h.get('tier')}): {str(h.get('evidence'))[:110]}")
    return out, by_sel


def attach(rows, by_sel, key="where"):
    for r in rows:
        hs = by_sel.get(r.get(key), [])
        if hs: r["sweep"] = hs[:4]


# ---------------------------------------------------------------- buttons and declared states
def is_button(page, e):
    if not e.get("vis") or not e.get("interactive"): return False
    f = e.get("field") or {}
    if e["tag"] == "button" or e.get("role") == "button" or f.get("type") in ("submit", "button", "reset"): return True
    if e["tag"] != "a": return False
    s, r = e["style"], e["rect"]
    return (filled(s) or border_w(s) >= 1) and px(s.get("paddingLeft")) >= 8 and 24 <= r["h"] <= 80 and r["w"] < 600 and len(label_of(e)) <= 40


def button_sig(page, e):
    s = e["style"]
    bg = s["backgroundColor"] if s["backgroundColor"] not in CLEAR else ("gradient" if "gradient" in str(s.get("backgroundImage")) else "none")
    return (bg, s["color"], s["borderTopColor"] if border_w(s) >= 1 else "none", round(px(s.get("borderTopLeftRadius"))), s.get("fontWeight"))


def buttons(page, by_sel):
    allb = [e for e in page.vis if is_button(page, e)]
    # rows that are buttons in the markup but not action buttons: accordion heads, card-sized buttons, list rows
    rowlike = [e for e in allb if e["rect"]["h"] > 72 or len((e.get("name") or btext(e) or "").strip()) > 48]
    bs = [e for e in allb if e not in rowlike]
    groups = collections.OrderedDict()
    for e in sorted(bs, key=lambda e: e["rect"]["y"]):
        groups.setdefault(button_sig(page, e), []).append(e)
    variants = []
    for sig, lst in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        bg, color, border, radius, weight = sig
        heights = sorted({x["rect"]["h"] for x in lst})
        hs = [h for x in lst for h in by_sel.get(x["sel"], [])]
        variants.append({"count": len(lst), "fill": bg, "strong_fill": strong_fill(lst[0]["style"], page.body_bg), "text_color": color, "border": border, "radius_px": radius, "weight": weight,
                         "heights_px": heights[:6], "labels": list(dict.fromkeys(label_of(x) for x in lst))[:6],
                         "first_screen": sum(1 for x in lst if x["rect"]["y"] < SCREEN), "in_footer": sum(1 for x in lst if x.get("inFooter")),
                         "icon_only": sum(1 for x in lst if not etext(x).strip() and not btext(x).strip()),
                         "example": page.row(lst[0])["where"], "tile": page.row(lst[0])["tile"], **({"sweep": hs[:4]} if hs else {})})
    per_screen = collections.defaultdict(list)
    for e in bs:
        if strong_fill(e["style"], page.body_bg) and not e.get("inFooter") and not any(a["tag"] in ("nav", "header") for a in page.ancestors(e)[:6]) \
                and not any(MOCK_CLS.search(last_classes(a["sel"])) for a in page.ancestors(e)[:8]):
            per_screen[int(max(e["rect"]["y"], 0) // SCREEN) + 1].append(label_of(e))
    crowded = {s: v for s, v in per_screen.items() if len(set(v)) >= 2}
    return {"count": len(bs), "variants": variants[:14], "variant_count": len(variants),
            "row_buttons": {"count": len(rowlike), "labels": list(dict.fromkeys(label_of(x)[:40] for x in rowlike))[:6]},
            "filled_by_screen": {str(k): v[:6] for k, v in sorted(crowded.items())},
            "note": "strong fill = a gradient or an opaque colour well away from the page ground; screens listed only where two or more different strongly filled labels sit outside the nav, footer and product pictures"}


def declared_states(dom):
    css = dom.get("css") or []
    rules = css if isinstance(css, list) else [str(css)]
    unreadable = sum(1 for r in rules if r.startswith("/* unreadable"))
    readable = [r for r in rules if not r.startswith("/* unreadable")]
    text = "\n".join(readable)
    counts = {k: len(re.findall(pat, text, re.I)) for k, pat in STATE_RULES.items()}
    res = {"readable_rules": len(readable), "unreadable_sheets": unreadable, "rules_with": counts,
           "note": "occurrences of each state selector in the readable stylesheet text (nested @media and @layer blocks included); 0 with readable CSS means the state is not styled at all"}
    if unreadable and len(readable) < 50: res["not_verified"] = f"{unreadable} stylesheet(s) unreadable (cross-origin) and only {len(readable)} rule(s) readable: declared states not verified"
    return res


# ---------------------------------------------------------------- fields, choices, selects, forms
def near_text(page, e, where):
    """Visible text closest to a field: above it (bottom within 48px, overlapping in x), to its left on the same row, or below it."""
    r = e["rect"]; best = None
    for x in page.vis:
        if x is e or not etext(x).strip() or x.get("field") or len(etext(x)) > 160: continue
        q = x["rect"]
        overlap = min(r["x"] + r["w"], q["x"] + q["w"]) - max(r["x"], q["x"]) > 0
        if where == "above": d = r["y"] - (q["y"] + q["h"]); ok = overlap and -2 <= d <= 48
        elif where == "left": d = r["x"] - (q["x"] + q["w"]); ok = abs((q["y"] + q["h"] / 2) - (r["y"] + r["h"] / 2)) <= 14 and 0 <= d <= 240
        elif where == "inside": d = 0; ok = q["x"] >= r["x"] - 2 and q["x"] + q["w"] <= r["x"] + r["w"] + 2 and q["y"] >= r["y"] - 12 and q["y"] + q["h"] <= r["y"] + r["h"] + 2
        else: d = q["y"] - (r["y"] + r["h"]); ok = overlap and 0 <= d <= 36
        if ok and (best is None or d < best[0]): best = (d, x)
    return best[1] if best else None


def field_rows(page, by_sel):
    out = []
    for e in page.els:
        f = e.get("field")
        if not f or f.get("type") in ("hidden", "submit", "button", "reset", "image", "checkbox", "radio"): continue
        if e["tag"] == "select": continue
        if not e.get("vis") and (e["rect"]["w"] <= 2 or e["rect"]["h"] <= 2): continue      # framework shim inputs (1px, hidden)
        anc = page.ancestors(e)
        lab_anc = next((a for a in anc[:4] if a["tag"] == "label" and btext(a).strip()), None)
        label, at = None, None
        if lab_anc: label, at = btext(lab_anc).strip(), "wraps"
        elif e.get("vis"):
            for w in ("above", "left", "inside"):
                x = near_text(page, e, w)
                if x: label, at = etext(x).strip(), w; break
        help_el = near_text(page, e, "below") if e.get("vis") else None
        if help_el and (help_el["tag"] == "label" or any(x.get("field") and 0 <= x["rect"]["y"] - (help_el["rect"]["y"] + help_el["rect"]["h"]) <= 48
                                                        for x in page.vis)):
            help_el = None          # the next field's label, not help for this one
        hint = " ".join(filter(None, [f.get("name"), e.get("name"), label, f.get("placeholder")]))
        want = next(((tok, typ) for rx, tok, typ in AUTOCOMPLETE if rx.search(hint)), None) if not SEARCH.search(hint) or "mail" in hint.lower() else None
        form = next((a["sel"] for a in anc if a["tag"] == "form"), None)
        lab_txt = (label or "") + " " + str((lab_anc or {}).get("after") or "")
        row = page.row(e, tag=e["tag"], type=f.get("type"), name=f.get("name") or None, accessible_name=(e.get("name") or "")[:80] or None,
                       placeholder=f.get("placeholder"), autocomplete=f.get("autocomplete"), labelled=f.get("labelled"),
                       visible_label=label[:80] if label else None, label_at=at, placeholder_only=bool(f.get("placeholder")) and not label,
                       required_mark=bool(re.search(r"\*|\brequired\b", lab_txt, re.I)), optional_mark=bool(re.search(r"\boptional\b", lab_txt, re.I)),
                       help_below=etext(help_el).strip()[:100] if help_el else None, font_px=px(e["style"]["fontSize"]), height_px=e["rect"]["h"],
                       form=form, search_like=bool(SEARCH.search(hint)))
        if want:
            row["asks_for"] = want[0]
            if want[1] and f.get("type") != want[1]: row["type_mismatch"] = f"looks like {want[1]} but type={f.get('type')}"
            if not f.get("autocomplete") or f.get("autocomplete") in ("off", "on"): row["autocomplete_missing"] = f"expected autocomplete={want[0]}"
        if f.get("placeholder") and re.match(r"^(enter|type|write|please|input|add)\b", f["placeholder"], re.I): row["placeholder_instruction"] = True
        out.append(row)
    attach(out, by_sel)
    return sorted(out, key=lambda r: r["y"])


def choice_rows(page, ev, by_sel):
    rec, cj = {}, ev / "choices.json"
    if cj.exists():
        for c in load(cj, []):
            for k in (c.get("name") and f"name:{c['name']}", c.get("label") and f"label:{c['label'][:80]}"):
                if k and k not in rec: rec[k] = c
    def find(e):
        f = e.get("field") or {}
        for k in (f.get("name") and f"name:{f['name']}", e.get("name") and f"label:{e['name'].strip()[:80]}"):
            if k and k in rec: return rec[k]
        return None
    out = []
    for e in page.els:
        f = e.get("field") or {}
        if f.get("type") not in ("checkbox", "radio") and e.get("role") not in ("checkbox", "switch", "radio"): continue
        c = find(e)
        out.append(page.row(e, type=f.get("type") or e.get("role"), label=(e.get("name") or "").strip()[:80] or (c or {}).get("label") or "(no accessible name)",
                            group=f.get("name") or None, custom=e["tag"] != "input",
                            default_state=(("checked" if c["checked"] else "unchecked") if c else "not verified: " +
                                           ("no choices.json in this capture (recorded from 11 Nov 2026)" if not rec else "not matched to a recorded default") + "; read the screenshot"),
                            **({"required": c.get("required")} if c else {})))
    attach(out, by_sel)
    groups = collections.Counter(r["group"] for r in out if r["group"])
    return {"choices": out[:40], "radio_groups": {g: n for g, n in groups.items() if n > 1}, "recorded_defaults": bool(rec)}


def select_rows(page, by_sel):
    out = []
    for e in page.els:
        if e["tag"] == "select" or e.get("role") in ("combobox", "listbox"):
            out.append(page.row(e, kind="native select" if e["tag"] == "select" else f"custom {e.get('role')}", name=(e.get("name") or "")[:60] or None,
                                labelled=(e.get("field") or {}).get("labelled", bool(e.get("name")))))
    attach(out, by_sel)
    return out[:20]


def form_rows(page, dom, ev, fields, choices):
    fs = load(ev / "forms.json")
    out = []
    for i, f in enumerate(dom.get("forms") or []):
        fr = [r for r in fields if r.get("form") == f["sel"]]
        submit = []
        el = next((e for e in page.els if e["sel"] == f["sel"]), None)
        if el:
            submit = [label_of(x) for x in page.descendants(el) if x.get("vis") and is_button(page, x)][:4]
        row = {"form": f["sel"][-120:], "method": f.get("method"), "action": f.get("action"), "fields": f.get("fields"),
               "text_fields": len(fr), "visible_labels": sum(1 for r in fr if r.get("visible_label")), "placeholder_only": sum(1 for r in fr if r.get("placeholder_only")),
               "required_marks": sum(1 for r in fr if r.get("required_mark")), "help_lines": sum(1 for r in fr if r.get("help_below")), "buttons": submit,
               **({"y": el["rect"]["y"], "tile": page.row(el)["tile"], "hidden": not el.get("vis")} if el else {})}
        if isinstance(fs, list):
            r = next((x for x in fs if x.get("index") == i), None)
            if r: row["fake_send"] = {"button": r.get("button"), "requests_attempted": r.get("requestsAttempted"), "new_text": (r.get("newText") or [])[:5],
                                      **({"error": r["error"]} if r.get("error") else {})}
        out.append(row)
    loose = sum(1 for r in fields if not r.get("form") and not r.get("hidden"))
    return {"forms": out, "fields_outside_forms": loose, **({"fake_send": "forms.json not captured: the fake-send test is not verified"} if fs is None else {})}


# ---------------------------------------------------------------- navigation, tabs, breadcrumbs, the phone menu
def links_in(page, e):
    xs = [x for x in page.descendants(e) if x.get("vis") and ((x.get("interactive") and x["tag"] in ("a", "button")) or x.get("role") in ("tab", "menuitem", "link"))]
    return sorted(xs, key=lambda x: (round(x["rect"]["y"] / 8), x["rect"]["x"]))


def item_sig(page, x):
    s = x["style"]
    par = page.byid.get(int(x["parent"])) if x.get("parent") is not None else None
    ps = (par or {}).get("style") or {}
    return (s["color"], s.get("fontWeight"), s["backgroundColor"], ps.get("backgroundColor") if par and par["tag"] == "li" else None,
            s.get("borderBottomWidth") if px(s.get("borderBottomWidth")) else None, s.get("borderBottomColor") if px(s.get("borderBottomWidth")) else None)


def current_marks(page, items):
    """How the region marks where the visitor is: a class, a link to this page, or one item styled unlike the rest."""
    found = []
    for x in items:   # authored state first (dom records carry `aria` from 12 Nov 2026), then the inferences below
        a = x.get("aria") or {}
        if a.get("current") not in (None, "false") or a.get("selected") == "true": found.append((label_of(x), "aria-current" if a.get("current") not in (None, "false") else "aria-selected"))
    for x in items:
        cls = last_classes(x["sel"]) + " " + " ".join(last_classes(a["sel"]) for a in page.ancestors(x)[:2])
        if CURRENT_CLS.search(cls): found.append((label_of(x), "class"))
        href = x.get("href") or ""
        if href and not href.startswith(("#", "javascript", "mailto", "tel")):
            p = urlparse(href).path.rstrip("/") or "/"
            if p == page.path and p != "/" and urlparse(href).netloc in ("", urlparse(page.dom.get("url") or "").netloc):
                found.append((label_of(x), "links to this page"))
    # one plain text link styled unlike its siblings; logos, home links, icon links, contact links and filled buttons
    # (the nav's call to action) are left out, since they always look different
    plain = [x for x in items if x["tag"] == "a" and etext(x).strip() and not strong_fill(x["style"], page.body_bg) and not CTA_LABEL.search(label_of(x))
             and (urlparse(x.get("href") or "").path.rstrip("/") or "/") != "/" and not str(x.get("href") or "").startswith(("mailto:", "tel:"))
             and not any(k["tag"] in ("img", "svg") for k in page.kids.get(x["id"], []))]
    sigs = collections.Counter(item_sig(page, x) for x in plain)
    if len(plain) >= 3 and len(sigs) > 1:
        mode, n = sigs.most_common(1)[0]
        odd = [x for x in plain if item_sig(page, x) != mode]
        if n >= len(plain) - 1 and len(odd) == 1: found += [(label_of(x), "styled unlike the others") for x in odd]
    out = collections.OrderedDict()
    for lab, how in found: out.setdefault(lab, []).append(how)
    return [{"item": k, "by": v} for k, v in out.items()][:4]


def nav_regions(page, by_sel):
    cands = []
    for e in page.vis:
        if e["tag"] in ("html", "body", "main"): continue
        cls = last_classes(e["sel"])
        if not (e["tag"] == "nav" or REGION_CLS.search(cls) or (e["tag"] == "header" and e["rect"]["y"] < 200)): continue
        items = links_in(page, e)
        if len(items) < 2: continue
        cands.append((e, items))
    page_h = max([x["rect"]["y"] + x["rect"]["h"] for x in page.vis] + [1])
    cands = [(e, items, frozenset(x["id"] for x in items)) for e, items in cands
             if not (e["rect"]["h"] > 0.5 * page_h and e["rect"]["w"] > 0.6 * page.width and e["tag"] != "nav")]      # page-wide layout wrappers
    keep1 = []
    for e, items, ids in cands:
        inner = [d for d in cands if d[0]["id"] != e["id"] and e["id"] in {a["id"] for a in page.ancestors(d[0])}]
        if any(len(d[2]) >= 0.8 * len(ids) for d in inner): continue       # a wrapper around one list: keep the list
        keep1.append((e, items))
    kept_ids = {e["id"] for e, _ in keep1}
    keep = [(e, items) for e, items in keep1 if not any(a["id"] in kept_ids for a in page.ancestors(e))]     # sub-lists of a kept region
    regions = []
    for e, items in sorted(keep, key=lambda t: t[0]["rect"]["y"]):
        anc = page.ancestors(e)
        cls = last_classes(e["sel"])
        pos = next((x["style"]["position"] for x in [e] + anc[:4] if x["style"]["position"] in ("fixed", "sticky")), "static")
        r = e["rect"]
        kind = ("breadcrumb" if re.search(r"breadcrumb", cls, re.I) else "tabs" if sum(1 for x in items if x.get("role") == "tab") * 2 > len(items) or re.search(r"\btabs?\b|tablist|tab-?bar", cls, re.I)
                else "pagination" if re.search(r"pagina|pager", cls, re.I) else "steps" if re.search(r"step", cls, re.I)
                else "footer" if e.get("inFooter") or any(a["tag"] == "footer" for a in anc) else "header" if r["y"] < 160 and r["w"] >= 0.5 * page.width
                else "sidebar" if r["h"] > 1.5 * r["w"] and r["x"] < 0.35 * page.width else "in-page")
        row = page.row(e, kind=kind, position=pos, box=[r["x"], r["y"], r["w"], r["h"]], items=len(items),
                       labels=list(dict.fromkeys(label_of(x) for x in items))[:16], current=current_marks(page, items),
                       dead_links=sum(1 for x in items if x["tag"] == "a" and (x.get("href") in (None, "", "#") or str(x.get("href")).startswith("javascript"))))
        hs = [h for x in items for h in by_sel.get(x["sel"], [])]
        if hs: row["sweep"] = hs[:4]
        regions.append(row)
    return regions[:14]


def breadcrumbs(page, regions):
    out = [r for r in regions if r["kind"] == "breadcrumb"]
    if out: return [{"where": r["where"], "labels": r["labels"]} for r in out]
    for e in page.vis:
        t = btext(e).strip()
        if 6 <= len(t) <= 120 and re.search(r"\S\s*[/›»>]\s*\S+\s*[/›»>]\s*\S", t) and sum(1 for x in page.kids.get(e["id"], []) if x.get("interactive")) >= 2 and e["rect"]["y"] < 2 * SCREEN:
            return [{"where": e["sel"], "text": t[:120], "by": "separator pattern"}]
    return []


def tabs(page, by_sel):
    groups = collections.defaultdict(list)
    tabs_ = [e for e in page.els if e.get("role") == "tab"]
    per_parent = collections.Counter(e.get("parent") for e in tabs_)
    for e in tabs_:       # tabs wrapped one level deeper (Ant, Radix) are grouped by their grandparent
        key = e.get("parent") if per_parent[e.get("parent")] > 1 else (page.byid.get(int(e["parent"])) or {}).get("parent") if e.get("parent") is not None else None
        groups[key].append(e)
    out = []
    for pid, lst in groups.items():
        vis = [x for x in lst if x.get("vis")]
        if len(vis) < 2: continue
        out.append(page.row(vis[0], tabs=len(vis), labels=[label_of(x) for x in vis][:10], selected=current_marks(page, vis),
                            wraps=len({round(x["rect"]["y"] / 8) for x in vis}) > 1))
    attach(out, by_sel)
    return out[:8]


def phone_nav(ev, regions_1440):
    dom = load(ev / "dom-375.json")
    if not dom: return "dom-375.json not captured: the phone navigation is not verified"
    p = Page(dom, 375)
    top = [e for e in p.vis if e.get("interactive") and e["rect"]["y"] < 220]
    toggles = [e for e in top if (e["tag"] == "button" or e.get("role") == "button" or e["tag"] == "summary") and
               (MENU_NAME.search(label_of(e)) or (not label_of(e) and any(k["tag"] == "svg" for k in p.descendants(e))))]
    links = [e for e in top if e["tag"] == "a" and btext(e).strip()]
    head_1440 = next((r for r in regions_1440 if r["kind"] == "header"), None)
    bottom = [e for e in p.vis if e["style"]["position"] == "fixed" and e["rect"]["y"] > 500 and len(links_in(p, e)) >= 3]
    regs = nav_regions(p, {})
    return {"toggle": [{"label": label_of(e) or "(icon, no text)", "where": e["sel"][-100:], "box": [e["rect"]["w"], e["rect"]["h"]]} for e in toggles][:3],
            "top_links_visible_375": [label_of(e) for e in links][:10], "header_items_1440": head_1440["items"] if head_1440 else None,
            "bottom_bar": [{"where": e["sel"][-90:], "items": len(links_in(p, e))} for e in bottom][:2],
            "regions_375": [{"kind": r["kind"], "items": r["items"], "position": r["position"], "current": r["current"]} for r in regs][:6],
            "note": "the capture opens triggers at 1440 only: what the phone menu holds and how it opens and closes is not verified; read shot-375.png and fold-375.png"}


# ---------------------------------------------------------------- overlays the capture opened
def overlays(ev, page, run):
    m = load(ev / "motion.json")
    dets = (load(run / "02-mechanical.json") or {}).get("detectors") or {}
    mhits = [(k, h) for k in ("motion", "motion_snap") for h in ((dets.get(k) or {}).get("hits") or [])]
    closed = {"dialog_elements": sum(1 for e in page.els if e["tag"] == "dialog"),
              "hidden_overlay_like": sum(1 for e in page.els if not e.get("vis") and re.search(r"modal|dialog|drawer|sheet|popover|dropdown|lightbox", last_classes(e["sel"]), re.I))}
    if m is None:
        mi = ((load(ev / "manifest.json") or {}).get("interaction") or {}).get("motion") or {}
        return {"note": "motion.json missing (" + (("skipped: " + mi["skipped"]) if mi.get("skipped") else ("error: " + mi["error"]) if mi.get("error") else "capture predates interaction capture") + "): overlays, menus and disclosures not opened", "in_dom": closed}
    out = []
    for i, t in enumerate(m.get("triggers") or []):
        n = t["runs"].get("normal") or {}
        row = {"t": i, "kind": t["kind"], "name": t["name"][:60], "selector": t["selector"][-100:], "status": n.get("status") + (f" ({n['reason']})" if n.get("reason") else "") if n else "missing"}
        if n.get("status") == "ok":
            ch = n.get("changed") or []
            row["opened"] = [f"{c.get('role') or c.get('tag')}: {(c.get('name') or '')[:40]}" for c in ch][:4]
            row["opened_source"] = n.get("rootSource")
            fin = n.get("final") or []
            row["covers_viewport"] = any(b[2] * b[3] >= 0.8 * VIEW[0] * VIEW[1] for b in fin if len(b) >= 4)
            row["largest_box"] = max(([b[2], b[3]] for b in fin if len(b) >= 4), key=lambda b: b[0] * b[1], default=None)
            # reset: after the run the capture pressed Escape and moved the pointer away; "escape" = the page was back to its state before the click
            row["closed_after_escape"] = None if not ch and n.get("rootSource") == "none" else (n.get("reset") == "escape")
            if n.get("note"): row["note"] = n["note"]
            fr = [f["file"] for f in n.get("frames", []) if (ev / f["file"]).exists()]
            if fr: row["still_open"] = fr[-1]; row["still_before"] = fr[0]
        r = t["runs"].get("reduce") or {}
        if r: row["reduce_status"] = r.get("status")
        pre = f"{t['kind']} trigger \"{t['name'][:40]}\""     # motion hits name the trigger, not its selector
        hs = [f"{k}/{h.get('check')}: {str(h.get('evidence'))[:110]}" for k, h in mhits if str(h.get("where", "")).startswith(pre)]
        if hs: row["sweep"] = hs[:4]
        out.append(row)
    kinds = collections.Counter(r["kind"] for r in out)
    return {"found": m.get("found"), "tried": len(out), "by_kind": dict(kinds), "triggers": out,
            "not_tried": [f"{s.get('name') or s.get('selector')}: {s.get('reason')}" for s in m.get("skipped", [])][:8],
            "not_verified": (m.get("notVerified") or [])[:4], "in_dom": closed,
            "not_measured": "focus moving into an overlay and back to its trigger, scroll lock behind it and a click on the backdrop are not recorded by the capture: read the stills, or list them under not_investigated"}


# ---------------------------------------------------------------- cards, tables, status regions, state text
def cards(page, by_sel):
    groups = collections.defaultdict(list)
    for e in page.vis:
        r = e["rect"]
        if r["h"] < 80 or r["w"] < 140 or e.get("parent") is None: continue
        s = e["style"]
        par = page.byid.get(int(e["parent"])) or {}
        boxed = border_w(s) >= 1 or s.get("boxShadow") not in (None, "none") or (filled(s) and s["backgroundColor"] != (par.get("style") or {}).get("backgroundColor"))
        if not boxed: continue
        groups[(e["parent"], e["tag"], last_classes(e["sel"]).split(" ")[0] if last_classes(e["sel"]) else "")].append(e)
    out = []
    for (pid, tag, cls), lst in groups.items():
        if len(lst) < 3: continue
        inner = [[x for x in page.descendants(c) if x.get("vis") and x.get("interactive")] for c in lst]
        whole = sum(1 for c, ins in zip(lst, inner) if c["tag"] == "a" or any(a["tag"] == "a" for a in page.ancestors(c)[:2]) or
                    (len(ins) == 1 and ins[0]["rect"]["w"] * ins[0]["rect"]["h"] >= 0.8 * c["rect"]["w"] * c["rect"]["h"]))
        row = page.row(lst[0], count=len(lst), size=[lst[0]["rect"]["w"], lst[0]["rect"]["h"]], section=page.section(lst[0]["rect"]["y"]),
                       controls_inside=sorted(len(i) for i in inner)[len(inner) // 2], whole_card_link=whole,
                       with_heading=sum(1 for c in lst if any(x["tag"] in ("h2", "h3", "h4", "h5") for x in page.descendants(c))))
        hs = [h for c in lst for h in by_sel.get(c["sel"], [])]
        if hs: row["sweep"] = hs[:3]
        out.append(row)
    out.sort(key=lambda r: r["y"])
    res = []
    for r in out:       # a grid nested inside another counts once
        if any(r["where"].startswith(x["where"]) for x in res): continue
        res.append(r)
    return res[:12]


def tables(page, ev):
    m375 = load(ev / "dom-375.json")
    w375 = {e["sel"]: e for e in (m375 or {}).get("elements", []) if e["tag"] == "table"}
    out = []
    for e in page.els:
        if e["tag"] != "table": continue
        d = page.descendants(e)
        cells = [x for x in d if x["tag"] == "td" and x.get("vis")]
        nums = [x for x in cells if re.fullmatch(r"[\s$€£¥+\-−–~≈<>]*[\d.,]+\s*(?:%|k|K|M|B|ms|s|x|×)?", btext(x) or "x")]
        al = collections.Counter(x["style"].get("textAlign") for x in nums)
        heads = [btext(x).strip()[:30] for x in d if x["tag"] == "th"]
        row = page.row(e, rows=sum(1 for x in d if x["tag"] == "tr"), header_cells=heads[:10], numeric_cells=len(nums),
                       numeric_align=dict(al), width_px=e["rect"]["w"], section=page.section(e["rect"]["y"]),
                       head_wraps=sum(1 for x in d if x["tag"] == "th" and x.get("vis") and x["rect"]["h"] > 2.2 * px(x["style"]["fontSize"]) * 1.0 + 12))
        p = w375.get(e["sel"])
        if p: row["at_375"] = {"width_px": p["rect"]["w"], "wider_than_screen": p["rect"]["w"] > 375, "visible": p.get("vis")}
        out.append(row)
    return out[:10]


def status_regions(page):
    out = []
    for e in page.els:
        cls = last_classes(e["sel"])
        if not STATUS_CLS.search(cls) or e["tag"] in ("html", "body", "main"): continue
        if any(STATUS_CLS.search(last_classes(a["sel"])) for a in page.ancestors(e)[:3]): continue
        t = btext(e).strip()
        out.append(page.row(e, cls=cls[:60], text=t[:120] or None, fixed=e["style"]["position"] in ("fixed", "sticky")))
    return out[:16]


def state_text(page):
    res = {k: [] for k in STATE_TEXT}
    seen = set()
    for e in page.els:
        t = (etext(e) or "").strip() or (btext(e).strip() if not page.kids.get(e["id"]) else "")
        if not t or len(t) > 160: continue
        for k, rx in STATE_TEXT.items():
            m = rx.search(t)
            if not m or (k, t.lower()) in seen: continue
            seen.add((k, t.lower()))
            res[k].append(page.row(e, text=t[:140], match=m.group(0)))
    classes = collections.Counter()
    ex = {}
    for e in page.els:
        m = STATE_CLS.search(last_classes(e["sel"]))
        if m:
            k = m.group(0).strip(" _-").lower(); classes[k] += 1; ex.setdefault(k, e["sel"][-90:])
    out = {k: v[:14] for k, v in res.items()}
    out["counts"] = {k: len(v) for k, v in res.items()}
    out["hidden_counts"] = {k: sum(1 for r in v if r.get("hidden")) for k, v in res.items()}
    out["state_classes"] = [{"class": k, "elements": n, "example": ex[k]} for k, n in classes.most_common(10)]
    out["note"] = "text and classes in the DOM, shown or hidden: a hidden error or empty template means the state exists; marketing copy also matches ('fewer errors'), so read each row in context"
    return out


# ---------------------------------------------------------------- interaction results
def async_rows(run, ev):
    a = load(ev / "async.json")
    if a is None: return "async.json not captured: loading, failure and success after a primary action are not verified"
    acts = a.get("actions") or []
    if not acts:
        return {"actions": [], "note": "; ".join(a.get("notVerified") or []) or "no primary actions (form submits, action buttons) found",
                "skipped": [f"{s.get('name')}: {s.get('reason')}" for s in a.get("skipped", [])][:6]}
    try:
        from core import Evidence
        from detectors_motion import action_summary
        cfg = (load(run / "resolved-thresholds.json") or {}).get("async_state")
        if not isinstance(cfg, dict):
            cfg = yaml.safe_load((ROOT / "data/thresholds.yaml").read_text(encoding="utf-8"))["detectors"]["async_state"]
        E = Evidence(run)
        rows = []
        for i, act in enumerate(acts):
            S = action_summary(E, act, cfg)
            row = {"a": i, "name": act["name"][:60], "kind": act["kind"], "selector": act["selector"][-90:], "form": (act.get("form") or "")[-80:] or None}
            for mode in ("slow", "fail"):
                r = S.get(mode) or {}
                d = {"status": r.get("status")}
                if str(r.get("status", "")).startswith("ok"):
                    fb = r.get("feedback") or {}
                    d["feedback"] = {k: (None if not v else {"responded": v["responded"], "how": [x for x in (
                        ("label/style " + "+".join(v["trigger_changed"])) if v["trigger_changed"] else None,
                        "aria-busy" if v["busy"] else None, "spinner" if v["spinners"] else None,
                        ("new text: " + " | ".join(v["new_text"])[:100]) if v["new_text"] else None) if x], "pending": v["pending"]}) for k, v in fb.items()}
                    d.update({"requests": r.get("same_origin_requests"), "first_answer_ms": r.get("first_answer_ms"),
                              "final_new_text": (r.get("final_new_text") or [])[:4], "final_success": (r.get("final_success") or [])[:2],
                              "spinner_after_answer": bool(r.get("final_spinners") or r.get("final_busy"))})
                    run_ = act["runs"].get(mode) or {}
                    d["shots"] = [run_.get("before", {}).get("shot")] + [s.get("shot") for s in run_.get("samples", [])]
                    live = [s for s in run_.get("samples", []) if (s.get("state") or {}).get("activeLiveRegions")]
                    if live: d["live_regions"] = live[-1]["state"]["activeLiveRegions"][:3]
                row[mode] = d
            rows.append(row)
    except Exception as x:          # the summary needs the screenshots; report rather than guess
        return {"actions": [{"name": a_["name"][:60], "kind": a_["kind"]} for a_ in acts], "note": f"action summary not computed: {x}"}
    return {"actions": rows, "skipped": [f"{s.get('name')}: {s.get('reason')}" for s in a.get("skipped", [])][:4], "not_verified": (a.get("notVerified") or [])[:4]}


def focus_summary(ev, page):
    f = load(ev / "focus.json")
    if f is None: return "focus.json not captured: keyboard focus not verified"
    stops = [s for s in f if s.get("tag") != "iframe"]
    plain = sum(1 for s in stops if re.match(r"none\b", s.get("outline") or "") and (s.get("boxShadow") or "none") == "none")
    ff = page.dom.get("firstFocusable") or {}
    return {"stops": len(f), "first": f"{ff.get('tag')} \"{(ff.get('text') or '')[:40]}\" href={ff.get('href')}" if ff else None,
            "skip_link_first": bool(ff and ff.get("tag") == "a" and str(ff.get("href") or "").startswith("#")),
            "no_outline_no_shadow": plain, "covered": sum(1 for s in stops if s.get("cover") or s.get("covered")),
            "note": "focus visibility and cover are the sweep's (focus_ring, A11-003): cite its hits; a stop with no outline may still draw a ring another way"}


def table(run, out):
    ev = run / "01-evidence"
    widths = sorted(int(p.stem.split("-")[1]) for p in ev.glob("dom-*.json"))
    if not widths: raise SystemExit(f"no dom-<w>.json in {ev}")
    w = 1440 if 1440 in widths else max(widths)
    dom = load(ev / f"dom-{w}.json")
    page = Page(dom, w)
    man = load(ev / "manifest.json") or {}
    sweep, by_sel = sweep_hits(run)
    fields = field_rows(page, by_sel)
    ch = choice_rows(page, ev, by_sel)
    regions = nav_regions(page, by_sel)
    res = {
        "run": str(run), "target": man.get("target"), "width": w, "captured": str(man.get("started") or "")[:10] or None,
        "landmarks": dom.get("landmarks"),
        "buttons": buttons(page, by_sel), "declared_states": declared_states(dom),
        "fields": fields[:40], "choices": ch, "selects": select_rows(page, by_sel),
        "forms": form_rows(page, dom, ev, fields, ch),
        "navigation": regions, "breadcrumbs": breadcrumbs(page, regions), "tabs": tabs(page, by_sel), "phone_nav": phone_nav(ev, regions),
        "overlays": overlays(ev, page, run), "cards": cards(page, by_sel), "tables": tables(page, ev),
        "status_regions": status_regions(page), "state_text": state_text(page),
        "async": async_rows(run, ev), "focus": focus_summary(ev, page),
        "hidden_content": load(ev / "hidden.json") or "hidden.json not captured",
        "network": {"mode": (man.get("network") or {}).get("mode"), "blocked": len((man.get("network") or {}).get("blocked", [])), "prep": man.get("prep")},
        "sweep": sweep,
    }
    vf = [r for r in fields if not r.get("hidden")]
    res["counts"] = {"buttons": res["buttons"]["count"], "button_variants": res["buttons"]["variant_count"], "fields_visible": len(vf),
                     "fields_placeholder_only": sum(1 for r in vf if r.get("placeholder_only")), "choices": len(ch["choices"]), "selects": len(res["selects"]),
                     "forms": len(res["forms"]["forms"]), "nav_regions": len(regions), "nav_with_current_mark": sum(1 for r in regions if r["current"]),
                     "tabs": len(res["tabs"]), "overlay_triggers": len((res["overlays"].get("triggers") or [])), "card_groups": len(res["cards"]),
                     "tables": len(res["tables"]), "status_regions": len(res["status_regions"]),
                     "async_actions": len(res["async"].get("actions", [])) if isinstance(res["async"], dict) else None}
    out.mkdir(parents=True, exist_ok=True)
    (out / "components-table.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    return res


def summary(res):
    c = res["counts"]
    s = res["sweep"] if isinstance(res["sweep"], dict) else {}
    n = lambda k: (s.get(k) or {}).get("n", "-") if isinstance(s.get(k), dict) else "-"
    ds = res["declared_states"]["rules_with"]
    print(f"components table at {res['width']}px for {res['target']} -> components-table.json")
    print(f"  buttons {c['buttons']} in {c['button_variants']} variant(s); screens with 2+ filled labels {list(res['buttons']['filled_by_screen']) or 'none'}; "
          f"CSS rules: hover {ds['hover']}, focus-visible {ds['focus_visible']}, active {ds['active']}, disabled {ds['disabled']}, invalid {ds['invalid']}, busy {ds['busy']}"
          + (f" ({res['declared_states']['not_verified']})" if res["declared_states"].get("not_verified") else ""))
    print(f"  fields {c['fields_visible']} visible ({c['fields_placeholder_only']} placeholder-only); choices {c['choices']} (defaults {'recorded' if res['choices']['recorded_defaults'] else 'not recorded'}); "
          f"selects {c['selects']}; forms {c['forms']}")
    nav = "; ".join(f"{r['kind']} {r['items']}{' ' + r['position'] if r['position'] != 'static' else ''}"
                    + (f" current={r['current'][0]['item'][:18]}({r['current'][0]['by'][0]})" if r["current"] else " no current mark") for r in res["navigation"][:4])
    pn = res["phone_nav"]
    print(f"  nav: {nav or 'none'}; phone: " + (pn if isinstance(pn, str) else f"toggle {[t['label'] for t in pn['toggle']] or 'none'}, top links {len(pn['top_links_visible_375'])}, bottom bar {len(pn['bottom_bar'])}")
          + f"; breadcrumbs {len(res['breadcrumbs'])}; tab groups {c['tabs']}")
    ov = res["overlays"]
    if ov.get("triggers") is not None:
        opened = [f"{t['kind']} \"{t['name'][:16]}\" esc={'y' if t.get('closed_after_escape') else 'n' if t.get('closed_after_escape') is False else '-'}" for t in ov["triggers"]]
        print(f"  overlays: {', '.join(opened) or 'none tried'}")
    else: print(f"  overlays: {ov.get('note')}")
    st = res["state_text"]["counts"]; hc = res["state_text"]["hidden_counts"]
    print(f"  cards {c['card_groups']} group(s); tables {c['tables']}; status regions {c['status_regions']}; state text "
          + ", ".join(f"{k} {v}{' (' + str(hc[k]) + ' hidden)' if hc[k] else ''}" for k, v in st.items()))
    a = res["async"]
    if isinstance(a, dict) and a.get("actions"):
        bits = []
        for x in a["actions"]:
            fb = ((x.get("slow") or {}).get("feedback") or {}).get("0.5s")
            bits.append(f"\"{x['name'][:20]}\" {'responded' if fb and fb['responded'] else 'no response' if fb else (x.get('slow') or {}).get('status')}")
        print(f"  async: {'; '.join(bits)}")
    else: print(f"  async: {a if isinstance(a, str) else a.get('note')}")
    print("  sweep: " + ", ".join(f"{k} {n(k)}" for k in SWEEP))


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args: print(__doc__); return 2
    run = pathlib.Path(args[0]).resolve()
    out = run / "03-lenses" / "components"
    if "--out" in argv:
        out = pathlib.Path(argv[argv.index("--out") + 1]).resolve()
    ev = (run / "01-evidence").resolve()
    if out == ev or ev in out.parents:
        print("refusing to write into 01-evidence/"); return 2
    res = table(run, out)
    summary(res)
    print(f"wrote {out / 'components-table.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
