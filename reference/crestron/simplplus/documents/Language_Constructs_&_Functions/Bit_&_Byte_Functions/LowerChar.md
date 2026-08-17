# LowerChar

Name:

LowerChar

Syntax:

INTEGER LowerChar(INTEGER character);

Description:

Converts the given character to lower case, so long as the character is between 'A' (0x41) and 'Z' (0x5A).

Parameters:

Value is an INTEGER character: The character to convert to lower case.

Return Value:

The character converted to lower case. If the character is not an upper case character, the same character is returned. 

Example:

INTEGER Converted1, Converted2;

Converted1 = LowerChar('a');

Converted2 = LowerChar('5');

Print("Converted1=%c, Converted2=%c\n", Converted1, Converted2);

Converted1=a (this is returned if the converted character was an upper case character).

Converted2=5 (this would be returned if the character to be converted was not an upper case character).

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.137 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/LowerChar.htm*
