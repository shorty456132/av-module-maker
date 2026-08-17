# Compiler Error 1313

declaration error: Minimum array size invalid

The minimum array size cannot exceed the total size of the array. The minimum array size must be between 1 and the total size of the array.

The following are examples of this error:

DIGITAL_INPUT digIn1[10]; // ok

DIGITAL_INPUT digIn2[10,5]; // ok – minimum size is 5

ANALOG_INPUT anlgIn3[10,0]; // error – minimum size must be

// greater than 0

STRING_INPUT strIn4[10,20]; // error – minimum size of 20 exceeds

// total array size of 10

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1313.htm*
