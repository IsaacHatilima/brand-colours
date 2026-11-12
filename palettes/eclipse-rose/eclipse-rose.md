# Eclipse Rose

![Eclipse Rose colour system sheet](eclipse-rose.png)

- Character: discreet, polished, warm
- Suggested uses: law firms, private clinics, boutique consultancies, wedding services
- Source: Rebuilt from the v1 palette Clear Horizon.
- Files: [CSS tokens](eclipse-rose.css) · [JSON tokens](eclipse-rose.tokens.json) · [Colour sheet](eclipse-rose.png)

Brand colours: Dark Eclipse #0A2943 (primary), Cherry Kisses #B16067 (accent). Charts: Cherry Kisses shades plus Dark Eclipse. Logo and icon only: Candid Blue #70C6E2 (spark), Black Is Back #11151A (ink).

## Brand colours

- Brand 1 · primary: [Dark Eclipse](../../colors/dark-eclipse.md) (#0A2943, RGB 10, 41, 67), the primary scale's anchor at step 900. Light UI uses primary-900 (#0A2943); dark UI uses primary-300 (#98B8D6).
- Brand 2 · accent: [Cherry Kisses](../../colors/cherry-kisses.md) (#B16067, RGB 177, 96, 103), the accent scale's anchor at step 500. Light UI uses accent-600 (#8E494F); dark UI uses accent-300 (#D8A2A5).

Supporting neutrals are plain greys, not brand colours: paper #FAFAFA for light pages, grey #656668 for muted text, and the ink for text and dark pages.

## Logo and icon colours

The two brand colours plus two that exist only for the logo and icon. Candid Blue and Black Is Back never appear as UI colours.

- Spark: [Candid Blue](../../colors/candid-blue.md) (#70C6E2). The signal light: a single dot, stroke or highlight in the mark.
- Ink: [Black Is Back](../../colors/black-is-back-11151a.md) (#11151A). Wordmark and one-colour versions.

### Which colours work on which ground (3:1 minimum for graphics)

| Mark | Paper | Black Is Back | Dark Eclipse | Cherry Kisses |
|---|---|---|---|---|
| Dark Eclipse | ✓ 14.3 | ✗ 1.2 | same | ✓ 3.4 |
| Cherry Kisses | ✓ 4.2 | ✓ 4.1 | ✓ 3.4 | same |
| Candid Blue | ✗ 1.9 | ✓ 9.5 | ✓ 7.7 | ✗ 2.3 |
| Black Is Back | ✓ 17.6 | same | ✗ 1.2 | ✓ 4.1 |
| Paper | same | ✓ 17.6 | ✓ 14.3 | ✓ 4.2 |

- On Paper: Dark Eclipse, Cherry Kisses, Black Is Back.
- On Black Is Back: Cherry Kisses, Candid Blue, Paper.
- On Dark Eclipse: Cherry Kisses, Candid Blue, Paper.
- On Cherry Kisses: Dark Eclipse, Black Is Back, Paper.

## Pairing rationale

Clear Horizon's deep navy becomes the lead, warmed by a dusty rose accent. A pale sky-blue spark gives the mark a crisp highlight on ink without adding another warm tone.

## Tokens

Light is the default; dark follows the system setting or `data-theme="dark"`. Use the semantic tokens in UI code, never raw scale steps.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | #FAFAFA | #11151A | Page background: a plain off-white in light, the Black Is Back ink in dark. Text on it uses `text` (17.6:1) and `text-muted` (5.5:1 light, 7.7:1 dark). |
| surface | #FFFFFF | #1B2025 | Cards, panels, table bodies and inputs, placed on `bg`. Text on it uses `text` and `text-muted`. |
| surface-raised | #FFFFFF | #262A2F | Menus, popovers, dialogs and toasts. Pair with `shadow-pop`; in dark it is one step lighter than `surface`. |
| surface-sunken | #F0F2F4 | #161A1F | Wells, table headers, code blocks and segmented-control tracks. Text on it uses `text` and `text-muted`. |
| border | #E2E3E5 | #30343A | Decorative dividers and card outlines. Never the only edge of a control; use `border-strong` for that. |
| border-strong | #848587 | #6E737A | Edges of inputs, checkboxes, secondary buttons and chips. At least 3:1 on `bg` and `surface` in both themes (3.5:1 light, 3.4:1 dark on surface). |
| text | #11151A | #FAFAFA | Primary text and icons on every surface. Black Is Back in light; the paper off-white in dark. |
| text-muted | #656668 | #A7A8AA | Secondary text, captions, helper text and placeholders on `bg`, `surface` and `surface-sunken`. |
| primary | #0A2943 | #98B8D6 | Fill of primary buttons, selected tabs, toggles, progress bars and active nav marks: Dark Eclipse (primary-900 light, primary-300 dark). Label text on it uses `on-primary`. |
| primary-hover | #0D151D | #BFD2E4 | Hover and pressed fill of `primary`. |
| primary-soft | #F2F6F9 | #253C51 | Tinted backgrounds: selected rows, hover on secondary buttons, info banners. Text on it uses `text` or `link`. |
| on-primary | #FFFFFF | #11151A | Text and icons on `primary` and `primary-hover` (14.9:1 light, 8.9:1 dark). Dark mode uses ink, not white. |
| link | #0A2943 | #BFD2E4 | Inline links and text-style buttons on `bg`, `surface` and `primary-soft`. Always underlined in running text. |
| link-hover | #0D151D | #E0E8F1 | Hover state of `link`. |
| accent | #8E494F | #D8A2A5 | The single secondary hue, Cherry Kisses: highlights, new-feature badges, chart emphasis, one accent button per view. Label text on it uses `on-accent`. |
| accent-soft | #FAF3F3 | #341C1E | Tinted background for accent badges and callouts. Text on it uses `accent`. |
| on-accent | #FFFFFF | #11151A | Text and icons on `accent` (6.5:1 light, 8.4:1 dark). |
| focus | #8E494F | #D8A2A5 | Keyboard focus ring: 2px solid with a 2px gap in `bg`. 6.3:1 on `bg` in light, 8.4:1 in dark. It uses the accent so it never blends into Dark Eclipse controls. |
| selection | #E0E8F1 | #253C51 | Text selection background. Text keeps `text`. |
| disabled-bg | #F0F2F4 | #262A2F | Fill of disabled buttons and inputs. |
| disabled-text | #848587 | #656668 | Text and icons on `disabled-bg`. Exempt from contrast rules, so never put required information here. |
| success | #13794A | #1BA766 | Success text, icons and fills on `bg`, `surface` and `success-soft` (5.4:1 light, 5.3:1 dark on `surface`). Always paired with a check icon and a word. |
| success-soft | #E4F3EB | #0F2A1E | Background of success banners and badges. Text on it uses `success`. |
| on-success | #FFFFFF | #11151A | Text on solid `success` fills. |
| warning | #915608 | #F4A134 | Warning text, icons and fills (5.9:1 light, 7.8:1 dark on `surface`). Always paired with a triangle icon and a word. |
| warning-soft | #FBEFD9 | #2B1F0A | Background of warning banners and badges. Text on it uses `warning`. |
| on-warning | #FFFFFF | #11151A | Text on solid `warning` fills. |
| danger | #B33C00 | #E37653 | Errors and destructive actions: text, icons, fills (5.9:1 light, 5.5:1 dark on `surface`). Always paired with an icon and a word. |
| danger-soft | #FBE9E3 | #2E170F | Background of error banners and field errors. Text on it uses `danger`. |
| on-danger | #FFFFFF | #11151A | Text on solid `danger` fills. |
| info | #0A2943 | #BFD2E4 | Informational text and icons. Deliberately the brand hue, so there is no separate blue. |
| info-soft | #F2F6F9 | #253C51 | Background of info banners. Text on it uses `info`. |
| chart-1 | #8E494F | #D8A2A5 | Chart series 1, the anchor shade of Cherry Kisses. Use alone for single-series charts. At least 3:1 on `surface` in both themes. Add a direct label or marker to every series. |
| chart-2 | #4F2A2D | #F2E2E3 | Chart series 2, a darker Cherry Kisses in light and a lighter Cherry Kisses in dark. |
| chart-3 | #CB7E83 | #B16067 | Chart series 3, a lighter Cherry Kisses in light and a deeper Cherry Kisses in dark. |
| chart-4 | #6E3A3F | #E6C5C6 | Chart series 4, a mid shade of Cherry Kisses. |
| chart-5 | #B16067 | #CB7E83 | Chart series 5, the remaining Cherry Kisses shade that still holds 3:1. |
| chart-alt | #0A2943 | #98B8D6 | The one contrasting chart series: Dark Eclipse, the primary brand colour. Chart colours are only Cherry Kisses shades and Dark Eclipse, never status or logo colours. |
| chart-grid | #E2E3E5 | #30343A | Gridlines and axis rules inside charts. Axis labels use `text-muted`. |
| ink | #11151A | #11151A | Raw near-black, Black Is Back: the light theme's text and the dark theme's page background. Use the semantic tokens in UI. |
| logo-spark | #70C6E2 | #70C6E2 | Logo and icon only: Candid Blue, the highlight or signal dot. Never a UI colour. |
| logo-ink | #11151A | #11151A | Logo and icon only: wordmark and one-colour versions, Black Is Back. |

## Scales

Each brand scale is generated from its library anchor. The anchor keeps its exact value at the step nearest its lightness: Dark Eclipse at primary-900, Cherry Kisses at accent-500. Identical in both themes.

| Step | Primary (Dark Eclipse) | Primary roles | Accent (Cherry Kisses) | Accent roles | Neutral |
|---|---|---|---|---|---|
| 50 | #F2F6F9 | light: primary-soft | #FAF3F3 | light: accent-soft | #F7F9FB |
| 100 | #E0E8F1 | light: selection; dark: link-hover | #F2E2E3 | dark: chart-2 | #F0F2F4 |
| 200 | #BFD2E4 | dark: primary-hover, link | #E6C5C6 | dark: chart-4 | #E2E3E5 |
| 300 | #98B8D6 | dark: primary | #D8A2A5 | dark: accent, chart-1 | #CACCCE |
| 400 | #6F9ECB |  | #CB7E83 | light: chart-3; dark: chart-5 | #A7A8AA |
| 500 | #5183B2 |  | #B16067 | brand anchor; light: chart-5; dark: chart-3 | #848587 |
| 600 | #3C6890 |  | #8E494F | light: accent, chart-1 | #656668 |
| 700 | #325270 |  | #6E3A3F | light: chart-4 | #464749 |
| 800 | #253C51 | dark: primary-soft, selection | #4F2A2D | light: chart-2 | #2F3032 |
| 900 | #0A2943 | brand anchor; light: primary, link | #341C1E | dark: accent-soft | #1B1C1E |
| 950 | #0D151D | light: primary-hover, link-hover | #1E1011 |  | #111214 |

## Accessible pairings

AA needs 4.5:1 for body text and 3:1 for large text, controls and chart marks.

- Text on page (light): `text` #11151A on `bg` #FAFAFA: **17.6:1**, AAA.
- Muted on page (light): `text-muted` #656668 on `bg` #FAFAFA: **5.5:1**, AA.
- Primary button (light): `on-primary` #FFFFFF on `primary` #0A2943: **14.9:1**, AAA.
- Accent button (light): `on-accent` #FFFFFF on `accent` #8E494F: **6.5:1**, AA.
- Link on page (light): `link` #0A2943 on `bg` #FAFAFA: **14.3:1**, AAA.
- Danger on soft (light): `danger` #B33C00 on `danger-soft` #FBE9E3: **5.0:1**, AA.
- Dark primary button (dark): `on-primary` #11151A on `primary` #98B8D6: **8.9:1**, AAA.
- Dark muted on surface (dark): `text-muted` #A7A8AA on `surface` #1B2025: **6.9:1**, AA.
- Dark accent on page (dark): `accent` #D8A2A5 on `bg` #11151A: **8.4:1**, AAA.
- Dark success on surface (dark): `success` #1BA766 on `surface` #1B2025: **5.3:1**, AA.
- Dark danger on surface (dark): `danger` #E37653 on `surface` #1B2025: **5.5:1**, AA.
- Dark warning on surface (dark): `warning` #F4A134 on `surface` #1B2025: **7.8:1**, AAA.

## Rules

- Use roles in UI code, never raw scale steps.
- Brand colours are Dark Eclipse and Cherry Kisses only. Candid Blue and Black Is Back are for the logo and icon, never for charts or UI.
- Charts use five shades of Cherry Kisses, plus Dark Eclipse as the one contrasting series. At least 3:1 on the card. Add a label or marker to every series.
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
