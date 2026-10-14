---
type: register
id: REG-rules
title: Business rules
---

# Business rules

Generated from the `rules` property of every capability and process page. Don't edit by hand;
`/review kb` rebuilds it. Each rule is defined, in context, on the page linked.

| Rule | Statement | Defined on | Status |
|---|---|---|---|
| BR-001 | A walkaround check can't be changed once submitted; a correction is a new check, and both stay in the audit trail. | [CAP-001 Reporting a defect from a walkaround check](domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md) | confirmed |
| BR-002 | Every defect has exactly one category: A (immobilising: the vehicle must not be driven), B (repair within 48 hours) or C (monitor, and repair at the next service). | [CAP-001 Reporting a defect from a walkaround check](domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md) | confirmed |
| BR-003 | Reporting a category-A defect sets the vehicle to VOR immediately. | [CAP-001 Reporting a defect from a walkaround check](domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md) | confirmed |
| BR-004 | A driver can submit walkaround checks and report defects only for vehicles assigned to them. | [CAP-001 Reporting a defect from a walkaround check](domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md) | confirmed |
| BR-005 | A defect moves through Reported, Triaged, Job card raised, In progress, Resolved and Closed in that order, without skipping a state, and Closed is final. | [CAP-002 Triaging a defect](domains/defects/CAP-002-triaging-a-defect.md) | confirmed |
| BR-006 | A defect can be rejected only from Triaged, and only with a reason. | [CAP-002 Triaging a defect](domains/defects/CAP-002-triaging-a-defect.md) | confirmed |
| BR-007 | A category-A defect still in Reported or Triaged 4 hours after it was reported is escalated to the transport manager. | [CAP-003 Escalating an unactioned category-A defect](domains/defects/CAP-003-escalating-an-unactioned-category-a-defect.md) | superseded |
| BR-008 | The escalation clock starts when the defect is reported. | [CAP-003 Escalating an unactioned category-A defect](domains/defects/CAP-003-escalating-an-unactioned-category-a-defect.md) | superseded |
| BR-009 | A job card belongs to exactly one vehicle and can bundle several defects, all at the same depot. | [CAP-005 Closing a job card](domains/workshop/CAP-005-closing-a-job-card.md) | draft |
| BR-010 | A job card can be closed only when labour time is recorded, every linked defect is resolved or deferred with a reason, and a technician has signed it. | [CAP-005 Closing a job card](domains/workshop/CAP-005-closing-a-job-card.md) | draft |
| BR-011 | Parts used reduce the depot's stock when the job card is closed, not when they are allocated, and closing fails if stock would fall below zero. | [CAP-005 Closing a job card](domains/workshop/CAP-005-closing-a-job-card.md) | draft |
| BR-012 | Every change to a vehicle, walkaround check, defect or job card is recorded in the audit trail with who made it, when, what changed and, where a reason is required, why. | [PROC-001 From defect report to return to service](processes/defects/defect-to-return-to-service/PROC-001-defect-to-return-to-service.md) | confirmed |
| BR-013 | Compliance records are kept for at least 15 months, and deleting a vehicle keeps its history. | [PROC-001 From defect report to return to service](processes/defects/defect-to-return-to-service/PROC-001-defect-to-return-to-service.md) | confirmed |
| BR-014 | Only a transport manager can triage a defect, reject it or raise a job card for it. | [CAP-002 Triaging a defect](domains/defects/CAP-002-triaging-a-defect.md) | confirmed |
| BR-015 | A category-A defect still in Reported or Triaged 4 hours after it was reported is escalated to the transport manager. | [CAP-004 Escalating unactioned defects](domains/defects/CAP-004-escalating-unactioned-defects.md) | confirmed |
| BR-016 | A category-B defect still in Reported or Triaged 36 hours after it was reported is escalated to the transport manager. | [CAP-004 Escalating unactioned defects](domains/defects/CAP-004-escalating-unactioned-defects.md) | confirmed |
| BR-017 | The escalation clock starts when the defect is reported. | [CAP-004 Escalating unactioned defects](domains/defects/CAP-004-escalating-unactioned-defects.md) | confirmed |
| BR-018 | Only a transport manager can authorise a vehicle's return to service. | [CAP-006 Authorising return to service](domains/vehicles/CAP-006-authorising-return-to-service.md) | approved |
| BR-019 | A vehicle can return to service only when every category-A defect on it is closed. | [CAP-006 Authorising return to service](domains/vehicles/CAP-006-authorising-return-to-service.md) | approved |
| BR-020 | A vehicle with an overdue inspection can't return to service. | [CAP-006 Authorising return to service](domains/vehicles/CAP-006-authorising-return-to-service.md) | approved |
