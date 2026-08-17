# Network > Date & Time

> Source: https://help.qsys.com/Content/Reflect/Core_Management/Date_Time.htm

# Network > Date & Time

Click Edit to adjust the Q-SYS Core processor's date, time, and time zone. When finished, click Save.

## Time Settings

* Set the Date by clicking the calendar icon or by manually typing a date in `monthdd, yyyy` format.
* Set the Time by clicking the clock icon or by manually typing the time in `hh:mm:ss` format.
* Set the Time Zone using the drop-down menu.

**Note:** After changing the Time Zone, you must re-deploy the design to the Core for the change to fully take effect, including within scripts (`os.date`), the Date/Time component, and Q-SYS Administrator schedules.

## Time Synchronization

Enable NTP (Network Time Protocol) to synchronize the Q-SYS Core's clock with an NTP server. Enable time synchronization when:

* The Core will be monitored remotely with Q-SYS Reflect.
* You have redundant Cores. Enable time synchronization on both the Primary Core and Backup Core using the same NTP servers.

Click + Add to add an NTP server to the list. By default, Q-SYS Core Manager uses NTP servers `0.pool.ntp.org` and `1.pool.ntp.org`.

**Note:** After enabling NTP synchronization, it takes a few seconds for the change to take effect. Refresh the page to see the NTP-synchronized time.
