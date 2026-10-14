# Setting up a project

From this template to a working BA knowledge repository that the whole project team can use. Budget
an hour for steps 1 to 5, plus however long the first `/kb-seed` review takes.

## What you need

| Need | Why |
|---|---|
| Claude Code (CLI, desktop app or IDE extension), signed in | Runs the commands |
| Git, with Git Bash on Windows | The repository, the copy script and the automatic sync. Git for Windows includes Git Bash |
| Access to the project's Jira (and Confluence, if used) on Atlassian Cloud | The commands read from them, and `/backlog` creates issues |
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

Open Claude Code in the repository folder (`claude`), then:

1. Run `/mcp`, choose `atlassian`, and sign in in the browser window that opens. This uses your own
   Atlassian account and permissions; no token is stored in the repository.
2. Approve the connection for your site. If your Atlassian admin restricts connected apps, they may
   need to allow it first.

## 4. Run `/setup`

`/setup` interviews you and fills `PROJECT-PROFILE.md`:

- the Jira project and the issues that count as "ours";
- Confluence spaces;
- the business areas, stakeholders and who can decide what;
- the fields Jira requires when creating issues.

It reads Jira to find required fields and offers what it finds. Have these ready:

- **Jira:** the project key or keys, and how you tell your team's issues apart (labels, components,
  issue types).
- **Confluence:** the spaces that hold project knowledge, and the page under which published
  knowledge should go.
- **Business areas:** the four to eight areas the product divides into.
- **Stakeholders:** the main stakeholders by role, and what each one can decide.
- **Existing material:** what already exists (documents, page trees, epics).

## 5. Seed the knowledge base

1. Put existing documents in `inbox/` (the charter, specs, process documents, glossaries). Office
   files need `markitdown`, or save them as PDF.
2. Run `/kb-seed`. It lists what it will read and asks once, then writes proposals to
   `knowledge/_staging/`.
3. Work through each staging file: accept, edit or reject every item. Accepted items become pages,
   and each batch is committed. The command asks before pushing.

This first pass is the longest review you'll do. After it, daily work is small batches.

## 6. Bring the team in

Send the repository URL to developers, testers and product owners:

> Clone this once, open Claude Code in it, and ask: `/ask <question>`. Your copy updates itself
> whenever you open it.

They need read access to the repository. Atlassian access is optional for them; without it, `/ask`
answers from the knowledge base only.

## 7. Daily rhythm

| When | Run |
|---|---|
| Start of the day | `/sync` |
| After each meeting or new document | `/intake inbox/<file>` |
| End of a working session with Claude | `/intake` |
| Per epic | `/requirements`, then `/review`, then `/backlog` |
| Weekly | `/review kb` |

The handbook ([`docs/index.html`](docs/index.html)) has the full guide.

## Optional: open the knowledge base in Obsidian

Open the `knowledge/` folder as a vault. The shipped settings (`knowledge/.obsidian/app.json`) keep
links in standard markdown, so nothing changes for anyone else. To stay in sync without opening
Claude Code, either:

- install the Obsidian Git community plugin and set an auto-pull interval (for example 30 minutes);
- or schedule a daily pull, for example in Windows Task Scheduler:
  `git -C "<path to repository>" pull --ff-only`.

Add knowledge through `/intake`, not by typing into pages. Fixing a typo or wording by hand is fine
as long as the meaning stays the same; add a `log.md` line with the command `EDIT`.

## Optional: turn the automatic sync off

Set `kb_auto_sync: off` in `PROJECT-PROFILE.md` section 5.

## Updating the harness in a project

`PROJECT-PROFILE.md` records the harness version and commit the repository started from. To see what
has changed since, run `git log --oneline v<version>..` in the template. Copy over the files you
want: usually `agents/`, `.claude/`, `templates/`, `knowledge/_meta/conventions.md` and
`knowledge/_meta/templates/`. Never copy `knowledge/_meta/sync.json` (it holds the project's last sync
time), `knowledge/` pages or `PROJECT-PROFILE.md`. Then update `HARNESS_VERSION` in the project.
