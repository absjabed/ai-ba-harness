# Open Knowledge (`okn`): evaluation

Evaluation note, October 2026. Question: could Open Knowledge (openknowledge.sh) replace Obsidian
for the BA harness's knowledge base, and do we need a tool like this at all? Nothing was installed;
this is from the project's site, docs, GitHub page and changelog.

## What it is

A command-line tool, `okn`, that manages a folder of markdown as a knowledge base "your agents can
use". It is a different kind of thing from Obsidian. Obsidian is an editor and viewer for people.
`okn` is tooling around a markdown folder: validation, search, an MCP server and publishing. It has
a simple browser viewer of its own.

| Command | What it does |
|---|---|
| `okn setup` | Adopts an existing markdown folder (default `Wiki/`) or makes a managed copy; can add minimal frontmatter; shows its plan before writing |
| `okn search` | Local search that returns file, line range and a content hash for each hit |
| `okn view` | Local browser viewer for reading and editing; agents can propose edits there, and a person reviews the diff before saving |
| `okn check` / `okn validate` | Structure, links, and (when configured) freshness, retrieval and claim checks |
| `okn mcp` | A read-only MCP server any MCP client can use (Claude Code, Codex, OpenCode) |
| `okn publish` | Static HTML viewer, `llms.txt` and a connect manifest |
| Knowledge CI and a "production runtime" | Optional extras: checks on pull requests, drift watching, retrieval evaluations, a served MCP endpoint with rollback |

The format is Open Knowledge Format (OKF), which Google Cloud published in June 2026 to formalise
Karpathy's "LLM Wiki" idea. OKF is plain markdown plus YAML frontmatter, and the only required field
is `type`. Version 0.2 also requires ISO 8601 timestamps with an explicit offset.

## The facts that matter for us

| Point | Finding |
|---|---|
| Licence | Apache-2.0; no account, server or model needed |
| Runtime | A downloaded binary (`curl … \| bash`) or an npm wrapper (Node 20+) |
| Windows | The site lists macOS and Linux. Windows isn't mentioned anywhere I could find. Our team works on Windows, so this is the first thing to test |
| Maturity | v0.3.0 on 20 June 2026, v0.14.0 on 11 October 2026: 12 releases in four months. 65 stars, 8 forks, 21 open pull requests. Maintainers aren't named |
| Breaking changes | Frequent: v0.7 renamed commands (`new` → `scaffold`, `to` → `export`, `agents` → `jobs`), v0.10 removed commands and moved the config file, v0.13 changed the timestamp format |
| Telemetry | On by default; turned off with `--no-telemetry` |
| Search method | Not documented (the docs say it returns scored local results; whether that is keyword or semantic isn't stated) |
| MCP | Read-only; tool names aren't listed in the docs I could read |

## Compared with our design and with Obsidian

| Need | Our design without extra tools | Obsidian | `okn` |
|---|---|---|---|
| A BA adds knowledge safely | `/intake` and `/sync`, staged and approved | Manual editing | Agent edits reviewed in its viewer, but no intake or judging step |
| Asking questions with citations | `/ask` in Claude Code, citing page and ID | Search only | `okn search` (file and line citations) and the read-only MCP server |
| Teammates using other AI tools (Claude Desktop, Codex) | `AGENTS.md` if they clone the repo | No | Yes, through `okn mcp`: its clearest advantage |
| Browsing and editing for people | Any markdown viewer; GitHub | Best: graph, backlinks, editor | A basic local viewer |
| Link and structure checks | `/review kb` | Plugins | `okn check` (deterministic; no AI cost) |
| Readers who never clone the repo | Publish to Confluence | Paid Obsidian Publish | Static HTML site with `llms.txt` |
| Setup for a BA | None beyond Claude Code | Install the app, set five settings | Install a binary or Node; unknown on Windows |

## Verdict

**Not in version 1. Keep the knowledge base compatible with it, and evaluate it later.**

1. **We don't need it to start.** The high-value part is the method: the structure, the rules for
   adding knowledge, the intake and confirmation step, and `/ask`. Claude Code reading plain files
   covers search and question answering at the size a project knowledge base reaches in its first
   months. `okn` doesn't do intake, judging or approval, which is the hard part.
2. **It is a reasonable alternative to Obsidian, not a replacement for what Obsidian does.** If the
   team wants something for people to browse and edit, Obsidian is better. If the team wants
   machine-checkable structure, a read-only MCP endpoint and a static published site, `okn` is the
   better fit.
3. **Three things argue against adopting it now:**
   - Windows support is unconfirmed, and we work on Windows.
   - It is four months old, with breaking changes in most minor releases.
   - It adds an install for BAs, which works against keeping setup simple.
4. **Making our knowledge base OKF-compatible costs almost nothing.** The planned frontmatter already
   has a `type` field, and pages are plain markdown with standard links. To keep the door open:
   - write `updated` and approval dates as ISO 8601 with an offset;
   - avoid any frontmatter that OKF reserves (to check against the spec when we build).

**When to look at it again:**

- teammates or production agents need to query the knowledge base from tools other than Claude Code;
- we want a published site without Confluence;
- the knowledge base passes a few hundred pages and we want deterministic link and freshness checks
  in CI.

If we do, the test should cover installing on Windows, a pinned version, telemetry turned off, and
running `okn check` and `okn mcp` against a copy of a real project knowledge base.

## Do we need a tool like Obsidian or `okn` at all?

Helpful, not essential. Neither one makes the knowledge base more correct; the intake rules and the
confirmation step do that. Both make it easier to use in different ways:

- Obsidian helps people browse and edit, through the graph, backlinks and properties view.
- `okn` helps machines and other tools use it, through checks, an MCP endpoint and a published site.

The design works without either. A team can add Obsidian on day one at no risk, because the harness
ships its settings. `okn` waits until there is a concrete need for one of the three triggers above.

## Sources

- https://openknowledge.sh/ (product page)
- https://openknowledge.sh/wiki/ and https://openknowledge.sh/getting-started/ (docs)
- https://openknowledge.sh/wiki/changelog/cli.html (changelog, v0.3.0 to v0.14.0)
- https://github.com/openknowledge-sh/openknowledge (repository)
- Open Knowledge Format: https://github.com/GoogleCloudPlatform/knowledge-catalog (spec at `okf/SPEC.md`) and
  https://www.noqta.tn/en/news/google-cloud-open-knowledge-format-okf-ai-agents-2026 (secondary)
