# CHANGE

Name:

CHANGE

Syntax:

CHANGE <variable_name1> [, <variable_name2> ...]

{

[Local Variable Definitions]

<statements>

}

Description:

The CHANGE event is called when a DIGITAL_INPUT transitions from low to high or high to low, or when an ANALOG_INPUT or STRING_INPUT changes.

<variable_name> may be either a DIGITAL_INPUT, ANALOG_INPUT, or STRING_INPUT type. If it is a DIGITAL_INPUT, the statements between { and } will be executed when the input transitions from low to high or high to low. If it is an ANALOG_INPUT or STRING_INPUT, the statements between { and } will be executed whenever the variable changes. Note that for an ANALOG_INPUT or STRING_INPUT, the same value re-issued will also cause the CHANGE to activate.

When using ANALOG_INPUT, BUFFER_INPUT, DIGITAL_INPUT, or STRING_INPUT arrays, only a change in the entire array can be detected, not an individual element. Refer to "[GetLastModifiedArrayIndex](<../Array_Operations/GetLastModifiedArrayIndex.htm>)" to determine which element actually changed. Use isSignalDefined to make sure that you send data only to outputs that exist or take input from signals that exist.

When listing multiple variable names, the names can be put on the same line or broken up into several CHANGE statements for readability.

(See also [StackedEvents](<Stacked_Events.htm>) and [THREADSAFE](<THREADSAFE.htm>))

Example:

STRING_INPUT some_data$[100];

ANALOG_OUTPUT level;

CHANGE some_data$

{

level=48;

}

When the STRING_INPUT changes, the ANALOG_OUTPUT level will have the value 48 put into it. If the same data comes in on some_data$, the CHANGE block is executed again.

ANALOG_INPUT ThingsToAdd[20];

ANALOG_OUTPUT Sum;

INTEGER I, Total;

CHANGE ThingsToAdd

{

Total=0;

FOR(I=0 to 20)

if (isSignalDefined (ThingsToAdd[I]))

Total = Total + ThingsToAdd[I];

Sum = Total;

}

In this example, an array is used to hold elements to add. When any element of the array changes, the total is recomputed and issued on an analog output variable.

Version:

X Generation:

SIMPL v1.20.01 and later

SIMPL v1.50.06 and later, ANALOG_INPUT, BUFFER_INPUT, DIGITAL_INPUT, and STRING_INPUT arrays as <variable_name>

2-Series:

SIMPL v2.01.05 and later [Same as X Generation SIMPL v1.50.06] and Local Variables allowed within CHANGE statements.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Events/CHANGE.htm*
