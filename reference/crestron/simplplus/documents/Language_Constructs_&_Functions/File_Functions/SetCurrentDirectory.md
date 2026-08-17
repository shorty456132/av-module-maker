# SetCurrentDirectory

Name:

SetCurrentDirectory

Syntax:

SIGNED_INTEGER SetCurrentDirectory(STRING DirName)

Description:

Changes the working directory to the specified name. Refer to [Relative Path Names](<../../General_Information/Relative_Path_Names_for_Files.htm>).

Parameters:

DIRNAME – string containing the name of the desired directory.

Return Value:

Returns 0 if successful and –1 if an error occurred.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

IF( SetCurrentDirectory("\\\CF0\\\NewDirect") < 0)

PRINT("Error occurred creating directory\n");

PRINT("Directory is now: %s\n", GetCurrentDirectory());

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/SetCurrentDirectory.htm*
