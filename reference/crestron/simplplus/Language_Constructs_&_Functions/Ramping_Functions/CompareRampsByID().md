# CompareRampsByID

Name:

CompareRampsByID

Syntax:

SIGNED_INTEGER CompareRampsByID (ANALOG_OUTPUT | ANALOG_INPUT signal, LONG_INTEGER ramp_identifier );

Description:

This function compares the ID field of the ramp on the given signal to the [rampIdentifier](<Ramping_Functions.htm>) member of the RAMP_INFO structure as specified by the RampData variable.

Parameters:

ANALOG_OUTPUT | ANALOG_INPUT signal RAMP_INFO RampData – the specific analog input or output to compare with the RampData in the RAMP_INFO structure.

Return Value:

If the return value is negative, it is an error code. (see [Ramping Functions Error Codes](<Ramping_Function_Return_Error_Codes.htm>))

The returned values for this function are as follows:

0: The ramping process on the specified signal and the data specified in the given RAMP_INFO structure are different.

1: The ramping process on the specified signal and the data specified in the given RAMP_INFO structure are the same.

3: There is no ramp process on the specified signal.

Example: 

This is a more efficient version of the code presented in CompareRampsByAttribute, as all It needs to do is check one long_integer. 

ANALOG_INPUT InputLevel;

ANALOG_OUTPUT OutputLevel;

RAMP_INFO InputRampInfo, OutputRampInfo;

LONG_INTEGER InputRampID;

Change InputLevel

{

if(IsRamping(InputLevel))

{

GetRampInfo(InputLevel, InputRampInfo);

If(InputRampInfo.rampIdentifier <> InputRampID)

{

CreateRamp(OutputLevel, InputRampInfo);

}

}

else

{

OutputLevel = InputLevel;

InitializeRampInfo(InputRampInfo);

}

}

function main()

{

// By initializing our test-against ID to zero, we will guarantee that the first

// time a ramp is found in the change statement, the ramps will not be thought to

// be the same.

InputRampID = 0;

}

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

2-series only, CUZ 4.000 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/CompareRampsByID%28%29.htm*
