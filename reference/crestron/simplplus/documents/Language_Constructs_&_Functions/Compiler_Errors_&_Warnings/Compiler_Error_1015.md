# Compiler Error 1015

syntax error: Invalid Parameter Unit(s): '<property_unit>'

The compiler was expecting a parameter unit and another token or type was found.

The following are examples of this error:

INTEGER_PARAMETER iParam, iAnotherParam;

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal | unitHex |

unitPercent | unitCharacter |

unitTime | unitTicks; // ok

propDefaultUnit = unitDecimal // ok

propDefaultUnit = unitString; // error – unitString is not a

valid Parameter Unit

#END_PARAMETER_PROPERTIES

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1015.htm*
