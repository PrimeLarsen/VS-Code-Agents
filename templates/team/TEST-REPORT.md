# Test report — append-only

Copy this file to `tests/results/TEST-REPORT.md` in your project.

Every test run gets one entry, appended at the bottom. Never edit, reorder, or delete existing entries — this file is the project's test history.

Entry format:

```text
## YYYY-MM-DD — what changed
- Command: `the command that was run`
- Outcome: green / red / could not run (reason)
- Notes: what failed, or what must run in CI instead
```

## 2026-01-15 — example entry: added dark-mode toggle

- Command: `npm test`
- Outcome: green (42 passed)
- Notes: happy path and no-permission path covered in `tests/ui/dark-mode.spec.ts`
