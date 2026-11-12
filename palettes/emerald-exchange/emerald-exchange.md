# Emerald Exchange

![Emerald Exchange colour system sheet](emerald-exchange.png)

- Character: prosperous, modern, steady
- Suggested uses: fintech, banking apps, investment platforms, sustainability reporting
- Source: A new combination from the colour library.
- Files: [CSS tokens](emerald-exchange.css) · [JSON tokens](emerald-exchange.tokens.json) · [Colour sheet](emerald-exchange.png)

Brand colours: Forestial #027A2F (primary), Gigas #594587 (accent). Charts: Gigas shades plus Forestial. Logo and icon only: Bright Gold #F4D80E (spark), Dark Moon #141B17 (ink).

## Brand colours

- Brand 1 · primary: [Forestial](../../colors/forestial.md) (#027A2F, RGB 2, 122, 47), the primary scale's anchor at step 600. Light UI uses primary-600 (#027A2F); dark UI uses primary-300 (#87C690).
- Brand 2 · accent: [Gigas](../../colors/gigas.md) (#594587, RGB 89, 69, 135), the accent scale's anchor at step 700. Light UI uses accent-700 (#594587); dark UI uses accent-300 (#BAAAEB).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #646765 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Bright Gold and Dark Moon never appear as UI colours.

- Spark: [Bright Gold](../../colors/bright-gold.md) (#F4D80E). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Dark Moon](../../colors/dark-moon.md) (#141B17). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Dark Moon | Forestial | Gigas |
|---|---|---|---|---|
| Forestial | ✓ 5.3 | ✓ 3.2 | same | ✗ 1.5 |
| Gigas | ✓ 7.7 | ✗ 2.2 | ✗ 1.5 | same |
| Bright Gold | ✗ 1.4 | ✓ 12.2 | ✓ 3.8 | ✓ 5.6 |
| Dark Moon | ✓ 16.8 | same | ✓ 3.2 | ✗ 2.2 |
| Paper | same | ✓ 16.8 | ✓ 5.3 | ✓ 7.7 |

- On Paper: Forestial, Gigas, Dark Moon.
- On Dark Moon: Forestial, Bright Gold, Paper.
- On Forestial: Bright Gold, Dark Moon, Paper.
- On Gigas: Bright Gold, Paper.

## Pairing rationale

Emerald signals growth and stability; a deep violet accent keeps highlights and focus apart from the green. Success shifts toward teal so it never reads as a brand button.

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
| primary | #027A2F | #87C690 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Forestial (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #105F27 | #B6DBBA | Hover and pressed fill of `primary`. |
| primary-soft | #F0F7F1 | #10441D | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #141B17 | Text and icons on `primary` and `primary-hover` (5.5:1 light, 8.8:1 dark). Dark mode uses ink, not white. |
| link | #105F27 | #B6DBBA | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #10441D | #DCEDDD | Hover state of `link`. |
| accent | #594587 | #BAAAEB | The single secondary hue, Gigas: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F5F4FC | #28203E | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #141B17 | Text and icons on `accent` (8.0:1 light, 8.4:1 dark). |
| focus | #594587 | #BAAAEB | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 7.7:1 on `bg` in light, 8.4:1 in dark. It uses the accent so it never blends into Forestial controls. |
| selection | #DCEDDD | #10441D | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F3F1 | #29302C | Fill of disabled buttons and inputs. |
| disabled-text | #838684 | #646765 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #007763 | #0DA88B | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.5:1 light, 5.1:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E2F3EF | #082A25 | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #141B17 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.4:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #141B17 | Text on solid `warning` fills. |
| danger | #B8331E | #E77562 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #141B17 | Text on solid `danger` fills. |
| info | #105F27 | #B6DBBA | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F0F7F1 | #10441D | Background of info banners. Text on it uses `info`. |
| chart-1 | #594587 | #BAAAEB | Chart series 1, the anchor shade of Gigas. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #28203E | #E8E5F7 | Chart series 2, a darker Gigas in light and a lighter Gigas in dark. |
| chart-3 | #8B6CD2 | #8B6CD2 | Chart series 3, a lighter Gigas in light and a deeper Gigas in dark. |
| chart-4 | #3F315F | #D3CAF1 | Chart series 4, a mid shade of Gigas. |
| chart-5 | #7054AC | #A488E8 | Chart series 5, the remaining Gigas shade that still holds 3:1. |
| chart-alt | #027A2F | #87C690 | The one contrasting chart series: Forestial, the primary brand colour. Chart colours are only Gigas shades and Forestial, never status or logo colours. |
| chart-grid | #E1E4E2 | #343B37 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #141B17 | #141B17 | Raw near-black, Dark Moon: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F4D80E | #F4D80E | Logo and icon only: Bright Gold, the highlight or signal dot. Never a UI colour. |
| logo-ink | #141B17 | #141B17 | Logo and icon only: wordmark and one-colour versions, Dark Moon. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Forestial at primary-600, Gigas at accent-700. Identical in both themes.

| Step | Primary (Forestial) | Primary roles | Accent (Gigas) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F0F7F1 | light: primary-soft | #F5F4FC | light: accent-soft | #F7FAF8 |
| 100 | #DCEDDD | light: selection; dark: link-hover | #E8E5F7 | dark: chart-2 | #F0F3F1 |
| 200 | #B6DBBA | dark: primary-hover, link | #D3CAF1 | dark: chart-4 | #E1E4E2 |
| 300 | #87C690 | dark: primary | #BAAAEB | dark: accent, chart-1 | #CACDCB |
| 400 | #4DB362 |  | #A488E8 | dark: chart-5 | #A6A9A7 |
| 500 | #1B9842 |  | #8B6CD2 | light: chart-3; dark: chart-3 | #838684 |
| 600 | #027A2F | brand anchor; light: primary | #7054AC | light: chart-5 | #646765 |
| 700 | #105F27 | light: primary-hover, link | #594587 | brand anchor; light: accent, chart-1 | #464846 |
| 800 | #10441D | light: link-hover; dark: primary-soft, selection | #3F315F | light: chart-4 | #2F312F |
| 900 | #0D2C14 |  | #28203E | light: chart-2; dark: accent-soft | #1B1C1B |
| 950 | #08190B |  | #161121 |  | #111211 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #141B17 on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #646765 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #027A2F: **5.5:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #594587: **8.0:1**, AAA.
- Link on page (light): `link` #105F27 on `bg` #FAFAFA: **7.5:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #141B17 on `primary` #87C690: **8.8:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A6A9A7 on `surface` #1F2622: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #BAAAEB on `bg` #141B17: **8.4:1**, AAA.
- Dark success on surface (dark): `success` #0DA88B on `surface` #1F2622: **5.1:1**, AA.
- Dark danger on surface (dark): `danger` #E77562 on `surface` #1F2622: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #1F2622: **7.4:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Forestial and Gigas only. Bright Gold and Dark Moon are for the logo and icon, never for charts or UI.
- Charts use five shades of Gigas, plus Forestial as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Success hue moved 18° toward teal (OKLCH 157° to 175°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
