---
type: guide
id: GUIDE-readme
title: How to read and contribute to this knowledge base
status: approved
---

# How to read and contribute to this knowledge base

This folder holds the project's knowledge: how the product works and must work, its business rules,
the decisions made and who made them, and the questions still open.

## Reading

- Start at [index.md](index.md), which lists every page with one line.
- Each page shows a status:
  - `draft`: extracted by AI, not yet checked;
  - `confirmed`: checked by a BA against its source;
  - `approved`: agreed by a named stakeholder;
  - `superseded`: replaced, kept for history.
- IDs in brackets, such as `(SRC-031)` or `(BR-104)`, point to where a statement came from or to the
  rule it refers to.
- `[!CAUTION]` boxes mark behaviour that is still unresolved, with a link to the open question.
- To ask a question instead of reading, run `/ask <question>` (`$ask` in Codex) from the repository
  root, or just ask your assistant.

## Opening it in Obsidian (optional)

Open this `knowledge/` folder as a vault. The shared settings in `.obsidian/app.json` keep links in
standard markdown, so everything works the same in Obsidian, on GitHub and in any AI assistant. Graph view,
backlinks and the Properties panel all work.

## Contributing

Don't change what a page says directly. Usually you give the new material to a BA. If you're
comfortable with git, you can instead run `/intake` on it, commit the staging file it writes to
`_staging/` on a branch, and open a pull request; a BA then decides each item. You may fix a typo or
awkward wording by hand if the meaning stays the same; when you do, add a `log.md` line with the
command `EDIT`. The rules are in [_meta/conventions.md](_meta/conventions.md).
