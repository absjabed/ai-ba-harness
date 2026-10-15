# AI BA Harness

**A business-analysis harness layer for Claude Code, OpenCode and Codex:** commands, agents and a project knowledge base that sit on top of the assistant's own agent runtime.

Each project gets a BA knowledge repository. Its knowledge base grows every day from meetings, documents, Jira and Confluence, and
nine commands turn it into reviewed requirements and a clean Jira backlog. Anyone on the project can
clone that repository and ask it questions.

It works at project level alongside two other harnesses: the AI Dev Harness for developers and the
AI QA Harness for testers. The three meet in Jira, where the BA harness creates the epics and stories
the other two read.

This repository is the template, so don't do project work in it. Create a project repository with
`scripts/new-project.sh`, then follow [SETUP.md](SETUP.md).

> The BA handbook is a single page, [`docs/index.html`](docs/index.html). It covers what the
> harness does, setting up a project, a worked example of every command on one project (from `/setup`
> to `/ask`), what to run when, the knowledge base, Jira templates and troubleshooting. Open it in a
> browser. To share the worked example with a team, use its own page,
> [`docs/walkthrough.html`](docs/walkthrough.html).

## What a project gets

| | |
|---|---|
| A knowledge base (`knowledge/`) | Capabilities, processes, entities, glossary, stakeholders, business rules, decisions, open questions; plain markdown that opens as an Obsidian vault |
| Nine commands | `/setup`, `/kb-seed`, `/intake`, `/sync`, `/requirements`, `/review`, `/backlog`, `/ask`, `/improve-harness` |
| A knowledge base tool | `tools/kb.py`: rebuilds the index and registers, checks links, properties and IDs; a GitHub workflow runs the check on every push |
| Templates | Jira epic, story, task, spike and bug; requirement document; knowledge pages |
| Safety | Nothing reaches the knowledge base, Jira or Confluence without a preview and the BA's yes |
| Automatic sync | Every clone pulls new knowledge when someone opens Claude Code or Codex in it, or runs an OpenCode command |
| Three assistants | Claude Code, OpenCode and Codex each get the nine commands and the same safety settings; any other assistant follows `AGENTS.md` |

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
| [`scripts/build-walkthrough.py`](scripts/build-walkthrough.py) | Rebuilds `docs/walkthrough.html` from the handbook's "Follow a whole project" section |
| [`examples/fleetkeep-ba-knowledge/`](examples/fleetkeep-ba-knowledge) | A complete, filled-in project repository to learn from |
| [`examples/fleetkeep-demo-test/`](examples/fleetkeep-demo-test/DEMO-TEST.md) | The raw output of the 0.5.0 demo test, kept as it was left (see `research/08-demo-test.md`) |
| [`examples/fleetkeep-demo-test-2/`](examples/fleetkeep-demo-test-2/DEMO-TEST.md) | The raw output of the second demo test, with two BAs and a developer (see `research/09-second-demo-test.md`) |
| [`docs/index.html`](docs/index.html) | The BA handbook |
| [`docs/walkthrough.html`](docs/walkthrough.html) | The handbook's worked example as a page of its own, for sharing with a team. Generated: don't edit it |
| [`SETUP.md`](SETUP.md) | Step-by-step setup of a project repository |
| [`design/`](design) | The agreed design: decisions, command definitions, workflow, knowledge-base conventions, Jira templates, layout |
| [`research/`](research) | The research behind the design |
| [`HARNESS_VERSION`](HARNESS_VERSION) · [`CHANGELOG.md`](CHANGELOG.md) | The template's version and history |

## Versioning

`HARNESS_VERSION` is copied into every project repository, and `PROJECT-PROFILE.md` records the
version and commit it started from. When you release a change to the template, bump the version, add
a `CHANGELOG.md` entry and tag the commit `v<version>`:

- patch for fixes and wording;
- minor for new features projects can use without changes;
- major when project repositories must change something.

The handbook's sidebar shows the same version, so update it in the same change. Then run
`python scripts/build-walkthrough.py`, which copies the new version and any edits to the worked
example into the walkthrough page.

## License

MIT. See [`LICENSE`](LICENSE): you may use, copy, change and share the harness freely, as long as the
copyright and license notice stays with it.

The harness files a project copies from `project/` stay under MIT. What a project writes with them
(its knowledge base, requirements and profile) belongs to that project.
