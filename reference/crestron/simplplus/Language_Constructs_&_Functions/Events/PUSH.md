# PUSH

Name:

PUSH

Syntax:

PUSH <variable_name1> [, <variable_name2> ...]

{

[Local Variable Definitions]

<statements>

}

Description:

PUSH is executed when a DIGITAL_INPUT transitions from low to high.

<variable_name> is a DIGITAL_INPUT type. On the rising edge of <variable_name>, the statements between the opening { and closing } are executed.

When using DIGITAL_INPUT arrays, only a change in the entire array can be detected, not an individual element. Refer to [GetLastModifiedArrayIndex](<../Array_Operations/GetLastModifiedArrayIndex.htm>) for a method of detecting a change to an individual element.

When listing multiple variable names, the names can be put on the same line or broken up into several PUSH statements for readability.

(see also [StackedEvents](<Stacked_Events.htm>) AND [THREADSAFE](<THREADSAFE.htm>))

Example:

DIGITAL_INPUT trigger;

STRING_OUTPUT output$;

PUSH trigger

{

output$ = "Hello, World!";

}

In this example, when the DIGITAL_INPUT trigger transitions from low to high, the STRING_OUTPUT output$ will have the string "Hello, World!" put into it.

Version:

X Generation:

SIMPL v1.20.01 and later

SIMPL v1.50.06 and later, DIGITAL_INPUT arrays as <variable_name>

2-Series:

SIMPL v2.01.05 and later [Same as X Generation SIMPL v1.50.06] and Local Variables allowed within PUSH Statements.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Events/PUSH.htm*
