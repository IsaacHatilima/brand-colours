# Terracotta Table

![Terracotta Table colour system sheet](terracotta-table.png)

- Character: warm, generous, artisanal
- Suggested uses: restaurants, ceramics, specialty food packaging
- Source: Rebuilt from the v1 palette Terracotta Table.
- Files: [CSS tokens](terracotta-table.css) · [JSON tokens](terracotta-table.tokens.json) · [Colour sheet](terracotta-table.png)

Brand colours: Grenadier #BF4C37 (primary), Olivenite #2C2E12 (accent). Charts: Olivenite shades plus Grenadier. Logo and icon only: Sunlit Clay #F7BB67 (spark), Nightshade Berries #1C1814 (ink).

## Brand colours

- Brand 1 · primary: [Grenadier](../../colors/grenadier.md) (#BF4C37, RGB 191, 76, 55), the primary scale's anchor at step 500. Light UI uses primary-500 (#BF4C37); dark UI uses primary-300 (#E39989).
- Brand 2 · accent: [Olivenite](../../colors/olivenite.md) (#2C2E12, RGB 44, 46, 18), the accent scale's anchor at step 900. Light UI uses accent-700 (#535637); dark UI uses accent-300 (#B5B99B).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #676664 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Sunlit Clay and Nightshade Berries never appear as UI colours.

- Spark: [Sunlit Clay](../../colors/sunlit-clay.md) (#F7BB67). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Nightshade Berries](../../colors/nightshade-berries-1c1814.md) (#1C1814). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Nightshade Berries | Grenadier | Olivenite |
|---|---|---|---|---|
| Grenadier | ✓ 4.7 | ✓ 3.6 | same | ✗ 2.9 |
| Olivenite | ✓ 13.4 | ✗ 1.3 | ✗ 2.9 | same |
| Sunlit Clay | ✗ 1.6 | ✓ 10.3 | ✗ 2.8 | ✓ 8.1 |
| Nightshade Berries | ✓ 16.9 | same | ✓ 3.6 | ✗ 1.3 |
| Paper | same | ✓ 16.9 | ✓ 4.7 | ✓ 13.4 |

- On Paper: Grenadier, Olivenite, Nightshade Berries.
- On Nightshade Berries: Grenadier, Sunlit Clay, Paper.
- On Grenadier: Nightshade Berries, Paper.
- On Olivenite: Sunlit Clay, Paper.

## Pairing rationale

Brick terracotta and dark olive set the table; the olive accent is deliberately deep, like oil and herbs against clay. Sunlit clay gives the mark its glow.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #1C1814 | Page background: a plain off-white in light, the Nightshade Berries ink in dark. Text on it uses `text` (16.9:1) and `text-muted` (5.5:1 light, 7.4:1 dark). |
| surface | #FFFFFF | #27231F | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #322D29 | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F4F2F0 | #211D19 | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E5E3E1 | #3C3833 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #878583 | #7C7772 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #1C1814 | #FAFAFA | Primary text and icons on every surface. Nightshade Berries in light; the paper off-white in dark. |
| text-muted | #676664 | #AAA8A6 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #BF4C37 | #E39989 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Grenadier (primary-500 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #9A3826 | #EEC0B6 | Hover and pressed fill of `primary`. |
| primary-soft | #FCF3F1 | #562319 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #1C1814 | Text and icons on `primary` and `primary-hover` (4.9:1 light, 7.7:1 dark). Dark mode uses ink, not white. |
| link | #9A3826 | #EEC0B6 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #782E21 | #F6E0DC | Hover state of `link`. |
| accent | #535637 | #B5B99B | The single secondary hue, Olivenite: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F5F5F2 | #2C2E12 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #1C1814 | Text and icons on `accent` (7.6:1 light, 8.7:1 dark). |
| focus | #535637 | #B5B99B | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 7.3:1 on `bg` in light, 8.7:1 in dark. It uses the accent so it never blends into Grenadier controls. |
| selection | #F6E0DC | #562319 | Text selection background. Text keeps `text`. |
| disabled-bg | #F4F2F0 | #322D29 | Fill of disabled buttons and inputs. |
| disabled-text | #878583 | #676664 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #21AA69 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #1C1814 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.4:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #1C1814 | Text on solid `warning` fills. |
| danger | #B82E42 | #E7727B | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.3:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #1C1814 | Text on solid `danger` fills. |
| info | #9A3826 | #EEC0B6 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #FCF3F1 | #562319 | Background of info banners. Text on it uses `info`. |
| chart-1 | #535637 | #B5B99B | Chart series 1, the anchor shade of Olivenite. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #2C2E12 | #E7E8E0 | Chart series 2, a darker Olivenite in light and a lighter Olivenite in dark. |
| chart-3 | #828656 | #828656 | Chart series 3, a lighter Olivenite in light and a deeper Olivenite in dark. |
| chart-4 | #3E402A | #D0D2C0 | Chart series 4, a mid shade of Olivenite. |
| chart-5 | #686B42 | #9CA074 | Chart series 5, the remaining Olivenite shade that still holds 3:1. |
| chart-alt | #BF4C37 | #E39989 | The one contrasting chart series: Grenadier, the primary brand colour. Chart colours are only Olivenite shades and Grenadier, never status or logo colours. |
| chart-grid | #E5E3E1 | #3C3833 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #1C1814 | #1C1814 | Raw near-black, Nightshade Berries: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F7BB67 | #F7BB67 | Logo and icon only: Sunlit Clay, the highlight or signal dot. Never a UI colour. |
| logo-ink | #1C1814 | #1C1814 | Logo and icon only: wordmark and one-colour versions, Nightshade Berries. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Grenadier at primary-500, Olivenite at accent-900. Identical in both themes.

| Step | Primary (Grenadier) | Primary roles | Accent (Olivenite) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #FCF3F1 | light: primary-soft | #F5F5F2 | light: accent-soft | #FBF9F7 |
| 100 | #F6E0DC | light: selection; dark: link-hover | #E7E8E0 | dark: chart-2 | #F4F2F0 |
| 200 | #EEC0B6 | dark: primary-hover, link | #D0D2C0 | dark: chart-4 | #E5E3E1 |
| 300 | #E39989 | dark: primary | #B5B99B | dark: accent, chart-1 | #CECCCA |
| 400 | #DB6E59 |  | #9CA074 | dark: chart-5 | #AAA8A6 |
| 500 | #BF4C37 | brand anchor; light: primary | #828656 | light: chart-3; dark: chart-3 | #878583 |
| 600 | #9A3826 | light: primary-hover, link | #686B42 | light: chart-5 | #676664 |
| 700 | #782E21 | light: link-hover | #535637 | light: accent, chart-1 | #484745 |
| 800 | #562319 | dark: primary-soft, selection | #3E402A | light: chart-4 | #31302E |
| 900 | #3A1812 |  | #2C2E12 | brand anchor; light: chart-2; dark: accent-soft | #1D1C1A |
| 950 | #210F0B |  | #14150E |  | #131210 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #1C1814 on `bg` #FAFAFA: **16.9:1**, AAA.
- Muted on page (light): `text-muted` #676664 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #BF4C37: **4.9:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #535637: **7.6:1**, AAA.
- Link on page (light): `link` #9A3826 on `bg` #FAFAFA: **6.8:1**, AA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #1C1814 on `primary` #E39989: **7.7:1**, AAA.
- Dark muted on surface (dark): `text-muted` #AAA8A6 on `surface` #27231F: **6.6:1**, AA.
- Dark accent on page (dark): `accent` #B5B99B on `bg` #1C1814: **8.7:1**, AAA.
- Dark success on surface (dark): `success` #21AA69 on `surface` #27231F: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E7727B on `surface` #27231F: **5.3:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #27231F: **7.4:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Grenadier and Olivenite only. Sunlit Clay and Nightshade Berries are for the logo and icon, never for charts or UI.
- Charts use five shades of Olivenite, plus Grenadier as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Olivenite itself sits at accent-900; light-mode UI uses accent-700 so labels and text pass 4.5:1. Use the exact Olivenite in the logo and large graphics.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.
- Danger still sits within 14° of a brand hue. Never signal danger by colour alone: always pair it with its icon and a word, and keep brand-coloured buttons away from destructive actions.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
