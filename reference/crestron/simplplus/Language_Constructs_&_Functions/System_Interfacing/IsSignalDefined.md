# IsSignalDefined

Name:

IsSignalDefined

Syntax:

INTEGER IsSignalDefined <input/output signal>;

Description:

Retrieves the current SIMPL signal number associated with a particular input or output. This is generally used to determine if a particular input or output on a gate is being used, and generally used with arrayed inputs or outputs. This can be used to build a gate of a predetermined maximum size, and allow the user to add and subtract signals on the input or output of the gate (i.e., the program would be written to iterate through a DIGITAL_INPUT array until IsSignalDefined returns a 0).

Parameters:

Legal output and input signal types are ANALOG_INPUT, ANALOG_OUTPUT, BUFFER_INPUT, DIGITAL_INPUT, DIGITAL_OUTPUT, STRING_INPUT, STRING_OUTPUT.

Return Value:

The particular input or output is tied to an integer giving the signal number. If a signal has been tied to that input or output of the gate, a non-zero value will be returned. If the input/output is tied to 0 in the SIMPL program or is not defined, then 0 will be returned. If a digital input/output in the SIMPL program is tied to 1, then 1 is returned. If an analog or serial input/output in the SIMPL program is tied to 1, then 0 is returned.

Example:

DIGITAL_INPUT INS[20];

INTEGER NumInputs;

FUNCTION MAIN()

{

FOR(NumInputs = 20 to 1 Step -1)

IF(IsSignalDefined(INS[NumInputs]))

Break;

}

This example computes how many inputs are used on the gate. It should be noted that it is useful to count backwards from the end of the gate. If the user tied five signals, a 0, and then five more signals, this would yield the correct result that the 11th input was the last one used.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/IsSignalDefined.htm*
