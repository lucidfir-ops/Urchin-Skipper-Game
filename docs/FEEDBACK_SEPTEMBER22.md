# September 22 playtest and optimisation amendment

> Historical amendment/implementation record. The current approved design is consolidated in [bible.md](../bible.md). This record preserves provenance; it is not an independent authority or fallback specification.

The designer authorises the September 22 playtest fixes and the performance audit's recommendations, with one superseding constraint: prepare required content before play, rather than defer essential terrain/artwork downloads into gameplay. Preserve all original maps, artwork, careers, older exports, the orthographic camera and the DOCX (including §23). The changes concern presentation, input delivery and implementation efficiency; simulation rules remain authoritative.

Acceptance work:
- [x] Reverse/pivot/thruster wash and underwater bubbles stay below boat artwork.
- [x] A quick Chart tap opens a persistent chart.
- [x] Phone rotation is permitted; tablet/phone layout adjustment survives rotation, with separate saved orientations and visible clock/load instruments.
- [x] Clock digits fit the face; Chart only has no surrounding text or card.
- [x] Reuse raster buffers and remove large tide/nearby-reef rebuild stalls.
- [x] Reduce autosave cloning/serialisation stalls while preserving verified backups and restore points.
- [x] Prepare compact vessel derivatives and required content before play; retain all terrain locally after startup.
- [x] Reduce decorative simulation/current sampling, repetitive normalisation/spec/geometry work, route searches and UI layout churn.
- [x] Compress local delivery; verify production browser flows, mature-save performance, unit tests and additive TEMP exports.

Implementation details, retained failed comparisons and verification are in [the release history](history/2026-09-22-performance-and-device-fixes/README.md). Synthetic rotation and input do not certify OS auto-rotate or physical controller routing.
