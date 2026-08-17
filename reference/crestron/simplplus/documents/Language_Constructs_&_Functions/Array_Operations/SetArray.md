# SetArray

Name:

SetArray

Syntax:

SetArray (ARRAY_NAME, INTEGER | STRING INIT_VALUE); 

Description:

Sets every element of ARRAY_NAME to the INIT_VALUE.

Parameters:

ARRAY_NAME is the name of the array to be initialized. It may be any array type.

The INIT_VALUE may be a INTEGER or STRING. The following chart shows the various combinations of ARRAY_NAME types and INIT_VALUE types:

NOTE: When working with DIGITAL_OUTPUT arrays, if the INIT_VALUE evaluates to 0, the digital signals are set low. For any non-zero value, the outputs are set high.

Return Value:

None.

Example:

DIGITAL_INPUT InitializeArrays;

INTEGER Levels[10];

STRING Names[5][5];

PUSH InitializeArrays

{

SetArray(Levels, 3);

SetArray(Levels, "3");

SetArray(Names, "xyz");

SetArray(Names, 0x41);

}

The first line initializes all elements of the integer array Levels to contain the integer 3.

The second line attempts to initialize the elements of the integer array Levels with a string value - an ATOI is done on the "3", which returns a 3, so that the end result is the same as the first line.

The third line initializes all elements of the elements of the string array Names to contain the string value "xyz".

The fourth line attempts to initialize the elements of the string array Names with an integer value - a CHR is done on the 0x41, which returns the string "A", so that the end result has all elements of the string array Names containing the string "A".

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Array_Operations/SetArray.htm*
