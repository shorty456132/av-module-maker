# _OEM_RTS

Name:

_OEM_RTS

Syntax:

_OEM_RTS = <expression>;

or

Any expression that can use a variable as part of its contents.

Description:

This variable is treated the same as DIGITAL_OUTPUT. In a program where hardware handshaking is not being used, the program may control the RTS pin for its own application. Writing a non-zero value to this variable sets the RTS pin high, writing 0 sets it low.

Example:

PUSH _OEM_CTS

{

DELAY(10);

_OEM_RTS = 1;

}

In this program, the RTS pin will be driven high by the CEN-OEM 0.1-seconds after the CTS pin is driven high by an external system.

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/CEN-OEM_Specific_Definitions/_OEM_RTS.htm*
