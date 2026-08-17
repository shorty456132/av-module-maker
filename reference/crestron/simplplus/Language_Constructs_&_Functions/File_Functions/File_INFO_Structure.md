# FILE_INFO Structure

Use this structure to retrieve information about a file. 

STRUCTURE FILE_INFO

{

STRING Name; // relative name of the found file

INTEGER iAttributes; // attributes for the file

INTEGER iTime; // file time in packed form

INTEGER iDate; // file date in packed form

LONG_INTEGER lSize; // size of the file in bytes

};

File Attribute Bit Flags (These may be bitwise OR'ed together)

KEYWORD |  ATTRIBUTE |  EQUIVALENT SIMPL+ FUNCTION  
---|---|---  
ARDONLY |  File is marked read only |  IsReadOnly  
AHIDDEN |  File is hidden |  IsHidden  
ASYSTEM |  File is marked as a system file |  IsSystem  
AVOLUME |  File is a volume label |  IsVolume  
ADIRENT |  File is a directory |  IsDirectory  
ARCHIVE |  File is marked as an archive |   
  
NOTE: For an example on how and where to use the FILE_INFO structure, refer to the example code for [FindFirst](<File_First.htm>).

Version:

SIMPL+ Version 3.00.02 or higher (2-series only)

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/File_INFO_Structure.htm*
