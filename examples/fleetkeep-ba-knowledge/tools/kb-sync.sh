#!/usr/bin/env bash
# Bring this clone's knowledge base up to date. Claude Code and Codex run it when a session starts
# (a SessionStart hook); OpenCode runs it at the start of each harness command. You can also run it
# by hand: bash tools/kb-sync.sh
#
# It only ever fast-forwards. If you have local changes, or your branch has diverged from the shared
# one, it changes nothing and says what to do. It never fails a session: every problem is reported
# and the script exits 0.
#
# Turn it off in PROJECT-PROFILE.md section 5: kb_auto_sync: off

cd "$(dirname "${BASH_SOURCE[0]}")/.." 2>/dev/null || exit 0

# Respect the profile switch.
if grep -qiE '^[[:space:]]*kb_auto_sync:[[:space:]]*off' PROJECT-PROFILE.md 2>/dev/null; then
  exit 0
fi

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

upstream="$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null)"
if [ -z "$upstream" ]; then
  exit 0   # No shared remote branch yet (a brand-new repository). Nothing to sync.
fi

# Fetch, but never let a slow or offline network hold up the session.
if command -v timeout >/dev/null 2>&1; then
  timeout 15 git fetch --quiet 2>/dev/null || { echo "Knowledge base: couldn't reach the remote; working with your local copy."; exit 0; }
else
  git fetch --quiet 2>/dev/null || { echo "Knowledge base: couldn't reach the remote; working with your local copy."; exit 0; }
fi

behind="$(git rev-list --count HEAD.."$upstream" 2>/dev/null || echo 0)"
ahead="$(git rev-list --count "$upstream"..HEAD 2>/dev/null || echo 0)"

if [ "$behind" = "0" ]; then
  if [ "$ahead" != "0" ]; then
    echo "Knowledge base: up to date. You have $ahead local commit(s) not yet pushed."
  fi
  exit 0
fi

if [ -n "$(git status --porcelain --untracked-files=no 2>/dev/null)" ]; then
  echo "Knowledge base: $behind new change(s) on the shared copy, but you have uncommitted edits, so nothing was pulled. Commit or stash them, then run: git pull --ff-only"
  exit 0
fi

if [ "$ahead" != "0" ]; then
  echo "Knowledge base: your copy and the shared copy have both changed ($ahead local, $behind shared). Nothing was pulled. Run: git pull --rebase, then push."
  exit 0
fi

if git merge --ff-only --quiet "$upstream" >/dev/null 2>&1; then
  echo "Knowledge base updated: $behind new change(s) pulled from the shared copy."
else
  echo "Knowledge base: $behind new change(s) available, but the update didn't apply cleanly. Run: git pull --ff-only"
fi
exit 0
