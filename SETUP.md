# Setting up a project

From this template to a working BA knowledge repository that the whole project team can use. Budget
an hour for steps 1 to 5, plus however long the first `/kb-seed` review takes.

## What you need

| Need | Why |
|---|---|
| Claude Code (CLI, desktop app or IDE extension), OpenCode or Codex, signed in | Runs the commands. The steps below use Claude Code; the handbook's "OpenCode and Codex" section has the differences |
| Git, with Git Bash on Windows | The repository, the copy script and the automatic sync. Git for Windows includes Git Bash |
| Access to the project's Jira (and Confluence, if used) on Atlassian Cloud | The commands read from them, and `/backlog` creates issues |
| *(recommended)* Python 3.8 or later | Runs `tools/kb.py`, which rebuilds the index and registers exactly and checks the knowledge base. Without it the commands do the same by hand |
| *(optional)* `markitdown` (`pip install markitdown`) | Lets `/intake` read Word, Excel and PowerPoint directly. Without it, save those files as PDF |
| *(optional)* Obsidian | A nicer way to read the knowledge base. Nothing depends on it |

## 1. Create the repository

From a clone of this template, in Git Bash (Windows) or a terminal:

```bash
scripts/new-project.sh ../<project>-ba-knowledge --name "<Project name>"
```

It copies the harness, records the harness version and commit in `PROJECT-PROFILE.md`, and refuses
to overwrite anything that already exists. If the template has uncommitted changes, it stops; commit
them first.

## 2. Put it under git and share it

```bash
cd ../<project>-ba-knowledge
git init -b main
git add -A
git commit -m "Start from AI BA Harness <version>"
```

Create an empty private repository called `<project>-ba-knowledge` where your team keeps
repositories (GitHub, Azure DevOps, Bitbucket), then:

```bash
git remote add origin <repository URL>
git push -u origin main
```

The automatic sync needs this shared remote.

## 3. Connect Atlassian

Open Claude Code in the repository folder (`claude`). The first time, it asks two things: whether
you trust the folder (yes: that lets the project's settings and the sync hook run), and whether to
use the `atlassian` server from the repository's `.mcp.json` (yes). Then:

1. Run `/mcp`, choose `atlassian`, and sign in in the browser window that opens. This uses your own
   Atlassian account and permissions; no token is stored in the repository.
2. Approve the connection for your site. If your Atlassian admin restricts connected apps, they may
   need to allow it first.

With **OpenCode**, run `opencode mcp auth atlassian` in the repository folder and sign in, then start
`opencode`. With **Codex**, start `codex` in the folder and trust the project (Codex ignores the
repository's settings until you do), run `/hooks` and trust the sync hook, then run
`codex mcp login atlassian` and restart Codex. In Codex, commands start with `$` (`$setup`).

## 4. Run `/setup`

`/setup` interviews you and fills `PROJECT-PROFILE.md`:

- the Jira project, its issue types and the issues that count as "ours";
- Confluence spaces;
- the business areas, stakeholders and who can decide what (a short RACI);
- the fields Jira requires when creating issues;
- the project's preferred words.

It reads Jira to find required fields and offers what it finds. Have these ready:

- **Jira:** the project key or keys, and how you tell your team's issues apart (labels, components,
  issue types).
- **Confluence:** the spaces that hold project knowledge, and the page under which published
  knowledge should go.
- **Business areas:** the four to eight areas the product divides into.
- **Stakeholders:** the main stakeholders by role, what each one can decide, and who signs off
  recurring decisions such as a change to a business rule or release content.
- **Existing material:** what already exists (documents, page trees, epics).
- **House terms:** words the project prefers and words to avoid ("job card", not "work order").

It finishes by showing the whole profile as a diff, writing it after your yes, drafting
`knowledge/stakeholders.md`, creating one folder per business area, committing, and asking before
pushing.

## 5. Seed the knowledge base

Give the BAs write access to the repository first, and everyone else read access.

If little is written down yet, skip `/kb-seed`: hold a discovery workshop and run `/intake` on its
notes. That is how the worked example in `examples/fleetkeep-ba-knowledge/` started.

1. Put existing documents in `inbox/` (the charter, specs, process documents, glossaries). Office
   files need `markitdown`, or save them as PDF.
2. Run `/kb-seed`. It lists what it will read and asks once, then writes proposals to
   `knowledge/_staging/`.
3. Work through each staging file: accept, edit or reject every item. Accepted items become pages,
   and each batch is committed. The command asks before pushing.

This first pass is the longest review you'll do. After it, daily work is small batches. If the
seed read Jira or Confluence, it records where it stopped, so the first `/sync` carries on from there.

## 6. Bring the team in

Send the repository URL to developers, testers and product owners:

> Clone this once, open Claude Code, OpenCode or Codex in it, and ask: `/ask <question>` (`$ask` in
> Codex). Your copy updates itself.

They need read access to the repository. The first time they open Claude Code there, they answer
the same two prompts (trust the folder: yes; the `atlassian` server: yes if they have Atlassian
access, otherwise no). Atlassian access is optional for them; without it, `/ask` answers from the
knowledge base only.

For every command worked through on one project, from `/setup` to `/ask`, read "Follow a whole
project" in the handbook ([`docs/index.html`](docs/index.html#example)), or the same example as a
page of its own to share with the team: [`docs/walkthrough.html`](docs/walkthrough.html).

## 7. Daily rhythm

| When | Run |
|---|---|
| Start of the day | `/sync` |
| After each meeting or new document | `/intake inbox/<file>` |
| End of a working session with your assistant | `/intake` |
| Per epic | `/requirements`, then `/review`, then `/backlog` |
| Weekly | `/review kb` |

The handbook ([`docs/index.html`](docs/index.html)) has the full guide.

## Optional: open the knowledge base in Obsidian

Open the `knowledge/` folder as a vault. The shipped settings (`knowledge/.obsidian/app.json`) keep
links in standard markdown, so nothing changes for anyone else. To stay in sync without opening
an assistant, either:

- install the Obsidian Git community plugin and set an auto-pull interval (for example 30 minutes);
- or schedule a daily pull, for example in Windows Task Scheduler:
  `git -C "<path to repository>" pull --ff-only`.

Add knowledge through `/intake`, not by typing into pages. Fixing a typo or wording by hand is fine
as long as the meaning stays the same; add a `log.md` line with the command `EDIT`.

## Optional: turn the automatic sync off

Set `kb_auto_sync: off` in `PROJECT-PROFILE.md` section 5.

## Improving the harness

When something in the harness should work differently for your project, run `/improve-harness` with
what isn't working. A project setting is changed in the profile; anything else becomes a proposal in
`harness-feedback/`, which you send to whoever maintains the harness (the repository in profile
section 1). Safe changes can also be applied in your project straight away; they are listed in
profile section 8.

**For the harness maintainers:** take the proposal file into the template, apply its change under
`project/`, bring the example and the handbook up to date, bump `HARNESS_VERSION`, add a
`CHANGELOG.md` entry naming the proposal, and tag the release. Tell the project which version
includes it, so they can mark the proposal `accepted`.

## Updating the harness in a project

`HARNESS_VERSION` in the project says which version it runs; profile section 1 records the one it
started from. In the template:

1. **Read what changed:** the `CHANGELOG.md` entries newer than the project's version, oldest
   first (or `git log --oneline v<version>..`).
2. **Copy from the template's `project/` folder:** `agents/`, `.claude/`, `.opencode/`, `.codex/`,
   `.agents/`, `opencode.json`, `templates/`, `tools/`, `.github/`, `CLAUDE.md`, `AGENTS.md`, `knowledge/_meta/conventions.md`,
   `knowledge/_meta/templates/`, and any new folder a CHANGELOG entry names. Never copy
   `knowledge/_meta/sync.json` (the project's last sync times), knowledge pages,
   `PROJECT-PROFILE.md`, `requirements/` or `trace/map.csv`: they hold the project's own content.
3. **Apply each entry's "To update a project" steps,** oldest first: edits to the profile, to the
   template text inside knowledge pages, and to file formats.
4. **Re-apply the local changes** listed in profile section 8 that the new version doesn't already
   include (projects from before 0.5.0 have none).
5. Set `HARNESS_VERSION` to the new version.
6. Run `python tools/kb.py rebuild` and `python tools/kb.py check`.
7. Commit (`harness: update to <version>`) and push. Everyone's clone picks it up the next time they
   open their assistant, and the GitHub check runs on every push from then on.
