# GetDst

Name:

GetDst

Syntax:

INTEGER GetDst()

Description:

Gets the current DST (Daylight Savings Time) state. In order to set the DST state, a [Clock Driver](<Clock_Driver.htm>) symbol with a DST value is needed in the SIMPL Program.

Parameters:

None

Return Value:

An INTEGER containing the DST status:

0: Unknown

1: In DST

2: Not in DST

Example:

INTEGER DstMode;

DstMode = GetDst();

If(DstMode = 0)

Print("DST Mode is currently unknown.\n");

Else if (DstMode = 1)

Print("DST Mode is currently On (In DST).\n");

Else if (DstMode = 2)

Print("DST Mode is currently Off (Not in DST).\n");

This example will return one of the following strings based on the DST status:

DST Mode is currently Unknown.

DST Mode is currently On (In DST).

DST Mode is currently Off (Not in DST).

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.154 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/GETDST.htm*
