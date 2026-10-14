# The project knowledge base: how the BA harness builds, grows and uses it

Design note, October 2026. Every project that adopts the BA harness gets a knowledge base. It
starts nearly empty at setup and grows every day from meeting notes, documents, conversations,
Jira tickets and comments, and Confluence pages. Every BA command reads it, and anyone who pulls
the repository can ask it questions. This note sets out the structure, the rules for adding to it,
how each source feeds it, how it is used, how teammates query it, and how to set up Obsidian if
the team wants it as a viewer.

An existing knowledge base from another project was studied as an example only. It is not part of the
harness. What it taught us is in the last section.

## Design principles

1. **Plain markdown in the project's BA repository.** No database, no required app, no MCP server
   for the knowledge base itself. Claude Code reads the files directly, GitHub and Azure DevOps
   render them, and Obsidian can open the folder as a vault.
2. **Nothing enters without a source and a person's yes.** Every fact cites where it came from. AI
   proposes; the BA accepts, edits or rejects each item before it is stored.
3. **One fact, one place.** Each rule, term, decision and question has a single home and a stable
   ID. Other pages link to it instead of repeating it.
4. **Contradictions are recorded, never overwritten.** A new statement that conflicts with an
   existing one becomes an open question or a decision waiting for an approver.
5. **Status is visible everywhere.** Readers, and every answer `/ask` gives, can tell an AI draft
   from a BA-confirmed fact from a stakeholder-approved decision.
6. **Readable by anyone.** Pages are written for people who know the business, not the code. A
   developer, tester or new BA should understand a page without asking.

## Structure

```text
knowledge/
├── README.md               how to read and contribute (for people)
├── index.md                catalogue: every page, one line each; the starting point for every query
├── log.md                  append-only: one line per change, with the source and who approved it
├── glossary.md             terms: one definition each, plus the words people actually use
├── stakeholders.md         who is who, what they own, what they can decide (RACI)
├── business-rules.md       register: BR-### → the page that explains the rule in context
├── decisions.md            DEC-###: what was decided, by whom, when, from which source
├── open-questions.md       Q-###: what is unclear, why it matters, owner, status
├── raid.md                 risks, assumptions, issues, dependencies
├── domains/<area>/         one page per capability or behaviour, grouped by business area
├── processes/              as-is and to-be process maps (Mermaid inside the markdown)
├── entities/               roles, systems, data objects and integrations
├── sources/                SRC-###: one record per processed input (meeting, document, ticket batch)
├── assets/                 images and diagrams referenced from pages
├── _staging/               proposals from /intake and /sync waiting for the BA
└── _meta/
    ├── conventions.md      the rules in this note, as the project's own copy
    ├── templates/          page templates (capability, entity, process, source record)
    └── sync.json           last-sync timestamps for Jira and Confluence
inbox/                      raw files dropped by the BA (gitignored; never published)
```

### Page types

| Type | Holds | Template sections |
|---|---|---|
| Capability (`domains/`) | How one part of the product works or must work | Purpose; who and when; what the user sees; inputs; rules applied (BR-ids, in evaluation order); outcomes; failure and blocked paths; interactions with other capabilities; open items; sources |
| Entity (`entities/`) | A role, system, data object or integration | What it is; attributes or permissions; lifecycle (states and transitions); where it appears; sources |
| Process (`processes/`) | An as-is or to-be workflow | Trigger; actors; steps (Mermaid diagram plus numbered list); variations; pain points (as-is) or changes (to-be); sources |
| Source record (`sources/`) | One processed input | Type, date, participants (roles, not personal data unless needed), summary, what was extracted and where it went, location of the original |
| Registers (root files) | Rules, decisions, questions, terms, stakeholders, RAID | One table row or section per item, each with an ID, status and source |

### Frontmatter

Every page carries a short header, so tools and people can filter it:

```yaml
---
id: CAP-012                # stable; never reused
type: capability           # capability | entity | process | source | register
title: Raising a job card
area: workshop
status: confirmed          # draft | confirmed | approved | superseded
owner: <BA name or role>
sources: [SRC-031, SRC-044, PROJ-1234]
updated: 2026-10-14
approved_by:               # name and date, only when status is approved
superseded_by:             # ID of the replacement, only when superseded
---
```

### IDs and links

- Prefixes: `CAP-`, `ENT-`, `PROC-`, `SRC-`, `BR-`, `DEC-`, `Q-`, `R-` (risk), `A-` (assumption).
  Numbers never get reused; a retired item is marked superseded.
- Links are standard relative markdown links (`[Raising a job card](../domains/workshop/raising-a-job-card.md)`),
  so they work in GitHub, Azure DevOps, Obsidian and Confluence exports.
- Inside a page, a claim cites its source inline when it isn't obvious: `(SRC-031)`, `(PROJ-1234)`,
  `(DEC-007)`. An unsourced statement is written as `[assumption]` or moved to open questions.

## Statuses

| Status | Meaning | Set by | How `/ask` treats it |
|---|---|---|---|
| `draft` | Extracted by AI, not yet checked | `/intake`, `/sync`, `/kb-seed` | Used, but labelled "unconfirmed" |
| `confirmed` | The BA checked it against its source | The BA, when accepting a proposal | Used normally |
| `approved` | A named stakeholder agreed; recorded in `decisions.md` | The BA, recording the approval | Used, shown as approved |
| `superseded` | Replaced; kept for history | The BA | Never used in answers |

Drafts older than 30 days show up in `/review kb` so they get confirmed or removed.

## The rules for adding knowledge

These go into `knowledge/_meta/conventions.md` at setup, and every command that writes to the
knowledge base follows them.

1. **Propose, then write.** Commands write only to `_staging/`. Pages, registers and the index
   change only after the BA accepts an item.
2. **Every item cites its source.** A quote and its location: file and paragraph, transcript
   timestamp, Jira key and comment, Confluence page and section.
3. **Search before adding.** Check the index, the glossary and the registers for an existing item.
   If one exists, propose an update or a link instead of a new entry.
4. **Conflicts become questions.** If a new statement contradicts a confirmed or approved item,
   propose an open question (or a decision for a named approver), and never overwrite.
5. **Authority matters.** A statement only becomes a decision if `stakeholders.md` says the
   speaker can decide that; otherwise it is recorded as their view, with a question to the owner.
6. **Strip personal data.** Store roles, not names, unless a name is needed (an approver, an owner).
   Redact patient, customer and other personal data from source records.
7. **Business language only.** No code paths, class names or table names in pages; put technical
   pointers in the source record if they matter.
8. **Every accepted change appends one line to `log.md`** with date, IDs touched, source and who
   approved it; `index.md` is updated in the same step.
9. **Never edit `superseded` items, and never delete.** Retire by superseding.
10. **Raw input stays out of git.** `inbox/` is gitignored; only the redacted source record is
    committed.

## Where knowledge comes from, and how it gets in

| Source | Command | What happens |
|---|---|---|
| Existing material at project start (charter, specs, slide decks, Confluence space, Jira epics) | `/kb-seed` | Reads everything named in the profile, drafts the first glossary, stakeholder map, capability list and open questions; all `draft` until the BA confirms. Run once, then occasionally |
| Meeting notes, transcripts, emails, documents | `/intake <file>` | File dropped in `inbox/` or pasted; extract, judge, stage, confirm (detailed below) |
| The BA's own conversations with Claude | `/intake` with no file | Stages what was learned or decided in the current session, using the conversation as the source |
| Jira tickets and comments | `/sync jira` | Reads issues in the project's scope updated since the last sync (JQL `updated >= <last sync>`), including comments and status changes; extracts answered questions, decisions, rule changes and new terms; stages them. Read-only towards Jira |
| Confluence pages | `/sync confluence` | Same for pages in the configured space(s) changed since the last sync |
| Stakeholder answers to open questions | `/intake` of the answer (email, comment, note) | Closes `Q-###` with the answer, updates the affected pages, records a decision when the person has authority |
| The product's current behaviour, derived from code (optional) | Dev harness, then `/intake` of its output | A developer or the Dev harness writes a behaviour description; the BA ingests it like any document, as `draft` "as-built" knowledge |

`/sync` records its timestamp in `_meta/sync.json` only after the BA has gone through the staging
file, so nothing is skipped. It reads at most 50 issues per run, one call at a time, to stay inside
Atlassian's rate limits.

### `/intake` in detail

1. **Read.** Markdown, text, PDF and images are read directly. Word, Excel and PowerPoint are saved
   as PDF first (version 1), or converted with a tool such as `markitdown` if the team installs one.
2. **Extract** candidate items, each with its quote and location: requirements, business rules,
   decisions, actions, questions, terms, risks, facts about stakeholders or systems.
3. **Judge** each item:

   | Check | Results |
   |---|---|
   | Against the knowledge base | New / confirms X / contradicts X / duplicate of X |
   | Clarity | Clear / vague (names the vague words) / incomplete |
   | Authority | Speaker can decide this / cannot / unknown |
   | Sensitivity | Clean / needs redaction (says what) |

4. **Stage** one proposal file in `_staging/`: every item with its verdict and the exact change it
   would make (new page, edit with a diff, new register row, open question, decision awaiting an
   approver, action with owner and date, or ignore). Optionally a short play-back message for the
   meeting's participants to confirm.
5. **Confirm.** The BA accepts, edits or rejects each item, in the chat or by editing the staging
   file.
6. **Store.** Accepted items are written as `confirmed` (or `approved` when a decision has its
   approver), the source record is created in `sources/`, `index.md` and `log.md` are updated, and
   the staging file is deleted.

## How the knowledge base is used

| Command | Uses it to |
|---|---|
| `/ask` | Answer questions with citations and statuses; say plainly when the knowledge base doesn't know |
| `/requirements` | Ground new requirements in existing rules, roles and terms; flag conflicts before writing |
| `/review` | Check stories and documents against business rules and the glossary; `/review kb` lints the knowledge base itself |
| `/backlog` | Put glossary terms and rule IDs into Jira stories so developers see the source |
| `/change` | Find affected capabilities, rules and processes through IDs and links |
| `/elicit` | Turn open questions into interview and workshop agendas per stakeholder |
| `/uat` | Build business scenarios from the capability pages' rules and failure paths |
| `/handoff` | Attach the relevant pages and rule IDs to the package the Dev harness picks up |

The Dev and QA harnesses can read the same folder when a project wants that, by adding the BA
repository's `knowledge/` path to their `additionalDirectories` setting. They read; they don't write.

## Asking questions: the BA and everyone else

Anyone who clones the BA repository can open Claude Code in it and run `/ask`.

- `/ask` uses only the files in the repository, so it works without Atlassian access. Jira and
  Confluence are searched too only when the person has signed in.
- It is read-only by construction: its `allowed-tools` are Read, Grep and Glob, so a teammate can't
  change the knowledge base by asking.
- Every answer cites pages and IDs and shows their status. If the only support is a draft, it says
  "unconfirmed". If the knowledge base has nothing, it says so and drafts an open question the
  person can send to the BA (as text, or as a Jira comment if they choose).
- The repository's `CLAUDE.md` tells any Claude session to start from `knowledge/index.md`, and an
  `AGENTS.md` says the same for other assistants (Copilot, Cursor, Codex), so plain questions work
  even without the `/ask` command.

How teammates contribute without breaking the rules: they drop material in their own `inbox/` and
run `/intake`, which stages it, then open a pull request with the staging file; the BA accepts or
rejects it. Or they send it to the BA, who runs the intake.

People who will never clone a repository (stakeholders, managers) read the published Confluence
copy. `/publish` pushes confirmed and approved pages there, one way; drafts are never published.

## Growth and upkeep

- **`/review kb`**, run weekly: broken links, orphan pages (not in the index), drafts older than 30
  days, open questions past their due date, contradictions between pages, registers out of step
  with pages.
- **The index** is rewritten by the same step that changes pages, never by hand.
- **Size.** Reading `index.md` and searching files works up to a few hundred pages. When the index
  no longer fits comfortably in one read, or answers miss pages because people use different words,
  add a local search server such as qmd (optional, an MCP server with keyword and semantic search).
  Until then nothing extra is installed.

## Obsidian: optional, with a standard setup

The knowledge base does not need Obsidian. Teams that want graph view, backlinks and a nicer editor
can open `knowledge/` as a vault. Obsidian has been free for work use since February 2025.

The harness would ship a small `knowledge/.obsidian/app.json` so links stay compatible with
everything else:

| Setting (Settings → Files and links) | Value | Why |
|---|---|---|
| Use [[Wikilinks]] | Off | Standard markdown links render in GitHub, Azure DevOps and Confluence exports |
| New link format | Relative path to file | Links keep working wherever the folder is opened |
| Automatically update internal links | On | Renaming a page fixes its links |
| Default location for new attachments | `assets/` | One place for images |
| Excluded files | `_staging/`, `_meta/` | Proposals and harness files stay out of search and the graph |

Other recommendations:

- Commit `app.json`. Gitignore `workspace.json`, `workspace-mobile.json` and `.obsidian/cache`.
- Useful core plugins: Backlinks, Graph view, Properties (shows the frontmatter), Templates (pointed
  at `_meta/templates/`).
- Dataview (community plugin) is optional; it can list pages by status or owner.
- For sharing, use git, with the Obsidian Git plugin if people prefer not to use the command line.
  Obsidian Sync isn't recommended: it has no review step and the agents can't see it.
- BAs should still add knowledge through `/intake`. Editing a page by hand in Obsidian is fine for
  typos and wording, but the change should still get a `log.md` line.

The exact `app.json` keys will be checked against the current Obsidian version when the harness is
built.

Open Knowledge (`okn`) is a different kind of tool that could sit alongside this later: it adds
link and structure checks, a read-only MCP server and a static published site. Note 07 evaluates
it; the knowledge base's frontmatter is kept compatible with its format (OKF) so adopting it later
is cheap.

## What the example knowledge base taught us

That existing knowledge base was a useful reference, not a component.

- **Its source half** (`knowledge-base/`, 81 pages, 985 numbered rules, 83 open questions): a fixed
  page template, numbered rules, an explicit open-questions register and inline "unresolved"
  markers. These make a large knowledge base navigable and honest. The capability template above
  follows it.
- **Its Obsidian half** (`brain/`, built with the open-source `obsidian-wiki` tool, an
  implementation of Andrej Karpathy's "LLM Wiki" idea): the raw inbox, staging area, index, log and
  lifecycle statuses. These are the ingest pattern above.
- **What we left out:**
  - wikilinks, which break outside Obsidian;
  - fractional confidence scores, which suggest more precision than they carry;
  - the tool's 39 skills;
  - keeping two AI-written copies of the same knowledge, which drift apart.

## Sources

- Karpathy, "LLM Wiki": https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- obsidian-wiki: https://github.com/ar9av/obsidian-wiki (skills `llm-wiki`, `wiki-stage-commit`, `wiki-lint`)
- qmd: https://github.com/tobi/qmd
- Basic Memory: https://github.com/basicmachines-co/basic-memory
- Obsidian links: https://obsidian.md/help/links
- Obsidian free for work: https://obsidian.md/blog/free-for-work/
- Obsidian Git: https://github.com/Vinzent03/obsidian-git
- Claude Code settings (`additionalDirectories`): https://docs.anthropic.com/en/docs/claude-code/settings
- Rovo search and fetch: https://support.atlassian.com/atlassian-rovo-mcp-server/docs/using-rovo-search-and-fetch-in-the-atlassian-remote-mcp-server
- Stale history in agent memory: https://arxiv.org/pdf/2607.21962

Unverified: the exact Obsidian `app.json` key names, and the page count at which index and search
stop being enough (an estimate; no rigorous benchmark exists).
