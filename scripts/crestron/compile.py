"""
Crestron SIMPL+ Compiler

Compiles a SIMPL+ source file (.usp) into its Crestron artifacts by driving
the Crestron command-line compiler, SPlusCC.exe -- no SIMPL Windows GUI
required. This is the Crestron analog of scripts/qsys/compile.py.

A successful compile writes a .ush header next to the .usp and a set of
target artifacts (test.dll / test.cs / test.inf, plus supporting assemblies)
into a SPlsWork/ subfolder beside the source.

Requires the Crestron SIMPL+ compiler, installed by default to:
  C:\\Program Files (x86)\\Crestron\\Simpl\\SPlusCC.exe
(obtained via the Crestron Master Installer). Override the location with the
--compiler flag or the SPLUSCC environment variable.

Usage:
  python compile.py <file.usp | directory> [more ...] [options]

A directory argument compiles every .usp it contains (non-recursive).

Options:
  --target=LIST     Comma-separated targets: series2, series3, series4
                    (default: series3)
  --build           Compile only if changed (\\build) instead of forcing a
                    full rebuild (\\rebuild, the default)
  --compiler=PATH   Path to SPlusCC.exe (default: SPLUSCC env var, else the
                    standard install path)
  --out=PATH        Also write all compiler output to a log file (\\out)
  --silent          Pass \\silent to suppress the compiler's console output
  --errorcodes      Pass \\errorcodes to show compilation error codes

Examples:
  python compile.py MyModule.usp
  python compile.py MyModule.usp --target=series3,series4
  python compile.py a.usp b.usp --target=series2,series3
  python compile.py ./src --target=series3        # compile every .usp in ./src
"""

import glob
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field

# Target artifacts written into the SPlsWork/ subfolder, per module.
WORK_ARTIFACT_EXTS = (".dll", ".cs", ".inf")

DEFAULT_COMPILER = r"C:\Program Files (x86)\Crestron\Simpl\SPlusCC.exe"
VALID_TARGETS = ("series2", "series3", "series4")

# e.g. [C:\work\broken.usp] Error 1002 (Line 1) - Missing ';'
DIAGNOSTIC_PATTERN = re.compile(
    r"^\[(?P<path>.*?)\]\s+"
    r"(?P<kind>Error|Warning)\s+"
    r"(?P<code>\d+)\s+"
    r"(?:\(Line\s+(?P<line>\d+)\)\s+)?"
    r"-\s+(?P<message>.*?)\s*$",
    re.IGNORECASE,
)
TOTAL_ERRORS_PATTERN = re.compile(r"Total\s+Error\(s\):\s*(\d+)", re.IGNORECASE)
TOTAL_WARNINGS_PATTERN = re.compile(r"Total\s+Warning\(s\):\s*(\d+)", re.IGNORECASE)


@dataclass
class Diagnostic:
    """A single compiler error or warning line."""

    kind: str  # "error" | "warning"
    code: int
    message: str
    path: str = ""
    line: int | None = None

    def format(self):
        loc = f" (Line {self.line})" if self.line is not None else ""
        src = f"{os.path.basename(self.path)}: " if self.path else ""
        return f"  {src}{self.kind.upper()} {self.code}{loc} - {self.message}"


@dataclass
class CompileResult:
    """Parsed result of a SPlusCC.exe run."""

    error_count: int = 0
    warning_count: int = 0
    diagnostics: list = field(default_factory=list)
    raw_output: str = ""

    @property
    def ok(self):
        return self.error_count == 0


def build_command(compiler, usp_files, targets, rebuild=True, silent=False,
                  out_file=None, errorcodes=False):
    """Build the SPlusCC.exe argument list.

    Layout mirrors the compiler's own syntax:
        SPlusCC.exe \\rebuild <file> [<file> ...] \\target <device> [<device> ...]

    Global switches (\\out, \\silent, \\errorcodes) are appended *after* the
    target device list so they are never mistaken for target device tokens.
    """
    if not usp_files:
        raise ValueError("At least one .usp file is required")
    if not targets:
        raise ValueError("At least one target is required")

    args = [compiler]
    args.append("\\build" if not rebuild else "\\rebuild")
    args.extend(usp_files)
    args.append("\\target")
    args.extend(targets)
    if out_file:
        args.extend(["\\out", out_file])
    if silent:
        args.append("\\silent")
    if errorcodes:
        args.append("\\errorcodes")
    return args


def parse_output(text):
    """Parse SPlusCC.exe console output into a CompileResult.

    The 'Total Error(s)' / 'Total Warning(s)' summary lines are authoritative
    for the counts; individual bracketed lines are collected as diagnostics.
    """
    result = CompileResult(raw_output=text)

    for line in text.splitlines():
        match = DIAGNOSTIC_PATTERN.match(line.strip())
        if match:
            result.diagnostics.append(
                Diagnostic(
                    kind=match.group("kind").lower(),
                    code=int(match.group("code")),
                    message=match.group("message"),
                    path=match.group("path"),
                    line=int(match.group("line")) if match.group("line") else None,
                )
            )

    errors = TOTAL_ERRORS_PATTERN.search(text)
    warnings = TOTAL_WARNINGS_PATTERN.search(text)
    result.error_count = (
        int(errors.group(1))
        if errors
        else sum(1 for d in result.diagnostics if d.kind == "error")
    )
    result.warning_count = (
        int(warnings.group(1))
        if warnings
        else sum(1 for d in result.diagnostics if d.kind == "warning")
    )
    return result


def find_compiler(explicit=None):
    """Resolve the SPlusCC.exe path.

    Precedence: explicit argument > SPLUSCC env var > default install path.
    Raises FileNotFoundError if the resolved path does not exist.
    """
    candidate = explicit or os.environ.get("SPLUSCC") or DEFAULT_COMPILER
    if not os.path.isfile(candidate):
        raise FileNotFoundError(
            f"SIMPL+ compiler not found: {candidate}\n"
            f"Install it via the Crestron Master Installer, or pass "
            f"--compiler=<path to SPlusCC.exe> / set the SPLUSCC env var."
        )
    return candidate


def discover_usp_files(path):
    """Expand a path into a list of .usp files.

    A file path returns itself; a directory returns its .usp files
    (non-recursive, sorted). Raises FileNotFoundError if none are found.
    """
    if os.path.isfile(path):
        return [path]
    if os.path.isdir(path):
        found = sorted(glob.glob(os.path.join(path, "*.usp")))
        if not found:
            raise FileNotFoundError(f"No .usp files found in directory: {path}")
        return found
    raise FileNotFoundError(f"Path not found: {path}")


def find_artifacts(usp_path):
    """Return the compile artifacts that exist on disk for a given .usp.

    Looks for the <name>.ush header beside the source and the per-module
    <name>.dll / .cs / .inf outputs inside the SPlsWork/ subfolder. Shared
    Crestron assemblies in SPlsWork/ are intentionally excluded.
    """
    base = os.path.splitext(os.path.basename(usp_path))[0]
    src_dir = os.path.dirname(os.path.abspath(usp_path))

    artifacts = []
    header = os.path.join(src_dir, base + ".ush")
    if os.path.isfile(header):
        artifacts.append(header)

    work_dir = os.path.join(src_dir, "SPlsWork")
    for ext in WORK_ARTIFACT_EXTS:
        candidate = os.path.join(work_dir, base + ext)
        if os.path.isfile(candidate):
            artifacts.append(candidate)

    return artifacts


def compile_usp(usp_files, targets=("series3",), rebuild=True, silent=False,
                out_file=None, errorcodes=False, compiler=None):
    """Compile one or more .usp files. Returns (CompileResult, returncode)."""
    compiler_path = find_compiler(compiler)
    resolved = [os.path.abspath(f) for f in usp_files]
    for path in resolved:
        if not os.path.isfile(path):
            raise FileNotFoundError(f".usp file not found: {path}")

    args = build_command(compiler_path, resolved, list(targets),
                          rebuild=rebuild, silent=silent,
                          out_file=out_file, errorcodes=errorcodes)
    proc = subprocess.run(args, capture_output=True, text=True)
    output = (proc.stdout or "") + (proc.stderr or "")
    return parse_output(output), proc.returncode


def _print_report(result, returncode, usp_files=None):
    for diag in result.diagnostics:
        print(diag.format())

    status = "OK" if (result.ok and returncode == 0) else "FAILED"
    print(
        f"[{status}] Errors: {result.error_count}  "
        f"Warnings: {result.warning_count}  (exit {returncode})"
    )

    if result.ok and returncode == 0 and usp_files:
        for usp in usp_files:
            artifacts = find_artifacts(usp)
            if artifacts:
                print(f"  {os.path.basename(usp)} ->")
                for path in artifacts:
                    print(f"    {path}")


def main():
    argv = sys.argv[1:]
    if not argv or "--help" in argv or "-h" in argv:
        print(__doc__.strip())
        sys.exit(0 if argv else 1)

    targets = ["series3"]
    rebuild = True
    silent = False
    errorcodes = False
    out_file = None
    compiler = None
    inputs = []

    for arg in argv:
        if arg.startswith("--target="):
            targets = [t.strip() for t in arg.split("=", 1)[1].split(",") if t.strip()]
        elif arg.startswith("--compiler="):
            compiler = arg.split("=", 1)[1]
        elif arg.startswith("--out="):
            out_file = arg.split("=", 1)[1]
        elif arg == "--build":
            rebuild = False
        elif arg == "--silent":
            silent = True
        elif arg == "--errorcodes":
            errorcodes = True
        elif arg.startswith("--"):
            print(f"Error: unknown option '{arg}'")
            sys.exit(1)
        else:
            inputs.append(arg)

    if not inputs:
        print("Error: no .usp file or directory specified")
        sys.exit(1)

    # Expand any directory arguments into their .usp files.
    usp_files = []
    try:
        for item in inputs:
            for usp in discover_usp_files(item):
                if usp not in usp_files:
                    usp_files.append(usp)
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    invalid = [t for t in targets if t not in VALID_TARGETS]
    if invalid:
        print(f"Error: invalid target(s) {invalid}. Valid: {', '.join(VALID_TARGETS)}")
        sys.exit(1)

    try:
        result, returncode = compile_usp(
            usp_files, targets=targets, rebuild=rebuild,
            silent=silent, out_file=out_file, errorcodes=errorcodes,
            compiler=compiler
        )
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    _print_report(result, returncode, usp_files)
    sys.exit(0 if (result.ok and returncode == 0) else 1)


if __name__ == "__main__":
    main()
