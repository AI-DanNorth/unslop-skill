# Gates

A run lives in `.unslop/<run-id>/` (run id = `YYYYMMDD-HHMM-<slug>`). A phase is done only when its gate file exists and validates. The orchestrator checks the gate before starting the next phase. A missing gate means the phase did not happen, whatever the conversation says.

| Phase | Skill | Gate file | Valid when |
|---|---|---|---|
| 0 Intake | intake | `00-contract.md` | Medium, visitor mode, scope, profile, brand authority and target URL or path are all filled |
| 1 Capture | capture | `01-evidence/manifest.json` | `control.ok` is true and every requested width has a screenshot, DOM dump and styles dump |
| 2 Sweep | sweep | `02-mechanical.json` | Every detector listed in the resolved thresholds has a status (`ran`, `skipped: reason`, `not-verified: reason`) |
| 3 Lenses | lens-* | `03-lenses/<lens>.json` | One file per lens the contract selected |
| 4 Synthesize | synthesize | `04-report.md` | Verdict word present; findings validate |
| 5 Remedies | remedies | `05-fixes/round-N.md` | Each fix names the finding it answers |
| 6 Verify | verify-fix | `06-verdict.md` | Every prior finding scored resolved, partial or unresolved |

## Skips

A phase may be skipped only when the user says so. The skip is written to `run.json` as `{"phase": 3, "skipped_by": "user", "reason": "..."}`. Three things are never skipped, even under time pressure: the control render, the Floor checks and the gate check itself.

## Loop budget

At most 3 fix rounds. After round 2 with Floor or P1 findings still open, the orchestrator offers `explore-directions` instead of a third round of patches.
