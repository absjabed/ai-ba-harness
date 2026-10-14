# Project profile

**This is the one file a project fills in.** Every command reads it before doing anything. `/setup`
fills it by interview; you can also edit it by hand. Replace every placeholder and delete rows
that don't apply. Keep the section headings: the commands look them up by name.

---

## 1. Project

| Field | Value |
|---|---|
| Project name | FleetKeep |
| One-line purpose | `Keeps commercial vehicle fleets road-legal and roadworthy: statutory due dates, driver walkaround checks, defects, workshop job cards and parts, for transport managers, technicians, drivers and compliance officers at haulage and coach operators` |
| BA repository | `fleetkeep-ba-knowledge` |
| Lead BA (role) | `Lead BA` |
| Other BAs (roles) | `BA, Product owner` |
| Harness version this copy started from | `0.1.0` |
| Harness commit this copy started from | `example` |

## 2. Atlassian

| Field | Value |
|---|---|
| Atlassian site | `northwind.atlassian.net` |
| Cloud ID | `00000000-0000-4000-8000-00000000f1ee` (fictional) |
| Jira project key(s) | `FK` |
| Issue key format | `FK-1234` |
| Scope JQL for `/sync` | `project = FK AND (labels = ba-harness OR issuetype in (Epic, Story, Spike))` |
| Confluence used | `yes` |
| Confluence space key(s) | `FK` |
| Confluence publish parent page | `FleetKeep BA knowledge (published copy)` |

## 3. Jira conventions

### Issue types

The names your Jira project actually uses for each harness template (some projects rename them).

| Harness template | Jira issue type name |
|---|---|
| Epic | `Epic` |
| Story | `Story` |
| Task | `Task` |
| Spike | `Spike` |
| Bug | `Bug` |

### Required and custom fields

`/setup` reads these from Jira. One row per field that must be filled when creating an issue, beyond
summary and description.

| Issue type | Field name | Field ID | How the harness fills it |
|---|---|---|---|
| `Story` | `Team` | `customfield_10001` | `default "FleetKeep Core"` |
| `Bug` | `Affected area` | `customfield_10045` | `the requirement's area; ask if there is no requirement` |

### Defaults

| Field | Value |
|---|---|
| Components (default) | `none` |
| Labels (always added) | `ba-harness` |
| Fix version convention | `release numbers "2026.11" (year and month); "unscheduled" until planned` |
| Link type for "duplicates" | `Duplicate` |
| Link type for "relates to" | `Relates` |

## 4. Business areas

The areas the product divides into. They become folders under `knowledge/domains/` and labels on Jira
issues. Lowercase, hyphenated.

| Area | Label | One line |
|---|---|---|
| `vehicles` | `vehicles` | `The vehicle register, depots, off-road (VOR) status and return to service` |
| `inspections` | `inspections` | `Inspection frequencies, anchor dates, due dates and red/amber/green compliance banding` |
| `defects` | `defects` | `Driver walkaround checks, defect reports, triage and escalation` |
| `workshop` | `workshop` | `Job cards, labour, parts used, depot stock and reorder alerts` |
| `tenancy-and-access` | `tenancy-and-access` | `Operators as tenants, users, roles and depot scoping` |

## 5. Settings

The harness reads this block. Values are `on` / `off` or numbers.

```yaml
kb_auto_sync: on         # pull new knowledge when a Claude Code session starts
confluence: on           # Confluence sync and publishing; set on if section 2 says yes
converter: markitdown    # markitdown (if installed) or pdf (ask the BA to save Office files as PDF)
max_batch: 15            # most items created in Jira or Confluence per approval
sync_max_issues: 50      # most Jira issues read per /sync run
sync_max_pages: 20       # most Confluence pages read per /sync run
draft_age_days: 30       # /review kb flags drafts older than this
```

## 6. Material for `/kb-seed`

What already exists that the first knowledge base should be built from. Files go in `inbox/`.

| Source | Where | Notes |
|---|---|---|
| `Product rules page tree` | `FK / FleetKeep product rules` | Written by the Product owner; the main statement of category, escalation and return-to-service rules. Not seeded yet: the Product owner is rewriting it. Run `/kb-seed confluence` once it is republished |
| `Regulator roadworthiness guidance (PDF)` | `inbox/regulator-roadworthiness-guidance.pdf` | Processed with `/intake` on 2026-09-24 as SRC-002; raw file removed from `inbox/` afterwards |
| `Existing epics` | `project = FK AND issuetype = Epic AND statusCategory != Done` | Read during `/sync` rather than seeded |

## 7. Writing rules

### Words that need a measure

`/review` flags these when a requirement uses them without a number or a definition. Add your own.

```text
fast, quick, slow, easy, simple, user-friendly, intuitive, flexible, robust, efficient, secure,
appropriate, as needed, etc., and/or, some, several, many, few, normally, usually, approximately,
promptly, urgent, soon, real time
```

### House terms

Words the project prefers, and words to avoid. The glossary (`knowledge/glossary.md`) holds the
definitions; this table only records preferences.

| Use | Instead of |
|---|---|
| `walkaround check` | `daily check, walkround, first-use check` |
| `VOR` (vehicle off road) | `grounded, parked up, off the road` |
| `job card` | `work order, job sheet, ticket` |
| `category-A defect` | `critical defect, dangerous defect, showstopper` |
| `return to service` | `release, back on the road, RTS` |
| `transport manager` | `fleet manager, TM` |
