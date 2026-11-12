# Velvet Bloom

![Velvet Bloom colour system sheet](velvet-bloom.png)

- Character: sensual, elegant, romantic
- Suggested uses: beauty brands, florists, fragrance, wedding stationery
- Source: A new combination from the colour library.
- Files: [CSS tokens](velvet-bloom.css) · [JSON tokens](velvet-bloom.tokens.json) · [Colour sheet](velvet-bloom.png)

Brand colours: Velvet Wine #9D4060 (primary), Iridescent Purple #8D6ED2 (accent). Charts: Iridescent Purple shades plus Velvet Wine. Logo and icon only: Jasmine #FED67D (spark), Kala Black #211718 (ink).

## Brand colours

- Brand 1 · primary: [Velvet Wine](../../colors/velvet-wine.md) (#9D4060, RGB 157, 64, 96), the primary scale's anchor at step 600. Light UI uses primary-600 (#9D4060); dark UI uses primary-300 (#E49DB0).
- Brand 2 · accent: [Iridescent Purple](../../colors/iridescent-purple.md) (#8D6ED2, RGB 141, 110, 210), the accent scale's anchor at step 500. Light UI uses accent-600 (#6F54A9); dark UI uses accent-300 (#BBABEB).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #686565 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Jasmine and Kala Black never appear as UI colours.

- Spark: [Jasmine](../../colors/jasmine.md) (#FED67D). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Kala Black](../../colors/kala-black.md) (#211718). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Kala Black | Velvet Wine | Iridescent Purple |
|---|---|---|---|---|
| Velvet Wine | ✓ 6.0 | ✗ 2.8 | same | ✗ 1.6 |
| Iridescent Purple | ✓ 3.8 | ✓ 4.4 | ✗ 1.6 | same |
| Jasmine | ✗ 1.3 | ✓ 12.6 | ✓ 4.5 | ✗ 2.9 |
| Kala Black | ✓ 16.8 | same | ✗ 2.8 | ✓ 4.4 |
| Paper | same | ✓ 16.8 | ✓ 6.0 | ✓ 3.8 |

- On Paper: Velvet Wine, Iridescent Purple, Kala Black.
- On Kala Black: Iridescent Purple, Jasmine, Paper.
- On Velvet Wine: Jasmine, Paper.
- On Iridescent Purple: Kala Black, Paper.

## Pairing rationale

Velvet rose leads and an iridescent violet accent adds a cool shimmer. Jasmine gives the mark a warm petal highlight.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #211718 | Page background: a plain off-white in light, the Kala Black ink in dark. Text on it uses `text` (16.8:1) and `text-muted` (5.5:1 light, 7.3:1 dark). |
| surface | #FFFFFF | #2A2323 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #352D2E | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F4F1F1 | #251D1E | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E5E2E2 | #403838 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #878485 | #7F7677 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #211718 | #FAFAFA | Primary text and icons on every surface. Kala Black in light; the paper off-white in dark. |
| text-muted | #686565 | #AAA7A8 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #9D4060 | #E49DB0 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Velvet Wine (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #79344B | #EEC2CD | Hover and pressed fill of `primary`. |
| primary-soft | #FBF2F5 | #572636 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #211718 | Text and icons on `primary` and `primary-hover` (6.3:1 light, 8.1:1 dark). Dark mode uses ink, not white. |
| link | #79344B | #EEC2CD | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #572636 | #F6E1E6 | Hover state of `link`. |
| accent | #6F54A9 | #BBABEB | The single secondary hue, Iridescent Purple: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F5F4FC | #281F3C | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #211718 | Text and icons on `accent` (6.0:1 light, 8.4:1 dark). |
| focus | #6F54A9 | #BBABEB | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 5.7:1 on `bg` in light, 8.4:1 in dark. It uses the accent so it never blends into Velvet Wine controls. |
| selection | #F6E1E6 | #572636 | Text selection background. Text keeps `text`. |
| disabled-bg | #F4F1F1 | #352D2E | Fill of disabled buttons and inputs. |
| disabled-text | #878485 | #686565 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #24AC6A | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.3:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #211718 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.3:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #211718 | Text on solid `warning` fills. |
| danger | #B8331E | #E77562 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #211718 | Text on solid `danger` fills. |
| info | #79344B | #EEC2CD | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #FBF2F5 | #572636 | Background of info banners. Text on it uses `info`. |
| chart-1 | #6F54A9 | #BBABEB | Chart series 1, the anchor shade of Iridescent Purple. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #3D2F5C | #E9E5F7 | Chart series 2, a darker Iridescent Purple in light and a lighter Iridescent Purple in dark. |
| chart-3 | #564282 | #8D6ED2 | Chart series 3, a lighter Iridescent Purple in light and a deeper Iridescent Purple in dark. |
| chart-4 | #8D6ED2 | #D4CBF1 | Chart series 4, a mid shade of Iridescent Purple. |
| chart-5 | #281F3C | #A68AE8 | Chart series 5, the remaining Iridescent Purple shade that still holds 3:1. |
| chart-alt | #9D4060 | #E49DB0 | The one contrasting chart series: Velvet Wine, the primary brand colour. Chart colours are only Iridescent Purple shades and Velvet Wine, never status or logo colours. |
| chart-grid | #E5E2E2 | #403838 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #211718 | #211718 | Raw near-black, Kala Black: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #FED67D | #FED67D | Logo and icon only: Jasmine, the highlight or signal dot. Never a UI colour. |
| logo-ink | #211718 | #211718 | Logo and icon only: wordmark and one-colour versions, Kala Black. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Velvet Wine at primary-600, Iridescent Purple at accent-500. Identical in both themes.

| Step | Primary (Velvet Wine) | Primary roles | Accent (Iridescent Purple) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #FBF2F5 | light: primary-soft | #F5F4FC | light: accent-soft | #FBF8F8 |
| 100 | #F6E1E6 | light: selection; dark: link-hover | #E9E5F7 | dark: chart-2 | #F4F1F1 |
| 200 | #EEC2CD | dark: primary-hover, link | #D4CBF1 | dark: chart-4 | #E5E2E2 |
| 300 | #E49DB0 | dark: primary | #BBABEB | dark: accent, chart-1 | #CECBCB |
| 400 | #DB7495 |  | #A68AE8 | dark: chart-5 | #AAA7A8 |
| 500 | #C2557A |  | #8D6ED2 | brand anchor; light: chart-4; dark: chart-3 | #878485 |
| 600 | #9D4060 | brand anchor; light: primary | #6F54A9 | light: accent, chart-1 | #686565 |
| 700 | #79344B | light: primary-hover, link | #564282 | light: chart-3 | #494647 |
| 800 | #572636 | light: link-hover; dark: primary-soft, selection | #3D2F5C | light: chart-2 | #322F2F |
| 900 | #391923 |  | #281F3C | light: chart-5; dark: accent-soft | #1E1B1B |
| 950 | #200E14 |  | #161121 |  | #141112 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #211718 on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #686565 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #9D4060: **6.3:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #6F54A9: **6.0:1**, AA.
- Link on page (light): `link` #79344B on `bg` #FAFAFA: **8.4:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #211718 on `primary` #E49DB0: **8.1:1**, AAA.
- Dark muted on surface (dark): `text-muted` #AAA7A8 on `surface` #2A2323: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #BBABEB on `bg` #211718: **8.4:1**, AAA.
- Dark success on surface (dark): `success` #24AC6A on `surface` #2A2323: **5.3:1**, AA.
- Dark danger on surface (dark): `danger` #E77562 on `surface` #2A2323: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #2A2323: **7.3:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Velvet Wine and Iridescent Purple only. Jasmine and Kala Black are for the logo and icon, never for charts or UI.
- Charts use five shades of Iridescent Purple, plus Velvet Wine as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Iridescent Purple itself sits at accent-500; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Iridescent Purple in the logo and large graphics.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
