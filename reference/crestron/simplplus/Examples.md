# Examples

This topic is provided to show cases of what is valid & invalid when declaring parameter properties. Legal values for bounds/list elements/default values/etc. for parameter properties can be found in [Allowable Ranges for 2 Series Numeric Formats](<Allowable_Ranges_for_2_Series_Numeric_Formats.htm>),

Example 1:

INTEGER_PARAMETER val;

By itself, an integer parameter is unsigned and may hold a value of 0d to 65535d in SIMPL. If the programmer tries to enter a value of (for example) 70000d, SIMPL will reject it.

Example 2:

INTEGER_PARAMETER val;

#BEGIN_PARAMETER_PROPERTIES val

propValidUnits=unitDecimal|unitHex;

propDefaultUnit=unitPercent;

#END_PARAMETER_PROPERTIES

This is incorrect because the propDefaultUnit is not contained in propValidUnits.

Example 3:

INTEGER_PARAMETER val;

#BEGIN_PARAMETER_PROPERTIES val

propValidUnits=unitDecimal|unitHex;

propDefaultUnit=unitDecimal;

propDefaultValue=25%;

#END_PARAMETER_PROPERTIES

This is incorrect because the propDefaultValue is not contained in the propValidUnits.

Example 4:

INTEGER_PARAMETER val;

LONG_INTEGER_PARAMETER val2;

#BEGIN_PARAMETER_PROPERTIES val, val2

propValidUnits=unitDecimal|unitHex;

propDefaultUnit=unitDecimal;

propDefaultValue=70000d

#END_PARAMETER_PROPERTIES

Example 5:

This is incorrect because 70000d is not a legal value for an INTEGER_PARAMETER. However, it is legal for the LONG_INTEGER_PARAMETER.

INTEGER_PARAMETER val;

#BEGIN_PARAMETER_PROPERTIES val

propValidUnits=unitDecimal|unitHex;

propDefaultUnit=unitDecimal;

propList={5d, "Value1"},{6d, "Value2"};

#END_PARAMETER_PROPERTIES

This is a valid, legal case. SIMPL will only let the programmer pick "Value1 [5d]" or "Value2 [6d]" from the dropdown.

Example 6:

INTEGER_PARAMETER val;

#BEGIN_PARAMETER_PROPERTIES val

propValidUnits=unitDecimal|unitHex;

propDefaultUnit=unitDecimal;

propBounds=0x25,0x30;

#END_PARAMETER_PROPERTIES

This is legal since the propBounds specifies a legal unit based on the propValidUnits list and the upper & lower bounds are legal for an INTEGER_PARAMETER. This example will restrict the the programmer using the module to typing in any value between 25h and 30h, whether they specify it in decimal or hex. The default notation is decimal if they do not type in a unit.

Example 7:

INTEGER_PARAMETER val;

#BEGIN_PARAMETER_PROPERTIES val

propDefaultUnit=unitTime;

propDefaultValue=8d;

#END_PARAMETER_PROPERTIES

Although this does not list a propValidUnits, it is still legal because ALL units are considered valid when no propValidUnits is entered. The default value when the symbol is dropped into SIMPL is 8d, however, when any value is entered without explicit units, the units are assumed to be "s". (i.e. entering 5 and hitting ENTER will change to 5s). This example may not be very practical, but it is legal.

---
*Source: https://help.crestron.com/simpl_plus/Content/Examples.htm*
