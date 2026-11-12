# Orchard Harvest

![Orchard Harvest colour system sheet](orchard-harvest.png)

- Character: earthy, abundant, seasonal
- Suggested uses: farm shops, cider packaging, rural hospitality
- Source: Rebuilt from the v1 palette Orchard Harvest.
- Files: [CSS tokens](orchard-harvest.css) · [JSON tokens](orchard-harvest.tokens.json) · [Colour sheet](orchard-harvest.png)

Brand colours: Spring Juniper #4B784A (primary), Grape Soda #8D4887 (accent). Charts: Grape Soda shades plus Spring Juniper. Logo and icon only: Kikuchiba Gold #E39945 (spark), Nightshade Berries #1C1814 (ink).

## Brand colours

- Brand 1 · primary: [Spring Juniper](../../colors/spring-juniper.md) (#4B784A, RGB 75, 120, 74), the primary scale's anchor at step 600. Light UI uses primary-600 (#4B784A); dark UI uses primary-300 (#A1C19F).
- Brand 2 · accent: [Grape Soda](../../colors/grape-soda.md) (#8D4887, RGB 141, 72, 135), the accent scale's anchor at step 600. Light UI uses accent-600 (#8D4887); dark UI uses accent-300 (#D5A1CE).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #676664 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Kikuchiba Gold and Nightshade Berries never appear as UI colours.

- Spark: [Kikuchiba Gold](../../colors/kikuchiba-gold.md) (#E39945). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Nightshade Berries](../../colors/nightshade-berries-1c1814.md) (#1C1814). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Nightshade Berries | Spring Juniper | Grape Soda |
|---|---|---|---|---|
| Spring Juniper | ✓ 4.9 | ✓ 3.4 | same | ✗ 1.2 |
| Grape Soda | ✓ 5.9 | ✗ 2.9 | ✗ 1.2 | same |
| Kikuchiba Gold | ✗ 2.3 | ✓ 7.5 | ✗ 2.2 | ✗ 2.6 |
| Nightshade Berries | ✓ 16.9 | same | ✓ 3.4 | ✗ 2.9 |
| Paper | same | ✓ 16.9 | ✓ 4.9 | ✓ 5.9 |

- On Paper: Spring Juniper, Grape Soda, Nightshade Berries.
- On Nightshade Berries: Spring Juniper, Kikuchiba Gold, Paper.
- On Spring Juniper: Nightshade Berries, Paper.
- On Grape Soda: Paper.

## Pairing rationale

Orchard green leads. The v1 browns and golds would muddy into the warning amber as accents, so a plum from the library ripens the palette instead. Kikuchiba gold stays as the harvest-light spark.

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
| primary | #4B784A | #A1C19F | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Spring Juniper (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #3B5D3A | #C4D8C3 | Hover and pressed fill of `primary`. |
| primary-soft | #F2F6F2 | #2A422A | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #1C1814 | Text and icons on `primary` and `primary-hover` (5.1:1 light, 8.9:1 dark). Dark mode uses ink, not white. |
| link | #3B5D3A | #C4D8C3 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #2A422A | #E2EBE1 | Hover state of `link`. |
| accent | #8D4887 | #D5A1CE | The single secondary hue, Grape Soda: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F9F3F8 | #331B30 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #1C1814 | Text and icons on `accent` (6.2:1 light, 8.2:1 dark). |
| focus | #8D4887 | #D5A1CE | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 5.9:1 on `bg` in light, 8.2:1 in dark. It uses the accent so it never blends into Spring Juniper controls. |
| selection | #E2EBE1 | #2A422A | Text selection background. Text keeps `text`. |
| disabled-bg | #F4F2F0 | #322D29 | Fill of disabled buttons and inputs. |
| disabled-text | #878583 | #676664 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #007861 | #0DA889 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E2F3EF | #082A24 | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #1C1814 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.4:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #1C1814 | Text on solid `warning` fills. |
| danger | #B8331E | #E57361 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #1C1814 | Text on solid `danger` fills. |
| info | #3B5D3A | #C4D8C3 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F2F6F2 | #2A422A | Background of info banners. Text on it uses `info`. |
| chart-1 | #8D4887 | #D5A1CE | Chart series 1, the anchor shade of Grape Soda. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #4E294A | #F1E2EF | Chart series 2, a darker Grape Soda in light and a lighter Grape Soda in dark. |
| chart-3 | #6D3968 | #AE5EA7 | Chart series 3, a lighter Grape Soda in light and a deeper Grape Soda in dark. |
| chart-4 | #AE5EA7 | #E4C4E0 | Chart series 4, a mid shade of Grape Soda. |
| chart-5 | #331B30 | #C87CC0 | Chart series 5, the remaining Grape Soda shade that still holds 3:1. |
| chart-alt | #4B784A | #A1C19F | The one contrasting chart series: Spring Juniper, the primary brand colour. Chart colours are only Grape Soda shades and Spring Juniper, never status or logo colours. |
| chart-grid | #E5E3E1 | #3C3833 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #1C1814 | #1C1814 | Raw near-black, Nightshade Berries: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #E39945 | #E39945 | Logo and icon only: Kikuchiba Gold, the highlight or signal dot. Never a UI colour. |
| logo-ink | #1C1814 | #1C1814 | Logo and icon only: wordmark and one-colour versions, Nightshade Berries. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Spring Juniper at primary-600, Grape Soda at accent-600. Identical in both themes.

| Step | Primary (Spring Juniper) | Primary roles | Accent (Grape Soda) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F2F6F2 | light: primary-soft | #F9F3F8 | light: accent-soft | #FBF9F7 |
| 100 | #E2EBE1 | light: selection; dark: link-hover | #F1E2EF | dark: chart-2 | #F4F2F0 |
| 200 | #C4D8C3 | dark: primary-hover, link | #E4C4E0 | dark: chart-4 | #E5E3E1 |
| 300 | #A1C19F | dark: primary | #D5A1CE | dark: accent, chart-1 | #CECCCA |
| 400 | #7CAD7A |  | #C87CC0 | dark: chart-5 | #AAA8A6 |
| 500 | #60945E |  | #AE5EA7 | light: chart-4; dark: chart-3 | #878583 |
| 600 | #4B784A | brand anchor; light: primary | #8D4887 | brand anchor; light: accent, chart-1 | #676664 |
| 700 | #3B5D3A | light: primary-hover, link | #6D3968 | light: chart-3 | #484745 |
| 800 | #2A422A | light: link-hover; dark: primary-soft, selection | #4E294A | light: chart-2 | #31302E |
| 900 | #1B2B1B |  | #331B30 | light: chart-5; dark: accent-soft | #1D1C1A |
| 950 | #0F170E |  | #1C0F1B |  | #131210 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #1C1814 on `bg` #FAFAFA: **16.9:1**, AAA.
- Muted on page (light): `text-muted` #676664 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #4B784A: **5.1:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #8D4887: **6.2:1**, AA.
- Link on page (light): `link` #3B5D3A on `bg` #FAFAFA: **7.2:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #1C1814 on `primary` #A1C19F: **8.9:1**, AAA.
- Dark muted on surface (dark): `text-muted` #AAA8A6 on `surface` #27231F: **6.6:1**, AA.
- Dark accent on page (dark): `accent` #D5A1CE on `bg` #1C1814: **8.2:1**, AAA.
- Dark success on surface (dark): `success` #0DA889 on `surface` #27231F: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E57361 on `surface` #27231F: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #27231F: **7.4:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Spring Juniper and Grape Soda only. Kikuchiba Gold and Nightshade Berries are for the logo and icon, never for charts or UI.
- Charts use five shades of Grape Soda, plus Spring Juniper as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Kikuchiba Gold reaches 3:1 only on Nightshade Berries; keep it off Spring Juniper and Grape Soda grounds.
- Success hue moved 17° toward teal (OKLCH 157° to 174°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
