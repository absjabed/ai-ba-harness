# Decisions

Agreed on 14 October 2026, after the research in `../research/`. Each later design note builds on
these. Change a decision here first, then update the notes that depend on it.

| # | Topic | Decision |
|---|---|---|
| 1 | Tracker and wiki | Atlassian Cloud through the official Rovo MCP server (`https://mcp.atlassian.com/v2/mcp`). Jira and Confluence are both confirmed for the first project. Confluence stays a profile switch so later projects without it still work |
| 2 | Meeting inputs | Paste notes or drop exported transcripts in `inbox/` for version 1. A transcript connection (Fireflies, Otter, Zoom) is added later if the team standardises on one |
| 3 | Atlassian's own Claude skills | Borrow their steps (confirm before create, duplicate search); don't run them directly |
| 4 | Repositories | **This folder (`ai-ba-harness`) is the template repository.** It holds the harness, the setup guide and the handbook. Each project gets its **own BA repository**, created from the template |
| 5 | Knowledge base | A `knowledge/` folder inside each project's BA repository. Team members clone that repository; it **syncs automatically** (see `03-knowledge-base-conventions.md`). Confluence is a one-way publishing target for people who don't use the repository |
| 6 | Obsidian | Optional. Knowledge is **stored by Obsidian's rules** (vault-compatible files, properties, links, attachments) and kept compatible with Open Knowledge Format, so either tool can be connected later without migration |
| 7 | Architecture | The QA harness pattern: one `PROJECT-PROFILE.md`, vendor-neutral agent definitions in `agents/`, thin Claude Code command files in `.claude/commands/` |
| 8 | First version | Eight commands: `/setup`, `/kb-seed`, `/intake`, `/sync`, `/requirements`, `/review`, `/backlog`, `/ask`. Each has a written definition (`01-commands.md`) and a place in the run-when guide (`02-workflow-guide.md`) |
| 9 | Requirement notation | User stories with Given/When/Then acceptance criteria; EARS statements for system rules and NFRs. Jira issues are created from fixed templates (`04-jira-templates.md`) |
| 10 | Diagrams | Mermaid inside the markdown pages; draw.io source and an exported SVG next to them for anything published to Confluence. All in a fixed folder structure (`05-repo-layout.md`) |
| 11 | Office documents | Converted at intake: PDF read directly; Word, Excel and PowerPoint through `markitdown` when installed, otherwise saved as PDF. After intake, the raw files can be removed from `inbox/` **only with the user's permission** |
| 12 | Approvals for outward writes | Preview every item, approve per batch, at most 15 items per batch, plus Claude Code's own permission prompt on every Jira and Confluence write tool |
| 13 | Data handling | Covered by the organisation's AI-use policy (confirmed). `inbox/` is gitignored; intake offers to strip personal data before anything is stored |
| 14 | Teammates | Anyone with a clone can use `/ask`, which is read-only. Contributions arrive through the BA (or as a staging file in a pull request) and are accepted by the BA |
| 15 | Internal critics (added in 0.2.0) | A critic re-checks every staging file against its source and the knowledge base before the BA sees it (fresh-context sub-agent where available); `/requirements` pre-checks its draft with `/review`'s rule checks; `/ask` checks each claim against the page it cites. `/backlog` keeps its preview and read-back, and `/review kb` is itself the critic for the knowledge base |

## Naming

- Display name: **AI BA Harness**. Template repository: `ai-ba-harness`.
- Each project's BA repository: **`<project>-ba-knowledge`** (for example `acme-ba-knowledge`). It
  says who maintains it (the BAs) and what everyone else clones it for (the knowledge base).
