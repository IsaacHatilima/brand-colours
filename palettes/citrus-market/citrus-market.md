# Citrus Market

![Citrus Market colour system sheet](citrus-market.png)

- Character: bright, practical, optimistic
- Suggested uses: fresh food, local markets, community initiatives
- Source: Rebuilt from the v1 palette Citrus Market.
- Files: [CSS tokens](citrus-market.css) · [JSON tokens](citrus-market.tokens.json) · [Colour sheet](citrus-market.png)

Brand colours: Fun Green #165F39 (primary), Orange Piñata #F96A15 (accent). Charts: Orange Piñata shades plus Fun Green. Logo and icon only: Tansy #CDC545 (spark), Darkness #14170E (ink).

## Brand colours

- Brand 1 · primary: [Fun Green](../../colors/fun-green.md) (#165F39, RGB 22, 95, 57), the primary scale's anchor at step 700. Light UI uses primary-700 (#165F39); dark UI uses primary-300 (#89C49E).
- Brand 2 · accent: [Orange Piñata](../../colors/orange-pinata.md) (#F96A15, RGB 249, 106, 21), the accent scale's anchor at step 400. Light UI uses accent-600 (#A44100); dark UI uses accent-300 (#F99A6F).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #666664 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Tansy and Darkness never appear as UI colours.

- Spark: [Tansy](../../colors/tansy.md) (#CDC545). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Darkness](../../colors/darkness.md) (#14170E). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Darkness | Fun Green | Orange Piñata |
|---|---|---|---|---|
| Fun Green | ✓ 7.4 | ✗ 2.4 | same | ✗ 2.6 |
| Orange Piñata | ✗ 2.8 | ✓ 6.1 | ✗ 2.6 | same |
| Tansy | ✗ 1.7 | ✓ 10.1 | ✓ 4.3 | ✗ 1.6 |
| Darkness | ✓ 17.4 | same | ✗ 2.4 | ✓ 6.1 |
| Paper | same | ✓ 17.4 | ✓ 7.4 | ✗ 2.8 |

- On Paper: Fun Green, Darkness.
- On Darkness: Orange Piñata, Tansy, Paper.
- On Fun Green: Tansy, Paper.
- On Orange Piñata: Darkness.

## Pairing rationale

Leafy green is dependable enough for every button, and the orange accent is loud enough to sell. Lime-yellow tansy finishes the citrus set in the mark.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #14170E | Page background: a plain off-white in light, the Darkness ink in dark. Text on it uses `text` (17.4:1) and `text-muted` (5.5:1 light, 7.7:1 dark). |
| surface | #FFFFFF | #1F211B | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #292C25 | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F1F2F0 | #1A1C16 | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E3E4E1 | #343630 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #858683 | #73766E | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #14170E | #FAFAFA | Primary text and icons on every surface. Darkness in light; the paper off-white in dark. |
| text-muted | #666664 | #A8A9A6 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #165F39 | #89C49E | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Fun Green (primary-700 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #134429 | #B7DAC2 | Hover and pressed fill of `primary`. |
| primary-soft | #F0F7F2 | #134429 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #14170E | Text and icons on `primary` and `primary-hover` (7.7:1 light, 9.0:1 dark). Dark mode uses ink, not white. |
| link | #165F39 | #B7DAC2 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #134429 | #DCECE1 | Hover state of `link`. |
| accent | #A44100 | #F99A6F | The single secondary hue, Orange Piñata: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FEF2ED | #411500 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #14170E | Text and icons on `accent` (6.3:1 light, 8.5:1 dark). |
| focus | #A44100 | #F99A6F | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.0:1 on `bg` in light, 8.5:1 in dark. It uses the accent so it never blends into Fun Green controls. |
| selection | #DCECE1 | #134429 | Text selection background. Text keeps `text`. |
| disabled-bg | #F1F2F0 | #292C25 | Fill of disabled buttons and inputs. |
| disabled-text | #858683 | #666664 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #007763 | #00A588 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.5:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E2F3EF | #082A25 | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #14170E | Text on solid `success` fills. |
| warning | #8A5B00 | #EAA825 | Warning text, icons and fills (5.9:1 light, 7.8:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F8F0D9 | #29200A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #14170E | Text on solid `warning` fills. |
| danger | #B82E42 | #E5707A | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.4:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #14170E | Text on solid `danger` fills. |
| info | #165F39 | #B7DAC2 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F0F7F2 | #134429 | Background of info banners. Text on it uses `info`. |
| chart-1 | #A44100 | #F99A6F | Chart series 1, the anchor shade of Orange Piñata. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #5F2200 | #FDE1D5 | Chart series 2, a darker Orange Piñata in light and a lighter Orange Piñata in dark. |
| chart-3 | #823200 | #D05400 | Chart series 3, a lighter Orange Piñata in light and a deeper Orange Piñata in dark. |
| chart-4 | #D05400 | #FCC1A8 | Chart series 4, a mid shade of Orange Piñata. |
| chart-5 | #411500 | #F96A15 | Chart series 5, the remaining Orange Piñata shade that still holds 3:1. |
| chart-alt | #165F39 | #89C49E | The one contrasting chart series: Fun Green, the primary brand colour. Chart colours are only Orange Piñata shades and Fun Green, never status or logo colours. |
| chart-grid | #E3E4E1 | #343630 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #14170E | #14170E | Raw near-black, Darkness: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #CDC545 | #CDC545 | Logo and icon only: Tansy, the highlight or signal dot. Never a UI colour. |
| logo-ink | #14170E | #14170E | Logo and icon only: wordmark and one-colour versions, Darkness. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Fun Green at primary-700, Orange Piñata at accent-400. Identical in both themes.

| Step | Primary (Fun Green) | Primary roles | Accent (Orange Piñata) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F0F7F2 | light: primary-soft | #FEF2ED | light: accent-soft | #F8F9F7 |
| 100 | #DCECE1 | light: selection; dark: link-hover | #FDE1D5 | dark: chart-2 | #F1F2F0 |
| 200 | #B7DAC2 | dark: primary-hover, link | #FCC1A8 | dark: chart-4 | #E3E4E1 |
| 300 | #89C49E | dark: primary | #F99A6F | dark: accent, chart-1 | #CBCCCA |
| 400 | #50B179 |  | #F96A15 | brand anchor; dark: chart-5 | #A8A9A6 |
| 500 | #22975C |  | #D05400 | light: chart-4; dark: chart-3 | #858683 |
| 600 | #0C7946 |  | #A44100 | light: accent, chart-1 | #666664 |
| 700 | #165F39 | brand anchor; light: primary, link | #823200 | light: chart-3 | #474745 |
| 800 | #134429 | light: primary-hover, link-hover; dark: primary-soft, selection | #5F2200 | light: chart-2 | #30302E |
| 900 | #0E2C1B |  | #411500 | light: chart-5; dark: accent-soft | #1C1C1A |
| 950 | #09180F |  | #250D03 |  | #121211 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #14170E on `bg` #FAFAFA: **17.4:1**, AAA.
- Muted on page (light): `text-muted` #666664 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #165F39: **7.7:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #A44100: **6.3:1**, AA.
- Link on page (light): `link` #165F39 on `bg` #FAFAFA: **7.4:1**, AAA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #14170E on `primary` #89C49E: **9.0:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A8A9A6 on `surface` #1F211B: **6.9:1**, AA.
- Dark accent on page (dark): `accent` #F99A6F on `bg` #14170E: **8.5:1**, AAA.
- Dark success on surface (dark): `success` #00A588 on `surface` #1F211B: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E5707A on `surface` #1F211B: **5.4:1**, AA.
- Dark warning on surface (dark): `warning` #EAA825 on `surface` #1F211B: **7.8:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Fun Green and Orange Piñata only. Tansy and Darkness are for the logo and icon, never for charts or UI.
- Charts use five shades of Orange Piñata, plus Fun Green as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Orange Piñata itself sits at accent-400; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Orange Piñata in the logo and large graphics.
- Success hue moved 18° toward teal (OKLCH 157° to 175°) to stay apart from the brand hues.
- Warning hue moved 10° toward yellow (OKLCH 65° to 75°) to stay apart from the brand hues.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
