"""A one-page visual sheet (HTML) for a colour system, laid out like the Harbour Signal sheet."""
from html import escape

from colormath import contrast, hex_to_rgb
from scales import STEPS
from render_tokens import ALL_TOKENS

PAGE_BG = "#F4F4F2"
ROLE_SWATCHES = ("bg", "surface", "surface-raised", "surface-sunken", "border", "border-strong", "text", "text-muted",
                 "primary", "accent", "focus", "link", "success", "warning", "danger", "info")
PROPORTIONS = (("Paper", "surfaces, space", 54), ("Ink", "text, dark UI", 26), ("primary", "brand 1", 14), ("accent", "brand 2", 6))
BAR_HEIGHTS = ((62, 38), (80, 52), (45, 70), (92, 60), (58, 84), (74, 46))

BASE_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: %(page)s; font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; color: #18181A; width: 1100px; }
.hero { padding: 56px 56px 44px; }
.eyebrow { font-size: 11px; letter-spacing: .14em; text-transform: uppercase; opacity: .7; }
.hero h1 { font-size: 64px; letter-spacing: -.03em; margin: 10px 0 8px; font-weight: 700; }
.hero p { font-size: 15px; opacity: .85; max-width: 640px; }
.bar { display: flex; height: 26px; margin-top: 30px; border-radius: 4px; overflow: hidden; outline: 1px solid rgba(255,255,255,.28); }
.bar-labels { display: flex; font-size: 11px; margin-top: 8px; opacity: .75; }
section { padding: 40px 56px 8px; }
h2 { font-size: 26px; letter-spacing: -.01em; margin-bottom: 4px; }
.sub { font-size: 13px; color: #5C5C60; margin-bottom: 18px; }
.label { font-size: 10px; letter-spacing: .12em; text-transform: uppercase; color: #5C5C60; margin: 22px 0 10px; }
.row { display: flex; gap: 16px; }
.brand-card { flex: 1; border-radius: 8px; overflow: hidden; background: #fff; border: 1px solid #E3E3E3; }
.brand-card .fill { height: 120px; padding: 14px 16px; display: flex; flex-direction: column; justify-content: space-between; }
.brand-card .fill b { font-size: 22px; }
.brand-card .meta { padding: 12px 16px 14px; font-size: 12px; color: #444; line-height: 1.45; }
.mono { font-family: ui-monospace, Menlo, monospace; font-size: 11px; }
.neutral { display: flex; align-items: center; gap: 12px; flex: 1; font-size: 12px; }
.neutral .chip { width: 64px; height: 44px; border-radius: 6px; border: 1px solid #E3E3E3; display: flex; align-items: flex-end; padding: 4px 6px; font-size: 10px; }
.logo-swatch { flex: 1; }
.logo-swatch .fill { height: 64px; border-radius: 6px; padding: 10px; font-weight: 600; font-size: 14px; display: flex; align-items: flex-end; }
.logo-swatch .cap { font-size: 11px; color: #444; margin-top: 6px; line-height: 1.4; }
.ground { flex: 1; background: #fff; border: 1px solid #E3E3E3; border-radius: 8px; padding: 14px; font-size: 11px; color: #444; }
.ground svg { display: block; margin-bottom: 10px; }
table { border-collapse: collapse; width: 100%%; background: #fff; border: 1px solid #E3E3E3; border-radius: 8px; font-size: 12px; }
th, td { text-align: left; padding: 8px 12px; border-bottom: 1px solid #EFEFEF; }
th { font-size: 10px; letter-spacing: .1em; text-transform: uppercase; color: #5C5C60; font-weight: 600; }
.dot { display: inline-block; width: 12px; height: 12px; border-radius: 3px; vertical-align: -2px; margin-right: 8px; border: 1px solid rgba(0,0,0,.12); }
.pass { color: #13794A; } .fail { color: #B8331E; }
.scale-name { font-size: 10px; letter-spacing: .12em; text-transform: uppercase; color: #5C5C60; margin: 18px 0 6px; }
.scale { display: flex; border-radius: 6px; overflow: hidden; }
.scale div { flex: 1; height: 92px; padding: 8px 7px; display: flex; flex-direction: column; justify-content: space-between; font-size: 10px; }
.scale b { font-size: 13px; }
.panels { display: flex; gap: 16px; }
.panel { flex: 1; border-radius: 8px; padding: 18px 20px; border: 1px solid; }
.panel .eyebrow { margin-bottom: 12px; }
.role { display: flex; align-items: center; justify-content: space-between; font-size: 12px; padding: 4px 0; }
.role span:first-child { display: flex; align-items: center; }
.role .sw { width: 18px; height: 14px; border-radius: 3px; margin-right: 10px; border: 1px solid rgba(127,127,127,.35); }
.demo { background: var(--bg); color: var(--text); border-color: var(--border); }
.card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 16px; box-shadow: var(--shadow-pop); }
.card h3 { font-size: 17px; } .card p { font-size: 12px; color: var(--text-muted); margin: 4px 0 14px; }
.btns { display: flex; gap: 8px; margin-bottom: 14px; }
.btn { font-size: 12px; font-weight: 600; padding: 7px 12px; border-radius: 6px; border: 1px solid transparent; }
.btn-primary { background: var(--primary); color: var(--on-primary); }
.btn-secondary { background: var(--surface); color: var(--text); border-color: var(--border-strong); outline: 2px solid var(--focus); outline-offset: 2px; }
.btn-accent { background: var(--accent); color: var(--on-accent); }
.chips { display: flex; gap: 8px; margin-bottom: 14px; }
.chip-s { font-size: 11px; font-weight: 600; padding: 3px 9px; border-radius: 99px; }
.card a { font-size: 12px; color: var(--link); text-decoration: underline; }
.chart-panel { flex: 1; border-radius: 8px; padding: 20px; border: 1px solid; }
.legend { display: flex; gap: 6px; margin-bottom: 16px; }
.legend div { flex: 1; height: 22px; border-radius: 4px; }
.bars { display: flex; align-items: flex-end; justify-content: space-around; height: 150px; border-bottom: 1px solid; padding: 0 10px; }
.bars .g { display: flex; gap: 6px; align-items: flex-end; height: 100%%; }
.bars .g div { width: 18px; border-radius: 3px 3px 0 0; }
.strip { display: flex; margin-top: 16px; height: 14px; border-radius: 3px; overflow: hidden; }
.strip div { flex: 1; }
.pairs { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.pair { border-radius: 8px; padding: 14px; border: 1px solid #E3E3E3; min-height: 92px; }
.pair b { font-size: 26px; display: block; }
.pair span { font-size: 11px; display: block; margin-top: 4px; }
.rules { display: flex; gap: 24px; padding-bottom: 56px; }
.rules ul { flex: 1; font-size: 12px; line-height: 1.6; padding-left: 16px; color: #333; }
.rules pre { flex: 1; background: #111113; color: #E6E6E6; border-radius: 8px; padding: 16px; font-size: 11px; line-height: 1.5; }
"""


def _text_on(hex_value):
    return "#FFFFFF" if contrast("#FFFFFF", hex_value) >= contrast("#0C0C0D", hex_value) else "#0C0C0D"


def _vars(theme):
    return " ".join(f"--{t}: {theme[t]};" for t in ALL_TOKENS)


def _hero(spec, system):
    k, p, a = spec["ink_color"], spec["primary_color"], spec["accent_color"]
    fills = {"Paper": system["light"]["bg"], "Ink": k["hex"], "primary": p["hex"], "accent": a["hex"]}
    names = {"Paper": "Paper", "Ink": "Ink", "primary": p["name"], "accent": a["name"]}
    bar = "".join(f'<div style="flex:{w};background:{fills[key]}"></div>' for key, _, w in PROPORTIONS)
    labels = "".join(f'<div style="flex:{w}">{escape(names[key])}: {cap}</div>' for key, cap, w in PROPORTIONS)
    return (f'<div class="hero" style="background:{k["hex"]};color:{system["dark"]["text"]}">'
            f'<div class="eyebrow">Kolors colour system · v2</div><h1>{escape(spec["name"])}</h1>'
            f'<p>Two brand colours, {escape(p["name"])} and {escape(a["name"])}, on plain greys. '
            f'{escape(spec["character"].capitalize())}. Built for dashboards, websites and apps, in light and dark.</p>'
            f'<div class="bar">{bar}</div><div class="bar-labels">{labels}</div></div>')


def _brand(spec, system):
    cards = []
    for role, label, caption in (
        ("primary", "Brand 1 · primary", "Buttons, links, selected states and active navigation."),
        ("accent", "Brand 2 · accent", "One highlight per view, new-feature badges and the keyboard focus ring."),
    ):
        c = spec[f"{role}_color"]
        rgb = ", ".join(str(round(v * 255)) for v in hex_to_rgb(c["hex"]))
        step = system["steps"][f"light-{role}"]
        cards.append(f'<div class="brand-card"><div class="fill" style="background:{c["hex"]};color:{_text_on(c["hex"])}">'
                     f'<span class="eyebrow">{label}</span><b>{escape(c["name"])}</b></div>'
                     f'<div class="meta">{caption} Light UI uses {role}-{step} {system["light"][role]}; dark UI uses '
                     f'{system["dark"][role]}.<br><span class="mono">HEX {c["hex"]} · RGB {rgb}</span></div></div>')
    neutrals = "".join(
        f'<div class="neutral"><div class="chip" style="background:{hx};color:{_text_on(hx)}">{name}</div>'
        f'<div><span class="mono">{hx}</span><br>{cap}</div></div>'
        for name, hx, cap in (("Paper", system["light"]["bg"], "Page background in light, text in dark."),
                              ("Grey", system["light"]["text-muted"], "Muted text and borders."),
                              ("Ink", spec["ink_color"]["hex"], "Text in light, page background in dark.")))
    return (f'<section><h2>Brand palette</h2><div class="sub">Two colours. Everything else is a neutral, a status colour or a shade of these two.</div>'
            f'<div class="row">{"".join(cards)}</div><div class="label">Supporting neutrals (not brand colours)</div><div class="row">{neutrals}</div></section>')


def _mark(ground_hex, arc_hex, dot_hex):
    return (f'<svg width="72" height="72" viewBox="0 0 72 72"><rect width="72" height="72" rx="16" fill="{ground_hex}" stroke="#E3E3E3"/>'
            f'<path d="M18 54 C 20 32, 34 20, 54 18" stroke="{arc_hex}" stroke-width="9" fill="none" stroke-linecap="round"/>'
            f'<circle cx="52" cy="50" r="7" fill="{dot_hex}"/></svg>')


def _logo(spec, system, matrix):
    swatches = "".join(
        f'<div class="logo-swatch"><div class="fill" style="background:{c["hex"]};color:{_text_on(c["hex"])}">{escape(c["name"])}</div>'
        f'<div class="cap"><span class="mono">{c["hex"]}</span><br>{cap}</div></div>'
        for c, cap in ((spec["primary_color"], "Brand 1. Main shape of the mark."), (spec["accent_color"], "Brand 2. Secondary shape or detail."),
                       (spec["spark_color"], "Logo only. The signal light: a single dot or highlight."), (spec["ink_color"], "Logo only. Wordmark and one-colour versions.")))
    hexes = {row["mark"]: row["hex"] for row in matrix["rows"]}
    spark = spec["spark_color"]["name"]
    tiles = []
    for ground_name, ground_hex in matrix["grounds"]:
        works = matrix["works_on"][ground_name]
        shapes = [m for m in works if m != spark] or works or [ground_name]
        arc = hexes.get(shapes[0], ground_hex)
        dot_name = spark if spark in works else (shapes[1] if len(shapes) > 1 else shapes[0])
        tiles.append(f'<div class="ground">{_mark(ground_hex, arc, hexes.get(dot_name, arc))}<b>On {escape(ground_name)}</b><br>'
                     f'{escape(", ".join(works) or "nothing reaches 3:1")}</div>')
    head = "".join(f"<th>{escape(g)}</th>" for g, _ in matrix["grounds"])
    body = ""
    for row in matrix["rows"]:
        cells = "".join("<td>same</td>" if c["same"] else f'<td class="{"pass" if c["passes"] else "fail"}">{"✓" if c["passes"] else "✗"} {c["ratio"]:.1f}</td>'
                        for c in row["cells"])
        body += f'<tr><td><span class="dot" style="background:{row["hex"]}"></span>{escape(row["mark"])}</td>{cells}</tr>'
    return (f'<section><h2>Logo and icon colours</h2><div class="sub">The two brand colours plus two that exist only for the logo and icon. '
            f'{escape(spark)} and {escape(spec["ink_color"]["name"])} never appear as UI colours.</div><div class="row">{swatches}</div>'
            f'<div class="label">Colour test on each ground</div><div class="row">{"".join(tiles)}</div>'
            f'<div class="label">Which colours work on which ground · 3:1 minimum for graphics</div>'
            f'<table><tr><th></th>{head}</tr>{body}</table></section>')


def _scales(spec, system):
    rows = ""
    for prefix, title in (("primary", spec["primary_color"]["name"]), ("accent", spec["accent_color"]["name"]), ("neutral", "Neutral")):
        cells = ""
        for step in STEPS:
            hx = system["scales"][prefix][step]
            fg = _text_on(hx)
            anchor = " · anchor" if system["steps"].get(f"{prefix}-anchor") == step else ""
            cells += f'<div style="background:{hx};color:{fg}"><b>{step}</b><span class="mono">{hx}<br>{contrast(fg, hx):.1f}:1{anchor}</span></div>'
        rows += f'<div class="scale-name">{escape(title)}</div><div class="scale">{cells}</div>'
    return (f'<section><h2>Scales</h2><div class="sub">Each brand anchor keeps its exact value at the step nearest its lightness. '
            f'Ratio shown is the contrast of the label colour on each swatch.</div>{rows}</section>')


def _roles(system):
    panels = ""
    for theme in ("light", "dark"):
        t = system[theme]
        rows = "".join(f'<div class="role"><span><span class="sw" style="background:{t[r]}"></span>{r}</span><span class="mono">{t[r]}</span></div>'
                       for r in ROLE_SWATCHES)
        panels += (f'<div class="panel" style="background:{t["bg"]};color:{t["text"]};border-color:{t["border"]}">'
                   f'<div class="eyebrow">{theme} theme</div>{rows}</div>')
    return f'<section><h2>Light and dark roles</h2><div class="sub">Use roles in UI, never raw steps. Each role has a value per theme.</div><div class="panels">{panels}</div></section>'


def _in_use(spec, system):
    panels = ""
    for theme in ("light", "dark"):
        t = system[theme]
        chips = "".join(f'<span class="chip-s" style="background:{t[s + "-soft"]};color:{t[s]}">{icon} {word}</span>'
                        for s, icon, word in (("success", "✓", "Saved"), ("warning", "▲", "Check this"), ("danger", "✕", "Failed"), ("info", "ℹ", "Note")))
        panels += (f'<div class="panel demo" style="{_vars(t)} --shadow-pop: {system["shadows"][theme]};">'
                   f'<div class="eyebrow">{theme}</div><div class="card"><h3>{escape(spec["name"])} Studio</h3>'
                   f'<p>Open until 18:00. New season collection in store.</p>'
                   f'<div class="btns"><span class="btn btn-primary">Save changes</span><span class="btn btn-secondary">Cancel</span>'
                   f'<span class="btn btn-accent">What\'s new</span></div><div class="chips">{chips}</div><a>View opening hours</a></div></div>')
    return (f'<section><h2>In use</h2><div class="sub">Status always carries an icon and a word. Focus is a 2px {escape(spec["accent_color"]["name"])} ring '
            f'(shown on Cancel).</div><div class="panels">{panels}</div></section>')


def _charts(spec, system):
    panels = ""
    for theme in ("light", "dark"):
        t = system[theme]
        series = [t[f"chart-{i}"] for i in range(1, 6)] + [t["chart-alt"]]
        legend = "".join(f'<div style="background:{c}"></div>' for c in series)
        groups = "".join(f'<div class="g"><div style="height:{h1}%;background:{series[i % 5]}"></div><div style="height:{h2}%;background:{t["chart-alt"]}"></div></div>'
                         for i, (h1, h2) in enumerate(BAR_HEIGHTS))
        strip = "".join(f'<div style="background:{system["scales"]["accent"][s]}"></div>' for s in STEPS)
        panels += (f'<div class="chart-panel" style="background:{t["surface"]};border-color:{t["border"]};color:{t["text-muted"]}">'
                   f'<div class="eyebrow" style="margin-bottom:12px">{theme}</div><div class="legend">{legend}</div>'
                   f'<div class="bars" style="border-color:{t["chart-grid"]}">{groups}</div><div class="strip">{strip}</div></div>')
    return (f'<section><h2>Chart palette</h2><div class="sub">Charts use five shades of {escape(spec["accent_color"]["name"])}, plus '
            f'{escape(spec["primary_color"]["name"])} as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.</div>'
            f'<div class="panels">{panels}</div></section>')


def _pairs(cards):
    tiles = "".join(f'<div class="pair" style="background:{c["bg_hex"]};color:{c["fg_hex"]}"><b>Aa</b><span>{escape(c["title"])}</span>'
                    f'<span class="mono">{c["ratio"]:.1f}:1 · {c["grade"]}</span></div>' for c in cards)
    return f'<section><h2>Accessible pairings</h2><div class="sub">AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.</div><div class="pairs">{tiles}</div></section>'


def _rules(spec, system):
    p, a, s, k = (spec[f"{r}_color"]["name"] for r in ("primary", "accent", "spark", "ink"))
    st = system["steps"]
    rules = [
        "Use roles in UI code, not raw scale steps.",
        f"Brand colours are {p} and {a} only. {s} and {k} are for the logo and icon, never for charts or UI.",
        f"Charts use shades of {a}, plus {p} as the one contrasting series.",
        "One primary button per view, and one accent button at most.",
        "Never signal status by colour alone: icon and word every time.",
        "Control borders use border-strong; decorative ones use border.",
        f"In dark mode the primary lightens to primary-{st['dark-primary']} and its label turns ink.",
    ]
    snippet_tokens = ("bg", "surface", "text", "text-muted", "primary", "primary-hover", "on-primary", "accent", "focus", "success", "warning", "danger")
    css = ":root {\n" + "".join(f"  --{t}: {system['light'][t]};\n" for t in snippet_tokens) + "}\n[data-theme=\"dark\"] {\n"
    css += "".join(f"  --{t}: {system['dark'][t]};\n" for t in snippet_tokens) + "}"
    items = "".join(f"<li>{escape(r)}</li>" for r in rules)
    return f'<section><h2>Rules</h2><div class="rules"><ul>{items}</ul><pre>{escape(css)}</pre></div></section>'


def render_sheet(spec, system, matrix, cards):
    body = "".join((_hero(spec, system), _brand(spec, system), _logo(spec, system, matrix), _scales(spec, system),
                    _roles(system), _in_use(spec, system), _charts(spec, system), _pairs(cards), _rules(spec, system)))
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{escape(spec["name"])}</title>'
            f'<style>{BASE_CSS % {"page": PAGE_BG}}</style></head><body>{body}</body></html>')
