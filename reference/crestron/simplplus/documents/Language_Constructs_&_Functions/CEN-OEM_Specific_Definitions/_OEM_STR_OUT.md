# _OEM_STR_OUT

Name:

_OEM_STR_OUT

Syntax:

Any expression where a BUFFER_OUTPUT is legal.

Description:

This variable is treated the same as BUFFER_OUTPUT and reflects data coming from the CEN-OEM input buffer. The buffer is 255 bytes wide.

Example:

INTEGER I;

CHANGE _OEM_STR_OUT

{

FOR(I=1 to len(_OEM_STR_OUT))

IF(byte(_OEM_STR_OUT, I) = 0x7F

_OEM_STR_IN = "\x15";

CLEARSTRING(_OEM_STR_OUT);

}

In this example, whenever the input buffer changes, it is scanned for the character with the hex value of 0x7F. Each time it is present, a 0x15 is transmitted. The buffer is cleared at the end of the iteration.

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/CEN-OEM_Specific_Definitions/_OEM_STR_OUT.htm*
