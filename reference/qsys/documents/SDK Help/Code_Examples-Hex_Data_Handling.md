# Handling Hex and Binary Data

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Hex_Data_Handling.htm

# Handling Hex and Binary Data

Lua scripts often encounter hex or binary data coming from remote devices. Handling this data effectively is achieved by planning the context of how the data is formatted, which avoids inconsistencies and confusion.

Received data from the TCPSocket, UDPSocket, and Serial objects is formatted as ASCII characters and wrapped in a string. The data is stored sequentially as received and each character represents one byte (0-255 decimal).

A byte value encoded as a character in a string can be input as a hex-encoded escape character, a decimal value escape character, a character, or encoded from a number using the string.char function:

â\x41â == â\65â == âAâ = string.char(65) == string.char(0x41)

The same byte can be encoded as a number using hex notation or decimal notation, translated from a character to a numerical byte:

0x41 == 65 == string.byte(âAâ)

Translating this byte data into a readable format (strings or numbers) is a common task. This allows the non-printable characters in the string of bytes to be used more effectively. The following helper functions support these tasks.

[Hex Handling Helper Functions](javascript:void(0))

```lua
--Convert a string's bytes to a string of human readable hex encoded value pairs  
function hex2str(str)  
  return str:gsub(".",  
    function(byte)  
      return string.format("%02X", string.byte(byte))  
    end  
  )  
end  
  
--Translate a string of 2 character hex values (human readable) to a string of character encoded bytes  
function str2hex(str)  
  return str:gsub("..",   
    function(byte)   
      return string.char( tonumber(byte,16) )   
    end  
  )  
end  
  
--Return a numerical equivalent of the bytes within the string  
--Note that a maximum of 7 bytes can be converted by this function before the number will overflow  
function hex2num(str)  
  local value = 0  
  if str:len()>0 then  
    for i=1,str:len() do  
      value = str:byte(i) + (value << 8)  
    end  
  end  
  return value  
end  
  
--Return a string of bytes equivalent to the numerical value  
function num2hex(val)  
  local str = ""  
  while val > 0 do  
    str = string.char(val % 256) .. str   
    val = val >> 8  
  end  
  return str  
end  
  
--String conversion test  
local data = "\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x21"  
print(data)           --> Hello World!  
data = hex2str(data)  
print(data)           --> 48656C6C6F20576F726C6421  
print(str2hex(data))  --> Hello World!  
  
--Number conversion test  
data = "\xDE\xCA\xFB\xAD"  
print(data)           --> ????   (4 unprintable characters)  
print(hex2str(data))  --> DECAFBAD  
data = hex2num(data)  
print(data)           --> 3737844653  
data = num2hex(data)  
print(hex2str(data))  --> DECAFBAD
```

This encode/decode string function uses gsub to replace byte values with the %20X format of the value the character represents. This is a 2 digit capital letter (00-FF) representation of the value. tonumber() is used to decode this as a base 16 number back into a single character encoded value.

Casting these bytes of data into Lua numbers allows the use of bitwise operators:

* &: bitwise AND
* |: bitwise OR
* ~: bitwise exclusive OR
* >>: right shift
* <<: left shift
* ~: unary bitwise NOT

Single bytes can be translated using string.char and string.byte functions. For multiple byte values, num2hex() and hex2num() translation supports up to 7 bytes.

These conversions can be changed within the helper functions if the needed translation differs from those implemented here.

Within Q-SYS designs, the input boxes encode the userâs input with escape characters. If the intended use of a text box in a text control, control script, or plugin is to receive the encoded character, the following decode script will encode the escape sequences into the appropriate character. The supported characters of this script are the c-escape strings generally supported by Lua: \x?? hex, \### decimal, \a, \b, \f, \r, \n, \t, \v.

[Escape Character Encoding from Q-SYS Text Inputs](javascript:void(0))

```lua
-- A lookup table for decimal representation of hex value characters  
HexValues = {}   
HexValues["0"]=0   
HexValues["1"]=1  
HexValues["2"]=2   
HexValues["3"]=3  
HexValues["4"]=4  
HexValues["5"]=5  
HexValues["6"]=6  
HexValues["7"]=7  
HexValues["8"]=8  
HexValues["9"]=9  
HexValues["a"]=10  
HexValues["A"]=10  
HexValues["b"]=11  
HexValues["B"]=11  
HexValues["c"]=12  
HexValues["C"]=12  
HexValues["d"]=13  
HexValues["D"]=13  
HexValues["e"]=14  
HexValues["E"]=14  
HexValues["f"]=15  
HexValues["F"]=15  
  
--Convert the escape sequences within a string to the character (lua, excape character is "\").    
--Supports converting \x?? hex, \### decimal, \a, \b, \f, \r, \n, \t, \v sequences.  
--Improperly formatted values are left as characters within the string.  
function EscapeSequenceEncode(str)  
  local result = ""  -- Encoded string  
  local last = 0     -- Pointer to end of processed string data  
  local index = 1    -- Pointer to current proceesing data  
  local nextEsc = str:find("\\")  -- Pointer to the next escape character  
  while nextEsc ~= nil do  
    -- Move the data between the escape characters into the result and index the pointers  
    index = index + nextEsc - 1  
    result = result .. str:sub(last+1, index-1)  
    last = index - 1  
    index = index + 1  
      
    -- Double \  
    if str:byte(index) == 92 then  
      result = result .. string.char(92)  
      last = index  
      --skip past the second \  
      index = index + 1  
    -- Hex value (of the form \x?? where ? is from 0-F)  
    elseif str:byte(index) == 120 or str:byte(index) == 88 then  
      msb = HexValues[ str:sub(index+1, index+1) ]  
      lsb = HexValues[ str:sub(index+2, index+2) ]  
      if msb~=nil and lsb~=nil then  
        result = result .. string.char(msb*16 + lsb)  
        last = index + 2  
      end  
    -- \a Bell character  
    elseif str:byte(index) == 97 then  
      result = result .. string.char(7)  
      last = index  
    -- \b Backspace character  
    elseif str:byte(index) == 98 then  
      result = result .. string.char(8)  
      last = index  
    -- \f Formfeed character  
    elseif str:byte(index) == 102 then  
      result = result .. string.char(12)  
      last = index  
    -- \r Carriage return  
    elseif str:byte(index) == 114 then  
      result = result .. string.char(13)  
      last = index  
    -- \n Newline/Linefeed  
    elseif str:byte(index) == 110 then  
      result = result .. string.char(10)  
      last = index  
    -- \t Horizontal tab  
    elseif str:byte(index) == 116 then  
      result = result .. string.char(9)  
      last = index  
    -- \v Vertical tab  
    elseif str:byte(index) == 118 then  
      result = result .. string.char(11)  
      last = index  
    -- Decimal input (\### where ### is between 0 and 255 decimal number)  
    elseif str:byte(index) ~= nil and str:byte(index) > 47 and str:byte(index) < 58 then  
      octal = str:byte(index) - 48  
      index = index + 1  
      -- Each digit is optional, check for a numerical value in each of the 3 characters after the \  
      if str:byte(index) ~= nil and str:byte(index) > 47 and str:byte(index) < 58 then  
        octal = octal * 10 + ( str:byte(index) - 48 )  
        index = index + 1  
        if str:byte(index) ~= nil and str:byte(index) > 47 and str:byte(index) < 58 then  
          octal = octal * 10 + ( str:byte(index) - 48 )  
          index = index + 1  
        end  
      end  
      --Add the character if the octal value is valid (if not the string will be added as is on the next iteration)  
      if octal > -1 and octal < 256 then  
        result = result .. string.char(octal)  
        last = index  
      end  
    end  
      
    -- Find the next escape character  
    nextEsc = str:sub(index, -1):find("\\")  
  end  
    
  --Append any data after the last escape character and return the encoded string  
  return result .. str:sub(last+1, -1)  
end
```

**Note:** Command Buttons already support hex encoding, as [documented here.](https://q-syshelp.qsc.com/Content/Schematic_Library/command_buttons.htm)
