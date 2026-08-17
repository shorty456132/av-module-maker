# GetLastModifiedArrayIndex

Name:

GetLastModifiedArrayIndex

Syntax:

INTEGER GetLastModifiedArrayIndex ();

Description:

Determines the specific index number of an input list array that has changed.

ANALOG_INPUT, BUFFER_INPUT, DIGITAL_INPUT, and STRING_INPUT arrays are subject to be used in CHANGE, PUSH, and RELEASE statements, but only the overall array can be specified in the statement, not an individual element. In order to find out what element has been modified (and hence caused the activation of the CHANGE, PUSH, or RELEASE), GETLASTMODIFIEDARRAYINDEX is used.

NOTE: To use GETLASTMODIFIEDARRAYINDEX, only one array may be used in a single CHANGE, PUSH, or RELEASE statement. If more than one element of the array changes at the same time, multiple events are run. For example, if D[10] is a DIGITAL_INPUT array that is subject to a PUSH event, and D[1] and D[2] change at the same time, the PUSH is first run where D[1] changes and GETLASTMODIFIEDARRAYINDEX returns 1, then the PUSH is run again where D[2] changes and GETLASTMODIFIEDARRAYINDEX returns 2.

NOTE: Using GetLastModifiedArrayIndex OUTSIDE of an event (PUSH, RELEASE, CHANGE or EVENT) may return an index to an ambiguous signal if more than one input array is declared within the program. Therefore, do not use this function if more than one input signal array is declared within the program, unless you use it within one of the event statements.

Return Value:

The element of the array that has changed.

Example 1, Correct Use:

DIGITAL_INPUT LIGHT_SCENES[10], MORE_LIGHT_SCENES[10};

DIGITAL_OUTPUT INTERLOCKED_LIGHT_SCENES[10];

INTEGER I;

PUSH LIGHT_SCENES

{

FOR(I=1 to 10)

INTERLOCKED_LIGHT_SCENES[I] = 0;

ProcessLogic();

INTERLOCKED_LIGHT_SCENES[GetLastModifiedArrayIndex()] = 1;

}

Example 2, Incorrect Use:

DIGITAL_INPUT LIGHT_SCENES[10];

DIGITAL_OUTPUT INTERLOCKED_LIGHT_SCENES[10];

INTEGER I;

PUSH LIGHT_SCENES,MORE_LIGHT_SCENES[10]

{//this PUSH statement will be called twice (once for LIGHT_SCENES and once for MORE_LIGHT_SCENES)

FOR(I=1 to 10)

INTERLOCKED_LIGHT_SCENES[I]=0

ProcessLogic();

INTERLOCKED_LIGHT_SCENES[GetLastModifiedArrayIndex()] = 1;

}

}

In this example, when one input element changes, all the output elements are set to 0 and then the output level corresponding to the changed input level is set to 1. This mimics the functionality of the Interlock symbol in SIMPL.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Array_Operations/GetLastModifiedArrayIndex.htm*
