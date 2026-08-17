# Module Maker

A Claude Code plugin for scaffolding, compiling, and revising control-system modules —
starting with Q-SYS plugins, with Crestron (SIMPL+/SIMPL#) and Extron Global Scripter
support planned.

Works from any Claude Code session in any project — no need to `cd` into this repo.

## Install

```
/plugin marketplace add <path-or-org/repo-to-this-folder>
/plugin install module-maker@module-maker
```

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

**Crestron** (WIP — stubs scaffolded): `simplplus-create` / `simplplus-revise`,
`simplsharp-create` / `simplsharp-revise`, `simplsharp-pro-create` / `simplsharp-pro-revise`.

## Roadmap

- **Now**: Q-SYS plugin creation, compilation, and revision.
- **In progress**: Crestron SIMPL+, SIMPL#, and SIMPL# Pro module creation — folder
  structure and skill stubs are in place; reference docs and implementation to follow.
- **Planned**: Extron Global Scripter module creation, following the same
  `skills/<platform>/` + `reference/<platform>/` convention.

## License

MIT — see `LICENSE`.
