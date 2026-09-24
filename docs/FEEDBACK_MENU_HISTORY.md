# September 16 — clarified Back/Forward navigation

The designer answered the pending question: **“Step back through menus to title; Forward retraces them.”** This explicitly supersedes the direct-to-title interpretation in the earlier [Frank/travel increment](FEEDBACK_FRANK_TRAVEL_NAVIGATION.md). All prior tutorial, fade, phone and gameplay updates remain included.

## Behavior

- Back/B walks the menus actually visited, one at a time, until the title root. Example: Controls → Settings → Harbour → Title. Water is not a Back destination; Resume and Menu retain their established gameplay behavior.
- Forward retraces those steps: Title → Harbour → Settings → Controls. The small arrow beside Back is enabled wherever a forward destination exists. At title, Up from Continue selects Forward; within menus the arrow participates in keyboard/controller focus. Left/right on remapping's navigation header moves between Back/Forward without changing the displayed device.
- Each visited view restores its selected choice, chart/forecast settings and scroll position. Opening a different menu or explicitly resuming gameplay clears the abandoned forward path. Scale/touch preferences can still be adjusted at title without losing that path.
- Back from a purchase cancels it and returns to its shop. Confirmations, order drafts and exit dialogs are not replayed through Forward. Explicit Cancel retains its local meaning; completed purchases are never executed again by navigation.
- History is transient in the current tab. New/load/next-day world replacement clears it; entries are also guarded by world identity and day phase. Back to the title preserves the current session, including an isolated Test Mode/prototype, so Forward can retrace it. Explicit return-to-title/leave-mode actions retain their existing return-to-career behavior, and Test Mode still cannot overwrite the real career.

## Verification and deliverables

Unit regressions cover multi-step traversal, draft/scroll restoration, branching, purchase dismissal, world replacement, Test Mode isolation and remapping header focus. Chromium/Firefox phone checks exercise the full route in both orientations at 80/100/150%, alongside the retained Frank and departure checks. The controller suite follows the rendered focus graph and checks Back/Forward plus existing helm, remapping, resume and reconnect behavior.

[Acceptance evidence and exact package fingerprints](history/2026-09-16-menu-history/acceptance/README.md). Recipe: `npm run build`, then `python3 scripts/package-temp.py --output exports/2026-09-16-navigation`. New title identity: **TEMP · SEP 16 · MENU HISTORY UPDATE**. Both additive ZIPs contain the same game bytes; all older builds and checkpoints are retained. Physical S22/Xbox/Deck testing and actual itch.io upload remain the designer's follow-up.
