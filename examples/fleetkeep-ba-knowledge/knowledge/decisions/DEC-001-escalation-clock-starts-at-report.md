---
type: decision
id: DEC-001
title: Escalation clock starts when the defect is reported
status: approved
decided_by: Product owner
decided_on: 2026-09-16
approved_by: Product owner
approved_on: 2026-09-16
owner: Product owner
sources:
  - SRC-001
  - SRC-003
tags:
  - defects
created: 2026-09-17
updated: 2026-10-06
---

# Escalation clock starts when the defect is reported

The time a defect may wait before it escalates is counted from the moment the driver reports it, not
from triage or the start of the next shift.

## Context

In the discovery workshop the Pilot transport manager asked whether a defect triaged late but within
the day "still counts as late". The rules said a category-A defect escalates after 4 hours but not
when the 4 hours start ([SRC-001](../sources/SRC-001-2026-09-16-discovery-workshop.md)).

## Options considered

| Option | For | Against |
|---|---|---|
| From the report | Simple; an immobilising defect needs action whoever has seen it | A report late in the day can escalate out of hours ([Q-002](../questions/Q-002-escalation-clock-outside-working-hours.md)) |
| From triage | Measures workshop response only | A defect nobody triages would never escalate, which defeats the purpose |
| From the start of the next shift | Fits depot working hours | Needs shift patterns FleetKeep doesn't hold |

## Decision

From the report. The Product owner said the point of escalation is to catch defects nobody has acted
on, so the clock can't wait for someone to act.

## Consequences

- BR-008 on [CAP-003](../domains/defects/CAP-003-escalating-an-unactioned-category-a-defect.md), now
  BR-017 on [CAP-004](../domains/defects/CAP-004-escalating-unactioned-defects.md).
- Whether the clock pauses outside working hours is a separate question, still open (Q-002).

## Sources

- SRC-001: Discovery workshop, 2026-09-16, decided by the Product owner during the escalation discussion
- [SRC-003](../sources/SRC-003-2026-10-06-jira-sync.md): Jira activity to 2026-10-06, after which the rule moved from CAP-003 to CAP-004
