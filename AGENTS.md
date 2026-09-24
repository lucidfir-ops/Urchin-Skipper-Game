# Urchin Skipper working guide

Read `PROJECT_STATUS.md` first; then retrieve only the source, tests or reference sections needed for the task. Record decisions once and link to them. Do not routinely load the full design or historical notes.

## Authority

`Urchin_Skipper_Bible_Definitive_v2.docx` is the sole definitive design document. The designer's authority reset is recorded in [PROJECT_STATUS.md](PROJECT_STATUS.md#design-authority).

Use the Bible and explicit subsequent designer amendments for design decisions. Per its section 1, if requested feedback implementation conflicts with the Bible, report the conflict before making that change so the document or request can be amended. Earlier designs and feedback decisions are historical records only, not active instructions or fallback specifications.

`PROJECT_STATUS.md`, implementation notes and tests describe the current build and outstanding work; they do not override the Bible or establish compliance with it. Preserve working systems while implementing authorized changes. Update tests when the definitive design intentionally changes observed behaviour.

## Work autonomously
Make routine technical, tuning, asset and reversible prototype decisions yourself. Preserve confirmed gameplay. Document consequential assumptions, keep blocked subsystems safe and continue independent useful work. Do not wait for the designer during an authorized autonomous pass. Do not introduce restrictive licences, destroy unique data or silently remove agreed features. USB Xbox is the known-good physical input. Device-aware mapping improvements are authorized; do not guess raw Deck layouts or change global Steam/desktop shortcuts without evidence.

## Verify and learn
Work in testable increments. Diagnose local code locally; after one sensible failed external/framework attempt, consult current official guidance before guessing again. Keep research proportional. Read `docs/FAILURE_NOTES.md` and relevant `docs/EXTERNAL_REFERENCES.md` sections when troubleshooting. Record significant failures, causes and successful alternatives briefly; avoid repeated failed approaches.
Run focused meaningful regressions after simulation changes; `npm test` and `npm run build` before handoff. Run applicable browser/controller smoke flows and inspect runtime screenshots after UI/art changes. Synthetic input tests do not establish physical controller behaviour. Preserve the orthographic camera and separate decoration from simulation geometry.

## Preservation and handoff
The designer's September 16 amendment replaces routine checkpoints with additive, verified game exports under `exports/`; do not recreate the deleted checkpoints. Preserve older exports. Human documents, raw data and assets are irreplaceable; never overwrite their only copy. See `data/README.md` for restore/data categories. Generated exports have authoring recipes; caches and test output are disposable. The DOCX alone is authoritative; its §23 harbour reference is approved and must be preserved except for explicit designer amendments.
Keep `PROJECT_STATUS.md` concise: actual state, superseding decisions, outstanding tasks, verification and latest exports. Put detailed history under `docs/history/`; technical references in `DEVELOPMENT_NOTES.md` and `docs/`. Update `PLAYTEST_GUIDE.md` for user-visible changes. Finish with a working playable build and an honest short handoff.

## GitHub backup and TEMP exports
The designer authorizes this standing workflow: after each completed, verified game update, commit and push the selected source and assets to the public GitHub repository, and create new dated TEMP itch.io and local/Wi-Fi exports. Preserve older exports. Report the GitHub commit and export locations; report any upload failure explicitly. Routine future pushes under this workflow do not require renewed confirmation unless the designer requests a pause or step-by-step work.

Keep GitHub limited to the selected rebuildable source, assets and essential documentation. Keep generated ZIPs, dependencies, caches, recordings, careers, credentials and machine-local files outside the repository. TEMP ZIPs remain local for the designer's itch.io upload. This supersedes earlier no-GitHub directions while retaining the additive export workflow.

The minimal checkout has been prepared and verified locally; its first local commit exists, but GitHub authentication and push permission are confirmed, and first publication remains pending. Follow the designer's current one-step-at-a-time instruction during setup. See [current setup status](PROJECT_STATUS.md#github-backup-and-release-workflow). Recording this policy does not itself complete setup or authorize skipping those steps.
