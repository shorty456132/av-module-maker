# Lua 5.3 Reference Manual - The Language

> Source: https://help.qsys.com/Content/Control_Scripting/Lua_5.3_Reference_Manual/3_-_The_Language.htm

# Lua 5.3 Reference Manual

by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes

Copyright Â© 2015â2018 Lua.org, PUC-Rio. Freely available under the terms of the [Lua license](http://www.lua.org/license.html).

[contents](Contents-Index.htm#contents)
Â·
[index](Contents-Index.htm#index)

# The Language

This section describes the lexis, the syntax, and the semantics of Lua.
In other words,
this section describes
which tokens are valid,
how they can be combined,
and what their combinations mean.

Language constructs will be explained using the usual extended BNF notation,
in which
{*a*} means 0 or more *a*'s, and
[*a*] means an optional *a*.
Non-terminals are shown like non-terminal,
keywords are shown like **kword**,
and other terminal symbols are shown like '**=**'.
The complete syntax of Lua can be found in [Complete Syntax](9_-_The_Complete_Syntax_of_Lua.htm#Syntax) at the end of this manual.

## 1 â Lexical Conventions

Lua is a free-form language.
It ignores spaces (including new lines) and comments
between lexical elements (tokens),
except as delimiters between names and keywords.

*Names*
(also called *identifiers*)
in Lua can be any string of letters,
digits, and underscores,
not beginning with a digit and
not being a reserved word.
Identifiers are used to name variables, table fields, and labels.

The following *keywords* are reserved
and cannot be used as names:

```lua
     and       break     do        else      elseif    end
			false     for       function  goto      if        in
			local     nil       not       or        repeat    return
			then      true      until     while
		
```

Lua is a case-sensitive language:
`and` is a reserved word, but `And` and `AND`
are two different, valid names.
As a convention,
programs should avoid creating
names that start with an underscore followed by
one or more uppercase letters (such as [`_VERSION`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-_VERSION)).

The following strings denote other tokens:

```lua
     +     -     *     /     %     ^     #
			&     ~     |     <<    >>    //
			==    ~=    <=    >=    <     >     =
			(     )     {     }     [     ]     ::
			;     :     ,     .     ..    ...
		
```

*Literal strings*
can be delimited by matching single or double quotes,
and can contain the following C-like escape sequences:
'`\a`' (bell),
'`\b`' (backspace),
'`\f`' (form feed),
'`\n`' (newline),
'`\r`' (carriage return),
'`\t`' (horizontal tab),
'`\v`' (vertical tab),
'`\\`' (backslash),
'`\"`' (quotation mark [double quote]),
and '`\'`' (apostrophe [single quote]).
A backslash followed by a real newline
results in a newline in the string.
The escape sequence '`\z`' skips the following span
of white-space characters,
including line breaks;
it is particularly useful to break and indent a long literal string
into multiple lines without adding the newlines and spaces
into the string contents.

Strings in Lua can contain any 8-bit value, including embedded zeros,
which can be specified as '`\0`'.
More generally,
we can specify any byte in a literal string by its numeric value.
This can be done
with the escape sequence `\xXX`,
where *XX* is a sequence of exactly two hexadecimal digits,
or with the escape sequence `\ddd`,
where *ddd* is a sequence of up to three decimal digits.
(Note that if a decimal escape sequence is to be followed by a digit,
it must be expressed using exactly three digits.)

The UTF-8 encoding of a Unicode character
can be inserted in a literal string with
the escape sequence `\u{XXX}`
(note the mandatory enclosing brackets),
where *XXX* is a sequence of one or more hexadecimal digits
representing the character code point.

Literal strings can also be defined using a long format
enclosed by *long brackets*.
We define an *opening long bracket of level *n** as an opening
square bracket followed by *n* equal signs followed by another
opening square bracket.
So, an opening long bracket of level 0 is written as `[[`,
an opening long bracket of level 1 is written as `[=[`,
and so on.
A *closing long bracket* is defined similarly;
for instance,
a closing long bracket of level 4 is written as `]====]`.
A *long literal* starts with an opening long bracket of any level and
ends at the first closing long bracket of the same level.
It can contain any text except a closing bracket of the same level.
Literals in this bracketed form can run for several lines,
do not interpret any escape sequences,
and ignore long brackets of any other level.
Any kind of end-of-line sequence
(carriage return, newline, carriage return followed by newline,
or newline followed by carriage return)
is converted to a simple newline.

Any byte in a literal string not
explicitly affected by the previous rules represents itself.
However, Lua opens files for parsing in text mode,
and the system file functions may have problems with
some control characters.
So, it is safer to represent
non-text data as a quoted literal with
explicit escape sequences for non-text characters.

For convenience,
when the opening long bracket is immediately followed by a newline,
the newline is not included in the string.
As an example, in a system using ASCII
(in which '`a`' is coded as 97,
newline is coded as 10, and '`1`' is coded as 49),
the five literal strings below denote the same string:

```lua
     a = 'alo\n123"'
			a = "alo\n123\""
			a = '\97lo\10\04923"'
			a = [[alo
			123"]]
			a = [==[
			alo
			123"]==]
		
```

A *numeric constant* (or *numeral*)
can be written with an optional fractional part
and an optional decimal exponent,
marked by a letter '`e`' or '`E`'.
Lua also accepts hexadecimal constants,
which start with `0x` or `0X`.
Hexadecimal constants also accept an optional fractional part
plus an optional binary exponent,
marked by a letter '`p`' or '`P`'.
A numeric constant with a fractional dot or an exponent
denotes a float;
otherwise it denotes an integer.
Examples of valid integer constants are

```lua
     3   345   0xff   0xBEBADA
		
```

Examples of valid float constants are

```lua
     3.0     3.1416     314.16e-2     0.31416E1     34e1
			0x0.1E  0xA23p-4   0X1.921FB54442D18P+1
		
```

A *comment* starts with a double hyphen (`--`)
anywhere outside a string.
If the text immediately after `--` is not an opening long bracket,
the comment is a *short comment*,
which runs until the end of the line.
Otherwise, it is a *long comment*,
which runs until the corresponding closing long bracket.
Long comments are frequently used to disable code temporarily.

## 2 â Variables

Variables are places that store values.
There are three kinds of variables in Lua:
global variables, local variables, and table fields.

A single name can denote a global variable or a local variable
(or a function's formal parameter,
which is a particular kind of local variable):

```lua
	var ::= Name
		
```

Name denotes identifiers, as defined in [Lexical Conventions](#1).

Any variable name is assumed to be global unless explicitly declared
as a local (see [Local Declarations](#3.7)).
Local variables are *lexically scoped*:
local variables can be freely accessed by functions
defined inside their scope (see [Visibility Rules](#5)).

Before the first assignment to a variable, its value is **nil**.

Square brackets are used to index a table:

```lua
	var ::= prefixexp '[' exp ']'
		
```

The meaning of accesses to table fields can be changed via metatables (see [Metatables and Metamethods](2_-_Basic_Concepts.htm#4)).

The syntax `var.Name` is just syntactic sugar for
`var["Name"]`:

```lua
	var ::= prefixexp '.' Name
		
```

An access to a global variable `x`
is equivalent to `_ENV.x`.
Due to the way that chunks are compiled,
`_ENV` is never a global name (see [Environments and the Global Environment](2_-_Basic_Concepts.htm#2)).

## 3 â Statements

Lua supports an almost conventional set of statements,
similar to those in Pascal or C.
This set includes
assignments, control structures, function calls,
and variable declarations.

### 3.1 â Blocks

A block is a list of statements,
which are executed sequentially:

```lua
	block ::= {stat}
		
```

Lua has *empty statements*
that allow you to separate statements with semicolons,
start a block with a semicolon
or write two semicolons in sequence:

```lua
	stat ::= ';'
		
```

Function calls and assignments
can start with an open parenthesis.
This possibility leads to an ambiguity in Lua's grammar.
Consider the following fragment:

```lua
     a = b + c
			(print or io.write)('done')
		
```

The grammar could see it in two ways:

```lua
     a = b + c(print or io.write)('done')
     
			a = b + c; (print or io.write)('done')
		
```

The current parser always sees such constructions
in the first way,
interpreting the open parenthesis
as the start of the arguments to a call.
To avoid this ambiguity,
it is a good practice to always precede with a semicolon
statements that start with a parenthesis:

```lua
     ;(print or io.write)('done')
		
```

A block can be explicitly delimited to produce a single statement:

```lua
	stat ::= do block end
		
```

Explicit blocks are useful
to control the scope of variable declarations.
Explicit blocks are also sometimes used to
add a **return** statement in the middle
of another block (see [Control Structures](#3.4)).

### 3.2 â Chunks

The unit of compilation of Lua is called a *chunk*.
Syntactically,
a chunk is simply a block:

```lua
	chunk ::= block
		
```

Lua handles a chunk as the body of an anonymous function
with a variable number of arguments
(see [Function Definitions](#4.11)).
As such, chunks can define local variables,
receive arguments, and return values.
Moreover, such anonymous function is compiled as in the
scope of an external local variable called `_ENV` (see [Environments and the Global Environment](2_-_Basic_Concepts.htm#2)).
The resulting function always has `_ENV` as its only upvalue,
even if it does not use that variable.

A chunk can be stored in a file or in a string inside the host program.
To execute a chunk,
Lua first *loads* it,
precompiling the chunk's code into instructions for a virtual machine,
and then Lua executes the compiled code
with an interpreter for the virtual machine.

Chunks can also be precompiled into binary form;
see program `luac` and function [`string.dump`](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.dump) for details.
Programs in source and compiled forms are interchangeable;
Lua automatically detects the file type and acts accordingly (see [`load`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-load)).

### 3.3 â Assignment

Lua allows multiple assignments.
Therefore, the syntax for assignment
defines a list of variables on the left side
and a list of expressions on the right side.
The elements in both lists are separated by commas:

```lua
	stat ::= varlist '=' explist
			varlist ::= var {',' var}
			explist ::= exp {',' exp}
		
```

Expressions are discussed in [Expressions](#4).

Before the assignment,
the list of values is *adjusted* to the length of
the list of variables.
If there are more values than needed,
the excess values are thrown away.
If there are fewer values than needed,
the list is extended with as many **nil**'s as needed.
If the list of expressions ends with a function call,
then all values returned by that call enter the list of values,
before the adjustment
(except when the call is enclosed in parentheses; see [Expressions](#4)).

The assignment statement first evaluates all its expressions
and only then the assignments are performed.
Thus the code

```lua
     i = 3
			i, a[i] = i+1, 20
		
```

sets `a[3]` to 20, without affecting `a[4]`
because the `i` in `a[i]` is evaluated (to 3)
before it is assigned 4.
Similarly, the line

```lua
     x, y = y, x
		
```

exchanges the values of `x` and `y`,
and

```lua
     x, y, z = y, z, x
		
```

cyclically permutes the values of `x`, `y`, and `z`.

The meaning of assignments to table fields and global variables (which are actually table fields, too) can be changed via metatables (see [Metatables and Metamethods](2_-_Basic_Concepts.htm#4)).

An assignment to a global name `x = val`
is equivalent to the assignment
`_ENV.x = val` (see [Environments and the Global Environment](2_-_Basic_Concepts.htm#2)).

### 3.4 â Control Structures

The control structures
**if**, **while**, and **repeat** have the usual meaning and
familiar syntax:

```lua
	stat ::= while exp do block end
			stat ::= repeat block until exp
			stat ::= if exp then block {elseif exp then block} [else block] end
		
```

Lua also has a **for** statement, in two flavors (see [For Statement](#3.5)).

The condition expression of a
control structure can return any value.
Both **false** and **nil** are considered false.
All values different from **nil** and **false** are considered true
(in particular, the number 0 and the empty string are also true).

In the **repeat**â**until** loop,
the inner block does not end at the **until** keyword,
but only after the condition.
So, the condition can refer to local variables
declared inside the loop block.

The **goto** statement transfers the program control to a label.
For syntactical reasons,
labels in Lua are considered statements too:

```lua
	stat ::= goto Name
			stat ::= label
			label ::= '::' Name '::'
		
```

A label is visible in the entire block where it is defined,
except
inside nested blocks where a label with the same name is defined and
inside nested functions.
A goto may jump to any visible label as long as it does not
enter into the scope of a local variable.

Labels and empty statements are called *void statements*,
as they perform no actions.

The **break** statement terminates the execution of a
**while**, **repeat**, or **for** loop,
skipping to the next statement after the loop:

```lua
	stat ::= break
		
```

A **break** ends the innermost enclosing loop.

The **return** statement is used to return values
from a function or a chunk
(which is an anonymous function).
Functions can return more than one value,
so the syntax for the **return** statement is

```lua
	stat ::= return [explist] [';']
		
```

The **return** statement can only be written
as the last statement of a block.
If it is really necessary to **return** in the middle of a block,
then an explicit inner block can be used,
as in the idiom `do return end`,
because now **return** is the last statement in its (inner) block.

### 3.5 â For Statement

The **for** statement has two forms:
one numerical and one generic.

The numerical **for** loop repeats a block of code while a
control variable runs through an arithmetic progression.
It has the following syntax:

```lua
	stat ::= for Name '=' exp ',' exp [',' exp] do block end
		
```

The *block* is repeated for *name* starting at the value of
the first *exp*, until it passes the second *exp* by steps of the
third *exp*.
More precisely, a **for** statement like

```lua
     for v = e1, e2, e3 do block end
		
```

is equivalent to the code:

```lua
     do
			local var, limit, step = tonumber(e1), tonumber(e2), tonumber(e3)
			if not (var and limit and step) then error() end
			var = var - step
			while true do
			var = var + step
			if (step >= 0 and var > limit) or (step < 0 and var < limit) then
			break
			end
			local v = var
			block
			end
			end
		
```

Note the following:

* All three control expressions are evaluated only once,
  before the loop starts.
  They must all result in numbers.
* `var`, `limit`, and `step` are invisible variables.
  The names shown here are for explanatory purposes only.
* If the third expression (the step) is absent,
  then a step of 1 is used.
* You can use **break** and **goto** to exit a **for** loop.
* The loop variable `v` is local to the loop body.
  If you need its value after the loop,
  assign it to another variable before exiting the loop.

The generic **for** statement works over functions,
called *iterators*.
On each iteration, the iterator function is called to produce a new value,
stopping when this new value is **nil**.
The generic **for** loop has the following syntax:

```lua
	stat ::= for namelist in explist do block end
			namelist ::= Name {',' Name}
		
```

A **for** statement like

```lua
     for var_1, Â·Â·Â·, var_n in explist do block end
		
```

is equivalent to the code:

```lua
     do
			local f, s, var = explist
			while true do
			local var_1, Â·Â·Â·, var_n = f(s, var)
			if var_1 == nil then break end
			var = var_1
			block
			end
			end
		
```

Note the following:

* `explist` is evaluated only once.
  Its results are an *iterator* function,
  a *state*,
  and an initial value for the first *iterator variable*.
* `f`, `s`, and `var` are invisible variables.
  The names are here for explanatory purposes only.
* You can use **break** to exit a **for** loop.
* The loop variables `var_i` are local to the loop;
  you cannot use their values after the **for** ends.
  If you need these values,
  then assign them to other variables before breaking or exiting the loop.

### 3.6 â Function Calls as Statements

To allow possible side-effects,
function calls can be executed as statements:

```lua
	stat ::= functioncall
		
```

In this case, all returned values are thrown away.
Function calls are explained in [Function Calls](#4.10).

### 3.7 â Local Declarations

Local variables can be declared anywhere inside a block.
The declaration can include an initial assignment:

```lua
	stat ::= local namelist ['=' explist]
		
```

If present, an initial assignment has the same semantics
of a multiple assignment (see [Assignment](#3.3)).
Otherwise, all variables are initialized with **nil**.

A chunk is also a block (see [Chunks](#3.2)),
and so local variables can be declared in a chunk outside any explicit block.

The visibility rules for local variables are explained in [Visibility Rule](#5).

## 4 â Expressions

The basic expressions in Lua are the following:

```lua
	exp ::= prefixexp
			exp ::= nil | false | true
			exp ::= Numeral
			exp ::= LiteralString
			exp ::= functiondef
			exp ::= tableconstructor
			exp ::= '...'
			exp ::= exp binop exp
			exp ::= unop exp
			prefixexp ::= var | functioncall | '(' exp ')'
		
```

Numerals and literal strings are explained in [Lexical Conventions](#1);
variables are explained [here](#2);
function definitions are explained [here](#4.11);
function calls are explained [here](#4.10);
table constructors are explained [here](#4.9).
Vararg expressions,
denoted by three dots ('`...`'), can only be used when
directly inside a vararg function;
they are explained in [Function Definitions](#4.11).

Binary operators comprise [arithmetic operators](#4.1),
[bitwise operators](#4.2),
[relational operators](#4.4), [logical operators](#4.5),
and the [concatenation operator](#4.6).
Unary operators comprise the unary minus (see [Arithmetic Operators](#4.1)),
the unary bitwise not (see [Bitwise Operators](#4.2)),
the unary logical **not** (see [Logical Operators](#4.5)),
and the unary *[length operator](#4.7)*.

Both function calls and vararg expressions can result in multiple values.
If a [function call is used as a statement](#3.6),
then its return list is adjusted to zero elements,
thus discarding all returned values.
If an expression is used as the last (or the only) element
of a list of expressions,
then no adjustment is made
(unless the expression is enclosed in parentheses).
In all other contexts,
Lua adjusts the result list to one element,
either discarding all values except the first one
or adding a single **nil** if there are no values.

Here are some examples:

```lua
     
			f()                -- adjusted to 0 results
			g(f(), x)          -- f() is adjusted to 1 result
			g(x, f())          -- g gets x plus all results from f()
			a,b,c = f(), x     -- f() is adjusted to 1 result (c gets nil)
			a,b = ...          -- a gets the first vararg argument, b gets the second
					      (both a and b can get nil if there is no corresponding vararg argument)
			a,b,c = x, f()     -- f() is adjusted to 2 results
			a,b,c = f()        -- f() is adjusted to 3 results
			return f()         -- returns all results from f()
			return ...         -- returns all received vararg arguments
			return x,y,f()     -- returns x, y, and all results from f()
			{f()}              -- creates a list with all results from f()
			{...}              -- creates a list with all vararg arguments
			{f(), nil}         -- f() is adjusted to 1 result
		
```

Any expression enclosed in parentheses always results in only one value.
Thus,
`(f(x,y,z))` is always a single value,
even if `f` returns several values.
(The value of `(f(x,y,z))` is the first value returned by `f`
or **nil** if `f` does not return any values.)

### 4.1 â Arithmetic Operators

Lua supports the following arithmetic operators:

* **`+`:** addition
* **`-`:** subtraction
* **`*`:** multiplication
* **`/`:** float division
* **`//`:** floor division
* **`%`:** modulo
* **`^`:** exponentiation
* **`-`:** unary minus

With the exception of exponentiation and float division,
the arithmetic operators work as follows:
If both operands are integers,
the operation is performed over integers and the result is an integer.
Otherwise, if both operands are numbers
or strings that can be converted to
numbers (see [Coercions and Conversions](#4.3)),
then they are converted to floats,
the operation is performed following the usual rules
for floating-point arithmetic
(usually the IEEE 754 standard),
and the result is a float.

Exponentiation and float division (`/`)
always convert their operands to floats
and the result is always a float.
Exponentiation uses the ISO C function `pow`,
so that it works for non-integer exponents too.

Floor division (`//`) is a division
that rounds the quotient towards minus infinity,
that is, the floor of the division of its operands.

Modulo is defined as the remainder of a division
that rounds the quotient towards minus infinity (floor division).

In case of overflows in integer arithmetic,
all operations *wrap around*,
according to the usual rules of two-complement arithmetic.
(In other words,
they return the unique representable integer
that is equal modulo *264* to the mathematical result.)

### 4.2 â Bitwise Operators

Lua supports the following bitwise operators:

* **`&`:** bitwise and
* **`|`:** bitwise or
* **`~`:** bitwise exclusive or
* **`>>`:** right shift
* **`<<`:** left shift
* **`~`:** unary bitwise not

All bitwise operations convert its operands to integers
(see [Coercions and Conversions](#4.3)),
operate on all bits of those integers,
and result in an integer.

Both right and left shifts fill the vacant bits with zeros.
Negative displacements shift to the other direction;
displacements with absolute values equal to or higher than
the number of bits in an integer
result in zero (as all bits are shifted out).

### 4.3 â Coercions and Conversions

Lua provides some automatic conversions between some
types and representations at run time.
Bitwise operators always convert float operands to integers.
Exponentiation and float division
always convert integer operands to floats.
All other arithmetic operations applied to mixed numbers
(integers and floats) convert the integer operand to a float;
this is called the *usual rule*.
The C API also converts both integers to floats and
floats to integers, as needed.
Moreover, string concatenation accepts numbers as arguments,
besides strings.

Lua also converts strings to numbers,
whenever a number is expected.

In a conversion from integer to float,
if the integer value has an exact representation as a float,
that is the result.
Otherwise,
the conversion gets the nearest higher or
the nearest lower representable value.
This kind of conversion never fails.

The conversion from float to integer
checks whether the float has an exact representation as an integer
(that is, the float has an integral value and
it is in the range of integer representation).
If it does, that representation is the result.
Otherwise, the conversion fails.

The conversion from strings to numbers goes as follows:
First, the string is converted to an integer or a float,
following its syntax and the rules of the Lua lexer.
(The string may have also leading and trailing spaces and a sign.)
Then, the resulting number (float or integer)
is converted to the type (float or integer) required by the context
(e.g., the operation that forced the conversion).

The conversion from numbers to strings uses a
non-specified human-readable format.
For complete control over how numbers are converted to strings,
use the `format` function from the string library
(see [`string.format`](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.format)).

### 4.4 â Relational Operators

Lua supports the following relational operators:

* **`==`:** equality
* **`~=`:** inequality
* **`<`:** less than
* **`>`:** greater than
* **`<=`:** less or equal
* **`>=`:** greater or equal

These operators always result in **false** or **true**.

Equality (`==`) first compares the type of its operands.
If the types are different, then the result is **false**.
Otherwise, the values of the operands are compared.
Strings are compared in the obvious way.
Numbers are equal if they denote the same mathematical value.

Tables, userdata, and threads
are compared by reference:
two objects are considered equal only if they are the same object.
Every time you create a new object
(a table, userdata, or thread),
this new object is different from any previously existing object.
A closure is always equal to itself.
Closures with any detectable difference
(different behavior, different definition) are always different.
Closures created at different times but with no detectable differences
may be classified as equal or not (depending on internal caching details).

You can change the way that Lua compares tables and userdata
by using the "eq" metamethod (see [Metatables and Metamethods](2_-_Basic_Concepts.htm#4)).

Equality comparisons do not convert strings to numbers
or vice versa.
Thus, `"0"==0` evaluates to **false**,
and `t[0]` and `t["0"]` denote different
entries in a table.

The operator `~=` is exactly the negation of equality (`==`).

The order operators work as follows.
If both arguments are numbers,
then they are compared according to their mathematical values
(regardless of their subtypes).
Otherwise, if both arguments are strings,
then their values are compared according to the current locale.
Otherwise, Lua tries to call the "lt" or the "le"
metamethod (see [Metatables and Metamethods](2_-_Basic_Concepts.htm#4)).
A comparison `a > b` is translated to `b < a`
and `a >= b` is translated to `b <= a`.

Following the IEEE 754 standard,
NaN is considered neither smaller than,
nor equal to, nor greater than any value (including itself).

### 4.5 â Logical Operators

The logical operators in Lua are
**and**, **or**, and **not**.
Like the [control structures](#3.4),
all logical operators consider both **false** and **nil** as false
and anything else as true.

The negation operator **not** always returns **false** or **true**.
The conjunction operator **and** returns its first argument
if this value is **false** or **nil**;
otherwise, **and** returns its second argument.
The disjunction operator **or** returns its first argument
if this value is different from **nil** and **false**;
otherwise, **or** returns its second argument.
Both **and** and **or** use short-circuit evaluation;
that is,
the second operand is evaluated only if necessary.
Here are some examples:

```lua
     10 or 20            --> 10
			10 or error()       --> 10
			nil or "a"          --> "a"
			nil and 10          --> nil
			false and error()   --> false
			false and nil       --> false
			false or nil        --> nil
			10 and 20           --> 20
		
```

(In this manual,
`-->` indicates the result of the preceding expression.)

### 4.6 â Concatenation

The string concatenation operator in Lua is
denoted by two dots ('`..`').
If both operands are strings or numbers, then they are converted to
strings according to the rules described in [Coercions and Conversions](#4.3).
Otherwise, the `__concat` metamethod is called (see [Metatables and Metamethods](2_-_Basic_Concepts.htm#4)).

### 4.7 â The Length Operator

The length operator is denoted by the unary prefix operator `#`.
The length of a string is its number of bytes
(that is, the usual meaning of string length when each
character is one byte).

A program can modify the behavior of the length operator for
any value but strings through the `__len` metamethod (see [Metatables and Metamethods](2_-_Basic_Concepts.htm#4)).

Unless a `__len` metamethod is given,
the length of a table `t` is only defined if the
table is a *sequence*,
that is,
the set of its positive numeric keys is equal to *{1..n}*
for some non-negative integer *n*.
In that case, *n* is its length.
Note that a table like

```lua
     {10, 20, nil, 40}
		
```

is not a sequence, because it has the key `4`
but does not have the key `3`.
(So, there is no *n* such that the set *{1..n}* is equal
to the set of positive numeric keys of that table.)
Note, however, that non-numeric keys do not interfere
with whether a table is a sequence.

### 4.8 â Precedence

Operator precedence in Lua follows the table below,
from lower to higher priority:

```lua
     or
			and
			<     >     <=    >=    ~=    ==
			|
			~
			&     <<    >>     ..
			+     -
			*     /     //    %
			unary operators (not   #     -     ~)
			^
		
```

As usual,
you can use parentheses to change the precedences of an expression.
The concatenation ('`..`') and exponentiation ('`^`')
operators are right associative.
All other binary operators are left associative.

### 4.9 â Table Constructors

Table constructors are expressions that create tables.
Every time a constructor is evaluated, a new table is created.
A constructor can be used to create an empty table
or to create a table and initialize some of its fields.
The general syntax for constructors is

```lua
	tableconstructor ::= '{' [fieldlist] '}'
			fieldlist ::= field {fieldsep field} [fieldsep]
			field ::= '[' exp ']' '=' exp | Name '=' exp | exp
			fieldsep ::= ',' | ';'
		
```

Each field of the form `[exp1] = exp2` adds to the new table an entry
with key `exp1` and value `exp2`.
A field of the form `name = exp` is equivalent to
`["name"] = exp`.
Finally, fields of the form `exp` are equivalent to
`[i] = exp`, where `i` are consecutive integers
starting with 1.
Fields in the other formats do not affect this counting.
For example,

```lua
     a = { [f(1)] = g; "x", "y"; x = 1, f(x), [30] = 23; 45 }
		
```

is equivalent to

```lua
     do
			local t = {}
			t[f(1)] = g
			t[1] = "x"         -- 1st exp
			t[2] = "y"         -- 2nd exp
			t.x = 1            -- t["x"] = 1
			t[3] = f(x)        -- 3rd exp
			t[30] = 23
			t[4] = 45          -- 4th exp
			a = t
			end
		
```

The order of the assignments in a constructor is undefined.
(This order would be relevant only when there are repeated keys.)

If the last field in the list has the form `exp`
and the expression is a function call or a vararg expression,
then all values returned by this expression enter the list consecutively
(see [Function Calls](#4.10)).

The field list can have an optional trailing separator,
as a convenience for machine-generated code.

### 4.10 â Function Calls

A function call in Lua has the following syntax:

```lua
	functioncall ::= prefixexp args
		
```

In a function call,
first prefixexp and args are evaluated.
If the value of prefixexp has type *function*,
then this function is called
with the given arguments.
Otherwise, the prefixexp "call" metamethod is called,
having as first argument the value of prefixexp,
followed by the original call arguments
(see [Metatables and Metamethods](2_-_Basic_Concepts.htm#4)).

The form

```lua
	functioncall ::= prefixexp ':' Name args
		
```

can be used to call "methods".
A call `v:name(args)`
is syntactic sugar for `v.name(v,args)`,
except that `v` is evaluated only once.

Arguments have the following syntax:

```lua
	args ::= '(' [explist] ')'
			args ::= tableconstructor
			args ::= LiteralString
		
```

All argument expressions are evaluated before the call.
A call of the form `f{fields}` is
syntactic sugar for `f({fields})`;
that is, the argument list is a single new table.
A call of the form `f'string'`
(or `f"string"` or `f[[string]]`)
is syntactic sugar for `f('string')`;
that is, the argument list is a single literal string.

A call of the form `return functioncall` is called
a *tail call*.
Lua implements *proper tail calls*
(or *proper tail recursion*):
in a tail call,
the called function reuses the stack entry of the calling function.
Therefore, there is no limit on the number of nested tail calls that
a program can execute.
However, a tail call erases any debug information about the
calling function.
Note that a tail call only happens with a particular syntax,
where the **return** has one single function call as argument;
this syntax makes the calling function return exactly
the returns of the called function.
So, none of the following examples are tail calls:

```lua
     return (f(x))        -- results adjusted to 1
			return 2 * f(x)
			return x, f(x)       -- additional results
			f(x); return         -- results discarded
			return x or f(x)     -- results adjusted to 1
		
```

### 4.11 â Function Definitions

The syntax for function definition is

```lua
	functiondef ::= function funcbody
			funcbody ::= '(' [parlist] ')' block end
		
```

The following syntactic sugar simplifies function definitions:

```lua
	stat ::= function funcname funcbody
			stat ::= local function Name funcbody
			funcname ::= Name {'.' Name} [':' Name]
		
```

The statement

```lua
     function f () body end
		
```

translates to

```lua
     f = function () body end
		
```

The statement

```lua
     function t.a.b.c.f () body end
		
```

translates to

```lua
     t.a.b.c.f = function () body end
		
```

The statement

```lua
     local function f () body end
		
```

translates to

```lua
     local f; f = function () body end
		
```

not to

```lua
     local f = function () body end
		
```

(This only makes a difference when the body of the function
contains references to `f`.)

A function definition is an executable expression,
whose value has type *function*.
When Lua precompiles a chunk,
all its function bodies are precompiled too.
Then, whenever Lua executes the function definition,
the function is *instantiated* (or *closed*).
This function instance (or *closure*)
is the final value of the expression.

Parameters act as local variables that are
initialized with the argument values:

```lua
	parlist ::= namelist [',' '...'] | '...'
		
```

When a function is called,
the list of arguments is adjusted to
the length of the list of parameters,
unless the function is a *vararg function*,
which is indicated by three dots ('`...`')
at the end of its parameter list.
A vararg function does not adjust its argument list;
instead, it collects all extra arguments and supplies them
to the function through a *vararg expression*,
which is also written as three dots.
The value of this expression is a list of all actual extra arguments,
similar to a function with multiple results.
If a vararg expression is used inside another expression
or in the middle of a list of expressions,
then its return list is adjusted to one element.
If the expression is used as the last element of a list of expressions,
then no adjustment is made
(unless that last expression is enclosed in parentheses).

As an example, consider the following definitions:

```lua
     function f(a, b) end
			function g(a, b, ...) end
			function r() return 1,2,3 end
		
```

Then, we have the following mapping from arguments to parameters and
to the vararg expression:

```lua
     CALL            PARAMETERS
     
			f(3)             a=3, b=nil
			f(3, 4)          a=3, b=4
			f(3, 4, 5)       a=3, b=4
			f(r(), 10)       a=1, b=10
			f(r())           a=1, b=2
     
			g(3)             a=3, b=nil, ... -->  (nothing)
			g(3, 4)          a=3, b=4,   ... -->  (nothing)
			g(3, 4, 5, 8)    a=3, b=4,   ... -->  5  8
			g(5, r())        a=5, b=1,   ... -->  2  3
		
```

Results are returned using the **return** statement (see [Control Structures](#3.4)).
If control reaches the end of a function
without encountering a **return** statement,
then the function returns with no results.

There is a system-dependent limit on the number of values
that a function may return.
This limit is guaranteed to be larger than 1000.

The *colon* syntax
is used for defining *methods*,
that is, functions that have an implicit extra parameter `self`.
Thus, the statement

```lua
     function t.a.b.c:f (params) body end
		
```

is syntactic sugar for

```lua
     t.a.b.c.f = function (self, params) body end
		
```

## 5 â Visibility Rules

Lua is a lexically scoped language.
The scope of a local variable begins at the first statement after
its declaration and lasts until the last non-void statement
of the innermost block that includes the declaration.
Consider the following example:

```lua
     x = 10                -- global variable
			do                    -- new block
			local x = x         -- new 'x', with value 10
			print(x)            --> 10
			x = x+1
			do                  -- another block
			local x = x+1     -- another 'x'
			print(x)          --> 12
			end
			print(x)            --> 11
			end
			print(x)              --> 10  (the global one)
		
```

Notice that, in a declaration like `local x = x`,
the new `x` being declared is not in scope yet,
and so the second `x` refers to the outside variable.

Because of the lexical scoping rules,
local variables can be freely accessed by functions
defined inside their scope.
A local variable used by an inner function is called
an *upvalue*, or *external local variable*,
inside the inner function.

Notice that each execution of a **local** statement
defines new local variables.
Consider the following example:

```lua
     a = {}
			local x = 20
			for i=1,10 do
			local y = 0
			a[i] = function () y=y+1; return x+y end
			end
		
```

The loop creates ten closures
(that is, ten instances of the anonymous function).
Each of these closures uses a different `y` variable,
while all of them share the same `x`.
