# FileGetHourNum

Name:

FileGetHourNum

Syntax:

SIGNED_INTEGER FileGetHourNum(FILEINFO Info);

Description:

Returns an integer corresponding to the number of hours in the time of the file.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<../File_Functions/File_First.htm>) for description).

Return Value:

The number of hours from 0 to 23 (24-hour time format).

Example: 

(see [File Functions Overview](<../File_Functions/File_Functions_Overview.htm>))

INTEGER NumHours;

[FILE_INFO](<../File_Functions/File_INFO_Structure.htm>) FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

NumHours = FileGetHourNum(FileInfo);

PRINT ( "Hours of file time = %d\n", NumHours);

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

An example output of this would be "Hours of file time = 22".

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/FILEGETHOURNUM.htm*
