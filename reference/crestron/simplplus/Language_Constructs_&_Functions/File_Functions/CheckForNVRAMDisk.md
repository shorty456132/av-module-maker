# CheckForNVRAMDisk

Name:

CheckForNVRAMDisk

Syntax:

INTEGER CheckForNVRAMDisk()

Description:

Tests whether or not an NVRam Disk is currently installed in the control system.

Parameters:

None.

Return Value:

Returns 1 if an NVRam Disk is currently installed in the control system.

Example:

(refer to [File Functions Overview](<File_Functions_Overview.htm>))

IF ( CheckForNVRAMDisk() = 1 )

PRINT ( "NVRAM Disk found" );

Version:

X Generation: Not Supported

2-Series: SIMPL v2.04.11 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/CheckForNVRAMDisk.htm*
