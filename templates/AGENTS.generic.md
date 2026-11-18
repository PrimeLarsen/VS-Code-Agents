# AGENTS.md template — generic project

Copy to the repository root as `AGENTS.md` and adapt the marked spots.

# Project instructions

## Testing policy (ALWAYS applies)

### Identify UI changes

Before finishing any task, check whether your change touches:

- Components, pages, routes, or styles that the user sees
- Interaction handlers (`onClick`, `onChange`, `onSubmit`) or conditional rendering
- Anything visual or interactive in the running app

If any of the above changed, the change is a **UI change** and the rest of this policy is mandatory.

### Where tests live

- All UI tests live in `tests/ui/` — create the folder if it does not exist
- After EVERY test run, append a short entry to `tests/results/TEST-REPORT.md` with: date, what changed, the command you ran, and the outcome (green/red, or why it could not run)
- Never truncate or rewrite the report: it is the project's append-only test history

### Write or update tests

- Add or update a test covering the change, in the project's existing test framework
- <!-- ADAPT: name your test framework here -->
- Tests must simulate real user behavior (click, type, navigate), not just assert on source code
- Cover at minimum the happy path and one failure path (validation error, empty input, no access)

### Run before reporting

- Run `<!-- ADAPT: your test command, e.g. npm test / npx playwright test -->` before declaring any task done
- NEVER say "all OK" or "done" while a test is failing or untested
- If tests cannot run locally, say so explicitly and list what must run in CI instead

### Report honestly

End every task with a short summary:

1. Which UI changes you made
2. Which tests you added or updated
3. The actual test result (green/red, or why it could not run)

## Boundaries

- Do not install new packages or test frameworks without asking first
- Do not modify test configuration to make failing tests pass
- Do not delete or skip existing tests to get a green run
- If the user asks to skip tests, do it, but list exactly which coverage is now missing

<!-- ADAPT: add project-specific sections: architecture, conventions, deploy commands, gotchas -->
