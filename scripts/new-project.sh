#!/usr/bin/env bash
# Create a project BA knowledge repository from this template.
#
#   scripts/new-project.sh <target-folder> [--name <project>] [--allow-dirty] [--inside-repo]
#
# Copies everything under project/ (dotfiles included) into <target-folder>, adds HARNESS_VERSION,
# and records in PROJECT-PROFILE.md which harness version and commit the copy came from.
# The target must be a new or empty folder outside any other git repository. With --inside-repo
# (only when the user explicitly asks for it) it may be a new subfolder of one. The script only adds
# files: it never changes, moves or deletes anything that was already there. Research notes, design
# notes and examples stay behind; they describe the template.
#
# Works in Git Bash on Windows, and in bash on macOS and Linux.

set -euo pipefail

usage() {
  echo "Usage: scripts/new-project.sh <target-folder> [--name <project>] [--allow-dirty] [--inside-repo]" >&2
  exit 2
}

target=""
name=""
allow_dirty=0
inside_repo=0
while [ $# -gt 0 ]; do
  case "$1" in
    --name) [ $# -ge 2 ] || usage; name="$2"; shift 2 ;;
    --allow-dirty) allow_dirty=1; shift ;;
    --inside-repo) inside_repo=1; shift ;;
    -h|--help) usage ;;
    -*) echo "Unknown option: $1" >&2; usage ;;
    *) [ -z "$target" ] || usage; target="$1"; shift ;;
  esac
done
[ -n "$target" ] || usage

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Validate the project name before touching anything. It goes into markdown tables and sed, so keep
# it to plain characters.
slug=""
if [ -n "$name" ]; then
  if ! printf '%s' "$name" | grep -qE '^[A-Za-z0-9][A-Za-z0-9 ._()+-]*$'; then
    echo "Project name may contain letters, digits, spaces and . _ ( ) + - only, and must start with a letter or digit: $name" >&2
    exit 1
  fi
  slug="$(printf '%s' "$name" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed 's/^-//; s/-$//')"
  [ -n "$slug" ] || { echo "Couldn't make a repository name from: $name" >&2; exit 1; }
fi
src="$root/project"
[ -d "$src" ] || { echo "Can't find $src. Run this from a copy of the AI BA Harness template." >&2; exit 1; }

version="$(tr -d '[:space:]' < "$root/HARNESS_VERSION")"
commit="unknown"
if git -C "$root" rev-parse --short HEAD >/dev/null 2>&1; then
  commit="$(git -C "$root" rev-parse --short HEAD)"
  if [ -n "$(git -C "$root" status --porcelain -- project HARNESS_VERSION)" ]; then
    if [ "$allow_dirty" -eq 1 ]; then
      commit="${commit}-dirty"
    else
      echo "The template has uncommitted changes under project/ or HARNESS_VERSION." >&2
      echo "Commit them first, or pass --allow-dirty to record the commit as ${commit}-dirty." >&2
      exit 1
    fi
  fi
fi

# Work out where the target would be without creating anything yet: the nearest folder that exists.
probe="$target"
while [ ! -d "$probe" ]; do probe="$(dirname "$probe")"; done
probe_abs="$(cd "$probe" && pwd)"
if [ -d "$target" ]; then
  target_abs="$(cd "$target" && pwd)"
else
  target_abs="$probe_abs/${target#"$probe"/}"
fi
existing_material="Existing documents or an existing knowledge repository stay where they are: list their path in PROJECT-PROFILE.md section 6 and /kb-seed reads them in place."

# The target must be new or empty. This script only ever adds files; it never changes, moves or
# deletes anything that was already there.
if [ -e "$target" ] && [ ! -d "$target" ]; then
  echo "The target exists and isn't a folder: $target" >&2; exit 1
fi
if [ -d "$target" ] && [ -n "$(ls -A "$target" 2>/dev/null)" ]; then
  echo "Nothing was copied: the target folder isn't empty ($target_abs)." >&2
  echo "Create the BA repository in a new, empty folder, for example ../<project>-ba-knowledge." >&2
  echo "$existing_material" >&2
  exit 1
fi

# Never create a project inside the template: it would be copied into every later project.
case "$target_abs/" in
  "$root"/*) echo "The target is inside the template ($root). Choose a folder outside it, e.g. ../<project>-ba-knowledge" >&2; exit 1 ;;
esac

# Not inside another git repository, unless the user explicitly asked for a subfolder of one.
outer=""
if git -C "$probe_abs" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  outer="$(git -C "$probe_abs" rev-parse --show-toplevel)"
  if [ "$inside_repo" -ne 1 ]; then
    echo "Nothing was copied: the target is inside the git repository $outer." >&2
    echo "Create the BA repository in a new folder outside it (recommended). If the user explicitly wants it" >&2
    echo "inside, pass --inside-repo: it then becomes a new subfolder there, and nothing else in $outer changes." >&2
    echo "$existing_material" >&2
    exit 1
  fi
fi

mkdir -p "$target"
target="$target_abs"

cp -a "$src/." "$target/"
cp "$root/HARNESS_VERSION" "$target/HARNESS_VERSION"
chmod +x "$target/tools/kb-sync.sh" 2>/dev/null || true

profile="$target/PROJECT-PROFILE.md"
sed -i.bak \
  -e "s#^| Harness version this copy started from | .*|\$#| Harness version this copy started from | \`$version\` |#" \
  -e "s#^| Harness commit this copy started from | .*|\$#| Harness commit this copy started from | \`$commit\` |#" \
  "$profile"
# Where the harness came from, for /improve-harness proposals. Credentials in the URL are dropped.
origin="$(git -C "$root" remote get-url origin 2>/dev/null | sed -E 's#://[^/@]+@#://#' || true)"
if [ -n "$origin" ]; then
  sed -i.bak -e "s#^| Harness repository | .*|\$#| Harness repository | \`$origin\` |#" "$profile"
fi
if [ -n "$name" ]; then
  sed -i.bak -e "s#^| Project name | .*|\$#| Project name | $name |#" \
             -e "s#^| BA repository | .*|\$#| BA repository | \`$slug-ba-knowledge\` |#" "$profile"
  sed -i.bak -e "1s#^\# \`<Project>\` BA knowledge#\# $name BA knowledge#" "$target/README.md"
  rm -f "$target/README.md.bak"
fi
rm -f "$profile.bak"

echo "Created a project BA knowledge repository in $target"
echo "  harness version $version, commit $commit"
echo
echo "Next:"
echo "  1. cd \"$target\" && git init -b main && git add -A && git commit -m \"Start from AI BA Harness $version\""
echo "  2. Create the shared remote repository (e.g. on GitHub), then: git remote add origin <url> && git push -u origin main"
echo "  3. Open your assistant there and sign in to Atlassian, then run /setup (\$setup in Codex):"
echo "       Claude Code: claude, then /mcp"
echo "       OpenCode:    opencode mcp auth atlassian, then opencode"
echo "       Codex:       codex, trust the project, approve the hook with /hooks, then codex mcp login atlassian"
echo "     A team that doesn't use one of them can delete its files; the handbook lists which they are."
if [ -n "$outer" ]; then
  echo
  echo "Note: this folder is inside the git repository $outer, and nothing in that repository was changed."
  echo "  Its own repository will show up there as an untracked folder. Ask the owner of $outer before adding"
  echo "  \"$(git -C "$target" rev-parse --show-prefix 2>/dev/null)\" to that repository's .gitignore."
fi
