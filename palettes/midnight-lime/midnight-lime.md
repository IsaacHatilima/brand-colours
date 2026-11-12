# Midnight Lime

![Midnight Lime colour system sheet](midnight-lime.png)

- Character: technical, energetic, unconventional
- Suggested uses: developer tools, experimental music, digital exhibitions
- Source: Rebuilt from the v1 palette Midnight Lime.
- Files: [CSS tokens](midnight-lime.css) · [JSON tokens](midnight-lime.tokens.json) · [Colour sheet](midnight-lime.png)

Brand colours: Cyanophobia #042033 (primary), Tansy #CDC545 (accent). Charts: Tansy shades plus Cyanophobia. Logo and icon only: Tangerine Dream #F3946B (spark), River Styx #141A1F (ink).

## Brand colours

- Brand 1 · primary: [Cyanophobia](../../colors/cyanophobia.md) (#042033, RGB 4, 32, 51), the primary scale's anchor at step 900. Light UI uses primary-800 (#1F3343); dark UI uses primary-300 (#98B4CB).
- Brand 2 · accent: [Tansy](../../colors/tansy.md) (#CDC545, RGB 205, 197, 69), the accent scale's anchor at step 300. Light UI uses accent-600 (#716B00); dark UI uses accent-400 (#B1A700).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #646668 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Tangerine Dream and River Styx never appear as UI colours.

- Spark: [Tangerine Dream](../../colors/tangerine-dream.md) (#F3946B). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [River Styx](../../colors/river-styx.md) (#141A1F). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | River Styx | Cyanophobia | Tansy |
|---|---|---|---|---|
| Cyanophobia | ✓ 16.0 | ✗ 1.1 | same | ✓ 9.3 |
| Tansy | ✗ 1.7 | ✓ 9.7 | ✓ 9.3 | same |
| Tangerine Dream | ✗ 2.2 | ✓ 7.7 | ✓ 7.4 | ✗ 1.3 |
| River Styx | ✓ 16.8 | same | ✗ 1.1 | ✓ 9.7 |
| Paper | same | ✓ 16.8 | ✓ 16.0 | ✗ 1.7 |

- On Paper: Cyanophobia, River Styx.
- On River Styx: Tansy, Tangerine Dream, Paper.
- On Cyanophobia: Tansy, Tangerine Dream, Paper.
- On Tansy: Cyanophobia, River Styx.

## Pairing rationale

Near-black navy and acid lime are built for dark mode, where the lime accent glows. In light mode the lime deepens to olive to stay readable. Tangerine gives the mark a second signal.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #141A1F | Page background: a plain off-white in light, the River Styx ink in dark. Text on it uses `text` (16.8:1) and `text-muted` (5.5:1 light, 7.4:1 dark). |
| surface | #FFFFFF | #1F2529 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #2A2F34 | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F0F2F4 | #1A1F24 | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E1E3E5 | #343A3F | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #838587 | #72797E | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #141A1F | #FAFAFA | Primary text and icons on every surface. River Styx in light; the paper off-white in dark. |
| text-muted | #646668 | #A6A8AA | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #1F3343 | #98B4CB | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Cyanophobia (primary-800 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #042033 | #BFD0DE | Hover and pressed fill of `primary`. |
| primary-soft | #F2F6F8 | #1F3343 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #141A1F | Text and icons on `primary` and `primary-hover` (13.0:1 light, 8.1:1 dark). Dark mode uses ink, not white. |
| link | #1F3343 | #BFD0DE | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #042033 | #E0E8EE | Hover state of `link`. |
| accent | #716B00 | #B1A700 | The single secondary hue, Tansy: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F6F6EA | #292700 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #141A1F | Text and icons on `accent` (5.5:1 light, 7.0:1 dark). |
| focus | #716B00 | #B1A700 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 5.3:1 on `bg` in light, 7.0:1 in dark. It uses the accent so it never blends into Cyanophobia controls. |
| selection | #E0E8EE | #1F3343 | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F2F4 | #2A2F34 | Fill of disabled buttons and inputs. |
| disabled-text | #838587 | #646668 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #21AA69 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #141A1F | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.4:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #141A1F | Text on solid `warning` fills. |
| danger | #B8331E | #E77562 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.3:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #141A1F | Text on solid `danger` fills. |
| info | #1F3343 | #BFD0DE | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F2F6F8 | #1F3343 | Background of info banners. Text on it uses `info`. |
| chart-1 | #716B00 | #B1A700 | Chart series 1, the anchor shade of Tansy. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #3F3B00 | #DDDA9E | Chart series 2, a darker Tansy in light and a lighter Tansy in dark. |
| chart-3 | #585300 | #CDC545 | Chart series 3, a lighter Tansy in light and a deeper Tansy in dark. |
| chart-4 | #918900 | #918900 | Chart series 4, a mid shade of Tansy. |
| chart-5 | #292700 | #EDECD0 | Chart series 5, the remaining Tansy shade that still holds 3:1. |
| chart-alt | #1F3343 | #98B4CB | The one contrasting chart series: Cyanophobia, the primary brand colour. Chart colours are only Tansy shades and Cyanophobia, never status or logo colours. |
| chart-grid | #E1E3E5 | #343A3F | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #141A1F | #141A1F | Raw near-black, River Styx: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F3946B | #F3946B | Logo and icon only: Tangerine Dream, the highlight or signal dot. Never a UI colour. |
| logo-ink | #141A1F | #141A1F | Logo and icon only: wordmark and one-colour versions, River Styx. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Cyanophobia at primary-900, Tansy at accent-300. Identical in both themes.

| Step | Primary (Cyanophobia) | Primary roles | Accent (Tansy) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F2F6F8 | light: primary-soft | #F6F6EA | light: accent-soft | #F7F9FB |
| 100 | #E0E8EE | light: selection; dark: link-hover | #EDECD0 | dark: chart-5 | #F0F2F4 |
| 200 | #BFD0DE | dark: primary-hover, link | #DDDA9E | dark: chart-2 | #E1E3E5 |
| 300 | #98B4CB | dark: primary | #CDC545 | brand anchor; dark: chart-3 | #CACCCE |
| 400 | #6F9ABC |  | #B1A700 | dark: accent, chart-1 | #A6A8AA |
| 500 | #507EA1 |  | #918900 | light: chart-4; dark: chart-4 | #838587 |
| 600 | #39617F |  | #716B00 | light: accent, chart-1 | #646668 |
| 700 | #2D4A61 |  | #585300 | light: chart-3 | #464749 |
| 800 | #1F3343 | light: primary, link; dark: primary-soft, selection | #3F3B00 | light: chart-2 | #2F3032 |
| 900 | #042033 | brand anchor; light: primary-hover, link-hover | #292700 | light: chart-5; dark: accent-soft | #1B1C1D |
| 950 | #0E151B |  | #171500 |  | #111213 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #141A1F on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #646668 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #1F3343: **13.0:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #716B00: **5.5:1**, AA.
- Link on page (light): `link` #1F3343 on `bg` #FAFAFA: **12.5:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #141A1F on `primary` #98B4CB: **8.1:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A6A8AA on `surface` #1F2529: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #B1A700 on `bg` #141A1F: **7.0:1**, AAA.
- Dark success on surface (dark): `success` #21AA69 on `surface` #1F2529: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E77562 on `surface` #1F2529: **5.3:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #1F2529: **7.4:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Cyanophobia and Tansy only. Tangerine Dream and River Styx are for the logo and icon, never for charts or UI.
- Charts use five shades of Tansy, plus Cyanophobia as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Cyanophobia itself sits at primary-900; light-mode UI uses primary-800 so labels and text pass 4.5:1. Use the exact Cyanophobia in the logo and large graphics.
- Tansy itself sits at accent-300; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Tansy in the logo and large graphics.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
