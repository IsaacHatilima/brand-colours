# Midnight Brass

![Midnight Brass colour system sheet](midnight-brass.png)

- Character: precise, premium, assured
- Suggested uses: boutique finance, watches, architectural practices
- Source: Rebuilt from the v1 palette Midnight Brass.
- Files: [CSS tokens](midnight-brass.css) · [JSON tokens](midnight-brass.tokens.json) · [Colour sheet](midnight-brass.png)

Brand colours: Yankees Blue #1C273E (primary), Golden Bronze #C39545 (accent). Charts: Golden Bronze shades plus Yankees Blue. Logo and icon only: Candid Blue #70C6E2 (spark), Black Is Back #11141B (ink).

## Brand colours

- Brand 1 · primary: [Yankees Blue](../../colors/yankees-blue.md) (#1C273E, RGB 28, 39, 62), the primary scale's anchor at step 900. Light UI uses primary-900 (#1C273E); dark UI uses primary-300 (#A7B4CF).
- Brand 2 · accent: [Golden Bronze](../../colors/golden-bronze.md) (#C39545, RGB 195, 149, 69), the accent scale's anchor at step 400. Light UI uses accent-600 (#855D00); dark UI uses accent-300 (#D1B281).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #656668 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Candid Blue and Black Is Back never appear as UI colours.

- Spark: [Candid Blue](../../colors/candid-blue.md) (#70C6E2). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Black Is Back](../../colors/black-is-back-11141b.md) (#11141B). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Black Is Back | Yankees Blue | Golden Bronze |
|---|---|---|---|---|
| Yankees Blue | ✓ 14.3 | ✗ 1.2 | same | ✓ 5.5 |
| Golden Bronze | ✗ 2.6 | ✓ 6.8 | ✓ 5.5 | same |
| Candid Blue | ✗ 1.9 | ✓ 9.5 | ✓ 7.7 | ✗ 1.4 |
| Black Is Back | ✓ 17.7 | same | ✗ 1.2 | ✓ 6.8 |
| Paper | same | ✓ 17.7 | ✓ 14.3 | ✗ 2.6 |

- On Paper: Yankees Blue, Black Is Back.
- On Black Is Back: Golden Bronze, Candid Blue, Paper.
- On Yankees Blue: Golden Bronze, Candid Blue, Paper.
- On Golden Bronze: Yankees Blue, Black Is Back.

## Pairing rationale

Midnight navy with a brass accent is the identity, so brass stays in the UI even though it sits near the warning amber; warnings are moved further toward orange. A cool sky spark keeps the mark crisp on ink.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #11141B | Page background: a plain off-white in light, the Black Is Back ink in dark. Text on it uses `text` (17.7:1) and `text-muted` (5.5:1 light, 7.7:1 dark). |
| surface | #FFFFFF | #1C1F24 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #26292F | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F1F2F4 | #17191F | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E2E3E6 | #31333A | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #848587 | #6E7279 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.4:1 dark on surface). |
| text | #11141B | #FAFAFA | Primary text and icons on every surface. Black Is Back in light; the paper off-white in dark. |
| text-muted | #656668 | #A7A8AA | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #1C273E | #A7B4CF | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Yankees Blue (primary-900 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #11141B | #C7D0E0 | Hover and pressed fill of `primary`. |
| primary-soft | #F3F5F8 | #313A4D | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #11141B | Text and icons on `primary` and `primary-hover` (14.9:1 light, 8.8:1 dark). Dark mode uses ink, not white. |
| link | #1C273E | #C7D0E0 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #11141B | #E3E7EF | Hover state of `link`. |
| accent | #855D00 | #D1B281 | The single secondary hue, Golden Bronze: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F8F5EF | #302209 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #11141B | Text and icons on `accent` (5.9:1 light, 9.1:1 dark). |
| focus | #855D00 | #D1B281 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 5.6:1 on `bg` in light, 9.1:1 in dark. It uses the accent so it never blends into Yankees Blue controls. |
| selection | #E3E7EF | #313A4D | Text selection background. Text keeps `text`. |
| disabled-bg | #F1F2F4 | #26292F | Fill of disabled buttons and inputs. |
| disabled-text | #848587 | #656668 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1BA766 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.3:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #11141B | Text on solid `success` fills. |
| warning | #985023 | #FF9850 | Warning text, icons and fills (6.0:1 light, 7.8:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FFEDDB | #2E1D0C | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #11141B | Text on solid `warning` fills. |
| danger | #B8331E | #E57361 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.5:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #11141B | Text on solid `danger` fills. |
| info | #1C273E | #C7D0E0 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F3F5F8 | #313A4D | Background of info banners. Text on it uses `info`. |
| chart-1 | #855D00 | #D1B281 | Chart series 1, the anchor shade of Golden Bronze. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #4A340B | #EFE7D9 | Chart series 2, a darker Golden Bronze in light and a lighter Golden Bronze in dark. |
| chart-3 | #684807 | #A87710 | Chart series 3, a lighter Golden Bronze in light and a deeper Golden Bronze in dark. |
| chart-4 | #A87710 | #E1CEB2 | Chart series 4, a mid shade of Golden Bronze. |
| chart-5 | #302209 | #C39545 | Chart series 5, the remaining Golden Bronze shade that still holds 3:1. |
| chart-alt | #1C273E | #A7B4CF | The one contrasting chart series: Yankees Blue, the primary brand colour. Chart colours are only Golden Bronze shades and Yankees Blue, never status or logo colours. |
| chart-grid | #E2E3E6 | #31333A | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #11141B | #11141B | Raw near-black, Black Is Back: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #70C6E2 | #70C6E2 | Logo and icon only: Candid Blue, the highlight or signal dot. Never a UI colour. |
| logo-ink | #11141B | #11141B | Logo and icon only: wordmark and one-colour versions, Black Is Back. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Yankees Blue at primary-900, Golden Bronze at accent-400. Identical in both themes.

| Step | Primary (Yankees Blue) | Primary roles | Accent (Golden Bronze) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F3F5F8 | light: primary-soft | #F8F5EF | light: accent-soft | #F8F9FB |
| 100 | #E3E7EF | light: selection; dark: link-hover | #EFE7D9 | dark: chart-2 | #F1F2F4 |
| 200 | #C7D0E0 | dark: primary-hover, link | #E1CEB2 | dark: chart-4 | #E2E3E6 |
| 300 | #A7B4CF | dark: primary | #D1B281 | dark: accent, chart-1 | #CBCCCE |
| 400 | #869AC1 |  | #C39545 | brand anchor; dark: chart-5 | #A7A8AA |
| 500 | #6A7FA9 |  | #A87710 | light: chart-4; dark: chart-3 | #848587 |
| 600 | #536488 |  | #855D00 | light: accent, chart-1 | #656668 |
| 700 | #424F6A |  | #684807 | light: chart-3 | #464749 |
| 800 | #313A4D | dark: primary-soft, selection | #4A340B | light: chart-2 | #2F3032 |
| 900 | #1C273E | brand anchor; light: primary, link | #302209 | light: chart-5; dark: accent-soft | #1B1C1E |
| 950 | #11141B | light: primary-hover, link-hover | #1B1307 |  | #111214 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #11141B on `bg` #FAFAFA: **17.7:1**, AAA.
- Muted on page (light): `text-muted` #656668 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #1C273E: **14.9:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #855D00: **5.9:1**, AA.
- Link on page (light): `link` #1C273E on `bg` #FAFAFA: **14.3:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #11141B on `primary` #A7B4CF: **8.8:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A7A8AA on `surface` #1C1F24: **6.9:1**, AA.
- Dark accent on page (dark): `accent` #D1B281 on `bg` #11141B: **9.1:1**, AAA.
- Dark success on surface (dark): `success` #1BA766 on `surface` #1C1F24: **5.3:1**, AA.
- Dark danger on surface (dark): `danger` #E57361 on `surface` #1C1F24: **5.5:1**, AA.
- Dark warning on surface (dark): `warning` #FF9850 on `surface` #1C1F24: **7.8:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Yankees Blue and Golden Bronze only. Candid Blue and Black Is Back are for the logo and icon, never for charts or UI.
- Charts use five shades of Golden Bronze, plus Yankees Blue as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Golden Bronze itself sits at accent-400; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Golden Bronze in the logo and large graphics.
- Warning hue moved 15° toward orange (OKLCH 65° to 50°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
