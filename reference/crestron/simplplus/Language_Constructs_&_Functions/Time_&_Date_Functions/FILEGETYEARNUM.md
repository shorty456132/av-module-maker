# FileGetYearNum

Name:

FileGetYearNum

Syntax:

SIGNED_INTEGER FileGetYearNum(FILEINFO Info);

Description:

Returns an integer corresponding to the year of the file.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<../File_Functions/File_First.htm>) for description).

Return Value:

The year as an integer. The full year is specified. For example, the year 2003 will return the integer 2003.

Example: 

(see [File Functions Overview](<../File_Functions/File_Functions_Overview.htm>))

INTEGER NumYear;

[FILE_INFO](<../File_Functions/File_INFO_Structure.htm>) FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

NumYear = FileGetYearNum(FileInfo);

PRINT ( "Year of file date = %d\n", NumYear);

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

An example output from this would be "Year of file date = 1999".

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Time_%26_Date_Functions/FILEGETYEARNUM.htm*
