# Facilitator notes

## Timing (half-day workshop)

| Slot | Content |
| --- | --- |
| 0:00-0:15 | Welcome, round of tool checks (Copilot / Vibe extension installed and signed in), everyone has their project cloned |
| 0:15-1:00 | Module 01 — AGENTS.md |
| 1:00-1:10 | Break |
| 1:10-1:45 | Module 02 — Agent skills |
| 1:45-2:30 | Module 03 — Vibe Code config (skip if the team only uses Copilot) |
| 2:30-2:40 | Break |
| 2:40-3:20 | Module 04 — Capstone |
| 3:20-3:30 | Retro: what will we adopt in our real repos on Monday? |

## Preparation

- This session builds on the earlier cloning session: participants work on the golden repo they already cloned, or on a real project they brought. The setup they build here is theirs to keep.
- If you prepare the golden repo yourself, plant one deliberate UI bug to give module 04 something to catch.
- Test every exercise yourself on the exact tool versions the team uses, the week before.
- Have the two templates printed or bookmarked.

## Discussion prompts that work

- "Show me the last agent change you accepted without reading. What would have caught a problem?" (leads naturally to AGENTS.md rules and CI)
- "Which of our team rules live only in people's heads?" (leads to the always-on vs on-demand split: AGENTS.md vs skills)
- "Who in the team would actually read `TEST-REPORT.md`, and when?" (standup, PR review, retro — this is the follow-up habit you are installing)
- For mixed-tool teams: "Which rules should be identical across Copilot and Vibe Code?" (AGENTS.md is the portable answer)

## Common pitfalls

1. **Vague rules.** "Be careful with tests" does nothing. "Run `npm test` before reporting" works. Fix wording live — it lands better than theory.
2. **AGENTS.md bloat.** Over ~150 lines agents start skipping. Move procedures into skills, keep always-on rules in AGENTS.md.
3. **Contradicting the user.** When someone tells the agent "just ship it", the policy often loses. The template handles this: the agent may comply but must report the coverage gap. Point this out explicitly.
4. **Trust-clicking.** In module 03, watch for participants clicking Trust without reading. That is the teachable moment: project agent config is code.
5. **Placeholder commands.** Participants who forget to adapt `npm test` to their real command get rules that enforce nothing. Check every repo's adapted command.
6. **Report hygiene.** Agents sometimes *rewrite* `TEST-REPORT.md` instead of appending, wiping history. The templates forbid it — check each participant's report still has all runs at the end.

## Follow-up

- Ask each participant to ship their AGENTS.md to one real repo within a week
- Review the first real PR where the policy triggered, together
- In the next team retro, open `TEST-REPORT.md` from someone's project and see whether anyone followed up on a red entry
