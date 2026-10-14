---
type: capability
id: CAP-006
title: Authorising return to service
status: approved
approved_by: Product owner
approved_on: 2026-10-02
area: vehicles
owner: Product owner
sources:
  - SRC-003
  - FK-1201
  - DEC-003
rules:
  - BR-018
  - BR-019
  - BR-020
aliases:
  - return to service
  - RTS
  - releasing a vehicle
  - putting a vehicle back on the road
tags:
  - vehicles
created: 2026-10-06
updated: 2026-10-06
---

# Authorising return to service

A transport manager authorises a vehicle that was off the road (VOR) to be driven again, once it is
safe and legal to use.

## Who and when

| Role | What they do here | When |
|---|---|---|
| Transport manager | Authorises the return to service | After the defects that made the vehicle VOR are closed |
| Workshop technician | Closes the job cards first; can't authorise | Before the authorisation |

## What the user sees

The transport manager sees the VOR vehicle and can authorise its return to service. If something
still blocks it, the authorisation is refused ([SRC-003](../../sources/SRC-003-2026-10-06-jira-sync.md),
[FK-1201](https://northwind.atlassian.net/browse/FK-1201)). The exact on-screen wording hasn't been
captured yet.

## Inputs

| Input | Required? | Rules |
|---|---|---|
| The vehicle | Yes | Must be VOR |

## Rules applied

In the order they are evaluated.

1. **BR-018** Only a transport manager can authorise a vehicle's return to service. ([DEC-003](../../decisions/DEC-003-return-to-service-conditions.md))
2. **BR-019** A vehicle can return to service only when every category-A defect on it is closed. (DEC-003)
3. **BR-020** A vehicle with an overdue inspection can't return to service. (DEC-003)

> [!IMPORTANT]
> These rules decide whether an immobilised vehicle goes back on the road. They were signed off by
> the Product owner on 2026-10-02 (DEC-003), and there is no override.

> [!WARNING]
> Closing a job card doesn't put a VOR vehicle back on the road. Only the transport manager's
> authorisation does (BR-018).

## Outcomes

- The vehicle is no longer VOR and can be driven.
- It shows in red-band alerts again if a due date passes (VOR vehicles are left out of those
  alerts).
- The authorisation is recorded in the audit trail with who and when.

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|
| A workshop technician or anyone else tries to authorise | Not offered, and refused | BR-018 |
| A category-A defect on the vehicle isn't closed | Refused | BR-019 |
| The vehicle has an overdue inspection | Refused until the inspection is done | BR-020 |

## Interactions

- Follows [Closing a job card](../workshop/CAP-005-closing-a-job-card.md).
- Ends the VOR state set in [Reporting a defect from a walkaround check](../defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md).
- The vehicle's states are on [Vehicle](../../entities/ENT-002-vehicle.md).

## Open items

None.

## Sources

- SRC-003: Jira activity 2026-09-28 to 2026-10-06; FK-1201 comment 3 recorded the sign-off (DEC-003)
