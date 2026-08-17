# Lua 5.3 Reference Manual - Table Manipulation

> Source: https://help.qsys.com/Content/Control_Scripting/Lua_5.3_Reference_Manual/Standard_Libraries/5_-_Table_Manipulation.htm

# Lua 5.3 Reference Manual

by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes

Copyright Â© 2015â2018 Lua.org, PUC-Rio. Freely available under the terms of the [Lua license](http://www.lua.org/license.html).

[contents](../Contents-Index.htm#contents)
Â·
[index](../Contents-Index.htm#index)

## Table Manipulation

This library provides generic functions for table manipulation.
It provides all its functions inside the table`table`.

Remember that, whenever an operation needs the length of a table,
the table must be a proper sequence
or have a `__len` metamethod (see [The Length Operator](../3_-_The_Language.htm#4.7)).
All functions ignore non-numeric keys
in the tables given as arguments.

---

### `table.concat (list [, sep [, i [, j]]])`

Given a list where all elements are strings or numbers,
returns the string `list[i]..sep..list[i+1] Â·Â·Â· sep..list[j]`.
The default value for `sep` is the empty string,
the default for `i` is 1,
and the default for `j` is `#list`.
If `i` is greater than `j`, returns the empty string.

---

### `table.insert (list, [pos,] value)`

Inserts element `value` at position `pos` in `list`,
shifting up the elements
`list[pos], list[pos+1], Â·Â·Â·, list[#list]`.
The default value for `pos` is `#list+1`,
so that a call `table.insert(t,x)` inserts `x` at the end
of list `t`.

---

### `table.move (a1, f, e, t [,a2])`

Moves elements from table `a1` to table `a2`.
This function performs the equivalent to the following
multiple assignment:
`a2[t],Â·Â·Â· = a1[f],Â·Â·Â·,a1[e]`.
The default for `a2` is `a1`.
The destination range can overlap with the source range.
The number of elements to be moved must fit in a Lua integer.

---

### `table.pack (Â·Â·Â·)`

Returns a new table with all arguments stored into keys 1, 2, etc.
and with a field "`n`" with the total number of arguments.
Note that the resulting table may not be a sequence.

---

### `table.remove (list [, pos])`

Removes from `list` the element at position `pos`,
returning the value of the removed element.
When `pos` is an integer between 1 and `#list`,
it shifts down the elements
`list[pos+1], list[pos+2], Â·Â·Â·, list[#list]`
and erases element `list[#list]`;
The index `pos` can also be 0 when `#list` is 0,
or `#list + 1`;
in those cases, the function erases the element `list[pos]`.

The default value for `pos` is `#list`,
so that a call `table.remove(l)` removes the last element
of list `l`.

---

### `table.sort (list [, comp])`

Sorts list elements in a given order, *in-place*,
from `list[1]` to `list[#list]`.
If `comp` is given,
then it must be a function that receives two list elements
and returns true when the first element must come
before the second in the final order
(so that, after the sort,
`i < j` implies `not comp(list[j],list[i])`).
If `comp` is not given,
then the standard Lua operator `<` is used instead.

Note that the `comp` function must define
a strict partial order over the elements in the list;
that is, it must be asymmetric and transitive.
Otherwise, no valid sort may be possible.

The sort algorithm is not stable;
that is, elements not comparable by the given order
(e.g., equal elements)
may have their relative positions changed by the sort.

---

### `table.unpack (list [, i [, j]])`

Returns the elements from the given list.
This function is equivalent to

```lua
     return list[i], list[i+1], Â·Â·Â·, list[j]
		
```

By default, `i` is 1 and `j` is `#list`.
