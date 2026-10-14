# `agents/`: the command definitions

Each file here is the canonical definition of one AI BA Harness command, in plain markdown, with no
vendor-specific syntax. The files in `.claude/commands/` are thin wrappers. They give the command its
name, description and tool permissions in Claude Code, then point here.

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

## Safety, in layers

1. **The definitions** tell each command to preview, stage and wait for a yes.
2. **The wrapper's `allowed-tools`** pre-approves only the reads and git commands each command needs.
   `/ask` also lists every write tool under `disallowed-tools`, so it can't change anything.
3. **`.claude/settings.json`** puts every Atlassian write tool (matched by verb, such as `create*`,
   `edit*`, `update*`) and `git push` on the "ask" list, so Claude Code prompts before each one even
   inside an approved batch. It denies Atlassian delete tools, `executeDestructive`, force pushes, hard
   resets and `git clean` outright. Ask and deny always win over a command's `allowed-tools`. The
   rules cover the repository's own `atlassian` server and the Atlassian plugin
   (`mcp__plugin_atlassian_atlassian__`). Any other Atlassian connection isn't covered, which is why
   `/setup` asks you to use the repository's server.

   These rules match commands as Claude normally writes them; a deliberately unusual form (such as
   `git -C . push`) isn't matched. That's why each command also pre-approves only the narrow git
   commands it needs (`git pull --ff-only`, `git add`, `git commit`, and read-only ones), so anything
   else prompts. Deleting a file (a staging file after applying, an inbox file after your yes) isn't
   pre-approved either, so Claude Code asks; that prompt is expected.
4. **The critic** (`.claude/agents/critic.md`) can only read: it checks every staging file and
   reports, and the command decides what to change.
5. **`tools/kb.py check`** and the GitHub workflow catch broken links, bad properties, unknown IDs
   and out-of-date registers on every push.

## Using another assistant

The definitions are plain prose, so another assistant can follow them: point it at the file, or
wrap it the way that tool expects. What is Claude Code-specific is only the wrapper format, the
tool names in `allowed-tools`, and the hook.
