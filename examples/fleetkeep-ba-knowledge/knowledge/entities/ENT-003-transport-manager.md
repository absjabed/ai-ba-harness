---
type: entity
id: ENT-003
title: Transport manager
status: confirmed
kind: role
owner: Product owner
sources:
  - SRC-001
  - SRC-003
aliases:
  - TM
  - fleet manager
tags:
  - tenancy-and-access
  - defects
created: 2026-09-17
updated: 2026-10-06
---

# Transport manager

The person at an operator who is accountable for its licence, and the FleetKeep role that triages
defects, receives escalations and authorises return to service.

## Attributes or permissions

| Name | Meaning | Rules |
|---|---|---|
| Read | Everything at their assigned depots | Sees only assigned depots, unless they also hold the compliance officer role, which reads across the whole operator |
| Schedule inspections | Schedule and reschedule a vehicle's inspections | Re-anchoring a schedule needs a reason and is recorded |
| Triage defects | Raise a job card or reject a defect | Only this role ([BR-014](../domains/defects/CAP-002-triaging-a-defect.md)) |
| Receive escalations | Emailed when a defect waits too long | [BR-015 and BR-016](../domains/defects/CAP-004-escalating-unactioned-defects.md) |
| Authorise return to service | Put a VOR vehicle back on the road | Only this role ([BR-018](../domains/vehicles/CAP-006-authorising-return-to-service.md)) |

A person can hold several FleetKeep roles at once, for example transport manager and compliance
officer.

## Lifecycle

None. The role is given and removed by the operator's tenant administrator.

## Where it appears

- [Triaging a defect](../domains/defects/CAP-002-triaging-a-defect.md)
- [Escalating unactioned defects](../domains/defects/CAP-004-escalating-unactioned-defects.md)
- [Authorising return to service](../domains/vehicles/CAP-006-authorising-return-to-service.md)
- [From defect report to return to service](../processes/defects/defect-to-return-to-service/PROC-001-defect-to-return-to-service.md)

## Open items

None.

## Sources

- [SRC-001](../sources/SRC-001-2026-09-16-discovery-workshop.md): Discovery workshop, 2026-09-16: role and depot scoping
- [SRC-003](../sources/SRC-003-2026-10-06-jira-sync.md): Jira activity to 2026-10-06: triage (FK-1192) and return to service (FK-1201)
