# Data Conversion Functions Overview

These functions take one form of data (integer or string) and convert it to the opposite type in a given SIMPL+ program. Usually, these functions are for converting number stored in strings to integers, or for converting numbers stored in integers to strings.

Function |  Description  
---|---  
[ATOI](<ATOI.htm>) |  Converts a STRING to an INTEGER value.  
[ATOL](<ATOL.htm>) |  Converts a STRING to an LONG_INTEGER value.  
[Chr](<Chr.htm>) |  Takes the integer value specified and returns the corresponding ASCII character as a one-byte string.  
[HexToI](<HexToI.htm>) |  Returns the INTEGER value of Source. If Source exceeds 4 characters, the lower 4 characters of Source are used.   
[HexToL](<HexToL.htm>) |  Returns the LONG_INTEGER value of Source. If Source exceeds 8 characters, the lower 8 characters of Source are used.   
[HexToSI](<HexToSI.htm>) |  Returns the SIGNED_INTEGER value of Source. If Source exceeds 4 characters, the lower 4 characters of Source are used.   
[HexToSL](<HexToSL.htm>) |  Returns the SIGNED_LONG_INTEGER value of Source. If Source exceeds 8 characters, the lower 8 characters of Source are used.   
[ITOA](<ITOA.htm>) |  Takes the value in CODE and creates a string containing the string equivalent of that integer.  
[ITOAHex](<ITOHEX.htm>) |  Takes the value in CODE and creates a string containing the hexadecimal equivalent.  
[LtoA](<LtoA.htm>) |  Takes the value in CODE and creates a string containing the string equivalent of that LONG_INTEGER.  
[LtoHex](<LtoHex.htm>) |  Takes the value in CODE and creates a string containing the hexadecimal equivalent.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Data_Conversion_Functions/Overview.htm*
