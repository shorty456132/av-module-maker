"""Unit tests for the SIMPL+ compiler wrapper (scripts/crestron/compile.py).

These test the pure logic only — command construction and parsing of the
real SPlusCC.exe console output. No subprocess is spawned, so they run on
any platform without the Crestron toolchain installed.

The fixture strings below are verbatim captures from SPlusCC.exe
(C:\\Program Files (x86)\\Crestron\\Simpl\\SPlusCC.exe) run against a known-good
and a deliberately-broken .usp file.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import compile as c  # noqa: E402


# --- Real SPlusCC.exe output captures ------------------------------------

SUCCESS_OUTPUT = (
    "Compiling for 3-Series Output: 'C:\\work\\test.usp'...\n"
    "Total Error(s): 0\n"
    "Total Warning(s): 0\n"
)

ERROR_OUTPUT = (
    "Compiling for 3-Series Output: 'C:\\work\\broken.usp'...\n"
    "[C:\\work\\broken.usp] Error 1002 (Line 1) - Missing ';'\n"
    "Total Error(s): 1\n"
    "Total Warning(s): 0\n"
)

# Synthesized from the observed Error line format (the compiler emits errors
# and warnings through the same formatter; the keyword is the only difference,
# as the symmetric "Total Error(s)/Total Warning(s)" summary confirms).
WARNING_OUTPUT = (
    "Compiling for 3-Series Output: 'C:\\work\\warn.usp'...\n"
    "[C:\\work\\warn.usp] Warning 4521 (Line 12) - Signal is never used\n"
    "Total Error(s): 0\n"
    "Total Warning(s): 1\n"
)


# --- build_command --------------------------------------------------------

def test_build_command_single_file_series3():
    args = c.build_command("SPlusCC.exe", ["a.usp"], ["series3"])
    assert args == [
        "SPlusCC.exe",
        "\\rebuild", "a.usp",
        "\\target", "series3",
    ]


def test_build_command_multiple_targets():
    args = c.build_command("SPlusCC.exe", ["a.usp"], ["series2", "series3", "series4"])
    assert args[-4:] == ["\\target", "series2", "series3", "series4"]


def test_build_command_multiple_files_between_rebuild_and_target():
    args = c.build_command("SPlusCC.exe", ["a.usp", "b.usp"], ["series3"])
    assert args == [
        "SPlusCC.exe",
        "\\rebuild", "a.usp", "b.usp",
        "\\target", "series3",
    ]


def test_build_command_build_not_rebuild():
    args = c.build_command("SPlusCC.exe", ["a.usp"], ["series3"], rebuild=False)
    assert "\\build" in args
    assert "\\rebuild" not in args


def test_build_command_rejects_no_files():
    with pytest.raises(ValueError):
        c.build_command("SPlusCC.exe", [], ["series3"])


def test_build_command_rejects_no_targets():
    with pytest.raises(ValueError):
        c.build_command("SPlusCC.exe", ["a.usp"], [])


def test_build_command_with_out_file():
    args = c.build_command("SPlusCC.exe", ["a.usp"], ["series3"], out_file="log.txt")
    assert "\\out" in args
    assert args[args.index("\\out") + 1] == "log.txt"


def test_build_command_with_errorcodes():
    args = c.build_command("SPlusCC.exe", ["a.usp"], ["series3"], errorcodes=True)
    assert "\\errorcodes" in args


def test_build_command_global_flags_after_targets():
    # \out / \silent / \errorcodes are global switches placed after the
    # target list so they never get consumed as target device tokens.
    args = c.build_command(
        "SPlusCC.exe", ["a.usp"], ["series3"],
        silent=True, out_file="log.txt", errorcodes=True,
    )
    target_idx = args.index("\\target")
    assert all(
        args.index(flag) > target_idx
        for flag in ("\\silent", "\\out", "\\errorcodes")
    )
    # the target device token must sit immediately after \target
    assert args[target_idx + 1] == "series3"


# --- parse_output ---------------------------------------------------------

def test_parse_success():
    result = c.parse_output(SUCCESS_OUTPUT)
    assert result.error_count == 0
    assert result.warning_count == 0
    assert result.ok is True
    assert result.diagnostics == []


def test_parse_error_counts():
    result = c.parse_output(ERROR_OUTPUT)
    assert result.error_count == 1
    assert result.warning_count == 0
    assert result.ok is False


def test_parse_error_diagnostic_fields():
    result = c.parse_output(ERROR_OUTPUT)
    assert len(result.diagnostics) == 1
    diag = result.diagnostics[0]
    assert diag.kind == "error"
    assert diag.code == 1002
    assert diag.line == 1
    assert diag.message == "Missing ';'"
    assert diag.path.endswith("broken.usp")


def test_parse_warning():
    result = c.parse_output(WARNING_OUTPUT)
    assert result.error_count == 0
    assert result.warning_count == 1
    assert result.ok is True  # warnings alone do not fail a compile
    assert len(result.diagnostics) == 1
    diag = result.diagnostics[0]
    assert diag.kind == "warning"
    assert diag.code == 4521
    assert diag.line == 12
    assert diag.message == "Signal is never used"


# --- find_compiler --------------------------------------------------------

def test_find_compiler_explicit_path(tmp_path):
    fake = tmp_path / "SPlusCC.exe"
    fake.write_text("")
    assert c.find_compiler(str(fake)) == str(fake)


def test_find_compiler_missing_explicit_raises():
    with pytest.raises(FileNotFoundError):
        c.find_compiler("Z:\\nope\\SPlusCC.exe")


# --- discover_usp_files ---------------------------------------------------

def test_discover_single_file(tmp_path):
    f = tmp_path / "one.usp"
    f.write_text("")
    assert c.discover_usp_files(str(f)) == [str(f)]


def test_discover_directory_returns_sorted_usp_only(tmp_path):
    (tmp_path / "b.usp").write_text("")
    (tmp_path / "a.usp").write_text("")
    (tmp_path / "notes.txt").write_text("")
    (tmp_path / "lib.clz").write_text("")
    found = c.discover_usp_files(str(tmp_path))
    assert [os.path.basename(p) for p in found] == ["a.usp", "b.usp"]


def test_discover_directory_is_non_recursive(tmp_path):
    (tmp_path / "top.usp").write_text("")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "nested.usp").write_text("")
    found = c.discover_usp_files(str(tmp_path))
    assert [os.path.basename(p) for p in found] == ["top.usp"]


def test_discover_empty_directory_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        c.discover_usp_files(str(tmp_path))


# --- find_artifacts -------------------------------------------------------

def test_find_artifacts_collects_ush_and_splswork(tmp_path):
    usp = tmp_path / "mod.usp"
    usp.write_text("")
    (tmp_path / "mod.ush").write_text("")  # header next to source
    work = tmp_path / "SPlsWork"
    work.mkdir()
    (work / "mod.dll").write_text("")
    (work / "mod.cs").write_text("")
    (work / "mod.inf").write_text("")
    (work / "SplusLibrary.dll").write_text("")  # shared, not this module

    names = {os.path.basename(p) for p in c.find_artifacts(str(usp))}
    assert names == {"mod.ush", "mod.dll", "mod.cs", "mod.inf"}


def test_find_artifacts_only_returns_existing(tmp_path):
    usp = tmp_path / "mod.usp"
    usp.write_text("")
    # nothing compiled yet -> no artifacts
    assert c.find_artifacts(str(usp)) == []
