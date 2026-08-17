# GetC

Name:

GetC

Syntax:

INTEGER GetC(BUFFER_INPUT SOURCE);

Description:

Returns the value at position 1 of SOURCE string and shifts the rest of the buffer up by one. In this way, values may be picked out of a buffer for processing.

Parameters:

SOURCE is typically from a BUFFER_INPUT statement. It may be defined as a STRING or STRING_INPUT, but since GETC removes characters from SOURCE, the result is destructive to the source string.

Return Value:

An INTEGER containing a single character from position 1 of the buffer.

If there are no characters in the buffer for GETC to retrieve, then the value of 65535 is returned.

Example:

In this example, a buffer input is read until the character "A" is retrieved.

BUFFER_INPUT IN$[100];

INTEGER INCHAR;

CHANGE IN$

{

INCHAR = 0;

WHILE(INCHAR <> 'A')

INCHAR = GETC(IN$);

// continue processing.

}

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/GETC.htm*
