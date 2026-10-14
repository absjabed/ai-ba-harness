# Staging: intake inbox/dev-note-dashboard.md, 2026-10-23

<!-- Proposed knowledge changes waiting for the BA. Nothing here is in the knowledge base yet.
     Start with the Critic section. Tick one box per item, or answer in the chat ("accept 1-4,
     reject 5, edit 6: ..."); the command writes chat decisions into this file. When you say apply
     (normally once every item is decided), the command applies the accepted items and deletes this
     file, or keeps only the undecided ones. -->

| Field | Value |
|---|---|
| Input | `inbox/dev-note-dashboard.md` (a developer's note, three sentences; not committed) |
| Kind | document |
| Source record to create | SRC-new |
| Items | 3: 3 new, 0 confirms, 0 extends, 0 contradicts, 0 duplicate, 0 answers; 0 proposed as ignore |
| Needs redaction | no |
| Critic | 9 findings: 3 fixed, 6 for you to check |

## Summary

A developer building the inspection status dashboard wrote a short note on 2026-10-23. They found
vehicles with no anchor date at all, about 40 in the pilot data, and nothing says what the
dashboard should show for them. They also suggest the dashboard should list overdue vehicles first.
Neither point is covered by the knowledge base: the due date and the dashboard status both depend
on the anchor date (BR-003, BR-004), and nothing says in what order the dashboard lists vehicles.
Both become questions for the Product owner, who decides product behaviour.

## Critic

Ran as the read-only `critic` sub-agent (`.claude/agents/critic.md`), given this file and
`inbox/dev-note-dashboard.md`. It confirmed all three quotes word for word, all three `new` verdicts,
and that every diff quotes the current page text exactly. 9 findings: 3 `fix`, 6 `check`.

- **Fixed:** item 1 now depends on item 2 (Q-new-1 links I-new-1); item 2 has its `Affects
  delivery` row; item 3's CAP-003 diff sets `updated` when item 1 isn't accepted, and its callout
  goes after item 1's when both are.
- **For you to check:** items 1 (three points), 3 (two points); see their `Critic` rows.

**Other findings:**
- (missed, check) The developer is building the dashboard from "the requirement", which isn't in
  this repository (`requirements/` is empty, `trace/map.csv` has no rows), while CAP-003 is still
  blocked by Q-001, Q-002 and Q-003. Consider a RAID issue, or an action for the Lead BA to find
  that requirement and link it to CAP-003. Not added as an item.
- (item 3, check) The developer role isn't in `stakeholders.md`; you may want to add a Developer row
  (Can decide: nothing in product behaviour; contact through the Engineering lead). Not an item.

## Items

### 1. What the dashboard shows for a vehicle with no anchor date

| Field | Value |
|---|---|
| Kind | question |
| Verdict | new |
| Searched for | "no anchor date", "without an anchor", "missing", "blank", "not set", "anchor date" (index, glossary with alias "start date", CAP-001, CAP-002, CAP-003, Q-001, Q-003, Q-011, registers) |
| Depends on | 2 (Q-new-1 links I-new-1; if item 2 is rejected, drop the I-new-1 line from Q-new-1) (added after the critic) |
| Clarity | clear |
| Authority | n/a |
| Sensitivity | clean |
| Quote | "while building the dashboard I noticed vehicles with no anchor date at all, about 40 in the pilot data. The requirement doesn't say what to show for them." (`inbox/dev-note-dashboard.md`, sentences 1 and 2) |
| Critic | fixed: `Depends on` row added. check: (a) consider adding CAP-001 to `blocks` and a `[!CAUTION]` callout in CAP-001's Open items, since CAP-001 says the anchor date's "Required?" is "Not stated in the source" (Q-011 also blocks CAP-001 without a callout, so either way can be consistent); (b) in "What is unclear", also cite CAP-002's Inputs row, which lists the anchor date as required for the due date calculation; (c) shorten the CAP-003 callout to the unresolved behaviour only ("what the dashboard shows for a vehicle with no anchor date"), leaving the pilot count in I-new-1 and Q-new-1, since a caution callout is for unclear behaviour (conventions section 6) |
| Affects delivery | none found: `trace/map.csv` has no rows and `requirements/` has no documents. The note refers to "the requirement", which isn't in this repository |
| Proposed change | new Q-new-1 for Product owner, due 2026-11-06 (proposed), status confirmed, state open; edit CAP-003 and CAP-002 to add a `[!CAUTION]` callout in Open items (diffs below) |

<details>
<summary>The proposed page, exactly as it will be written</summary>

```markdown
---
type: question
id: Q-new-1
title: What the dashboard shows for a vehicle with no anchor date
status: confirmed
state: open
asked_on: 2026-10-23
asked_of: Product owner
due: 2026-11-06
answered_on:
answer_source:
approved_by:
approved_on:
blocks: [CAP-003, CAP-002]
owner: Lead BA
sources: [SRC-new]
tags: [inspections]
created: 2026-10-23
updated: 2026-10-23
---

# What the dashboard shows for a vehicle with no anchor date

What does the dashboard show for a vehicle that has no anchor date, and must every vehicle have one?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md): the status depends on the next due date (BR-004).
- [Calculating the next inspection due date](../domains/inspections/CAP-002-calculating-next-inspection-due-date.md): the next due date counts from the anchor date (BR-003).
- [Setting a vehicle's inspection interval and anchor date](../domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md): whether a vehicle must have an anchor date is not stated.
- I-new-1 in the [RAID log](../raid.md).

## What is unclear

A developer building the dashboard noticed "vehicles with no anchor date at all, about 40 in the pilot data" and that "The requirement doesn't say what to show for them" ([SRC-new](../sources/SRC-new-2026-10-23-developer-dashboard-note.md), sentences 1 and 2). The next due date is the anchor date plus a whole number of the vehicle's inspection intervals (BR-003), and the dashboard status depends on the next due date (BR-004), so under the current rules a vehicle without an anchor date has no due date and no status. Nothing says whether a vehicle may exist without an anchor date.

## Possible answers

1. Every vehicle must have an anchor date. The dashboard shows a vehicle without one apart from the green, amber and red bands, as needing a transport manager to set it (BR-002).
2. A vehicle without an anchor date is shown red until a transport manager sets one.
3. Something else the Product owner decides.

## Why it matters

The dashboard can't show or be tested for these vehicles until this is decided, and about 40 vehicles in the pilot data are affected.

## Answer
```

</details>

```diff
 # knowledge/domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md
-sources: [SRC-001]
+sources: [SRC-001, SRC-new]
-updated: 2026-10-15
+updated: 2026-10-23
 ...
 > [!CAUTION]
 > **Unresolved:** how a VOR vehicle's status is shown on the dashboard. See [Q-003](../../questions/Q-003-inspection-rules-for-vor-vehicles.md).
+
+> [!CAUTION]
+> **Unresolved:** what the dashboard shows for a vehicle with no anchor date; about 40 vehicles in the pilot data have none. See [Q-new-1](../../questions/Q-new-1-dashboard-vehicle-with-no-anchor-date.md).
 
 ## Sources
 
 - SRC-001: the Product owner's inspection rules, draft v2, 2026-10-02
+- SRC-new: a developer's note on the dashboard, 2026-10-23
```

```diff
 # knowledge/domains/inspections/CAP-002-calculating-next-inspection-due-date.md
-sources: [SRC-001]
+sources: [SRC-001, SRC-new]
-updated: 2026-10-15
+updated: 2026-10-23
 ...
 > [!CAUTION]
 > **Unresolved:** how the inspection rules apply to a vehicle while it is VOR. See [Q-003](../../questions/Q-003-inspection-rules-for-vor-vehicles.md).
+
+> [!CAUTION]
+> **Unresolved:** what happens for a vehicle that has no anchor date, so no due date can be worked out. See [Q-new-1](../../questions/Q-new-1-dashboard-vehicle-with-no-anchor-date.md).
 
 ## Sources
 
 - SRC-001: the Product owner's inspection rules, draft v2, 2026-10-02
+- SRC-new: a developer's note on the dashboard, 2026-10-23
```

- [ ] accept
- [ ] edit: <what to change>
- [ ] reject: <why>

### 2. About 40 vehicles in the pilot data have no anchor date

| Field | Value |
|---|---|
| Kind | risk (an issue) |
| Verdict | new |
| Searched for | "pilot data", "no anchor date", "missing", "data quality", "import" (index, `raid.md`, CAP-001, Q-011, R-003) |
| Depends on | 1 (links Q-new-1) |
| Clarity | vague: "about" (an approximate count; the question in item 1 covers what is missing, and the exact number isn't needed to answer it) |
| Authority | n/a |
| Sensitivity | clean |
| Quote | "I noticed vehicles with no anchor date at all, about 40 in the pilot data." (`inbox/dev-note-dashboard.md`, sentence 1) |
| Critic | fixed: `Affects delivery` row added |
| Affects delivery | none found: `trace/map.csv` has no rows and `requirements/` has no documents (added after the critic) |
| Proposed change | new I-new-1 row in the Issues table of `raid.md`, owner Product owner (the pilot customer is reached through the Product owner, `stakeholders.md`); add SRC-new to `raid.md` `sources`, `updated: 2026-10-23` |

```diff
 # knowledge/raid.md
-sources: [SRC-001, SRC-002, SRC-003, SRC-004, SRC-005]
+sources: [SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-new]
-updated: 2026-10-17
+updated: 2026-10-23
 ...
 | ID | Issue | Impact | Action | Owner | Status | Source |
 |---|---|---|---|---|---|---|
+| I-new-1 | About 40 vehicles in the pilot data have no anchor date, as reported by a developer building the dashboard | The product can't work out their next due date or show their dashboard status | Settle [Q-new-1](questions/Q-new-1-dashboard-vehicle-with-no-anchor-date.md) | Product owner | open | SRC-new |
```

- [ ] accept
- [ ] edit: <what to change>
- [ ] reject: <why>

### 3. The order the dashboard lists vehicles in

| Field | Value |
|---|---|
| Kind | requirement |
| Verdict | new |
| Searched for | "sort", "order", "overdue first", "list", "dashboard" (index, CAP-003, Q-001, Q-002, Q-003, registers) |
| Clarity | incomplete: only says overdue vehicles come first ("probably"); nothing on the order of the other vehicles or within a band |
| Authority | unknown: the speaker's role (developer) isn't in `stakeholders.md`. The order of the dashboard is product behaviour, which the Product owner decides, so it is staged as a question to the Product owner with the developer's suggestion as a possible answer |
| Sensitivity | clean |
| Quote | "Also, the dashboard should probably sort overdue vehicles first." (`inbox/dev-note-dashboard.md`, sentence 3) |
| Critic | fixed: the CAP-003 diff now sets `updated` if item 1 isn't accepted, and says where the callout goes when both are. check: (a) in Q-new-2's "What is unclear", consider one more sentence saying that where VOR vehicles (Q-003) and vehicles without an anchor date (Q-new-1) appear in the list is also undecided, and optionally `Depends on: 1`; (b) the developer role isn't in `stakeholders.md` (see Other findings) |
| Affects delivery | none found: `trace/map.csv` has no rows and `requirements/` has no documents |
| Proposed change | new Q-new-2 for Product owner, due 2026-11-06 (proposed), status confirmed, state open; edit CAP-003 to add a `[!CAUTION]` callout in Open items (diff below) |

<details>
<summary>The proposed page, exactly as it will be written</summary>

```markdown
---
type: question
id: Q-new-2
title: The order the dashboard lists vehicles in
status: confirmed
state: open
asked_on: 2026-10-23
asked_of: Product owner
due: 2026-11-06
answered_on:
answer_source:
approved_by:
approved_on:
blocks: [CAP-003]
owner: Lead BA
sources: [SRC-new]
tags: [inspections]
created: 2026-10-23
updated: 2026-10-23
---

# The order the dashboard lists vehicles in

In what order does the dashboard list vehicles: overdue vehicles first, and then what?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md).

## What is unclear

The dashboard bands each vehicle green, amber or red (BR-004), but nothing says in what order it lists them. A developer building the dashboard suggests "the dashboard should probably sort overdue vehicles first" ([SRC-new](../sources/SRC-new-2026-10-23-developer-dashboard-note.md), sentence 3). That is their view; the order is product behaviour, which the Product owner decides ([stakeholders](../stakeholders.md)). Which vehicles count as overdue is itself still open ([Q-001](Q-001-next-due-date-after-a-missed-inspection.md), [Q-002](Q-002-grace-period-before-an-inspection-is-overdue.md)).

## Possible answers

1. Overdue (red) vehicles first, then amber, then green; within each band, the earliest next due date first. (The developer's suggestion, extended to the other bands.)
2. Overdue vehicles first, then the rest in another order the Product owner names.
3. Something else the Product owner decides.

## Why it matters

The dashboard's list can't be specified or tested until its order is known.

## Answer
```

</details>

If item 1 is also accepted, this callout goes after item 1's Q-new-1 callout, and the `sources`
and `updated` lines below are already changed by item 1. (Added after the critic.)

```diff
 # knowledge/domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md
-sources: [SRC-001]
+sources: [SRC-001, SRC-new]
-updated: 2026-10-15
+updated: 2026-10-23
 ...
 > [!CAUTION]
 > **Unresolved:** how a VOR vehicle's status is shown on the dashboard. See [Q-003](../../questions/Q-003-inspection-rules-for-vor-vehicles.md).
+
+> [!CAUTION]
+> **Unresolved:** in what order the dashboard lists vehicles. See [Q-new-2](../../questions/Q-new-2-order-of-vehicles-on-the-dashboard.md).
 
 ## Sources
 
 - SRC-001: the Product owner's inspection rules, draft v2, 2026-10-02
+- SRC-new: a developer's note on the dashboard, 2026-10-23
```

- [ ] accept
- [ ] edit: <what to change>
- [ ] reject: <why>
