# Aegean Pop

![Aegean Pop colour system sheet](aegean-pop.png)

- Character: sunny, playful, confident
- Suggested uses: travel apps, beach clubs, creator tools, summer events
- Source: Rebuilt from the v1 palette Electric Current.
- Files: [CSS tokens](aegean-pop.css) · [JSON tokens](aegean-pop.tokens.json) · [Colour sheet](aegean-pop.png)

Brand colours: Greek Blue #06A1BF (primary), Tutti Frutti #BF587E (accent). Charts: Tutti Frutti shades plus Greek Blue. Logo and icon only: Trumpet Gold #EAB313 (spark), Neverything #15191A (ink).

## Brand colours

- Brand 1 · primary: [Greek Blue](../../colors/greek-blue.md) (#06A1BF, RGB 6, 161, 191), the primary scale's anchor at step 400. Light UI uses primary-600 (#00697D); dark UI uses primary-300 (#72BACD).
- Brand 2 · accent: [Tutti Frutti](../../colors/tutti-frutti.md) (#BF587E, RGB 191, 88, 126), the accent scale's anchor at step 500. Light UI uses accent-600 (#994162); dark UI uses accent-300 (#E19EB3).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #646767 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Trumpet Gold and Neverything never appear as UI colours.

- Spark: [Trumpet Gold](../../colors/trumpet-gold.md) (#EAB313). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Neverything](../../colors/neverything.md) (#15191A). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Neverything | Greek Blue | Tutti Frutti |
|---|---|---|---|---|
| Greek Blue | ✗ 2.9 | ✓ 5.8 | same | ✗ 1.4 |
| Tutti Frutti | ✓ 4.1 | ✓ 4.1 | ✗ 1.4 | same |
| Trumpet Gold | ✗ 1.8 | ✓ 9.2 | ✗ 1.6 | ✗ 2.2 |
| Neverything | ✓ 17.0 | same | ✓ 5.8 | ✓ 4.1 |
| Paper | same | ✓ 17.0 | ✗ 2.9 | ✓ 4.1 |

- On Paper: Tutti Frutti, Neverything.
- On Neverything: Greek Blue, Tutti Frutti, Trumpet Gold, Paper.
- On Greek Blue: Neverything.
- On Tutti Frutti: Neverything, Paper.

## Pairing rationale

Electric Current's cyan becomes the lead, paired with a raspberry pink accent from the library for holiday energy. Gold remains the logo highlight.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #15191A | Page background: a plain off-white in light, the Neverything ink in dark. Text on it uses `text` (17.0:1) and `text-muted` (5.5:1 light, 7.5:1 dark). |
| surface | #FFFFFF | #202425 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #2A2E2F | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F0F3F3 | #1A1E1F | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E1E4E5 | #35393A | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #838686 | #727778 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #15191A | #FAFAFA | Primary text and icons on every surface. Neverything in light; the paper off-white in dark. |
| text-muted | #646767 | #A6A9AA | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #00697D | #72BACD | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Greek Blue (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #005363 | #ABD3DF | Hover and pressed fill of `primary`. |
| primary-soft | #EFF7F9 | #003C49 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #15191A | Text and icons on `primary` and `primary-hover` (6.3:1 light, 8.1:1 dark). Dark mode uses ink, not white. |
| link | #005363 | #ABD3DF | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #003C49 | #D7E9EF | Hover state of `link`. |
| accent | #994162 | #E19EB3 | The single secondary hue, Tutti Frutti: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FBF3F5 | #381A24 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #15191A | Text and icons on `accent` (6.4:1 light, 8.2:1 dark). |
| focus | #994162 | #E19EB3 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.1:1 on `bg` in light, 8.2:1 in dark. It uses the accent so it never blends into Greek Blue controls. |
| selection | #D7E9EF | #003C49 | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F3F3 | #2A2E2F | Fill of disabled buttons and inputs. |
| disabled-text | #838686 | #646767 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1EA967 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #15191A | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.5:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #15191A | Text on solid `warning` fills. |
| danger | #B8331E | #E57361 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E5 | #2E1612 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #15191A | Text on solid `danger` fills. |
| info | #005363 | #ABD3DF | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #EFF7F9 | #003C49 | Background of info banners. Text on it uses `info`. |
| chart-1 | #994162 | #E19EB3 | Chart series 1, the anchor shade of Tutti Frutti. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #552637 | #F5E1E7 | Chart series 2, a darker Tutti Frutti in light and a lighter Tutti Frutti in dark. |
| chart-3 | #77354D | #BF587E | Chart series 3, a lighter Tutti Frutti in light and a deeper Tutti Frutti in dark. |
| chart-4 | #BF587E | #ECC3CF | Chart series 4, a mid shade of Tutti Frutti. |
| chart-5 | #381A24 | #D87798 | Chart series 5, the remaining Tutti Frutti shade that still holds 3:1. |
| chart-alt | #00697D | #72BACD | The one contrasting chart series: Greek Blue, the primary brand colour. Chart colours are only Tutti Frutti shades and Greek Blue, never status or logo colours. |
| chart-grid | #E1E4E5 | #35393A | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #15191A | #15191A | Raw near-black, Neverything: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #EAB313 | #EAB313 | Logo and icon only: Trumpet Gold, the highlight or signal dot. Never a UI colour. |
| logo-ink | #15191A | #15191A | Logo and icon only: wordmark and one-colour versions, Neverything. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Greek Blue at primary-400, Tutti Frutti at accent-500. Identical in both themes.

| Step | Primary (Greek Blue) | Primary roles | Accent (Tutti Frutti) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #EFF7F9 | light: primary-soft | #FBF3F5 | light: accent-soft | #F7FAFA |
| 100 | #D7E9EF | light: selection; dark: link-hover | #F5E1E7 | dark: chart-2 | #F0F3F3 |
| 200 | #ABD3DF | dark: primary-hover, link | #ECC3CF | dark: chart-4 | #E1E4E5 |
| 300 | #72BACD | dark: primary | #E19EB3 | dark: accent, chart-1 | #CACDCD |
| 400 | #06A1BF | brand anchor | #D87798 | dark: chart-5 | #A6A9AA |
| 500 | #00859E |  | #BF587E | brand anchor; light: chart-4; dark: chart-3 | #838686 |
| 600 | #00697D | light: primary | #994162 | light: accent, chart-1 | #646767 |
| 700 | #005363 | light: primary-hover, link | #77354D | light: chart-3 | #454848 |
| 800 | #003C49 | light: link-hover; dark: primary-soft, selection | #552637 | light: chart-2 | #2E3031 |
| 900 | #012932 |  | #381A24 | light: chart-5; dark: accent-soft | #1A1C1D |
| 950 | #05171C |  | #1F0F14 |  | #101213 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #15191A on `bg` #FAFAFA: **17.0:1**, AAA.
- Muted on page (light): `text-muted` #646767 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #00697D: **6.3:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #994162: **6.4:1**, AA.
- Link on page (light): `link` #005363 on `bg` #FAFAFA: **8.3:1**, AAA.
- Danger on soft (light): `danger` #B8331E on `danger-soft` #FBE9E5: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #15191A on `primary` #72BACD: **8.1:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A6A9AA on `surface` #202425: **6.6:1**, AA.
- Dark accent on page (dark): `accent` #E19EB3 on `bg` #15191A: **8.2:1**, AAA.
- Dark success on surface (dark): `success` #1EA967 on `surface` #202425: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E57361 on `surface` #202425: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #202425: **7.5:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Greek Blue and Tutti Frutti only. Trumpet Gold and Neverything are for the logo and icon, never for charts or UI.
- Charts use five shades of Tutti Frutti, plus Greek Blue as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Greek Blue itself sits at primary-400; light-mode UI uses primary-600 so labels and text pass 4.5:1. Use the exact Greek Blue in the logo and large graphics.
- Tutti Frutti itself sits at accent-500; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Tutti Frutti in the logo and large graphics.
- Trumpet Gold reaches 3:1 only on Neverything; keep it off Greek Blue and Tutti Frutti grounds.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
