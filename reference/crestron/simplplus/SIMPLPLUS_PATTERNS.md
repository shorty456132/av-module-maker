# SIMPL+ Patterns (WIP)

> Scope: **SIMPL+ only** (`.usp`). Mirrors the role of
> `reference/qsys/QSYS_PATTERNS.md`: ready-to-adapt code patterns for the most
> common needs, so most work needs no doc search. Read alongside
> `SIMPLPLUS_CONSTRAINTS.md` — every pattern here must obey those rules
> (directive order, digital→analog→serial I/O order, `_SKIP_` padding, CRLF).
>
> Sibling targets: SIMPL# → `../simplsharp/SIMPLSHARP_PATTERNS.md`,
> SIMPL# Pro → `../simplsharp-pro/SIMPLSHARP_PRO_PATTERNS.md`.

## Planned pattern coverage
- Module skeleton: directives, I/O declared in type order, matching feedback outputs.
- `CHANGE`, `PUSH`, `RELEASE`, `EVENT` handlers.
- `#BEGIN_PARAMETER_PROPERTIES` blocks with correctly ordered property lines.
- Serial/TCP comms via `SOCKET` and buffer parsing with `GATHER` / `FIND`.
- `WAIT` / retry timers and debounce.

_Add confirmed patterns here, each with a `> Source:` link to the SIMPL+ help doc
in `documents/` it derives from. Keep this file SIMPL+-only._
