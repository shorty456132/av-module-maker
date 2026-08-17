# Compiler Error 1324

declaration error: propList cannot be used in conjunction with propBounds.

propBounds cannot be used in conjunction with propList.

NOTE: propList and propBounds cannot be used within the same parameter properties block.

The following are examples of this error:

INTEGER_PARAMETER iParam, iAnotherParam;

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propBounds = 10,20; // ok

propList = {10d, "value1"}, {20d, "value2" }; // error -

// propBounds previously used

// within block

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propList = {10d, "value1"}, {20d, "value2" }; // ok

propBounds = 10,20; // error -

// propList previously used

// within block

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propList = {10d, "value1"}, {20d, "value2" }; // ok

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propBounds = 10,20; // ok

#END_PARAMETER_PROPERTIES

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1324.htm*
