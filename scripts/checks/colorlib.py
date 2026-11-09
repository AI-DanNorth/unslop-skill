"""Colour helpers: parse computed CSS colours, convert to OKLab/OKLCH, WCAG contrast, APCA (advisory)."""
import math, re

_NUM = r"[-+]?\d*\.?\d+(?:e[-+]?\d+)?"

def parse(s):
    """Return (r, g, b, a) with r,g,b in 0..1 (sRGB) or None. Handles rgb(), rgba(), #hex, oklch(), oklab(), color(srgb ...)."""
    if not s: return None
    s = s.strip().lower()
    if s in ("transparent", "none", ""): return (0, 0, 0, 0)
    if s.startswith("#"):
        h = s[1:]
        if len(h) in (3, 4): h = "".join(c * 2 for c in h)
        if len(h) not in (6, 8): return None
        v = [int(h[i:i + 2], 16) / 255 for i in range(0, len(h), 2)]
        return (v[0], v[1], v[2], v[3] if len(v) == 4 else 1.0)
    m = re.match(r"rgba?\(([^)]*)\)", s)
    if m:
        parts = re.split(r"[\s,/]+", m.group(1).strip())
        vals = [p for p in parts if p]
        def ch(p): return float(p[:-1]) * 2.55 / 255 if p.endswith("%") else float(p) / 255
        r, g, b = (ch(p) for p in vals[:3])
        a = float(vals[3].rstrip("%")) / (100 if vals[3].endswith("%") else 1) if len(vals) > 3 else 1.0
        return (r, g, b, a)
    m = re.match(r"(lab|lch)\(([^)]*)\)", s)      # CSS lab()/lch() (CIELAB D50); phase-2 round 1: L10 colours were unreadable
    if m:
        vals = [p for p in re.split(r"[\s,/]+", m.group(2).strip()) if p]
        def g(p, scale=1.0): return 0.0 if p == "none" else (float(p[:-1]) / 100 * scale if p.endswith("%") else float(p.replace("deg", "")))
        L = g(vals[0], 100.0); a_ = 1.0 if len(vals) < 4 else g(vals[3])
        if m.group(1) == "lab": A, B = g(vals[1], 125.0), g(vals[2], 125.0)
        else:
            import math as _m; C, H = g(vals[1], 150.0), g(vals[2]); A, B = C * _m.cos(_m.radians(H)), C * _m.sin(_m.radians(H))
        fy = (L + 16) / 116; fx = fy + A / 500; fz = fy - B / 200
        inv = lambda t: t ** 3 if t ** 3 > 216 / 24389 else (116 * t - 16) / (24389 / 27)
        X, Y, Z = inv(fx) * 0.96422, inv(fy) * 1.0, inv(fz) * 0.82521          # D50 white
        X, Y, Z = (0.9554734 * X - 0.0230985 * Y + 0.0632593 * Z, -0.0283697 * X + 1.0099956 * Y + 0.0210414 * Z, 0.0123140 * X - 0.0205077 * Y + 1.3303659 * Z)   # Bradford D50 -> D65
        rl, gl, bl = (3.2404542 * X - 1.5371385 * Y - 0.4985314 * Z, -0.9692660 * X + 1.8760108 * Y + 0.0415560 * Z, 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z)
        enc = lambda u: max(0.0, min(1.0, 12.92 * u if u <= 0.0031308 else 1.055 * u ** (1 / 2.4) - 0.055))
        return (enc(rl), enc(gl), enc(bl), a_)
    m = re.match(r"(oklch|oklab)\(([^)]*)\)", s)
    if m:
        vals = [p for p in re.split(r"[\s,/]+", m.group(2).strip()) if p]
        def f(p, scale=1.0): return float(p[:-1]) / 100 * scale if p.endswith("%") else float(p)
        a = f(vals[3]) if len(vals) > 3 else 1.0
        if m.group(1) == "oklch":
            L, C, H = f(vals[0]), f(vals[1], 0.4), float(vals[2].replace("deg", "")) if vals[2] != "none" else 0.0
            A, B = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
        else:
            L, A, B = f(vals[0]), f(vals[1], 0.4), f(vals[2], 0.4)
        r, g, b = oklab_to_srgb(L, A, B)
        return (r, g, b, a)
    m = re.match(r"color\(srgb\s+(" + _NUM + r")\s+(" + _NUM + r")\s+(" + _NUM + r")(?:\s*/\s*(" + _NUM + r"))?\)", s)
    if m:
        return (float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)) if m.group(4) else 1.0)
    return None

def colors_in(s):
    """All colour literals inside a CSS value such as a gradient or box-shadow."""
    if not s: return []
    out = []
    for m in re.finditer(r"(rgba?\([^)]*\)|oklch\([^)]*\)|oklab\([^)]*\)|color\(srgb[^)]*\)|#[0-9a-fA-F]{3,8}\b)", s):
        c = parse(m.group(1))
        if c: out.append(c)
    return out

def _lin(c): return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def _delin(c):
    c = max(0.0, min(1.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055

def srgb_to_oklab(r, g, b):
    r, g, b = _lin(r), _lin(g), _lin(b)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (math.copysign(abs(x) ** (1 / 3), x) for x in (l, m, s))
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)

def oklab_to_srgb(L, A, B):
    l = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
    m = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
    s = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    b = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return (_delin(r), _delin(g), _delin(b))

def oklch(rgb):
    L, A, B = srgb_to_oklab(*rgb[:3])
    C = math.hypot(A, B)
    H = math.degrees(math.atan2(B, A)) % 360
    return (L, C, H)

def oklab_dist(c1, c2):
    a, b = srgb_to_oklab(*c1[:3]), srgb_to_oklab(*c2[:3])
    return math.dist(a, b)

def hsl_sat(rgb):
    r, g, b = rgb[:3]; mx, mn = max(r, g, b), min(r, g, b); l = (mx + mn) / 2
    if mx == mn: return 0.0
    d = mx - mn
    return d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)

def hsl_hue(rgb):
    r, g, b = rgb[:3]; mx, mn = max(r, g, b), min(r, g, b)
    if mx == mn: return 0.0
    d = mx - mn
    if mx == r: h = ((g - b) / d) % 6
    elif mx == g: h = (b - r) / d + 2
    else: h = (r - g) / d + 4
    return h * 60

def luminance(rgb):
    r, g, b = (_lin(c) for c in rgb[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(c1, c2):
    l1, l2 = luminance(c1), luminance(c2)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)

def over(fg, bg):
    """Composite fg (with alpha) over opaque bg."""
    a = fg[3] if len(fg) > 3 else 1.0
    return tuple(fg[i] * a + bg[i] * (1 - a) for i in range(3)) + (1.0,)

def apca(text, bg):
    """APCA-W3 0.0.98G Lc (advisory only). Positive = dark text on light."""
    def y(c):
        r, g, b = (x ** 2.4 for x in c[:3])
        v = 0.2126729 * r + 0.7151522 * g + 0.0721750 * b
        return v if v > 0.022 else v + (0.022 - v) ** 1.414
    yt, yb = y(text), y(bg)
    if abs(yb - yt) < 0.0005: return 0.0
    if yb > yt:
        s = (yb ** 0.56 - yt ** 0.57) * 1.14
        return 0.0 if s < 0.1 else (s - 0.027) * 100
    s = (yb ** 0.65 - yt ** 0.62) * 1.14
    return 0.0 if s > -0.1 else (s + 0.027) * 100

def hexstr(c): return "#%02x%02x%02x" % tuple(int(round(max(0, min(1, x)) * 255)) for x in c[:3])
