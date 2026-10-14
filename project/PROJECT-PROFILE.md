# Project profile

**This is the one file a project fills in.** Every command reads it before doing anything. `/setup`
fills it by interview; you can also edit it by hand. Replace every `<...>` placeholder and delete rows
that don't apply. Keep the section headings: the commands look them up by name.

---

## 1. Project

| Field | Value |
|---|---|
| Project name | `<Project name>` |
| One-line purpose | `<What the product does and for whom, in one sentence>` |
| BA repository | `<project>-ba-knowledge` |
| Lead BA (role) | `<e.g. Lead BA>` |
| Other BAs (roles) | `<e.g. BA, Product owner>` |
| Harness version this copy started from | `<filled by scripts/new-project.sh>` |
| Harness commit this copy started from | `<filled by scripts/new-project.sh>` |

## 2. Atlassian

| Field | Value |
|---|---|
| Atlassian site | `<your-site>.atlassian.net` |
| Cloud ID | `<filled by /setup from getAccessibleAtlassianResources>` |
| Jira project key(s) | `<e.g. PROJ>` |
| Issue key format | `<e.g. PROJ-1234>` |
| Scope JQL for `/sync` | `<e.g. project = PROJ AND (labels = ba-harness OR issuetype in (Epic, Story))>` |
| Confluence used | `<yes / no>` |
| Confluence space key(s) | `<e.g. PROJ>` |
| Confluence publish parent page | `<page title or ID under which published knowledge pages go>` |

## 3. Jira conventions

### Issue types

The names your Jira project actually uses for each harness template (some projects rename them).

| Harness template | Jira issue type name |
|---|---|
| Epic | `<Epic>` |
| Story | `<Story>` |
| Task | `<Task>` |
| Spike | `<Spike, or the type used for investigations>` |
| Bug | `<Bug>` |

### Required and custom fields

`/setup` reads these from Jira. One row per field that must be filled when creating an issue, beyond
summary and description.

| Issue type | Field name | Field ID | How the harness fills it |
|---|---|---|---|
| `<Story>` | `<Team>` | `<customfield_10001>` | `<default value, or "ask">` |

### Defaults

| Field | Value |
|---|---|
| Components (default) | `<none, or component names>` |
| Labels (always added) | `ba-harness` |
| Fix version convention | `<e.g. release numbers "2.26", or "unscheduled" until planned>` |
| Link type for "duplicates" | `<Duplicate>` |
| Link type for "relates to" | `<Relates>` |

## 4. Business areas

The areas the product divides into. They become folders under `knowledge/domains/` and labels on Jira
issues. Lowercase, hyphenated.

| Area | Label | One line |
|---|---|---|
| `<area-name>` | `<area-name>` | `<What it covers>` |

## 5. Settings

The harness reads this block. Values are `on` / `off` or numbers.

```yaml
kb_auto_sync: on         # pull new knowledge when a Claude Code session starts
confluence: off          # Confluence sync and publishing; set on if section 2 says yes
converter: pdf           # markitdown (if installed) or pdf (ask the BA to save Office files as PDF)
max_batch: 15            # most items created in Jira or Confluence per approval
sync_max_issues: 50      # most Jira issues read per /sync run
sync_max_pages: 20       # most Confluence pages read per /sync run
draft_age_days: 30       # /review kb flags drafts older than this
```

## 6. Material for `/kb-seed`

What already exists that the first knowledge base should be built from. Files go in `inbox/`.

| Source | Where | Notes |
|---|---|---|
| `<Project charter>` | `inbox/<file>.pdf` | |
| `<Confluence space or page tree>` | `<space key / page>` | |
| `<Existing epics>` | `<JQL>` | |

## 7. Writing rules

### Words that need a measure

`/review` flags these when a requirement uses them without a number or a definition. Add your own.

```text
fast, quick, slow, easy, simple, user-friendly, intuitive, flexible, robust, efficient, secure,
appropriate, as needed, etc., and/or, some, several, many, few, normally, usually, approximately
```

### House terms

Words the project prefers, and words to avoid. The glossary (`knowledge/glossary.md`) holds the
definitions; this table only records preferences.

| Use | Instead of |
|---|---|
| `<preferred term>` | `<words to avoid>` |
