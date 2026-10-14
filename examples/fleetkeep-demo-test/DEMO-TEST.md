# About this folder

This is the raw output of the demo test of 0.4.2 and 0.5.0, kept as it was left, not tidied up. For a
curated example to learn from, use [`../fleetkeep-ba-knowledge/`](../fleetkeep-ba-knowledge/EXAMPLE.md)
instead. The method and the findings are in [`research/08-demo-test.md`](../../research/08-demo-test.md).

## What it is

A project BA repository, "FleetKeep Demo", created with `scripts/new-project.sh` from harness 0.4.2
on 2026-10-14. Every command was then run on it by a sub-agent following the command files exactly,
with the BA's answers given up front, and without Atlassian. Midway through, the harness files were
updated to the 0.5.0 pre-release, so the commands from `/review` onwards ran on newer definitions than
the earlier ones.

- **The harness files here (`agents/`, `.claude/`, `templates/`, `tools/`) are a snapshot,** not the
  current harness. Use `project/` for that. They also include one local change made by
  `/improve-harness` (profile section 8).
- **Its remote was a throwaway local repository,** so it was never pushed anywhere. Its own git
  history isn't kept; the commits are listed below.
- **Everything in it is fictional,** including the person's name and phone number in the test input,
  which were planted to test redaction.

## What to look at

| What | Where | Produced by |
|---|---|---|
| The input | [`test-input/2026-10-14-inspections-workshop-notes.md`](test-input/2026-10-14-inspections-workshop-notes.md) | Written for the test. In a real project it would sit in `inbox/` and never be committed |
| The profile, filled offline | [`PROJECT-PROFILE.md`](PROJECT-PROFILE.md) | `/setup` |
| The knowledge from the workshop | [`knowledge/index.md`](knowledge/index.md), [`knowledge/sources/`](knowledge/sources/) | `/intake`, staged, critiqued, then applied in a second session |
| A requirement with five stories, most waiting on the Product owner | [`requirements/inspection-due-dates-and-dashboard-banding/`](requirements/inspection-due-dates-and-dashboard-banding/requirement.md) | `/requirements` |
| Its review: not ready | [`review.md`](requirements/inspection-due-dates-and-dashboard-banding/review.md) in the same folder | `/review` |
| Two harness proposals: one applied locally, one safety change refused locally | [`harness-feedback/`](harness-feedback/) | `/improve-harness` |
| The change log | [`knowledge/log.md`](knowledge/log.md) | every command |

`python tools/kb.py check` passes here with no errors.

## Its commits, newest first

| Commit | Date | Message |
|---|---|---|
| `8724b94` | 2026-10-15 | harness: proposed backlog-create-without-per-issue-prompts |
| `4db544c` | 2026-10-15 | harness: local data-line-under-each-story |
| `7376af6` | 2026-10-15 | kb: profile vague word due soon |
| `0b8945c` | 2026-10-15 | Update harness to 0.5.0; review of inspection due dates |
| `c06a05e` | 2026-10-15 | kb: rebuild generated files with tools/kb.py |
| `2355a6f` | 2026-10-15 | Update harness to 0.5.0 (pre-release) |
| `82f38b4` | 2026-10-15 | req: draft inspection-due-dates-and-dashboard-banding |
| `f418d11` | 2026-10-14 | kb: intake SRC-001 inspections workshop 2026-10-14 |
| `95d30ac` | 2026-10-14 | kb: setup FleetKeep Demo |
| `a92c414` | 2026-10-14 | Start from AI BA Harness 0.4.2 |

`/backlog` was also run, in both modes, but stopped cleanly without Jira and changed nothing, so it
has no commit.
