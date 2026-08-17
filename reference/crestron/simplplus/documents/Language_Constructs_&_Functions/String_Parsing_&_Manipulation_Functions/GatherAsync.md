# GatherAsync

Name:

GatherAsync

Syntax:

[SIGNED_INTEGER] GatherAsync (STRING Delimiter, BUFFER_INPUT Input, GatherEventHandler EventHandler, [INTEGER Timeout]);

Description:

Receives BUFFER_INPUT  data and flags it as waiting for a gather operation. When new data comes in from the logic engine, the match criteria will be evaluated. If the condition is met, i.e. specific sequence of characters is received, a thread will be triggered to invoke the callback function, thus eliminating the need for a separate thread waiting on each input, as each threads will only be active when there is work to be done.

If the Timeout parameter is specified and the match condition has not been met before this time expires, the callback function is invoked with a result code of timeout.

Parameters:

Delimiter is a specific sequence of characters that marks the end of the desired data

Input is a BUFFER_INPUT variable that will receive data coming into the SIMPL+ module.

EventHandler is the callback function which is invoked when the Delimiter is found

Timeout is an optional INTEGER parameter which specifies the timeout period (n 1/100ths of a second.) after which the callback function will be called and the result code in the [GatherEventArgs](<GatherEventArgs.htm>) parameter will be set to -1.

Return Value:

Returned value provides information about the status of the gather operation, as follows:

Return Value |  Description  
---|---  
0 |  Success  
<0 |  Error occurred  
-1 |  Problem with one of the parameters  
1 |  Success, but replacing previously set criteria  
  
Example:

DIGITAL_INPUT ByDelimiter;

PUSH ByDelimiter

{

GatherAsync(“\n”, MyInput, MyGatherCallback);

}

In this example, the event is triggered when the DIGITAL_INPUT ByDelimiter goes high. Data coming into MyInput is gathered until finding the delimiter '\n'. After the delimiter is found, MyGatherCallback is executed with the gathered data (including the delimiter) as an argument.

Version:

SIMPL+ Version 4.04.01 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/GatherAsync.htm*
