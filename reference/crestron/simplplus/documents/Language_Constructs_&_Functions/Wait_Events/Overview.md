# Wait Events Overview

When writing a SIMPL+ program, it is often desirable to have an event that will be processed a predetermined amount of time after it is triggered. The WAIT event allows a block of code to be executed after a specified amount of time. There are related functions which allow WAITS to be paused, resumed, cancelled, or have their times changed. The system supports up to 200 total timed events that may be running at any given time across all SIMPL+ modules.

Timed events include: WAIT, DELAY, and PAUSE statements.

A WAIT statement differs from a DELAY in both timing and order of statement execution. In a WAIT statement, the WAIT block executes only after the specified amount of time, but execution proceeds immediately to the statement following the WAIT block. In a DELAY, all execution is halted until the delay is finished.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Wait_Events/Overview.htm*
