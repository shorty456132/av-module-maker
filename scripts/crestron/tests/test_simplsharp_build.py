"""Unit tests for the SIMPL# build orchestrator (scripts/crestron/simplsharp_build.py).

The orchestrator chains the two toolchains a SIMPL# deliverable needs:

    dotnet build (.clz)  ->  locate the .clz (catch the "-> .dll" decoy)
    ->  copy the .clz beside the .usp  ->  SPlusCC.exe compile the .usp

These tests exercise the pure logic (command construction, .clz discovery, the
copy step, CLI parsing) plus the orchestration flow with *injected* runners, so
no `dotnet` and no `SPlusCC.exe` are ever spawned. They run on any platform.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import simplplus_build as c  # noqa: E402  reused for CompileResult in orchestration tests
import simplsharp_build as sb  # noqa: E402


# --- policy default -------------------------------------------------------

def test_default_target_is_series4_only():
    # SIMPL# builds net47 / 4-Series only, so the wrapper over its .clz targets
    # series4 by default (NOT series3+series4 like the bare SIMPL+ compiler).
    assert sb.DEFAULT_TARGETS == ["series4"]


# --- build_dotnet_command -------------------------------------------------

def test_build_dotnet_command_basic():
    args = sb.build_dotnet_command("proj/PresetStore.csproj")
    assert args == ["dotnet", "build", "proj/PresetStore.csproj", "-c", "Debug"]


def test_build_dotnet_command_custom_config():
    args = sb.build_dotnet_command("p.csproj", config="Release")
    assert args[args.index("-c") + 1] == "Release"


def test_build_dotnet_command_no_restore():
    args = sb.build_dotnet_command("p.csproj", restore=False)
    assert "--no-restore" in args
    args_default = sb.build_dotnet_command("p.csproj")
    assert "--no-restore" not in args_default


def test_build_dotnet_command_custom_dotnet_path():
    args = sb.build_dotnet_command("p.csproj", dotnet="/opt/dotnet/dotnet")
    assert args[0] == "/opt/dotnet/dotnet"


# --- clz_search_root ------------------------------------------------------

def test_clz_search_root_is_bin_config_beside_csproj(tmp_path):
    proj = tmp_path / "src" / "PresetStore" / "PresetStore.csproj"
    root = sb.clz_search_root(str(proj), config="Debug")
    assert os.path.normpath(root) == os.path.normpath(
        str(tmp_path / "src" / "PresetStore" / "bin" / "Debug")
    )


# --- find_clz_files (the "-> .dll" decoy catcher) -------------------------

def _touch(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write("")


def test_find_clz_files_finds_the_clz(tmp_path):
    root = tmp_path / "bin" / "Debug"
    _touch(str(root / "net47" / "PresetStore.clz"))
    found = sb.find_clz_files(str(root))
    assert [os.path.basename(p) for p in found] == ["PresetStore.clz"]


def test_find_clz_files_dll_only_is_empty(tmp_path):
    # The decoy: build "succeeded" but emitted only a .dll and no .clz.
    root = tmp_path / "bin" / "Debug"
    _touch(str(root / "net47" / "PresetStore.dll"))
    assert sb.find_clz_files(str(root)) == []


def test_find_clz_files_prefers_net47_when_multi_targeted(tmp_path):
    # A multi-TFM build emits a .clz per TFM; SIMPL# wants the net47 one.
    root = tmp_path / "bin" / "Debug"
    _touch(str(root / "net47" / "PresetStore.clz"))
    _touch(str(root / "net6.0" / "PresetStore.clz"))
    found = sb.find_clz_files(str(root), prefer_tfm="net47")
    assert len(found) == 1
    assert "net47" in os.path.normpath(found[0]).split(os.sep)


def test_find_clz_files_missing_root_is_empty(tmp_path):
    assert sb.find_clz_files(str(tmp_path / "does_not_exist")) == []


# --- copy_clz_beside_wrapper ----------------------------------------------

def test_copy_clz_beside_wrapper_places_it_next_to_usp(tmp_path):
    clz = tmp_path / "bin" / "Debug" / "net47" / "PresetStore.clz"
    _touch(str(clz))
    usp = tmp_path / "wrapper" / "PresetStoreWrapper.usp"
    _touch(str(usp))

    dest = sb.copy_clz_beside_wrapper(str(clz), str(usp))

    assert os.path.dirname(os.path.abspath(dest)) == os.path.dirname(os.path.abspath(str(usp)))
    assert os.path.basename(dest) == "PresetStore.clz"
    assert os.path.isfile(dest)


def test_copy_clz_beside_wrapper_overwrites_stale(tmp_path):
    clz = tmp_path / "out" / "PresetStore.clz"
    _touch(str(clz))
    with open(clz, "w") as fh:
        fh.write("NEW")
    usp = tmp_path / "wrapper" / "PresetStoreWrapper.usp"
    _touch(str(usp))
    stale = tmp_path / "wrapper" / "PresetStore.clz"
    with open(stale, "w") as fh:
        fh.write("OLD")

    dest = sb.copy_clz_beside_wrapper(str(clz), str(usp))
    with open(dest) as fh:
        assert fh.read() == "NEW"


def test_copy_clz_beside_wrapper_noop_when_same_dir(tmp_path):
    # If the .clz already sits next to the .usp, copying onto itself must not raise.
    clz = tmp_path / "PresetStore.clz"
    _touch(str(clz))
    usp = tmp_path / "PresetStoreWrapper.usp"
    _touch(str(usp))
    dest = sb.copy_clz_beside_wrapper(str(clz), str(usp))
    assert os.path.abspath(dest) == os.path.abspath(str(clz))
    assert os.path.isfile(dest)


# --- run_build orchestration (injected runners; no real toolchain) --------

def _ok_compile_result():
    return c.CompileResult(error_count=0, warning_count=0)


def _fake_usp_compiler_ok(usp_files, targets, compiler=None, silent=False, errorcodes=False):
    return _ok_compile_result(), 0


def _explode_usp_compiler(*a, **k):  # must never be called
    raise AssertionError("usp compiler should not run after an earlier step failed")


def test_run_build_happy_path_runs_all_four_steps(tmp_path):
    proj = tmp_path / "src" / "PresetStore" / "PresetStore.csproj"
    _touch(str(proj))
    _touch(str(tmp_path / "src" / "PresetStore" / "bin" / "Debug" / "net47" / "PresetStore.clz"))
    usp = tmp_path / "src" / "wrapper" / "PresetStoreWrapper.usp"
    _touch(str(usp))

    report = sb.run_build(
        str(proj), str(usp),
        dotnet_runner=lambda args: (0, "PresetStore -> ...\\PresetStore.dll"),
        usp_compiler=_fake_usp_compiler_ok,
    )

    assert report.ok is True
    assert [s.name for s in report.steps] == [
        "dotnet-build", "locate-clz", "copy-clz", "simplplus",
    ]
    # the .clz was staged next to the wrapper so bare-name resolution works
    assert os.path.isfile(os.path.join(os.path.dirname(str(usp)), "PresetStore.clz"))
    assert report.clz_path is not None


def test_run_build_stops_when_dotnet_fails(tmp_path):
    proj = tmp_path / "PresetStore.csproj"
    _touch(str(proj))
    usp = tmp_path / "PresetStoreWrapper.usp"
    _touch(str(usp))

    report = sb.run_build(
        str(proj), str(usp),
        dotnet_runner=lambda args: (1, "error CS1002: ; expected"),
        usp_compiler=_explode_usp_compiler,  # proves we short-circuit
    )

    assert report.ok is False
    assert [s.name for s in report.steps] == ["dotnet-build"]
    assert report.steps[0].ok is False


def test_run_build_detects_dll_decoy(tmp_path):
    # dotnet exits 0 but no .clz was produced (only a .dll) -> hard failure,
    # and we must NOT proceed to copy/compile.
    proj = tmp_path / "src" / "PresetStore" / "PresetStore.csproj"
    _touch(str(proj))
    _touch(str(tmp_path / "src" / "PresetStore" / "bin" / "Debug" / "net47" / "PresetStore.dll"))
    usp = tmp_path / "wrapper" / "PresetStoreWrapper.usp"
    _touch(str(usp))

    report = sb.run_build(
        str(proj), str(usp),
        dotnet_runner=lambda args: (0, "PresetStore -> ...\\PresetStore.dll"),
        usp_compiler=_explode_usp_compiler,
    )

    assert report.ok is False
    assert [s.name for s in report.steps] == ["dotnet-build", "locate-clz"]
    assert "no .clz" in report.steps[-1].detail.lower()


def test_run_build_propagates_simplplus_failure(tmp_path):
    proj = tmp_path / "src" / "PresetStore" / "PresetStore.csproj"
    _touch(str(proj))
    _touch(str(tmp_path / "src" / "PresetStore" / "bin" / "Debug" / "net47" / "PresetStore.clz"))
    usp = tmp_path / "wrapper" / "PresetStoreWrapper.usp"
    _touch(str(usp))

    def failing_usp(usp_files, targets, compiler=None, silent=False, errorcodes=False):
        return c.CompileResult(error_count=2, warning_count=0), 1

    report = sb.run_build(
        str(proj), str(usp),
        dotnet_runner=lambda args: (0, "ok"),
        usp_compiler=failing_usp,
    )
    assert report.ok is False
    assert report.steps[-1].name == "simplplus"
    assert report.steps[-1].ok is False


def test_run_build_passes_targets_to_usp_compiler(tmp_path):
    proj = tmp_path / "src" / "PresetStore" / "PresetStore.csproj"
    _touch(str(proj))
    _touch(str(tmp_path / "src" / "PresetStore" / "bin" / "Debug" / "net47" / "PresetStore.clz"))
    usp = tmp_path / "wrapper" / "PresetStoreWrapper.usp"
    _touch(str(usp))

    captured = {}

    def spy_usp(usp_files, targets, compiler=None, silent=False, errorcodes=False):
        captured["targets"] = targets
        captured["usp_files"] = usp_files
        return _ok_compile_result(), 0

    sb.run_build(str(proj), str(usp), targets=["series4"],
                 dotnet_runner=lambda args: (0, "ok"), usp_compiler=spy_usp)

    assert captured["targets"] == ["series4"]
    assert [os.path.basename(p) for p in captured["usp_files"]] == ["PresetStoreWrapper.usp"]


# --- parse_cli ------------------------------------------------------------

def test_parse_cli_positional_by_extension():
    opts = sb.parse_cli(["src/PresetStore.csproj", "src/PresetStoreWrapper.usp"])
    assert opts.project == "src/PresetStore.csproj"
    assert opts.wrapper == "src/PresetStoreWrapper.usp"


def test_parse_cli_explicit_flags():
    opts = sb.parse_cli(["--project=a.csproj", "--wrapper=b.usp"])
    assert opts.project == "a.csproj"
    assert opts.wrapper == "b.usp"


def test_parse_cli_defaults():
    opts = sb.parse_cli(["a.csproj", "b.usp"])
    assert opts.config == "Debug"
    assert opts.targets == ["series4"]
    assert opts.restore is True


def test_parse_cli_config_and_target_and_no_restore():
    opts = sb.parse_cli(["a.csproj", "b.usp", "--config=Release",
                         "--target=series3,series4", "--no-restore"])
    assert opts.config == "Release"
    assert opts.targets == ["series3", "series4"]
    assert opts.restore is False


def test_parse_cli_rejects_unknown_option():
    with pytest.raises(ValueError):
        sb.parse_cli(["a.csproj", "b.usp", "--nope"])
