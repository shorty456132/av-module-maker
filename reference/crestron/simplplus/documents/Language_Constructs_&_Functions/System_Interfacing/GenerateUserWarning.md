# GenerateUserWarning

Name:

GenerateUserWarning

Syntax:

GenerateUserWarning(<Static Specification String> [, <arg1> ...]);

Description:

Places a warning message into the control system's error log.

Parameters:

<Static Specification String> is a quoted string that contains text and formatting information. Format specifiers are of the form: %[[Pad]Width]specifier

See Print for a list and description of valid Format Specifiers.

Return Value:

None.

Example:

Function MyFunc()

{

STRING sWarning;

sWarning = "Projector";

GenerateUserWarning( "The %s bulb has a total of %d hours", sWarning, 800 );

}

Version:

X Generation: Not Supported

2-Series: SIMPL v2.04.11 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/GenerateUserWarning.htm*
