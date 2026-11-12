"""Plain-language 'Use' descriptions for each semantic token, with live contrast figures."""
from colormath import contrast


def _r(fg, bg):
    return f"{contrast(fg, bg):.1f}:1"


def token_uses(system, names):
    """Return {token: description}. `names` maps primary/accent/spark/ink to colour names."""
    L, D = system["light"], system["dark"]
    steps = system["steps"]
    p, a = names["primary"], names["accent"]
    return {
        "bg": f"Page background: a plain off-white in light, the {names['ink']} ink in dark. Text on it uses `text` ({_r(L['text'], L['bg'])}) and `text-muted` ({_r(L['text-muted'], L['bg'])} light, {_r(D['text-muted'], D['bg'])} dark).",
        "surface": "Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`.",
        "surface-raised": "Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`.",
        "surface-sunken": "Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`.",
        "border": "Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that.",
        "border-strong": f"Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes ({_r(L['border-strong'], L['bg'])} light, {_r(D['border-strong'], D['surface'])} dark on surface).",
        "text": f"Primary text and icons on every surface. {names['ink']} in light; the paper off-white in dark.",
        "text-muted": "Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`.",
        "primary": f"Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: {p} (primary-{steps['light-primary']} light, primary-{steps['dark-primary']} dark). Label text on it uses `on-primary`.",
        "primary-hover": "Hover and pressed fill of `primary`.",
        "primary-soft": "Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`.",
        "on-primary": f"Text and icons on `primary` and `primary-hover` ({_r(L['on-primary'], L['primary'])} light, {_r(D['on-primary'], D['primary'])} dark). Dark mode uses ink, not white.",
        "link": "Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text.",
        "link-hover": "Hover state of `link`.",
        "accent": f"The single secondary hue, {a}: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`.",
        "accent-soft": "Tinted background for accent badges and callouts. Text on it uses `accent`.",
        "on-accent": f"Text and icons on `accent` ({_r(L['on-accent'], L['accent'])} light, {_r(D['on-accent'], D['accent'])} dark).",
        "focus": f"Keyboard focus ring: 2px solid with a 2px gap in `bg`. {_r(L['focus'], L['bg'])} on `bg` in light, {_r(D['focus'], D['bg'])} in dark. It uses the accent so it never blends into {p} controls.",
        "selection": "Text selection background. Text keeps `text`.",
        "disabled-bg": "Fill of disabled buttons and inputs.",
        "disabled-text": "Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here.",
        "success": f"Success text, icons and fills on `bg`, `surface` and `success-soft` ({_r(L['success'], L['surface'])} light, {_r(D['success'], D['surface'])} dark on `surface`). Always paired with a check icon and a word.",
        "success-soft": "Background of success banners and badges. Text on it uses `success`.",
        "on-success": "Text on solid `success` fills.",
        "warning": f"Warning text, icons and fills ({_r(L['warning'], L['surface'])} light, {_r(D['warning'], D['surface'])} dark on `surface`). Always paired with a triangle icon and a word.",
        "warning-soft": "Background of warning banners and badges. Text on it uses `warning`.",
        "on-warning": "Text on solid `warning` fills.",
        "danger": f"Errors and destructive actions: text, icons, fills ({_r(L['danger'], L['surface'])} light, {_r(D['danger'], D['surface'])} dark on `surface`). Always paired with an icon and a word.",
        "danger-soft": "Background of error banners and field errors. Text on it uses `danger`.",
        "on-danger": "Text on solid `danger` fills.",
        "info": "Informational text and icons. Deliberately the brand hue, so there is no separate blue.",
        "info-soft": "Background of info banners. Text on it uses `info`.",
        "chart-1": f"Chart series 1, the anchor shade of {a}. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series.",
        "chart-2": f"Chart series 2, a darker {a} in light and a lighter {a} in dark.",
        "chart-3": f"Chart series 3, a lighter {a} in light and a deeper {a} in dark.",
        "chart-4": f"Chart series 4, a mid shade of {a}.",
        "chart-5": f"Chart series 5, the remaining {a} shade that still holds 3:1.",
        "chart-alt": f"The one contrasting chart series: {p}, the primary brand colour. Chart colours are only {a} shades and {p}, never status or logo colours.",
        "chart-grid": "Gridlines and axis rules inside charts. Axis labels use `text-muted`.",
        "ink": f"Raw near-black, {names['ink']}: the light theme's text and the dark theme's page background. Use the semantic tokens in UI.",
        "logo-spark": f"Logo and icon only: {names['spark']}, the highlight or signal dot. Never a UI colour.",
        "logo-ink": f"Logo and icon only: wordmark and one-colour versions, {names['ink']}.",
    }


SEMANTIC_ORDER = (
    "bg", "surface", "surface-raised", "surface-sunken", "border", "border-strong", "text", "text-muted",
    "primary", "primary-hover", "primary-soft", "on-primary", "link", "link-hover", "accent", "accent-soft",
    "on-accent", "focus", "selection", "disabled-bg", "disabled-text", "success", "success-soft", "on-success",
    "warning", "warning-soft", "on-warning", "danger", "danger-soft", "on-danger", "info", "info-soft",
    "chart-1", "chart-2", "chart-3", "chart-4", "chart-5", "chart-alt", "chart-grid", "ink", "logo-spark", "logo-ink",
)
