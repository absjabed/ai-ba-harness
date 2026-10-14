---
type: capability
id: CAP-001
title: Reporting a defect from a walkaround check
status: confirmed
area: defects
owner: Product owner
sources:
  - SRC-001
  - SRC-002
  - SRC-003
rules:
  - BR-001
  - BR-002
  - BR-003
  - BR-004
aliases:
  - defect report
  - reporting a fault
  - walkaround defect
tags:
  - defects
created: 2026-09-17
updated: 2026-10-06
---

# Reporting a defect from a walkaround check

A driver records any defect found during the walkaround check of an assigned vehicle, so the fault
is on record and, if it is immobilising, the vehicle is taken off the road at once.

## Who and when

| Role | What they do here | When |
|---|---|---|
| Driver | Submits the walkaround check from a phone and reports each defect found, with a photo where it helps | Before using the vehicle |
| Transport manager | Sees the defect waiting for triage, and the vehicle set to VOR if the defect is category A | As soon as the check is submitted |
| Workshop technician | Sees the defect in the depot's workshop queue | As soon as the check is submitted |

## What the user sees

The driver chooses one of the vehicles assigned to them, works through the check and, for each
defect, gives a description, chooses a category and can add a photo. The exact on-screen wording
hasn't been captured yet ([SRC-001](../../sources/SRC-001-2026-09-16-discovery-workshop.md)).

## Inputs

| Input | Required? | Rules |
|---|---|---|
| Vehicle | Yes | Must be assigned to the driver (BR-004) |
| Defect description | Yes, for each defect | Free text |
| Defect category | Yes, for each defect | A, B or C (BR-002) |
| Photo | No | Kept with the defect and visible only inside the operator's own account |

## Rules applied

In the order they are evaluated.

1. **BR-004** A driver can submit walkaround checks and report defects only for vehicles assigned to them. (SRC-001)
2. **BR-002** Every defect has exactly one category: A (immobilising: the vehicle must not be driven), B (repair within 48 hours) or C (monitor, and repair at the next service). (SRC-001)
3. **BR-001** A walkaround check can't be changed once submitted; a correction is a new check, and both stay in the audit trail. (SRC-001)
4. **BR-003** Reporting a category-A defect sets the vehicle to VOR immediately. (SRC-001)

> [!IMPORTANT]
> The regulator's guidance, as summarised by the Compliance adviser, expects a walkaround check
> before a vehicle is used and every defect to be reported in writing. The submitted check is the
> operator's written record of both ([SRC-002](../../sources/SRC-002-2026-09-23-regulator-roadworthiness-guidance.md)).

## Outcomes

- The check and its defects are recorded against the vehicle, with the driver and the time, in the
  audit trail.
- Each defect starts in the Reported state (see [Defect](../../entities/ENT-001-defect.md)) and
  appears in the workshop queue of the vehicle's depot.
- A category-A defect sets the [vehicle](../../entities/ENT-002-vehicle.md) to VOR (BR-003).

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|
| The vehicle isn't assigned to the driver | The vehicle isn't offered, and a report for it is refused | BR-004 |
| The driver wants to change a submitted check | Not possible; they submit a new check as the correction | BR-001 |
| A defect has no category | The check can't be submitted until each defect has one | BR-002 |
| No signal at the depot when submitting | Unresolved: see Q-003 below | None yet |

## Interactions

- [Triaging a defect](CAP-002-triaging-a-defect.md) picks up every reported defect.
- [Escalating unactioned defects](CAP-004-escalating-unactioned-defects.md) alerts the transport
  manager when nobody triages it in time.
- [Authorising return to service](../vehicles/CAP-006-authorising-return-to-service.md) is the only
  way a vehicle set to VOR here goes back on the road.
- The whole journey is in [From defect report to return to service](../../processes/defects/defect-to-return-to-service/PROC-001-defect-to-return-to-service.md).

## Open items

> [!CAUTION]
> **Unresolved:** what happens when a driver submits a walkaround check with no signal at the
> depot. See [Q-003](../../questions/Q-003-walkaround-check-without-a-signal.md).

> [!NOTE]
> **Assumption:** one walkaround check can carry several defects, each with its own category. Not
> yet confirmed ([A-001](../../raid.md#assumptions)).

## Sources

- SRC-001: Discovery workshop on defects, the workshop and return to service, 2026-09-16
- SRC-002: Regulator roadworthiness guidance, summary for FleetKeep, 2026-09-23
- [SRC-003](../../sources/SRC-003-2026-10-06-jira-sync.md): Jira activity to 2026-10-06; links updated to the new escalation and return-to-service pages
