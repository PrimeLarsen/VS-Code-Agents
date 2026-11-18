# Setting up AI coding agents in VS Code — a hands-on workshop

Teach your team how to make coding agents (**GitHub Copilot**, **Mistral Vibe Code**, and other AGENTS.md-compatible agents) follow your project rules automatically — so "the agent forgot to test again" stops being a thing.

You will learn three mechanisms, and when to use each:

| Mechanism | What it is | When it applies |
| --- | --- | --- |
| `AGENTS.md` | Always-on project instructions every agent reads | Rules that must apply to *every* task |
| Agent Skills (`.agents/skills/`) | Reusable on-demand procedures | Multi-step workflows the agent runs *when relevant* |
| `.vibe/` project config | Vibe Code-specific configuration (permissions, prompts, tools) | Locking down or extending *Vibe Code behavior* in this repo |

The first two mechanisms are tool-agnostic and work with GitHub Copilot out of the box. The third one is specific to Mistral Vibe Code — **Copilot-only teams can skip it (module 03)**.

## Format

Four modules, about 3 hours of content (each module: ~10 min theory, ~25 min exercise, ~5 min debrief). Runs as one half-day session — ~3.5 h including welcome, breaks, and retro, see [facilitator-notes.md](facilitator-notes.md) — or as four separate sessions.

| Module | Topic | Key outcome |
| --- | --- | --- |
| 01 | Project instructions with `AGENTS.md` | A testing policy the agent actually follows |
| 02 | Agent skills | A reusable "UI test reviewer" skill |
| 03 | Vibe Code project configuration | A `.vibe/` setup with sensible tool limits |
| 04 | Capstone: wire it all together | An agent that never says "all OK" before tests pass |

**Module 03 is optional.** It covers Vibe Code-specific configuration; if your team works mainly with GitHub Copilot, skip it — modules 01, 02, and 04 run entirely on `AGENTS.md` and skills, which Copilot reads natively.

## Prerequisites

- VS Code with the **GitHub Copilot** extension and/or the **Mistral Vibe** extension installed
- A project to experiment on: **any real project you are working on** (if your team already has a "golden repo" from a previous session, use that). You will build the agent setup directly on that project, so everything you do here is reusable on Monday.
- Basic experience asking an AI agent for code changes
- Only if you run module 03 (optional — skip it if your team only uses Copilot): the Vibe Code extension ([overview](https://docs.mistral.ai/vibe/code/overview))

## What you end up with

By the end, your own project contains an agent setup plus a **dedicated `tests/` folder** that the agent creates and maintains:

```text
tests/
  ui/                # UI test specs (Playwright / Test Engine / project framework)
  results/
    TEST-REPORT.md   # Append-only log of every test run: what changed, command, outcome
```

The agent writes the specs and appends to the report after every run, so the team can always follow up on what has been tested and what failed.

## Repo map

```text
exercises/
  01-agents-md/      Project instructions that agents actually follow
  02-agent-skills/   Reusable procedures as skills
  03-vibe-config/    Vibe Code: .vibe/ config, trust, tool permissions
  04-capstone/       Combine everything on your own project
templates/
  AGENTS.generic.md          Copy-paste starting point for any repo
  AGENTS.powerapps.md        Ready-made policy for Power Apps projects
  skills/ui-test-reviewer/   The module 02 skill as a ready-made template
  vibe/agents/reviewer.toml  The module 03 bonus agent as a ready-made template
  team/                      Copy into your own repo: CODEOWNERS, PR template, TEST-REPORT seed, CI workflow
docs/
  adopting-in-your-team-repo.md  Personal vs team-shared setup (golden repo, plugins), what goes where, rollout checklist
facilitator-notes.md      Timing, discussion prompts, common pitfalls
CONTRIBUTING.md           How to propose changes and ask questions
LICENSE                   MIT — free to use, adapt, and share
```

## How to run it

1. Everyone clones this workshop repo and the project they will test on.
2. Each module has a `README.md` with theory and an exercise. Solutions live in `solution/` — try first, compare after.
3. Use `templates/` as starting points during the exercises.

## Using this in your own project and team

After the workshop, [docs/adopting-in-your-team-repo.md](docs/adopting-in-your-team-repo.md) covers how to apply the setup to your real repos: whether the agent setup is **personal only** (user-level `~/.vibe/`), **per project** (committed `AGENTS.md` + skills), or **team-wide** (a golden repo everyone clones from, or an installable Vibe plugin) — plus a what-goes-where table and a rollout checklist. Ready-made files for your own repo live in `templates/team/`.

## FAQ for participants

- **The agent ignores my `AGENTS.md`.** Check the file is named exactly `AGENTS.md` and sits in the repo root (agents that support workspaces also read `AGENTS.md` files in subfolders closest to the files being edited). Restart the agent session after adding or changing it.
- **My skill never triggers.** Agents choose skills based on the `description` in the SKILL.md frontmatter. Write *when* to use the skill ("Use when the user changes UI code or asks for a change review"), not just what it does.
- **Vibe Code asks about trust every session.** You chose "Don't trust" or closed the dialog. Reopen the project and choose **Trust folder**, or trust once per run with `vibe --trust` in the CLI. Trusted folders are remembered in `~/.vibe/trusted_folders.toml`.
- **The agent says "all OK" but I don't see a test run.** Per the policy it must log every run in `tests/results/TEST-REPORT.md` — open it. If nothing was logged, the policy was not followed; tighten the wording in `AGENTS.md`.
- **Tests can't run in my environment.** The policy covers this: the agent must say so explicitly and list what would have to run in CI.

---

## The one idea to take home

Agents are consistent, not clairvoyant. They follow written, concrete, testable rules — they don't guess your intentions. If a rule matters, write it down where the agent reads it: `AGENTS.md` for always-on rules, a skill for a procedure, `.vibe/` config for tool behavior. Then let CI be the backstop that catches what the agent missed.

---

Licensed under the [MIT License](LICENSE). Questions or improvements? See [CONTRIBUTING.md](CONTRIBUTING.md).
