# Task Switching for X-Generation (CNX) Control Systems

Each SIMPL+ module runs as a separate task in the X-Generation (CEN-TVAV, CNMSX-AV/PRO, CNRACKX/-DP) Control System. In order to insure that no SIMPL+ program takes up too much time, each task is allotted a certain amount of time to run. If the task exceeds this time limit, the system will switch out and allow other tasks (including the SIMPL program) to run.

The system will not arbitrarily switch out at any point in time. Even if the task limit is exceeded, the system will force a task switch only at predetermined points.

The system will perform a task switch when a PROCESSLOGIC, DELAY, or PULSE function is encountered. When a task switch is performed, the output I/O definitions are updated (refer to ANALOG_OUTPUT, DIGITAL_OUTPUT, STRING_OUTPUT for further information). Note that a WAIT does not cause a task switch.

When a WHILE, DO-UNTIL, or FOR construct encounters its last statement, or any construct that causes a "backwards branch", the system checks to see if a timeout has occurred. If the timeout has occurred, then the system will task switch away. When the module is given time to run, it will resume at the top of the construct.

For this reason, a designer of a SIMPL+ module should take care to design with this in mind. A particular concern is if the outputs need to be updated in a specific fashion and have a loop, which may potentially cause the system to switch away. One solution would be to store the output variables in intermediate arrays or variables, and assign the intermediate variables to the output variables before the event terminates.

For example:

DIGITAL_INPUT trig;

ANALOG_OUTPUT i;

INTEGER j;

PUSH trig

{

j=0;

FOR(j=0 to 32000)

{

i = j;

}

}

A SIMPL program drives the trig signal and monitors the state of the analog_output with an ANALOG DEBUGGER (Speedkey: TEST2) symbol. If the system did not task switch out, the only TEST2 output would show 32000. If this program were run, there would be many outputs, indicating each time the FOR loop exceeded the allotted time, the SIMPL program would be given time to run and the TEST2 symbol would post the results.

If it were critical that the analog_output were only updated with the final value, the following alternative solution could be used:

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

This program output would only show the final result; the TEST2 would be triggered once with the value 32000. The system will still perform whatever task switching it requires.

When an event has task switched away, it is possible that the event may be retriggered and a new copy of the event will start running. Therefore, SIMPL+ events are considered to be re-entrant. The event may be reentered only a limited number of times before an Rstack overflow error occurs (refer to "Common Runtime Errors" that begins on page 128). In order to prevent the event from running multiple times, consider the following example:

DIGITAL_INPUT trig;

INTEGER I;

PUSH trig

{

FOR(I = 0 TO 32000)

{

// code

}

}

This code will task switch away at some point in the FOR loop. If trig is hit again while the event is task switched out, a new copy will run. This code can be changed to prevent multiple copies from running.

DIGITAL_INPUT trig;

INTEGER I, Running;

PUSH trig

{

IF(!Running)

{

Running = 1;

FOR(I = 0 TO 32000)

{

// code

}

Running = 0;

}

}

FUNCTION MAIN()

{

Running = 0;

}

In this case, a new variable, Running is declared and set to 0 on system startup in the MAIN. When the event is triggered, if Running is 0, then it will be set to 1, and the FOR loop will execute. Assume now the event has a task switch. If trig is hit again, the event will start, but will immediately exit because IF statement evaluates to false. When the task resumes, and ultimately completes, Running will be set to 0 again so the bulk of the function may execute again.

NOTE: The event is STILL reentering. It is being forced to terminate immediately and prevent reentry more than one level deep.

---
*Source: https://help.crestron.com/simpl_plus/Content/Task_Switching/Task_Switching_for_CNX_Control_Systems.htm*
