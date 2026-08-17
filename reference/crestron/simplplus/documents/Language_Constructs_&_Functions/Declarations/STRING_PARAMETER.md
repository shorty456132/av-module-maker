# STRING_PARAMETER

Name:

STRING_PARAMETER

Syntax:

STRING_PARAMETER <var1[size1]>[,<var2[size2]>...];

STRING_PARAMETER <var1[num_elements1][num_characters1]>[,

<var2[num_elements2][num_characters2]>...];

Description:

The first form declares a STRING_PARAMETER value that is local to this SIMPL+ program. 

The second form declares a one dimensional array of STRING_PARAMETER values.

The values for SIZE may be up to 65534. Note that at runtime, the string is truncated to this length if the string specified in SIMPL is longer.

The actual value for the parameter is entered as a parameter to the SIMPL+ module when the SIMPL+ module is used the SIMPL program. 

STRING_PARAMETERs may have programmatic restrictions placed on them, similar to parameter property sheets for SIMPL modules. The programmer can allow certain values to be entered, assume default values, among others restrictions. For more information, please see [Parameter Property Blocks](<../Compiler_Directives/PARAMETER_PROPERTIES.htm>)

A STRING_PARAMETER array element may be used anywhere a STRING is legal, with the caveat that it may not be written to. Array elements are referenced by using the name followed by [element]. The element number may range from 1 to the element size. For example, if an array is declared as NUM[2], then legal elements are NUM[1], and NUM[2]. The bracket notation is often called an array subscript..

NOTE: The [_SKIP_](<../Compiler_Directives/_SKIP_.htm>) keyword can be used in INTEGER_PARAMETER, LONG_INTEGER_PARAMETER, SIGNED_INTEGER_PARAMETER, SIGNED_LONG_INTEGER_PARAMETER and STRING_PARAMETER declarations.

Example:

STRING_PARAMETER SystemName[10];

Signifies that one local STRING_PARAMETER of 10 bytes wide is declared in this SIMPL+ program and named "SystemName"

STRING_PARAMETER Labels[2][10];

Signifies that two strings of 10 characters long have been allocated and referenced by the array name "Labels". To reference an element, simply use the [] index notation:

Print("The value of parameter 1 is %s\n", Labels[1]);

Version:

X Generation: Not Supported.

2-Series: SIMPL v2.10.24 or later, CUZ 4.000 or later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/STRING_PARAMETER.htm*
