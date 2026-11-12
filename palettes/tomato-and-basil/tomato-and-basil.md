# Tomato and Basil

![Tomato and Basil colour system sheet](tomato-and-basil.png)

- Character: appetising, lively, homely
- Suggested uses: restaurants, food delivery, recipe apps, delis
- Source: A new combination from the colour library.
- Files: [CSS tokens](tomato-and-basil.css) · [JSON tokens](tomato-and-basil.tokens.json) · [Colour sheet](tomato-and-basil.png)

Brand colours: Gazpacho #C23A23 (primary), Rainforest Matcha #48691A (accent). Charts: Rainforest Matcha shades plus Gazpacho. Logo and icon only: Sunlit Clay #F7BB67 (spark), Darkness #18180F (ink).

## Brand colours

- Brand 1 · primary: [Gazpacho](../../colors/gazpacho.md) (#C23A23, RGB 194, 58, 35), the primary scale's anchor at step 500. Light UI uses primary-500 (#C23A23); dark UI uses primary-300 (#E79280).
- Brand 2 · accent: [Rainforest Matcha](../../colors/rainforest-matcha.md) (#48691A, RGB 72, 105, 26), the accent scale's anchor at step 600. Light UI uses accent-600 (#48691A); dark UI uses accent-300 (#A1BB87).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #666664 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Sunlit Clay and Darkness never appear as UI colours.

- Spark: [Sunlit Clay](../../colors/sunlit-clay.md) (#F7BB67). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Darkness](../../colors/darkness-18180f.md) (#18180F). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Darkness | Gazpacho | Rainforest Matcha |
|---|---|---|---|---|
| Gazpacho | ✓ 5.1 | ✓ 3.3 | same | ✗ 1.2 |
| Rainforest Matcha | ✓ 6.1 | ✗ 2.8 | ✗ 1.2 | same |
| Sunlit Clay | ✗ 1.6 | ✓ 10.4 | ✓ 3.1 | ✓ 3.7 |
| Darkness | ✓ 17.1 | same | ✓ 3.3 | ✗ 2.8 |
| Paper | same | ✓ 17.1 | ✓ 5.1 | ✓ 6.1 |

- On Paper: Gazpacho, Rainforest Matcha, Darkness.
- On Darkness: Gazpacho, Sunlit Clay, Paper.
- On Gazpacho: Sunlit Clay, Darkness, Paper.
- On Rainforest Matcha: Sunlit Clay, Paper.

## Pairing rationale

A ripe tomato red drives calls to action and a basil green accent keeps it fresh. Because the primary is red, danger moves toward crimson and always carries an icon and a word.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #18180F | Page background: a plain off-white in light, the Darkness ink in dark. Text on it uses `text` (17.1:1) and `text-muted` (5.5:1 light, 7.5:1 dark). |
| surface | #FFFFFF | #22231C | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #2D2D26 | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F2F2F0 | #1D1D17 | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E3E3E1 | #383831 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #858583 | #76766E | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #18180F | #FAFAFA | Primary text and icons on every surface. Darkness in light; the paper off-white in dark. |
| text-muted | #666664 | #A8A8A6 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #C23A23 | #E79280 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Gazpacho (primary-500 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #9E2814 | #F1BCB1 | Hover and pressed fill of `primary`. |
| primary-soft | #FDF2F0 | #591C12 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #18180F | Text and icons on `primary` and `primary-hover` (5.4:1 light, 7.5:1 dark). Dark mode uses ink, not white. |
| link | #9E2814 | #F1BCB1 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #7B2415 | #F8DFD9 | Hover state of `link`. |
| accent | #48691A | #A1BB87 | The single secondary hue, Rainforest Matcha: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F3F6F0 | #1C280F | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #18180F | Text and icons on `accent` (6.3:1 light, 8.5:1 dark). |
| focus | #48691A | #A1BB87 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.1:1 on `bg` in light, 8.5:1 in dark. It uses the accent so it never blends into Gazpacho controls. |
| selection | #F8DFD9 | #591C12 | Text selection background. Text keeps `text`. |
| disabled-bg | #F2F2F0 | #2D2D26 | Fill of disabled buttons and inputs. |
| disabled-text | #858583 | #666664 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #01794E | #07A96D | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.5:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EC | #0E2A1F | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #18180F | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.5:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #18180F | Text on solid `warning` fills. |
| danger | #B82E42 | #E5707A | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #18180F | Text on solid `danger` fills. |
| info | #9E2814 | #F1BCB1 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #FDF2F0 | #591C12 | Background of info banners. Text on it uses `info`. |
| chart-1 | #48691A | #A1BB87 | Chart series 1, the anchor shade of Rainforest Matcha. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #2A3B14 | #E2E9DB | Chart series 2, a darker Rainforest Matcha in light and a lighter Rainforest Matcha in dark. |
| chart-3 | #395219 | #60872E | Chart series 3, a lighter Rainforest Matcha in light and a deeper Rainforest Matcha in dark. |
| chart-4 | #60872E | #C4D4B5 | Chart series 4, a mid shade of Rainforest Matcha. |
| chart-5 | #1C280F | #7EA353 | Chart series 5, the remaining Rainforest Matcha shade that still holds 3:1. |
| chart-alt | #C23A23 | #E79280 | The one contrasting chart series: Gazpacho, the primary brand colour. Chart colours are only Rainforest Matcha shades and Gazpacho, never status or logo colours. |
| chart-grid | #E3E3E1 | #383831 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #18180F | #18180F | Raw near-black, Darkness: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F7BB67 | #F7BB67 | Logo and icon only: Sunlit Clay, the highlight or signal dot. Never a UI colour. |
| logo-ink | #18180F | #18180F | Logo and icon only: wordmark and one-colour versions, Darkness. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Gazpacho at primary-500, Rainforest Matcha at accent-600. Identical in both themes.

| Step | Primary (Gazpacho) | Primary roles | Accent (Rainforest Matcha) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #FDF2F0 | light: primary-soft | #F3F6F0 | light: accent-soft | #F9F9F7 |
| 100 | #F8DFD9 | light: selection; dark: link-hover | #E2E9DB | dark: chart-2 | #F2F2F0 |
| 200 | #F1BCB1 | dark: primary-hover, link | #C4D4B5 | dark: chart-4 | #E3E3E1 |
| 300 | #E79280 | dark: primary | #A1BB87 | dark: accent, chart-1 | #CCCCCA |
| 400 | #DF614B |  | #7EA353 | dark: chart-5 | #A8A8A6 |
| 500 | #C23A23 | brand anchor; light: primary | #60872E | light: chart-4; dark: chart-3 | #858583 |
| 600 | #9E2814 | light: primary-hover, link | #48691A | brand anchor; light: accent, chart-1 | #666664 |
| 700 | #7B2415 | light: link-hover | #395219 | light: chart-3 | #474745 |
| 800 | #591C12 | dark: primary-soft, selection | #2A3B14 | light: chart-2 | #30302E |
| 900 | #3C150E |  | #1C280F | light: chart-5; dark: accent-soft | #1C1C1A |
| 950 | #230D09 |  | #10170A |  | #121210 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #18180F on `bg` #FAFAFA: **17.1:1**, AAA.
- Muted on page (light): `text-muted` #666664 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #C23A23: **5.4:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #48691A: **6.3:1**, AA.
- Link on page (light): `link` #9E2814 on `bg` #FAFAFA: **7.3:1**, AAA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #18180F on `primary` #E79280: **7.5:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A8A8A6 on `surface` #22231C: **6.7:1**, AA.
- Dark accent on page (dark): `accent` #A1BB87 on `bg` #18180F: **8.5:1**, AAA.
- Dark success on surface (dark): `success` #07A96D on `surface` #22231C: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E5707A on `surface` #22231C: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #22231C: **7.5:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Gazpacho and Rainforest Matcha only. Sunlit Clay and Darkness are for the logo and icon, never for charts or UI.
- Charts use five shades of Rainforest Matcha, plus Gazpacho as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Success hue moved 3° toward teal (OKLCH 157° to 160°) to stay apart from the brand hues.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.
- Danger still sits within 14° of a brand hue. Never signal danger by colour alone: always pair it with its icon and a word, and keep brand-coloured buttons away from destructive actions.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
