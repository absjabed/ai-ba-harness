---
type: source
id: SRC-005
title: Engineering lead's email on anchor dates and VOR
status: confirmed
kind: email
input_date: 2026-10-17
created: 2026-10-17
updated: 2026-10-17
---

# Engineering lead's email on anchor dates and VOR

An email from the Engineering lead, written after looking at how the product works today, about anchor dates on re-registered vehicles and recording when a vehicle went VOR.

## Details

| Field | Value |
|---|---|
| Kind | email |
| Date | 2026-10-17 |
| Participants or author | Engineering lead |
| Original | The BA's own copy (`inbox/2026-10-17-email-engineering.md`, not committed) |
| Processed by | /intake on 2026-10-17 |

## Summary

Anchor dates are kept per vehicle today, but nothing stops two vehicles sharing one record when a vehicle is re-registered, which could double up their inspection schedules. The product has no way to record when a vehicle went VOR, so nothing can be paused while a vehicle is off the road. The Engineering lead asks who decides whether the schedule pauses while a vehicle is VOR: the Product owner, through Q-003 (`stakeholders.md`: product behaviour and business rules). Technical pointer: the Engineering lead found both points by reading the code; there is no stored field for the date a vehicle went VOR.

## What it changed

| Item | Change |
|---|---|
| CAP-001 | edited: SRC-005 added as a source, with the re-registration exception |
| R-003 | added: a re-registered vehicle could share a record with another vehicle (Product owner) |
| Q-011 | opened: what happens to a vehicle's record and schedule when it is re-registered (Product owner) |
| Q-003 | edited: the product can't record when a vehicle went VOR; pausing added as a possible answer; still open |

## Play-back

None (an email, not a meeting). The answer to the Engineering lead's question: the Product owner decides, through Q-003.

## Rejected, ignored and declined

None. The critic's optional idea of an Open items note on CAP-001 for the re-registration risk was not part of the suggestion the BA took, so CAP-001 has no such note.
