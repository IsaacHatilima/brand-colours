"""Contrast audit, logo-ground matrix and the accessible-pairing cards for a built system."""
from colormath import contrast, grade

TEXT_MIN = 4.5
NON_TEXT_MIN = 3.0
LOGO_MIN = 3.0

# (label, foreground token, background tokens, minimum)
_TEXT_AUDIT = [
    ("Body text", "text", ("bg", "surface", "surface-raised", "surface-sunken")),
    ("Muted text", "text-muted", ("bg", "surface", "surface-sunken")),
    ("Primary button label", "on-primary", ("primary", "primary-hover")),
    ("Accent button label", "on-accent", ("accent",)),
    ("Link", "link", ("bg", "surface", "primary-soft")),
    ("Link hover", "link-hover", ("bg", "surface")),
    ("Text on tinted fills", "text", ("primary-soft", "selection", "accent-soft")),
    ("Accent text on accent-soft", "accent", ("accent-soft",)),
    ("Info", "info", ("bg", "surface", "info-soft")),
]
_NON_TEXT_AUDIT = [
    ("Control border", "border-strong", ("bg", "surface")),
    ("Focus ring", "focus", ("bg", "surface")),
    ("Primary fill", "primary", ("bg", "surface")),
]
STATUSES = ("success", "warning", "danger")
CHART_TOKENS = ("chart-1", "chart-2", "chart-3", "chart-4", "chart-5", "chart-alt")


def audit(system):
    """Every documented pairing in both themes. Returns a list of result dicts."""
    rows = []
    for theme_name in ("light", "dark"):
        theme = system[theme_name]
        checks = [(label, fg, bgs, TEXT_MIN, "text") for label, fg, bgs in _TEXT_AUDIT]
        for status in STATUSES:
            checks.append((f"{status.capitalize()} text", status, ("bg", "surface", f"{status}-soft"), TEXT_MIN, "text"))
            checks.append((f"{status.capitalize()} label", f"on-{status}", (status,), TEXT_MIN, "text"))
        checks += [(label, fg, bgs, NON_TEXT_MIN, "non-text") for label, fg, bgs in _NON_TEXT_AUDIT]
        checks += [(f"Chart series {t}", t, ("surface",), NON_TEXT_MIN, "non-text") for t in CHART_TOKENS]
        for label, fg, bgs, minimum, kind in checks:
            for bg in bgs:
                ratio = contrast(theme[fg], theme[bg])
                rows.append({"theme": theme_name, "label": label, "fg": fg, "bg": bg, "ratio": ratio,
                             "minimum": minimum, "kind": kind, "passes": ratio >= minimum})
    return rows


def logo_matrix(spec, system):
    """Which logo colours hold 3:1 on which grounds, as in Harbour Signal's ground table."""
    paper = system["light"]["bg"]
    marks = [
        (spec["primary_color"]["name"], spec["primary_color"]["hex"]),
        (spec["accent_color"]["name"], spec["accent_color"]["hex"]),
        (spec["spark_color"]["name"], spec["spark_color"]["hex"]),
        (spec["ink_color"]["name"], spec["ink_color"]["hex"]),
        ("Paper", paper),
    ]
    grounds = [("Paper", paper), marks[3], marks[0], marks[1]]
    rows = []
    for mark_name, mark_hex in marks:
        cells = []
        for ground_name, ground_hex in grounds:
            if mark_hex == ground_hex:
                cells.append({"ground": ground_name, "same": True})
            else:
                ratio = contrast(mark_hex, ground_hex)
                cells.append({"ground": ground_name, "ratio": ratio, "passes": ratio >= LOGO_MIN, "same": False})
        rows.append({"mark": mark_name, "hex": mark_hex, "cells": cells})
    works_on = {
        ground_name: [row["mark"] for row in rows if not row["cells"][i]["same"] and row["cells"][i]["passes"]]
        for i, (ground_name, _) in enumerate(grounds)
    }
    return {"grounds": grounds, "rows": rows, "works_on": works_on}


def pairing_cards(system):
    """Harbour Signal's twelve showcase pairings: (title, theme, fg token, bg token, ratio, grade)."""
    cards = [
        ("Text on page", "light", "text", "bg"),
        ("Muted on page", "light", "text-muted", "bg"),
        ("Primary button", "light", "on-primary", "primary"),
        ("Accent button", "light", "on-accent", "accent"),
        ("Link on page", "light", "link", "bg"),
        ("Danger on soft", "light", "danger", "danger-soft"),
        ("Dark primary button", "dark", "on-primary", "primary"),
        ("Dark muted on surface", "dark", "text-muted", "surface"),
        ("Dark accent on page", "dark", "accent", "bg"),
        ("Dark success on surface", "dark", "success", "surface"),
        ("Dark danger on surface", "dark", "danger", "surface"),
        ("Dark warning on surface", "dark", "warning", "surface"),
    ]
    result = []
    for title, theme, fg, bg in cards:
        fg_hex, bg_hex = system[theme][fg], system[theme][bg]
        ratio = contrast(fg_hex, bg_hex)
        result.append({"title": title, "theme": theme, "fg": fg, "bg": bg, "fg_hex": fg_hex, "bg_hex": bg_hex,
                       "ratio": ratio, "grade": grade(ratio)})
    return result
