# MakeDirectory

Name:

MakeDirectory

Syntax:

SIGNED_INTEGER MakeDirectory(STRING DirName)

Description:

Creates a directory with the specified name. The path can be [relative](<../../General_Information/Relative_Path_Names_for_Files.htm>) or absolute.

NOTE: You cannot use MakeDirectory to create directories in the NVRAM or internal flash. You can only make directories in compact flash.

Parameters:

DIRNAME – string containing the name of the desired directory.

Return Value:

Returns 0 if successful. Returns 0 or a [File Function Error Code](<File_Function_Return_Error_Codes.htm>) if unsuccessful.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

IF( MakeDirectory("NewDirect") < 0)

PRINT("Error occurred creating directory\n");

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/MakeDirectory.htm*
