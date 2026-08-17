# FileGetMonthNum

Name:

FileGetMonthNum

Syntax:

SIGNED_INTEGER FileGetMonthNum(FILEINFO Info);

Description:

Returns an integer corresponding to the month of the year of file.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<../File_Functions/File_First.htm>) ).

Return Value:

The month of the year as an integer from 1 to 12.

Example: 

(see [File Functions Overview](<../File_Functions/File_Functions_Overview.htm>))

INTEGER NumMonth;

[FILE_INFO](<../File_Functions/File_INFO_Structure.htm>) FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

NumMonth = FileGetMonthNum(FileInfo);

PRINT ( "Month of file date = %d\n", NumMonth);

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

An example output of this would be "Month of file date = 9".

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/FILEGETMONTHNUM.htm*
