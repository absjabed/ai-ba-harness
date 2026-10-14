# FleetKeep BA knowledge

What this project knows: how the product works and must work, the business rules, the decisions
made and who made them, the open questions, and the requirements behind the Jira backlog. The
business analysts maintain it with the AI BA Harness. **Everyone else can clone it and ask it
questions.**

> [!NOTE]
> **This is a worked example.** FleetKeep and Northwind Systems are fictional, and so are every
> stakeholder, meeting, Jira key and Confluence page in it. One staging file,
> [`knowledge/_staging/2026-10-14-intake-defect-triage-call.md`](knowledge/_staging/2026-10-14-intake-defect-triage-call.md),
> is deliberately left pending (its boxes unticked) to show what an `/intake` proposal looks like
> before the BA decides it. See [`EXAMPLE.md`](EXAMPLE.md) for where to start reading.

## Ask a question

1. Clone this repository once: `git clone <repository URL>`.
2. Open Claude Code in the folder (`claude`).
3. Run `/ask <your question>`, for example `/ask who can authorise a vehicle's return to service?`

Answers cite the pages they come from and say whether each source is a draft, confirmed by a BA, or
approved by a stakeholder. If the knowledge base doesn't know, `/ask` says so and drafts a question
you can send to the BA.

Your copy updates itself whenever you open Claude Code here. Other assistants (Copilot, Cursor,
Codex) follow `AGENTS.md` and answer the same way.

You can also read the pages directly: start at [`knowledge/index.md`](knowledge/index.md). They
render on GitHub and open as an Obsidian vault (`knowledge/`).

## What's here

| Folder | Holds |
|---|---|
| [`knowledge/`](knowledge) | The knowledge base: capabilities, processes, entities, glossary, business rules, decisions, open questions, stakeholders |
| [`requirements/`](requirements) | One folder per epic: the requirement document and its review |
| [`trace/`](trace) | Which requirement became which Jira issue and knowledge page |
| `inbox/` | The BA's raw material (never committed) |

## For BAs

The commands and when to run them are in the AI BA Harness handbook, and in short in
[`CLAUDE.md`](CLAUDE.md). The rules for the knowledge base are in
[`knowledge/_meta/conventions.md`](knowledge/_meta/conventions.md).

## Suggesting a change

Send the material to the BA, or open a pull request that adds a staging file (run `/intake` on your
material; it writes one to `knowledge/_staging/`). The BA accepts or rejects each item.
