---
type: capability
id: CAP-005
title: Closing a job card
status: draft
area: workshop
owner: Product owner
sources:
  - SRC-001
  - SRC-004
rules:
  - BR-009
  - BR-010
  - BR-011
aliases:
  - signing off a job card
  - completing a job
  - closing a work order
tags:
  - workshop
created: 2026-09-17
updated: 2026-10-09
---

# Closing a job card

A workshop technician closes a job card once the work on the vehicle is done, recording labour,
parts and the outcome of each defect, so the repair is on record and depot stock stays accurate.

## Who and when

| Role | What they do here | When |
|---|---|---|
| Workshop technician | Records labour time and parts used, resolves or defers each linked defect, and signs the job card | When the work on the vehicle is finished |
| Transport manager | Authorises return to service if the vehicle was VOR | After the job card is closed |

## What the user sees

The technician sees the job card with its linked defects, the labour and parts recorded so far, and
a way to sign and close it ([SRC-001](../../sources/SRC-001-2026-09-16-discovery-workshop.md)). The
exact on-screen wording hasn't been captured yet.

## Inputs

| Input | Required? | Rules |
|---|---|---|
| Labour time | Yes | BR-010 |
| Outcome of each linked defect | Yes | Resolved, or deferred with a reason (BR-010) |
| Parts used | When parts were used | Taken from the depot's stock at closure (BR-011) |
| Technician's signature | Yes | The technician who is signed in (BR-010) |

## Rules applied

In the order they are evaluated.

1. **BR-009** A job card belongs to exactly one vehicle and can bundle several defects, all at the same depot. (SRC-001)
2. **BR-010** A job card can be closed only when labour time is recorded, every linked defect is resolved or deferred with a reason, and a technician has signed it. (SRC-001)
3. **BR-011** Parts used reduce the depot's stock when the job card is closed, not when they are allocated, and closing fails if stock would fall below zero. (SRC-001)

## Outcomes

- The job card is closed and signed; each linked defect is resolved or deferred.
- Depot stock goes down by the parts used. A part that falls below its reorder level raises a
  reorder alert at FleetKeep's next scheduled check.
- If the vehicle was VOR it stays VOR until a transport manager
  [authorises its return to service](../vehicles/CAP-006-authorising-return-to-service.md).

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|
| No labour time recorded | Closing is refused | BR-010 |
| A linked defect is neither resolved nor deferred with a reason | Closing is refused | BR-010 |
| Not enough stock for the parts used | Closing fails with a message; stock is unchanged | BR-011 |

## Interactions

- Job cards are raised in [Triaging a defect](../defects/CAP-002-triaging-a-defect.md).
- The defect states are on [Defect](../../entities/ENT-001-defect.md).
- Followed by [Authorising return to service](../vehicles/CAP-006-authorising-return-to-service.md)
  for VOR vehicles.

## Open items

Kept as draft: the rules come from the Pilot workshop supervisor's description in SRC-001 and
haven't yet been checked against the product.

> [!CAUTION]
> **Unresolved:** which state a deferred defect takes when its job card closes, since the defect
> states have no "deferred" state, and whether it returns to the workshop queue. See
> [Q-004](../../questions/Q-004-state-of-a-deferred-defect.md).

## Sources

- SRC-001: Discovery workshop on defects, the workshop and return to service, 2026-09-16
- SRC-004: Requirements session on defect escalation to the workshop, 2026-10-09, which raised Q-004
