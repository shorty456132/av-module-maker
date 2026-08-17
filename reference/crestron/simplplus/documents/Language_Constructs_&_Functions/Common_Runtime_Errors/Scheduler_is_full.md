# Scheduler is full

Any time-based function such as DELAY, PULSE, or WAIT will schedule an event in SIMPL+. A scheduled event will add one or more entries to the SIMPL+ scheduler. The scheduler currently supports 200 events and is global to the entire SIMPL+ system. If the scheduler is full and another event is added, this message is issued.

NOTE: The message "Skedder Full" is issued from a SIMPL program, not SIMPL+. "Skedder full" is a similar problem, but results if too many time-based events are occurring in a SIMPL program.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Common_Runtime_Errors/Scheduler_is_full.htm*
