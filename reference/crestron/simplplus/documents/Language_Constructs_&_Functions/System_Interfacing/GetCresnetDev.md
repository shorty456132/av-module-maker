# GetCresnet

Name:

GetCresnet

Syntax:

INTEGER GetCresnet(INTEGER CRESNET_ID, INTEGER JOIN_NUMBER,

INTEGER TYPE);

Description:

Retrieves the current state of the join number on a particular Cresnet Network ID. Note that the device must be defined in SIMPL and the join number to use must have a signal tied to it for this function to work.

Parameters:

CRESNET_ID is an INTEGER containing the ID of the Cresnet Network device to query.

JOIN_NUMBER is an INTEGER containing the Join number to get the status. For touchpanels, the join number is identical to the press/feedback number. For other devices, contact Crestron customer service.

TYPE is one of several predefined constants:

din: Digital inputs from device (symbol output list)

ain: Analog inputs from device (symbol output list)

dout: Digital outputs to device (symbol input list)

aout: Analog outputs to device (symbol input list)

NOTE: Access to serial signals is not supported.

Return Value:

An Integer. For Digital values, a non-zero value indicates a logic high and a 0 value indicates a logic low. For analog values, a 16-bit number is returned corresponding to the state of the analog join.

Example:

Assuming a relay card has been defined in Slot 1 and Relay A2 has a signal name tied to it, and a touch screen has been defined at Cresnet ID 07, and press 42 has a signal name tied to it, this SIMPL+ statement will connect the two:

SetSlot(1,2,dout) = GetCresnet(0x07,42,din);

NOTE: This is not a permanent connection; it will only set the state when this statement is executed.

Version:

X Generation: SIMPL v1.50.06 and later

2-Series: Not Supported.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/GetCresnetDev.htm*
