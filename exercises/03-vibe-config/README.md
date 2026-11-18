# Module 03 — Vibe Code: project configuration, trust, and tool limits

**Goal:** configure how Vibe Code itself behaves in this repo, and understand the trust model.

## Theory (10 min)

Vibe Code (the **Mistral Vibe** VS Code extension, the CLI, or Vibe Desktop) supports project-level configuration in a **`.vibe/` directory at the repo root**. It can contain:

- `config.toml` — configuration: tool permissions, model presets, utility models
- `agents/`, `skills/`, `prompts/`, `plugins/`, `tools/` — project-scoped agents, skills, prompts, and tools
- Vibe Code also reads the open-standard `.agents/skills/` directory (module 02)

**The trust model (do not skip this part in the workshop):**

- Because `.vibe/` config *changes how the agent behaves*, Vibe Code only loads it from directories you have explicitly trusted
- On first start in a folder containing `.vibe/` config, `.agents/skills/`, or an `AGENTS.md`, Vibe asks: **Trust folder / Trust full repo / Don't trust**
- Review project agent config like any other code, especially MCP server definitions and tool permissions — they can grant access to external services or local commands
- Trusted folders are remembered in `~/.vibe/trusted_folders.toml`; the CLI can trust once with `vibe --trust`

**Per-tool permissions** in `config.toml` let you enable or disable tools for this project, e.g. lock the agent down to read-only, or allow full bash. See [Safety, approvals, and permissions](https://docs.mistral.ai/vibe/code/safety-approvals-permissions).

## Exercise (25 min)

1. In the project you cloned for module 01, create a `.vibe/config.toml` with one sensible restriction for your project (for example, disable a tool or restrict shell commands), plus one custom prompt in `.vibe/prompts/`.
2. Restart the Vibe Code session and confirm the trust dialog appears; read every item before clicking **Trust folder**.
3. Verify the restriction actually applies: ask the agent to do something the config forbids and watch it refuse or ask.
4. Compare with `solution/.vibe/config.toml`.

**Bonus:** put a `reviewer` agent in `.vibe/agents/` that always runs the UI test reviewer skill from module 02 before reporting.

## Debrief (5 min)

- Why does the trust prompt exist? (Anyone can commit agent config that weakens safety — trust is your review of that code.)
- What is the right default permission level for a production repo vs a sandbox?
