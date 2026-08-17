# Byte

Name:

Byte

Syntax:

INTEGER Byte(STRING SOURCE, INTEGER SOURCE_BYTE);

Description:

Returns the integer equivalent of the byte at position SOURCE_BYTE within a SOURCE string.

Parameters:

SOURCE is a STRING of characters. Each character in SOURCE is considered one byte.

SOURCE_BYTE references a character in the SOURCE string. The leftmost character in SOURCE is considered 1.

Return Value:

An integer containing the ASCII numeric value of the byte at position SOURCE_BYTE in the string SOURCE. If SOURCE_BYTE is greater than the length of the SOURCE string or is 0, 65535 is returned.

Example:

This piece of code will examine an input string to make sure that it starts with STX character (02). From there, it will test the second byte and process different command types accordingly.

STRING_INPUT IN$[100];

CHANGE IN$

{

IF(BYTE(IN$,1) = 02)

{

SWITCH(BYTE(IN$,2))

{

CASE (65):

{

// Process Command type 65 (A) here.

}

CASE (66):

{

// Process Command type 66 (B) here.

}

}

}

}

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/BYTE.htm*
