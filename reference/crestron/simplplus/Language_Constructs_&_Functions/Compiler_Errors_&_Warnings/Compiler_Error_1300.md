# Compiler Error 1300

declaration error: Array size missing

Array size invalid

STRING, STRING_INPUT and BUFFER_INPUT variables require a valid length. A length is specified by number enclosed within brackets. Arrays for these datatypes are specified by the first set of brackets containing the number of strings and the second set of brackets containing the total length for each string. Two-dimensional arrays are not allowed for these datatypes.

In a function’s argument list, since all strings are passed by reference, no array size is necessary. A string array is indicated by an empty set of brackets. See example below.

The following are examples of this error:

#DEFINE_CONSTANT ARR_SIZE 100

STRING str[100]; // ok – str has a length of 100

STRING_INPUT strIn[ARR_SIZE]; // ok – strIn has a length of 100

BUFFER_INPUT bufIn[ARR_SIZE]; // ok – bufIn has a length of 100

STRING strArr[50][100]; // ok – 51 strings of length 100

STRING_INPUT strIn[50][100]; // ok - 51 strings of length 100

BUFFER_INPUT bufIn[50][100]; // ok – 51 strings of length 100

STRING_OUTPUT strOut; // ok – STRING_OUTPUTs do not

// require a length

STRING_OUTPUT strOutArr[10]; // ok – array of 10 STRING_OUTPUTs

STRING str2; // error – no length specified

STRING_INPUT strIn; // error – no length specified

BUFFER_INPUT bufIn; // error – no length specified

STRING_OUTPUT strOutArr[10][20]; // error – 2-D arrays not supported

STRING str[x]; // error – variables are not allowed

STRING str[myFunc()]; // error – function calls are

// not allowed

FUNCTION myFunc( STRING sArg, // ok – strings are passed by

STRING sArgArr[] ) // reference. sArg is a

// string and sArgArr is a

// string array

{

}

FUNCTION myFunc2( STRING sArg[10], // error – size is not allowed

STRING sArgArr[][] ) // error – 2-D strings not

// supported

{

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1300.htm*
