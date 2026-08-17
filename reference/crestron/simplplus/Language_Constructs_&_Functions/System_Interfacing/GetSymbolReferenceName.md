# GetSymbolReferenceName

Name:

GetSymbolReferenceName

Syntax:

STRING GetSymbolReferenceName();

Description:

Returns the string entered into the [Reference Name] SIMPL+ symbol in SIMPL corresponding to the SIMPL+ module.

NOTE: CIP is defined as Cresnet (over) Internet Protocol.

Parameters:

None.

Return Value:

Returns the string entered into the Reference Name field of a SIMPL+ symbol in SIMPL. If no Reference Name has been entered, an empty string is returned.

Example:

STRING RefName[20];

Function Main()

{

WaitForInitializationComplete();

RefName=GetSymbolReferenceName();

Print("Reference Name is: %s.\n", RefName);

}

Assuming the Reference Name Parameter is, for example, Kitchen Light Control, "Reference Name is: Kitchen Light Control" is the returned string.

Version:

SIMPL+ Version 3.03.00 or later

CUZ 3.154 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/GetSymbolReferenceName.htm*
