# WaitForNewDisk

Name:

WaitForNewDisk

Syntax:

SIGNED_INTEGER WaitForNewDisk()

Description:

Waits for a compact flash card to be inserted into the control system.

See also [CheckForDisk()](<CheckForDisk.htm>).

Parameters:

None.

Return Value:

Returns 0 when a new compact flash card is installed into the control system, <0 if an error occurs.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

while(1)

{

if ( WaitForNewDisk() < 0 )

break;

// perform operations on the new disk. Read a file, etc.

}

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/WaitForNewDisk.htm*
