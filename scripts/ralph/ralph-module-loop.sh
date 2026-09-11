#!/usr/bin/env bash
#
# ralph-module-loop.sh — a RAW Ralph loop for A/V module creation.
#
# Re-runs `claude -p` every pass, advancing exactly one card, until the board's
# `_Status:` line reads `done` or `blocked`. The module's TODO.md board plus the
# files on disk are the durable memory (no git).
#
# Session handling is token-monitored, not fresh-every-pass. The loop keeps one
# `claude` session warm across cards with `--resume`, so a small slice does not
# pay to rebuild context it just read, and rotates to a fresh `--session-id`
# only when the live window crosses CONTEXT_ROTATE_TOKENS (or a pass fails).
# That bounds context growth — the rot the old fresh-every-pass design avoided —
# while killing the per-pass re-read cost; the per-card verify gate is the
# correctness backstop. (This is still NOT the /ralph-loop plugin's unbounded
# accumulating session.)
#
# Usage:
#   ralph-module-loop.sh <module-dir> [max-passes]
#
# Watching a run (from anywhere, while it runs or after it ends):
#   python scripts/ralph/status.py show <module-dir>     # which pass, which card, spend
#   tail -f <module-dir>/.ralph/run.log                  # the live narration
#   cat <module-dir>/.ralph/REPORT.md                    # the post-run summary
#   touch <module-dir>/.ralph/STOP                       # stop cleanly, no PID hunt
#
# Exit codes (the caller's contract; mirrored in status.py EXIT_MEANING):
#   0 done · 1 max passes · 2 no TODO.md · 3 blocked · 4 not converging ·
#   5 stopped · 6 pass timeout
#
# Environment knobs:
#   STALL_MAX        (2)    passes without progress before halting
#   PASS_TIMEOUT     (900)  seconds before a wedged pass is killed
#   IDLE_WARN        (300)  seconds of silence before a heartbeat warning
#   PASS_BUDGET_USD  (—)    per-pass spend cap, handed to `claude --max-budget-usd`
#   RUN_BUDGET_USD   (—)    cumulative cap; the loop stops between passes
#   CONTEXT_ROTATE_TOKENS (150000)  live-window ceiling; above it the warm
#                           session is rotated to a fresh one (~75% of a 200K
#                           window — lower it to rotate sooner, raise to keep the
#                           session warm longer)
#
# Windows: run through Git Bash explicitly, e.g.
#   "C:/Program Files/Git/bin/bash.exe" scripts/ralph/ralph-module-loop.sh ./My-Plugin/
# (a bare `bash` may resolve to a misconfigured WSL bash).

set -uo pipefail

# The board, status and render helpers print status glyphs. A Windows pipe would
# otherwise encode them with the locale codec and kill the child mid-pass.
export PYTHONIOENCODING="${PYTHONIOENCODING:-utf-8}"

MODULE_DIR="${1:?usage: ralph-module-loop.sh <module-dir> [max-passes]}"
MAX="${2:-40}"

# Convergence guard: halt if the count of unfinished cards fails to drop for this
# many passes running. `remaining` only drops when a card reaches Done (real
# forward progress), so a stall means the loop is spinning — e.g. a verify gate
# that never passes. This bounds wasted `claude -p` calls far below MAX; combined
# with a frozen board (which can't grow) and the MAX ceiling, it's the middle of
# three brakes.
STALL_MAX="${STALL_MAX:-2}"

# Hang guards. Both defaults are guesses until a real run measures a SIMPL#
# `dotnet build` + `SPlusCC.exe` gate — raise them if a legitimate pass trips one.
PASS_TIMEOUT="${PASS_TIMEOUT:-900}"
IDLE_WARN="${IDLE_WARN:-300}"

PASS_BUDGET_USD="${PASS_BUDGET_USD:-}"
RUN_BUDGET_USD="${RUN_BUDGET_USD:-}"

# Live-context ceiling for the warm session. The renderer writes each pass's
# window occupancy (input + cache-read + cache-creation) to status.json as
# `last_context_tokens`; when it reaches this, the loop rotates to a fresh
# session rather than dragging a near-full window into the next card.
CONTEXT_ROTATE_TOKENS="${CONTEXT_ROTATE_TOKENS:-150000}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPT="$SCRIPT_DIR/module-loop-prompt.md"
BOARD="$SCRIPT_DIR/board.py"
STATUS="$SCRIPT_DIR/status.py"
RENDER="$SCRIPT_DIR/render_pass.py"
TODO="$MODULE_DIR/TODO.md"

# The plugin root (…/scripts/ralph → the plugin dir) and its reference/ docs.
# Both are added to the session and baked into the prompt so a pass can read the
# reference docs and run board.py without a permission prompt or a scavenger
# hunt for the path — the single biggest source of wasted per-pass turns.
PLUGIN_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
REF_DIR="$PLUGIN_ROOT/reference"

# A fresh session id (Python: uuidgen is absent on a stock Windows Git Bash).
new_sid() { python -c 'import uuid; print(uuid.uuid4())'; }

# `type -P` (not `command -v`, which would return bash's builtin) resolves the
# real `kill` binary in *this* shell's PATH, and the renderer is told where it
# is: a Python child started with a bare Windows PATH cannot see Git Bash's
# /usr/bin, and without a `kill` it refuses to terminate anything by pid.
KILL_BIN="$(type -P kill || true)"

RALPH_DIR="$MODULE_DIR/.ralph"
RUN_LOG="$RALPH_DIR/run.log"
STATUS_JSON="$RALPH_DIR/status.json"
STOP_FILE="$RALPH_DIR/STOP"
PID_FILE="$RALPH_DIR/child.pid"

if [[ ! -f "$TODO" ]]; then
  echo "No TODO.md in '$MODULE_DIR' — have the create/build skill emit the board first." >&2
  exit 2
fi

mkdir -p "$RALPH_DIR/logs"

# Everything the loop says goes to the terminal AND to run.log, so a background
# run is readable after the fact and a foreground one is readable live.
say() {
  printf '%s\n' "$*"
  printf '%s\n' "$*" >> "$RUN_LOG"
}

stamp() { date '+%H:%M:%S'; }

# One engine call per pass for every board fact (B_STATUS/B_CURRENT/B_DONE/...).
# Values are shell-quoted by `board.py summary --shell`, so this eval is safe.
load_board() {
  local vars
  vars="$(python "$BOARD" summary "$MODULE_DIR" --shell)" || {
    say "⚠ could not read the board at $TODO"
    return 1
  }
  eval "$vars"
}

# state=… plus any key=value / +key=value pairs, merged into .ralph/status.json.
status_write() {
  python "$STATUS" write "$MODULE_DIR" "$@" || true
}

finish() {
  local code="$1" message="$2"
  status_write "state=finished" "exit_code=$code"
  say "$message"
  say "   report: $(python "$STATUS" report "$MODULE_DIR")"
  exit "$code"
}

# The idle heartbeat lives in render_pass.py, not here: a backgrounded shell
# watcher leaves an orphaned `sleep` holding this pipe open after the pass ends,
# while the renderer's daemon thread dies with its process.

run_cost() {
  python - "$STATUS_JSON" <<'PYEOF' 2>/dev/null || echo 0
import json, sys
try:
    with open(sys.argv[1], encoding="utf-8") as f:
        print(json.load(f).get("cost_usd") or 0)
except Exception:
    print(0)
PYEOF
}

# This pass's live-context window size, which the renderer wrote to status.json.
# The rotation decision reads it; 0 if the file is missing or the pass emitted no
# result event (a crash), which with the claude_rc check still forces a rotation.
context_tokens() {
  python - "$STATUS_JSON" <<'PYEOF' 2>/dev/null || echo 0
import json, sys
try:
    with open(sys.argv[1], encoding="utf-8") as f:
        print(int(json.load(f).get("last_context_tokens") or 0))
except Exception:
    print(0)
PYEOF
}

# --- pre-flight -----------------------------------------------------------

if [[ -f "$STOP_FILE" ]]; then
  say "⏹ A STOP file is already present ($STOP_FILE) — remove it to run."
  status_write "state=stopped" "exit_code=5"
  finish 5 "⏹ Stopped before the first pass."
fi

CLAUDE_ARGS=(--add-dir "$MODULE_DIR"
             # The reference docs and board.py live under the plugin root, not
             # the module dir. Without this the pass is DENIED reading them and
             # burns turns retrying — a confirmed waste in real runs.
             --add-dir "$PLUGIN_ROOT"
             --permission-mode acceptEdits
             # acceptEdits auto-approves file writes but not Bash, so every
             # `python board.py …` and the `python …/compile.py` verify gate
             # would otherwise need an approval no headless run can give.
             --allowedTools "Bash(python:*)"
             --output-format stream-json --verbose
             # The dynamic sections change between passes and would bust the
             # prompt cache every time; excluding them keeps a stable prefix so
             # a resumed (or freshly rotated) pass reuses the cached preamble.
             --exclude-dynamic-system-prompt-sections)
[[ -n "$PASS_BUDGET_USD" ]] && CLAUDE_ARGS+=(--max-budget-usd "$PASS_BUDGET_USD")

status_write "state=running" "pass=0" "max_passes=$MAX" "pid=$$" "exit_code=null"
say "──────────── Ralph loop · $MODULE_DIR ────────────"
say "   max $MAX passes · stall $STALL_MAX · timeout ${PASS_TIMEOUT}s · stop: touch $STOP_FILE"

pass=0
stall=0
# The warm session carried across cards. `fresh_session=1` means the next pass
# creates it (`--session-id`); after a pass under the context ceiling it flips to
# 0 so the following pass resumes it. Rotation mints a new id and sets it back.
SID="$(new_sid)"
fresh_session=1
load_board || exit 2
prev_remaining="$B_REMAINING"

while (( pass < MAX )); do
  if [[ -f "$STOP_FILE" ]]; then
    finish 5 "⏹ STOP file found — halting between passes ($pass pass(es) run)."
  fi

  load_board || exit 2
  if [[ -z "$B_CURRENT" ]]; then
    # Nothing eligible: either drained (the pass below will confirm via the
    # gate) or every remaining card is behind a blocked dependency.
    B_CURRENT="(no eligible card)"
  fi

  pass=$((pass + 1))
  pass_label="$(printf '%02d' "$pass")"
  pass_started="$(date +%s)"
  say "──────────── Ralph pass $pass / $MAX ────────────"
  say "   [$(stamp)] card: $B_CURRENT · ${B_DONE}/${B_TOTAL} done · ${B_REMAINING} remaining"

  status_write "state=running" "pass=$pass" "max_passes=$MAX" \
               "current_card=$B_CURRENT" "pass_started_at=$(date -Iseconds)"

  # Keep the session warm across cards, or create/rotate it when fresh. The
  # prompt is told which, so it does not re-read what is already in context (or,
  # on a fresh pass, lean on context it no longer has). acceptEdits lets the pass
  # write files and run the verify gate unattended.
  if (( fresh_session )); then
    session_args=(--session-id "$SID")
    mode_line="Fresh session — your working memory is TODO.md plus the files you read this pass."
  else
    session_args=(--resume "$SID")
    mode_line="Continuing an open session — earlier cards this run are already in your context; re-read a file only if it changed on disk since."
  fi
  # Resolve the plugin paths into the prompt so a pass never burns turns hunting
  # for board.py: the ${CLAUDE_PLUGIN_ROOT} the prompt once told it to use is not
  # visible to the Bash tool, and the literal ${...} trips a permission block.
  prompt_text="$mode_line"$'\n\n'"$(cat "$PROMPT")"
  prompt_text="${prompt_text//__BOARD_PY__/$BOARD}"
  prompt_text="${prompt_text//__REF_DIR__/$REF_DIR}"
  prompt_text="${prompt_text//__MODULE_DIR__/$MODULE_DIR}"

  # The child's PID is parked in a file because the renderer sits downstream in
  # this pipe and cannot see it: that is how a mid-pass STOP kills the pass.
  # `wait $!` makes the group's status `claude`'s own, so PIPESTATUS[0] is the
  # real exit code — the old `|| true` hid a rate-limited or crashed pass until
  # it resurfaced two passes later as a stall.
  { timeout "$PASS_TIMEOUT" claude -p "$prompt_text" "${CLAUDE_ARGS[@]}" "${session_args[@]}" & \
      echo $! > "$PID_FILE"; wait $!; } \
    | tee "$RALPH_DIR/logs/pass-${pass_label}.jsonl" \
    | python "$RENDER" --dir "$MODULE_DIR" --pass "$pass" --card "$B_CURRENT" \
        --pid-file "$PID_FILE" --idle-warn "$IDLE_WARN" --kill-bin "$KILL_BIN" \
    | tee -a "$RUN_LOG"
  codes=("${PIPESTATUS[@]}")
  claude_rc="${codes[0]}"
  render_rc="${codes[2]}"

  elapsed=$(( $(date +%s) - pass_started ))
  say "   [$(stamp)] pass $pass ended in ${elapsed}s (claude exit $claude_rc)"

  if (( render_rc == 5 )) || [[ -f "$STOP_FILE" ]]; then
    finish 5 "⏹ STOP file found — halted mid-pass $pass."
  fi
  if (( claude_rc == 124 )); then
    status_write "state=timeout"
    finish 6 "⏱ Pass $pass exceeded PASS_TIMEOUT (${PASS_TIMEOUT}s) and was killed."
  fi
  if (( claude_rc != 0 )); then
    # Not fatal on its own — a pass can fail after finishing its card — but it
    # is now visible instead of swallowed, and the board check below decides.
    say "   ⚠ claude exited $claude_rc on pass $pass (see .ralph/logs/pass-${pass_label}.jsonl)"
  fi

  load_board || exit 2
  say "   board status: ${B_STATUS:-unknown} · ${B_DONE}/${B_TOTAL} cards done"
  status_write "pass=$pass"
  case "$B_STATUS" in
    done)    finish 0 "✓ Module complete in $pass pass(es)." ;;
    blocked) finish 3 "✗ Blocked — see the 🚫 Blocked section of $TODO." ;;
  esac

  # Convergence check: did this pass finish a card? If the unfinished count did
  # not drop, count a stall; a run of STALL_MAX stalls means we're not making
  # progress, so stop rather than burn the rest of the pass budget.
  if [[ -n "$B_REMAINING" && -n "$prev_remaining" && "$B_REMAINING" -lt "$prev_remaining" ]]; then
    stall=0
  else
    stall=$((stall + 1))
  fi
  say "   remaining cards: ${B_REMAINING:-unknown} (stall ${stall}/${STALL_MAX})"
  prev_remaining="$B_REMAINING"
  if (( stall >= STALL_MAX )); then
    finish 4 "⚠ Not converging — remaining cards did not drop for $STALL_MAX passes. Inspect $TODO."
  fi

  # Session rotation: the renderer wrote this pass's live-window size to
  # status.json. Keep resuming while it is under the ceiling; once it crosses —
  # or the pass exited non-zero, so its session may be unusable — mint a fresh id
  # so the next pass starts clean instead of dragging a near-full window forward.
  ctx="$(context_tokens)"
  if (( claude_rc != 0 )) || awk "BEGIN{exit !($ctx >= $CONTEXT_ROTATE_TOKENS)}"; then
    SID="$(new_sid)"
    fresh_session=1
    say "   ↻ rotating session — context ${ctx} tok ≥ ceiling ${CONTEXT_ROTATE_TOKENS} (or pass exit ${claude_rc}); next pass starts fresh"
  else
    fresh_session=0
  fi

  if [[ -n "$RUN_BUDGET_USD" ]]; then
    spent="$(run_cost)"
    if awk "BEGIN{exit !($spent >= $RUN_BUDGET_USD)}"; then
      finish 1 "💸 Run budget reached (\$$spent >= \$$RUN_BUDGET_USD) after $pass pass(es)."
    fi
  fi
done

finish 1 "⚠ Hit max passes ($MAX) without draining the board. Inspect $TODO."
