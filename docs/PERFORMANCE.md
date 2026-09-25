# Frame performance checks

`npm run verify -- --suite=performance` measures the production build in Chromium. `--suite=performance-firefox` uses Firefox. Run these in isolation, not concurrently with another browser or a build. Player profiles are not opened.

The default software-renderer regression budget is mean frame ≤40 ms, p95 frame ≤65 ms and p95 update-through-render-submission CPU ≤25 ms. These intentionally detect the previously observed ~103 ms/frame regression; they are not a declaration that 25 FPS is the hardware target. Set `URCHIN_PERFORMANCE_PROFILE=hardware` for the stricter 60 Hz target: mean ≤17.5 ms, p95 ≤22 ms, CPU p95 ≤14 ms. Physical Deck sustained performance still requires a hardware run.

Samples include input/UI, fixed-step simulation, effects/audio, save, drawing, HUD and Phaser renderer submission. `frameMs` uses the engine's **raw inter-frame interval**, not its smoothed simulation delta. GPU completion and browser composition cannot be individually attributed by these CPU timestamps. Their scheduling impact remains visible in the raw frame interval. A 600-frame ring bounds diagnostic memory. Reports include means, p95 and maxima, and the checker fails on budget violations.

Automatic renderer selection retains hardware WebGL, but uses Canvas when a WebGL context rejects `failIfMajorPerformanceCaveat` or explicitly identifies software emulation (SwiftShader/llvmpipe/softpipe). `?renderer=webgl` and `?renderer=canvas` allow controlled comparisons. This does not change simulation, camera projection, controls or browser/global settings. No Phaser/runtime dependency was added or removed.

The first instrumented comparison identified high renderer/presentation overhead, with drawing averaging only ~1.3 ms. That attempt was not a valid isolated benchmark (another controller run overlapped); its failure remains recorded. Subsequent isolated production results are the acceptance evidence. Phaser's [rendering guide](https://phaser.io/tutorials/phaser-4-rendering-concepts) explains upload, text-update and draw-call costs; installed `TimeStep.js` distinguishes raw from smoothed delta, and `Game.js` emits the post-render event used here.

The final pass adds an enforced seven-vessel scene at the minimum gameplay zoom, using real sector depths and maximum bounded traffic. A dedicated isolated training fixture fixes weather/clock; it measures rendering/simulation, not heavy real-save writes. Separate career/save regressions cover saving, and instrumentation includes the autosave phase in real play. Storm coverage remains in the iteration suite.

The populated coastal scene initially failed at 45.28 ms/frame (CPU p95 23.9 ms). Distant decorative tree facets, kelp veins and product-dot density—not terrain, currents, markers or collision geometry—were simplified. The isolated rerun passed at 24.07 ms/frame, p95 33.4 ms and CPU p95 13.3 ms; normal Chromium Canvas averaged 16.76 ms. Before/after evidence is retained under `docs/history/2026-09-14-v2/`. This is software-rendered headless evidence, not physical Deck FPS.

Firefox then exposed the cost of repeatedly rendering even unchanged Graphics commands: the populated scene averaged 32.50 ms, but CPU p95 was 36 ms, failing the same 25 ms budget. Following the [official Graphics guidance](https://docs.phaser.io/phaser/concepts/gameobjects/graphics), distant static coastal decoration is now baked into one reusable, at-most-2048×2048 texture. It invalidates on terrain, camera bucket, viewport or conservative tidal-exposure changes; close views retain detailed vectors. No per-frame texture creation or world-sized atlas. The focused Firefox rerun passed at 16.95 ms/frame and CPU p95 18 ms. Both failures and successful alternatives are retained, not discarded.

The broader storm fixture separately found a 27 ms CPU p95 in Firefox. Wide-view water now omits tiny foam droplets/grain and scales decorative wavelet spacing, while preserving the same wind-driven whitecap silhouette calculation and all physics. The focused rerun passed at 19.87 ms/frame, 33.30 ms frame p95 and 24 ms CPU p95. Close views retain full detail. This is an additional scene, not a replacement for the populated/coastal or normal baselines; budgets remain unchanged.

## v2 stabilization samples

Production bundle `index-B3u2dhgX.js`, isolated sequential headless runs, milliseconds:

| Browser / automatic renderer | Scene | Mean frame | Frame p95 | CPU p95 |
| --- | --- | ---: | ---: | ---: |
| Chromium / Canvas | Normal | 16.67 | 16.70 | 8.2 |
| Chromium / Canvas | Seven vessels, wide coast | 19.72 | 33.40 | 8.1 |
| Chromium / Canvas | Wide storm, default 15 Hz surface redraw | 24.30 | 33.40 | 7.5 |
| Firefox / WebGL | Normal | 16.66 | 17.14 | 18 |
| Firefox / WebGL | Seven vessels, wide coast | 16.67 | 17.14 | 16 |
| Firefox / WebGL | Wide storm, default 15 Hz surface redraw | 19.16 | 33.24 | 21 |

All six pass the unchanged software regression budget. Forced Chromium software WebGL remains diagnostic-only at 67.87 ms mean, confirming why automatic fallback matters. The 60 Hz surface-redraw comparison still records occasional costly rebuild frames (Firefox maximum 167.28 ms); it is not the shipped 15 Hz setting, and maxima are retained rather than hidden. Brief samples and passing means/p95 do not establish hitch-free long sessions or physical Deck 60 FPS. Run sustained hardware profiling before raising surface cadence or claiming a hardware performance target.

## Touchscreen and fishing feedback samples

Production bundle `index-Rz4td_eD.js`, September 15 UTC. Isolated normal and seven-vessel checks pass in both browsers; touch input/layout is tested separately. The software budgets above are unchanged.

| Browser / automatic renderer | Scene | Mean frame | Frame p95 | CPU p95 |
| --- | --- | ---: | ---: | ---: |
| Chromium / Canvas | Normal | 16.67 | 16.80 | 8.3 |
| Chromium / Canvas | Seven vessels, wide coast | 19.44 | 33.40 | 8.0 |
| Firefox / WebGL | Normal | 16.85 | 17.16 | 18 |
| Firefox / WebGL | Seven vessels, wide coast | 16.67 | 17.16 | 17 |

[Raw samples and acceptance](history/2026-09-14-touch-feedback/acceptance/README.md) retain maxima and the forced Chromium software-WebGL diagnostic (64.44 ms mean). Storm figures above belong to the earlier v2 build. These short headless samples do not establish Android/iOS or physical Deck FPS.

## September 22 performance and reliability

[Implementation, measurements and retained failures](history/2026-09-22-performance-and-device-fixes/README.md) cover worker terrain painting and save encoding, prepared vessel artwork, immutable grid sharing, bounded route retries/spatial bins, cached geometry/quota/crew work and reduced UI churn. All maps stay eager; required content is prepared before play. Close shoreline detail is baked; distant kelp uses one representative stem per bed. Canvas water commands use a bounded image at the existing 15 Hz; WebGL keeps native animated geometry. Canvas paths avoid unused full pixel readbacks.


Final retained measurements (ms; software/headless conditions):

| Scene | Mean interval | p95 interval | Maximum interval | CPU p95 |
| --- | ---: | ---: | ---: | ---: |
| Mature career, Chromium Canvas, 22 s | 17.90 | 33.30 | 66.60 | 8.30 |
| Seven vessels, Chromium Canvas | 24.54 | 33.40 | 50.00 | 13.90 |
| Seven vessels, Firefox WebGL | 20.18 | 33.32 | 34.22 | 23.00 |

The final mature run contains 1230 frames, 4 tide updates and 2 real autosaves. Save preparation/dispatch peaked at 5.0 ms; final storage commits took 1.7/1.7 ms. It still records simulation and HUD peaks of 46.7/34.8 ms. Those remaining spikes need longer hardware profiling; the traffic budget does not establish their elimination. Forced Chromium software WebGL remains diagnostic-only, at 97.87 ms mean; automatic selection uses Canvas on that path. The seven-vessel software regression budgets remain unchanged.

The old 180-frame sandbox check alone cannot capture mature saves/tide stalls. Run `npm run verify -- --browsers-only --suite=september22-performance` for the sustained imported-career check, and `--suite=performance` / `--suite=performance-firefox` for the separate seven-vessel and renderer comparisons. Hardware/frame-time certification and long-session leak analysis remain outstanding.

## September 24 tablet recording

Dry full-screen weather shading now retains its Canvas until quantized visible inputs change; rain/lightning, visibility, working lights, viewport and zoom still update. Decorative foam uses elapsed-time cohorts with swept wet-path checks instead of running every foam shoreline check on every physics step. Physical entities keep their previous cadence. Unchanged touch text is retained. [Before/after diagnostic profiles, limitations and production receipts](history/2026-09-24-deploy-and-tablet/README.md). The isolated desktop portrait comparison improved mean frame time from 29.46 to 18.98 ms; p95 remained ~33.3 ms and occasional long stalls remain. This does not establish physical tablet performance.
