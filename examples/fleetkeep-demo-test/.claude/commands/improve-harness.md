---
description: Change how the harness works - work out what's wrong, decide where the fix belongs (profile, knowledge or harness), draft it as a proposal, and apply it locally only when safe and approved
argument-hint: "[what isn't working | list]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(git status), Bash(git status *), Bash(git log), Bash(git log *), Bash(git diff), Bash(git diff *), Bash(git fetch), Bash(git fetch *), Bash(git pull --ff-only), Bash(git pull --ff-only *), Bash(git add *), Bash(git commit *), Bash(git remote -v), Bash(git rev-parse *), Bash(mkdir *), PowerShell(git status), PowerShell(git status *), PowerShell(git log), PowerShell(git log *), PowerShell(git diff), PowerShell(git diff *), PowerShell(git fetch), PowerShell(git fetch *), PowerShell(git pull --ff-only), PowerShell(git pull --ff-only *), PowerShell(git add *), PowerShell(git commit *), PowerShell(git remote -v), PowerShell(git rev-parse *)
---

Read [`agents/improve-harness.md`](../../agents/improve-harness.md) and follow it exactly.

Arguments: $ARGUMENTS

That file is the canonical, vendor-neutral definition of this command. This file only wires it into
Claude Code, and deliberately carries no instructions of its own, so the two can never drift apart.
