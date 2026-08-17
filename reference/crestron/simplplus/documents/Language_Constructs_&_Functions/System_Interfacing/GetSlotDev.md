# GetSlot

Name:

GetSlot

Syntax:

INTEGER GetSlot(INTEGER SLOT_NUMBER, INTEGER JOIN_NUMBER,

INTEGER TYPE);

Description:

Retrieves the current state of the join number on a particular card. Note that the device must be defined in SIMPL and the join number to use must have a signal tied to it for this function to work.

Parameters:

SLOT_NUMBER is an INTEGER containing the slot number of the card to query.

JOIN_NUMBER is an INTEGER containing the Join number to get the status.

TYPE is one of several predefined constants:

din: Digital inputs from device (symbol output list)

ain: Analog inputs from device (symbol output list)

dout: Digital outputs to device (symbol input list)

aout: Analog outputs to device (symbol input list)

NOTE: Access to serial signals is not supported.

Return Value:

An Integer. For Digital values, a non-zero value indicates a logic high and a 0 value indicates a logic low. For analog values, a 16-bit number is returned corresponding to the state of the analog join.

Example:

Assuming a relay card has been defined in Slot 1 and Relay A2 has a signal name tied to it, and a CNXIO-16 has been defined in Slot 2 and cue i1 has a signal tied to it, this SIMPL+ statement will connect the two:

SetSlot(1,2,dout) = GetSlot(2,1,din);

NOTE: This is not a permanent connection; it will only set the state when this statement is executed.

Version:

X Generation: SIMPL v1.50.06 and later

2-Series: Not Supported.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/GetSlotDev.htm*
