# `/backlog`: create the epic and stories in Jira from a reviewed requirement

You turn a reviewed requirement document into Jira issues built from the project's templates. You
check every one for duplicates first and show the whole batch for approval. You create only what the
BA approves. This is the only version 1 command that writes to Jira.

## Before anything

Read:
- `PROJECT-PROFILE.md`: sections 2 and 3 (issue types, required fields, defaults) and section 5
  (`max_batch`);
- `knowledge/_meta/conventions.md`;
- `templates/jira/*.md`;
- the requirement document and its `review.md`.

If the Atlassian server isn't connected, tell the BA to run `/mcp` and sign in, and stop.

## Input

The path to a `requirement.md`, for example `/backlog requirements/approve-lists/requirement.md`.

## Steps

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
4. **Show the preview table:** number, type, summary, parent, fix version, required fields, duplicate
   verdict, and accept / edit / decline. If there are more than `max_batch` items, split them into
   batches. The epic goes in the first batch.
5. **Create, after an explicit yes for the batch.**
   - Create the epic first. Then each story with `parent` set to the epic key, one at a time.
   - Claude Code will also ask before each write tool call; that prompt is expected.
   - After each create, read the issue back with `getJiraIssue`. Check that summary, type, parent,
     fix version and required fields are as sent. v2 "execute" calls can drop fields silently, so if
     something didn't stick, say so and offer to fix it with `editJiraIssue`.
   - Add the approved links (`createJiraIssueLink`).
   - If a create fails, stop the batch, report what was created and what wasn't, and don't retry
     blindly.
6. **Write the keys back:**
   - the document's `jira_epic` property and its story table's "Jira key" column;
   - one row per story in `trace/map.csv`:
     `FR ids, ST id, Jira key, knowledge pages, Confluence page (empty), requirement doc path`.
7. Commit: `req: backlog <slug> <epic key>`. Ask before pushing.

## Report

- Created issues with keys and links.
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
