---
type: capability
id: CAP-003
title: Escalating an unactioned category-A defect
status: superseded
superseded_by: CAP-004
area: defects
owner: Product owner
sources:
  - SRC-001
  - SRC-003
  - DEC-001
rules:
  - BR-007
  - BR-008
aliases:
  - category-A escalation
tags:
  - defects
created: 2026-09-17
updated: 2026-10-06
---

# Escalating an unactioned category-A defect

FleetKeep alerts the transport manager when a category-A defect has waited too long for triage, so an
immobilised vehicle isn't forgotten.

> [!WARNING]
> **Superseded on 2026-10-06 by [CAP-004 Escalating unactioned defects](CAP-004-escalating-unactioned-defects.md).**
> This page only covered category-A defects. The Jira sync of 2026-10-06 showed category-B defects
> escalate too ([FK-1188](https://northwind.atlassian.net/browse/FK-1188), [SRC-003](../../sources/SRC-003-2026-10-06-jira-sync.md)),
> so the BA replaced it with a page for both categories. Kept for history; don't use it.
> BR-007 is replaced by BR-015, and BR-008 by BR-017.

## Who and when

| Role | What they do here | When |
|---|---|---|
| Transport manager | Receives the escalation | 4 hours after a category-A defect is reported, if it is still untriaged |

## What the user sees

An escalation email to the transport manager ([SRC-001](../../sources/SRC-001-2026-09-16-discovery-workshop.md)).

## Inputs

| Input | Required? | Rules |
|---|---|---|
| None | | The escalation is automatic |

## Rules applied

In the order they are evaluated.

1. **BR-008** The escalation clock starts when the defect is reported. ([DEC-001](../../decisions/DEC-001-escalation-clock-starts-at-report.md))
2. **BR-007** A category-A defect still in Reported or Triaged 4 hours after it was reported is escalated to the transport manager. (SRC-001)

## Outcomes

The transport manager is told about the waiting defect.

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|
| The defect is triaged in time | No escalation | BR-007 |

## Interactions

Replaced by [Escalating unactioned defects](CAP-004-escalating-unactioned-defects.md).

## Open items

None on this page. Open items moved to CAP-004.

## Sources

- SRC-001: Discovery workshop on defects, the workshop and return to service, 2026-09-16
- SRC-003: Jira activity 2026-09-28 to 2026-10-06, which led to this page being superseded
