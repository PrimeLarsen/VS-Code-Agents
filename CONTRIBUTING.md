# Contributing

Thanks for helping make this workshop better. This repo is shared with groups of developers (including juniors), so clarity beats cleverness.

## Questions and ideas

- Open an **issue** for anything that is unclear, wrong, or missing — no question is too small.
- Facilitators: if an exercise step didn't work as written for your group, note the tool versions in the issue so we can reproduce it.

## Proposing changes

1. Fork the repo and create a branch named `vibe/<short-topic>`.
2. Make focused changes; one topic per pull request.
3. Open a pull request against `main` and describe what changed and why.

## Content rules for this repo

- **Keep exercise steps and `solution/` in sync.** If you change a step in `exercises/<n>/README.md`, update the matching file under `solution/`.
- **Templates use `<!-- ADAPT: ... -->` markers** for project-specific spots. Never hardcode one project's commands into `templates/`; solutions may show a generic default (e.g. `npm test`) because they demonstrate the pattern.
- **Stay tool-accurate.** Claims about GitHub Copilot or Mistral Vibe Code behavior must match the current docs (see the links in the module READMEs). When behavior changes, update the module text and the facilitator notes together.
- **Junior-friendly language.** Short sentences, concrete examples, no unexplained jargon. If a rule matters, write it the way you would tell a new teammate.
- **Never commit secrets, tokens, or real project paths** from a participant's machine. Solutions and templates must be generic.
- Markdown style: ATX headings, fenced code blocks with a language tag, tables for comparisons. Keep lines readable; hard-wrap is not required.

## Running the workshop

See [README.md](README.md) for the format and [facilitator-notes.md](facilitator-notes.md) for timing, prompts, and pitfalls. Test any exercise change yourself on the tool versions your group uses before submitting.

## License

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE), the same as the rest of the repo.
