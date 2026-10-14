# Command definitions (version 1)

Eight commands. Each definition says what the command is for, when to run it, what it needs, what
it reads and writes, the steps it follows, where it stops for approval, and when it refuses. The
canonical text of each command will live in `agents/<command>.md`; the file in `.claude/commands/`
only points at it.

Rules every command follows:

- **No writes outside the repository without a yes.** Jira and Confluence write tools are set to
  "ask" in `.claude/settings.json`, and commands show a preview first.
- **Knowledge changes go through `knowledge/_staging/`** and the BA's per-item acceptance
  (`03-knowledge-base-conventions.md`).
- **Nothing is invented.** A fact without a source becomes an open question or an `[assumption]`.
- **Pull before writing; commit after accepting; ask before pushing.**
- **Every command ends with a short report:** what it did, what is waiting for the BA, and the
  suggested next command.

Quick reference:

| Command | One line | Who | Writes to Jira or Confluence? |
|---|---|---|---|
| `/setup` | Configure this repository for the project | Lead BA, once | No |
| `/kb-seed` | Build the first knowledge base from existing material | BA, at the start | No |
| `/intake` | Turn notes, documents or a conversation into proposed knowledge | BA, daily | No |
| `/sync` | Turn new Jira and Confluence activity into proposed knowledge | BA, daily | No (reads only) |
| `/requirements` | Write a requirement document for an epic or topic | BA, per epic | No |
| `/review` | Check a requirement document, a Jira issue or the knowledge base | BA, before `/backlog`; weekly for `kb` | No |
| `/backlog` | Create the epic and stories in Jira from a reviewed requirement | BA, per epic | Yes, after approval |
| `/ask` | Answer a question from the knowledge base, with citations | Anyone | No |

---

## `/setup`

**Purpose.** Turn a fresh copy of the template into this project's BA repository.

**When.** Once, right after creating the repository from the template. Run again to change
settings; it shows the differences before writing.

**Arguments.** None.

**Needs.**
- A git clone with a shared remote.
- Claude Code signed in.
- The Atlassian server authenticated: `/mcp`, then sign in once in the browser.

**Reads.** `PROJECT-PROFILE.md` (template state); Jira through read tools.

**Steps.**
1. Interview, in short rounds:
   - **Project:** name and one-line purpose.
   - **Jira:** the project key or keys, and the JQL that defines "our scope" for `/sync`.
   - **Confluence:** whether it is used and, if so, which spaces.
   - **Stakeholders:** the main people, their roles and what each can decide.
   - **Conventions:** the release or fix-version convention, labels and components to apply.
   - **Existing material:** what `/kb-seed` should read.
   - **Options:** whether to use Obsidian and whether to sync automatically.
2. Read Jira metadata for each project and issue type: required fields, custom field IDs, available
   components and versions.
3. Write `PROJECT-PROFILE.md` and `knowledge/stakeholders.md` (status `draft`).
4. Create the knowledge skeleton if it is missing, and keep `.obsidian/app.json` if Obsidian is
   wanted.
5. Check that `inbox/` is gitignored and that the sync hook runs.
6. Show the changes, commit after a yes, ask before pushing.

**Writes.** `PROJECT-PROFILE.md`, `knowledge/stakeholders.md`, the skeleton files. Nothing outside
the repository.

**Refuses when.** The profile was already filled and the BA hasn't confirmed overwriting a section.
Atlassian isn't reachable: it finishes the local part and lists what is still missing.

**Report.** What was configured, what is still unknown, the next step (`/kb-seed`).

---

## `/kb-seed`

**Purpose.** Build the first draft of the knowledge base from material that already exists.

**When.** After `/setup`. Again later only when a large body of new material arrives (for example,
a predecessor project's documentation).

**Arguments.** Optional: a subset of the sources listed in the profile, for example
`/kb-seed confluence` or `/kb-seed inbox/charter.pdf`.

**Needs.** `/setup` done. The sources listed in the profile: files in `inbox/`, Confluence spaces or
pages, Jira epics by JQL.

**Reads.** Those sources (read-only), and the current `knowledge/`.

**Steps.**
1. List what it will read, with page and issue counts, and ask once before starting.
2. Process one source at a time, in batches (at most 20 Confluence pages or 50 Jira issues per
   batch).
3. Extract the following, each with a quote and its location:
   - glossary terms;
   - stakeholders and roles;
   - capabilities and their rules;
   - processes;
   - decisions;
   - open questions;
   - risks.
4. Write one staging file per source to `_staging/`, all items `draft`.
5. Hand over to the same acceptance step as `/intake`; accepted items are stored as `confirmed` or
   kept as `draft` at the BA's choice.

**Writes.** `knowledge/_staging/`, and after acceptance the knowledge pages, registers, index and
log.

**Refuses when.** A source is outside the scope set in the profile. More than 200 items would be
staged in one run: it stops and asks to split the work.

**Report.** Items staged per source, conflicts found, and the suggestion to work through the staging
files before anything else.

---

## `/intake`

**Purpose.** Turn new material into proposed knowledge, judged against what the knowledge base
already holds.

**When.** Whenever new material arrives: after a meeting, on receiving a document or email, when a
stakeholder answers a question. With no argument, at the end of a working session, to capture what
was learned in the conversation.

**Arguments.** A file in `inbox/`, a folder in `inbox/`, pasted text, or nothing (the current
conversation).

**Needs.** Nothing beyond the repository.
- Markdown, text, PDF and images are read directly.
- Word, Excel and PowerPoint are converted with `markitdown` when it is installed; otherwise the
  command asks the BA to save them as PDF.

**Reads.** The input, and the whole `knowledge/` (index first, then the relevant pages).

**Steps.**
1. Pull, then read and, if needed, convert the input. Conversions go to `inbox/.converted/`.
2. **Extract** candidate items, each with a quote and its location:
   - requirements and business rules;
   - decisions and actions (with owner and date);
   - questions and answers to existing questions;
   - terms, risks, and facts about stakeholders or systems.
3. **Judge** each item:
   - against the knowledge base: new, confirms X, contradicts X, or duplicate of X;
   - clarity: clear, vague (naming the vague words) or incomplete;
   - authority: whether the speaker can decide this, per `stakeholders.md`;
   - sensitivity: personal or confidential data to strip.
4. **Stage:** write `_staging/<yyyy-mm-dd>-<command>-<slug>.md` listing every item with its verdict and the exact
   change it would make. Optionally draft a play-back message for the meeting's participants.
5. **Confirm:** the BA accepts, edits or rejects each item, in the chat or by editing the staging
   file.
6. **Store:**
   - accepted items become pages or edits (`confirmed`, or `approved` where a decision has its
     approver);
   - answered questions are closed and contradictions become new questions;
   - a source record is written to `sources/`, and `index.md`, the registers and `log.md` are
     updated;
   - the staging file is deleted, and the change is committed. It asks before pushing.
7. **Clean up:** it lists the raw files and converted copies used, and asks whether to delete them
   from `inbox/`. The default is to keep them, and nothing is deleted without a yes.

**Writes.** `_staging/`, then knowledge pages, `sources/`, registers, index, log. Deletes from
`inbox/` only with permission.

**Refuses when.** The input can't be read or converted (it says why and how to fix it). An accepted
item would overwrite a confirmed or approved one: it becomes a question instead.

**Report.** Counts of accepted, edited and rejected items; questions opened and closed; decisions
awaiting an approver; the next suggested step.

---

## `/sync`

**Purpose.** Bring what happened in Jira (and Confluence, if used) since the last sync into the
knowledge base.

**When.** Daily, or before writing requirements for an area.

**Arguments.** `jira`, `confluence`, or nothing (both, as configured).

**Needs.** `/setup` done; Atlassian authenticated; the scope JQL and spaces in the profile.

**Reads.**
- Jira issues in scope updated since the last sync, with their comments and status changes.
- Confluence pages changed since the last sync, if Confluence is used.
- The knowledge base.

**Steps.**
1. Read the last sync time from `_meta/sync.json` and list what changed, at most 50 issues or 20
   pages per run, read one at a time.
2. Extract:
   - answers to open questions;
   - decisions recorded in comments;
   - rule or scope changes;
   - new terms;
   - status changes that matter, such as an epic cancelled or a story descoped.
3. Judge and stage exactly as `/intake` does, citing the issue key and comment.
4. After the BA has worked through the staging file, update `_meta/sync.json`. If the run stopped
   early, the time stays where it was, so nothing is skipped.

**Writes.** The same as `/intake`. Nothing in Jira or Confluence.

**Refuses when.** Atlassian isn't authenticated or the scope isn't set (it says how to fix it). The
rate limit is hit: it stops cleanly and the next run continues.

**Report.** Issues and pages read, items staged, what remains for the next run.

---

## `/requirements`

**Purpose.** Write the requirement document for an epic or topic, grounded in the knowledge base.

**When.** When a new epic or significant change needs defining; before `/backlog`.

**Arguments.** An epic name, a topic, or an existing Jira epic key.

**Needs.** The knowledge base, with at least the relevant area seeded. The `templates/requirement.md`
template.

**Reads.** The knowledge base: capabilities, rules, glossary, open questions and stakeholders for
the area. The Jira epic if a key is given. Related `requirements/` documents.

**Steps.**
1. Summarise what the knowledge base already says about the area, with citations, so the BA starts
   from the current state.
2. Clarification loop: one question at a time, multiple choice with a recommended answer, at most
   five per round. Prefer stated assumptions to questions for low-impact gaps. Answers are recorded
   in a dated Clarifications section.
3. Write `requirements/<epic-slug>/requirement.md` from the template:
   - goal and scope (in and out);
   - stakeholders;
   - functional requirements (`FR-001`) and non-functional requirements (`NFR-001`, in EARS form);
   - user stories with Given/When/Then acceptance criteria;
   - affected rules (`BR-` IDs);
   - assumptions, open questions and success measures.
4. Flag every conflict with existing rules or terms inline, and open a question for each.
5. Propose new knowledge (terms, rules, decisions) through staging, as `/intake` does.

**Writes.** `requirements/<epic-slug>/requirement.md` (status `draft`); `_staging/` for any knowledge
changes.

**Refuses when.** It is asked to state a rule or value with no source, and the BA won't supply one
(that item stays an open question).

**Report.** The document path, open questions, conflicts, and the next step (`/review`).

---

## `/review`

**Purpose.** A read-only quality report.

**When.**
- On a requirement document before `/backlog`.
- On a Jira issue someone else wrote.
- Weekly on the knowledge base (`/review kb`).

**Arguments.** A requirement document path, a Jira issue key, or `kb`.

**Needs.** The knowledge base. Atlassian for Jira keys.

**Reads.** The target and the knowledge base.

**Steps (documents and issues).**
1. Run the rule-based checks first:
   - every story has the As a / I want / so that form and at least two Given/When/Then scenarios;
   - each requirement is singular and verifiable;
   - the vague-word list (fast, easy, etc., as appropriate);
   - IDs are present and unique.
2. Then the judgement checks:
   - INVEST for each story;
   - conflicts with business rules and glossary;
   - gaps (error paths, permissions, empty states);
   - duplicates of existing Jira issues (JQL search);
   - readiness against the definition of ready.
3. Write `requirements/<epic-slug>/review.md`: findings graded critical, major, minor; a ready or
   not-ready verdict; suggested fixes. Fixes are applied only when the BA asks.

**Steps (`kb`).** The growth checks in `03-knowledge-base-conventions.md`, then regenerate `index.md`
and the registers.

**Writes.** `review.md`; for `kb`, the generated index and registers only.

**Report.** Counts by severity, the verdict, the top fixes.

---

## `/backlog`

**Purpose.** Create the epic and its stories in Jira from a reviewed requirement document, without
duplicates.

**When.** After `/review` gives the document a ready verdict, or the BA accepts its remaining
findings.

**Arguments.** The requirement document path.

**Needs.** Atlassian authenticated; the Jira field metadata from `/setup`; the Jira templates
(`04-jira-templates.md`).

**Reads.** The requirement document, its review, `trace/map.csv`, and Jira (duplicate search).

**Steps.**
1. Check that the review verdict is ready, or that the BA has accepted the open findings.
2. Build the issues from the templates: one epic, then a story per user story, with fields filled
   from the profile (components, labels, fix version).
3. For each issue, search Jira for likely duplicates (summary terms, labels, epic). Show possible
   matches and offer link, update or create.
4. Show the preview table: type, summary, parent, key fields and duplicate verdict, with an accept,
   edit or decline choice per item. At most 15 items per batch.
5. On a yes, create in order (epic first, then its children). Read each created issue back to confirm
   the fields stuck, and link each issue back to the requirement document.
6. Update `trace/map.csv` and the document's story table with the new keys. Commit, and ask before
   pushing.

**Writes.** Jira issues (after approval), `trace/map.csv`, the requirement document's key column.

**Refuses when.**
- A story has open blocking questions.
- A required Jira field has no value.
- A batch would exceed 15 items without the BA splitting it.

**Report.** Created keys with links, items skipped and why, duplicates linked instead of created.

---

## `/ask`

**Purpose.** Answer a question from the project's knowledge, with citations.

**When.** Anytime, by anyone with a clone: BAs, developers, testers, product owners.

**Arguments.** The question.

**Needs.** The repository. Atlassian is optional: without it, only local knowledge is used.

**Reads.**
- `knowledge/`: the index first, then search, then the pages.
- `requirements/`.
- Optionally, Jira and Confluence search if the person is signed in.

**Tools.** Read, Grep, Glob, and Atlassian read and search tools only. It cannot write anything.

**Steps.**
1. Read `index.md`, then search the question's terms and their glossary synonyms (`aliases`).
2. Read the relevant pages and answer, citing every claim with page and ID.
3. Show each source's status: draft content is labelled "unconfirmed", and superseded content is
   never used.
4. If the knowledge base doesn't answer it, say so plainly, and draft an open question the person can
   send to the BA. Never fill the gap from general knowledge.

**Writes.** Nothing.

**Report.** The answer and its citations.
