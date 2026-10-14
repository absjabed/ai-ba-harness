# Project profile

**This is the one file a project fills in.** Every command reads it before doing anything. `/setup`
fills it by interview; you can also edit it by hand. Replace every `<...>` placeholder and delete rows
that don't apply. Keep the section headings: the commands look them up by name.

---

## 1. Project

| Field | Value |
|---|---|
| Project name | FleetKeep Demo |
| One-line purpose | Keeps commercial vehicle fleets road-legal: inspections, walkaround checks, defects, workshop job cards and return to service, for transport managers, technicians, drivers and compliance officers. |
| BA repository | `fleetkeep-demo-ba-knowledge` |
| Lead BA (role) | Lead BA |
| Other maintainers (roles) | BA, Product owner |
| Harness repository | `https://github.com/absjabed/ai-ba-harness` |
| Harness version this copy started from | `0.4.2` |
| Harness commit this copy started from | `23e290f` |

## 2. Atlassian

| Field | Value |
|---|---|
| Atlassian site | `northwind-demo.atlassian.net` |
| Cloud ID | `<filled by /setup from getAccessibleAtlassianResources>` |
| Jira project key(s) | `FKD` |
| Issue key format | `FKD-1234` |
| Scope JQL for `/sync` | `project = FKD AND (labels = ba-harness OR issuetype in (Epic, Story, Spike))` |
| Confluence used | yes |
| Confluence space key(s) | `FKD` |
| Confluence publish parent page | none |

## 3. Jira conventions

### Issue types

The names your Jira project actually uses for each harness template (some projects rename them).

| Harness template | Jira issue type name |
|---|---|
| Epic | Epic |
| Story | Story |
| Task | Task |
| Spike | Spike |
| Bug | Bug |

### Required and custom fields

`/setup` reads these from Jira. One row per field that must be filled when creating an issue, beyond
summary and description.

| Issue type | Field name | Field ID | How the harness fills it |
|---|---|---|---|
| Story | Team | `customfield_10001` | Fixed default: `FleetKeep Core` |

Given by the Lead BA on 2026-10-14; not yet read from Jira, because the Atlassian server wasn't
connected. The required fields of Epic, Task, Spike and Bug haven't been read either. Run `/setup`
again once it is connected.

### Defaults

| Field | Value |
|---|---|
| Components (default) | none |
| Labels (always added) | `ba-harness` |
| Fix version convention | Year.month, for example `2026.11`; `unscheduled` until planned |
| Link type for "duplicates" | Duplicate |
| Link type for "relates to" | Relates |

## 4. Business areas

The areas the product divides into. They become folders under `knowledge/domains/` and labels on Jira
issues. Lowercase, hyphenated.

| Area | Label | One line |
|---|---|---|
| vehicles | vehicles | The fleet's vehicles and their records, including inspection intervals and VOR status |
| inspections | inspections | Scheduled safety inspections and walkaround checks |
| defects | defects | Defects found on checks and inspections, from report to resolution |
| workshop | workshop | Workshop job cards, repairs and return to service |
| tenancy-and-access | tenancy-and-access | Customer organisations (tenants), users, roles and what each can see and do |

## 5. Settings

The harness reads this block. Values are `on` / `off` or numbers.

```yaml
kb_auto_sync: on         # pull new knowledge when a Claude Code session starts
confluence: on           # Confluence sync and publishing; set on if section 2 says yes
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
| Regulator guidance on inspection intervals | `inbox/` (not received yet) | PDF; add when it arrives |

Little is written down yet. The first knowledge comes from the inspections workshop of 2026-10-14:
its notes are in `inbox/` and go through `/intake`, not `/kb-seed`.

## 7. Writing rules

### Words that need a measure

`/review` flags these when a requirement uses them without a number or a definition. Add your own.

```text
fast, quick, slow, easy, simple, user-friendly, intuitive, flexible, robust, efficient, secure,
appropriate, as needed, etc., and/or, some, several, many, few, normally, usually, approximately,
promptly, soon, due soon, real time
```

### House terms

Words the project prefers, and words to avoid. The glossary (`knowledge/glossary.md`) holds the
definitions; this table only records preferences.

| Use | Instead of |
|---|---|
| walkaround check | daily check |
| job card | work order |
| VOR | grounded |
| anchor date | start date |

## 8. Local harness changes

Changes made to this repository's copy of the harness (`agents/`, `templates/`, the conventions)
through `/improve-harness`. Re-apply them after updating the harness, unless the new version already
includes them.

| Date | File | Change | Proposal |
|---|---|---|---|
| 2026-10-15 | `templates/requirement.md` | A "Data" line under each story's business rules: the entities and fields it reads or changes | [2026-10-15-data-line-under-each-story](harness-feedback/2026-10-15-data-line-under-each-story.md) |
| 2026-10-15 | `agents/requirements.md` | Step 3, user stories: how `/requirements` fills the Data line | [2026-10-15-data-line-under-each-story](harness-feedback/2026-10-15-data-line-under-each-story.md) |
