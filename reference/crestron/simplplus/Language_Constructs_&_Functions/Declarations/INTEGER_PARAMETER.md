# INTEGER_PARAMETER

Name:

INTEGER_PARAMETER

Syntax:

INTEGER_PARAMETER <var1>[,<var2>...];

INTEGER_PARAMETER <var1>[size] [,<var2>[size]…];

Description:

The first form declares an INTEGER_PARAMETER value that is local to this SIMPL+ program. 

The second form declares a one dimensional array of INTEGER_PARAMETER values.

The values for SIZE may be up to 65534.

The actual value for the parameter is entered as a parameter to the SIMPL+ module when the SIMPL+ module is used the SIMPL program. The parameter has a default range of legal values. Since parameters can be entered in various formats (percentage, hex, decimal, time, etc.), please see [Allowable Ranges for 2 Series Numeric Formats](<../../Allowable_Ranges_for_2_Series_Numeric_Formats.htm>) to find the valid ranges for the various types.

SIMPL+ Parameters may have further programmatic restrictions placed on them, similar to parameter property sheets for SIMPL modules. The programmer can restrict the range, only allow certain values to be entered, assume default values, restrict types of units entered among others restrictions. For more information, please see [Parameter Property Blocks](<../Compiler_Directives/PARAMETER_PROPERTIES.htm>)

An INTEGER_PARAMETER array element may be used anywhere an INTEGER is legal, with the caveat that it may not be written to. Array elements are referenced by using the name followed by [element]. The element number may range from 1 to the element size. For example, if an array is declared as NUM[2], then legal elements are NUM[1], and NUM[2]. The bracket notation is often called an array subscript.

NOTE: The [_SKIP_](<../Compiler_Directives/_SKIP_.htm>) keyword can be used in INTEGER_PARAMETER, LONG_INTEGER_PARAMETER, SIGNED_INTEGER_PARAMETER, SIGNED_LONG_INTEGER_PARAMETER and STRING_PARAMETER declarations.

Example:

INTEGER_PARAMETER temp_level;

Specifies one INTEGER_PARAMETER with the name temp_level in this SIMPL+ program

INTEGER_PARAMETER CommandBytes[2];

Specifies an array of two INTEGER_PARAMETERS that can be referenced under the name CommandBytes.

NOTE: The subscripts of an array may be any positive valid integral expression such as the one shown below.

INTEGER_PARAMETER location[5], room;

INTEGER var;

var = 3;

if(room>0 && room <= 5)

{

print("The location is %d\n", location[var]);

}

print("The location is %d\n", location[room]);

Version:

X Generation: Not Supported.

2-Series: SIMPL v2.10.24 or later, CUZ 4.000 or later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/INTEGER_PARAMETER.htm*
