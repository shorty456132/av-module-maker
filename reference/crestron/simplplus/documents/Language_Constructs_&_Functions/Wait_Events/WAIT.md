# Wait

Name:

Wait

Syntax:

Wait(INTEGER |LONG_INTEGER TIME[, NAME])

[{]

<statements>

[}]

NOTE: There is no semicolon after a WAIT statement because it has a clause or block following it.

Description:

Adds an event to a list to be executed in TIME hundredths of a second. Giving a WAIT a name is optional, but to cancel, pause, resume, or retime a wait, a name must be specified. A currently running WAIT will finish before being entered into the WAIT list again. For example, if in an endless WHILE loop, a second WAIT will only begin after the first finishes.

When the system encounters a WAIT, the event is put into the WAIT scheduler. The SIMPL+ module continues to execute without interruption. At some point, a task switch will occur (either due to event termination or other means, refer to [Task Scheduling Changes and Consequences](<../../Task_Switching/Task_Scheduling_Changes_and_Consequences.htm>), [Task Switching for 2-Series Control Systems](<../../Task_Switching/Task_Switching_for_2-Series_Control_Systems.htm>) and [Task Switching for X-Generation (CNX) Control Systems](<../../Task_Switching/Task_Switching_for_CNX_Control_Systems.htm>)). The WAIT schedule is checked by the operating system after a task switch, and if a wait event needs to be serviced, it is run and then terminates. Note that the module may task switch away while inside the WAIT, just like in other events.

A WAIT statement differs from a DELAY in both timing and order of statement execution. In a WAIT statement, the WAIT block executes only after the specified amount of time, but execution proceeds immediately to the statement following the WAIT block. In a DELAY, all execution is halted until the delay is finished.

Parameters:

TIME is a long_integer, expressed in hundredths of a second. For example, 525 specifies a wait time of 5.25 seconds.

NAME is an optional name given to the WAIT event. It has the same syntax as a variable name. Note that you cannot put two separate WAIT statements in the same SIMPL+ program that have the same NAME (this will cause a compilation error).

NOTE: (2-Series Only) The only variable types that are allowed to be used within a Wait Statement block are global variables and variables declared locally within the Wait Statement's block. Local variables declared within the function containing the Wait Statement are not allowed.

NOTE: A semicolon should not be used at the end of the WAIT statement. If a semicolon is placed immediately after the wait statement, a compiler error will result. If braces are not following the WAIT statement, only the statement immediately following will be part of the WAIT statement. See example below.

Example:

LONG_INTEGER WaitTime;

DIGITAL_INPUT StopVCR;

ANALOG_INPUT SysWait;

STRING_OUTPUT VCR$;

PUSH StopVCR

{

WAIT (SysWait, VCR_Stop) // correct

{

VCR$ = "\x02STOP\x03";

}

WAIT (SysWait, VCR_Stop) // correct

VCR$ = "\x02STOP\x03"; // this is the only statement for this WAIT statement

VCR$ = "\x02PLAY\x03"; // will NOT be included in WAIT statement

WAIT (SysWait, VCR_Stop); // ERROR - semicolon should NOT be used

{

VCR$ = "\x02STOP\x03";

}

}

FUNCTION MyFunc()

{

while ( 1 )

{

// statements (will keep executing during the wait statement)

Wait( 500 )

{

// statements (execute once for each wait statement occurence)

}

// statements (will keep executing during the wait statement)

}

}

In this example, a VCR is triggered to go into STOP, but the STOP command is delayed based upon a time specified by an analog input to the SIMPL+ program.

Version:

X Generation

SIMPL v1.20.01 and later

2-Series:

SIMPL v2.01.05 and later [Same as X Generation SIMPL v1.20.01] however local variables are allowed within WAIT statements.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Wait_Events/WAIT.htm*
