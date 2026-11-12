# Lavender Atelier

![Lavender Atelier colour system sheet](lavender-atelier.png)

- Character: gentle, imaginative, refined
- Suggested uses: beauty studios, independent publishing, creative services
- Source: Rebuilt from the v1 palette Lavender Atelier.
- Files: [CSS tokens](lavender-atelier.css) · [JSON tokens](lavender-atelier.tokens.json) · [Colour sheet](lavender-atelier.png)

Brand colours: Sumptuous Purple #624D85 (primary), Ciao #DF9A7D (accent). Charts: Ciao shades plus Sumptuous Purple. Logo and icon only: Jasmine #FED67D (spark), Absence Of Light #14131A (ink).

## Brand colours

- Brand 1 · primary: [Sumptuous Purple](../../colors/sumptuous-purple.md) (#624D85, RGB 98, 77, 133), the primary scale's anchor at step 600. Light UI uses primary-600 (#624D85); dark UI uses primary-300 (#B5A6D1).
- Brand 2 · accent: [Ciao](../../colors/ciao.md) (#DF9A7D, RGB 223, 154, 125), the accent scale's anchor at step 300. Light UI uses accent-600 (#96431A); dark UI uses accent-300 (#DF9A7D).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #666668 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Jasmine and Absence Of Light never appear as UI colours.

- Spark: [Jasmine](../../colors/jasmine.md) (#FED67D). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Absence Of Light](../../colors/absence-of-light.md) (#14131A). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Absence Of Light | Sumptuous Purple | Ciao |
|---|---|---|---|---|
| Sumptuous Purple | ✓ 6.9 | ✗ 2.6 | same | ✓ 3.1 |
| Ciao | ✗ 2.2 | ✓ 8.0 | ✓ 3.1 | same |
| Jasmine | ✗ 1.3 | ✓ 13.3 | ✓ 5.2 | ✗ 1.7 |
| Absence Of Light | ✓ 17.7 | same | ✗ 2.6 | ✓ 8.0 |
| Paper | same | ✓ 17.7 | ✓ 6.9 | ✗ 2.2 |

- On Paper: Sumptuous Purple, Absence Of Light.
- On Absence Of Light: Ciao, Jasmine, Paper.
- On Sumptuous Purple: Ciao, Jasmine, Paper.
- On Ciao: Sumptuous Purple, Absence Of Light.

## Pairing rationale

Sumptuous purple keeps the atelier mood. The v1 sage was too grey to work as an accent and berry tones blurred into the purple, so a soft apricot from the library becomes the accent; in light mode it deepens to a burnt clay. Jasmine lifts the mark.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #14131A | Page background: a plain off-white in light, the Absence Of Light ink in dark. Text on it uses `text` (17.7:1) and `text-muted` (5.5:1 light, 7.8:1 dark). |
| surface | #FFFFFF | #1E1E24 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #29282F | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F2F2F4 | #19181E | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E3E3E5 | #333239 | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #858587 | #717178 | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.4:1 dark on surface). |
| text | #14131A | #FAFAFA | Primary text and icons on every surface. Absence Of Light in light; the paper off-white in dark. |
| text-muted | #666668 | #A8A8AA | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #624D85 | #B5A6D1 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Sumptuous Purple (primary-600 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #4D3D68 | #D0C7E2 | Hover and pressed fill of `primary`. |
| primary-soft | #F6F4F9 | #382D4B | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #14131A | Text and icons on `primary` and `primary-hover` (7.2:1 light, 8.2:1 dark). Dark mode uses ink, not white. |
| link | #624D85 | #D0C7E2 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #4D3D68 | #E7E4F0 | Hover state of `link`. |
| accent | #96431A | #DF9A7D | The single secondary hue, Ciao: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FBF3F0 | #371B0F | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #14131A | Text and icons on `accent` (6.7:1 light, 8.0:1 dark). |
| focus | #96431A | #DF9A7D | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.5:1 on `bg` in light, 8.0:1 in dark. It uses the accent so it never blends into Sumptuous Purple controls. |
| selection | #E7E4F0 | #382D4B | Text selection background. Text keeps `text`. |
| disabled-bg | #F2F2F4 | #29282F | Fill of disabled buttons and inputs. |
| disabled-text | #858587 | #666668 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1BA766 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.3:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #14131A | Text on solid `success` fills. |
| warning | #8A5B00 | #EBA726 | Warning text, icons and fills (5.9:1 light, 8.0:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #F8F0D9 | #29200A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #14131A | Text on solid `warning` fills. |
| danger | #B82E42 | #E5707A | Errors and destructive actions: text, icons, fills (6.0:1 light, 5.5:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE8E8 | #2E1517 | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #14131A | Text on solid `danger` fills. |
| info | #624D85 | #D0C7E2 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F6F4F9 | #382D4B | Background of info banners. Text on it uses `info`. |
| chart-1 | #96431A | #DF9A7D | Chart series 1, the anchor shade of Ciao. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #542814 | #F4E1DA | Chart series 2, a darker Ciao in light and a lighter Ciao in dark. |
| chart-3 | #D3774F | #BB592B | Chart series 3, a lighter Ciao in light and a deeper Ciao in dark. |
| chart-4 | #753619 | #E9C2B2 | Chart series 4, a mid shade of Ciao. |
| chart-5 | #BB592B | #D3774F | Chart series 5, the remaining Ciao shade that still holds 3:1. |
| chart-alt | #624D85 | #B5A6D1 | The one contrasting chart series: Sumptuous Purple, the primary brand colour. Chart colours are only Ciao shades and Sumptuous Purple, never status or logo colours. |
| chart-grid | #E3E3E5 | #333239 | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #14131A | #14131A | Raw near-black, Absence Of Light: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #FED67D | #FED67D | Logo and icon only: Jasmine, the highlight or signal dot. Never a UI colour. |
| logo-ink | #14131A | #14131A | Logo and icon only: wordmark and one-colour versions, Absence Of Light. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Sumptuous Purple at primary-600, Ciao at accent-300. Identical in both themes.

| Step | Primary (Sumptuous Purple) | Primary roles | Accent (Ciao) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F6F4F9 | light: primary-soft | #FBF3F0 | light: accent-soft | #F9F9FB |
| 100 | #E7E4F0 | light: selection; dark: link-hover | #F4E1DA | dark: chart-2 | #F2F2F4 |
| 200 | #D0C7E2 | dark: primary-hover, link | #E9C2B2 | dark: chart-4 | #E3E3E5 |
| 300 | #B5A6D1 | dark: primary | #DF9A7D | brand anchor; dark: accent, chart-1 | #CCCCCE |
| 400 | #9C85C4 |  | #D3774F | light: chart-3; dark: chart-5 | #A8A8AA |
| 500 | #8067A9 |  | #BB592B | light: chart-5; dark: chart-3 | #858587 |
| 600 | #624D85 | brand anchor; light: primary, link | #96431A | light: accent, chart-1 | #666668 |
| 700 | #4D3D68 | light: primary-hover, link-hover | #753619 | light: chart-4 | #474749 |
| 800 | #382D4B | dark: primary-soft, selection | #542814 | light: chart-2 | #303032 |
| 900 | #251F32 |  | #371B0F | dark: accent-soft | #1C1C1D |
| 950 | #16121D |  | #201009 |  | #121213 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #14131A on `bg` #FAFAFA: **17.7:1**, AAA.
- Muted on page (light): `text-muted` #666668 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #624D85: **7.2:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #96431A: **6.7:1**, AA.
- Link on page (light): `link` #624D85 on `bg` #FAFAFA: **6.9:1**, AA.
- Danger on soft (light): `danger` #B82E42 on `danger-soft` #FBE8E8: **5.1:1**, AA.
- Dark primary button (dark): `on-primary` #14131A on `primary` #B5A6D1: **8.2:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A8A8AA on `surface` #1E1E24: **7.0:1**, AA.
- Dark accent on page (dark): `accent` #DF9A7D on `bg` #14131A: **8.0:1**, AAA.
- Dark success on surface (dark): `success` #1BA766 on `surface` #1E1E24: **5.3:1**, AA.
- Dark danger on surface (dark): `danger` #E5707A on `surface` #1E1E24: **5.5:1**, AA.
- Dark warning on surface (dark): `warning` #EBA726 on `surface` #1E1E24: **8.0:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Sumptuous Purple and Ciao only. Jasmine and Absence Of Light are for the logo and icon, never for charts or UI.
- Charts use five shades of Ciao, plus Sumptuous Purple as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
- One primary button per view, and one accent button at most.
- Never signal status by colour alone: icon and word every time.
- Control borders use `border-strong`; decorative ones use `border`.
- In dark mode the primary lightens to primary-300, links to primary-200, and button labels turn ink.
- Ciao itself sits at accent-300; light-mode UI uses accent-600 so labels and text pass 4.5:1. Use the exact Ciao in the logo and large graphics.
- Warning hue moved 9° toward yellow (OKLCH 65° to 74°) to stay apart from the brand hues.
- Danger hue moved 14° toward crimson (OKLCH 32° to 18°) to stay apart from the brand hues.

## Verification notes

- Anchors are the four library colours linked above. Every other value is generated: the 50–950 scales follow Harbour Signal's lightness curve and per-step chroma in OKLCH, the greys are plain neutrals tinted only by the ink's hue, and every value is gamut-mapped to sRGB. Refer to generated values by token, not by a library colour name.
- Contrast audit: 92 documented pairings across both themes, all passing (4.5:1 for text; 3:1 for control borders, focus rings, primary fills and chart series). WCAG 2.x relative luminance; pass/fail uses unrounded ratios.
- Hover, pressed and disabled states are defined, but components still need their own checks in context.
- Character and suggested uses are design judgments, not user-research findings.
