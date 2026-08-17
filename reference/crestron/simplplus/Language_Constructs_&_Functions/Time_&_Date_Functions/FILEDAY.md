# FileDay

Name:

FileDay

Syntax:

STRING FileDay(FILE_INFO Info);

Description:

Returns the day of the week of the file as a STRING.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<../File_Functions/File_First.htm>) for description).

Return Value:

The day of the week of the file is returned in a string. Valid returns are Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday.

Example: 

(see [File Functions Overview](<../File_Functions/File_Functions_Overview.htm>))

STRING TheDay$[100];

FILE_INFO FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

TheDay$ = FileDay(FileInfo);

PRINT ( "Day of file = %s\n", TheDay$ );

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

An example output of this would be "Day of file = Monday".

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/FILEDAY.htm*
