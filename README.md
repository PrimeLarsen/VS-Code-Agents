# Setting up AI coding agents in VS Code — a hands-on workshop

Teach your team how to make coding agents (**GitHub Copilot**, **Mistral Vibe Code**, and other AGENTS.md-compatible agents) follow your project rules automatically — so "the agent forgot to test again" stops being a thing.

You will learn three mechanisms, and when to use each:

| Mechanism | What it is | When it applies |
| --- | --- | --- |
| `AGENTS.md` | Always-on project instructions every agent reads | Rules that must apply to *every* task |
| Agent Skills (`.agents/skills/`) | Reusable on-demand procedures | Multi-step workflows the agent runs *when relevant* |
| `.vibe/` project config | Vibe Code-specific configuration (permissions, prompts, tools) | Locking down or extending *Vibe Code behavior* in this repo |

## Format

Four modules, roughly 3 hours total. Each module: ~10 min theory, ~25 min exercise, ~5 min debrief. Works as a half-day workshop or as four separate sessions.

| Module | Topic | Key outcome |
| --- | --- | --- |
| 01 | Project instructions with `AGENTS.md` | A testing policy the agent actually follows |
| 02 | Agent skills | A reusable "UI test reviewer" skill |
| 03 | Vibe Code project configuration | A `.vibe/` setup with sensible tool limits |
| 04 | Capstone: wire it all together | An agent that never says "all OK" before tests pass |

## Prerequisites

- VS Code with the **GitHub Copilot** extension and/or the **Mistral Vibe** extension installed
- A project to experiment on: **clone the golden repo from the previous session, or any real project you are working on.** You will build the agent setup directly on that project, so everything you do here is reusable on Monday.
- Basic experience asking an AI agent for code changes
- For module 3: the Vibe Code extension ([overview](https://docs.mistral.ai/vibe/code/overview))

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
  AGENTS.generic.md       Copy-paste starting point for any repo
  AGENTS.powerapps.md     Ready-made policy for Power Apps projects
facilitator-notes.md      Timing, discussion prompts, common pitfalls
```

## How to run it

1. Everyone clones this workshop repo and the project they will test on.
2. Each module has a `README.md` with theory and an exercise. Solutions live in `solution/` — try first, compare after.
3. Use `templates/` as starting points during the exercises.

---

## The one idea to take home

Agents are consistent, not clairvoyant. They follow written, concrete, testable rules — they don't guess your intentions. If a rule matters, write it down where the agent reads it: `AGENTS.md` for always-on rules, a skill for a procedure, `.vibe/` config for tool behavior. Then let CI be the backstop that catches what the agent missed.
