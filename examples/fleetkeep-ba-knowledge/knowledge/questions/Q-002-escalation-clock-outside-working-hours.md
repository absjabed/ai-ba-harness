---
type: question
id: Q-002
title: Does the escalation clock run outside depot working hours?
status: confirmed
state: open
asked_on: 2026-09-16
asked_of: Product owner
due: 2026-10-21
answered_on:
answer_source:
blocks:
  - CAP-004
  - REQ-defect-escalation-to-workshop
owner: Lead BA
sources:
  - SRC-001
  - SRC-003
  - SRC-004
tags:
  - defects
created: 2026-09-17
updated: 2026-10-09
---

# Does the escalation clock run outside depot working hours?

Does the time before a defect escalates keep counting when the depot is closed, or only during the
depot's working hours?

## Where it comes up

- [Escalating unactioned defects](../domains/defects/CAP-004-escalating-unactioned-defects.md) (BR-015, BR-016)
- [Defect escalation to workshop](../../requirements/defect-escalation-to-workshop/requirement.md), marked non-blocking

## What is unclear

The Pilot workshop supervisor said: "A defect reported at nine at night escalates at one in the
morning, when there's nobody in the workshop to see it"
([SRC-001](../sources/SRC-001-2026-09-16-discovery-workshop.md)). The rules say a category-A defect
escalates 4 hours after it is reported ([DEC-001](../decisions/DEC-001-escalation-clock-starts-at-report.md)),
but not whether those are clock hours or working hours.

## Possible answers

1. The clock runs continuously. A category-A vehicle can't move, so someone is told whatever the
   hour. This is how the rules read today.
2. The clock counts only the depot's working hours. Escalations arrive when someone can act, but
   FleetKeep would need each depot's working hours (D-001).

## Why it matters

It decides when escalations arrive and who receives them at night. The thresholds in BR-015 and
BR-016 can't be tested at the edges of a shift until it is answered.

## Answer
