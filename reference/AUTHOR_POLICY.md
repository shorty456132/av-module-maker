# Author Attribution Policy

Applies to every module-maker skill. Governs any author, programmer, company, or
copyright field written into a **generated** module — Q-SYS `.qplug`, SIMPL+ `.usp`,
SIMPL# `.clz` / `.cpz`. It does not govern this repo's own manifests.

## 1. Never infer an author

Do **not** populate an author field from ambient identity. Specifically, never read:

- `git config user.name` / `user.email`, or commit history
- the session user's name or email address
- `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json` or `marketplace.json`
- the `LICENSE` copyright line
- directory names, existing sibling projects, or any other incidental source

The person running this tool is not necessarily the author of the module it produces,
and their identity is not yours to attach to generated artifacts.

## 2. Ask only when the field is unpopulated

If the target format has an author field and it is absent or still a placeholder, ask
with `AskUserQuestion` before writing it. Treat these as unpopulated: an empty string,
`Author Name`, `Your Name`, `MyCompany`, `TODO`.

Offer these options:

- **Unspecified** *(recommended default)* — write the literal `Unspecified`. No identity
  is attached.
- **Enter a name** — the user types the person or company to credit.

Ask once per run, not once per file. Apply the same answer to every author surface in
that module.

## 3. If it is already populated, leave it alone

Revise and compile skills must not overwrite, "correct", or re-ask about an existing
author value. An existing name is the user's deliberate choice, even when it looks
unusual. Only an absent or placeholder value triggers the ask in §2.

## 4. Store nothing

The answer is scoped to the current run. Do **not** write it to any file under the
plugin root, `~/.claude/`, a settings or defaults file, or a memory entry. There is no
remembered author — a later run asks again.

## 5. Do not invent new author surfaces

Where a format has no author field today, do not add one. In particular:

- SIMPL+ `.usp` — the required directives are `#DEFAULT_VOLATILE`,
  `#ENABLE_STACK_CHECKING`, `#ENABLE_TRACE`. Do not add a `Programmer:` /
  `Written by:` header comment.
- SIMPL# `.csproj` — the template carries `TargetFramework`, `DebugType`, and the
  Crestron `PackageReference`. Do not add `<Authors>`, `<Company>`, or `<Copyright>`.
- Namespaces — keep the `MyCompany.*` placeholder unless the user supplies a real one.

If the user explicitly asks for a byline in one of these, add it with the name they
give. Otherwise leave the surface absent.
