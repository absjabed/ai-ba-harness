# Project profile

**This is the one file a project fills in.** Every command reads it before doing anything. `/setup`
fills it by interview; you can also edit it by hand. Replace every `<...>` placeholder. Where a row
doesn't apply, write `none` rather than deleting it. Keep the section headings: the commands look
them up by name.

---

## 1. Project

| Field | Value |
|---|---|
| Project name | FleetKeep Demo |
| One-line purpose | Keeps commercial vehicle fleets road-legal: inspections, walkaround checks, defects, workshop job cards and return to service, for transport managers, technicians, drivers and compliance officers. |
| BA repository | `fleetkeep-demo-ba-knowledge` |
| Lead BA (role) | Lead BA |
| Other maintainers (roles) | BA |
| Harness repository | `https://github.com/absjabed/ai-ba-harness.git` |
| Harness version this copy started from | `0.5.0` |
| Harness commit this copy started from | `118569b` |

The Lead BA and the other maintainers are the only roles that apply changes to the knowledge base
and to the harness files here. Keep this list the same as the "Accepting a knowledge base change"
row in `knowledge/stakeholders.md`.

## 2. Atlassian

| Field | Value |
|---|---|
| Atlassian site | `northwind-demo.atlassian.net` (not verified) |
| Cloud ID | `<filled by /setup from getAccessibleAtlassianResources; the Atlassian tools need it>` |
| Jira project key(s) | `FKD` (not verified) |
| Issue key format | `FKD-1234` (not verified) |
| Scope JQL for `/sync` | `project = FKD AND (labels = ba-harness OR issuetype in (Epic, Story, Spike))` (not verified; issue count: not run) |
| Confluence used | yes |
| Confluence space key(s) | `FKD` (not verified) |
| Confluence publish parent page | none |

## 3. Jira conventions

### Issue types

The names your Jira project actually uses for each harness template (some projects rename them).

| Harness template | Jira issue type name |
|---|---|
| Epic | `Epic` (not verified) |
| Story | `Story` (not verified) |
| Task | `Task` (not verified) |
| Spike | `Spike` (not verified) |
| Bug | `Bug` (not verified) |

### Required and custom fields

`/setup` reads these from Jira. One row per field that must be filled when creating an issue, beyond
summary and description.

| Issue type | Field name | Field ID | How the harness fills it |
|---|---|---|---|
| `Story` | `Team` | `customfield_10001` (not verified) | Fixed default: `FleetKeep Core` |

### Defaults

| Field | Value |
|---|---|
| Components (default) | none (not verified) |
| Labels (always added) | `ba-harness` |
| Fix version convention | Year and month, `2026.12`; "unscheduled" until planned (not verified) |
| Link type for "duplicates" | `Duplicate` (not verified) |
| Link type for "relates to" | `Relates` (not verified) |

## 4. Business areas

The areas the product divides into. They become folders under `knowledge/domains/` and labels on Jira
issues. Lowercase, hyphenated.

| Area | Label | One line |
|---|---|---|
| `vehicles` | `vehicles` | Vehicle register, depots, VOR status |
| `inspections` | `inspections` | Inspection intervals, anchor dates, due dates, dashboard banding |
| `defects` | `defects` | Walkaround checks, defect reports, triage |
| `workshop` | `workshop` | Job cards, parts |
| `tenancy-and-access` | `tenancy-and-access` | Operators, users, roles |

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

Status is `ready` (there to read), `expected` (promised, not received) or `done` (seeded).
`/kb-seed` with no argument reads only the `ready` rows.

| Source | Where | Status | Notes |
|---|---|---|---|
| Product owner's inspection rules | `inbox/product-rules-inspections.md` | `done` | Draft v2, 2026-10-02. Seeded 2026-10-15 as SRC-001. |
| Compliance adviser's regulator guidance summary | `inbox/regulator-guidance-summary.md` | `done` | 2026-10-05. Seeded 2026-10-15 as SRC-002. |
| Confluence business rules page tree | `FKD` / `<root page not given yet>` | `expected` | Promised later. |

## 7. Writing rules

### Words that need a measure

`/review` flags these when a requirement uses them without a number or a definition. Add your own.

```text
fast, quick, slow, easy, simple, user-friendly, intuitive, flexible, robust, efficient, secure,
appropriate, as needed, etc., and/or, some, several, many, few, normally, usually, approximately,
promptly, soon, real time
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

Changes made to this repository's copy of the harness (`agents/`, `templates/`, the conventions, a
wrapper's description) through `/improve-harness`, one row per changed file. Re-apply them after
updating the harness, unless the new version already includes them. The version in use now is in
`HARNESS_VERSION`.

| Date | File | Change | Proposal |
|---|---|---|---|
