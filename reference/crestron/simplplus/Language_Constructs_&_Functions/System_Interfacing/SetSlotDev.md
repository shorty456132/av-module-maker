# SetSlot

Name:

SetSlot

Syntax:

SetSlot(INTEGER SLOT_NUMBER, INTEGER JOIN_NUMBER,

INTEGER TYPE);

Description:

Sets the state of the join number on a particular card slot. Note that the device must be defined in SIMPL and the join number to use must have a signal tied to it for this function to work.

Parameters:

SLOT_NUMBER is an INTEGER containing the slot number of card to set the join number.

JOIN_NUMBER is an INTEGER containing the Join number to set.

TYPE is one of several predefined constants:

din: Digital inputs from device (symbol output list)

ain: Analog inputs from device (symbol output list)

dout: Digital outputs to device (symbol input list)

aout: Analog outputs to device (symbol input list)

Return Value:

None.

Example:

Assuming a relay card has been defined in Slot 1 and Relay A2 has a signal name tied to it, and a touch screen has been defined at Cresnet ID 07, and press 42 has a signal name tied to it, this SIMPL+ statement will connect the two:

SetSlot(1,2,dout) = GetCresnet(0x07,42,din);

NOTE: This is not a permanent connection; it will only set the state when this statement is executed.

Version:

X Generation: SIMPL v1.50.06 and later

2-Series: Not Supported.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/SetSlotDev.htm*
