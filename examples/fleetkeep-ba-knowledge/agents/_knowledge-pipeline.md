# The knowledge pipeline: extract, judge, stage, critique, confirm, apply

Shared by `/kb-seed`, `/intake`, `/sync` and `/requirements`. It is how anything gets into
`knowledge/`. The rules it enforces are in `knowledge/_meta/conventions.md`; read that first.

## 0. Prepare

1. `git pull --ff-only`. If it fails (local changes or diverged history), stop and tell the BA what
   to do; don't stage against an out-of-date copy.
2. Read `knowledge/index.md`, `knowledge/glossary.md`, `knowledge/stakeholders.md` and the three
   registers. Keep the list of existing IDs at hand.

## 1. Extract

Go through the input once and pull out candidate items. Each item needs a quote (the exact words, or
the closest short passage) and its location: file and paragraph or page, transcript timestamp, Jira
key and comment number, Confluence page and section.

| Kind | What it looks like |
|---|---|
| requirement | Something the product must do or be |
| rule | A condition, threshold, ordering, permission or calculation the product applies |
| decision | A choice made by someone, with or without authority |
| action | Someone will do something, ideally by a date |
| question | Something nobody could answer, or that people disagreed on |
| answer | A reply to an existing open question |
| term | A word with a project-specific meaning, or a synonym for an existing term |
| risk | Something that might go wrong (also assumptions, issues, dependencies) |
| fact | How something works today, who someone is, what a system does |

Leave out chit-chat, scheduling logistics and anything already captured identically.

## 2. Judge

For every item, record four verdicts.

**Against the knowledge base.** Search the index, the glossary (including aliases) and the pages
for the subject, with at least two different wordings.

| Verdict | When |
|---|---|
| `new` | Nothing on this subject exists |
| `confirms <ID>` | It says the same as an existing item (this strengthens its sources) |
| `extends <ID>` | It adds detail without conflicting |
| `contradicts <ID>` | It conflicts with an existing item. If that item is `confirmed` or `approved`, the change can only be a new question or a decision awaiting an approver (conventions, rule 4) |
| `duplicate of <ID>` | It repeats something already captured from this same source, or a pending staging file |
| `answers <Q-ID>` | It answers an open question |

**Clarity.**
- `clear`;
- `vague: "<word>"`, using the words in `PROJECT-PROFILE.md` section 7;
- `incomplete: <what's missing>`, such as the error case, who, or a number.

**Authority** (decisions and answers only). Look the speaker's role up in `stakeholders.md`.
- `can decide (<role>)`;
- `cannot (<role>; owner is <role>)`;
- `unknown`, when the speaker or the owner isn't in the register.

**Sensitivity.**
- `clean`;
- `redact: <what>`, for personal names where a role would do, contact details, health or customer
  data, credentials, or anything marked confidential.

## 3. Stage

Write one file, `knowledge/_staging/<yyyy-mm-dd>-<command>-<slug>.md`, from
`knowledge/_meta/templates/staging.md`. For every item, state the exact proposed change:

| Situation | Proposed change |
|---|---|
| New capability, process or entity | Create `CAP-new-n`, `PROC-new-n` or `ENT-new-n` in the right folder from its template, status `draft` |
| New detail on an existing page | Edit `<ID>` with a diff of the exact lines |
| A rule | Add it to the page that applies it, as `BR-new-n`, and list it in that page's `rules` |
| A decision by someone who can decide | Create `DEC-new-n` (`approved` if they decided it in the source, otherwise `confirmed` once the BA accepts) and update the pages it affects |
| A decision by someone who can't | Create `Q-new-n` addressed to the owner, recording the view |
| A contradiction of a confirmed or approved item | Create `Q-new-n` linking both, and add a `[!CAUTION]` callout on the affected page. Never edit the confirmed text |
| An answer to `Q-xxx` | Fill the question's Answer section; set `state: answered`, `answered_on` and `answer_source`, and `status: approved` if the person could decide it; update the pages it unblocks and remove their caution callouts |
| A term | Add a `T-new-n` glossary entry, or add the word to an existing term's "Also called" and to the page's `aliases` |
| A risk, assumption, issue or dependency | A new row in `raid.md` |
| An action | Listed in the staging summary and the source record; offer to turn it into a Jira task later via `/backlog` |
| Nothing useful | `ignore`, with the reason |

Add the summary table at the top (item counts by verdict) and, for meetings, a short play-back
message the BA can send to participants.

If there are more than 40 items, split them into several staging files of related items, so the BA
can decide them in sittings.

## 4. Critique

Run the critic on the staging file, as [`_critic.md`](_critic.md) describes: a fresh-context
sub-agent when your tool has one, otherwise a separate second pass. It re-reads the source, looks
for missed items, misquotes, wrong verdicts, unchecked authority and unredacted data, and returns
findings. Correct the staging file for the `fix` findings, note the `check` findings on their items,
and fill the staging file's `Critic` section. One critique per staging file; then go to the BA.

When resuming a staging file that already has its `Critic` section filled, skip this step.

## 5. Confirm

Show the BA the staging file, pointing out the critic's findings first. They decide each item by ticking a box in the file, or in the chat
("accept 1-6, reject 7: wrong meeting, edit 8: it's 10 days not 14"). Wait for their decisions.
Apply when the BA says to: normally once every item is decided, or earlier if they say "apply the
decided ones". Undecided items stay in the staging file for later. To resume in another session, run
`/intake knowledge/_staging/<file>`; it picks up at this step.

## 6. Apply

Only a BA who maintains this repository applies proposals (`PROJECT-PROFILE.md` section 1 lists the
roles). If you can't tell that the person is one, ask. A teammate's run stops after step 4: the
staging file is their contribution, sent to the BA or opened as a pull request.

1. `git pull --ff-only` again.
2. Give real IDs: the next number for each prefix, after checking both files and registers.
3. Write the accepted items:
   - New pages come from their template, with `status: confirmed`. Use `draft` only if the BA said
     "keep as draft".
   - Edits are applied exactly as accepted (with the BA's changes), and `updated` is set to today.
   - Every changed page gets the new source ID in its `sources` list.
4. Write the source record `sources/SRC-<n>-<date>-<slug>.md` from its template: a redacted summary,
   what it changed, and the rejected items with their reasons, so they aren't proposed again.
5. Regenerate `index.md`, `business-rules.md`, `decisions.md` and `open-questions.md` from the
   pages' properties (conventions, section 12).
6. Append one line to `log.md`.
7. Delete the staging file, or keep it with only its undecided items left.
8. Check before committing:
   - every link you wrote resolves;
   - every new file name follows the naming rule;
   - every page has `type`, `id`, `title` and `status`.
9. Commit: `kb: <command> <SRC-id> <short description>`. Then ask whether to push.

## Never

- Write to a knowledge page before the BA has accepted the item.
- Overwrite or remove `confirmed` or `approved` content. Supersede it, or raise a question.
- Store a fact without a source, or a decision without checking authority.
- Store personal data that a role would replace.
- Commit anything from `inbox/`.
