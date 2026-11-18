# Adopting agent setup in your own project and team

The workshop modules (01–04) teach the mechanisms on a project you bring. This guide is for afterwards: applying them to the repo you actually work in, and deciding **who the setup is for**.

## 1. Decide the scope: personal, per-project, or team-wide

| Scope | Where the files live | Who is covered | How it spreads |
| --- | --- | --- | --- |
| **Personal only** | User-level config: `~/.vibe/AGENTS.md`, `~/.vibe/skills/`, `~/.vibe/config.toml` (Vibe); Copilot personal custom instructions in VS Code settings | Only you, on every project you open | Nothing is committed; teammates never see it |
| **One project (recommended start)** | Repo root: `AGENTS.md`, `.agents/skills/`, optionally `.vibe/` and `.github/copilot-instructions.md` | Everyone who clones the repo | Committed in the repo. Copilot reads it automatically; Vibe asks each person to **trust the folder once**, then loads it |
| **A sub-area of a monorepo** | `AGENTS.md` in the subfolder closest to the code | Everyone working in that sub-area | Committed; agents that support workspaces read the closest `AGENTS.md` |
| **A whole team, many repos** | A shared **golden repo** holding the canonical `AGENTS.md`, skills, agents, and templates | Every project started by cloning the golden repo, or by copying files out of it | Keep one canonical copy and change it only via PR; new projects clone it or copy from it |
| **Installable package (Vibe)** | A [Vibe plugin](https://docs.mistral.ai/vibe/code/cli/plugins) (`plugin.json` plus `ai.mistral.vibe/` components) | Everyone who installs the plugin | Shared as a package from a repo, instead of merging files into each project |

Rule of thumb: start **per-project in one repo**. Build a golden repo or plugin only when a second team asks for the same rules — then you have one canonical copy to maintain instead of many drifting forks.

## 2. Pick what goes where

| You want… | Put it in | Starting point |
| --- | --- | --- |
| A rule that applies to every task | `AGENTS.md` | [AGENTS.generic.md](../templates/AGENTS.generic.md), [AGENTS.powerapps.md](../templates/AGENTS.powerapps.md) |
| A multi-step procedure the agent runs when relevant | `.agents/skills/<name>/SKILL.md` | [ui-test-reviewer](../templates/skills/ui-test-reviewer/SKILL.md) |
| To change how Vibe Code itself behaves in this repo | `.vibe/config.toml` | [module 03 solution](../exercises/03-vibe-config/solution/.vibe/config.toml) |
| A dedicated reviewer agent | `.vibe/agents/<name>.toml` | [reviewer.toml](../templates/vibe/agents/reviewer.toml) |
| Enforcement that counts even when an agent errs | CI on every push/PR | [ci-tests.yml](../templates/team/ci-tests.yml) |

## 3. Make the team review agent config like code

Agent config changes how agents behave, so treat it like code:

- Copy [CODEOWNERS](../templates/team/CODEOWNERS) to `.github/CODEOWNERS` — changes to `AGENTS.md`, `.agents/`, and `.vibe/` then require a team review.
- Copy [PULL_REQUEST_TEMPLATE.md](../templates/team/PULL_REQUEST_TEMPLATE.md) to `.github/PULL_REQUEST_TEMPLATE.md` — every PR states the test result and the `TEST-REPORT.md` entry.
- Seed `tests/results/TEST-REPORT.md` from [TEST-REPORT.md](../templates/team/TEST-REPORT.md).

## 4. Rollout checklist

- [ ] Pick one real repo; add `AGENTS.md` from a template and **adapt the test command to the project's real one** — placeholders enforce nothing
- [ ] Open the setup as a PR so the whole team reviews it once
- [ ] Add the skills the team will actually use
- [ ] Vibe users: add `.vibe/config.toml` (module 03) and review it before trusting the folder
- [ ] Add the CI backstop so tests count even when the agent errs
- [ ] In the next retro: did the policy trigger on a real PR? Did anyone follow up on a red `TEST-REPORT.md` entry?
- [ ] If other teams want the same rules: promote the setup to a golden repo (or a Vibe plugin) instead of copy-pasting it repo by repo
