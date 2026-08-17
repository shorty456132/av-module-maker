# Understanding Processing Order

## How SIMPL+ and SIMPL Interact

Advanced SIMPL programmers should be familiar with how logic is processed in SIMPL programs. This guide does not attempt to explain this concept here, but it does detail how SIMPL+ programs fit into the picture. However, a couple of definitions may be helpful.

**Logic Wave** ‑ The act of propagating signals from the input to the output of a logic symbol. In a typical program, a single logic wave may include the processing of many symbols.

**Logic Solution** ‑ An arbitrary number of logic waves, processed until the state of all signals in the program have settled to a stable (i.e. unchanging) state.

In general, when a SIMPL+ event function is triggered, it is processed to conclusion in a single logic wave. That is, if this event caused a change to one of the output signals, that signal would be valid one logic wave after the event was triggered. In this simple case, a SIMPL+ program acts identically to a SIMPL logic symbol from a timing standpoint. In addition, for multiple SIMPL+ events triggered on the same logic wave (whether or not they are in the same module), these events multi-task (run at the same time) and complete before the next wave.

As SIMPL+ programs become more complex and processor intensive however, this general rule may no longer apply. Instead, the operating system may determine that too much time has elapsed and temporarily suspend the SIMPL+ program while it continues to process the SIMPL logic (which may also include other SIMPL+ programs). For example, if an event function must run through a loop 2000 times before completing, the processor may decide to perform a task switch and process other logic before completing the loop.

This task‑switching ability has the benefit of not freezing up the rest of the program while a particularly intensive calculation is proceeding. After the completion of the current logic solution, the SIMPL+ program that was exited continues from where it left off.

## Forcing a Task Switch

There may be times in programming when it is necessary to force a task switch to occur. For example, when a digital_output is set high, it normally is not propagated to the SIMPL program until the SIMPL+ completes. To guarantee that the digital signal is asserted, force the system to switch from the SIMPL+ module back into the SIMPL program.

There are two ways to force a task switch: with the **ProcessLogic** function or the **Delay** function. To provide an immediate task switch out of the current SIMPL+ module, use **ProcessLogic**. When the logic processor enters this module on the next logic solution, execution begins with the line immediately following. An immediate task switch also results from **Delay** , but the SIMPL+ module does not continue executing until the time specified has elapsed. The **Delay** function is discussed in greater detail in [Working with Time](<../Working_With_Time/TP_Working-with-Time.htm>).

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Understanding_Processing_Order/TP_Understanding-Processing-Order.htm*
