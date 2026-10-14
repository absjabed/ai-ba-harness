---
description: Answer a question from the project knowledge base, with citations (read-only; anyone can use it)
argument-hint: "<your question>"
allowed-tools: Read, Glob, Grep, mcp__atlassian__getAccessibleAtlassianResources, mcp__atlassian__searchJiraIssuesUsingJql, mcp__atlassian__getJiraIssue, mcp__atlassian__searchConfluence, mcp__atlassian__getConfluenceContent, mcp__atlassian__search
disallowed-tools: Write, Edit, MultiEdit, NotebookEdit, Bash, PowerShell, Agent, Task, mcp__atlassian__create*, mcp__atlassian__edit*, mcp__atlassian__transition*, mcp__atlassian__addOrEdit*, mcp__atlassian__add*, mcp__atlassian__update*, mcp__atlassian__manage*, mcp__atlassian__watch*, mcp__atlassian__unwatch*, mcp__atlassian__upload*, mcp__atlassian__convert*, mcp__atlassian__move*, mcp__atlassian__archive*, mcp__atlassian__unarchive*, mcp__atlassian__restore*, mcp__atlassian__set*, mcp__atlassian__copy*, mcp__atlassian__replace*, mcp__atlassian__remove*, mcp__atlassian__enable*, mcp__atlassian__disable*, mcp__atlassian__complete*, mcp__atlassian__reopen*, mcp__atlassian__star*, mcp__atlassian__unstar*, mcp__atlassian__publish*, mcp__atlassian__share*, mcp__atlassian__recover*, mcp__atlassian__approve*, mcp__atlassian__requestChanges*, mcp__atlassian__merge*, mcp__atlassian__run*, mcp__atlassian__resolveBitbucket*, mcp__atlassian__delete*, mcp__atlassian__executeWrite, mcp__atlassian__executeDestructive
---

Read [`agents/ask.md`](../../agents/ask.md) and follow it exactly.

Arguments: $ARGUMENTS

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Claude Code, and deliberately carries no instructions of its own, so the two can never drift apart.
