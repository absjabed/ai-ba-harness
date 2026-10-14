---
type: question
id: Q-003
title: How quickly must the dashboard load, and for how many vehicles?
status: approved
state: answered
asked_on: 2026-10-14
asked_of: Product owner
due: 2026-10-28
answered_on: 2026-10-15
approved_by: Product owner
approved_on: 2026-10-15
answer_source: SRC-002
blocks: [CAP-003]
owner: Lead BA
sources: [SRC-001, SRC-002, DEC-003]
tags: [inspections]
created: 2026-10-14
updated: 2026-10-15
---

# How quickly must the dashboard load, and for how many vehicles?

How quickly must the dashboard load, and for a fleet of how many vehicles?

## Where it comes up

- [CAP-003 Seeing inspection due status on the dashboard](../domains/inspections/CAP-003-seeing-inspection-due-status-on-the-dashboard.md).

## What is unclear

The notes say "The dashboard needs to load fast for big fleets"
([SRC-001](../sources/SRC-001-2026-10-14-inspections-workshop.md)). "Fast" has no measure, "big
fleets" has no size, and the notes don't say who said it. The Engineering lead is to be consulted.
The due date was set for 2026-10-28 by the Lead BA; no date was given in the meeting.

## Possible answers

1. A load time and a fleet size the Product owner sets, for example "within N seconds for a fleet of
   M vehicles".

## Why it matters

The dashboard's performance requirement can't be written or tested without a number.

## Answer

Under 3 seconds for fleets of up to 2,000 vehicles. Given by the Product owner by email on
2026-10-15 and relayed by the Lead BA
([SRC-002](../sources/SRC-002-2026-10-15-requirements-due-dates-and-banding.md)); recorded as
[DEC-003](../decisions/DEC-003-dashboard-load-time-for-large-fleets.md).
