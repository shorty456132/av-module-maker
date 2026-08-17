# Clock Driver

The Clock Driver symbol makes the internal clock of the control system available to other symbols. In addition, its presence alone will synchronize the internal clocks on touchpanels with the internal clock of the control system. (The output signal and parameter need not be defined.)

The <dst> parameter specifies the format for Daylight Savings Time, as shown in the following table:

<dst> |  Format  
---|---  
0 |  No DST  
1 |  U.S. (first Sunday in April to the last Sunday in October)  
2 |  Southern Hemisphere (first Sunday in October to the 3rd Sunday in March)  
3 |  Same as 2 (for compatibility with MSX)  
4 (2-Series only) |  European Union Standard (last Sunday in March to the last Sunday in October)  
5 (2-Series only) |  Egypt (last Friday in April to the last Thursday in September)  
  
Entering Daylight Savings Time drives the time back one hour beginning at 2:00 A.M. Leaving Daylight Savings Time moves the time ahead one hour beginning at 2:00 A.M.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/Clock_Driver.htm*
