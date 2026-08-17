# RearmGatherAsync  
  
Name:

RearmGatherAsync

Syntax:

SIGNED_INTEGER RearmGatherAsync (BUFFER_INPUT Input);

Description:

Resets the Gather trigger to the criteria used in the previous match. When criteria in [GatherAsync](<GatherAsync.htm>) or [GatherAsyncByLength](<GatherAsyncByLength.htm>). is met, the callback function [GatherEventHandler](<GatherEventHandler.htm>) will be triggered once. If a further match is desired, the RearmGatherAsync function has to be called as the end line of [GatherEventHandler](<GatherEventHandler.htm>).

Parameters:

Input is the buffer input associated with the [GatherAsync](<GatherAsync.htm>) or [GatherAsyncByLength](<GatherAsyncByLength.htm>).

Return Value:

Returned value provides information about the status of the gather operation, as follows:

Return Value |  Description  
---|---  
0 |  Success  
<0 |  Error occurred  
-1 |  There was no previous gather operation for the specified BUFFER_INPUT  
  
Example:

callback GatherEventHandler MyGatherCallback(GatherEventArgs Args)

{

if (Args.RESULTS = 0)

{

RearmGatherAsync(Args.INPUT);

}

else

...

}

In this example, the callback function, the RearmGatherAsync is called so to utilize the same gather criteria that was used in the previous gather operation.

Version:

SIMPL+ Version 4.04.01 or later required

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/RearmGatherAsync.htm*
