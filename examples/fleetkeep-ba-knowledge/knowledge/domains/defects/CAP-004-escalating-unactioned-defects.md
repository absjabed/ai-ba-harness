---
type: capability
id: CAP-004
title: Escalating unactioned defects
status: confirmed
area: defects
owner: Product owner
sources:
  - SRC-001
  - SRC-003
  - SRC-004
  - FK-1188
  - DEC-001
rules:
  - BR-015
  - BR-016
  - BR-017
aliases:
  - defect escalation
  - chasing a defect
  - overdue defect alert
tags:
  - defects
created: 2026-10-06
updated: 2026-10-09
---

# Escalating unactioned defects

FleetKeep alerts the transport manager when a category-A or category-B defect has waited longer than
its category allows without a triage outcome, so no serious defect sits unnoticed.

## Who and when

| Role | What they do here | When |
|---|---|---|
| Transport manager | Receives the escalation and triages the defect | 4 hours after a category-A defect is reported, or 36 hours after a category-B defect, if it has no triage outcome |
| FleetKeep | Checks every defect against its threshold | Once an hour |

## What the user sees

The transport manager receives an escalation email about the defect
([SRC-001](../../sources/SRC-001-2026-09-16-discovery-workshop.md)). FleetKeep checks once an hour,
so the email can arrive up to an hour after the threshold passes
([SRC-003](../../sources/SRC-003-2026-10-06-jira-sync.md)).

## Inputs

| Input | Required? | Rules |
|---|---|---|
| None | | The escalation is automatic |

## Rules applied

In the order they are evaluated.

1. **BR-017** The escalation clock starts when the defect is reported. ([DEC-001](../../decisions/DEC-001-escalation-clock-starts-at-report.md))
2. **BR-015** A category-A defect still in Reported or Triaged 4 hours after it was reported is escalated to the transport manager. (SRC-001, [FK-1188](https://northwind.atlassian.net/browse/FK-1188))
3. **BR-016** A category-B defect still in Reported or Triaged 36 hours after it was reported is escalated to the transport manager. (FK-1188)

> [!WARNING]
> A defect in Triaged still escalates. Escalation stops only when the defect reaches Job card raised
> or is rejected (BR-015, BR-016).

## Outcomes

- The transport manager is emailed about the defect.
- The escalation is recorded in the defect's audit trail.

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|
| A job card is raised, or the defect is rejected, before the threshold | No escalation | BR-015, BR-016 |
| The escalation email can't be sent | It is tried again at the next hourly check | None (product behaviour, SRC-003) |

## Interactions

- Watches defects from [Reporting a defect from a walkaround check](CAP-001-reporting-a-defect-from-a-walkaround-check.md)
  until [Triaging a defect](CAP-002-triaging-a-defect.md) gives an outcome.
- Replaces [CAP-003](CAP-003-escalating-an-unactioned-category-a-defect.md) (superseded).
- The epic [Defect escalation to workshop](../../../requirements/defect-escalation-to-workshop/requirement.md)
  extends escalation to the depot's workshop ([SRC-004](../../sources/SRC-004-2026-10-09-escalation-requirements-session.md)).

## Open items

> [!CAUTION]
> **Unresolved:** whether the escalation clock keeps running outside depot working hours, so that a
> category-A defect reported late in the evening escalates overnight. See
> [Q-002](../../questions/Q-002-escalation-clock-outside-working-hours.md).

## Sources

- SRC-001: Discovery workshop on defects, the workshop and return to service, 2026-09-16
- SRC-003: Jira activity 2026-09-28 to 2026-10-06; FK-1188 showed category-B escalation at 36 hours
- SRC-004: Requirements session on defect escalation to the workshop, 2026-10-09
