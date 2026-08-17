# Gather

Name:

Gather

Syntax:

STRING Gather(STRING Delimiter, STRING SourceString [INTEGER TimeOut]);

Description:

Concatenates the data from SourceString and issues it on the return string when the specified delimiter has been reached. At that time, the data will be removed from SourceString. Note that when Gather is executed, if SourceString does not include the Delimiter, then the equivalent of a PROCESSLOGIC is performed. When the system returns to the Gather, it will once again check for the proper delimiter. In effect, a section of code (a CHANGE statement, for example) is held up at the Gather until the proper data is received.

The optional Timeout parameter will provide a way for the function to transfer control back to the module when the specified time allows. If the Timeout parameter is specified, then the length of the return string should be checked to determine if a Timeout has occurred (length = 0).

Parameters:

Delimter is a string containing the terminating sequence of characters in the desired string.

SourceString is the string from which to remove the sequence of characters ending in the desired sequence.

Timeout is an integer specifying the timeout period in 1/100ths of a second.

NOTE: It makes sense only to use Gather with STRING_INPUT or BUFFER_INPUT types.

Return Value:

The returned string includes concatenated data from SOURCESTRING and the STRING DELIMITER.

Example:

BUFFER_INPUT COM$[100];

DIGITAL_INPUT trig;

STRING IN$[100];

PUSH trig

{

IN$ = GATHER("\n", COM$);

PRINT("The value of IN$ is %s\n", IN$);

}

In this example, the event is started when TRIG goes high. When data comes into COM$, the GATHER statement is evaluated. The PRINT statement is never reached until the delimiter \n (CRLF) is found. When the delimiter is found, then the string will be printed. Note that the GATHERed string will have the \n on it.

Example:

BUFFER_INPUT COM$[100];

DIGITAL_INPUT trig;

STRING IN$[100];

CHANGE COM$

{

IN$ = GATHER("\n", COM$);

PRINT("The value of IN$ is %s\n", IN$);

}

If, in the first event, COM$ contains the string "Hello", the event will wait in the GATHER. When the COM$ changes again to contain " World!\n", the event will immediately resume after the GATHER. The CHANGE COM$ event will only be called once in this case. In the X-Generation Control Systems, the CHANGE event would be called both times.

In the 2-Series Control System processors, a GATHER that is waiting for data will use up the next changes in the BUFFER_INPUT until the terminating character is encountered. That is, any CHANGE event handler for the BUFFER_INPUT will not be called. 

Version:

SIMPL+ Version 3.03.00 or later

CUZ3.154 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/GATHER.htm*
