---
type: guide
id: GUIDE-conventions
title: Knowledge base conventions
status: approved
---

# Knowledge base conventions

The rules every harness command follows when it reads or changes this knowledge base. People
editing by hand follow them too. The files are stored by Obsidian's rules and stay compatible with
Open Knowledge Format, so the folder opens as an Obsidian vault and works with OKF tools, while
Claude Code, GitHub and any text editor read it as plain markdown.

## 1. Folders

| Folder or file | Holds | Edited by |
|---|---|---|
| `index.md` | Every page, one line each, grouped by type and area | Generated; never by hand |
| `log.md` | One line per accepted change | Appended by commands |
| `glossary.md` | One section per term | Commands, after acceptance |
| `stakeholders.md` | People and roles, what they own, what they can decide | Commands, after acceptance |
| `raid.md` | Risks `R-`, assumptions `A-`, issues `I-`, dependencies `D-`, actions `ACT-` | Commands, after acceptance |
| `business-rules.md` | Register: every `BR-` with the page that defines it | Generated |
| `decisions.md` | Register of `decisions/` | Generated |
| `open-questions.md` | Register of `questions/` | Generated |
| `domains/<area>/` | `CAP-###-<slug>.md`: how one capability works | Commands, after acceptance |
| `entities/` | `ENT-###-<slug>.md`: roles, systems, data objects, integrations | Commands, after acceptance |
| `processes/<area>/<slug>/` | `PROC-###-<slug>.md` and its diagrams | Commands, after acceptance |
| `decisions/` | `DEC-###-<slug>.md`, one per decision | Commands, after acceptance |
| `questions/` | `Q-###-<slug>.md`, one per question | Commands, after acceptance |
| `sources/` | `SRC-###-<yyyy-mm-dd>-<slug>.md`, one per processed input | Commands, after acceptance |
| `assets/` | Images that aren't diagrams (`<page-id>-<what>.png`), and draw.io sources with their SVG for pages outside `processes/` (`<page-id>-<kind>.drawio`) | Anyone |
| `_staging/` | Proposals waiting for the BA | Commands |
| `_meta/templates/` | Page templates | The harness |
| `_meta/sync.json` | Last Jira and Confluence sync times | `/sync` |

`<area>` is one of the areas in `PROJECT-PROFILE.md` section 4.

## 2. IDs

| Prefix | For | Where it lives |
|---|---|---|
| `CAP-` | Capability page | `domains/` |
| `ENT-` | Entity page | `entities/` |
| `PROC-` | Process page | `processes/` |
| `DEC-` | Decision | `decisions/` |
| `Q-` | Open question | `questions/` |
| `SRC-` | Source record | `sources/` |
| `BR-` | Business rule | Defined inside a capability or process page, listed in its `rules` property |
| `R-` `A-` `I-` `D-` | Risk, assumption, issue, dependency | `raid.md` |
| `ACT-` | Action, with owner, due date and status (`open`, `done`, `dropped`) | `raid.md`, Actions table |
| `T-` | Glossary term | `glossary.md` |
| `REQ-` | Requirement document, `REQ-<epic-slug>` | `requirements/<epic-slug>/requirement.md` |
| `REVIEW-` | Review report, `REVIEW-<epic-slug>` | `requirements/<epic-slug>/review.md` |
| `FR-` `NFR-` `ST-` `AC-` | Functional and non-functional requirements, stories, acceptance criteria | Inside a requirement document; unique within it |

- Numbers have three digits and grow without gaps: the next ID is the highest existing number for
  that prefix plus one. Look at both the files and the registers before choosing.
- An ID is never reused, even after its item is superseded.
- IDs in staging files are provisional (`CAP-new-1`). The real number is given when the item is
  accepted.

## 3. File names

`<ID>-<slug>.md`: lowercase, hyphenated, ASCII, no spaces, at most about 60 characters. None of the
characters `* " \ / < > : | ? # ^ [ ]`. For example `CAP-012-raising-a-job-card.md`.

## 4. Properties

Every page starts with a flat YAML block, which Obsidian shows as Properties and OKF reads as the
document's metadata. Only text, lists, numbers, checkboxes and dates are used; no nested objects.
Dates are `YYYY-MM-DD`.

| Property | On | Value |
|---|---|---|
| `type` | All | `capability`, `entity`, `process`, `decision`, `question`, `source`, `glossary`, `register`, `index`, `guide`; and outside `knowledge/`, `requirement` and `review` |
| `id` | All | The page's ID |
| `title` | All | Human title |
| `status` | All except registers | `draft`, `confirmed`, `approved`, `superseded` |
| `area` | Capability, process | An area from the profile |
| `owner` | All except sources | A role, not a person's name |
| `sources` | All except sources | List of `SRC-` IDs, Jira keys and `DEC-` IDs |
| `rules` | Capability, process | List of `BR-` IDs defined on the page |
| `aliases` | Any | Other names people use for the subject |
| `tags` | Any | Lowercase, hyphenated; usually the area |
| `created` / `updated` | All | Dates |
| `approved_by` / `approved_on` | When `approved` | Role (and name only if needed), date |
| `superseded_by` | When `superseded` | ID of the replacement |

Generated files (`index.md`, the three registers) and `log.md` carry only `type`, `id` and `title`.
`/setup` fills `created` on the hand-maintained root pages (glossary, stakeholders, RAID).

Type-specific properties:

| Type | Adds |
|---|---|
| `question` | `state` (`open`, `answered`, `wontfix`), `asked_on`, `asked_of` (role), `due`, `answered_on`, `answer_source`, `blocks` (list of IDs) |
| `decision` | `decided_by` (role), `decided_on`, and `approved_by` / `approved_on` when approved |
| `source` | `kind` (`meeting`, `transcript`, `document`, `email`, `conversation`, `jira`, `confluence`), `input_date` |
| `entity` | `kind` (`role`, `system`, `data`, `integration`) |
| `process` | `variant` (`as-is`, `to-be`, `both`) |
| `requirement` | `jira_epic`, `fix_version`, `approved_by` / `approved_on` once signed off, `delivered_on` once every story is done |
| `review` | `verdict` (`ready`, `not-ready`), `reviewed_on` |

`status` says how far an item is trusted; a question's `state` says whether it is still open. An
open question can be `confirmed` (the BA agrees it is a real question).

## 5. Links and citations

- Standard markdown links with relative paths: `[Raising a job card](../workshop/CAP-012-raising-a-job-card.md)`.
  No `[[wikilinks]]`, no `![[embeds]]`.
- Link to a section with `page.md#heading-text`.
- Cite a claim with its ID in brackets right after it: `(SRC-031)`, `(PROJ-1234)`, `(DEC-007)`. Link the
  ID the first time it appears on a page.
- Images: `![What it shows](../../assets/CAP-012-approve-button.png)`.

## 6. Callouts

Only the five types GitHub and Obsidian both render:

| Callout | Use |
|---|---|
| `> [!CAUTION]` | **Unresolved:** behaviour that is unclear; always links the `Q-` |
| `> [!NOTE]` | **Assumption:** stated but not confirmed; links the `A-` |
| `> [!WARNING]` | A trap readers often fall into |
| `> [!IMPORTANT]` | A rule with legal, safety or contractual weight |
| `> [!TIP]` | Practical guidance |

## 7. Statuses

| Status | Meaning | Set by |
|---|---|---|
| `draft` | Extracted by AI, not yet checked | `/kb-seed`, `/intake`, `/sync` |
| `confirmed` | A BA checked it against its source | The BA, when accepting |
| `approved` | A named stakeholder agreed; `approved_by` and `approved_on` set, and a `DEC-` exists | The BA |
| `superseded` | Replaced; `superseded_by` set | The BA |

Answers label draft content "unconfirmed" and never use superseded content.

Requirement documents (`requirements/<slug>/requirement.md`) use the same four statuses:

| Status | Meaning |
|---|---|
| `draft` | Written by `/requirements`; still being clarified or reviewed |
| `confirmed` | `/review` says ready (or the BA accepted the remaining findings) and the BA agrees the content. `/backlog` needs at least this |
| `approved` | A named stakeholder signed it off; `approved_by` and `approved_on` set. The pipeline records it when a sign-off arrives through `/intake` or `/sync` |
| `superseded` | Replaced by another requirement document |

Each `review.md` starts with `type: review`, `id: REVIEW-<slug>`, `title`, `verdict` (`ready` or
`not-ready`), `reviewed_on` and `sources` (the requirement's `REQ-` ID).

## 8. The ten rules for changing the knowledge base

1. **Propose, then write.** Commands write proposals to `_staging/` only. Pages change only after the
   BA accepts an item.
2. **Cite the source.** Every item carries a quote and its location: file and paragraph, transcript
   time, Jira key and comment, Confluence page and section.
3. **Search before adding.** Check the index, the glossary (with aliases) and the registers. An
   existing item gets an update or a link, never a duplicate.
4. **Contradictions become questions.** A statement that conflicts with a `confirmed` or `approved`
   item becomes a `Q-` (or a `DEC-` waiting for a named approver). Nothing is overwritten.
5. **Authority decides decisions.** A statement becomes a `DEC-` only if `stakeholders.md` says the
   speaker can decide that matter. Otherwise it is recorded as their view, with a question to the
   owner.
6. **No personal data.** Use roles, not names, unless a name is needed (an approver, an owner).
   Remove patient, customer and other personal data from source records.
7. **Business language.** No code paths, class names or table names in pages. Put technical
   pointers in the source record if they matter.
8. **Log and index every change.** Each accepted change appends a line to `log.md` and regenerates
   `index.md` and the registers.
9. **Never delete.** Retire an item by setting `superseded` and `superseded_by`. A single business
   rule is retired on its page: its line stays, struck through and followed by "superseded by
   BR-022 (DEC-005)", the replacement rule gets a new ID, and the old ID moves out of the page's
   `rules` list, so the register lists only rules in force.

People may fix typos and wording on a page by hand, as long as the meaning doesn't change; add a
`log.md` line with the command `EDIT`. Anything that changes meaning goes through `/intake`.
10. **Raw input stays out of git.** `inbox/` is gitignored; only the redacted source record is
    committed.

## 9. Staging files

One file per input, `_staging/<yyyy-mm-dd>-<command>-<slug>.md`, from
[`templates/staging.md`](templates/staging.md). Each item has a kind, a verdict, the quote, the
critic's note and the exact change, followed by three checkboxes. Before the BA sees it, the critic
(`agents/_critic.md`) checks the file against the source and the knowledge base, and its findings are
recorded in the file's `Critic` section. The BA ticks one box per item, or answers in the chat
("accept 1-4, reject 5, edit 6: …"). The command applies the decided items when the BA says so,
normally once every item is decided. It deletes the staging file then, or keeps it with only the
undecided items left.

A staging file left in place for more than a day is reported by `/review kb`.

## 10. `log.md` lines

```text
- YYYY-MM-DD | COMMAND | SOURCE | CHANGES | accepted by ROLE
```

Each line is a list item, so it renders one per line on GitHub and in Obsidian.

`CHANGES` uses `+` for new, `~` for edited, `x` for superseded, `?` for questions closed:
`+CAP-012 ~CAP-007 +Q-014 ?Q-009 +DEC-007`.

## 11. Git

- Commands pull (`git pull --ff-only`) before staging and again before applying.
- After applying, they commit with `kb: <command> <source id> <short description>`, for example
  `kb: intake SRC-031 scheduling workshop 2026-10-14`.
- They ask before every push, because a push shares the change with everyone.
- Conflicts in the generated files (`index.md`, the registers): take either side, then run
  `/review kb`, which rebuilds them.

**When a push is rejected because another BA pushed first:**

1. `git pull --rebase` (Claude Code asks first).
2. If it stops on conflicts only in generated files or `log.md`: keep both sides' lines in
   `log.md`, rebuild `index.md` and the registers from the pages, `git add` them and
   `git rebase --continue`.
3. If the other BA created the same new IDs (same number, different item): renumber this side's
   items to the next free numbers, update every link, `rules`, `sources` and `blocks` entry that
   uses them, rebuild the generated files, and continue the rebase.
4. If both sides changed the text of the same page: `git rebase --abort` and tell the BA. Two people
   changed one page at once, and that needs a person to decide.
5. Push again (Claude Code asks).

## 12. Generated files

`index.md` and the three registers are rebuilt from the pages' properties. Never edit them by hand:
a hand edit is lost at the next rebuild. Order:

- **`index.md`:** by type, then area, then ID; one line per page with title, status and a one-line
  summary (the first sentence of the page).
- **`business-rules.md`:** by `BR-` number, with the rule's one-line statement and its page.
- **`decisions.md`:** by `DEC-` number, with date, decider and status.
- **`open-questions.md`:** questions with `state: open` first, by `due` (oldest first), with
  `asked_of` and `blocks`; then answered ones with `answered_on` and `answer_source`; `wontfix` last.
