"""The Palettes and Colours sections of Kolors/index.md. Links are relative to Kolors/."""
from colormath import hex_to_oklch

ROLES = ("primary", "accent", "spark", "ink")
NEUTRAL_MAX_CHROMA = 0.03
WHITE_MIN_L, BLACK_MAX_L = 0.9, 0.3
BROWN_HUES, BROWN_MAX_L, BROWN_MAX_CHROMA = (20, 85), 0.6, 0.13
COOL_GREY_HUES = (110, 300)
# Hue families in OKLCH degrees; pinks wrap past 360.
HUE_FAMILIES = (
    ("Reds", 10, 40), ("Oranges", 40, 75), ("Yellows", 75, 115), ("Greens", 115, 170),
    ("Teals", 170, 215), ("Blues", 215, 275), ("Purples", 275, 325), ("Pinks", 325, 370),
)
FAMILY_ORDER = tuple(name for name, _, _ in HUE_FAMILIES) + ("Browns", "Whites", "Warm greys", "Cool greys", "Blacks")
FAMILY_NOTES = {
    "Browns": "warm hues that are dark and muted",
    "Whites": "near-colourless and very light",
    "Warm greys": "near-colourless with a red, yellow or pink cast: stones, taupes and greiges",
    "Cool greys": "near-colourless with a green, blue or violet cast",
    "Blacks": "near-colourless and very dark",
}


def color_family(hex_value):
    lightness, chroma, hue = hex_to_oklch(hex_value)
    if chroma < NEUTRAL_MAX_CHROMA:
        if lightness >= WHITE_MIN_L:
            return "Whites"
        if lightness < BLACK_MAX_L:
            return "Blacks"
        return "Cool greys" if COOL_GREY_HUES[0] <= hue < COOL_GREY_HUES[1] else "Warm greys"
    if BROWN_HUES[0] <= hue < BROWN_HUES[1] and lightness < BROWN_MAX_L and chroma < BROWN_MAX_CHROMA:
        return "Browns"
    wrapped = hue if hue >= HUE_FAMILIES[0][1] else hue + 360
    return next(name for name, start, end in HUE_FAMILIES if start <= wrapped < end)


def palette_usage(specs):
    """{colour slug: [(palette spec, role), ...]} for every colour a system uses."""
    usage = {}
    for spec in sorted(specs, key=lambda s: s["name"]):
        for role in ROLES:
            slug = spec[role]
            usage[slug] = usage.get(slug, []) + [(spec, role)]
    return usage


def _anchor(title):
    return title.lower().replace(" ", "-")


def _cell(text):
    return text.replace("|", "\\|")


def _sort_key(color):
    lightness, chroma, hue = hex_to_oklch(color["hex"])
    return (-round(lightness, 2), hue, -chroma)


def _usage_cell(entries):
    return ", ".join(f"[{spec['name']}](palettes/{spec['slug']}/{spec['slug']}.md) ({role})" for spec, role in entries)


def _swatch_link(color):
    return f"![{color['hex']}](colors/swatches/{color['slug']}.png) [{_cell(color['name'])}](colors/{color['slug']}.md)"


def render_palettes_section(specs):
    lines = [
        "## Palettes", "",
        f"{len(specs)} colour systems built on the Harbour Signal model: **two brand colours** (a primary and an accent), "
        "**two logo-only colours** (a spark and an ink), plain grey neutrals, and full light and dark role tokens. "
        "Each folder holds the documentation, CSS custom properties, JSON tokens and a visual sheet.", "",
        "| Palette | Brand: primary + accent | Logo only: spark + ink | Character | Source |", "|---|---|---|---|---|",
    ]
    for s in sorted(specs, key=lambda s: s["name"]):
        source = "new library combination" if s["source"] == "library" else f"v1 {s['source_name']}"
        brand = " + ".join(_swatch_link(s[f"{r}_color"]) for r in ("primary", "accent"))
        logo = " + ".join(_swatch_link(s[f"{r}_color"]) for r in ("spark", "ink"))
        lines.append(f"| [{s['name']}](palettes/{s['slug']}/{s['slug']}.md) | {brand} | {logo} | {s['character']} | {source} |")
    return lines + [""]


def render_colors_section(library, specs):
    usage = palette_usage(specs)
    groups = {name: [] for name in FAMILY_ORDER}
    for color in library.values():
        groups[color_family(color["hex"])].append(color)
    used = sum(1 for slug in library if slug in usage)
    lines = [
        "## Colours", "",
        f"{len(library)} colours, grouped by hue family and sorted light to dark. "
        f"{used} of them anchor a system in [Palettes](#palettes); the last column shows which and in what role.", "",
        " · ".join(f"[{name} ({len(groups[name])})](#{_anchor(name)})" for name in FAMILY_ORDER if groups[name]), "",
        "Families use OKLCH hue. Near-colourless colours (chroma under "
        f"{NEUTRAL_MAX_CHROMA}) are split into whites, greys and blacks by lightness.", "",
    ]
    for name in FAMILY_ORDER:
        members = sorted(groups[name], key=_sort_key)
        if not members:
            continue
        note = f" ({FAMILY_NOTES[name]})" if name in FAMILY_NOTES else ""
        lines += [f"### {name}", "", f"{len(members)} colours{note}.", "",
                  "| Colour | HEX | Character | In palettes |", "|---|---|---|---|"]
        for color in members:
            lines.append(f"| {_swatch_link(color)} | {color['hex']} | {_cell(color['character'])} | "
                         f"{_usage_cell(usage.get(color['slug'], []))} |")
        lines.append("")
    return lines


def render_index_block(library, specs):
    return "\n".join(render_palettes_section(specs) + render_colors_section(library, specs)).rstrip() + "\n"
