---
type: question
id: Q-021
title: What the dashboard shows when there are no vehicles to list
status: confirmed
state: open
asked_on: 2026-10-22
asked_of: Product owner
consulted: []
due: 2026-11-05
answered_on:
answer_source:
approved_by:
approved_on:
blocks: [CAP-003]
owner: Lead BA
sources: [SRC-009]
tags: [inspections]
created: 2026-10-22
updated: 2026-10-22
---

# What the dashboard shows when there are no vehicles to list

What does the inspection dashboard show when there are no vehicles to list?

## Where it comes up

- [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md), which says how each listed vehicle shows but not what an empty dashboard shows.
- [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md), FR-021 and ST-03.

## What is unclear

The dashboard's rules describe each vehicle's status and the order of the list, but not what the user sees when the list is empty. The review of the requirement on 2026-10-20 found the gap.

## Possible answers

1. A message: "No vehicles to show".
2. An empty list with no message.

## Why it matters

The empty dashboard can't be specified or tested until this is settled.

## Proposed answer

The Lead BA, 2026-10-22 ([SRC-009](../sources/SRC-009-2026-10-22-inspection-dashboard-proposals.md)); for the Product owner to confirm or change: possible answer 1. The rule it would become, on [Showing a vehicle's inspection status on the dashboard](../domains/inspections/CAP-003-showing-inspection-status-on-dashboard.md): "When there are no vehicles to list, the dashboard shows the message 'No vehicles to show'."

## Answer
