"""Tonal scales (50-950) generated from a library anchor colour, modelled on Harbour Signal."""
from colormath import hex_to_oklch, oklch_to_hex, luminance

STEPS = (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950)

# OKLCH lightness per step: the average of Harbour Signal's Petrol and Dusk scales.
BRAND_L = (0.970, 0.927, 0.853, 0.765, 0.679, 0.589, 0.495, 0.418, 0.336, 0.261, 0.193)

# Harbour Signal's plain grey ramp.
NEUTRAL_L = (0.982, 0.961, 0.916, 0.845, 0.732, 0.617, 0.510, 0.398, 0.309, 0.226, 0.182)

# Chroma per step as a share of the scale's peak, fitted to Harbour Signal's Petrol and Dusk scales.
CHROMA_SHARE = (0.07, 0.165, 0.36, 0.61, 0.92, 1.0, 0.89, 0.70, 0.52, 0.36, 0.215)
# A muted anchor keeps a muted scale: the peak may not exceed the anchor's chroma by more than this.
MAX_PEAK_BOOST = 1.5
# Greys stay visibly plain; the ink's hue only nudges them below the threshold of notice.
NEUTRAL_TINT_LIMIT = 0.0035
DARK_SURFACE_TINT_LIMIT = 0.012
PAPER = "#FAFAFA"


def _stretched_lightness(anchor_L, anchor_index):
    """Stretch BRAND_L so the anchor step lands exactly on the anchor's lightness."""
    top, bottom, target = BRAND_L[0], BRAND_L[-1], BRAND_L[anchor_index]
    result = []
    for i, base in enumerate(BRAND_L):
        if i == anchor_index:
            result.append(anchor_L)
        elif i < anchor_index:
            result.append(top + (base - top) * (anchor_L - top) / (target - top))
        else:
            result.append(bottom + (base - bottom) * (anchor_L - bottom) / (target - bottom))
    return result


def brand_scale(anchor_hex):
    """Return (scale, anchor_step). scale maps step -> HEX; the anchor step holds the exact anchor."""
    L, C, H = hex_to_oklch(anchor_hex)
    anchor_index = min(range(len(STEPS)), key=lambda i: abs(BRAND_L[i] - L))
    anchor_index = min(max(anchor_index, 1), len(STEPS) - 2)
    peak = min(C / CHROMA_SHARE[anchor_index], C * MAX_PEAK_BOOST)
    scale = {}
    for i, step_L in enumerate(_stretched_lightness(L, anchor_index)):
        if i == anchor_index:
            scale[STEPS[i]] = anchor_hex.upper()
            continue
        scale[STEPS[i]] = oklch_to_hex(step_L, peak * CHROMA_SHARE[i], H)
    _assert_monotonic(scale, anchor_hex)
    return scale, STEPS[anchor_index]


def neutral_scale(ink_hex):
    """Plain greys, tinted only by the ink's hue at a barely visible chroma."""
    _, C, H = hex_to_oklch(ink_hex)
    tint = min(C, NEUTRAL_TINT_LIMIT)
    scale = {step: oklch_to_hex(L, tint, H) for step, L in zip(STEPS, NEUTRAL_L)}
    _assert_monotonic(scale, ink_hex)
    return scale


def ink_relative(ink_hex, lightness_offset, tint_limit=DARK_SURFACE_TINT_LIMIT):
    """A dark-theme surface: the ink lifted by a lightness offset, keeping its hue."""
    L, C, H = hex_to_oklch(ink_hex)
    return oklch_to_hex(L + lightness_offset, min(C, tint_limit), H)


def paper(ink_hex):
    """Light-theme page background: Harbour Signal's plain off-white, whatever the ink."""
    return PAPER


def _assert_monotonic(scale, source):
    values = [luminance(scale[step]) for step in STEPS]
    if any(later >= earlier for earlier, later in zip(values, values[1:])):
        raise ValueError(f"Scale from {source} is not strictly darkening: {scale}")
