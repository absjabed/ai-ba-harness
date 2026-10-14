# About this example

A complete, filled-in project BA repository, as it would look about a month after `/setup`. The
project is **FleetKeep** by **Northwind Systems**, the same fictional product used as the worked
example of the AI Dev Harness. Product facts come from that example; the stakeholders, meetings,
Jira comments and keys (FK-1188 to FK-1305) are invented, and so are the two names in
`knowledge/stakeholders.md`.

## What it shows

| What | Where |
|---|---|
| A filled profile: Jira project FK, scope JQL, issue types, required fields, five areas, settings | [`PROJECT-PROFILE.md`](PROJECT-PROFILE.md) |
| 21 knowledge pages that follow the conventions: capabilities with numbered rules, entities with lifecycles, a process with a Mermaid flowchart, decisions, questions and source records | [`knowledge/index.md`](knowledge/index.md) |
| Every status: mostly `confirmed`, two `draft`, an `approved` capability with its decision, and a `superseded` page pointing at its replacement | CAP-003 and CAP-004 in the index |
| Callouts: unresolved behaviour linking a question, an assumption linking the RAID log, legal weight, common traps | [CAP-001](knowledge/domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md), [CAP-006](knowledge/domains/vehicles/CAP-006-authorising-return-to-service.md) |
| Authority at work: a decision recorded second-hand stays `confirmed` until its owner confirms it | [DEC-002](knowledge/decisions/DEC-002-escalated-defects-top-of-workshop-queue.md) |
| The generated files, rebuilt from the pages' properties | [`business-rules.md`](knowledge/business-rules.md), [`decisions.md`](knowledge/decisions.md), [`open-questions.md`](knowledge/open-questions.md) |
| One log line per accepted change, from `/setup` to the last `/intake` | [`knowledge/log.md`](knowledge/log.md) |
| A proposal still waiting for the BA | [`knowledge/_staging/2026-10-14-intake-defect-triage-call.md`](knowledge/_staging/2026-10-14-intake-defect-triage-call.md) |
| A requirement grounded in the knowledge base, its review, and the trace to Jira | [`requirements/defect-escalation-to-workshop/`](requirements/defect-escalation-to-workshop/requirement.md), [`trace/map.csv`](trace/map.csv) |

## Where to start reading

1. **[`knowledge/index.md`](knowledge/index.md).** Every page in one list. Open CAP-004, then the
   superseded CAP-003 beside it.
2. **[The staging file](knowledge/_staging/2026-10-14-intake-defect-triage-call.md).** It is
   deliberately left pending, with every box unticked, to show what `/intake` proposes before the BA
   decides. Its eight items cover each verdict: new, confirms, contradicts (which becomes a question,
   because the speaker can't decide), answers an open question, and duplicate. Read its `Critic`
   section first: the critic added a missed action (item 8), fixed items 1 and 2, and left one point
   for the BA to check (item 1). A BA would decide it by
   ticking boxes, or by running `/intake knowledge/_staging/2026-10-14-intake-defect-triage-call.md`
   to resume it.
3. **[The requirement](requirements/defect-escalation-to-workshop/requirement.md)** and
   **[its review](requirements/defect-escalation-to-workshop/review.md).** The "Current state"
   section cites the knowledge base; the review is ready with four minor findings; `/backlog` created
   epic FK-1301 and stories FK-1302 to FK-1305.

## The story so far

| Date | Command | What happened |
|---|---|---|
| 2026-09-15 | `/setup` | Profile, stakeholders and areas |
| 2026-09-17 | `/intake` | Discovery workshop (SRC-001): the first glossary, capabilities, entities, process and questions |
| 2026-09-24 | `/intake` | Regulator guidance summary (SRC-002) |
| 2026-10-06 | `/sync jira` | Jira activity (SRC-003): Q-001 answered, CAP-003 superseded by CAP-004, two decisions |
| 2026-10-09 | `/requirements`, then `/intake` | Requirement drafted; the working session (SRC-004) opened Q-004 |
| 2026-10-12 | `/review` | Verdict: ready |
| 2026-10-13 | `/backlog` | Epic and four stories created in Jira; keys written back |
| 2026-10-14 | `/intake` | Triage call staged, waiting for the BA |

`inbox/` holds only `.gitkeep`: raw notes and documents are never committed, and the source records
summarise them instead. As in any project copy, the command files, agents and templates are the
harness's own, unchanged.
