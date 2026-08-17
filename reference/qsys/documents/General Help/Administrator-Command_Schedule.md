# Command Schedule (Administrator)

> Source: https://help.qsys.com/Content/Administrator/Command_Schedule.htm

# Command Schedule (Administrator)

The Command Schedule tab provides the capability to schedule any of the Commands with the exception of a Page type Command. The Command Schedule provides options for when a Command starts, the recurring frequency, looping, and more. Each scheduled Command is known as an Event.

**Note:** Use Q-SYS Core Manager to set the time and date on the Q-SYS Core processor.

[Changing the View](javascript:void(0))

To change views, click the Command Scheduler tab. In the upper right corner of the scheduler, click one of the following views:

* **E** (Event view) Shows all scheduled events for a day. You can change the day by clicking the drop-down calendar and selecting a day, or use the right (forward) or left (backwards) arrows.
* **1** (one day) Shows the events scheduled for today. You can change the day by clicking the drop-down calendar and selecting a day, or use the right (forward) or left (backwards) arrows.
* **7** (seven days) The 7 day view displays columns Sunday through Saturday, and rows from 00:00 (AM) through 24:30 (PM) in half-hour increments. The left / right arrows move forward or backwards one week at a time.
* **31** (31 days) The 31, or month, view displays columns Sunday through Saturday from the first day of the month, until the last. The left / right arrows move forward or backwards one month at a time.

List and Calendar - List displays a list of events, Calendar displays the information in a calendar type format.

**Note:** When you make any changes in the Administrator, you must Update the Administrator for the changes to take effect. After making a change in a dialog box in the Administrator, and exiting the dialog box, a red banner displays across the top of the interface with an Update button, and a Cancel button.

[Creating an Event](javascript:void(0))

1. In the **Run** or **Emulate** mode, select the **Administrator** > **Command Schedule** tab.
2. The tab opens displaying the current month's calendar. You can click the left and right arrows at the top of the calendar to change the month.
3. Double-click one of the days in the calendar. The **Edit Event** dialog box opens with the **Occurs** date set to the date you clicked. The time is the current time. Both of these parameters can be changed.
4. Give a **Name** to the Event.
5. Select a **Command** from the drop-down menu. (If you don't have at least one Command created, the only choice is the AdHoc Command. You must select a Command to Schedule an Event.) For an AdHoc Command, you are prompted to create a Command as part of the Event. Steps a. and b. below are for creating an AdHoc Command.
   1. Command Type - The [Commands](Commands.htm) you have created in your design are shown in the drop-down list. Select the type.
   2. Based on the Command type, you have different parameters to select. Refer to the Commands topic for details on the types of Commands, and how to create them.
6. The **Enabled** drop-down is, by default, set to **Yes**. This selection gives you the option to enable or disable an event at any time.
7. Select one of the following from the **Occurs** drop-down menu.

   **Note:** If you create an Event and schedule it to repeat periodically, do not set the Audio Player to Loop. Use the tools in the Command Schedule to loop the message. If you use the Loop on the Audio Player, when the Event stops, the Audio Player continues to play.

   * **Once** creates a one-time event.
     + Specify a date and time for this Event to occur.
   * **Daily** creates an Event that occurs every day at the same time.
     + Specify a time for this Event to occur.
   * **Weekly** creates an Event that occurs on the selected days every week, at the same time.
     + Specify a time for this Event to occur.
     + Click the check box corresponding to the days of the week you want the Event to take place.
   * **Monthly** creates an Event that occurs on the same day of the month, every month, at the same time.
     + Specify a time, for this Event to occur.
     + Select the day of the month for the Event to occur. If you schedule an event on the 29th, 30th, or 31st, it will occur only in the months in which those days exist.
8. **Loop** allows you to execute the Event repeatedly, at set intervals, until a specified time. The Loop is in effect every time the Event occurs. Select **Yes** from the drop-down if you want to loop the Event.
   * "**Until**" Specify a time when the event will stop looping. If you select a time earlier than the Event start time, the Event continues to loop until the next day at the set time.
   * Specify an interval time between the end of a loop, and the beginning of the next loop.
9. If you selected **Daily**, **Weekly** or **Monthly** from the Occurs drop-down, you can click the check box next to **Show Advanced Settings** to reveal the following options. (If you selected **Once**, the Show Advanced Settings option is not displayed.)
   * Select a **Starting** date. This is the date on which the Event begins. If you select a date earlier than "today" the event starts on the next occurrence based on the selections you made in Occurs and other associated fields.
   * Select an **Ending**.
     + **Never** means the event continues until infinity and perhaps longer.
     + **After** provides the option to have the Event occur a specified number of times.
       - Select the number of times you want the Event to **Occur**.
     + **On** provides the option to select a date that the Event ends.
       - Select the ending date from the drop-down.
   * **Every** provides the option to skip days, weeks, or months depending on your selection in the **Occurs** field.
     + If you enter 1, the Event happens every day, week, or month with out skipping any. If you enter, for example 3, the Event occurs every third month based on the other settings.

[Copying an Event](javascript:void(0))

1. Select the Event you wish to copy.
2. Press Ctrl-C to copy the event.
3. Navigate to the date to which you want to copy the event.
4. Press Ctrl-V to paste the event.

[Disabling an Event](javascript:void(0))

Double-click the Event you wish to Disable. In the Edit Event dialog box, select No using the Enabled drop-down. Click the OK button. The dialog box closes, and all occurrences of the Event are grayed out, and disabled.

To re-enable, repeat the Disable process except select Yes in the Enabled field.

[Deleting an Event](javascript:void(0))

Select the Event you want to delete, and press the Delete key. If the event is recurring, all the occurrences of the Event are deleted, regardless of which occurrence of the Event you select.
