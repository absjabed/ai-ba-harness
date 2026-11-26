# Harness docs

Technical references for how the AI BA Harness works, with editable diagrams.

## Guides

| Guide | What it covers |
|-------|----------------|
| [AI BA Harness](ai-ba-harness.md) | How the AI BA Harness works: architecture, the agent pattern across Claude Code, OpenCode and Codex, the BA lifecycle, the knowledge pipeline, requirements and review, backlog, ask, safety layers, changing the harness, concepts, a BA's day and week, and which command to use, with draw.io diagrams. Published as [`../how-it-works.html`](../how-it-works.html). |

## Conventions

- Technical audience; CLI and file-level detail are fine.
- Never put a secret in a guide; use `<placeholders>`.
- Edit the `.md`, then run `python scripts/build-harness-guide.py` to regenerate the HTML page.
