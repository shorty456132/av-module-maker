# HighWord

Name:

HighWord

Syntax:

INTEGER HighWord(LONG_INTEGER Value);

Description:

Returns the upper 16 significant bits of a LONG_INTEGER.

Parameters:

Value is a LONG_INTEGER containing the uppermost 16 significant bits the user wants.

Return Value:

The upper 16 significant bits of Value.

Example:

Function main()

{

LONG_INTEGER x;

INTEGER y;

x=0xAABBCCDD;

y=HighWord(x);

print("The UpperMost 16 Bits of %08IX are %04X\n", x, y);

}

This will print: The UpperMost 16 bits of AABBCCDD are AABB.

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.154 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/HighWord.htm*
