# `/improve-harness`: change how the harness works

Someone thinks a command, template or rule should work differently: `/sync` proposes too much noise,
a staging file is hard to read, a Jira template misses a field the team needs. You find out exactly
what is wrong, decide where the fix belongs, draft it, and record it so the harness can learn from
it. You never change the knowledge base here, and you never weaken a safety rule locally.

## Before anything

Read `PROJECT-PROFILE.md` (section 1 for who maintains the repository and where the harness comes
from, section 8 for changes already made locally), `HARNESS_VERSION` and `agents/README.md`. Then
read the files the problem is about. `git pull --ff-only` first.

## Input

| Argument | What it does |
|---|---|
| A description, for example `/improve-harness /sync keeps proposing estimate changes` | Works through that problem |
| Nothing | Asks what isn't working |
| `list` | Shows the proposals in `harness-feedback/` and their status |

## Steps

1. **Understand it.** Ask, one question at a time and at most three in all, skipping what the
   argument already says:
   - which command or file, and what happened;
   - what should have happened instead;
   - an example: a staging file, a commit, a log line, or the words of the output. Read it. The BA's
     own account is evidence too when nothing was written down. Quote raw notes from `inbox/` only
     with names and contact details replaced by roles.
   If the example doesn't show the problem (the harness already does what the BA asks), say so and
   ask whether to carry on, change the request, or drop it. Stop when you could explain the problem
   to someone who wasn't there.
2. **Decide where it belongs**, and say which and why:

   | Kind | Example | Where the fix goes |
   |---|---|---|
   | A project setting | Add "asap" to the vague words; widen the scope JQL; read 100 issues per sync | `PROJECT-PROFILE.md`. No harness change |
   | Knowledge, not the harness | "The glossary is wrong about VOR" | Not here: run `/intake` |
   | A harness change | A command's steps, a template, the conventions, a wrapper | A proposal, and optionally a local change (steps 3 to 6) |

   A word people use with different meanings is usually a glossary or house-term matter: knowledge,
   through `/intake`, as well as or instead of a vague word.

   For a project setting, show the profile diff, write it after a yes, append a log line
   (`- <date> | IMPROVE-HARNESS | profile | section <n>: <what> | accepted by <role>`), commit
   `kb: profile <what>`, ask before pushing, and stop. No proposal file is needed.
3. **Draft the change.** Read the harness files involved and write the exact change as a diff. Keep
   it as small as the problem; long unchanged lines may be shortened with `...` in the proposal, but
   the applied change must be exact (check it with `git apply --check` or by reading the result).
   Then check it against the rest of the harness: other commands that read the same file, the
   conventions, and the handbook if the repository has one (otherwise note it for the
   maintainers). List every file it touches.
4. **Judge the risk.**
   - **Safety change:** it changes *whether, when or with what approval* the harness writes
     anything: `.claude/settings.json`, a wrapper's `allowed-tools` or `disallowed-tools`, a "Never"
     rule, a preview or approval step, redaction, or when Jira or Confluence is written. These are
     never applied locally; they go to the harness maintainers only. (Changing *what text* goes into
     a Jira issue, such as a template section, is a behaviour change.)
   - **Behaviour change:** new content or steps a command must produce, read or propose.
   - **Wording or template change:** the wording or layout of what already exists.
   Suggest how the harness version would change: patch for a fix, minor for something new that
   projects can take as is, major when every project must change something. A safety change is at
   least minor.
5. **Write the proposal** to `harness-feedback/<yyyy-mm-dd>-<slug>.md` (the slug in at most five
   words) from
   `templates/harness-feedback.md`: the problem in the BA's words, the evidence, the kind and risk,
   the diff, the files touched, and `status: proposed`. Anyone may write one, including teammates
   who can't apply knowledge changes.
6. **Offer to apply it here too**, only when all of these hold: the person maintains this repository
   (profile section 1), it isn't a safety change, and the BA says yes. Then:
   - apply the diff exactly;
   - add one row per changed file to profile section 8 ("Local harness changes"), so a later
     harness update doesn't silently undo it;
   - set the proposal's `status: applied-locally` and `applied_on`.
   Otherwise the change waits for the harness maintainers. If the BA asks to apply a safety change
   anyway, say: "This changes a permission or approval step. Projects never change those
   themselves; the harness maintainers decide for every project at once. Please send them the
   proposal." Record the request in the proposal's Outcome section.
7. Append a log line (`- <date> | IMPROVE-HARNESS | <proposal file> | proposed or applied locally |
   accepted by <role>`) and commit `harness: <proposed|local> <slug>` (the slug without the date)
   with the proposal, the log line and the local change, if applied. Ask before pushing.

## Report

- The problem, as you understood it, in two sentences.
- Where it belongs, and what was done: profile changed, proposal written, applied locally or not.
- **Send it on:** the proposal file and the harness repository from profile section 1. Ask the BA to
  share it with the harness maintainers (an issue or a message with the file attached). Don't send it
  yourself.

## `/improve-harness list`

Read `harness-feedback/*.md` and show a table: date, title, risk, version impact, status. Point out
proposals that are `applied-locally` but not yet `accepted` upstream: they are what a harness update
could undo. Mention profile settings changed this way too, from the `IMPROVE-HARNESS | profile` lines
in `knowledge/log.md`.

## Never

- Change knowledge pages, staging files or registers (appending the log line is the one exception).
- Apply a safety change locally, or remove or weaken a "Never" rule, an approval step or a
  permission rule.
- Apply anything without showing the diff and getting a yes.
- Send the proposal anywhere outside the repository. The BA shares it.
