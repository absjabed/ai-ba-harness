# `/setup`: configure this repository for the project

You turn a fresh copy of the AI BA Harness into this project's BA knowledge repository. You
interview the lead BA, read the project's Jira and Confluence configuration, and fill
`PROJECT-PROFILE.md`. You write nothing outside the repository.

## Before anything

1. Read `PROJECT-PROFILE.md` and `knowledge/_meta/conventions.md`.
2. Check the state:
   - Is this a git repository with a remote (`git remote -v`)? If not, say so and continue; the
     sync hook needs a remote later.
   - Is the Atlassian server available? Call `getAccessibleAtlassianResources`. If it fails, tell the
     BA to run `/mcp`, choose `atlassian` and sign in, then continue with the parts that don't need
     it.
   - Is the profile already filled (no `<...>` placeholders left in a section)? If so, this is a
     re-run: show what is filled and ask which sections to change. Never overwrite a filled section
     without a yes.

## Interview

Ask in short rounds of three to five grouped questions. Propose a sensible default where you can and
mark it. Don't move on until each round is answered or deliberately skipped.

1. **Project:** name, one-line purpose, the roles of the BAs who maintain this repository.
2. **Jira:**
   - Which project key or keys? Read the available projects (through `discover`, then
     `listJiraProjects` via `executeRead`) and offer them.
   - Which issues count as "ours" for `/sync`? Propose a scope JQL and show how many issues it
     matches with `searchJiraIssuesUsingJql` (`maxResults` 1, read the total).
   - Fix-version convention, default components, and the link types used for duplicates and related
     work.
3. **Confluence:** used or not? If yes, which space keys, and under which page should published
   knowledge go later?
4. **Business areas:** the four to eight areas the product divides into. They become
   `knowledge/domains/<area>/` folders and Jira labels.
5. **Stakeholders:** the main people by role. For each, their interest, what they own, and **what
   they can decide**. Names only where people need to know who to go to.
6. **Existing material** for `/kb-seed`: documents (to be dropped in `inbox/`), Confluence page trees,
   Jira epics.
7. **Options:**
   - Automatic sync on? (default on)
   - Is `markitdown` installed, for Word, Excel and PowerPoint? (default pdf)
   - Batch size (default 15).

## Read Jira's field rules

For each project key and each issue type in the profile's issue-type table:

1. Use `discover` and then `getJiraIssueTypeMetaWithFields` (through `executeRead`) to list the
   required fields.
2. For every required field other than summary, description, project, issue type, reporter and
   parent, add a row to section 3's "Required and custom fields" table with its name and ID.
3. Ask the BA how the harness should fill each one: a fixed default, a value from the requirement,
   or "ask each time".
4. Read the available fix versions and components and confirm the defaults.

v2 "execute" calls silently drop parameter names they don't recognise. After each one, check that
the result actually contains what you asked for; if it doesn't, say so rather than guessing.

## Write

1. Show the complete filled `PROJECT-PROFILE.md` as a diff, and write it after a yes. Set
   `confluence: on` in section 5 if Confluence is used. Fill the Cloud ID from
   `getAccessibleAtlassianResources`.
2. Fill `knowledge/stakeholders.md` with the stakeholders as `draft`: one row each, plus the RACI
   rows the BA gave.
3. Create a `knowledge/domains/<area>/` folder, each with a `.gitkeep`, for every area.
4. Check that `.gitignore` excludes `inbox/` and that `.claude/hooks/kb-sync.sh` exists.
5. Append a log line:
   `- <date> | SETUP | interview | profile, stakeholders, areas | accepted by <role>`.
6. Commit: `kb: setup <project>`. Then ask whether to push. If there is no remote yet, give the two
   commands to add one and push.

## Report

- **What was configured:** project, Jira keys, scope JQL with its issue count, Confluence on or off,
  areas, stakeholders.
- **What is still unknown** (left as `<...>`), and how to fill it later (`/setup` again).
- **Next step:** drop existing documents into `inbox/`, then run `/kb-seed`.

## Never

- Invent a stakeholder, a field rule or a JQL that wasn't confirmed.
- Write to Jira or Confluence.
- Store an API token or password anywhere. The Atlassian connection is OAuth through `/mcp` only.
