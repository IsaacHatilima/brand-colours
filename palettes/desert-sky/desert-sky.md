# Desert Sky

![Desert Sky colour system sheet](desert-sky.png)

- Character: earthy, calm, balanced
- Suggested uses: travel, interiors, lifestyle brands
- Source: Rebuilt from the v1 palette Desert Sky.
- Files: [CSS tokens](desert-sky.css) · [JSON tokens](desert-sky.tokens.json) · [Colour sheet](desert-sky.png)

Brand colours: Cotton Cardigan #7693B7 (primary), Buffed Copper #DA9071 (accent). Charts: Buffed Copper shades plus Cotton Cardigan. Logo and icon only: Sunlit Clay #F7BB67 (spark), Black Umber #1E1816 (ink).

## Brand colours

- Brand 1 · primary: [Cotton Cardigan](../../colors/cotton-cardigan.md) (#7693B7, RGB 118, 147, 183), the primary scale's anchor at step 400. Light UI uses primary-600 (#455F80); dark UI uses primary-300 (#9BAFC8).
- Brand 2 · accent: [Buffed Copper](../../colors/buffed-copper.md) (#DA9071, RGB 218, 144, 113), the accent scale's anchor at step 400. Light UI uses accent-600 (#975539); dark UI uses accent-300 (#E2AF9A).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #686564 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Sunlit Clay and Black Umber never appear as UI colours.

- Spark: [Sunlit Clay](../../colors/sunlit-clay.md) (#F7BB67). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Black Umber](../../colors/black-umber.md) (#1E1816). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Black Umber | Cotton Cardigan | Buffed Copper |
|---|---|---|---|---|
| Cotton Cardigan | ✓ 3.0 | ✓ 5.5 | same | ✗ 1.2 |
| Buffed Copper | ✗ 2.5 | ✓ 6.9 | ✗ 1.2 | same |
| Sunlit Clay | ✗ 1.6 | ✓ 10.2 | ✗ 1.8 | ✗ 1.5 |
| Black Umber | ✓ 16.8 | same | ✓ 5.5 | ✓ 6.9 |
| Paper | same | ✓ 16.8 | ✓ 3.0 | ✗ 2.5 |

- On Paper: Cotton Cardigan, Black Umber.
- On Black Umber: Cotton Cardigan, Buffed Copper, Sunlit Clay, Paper.
- On Cotton Cardigan: Black Umber, Paper.
- On Buffed Copper: Black Umber.

## Pairing rationale

Dusty sky blue and sun-warmed copper are complementary, so the accent is unmistakable while both stay soft. Sunlit clay gives the mark a desert-light highlight.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #1E1816 | Page background: a plain off-white in light, the Black Umber ink in dark. Text on it uses `text` (16.8:1) and `text-muted` (5.5:1 light, 7.3:1 dark). |
| surface | #FFFFFF | #292321 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #342D2B | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F4F1F0 | #231D1B | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E5E2E1 | #3F3836 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #878484 | #7D7673 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.6:1 light, 3.5:1 dark on surface). |
| text | #1E1816 | #FAFAFA | Primary text and icons on every surface. Black Umber in light; the paper off-white in dark. |
| text-muted | #686564 | #AAA7A7 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #455F80 | #9BAFC8 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Cotton Cardigan (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #374B63 | #C1CDDC | Hover and pressed fill of `primary`. |
| primary-soft | #F3F5F8 | #283647 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #1E1816 | Text and icons on `primary` and `primary-hover` (6.6:1 light, 7.8:1 dark). Dark mode uses ink, not white. |
| link | #374B63 | #C1CDDC | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #283647 | #E1E6ED | Hover state of `link`. |
| accent | #975539 | #E2AF9A | The single secondary hue, Buffed Copper: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FAF4F1 | #361F16 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #1E1816 | Text and icons on `accent` (5.7:1 light, 9.0:1 dark). |
| focus | #975539 | #E2AF9A | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 5.5:1 on `bg` in light, 9.0:1 in dark. It uses the accent so it never blends into Cotton Cardigan controls. |
| selection | #E1E6ED | #283647 | Text selection background. Text keeps `text`. |
| disabled-bg | #F4F1F0 | #342D2B | Fill of disabled buttons and inputs. |
| disabled-text | #878484 | #686564 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #21AA69 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #1E1816 | Text on solid `success` fills. |
| warning | #8A5B00 | #EBA726 | Warning text, icons and fills (5.9:1 light, 7.4:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F8F0D9 | #29200A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #1E1816 | Text on solid `warning` fills. |
| danger | #B82E42 | #E7727B | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #1E1816 | Text on solid `danger` fills. |
| info | #374B63 | #C1CDDC | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F3F5F8 | #283647 | Background of info banners. Text on it uses `info`. |
| chart-1 | #975539 | #E2AF9A | Chart series 1, the anchor shade of Buffed Copper. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #533021 | #F4E5DF | Chart series 2, a darker Buffed Copper in light and a lighter Buffed Copper in dark. |
| chart-3 | #75432E | #BD704F | Chart series 3, a lighter Buffed Copper in light and a deeper Buffed Copper in dark. |
| chart-4 | #BD704F | #ECCDC0 | Chart series 4, a mid shade of Buffed Copper. |
| chart-5 | #361F16 | #DA9071 | Chart series 5, the remaining Buffed Copper shade that still holds 3:1. |
| chart-alt | #455F80 | #9BAFC8 | The one contrasting chart series: Cotton Cardigan, the primary brand colour. Chart colours are only Buffed Copper shades and Cotton Cardigan, never status or logo colours. |
| chart-grid | #E5E2E1 | #3F3836 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #1E1816 | #1E1816 | Raw near-black, Black Umber: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F7BB67 | #F7BB67 | Logo and icon only: Sunlit Clay, the highlight or signal dot. Never a UI colour. |
| logo-ink | #1E1816 | #1E1816 | Logo and icon only: wordmark and one-colour versions, Black Umber. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Cotton Cardigan at primary-400, Buffed Copper at accent-400. Identical in both themes.

| Step | Primary (Cotton Cardigan) | Primary roles | Accent (Buffed Copper) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F3F5F8 | light: primary-soft | #FAF4F1 | light: accent-soft | #FBF8F7 |
| 100 | #E1E6ED | light: selection; dark: link-hover | #F4E5DF | dark: chart-2 | #F4F1F0 |
| 200 | #C1CDDC | dark: primary-hover, link | #ECCDC0 | dark: chart-4 | #E5E2E1 |
| 300 | #9BAFC8 | dark: primary | #E2AF9A | dark: accent, chart-1 | #CECBCA |
| 400 | #7693B7 | brand anchor | #DA9071 | brand anchor; dark: chart-5 | #AAA7A7 |
| 500 | #5B799F |  | #BD704F | light: chart-4; dark: chart-3 | #878484 |
| 600 | #455F80 | light: primary | #975539 | light: accent, chart-1 | #686564 |
| 700 | #374B63 | light: primary-hover, link | #75432E | light: chart-3 | #494646 |
| 800 | #283647 | light: link-hover; dark: primary-soft, selection | #533021 | light: chart-2 | #322F2F |
| 900 | #1B242F |  | #361F16 | light: chart-5; dark: accent-soft | #1D1B1B |
| 950 | #10151B |  | #1D110C |  | #131111 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #1E1816 on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #686564 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #455F80: **6.6:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #975539: **5.7:1**, AA.
- Link on page (light): `link` #374B63 on `bg` #FAFAFA: **8.6:1**, AAA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #1E1816 on `primary` #9BAFC8: **7.8:1**, AAA.
- Dark muted on surface (dark): `text-muted` #AAA7A7 on `surface` #292321: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #E2AF9A on `bg` #1E1816: **9.0:1**, AAA.
- Dark success on surface (dark): `success` #21AA69 on `surface` #292321: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E7727B on `surface` #292321: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #EBA726 on `surface` #292321: **7.4:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Cotton Cardigan and Buffed Copper only. Sunlit Clay and Black Umber are for the logo and icon, never for charts or UI.
- Charts use five shades of Buffed Copper, plus Cotton Cardigan as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Cotton Cardigan itself sits at primary-400; light-mode UI uses primary-600 so labels and text pass 4.5:1. Use the exact Cotton Cardigan in the logo and large graphics.
- Buffed Copper itself sits at accent-400; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Buffed Copper in the logo and large graphics.
- Sunlit Clay reaches 3:1 only on Black Umber; keep it off Cotton Cardigan and Buffed Copper grounds.
- Warning hue moved 9° toward yellow (OKLCH 65° to 74°) to stay apart from the brand hues.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
