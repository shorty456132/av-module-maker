# Ramping Function Return Error Codes  
  
KEYWORD |  VALUE |  FUNCTION  
---|---|---  
RAMP_ILLEGAL_BASE_VALUE |  -22 |  rampBaseValue is not within the bounds of rampUpperBound to rampLowerBound  
RAMP_ILLEGAL_TARGET_VALUE |  -21 |  rampTargetValue is not within the bounds of rampUpperBound to rampLowerBound  
RAMP_BOUNDS |  -20 |  Illegal bounds have been specified. Bounds must be -32768 to 32767 or 0 to 65535. An error message is placed in the error log.  
RAMP_INVALID |  -15 |  Invalid Ramp (Internal, Contact Crestron)  
RAMP_NO_CREATE |  -14 |  Could Not Create Ramp (Internal, Contact Crestron)  
RAMP_BAD_POINTER |  -13 |  Illegal internal Ramp Pointer (Internal, Contact Crestron)  
RAMP_ILLEGAL_ISABSOLUTE |  -12 |  Illegal value specified for rampIsAbsolute, must be 0 or 1.  
RAMP_NO_SIGNAL |  -8 |  No signal at given index.1  
RAMP_SUCCESS |  0 |  Ramping process created/modified successfully  
RAMP_DIFFERENT_RAMP2 |  0 |  The ramping process on the specified signal and the data specified in the given RAMP_INFO structure are the different.  
RAMP_RAMP_PRESENT |  1 |  Ramp present on the given signal  
RAMP_SAME_RAMP2 |  1 |  The ramping process on the specified signal and the data specified in the given RAMP_INFO structure are the same.  
RAMP_NO_RAMP |  2 |  No Ramp on the signal to stop  
RAMP_NO_RAMP_PRESENT |  3 |  No Ramp on the given signal  
  
  1. This would typically happen if an element of an ANALOG_OUTPUT array is used that is not defined on the SIMPL symbol. For example, ANALOG_OUTPUT levels[20]; is in the SIMPL+ program, and the symbol is only expanded to 5, but an attempt is made to create a ramping process on levels[15].

  2. Applies to CompareRampByAttribute and CompareRampsByID. only.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/Ramping_Function_Return_Error_Codes.htm*
