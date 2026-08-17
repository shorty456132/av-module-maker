# MakeDirectoryShared

Name:

MakeDirectoryShared

Syntax:

SIGNED_INTEGER MakeDirectoryShared(STRING DirName)

Description:

Creates a shared directory with the specified name. The path can be [relative](<../../General_Information/Relative_Path_Names_for_Files.htm>) or absolute.

NOTE: You cannot use MakeDirectoryShared to create directories in the NVRAM or internal flash. You can only make directories in compact flash.

Parameters:

DIRNAME – string containing the name of the desired directory.

Return Value:

Returns 0 if successful. Returns 0 or a [File Function Error Code](<File_Function_Return_Error_Codes.htm>) if unsuccessful.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

IF( MakeDirectoryShared("NewDirect") < 0)

PRINT("Error occurred creating directory\n");

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v <> and above

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/MakeDirectoryShared.htm*
