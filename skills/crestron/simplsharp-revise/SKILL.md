---
name: simplsharp-revise
description: Review and revise an existing Crestron SIMPL# library (.clz) C# project — fix bugs, improve logic, verify against SIMPL# constraints
argument-hint: project file or directory path
---

# Revise Crestron SIMPL# Library

A SIMPL# module is **two halves**: a C# class compiled to a `.clz`, and a SIMPL+
`.usp` wrapper that is the actual SIMPL Windows symbol. **This skill owns the C#
half.** The class/`.clz` is the **source of truth** for the wrapper's I/O — so if a
revision changes the class's public surface, the wrapper must be re-synced to match
(see Step 3). Verify both halves the same way `simplsharp-create` does: the
orchestrator, exit 0.

## Before revising
- Confirm this is a **SIMPL#** job (`.clz` + `.usp` wrapper), not SIMPL# Pro (`.cpz`):
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_OVERVIEW.md`.
- Read `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp/SIMPLSHARP_CONSTRAINTS.md`
  (the **Gotchas #1–8** — `net47`/4-Series only; `SimplSharpString` for serial and
  `ushort` for digital/analog at the boundary; never block the SIMPL+ thread; feedback
  only through delegate properties; `IDisposable` on program stop) and
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/simplsharp/SIMPLSHARP_PATTERNS.md`
  (**Pattern 1** = the C# class; **Pattern 2** = the wrapper glue).
- For `Crestron.SimplSharp*` API questions, search the corpus per
  `${CLAUDE_PLUGIN_ROOT}/reference/crestron/SIMPLSHARP_API_CORPUS.md` via the
  `crestron-lookup` sub-agent — never bulk-load or invent a signature.
- Locate both halves from the path you were given: the `.csproj` (the `.clz` project)
  and its sibling `<Name>Wrapper/<Name>Wrapper.usp`. The orchestrator needs both.

## Step 1 — Establish a build baseline (before any edit)
Compile the module **before** changing anything, so a later failure is attributable to
your edit and not blamed on a pre-existing error. This mirrors `simplplus-revise`'s
pre-edit compile baseline — but here it runs through the SIMPL# orchestrator, which
builds the `.clz`, stages it beside the wrapper, and compiles the wrapper in one shot:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplsharp_build.py" \
    <Name>/<Name>.csproj <Name>Wrapper/<Name>Wrapper.usp
```

Read the step lines and record the result before touching anything:

- **`[OK] SIMPL# build` (exit 0):** clean baseline. Note the `.clz` path and the class's
  current public surface (public methods + delegate properties) — Step 3 compares the
  post-edit surface against this to decide whether the wrapper needs re-syncing.
- **`[FAILED]` (exit ≠ 0):** the module did **not** start clean. Record which step failed
  and each `ERROR <code> (Line <n>)` — these are pre-existing and are what the revision may
  be meant to fix. Do **not** attribute them to an edit you have not made yet.
- **If the script prints `SIMPL+ compiler not found` or `dotnet` / the SDK is missing:**
  the toolchain isn't installed on this host. Do **not** report the module broken and do
  **not** fabricate a baseline. Tell the user the baseline could not be established here,
  hand them the command above, and note the install path (Crestron Master Installer for
  `SPlusCC.exe`, or `--compiler=<path>` / the `SPLUSCC` env var; `dotnet` on PATH with the
  SDK package restoring from nuget.org). Same graceful fallback as `simplsharp-create`.

## Step 2 — Audit & fix
**A green baseline does not mean bug-free.** Most SIMPL# defects are *runtime/boundary*
mistakes, not C# compile errors — a blocking call, a leaked handle, or `System.String` at
the boundary all compile and produce a `.clz` that Step 1 reports `[OK]`. The build proves
the module *assembles*, not that it *behaves*. So audit the class against the **Gotchas
#1–8** in `SIMPLSHARP_CONSTRAINTS.md` by reading, not by trusting the exit code:

- [ ] **#3 — never block the SIMPL+ thread.** No `Thread.Sleep`, synchronous socket read,
      long loop, or device wait inside a public method — it stalls the whole SIMPL Windows
      program. Offload to a `CTimer`/`CrestronThread`, return immediately, report back
      through a callback. *(This is the classic one the compiler can't catch.)*
- [ ] **#2 — marshal types at the boundary.** Serial params/returns are `SimplSharpString`
      (not `System.String`); digital/analog are `ushort`. A public method with an
      unmarshalable signature silently never fires from SIMPL+.
- [ ] **#4 — feedback only through delegate properties**, invoked null-guarded. No other
      path drives an output.
- [ ] **#7 — `IDisposable`** stops timers/threads, closes sockets, and nulls callbacks in
      `Dispose()`, or a program restart leaks handles.
- [ ] **#1 / #8** — no unsupported desktop `System.*` API on the `net47` 4-Series runtime
      (use the `Crestron.SimplSharp.*` equivalent); analog scaled to/from `ushort` 0–65535.
- For any `Crestron.SimplSharp*` API you're unsure of, confirm the signature via
  `crestron-lookup` (per `SIMPLSHARP_API_CORPUS.md`) — never invent one.

**Fix the bugs, but keep the public surface stable** — the class's public methods and
delegate properties *are* the wrapper's I/O contract (Decision 5). A fix that stays inside
existing members (like offloading a blocked call to a `CTimer`) needs no wrapper change;
re-verify it with a plain orchestrator rebuild (Step 4). Only when the fix must
**add/remove/rename** a public member does the wrapper need re-syncing — that's Step 3.

## Step 3 — Wrapper sync (only if the public surface changed)
The class's public surface **is** the wrapper's I/O contract, so compare the post-edit
surface against the one you recorded in Step 1:

- **Unchanged** (fix stayed inside existing members — the common case): the wrapper still
  matches. **No wrapper edit** — skip straight to Step 4's rebuild.
- **Changed** — a public method or delegate property was **added, removed, or renamed**:
  the wrapper no longer mirrors the class and must be re-synced (Decision 8). Leaving it
  stale fails in one of two ways:
  - a **renamed/removed** member still called by the wrapper → the orchestrator's SIMPL+
    step errors, e.g. `ERROR 1009 … Class or Structure does not contain member: 'X'`;
  - an **added** member with no wrapper wiring → builds clean but the new signal silently
    does nothing (the compiler can't flag it — same trap as Step 2).

To re-sync, re-derive the signal spec from the **new** class surface (the same mechanical
method→input / delegate→output table as `simplsharp-create` Step 4), then **invoke
`simplplus-revise`** with that spec to update the wrapper — the method binding
(`device.<Method>(…)` in the `CHANGE` handler), plus the `CALLBACK FUNCTION` +
`RegisterDelegate` for any added/renamed delegate property. `simplplus-revise` owns the
SIMPL+ rules (I/O order, `_SKIP_`, CRLF); this skill only hands it the spec derived from
the built class, so the wrapper is re-derived from the `.clz`, never re-guessed from prose.

## Step 4 — Re-verify & summarize
Re-run the orchestrator and compare against the Step 1 baseline, so you know which errors
(if any) your change introduced versus which were already present:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplsharp_build.py" \
    <Name>/<Name>.csproj <Name>Wrapper/<Name>Wrapper.usp
```

- A revision isn't done until this exits **0** (or emits the documented toolchain-missing
  fallback from Step 1 — same graceful handling; don't report broken when the toolchain is
  simply absent).
- Summarize **every change made** — both halves: the C# fixes and any wrapper re-sync (or
  note explicitly that the public surface was unchanged, so the wrapper needed no edit).

## Ralph Loop Mode (optional — for long or unattended revisions)

For a large audit, or when the user wants the revision to run autonomously, do not
work every gotcha in one session. Instead **emit a `TODO.md` board** and hand off to
the raw Ralph loop, which works one card per fresh-context pass. The full contract is
`${CLAUDE_PLUGIN_ROOT}/reference/RALPH_TODO.md`; the board engine is
`${CLAUDE_PLUGIN_ROOT}/scripts/ralph/board.py`.

Use this mode when the user asks for a Ralph loop / TODO.md / unattended revision.
Otherwise revise inline as usual (Steps 1–4 above).

**To emit the board**, translate Steps 1–4 into a **bug-checklist board**: a baseline
build first, one audit-and-fix card per gotcha class (the `## Step 2 — Audit & fix`
checklist, #1–8), a conditional wrapper-sync card, and the orchestrator re-verify as
the final gate. Write `TODO.md` into the module directory **before** touching any
files, with the header line `_Plan: frozen_` and the **complete** card list up
front: a frozen board cannot grow during the loop (`board.py add` is refused), so a
cold pass that finds a further defect `block`s (never adds). The card list is:

1. `baseline-build` — run the orchestrator **before any edit** to establish a baseline (Step 1); record the current public surface (methods + delegate properties) in the card's notes so later cards know it cold.
2. `audit-block` — Gotcha #3 (never block the SIMPL+ thread: no `Thread.Sleep`/sync socket read/long loop in a public method; offload to `CTimer`/`CrestronThread`). Depends: `baseline-build`.
3. `audit-marshal` — Gotcha #2 (`SimplSharpString` for serial, `ushort` for digital/analog at the boundary; no `System.String`). Depends: `baseline-build`.
4. `audit-feedback` — Gotcha #4 (feedback only through null-guarded delegate properties). Depends: `baseline-build`.
5. `audit-dispose` — Gotcha #7 (`IDisposable` stops timers/threads, closes sockets, nulls callbacks). Depends: `baseline-build`.
6. `audit-runtime` — Gotchas #1/#8 (no unsupported desktop `System.*` on `net47` 4-Series; analog scaled to/from `ushort` 0–65535). Depends: `baseline-build`.
7. `wrapper-sync` — re-sync the wrapper **only if** an audit card added/removed/renamed a public member (Step 3); otherwise a no-op that records "surface unchanged". Depends: the five `audit-*` cards.
8. **final card `re-verify`** — the orchestrator verify gate (Step 4). Depends: `wrapper-sync`.

Because a loop pass has only `TODO.md` + the files on disk as memory, fold each
gotcha's rule **into its card's `Spec`** so a cold pass can apply it without reading
`SIMPLSHARP_CONSTRAINTS.md` (though a card may still consult it). Two constraints are
load-bearing for the board's correctness:

- **Keep the public surface stable unless a fix requires changing it.** The class's
  public methods and delegate properties **are** the wrapper's I/O contract (Decision
  5). Each `audit-*` card's `Spec` must say: fix inside existing members where
  possible (e.g. offload a blocked call to a `CTimer`) — that needs no wrapper change;
  only add/remove/rename a member when the fix demands it, and if so, note it for the
  `wrapper-sync` card.
- **`wrapper-sync` runs after every audit card** (`Depends:` all five) so it sees the
  final surface. If unchanged, it records "surface unchanged, wrapper needs no edit"
  and does nothing; if changed, it re-derives the spec from the **new** class surface
  and invokes `simplplus-revise` to update the wrapper (`simplplus-revise` owns the
  SIMPL+ rules; this card only hands it the spec derived from the built class).

The **final card is the verify gate** — its `Verify gate:` header line and the card's
command are:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/crestron/simplsharp_build.py" ./<Name>/<Name>/<Name>.csproj ./<Name>/<Name>Wrapper/<Name>Wrapper.usp
```

A revision is not done until this card exits 0 (or emits the documented
toolchain-missing fallback — same graceful handling). Then start the loop (from Git
Bash on Windows):

```
scripts/ralph/ralph-module-loop.sh ./<Name>/
```
