# FileGetMinutesNum

Name:

2-series only

Syntax:

SIGNED_INTEGER FileGetMinutesNum(FILEINFO Info);

Description:

Returns an integer corresponding to the number of minutes in the file time.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<../File_Functions/File_First.htm>) for description).

Return Value:

The number of minutes from 0 to 59.

Example: 

(see [File Functions Overview](<../File_Functions/File_Functions_Overview.htm>))

INTEGER NumMinutes;

[FILE_INFO](<../File_Functions/File_INFO_Structure.htm>) FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

NumMinutes = FileGetMinutesNum(FileInfo);

PRINT ( "Minutes of file time = %d\n", NumMinutes);

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

An example output of this would be "Minutes of file time = 33".

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/FILEGETMINUTESNUM.htm*
