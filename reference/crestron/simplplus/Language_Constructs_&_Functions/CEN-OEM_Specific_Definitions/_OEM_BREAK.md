# _OEM_BREAK

Name:

_OEM_BREAK

Syntax:

_OEM_BREAK = <expression>; // Write to Variable

or

Any expression that can use a variable as part of its contents.

Description:

When set to a non-zero value, causes a short break to be transmitted on the port. A Short break is 17-20 bits of logic low. When the system is done generating the short break, it will set the variable to 0. The variable may also be read back from to determine its current status. It is treated the same as a DIGITAL_OUTPUT.

Example:

_OEM_BREAK = 1; // Generate A Short Break

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/CEN-OEM_Specific_Definitions/_OEM_BREAK.htm*
