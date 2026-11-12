# Plum After Dark

![Plum After Dark colour system sheet](plum-after-dark.png)

- Character: dramatic, expressive, polished
- Suggested uses: evening venues, fashion campaigns, premium cosmetics
- Source: Rebuilt from the v1 palette Plum After Dark.
- Files: [CSS tokens](plum-after-dark.css) · [JSON tokens](plum-after-dark.tokens.json) · [Colour sheet](plum-after-dark.png)

Brand colours: Dark Amethyst #422962 (primary), Picnic Day Sky #04C9E5 (accent). Charts: Picnic Day Sky shades plus Dark Amethyst. Logo and icon only: Mazzy Star #C161AB (spark), Absence Of Light #14131A (ink).

## Brand colours

- Brand 1 · primary: [Dark Amethyst](../../colors/dark-amethyst.md) (#422962, RGB 66, 41, 98), the primary scale's anchor at step 800. Light UI uses primary-800 (#422962); dark UI uses primary-300 (#BDA6E4).
- Brand 2 · accent: [Picnic Day Sky](../../colors/picnic-day-sky.md) (#04C9E5, RGB 4, 201, 229), the accent scale's anchor at step 300. Light UI uses accent-600 (#006F7F); dark UI uses accent-300 (#04C9E5).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #666668 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Mazzy Star and Absence Of Light never appear as UI colours.

- Spark: [Mazzy Star](../../colors/mazzy-star.md) (#C161AB). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Absence Of Light](../../colors/absence-of-light.md) (#14131A). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Absence Of Light | Dark Amethyst | Picnic Day Sky |
|---|---|---|---|---|
| Dark Amethyst | ✓ 11.7 | ✗ 1.5 | same | ✓ 6.1 |
| Picnic Day Sky | ✗ 1.9 | ✓ 9.2 | ✓ 6.1 | same |
| Mazzy Star | ✓ 3.6 | ✓ 4.9 | ✓ 3.2 | ✗ 1.9 |
| Absence Of Light | ✓ 17.7 | same | ✗ 1.5 | ✓ 9.2 |
| Paper | same | ✓ 17.7 | ✓ 11.7 | ✗ 1.9 |

- On Paper: Dark Amethyst, Mazzy Star, Absence Of Light.
- On Absence Of Light: Picnic Day Sky, Mazzy Star, Paper.
- On Dark Amethyst: Picnic Day Sky, Mazzy Star, Paper.
- On Picnic Day Sky: Dark Amethyst, Absence Of Light.

## Pairing rationale

Amethyst leads and a neon cyan accent cuts through the dark like stage light. Magenta sat too close to amethyst to work in the interface, so it moves to the mark, where it still reads on ink and amethyst.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #14131A | Page background: a plain off-white in light, the Absence Of Light ink in dark. Text on it uses `text` (17.7:1) and `text-muted` (5.5:1 light, 7.8:1 dark). |
| surface | #FFFFFF | #1E1E24 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #29282F | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F2F2F4 | #19181E | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E3E3E5 | #333239 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #858587 | #717178 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.4:1 dark on surface). |
| text | #14131A | #FAFAFA | Primary text and icons on every surface. Absence Of Light in light; the paper off-white in dark. |
| text-muted | #666668 | #A8A8AA | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #422962 | #BDA6E4 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Dark Amethyst (primary-800 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #2A1E3A | #D5C8ED | Hover and pressed fill of `primary`. |
| primary-soft | #F6F4FB | #422962 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #14131A | Text and icons on `primary` and `primary-hover` (12.2:1 light, 8.6:1 dark). Dark mode uses ink, not white. |
| link | #422962 | #D5C8ED | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #2A1E3A | #EAE4F5 | Hover state of `link`. |
| accent | #006F7F | #04C9E5 | The single secondary hue, Picnic Day Sky: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #EBF8FB | #002A31 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #14131A | Text and icons on `accent` (5.9:1 light, 9.2:1 dark). |
| focus | #006F7F | #04C9E5 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 5.6:1 on `bg` in light, 9.2:1 in dark. It uses the accent so it never blends into Dark Amethyst controls. |
| selection | #EAE4F5 | #422962 | Text selection background. Text keeps `text`. |
| disabled-bg | #F2F2F4 | #29282F | Fill of disabled buttons and inputs. |
| disabled-text | #858587 | #666668 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1BA766 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.3:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #14131A | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.9:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #14131A | Text on solid `warning` fills. |
| danger | #B8331E | #E57361 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.5:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #14131A | Text on solid `danger` fills. |
| info | #422962 | #D5C8ED | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F6F4FB | #422962 | Background of info banners. Text on it uses `info`. |
| chart-1 | #006F7F | #04C9E5 | Chart series 1, the anchor shade of Picnic Day Sky. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #003F49 | #CFEDF4 | Chart series 2, a darker Picnic Day Sky in light and a lighter Picnic Day Sky in dark. |
| chart-3 | #005764 | #008DA1 | Chart series 3, a lighter Picnic Day Sky in light and a deeper Picnic Day Sky in dark. |
| chart-4 | #008DA1 | #97DCEB | Chart series 4, a mid shade of Picnic Day Sky. |
| chart-5 | #002A31 | #00ABC3 | Chart series 5, the remaining Picnic Day Sky shade that still holds 3:1. |
| chart-alt | #422962 | #BDA6E4 | The one contrasting chart series: Dark Amethyst, the primary brand colour. Chart colours are only Picnic Day Sky shades and Dark Amethyst, never status or logo colours. |
| chart-grid | #E3E3E5 | #333239 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #14131A | #14131A | Raw near-black, Absence Of Light: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #C161AB | #C161AB | Logo and icon only: Mazzy Star, the highlight or signal dot. Never a UI colour. |
| logo-ink | #14131A | #14131A | Logo and icon only: wordmark and one-colour versions, Absence Of Light. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Dark Amethyst at primary-800, Picnic Day Sky at accent-300. Identical in both themes.

| Step | Primary (Dark Amethyst) | Primary roles | Accent (Picnic Day Sky) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F6F4FB | light: primary-soft | #EBF8FB | light: accent-soft | #F9F9FB |
| 100 | #EAE4F5 | light: selection; dark: link-hover | #CFEDF4 | dark: chart-2 | #F2F2F4 |
| 200 | #D5C8ED | dark: primary-hover, link | #97DCEB | dark: chart-4 | #E3E3E5 |
| 300 | #BDA6E4 | dark: primary | #04C9E5 | brand anchor; dark: accent, chart-1 | #CCCCCE |
| 400 | #A883DE |  | #00ABC3 | dark: chart-5 | #A8A8AA |
| 500 | #8E65C6 |  | #008DA1 | light: chart-4; dark: chart-3 | #858587 |
| 600 | #714DA0 |  | #006F7F | light: accent, chart-1 | #666668 |
| 700 | #583E7C |  | #005764 | light: chart-3 | #474749 |
| 800 | #422962 | brand anchor; light: primary, link; dark: primary-soft, selection | #003F49 | light: chart-2 | #303032 |
| 900 | #2A1E3A | light: primary-hover, link-hover | #002A31 | light: chart-5; dark: accent-soft | #1C1C1D |
| 950 | #171120 |  | #00181D |  | #121213 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #14131A on `bg` #FAFAFA: **17.7:1**, AAA.
- Muted on page (light): `text-muted` #666668 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #422962: **12.2:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #006F7F: **5.9:1**, AA.
- Link on page (light): `link` #422962 on `bg` #FAFAFA: **11.7:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #14131A on `primary` #BDA6E4: **8.6:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A8A8AA on `surface` #1E1E24: **7.0:1**, AA.
- Dark accent on page (dark): `accent` #04C9E5 on `bg` #14131A: **9.2:1**, AAA.
- Dark success on surface (dark): `success` #1BA766 on `surface` #1E1E24: **5.3:1**, AA.
- Dark danger on surface (dark): `danger` #E57361 on `surface` #1E1E24: **5.5:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #1E1E24: **7.9:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Dark Amethyst and Picnic Day Sky only. Mazzy Star and Absence Of Light are for the logo and icon, never for charts or UI.
- Charts use five shades of Picnic Day Sky, plus Dark Amethyst as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Picnic Day Sky itself sits at accent-300; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Picnic Day Sky in the logo and large graphics.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
