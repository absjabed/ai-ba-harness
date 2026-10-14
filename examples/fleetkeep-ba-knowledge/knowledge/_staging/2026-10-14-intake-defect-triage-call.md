# Staging: intake defect triage call, 2026-10-14

<!-- Proposed knowledge changes waiting for the BA. Nothing here is in the knowledge base yet.
     Start with the Critic section. Tick one box per item, or answer in the chat ("accept 1-4,
     reject 5, edit 6: ..."). When you say apply (normally once every item is decided), the command
     applies the accepted items and deletes this file, or keeps only the undecided ones. -->

| Field | Value |
|---|---|
| Input | `inbox/2026-10-14-defect-triage-call-notes.md` (the Lead BA's typed notes; never committed) |
| Kind | meeting |
| Source record to create | SRC-new |
| Items | 8 (4 new, 1 confirm, 1 contradict, 1 duplicate, 1 answer) |
| Needs redaction | yes: a driver's name and a vehicle registration in item 4's quote, replaced with "[driver]" and "[registration]" |
| Critic | 4 findings: 3 fixed, 1 for you to check |

## Summary

The weekly defect triage call with the pilot operator, 2026-10-14. The Product owner answered
whether the escalation clock runs at night (it does), which closes Q-002. The Pilot workshop
supervisor argued that category-B defects should escalate at 24 hours rather than 36; they can't
decide that, so it becomes a question for the Product owner. The call also confirmed that category-A
defects take vehicles off the road at once, raised the deferred-defect question again, and named a
new term and a new risk.

**Attendees (by role):** Product owner, Lead BA, Engineering lead, Pilot transport manager, Pilot
workshop supervisor.

**Decisions:**
- The escalation clock keeps running outside working hours. Product owner: **can decide**.
- Category-B defects should escalate at 24 hours. Pilot workshop supervisor: **needs owner**
  (Product owner).

**Actions:**
- Pilot workshop supervisor: send the shift patterns for both pilot depots, by 2026-10-16 (D-001).
- Engineering lead: count the category-B escalations at pilot depots between 22:00 and 06:00 in
  September, by 2026-10-21, to inform the new question in item 2.

## Critic

Ran as a sub-agent with a fresh context, re-reading the notes and searching the knowledge base again.

- **Fixed, item 8 (added by the critic):** the Engineering lead's action to count September's
  overnight category-B escalations was in the summary and the play-back message but had no item, so
  it wouldn't have reached the source record.
- **Fixed, item 1:** the proposed change set Q-002's status but not `state: answered` and
  `answered_on`, so the question would have stayed in the open list.
- **Fixed, item 2:** Q-new-1 had no `blocks`. It now lists CAP-004 and
  REQ-defect-escalation-to-workshop, whose FR-001 cites BR-016.
- **Check, item 1:** "we want someone told whatever the hour" suggests overnight escalations go to
  someone on call, but `stakeholders.md` has no on-call role and BR-015 sends them to the transport
  manager. Consider asking the Product owner who that someone is before accepting.

## Items

### 1. The escalation clock runs outside working hours

| Field | Value |
|---|---|
| Kind | answer |
| Verdict | answers [Q-002](../questions/Q-002-escalation-clock-outside-working-hours.md) |
| Clarity | clear |
| Authority | can decide (Product owner) |
| Sensitivity | clean |
| Quote | "The clock keeps running overnight. If it's category A the vehicle can't move, and we want someone told whatever the hour." (notes ¶3) |
| Critic | fixed: `state: answered` and `answered_on` added; check: who is told overnight (see Critic) |
| Affects delivery | REQ-defect-escalation-to-workshop: ST-01 (FK-1302) and ST-02 (FK-1303) list CAP-004. The requirement treats the clock as out of scope (Q-002 non-blocking), so its stories need no change; update its Current state |
| Proposed change | Fill Q-002's Answer with this, set `state: answered`, `answered_on: 2026-10-14`, `answer_source: SRC-new` and status `approved` (`approved_by: Product owner`, `approved_on: 2026-10-14`); new DEC-new-1 "Escalation clock runs continuously", approved, decided by the Product owner; edit CAP-004: add BR-new-1 and remove the caution callout (diff below) |

```diff
 rules:
   - BR-015
   - BR-016
   - BR-017
+  - BR-new-1
@@ Rules applied
 3. **BR-016** A category-B defect still in Reported or Triaged 36 hours after it was reported is escalated to the transport manager. (FK-1188)
+4. **BR-new-1** The escalation clock runs continuously, including outside depot working hours. (DEC-new-1)
@@ Open items
-> [!CAUTION]
-> **Unresolved:** whether the escalation clock keeps running outside depot working hours, so that a
-> category-A defect reported late in the evening escalates overnight. See
-> [Q-002](../../questions/Q-002-escalation-clock-outside-working-hours.md).
```

- [ ] accept
- [ ] edit:
- [ ] reject:

### 2. Category-B defects should escalate at 24 hours

| Field | Value |
|---|---|
| Kind | rule |
| Verdict | contradicts BR-016 on [CAP-004](../domains/defects/CAP-004-escalating-unactioned-defects.md) (confirmed) |
| Clarity | clear |
| Authority | cannot (Pilot workshop supervisor; owner is Product owner) |
| Sensitivity | clean |
| Quote | "Thirty-six hours is too long for a B. By then it's three quarters of the way to its 48. Make it 24." (notes ¶5) |
| Critic | fixed: `blocks` added to Q-new-1 (CAP-004, REQ-defect-escalation-to-workshop) |
| Affects delivery | REQ-defect-escalation-to-workshop: ST-01 (FK-1302) and ST-02 (FK-1303) list CAP-004, and FR-001 cites BR-016. Nothing changes now; if the Product owner moves BR-016 to 24 hours, at least these two stories change |
| Proposed change | New Q-new-1 "Should category-B defects escalate at 24 hours instead of 36?", asked of the Product owner, due 2026-10-28, `blocks` CAP-004 and REQ-defect-escalation-to-workshop, recording the Pilot workshop supervisor's view. Add a caution callout on CAP-004 linking it. BR-016 stays as it is |

```diff
 ## Open items
 
+> [!CAUTION]
+> **Unresolved:** the Pilot workshop supervisor proposes escalating category-B defects at 24 hours
+> instead of 36 (BR-016). See Q-new-1.
```

- [ ] accept
- [ ] edit:
- [ ] reject:

### 3. Nil-defect check

| Field | Value |
|---|---|
| Kind | term |
| Verdict | new |
| Clarity | clear |
| Authority | not needed (a term) |
| Sensitivity | clean |
| Quote | "Most of what comes in is nil-defect checks. We only look at the ones with something on them." (notes ¶2) |
| Critic | ok |
| Affects delivery | none |
| Proposed change | Add T-new-1 "Nil-defect check": a walkaround check submitted with no defects reported. Also called: clear check, nil return. See: [CAP-001](../domains/defects/CAP-001-reporting-a-defect-from-a-walkaround-check.md) |

- [ ] accept
- [ ] edit:
- [ ] reject:

### 4. A category-A defect takes the vehicle off the road at once

| Field | Value |
|---|---|
| Kind | fact |
| Verdict | confirms CAP-001 (BR-003) |
| Clarity | clear |
| Authority | not needed (a fact) |
| Sensitivity | redact: the driver's name and the vehicle's registration, replaced in the quote |
| Quote | "When [driver] reported the brake fault on [registration] on Monday it went VOR straight away, before I'd even seen it." (Pilot transport manager, notes ¶4) |
| Critic | ok |
| Affects delivery | none |
| Proposed change | Edit CAP-001: add SRC-new to its sources (strengthens BR-003). No change to the text |

```diff
 sources:
   - SRC-001
   - SRC-002
   - SRC-003
+  - SRC-new
```

- [ ] accept
- [ ] edit:
- [ ] reject:

### 5. Where does a deferred defect go?

| Field | Value |
|---|---|
| Kind | question |
| Verdict | duplicate of [Q-004](../questions/Q-004-state-of-a-deferred-defect.md) |
| Clarity | clear |
| Authority | not needed (a question) |
| Sensitivity | clean |
| Quote | "If we defer something on a job card, where does it go? Does it come back on the queue?" (Pilot workshop supervisor, notes ¶6) |
| Critic | ok |
| Affects delivery | REQ-defect-escalation-to-workshop cites Q-004 as non-blocking; adding a source changes nothing for its stories |
| Proposed change | No new question. Edit Q-004: add SRC-new to its sources, as the same question raised again by the workshop |

```diff
 sources:
   - SRC-004
+  - SRC-new
```

- [ ] accept
- [ ] edit:
- [ ] reject:

### 6. Technicians don't read email on shift

| Field | Value |
|---|---|
| Kind | risk |
| Verdict | new |
| Clarity | vague: "on the floor" (no measure of how often email is read) |
| Authority | not needed (a risk) |
| Sensitivity | clean |
| Quote | "My technicians don't look at email on the floor. If it's not on the queue screen they won't see it." (Pilot workshop supervisor, notes ¶7) |
| Critic | ok |
| Affects delivery | none |
| Proposed change | New R-new-1 in raid.md: "Technicians don't read email during a shift, so escalation emails alone don't reach the workshop". Likelihood high, impact medium, mitigation: the queue flag in [Defect escalation to workshop](../../requirements/defect-escalation-to-workshop/requirement.md) (ST-01), owner Product owner. Also bears on A-003 |

- [ ] accept
- [ ] edit:
- [ ] reject:

### 7. Shift patterns for the pilot depots

| Field | Value |
|---|---|
| Kind | action |
| Verdict | new |
| Clarity | clear |
| Authority | not needed (an action) |
| Sensitivity | clean |
| Quote | "I'll send over the shift rota for both depots by Friday." (Pilot workshop supervisor, notes ¶8) |
| Critic | ok |
| Affects delivery | none |
| Proposed change | New ACT-new-1 in the Actions table of raid.md: "Send the shift patterns for both pilot depots", owner Pilot workshop supervisor, due 2026-10-16, status open. It fulfils D-001. `/backlog task` can make it a Jira task if the BA wants one |

- [ ] accept
- [ ] edit:
- [ ] reject:

### 8. Overnight category-B escalations in September (added by the critic)

| Field | Value |
|---|---|
| Kind | action |
| Verdict | new |
| Clarity | clear |
| Authority | not needed (an action) |
| Sensitivity | clean |
| Quote | "I can pull how many B escalations would have fired overnight in September. Give me a week." (Engineering lead, notes ¶5) |
| Critic | fixed: item added; it was in the summary but missing from the items |
| Affects delivery | none |
| Proposed change | New ACT-new-2 in the Actions table of raid.md: "Count category-B escalations at the pilot depots between 22:00 and 06:00 in September", owner Engineering lead, due 2026-10-21, status open. It informs Q-new-1 (item 2). `/backlog task` can make it a Jira task if the BA wants one |

- [ ] accept
- [ ] edit:
- [ ] reject:

## Play-back message (optional)

> Thanks for today's triage call. Here is what we captured; please reply by Friday 2026-10-16 if
> anything is wrong.
>
> - The escalation clock keeps running overnight and at weekends: a category-A defect is escalated
>   4 hours after it is reported, whatever the hour (Product owner).
> - Proposal to escalate category-B defects at 24 hours instead of 36: recorded as a question for the
>   Product owner, due 2026-10-28. Nothing changes until it is decided.
> - Open question still with the Product owner: what happens to a defect deferred on a job card.
> - Actions: the Pilot workshop supervisor sends both depots' shift patterns by 2026-10-16; the
>   Engineering lead counts September's overnight category-B escalations by 2026-10-21.
