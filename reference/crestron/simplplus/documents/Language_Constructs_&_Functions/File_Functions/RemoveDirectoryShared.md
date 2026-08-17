# RemoveDirectoryShared

Name:

RemoveDirectoryShared

Syntax:

SIGNED_INTEGER RemoveDirectoryShared(STRING DirName)

Description:

Removes the shared directory with the specified name. The path name can be [relative](<../../General_Information/Relative_Path_Names_for_Files.htm>) or absolute. Must be empty. Requires [StartFileOperations](<StartFileOperations.htm>).

Parameters:

DIRNAME – string containing the name of the desired directory.

Return Value:

Returns 0 if successful and –1 if an error occurred.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

IF( RemoveDirectoryShared("\\\CF0\\\NewDirect") < 0)

PRINT("Error occurred deleting directory\n");

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v <> and above

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/RemoveDirectoryShared.htm*
