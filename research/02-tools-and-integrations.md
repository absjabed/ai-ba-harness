# Tools and integrations a BA harness can use

Research note, October 2026. Everything below is reached from Claude Code through MCP servers.
Items I could not verify against official pages are marked [unverified].

## Trackers, wikis and boards

| System | MCP server | Official | Main tools | Auth | Caveats |
|---|---|---|---|---|---|
| Jira + Confluence Cloud | Atlassian Rovo MCP server, `https://mcp.atlassian.com/v2/mcp` (`/v1/mcp` still works; `/v1/sse` stopped after 30 June 2026) | Yes | See the Atlassian section below | OAuth 2.1, or an API token if an admin enables it | Cloud only; per-site rate limits; draws on Rovo credits |
| Jira / Confluence Data Center | `sooperset/mcp-atlassian` | Community (MIT, about 6k stars, about 98 tools) | `jira_search`, `jira_get_issue`, `jira_create_issue`, `jira_update_issue`, `jira_transition_issue`, `confluence_search`, `confluence_get_page`, `confluence_create_page`, `confluence_update_page`, `confluence_add_comment` | API token (Cloud) or personal access token (DC) | Self-hosted; Jira DC 8.14+, Confluence DC 6.0+; no release tags, 172 open issues |
| Azure DevOps | Remote `https://mcp.dev.azure.com/{org}` (GA 5 Aug 2026) or local `microsoft/azure-devops-mcp` | Yes | Work items, boards, wiki, test plans, search, repos, pipelines | Entra ID | Claude Code cannot use the remote server yet; use the local one [tool names unverified] |
| Linear | `https://mcp.linear.app/mcp` (also `/mcp/readonly`) | Yes | Issues, projects, comments | OAuth 2.1 or API key | Linear says coverage is incomplete |
| GitHub Issues / Projects | `https://api.githubcopilot.com/mcp/` | Yes | Issues, sub-issues, Projects v2, labels, discussions; a read-only flag | OAuth or PAT | |
| Notion | Hosted server | Yes | Search, fetch, create and update pages, query databases, comments, meeting notes | OAuth | Standard API rate limits [endpoint unverified] |
| Google Drive / Docs | Google Workspace MCP servers, developer preview (May 2026) | Yes (preview) | Drive fetch, list, upload, permissions | Google OAuth; project enrolment | Docs/Sheets/Slides coverage unclear |
| SharePoint / Microsoft 365 | Work IQ MCP (GA), one endpoint with generic tools | Yes | Discover and query M365 content | Entra; M365 Copilot licence and admin consent | Claude Code support not verified; community fallback uses Graph |
| Miro | `https://mcp.miro.com/` | Yes | Summarise and search boards, build boards, generate diagrams, act on comments | OAuth 2.1 | Interactive consent only [tool names unverified] |
| Lucid | Lucid MCP server | Yes | Search and fetch documents, create diagrams including BPMN shapes and swimlanes | OAuth 2.0 | [endpoint and tool names unverified] |
| draw.io | `https://mcp.draw.io/mcp` or `@drawio/mcp` | Yes (jgraph) | `create_diagram` from draw.io XML, CSV or Mermaid; `search_shapes` | None | Can be self-hosted |
| Figma | `https://mcp.figma.com/mcp` | Yes | Design context, screenshots, FigJam diagrams from Mermaid | OAuth | Write tools are remote-only; seat type matters |

## The Atlassian server in detail

This is the integration that matters most for this team.

**Jira tools.**

- Read: `getJiraIssue`, `listJiraIssueComments`, `listJiraIssueTransitions`, `listJiraIssueLinkTypes`,
  `listJiraIssueChangelogs`, `lookupJiraAccountId`, `listJiraIssueAssignableUsers`,
  `downloadJiraIssueAttachment`.
- Search: `searchJiraIssuesUsingJql`.
- Write: `createJiraIssue`, `editJiraIssue`, `transitionJiraIssue` (also moves issues to a sprint or
  the backlog), `addOrEditJiraIssueComment`, `createJiraIssueLink`, `createJiraIssueRemoteIssueLink`,
  `convertJiraIssueHierarchy`, `uploadAttachmentToJiraIssue`, `addOrEditJiraIssueWorklog`.

**Confluence tools.** `getConfluenceContent` (returns Markdown), `searchConfluence` (CQL),
`createConfluenceContent` (pages, blogs, whiteboards, databases, folders), `updateConfluenceContent`
(full replacement or granular edits) and `createConfluenceComment`. Rovo `search` (beta) searches
across products semantically.

**v2 tool exposure.** Only "primary" tools are exposed directly. Others, such as
`listJiraProjects`, `listJiraProjectIssueTypesMetadata` and `getJiraIssueTypeMetaWithFields`, go
through `discover` and `execute`. Atlassian's own skill warns that wrong parameter names in those
calls are dropped silently, so a call can look successful when it isn't. A harness must read the
result back to confirm.

**Limits that shape the design.**

- There is no bulk create. Issues are created one at a time, and children need the parent to exist
  first (`parent=`), so an epic is created before its stories.
- Required or custom fields can block creation. Look them up first with
  `getJiraIssueTypeMetaWithFields`, which is a good job for project setup.
- Delete tools are off by default and need an admin.
- Confluence attachment upload returns a curl command instead of uploading.
- Every call runs with the signed-in user's own permissions, and activity is audited under "Rovo MCP
  User Actions". API-token auth is off by default.
- Rate limits per site, from a marketing page and community posts: Free 500 calls an hour,
  Standard 1,000, Premium and Enterprise 1,000 plus 20 per user up to 10,000. Calls also use Rovo
  credits. One GitHub issue reports 429 errors after about 20 parallel calls, so writes should be
  sequential.
- Cloud only. Data Center needs a community server.

**Atlassian's own Claude skills** (in `atlassian/atlassian-mcp-server/skills`, targeting v2):

| Skill | What it does |
|---|---|
| spec-to-backlog | Reads a Confluence spec, proposes one epic and about 3 to 10 tasks, waits for confirmation, then creates the epic and children; asks again above 15 tickets |
| capture-tasks-from-meeting-notes | Pulls action items out of notes, looks up account IDs, creates Jira tasks |
| generate-status-report | Runs JQL, groups by status and priority, publishes a report to Confluence |
| triage-issue | Searches for duplicates with several JQL queries, then comments on an existing issue or creates a bug, as the user chooses |
| search-company-knowledge | Searches Rovo, then CQL and JQL, and answers with citations |
| jira-sprint-dashboard | Builds a visual sprint dashboard |

These are generic. They know nothing about a project's glossary, conventions or traceability, but
they show the confirmation and duplicate-search steps Atlassian itself considers necessary.

## Meeting and elicitation inputs

| Source | MCP | Notes |
|---|---|---|
| Fireflies | Official, `https://api.fireflies.ai/mcp` | Reads transcripts and summaries |
| Otter | Reported official, `mcp.otter.ai/mcp` | Three read-only tools; REST API is Enterprise-only |
| Zoom | Zoom-hosted server | Transcripts need cloud recording or AI Companion [tool names unverified] |
| Microsoft Teams | No dedicated transcript MCP confirmed | Graph `onlineMeetings/{id}/transcripts` needs `OnlineMeetingTranscript.Read.All` |
| Google Meet | No dedicated MCP | The transcript lands in a Google Doc readable through Drive |
| Notion AI notes | Via the Notion server | `notion-query-meeting-notes` |

The practical default for Teams and Meet is for the BA to export the transcript (`.vtt` or `.docx`)
or paste notes into an inbox folder.

## Diagrams as code

| Format | Good for | Renders in |
|---|---|---|
| Mermaid | Flowcharts, sequence, state, ER, journey, timeline | GitHub natively; Azure DevOps wiki (with limits); **not Confluence Cloud** without a Marketplace app (Mermaid Macros, Merfluence, Diagram Lens); FigJam via Figma's `generate_diagram`; draw.io can import it |
| PlantUML | Activity diagrams with swimlanes, use cases, sequence | Needs a PlantUML server or Kroki |
| BPMN 2.0 XML | Real BPMN process maps | bpmn-js, Kroki, Camunda, Lucid, draw.io |
| draw.io XML | Anything, editable by BAs | draw.io MCP, draw.io for Confluence [app not verified] |

Mermaid has no real BPMN; subgraphs only approximate swimlanes. For process maps that business
stakeholders will review in Confluence, draw.io (via its MCP or the Confluence app) or BPMN XML is
the safer target. Mermaid suits the git-tracked copy.

## Claude Code features that matter here

- **Skills and commands:** `.claude/commands/x.md` and `.claude/skills/x/SKILL.md` both create `/x`.
  Skill frontmatter supports `allowed-tools`, `disable-model-invocation` and forked context.
- **Sub-agents** in `.claude/agents/*.md`, with their own tool lists.
- **Hooks** (33 events; types include command, http, mcp_tool, prompt and agent). A `PreToolUse`
  hook on `mcp__atlassian__createJiraIssue` could enforce an approval rule.
- **Permissions** in `settings.json` can mark tools `allow`, `ask` or `deny`. Setting every
  Atlassian write tool to `ask` gives a native approval prompt with no bash dependency. That
  matters for BAs, who are less likely than developers to have bash set up.
- **Plugins** bundle skills, agents, hooks and `.mcp.json`, installed at user, project or local
  scope through a marketplace. Each enabled skill's description uses context on every turn.

## Sources

- https://github.com/atlassian/atlassian-mcp-server (and its `skills/` folder)
- https://support.atlassian.com/atlassian-rovo-mcp-server/docs/supported-tools/
- https://support.atlassian.com/atlassian-rovo-mcp-server/docs/use-atlassian-rovo-mcp-server/
- https://www.atlassian.com/platform/rovo-mcp
- https://community.atlassian.com/forums/Rovo-questions/Clarification-on-Atlassian-Rovo-MCP-Server-Rate-Limits-10-000/qaa-p/3264375
- https://github.com/atlassian/atlassian-mcp-server/issues/171
- https://github.com/sooperset/mcp-atlassian
- https://github.com/microsoft/azure-devops-mcp
- https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-ga/
- https://linear.app/docs/mcp
- https://github.com/github/github-mcp-server
- https://developers.notion.com/docs/mcp-supported-tools
- https://workspaceupdates.googleblog.com/2026/05/agent-tools-and-security-updates-for-workspace-developers.html
- https://learn.microsoft.com/microsoft-agent-365/tooling-servers-overview
- https://developers.miro.com/docs/miro-mcp
- https://learn.microsoft.com/en-in/connectors/lucidmcpserver/
- https://cdn.jsdelivr.net/gh/jgraph/drawio-mcp@main/README.md
- https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/
- https://docs.fireflies.ai/getting-started/mcp-configuration
- https://www.scalekit.com/blog/otter-mcp-vs-api
- https://developers.zoom.us/docs/mcp/zoom-mcp-server/
- https://learn.microsoft.com/en-us/graph/api/calltranscript-get
- https://developers.google.com/workspace/meet/api/reference/rest/v2/conferenceRecords.transcripts
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams
- https://learn.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance
- https://marketplace.atlassian.com/apps/1928341778/mermaid-macros-for-confluence
- https://www.npmjs.com/package/bpmn-js
- https://plantuml.com/activity-diagram-beta
- https://code.claude.com/docs/en/plugins, /skills, /hooks, /sub-agents, /mcp
