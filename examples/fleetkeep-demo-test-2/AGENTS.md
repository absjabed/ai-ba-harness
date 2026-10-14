# AGENTS.md

Instructions for any AI assistant working in this repository: Copilot, Cursor, Codex, Gemini, or
anything else that reads an `AGENTS.md`. Claude Code reads `CLAUDE.md`, which says the same thing.

This repository is a project's business-analysis knowledge base. It isn't code.

## Answering questions

Follow `agents/ask.md`, the same instructions the harness's `/ask` command uses. In short: start
from `knowledge/index.md`; answer only from the pages in `knowledge/` and `requirements/`; cite the
defining page and ID for every claim; label `draft` content unconfirmed and never use `superseded`
pages; never read `inbox/`; and if the knowledge base has no answer, say so and suggest a question
for the BA instead of answering from general knowledge.

## Changing anything

Don't. This repository's content is maintained by the business analysts through the AI BA Harness
commands, which check sources, contradictions and approvals before anything is stored. To suggest a
change, send the material to the BA or open a pull request that only adds a file under
`knowledge/_staging/`.

Never commit files from `inbox/`, and never edit `knowledge/index.md` or the generated registers by
hand; `python tools/kb.py rebuild` writes them.
