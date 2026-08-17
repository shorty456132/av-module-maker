# RemoveByLength

Name:

RemoveByLength

Syntax:

STRING RemoveByLength(INTEGER NUMBYTES, STRING SOURCESTRING);

Description:

Removes all characters from the beginning of the string <SOURCESTRING> up to the NumBytes specified. Returns a string containing the number of bytes removed.

Parameters:

SOURCESTRING is the string the RemoveByLength function is performed on. Characters up to the NumBytes are removed and returned as a string.

NUMBYTES is an integer specifying the number of characters to be removed from a SOURCESTRING. The bytes are removed starting at the first character (position 1) in the <SOURCESTRING)

Return Value:

If the length of <SOURCESTRING> is 0, a string of length 0 is returned.

If the length of <SOURCESTRING> is < <NUMBYTES>, then <SOURCESTRING> is not modified and a string of 0 length will be returned.

If the length of <SOURCESTRING> is >= <NUMBYTES>, then the first <NUMBYTES> of <SOURCESTRING> will be returned. <SOURECESTRING> is left with the rightmost LEN(<SOURCESTRING>)-<NUMBYTES> characters.

Example:

BUFFER_INPUT SOURCE$[50];

STRING OUTPUT$[50];

CHANGE SOURCE$

{

OUTPUT$ = REMOVEBYLENGTH(2, SOURCE$);

}

In this example, if SOURCE$ were "testabc123", then OUTPUT$ would be "te" and SOURCE$ would contain "stabc123".

Version:

SIMPL+ Version 3.02.05 or later

CUZ 3.154 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/RemoveByLength.htm*
