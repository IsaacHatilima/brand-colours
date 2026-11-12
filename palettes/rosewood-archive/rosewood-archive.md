# Rosewood Archive

![Rosewood Archive colour system sheet](rosewood-archive.png)

- Character: literary, intimate, mature
- Suggested uses: bookshops, heritage hospitality, editorial brands
- Source: Rebuilt from the v1 palette Rosewood Archive.
- Files: [CSS tokens](rosewood-archive.css) · [JSON tokens](rosewood-archive.tokens.json) · [Colour sheet](rosewood-archive.png)

Brand colours: Vino Tinto #541625 (primary), Ansel #056986 (accent). Charts: Ansel shades plus Vino Tinto. Logo and icon only: Golden Beige #D1A577 (spark), Kala Black #211718 (ink).

## Brand colours

- Brand 1 · primary: [Vino Tinto](../../colors/vino-tinto.md) (#541625, RGB 84, 22, 37), the primary scale's anchor at step 800. Light UI uses primary-800 (#541625); dark UI uses primary-300 (#DF9AA4).
- Brand 2 · accent: [Ansel](../../colors/ansel.md) (#056986, RGB 5, 105, 134), the accent scale's anchor at step 600. Light UI uses accent-600 (#056986); dark UI uses accent-300 (#86BAD0).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #686565 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Golden Beige and Kala Black never appear as UI colours.

- Spark: [Golden Beige](../../colors/golden-beige.md) (#D1A577). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Kala Black](../../colors/kala-black.md) (#211718). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Kala Black | Vino Tinto | Ansel |
|---|---|---|---|---|
| Vino Tinto | ✓ 13.3 | ✗ 1.3 | same | ✗ 2.2 |
| Ansel | ✓ 6.0 | ✗ 2.8 | ✗ 2.2 | same |
| Golden Beige | ✗ 2.1 | ✓ 7.8 | ✓ 6.2 | ✗ 2.8 |
| Kala Black | ✓ 16.8 | same | ✗ 1.3 | ✗ 2.8 |
| Paper | same | ✓ 16.8 | ✓ 13.3 | ✓ 6.0 |

- On Paper: Vino Tinto, Ansel, Kala Black.
- On Kala Black: Golden Beige, Paper.
- On Vino Tinto: Golden Beige, Paper.
- On Ansel: Paper.

## Pairing rationale

Wine red stays the anchor. A deep library teal is the accent, the classic bookbinding pairing, and golden beige gilds the mark.

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
| primary | #541625 | #DF9AA4 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Vino Tinto (primary-800 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #35161C | #EBC0C6 | Hover and pressed fill of `primary`. |
| primary-soft | #FBF3F3 | #541625 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #211718 | Text and icons on `primary` and `primary-hover` (13.8:1 light, 7.7:1 dark). Dark mode uses ink, not white. |
| link | #541625 | #EBC0C6 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #35161C | #F5E0E3 | Hover state of `link`. |
| accent | #056986 | #86BAD0 | The single secondary hue, Ansel: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F0F6F9 | #0D2731 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #211718 | Text and icons on `accent` (6.2:1 light, 8.3:1 dark). |
| focus | #056986 | #86BAD0 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.0:1 on `bg` in light, 8.3:1 in dark. It uses the accent so it never blends into Vino Tinto controls. |
| selection | #F5E0E3 | #541625 | Text selection background. Text keeps `text`. |
| disabled-bg | #F4F1F1 | #352D2E | Fill of disabled buttons and inputs. |
| disabled-text | #878485 | #686565 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #24AC6A | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.3:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #211718 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.3:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #211718 | Text on solid `warning` fills. |
| danger | #B33C00 | #E57855 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E3 | #2E170F | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #211718 | Text on solid `danger` fills. |
| info | #541625 | #EBC0C6 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #FBF3F3 | #541625 | Background of info banners. Text on it uses `info`. |
| chart-1 | #056986 | #86BAD0 | Chart series 1, the anchor shade of Ansel. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #103B4A | #DBE9EF | Chart series 2, a darker Ansel in light and a lighter Ansel in dark. |
| chart-3 | #105268 | #1F87A9 | Chart series 3, a lighter Ansel in light and a deeper Ansel in dark. |
| chart-4 | #1F87A9 | #B5D4E1 | Chart series 4, a mid shade of Ansel. |
| chart-5 | #0D2731 | #4DA2C2 | Chart series 5, the remaining Ansel shade that still holds 3:1. |
| chart-alt | #541625 | #DF9AA4 | The one contrasting chart series: Vino Tinto, the primary brand colour. Chart colours are only Ansel shades and Vino Tinto, never status or logo colours. |
| chart-grid | #E5E2E2 | #403838 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #211718 | #211718 | Raw near-black, Kala Black: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #D1A577 | #D1A577 | Logo and icon only: Golden Beige, the highlight or signal dot. Never a UI colour. |
| logo-ink | #211718 | #211718 | Logo and icon only: wordmark and one-colour versions, Kala Black. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Vino Tinto at primary-800, Ansel at accent-600. Identical in both themes.

| Step | Primary (Vino Tinto) | Primary roles | Accent (Ansel) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #FBF3F3 | light: primary-soft | #F0F6F9 | light: accent-soft | #FBF8F8 |
| 100 | #F5E0E3 | light: selection; dark: link-hover | #DBE9EF | dark: chart-2 | #F4F1F1 |
| 200 | #EBC0C6 | dark: primary-hover, link | #B5D4E1 | dark: chart-4 | #E5E2E2 |
| 300 | #DF9AA4 | dark: primary | #86BAD0 | dark: accent, chart-1 | #CECBCB |
| 400 | #D57082 |  | #4DA2C2 | dark: chart-5 | #AAA7A8 |
| 500 | #BA5065 |  | #1F87A9 | light: chart-4; dark: chart-3 | #878485 |
| 600 | #93394C |  | #056986 | brand anchor; light: accent, chart-1 | #686565 |
| 700 | #702C3A |  | #105268 | light: chart-3 | #494647 |
| 800 | #541625 | brand anchor; light: primary, link; dark: primary-soft, selection | #103B4A | light: chart-2 | #322F2F |
| 900 | #35161C | light: primary-hover, link-hover | #0D2731 | light: chart-5; dark: accent-soft | #1E1B1B |
| 950 | #200F11 |  | #09171C |  | #141112 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #211718 on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #686565 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #541625: **13.8:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #056986: **6.2:1**, AA.
- Link on page (light): `link` #541625 on `bg` #FAFAFA: **13.3:1**, AAA.
- Danger on soft (light): `danger` #B33C00 on `danger-soft` #FBE9E3: **5.0:1**, AA.
- Dark primary button (dark): `on-primary` #211718 on `primary` #DF9AA4: **7.7:1**, AAA.
- Dark muted on surface (dark): `text-muted` #AAA7A8 on `surface` #2A2323: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #86BAD0 on `bg` #211718: **8.3:1**, AAA.
- Dark success on surface (dark): `success` #24AC6A on `surface` #2A2323: **5.3:1**, AA.
- Dark danger on surface (dark): `danger` #E57855 on `surface` #2A2323: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #2A2323: **7.3:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Vino Tinto and Ansel only. Golden Beige and Kala Black are for the logo and icon, never for charts or UI.
- Charts use five shades of Ansel, plus Vino Tinto as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Danger hue moved 8° toward orange-red (OKLCH 32° to 40°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
