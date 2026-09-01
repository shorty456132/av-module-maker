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

# Convergence guard: halt if the count of unfinished cards fails to drop for this
# many passes running. `remaining` only drops when a card reaches Done (real
# forward progress), so a stall means the loop is spinning — e.g. a verify gate
# that never passes. This bounds wasted `claude -p` calls far below MAX; combined
# with a frozen board (which can't grow) and the MAX ceiling, it's the middle of
# three brakes. Override with the STALL_MAX env var.
STALL_MAX="${STALL_MAX:-2}"

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

board_remaining() {
  python "$BOARD" remaining "$MODULE_DIR" 2>/dev/null | tr -d '[:space:]'
}

pass=0
stall=0
prev_remaining="$(board_remaining)"
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

  # Convergence check: did this pass finish a card? If the unfinished count did
  # not drop, count a stall; a run of STALL_MAX stalls means we're not making
  # progress, so stop rather than burn the rest of the pass budget.
  rem="$(board_remaining)"
  if [[ -n "$rem" && -n "$prev_remaining" && "$rem" -lt "$prev_remaining" ]]; then
    stall=0
  else
    stall=$((stall + 1))
  fi
  echo "   remaining cards: ${rem:-unknown} (stall ${stall}/${STALL_MAX})"
  prev_remaining="$rem"
  if (( stall >= STALL_MAX )); then
    echo "⚠ Not converging — remaining cards did not drop for $STALL_MAX passes. Inspect $TODO." >&2
    exit 4
  fi
done

echo "⚠ Hit max passes ($MAX) without draining the board. Inspect $TODO." >&2
exit 1
