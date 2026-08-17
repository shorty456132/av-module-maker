# Compiler Error 1309

declaration error: Compiler Directive must be set before all global

variable declarations

#DEFAULT_NONVOLATILE Compiler Directive already set

#DEFAULT_VOLATILE Compiler Directive already set

The compiler directives, #DEFAULT_VOLATILE and #DEFAULT_NONVOLATILE, must be used before any global variables are encountered within the SIMPL+ module. A module cannot contain more than one of these directives.

The following are examples of this error:

//////////////////////////////////////////////////////////////////

// Example 1

#DEFAULT_VOLATILE // ok – compiler directive exists before

// all global variables

INTEGER x;

STRING str[100];

DIGITAL_INPUT di;

FUNCTION MyFunc()

{

}

//////////////////////////////////////////////////////////////////

// Example 2

INTEGER x;

STRING str[100];

DIGITAL_INPUT di;

#DEFAULT_VOLATILE // error – global variables have already been

// declared within this module

FUNCTION MyFunc()

{

}

//////////////////////////////////////////////////////////////////

// Example 3

#DEFAULT_VOLATILE // ok – compiler directive exists before

// all global variables

INTEGER x;

STRING str[100];

DIGITAL_INPUT di;

#DEFAULT_NONVOLATILE // error – #DEFAULT_VOLATILE has already

// been set

INTEGER y;

#DEFAULT_NONVOLATILE // error – #DEFAULT_VOLATILE has already

// been set

INTEGER z; 

FUNCTION MyFunc()

{

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1309.htm*
