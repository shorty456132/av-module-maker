# GetRampInfo()

Name:

GetRampInfo()

Syntax:

SIGNED_INTEGER GetRampInfo (ANALOG_OUTPUT | ANALOG_INPUT signal, RAMP_INFO RampData)

Description:

This function populates the fields of the given RAMP_INFO structure with the information from the ramping process on the given output signal.

Parameters:

ANALOG_OUTPUT | ANALOG_INPUT signal RAMP_INFO RampData

Return Value:

If the return value is negative, it is an error code. (see [Ramping Functions Error Codes](<Ramping_Function_Return_Error_Codes.htm>))

The returned values for this function are as follows:

0: The info on the ramping process on a given output was obtained successfully and placed into the RAMP_INFO structure.

3: There is no ramp process on the specified signal.

Example: 

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
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/GetRampInfo%28%29.htm*
