# Compiler Error 1007

syntax error: Missing array index: '<identifier>'

A variable declared as an array is being used within an expression without the array index being specified. For two-dimensional arrays, both indices must be specified. When passing entire arrays as function arguments, no index is needed.

The following are examples of this error:

FUNCTION MyFunc()

{ 

INTEGER i, arr[10], arr2[10][20];

STRING str[100], str2[100][50];

i = arr[5]; // ok

i = arr2[5][10]; // ok

arr[5] = arr2[5][10]; // ok

arr2[5][10] = 5; // ok

i = arr; // error – no index specified

arr = 5; // error – no index specified

i = arr2[5]; // error – 2nd index not specified

str2[5] = “a”; // ok

str[5] = “a”; // error – ‘str’ is not an array

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1007.htm*
