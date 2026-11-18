Review the current change set (staged, unstaged, or the last commit) for UI changes and test coverage:

1. Identify whether the change touches anything a user sees or clicks. If not, say so and stop.
2. If yes, check that a test in `tests/ui/` covers it — happy path plus one failure path.
3. Add or update the missing test in `tests/ui/` if coverage is missing.
4. Run the project's test suite in the terminal.
5. Append the run to `tests/results/TEST-REPORT.md`: date, what changed, the command, and the outcome.
6. Report: (1) UI changes found, (2) tests added or updated, (3) the actual test result. Never claim "all OK" without a green run in this session.
