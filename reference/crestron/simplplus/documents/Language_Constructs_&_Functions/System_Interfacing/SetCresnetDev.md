# SetCresnet  
  
Name:

SetCresnet

Syntax:

SetCresnet(INTEGER CRESNET_ID, INTEGER JOIN_NUMBER,

INTEGER TYPE);

Description:

Sets the state of the join number on a particular Cresnet Network ID. Note that the device must be defined in SIMPL and the join number to use must have a signal tied to it for this function to work.

Parameters:

CRESNET_ID is an INTEGER containing the ID of the Cresnet Network device to set the join number.

JOIN_NUMBER is an INTEGER containing the Join number to set.

TYPE is one of several predefined constants:

din: Digital inputs from device (symbol output list)

ain: Analog inputs from device (symbol output list)

dout: Digital outputs to device (symbol input list)

aout: Analog outputs to device (symbol input list)

Return Value:

None.

Example:

Assuming a touch screen has been defined at Cresnet ID 07, and press 42 and feedback 69 have signal names tied to them, this SIMPL+ statement will connect the two:

SetCresnet(0x07,69,dout) = GetCresnet(0x07,42,din);

NOTE: This is not a permanent connection; it will only set the state when this statement is executed.

Version:

X Generation: SIMPL v1.50.06 and later

2-Series: Not Supported.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/SetCresnetDev.htm*
