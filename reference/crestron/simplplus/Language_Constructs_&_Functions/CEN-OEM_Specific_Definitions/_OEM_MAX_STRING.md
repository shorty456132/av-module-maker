# _OEM_MAX_STRING

Name:

_OEM_MAX_STRING

Syntax:

_OEM_MAX_STRING = <expression>;

or

Any expression that can use a variable as part of its contents.

Description:

Controls the maximum embedded packet size that is transmitted on the Ethernet port. This variable is treated the same as ANALOG_OUTPUT. The default is 250 bytes but it is recommended that this value not be changed for most applications.

Example:

_OEM_MAX_STRING = 1000; 

In this example, the maximum embedded packet size is changed to 1000 bytes.

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/CEN-OEM_Specific_Definitions/_OEM_MAX_STRING.htm*
