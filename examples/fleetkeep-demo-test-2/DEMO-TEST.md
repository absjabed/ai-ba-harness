# About this folder

The raw output of the second demo test (of 0.5.0, leading to 0.5.1), kept as it was left. For a
curated example use [`../fleetkeep-ba-knowledge/`](../fleetkeep-ba-knowledge/EXAMPLE.md). The method
and findings are in [`research/09-second-demo-test.md`](../../research/09-second-demo-test.md); the
first test is in [`../fleetkeep-demo-test/`](../fleetkeep-demo-test/DEMO-TEST.md).

## What it is

"FleetKeep Demo", a fresh project created from harness 0.5.0, with a shared remote and three clones:
the Lead BA's (this folder), a second BA's and a developer's. Every command was run on it by a
sub-agent following the command files exactly, without Atlassian. Twice during the run the clone was
updated to the fixes made so far ("0.5.1 pre-release"), so later commands ran on newer definitions.

- **The harness files here are a snapshot,** not the current harness. Use `project/` for that.
- **Its git history isn't kept;** the commits are listed below. The scenario's dates (16 to 22
  October) are in the commit messages; the commit dates are the machine's.
- **Everything in it is fictional,** including the names and contact details in the test inputs,
  which were planted to test redaction.

## What to look at

| What | Where |
|---|---|
| Every input, as the BAs and the developer received it | [`test-input/`](test-input/) (in a real project these sit in `inbox/` and are never committed) |
| The developer's proposal, as committed on their branch for a pull request; never applied | [`test-input/teammate-proposal-branch-kb-stage-dashboard-anchor-dates.md`](test-input/teammate-proposal-branch-kb-stage-dashboard-anchor-dates.md) |
| The knowledge base: 42 pages from two seeded documents, a workshop, three emails, a sign-off and a rule change | [`knowledge/index.md`](knowledge/index.md) |
| A rule retired and replaced after sign-off (BR-004 by BR-019) | [`knowledge/business-rules.md`](knowledge/business-rules.md), [`knowledge/decisions/`](knowledge/decisions/) |
| SRC-005, renumbered from SRC-004 after two BAs pushed at once | [`knowledge/sources/`](knowledge/sources/) |
| A requirement signed off, then changed and back to draft with four new proposals | [`requirements/inspection-scheduling-and-dashboard/`](requirements/inspection-scheduling-and-dashboard/requirement.md) |
| The change log | [`knowledge/log.md`](knowledge/log.md) |

`python tools/kb.py check` passes here with no errors.

## Its commits, newest first

| Commit | Date | Message |
|---|---|---|
| `4dd67cf` | 2026-10-15 | req: update inspection-scheduling-and-dashboard SRC-009 amber 21 days, back to draft |
| `4b97df2` | 2026-10-15 | kb: intake SRC-008 product owner amber band change 2026-10-22 |
| `f653808` | 2026-10-15 | harness: update to 0.5.1 pre-release (2) |
| `323ba08` | 2026-10-15 | req: review inspection-scheduling-and-dashboard not-ready |
| `b280d93` | 2026-10-15 | kb: intake SRC-007 product owner sign-off inspection scheduling 2026-10-20 |
| `5a228c1` | 2026-10-15 | harness: update to 0.5.1 pre-release |
| `608a1bc` | 2026-10-15 | req: draft inspection-scheduling-and-dashboard |
| `cd3c5dd` | 2026-10-15 | kb: intake SRC-004 engineering lead email anchor dates and VOR 2026-10-17 (by the second BA; renumbered to SRC-005 in the push recovery, message not corrected) |
| `398a9b1` | 2026-10-15 | kb: intake SRC-004 compliance adviser brake test email 2026-10-17 |
| `8466de1` | 2026-10-15 | kb: intake SRC-003 defects workshop 2026-10-16 (applied by the second BA from the committed staging file) |
| `c131a33` | 2026-10-15 | kb: stage 2026-10-16-intake-defects-workshop.md |
| `9bf9768` | 2026-10-15 | kb: kb-seed SRC-002 compliance adviser regulator guidance 2026-10-05 |
| `59e5ccc` | 2026-10-15 | kb: kb-seed SRC-001 product owner inspection rules 2026-10-02 |
| `b5e535d` | 2026-10-15 | kb: setup fleetkeep-demo-ba-knowledge |
| `4c06973` | 2026-10-15 | Start from AI BA Harness 0.5.0 |
