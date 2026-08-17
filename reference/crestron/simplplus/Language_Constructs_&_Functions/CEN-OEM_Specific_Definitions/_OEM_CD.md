# _OEM_CD

Name:

_OEM_CD

Syntax:

Any expression that can use a variable as part of its contents.

Description:

This variable is treated as a DIGITAL_INPUT and may be read from only. CD is the acronym for Carrier Detect. When a modem is hooked up to an RS-232 port and a connection (carrier) is made, the modem typically drives this pin high to let the connected hardware know that a data connection is present. This line may be used for other purposes depending on the hardware connected to the CEN-OEM.

Example:

PUSH _OEM_CD

{

PRINT("Carrier Detect Pin has gone high!\n");

}

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/CEN-OEM_Specific_Definitions/_OEM_CD.htm*
