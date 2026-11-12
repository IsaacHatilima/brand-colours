"""Load and validate palette specs against the colour library."""
import json, math
from pathlib import Path
from colormath import hex_to_oklch, contrast, hue_distance, rgb_to_oklab, hex_to_rgb

SPEC_PATH = Path(__file__).resolve().parent / "palette_specs.json"
ROLES = ("primary", "accent", "spark", "ink")
MIN_BRAND_HUE_GAP = 35
# Harbour Signal's own pair is 0.14 apart in dark mode.
MIN_UI_DISTANCE = 0.09
NEAR_DUPLICATE = 0.06
INK_MAX_L = 0.23
SPARK_MIN_ON_INK = 3.0


def oklab_distance(a, b):
    return math.dist(rgb_to_oklab(hex_to_rgb(a)), rgb_to_oklab(hex_to_rgb(b)))


def load_specs(library):
    specs = json.loads(SPEC_PATH.read_text())
    slugs = [s["slug"] for s in specs]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Duplicate palette slugs in specs")
    resolved = []
    for spec in specs:
        missing = [spec[r] for r in ROLES if spec[r] not in library]
        if missing:
            raise ValueError(f"{spec['slug']}: unknown colour files {missing}")
        resolved.append({**spec, **{f"{r}_color": library[spec[r]] for r in ROLES}})
    return resolved


def spec_problems(spec, system):
    """Design-rule problems for one spec, given its built system."""
    p, a = spec["primary_color"]["hex"], spec["accent_color"]["hex"]
    spark, ink = spec["spark_color"]["hex"], spec["ink_color"]["hex"]
    problems = []
    _, pc, ph = hex_to_oklch(p)
    _, ac, ah = hex_to_oklch(a)
    if pc >= 0.02 and hue_distance(ph, ah) < MIN_BRAND_HUE_GAP:
        problems.append(f"primary and accent hues only {hue_distance(ph, ah):.0f}° apart")
    if oklab_distance(system["light"]["primary"], system["light"]["accent"]) < MIN_UI_DISTANCE:
        problems.append("light primary and accent look too alike")
    if oklab_distance(system["dark"]["primary"], system["dark"]["accent"]) < MIN_UI_DISTANCE:
        problems.append("dark primary and accent look too alike")
    if hex_to_oklch(ink)[0] > INK_MAX_L:
        problems.append("ink is not dark enough")
    if contrast(spark, ink) < SPARK_MIN_ON_INK:
        problems.append("spark under 3:1 on ink")
    return problems


def duplicate_pairs(specs):
    found = []
    for i, x in enumerate(specs):
        for y in specs[i + 1:]:
            if (oklab_distance(x["primary_color"]["hex"], y["primary_color"]["hex"]) < NEAR_DUPLICATE
                    and oklab_distance(x["accent_color"]["hex"], y["accent_color"]["hex"]) < NEAR_DUPLICATE):
                found.append((x["slug"], y["slug"]))
    return found
