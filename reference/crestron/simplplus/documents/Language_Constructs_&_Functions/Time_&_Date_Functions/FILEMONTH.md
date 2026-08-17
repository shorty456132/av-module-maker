# FileMonth

Name:

FileMonth

Syntax:

STRING FileMonth(FILEINFO Info);

Description:

Returns the month of the file date as a string.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<../File_Functions/File_First.htm>) for description).

Return Value:

The current month is returned in a string. Valid returns are January, February, March, April, May, June, July, August, September, October, November, or December.

Example: 

(see [File Functions Overview](<../File_Functions/File_Functions_Overview.htm>))

STRING TheMonth$[100];

[FILE_INFO](<../File_Functions/File_INFO_Structure.htm>) FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

TheMonth$ = FileMONTH(FileInfo);

PRINT ( "Month of file date = %s\n", TheMonth$);

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

An example output of this would be "Month of file date = September".

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/FILEMONTH.htm*
