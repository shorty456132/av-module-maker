# JSON

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/JSON.htm

# JSON

Use the JSON module to encode and decode Lua tables to and from JSON strings.

**Note:** For faster performance, and to avoid raising execution count errors with large amounts of data, use [RapidJSON](RapidJSON.htm) instead.

To use the JSON module, add the following line to your script:

require("json")

[json.encode()](javascript:void(0))

Returns the Lua object JSON encoded into a string.

### Syntax

json.encode( *lua\_object* )

### Example

```lua
require("json")  
print (json.encode( { 1, 2, 'fred', {first='mars',second='venus',third='earth'} } ))
```

#### Debug Output

```lua
[1,2,"fred", {"first":"mars","second":"venus","third","earth"}]
```

[json.decode()](javascript:void(0))

Decodes the JSON encoded data structure, and returns a Lua object with the appropriate data.

### Syntax

json.decode( *json\_string* )

### Example

```lua
require("json")  
  
tbl = {"Thing 1", "Thing 2"}  
jsonstr = json.encode(tbl)  
print(jsonstr)  
tbl2 = json.decode(jsonstr)  
  
print(table.concat(tbl2,","))
```

#### Debug Output

```lua
["Thing 1","Thing 2"]
Thing 1,Thing 2
```

[json.null()](javascript:void(0))

Returns a unique value that will be encoded as a null in a JSON encoding.

### Example

This is necessary in one situation. In Lua, if a key in a table has a `nil` value, the key is simply discarded (since any non-existent key has a nil value). The encoding of arrays has been built to manage this nil-values in arrays, but associative arrays provide a problem. For example:

```lua
t = { user="test", password=nil }
```

Since Lua simply discards the password key, JSON4Lua encodes this as the JSON string.

```lua
{"user":"test"}
```

If your system requires a defined null value, use the following code:

```lua
t = { user="test", password=json.null }
```

This will now correctly encode to:

```lua
{"user":"test","password":null}
```

Incidentally, `json.null` is simply a function that returns itself, so that you can use either `json.null` or `json.null()` as desired.

Portions of this topic are reprinted under permission of the [JSON4Lua](../../Legal.htm#JSON4Lua) license.
