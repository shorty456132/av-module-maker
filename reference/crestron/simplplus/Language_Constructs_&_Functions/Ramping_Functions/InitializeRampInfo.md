# InitializeRampInfo()

Name:

InitializeRampInfo()

Syntax:

InitializeRampInfo(RAMP_INFO val)

Description:

Initializes the given RAMP_INFO structure to it's default state. The value can be either an arrayed or non-arrayed structure. The default states are the same as when the RAMP_INFO structure is declared. Refer to [Ramping Function Defaults](<RAMP_INFO_Structure.htm>).

This is useful for returning the structure back to a safe state after performing comparisons. (see CompareRampsByAttribute(), CompareRampsByID()).

Parameters:

RAMP_INFO val: – the variable "val" of the type RAMP_INFO is initialized.

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
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/InitializeRampInfo.htm*
