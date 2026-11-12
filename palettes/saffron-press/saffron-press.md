# Saffron Press

![Saffron Press colour system sheet](saffron-press.png)

- Character: graphic, warm, decisive
- Suggested uses: independent publishing, cultural events, food journals
- Source: Rebuilt from the v1 palette Saffron Press.
- Files: [CSS tokens](saffron-press.css) · [JSON tokens](saffron-press.tokens.json) · [Colour sheet](saffron-press.png)

Brand colours: Goldenrod #D0970C (primary), Baltic Blue #0A6187 (accent). Charts: Baltic Blue shades plus Goldenrod. Logo and icon only: Tangerine Dream #F3946B (spark), Sinister #13120E (ink).

## Brand colours

- Brand 1 · primary: [Goldenrod](../../colors/goldenrod.md) (#D0970C, RGB 208, 151, 12), the primary scale's anchor at step 400. Light UI uses primary-600 (#876000); dark UI uses primary-400 (#D0970C).
- Brand 2 · accent: [Baltic Blue](../../colors/baltic-blue.md) (#0A6187, RGB 10, 97, 135), the accent scale's anchor at step 600. Light UI uses accent-600 (#0A6187); dark UI uses accent-300 (#86B6D3).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #676664 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Tangerine Dream and Sinister never appear as UI colours.

- Spark: [Tangerine Dream](../../colors/tangerine-dream.md) (#F3946B). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Sinister](../../colors/sinister.md) (#13120E). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Sinister | Goldenrod | Baltic Blue |
|---|---|---|---|---|
| Goldenrod | ✗ 2.5 | ✓ 7.2 | same | ✗ 2.6 |
| Baltic Blue | ✓ 6.5 | ✗ 2.7 | ✗ 2.6 | same |
| Tangerine Dream | ✗ 2.2 | ✓ 8.3 | ✗ 1.1 | ✓ 3.0 |
| Sinister | ✓ 18.0 | same | ✓ 7.2 | ✗ 2.7 |
| Paper | same | ✓ 18.0 | ✗ 2.5 | ✓ 6.5 |

- On Paper: Baltic Blue, Sinister.
- On Sinister: Goldenrod, Tangerine Dream, Paper.
- On Goldenrod: Sinister.
- On Baltic Blue: Tangerine Dream, Paper.

## Pairing rationale

Goldenrod leads; in light mode it deepens to an ochre that can carry white labels. A Baltic blue from the library is the cool counterweight for focus and highlights. Tangerine warms the mark.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #13120E | Page background: a plain off-white in light, the Sinister ink in dark. Text on it uses `text` (18.0:1) and `text-muted` (5.5:1 light, 7.9:1 dark). |
| surface | #FFFFFF | #1D1C18 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #282722 | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F3F2EF | #181713 | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E4E3E1 | #32312C | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #868583 | #71706A | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.4:1 dark on surface). |
| text | #13120E | #FAFAFA | Primary text and icons on every surface. Sinister in light; the paper off-white in dark. |
| text-muted | #676664 | #A9A8A6 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #876000 | #D0970C | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Goldenrod (primary-600 light, primary-400 dark). Label text on it uses `on-primary`. |
| primary-hover | #6A4B00 | #DAB471 | Hover and pressed fill of `primary`. |
| primary-soft | #F9F4ED | #4C3500 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #13120E | Text and icons on `primary` and `primary-hover` (5.7:1 light, 7.2:1 dark). Dark mode uses ink, not white. |
| link | #6A4B00 | #DAB471 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #4C3500 | #E6D0A9 | Hover state of `link`. |
| accent | #0A6187 | #86B6D3 | The single secondary hue, Baltic Blue: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F0F6F9 | #0E2633 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #13120E | Text and icons on `accent` (6.8:1 light, 8.6:1 dark). |
| focus | #0A6187 | #86B6D3 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.5:1 on `bg` in light, 8.6:1 in dark. It uses the accent so it never blends into Goldenrod controls. |
| selection | #F2E7D6 | #4C3500 | Text selection background. Text keeps `text`. |
| disabled-bg | #F3F2EF | #282722 | Fill of disabled buttons and inputs. |
| disabled-text | #868583 | #676664 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1BA766 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.5:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #13120E | Text on solid `success` fills. |
| warning | #975022 | #FF984D | Warning text, icons and fills (6.0:1 light, 8.0:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FFEDDA | #2E1D0C | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #13120E | Text on solid `warning` fills. |
| danger | #B8331E | #E57361 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.6:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #13120E | Text on solid `danger` fills. |
| info | #6A4B00 | #DAB471 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F9F4ED | #4C3500 | Background of info banners. Text on it uses `info`. |
| chart-1 | #0A6187 | #86B6D3 | Chart series 1, the anchor shade of Baltic Blue. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #11384C | #DBE8F0 | Chart series 2, a darker Baltic Blue in light and a lighter Baltic Blue in dark. |
| chart-3 | #4F9CC6 | #237FAC | Chart series 3, a lighter Baltic Blue in light and a deeper Baltic Blue in dark. |
| chart-4 | #124C69 | #B5D1E2 | Chart series 4, a mid shade of Baltic Blue. |
| chart-5 | #237FAC | #4F9CC6 | Chart series 5, the remaining Baltic Blue shade that still holds 3:1. |
| chart-alt | #876000 | #D0970C | The one contrasting chart series: Goldenrod, the primary brand colour. Chart colours are only Baltic Blue shades and Goldenrod, never status or logo colours. |
| chart-grid | #E4E3E1 | #32312C | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #13120E | #13120E | Raw near-black, Sinister: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F3946B | #F3946B | Logo and icon only: Tangerine Dream, the highlight or signal dot. Never a UI colour. |
| logo-ink | #13120E | #13120E | Logo and icon only: wordmark and one-colour versions, Sinister. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Goldenrod at primary-400, Baltic Blue at accent-600. Identical in both themes.

| Step | Primary (Goldenrod) | Primary roles | Accent (Baltic Blue) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F9F4ED | light: primary-soft | #F0F6F9 | light: accent-soft | #FAF9F6 |
| 100 | #F2E7D6 | light: selection | #DBE8F0 | dark: chart-2 | #F3F2EF |
| 200 | #E6D0A9 | dark: link-hover | #B5D1E2 | dark: chart-4 | #E4E3E1 |
| 300 | #DAB471 | dark: primary-hover, link | #86B6D3 | dark: accent, chart-1 | #CDCCCA |
| 400 | #D0970C | brand anchor; dark: primary | #4F9CC6 | light: chart-3; dark: chart-5 | #A9A8A6 |
| 500 | #AC7B00 |  | #237FAC | light: chart-5; dark: chart-3 | #868583 |
| 600 | #876000 | light: primary | #0A6187 | brand anchor; light: accent, chart-1 | #676664 |
| 700 | #6A4B00 | light: primary-hover, link | #124C69 | light: chart-4 | #484745 |
| 800 | #4C3500 | light: link-hover; dark: primary-soft, selection | #11384C | light: chart-2 | #30302E |
| 900 | #332200 |  | #0E2633 | dark: accent-soft | #1C1C1A |
| 950 | #1C1303 |  | #0A161D |  | #121210 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #13120E on `bg` #FAFAFA: **18.0:1**, AAA.
- Muted on page (light): `text-muted` #676664 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #876000: **5.7:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #0A6187: **6.8:1**, AA.
- Link on page (light): `link` #6A4B00 on `bg` #FAFAFA: **7.7:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #13120E on `primary` #D0970C: **7.2:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A9A8A6 on `surface` #1D1C18: **7.2:1**, AAA.
- Dark accent on page (dark): `accent` #86B6D3 on `bg` #13120E: **8.6:1**, AAA.
- Dark success on surface (dark): `success` #1BA766 on `surface` #1D1C18: **5.5:1**, AA.
- Dark danger on surface (dark): `danger` #E57361 on `surface` #1D1C18: **5.6:1**, AA.
- Dark warning on surface (dark): `warning` #FF984D on `surface` #1D1C18: **8.0:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Goldenrod and Baltic Blue only. Tangerine Dream and Sinister are for the logo and icon, never for charts or UI.
- Charts use five shades of Baltic Blue, plus Goldenrod as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-400, links to primary-300, and button labels turn ink.
- Goldenrod itself sits at primary-400; light-mode UI uses primary-600 so labels and text pass 4.5:1. Use the exact Goldenrod in the logo and large graphics.
- Warning hue moved 14° toward orange (OKLCH 65° to 51°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
