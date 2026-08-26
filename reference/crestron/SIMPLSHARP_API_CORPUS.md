# SIMPL# / SIMPL# Pro API Corpus — Where the `.NET` reference lives

> Scope: the single source of truth for the **`Crestron.SimplSharp*` .NET API
> reference** that both C# targets compile against. Read this before answering any
> API question for a `simplsharp-*` or `simplsharp-pro-*` skill. It tells you
> **where** the corpus is and **how** to search it — it does not reproduce it.
>
> Sibling reference: [`SIMPLSHARP_OVERVIEW.md`](SIMPLSHARP_OVERVIEW.md) decides
> *which target* a job is; this file is *where the API docs are* for either one.

## The corpus is external and reference-only

The API reference is a flat markdown export of Crestron's *"Simpl# and Simpl# Pro
Help"* site. It is **not** copied, vendored, or submoduled into this repo — it is
read in place from an absolute path on disk:

```
C:\Users\alaia\Documents\AI\claude\claude-skills\Implement Projects\Crestron\SimplSharp-helpDocs
```

- **1,499 files**, one API member per file, flat (no subdirectories).
- Namespaces: `Crestron.SimplSharp*` — skewed toward `Crestron.SimplSharpPro*`
  (device support, sigs, control-system classes). Core types such as
  `SimplSharpString` live in the base `Crestron.SimplSharp` namespace.
- **Shared by both targets.** SIMPL# (`.clz`) and SIMPL# Pro (`.cpz`) draw from
  this one reference; there is no separate corpus per target.

## Corpus shape — file naming

Each file is `<MemberName>-<Kind>.md`. The `<Kind>` suffix tells you what the
file documents:

| Suffix | What it is | Count |
|---|---|---|
| `-Property.md` / `-Properties.md` | a single property / a class's property list | ~479 |
| `-Class.md` | a class overview (summary, syntax, members) | ~350 |
| `-Field.md` / `-Fields.md` | a field / a class's field list | ~197 |
| `-Enumeration.md` | an enum and its values | ~138 |
| `-Method.md` / `-Methods.md` | a method / a class's method list | ~164 |
| `-Interface.md` | an interface | ~67 |
| `-Delegate.md` | a delegate signature (callback types) | ~42 |
| `-Event.md` / `-Events.md` | an event / a class's event list | ~38 |
| `-Constructor.md` | a constructor | ~7 |
| `-Namespace.md` | a namespace overview | ~3 |

Generic types spell the type parameter into the filename rather than using
`<T>` (e.g. `UShortInputSigTClass.md`, `DeviceGroupTClass.md`).

## How to search it — use `crestron-lookup`, don't bulk-load

**Never bulk-load or `cat` the corpus** — 1,499 files will bury the context. Route
every API question through the installed **`crestron-lookup`** sub-agent, which
searches these files and returns just the relevant member docs.

- To confirm a class/method/property exists and get its real signature, ask
  `crestron-lookup` for the member by name (e.g. *"CrestronControlSystem class"*,
  *"TcpClient SendData method"*).
- **Never invent a signature.** If `crestron-lookup` cannot find it, it does not
  exist in this corpus — say so rather than guessing.
- When a constraint or pattern doc cites a corpus-derived fact, carry a
  `> Source:` line to the member (file name or the Crestron help URL), matching
  the Q-SYS `> Source:` convention used across `reference/`.

## Consumers of this pointer

- Skills: `simplsharp-create`, `simplsharp-revise`, `simplsharp-pro-create`,
  `simplsharp-pro-revise` — their "For API questions" line routes here.
- READMEs: [`simplsharp/README.md`](simplsharp/README.md),
  [`simplsharp-pro/README.md`](simplsharp-pro/README.md) point here as the shared
  corpus.
- Docs to come: `simplsharp/SIMPLSHARP_CONSTRAINTS.md` + `_PATTERNS.md` (Slice 3)
  and `simplsharp-pro/SIMPLSHARP_PRO_CONSTRAINTS.md` + `_PATTERNS.md` (Slice 4)
  source-trace their rules and signatures back through this corpus.
