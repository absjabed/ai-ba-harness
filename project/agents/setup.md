# `/setup`: configure this repository for the project

You turn a fresh copy of the AI BA Harness into this project's BA knowledge repository. You
interview the lead BA, read the project's Jira and Confluence configuration, and fill
`PROJECT-PROFILE.md`. You write nothing outside the repository.

## Before anything

1. Read `PROJECT-PROFILE.md` and `knowledge/_meta/conventions.md`.
2. Check the state:
   - Is this a git repository with a remote (`git remote -v`)? If not, say so and continue; the
     knowledge base sync needs a remote later.
   - Is the repository's own `atlassian` server available? Call `getAccessibleAtlassianResources`.
     If it returns more than one site, ask which one this project uses.
     - If it fails, tell the BA to approve the project's `atlassian` server and sign in: `/mcp` in
       Claude Code, `opencode mcp auth atlassian` in OpenCode, `codex mcp login atlassian` in Codex
       (Codex also needs the project trusted first, or it ignores `.codex/`).
       Then carry on **offline**: record what the BA tells you, mark each Jira or Confluence value
       by adding ` (not verified)` after it (outside any backticks), leave the Cloud ID as a
       placeholder, skip the label check in round 4 and the "Read Jira's field rules" section, and
       list all of them under "Still unknown" in the report.
     - If Atlassian tools are available only under another name (a plugin, a claude.ai connector or
       a server from the BA's own settings), say so: the harness's permission rules are written for
       the project's `atlassian` server (and, in Claude Code, the Atlassian plugin), and any other
       connection would let Jira writes through without the per-write prompt. Ask the BA to use the
       project's server.
   - Is this a re-run? It is if `knowledge/log.md` already has a `SETUP` line. Then show what is
     filled, ask which sections to change, and never overwrite a section without a yes. If values
     were marked "not verified" and Atlassian is now available, offer to **verify**: read Jira and
     Confluence again and show where they differ from the profile.
   - Values the harness's copy script already filled (project name, repository name, harness
     version and commit) are shown for confirmation, not asked again. Fill the harness repository
     row from the template's address if the BA knows it.

## Interview

Ask in short rounds of three to five grouped questions. Propose a sensible default where you can and
mark it. Don't move on until each round is answered or deliberately skipped.

1. **Project:** name, one-line purpose, the roles who maintain this repository, and where the
   harness template lives (for `/improve-harness`). Only the maintainers apply proposals to the
   knowledge base (pipeline step 6). They are normally BAs; someone who decides product behaviour,
   such as the Product owner, shouldn't also accept the record of their own decisions.
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
4. **Business areas:** the four to eight areas the product divides into, each with a one-line
   description of what it covers. They become `knowledge/domains/<area>/` folders and Jira labels.
   If Jira is available, check that the labels don't clash with labels already used for something
   else.
5. **Stakeholders:** the main people by role, filling every column of `knowledge/stakeholders.md`:
   organisation, interest, what they own, **what they can decide**, and how to reach them. Leave a
   cell blank when the BA doesn't know; never invent one. Names only where people need to know who
   to go to. Then the decisions that come up again and again (a change to a business rule, release
   content, accepting a knowledge base change): who is responsible, accountable, consulted and
   informed for each. Propose a starting RACI from the answers and let the BA correct it.
   - Every role named in the RACI must be a stakeholder row; add any that are missing.
   - "Can decide" and the RACI's accountable role must agree. Where they don't, propose making the
     RACI follow "Can decide" (the other role becomes consulted) and ask. Every authority check
     reads both.
   - The "Accepting a knowledge base change" row: every maintainer from round 1 is responsible, the
     Lead BA is accountable, and nobody else is either.
6. **Existing material** for `/kb-seed`: documents (to be dropped in `inbox/`), Confluence page trees,
   Jira epics. Each row gets a status: `ready` only if the file is already in `inbox/` (or the page
   tree or epics exist); otherwise `expected`, with a placeholder name. Replace the template's
   example rows; `none` is only for fixed rows such as the publish parent page. If there is little written down, say so: the first knowledge can come from a discovery
   workshop through `/intake` instead, and notes for `/intake` don't belong in this table.
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

1. `git pull --ff-only`, so two people running `/setup` don't overwrite each other.
2. Show **one** preview of everything this step writes: the profile as a diff, the stakeholder rows
   and RACI, the dates, the folders. Write it all after one yes.
   - `PROJECT-PROFILE.md`: set `confluence: on` in section 5 if Confluence is used. Fill the Cloud ID
     from `getAccessibleAtlassianResources`, or leave the placeholder when offline. Write `none` in
     rows that don't apply.
3. Fill `knowledge/stakeholders.md`: one row per stakeholder and the RACI rows. The page keeps
   `status: draft` until the Product owner (or whoever the RACI makes accountable for business
   rules) has checked it; the report says so.
   - Set `created` and `updated` to today on `knowledge/glossary.md`, `knowledge/stakeholders.md`
     and `knowledge/raid.md`, replacing the `YYYY-MM-DD` placeholders.
4. Create a `knowledge/domains/<area>/` folder, each with a `.gitkeep`, for every area.
5. Check that `.gitignore` excludes `inbox/` and that `tools/kb-sync.sh` exists.
6. Append a log line:
   `- <date> | SETUP | interview | profile, stakeholders, areas | accepted by <role>`.
7. If Python is available, run `python tools/kb.py rebuild`, so the index lists the root pages.
8. Commit `kb: setup <repository name>`, for example `kb: setup fleetkeep-ba-knowledge`. Then ask
   whether to push. If there is no remote yet, give the two
   commands to add one and push.

## Report

- **What was configured:** project, Jira keys and issue types, scope JQL with its issue count,
  required fields, Confluence on or off, areas, stakeholders and RACI, writing rules.
- **What is still unknown:** placeholders left, values marked "not verified" (with "issue count:
  not run" for the scope JQL when offline), and how to fill them later (`/setup` again).
- **Next steps:**
  1. push, if you didn't;
  2. give the BAs write access to the repository and everyone else read access;
  3. have the stakeholder list and RACI checked by the person accountable for business rules, then
     set `knowledge/stakeholders.md` to `confirmed`;
  4. drop existing documents into `inbox/` and run `/kb-seed`; or, with little written down, hold a
     discovery workshop and `/intake` its notes;
  5. work through the staging files, then share the repository URL with the team.

## Never

- Invent a stakeholder, a field rule or a JQL that wasn't confirmed.
- Write to Jira or Confluence.
- Store an API token or password anywhere. The Atlassian connection is OAuth through the
  assistant's own sign-in only.
