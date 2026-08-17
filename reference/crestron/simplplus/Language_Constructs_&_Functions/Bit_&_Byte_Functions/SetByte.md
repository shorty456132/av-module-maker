# SetByte

Name:

SetByte

Syntax:

INTEGER SetByte(STRING SOURCE, INTEGER POSITION, INTEGER VALUE);

Description:

Sets the byte at the position given by POSITION in the string given by SOURCE to the value in VALUE.

Parameters:

SOURCE is a STRING of characters. Each character in SOURCE is considered one byte.

POSITION references a character in the SOURCE string. The leftmost character in SOURCE is considered 1. The only valid positions are 1 to LEN(SOURCE). Any other position is out of bounds and will return an error.

VALUE is the data to set the source string position to. If it is greater than 255, the lower 8 bits are used.

Return Value:

0 if success, -1 if failure.

Example:

function main()

{

STRING Text$[25];

INTEGER ReturnValue;

Text$="CPQ1704TKS";

ReturnValue = SetByte(Text$, 3, 'E');

if(ReturnValue <> 0)

{

print("Error, could not Set Byte at given position\n");

}

else

{

print("New String is: <%s>\n", Text$);

}

}

In this example, the output is "New String is: <CPE1704TKS>"

Version:

2-Series Only: SIMPL v2.10.10 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/SetByte.htm*
