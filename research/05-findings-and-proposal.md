# AI BA Harness: findings and proposal

Written from the point of view of a principal BA designing AI-assisted BA work. It draws on the four
research notes in this folder (01 to 04). Nothing has been built, and the Dev and QA harnesses were
not changed. This document is for deciding what to build.

## What the research says, in eight points

1. **AI helps most with the paperwork of BA work, and least with the people side.** Meeting
   summaries, story and acceptance-criteria drafts, glossary and rule extraction, gap and ambiguity
   detection, trace links, change-impact candidates, release notes and UAT scenarios all suit AI
   well. Running workshops, stakeholder politics, prioritisation calls, approvals and sign-off do
   not (01).
2. **Context decides quality.** The one industrial pilot with numbers (Thoughtworks, about 20% less
   analysis time) found output only became useful once the agent had reusable domain context. A
   harness is mostly a way of keeping that context and loading it every time (01, 03).
3. **The known failure modes are specific:** invented systems and rule values, acceptance criteria
   that break unwritten policy, contradictions between runs, missed edge cases, duplicate or
   excessive tickets, and confidential data in the wrong tool (01).
4. **Every serious tool uses propose, review, then write.** Rovo, Confluence's "Create Jira work
   items", Atlassian's own Claude skills and CCPM all show a per-item preview and wait for
   confirmation before touching the tracker (02, 03).
5. **Nobody catches duplicates reliably.** Jira's pre-save duplicate check is still beta, and Rovo's
   triage flags duplicates only after creation. The harness has to search before it creates (02,
   03).
6. **Quality checks work best in two layers:** deterministic rules first (INVEST, EARS, ISO 29148,
   AQUSA-style structure), then an LLM review. LLMs alone have high recall but hallucinate and vary
   between runs (01).
7. **The Atlassian MCP server covers what a BA needs** (search, create, edit, link, transition,
   comment, Confluence pages). It has three constraints: no bulk create, custom required fields, and
   per-site rate limits. Calls run as the signed-in user and are audited (02).
8. **The Dev harness already owns per-feature specs (`/ba`, `/qa`).** The BA harness should work at
   project and epic level and hand over through Jira, which the Dev harness's `/ba` and the QA
   harness's issue-key rule already read (04).

## Proposed shape

### Who it is for and where it lives

One BA (or a small BA team) on one project. A small git repository per project, the "BA workspace",
holds the project knowledge and the harness files. Jira and Confluence remain where stakeholders
see the work. The repository is the BA's working record and audit trail, and pages and tickets are
published from it.

### Structure (QA harness pattern)

```text
ai-ba-harness/                       (template; copied per project)
├── PROJECT-PROFILE.md               the one file a BA fills in
├── agents/                          vendor-neutral agent definitions (plain markdown)
├── .claude/commands/                thin wrappers pointing at agents/
├── .claude/settings.json            Atlassian write tools set to "ask"
├── .mcp.json                        Atlassian Rovo MCP (OAuth, no secrets)
├── knowledge/                       the project's living knowledge base (see note 06)
│   ├── index.md                     catalogue every query starts from
│   ├── log.md                       append-only record of what changed and why
│   ├── glossary.md
│   ├── stakeholders.md              register + RACI + who approves what
│   ├── business-rules.md            BR-### rules, each with a source
│   ├── decisions.md                 decision log with the approver's name
│   ├── open-questions.md            Q-### with owner and due date
│   ├── raid.md                      risks, assumptions, issues, dependencies
│   ├── domains/<area>/              capability pages: how each part of the product works
│   ├── processes/                   as-is / to-be maps (Mermaid in git; draw.io for Confluence)
│   ├── entities/                    roles, systems, data objects, integrations
│   ├── sources/                     SRC-###: redacted record of every processed input
│   ├── _staging/                    /intake and /sync proposals waiting for the BA's yes
│   └── _meta/                       conventions, page templates, last-sync timestamps
├── requirements/<epic-slug>/        requirement docs: FR-/NFR- items, stories, acceptance criteria
├── trace/map.csv                    FR id ↔ story file ↔ Jira key ↔ Confluence page
├── changes/CR-###.md                change requests with impact analysis
├── inbox/                           raw notes, transcripts, documents (gitignored)
└── docs/index.html                  handbook for BAs
```

### Ground rules

1. **Read freely; write only after a yes.** All Jira and Confluence write tools are set to `ask` in
   `settings.json`, so Claude Code itself prompts. The agents also show a preview table first:
   accept, edit or decline per item, at most 15 items per batch.
2. **Search before creating.** Every proposed ticket is checked against existing issues (JQL on
   summary and key terms) and the trace map. Possible duplicates are offered as "link or update"
   instead of "create".
3. **Every claim has a source.** Requirements, rules and criteria cite a note file and line, a
   transcript timestamp, a ticket key or a page. Anything without a source is written as an
   assumption or an open question, never as fact.
4. **Ask a few good questions, and write the answers down.** One question at a time, multiple
   choice with a recommended answer, about five per session. Answers go into a dated clarifications
   section of the document.
5. **People own decisions.** Priorities, approvals, scope trade-offs and UAT sign-off are recorded
   with a named person. The harness drafts them and never makes them.
6. **Two-layer quality check.** Rule-based checks first (INVEST, Gherkin or EARS form, vague-word
   list, singular and verifiable), then a model review. The review is read-only and graded by
   severity. Fixes are applied only when the BA agrees.
7. **The knowledge base is plain files, read directly.** It lives in the BA repo, grows from day
   one through `/kb-seed`, `/intake` and `/sync`, and anyone who clones the repo can query it with a
   read-only `/ask`. No MCP server, vector database or Obsidian is required; `index.md` plus search
   is enough up to a few hundred pages, and Obsidian is an optional viewer with a shipped config
   (note 06).
8. **Sensitive input stays local.** `inbox/` is gitignored, and the intake step offers to redact
   names and personal data before anything is stored or published.
9. **Scale to the job.** A one-line change to a story doesn't go through the full epic flow.

### Commands, by phase

| Phase | Command | What it does | Writes outside the repo? |
|---|---|---|---|
| 1 (MVP) | `/setup` | Interview → `PROJECT-PROFILE.md`; checks the Atlassian connection; reads the Jira project's issue types and required fields | No |
| 1 | `/kb-seed` | Builds the first draft of the knowledge base from existing material named in the profile (charter, specs, Confluence space, Jira epics): glossary, stakeholders, capability list, open questions; all draft until the BA confirms | No |
| 1 | `/intake <file or text>` | Extracts requirements, rules, decisions, actions, questions and terms from notes, transcripts or documents, each with its source; judges each against the knowledge base (new, confirms, contradicts, duplicate), for clarity, authority and sensitive data; writes a staging proposal; promotes only what the BA accepts; drafts a play-back message to participants | No |
| 1 | `/requirements <epic or topic>` | Clarification loop, then a requirement doc with FR/NFR items and stories with Given/When/Then criteria | No |
| 1 | `/review <doc, Jira key or kb>` | Read-only quality report: INVEST, criteria form, ambiguity, gaps, conflicts with rules or glossary, duplicates. `/review kb` lints the knowledge base: broken links, orphan pages, stale drafts, contradictions | No |
| 1 | `/backlog <requirement doc>` | Splits it into an epic and stories, searches for duplicates, shows the preview table, creates on approval, records keys in `trace/map.csv`, links them back | Jira (after approval) |
| 1 | `/sync jira` · `/sync confluence` | Reads tickets, comments and pages changed since the last sync (read-only), extracts answered questions, decisions, rule changes and new terms, and stages them like `/intake` | No |
| 1 | `/ask <question>` | Answers from the knowledge sources in the profile (and optionally Jira and Confluence), citing each source with its status; says so when the knowledge base doesn't know, and offers to log an open question | No |
| 2 | `/publish <doc>` | Creates or updates the Confluence page, showing the change first | Confluence (after approval) |
| 2 | `/change <description>` | Change request with impact analysis through the trace map and Jira links; proposed ticket edits | Jira (after approval) |
| 2 | `/status` | Requirements health: open questions, unapproved docs, stories not ready, open change requests; optional Confluence publish | Optional |
| 2 | `/handoff <epic>` | Readiness check (definition of ready) with a pass, concerns or fail verdict, before the Dev harness picks it up | No |
| 3 | `/elicit <stakeholder or topic>` | Interview or workshop prep: agenda and question sets per stakeholder | No |
| 3 | `/process <name>` | As-is and to-be process maps from notes (Mermaid, plus draw.io or BPMN for Confluence) | Optional |
| 3 | `/uat <epic or fix version>` | UAT scenarios from acceptance criteria and a sign-off checklist a person completes | Optional |
| 3 | `/release-notes <fix version>` | Business-facing release notes from Jira | Optional |

The MVP closes two loops. One runs from notes, documents, conversations and Jira activity into a
confirmed knowledge base. The other runs from that knowledge to reviewed requirements and a clean
Jira backlog. Together they cover the highest-value, highest-frequency work and exercise every
safety rule above.

### How it connects to the other two harnesses

```text
BA harness  ── epics + stories in Jira (with acceptance criteria, fix version) ──► Dev harness /ba <key>
            ── story keys ───────────────────────────────────────────────────────► QA harness test plans
            ◄── defect summaries (QA) and deploy notes (Dev) ── /uat, /release-notes
```

No harness edits another's files. Jira is the contract.

## Decisions needed before building

| # | Decision | Options | My recommendation |
|---|---|---|---|
| 1 | Tracker and wiki for version 1 | Jira + Confluence Cloud only / also Data Center / also Azure DevOps | Cloud only (official server). Add others later behind the same commands |
| 2 | Where BA work lives | Separate BA repo per project / a `ba/` folder in the product repo / no repo, Jira and Confluence only | Separate BA repo: BA history stays out of code reviews, and BAs don't need the dev toolchain |
| 3 | Harness architecture | QA-harness pattern (profile + `agents/` + thin wrappers) / Dev-harness pattern (`.ai/` + `/init-project`) / Claude Code plugin | QA-harness pattern now; package as a plugin later if distribution becomes a chore |
| 4 | Requirement notation | User stories + Given/When/Then / EARS / both | Stories + Given/When/Then for the backlog, EARS for system rules and NFRs |
| 5 | Write approval granularity | Per item / per batch / both | Preview per item, approve per batch, cap 15, plus the `ask` permission prompt |
| 6 | Meeting inputs | Paste or export files / Fireflies or Otter MCP / Zoom MCP / Teams via Graph | Paste or export for version 1; add a transcript MCP when the team settles on a meeting tool |
| 7 | Diagrams | Mermaid only / draw.io / BPMN XML | Mermaid in git, draw.io for anything published to Confluence (Confluence Cloud doesn't render Mermaid without an app) |
| 8 | Reuse Atlassian's own skills | Use spec-to-backlog and the others as they are / borrow their steps into our agents | Borrow the steps; ours add project context, provenance, trace IDs and quality checks |
| 9 | MVP scope | The eight phase-1 commands / fewer / more | Eight, then real use on one project before phase 2. If eight is too many, `/kb-seed` and `/sync` can move to phase 2 |
| 10 | Data handling | Transcripts allowed / notes only; redaction on or off | `inbox/` gitignored, redaction offered at intake, confirm the org's AI-use policy covers meeting content |
| 11 | Where the knowledge base lives | A `knowledge/` folder in the BA repo / a separate repo / Confluence only | A `knowledge/` folder in the BA repo; Confluence as a one-way publishing target for people who don't use the repo (note 06) |
| 12 | Obsidian | Not used / optional viewer with a shipped config / required | Optional viewer: the harness ships `knowledge/.obsidian/app.json` (markdown links, relative paths) and instructions; nothing depends on it |
| 13 | Office documents at intake | Save as PDF / a converter (`markitdown`, pandoc) | Save as PDF in version 1, so nothing extra is installed |
| 14 | How teammates contribute | Send material to the BA / their own `/intake` plus a pull request with the staging file | Both: `/ask` is open to everyone and read-only; contributions arrive as staging files the BA accepts |

## Risks and how the design handles them

| Risk | Handling |
|---|---|
| Invented requirements or rule values | Source citations required; unsourced items become open questions |
| Ticket floods and duplicates | Search before create, batch cap of 15, per-item decline |
| Silent failures in v2 "execute" calls | Read back every created or edited item and compare |
| Rate limits (about 1,000 calls an hour per site on Standard) | Sequential writes, no parallel bursts, batch caps |
| Required custom fields block creation | `/setup` records each issue type's required fields in the profile |
| Confidential meeting content | Gitignored inbox, redaction step, approved tenant only |
| BAs without git or bash | No bash-dependent hooks; permissions-based approval; a handbook page; optional plain-folder mode |
| Model output varies between runs | Rule-based checks first; quality review can be run twice and compared |

## Suggested next step

Pick answers for the fourteen decisions (or accept the recommendations), then build phase 1 as a
template in this folder with a small worked example project, the same way the Dev harness has
FleetKeep. After that, try it on one real project before adding phase 2.

## Related issue spotted in passing

The Dev harness's `.mcp.json` pointed at Atlassian's v1 endpoint (`/v1/mcp/authv2`). That was fixed
separately in the Dev harness repo (commit `0af5190`, now `https://mcp.atlassian.com/v2/mcp`).
