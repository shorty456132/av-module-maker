# RapidJSON

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/RapidJSON.htm

# RapidJSON

Use the RapidJSON module to quickly encode and decode large Lua tables to and from JSON documents (strings). This may be useful in cases where an API is expecting a JSON string (instead of tables), or if you want to convert a Lua table of values into a string that can then be saved in a control value.

**Tip:** RapidJSON is similar to the standard [JSON](JSON.htm) module, but can handle large amounts of data without risk of raising execution count errors. For this reason, it is recommended to use the RapidJSON module instead of the JSON module.

[Usage](javascript:void(0))

To use the RapidJSON module, add the following line to your script:

rapidjson = require("rapidjson")

**Note:** You can assign any local variable name to the `require("rapidjson")` object.

[Name and Version](javascript:void(0))

Returns the RapidJSON name or version.

### rapidjson.\_NAME

A string that is `"rapidjson"`.

### rapidjson.\_VERSION

The current loaded rapidjson version. `"scm"` when not built with luarocks.

[rapidjson.encode()](javascript:void(0))

Encode a Lua table to JSON string. JSON object keys are sorted by this function.

The function supports the following types:

* boolean
* rapidjson.null (it is actually a function)
* number
* string
* table

The function does not support:

* Q-SYS Controls
* Serialport, TcpSocket, UdpSocket, Timer objects, etc.

### Syntax

string = rapidjson.encode(*value* [, *option*])

### Arguments

#### value:

When passed as a table:

1. it is encoded as JSON array if:
   * meta field `__jsontype` set to `array`.
   * table contains length > 0.
2. otherwise the table is encoded as JSON object and non string keys and its values are ignored.

When passed with `true`, `false`, number and `rapidjson.null`, simply encode as a simple JSON value.

#### option:

A optional table contains the following field:

* `pretty` boolean: Set `true` to make output string to be pretty formated. Default is `false`.
* `sort_keys` boolean: Set `true` to make JSON object keys be sorted. Default is `false`.
* `empty_table_as_array` boolean: Set `true` to make empty table encode as JSON array. Default is `false`.

### Returns

JSON string on success. Returns nil on failure, plus an error message as a second result.

### Errors

* When option passed a value other than table.

### Examples

[Example 1: Usage variants](javascript:void(0))

```lua
local rapidjson = require('rapidjson')  
  
print( rapidjson.encode({}) ) -- '{}'  
print( rapidjson.encode(rapidjson.object()) ) --> '{}'  
print( rapidjson.encode(rapidjson.array()) ) --> '[]'  
print( rapidjson.encode(setmetatable({}, {__jsontype='object'})) ) --> '{}'  
print( rapidjson.encode(setmetatable({}, {__jsontype='array'})) ) --> '[]'  
print( rapidjson.encode(true) ) --> 'true'  
print( rapidjson.encode(rapidjson.null) ) --> 'null'  
print( rapidjson.encode(123) ) --> '123.0' or '123' in Lua 5.3.  
print( rapidjson.encode({true, false}) ) --> '[true, false]'  
print( rapidjson.encode({a=true, b=false}) ) --> '{"a":true,"b":false]'
```

Debug Output

```lua
{}
{}
[]
{}
[]
true
null
123
[true,false]
{"a":true,"b":false}
```

[Example 2: Sort object keys](javascript:void(0))

```lua
rapidjson = require("rapidjson")  
  
function TablePretty(tbl,sort)  
  return rapidjson.encode(tbl,{ pretty=true, sort_keys=sort })  
end  
test = {  
  ["Top Level Item"]={  
    Value=math.pi,  
    Str="String",  
    Options={1,2,3,4} -- an "array"  
  }  
}  
print(TablePretty(test,true))
```

#### Debug Output

```lua
{
    "Top Level Item": {
        "Options": [
            1,
            2,
            3,
            4
        ],
        "Str": "String",
        "Value": 3.141592653589793
    }
}
```

[rapidjson.decode()](javascript:void(0))

Decode JSON to a Lua table.

### Syntax

value = rapidjson.decode(*jsonstring*)

### Arguments

*jsonstring* : A JSON value string to be decoded.

### Returns

Return table if JSON is an object or array.

Return `true`, `false`, number and `rapidjson.null` respectively if JSON is a simple value.

Return nil plus an error message as a second result when passed string is not a valid JSON.

### Errors

* When passed value is not (convertable to) string.

[rapidjson.load()](javascript:void(0))

Load JSON file into Lua table.

### Syntax

value = rapidjson.load(*filename*)

### Arguments

*filename* : The JSON file to be loaded.

### Returns

Return table if file contains an object or array.

Return `true`, `false`, number and `rapidjson.null` respectively if file contains a simple value.

Return nil plus an error message as a second result when passed file is not valid JSON file.

### Errors

* When passed filename is not (convertible to) string.

[rapidjson.Document()](javascript:void(0))

Creates a rapidjson Document object. Optionally create from a Lua table or string of JSON document.

### Syntax

doc = rapidjson.Document(*t*|*s*)

### Arguments

*t* : Optional table to be create a rapidjson Document from.

*s* : Optional a string contains a JSON document, then when document created the string is parsed into the document.

[document:parse()](javascript:void(0))

Parse JSON document contained in string s.

### Syntax

local ok, message = document:parse(*s*)

### Arguments

*s* : A string contains a JSON document.

### Returns

Returns `true` on success.

Returns `false` and additional error message when failed.

### Example

```lua
local rapidjson = require('rapidjson')  
local doc = rapidjson.Document()  
local ok, message = doc:parse('{"a":["appke", "air"]}')  
if not ok then  
  print(message)  
end
```

[document:get()](javascript:void(0))

Get document member by JSON Pointer.

### Syntax

Local value = document:get(*pointer*[, *default*])

### Arguments

*pointer* : A string contains JSON pointer.

*default* : The default value to return if the document does not contains value specified by the pointer.

### Returns

If the document has elements specified by pointer, the element value is returned as a Lua value. Otherwise `default` value is returned.

Returns `nil` if `default` is not specified.

[document:set()](javascript:void(0))

Set document member by JSON Pointer with specified value.

### Syntax

document:set(*pointer*, *value*)

### Arguments

*pointer* : A string contains JSON pointer.

*value* : The value to set as new value for document element specified by pointer.

### Example

```lua
local doc = rapidjson.Document()  
doc:set('/a', {'apple', 'air'})
```

[rapidjson.dump()](javascript:void(0))

Dump a Lua value to a JSON file.

### Syntax

success, err = rapidjson.dump(*value*, *filename* [, *option*])

### Arguments

*value* : Same as in `rapidjson.encode()`.

*filename* : The file path string where to save the rapidjson string.

*option* : Same as in options in `rapidjson.encode()`.

### Example

```lua
local rapidjson = require('rapidjson')  
  
rapidjson.dump({rapidjson.null}, 'media/test.json')  
rapidjson.dump({rapidjson.null}, 'media/test-pretty.json', {pretty=true})
```

**Note:** For security and stability reasons, the `media/` folder and `design/` folder and their subfolders are the only locations within the file system accessible by the Lua libraries.

[rapidjson.null](javascript:void(0))

The placeholder for null values in rapidjson.

### Example

```lua
local rapidjson = require('rapidjson')  
  
rapidjson.decode('[null]') --> {rapidjson.null}  
rapidjson.encode({rapidjson.null}) --> '[null]'
```

[rapidjson.object()](javascript:void(0))

Create a new empty table that has the metatable field `__jsontype` set as `'object'` so that the `encode` and `dump` function will encode it as a JSON object.

When passed a valid table:

* Passed table does not have metatable - just set above metatable for the table.
* Passed table already has metatable - set the metatable field `__jsontype` to `'object'`.

### Synopsis

obj = rapidjson.object([*t*])

### Arguments

*t* : Optional table to set the metatable with meta field `__jsontype` set as `'object'`.

### Returns

Origin passed in table when passed with a table. Or new created table.

[rapidjson.array()](javascript:void(0))

Same as rapidjson.object(), except the metatable field `__jsontype` is set as `'array'`. The `encode` and `dump` function will encode it as JSON array.

See rapidjson.object() for usage.

[rapidjson.SchemaDocument()](javascript:void(0))

Creates a SchemaDocument from Document or a Lua table or a string contains a JSON schema.

### Syntax

local sd = rapidjson.SchemaDocument(*doc*|*t*|*s*)

### Arguments

*doc* : The the JSON schema stored in rapidjson.Document object.

*t* : The Lua table representation of a JSON schema.

*s* : The string contains a JSON schema.

### Returns

Returns the new SchemaDocument object.

### Example

```lua
local d = rapidjson.Document('{"type": ["string", "number"]}')  
local sd = rapidjson.SchemaDocument(d)
```

[rapidjson.SchemaValidator()](javascript:void(0))

Creates a SchemaValidator from a Schema Document

### Syntax

local validator = apidjson.SchemaValidator(*sd*)

### Arguments

*sd* : The SchemaDocument to create the validator. SchemaDocument can be shared by schema validators.

### Returns

Returns the new created validator object.

### Example

```lua
local sd = rapidjson.SchemaDocument('{"type": ["string", "number"]}')  
local validator = rapidjson.SchemaValidator(sd)  
  
local d = rapidjson.Document('.....')  
  
local ok, message = validator:validate(d)
```

[SchemaValidator:validate()](javascript:void(0))

Validates a JSON document.

### Syntax

local ok, message = validator:validate(*d*)

### Arguments

*d* : The document to be validated against the schema stored inside the validator.

### Returns

Returns `true` if the document is valid.

Returns `false` and an extra error message if invalid.

Portions of this topic are reprinted under permission of the [lua-rapidjson](../../Legal.htm#lua-rapi) license.
