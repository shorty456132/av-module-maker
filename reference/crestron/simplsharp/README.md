# SIMPL# Reference

SIMPL# targets C# / .NET class libraries compiled to `.clz` and loaded by SIMPL
Windows as custom modules (via a SIMPL+ `.usp` wrapper).

- **Which target is this?** → [`../SIMPLSHARP_OVERVIEW.md`](../SIMPLSHARP_OVERVIEW.md)
  (SIMPL# vs SIMPL# Pro; the `.clz` + `.usp` wrapper deliverable).
- **API reference** (the `Crestron.SimplSharp*` .NET docs) is **not** stored here.
  It lives at the shared corpus — see
  [`../SIMPLSHARP_API_CORPUS.md`](../SIMPLSHARP_API_CORPUS.md) for the path and
  how to search it (via the `crestron-lookup` sub-agent — do not bulk-load).

Target-specific rules and skeletons land in this folder as
`SIMPLSHARP_CONSTRAINTS.md` and `SIMPLSHARP_PATTERNS.md`. Each corpus-derived doc
keeps a `> Source:` header line, following the Q-SYS convention.
