"""Shared machinery for sweep detectors: registry, evidence loader, config resolution."""
import json, pathlib, re, functools
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
REGISTRY = {}

class Skip(Exception):
    """Detector does not apply to this artifact (status: skipped)."""
class NotVerified(Exception):
    """Detector applies but its evidence is missing or untrustworthy (status: not-verified)."""

def detector(name, needs=()):
    def wrap(fn):
        REGISTRY[name] = {"fn": fn, "needs": needs}
        return fn
    return wrap

def hit(cfg, where, evidence, value=None, after=None, tier=None, width=None, **extra):
    h = {"rule": cfg["rule"], "tier": tier or cfg.get("tier", "Reflex"), "where": where, "evidence": evidence}
    if width: h["width"] = width
    if value is not None: h["value"] = value
    if after is not None: h["after"] = after
    h.update(extra)
    return h

# ---------------------------------------------------------------- config
def _merge(base, over):
    for k, v in (over or {}).items():
        if isinstance(v, dict) and isinstance(base.get(k), dict): _merge(base[k], v)
        else: base[k] = v
    return base

def resolve(profile="balanced", medium="web", contract_overrides=None):
    """core default <- profile <- media adapter <- brand/brief overrides (core/precedence.md)."""
    thr = yaml.safe_load((ROOT / "data/thresholds.yaml").read_text())
    prof = yaml.safe_load((ROOT / f"core/profiles/{profile}.yaml").read_text())
    _merge(thr["detectors"], prof.get("detectors"))
    media_file = ROOT / f"skills/media-{medium}/thresholds.yaml"
    if media_file.exists():
        _merge(thr["detectors"], (yaml.safe_load(media_file.read_text()) or {}).get("detectors"))
    _merge(thr["detectors"], contract_overrides or {})
    floors = {k for k, v in yaml.safe_load((ROOT / "data/thresholds.yaml").read_text())["detectors"].items() if v.get("tier") == "Floor"}
    for k in floors: thr["detectors"][k]["tier"] = "Floor"          # floors never bend
    thr["profile"] = prof
    return thr

@functools.lru_cache(None)
def lexicon(name):
    return yaml.safe_load((ROOT / f"data/lexicons/{name}.yaml").read_text())

def lexicon_patterns(name, groups=None):
    """[(group, policy, budget, compiled_regex, term)] for a lexicon."""
    lx = lexicon(name)
    out = []
    for g in lx["groups"]:
        if groups and g["name"] not in groups: continue
        for e in g["entries"]:
            t = e["term"]
            is_re = any(ch in t for ch in "\\[](){}^$|?+*") and not t.startswith("#")
            if is_re: pat = t
            else:
                pat = re.escape(t)
                if re.match(r"\w", t): pat = r"(?<![\w-])" + pat
                if re.search(r"\w$", t): pat = pat + r"(?:s|es|ed|ing|ly|d)?(?![\w-])"
            flags = 0 if lx.get("match", "").startswith("case-sensitive") else re.I
            try: out.append((g["name"], g.get("policy", "fail"), g.get("budget", 0), re.compile(pat, flags | re.M), t))
            except re.error: pass
    return out

# ---------------------------------------------------------------- evidence
class Evidence:
    def __init__(self, run_dir):
        self.run = pathlib.Path(run_dir)
        self.dir = self.run / "01-evidence"
        if not (self.dir / "manifest.json").exists(): raise SystemExit(f"no capture at {self.dir}")
        self.manifest = json.loads((self.dir / "manifest.json").read_text())
        self.widths = sorted(self.manifest["widths"])
        self._dom, self._img = {}, {}

    @property
    def primary(self):
        return 1440 if 1440 in self.widths else (1280 if 1280 in self.widths else max(self.widths))

    def has(self, name): return (self.dir / name).exists()

    def json(self, name):
        p = self.dir / name
        if not p.exists(): raise NotVerified(f"{name} not captured")
        return json.loads(p.read_text())

    def dom(self, w=None):
        w = w or self.primary
        if w not in self._dom:
            p = self.dir / f"dom-{w}.json"
            if not p.exists(): raise NotVerified(f"no DOM capture at {w}px")
            d = json.loads(p.read_text())
            d["byid"] = {e["id"]: e for e in d["elements"]}
            self._dom[w] = d
        return self._dom[w]

    def img(self, name):
        if name not in self._img:
            import numpy as np
            from PIL import Image
            p = self.dir / name
            if not p.exists(): raise NotVerified(f"{name} not captured")
            self._img[name] = np.array(Image.open(p).convert("RGB"))
        return self._img[name]

    # ---- exhibits: regions a page shows on purpose as examples (a slop specimen, a "before" panel) -------------
    # sweep sets skip_exhibits for the slop-tell detectors listed in thresholds.yaml `exhibits`; texts() and visible()
    # then leave those regions out. Accessibility detectors never skip them: a user still meets those failures.
    skip_exhibits = False
    exhibit_cfg = None

    def exhibit_ids(self, w=None):
        w = w or self.primary
        key = ("exhibits", w)
        if key in self._dom: return self._dom[key]
        cfg = self.exhibit_cfg or {}
        pat = re.compile(cfg.get("pattern", r"$^"), re.I)
        d = self.dom(w); els = d["elements"]
        page_h = max([e["rect"]["y"] + e["rect"]["h"] for e in els if e["vis"]] + [1])
        roots = set()
        for e in els:
            if e["tag"] in ("html", "body", "main"): continue
            last = e["sel"].split(" > ")[-1]
            names = " ".join(re.findall(r"[.#]((?:\\.|[\w-])+)", last)).replace("\\", "")
            if names and pat.search(names) and e["rect"]["h"] <= cfg.get("max_share", 0.5) * page_h: roots.add(e["id"])
        inside, memo = set(), {}
        def walk(e):
            i = e["id"]
            if i in memo: return memo[i]
            memo[i] = False
            p = e.get("parent")
            par = d["byid"].get(int(p)) if p is not None else None
            memo[i] = i in roots or (par is not None and walk(par))
            return memo[i]
        for e in els:
            if walk(e): inside.add(e["id"])
        self._dom[key] = (roots, inside)
        return self._dom[key]

    def _own(self, lst, w):
        if not self.skip_exhibits: return lst
        roots, inside = self.exhibit_ids(w)
        return [e for e in lst if e["id"] not in inside] if inside else lst

    # convenience
    def texts(self, w=None, min_len=1):
        return self._own([e for e in self.dom(w)["elements"] if e["vis"] and e["textLen"] >= min_len], w)

    def visible(self, w=None):
        return self._own([e for e in self.dom(w)["elements"] if e["vis"]], w)

    def ancestors(self, e, w=None):
        d = self.dom(w); out = []
        p = e.get("parent")
        while p is not None:
            a = d["byid"].get(int(p))
            if not a: break
            out.append(a); p = a.get("parent")
        return out

    def words(self, w=None):
        return re.findall(r"[\w'’-]+", self.dom(w)["bodyText"])

def px(v):
    try: return float(str(v).replace("px", ""))
    except ValueError: return 0.0

def where(e):
    return e["sel"] + (f'  "{e["text"][:50]}"' if e.get("text") else "")
