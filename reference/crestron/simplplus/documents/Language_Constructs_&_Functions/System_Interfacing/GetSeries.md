# GetSeries

Name:

GetSeries

Syntax:

GetSeries

Description:

Returns the product series. For example, the 3-series architecture will return 3 and the 2-series architecture will return 2.

Example:

FUNCTION GetMySeries()

{

SWITCH( GetSeries() )

{

CASE (2):

PRINT( “2-Series” );

CASE (3):

PRINT( “3-series” );

}

}

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v <> and above

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/GetSeries.htm*
