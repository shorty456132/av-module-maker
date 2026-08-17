# REMOVE

STRING Lower(STRING SOURCE);# Remove

Name:

Remove

Syntax:

STRING Remove(STRING DELIMITER, STRING SOURCESTRING, [INTEGER STARTPOS]);

Description:

Begins searching a string <SOURCESTRING> for the <DELIMITER> at the specified starting position <STARTPOS>, then removes all characters from the beginning of the string <SOURCESTRING> up to and including the delimiter. Returns a string containing all of the removed characters.

Parameters:

DELIMITER is a string containing the terminating sequence of characters in the desired string.

SOURCESTRING is the string the Remove function is performed on. Characters up to and including the DELIMITER are removed and returned as a string.

STARTPOS is the starting position in the <SOURCESTRING> to start searching for the <DELIMITER>. It is 1 based. The first byte of <SOURCESTRING> is at position 1.

Return Value:

A string including the delimiter.

Example:

BUFFER_INPUT SOURCE$[50];

STRING OUTPUT$[50];

CHANGE SOURCE$

{

OUTPUT$ = REMOVE("abc", SOURCE$);

}

In this example, if SOURCE$ were "testabc123", then OUTPUT$ would be "testabc" and SOURCE$ would contain "123".

BUFFER_INPUT SOURCE$[50];

STRING OUTPUT$[50];

CHANGE SOURCE$

{

OUTPUT$ = REMOVE("abc", SOURCE$, 6);

}

If SOURCE$ were "testabcabc123", then OUTPUT$ would be "testabcabc" and SOURCE$ would contain "123".

Version:

SIMPL+ Version 3.02.02 or later

CUZ 3.137 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/REMOVE.htm*
