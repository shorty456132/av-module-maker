# Module Maker

A Claude Code plugin for scaffolding, compiling, and revising control-system modules —
Q-SYS plugins and Crestron SIMPL+ modules today, with Crestron SIMPL#/SIMPL# Pro and
Extron Global Scripter support planned.

Works from any Claude Code session in any project — no need to `cd` into this repo.

## Install

From any Claude Code terminal session:

```
/plugin marketplace add shorty456132/av-module-maker
/plugin install module-maker@module-maker
```

The first command registers this repo as a plugin marketplace (Claude Code reads
`.claude-plugin/marketplace.json` from the repo root); the second installs the plugin.
You can also run `/plugin` with no arguments to add the marketplace and install from the
interactive menu. The `/module-maker:*` skill commands run in the terminal CLI.

## Layout

Skills, reference docs, and scripts are grouped by platform:

```
skills/qsys/…        reference/qsys/…        scripts/qsys/…
skills/crestron/…    reference/crestron/…    scripts/crestron/…
```

Each platform folder is registered as a skill root in `.claude-plugin/plugin.json`
(`"skills": ["./skills/qsys/", "./skills/crestron/"]`), since plugin skill discovery
is not recursive.

## Skills

**Q-SYS** (ready):
- `/module-maker:create-plugin <description>` — scaffold a complete Q-SYS plugin (all
  modular `.lua` files) from a device description.
- `/module-maker:compile <plugin-directory>` — resolve `--[[ #include ]]` directives and
  produce a single `.qplug` file, with a version-bump prompt.
- `/module-maker:plugin-revision <plugin-directory>` — review and revise an existing Q-SYS
  plugin's Lua, then recompile.

**Crestron SIMPL+** (ready):
- `/module-maker:simplplus-create <description>` — scaffold a Crestron SIMPL+ module
  (`.usp`) from a device description, with correct INPUT/OUTPUT signal structure, event
  handlers, and automatic compile verification via the SIMPL+ Cross Compiler.
- `/module-maker:simplplus-revise <module-path>` — review and revise an existing SIMPL+
  module against the SIMPL+ constraints, then recompile clean.

**Crestron SIMPL# / SIMPL# Pro** (WIP — stubs scaffolded): `simplsharp-create` /
`simplsharp-revise`, `simplsharp-pro-create` / `simplsharp-pro-revise`.

## Roadmap

- **Now**: Q-SYS plugin creation, compilation, and revision; Crestron SIMPL+ module
  creation and revision with compile verification.
- **In progress**: Crestron SIMPL# and SIMPL# Pro module creation — folder structure
  and skill stubs are in place; reference docs and implementation to follow.
- **Planned**: Extron Global Scripter module creation, following the same
  `skills/<platform>/` + `reference/<platform>/` convention.

## License

MIT — see `LICENSE`.
