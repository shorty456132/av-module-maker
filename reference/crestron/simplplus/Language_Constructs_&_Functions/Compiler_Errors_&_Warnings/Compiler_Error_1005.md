# Compiler Error 1005

syntax error: Unexpected symbol in compiler directive: '<identifier>'

An invalid identifier is following a compiler directive.

The following are examples of this error:

#DEFINE_CONSTANT MyIntConst 100 // ok

#DEFINE_CONSTANT “MyIntConst” 100 // error – MyIntConst should not

// be in quotes – this

// will be evaluated as

// a literal string

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1005.htm*
