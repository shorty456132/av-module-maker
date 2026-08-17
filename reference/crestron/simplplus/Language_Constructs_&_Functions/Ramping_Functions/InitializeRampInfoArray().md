# InitializeRampInfoArray()

Name:

InitializeRampInfoArray()

Syntax:

InitializeRampInfoArray(RAMP_INFO array[])

Description:

Initializes each structure the given RAMP_INFO array to it's default state. The default states are the same as when the RAMP_INFO structure is declared:

rampUpperBound: 65535

rampLowerBound: 0

rampBaseValue: 100000

rampTargetValue: 65535

rampBaseTime: 0

rampTransitionTime: 0

rampIsSigned: 0

rampIsAbsolute: 0

This is useful for returning the structure back to a safe state after performing comparisons. (see CompareRampsByAttribute(), CompareRampsByID()).

Parameters:

RAMP_INFO array[ ] – a RAMP_INFO array is initialized.

Return Value:

None

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
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/InitializeRampInfoArray%28%29.htm*
