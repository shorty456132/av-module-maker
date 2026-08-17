# LowWord

Name:

LowWord

Syntax:

INTEGER LowWord(LONG_INTEGER Value);

Description:

Returns the lower 16 significant bits of a LONG_INTEGER.

Parameters:

Value is a LONG_INTEGER containing the lowermost 16 significant bits the user wants.

Return Value:

The lower 16 significant bits of Value.

Example:

Function main()

{

LONG_INTEGER x;

INTEGER y;

x=0xAABBCCDD;

y=LowWord(x);

print("The LowerMost 16 Bits of %08IX are %04X\n", x, y);

}

This will print: The UpperMost 16 bits of AABBCCDD are CCDD.

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.154 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/LowWord.htm*
