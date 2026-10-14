# `/sync`: bring new Jira and Confluence activity into the knowledge base

You read what changed in the project's Jira issues and Confluence pages since the last sync, pick out
what matters to the knowledge base, and propose it to the BA. You only read from Jira and
Confluence; you never write to them.

## Before anything

Read `PROJECT-PROFILE.md` (section 2 for scope, section 5 for limits), `knowledge/_meta/conventions.md`,
`agents/_knowledge-pipeline.md` and `knowledge/_meta/sync.json`.

If the Atlassian server isn't connected, tell the BA to run `/mcp` and sign in, and stop. If the
scope JQL is still a placeholder, tell them to run `/setup`.

## Input

`/sync jira`, `/sync confluence`, or `/sync` for both. Confluence only runs when `confluence: on`.

## Steps

### Jira

1. Take `last_synced` from `sync.json`. If it is empty, ask how far back to go (default 14 days).
2. Work out the minutes between `last_synced` and now, and add 10 minutes of overlap. JQL doesn't
   accept ISO timestamps, and it reads absolute dates in the Jira user's time zone, so use the
   relative form instead: the scope JQL plus `AND updated >= -<minutes>m`, ordered by `updated ASC`,
   at most `sync_max_issues` issues. (For a first sync of 14 days: `updated >= -20160m`.)
3. The overlap can bring back items already processed. Check the `jira` source records in
   `knowledge/sources/`: comments and changes already recorded there are skipped, not proposed
   again.
4. For each issue, one at a time:
   - `getJiraIssue` for its fields and description;
   - `listJiraIssueComments` for comments added since `last_synced`;
   - `listJiraIssueChangelogs` for status, fix version and parent changes since then.
5. Keep what matters to the knowledge base:
   - **Answers:** comments that answer an open question, by key or by subject.
   - **Decisions:** "agreed", "decided", "we'll go with", or a stakeholder's approval.
   - **Changes:** to rules or scope, such as acceptance criteria rewritten or a story descoped.
   - **Terms:** new or changed.
   - **Status changes with business meaning:** an epic cancelled, a story moved to another release,
     an issue closed as "won't do".

   Ignore routine workflow moves, estimates and assignee changes.

### Confluence

1. Take `last_synced` and work out the minutes since then plus 10, as for Jira. Search the profile's
   spaces with CQL `space in (<keys>) AND lastmodified >= now("-<minutes>m")`, at most
   `sync_max_pages` pages.
2. Read each changed page with `getConfluenceContent`. Pages this repository published itself (those
   under the publish parent page) are skipped; they are copies of the knowledge base.
3. Keep the same kinds of change as for Jira.

### Then

1. Run the pipeline steps 1 to 6, critique included:
   - every item's location is the issue key and comment number, or the page title and section;
   - the source record's kind is `jira` or `confluence`, and its title covers the date range.
2. **Only after the BA has decided every item** (or explicitly deferred the rest), set `last_synced`
   in `sync.json`:
   - to the `updated` time of the last issue or page fully processed;
   - as an ISO 8601 date and time with offset, for example `2026-10-15T08:55:00+01:00`.
   If the run stopped early, the time stays where it was, so nothing is skipped. Commit `sync.json`
   with the knowledge changes.
3. If a rate limit is hit (a 429 error), stop cleanly. Stage what was read, report where you stopped,
   and the next run continues from there.

## Report

- What was read: issues and pages, with the date range.
- Items staged by verdict; questions answered; decisions found.
- Anything left for the next run.

## Never

- Write to Jira or Confluence, including comments.
- Move `last_synced` past anything the BA hasn't decided.
- Read outside the scope JQL or the profile's spaces.
