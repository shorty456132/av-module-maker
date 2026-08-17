# Working with Time

Up until now, this manual has discussed elements of the SIMPL+ language that have no concept of time. This means that each statement in a SIMPL+ program executes after the previous statement is completed. There are times when programming where there is a need to have control over exactly when the statements in the program execute. This section deals with those language constructs.

## Delay

The **Delay** function pauses the execution of the current SIMPL+ for the time specified in the parameter field. As with most time values in SIMPL+, this time value is specified in hundredths of seconds. The following program causes the program to stop for five seconds before resuming.

PUSH startMe  
{  
Print("I’m starting now...");  
Delay(500); //this equals 5 seconds  
Print("and I’m ending 5 seconds later.\n");} 

It is important to realize that the control system never allows a SIMPL+ program to lock up the rest of the system for any significant amount of time. Thus, whenever a delay function is reached, the control system performs a task switch, meaning that the execution of the current SIMPL+ module stops momentarily as the natural flow through the SIMPL program continues. In this case, even though the SIMPL+ program has stopped for five seconds, other code in the overall SIMPL program (including standard logic symbols and other SIMPL+ modules) continues to operate normally. The concept of task switching is covered in more detail in the section [Understanding Processing Order](<../Understanding_Processing_Order/TP_Understanding-Processing-Order.htm>).

## Pulse

The **Pulse** function is used to drive a digital output signal high for a specified amount of time. Once again, the time is specified in hundredths of seconds. When a **Pulse** statement is executed, the digital output signal specified is driven high and a task switch occurs. Such a task switch is necessary in order for the rest of the SIMPL program to recognize that the digital signal has indeed gone high. After the time specified has expired, the digital output is driven low and another task switch occurs. The following program causes the digital output signal, **preset_1** , to be pulsed for a half a second.

#DEFINE_CONSTANT PULSE_TIME 50

DIGITAL_OUTPUT preset_1, preset_2, preset_3;

PUSH some_input  
{  
Pulse(PULSE_TIME, preset_1);}

The **Pulse** function is very similar in operation to the SIMPL One Shot symbol. In fact, in many cases, it may be more convenient (or more sensible) to simply connect a One Shot, or Multiple One Shot symbols to the output signals of a SIMPL+ module.

Also notice that unlike the **Delay** function, **Pulse** does not cause a pause in the execution of the SIMPL+ code. Therefore, the statements that follow the **Pulse** execute immediately and do not wait for the expiration of the pulse time.

## Wait Events

Wait events in SIMPL+ allow operations that are somewhat similar to the Delay SIMPL logic symbol. The syntax for a Wait event is as follows.

Wait (wait_time [, wait_name])  
{  
<statements>}

This syntax defines a Wait event to occur at some time in the future, defined by the value of **wait_time**. While the Wait event is pending execution, it is said to have been scheduled. The Wait event may have an optional name, which can be used to refer back to the event elsewhere in the code.

When a Wait event definition is reached during execution, the execution of the statements inside the braces (these braces are not needed if the event is only one statement long) is deferred until the time defined by **wait_time** has expired. Until this occurs, the remainder of the SIMPL+ program executes. If a Wait event definition is nested inside of a loop, it is possible that it can be reached multiple times before it even executes once. If a Wait event is pending (i.e., has been scheduled, but not executed), it is not scheduled again until it has been completed.

Once a Wait event has been scheduled to execute at some later point in time, various operations can be performed on the event before it actually executes. However, only named Wait events can be modified in this manner, since it is necessary to use the name to refer to the event. The table on the next page lists the available functions, which can operate on Wait events.

Functions Available During Wait Events Function | Description  
---|---  
CancelWait(name) | Removes the named wait from the schedule. The code never executes.  
CancelAllWait() | Removes all pending waits from the schedule.  
PauseWait(name) | Stops the timer for the named wait. The code does not execute until the timer is started again using ResumeWait().  
ResumeWait(name) | Resumes the timer for the named wait, which had been paused earlier.  
PauseAllWait() | Similar to PauseWait(), but acts on all pending wait events.  
ResumeAllWait() | Similar to ResumeWait(), but acts on all paused wait events.  
RetimeWait(time, name) | Sets the time for a pending wait event to the value specified.  
  
This example shows a typical use of wait events. Here, the **SYSTEM ON** button starts a power up sequence and the **SYSTEM OFF** button likewise starts a power down sequence.

#DEFINE_CONSTANT PULSETIME 50 // half second

DIGITAL_INPUT system_on, system_off;  
DIGITAL_OUTPUT screen_up, screen_down, lift_up, lift_down;  
DIGITAL_OUTPUT vcr_on, vcr_off, dvd_on, dvd_off;  
DIGITAL_OUTPUT vproj_on, vproj_off;  
DIGITAL_OUTPUT vproj_video1, vproj_video2, vproj_rgb;  
DIGITAL_OUTPUT lights_pre_1, lights_pre_2, lights_pre_3;

PUSH system_on  
{  
CancelWait(sysOffWait); // cancel the system off wait event

Pulse(2000, screen_down); // lower screen for 20 sec.  
Pulse(9500, lift_down); // lower lift for 9.5 sec.

Wait (1000, sysOnWait1) // 10 second delay  
{Pulse(PULSETIME, vcr_on);  
Pulse(PULSETIME, dvd_on);  
Pulse(PULSETIME, lights_pre_1);  
Pulse(PULSETIME, vproj_on);}

Wait (1500, sysOnWait2) // 15 second delay pulse(PULSETIME, vproj_video);} // end of push event 

PUSH system_off  
{  
CancelWait(sysOnWait1);  
CancelWait(sysOnWait2);

Pulse(2000, screen_up);  
Pulse(PULSETIME, vproj_off);  
Pulse(PULSETIME, vcr_off);  
Pulse(PULSETIME, dvd_off);

Wait(500, sysOffWait)  
{Pulse(9500, lift_up);  
Pulse(PULSETIME, lights_pre_3); } } // end of push event

Notice that in this example, the **CancelWait** function was used to cancel any pending waits when the **SYSTEM ON** or **SYSTEM OFF** buttons were pressed. This is analogous to using the reset input on the Delay symbol in SIMPL.

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Working_With_Time/TP_Working-with-Time.htm*
