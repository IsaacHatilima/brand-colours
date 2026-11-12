# Coastal Herbarium

![Coastal Herbarium colour system sheet](coastal-herbarium.png)

- Character: fresh, restorative, grounded
- Suggested uses: botanical skincare, garden studios, wellness retreats
- Source: Rebuilt from the v1 palette Coastal Herbarium.
- Files: [CSS tokens](coastal-herbarium.css) · [JSON tokens](coastal-herbarium.tokens.json) · [Colour sheet](coastal-herbarium.png)

Brand colours: Pine Teal #084F4A (primary), Velvet Orchid #6D418B (accent). Charts: Velvet Orchid shades plus Pine Teal. Logo and icon only: Cane Sugar #E2BA80 (spark), Onyx #0D1616 (ink).

## Brand colours

- Brand 1 · primary: [Pine Teal](../../colors/pine-teal-084f4a.md) (#084F4A, RGB 8, 79, 74), the primary scale's anchor at step 700. Light UI uses primary-700 (#084F4A); dark UI uses primary-300 (#86BBB5).
- Brand 2 · accent: [Velvet Orchid](../../colors/velvet-orchid.md) (#6D418B, RGB 109, 65, 139), the accent scale's anchor at step 600. Light UI uses accent-600 (#6D418B); dark UI uses accent-300 (#BE9FD7).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #646767 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Cane Sugar and Onyx never appear as UI colours.

- Spark: [Cane Sugar](../../colors/cane-sugar.md) (#E2BA80). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Onyx](../../colors/onyx-0d1616.md) (#0D1616). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Onyx | Pine Teal | Velvet Orchid |
|---|---|---|---|---|
| Pine Teal | ✓ 9.0 | ✗ 1.9 | same | ✗ 1.2 |
| Velvet Orchid | ✓ 7.2 | ✗ 2.4 | ✗ 1.2 | same |
| Cane Sugar | ✗ 1.7 | ✓ 10.1 | ✓ 5.2 | ✓ 4.2 |
| Onyx | ✓ 17.6 | same | ✗ 1.9 | ✗ 2.4 |
| Paper | same | ✓ 17.6 | ✓ 9.0 | ✓ 7.2 |

- On Paper: Pine Teal, Velvet Orchid, Onyx.
- On Onyx: Cane Sugar, Paper.
- On Pine Teal: Cane Sugar, Paper.
- On Velvet Orchid: Cane Sugar, Paper.

## Pairing rationale

Pine teal stays the anchor. Seagrass sat too close in hue to act as an accent, so a heather-purple orchid from the library plays that role, like pressed flowers on a green page. Cane sugar keeps the sandy warmth in the mark.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #0D1616 | Page background: a plain off-white in light, the Onyx ink in dark. Text on it uses `text` (17.6:1) and `text-muted` (5.5:1 light, 7.8:1 dark). |
| surface | #FFFFFF | #182020 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #222B2B | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F0F3F3 | #131B1B | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E1E4E4 | #2D3535 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #838686 | #6A7474 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.4:1 dark on surface). |
| text | #0D1616 | #FAFAFA | Primary text and icons on every surface. Onyx in light; the paper off-white in dark. |
| text-muted | #646767 | #A6A9A9 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #084F4A | #86BBB5 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Pine Teal (primary-700 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #0D3A36 | #B5D4D0 | Hover and pressed fill of `primary`. |
| primary-soft | #F1F7F6 | #0D3A36 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #0D1616 | Text and icons on `primary` and `primary-hover` (9.4:1 light, 8.6:1 dark). Dark mode uses ink, not white. |
| link | #084F4A | #B5D4D0 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #0D3A36 | #DBEAE8 | Hover state of `link`. |
| accent | #6D418B | #BE9FD7 | The single secondary hue, Velvet Orchid: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F7F3FA | #2A1B34 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #0D1616 | Text and icons on `accent` (7.6:1 light, 8.0:1 dark). |
| focus | #6D418B | #BE9FD7 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 7.2:1 on `bg` in light, 8.0:1 in dark. It uses the accent so it never blends into Pine Teal controls. |
| selection | #DBEAE8 | #0D3A36 | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F3F3 | #222B2B | Fill of disabled buttons and inputs. |
| disabled-text | #838686 | #646767 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1BA766 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.3:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #0D1616 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.9:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #0D1616 | Text on solid `warning` fills. |
| danger | #B8331E | #E57361 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.5:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #0D1616 | Text on solid `danger` fills. |
| info | #084F4A | #B5D4D0 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F1F7F6 | #0D3A36 | Background of info banners. Text on it uses `info`. |
| chart-1 | #6D418B | #BE9FD7 | Chart series 1, the anchor shade of Velvet Orchid. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #3E274E | #EAE2F2 | Chart series 2, a darker Velvet Orchid in light and a lighter Velvet Orchid in dark. |
| chart-3 | #A97ACC | #8E5AB1 | Chart series 3, a lighter Velvet Orchid in light and a deeper Velvet Orchid in dark. |
| chart-4 | #55356C | #D6C4E5 | Chart series 4, a mid shade of Velvet Orchid. |
| chart-5 | #8E5AB1 | #A97ACC | Chart series 5, the remaining Velvet Orchid shade that still holds 3:1. |
| chart-alt | #084F4A | #86BBB5 | The one contrasting chart series: Pine Teal, the primary brand colour. Chart colours are only Velvet Orchid shades and Pine Teal, never status or logo colours. |
| chart-grid | #E1E4E4 | #2D3535 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #0D1616 | #0D1616 | Raw near-black, Onyx: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #E2BA80 | #E2BA80 | Logo and icon only: Cane Sugar, the highlight or signal dot. Never a UI colour. |
| logo-ink | #0D1616 | #0D1616 | Logo and icon only: wordmark and one-colour versions, Onyx. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Pine Teal at primary-700, Velvet Orchid at accent-600. Identical in both themes.

| Step | Primary (Pine Teal) | Primary roles | Accent (Velvet Orchid) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F1F7F6 | light: primary-soft | #F7F3FA | light: accent-soft | #F7FAFA |
| 100 | #DBEAE8 | light: selection; dark: link-hover | #EAE2F2 | dark: chart-2 | #F0F3F3 |
| 200 | #B5D4D0 | dark: primary-hover, link | #D6C4E5 | dark: chart-4 | #E1E4E4 |
| 300 | #86BBB5 | dark: primary | #BE9FD7 | dark: accent, chart-1 | #CACDCD |
| 400 | #4DA49C |  | #A97ACC | light: chart-3; dark: chart-5 | #A6A9A9 |
| 500 | #1D8880 |  | #8E5AB1 | light: chart-5; dark: chart-3 | #838686 |
| 600 | #006962 |  | #6D418B | brand anchor; light: accent, chart-1 | #646767 |
| 700 | #084F4A | brand anchor; light: primary, link | #55356C | light: chart-4 | #454848 |
| 800 | #0D3A36 | light: primary-hover, link-hover; dark: primary-soft, selection | #3E274E | light: chart-2 | #2E3131 |
| 900 | #0C2725 |  | #2A1B34 | dark: accent-soft | #1A1C1C |
| 950 | #091716 |  | #19111F |  | #101212 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #0D1616 on `bg` #FAFAFA: **17.6:1**, AAA.
- Muted on page (light): `text-muted` #646767 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #084F4A: **9.4:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #6D418B: **7.6:1**, AAA.
- Link on page (light): `link` #084F4A on `bg` #FAFAFA: **9.0:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #0D1616 on `primary` #86BBB5: **8.6:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A6A9A9 on `surface` #182020: **7.0:1**, AAA.
- Dark accent on page (dark): `accent` #BE9FD7 on `bg` #0D1616: **8.0:1**, AAA.
- Dark success on surface (dark): `success` #1BA766 on `surface` #182020: **5.3:1**, AA.
- Dark danger on surface (dark): `danger` #E57361 on `surface` #182020: **5.5:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #182020: **7.9:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Pine Teal and Velvet Orchid only. Cane Sugar and Onyx are for the logo and icon, never for charts or UI.
- Charts use five shades of Velvet Orchid, plus Pine Teal as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
