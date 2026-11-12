# Ink and Poppy

![Ink and Poppy colour system sheet](ink-and-poppy.png)

- Character: bold, economical, memorable
- Suggested uses: editorial identities, galleries, event posters
- Source: Rebuilt from the v1 palette Ink and Poppy.
- Files: [CSS tokens](ink-and-poppy.css) · [JSON tokens](ink-and-poppy.tokens.json) · [Colour sheet](ink-and-poppy.png)

Brand colours: Flag Red #D81B21 (primary), Lapis Jewel #0C5F9A (accent). Charts: Lapis Jewel shades plus Flag Red. Logo and icon only: Bright Gold #F4D80E (spark), Thamar Black #181718 (ink).

## Brand colours

- Brand 1 · primary: [Flag Red](../../colors/flag-red.md) (#D81B21, RGB 216, 27, 33), the primary scale's anchor at step 500. Light UI uses primary-500 (#D81B21); dark UI uses primary-300 (#F78B80).
- Brand 2 · accent: [Lapis Jewel](../../colors/lapis-jewel.md) (#0C5F9A, RGB 12, 95, 154), the accent scale's anchor at step 600. Light UI uses accent-600 (#0C5F9A); dark UI uses accent-300 (#85B5E1).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #676567 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Bright Gold and Thamar Black never appear as UI colours.

- Spark: [Bright Gold](../../colors/bright-gold.md) (#F4D80E). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Thamar Black](../../colors/thamar-black.md) (#181718). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Thamar Black | Flag Red | Lapis Jewel |
|---|---|---|---|---|
| Flag Red | ✓ 4.9 | ✓ 3.5 | same | ✗ 1.3 |
| Lapis Jewel | ✓ 6.5 | ✗ 2.7 | ✗ 1.3 | same |
| Bright Gold | ✗ 1.4 | ✓ 12.5 | ✓ 3.6 | ✓ 4.7 |
| Thamar Black | ✓ 17.1 | same | ✓ 3.5 | ✗ 2.7 |
| Paper | same | ✓ 17.1 | ✓ 4.9 | ✓ 6.5 |

- On Paper: Flag Red, Lapis Jewel, Thamar Black.
- On Thamar Black: Flag Red, Bright Gold, Paper.
- On Flag Red: Bright Gold, Thamar Black, Paper.
- On Lapis Jewel: Bright Gold, Paper.

## Pairing rationale

Poppy red on ink stays the signature. The v1 palette had no second hue, so a lapis blue from the library becomes the accent and focus colour, keeping focus rings from reading as errors. Bright gold completes a poster-like primary set in the mark.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #181718 | Page background: a plain off-white in light, the Thamar Black ink in dark. Text on it uses `text` (17.1:1) and `text-muted` (5.5:1 light, 7.5:1 dark). |
| surface | #FFFFFF | #232223 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #2D2C2D | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F3F1F3 | #1D1C1D | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E4E3E4 | #383738 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #868586 | #767576 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #181718 | #FAFAFA | Primary text and icons on every surface. Thamar Black in light; the paper off-white in dark. |
| text-muted | #676567 | #A9A8A9 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #D81B21 | #F78B80 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Flag Red (primary-500 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #B00011 | #FBB9B1 | Hover and pressed fill of `primary`. |
| primary-soft | #FFF2F0 | #621210 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #181718 | Text and icons on `primary` and `primary-hover` (5.1:1 light, 7.6:1 dark). Dark mode uses ink, not white. |
| link | #B00011 | #FBB9B1 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #881113 | #FDDDD9 | Hover state of `link`. |
| accent | #0C5F9A | #85B5E1 | The single secondary hue, Lapis Jewel: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F0F6FB | #0D2539 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #181718 | Text and icons on `accent` (6.7:1 light, 8.3:1 dark). |
| focus | #0C5F9A | #85B5E1 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.5:1 on `bg` in light, 8.3:1 in dark. It uses the accent so it never blends into Flag Red controls. |
| selection | #FDDDD9 | #621210 | Text selection background. Text keeps `text`. |
| disabled-bg | #F3F1F3 | #2D2C2D | Fill of disabled buttons and inputs. |
| disabled-text | #868586 | #676567 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1EA967 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #181718 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.5:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #181718 | Text on solid `warning` fills. |
| danger | #B33C00 | #E37653 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.3:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E3 | #2E170F | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #181718 | Text on solid `danger` fills. |
| info | #B00011 | #FBB9B1 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #FFF2F0 | #621210 | Background of info banners. Text on it uses `info`. |
| chart-1 | #0C5F9A | #85B5E1 | Chart series 1, the anchor shade of Lapis Jewel. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #113756 | #DBE8F5 | Chart series 2, a darker Lapis Jewel in light and a lighter Lapis Jewel in dark. |
| chart-3 | #4E9ADB | #237CC2 | Chart series 3, a lighter Lapis Jewel in light and a deeper Lapis Jewel in dark. |
| chart-4 | #124B77 | #B4D1EB | Chart series 4, a mid shade of Lapis Jewel. |
| chart-5 | #237CC2 | #4E9ADB | Chart series 5, the remaining Lapis Jewel shade that still holds 3:1. |
| chart-alt | #D81B21 | #F78B80 | The one contrasting chart series: Flag Red, the primary brand colour. Chart colours are only Lapis Jewel shades and Flag Red, never status or logo colours. |
| chart-grid | #E4E3E4 | #383738 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #181718 | #181718 | Raw near-black, Thamar Black: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F4D80E | #F4D80E | Logo and icon only: Bright Gold, the highlight or signal dot. Never a UI colour. |
| logo-ink | #181718 | #181718 | Logo and icon only: wordmark and one-colour versions, Thamar Black. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Flag Red at primary-500, Lapis Jewel at accent-600. Identical in both themes.

| Step | Primary (Flag Red) | Primary roles | Accent (Lapis Jewel) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #FFF2F0 | light: primary-soft | #F0F6FB | light: accent-soft | #FAF8FA |
| 100 | #FDDDD9 | light: selection; dark: link-hover | #DBE8F5 | dark: chart-2 | #F3F1F3 |
| 200 | #FBB9B1 | dark: primary-hover, link | #B4D1EB | dark: chart-4 | #E4E3E4 |
| 300 | #F78B80 | dark: primary | #85B5E1 | dark: accent, chart-1 | #CDCBCD |
| 400 | #F45149 |  | #4E9ADB | light: chart-3; dark: chart-5 | #A9A8A9 |
| 500 | #D81B21 | brand anchor; light: primary | #237CC2 | light: chart-5; dark: chart-3 | #868586 |
| 600 | #B00011 | light: primary-hover, link | #0C5F9A | brand anchor; light: accent, chart-1 | #676567 |
| 700 | #881113 | light: link-hover | #124B77 | light: chart-4 | #484748 |
| 800 | #621210 | dark: primary-soft, selection | #113756 | light: chart-2 | #313031 |
| 900 | #410F0D |  | #0D2539 | dark: accent-soft | #1D1C1D |
| 950 | #260B08 |  | #091621 |  | #131213 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #181718 on `bg` #FAFAFA: **17.1:1**, AAA.
- Muted on page (light): `text-muted` #676567 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #D81B21: **5.1:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #0C5F9A: **6.7:1**, AA.
- Link on page (light): `link` #B00011 on `bg` #FAFAFA: **7.0:1**, AAA.
- Danger on soft (light): `danger` #B33C00 on `danger-soft` #FBE9E3: **5.0:1**, AA.
- Dark primary button (dark): `on-primary` #181718 on `primary` #F78B80: **7.6:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A9A8A9 on `surface` #232223: **6.7:1**, AA.
- Dark accent on page (dark): `accent` #85B5E1 on `bg` #181718: **8.3:1**, AAA.
- Dark success on surface (dark): `success` #1EA967 on `surface` #232223: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E37653 on `surface` #232223: **5.3:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #232223: **7.5:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Flag Red and Lapis Jewel only. Bright Gold and Thamar Black are for the logo and icon, never for charts or UI.
- Charts use five shades of Lapis Jewel, plus Flag Red as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Danger hue moved 8° toward orange-red (OKLCH 32° to 40°) to stay apart from the brand hues.
- Danger still sits within 13° of a brand hue. Never signal danger by colour alone: always pair it with its icon and a word, and keep brand-coloured buttons away from destructive actions.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
