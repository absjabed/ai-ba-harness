# `<Project>` BA knowledge

This repository holds what the project knows: how the product works and must work, the business
rules, the decisions made and who made them, the open questions, and the requirements behind the
Jira backlog. The business analysts maintain it with the AI BA Harness, and everyone else can clone
it and ask it questions.

## Ask a question

1. Clone this repository once: `git clone <repository URL>`.
2. Open Claude Code in the folder (`claude`).
3. Run `/ask <your question>`, for example `/ask who can raise a job card?`

Answers cite the pages they come from and say whether each source is a draft, confirmed by a BA, or
approved by a stakeholder. If the knowledge base doesn't know, `/ask` says so and drafts a question
you can send to the BA.

Your copy updates itself whenever you open Claude Code here. Other assistants (Copilot, Cursor,
Codex) follow `AGENTS.md` and answer the same way.

To read the pages directly, start at [`knowledge/index.md`](knowledge/index.md). They render on
GitHub, and the `knowledge/` folder opens as an Obsidian vault.

## What's here

| Folder | Holds |
|---|---|
| [`knowledge/`](knowledge) | The knowledge base: capabilities, processes, entities, glossary, business rules, decisions, open questions, stakeholders |
| [`requirements/`](requirements) | One folder per epic: the requirement document and its review |
| [`trace/`](trace) | Which requirement became which Jira issue and knowledge page |
| `inbox/` | The BA's raw material (never committed) |

## For BAs

The AI BA Harness handbook lists the commands and when to run them; [`CLAUDE.md`](CLAUDE.md) has a
short version. The rules for the knowledge base are in
[`knowledge/_meta/conventions.md`](knowledge/_meta/conventions.md).

## Suggesting a change

Send the material to the BA, or open a pull request that adds a staging file. To make one, run
`/intake` on your material and it writes the file to `knowledge/_staging/`. The BA accepts or
rejects each item.
