"""CSS custom properties and a JSON token file, in Harbour Signal's format."""
import json

from describe import SEMANTIC_ORDER
from scales import STEPS

SCALE_TOKENS = tuple(f"{prefix}-{step}" for prefix in ("primary", "accent", "neutral") for step in STEPS)
ALL_TOKENS = SEMANTIC_ORDER + SCALE_TOKENS


def _block(selector, theme, shadow, scheme, indent=""):
    lines = [f"{indent}{selector} {{"]
    lines += [f"{indent}  --{token}: {theme[token]};" for token in ALL_TOKENS]
    lines += [f"{indent}  --shadow-pop: {shadow};", f"{indent}  color-scheme: {scheme};", f"{indent}}}"]
    return lines


def render_css(spec, system):
    p, a = spec["primary_color"]["name"], spec["accent_color"]["name"]
    header = (f"/* {spec['name']}: colour tokens. Primary {p}, accent {a}. "
              "Light is default; dark follows the system or data-theme=\"dark\". */")
    lines = [header]
    lines += _block(":root", system["light"], system["shadows"]["light"], "light")
    lines += ["", "@media (prefers-color-scheme: dark) {"]
    lines += _block(':root:not([data-theme="light"])', system["dark"], system["shadows"]["dark"], "dark", indent="  ")
    lines += ["}", ""]
    lines += _block(':root[data-theme="dark"]', system["dark"], system["shadows"]["dark"], "dark")
    return "\n".join(lines) + "\n"


def _color_ref(color):
    return {"name": color["name"], "hex": color["hex"], "file": f"../../colors/{color['slug']}.md"}


def render_json(spec, system):
    colors = {role: spec[f"{role}_color"] for role in ("primary", "accent", "spark", "ink")}
    document = {
        "name": spec["name"],
        "slug": spec["slug"],
        "character": spec["character"],
        "uses": spec["uses"],
        "source": spec["source"],
        "brand": {"primary": _color_ref(colors["primary"]), "accent": _color_ref(colors["accent"])},
        "logo": {role: _color_ref(colors[role]) for role in ("primary", "accent", "spark", "ink")},
        "anchorSteps": {"primary": system["steps"]["primary-anchor"], "accent": system["steps"]["accent-anchor"]},
        "themes": {theme: {token: system[theme][token] for token in ALL_TOKENS} for theme in ("light", "dark")},
        "shadow-pop": system["shadows"],
    }
    return json.dumps(document, indent=2, ensure_ascii=False) + "\n"
