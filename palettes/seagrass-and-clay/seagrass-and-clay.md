# Seagrass and Clay

![Seagrass and Clay colour system sheet](seagrass-and-clay.png)

- Character: sunny, restorative, outdoorsy
- Suggested uses: wellness apps, outdoor retreats, surf and swim schools, plant-based food
- Source: Rebuilt from the v1 palette Coastal Herbarium.
- Files: [CSS tokens](seagrass-and-clay.css) · [JSON tokens](seagrass-and-clay.tokens.json) · [Colour sheet](seagrass-and-clay.png)

Brand colours: Seagrass #35A387 (primary), Maui Mai Tai #B46240 (accent). Charts: Maui Mai Tai shades plus Seagrass. Logo and icon only: Cane Sugar #E2BA80 (spark), Onyx #060E0E (ink).

## Brand colours

- Brand 1 · primary: [Seagrass](../../colors/seagrass.md) (#35A387, RGB 53, 163, 135), the primary scale's anchor at step 400. Light UI uses primary-600 (#006C57); dark UI uses primary-300 (#7BBAA7).
- Brand 2 · accent: [Maui Mai Tai](../../colors/maui-mai-tai.md) (#B46240, RGB 180, 98, 64), the accent scale's anchor at step 500. Light UI uses accent-600 (#914B2D); dark UI uses accent-300 (#DAA48E).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #646767 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Cane Sugar and Onyx never appear as UI colours.

- Spark: [Cane Sugar](../../colors/cane-sugar.md) (#E2BA80). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Onyx](../../colors/onyx-060e0e.md) (#060E0E). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Onyx | Seagrass | Maui Mai Tai |
|---|---|---|---|---|
| Seagrass | ✗ 3.0 | ✓ 6.3 | same | ✗ 1.4 |
| Maui Mai Tai | ✓ 4.2 | ✓ 4.4 | ✗ 1.4 | same |
| Cane Sugar | ✗ 1.7 | ✓ 10.7 | ✗ 1.7 | ✗ 2.4 |
| Onyx | ✓ 18.7 | same | ✓ 6.3 | ✓ 4.4 |
| Paper | same | ✓ 18.7 | ✗ 3.0 | ✓ 4.2 |

- On Paper: Maui Mai Tai, Onyx.
- On Onyx: Seagrass, Maui Mai Tai, Cane Sugar, Paper.
- On Seagrass: Onyx.
- On Maui Mai Tai: Onyx, Paper.

## Pairing rationale

The brighter green-teal from Coastal Herbarium leads, balanced by a sunbaked clay accent. Cane sugar ties both to the shoreline.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #060E0E | Page background: a plain off-white in light, the Onyx ink in dark. Text on it uses `text` (18.7:1) and `text-muted` (5.5:1 light, 8.2:1 dark). |
| surface | #FFFFFF | #101818 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #1A2222 | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F0F3F3 | #0B1313 | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E1E4E4 | #242C2C | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #838686 | #677171 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.6:1 dark on surface). |
| text | #060E0E | #FAFAFA | Primary text and icons on every surface. Onyx in light; the paper off-white in dark. |
| text-muted | #646767 | #A6A9A9 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #006C57 | #7BBAA7 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Seagrass (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #005644 | #B0D4C7 | Hover and pressed fill of `primary`. |
| primary-soft | #F0F7F4 | #043E31 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #060E0E | Text and icons on `primary` and `primary-hover` (6.4:1 light, 8.8:1 dark). Dark mode uses ink, not white. |
| link | #005644 | #B0D4C7 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #043E31 | #D9EAE4 | Hover state of `link`. |
| accent | #914B2D | #DAA48E | The single secondary hue, Maui Mai Tai: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FAF3F1 | #351D13 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #060E0E | Text and icons on `accent` (6.5:1 light, 9.0:1 dark). |
| focus | #914B2D | #DAA48E | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.2:1 on `bg` in light, 9.0:1 in dark. It uses the accent so it never blends into Seagrass controls. |
| selection | #D9EAE4 | #043E31 | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F3F3 | #1A2222 | Fill of disabled buttons and inputs. |
| disabled-text | #838686 | #646767 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #3B7635 | #54A349 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.5:1 light, 5.8:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E7F2E8 | #162918 | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #060E0E | Text on solid `success` fills. |
| warning | #8B5A00 | #ECA628 | Warning text, icons and fills (5.9:1 light, 8.6:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F8F0D9 | #29200A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #060E0E | Text on solid `warning` fills. |
| danger | #B82E42 | #E5707A | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.9:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #060E0E | Text on solid `danger` fills. |
| info | #005644 | #B0D4C7 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F0F7F4 | #043E31 | Background of info banners. Text on it uses `info`. |
| chart-1 | #914B2D | #DAA48E | Chart series 1, the anchor shade of Maui Mai Tai. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #502B1C | #F3E3DD | Chart series 2, a darker Maui Mai Tai in light and a lighter Maui Mai Tai in dark. |
| chart-3 | #CE8060 | #B46240 | Chart series 3, a lighter Maui Mai Tai in light and a deeper Maui Mai Tai in dark. |
| chart-4 | #703B26 | #E7C6B9 | Chart series 4, a mid shade of Maui Mai Tai. |
| chart-5 | #B46240 | #CE8060 | Chart series 5, the remaining Maui Mai Tai shade that still holds 3:1. |
| chart-alt | #006C57 | #7BBAA7 | The one contrasting chart series: Seagrass, the primary brand colour. Chart colours are only Maui Mai Tai shades and Seagrass, never status or logo colours. |
| chart-grid | #E1E4E4 | #242C2C | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #060E0E | #060E0E | Raw near-black, Onyx: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #E2BA80 | #E2BA80 | Logo and icon only: Cane Sugar, the highlight or signal dot. Never a UI colour. |
| logo-ink | #060E0E | #060E0E | Logo and icon only: wordmark and one-colour versions, Onyx. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Seagrass at primary-400, Maui Mai Tai at accent-500. Identical in both themes.

| Step | Primary (Seagrass) | Primary roles | Accent (Maui Mai Tai) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F0F7F4 | light: primary-soft | #FAF3F1 | light: accent-soft | #F7FAFA |
| 100 | #D9EAE4 | light: selection; dark: link-hover | #F3E3DD | dark: chart-2 | #F0F3F3 |
| 200 | #B0D4C7 | dark: primary-hover, link | #E7C6B9 | dark: chart-4 | #E1E4E4 |
| 300 | #7BBAA7 | dark: primary | #DAA48E | dark: accent, chart-1 | #CACDCD |
| 400 | #35A387 | brand anchor | #CE8060 | light: chart-3; dark: chart-5 | #A6A9A9 |
| 500 | #00896E |  | #B46240 | brand anchor; light: chart-5; dark: chart-3 | #838686 |
| 600 | #006C57 | light: primary | #914B2D | light: accent, chart-1 | #646767 |
| 700 | #005644 | light: primary-hover, link | #703B26 | light: chart-4 | #454848 |
| 800 | #043E31 | light: link-hover; dark: primary-soft, selection | #502B1C | light: chart-2 | #2E3131 |
| 900 | #082A21 |  | #351D13 | dark: accent-soft | #1A1C1C |
| 950 | #071813 |  | #1E110B |  | #101212 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #060E0E on `bg` #FAFAFA: **18.7:1**, AAA.
- Muted on page (light): `text-muted` #646767 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #006C57: **6.4:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #914B2D: **6.5:1**, AA.
- Link on page (light): `link` #005644 on `bg` #FAFAFA: **8.3:1**, AAA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #060E0E on `primary` #7BBAA7: **8.8:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A6A9A9 on `surface` #101818: **7.6:1**, AAA.
- Dark accent on page (dark): `accent` #DAA48E on `bg` #060E0E: **9.0:1**, AAA.
- Dark success on surface (dark): `success` #54A349 on `surface` #101818: **5.8:1**, AA.
- Dark danger on surface (dark): `danger` #E5707A on `surface` #101818: **5.9:1**, AA.
- Dark warning on surface (dark): `warning` #ECA628 on `surface` #101818: **8.6:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Seagrass and Maui Mai Tai only. Cane Sugar and Onyx are for the logo and icon, never for charts or UI.
- Charts use five shades of Maui Mai Tai, plus Seagrass as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Seagrass itself sits at primary-400; light-mode UI uses primary-600 so labels and text pass 4.5:1. Use the exact Seagrass in the logo and large graphics.
- Maui Mai Tai itself sits at accent-500; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Maui Mai Tai in the logo and large graphics.
- Cane Sugar reaches 3:1 only on Onyx; keep it off Seagrass and Maui Mai Tai grounds.
- Success hue moved 15° toward yellow-green (OKLCH 157° to 142°) to stay apart from the brand hues.
- Warning hue moved 8° toward yellow (OKLCH 65° to 73°) to stay apart from the brand hues.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
