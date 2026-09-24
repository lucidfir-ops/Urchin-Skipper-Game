# Urchin Skipper

Read [PROJECT_STATUS.md](PROJECT_STATUS.md) for the current playable build and outstanding work. The definitive design is [Urchin_Skipper_Bible_Definitive_v2.docx](Urchin_Skipper_Bible_Definitive_v2.docx), with subsequent designer amendments linked from the status document.

## Local development

Use Node.js 22.12 or later and npm:

```sh
npm ci
npm run dev
```

Open the local address printed by Vite. To verify and build:

```sh
npm test
npm run build
npm start
```

Source, canonical artwork in `public/assets/`, unique source art in `assets/`, generated map data and design documents are preserved. See the [asset layout](docs/ASSET_LAYOUT.md); canonical public artwork is not disposable build output. Dependencies, browser profiles, saved careers, recordings, caches and generated builds stay local. See [data ownership and Git exclusions](data/README.md#git-source-and-local-game-exports).

## itch.io game ZIPs

After each completed, verified game update, back up the selected source and assets to GitHub and create new dated TEMP ZIPs for manual itch.io upload. See the [standing workflow](AGENTS.md#github-backup-and-temp-exports) and [setup status](PROJECT_STATUS.md#github-backup-and-release-workflow).

The existing local packaging workflow is unchanged. After verification and `npm run build`, choose a **new** dated export folder:

```sh
python3 scripts/package-temp.py --output exports/YYYY-MM-DD-release --label "Release description"
```

Upload `UrchinSkipper-TEMP-ITCHIO.zip` from that folder to itch.io. It contains the built game, required licence notices and build identity. The packager also produces the separate local/Wi-Fi ZIP and verifies archive contents. It refuses to overwrite an existing export folder.

Both `dist/` and `exports/` are ignored by Git. Initializing or pushing this repository does not add source code, Git history, recordings or player data to the game ZIPs. Keep older exports locally; [PLAYTEST_GUIDE.md](PLAYTEST_GUIDE.md) covers gameplay checks.

The regular unit suite uses synthetic fixtures. An additional migration regression runs against a private supplied career when it exists locally. Historical September 21/22 browser scenarios and reference-document recipes also use local feedback inputs, which are deliberately excluded from Git; consult their scripts before running those specific scenarios on another machine.

## Minimal source checkout

The public backup selection includes game code, generated maps, canonical runtime artwork, tests, build tools, the definitive DOCX and essential notes. Unique reference artwork, historical screenshots, feedback and exports remain in the author's full workspace; documentation links into those excluded folders will not resolve in a minimal checkout. The artwork integrity test uses the included `assets/asset-integrity.json`, without duplicate source images.

`npm ci`, `npm test` and `npm run build` work from this selection. For lint, formatting, unit tests and the production build together, run `npm run verify -- --unit-only`. Launcher tests need permission to open a local HTTP server. Browser suites additionally need Playwright browser installations; some historical scenarios require excluded private inputs. `scripts/extract-boat-sheets.js` needs the original supplied sheets, and reference-document editing scripts need local historical inputs. These authoring operations are not prerequisites for building or playing the backed-up game.
