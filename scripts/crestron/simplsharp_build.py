"""
SIMPL# build orchestrator

A SIMPL# deliverable is built by TWO different toolchains and, until now, by two
separate commands with a manual seam between them. This script chains them:

    1. dotnet build   -> compile the C# project into a .clz
    2. locate the .clz (NOT the "-> .dll" the MSBuild log prints; see below)
    3. copy the .clz next to the .usp so bare-name resolution works
    4. SPlusCC.exe     -> compile the .usp wrapper (reuses simplplus_build.py)

so one command turns C# + a SIMPL+ wrapper into a placeable SIMPL Windows symbol.

The "-> .dll" decoy
-------------------
MSBuild prints its primary output -- `PresetStore -> ...\\bin\\Debug\\net47\\
PresetStore.dll`. The .clz NEVER appears in that log line; the Crestron SDK
target emits it as a side artifact into the SAME folder. So a "successful"
dotnet build with no .clz next to the .dll is the real failure (the SDK target
did not run -- wrong package, or a plain Microsoft.NET.Sdk project). This script
verifies the .clz on disk rather than trusting the build log. See
reference/crestron/SIMPLSHARP_COMPILATION.md.

Requirements
------------
- The .NET SDK (`dotnet` on PATH, or pass --dotnet=<path>). Visual Studio is NOT
  required -- it only wraps the same MSBuild + Crestron SDK targets.
- The SIMPL+ compiler SPlusCC.exe for step 4 (see simplplus_build.py / --compiler).

Usage
-----
  python simplsharp_build.py <project.csproj> <wrapper.usp> [options]
  python simplsharp_build.py --project=<csproj> --wrapper=<usp> [options]

Options:
  --config=NAME     Build configuration (default: Debug)
  --target=LIST     SIMPL+ targets for the wrapper, comma-separated
                    (default: series4 -- SIMPL# is net47 / 4-Series only)
  --no-restore      Pass --no-restore to dotnet build (skip NuGet restore)
  --dotnet=PATH     Path to the dotnet executable (default: `dotnet` on PATH)
  --compiler=PATH   Path to SPlusCC.exe (passed through to simplplus_build.py)
  --silent          Suppress SPlusCC.exe console output
  --errorcodes      Show SIMPL+ compilation error codes

Examples:
  python simplsharp_build.py src/PresetStore/PresetStore.csproj \\
                             src/PresetStoreWrapper/PresetStoreWrapper.usp
  python simplsharp_build.py --project=a.csproj --wrapper=b.usp --config=Release
"""

import glob
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simplplus_build import compile_usp  # noqa: E402  reuse the SIMPL+ compiler wrapper

# SIMPL# is net47 / 4-Series only, so the .usp wrapper over its .clz targets
# series4 by default -- NOT series3+series4 like the bare SIMPL+ compiler.
DEFAULT_TARGETS = ["series4"]

# The TFM whose .clz we want when a project multi-targets (e.g. net47 + net6.0).
DEFAULT_PREFER_TFM = "net47"


# --- pure helpers ---------------------------------------------------------

def build_dotnet_command(project, config="Debug", restore=True, dotnet="dotnet"):
    """Build the `dotnet build` argument list for the .clz project."""
    args = [dotnet, "build", project, "-c", config]
    if not restore:
        args.append("--no-restore")
    return args


def clz_search_root(project, config="Debug"):
    """The bin/<config> folder beside the .csproj, where the .clz is emitted."""
    proj_dir = os.path.dirname(os.path.abspath(project))
    return os.path.join(proj_dir, "bin", config)


def find_clz_files(search_root, prefer_tfm=DEFAULT_PREFER_TFM):
    """Return the .clz files under search_root (recursive), newest search first.

    This is the decoy catcher: a build that emitted only a `.dll` yields an
    empty list. When a project multi-targets and produces a .clz per TFM, prefer
    the `prefer_tfm` one (SIMPL# wants net47) so the result is unambiguous.
    """
    if not os.path.isdir(search_root):
        return []
    found = sorted(glob.glob(os.path.join(search_root, "**", "*.clz"), recursive=True))
    if prefer_tfm:
        preferred = [
            p for p in found
            if prefer_tfm in os.path.normpath(p).split(os.sep)
        ]
        if preferred:
            return preferred
    return found


def copy_clz_beside_wrapper(clz_path, usp_path):
    """Copy the .clz into the .usp's folder so `#USER_SIMPLSHARP_LIBRARY` resolves
    it by bare name. Overwrites a stale copy; a no-op if it is already there.
    Returns the destination path.
    """
    dest_dir = os.path.dirname(os.path.abspath(usp_path))
    dest = os.path.join(dest_dir, os.path.basename(clz_path))
    if os.path.abspath(clz_path) == os.path.abspath(dest):
        return dest
    shutil.copy2(clz_path, dest)
    return dest


# --- result types ---------------------------------------------------------

@dataclass
class StepResult:
    """One stage of the orchestration."""

    name: str   # dotnet-build | locate-clz | copy-clz | simplplus
    ok: bool
    detail: str = ""

    def format(self):
        mark = "OK " if self.ok else "FAIL"
        return f"  [{mark}] {self.name}: {self.detail}"


@dataclass
class BuildReport:
    """Aggregated result of a full SIMPL# build."""

    steps: list = field(default_factory=list)
    clz_path: str | None = None
    clz_beside_wrapper: str | None = None
    dotnet_output: str = ""
    usp_result: object = None

    @property
    def ok(self):
        return bool(self.steps) and all(s.ok for s in self.steps)


# --- default runners (injected in tests) ----------------------------------

def _default_dotnet_runner(args):
    """Run dotnet build; return (returncode, combined stdout+stderr)."""
    proc = subprocess.run(args, capture_output=True, text=True)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def _default_usp_compiler(usp_files, targets, compiler=None, silent=False,
                          errorcodes=False):
    """Compile the .usp via simplplus_build.py; return (CompileResult, returncode)."""
    return compile_usp(usp_files, targets=targets, compiler=compiler,
                       silent=silent, errorcodes=errorcodes)


# --- orchestration --------------------------------------------------------

def run_build(project, wrapper, config="Debug", targets=None, restore=True,
              dotnet="dotnet", prefer_tfm=DEFAULT_PREFER_TFM,
              compiler=None, silent=False, errorcodes=False,
              dotnet_runner=None, usp_compiler=None):
    """Run the full .clz -> copy -> .usp chain. Returns a BuildReport.

    Stops at the first failing step (a broken build never reaches the copy or
    the SIMPL+ compile). `dotnet_runner` and `usp_compiler` are injectable so
    the flow can be tested without a real toolchain.
    """
    if targets is None:
        targets = list(DEFAULT_TARGETS)
    dotnet_runner = dotnet_runner or _default_dotnet_runner
    usp_compiler = usp_compiler or _default_usp_compiler

    report = BuildReport()

    # 1. dotnet build -> .clz
    args = build_dotnet_command(project, config=config, restore=restore, dotnet=dotnet)
    rc, output = dotnet_runner(args)
    report.dotnet_output = output
    if rc != 0:
        report.steps.append(StepResult(
            "dotnet-build", False, f"dotnet build failed (exit {rc})"))
        return report
    report.steps.append(StepResult("dotnet-build", True, "build succeeded"))

    # 2. locate the .clz (catch the "-> .dll" decoy)
    root = clz_search_root(project, config)
    clz_files = find_clz_files(root, prefer_tfm=prefer_tfm)
    if not clz_files:
        report.steps.append(StepResult(
            "locate-clz", False,
            f"build reported success but no .clz was produced under {root} "
            f"(only a .dll?) -- the Crestron SDK target did not run"))
        return report
    if len(clz_files) > 1:
        report.steps.append(StepResult(
            "locate-clz", False,
            f"ambiguous: multiple .clz found, cannot choose: {clz_files}"))
        return report
    report.clz_path = clz_files[0]
    report.steps.append(StepResult("locate-clz", True, report.clz_path))

    # 3. stage the .clz next to the wrapper
    dest = copy_clz_beside_wrapper(report.clz_path, wrapper)
    report.clz_beside_wrapper = dest
    report.steps.append(StepResult("copy-clz", True, dest))

    # 4. compile the .usp wrapper
    result, urc = usp_compiler([wrapper], targets, compiler=compiler,
                               silent=silent, errorcodes=errorcodes)
    report.usp_result = result
    ok = getattr(result, "ok", False) and urc == 0
    report.steps.append(StepResult(
        "simplplus", ok,
        f"errors={result.error_count} warnings={result.warning_count} (exit {urc})"))
    return report


# --- CLI ------------------------------------------------------------------

@dataclass
class BuildOptions:
    project: str | None = None
    wrapper: str | None = None
    config: str = "Debug"
    targets: list = field(default_factory=lambda: list(DEFAULT_TARGETS))
    restore: bool = True
    dotnet: str = "dotnet"
    compiler: str | None = None
    silent: bool = False
    errorcodes: bool = False


def parse_cli(argv):
    """Parse argv (excluding program name) into BuildOptions.

    The .csproj and .usp may be given positionally (matched by extension) or via
    --project= / --wrapper=. Raises ValueError on an unknown --option.
    """
    opts = BuildOptions()
    for arg in argv:
        if arg.startswith("--project="):
            opts.project = arg.split("=", 1)[1]
        elif arg.startswith("--wrapper="):
            opts.wrapper = arg.split("=", 1)[1]
        elif arg.startswith("--config="):
            opts.config = arg.split("=", 1)[1]
        elif arg.startswith("--target="):
            opts.targets = [
                t.strip() for t in arg.split("=", 1)[1].split(",") if t.strip()
            ]
        elif arg.startswith("--dotnet="):
            opts.dotnet = arg.split("=", 1)[1]
        elif arg.startswith("--compiler="):
            opts.compiler = arg.split("=", 1)[1]
        elif arg == "--no-restore":
            opts.restore = False
        elif arg == "--silent":
            opts.silent = True
        elif arg == "--errorcodes":
            opts.errorcodes = True
        elif arg.startswith("--"):
            raise ValueError(f"unknown option '{arg}'")
        elif arg.lower().endswith(".csproj"):
            opts.project = arg
        elif arg.lower().endswith(".usp"):
            opts.wrapper = arg
        else:
            raise ValueError(f"unrecognized argument '{arg}' "
                             f"(expected a .csproj, a .usp, or an --option)")
    return opts


def _print_report(report):
    for step in report.steps:
        print(step.format())
    if report.usp_result is not None:
        for diag in report.usp_result.diagnostics:
            print(diag.format())
    status = "OK" if report.ok else "FAILED"
    print(f"[{status}] SIMPL# build")
    if report.ok:
        print(f"  .clz : {report.clz_path}")
        print(f"  staged next to wrapper: {report.clz_beside_wrapper}")


def main():
    argv = sys.argv[1:]
    if not argv or "--help" in argv or "-h" in argv:
        print(__doc__.strip())
        sys.exit(0 if argv else 1)

    try:
        opts = parse_cli(argv)
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    missing = [n for n, v in (("project (.csproj)", opts.project),
                              ("wrapper (.usp)", opts.wrapper)) if not v]
    if missing:
        print(f"Error: missing required {' and '.join(missing)}")
        sys.exit(1)
    for label, path in (("project", opts.project), ("wrapper", opts.wrapper)):
        if not os.path.isfile(path):
            print(f"Error: {label} not found: {path}")
            sys.exit(1)

    try:
        report = run_build(
            opts.project, opts.wrapper, config=opts.config, targets=opts.targets,
            restore=opts.restore, dotnet=opts.dotnet, compiler=opts.compiler,
            silent=opts.silent, errorcodes=opts.errorcodes,
        )
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    _print_report(report)
    sys.exit(0 if report.ok else 1)


if __name__ == "__main__":
    main()
