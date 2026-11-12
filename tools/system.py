"""Build a Harbour-style colour system (light and dark tokens) from four library anchors."""
from colormath import contrast, hex_to_oklch, oklch_to_hex, hex_to_rgb
from scales import STEPS, brand_scale, neutral_scale, ink_relative, paper
from status import status_colors

WHITE = "#FFFFFF"
TEXT_MIN = 4.5
NON_TEXT_MIN = 3.0
DARK_ROLE_MIN = 7.0
PRIMARY_MAX_WHITE = 15.0
# An accent must still read as a colour, not as near-black text.
ACCENT_MAX_WHITE = 10.0
LIGHTNESS_STEP = 0.005
MAX_ADJUST_STEPS = 80

# Dark-theme surfaces as lightness offsets above the ink (Harbour Signal: #0C0C0D -> #161617 etc.).
DARK_SURFACE_OFFSETS = {"surface": 0.046, "surface-raised": 0.089, "surface-sunken": 0.023, "border": 0.131}
DARK_BORDER_STRONG_L = 0.54


def _shift(step, offset):
    index = min(max(STEPS.index(step) + offset, 0), len(STEPS) - 1)
    return STEPS[index]


def adjust_to_contrast(hex_value, grounds, minimum, darker):
    """Move a colour's lightness until it reaches `minimum` contrast on every ground."""
    L, C, H = hex_to_oklch(hex_value)
    current = hex_value
    for _ in range(MAX_ADJUST_STEPS):
        if all(contrast(current, g) >= minimum for g in grounds):
            return current
        L = L - LIGHTNESS_STEP if darker else L + LIGHTNESS_STEP
        current = oklch_to_hex(L, C, H)
    raise ValueError(f"Could not reach {minimum}:1 for {hex_value} on {grounds}")


def _light_brand_step(scale, anchor_step, grounds, max_white=PRIMARY_MAX_WHITE):
    """Anchor if it carries white labels (and text on `grounds`); otherwise the nearest step that does."""
    def ok(step):
        value = scale[step]
        white = contrast(value, WHITE)
        return TEXT_MIN <= white <= max_white and all(contrast(value, g) >= TEXT_MIN for g in grounds)

    if ok(anchor_step):
        return anchor_step
    candidates = [s for s in STEPS if ok(s)]
    if not candidates:
        raise ValueError(f"No light-theme step works for scale {scale}")
    return min(candidates, key=lambda s: abs(STEPS.index(s) - STEPS.index(anchor_step)))


def _dark_brand_step(scale, ink):
    """Darkest step that still gives ink labels 7:1, as Harbour Signal's Petrol 400 and Dusk 300 do."""
    passing = [s for s in STEPS if contrast(scale[s], ink) >= DARK_ROLE_MIN]
    return max(passing, key=STEPS.index)


def _chart_steps(scale, start, ground, order):
    """Harbour's chart order around the accent step, keeping only shades with 3:1 on the surface."""
    usable = [s for s in STEPS if contrast(scale[s], ground) >= NON_TEXT_MIN]
    picked = []
    for offset in order:
        step = _shift(start, offset)
        if step in usable and step not in picked and len(picked) < 5:
            picked.append(step)
    for step in sorted(usable, key=lambda s: abs(STEPS.index(s) - STEPS.index(start))):
        if len(picked) == 5:
            break
        if step not in picked:
            picked.append(step)
    if len(picked) < 5:
        raise ValueError(f"Only {len(picked)} chart shades reach 3:1 on {ground}")
    return picked


def _soft_for(scale, preferred, text_values):
    """Dark soft fill: the preferred step, or a darker one if the text on it falls short."""
    for step in STEPS[STEPS.index(preferred):]:
        if all(contrast(t, scale[step]) >= TEXT_MIN for t in text_values):
            return step
    raise ValueError("No dark soft step keeps text readable")


def build_system(primary_hex, accent_hex, spark_hex, ink_hex):
    p_scale, p_anchor = brand_scale(primary_hex)
    a_scale, a_anchor = brand_scale(accent_hex)
    n_scale = neutral_scale(ink_hex)
    status, status_notes = status_colors([primary_hex, accent_hex])
    light, dark, steps = {}, {}, {"primary-anchor": p_anchor, "accent-anchor": a_anchor}

    # Light foundation.
    bg = paper(ink_hex)
    light.update({"bg": bg, "surface": WHITE, "surface-raised": WHITE, "surface-sunken": n_scale[100], "border": n_scale[200]})
    light["border-strong"] = adjust_to_contrast(n_scale[500], [bg, WHITE], NON_TEXT_MIN, darker=True)
    light["text"] = ink_hex
    light["text-muted"] = adjust_to_contrast(n_scale[600], [bg, WHITE, n_scale[100]], TEXT_MIN, darker=True)

    # Dark foundation.
    dark["bg"] = ink_hex
    for token, offset in DARK_SURFACE_OFFSETS.items():
        dark[token] = ink_relative(ink_hex, offset)
    dark_grounds = [dark["bg"], dark["surface"], dark["surface-raised"]]
    _, ink_c, ink_h = hex_to_oklch(ink_hex)
    dark["border-strong"] = adjust_to_contrast(oklch_to_hex(DARK_BORDER_STRONG_L, min(ink_c, 0.012), ink_h), dark_grounds, NON_TEXT_MIN, darker=False)
    dark["text"] = bg
    dark["text-muted"] = adjust_to_contrast(n_scale[400], dark_grounds + [dark["surface-sunken"]], TEXT_MIN, darker=False)

    # Primary.
    lp = _light_brand_step(p_scale, p_anchor, [])
    link_step = _shift(lp, 1) if contrast(p_scale[lp], WHITE) < DARK_ROLE_MIN else lp
    while any(contrast(p_scale[link_step], g) < TEXT_MIN for g in (bg, WHITE, p_scale[50])):
        link_step = _shift(link_step, 1)
    light.update({
        "primary": p_scale[lp], "primary-hover": p_scale[_shift(lp, 1) if lp != 950 else 900],
        "primary-soft": p_scale[50], "on-primary": WHITE,
        "link": p_scale[link_step], "link-hover": p_scale[_shift(link_step, 1) if link_step != 950 else 900],
    })
    dp = _dark_brand_step(p_scale, ink_hex)
    dark_link_step = _shift(dp, -1)
    p_soft = _soft_for(p_scale, 800, [p_scale[dark_link_step], bg])
    dark.update({
        "primary": p_scale[dp], "primary-hover": p_scale[_shift(dp, -1)], "primary-soft": p_scale[p_soft], "on-primary": ink_hex,
        "link": p_scale[dark_link_step], "link-hover": p_scale[_shift(dp, -2)],
    })

    # Accent and focus.
    la = _light_brand_step(a_scale, a_anchor, [bg, a_scale[50]], ACCENT_MAX_WHITE)
    da = _dark_brand_step(a_scale, ink_hex)
    a_soft = _soft_for(a_scale, 900, [a_scale[da]])
    light.update({"accent": a_scale[la], "accent-soft": a_scale[50], "on-accent": WHITE, "focus": a_scale[la], "selection": p_scale[100]})
    dark.update({"accent": a_scale[da], "accent-soft": a_scale[a_soft], "on-accent": ink_hex, "focus": a_scale[da], "selection": p_scale[p_soft]})

    # Disabled and info.
    light.update({"disabled-bg": n_scale[100], "disabled-text": n_scale[500], "info": light["link"], "info-soft": light["primary-soft"]})
    dark.update({"disabled-bg": dark["surface-raised"], "disabled-text": n_scale[600], "info": dark["link"], "info-soft": dark["primary-soft"]})

    # Status.
    for name, values in status.items():
        light_soft, dark_soft = values["light-soft"], values["dark-soft"]
        light[name] = adjust_to_contrast(values["light"], [bg, WHITE, light_soft], TEXT_MIN, darker=True)
        light[f"{name}-soft"], light[f"on-{name}"] = light_soft, WHITE
        dark[name] = adjust_to_contrast(values["dark"], dark_grounds + [dark_soft, ink_hex], TEXT_MIN, darker=False)
        dark[f"{name}-soft"], dark[f"on-{name}"] = dark_soft, ink_hex

    # Charts: accent shades plus the primary as the one contrasting series.
    light_chart = _chart_steps(a_scale, la, WHITE, (0, 2, -2, 1, -1))
    dark_chart = _chart_steps(a_scale, da, dark["surface"], (0, -2, 2, -1, 1))
    for i, (ls, ds) in enumerate(zip(light_chart, dark_chart), start=1):
        light[f"chart-{i}"], dark[f"chart-{i}"] = a_scale[ls], a_scale[ds]
    light.update({"chart-alt": light["primary"], "chart-grid": light["border"]})
    dark.update({"chart-alt": dark["primary"], "chart-grid": dark["border"]})

    # Logo-only and raw colours, then the scales (identical in both themes, as in Harbour Signal).
    for theme in (light, dark):
        theme.update({"ink": ink_hex, "logo-spark": spark_hex, "logo-ink": ink_hex})
        for prefix, scale in (("primary", p_scale), ("accent", a_scale), ("neutral", n_scale)):
            theme.update({f"{prefix}-{step}": scale[step] for step in STEPS})

    steps.update({
        "light-primary": lp, "light-link": link_step, "dark-primary": dp, "dark-link": dark_link_step,
        "dark-primary-soft": p_soft, "light-accent": la, "dark-accent": da, "dark-accent-soft": a_soft,
        "light-chart": light_chart, "dark-chart": dark_chart,
    })
    ink_rgb = ", ".join(str(round(c * 255)) for c in hex_to_rgb(ink_hex))
    shadows = {
        "light": f"0 1px 2px 0 rgba({ink_rgb}, 0.08), 0 8px 24px 0 rgba({ink_rgb}, 0.10)",
        "dark": "0 1px 2px 0 rgba(0, 0, 0, 0.60), 0 8px 24px 0 rgba(0, 0, 0, 0.45)",
    }
    return {"light": light, "dark": dark, "steps": steps, "status_notes": status_notes, "shadows": shadows,
            "scales": {"primary": p_scale, "accent": a_scale, "neutral": n_scale}}
