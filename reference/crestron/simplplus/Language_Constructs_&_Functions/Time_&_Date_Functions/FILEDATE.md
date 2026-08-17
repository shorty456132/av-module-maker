# FileDate

Name:

FileDate

Syntax:

STRING FileDate(FILE_INFO Info, INTEGER FORMAT);

Description:

Returns a string corresponding to the current date of the specified file with the specified FORMAT.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<../File_Functions/File_First.htm>) for description)

FORMAT is an integer describing the way to format the date for the return. Valid formats are 1 through 4.

FORMAT 1 returns a string in the form MM/DD/YYYY

FORMAT 2 returns a string in the form DD/MM/YYYY

FORMAT 3 returns a string in the form YYYY/MM/DD

FORMAT 4 returns a string in the form MM/DD/YY

In format 4, the year 2000 is shown as 00. Digits 58 - 99 are treated as 1958-1999 and 00-57 are treated as 2000 through 2057.

Return Value:

A STRING corresponding to the current date.

Example: 

(see [File Functions Overview](<../File_Functions/File_Functions_Overview.htm>))

STRING TheDate$[100];

FILE_INFO FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

TheDate$ = FileDate(FileInfo, 1);

PRINT ( "Date of file = %s\n", TheDate$ );

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

This would print a string such as "Date of file = 03/25/2003".

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/FILEDATE.htm*
