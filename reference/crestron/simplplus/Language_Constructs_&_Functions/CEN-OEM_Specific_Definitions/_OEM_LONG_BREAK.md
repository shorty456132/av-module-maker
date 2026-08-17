# _OEM_LONG_BREAK

Name:

_OEM_LONG_BREAK

Syntax:

_OEM_LONG_BREAK = <expression>;

or

Any expression that can use a variable as part of its contents.

Description:

When set to a non-zero value, causes the start of a break being transmitted on the port. A break is continuous logic low being generated on the port. In order to stop break generation, the variable should be set to 0. The variable may also be read back from to determine its current status. It is treated the same as a DIGITAL_OUTPUT.

If break generation is in progress and data transmission on _OEM_STR_OUT will be ignored.

Example:

PUSH _OEM_CTS

{

_OEM_LONG_BREAK = 1;

WAIT(100)

_OEM_LONG_BREAK=0;

}

In this example, the break is generated for 1-second when the CTS pin is driven high.

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/CEN-OEM_Specific_Definitions/_OEM_LONG_BREAK.htm*
