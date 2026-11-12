# Clear Horizon

![Clear Horizon colour system sheet](clear-horizon.png)

- Character: open, dependable, understated
- Suggested uses: consulting, education, B2B services
- Source: Rebuilt from the v1 palette Clear Horizon.
- Files: [CSS tokens](clear-horizon.css) · [JSON tokens](clear-horizon.tokens.json) · [Colour sheet](clear-horizon.png)

Brand colours: Air Force Blue #5E83A3 (primary), Ground Nutmeg #9F5A3C (accent). Charts: Ground Nutmeg shades plus Air Force Blue. Logo and icon only: Bright Gold #F4D80E (spark), Midnight Edition #0D1219 (ink).

## Brand colours

- Brand 1 · primary: [Air Force Blue](../../colors/air-force-blue.md) (#5E83A3, RGB 94, 131, 163), the primary scale's anchor at step 500. Light UI uses primary-600 (#476782); dark UI uses primary-300 (#A0B7CC).
- Brand 2 · accent: [Ground Nutmeg](../../colors/ground-nutmeg.md) (#9F5A3C, RGB 159, 90, 60), the accent scale's anchor at step 600. Light UI uses accent-600 (#9F5A3C); dark UI uses accent-300 (#E0AB95).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #656668 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Bright Gold and Midnight Edition never appear as UI colours.

- Spark: [Bright Gold](../../colors/bright-gold.md) (#F4D80E). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Midnight Edition](../../colors/midnight-edition.md) (#0D1219). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Midnight Edition | Air Force Blue | Ground Nutmeg |
|---|---|---|---|---|
| Air Force Blue | ✓ 3.8 | ✓ 4.7 | same | ✗ 1.3 |
| Ground Nutmeg | ✓ 5.0 | ✓ 3.6 | ✗ 1.3 | same |
| Bright Gold | ✗ 1.4 | ✓ 13.1 | ✗ 2.8 | ✓ 3.7 |
| Midnight Edition | ✓ 18.0 | same | ✓ 4.7 | ✓ 3.6 |
| Paper | same | ✓ 18.0 | ✓ 3.8 | ✓ 5.0 |

- On Paper: Air Force Blue, Ground Nutmeg, Midnight Edition.
- On Midnight Edition: Air Force Blue, Ground Nutmeg, Bright Gold, Paper.
- On Air Force Blue: Midnight Edition, Paper.
- On Ground Nutmeg: Bright Gold, Midnight Edition, Paper.

## Pairing rationale

Steel blue keeps the original calm. The v1 palette had no second hue, so a warm nutmeg from the library adds a quiet complementary accent for focus and highlights. Gold is reserved for the mark.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #0D1219 | Page background: a plain off-white in light, the Midnight Edition ink in dark. Text on it uses `text` (18.0:1) and `text-muted` (5.5:1 light, 7.9:1 dark). |
| surface | #FFFFFF | #191C22 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #23272C | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F1F2F4 | #13171C | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E2E3E5 | #2D3137 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #848587 | #6B7077 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.4:1 dark on surface). |
| text | #0D1219 | #FAFAFA | Primary text and icons on every surface. Midnight Edition in light; the paper off-white in dark. |
| text-muted | #656668 | #A7A8AA | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #476782 | #A0B7CC | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Air Force Blue (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #385065 | #C3D1DE | Hover and pressed fill of `primary`. |
| primary-soft | #F3F5F8 | #293948 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #0D1219 | Text and icons on `primary` and `primary-hover` (5.9:1 light, 9.1:1 dark). Dark mode uses ink, not white. |
| link | #385065 | #C3D1DE | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #293948 | #E1E8EE | Hover state of `link`. |
| accent | #9F5A3C | #E0AB95 | The single secondary hue, Ground Nutmeg: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FAF4F1 | #372016 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #0D1219 | Text and icons on `accent` (5.2:1 light, 9.3:1 dark). |
| focus | #9F5A3C | #E0AB95 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 5.0:1 on `bg` in light, 9.3:1 in dark. It uses the accent so it never blends into Air Force Blue controls. |
| selection | #E1E8EE | #293948 | Text selection background. Text keeps `text`. |
| disabled-bg | #F1F2F4 | #23272C | Fill of disabled buttons and inputs. |
| disabled-text | #848587 | #656668 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1BA766 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.5:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #0D1219 | Text on solid `success` fills. |
| warning | #8A5B00 | #EBA726 | Warning text, icons and fills (5.9:1 light, 8.2:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F8F0D9 | #29200A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #0D1219 | Text on solid `warning` fills. |
| danger | #B82E42 | #E5707A | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.6:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #0D1219 | Text on solid `danger` fills. |
| info | #385065 | #C3D1DE | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F3F5F8 | #293948 | Background of info banners. Text on it uses `info`. |
| chart-1 | #9F5A3C | #E0AB95 | Chart series 1, the anchor shade of Ground Nutmeg. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #563222 | #F4E5DE | Chart series 2, a darker Ground Nutmeg in light and a lighter Ground Nutmeg in dark. |
| chart-3 | #7A4630 | #C0704D | Chart series 3, a lighter Ground Nutmeg in light and a deeper Ground Nutmeg in dark. |
| chart-4 | #C0704D | #EBCBBD | Chart series 4, a mid shade of Ground Nutmeg. |
| chart-5 | #372016 | #D78B6A | Chart series 5, the remaining Ground Nutmeg shade that still holds 3:1. |
| chart-alt | #476782 | #A0B7CC | The one contrasting chart series: Air Force Blue, the primary brand colour. Chart colours are only Ground Nutmeg shades and Air Force Blue, never status or logo colours. |
| chart-grid | #E2E3E5 | #2D3137 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #0D1219 | #0D1219 | Raw near-black, Midnight Edition: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F4D80E | #F4D80E | Logo and icon only: Bright Gold, the highlight or signal dot. Never a UI colour. |
| logo-ink | #0D1219 | #0D1219 | Logo and icon only: wordmark and one-colour versions, Midnight Edition. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Air Force Blue at primary-500, Ground Nutmeg at accent-600. Identical in both themes.

| Step | Primary (Air Force Blue) | Primary roles | Accent (Ground Nutmeg) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F3F5F8 | light: primary-soft | #FAF4F1 | light: accent-soft | #F8F9FB |
| 100 | #E1E8EE | light: selection; dark: link-hover | #F4E5DE | dark: chart-2 | #F1F2F4 |
| 200 | #C3D1DE | dark: primary-hover, link | #EBCBBD | dark: chart-4 | #E2E3E5 |
| 300 | #A0B7CC | dark: primary | #E0AB95 | dark: accent, chart-1 | #CBCCCE |
| 400 | #7B9EBC |  | #D78B6A | dark: chart-5 | #A7A8AA |
| 500 | #5E83A3 | brand anchor | #C0704D | light: chart-4; dark: chart-3 | #848587 |
| 600 | #476782 | light: primary | #9F5A3C | brand anchor; light: accent, chart-1 | #656668 |
| 700 | #385065 | light: primary-hover, link | #7A4630 | light: chart-3 | #464749 |
| 800 | #293948 | light: link-hover; dark: primary-soft, selection | #563222 | light: chart-2 | #2F3032 |
| 900 | #1B262F |  | #372016 | light: chart-5; dark: accent-soft | #1B1C1E |
| 950 | #0F151A |  | #1E110B |  | #111214 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #0D1219 on `bg` #FAFAFA: **18.0:1**, AAA.
- Muted on page (light): `text-muted` #656668 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #476782: **5.9:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #9F5A3C: **5.2:1**, AA.
- Link on page (light): `link` #385065 on `bg` #FAFAFA: **8.0:1**, AAA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #0D1219 on `primary` #A0B7CC: **9.1:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A7A8AA on `surface` #191C22: **7.2:1**, AAA.
- Dark accent on page (dark): `accent` #E0AB95 on `bg` #0D1219: **9.3:1**, AAA.
- Dark success on surface (dark): `success` #1BA766 on `surface` #191C22: **5.5:1**, AA.
- Dark danger on surface (dark): `danger` #E5707A on `surface` #191C22: **5.6:1**, AA.
- Dark warning on surface (dark): `warning` #EBA726 on `surface` #191C22: **8.2:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Air Force Blue and Ground Nutmeg only. Bright Gold and Midnight Edition are for the logo and icon, never for charts or UI.
- Charts use five shades of Ground Nutmeg, plus Air Force Blue as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Air Force Blue itself sits at primary-500; light-mode UI uses primary-600 so labels and text pass 4.5:1. Use the exact Air Force Blue in the logo and large graphics.
- Warning hue moved 9° toward yellow (OKLCH 65° to 74°) to stay apart from the brand hues.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
