# Monochrome Foundry

![Monochrome Foundry colour system sheet](monochrome-foundry.png)

- Character: precise, neutral, adaptable
- Suggested uses: architecture portfolios, industrial services, photography
- Source: Rebuilt from the v1 palette Monochrome Foundry.
- Files: [CSS tokens](monochrome-foundry.css) · [JSON tokens](monochrome-foundry.tokens.json) · [Colour sheet](monochrome-foundry.png)

Brand colours: Graphite Black #26292A (primary), Americana #0473B5 (accent). Charts: Americana shades plus Graphite Black. Logo and icon only: Bright Gold #F4D80E (spark), Dreamless Sleep #120F10 (ink).

## Brand colours

- Brand 1 · primary: [Graphite Black](../../colors/graphite-black.md) (#26292A, RGB 38, 41, 42), the primary scale's anchor at step 900. Light UI uses primary-900 (#26292A); dark UI uses primary-300 (#B1B5B6).
- Brand 2 · accent: [Americana](../../colors/americana.md) (#0473B5, RGB 4, 115, 181), the accent scale's anchor at step 600. Light UI uses accent-600 (#0473B5); dark UI uses accent-400 (#49A7EF).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #686566 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Bright Gold and Dreamless Sleep never appear as UI colours.

- Spark: [Bright Gold](../../colors/bright-gold.md) (#F4D80E). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Dreamless Sleep](../../colors/dreamless-sleep.md) (#120F10). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Dreamless Sleep | Graphite Black | Americana |
|---|---|---|---|---|
| Graphite Black | ✓ 14.0 | ✗ 1.3 | same | ✗ 2.9 |
| Americana | ✓ 4.9 | ✓ 3.7 | ✗ 2.9 | same |
| Bright Gold | ✗ 1.4 | ✓ 13.3 | ✓ 10.2 | ✓ 3.6 |
| Dreamless Sleep | ✓ 18.3 | same | ✗ 1.3 | ✓ 3.7 |
| Paper | same | ✓ 18.3 | ✓ 14.0 | ✓ 4.9 |

- On Paper: Graphite Black, Americana, Dreamless Sleep.
- On Dreamless Sleep: Americana, Bright Gold, Paper.
- On Graphite Black: Bright Gold, Paper.
- On Americana: Bright Gold, Dreamless Sleep, Paper.

## Pairing rationale

Graphite is the primary, so buttons and active marks are near-black in light mode and pale grey in dark mode. A single clear blue from the library is the only hue, for links in charts, focus and highlights. Gold is the mark's spark.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #120F10 | Page background: a plain off-white in light, the Dreamless Sleep ink in dark. Text on it uses `text` (18.3:1) and `text-muted` (5.5:1 light, 8.0:1 dark). |
| surface | #FFFFFF | #1C191A | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #272324 | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F4F1F2 | #171415 | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E5E2E3 | #312E2F | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #878485 | #716D6F | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.4:1 dark on surface). |
| text | #120F10 | #FAFAFA | Primary text and icons on every surface. Dreamless Sleep in light; the paper off-white in dark. |
| text-muted | #686566 | #AAA7A8 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #26292A | #B1B5B6 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Graphite Black (primary-900 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #141515 | #CED0D1 | Hover and pressed fill of `primary`. |
| primary-soft | #F5F5F5 | #393B3C | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #120F10 | Text and icons on `primary` and `primary-hover` (14.7:1 light, 9.2:1 dark). Dark mode uses ink, not white. |
| link | #26292A | #CED0D1 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #141515 | #E6E7E8 | Hover state of `link`. |
| accent | #0473B5 | #49A7EF | The single secondary hue, Americana: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #EFF6FC | #0C293F | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #120F10 | Text and icons on `accent` (5.1:1 light, 7.3:1 dark). |
| focus | #0473B5 | #49A7EF | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 4.9:1 on `bg` in light, 7.3:1 in dark. It uses the accent so it never blends into Graphite Black controls. |
| selection | #E6E7E8 | #393B3C | Text selection background. Text keeps `text`. |
| disabled-bg | #F4F1F2 | #272324 | Fill of disabled buttons and inputs. |
| disabled-text | #878485 | #686566 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1BA766 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.6:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #120F10 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 8.3:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #120F10 | Text on solid `warning` fills. |
| danger | #B8331E | #E57361 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.8:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #120F10 | Text on solid `danger` fills. |
| info | #26292A | #CED0D1 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F5F5F5 | #393B3C | Background of info banners. Text on it uses `info`. |
| chart-1 | #0473B5 | #49A7EF | Chart series 1, the anchor shade of Americana. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #0F3F62 | #B5D7F4 | Chart series 2, a darker Americana in light and a lighter Americana in dark. |
| chart-3 | #10598B | #0473B5 | Chart series 3, a lighter Americana in light and a deeper Americana in dark. |
| chart-4 | #168DDA | #86BFEF | Chart series 4, a mid shade of Americana. |
| chart-5 | #0C293F | #168DDA | Chart series 5, the remaining Americana shade that still holds 3:1. |
| chart-alt | #26292A | #B1B5B6 | The one contrasting chart series: Graphite Black, the primary brand colour. Chart colours are only Americana shades and Graphite Black, never status or logo colours. |
| chart-grid | #E5E2E3 | #312E2F | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #120F10 | #120F10 | Raw near-black, Dreamless Sleep: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F4D80E | #F4D80E | Logo and icon only: Bright Gold, the highlight or signal dot. Never a UI colour. |
| logo-ink | #120F10 | #120F10 | Logo and icon only: wordmark and one-colour versions, Dreamless Sleep. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Graphite Black at primary-900, Americana at accent-600. Identical in both themes.

| Step | Primary (Graphite Black) | Primary roles | Accent (Americana) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F5F5F5 | light: primary-soft | #EFF6FC | light: accent-soft | #FBF8F9 |
| 100 | #E6E7E8 | light: selection; dark: link-hover | #DBEAF8 |  | #F4F1F2 |
| 200 | #CED0D1 | dark: primary-hover, link | #B5D7F4 | dark: chart-2 | #E5E2E3 |
| 300 | #B1B5B6 | dark: primary | #86BFEF | dark: chart-4 | #CECBCC |
| 400 | #969B9D |  | #49A7EF | dark: accent, chart-1 | #AAA7A8 |
| 500 | #7B8183 |  | #168DDA | light: chart-4; dark: chart-5 | #878485 |
| 600 | #616668 |  | #0473B5 | brand anchor; light: accent, chart-1; dark: chart-3 | #686566 |
| 700 | #4D5152 |  | #10598B | light: chart-3 | #494647 |
| 800 | #393B3C | dark: primary-soft, selection | #0F3F62 | light: chart-2 | #322F30 |
| 900 | #26292A | brand anchor; light: primary, link | #0C293F | light: chart-5; dark: accent-soft | #1D1B1C |
| 950 | #141515 | light: primary-hover, link-hover | #071622 |  | #131112 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #120F10 on `bg` #FAFAFA: **18.3:1**, AAA.
- Muted on page (light): `text-muted` #686566 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #26292A: **14.7:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #0473B5: **5.1:1**, AA.
- Link on page (light): `link` #26292A on `bg` #FAFAFA: **14.0:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #120F10 on `primary` #B1B5B6: **9.2:1**, AAA.
- Dark muted on surface (dark): `text-muted` #AAA7A8 on `surface` #1C191A: **7.3:1**, AAA.
- Dark accent on page (dark): `accent` #49A7EF on `bg` #120F10: **7.3:1**, AAA.
- Dark success on surface (dark): `success` #1BA766 on `surface` #1C191A: **5.6:1**, AA.
- Dark danger on surface (dark): `danger` #E57361 on `surface` #1C191A: **5.8:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #1C191A: **8.3:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Graphite Black and Americana only. Bright Gold and Dreamless Sleep are for the logo and icon, never for charts or UI.
- Charts use five shades of Americana, plus Graphite Black as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
