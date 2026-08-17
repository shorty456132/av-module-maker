# Lua 5.3 Reference Manual - Contents-Index

> Source: https://help.qsys.com/Content/Control_Scripting/Lua_5.3_Reference_Manual/Contents-Index.htm

# Lua 5.3 Reference Manual

The reference manual is the official definition of the Lua language.
  
 For a complete introduction to Lua programming, see the book
[Programming in Lua](http://www.lua.org/pil/).

[start](1_-_Introduction.htm)
Â·
[contents](#contents)
Â·
[index](#index)

Copyright Â© 2015â2018 Lua.org, PUC-Rio.
Freely available under the terms of the
[Lua license](http://www.lua.org/license.html).

**Note:** Certain elements of the Lua 5.3 Reference Manual have been omitted here if they do not pertain to the Lua implementation within Q-SYS.

## Contents

* [Introduction](1_-_Introduction.htm#Introduction)
* [Basic Concepts](2_-_Basic_Concepts.htm#BasicConcepts)
  + [1 â Values and Types](2_-_Basic_Concepts.htm#1)
  + [2 â Environments and the Global Environment](2_-_Basic_Concepts.htm#2)
  + [3 â Error Handling](2_-_Basic_Concepts.htm#3)
  + [4 â Metatables and Metamethods](2_-_Basic_Concepts.htm#4)
  + [5 â Garbage Collection](2_-_Basic_Concepts.htm#5)
    - [5.1 â Garbage-Collection Metamethods](2_-_Basic_Concepts.htm#5.1)
    - [5.2 â Weak Tables](2_-_Basic_Concepts.htm#5.2)
* [The Language](3_-_The_Language.htm#TheLanguage)
  + [1 â Lexical Conventions](3_-_The_Language.htm#1)
  + [2 â Variables](3_-_The_Language.htm#2)
  + [3 â Statements](3_-_The_Language.htm#3)
    - [3.1 â Blocks](3_-_The_Language.htm#3.1)
    - [3.2 â Chunks](3_-_The_Language.htm#3.2)
    - [3.3 â Assignment](3_-_The_Language.htm#3.3)
    - [3.4 â Control Structures](3_-_The_Language.htm#3.4)
    - [3.5 â For Statement](3_-_The_Language.htm#3.5)
    - [3.6 â Function Calls as Statements](3_-_The_Language.htm#3.6)
    - [3.7 â Local Declarations](3_-_The_Language.htm#3.7)
  + [4 â Expressions](3_-_The_Language.htm#4)
    - [4.1 â Arithmetic Operators](3_-_The_Language.htm#4.1)
    - [4.2 â Bitwise Operators](3_-_The_Language.htm#4.2)
    - [4.3 â Coercions and Conversions](3_-_The_Language.htm#4.3)
    - [4.4 â Relational Operators](3_-_The_Language.htm#4.4)
    - [4.5 â Logical Operators](3_-_The_Language.htm#4.5)
    - [4.6 â Concatenation](3_-_The_Language.htm#4.6)
    - [4.7 â The Length Operator](3_-_The_Language.htm#4.7)
    - [4.8 â Precedence](3_-_The_Language.htm#4.8)
    - [4.9 â Table Constructors](3_-_The_Language.htm#4.9)
    - [4.10 â Function Calls](3_-_The_Language.htm#4.10)
    - [4.11 â Function Definitions](3_-_The_Language.htm#4.11)
  + [5 â Visibility Rules](3_-_The_Language.htm#5)
* [Standard Libraries](Standard_Libraries/Standard_Libraries_Intro.htm#StandardLibraries)
  + [1 â Basic Functions](Standard_Libraries/1_-_Basic_Functions.htm#BasicFunctions)
  + [2 â Modules](Standard_Libraries/2_-_Modules.htm#Modules)
  + [3 â String Manipulation](Standard_Libraries/3_-_String_Manipulation.htm#StringManipulation)
    - [3.1 â Patterns](Standard_Libraries/3_-_String_Manipulation.htm#3.1)
    - [3.2 â Format Strings for Pack and Unpack](Standard_Libraries/3_-_String_Manipulation.htm#3.2)
  + [4 â UTF-8 Support](Standard_Libraries/4_-_Basic_UTF-8_Support.htm#UTF8Support)
  + [5 â Table Manipulation](Standard_Libraries/5_-_Table_Manipulation.htm#Table)
  + [6 â Mathematical Functions](Standard_Libraries/6_-_Mathematical_Functions.htm#MathFunctions)
  + [7 â Operating System Facilities](Standard_Libraries/7_-_Operating_System_Facilities.htm#OSFacilities)
* [Incompatibilities with the Previous Version](8_-_Incompatibilities_with_the_Previous_Version.htm#Incompatibilities)
  + [1 â Changes in the Language](8_-_Incompatibilities_with_the_Previous_Version.htm#1)
  + [2 â Changes in the Libraries](8_-_Incompatibilities_with_the_Previous_Version.htm#2)
* [The Complete Syntax of Lua](9_-_The_Complete_Syntax_of_Lua.htm#Syntax)

## Index

|  |  |
| --- | --- |
| Lua functions [basic](Standard_Libraries/1_-_Basic_Functions.htm#BasicFunctions)  [\_G](Standard_Libraries/1_-_Basic_Functions.htm#pdf-_G)  [\_VERSION](Standard_Libraries/1_-_Basic_Functions.htm#pdf-_VERSION)  [assert](Standard_Libraries/1_-_Basic_Functions.htm#pdf-assert)  [collectgarbage](Standard_Libraries/1_-_Basic_Functions.htm#pdf-collectgarbage)  [error](Standard_Libraries/1_-_Basic_Functions.htm#pdf-error)  [getmetatable](Standard_Libraries/1_-_Basic_Functions.htm#pdf-getmetatable)  [ipairs](Standard_Libraries/1_-_Basic_Functions.htm#pdf-ipairs)  [load](Standard_Libraries/1_-_Basic_Functions.htm#pdf-load)  [next](Standard_Libraries/1_-_Basic_Functions.htm#pdf-next)  [pairs](Standard_Libraries/1_-_Basic_Functions.htm#pdf-pairs)  [pcall](Standard_Libraries/1_-_Basic_Functions.htm#pdf-pcall)  [print](Standard_Libraries/1_-_Basic_Functions.htm#pdf-print)  [rawequal](Standard_Libraries/1_-_Basic_Functions.htm#pdf-rawequal)  [rawget](Standard_Libraries/1_-_Basic_Functions.htm#pdf-rawget)  [rawlen](Standard_Libraries/1_-_Basic_Functions.htm#pdf-rawlen)  [rawset](Standard_Libraries/1_-_Basic_Functions.htm#pdf-rawset)  [require](Standard_Libraries/2_-_Modules.htm#pdf-require)  [select](Standard_Libraries/1_-_Basic_Functions.htm#pdf-select)  [setmetatable](Standard_Libraries/1_-_Basic_Functions.htm#pdf-setmetatable)  [tonumber](Standard_Libraries/1_-_Basic_Functions.htm#pdf-tonumber)  [tostring](Standard_Libraries/1_-_Basic_Functions.htm#pdf-tostring)  [type](Standard_Libraries/1_-_Basic_Functions.htm#pdf-type)  [xpcall](Standard_Libraries/1_-_Basic_Functions.htm#pdf-xpcall)  [math](Standard_Libraries/6_-_Mathematical_Functions.htm#MathFunctions)  [math.abs](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.abs)  [math.acos](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.acos)  [math.asin](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.asin)  [math.atan](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.atan)  [math.ceil](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.ceil)  [math.cos](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.cos)  [math.deg](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.deg)  [math.exp](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.exp)  [math.floor](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.floor)  [math.fmod](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.fmod)  [math.huge](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.huge)  [math.log](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.log)  [math.max](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.max)  [math.maxinteger](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.maxinteger)  [math.min](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.min)  [math.mininteger](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.mininteger)  [math.modf](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.modf)  [math.pi](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.pi)  [math.rad](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.rad)  [math.random](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.random)  [math.randomseed](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.randomseed)  [math.sin](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.sin)  [math.sqrt](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.sqrt)  [math.tan](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.tan)  [math.tointeger](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.tointeger)  [math.type](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.type)  [math.ult](Standard_Libraries/6_-_Mathematical_Functions.htm#pdf-math.ult) | [os](Standard_Libraries/7_-_Operating_System_Facilities.htm#OSFacilities)  [os.clock](Standard_Libraries/7_-_Operating_System_Facilities.htm#pdf-os.clock)  [os.date](Standard_Libraries/7_-_Operating_System_Facilities.htm#pdf-os.date)  [os.difftime](Standard_Libraries/7_-_Operating_System_Facilities.htm#pdf-os.difftime)    [os.time](Standard_Libraries/7_-_Operating_System_Facilities.htm#pdf-os.time)  [package](Standard_Libraries/2_-_Modules.htm#Modules)  [package.loaded](Standard_Libraries/2_-_Modules.htm#pdf-package.loaded)  [package.path](Standard_Libraries/2_-_Modules.htm#pdf-package.path)  [package.preload](Standard_Libraries/2_-_Modules.htm#pdf-package.preload)  [package.searchers](Standard_Libraries/2_-_Modules.htm#pdf-package.searchers)  [package.searchpath](Standard_Libraries/2_-_Modules.htm#pdf-package.searchpath)  [string](Standard_Libraries/3_-_String_Manipulation.htm#StringManipulation)  [string.byte](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.byte)  [string.char](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.char)  [string.dump](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.dump)  [string.find](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.find)  [string.format](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.format)  [string.gmatch](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.gmatch)  [string.gsub](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.gsub)  [string.len](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.len)  [string.lower](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.lower)  [string.match](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.match)  [string.pack](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.pack)  [string.packsize](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.packsize)  [string.rep](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.rep)  [string.reverse](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.reverse)  [string.sub](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.sub)  [string.unpack](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.unpack)  [string.upper](Standard_Libraries/3_-_String_Manipulation.htm#pdf-string.upper)  [table](Standard_Libraries/5_-_Table_Manipulation.htm#Table)  [table.concat](Standard_Libraries/5_-_Table_Manipulation.htm#pdf-table.concat)  [table.insert](Standard_Libraries/5_-_Table_Manipulation.htm#pdf-table.insert)  [table.move](Standard_Libraries/5_-_Table_Manipulation.htm#pdf-table.move)  [table.pack](Standard_Libraries/5_-_Table_Manipulation.htm#pdf-table.pack)  [table.remove](Standard_Libraries/5_-_Table_Manipulation.htm#pdf-table.remove)  [table.sort](Standard_Libraries/5_-_Table_Manipulation.htm#pdf-table.sort)  [table.unpack](Standard_Libraries/5_-_Table_Manipulation.htm#pdf-table.unpack)  [utf8](Standard_Libraries/4_-_Basic_UTF-8_Support.htm#UTF8Support)  [utf8.char](Standard_Libraries/4_-_Basic_UTF-8_Support.htm#pdf-utf8.char)  [utf8.charpattern](Standard_Libraries/4_-_Basic_UTF-8_Support.htm#pdf-utf8.charpattern)  [utf8.codepoint](Standard_Libraries/4_-_Basic_UTF-8_Support.htm#pdf-utf8.codepoint)  [utf8.codes](Standard_Libraries/4_-_Basic_UTF-8_Support.htm#pdf-utf8.codes)  [utf8.len](Standard_Libraries/4_-_Basic_UTF-8_Support.htm#pdf-utf8.len)  [utf8.offset](Standard_Libraries/4_-_Basic_UTF-8_Support.htm#pdf-utf8.offset) |
