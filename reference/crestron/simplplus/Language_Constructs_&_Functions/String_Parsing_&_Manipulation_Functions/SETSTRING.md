# SetString

Name:

SetString

Syntax:

For X Generation: INTEGER SetString(STRING SOURCE, INTEGER POSITION,

STRING DESTINATION);

For 2-Series: SIGNED_INTEGER SetString(STRING SOURCE,

INTEGER POSITION, STRING DESTINATION);

Description:

Overwrites the bytes in DESTINATION with the bytes in SOURCE starting at POSITION in the DESTINATION string. Performs an overwrite.

Parameters:

DESTINATION is a STRING containing the string to be modified.

POSITION is an INTEGER referencing the starting byte to write at in DESTINATION. 1 is the first byte of the string.

SOURCE is a STRING containing the string to use in the operation.

Return Value:

The new length or an error code, as defined below:

For the purposes of the explanation, a string has been declared STRING DESTINATION[MAX_LEN]. The string has a current length defined by LEN(DESTINATION).

e.g., If the specified position is beyond the declared length of the destination string:

If POSITION > MAX_LEN, no operation is performed and -8 is returned.

e.g., If the entire source string can't be inserted without exceeding the length of the destination string:

If POSITION-1+LEN(SOURCE) > MAX_LEN, the operation is performed, the string is truncated and -4 is returned.

e.g., If the position exceeds the current length of the destination:

If POSITION > LEN(DESTINATION), the string is padded with spaces and -2 is returned.

e.g., If the source string will make the destination string longer:

If POSITION-1+LEN(SOURCE) > LEN(DESTINATION), the string will be expanded to fit and -1 will be returned.

NOTE: If more than one condition is met (typically -2 and -1 would be met at the same time), the codes are added together as the return value.

NOTE: The subroutine knows the max length of the destination string.

If the operation meets none of the above conditions, the new length is returned.

The return code may be ignored (as in the example below).

Example:

STRING DESTINATION$[100];

DESTINATION$ = "Space XXXX To Fill";

SETSTRING("ABCD", 7, DESTINATION$);

Would result in DESTINATION containing the string "Space ABCD To Fill". If the return code were used, it would contain 18 (the string length).

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/SETSTRING.htm*
