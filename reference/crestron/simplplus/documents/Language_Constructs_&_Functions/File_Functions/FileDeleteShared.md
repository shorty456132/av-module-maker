# FileDeleteShared

Name:

FileDeleteShared

Syntax:

SIGNED_INTEGER FileDeleteShared (STRING filename)

Description:

Deletes the specified shared file from the file system.

[FindFirstShared](<FindFirstShared.htm>) and [FileOpenShared](<FileOpenShared.htm>) should be used in conjunction with FileDeleteShared when necessary.

NOTE: Refer to the [File Functions Overview](<File_Functions_Overview.htm>) topic statement on [Shared File Functions](<File_Functions_Overview.htm#SharedFileFunctions>) for more information.

Parameters:

FILENAME specifies the name of the file to delete. Can contain wildcards (*) if a full path is not given.

Return Value:

Returns 0 if successful. Otherwise, file [error code](<File_Function_Return_Error_Codes.htm>) is returned.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

StartFileOperations(); 

IF ( FileDeleteShared ( "\\\CF0\\\MyFile" ) <> 0 )

PRINT ( "Error deleting file\n" );

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v <> and above

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/FileDeleteShared.htm*
