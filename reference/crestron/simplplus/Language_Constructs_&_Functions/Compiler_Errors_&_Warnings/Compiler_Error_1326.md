# Compiler Error 1326

declaration error: propDefaultValue is not within propBounds.

propBound's Upper Bound value must be greater than the

Lower Bound value

propBound's Lower, Upper and Default values must be of the same

type

The Default Value must be within the bounds specified in propBounds. The compiler will also enforce that the lower bound is less than the upper bound. All values specified must also be of the type indicated within propValidUnits.

The following are examples of this error:

INTEGER_PARAMETER iParam, iAnotherParam;

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propDefaultUnit = unitDecimal;

propBounds = 1d,20d; // ok, 1d and 20d are both of type

// unitDecimal.

propDefaultValue = 10d;// ok, 10d is within 1d and 20d and

// of type unitDecimal.

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propDefaultUnit = unitDecimal;

propBounds = 1d,20d;

propDefaultValue = 50d; // error, 50d is NOT within 1d and 20d

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propDefaultUnit = unitDecimal;

propBounds = 50d,20d; // error – 50d is not less than 20d

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES iParam, iAnotherParam 

propValidUnits = unitDecimal;

propBounds = 50t,20t; // error – 50t is not of type unitDecimal

#END_PARAMETER_PROPERTIES

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1326.htm*
