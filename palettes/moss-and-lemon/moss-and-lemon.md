# Moss and Lemon

![Moss and Lemon colour system sheet](moss-and-lemon.png)

- Character: curious, organic, buoyant
- Suggested uses: plant shops, natural home goods, creative workshops
- Source: Rebuilt from the v1 palette Moss and Lemon.
- Files: [CSS tokens](moss-and-lemon.css) · [JSON tokens](moss-and-lemon.tokens.json) · [Colour sheet](moss-and-lemon.png)

Brand colours: Fern Frond #68771A (primary), Cherry Kisses #B16067 (accent). Charts: Cherry Kisses shades plus Fern Frond. Logo and icon only: Lemon Meringue #F4E397 (spark), Twilight Zone #1A1C13 (ink).

## Brand colours

- Brand 1 · primary: [Fern Frond](../../colors/fern-frond.md) (#68771A, RGB 104, 119, 26), the primary scale's anchor at step 600. Light UI uses primary-600 (#68771A); dark UI uses primary-300 (#B3C086).
- Brand 2 · accent: [Cherry Kisses](../../colors/cherry-kisses.md) (#B16067, RGB 177, 96, 103), the accent scale's anchor at step 500. Light UI uses accent-600 (#8E494F); dark UI uses accent-300 (#D8A2A5).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #666664 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Lemon Meringue and Twilight Zone never appear as UI colours.

- Spark: [Lemon Meringue](../../colors/lemon-meringue.md) (#F4E397). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Twilight Zone](../../colors/twilight-zone.md) (#1A1C13). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Twilight Zone | Fern Frond | Cherry Kisses |
|---|---|---|---|---|
| Fern Frond | ✓ 4.7 | ✓ 3.5 | same | ✗ 1.1 |
| Cherry Kisses | ✓ 4.2 | ✓ 3.9 | ✗ 1.1 | same |
| Lemon Meringue | ✗ 1.2 | ✓ 13.4 | ✓ 3.8 | ✓ 3.4 |
| Twilight Zone | ✓ 16.5 | same | ✓ 3.5 | ✓ 3.9 |
| Paper | same | ✓ 16.5 | ✓ 4.7 | ✓ 4.2 |

- On Paper: Fern Frond, Cherry Kisses, Twilight Zone.
- On Twilight Zone: Fern Frond, Cherry Kisses, Lemon Meringue, Paper.
- On Fern Frond: Lemon Meringue, Twilight Zone, Paper.
- On Cherry Kisses: Lemon Meringue, Twilight Zone, Paper.

## Pairing rationale

The v1 greens were too grey to carry buttons, so a livelier library moss leads, with a dusty rose accent like a flowering plant. Lemon meringue stays as the logo highlight.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #1A1C13 | Page background: a plain off-white in light, the Twilight Zone ink in dark. Text on it uses `text` (16.5:1) and `text-muted` (5.5:1 light, 7.3:1 dark). |
| surface | #FFFFFF | #252720 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #30312A | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F2F2F0 | #20211B | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E3E3E1 | #3A3C35 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #858583 | #787A72 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #1A1C13 | #FAFAFA | Primary text and icons on every surface. Twilight Zone in light; the paper off-white in dark. |
| text-muted | #666664 | #A8A9A6 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #68771A | #B3C086 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Fern Frond (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #515C19 | #CFD7B5 | Hover and pressed fill of `primary`. |
| primary-soft | #F4F6EF | #394114 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #1A1C13 | Text and icons on `primary` and `primary-hover` (5.0:1 light, 8.9:1 dark). Dark mode uses ink, not white. |
| link | #515C19 | #CFD7B5 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #394114 | #E6EADB | Hover state of `link`. |
| accent | #8E494F | #D8A2A5 | The single secondary hue, Cherry Kisses: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FAF3F3 | #341C1E | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #1A1C13 | Text and icons on `accent` (6.5:1 light, 7.9:1 dark). |
| focus | #8E494F | #D8A2A5 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.3:1 on `bg` in light, 7.9:1 in dark. It uses the accent so it never blends into Fern Frond controls. |
| selection | #E6EADB | #394114 | Text selection background. Text keeps `text`. |
| disabled-bg | #F2F2F0 | #30312A | Fill of disabled buttons and inputs. |
| disabled-text | #858583 | #666664 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #27AD6C | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #1A1C13 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.2:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #1A1C13 | Text on solid `warning` fills. |
| danger | #B33C00 | #E67956 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E3 | #2E170F | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #1A1C13 | Text on solid `danger` fills. |
| info | #515C19 | #CFD7B5 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F4F6EF | #394114 | Background of info banners. Text on it uses `info`. |
| chart-1 | #8E494F | #D8A2A5 | Chart series 1, the anchor shade of Cherry Kisses. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #4F2A2D | #F2E2E3 | Chart series 2, a darker Cherry Kisses in light and a lighter Cherry Kisses in dark. |
| chart-3 | #CB7E83 | #B16067 | Chart series 3, a lighter Cherry Kisses in light and a deeper Cherry Kisses in dark. |
| chart-4 | #6E3A3F | #E6C5C6 | Chart series 4, a mid shade of Cherry Kisses. |
| chart-5 | #B16067 | #CB7E83 | Chart series 5, the remaining Cherry Kisses shade that still holds 3:1. |
| chart-alt | #68771A | #B3C086 | The one contrasting chart series: Fern Frond, the primary brand colour. Chart colours are only Cherry Kisses shades and Fern Frond, never status or logo colours. |
| chart-grid | #E3E3E1 | #3A3C35 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #1A1C13 | #1A1C13 | Raw near-black, Twilight Zone: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F4E397 | #F4E397 | Logo and icon only: Lemon Meringue, the highlight or signal dot. Never a UI colour. |
| logo-ink | #1A1C13 | #1A1C13 | Logo and icon only: wordmark and one-colour versions, Twilight Zone. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Fern Frond at primary-600, Cherry Kisses at accent-500. Identical in both themes.

| Step | Primary (Fern Frond) | Primary roles | Accent (Cherry Kisses) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F4F6EF | light: primary-soft | #FAF3F3 | light: accent-soft | #F9F9F7 |
| 100 | #E6EADB | light: selection; dark: link-hover | #F2E2E3 | dark: chart-2 | #F2F2F0 |
| 200 | #CFD7B5 | dark: primary-hover, link | #E6C5C6 | dark: chart-4 | #E3E3E1 |
| 300 | #B3C086 | dark: primary | #D8A2A5 | dark: accent, chart-1 | #CCCCCA |
| 400 | #99AA4F |  | #CB7E83 | light: chart-3; dark: chart-5 | #A8A9A6 |
| 500 | #809228 |  | #B16067 | brand anchor; light: chart-5; dark: chart-3 | #858583 |
| 600 | #68771A | brand anchor; light: primary | #8E494F | light: accent, chart-1 | #666664 |
| 700 | #515C19 | light: primary-hover, link | #6E3A3F | light: chart-4 | #474745 |
| 800 | #394114 | light: link-hover; dark: primary-soft, selection | #4F2A2D | light: chart-2 | #30302E |
| 900 | #242A0D |  | #341C1E | dark: accent-soft | #1C1C1A |
| 950 | #131608 |  | #1E1011 |  | #121211 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #1A1C13 on `bg` #FAFAFA: **16.5:1**, AAA.
- Muted on page (light): `text-muted` #666664 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #68771A: **5.0:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #8E494F: **6.5:1**, AA.
- Link on page (light): `link` #515C19 on `bg` #FAFAFA: **7.0:1**, AA.
- Danger on soft (light): `danger` #B33C00 on `danger-soft` #FBE9E3: **5.0:1**, AA.
- Dark primary button (dark): `on-primary` #1A1C13 on `primary` #B3C086: **8.9:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A8A9A6 on `surface` #252720: **6.4:1**, AA.
- Dark accent on page (dark): `accent` #D8A2A5 on `bg` #1A1C13: **7.9:1**, AAA.
- Dark success on surface (dark): `success` #27AD6C on `surface` #252720: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E67956 on `surface` #252720: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #252720: **7.2:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Fern Frond and Cherry Kisses only. Lemon Meringue and Twilight Zone are for the logo and icon, never for charts or UI.
- Charts use five shades of Cherry Kisses, plus Fern Frond as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Cherry Kisses itself sits at accent-500; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Cherry Kisses in the logo and large graphics.
- Danger hue moved 8° toward orange-red (OKLCH 32° to 40°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
