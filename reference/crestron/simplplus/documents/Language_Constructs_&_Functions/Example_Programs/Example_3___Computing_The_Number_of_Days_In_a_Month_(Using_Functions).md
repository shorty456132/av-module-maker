# Example 3: Computing the Number of Days in a Month (Using Functions)

#SYMBOL_NAME "Compute Number of Days in a Month"

#ANALOG_INPUT MONTH;

#ANALOG_OUTPUT DAYS;

INTEGER_FUNCTION ComputeDaysInMonth(INTEGER Month)

{

// Note that this computation does NOT take into account leap

// year!

INTEGER Days;

SWITCH (Month)

{

CASE( 2): Days = 28; // February

CASE( 4): Days = 30; // April

CASE( 6): Days = 30; // June

CASE( 9): Days = 30; // September

CASE(11): Days = 30; // November

Default: Days = 31; // All others

}

Return(Days);

}

CHANGE MONTH

{

DAYS = ComputeDaysInMonth(MONTH);

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Example_Programs/Example_3___Computing_The_Number_of_Days_In_a_Month_%28Using_Functions%29.htm*
