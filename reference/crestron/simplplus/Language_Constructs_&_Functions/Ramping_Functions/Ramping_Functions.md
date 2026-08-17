# Ramping Functions

Ramping functions make it possible to manage processes that smoothly transition an ANALOG_OUTPUT from one value to another over a specified period of time. In the past, it was necessary to use methods such as loops to issue multiple values or an oscillator to trigger a DIGITAL_INPUT to increment an ANALOG_OUTPUT in order to get the same effect. Functions are available for creation, destruction, detection and comparison.

The Ramping functions use a pre-defined structure called RAMP_INFO. 

STRUCTURE RAMP_INFO

{

SIGNED_LONG_INTEGER // rampLowerBound;

SIGNED_LONG_INTEGER // rampUpperBound;

SIGNED_LONG_INTEGER // rampBaseValue;

SIGNED_LONG_INTEGER // rampTargetValue;

INTEGER // rampIsAbsolute;

LONG_INTEGER // rampTransitionTime;

INTEGER // rampIsRunnable;

LONG_INTEGER // rampIdentifier;

LONG_INTEGER // rampBaseTime;

INTEGER // rampIsSigned;

INTEGER // rampIsExpired; 

};

NOTE: Your choice of values for rampLowerBound, rampUpperBound, rampBaseValue and rampTargetValue must be consistent within a given RAMP_INFO function (shown later in this topic). Choose either the -32768 to 32767 range or the 0 to 65535 range.

The members of RAMP_INFO are described as follows:

MEMBER |  DESCRIPTION |  NOTES  
---|---|---  
rampLowerBound |  The lowest possible value of the ramp. |  Legal values are -32768 to 32767 or 0 to 65535. Default is 0.  
rampUpperBound |  The highest possible value of the ramp. |  Legal values are -32768 to 32767 or 0 to 65535. Default is 65535.  
rampBaseValue |  The starting value of the ramp. |  Legal values are -32768 to 32767 or 0 to 65535. Default is 1000001. The ramp will start from the current value of the signal on the ANALOG_OUT in SIMPL. The predefined constant; SIGNAL_DEFAULT_VALUE can also be used.  
rampTargetValue |  The ending value of the ramp. |  Legal values are -32768 to 32767 or 0 to 65535. Default is 65535.  
rampTransitionTime |  The length of time (in units of 0.01sec.) for the ramping function to go from rampBaseValue to rampTargetValue. |  The rampTransitionTime is dependent on the value of the rampIsAbsolute member. Default is 5002.  
rampIsAbsolute |  Indicates whether or not the rampTransitionTime is relative (indicated by <>1) or absolute (indicated by 1). |  If rampTransitionTime is relative, the rampTransitionTime will be the result of the following formula: If rampTransitionTime is absolute, the time to get from rampBaseValue to rampTargetValue is exactly as specified. Default is 0 (FALSE). Legal values are 0 and 1.  
rampIsRunnable |  Specifies if the ramp actually creates values to put into a signal or if the ramp is a place holder. |  If a SIMPL+ module is creating a ramp, like the Analog Ramp symbol does, then IsRunnable is 1. If the SIMPL+ module is looking at a ramp on an ANALOG_INPUT and then placing one on an ANALOG_OUTPUT, it should set IsRunnable=0, and the module itself should be responsible for setting the correct discrete value on the analog output. Default is 1 (TRUE).  
rampIdentifier |  Used to distinguish one ramp from another where two ramps are in use. |  Since two ramps can be created at the same time and have the same start/end values and rampTransitionTime, this member is used to distinguish one ramp from another. The system assigns the rampIdentifier. It is not user-specifiable.  
rampBaseTime |  The system time at which the ramping process was created. |  This member is not user-specifiable.  
rampIsSigned |  |   
rampIsExpired |  |   
  
  1. The rampBaseValue default of 100000 is not a legal value for an analog signal (legal values are -32768 to 32767 or 0 to 65535). The default of 100000 means that when the ramp is launched it's value--the 100000--is replaced by the existing rampBaseValue from the ANALOG_OUTPUT signal parameter called by the [CreateRamp](<CreateRamp\(\).htm>) function.

  2. In SIMPL+ time is rendered in hundredths of a second. Therefore, 5 seconds is represented as 500.




The functions available to the RAMP_INFO structure are:

[CreateRamp](<CreateRamp\(\).htm>)

[StopRamp](<StopRamp\(\).htm>)

[IsRamping](<IsRamping\(\).htm>)

[GetRampInfo](<GetRampInfo\(\).htm>)

[CompareRampsByAttribute](<CompareRampsByAttribute\(\).htm>)

[CompareRampsByID](<CompareRampsByID\(\).htm>)

[InitializeRampInfo](<InitializeRampInfo.htm>)

[InitializeRampInfoArray](<InitializeRampInfoArray\(\).htm>)

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

2-series only, CUZ 4.000 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/Ramping_Functions.htm*
