# LuaXML

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/LuaXML.htm

# LuaXML

Using the LuaXML module provides a very simple and natural mapping between the XML data format and Lua tables. Allowing you to parse XML data just using Lua's normal table access and iteration methods. This may be useful in cases when talking to 3rd party devices or services that use XML formatting for their data.

[Usage](javascript:void(0))

To use LuaXML, add the following line to your script:

`LuaXML = require("LuaXML")`

**Note:** LuaXML consists of a lua file `(LuaXML.lua)` and a shared library `(.dll/.so)`, although a static linking is possible as well. Both parts are imported by this call provided they are found in Lua's package search path.

[Examples](javascript:void(0))

[Example 1: Import LuaXML module](javascript:void(0))

```lua
-- import the LuaXML module  
require("LuaXML")  
-- load XML data from file "test.xml" into local table xfile  
local xfile = xml.load("test.xml")  
-- search for substatement having the tag "scene"  
local xscene = xfile:find("scene")  
-- if this substatement is found...  
if xscene ~= nil then  
  --  ...print it to screen  
  print(xscene)  
  --  print attribute id and first substatement  
  print( xscene.id, xscene[1] )  
  -- set attribute id  
  xscene["id"] = "newId"  
end
```

[Example 2: Creating a New XML Object](javascript:void(0))

```lua
-- create a new XML object and set its tag to "root"  
local x = xml.new("root")  
-- append a new subordinate XML object, set its tag to "child", and its content to 123  
x:append("child")[1] = 123  
print(x
```

[function xml.new()](javascript:void(0))

Creates a new LuaXML object.

### Syntax

value = function xml.new(*arg*)

### Arguments

*arg*: (Optional) A table to be converted to a LuaXML object, or the tag of the new LuaXML object.

### Returns

Returns a new LuaXML object.

### Errors

* When passed value is not (convertable to) string.

[function xml.append()](javascript:void(0))

Appends a new subordinate LuaXML object to an existing one, optionally sets tag.

### Syntax

value = function xml.append(*var*, *tag*)

### Arguments

*var*: The parent LuaXML object.

*tag*: (Optional) The tag of the appended LuaXML object.

### Returns

Returns appended LuaXML object.

Returns `nil` in case of error.

### Errors

* When passed value is not (convertable to) string.

[function xml.children()](javascript:void(0))

Iterate subelements (âXML childrenâ) as key â value pairs.

### Syntax

value = function xml.children(*var*, *tag*, *key*, *value*, *maxdepth*)

### Arguments

*var*: The table (LuaXML object) to work on

*tag*: (Optional) XML tag to be matched

*key*: (Optional) Attribute key to be matched

*value*: (Optional) Attribute value to be matched

*maxdepth*: (Optional number) Maximum depth allowed, defaults to 1 (only immediate children). You can pass 0 or `true` to iterate *all* children recursively.

### Returns

Lua iterator function and initial state (Lua-internal use) â suitable for a `for` loop a if successful.

### Errors

* When passed value is not (convertable to) string.

[function xml.decode()](javascript:void(0))

Converts a string from XML encoding.

### Syntax

value = function xml.decode(*str*)

### Arguments

*str*: String to be transformed.

### Returns

Returns the decoded string if successful.

### Errors

* When passed value is not (convertable to) string.

[function xml.encode()](javascript:void(0))

Converts a string to XML encoding.

### Syntax

value = function xml.encode(*str*)

### Arguments

*str*: String to be transformed.

### Returns

Returns the XML-encoded string if successful.

### Errors

* When passed value is not (convertable to) string.

[function xml.interate()](javascript:void(0))

Iterates a LuaXML object, invoking a callback function for all matching (sub)elements.

### Syntax

value = function xml.interate(*var*, *cb*, *tag*, *key*, *value*, *r*, *max*, *d*)

### Arguments

*var*: The table (LuaXML object) to iterate

*cb*: Callback function. `callback(var, depth)` will be called for each matching element. The function may return `false` to request a stop; if its result is any other value (including `nil`), the iteration will continue.

*tag*: (Optional) XML tag to be matched.

*key*: (Optional) Attribute key to be matched.

*value*: (Optional) Attribute value to be matched.

*r*: (Optional boolean) Recursive operation. If `true`, also iterate over the subelements of `var`.

*max*: (Optional number) Maximum depth allowed.

*d*: (Optional number) Initial depth value, defaults to 0.

### Returns

The function returns two values: a counter representing the number of elements that were successfully matched (and processed), and a boolean completion flag. The latter is `true` for an exhaustive iteration, and `false` if was stopped from the callback.

### Errors

* When passed value is not (convertable to) string.

[function xml.match()](javascript:void(0))

Match XML entity against given (optional) criteria.

**Note:** If you want to test for a specific attribute `value`, you also have to supply a `key` â otherwise `value` will be ignored.

### Syntax

value = function xml.match(*var*, *tag*, *key*, *value*)

### Arguments

*var*: The variable to test, normally a Lua table or LuaXML object. (If `var` is not a table type, the test always fails).

*tag*: (Optional) If set, has to match the XML tag (i.e. must be equal to the `tag(var, nil)` result).

*key*: (Optional) If set, a corresponding attribute key needs to be present (exact name match).

*value*: (Optional) Arbitrary Lua value. If set, the attribute value for `key` has to match it.

### Returns

Returns the `var` argument converted to a LuaXML object, equivalent to `xml.new(var)` if successful.

Returns `nil` in case of error.

### Errors

* When passed value is not (convertable to) string.

[function xml.load()](javascript:void(0))

Loads XML data from a file and returns it as table.

### Syntax

value = function xml.load(*filename*)

### Arguments

*filename*: The name and path of the file to be loaded.

### Returns

Returns a Lua table containing the XML data if successful.

Returns `nil` in case of error.

### Errors

* When passed value is not (convertable to) string.

[function xml.save()](javascript:void(0))

Saves a Lua var as XML file.

### Syntax

value = function xml.save(*var*, *filename*)

### Arguments

*var*: The variable to be saved

*filename*: The filename to be used.

### Returns

Returns a Lua table containing the XML data if successful.

Returns `nil` in case of error.

**Note:** An existing file of the same name gets overwritten

### Errors

* When passed value is not (convertable to) string.

[function xml.eval()](javascript:void(0))

Converts an XML string to a Lua table.

### Syntax

value = function xml.eval(*xmlstring*)

### Arguments

*xmlstring*: The string to be converted.

### Returns

Returns a Lua table containing the XML data if successful.

Returns `nil` in case of error.

### Errors

* When passed value is not (convertable to) string.

[function xml.tag()](javascript:void(0))

Sets or returns tag of a LuaXML object.

### Syntax

value = function xml.tag(*var*, *tag*)

**Note:** LuaXML stores the tag value of an XML statement at table index 0, so it can be accessed or altered by `var[0]` or `var[xml.TAG]`.

### Arguments

*var*: The variable whose tag should be accessed.

*tag*: (Optional) The new tag to be set.

### Returns

*var*: Returns a LuaXML object.

*tag*: Returns the current tag as string.

### Errors

* When passed value is not (convertable to) string.

[function xml.str()](javascript:void(0))

Converts any Lua var to an xml string.

### Syntax

value = function xml.str(*var*, *indent*, *tag*)

### Arguments

*var*: The variable to be converted.

*indent*: (Optional) The current level of indentation for pretty output.

*tag*: (Optional) The tag to be used for a table without tag.

### Returns

Returns an XML string if successful.

Returns `nil` in case of error.

### Errors

* When passed value is not (convertable to) string.

[function xml.find()](javascript:void(0))

Recursively parses a Lua table for a substatement fitting to the provided tag and attribute.

### Syntax

value = function xml.find(*var*, *tag*, *attributeKey*, *attributeValue*)

### Arguments

*var*: The table to be searched in.

*tag*: (Optional) The XML tag to be found.

*attributeKey*:(Optional) The exact attribute to be found.

*attributeValue*: (Optional) The attribute value to be found.

### Returns

Returns the first (sub-)table which matches the search condition.

Returns `nil` in case of errors.

### Errors

* When passed value is not (convertable to) string.

[function xml.registerCode()](javascript:void(0))

Registers a custom code for the conversion between non-standard characters and XML character entities.

### Syntax

value = function xml.registerCode(*decoded*, *encoded*)

### Arguments

*decoded*: The character (sequence) to be used within Lua.

*encoded*:The character entity to be used in XML.

**Note:** By default, only the most basic entities are known to LuaXML (" & < > ')

Portions of this topic are reprinted under permission of the [LuaXML](../../Legal.htm#LuaXML) license.
