# _OEM_PACING

Name:

_OEM_PACING

Syntax:

_OEM_PACING = <expression>;

or

Any expression that can use a variable as part of its contents.

Description:

Controls the number of milliseconds the system will delay between sending bytes in a given string. This variable is treated the same as ANALOG_OUTPUT. The maximum value allowed is 255 (250ms). Values greater than 255 will use the lower byte of the number.

Example:

CHANGE _OEM_STR_IN

{

IF(_OEM_STR_IN = "\x01\x02")

{

_OEM_STR_OUT = "\x02ACK\x03";

CLEARSTRING(_OEM_STR_IN);

}

}

FUNCTION MAIN()

{

_OEM_PACING = 10;

}

In this example, the pacing is set to 10ms. When the string "\x01\x02" comes into the port, a 5-byte string is sent out the port. The system waits 10ms after generating each character before sending the next one.

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/CEN-OEM_Specific_Definitions/_OEM_PACING.htm*
