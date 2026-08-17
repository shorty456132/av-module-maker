# UpperChar

Name:

UpperChar

Syntax:

INTEGER UpperChar(INTEGER character);

Description:

Converts the given character to upper case, so long as the character is between 'a' (0x61) and 'z' (0x7A).

Parameters:

Value is an INTEGER character: The character to convert to upper case.

Return Value:

The character converted to upper case. If the character is not a lower case character, the same character is returned. 

Example:

INTEGER Converted1, Converted2;

Converted1 = UpperChar('a');

Converted2 = UpperChar('5');

Print("Converted1=%c, Converted2=%c\n", Converted1, Converted2);

Converted1=A (this is returned if the converted character was a lower case character).

Converted2=5 (this would be returned if the character to be converted was not a lower case character).

Version:

SIMPL+ Version 2.10.00 or later

CUZ 3.137 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/UpperChar.htm*
