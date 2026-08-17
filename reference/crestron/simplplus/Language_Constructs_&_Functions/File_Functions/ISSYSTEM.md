# IsSystem

Name:

IsSystem

Syntax:

INTEGER IsSystem(FILE_INFO info)

Description:

This routine returns whether the specified file is a system file. Equivalent to checking attributes in [FILE_INFO](<File_INFO_Structure.htm>).

Parameters:

INFO – structure containing the information about a found file (see [FindFirst](<File_First.htm>) for description).

Return Value:

Returns 1 if file is a system file and 0 if otherwise.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

[FILE_INFO](<File_INFO_Structure.htm>) FileInfo;

SIGNED_INTEGER Found;

StartFileOperations();

Found = FindFirst("*.dat", FileInfo );

WHILE (Found = 0)

{

if (IsSystem(FileInfo))

PRINT( "%s is a system file\n", FileInfo.Name );

Found = FindNext(FileInfo);

}

IF ( FindClose() < 0 )

PRINT ( "Error in closing find operation\n" );

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/ISSYSTEM.htm*
