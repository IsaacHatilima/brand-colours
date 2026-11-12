# Tidal Signal

![Tidal Signal colour system sheet](tidal-signal.png)

- Character: confident, maritime, lively
- Suggested uses: coastal tourism, watersports, transport brands
- Source: Rebuilt from the v1 palette Tidal Signal.
- Files: [CSS tokens](tidal-signal.css) · [JSON tokens](tidal-signal.tokens.json) · [Colour sheet](tidal-signal.png)

Brand colours: Pristine Seas #047898 (primary), Tangerine Dream #F3946B (accent). Charts: Tangerine Dream shades plus Pristine Seas. Logo and icon only: Bright Gold #F4D80E (spark), Black Feather #101C21 (ink).

## Brand colours

- Brand 1 · primary: [Pristine Seas](../../colors/pristine-seas.md) (#047898, RGB 4, 120, 152), the primary scale's anchor at step 600. Light UI uses primary-600 (#047898); dark UI uses primary-300 (#87C2D9).
- Brand 2 · accent: [Tangerine Dream](../../colors/tangerine-dream.md) (#F3946B, RGB 243, 148, 107), the accent scale's anchor at step 300. Light UI uses accent-600 (#9F3D00); dark UI uses accent-300 (#F3946B).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #646668 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Bright Gold and Black Feather never appear as UI colours.

- Spark: [Bright Gold](../../colors/bright-gold.md) (#F4D80E). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Black Feather](../../colors/black-feather-101c21.md) (#101C21). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Black Feather | Pristine Seas | Tangerine Dream |
|---|---|---|---|---|
| Pristine Seas | ✓ 4.9 | ✓ 3.4 | same | ✗ 2.2 |
| Tangerine Dream | ✗ 2.2 | ✓ 7.7 | ✗ 2.2 | same |
| Bright Gold | ✗ 1.4 | ✓ 12.1 | ✓ 3.5 | ✗ 1.6 |
| Black Feather | ✓ 16.6 | same | ✓ 3.4 | ✓ 7.7 |
| Paper | same | ✓ 16.6 | ✓ 4.9 | ✗ 2.2 |

- On Paper: Pristine Seas, Black Feather.
- On Black Feather: Pristine Seas, Tangerine Dream, Bright Gold, Paper.
- On Pristine Seas: Bright Gold, Black Feather, Paper.
- On Tangerine Dream: Black Feather.

## Pairing rationale

Sea teal and signal-flag coral are complementary, so the accent never blends into teal controls. Bright gold is the buoy light in the mark.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #101C21 | Page background: a plain off-white in light, the Black Feather ink in dark. Text on it uses `text` (16.6:1) and `text-muted` (5.5:1 light, 7.3:1 dark). |
| surface | #FFFFFF | #1F2629 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #293134 | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F0F3F4 | #192124 | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E1E4E5 | #343C3F | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #838687 | #727A7E | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #101C21 | #FAFAFA | Primary text and icons on every surface. Black Feather in light; the paper off-white in dark. |
| text-muted | #646668 | #A6A9AA | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #047898 | #87C2D9 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Pristine Seas (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #115D75 | #B6D8E6 | Hover and pressed fill of `primary`. |
| primary-soft | #F0F6F9 | #104252 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #101C21 | Text and icons on `primary` and `primary-hover` (5.1:1 light, 8.9:1 dark). Dark mode uses ink, not white. |
| link | #115D75 | #B6D8E6 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #104252 | #DCEBF1 | Hover state of `link`. |
| accent | #9F3D00 | #F3946B | The single secondary hue, Tangerine Dream: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FEF2EE | #3E1604 | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #101C21 | Text and icons on `accent` (6.7:1 light, 7.7:1 dark). |
| focus | #9F3D00 | #F3946B | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.4:1 on `bg` in light, 7.7:1 in dark. It uses the accent so it never blends into Pristine Seas controls. |
| selection | #DCEBF1 | #104252 | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F3F4 | #293134 | Fill of disabled buttons and inputs. |
| disabled-text | #838687 | #646668 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #24AC6A | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.3:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #101C21 | Text on solid `success` fills. |
| warning | #8A5B00 | #EBA726 | Warning text, icons and fills (5.9:1 light, 7.4:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F8F0D9 | #29200A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #101C21 | Text on solid `warning` fills. |
| danger | #B82E42 | #E8737D | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.3:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #101C21 | Text on solid `danger` fills. |
| info | #115D75 | #B6D8E6 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F0F6F9 | #104252 | Background of info banners. Text on it uses `info`. |
| chart-1 | #9F3D00 | #F3946B | Chart series 1, the anchor shade of Tangerine Dream. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #5D2100 | #FAE0D6 | Chart series 2, a darker Tangerine Dream in light and a lighter Tangerine Dream in dark. |
| chart-3 | #EB6A29 | #C95000 | Chart series 3, a lighter Tangerine Dream in light and a deeper Tangerine Dream in dark. |
| chart-4 | #7F2F00 | #F5BFA9 | Chart series 4, a mid shade of Tangerine Dream. |
| chart-5 | #C95000 | #EB6A29 | Chart series 5, the remaining Tangerine Dream shade that still holds 3:1. |
| chart-alt | #047898 | #87C2D9 | The one contrasting chart series: Pristine Seas, the primary brand colour. Chart colours are only Tangerine Dream shades and Pristine Seas, never status or logo colours. |
| chart-grid | #E1E4E5 | #343C3F | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #101C21 | #101C21 | Raw near-black, Black Feather: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #F4D80E | #F4D80E | Logo and icon only: Bright Gold, the highlight or signal dot. Never a UI colour. |
| logo-ink | #101C21 | #101C21 | Logo and icon only: wordmark and one-colour versions, Black Feather. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Pristine Seas at primary-600, Tangerine Dream at accent-300. Identical in both themes.

| Step | Primary (Pristine Seas) | Primary roles | Accent (Tangerine Dream) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F0F6F9 | light: primary-soft | #FEF2EE | light: accent-soft | #F7FAFB |
| 100 | #DCEBF1 | light: selection; dark: link-hover | #FAE0D6 | dark: chart-2 | #F0F3F4 |
| 200 | #B6D8E6 | dark: primary-hover, link | #F5BFA9 | dark: chart-4 | #E1E4E5 |
| 300 | #87C2D9 | dark: primary | #F3946B | brand anchor; dark: accent, chart-1 | #CACDCE |
| 400 | #4BACCF |  | #EB6A29 | light: chart-3; dark: chart-5 | #A6A9AA |
| 500 | #1893B9 |  | #C95000 | light: chart-5; dark: chart-3 | #838687 |
| 600 | #047898 | brand anchor; light: primary | #9F3D00 | light: accent, chart-1 | #646668 |
| 700 | #115D75 | light: primary-hover, link | #7F2F00 | light: chart-4 | #454749 |
| 800 | #104252 | light: link-hover; dark: primary-soft, selection | #5D2100 | light: chart-2 | #2E3031 |
| 900 | #0C2A35 |  | #3E1604 | dark: accent-soft | #1A1C1D |
| 950 | #07171D |  | #230E05 |  | #101213 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #101C21 on `bg` #FAFAFA: **16.6:1**, AAA.
- Muted on page (light): `text-muted` #646668 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #047898: **5.1:1**, AA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #9F3D00: **6.7:1**, AA.
- Link on page (light): `link` #115D75 on `bg` #FAFAFA: **7.1:1**, AAA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #101C21 on `primary` #87C2D9: **8.9:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A6A9AA on `surface` #1F2629: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #F3946B on `bg` #101C21: **7.7:1**, AAA.
- Dark success on surface (dark): `success` #24AC6A on `surface` #1F2629: **5.3:1**, AA.
- Dark danger on surface (dark): `danger` #E8737D on `surface` #1F2629: **5.3:1**, AA.
- Dark warning on surface (dark): `warning` #EBA726 on `surface` #1F2629: **7.4:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Pristine Seas and Tangerine Dream only. Bright Gold and Black Feather are for the logo and icon, never for charts or UI.
- Charts use five shades of Tangerine Dream, plus Pristine Seas as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Tangerine Dream itself sits at accent-300; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Tangerine Dream in the logo and large graphics.
- Warning hue moved 9° toward yellow (OKLCH 65° to 74°) to stay apart from the brand hues.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
