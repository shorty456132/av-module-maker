# GetSymbolInstanceName

Name:

GetSymbolInstanceName

Syntax:

STRING GetSymbolInstanceName();

Description:

Returns the symbol "S-" and the number where this SIMPL+ symbol is located within the SIMPL program.

Parameters:

None.

Return Value:

A string indicating the location of the SIMPL+ symbol in SIMPL. For example, if the SIMPL+ symbol is at S-5.2 in the SIMPL program, the returned string will be "S-5.2". If that same symbol resides in a macro that is located at S-6 in the SIMPL program, the returned string will be "S-6:S-5.2"

Example:

STRING InstanceName[20];

InstanceName=GetSymbolInstanceName();

Print("Instance Name is: %s", InstanceName);

Assuming the SIMPL+ symbol is located at S-5.2 in the SIMPL Program, the Instance Name is: S-5.2

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.154 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/GetSymbolInstanceName.htm*
