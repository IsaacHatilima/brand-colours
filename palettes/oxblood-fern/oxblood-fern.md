# Oxblood and Fern

![Oxblood and Fern colour system sheet](oxblood-fern.png)

- Character: heritage, assured, botanical
- Suggested uses: wine merchants, apothecaries, heritage hotels, members' clubs
- Source: Rebuilt from the v1 palette Berry and Mint.
- Files: [CSS tokens](oxblood-fern.css) · [JSON tokens](oxblood-fern.tokens.json) · [Colour sheet](oxblood-fern.png)

Brand colours: Red Oxide #611B21 (primary), Holly Fern #89B199 (accent). Charts: Holly Fern shades plus Red Oxide. Logo and icon only: Jasmine #FED67D (spark), Kala Black #211718 (ink).

## Brand colours

- Brand 1 · primary: [Red Oxide](../../colors/red-oxide.md) (#611B21, RGB 97, 27, 33), the primary scale's anchor at step 800. Light UI uses primary-800 (#611B21); dark UI uses primary-300 (#E89B9B).
- Brand 2 · accent: [Holly Fern](../../colors/holly-fern.md) (#89B199, RGB 137, 177, 153), the accent scale's anchor at step 300. Light UI uses accent-600 (#33684C); dark UI uses accent-300 (#89B199).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #686565 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Jasmine and Kala Black never appear as UI colours.

- Spark: [Jasmine](../../colors/jasmine.md) (#FED67D). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Kala Black](../../colors/kala-black.md) (#211718). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Kala Black | Red Oxide | Holly Fern |
|---|---|---|---|---|
| Red Oxide | ✓ 11.9 | ✗ 1.4 | same | ✓ 5.2 |
| Holly Fern | ✗ 2.3 | ✓ 7.3 | ✓ 5.2 | same |
| Jasmine | ✗ 1.3 | ✓ 12.6 | ✓ 9.0 | ✗ 1.7 |
| Kala Black | ✓ 16.8 | same | ✗ 1.4 | ✓ 7.3 |
| Paper | same | ✓ 16.8 | ✓ 11.9 | ✗ 2.3 |

- On Paper: Red Oxide, Kala Black.
- On Kala Black: Holly Fern, Jasmine, Paper.
- On Red Oxide: Holly Fern, Jasmine, Paper.
- On Holly Fern: Red Oxide, Kala Black.

## Pairing rationale

The darker half of Berry and Mint: deep oxblood leads, and sage softens it as the single secondary hue. Warm jasmine keeps the logo glowing on the red-black ink.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #211718 | Page background: a plain off-white in light, the Kala Black ink in dark. Text on it uses `text` (16.8:1) and `text-muted` (5.5:1 light, 7.3:1 dark). |
| surface | #FFFFFF | #2A2323 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #352D2E | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F4F1F1 | #251D1E | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E5E2E2 | #403838 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #878485 | #7F7677 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.5:1 dark on surface). |
| text | #211718 | #FAFAFA | Primary text and icons on every surface. Kala Black in light; the paper off-white in dark. |
| text-muted | #686565 | #AAA7A8 | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #611B21 | #E89B9B | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Red Oxide (primary-800 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #3B1819 | #F1C1C0 | Hover and pressed fill of `primary`. |
| primary-soft | #FCF2F2 | #611B21 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #211718 | Text and icons on `primary` and `primary-hover` (12.4:1 light, 8.0:1 dark). Dark mode uses ink, not white. |
| link | #611B21 | #F1C1C0 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #3B1819 | #F7E1E0 | Hover state of `link`. |
| accent | #33684C | #89B199 | The single secondary hue, Holly Fern: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #F2F6F4 | #16281E | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #211718 | Text and icons on `accent` (6.5:1 light, 7.3:1 dark). |
| focus | #33684C | #89B199 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.2:1 on `bg` in light, 7.3:1 in dark. It uses the accent so it never blends into Red Oxide controls. |
| selection | #F7E1E0 | #611B21 | Text selection background. Text keeps `text`. |
| disabled-bg | #F4F1F1 | #352D2E | Fill of disabled buttons and inputs. |
| disabled-text | #878485 | #686565 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #3F7532 | #5EA749 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.5:1 light, 5.2:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E7F2E7 | #172918 | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #211718 | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.3:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #211718 | Text on solid `warning` fills. |
| danger | #B33C00 | #E57855 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.2:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E3 | #2E170F | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #211718 | Text on solid `danger` fills. |
| info | #611B21 | #F1C1C0 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #FCF2F2 | #611B21 | Background of info banners. Text on it uses `info`. |
| chart-1 | #33684C | #89B199 | Chart series 1, the anchor shade of Holly Fern. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #203B2C | #DDE7E1 | Chart series 2, a darker Holly Fern in light and a lighter Holly Fern in dark. |
| chart-3 | #649C7C | #468462 | Chart series 3, a lighter Holly Fern in light and a deeper Holly Fern in dark. |
| chart-4 | #2A523C | #B8CEC0 | Chart series 4, a mid shade of Holly Fern. |
| chart-5 | #468462 | #649C7C | Chart series 5, the remaining Holly Fern shade that still holds 3:1. |
| chart-alt | #611B21 | #E89B9B | The one contrasting chart series: Red Oxide, the primary brand colour. Chart colours are only Holly Fern shades and Red Oxide, never status or logo colours. |
| chart-grid | #E5E2E2 | #403838 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #211718 | #211718 | Raw near-black, Kala Black: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #FED67D | #FED67D | Logo and icon only: Jasmine, the highlight or signal dot. Never a UI colour. |
| logo-ink | #211718 | #211718 | Logo and icon only: wordmark and one-colour versions, Kala Black. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Red Oxide at primary-800, Holly Fern at accent-300. Identical in both themes.

| Step | Primary (Red Oxide) | Primary roles | Accent (Holly Fern) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #FCF2F2 | light: primary-soft | #F2F6F4 | light: accent-soft | #FBF8F8 |
| 100 | #F7E1E0 | light: selection; dark: link-hover | #DDE7E1 | dark: chart-2 | #F4F1F1 |
| 200 | #F1C1C0 | dark: primary-hover, link | #B8CEC0 | dark: chart-4 | #E5E2E2 |
| 300 | #E89B9B | dark: primary | #89B199 | brand anchor; dark: accent, chart-1 | #CECBCB |
| 400 | #E17175 |  | #649C7C | light: chart-3; dark: chart-5 | #AAA7A8 |
| 500 | #C75157 |  | #468462 | light: chart-5; dark: chart-3 | #878485 |
| 600 | #A03B42 |  | #33684C | light: accent, chart-1 | #686565 |
| 700 | #7C3035 |  | #2A523C | light: chart-4 | #494647 |
| 800 | #611B21 | brand anchor; light: primary, link; dark: primary-soft, selection | #203B2C | light: chart-2 | #322F2F |
| 900 | #3B1819 | light: primary-hover, link-hover | #16281E | dark: accent-soft | #1E1B1B |
| 950 | #210E0E |  | #0E1711 |  | #141112 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #211718 on `bg` #FAFAFA: **16.8:1**, AAA.
- Muted on page (light): `text-muted` #686565 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #611B21: **12.4:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #33684C: **6.5:1**, AA.
- Link on page (light): `link` #611B21 on `bg` #FAFAFA: **11.9:1**, AAA.
- Danger on soft (light): `danger` #B33C00 on `danger-soft` #FBE9E3: **5.0:1**, AA.
- Dark primary button (dark): `on-primary` #211718 on `primary` #E89B9B: **8.0:1**, AAA.
- Dark muted on surface (dark): `text-muted` #AAA7A8 on `surface` #2A2323: **6.5:1**, AA.
- Dark accent on page (dark): `accent` #89B199 on `bg` #211718: **7.3:1**, AAA.
- Dark success on surface (dark): `success` #5EA749 on `surface` #2A2323: **5.2:1**, AA.
- Dark danger on surface (dark): `danger` #E57855 on `surface` #2A2323: **5.2:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #2A2323: **7.3:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Red Oxide and Holly Fern only. Jasmine and Kala Black are for the logo and icon, never for charts or UI.
- Charts use five shades of Holly Fern, plus Red Oxide as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Holly Fern itself sits at accent-300; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Holly Fern in the logo and large graphics.
- Success hue moved 17° toward yellow-green (OKLCH 157° to 140°) to stay apart from the brand hues.
- Danger hue moved 8° toward orange-red (OKLCH 32° to 40°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
