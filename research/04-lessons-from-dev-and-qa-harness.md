# Lessons from the AI Dev Harness and AI QA Harness

Both existing harnesses were read, not changed. This note records what a BA harness should copy from
them, where it must not overlap, and the hand-offs between the three.

## How the two harnesses are built

| | AI Dev Harness (`ai-harness`) | AI QA Harness (`ai-qa-harness`) |
|---|---|---|
| Who uses it | Developers | QA engineers, on a QA environment |
| Shape | `.ai/` knowledge layer (personas, playbooks, standards, templates, config) + `.claude/` execution layer (27 commands, 8 sub-agents, 9 hooks) | Canonical vendor-neutral agents in `agents/*.md`; thin `.claude/commands/` wrappers that only point at them |
| Per-project setup | `/init-project` interview fills `{{TOKENS}}` and `[FILL IN]` blocks across many files | One file, `PROJECT-PROFILE.md`, plus `.env` |
| Distribution | Copy folders; `.claude/HARNESS_VERSION` + git tag `v1.0.0` | `npm run export` copies the right files and records template version + commit |
| Tracker integration | Atlassian remote MCP in `.mcp.json`; read-only intake, every outward write behind a STOP gate | No live tracker writes: defects go to a CSV in Jira import format |
| Safety model | Hooks hard-block dangerous commands; STOP gates; reviewer sub-agents without edit tools | Invariants I1 to I8 the agents must not break; read-only DB account; agents refuse to guess |
| Docs | `README.md`, `docs/` markdown + one HTML guide, worked example (FleetKeep) | `README.md`, `SETUP.md`, `docs/` + one HTML handbook |

## What the BA harness should copy

1. **One profile file per project** (QA harness pattern). BAs are not going to edit twenty template
   files. A single `PROJECT-PROFILE.md` (project, stakeholders, tracker keys, Confluence space,
   glossary location, ticket conventions) keeps setup to minutes.
2. **Vendor-neutral agent definitions with thin wrappers** (QA harness pattern). The knowledge sits
   in plain markdown; Claude Code wrappers only point at it. That keeps the door open for Copilot or
   another assistant later.
3. **Read freely, write only after a STOP** (Dev harness integration rules). Fetching an issue or a
   page needs no approval. Creating, editing, transitioning or commenting in Jira or Confluence is an
   outward write: show exactly what will be sent where, act only on an explicit yes.
4. **No secrets in committed config** (both). OAuth-based MCP servers only; anything with a token
   lives in a gitignored file.
5. **Traceability by key** (QA invariant I8, Dev fix-version rule). Every requirement and story
   carries an ID and a source; every ticket the harness creates links back to the artifact it came
   from.
6. **Refuse to guess** (both). If a fact is not in the notes, transcript or tracker, ask, or record
   it as an open question. Never invent a requirement, a stakeholder, a version or a priority.
7. **Versioned template + recorded origin** (both). A marker that records which template release a
   project copy came from.
8. **One HTML handbook** for people who will never open a markdown file (both).

## Where it must not overlap

The Dev harness already has BA features. They stay where they are; the BA harness works upstream of
them and hands off in their format.

| Already in the Dev harness | What it does | Consequence for the BA harness |
|---|---|---|
| `/ba` (BA Studio) | Interviews a BA for **one feature or epic** and writes `requirement-spec.md`, `user-stories.md`, `epic-breakdown.md` under `.ai/features/<slug>/`, including the fix version | Don't rebuild per-feature specs for developers. Produce the project-level material that feeds `/ba`, or emit files in exactly that shape when a feature is handed to dev |
| `/qa` (QA Studio) | Writes `test-specs.md` from those specs | Out of scope. UAT planning from the business side is in scope; test design is not |
| `/agents:pm` | Status reports, planning | Overlaps with BA status reporting. Keep BA reporting about requirements health (open questions, unapproved items, change requests), not delivery progress |

The QA harness owns automated testing on QA environments and defect raising. The BA harness should
not write tests or raise defects; it can consume defect summaries when assessing UAT readiness.

## Hand-offs between the three harnesses

```text
BA harness (project level)                Dev harness (feature level)          QA harness
───────────────────────────               ───────────────────────────          ──────────
stakeholders, scope, glossary,
process maps, business rules
            │
backlog: epics + stories in Jira ──────►  /ba <slug> reads the Jira issue
            │                             /qa writes test specs  ─────────────► story keys drive test plans
change requests + impact analysis ─────►  updated specs, fix version
UAT plan + sign-off   ◄──────────────────────────────────────────────────────── defect log / CSV
release notes for the business ◄────────  deploy notes (fix version)
```

The cleanest contract is the tracker itself: the BA harness writes well-formed Jira epics and
stories (with acceptance criteria and a fix version); the Dev harness's `/ba` already reads an issue
key as its starting requirement, and the QA harness already requires an issue key on every story.

## Differences in the user

BAs are less likely than developers to have git, bash or a terminal habit. That argues for:

- as little setup as possible (one profile, OAuth sign-in to Atlassian, nothing else required);
- no hooks that depend on bash for core safety (use STOP gates in the agent instructions, and keep
  hooks as an optional extra);
- outputs that live where BAs already work (Jira, Confluence) with the markdown copy as the record,
  not the other way round;
- a handbook page and a cheat sheet rather than a README full of commands.
