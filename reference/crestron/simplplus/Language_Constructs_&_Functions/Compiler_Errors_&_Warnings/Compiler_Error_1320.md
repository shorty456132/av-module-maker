# Compiler Error 1320

construct error: Cannot combine property unit: <unit>

The property unit, unitString, cannot be combined with any other property unit (i.e., unitDecimal,unitCharacter, etc).

The following are examples of this error:

INTEGER_PARAMETER intParam;

STRING_PARAMETER strParam;

#BEGIN_PARAMETER_PROPERTIES intParam

propValidUnits = unitDecimal|unitCharacter; // ok

propValidUnits = unitString; // ok

propValidUnits = unitString|unitDecimal; // error

#END_PARAMETER_PROPERTIES

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1320.htm*
