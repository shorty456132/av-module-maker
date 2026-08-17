# LPeg

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/LPeg.htm

# LPeg

LPeg is a pattern-matching library for Lua, based on Parsing Expression Grammars (PEGs). LPeg defines patterns as first-class objects; patterns are regular Lua values (represented by userdata). This topic is useful for several functions in creating and compose patterns.

[Usage](javascript:void(0))

To use LPeg, add the following line to your script:

`lualpeg = require("lpeg")`

**Note:** LPeg also offers the `re` module, which implements patterns following a regular-expression style (e.g., `[09]`+). (This module is 260 lines of Lua code, and of course it uses LPeg to parse regular expressions and translate them to regular LPeg patterns.)

[Import LPeg Module](javascript:void(0))

```lua
-- imported functions and modules  
local tonumber, type, print, error = tonumber, type, print, error  
local setmetatable = setmetatable  
local m = require"lpeg"
```

[Basic Constructions](javascript:void(0))

The following operations build patterns. All operations that expect a pattern as an argument may receive also strings, tables, numbers, booleans, or functions, which are translated to patterns according these rules:

* If the argument is a pattern, it is returned unmodified.
* If the argument is a string, it is translated to a pattern that matches the string literally.
* If the argument is a non-negative number n, the result is a pattern that matches exactly n characters.
* If the argument is a negative number -n, the result is a pattern that succeeds only if the input string has less than n characters left: lpeg.P(-n) is equivalent to -lpeg.P(n) (see the unary minus operation).
* If the argument is a boolean, the result is a pattern that always succeeds or always fails (according to the boolean value), without consuming any input.
* If the argument is a table, it is interpreted as a grammar (see Grammars).
* If the argument is a function, returns a pattern equivalent to a match-time capture over the empty string.

[function lpeg.match()](javascript:void(0))

This matching function attempts to match the given pattern against the subject string.

### Syntax

### Arguments

*pattern*: Will find a pattern anywhere in a string.

*subject*: Attempts to match the pattern with a prefix of the given subject string (at position `init`), not with an arbitrary substring of the subject.

*init*: (Optional) A numeric argument that makes the match start at that position in the subject string.

### Returns

Returns the index in the subject of the first character after the match, or the captured values (if the pattern captured any value).

### Example

```lua
local lpeg = require "lpeg"  
  
-- matches a word followed by end-of-string  
p = lpeg.R"az"^1 * -1  
  
print(p:match("hello"))        --> 6  
print(lpeg.match(p, "hello"))  --> 6  
print(p:match("1 hello"))      --> nil
```

[function lpeg.type()](javascript:void(0))

This matching function returns the string pattern.

### Syntax

value = function lpeg.type(*value*)

### Arguments

*value*: Will return the string `pattern`.

### Returns

Returns the string `pattern` if successful.

Returns nil if unsuccessful.

[function lpeg.version()](javascript:void(0))

This matching function returns a string with the running version of LPeg.

### Syntax

value = function lpeg.version

Returns the string with the running version of LPEG.

Returns nil if unsuccessful.

[function lpeg.P()](javascript:void(0))

This coverts the given value into a proper pattern.

### Syntax

value = function lpeg.P(`string`, `n`)

### Arguments

`string`: Matches `string` literally

`n`: Matches exactly `n` characters

### Returns

* If the argument is a pattern, it is returned unmodified.
* If the argument is a string, it is translated to a pattern that matches the string literally.
* If the argument is a non-negative number n, the result is a pattern that matches exactly n characters.
* If the argument is a negative number -n, the result is a pattern that succeeds only if the input string has less than n characters left: lpeg.P(-n) is equivalent to -lpeg.P(n) (see the unary minus operation).
* If the argument is a boolean, the result is a pattern that always succeeds or always fails (according to the boolean value), without consuming any input.
* If the argument is a table, it is interpreted as a grammar (see Grammars).
* If the argument is a function, returns a pattern equivalent to a match-time capture over the empty string.

[function lpeg.B()](javascript:void(0))

This function returns a pattern that matches the input string.

### Syntax

value = function lpeg.B(`patt`, `#patt`, `-patt`, `patt1 + patt2`, `patt1 - patt2`, `patt1 * patt2`, `patt^n`)

### Arguments

`patt`: Matches `patt` behind the current position, consuming no input.

`#patt`: Matches `patt` but consumes no input.

`-patt`: Returns a pattern that matches only if the input string does not match `patt`. Equivalent to `("" - patt)`.

`patt1 + patt2`: Returns a pattern equivalent to an `ordered choice` of `patt1` and `patt2`.

`patt1 - patt2`: Returns a pattern equivalent to *!patt2 patt1*. Matches `patt1` if `patt2` does not match

`patt1 * patt2`: Returns a pattern that matches `patt1` and then matches `patt2`, starting where `patt1` finished.

`patt^n`: Matches at least `n` repetitions of `patt`.

`patt^-n`: Matches at most `n` repetitions of `patt`.

### Returns

Returns pattern if successful.

Returns nil if unsuccessful.

[function lpeg.R()](javascript:void(0))

This function returns a pattern that matches any single character belonging to one of the given ranges.

### Syntax

value = function lpeg.R({range})

### Arguments

`"xy"`: Matches any character between `x` and `y` (Range).

### Returns

Returns pattern if successful.

Returns nil if unsuccessful.

### Example

In this example, the pattern `lpeg.R("az", "AZ")` matches any ASCII letter

```lua
lower = lpeg.R("az")  
upper = lpeg.R("AZ")  
letter = lower + upper
```

[function lpeg.S()](javascript:void(0))

This function returns a pattern that matches any single character that appears in the given string.

### Syntax

value = function lpeg.S(string)

### Arguments

`string`: Returns a pattern that matches any single character that appears in the given `string`

### Returns

Returns pattern if successful.

Returns nil if unsuccessful.

### Example

In this example, the pattern`lpeg.S("+-*/")` matches any arithmetic operator.

```lua
lpeg.S("+-*/")
```

[function lpeg.V()](javascript:void(0))

This function creates a non-terminal (a `variable`) for a grammar.

### Syntax

value = function lpeg.V(v)

### Arguments

`v`: The created non-terminal refers to the rule indexed by `v` in the enclosing grammar. Because the grammar still does not exist when this function is evaluated, the result is an `open reference` to the respective rule. A table is *fixed* when it is converted to a pattern (either by calling `lpeg.P` or by using it wherein a pattern is expected). Then every open reference created by `lpeg.V(v)` is corrected to refer to the rule indexed by `v` in the table.

### Returns

Returns pattern if successful.

Returns nil if unsuccessful.

### Example

In this example, the following grammar matches strings of a's and b's that have the same number of a's and b's.

```lua
equalcount = lpeg.P{  
  "S";   -- initial rule name  
  S = "a" * lpeg.V"B" + "b" * lpeg.V"A" + "",  
  A = "a" * lpeg.V"S" + "b" * lpeg.V"A" * lpeg.V"A",  
  B = "b" * lpeg.V"S" + "a" * lpeg.V"B" * lpeg.V"B",  
} * -1
```

It is equivalent to the following grammar in standard PEG notation.

```lua
  S <- 'a' B / 'b' A / ''  
  A <- 'a' S / 'b' A A  
  B <- 'b' S / 'a' B B
```

[function lpeg.locale()](javascript:void(0))

This function returns a table with patterns for matching some character classes according to the current locale.

### Syntax

value = function lpeg.local([table])

### Arguments

`table`: Returns a table with patterns for matching some character classes according to the current locale.

### Returns

Returns table if successful. The table has fields named `alnum`, `alpha`, `cntrl`, `digit`, `graph`, `lower`, `print`, `punct`, `space`, `upper`, and `xdigit`, each one containing a correspondent pattern. Each pattern matches any single character that belongs to its class.

Returns nil if unsuccessful.

[Captures](javascript:void(0))

A `capture` is a pattern that produces values according to what it matches. LPeg offers several kinds of captures, which produces values based on matches and combine these values to produce new values. Each capture may produce zero or more values.

[function lpeg.C()](javascript:void(0))

Creates a *simple capture*, which captures the substring of the subject that matches `patt`. The captured value is a string. If `patt` has other captures, their values are returned after this one.

### Syntax

value = function lpeg.C(*patt*)

### Arguments

*patt*: Produces the match for `patt` plus all captures made by `patt`.

### Returns

Returns capture, which captures the substring of the subject that matches `patt`.

### Example

In this example, we want to split a string using a given pattern `sep` as a separator.

```lua
function split (s, sep)  
  sep = lpeg.P(sep)  
  local elem = lpeg.C((1 - sep)^0)  
  local p = elem * (sep * elem)^0  
  return lpeg.match(p, s)  
end
```

[function lpeg.Carg()](javascript:void(0))

Creates an argument capture. This pattern matches the empty string and produces the value given as the nth extra argument given in the call to `lpeg.match`.

### Syntax

value = function lpeg.Carg(*n*)

### Arguments

*n*: The value of the nth extra argument to `lpeg.match` (matches the empty string).

### Returns

Returns the value of the nth extra argument.

Returns nil if unsuccessful.

[function lpeg.Cb()](javascript:void(0))

Creates a *back capture*. This pattern matches the empty string and produces the values produced by the most recent group capture named `name` (where `name` can be any Lua value).

### Syntax

value = function lpeg.Cb(`name`)

### Arguments

`name`: The values produced by the previous group capture named `name` (matches the empty string).

### Returns

Returns the value produced by the most recent group capture named `name`.

Returns nil if unsuccessful.

[function lpeg.Cc()](javascript:void(0))

Creates a *constant capture*. This pattern matches the empty string and produces all given values as its captured values.

### Syntax

value = function lpeg.Cc(`values`)

### Arguments

`values`: the given values (matches the empty string).

### Returns

Returns all given values if successful.

Returns nil if unsuccesful.

[function lpeg.Cf()](javascript:void(0))

Creates a *fold capture*. This capture assumes that `patt` should produce at least one capture with at least one value (of any type), which becomes the initial value of an *accumulator*.

### Syntax

value = function lpeg.Cf(`patt`, `func`)

### Arguments

`patt`: Produces a list of captures **C1 C2 ... Cn**.

`func`: Produces the value *`func`(...*func(func(C1, C2), C3)..., Cn*)*.

### Returns

Returns a *fold capture* if successful.

Returns nil if unsuccessful.

### Example

In this example, the following pattern matches a list of numbers separated by commas and returns their addition.

```lua
-- matches a numeral and captures its numerical value  
number = lpeg.R"09"^1 / tonumber  
  
-- matches a list of numbers, capturing their values  
list = number * ("," * number)^0  
  
-- auxiliary function to add two numbers  
function add (acc, newvalue) return acc + newvalue end  
  
-- folds the list of numbers adding them  
sum = lpeg.Cf(list, add)  
  
-- example of use  
print(sum:match("10,30,43"))   --> 83
```

[function lpeg.Cg()](javascript:void(0))

Creates a *group capture*. It groups all values returned by `patt` into a single capture.

### Syntax

value = function lpeg.Cg(`patt [, name]`)

### Arguments

`"patt [, name]"`: The values produced by `patt`, optionally tagged with `name`.

### Returns

Groups all values returned by `patt` into a single capture if successful.

Returns nil if unsuccessful.

### Example

In this example, the `lpeg.Cg` parses a list of name-value paris and returns a table with those pairs.

```lua
lpeg.locale(lpeg)   -- adds locale entries into 'lpeg' table  
  
local space = lpeg.space^0  
local name = lpeg.C(lpeg.alpha^1) * space  
local sep = lpeg.S(",;") * space  
local pair = lpeg.Cg(name * "=" * space * name) * sep^-1  
local list = lpeg.Cf(lpeg.Ct("") * pair^0, rawset)  
t = list:match("a=b, c = hi; next = pi")  --> { a = "b", c = "hi", next = "pi" }
```

[function lpeg.Cp()](javascript:void(0))

Creates a *position capture*. It matches the empty string and captures the position in the subject where the match occurs. The captured value is a number.

### Syntax

value = function lpeg.Cp()

### Arguments

`()`: The current position (matches the empty `string`)

### Returns

Returns a number of the position in the subject where the match occurs.

Returns nil if unsuccessful.

### Example

In this example, we want to know where the pattern is in the string.

```lua
local I = lpeg.Cp()  
function anywhere (p)  
  return lpeg.P{ I * p * I + 1 * lpeg.V(1) }  
end  
  
print(anywhere("world"):match("hello world!"))   -> 7   12
```

[function lpeg.Cs()](javascript:void(0))

Creates a *substitution capture*, which captures the substring of the subject that matches `patt`, with *substitutions*.

### Syntax

value = function lpeg.Cs(patt)

### Arguments

`patt`: The match for `patt` with the values from nested captures replacing their matches.

### Returns

For any capture inside `patt` with a value, the substring that matched the capture is replaced by the capture value if successful. The final captured value is the string resulting from all replacements.

Returns nil if unsuccessful.

### Example

In this example, LPeg receives a pattern and a replacement value, and substitutes the replacement value for all occurrences of the pattern in a given string.

```lua
function gsub (s, patt, repl)  
  patt = lpeg.P(patt)  
  patt = lpeg.Cs((patt / repl + 1)^0)  
  return lpeg.match(patt, s)  
end
```

[function lpeg.Ct()](javascript:void(0))

Creates a *table capture*. For each named capture group created by `patt`, the first value of the group is put into the table with the group name as its key. The captured value is only the table.

### Syntax

value = function lpeg.Ct(patt)

### Arguments

`patt`: Returns a table with all captures from `patt`.

### Returns

Returns table if successfulwith all values from all anonymous captures made by `patt` inside this table in successive integer keys, starting at 1.

Returns nil if unsuccessful.

### Example

In this example, a table capture will break a string into comma-separated values, returning all fields.

```lua
local field = '"' * lpeg.Cs(((lpeg.P(1) - '"') + lpeg.P'""' / '"')^0) * '"' +  
                    lpeg.C((1 - lpeg.S',\n"')^0)  
  
local record = lpeg.Ct(field * (',' * field)^0) * (lpeg.P'\n' + -1)  
  
function csv (s)  
  return lpeg.match(record, s)  
end
```

Portions of this topic are reprinted under permission of the [LPeg](../../Legal.htm#LPeg) license.
