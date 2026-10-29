"""Guard tests for the TASKS.md build-board convention (reference/BUILD_TASKS.md).

Every create/revise skill keeps a TASKS.md kanban in the module directory while
it works, resumes from an existing one, and deletes it after a clean build.
These tests check the shared reference exists and that each skill still points
at it, so a later skill edit can't silently drop the board.
"""

import os
import re

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REFERENCE = os.path.join(REPO_ROOT, "reference", "BUILD_TASKS.md")

SKILLS = [
    "skills/qsys/create-plugin/SKILL.md",
    "skills/qsys/plugin-revision/SKILL.md",
    "skills/crestron/simplplus-create/SKILL.md",
    "skills/crestron/simplplus-revise/SKILL.md",
    "skills/crestron/simplsharp-create/SKILL.md",
    "skills/crestron/simplsharp-revise/SKILL.md",
]


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_reference_exists():
    assert os.path.isfile(REFERENCE)


@pytest.mark.parametrize("heading", ["## To Do", "## In Progress", "## Done"])
def test_reference_defines_columns(heading):
    assert re.search(r"^" + re.escape(heading) + r"\s*$", _read(REFERENCE), re.M)


@pytest.mark.parametrize("skill", SKILLS)
def test_skill_points_at_reference(skill):
    assert "reference/BUILD_TASKS.md" in _read(os.path.join(REPO_ROOT, skill))


@pytest.mark.parametrize("skill", SKILLS)
def test_skill_deletes_board_after_clean_build(skill):
    text = _read(os.path.join(REPO_ROOT, skill))
    assert re.search(r"[Dd]elete `TASKS\.md`", text)


@pytest.mark.parametrize("skill", SKILLS)
def test_skill_resumes_from_existing_board(skill):
    text = _read(os.path.join(REPO_ROOT, skill))
    assert re.search(r"[Rr]esume", text) and "TASKS.md" in text
