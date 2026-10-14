---
description: Build the first knowledge base from existing documents, Confluence pages and Jira epics (proposals for the BA to accept)
argument-hint: "[confluence | jira | inbox | <path or page>]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(git status *), Bash(git log *), Bash(git diff *), Bash(git fetch *), Bash(git pull --ff-only *), Bash(git add *), Bash(git commit *), Bash(git remote -v), Bash(git rev-parse *), Bash(markitdown *), Bash(mkdir *), mcp__atlassian__getAccessibleAtlassianResources, mcp__atlassian__searchJiraIssuesUsingJql, mcp__atlassian__getJiraIssue, mcp__atlassian__searchConfluence, mcp__atlassian__getConfluenceContent, mcp__atlassian__discover, mcp__atlassian__executeRead
---

Read [`agents/kb-seed.md`](../../agents/kb-seed.md) and follow it exactly.

Arguments: $ARGUMENTS

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Claude Code, and deliberately carries no instructions of its own, so the two can never drift apart.
