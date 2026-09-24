# Chart window sizing — September 17 designer amendment

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

The designer supplied [current layout](../feedback/9-17a.jpg) and [preferred proportions](../feedback/9-17b.jpg), requesting a narrower information window on larger screens so the local chart does not become small inside a stretched parchment panel. This is a presentation amendment to the definitive DOCX menu charts, without a substantive design conflict.

Local departure and knowledge windows now centre horizontally, with width bounded by viewport height and a 1200 screen-pixel ceiling, independent of text scaling. The local map no longer has the 480-pixel display-width cap. It scales to its column and available screen height, keeping a square click target. The separate parchment container background is removed; the existing chart artwork, symbols, hazard/depth data and caption remain. Touchscreen menus retain their full-width scrollable page and charts fill their columns. No SVG conversion is needed for this layout fix.

Verification uses `npm run verify -- --unit-only`, and Chromium/Firefox `--browsers-only --suite=chart-layout` / `--suite=chart-layout-firefox`. The focused browser journey covers 1728×1117, 1920×1080, 1280×800 and 1024×640 desktops, 50/150% UI scales, keyboard/gamepad Back and chart navigation, and 780×360 / 360×780 touch scrolling. Runtime screenshots and measurements are kept under [acceptance](history/2026-09-17-chart-layout/acceptance/README.md).

Additive export recipe: `npm run build`, then `python3 scripts/package-temp.py --output exports/2026-09-17-chart-layout`. Both verified ZIPs retain earlier releases and exclude careers/profiles. Title identity: “TEMP · SEP 17 · CHART LAYOUT”.
