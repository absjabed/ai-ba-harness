# `/kb-seed`: build the first knowledge base from existing material

You read the material that already exists about the project (documents, Confluence pages, Jira
epics) and propose the first version of the knowledge base: glossary, stakeholders, capabilities and
their rules, processes, decisions, open questions and risks. The BA accepts what is right.

## Before anything

Read `PROJECT-PROFILE.md` (section 6 lists the material), `knowledge/_meta/conventions.md` and
`agents/_knowledge-pipeline.md`. You follow that pipeline; this file adds what is specific to
seeding.

## Input

- No argument: every `ready` row in profile section 6 (not `expected` ones, and not other files that
  happen to be in `inbox/`). Set a row to `done` once its staging files are applied.
- `inbox`: every file in `inbox/`. Match each one to a section 6 row as part of the plan (fill in
  its file name and set it `ready`); offer to add a row for any that don't match.
- An argument narrows it: `confluence`, `jira`, `inbox`, or one path or page.

## Steps

1. **Plan and ask once.** List what you'll read with counts:
   - files in `inbox/`;
   - Confluence pages under each listed page tree (through `searchConfluence` with CQL);
   - Jira epics matching the JQL, with their child counts.
   Give a rough number of staging files. Proceed only after a yes.
2. **Read in batches.**
   - One file at a time, read or converted exactly as `/intake` does (see its "Reading the file"
     table: Office files through `markitdown` when the profile says so, otherwise ask for a PDF).
   - Confluence: at most `sync_max_pages` pages per batch, through `getConfluenceContent`.
   - Jira: at most `sync_max_issues` issues per batch, through `searchJiraIssuesUsingJql` and
     `getJiraIssue`.
   - Read one item at a time rather than in parallel, to stay inside Atlassian's rate limits.
3. **Extract and judge** (pipeline steps 1 and 2). The knowledge base is mostly empty at first, so most
   verdicts will be `new`. Still compare sources with each other: when two documents disagree,
   propose an open question, not two facts.
4. **Stage by source** (pipeline step 3): one staging file per document, per Confluence page tree and
   per Jira epic group. Run the critic on each staging file (pipeline step 4).
   - Number provisional IDs across the whole run (`CAP-new-1` in one file is never reused in
     another; source records are `SRC-new-1`, `SRC-new-2`), and apply the files in order.
   - An item that adds to a page an earlier file proposes is `confirms` or `extends <provisional
     ID>`, with a `Depends on` row naming that file and item.
   - Something two documents raise together (a contradiction between them) goes in the later
     document's staging file, so it can cite both sources once they are applied.
   - Links may point forward to an item later in the same file, with a `Depends on` row.
5. **Structure first.** Propose in this order, so later items can link to earlier ones:
   1. glossary terms;
   2. stakeholders and roles;
   3. entities;
   4. capabilities and processes with their rules;
   5. decisions;
   6. open questions;
   7. risks.
6. **Confirm and apply** each staging file (pipeline steps 5 and 6). Accepted items become
   `confirmed` pages, as in any pipeline run. The BA may accept a whole file at once ("accept all in
   this file as draft"); apply with `status: draft` in that case.
7. **Hand over to `/sync`.** If this run read Jira or Confluence, note the time you started reading
   them. Once the BA has decided every item from those sources, set that time as `last_synced` for
   each in `knowledge/_meta/sync.json`, so the first `/sync` starts where the seed stopped instead of
   asking how far back to go.
8. If more than 200 items would be staged in one run, stop after planning and ask the BA to split the
   work (for example one area at a time).

## Report

- Staging files written, with item counts per file.
- Contradictions between sources, raised as questions.
- Areas from the profile with no material at all, as gaps to fill through elicitation.
- Next: work through the staging files before anything else; then `/sync` daily and `/intake` as
  material arrives.

## Never

- Read Confluence spaces or Jira projects outside the profile.
- Write to Jira or Confluence.
- Mark anything `approved` unless the source records a decision by someone who can decide it.
