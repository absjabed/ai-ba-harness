# Changelog

All notable changes to the AI BA Harness template. Versions follow the rule in the README: patch for
fixes, minor for new features projects can use without changes, major when project repositories must
change something.

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
