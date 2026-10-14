# AGENTS.md

Instructions for any AI assistant working in this repository: Copilot, Cursor, Codex, Gemini, or
anything else that reads an `AGENTS.md`. Claude Code reads `CLAUDE.md`, which says the same thing.

This repository is a project's business-analysis knowledge base. It isn't code.

## Answering questions

1. Start from `knowledge/index.md`, the catalogue of every page.
2. Search `knowledge/` for the question's terms and their synonyms (the `aliases` property on pages,
   and the glossary).
3. Answer only from the pages. Cite the page and its ID (for example `CAP-012`, `BR-104`, `DEC-007`)
   for every claim.
4. Report each source's status from its `status` property:
   - `draft` means unconfirmed;
   - `confirmed` means a BA checked it;
   - `approved` means a named stakeholder agreed.
   Ignore `superseded` pages.
5. If the knowledge base has no answer, say so. Do not answer from general knowledge. Suggest the
   question be sent to the BA.

## Changing anything

Don't. This repository's content is maintained by the business analysts through the AI BA Harness
commands, which check sources, contradictions and approvals before anything is stored. To suggest a
change, send the material to the BA or open a pull request that only adds a file under
`knowledge/_staging/`.

Never commit files from `inbox/`, and never edit `knowledge/index.md` or the generated registers.
