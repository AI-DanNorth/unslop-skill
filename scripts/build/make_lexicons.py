"""Generate data/lexicons/*.yaml from the consolidated lists in research/mining/A (appendix).
Re-run after editing the lists below. Every entry carries `added` so stale tells can be reviewed yearly."""
import yaml, pathlib, re
OUT = pathlib.Path(__file__).resolve().parents[2] / "data" / "lexicons"
OUT.mkdir(parents=True, exist_ok=True)
ADDED = "2026-11-08"

def split(s): return [t.strip() for t in s.split(",") if t.strip()]

def write(name, meta, groups):
    doc = {"lexicon": name, **meta, "groups": []}
    for g in groups:
        entries = [{"term": t, "added": ADDED} for t in g.pop("terms")]
        doc["groups"].append({**g, "entries": entries})
    (OUT / f"{name}.yaml").write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=120))

COMMON = {"match": "word, case-insensitive, any inflection", "scope": ["visible text", "alt", "title", "meta description"]}

write("buzzwords", {**COMMON, "rule": "CPY-005", "sources": ["taste-skill §37 §40 §42", "hallmark §106 §356", "kami §224 §236 §238 §303", "agent-skills §119-122"]}, [
 {"name": "slop-words", "policy": "fail", "note": "unless a literal trade use", "terms": split("delve, tapestry, testament to, realm, embark, beacon, multifaceted, paradigm, myriad, plethora, meticulous, intricate, interplay, garner, elevate, unlock, unleash, empower, harness, supercharge, turbocharge, seamless, effortless, cutting-edge, revolutionary, revolutionize, revolutionise, transformative, holistic, next-level, world-class, best-in-class, game-changer, game-changing, state-of-the-art, bespoke, synergy, leverage, reimagine, next-generation, next-gen, unparalleled, unrivaled, unrivalled, streamline, industry-leading, mission-critical, future-proof, enterprise-grade, one-stop solution, nestled")},
 {"name": "weak-intensifiers", "policy": "cap", "budget": 3, "terms": split("powerful, robust, very, just, really, simply, significantly, easy, simple, quick")},
 {"name": "virtue-words", "policy": "cap", "budget": 2, "terms": split("honest, honestly, calm, calmly, quiet, quietly, actually, genuine, genuinely, truly, thoughtful, thoughtfully, carefully, intentional, intentionally, steady, dependable")},
 {"name": "puffery", "policy": "fail", "terms": split("serves as, stands as, pivotal, crucial, plays a key role, plays a vital role, in the heart of, as seen in, the world of")},
 {"name": "dead-metaphors", "policy": "context", "note": "fail unless literal (journey on a travel site) or the audience is fluent", "terms": split("landscape, ecosystem, journey, hub, flywheel, closed loop")},
])

write("stock-phrases", {"match": "phrase, case-insensitive, regex allowed", "rule": "CPY-005", "sources": ["taste-skill §38-40", "hallmark §106 §357", "kami §238 §298 §303", "agent-skills §124 §129"]}, [
 {"name": "openers", "policy": "fail", "terms": [r"in today's (fast-paced|digital|modern|ever-changing|busy|rapidly evolving)", "in today's landscape", "built for the modern team", r"whether you're (a|an)\b", r"unlock the (power|potential)", "harness the power", r"the future of \w+ is (here|now)", "say goodbye to", "look no further", r"join (thousands|millions|hundreds) of", r"trusted by (teams|businesses|companies|brands|people) (worldwide|everywhere|around the world)", "quietly trusted by", "imagine a world", r"ready to (transform|take your|elevate|level up)", "ever-evolving", "one-stop shop", "to the next level", r"(it's|this is|we're) not just an?\b", r"not only .{1,60} but also", "here's the thing", "let that sink in", "let's dive in", r"it's (important|worth) (to note|noting)", r"(in|with) just a few clicks", "we've got you covered", "the possibilities are endless", "at your fingertips", r"\w+ made (simple|easy)", "everything you need to", "all in one place", "enter your email below", "made with ♥", "made with <3", "this means that"]},
 {"name": "not-x-but-y", "policy": "cap", "budget": 1, "terms": [r"\bit'?s not (just )?[^.,;]{1,40}[,;—-] it'?s\b", r"\bnot [^.,;]{1,30}\. (it'?s|just)\b"]},
 {"name": "staged-reveals", "policy": "fail", "terms": ["the result?", "why does this matter?", r"one thing changed:", "this section shows", "below, you'll find", r"here are \d+ reasons", "we've added"]},
 {"name": "chat-residue", "policy": "fail", "terms": ["certainly!", "i hope this helps", "as an ai", "great question!"]},
 {"name": "suspect", "policy": "info", "terms": ["all rights reserved", "no credit card required"]},
])

write("default-names", {"match": "case-sensitive whole name", "rule": "INT-002", "policy_note": "fail as real people or as the page's own brand; allowed only inside an obvious product-UI sample", "sources": ["hallmark §110 §354-355", "taste-skill §35 §43-44"]}, [
 {"name": "placeholder-people", "policy": "fail", "terms": split("Jane Doe, John Smith, John Doe, Example User")},
 {"name": "default-cast", "policy": "cap", "budget": 0, "note": "model's default first names; flag when used for testimonials or team members", "terms": split("Priya, Okafor, Raman, Natarajan, Sarah J., Elara, Aisha, Lena M., Marcus, Dana, Tomas, Nora, Mara, Theo, Isla, Maya, Ines, Jess")},
 {"name": "fake-brands", "policy": "fail", "terms": split("Acme, Nexus, Fieldnote, Kestrel, Halcyon, Brightloop, Northwind, Lumen, Nimbus, Zenith, Apex, Vertex")},
 {"name": "fake-specifics", "policy": "fail", "terms": ["Batch No. 047", "Room 9, 6:12 a.m.", "Field study no. 12", "Example Kitchen"]},
])

write("button-labels", {"match": "whole accessible name of a link or button, case-insensitive", "rule": "CPY-005", "sources": ["taste-skill §45", "hallmark §106 §107 §361 §365", "agent-skills §164-165", "web-interface-guidelines"]}, [
 {"name": "empty-labels", "policy": "fail", "terms": split("learn more, read more, view more, show more, discover, discover more, explore, explore more, more, find out more, see more, click here, more info, details, begin, go, here, link, mehr erfahren, weitere infos")},
 {"name": "stock-second-action", "policy": "info", "note": "a finding when it is the hero's second action", "terms": split("see how it works, watch demo, get started, book a demo")},
 {"name": "arrow-suffix", "policy": "cap", "budget": 1, "match": "label ends with", "terms": ["→", "->", "›", "»", "⟶"]},
])

write("invented-metrics", {"match": "regex over visible text", "rule": "INT-001", "tier": "Floor", "policy_note": "a finding unless the contract lists the figure with unit and source", "sources": ["hallmark §362", "taste-skill §40 §43", "huashu §60", "kami §299"]}, [
 {"name": "multipliers", "policy": "fail", "terms": [r"\b\d+(\.\d+)?x (faster|better|more|cheaper|quicker)\b"]},
 {"name": "social-proof-counts", "policy": "fail", "terms": [r"\btrusted by [\d,.]+\+?", r"\b[\d,.]+\+ (happy )?(customers|teams|users|developers|companies|businesses)\b"]},
 {"name": "percent-claims", "policy": "fail", "terms": [r"\b\d{2}(\.\d+)?% (faster|fewer|more|less|uptime|satisfied|conversion|revenue|cheaper)\b", r"\b99\.9+% uptime\b", r"\+\d+% (conversion|revenue|growth)\b"]},
 {"name": "time-savings", "policy": "fail", "terms": [r"\bsaves? \d+ (hours|minutes|days)\b"]},
 {"name": "uncited-decimal", "policy": "info", "terms": [r"\b\d{1,2}\.\d%"]},
])

write("self-labels", {"match": "phrase in captions, alt text and visible text", "rule": "CPY-005", "sources": ["taste-skill §34 §39", "hallmark §112", "huashu §71", "kami §452 §654"]}, [
 {"name": "medium-descriptions", "policy": "fail", "scope": ["alt", "figcaption"], "terms": split("image of, picture of, photo of, pictured, view of, rendering, render of, made in code, made with code, this photo shows, for illustration, illustrative, stock photo")},
 {"name": "residue", "policy": "fail", "tier": "Floor", "note": "shipped placeholder text", "terms": ["lorem ipsum", "placeholder", "TODO", "your name here", "Title Text", "your screenshot here", "to be added", r"\[(company|brand|business|product) name\]", r"\[insert", r"\[NEED", r"\{\{[^}]+\}\}", r"\(sample\)", r"\(example\)"]},
 {"name": "figure-numbers-in-ui", "policy": "info", "terms": [r"\bfig(\.|ure) \d+\b"]},
])

write("fonts", {"match": "resolved font-family of rendered text (not the declared stack)", "rule": "TYP-003", "sources": ["hallmark §291 §292 §386 §390", "huashu §61 §67 §125 §210", "taste-skill §30"]}, [
 {"name": "banned-as-display", "policy": "fail", "applies_to": "display (>= 32px or h1-h2)", "terms": split("Inter, Roboto, Open Sans, Poppins, Lato, Arial, Helvetica, Helvetica Neue, Segoe UI, system-ui, -apple-system, Source Sans, Nunito, Montserrat, Raleway, Work Sans, DM Sans, Plus Jakarta Sans")},
 {"name": "saturated", "policy": "info", "note": "counts toward a look-family cluster; needs an argument in the contract", "terms": split("Playfair Display, Cormorant, Cormorant Garamond, DM Serif Display, Fraunces, Instrument Serif, Recoleta, Space Grotesk, Hubot Sans, Bebas Neue, Unbounded, Geist, Instrument Sans, Mona Sans, Gloock, Newsreader, Canela")},
 {"name": "never-specify-paid", "policy": "fail", "note": "paid faces cannot ship unlicensed", "terms": split("Söhne, Circular")},
], )
# substitutes as a separate map
(OUT / "fonts.yaml").write_text((OUT / "fonts.yaml").read_text() + yaml.safe_dump({"substitutes": {
  "Fraunces": ["Newsreader", "Libre Caslon Text"], "Inter (display)": ["Archivo", "Anton", "Schibsted Grotesk"],
  "Space Grotesk": ["Schibsted Grotesk", "Familjen Grotesk"], "Playfair Display": ["Cormorant", "DM Serif Display"]}}, sort_keys=False, allow_unicode=True))

write("swatches", {"match": "computed colour of tokens (custom properties) and large fills, case-insensitive hex", "rule": "CLR-002", "sources": ["hallmark §371 §386-387 §408", "kami §688", "huashu §58-60 §68 §213 §215", "taste-skill §31"]}, [
 {"name": "tailwind-defaults", "policy": "fail", "note": "as brand tokens", "terms": split("#0f172a, #1e293b, #64748b, #f8fafc, #6366f1, #8b5cf6, #3b82f6, #06b6d4, #6b7280, #9ca3af, #d1d5db, #e5e7eb, #f3f4f6, #4b5563, #374151, #1f2937, #111827")},
 {"name": "bootstrap-neutrals", "policy": "fail", "note": "as brand tokens", "terms": split("#f8f9fa, #e9ecef, #dee2e6, #ced4da, #adb5bd, #6c757d, #495057, #343a40, #212529")},
 {"name": "pure", "policy": "info", "note": "flag when undocumented (C09)", "terms": split("#000000, #ffffff, #0b0b0b, #111111")},
 {"name": "ai-look-anchors", "policy": "info", "note": "count toward look families", "terms": split("#f4f1ea, #f5f0e8, #f6efe6, #d97757, #cc785c, #0d1117, #0066ff, #39ff14, #5b5bd6, #7c7cff")},
])

write("fake-people", {"match": "substring of img/src, srcset, CSS url()", "rule": "INT-003", "tier": "Floor", "sources": ["hallmark §389 §465 §467"]}, [
 {"name": "avatar-services", "policy": "fail", "terms": split("pravatar, dicebear, randomuser, thispersondoesnotexist, ui-avatars")},
 {"name": "placeholder-services", "policy": "fail", "terms": split("placehold.co, via.placeholder.com, placeholder.com, dummyimage.com, picsum.photos, source.unsplash.com")},
 {"name": "hotlinked-stock", "policy": "fail", "note": "hotlinking breaks licence and performance; self-host", "terms": split("images.unsplash.com, images.pexels.com, cdn.pixabay.com, plus.unsplash.com")},
])

write("fake-success", {"match": "text that appears after submitting a form that made no network request", "rule": "INT-004", "tier": "Floor", "sources": ["hallmark §93 §364 §510"]}, [
 {"name": "success-strings", "policy": "fail", "terms": split("Sent, Thanks, Thank you, Reserved, Booked, You're on the list, Subscribed, Confirmed, All set, You're in, Success")},
])
(OUT / "fake-success.yaml").write_text((OUT / "fake-success.yaml").read_text() + yaml.safe_dump({"honest_replacements": [
  "Nothing was sent: this form is not connected yet.", "That address looks incomplete. Write it as name@example.com.", "That did not go through. Try again in a minute."]}, sort_keys=False, allow_unicode=True))

write("chrome-glyphs", {"match": "regex over visible text runs", "rule": "SLP-010", "sources": ["hallmark §125 §365-366", "huashu §59-60 §67", "taste-skill §22"]}, [
 {"name": "middot-chains", "policy": "cap", "budget": 1, "note": "a run with two or more ' · ' joins", "terms": [r"\S+ · \S+[^·]* · \S+"]},
 {"name": "dash-labels", "policy": "cap", "budget": 0, "terms": [r"^[A-Z]{1,20} [—–-] \S"]},
 {"name": "numbering-tokens", "policy": "cap", "budget": 2, "terms": [r"^0\d\b", r"^\d{2,3} [·/] ", r"^00 / INDEX"]},
 {"name": "fake-versions", "policy": "cap", "budget": 0, "note": "decorative only; real changelogs exempt", "terms": [r"\bv\d+\.\d+(\.\d+)?\b", r"\bBuild \d{3,}\b", r"^BETA$", "INVITE-ONLY PREVIEW"]},
 {"name": "scroll-cues", "policy": "fail", "terms": ["scroll to explore", r"^↓ ?scroll$", r"^scroll$"]},
 {"name": "emoji-bullets", "policy": "cap", "budget": 0, "terms": [r"^[🚀⚡✨🎯💡✅]"]},
])

write("cliche-imagery", {"match": "alt text, filenames, image prompts, and vision review", "rule": "IMG-001", "sources": ["huashu §60", "taste-skill §23 §24 §36", "hallmark §373"]}, [
 {"name": "ai-cliche", "policy": "fail", "terms": split("gradient sphere, digital rain, circuit board, robot face, 3d blob, glowing particles, data stream, holographic hud, aurora, mesh gradient, blurred orb")},
 {"name": "stock-cliche", "policy": "fail", "terms": split("people at screens, handshake, latte art, coffee beans, croissant and cappuccino, made bed, flour thrown")},
 {"name": "mood-stock", "policy": "info", "terms": split("curtain, plant shadows, sky, grass, forest, fog, waterfall")},
])
print(sorted(p.name for p in OUT.glob("*.yaml")))
