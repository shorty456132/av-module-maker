# GetCurrentDirectory

Name:

GetCurrentDirectory

Syntax:

STRING GetCurrentDirectory()

Description:

Returns the complete path name of the current working directory. Refer to [Relative Path Names](<../../General_Information/Relative_Path_Names_for_Files.htm>) for a discussion of setting the current directory. It ends with "\".

Parameters:

None.

Return Value:

String containing the current directory. If an error occurs, string length equals 0.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

PRINT( "The current directory = %s\n", GetCurrentDirectory());

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/GetCurrentDirectory.htm*
