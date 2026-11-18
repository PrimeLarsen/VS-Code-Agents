# Module 02 — Agent skills: reusable procedures

**Goal:** package a multi-step procedure once, and have every agent run it on demand.

## Theory (10 min)

`AGENTS.md` rules are **always on**. Skills are the complement: **on-demand procedures** the agent loads when the task matches. A skill is a folder with a `SKILL.md` file (and optional supporting files) that describes how to run a workflow.

- **Location:** `.agents/skills/<skill-name>/SKILL.md` is the open Agent Skills standard that several agents read. Vibe Code reads both that location and its own `.vibe/skills/` directory.
- **Anatomy of a SKILL.md:** YAML frontmatter with `name` and `description` (the description is what the agent uses to decide when the skill is relevant — write it carefully!), then the procedure as markdown steps.
- **Good skill candidates:** "review a UI change and ensure test coverage", "cut a release", "onboard to this codebase", "write a migration". Bad candidates: one-liner facts (those belong in `AGENTS.md`).
- **Discovery:** agents typically read the description and load the full skill only when relevant, so a precise description ("Use when the user changes UI code or asks for a change review") works better than "Helps with tests".

## Exercise (25 min)

1. In the project you cloned for module 01, create `.agents/skills/ui-test-reviewer/SKILL.md`.
2. Give it a description that triggers on UI changes and code review requests.
3. Write the procedure: check the diff for UI code, verify a test exists per the project policy, run the suite, append the run to `tests/results/TEST-REPORT.md`, report gaps.
4. Test it: ask the agent "review my last change for test coverage" and watch it follow the steps.
5. Compare with `solution/.agents/skills/ui-test-reviewer/SKILL.md`. A ready-made copy also ships as a template at `templates/skills/ui-test-reviewer/SKILL.md` (from the repo root).

**Bonus:** add a checklist file inside the skill folder and reference it from `SKILL.md`. Skills can carry their own supporting files.

## Debrief (5 min)

- When is a rule better placed in `AGENTS.md` vs a skill? (Always-on vs on-demand.)
- Did the agent load the skill without being told its name? If not, improve the description.
