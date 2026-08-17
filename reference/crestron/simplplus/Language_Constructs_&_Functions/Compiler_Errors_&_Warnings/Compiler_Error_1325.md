# Compiler Error 1325

declaration error: propDefaultValue must be declared before using propList.

propBounds must be declared before using propDefaultValue.

propList must contain an element with the propDefaultValue.

Default values, if specified, must be specified before a propList declaration. If using propBounds, the Default Value must be defined beforehand. If a default value is specified, the propList must contain at least one element that contains this default value.

The following are examples of this error:

INTEGER_PARAMETER iParam, iAnotherParam;

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propBounds = 10d,20d; // ok

propList = {10d, "value1"}, {20d, "value2" }; // error -

// propBounds previously used

// within block

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propDefaultValue = 15d; // ok

propBounds = 10d,20d; // ok

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propDefaultValue = 15d;// ok

propBounds = 10d,20d; // error – propDefaultValue has been

// defined beforehand

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propDefaultValue = 15d;// ok

propList = {10d, "value1"}, {20d, "value2" }; // error –

// propDefaultValue has been

// defined beforehand

#END_PARAMETER_PROPERTIES

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1325.htm*
