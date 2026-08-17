# Lua 5.3 Reference Manual - Standard Libraries Intro

> Source: https://help.qsys.com/Content/Control_Scripting/Lua_5.3_Reference_Manual/Standard_Libraries/Standard_Libraries_Intro.htm

# Lua 5.3 Reference Manual

by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes

Copyright Â© 2015â2018 Lua.org, PUC-Rio. Freely available under the terms of the [Lua license](http://www.lua.org/license.html).

[contents](../Contents-Index.htm#contents)
Â·
[index](../Contents-Index.htm#index)

# Standard Libraries

The standard Lua libraries provide useful functions
that are implemented directly through the C API.
Some of these functions provide essential services to the language
(e.g., [`type`](1_-_Basic_Functions.htm#pdf-type) and [`getmetatable`](1_-_Basic_Functions.htm#pdf-getmetatable));
others provide access to "outside" services;
and others could be implemented in Lua itself,
but are quite useful or have critical performance requirements that
deserve an implementation in C (e.g., [`table.sort`](5_-_Table_Manipulation.htm#pdf-table.sort)).

All libraries are implemented through the official C API
and are provided as separate C modules.
Currently, Lua has the following standard libraries:

* [1 â Basic Functions](1_-_Basic_Functions.htm#BasicFunctions)
* [2 â Modules](2_-_Modules.htm#Modules)
* [3 â String Manipulation](3_-_String_Manipulation.htm#StringManipulation)
  + [3.1 â Patterns](3_-_String_Manipulation.htm#3.1)
  + [3.2 â Format Strings for Pack and Unpack](3_-_String_Manipulation.htm#3.2)
* [4 â UTF-8 Support](4_-_Basic_UTF-8_Support.htm#UTF8Support)
* [5 â Table Manipulation](5_-_Table_Manipulation.htm#Table)
* [6 â Mathematical Functions](6_-_Mathematical_Functions.htm#MathFunctions) (sin, log, etc.)
* [7 â Operating System Facilities](7_-_Operating_System_Facilities.htm#OSFacilities)

Except for the basic and the package libraries,
each library provides all its functions as fields of a global table
or as methods of its objects.
