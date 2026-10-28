# Build Board — `TASKS.md`

Every create and revise skill tracks its work in a small `TASKS.md` kanban kept in
the module directory it is building or revising. The board paces the build one
card at a time and is the resume point: at any card boundary the user can check
`/context`, then `/compact` or `/clear` and say "resume from TASKS.md".

It is a checklist, nothing more — no status header, no dependency fields, no
scripts. `TASKS.md` is git-ignored.

## Rules

- **Resume first.** When the skill starts, look for `TASKS.md` in the module
  directory. If it exists, read it and continue from the **In Progress** card (or
  the first **To Do** card if none is in progress). Do not restart, re-ask
  settled questions, or rewrite files already in **Done** — read them from disk.
- **Create it after discovery.** Once the requirements, protocol and command set
  are confirmed — and before the first file is written or edited — write the
  board. One card per file or step, in build order, ending with a final
  compile/build card. Put any confirmed detail a fresh session would need (the
  command set, the agreed fix list) on the cards themselves.
- **Move cards as you go.** Move a card to **In Progress** when you start it and
  to **Done** the moment it is finished. Write `TASKS.md` on every move so it is
  always current. Keep going to the next card — do not pause for confirmation.
- **Delete it after a clean build.** Delete `TASKS.md` only once the final
  compile/build card exits clean. If the build is blocked or stopped, leave the
  file and add a one-line note to the stuck card saying why.

## Template

```markdown
# TASKS — <Module Name>

## To Do
- runtime.lua — Send/ParseResponse, polling, connection handling
- plugin.lua
- README.md
- compile

## In Progress
- layout.lua — Setup + Control pages

## Done
- info.lua
- properties.lua
- controls.lua — Power, Input1..4, Volume, Mute
```
