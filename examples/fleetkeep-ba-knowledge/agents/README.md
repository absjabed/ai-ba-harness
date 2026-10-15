# `agents/`: the command definitions

Each file here is the canonical definition of one AI BA Harness command, in plain markdown, with no
vendor-specific syntax. Each assistant gets thin wrappers (below) that give the command its name,
description and permissions in that tool, then point here.

**Edit these files. Never put instructions in a wrapper**: a wrapper with its own instructions is a
second copy waiting to drift.

| File | Command | What it does | Writes to Jira or Confluence? |
|---|---|---|---|
| [`setup.md`](setup.md) | `/setup` | Configures the repository for the project | No |
| [`kb-seed.md`](kb-seed.md) | `/kb-seed` | Builds the first knowledge base from existing material | No |
| [`intake.md`](intake.md) | `/intake` | Turns new material or this conversation into proposed knowledge | No |
| [`sync.md`](sync.md) | `/sync` | Turns new Jira and Confluence activity into proposed knowledge | No (reads only) |
| [`requirements.md`](requirements.md) | `/requirements` | Writes the requirement document for an epic or topic | No |
| [`review.md`](review.md) | `/review` | Quality report on a document, an issue, or the knowledge base; changes nothing but its report unless the BA asks | No |
| [`backlog.md`](backlog.md) | `/backlog` | Creates the epic and stories in Jira after approval | **Yes**, after approval |
| [`ask.md`](ask.md) | `/ask` | Answers questions from the knowledge base with citations | No; it has no write, shell or sub-agent tools |
| [`_knowledge-pipeline.md`](_knowledge-pipeline.md) | (shared) | Extract, judge, stage, critique, confirm, apply: used by `/kb-seed`, `/intake`, `/sync`, `/requirements` | No |
| [`improve-harness.md`](improve-harness.md) | `/improve-harness` | Works out what isn't working, decides whether it's a setting, knowledge or a harness change, writes a proposal, and applies safe changes locally after a yes | No |
| [`_critic.md`](_critic.md) | (shared) | The second look at a staging file before the BA decides: pipeline step 4 | No; it writes nothing |

## Wrappers, one set per assistant

| Assistant | Commands | Read-only agents | Settings |
|---|---|---|---|
| Claude Code | `.claude/commands/<name>.md`, run as `/<name>` | `.claude/agents/critic.md` | `.claude/settings.json`, `.mcp.json`, `CLAUDE.md` |
| OpenCode | `.opencode/commands/<name>.md`, run as `/<name>` | `.opencode/agents/critic.md`, `.opencode/agents/kb-reader.md` (runs `/ask`) | `opencode.json`, `AGENTS.md` |
| Codex | `.agents/skills/<name>/SKILL.md`, run as `$<name>` | `.codex/agents/critic.toml` | `.codex/config.toml`, `.codex/rules/`, `.codex/hooks.json`, `AGENTS.md` |
| Any other | none; ask it to "run intake" and it reads the definition | none | `AGENTS.md` |

Each wrapper only names the command and points here. `python tools/kb.py check` fails when a
command is missing from an assistant's folder, or when a wrapper doesn't point at its definition.
A team that never uses one of the assistants can delete that assistant's folder and file.

## Safety, in layers

1. **The definitions** tell each command to preview, stage and wait for a yes. This layer works in
   every assistant; for one without settings in this repository it's the only layer, which is why
   `AGENTS.md` repeats the rules that matter most.
2. **Each assistant's settings** ask before every Jira or Confluence write and every `git push`, and
   refuse Jira and Confluence deletes, force pushes, hard resets and `git clean`:

   | | Claude Code | OpenCode | Codex |
   |---|---|---|---|
   | Jira and Confluence reads | allowed per command (`allowed-tools`) | allowed by name | run without asking when the server marks them read-only |
   | Jira and Confluence writes | ask (matched by verb, such as `create*`, `edit*`) | ask (every tool not listed as a read) | ask (every tool not marked read-only; `executeWrite` always) |
   | Jira and Confluence deletes | denied | denied | `executeDestructive` switched off |
   | `git push` | ask | ask | ask |
   | Force push, hard reset, `git clean`, `git branch -D` | denied | denied | forbidden (rules match the start of a command only) |
   | Changing the harness's own files | ask (`.claude/`) | ask (all harness folders) | inside the sandbox; the definitions forbid it |
   | `/ask` | can't write, run commands or start agents | runs as `kb-reader`, which can't either | the definition forbids it |
   | Takes effect | when the folder opens | when the folder opens | only after you trust the project (and the hook with `/hooks`) |

   The rules cover the repository's own `atlassian` server, and in Claude Code also the Atlassian
   plugin (`mcp__plugin_atlassian_atlassian__`). Any other Atlassian connection isn't covered, which
   is why `/setup` asks you to use the repository's server.

   The rules match commands as assistants normally write them; a deliberately unusual form (such as
   `git -C . push`) isn't matched. That's why only the narrow git commands the commands need are
   pre-approved (`git pull --ff-only`, `git add`, `git commit`, and read-only ones), so anything else
   prompts. Deleting a file (a staging file after applying, an inbox file after your yes) isn't
   pre-approved either, so your assistant asks; that prompt is expected.
3. **The critic** can only read: it checks every staging file and reports, and the command decides
   what to change.
4. **`tools/kb.py check`** and the GitHub workflow catch broken links, bad properties, unknown IDs
   and out-of-date registers on every push.
5. **`tools/kb-sync.sh`** keeps each copy current, so nobody stages work against an old knowledge
   base: Claude Code and Codex run it when a session starts, OpenCode with each command.
