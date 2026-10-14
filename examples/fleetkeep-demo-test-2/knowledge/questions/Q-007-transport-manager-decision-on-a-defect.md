---
type: question
id: Q-007
title: What the transport manager decides on a defect, and what it comes before
status: confirmed
state: open
asked_on: 2026-10-17
asked_of: Product owner
due: 2026-10-31
answered_on:
answer_source:
approved_by:
approved_on:
blocks: [CAP-006, CAP-005]
owner: Lead BA
sources: [SRC-003]
tags: [defects]
created: 2026-10-17
updated: 2026-10-17
---

# What the transport manager decides on a defect, and what it comes before

Which decisions can the transport manager make on a reported defect, and what must that decision come before?

## Where it comes up

- [Deciding what happens to a reported defect](../domains/defects/CAP-006-deciding-what-happens-to-a-reported-defect.md).
- [Reporting a defect in a walkaround check](../domains/defects/CAP-005-reporting-a-defect-in-a-walkaround-check.md), for when a category-A defect takes the vehicle off the road.

## What is unclear

The Product owner decided: "Every defect gets a decision from the transport manager first." ([SRC-003](../sources/SRC-003-2026-10-16-defects-workshop.md), bullet 3). The notes don't say which decisions are possible, or what "first" comes before: a repair, a job card, a technician clearing the defect. The same workshop decided that a category-A defect takes the vehicle off the road "immediately" (bullet 2); it isn't said whether that happens before or after the transport manager's decision.

## Possible answers

1. A category-A defect makes the vehicle VOR as soon as it is reported; for every defect, nothing else (no job card, no repair, no clearing) happens until the transport manager has decided.
2. The transport manager's decision comes before everything, including taking a vehicle off the road for a category-A defect.
3. Something else the Product owner decides.

## Why it matters

Deciding what happens to a defect, and how it leads to a job card or a repair, can't be specified until the possible decisions and their order are known.

## Answer
