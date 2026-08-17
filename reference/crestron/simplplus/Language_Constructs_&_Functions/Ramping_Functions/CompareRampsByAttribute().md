# CompareRampsByAttribute

Name:

CompareRampsByAttribute

Syntax:

SIGNED_INTEGER CompareRampsByAttribute (ANALOG_OUTPUT | ANALOG_INPUT signal, RAMP_INFO RampData);

Description:

This function compares the ramping process on the given signal to the ramp described by RampData. Specifically, it checks to make sure that the rampTransitionTime, rampBaseValue and rampTargetValue are the same.

Parameters:

ANALOG_OUTPUT | ANALOG_INPUT signal RAMP_INFO RampData – the specific analog input or output to test against the described values of RampData in the RAMP_INFO structure.

Return Value:

If the return value is negative, it is an error code. (see [Ramping Functions Error Codes](<Ramping_Function_Return_Error_Codes.htm>))

The returned values for this function are as follows:

3: There is no ramp process on the specified signal.

1: The ramping process on the specified signal and the data specified in the given RAMP_INFO structure are the same.

0: The ramping process on the specified signal and the data specified in the given RAMP_INFO structure are different.

Example: 

In this example, the SIMPL+ module will monitor the input signal. If the input signal has a ramping process, it will copy it to the output. It then stores the ramping information for future comparison; each time the input ramp changes, it will trigger this module, but the module will end up stopping once it realizes that it has already processed the ramping process that is on the input. If there is no ramping process, it will simply copy the input value to the output value.

ANALOG_INPUT InputLevel;

ANALOG_OUTPUT OutputLevel;

RAMP_INFO InputRampInfo, OutputRampInfo;

Change InputLevel

{

if(IsRamping(InputLevel))

{

if(CompareRampsByAttribute(InputLevel, InputRampInfo)=0)

{

GetRampInfo(InputLevel, InputRampInfo);

CreateRamp(OutputLevel, InputRampInfo);

}

}

else

{

OutputLevel = InputLevel;

InitializeRampInfo(InputRampInfo);

}

}

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

2-series only, CUZ 4.000 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/CompareRampsByAttribute%28%29.htm*
