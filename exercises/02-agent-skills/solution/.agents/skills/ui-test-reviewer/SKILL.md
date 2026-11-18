---
name: ui-test-reviewer
description: Reviews recent code changes and verifies UI test coverage before anything is reported as done. Use when the user changes UI code, asks for a change review, or wants to confirm test coverage.
---

# UI Test Reviewer

Run this procedure on the current change set (staged, unstaged, or the last commit).

## 1. Find UI changes

Look at the diff and flag anything matching:

- Components, pages, routes, or style files
- Interaction handlers (`onClick`, `onChange`, `onSubmit`) or conditional rendering
- Anything a user sees or clicks in the running app

If nothing matches, say so and stop here: no UI change, no UI test needed.

## 2. Check coverage

For each flagged change, answer:

- Does a test already cover this behavior? (search `tests/ui/`)
- Does the test simulate real user behavior, not just source-code assertions?
- Is at least one failure path covered (validation error, empty input, no access)?

## 3. Fix the gaps

- Extend an existing test if possible; create a new one only when nothing fits
- New tests go in `tests/ui/` (create the folder if it does not exist)
- Follow the project's existing test framework and naming conventions

## 4. Run and report

- Run the project's test suite in the terminal
- Append the run to `tests/results/TEST-REPORT.md`: date, what changed, the command, and the outcome
- Report: (1) UI changes found, (2) tests added or updated, (3) actual test result
- If a test cannot run locally, say why and list what must run in CI instead

Never report "all green" without a real test run in this session.
