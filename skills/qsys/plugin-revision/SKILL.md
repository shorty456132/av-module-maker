---
name: plugin-revision
description: Review and revise an existing Q-SYS plugin — fix bugs, improve logic, and bump the version
argument-hint: plugin directory path
---

# Revise Q-SYS Plugin

Review and revise an existing Q-SYS plugin in the specified directory.

**Target directory:** `$ARGUMENTS`

If `$ARGUMENTS` is empty, ask the user which plugin directory to revise.

## Reference Documentation

Read `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_PATTERNS.md` and `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_CONSTRAINTS.md` before revising Lua — together they cover sockets, timers, JSON, control types, reserved names, design-time function signatures, naming/scoping rules, and the platform's common pitfalls, and answer most review questions without a doc search.

For anything they don't cover, **do not read the doc index or WebFetch help pages in this thread** — fetched pages are large and reading them inline exhausts the context window. Delegate instead: call the **Agent tool with `subagent_type: "Explore"`**, point it at `${CLAUDE_PLUGIN_ROOT}/reference/qsys/QSYS_DOC_INDEX.md` (a `Topic | Title | Source URL` table), have it grep the `Topic` column for the subject, **WebFetch** the matching Source URL for the current page, and use only the excerpts (plus the source URL) it returns. The full help text is not stored in the repo — it is QSC copyrighted material fetched live. Index topics prefixed `Schematic_Library-`, `Hardware-`, `Networking-`, `Control_Scripting-` cover components, hardware, networking, and Lua; `Getting_Started-`, `Standards_Definitions-`, `Code_Examples-`, `Recommended_Practices-` cover plugin standards, examples, and TCP/UDP/Serial.

## Step 1: Read the Plugin

Read **all** `.lua` files in the target directory to understand the full plugin:

- `info.lua` — metadata and current version
- `plugin.lua` — entry point and lifecycle structure
- `properties.lua` — user-configurable properties
- `controls.lua` — control definitions
- `layout.lua` — UI layout and styling
- `runtime.lua` — runtime logic, event handlers, networking
- `pages.lua`, `model.lua`, `components.lua`, `pins.lua`, `wiring.lua`, `rectify_properties.lua` — supporting files

## Step 2: Ask What to Revise

After reading the plugin, present a summary of what the plugin does, then ask the user what they want to do using AskUserQuestion with these options:

- **Bug Review** — Scan for common Q-SYS pitfalls and bugs (see checklist below)
- **Feature Revision** — Add, modify, or remove functionality
- **Layout/UI Revision** — Adjust control positioning, styling, or page structure
- **Full Review** — Comprehensive review of all files for bugs, style, and best practices

If the user selects **Bug Review** or **Full Review**, run through the Bug Review Checklist and report all findings before making changes. Ask the user which issues to fix.

If the user selects **Feature Revision** or **Layout/UI Revision**, ask the user to describe the specific changes they want.

## Bug Review Checklist

Check for these common issues:

### Control & Property Consistency
- [ ] Every `Controls["..."]` in `runtime.lua` has a matching entry in `controls.lua`
- [ ] Every control in `controls.lua` has a layout entry in `layout.lua`
- [ ] Every `Properties["..."]` or `props["..."]` reference has a matching definition in `properties.lua`
- [ ] Control `Count` values match indexed references (e.g., `"Button 1"`, `"Button 2"`)
- [ ] No references to `Controls` object in design-time functions

### Scoping & Garbage Collection
- [ ] Sockets, timers, and serial ports are **not** declared with `local` at top level
- [ ] Loop variables are captured in local variables before use in closures/EventHandlers
- [ ] No global variable name collisions with Q-SYS reserved names

### Networking & Communication
- [ ] `.IsConnected` or `.IsOpen` checked before writing to sockets/ports
- [ ] Socket/serial error handlers are defined (`.Error`, `.Timeout`, `.Closed`)
- [ ] Serial port opens are wrapped in `Timer.CallAfter` with `pcall`
- [ ] UDP buffering is handled if messages can arrive incomplete
- [ ] Heartbeat/reconnect logic present for TCP connections

### Runtime Safety
- [ ] Risky operations wrapped in `pcall` (socket opens, server listen, port opens)
- [ ] String concatenation with control values uses `tostring()`
- [ ] JSON parsing uses `pcall` to handle malformed responses
- [ ] No infinite loops or blocking operations in event handlers

### Debug Logging
- [ ] Commands sent to devices are printed (e.g., `print("TX: " .. cmd)`)
- [ ] Responses received from devices are printed (e.g., `print("RX: " .. data)`)
- [ ] Socket/serial errors, timeouts, and closures print a message
- [ ] Connection state changes (connect, disconnect, reconnect) are printed
- [ ] `pcall` failures print the error message

### Layout & UI
- [ ] All controls have appropriate sizing (buttons >= 80x24, text >= 150x24, LEDs >= 16x16)
- [ ] Text contrast is sufficient (light text on dark backgrounds, dark text on light)
- [ ] `PageNames` in `plugin.lua` matches pages handled in `layout.lua`
- [ ] ZOrder is correct (background elements have negative ZOrder)

### Plugin Metadata
- [ ] `PluginInfo` has all required fields (Name, Version, BuildVersion, Id, Author, Description)
- [ ] `Author` holds a real value. If it is already populated, **leave it exactly as-is** —
      never overwrite it or re-ask. If it is missing or still a placeholder (`Author Name`,
      `<author>`, empty), ask per `${CLAUDE_PLUGIN_ROOT}/reference/AUTHOR_POLICY.md`.
      Never infer it from `git config` or session identity.
- [ ] Version format is `Major.Minor.Fix.Development` (4-part semantic)

## Step 3: Make Changes

Edit **only** the files that need changes. Do not rewrite files that are already correct. Use the Edit tool for targeted modifications.

After making changes, run through the consistency checklist to verify nothing is broken:

- [ ] Every `Controls["..."]` reference in `runtime.lua` has a matching entry in `controls.lua`
- [ ] Every control defined in `controls.lua` has a layout entry in `layout.lua`
- [ ] Every `Properties["..."]` or `props["..."]` reference has a matching definition in `properties.lua`
- [ ] `PageNames` in `plugin.lua` matches the pages handled in `layout.lua`
- [ ] All `table.insert` calls target the correct local variable (`ctrls`, `props`, `pages`, etc.)
- [ ] Control `Count` values match the indexed references in `runtime.lua`

## Step 4: Version Bump & Compile

After all changes are made, read the current version from `info.lua` and ask the user which version component to bump using AskUserQuestion:

- **Major** — Breaking changes or major feature releases
- **Minor** — New features, backwards-compatible
- **Fix** — Bug fixes
- **Development** — Development/build iterations
- **Skip** — Keep the current version

Then compile with the appropriate flag:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/qsys/compile.py" $ARGUMENTS --bump=<choice>
```

If the user chooses Skip:

```
python "${CLAUDE_PLUGIN_ROOT}/scripts/qsys/compile.py" $ARGUMENTS
```

Tell the user the new version and where the `.qplug` file was created.
