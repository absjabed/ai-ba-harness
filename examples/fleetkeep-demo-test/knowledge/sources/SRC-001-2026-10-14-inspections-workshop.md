---
type: source
id: SRC-001
title: Inspections workshop
status: confirmed
kind: meeting
input_date: 2026-10-14
created: 2026-10-14
updated: 2026-10-14
---

# Inspections workshop

The Lead BA's notes from the inspections workshop of 2026-10-14, which settled how the safety
inspection schedule and its dashboard banding work; the project's first knowledge input.

## Details

| Field | Value |
|---|---|
| Kind | meeting |
| Date | 2026-10-14 |
| Participants or author | Product owner, Lead BA, Compliance adviser, Pilot transport manager (pilot customer), Engineering lead. Notes by the Lead BA |
| Original | The Lead BA's own notes; not kept in this repository |
| Processed by | /intake on 2026-10-14 |

## Summary

Every vehicle has its own safety inspection interval; the pilot customer uses 6 weeks for HGVs and
8 weeks for vans, and the Compliance adviser said the regulator expects the interval written down
per vehicle, not per fleet. The Product owner decided that the next due date counts from the anchor
date, so neither a late nor an early inspection moves the schedule; the pilot transport manager,
who moves the date forward after an early inspection today, wasn't convinced. The Product owner
agreed green/amber/red banding on the dashboard (more than 14 days, 14 days or less, overdue). The
Compliance adviser said a brake performance test is needed at every safety inspection. Left open:
the due date while a vehicle is VOR, whether closing an inspection without a brake test result is
blocked (the Product owner leans yes and will check with the pilot), and how fast the dashboard must
load for large fleets. Two actions were agreed, and "anchor date" was defined.

## What it changed

| Item | Change |
|---|---|
| [CAP-001](../domains/vehicles/CAP-001-setting-a-vehicles-safety-inspection-interval.md) | created, with BR-001 and the regulator callout |
| [CAP-002](../domains/inspections/CAP-002-calculating-the-next-inspection-due-date.md) | created, with BR-002 |
| [CAP-003](../domains/inspections/CAP-003-seeing-inspection-due-status-on-the-dashboard.md) | created, with BR-003 |
| [CAP-004](../domains/inspections/CAP-004-recording-a-safety-inspection.md) | created, with BR-004 |
| [DEC-001](../decisions/DEC-001-due-date-counts-from-the-anchor-date.md) | created (approved, Product owner) |
| [DEC-002](../decisions/DEC-002-inspection-due-banding.md) | created (approved, Product owner) |
| [Q-001](../questions/Q-001-due-date-while-a-vehicle-is-vor.md) | opened, asked of the Product owner |
| [Q-002](../questions/Q-002-block-closing-an-inspection-without-a-brake-test.md) | opened, asked of the Product owner |
| [Q-003](../questions/Q-003-dashboard-load-time-for-large-fleets.md) | opened, asked of the Product owner |
| R-001 | added to [raid.md](../raid.md#risks) |
| ACT-001, ACT-002 | added to [raid.md](../raid.md#actions) |
| T-001 | added to [glossary.md](../glossary.md#anchor-date): anchor date |

## Rejected items

No item was rejected. Not stored, so they aren't proposed again:

- The attendee list's personal details (the pilot transport manager's name and mobile number):
  ignored as personal data; only the roles are kept, above.
- `ACT-` rows for the Product owner's two undated commitments ("think about" the due date while a
  vehicle is VOR; "check with the pilot" on blocking closure): declined by the Lead BA; Q-001 and
  Q-002 track them.
- A glossary entry for "VOR": declined by the Lead BA; the notes don't define it.
