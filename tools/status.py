"""Status colours (success, warning, danger) re-hued per system to stay apart from the brand hues."""
from colormath import hex_to_oklch, oklch_to_hex, hue_distance

# Harbour Signal's status values: light text/fill, light soft, dark text/fill, dark soft.
HARBOUR_STATUS = {
    "success": {"light": "#13794A", "light-soft": "#E4F3EB", "dark": "#1BA766", "dark-soft": "#0F2A1E",
                "family": (140, 175), "lower": "yellow-green", "higher": "teal"},
    "warning": {"light": "#915608", "light-soft": "#FBEFD9", "dark": "#F4A134", "dark-soft": "#2B1F0A",
                "family": (50, 85), "lower": "orange", "higher": "yellow"},
    "danger": {"light": "#B8331E", "light-soft": "#FBE9E5", "dark": "#E57361", "dark-soft": "#2E1612",
               "family": (18, 40), "lower": "crimson", "higher": "orange-red"},
}

# Brand colours below this chroma read as neutrals and cannot be confused with a status hue.
BRAND_HUE_MIN_CHROMA = 0.04
COMFORTABLE_DISTANCE = 30
COLLISION_DISTANCE = 15
DRIFT_PENALTY = 0.25


def _choose_hue(base, family, brand_hues):
    """Pick the hue inside the status family that keeps furthest from brand hues, preferring the base."""
    if not brand_hues:
        return base
    low, high = family

    def score(h):
        distance = min(hue_distance(h, b) for b in brand_hues)
        return min(distance, COMFORTABLE_DISTANCE) - DRIFT_PENALTY * abs(h - base)

    return max([base] + list(range(low, high + 1)), key=score)


def status_colors(brand_anchor_hexes):
    """Return (colors, notes). colors[name] holds the four values; notes explain hue moves and collisions."""
    brand_hues = []
    for hex_value in brand_anchor_hexes:
        _, C, H = hex_to_oklch(hex_value)
        if C >= BRAND_HUE_MIN_CHROMA:
            brand_hues.append(H)
    colors, notes = {}, []
    for name, ref in HARBOUR_STATUS.items():
        base = round(hex_to_oklch(ref["light"])[2])
        hue = _choose_hue(base, ref["family"], brand_hues)
        shift = hue - base
        colors[name] = {}
        for key in ("light", "light-soft", "dark", "dark-soft"):
            L, C, H = hex_to_oklch(ref[key])
            colors[name][key] = ref[key] if shift == 0 else oklch_to_hex(L, C, (H + shift) % 360)
        if shift:
            direction = ref["lower"] if shift < 0 else ref["higher"]
            notes.append(f"{name.capitalize()} hue moved {abs(shift)}° toward {direction} (OKLCH {base}° to {hue}°) to stay apart from the brand hues.")
        nearest = min((hue_distance(hue, b) for b in brand_hues), default=180)
        if nearest < COLLISION_DISTANCE:
            notes.append(
                f"{name.capitalize()} still sits within {nearest:.0f}° of a brand hue. Never signal {name} by colour alone: "
                "always pair it with its icon and a word, and keep brand-coloured buttons away from "
                f"{'destructive actions' if name == 'danger' else name + ' messages'}."
            )
    return colors, notes
