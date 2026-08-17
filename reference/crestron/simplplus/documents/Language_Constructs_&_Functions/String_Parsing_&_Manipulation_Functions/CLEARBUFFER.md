# ClearBuffer

Name:

ClearBuffer

Syntax:

ClearBuffer(STRING BUFFERNAME);

Description:

Deletes the contents of the specified buffer. If a LEN is done on the buffer after a CLEARBUFFER, the return value will be 0. This is equivalent to assigning an empty string to the buffer, e.g., BUFFERNAME="";

Parameters:

BUFFERNAME specifies the name of the string to empty. BUFFER_INPUT, STRING, and STRING_INPUT sources are legal.

Return Value:

None.

Example:

BUFFER_INPUT IN$[100];

CHANGE IN$

{

IF(RIGHT$(IN$,1) = "Z")

CLEARBUFFER(IN$);

// Code to process IN$ goes here.

}

In this example, if the last character that comes into the BUFFER_INPUT is "Z", the buffer is cleared.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/CLEARBUFFER.htm*
