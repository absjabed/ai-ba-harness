---
type: glossary
id: GLOSSARY
title: Glossary
status: draft
owner: Lead BA
sources: [SRC-001, SRC-002, SRC-003, SRC-007]
created: 2026-10-15
updated: 2026-10-20
---

# Glossary

One section per term, alphabetical. Each term has an ID, one definition, the words people actually
use for it, and its source. Terms the project prefers or avoids are listed in `PROJECT-PROFILE.md`
section 7.

<!-- Entry format:

## <Term>
**T-000** · status: confirmed · (SRC-000)

<One-sentence definition, in business language.>

**Also called:** <synonyms people use, including the "instead of" words from profile section 7>

**Not to be confused with:** <similar term, linked>

**See:** <the page that explains it in context>
-->

## Anchor date
**T-001** · status: confirmed · ([SRC-001](sources/SRC-001-2026-10-02-product-owner-inspection-rules.md))

The date a vehicle's inspection schedule counts from: each due date is the anchor date plus a whole number of the vehicle's inspection intervals.

The anchor date itself is not a due date: the first due date is the anchor date plus one interval (BR-008, [Q-014](questions/Q-014-is-the-anchor-date-a-due-date.md)).

**Also called:** start date (the project prefers "anchor date")

**See:** [Calculating the next inspection due date](domains/inspections/CAP-002-calculating-next-inspection-due-date.md)

## Inspection interval
**T-002** · status: confirmed · (SRC-001)

The number of whole weeks between a vehicle's safety inspections, set separately for each vehicle; there is no fleet-wide interval.

**Also called:** safety inspection interval

**See:** [Setting a vehicle's inspection interval and anchor date](domains/inspections/CAP-001-setting-inspection-interval-and-anchor-date.md)

## Late inspection
**T-003** · status: confirmed · ([SRC-002](sources/SRC-002-2026-10-05-regulator-inspection-guidance.md))

In the regulator guidance, as summarised by the Compliance adviser: an inspection carried out after its due date. The guidance has no grace period.

**Not to be confused with:** overdue, which turns a vehicle red on the dashboard: a vehicle is overdue from the day after a due date that no inspection has met, with no grace period (BR-009, [Q-002](questions/Q-002-grace-period-before-an-inspection-is-overdue.md)).

**See:** [Recording a safety inspection](domains/inspections/CAP-004-recording-a-safety-inspection.md)

## VOR
**T-005** · status: confirmed · ([SRC-003](sources/SRC-003-2026-10-16-defects-workshop.md))

Vehicle off the road: a vehicle that has been taken off the road. A category-A defect makes a vehicle VOR immediately ([DEC-001](decisions/DEC-001-category-a-defect-makes-vehicle-vor.md)); what else does, and how the inspection rules apply to it, is [Q-003](questions/Q-003-inspection-rules-for-vor-vehicles.md).

**Also called:** grounded (the project prefers "VOR")

**See:** [Reporting a defect in a walkaround check](domains/defects/CAP-005-reporting-a-defect-in-a-walkaround-check.md)

## Walkaround check
**T-004** · status: confirmed · ([SRC-003](sources/SRC-003-2026-10-16-defects-workshop.md))

The driver's check of the vehicle before using it.

**Also called:** daily check (the project prefers "walkaround check")

**See:** [Reporting a defect in a walkaround check](domains/defects/CAP-005-reporting-a-defect-in-a-walkaround-check.md)
