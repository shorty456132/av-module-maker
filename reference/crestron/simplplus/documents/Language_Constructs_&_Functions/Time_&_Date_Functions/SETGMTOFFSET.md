# SetGmtOffset

Name:

SetGmtOffset

Syntax:

SIGNED_INTEGER SetGmtOffset(SIGNED_INTEGER GmtOffset);

Description:

Sets the system GMT Offset. Can be used as an alternative to the GMTOFFSET console command.

Parameters:

A SIGNED_INTEGER containing the offset in minutes. Valid values are -720 through 780.

Return Value:

A SIGNED_INTEGER

0: Success

-1: Could not set (out of range)

Example:

// Set the GMT Offset to -300 minutes (-5 hours)

SIGNED_INTEGER return_code;

return_code = SetGmtOffset(-300);

if(return_code = -1)

print("Could not set GMT Offset, out of range.\n");

Error (-1) is returned.

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.154 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/SETGMTOFFSET.htm*
