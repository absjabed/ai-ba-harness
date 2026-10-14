# Second demo test, of 0.5.0, and what 0.5.1 changed

On 2026-10-15 a fresh project, "FleetKeep Demo", was created from harness 0.5.0 with a shared
(local) remote and three clones: the Lead BA's, a second BA's and a developer's. A separate project
created from 0.4.2 was used to test the upgrade instructions. As in the first test
([`08-demo-test.md`](08-demo-test.md)), each command ran as a sub-agent in a fresh context following
the command files exactly, without Atlassian, and logged every point where the definitions were
unclear, contradictory or forced a guess. Fixes were made between runs, and the Lead BA's clone was
updated to them twice, so the later runs also tested the fixes.

The raw output is kept in
[`examples/fleetkeep-demo-test-2/`](../examples/fleetkeep-demo-test-2/DEMO-TEST.md).

| Run | What it tested | Outcome | Points |
|---|---|---|---|
| Upgrade 0.4.2 to 0.5.0 | The CHANGELOG and SETUP upgrade steps, followed as written | Upgraded and checked clean, but the steps missed files and contradicted each other on `sync.json` | 10 |
| `/setup`, offline | Offline mode, re-run detection, one preview, the RACI and maintainers check | Worked; two RACI disagreements found and fixed with the BA | 7 |
| `/kb-seed inbox` | Two documents, one contradicting the other, a contact to redact | Worked; the contradiction became a question, the contact was redacted | 13 |
| `/intake`, then decide later | Meeting sections, play-back, committing a staging file | Worked | 9 |
| Second BA resumes on another machine | Pulling the staging file, the re-check, applying without the source | Worked | 8 |
| Two BAs push at once | Clashing SRC, Q and R numbers, push rejected, recovery | Recovered and renumbered; the clash was invisible to git for pages | 8 |
| A developer's `/intake` | A non-maintainer's run, the pull-request route | Stopped correctly at the proposal and put it on a branch | 9 |
| `/requirements` | The BA's product answers becoming proposals for the owner | 19 FRs, 12 pending; one commit | 6 |
| Sign-off, `/review`, `/backlog` | Pending proposals answered by the owner's sign-off; readiness | Seven questions answered, eleven rules added; found `/backlog` and `/review` disagreeing on "ready" | 8 |
| Rule change after sign-off, update, `/review kb` | Retiring a confirmed rule; an approved requirement changing | BR-004 retired for BR-019; requirement back to draft with four new proposals | 13 |

## The main findings

- **Upgrades:** the written steps would have reset the project's sync times and missed template text
  inside knowledge pages, profile edits and new columns.
- **Two BAs at once:** new pages with the same ID but different file names don't conflict in git, so
  only a check after the rebase finds them; `kb.py` didn't detect duplicate RAID or glossary IDs.
- **Teammates** were asked to make decisions they can't make before being told so; the branch route
  wasn't possible with the command's tools.
- **Proposals and sign-off:** no place on a question for a proposed answer and its rule text; parts
  of a question with no proposal were silently lost at sign-off; a sign-off let `/backlog` skip
  `/review`'s verdict.
- **Rule changes by the owner** fell between "contradiction" and "decision" in the pipeline.
- **Updating an approved requirement** had no rule for its status and sign-off.
- Many smaller gaps: resuming re-checked by date instead of by commit, deleting a committed staging
  file, dates when applying on a later day, one concrete suggestion per critic finding, a box for
  "take the critic's suggestion", staging files across a seeding run, and a date override for
  `kb.py`.

Still not tested: anything against a real Jira or Confluence site (`/sync`, `/kb-seed confluence`
or `jira`, `/backlog` creating and updating issues, `/review` of a Jira issue), and the real slash
commands with Claude Code's own permission prompts.
