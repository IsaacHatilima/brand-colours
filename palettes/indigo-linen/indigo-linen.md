# Indigo Linen

![Indigo Linen colour system sheet](indigo-linen.png)

- Character: crafted, thoughtful, quietly bold
- Suggested uses: textiles, artisan homewares, boutique stationery
- Source: Rebuilt from the v1 palette Indigo Linen.
- Files: [CSS tokens](indigo-linen.css) · [JSON tokens](indigo-linen.tokens.json) · [Colour sheet](indigo-linen.png)

Brand colours: Indigo Velvet #52227F (primary), Sandpaper #D4B2A3 (accent). Charts: Sandpaper shades plus Indigo Velvet. Logo and icon only: Metallic Gold #E3B413 (spark), Violet Void #1B181D (ink).

## Brand colours

- Brand 1 · primary: [Indigo Velvet](../../colors/indigo-velvet.md) (#52227F, RGB 82, 34, 127), the primary scale's anchor at step 800. Light UI uses primary-800 (#52227F); dark UI uses primary-300 (#C9A0FD).
- Brand 2 · accent: [Sandpaper](../../colors/sandpaper.md) (#D4B2A3, RGB 212, 178, 163), the accent scale's anchor at step 300. Light UI uses accent-600 (#835B49); dark UI uses accent-300 (#D4B2A3).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #676567 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Metallic Gold and Violet Void never appear as UI colours.

- Spark: [Metallic Gold](../../colors/metallic-gold.md) (#E3B413). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Violet Void](../../colors/violet-void.md) (#1B181D). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Violet Void | Indigo Velvet | Sandpaper |
|---|---|---|---|---|
| Indigo Velvet | ✓ 10.6 | ✗ 1.6 | same | ✓ 5.6 |
| Sandpaper | ✗ 1.9 | ✓ 9.0 | ✓ 5.6 | same |
| Metallic Gold | ✗ 1.9 | ✓ 9.0 | ✓ 5.7 | ✗ 1.0 |
| Violet Void | ✓ 16.8 | same | ✗ 1.6 | ✓ 9.0 |
| Paper | same | ✓ 16.8 | ✓ 10.6 | ✗ 1.9 |

- On Paper: Indigo Velvet, Violet Void.
- On Violet Void: Sandpaper, Metallic Gold, Paper.
- On Indigo Velvet: Sandpaper, Metallic Gold, Paper.
- On Sandpaper: Indigo Velvet, Violet Void.

## Pairing rationale

Deep indigo leads and a soft clay-linen accent tempers it. The accent is deliberately quiet, so the indigo stays the hero; gold thread lights up the mark.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #1B181D | Page background: a plain off-white in light, the Violet Void ink in dark. Text on it uses `text` (16.8:1) and `text-muted` (5.5:1 light, 7.4:1 dark). |
| surface | #FFFFFF | #262328 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #302D33 | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F3F1F4 | #201D22 | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E4E2E5 | #3B383D | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #868587 | #7A767C | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #1B181D | #FAFAFA | Primary text and icons on every surface. Violet Void in light; the paper off-white in dark. |
| text-muted | #676567 | #A9A8AA | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #52227F | #C9A0FD | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Indigo Velvet (primary-800 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #311C48 | #DCC5FD | Hover and pressed fill of `primary`. |
| primary-soft | #F7F3FE | #52227F | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #1B181D | Text and icons on `primary` and `primary-hover` (11.1:1 light, 8.3:1 dark). Dark mode uses ink, not white. |
| link | #52227F | #DCC5FD | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #311C48 | #EDE2FD | Hover state of `link`. |
| accent | #835B49 | #D4B2A3 | The single secondary hue, Sandpaper: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F8F4F2 | #2F211B | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #1B181D | Text and icons on `accent` (5.9:1 light, 9.0:1 dark). |
| focus | #835B49 | #D4B2A3 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 5.7:1 on `bg` in light, 9.0:1 in dark. It uses the accent so it never blends into Indigo Velvet controls. |
| selection | #EDE2FD | #52227F | Text selection background. Text keeps `text`. |
| disabled-bg | #F3F1F4 | #302D33 | Fill of disabled buttons and inputs. |
| disabled-text | #868587 | #676567 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #21AA69 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #1B181D | Text on solid `success` fills. |
| warning | #8A5B00 | #EAA825 | Warning text, icons and fills (5.9:1 light, 7.5:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F8F0D9 | #29200A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #1B181D | Text on solid `warning` fills. |
| danger | #B82E42 | #E7727B | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #1B181D | Text on solid `danger` fills. |
| info | #52227F | #DCC5FD | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F7F3FE | #52227F | Background of info banners. Text on it uses `info`. |
| chart-1 | #835B49 | #D4B2A3 | Chart series 1, the anchor shade of Sandpaper. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #483329 | #EFE6E3 | Chart series 2, a darker Sandpaper in light and a lighter Sandpaper in dark. |
| chart-3 | #654739 | #A47560 | Chart series 3, a lighter Sandpaper in light and a deeper Sandpaper in dark. |
| chart-4 | #A47560 | #E2CFC6 | Chart series 4, a mid shade of Sandpaper. |
| chart-5 | #2F211B | #C0937F | Chart series 5, the remaining Sandpaper shade that still holds 3:1. |
| chart-alt | #52227F | #C9A0FD | The one contrasting chart series: Indigo Velvet, the primary brand colour. Chart colours are only Sandpaper shades and Indigo Velvet, never status or logo colours. |
| chart-grid | #E4E2E5 | #3B383D | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #1B181D | #1B181D | Raw near-black, Violet Void: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #E3B413 | #E3B413 | Logo and icon only: Metallic Gold, the highlight or signal dot. Never a UI colour. |
| logo-ink | #1B181D | #1B181D | Logo and icon only: wordmark and one-colour versions, Violet Void. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Indigo Velvet at primary-800, Sandpaper at accent-300. Identical in both themes.

| Step | Primary (Indigo Velvet) | Primary roles | Accent (Sandpaper) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F7F3FE | light: primary-soft | #F8F4F2 | light: accent-soft | #FAF8FB |
| 100 | #EDE2FD | light: selection; dark: link-hover | #EFE6E3 | dark: chart-2 | #F3F1F4 |
| 200 | #DCC5FD | dark: primary-hover, link | #E2CFC6 | dark: chart-4 | #E4E2E5 |
| 300 | #C9A0FD | dark: primary | #D4B2A3 | brand anchor; dark: accent, chart-1 | #CDCBCE |
| 400 | #B778FF |  | #C0937F | dark: chart-5 | #A9A8AA |
| 500 | #A154EE |  | #A47560 | light: chart-4; dark: chart-3 | #868587 |
| 600 | #833FC5 |  | #835B49 | light: accent, chart-1 | #676567 |
| 700 | #68379A |  | #654739 | light: chart-3 | #484748 |
| 800 | #52227F | brand anchor; light: primary, link; dark: primary-soft, selection | #483329 | light: chart-2 | #313031 |
| 900 | #311C48 | light: primary-hover, link-hover | #2F211B | light: chart-5; dark: accent-soft | #1C1B1D |
| 950 | #190E26 |  | #1A120F |  | #121213 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #1B181D on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #676567 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #52227F: **11.1:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #835B49: **5.9:1**, AA.
- Link on page (light): `link` #52227F on `bg` #FAFAFA: **10.6:1**, AAA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #1B181D on `primary` #C9A0FD: **8.3:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A9A8AA on `surface` #262328: **6.6:1**, AA.
- Dark accent on page (dark): `accent` #D4B2A3 on `bg` #1B181D: **9.0:1**, AAA.
- Dark success on surface (dark): `success` #21AA69 on `surface` #262328: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E7727B on `surface` #262328: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #EAA825 on `surface` #262328: **7.5:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Indigo Velvet and Sandpaper only. Metallic Gold and Violet Void are for the logo and icon, never for charts or UI.
- Charts use five shades of Sandpaper, plus Indigo Velvet as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Sandpaper itself sits at accent-300; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Sandpaper in the logo and large graphics.
- Warning hue moved 10° toward yellow (OKLCH 65° to 75°) to stay apart from the brand hues.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
