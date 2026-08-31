# Extron helper scripts

## `extron_check.py` — ControlScript device-module static checker

Extron ControlScript has **no CLI compiler** (unlike Crestron SIMPL+), so a
device module can't be "built" to prove it's correct. This script verifies a
module by **static analysis** instead: it encodes the hard rules from
`reference/extron/EXTRON_CONSTRAINTS.md` as AST checks and, when `pyright` is
installed, also type-checks the module against the vendored `extronlib` stubs.
It is the Extron analog of the Crestron compilers — the `Verify` step the
`extron-create` / `extron-revise` skills gate on.

```
python extron_check.py <file.py | directory> [more ...] [options]
```

A **directory** argument checks every `.py` it contains (non-recursive).

### Checks

| Code | Rule (EXTRON_CONSTRAINTS.md) | Severity |
|---|---|---|
| `EX-SYNTAX` | module does not parse | error |
| `EX-SLEEP` | blocking `time.sleep()` — use `extronlib.system.Wait`/`Timer` (#9) | error |
| `EX-CONN` | `Connect(timeout)` result discarded, not checked (#7) | error |
| `EX-RXBUF` | a `ReceiveData` handler doesn't buffer the byte stream (#4/#5) | error |
| `EX-MIX` | one interface bound to `ReceiveData` **and** used with `SendAndWait` (#6) | warning |

The AST checks are pure stdlib and run on any platform with no Extron toolchain.
`EX-CONN` uses a "has args" discriminator so a no-arg module method
(`self.Connect()`) isn't confused with the interface's `Connect(10)`. `EX-MIX` is
a warning because two *different* interfaces can legitimately use each model.

### Options

| Option | Description |
|---|---|
| `--stubs=PATH` | extronlib stubs for pyright's path (default `reference/extron/extronlib/1.8.21xi`; use `.../3.13.39` for a `Pro`-generation module) |
| `--no-pyright` | Skip the optional pyright pass; run AST checks only |
| `--warnings-as-errors` | Treat warnings (e.g. `EX-MIX`) as failures too |

```bash
python extron_check.py src/modules/device/MyDisplay.py
python extron_check.py src/modules/device --no-pyright
```

Exit code is `0` when no error-severity diagnostic is found (non-zero otherwise),
so a skill can gate on it. Each finding prints as
`<path>: ERROR <code> (Line <n>) - <message>`, followed by `[OK]` / `[FAILED]`
per module.

### Tests

```
python -m pytest scripts/extron/tests/ -q
```

Tests run each check against good and deliberately-broken module fixtures; they
need no Extron toolchain and no external type checker.
