# IsRamping

Name:

IsRamping

Syntax:

SIGNED_INTEGER IsRamping (ANALOG_OUTPUT | ANALOG_INPUT signal);

Description:

This function determines if there is a ramping process present on the specified ANALOG_OUTPUT signal.

Parameters:

ANALOG_OUTPUT | ANALOG_INPUT signal – the specific analog input or output to test for the presence of a ramping process.

Return Value:

If the return value is negative, it is an error code. (see [Ramping Functions Error Codes](<Ramping_Function_Return_Error_Codes.htm>))

The returned values for this function are as follows:

1: There is a ramping process present on the specified signal.

3: There is no ramping process present on the specified signal.

Example: 

In this example, the SIMPL+ module will start a ramping transition on the analog output "LightingLevel" using the default RAMP_INFO structure values, only if there is no ramping process currently on it (i.e. an "Analog Ramp" symbol or other ramp-generating symbol currently has a ramping operation in progress on that analog output signal in SIMPL).

DIGITAL_INPUT StartFade;

ANALOG_INPUT LightingLevel;

ANALOG_OUTPUT OutputLevel;

RAMP_INFO LightInfo;

Push StartFade

{

if(IsRamping(LightingLevel) != 1)

{

CreateRamp(OutputLevel, LightInfo);

}

}

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

2-series only, CUZ 4.000 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/IsRamping%28%29.htm*
