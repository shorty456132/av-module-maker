# Task Switching for 2-Series Control Systems

In the 2-Series Control Systems, each SIMPL+ module also runs as one or more concurrent tasks in the control system. The MAIN and each event handler run as separate tasks sharing a common global data space.

NOTE: the following applies to 2-series firmware prior to release 3.137. For information about release 3.137 and higher, refer to [Task Scheduling Changes and Consequences](<Task_Scheduling_Changes_and_Consequences.htm>)

NOTE: Also refer to [Task Switching for X-Generation (CNX) Control Systems](<Task_Switching_for_CNX_Control_Systems.htm>) for a discussion of task switching in that environment.

To insure that no SIMPL+ program takes too much time, each task is allotted a certain amount of time to run. If the task exceeds this time limit, the system will switch out and allow other tasks (including the SIMPL program) to run. It should also be noted that the task would run until it has completed the operation, the allotted time expires or a task switching call is executed.

Unlike the X-Generation systems, the system will arbitrarily switch out at any point in time. If this may result in undesirable behavior, then the programmer should control his task switching by issuing a PROCESSLOGIC function.

The system will perform a task switch when a PROCESSLOGIC or DELAY function is encountered. The PULSE will no longer cause a task switch because it is no longer needed for the logic processor to process the digital output pulse. Note that a WAIT does not cause a task switch but will execute in its own task.

All outputs are processed by the logic processor as soon as assigned. As soon as the SIMPL+ module releases the processor, all the outputs are seen by the logic processor. Also, the programmer can read back DIGITAL_OUTPUTS and ANALOG_OUTPUTS without having to insert a PROCESSLOGIC in between. 

To use the example from the Task Switching for X-Generation Control System discussion:

DIGITAL_INPUT trig;

ANALOG_OUTPUT i;

ANALOG_OUTPUT NewNumber;

INTEGER j;

PUSH trig

{

j=0;

NewNumber = 1234;

j = NewNumber; //j = 1234, not old value of NewNumber

FOR(j=0 to 32000)

{

i = j;

}

}

A SIMPL program drives the trig signal and monitors the state of ANALOG_OUTPUT with an ANALOG DEBUGGER (Speedkey: TEST2) symbol. The TEST2 output would show all numbers from 0 to 32000. If it were critical that the ANALOG_OUTPUT were only updated with the final value, the following alternative solution could be used:

DIGITAL_INPUT trig;

ANALOG_OUTPUT i;

INTEGER j, q;

PUSH trig

{

j=0;

FOR(j=0 to 32000)

{

q = j;

}

i = q;

}

This program output would only show the final result; the TEST2 would be triggered once with the value 32000. The system will still perform whatever task switching required.

As with the X-Generation series, re-entrancy can still be a problem. When an event has task switched away, the event may be retriggered and a new copy of the event will start running. Therefore, SIMPL+ events are considered to be re-entrant. The amount of times that this could occur is dependent upon the available memory in the system. In order to prevent the event from running multiple times, refer to the re-entrant example in the X-Generation task switching section.

The programmer should exercise caution when using looping constructs without constraints (i.e. while(1) ) or depend upon outside influence. Because each event will run for the allotted time unless specified otherwise, PROCESSLOGIC calls should be used to reduce the CPU overhead. Consider the following:

DIGITAL_INPUT diInput1, diInput2;

INTEGER I, LastNumSeconds;

PUSH diInput1

{

WHILE (diInput1)

{

// do something

}

}

main()

{

LastNumSeconds = 0;

WHILE (1)

{

seconds = GetSecondsNum();

IF (seconds <> LastNumSeconds)

{

// do something

}

}

}

At the loop in MAIN, the programmer wants to perform an operation every second. This code will achieve that goal. However, a side effect of the code is that every time the task is scheduled to run, it will sit in a very tight loop checking for a change in the number of seconds. Since the allotted time for a SIMPL+ task to run is in fractions of a second, it is very unlikely to change during the allotted time. Unless the programmer puts in a DELAY which will put the task to "sleep" for a period of time, this task will dominate the CPU time.

The programmer who writes the MAIN() function should also be aware that the MAIN() function begins running when the SIMPL program is initializing. The module's inputs do not have this programmed state until sometime after the first break in the program execution due either to a process logic statement, delay, or expiration of a time slice.

The PUSH event indicates a more subtle problem. The programmer wants to loop in the event until the input diInput1 is released. Once the task containing the event is started, it will run for its allotted time and no other inputs will change. If the signal attached to the diInput1 signal goes low, the event will not see the change until the event switches out and the diInput1 low signal is processed. 

The following is an alternative:

DIGITAL_INPUT diInput1, diInput2;

INTEGER I, LastNumSeconds;

PUSH diInput1

{

WHILE (diInput1)

{

// do something

ProcessLogic();

}

}

MAIN()

{

LastNumSeconds = 0;

WHILE (1)

{

seconds = GetSecondsNum();

IF (seconds <> LastNumSeconds)

{

// do something

}

delay(10);

}

}

Here, a 100ms delay is put in the MAIN loop. That means that the task will only wake up 10-times per second. It will still catch the change of the seconds to within a 1/10 of a second and lessen system requirements. 

The PROCESSLOGIC call in the PUSH event handler will immediately cause a task switch to be performed. This will allow a low transition on the diInput1 signal to be seen immediately, making the system more responsive.

One more operational difference between the X-Generation and 2-Series control systems is the event interaction. For example:

DIGITAL_INPUT diEvent1, diEvent2;

PUSH diEvent1

{

PRINT("Starting Event 1\n");

DELAY(500); // 5 sec delay

PRINT ("Event 1 done\n");

}

PUSH diEvent2

{

PRINT ("Starting Event 2\n");

DELAY (1500); // 15 sec delay

PRINT ("Event 2 done\n");

}

The output from the X-Generation system would be:

Starting Event 1

Starting Event 2

Event 2 Done

Event 1 Done

The order dictates that the second delay (15 seconds) will hold off the first delay. As soon as the second delay has finished, the first delay is checked. Therefore, the two events complete at approximately the same time (15 seconds).

The output from the 2-Series system would be:

Starting Event 1

Starting Event 2

Event 1 Done

Event 2 Done

The events run independently. When the 5-seconds expires for the first delay, the first event continues and prints its message. The second delay expires 10 seconds later and the message is displayed.

---
*Source: https://help.crestron.com/simpl_plus/Content/Task_Switching/Task_Switching_for_2-Series_Control_Systems.htm*
