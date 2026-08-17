# Compiler Error 1318

construct error: Invalid Parameter Property Value or Property Value not allowed for <parameter>

Invalid Parameter Property Value (Numeric value expected)

Invalid Parameter Property Value (String expected)

A parameter was being assigned a value that was either out of range or of the wrong type for the parameter specified. Numeric values can only be assigned to non-String_Parameters with propValidUnits containing one of the following types: unitDecimal, unitHex, unitPercent, unitCharacter, unitTime or unitTicks. String values can only be assigned to a String_Parameter and with propValidUnits=unitString.

The following are examples of this error:

INTEGER_PARAMETER intParam;

STRING_PARAMETER strParam;

#BEGIN_PARAMETER_PROPERTIES intParam specified

propValidUnits = unitDecimal; // ok

propValidUnits = unitString; // error – intParam is not

a string

propDefaultValue = “abc”; // error – number expected

propDefaultValue = 5d; // ok

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES strParam 

propValidUnits = unitDecimal; // error – strParam is not

a number

propValidUnits = unitString; // ok

propDefaultValue = “abc”; // ok

propDefaultValue = 5d; // error

#END_PARAMETER_PROPERTIES

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1318.htm*
