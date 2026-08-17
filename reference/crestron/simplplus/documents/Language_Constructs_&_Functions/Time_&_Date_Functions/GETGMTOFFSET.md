# GetGmtOffset

Name:

GetGmtOffset

Syntax:

SIGNED_INTEGER GetGmtOffset();

Description:

Retrieves the GMT Offset that was configured via the consol command GMTOFFSET or through the SetGmtOffset() function.

Parameters:

None.

Return Value:

A SIGNED_INTEGER containing the offset in minutes.

Example:

SIGNED_INTEGER SystemGmtOffset;

SystemGmtOffset = GetGmtOffset();

Print("GmtOffset = %d minutes\n", SystemGmtOffset);

In this example the GmtOffset would be the value of %d expressed as a positive or negative number.

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.154 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETGMTOFFSET.htm*
