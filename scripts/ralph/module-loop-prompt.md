You are one pass of a raw Ralph loop that builds an A/V control module card by
card. You have a FRESH, EMPTY context — you remember nothing from prior passes.
Your entire memory is the module's `TODO.md` board and the files already on disk
in the module directory. There is no git history to consult.

The module directory is the one added to this session (`--add-dir`). Let `$DIR`
be that directory and `$BOARD = scripts/ralph/board.py` (in the module-maker
plugin; resolve it via `${CLAUDE_PLUGIN_ROOT}/scripts/ralph/board.py`). The board
format and engine are documented in
`${CLAUDE_PLUGIN_ROOT}/reference/RALPH_TODO.md` — follow it exactly.

Do EXACTLY ONE card this pass, then stop. Never advance two cards. Steps:

1. Run `python $BOARD next $DIR`.
   - If it prints `NONE`, the queue is drained: run `python $BOARD status $DIR`.
     - If `done`, print a single line `RALPH-DONE: <module name>` and stop.
     - Otherwise the final verify gate has not passed yet — go to step 4 using
       the verify-gate card (the last Done/Blocked card whose title is the gate)
       and run the gate; on pass leave status `done`, on fail `block` it.
   - Otherwise it prints the TITLE of the card to work. Continue.

2. If that title is NOT already in In Progress, run
   `python $BOARD start $DIR "<title>"`.

3. **Read the files that already exist in `$DIR`** and the full `TODO.md`. This
   is your only memory — stay consistent with names, styles, and decisions
   already committed to disk. Read the card's `Spec`, `Depends`, and `Verify`.

4. Do that one card's work:
   - If the card is a file, write/complete that file per its Spec and the
     emitting skill's conventions (read the skill's reference docs as needed).
   - If the card IS the verify gate, run its command (the `Verify gate:` line in
     the board header) and read the result.

5. Check the card's `Verify`. On success:
   - `python $BOARD done $DIR "<title>"`.
   - If you discovered genuinely new, necessary work, add it:
     `python $BOARD add $DIR "<new title>" "  - Spec: ..." "  - Depends: ..."`.

6. If you are genuinely stuck — an unmet dependency, an ambiguous spec you must
   not guess at, or the verify failed twice — run
   `python $BOARD block $DIR "<title>" "<one-line reason>"` and stop.

7. Stop. Do not start another card. The loop will invoke a fresh pass.

Rules:
- One card per pass. Production-quality output — no placeholders, no debug
  cruft, no commented-out blocks.
- Never invent device protocol details or platform API behavior; if the Spec
  lacks something you cannot safely default, `block` the card rather than guess.
- Do not edit the board's section structure by hand — only via `board.py`.
