# The knowledge pipeline: extract, judge, stage, critique, confirm, apply

Shared by `/kb-seed`, `/intake`, `/sync` and `/requirements`. It is how anything gets into
`knowledge/`. The rules it enforces are in `knowledge/_meta/conventions.md`; read that first.

## 0. Prepare

1. `git pull --ff-only`. If it fails (local changes or diverged history), stop and tell the BA what
   to do; don't stage against an out-of-date copy.
2. Read `knowledge/index.md`, `knowledge/glossary.md`, `knowledge/stakeholders.md`, `knowledge/raid.md`
   and the three registers. Keep the list of existing IDs at hand.
3. **When resuming a staging file,** do steps 1 and 2 as well, then look at what changed in
   `knowledge/` since the file's date (`git log --since=<date> -- knowledge/`). Re-judge any item
   whose subject was touched, and tell the BA which verdicts changed.

## 1. Extract

Go through the input once and pull out candidate items. Each item needs:

- **a quote:** the exact words, or the closest short passage. Staging files get committed and
  shared, so names and contact details in a quote are replaced by the role in square brackets:
  `"[Pilot transport manager] said they move it forward"`, `"[number removed]"`;
- **a location:** file and paragraph, line or bullet (`notes, bullet 3`), transcript timestamp, Jira
  key and comment number, Confluence page and section.

| Kind | What it looks like |
|---|---|
| requirement | Something the product must do or be, measurable or not |
| rule | A condition, threshold, ordering, permission or calculation the product applies |
| decision | A choice made by someone, with or without authority |
| action | Someone will do something, ideally by a date; or reports that an action is done |
| approval | A stakeholder signs off a requirement document |
| question | Something nobody could answer, or that people disagreed on |
| answer | A reply to an existing open question |
| term | A word with a project-specific meaning, or a synonym for an existing term |
| risk | Something that might go wrong (also assumptions, issues, dependencies) |
| fact | How something works today, who someone is, what a system does, what a regulator or contract requires |

Leave out chit-chat, scheduling logistics and anything already captured identically. A promise
without a date ("I'll think about it") is an action with no due date, or, when it is really a
question for that person, a question; don't record it twice.

## 2. Judge

For every item, record four verdicts.

**Against the knowledge base.** Search the index, the glossary (including aliases), the pages and
pending staging files for the subject, with at least two different wordings. Record the wordings in
the item's `Searched for` row.

| Verdict | When |
|---|---|
| `new` | Nothing on this subject exists |
| `confirms <ID>` | It says the same as an existing item (this strengthens its sources) |
| `extends <ID>` | It adds detail without conflicting |
| `contradicts <ID>` | It conflicts with an existing item. If that item is `confirmed` or `approved`, the change can only be a new question or a decision awaiting an approver (conventions, rule 4) |
| `duplicate of <ID>` | It repeats something already captured from this same source, or a pending staging file |
| `answers <Q-ID>` | It answers an open question |

An item that adds to a page another item in the same file creates is `new`, with a `Depends on`
row naming that item.

**Clarity.**
- `clear`;
- `vague: "<word>"`, using the words in `PROJECT-PROFILE.md` section 7;
- `incomplete: <what's missing>`, such as the error case, who, or a number.

A vague or incomplete item can't be accepted on its own: its proposed change also opens a question
or adds an Open items note naming what is missing.

**Authority** (decisions, answers, approvals, and rules or permissions someone states as settled;
`n/a` for other kinds). Look the speaker's role up in `stakeholders.md`: the "Can decide" column,
and the RACI row for that kind of decision. A rule stated by someone who can't decide it is staged
as a question to the owner, with their wording as the proposed answer. An approval passed on by
someone else ("the Product owner agreed by email") is second-hand: `confirmed`, not `approved`,
unless the message itself is the input (in `inbox/`, or a Jira comment).
- `can decide (<role>)`, when both say so;
- `cannot (<role>; owner is <role>)`;
- `unknown`, when the speaker or the owner isn't in the register, or the column and the RACI
  disagree. Say which, so the BA can fix `stakeholders.md`.

**Sensitivity.**
- `clean`;
- `redact: <what>`, for personal names where a role would do, contact details, health or customer
  data, credentials, or anything marked confidential.

## 3. Stage

Write one file, `knowledge/_staging/<yyyy-mm-dd>-<command>-<slug>.md`, from
`knowledge/_meta/templates/staging.md`. The slug is the input's subject in at most five words,
without dates or words like "notes" and "minutes": `inspections-workshop`.

For every item, state the exact proposed change:

| Situation | Proposed change |
|---|---|
| A new page of any kind (capability, process, entity, question) | Create `CAP-new-n`, `PROC-new-n`, `ENT-new-n` or `Q-new-n` in the right folder from its template. Put the **whole proposed page** in the item, in a `<details>` block, so the BA accepts exactly what will be written |
| New detail on an existing page | Edit `<ID>` with a diff of the exact lines |
| A rule | Add it to the page that applies it, as `BR-new-n`, and list it in that page's `rules` |
| A measurable requirement | A rule, or a line on the page it belongs to, citing the source |
| A requirement without a measure | `Q-new-n` (in full) asking for the measure, and a `[!CAUTION]` callout in the page's Open items |
| A fact | A line on the page it describes. What a regulator or contract requires becomes a `[!IMPORTANT]` callout citing the source |
| A decision by someone who can decide | Create `DEC-new-n` (with its full text, like a new page) and update the pages it affects |
| A decision by someone who can't | Create `Q-new-n` addressed to the owner, recording the view |
| A contradiction of a confirmed or approved item | Create `Q-new-n` linking both, and add a `[!CAUTION]` callout in the affected page's Open items. Never edit the confirmed text |
| An answer to `Q-xxx` | Fill the question's Answer section; set `state: answered`, `answered_on` and `answer_source`, and `status: approved` with `approved_by` and `approved_on` if the person could decide it (no separate decision page is needed); update the pages it unblocks and remove their caution callouts. `blocks` stays, as a record of what the answer unblocked |
| A term | Add a `T-new-n` glossary entry, or add the word to an existing term's "Also called" and to the page's `aliases` |
| A risk, assumption, issue or dependency | A new row in `raid.md` |
| An action | A new `ACT-new-n` row in the Actions table of `raid.md`, with owner, due date (or "none given") and source. `/backlog task ACT-<n>` can turn it into a Jira task later |
| An action reported done | Set its `ACT-` row's status to `done` |
| A sign-off of a requirement by someone who can approve it | Set the requirement's `status: approved`, `approved_by` and `approved_on`, and add the source to its `sources`. Every question the requirement marks "pending" is answered with its proposed answer by the same sign-off (`state: answered`, `status: approved`, the sign-off as `answer_source`), its rules are added to their pages, and the requirement's FRs change from `pending` to `agreed`. Outside `knowledge/`, the pipeline changes only the requirement's sign-off properties, FR statuses and `delivered_on` (from `/sync`) |
| Nothing useful | `ignore`, with the reason |

**Statuses** an accepted item will get, so the proposal can say so (conventions section 7):
pages, terms and questions `confirmed`; a decision the source shows the owner making ("decided",
"agreed", "we'll go with", from someone who can decide) `approved`, with `approved_by` and
`approved_on`; a decision recorded second-hand `confirmed`. `draft` only when the BA says "keep as
draft".

**Questions** get `due` = the date asked plus 14 days, marked "(proposed)", unless the source gives
a date.

**Delivery impact.** For every item that edits, supersedes or contradicts an existing page, rule or
decision, find the work that relies on it: the rows of `trace/map.csv` whose `knowledge_pages` list
the page, and the requirement documents that cite the page or its `BR-` IDs. Record the requirement,
stories and Jira keys in the item's `Affects delivery` row. Leave the row out for `new` items.

**The top of the file:** the summary table with the item counts by verdict and the number proposed
as `ignore`, then a short summary. When the input is a conversation or pasted text, copy the passages
the items quote into a "Source excerpt" section, so the critic can check the quotes. For meetings and transcripts, also the attendees by role, the
decisions (each marked "can decide" or "needs owner") and the actions with owner and date, and a
play-back message the BA can send to the participants. For `/requirements`, the message goes to
the owner of the pending proposals instead, asking them to confirm or change each. In the play-back, write what an authorised
person decided as "Decided (by <role>)", not "Agreed"; put disputed points neutrally under "Still
open"; leave out risks, internal notes and the critic's findings.

If there are more than 40 items, split them into several staging files of related items, so the BA
can decide them in sittings.

## 4. Critique

Run the critic on the staging file, as [`_critic.md`](_critic.md) describes: the read-only `critic`
sub-agent (`.claude/agents/critic.md`) when your tool has sub-agents, otherwise a separate second
pass. It re-reads the source and returns findings. Correct the staging file for the `fix` findings,
note the `check` findings on their items, and fill the staging file's `Critic` section; findings that
belong to no item (the summary, the play-back, a missed point you didn't add) go under "Other
findings" there. One critique per staging file; your own corrections aren't critiqued again.

When resuming a staging file that already has its `Critic` section filled, skip this step.

## 5. Confirm

Show the BA, in this order:
1. the counts, and what was redacted;
2. the critic's findings: what it fixed, and what it left for them to check;
3. items that depend on others, so they decide those together;
4. the request for decisions: tick a box per item in the file, or answer in the chat
   ("accept 1-6, reject 7: wrong meeting, edit 8: it's 10 days not 14").

Accepting an item accepts its proposal as written. For each item with an open critic `check`, ask
whether to take the critic's suggestion or keep the proposal. Write every decision into the staging
file (tick the box, add the edit text) before applying, so the file always shows what was decided.

Apply when the BA says to: normally once every item is decided, or earlier if they say "apply the
decided ones". Undecided items stay in the staging file. To decide later or on another machine,
commit the staging file (`kb: stage <file name>`) and ask whether to push it. To resume, run
`/intake knowledge/_staging/<file>`; it starts again at step 0.3.

## 6. Apply

Only a maintainer applies proposals (`PROJECT-PROFILE.md` section 1 lists the roles). If you can't
tell that the person is one, ask. A teammate's run stops after step 5: the staging file is their
contribution, committed and sent to the BA or opened as a pull request.

1. `git pull --ff-only` again.
2. Give real IDs, in item order: `python tools/kb.py next <PREFIX>` when Python is available,
   otherwise the highest existing number plus one, checking both files and registers. Replace every
   provisional ID (`CAP-new-1`) everywhere in the accepted text. If an accepted item refers to a
   rejected one, stop and ask the BA how to resolve it.
3. Write the accepted items:
   - New pages and decisions are written exactly as accepted, from the full text in the proposal.
   - Edits are applied exactly as accepted (with the BA's changes), and `updated` is set to today.
   - Every changed page gets the new source ID in its `sources` list.
4. Write the source record `sources/SRC-<n>-<date>-<slug>.md` from its template: a redacted summary,
   what it changed, the play-back message if there was one, and the rejected, ignored and declined
   items with their reasons, so they aren't proposed again.
5. Rebuild `index.md` and the three registers: `python tools/kb.py rebuild` when Python is
   available, otherwise by hand, exactly as conventions section 12 describes.
6. Append one line to `log.md` (conventions section 10).
7. Delete the staging file, or keep it with only its undecided items left. If the file was committed,
   remove it with `git rm`.
8. Check before committing: `python tools/kb.py check` when Python is available. Otherwise check by
   hand that every link you wrote resolves, every new file name follows the naming rule, and every
   page has `type`, `id`, `title` and `status`.
9. Commit: `kb: <command> <SRC-id> <short description>`. Then ask whether to push. If the push is
   rejected because someone else pushed first, recover as conventions section 11 describes.
10. If any accepted item had delivery impact, end the report with it: the requirements, stories and
    Jira keys affected, and the next step. Usually that is `/requirements <slug>` to update the
    document, then `/review`, then `/backlog`, which updates the existing stories. Never change Jira
    from here.

## Never

- Write to a knowledge page before the BA has accepted the item, or write text the BA didn't see.
- Overwrite or remove `confirmed` or `approved` content. Supersede it, or raise a question.
- Store a fact without a source, or a decision without checking authority.
- Accept a vague or incomplete item without a question or an Open items note for what is missing.
- Store personal data that a role would replace.
- Commit any file from `inbox/`.
