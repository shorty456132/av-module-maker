# Lua 5.3 Reference Manual - Modules

> Source: https://help.qsys.com/Content/Control_Scripting/Lua_5.3_Reference_Manual/Standard_Libraries/2_-_Modules.htm

# Lua 5.3 Reference Manual

by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes

Copyright Â© 2015â2018 Lua.org, PUC-Rio. Freely available under the terms of the [Lua license](http://www.lua.org/license.html).

[contents](../Contents-Index.htm#contents)
Â·
[index](../Contents-Index.htm#index)

## Modules

The package library provides basic
facilities for loading modules in Lua.
It exports one function directly in the global environment:
[`require`](#pdf-require).
Everything else is exported in a table `package`.

---

### `require (modname)`

Loads the given module.
The function starts by looking into the [`package.loaded`](#pdf-package.loaded) table
to determine whether `modname` is already loaded.
If it is, then `require` returns the value stored
at `package.loaded[modname]`.
Otherwise, it tries to find a *loader* for the module.

To find a loader,
`require` is guided by the [`package.searchers`](#pdf-package.searchers) sequence.
By changing this sequence,
we can change how `require` looks for a module.
The following explanation is based on the default configuration
for [`package.searchers`](#pdf-package.searchers).

First `require` queries `package.preload[modname]`.
If it has a value,
this value (which must be a function) is the loader.
Otherwise `require` searches for a Lua loader using the
path stored in [`package.path`](#pdf-package.path).
If that also fails,
it tries an *all-in-one* loader (see [`package.searchers`](#pdf-package.searchers)).

Once a loader is found,
`require` calls the loader with two arguments:
`modname` and an extra value dependent on how it got the loader.
(If the loader came from a file,
this extra value is the file name.)
If the loader returns any non-nil value,
`require` assigns the returned value to `package.loaded[modname]`.
If the loader does not return a non-nil value and
has not assigned any value to `package.loaded[modname]`,
then `require` assigns **true** to this entry.
In any case, `require` returns the
final value of `package.loaded[modname]`.

If there is any error loading or running the module,
or if it cannot find any loader for the module,
then `require` raises an error.

---

### `package.loaded`

A table used by [`require`](#pdf-require) to control which
modules are already loaded.
When you require a module `modname` and
`package.loaded[modname]` is not false,
[`require`](#pdf-require) simply returns the value stored there.

This variable is only a reference to the real table;
assignments to this variable do not change the
table used by [`require`](#pdf-require).

---

### `package.path`

The path used by [`require`](#pdf-require) to search for a Lua loader.

At start-up, Lua initializes this variable with
the value of the environment variable `LUA_PATH_5_3` or
the environment variable `LUA_PATH`,
if those environment variables are not defined.
Any "`;;`" in the value of the environment variable
is replaced by the default path.

---

### `package.preload`

A table to store loaders for specific modules
(see [`require`](#pdf-require)).

This variable is only a reference to the real table;
assignments to this variable do not change the
table used by [`require`](#pdf-require).

---

### `package.searchers`

A table used by [`require`](#pdf-require) to control how to load modules.

Each entry in this table is a *searcher function*.
When looking for a module,
[`require`](#pdf-require) calls each of these searchers in ascending order,
with the module name (the argument given to [`require`](#pdf-require)) as its
sole parameter.
The function can return another function (the module *loader*)
plus an extra value that will be passed to that loader,
or a string explaining why it did not find that module
(or **nil** if it has nothing to say).

Lua initializes this table with four searcher functions.

The first searcher simply looks for a loader in the
[`package.preload`](#pdf-package.preload) table.

The second searcher looks for a loader as a Lua library,
using the path stored at [`package.path`](#pdf-package.path).
The search is done as described in function [`package.searchpath`](#pdf-package.searchpath).

All searchers except the first one (preload) return as the extra value
the file name where the module was found,
as returned by [`package.searchpath`](#pdf-package.searchpath).
The first searcher returns no extra value.

---

### `package.searchpath (name, path [, sep [, rep]])`

Searches for the given `name` in the given `path`.

A path is a string containing a sequence of
*templates* separated by semicolons.
For each template,
the function replaces each interrogation mark (if any)
in the template with a copy of `name`
wherein all occurrences of `sep`
(a dot, by default)
were replaced by `rep`
(the system's directory separator, by default),
and then tries to open the resulting file name.

For instance, if the path is the string

```lua
     "./?.lua;./?.lc;/usr/local/?/init.lua"
		
```

the search for the name `foo.a`
will try to open the files
`./foo/a.lua`, `./foo/a.lc`, and
`/usr/local/foo/a/init.lua`, in that order.

Returns the resulting name of the first file that it can
open in read mode (after closing the file),
or **nil** plus an error message if none succeeds.
(This error message lists all file names it tried to open.)
