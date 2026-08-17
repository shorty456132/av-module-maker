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

## Skills

- `/module-maker:create-plugin <description>` — scaffold a complete Q-SYS plugin (all
  modular `.lua` files) from a device description.
- `/module-maker:compile <plugin-directory>` — resolve `--[[ #include ]]` directives and
  produce a single `.qplug` file, with a version-bump prompt.
- `/module-maker:plugin-revision <plugin-directory>` — review and revise an existing Q-SYS
  plugin's Lua, then recompile.

## Roadmap

- **Now**: Q-SYS plugin creation, compilation, and revision.
- **Planned**: Crestron SIMPL+ and SIMPL# module creation, Extron Global Scripter module
  creation — each as its own skill + bundled reference material, following the same
  `skills/<name>/` + `reference/<platform>/` convention established here.

## License

MIT — see `LICENSE`.
