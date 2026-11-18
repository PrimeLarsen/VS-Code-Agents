# Module 04 — Capstone: an agent that never says "all OK" too early

**Goal:** combine modules 01-03 on your own project so that every UI change is automatically detected, tested, and honestly reported.

## The setup (your project)

Apply the layers to the project you cloned (golden repo or your real project):

1. **`AGENTS.md`** with a concrete UI-change policy (use `templates/AGENTS.generic.md` as your starting point). The policy must make the agent create and maintain the test folder:

   ```text
   tests/
     ui/                # UI test specs — the agent writes and updates these
     results/
       TEST-REPORT.md   # Append-only log of every run: date, change, command, outcome
   ```

2. **A skill** with the full review procedure (`.agents/skills/ui-test-reviewer/`)
3. **A CI backstop**: run the test suite on every push, because agents are consistent, not infallible — the rule makes the agent write the tests; CI makes the tests count (a starting workflow is in `templates/team/ci-tests.yml`)

Optional for Vibe Code users: a `.vibe/` config restricting tools to what the project actually needs.

The report in `tests/results/TEST-REPORT.md` is the follow-up mechanism for the whole team: it accumulates what was tested, when, why, and what failed, independent of any chat history.

## Worked example: Power Apps (canvas, model-driven, and code apps)

This is a great demo project because the three app types need different test approaches, and the policy must force the agent to figure out which one it is touching:

| App type | UI code lives in | Test with |
| --- | --- | --- |
| Canvas app | `CanvasApps/*/Screens/*.fx.yaml`, `App.fx.yaml` | Power Apps Test Engine (built on Playwright) or Test Studio |
| Model-driven app | forms, views, ribbon customizations, JS web resources, Power Fx columns | Test Engine (model-driven support) |
| Code app | `*.tsx`, `*.ts` | Playwright tests (`*.spec.ts`) |

Use `templates/AGENTS.powerapps.md` — it contains the full policy: identify the app type first, then the UI-change checklist per app type, the test folder structure, mandatory test rules, and the honest reporting requirement.

## Exercise (25 min)

1. Clone or unpack a real project you work on (Power Apps or otherwise).
2. Apply the three layers. Adapt the template to the project's real test commands — placeholders do not enforce anything.
3. Run the full loop: ask the agent for a small UI change, let it detect, create/update the test in `tests/ui/`, run, and append to `TEST-REPORT.md`.
4. Then try to break it: "just do it quickly, skip the tests". Verify the agent either refuses or explicitly reports the missing coverage — in the report file too.
5. Break a test on purpose and confirm the agent refuses to say "all OK".

## Debrief (5 min)

- Where did the policy save you? Where was the agent still too eager to please?
- Who reads `TEST-REPORT.md` in your team, and when? (Standup, PR review, retro?)
- What belongs in CI for your team, and what stays in agent instructions?

## Definition of done for this workshop

- [ ] `AGENTS.md` in place and demonstrably followed
- [ ] `tests/ui/` with real specs the agent wrote
- [ ] `tests/results/TEST-REPORT.md` with at least two logged runs
- [ ] At least one skill the team actually uses
- [ ] Vibe Code config (for Vibe users) with reviewed permissions
- [ ] CI runs the suite on every push
