---
type: guide
id: GUIDE-readme
title: How to read and contribute to this knowledge base
status: approved
---

# How to read and contribute to this knowledge base

This folder is the project's knowledge: how the product works and must work, its business rules,
the decisions made and who made them, and the questions still open.

## Reading

- Start at [index.md](index.md). Every page is listed there with one line.
- Each page shows a **status**:
  - `draft`: extracted by AI, not yet checked;
  - `confirmed`: checked by a BA against its source;
  - `approved`: agreed by a named stakeholder;
  - `superseded`: replaced, kept for history.
- IDs in brackets, such as `(SRC-031)` or `(BR-104)`, point to where a statement came from or to the
  rule it refers to.
- `[!CAUTION]` boxes mark behaviour that is still unresolved, with a link to the open question.
- To ask a question instead of reading, run `/ask <question>` in Claude Code from the repository root.

## Opening it in Obsidian (optional)

Open this `knowledge/` folder as a vault. The shared settings in `.obsidian/app.json` keep links in
standard markdown, so everything works the same in Obsidian, on GitHub and in Claude Code. Graph
view, backlinks and the Properties panel all work.

## Contributing

Don't change what a page says directly. Either give the new material to a BA (the usual route), or,
if you're comfortable with git, run `/intake` on it, commit the staging file it writes to `_staging/`
on a branch, and open a pull request: a BA decides each item. Fixing a typo or awkward wording by
hand is fine, as long as the meaning stays the same; add a `log.md` line with the command `EDIT`. The rules are in
[_meta/conventions.md](_meta/conventions.md).
