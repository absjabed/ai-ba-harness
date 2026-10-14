# CLAUDE.md

This is a **project BA knowledge repository**, created from the AI BA Harness. It holds what the
project knows (the knowledge base), the requirement documents, and the commands the business
analysts use to keep both current.

## For every question about the project

1. Start from [`knowledge/index.md`](knowledge/index.md). It lists every page with one line each.
2. Search `knowledge/` for the question's terms and for their synonyms, which pages list as `aliases`
   and the glossary lists under each term.
3. Answer only from what the pages say, and cite the page and ID for every claim.
4. Say how certain each source is:
   - **draft:** unconfirmed;
   - **confirmed:** checked by a BA;
   - **approved:** agreed by a named stakeholder.
   Never use **superseded** pages.
5. If the knowledge base doesn't answer it, say so. Don't fill the gap from general knowledge; offer
   to draft an open question for the BA instead.

`/ask` does exactly this, with no tools that write files, run commands or change Jira.

## Before changing anything

- Read [`PROJECT-PROFILE.md`](PROJECT-PROFILE.md) and
  [`knowledge/_meta/conventions.md`](knowledge/_meta/conventions.md).
- Knowledge changes go through `/intake`, `/sync` or `/kb-seed`: proposals in `knowledge/_staging/`,
  then the BA accepts each item. Never edit knowledge pages directly in response to a request; stage
  the change instead. (People may fix typos by hand; you always stage.)
- Never edit the generated files: `knowledge/index.md`, `knowledge/business-rules.md`,
  `knowledge/decisions.md`, `knowledge/open-questions.md`. `/review kb` rebuilds them.
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
| `/backlog` | Create the epic and stories in Jira from a reviewed requirement |
| `/ask` | Answer a question from the knowledge base, with citations |

The definition of each command is in [`agents/`](agents).
