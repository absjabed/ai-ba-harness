---
type: source
id: SRC-008
title: Product owner's email changing the amber band to 21 days
status: confirmed
kind: email
input_date: 2026-10-22
created: 2026-10-22
updated: 2026-10-22
---

# Product owner's email changing the amber band to 21 days

The Product owner's email of 2026-10-22 changing the dashboard's amber band from 14 to 21 days before a vehicle's next due date, two days after signing off the inspection scheduling and dashboard requirement.

## Details

| Field | Value |
|---|---|
| Kind | email |
| Date | 2026-10-22 |
| Participants or author | Product owner |
| Original | The BA's own copy (`inbox/2026-10-22-po-change.md`, not committed) |
| Processed by | /intake on 2026-10-22 |

## Summary

A "change of plan on the dashboard": amber should start at 21 days, not 14, because customers want more notice. Green stays "more than that" and red stays overdue. The Product owner can decide business rules and the email itself was the input, so it is recorded as an approved decision (DEC-003) that retires BR-004 and replaces it with BR-019. The [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) requirement, approved on 2026-10-20, still states the 14 days and needs updating through `/requirements`. The RACI for a change to a business rule lists the Compliance adviser and the Engineering lead as Consulted and the Pilot transport manager as Informed; the email doesn't show them consulted.

## What it changed

| Item | Change |
|---|---|
| DEC-003 | created (approved by the Product owner, 2026-10-22): amber starts 21 days before a vehicle's next due date |
| BR-004 | superseded by BR-019 (DEC-003), struck through on CAP-003 and removed from its `rules` |
| BR-019 | created on CAP-003: green more than 21 days away, amber 21 days away or less, red when overdue |
| CAP-003 | edited: BR-004 retired, BR-019 added, "What the user sees" cites BR-019 |
| Q-019 | edited: cites BR-019 instead of BR-004; amber on the due day now applies to intervals of 3 weeks or less |

## Play-back

None: an email from the person who decides; no meeting to play back.

## Rejected, ignored and declined

None. The one staged item was accepted with all three of the critic's suggestions (the RACI note in the Authority row, and two Consequences bullets on DEC-003); the critic's `fix` (a fuller delivery impact) was applied before the BA decided.
