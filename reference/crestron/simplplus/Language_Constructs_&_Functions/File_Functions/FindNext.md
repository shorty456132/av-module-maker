# FindNext

Name:

FindNext

Syntax:

SIGNED_INTEGER FindNext(FILE_INFO info)

Description:

This command continues the current directory for file(s) matching the file specification in the [FindFirst](<File_First.htm>) command.

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<File_First.htm>) for description). Must be followed by a [FindClose](<FindClose.htm>).

Return Value:

Returns 0 if a file is found matching the specification and –1 if an error occurred.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

[FILE_INFO](<File_INFO_Structure.htm>) FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

PRINT ( "%s\n", FileInfo.Name );

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FindNext.htm*
