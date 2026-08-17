# Lua 5.3 Reference Manual - Incompatibilities with the Previous Version

> Source: https://help.qsys.com/Content/Control_Scripting/Lua_5.3_Reference_Manual/8_-_Incompatibilities_with_the_Previous_Version.htm

# Lua 5.3 Reference Manual

by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes

Copyright Â© 2015â2018 Lua.org, PUC-Rio. Freely available under the terms of the [Lua license](http://www.lua.org/license.html).

[contents](Contents-Index.htm#contents)
Â·
[index](Contents-Index.htm#index)

# Incompatibilities with the Previous Version

***QSC Note:* We have compiled the Lua 5.3 environment (contained in the Q-SYS 5.3 and higher releases) with Lua 5.2 compatibility enabled (FYI, Lua v5.2 was used in Q-SYS versions v4.0 - v5.2). Therefore, any previous Lua scripts written in the Q-SYS Script v2 environments should continue to function under Lua 5.3. However, newly written scripts should use the latest Lua 5.3 methods and libraries to avoid any future incompatibilities.
Pay special attention to language in this section related to syntax and methods being 'depreciated.' In Q-Sys 5.3 and above, depreciated Lua 5.2 functions will continue to work, but may not be able to function if we later upgrade to a newer version of Lua.**

Here we list the incompatibilities that you may find when moving a program
from Lua 5.2 to Lua 5.3.
You can avoid some incompatibilities by compiling Lua with
appropriate options (see file `luaconf.h`).
However,
all these compatibility options will be removed in the future.

Lua versions can always change the C API in ways that
do not imply source-code changes in a program,
such as the numeric values for constants
or the implementation of functions as macros.
Therefore,
you should not assume that binaries are compatible between
different Lua versions.
Always recompile clients of the Lua API when
using a new version.

Similarly, Lua versions can always change the internal representation
of precompiled chunks;
precompiled chunks are not compatible between different Lua versions.

The standard paths in the official distribution may
change between versions.

## 1 â Changes in the Language

* The main difference between Lua 5.2 and Lua 5.3 is the
  introduction of an integer subtype for numbers.
  Although this change should not affect "normal" computations,
  some computations
  (mainly those that involve some kind of overflow)
  can give different results.

  You can fix these differences by forcing a number to be a float
  (in Lua 5.2 all numbers were float),
  in particular writing constants with an ending `.0`
  or using `x = x + 0.0` to convert a variable.
  (This recommendation is only for a quick fix
  for an occasional incompatibility;
  it is not a general guideline for good programming.
  For good programming,
  use floats where you need floats
  and integers where you need integers.)
* The conversion of a float to a string now adds a `.0` suffix
  to the result if it looks like an integer.
  (For instance, the float 2.0 will be printed as `2.0`,
  not as `2`.)
  You should always use an explicit format
  when you need a specific format for numbers.

  (Formally this is not an incompatibility,
  because Lua does not specify how numbers are formatted as strings,
  but some programs assumed a specific format.)
* The generational mode for the garbage collector was removed.
  (It was an experimental feature in Lua 5.2.)

## 2 â Changes in the Libraries

* The `bit32` library has been deprecated.
  It is easy to require a compatible external library or,
  better yet, to replace its functions with appropriate bitwise operations.
  (Keep in mind that `bit32` operates on 32-bit integers,
  while the bitwise operators in Lua 5.3 operate on Lua integers,
  which by default have 64 bits.)
* The Table library now respects metamethods
  for setting and getting elements.
* The [`ipairs`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-ipairs) iterator now respects metamethods and
  its `__ipairs` metamethod has been deprecated.
* The following functions were deprecated in the mathematical library:
  `atan2`, `cosh`, `sinh`, `tanh`, `pow`,
  `frexp`, and `ldexp`.
  You can replace `math.pow(x,y)` with `x^y`;
  you can replace `math.atan2` with `math.atan`,
  which now accepts one or two arguments;
  you can replace `math.ldexp(x,exp)` with `x * 2.0^exp`.
  For the other operations,
  you can either use an external library or
  implement them in Lua.
* The searcher for C loaders used by [`require`](Standard_Libraries/2_-_Modules.htm#pdf-require)
  changed the way it handles versioned names.
  Now, the version should come after the module name
  (as is usual in most other tools).
  For compatibility, that searcher still tries the old format
  if it cannot find an open function according to the new style.
  (Lua 5.2 already worked that way,
  but it did not document the change.)
* The call `collectgarbage("count")` now returns only one result.
  (You can compute that second result from the fractional part
  of the first result.)
