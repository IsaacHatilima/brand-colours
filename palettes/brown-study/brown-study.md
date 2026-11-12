# Brown Study

![Brown Study colour system sheet](brown-study.png)

- Character: studious, warm, trustworthy
- Suggested uses: independent bookshops, coffee roasters, leather goods, editorial publishing
- Source: Rebuilt from the v1 palette Desert Sky.
- Files: [CSS tokens](brown-study.css) · [JSON tokens](brown-study.tokens.json) · [Colour sheet](brown-study.png)

Brand colours: Brown Study #4B2510 (primary), Cotton Cardigan #7693B7 (accent). Charts: Cotton Cardigan shades plus Brown Study. Logo and icon only: Bright Gold #F4D80E (spark), Black Umber #1E1816 (ink).

## Brand colours

- Brand 1 · primary: [Brown Study](../../colors/brown-study.md) (#4B2510, RGB 75, 37, 16), the primary scale's anchor at step 800. Light UI uses primary-800 (#4B2510); dark UI uses primary-300 (#D1A590).
- Brand 2 · accent: [Cotton Cardigan](../../colors/cotton-cardigan.md) (#7693B7, RGB 118, 147, 183), the accent scale's anchor at step 400. Light UI uses accent-600 (#455F80); dark UI uses accent-300 (#9BAFC8).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #686564 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Bright Gold and Black Umber never appear as UI colours.

- Spark: [Bright Gold](../../colors/bright-gold.md) (#F4D80E). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Black Umber](../../colors/black-umber.md) (#1E1816). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Black Umber | Brown Study | Cotton Cardigan |
|---|---|---|---|---|
| Brown Study | ✓ 12.8 | ✗ 1.3 | same | ✓ 4.2 |
| Cotton Cardigan | ✓ 3.0 | ✓ 5.5 | ✓ 4.2 | same |
| Bright Gold | ✗ 1.4 | ✓ 12.3 | ✓ 9.3 | ✗ 2.2 |
| Black Umber | ✓ 16.8 | same | ✗ 1.3 | ✓ 5.5 |
| Paper | same | ✓ 16.8 | ✓ 12.8 | ✓ 3.0 |

- On Paper: Brown Study, Cotton Cardigan, Black Umber.
- On Black Umber: Cotton Cardigan, Bright Gold, Paper.
- On Brown Study: Cotton Cardigan, Bright Gold, Paper.
- On Cotton Cardigan: Brown Study, Black Umber, Paper.

## Pairing rationale

Desert Sky's deep brown leads and its blue becomes the cool accent, giving a library-and-leather feel. Bright gold is the signal light in the mark.

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
| primary | #4B2510 | #D1A590 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Brown Study (primary-800 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #2F1C12 | #E2C7BA | Hover and pressed fill of `primary`. |
| primary-soft | #F9F4F1 | #4B2510 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #1E1816 | Text and icons on `primary` and `primary-hover` (13.4:1 light, 7.9:1 dark). Dark mode uses ink, not white. |
| link | #4B2510 | #E2C7BA | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #2F1C12 | #F0E3DD | Hover state of `link`. |
| accent | #455F80 | #9BAFC8 | The single secondary hue, Cotton Cardigan: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F3F5F8 | #1B242F | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #1E1816 | Text and icons on `accent` (6.6:1 light, 7.8:1 dark). |
| focus | #455F80 | #9BAFC8 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.3:1 on `bg` in light, 7.8:1 in dark. It uses the accent so it never blends into Brown Study controls. |
| selection | #F0E3DD | #4B2510 | Text selection background. Text keeps `text`. |
| disabled-bg | #F4F1F0 | #342D2B | Fill of disabled buttons and inputs. |
| disabled-text | #878484 | #686564 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #21AA69 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #1E1816 | Text on solid `success` fills. |
| warning | #875D00 | #E6AA22 | Warning text, icons and fills (5.8:1 light, 7.5:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F7F1D9 | #28210A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #1E1816 | Text on solid `warning` fills. |
| danger | #B82E42 | #E7727B | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #1E1816 | Text on solid `danger` fills. |
| info | #4B2510 | #E2C7BA | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F9F4F1 | #4B2510 | Background of info banners. Text on it uses `info`. |
| chart-1 | #455F80 | #9BAFC8 | Chart series 1, the anchor shade of Cotton Cardigan. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #283647 | #E1E6ED | Chart series 2, a darker Cotton Cardigan in light and a lighter Cotton Cardigan in dark. |
| chart-3 | #7693B7 | #5B799F | Chart series 3, a lighter Cotton Cardigan in light and a deeper Cotton Cardigan in dark. |
| chart-4 | #374B63 | #C1CDDC | Chart series 4, a mid shade of Cotton Cardigan. |
| chart-5 | #5B799F | #7693B7 | Chart series 5, the remaining Cotton Cardigan shade that still holds 3:1. |
| chart-alt | #4B2510 | #D1A590 | The one contrasting chart series: Brown Study, the primary brand colour. Chart colours are only Cotton Cardigan shades and Brown Study, never status or logo colours. |
| chart-grid | #E5E2E1 | #3F3836 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #1E1816 | #1E1816 | Raw near-black, Black Umber: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F4D80E | #F4D80E | Logo and icon only: Bright Gold, the highlight or signal dot. Never a UI colour. |
| logo-ink | #1E1816 | #1E1816 | Logo and icon only: wordmark and one-colour versions, Black Umber. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Brown Study at primary-800, Cotton Cardigan at accent-400. Identical in both themes.

| Step | Primary (Brown Study) | Primary roles | Accent (Cotton Cardigan) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F9F4F1 | light: primary-soft | #F3F5F8 | light: accent-soft | #FBF8F7 |
| 100 | #F0E3DD | light: selection; dark: link-hover | #E1E6ED | dark: chart-2 | #F4F1F0 |
| 200 | #E2C7BA | dark: primary-hover, link | #C1CDDC | dark: chart-4 | #E5E2E1 |
| 300 | #D1A590 | dark: primary | #9BAFC8 | dark: accent, chart-1 | #CECBCA |
| 400 | #C38363 |  | #7693B7 | brand anchor; light: chart-3; dark: chart-5 | #AAA7A7 |
| 500 | #A86543 |  | #5B799F | light: chart-5; dark: chart-3 | #878484 |
| 600 | #844C2E |  | #455F80 | light: accent, chart-1 | #686564 |
| 700 | #653B24 |  | #374B63 | light: chart-4 | #494646 |
| 800 | #4B2510 | brand anchor; light: primary, link; dark: primary-soft, selection | #283647 | light: chart-2 | #322F2F |
| 900 | #2F1C12 | light: primary-hover, link-hover | #1B242F | dark: accent-soft | #1D1B1B |
| 950 | #1C120C |  | #10151B |  | #131111 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #1E1816 on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #686564 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #4B2510: **13.4:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #455F80: **6.6:1**, AA.
- Link on page (light): `link` #4B2510 on `bg` #FAFAFA: **12.8:1**, AAA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #1E1816 on `primary` #D1A590: **7.9:1**, AAA.
- Dark muted on surface (dark): `text-muted` #AAA7A7 on `surface` #292321: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #9BAFC8 on `bg` #1E1816: **7.8:1**, AAA.
- Dark success on surface (dark): `success` #21AA69 on `surface` #292321: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E7727B on `surface` #292321: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #E6AA22 on `surface` #292321: **7.5:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Brown Study and Cotton Cardigan only. Bright Gold and Black Umber are for the logo and icon, never for charts or UI.
- Charts use five shades of Cotton Cardigan, plus Brown Study as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Cotton Cardigan itself sits at accent-400; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Cotton Cardigan in the logo and large graphics.
- Warning hue moved 13° toward yellow (OKLCH 65° to 78°) to stay apart from the brand hues.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
