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
     it. If it returns more than one site, ask which one this project uses.
   - Is the profile already filled (no `<...>` placeholders left in a section)? If so, this is a
     re-run: show what is filled and ask which sections to change. Never overwrite a filled section
     without a yes.
   - Values `scripts/new-project.sh` already filled (project name, repository name, harness version
     and commit) are shown for confirmation, not asked again.

## Interview

Ask in short rounds of three to five grouped questions. Propose a sensible default where you can and
mark it. Don't move on until each round is answered or deliberately skipped.

1. **Project:** name, one-line purpose, the roles of the BAs who maintain this repository. Only
   these roles apply proposals to the knowledge base (pipeline step 6).
2. **Jira:**
   - Which project key or keys? Read the available projects (through `discover`, then
     `listJiraProjects` via `executeRead`) and offer them.
   - Which issue types does the project use? Read them (`listJiraProjectIssueTypesMetadata`) and map
     each harness template (Epic, Story, Task, Spike, Bug) to one. If there is no Spike type, ask
     which type investigations use (often Task with a `spike` label).
   - Which issues count as "ours" for `/sync`? Propose a scope JQL and run it with
     `searchJiraIssuesUsingJql`. Show the total if the result gives one; Jira's newer search doesn't
     always, so otherwise page up to 100 and report "at least N", with the first few summaries so
     the BA can see the JQL catches the right issues.
   - Fix-version convention, default components, and the link types used for duplicates and related
     work (read the link types and offer them).
3. **Confluence:** used or not? If yes, read the spaces through `discover` and offer them; the BA
   picks the space keys. The publish parent page is optional: no command in this version publishes,
   but `/sync` skips pages under it, so record it if a published copy already exists.
4. **Business areas:** the four to eight areas the product divides into. They become
   `knowledge/domains/<area>/` folders and Jira labels.
5. **Stakeholders:** the main people by role. For each, their interest, what they own, and **what
   they can decide**. Names only where people need to know who to go to. Then the decisions that
   come up again and again (a change to a business rule, release content, accepting a knowledge
   base change): who is responsible, accountable, consulted and informed for each. Every authority
   check reads this, so propose a starting RACI from the answers and let the BA correct it.
6. **Existing material** for `/kb-seed`: documents (to be dropped in `inbox/`), Confluence page trees,
   Jira epics. If there is little written down, say so: the first knowledge can come from a
   discovery workshop through `/intake` instead.
7. **Writing rules** (profile section 7): words the project prefers and the ones to avoid (for
   example "job card", not "work order"), and any vague words to add to the list. Propose a few
   from what you've heard so far.
8. **Options:**
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
3. Set `created` and `updated` to today on `knowledge/glossary.md`, `knowledge/stakeholders.md` and
   `knowledge/raid.md`, replacing the `YYYY-MM-DD` placeholders.
4. Create a `knowledge/domains/<area>/` folder, each with a `.gitkeep`, for every area.
5. Check that `.gitignore` excludes `inbox/` and that `.claude/hooks/kb-sync.sh` exists.
6. Append a log line:
   `- <date> | SETUP | interview | profile, stakeholders, areas | accepted by <role>`.
7. Commit: `kb: setup <project>`. Then ask whether to push. If there is no remote yet, give the two
   commands to add one and push.

## Report

- **What was configured:** project, Jira keys and issue types, scope JQL with its issue count,
  required fields, Confluence on or off, areas, stakeholders and RACI, writing rules.
- **What is still unknown** (left as `<...>`), and how to fill it later (`/setup` again).
- **Next steps:**
  1. push, if you didn't;
  2. give the BAs write access to the repository and everyone else read access;
  3. drop existing documents into `inbox/` and run `/kb-seed`; or, with little written down, hold a
     discovery workshop and `/intake` its notes;
  4. work through the staging files, then share the repository URL with the team.

## Never

- Invent a stakeholder, a field rule or a JQL that wasn't confirmed.
- Write to Jira or Confluence.
- Store an API token or password anywhere. The Atlassian connection is OAuth through `/mcp` only.
