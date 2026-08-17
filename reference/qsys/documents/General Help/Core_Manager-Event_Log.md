# Event Log

> Source: https://help.qsys.com/Content/Core_Manager/Event_Log.htm

# Event Log

The Event Log page provides a listing of events that take place on the Q-SYS Core. The Event Log is stored on the Q-SYS Core, abstracted from the running design file and previous design files. All events visible in Core Manager are synchronized to the Q-SYS Reflect Event Log with the exception of events created by the Event Logger component and generic scripting components.

**Note:** The Q-SYS Core retains a maximum of 5,000 logged events (or 30 days worth of events) that can be viewed locally via Core Manager, with the oldest events removed to make room for new events.

## Viewing Events

Events are listed by order of newest first. Use the Show events per page drop-down menu to restrict the number of events shown.

**Tip:** To change the order in which columns appear, click and drag a column name within the Columns menu.

All logged events are assigned a severity level:

|  |  |
| --- | --- |
| Normal | The event is an expected occurrence, indicating healthy operation. |
| Warning | The event indicates compromised operation of the affected source and reduced functionality, such as a network redundancy (LAN B) communication problem. |
| Error | The event indicates a more serious issue with the affected source, such as a connection failure, clock sync fault, or missing device. |

[Filtering Events](javascript:void(0))

You can filter events by:

* Severity: Normal, Warning, or Error.
* Category: For example, Hardware, Telephony.
* Source: The specific device or component generating the event.
* Start date ~ End date: Restrict the list to show only events whose Date & Time stamp is within a target range.
* Search Messages: Restrict the list to show only events with a Message containing a specified text string.

**Tip:** When selecting filter parameters, the quantity for each parameter is indicated. This can help you quickly determine, for example, the number of Errors in the log, the number of events associated with a particular device, and so on.

[Changing the Time Zone of Events](javascript:void(0))

By default, events are shown using your browser's time zone (UTC offset). To show events using the time zone of the Core, select 'Core' from the Time Zone drop-down menu.

## Clearing Events

To clear the event log for this Core, click Clear Events. This permanently deletes all Event Log data from Core Manager. Only Administrators can clear Event Log data.

**CAUTION:** This action cannot be undone.
