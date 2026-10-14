# AI BA Harness

A business-analysis workflow for Claude Code. Each project gets a BA knowledge repository: a
knowledge base that grows every day from meetings, documents, Jira and Confluence, and eight
commands that turn it into reviewed requirements and a clean Jira backlog. Anyone on the project can
clone that repository and ask it questions.

It is the project-level companion to the AI Dev Harness (developers) and the AI QA Harness (testers).
The three meet in Jira: the BA harness creates the epics and stories the other two read.

**This repository is the template.** Don't do project work here. Create a project repository from it
with `scripts/new-project.sh`, then follow [SETUP.md](SETUP.md).

> **Start here:** [`docs/index.html`](docs/index.html) is the BA handbook on one page: what the harness
> does, setting up a project, the eight commands, what to run when, the knowledge base, Jira templates
> and troubleshooting. Open it in a browser. To see one project from `/setup` to stories in Jira, read
> [`docs/walkthrough.html`](docs/walkthrough.html).

## What a project gets

| | |
|---|---|
| A knowledge base (`knowledge/`) | Capabilities, processes, entities, glossary, stakeholders, business rules, decisions, open questions; plain markdown that opens as an Obsidian vault |
| Eight commands | `/setup`, `/kb-seed`, `/intake`, `/sync`, `/requirements`, `/review`, `/backlog`, `/ask` |
| Templates | Jira epic, story, task, spike and bug; requirement document; knowledge pages |
| Safety | Nothing reaches the knowledge base, Jira or Confluence without a preview and the BA's yes |
| Automatic sync | Every clone pulls new knowledge when someone opens Claude Code in it |

## Start a project

```bash
scripts/new-project.sh ../acme-ba-knowledge --name "Acme"
```

Then follow [SETUP.md](SETUP.md): create the shared remote, sign in to Atlassian, run `/setup` and
`/kb-seed`.

## What's in this repository

| Path | What it is |
|---|---|
| [`project/`](project) | Everything a project repository receives. Edit the harness here |
| [`scripts/new-project.sh`](scripts/new-project.sh) | Copies `project/` into a new project repository and records the harness version |
| [`examples/fleetkeep-ba-knowledge/`](examples/fleetkeep-ba-knowledge) | A complete, filled-in project repository to learn from |
| [`docs/index.html`](docs/index.html) | The BA handbook |
| [`docs/walkthrough.html`](docs/walkthrough.html) | FleetKeep, from setup to release: one project command by command, including changes after the stories reach Jira |
| [`SETUP.md`](SETUP.md) | Step-by-step setup of a project repository |
| [`design/`](design) | The agreed design: decisions, command definitions, workflow, knowledge-base conventions, Jira templates, layout |
| [`research/`](research) | The research behind the design |
| [`HARNESS_VERSION`](HARNESS_VERSION) · [`CHANGELOG.md`](CHANGELOG.md) | The template's version and history |

## Versioning

`HARNESS_VERSION` is copied into every project repository, and `PROJECT-PROFILE.md` records the
version and commit it started from. When you release a change to the template, bump the version, add
a `CHANGELOG.md` entry and tag the commit `v<version>`:

- **patch** for fixes and wording;
- **minor** for new features projects can use without changes;
- **major** when project repositories must change something.

The sidebars of the handbook and the walkthrough show the same version; update both in the same change.

## Licence

Private repository. All rights reserved. Not licensed for distribution, publication, or use outside
the organisations that hold rights to it.
