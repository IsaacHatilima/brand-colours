# Sunwashed Stone

![Sunwashed Stone colour system sheet](sunwashed-stone.png)

- Character: warm, minimal, tactile
- Suggested uses: interiors, handmade goods, slow-living brands
- Source: Rebuilt from the v1 palette Sunwashed Stone.
- Files: [CSS tokens](sunwashed-stone.css) · [JSON tokens](sunwashed-stone.tokens.json) · [Colour sheet](sunwashed-stone.png)

Brand colours: Tibetan Orange #AE5846 (primary), Tubbataha Teal #0A8383 (accent). Charts: Tubbataha Teal shades plus Tibetan Orange. Logo and icon only: Sunlit Clay #F7BB67 (spark), Black Umber #1E1816 (ink).

## Brand colours

- Brand 1 · primary: [Tibetan Orange](../../colors/tibetan-orange.md) (#AE5846, RGB 174, 88, 70), the primary scale's anchor at step 500. Light UI uses primary-500 (#AE5846); dark UI uses primary-300 (#D79E91).
- Brand 2 · accent: [Tubbataha Teal](../../colors/tubbataha-teal.md) (#0A8383, RGB 10, 131, 131), the accent scale's anchor at step 500. Light UI uses accent-600 (#006868); dark UI uses accent-300 (#82B8B7).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #686564 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Sunlit Clay and Black Umber never appear as UI colours.

- Spark: [Sunlit Clay](../../colors/sunlit-clay.md) (#F7BB67). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Black Umber](../../colors/black-umber.md) (#1E1816). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Black Umber | Tibetan Orange | Tubbataha Teal |
|---|---|---|---|---|
| Tibetan Orange | ✓ 4.7 | ✓ 3.6 | same | ✗ 1.1 |
| Tubbataha Teal | ✓ 4.4 | ✓ 3.8 | ✗ 1.1 | same |
| Sunlit Clay | ✗ 1.6 | ✓ 10.2 | ✗ 2.9 | ✗ 2.7 |
| Black Umber | ✓ 16.8 | same | ✓ 3.6 | ✓ 3.8 |
| Paper | same | ✓ 16.8 | ✓ 4.7 | ✓ 4.4 |

- On Paper: Tibetan Orange, Tubbataha Teal, Black Umber.
- On Black Umber: Tibetan Orange, Tubbataha Teal, Sunlit Clay, Paper.
- On Tibetan Orange: Black Umber, Paper.
- On Tubbataha Teal: Black Umber, Paper.

## Pairing rationale

Weathered terracotta leads on plain stone-grey surfaces. A deep library teal is the complementary accent, and sunlit clay warms the mark.

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
| primary | #AE5846 | #D79E91 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Tibetan Orange (primary-500 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #8C4334 | #E6C3BB | Hover and pressed fill of `primary`. |
| primary-soft | #FAF3F2 | #4F281F | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #1E1816 | Text and icons on `primary` and `primary-hover` (4.9:1 light, 7.7:1 dark). Dark mode uses ink, not white. |
| link | #8C4334 | #E6C3BB | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #6D362A | #F2E2DE | Hover state of `link`. |
| accent | #006868 | #82B8B7 | The single secondary hue, Tubbataha Teal: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F0F7F6 | #0C2828 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #1E1816 | Text and icons on `accent` (6.6:1 light, 7.9:1 dark). |
| focus | #006868 | #82B8B7 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.3:1 on `bg` in light, 7.9:1 in dark. It uses the accent so it never blends into Tibetan Orange controls. |
| selection | #F2E2DE | #4F281F | Text selection background. Text keeps `text`. |
| disabled-bg | #F4F1F0 | #342D2B | Fill of disabled buttons and inputs. |
| disabled-text | #878484 | #686564 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #21AA69 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #1E1816 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.4:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #1E1816 | Text on solid `warning` fills. |
| danger | #B82E42 | #E7727B | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #1E1816 | Text on solid `danger` fills. |
| info | #8C4334 | #E6C3BB | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #FAF3F2 | #4F281F | Background of info banners. Text on it uses `info`. |
| chart-1 | #006868 | #82B8B7 | Chart series 1, the anchor shade of Tubbataha Teal. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #0D3B3B | #DBE9E9 | Chart series 2, a darker Tubbataha Teal in light and a lighter Tubbataha Teal in dark. |
| chart-3 | #46A0A0 | #0A8383 | Chart series 3, a lighter Tubbataha Teal in light and a deeper Tubbataha Teal in dark. |
| chart-4 | #095252 | #B3D2D2 | Chart series 4, a mid shade of Tubbataha Teal. |
| chart-5 | #0A8383 | #46A0A0 | Chart series 5, the remaining Tubbataha Teal shade that still holds 3:1. |
| chart-alt | #AE5846 | #D79E91 | The one contrasting chart series: Tibetan Orange, the primary brand colour. Chart colours are only Tubbataha Teal shades and Tibetan Orange, never status or logo colours. |
| chart-grid | #E5E2E1 | #3F3836 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #1E1816 | #1E1816 | Raw near-black, Black Umber: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F7BB67 | #F7BB67 | Logo and icon only: Sunlit Clay, the highlight or signal dot. Never a UI colour. |
| logo-ink | #1E1816 | #1E1816 | Logo and icon only: wordmark and one-colour versions, Black Umber. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Tibetan Orange at primary-500, Tubbataha Teal at accent-500. Identical in both themes.

| Step | Primary (Tibetan Orange) | Primary roles | Accent (Tubbataha Teal) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #FAF3F2 | light: primary-soft | #F0F7F6 | light: accent-soft | #FBF8F7 |
| 100 | #F2E2DE | light: selection; dark: link-hover | #DBE9E9 | dark: chart-2 | #F4F1F0 |
| 200 | #E6C3BB | dark: primary-hover, link | #B3D2D2 | dark: chart-4 | #E5E2E1 |
| 300 | #D79E91 | dark: primary | #82B8B7 | dark: accent, chart-1 | #CECBCA |
| 400 | #CA7866 |  | #46A0A0 | light: chart-3; dark: chart-5 | #AAA7A7 |
| 500 | #AE5846 | brand anchor; light: primary | #0A8383 | brand anchor; light: chart-5; dark: chart-3 | #878484 |
| 600 | #8C4334 | light: primary-hover, link | #006868 | light: accent, chart-1 | #686564 |
| 700 | #6D362A | light: link-hover | #095252 | light: chart-4 | #494646 |
| 800 | #4F281F | dark: primary-soft, selection | #0D3B3B | light: chart-2 | #322F2F |
| 900 | #351B16 |  | #0C2828 | dark: accent-soft | #1D1B1B |
| 950 | #1E100D |  | #091717 |  | #131111 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #1E1816 on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #686564 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #AE5846: **4.9:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #006868: **6.6:1**, AA.
- Link on page (light): `link` #8C4334 on `bg` #FAFAFA: **6.8:1**, AA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #1E1816 on `primary` #D79E91: **7.7:1**, AAA.
- Dark muted on surface (dark): `text-muted` #AAA7A7 on `surface` #292321: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #82B8B7 on `bg` #1E1816: **7.9:1**, AAA.
- Dark success on surface (dark): `success` #21AA69 on `surface` #292321: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E7727B on `surface` #292321: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #292321: **7.4:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Tibetan Orange and Tubbataha Teal only. Sunlit Clay and Black Umber are for the logo and icon, never for charts or UI.
- Charts use five shades of Tubbataha Teal, plus Tibetan Orange as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Tubbataha Teal itself sits at accent-500; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Tubbataha Teal in the logo and large graphics.
- Sunlit Clay reaches 3:1 only on Black Umber; keep it off Tibetan Orange and Tubbataha Teal grounds.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
