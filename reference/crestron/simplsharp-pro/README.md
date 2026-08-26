# SIMPL# Pro Reference

SIMPL# Pro targets full C# / .NET programs compiled to `.cpz` for 4-Series
appliances and VC-4 — standalone, with a `CrestronControlSystem` entry class and
no SIMPL Windows.

- **Which target is this?** → [`../SIMPLSHARP_OVERVIEW.md`](../SIMPLSHARP_OVERVIEW.md)
  (SIMPL# vs SIMPL# Pro; when to use which).
- **API / SDK reference** (the `Crestron.SimplSharp*` .NET docs) is **not** stored
  here. It lives at the shared corpus — see
  [`../SIMPLSHARP_API_CORPUS.md`](../SIMPLSHARP_API_CORPUS.md) for the path and how
  to search it (via the `crestron-lookup` sub-agent — do not bulk-load).

Target-specific rules and skeletons land in this folder as
`SIMPLSHARP_PRO_CONSTRAINTS.md` and `SIMPLSHARP_PRO_PATTERNS.md`. Each
corpus-derived doc keeps a `> Source:` header line, following the Q-SYS convention.
