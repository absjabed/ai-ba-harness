# Knowledge base conventions

How the knowledge base in every project BA repository is stored, kept in sync on everyone's machine,
and grown. The research behind it is `../research/06-knowledge-base.md`.

The files are stored by Obsidian's rules, so the folder opens as an Obsidian vault with nothing to
convert. They are also kept compatible with Open Knowledge Format (OKF), so `okn` can be pointed at
it later. Neither app is needed to use it: Claude Code, GitHub and any text editor read the same
files.

## Folder structure

```text
knowledge/
├── README.md                    how to read and contribute (for people)
├── index.md                     generated: every page, one line each; every query starts here
├── log.md                       append-only: one line per accepted change
├── glossary.md                  one section per term; synonyms listed with it
├── stakeholders.md              people and roles, what they own, what they can decide
├── raid.md                      risks (R-), assumptions (A-), issues (I-), dependencies (D-)
├── business-rules.md            generated register: BR-### → the page that holds the rule
├── decisions.md                 generated register of decisions/
├── open-questions.md            generated register of questions/
├── domains/<area>/              CAP-###-<slug>.md: how one capability works
├── entities/                    ENT-###-<slug>.md: roles, systems, data objects, integrations
├── processes/<area>/<slug>/     PROC-###-<slug>.md plus its diagrams (05-repo-layout.md)
├── decisions/                   DEC-###-<slug>.md: one file per decision
├── questions/                   Q-###-<slug>.md: one file per open question
├── sources/                     SRC-###-<yyyy-mm-dd>-<slug>.md: one record per processed input
├── assets/                      images that aren't diagrams
├── _staging/                    proposals waiting for the BA (excluded from search and the graph)
├── _meta/
│   ├── conventions.md           this note's rules, as the project's own copy
│   ├── templates/               page templates (also used by Obsidian's Templates plugin)
│   └── sync.json                last Jira and Confluence sync times
└── .obsidian/
    └── app.json                 shipped settings, used only if someone opens the vault in Obsidian
```

Decisions, questions and sources are **one file per item**. That gives each one a page that can be
linked and back-linked, and two BAs adding items on the same day don't edit the same file. The
registers at the root (`decisions.md`, `open-questions.md`, `business-rules.md`) and `index.md` are
**generated** from those files, never edited by hand.

## File rules (Obsidian and OKF compatible)

### File names

- Pattern: `<ID>-<slug>.md`, for example `CAP-012-raising-a-job-card.md`.
- Lowercase, hyphenated, ASCII. No spaces. None of the characters Obsidian rejects in links:
  `* " \ / < > : | ? # ^ [ ]`.
- Unique across the whole folder. The ID prefix guarantees that.

### Properties (frontmatter)

Every page starts with a flat YAML block that Obsidian shows as Properties. Only text, list, number,
checkbox and date values are used; there are no nested objects, which Obsidian can't display.

```yaml
---
type: capability            # required by OKF; one of the page types below
id: CAP-012
title: Raising a job card
area: workshop
status: confirmed           # draft | confirmed | approved | superseded
owner: Lead BA
sources:                    # IDs of source records, Jira keys, decision IDs
  - SRC-031
  - PROJ-1234
rules:                      # business rules defined on this page
  - BR-104
  - BR-105
aliases:                    # other names people use; Obsidian uses these to resolve links and search
  - opening a job card
tags:
  - workshop
created: 2026-10-14         # dates only (YYYY-MM-DD): valid in Obsidian and OKF
updated: 2026-10-14
approved_by:                # set only when status is approved
approved_on:
superseded_by:              # set only when status is superseded
---
```

Page types (`type`): `capability`, `entity`, `process`, `decision`, `question`, `source`,
`glossary`, `register`, `index`, `guide`.

### Links

- Standard markdown links with relative paths: `[Raising a job card](../workshop/CAP-012-raising-a-job-card.md)`.
  Obsidian follows them with the shipped settings, and GitHub, Azure DevOps and Confluence exports
  render them. No `[[wikilinks]]` and no `![[embeds]]`.
- Link to a section with `file.md#heading-text`.
- Cite inline with the ID in brackets, `(SRC-031)`, `(BR-104)`, `(DEC-007)`, linked the first time on a
  page.
- Images: `![What it shows](../../assets/CAP-012-approve-button.png)`.

### Callouts

Use the five callout types GitHub and Obsidian both render: `> [!NOTE]`, `> [!TIP]`,
`> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`. Two fixed uses:

```markdown
> [!CAUTION]
> **Unresolved:** a locked account sees the ordinary failed-sign-in message. See [Q-014](../../questions/Q-014-locked-account-message.md).

> [!NOTE]
> **Assumption:** a job card is always raised by the transport manager. Not yet confirmed (A-006).
```

### Shipped Obsidian settings

`knowledge/.obsidian/app.json` (keys to be checked against the current Obsidian version at build):

| Setting | Value |
|---|---|
| Use [[Wikilinks]] | off |
| New link format | relative path to file |
| Automatically update internal links | on |
| Default location for new attachments | `assets/` |
| Excluded files | `_staging/`, `_meta/sync.json` |
| Template folder location (Templates core plugin) | `_meta/templates` |

Committed: `.obsidian/app.json` and `.obsidian/core-plugins.json`. Gitignored:
`.obsidian/workspace*.json`, `.obsidian/cache`, `.trash/`.

## Statuses

| Status | Meaning | Who sets it |
|---|---|---|
| `draft` | Extracted by AI, not yet checked | `/kb-seed`, `/intake`, `/sync` |
| `confirmed` | The BA checked it against the source | The BA, when accepting a proposal |
| `approved` | A named stakeholder agreed; `approved_by` and `approved_on` are set and a decision file exists | The BA |
| `superseded` | Replaced; `superseded_by` points to the replacement | The BA |

`/ask` labels draft content "unconfirmed" and never uses superseded content.

## Rules for changing the knowledge base

1. Commands write proposals to `_staging/` only. Pages change only after the BA accepts an item.
2. Every item cites its source: a quote and its location (file and paragraph, transcript time, Jira
   key and comment, Confluence page and section).
3. Search before adding. An existing item gets an update or a link, never a duplicate.
4. A contradiction with a confirmed or approved item becomes an open question (or a decision
   awaiting a named approver). Nothing is overwritten.
5. A statement becomes a decision only if `stakeholders.md` says the speaker can decide it.
6. Personal data is removed: roles, not names, unless a name is needed (owner, approver).
7. Business language only; technical pointers go in the source record.
8. Each accepted change appends one line to `log.md` and regenerates `index.md` and the registers.
9. Nothing is deleted. Retire an item by superseding it.
10. Raw input never enters git; only the redacted source record does.

`log.md` line format (fixed, so it can be searched):

```text
2026-10-14 | INTAKE | SRC-031 | +CAP-012 ~CAP-007 +Q-014 +DEC-007 | accepted by Lead BA
2026-10-15 | SYNC   | jira 2026-10-14T09:00+01:00..2026-10-15T08:55+01:00 | ~CAP-012 Q-014 answered | accepted by Lead BA
```

## Keeping every copy up to date

Team members clone the project BA repository once. After that it updates itself.

**When anyone opens Claude Code or Codex in the repository**, a `SessionStart` hook
(`tools/kb-sync.sh`) runs; OpenCode runs the same script at the start of each command:

1. `git fetch` from the shared remote.
2. If the working copy has no local changes and can fast-forward, it pulls (`git merge --ff-only`)
   and prints "Knowledge base updated: N new changes".
3. If there are local changes, or the branches have diverged, it changes nothing and prints what the
   person should do.

The hook needs `git` and `bash`. Git for Windows provides both, and anyone who cloned the repository
already has it. It can be switched off in `PROJECT-PROFILE.md` (`kb_auto_sync: off`).

**For people who read in Obsidian without opening Claude Code**, `SETUP.md` gives two optional ways:

- the Obsidian Git plugin with "Auto pull interval" set (for example every 30 minutes);
- a daily scheduled task (Windows Task Scheduler) running `git -C <repo> pull --ff-only`.

**When a BA writes**, every command that changes the knowledge base:

1. pulls first, so proposals are made against the latest copy;
2. after the BA accepts items, commits with a message such as `kb: intake SRC-031 workshop 2026-10-14`;
3. asks before pushing, because pushing shares it with everyone.

If two BAs change the same page on the same day, git reports a conflict as usual. Generated files
(`index.md`, the registers) never need hand-merging: take either side and `/review kb` regenerates
them.

## Growth checks

`/review kb` (weekly, or before a release) reports:

- broken links and pages missing from `index.md`;
- drafts older than 30 days;
- open questions past their due date;
- contradictions between pages;
- rules referenced in Jira or requirements that don't exist;
- files that break the naming or property rules.

When `index.md` no longer fits comfortably in one read (roughly 300 or more pages), or answers miss
pages because people use different words, add a local search server (qmd, or `okn` once it is
proven on Windows). Until then nothing extra is installed.
