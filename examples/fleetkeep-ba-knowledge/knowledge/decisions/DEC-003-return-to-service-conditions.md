---
type: decision
id: DEC-003
title: Return to service stays with the transport manager, with no override
status: approved
decided_by: Product owner
decided_on: 2026-10-02
approved_by: Product owner
approved_on: 2026-10-02
owner: Product owner
sources:
  - SRC-003
  - FK-1201
tags:
  - vehicles
created: 2026-10-06
updated: 2026-10-06
---

# Return to service stays with the transport manager, with no override

Only a transport manager can return a VOR vehicle to service, only once every category-A defect on it
is closed and no inspection is overdue, and there is no override.

## Context

[FK-1201](https://northwind.atlassian.net/browse/FK-1201) asked whether a compliance officer, or a
transport manager with a recorded reason, should be able to return a vehicle to service with an
inspection overdue, for example to drive it to the inspection ([SRC-003](../sources/SRC-003-2026-10-06-jira-sync.md)).

## Options considered

| Option | For | Against |
|---|---|---|
| Transport manager only, no override | Clear accountability; matches the licence holder's duty | A vehicle due for inspection can't be released, even to drive it to the inspection |
| Allow an override with a reason | Flexible | Weakens the record an auditor relies on |
| Let a compliance officer authorise as well | Cover when the transport manager is away | Compliance officers can't change operational records |

## Decision

Transport manager only, with no override. The Product owner wrote in FK-1201 comment 3: "Signed off.
Return to service stays with the transport manager alone, every category-A defect closed, no overdue
inspection. No override."

## Consequences

- [CAP-006 Authorising return to service](../domains/vehicles/CAP-006-authorising-return-to-service.md)
  is approved, with BR-018, BR-019 and BR-020.

## Sources

- SRC-003: Jira activity 2026-09-28 to 2026-10-06; FK-1201 comment 3
