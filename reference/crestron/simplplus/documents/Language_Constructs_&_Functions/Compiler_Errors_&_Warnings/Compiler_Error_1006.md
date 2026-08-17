# Compiler Error 1006

syntax error: Invalid #DEFINE_CONSTANT value: '<identifier>'

The value for a #DEFINE_CONSTANT compiler directive must be either a literal string or an integer value. Expressions, variables, functions and events cannot be specified as the compiler directive’s value.

The following are examples of this error:

INTEGER x;

#DEFINE_CONSTANT MyIntConst 100 // ok

#DEFINE_CONSTANT MyStrConst “abc” // ok

#DEFINE_CONSTANT MyExprConst (1+2) // error – expressions are

// not allowed

#DEFINE_CONSTANT MyVarConst x // error – substitutions are

// not allowed

#DEFINE_CONSTANT MyExprConst (x+1) // error – macros are not

// supported

#DEFINE_CONSTANT MyFuncConst myFunc // error

#DEFINE_CONSTANT MyFuncConst getc // error

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1006.htm*
