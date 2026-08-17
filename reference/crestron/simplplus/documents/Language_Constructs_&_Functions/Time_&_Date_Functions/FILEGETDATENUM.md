# FileGetDateNum

Name:

FileGetDateNum

Syntax:

SIGNED_INTEGER FileGetDateNum(FILEINFO Info);

Description:

Returns an integer corresponding to the day of the month of the file.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<../File_Functions/File_First.htm>) for description).

Return Value:

The day of the month as an integer from 1 to 31.

Example: 

(see [File Functions Overview](<../File_Functions/File_Functions_Overview.htm>))

INTEGER NumDateOfMonth;

[FILE_INFO](<../File_Functions/File_INFO_Structure.htm>) FileInfo;

INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

NumDateOfMonth = FileGetDateNum(FileInfo);

PRINT ( "Day of the month of file = %d\n", NumDateOfMonth);

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

An example output of this would be "Day of the month of file = 25".

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/FILEGETDATENUM.htm*
