# Forest Ledger

![Forest Ledger colour system sheet](forest-ledger.png)

- Character: grounded, trustworthy, restrained
- Suggested uses: sustainable finance, conservation, outdoor services
- Source: Rebuilt from the v1 palette Forest Ledger.
- Files: [CSS tokens](forest-ledger.css) · [JSON tokens](forest-ledger.tokens.json) · [Colour sheet](forest-ledger.png)

Brand colours: Government Green #34463F (primary), Sienna #AD581E (accent). Charts: Sienna shades plus Government Green. Logo and icon only: Cane Sugar #E2BA80 (spark), Dark Moon #141B17 (ink).

## Brand colours

- Brand 1 · primary: [Government Green](../../colors/government-green.md) (#34463F, RGB 52, 70, 63), the primary scale's anchor at step 800. Light UI uses primary-800 (#34463F); dark UI uses primary-300 (#A9BCB4).
- Brand 2 · accent: [Sienna](../../colors/sienna.md) (#AD581E, RGB 173, 88, 30), the accent scale's anchor at step 500. Light UI uses accent-500 (#AD581E); dark UI uses accent-300 (#D69F7F).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #646765 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Cane Sugar and Dark Moon never appear as UI colours.

- Spark: [Cane Sugar](../../colors/cane-sugar.md) (#E2BA80). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Dark Moon](../../colors/dark-moon.md) (#141B17). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Dark Moon | Government Green | Sienna |
|---|---|---|---|---|
| Government Green | ✓ 9.6 | ✗ 1.7 | same | ✗ 2.0 |
| Sienna | ✓ 4.8 | ✓ 3.5 | ✗ 2.0 | same |
| Cane Sugar | ✗ 1.7 | ✓ 9.6 | ✓ 5.5 | ✗ 2.8 |
| Dark Moon | ✓ 16.8 | same | ✗ 1.7 | ✓ 3.5 |
| Paper | same | ✓ 16.8 | ✓ 9.6 | ✓ 4.8 |

- On Paper: Government Green, Sienna, Dark Moon.
- On Dark Moon: Sienna, Cane Sugar, Paper.
- On Government Green: Cane Sugar, Paper.
- On Sienna: Dark Moon, Paper.

## Pairing rationale

A muted forest green keeps the interface restrained. Royal Oakleaf was too close in hue and too soft to act as an accent, so a sienna from the library takes that role, like copper fittings on a ledger. Cane sugar is the warm mark highlight.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #141B17 | Page background: a plain off-white in light, the Dark Moon ink in dark. Text on it uses `text` (16.8:1) and `text-muted` (5.5:1 light, 7.4:1 dark). |
| surface | #FFFFFF | #1F2622 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #29302C | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F0F3F1 | #1A201C | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E1E4E2 | #343B37 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #838684 | #727A75 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #141B17 | #FAFAFA | Primary text and icons on every surface. Dark Moon in light; the paper off-white in dark. |
| text-muted | #646765 | #A6A9A7 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #34463F | #A9BCB4 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Government Green (primary-800 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #222B28 | #C9D4CF | Hover and pressed fill of `primary`. |
| primary-soft | #F3F6F5 | #34463F | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #141B17 | Text and icons on `primary` and `primary-hover` (10.0:1 light, 8.8:1 dark). Dark mode uses ink, not white. |
| link | #34463F | #C9D4CF | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #222B28 | #E4E9E7 | Hover state of `link`. |
| accent | #AD581E | #D69F7F | The single secondary hue, Sienna: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FBF3F0 | #351C0D | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #141B17 | Text and icons on `accent` (5.0:1 light, 7.6:1 dark). |
| focus | #AD581E | #D69F7F | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 4.8:1 on `bg` in light, 7.6:1 in dark. It uses the accent so it never blends into Government Green controls. |
| selection | #E4E9E7 | #34463F | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F3F1 | #29302C | Fill of disabled buttons and inputs. |
| disabled-text | #838684 | #646765 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #21AA69 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #141B17 | Text on solid `success` fills. |
| warning | #855E00 | #E3AC1F | Warning text, icons and fills (5.8:1 light, 7.5:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F5F1D9 | #27210A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #141B17 | Text on solid `warning` fills. |
| danger | #B82F3E | #E77277 | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E8 | #2E1516 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #141B17 | Text on solid `danger` fills. |
| info | #34463F | #C9D4CF | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F3F6F5 | #34463F | Background of info banners. Text on it uses `info`. |
| chart-1 | #AD581E | #D69F7F | Chart series 1, the anchor shade of Sienna. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #6D3612 | #F2E2D9 | Chart series 2, a darker Sienna in light and a lighter Sienna in dark. |
| chart-3 | #8C430E | #AD581E | Chart series 3, a lighter Sienna in light and a deeper Sienna in dark. |
| chart-4 | #C97848 | #E5C3B0 | Chart series 4, a mid shade of Sienna. |
| chart-5 | #4F2810 | #C97848 | Chart series 5, the remaining Sienna shade that still holds 3:1. |
| chart-alt | #34463F | #A9BCB4 | The one contrasting chart series: Government Green, the primary brand colour. Chart colours are only Sienna shades and Government Green, never status or logo colours. |
| chart-grid | #E1E4E2 | #343B37 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #141B17 | #141B17 | Raw near-black, Dark Moon: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #E2BA80 | #E2BA80 | Logo and icon only: Cane Sugar, the highlight or signal dot. Never a UI colour. |
| logo-ink | #141B17 | #141B17 | Logo and icon only: wordmark and one-colour versions, Dark Moon. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Government Green at primary-800, Sienna at accent-500. Identical in both themes.

| Step | Primary (Government Green) | Primary roles | Accent (Sienna) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F3F6F5 | light: primary-soft | #FBF3F0 | light: accent-soft | #F7FAF8 |
| 100 | #E4E9E7 | light: selection; dark: link-hover | #F2E2D9 | dark: chart-2 | #F0F3F1 |
| 200 | #C9D4CF | dark: primary-hover, link | #E5C3B0 | dark: chart-4 | #E1E4E2 |
| 300 | #A9BCB4 | dark: primary | #D69F7F | dark: accent, chart-1 | #CACDCB |
| 400 | #89A59A |  | #C97848 | light: chart-4; dark: chart-5 | #A6A9A7 |
| 500 | #6E8C80 |  | #AD581E | brand anchor; light: accent, chart-1; dark: chart-3 | #838684 |
| 600 | #577167 |  | #8C430E | light: chart-3 | #646765 |
| 700 | #485B53 |  | #6D3612 | light: chart-2 | #464846 |
| 800 | #34463F | brand anchor; light: primary, link; dark: primary-soft, selection | #4F2810 | light: chart-5 | #2F312F |
| 900 | #222B28 | light: primary-hover, link-hover | #351C0D | dark: accent-soft | #1B1C1B |
| 950 | #111614 |  | #1F1109 |  | #111211 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #141B17 on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #646765 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #34463F: **10.0:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #AD581E: **5.0:1**, AA.
- Link on page (light): `link` #34463F on `bg` #FAFAFA: **9.6:1**, AAA.
- Danger on soft (light): `danger` #B82F3E on `danger-soft` #FBE9E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #141B17 on `primary` #A9BCB4: **8.8:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A6A9A7 on `surface` #1F2622: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #D69F7F on `bg` #141B17: **7.6:1**, AAA.
- Dark success on surface (dark): `success` #21AA69 on `surface` #1F2622: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E77277 on `surface` #1F2622: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #E3AC1F on `surface` #1F2622: **7.5:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Government Green and Sienna only. Cane Sugar and Dark Moon are for the logo and icon, never for charts or UI.
- Charts use five shades of Sienna, plus Government Green as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Warning hue moved 16° toward yellow (OKLCH 65° to 81°) to stay apart from the brand hues.
- Danger hue moved 12° toward crimson (OKLCH 32° to 20°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
