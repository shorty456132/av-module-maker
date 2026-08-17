# Rstack overflow

The Rstack that this message refers to is the Return Stack. When an event is interrupted by some means (via a process_logic statement or an implied task switch from inside a loop), information about that event is put on the Return stack, so that when the event resumes, it knows how to continue. When the event continues, the saved information is removed from the return stack.

If during this interruption the event is called again, and interrupted again, more information is saved on the return stack. The return stack is of limited size and if this keeps occurring, the Return stack will not have enough space to contain more data and this message will be issued.

For a further discussion of how to handle the programming when events are likely to be interrupted, refer to "[Task Switching](<../../Task_Switching/Task_Switching_for_2-Series_Control_Systems.htm>)".

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Common_Runtime_Errors/Rstack_overflow.htm*
