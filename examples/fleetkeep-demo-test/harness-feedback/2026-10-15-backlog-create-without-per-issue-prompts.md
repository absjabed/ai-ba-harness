---
type: harness-feedback
title: Let /backlog create approved Jira issues without a prompt per issue
status: proposed
kind: harness change
risk: safety
version_impact: minor
raised_by: Lead BA
raised_on: 2026-10-15
harness_version: 0.5.0
---

# Let /backlog create approved Jira issues without a prompt per issue

<!-- status: proposed (written, not applied) · applied-locally (also changed in this repository) ·
     accepted (taken into the harness; give the version) · declined (with the reason) -->

## The problem

The Lead BA: "/backlog should be allowed to create issues without asking me each time, the prompts
are annoying". After the BA approves a batch in `/backlog`'s preview, Claude Code still asks before
every single issue it creates, so the BA approves the same work twice: once for the batch and once
per issue. The BA would like the batch's yes to be enough for creating issues.

## Evidence

The Lead BA: "creating five stories means five prompts". No `/backlog` run exists in this
repository yet (the Atlassian connection isn't available), so there is no log line or output to
quote; the behaviour is the one the harness describes:

- `agents/backlog.md`, requirement step 5: "Claude Code will also ask before each write tool call;
  that prompt is expected."
- `.claude/settings.json`, `permissions.ask`: `"mcp__atlassian__create*"` and
  `"mcp__plugin_atlassian_atlassian__create*"`, which match `createJiraIssue`.
- `agents/README.md`, "Safety, in layers", layer 3: the ask list makes Claude Code prompt "before
  each one even inside an approved batch", and "Ask and deny always win over a command's
  `allowed-tools`", so `/backlog`'s wrapper can't pre-approve creates while the ask rule matches them.

With five stories and an epic, that is one batch approval plus six create prompts (and one more per
approved link).

## Proposed change

**This is a safety change. It must not be applied in a project repository; it is for the harness
maintainers to decide.** It removes the second, per-issue confirmation that layer 3 adds on purpose,
and it touches `.claude/settings.json`, a wrapper's `allowed-tools`, the approval steps of the only
command that writes to Jira, and the handbook's description of the safety layers.

The smallest change that does what the BA asks: take the `create*` patterns off the ask list, and
let `/backlog`'s wrapper pre-approve `createJiraIssue` only. The batch preview and its explicit yes
(requirement step 5, single-item step 4) stay as they are; edits, links, transitions and every other
write still prompt.

```diff
--- a/.claude/settings.json
+++ b/.claude/settings.json
@@ -2,7 +2,6 @@
   "$schema": "https://json.schemastore.org/claude-code-settings.json",
   "permissions": {
     "ask": [
-      "mcp__atlassian__create*",
       "mcp__atlassian__edit*",
       "mcp__atlassian__transition*",
       "mcp__atlassian__addOrEdit*",
@@ -48,6 +47,5 @@
       "PowerShell(git restore *)",
       "PowerShell(git rebase *)",
       "PowerShell(git stash drop *)",
-      "mcp__plugin_atlassian_atlassian__create*",
       "mcp__plugin_atlassian_atlassian__edit*",
       "mcp__plugin_atlassian_atlassian__transition*",
--- a/.claude/commands/backlog.md
+++ b/.claude/commands/backlog.md
@@ -1,5 +1,5 @@
 ---
 description: Put approved work into Jira after duplicate checks and your approval - stories from a reviewed requirement (and later changes to them), or a single task, spike or UAT bug
 argument-hint: "<requirements/<slug>/requirement.md | task ACT-<n> | spike Q-<n> | bug <SRC-id> <item>>"
-allowed-tools: Read, Write, Edit, ..., mcp__atlassian__getJiraIssueTypeMetaWithFields
+allowed-tools: Read, Write, Edit, ..., mcp__atlassian__getJiraIssueTypeMetaWithFields, mcp__atlassian__createJiraIssue, mcp__plugin_atlassian_atlassian__createJiraIssue
 ---
--- a/agents/backlog.md
+++ b/agents/backlog.md
@@ -87,6 +87,7 @@
    - Create the epic first (`createJiraIssue`, or `executeWrite` on the v2 server). Then each story
      with `parent` set to the epic key, one at a time.
    - Apply approved updates with `editJiraIssue`, one at a time.
-   - Claude Code will also ask before each write tool call; that prompt is expected.
+   - The batch's yes covers each `createJiraIssue`. Claude Code still asks before each update, link
+     and `executeWrite` call; that prompt is expected.
    - After each create or update, read the issue back with `getJiraIssue`. Check that summary, type,
      parent, fix version, labels and required fields are as sent, and that every description heading
--- a/agents/README.md
+++ b/agents/README.md
@@ -29,5 +29,7 @@
-3. **`.claude/settings.json`** puts every Atlassian write tool (matched by verb, such as `create*`,
-   `edit*`, `update*`) and `git push` on the "ask" list, so Claude Code prompts before each one even
-   inside an approved batch. It denies Atlassian delete tools, `executeDestructive`, force pushes, hard
-   resets and `git clean` outright. Ask and deny always win over a command's `allowed-tools`. The
+3. **`.claude/settings.json`** puts every Atlassian write tool (matched by verb, such as `edit*`,
+   `update*`) and `git push` on the "ask" list, so Claude Code prompts before each one even inside
+   an approved batch. The exception is creating Jira issues: `/backlog` pre-approves
+   `createJiraIssue`, so the batch's yes covers each create. It denies Atlassian delete tools,
+   `executeDestructive`, force pushes, hard resets and `git clean` outright. Ask and deny always win
+   over a command's `allowed-tools`. The
    rules cover the repository's own `atlassian` server and the Atlassian plugin
```

(The wrapper's `allowed-tools` line is shortened with `...`: only the two new entries at the end
change.)

## Files touched

- `.claude/settings.json`
- `.claude/commands/backlog.md`
- `agents/backlog.md`
- `agents/README.md`

## What else it affects

Points for the maintainers to weigh; they are why this needs their decision:

- **It removes a layer that was designed in.** Layer 3 exists so a create is confirmed even inside
  an approved batch. After this change, the only check between the batch's yes and Jira is the agent
  following its own definition (one batch, at most `max_batch` items, only what was approved).
- **`create*` is a pattern, not one tool.** Taking it off the ask list stops the prompt for every
  Atlassian create tool in every command (Confluence pages and comments, issue links, and others), not
  just `createJiraIssue`. They would then prompt only because no wrapper pre-approves them, which
  doesn't hold when someone runs Claude Code in an auto-accept or bypass permission mode. A safer form
  would replace the `create*` pattern with the explicit create tools other than `createJiraIssue`; that
  needs the server's current tool list, which wasn't available here.
- **The v2 server is unchanged.** On it, creates go through `executeWrite`, which covers every write,
  so it must stay on the ask list; those projects keep one prompt per create.
- **Alternatives the maintainers might prefer:** keep the prompts and say in `/backlog`'s preview how
  many there will be ("6 creates: Claude Code will ask 6 times"); or keep them and leave it as it is,
  with `max_batch` capping a batch at 15.
- `CLAUDE.md` ("Writes to Jira happen only through `/backlog`, after a preview and an explicit yes")
  stays true. The handbook's description of the safety layers would need the same change as
  `agents/README.md`; the handbook isn't in project repositories, so it wasn't checked.
- Version: minor if the maintainers accept it (projects can take it as is), but every project's
  safety layer changes, so it deserves a note in the changelog.

## Outcome

Not applied in this repository: it is a safety change, which `/improve-harness` never applies
locally. The Lead BA asked for it to be applied here on 2026-10-15; it was declined for that reason.
