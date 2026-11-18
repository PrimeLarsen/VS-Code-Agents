# Module 01 — Project instructions with AGENTS.md

**Goal:** make every agent in VS Code follow your project rules without being asked.

## Theory (10 min)

`AGENTS.md` is an open standard for project-level agent instructions. You put a file named `AGENTS.md` in the repo root, and compatible coding agents read it automatically as standing instructions for every task in that repo. GitHub Copilot and Mistral Vibe Code both support it, so one file covers your whole toolchain.

Notes:

- **Copilot specifics:** Copilot also reads `.github/copilot-instructions.md`. If you only maintain one file, make it `AGENTS.md` — it is portable across agents. (Many teams keep a one-line copilot-instructions file that says "Read AGENTS.md and follow it.")
- **Where agents look:** repo root first; agents that support workspaces also read `AGENTS.md` in subfolders closest to the files being edited. Keep the root file for project-wide rules.
- **What works in practice:**
  - Short, concrete, behavioral rules ("run X before declaring done", not "care about quality")
  - Commands the agent can literally copy and run
  - A defined place where tests and test results live, so nothing disappears into chat history
  - Explicit priorities when rules conflict (e.g. "security rules win over speed")
  - What NOT to do ("never commit directly to main", "never install packages without asking")
- **What fails:** vague aspirations, long walls of text (past ~150 lines agents start skipping — move procedures into skills), rules that contradict what the user asks in chat — tell users that when they want an exception, they must say so explicitly.

## Exercise (25 min)

1. Clone the project you will use throughout the workshop: the golden repo from the previous session, or a real project you are working on.
2. Write an `AGENTS.md` at its root that enforces a **testing policy**:
   - The agent must identify whether its change touches UI
   - If yes: write or update a test covering it, in the project's `tests/ui/` folder (the agent creates the folder if it does not exist)
   - It must run the test suite in the terminal before declaring the task done, and append the result to `tests/results/TEST-REPORT.md`
   - It must never say "all OK" while a test is red
3. Ask the agent for a small UI change ("add a dark-mode toggle button").
4. Observe: does it write a test? Does it run the suite? Does its final report mention the test result?
5. Open `tests/results/TEST-REPORT.md` and confirm the run was logged there.
6. Compare with `solution/AGENTS.md` and `solution/.github/copilot-instructions.md`.

**Bonus:** move the same file to a second repo and confirm the policy travels with zero extra setup.

## Debrief (5 min)

- Which rules did the agent follow, which did it skip, and how could the wording be tightened?
- Rule of thumb: if a human junior dev could follow your rule without asking questions, the agent can too.
