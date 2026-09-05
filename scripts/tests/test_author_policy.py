"""Repo-hygiene tests for the author-attribution policy.

Generated modules must never carry an author name that was inferred from
ambient session identity (git config, the user's email, this repo's own
plugin manifest). These tests guard the two halves of that:

  1. No personal identity strings leak into the skill instructions or the
     first-party reference docs that Claude reads while scaffolding.
  2. Every skill points at reference/AUTHOR_POLICY.md, which carries the
     ask-don't-infer rule.

The repo's own manifests (.claude-plugin/*.json) and LICENSE are
deliberately out of scope — Andrew is the author of the tool itself.
"""

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = REPO_ROOT / "skills"
POLICY_FILE = REPO_ROOT / "reference" / "AUTHOR_POLICY.md"

# Identity strings that must never appear in generated-module instructions.
IDENTITY_PATTERNS = ["Andrew", "Laiacano", "shorty456132", "a.laiacano@gmail.com"]

# reference/crestron/simplplus/documents/** is ~500 vendored Crestron help
# pages. Claude never emits from them verbatim and one contains "Andrew" as
# coincidental sample data, so they are excluded.
VENDORED = REPO_ROOT / "reference" / "crestron" / "simplplus" / "documents"


def skill_files():
    return sorted(SKILLS_DIR.rglob("SKILL.md"))


def first_party_docs():
    """Skill instructions plus the reference docs skills actually cite."""
    files = skill_files()
    for path in sorted((REPO_ROOT / "reference").rglob("*.md")):
        if VENDORED in path.parents or path == VENDORED:
            continue
        files.append(path)
    return files


def test_skills_are_discovered():
    """Guard against the globs silently matching nothing."""
    assert len(skill_files()) == 9


@pytest.mark.parametrize("path", first_party_docs(), ids=lambda p: p.name)
def test_no_personal_identity_in_instructions(path):
    text = path.read_text(encoding="utf-8")
    hits = [pat for pat in IDENTITY_PATTERNS if pat in text]
    assert not hits, f"{path.relative_to(REPO_ROOT)} leaks identity: {hits}"


def test_author_policy_file_exists():
    assert POLICY_FILE.is_file(), "reference/AUTHOR_POLICY.md is missing"
    text = POLICY_FILE.read_text(encoding="utf-8").lower()
    assert "never infer" in text
    assert "do not store" in text or "store nothing" in text


@pytest.mark.parametrize("path", skill_files(), ids=lambda p: p.parent.name)
def test_every_skill_references_policy(path):
    text = path.read_text(encoding="utf-8")
    assert "AUTHOR_POLICY.md" in text, (
        f"{path.relative_to(REPO_ROOT)} does not reference the author policy"
    )


def test_no_hardcoded_author_placeholder():
    """The Q-SYS info.lua template must not ship a fill-in-the-blank name."""
    text = (SKILLS_DIR / "qsys" / "create-plugin" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    assert not re.search(r'Author\s*=\s*"Author Name"', text)
    assert "-- by Author Name" not in text
