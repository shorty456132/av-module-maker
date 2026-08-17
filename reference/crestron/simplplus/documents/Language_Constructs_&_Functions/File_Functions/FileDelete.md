# FileDelete

Name:

FileDelete

Syntax:

SIGNED_INTEGER FileDelete (STRING filename)

Description:

Deletes the specified file from the file system.

[FileOpen](<FileOpen.htm>) and [FindFirst](<File_First.htm>) should be used in conjunction with FileDelete when necessary.

NOTE: Refer to the [File Functions Overview](<File_Functions_Overview.htm>) topic statement on [Shared File Functions](<File_Functions_Overview.htm#SharedFileFunctions>) for more information.

Parameters:

FILENAME specifies the name of the file to delete. Can contain wildcards (*) if a full path is not given.

Return Value:

Returns 0 if successful. Otherwise, file [error code](<File_Function_Return_Error_Codes.htm>) is returned.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

StartFileOperations(); 

IF ( FileDelete ( "\\\CF0\\\MyFile" ) <> 0 )

PRINT ( "Error deleting file\n" );

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FileDelete.htm*
