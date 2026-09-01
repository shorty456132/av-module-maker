#!/usr/bin/env bash
#
# ralph-module-loop.sh — a RAW Ralph loop for A/V module creation.
#
# Re-runs `claude -p` with the same prompt every pass. Each pass is a fresh
# process with a clean context window; the module's TODO.md board plus the files
# on disk are the ONLY memory (no git). The loop advances exactly one card per
# pass and stops when the board's `_Status:` line reads `done` or `blocked`.
#
# This is deliberately NOT the /ralph-loop plugin (that keeps one accumulating
# session via a Stop hook — the opposite of fresh context).
#
# Usage:
#   ralph-module-loop.sh <module-dir> [max-passes]
#
# Windows: run through Git Bash explicitly, e.g.
#   "C:/Program Files/Git/bin/bash.exe" scripts/ralph/ralph-module-loop.sh ./My-Plugin/
# (a bare `bash` may resolve to a misconfigured WSL bash).

set -uo pipefail

MODULE_DIR="${1:?usage: ralph-module-loop.sh <module-dir> [max-passes]}"
MAX="${2:-40}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPT="$SCRIPT_DIR/module-loop-prompt.md"
BOARD="$SCRIPT_DIR/board.py"
TODO="$MODULE_DIR/TODO.md"

if [[ ! -f "$TODO" ]]; then
  echo "No TODO.md in '$MODULE_DIR' — have the create/build skill emit the board first." >&2
  exit 2
fi

board_status() {
  python "$BOARD" status "$MODULE_DIR" 2>/dev/null | tr -d '[:space:]'
}

pass=0
while (( pass < MAX )); do
  pass=$((pass + 1))
  echo "──────────── Ralph pass $pass / $MAX ────────────"

  # Fresh context every pass. acceptEdits lets the pass write files and run the
  # verify gate unattended; swap for a settings allowlist if you prefer.
  claude -p "$(cat "$PROMPT")" --add-dir "$MODULE_DIR" --permission-mode acceptEdits || true

  status="$(board_status)"
  echo "   board status: ${status:-unknown}"
  case "$status" in
    done)    echo "✓ Module complete in $pass pass(es)."; exit 0 ;;
    blocked) echo "✗ Blocked — see the 🚫 Blocked section of $TODO."; exit 3 ;;
  esac
done

echo "⚠ Hit max passes ($MAX) without draining the board. Inspect $TODO." >&2
exit 1
