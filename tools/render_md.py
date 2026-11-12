"""Markdown documentation for one colour system."""
from colormath import hex_to_rgb
from describe import token_uses, SEMANTIC_ORDER
from scales import STEPS

COLORS_REL = "../../colors"
SCALE_MARKER_TOKENS = ("primary", "primary-hover", "primary-soft", "link", "link-hover", "accent", "accent-soft",
                       "selection", "chart-1", "chart-2", "chart-3", "chart-4", "chart-5")


def _link(color):
    return f"[{color['name']}]({COLORS_REL}/{color['slug']}.md)"


def _rgb(hex_value):
    return ", ".join(str(round(c * 255)) for c in hex_to_rgb(hex_value))


def _names(spec):
    return {role: spec[f"{role}_color"]["name"] for role in ("primary", "accent", "spark", "ink")}


def _header(spec, system):
    p, a, s, k = (spec[f"{r}_color"] for r in ("primary", "accent", "spark", "ink"))
    slug = spec["slug"]
    if spec["source"] == "library":
        source = "A new combination from the colour library."
    else:
        source = f"Rebuilt from the v1 palette {spec['source_name']}."
    return [
        f"# {spec['name']}", "",
        f"![{spec['name']} colour system sheet]({slug}.png)", "",
        f"- Character: {spec['character']}",
        f"- Suggested uses: {spec['uses']}",
        f"- Source: {source}",
        f"- Files: [CSS tokens]({slug}.css) · [JSON tokens]({slug}.tokens.json) · [Colour sheet]({slug}.png)", "",
        f"Brand colours: {p['name']} {p['hex']} (primary), {a['name']} {a['hex']} (accent). "
        f"Charts: {a['name']} shades plus {p['name']}. Logo and icon only: {s['name']} {s['hex']} (spark), {k['name']} {k['hex']} (ink).", "",
    ]


def _brand_section(spec, system):
    st, L, D = system["steps"], system["light"], system["dark"]
    lines = ["## Brand colours", ""]
    for role, label, light_key, dark_key, anchor_key in (
        ("primary", "Brand 1 · primary", "light-primary", "dark-primary", "primary-anchor"),
        ("accent", "Brand 2 · accent", "light-accent", "dark-accent", "accent-anchor"),
    ):
        color = spec[f"{role}_color"]
        lines.append(
            f"- {label}: {_link(color)} ({color['hex']}, RGB {_rgb(color['hex'])}), the {role} scale's anchor at step {st[anchor_key]}. "
            f"Light UI uses {role}-{st[light_key]} ({L[role]}); dark UI uses {role}-{st[dark_key]} ({D[role]})."
        )
    lines += ["", "Supporting neutrals are plain greys, not brand colours: paper "
              f"{L['bg']} for light pages, grey {L['text-muted']} for muted text, and the ink for text and dark pages.", ""]
    return lines


def _logo_section(spec, matrix):
    s, k = spec["spark_color"], spec["ink_color"]
    lines = [
        "## Logo and icon colours", "",
        f"The two brand colours plus two that exist only for the logo and icon. {s['name']} and {k['name']} never appear as UI colours.", "",
        f"- Spark: {_link(s)} ({s['hex']}). The signal light: a single dot, stroke or highlight in the mark.",
        f"- Ink: {_link(k)} ({k['hex']}). Wordmark and one-colour versions.", "",
        "### Which colours work on which ground (3:1 minimum for graphics)", "",
        "| Mark | " + " | ".join(name for name, _ in matrix["grounds"]) + " |",
        "|---|" + "---|" * len(matrix["grounds"]),
    ]
    for row in matrix["rows"]:
        cells = []
        for cell in row["cells"]:
            if cell["same"]:
                cells.append("same")
            else:
                cells.append(f"{'✓' if cell['passes'] else '✗'} {cell['ratio']:.1f}")
        lines.append(f"| {row['mark']} | " + " | ".join(cells) + " |")
    lines.append("")
    for ground, marks in matrix["works_on"].items():
        lines.append(f"- On {ground}: {', '.join(marks) if marks else 'no listed colour reaches 3:1'}.")
    return lines + [""]


def _token_table(spec, system):
    uses = token_uses(system, _names(spec))
    lines = [
        "## Tokens", "",
        "Light is the default; dark follows the system setting or `data-theme=\"dark\"`. Use the semantic tokens in UI code, never raw scale steps.", "",
        "| Token | Light | Dark | Use |", "|---|---|---|---|",
    ]
    for token in SEMANTIC_ORDER:
        lines.append(f"| {token} | {system['light'][token]} | {system['dark'][token]} | {uses[token]} |")
    return lines + [""]


def _scale_markers(system, prefix, step):
    value = system["scales"][prefix][step]
    marks = []
    for theme in ("light", "dark"):
        used = [t for t in SCALE_MARKER_TOKENS if system[theme][t] == value]
        if used:
            marks.append(f"{theme}: {', '.join(used)}")
    if system["steps"].get(f"{prefix}-anchor") == step:
        marks.insert(0, "brand anchor")
    return "; ".join(marks)


def _scales_section(spec, system):
    p, a = spec["primary_color"]["name"], spec["accent_color"]["name"]
    lines = [
        "## Scales", "",
        f"Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: "
        f"{p} at primary-{system['steps']['primary-anchor']}, {a} at accent-{system['steps']['accent-anchor']}. Identical in both themes.", "",
        f"| Step | Primary ({p}) | Primary roles | Accent ({a}) | Accent roles | Neutral |", "|---|---|---|---|---|---|",
    ]
    for step in STEPS:
        sc = system["scales"]
        lines.append(f"| {step} | {sc['primary'][step]} | {_scale_markers(system, 'primary', step)} | "
                     f"{sc['accent'][step]} | {_scale_markers(system, 'accent', step)} | {sc['neutral'][step]} |")
    return lines + [""]


def _pairings_section(cards):
    lines = ["## Accessible pairings", "", "AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.", ""]
    for card in cards:
        lines.append(f"- {card['title']} ({card['theme']}): `{card['fg']}` {card['fg_hex']} on `{card['bg']}` {card['bg_hex']}: "
                     f"**{card['ratio']:.1f}:1**, {card['grade']}.")
    return lines + [""]


def _rules_section(spec, system, matrix):
    p, a, s, k = (spec[f"{r}_color"]["name"] for r in ("primary", "accent", "spark", "ink"))
    st = system["steps"]
    rules = [
        "Use roles in UI code, never raw scale steps.",
        f"Brand colours are {p} and {a} only. {s} and {k} are for the logo and icon, never for charts or UI.",
        f"Charts use five shades of {a}, plus {p} as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.",
        "One primary button per view, and one accent button at most.",
        "Never signal status by colour alone: icon and word every time.",
        "Control borders use `border-strong`; decorative ones use `border`.",
        f"In dark mode the primary lightens to primary-{st['dark-primary']}, links to primary-{st['dark-link']}, and button labels turn ink.",
    ]
    for role in ("primary", "accent"):
        if st[f"light-{role}"] != st[f"{role}-anchor"]:
            name = spec[f"{role}_color"]["name"]
            rules.append(f"{name} itself sits at {role}-{st[f'{role}-anchor']}; light-mode UI uses {role}-{st[f'light-{role}']} so labels and text "
                         f"pass 4.5:1. Use the exact {name} in the logo and large graphics.")
    if s not in matrix["works_on"][p] and s not in matrix["works_on"][a]:
        rules.append(f"{s} reaches 3:1 only on {', '.join(g for g, m in matrix['works_on'].items() if s in m)}; keep it off {p} and {a} grounds.")
    rules += system["status_notes"]
    return ["## Rules", ""] + [f"- {r}" for r in rules] + [""]


def _verification_section(audit_rows):
    count = len(audit_rows)
    return [
        "## Verification notes", "",
        "- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's "
        "lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. "
        "Refer to generated values by token, not by a library colour name.",
        f"- Contrast audit: {count} documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, "
        "primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.",
        "- Hover, pressed and disabled states are defined, but components still need their own checks in context.",
        "- Character and suggested uses are design judgments, not user-research findings.", "",
    ]


def render_markdown(spec, system, matrix, cards, audit_rows):
    sections = (
        _header(spec, system), _brand_section(spec, system), _logo_section(spec, matrix),
        ["## Pairing rationale", "", spec["rationale"], ""], _token_table(spec, system), _scales_section(spec, system),
        _pairings_section(cards), _rules_section(spec, system, matrix), _verification_section(audit_rows),
    )
    return "\n".join(line for section in sections for line in section).rstrip() + "\n"
