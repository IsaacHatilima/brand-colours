# Berry and Mint

![Berry and Mint colour system sheet](berry-and-mint.png)

- Character: fresh, expressive, approachable
- Suggested uses: specialty beverages, contemporary skincare, creative retail
- Source: Rebuilt from the v1 palette Berry and Mint.
- Files: [CSS tokens](berry-and-mint.css) · [JSON tokens](berry-and-mint.tokens.json) · [Colour sheet](berry-and-mint.png)

Brand colours: Holly Fern #89B199 (primary), Cranberry Splash #D64F67 (accent). Charts: Cranberry Splash shades plus Holly Fern. Logo and icon only: Lemon Meringue #F4E397 (spark), Dark Moon #141B17 (ink).

## Brand colours

- Brand 1 · primary: [Holly Fern](../../colors/holly-fern.md) (#89B199, RGB 137, 177, 153), the primary scale's anchor at step 300. Light UI uses primary-600 (#33684C); dark UI uses primary-300 (#89B199).
- Brand 2 · accent: [Cranberry Splash](../../colors/cranberry-splash.md) (#D64F67, RGB 214, 79, 103), the accent scale's anchor at step 500. Light UI uses accent-600 (#AC384E); dark UI uses accent-300 (#F19BA4).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #646765 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Lemon Meringue and Dark Moon never appear as UI colours.

- Spark: [Lemon Meringue](../../colors/lemon-meringue.md) (#F4E397). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Dark Moon](../../colors/dark-moon.md) (#141B17). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Dark Moon | Holly Fern | Cranberry Splash |
|---|---|---|---|---|
| Holly Fern | ✗ 2.3 | ✓ 7.4 | same | ✗ 1.7 |
| Cranberry Splash | ✓ 3.9 | ✓ 4.3 | ✗ 1.7 | same |
| Lemon Meringue | ✗ 1.2 | ✓ 13.6 | ✗ 1.8 | ✓ 3.1 |
| Dark Moon | ✓ 16.8 | same | ✓ 7.4 | ✓ 4.3 |
| Paper | same | ✓ 16.8 | ✗ 2.3 | ✓ 3.9 |

- On Paper: Cranberry Splash, Dark Moon.
- On Dark Moon: Holly Fern, Cranberry Splash, Lemon Meringue, Paper.
- On Holly Fern: Dark Moon.
- On Cranberry Splash: Lemon Meringue, Dark Moon, Paper.

## Pairing rationale

A cool sage carries the interface while a ripe cranberry marks what matters. The two sit nearly opposite on the colour wheel, so the accent reads instantly without fighting the calm primary; lemon gives the mark a soft lift on dark grounds.

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
| primary | #33684C | #89B199 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Holly Fern (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #2A523C | #B8CEC0 | Hover and pressed fill of `primary`. |
| primary-soft | #F2F6F4 | #203B2C | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #141B17 | Text and icons on `primary` and `primary-hover` (6.5:1 light, 7.4:1 dark). Dark mode uses ink, not white. |
| link | #2A523C | #B8CEC0 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #203B2C | #DDE7E1 | Hover state of `link`. |
| accent | #AC384E | #F19BA4 | The single secondary hue, Cranberry Splash: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FDF2F3 | #3E171D | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #141B17 | Text and icons on `accent` (6.1:1 light, 8.3:1 dark). |
| focus | #AC384E | #F19BA4 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 5.9:1 on `bg` in light, 8.3:1 in dark. It uses the accent so it never blends into Holly Fern controls. |
| selection | #DDE7E1 | #203B2C | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F3F1 | #29302C | Fill of disabled buttons and inputs. |
| disabled-text | #838684 | #646765 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #3F7532 | #5EA749 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.5:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E7F2E7 | #172918 | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #141B17 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.4:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #141B17 | Text on solid `warning` fills. |
| danger | #B33C00 | #E57855 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.3:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E3 | #2E170F | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #141B17 | Text on solid `danger` fills. |
| info | #2A523C | #B8CEC0 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F2F6F4 | #203B2C | Background of info banners. Text on it uses `info`. |
| chart-1 | #AC384E | #F19BA4 | Chart series 1, the anchor shade of Cranberry Splash. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #5E222C | #FAE1E2 | Chart series 2, a darker Cranberry Splash in light and a lighter Cranberry Splash in dark. |
| chart-3 | #852E3E | #D64F67 | Chart series 3, a lighter Cranberry Splash in light and a deeper Cranberry Splash in dark. |
| chart-4 | #D64F67 | #F7C2C6 | Chart series 4, a mid shade of Cranberry Splash. |
| chart-5 | #3E171D | #EE7082 | Chart series 5, the remaining Cranberry Splash shade that still holds 3:1. |
| chart-alt | #33684C | #89B199 | The one contrasting chart series: Holly Fern, the primary brand colour. Chart colours are only Cranberry Splash shades and Holly Fern, never status or logo colours. |
| chart-grid | #E1E4E2 | #343B37 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #141B17 | #141B17 | Raw near-black, Dark Moon: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F4E397 | #F4E397 | Logo and icon only: Lemon Meringue, the highlight or signal dot. Never a UI colour. |
| logo-ink | #141B17 | #141B17 | Logo and icon only: wordmark and one-colour versions, Dark Moon. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Holly Fern at primary-300, Cranberry Splash at accent-500. Identical in both themes.

| Step | Primary (Holly Fern) | Primary roles | Accent (Cranberry Splash) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F2F6F4 | light: primary-soft | #FDF2F3 | light: accent-soft | #F7FAF8 |
| 100 | #DDE7E1 | light: selection; dark: link-hover | #FAE1E2 | dark: chart-2 | #F0F3F1 |
| 200 | #B8CEC0 | dark: primary-hover, link | #F7C2C6 | dark: chart-4 | #E1E4E2 |
| 300 | #89B199 | brand anchor; dark: primary | #F19BA4 | dark: accent, chart-1 | #CACDCB |
| 400 | #649C7C |  | #EE7082 | dark: chart-5 | #A6A9A7 |
| 500 | #468462 |  | #D64F67 | brand anchor; light: chart-4; dark: chart-3 | #838684 |
| 600 | #33684C | light: primary | #AC384E | light: accent, chart-1 | #646765 |
| 700 | #2A523C | light: primary-hover, link | #852E3E | light: chart-3 | #464846 |
| 800 | #203B2C | light: link-hover; dark: primary-soft, selection | #5E222C | light: chart-2 | #2F312F |
| 900 | #16281E |  | #3E171D | light: chart-5; dark: accent-soft | #1B1C1B |
| 950 | #0E1711 |  | #220D10 |  | #111211 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #141B17 on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #646765 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #33684C: **6.5:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #AC384E: **6.1:1**, AA.
- Link on page (light): `link` #2A523C on `bg` #FAFAFA: **8.5:1**, AAA.
- Danger on soft (light): `danger` #B33C00 on `danger-soft` #FBE9E3: **5.0:1**, AA.
- Dark primary button (dark): `on-primary` #141B17 on `primary` #89B199: **7.4:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A6A9A7 on `surface` #1F2622: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #F19BA4 on `bg` #141B17: **8.3:1**, AAA.
- Dark success on surface (dark): `success` #5EA749 on `surface` #1F2622: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E57855 on `surface` #1F2622: **5.3:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #1F2622: **7.4:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Holly Fern and Cranberry Splash only. Lemon Meringue and Dark Moon are for the logo and icon, never for charts or UI.
- Charts use five shades of Cranberry Splash, plus Holly Fern as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Holly Fern itself sits at primary-300; light-mode UI uses primary-600 so labels and text pass 4.5:1. Use the exact Holly Fern in the logo and large graphics.
- Cranberry Splash itself sits at accent-500; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Cranberry Splash in the logo and large graphics.
- Success hue moved 17° toward yellow-green (OKLCH 157° to 140°) to stay apart from the brand hues.
- Danger hue moved 8° toward orange-red (OKLCH 32° to 40°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
