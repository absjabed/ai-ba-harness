# `/backlog`: put approved work into Jira

You turn a reviewed requirement document into Jira issues built from the project's templates, and
bring later changes to that document into the stories it already created. You also create single
tasks, spikes and UAT bugs. You check every issue for duplicates first and show the whole batch for
approval. You create or change only what the BA approves. This is the only command that writes to
Jira.

## Before anything

Read:
- `PROJECT-PROFILE.md`: sections 2 and 3 (issue types, required fields, defaults) and section 5
  (`max_batch`);
- `knowledge/_meta/conventions.md`;
- `templates/jira/*.md`;
- the requirement document and its `review.md`.

If the Atlassian server isn't connected, tell the BA to run `/mcp` and sign in, and stop.

## Input

| Argument | What it does |
|---|---|
| `requirements/<slug>/requirement.md` | Creates the epic and one story per `ST-`. Run it again after the document changes: stories that already have keys are compared and updated, not created again |
| `task ACT-<n>` | Creates one Task from an action in `knowledge/raid.md` |
| `spike Q-<n>` | Creates one Spike to investigate an open question |
| `bug <SRC-id> <item>` or `bug <description>` | Creates one Bug for a problem found in UAT or business review. Defects found in testing belong to the QA harness |

## Steps for a requirement document

1. **Check readiness.**
   - If `review.md` is missing, or older than the document, ask the BA to run `/review` first.
   - If its verdict is not ready, offer to create only the stories it lists as ready, or to stop.
   - The document's `status` must be `confirmed` or `approved`. If it is still `draft`, ask the BA to
     confirm it first.
   - Never create a story that has a blocking open question.
2. **Build the issues** from the templates:
   - **The epic** (unless the document's `jira_epic` already names one): summary from the goal;
     description from `templates/jira/epic.md`.
   - **One story per `ST-`**, from `templates/jira/story.md`.
   - **Stories that already have a key** (in the document's story table or in `trace/map.csv`): read
     the issue with `getJiraIssue`, rebuild it from the template and the current document, and
     compare. If the summary, description, fix version or required fields differ, propose an edit,
     shown as a diff, instead of a create. If nothing differs, leave it alone.
   - **Keys whose story is no longer in the document:** never transition or delete them. List them
     for the BA to close or rescope in Jira by hand, and remove their rows from `trace/map.csv` once
     the BA confirms.
   - **Fields:**
     - issue type names, components and labels (`ba-harness` plus the area) from the profile;
     - fix version from the document;
     - every required custom field from the profile's table, asking where it says "ask";
     - priority only when the requirement states one with a source (priority is a stakeholder
       decision, never the agent's); story points and assignee always left empty.
   - **Source section:** link the requirement document and the knowledge pages. Use the repository
     web URL if the remote is on GitHub or Azure DevOps; otherwise give the path.
3. **Search for duplicates.** For each issue, search Jira in the profile's projects with the summary's
   key terms (`searchJiraIssuesUsingJql`, text search plus area label). For each possible match, show
   it and offer three choices:
   - **link:** create the new issue and link it as "relates";
   - **update:** don't create; propose an edit to the existing issue instead, shown as a diff;
   - **create anyway.**
4. **Show the preview table:** number, action (create, update or no change), type, summary, parent,
   fix version, required fields, duplicate verdict, and accept / edit / decline. Updates show their
   diff. If there are more than `max_batch` items, split them into
   batches. The epic goes in the first batch.
5. **Create, after an explicit yes for the batch.**
   - Create the epic first. Then each story with `parent` set to the epic key, one at a time.
   - Apply approved updates with `editJiraIssue`, one at a time.
   - Claude Code will also ask before each write tool call; that prompt is expected.
   - After each create or update, read the issue back with `getJiraIssue`. Check that summary, type, parent,
     fix version and required fields are as sent. v2 "execute" calls can drop fields silently, so if
     something didn't stick, say so and offer to fix it with `editJiraIssue`.
   - Add the approved links (`createJiraIssueLink`).
   - If a create fails, stop the batch, report what was created and what wasn't, and don't retry
     blindly.
6. **Write the keys back:**
   - the document's `jira_epic` property and its story table's "Jira key" column;
   - one row per story in `trace/map.csv`:
     `FR ids, ST id, Jira key, knowledge pages, Confluence page (empty), requirement doc path`.
     Rows for updated stories are rewritten with their current FRs and pages.
7. Commit: `req: backlog <slug> <epic key>`. Ask before pushing.

## Steps for a single task, spike or bug

1. **Read what it comes from.**
   - **task:** the `ACT-` row in the Actions table of `knowledge/raid.md`: the action, owner, due
     date and source. If the row already has a Jira key, show it and stop.
   - **spike:** the `Q-` page: the question, why it matters, what it `blocks`. If its `state` isn't
     `open`, say so and stop.
   - **bug:** the item in the source record (a UAT session processed with `/intake`), or the BA's
     description. Ask for whatever the template needs and is missing: steps, the expected behaviour
     with the acceptance criterion or rule it breaks, the environment and the business impact. Never
     put real personal data in it.
2. **Build it** from `templates/jira/task.md`, `spike.md` or `bug.md`, with the same field rules as
   above. Ask for the parent epic if it belongs to one, and for the fix version (for a bug, usually
   the release under test).
3. **Search for duplicates** as above.
4. **Preview** the one issue and wait for a yes. Create it, and read it back.
5. **Write the key back:**
   - task: the Jira column of its `ACT-` row, and the row's status stays `open` until the work is done;
   - spike: the question's `sources` list and its "Where it comes up" section;
   - bug: the source record's "What it changed" table.
6. Append a log line, for example
   `- 2026-10-20 | BACKLOG | ACT-002 | ~RAID FK-1310 | accepted by Lead BA`, and commit
   `req: backlog task ACT-002 FK-1310`. Ask before pushing.

## Report

- Created issues with keys and links; updated issues with what changed.
- Linked or updated instead of created, and why.
- Declined or skipped items, and why.
- Fields that didn't stick.
- Next: the delivery team picks up the keys. A developer can start the Dev harness's `/ba` from a
  story key: it reads the issue as its starting requirement and writes its own feature spec. The QA
  harness plans tests per story key.

## Never

- Create anything before the batch is approved, or more than `max_batch` items in one batch.
- Set story points or assignee, or a priority the requirement doesn't state.
- Create a story with a blocking open question, or without a fix version, unless the BA explicitly
  chose "unscheduled".
- Delete or transition existing issues.
- Change an existing issue without showing the diff and getting a yes.
