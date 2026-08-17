# SendCresnetPacket

Name:

SendCresnetPacket

Syntax:

SendCresnetPacket(STRING PACKET);

Description:

Sends the string specified by PACKET onto the Cresnet network. It duplicates the function of the SIMPL symbol "Network Transmission (Speedkey: NTX)." This function is not used in general programming.

Parameters:

PACKET is a string containing the command to put on the Cresnet network.

Return Value:

None.

Example:

SendCresnetPacket("\xFF\x03\x02");

This example will send a broadcast message to all touchpanels causing them to enter sleep mode. The preferable way to do this is use the SLEEP input of the BROADCAST symbol in SIMPL.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/SendCresnetPacket.htm*
