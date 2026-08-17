# Time and Date Functions Overview

Time and Date functions in a given SIMPL+ program are used to retrieve information about the current date and time from the system clock. Values can be retrieved as either text strings i.e. "January" or as integer values. Typically, integer values are used if computations need to be performed (i.e. when the date is the 25th, perform a specific action).

Function |  Description  
---|---  
[Date](<DATE.htm>) |  Returns a string corresponding to the current date with the specified FORMAT.  
[Day](<DAY.htm>) |  Returns the day of the week as a STRING.  
[FileDate](<FILEDATE.htm>) |  Returns a string corresponding to the current date of the specified file with the specified FORMAT.  
[FileDay](<FILEDAY.htm>) |  Returns the day of the week of the file as a STRING.  
[FileGetDateNum](<FILEGETDATENUM.htm>) |  Returns an integer corresponding to the day of the month of the file.  
[FileGetDayOfWeekNum](<FILEGETDAYOFWEEKNUM.htm>) |  Returns an integer corresponding to the day of the week of file.  
[FileGetHourNum](<FILEGETHOURNUM.htm>) |  Returns an integer corresponding to the number of hours in the time of the file.  
[FileGetMinutesNum](<FILEGETMINUTESNUM.htm>) |  Returns an integer corresponding to the number of minutes in the file time.  
[FileGetMonthNum](<FILEGETMONTHNUM.htm>) |  Returns an integer corresponding to the month of the year of file.  
[FileGetSecondsNum](<FILEGETSECONDSNUM.htm>) |  Returns an integer corresponding to the number of seconds in the time of the file.  
[FileGetYearNum](<FILEGETYEARNUM.htm>) |  Returns an integer corresponding to the year of the file.  
[FileMonth](<FILEMONTH.htm>) |  Returns a string containing the current system time.  
[FileTime](<FILETIME.htm>) |  Returns a string containing the current system time.  
[GetDateNum](<GETDATENUM.htm>) |  Returns an integer corresponding to the current day of the month.  
[GetDayOfWeekNum](<GETDAYOFWEEKNUM.htm>) |  Returns an integer corresponding to the current day of the week.  
[GetDst](<GETDST.htm>) |  Gets the current DST (Daylight Savings Time) state.  
[GetGmtOffset](<GETGMTOFFSET.htm>) |  Retrieves the GMT Offset that was configured via the consol command GMTOFFSET or through the SetGmtOffset() function.  
[GetHourNum](<GETHOURNUM.htm>) |  Returns an integer corresponding to the number of hours in the current time.  
[GetHSeconds](<GETHSECONDS.htm>) |  Returns an integer corresponding to the number of hundredths of a second based on the system clock.  
[GetMinutesNum](<GETMINUTESNUM.htm>) |  Returns an integer corresponding to the number of minutes in the current time.  
[GetMonthNum](<GETMONTHNUM.htm>) |  Returns an integer corresponding to the current month of the year.  
[GetSecondsNum](<GETSECONDSNUM.htm>) |  Returns an integer corresponding to the number of seconds in the current time.  
[GetTicks](<GETTICKS.htm>) |  Returns an integer corresponding to the number of system ticks.  
[GetYearNum](<GETYEARNUM.htm>) |  Returns an integer corresponding to the current year.  
[Month](<MONTH.htm>) |  Returns the current month as a string.  
[SetClock](<SETCLOCK.htm>) |  Sets the system clock.  
[SetDate](<SETDATE.htm>) |  Sets the system date.  
[SetGmtOffset](<SETGMTOFFSET.htm>) |  Sets the system GMT Offset.  
[Time](<TIME.htm>) |  Returns a string containing the current system time.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/Overview.htm*
