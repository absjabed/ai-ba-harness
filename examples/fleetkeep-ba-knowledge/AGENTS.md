# AGENTS.md

Instructions for any AI assistant working in this repository other than Claude Code: OpenCode,
Codex, Copilot, Cursor, Gemini, or anything else that reads an `AGENTS.md`. Claude Code reads
`CLAUDE.md`, which says the same thing.

This is a **project BA knowledge repository**, created from the AI BA Harness. It holds what the
project knows (the knowledge base), the requirement documents, and the commands the business
analysts use to keep both current. It isn't code.

## For every question about the project

Answer exactly as [`agents/ask.md`](agents/ask.md) describes, whether or not the person used the
ask command: start from [`knowledge/index.md`](knowledge/index.md), answer only from the pages in
`knowledge/` and `requirements/`, cite the defining page and ID for every claim, label `draft`
content unconfirmed and never use `superseded` pages, never read `inbox/`, and if the knowledge base
has no answer, say so and suggest a question for the BA instead of answering from general knowledge.

## Running a command

Run a command only when someone asks for it by name. Then read its definition in
[`agents/`](agents) and follow it exactly; the definition is the same for every assistant.

| Command | Definition | OpenCode | Codex | Any other assistant |
|---|---|---|---|---|
| Configure the repository (once) | [`setup.md`](agents/setup.md) | `/setup` | `$setup` | "run setup" |
| Build the first knowledge base | [`kb-seed.md`](agents/kb-seed.md) | `/kb-seed` | `$kb-seed` | "run kb-seed" |
| Turn new material into proposed knowledge | [`intake.md`](agents/intake.md) | `/intake` | `$intake` | "run intake" |
| Turn Jira and Confluence activity into proposed knowledge | [`sync.md`](agents/sync.md) | `/sync` | `$sync` | "run sync" |
| Write a requirement document | [`requirements.md`](agents/requirements.md) | `/requirements` | `$requirements` | "run requirements" |
| Check a document, an issue or the knowledge base | [`review.md`](agents/review.md) | `/review` | `$review` | "run review" |
| Put approved work into Jira | [`backlog.md`](agents/backlog.md) | `/backlog` | `$backlog` | "run backlog" |
| Answer a question with citations | [`ask.md`](agents/ask.md) | `/ask` | `$ask` | any question |
| Change how the harness works | [`improve-harness.md`](agents/improve-harness.md) | `/improve-harness` | `$improve-harness` | "run improve-harness" |

Before a command that changes anything, run `bash tools/kb-sync.sh` once per session unless your
tool already did (Claude Code and Codex run it when a session starts; OpenCode runs it with each
command). It only fast-forwards and says what to do when it can't.

## Rules that hold even when your tool doesn't enforce them

Claude Code, OpenCode and Codex each have settings in this repository that ask before risky steps.
Other assistants have none, so these rules are yours to keep:

- Show a preview and wait for an explicit yes before every write to Jira or Confluence. Writes to
  Jira happen only through the backlog command. No command in this version writes to Confluence.
- Never delete anything in Jira or Confluence.
- Never force-push, `git reset --hard`, `git clean`, `git branch -D` or rewrite history. Ask before
  every `git push`.
- Read [`PROJECT-PROFILE.md`](PROJECT-PROFILE.md) and
  [`knowledge/_meta/conventions.md`](knowledge/_meta/conventions.md) before changing anything.
- Knowledge changes go through the intake, sync or kb-seed commands: proposals in
  `knowledge/_staging/`, then the BA accepts each item. Never edit knowledge pages directly in
  response to a request; stage the change instead. (People may fix typos by hand; you always stage.)
- Never edit the generated files by hand: `knowledge/index.md`, `knowledge/business-rules.md`,
  `knowledge/decisions.md`, `knowledge/open-questions.md`. Commands rebuild them with
  `python tools/kb.py rebuild` (or by hand to conventions section 12 when Python isn't available).
- Never commit anything in `inbox/`.
- Don't change the harness's own files (`.claude/`, `.opencode/`, `.codex/`, `.agents/`,
  `opencode.json`, `.mcp.json`, `agents/`) except through the improve-harness command.

If you aren't one of the BAs who maintain this repository, don't run the commands that change it.
To suggest a change, send the material to the BA or open a pull request that only adds a file under
`knowledge/_staging/`.
