# RemoveGatherAsync

Name:

RemoveGatherAsync

Syntax:

SIGNED_INTEGER RemoveGatherAsync (BUFFER_INPUT Input);

Description:

Removes/un-registers the specified BUFFER_INPUT serial data from the gather operation. 

Parameters:

Input is the BUFFER_INPUT associated with [GatherAsync](<GatherAsync.htm>) or [GatherAsyncByLength](<GatherAsyncByLength.htm>).

Return Value:

Returned value provides information about the status of the gather operation, as follows:

Return Value |  Description  
---|---  
0 |  Success  
<0 |  Error occurred  
-1 |  There was no previous gather operation for the specified BUFFER_INPUT  
  
Example:

DIGITAL_INPUT StopGather;

BUFFER_INPUT MyInput[256];

PUSH StopGather

{

RemoveGatherAsync(MyInput);

}

In this example, when DIGITAL_INPUT StopGather goes high the BUFFER_INPUT MyInput is removed from the Gather operation.

Version:

SIMPL+ Version 4.04.01 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/RemoveGatherAsync.htm*
