# Repository layout: the template and a project's BA repository

There are two kinds of repository.

- **The template** is this folder, `ai-ba-harness`. It is kept in its own private GitHub repository
  and is never used for project work. It holds the harness, the setup guide, the handbook, a worked
  example, and these design notes.
- **A project BA repository**, named `<project>-ba-knowledge` (for example `acme-ba-knowledge`), is created from the template once per
  project. The BAs work in it, and teammates clone it to ask questions.

## The template

```text
ai-ba-harness/
├── README.md                     what the harness is, and how to start a project from it
├── SETUP.md                      step by step: create a project BA repository, run /setup, first week
├── CHANGELOG.md                  harness releases
├── HARNESS_VERSION               e.g. 1.0.0; copied into every project, never edited there
├── docs/
│   └── index.html                the BA handbook: one page, opens in a browser
├── scripts/
│   └── new-project.*             copies the right files into a new project repository (like the QA harness export)
├── research/                     the research behind the design (template only)
├── design/                       these notes (template only)
├── examples/
│   └── <sample-project>/         a complete, filled-in project BA repository to learn from
└── project/                      everything below is what a project repository receives
    ├── PROJECT-PROFILE.md
    ├── CLAUDE.md                 tells Claude to start from knowledge/index.md and follow the conventions
    ├── AGENTS.md                 the same for OpenCode, Codex and any other assistant
    ├── opencode.json             OpenCode: Atlassian server, ask and deny rules (0.6.0)
    ├── .gitignore                inbox/, Obsidian workspace files, local settings
    ├── .mcp.json                 Atlassian Rovo MCP server (OAuth; no secrets)
    ├── .claude/
    │   ├── settings.json         Atlassian write tools set to "ask"; the knowledge-sync hook
    │   ├── commands/             thin command files pointing at agents/
    │   └── agents/critic.md      the read-only critic
    ├── .opencode/                OpenCode commands and read-only agents (0.6.0)
    ├── .codex/                   Codex settings, command rules, sync hook, critic (0.6.0)
    ├── .agents/skills/           the commands as Codex skills (0.6.0)
    ├── agents/                   the canonical command definitions, plain markdown
    ├── tools/                    kb.py (rebuild, check) and kb-sync.sh (pulls new knowledge)
    ├── templates/
    │   ├── jira/                 epic, story, task, spike, bug
    │   └── requirement.md        requirement document
    │                             (page templates live in knowledge/_meta/templates/, inside the vault)
    ├── knowledge/                the knowledge base skeleton (03-knowledge-base-conventions.md)
    ├── requirements/             empty; one folder per epic is created by /requirements
    ├── trace/
    │   └── map.csv               header row only
    └── inbox/                    empty, with a .gitkeep; gitignored contents
```

Copying from `project/` is done by the `new-project` script. It writes the template version and
commit into `PROJECT-PROFILE.md`, refuses to overwrite existing files, and leaves research, design
notes and examples behind.

## A project BA repository

```text
acme-ba-knowledge/
├── PROJECT-PROFILE.md            filled by /setup
├── CLAUDE.md · AGENTS.md
├── .mcp.json · .gitignore · .claude/ · agents/ · templates/
├── HARNESS_VERSION
├── knowledge/                    grows every day
├── requirements/
│   └── <epic-slug>/
│       ├── requirement.md        FR / NFR items, stories, acceptance criteria, clarifications log
│       ├── review.md             latest /review report
│       └── diagrams/             only diagrams specific to this requirement
├── trace/
│   └── map.csv                   FR id, story id, Jira key, knowledge page, Confluence page
└── inbox/                        raw material for /intake (never committed)
```

## Diagrams

Diagrams live with the page they explain, in one fixed shape, so people and tools can always find
the source and the rendered image.

```text
knowledge/processes/<area>/<process-slug>/
├── PROC-###-<process-slug>.md    the process page: text plus a Mermaid diagram
├── <process-slug>.as-is.drawio   draw.io source (only when it will be published or needs real BPMN shapes)
├── <process-slug>.as-is.svg      exported image, referenced from the page and from Confluence
├── <process-slug>.to-be.drawio
└── <process-slug>.to-be.svg
```

Rules:

1. **Mermaid is the default.** It sits inside the page, diffs cleanly in git, and renders in GitHub
   and in Obsidian.
2. **Add draw.io only when needed:** for Confluence (which doesn't render Mermaid without an add-on)
   or when stakeholders need real BPMN shapes and swimlanes.
3. **Keep source and export together.** Re-export the SVG whenever the `.drawio` changes; the page
   records the export date.
4. **Names:** `<process-slug>.as-is.*` and `<process-slug>.to-be.*`; lowercase, hyphenated, no
   spaces.
5. **Other diagrams** (entity relationships, state machines, context diagrams) are Mermaid inside the
   page. Entity pages sit flat in `knowledge/entities/`, so a draw.io source for one goes in
   `knowledge/assets/` as `<page-id>-<kind>.drawio` with its `.svg` beside it.
6. **Images that aren't diagrams** (screenshots, photos of whiteboards) go in `knowledge/assets/`,
   named `<page-id>-<what>.png`.
