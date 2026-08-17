# StopRamp

Name:

StopRamp

Syntax:

SIGNED_INTEGER StopRamp (ANALOG_OUTPUT signal);

Description:

This function unconditionally terminates, or stops, the ramping process on a given ANALOG_OUTPUT signal.

Parameters:

ANALOG_OUTPUT signal – the specific output of the ramping process you want to stop. It is legal to use an ANALOG_OUTPUT or an element of an ANALOG_OUTPUT array.

Return Value:

If the return value is negative, it is an error code. (see [Ramping Functions Error Codes](<Ramping_Function_Return_Error_Codes.htm>))

The returned values for this function are as follows:

2: There is no Ramp Control Block (RCB) to stop on the specified signal.

0: RCB stopped successfully.

Example: 

In this example, when TerminateFade is driven high, the SIMPL+ module will stop the fade in progress on the Light driven by analog output LightLevel[1].

DIGITAL_INPUT TerminateFade;

ANALOG_OUTPUT LightLevel[20];

PUSH TerminateFade

{

SIGNED_INTEGER status;

if(IsSignalDefined(LightLevel[1]))

{

status = StopRamp(LightLevel[1]);

if(status < 0)

GenerateUserWarning("Error stopping ramping process, status = %d", status);

}

} 

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

2-series only, CUZ 4.000 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/StopRamp%28%29.htm*
