# Compiler Error 1014

syntax error: Invalid Parameter: <’parameter_variable’>

Missing Parameters in directive construct

The compiler was expecting a parameter type variable and another declaration type or token was found.

The following are examples of this error:

INTEGER_PARAMETER iParam;

#BEGIN_PARAMETER_PROPERTIES // error – no parameter was

specified

propDefaultUnit = unitDecimal;

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam // ok – iParam is a declared

parameter

propDefaultUnit = unitDecimal;

#END_PARAMETER_PROPERTIES

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1014.htm*
