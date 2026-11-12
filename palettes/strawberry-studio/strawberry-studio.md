# Strawberry Studio

![Strawberry Studio colour system sheet](strawberry-studio.png)

- Character: soft, playful, welcoming
- Suggested uses: friendly consumer brands, stationery, family services
- Source: Rebuilt from the v1 palette Strawberry Studio.
- Files: [CSS tokens](strawberry-studio.css) · [JSON tokens](strawberry-studio.tokens.json) · [Colour sheet](strawberry-studio.png)

Brand colours: Royal Plum #613C5E (primary), Seagrass #35A387 (accent). Charts: Seagrass shades plus Royal Plum. Logo and icon only: Strawberry Ice #E68890 (spark), Violet Void #1B181D (ink).

## Brand colours

- Brand 1 · primary: [Royal Plum](../../colors/royal-plum.md) (#613C5E, RGB 97, 60, 94), the primary scale's anchor at step 700. Light UI uses primary-700 (#613C5E); dark UI uses primary-300 (#CAA4C6).
- Brand 2 · accent: [Seagrass](../../colors/seagrass.md) (#35A387, RGB 53, 163, 135), the accent scale's anchor at step 400. Light UI uses accent-600 (#006C57); dark UI uses accent-300 (#7BBAA7).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #676567 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Strawberry Ice and Violet Void never appear as UI colours.

- Spark: [Strawberry Ice](../../colors/strawberry-ice.md) (#E68890). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Violet Void](../../colors/violet-void.md) (#1B181D). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Violet Void | Royal Plum | Seagrass |
|---|---|---|---|---|
| Royal Plum | ✓ 8.7 | ✗ 1.9 | same | ✗ 2.9 |
| Seagrass | ✗ 3.0 | ✓ 5.6 | ✗ 2.9 | same |
| Strawberry Ice | ✗ 2.4 | ✓ 6.9 | ✓ 3.6 | ✗ 1.2 |
| Violet Void | ✓ 16.8 | same | ✗ 1.9 | ✓ 5.6 |
| Paper | same | ✓ 16.8 | ✓ 8.7 | ✗ 3.0 |

- On Paper: Royal Plum, Violet Void.
- On Violet Void: Seagrass, Strawberry Ice, Paper.
- On Royal Plum: Strawberry Ice, Paper.
- On Seagrass: Violet Void.

## Pairing rationale

Royal plum gives the playful palette a steady base for buttons and a leafy seagrass green is the accent. Strawberry pink blurred into the plum as an accent, so it becomes the fruit in the mark.

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
| primary | #613C5E | #CAA4C6 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Royal Plum (primary-700 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #462C43 | #DDC6DA | Hover and pressed fill of `primary`. |
| primary-soft | #F8F3F7 | #462C43 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #1B181D | Text and icons on `primary` and `primary-hover` (9.1:1 light, 8.1:1 dark). Dark mode uses ink, not white. |
| link | #613C5E | #DDC6DA | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #462C43 | #EEE3EC | Hover state of `link`. |
| accent | #006C57 | #7BBAA7 | The single secondary hue, Seagrass: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F0F7F4 | #082A21 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #1B181D | Text and icons on `accent` (6.4:1 light, 7.9:1 dark). |
| focus | #006C57 | #7BBAA7 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.1:1 on `bg` in light, 7.9:1 in dark. It uses the accent so it never blends into Royal Plum controls. |
| selection | #EEE3EC | #462C43 | Text selection background. Text keeps `text`. |
| disabled-bg | #F3F1F4 | #302D33 | Fill of disabled buttons and inputs. |
| disabled-text | #868587 | #676567 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #3B7635 | #59A84E | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.5:1 light, 5.3:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E7F2E8 | #162918 | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #1B181D | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.4:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #1B181D | Text on solid `warning` fills. |
| danger | #B8331E | #E77562 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.3:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #1B181D | Text on solid `danger` fills. |
| info | #613C5E | #DDC6DA | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F8F3F7 | #462C43 | Background of info banners. Text on it uses `info`. |
| chart-1 | #006C57 | #7BBAA7 | Chart series 1, the anchor shade of Seagrass. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #043E31 | #D9EAE4 | Chart series 2, a darker Seagrass in light and a lighter Seagrass in dark. |
| chart-3 | #35A387 | #00896E | Chart series 3, a lighter Seagrass in light and a deeper Seagrass in dark. |
| chart-4 | #005644 | #B0D4C7 | Chart series 4, a mid shade of Seagrass. |
| chart-5 | #00896E | #35A387 | Chart series 5, the remaining Seagrass shade that still holds 3:1. |
| chart-alt | #613C5E | #CAA4C6 | The one contrasting chart series: Royal Plum, the primary brand colour. Chart colours are only Seagrass shades and Royal Plum, never status or logo colours. |
| chart-grid | #E4E2E5 | #3B383D | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #1B181D | #1B181D | Raw near-black, Violet Void: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #E68890 | #E68890 | Logo and icon only: Strawberry Ice, the highlight or signal dot. Never a UI colour. |
| logo-ink | #1B181D | #1B181D | Logo and icon only: wordmark and one-colour versions, Violet Void. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Royal Plum at primary-700, Seagrass at accent-400. Identical in both themes.

| Step | Primary (Royal Plum) | Primary roles | Accent (Seagrass) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F8F3F7 | light: primary-soft | #F0F7F4 | light: accent-soft | #FAF8FB |
| 100 | #EEE3EC | light: selection; dark: link-hover | #D9EAE4 | dark: chart-2 | #F3F1F4 |
| 200 | #DDC6DA | dark: primary-hover, link | #B0D4C7 | dark: chart-4 | #E4E2E5 |
| 300 | #CAA4C6 | dark: primary | #7BBAA7 | dark: accent, chart-1 | #CDCBCE |
| 400 | #B882B3 |  | #35A387 | brand anchor; light: chart-3; dark: chart-5 | #A9A8AA |
| 500 | #9E6499 |  | #00896E | light: chart-5; dark: chart-3 | #868587 |
| 600 | #7D4C7A |  | #006C57 | light: accent, chart-1 | #676567 |
| 700 | #613C5E | brand anchor; light: primary, link | #005644 | light: chart-4 | #484748 |
| 800 | #462C43 | light: primary-hover, link-hover; dark: primary-soft, selection | #043E31 | light: chart-2 | #313031 |
| 900 | #2E1D2D |  | #082A21 | dark: accent-soft | #1C1B1D |
| 950 | #1A1119 |  | #071813 |  | #121213 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #1B181D on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #676567 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #613C5E: **9.1:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #006C57: **6.4:1**, AA.
- Link on page (light): `link` #613C5E on `bg` #FAFAFA: **8.7:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #1B181D on `primary` #CAA4C6: **8.1:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A9A8AA on `surface` #262328: **6.6:1**, AA.
- Dark accent on page (dark): `accent` #7BBAA7 on `bg` #1B181D: **7.9:1**, AAA.
- Dark success on surface (dark): `success` #59A84E on `surface` #262328: **5.3:1**, AA.
- Dark danger on surface (dark): `danger` #E77562 on `surface` #262328: **5.3:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #262328: **7.4:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Royal Plum and Seagrass only. Strawberry Ice and Violet Void are for the logo and icon, never for charts or UI.
- Charts use five shades of Seagrass, plus Royal Plum as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Seagrass itself sits at accent-400; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Seagrass in the logo and large graphics.
- Success hue moved 15° toward yellow-green (OKLCH 157° to 142°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
