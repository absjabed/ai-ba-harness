# Demo test of 0.4.2, and what 0.5.0 changed

On 2026-10-14 and 15 every command was run on a throwaway project, "FleetKeep Demo", created with
`scripts/new-project.sh`, with a local bare repository as its remote and an inspections workshop's
notes in `inbox/`. Atlassian was not connected.

## How it was run

The headless Claude CLI wasn't signed in, so each command ran as a separate sub-agent with a fresh
context. Each one read the demo repository's wrapper and command definition and followed them to the
letter, with the BA's answers given up front. Each reported what it did, the files and commits it
produced, and a log of every point where the definitions were unclear, contradictory, impossible or
forced a guess. After the first fixes, the updated harness was copied into the demo repository
(as the CHANGELOG's update steps describe) and the later commands ran against it.

| Run | Outcome | Points logged |
|---|---|---|
| `/setup`, offline | Profile, stakeholders and areas written and committed | 20 |
| `/intake` to staging | 15 items; a name and phone number redacted; the critic sub-agent found 14 real problems | 22 |
| Resume and apply | 10 pages, IDs, a source record, registers rebuilt by hand, committed | 32 |
| `/ask`, four questions | Cited answers; the write request refused; no broken links | 17 |
| `/requirements` | A requirement with 11 FRs and 5 stories; the critic turned the BA's product-behaviour answers into questions | 26 |
| `/review` | Not ready, 5 critical (blocked stories), 8 major, 6 minor; all accurate | 25 |
| `/backlog`, both modes | Stopped cleanly without Jira | 34 |
| `/improve-harness`, four runs | A profile setting, a local harness change, and a safety change it correctly refused to apply | 21 |

`tools/kb.py check`, run over the knowledge base the sub-agents had built by hand, found no broken
links or IDs. It did find that the agents' hand-written registers didn't match a deterministic
rebuild, and it showed that the tool itself didn't read inline YAML lists. Both were fixed.

## The main findings

- **Safety:** Jira writes through the Atlassian plugin's tool names weren't covered by the "ask"
  rules.
- **Approval:** new pages were written at apply time from text the BA hadn't seen.
- **Authority:** the BA's answers on product behaviour were either recorded as rules they couldn't
  decide or blocked their own stories. 0.5.0 makes them proposals that the owner's sign-off settles.
- **Bookkeeping:** the index and registers had no exact format and no tool.
- Many smaller gaps in ordering, statuses, IDs, redaction, resuming and git.

The CHANGELOG entry for 0.5.0 lists what changed. Not tested yet: anything against a real Jira or
Confluence site, the `/sync` command, and `/kb-seed`.
