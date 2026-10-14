---
type: source
id: SRC-007
title: Product owner's sign-off of the inspection scheduling requirement
status: confirmed
kind: email
input_date: 2026-10-20
created: 2026-10-20
updated: 2026-10-20
---

# Product owner's sign-off of the inspection scheduling requirement

The Product owner's email of 2026-10-20 approving the inspection scheduling and dashboard requirement for 2026.12, including every proposal it marked pending.

## Details

| Field | Value |
|---|---|
| Kind | email |
| Date | 2026-10-20 |
| Participants or author | Product owner |
| Original | The BA's own copy (`inbox/2026-10-20-po-signoff.md`, not committed) |
| Processed by | /intake on 2026-10-20 |

## Summary

The Product owner read the [Inspection scheduling and dashboard](../../requirements/inspection-scheduling-and-dashboard/requirement.md) requirement and approved it for fix version 2026.12 "as written, including all the proposals marked pending in it". The Product owner can decide product behaviour, business rules and release content, and the email itself was the input, so the requirement is approved and each pending proposal (Q-001, Q-002, Q-012 to Q-016) is answered with its proposed answer and became a rule. Two points the proposals had left open are asked again: the order among overdue vehicles (from Q-016) and whether a vehicle is measured against its due date on that day (from Q-001).

## What it changed

| Item | Change |
|---|---|
| REQ-inspection-scheduling-and-dashboard | approved by the Product owner, 2026-10-20; FR-006 to FR-010 and FR-013 to FR-019 changed from pending to agreed |
| Q-014 | answered (approved): the anchor date is not a due date; BR-008 on CAP-002 |
| Q-002 | answered (approved): no grace period; BR-009 on CAP-003 |
| Q-001 | answered (approved): which due date an inspection meets and which is next, and when an overdue ends; BR-010 and BR-011 on CAP-002, BR-012 and BR-013 on CAP-003 |
| Q-015 | answered (approved): calendar days; BR-014 on CAP-003 |
| Q-013 | answered (approved): grey, "Not scheduled"; BR-015 on CAP-003 |
| Q-016 | answered (approved), except the order among overdue vehicles: BR-016 and BR-017 on CAP-003 |
| Q-018 | opened: the order the dashboard lists overdue vehicles in (Product owner), blocks CAP-003 |
| Q-012 | answered (approved): transport managers and compliance officers; BR-018 on CAP-003 |
| CAP-002 | edited: BR-008, BR-010, BR-011; cautions for Q-001 and Q-014 removed |
| CAP-003 | edited: BR-009, BR-012 to BR-018, who sees it, what the user sees; cautions for Q-001, Q-002, Q-012, Q-013, Q-015 and Q-016 removed, caution for Q-018 added |
| ENT-001 | edited: can see the inspection dashboard (BR-018) |
| ENT-002 | edited: can see the inspection dashboard, read only (BR-018); caution for Q-012 removed |
| R-001 | closed: Q-002 settled with no grace period |
| T-001 | edited: the anchor date itself is not a due date (BR-008) |
| T-003 | edited: overdue starts the day after an unmet due date, no grace period (BR-009) |
| Q-019 | opened: whether a vehicle is measured against its due date on that day (Product owner), non-blocking (added by the critic) |

## Play-back

None: an email from the person who decides; no meeting to play back.

## Rejected, ignored and declined

None. All 12 staged items were accepted, and the BA took every critic suggestion (the `Affects delivery` rows of items 7 and 9; item 12, Q-019, added by the critic).
