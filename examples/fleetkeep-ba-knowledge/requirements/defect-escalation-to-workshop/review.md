---
type: review
id: REVIEW-defect-escalation-to-workshop
title: Review of Defect escalation to workshop
status: confirmed
owner: Lead BA
sources:
  - REQ-defect-escalation-to-workshop
verdict: ready
reviewed_on: 2026-10-12
---

# Review of Defect escalation to workshop

| Field | Value |
|---|---|
| Document | [requirement.md](requirement.md) |
| Date | 2026-10-12 |
| Verdict | **Ready** |
| Critical | 0 |
| Major | 0 |
| Minor | 4 |

## Findings

| ID | Severity | Where | Finding | Fix |
|---|---|---|---|---|
| F-01 | minor | ST-03, AC-1 | The When step describes a screen action ("I select "Raise job card"") rather than the behaviour | Write "When I raise a job card for the escalated defect" |
| F-02 | minor | Assumptions, A-002 | "usually" is on the profile's list of words that need a measure | Say "at the start of every shift", or keep the vague word and rely on D-001 to confirm it |
| F-03 | minor | NFR-003 | WHILE is used for a rule that always holds; the EARS form without a keyword fits | "FleetKeep shall show a technician only flagged defects for vehicles at their own depots." |
| F-04 | minor | FR-001, FR-002 | Both rest on DEC-002, which is confirmed but not yet approved (recorded second-hand in FK-1192) | Ask the Product owner to confirm DEC-002 in writing before sprint planning |

## Checks

| Check | Result |
|---|---|
| Every story in "As a ... I want ... so that ..." form | Pass |
| At least two Given/When/Then criteria per story, with a failure or permission path where one exists | Pass: ST-01 AC-3, ST-02 AC-3, ST-03 AC-2, ST-04 AC-2 |
| Each FR and NFR is one testable statement | Pass |
| NFRs in EARS form with a measure | Pass, with F-03 |
| Vague words from the profile | F-02 |
| IDs present and unique (FR, NFR, ST, AC) | Pass |
| Fix version and epic present | Pass: 2026.11; the epic is created by /backlog |
| Every BR-, Q-, DEC- and CAP- cited exists in the knowledge base | Pass |
| Contradicts a confirmed or approved rule, term or decision | None found. FR-005 checked against BR-005 |
| Terms used as the glossary defines them (escalation, triage, job card, VOR) | Pass |
| INVEST | Pass. ST-01 is the largest; split it (FR-003 into its own story) if the team estimates it above one sprint |
| Duplicates in Jira | [FK-1192](https://northwind.atlassian.net/browse/FK-1192) is the spike this epic came from: link as "Relates", not a duplicate |
| Open questions blocking a story | None: Q-002 and Q-004 are marked non-blocking by the Lead BA |

## Ready stories

ST-01, ST-02, ST-03, ST-04.
