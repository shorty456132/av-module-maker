# Lua 5.3 Reference Manual - Basic Concepts

> Source: https://help.qsys.com/Content/Control_Scripting/Lua_5.3_Reference_Manual/2_-_Basic_Concepts.htm

# Lua 5.3 Reference Manual

by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes

Copyright Â© 2015â2018 Lua.org, PUC-Rio. Freely available under the terms of the [Lua license](http://www.lua.org/license.html).

[contents](Contents-Index.htm#contents)
Â·
[index](Contents-Index.htm#index)

# Basic Concepts

This section describes the basic concepts of the language.

## 1 â Values and Types

Lua is a *dynamically typed language*.
This means that
variables do not have types; only values do.
There are no type definitions in the language.
All values carry their own type.

All values in Lua are *first-class values*.
This means that all values can be stored in variables,
passed as arguments to other functions, and returned as results.

There are eight basic types in Lua:
*nil*, *boolean*, *number*,
*string*, *function*, *userdata*,
*thread*, and *table*.
The type *nil* has one single value, **nil**,
whose main property is to be different from any other value;
it usually represents the absence of a useful value.
The type *boolean* has two values, **false** and **true**.
Both **nil** and **false** make a condition false;
any other value makes it true.
The type *number* represents both
integer numbers and real (floating-point) numbers.
The type *string* represents immutable sequences of bytes.
Lua is 8-bit clean:
strings can contain any 8-bit value,
including embedded zeros ('`\0`').
Lua is also encoding-agnostic;
it makes no assumptions about the contents of a string.

The type *number* uses two internal representations,
or two subtypes,
one called *integer* and the other called *float*.
Lua has explicit rules about when each representation is used,
but it also converts between them automatically as needed (see [Coercions and Conversions](3_-_The_Language.htm#4.3)).
Therefore,
the programmer may choose to mostly ignore the difference
between integers and floats
or to assume complete control over the representation of each number.
Standard Lua uses 64-bit integers and double-precision (64-bit) floats,
but you can also compile Lua so that it
uses 32-bit integers and/or single-precision (32-bit) floats.
The option with 32 bits for both integers and floats
is particularly attractive
for small machines and embedded systems.
(See macro `LUA_32BITS` in file `luaconf.h`.)

Lua can call (and manipulate) functions written in Lua and
functions written in C (see [Function Calls](3_-_The_Language.htm#4.10)).
Both are represented by the type *function*.

The type *userdata* is provided to allow arbitrary C data to
be stored in Lua variables.
A userdata value represents a block of raw memory.
There are two kinds of userdata:
*full userdata*,
which is an object with a block of memory managed by Lua,
and *light userdata*,
which is simply a C pointer value.
Userdata has no predefined operations in Lua,
except assignment and identity test.
By using *metatables*,
the programmer can define operations for full userdata values
(see [Metatables and Metamethods](#4)).
Userdata values cannot be created or modified in Lua,
only through the C API.
This guarantees the integrity of data owned by the host program.

The type *table* implements associative arrays,
that is, arrays that can have as indices not only numbers, but any Lua value except **nil** and NaN.
(*Not a Number* is a special value used to represent
undefined or unrepresentable numerical results, such as `0/0`.)
Tables can be *heterogeneous*;
that is, they can contain values of all types (except **nil**).
Any key with value **nil** is not considered part of the table.
Conversely, any key that is not part of a table has
an associated value **nil**.

Tables are the sole data-structuring mechanism in Lua;
they can be used to represent ordinary arrays, sequences,
symbol tables, sets, records, graphs, trees, etc.
To represent records, Lua uses the field name as an index.
The language supports this representation by
providing `a.name` as syntactic sugar for `a["name"]`.
There are several convenient ways to create tables in Lua
(see [Table Constructors](3_-_The_Language.htm#4.9)).

We use the term *sequence* to denote a table where
the set of all positive numeric keys is equal to {1..*n*}
for some non-negative integer *n*,
which is called the length of the sequence (see [The Length Operator](3_-_The_Language.htm#4.7)).

Like indices,
the values of table fields can be of any type.
In particular,
because functions are first-class values,
table fields can contain functions.
Thus tables can also carry *methods* (see [Function Definitions](3_-_The_Language.htm#4.11)).

The indexing of tables follows
the definition of raw equality in the language.
The expressions `a[i]` and `a[j]`
denote the same table element
if and only if `i` and `j` are raw equal
(that is, equal without metamethods).
In particular, floats with integral values
are equal to their respective integers
(e.g., `1.0 == 1`).
To avoid ambiguities,
any float with integral value used as a key
is converted to its respective integer.
For instance, if you write `a[2.0] = true`,
the actual key inserted into the table will be the
integer `2`.
(On the other hand,
2 and "`2`" are different Lua values and therefore
denote different table entries.)

Tables, functions, threads, and (full) userdata values are *objects*:
variables do not actually *contain* these values,
only *references* to them.
Assignment, parameter passing, and function returns
always manipulate references to such values;
these operations do not imply any kind of copy.

The library function [`type`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-type) returns a string describing the type
of a given value (see [Basic Functions](Standard_Libraries/1_-_Basic_Functions.htm#BasicFunctions)).

## 2 â Environments and the Global Environment

As will be discussed in [Variables](3_-_The_Language.htm#2) and [Assignment](3_-_The_Language.htm#3.3),
any reference to a free name
(that is, a name not bound to any declaration) `var`
is syntactically translated to `_ENV.var`.
Moreover, every chunk is compiled in the scope of
an external local variable named `_ENV` (see [Chunks](3_-_The_Language.htm#3.2)),
so `_ENV` itself is never a free name in a chunk.

Despite the existence of this external `_ENV` variable and
the translation of free names,
`_ENV` is a completely regular name.
In particular,
you can define new variables and parameters with that name.
Each reference to a free name uses the `_ENV` that is
visible at that point in the program,
following the usual visibility rules of Lua (see [Visibility Rules](3_-_The_Language.htm#5)).

Any table used as the value of `_ENV` is called an *environment*.

Lua keeps a distinguished environment called the *global environment*.
In Lua, the global variable [`_G`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-_G) is initialized with this value.
([`_G`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-_G) is never used internally.)

When Lua loads a chunk,
the default value for its `_ENV` upvalue
is the global environment (see [`load`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-load)).
Therefore, by default,
free names in Lua code refer to entries in the global environment
(and, therefore, they are also called *global variables*).
Moreover, all standard libraries are loaded in the global environment
and some functions there operate on that environment.
You can use [`load`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-load)
to load a chunk with a different environment.
(In C, you have to load the chunk and then change the value
of its first upvalue.)

## 3 â Error Handling

Because Lua is an embedded extension language,
all Lua actions start from C code in the host program
calling a function from the Lua library.
Whenever an error occurs during
the compilation or execution of a Lua chunk,
control returns to the host,
which can take appropriate measures
(such as printing an error message).

Lua code can explicitly generate an error by calling the
[`error`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-error) function.
If you need to catch errors in Lua,
you can use [`pcall`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-pcall) or [`xpcall`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-xpcall)
to call a given function in *protected mode*.

Whenever there is an error,
an *error object* (also called an *error message*)
is propagated with information about the error.
Lua itself only generates errors whose error object is a string,
but programs may generate errors with
any value as the error object.
It is up to the Lua program or its host to handle such error objects.

When you use [`xpcall`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-xpcall),
you may give a *message handler*
to be called in case of errors.
This function is called with the original error message
and returns a new error message.
It is called before the error unwinds the stack,
so that it can gather more information about the error,
for instance by inspecting the stack and creating a stack traceback.
This message handler is still protected by the protected call;
so, an error inside the message handler
will call the message handler again.
If this loop goes on for too long,
Lua breaks it and returns an appropriate message.

## 4 â Metatables and Metamethods

Every value in Lua can have a *metatable*.
This *metatable* is an ordinary Lua table
that defines the behavior of the original value
under certain special operations.
You can change several aspects of the behavior
of operations over a value by setting specific fields in its metatable.
For instance, when a non-numeric value is the operand of an addition,
Lua checks for a function in the field "`__add`" of the value's metatable.
If it finds one,
Lua calls this function to perform the addition.

The keys in a metatable are derived from the *event* names;
the corresponding values are called *metamethods*.
In the previous example, the event is `"add"`
and the metamethod is the function that performs the addition.
Unless stated otherwise, metamethods should be function values.

You can query the metatable of any value
using the [`getmetatable`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-getmetatable) function.

You can replace the metatable of tables
using the [`setmetatable`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-setmetatable) function.
You cannot change the metatable of other types from Lua code.

Tables and full userdata have individual metatables
(although multiple tables and userdata can share their metatables).
Values of all other types share one single metatable per type;
that is, there is one single metatable for all numbers,
one for all strings, etc.
By default, a value has no metatable,
but the string library sets a metatable for the string type (see [String Manipulation](Standard_Libraries/3_-_String_Manipulation.htm#StringManipulation)).

A metatable controls how an object behaves in
arithmetic operations, bitwise operations,
order comparisons, concatenation, length operation, calls, and indexing.
A metatable also can define a function to be called
when a userdata or a table is garbage collected ([Garbage Collection](#5)).

A detailed list of events controlled by metatables is given next.
Each operation is identified by its corresponding event name.
The key for each event is a string with its name prefixed by
two underscores, '`__`';
for instance, the key for operation "add" is the
string "`__add`".
Note that queries for metamethods are always raw;
the access to a metamethod does not invoke other metamethods.

For the unary operators (negation, length, and bitwise not),
the metamethod is computed and called with a dummy second operand,
equal to the first one.
This extra operand is only to simplify Lua's internals
(by making these operators behave like a binary operation)
and may be removed in future versions.
(For most uses this extra operand is irrelevant.)

* **"add":** 
  the `+` operation.
  If any operand for an addition is not a number
  (nor a string coercible to a number),
  Lua will try to call a metamethod.
  First, Lua will check the first operand (even if it is valid).
  If that operand does not define a metamethod for the "`__add`" event,
  then Lua will check the second operand.
  If Lua can find a metamethod,
  it calls the metamethod with the two operands as arguments,
  and the result of the call
  (adjusted to one value)
  is the result of the operation.
  Otherwise,
  it raises an error.
* **"sub":** 
  the `-` operation.
  Behavior similar to the "add" operation.
* **"mul":** 
  the `*` operation.
  Behavior similar to the "add" operation.
* **"div":** 
  the `/` operation.
  Behavior similar to the "add" operation.
* **"mod":** 
  the `%` operation.
  Behavior similar to the "add" operation.
* **"pow":** 
  the `^` (exponentiation) operation.
  Behavior similar to the "add" operation.
* **"unm":** 
  the `-` (unary minus) operation.
  Behavior similar to the "add" operation.
* **"idiv":** 
  the `//` (floor division) operation.
  Behavior similar to the "add" operation.
* **"band":** 
  the `&` (bitwise and) operation.
  Behavior similar to the "add" operation,
  except that Lua will try a metamethod
  if any operand is neither an integer
  nor a value coercible to an integer (see [Coercions and Conversions](3_-_The_Language.htm#4.3)).
* **"bor":** 
  the `|` (bitwise or) operation.
  Behavior similar to the "band" operation.
* **"bxor":** 
  the `~` (bitwise exclusive or) operation.
  Behavior similar to the "band" operation.
* **"bnot":** 
  the `~` (bitwise unary not) operation.
  Behavior similar to the "band" operation.
* **"shl":** 
  the `<<` (bitwise left shift) operation.
  Behavior similar to the "band" operation.
* **"shr":** 
  the `>>` (bitwise right shift) operation.
  Behavior similar to the "band" operation.
* **"concat":** 
  the `..` (concatenation) operation.
  Behavior similar to the "add" operation,
  except that Lua will try a metamethod
  if any operand is neither a string nor a number
  (which is always coercible to a string).
* **"len":** 
  the `#` (length) operation.
  If the object is not a string,
  Lua will try its metamethod.
  If there is a metamethod,
  Lua calls it with the object as argument,
  and the result of the call
  (always adjusted to one value)
  is the result of the operation.
  If there is no metamethod but the object is a table,
  then Lua uses the table length operation (see [The Length Operator](3_-_The_Language.htm#4.7)).
  Otherwise, Lua raises an error.
* **"eq":** 
  the `==` (equal) operation.
  Behavior similar to the "add" operation,
  except that Lua will try a metamethod only when the values
  being compared are either both tables or both full userdata
  and they are not primitively equal.
  The result of the call is always converted to a boolean.
* **"lt":** 
  the `<` (less than) operation.
  Behavior similar to the "add" operation,
  except that Lua will try a metamethod only when the values
  being compared are neither both numbers nor both strings.
  The result of the call is always converted to a boolean.
* **"le":** 
  the `<=` (less equal) operation.
  Unlike other operations,
  the less-equal operation can use two different events.
  First, Lua looks for the "`__le`" metamethod in both operands,
  like in the "lt" operation.
  If it cannot find such a metamethod,
  then it will try the "`__lt`" event,
  assuming that `a <= b` is equivalent to `not (b < a)`.
  As with the other comparison operators,
  the result is always a boolean.
  (This use of the "`__lt`" event can be removed in future versions;
  it is also slower than a real "`__le`" metamethod.)
* **"index":** 
  The indexing access operation `table[key]`.
  This event happens when `table` is not a table or
  when `key` is not present in `table`.
  The metamethod is looked up in `table`.

  Despite the name,
  the metamethod for this event can be either a function or a table.
  If it is a function,
  it is called with `table` and `key` as arguments.
  If it is a table,
  the final result is the result of indexing this table with `key`.
  (This indexing is regular, not raw,
  and therefore can trigger another metamethod.)
* **"newindex":** 
  The indexing assignment `table[key] = value`.
  Like the index event,
  this event happens when `table` is not a table or
  when `key` is not present in `table`.
  The metamethod is looked up in `table`.

  Like with indexing,
  the metamethod for this event can be either a function or a table.
  If it is a function,
  it is called with `table`, `key`, and `value` as arguments.
  If it is a table,
  Lua does an indexing assignment to this table with the same key and value.
  (This assignment is regular, not raw,
  and therefore can trigger another metamethod.)

  Whenever there is a "newindex" metamethod,
  Lua does not perform the primitive assignment.
  (If necessary,
  the metamethod itself can call [`rawset`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-rawset)
  to do the assignment.)
* **"call":** 
  The call operation `func(args)`.
  This event happens when Lua tries to call a non-function value
  (that is, `func` is not a function).
  The metamethod is looked up in `func`.
  If present,
  the metamethod is called with `func` as its first argument,
  followed by the arguments of the original call (`args`).

It is a good practice to add all needed metamethods to a table
before setting it as a metatable of some object.
In particular, the "`__gc`" metamethod works only when this order
is followed (see [Garbage-Collection Metamethods](#5.1)).

## 5 â Garbage Collection

Lua performs automatic memory management.
This means that
you do not have to worry about allocating memory for new objects
or freeing it when the objects are no longer needed.
Lua manages memory automatically by running
a *garbage collector* to collect all *dead objects*
(that is, objects that are no longer accessible from Lua).
All memory used by Lua is subject to automatic management:
strings, tables, userdata, functions, threads, internal structures, etc.

Lua implements an incremental mark-and-sweep collector.
It uses two numbers to control its garbage-collection cycles:
the *garbage-collector pause* and
the *garbage-collector step multiplier*.
Both use percentage points as units
(e.g., a value of 100 means an internal value of 1).

The garbage-collector pause
controls how long the collector waits before starting a new cycle.
Larger values make the collector less aggressive.
Values smaller than 100 mean the collector will not wait to
start a new cycle.
A value of 200 means that the collector waits for the total memory in use
to double before starting a new cycle.

The garbage-collector step multiplier
controls the relative speed of the collector relative to
memory allocation.
Larger values make the collector more aggressive but also increase
the size of each incremental step.
You should not use values smaller than 100,
because they make the collector too slow and
can result in the collector never finishing a cycle.
The default is 200,
which means that the collector runs at "twice"
the speed of memory allocation.

If you set the step multiplier to a very large number
(larger than 10% of the maximum number of
bytes that the program may use),
the collector behaves like a stop-the-world collector.
If you then set the pause to 200,
the collector behaves as in old Lua versions,
doing a complete collection every time Lua doubles its
memory usage.

You can change these numbers by calling [`collectgarbage`](Standard_Libraries/1_-_Basic_Functions.htm#pdf-collectgarbage) in Lua.
You can also use these functions to control
the collector directly (e.g., stop and restart it).

### 5.1 â Garbage-Collection Metamethods

You can set garbage-collector metamethods for tables.
These metamethods are also called *finalizers*.
Finalizers allow you to coordinate Lua's garbage collection
with external resource management
(such as closing files, network or database connections,
or freeing your own memory).

For an object (table or userdata) to be finalized when collected,
you must *mark* it for finalization.
You mark an object for finalization when you set its metatable
and the metatable has a field indexed by the string "`__gc`".
Note that if you set a metatable without a `__gc` field
and later create that field in the metatable,
the object will not be marked for finalization.

When a marked object becomes garbage,
it is not collected immediately by the garbage collector.
Instead, Lua puts it in a list.
After the collection,
Lua goes through that list.
For each object in the list,
it checks the object's `__gc` metamethod:
If it is a function,
Lua calls it with the object as its single argument;
if the metamethod is not a function,
Lua simply ignores it.

At the end of each garbage-collection cycle,
the finalizers for objects are called in
the reverse order that the objects were marked for finalization,
among those collected in that cycle;
that is, the first finalizer to be called is the one associated
with the object marked last in the program.
The execution of each finalizer may occur at any point during
the execution of the regular code.

Because the object being collected must still be used by the finalizer,
that object (and other objects accessible only through it)
must be *resurrected* by Lua.
Usually, this resurrection is transient,
and the object memory is freed in the next garbage-collection cycle.
However, if the finalizer stores the object in some global place
(e.g., a global variable),
then the resurrection is permanent.
Moreover, if the finalizer marks a finalizing object for finalization again,
its finalizer will be called again in the next cycle where the
object is unreachable.
In any case,
the object memory is freed only in a GC cycle where
the object is unreachable and not marked for finalization.

When you close a state,
Lua calls the finalizers of all objects marked for finalization,
following the reverse order that they were marked.
If any finalizer marks objects for collection during that phase,
these marks have no effect.

### 5.2 â Weak Tables

A *weak table* is a table whose elements are
*weak references*.
A weak reference is ignored by the garbage collector.
In other words,
if the only references to an object are weak references,
then the garbage collector will collect that object.

A weak table can have weak keys, weak values, or both.
A table with weak values allows the collection of its values,
but prevents the collection of its keys.
A table with both weak keys and weak values allows the collection of
both keys and values.
In any case, if either the key or the value is collected,
the whole pair is removed from the table.
The weakness of a table is controlled by the
`__mode` field of its metatable.
If the `__mode` field is a string containing the character '`k`',
the keys in the table are weak.
If `__mode` contains '`v`',
the values in the table are weak.

A table with weak keys and strong values
is also called an *ephemeron table*.
In an ephemeron table,
a value is considered reachable only if its key is reachable.
In particular,
if the only reference to a key comes through its value,
the pair is removed.

Any change in the weakness of a table may take effect only
at the next collect cycle.
In particular, if you change the weakness to a stronger mode,
Lua may still collect some items from that table
before the change takes effect.

Only objects that have an explicit construction
are removed from weak tables.
Values, such as numbers are not subject to garbage collection,
and therefore are not removed from weak tables
(unless their associated values are collected).
Although strings are subject to garbage collection,
they do not have an explicit construction,
and therefore are not removed from weak tables.

Resurrected objects
(that is, objects being finalized
and objects accessible only through objects being finalized)
have a special behavior in weak tables.
They are removed from weak values before running their finalizers,
but are removed from weak keys only in the next collection
after running their finalizers, when such objects are actually freed.
This behavior allows the finalizer to access properties
associated with the object through weak tables.

If a weak table is among the resurrected objects in a collection cycle,
it may not be properly cleared until the next cycle.
