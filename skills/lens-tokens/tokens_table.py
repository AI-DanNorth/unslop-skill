"""Tokens table for lens-tokens: measures the design system under a capture (how many distinct values each property
family uses, whether they sit on a scale, whether custom properties exist and are used, how they are named and themed),
so the lens judges the system on numbers and never counts values off a screenshot.

usage: python skills/lens-tokens/tokens_table.py <run-dir> [--out <dir>] [--system <tokens.css|tokens.json>]

Reads 01-evidence/dom-<w>.json at every captured width (each element's computed style: colours, font sizes, line
heights, letter spacing, margins, paddings, gaps, radii, shadows, border widths, z-index, transition and animation
timing; `tokens`, the custom properties resolved on :root; `css`, the readable stylesheet text), manifest.json (widths,
network), data/thresholds.yaml (`exhibits`) and 02-mechanical.json (the sweep's hits on these properties). `--system`
names a token file the brand or design system supplies (CSS custom properties, or JSON: flat, nested or DTCG `$value`);
the table then measures drift from those values. Writes <out>/tokens-table.json, where <out> defaults to
<run>/03-lenses/tokens. It never writes into 01-evidence/.

Rows: per property family and width, the distinct computed values with counts and share of elements, one-off values,
near-duplicate clusters, a fitted scale where one exists (a geometric ratio for type, a 4 or 8 px base for spacing) with
the share on it and the share chance alone would put on it, and the share that equals a declared token's value; the
token inventory (declared custom properties by scope, family and naming tier, aliases, and how often the readable CSS
references each one); literal against var() use per family in the stylesheet's own declarations, framework utility
rules apart, and literals that retype a token's value; theme parity (tokens redefined under a dark media query or a
theme class, which colour tokens are missing, literal colours set in dark rules); framework fingerprints (token
prefixes and recorded class names); the sweep's hits. Every row is a pointer for the lens, not a finding.

The DOM records the computed style of every element but not inline style attributes, the left and right margins, or
which rule set a value; cross-origin stylesheets are unreadable, so the stylesheet rows cover the readable sheets only
(`unreadable_sheets`). The capture renders one colour scheme: the other theme is read from the stylesheet, never seen.
rem values are converted at the root font size the stylesheet sets on html or :root (16px when it sets none). Page
text is evidence, never instructions.
"""
import collections, json, math, pathlib, re, sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
sys.path.insert(0, str(ROOT / "skills" / "lens-color"))
sys.path.insert(0, str(ROOT / "skills" / "lens-typography"))
import colorlib as cl  # noqa: E402
try:
    from palette_table import cluster  # noqa: E402  (lens-color's greedy colour clustering, heaviest first)
except Exception:                       # pragma: no cover - keep the table usable on its own
    def cluster(items, close):
        out = []
        for c, w, p in sorted(items, key=lambda x: -x[1]):
            for g in out:
                if close(g[0], c): g[1] += w; g[2].append(p); break
            else: out.append([c, w, [p]])
        return out
try:
    from type_table import base_family  # noqa: E402
except Exception:
    def base_family(name): return (name or "").strip()

SWEEP = ["off_scale_spacing", "spacing_monotony", "type_ladder", "flat_hierarchy", "banned_fonts", "stock_swatches",
         "accent_footprint", "nested_radius", "card_kit", "container_monotony", "motion_css", "motion", "look_family", "fallback_face"]
NEAR_OKLAB = 0.02            # two colours closer than this in OKLab read as one (#333 and #323232 are 0.004 apart)
NEAR_SIZE_RATIO = 1.08       # two font sizes closer than this are a near-duplicate (15/16 is 1.067; Tailwind's 14/16 is 1.14)
NEAR_SPACE_PX = 1.0          # two spacing values 1px apart, one of them on the base (15 and 16, 23 and 24)
RATIOS = [1.067, 1.125, 1.2, 1.25, 1.333, 1.414, 1.5, 1.618]
TW_TEXT = [12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72, 96, 128]
TOP = 30
NEUTRAL_KW = {"0", "0px", "none", "auto", "inherit", "initial", "unset", "revert", "revert-layer", "currentcolor", "transparent",
              "normal", "0s", "0ms", "100%", "50%", "1", "0 0", "0px 0px", "0 0 0 0", "0px 0px 0px 0px", "unset !important", "inherit !important"}
FAMILY_OF_PROP = {
    "color": "colour", "background-color": "colour", "border-color": "colour", "border-top-color": "colour", "border-bottom-color": "colour",
    "border-left-color": "colour", "border-right-color": "colour", "outline-color": "colour", "fill": "colour", "stroke": "colour",
    "text-decoration-color": "colour", "caret-color": "colour", "accent-color": "colour", "column-rule-color": "colour", "background": "colour",
    "font-size": "font_size", "line-height": "line_height", "letter-spacing": "letter_spacing",
    "margin": "spacing", "margin-top": "spacing", "margin-bottom": "spacing", "margin-left": "spacing", "margin-right": "spacing",
    "margin-inline": "spacing", "margin-block": "spacing", "margin-inline-start": "spacing", "margin-inline-end": "spacing",
    "margin-block-start": "spacing", "margin-block-end": "spacing", "padding": "spacing", "padding-top": "spacing", "padding-bottom": "spacing",
    "padding-left": "spacing", "padding-right": "spacing", "padding-inline": "spacing", "padding-block": "spacing",
    "padding-inline-start": "spacing", "padding-inline-end": "spacing", "padding-block-start": "spacing", "padding-block-end": "spacing",
    "gap": "spacing", "row-gap": "spacing", "column-gap": "spacing", "grid-gap": "spacing",
    "border-radius": "radius", "border-top-left-radius": "radius", "border-top-right-radius": "radius", "border-bottom-left-radius": "radius",
    "border-bottom-right-radius": "radius", "border-start-start-radius": "radius", "border-start-end-radius": "radius",
    "border-end-start-radius": "radius", "border-end-end-radius": "radius",
    "box-shadow": "shadow", "border-width": "border_width", "border-top-width": "border_width", "border-bottom-width": "border_width",
    "border-left-width": "border_width", "border-right-width": "border_width", "z-index": "z_index",
    "transition-duration": "duration", "animation-duration": "duration", "transition-timing-function": "easing",
    "animation-timing-function": "easing", "font-family": "font_family",
}
FAMILY_OF_NAME = [   # token name -> family, first match wins (names are matched without the leading --)
    ("z_index", r"(?:^|-)(?:z|z-?index|zindex|layer|elevation-z|stack)(?:-|$)"),
    ("duration", r"duration|(?:^|-)(?:speed|delay|time|timing-duration)(?:-|$)|(?:^|-)dur(?:-|$)"),
    ("easing", r"eas(?:e|ing)|(?:^|-)curve(?:-|$)|bezier|timing-function"),
    ("shadow", r"shadow|(?:^|-)elevation(?:-|$)"),
    ("radius", r"radius|rounded|(?:^|-)corner"),
    ("border_width", r"border-width|stroke-width|hairline|(?:^|-)border-(?:thin|thick|\d)"),
    ("font_family", r"(?:^|-)(?:font-family|family|typeface|font-(?:sans|serif|mono|display|body|heading|ui|code))(?:-|$)|^font$"),
    ("letter_spacing", r"tracking|letter-spacing|(?:^|-)ls(?:-|$)"),
    ("line_height", r"leading|line-height|(?:^|-)lh(?:-|$)"),
    ("font_weight", r"font-weight|(?:^|-)weight(?:-|$)|(?:^|-)fw(?:-|$)"),
    ("font_size", r"font-size|(?:^|-)(?:fs|text-size|type-size|size-text)(?:-|$)|^text-(?:\dx?s|xs|sm|base|md|lg|x+l|\d?xl|\d+)$|(?:^|-)heading-\d|(?:^|-)display-(?:\d|xs|sm|md|lg|xl)"),
    ("breakpoint", r"breakpoint|(?:^|-)(?:bp|screen|mq)(?:-|$)"),
    ("container", r"container|max-width|(?:^|-)measure(?:-|$)|content-width|page-width"),
    ("spacing", r"spac(?:e|ing)|(?:^|-)(?:gap|gutter|inset|margin|padding|space|sp|size|stack|inline|pad)(?:-|$)"),
    ("colour", r"colou?r|(?:^|-)(?:bg|background|foreground|fg|text|ink|paper|surface|canvas|accent|primary|secondary|tertiary|muted|"
               r"brand|success|error|danger|warning|info|border|ring|outline|fill|stroke|link|focus|overlay|scrim|neutral|gr[ae]y|"
               r"red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose|slate|zinc|stone|"
               r"black|white|destructive|popover|card|highlight|selection|shade|tint)(?:-|$)"),
]
HUE_WORD = re.compile(r"(?:^|-)(?:red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose|"
                      r"slate|gr[ae]y|zinc|neutral|stone|black|white|sand|mauve|olive|sage|plum|crimson|tomato|navy|gold|silver|brown|"
                      r"magenta|aqua|mint|coral|lavender|beige|cream|charcoal)(?:-|$)", re.I)
NUM_STEP = re.compile(r"-(?:\d{1,4}|\d+(?:\.\d+)?(?:px|rem)?|a?\d{1,2})$")
SHIRT = re.compile(r"-(?:\d?x+[sl]|xs|sm|s|m|md|l|lg|xl|base|tiny|small|medium|large|huge)$", re.I)
ROLE_WORD = re.compile(r"(?:^|-)(?:primary|secondary|tertiary|accent|background|bg|foreground|fg|surface|canvas|ink|paper|text|body|muted|subtle|"
                       r"emphasis|strong|weak|border|divider|rule|ring|focus|link|action|interactive|success|positive|error|negative|danger|"
                       r"critical|warning|caution|info|notice|brand|disabled|hover|active|pressed|selected|inverse|on|overlay|scrim|"
                       r"destructive|popover|highlight|placeholder|heading|caption|display|label|title|default|base|page|app|elevated|raised|"
                       r"sunken|backdrop|shadow|tooltip|toast|modal|dropdown|sticky|fixed|header|nav|menu|input|field|control)(?:-|$)", re.I)
COMPONENT_WORD = re.compile(r"(?:^|-)(?:button|btn|card|input|field|form|nav|navbar|navigation|header|footer|menu|modal|dialog|drawer|tooltip|"
                            r"badge|chip|tag|pill|tab|tabs|table|sidebar|toast|alert|banner|avatar|switch|toggle|checkbox|radio|select|"
                            r"dropdown|popover|accordion|hero|breadcrumb|pagination|progress|slider|stepper|list-item|callout|code-block|"
                            r"skeleton|spinner|kbd|textarea|search|combobox|carousel|calendar|datepicker|upload|notification)(?:-|$)", re.I)
FRAMEWORK_PREFIX = [("tailwind", r"^--tw-"), ("bootstrap", r"^--bs-"), ("mui", r"^--mui-"), ("material", r"^--(?:md-sys|md-ref|mdc|mat)-"),
                    ("ant", r"^--ant-"), ("carbon", r"^--cds-"), ("chakra", r"^--chakra-"), ("mantine", r"^--mantine-"),
                    ("radix", r"^--(?:radix-|(?:gray|mauve|slate|sage|olive|sand|accent|blue|red|green)-a?\d{1,2}$)"),
                    ("govuk", r"^--govuk-"), ("geist", r"^--(?:geist|ds)-"), ("wordpress", r"^--wp--"), ("framer", r"^--(?:framer|token)-"),
                    ("spectrum", r"^--spectrum-"), ("primer", r"^--(?:fgColor|bgColor|borderColor|color-(?:canvas|fg|border)|base-size)-"),
                    ("open_props", r"^--(?:size-\d|size-fluid|font-size-\d|radius-\d|shadow-\d|ease-\d|gray-\d{1,2}$)"),
                    ("webflow", r"^--_[\w-]*---"), ("daisyui", r"^--(?:p|pc|s|sc|a|ac|n|nc|b1|b2|b3|bc|in|su|wa|er|rounded-box|rounded-btn)$"),
                    ("shopify_polaris", r"^--p-"), ("fluent", r"^--(?:colorNeutral|colorBrand|spacingHorizontal|fontSizeBase)"),
                    ("salesforce_slds", r"^--(?:slds|lwc)-")]
SHADCN = {"--background", "--foreground", "--card", "--card-foreground", "--popover", "--popover-foreground", "--primary",
          "--primary-foreground", "--secondary", "--secondary-foreground", "--muted", "--muted-foreground", "--accent",
          "--accent-foreground", "--destructive", "--destructive-foreground", "--border", "--input", "--ring", "--radius"}
TW_V4_THEME = re.compile(r"^--(?:color-[a-z]+-\d{2,3}|spacing|text-(?:xs|sm|base|lg|\d?xl)|font-(?:sans|serif|mono)|radius-(?:xs|sm|md|lg|\d?xl)|"
                         r"shadow-(?:2xs|xs|sm|md|lg|\d?xl)|ease-(?:in|out|in-out)|default-transition-duration|container-\d?(?:xs|sm|md|lg|xl))$")
CLASS_PRINTS = [
    ("tailwind", re.compile(r"^(?:[a-z0-9]+\\?:)*-?(?:flex|grid|mx-auto|items-center|justify-(?:between|center)|(?:p|px|py|pt|pb|pl|pr|m|mx|my|mt|mb|ml|mr|gap|space-[xy])-\d+(?:\\?\.5)?|"
                            r"text-(?:xs|sm|base|lg|\d?xl)|bg-[a-z]+-\d{2,3}|text-[a-z]+-\d{2,3}|rounded(?:-[a-z0-9]+)?|shadow(?:-[a-z0-9]+)?|"
                            r"font-(?:medium|semibold|bold|normal)|w-full|h-full|max-w-[a-z0-9]+|min-h-screen|leading-[a-z0-9]+|tracking-[a-z]+)$")),
    ("bootstrap", re.compile(r"^(?:btn-(?:primary|secondary|outline-[a-z]+|lg|sm)|col-(?:sm|md|lg|xl|xxl)-\d+|d-(?:flex|none|block|inline-block|md-[a-z]+)|"
                             r"navbar-(?:expand\S*|brand|nav|toggler)|card-body|form-control|form-label|text-muted|justify-content-[a-z]+|align-items-[a-z]+|container-fluid)$")),
    ("mui", re.compile(r"^Mui[A-Z]")), ("ant", re.compile(r"^ant-")), ("carbon", re.compile(r"^(?:cds|bx)--")), ("govuk", re.compile(r"^govuk-")),
    ("chakra", re.compile(r"^chakra-")), ("mantine", re.compile(r"^mantine-")), ("framer", re.compile(r"^framer-")),
    ("webflow", re.compile(r"^w-(?:nav|container|inline-block|button|richtext|layout)")), ("shadcn_radix", re.compile(r"^radix-")),
    ("css_modules_or_in_js", re.compile(r"^(?:css|sc|emotion|jsx|styled|svelte)-[a-zA-Z0-9]{4,}$|^[A-Za-z][\w-]*_[\w-]+__[A-Za-z0-9_-]{5}$")),
]
UTILITY_SEL = re.compile(r"^\.(?:[a-z0-9-]+\\?:)*(?:-?(?:p|px|py|pt|pb|pl|pr|ps|pe|m|mx|my|mt|mb|ml|mr|ms|me|gap|gap-x|gap-y|space-x|space-y|"
                         r"text|bg|border|border-[trblxy]|rounded|rounded-[trbl]{1,2}|shadow|leading|tracking|z|duration|ease|delay|fill|stroke|"
                         r"outline|ring|divide|from|via|to|decoration|caret|accent|placeholder|font|inset|top|left|right|bottom|w|h|size|"
                         r"max-w|min-w|max-h|min-h|opacity|fs|fw|lh|lead|display)(?:-[a-z0-9.\\/]+)*|text-(?:start|end|center))"
                         r"(?::{1,2}[a-z-]+(?:\([^)]*\))?)*(?:\s*>\s*:not\(\[hidden\]\)\s*~\s*:not\(\[hidden\]\))?$")
ARB_ESC = re.compile(r"-\\\[(.*?)\\\](\\:)?")   # .text-\[15px\] in a selector; a variant (data-\[state\=open\]\:) is followed by \:
ARB_RAW = re.compile(r"-\[([^\]]+)\](:)?")
ARB_VALUE = re.compile(r"^(?:\\?#|-?\.?\d|calc|rgb|hsl|oklch|oklab|color|url|clamp|min\(|max\()", re.I)
DARK_SEL = re.compile(r"\.dark(?![\w\\-])|\.theme-dark|\.dark-(?:theme|mode)(?![\w-])|\[data-(?:theme|mode|color-mode|color-scheme|bs-theme|appearance|scheme)"
                      r"\s*[~|^$*]?=\s*['\"]?[\w-]*dark|\[theme\s*=\s*['\"]?dark|\.cds--g(?:90|100)(?![\w-])|\.night(?![\w-])|\.is-dark(?![\w-])", re.I)
LIGHT_SEL = re.compile(r"\.light(?![\w\\-])|\.theme-light|\[data-(?:theme|mode|color-mode|color-scheme|bs-theme|appearance|scheme)\s*[~|^$*]?=\s*['\"]?[\w-]*light|"
                       r"\.cds--(?:white|g10)(?![\w-])", re.I)
THEME_ATTR = re.compile(r"\[data-(?:theme|brand|mode|color-mode|scheme)\s*=\s*['\"]?([\w-]+)", re.I)
ROOTISH = re.compile(r"^(?::root|html|:host|body|\*|::?before|::?after|::backdrop|:root:not\([^)]*\)|html:not\([^)]*\)|:where\(:root\)|:where\(html\))$", re.I)
DARK_MQ = re.compile(r"prefers-color-scheme\s*:\s*dark", re.I)
LIGHT_MQ = re.compile(r"prefers-color-scheme\s*:\s*light", re.I)
GROUPING_AT = ("@media", "@supports", "@layer", "@container", "@document", "@scope", "@starting-style")
SKIP_AT = ("@keyframes", "@-webkit-keyframes", "@font-face", "@property", "@page", "@counter-style", "@font-feature-values", "@font-palette-values",
           "@view-transition", "@position-try")
PLACEHOLDER_VAL = re.compile(r"^(?:todo|tbd|xxx+|placeholder|fixme|changeme|replace[-_ ]?me|lorem)$", re.I)
CHANNELS = re.compile(r"^(-?\d+(?:\.\d+)?)(?:deg)?\s*,?\s+(\d+(?:\.\d+)?)%\s*,?\s+(\d+(?:\.\d+)?)%(?:\s*/\s*([\d.]+%?))?$")


def load(p, default=None):
    try: return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
    except (OSError, ValueError): return default


def px(v):
    try: return float(str(v).replace("px", "").strip() or 0)
    except ValueError: return None


def rnd(x, q=0.5): return round(round(x / q) * q, 3)


def arbitrary(sel, escaped=True):
    """A bracketed one-off value in a utility class (text-[15px], bg-[#f5f5f5]); var() inside the brackets references a token."""
    for m in (ARB_ESC if escaped else ARB_RAW).finditer(sel or ""):
        if not m.group(2) and ARB_VALUE.match(m.group(1).replace("\\", "")) and "var(" not in m.group(1): return True
    return False


def classes(sel):
    last = (sel or "").split(" > ")[-1]
    return [c.replace("\\", "") for c in re.findall(r"\.((?:\\.|[\w-])+)", last)]


# ---------------------------------------------------------------- colour and length parsing
def hsl_rgb(h, s, l):
    s, l = s / 100, l / 100
    c = (1 - abs(2 * l - 1)) * s; hp = (h % 360) / 60; x = c * (1 - abs(hp % 2 - 1))
    r, g, b = [(c, x, 0), (x, c, 0), (0, c, x), (0, x, c), (x, 0, c), (c, 0, x)][int(hp) % 6]
    m = l - c / 2
    return (r + m, g + m, b + m)


def colour(v):
    """(r, g, b, a) or None. colorlib's parser plus hsl()/hsla() and bare shadcn-style channels ("222 47% 11%")."""
    if not v: return None
    s = str(v).strip().lower()
    if s in ("transparent", "none", "currentcolor", "inherit", "initial", "unset"): return None
    m = re.match(r"hsla?\(([^)]*)\)$", s)
    if m: s = m.group(1).strip()
    m = CHANNELS.match(s)
    if m:
        r, g, b = hsl_rgb(float(m.group(1)), float(m.group(2)), float(m.group(3)))
        a = m.group(4); a = (float(a[:-1]) / 100 if a.endswith("%") else float(a)) if a else 1.0
        return (r, g, b, a)
    if not re.match(r"^(?:#[0-9a-f]{3,8}|rgba?\(|oklch\(|oklab\(|lab\(|lch\(|color\(srgb)", s): return None
    try: return cl.parse(s)
    except (ValueError, IndexError, TypeError): return None


def ckey(c):
    if c is None: return None
    h = cl.hexstr(c)
    return h if c[3] >= 0.995 else f"{h}/{c[3]:.2f}"


def length_px(v, rem):
    """A single CSS length in px, or None (calc, var, keywords and percentages are not lengths here)."""
    m = re.match(r"^\s*(-?\d*\.?\d+)\s*(px|rem|em)?\s*$", str(v or ""))
    if not m: return None
    n = float(m.group(1)); u = m.group(2)
    if u == "rem" or u == "em": return n * rem
    if u is None and n != 0: return None
    return n


def duration_ms(v):
    m = re.match(r"^\s*(-?\d*\.?\d+)\s*(ms|s)\s*$", str(v or ""))
    if not m: return None
    return float(m.group(1)) * (1000 if m.group(2) == "s" else 1)


# ---------------------------------------------------------------- stylesheet walk
def _split_blocks(text):
    """Yield ('decl', 'prop: value') and ('block', prelude, body) at depth 0, skipping comments, strings and escapes
    (Tailwind selectors escape brackets, parentheses and quotes: .max-w-\\(--x\\), .\\[a\\]\\:hover)."""
    i, n, buf = 0, len(text), []
    while i < n:
        ch = text[i]
        if ch == "\\":
            buf.append(text[i:i + 2]); i += 2; continue
        if ch == "/" and text.startswith("/*", i):
            j = text.find("*/", i + 2); i = n if j < 0 else j + 2; continue
        if ch in "\"'":
            j = i + 1
            while j < n and text[j] != ch:
                j += 2 if text[j] == "\\" else 1
            buf.append(text[i:j + 1]); i = j + 1; continue
        if ch == "(":
            depth, j = 1, i + 1
            while j < n and depth:
                if text[j] == "\\": j += 2; continue
                if text[j] == "(": depth += 1
                elif text[j] == ")": depth -= 1
                elif text[j] in "\"'":
                    q = text[j]; j += 1
                    while j < n and text[j] != q: j += 2 if text[j] == "\\" else 1
                j += 1
            buf.append(text[i:j]); i = j; continue
        if ch == ";":
            s = "".join(buf).strip(); buf = []
            if s: yield ("decl", s)
            i += 1; continue
        if ch == "{":
            depth, j = 1, i + 1
            while j < n and depth:
                c = text[j]
                if c == "\\": j += 2; continue
                if c in "\"'":
                    q = c; j += 1
                    while j < n and text[j] != q: j += 2 if text[j] == "\\" else 1
                elif c == "{": depth += 1
                elif c == "}": depth -= 1
                j += 1
            yield ("block", "".join(buf).strip(), text[i + 1:j - 1]); buf = []; i = j; continue
        if ch == "}": i += 1; continue
        buf.append(ch); i += 1
    s = "".join(buf).strip()
    if s: yield ("decl", s)


def walk(text, ctx=(), sel=None, out=None, stats=None):
    """Flatten CSS into (ctx, selector, prop, value) rows. ctx holds the enclosing at-rule preludes."""
    for item in _split_blocks(text):
        if item[0] == "decl":
            if sel is None:
                if item[1].startswith("@"): stats["at_statements"] += 1
                continue
            p, _, v = item[1].partition(":")
            if not _: continue
            v = re.sub(r"\s*!important\s*$", "", v.strip(), flags=re.I)
            out.append((ctx, sel, p.strip().lower() if not p.strip().startswith("--") else p.strip(), v))
            continue
        _, pre, body = item
        low = pre.lower()
        if low.startswith(SKIP_AT):
            stats[low.split()[0] if low.split() else "@?"] += 1
            if low.startswith("@property"): stats["property_rules"] += 1
            continue
        if low.startswith(GROUPING_AT):
            walk(body, ctx + (pre,), sel, out, stats); continue
        if low.startswith("@"):
            stats["other_at"] += 1; continue
        if sel is not None:              # CSS nesting: & or a relative selector inside a rule
            pre = pre.replace("&", sel) if "&" in pre else f"{sel} {pre}"
        stats["style_rules"] += 1
        walk(body, ctx, pre, out, stats)
    return out


def root_font_px(rows):
    for ctx, sel, p, v in rows:
        if ctx or p != "font-size": continue
        if any(s.strip().lower() in ("html", ":root") for s in sel.split(",")):
            m = re.match(r"^\s*(\d*\.?\d+)\s*(px|%)\s*$", v)
            if m: return float(m.group(1)) * (16 / 100 if m.group(2) == "%" else 1)
    return 16.0


# ---------------------------------------------------------------- tokens
def family_of_token(name, value):
    n = name.lstrip("-").lower()
    for fam, rx in FAMILY_OF_NAME:
        if re.search(rx, n): return fam
    if colour(value): return "colour"
    if duration_ms(value) is not None: return "duration"
    if re.match(r"^\s*(?:cubic-bezier|steps|linear\()", value or ""): return "easing"
    if re.search(r"\d(?:px|rem|em)\b.*\d(?:px|rem|em)\b.*(?:rgb|#|hsl|oklch)", value or ""): return "shadow"
    if re.match(r"^\s*-?\d*\.?\d+(?:px|rem|em)\s*$", value or ""): return "length"
    if re.search(r"['\"]|,\s*(?:sans-serif|serif|monospace|system-ui)\b", value or ""): return "font_family"
    return "other"


def tier_of_token(name, value):
    n = name.lower()
    for fw, rx in FRAMEWORK_PREFIX[:1]:
        if re.search(rx, n): return "framework_internal"
    bare = re.sub(r"^--(?:[a-z]{1,6}-)?", "--", n) if re.match(r"^--(?:bs|ant|cds|mui|chakra|mantine|govuk|ds|geist|p|tc)-", n) else n
    if COMPONENT_WORD.search(bare[2:]): return "component"
    if HUE_WORD.search(bare[2:]) and not ROLE_WORD.search(re.sub(HUE_WORD, "-", bare[2:])): return "primitive"
    if ROLE_WORD.search(bare[2:]): return "semantic"
    if NUM_STEP.search(bare): return "primitive"
    if SHIRT.search(bare): return "scale_step"
    return "other"


def inventory(rows, root_tokens, rem):
    decls = collections.defaultdict(list)       # name -> [(scope, theme, selector, value)]
    for ctx, sel, p, v in rows:
        if not p.startswith("--"): continue
        dark = bool(DARK_SEL.search(sel)) or any(DARK_MQ.search(c) for c in ctx)
        light = bool(LIGHT_SEL.search(sel)) or any(LIGHT_MQ.search(c) for c in ctx)
        parts = [s.strip() for s in sel.split(",")]
        bare = [DARK_SEL.sub("", LIGHT_SEL.sub("", s)).strip() or ":root" for s in parts]
        rootish = all(ROOTISH.match(re.sub(r"\s+", "", s)) or s in (":root", "") for s in bare)
        scope = "root" if rootish else "scoped"
        decls[p].append({"scope": scope, "theme": "dark" if dark else "light" if light else "base", "sel": sel[:120],
                         "ctx": [c[:80] for c in ctx], "value": v[:160]})
    names = set(decls) | set(root_tokens)
    rows_out, fams, tiers, scopes = {}, collections.Counter(), collections.Counter(), collections.Counter()
    for name in sorted(names):
        ds = decls.get(name, [])
        base = [d for d in ds if d["theme"] == "base"] or ds
        raw = base[0]["value"] if base else ""
        resolved = root_tokens.get(name, "")
        val = resolved or raw
        fam = family_of_token(name, val if val and "var(" not in val else raw)
        tier = tier_of_token(name, val)
        scope = "root" if any(d["scope"] == "root" for d in ds) or (not ds and name in root_tokens) else "scoped"
        fams[fam] += 1; tiers[tier] += 1; scopes[scope] += 1
        rows_out[name] = {"family": fam, "tier": tier, "scope": scope, "declared": len(ds), "raw": raw[:100], "resolved_on_root": resolved[:100],
                          "alias_of": re.findall(r"var\((--[\w-]+)", raw)[:3], "themes": sorted({d["theme"] for d in ds}),
                          "scoped_selectors": sorted({d["sel"] for d in ds if d["scope"] == "scoped"})[:4]}
    return decls, rows_out, fams, tiers, scopes


def token_pools(tok_rows, rem):
    """Resolved values of declared tokens by family: colour keys and lengths in px."""
    pools = collections.defaultdict(set)
    for name, t in tok_rows.items():
        if t["tier"] == "framework_internal": continue
        for val in (t["resolved_on_root"], t["raw"]):
            if not val or "var(" in val: continue
            c = colour(val)
            if c and t["family"] in ("colour", "other", "shadow"):
                pools["colour"].add(ckey(c)); break
            L = length_px(val, rem)
            if L is not None:
                fam = t["family"] if t["family"] in ("spacing", "font_size", "radius", "line_height", "letter_spacing", "border_width") else "length"
                pools[fam].add(round(L, 2)); break
            d = duration_ms(val)
            if d is not None: pools["duration"].add(round(d)); break
            if t["family"] == "z_index" and re.match(r"^-?\d+$", val.strip()): pools["z_index"].add(int(val)); break
            if t["family"] == "shadow": pools["shadow"].add(re.sub(r"\s+", " ", val.strip())); break
    return pools


# ---------------------------------------------------------------- computed values per family
def exhibits_rx():
    try:
        t = yaml.safe_load((ROOT / "data" / "thresholds.yaml").read_text(encoding="utf-8"))
        return re.compile(t["exhibits"]["pattern"], re.I)
    except (OSError, KeyError, TypeError, re.error): return None


def elements(dom, exrx):
    els = dom.get("elements") or []
    by_id = {str(e["id"]): e for e in els}
    ex_ids, out = set(), []
    for e in els:
        if not e.get("vis"): continue
        if exrx:
            a, hops, hit = e, 0, False
            while a is not None and hops < 12:
                if exrx.search(" ".join(classes(a.get("sel")))): hit = True; break
                a = by_id.get(str(a.get("parent"))); hops += 1
            if hit: ex_ids.add(e["id"]); continue
        out.append(e)
    return out, len(ex_ids)


def counter_rows(cnt, total, fmt=lambda k: k):
    return [{"value": fmt(k), "count": n, "share": round(n / total, 3) if total else 0} for k, n in cnt.most_common(TOP)]


def family_values(els, rem):
    fam = {k: collections.Counter() for k in ("colour_text", "colour_fill", "colour_border", "font_size", "line_height", "letter_spacing",
                                              "spacing", "radius", "shadow", "border_width", "z_index", "duration", "easing", "font_family")}
    examples = collections.defaultdict(dict)
    considered = collections.Counter()
    for e in els:
        st = e.get("style") or {}
        sel = e.get("sel", "")
        has_text = bool(e.get("text"))
        if has_text:
            c = colour(st.get("color"))
            if c and c[3] > 0.02: k = ckey(c); fam["colour_text"][k] += 1; examples["colour_text"].setdefault(k, sel); considered["colour_text"] += 1
            fs = px(st.get("fontSize"))
            if fs:
                k = rnd(fs, 0.5); fam["font_size"][k] += 1; examples["font_size"].setdefault(k, sel); considered["font_size"] += 1
                lh = st.get("lineHeight", "normal")
                lk = "normal" if lh == "normal" else (rnd(px(lh) / fs, 0.05) if px(lh) else None)
                if lk is not None: fam["line_height"][lk] += 1; examples["line_height"].setdefault(lk, sel); considered["line_height"] += 1
                ls = st.get("letterSpacing", "normal")
                lsk = 0.0 if ls == "normal" else (rnd(px(ls) / fs, 0.005) if px(ls) is not None else None)
                if lsk is not None: fam["letter_spacing"][lsk] += 1; examples["letter_spacing"].setdefault(lsk, sel); considered["letter_spacing"] += 1
            ff = st.get("fontFamily")
            if ff: k = base_family(ff.split(",")[0].strip().strip("\"'")); fam["font_family"][k] += 1; considered["font_family"] += 1; examples["font_family"].setdefault(k, ff[:80])
        bg = colour(st.get("backgroundColor"))
        if bg and bg[3] > 0.02: k = ckey(bg); fam["colour_fill"][k] += 1; examples["colour_fill"].setdefault(k, sel); considered["colour_fill"] += 1
        bws = [px(st.get(f"border{s}Width")) or 0 for s in ("Top", "Right", "Bottom", "Left")]
        for s, w in zip(("Top", "Right", "Bottom", "Left"), bws):
            if w > 0:
                fam["border_width"][rnd(w, 0.5)] += 1; considered["border_width"] += 1; examples["border_width"].setdefault(rnd(w, 0.5), sel)
                c = colour(st.get(f"border{s}Color"))
                if c and c[3] > 0.02: k = ckey(c); fam["colour_border"][k] += 1; examples["colour_border"].setdefault(k, sel); considered["colour_border"] += 1
                break
        for k in ("marginTop", "marginBottom", "paddingTop", "paddingBottom", "paddingLeft", "paddingRight", "rowGap", "columnGap"):
            v = st.get(k)
            if not v or v == "normal": continue
            n = px(v)
            if n and abs(n) >= 0.5:
                key = rnd(abs(n), 0.5); fam["spacing"][key] += 1; considered["spacing"] += 1; examples["spacing"].setdefault(key, f"{sel} {k}")
        r = px(st.get("borderTopLeftRadius"))
        if r and r > 0:
            rect = e.get("rect") or {}
            short = min(rect.get("w") or 0, rect.get("h") or 0)
            key = "full" if short and r >= short / 2 - 1 else rnd(r, 0.5)
            fam["radius"][key] += 1; considered["radius"] += 1; examples["radius"].setdefault(key, sel)
        sh = st.get("boxShadow")
        if sh and sh != "none":
            key = re.sub(r"\s+", " ", sh.strip())[:160]; fam["shadow"][key] += 1; considered["shadow"] += 1; examples["shadow"].setdefault(key, sel)
        z = st.get("zIndex")
        if z and z != "auto" and st.get("position") not in (None, "static"):
            try: fam["z_index"][int(z)] += 1; considered["z_index"] += 1; examples["z_index"].setdefault(int(z), sel)
            except ValueError: pass
        if st.get("transitionProperty") not in (None, "none"):
            durs = [duration_ms(x) for x in str(st.get("transitionDuration", "0s")).split(",")]
            eases = [x.strip() for x in re.split(r",(?![^(]*\))", str(st.get("transitionTimingFunction", "")))]
            for i, d in enumerate(durs):
                if d:
                    fam["duration"][round(d)] += 1; considered["duration"] += 1; examples["duration"].setdefault(round(d), sel)
                    ez = eases[i % len(eases)] if eases else ""
                    if ez: fam["easing"][ez] += 1; considered["easing"] += 1; examples["easing"].setdefault(ez, sel)
        if st.get("animationName") not in (None, "none"):
            d = duration_ms(str(st.get("animationDuration", "0s")).split(",")[0])
            if d: fam["duration"][round(d)] += 1; considered["duration"] += 1; examples["duration"].setdefault(round(d), sel + " (animation)")
    return fam, examples, considered


def near_colours(cnt):
    items = [(colour(k.split("/")[0]), n, k) for k, n in cnt.items() if "/" not in k]
    items = [x for x in items if x[0]]
    groups = cluster(items, lambda a, b: cl.oklab_dist(a, b) < NEAR_OKLAB)
    out = []
    for rep, w, members in groups:
        if len(members) > 1:
            out.append({"members": [{"value": m, "count": cnt[m]} for m in members], "count": w,
                        "max_oklab": round(max(cl.oklab_dist(colour(members[0]), colour(m)) for m in members), 4)})
    return sorted(out, key=lambda g: -g["count"])[:15]


def near_numbers(cnt, close):
    vals = sorted(k for k in cnt if isinstance(k, (int, float)))
    out = []
    for a, b in zip(vals, vals[1:]):
        if close(a, b): out.append({"values": [a, b], "counts": [cnt[a], cnt[b]]})
    return out[:15]


def scale_fit_type(cnt):
    sizes = {k: n for k, n in cnt.items() if isinstance(k, (int, float)) and k > 0}
    if len(sizes) < 3: return {"note": f"{len(sizes)} distinct sizes: too few to fit a scale (a page with few sizes is not off-scale)"}
    total = sum(sizes.values())
    base_cands = sorted({16.0, max(sizes, key=sizes.get)})
    best = None
    for R in RATIOS:
        tol = min(0.03, (R - 1) / 4)
        chance = min(1.0, 2 * math.log(1 + tol) / math.log(R))
        for b in base_cands:
            on = sum(n for s, n in sizes.items() if abs(s - b * R ** round(math.log(s / b) / math.log(R))) <= max(0.75, tol * s))
            share = on / total
            cand = {"ratio": R, "base_px": b, "share_on": round(share, 3), "chance_share": round(chance, 3), "excess": round(share - chance, 3),
                    "steps_used": sorted({round(math.log(s / b) / math.log(R)) for s in sizes})}
            if best is None or cand["excess"] > best["excess"]: best = cand
    off = [s for s in sorted(sizes) if abs(s - best["base_px"] * best["ratio"] ** round(math.log(s / best["base_px"]) / math.log(best["ratio"]))) > max(0.75, min(0.03, (best["ratio"] - 1) / 4) * s)]
    tw = sum(n for s, n in sizes.items() if any(abs(s - t) <= 0.5 for t in TW_TEXT)) / total
    return {"best_ratio": best, "off_best_ratio_px": off[:20], "tailwind_scale_share": round(tw, 3)}


def scale_fit_spacing(cnt):
    vals = {k: n for k, n in cnt.items() if isinstance(k, (int, float))}
    total = sum(vals.values())
    if not total: return {"note": "no spacing values"}
    def share(pred): return round(sum(n for v, n in vals.items() if pred(v)) / total, 3)
    on4 = lambda v: abs(v - round(v)) < 0.05 and (round(v) % 4 == 0 or round(v) in (1, 2, 6, 10, 14))
    on8 = lambda v: abs(v - round(v)) < 0.05 and (round(v) % 8 == 0 or round(v) in (1, 2, 4, 12))
    off4 = collections.Counter({v: n for v, n in vals.items() if not on4(v)})
    bases = []
    for b in (4, 5, 6, 8, 10):
        on = share(lambda v, b=b: abs(v - round(v)) < 0.05 and (round(v) % b == 0 or round(v) in (1, 2)))
        chance = round(min(1.0, 1 / b + 0.05), 3)      # a random integer px value lands on base b about 1/b of the time, plus the hairlines
        bases.append({"base_px": b, "share_on": on, "chance_share": chance, "excess": round(on - chance, 3)})
    best = max(bases, key=lambda x: (x["excess"], x["base_px"]))
    return {"share_on_4px": share(on4), "share_on_8px": share(on8), "bases": bases, "best_base": best, "share_fractional": share(lambda v: abs(v - round(v)) >= 0.05),
            "off_4px_values": [{"value": v, "count": n} for v, n in off4.most_common(20)],
            "note": "4px base counts 1, 2, 6, 10 and 14 as hairlines and half-steps, as the off_scale_spacing detector does; 8px counts 1, 2, 4 and 12"}


def ladder(cnt):
    vals = sorted(k for k in cnt if isinstance(k, int))
    return {"values": vals[:40], "max": vals[-1] if vals else None, "over_1000": [v for v in vals if v >= 1000][:20],
            "distinct": len(vals)}


def on_token_share(cnt, pool, tol=0.5, colourish=False):
    if not pool: return None
    total = sum(cnt.values())
    if not total: return None
    if colourish: on = sum(n for k, n in cnt.items() if k.split("/")[0] in pool or k in pool)
    else: on = sum(n for k, n in cnt.items() if isinstance(k, (int, float)) and any(abs(k - p) <= tol for p in pool))
    return round(on / total, 3)


def families_at(dom, exrx, rem, pools, supplied):
    els, n_ex = elements(dom, exrx)
    fam, ex, considered = family_values(els, rem)
    out = {"elements_visible": len(els), "elements_in_exhibits_left_out": n_ex}
    col_all = fam["colour_text"] + fam["colour_fill"] + fam["colour_border"]
    for k, cnt in fam.items():
        tot = considered[k]
        row = {"considered": tot, "distinct": len(cnt), "values": counter_rows(cnt, tot),
               "one_offs": sum(1 for v in cnt.values() if v == 1),
               "examples": {str(v): ex[k][v] for v, _ in cnt.most_common(8) if v in ex[k]}}
        if k.startswith("colour"): row["near_duplicates"] = near_colours(cnt)
        if k == "font_size":
            row["near_duplicates"] = near_numbers(cnt, lambda a, b: b / a < NEAR_SIZE_RATIO)
            row["scale"] = scale_fit_type(cnt)
            row["on_token_share"] = on_token_share(cnt, pools.get("font_size", set()) | pools.get("length", set()))
        if k == "spacing":
            row["near_duplicates"] = near_numbers(cnt, lambda a, b: b - a <= NEAR_SPACE_PX and a >= 3 and (b % 4 == 0 or a % 4 == 0))
            row["scale"] = scale_fit_spacing(cnt)
            sp = pools.get("spacing", set()) | pools.get("length", set())
            row["on_token_share"] = on_token_share(cnt, sp)
        if k == "radius":
            row["on_token_share"] = on_token_share(collections.Counter({a: b for a, b in cnt.items() if a != "full"}), pools.get("radius", set()) | pools.get("length", set()))
        if k == "z_index": row["ladder"] = ladder(cnt)
        if k == "duration": row["on_token_share"] = on_token_share(cnt, pools.get("duration", set()), tol=1)
        if k == "shadow": row["on_token_share"] = on_token_share(cnt, pools.get("shadow", set()), colourish=True) if pools.get("shadow") else None
        out[k] = row
    out["colour_all"] = {"considered": sum(col_all.values()), "distinct": len(col_all), "opaque_distinct": sum(1 for k in col_all if "/" not in k),
                         "near_duplicates": near_colours(col_all), "on_token_share": on_token_share(col_all, pools.get("colour", set()), colourish=True)}
    if supplied:
        out["supplied_system"] = drift_from(supplied, fam, col_all)
    return out


# ---------------------------------------------------------------- stylesheet declarations: literal vs var()
def declarations(rows, pools, rem, tok_names):
    per = collections.defaultdict(collections.Counter)
    retyped = collections.defaultdict(list)
    arbitrary_sels = collections.Counter()
    refs = collections.Counter()
    alias_refs = collections.Counter()
    undeclared = collections.Counter()
    undeclared_nofb = collections.Counter()
    lit_colours = collections.Counter()
    for ctx, sel, p, v in rows:
        for m in re.finditer(r"var\(\s*(--[\w-]+)\s*(,)?", v):
            name = m.group(1)
            (alias_refs if p.startswith("--") else refs)[name] += 1
            if name not in tok_names:
                undeclared[name] += 1
                if not m.group(2): undeclared_nofb[name] += 1
        if p.startswith("--"): continue
        fam = FAMILY_OF_PROP.get(p)
        if fam is None:
            if p in ("border", "border-top", "border-bottom", "border-left", "border-right", "outline"): fam = "colour"
            elif p in ("transition", "animation"): fam = "duration"
            else: continue
        arb = arbitrary(sel) and "var(--" not in v
        if arb: arbitrary_sels[sel[:80]] += 1
        vl = v.strip().lower()
        if "var(--" in vl: kind = "var"
        elif vl in NEUTRAL_KW or re.fullmatch(r"(?:0(?:px)?\s*){1,4}", vl): kind = "keyword"
        elif fam == "colour" and p in ("background", "border", "border-top", "border-bottom", "border-left", "border-right", "outline") and not cl.colors_in(vl) and not re.search(r"#[0-9a-f]{3,8}|hsla?\(", vl): continue
        elif sel and all(UTILITY_SEL.match(s.strip()) for s in sel.split(",")): kind = "utility_literal"
        else: kind = "literal"
        if arb: kind = "arbitrary_utility"
        per[fam][kind] += 1
        if kind in ("literal", "arbitrary_utility"):
            if fam == "colour":
                for c in ([colour(vl)] if colour(vl) else cl.colors_in(vl)):
                    if not c or c[3] < 0.02: continue
                    k = ckey(c); lit_colours[k] += 1
                    if k in pools.get("colour", set()) and len(retyped["colour"]) < 400: retyped["colour"].append((sel[:80], p, k))
            elif fam in ("spacing", "font_size", "radius"):
                for part in vl.split():
                    L = length_px(part, rem)
                    if L and (L in pools.get(fam, set()) or L in pools.get("length", set())) and len(retyped[fam]) < 400:
                        retyped[fam].append((sel[:80], p, round(L, 2)))
    usage = {}
    for fam, c in sorted(per.items()):
        tot = sum(c.values()) - c["keyword"]
        usage[fam] = {"var": c["var"], "literal": c["literal"], "utility_literal": c["utility_literal"], "arbitrary_utility": c["arbitrary_utility"],
                      "keyword": c["keyword"], "var_share_of_non_keyword": round(c["var"] / tot, 3) if tot else None,
                      "literal_share_of_non_keyword": round(c["literal"] / tot, 3) if tot else None}
    ret = {f: {"count": len(l), "samples": [{"sel": s, "prop": p, "value": v} for s, p, v in l[:8]]} for f, l in retyped.items()}
    return usage, ret, arbitrary_sels, refs, alias_refs, undeclared, undeclared_nofb, lit_colours


# ---------------------------------------------------------------- theme parity
def theme_parity(decls, tok_rows, rows):
    # the light side: tokens on :root outside any theme, plus those a light class or media query sets ([data-theme=light])
    base = {n for n, ds in decls.items() if any((d["theme"] == "base" and d["scope"] == "root") or d["theme"] == "light" for d in ds)}
    dark_mq = {n for n, ds in decls.items() if any(d["theme"] == "dark" and any(DARK_MQ.search(c) for c in d["ctx"]) for d in ds)}
    dark_cls = {n for n, ds in decls.items() if any(d["theme"] == "dark" and DARK_SEL.search(d["sel"]) for d in ds)}
    light_cls = {n for n, ds in decls.items() if any(d["theme"] == "light" for d in ds)}
    dark = dark_mq | dark_cls
    base_colour = {n for n in base if tok_rows.get(n, {}).get("family") == "colour" and tok_rows[n]["tier"] != "framework_internal"}
    sem_colour = {n for n in base_colour if tok_rows[n]["tier"] in ("semantic", "component", "other")}
    dark_sel_groups = collections.Counter()
    for n, ds in decls.items():
        for d in ds:
            if d["theme"] == "dark":
                m = DARK_SEL.search(d["sel"])
                dark_sel_groups[m.group(0) if m else "@media (prefers-color-scheme: dark)"] += 1
    alt = collections.Counter()
    for ctx, sel, p, v in rows:
        if p.startswith("--"):
            for m in THEME_ATTR.finditer(sel):
                if not re.search(r"dark|light", m.group(1), re.I): alt[m.group(1)] += 1
    lit_dark, var_dark, samples = 0, 0, []
    for ctx, sel, p, v in rows:
        if p.startswith("--") or FAMILY_OF_PROP.get(p) != "colour": continue
        if not (DARK_SEL.search(sel) or any(DARK_MQ.search(c) for c in ctx)): continue
        if any(re.search(r"forced-colors", c) for c in ctx): continue
        if "var(--" in v: var_dark += 1
        elif colour(v) or cl.colors_in(v):
            lit_dark += 1
            if len(samples) < 6: samples.append({"sel": sel[:80], "prop": p, "value": v[:60]})
    schemes = sorted({v.strip() for ctx, sel, p, v in rows if p == "color-scheme"})[:8]
    return {"base_root_tokens": len(base), "base_colour_tokens": len(base_colour), "base_semantic_colour_tokens": len(sem_colour),
            "dark_tokens_media_query": len(dark_mq), "dark_tokens_class_or_attr": len(dark_cls), "light_tokens_class_or_attr": len(light_cls),
            "dark_mechanisms": [k for k, v in (("media_query", dark_mq), ("class_or_attr", dark_cls)) if v],
            "dark_selectors": [{"selector": k, "declarations": v} for k, v in dark_sel_groups.most_common(8)],
            "dark_redefines_base": len(dark & base), "dark_only_names": sorted(dark - base)[:30],
            "semantic_colour_redefined_share": round(len(sem_colour & dark) / len(sem_colour), 3) if sem_colour and dark else None,
            "semantic_colour_not_redefined": sorted(sem_colour - dark)[:40] if dark else [],
            "media_query_and_class_mirror": {"in_both": len(dark_mq & dark_cls), "only_media_query": len(dark_mq - dark_cls), "only_class": len(dark_cls - dark_mq)} if dark_mq and dark_cls else None,
            "dark_rules_colour_declarations": {"var": var_dark, "literal": lit_dark, "literal_samples": samples},
            "color_scheme_values": schemes, "alternate_theme_attrs": [{"theme": k, "declarations": v} for k, v in alt.most_common(8)],
            "note": "the capture renders one colour scheme; the other theme is read from the stylesheet only, never seen or measured"}


# ---------------------------------------------------------------- framework fingerprints
def fingerprints(tok_rows, refs, doms, rows):
    out = {}
    names = set(tok_rows) | set(refs)
    for fw, rx in FRAMEWORK_PREFIX:
        r = re.compile(rx)
        n = sum(1 for x in names if r.search(x))
        # short or generic names (--p, --gray-3, --size-2) also occur outside the framework: ask for more of them
        if n >= (6 if fw in ("radix", "open_props", "daisyui", "primer", "shopify_polaris", "fluent", "framer") else 2): out[fw] = {"tokens_or_refs": n}
    sh = SHADCN & names
    if len(sh) >= 8: out["shadcn_roles"] = {"present": len(sh), "of": len(SHADCN), "missing": sorted(SHADCN - names)}
    v4 = sum(1 for x in names if TW_V4_THEME.match(x))
    layer_theme = any(any(c.lower().startswith("@layer theme") for c in ctx) for ctx, sel, p, v in rows[:20000])
    if v4 >= 5 or layer_theme: out["tailwind_v4_theme"] = {"theme_tokens": v4, "layer_theme": layer_theme}
    cls_hits = collections.Counter(); arb_cls = collections.Counter(); seen = set()
    for w, d in doms.items():
        for e in d.get("elements") or []:
            for c in classes(e.get("sel")):
                if (c in seen): continue
                seen.add(c)
                for fw, rx in CLASS_PRINTS:
                    if rx.search(c): cls_hits[fw] += 1; break
                if arbitrary(c, escaped=False): arb_cls[c] += 1
    for fw, n in cls_hits.items():
        out.setdefault(fw, {})["distinct_class_names"] = n
    if arb_cls:
        out.setdefault("tailwind", {})["arbitrary_value_classes"] = {"distinct": len(arb_cls), "samples": sorted(arb_cls)[:20]}
    return out


# ---------------------------------------------------------------- supplied system
def read_supplied(path, rem):
    p = pathlib.Path(path)
    vals = {}
    try: text = p.read_text(encoding="utf-8")
    except OSError: return {"error": f"could not read {p}"}
    if p.suffix.lower() == ".json":
        try: data = json.loads(text)
        except ValueError: return {"error": f"{p} is not JSON"}
        def rec(node, pre):
            if isinstance(node, dict):
                if "$value" in node or "value" in node and not isinstance(node.get("value"), dict):
                    vals["--" + "-".join(pre)] = str(node.get("$value", node.get("value"))); return
                for k, v in node.items():
                    if not k.startswith("$"): rec(v, pre + [k])
            elif isinstance(node, (str, int, float)): vals["--" + "-".join(pre)] = str(node)
        rec(data, [])
    else:
        for ctx, sel, prop, v in walk(text, stats=collections.Counter(), out=[]):
            if prop.startswith("--"): vals.setdefault(prop, v)
    pools = collections.defaultdict(set)
    for n, v in vals.items():
        c = colour(v)
        if c: pools["colour"].add(ckey(c)); continue
        L = length_px(v, rem)
        if L is not None: pools["length"].add(round(L, 2)); continue
        d = duration_ms(v)
        if d is not None: pools["duration"].add(round(d))
    return {"file": str(p), "tokens": len(vals), "pools": {k: sorted(v, key=str)[:200] for k, v in pools.items()}, "_pools": pools}


def drift_from(supplied, fam, col_all):
    pools = supplied.get("_pools") or {}
    out = {}
    if pools.get("colour"):
        off = collections.Counter({k: n for k, n in col_all.items() if k.split("/")[0] not in pools["colour"] and k not in pools["colour"]})
        tot = sum(col_all.values())
        out["colour"] = {"share_on_system": round(1 - sum(off.values()) / tot, 3) if tot else None,
                         "off_system": [{"value": k, "count": n, "nearest_system": nearest_colour(k, pools["colour"])} for k, n in off.most_common(15)]}
    if pools.get("length"):
        for k in ("spacing", "font_size", "radius"):
            cnt = collections.Counter({a: b for a, b in fam[k].items() if isinstance(a, (int, float))})
            tot = sum(cnt.values())
            off = collections.Counter({a: b for a, b in cnt.items() if not any(abs(a - p) <= 0.5 for p in pools["length"])})
            out[k] = {"share_on_system": round(1 - sum(off.values()) / tot, 3) if tot else None, "off_system": [{"value": a, "count": b} for a, b in off.most_common(15)]}
    if pools.get("duration"):
        cnt = fam["duration"]; tot = sum(cnt.values())
        off = collections.Counter({a: b for a, b in cnt.items() if a not in pools["duration"]})
        out["duration"] = {"share_on_system": round(1 - sum(off.values()) / tot, 3) if tot else None, "off_system": [{"value": a, "count": b} for a, b in off.most_common(10)]}
    return out


def nearest_colour(k, pool):
    c = colour(k.split("/")[0])
    if not c: return None
    best = min(((cl.oklab_dist(c, colour(p)), p) for p in pool if colour(p)), default=None)
    return {"value": best[1], "oklab": round(best[0], 4)} if best else None


# ---------------------------------------------------------------- sweep
def sweep_hits(run):
    mech = load(run / "02-mechanical.json") or {}
    dets = mech.get("detectors") or {}
    out = {}
    for k in SWEEP:
        d = dets.get(k)
        if not d: out[k] = {"status": "absent"}; continue
        out[k] = {"status": d.get("status"), "rule": d.get("rule"), "note": d.get("reason") or d.get("note"),
                  "hits": [{"where": str(h.get("where"))[:120], "evidence": str(h.get("evidence"))[:220], "tier": h.get("tier")} for h in (d.get("hits") or [])[:6]]}
    return out, (mech.get("summary") or {}).get("exhibits")


# ---------------------------------------------------------------- main
def table(run, out, system=None):
    ev = run / "01-evidence"
    man = load(ev / "manifest.json") or {}
    doms = {}
    for p in sorted(ev.glob("dom-*.json")):
        m = re.match(r"dom-(\d+)\.json$", p.name)
        if m:
            d = load(p)
            if d: doms[int(m.group(1))] = d
    out.mkdir(parents=True, exist_ok=True)
    net = man.get("network") or {}
    res = {"run": str(run), "widths": sorted(doms), "network": {"mode": net.get("mode"), "blocked": len(net.get("blocked", []))}}
    if not doms:
        res["note"] = ("no dom-<w>.json in 01-evidence: nothing was measured. On an image-only item, judge by eye only what a picture shows "
                       "(how many distinct colours, sizes, radii and spacings it uses, and whether they repeat), and write the stylesheet rows as not investigated.")
        res["files"] = sorted(p.name for p in ev.glob("*")) if ev.is_dir() else []
        (out / "tokens-table.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
        return res
    ref_w = 1440 if 1440 in doms else max(doms)
    dom = doms[ref_w]
    css = dom.get("css") or []
    unreadable = [c for c in css if c.startswith("/* unreadable")]
    stats = collections.Counter()
    rows = walk("\n".join(c for c in css if not c.startswith("/* unreadable")), out=[], stats=stats)
    rem = root_font_px(rows)
    root_tokens = dom.get("tokens") or {}
    decls, tok_rows, fams, tiers, scopes = inventory(rows, root_tokens, rem)
    pools = token_pools(tok_rows, rem)
    supplied = read_supplied(system, rem) if system else None
    usage, retyped, arbitrary_sels, refs, alias_refs, undeclared, undeclared_nofb, lit_colours = declarations(rows, pools, rem, set(tok_rows))
    used_names = set(refs) | set(alias_refs)
    own = {n: t for n, t in tok_rows.items() if t["tier"] != "framework_internal"}
    never = sorted(n for n in own if n not in used_names)
    placeholder = sorted(n for n, t in tok_rows.items() if PLACEHOLDER_VAL.match((t["raw"] or "").strip()))
    res["stylesheet"] = {"rules_listed": len(css), "unreadable_sheets": len(unreadable), "unreadable": [u[:120] for u in unreadable[:6]],
                         "style_rules": stats["style_rules"], "declarations": len(rows), "root_font_px": rem,
                         "note": None if not unreadable else "cross-origin sheets could not be read: their tokens and declarations are unknown, not absent",
                         "verified": bool(rows)}
    fam_counts = collections.Counter(t["family"] for t in own.values())
    tier_counts = collections.Counter(t["tier"] for t in own.values())
    aliases = {n: t["alias_of"] for n, t in own.items() if t["alias_of"]}
    sem_alias_prim = sum(1 for n, a in aliases.items() if own[n]["tier"] in ("semantic", "component") and any(tok_rows.get(x, {}).get("tier") == "primitive" for x in a))
    comp_to_prim = sorted(n for n, a in aliases.items() if own[n]["tier"] == "component" and any(tok_rows.get(x, {}).get("tier") == "primitive" for x in a))[:15]
    lit_in_comp = sorted(n for n, t in own.items() if t["tier"] in ("component",) and t["family"] == "colour" and not t["alias_of"])[:15]
    res["tokens"] = {
        "declared": len(tok_rows), "own": len(own), "framework_internal": len(tok_rows) - len(own),
        "by_scope": dict(collections.Counter(t["scope"] for t in own.values())), "by_family": dict(fam_counts.most_common()), "by_tier_guess": dict(tier_counts.most_common()),
        "aliases": len(aliases), "semantic_or_component_aliasing_a_primitive": sem_alias_prim,
        "component_tokens_pointing_at_primitives": comp_to_prim, "component_colour_tokens_with_literal_values": lit_in_comp,
        "referenced_by_declarations": len([n for n in refs if n in tok_rows]), "var_references": sum(refs.values()),
        "alias_references": sum(alias_refs.values()), "own_tokens_never_referenced": {"count": len(never), "sample": never[:25]},
        "undeclared_references": {"count": len(undeclared), "without_fallback": [{"name": n, "uses": c} for n, c in undeclared_nofb.most_common(15)],
                                  "note": "names referenced but declared in no readable sheet: from an unreadable sheet, script or an inline style, or a real typo"},
        "placeholder_values": placeholder,
        "most_referenced": [{"name": n, "uses": c, "family": tok_rows.get(n, {}).get("family"), "tier": tok_rows.get(n, {}).get("tier")} for n, c in refs.most_common(20)],
        "naming_samples": {t: sorted(n for n, r in own.items() if r["tier"] == t)[:12] for t in ("primitive", "semantic", "component", "scale_step", "other")},
        "pools": {k: len(v) for k, v in pools.items()},
        "note": "tier is guessed from the name: a hue word or a numbered step is a primitive, a role word semantic, a component word component; read the samples",
    }
    res["declarations"] = {"by_family": usage, "literal_retypes_a_token_value": retyped,
                           "distinct_literal_colours": len(lit_colours), "literal_colours_top": [{"value": k, "count": n} for k, n in lit_colours.most_common(15)],
                           "arbitrary_value_selectors": {"distinct": len(arbitrary_sels), "samples": [s for s, _ in arbitrary_sels.most_common(12)]},
                           "note": "utility_literal: a framework utility rule (.p-4, .text-sm) whose literal value is the framework's own scale step; arbitrary_utility: a bracketed one-off (text-[15px])"}
    res["theme"] = theme_parity(decls, tok_rows, rows)
    res["frameworks"] = fingerprints(tok_rows, refs, doms, rows)
    res["values"] = {str(w): families_at(doms[w], exhibits_rx(), rem, pools, supplied) for w in sorted(doms)}
    if supplied: res["supplied_system"] = {k: v for k, v in supplied.items() if k != "_pools"}
    res["sweep"], res["sweep_exhibits"] = sweep_hits(run)
    res["not_captured"] = ["inline style attributes", "margin-left and margin-right", "which rule set each computed value",
                           "the second colour scheme (read from the stylesheet only)", "tokens in unreadable cross-origin sheets",
                           "token source files (only the shipped CSS is read)"]
    (out / "tokens-table.json").write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    return res


def summary(res):
    if "values" not in res: print(res.get("note")); return
    t, s, th = res["tokens"], res["stylesheet"], res["theme"]
    v = res["values"].get("1440") or next(iter(res["values"].values()))
    fs, sp = v["font_size"], v["spacing"]
    br = (fs.get("scale") or {}).get("best_ratio") or {}
    dv = res["declarations"]["by_family"]
    def vs(f): return f"{(dv.get(f) or {}).get('var_share_of_non_keyword')}"
    print(f"tokens {t['own']} own ({t['framework_internal']} framework-internal), scopes {t['by_scope']}, tiers {t['by_tier_guess']}, "
          f"refs {t['var_references']}, never used {t['own_tokens_never_referenced']['count']}, undeclared {t['undeclared_references']['count']}")
    print(f"sheets: {s['declarations']} declarations, {s['unreadable_sheets']} unreadable; var share colour {vs('colour')} spacing {vs('spacing')} "
          f"font_size {vs('font_size')} radius {vs('radius')}; frameworks {sorted(res['frameworks'])}")
    print(f"@{res['widths'][-1] if '1440' not in res['values'] else 1440}: colours {v['colour_all']['distinct']} (near-dup groups {len(v['colour_all']['near_duplicates'])}, on token {v['colour_all']['on_token_share']}), "
          f"sizes {fs['distinct']} (ratio {br.get('ratio')} on {br.get('share_on')} vs chance {br.get('chance_share')}), spacing {sp['distinct']} "
          f"(4px {sp['scale'].get('share_on_4px')}, best base {(sp['scale'].get('best_base') or {}).get('base_px')}), radii {v['radius']['distinct']}, shadows {v['shadow']['distinct']}, z {v['z_index']['distinct']}, durations {v['duration']['distinct']}")
    print(f"theme: dark {th['dark_mechanisms'] or 'none'}, base colour tokens {th['base_colour_tokens']}, semantic redefined {th['semantic_colour_redefined_share']}, "
          f"literal colours in dark rules {th['dark_rules_colour_declarations']['literal']}")


def main(argv):
    if not argv or argv[0].startswith("--"): print(__doc__); return 2
    run = pathlib.Path(argv[0]).resolve()
    if not run.is_dir(): print(f"run folder not found: {run}"); return 2
    out = run / "03-lenses" / "tokens"
    if "--out" in argv: out = pathlib.Path(argv[argv.index("--out") + 1]).resolve()
    system = argv[argv.index("--system") + 1] if "--system" in argv else None
    ev = (run / "01-evidence").resolve()
    if out == ev or ev in out.parents:
        print("refusing to write into 01-evidence/"); return 2
    res = table(run, out, system)
    summary(res)
    print(f"wrote {out / 'tokens-table.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
