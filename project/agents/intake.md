# `/intake`: turn new material into proposed knowledge

You read new material the BA has (meeting notes, a transcript, a document, an email, a stakeholder's
answer, or the current conversation), work out what it adds to or changes in the knowledge base, and
propose those changes for the BA to accept. Nothing reaches the knowledge base without the BA's yes.

## Before anything

Read `PROJECT-PROFILE.md`, `knowledge/_meta/conventions.md` and `agents/_knowledge-pipeline.md`.
You follow that pipeline exactly; this file only adds what is specific to `/intake`.

## Input

The argument is one of:

| Argument | Input |
|---|---|
| A file in `inbox/` | That file |
| A folder in `inbox/` | Every file in it, one staging file per file |
| Pasted text after the command | The text; ask the BA what it is (meeting, email, document) and its date |
| A staging file in `knowledge/_staging/` | Resume it: show the items still undecided, then continue from the pipeline's confirm step |
| Nothing | The current conversation: what was learned, decided or found unclear while working with the BA in this session. The source kind is `conversation` |

If the argument is a path outside `inbox/`, ask the BA to move or copy the file into `inbox/` first,
so the original never ends up committed.

## Reading the file

| File type | How |
|---|---|
| `.md`, `.txt`, `.vtt`, `.srt`, `.csv`, `.eml` | Read directly |
| `.pdf`, images | Read directly |
| `.docx`, `.xlsx`, `.pptx` | If `converter: markitdown` in the profile, run `markitdown "<file>" -o "inbox/.converted/<name>.md"` and read the result. Otherwise ask the BA to save it as PDF in `inbox/` |
| Anything else | Say you can't read it and suggest a format |

For transcripts, use timestamps as locations. For documents, use page and section.

## Steps

1. Run the pipeline from step 0 to step 3 (prepare, extract, judge, stage).
2. **For meetings and transcripts,** also put three things in the staging summary:
   - the attendees by role;
   - the decisions made, each marked "can decide" or "needs owner";
   - the actions with owner and date.
   Then draft the play-back message.
3. Show the staging file and wait for the BA's decisions (pipeline step 4).
4. Apply (pipeline step 5).
5. **Clean up the inbox, only with permission.** List the raw files and any converted copies in
   `inbox/.converted/` that this run used, and ask: "Delete these N files from inbox/? The redacted
   source record is kept. (yes / no / choose)". Default no. Delete only the files the BA agrees to.
   Never delete anything outside `inbox/`.

## Report

- **The source record:** its ID and title.
- **Counts:** accepted, edited and rejected items.
- **Questions:** opened (with who to ask) and closed.
- **Decisions:** recorded, and any waiting for an approver.
- **Actions:** with owner and date.
- **The play-back message,** if any, ready to send.
- **Next:** usually nothing, or `/requirements` if the material defines new scope.

## Never

- Change a knowledge page before the BA accepts the item.
- Commit or move anything out of `inbox/`.
- Delete inbox files without an explicit yes, or any file outside `inbox/`.
- Treat a statement as a decision when the speaker can't decide it.
