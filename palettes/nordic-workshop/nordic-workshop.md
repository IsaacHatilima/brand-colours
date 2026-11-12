# Nordic Workshop

![Nordic Workshop colour system sheet](nordic-workshop.png)

- Character: quiet, functional, crisp
- Suggested uses: industrial design, software tools, professional portfolios
- Source: Rebuilt from the v1 palette Nordic Workshop.
- Files: [CSS tokens](nordic-workshop.css) · [JSON tokens](nordic-workshop.tokens.json) · [Colour sheet](nordic-workshop.png)

Brand colours: Carrier Pigeon Blue #879398 (primary), Decaying Leaf #D67735 (accent). Charts: Decaying Leaf shades plus Carrier Pigeon Blue. Logo and icon only: Lemon Meringue #F4E397 (spark), Neverything #15191A (ink).

## Brand colours

- Brand 1 · primary: [Carrier Pigeon Blue](../../colors/carrier-pigeon-blue.md) (#879398, RGB 135, 147, 152), the primary scale's anchor at step 400. Light UI uses primary-600 (#556064); dark UI uses primary-300 (#A7AFB2).
- Brand 2 · accent: [Decaying Leaf](../../colors/decaying-leaf.md) (#D67735, RGB 214, 119, 53), the accent scale's anchor at step 400. Light UI uses accent-600 (#944600); dark UI uses accent-300 (#DF9F77).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #646767 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Lemon Meringue and Neverything never appear as UI colours.

- Spark: [Lemon Meringue](../../colors/lemon-meringue.md) (#F4E397). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Neverything](../../colors/neverything.md) (#15191A). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Neverything | Carrier Pigeon Blue | Decaying Leaf |
|---|---|---|---|---|
| Carrier Pigeon Blue | ✓ 3.0 | ✓ 5.6 | same | ✗ 1.0 |
| Decaying Leaf | ✓ 3.1 | ✓ 5.5 | ✗ 1.0 | same |
| Lemon Meringue | ✗ 1.2 | ✓ 13.7 | ✗ 2.4 | ✗ 2.5 |
| Neverything | ✓ 17.0 | same | ✓ 5.6 | ✓ 5.5 |
| Paper | same | ✓ 17.0 | ✓ 3.0 | ✓ 3.1 |

- On Paper: Carrier Pigeon Blue, Decaying Leaf, Neverything.
- On Neverything: Carrier Pigeon Blue, Decaying Leaf, Lemon Meringue, Paper.
- On Carrier Pigeon Blue: Neverything, Paper.
- On Decaying Leaf: Neverything, Paper.

## Pairing rationale

A barely-blue grey primary keeps the interface almost monochrome, so the burnt-orange accent does all the signalling, like a safety mark on a workbench. Pale lemon lights the mark.

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
| primary | #556064 | #A7AFB2 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Carrier Pigeon Blue (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #434B4E | #C8CCCF | Hover and pressed fill of `primary`. |
| primary-soft | #F4F5F6 | #303639 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #15191A | Text and icons on `primary` and `primary-hover` (6.5:1 light, 7.9:1 dark). Dark mode uses ink, not white. |
| link | #434B4E | #C8CCCF | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #303639 | #E4E6E7 | Hover state of `link`. |
| accent | #944600 | #DF9F77 | The single secondary hue, Decaying Leaf: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FBF3EF | #381B07 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #15191A | Text and icons on `accent` (6.7:1 light, 7.9:1 dark). |
| focus | #944600 | #DF9F77 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.4:1 on `bg` in light, 7.9:1 in dark. It uses the accent so it never blends into Carrier Pigeon Blue controls. |
| selection | #E4E6E7 | #303639 | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F3F3 | #2A2E2F | Fill of disabled buttons and inputs. |
| disabled-text | #838686 | #646767 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1EA967 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #15191A | Text on solid `success` fills. |
| warning | #845F00 | #E1AD1F | Warning text, icons and fills (5.8:1 light, 7.6:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F5F1D9 | #27210A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #15191A | Text on solid `warning` fills. |
| danger | #B82F39 | #E57173 | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E7 | #2E1516 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #15191A | Text on solid `danger` fills. |
| info | #434B4E | #C8CCCF | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F4F5F6 | #303639 | Background of info banners. Text on it uses `info`. |
| chart-1 | #944600 | #DF9F77 | Chart series 1, the anchor shade of Decaying Leaf. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #552805 | #F5E2D7 | Chart series 2, a darker Decaying Leaf in light and a lighter Decaying Leaf in dark. |
| chart-3 | #D67735 | #BB5A00 | Chart series 3, a lighter Decaying Leaf in light and a deeper Decaying Leaf in dark. |
| chart-4 | #763600 | #EBC3AC | Chart series 4, a mid shade of Decaying Leaf. |
| chart-5 | #BB5A00 | #D67735 | Chart series 5, the remaining Decaying Leaf shade that still holds 3:1. |
| chart-alt | #556064 | #A7AFB2 | The one contrasting chart series: Carrier Pigeon Blue, the primary brand colour. Chart colours are only Decaying Leaf shades and Carrier Pigeon Blue, never status or logo colours. |
| chart-grid | #E1E4E5 | #35393A | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #15191A | #15191A | Raw near-black, Neverything: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F4E397 | #F4E397 | Logo and icon only: Lemon Meringue, the highlight or signal dot. Never a UI colour. |
| logo-ink | #15191A | #15191A | Logo and icon only: wordmark and one-colour versions, Neverything. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Carrier Pigeon Blue at primary-400, Decaying Leaf at accent-400. Identical in both themes.

| Step | Primary (Carrier Pigeon Blue) | Primary roles | Accent (Decaying Leaf) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F4F5F6 | light: primary-soft | #FBF3EF | light: accent-soft | #F7FAFA |
| 100 | #E4E6E7 | light: selection; dark: link-hover | #F5E2D7 | dark: chart-2 | #F0F3F3 |
| 200 | #C8CCCF | dark: primary-hover, link | #EBC3AC | dark: chart-4 | #E1E4E5 |
| 300 | #A7AFB2 | dark: primary | #DF9F77 | dark: accent, chart-1 | #CACDCD |
| 400 | #879398 | brand anchor | #D67735 | brand anchor; light: chart-3; dark: chart-5 | #A6A9AA |
| 500 | #6D7A7F |  | #BB5A00 | light: chart-5; dark: chart-3 | #838686 |
| 600 | #556064 | light: primary | #944600 | light: accent, chart-1 | #646767 |
| 700 | #434B4E | light: primary-hover, link | #763600 | light: chart-4 | #454848 |
| 800 | #303639 | light: link-hover; dark: primary-soft, selection | #552805 | light: chart-2 | #2E3031 |
| 900 | #202426 |  | #381B07 | dark: accent-soft | #1A1C1D |
| 950 | #131516 |  | #201006 |  | #101213 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #15191A on `bg` #FAFAFA: **17.0:1**, AAA.
- Muted on page (light): `text-muted` #646767 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #556064: **6.5:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #944600: **6.7:1**, AA.
- Link on page (light): `link` #434B4E on `bg` #FAFAFA: **8.5:1**, AAA.
- Danger on soft (light): `danger` #B82F39 on `danger-soft` #FBE9E7: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #15191A on `primary` #A7AFB2: **7.9:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A6A9AA on `surface` #202425: **6.6:1**, AA.
- Dark accent on page (dark): `accent` #DF9F77 on `bg` #15191A: **7.9:1**, AAA.
- Dark success on surface (dark): `success` #1EA967 on `surface` #202425: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E57173 on `surface` #202425: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #E1AD1F on `surface` #202425: **7.6:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Carrier Pigeon Blue and Decaying Leaf only. Lemon Meringue and Neverything are for the logo and icon, never for charts or UI.
- Charts use five shades of Decaying Leaf, plus Carrier Pigeon Blue as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Carrier Pigeon Blue itself sits at primary-400; light-mode UI uses primary-600 so labels and text pass 4.5:1. Use the exact Carrier Pigeon Blue in the logo and large graphics.
- Decaying Leaf itself sits at accent-400; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Decaying Leaf in the logo and large graphics.
- Lemon Meringue reaches 3:1 only on Neverything; keep it off Carrier Pigeon Blue and Decaying Leaf grounds.
- Warning hue moved 17° toward yellow (OKLCH 65° to 82°) to stay apart from the brand hues.
- Danger hue moved 10° toward crimson (OKLCH 32° to 22°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
