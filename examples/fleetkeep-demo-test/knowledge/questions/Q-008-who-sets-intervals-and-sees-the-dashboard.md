---
type: question
id: Q-008
title: Who can set a vehicle's interval, and who can see the dashboard?
status: confirmed
state: open
asked_on: 2026-10-15
asked_of: Product owner
due: 2026-10-29
answered_on:
answer_source:
blocks: [CAP-001, CAP-003]
owner: Lead BA
sources: [SRC-002]
tags: [vehicles, inspections, tenancy-and-access]
created: 2026-10-15
updated: 2026-10-15
---

# Who can set a vehicle's interval, and who can see the dashboard?

Which roles can set or change a vehicle's safety inspection interval, and which can see the
dashboard's inspection due status?

## Where it comes up

- [CAP-001 Setting a vehicle's safety inspection interval](../domains/vehicles/CAP-001-setting-a-vehicles-safety-inspection-interval.md).
- [CAP-003 Seeing inspection due status on the dashboard](../domains/inspections/CAP-003-seeing-inspection-due-status-on-the-dashboard.md).
- Requirement REQ-inspection-due-dates-and-dashboard-banding.

## What is unclear

No page says who sets an interval or who sees the dashboard. The Lead BA's view: "transport managers
set intervals and see the dashboard; compliance officers see the dashboard read-only"
([SRC-002](../sources/SRC-002-2026-10-15-requirements-due-dates-and-banding.md)). Permissions are
product behaviour, which the Product owner decides. What technicians and drivers can do here isn't
stated. The due date was set for 2026-10-29 by the Lead BA.

## Possible answers

1. Transport managers set intervals and see the dashboard; compliance officers see the dashboard
   read-only (the Lead BA's view).
2. Transport managers and compliance officers both set intervals and see the dashboard.

## Why it matters

The permission paths of setting an interval and seeing the dashboard can't be built or tested until
this is decided.

## Answer

