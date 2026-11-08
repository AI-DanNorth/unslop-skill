"""Copy and content-integrity detectors (lexicons, budgets, honest forms)."""
import re, collections
from core import detector, hit, px, where, Skip, NotVerified, lexicon, lexicon_patterns
import colorlib as cl

HONEST = re.compile(r"nothing was sent|not connected|did not go through|didn't go through|could not|couldn't|failed|try again|error", re.I)

def own_texts(ev, w=None):
    for e in ev.texts(w):
        yield e, e["text"]
        if e.get("img") and e["img"].get("alt"): yield e, e["img"]["alt"]

def run_lexicon(ev, cfg, name, groups=None, field="text", per_page=True, tier=None):
    pats = lexicon_patterns(name, groups)
    counts = collections.defaultdict(list)
    for e, text in own_texts(ev):
        for g, pol, budget, rx, term in pats:
            for m in rx.finditer(text):
                counts[(g, pol, budget)].append((e, m.group(0), term))
    out = []
    for (g, pol, budget), hits in counts.items():
        if pol == "info": continue
        if pol == "cap" and len(hits) <= budget: continue
        t = tier or ("Finish" if pol == "context" else cfg.get("tier"))
        for e, s, term in hits[:8]:
            out.append(hit(cfg, where(e), f"\"{s}\" ({name}/{g}, {pol}{' budget %d, found %d' % (budget, len(hits)) if pol == 'cap' else ''})", tier=t, value=s, lexicon=f"{name}/{g}"))
    return out

@detector("lexicon_copy")
def lexicon_copy(ev, cfg):
    out = run_lexicon(ev, cfg, "buzzwords") + run_lexicon(ev, cfg, "stock-phrases") + run_lexicon(ev, cfg, "self-labels", groups=["medium-descriptions"])
    # button and link labels: whole accessible name
    lab = lexicon("button-labels")
    empty = {e["term"] for g in lab["groups"] if g["name"] == "empty-labels" for e in g["entries"]}
    arrows = [e["term"] for g in lab["groups"] if g["name"] == "arrow-suffix" for e in g["entries"]]
    arrowed = []
    for e in ev.visible():
        if not e.get("interactive") or e["tag"] not in ("a", "button"): continue
        name = (e.get("name") or "").strip()
        core_name = re.sub(r"\s*(" + "|".join(re.escape(a) for a in arrows) + r")\s*$", "", name).strip().lower()
        if core_name in empty:
            out.append(hit(cfg, where(e), f"link or button labelled \"{name}\": says nothing about where it goes", lexicon="button-labels/empty-labels"))
        if core_name != name.lower() and name: arrowed.append(e)
    if len(arrowed) > 1:
        out += [hit(cfg, where(e), f"arrow glued to label \"{e.get('name')}\" ({len(arrowed)} on page)", lexicon="button-labels/arrow-suffix") for e in arrowed[:5]]
    return out

@detector("chrome_glyphs")
def chrome_glyphs(ev, cfg):
    pats = lexicon_patterns("chrome-glyphs")
    hits = collections.defaultdict(list)
    for e, text in own_texts(ev):
        for g, pol, budget, rx, term in pats:
            if rx.search(text): hits[(g, pol, budget)].append((e, text))
    out = []
    budget_override = cfg.get("budget")
    for (g, pol, budget), lst in hits.items():
        b = budget if budget_override is None else max(budget, budget_override) if pol == "cap" else budget
        if pol == "cap" and len(lst) <= b: continue
        out += [hit(cfg, where(e), f"template chrome ({g}): \"{t[:60]}\"", lexicon=f"chrome-glyphs/{g}") for e, t in lst[:5]]
    return out

@detector("words_per_screen")
def words_per_screen(ev, cfg):
    if cfg.get("enabled") is False: raise Skip("disabled by profile")
    d = ev.dom(); H = cfg["screen_px"]
    slices = collections.Counter()
    for e in ev.texts():
        y = e["rect"]["y"] + e["rect"]["h"] / 2
        slices[int(y // H)] += len(re.findall(r"[\w'’-]+", e["text"]))
    if not slices: raise Skip("no text")
    k, n = max(slices.items(), key=lambda kv: kv[1])
    if n > cfg["fail"]: return [hit(cfg, f"screen {k+1} (y {k*H}-{(k+1)*H}) at {ev.primary}px", f"{n} words on one {H}px screen (fail > {cfg['fail']})", value=n, priority="P1")]
    if n > cfg["warn"]: return [hit(cfg, f"screen {k+1} at {ev.primary}px", f"{n} words on one {H}px screen (warn > {cfg['warn']})", value=n, priority="P2")]
    return []

@detector("page_words")
def page_words(ev, cfg):
    if cfg.get("enabled") is False: raise Skip("disabled by profile")
    n = sum(len(re.findall(r"[\w'’-]+", e["text"])) for e in ev.texts())
    return [hit(cfg, "whole page", f"{n} words on the page (budget {cfg['fail']})", value=n)] if n > cfg["fail"] else []

@detector("h1_words")
def h1_words(ev, cfg):
    if cfg.get("enabled") is False: raise Skip("disabled by profile")
    out = []
    max_chars = round(cfg.get("max_chars", 50) * cfg["fail"] / 7)
    for e in ev.texts():
        if e.get("level") != 1: continue
        n = len(e["text"].split())
        if n > cfg["fail"] or len(e["text"]) > max_chars:
            out.append(hit(cfg, where(e), f"h1 has {n} words / {len(e['text'])} characters (max {cfg['fail']} / {max_chars})", value=n))
    return out

@detector("em_dash")
def em_dash(ev, cfg):
    text = ev.dom()["bodyText"]
    n = text.count("—") + len(re.findall(r"\s–\s", text))
    out = []
    if n > cfg.get("budget", 0):
        out.append(hit(cfg, "whole page", f"{n} em/spaced en dashes (budget {cfg.get('budget', 0)})", value=n))
    if n >= cfg["saturation_count"] and n / max(1, len(text)) * cfg["saturation_per_chars"] >= 1:
        out.append(hit(cfg, "whole page", f"dash saturation: {n} dashes in {len(text)} characters", value=n, priority="P1"))
    return out

@detector("repeated_label")
def repeated_label(ev, cfg):
    d = ev.dom(); out = []
    kids = collections.defaultdict(list)
    for e in ev.texts():
        for a in ev.ancestors(e)[:3]:
            kids[a["id"]].append(e["text"])
    for aid, texts in kids.items():
        c = collections.Counter(t for t in texts if len(t) >= 2)
        for t, n in c.items():
            if n >= cfg["min_repeats_in_card"]:
                out.append(hit(cfg, where(d["byid"][aid]), f"\"{t[:40]}\" repeated {n} times in one container", value=n)); break
    # keep the innermost container only
    seen, res = set(), []
    for h in out:
        if h["evidence"] not in seen: seen.add(h["evidence"]); res.append(h)
    return res[:5]

# ------------------------------------------------------------------ integrity
@detector("invented_metrics")
def invented_metrics(ev, cfg):
    supplied = [s.lower() for s in cfg.get("supplied", [])]
    out = []
    for h in run_lexicon(ev, cfg, "invented-metrics", tier="Floor"):
        if any(s in h["value"].lower() for s in supplied): continue
        h["after"] = "Use the real figure with its source, a [DATA NEEDED] slot, or nothing."
        out.append(h)
    return out

@detector("default_names")
def default_names(ev, cfg):
    return run_lexicon(ev, cfg, "default-names")

@detector("fake_people")
def fake_people(ev, cfg):
    lx = lexicon("fake-people"); terms = [(g["name"], e["term"]) for g in lx["groups"] for e in g["entries"]]
    out = []
    for e in ev.visible():
        srcs = []
        if e.get("img"): srcs.append(e["img"].get("src") or "")
        bi = e["style"]["backgroundImage"]
        if "url(" in bi: srcs.append(bi)
        for s in srcs:
            for g, t in terms:
                if t in s: out.append(hit(cfg, where(e), f"image from {t} ({g}): {s[:80]}", tier="Floor")); break
    return out

@detector("fake_send", needs=("forms.json",))
def fake_send(ev, cfg):
    forms = ev.json("forms.json")
    if not forms: raise Skip("no forms")
    pats = lexicon_patterns("fake-success")
    out = []
    for f in forms:
        for line in f.get("newText", []):
            if HONEST.search(line): continue
            for g, pol, b, rx, term in pats:
                if rx.search(line):
                    out.append(hit(cfg, f"form #{f['index']} (submit \"{f.get('button')}\")", f"with the network blocked the form showed \"{line[:80]}\"", tier="Floor",
                                   after="Nothing was sent: this form is not connected yet.")); break
            else: continue
            break
    return out

@detector("placeholder_residue")
def placeholder_residue(ev, cfg):
    out = run_lexicon(ev, cfg, "self-labels", groups=["residue"], tier="Floor")
    d = ev.dom()
    if re.search(r"lorem ipsum", d.get("title", ""), re.I): out.append(hit(cfg, "<title>", "placeholder title", tier="Floor"))
    return out

@detector("data_slots")
def data_slots(ev, cfg):
    n = len(re.findall(cfg["pattern"], ev.dom()["bodyText"]))
    return [hit(cfg, "whole page", f"{n} [DATA NEEDED] slots (max {cfg['max_per_page']})", value=n)] if n > cfg["max_per_page"] else []
