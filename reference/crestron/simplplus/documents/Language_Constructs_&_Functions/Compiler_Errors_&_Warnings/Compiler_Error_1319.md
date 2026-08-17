# Compiler Error 1319

construct error: Invalid format specifier: <format specifier>, propValidUnits undefined or specifier not declared within propValidUnits

Specifier not declared within propValidUnits

A parameter was being assigned a value that was either out of range or of the wrong type. Before any property or property value can be defined, propValidUnits must be specified. The PropDefaultUnit specified must be contained within propValidUnits.

The following are examples of this error:

INTEGER_PARAMETER intParam;

#BEGIN_PARAMETER_PROPERTIES intParam

propBounds = 25d, 50d; // error – propValidUnits undefined

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES intParam

propValidUnits = unitDecimal;

propBounds = 25d, 50d; //ok – propValidUnits defined above

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES intParam

propValidUnits = unitDecimal|unitCharacter;

propDefaultUnit = unitHex; // error – unitHex not contained

within propValidUnits

propDefaultUnit = unitCharacter; // ok

propBounds = 25d, 50d; // ok – valid Integer range is 0-65535

propBounds = -50d, -25d; // error – Integer range is not 0-65535

propBounds = “abc”, "def"; // error – “abc” is not a valid number

#END_PARAMETER_PROPERTIES

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1319.htm*
