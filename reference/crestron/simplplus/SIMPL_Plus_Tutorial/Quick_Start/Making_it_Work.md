# Making it Work

This section describes how to make the simple SIMPL+ program written in the last section work inside a Crestron control processor. As was mentioned earlier, SIMPL+ programs cannot run all by themselves. They must be enclosed inside a SIMPL wrapper. This section discusses how to set up this program in SIMPL.

Create a new SIMPL program and fill in the boxes in the **Program Header Information** window. Make sure to select the relevant information from the **Program ID Tag** and **Control Processor** dropboxes. Notice that only CNX‑series or newer control processors are compatible with SIMPL+. For this example, use the SIMPL Debugger to trigger the digital input. As a result, there is no need to define a touch screen or other user-interface device, although it is even better if one is available for testing.

After the system is configured, switch to the Program Manager by selecting **Project** > **Program System** and make sure that the **Symbol Library** pane is visible on the left-hand side of the screen. Find the **User Modules** folder and open it. An icon representing the SIMPL+ program written in the previous section appears. Drag this icon into the **Logic** folder in the **Program View** pane. The SIMPL+ program now becomes just another symbol in the program.

Double‑click on the logic symbol to bring it into the **Detail View** window. It should have a single input, labeled **speak**. This corresponds directly to the declarations section of our SIMPL+ code, where only a single input and no outputs were defined. Define a signal for this input. The signal name here is not important, but for this example, call it **test_me**. Also note that if a user interface was defined in an earlier step, assign this same signal to a button press.

That’s it! The first program is complete. All that is left is to compile the whole thing, transfer it to the control processor, and test it. As in SIMPL, compile the program by clicking on the compile toolbar button or selecting **Project** > **Convert/Compile**. The compile process automatically recognizes that there is a SIMPL+ module in the program and compiles it along with the SIMPL code (even though it was already compiled when it was saved; SIMPL always recompiles because it must link the modules together with the SIMPL program).

After compilation, transfer the program when prompted by SIMPL. Click **Yes** and the SIMPL code section is sent first (followed by the save permanent memory image). Once completed, the SIMPL+ program code is sent along with the SIMPL code base.

At this point a program has been loaded into the control system and is ready to be tested. Start SIMPL Debugger by opening Crestron Toolbox™ and selecting **Tools** > **SIMPL Debugger**. Select the processor with the program that is running from the address bar in the bottom left corner of the Debugger window. Select **Yes** in the **Synchronize Signal** window. 

The program is ready to be tested. Drive the signal to the high state by selecting it from the left-most pane and clicking the **Rising Edge** button from the **Stimulus** window above the signal tree. Driving the signal to the high state triggers the push event. In the right-hand pane, known as the **Trace Window** , the events that occur as a result of the button press display. The string **Hello world!** appears under the **Value** tab.

Click on the **Falling Edge** button to drive the signal low and trigger the release event. In the **Trace** window, the string **Crestron people make the difference** appears.

By clicking on the **Positive Pulse** button, both strings appear one after the other, since the push and release events are triggered in rapid succession.

NOTE: There are multiple ways to manually trigger the above events. Using the **Momentary Press** button in the **Stimulus** window, for instance, will trigger multiple events that display in the **Trace Window**. The various strings discussed above will all appear under the **Value** tab in as separate events. 

Finally, what happened to the startup text “`I am born!`?” Remember that `Function Main` only runs on system startup and this occurred even before Debugger was started. Thus it was missed. To see it now, reboot the control processor by selecting **Options** > **Reset Rack**.

In addition to the latest revision of the SIMPL+ Language Reference Guide, continue reading through this manual to learn more about how to program in SIMPL+.

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Quick_Start/Making_it_Work.htm*
