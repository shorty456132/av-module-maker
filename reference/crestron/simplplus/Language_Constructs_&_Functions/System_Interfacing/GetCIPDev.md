# GetCIP

Name:

GetCIP

Syntax:

INTEGER GetCIP(INTEGER CIPID, INTEGER JOIN_NUMBER,

INTEGER TYPE);

Description:

Retrieves the current state of the join number on a particular CIP ID (referred to as IP ID in SIMPL+). Note that the device must be defined in SIMPL and the join number to use must have a signal tied to it for this function to work.

NOTE: CIP is defined as Cresnet (over) Internet Protocol.

Parameters:

CIPID is an INTEGER containing the ID of the CIP device to query.

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

Assuming a relay card has been defined in Slot 1 and Relay A2 has a signal name tied to it, and a CEN-IO has been defined at CIP ID 03 and cue i1 has a signal tied to it, this SIMPL+ statement will connect the two:

SetSlot(1,2,dout) = GetCIP(0x03,18,din);

NOTE: In the above example statement, the join number representing cue i1 on the CEN-IO is 18.

NOTE: This is not a permanent connection; it will only set the state when this statement is executed.

Version:

X Generation: SIMPL v1.50.06 and later

2-Series: Not Supported.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/GetCIPDev.htm*
