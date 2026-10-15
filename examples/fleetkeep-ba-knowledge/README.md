# FleetKeep BA knowledge

This repository holds what the project knows: how the product works and must work, the business
rules, the decisions made and who made them, the open questions, and the requirements behind the
Jira backlog. The business analysts maintain it with the AI BA Harness, and everyone else can clone
it and ask it questions.

> [!NOTE]
> **This is a worked example.** FleetKeep and Northwind Systems are fictional, and so are every
> stakeholder, meeting, Jira key and Confluence page in it. One staging file,
> [`knowledge/_staging/2026-10-14-intake-defect-triage-call.md`](knowledge/_staging/2026-10-14-intake-defect-triage-call.md),
> is deliberately left pending (its boxes unticked) to show what an `/intake` proposal looks like
> before the BA decides it. See [`EXAMPLE.md`](EXAMPLE.md) for where to start reading.

## Ask a question

1. Clone this repository once: `git clone <repository URL>`.
2. Open your AI assistant in the folder: Claude Code (`claude`), OpenCode (`opencode`) or Codex
   (`codex`).
3. Run `/ask <your question>` (`$ask` in Codex), for example `/ask who can authorise a vehicle's return to service?`

Answers cite the pages they come from and say whether each source is a draft, confirmed by a BA, or
approved by a stakeholder. If the knowledge base doesn't know, `/ask` says so and drafts a question
you can send to the BA.

Your copy updates itself when you open Claude Code or Codex here, and with every OpenCode command.
Other assistants (Copilot, Cursor, Gemini) follow `AGENTS.md` and answer the same way.

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

The AI BA Harness handbook lists the commands and when to run them; [`CLAUDE.md`](CLAUDE.md) and
[`AGENTS.md`](AGENTS.md) have a short version. The rules for the knowledge base are in
[`knowledge/_meta/conventions.md`](knowledge/_meta/conventions.md).

## Suggesting a change

Send the material to the BA, or open a pull request that adds a staging file. To make one, run
`/intake` on your material and it writes the file to `knowledge/_staging/`. The BA accepts or
rejects each item.
