# CLAUDE.md

This is a **project BA knowledge repository**, created from the AI BA Harness. It holds what the
project knows (the knowledge base), the requirement documents, and the commands the business
analysts use to keep both current.

## For every question about the project

Answer exactly as [`agents/ask.md`](agents/ask.md) describes, whether or not the person typed
`/ask`: start from [`knowledge/index.md`](knowledge/index.md), answer only from the pages, cite every
claim, say how sure each source is, and say plainly when the knowledge base doesn't know.
`/ask` does the same with no tools that write files, run commands or change Jira.

## Before changing anything

- Read [`PROJECT-PROFILE.md`](PROJECT-PROFILE.md) and
  [`knowledge/_meta/conventions.md`](knowledge/_meta/conventions.md).
- Knowledge changes go through `/intake`, `/sync` or `/kb-seed`: proposals in `knowledge/_staging/`,
  then the BA accepts each item. Never edit knowledge pages directly in response to a request; stage
  the change instead. (People may fix typos by hand; you always stage.)
- Never edit the generated files by hand: `knowledge/index.md`, `knowledge/business-rules.md`,
  `knowledge/decisions.md`, `knowledge/open-questions.md`. Commands rebuild them with
  `python tools/kb.py rebuild` (or by hand to conventions section 12 when Python isn't available).
- Never commit anything in `inbox/`.
- Writes to Jira happen only through `/backlog`, after a preview and an explicit yes. No command in
  this version writes to Confluence.

## Commands

| Command | Use it to |
|---|---|
| `/setup` | Configure this repository for the project (once) |
| `/kb-seed` | Build the first knowledge base from existing material |
| `/intake` | Turn notes, documents or this conversation into proposed knowledge |
| `/sync` | Turn new Jira and Confluence activity into proposed knowledge |
| `/requirements` | Write a requirement document for an epic or topic |
| `/review` | Check a requirement document, a Jira issue, or the knowledge base (`/review kb`) |
| `/backlog` | Put approved work into Jira: stories from a reviewed requirement (and later changes to them), or a single task, spike or UAT bug |
| `/ask` | Answer a question from the knowledge base, with citations |
| `/improve-harness` | Change how the harness works: a setting, or a proposal for the harness itself |

The definition of each command is in [`agents/`](agents).
