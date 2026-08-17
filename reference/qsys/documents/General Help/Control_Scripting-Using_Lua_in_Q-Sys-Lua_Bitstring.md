# Lua bitstring

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Lua_Bitstring.htm

# Lua bitstring

Bitstring is useful for network protocol programming and for manipulation of bit based file formats. It provides conversion of strings to binary and hexadecimal formats.

[Usage](javascript:void(0))

To use the bitstring module, add the following line to your script:

require "bitstring"

[Substring Parameters](javascript:void(0))

Substring parameters allow you to handle different parts of the same string parameter in consecutive invocations, thus making most parsing tasks more efficient.

Substring parameters specify substring that starts at `start` and ends at `end` inclusively. Parameters may be negative. 1, -1 specify the whole string.

Substring parameters behave similarly to `string.Fsub` parameters; however, it is illegal for `start` or `end` to be out of bounds.

[Format Specification](javascript:void(0))

The format string passed to pack / unpack function consists of elements separated by a coma and optional white space. Each element specifies a value that is packed or unpacked, its size, type, and endianess. These element parts are delimited by '**:**'. Examples of this would include:

```lua
format ::= element | element-list  
--  
element ::= size ':' type ':' [endianess]  
--  
size ::= number | all | rest  
--  
type ::= int | bin | float  
--  
endianess ::= big | little  
--  
element-list ::= element element-delimiter element-list [ element-delimiter ]  
--  
element-delimiter ::= [' ' | '\t' | '\n' ] ',' [' ' | '\t' | '\n' ]
```

[bitstring.pack()](javascript:void(0))

Pack one or more elements as specified by format or by bitmatch into regular Lua string.

### Syntax

bitstring.pack(*format*, *arg1* [, *arg2*, *argn*])

### Arguments

*format*: Packs one or more elements as specified by format.

*bitmatch*: Variables holding values to be packed.

### Returns

Returns a regular Lua string.

Returns nil in case of error.

### Example

```lua
local data = bitstring.pack( "8:int, 8:int, 8:int, 8:int, 8:int", v1, v2, v3, v4, v5).
```

**Note:** v1-v5 are variables.

[bitstring.unpack()](javascript:void(0))

Unpack one or more elements as specified by format or by bitmatch and return them as multiple values. Substring of `s` may be specified by start and end parameters.

### Syntax

bitstring.unpack(*format*, *bitstring*)

### Arguments

*format*: String representing how the data is to be unpacked. The string contains one or more elements. Each element is made of two parts and; a number representing the number of bits then a variable type. value options are `int`, `bin` or `float`. You can also optionally specify the endianness of the data with `big` or `little`. For example `3:int` will take three bits as an integer, `8:int:little` would be 8 bits converted to an integer with little endianness.

*bitstring*: Variable containing the bitstring data.

### Returns

Returns result1 [, result2, resultn]

Returns nil in case of error.

### Example

```lua
-- parse-radius.lua   
-- This example demonstrates parsing and creation of RADIUS protocol messages  
-- using bitstring.pack and bitstring.unpack. It also uses bitstring.hexstream  
-- and bitstring.fromhexstream utility functions that ease on debugging.  
-- RADIUS protocol is defined in RFC 2865.  
-- ---------------------------------------  
  
-- copied from wireshark  
packet = "01e40088abe03a1b2b38bbd7edcf08b26334f417010867696f7261300c06000005781e10303034302e393661302e343931301f10303034302e393662312e653036330606000000015012efbdb1bd5e4fe4147a95a78d001c51844f0d0202000b0167696f7261303d06000000130506000044f504060a383e83200f63642d617031313230622d3031"  
  
radis_message = bitstring.fromhexstream(packet)  
  
-- parse radius message  
code, identifier, message_length, authenticator, attributes =   
    bitstring.unpack("8:int, 8:int, 16:int:big, 16:bin, rest:bin", radis_message)  
  
attribute_list = {}  
while(#attributes > 0) do  
    number, length, attributes = bitstring.unpack("8:int, 8:int, rest:bin", attributes)  
    value, attributes  = bitstring.unpack((length - 2) .. ":bin, rest:bin", attributes)  
    table.insert(attribute_list, {number = number, length = length, value = value})  
end  
  
-- compose radius message  
attributes = {}  
for i, a in ipairs(attribute_list) do  
    attribute = bitstring.pack("8:int, 8:int, all:bin", a.number, a.length, a.value)  
    table.insert(attributes, attribute)  
end  
attributes = table.concat(attributes)  
  
composed_message_length = 20 + #attributes  
composed_radius_message = bitstring.pack("8:int, 8:int, 16:int:big, 16:bin, all:bin",  
    code, identifier, composed_message_length, authenticator, attributes)   
  
-- print results  
print("parsed radius message")  
print("code: ", code)  
print("identifier: ", identifier)  
print("radius message length: ", message_length)  
print("authenticator: ", bitstring.hexstream(authenticator))  
print("attributes:")  
  
for i, attribute in ipairs(attribute_list) do  
    print("--------------------------------------")  
    print("   number: ", attribute.number)  
    print("   length: ", attribute.length)  
    print("   value: ", bitstring.hexstream(attribute.value))  
end  
print("--------------------------------------")  
  
print("composed radius message")  
print(bitstring.hexstream(composed_radius_message))  
assert(composed_radius_message == radis_message)
```

[bitstring.compile()](javascript:void(0))

Compiles format into bitmatch object.

### Syntax

bitstring.compile(*format*)

### Arguments

*format*: Compiles format into bitmatch object.

### Returns

Returns bitmatch.

Returns nil in case of error.

[bitstring.bindump()](javascript:void(0))

Dump string into multi line âoffset â binary digits - textâ similar to xxd -b output. Useful for visually validating UTF-8 input.

### Syntax

bitstring.bindump(s [, *start*, *end*])

**Note:** Lines are separated by '**\n**'.

### Arguments

*s*: Dump string `s` into multi line âoffset â binary digits - textâ similar to xxd -b output.

*start*: Substring parameter specifying start.

*end*: Substring parameter specifying end.

### Returns

Returns a Lua string.

Returns nil in case of error.

[bitstring.hexdump()](javascript:void(0))

Dumps string into multi line, similar to xxd output.

### Syntax

bitstring.hexdump(s [, *start*, *end*])

### Arguments

*s*: Dump string `s` into multi line "offset - hexadecimal bytes - text".

*start*: Substring parameter specifying start.

*end*: Substring parameter specifying end.

### Returns

Returns a Lua string.

Returns nil in case of error.

### Example

```lua
print(bitstring.hexstream( status ))
```

[bitstring.binstream()](javascript:void(0))

Dumps string into single line binary digit stream.

### Syntax

bitstring.binstream(s [, *start*, *end*])

### Arguments

*s*: Dump string `s` into single line binary digit stream.

*start*: Substring parameter specifying start.

*end*: Substring parameter specifying end.

### Returns

Returns a Lua string.

Returns nil in case of error.

[bitstring.hexstream()](javascript:void(0))

Dumps string into single line hexadecimal digit stream.

### Syntax

bitstring.hexstream(s [, *start*, *end*])

### Arguments

*s*: Dump string `s` into single line hexadecimal digit stream.

*start*: Substring parameter specifying start.

*end*: Substring parameter specifying end.

### Returns

Returns a Lua string.

Returns nil in case of error.

[bitstring.frombinstream()](javascript:void(0))

Convert hexadecimal stream of bytes to regular Lua string.

### Syntax

bitstring.frombinstream(s [, *start*, *end*])

### Arguments

*s*: Convert string `s` into hexadecimal stream of bytes to regular Lua string.

*start*: Substring parameter specifying start.

*end*: Substring parameter specifying end.

### Returns

Returns a Lua string.

Returns nil in case of error.

[bitstring.fromhexstream()](javascript:void(0))

Convert hexadecimal stream of bytes to regular Lua string.

### Syntax

bitstring.fromhexstream(s [, *start*, *end*])

### Arguments

*s*: Convert string `s` into hexadecimal stream of bytes to regular Lua string.

*start*: Substring parameter specifying start.

*end*: Substring parameter specifying end.

### Returns

Returns a Lua string.

Returns nil in case of error.

Portions of this topic are reprinted under permission of the [Lua Bitstring](../../Legal.htm#NewBSD) license.
