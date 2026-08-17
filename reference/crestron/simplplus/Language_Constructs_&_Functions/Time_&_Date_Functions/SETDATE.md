# SETDATE

Name:

SetDate

Syntax:

SetDate(INTEGER MONTH, INTEGER DAY, INTEGER YEAR);

Description:

Sets the system date.

Parameters:

MONTH is an integer containing the month to which the date is set. A valid range is 1 through 12, corresponding to January through December.

DAY is an integer containing the day of the month to which the date is set. The range varies from month to month, but always starts at 1.

YEAR is an integer containing the year to which the date is set. The year is four digits, i.e. 1999.

Return Value:

None.

Example:

ANALOG_INPUT Month, Day, Year;

CHANGE Month, Day, Year

{

SetDate(Month, Day, Year);

PRINT("Current Date is: %s\n", Date(1));

}

In this example, Month, Day, and Year come from a SIMPL program. For example, if Month = 12, Day = 25, Year = 1999, the output from this program will be Current Date = 12/25/1999.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/SETDATE.htm*
