# Bit

Name:

Bit

Syntax:

INTEGER Bit(STRING SOURCE, INTEGER SOURCE_BYTE, INTEGER

BIT_IN_BYTE);

Description:

Determine the state of a specified bit in a particular byte of a given string.

Parameters:

SOURCE contains a STRING in which a bit of one byte is to be examined. Each character in SOURCE is considered one byte.

SOURCE_BYTE references a character in the SOURCE string. The leftmost character in SOURCE is considered 1.

BIT_IN_BYTE specifies which bit in the SOURCE_BYTE of SOURCE is to be examined. BIT_IN_BYTE starts at position 0 (least significant or rightmost bit of the byte). 7 is the most significant or leftmost bit of the byte.

Return Value:

Returns 0 or 1 for a valid bit position. Illegal bit references will return 65535. It is illegal if SOURCE_BYTE is 0 or greater than the length of the SOURCE string. Note that it is legal to specify a bit beyond 7. This will reference a bit in another byte. In this way, a source string can be used as a set of packed bit flags. The algorithm for determining which bit in which byte is set when BIT_IN_BYTE is greater than 7 is as follows.

Actual Byte in SOURCE = (BIT_IN_BYTE / 8) + SOURCE_BYTE

Actual Bit in Actual Byte = (BIT_IN_BYTE MOD 8)

Applying this to BIT("abc",1,16) will reference bit 0 of byte 3 (the least significant bit of byte "c" in SOURCE).

Example:

This example takes an input string and creates an output string containing the elements of the input string that do not have the most significant bit (bit 7) set.

STRING_INPUT SOURCE$[100];

STRING_OUTPUT OUT$;

STRING TEMP$[100];

INTEGER I;

CHANGE SOURCE$

{

FOR(I = 1 to LEN(SOURCE$))

{

IF(BIT(SOURCE$, I, 7) = 0)

{

MAKESTRING(TEMP$, "%s%s", TEMP$, MID(SOURCE$, I, 1));

} 

}

OUT$ = TEMP$;

}

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Bit_%26_Byte_Functions/BIT.htm*
