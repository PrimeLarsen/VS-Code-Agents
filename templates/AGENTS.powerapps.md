# AGENTS.md template — Power Apps (canvas, model-driven, and code apps)

Copy to the solution folder root as `AGENTS.md`. Adapt the marked spots.

# Project instructions

This is a Power Apps project that may contain one or more of the following app types:

- **Canvas apps** (YAML source + Power Fx, edited in code)
- **Model-driven apps** (forms, views, commands, client scripts, Power Fx columns)
- **Code apps** (TypeScript/React apps built on the Power Apps code app framework)

UI behavior is verified with **Power Apps Test Engine** (built on Playwright) for canvas and model-driven apps, and **Playwright tests** for code apps.

## Where tests live

All UI tests and their results live in one place, so the team can follow up:

```text
tests/
  ui/                 # Test specs: Test Engine cases (*.test.fx.yaml) and/or Playwright (*.spec.ts)
  results/
    TEST-REPORT.md    # Append-only log of every run: date, app + change, command, outcome
```

- The agent creates these folders if they do not exist
- After EVERY test run, append a short entry to `tests/results/TEST-REPORT.md`: date, what changed, the command, and the outcome (green/red, or why it could not run)
- Never truncate or rewrite the report: it is the project's append-only test history

## UI test policy (ALWAYS applies)

### 1. Identify the app type first

Before making changes, determine which app type you are touching, because the test approach differs:

| App type | UI code lives in | Test with |
| --- | --- | --- |
| Canvas app | `CanvasApps/*/Screens/*.fx.yaml`, `App.fx.yaml`, components | Test Engine test cases (`*.test.fx.yaml`) or Test Studio |
| Model-driven app | forms, views, command bar ribbon customizations, JavaScript/web resources, Power Fx columns | Test Engine (model-driven support) |
| Code app | `*.tsx`, `*.ts`, component/style files | Playwright tests (`*.spec.ts` / `*.spec.tsx`) |

If the project mixes app types, apply the matching rule for each type you touch.

### 2. Identify UI changes

A change is a **UI change** if it touches any of the following. If anything below is touched, steps 3-5 are mandatory.

For **all app types**:

- Anything visual or interactive the end user sees or clicks

For **canvas apps**:

- Screens, components, or controls (galleries, forms, buttons, inputs, charts)
- Behavior or visual properties: `OnSelect`, `OnVisible`, `DisplayMode`, `Visible`, `Items`, `Default`, `Text`, `OnChange`, `Update`
- Navigation (`Navigate()`), forms (`Form.New`/`Edit`/`Submit`), or data validation
- Formulas in `App.fx.yaml` or state variables that drive UI

For **model-driven apps**:

- Form layout, columns added/removed/reordered, business rules affecting fields
- Views (columns, filters, sorting), command bar buttons or ribbon customizations
- JavaScript web resources attached to form events (`onload`, `onsave`, `onChange`)
- Power Fx formulas in low-code plug-ins or columns

For **code apps**:

- React components, props affecting rendering, routes, styles, or state that drives UI
- User interaction handlers (`onClick`, `onChange`, `onSubmit`), conditional rendering, accessibility attributes

### 3. Write or update tests

- Create or update a test that covers the change, following the matching approach from the table above, stored under `tests/ui/`
- Tests must simulate real user behavior: clicks, keyboard input, navigation, form states, not just checking that source code exists
- Cover at minimum: the happy path + one failure path (e.g. validation error, empty input, no access)
- Prefer extending an existing test over creating duplicate coverage

### 4. Run the tests

- Run the project's test suite in the terminal (for example `pac test run`, `npx playwright test`, <!-- ADAPT: your actual command -->) before declaring anything done
- If tests cannot run locally (missing credentials, environment, or dependencies), say so explicitly and list which tests would have to run

### 5. Report honestly

- NEVER say "all OK" or "done" before all relevant tests have been run and are green
- If a test fails: fix it, or report the failure clearly with what failed and why
- Always end with a short summary: which UI changes you made, which tests you added or updated, and the test result
- If asked to skip tests to save time, list exactly which tests are missing so the gap is visible

## Boundaries

- Do not install new packages or test frameworks without asking first
- Do not modify test configuration to make failing tests pass
- Do not delete or skip existing tests to get a green run
