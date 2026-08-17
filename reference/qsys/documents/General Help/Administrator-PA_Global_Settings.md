# PA Global Settings (Administrator)

> Source: https://help.qsys.com/Content/Administrator/PA_Global_Settings.htm

# PA Global Settings (Administrator)

The Public Address Global Settings contain settings that are used in several other portions of the Public Address system. You must have at least one Page Station, Virtual or proxy, and a PA Router in your design to access these settings.

[Controls](javascript:void(0))

#### Priority Mode

A drop-down list from which you can select:

**Station/User Priority** - Each Page Station is assigned a Priority Level that determines the priority of the Commands issued by that station. In addition, if the Page Station requires Users to logon, and the User has Override Page Station Settings set to Yes, when the User logs on to a Page Station, that User's priority is used instead of the stations's regardless if the User's Priority is higher or lower.

In this mode, each Page Command can optionally be given a Priority Level with Override Source Priority that overrides the priority of the station or User issuing the command. This allows, for example, an emergency level Page Command to be issued from a Page Station that normally issues lower priority page events.

**Command Priority** - Each Page Command is given a Priority Level that determines its priority relative to other Commands.

In this mode, Page Stations and Users can optionally be given override capability that overrides the priority of the Commands they issue. This allows, for example, the priority of a Page Command to be elevated when issued by a User configured with override capability.

Refer to the Q-SYS Command Priority Flow Diagram below.

#### Queue Timeout

If a Play Message or Delayed Page command is held up because the zones are busy for this long, the command will be discarded.

#### Cancel Delay

Wait this long after issuing a Play Message command to allow canceling before the message is queued for playback.

#### Retry Count

The Retry Count applies only to pages with a Priority that has Retry checked. The number of times a page is retried before it is canceled. Queue Timeout may expire before the page reaches this number.

#### Enable Archive Export

Checking the Enable Archive Export enables you to select an FTP server and a Remote Directory on that server to which you can export the archived pages. (You must enable Archiving for each priority level you wish to archive.) After checking the Enable Archive Export checkbox, you must enter the following information:

**FTP Server**
- The entry must be in one of the following formats.`ftp://[server-IP-Address]/` or `ftp://[server-resolved-hostname]/`

**Remote Directory**
- Can be any valid directory on the FTP server, and must be in the following format. `[folder name]/[subfolder name]/`

**Username** and **Password** - A valid username/password combination on the FTP server.

Click [here](#Page_Archiving_Export) for complete details.

#### Priority Levels

Priority Levels can be assigned to **Commands**, **Page Stations**, and **Users** to determine priority of concurrent paging events. An event with a higher priority will interrupt an event with a lower priority level if there are any common destination **Zones**.

Priorities are not used to determine if a **Command's** priority, **Page Station's** priority, or **User's** priority is used for a given paging event. The **Priority Mode** and the configuration of **Commands**, **Page Stations** and **Users** determines which these element's priority is used for an event.

You can add Priority Levels by clicking the plus sign above the Priority Level field. When a Priority Level is selected, new Priority Levels are inserted above the selection. When a Priority Level is not selected, new Priority Levels are added to the bottom of the list.

You can rename a Priority Level by double-clicking the name and typing the new name.

You can delete a Priority Level by selecting it, then pressing the **Delete** key.

The order of the list determines the Priority Level. Each Priority Level has a number associated with it, and a lower number (top of list) denotes a higher priority (i.e. "1" is the highest priority). You can rearrange the Priority Levels by either selecting one of the levels then using the up and down arrows at the top of the Priority Level field to move it to the desired position, or selecting one of the levels and dragging it to its new position.

#### Retry

Retry does not apply to live pages.

Checkbox indicating whether or not a page (except Live pages), of the associated Priority, gets retried.

#### Archive

Does not apply to Play Message commands.

Checkbox to indicate whether or not pages of the associated Priority level are Archived.

A compressed mp3 file of the page audio is saved in the **PageArchives** folder, accessible from the Q-SYS Core Manager > Audio Files page. In the log, there is a play button, next to the page event, to listen to the archive. If the Page Archive is large enough to be purged before 31 days, the mp3 file of the associated page may be deleted before the Event Log entry. In this case, the link no longer works.

The Page Archives (mp3 recordings of pages) are stored for up to 31 days or until the total size of the stored archives exceeds 100MB. At midnight each day, page archives older than 31 days are deleted. Also, if at any time the total size of stored page archives exceeds 100MB, the oldest archives are purged until the total is below 100MB. This means that in a system with lots of paging activity, there is no guarantee that you will have a full 31 days of history stored.

Refer to the Q-SYS Public Address Router Logic Diagram below.

#### Split

For Pages and Messages, clicking this checkbox means that page or message (command) will not wait for all Page Zones to be available to start; only one zone needs to be available.

If one or more, but not all, zones are interrupted during the "splitable" command, the command for those zones is discontinued, but the command continues on the available zones. If retry is enabled and any of the zones had been interrupted or were not available when the command was issued, those zones will be retried. This will continue until all of the zones have succeeded, the retry count is exhausted, the command is canceled or the queue timeout expires.

Typically, the Split mode would be used for low priority, non-essential, background messages that go to a large number of zones.

Refer to the Q-SYS Public Address Router Logic Diagram below.

[Q-SYS Command Priority Flow Diagram](javascript:void(0))

[Q-SYS Public Address Router Logic Diagram](javascript:void(0))

[Page Archiving Export](javascript:void(0))

Archive Export enables you to select an FTP server, and a directory on that server, to which you can export the archived pages.

To export page files, you must first enable Archiving for each priority level you wish to archive. Archiving saves a compressed mp3 file of the page audio in the PageArchives folder, accessible from the Q-SYS Core Manager > Audio Files page.

Exporting the files does not move them from the Core, but copies them. The files on the Core remain until they meet the purge deadline - 31 days, or when the directory reaches 100 MB. Oldest files get deleted first. This is the same as the Event Log purge scheme.

When you check the Enable Archive Export checkbox, the following fields display in which you must enter the required information:

**FTP Server**
- The entry must be in one of the following formats. `ftp://[server-IP-Address]/` or `ftp://[server-resolved-hostname]/`.

**Remote Directory**
- Can be any valid address on the FTP server, and must be in the following format. `[folder name]/[subfolder name]/`.

**Username** and **Password** - Enter a valid username/password combination on the FTP server.

The mp3 files are copied to the FTP server every 5 minutes, or when the export configuration is changed. If the FTP server can not be reached, an error is logged in the event log. When the valid FTP server connection is restored, the files are then copied to the server.

The filename format is: `page_[year]-[month]-[day]T[hour]_[minute]_[second]_station_[station#].mp3`

For example, `page_2012-04-05T10_10_40_station_2.mp3`

The `station#` is the input number on the PA Router component in the Q-SYS Design file. Additionally, there are tags (metadata) associated with the archived files. This allows files to be organized with file browsers. In Windows Explorer, you can right click the file, select Properties - then select the Details tab.

The available information includes:

**Title**
- The page type (live/auto/delayed), from which status, and completion status (timeout/complete/error)

**Comments**
- All available information about the page - Title info plus priority, zones, and filename. For example, "Page live from station 3 timeout archived to page\_2025-12-16T16\_23\_59\_station\_3.mp3 -- Page 'Live' at priority 'Important' to zones 1,2,3,4"

**Album Artist**
- Station that initiated page

**Album**
- Q-SYS Design name
