# CheckForDisk

Name:

CheckForDisk

Syntax:

INTEGER CheckForDisk()

Description:

Tests whether or not a compact flash card is currently installed in the control system.

Parameters:

None.

Return Value:

Returns 1 if a compact flash card is currently installed in the control system.

see also [WaitForNewDisk](<WaitForNewDisk.htm>)()

Example:

(see [File Functions Overview](<File_Functions_Overview.htm>))

StartFileOperations(); // all file operations must first identify themselves with the operating system

IF ( CheckForDisk () = 1 )

PRINT ( "compact flash card found" );

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/CheckForDisk.htm*
