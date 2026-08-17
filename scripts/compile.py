"""
Q-SYS Plugin Compiler

Resolves --[[ #include "filename.lua" ]] directives in plugin.lua
and outputs a single .qplug file ready for Q-SYS Designer.

Automatically prompts for a semantic version bump (Major.Minor.Fix.Dev)
before compiling, or accepts a --bump flag for non-interactive use.

Usage:
  python compile.py <plugin-directory> [output-file]
  python compile.py <plugin-directory> --bump=major|minor|fix|development|skip

Examples:
  python compile.py ./My-Plugin
  python compile.py ./My-Plugin --bump=minor
  python compile.py ./My-Plugin ./My-Plugin.qplug
"""

import sys
import os
import re

INCLUDE_PATTERN = re.compile(r'^(\s*)--\[\[\s*#include\s+"([^"]+)"\s*\]\]')
BUILD_VERSION_PATTERN = re.compile(r'(BuildVersion\s*=\s*")(\d+(?:\.\d+)*)(")')
DISPLAY_VERSION_PATTERN = re.compile(r'(?<!Build)(Version\s*=\s*")(\d+(?:\.\d+)*)(")')


def read_version(info_path):
    """Read the current BuildVersion from info.lua."""
    with open(info_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = BUILD_VERSION_PATTERN.search(content)
    if match:
        return match.group(2)
    return None


def bump_version(version, bump_type):
    """Bump a semantic version string (Major.Minor.Fix.Dev)."""
    parts = [int(x) for x in version.split(".")]
    while len(parts) < 4:
        parts.append(0)

    if bump_type == "major":
        parts[0] += 1
        parts[1] = 0
        parts[2] = 0
        parts[3] = 0
    elif bump_type == "minor":
        parts[1] += 1
        parts[2] = 0
        parts[3] = 0
    elif bump_type == "fix":
        parts[2] += 1
        parts[3] = 0
    elif bump_type == "development":
        parts[3] += 1

    return ".".join(str(p) for p in parts)


def update_version_in_file(info_path, new_version):
    """Write the new version back to info.lua (both Version and BuildVersion)."""
    parts = [int(x) for x in new_version.split(".")]
    while len(parts) < 4:
        parts.append(0)
    build_version = ".".join(str(p) for p in parts)
    display_version = ".".join(str(p) for p in parts[:3])

    with open(info_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = BUILD_VERSION_PATTERN.sub(rf'\g<1>{build_version}\3', content)
    content = DISPLAY_VERSION_PATTERN.sub(rf'\g<1>{display_version}\3', content)
    with open(info_path, "w", encoding="utf-8") as f:
        f.write(content)


def prompt_version_bump(info_path):
    """Interactively prompt the user to bump the version."""
    current = read_version(info_path)
    if current is None:
        print("Warning: No version found in info.lua (expected BuildVersion = \"X.X.X.X\")")
        return

    print(f"Current version: {current}")
    print()
    print("Which version component to bump?")
    print(f"  1) Major       -> {bump_version(current, 'major')}")
    print(f"  2) Minor       -> {bump_version(current, 'minor')}")
    print(f"  3) Fix         -> {bump_version(current, 'fix')}")
    print(f"  4) Development -> {bump_version(current, 'development')}")
    print(f"  5) Skip (keep {current})")
    print()

    while True:
        choice = input("Enter choice [1-5]: ").strip()
        bump_map = {"1": "major", "2": "minor", "3": "fix", "4": "development"}
        if choice == "5":
            print(f"Keeping version {current}")
            return
        if choice in bump_map:
            new_version = bump_version(current, bump_map[choice])
            update_version_in_file(info_path, new_version)
            print(f"Version updated: {current} -> {new_version}")
            return
        print("Invalid choice. Enter 1-5.")


def resolve_includes(filepath, base_dir, included=None):
    if included is None:
        included = set()

    abs_path = os.path.normpath(os.path.join(base_dir, filepath))

    if abs_path in included:
        print(f"  Warning: Skipping circular include: {filepath}")
        return f"-- [circular include skipped: {filepath}]\n"

    if not os.path.isfile(abs_path):
        print(f"  Warning: Include file not found: {filepath}")
        return f"-- [file not found: {filepath}]\n"

    included.add(abs_path)
    lines = []

    with open(abs_path, "r", encoding="utf-8") as f:
        for line in f:
            match = INCLUDE_PATTERN.match(line)
            if match:
                indent = match.group(1)
                include_file = match.group(2)
                print(f"  Including: {include_file}")
                content = resolve_includes(include_file, base_dir, included)
                # Preserve indentation from the include directive
                if indent:
                    content = "\n".join(
                        indent + l if l.strip() else l
                        for l in content.splitlines()
                    )
                lines.append(content)
            else:
                lines.append(line.rstrip("\n"))

    return "\n".join(lines)


def compile_plugin(plugin_dir, output_path=None, bump_type=None):
    plugin_dir = os.path.abspath(plugin_dir)
    entry_point = os.path.join(plugin_dir, "plugin.lua")

    if not os.path.isfile(entry_point):
        print(f"Error: plugin.lua not found in {plugin_dir}")
        sys.exit(1)

    # Version bump
    info_path = os.path.join(plugin_dir, "info.lua")
    if os.path.isfile(info_path):
        if bump_type:
            # Non-interactive bump via CLI flag
            if bump_type == "skip":
                current = read_version(info_path)
                print(f"Keeping version {current}")
            else:
                current = read_version(info_path)
                if current:
                    new_version = bump_version(current, bump_type)
                    update_version_in_file(info_path, new_version)
                    print(f"Version updated: {current} -> {new_version}")
                else:
                    print("Warning: No version found in info.lua (expected BuildVersion = \"X.X.X.X\")")
        else:
            # Interactive prompt
            prompt_version_bump(info_path)
        print()

    # Determine output filename from PluginInfo.Name if not specified
    if output_path is None:
        plugin_name = os.path.basename(plugin_dir)

        # Try to extract name from info.lua
        if os.path.isfile(info_path):
            with open(info_path, "r", encoding="utf-8") as f:
                info_content = f.read()
                name_match = re.search(r'Name\s*=\s*"([^"]+)"', info_content)
                if name_match:
                    plugin_name = name_match.group(1)

        safe_name = re.sub(r'[^\w\s-]', '', plugin_name).strip().replace(' ', '-')
        output_path = os.path.join(plugin_dir, f"{safe_name}.qplug")

    print(f"Compiling: {entry_point}")
    print(f"Output:    {output_path}")
    print()

    result = resolve_includes("plugin.lua", plugin_dir)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)
        f.write("\n")

    print()
    print(f"Done! Created {output_path}")


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        sys.exit(1)

    args = [a for a in sys.argv[1:] if not a.startswith("--bump")]
    bump_flag = next((a for a in sys.argv[1:] if a.startswith("--bump")), None)

    bump_type = None
    if bump_flag:
        if "=" in bump_flag:
            bump_type = bump_flag.split("=", 1)[1].lower()
            valid = ("major", "minor", "fix", "development", "skip")
            if bump_type not in valid:
                print(f"Error: Invalid bump type '{bump_type}'. Use: {', '.join(valid)}")
                sys.exit(1)
        else:
            print("Error: Use --bump=major|minor|fix|development|skip")
            sys.exit(1)

    plugin_dir = args[0] if args else None
    output_path = args[1] if len(args) > 1 else None

    if not plugin_dir:
        print(__doc__.strip())
        sys.exit(1)

    if not os.path.isdir(plugin_dir):
        print(f"Error: Directory not found: {plugin_dir}")
        sys.exit(1)

    compile_plugin(plugin_dir, output_path, bump_type)


if __name__ == "__main__":
    main()
