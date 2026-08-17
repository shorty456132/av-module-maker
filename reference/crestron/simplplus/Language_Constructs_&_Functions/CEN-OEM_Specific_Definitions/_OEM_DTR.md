# _OEM_DTR

Name:

_OEM_DTR

Syntax:

_OEM_DTR = <value>;

or

Any expression that can use a variable as part of its contents.

Description:

When set to a non-zero value, raises the DTR pin high. This pin is typically used to signify "Data Terminal Ready", which means that the CEN-OEM is telling an external piece of equipment that it is online and ready to function. The pin may be used for other purposes (or not at all). This value is treated as a DIGITAL_OUTPUT and may be read.

Example:

PUSH _OEM_CTS

{

PULSE(500, _OEM_DTR);

}

The above example will pulse the DTR pin for 5-seconds when the CTS line goes high.

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/CEN-OEM_Specific_Definitions/_OEM_DTR.htm*
