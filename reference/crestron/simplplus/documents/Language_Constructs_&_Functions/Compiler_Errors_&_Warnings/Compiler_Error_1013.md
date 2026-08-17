# Compiler Error 1013

syntax error: Source code does not evaluate to anything

A statement must perform an action in order to be valid. If no action is specified, the statement will not be useful to the program.

The following are examples of this error:

FUNCTION MyFunc()

{

INTTEGER x;

STRING str[100];

x = 5; // ok

str = “abc”; // ok

x; // error

str; // error

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1013.htm*
