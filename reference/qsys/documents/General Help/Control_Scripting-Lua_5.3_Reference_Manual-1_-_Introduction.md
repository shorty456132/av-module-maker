# Lua 5.3 Reference Manual

> Source: https://help.qsys.com/Content/Control_Scripting/Lua_5.3_Reference_Manual/1_-_Introduction.htm

# Lua 5.3 Reference Manual

by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes

Copyright Â© 2015â2018 Lua.org, PUC-Rio. Freely available under the terms of the [Lua license](http://www.lua.org/license.html).

[contents](Contents-Index.htm#contents)
Â·
[index](Contents-Index.htm#index)

**Note:** Certain elements of the Lua 5.3 Reference Manual have been omitted here if they do not pertain to the Lua implementation within Q-SYS.

# 1 â Introduction

Lua is an extension programming language designed to support
general procedural programming with data description
facilities.
Lua also offers good support for object-oriented programming,
functional programming, and data-driven programming.
Lua is intended to be used as a powerful, lightweight,
embeddable scripting language for any program that needs one.
Lua is implemented as a library, written in *clean C*,
the common subset of Standard C and C++.

As an extension language, Lua has no notion of a "main" program:
it only works *embedded* in a host client,
called the *embedding program* or simply the *host*.
The host program can invoke functions to execute a piece of Lua code,
can write and read Lua variables,
and can register C functions to be called by Lua code.
Through the use of C functions, Lua can be augmented to cope with
a wide range of different domains,
thus creating customized programming languages sharing a syntactical framework.
The Lua distribution includes a sample host program called `lua`,
which uses the Lua library to offer a complete, standalone Lua interpreter,
for interactive or batch use.

Lua is free software,
and is provided as usual with no guarantees,
as stated in its license.
The implementation described in this manual is available
at Lua's official web site, `www.lua.org`.

Like any other reference manual,
this document is dry in places.
For a discussion of the decisions behind the design of Lua,
see the technical papers available at Lua's web site.
For a detailed introduction to programming in Lua,
see Roberto's book, *Programming in Lua*.
