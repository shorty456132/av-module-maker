"""
Extron ControlScript Module Checker

Static verification for an Extron ControlScript **device module** (`.py`).
ControlScript has no CLI compiler (unlike Crestron SIMPL+), so a module is
"verified" by static analysis rather than a build: this script encodes the hard
rules from reference/extron/EXTRON_CONSTRAINTS.md as AST checks and, when a
`pyright` executable is available, additionally type-checks the module against
the vendored `extronlib` stubs.

The AST checks are pure stdlib and run anywhere. Each finding is a `Diagnostic`
with a line number, a stable code, and a message. The exit code is non-zero if
any error-severity diagnostic is found, so a skill can gate on it.

Usage:
  python extron_check.py <file.py | directory> [more ...] [options]

A directory argument checks every .py it contains (non-recursive).

Options:
  --stubs=PATH      extronlib stubs dir to add to pyright's path (default:
                    reference/extron/extronlib/1.8.21xi). Only used if pyright
                    is installed.
  --no-pyright      Skip the optional pyright pass; run AST checks only.
  --warnings-as-errors
                    Treat warning-severity diagnostics as failures too.

Checks (see EXTRON_CONSTRAINTS.md for the rationale of each):
  EX-SYNTAX  module does not parse
  EX-SLEEP   blocking time.sleep()/sleep() — use extronlib.system.Wait/Timer (#9)
  EX-CONN    EthernetClientInterface.Connect(timeout) result discarded (#7)
  EX-RXBUF   a ReceiveData handler does not buffer the byte stream (#4/#5)
  EX-MIX     one interface bound to ReceiveData AND used with SendAndWait (#6)

Examples:
  python extron_check.py src/modules/device/MyDisplay.py
  python extron_check.py src/modules/device --no-pyright
"""

import ast
import glob
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass


DEFAULT_STUBS = os.path.join("reference", "extron", "extronlib", "1.8.21xi")


@dataclass
class Diagnostic:
    line: int
    code: str
    severity: str  # "error" | "warning"
    message: str

    def format(self, path):
        return "{}: {} {} (Line {}) - {}".format(
            path, self.severity.upper(), self.code, self.line, self.message
        )


# --- helpers --------------------------------------------------------------

def _attr_name(node):
    """Return the attribute name of a Call's func (e.g. 'Connect' for x.Connect())."""
    func = getattr(node, "func", None)
    if isinstance(func, ast.Attribute):
        return func.attr
    return None


def _decorator_targets_event(dec, event_name):
    """True if `dec` is @event(...) / @eventEx(...) referencing `event_name`."""
    if not isinstance(dec, ast.Call):
        return False
    fname = dec.func.id if isinstance(dec.func, ast.Name) else None
    if fname not in ("event", "eventEx"):
        return False
    for arg in dec.args:
        if isinstance(arg, ast.Constant) and arg.value == event_name:
            return True
        if isinstance(arg, ast.List):
            for elt in arg.elts:
                if isinstance(elt, ast.Constant) and elt.value == event_name:
                    return True
    return False


def _handler_buffers(func):
    """Heuristic: a ReceiveData handler is considered to buffer the stream if its
    body either accumulates with augmented assignment (`buf += data`) or touches a
    frame-splitting call (partition/find/split) or a name/attr that looks like a
    buffer. A handler that only decodes/parses the raw event payload does none."""
    for node in ast.walk(func):
        if isinstance(node, ast.AugAssign) and isinstance(node.op, ast.Add):
            return True
        if isinstance(node, ast.Call) and _attr_name(node) in ("partition", "find", "split"):
            return True
        if isinstance(node, ast.Name) and "buf" in node.id.lower():
            return True
        if isinstance(node, ast.Attribute) and "buf" in node.attr.lower():
            return True
    return False


# --- individual checks ----------------------------------------------------

def _check_sleep(tree):
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        is_time_sleep = (
            isinstance(func, ast.Attribute)
            and func.attr == "sleep"
            and isinstance(func.value, ast.Name)
            and func.value.id == "time"
        )
        is_bare_sleep = isinstance(func, ast.Name) and func.id == "sleep"
        if is_time_sleep or is_bare_sleep:
            out.append(Diagnostic(
                node.lineno, "EX-SLEEP", "error",
                "blocking sleep() stalls all event processing; use "
                "extronlib.system.Wait/Timer instead",
            ))
    return out


def _check_connect_result(tree):
    """Flag a bare-statement `x.Connect(<args>)` whose return is discarded. The
    interface's Connect(timeout) returns a status string that must be checked;
    the discriminator `has args` separates it from a no-arg module method like
    `self.Connect()`."""
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Expr):
            continue
        call = node.value
        if isinstance(call, ast.Call) and _attr_name(call) == "Connect" and call.args:
            out.append(Diagnostic(
                node.lineno, "EX-CONN", "error",
                "Connect() result is discarded; test it "
                "(e.g. \"if 'Connected' not in x.Connect(10): ...\") and retry on failure",
            ))
    return out


def _collect_rx_handlers(tree):
    """Return (handler_funcs, rx_bound). handler_funcs is the set of FunctionDef
    nodes that handle ReceiveData (via @event/@eventEx or by being assigned to a
    `.ReceiveData` attribute); rx_bound is True if any ReceiveData binding exists."""
    funcs_by_name = {}
    rx_names = set()
    decorated = set()
    rx_bound = False

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs_by_name[node.name] = node
            for dec in node.decorator_list:
                if _decorator_targets_event(dec, "ReceiveData"):
                    decorated.add(node)
                    rx_bound = True
        # `x.ReceiveData = <Name>`  → record handler name
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Attribute) and tgt.attr == "ReceiveData":
                    rx_bound = True
                    if isinstance(node.value, ast.Attribute):
                        rx_names.add(node.value.attr)
                    elif isinstance(node.value, ast.Name):
                        rx_names.add(node.value.id)

    handlers = set(decorated)
    for name in rx_names:
        if name in funcs_by_name:
            handlers.add(funcs_by_name[name])
    return handlers, rx_bound


def _check_receive_buffering(handlers):
    out = []
    for func in handlers:
        if not _handler_buffers(func):
            out.append(Diagnostic(
                func.lineno, "EX-RXBUF", "error",
                "ReceiveData handler '{}' does not buffer the stream; data arrives "
                "in <=1024-byte chunks as bytes, so accumulate and split on a "
                "delimiter (e.g. buffer += data; buffer.partition(b'\\r'))".format(func.name),
            ))
    return out


def _check_mixed_io(tree, rx_bound):
    out = []
    if not rx_bound:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and _attr_name(node) == "SendAndWait":
            out.append(Diagnostic(
                node.lineno, "EX-MIX", "warning",
                "SendAndWait (blocking) is used on a module that also handles "
                "ReceiveData; pick one model per interface (async Send + ReceiveData, "
                "or synchronous SendAndWait) — mixing can lose data",
            ))
    return out


# --- top-level AST check --------------------------------------------------

def check_source(source, filename="<module>"):
    """Run all AST checks against a module source string. Returns a list of
    Diagnostic (empty if clean). Never raises on bad syntax — reports EX-SYNTAX."""
    try:
        tree = ast.parse(source, filename=filename)
    except SyntaxError as exc:
        return [Diagnostic(exc.lineno or 1, "EX-SYNTAX", "error",
                           "module does not parse: {}".format(exc.msg))]

    diags = []
    diags += _check_sleep(tree)
    diags += _check_connect_result(tree)
    handlers, rx_bound = _collect_rx_handlers(tree)
    diags += _check_receive_buffering(handlers)
    diags += _check_mixed_io(tree, rx_bound)
    diags.sort(key=lambda d: (d.line, d.code))
    return diags


# --- optional pyright pass ------------------------------------------------

def run_pyright(path, stubs):
    """Type-check `path` against the vendored extronlib stubs, if pyright is on
    PATH. Returns (available, ok, output). Never raises."""
    exe = shutil.which("pyright")
    if not exe:
        return (False, True, "")
    env = dict(os.environ)
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = stubs + (os.pathsep + existing if existing else "")
    try:
        proc = subprocess.run(
            [exe, "--extrapaths", stubs, path],
            capture_output=True, text=True, env=env,
        )
    except OSError as exc:
        return (True, True, "pyright could not run: {}".format(exc))
    return (True, proc.returncode == 0, proc.stdout + proc.stderr)


# --- CLI ------------------------------------------------------------------

def _iter_targets(args):
    for arg in args:
        if os.path.isdir(arg):
            for py in sorted(glob.glob(os.path.join(arg, "*.py"))):
                yield py
        else:
            yield arg


def main(argv):
    stubs = DEFAULT_STUBS
    use_pyright = True
    warn_as_err = False
    targets = []
    for arg in argv:
        if arg.startswith("--stubs="):
            stubs = arg.split("=", 1)[1]
        elif arg == "--no-pyright":
            use_pyright = False
        elif arg == "--warnings-as-errors":
            warn_as_err = True
        elif arg.startswith("-"):
            print("Unknown option: {}".format(arg))
            return 2
        else:
            targets.append(arg)

    if not targets:
        print(__doc__)
        return 2

    failed = False
    for path in _iter_targets(targets):
        try:
            with open(path, "r", encoding="utf-8") as fh:
                source = fh.read()
        except OSError as exc:
            print("[FAILED] {} - cannot read: {}".format(path, exc))
            failed = True
            continue

        diags = check_source(source, filename=path)
        if use_pyright:
            available, ok, output = run_pyright(path, stubs)
            if available and not ok:
                failed = True
                print(output.strip())

        errors = [d for d in diags if d.severity == "error"]
        warnings = [d for d in diags if d.severity == "warning"]
        for d in diags:
            print(d.format(path))

        module_failed = bool(errors) or (warn_as_err and warnings)
        if module_failed:
            failed = True
            print("[FAILED] {} - {} error(s), {} warning(s)".format(
                path, len(errors), len(warnings)))
        else:
            note = " ({} warning(s))".format(len(warnings)) if warnings else ""
            print("[OK] {}{}".format(path, note))

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
