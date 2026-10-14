---
type: capability
id: CAP-002
title: Triaging a defect
status: confirmed
area: defects
owner: Product owner
sources:
  - SRC-001
  - SRC-003
  - FK-1192
rules:
  - BR-005
  - BR-006
  - BR-014
aliases:
  - defect triage
  - reviewing a defect
  - assessing a defect
tags:
  - defects
created: 2026-09-17
updated: 2026-10-06
---

# Triaging a defect

The transport manager looks at each reported defect and either raises a job card for it or rejects
it with a reason, so every defect gets a decision and none is lost.

## Who and when

| Role | What they do here | When |
|---|---|---|
| Transport manager | Triages the defect: raises a job card or rejects it with a reason | After a driver reports it; before it escalates |
| Workshop technician | Starts work once a job card is raised; can't triage | After triage |

## What the user sees

The transport manager sees the defects waiting for triage at their depots. For each one they can
raise a job card for the vehicle, or reject the defect and give a reason
([SRC-001](../../sources/SRC-001-2026-09-16-discovery-workshop.md)). The exact on-screen wording
hasn't been captured yet.

## Inputs

| Input | Required? | Rules |
|---|---|---|
| Triage outcome | Yes | Raise a job card, or reject (BR-005, BR-006) |
| Rejection reason | Yes, when rejecting | Free text (BR-006) |

## Rules applied

In the order they are evaluated.

1. **BR-014** Only a transport manager can triage a defect, reject it or raise a job card for it. ([SRC-003](../../sources/SRC-003-2026-10-06-jira-sync.md), [FK-1192](https://northwind.atlassian.net/browse/FK-1192))
2. **BR-005** A defect moves through Reported, Triaged, Job card raised, In progress, Resolved and Closed in that order, without skipping a state, and Closed is final. (SRC-001)
3. **BR-006** A defect can be rejected only from Triaged, and only with a reason. (SRC-001)

## Outcomes

- **Job card raised:** the defect moves to Triaged and then Job card raised, and is linked to a job
  card for the vehicle, which can bundle other defects at the same depot (see
  [Closing a job card](../workshop/CAP-005-closing-a-job-card.md)).
- **Rejected:** the defect moves to Rejected with the reason recorded.
- Either way the defect stops counting towards [escalation](CAP-004-escalating-unactioned-defects.md),
  and each state change is in the audit trail.

## Failure and blocked paths

| Situation | What happens | Rule |
|---|---|---|
| A workshop technician tries to triage | Triage isn't offered to them | BR-014 |
| Rejecting without a reason | Refused until a reason is given | BR-006 |
| Rejecting a defect still in Reported | It must be triaged first | BR-006 |
| Moving a defect straight from Reported to Job card raised | Not allowed as one jump; it passes through Triaged | BR-005 |

## Interactions

- Fed by [Reporting a defect from a walkaround check](CAP-001-reporting-a-defect-from-a-walkaround-check.md).
- Watched by [Escalating unactioned defects](CAP-004-escalating-unactioned-defects.md).
- The states are drawn on [Defect](../../entities/ENT-001-defect.md); the role is described on
  [Transport manager](../../entities/ENT-003-transport-manager.md).

## Open items

None. Who may triage was asked in [Q-001](../../questions/Q-001-who-can-triage-a-defect.md) and
answered on 2026-10-06 (BR-014).

## Sources

- SRC-001: Discovery workshop on defects, the workshop and return to service, 2026-09-16
- SRC-003: Jira activity 2026-09-28 to 2026-10-06; FK-1192 comment 4 answered Q-001
