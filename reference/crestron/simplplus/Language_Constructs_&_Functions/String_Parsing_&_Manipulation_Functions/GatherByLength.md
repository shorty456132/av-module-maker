# GatherByLength

Name:

GatherByLength

Syntax:

STRING GatherByLength(INTEGER NumBytes, STRING SourceString [INTEGER Timeout]);

Description:

Concatenates the data from SourceString and issues it on the return string when the specified number of bytes have been reached. At that time, the data will be removed from SourceString. Note that when GatherByLength is executed, if SourceString does not include the specified number of bytes, then the equivalent of a PROCESSLOGIC is performed. When the system returns to the GatherByLength, it will once again check for the specified number of bytes (INTEGER NumBytes). In effect, a section of code (a CHANGE statement, for example) is held up at the GatherByLength until the specified NumBytes is received.

The optional Timeout parameter will provide a way for the function to transfer control back to the module when the specified time allows. If the Timeout parameter is specified, then the length of the return string should be checked to determine if a Timeout has occurred (length = 0).

Parameters:

NumBytes is an integer specifying the number of characters to be removed from the SourceString.

SourceString is the string from which to remove the sequence of characters ending in the desired sequence.

Timeout is an integer specifying the timeout period in 1/100ths of a second.

NOTE: It makes sense only to use GatherByLength with STRING_INPUT or BUFFER_INPUT types.

Return Value:

The length of the returned string is the NumBytes specified.

Example:

BUFFER_INPUT COM$[100];

DIGITAL_INPUT trig;

STRING IN$[100];

PUSH trig

{

IN$ = GATHERBYLENGTH(2, COM$);

PRINT("The value of IN$ is %s\n", IN$);

}

In this example, the event is started when TRIG goes high. When data comes into COM$, the GatherByLength statement is evaluated. The PRINT statement is never reached until the number of bytes, NumBytes, is obtained. When the total number of bytes specified is obtained, then the string will be printed.

Example:

BUFFER_INPUT COM$[100];

DIGITAL_INPUT trig;

STRING IN$[100];

CHANGE COM$

{

IN$ = GATHER(2, COM$);

PRINT("The value of IN$ is %s\n", IN$);

}

If, in the first event, COM$ contains the string "Hello", the event will wait in the GATHERBYLENGTH. When the COM$ changes again to contain " World!\n", the event will immediately resume after the GATHERBYLENGTH. The CHANGE COM$ event will only be called once in this case.

In the 2-Series Control System processors, a GATHERBYLENGTH that is waiting for data will use up the next changes in the BUFFER_INPUT until the number of bytes is obtained. That is, any CHANGE event handler for the BUFFER_INPUT will not be called. 

Example:

#DEFINE_CONSTANT GATHERBYLENGTH_TIMEOUT 200 // 2 second timeout

BUFFER_INPUT MyLengthString[1000];

CHANGE MyDelimitedString

{

STRING LocalString[256];

While (1)

{

LocalString = GatherByLength(2, MyDelimitedString, GATHER_TIMEOUT);

If (Len(LocalString) = 0) // timeout occurred

{

ClearBuffer(MyDelimitedString);

Print("Timeout occurred in Delimited string. \n");

Break;

}

// code to work with received string

}

}

CHANGE MyLengthString

{

STRING LocalString[256];

While (1)

{

LocalString = GatherByLength(20, MyLengthString, GATHER_TIMEOUT);

If (Len(LocalString) = 0) // timeout occurred

{

ClearBuffer(MyLengthString);

Print("Timeout occurred in Length string. \n");

Break;

}

// code to work with received string

}

}

In this example, GatherByLength would continue to remove the specified number of bytes in MyLengthString until it was empty, which would cause a timeout.

Version:

SIMPL+ Version 3.03.00 or later

CUZ3.154 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/GatherByLength.htm*
