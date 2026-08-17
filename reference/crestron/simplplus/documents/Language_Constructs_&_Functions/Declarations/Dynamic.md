# DYNAMIC

Name:

DYNAMIC

Syntax:

DYNAMIC [<string> | <integer_array> | <string_array> | <structure_array>];

Description:

Compiler directive to allow the size of a declared array to be changed to a new size. Global and Local Integer, String and Structure arrays can be declared as dynamic.

Argument:

string, integer array, string array, or structure_array

Example:

DYNAMIC STRING MyStr[10], MyStrArr[10][20];

DYNAMIC INTEGER MyInt[10], MyIntArr[10][20];

DYNAMIC tagMyStruct myStructArr[10];

Version:

X-Generation

Not Supported

2-Series

SIMPL 2.10.24 or later 

Requires CUZ 4.000 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/Dynamic.htm*
