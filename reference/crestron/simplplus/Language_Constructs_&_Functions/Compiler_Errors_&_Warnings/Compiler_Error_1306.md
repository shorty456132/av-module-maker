# Compiler Error 1306

declaration error: Declaration type can only be used globally: '<identifier>'

I/O declarations must be defined globally; they cannot be declared as local variables inside of a function or library file.

The following are examples of this error:

INTEGER i; // ok

STRING str[100]; // ok

DIGITAL_INPUT di; // ok

DIGITAL_OUTPUT do; // ok

ANALOG_INPUT ai; // ok

ANALOG_OUTPUT ao; // ok

STRING_INPUT si[100]; // ok

STRING_OUTPUT so; // ok

BUFFER_INPUT bi[100]; // ok

FUNCTION MyFunc()

{

INTEGER i; // ok – not an I/O declaration

STRING str[100]; // ok – not an I/O declaration

DIGITAL_INPUT di; // error

DIGITAL_OUTPUT do; // error

ANALOG_INPUT ai; // error

ANALOG_OUTPUT ao; // error

STRING_INPUT si[100]; // error

STRING_OUTPUT so; // error

BUFFER_INPUT bi[100]; // error

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1306.htm*
