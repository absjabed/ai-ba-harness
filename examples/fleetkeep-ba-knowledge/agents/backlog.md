# `/backlog`: put approved work into Jira

You turn a reviewed requirement document into Jira issues built from the project's templates, and
bring later changes to that document into the issues it already created. You also create single
tasks, spikes and UAT bugs. You check every issue for duplicates first and show the whole batch for
approval. You create or change only what the BA approves. This is the only command that writes to
Jira.

## Input

| Argument | What it does |
|---|---|
| `requirements/<slug>/requirement.md` | Creates the epic and one story per `ST-`. Run it again after the document changes: issues that already have keys are compared and updated, not created again |
| `task ACT-<n>` | Creates one Task from an action in `knowledge/raid.md` |
| `spike Q-<n>` | Creates one Spike to investigate an open question |
| `bug <SRC-id> <item>` or `bug <description>` | Creates one Bug for a problem found in UAT or business review. Defects found in testing belong to the QA harness |

## Before anything (every mode)

1. Read `PROJECT-PROFILE.md` (sections 2 and 3 for the site, issue types, required fields and
   defaults; section 5 for `max_batch`), `knowledge/_meta/conventions.md` and `templates/jira/*.md`.
   For a requirement, also the document and its `review.md`.
2. **Local checks first,** so the BA hears every problem at once: the requirement mode's readiness
   (step 1 below), or the single item's source (single step 1).
3. **Then Jira.** Call `getAccessibleAtlassianResources` and check that the profile's site is listed.
   - If the tools aren't there or the call fails, tell the BA: run `/mcp`, approve and sign in to
     the repository's `atlassian` server (from `.mcp.json`; not another Atlassian connection), then
     run the command again. Report the local findings from step 2 too, and stop.
   - If the profile's Cloud ID is still a placeholder, use the one returned for the site, and tell
     the BA to run `/setup` again to record it.
   - Read the create metadata for each issue type you'll use (`getJiraIssueTypeMetaWithFields`, or
     `discover` and `executeRead`). If a required field isn't in the profile's table, ask for its
     value, and suggest `/setup` to record it. If the fix version doesn't exist in the project, stop
     and ask the BA to create it in Jira; "unscheduled" means the fix version field is left empty.
4. `git pull --ff-only`.

## Steps for a requirement document

1. **Check readiness.** Stop at the first that fails, and say what to run.
   - `review.md` must exist, with `reviewed_on` on or after the requirement's `updated` date.
     Writing keys back (step 6) doesn't change `updated`, so a re-run doesn't need a new review.
   - The document's `status` must be `confirmed` or `approved`. If the verdict was not ready, the BA
     may still confirm it for the stories `review.md` lists as ready; only `/review` (or the BA by
     hand) changes the status, never `/backlog`.
   - What blocks: the requirement's own lines decide (each story's "Open questions" and the FR
     table's Status), checked against each question's `state`. A story is blocked if it has a
     blocking open question, or relies on an FR still `pending` after the requirement's sign-off. A
     question that blocks only some criteria: offer to create the story without those criteria
     (listed in its description as "waiting for Q-x") if what remains still meets the definition of
     ready in `templates/jira/story.md`; otherwise the whole story waits.
   - An assumption that a criterion depends on must have an `A-` row in `raid.md`; if not, say so.
2. **Build the issues** from the templates:
   - **The epic:** summary from the goal; description from `templates/jira/epic.md`, including the
     non-functional requirements. If `jira_epic` already names one, compare it like a story below.
   - **One story per `ST-`**, from `templates/jira/story.md`. Each story lists the NFRs that
     constrain it.
   - **Issues that already have a key:** the document's story table is the source of truth; if
     `trace/map.csv` disagrees, say so. Read the issue with `getJiraIssue` and compare it section by
     section, as plain text (Jira returns its own formatting, so ignore differences in markup), plus
     the summary, parent, labels, fix version and required fields. Propose an edit, shown as a diff,
     only where the content differs.
   - **Keys whose story is no longer in the document:** never transition or delete them. List them
     for the BA to close or rescope in Jira by hand, and remove their rows from `trace/map.csv` once
     the BA confirms.
   - **Fields:**
     - issue type names, components, and labels `ba-harness` plus the document's `area` (each area
       when there are several);
     - fix version from the document;
     - every required field from the profile's table and the create metadata, asking where it says
       "ask";
     - priority only when the requirement states one with a source (priority is a stakeholder
       decision, never the agent's); story points and assignee always left empty.
   - **Source section:** link the requirement document and the knowledge pages at the commit being
     linked. When the remote is on GitHub or Azure DevOps, use its web URL and say the links work
     once pushed; otherwise give the paths.
3. **Search for duplicates.** For each new issue, search Jira in the profile's projects with the
   summary's key terms (`searchJiraIssuesUsingJql`, text search plus area label). For each possible
   match, show it and offer three choices:
   - **link:** create the new issue and link it as "relates";
   - **update:** don't create; propose an edit to the existing issue instead, shown as a diff;
   - **create anyway.**
4. **Show the preview table:** number, action (create, update or no change), type, summary, parent,
   fix version, required fields, duplicate verdict, and accept / edit / decline. Updates show their
   diff. If there are more than `max_batch` items, split them into batches. The epic goes in the
   first batch.
5. **Create, after an explicit yes for the batch.**
   - Create the epic first (`createJiraIssue`, or `executeWrite` on the v2 server). Then each story
     with `parent` set to the epic key, one at a time.
   - Apply approved updates with `editJiraIssue`, one at a time.
   - Claude Code will also ask before each write tool call; that prompt is expected.
   - After each create or update, read the issue back with `getJiraIssue`. Check that summary, type,
     parent, fix version, labels and required fields are as sent, and that every description heading
     is there. Calls can drop fields silently, so if something didn't stick, say so and offer to fix
     it with `editJiraIssue`.
   - Add the approved links (`createJiraIssueLink`).
   - If a create fails, stop the batch, report what was created and what wasn't, and don't retry
     blindly.
6. **Write the keys back,** without changing the document's `updated` date:
   - the document's `jira_epic` property and its story table's "Jira key" column;
   - one row per story in `trace/map.csv`: `fr_ids` (semicolon-separated, `FR-001;FR-002`),
     `story_id`, `jira_key`, `knowledge_pages` (semicolon-separated IDs, `CAP-004;DEC-002`),
     `confluence_page` (empty), `requirement_doc` (the path). Rows for updated stories are
     rewritten.
7. Append a log line (`- <date> | BACKLOG | REQ-<slug> | +<keys> ~<keys> | accepted by <role>`).
   Stage only the files this command changed, by name, and commit `req: backlog <slug> <epic key>`.
   Ask before pushing.

## Steps for a single task, spike or bug

1. **Read what it comes from.**
   - **task:** the `ACT-` row in the Actions table of `knowledge/raid.md`: the action, owner, due
     date and source. If its status isn't `open`, or it already has a Jira key, say so and stop.
   - **spike:** the `Q-` page: the question, why it matters, what it `blocks`. If its `state` isn't
     `open`, say so and stop.
   - **bug:** the item in the source record (a UAT session processed with `/intake`), or the BA's
     description. Ask for whatever the template needs and is missing: steps, the expected behaviour
     with the acceptance criterion or rule it breaks, the environment and the business impact. Never
     put real personal data in it.
2. **Build it** from `templates/jira/task.md`, `spike.md` or `bug.md`:
   - ask the BA for what the source doesn't give: for a task, why it's needed and when it's done;
     an action that is really an investigation can become a spike instead, if the BA prefers;
   - the owner's role goes in the description (assignee stays empty), and the action's due date in
     Jira's due date field;
   - labels `ba-harness` plus the area of the page the item comes from (ask if there isn't one);
   - ask for the parent epic if it belongs to one, and the fix version (for a bug, usually the
     release under test). If the epic doesn't exist yet, the issue is created without a parent; the
     requirement flow offers to re-parent it later.
3. **Search for duplicates** as in requirement step 3.
4. **Preview** the one issue and wait for a yes. Create it, read it back and fix what didn't stick, as
   in requirement step 5.
5. **Write the key back.** The preview's yes covers this edit; set the page's `updated` to today:
   - task: the Jira column of its `ACT-` row; the status stays `open` until the work is done;
   - spike: the question's `sources` list and its "Where it comes up" section;
   - bug: the source record's "What it changed" table.
6. Append a log line with the item's source record as SOURCE, for example
   `- <date> | BACKLOG | SRC-001 | ~ACT-002 <key> | accepted by Lead BA`, and commit
   `req: backlog task ACT-002 <key>`, staging only the files changed. Ask before pushing.

In the requirement flow, offer to set the epic as parent of existing tasks and spikes whose `ACT-` or
`Q-` the requirement cites, as updates in the preview.

## Report

- Created issues with keys and links; updated issues with what changed.
- Linked or updated instead of created, and why.
- Declined, skipped or waiting items, and why.
- Fields that didn't stick.
- Next: the delivery team picks up the keys. A developer can start the Dev harness's `/ba` from a
  story key: it reads the issue as its starting requirement and writes its own feature spec. The QA
  harness plans tests per story key.

## Never

- Create anything before the batch is approved, or more than `max_batch` items in one batch.
- Set story points or assignee, or a priority the requirement doesn't state.
- Include a criterion that a blocking open question still blocks, or create an issue without a fix
  version unless the BA explicitly chose "unscheduled".
- Delete or transition existing issues, or create Jira versions.
- Change an existing issue without showing the diff and getting a yes.
- Change the requirement's `status`.
