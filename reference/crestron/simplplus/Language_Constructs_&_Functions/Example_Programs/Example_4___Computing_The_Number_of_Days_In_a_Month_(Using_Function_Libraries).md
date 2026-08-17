# Example 4: Computing the Number of Days in a Month (Using Function Libraries)  
  
The following code would be saved as, in this example, "My Function Library.USL".

INTEGER_FUNCTION ComputeDaysInMonth(INTEGER CurrentMonth)

{

// Note that this computation does NOT take into account leap

// year!

INTEGER NumDays;

SWITCH(CurrentMonth)

{

CASE( 2): NumDays = 28; // February

CASE( 4): NumDays = 30; // April

CASE( 6): NumDays = 30; // June

CASE( 9): NumDays = 30; // September

CASE(11): NumDays = 30; // November

Default: NumDays = 31; // All others

}

Return(NumDays);

}

The following code can be saved as any filename:

#SYMBOL_NAME "Compute Number of Days in a Month"

#USER_LIBRARY "My Function Library"

ANALOG_INPUT CURRENTMONTH;

ANALOG_OUTPUT NUMDAYS;

CHANGE CURRENTMONTH

{

NUMDAYS = ComputeDaysInMonth(CURRENTMONTH);

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Example_Programs/Example_4___Computing_The_Number_of_Days_In_a_Month_%28Using_Function_Libraries%29.htm*
