# ReverseFindNoCase

Name:

ReverseFindNoCase

Syntax:

INTEGER ReverseFindNoCase(STRING

[, INTEGER START_POSITION]);

Description:

Finds the position in SOURCE_STRING where

Parameters:

MATCH_STRING is a STRING containing the searched for data.

SOURCE_STRING is a STRING containing the data to be searched.

START_POSITION is an INTEGER which tells

Return Value:

The index of where MATCH_STRING last occurs (going right to left) in

Example:

STRING_INPUT IN$[100];

INTEGER START_LOC;

CHANGE IN$

{

START_LOC =

PRINT("last XYZ occurrence was found at position %d in %s\n", START_LOC, IN$);

}

If IN$ was set equal to "Hello, World!" then START_LOC would be 0 since "XYZ" cannot be found. If IN$ was equal to "CPE1704XYZXYZ", then START_LOC would be equal to 11.

Version:

SIMPL+ Version 2.10.00 or later

CUZ 3.137 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/ReverseFindNoCase.htm*
