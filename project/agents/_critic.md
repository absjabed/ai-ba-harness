# The critic: a second look before the BA decides

Step 4 of the knowledge pipeline. The pass that extracted and judged the items is too close to its
own work to see what it missed. The critic reads the source again and checks the staging file
against it and against the knowledge base, so the BA decides on items that have already been
questioned once.

The critic reads; it never writes a file. It returns a list of findings, and the command that
called it updates the staging file.

## How to run it

- **With sub-agents:** in Claude Code, start the `critic` sub-agent (`.claude/agents/critic.md`),
  which can only read. Other tools: start a fresh-context sub-agent and tell it to read only. Give it
  the staging file's path and the source: an `inbox/` path, the pasted text or conversation excerpt
  itself, or the Jira keys and Confluence page IDs.
- **Without sub-agents:** do it yourself as a separate pass. Re-read the source from the beginning
  and search the knowledge base again; don't rely on what you remember from extracting.

Either way, run it once per staging file. Don't loop: one critique, then the BA.

## What the critic reads

1. `knowledge/_meta/conventions.md` and `PROJECT-PROFILE.md` section 7 (vague words).
2. The source, in full.
3. The staging file.
4. `knowledge/index.md`, `knowledge/glossary.md`, `knowledge/stakeholders.md`, and any page the
   staging file names or that a search turns up.

## Checks

| # | Check | How |
|---|---|---|
| 1 | Nothing important left out | Go through the source again for each kind in the pipeline's step 1. Anything that is a requirement, rule, decision, action, question, answer, term or risk, and isn't in the staging file or deliberately ignored, is a finding, with its quote and location |
| 2 | Quotes are faithful | Each quote appears at its stated location, and the item doesn't claim more than the quote says |
| 3 | `new` really is new | Search the knowledge base for each `new` item with two wordings the staging file didn't use, plus glossary aliases. A page on the same subject means the verdict should be `confirms`, `extends` or `contradicts` |
| 4 | Contradictions handled by the rules | No proposed change edits `confirmed` or `approved` text. A contradiction must become a question or a decision awaiting its approver (conventions, rule 4) |
| 5 | Authority checked | Every decision and answer names the speaker's role and checks it against `stakeholders.md`. A decision recorded as `approved` came from someone who can decide it |
| 6 | Clarity | Vague words from profile section 7 without a measure are flagged as `vague` |
| 7 | Nothing sensitive left | Names where a role would do, contact details, health or customer data and credentials don't appear in the proposed changes, the summary or the play-back message |
| 8 | Proposed changes are well formed | Target folders and file names follow the conventions; cited IDs exist; edits quote the current text exactly; each new rule is listed in its page's `rules` |
| 9 | Delivery impact is complete | Every item that edits, supersedes or contradicts an existing page has its `Affects delivery` row, matching `trace/map.csv` and the requirement documents that cite it |
| 10 | Business language | Proposed page text has no code paths, class or table names, or harness jargon (conventions rule 7) |

## Findings

Return a list. Each finding has:

- **Item:** the staging item number, `missed` for check 1, or `other` for the summary, the
  play-back or anything that isn't an item.
- **Severity:**
  - `fix`: the staging file is wrong (a misquote, a wrong verdict with the page to prove it, a
    missed item that clearly belongs in the knowledge base, data to redact, a broken change);
  - `check`: the BA should look at it (a possible duplicate, an authority you couldn't confirm).
- **Finding:** one sentence, with the quote or the page ID that shows it.
- **Suggested change:** what to change in the staging file.

If there is nothing to report, say so.

## What the calling command does with the findings

1. **`fix` findings:** correct the staging file. A missed item becomes a new item marked `(added by
   the critic)`. A corrected verdict or quote keeps a short note of what changed.
2. **`check` findings:** don't change the item; put the finding in its `Critic` row. Findings marked
   `other`, and `missed` points you didn't add as items, go under "Other findings" in the `Critic`
   section, and the play-back's own `Critic` line.
3. Fill the staging file's `Critic` section: how it ran (sub-agent or second pass), the number of
   findings, what was changed, and what is left for the BA.
4. If you disagree with a finding, leave the item as it was and record the finding and your reason
   in the `Critic` row, so the BA can decide.

## Never

- Write or edit any file (as the critic).
- Accept, reject or apply items. That is the BA's decision, in step 5.
- Run more than once on the same staging file, unless the BA asks.
