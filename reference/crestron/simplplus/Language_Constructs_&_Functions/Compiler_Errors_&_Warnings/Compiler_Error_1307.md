# Compiler Error 1307

declaration error: Variables must be declared before array

declarations: '<identifier>'

I/O declarations must be declared in a specific order. All arrays of an I/O declaration type (i.e.: DIGITAL_INPUT) must be declared after any variables of the same type.

The following are examples of this error:

DIGITAL_INPUT di1, di2; // ok

DIGITAL_INPUT di3; // ok

ANALOG_INPUT ai1 // ok

DIGITAL_OUTPUT do1; // ok

ANALOG_INPUT aiArr1[10]; // ok

DIGITAL_INPUT di4; // ok – no DIGITAL_INPUT array exists yet

DIGITAL_INPUT diArr1[10]; // ok

DIGITAL_OUTPUT do2; // ok

ANALOG_INPUT aiArr2[20]; // ok – multiple arrays are allowed

DIGITAL_INPUT di5; // error – cannot define after diArr1

ANALOG_INPUT ai2; // error – cannot define after aiArr2

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1307.htm*
