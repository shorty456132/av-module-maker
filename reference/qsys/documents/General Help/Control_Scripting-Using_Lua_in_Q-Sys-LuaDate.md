# LuaDate

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/LuaDate.htm

# LuaDate

LuaDate is a Lua module for date and time calculation and retrieval using the Gregorian Date system. LuaDate allows you to take advantage of the following features:

* Date and Time string Parsing.
* Time addition and subtraction.
* Time span calculation.
* Local time support.
* Formats Date and Time like strftime.

[Usage](javascript:void(0))

To use LuaDate, add the following line to your script:

`local date = require"date"`

[Example](javascript:void(0))

#### Examine Specific Date During Specific Time Frame

```lua
local date = require "date"  
-- prints all FRIDAY the 13TH dates between year 2000 and 2010  
for i = 2000, 2010 do  
        -- year jan 1  
        x = date(i, 1, 1)  
        -- from january to december  
        for j = 1, 12 do  
                -- set date to 13, check if friday  
                if x:setmonth(j, 13):getweekday() == 6 then  
                        print(x:fmt("%A, %B %d %Y"))  
                end  
        end  
end
```

#### Debug Output

```lua
Friday, October 13 2000
Friday, October 13 2000
Friday, April 13 2001
Friday, July 13 2001
Friday, September 13 2002
Friday, December 13 2002
Friday, June 13 2003
Friday, February 13 2004
Friday, August 13 2004
Friday, May 13 2005
Friday, January 13 2006
Friday, October 13 2006
Friday, April 13 2007
Friday, July 13 2007
Friday, June 13 2008
Friday, February 13 2009
Friday, March 13 2009
Friday, November 13 2009
Friday, August 13 2010
Friday, October 13 2000
```

[Limitations](javascript:void(0))

* This module does not recognize leap seconds.
* It assumes that a day as exactly 24\*60\*60 seconds.
* The Lua number must be a double C data type.
* This module supports dates that are greater than `Mon Jan 01 1000000 BCE 00:00:00` and less than `Mon Jan 01 1000001 00:00:00`.

[Local Time Support](javascript:void(0))

This module supports local time. Local Time is:

`Local=UTC + bias`

The *bias* is time zone offset plus the daylight savings if in effect. The *bias* is retrieve using the Lua function `os.date` and `os.time`. It assumes that the Lua function `os.time` returns the number of seconds since the start time (called "epoch").

If the time value is outside the allowable range of times, usually `Jan 01 1970 00:00:00` to `Jan 19 2038 03:14:07` the *bias* will be retrieved using the equivalent year inside the allowable range.

**Note:** Two years are considered equivalent if they have the same leap year and starting weekday.

The function that needs local time support are `date(true)` to get the current UTC time; `date(false)` to get the current local time; `date(num_time)`, `dateObj:getbias()`, `dateObject:fmt(str)` when str has a '`%Z`' or '`%z`'.

[Parsable Date Value](javascript:void(0))

Parsable date value is a lua value that can be converted to a *dateObject*. This value must be `num_time`, or `tbl_date`, or `str_date or bool_now` argument described in the date [LuaDate](#date.:_c) method.

[Parsable Month Value](javascript:void(0))

If a function needs a month value it must be a string or a number. If the value is a `string`, it must be the name of the month full or abbreviated. If the value is a `number`, that number must be 1-12 (January-December).

| Index | Abbreviation | Full Name |
| --- | --- | --- |
| 1 | Jan | January |
| 2 | Feb | February |
| 3 | Mar | March |
| 4 | Apr | April |
| 5 | May | May |
| 6 | Jun | June |
| 7 | Jul | July |
| 8 | Aug | August |
| 9 | Sep | September |
| 10 | Oct | October |
| 11 | Nov | November |
| 12 | Dec | December |

If the value does not represent month, that is equivalent to passing a nil value.

[dateObject](javascript:void(0))

`dateObject` is a table containing date and time value. It has a metatable for manipulation and retrieval of dates and times. Use the `__call` method of date to construct a `dateObject`.

### How Date and Time are Stored in `dateObject`

Time is stored in `dateObject` as Ticks or Day Fraction. Date is stored in `dateObject` as Day Number. Ticks is time unit per seconds. For example, if the tick unit is 1000000. 0.25 seconds is equivalent to 250000 ticks (0.25\*1000000). Day number, is the number days since the epoch, which is January 1, 0001 AD. Example.

`dobj = date("15:49:59.3669")`

If the tick unit is 1000000, dobj store this time as 56999366900 ticks and 0 days.

`((((15*60)+49)*60)+59.3669)*1000000 == 56999366900`

[Example Date and Time](javascript:void(0))

`dobj = date("Jan-5-0001 10:30:15")`

If the tick unit is 1000000, `dobj` stores this date and time as 37815000000 ticks and 4 days.

| Day # | Date |
| --- | --- |
| 0 | Jan 1 0001 |
| 1 | Jan 2 0001 |
| 2 | Jan 3 0001 |
| 3 | Jan 4 0001 |
| 4 | Jan 5 0001 |
| 5 | Jan 6 0001 |
| ... | ... |

**Tip:** The default tick unit is 1000000 (micro-second-ticks).

[Method(s) of dateObject](javascript:void(0))

The dateObject module provides many different functions. `dateObject:` `adddays`, `addhours`, `addminutes`, `addmonths`, `addseconds`, `addticks`, `addyears`, `copy`, `fmt`, `getbias`, `getclockhour`, `getdate`, `getday`, `getfracsec`, `gethours`, `getisoweekday`, `getisoweeknumber`, `getisoyear`, `getminutes`, `getmonth`, `getseconds`, `getticks`, `gettime`, `getweekday`, `getweeknumber`, `getyear`, `getyearday`, `setday`, `sethours`, `setisoweekday`, `setisoweeknumber`, `setisoyear`, `setminutes`, `setmonth`, `setseconds`, `setticks`, `setyear`, `spandays`, `spanhours`, `spanminutes`, `spanseconds`, `spanticks`, `tolocal`, `toutc`.

**Tip:** To learn more about dateObject, see [dateObject Methods](http://tieske.github.io/date/#dateObject).

[Date](javascript:void(0))

The date module provides three different functions. `.diff`, `.epoch`, and `.isleapyear`. Additionally, there is a metamethod of date, which is the [LuaDate](#date.:_c) function.

[date.diff()](javascript:void(0))

Subtracts the date and time value of two dateObject and returns the resulting dateObject.

### Syntax

`date.diff(var_date1, var_date2)`

### Arguments

*var\_date1*: Requires a dateObject or

*var\_date2*: Requires a parsable date value

### Returns

The resulting dateObject if successful.

Returns nil in case of error.

### Example

```lua
-- get the days between two dates  
d = date.diff("Jan 7 1563", date(1563, 1, 2))  
assert(d:spandays()==5)
```

[date.epoch()](javascript:void(0))

Returns dateObject whose date and time value is the Operating System epoch.

### Syntax

`date.ephoch()`

### Arguments

*var\_date1*: Requires a dateObject.

*var\_date2*: Requires a parsable date value.

### Returns

The resulting dateObject if successful.

Returns nil in case of error.

### Example

`assert(date.epoch()==("Jan 1 1920"))`

[date.isleapyear()](javascript:void(0))

Checks if a number or dateObject is a leapyear.

### Syntax

`date.isleapyear(var_year)`

### Arguments

*var\_year*: A number, dateObject, or parsable date value.

### Returns

Returns `true` if `var_year` is a leap year.

Returns `false` if `var_year` is not leap year.

### Example

```lua
d = date(1776, 1, 1)  
asert(date.isleapyear(d))  
assert(date.isleapyear(d:getyear()))  
assert(date.isleapyear(1776))
```

[date:\_call()](javascript:void(0))

Constructs a dateObject. This is a metamethod of date. Remember, `date:_call()` is the same as `date()`.

### Syntax

`date.(num_time)`

`date.(tbl_date)`

`date.(str_date)`

`date.(bool_now)`

`date.(int_year, var_month, int_day, [num_hour], [num_min], [num_sec], [int_ticks])`.

### Arguments

*num\_time*: Required `number` value. Represents the number of seconds in Universal Coordinated Time between the specified value and the System epoch.

*tbl\_date*: Required `table` value. Time (`hour,`,`min`, `sec`, or `msec`) must be supplied if date (`year`,  `month`, and `day`) is not given, vice versa. The constructor will look for the value of this key:

* `year`- an integer, the full year, for example, 1969. Required if month and day is given.
* `month` - a parsable month value. Required if year and day is given.
* `day` - an integer, the day of month from 1 to 31. Required if year and month is given.
* `hour` - a number, hours value, from 0 to 23, indicating the number of hours since midnight. (default = 0).
* `min` - a number, minutes value, from 0 to 59. (default = 0).
* `sec` - a number, seconds value, from 0 to 59. (default = 0).

*str\_date*: Required `string` value. It must have number / words representing date and / or time. Use commas and spaces as delimiters. Strings enclosed by parenthesis is treated as a comment and is ignored. The stated day of the week is ignored whether its correct or not. A string containing an invalid date is an error. For example, a string containing two years or two months is an error. Time must be supplied if date is not given, vice versa.

* **Time Format**: Hours, minutes, and seconds are separated by colons, although all need not be specified. "10:", "10:11", and "10:11:12" are all valid. If the 24-hour clock is used, it is an error to specify "PM" for times later than 12 noon. For example, "23:15 PM" is an error.

* **Time Zone Format**: First character is a sign "+" (east of UTC) or "-" (west of UTC). Hours and minutes offset are separated by colons.

* **Example**: `assert( date("Jul 27 2006 03:56:28 +2:00") == date(2006,07,27,1,56,28))`

* Another format is [sign][number] If [number] is less than 24, it is the offset in hours e.g. "-10" = -10 hours. Otherwise it is the offset in hundred hours e.g. "+75" = "+115" = +1.25 hours.

* **Examples**: `assert(date("Jul 27 2006 -75 ") == date(2006,07,27,1,15,0))`, Or `assert(date("Jul 27 2006 -115") == date(2006,07,27,1,15,0))`.

*bool\_now*: Required `boolean` value. if `bool_now` is false it returns the current local date and time. If `bool_now` is true it returns the current UTC date and time.

*int\_year*: Required `integer` value. The year value.

*var\_month*: Required. A parsable month value.

*int\_day*: Required `integer` value. The day of month.

*num\_hour*: Optional `number` value. Equal to the hours value. The default value is 0.

*num\_min*: Optional `number` value. Equal to the minutes value. The default value is 0.

*num\_sec*: Optional `number` value. Equal to the seconds value. The default value is 0.

*int\_ticks*: Optional `integer` value. Equal to the ticks value. The default value is 0.

### Returns

The resulting dateObject if successful.

Returns nil in case of error.

### Example

```lua
a = date(2006, 8, 13)   assert(a == date("Sun Aug 13 2006"))  
b = date("Jun 13 1999") assert(b == date(1999, 6, 13))  
c = date(1234483200)    assert(c == date("Feb 13 2009"))  
d = date({year=2009, month=11, day=13, min=6})  
        assert(d == date("Nov 13 2009 00:06:00"))  
e = date() assert(e)
```

Portions of this topic are reprinted under permission of the [LuaDate](../../Legal.htm#LuaDate) license.
