---
type: capability
id: CAP-003
title: Seeing inspection due status on the dashboard
status: confirmed
area: inspections
owner: Product owner
sources: [SRC-001, DEC-002, SRC-002, DEC-003]
rules: [BR-003, BR-005]
aliases: [RAG banding]
tags: [inspections]
created: 2026-10-14
updated: 2026-10-15
---

# Seeing inspection due status on the dashboard

Shows each vehicle's safety inspection due status on the dashboard as green, amber or red
([DEC-002](../../decisions/DEC-002-inspection-due-banding.md)).

## Who and when

Not described in the sources yet.

## What the user sees

The dashboard loads in under 3 seconds for fleets of up to 2,000 vehicles
([DEC-003](../../decisions/DEC-003-dashboard-load-time-for-large-fleets.md), answering
[Q-003](../../questions/Q-003-dashboard-load-time-for-large-fleets.md)).

## Inputs

| Input | Required? | Rules |
|---|---|---|
| Next safety inspection due date | yes | From [CAP-002](CAP-002-calculating-the-next-inspection-due-date.md) |

## Rules applied

In the order they are evaluated.

1. **BR-003** Each vehicle's safety inspection status on the dashboard is green when the next due
   date is more than 14 days away, amber when it is 14 days away or less, and red when it is
   overdue. ([SRC-001](../../sources/SRC-001-2026-10-14-inspections-workshop.md), DEC-002)
2. **BR-005** The days in BR-003 are calendar days, counted from today to the next due date. A
   vehicle whose next due date is today is amber; it is red from the day after its due date.
   ([SRC-002](../../sources/SRC-002-2026-10-15-requirements-due-dates-and-banding.md))

## Outcomes

Not described in the sources yet.

## Failure and blocked paths

Not described in the sources yet.

## Interactions

- [CAP-002 Calculating the next safety inspection due date](CAP-002-calculating-the-next-inspection-due-date.md)
  provides the due date that is banded.

## Open items

> [!CAUTION]
> **Unresolved:** what the dashboard shows for a vehicle with no anchor date
> ([Q-004](../../questions/Q-004-no-anchor-date-on-the-dashboard.md)).

> [!CAUTION]
> **Unresolved:** who can see the dashboard
> ([Q-008](../../questions/Q-008-who-sets-intervals-and-sees-the-dashboard.md)).

> [!NOTE]
> **Assumption:** until Q-001 is answered, a VOR vehicle is banded like any other vehicle
> ([A-001](../../raid.md#assumptions)).

## Sources

- SRC-001: Inspections workshop, 2026-10-14 (Lead BA's notes)
- DEC-002: Inspection due banding on the dashboard
- SRC-002: Requirements clarification session, 2026-10-15 (Lead BA)
- DEC-003: Dashboard load time for large fleets
