# GatherByLengthWithDest

Name:

GatherByLengthWithDest

Syntax:

[SIGNED INTEGER] GatherByLengthWithDest(INTEGER NumCharsToMatch, BUFFER_INPUT Input, STRING Destination [,INTEGER Timeout]);

Description:

Concatenates the data from the BUFFER INPUT string into the destination string parameter till the specified number of characters has been reached. In effect, GatherByLengthWithDest is a version of the traditional [GatherByLength](<GatherByLength.htm>) function that holds the result of the gather operation in the destination string parameter, thus improving the operational speed of GatherByLengthWithDest over the speed of the [GatherByLength](<GatherByLength.htm>) function.

Note that similarly to the traditional [GatherByLength](<GatherByLength.htm>) function, GatherByLengthWithDest is a blocking operation i.e. the thread will stop executing until the gather condition is satisfied or the optional timeout expires.

Parameters:

NumCharsToMatch is an integer specifying the number of desired characters. 

Input is a BUFFER_INPUT variable that will receive data coming into the SIMPL+ module.

Destination is the destination string which will hold the result of the gather operation.

Timeout is an optional INTEGER parameter that allows the thread to continue to execute if the gather conditions are not met within the specified timeout period (in 1/100ths of a second.).

Return Values:

Return Value |  Description  
---|---  
0 |  Success  
<0 |  Error occurred  
-1 |  Timeout occurred  
-2 |  Resource conflict. Two threads are trying to access the same BUFFER_INPUT at the same time.  
  
Example:

BUFFER_INPUT MyInput[256];

DIGITAL_INPUT trig;

STRING dest[80];

PUSH trig

{

Signed_Integer Status;

Status = GatherByLengthWithDest(24, MyInput, dest);

PRINT ("The Value of dest is %s\n", dest);

}

In this example, the event is triggered when the DIGITAL_INPUT trig goes high. Data coming into MyInput is gathered until the specified number of characters has been reached. After that, the destination string will be printed.

Version:

SIMPL+ Version 4.05.01 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/GatherByLengthWithDest.htm*
