# CreateRamp

Name:

CreateRamp

Syntax:

SIGNED_INTEGER CreateRamp (ANALOG_OUTPUT signal, RAMP_INFO RampData);

Description:

Creates a ramping process on the specific ANALOG_OUTPUT. If the output already has a running ramping process on it this function will modify that process regardless of its origin. (e.g., rampTransitionTime could be increased or rampTargetValue could be reduced). The following members must be filled in by the user:

rampLowerBound

rampUpperBound

rampBaseValue

rampTargetValue

rampTransitionTime

rampIsAbsolute

rampIsRunnable

NOTE: See [Ramping Functions Defaults](<RAMP_INFO_Structure.htm>) for the default values of these members.

Parameters:

ANALOG_OUTPUT signal – the specific output on which to create the ramping process. It is legal to use an ANALOG_OUTPUT or an element of an ANALOG_OUTPUT array.

RAMP_INFO RampData – a declared variable of RAMP_INFO used to hold information about the created ramping process.

NOTE: This function will change the following user-defined values in the RAMP_INFO structure:   
  
rampIsAbsolute: will be changed to 1 (Absolute) if the user specified that it would be Relative (<>1).  
  
rampTransitionTime: will be changed to the Absolute Transition Time reported by ANALOG_OUTPUT signal if the user originally specified rampTransitionTime as Relative (<>1).  
  
rampBaseValue: will be set to the value reported by ANALOG_OUT signal if rampBaseValue has been set to 100000.

NOTE: This function will fill in the following non-user specifiable values in the RAMP_INFO structure:   
  
rampBaseTime: will be automatically set to the system time at which the ramp was created.  
  
rampIdentifier: will be automatically set to distinguish the current ramp from any other existing ramps.  


Return Value:

If the return value is negative, it is an error code. (see [Ramping Functions Error Codes](<Ramping_Function_Return_Error_Codes.htm>))

The returned values for this function are as follows:

0: Ramping process created or modified successfully.

Example: 

In this example, an analog output array element is given a ramping process that will ramp from signal's current value to 10% (6553) in 10 seconds (1000).

DIGITAL_INPUT GoToPresetLevel;

ANALOG_OUTPUT LightLevel[20];

PUSH GoToPresetLevel

{

RAMP_INFO LightInfo;

SIGNED_INTEGER status;

// 10% of 65535 is 6553.

LightInfo.rampTargetValue=6553;

// Always takes "rampTransitionTime" to go to the Target Value. 

LightInfo.isAbsolute=1;

// Transition time of 10 seconds (1000 hundredths of a second)

LightInfo.rampTransitionTime=1000;

If(IsSignalDefined(LightLevel[1])

{ 

status = CreateRamp(LightLevel[1], LightInfo);

if(status <> 0)

GenerateUserWarning("Could not create Ramping Process, status = %d", status);

}

}

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

2-series only, CUZ 4.000 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Ramping_Functions/CreateRamp%28%29.htm*
