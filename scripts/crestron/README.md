# Crestron build/helper scripts

## `simplsharp_build.py` — SIMPL# (.clz + .usp) end-to-end build

Builds a **complete SIMPL# deliverable** with one command by chaining the two
toolchains a SIMPL# module needs. A SIMPL# module is always two parts — a C#
`.clz` and a SIMPL+ `.usp` wrapper — built by two different compilers; this
orchestrates them in the right order with the manual seam closed.

```
python simplsharp_build.py <project.csproj> <wrapper.usp> [options]
python simplsharp_build.py --project=<csproj> --wrapper=<usp> [options]
```

Four steps, stopping at the first failure:

1. **`dotnet build`** the C# project → `.clz` (Visual Studio not required).
2. **Locate the `.clz`** on disk — this catches the **`-> .dll` decoy**: MSBuild's
   log prints only the `.dll`, while the Crestron SDK target emits the `.clz` beside
   it. A build that produced only a `.dll` (SDK target didn't run) **fails here**
   instead of silently.
3. **Copy the `.clz` next to the `.usp`** so `#USER_SIMPLSHARP_LIBRARY "Name"`
   resolves it by bare name.
4. **`SPlusCC.exe` compile the `.usp`** (reuses `simplplus_build.py`, incl. CRLF fixup).

| Option | Description |
|---|---|
| `--config=NAME` | Build configuration (default `Debug`) |
| `--target=LIST` | SIMPL+ targets for the wrapper (default `series4` — SIMPL# is `net47`/4-Series only) |
| `--no-restore` | Pass `--no-restore` to `dotnet build` |
| `--dotnet=PATH` | Path to the `dotnet` executable (default: `dotnet` on PATH) |
| `--compiler=PATH` | Path to `SPlusCC.exe` (passed through to `simplplus_build.py`) |
| `--silent` / `--errorcodes` | Passed through to the SIMPL+ compile |

Requires the **.NET SDK** (`dotnet`) for the `.clz` and **`SPlusCC.exe`** for the
`.usp` (see below). Exit code is `0` only if every step succeeds. See
`reference/crestron/SIMPLSHARP_COMPILATION.md` for the build rules and the
`-> .dll` decoy in depth.

## `simplplus_build.py` — SIMPL+ (.usp) command-line compiler

Compiles SIMPL+ source (`.usp`) into its Crestron artifacts by driving the
Crestron command-line compiler `SPlusCC.exe` — **no SIMPL Windows GUI required**.
This is the Crestron analog of `scripts/qsys/compile.py`.

### Requirements

The Crestron SIMPL+ compiler must be installed (via the **Crestron Master
Installer**). Default location:

```
C:\Program Files (x86)\Crestron\Simpl\SPlusCC.exe
```

Override with `--compiler=<path>` or the `SPLUSCC` environment variable.

### Usage

```
python simplplus_build.py <file.usp | directory> [more ...] [options]
```

A **directory** argument compiles every `.usp` it contains (non-recursive, in
one compiler invocation) and reports the generated artifacts per module.

| Option | Description |
|---|---|
| `--target=LIST` | Comma-separated targets: `series2`, `series3`, `series4` (default `series3,series4` — both current generations) |
| `--build` | Compile only if changed (`\build`) instead of forcing a rebuild (`\rebuild`, default) |
| `--compiler=PATH` | Path to `SPlusCC.exe` |
| `--out=PATH` | Also write all compiler output to a log file (`\out`) |
| `--silent` | Suppress the compiler's console output (`\silent`) |
| `--errorcodes` | Show compilation error codes (`\errorcodes`) |

```bash
python simplplus_build.py MyModule.usp
python simplplus_build.py MyModule.usp --target=series3,series4
python simplplus_build.py a.usp b.usp --target=series2,series3
python simplplus_build.py ./src --target=series3        # every .usp in ./src
```

Exit code is `0` on a clean compile, non-zero if the compiler reports any error.
On success, each module's generated artifacts (the `.ush` header and its
`SPlsWork/` outputs) are listed under its name.

### Output artifacts

A successful compile writes, **next to the `.usp`**:

- `<name>.ush` — SIMPL+ header consumed by SIMPL Windows

and into a **`SPlsWork/`** subfolder beside the source:

- `<name>.dll`, `<name>.cs`, `<name>.inf` — target build outputs
- supporting Crestron assemblies (`SplusLibrary.dll`, `SplusObjects.dll`, …)

### How it works (SPlusCC.exe reference)

The wrapper builds and runs:

```
SPlusCC.exe \rebuild "<file.usp>" \target series3
```

`SPlusCC.exe` switches (from its own `\?` help):

| Switch | Meaning |
|---|---|
| `\build <module…>` | Compile module(s) |
| `\rebuild <module…>` | Force a full recompilation |
| `\target <device…>` | Target devices: `series2` \| `series3` \| `series4` |
| `\out <file>` | Write all compilation output to a file |
| `\usersplusfolder <folder>` | User SIMPL+ folder |
| `\silent` | Suppress console output |
| `\errorcodes` | Display compilation error codes |

Success output ends with `Total Error(s): 0` / `Total Warning(s): 0`; errors are
reported as `[<path>] Error <code> (Line <n>) - <message>`, which the wrapper
parses into a structured report.

Prior art / reference: the VS Code SIMPL+ extension
[`mikegustin/crestron-simpl-plus`](https://gitlab.com/mikegustin/crestron-simpl-plus)
drives the same compiler.

### Tests

```
python -m pytest scripts/crestron/tests/ -q
```

Tests cover command construction and parsing of real `SPlusCC.exe` output; they
run on any platform (no Crestron toolchain needed).
