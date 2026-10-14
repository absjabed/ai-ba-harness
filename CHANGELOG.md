# Changelog

All notable changes to the AI BA Harness template. Versions follow the rule in the README: patch for
fixes, minor for new features projects can use without changes, major when project repositories must
change something.

## 0.5.0 (2026-10-15)

Tested on a demo project ("FleetKeep Demo"): each command was run, in a fresh context, exactly as
its definition says, and every point where it was unclear, contradictory or impossible was logged
and fixed (about 200 in all; see `research/08-demo-test.md`). Plus a command for improving the
harness itself.

- **`/improve-harness`** (new, the ninth command): works out what isn't working, decides whether the
  fix is a project setting, knowledge or a harness change, writes a proposal to `harness-feedback/`
  from `templates/harness-feedback.md`, and applies safe changes locally after a yes, recording
  them in the new profile section 8. Safety changes are never applied locally.
- **`tools/kb.py`** (new): `rebuild` writes the index and registers deterministically, `check`
  validates properties, file names, IDs, rules, links and anchors, cited IDs, overdue questions and
  actions, and whether the generated files are current; `next` gives the next free ID. Commands use
  it when Python is available. `.github/workflows/kb-check.yml` runs the check on every push.
- **Safety:** the permission rules now also cover the Atlassian plugin's tool names
  (`mcp__plugin_atlassian_atlassian__`), which previously let Jira writes skip the per-write prompt;
  `/setup` warns about any other Atlassian connection. The critic is a read-only sub-agent
  (`.claude/agents/critic.md`).
- **Knowledge pipeline:** new pages, questions and decisions are proposed in full, so the BA accepts
  exactly what is written; chat decisions are written into the staging file; resuming re-checks
  what changed since staging; one rule for statuses, due dates, redacted quotes, provisional IDs and
  dependent items; vague or incomplete items must carry a question or an Open items note; meeting
  sections and the play-back are part of staging; clearer critic findings.
- **`/setup`:** an offline mode that records values as "not verified" and a later verify run;
  re-runs detected from `log.md`; one preview of everything it writes; maintainers, "Can decide" and
  the RACI must agree; every stakeholder column asked; the harness repository recorded.
- **`/ask`:** never reads `inbox/`; clearer citations; says when Jira wasn't checked; points to an
  existing question instead of drafting a duplicate; a single rule set in `agents/ask.md`, which
  `CLAUDE.md` and `AGENTS.md` now defer to.
- **Conventions:** how to choose a page and area, the heading-anchor rule, file names of at most 64
  characters, statuses and what they cover, the log line's fields, RAID statuses, staging files
  committed to finish later, and the generated files' exact format.
- **`/requirements`:** the BA's answers on product behaviour become proposals: a question to the
  owner, the FR marked "pending", and the owner's sign-off of the requirement answers them all. The
  draft is written first, pre-checked, then shown together with its staged knowledge; one commit.
  FR Status column, per-criterion blocking (`Q-x (blocks AC-2)`), assumptions staged as `A-` rows.
- **`/review`:** a clear definition of blocked criteria and stories, which no longer count against the
  verdict; checks for assumptions, FR statuses and NFR coverage; finding IDs; a commit for the
  review; what to do without Atlassian.
- **`/backlog`:** local checks before the Jira check; create metadata, Cloud ID and fix versions
  checked; epic compared and updated too; NFRs in the epic; partial stories only if they still meet
  the definition of ready; keys written back without making the review stale; a log line; trace map
  column `fr_ids`; task fields (owner, due date) and re-parenting tasks under a later epic.
- **Profile:** "Other maintainers" replaces "Other BAs"; `none` instead of deleting rows; section 6
  gets a status column; section 8 lists local harness changes.

To update a project from 0.4.x: copy `agents/`, `.claude/`, `templates/`, `tools/`, `.github/`,
`knowledge/_meta/`, `CLAUDE.md` and `AGENTS.md`; add `harness-feedback/`; in `PROJECT-PROFILE.md`
rename "Other BAs" to "Other maintainers", add the "Harness repository" row, the status column in
section 6 and section 8; rename `trace/map.csv`'s first column to `fr_ids`; add a Status column to
each requirement's FR table; then run `python tools/kb.py rebuild` and `check`.

## 0.4.2 (2026-10-14)

- `docs/walkthrough.html` is back, as in the QA harness: the handbook's worked example as a page of
  its own for sharing with a team. It is generated from the handbook by
  `scripts/build-walkthrough.py`, so the two can't drift; the handbook and the walkthrough link to
  each other.

No changes to `project/`; projects need nothing.

## 0.4.1 (2026-10-14)

- One handbook. The walkthrough is now the handbook's "Follow a whole project" section, in the same
  shape as the QA harness's worked example: the example, the words you will see, six parts from
  `/setup` to `/ask`, and a "who does what" table. Every command has a worked example, with what you
  type, what it reads, what it asks and what you get, including ones the walkthrough lacked:
  `/kb-seed`, `/review` on someone else's Jira issue, and `/ask` when the knowledge base doesn't know.
  `docs/walkthrough.html` is removed.

No changes to `project/`; projects need nothing.

## 0.4.0 (2026-10-14)

Closes the gaps after `/backlog`, where work is in Jira but still changing.

- `/backlog` creates single items: `task ACT-<n>` from an action, `spike Q-<n>` for an open
  question, `bug <SRC-id> <item>` for a UAT finding. Re-running it on a requirement updates the
  stories that already have keys (shown as diffs), creates new ones, and lists dropped ones for the
  BA to close by hand.
- Delivery impact: every staged change to an existing page lists the requirements, stories and Jira
  keys that rely on it (from `trace/map.csv` and the requirement documents), and the apply report
  ends with the next step. The critic checks it.
- `/sync` brings delivered work into the knowledge base: when a traced story reaches Done, it
  proposes page updates from the requirement, and sets the requirement's `delivered_on` when every
  story is done.
- Actions register: an Actions table (`ACT-`) in `raid.md`; `/review kb` reports overdue actions.
- Sign-off: a requirement's approval arriving through `/intake` or `/sync` sets it to `approved` with
  `approved_by` and `approved_on`.
- `/review kb` drafts one message per stakeholder with the open questions waiting on them.
- Conventions: how to recover when a push is rejected because another BA pushed first, and how a
  single business rule is retired.
- The walkthrough gains weeks 5 to 11: deciding with delivery impact, a task, questions to chase, a
  rule changing after the stories exist, sign-off, a UAT bug and the release.

To update a project from 0.3.0, copy `agents/`, `.claude/commands/backlog.md`,
`knowledge/_meta/conventions.md`, `knowledge/_meta/templates/` and `templates/requirement.md`, and
add the Actions section from the template's `knowledge/raid.md` to the project's `raid.md`.

## 0.3.0 (2026-10-14)

From walking a full project through the harness, starting at `/setup`:

- `docs/walkthrough.html`: a month on FleetKeep, from `/setup` to stories in Jira, showing what each
  command reads, asks and produces, with links into the worked example. Linked from the handbook.
- `/setup` now maps Jira issue types to the harness templates, asks for a RACI of recurring
  decisions and for the writing rules (house terms and vague words), copes with Jira searches that
  return no total, asks which site to use when there are several, confirms what the copy script
  already filled instead of asking again, dates the glossary, stakeholders and RAID pages, and ends
  with a fuller list of next steps (repository access; `/kb-seed` or a discovery workshop).
- `/kb-seed` hands over to `/sync`: after seeding from Jira or Confluence it records where it
  stopped, so the first `/sync` carries on from there. Its wording on draft and confirmed now
  matches the pipeline.
- `/review kb` reports business areas with no pages yet.
- `SETUP.md` and the handbook cover Claude Code's first-open prompts (trust the folder, enable the
  `atlassian` server), repository access, and starting from a workshop when little is written down.

To update a project from 0.2.0, copy `agents/setup.md`, `agents/kb-seed.md` and `agents/review.md`.

## 0.2.0 (2026-10-14)

- Critic for the knowledge pipeline (`agents/_critic.md`, new step 4): before the BA decides, a
  fresh-context sub-agent (or a second pass) re-reads the source and checks the staging file for
  missed items, misquotes, wrong verdicts, contradictions of confirmed text, unchecked authority and
  unredacted data. Staging files gain a `Critic` section and a `Critic` row per item. Pipeline steps
  after it are renumbered: confirm is 5, apply is 6.
- `/requirements` pre-checks its draft with `/review`'s rule checks before showing it, fixing only
  mechanical problems. `/review` remains the gate for `/backlog`.
- `/ask` checks each claim against the page it cites before answering.
- `/kb-seed`, `/intake`, `/sync` and `/requirements` may start sub-agents (`Agent` added to their
  allowed tools). `/ask` still can't.
- Staging rules in the conventions say when decided items are applied and mention the critic.

To update a project from 0.1.0, copy `agents/`, `.claude/commands/`,
`knowledge/_meta/conventions.md` and `knowledge/_meta/templates/staging.md`. Existing staging files
get their critique the next time they are resumed.

## 0.1.0 (2026-10-14)

First version, built from the agreed design in `design/`. Not yet used on a real project.

- Eight commands: `/setup`, `/kb-seed`, `/intake`, `/sync`, `/requirements`, `/review`, `/backlog`,
  `/ask`, with vendor-neutral definitions in `project/agents/` and thin Claude Code wrappers.
- A shared knowledge pipeline (extract, judge, stage, confirm, apply) for everything that enters the
  knowledge base.
- Knowledge base skeleton with conventions, page templates and generated registers, stored by
  Obsidian's rules and compatible with Open Knowledge Format; shipped Obsidian settings.
- Automatic sync: a session-start hook that fast-forwards each clone when it is safe to.
- Jira templates for epics, stories, tasks, spikes and UAT bugs, and a requirement document template.
- Safety: Atlassian write tools and `git push` need confirmation; force push and hard reset are
  denied; `/ask` can't write; `inbox/` is gitignored.
- `scripts/new-project.sh` to create a project repository.
- Worked example (`examples/fleetkeep-ba-knowledge/`), setup guide and BA handbook.
