---
type: glossary
id: GLOSSARY
title: Glossary
status: confirmed
owner: Lead BA
sources:
  - SRC-001
  - SRC-002
  - SRC-003
created: 2026-09-17
updated: 2026-10-06
---

# Glossary

One section per term, alphabetical. Each term has an ID, one definition, the words people actually
use for it, and its source. Terms the project prefers or avoids are listed in `PROJECT-PROFILE.md`
section 7.

<!-- Entry format:

## <Term>
**T-000** · status: draft · (SRC-000)

<One-sentence definition, in business language.>

**Also called:** <synonyms people use>
**Not to be confused with:** <similar term, linked>
**See:** <the page that explains it in context>
-->

## Anchor date
**T-010** · status: confirmed · ([SRC-001](sources/SRC-001-2026-09-16-discovery-workshop.md))

The date a vehicle's inspection schedule is counted from; every due date is a whole number of
inspection intervals after it, whatever date the last inspection was actually done.

**Also called:** schedule anchor, base date, start date
**Not to be confused with:** the date the last inspection was completed, which never moves the schedule unless a transport manager re-anchors it
**See:** [Vehicle](entities/ENT-002-vehicle.md)

## Audit pack
**T-012** · status: confirmed · ([SRC-002](sources/SRC-002-2026-09-23-regulator-roadworthiness-guidance.md))

A date-ranged export, for one vehicle or one depot, of every walkaround check, defect and job card,
produced so an operator can show an auditor the full history.

**Also called:** audit export, DVSA pack, inspection pack
**Not to be confused with:** the audit trail, which is the record the pack is built from
**See:** [From defect report to return to service](processes/defects/defect-to-return-to-service/PROC-001-defect-to-return-to-service.md)

## Compliance banding
**T-011** · status: confirmed · (SRC-001)

The red, amber or green band a vehicle shows for its nearest due date: green with more than 14 days
to go, amber with 14 days or fewer, red once the date has passed.

**Also called:** RAG status, red/amber/green, compliance status
**Not to be confused with:** VOR, which is about whether the vehicle may be driven, not about due dates
**See:** [Vehicle](entities/ENT-002-vehicle.md)

## Defect
**T-002** · status: confirmed · (SRC-001)

A fault on a vehicle, reported by a driver in a walkaround check, that has a category and moves
through a fixed set of states until it is closed or rejected.

**Also called:** fault, defect report, reported fault
**Not to be confused with:** a job card, which is the workshop's work to fix one or more defects
**See:** [Defect](entities/ENT-001-defect.md)

## Defect category
**T-003** · status: confirmed · (SRC-001)

The seriousness of a defect: A (immobilising: the vehicle must not be driven), B (repair within 48
hours) or C (monitor, and repair at the next service).

**Also called:** severity, A/B/C rating, defect grade
**Not to be confused with:** compliance banding, which is about inspection due dates
**See:** [Reporting a defect from a walkaround check](domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md)

## Depot
**T-009** · status: confirmed · (SRC-001)

A site where an operator keeps and maintains vehicles; vehicles, drivers, technicians, stock and job
cards each belong to one depot, and most people only see the depots they are assigned to.

**Also called:** site, yard, base
**Not to be confused with:** the operator, which is the whole organisation (one tenant) and can have several depots
**See:** [Transport manager](entities/ENT-003-transport-manager.md)

## Escalation
**T-008** · status: confirmed · (SRC-001)

The automatic alert FleetKeep sends when a category-A or category-B defect has had no triage outcome
for longer than its category allows.

**Also called:** chase, defect alert, overdue defect alert
**Not to be confused with:** a red compliance band, which is about an overdue inspection
**See:** [Escalating unactioned defects](domains/defects/CAP-004-escalating-unactioned-defects.md)

## Job card
**T-006** · status: confirmed · (SRC-001)

The workshop's record of the work on one vehicle: the defects it fixes, the labour and parts used,
and the technician's signature when it is closed.

**Also called:** work order, job sheet, workshop ticket
**Not to be confused with:** a defect, which is the fault itself
**See:** [Closing a job card](domains/workshop/CAP-005-closing-a-job-card.md)

## Return to service
**T-007** · status: confirmed · (SRC-001)

The transport manager's authorisation that a vehicle that was off the road (VOR) may be driven
again.

**Also called:** RTS, release, back on the road, sign-off
**Not to be confused with:** closing a job card, which on its own does not put a VOR vehicle back on the road
**See:** [Authorising return to service](domains/vehicles/CAP-006-authorising-return-to-service.md)

## Triage
**T-005** · status: confirmed · (SRC-001)

The transport manager's first look at a reported defect, which ends in either raising a job card or
rejecting the defect with a reason.

**Also called:** defect review, assessing a defect, screening
**Not to be confused with:** escalation, which happens when triage hasn't happened in time
**See:** [Triaging a defect](domains/defects/CAP-002-triaging-a-defect.md)

## VOR
**T-004** · status: confirmed · (SRC-001)

Vehicle off road: a vehicle that must not be driven, set automatically when a category-A defect is
reported, until a transport manager authorises its return to service.

**Also called:** off road, grounded, immobilised, parked up
**Not to be confused with:** a deleted vehicle, which has left the fleet but keeps its history
**See:** [Vehicle](entities/ENT-002-vehicle.md)

## Walkaround check
**T-001** · status: confirmed · (SRC-001)

The check a driver does on a vehicle before using it, submitted in FleetKeep from a phone, in which
any defects found are reported.

**Also called:** daily check, walkround, first-use check, driver check
**Not to be confused with:** a statutory inspection, which is done by the workshop on a fixed interval
**See:** [Reporting a defect from a walkaround check](domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md)
