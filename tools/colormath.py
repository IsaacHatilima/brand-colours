"""Colour maths for the Kolors palette builder: sRGB, OKLab/OKLCH, WCAG contrast."""
import math


def hex_to_rgb(hex_value):
    value = hex_value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{round(max(0.0, min(1.0, c)) * 255):02X}" for c in rgb)


def _to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _from_linear(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def rgb_to_oklab(rgb):
    r, g, b = (_to_linear(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (math.copysign(abs(x) ** (1 / 3), x) for x in (l, m, s))
    return (
        0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
        1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
        0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s,
    )


def oklab_to_linear_rgb(lab):
    L, a, b = lab
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def hex_to_oklch(hex_value):
    L, a, b = rgb_to_oklab(hex_to_rgb(hex_value))
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def _in_gamut(linear):
    return all(-1e-6 <= c <= 1 + 1e-6 for c in linear)


def oklch_to_hex(L, C, H):
    """Convert OKLCH to HEX, reducing chroma until the colour fits in sRGB."""
    def lab(chroma):
        return (L, chroma * math.cos(math.radians(H)), chroma * math.sin(math.radians(H)))

    if not _in_gamut(oklab_to_linear_rgb(lab(C))):
        low, high = 0.0, C
        for _ in range(30):
            mid = (low + high) / 2
            if _in_gamut(oklab_to_linear_rgb(lab(mid))):
                low = mid
            else:
                high = mid
        C = low
    linear = oklab_to_linear_rgb(lab(C))
    return rgb_to_hex(tuple(_from_linear(max(0.0, min(1.0, c))) for c in linear))


def luminance(hex_value):
    r, g, b = (_to_linear(c) for c in hex_to_rgb(hex_value))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg, bg):
    a, b = luminance(fg), luminance(bg)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def hue_distance(h1, h2):
    d = abs(h1 - h2) % 360
    return min(d, 360 - d)


def grade(ratio):
    """WCAG text grade for a ratio."""
    if ratio >= 7:
        return "AAA"
    if ratio >= 4.5:
        return "AA"
    if ratio >= 3:
        return "AA large"
    return "fail"

