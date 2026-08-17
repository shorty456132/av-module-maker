# _OEM_CTS

Name:

_OEM_CTS

Syntax:

Any expression that can use a variable as part of its contents.

Description:

This variable is treated as a DIGITAL_INPUT and may be read from only. CTS is the acronym for Clear To Send. In flow control for handshaking, a device will typically control this line, and raise it high when the CEN-OEM is allowed to transmit, and drop it low when it wants the CEN-OEM to stop transmitting.

It can also be used in other situations besides flow control, and in these situations, the CEN-OEM can monitor the status of the line directly through this pin.

Example:

PUSH _OEM_CTS

{

PRINT("CTS Pin has gone high!\n");

}

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/CEN-OEM_Specific_Definitions/_OEM_CTS.htm*
