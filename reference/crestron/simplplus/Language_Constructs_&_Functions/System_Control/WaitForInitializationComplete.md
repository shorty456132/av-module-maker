# WaitForInitializationComplete

Name:

WaitForInitializationComplete

Syntax:

SIGNED_INTEGER WaitForInitializationComplete()

Description:

Waits for the logic processor to perform its first logic solution before returning control back to the calling task. This makes it possible to access inputs and outputs in function main() that are modified during the initial logic solution (propagating signals with logic "1" attached). The function Main() starts to run at when the Simpl+ module is initialized. This allows any initial values for global variables to be set before any event handlers are run. However, since it does run at initialization time, any inputs or outputs accessed would have their initial value of 0 when accessed. WaitForInitializationComplete will stop main() from running until the "Initialization Complete" message appears in Toolbox. This means that any input or output whose value is modified while processing the "1" logic solution, will now have the correct values.

Parameters:

None.

Return Value:

Returns 0 if successful , <0 if an error occurs.

Example:

DIGITAL_INPUT diEnable;

INTEGER giProcessEnabled;

main()

{

// initialize local variables.

giProcessEnabled = 0;

if ( WaitForInitializationComplete() < 0 )

{

print(Error waiting for initialization complete\n");

return;

}

// now we can access variables that were processed with the logic "1" solution

while (diEnable)

{

giProcessEnabled = 1;

// rest of the code for the process.

}

}

Version: 

X Generation: Not Supported

2-Series: SIMPL v2.05.17 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Control/WaitForInitializationComplete.htm*
