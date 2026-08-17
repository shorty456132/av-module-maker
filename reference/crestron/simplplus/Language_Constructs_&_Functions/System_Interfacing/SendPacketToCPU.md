# SendPacketToCPU

Name:

SendPacketToCPU

Syntax:

SendPacketToCPU(STRING PACKET);

Description:

Sends the string specified by PACKET to the Cresnet CPU. This is normally used for sending ESC style commands to the CPU for control. This function duplicates the functionality of the SIMPL symbol "Send Message to CPU (Speedkey: TMSG)." This function is not used in general programming.

Parameters:

PACKET is a string containing the command to send to the CPU.

Return Value:

None.

Example:

SendPacketToCPU("\x1BDFF\r");

This example will turn the Super Debugger on, which shows all network transitions on the console port of the control system. This command would normally be typed in manually through the Crestron Viewport, since it is for debugging only.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/SendPacketToCPU.htm*
