# Task Scheduling Changes and Consequences

NOTE: the following applies to 2-series firmware 3.137 and higher.

The previous scheduling algorithm method for SIMPL+ events caused unexpected results when writing multiple files simultaneously to compact flash. We will describe both the old and new algorithms. This advanced topic assumes that you are familiar with the 2-series task-switching topic [Task Switching for 2-Series Control Systems](<Task_Switching_for_2-Series_Control_Systems.htm>).

NOTE: Also refer to [Task Switching for X-Generation (CNX) Control Systems](<Task_Switching_for_CNX_Control_Systems.htm>) for a discussion of task switching in that environment.

Overview

One of the premises of a SIMPL+ module is that it has to appear to be the same as any other logic gate in terms of logic delays. That means that the SIMPL+ code should transfer its inputs into outputs in one logic wave. This is not always possible due to what the programmer has coded into the SIMPL+ module. Because the programmer can put delays or loops in his code, the SIMPL+ code is limited in the amount of time it can run before logic resumes. This slice of time is currently 20 milliseconds. 

Initial Design

In the initial design for the 2-series, the SIMPL+ code ran at the lowest priority in the system. This priority level was chosen to prevent SIMPL+ code from blocking other code from running. For example, if the programmer used a “while(1)” loop without any delays, no lower priority code would ever run. The mechanism for getting SIMPL+ to run as a logic gate required the logic processor to pause to allow for the SIMPL+ code to start running. The logic processor would wait for a maximum of 0.5 seconds before resuming. If the SIMPL+ task has not started after waiting 0.5 seconds, the processor generates a “SIMPL+ Event Timeout” error message. This is caused by other parts of the system occupying the processor besides the logic processor. 

Also, in the initial design, the SIMPL+ code was marked as non-preemptive. This means that while the SIMPL+ code was running, no other process in the system could interrupt its execution. The code ran until it finished, release control temporarily back to the control system (delay() or ProcessLogic()), or its allotted time of 20 ms ran out. This is the portion that may interfere with the low level operations of the file system. Low-level function calls dealing with file operations would mark the current task as non-preemptive. The system then assumed that no other task could interrupt the current task while it was non-preemptive. Since SIMPL+ would timeslice out and release the processor, if another SIMPL+ task performed a file operation, possible data corruption could occur.

Redesign

The goal of the redesign was to allow SIMPL+ to be able to run in a preemptive mode while still maintaining its logic wave propagation as well as protect against runaway user code. The initial timeslice for SIMPL+ code will execute at a priority higher than the logic processor for code generated from events and the function Main(). This allows the signals to propagate as a logic wave. If the SIMPL+ code either returns control back to the operating system (delay() or ProcessLogic()) or its 20 ms timeslice expires, the SIMPL+ task will then drop to the lowest priority in the system to protect against runaway SIMPL+ code. It should be noted that Wait() events always run at the lowest priority. There is no logic wave propagation requirement for Wait() events.

The new design resolves the possible conflicts with the low-level constructs of the system that was causing problems during file operations. Since there was no alternative to correcting these conflicts, we needed to make the SIMPL+ tasks preemptive. 

Now that the SIMPL+ code starts at a higher priority than logic, there is the possibility that SIMPL programs will operate differently. Most notable will be SIMPL+ events fired from SIMPL+ code running at the low priority. This could be a Wait() statement or any SIMPL+ code after it has called ProcessLogic(). For example, if a Wait() statement set a digital output high and that signal went to trigger other SIMPL+ code, the new SIMPL+ code would run before the rest of the Wait() statement. This will create subtle timing changes that should be negligible for most applications. 

Example

The following is an example of SIMPL+ code that demonstrates a timing change caused by the new algorithm. 

/*

Comments: This is a test to demonstate what happens when a Wait() statement

triggers an input in the same module. The premise behind the

module is that a device can only process commands one at a time. 

The SIMPL program must wait until it either gets a response

from the device or a timeout occurs. 

In this example program, there is no device attached to the com

port so the timeout will always occur. It is the timeout code in

the Wait() statement that is causing the change that is seen in

firmware 3.137. This modules emulates talking to two devices. The

code for both devices is almost identical with the exception that

device 2 code has a ProcessLogic() call before its Wait() statement.

This reverts the scheduling to the old method.

*/

#DEFINE_CONSTANT MAX_NUM_RETRIES 4

#DEFINE_CONSTANT TIMEOUT_VALUE 100 // use a 1 second timeout

#DEFAULT_NONVOLATILE

#ENABLE_STACK_CHECKING

DIGITAL_INPUT diEnable1; // start sending commands.

DIGITAL_INPUT diTrigger1; // Resend the last command or get the next one.

DIGITAL_INPUT diEnable2; // start sending commands.

DIGITAL_INPUT diTrigger2; // Resend the last command or get the next one.

STRING_INPUT siRx1$[1024]; // Holds the response from the first device.

BUFFER_INPUT biCmdQueue1[1024]; // Commands to send to the first device.

STRING_INPUT siRx2$[1024]; // Holds the response from the second device.

BUFFER_INPUT biCmdQueue2[1024]; // Commands to send to the second device.

DIGITAL_OUTPUT doResend1; // this will be wrapped around to diTrigger1

DIGITAL_OUTPUT doResend2; // this will be wrapped around to diTrigger2

DIGITAL_OUTPUT doTest1Complete; // For thistest only, clears the Enable input

DIGITAL_OUTPUT doTest2Complete;

STRING_OUTPUT soTx1$; // Data to send to device 1.

STRING_OUTPUT soTx2$; // Data to send to device 2.

// Global Variables

INTEGER iCmdSendCnt1, iCmdSendCnt2; // Retry counters

STRING sCmd1[80], sCmd2[80]; // holds the last command sent

INTEGER_Function ExtractCommand1()

{

if (Find("\n", biCmdQueue1) > 0)

{

sCmd1 = Remove("\n", biCmdQueue1);

if (len(sCmd1) > 0)

{

iCmdSendCnt1 = 0;

return (1);

}

}

else // Queue is empty. Test is over. This is used for our test only.

{

doTest1Complete = 1;

doTest1Complete = 0;

}

return (0);

}

Function SendCommand1()

{

/* The Wait() statement pulses the Resend signal. This will cause an PUSH

event to be generated. In firmware version 3.137 and above, the PUSH

event runs before the code in the Wait() statement finished. Since the

trigger event calls this routine again, the Wait() statement will not

get scheduled because it is still running in a different thread. 

*/

soTx1$ = sCmd1;

iCmdSendCnt1 = iCmdSendCnt1 + 1;

wait(TIMEOUT_VALUE, ResponseTimeout1)

{

doResend1 = 1;

doResend1 = 0;

} 

}

INTEGER_Function ExtractCommand2()

{

if (Find("\n", biCmdQueue2) > 0)

{

sCmd2 = Remove("\n", biCmdQueue2);

if (len(sCmd2) > 0)

{

iCmdSendCnt2 = 0;

return (1);

}

}

else // Queue is empty. Test is over. This is used for our test only.

{

doTest2Complete = 1;

doTest2Complete = 0;

}

return (0);

}

Function SendCommand2()

{

/* The Wait() statement pulses the Resend signal. This will cause an PUSH

event to be generated. In firmware version 3.137 and above, the PUSH

event runs before the code in the Wait() statement finished. By calling

ProcessLogic(), the PUSH event task is scheduled at the same priority of

the Wait() event task and will run after the Wait() event has finished.

This allows the PUSH event task to schedule a new Wait() timeout for the

new command sent.

*/

soTx2$ = sCmd2;

iCmdSendCnt2 = iCmdSendCnt2 + 1;

ProcessLogic();

wait(TIMEOUT_VALUE, ResponseTimeout2)

{

doResend2 = 1;

doResend2 = 0;

} 

}

// Event Handlers

PUSH diEnable1

{

if (ExtractCommand1() = 1)

SendCommand1();

}

PUSH diEnable2

{

if (ExtractCommand2() = 1)

SendCommand2();

}

/* These RELEASE events are added to rerun the test. Clear the buffers because

the queue will be reprimed when the test ends

*/

RELEASE diEnable1

{

ClearBuffer(biCmdQueue1);

}

RELEASE diEnable2

{

ClearBuffer(biCmdQueue2);

}

PUSH diTrigger1

{

if (iCmdSendCnt1 >= MAX_NUM_RETRIES) // get the next command

{

if (ExtractCommand1() = 1)

{

SendCommand1();

}

}

else

{

SendCommand1();

}

}

PUSH diTrigger2

{

if (iCmdSendCnt2 >= MAX_NUM_RETRIES) // get the next command

{

if (ExtractCommand2() = 1)

{

SendCommand2();

}

}

else

{

SendCommand2();

}

}

CHANGE biCmdQueue1

{

if (diEnable1)

{

SendCommand1();

}

}

CHANGE biCmdQueue2

{

if (diEnable2)

{

SendCommand2();

}

}

CHANGE siRx1$

{

CancelWait(ResponseTimeout1);

// get next command

if (ExtractCommand1() = 1)

SendCommand1();

}

CHANGE siRx2$

{

CancelWait(ResponseTimeout2);

// get next command

if (ExtractCommand2() = 1)

SendCommand2();

}

Function Main()

{

iCmdSendCnt1 = 0;

iCmdSendCnt2 = 0;

}

Glossary

Preemptive – A process that will be interrupted when a higher priority process is ready to execute.

Non-preemptive – A process that will continue to run even though a higher priority process is waiting to execute. 

Timeslice – A period of time that a process is allowed to execute before relinquishing the processor for other processes.

---
*Source: https://help.crestron.com/simpl_plus/Content/Task_Switching/Task_Scheduling_Changes_and_Consequences.htm*
