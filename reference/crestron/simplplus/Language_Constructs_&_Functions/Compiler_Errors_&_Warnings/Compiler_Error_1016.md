# Compiler Error 1016

syntax error: Invalid Parameter Property or

#END_PARAMETER_PROPERTIES not

found <’parameter_property’>

The compiler was expecting a parameter property and another token or type was found.

The following are examples of this error:

INTEGER_PARAMETER iParam, iAnotherParam;

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal|unitHex;

propDefaultUnit = unitDecimal; // ok –unitDecimal is a valid

Parameter Property.

propDefaultValue = 10d;

propList = {10d, "value1"}, {20d, "value2" };

propBounds = 1d, 20d;

propShortDescription = "a short description";

propFullDescription = "a full description.....";

propNotes = "Here's the notes";

Integer i; // error – Integer is not

A valid Parameter Property

// #END_PARAMETER_PROPERTIES // error – comment line

#END_PARAMETER_PROPERTIES // ok

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1016.htm*
