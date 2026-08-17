# FileTime

Name:

FileTime

Syntax:

STRING FileTime(FILEINFO Info);

Description:

Returns a string containing the current system time.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<../File_Functions/File_First.htm>) for description).

Return Value:

The return string contains the time in HH:MM:SS format, in 24-hour time. If a value is not two digits wide, it is padded with leading 0s.

Example: 

(see [File Functions Overview](<../File_Functions/File_Functions_Overview.htm>))

STRING TheTime$[100];

[FILE_INFO](<../File_Functions/File_INFO_Structure.htm>) FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

TheTime$=TIME();

PRINT ( "File time = %s\n", TheTime$);

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

An example output from this would be "File time = 14:25:32".

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/FILETIME.htm*
