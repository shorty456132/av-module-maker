---
name: compile
description: Compile a Q-SYS plugin directory into a single .qplug file
argument-hint: plugin directory path
---

# Compile Q-SYS Plugin

Run the plugin compiler to resolve all `--[[ #include ]]` directives and produce a `.qplug` file.

**Target directory:** `$ARGUMENTS`

If `$ARGUMENTS` is empty, ask the user which plugin directory to compile.

## Version Bump

Before compiling, read the `info.lua` file in the target directory to find the current version (the `Version` field in `PluginInfo`). The version follows semantic format: `Major.Minor.Fix.Development`.

Display the current version to the user and ask which component to bump using AskUserQuestion with these options:
- **Major** — Breaking changes or major feature releases
- **Minor** — New features, backwards-compatible
- **Fix** — Bug fixes
- **Development** — Development/build iterations
- **Skip** — Keep the current version

Then run the compile command with the appropriate `--bump` flag:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/compile.py" $ARGUMENTS --bump=<choice>
```

If the user chooses Skip, run without the `--bump` flag:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/compile.py" $ARGUMENTS
```

If the compile succeeds, tell the user the new version and where the `.qplug` file was created.
