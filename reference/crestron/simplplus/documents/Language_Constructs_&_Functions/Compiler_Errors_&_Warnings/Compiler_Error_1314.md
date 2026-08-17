# Compiler Error 1314

declaration error: Minimum array size is not allowed for this

datatype: '<identifier>'

Minimum array size for this datatype has already

been declared: '<identifier>'

Minimum array sizes are only applicable to Input and Output datatypes (i.e.: DIGITAL_INPUT, ANALOG_OUTPUT, STRING_INPUT, etc.). A variable of another datatype was found trying to define a minimum array size. Only one array for each Input or Output datatype is allowed to be declared with a minimum array size.

The following are examples of this error:

DIGITAL_INPUT digIn1[10]; // ok

DIGITAL_INPUT digIn2[10,5]; // ok – minimum size is 5

DIGITAL_INPUT digIn3[20,10]; // error – the DIGITAL_INPUT array

// variable, digIn2, has already

// been declared with a minimum

// array size

ANALOG_INPUT anlgIn1[10]; // ok

ANALOG_INPUT anlgIn2[10,5]; // ok – no other ANALOG_INPUT has been

// declared with a minimum array size

INTEGER x[10]; // ok

INTEGER y[10,5]; // error – INTEGER is not an Input or

// Output datatype

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1314.htm*
